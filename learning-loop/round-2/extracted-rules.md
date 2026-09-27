# Round 2 — Extracted Rules

## Rule candidates

### Rule: Lead with the useful status or action
- **Statement**: In support, coordination, and customer-facing messages, put the content-bearing status, action, or request before administrative setup. Keep the deadline, requested response, and channel-appropriate courtesy; this is not a mandate to remove conventional greetings from formal notices.
- **Evidence**:
  - Subject 1: B leads with the order dates and unchanged tracking status, then asks for the two requested outcomes.
  - Subject 5: B starts with the volunteer schedule and the response deadline instead of the event-approach preamble.
  - Subject 6: A retains the time and source-stated resident impact, then asks for the repair time without the generic “take necessary action” tail.
  - Subject 11: A retains the conventional resident salutation but puts the exact outage window and stair instruction immediately after it.
  - Subject 17: B puts the unregistered payment status before the conditional receipt/payment actions.
  - Subject 23: B states that the order is still being prepared before requesting the old-to-new address change.
  - Subject 25: C connects the Thursday repair to the revised opening time and retains the apology.
- **Conflicts**: Subjects 8 and 11 favor conventional courtesy in school/building messages; they qualify the rule against blanket removal of greetings, not the preference for early actionable information. Subject 6 is a group update rather than a transactional notice, so its brevity should not be generalized to every business message.
- **Maps to**: references/patterns.md (lead with substance); references/genre-matrix.md (channel-appropriate courtesy and support status).
- **Confidence**: LOW — several examples point the same way, but this round is AI-judged and cannot raise confidence above LOW.

### Rule: Cushion the imposition, not the relationship
- **Statement**: Scale cushioning to the message's burden: acknowledge late changes, apologies, requests that inconvenience the recipient, and unwelcome news. Neutral logistics can stay direct even between close contacts; do not add formality or emotional intensity merely because a relationship is close.
- **Evidence**:
  - Subject 2: A explicitly acknowledges the late notice and apologizes before proposing a conditional reschedule.
  - Subject 10: A keeps the conditional “اگر ممکن است” extension request rather than turning it into a command.
  - Subject 13: C keeps “اگر می‌توانید” in a family dinner invitation, which asks recipients to spend time and requires preparation.
  - Subject 25: C preserves an apology and thanks alongside the changed opening time.
- **Conflicts**: Subject 6 uses a direct request for a repair update, while Subjects 8 and 11 retain conventional courtesy; these are neutral group/school/building communications, not evidence that an apology or formal cushion is always needed. Subject 2's Round 1 winner was the more direct Candidate C, while this round selects A for explicitly naming the lateness; this is a partial convergence signal and should be checked by a human.
- **Maps to**: references/voice-and-intervention.md; references/genre-matrix.md.
- **Confidence**: LOW — the examples are context-sensitive and the repeat result for Subject 2 is only a partial match to the prior human preference.

### Rule: Keep dependent procedures in order and warnings attached
- **Statement**: For procedures with sequence-dependent actions, keep the steps in readable prose and place a warning beside the command or step it qualifies. For a single condition-and-consequence, concise if/then wording is suitable, but the recovery path must still name the required next action.
- **Evidence**:
  - Subject 3: A keeps stop → select → restore command → overwrite warning → verify → restart in order, with the warning in the command sentence.
  - Subject 15: A preserves the expired-code branch and explicitly says to repeat the steps after requesting a fresh code.
  - Subject 24: A keeps departure, route, rest, weather condition, return action, and river prohibition in order; the warning remains adjacent to its condition.
  - Subject 20: A and C use the same direct condition/consequence and recovery wording; this supports the form's suitability, but their identical text yields no comparative preference.
- **Conflicts**: No clear contrary preference. Subject 20's A and C are identical, so that item cannot show which wording the judge preferred. Subject 15 also shows that compression is not useful if it obscures whether a replacement code must be entered.
- **Maps to**: references/genre-matrix.md (technical documentation); references/quality-check.md (conditions and sequence).
- **Confidence**: LOW — the procedural distinctions recur, but one example is a duplicate and all judgments are provisional.

### Rule: Keep claims inside the evidence and its scope
- **Statement**: Retain a broad or evaluative descriptor only when nearby source details substantiate that exact claim. Otherwise remove or narrow it, and do not expand a measured result, product capability, event, or technical failure beyond the source's evidence.
- **Evidence**:
  - Subject 4: A keeps “جامع” because the source enumerates note creation, categorization, syncing, and reminders, while removing unsupported “نوآورانه.”
  - Subject 7: C states the supported phone/laptop sync capability without adding a separate “available” benefit.
  - Subject 9: B keeps dimensions, drawers, wear, and price while dropping “فوق‌العاده” and “بی‌نظیر.”
  - Subject 12: B retains the 18% comparison and table reference but removes unsupported market rank, exceptional performance, and employee-cause claims.
  - Subject 14: B retains the source's stated encouragement to attend but removes “بی‌نظیر” and “فراموش‌نشدنی,” which the event details do not substantiate.
  - Subject 16: C limits the 62% result to the 84 respondents in the named campus survey instead of generalizing to city students or all universities.
  - Subject 18: C removes gift/quality praise while preserving the source's definite statement about color variation.
  - Subject 21: C reports the three Safari failures and Chrome/Firefox comparison without the unsupported conclusion that the whole system has a general problem.
- **Conflicts**: Subject 4 is a deliberate boundary case: “جامع” survives because the listed capabilities support it, while Subject 9's quality superlatives do not. Subject 14 similarly preserves the invitation's source-stated effect on organizers; this is not support for adding new emotional claims such as Subject 14 A's “خوشحال می‌شویم ببینیمتان.”
- **Maps to**: references/patterns.md; references/quality-check.md; references/evaluation.md.
- **Confidence**: LOW — this pattern appears in many subjects, but the confidence ceiling remains LOW because the judgments are AI-generated.

### Rule: Preserve the source's communicative act and semantic ledger
- **Statement**: A rewrite must preserve what the source is doing—requesting, granting permission, apologizing, offering, or instructing—as well as its material facts, modality, conditions, scope, and next action. If a candidate sounds smoother but changes or deletes one of those propositions, reject it or flag the case.
- **Evidence**:
  - Subject 1: B retains the original order dates and the either/or request for an exact delivery time or cancellation.
  - Subject 8: A states the parent's permission and keeps the offer to provide information or complete a form.
  - Subject 10: A preserves a conditional request for an extension and both reasons supporting it.
  - Subject 15: A retains the expired-code condition and the repeat-the-steps recovery branch.
  - Subject 16: C retains the sample size and scopes the percentage to that sample.
  - Subject 17: B keeps the if-paid/send-receipt, otherwise/pay alternatives and the invoice identifiers.
  - Subject 19: No candidate wins because all omit the source's explicit acknowledgement of the recipient's difficult days and hope that support will help; natural phrasing does not excuse loss of that proposition.
  - Subject 20: The tied A/C text retains the five-attempt threshold and 15-minute duration.
  - Subject 21: C preserves the count, browser/version scope, and passing comparison.
  - Subject 22: No candidate wins: all three omit the source's tentative “appears to be lost” assessment, changing the message's stated uncertainty.
  - Subject 23: B retains the explicit address-change request, both addresses, order status, and requested confirmation.
  - Subject 24: A preserves the route sequence and the conditional weather/safety instructions.
- **Conflicts**: Subject 19 exposes a candidate-set failure rather than a conflict in the rule: all three options delete a meaningful supportive sentence. Subject 20 has duplicate A/C text, so it provides no letter-level ranking evidence. Subject 2's partial repeat match also leaves open whether added explicit acknowledgement should outrank the more direct informal phrasing when both retain an apology.
- **Maps to**: references/quality-check.md; references/evaluation.md; references/voice-and-intervention.md.
- **Confidence**: LOW — many examples touch semantic preservation, but one case has no acceptable candidate, one contains a duplicate, and the AI-judged caveat caps confidence.

## Skipped subjects

None. All 25 subjects have a winner, ranking, or explicit “none” judgment with a completed rationale.

## Open questions / inconsistencies

- These are AI judgments, not repository-maintainer preferences. The four repeat comparisons are therefore provisional model-to-human comparisons, not a valid human convergence measurement; a human should confirm them before treating them as learning signal.
- Subject 20 has byte-for-byte identical Candidate A and Candidate C text. The tie is deliberate; remove or replace one candidate before using this item to measure preference.
- Subjects 19 and 22 have no acceptable candidate: all rewrites delete, respectively, the supportive thought and the tentative lost-status. Rebuild both candidate sets and re-judge rather than extracting a tone preference from them.
- Subject 2 is a partial repeat match: Round 1 preferred C > B, while this round selects A for its explicit late-notice acknowledgement. The distinction is plausible under the cushioning rule but remains unverified by a human.
- Subject 14 shows why a separate fabrication check matters: the natural-sounding “خوشحال می‌شویم ببینیمتان” adds an emotional claim not in the source, while B retains the invitation wording that is actually present.
- Rules about status-first structure and cushioning overlap at the channel boundary: formal notices may retain a greeting, and bad-news messages may need both early status and a proportionate apology. Do not turn either preference into a rigid template.
