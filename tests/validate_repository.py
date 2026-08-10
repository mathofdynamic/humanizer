"""Validate the Humanizer skill without third-party dependencies."""

from __future__ import annotations

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
    "tests/examples.md",
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


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def validate() -> list[str]:
    errors: list[str] = []
    files = [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]

    for required in REQUIRED_FILES:
        path = ROOT / required
        if not path.is_file():
            errors.append(f"missing required file: {required}")

    for path in files:
        if path.name in JUNK_NAMES or path.suffix.lower() in {".pyc", ".pyo", ".tmp", ".bak"}:
            errors.append(f"temporary or generated file present: {relative(path)}")
        if any(part in JUNK_DIRS for part in path.parts):
            errors.append(f"temporary or generated directory present: {relative(path)}")

    text_by_path: dict[Path, str] = {}
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"not valid UTF-8: {relative(path)} ({exc})")
            continue
        text_by_path[path] = text

        for character in text:
            if unicodedata.category(character) == "Cf" and character != "\u200c":
                codepoint = f"U+{ord(character):04X}"
                errors.append(f"hidden formatting character {codepoint} in {relative(path)}")
            if character == chr(0xFFFD):
                errors.append(f"replacement character U+FFFD in {relative(path)}")

        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                errors.append(f"possible mojibake marker {marker!r} in {relative(path)}")

    skill_path = ROOT / "SKILL.md"
    skill_text = text_by_path.get(skill_path, "")
    validate_frontmatter(skill_text, errors)
    validate_relative_references(text_by_path, errors)
    validate_markdown_structure(text_by_path, errors)
    validate_ui_metadata(text_by_path, errors)
    return errors


def validate_frontmatter(text: str, errors: list[str]) -> None:
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
        return

    closing = text.find("\n---", 4)
    if closing == -1:
        errors.append("SKILL.md frontmatter has no closing delimiter")
        return

    header = text[4:closing].splitlines()
    values: dict[str, str] = {}
    for line in header:
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
    if "compatibility" in values and not 1 <= len(values["compatibility"]) <= 500:
        errors.append("SKILL.md compatibility must contain 1-500 characters")


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
    examples_path = ROOT / "tests/examples.md"
    examples = text_by_path.get(examples_path, "")
    sections = re.findall(r"^## (\d+)\. ", examples, flags=re.MULTILINE)
    expected = [str(number) for number in range(1, 16)]
    if sections != expected:
        errors.append(f"tests/examples.md must contain numbered cases 1-15 in order; found {sections}")

    required_headings = (
        "Overly formal Persian",
        "Generic AI-style blog introduction",
        "Marketing copy",
        "Customer-support message",
        "Telegram or social-media text",
        "Academic writing",
        "Technical documentation",
        "Translated-English Persian",
        "Bullet-heavy writing",
        "Repetitive transitions",
        "Already-good Persian",
        "Intentionally colloquial Persian",
        "Persian mixed with English technical terminology",
        "Quoted material that must remain untouched",
        "Factual and citation-heavy text",
    )
    for heading in required_headings:
        if f". {heading}" not in examples:
            errors.append(f"missing test heading: {heading}")

    readme = text_by_path.get(ROOT / "README.md", "")
    for required in ("rewrite", "audit", "edit", "Codex", "Claude Code", "Limitations", "Attribution", "License"):
        if required not in readme:
            errors.append(f"README.md is missing required topic: {required}")
    if "<YOUR_REPO_URL>" in readme:
        errors.append("README.md still contains a repository URL placeholder")

    for path, text in text_by_path.items():
        if path.name not in {"SKILL.md", "patterns.md", "persian-style.md", "quality-check.md"}:
            continue
        headings = [match.group(2).strip() for match in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", text, re.MULTILINE)]
        duplicates = sorted(heading for heading, count in Counter(headings).items() if count > 1)
        for heading in duplicates:
            errors.append(f"duplicate Markdown heading in {relative(path)}: {heading}")
        rules = [line.strip() for line in text.splitlines() if line.lstrip().startswith(("- ", "* "))]
        duplicate_rules = sorted(rule for rule, count in Counter(rules).items() if count > 1)
        for rule in duplicate_rules:
            errors.append(f"duplicate rule in {relative(path)}: {rule}")


def validate_ui_metadata(text_by_path: dict[Path, str], errors: list[str]) -> None:
    path = ROOT / "agents/openai.yaml"
    text = text_by_path.get(path, "")
    if not text:
        return
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s+{key}:\s+\".+\"\s*$", text, flags=re.MULTILINE):
            errors.append(f"agents/openai.yaml must quote interface.{key}")
    if "$humanizer" not in text:
        errors.append("agents/openai.yaml default_prompt must mention $humanizer")


def main() -> int:
    errors = validate()
    if errors:
        print("Humanizer validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Humanizer validation passed: {len(REQUIRED_FILES)} required files, UTF-8, links, frontmatter, references, tests, and junk-file checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
