# Persian Writing Pattern Catalog

These are editing diagnostics, not proof of AI authorship. Diagnose clusters, repetition, discourse mismatch, and genre mismatch. Never treat the presence of one phrase as sufficient reason to rewrite.

Each entry uses the same operational fields:

- **Cues:** what to notice
- **Cluster signal:** what makes the diagnosis stronger
- **False positives / genre license:** when the pattern may be legitimate
- **Correction:** smallest useful repair
- **Forbidden transformation / semantic risk:** what the edit must not change

## 1. Throat-clearing introduction

**Cues:** `در دنیای امروز`, `در عصر حاضر`, generic statements about importance, or `در این مقاله قصد داریم...` before any content-bearing claim.

**Cluster signal:** two or more generic framing sentences plus a roadmap sentence, with no concrete actor, event, scope, or thesis.

**False positives / genre license:** speeches, historical framing, long reports, academic introductions, or articles where the scope statement itself is useful.

**Correction:** start at the first useful claim or keep only the background needed to interpret it.

**Forbidden transformation / semantic risk:** do not invent a stronger thesis, fact, trend, example, or statistic.

## 2. Decorative conclusion or micro-summary

**Cues:** `در نهایت می‌توان گفت`, `به طور کلی می‌توان گفت`, or a final sentence that merely repeats the previous claim.

**Cluster signal:** repeated claim → explanation → restated claim units across several paragraphs.

**False positives / genre license:** academic conclusions, executive summaries, teaching material, or branded taglines that add genuine synthesis or navigation.

**Correction:** remove the redundant closure or replace it with an actual supported consequence.

**Forbidden transformation / semantic risk:** do not fabricate an implication or broaden the claim beyond the source.

## 3. Mechanical discourse-marker density

**Cues:** nearby sentences or paragraphs repeatedly start with `همچنین`, `علاوه بر این`, `از سوی دیگر`, `در واقع`, `بنابراین`, `در نتیجه`, `با این حال`.

**Cluster signal:** repeated paragraph-initial placement, connector stacking, or a marker whose logical relation does not match the sentence.

**False positives / genre license:** academic, legal, or analytic argument where explicit relations prevent ambiguity.

**Correction:** keep the marker that performs real work; otherwise use direct content, reference continuity, or simple adjacency.

**Forbidden transformation / semantic risk:** do not remove a causal or contrastive marker when doing so changes how propositions relate.

## 4. Demonstrative-shell glue

**Cues:** repeated `این موضوع`, `این امر`, `این مسئله` used after nearly every proposition.

**Cluster signal:** the shell noun can be deleted without losing referential clarity, or its antecedent is vague.

**False positives / genre license:** when the text genuinely categorizes something as an issue, matter, problem, question, or topic.

**Correction:** use zero reference, a clear pronoun, or name the actual antecedent.

**Forbidden transformation / semantic risk:** do not create ambiguous reference after topic shifts.

## 5. Bureaucratic padding

**Cues:** dense uses of `می‌باشد`, `می‌نماید`, `گردید`, `می‌گردد`, `در خصوص`, `در راستای`, `بدین منظور`, `نسبت به انجام`, `اقدام به ... نمودن`, `مورد بررسی قرار دادن`.

**Cluster signal:** multiple padded constructions in ordinary product, support, social, or explanatory prose where direct verbs would preserve the same function.

**False positives / genre license:** legal, government, administrative, ceremonial, historical, or fixed institutional wording.

**Correction:** use a direct predicate or state the actual purpose/action.

**Forbidden transformation / semantic risk:** do not weaken legal/procedural force or convert a required institutional register into casual Persian.

## 6. Institutional ceremony in the wrong channel

**Cues:** `بدین‌وسیله`, `به استحضار می‌رساند`, `شایان ذکر است`, `لازم به ذکر است` in an app notice, ordinary support reply, social post, or internal chat.

**Cluster signal:** ceremony outweighs the actual status, answer, or next action.

**False positives / genre license:** formal letters, official notices, ceremonial correspondence.

**Correction:** state the fact, status, or action directly while preserving appropriate politeness.

**Forbidden transformation / semantic risk:** do not make support curt or remove required etiquette.

## 7. Translationese syntax

**Cues:** unnecessary overt subjects, English-shaped clause order, literal predicates, repeated full noun subjects, heavy noun chains, literal connective frames.

**Cluster signal:** several structural cues appear together and the sentence is grammatical but reads as translated.

**False positives / genre license:** established technical calques, quotations, intentionally translated terminology.

**Correction:** rewrite the construction according to Persian information flow; omit recoverable subjects; use a natural predicate; prefer a direct verb where genre permits.

**Forbidden transformation / semantic risk:** do not invent an actor, causal relation, result, or technical meaning.

Read [translationese](translationese.md) for detailed cases.

## 8. Compulsive triads and false symmetry

**Cues:** exactly three benefits, three adjectives, or three sections despite unequal or unsupported content.

**Cluster signal:** repeated three-item structures plus uniform paragraph shape or a vague third item.

**False positives / genre license:** intentional rhetoric, established slogans, real three-step procedures, genuinely parallel requirements.

**Correction:** let the number and weight of items follow the information.

**Forbidden transformation / semantic risk:** do not destroy real parallel structure merely because it contains three items.

## 9. Heading or bullet inflation

**Cues:** a heading for every short paragraph, or long bullets that are merely consecutive prose sentences.

**Cluster signal:** headings restate the paragraph instead of aiding navigation; bullets are not truly parallel or scannable.

**False positives / genre license:** documentation, help centers, requirements, procedures, options, feature matrices.

**Correction:** merge into prose or fewer sections only when continuity improves.

**Forbidden transformation / semantic risk:** do not damage scanability, step order, requirements, or information architecture.

## 10. Unsupported marketing filler

**Cues:** `جامع`, `قدرتمند`, `نوآورانه`, `منحصربه‌فرد`, `بی‌نظیر`, `تحولی بزرگ`, `در سطحی جدید` without a concrete basis in the source.

**Cluster signal:** several evaluative adjectives with no mechanism, audience, condition, proof, or observable property.

**False positives / genre license:** deliberate brand voice, slogans, campaigns, or explicitly hyperbolic copy.

**Correction:** use a source-supported capability or benefit; otherwise remove or soften the adjective.

**Forbidden transformation / semantic risk:** never manufacture a metric, proof point, customer reaction, market position, or guaranteed result.

## 11. Pseudo-profundity and abstraction cascade

**Cues:** generic metaphors such as `پلی به سوی آینده`, or abstract chains like `بهبود تجربه، افزایش بهره‌وری و ارتقای کیفیت` without mechanism.

**Cluster signal:** the sentence could describe many unrelated products or topics with no meaningful change.

**False positives / genre license:** opinion writing, creative brand language, intentional metaphor.

**Correction:** recover the supported actor/action/outcome or keep the metaphor only when it is actually part of the writer's voice.

**Forbidden transformation / semantic risk:** do not invent a mechanism just to make the claim concrete.

## 12. Over-explaining and excessive completeness

**Cues:** a simple instruction or answer grows into definitions, obvious consequences, history, benefits, risks, and summary not required by the task.

**Cluster signal:** later sentences add no constraint, state, failure mode, or decision-relevant information.

**False positives / genre license:** beginner teaching, compliance material, comprehensive reports, safety-critical documentation.

**Correction:** retain only the explanation needed by this audience and task.

**Forbidden transformation / semantic risk:** do not remove prerequisites, safety warnings, legal disclosures, or novice-critical context.

## 13. Fake precision

**Cues:** added numbers, percentages, dates, benchmarks, timeframes, certainty words, named mechanisms, or causal links not present in the source.

**Cluster signal:** the rewrite is more specific than the input without evidence.

**False positives / genre license:** none when the information was introduced by the editor rather than supplied by the source.

**Correction:** restore the original level of specificity and uncertainty.

**Forbidden transformation / semantic risk:** this is a hard failure. Do not retain invented precision because it sounds more persuasive.

## 14. Uniform sentence or paragraph templates

**Cues:** repeated syntactic frames, identical paragraph lengths, or repeated claim → explanation → conclusion structures.

**Cluster signal:** uniformity aligns with a template rather than genuinely parallel ideas.

**False positives / genre license:** comparison tables, procedures, repeated legal clauses, deliberate rhetoric, teaching exercises.

**Correction:** restructure only where the ideas perform different communicative work.

**Forbidden transformation / semantic risk:** never split, merge, or vary sentence length solely to create "burstiness."

## 15. Support-script ceremony

**Cues:** long acknowledgements, repeating the user's request, `حتماً با کمال میل`, empty closings, or vague promises such as `در اسرع وقت`.

**Cluster signal:** social ritual is longer than the answer/status/next action.

**False positives / genre license:** channels where hospitality, formality, or an open invitation is expected.

**Correction:** prefer acknowledgement → answer/status → next action, with the minimum politeness needed for the relationship.

**Forbidden transformation / semantic risk:** do not invent resolution time, guarantees, escalation, or commitments.

## 16. Academic significance inflation

**Cues:** `به‌وضوح نشان می‌دهد`, `تحولی قابل توجه`, `نقش کلیدی`, broad future or external-validity claims unsupported by the cited result.

**Cluster signal:** evaluative wording is stronger than the evidence or removes hedging.

**False positives / genre license:** claims directly supported by the study design, data, and cited evidence.

**Correction:** preserve measured uncertainty and scope the claim to the reported conditions.

**Forbidden transformation / semantic risk:** do not change citation scope, confidence, limitations, or causal status.

## 17. Artificial balance or neutrality

**Cues:** automatic `مزایا و چالش‌ها`, `از یک سو / از سوی دیگر`, or a generic counterpoint added to make an argument look balanced.

**Cluster signal:** the counterpoint has no evidence or relevance to the source's actual purpose.

**False positives / genre license:** analysis where competing evidence genuinely exists.

**Correction:** preserve the writer's supported position and real limitations.

**Forbidden transformation / semantic risk:** do not remove genuine counterevidence or turn cautious analysis into advocacy.

## 18. Over-polished, personality-free prose

**Cues:** contractions, bluntness, humor, recurring vocabulary, emphasis, code-switching, and writer-specific rhythm disappear even though they were not defects.

**Cluster signal:** the rewrite is grammatically smooth but sounds like a generic corporate or essay voice.

**False positives / genre license:** user explicitly requested a new brand voice, formalization, standardization, or ghostwriting.

**Correction:** restore voice fingerprints and keep already-effective wording.

**Forbidden transformation / semantic risk:** do not replace the writer's stance, politeness, hedging, emotional intensity, dialect, or first-person habits without instruction.

## Integrity boundary

Never treat these as legitimate humanization techniques:

- detector optimization;
- deliberate typos or grammar errors;
- hidden/invisible Unicode or homoglyphs;
- random punctuation or spacing attacks;
- arbitrary synonym rotation;
- random sentence-length variation;
- fabricated anecdotes, sources, metrics, reactions, opinions, uncertainty, or experiences.

The target is better Persian, not a lower detector score.
