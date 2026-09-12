# Voice Preservation and Intervention

Humanizer should behave closer to a native copy editor than a ghostwriter unless the user explicitly asks for a new voice.

## 1. Voice fingerprints

Treat these as protected or semi-protected when they are observable in the source.

| Fingerprint | Default |
| --- | --- |
| preferred recurring vocabulary | protect |
| domain terminology | hard protect |
| formality level | protect |
| colloquial contractions | protect |
| dialectal forms | protect |
| hedging / certainty habits | hard protect semantically |
| humor, irony, sarcasm | protect semantically and pragmatically |
| bluntness / directness | protect |
| politeness level | protect unless channel clearly requires correction |
| emotional intensity | protect |
| code-switching preference | protect unless clearly accidental |
| first-person use or avoidance | protect |
| intentional repetition | protect |
| recurring expressions/catchphrases | soft protect |
| characteristic long/short sentence habits | soft protect |
| parenthetical habit | soft protect; edit only when readability is harmed |

Do not create a generic "better Persian voice." Recover this writer's best version of the existing voice.

## 2. Intervention gate

Choose the smallest sufficient level.

### KEEP

Use when:

- the text is already natural for its audience and genre;
- the only "problem" is a phrase that is legitimate in context;
- a change would be merely stylistic preference;
- the source contains intentional colloquial, formal, technical, or rhetorical choices.

Allowed output: source unchanged.

### MINOR

Use for local defects that do not require structural rewriting:

- one unnecessary pronoun;
- local bureaucratic padding;
- punctuation/spacing issue;
- one weak connector;
- one unclear referent;
- one register collision;
- local orthographic cleanup.

Do not rewrite neighboring natural sentences.

### REWRITE

Use when structure is the problem:

- English-shaped clause architecture;
- repeated formulaic paragraph skeleton;
- a long nominal chain that obscures action;
- false symmetry or bullet inflation;
- multiple interacting patterns that cannot be fixed safely by substitution.

Rewrite only the affected span.

### FLAG

Use when a safe edit requires information the source does not provide:

- actor is unknown but needed for a direct active sentence;
- legal force is unclear;
- technical terminology may be fixed by policy;
- ambiguity prevents safe pronoun removal;
- vague claim cannot be made concrete without evidence;
- quotation/fixed wording appears awkward but is protected.

## 3. Decision questions

Before editing a span, ask:

1. What exact defect is present?
2. Is the defect contextual, or am I reacting to a word on a list?
3. Does this genre license the construction?
4. Is the writer using it intentionally for emphasis, voice, or precision?
5. Can a smaller edit fix the problem?
6. Could the edit alter meaning, uncertainty, causality, obligation, attribution, or capability?

If the defect cannot be named clearly, prefer `KEEP`.

## 4. Copy editing vs style rewriting

Default Humanizer behavior is copy/stylistic editing:

- improve clarity and naturalness;
- repair local syntax and discourse;
- preserve structure when it already works;
- preserve voice;
- minimize semantic risk.

Substantive rewriting is justified only when the existing structure itself creates the diagnosed problem or the user explicitly requests broader rewriting.

## 5. Stop rule

After one rewrite and one bounded verification pass, stop when:

- diagnosed defects are resolved;
- protected spans are intact;
- semantic invariants hold;
- register and voice remain appropriate;
- no new ambiguity was introduced.

Do not keep iterating toward "more human." Zero catalog matches is not a meaningful target.
