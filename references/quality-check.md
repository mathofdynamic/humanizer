# Final Quality Check

Use this protocol after a rewrite or targeted file edit, especially for public, factual, academic, commercial, technical, legal-adjacent, or long-form text. It is a verification step, not a reason to keep rewriting.

## 1. Protected-span hard gate

Confirm that every protected item is exact unless the user explicitly authorized editing it:

- names
- numbers and quantities
- dates and times
- citations and quotation text
- URLs, paths, code, commands, identifiers
- model/product/API names
- table data and structural Markdown
- fixed terminology
- legally or technically mandated phrases

Any unauthorized change is a failure, even if the new prose sounds better.

## 2. Semantic ledger

Compare source and result proposition by proposition.

Check:

- **actor:** who did or will do the action?
- **action:** what actually happened or is required?
- **object:** what is affected?
- **polarity:** did positive/negative meaning change?
- **modality:** did `ممکن است`, `احتمالاً`, `باید`, `می‌تواند`, or certainty level change?
- **quantity/date:** did a number, range, unit, date, or timeframe change?
- **condition:** did an `اگر`, prerequisite, limitation, or exception disappear?
- **causality:** did correlation become cause, or did a causal link disappear?
- **scope:** did the claim become broader or narrower?
- **attribution:** is the same person/source responsible for the claim?
- **capability:** did the edit add or remove a product/system behavior?
- **obligation:** did legal, policy, or procedural force change?

If any material difference is not explicitly requested, revert it.

## 3. Unsupported-information hard gate

The rewrite must not add:

- facts, examples, statistics, metrics, dates, deadlines
- actors or mechanisms not identified by the source
- customer reactions, market position, guarantees, promises
- new citations or authorities
- personal experience, opinion, emotion, or uncertainty
- causal explanations that were not present

A slightly formulaic but faithful sentence is preferable to a polished sentence that invents information.

## 4. Intervention audit

For each changed span, ask:

1. What exact defect was diagnosed?
2. Did the edit fix that defect?
3. Could a smaller change have done the job?
4. Did the edit remove a useful voice fingerprint?
5. Would `KEEP` have been better?

Already-natural text should survive unchanged except for explicitly permitted mechanical corrections.

## 5. Register and voice

Confirm that:

- the genre is still the same unless the user requested a change;
- formality and politeness fit the audience/channel;
- academic hedging remains calibrated;
- legal/administrative force remains intact;
- marketing still persuades without invented evidence;
- colloquial contractions and dialect remain when intentional;
- technical terms and code-switching remain stable;
- humor, irony, bluntness, first-person use, and emotional intensity were not flattened.

## 6. Persian discourse and mechanics

Confirm that:

- reference remains clear after pronoun removal or clause reordering;
- topic changes are explicit enough to avoid ambiguity;
- discourse markers express real relations;
- repeated structures remain only when useful or intentional;
- paragraph boundaries follow ideas rather than a template;
- sentence length changed only for a linguistic reason;
- Persian `ی` and `ک`, punctuation, spacing, and reasonable نیم‌فاصله fit the chosen register;
- code, URLs, identifiers, and quotations were excluded from normalization.

## 7. Hard-failure conditions

Treat the result as failed if it:

- changes a protected factual token without authorization;
- invents information;
- changes material modality, causality, scope, capability, or obligation;
- corrupts code, URLs, tables, paths, or Markdown semantics;
- replaces stable technical terminology merely for variety;
- shifts the communicative function by casualizing/formalizing the text;
- modifies quotations or fixed legal wording without permission.

## Final editor question

Does every changed span have a concrete reason tied to this audience, genre, and writer?

If not, restore the unnecessary change. Once diagnosed defects are resolved and invariants hold, stop.
