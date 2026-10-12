# Cheapify — Operations, Budget & Go-To-Market Playbook

**Version:** 1.0 (Operations Blueprint - Archived Reference)  
**Target:** 6-Month Pilot Launch in Duhok / Iraqi Kurdistan  

---

## 1. Core Business Processes (Standard Operating Procedures)

### 1.1 Process 1: Merchant & Product Onboarding
This workflow ensures zero duplicate clutter, strictly standardized single-SKU listings, and vetted merchant credentials.

```
[Merchant Application] ──► [KYC & Verification] ──► [Barcode / SKU Match]
                                                           │
                                ┌──────────────────────────┴──────────────────────────┐
                                ▼                                                     ▼
                       [Existing SKU in DB]                                  [New Master Product]
                                │                                                     │
                   Attach Merchant's Stock & Price                       Create Clean Catalog Entry & Specs
                                │                                                     │
                                └──────────────────────────┬──────────────────────────┘
                                                           ▼
                                            [Price & Alert Engine Setup]
                                                           │
                                                           ▼
                                          [Storefront & Listings Activated]
```

* **Inputs:**
  - Store identity (Trade name, physical location, owner ID, phone & WhatsApp number).
  - Product inventory data: manufacturer barcode/SKU, product specifications, real photo, stock count, price in IQD.
* **Execution Steps:**
  1. **Verification:** Inspect physical shop presence or social media store history.
  2. **Catalog Matching:** Scan barcode against central database.
  3. **Listing Assignment:** If item exists, attach merchant stock and price to the shared product card. If new, ingest hero specs and assign master SKU.
  4. **Pricing Engine Setup:** Configure automated competitive alerts.
  5. **Activation:** Deliver branded starter kit (Acrylic QR counter stand and "Cheapify Verified Partner" window sticker) and publish store profile.
* **Quality Check Protocols:**
  - Verify photo clarity and neutral white backdrop standards.
  - Reject placeholder prices (e.g., 0 IQD or 999,999 IQD).
  - Prevent duplicate SKU creation.

---

### 1.2 Process 2: Order Processing & Delivery Fulfillment
An asset-light 3PL integration linking local merchants directly to courier networks.

```
[Order Placed on Cheapify]
          │
          ▼
[Instant WhatsApp Alert to Merchant]
          │
          ▼
[Merchant Confirms Stock & Packs]
          │
          ▼
[Automated 3PL Courier Dispatch & Waybill]
          │
          ▼
[Courier Pick-up from Store]
          │
          ▼
[Transit & Delivery to Customer Doorstep]
          │
          ▼
[Cash / Digital Settlement Collected]
          │
          ▼
[Automated 1-Click Post-Delivery Quality Ping]
```

* **Inputs:** Customer order details (Product SKU, delivery address, selected payment method: COD, FastPay, FIB, or Qi Card).
* **Execution Steps:**
  1. **Order Dispatch Alert:** Real-time push alert & WhatsApp trigger dispatched to the merchant.
  2. **Merchant Confirmation:** Seller confirms item readiness within 30 minutes.
  3. **Courier Automated Booking:** Platform issues dispatch payload to 3PL logistics partner (e.g., ZMC Express / local courier).
  4. **Pickup & Transit:** Courier collects parcel from store and transports to customer address.
  5. **Payment Collection & Settlement:** Courier collects COD funds, confirms drop-off via app. Platform deducts tiered platform fee and queues merchant payout.
* **Quality Check Protocols:**
  - Automated WhatsApp feedback check to buyer: *"Did you receive the correct item in good condition at the agreed price?"*
  - Monitor delivery SLA (guaranteeing same-day or 24h intra-city delivery).
  - Update merchant fulfillment reliability score.

---

## 2. Financial Model & 6-Month Pilot Budget

Because platform development is engineered in-house by the founder, **100% of seed capital is directed into operational infrastructure, merchant acquisition, and local customer adoption rather than development agency salaries**.

### 2.1 Itemized Pilot Launch Budget ($3,000 USD)

| Category | Deliverables & Scope | Budget (USD) | Share (%) |
| :--- | :--- | :--- | :--- |
| **Domain & Cloud Hosting Setup** | `.com` domain registration, high-availability cloud VPS (12 mos), SSL certificates, and managed database clustering. | $180 | 6.0% |
| **WhatsApp Business API & Comms** | Official Meta Cloud API setup, phone verification, 5,000 automated conversation bundles, and webhook routing. | $170 | 5.7% |
| **Payment Gateway Integration** | FastPay, FIB, and Qi Card merchant account clearance, API sandbox tests, and payout logic security audit. | $450 | 15.0% |
| **Merchant Onboarding & Collateral** | 10 acrylic QR counter stands, 10 window badges, and printed merchant agreements for initial 5–10 pilot shops. | $250 | 8.3% |
| **Digital Marketing & Acquisition** | 4-week hyper-local Meta/TikTok ads in Duhok/KRI, micro-influencer product tests, and first-order delivery subsidies. | $650 | 21.7% |
| **Content Creation & SKU Photography**| Studio lightbox kit, 50 standardized hero SKU photo shoots, and social launch assets. | $300 | 10.0% |
| **Delivery Testing & Logistics** | 20 end-to-end pilot deliveries with 3PL couriers in Duhok to validate packaging and SLAs. | $200 | 6.7% |
| **Legal & Administrative Registration** | Trade name filing with Chamber of Commerce, municipal compliance, and legal terms review. | $300 | 10.0% |
| **Operational Contingency Buffer** | Liquidity float for ad traffic surges, payment chargeback tests, and unexpected operational expenses. | $500 | 16.7% |
| **Total Pilot Launch Budget** | **Complete Runway for 6-Month Validated Pilot** | **$3,000** | **100.0%** |

### 2.2 Post-Launch Monthly Operating Run-Rate ($90 / month)
* Cloud hosting & database maintenance: **$35 / mo**
* WhatsApp Business messaging volume: **$25 / mo**
* Targeted local digital promotion: **$30 / mo**
* **Total Monthly Burn:** **$90 / mo**

---

## 3. Market Validation Survey Framework

Validated via Google Forms across 3 languages (English, Kurdish Badini, Arabic) with branching logic separating buyers and sellers.

### Automated Google Apps Script Setup
Deployable directly via [script.google.com](https://script.google.com) to instantly generate the live multi-lingual survey in Google Drive:
```javascript
function createCheapifySurvey() {
  var form = FormApp.create('Cheapify Market Validation Survey | راپرسی | استطلاع');
  form.setDescription('Market research on e-commerce pricing & disorganization in Iraq.');

  var langItem = form.addMultipleChoiceItem()
    .setTitle('Choose your language / زمانێ خۆ هەلبژێرە / اختر لغتك')
    .setRequired(true);

  // English Flow
  var secEnRole = form.addPageBreakItem().setTitle('Role Selection (English)');
  var enRole = form.addMultipleChoiceItem().setTitle('I mainly use social media/apps to:').setRequired(true);
  var secEnBuyer = form.addPageBreakItem().setTitle('Cheapify — Buyer Survey');
  var enB1 = form.addMultipleChoiceItem().setTitle('How often do you shop online from Facebook, Instagram, or local apps?')
      .setChoiceValues(['Weekly', 'A few times a month', 'Rarely', 'Never']);
  var enB2 = form.addMultipleChoiceItem().setTitle('Do you notice big price differences for the exact same item across pages?')
      .setChoiceValues(['Yes, constantly (large gaps)', 'Sometimes', 'Rarely / Never', 'No, prices are similar']);
  var enB3 = form.addCheckboxItem().setTitle('What annoys you the most when shopping online locally?')
      .setChoiceValues([
        'Sending DMs just to ask "Price?" / Waiting hours for replies',
        'Finding the exact same item cheaper after buying it',
        'Duplicate listings and messy feeds',
        'Lack of trust in unverified sellers',
        'Delivery delays and manual ordering'
      ]);
  var enB4 = form.addMultipleChoiceItem().setTitle('If an app showed you the exact product with every local seller price side-by-side to get the best deal, would you use it?')
      .setChoiceValues(['Definitely yes', 'Probably yes', 'Maybe, depends on delivery/speed', 'No, I prefer direct DMs']);
  var enB5 = form.addTextItem().setTitle('Would you like early beta access? (Leave WhatsApp or IG handle)');

  // Kurdish (Badini) Flow
  var secKuRole = form.addPageBreakItem().setTitle('دیارکرنا ڕۆلی (کوردی)');
  var kuRole = form.addMultipleChoiceItem().setTitle('ئەز ب شێوەیەکێ سەرەکی سۆشیال میدیایێ بکار دئینم بۆ:').setRequired(true);
  var secKuBuyer = form.addPageBreakItem().setTitle('Cheapify — راپرسییا کڕیاران (کوردی)');
  var kuB1 = form.addMultipleChoiceItem().setTitle('چەند جار ئەنلاین یاخوود ژ پەیجێن فەیسبووک و ئینستاگرامی تشتان دکڕی?')
      .setChoiceValues(['حەفتییانە', 'مەهانە چەند جاران', 'دەگمەن', 'چ جاران']);
  var kuB2 = form.addMultipleChoiceItem().setTitle('دەمێ ل بەرهەمەکی دگەڕی، ئایا جیاوازییا بهایان د ناڤبەرا پەیجان دا بۆ هەمان کەلوپەل دبینى?')
      .setChoiceValues(['بەڵێ، بەردەوام (جیاوازییا مەزن یا هەی)', 'هندەک جاران', 'کێم جار', 'نەخێر، بهایێن وان نێزیکی ئێکن']);
  var kuB3 = form.addCheckboxItem().setTitle('چ تشت زێدەتر تە بێزار دکەت دەمێ ب ئۆنلاین تشتان دکڕی؟')
      .setChoiceValues([
        'هنارتنا نامەیان بتنێ بۆ پرسیارکرنا "ب چەندە؟"',
        'دیتنا هەمان کەلوپەل ب ئەرزانتر ئێکسەر پشتی تە کڕی',
        'پۆستێن دووبارە و نەبوونا باوەریێ ب پەیجێن نەدیار',
        'درەنگ گەهشتنا بەرهەمی و ئالۆزییا گەیاندنێ'
      ]);
  var kuB4 = form.addMultipleChoiceItem().setTitle('ئەگەر ئەپڵیکەیشنەک هەبیت کو ئێکسەر هەمی فرۆشیاران ب بهایێن وان ڤە بدانیتە تەنیشت ئێك دا ب هەرزانترین نرخ بکڕی، دێ بکارئینی?')
      .setChoiceValues(['بێگومان بەڵێ', 'ڕەنگە بەڵێ', 'بەندە ل سەر لەزاتی و گەیاندنێ', 'نەخێر']);

  // Arabic Flow
  var secArRole = form.addPageBreakItem().setTitle('تحديد الدور (العربية)');
  var arRole = form.addMultipleChoiceItem().setTitle('أستخدم وسائل التواصل الاجتماعي بشكل أساسي من أجل:').setRequired(true);
  var secArBuyer = form.addPageBreakItem().setTitle('Cheapify — استطلاع المشترين');
  var arB1 = form.addMultipleChoiceItem().setTitle('كم مرة تتسوق عبر الإنترنت من فيسبوك أو إنستغرام أو التطبيقات المحلية؟')
      .setChoiceValues(['أسبوعياً', 'عدة مرات في الشهر', 'نادراً', 'أبداً']);
  var arB2 = form.addMultipleChoiceItem().setTitle('عند البحث عن منتج معين، هل تلاحظ فارقاً كبيراً في الأسعار لنفس المنتج تماماً؟')
      .setChoiceValues(['نعم، دائماً وبفارق كبير', 'أحياناً', 'نادراً / لم ألاحظ', 'لا، الأسعار متقاربة']);
  var arB3 = form.addCheckboxItem().setTitle('ما أكثر ما يزعجك أثناء التسوق محلياً عبر الإنترنت؟')
      .setChoiceValues([
        'إرسال رسائل خاصة لمجرد معرفة السعر والانتظار لساعات',
        'العثور على نفس المنتج بسعر أرخص فور الشراء',
        'الصفحات غير الموثوقة والمنتجات المكررة',
        'تأخر التوصيل والطلب اليدوي غير المنظم'
      ]);
  var arB4 = form.addMultipleChoiceItem().setTitle('إذا توفر تطبيق يعرض المنتج مع أسعار جميع المتاجر المحلية جنباً إلى جنب لاختيار أرخص سعر، هل ستستخدمه؟')
      .setChoiceValues(['نعم بالتأكيد — أحتاجه الآن', 'غالباً نعم', 'ربما، يعتمد على التوصيل', 'لا، أفضل المراسلة المباشرة']);

  // Navigation connections
  langItem.setChoices([
    langItem.createChoice('English', secEnRole),
    langItem.createChoice('کوردی (Badînî)', secKuRole),
    langItem.createChoice('العربية', secArRole)
  ]);
  enRole.setChoices([enRole.createChoice('Shop & buy products', secEnBuyer)]);
  kuRole.setChoices([kuRole.createChoice('کڕینا کەلوپەلان (کڕیار)', secKuBuyer)]);
  arRole.setChoices([arRole.createChoice('تسوق وشراء المنتجات (مشتري)', secArBuyer)]);

  secEnBuyer.setGoToPage(FormApp.PageNavigationType.SUBMIT);
  secKuBuyer.setGoToPage(FormApp.PageNavigationType.SUBMIT);
  secArBuyer.setGoToPage(FormApp.PageNavigationType.SUBMIT);
}
```

---

## 4. Go-To-Market & 30-Day Content Execution

### 4.1 Content Pillars
1. **Pillar 1: Transparent Value (40%):** Concrete price comparisons of identical products across different sellers to visually illustrate real IQD savings.
2. **Pillar 2: Reliability & Trust (30%):** Spotlights on local verified shops, vetting transparency, and courier safety.
3. **Pillar 3: Smart Discovery (30%):** Feature education on the Single-SKU catalog, elimination of duplicate listings, and 1-click WhatsApp order confirmation.

### 4.2 Core Social Launch Copy (Trilingual)
* **Launch Teaser Hook:** *The end of "DM for price" is here.*
  - **English:** "Stop scrolling through endless pages asking 'Price?'. Cheapify brings verified local stores under one single catalog so you instantly see who has the best deal."
  - **Kurdish (Badini):** "دووماهیا دەمێ 'بۆ بهایی وەرە تایبەت (DM)' هات. ب ڕێکا Cheapify دشێی ب ساناهیترین شێوە بهایێن فرۆشیارێن باوەڕپێکری یێن باژێرێ خۆ هەڤبەر بکەی و ب بهایەکێ شەفاف و ئاشکرا داخواز بکەی."
  - **Arabic:** "انتهى عصر عبارة 'أرسل رسالة لتعرف السعر' (DM) إلى الأبد. قارنوا الأسعار لنفس المنتجات من بائعين محليين موثوقين جنباً إلى جنب، واطلبوا مباشرة حتى باب منزلكم."
