# Humanizer

Humanizer is a Persian-first Agent Skill for refining writing that feels translated, repetitive, bureaucratic, generic, overly formal, or mechanically structured. It rewrites only as much as needed to make the Persian natural for its context while preserving meaning, facts, terminology, and the writer's voice.

It is a writing-quality tool. It does not detect authorship, promise that text is "undetectable" or "100% human," optimize detector scores, or use adversarial text tricks.

## What it improves

- Persian syntax and information flow rather than word-for-word English-shaped phrasing
- Artificial formality, bureaucratic padding, generic transitions, and empty marketing language
- Repetitive paragraph structure, bullet inflation, unnecessary headings, and decorative conclusions
- Register fit across conversational, semi-formal, formal, academic, news, marketing, technical, support, social, and blog writing
- Persian punctuation, spacing, نیم‌فاصله, and consistent use of Persian `ی` and `ک`

Humanizer does not fact-check the source. It preserves factual claims and flags uncertainty rather than inventing corrections.

## Modes

- `rewrite` (default): return an improved Persian version.
- `audit`: identify writing-quality problems without rewriting.
- `edit`: make minimal targeted edits to a named file and verify the result.

You can also specify the target register, audience, terminology to preserve, or desired degree of intervention in ordinary language.

## Install

### OpenAI Codex and other Agent Skills clients

Project-local:

```bash
git clone https://github.com/mathofdynamic/humanizer .agents/skills/humanizer
```

User-wide:

```bash
git clone https://github.com/mathofdynamic/humanizer ~/.agents/skills/humanizer
```

Create the parent directory first if it does not exist. On Windows PowerShell, for example:

```powershell
New-Item -ItemType Directory -Force .agents/skills | Out-Null
git clone https://github.com/mathofdynamic/humanizer .agents/skills/humanizer
```

### Claude Code

For Claude Code setups that load Agent Skills from `~/.claude/skills/`:

```bash
git clone https://github.com/mathofdynamic/humanizer ~/.claude/skills/humanizer
```

### Generic Agent Skills installation

Copy or clone the `humanizer/` directory into the client's Agent Skills directory. Keep `SKILL.md` at the skill root and preserve the relative `references/` paths. `agents/openai.yaml` is optional client metadata and is safe for clients that do not use it.

## Usage

Ask the agent in natural language. For example:

```text
«این متن فارسی را طبیعی‌تر کن، اما لحن رسمی و اصطلاحات فنی‌اش حفظ شود.»
```

```text
«این متن را audit کن. عبارت‌های bureaucratic، ترجمه‌وار و انتقال‌های تکراری را مشخص کن، اما بازنویسی نکن.»
```

```text
«فایل draft.md را edit کن؛ فقط جمله‌های مصنوعی را هدف بگیر و نقل‌قول‌ها، لینک‌ها و جدول‌ها را تغییر نده.»
```

If no mode is named, Humanizer uses `rewrite`. A rewrite runs one editing pass and one bounded editorial pass for fidelity, rhythm, register, and Persian orthography.

## Repository structure

```text
humanizer/
├── SKILL.md
├── agents/openai.yaml
├── README.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── references/
│   ├── patterns.md
│   ├── persian-style.md
│   └── quality-check.md
└── tests/
    ├── examples.md
    └── validate_repository.py
```

Run the dependency-free repository checks with:

```bash
python tests/validate_repository.py
```

## Limitations

- Naturalness is contextual. Good results still benefit from a stated audience and target register.
- The skill improves wording; it does not verify facts, citations, legal correctness, or subject-matter accuracy.
- Quotations, code, tables, and attributed material are protected by default and may be reported without being rewritten.
- Persian dialect, colloquial spelling, and terminology choices can be intentional; Humanizer favors preservation over blanket normalization.

## Attribution and license

Humanizer is released under the [MIT License](LICENSE).

Its pattern-auditing approach was informed by [Conor Bronsdon's `avoid-ai-writing`](https://github.com/conorbronsdon/avoid-ai-writing), which is MIT-licensed. Persian-specific rules and wording were developed independently. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for attribution and research references, including the [Agent Skills specification](https://agentskills.io/specification).
