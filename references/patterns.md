# Persian Writing Pattern Catalog

These are editing signals, not proof of AI authorship. Flag clusters, repetition, and context mismatch rather than isolated words. A phrase can be correct in an administrative letter, an academic paper, a quotation, or a deliberately rhetorical passage.

The right correction is the smallest one that makes this text clearer and more natural. Do not replace every flagged phrase automatically.

## 1. Artificially formal and bureaucratic Persian

Review these when they add ceremony without adding precision:

- `می‌باشد`, `می‌نماید`, `گردید`, `می‌گردد`
- `بدین منظور`, `در خصوص`, `در راستای`, `در این راستا`
- `شایان ذکر است`, `لازم به ذکر است`
- `با توجه به موارد فوق`, `در نهایت می‌توان گفت`
- `به استحضار می‌رساند`, `نسبت به انجام`, `اقدام به ... نمودن`, `مورد بررسی قرار دادن`
- `در دنیای امروز`, `در عصر حاضر` when they only delay the point

Possible directions, chosen by context:

| Signal | Consider |
| --- | --- |
| `می‌باشد` as an inflated copula | `است` or a direct predicate |
| `می‌نماید` as a padded verb | A normal direct verb such as `می‌کند` or `نشان می‌دهد` |
| `گردید` / `می‌گردد` as administrative padding | `شد` / `می‌شود`, or a more specific verb |
| `در خصوص` | `درباره` when the register allows it |
| `در راستای` / `بدین منظور` | State the actual purpose or action |
| `شایان ذکر است` / `لازم به ذکر است` | Delete it and start with the fact |
| `با توجه به موارد فوق` | State the actual inference, or stop if it is obvious |
| `در نهایت می‌توان گفت` | State the conclusion directly, if a conclusion is needed |

Do not ban formal language. A legal notice, government form, or ceremonial letter may need a different register. The question is whether the form serves that genre or merely inflates an ordinary sentence.

## 2. Translationese and English-shaped syntax

Look beyond individual vocabulary. Common signals include:

- English-like word order or rhetorical progression that feels translated rather than written in Persian.
- Explicit pronouns (`او`, `آن‌ها`, `این موضوع`) where Persian verb agreement or context already supplies the subject.
- Repetition of the subject at the start of nearby sentences.
- Passive constructions that hide a known actor: name the actor when responsibility matters; keep passive voice when the actor is unknown or irrelevant.
- Dense noun stacks and literal nominalizations where a Persian verb would be clearer.
- Literal translations of English transitions or sentence frames.
- Repeated `این موضوع`, `این امر`, and `این مسئله` used only as paragraph glue.
- Repeated `با ارائه ...، موجب ... می‌شود` and similar participial frames that avoid a direct sentence.

Rewrite the sentence according to Persian information flow. Do not perform a word-for-word synonym swap, and do not invent an actor or a concrete result that the source does not provide.

## 3. Generic LLM transitions

These connectors are valid Persian:

- `علاوه بر این`
- `همچنین`
- `از سوی دیگر`
- `در واقع`
- `به طور کلی`
- `به عبارت دیگر`
- `بنابراین`
- `در نتیجه`
- `با این حال`

Flag them when several paragraphs open with one, multiple connectors appear in a short passage, or the connector announces a relation that the sentences do not actually have. Remove unnecessary signposting or replace it with a content-bearing bridge. Do not delete a connector just to make the text less regular.

## 4. Formulaic structure and rhythm

Inspect the whole passage for:

- Paragraphs with nearly identical length and internal shape.
- Repeated `claim → explanation → conclusion` units.
- A compulsory introduction, followed by exactly three benefits, followed by a summary.
- Repeated three-item adjective or benefit groups when two items or a sentence would be more accurate.
- Numbered lists used for prose that has no sequential steps.
- A heading for every short paragraph.
- A conclusion that merely repeats the preceding claims.
- A micro-summary at the end of every section.
- Predictable openings that delay the actual point.

Let the information determine paragraph length and structure. Convert bullets to prose only when prose is clearer; keep lists for genuinely parallel steps, requirements, options, features, or constraints.

## 5. Corporate filler and unsupported praise

Review dense or unsupported uses of:

- `تجربه‌ای بی‌نظیر`
- `راهکاری جامع`
- `تحولی بزرگ`
- `انقلابی`
- `قدرتمند`
- `نوآورانه`
- `پیشرفته`
- `منحصربه‌فرد`
- `در سطحی جدید`
- `مهم`, `کارآمد`, `هوشمند`, `یکپارچه`, `بهینه`, `قابل توجه`, `تأثیرگذار`

Ask what the product, method, or event actually does, for whom, and under what condition. Replace praise with an observable property only when that property is present in the source. Otherwise delete the adjective or make the claim appropriately modest.

## 6. Natural Persian rhythm and presentation

Review whether:

- Sentence lengths and clause counts vary because the ideas vary, not because of random rewriting.
- Verb placement and clause order sound native rather than translated.
- Paragraphs carry one useful local idea without a forced closing sentence.
- Punctuation clarifies syntax instead of decorating it.
- `،`, `؛`, `؟`, and `« »` fit the register; parentheses, quotation marks, and ellipses are not overused.
- Persian `ی` and `ک` are used consistently where normalization is requested.
- نیم‌فاصله is reasonable in forms such as `می‌شود`, `نمی‌توان`, and `آن‌ها` without correcting intentional colloquial usage into a different voice.
- Markdown headings, emphasis, and bullets serve the publication context.

Do not use inconsistent نیم‌فاصله, random punctuation, suspicious Unicode, or artificial roughness as a style technique.

## 7. Conversation and support patterns

In replies, flag:

- Repeating the user's request before answering.
- A long preamble before the useful message.
- Ceremony such as `حتماً! با کمال میل` when it adds nothing.
- `امیدوارم این توضیحات برای شما مفید باشد` or `اگر سؤال دیگری داشتید` when no follow-up is needed.
- A formal institutional register mixed with casual particles.

For customer support, prefer the context-appropriate combination of acknowledgement, answer, status, and next action. Do not remove necessary politeness or turn a formal support channel into chat slang.

## 8. Integrity boundary

Never treat these as acceptable edits:

- Deliberate typos, false uncertainty, fake slang, or grammatical mistakes.
- Hidden or zero-width characters, homoglyphs, spacing attacks, or other adversarial Unicode changes.
- Fabricated anecdotes, sources, citations, quotations, statistics, dates, or customer reactions.
- Claims that the text is undetectable, guaranteed human, or optimized for a detector score.

Quoted, attributed, cited, coded, tabular, and factual material is protected content. Flag an issue inside it if useful, but leave it unchanged unless the user explicitly authorizes an edit.
