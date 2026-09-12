# Humanizer

Humanizer is a Persian-first Agent Skill for refining writing that feels translated, repetitive, bureaucratic, generic, overly formal, mechanically structured, or mismatched to its actual genre.

Version 2 behaves like a careful native Persian editor: it diagnoses first, preserves semantic and voice invariants, and makes the smallest justified edit. Returning already-natural text unchanged is a valid success state.

It is a writing-quality tool. It does not detect authorship, promise that text is "undetectable" or "100% human," optimize detector scores, or use adversarial text tricks.

## What v2 improves

- native Persian information flow rather than word-for-word English-shaped syntax
- explicit `KEEP / MINOR / REWRITE / FLAG` intervention decisions
- stronger semantic-drift protection for uncertainty, causality, scope, capability, and obligation
- writer-voice preservation instead of generic "polishing"
- genre-aware handling across conversation, business, news, academic, technical, marketing, support, administrative, and other Persian
- structured detection of bureaucratic padding, translationese, repetitive transitions, false symmetry, over-explanation, fake precision, and generic marketing filler
- Persian punctuation, spacing, نیم‌فاصله, and character normalization as a final pass rather than a rewriting strategy

Humanizer does not fact-check the source. It preserves source claims and flags ambiguity instead of inventing corrections.

## Modes

- `rewrite` (default): run the full workflow and edit only justified defects. It may return the input unchanged.
- `audit`: diagnose material writing-quality problems without rewriting.
- `edit`: make minimal targeted edits to a named file and verify the result.

You can specify target register, audience, terminology, or intervention level in ordinary language.

## Install

### OpenAI Codex and Agent Skills clients

Project-local:

```bash
git clone https://github.com/mathofdynamic/humanizer .agents/skills/humanizer
```

User-wide:

```bash
git clone https://github.com/mathofdynamic/humanizer ~/.agents/skills/humanizer
```

### Claude Code

```bash
git clone https://github.com/mathofdynamic/humanizer ~/.claude/skills/humanizer
```

Keep `SKILL.md` at the skill root and preserve the relative `references/` paths.

## Usage

```text
«این متن فارسی را طبیعی‌تر کن، اما لحن رسمی، میزان قطعیت و اصطلاحات فنی‌اش را حفظ کن.»
```

```text
«این متن را audit کن. فقط مشکلاتی را بگو که واقعاً در این بافت نیاز به اصلاح دارند.»
```

```text
«فایل draft.md را edit کن؛ فقط بخش‌های ترجمه‌وار را اصلاح کن و نقل‌قول‌ها، لینک‌ها، اعداد و اصطلاحات فنی را دست نزن.»
```

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
│   ├── quality-check.md
│   ├── translationese.md
│   ├── genre-matrix.md
│   ├── voice-and-intervention.md
│   └── evaluation.md
└── tests/
    ├── examples.md
    ├── edge-cases.md
    ├── benchmark-fixtures.json
    └── validate_repository.py
```

Run dependency-free repository checks with:

```bash
python tests/validate_repository.py
```

## Evaluation philosophy

Do not score Humanizer with an AI detector.

The benchmark should combine:

- blind pairwise preference for natural Persian in the exact genre;
- hard semantic/protected-span gates;
- ratings for register, voice, fluency, mechanics, structure, and unnecessary intervention;
- explicit no-regression cases where the best edit is `KEEP`.

See [references/evaluation.md](references/evaluation.md).

## Limitations

- Naturalness is contextual and genre-specific.
- The skill improves wording; it does not verify facts, citations, legal correctness, or subject-matter accuracy.
- Quotations, code, data, identifiers, and fixed terminology are protected by default.
- Legal, highly technical, poetic, historical, and dialect-heavy material may require `FLAG` or very limited intervention.
- Persian-specific evidence does not justify universal "human" sentence-length, connector-frequency, or lexical-diversity targets.

## Attribution and license

Humanizer is released under the [MIT License](LICENSE).

Its pattern-auditing approach was informed by [Conor Bronsdon's `avoid-ai-writing`](https://github.com/conorbronsdon/avoid-ai-writing), which is MIT-licensed. Persian-specific rules and wording were developed independently.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for attribution and research references, including the [Agent Skills specification](https://agentskills.io/specification).
