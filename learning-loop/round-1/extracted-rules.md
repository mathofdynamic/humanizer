# Round 1 — Extracted Rules

**Evidence note:** The per-subject “Why” and candidate-note fields in `judgments.md` remain blank. The human clarifications below resolve specific comparisons; other pattern attributions remain provisional. Subject 4 also has no confidence entry.

## Rule candidates

### Rule: Lead with the real status or action
- **Statement**: Remove throat-clearing and administrative wrappers when they add no function. Put the event, status, action, or request early, while retaining the context, details, and courtesy needed for the reader to act.
- **Evidence**:
  - Subject 1 (B > C): B leads with the order and dates, then states the missing update and asks for status or cancellation.
  - Subject 4 (C > A): C asks directly for UI/test status, blockers, and a revised schedule instead of opening with coordination boilerplate.
  - Subject 5 (B > C): B states the outage and its concrete effects before asking neighbors to share updates.
  - Subject 6 (C > A): C leads with the municipality and opening, retaining the book count and study room while dropping the generic cultural preamble.
  - Subject 10 (B > A): B gives the refund status and seven-working-day expectation before the follow-up condition.
  - Subject 18 (B): B turns a formal setup into a direct moving-date/help/time question.
  - Subject 20 (B): B states the title prerequisite and save outcome in two short instructions.
- **Conflicts**: Subjects 11 and 25 are not valid support for directness: Subject 11 is a confirmed ranking error involving a changed speech act; Subject 25’s winning candidate adds an unstated follow-up intention. Both are excluded from this rule’s evidence.
- **Maps to**: `patterns.md` (bureaucratic padding; institutional ceremony), `translationese.md` (administrative inflation; English-shaped information flow), `persian-style.md`.
- **Confidence**: Medium — seven usable rankings support the pattern; four reported high confidence, two medium, and Subject 4 has no confidence entry. Two apparent supports were excluded after clarification.

### Rule: Preserve the source speech act
- **Statement**: Keep a request a request, a question a question, and a statement a statement. Restructure for directness or brevity only if the same action is still being requested or communicated; do not replace a request to act with a question about how to act unless that change is explicitly intended.
- **Evidence**:
  - Subject 11 (B > A, confirmed ranking error): the source asks the university to issue a transcript; B instead asks what steps the writer should follow. The human confirmed this was not an intended preference and must be treated as a regression, not evidence for directness.
- **Conflicts**: The stored B > A ranking contradicts this rule, but the human has explicitly invalidated that preference. Do not count Subject 11 as support for any style rule; correct or rejudge it before using the ranking as training data.
- **Maps to**: `quality-check.md` (semantic ledger; unsupported-information hard gate), `voice-and-intervention.md` (intervention audit).
- **Confidence**: High — one direct regression is explicitly identified by the human, and the speech-act distinction is a semantic invariant, not a style preference.

### Rule: Cushion face-threats, not every informal message
- **Statement**: Choose cushioning by the message’s communicative burden, not relationship-closeness alone. Add proportionate softening for bad news, apologies, impositions, or potentially unwelcome requests; keep neutral logistics and information exchanges direct, even between close contacts, while retaining the channel’s appropriate register.
- **Evidence**:
  - Subject 3 (C > B): canceling plans is unwelcome news and carries an apology; the preferred version cushions the cancellation.
  - Subject 18 (B): asking a sibling about help and timing is a neutral logistics exchange; the preferred version is direct rather than emotionally amplified.
  - Subject 14 (C): a school message reports an absence and asks for accommodation; the preferred version retains courteous softening around the request.
- **Conflicts**: The Subject 3/18 difference is resolved by the human’s clarification: cancellation/apology versus neutral logistics, not closeness. Do not generalize either candidate’s warmth level to all informal messages.
- **Maps to**: `genre-matrix.md`, `voice-and-intervention.md`, `persian-style.md`.
- **Confidence**: High — the human explicitly identified the deciding factor, and Subjects 3 and 18 provide the contrast; Subject 14 is consistent with cushioning an unwelcome update and request.

### Rule: Use the smallest sufficient rewrite and reject unsupported additions
- **Statement**: Prefer `KEEP` or `MINOR` when it fixes the diagnosed defect; use `REWRITE` when structure obstructs the message. Never add an example, actor, motive, promise, observation, or follow-up intention absent from the source or explicit authorization, even if it reads naturally.
- **Evidence**:
  - Subject 2 (A): A removes padding while retaining the enumerated product capabilities; it is preferred over more extensive rewrites.
  - Subject 12 (A): A trims sweeping pitch language and retains the listed scheduling functions.
  - Subject 16 (A > C): A keeps the restore procedure and overwrite warning in prose instead of converting it to a numbered list.
  - Subject 19 (A > B): A retains more of the source’s controlled report framing around the 18% comparison.
  - Subject 21 (A): A reports the opening, artwork count, artists, and date in a restrained caption.
  - Subject 22 (A > C): A keeps the grandmother’s recipe and preparation time without adding C’s personal family-memory claim.
  - Subject 24 (A > B): A keeps the neighborhood-level association and cross-sectional caveat; B shifts the wording toward individual residents.
- **Conflicts**: More extensive rewrites still win where they solve a structural or genre problem, including Subjects 1, 4, 5, 6, 8, 9, 10, 17, 18, 20, and 23. This is a smallest-sufficient-edit rule, not a blanket preference for Candidate A. Subjects 13 and 25 are excluded as preference evidence: their additions were ranking blind spots, not approval of helpful additions.
- **Maps to**: `voice-and-intervention.md` (intervention gate), `quality-check.md` (intervention audit; unsupported-information hard gate).
- **Confidence**: Medium — seven remaining rankings support restrained intervention (three high-confidence, four medium-confidence); Subjects 13 and 25 no longer count as evidence for accepting additions.

### Rule: Preserve semantic invariants and match instruction structure to dependency
- **Statement**: Preserve actors, quantities, dates, conditions, identifiers, warnings, scope, causality, uncertainty, and obligation when simplifying. For order-dependent procedures with an inline warning, favor prose that keeps the warning attached to the sequence; for a simple single condition-to-consequence pair, use a compact condition/action structure.
- **Evidence**:
  - Subject 7 (B): B retains the 120-student, single-university scope and the limit on generalization; confidence was low.
  - Subject 8 (C): C preserves `/v1/events`, the 100-per-minute limit, response 429, and the `Retry-After` wait while presenting the threshold and consequence compactly.
  - Subject 10 (B > A): B retains ticket `#4821`, approval, and the seven-working-day bound, plus a follow-up condition.
  - Subject 16 (A > C): A preserves `Settings > Backups`, `restore --snapshot`, the overwrite warning, and restart order in prose; the warning sits within the order-dependent procedure.
  - Subject 20 (B): B states the title prerequisite and disabled-save consequence as a compact condition/action pair.
  - Subject 23 (B > A): B keeps the symptoms, transmission routes, and advice to contact a doctor for severe symptoms, especially for higher-risk people.
  - Subject 24 (A > B): A preserves the four-neighborhood survey scope and avoids inferring causation from a cross-sectional association.
- **Conflicts**: The earlier format conflict is resolved by dependency, not task length: Subject 16 is an ordered restore procedure with a warning that can be missed if steps are skimmed out of order; Subjects 8 and 20 are simple condition-to-consequence cases. This does not prescribe prose for every technical explanation or lists for every short instruction.
- **Maps to**: `quality-check.md` (semantic ledger; unsupported-information hard gate), `translationese.md` (causality and terminology), `genre-matrix.md` (academic and technical genres).
- **Confidence**: High — the human clarification directly resolves the format distinction; seven cases support semantic/structural preservation (four high, two medium, one low in stated subject confidence).

### Rule: Keep evaluative language only when specifics substantiate it
- **Statement**: Retain a broad evaluative word only when the text supplies concrete specifics that the word accurately summarizes. If a claim such as “unique,” “flawless,” or “unparalleled” stands without evidence that supports that exact evaluation, cut it rather than substituting another unsupported benefit.
- **Evidence**:
  - Subject 2 (A): “Comprehensive” summarizes the adjacent, enumerated note creation, categorization, cross-device sync, and reminder functions.
  - Subject 6 (C): C removes the claim that the opening is an important step in cultural development; the listed book count and study room do not substantiate that impact claim.
  - Subject 12 (A): A removes “unique,” “major transformation,” and “flawless experience”; the enumerated scheduling functions do not establish uniqueness or flawlessness.
  - Subject 15 (B): B replaces “unique/unparalleled” praise with the observed soup quality, 40-minute wait, and price-to-portion comparison.
  - Subject 21 (A): A removes the generic cultural-benefit conclusion; the event facts do not establish a broader cultural impact.
  - Subject 22 (A > C): A centers the recipe and preparation time instead of the unsupported “unparalleled” experience claim.
- **Conflicts**: The Subject 2 versus Subjects 6, 12, 15, and 21 contrast is resolved by claim-specific substantiation: listed capabilities support “comprehensive,” but do not support unrelated superlatives or broad impact claims. Do not read Subject 12’s ranking as permission to add benefits; check each evaluative phrase against the specific details that follow.
- **Maps to**: `patterns.md` (unsupported marketing filler; pseudo-profundity; academic significance inflation), `genre-matrix.md` (marketing and journalism), `quality-check.md` (unsupported-information hard gate).
- **Confidence**: High — the human supplied the explicit threshold, and six cases illustrate supported summary versus unsubstantiated evaluation; stated subject confidence is mixed (three high, three medium).

## Skipped subjects

- No subject has a blank winner/ranking. Exclude Subjects 11, 13, and 25 from valid preference evidence: 11 is a confirmed ranking error; 13 and 25 contain additions the human identifies as pairwise-judging blind spots, not preferences.

## Open questions / inconsistencies

- Subject 11’s stored B > A ranking remains a known regression in `judgments.md`. This file flags it but does not alter the judgment record; correct or rejudge it before using the data for learning.
- Subjects 13 and 25 show that side-by-side preference can miss small fabrications that read naturally. Future rounds should include an explicit post-ranking fabrication check against the original, checking each candidate for new examples, actors, intentions, promises, and claims.
- The per-subject “Why” and candidate-note fields are still blank, so patterns beyond the five clarified questions remain partly inferred. Subject 4’s confidence is also still missing.
