# Persian Style Reference

Use this reference when a Persian rewrite needs more than surface cleanup. Natural Persian is not deliberately imperfect Persian. It is context-aware, clear, specific, rhythmically believable, and recognizably consistent with its writer.

## 1. Infer and preserve the register

Choose the dominant register from the request, audience, channel, and source voice. If the user gives a target register, it outranks the inference.

| Register | Typical context | Editing target |
| --- | --- | --- |
| محاوره‌ای | Chat, personal messages, casual scripts | Spoken syntax and contractions may stay. Do not add fake slang or typos. |
| نیمه‌رسمی | Product copy, business chat, internal communication, accessible articles | Modern, direct Persian with light politeness. |
| رسمی | Letters, reports, institutional material, proposals | Precise and courteous; formal does not mean inflated. |
| دانشگاهی / پژوهشی | Papers, theses, research reports | Stable terminology, explicit evidence, calibrated uncertainty, intact citations. |
| خبری | News, announcements, press copy | Lead with the verifiable event, actor, time, and consequence; avoid promotional framing. |
| تبلیغاتی | Ads, landing pages, campaign copy | Persuade with a concrete promise, audience benefit, or proof; keep brand voice. |
| فنی | Documentation, specifications, changelogs | Optimize for unambiguous instructions and stable terminology. |
| پشتیبانی مشتری | Ticket replies, help-center responses, service messages | Acknowledge when useful, answer directly, state the next action or status. |
| شبکه اجتماعی | Captions, posts, replies, community updates | Respect the platform's brevity and the writer's real voice; do not impose essay structure. |
| مقاله / وبلاگ | Explanatory, editorial, or educational prose | Reach the point quickly, develop one idea per paragraph, and use transitions only when logic needs them. |

Do not make a customer-support reply sound like a thesis, turn academic writing into Telegram slang, or flatten advertising into neutral documentation.

## 2. Edit as little as necessary

- Preserve useful quirks, humor, brevity, dialect, recurring vocabulary, and intentional repetition.
- Keep established terminology stable. Do not rotate `کاربر`, `مخاطب`, and `استفاده‌کننده` merely to create variation when they name the same role.
- Preserve quotations, attributed passages, citations, links, numbers, dates, names, identifiers, and Markdown structure unless the structure itself is the problem.
- Do not make the writer more emotional, certain, friendly, casual, or polished than the source supports.
- When the source is already good, make no change or make only a targeted correction.

## 3. Replace artificial formality by context, not by blacklist

Formal forms are not automatically wrong. Ask whether the genre needs them and whether they recur densely.

| Padded form | Use a simpler form when it means |
| --- | --- |
| `می‌باشد` | `است` |
| `می‌نماید` | A direct verb such as `می‌کند` or `نشان می‌دهد` |
| `گردید` / `می‌گردد` | `شد` / `می‌شود` or a specific action |
| `در خصوص` | `درباره` |
| `در راستای` / `در این راستا` | The actual purpose, action, or relation |
| `بدین منظور` | `برای این کار` or the action itself |
| `شایان ذکر است` / `لازم به ذکر است` | Delete the ceremony and state the fact |
| `با توجه به موارد فوق` | State the actual inference |
| `در نهایت می‌توان گفت` | State a necessary conclusion directly, or stop |
| `نسبت به انجام ... اقدام نمود` | Use the direct verb |
| `مورد بررسی قرار داد` | `بررسی کرد` when the actor and action are clear |

Do not force these substitutions in legal wording, official templates, historical quotations, or a consciously ceremonial register.

## 4. Rewrite translationese in native Persian

Prefer Persian information flow over word-for-word equivalence.

- Omit pronouns when the verb and context already identify the subject. Keep them when contrast, emphasis, or disambiguation requires them.
- Name the actor when responsibility matters. Keep passive voice when the actor is unknown, unimportant, or intentionally omitted.
- Turn heavy nominal phrases into direct verbs when clarity improves: `انجام بررسی و ارزیابی نتایج صورت گرفت` can become `نتایج را بررسی و ارزیابی کردیم` when the source identifies `we`.
- Reorder clauses when a literal English sequence sounds unnatural in Persian.
- Remove repeated scaffolding such as `این موضوع`, `این امر`, and `این مسئله` when it carries no meaning.
- Keep a technical English term when the audience uses it and the Persian alternative would reduce precision.

Do not add a missing actor, mechanism, or result merely to make a sentence sound more concrete.

## 5. Control rhythm and connective logic

- Vary sentence length when the ideas vary. Do not randomize sentence lengths or split every long sentence.
- Place the verb where Persian syntax and the chosen register naturally call for it; do not preserve an English clause order at the cost of fluency.
- Use `همچنین`, `علاوه بر این`, `از سوی دیگر`, `در واقع`, `به طور کلی`, `به عبارت دیگر`, `بنابراین`, `در نتیجه`, and `با این حال` only when the relation needs a signal.
- Remove repeated paragraph-opening transitions and replace them with a direct sentence when the relation is already clear.
- Let paragraphs end when the point is complete. Do not add a miniature conclusion to every paragraph.
- Keep a list when items are genuinely parallel. Turn it into prose when bullets only split one continuous idea.

## 6. Persian orthography and punctuation

- Use Persian `ی` and `ک` in ordinary Persian text when normalizing characters; do not alter code, URLs, product names, or identifiers.
- Use a reasonable نیم‌فاصله in forms such as `می‌شود`, `نمی‌توان`, `آن‌ها`, `به‌کارگیری`, and `داده‌ها` when the chosen register uses standard orthography.
- Do not over-normalize colloquial writing. A user's deliberate `می‌خوام`, `نمی‌شه`, or dialect spelling may be part of the voice.
- Keep one normal space after `،`, `؛`, and `؟`, and no space before them. Adjust only when it improves readability and does not alter protected material.
- Use `« »` for Persian quotations when the source style uses them. Do not add quotation marks for decorative emphasis.
- Reduce excessive parentheses, semicolons, ellipses, separators, and English-style em-dash splices when they do not serve the register.
- Never add zero-width characters, homoglyphs, invisible formatting, or deliberate punctuation noise. The ZWNJ is allowed only as legitimate نیم‌فاصله.

## 7. Genre reminders

### Marketing

Keep persuasion, but replace empty praise with a concrete promise or an evidenced property. If the source says a product is `قدرتمند` or `منحصربه‌فرد` without support, remove or qualify the adjective; do not invent a metric or feature.

### Customer support

Prefer direct acknowledgement, answer, status, and next action in the order the customer needs. Preserve necessary politeness, ticket numbers, dates, policy language, and commitments.

### Academic and research writing

Do not make the text casual. Tighten nominal phrases, remove unsupported significance, keep technical terms and citations stable, and preserve hedges such as `ممکن است` when the evidence is limited.

### Technical documentation

Optimize for unambiguous meaning. Preserve API names, CLI commands, flags, code blocks, file paths, versions, and warnings. Do not vary terminology merely for style.
