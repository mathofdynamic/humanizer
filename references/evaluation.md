# Evaluation Protocol

Humanizer v2 should be evaluated as an editor, not as an authorship detector.

## 1. Benchmark strata

Include examples across both pathology and genre.

Quality/pathology labels:

- obvious formulaic or AI-slop-like prose
- mildly unnatural Persian
- translationese
- bureaucratic padding
- over-marketed prose
- already-natural Persian
- intentionally formal Persian
- colloquial Persian
- factual/citation-heavy text
- difficult semantic edge cases

Genre labels:

- conversation
- semi-formal
- business
- article/blog
- news
- academic
- technical
- product documentation
- marketing
- social media
- support
- corporate report
- formal letter
- administrative/government
- opinion/editorial

Do not learn "formal = bad." Pathology and genre are separate metadata.

## 2. Benchmark case schema

A useful case records:

- `id`
- `input`
- `genre`
- `register`
- `audience`
- `expected_intervention`: `KEEP`, `MINOR`, `REWRITE`, or `FLAG`
- `known_diagnoses`
- `protected_spans`
- `semantic_invariants`
- `voice_fingerprints`
- `forbidden_transformations`

Avoid a single "gold rewrite." Natural editing can have several valid outputs.

Machine-readable starter fixtures live in `tests/benchmark-fixtures.json`.

## 3. Human rating dimensions

Use anchored 0-4 ratings.

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Naturalness | clearly unnatural | mixed | fully natural for context |
| Semantic preservation | major drift | minor drift | proposition/modality preserved |
| Register preservation | wrong communicative function | mixed | precise genre fit |
| Voice preservation | writer erased | partly retained | same writer, better edited |
| Fluency | difficult/incorrect | acceptable | effortless |
| Concision appropriateness | bloated/destructive | mixed | right amount for genre |
| Structural naturalness | strongly templated | mixed | structure follows information |
| Persian mechanics | repeated issues | minor issues | correct and register-sensitive |
| Unnecessary editing | extensive needless change | some needless change | every changed span justified |

Unsupported information is also a hard gate, not merely a score.

## 4. Hard failures

Fail an output regardless of style score when it:

- changes a protected name, number, date, citation, quotation, identifier, code token, path, or URL;
- invents a fact, metric, example, causal relation, deadline, capability, source, or experience;
- changes material uncertainty, condition, scope, legal obligation, or technical behavior;
- corrupts tables or Markdown semantics;
- renames stable technical terminology without authorization;
- changes register enough to alter the communicative function.

## 5. Pairwise evaluation

Use blinded randomized comparisons for the holistic question:

> Which version reads as more natural Persian for this exact audience and genre without changing what the writer meant?

Useful comparisons:

- Original vs v1
- Original vs v2
- v1 vs v2

Then collect separate ratings for semantic preservation, register, voice, mechanics, and unnecessary intervention.

For already-natural cases, ask:

> Is the rewrite actually better than the original?

A tie or preference for the original is compatible with a correct `KEEP` decision.

## 6. Initial release criteria

These are engineering targets, not universal linguistic laws.

- zero critical semantic violations in release-blocking fixtures;
- exact protected-span preservation unless explicitly editable;
- zero invented factual claims in factual fixtures;
- v2 should show a reliable preference over v1 on diagnosed slop/translationese cases;
- no systematic disadvantage to the original on already-natural cases;
- `KEEP` cases should normally remain unchanged except explicitly permitted mechanical fixes;
- no systematic casualization of academic, formal, administrative, or legal-adjacent text;
- no systematic loss of observable writer voice.

Refresh benchmark cases periodically so the skill does not overfit a fixed list.
