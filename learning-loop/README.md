# Humanizer learning loop

This folder is a human-preference benchmark for improving the Persian Humanizer skill. It is not an authorship or AI-detector benchmark. The goal is to learn which faithful, context-sensitive edits a human Persian editor prefers.

## Purpose

Each round generates diverse, intentionally flawed Persian samples, produces multiple rewrites of each sample using distinct Humanizer strategies, asks a human to choose or rank the acceptable outputs, and turns the human's reasoning into reusable rules. Repeating the process across rounds tests whether the skill is converging on the same decisions the human would make.

The samples are synthetic benchmark material written in realistic everyday contexts. Calling a sample “AI-sounding” describes the target writing pathology, not a claim about its provenance.

## Round design

- Every round contains exactly 25 subjects.
- Subjects are open and real-world-style, not a fixed genre-matrix grid. Examples include emails, product descriptions, social posts, essays, technical explanations, personal notes, news-style writing, support replies, formal requests, reports, and community messages.
- Each subject has one fixed bad/original Persian sample and three or four rewrites of that same sample.
- The bad sample should normally be 200–400 characters and should contain a plausible cluster of problems: translationese, bureaucratic padding, generic framing, mechanical connectors, unsupported praise, over-explanation, register collision, weak reference continuity, or another pattern documented by the skill.
- Candidate labels state the intervention that produced the rewrite. The labels are part of the experiment; they are not claims that one strategy is always correct.
- Candidates must preserve meaning, names, numbers, dates, links, quotations, terminology, uncertainty, attribution, causality, scope, capability, obligation, and observable voice unless the scenario explicitly authorizes a change.

The relevant strategy vocabulary comes from the skill and its references:

- `KEEP`: leave already-natural or contextually licensed wording unchanged.
- `MINOR`: make only local wording, punctuation, reference, or register repairs.
- `REWRITE`: change sentence or paragraph structure when the structure itself is the problem.
- `FLAG`: avoid guessing when a safe edit requires missing facts, intent, legal interpretation, or fixed specialist wording.
- Translationese repair: fix English-shaped information flow, overt-subject carryover, literal predicates, heavy noun chains, and passive organization only when the context supports the repair.
- Voice-first editing: preserve contractions, bluntness, humor, hedging, emotional intensity, first-person habits, and code-switching when they belong to the writer.
- Genre-matrix editing: fit the exact channel and audience without equating natural Persian with casual Persian. Technical terms, academic hedges, formal etiquette, support commitments, and marketing claims each have different constraints.

The references used to design the candidates include /references/patterns.md, /references/translationese.md, /references/voice-and-intervention.md, /references/persian-style.md, /references/genre-matrix.md, and /references/quality-check.md.

## Per-subject workflow

1. Freeze the bad/original sample. Do not silently revise it after judgments begin.
2. Produce three or four candidates for the same input. Make the strategy and intervention level explicit in each heading.
3. Check each candidate against the semantic ledger before human review: actor, action, object, polarity, modality, quantity, date, condition, causality, scope, attribution, capability, obligation, protected terms, and voice.
4. Have the human choose exactly one winner, or rank two or more acceptable candidates from best to worst. A tie is not a valid final response unless the candidates are listed in preference order.
5. Require a specific reason tied to a decision: for example, preserved a necessary hedge, removed a literal predicate without changing the claim, retained a support commitment, kept a colloquial voice, or correctly left a genre-licensed formal phrase alone.
6. Record what was wrong with rejected candidates. “Sounds better” alone is not enough for rule extraction.

The human may prefer the original in a future round if a candidate over-edits it. `KEEP` is a valid outcome. A polished candidate that changes facts, modality, causality, register, protected terminology, or voice is not acceptable merely because it sounds smoother.

## Human judgment and rule extraction

`judgments.md` is the only round file that the human fills in. For every subject, record the winner or ordered acceptable list, the concrete reason, the weakness of each rejected candidate, and confidence (`low`, `medium`, or `high`). Judge naturalness for the exact audience and genre, while separately watching semantic preservation, register, voice, fluency, structure, mechanics, and unnecessary intervention.

After a round is judged:

1. Extract recurring decisions into `extracted-rules.md`.
2. Convert each proposed rule into a small, reviewable diff to the appropriate file under /references/*.md or to a new /references/learned-patterns.md.
3. Include the triggering examples, the genre or register boundary, the smallest justified correction, and the semantic failure mode to avoid.
4. Have the human review the proposed diffs.
5. Merge only the reviewed rules. Do not treat an unreviewed preference as a universal Persian rule.

Do not optimize for lexical variety, sentence-length distributions, artificial “burstiness,” or AI-detector scores. The loop should learn contextual editing decisions, not manufacture human-like noise.

## Repeat rounds and convergence

Rounds 2 and 3 each contain 3–5 repeat subjects copied from round 1: the same subject description and exactly the same bad/original text. The remaining subjects are new, so the round still totals 25. Keep repeat inputs byte-for-byte stable and clearly mark them as repeats in the round's subject inventory.

For repeat subjects, compare the newly generated candidates with the earlier human preference. The purpose is to test whether newly learned rules cause the preferred decision to reappear, not to reward superficial reuse of the old winning wording. Track:

- whether the same candidate strategy wins again;
- whether the human's reason is stable or changes by context;
- whether a learned rule fixes the old failure without creating semantic or register regressions;
- whether the human increasingly prefers one bounded intervention level, including `KEEP`;
- whether new subjects expose an overfit rule.

After round 3, review the repeat outcomes and new-subject outcomes together. A rule is a convergence candidate only when it generalizes across relevant contexts, has a clear exception boundary, and survives the protected-span and semantic checks.

## Files

- `round-1/subjects.md`: 25 one-line scenario descriptions.
- `round-1/candidates.md`: fixed originals and labeled candidate rewrites.
- `round-1/judgments.md`: empty human-review template.
- `round-1/extracted-rules.md`: filled only after the human completes the judgments.

Future rounds should use the same four-file shape and should preserve a clear link from every repeat subject to its round-1 source.
