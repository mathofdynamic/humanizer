# Humanizer Test Cases

These are behavioral fixtures for a Persian writing skill. They test writing quality, meaning preservation, register control, and protected content—not authorship detection or detector evasion.

There is no single correct rewrite. Evaluate each case against the listed characteristics and forbidden changes. An acceptable result may use different words or sentence boundaries while preserving the same constraints.

## 1. Overly formal Persian

### Input

«بدین‌وسیله به استحضار می‌رساند درخواست شما در حال بررسی می‌باشد و نتیجه نهایی متعاقباً اعلام خواهد گردید.»

### Should detect

`بدین‌وسیله`, `به استحضار می‌رساند`, `می‌باشد`, and `اعلام خواهد گردید` create bureaucratic padding. The formal channel itself is not a problem.

### Acceptable rewrite characteristics

Keep a formal, courteous support register and use direct forms such as «درخواست شما در حال بررسی است». State the next communication without adding a deadline.

### Forbidden changes

Do not make it slangy, claim approval, invent a timeframe, or remove the status information.

## 2. Generic AI-style blog introduction

### Input

«در دنیای امروز، فناوری با سرعتی بی‌سابقه در حال پیشرفت است. در عصر حاضر، اهمیت این موضوع بر کسی پوشیده نیست. در این مقاله قصد داریم به بررسی نقش آن در زندگی روزمره بپردازیم.»

### Should detect

Ceremonial openings, repeated time framing, unsupported generality, and an essay-boilerplate promise to discuss the topic.

### Acceptable rewrite characteristics

Start with the actual topic or claim. Keep only context that helps the reader understand the article, and use a specific consequence if the source provides one.

### Forbidden changes

Do not add statistics, trends, examples, or a stronger thesis that the input does not support.

## 3. Marketing copy

### Input

«با استفاده از این راهکار جامع و قدرتمند، تجربه‌ای بی‌نظیر و منحصربه‌فرد را در سطحی جدید تجربه کنید. این محصول نوآورانه و پیشرفته، تحولی بزرگ در کسب‌وکار شما ایجاد می‌کند.»

### Should detect

Stacked promotional adjectives, duplicated praise, and a promise of transformation without a concrete mechanism or outcome.

### Acceptable rewrite characteristics

Keep persuasive intent and brand energy, but lead with a concrete capability or user benefit already supported by the source. Remove unsupported superlatives.

### Forbidden changes

Do not invent features, metrics, customers, market position, or a guaranteed business result.

## 4. Customer-support message

### Input

«ضمن تشکر از همراهی شما، به اطلاع می‌رساند مشکل اعلام‌شده در دست بررسی می‌باشد و تیم فنی در اسرع وقت نسبت به رفع آن اقدام خواهد نمود. از صبوری شما سپاسگزاریم.»

### Should detect

Ceremonial framing, `می‌باشد`, `در اسرع وقت`, `نسبت به رفع ... اقدام خواهد نمود`, and a vague promise. Some politeness is appropriate.

### Acceptable rewrite characteristics

Use a direct acknowledgement, current status, and next action. Preserve the fact that the technical team is investigating and keep a concise polite closing if the channel requires it.

### Forbidden changes

Do not promise resolution, add a deadline, remove a ticket or incident detail, or make the message dismissive.

## 5. Telegram or social-media text

### Input

«سلام بچه‌ها. در عصر حاضر، لازم به ذکر است که دورهمی فردا در راستای ایجاد تعامل بیشتر برگزار می‌گردد. بدین منظور لطفاً رأس ساعت ۸ تشریف بیارید.»

### Should detect

Register collision: formal and ceremonial phrases in an informal group message. The time and invitation are useful facts.

### Acceptable rewrite characteristics

Use natural spoken Persian suited to the writer and channel, for example a shorter invitation that preserves the date/time and purpose. Keep the existing level of warmth.

### Forbidden changes

Do not add fake typos, slang, emojis, or a more familiar relationship than the source establishes. Do not change the time.

## 6. Academic writing

### Input

«نتایج به‌دست‌آمده به‌وضوح نشان می‌دهد که روش پیشنهادی تحولی قابل توجه در این حوزه ایجاد کرده و می‌تواند نقش کلیدی در پژوهش‌های آینده ایفا کند.»

### Should detect

Unsupported significance (`تحولی قابل توجه`, `نقش کلیدی`) and a broad future claim. The academic register should remain formal and cautious.

### Acceptable rewrite characteristics

Tie the sentence to the reported experiment or metric if the input contains one; otherwise use a modest claim such as improvement under the reported conditions. Preserve justified uncertainty.

### Forbidden changes

Do not invent a baseline, result, dataset, limitation, citation, or external validity claim. Do not turn the paragraph into casual Persian.

## 7. Technical documentation

### Input

«این endpoint به‌عنوان بستری برای احراز هویت عمل می‌نماید و امکان ارسال توکن را فراهم می‌آورد. به‌منظور استفاده از آن، کاربر می‌بایست ابتدا درخواست را ارسال نموده و سپس پاسخ را مورد بررسی قرار دهد.»

### Should detect

Indirect verbs and bureaucratic technical phrasing: `عمل می‌نماید`, `فراهم می‌آورد`, `به‌منظور`, `می‌بایست`, `ارسال نموده`, and `مورد بررسی قرار دهد`.

### Acceptable rewrite characteristics

Use concise, unambiguous instructions and preserve `endpoint`, token behavior, request order, and any API terminology. Keep passive voice only when it is clearer.

### Forbidden changes

Do not rename an API concept, alter the request/response sequence, change a command, or translate a protected identifier.

## 8. Translated-English Persian

### Input

«این قابلیت یک نقش مهم در تجربه کاربری بازی می‌کند و به کاربران اجازه می‌دهد که آن‌ها فایل را آپلود کرده و خروجی را دریافت نمایند.»

### Should detect

English-shaped collocations, an unnecessary pronoun, a heavy noun phrase, and an indirect verb. The intended behavior is still clear.

### Acceptable rewrite characteristics

Use native Persian information flow and direct verbs, such as «این قابلیت به کاربر اجازه می‌دهد فایل را آپلود کند و خروجی بگیرد»، while preserving the capability and technical term if appropriate.

### Forbidden changes

Do not infer a different user role, add a file format, promise speed, or replace an established technical term without reason.

## 9. Bullet-heavy writing

### Input

«مزایای این سرویس عبارت‌اند از:

- این سرویس فرایند ثبت درخواست را ساده می‌کند و به کاربران امکان می‌دهد اطلاعات خود را در یک محیط یکپارچه وارد کنند.
- این سرویس با ارائه گزارش‌های دقیق، دید جامعی از وضعیت فرایند در اختیار مدیران قرار می‌دهد.
- این سرویس با استفاده از ابزارهای پیشرفته، تجربه‌ای متفاوت و راهکاری نوآورانه برای تیم‌ها فراهم می‌کند.»

### Should detect

Three parallel bullets mix concrete behavior with generic claims, and each bullet is a long mini-paragraph. The list may still be appropriate if the items are product features.

### Acceptable rewrite characteristics

Keep a compact list if the items are genuinely parallel, or turn them into prose if they form one explanation. Remove unsupported praise and preserve each distinct capability.

### Forbidden changes

Do not delete a real requirement, merge unrelated features, reorder a workflow, or invent what the reports contain.

## 10. Repetitive transitions

### Input

«علاوه بر این، سامانه گزارش‌ها را ذخیره می‌کند.

همچنین، کاربران می‌توانند گزارش‌ها را به‌صورت PDF دریافت کنند.

از سوی دیگر، مدیران امکان مشاهده وضعیت درخواست‌ها را دارند.

در نتیجه، این سامانه راهکاری جامع و قدرتمند برای مدیریت فرایندهاست.»

### Should detect

Repeated paragraph-opening transitions and a generic conclusion that restates the features as praise.

### Acceptable rewrite characteristics

Keep a connector only where the relationship matters, vary the paragraph openings naturally, and end with a concrete consequence or stop after the last supported feature.

### Forbidden changes

Do not remove the PDF capability, change who can see the requests, or turn the final sentence into a stronger product claim.

## 11. Already-good Persian

### Input

«نسخه جدید امروز منتشر شد. زمان بارگذاری صفحه اصلی کمتر شده و تنظیمات قبلی هم باقی مانده است. اگر مشکلی دیدید، در issue گزارش دهید.»

### Should detect

No required style problem. The mix of Persian and `issue` may be intentional technical usage, and `هم` gives the sentence a natural tone.

### Acceptable rewrite characteristics

Leave it unchanged or make only a clearly justified punctuation or terminology correction. Preserve its concise semi-formal register.

### Forbidden changes

Do not add an introduction, transitions, synonyms, a conclusion, or more formal vocabulary just to show activity.

## 12. Intentionally colloquial Persian

### Input

«راستش این اپ رو برای کارهای روزمره‌م دوست دارم. سریع باز می‌شه، ولی بخش جست‌وجوش هنوز یه کم اذیتم می‌کنه.»

### Should detect

No artificial pattern requires correction. Contractions and the personal evaluation are part of the voice.

### Acceptable rewrite characteristics

Preserve `رو`, `می‌شه`, `یه کم`, and the informal cadence. Edit only if the user requests a different register or a specific clarity fix.

### Forbidden changes

Do not convert it into formal prose, add corporate praise, replace the personal view with a generic claim, or manufacture slang.

## 13. Persian mixed with English technical terminology

### Input

«برای deploy سرویس، اول `.env.example` را کپی کن، مقدار `DATABASE_URL` را تنظیم کن و بعد `npm run build` را اجرا کن. API در endpoint `/v1/jobs` درخواست‌های جدید را می‌گیرد.»

### Should detect

No automatic problem. English technical terms, code spans, environment variable names, commands, and the endpoint are protected or intentionally used by the audience.

### Acceptable rewrite characteristics

Improve only surrounding Persian if needed. Keep every code span, identifier, command, path, and API term exact; keep the instructional register consistent.

### Forbidden changes

Do not translate or reformat code, rename `DATABASE_URL`, change the command, alter the endpoint, or introduce a different deployment step.

## 14. Quoted material that must remain untouched

### Input

مدیر در اطلاعیه نوشت: «در راستای ارتقای کیفیت، بدین‌وسیله اعلام می‌گردد که فرایند جدید از فردا اجرا خواهد شد.» سپس تیم توضیح کوتاهی درباره مراحل اجرا منتشر کرد.

### Should detect

The quoted announcement contains bureaucratic phrasing, but it is attributed and protected. The surrounding sentence can be edited if it is awkward.

### Acceptable rewrite characteristics

Leave the quotation and attribution unchanged. If requested, make a minimal edit only to the surrounding narration, such as making the second sentence more direct.

### Forbidden changes

Do not modernize the quote, alter its punctuation or meaning, change the speaker, or present the quoted wording as the editor's own claim.

## 15. Factual and citation-heavy text

### Input

«طبق گزارش مرکز آمار ایران، در سال ۱۴۰۲ تعداد کاربران این خدمت به ۲٫۴ میلیون نفر رسید [1]. با توجه به موارد فوق، می‌توان گفت این روند گامی مهم در راستای تحول دیجیتال کشور محسوب می‌گردد.»

### Should detect

`با توجه به موارد فوق`, `گامی مهم`, `در راستای`, and `محسوب می‌گردد` add a generic conclusion. The institution, year, number, and citation are protected factual content.

### Acceptable rewrite characteristics

Keep the source name, Persian digits, number, year, citation marker, and cautious level of the claim. Replace or remove the generic conclusion without adding an interpretation that the citation does not support.

### Forbidden changes

Do not change `۱۴۰۲`, `۲٫۴`, `[1]`, the institution, the cited claim, or the certainty level. Do not add a link, source, comparison, or causal explanation.
