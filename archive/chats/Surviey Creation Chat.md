# gemini response

Here are the complete translations and the automated script to build it cleanly.

---

### Step 1: The Automated Google Apps Script
Instead of typing every question manually across 3 languages:

1. Open your browser and go to [script.google.com](https://script.google.com).
2. Click **New project**.
3. Clear out whatever code is there and **paste the code block below**.
4. Click the **Save** icon, then click **Run**.
5. Grant permissions if prompted. 
6. Open your [Google Forms Dashboard](https://forms.google.com) — your 3-language Cheapify survey will be ready with sections and routing set up.

```javascript
function createCheapifySurvey() {
  var form = FormApp.create('Cheapify Market Validation Survey | راپرسی | استطلاع');
  form.setDescription('Validation research on online shopping and pricing across Iraq / KRI.');

  // Language Selection Section
  var langItem = form.addMultipleChoiceItem();
  langItem.setTitle('Choose your language / زمانێ خۆ هەلبژێرە / اختر لغتك')
          .setRequired(true);

  // --- ENGLISH FLOW ---
  var secEnRole = form.addPageBreakItem().setTitle('Role Selection (English)');
  var enRole = form.addMultipleChoiceItem().setTitle('I mainly use social media/apps to:').setRequired(true);
  
  var secEnBuyer = form.addPageBreakItem().setTitle('Cheapify — Buyer Survey (English)');
  var enB1 = form.addMultipleChoiceItem().setTitle('How often do you shop online from Facebook, Instagram, or local apps?')
      .setChoiceValues(['Weekly', 'A few times a month', 'Rarely', 'Never']);
  var enB2 = form.addMultipleChoiceItem().setTitle('When searching for a product, do you notice big price differences for the exact same item across pages?')
      .setChoiceValues(['Yes, constantly (large gaps)', 'Sometimes', 'Rarely / Never', 'No, prices are similar']);
  var enB3 = form.addCheckboxItem().setTitle('What annoys you the most when shopping online locally? (Select top 2)')
      .setChoiceValues([
        'Sending DMs just to ask "Price?" / Waiting hours for replies',
        'Finding the exact same item cheaper after buying it',
        'Duplicate listings and messy feeds',
        'Lack of trust in unverified sellers',
        'Delivery delays and manual ordering'
      ]);
  var enB4 = form.addMultipleChoiceItem().setTitle('If an app showed you the exact product with every local verified seller’s price side-by-side to get the cheapest deal, would you use it?')
      .setChoiceValues(['Definitely yes', 'Probably yes', 'Maybe, depends on delivery/speed', 'No, I prefer direct DMs']);
  var enB5 = form.addTextItem().setTitle('Would you like early beta access? (Leave WhatsApp or IG handle)');

  var secEnSeller = form.addPageBreakItem().setTitle('Cheapify — Merchant Survey (English)');
  var enS1 = form.addCheckboxItem().setTitle('Where do you currently sell your products?')
      .setChoiceValues(['Instagram / Facebook page', 'TikTok live/shop', 'Physical store only', 'Marketplace apps (iBazzar, etc.)']);
  var enS2 = form.addCheckboxItem().setTitle('What is your biggest operational headache? (Select top 2)')
      .setChoiceValues([
        'Replying to repetitive "Price?" DMs from non-serious buyers',
        'Competing with arbitrary price undercutters',
        'Expensive custom website/app development',
        'Coordinating delivery and order addresses manually'
      ]);
  var enS3 = form.addMultipleChoiceItem().setTitle('If a platform listed your products under unified listings with zero tech setup fees and alerted you to stay competitive, would you test it?')
      .setChoiceValues(['Yes, definitely', 'Possibly, depends on commission', 'No, satisfied with current setup']);
  var enS4 = form.addTextItem().setTitle('Interested in joining our 5–10 pilot shops? (Store Name & Phone/WhatsApp)');

  // --- KURDISH (BADINI) FLOW ---
  var secKuRole = form.addPageBreakItem().setTitle('دیارکرنا ڕۆلی (کوردی)');
  var kuRole = form.addMultipleChoiceItem().setTitle('ئەز ب شێوەیەکێ سەرەکی سۆشیال میدیایێ بکار دئینم بۆ:').setRequired(true);

  var secKuBuyer = form.addPageBreakItem().setTitle('Cheapify — راپرسییا کڕیاران (کوردی)');
  var kuB1 = form.addMultipleChoiceItem().setTitle('چەند جار ئەنلاین یاخوود ژ پەیجێن فەیسبووک و ئینستاگرامی تشتان دکڕی؟')
      .setChoiceValues(['حەفتییانە', 'مەهانە چەند جاران', 'دەگمەن', 'چ جاران']);
  var kuB2 = form.addMultipleChoiceItem().setTitle('دەمێ ل بەرهەمەکی دگەڕی، ئایا جیاوازییا بهایان د ناڤبەرا پەیجان دا بۆ هەمان کەلوپەل دبینى؟')
      .setChoiceValues(['بەڵێ، بەردەوام (جیاوازییا مەزن یا هەی)', 'هندەک جاران', 'کێم جار', 'نەخێر، بهایێن وان نێزیکی ئێکن']);
  var kuB3 = form.addCheckboxItem().setTitle('چ تشت زێدەتر تە بێزار دکەت دەمێ ب ئۆنلاین تشتان دکڕی؟ (٢ هەلبژێرە)')
      .setChoiceValues([
        'هنارتنا نامەیان بتنێ بۆ پرسیارکرنا "ب چەندە؟" و مانا ل هیڤییا بەرسڤێ',
        'دیتنا هەمان کەلوپەل ب ئەرزانتر ئێکسەر پشتی تە کڕی',
        'پۆستێن دووبارە و نەبوونا باوەریێ ب پەیجێن نەدیار',
        'درەنگ گەهشتنا بەرهەمی و ئالۆزییا گەیاندنێ'
      ]);
  var kuB4 = form.addMultipleChoiceItem().setTitle('ئەگەر ئەپڵیکەیشنەک هەبیت کو ئێکسەر هەمی فرۆشیاران ب بهایێن وان ڤە بدانیتە تەنیشت ئێك دا ب هەرزانترین نرخ بکڕی، دێ بکارئینی؟')
      .setChoiceValues(['بێگومان بەڵێ — فەرهە', 'ڕەنگە بەڵێ', 'بەندە ل سەر لەزاتی و گەیاندنێ', 'نەخێر، نامەیێن ئاسایی باشترن']);
  var kuB5 = form.addTextItem().setTitle('حەز دکەی پشکدار بی د تاقیکرنا ڤێرژنا ئێکێ دا؟ (ژمارا واتسئەپی یان ئەکاونتێ ئینستاگرامی بنڤیسە)');

  var secKuSeller = form.addPageBreakItem().setTitle('Cheapify — راپرسییا فرۆشیاران (کوردی)');
  var kuS1 = form.addCheckboxItem().setTitle('نوکە ل کیڤە کەلوپەلێن خۆ دفرۆشی؟')
      .setChoiceValues(['پەیجێن ئینستاگرام / فەیسبووک', 'تیکتۆک', 'بتنێ دکان/مەعرەزێ فیزیکی', 'ئەپڵیکەیشنێن دی یێن ناڤخۆیی']);
  var kuS2 = form.addCheckboxItem().setTitle('مەزنترین ئاستەنگ د فرۆتنا ئۆنلاین دا بۆ تە چییە؟ (٢ هەلبژێرە)')
      .setChoiceValues([
        'بەرسڤدانا نامەیێن دووبارە یێن "ب چەندە؟"',
        'کێبڕکێیا نەدادپەروەرانە د بهایان دا',
        'تێچوویێ گران یێ چێکرنا مالپەر یان ئەپڵیکەیشنێ تایبەت',
        'رێکخستنا ناڤونیشان و گەیاندنێ ب شێوەیەکێ دەستی ب واتسئەپێ'
      ]);
  var kuS3 = form.addMultipleChoiceItem().setTitle('ئەگەر پلاتفۆرمەک هەبیت بێی تێچوویێ دەستپێکێ بەرهەمێن تە نیشان بدەت و ئاگەهدارییا بهایێن کێبڕکێیێ بدەتە تە، دێ بەشداریێ تێدا کەی؟')
      .setChoiceValues(['بەڵێ، ب دڵنیایی ڤە', 'ڕەنگە، بەندە ل سەر رێژەیا کومسیۆنێ', 'نەخێر، رازی مە ژ ڕەوشا نوکە']);
  var kuS4 = form.addTextItem().setTitle('حەز دکەی دکان/پەیجێ تە ئێک ژ فرۆشگەهێن دەستپێکێ بیت؟ (ناڤێ دکانێ و ژمارا واتسئەپی بنڤیسە)');

  // --- ARABIC FLOW ---
  var secArRole = form.addPageBreakItem().setTitle('تحديد الدور (العربية)');
  var arRole = form.addMultipleChoiceItem().setTitle('أستخدم وسائل التواصل الاجتماعي بشكل أساسي من أجل:').setRequired(true);

  var secArBuyer = form.addPageBreakItem().setTitle('Cheapify — استطلاع المشترين (العربية)');
  var arB1 = form.addMultipleChoiceItem().setTitle('كم مرة تتسوق عبر الإنترنت من فيسبوك، إنستغرام أو التطبيقات المحلية؟')
      .setChoiceValues(['أسبوعياً', 'عدة مرات في الشهر', 'نادراً', 'أبداً']);
  var arB2 = form.addMultipleChoiceItem().setTitle('عند البحث عن منتج معين، هل تلاحظ فارقاً كبيراً في الأسعار لنفس المنتج تماماً بين الصفحات؟')
      .setChoiceValues(['نعم، دائماً وبفارق كبير', 'أحياناً', 'نادراً / لم ألاحظ', 'لا، الأسعار متقاربة']);
  var arB3 = form.addCheckboxItem().setTitle('ما أكثر ما يزعجك أثناء التسوق محلياً عبر الإنترنت؟ (اختر أهم ٢)')
      .setChoiceValues([
        'إرسال رسائل خاصة لمجرد معرفة السعر والانتظار لساعات',
        'العثور على نفس المنتج بسعر أرخص فور الشراء',
        'الصفحات غير الموثوقة والمنتجات المكررة',
        'تأخر التوصيل والطلب اليدوي غير المنظم'
      ]);
  var arB4 = form.addMultipleChoiceItem().setTitle('إذا كان هناك تطبيق يجمع نفس المنتج مع أسعار جميع المتاجر المحلية جنباً إلى جنب لاختيار أرخص سعر، هل ستستخدمه؟')
      .setChoiceValues(['نعم بالتأكيد — أحتاجه الآن', 'غالباً نعم', 'ربما، يعتمد على سرعة التوصيل', 'لا، أفضل المراسلة المباشرة']);
  var arB5 = form.addTextItem().setTitle('هل تود تجربة النسخة الأولى التجريبية؟ (ضع رقم الواتساب أو حساب الإنستغرام)');

  var secArSeller = form.addPageBreakItem().setTitle('Cheapify — استطلاع التجار وأصحاب المتاجر (العربية)');
  var arS1 = form.addCheckboxItem().setTitle('أين تبيع منتجاتك حالياً؟')
      .setChoiceValues(['صفحات إنستغرام / فيسبوك', 'تيك توك', 'محل فعلي فقط', 'تطبيقات ومتاجر إلكترونية أخرى']);
  var arS2 = form.addCheckboxItem().setTitle('ما هو أكبر تحدٍ يواجهك في البيع عبر الإنترنت؟ (اختر أهم ٢)')
      .setChoiceValues([
        'الرد لساعات على رسائل "بكم السعر؟" لزبائن غير جادين',
        'المنافسة العشوائية وتضارب الأسعار',
        'التكلفة العالية لبرمجة موقع أو تطبيق خاص',
        'تنظيم العناوين وشركات التوصيل يدوياً عبر الواتساب'
      ]);
  var arS3 = form.addMultipleChoiceItem().setTitle('إذا توفرت منصة تعرض منتجاتك بدون رسوم تقنية مسبقة وتشعرك بالأسعار المنافسة لتحقيق مبيعات، هل ستنضم للتجربة؟')
      .setChoiceValues(['نعم، مهتم جداً', 'ربما، حسب نسبة العمولة', 'لا، مكتفٍ بنظام البيع الحالي']);
  var arS4 = form.addTextItem().setTitle('هل ترغب بأن يكون متجرك ضمن المتاجر الأولى في الإطلاق التجريبي؟ (اسم المتجر ورقم الواتساب)');

  // Logic jumps based on language selection
  langItem.setChoices([
    langItem.createChoice('English', secEnRole),
    langItem.createChoice('کوردی (Badînî)', secKuRole),
    langItem.createChoice('العربية', secArRole)
  ]);

  // English jumps
  enRole.setChoices([
    enRole.createChoice('Shop & buy products', secEnBuyer),
    enRole.createChoice('Sell products / Manage a shop', secEnSeller)
  ]);

  // Kurdish jumps
  kuRole.setChoices([
    kuRole.createChoice('کڕینا کەلوپەلان (کڕیار)', secKuBuyer),
    kuRole.createChoice('فرۆتنا کەلوپەلان / خودان جهـ (فرۆشیار)', secKuSeller)
  ]);

  // Arabic jumps
  arRole.setChoices([
    arRole.createChoice('تسوق وشراء المنتجات (مشتري)', secArBuyer),
    arRole.createChoice('بيع المنتجات وإدارة متجر (تاجر / بائع)', secArSeller)
  ]);
  
  // Set endings
  secEnBuyer.setGoToPage(FormApp.PageNavigationType.SUBMIT);
  secEnSeller.setGoToPage(FormApp.PageNavigationType.SUBMIT);
  secKuBuyer.setGoToPage(FormApp.PageNavigationType.SUBMIT);
  secKuSeller.setGoToPage(FormApp.PageNavigationType.SUBMIT);
  secArBuyer.setGoToPage(FormApp.PageNavigationType.SUBMIT);
  secArSeller.setGoToPage(FormApp.PageNavigationType.SUBMIT);
}
```

---

### Step 2: Essential Form Settings
Before sharing your form link across social media or WhatsApp:
1. Open the form in edit mode and go to **Settings**.
2. Under **Responses**, verify that **"Restrict to users in [Domain]"** and **"Limit to 1 response" (which forces Google Sign-in)** are both toggled **OFF**. 
3. Turn off sign-in requirements so users can open and complete the survey seamlessly inside Instagram, Facebook, and WhatsApp in-app browsers without login screens causing drop-offs.