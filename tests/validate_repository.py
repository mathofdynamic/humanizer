"""Validate the Humanizer skill without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "agents/openai.yaml",
    "references/patterns.md",
    "references/persian-style.md",
    "references/quality-check.md",
    "references/translationese.md",
    "references/genre-matrix.md",
    "references/voice-and-intervention.md",
    "references/evaluation.md",
    "tests/examples.md",
    "tests/edge-cases.md",
    "tests/benchmark-fixtures.json",
    "tests/validate_repository.py",
)

MOJIBAKE_MARKERS = (
    chr(0xFFFD),
    chr(0x00C3),
    chr(0x00C2),
    chr(0x00E2),
    chr(0x00F0),
    chr(0x00D9),
)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)")
PATH_REFERENCE = re.compile(r"`((?:references|agents|scripts|assets|tests)/[^`\s]+)`")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
JUNK_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
JUNK_DIRS = {"__pycache__", ".pytest_cache", "node_modules", ".venv", "venv"}
BINARY_ASSET_SUFFIXES = {".avif", ".gif", ".jpeg", ".jpg", ".pdf", ".png", ".webp"}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def validate() -> list[str]:
    errors: list[str] = []
    files = [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]

    for required in REQUIRED_FILES:
        if not (ROOT / required).is_file():
            errors.append(f"missing required file: {required}")

    text_by_path: dict[Path, str] = {}
    for path in files:
        if path.name in JUNK_NAMES or path.suffix.lower() in {".pyc", ".pyo", ".tmp", ".bak"}:
            errors.append(f"temporary or generated file present: {relative(path)}")
        if any(part in JUNK_DIRS for part in path.parts):
            errors.append(f"temporary or generated directory present: {relative(path)}")
        if path.suffix.lower() in BINARY_ASSET_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"not valid UTF-8: {relative(path)} ({exc})")
            continue
        text_by_path[path] = text

        for character in text:
            if unicodedata.category(character) == "Cf" and character != "\u200c":
                errors.append(f"hidden formatting character U+{ord(character):04X} in {relative(path)}")
            if character == chr(0xFFFD):
                errors.append(f"replacement character U+FFFD in {relative(path)}")

        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                errors.append(f"possible mojibake marker {marker!r} in {relative(path)}")

    skill_text = text_by_path.get(ROOT / "SKILL.md", "")
    validate_frontmatter(skill_text, errors)
    validate_relative_references(text_by_path, errors)
    validate_markdown_structure(text_by_path, errors)
    validate_ui_metadata(text_by_path, errors)
    validate_benchmark(errors)
    return errors


def validate_frontmatter(text: str, errors: list[str]) -> None:
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
        return
    closing = text.find("\n---", 4)
    if closing == -1:
        errors.append("SKILL.md frontmatter has no closing delimiter")
        return

    values: dict[str, str] = {}
    for line in text[4:closing].splitlines():
        if not line or line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')

    name = values.get("name", "")
    description = values.get("description", "")
    if not SKILL_NAME.fullmatch(name):
        errors.append(f"invalid skill name in SKILL.md: {name!r}")
    if name != ROOT.name:
        errors.append(f"skill name {name!r} does not match directory {ROOT.name!r}")
    if not 1 <= len(description) <= 1024:
        errors.append("SKILL.md description must contain 1-1024 characters")


def validate_relative_references(text_by_path: dict[Path, str], errors: list[str]) -> None:
    for path, text in text_by_path.items():
        if path.suffix.lower() not in {".md", ".yaml", ".yml"}:
            continue
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if target and not (path.parent / target).is_file():
                errors.append(f"broken relative link in {relative(path)}: {target}")
        for match in PATH_REFERENCE.finditer(text):
            target = match.group(1)
            if not (ROOT / target).is_file():
                errors.append(f"broken referenced path in {relative(path)}: {target}")


def validate_markdown_structure(text_by_path: dict[Path, str], errors: list[str]) -> None:
    examples = text_by_path.get(ROOT / "tests/examples.md", "")
    sections = re.findall(r"^## (\d+)\. ", examples, flags=re.MULTILINE)
    expected = [str(number) for number in range(1, 26)]
    if sections != expected:
        errors.append(f"tests/examples.md must contain numbered cases 1-25 in order; found {sections}")

    readme = text_by_path.get(ROOT / "README.md", "")
    for required in ("rewrite", "audit", "edit", "Codex", "Claude Code", "Limitations", "Attribution", "license"):
        if required.lower() not in readme.lower():
            errors.append(f"README.md is missing required topic: {required}")

    for path, text in text_by_path.items():
        if path.suffix.lower() != ".md":
            continue
        headings = [m.group(2).strip() for m in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", text, re.MULTILINE)]
        duplicates = sorted(h for h, count in Counter(headings).items() if count > 1)
        for heading in duplicates:
            errors.append(f"duplicate Markdown heading in {relative(path)}: {heading}")


def validate_ui_metadata(text_by_path: dict[Path, str], errors: list[str]) -> None:
    text = text_by_path.get(ROOT / "agents/openai.yaml", "")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s+{key}:\s+\".+\"\s*$", text, flags=re.MULTILINE):
            errors.append(f"agents/openai.yaml must quote interface.{key}")
    if "$humanizer" not in text:
        errors.append("agents/openai.yaml default_prompt must mention $humanizer")


def validate_benchmark(errors: list[str]) -> None:
    path = ROOT / "tests/benchmark-fixtures.json"
    if not path.is_file():
        return
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in tests/benchmark-fixtures.json: {exc}")
        return

    required = {
        "id", "input", "genre", "register", "audience", "expected_intervention",
        "known_diagnoses", "protected_spans", "semantic_invariants",
        "voice_fingerprints", "forbidden_transformations"
    }
    allowed = {"KEEP", "MINOR", "REWRITE", "FLAG"}
    ids: set[str] = set()
    for index, case in enumerate(cases):
        missing = required - case.keys()
        if missing:
            errors.append(f"benchmark case {index} missing fields: {sorted(missing)}")
        if case.get("expected_intervention") not in allowed:
            errors.append(f"benchmark case {index} has invalid intervention")
        case_id = case.get("id")
        if case_id in ids:
            errors.append(f"duplicate benchmark id: {case_id}")
        ids.add(case_id)


def main() -> int:
    errors = validate()
    if errors:
        print("Humanizer validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Humanizer validation passed: {len(REQUIRED_FILES)} required files, UTF-8, links, frontmatter, references, 25 behavioral tests, benchmark fixtures, and junk-file checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
