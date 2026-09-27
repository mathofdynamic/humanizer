# Round 1 — Reference Merge Report

## Changed files

- `references/patterns.md` — made status/action-first edits preserve source intent; tightened substantiation rules for marketing, abstract benefits, and significance claims.
- `references/quality-check.md` — added speech-act checks, unsupported-addition auditing, procedure sequence/warning checks, and substantiation checks for evaluative claims.
- `references/voice-and-intervention.md` — tied cushioning to face-threat and clarified that `REWRITE` does not permit new facts or intentions.
- `references/genre-matrix.md` — distinguished dependent procedures from simple condition/action instructions and clarified claim scope in news and marketing.
- `references/evaluation.md` — added a separate fabrication check after the initial pairwise preference.

**Adjustment from proposal:** The evaluative-claim checklist item in `quality-check.md` was phrased declaratively to match the existing checklist grammar. No target section had drifted from the proposal.

## Validation

- `python tests/validate_repository.py` — **PASS**. Output: “Humanizer validation passed: 16 required files, UTF-8, links, frontmatter, references, 25 behavioral tests, benchmark fixtures, and junk-file checks.”
- Errors: none.
- `git diff --check` — no whitespace errors. Git emitted LF-to-CRLF conversion notices for modified Markdown files.

## KEEP-regression spot check

**Method:** Reasoned review, not execution. This repository has no standalone runner for applying the Humanizer prompt to samples. Each sample was checked against the Humanizer workflow and all seven current files in `/references/`, including genre, voice, semantic, intervention, and mechanics guidance.

**Result:** 5/5 samples remain `KEEP`; 0 unnecessary edits. The stop threshold of two regressions was not reached.

1. **Personal, informal — KEEP**

   > ببخش که دقیقه‌نودی می‌گم؛ امشب نمی‌تونم بیام. می‌دونم قرار گذاشته بودیم، جبران می‌کنم.

   The apology and cushioning fit the cancellation; the informal voice and all three speech acts are clear and need no edit.

2. **Professional email — KEEP**

   > سلام خانم احمدی، فایل اصلاح‌شده را پیوست کردم. اگر نکته‌ای مانده، تا ظهر فردا خبرم کنید تا همان روز انجامش بدهم.

   Status, conditional request, deadline, and commitment are direct and explicit; no administrative wrapper or unsupported promise needs correction.

3. **Academic — KEEP**

   > در این نمونه، میان سن و میزان استفاده از برنامه همبستگی دیده شد. از آنجا که داده‌ها در یک مقطع جمع‌آوری شده‌اند، نمی‌توان از این یافته رابطهٔ علّی استنباط کرد.

   The prose preserves scope, method, and uncertainty without turning correlation into causation or inflating significance.

4. **Technical instruction — KEEP**

   > برای گرفتن خروجی PDF، از منوی File گزینهٔ Export را باز کنید و قالب PDF را انتخاب کنید.

   The ordered UI instruction is already clear; stable interface terms and the step sequence should remain intact.

5. **Product description — KEEP**

   > این برنامه مجموعه‌ای جامع برای یادداشت‌برداری است؛ یادداشت‌ها را می‌شود بر اساس موضوع دسته‌بندی کرد، بین گوشی و لپ‌تاپ همگام‌سازی کرد و برایشان یادآور گذاشت.

   The listed functions substantiate “جامع”; the descriptor summarizes the supplied specifics rather than standing alone as unsupported praise.
