# Humanizer Test Cases

These are behavioral fixtures for a Persian writing skill. They test naturalness, semantic preservation, register control, voice preservation, protected content, and unnecessary editing—not authorship detection.

There is no single correct rewrite. Evaluate each case against the listed diagnosis, expected intervention, and forbidden changes.

## 1. Overly formal Persian

**Input:** «بدین‌وسیله به استحضار می‌رساند درخواست شما در حال بررسی می‌باشد و نتیجه نهایی متعاقباً اعلام خواهد گردید.»

**Expected intervention:** `MINOR`

**Should detect:** bureaucratic padding in an ordinary support-style status message.

**Forbidden:** slang, invented approval, invented timeframe, removal of status.

## 2. Generic AI-style blog introduction

**Input:** «در دنیای امروز، فناوری با سرعتی بی‌سابقه در حال پیشرفت است. در عصر حاضر، اهمیت این موضوع بر کسی پوشیده نیست. در این مقاله قصد داریم به بررسی نقش آن در زندگی روزمره بپردازیم.»

**Expected intervention:** `REWRITE`

**Should detect:** ceremonial framing, stacked time phrases, roadmap before content.

**Forbidden:** invented statistics, examples, trend claims, or stronger thesis.

## 3. Marketing copy

**Input:** «با استفاده از این راهکار جامع و قدرتمند، تجربه‌ای بی‌نظیر و منحصربه‌فرد را در سطحی جدید تجربه کنید. این محصول نوآورانه و پیشرفته، تحولی بزرگ در کسب‌وکار شما ایجاد می‌کند.»

**Expected intervention:** `REWRITE`

**Should detect:** unsupported adjective stack and transformation promise.

**Forbidden:** invented features, metrics, customers, market position, guaranteed results.

## 4. Customer-support message

**Input:** «ضمن تشکر از همراهی شما، به اطلاع می‌رساند مشکل اعلام‌شده در دست بررسی می‌باشد و تیم فنی در اسرع وقت نسبت به رفع آن اقدام خواهد نمود. از صبوری شما سپاسگزاریم.»

**Expected intervention:** `MINOR`

**Should detect:** ceremony, vague deadline language, padded verb forms.

**Forbidden:** promise of resolution or new deadline.

## 5. Telegram or social-media text

**Input:** «سلام بچه‌ها. در عصر حاضر، لازم به ذکر است که دورهمی فردا در راستای ایجاد تعامل بیشتر برگزار می‌گردد. بدین منظور لطفاً رأس ساعت ۸ تشریف بیارید.»

**Expected intervention:** `REWRITE`

**Should detect:** register collision.

**Forbidden:** fake typos, new slang, emojis, changed time.

## 6. Academic writing

**Input:** «نتایج به‌دست‌آمده به‌وضوح نشان می‌دهد که روش پیشنهادی تحولی قابل توجه در این حوزه ایجاد کرده و می‌تواند نقش کلیدی در پژوهش‌های آینده ایفا کند.»

**Expected intervention:** `MINOR`

**Should detect:** significance inflation and broad future claim.

**Forbidden:** invented baseline, dataset, citation, limitation, or stronger certainty.

## 7. Technical documentation

**Input:** «این endpoint به‌عنوان بستری برای احراز هویت عمل می‌نماید و امکان ارسال توکن را فراهم می‌آورد. به‌منظور استفاده از آن، کاربر می‌بایست ابتدا درخواست را ارسال نموده و سپس پاسخ را مورد بررسی قرار دهد.»

**Expected intervention:** `REWRITE`

**Should detect:** bureaucratic technical phrasing.

**Forbidden:** renamed API concept, changed order, changed command or token behavior.

## 8. Translated-English Persian

**Input:** «این قابلیت یک نقش مهم در تجربه کاربری بازی می‌کند و به کاربران اجازه می‌دهد که آن‌ها فایل را آپلود کرده و خروجی را دریافت نمایند.»

**Expected intervention:** `REWRITE`

**Should detect:** literal predicate, unnecessary pronoun, indirect verb.

**Forbidden:** different user role, file format, speed promise, new capability.

## 9. Bullet-heavy writing

**Input:** «مزایای این سرویس عبارت‌اند از: ۱) ثبت درخواست را ساده می‌کند. ۲) گزارش در اختیار مدیران می‌گذارد. ۳) تجربه‌ای نوآورانه و پیشرفته ایجاد می‌کند.»

**Expected intervention:** `MINOR`

**Should detect:** concrete items mixed with generic praise.

**Forbidden:** deletion of real capability or invented report content.

## 10. Repetitive transitions

**Input:** «علاوه بر این، سامانه گزارش‌ها را ذخیره می‌کند. همچنین، کاربران می‌توانند گزارش‌ها را به‌صورت PDF دریافت کنند. از سوی دیگر، مدیران امکان مشاهده وضعیت درخواست‌ها را دارند. در نتیجه، این سامانه راهکاری جامع و قدرتمند است.»

**Expected intervention:** `REWRITE`

**Should detect:** marker density and generic conclusion.

**Forbidden:** removal of PDF capability or actor permissions.

## 11. Already-good Persian

**Input:** «نسخه جدید امروز منتشر شد. زمان بارگذاری صفحه اصلی کمتر شده و تنظیمات قبلی هم باقی مانده است. اگر مشکلی دیدید، در issue گزارش دهید.»

**Expected intervention:** `KEEP`

**Should detect:** no required style defect.

**Forbidden:** introduction, synonym rotation, conclusion, unnecessary formalization.

## 12. Intentionally colloquial Persian

**Input:** «راستش این اپ رو برای کارهای روزمره‌م دوست دارم. سریع باز می‌شه، ولی بخش جست‌وجوش هنوز یه کم اذیتم می‌کنه.»

**Expected intervention:** `KEEP`

**Should detect:** contractions and personal voice are intentional.

**Forbidden:** standardization, corporate praise, manufactured slang.

## 13. Persian mixed with English technical terminology

**Input:** «برای deploy سرویس، اول `.env.example` را کپی کن، مقدار `DATABASE_URL` را تنظیم کن و بعد `npm run build` را اجرا کن. API در endpoint `/v1/jobs` درخواست‌های جدید را می‌گیرد.»

**Expected intervention:** `KEEP`

**Should detect:** protected technical mixing, not a defect.

**Forbidden:** changing any code span, identifier, command, path, or API term.

## 14. Quoted material that must remain untouched

**Input:** مدیر نوشت: «در راستای ارتقای کیفیت، بدین‌وسیله اعلام می‌گردد که فرایند جدید از فردا اجرا خواهد شد.» سپس تیم مراحل اجرا را توضیح داد.

**Expected intervention:** `KEEP` or `MINOR` outside the quote only.

**Should detect:** bureaucratic wording is protected quotation.

**Forbidden:** any quotation change.

## 15. Factual and citation-heavy text

**Input:** «طبق گزارش مرکز آمار ایران، در سال ۱۴۰۲ تعداد کاربران این خدمت به ۲٫۴ میلیون نفر رسید [1]. با توجه به موارد فوق، می‌توان گفت این روند گامی مهم در راستای تحول دیجیتال کشور محسوب می‌گردد.»

**Expected intervention:** `MINOR`

**Should detect:** generic conclusion while preserving the factual sentence.

**Forbidden:** changes to `۱۴۰۲`, `۲٫۴`, `[1]`, institution, or certainty.

## 16. Redundant subject pronouns

**Input:** «ما گزارش را بررسی کردیم و ما متوجه شدیم که چند ردیف تکراری است.»

**Expected intervention:** `MINOR`

**Should detect:** second overt `ما` is unnecessary if no contrast exists.

**Forbidden:** removing first-person authorship or changing the finding.

## 17. Ambiguous subject switch

**Input:** «علی با رضا صحبت کرد و گفت فردا نسخه را می‌فرستد.»

**Expected intervention:** `FLAG`

**Should detect:** pronoun/zero-subject resolution is ambiguous.

**Forbidden:** guessing whether Ali or Reza sends the version.

## 18. Legal formula

**Input:** «مستأجر موظف می‌باشد مبلغ اجاره را تا روز پنجم هر ماه پرداخت نماید.»

**Expected intervention:** `KEEP` or `FLAG`

**Should detect:** formal forms may carry legal genre expectations.

**Forbidden:** changing obligation, deadline, actor, or legal force.

## 19. Academic hedge

**Input:** «این یافته‌ها ممکن است نشان دهد که متغیر X با Y مرتبط است، اما برای نتیجه‌گیری علّی داده کافی نداریم [4].»

**Expected intervention:** `KEEP`

**Should detect:** calibrated uncertainty and limitation are valuable.

**Forbidden:** changing `ممکن است`, causal status, or citation.

## 20. News attribution

**Input:** «سخنگوی وزارتخانه گفت طرح از مهر اجرا می‌شود. سخنگوی وزارتخانه افزود جزئیات آیین‌نامه هفته آینده منتشر خواهد شد.»

**Expected intervention:** `MINOR` or `KEEP`

**Should detect:** repeated attribution may be justified for clarity.

**Forbidden:** ambiguous pronoun replacement or changed chronology.

## 21. Brand slogan repetition

**Input:** «کمتر کلیک کن. کمتر منتظر بمان. کمتر وقت تلف کن.»

**Expected intervention:** `KEEP`

**Should detect:** repetition is intentional rhetoric.

**Forbidden:** synonym variation or prose conversion.

## 22. Over-explained instruction

**Input:** «برای ذخیره فایل، روی دکمه ذخیره کلیک کنید. با کلیک روی این دکمه، فایل ذخیره می‌شود.»

**Expected intervention:** `MINOR`

**Should detect:** second sentence is tautological for the stated audience.

**Forbidden:** removal of a real prerequisite if one exists outside the fixture.

## 23. Fake precision risk

**Input:** «این تغییر عملکرد سامانه را بهتر می‌کند.»

**Expected intervention:** `KEEP` or `FLAG`

**Should detect:** vague claim may be weak, but source gives no metric.

**Forbidden:** adding `۳۰٪`, benchmark, mechanism, or guarantee.

## 24. Sarcasm

**Input:** «عالیه؛ دقیقاً چیزی که لازم داشتیم: یک فرم دیگر با ده تا فیلد اجباری.»

**Expected intervention:** `KEEP`

**Should detect:** irony and frustration are voice.

**Forbidden:** rewriting into sincere praise or neutral documentation.

## 25. Mixed Markdown and code

**Input:** «### نصب\nاول `pip install foo` را اجرا کن. بعد مقدار `FOO_TOKEN` را در `.env` بگذار.»

**Expected intervention:** `KEEP`

**Should detect:** structure and technical tokens are protected.

**Forbidden:** changing heading level, code, variable name, file name, or step order.
