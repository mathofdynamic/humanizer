# Proposed reference diffs

## Summary of changes

- `references/patterns.md` — tighten the status/action correction and require source-specific support for broad evaluative language in marketing, abstract claims, and academic significance.
- `references/voice-and-intervention.md` — add cushioning based on bad news, imposition, or apology rather than presumed closeness; clarify that `REWRITE` does not authorize new propositions.
- `references/quality-check.md` — add speech act as a semantic invariant and hard failure; check unsupported additions, procedure order/warning attachment, and exact support for evaluative claims.
- `references/genre-matrix.md` — distinguish ordered procedures with inline warnings from simple condition-to-consequence instructions; make claim scope/support explicit for news and marketing.
- `references/evaluation.md` — add a separate post-ranking fabrication check so natural-sounding additions do not become preference signals.
- No separate changes proposed for `references/translationese.md` or `references/persian-style.md`; their existing guidance already covers information flow, causal preservation, direct predicates, and register. The narrower additions belong in the files above and should not be duplicated.

## Rule: Lead with the real status or action

**Target file**: `references/patterns.md`

**Current relevant section**:

> ## 6. Institutional ceremony in the wrong channel
>
> **Correction:** state the fact, status, or action directly while preserving appropriate politeness.
>
> **Forbidden transformation / semantic risk:** do not make support curt or remove required etiquette.

**Proposed change**:

Replace the correction line with:

> **Correction:** lead with the source's content-bearing event, status, action, or request instead of a wrapper. Then retain the context, details, and courtesy the reader needs; do not imply a status or next step absent from the source.

**Rationale**: Subjects 1, 4, 5, 6, 10, 18, and 20 favor status/action-first wording; Subjects 11 and 25 are excluded because their rankings contain a speech-act regression or unsupported addition.

## Rule: Preserve the source speech act

**Target file**: `references/quality-check.md`

**Current relevant section**:

> ## 2. Semantic ledger
>
> Check:
>
> - **action:** what actually happened or is required?
> - **obligation:** did legal, policy, or procedural force change?
>
> ## 7. Hard-failure conditions
>
> - shifts the communicative function by casualizing/formalizing the text;

**Proposed change**:

Add this item to the semantic ledger after `action`:

> - **speech act:** does the rewrite preserve whether the source requests, asks, asserts, offers, or instructs, along with the addressee and requested response?

Add this hard-failure bullet, retaining the existing bullet about shifts caused by casualizing/formalizing:

> - changes the source's speech act or requested response, such as turning a request to issue a document into a question about the procedure;

**Rationale**: Subject 11’s B > A ranking is a confirmed error: B changes a request for transcript issuance into a question about procedure. `quality-check.md` is the best home because it already defines semantic invariants and hard failures; this is not merely a voice or register preference, so a new file is unnecessary.

## Rule: Cushion face-threats, not every informal message

**Target file**: `references/voice-and-intervention.md`

**Current relevant section**:

> ## 1. Voice fingerprints
>
> | Fingerprint | Default |
> |---|---|
> | politeness level | protect unless channel clearly requires correction |
> | emotional intensity | protect |
>
> Do not create a generic "better Persian voice." Recover this writer's best version of the existing voice.

**Proposed change**:

Insert after the table and before the final paragraph:

> Choose cushioning by communicative burden, not presumed relationship closeness. Soften bad news, apologies, impositions, and potentially unwelcome requests; keep neutral logistics direct even between close contacts. Then fit the degree of formality to the channel.

**Rationale**: The human identifies Subject 3’s cancellation and apology as requiring cushioning, while Subject 18’s neutral scheduling exchange calls for directness regardless of sibling closeness. This pragmatic distinction fits the voice guidance; the genre and Persian-style files already establish audience-appropriate register and need no duplicate rule.

## Rule: Use the smallest sufficient rewrite and reject unsupported additions

**Target files**: `references/voice-and-intervention.md`; `references/quality-check.md`; `references/evaluation.md`

**Current relevant sections**:

> `references/quality-check.md`, ## 3. Unsupported-information hard gate:
>
> The rewrite must not add:
>
> - facts, examples, statistics, metrics, dates, deadlines
> - actors or mechanisms not identified by the source
> - customer reactions, market position, guarantees, promises
> - personal experience, opinion, emotion, or uncertainty
>
> `references/voice-and-intervention.md`, ## 2. Intervention gate, REWRITE:
>
> Rewrite only the affected span.
>
> `references/evaluation.md`, ## 5. Pairwise evaluation:
>
> Use blinded randomized comparisons for the holistic question:
>
> > Which version reads as more natural Persian for this exact audience and genre without changing what the writer meant?
>
> Then collect separate ratings for semantic preservation, register, voice, mechanics, and unnecessary intervention.

**Proposed change**:

In `voice-and-intervention.md`, append this sentence after “Rewrite only the affected span”:

> A structural rewrite does not authorize new facts, examples, actors, or follow-up intentions absent from the source or explicit user instruction.

In `quality-check.md`, append this question to the numbered list in `## 4. Intervention audit`:

> 6. Does any changed span add an example, actor, motive, promise, observation, or follow-up intention absent from the source and not explicitly authorized? If so, remove it or mark the span `FLAG`.

In `evaluation.md`, insert after the paragraph beginning “Then collect separate ratings”:

> After recording the initial preference, compare the selected candidate with the original in a separate fabrication check. Flag any added example, actor, intention, promise, or other proposition the source does not support. A natural-sounding addition is still a hard failure, not a positive preference signal; mark the case for correction or re-judgment.

**Rationale**: Subjects 13 and 25’s added example and follow-up intention were ranking blind spots, not accepted preferences. The intervention gate prevents broad rewriting from being treated as permission; the quality gate makes the check actionable during editing, and evaluation adds a separate check after pairwise judging.

## Rule: Preserve semantic invariants and match instruction structure to dependency

**Target files**: `references/genre-matrix.md`; `references/quality-check.md`

**Current relevant sections**:

> `references/genre-matrix.md`, Technical documentation row:
>
> | Technical documentation | stable terms, direct imperatives/declaratives | exact term repetition is desirable | synonym rotation, translating identifiers | code, commands, API names, sequence, warnings |
>
> `references/quality-check.md`, ## 2. Semantic ledger:
>
> - **condition:** did an `اگر`, prerequisite, limitation, or exception disappear?
>
> If any material difference is not explicitly requested, revert it.

**Proposed change**:

Replace the Technical documentation row with:

> | Technical documentation | stable terms, direct imperatives/declaratives; compact condition-to-consequence wording for a single prerequisite | exact term repetition is desirable; use prose when order-dependent steps and an inline warning need to stay together | synonym rotation, translating identifiers, or fragmenting dependent steps | code, commands, API names, sequence, warnings |

Add this item to the semantic ledger after `condition`:

> - **sequence / warning attachment:** are dependent steps still in order, and does each warning remain attached to the step it qualifies?

**Rationale**: Subjects 8 and 20 are simple condition-to-consequence cases; Subject 16 is an order-dependent restore procedure whose warning should stay with its sequence. The distinction is dependency and warning placement, not task length. `translationese.md` already protects causal and technical meaning, so no duplicate change is proposed there.

## Rule: Keep evaluative language only when specifics substantiate it

**Target files**: `references/patterns.md`; `references/genre-matrix.md`; `references/quality-check.md`

**Current relevant sections**:

> `references/patterns.md`, ## 10. Unsupported marketing filler:
>
> **False positives / genre license:** deliberate brand voice, slogans, campaigns, or explicitly hyperbolic copy.
>
> **Correction:** use a source-supported capability or benefit; otherwise remove or soften the adjective.
>
> `references/patterns.md`, ## 11. Pseudo-profundity and abstraction cascade:
>
> **Correction:** recover the supported actor/action/outcome or keep the metaphor only when it is actually part of the writer's voice.
>
> `references/patterns.md`, ## 16. Academic significance inflation:
>
> **Correction:** preserve measured uncertainty and scope the claim to the reported conditions.
>
> `references/genre-matrix.md`, Journalism/news and Marketing/advertising rows:
>
> | Journalism/news | event/actor/time/consequence orientation | repeated names may support attribution | essay framing or marketing tone | attribution, chronology, uncertainty |
> | Marketing/advertising | brand voice, compressed syntax, persuasion | slogan rhythm and intentional repetition can be valid | neutralizing persuasion or inventing proof | claims, slogans, CTA, brand terms |
>
> `references/quality-check.md`, ## 5. Register and voice:
>
> - marketing still persuades without invented evidence;

**Proposed change**:

In `patterns.md`, replace the false-positive and correction lines in `## 10` with:

> **False positives / genre license:** a requested slogan may keep its rhetorical form, but marketing genre alone does not substantiate a factual evaluation.
>
> **Correction:** keep a broad descriptor only when concrete details in the source substantiate the exact claim it summarizes. Otherwise remove it; do not replace it with another unsupported benefit.

In `patterns.md`, replace the correction line in `## 11` with:

> **Correction:** recover the supported actor/action/outcome; keep the metaphor only when it is actually part of the writer's voice; retain broad benefit language only when source details substantiate the exact claim.

Replace the correction line in `## 16` with:

> **Correction:** preserve measured uncertainty and scope each significance claim to the reported conditions; retain it only when the study design, data, and cited evidence support that exact claim.

In `genre-matrix.md`, replace the Journalism/news row with:

> | Journalism/news | event/actor/time/consequence orientation | repeated names may support attribution | essay framing or marketing tone | attribution, chronology, uncertainty, claim scope |

Replace the Marketing/advertising row with:

> | Marketing/advertising | brand voice, compressed syntax, persuasion | slogan rhythm and intentional repetition can be valid | neutralizing persuasion or inventing proof | claims only when substantiated by source details, slogans, CTA, brand terms |

In `quality-check.md`, add this item to the checklist in `## 5. Register and voice`:

> - retain a broad evaluative claim only when concrete source details support its exact scope; otherwise remove or narrow it without inventing proof;

**Rationale**: Subject 2’s “comprehensive” summarizes its enumerated functions; the superlatives and impact claims in Subjects 6, 12, 15, and 21 lack details that substantiate those exact evaluations. The pattern catalog gives genre-specific diagnostics, while the quality check applies the substantiation test across genres.
