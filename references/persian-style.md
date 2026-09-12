# Persian Style Reference

Use this reference when a Persian rewrite needs more than surface cleanup. It describes native-oriented editing principles, not statistical targets.

## 1. Information structure before word substitution

Persian commonly has verb-final/SOV tendencies, but actual clause order is flexible and sensitive to topic, focus, contrast, discourse continuity, and genre. Do not impose one rigid template.

Prefer an order in which established or topical material is easy to recover and new information arrives where the reader expects it. A grammatically possible sentence may still feel translated if it preserves English sequencing too literally.

Editing rule:

- diagnose the discourse relation first;
- reorder only when the source meaning and emphasis remain intact;
- never invent a topic, actor, focus, or causal relation to make the sentence smoother.

## 2. Subject expression and reference

Persian frequently omits an overt subject because the verb and context identify it.

Consider removing an explicit pronoun when:

- the subject is stable across adjacent clauses;
- verb morphology and context identify the referent;
- no contrast, correction, emphasis, or switch-reference is intended.

Keep or restore an explicit noun/pronoun when:

- two antecedents are plausible;
- responsibility matters;
- the topic changes;
- contrast or emphasis is intentional;
- omission would make technical or legal meaning less precise.

Do not replace every repeated noun with a pronoun merely to create variation.

## 3. Topic continuity and anaphora

Use the least explicit referring expression that stays clear.

Review:

- repeated full noun phrases that unnecessarily restart every sentence;
- repeated `این موضوع`, `این امر`, or `این مسئله` used only as glue;
- vague `این` or `آن` whose antecedent is unclear;
- sudden zero subjects after a topic shift.

Lexical repetition can be desirable when the repeated word is the correct technical term, a defined legal term, or a deliberate rhetorical anchor.

## 4. Active, passive, and nominal style

Active voice is not inherently more natural. Passive is useful when the actor is unknown, irrelevant, intentionally backgrounded, or when the affected entity is the discourse topic.

Prefer naming the actor when:

- responsibility matters;
- the source already identifies the actor;
- a `توسط` construction merely preserves English passive organization.

Do not invent an actor.

Nominalization is legitimate in academic, legal, administrative, and technical prose. Rewrite it into a direct verb only when:

- the action is clearer as a verb;
- the actor/action is actually licensed by the source;
- the genre does not depend on the nominal form.

For example, `انجام بررسی نتایج صورت گرفت` may become `نتایج بررسی شد` or `نتایج را بررسی کردیم` only if the source supports the chosen actor.

## 5. Translation-like predicates and collocations

Translationese is often constructional, not lexical.

Review literal frames such as:

- `نقش مهمی بازی می‌کند` where `نقش مهمی دارد` is the natural predicate;
- repeated `به کاربران اجازه می‌دهد که آن‌ها ...`;
- noun-heavy participial frames such as `با ارائه ... موجب ... می‌شود`;
- English rhetorical sequencing preserved despite awkward Persian flow.

Rewrite the construction as a whole. Do not perform isolated synonym swaps.

For deeper cases, read [translationese](translationese.md).

## 6. Discourse markers and cohesion

Connectors are legitimate Persian. Their function matters more than frequency alone.

Keep a marker when it:

- expresses a real contrast, cause, consequence, addition, reformulation, or shift;
- prevents misreading;
- belongs to the genre's argument structure.

Review a marker when:

- several nearby paragraphs begin with one;
- multiple markers stack in the same transition;
- the marker announces a relation the content does not support;
- adjacency or reference already makes the relation obvious.

Do not rotate connector synonyms merely to create variety.

## 7. Rhythm and structural variation

Variation should be an effect of varying communicative work.

Natural outcomes may include:

- a one-sentence paragraph for a transition;
- a longer paragraph for a difficult mechanism;
- a short emphatic sentence;
- a long sentence whose clauses genuinely belong together;
- repeated use of the same technical noun;
- two supporting reasons instead of a forced three.

Never target a sentence-length distribution, paragraph-length distribution, "burstiness" score, or lexical-diversity score.

## 8. Register preservation

Do not equate natural Persian with casual Persian.

- conversational text may use contractions, ellipsis, fragments, and spoken cadence;
- formal correspondence may legitimately use formulaic politeness;
- academic writing may need hedging, nominalization, and explicit argument markers;
- technical writing should privilege stable terms and unambiguous steps;
- marketing may use compressed syntax, slogan rhythm, and intentional repetition;
- administrative/legal language may contain forms that would be padding elsewhere.

Read [genre matrix](genre-matrix.md) when genre materially affects the edit.

## 9. Technical English and code-switching

English technical terms can be natural for Iranian technical audiences.

Preserve established terms, product/model names, package names, API names, commands, flags, file names, paths, environment variables, and code.

Do not Persianize terminology merely to increase the proportion of Persian words. The surrounding syntax can still be edited into natural Persian.

## 10. Persian orthography and punctuation

Apply mechanics after substantive editing.

- use Persian `ی` and `ک` in ordinary normalized Persian prose;
- use reasonable نیم‌فاصله in forms such as `می‌شود`, `نمی‌توان`, `آن‌ها`, `داده‌ها`;
- keep one normal space after Persian punctuation and none before it;
- use punctuation to clarify syntax, not to imitate English rhythm;
- avoid decorative em-dash chains, excessive parentheses, and punctuation noise when they do not fit the house style.

Do not normalize:

- code, URLs, paths, identifiers, citations, model names;
- exact quotations where form matters;
- intentionally colloquial spelling unless the user requests standardization.

## 11. Minimal-intervention reminder

A fluent source sentence that fits its purpose is not a problem simply because a catalog contains one of its words.

Before changing a sentence, identify the exact defect and why the edit improves this context. If no such reason exists, keep it.
