# Edge-Case Expectations

These cases exist to prevent over-editing. For each one, semantic and genre safety outrank stylistic smoothness.

## 1. Legal or contractual Persian

Expected: preserve defined terms, obligation, permission, scope, exceptions, repeated legal terms, and fixed formulae. Prefer `FLAG` over simplification when legal force could change.

## 2. Academic hedging

Expected: preserve `ممکن است`, `احتمالاً`, `به نظر می‌رسد`, confidence language, limitations, and citation scope. Do not turn evidence into certainty.

## 3. Awkward quotation

Expected: leave quotation exact. Edit surrounding attribution only if requested.

## 4. Historical or ceremonial Persian

Expected: do not modernize morphology, vocabulary, punctuation style, or ceremony unless modernization is the task.

## 5. Fixed corporate terminology

Expected: preserve glossary terms even when repetitive. Terminology consistency outranks synonym variety.

## 6. Brand slogan with repetition

Expected: preserve deliberate repetition and rhythm unless the user asks for alternative copy.

## 7. Poetry or highly literary prose

Expected: default to `KEEP` or `FLAG`. Ordinary prose rules about fragments, repetition, inversion, or punctuation may not apply.

## 8. Sarcasm and irony

Expected: preserve pragmatic reversal and intensity. Do not "clarify" sarcasm into a sincere literal statement.

## 9. Dialect or regional Persian

Expected: preserve dialectal morphology and vocabulary. Standardization requires explicit instruction.

## 10. Non-native Persian

Expected: correct genuine clarity/grammar problems without erasing the writer's intended register. Do not fabricate native slang to disguise authorship.

## 11. Mixed RTL/LTR technical text

Expected: protect code, paths, flags, package names, model names, numbers, and direction-sensitive tokens. Edit only surrounding prose.

## 12. Markdown-heavy document

Expected: preserve heading hierarchy, list semantics, code fences, links, tables, and inline code. Do not turn structure into prose solely for style.

## 13. News attribution

Expected: repeated actor/source names may be necessary. Do not over-apply pronoun omission where attribution could become ambiguous.

## 14. Government template

Expected: bureaucratic forms may be procedurally required. Do not replace them merely because they appear in the pattern catalog.

## 15. Marketing claim with no evidence

Expected: remove or soften unsupported praise; do not invent proof, numbers, testimonials, or capabilities to make the copy more concrete.
