> From: https://gemini.google.com/app/3f82514a94735a8e

# you asked

message time: 2026-09-22 13:37:23

Marketing Part. 
Now we create the content strategy

---

# gemini response

This comprehensive content strategy for Cheapify is built upon the foundational marketing exercises and pitch materials developed during the GIZ Entrep. Program. 

## Brand Foundation & Voice
*   **Brand Name & Slogan:** Cheapify — "The bright side of choosing".
*   **Core Offer:** Find the lowest price from verified local sellers in seconds, compare options side by side, and order securely with local delivery.
*   **Brand Voice:** Transparent, Smart, and Reliable. Content must list prices upfront immediately, avoid "dirt cheap" slang, never imply low quality, and eliminate friction by never using phrases like "DM for price".
*   **Visual Identity:** The brand colors are Boston Blue, Azure Blue, and Jade Green. Visual assets should consistently utilize the primary logo lockup: a modern blue shopping bag (representing the Market Hub) featuring an upward green arrow (Growth) and a green magnifying glass (Discovery).

## Target Audience Profiles
*   **Everyday Deal-Seekers:** Young adults (ages 18–35) across major KRI and Iraqi cities who are looking for transparent, fair prices without the hassle of DM negotiations or arbitrary price disparities across different apps.
*   **Local Retail Merchants:** Small to medium physical stores and social-media retailers who need a scalable digital storefront without the expense and maintenance of building custom e-commerce apps.

## Content Pillars
| Pillar | Strategic Focus | Content Execution |
| :--- | :--- | :--- |
| **1. Transparent Value** | Side-by-Side Price Comparisons & "Deal of the Day" spotlights. | Visually showcase real price savings directly in the feed, emphasizing the platform's algorithmic best-value ranking and zero hidden fees. |
| **2. Reliability & Trust** | Local Verified Seller Spotlights. | Build buyer confidence by highlighting participating shops, detailing the strict merchant vetting process, and showcasing secure local payment and courier integration. |
| **3. Smart Discovery** | Smart Shopping Tips & Customer Savings Proof. | Demonstrate how buyers save time and money using the platform's single-SKU master product pages, which eliminate messy duplicate listings and simplify the shopping experience. |

## Strategic Campaign Goals
The immediate objective of executing this content strategy is to successfully launch Cheapify's social media pages. This content foundation will drive traffic to test a simple Web Catalog MVP alongside 5–10 pilot sellers. By maintaining clear, specific messaging across all initial posts and ads, the strategy is designed to generate the first test orders via WhatsApp by Week 6.

---

# you asked

message time: 2026-09-22 13:40:48

Now create a 1 month content plan for me. You can use html to make a nice calendar, printable to PDF. 
After than, we well transform the plan to reality, for each item of the content plan, we will make AI generate the prompts, then make another AI generate content(images or videos)

---

# gemini response

I will now design a complete 1-month content calendar for Cheapify as a styled, printable HTML file. 

This calendar will map out a 4-week launch plan focusing on your three core pillars (Transparent Value, Reliability & Trust, and Smart Discovery) to drive traffic to your Web Catalog MVP and secure those first WhatsApp orders. I will include a "Print to PDF" button directly in the document so you can easily export it.

Cheapify 1-Month Content Calendar

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cheapify - 1 Month Content Calendar</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --boston-blue: #3B90CE;
            --azure-blue: #007FFF;
            --jade-green: #00A36C;
            --cloud-bg: #F6F8FA;
            --text-main: #333333;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--cloud-bg);
            color: var(--text-main);
            margin: 0;
            padding: 40px 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 3px solid var(--cloud-bg);
            padding-bottom: 20px;
            margin-bottom: 30px;
        }

        .brand-title {
            margin: 0;
            color: var(--text-main);
            font-size: 28px;
        }

        .brand-subtitle {
            color: var(--boston-blue);
            font-weight: 600;
            margin-top: 5px;
        }

        .controls button {
            background-color: var(--jade-green);
            color: white;
            border: none;
            padding: 10px 20px;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .controls button:hover {
            background-color: #008f5e;
        }

        .legend {
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
            font-size: 14px;
            font-weight: 600;
        }

        .badge {
            padding: 4px 10px;
            border-radius: 20px;
            color: white;
            font-size: 12px;
        }

        .bg-pillar1 { background-color: var(--azure-blue); } /* Transparent Value */
        .bg-pillar2 { background-color: var(--jade-green); } /* Reliability */
        .bg-pillar3 { background-color: var(--boston-blue); } /* Smart Discovery */

        .calendar-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 10px;
        }

        .day-header {
            text-align: center;
            font-weight: 700;
            padding: 10px;
            background-color: var(--cloud-bg);
            border-radius: 6px;
        }

        .day-cell {
            min-height: 120px;
            border: 2px solid var(--cloud-bg);
            border-radius: 8px;
            padding: 10px;
            display: flex;
            flex-direction: column;
            background: white;
        }

        .day-number {
            font-weight: 700;
            color: #999;
            margin-bottom: 8px;
            font-size: 14px;
        }

        .post-content {
            font-size: 12px;
            line-height: 1.4;
            margin-top: 8px;
        }

        .post-title {
            font-weight: 700;
            margin-bottom: 4px;
        }

        .empty-day {
            background-color: #fcfcfc;
        }

        /* Print Styles */
        @media print {
            body {
                background: white;
                padding: 0;
            }
            .container {
                box-shadow: none;
                padding: 0;
            }
            .controls {
                display: none;
            }
            .day-cell {
                min-height: 100px;
                break-inside: avoid;
            }
            /* Force background colors to print */
            * {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="header">
            <div>
                <h1 class="brand-title">Cheapify Content Plan</h1>
                <div class="brand-subtitle">Month 1: MVP Launch & Web Catalog Testing</div>
            </div>
            <div class="controls">
                <button onclick="window.print()">Print to PDF</button>
            </div>
        </div>

        <div class="legend">
            <div><span class="badge bg-pillar1">Pillar 1</span> Transparent Value</div>
            <div><span class="badge bg-pillar2">Pillar 2</span> Reliability & Trust</div>
            <div><span class="badge bg-pillar3">Pillar 3</span> Smart Discovery</div>
        </div>

        <div class="calendar-grid">
            <!-- Headers -->
            <div class="day-header">Monday</div>
            <div class="day-header">Tuesday</div>
            <div class="day-header">Wednesday</div>
            <div class="day-header">Thursday</div>
            <div class="day-header">Friday</div>
            <div class="day-header">Saturday</div>
            <div class="day-header">Sunday</div>

            <!-- WEEK 1 -->
            <div class="day-cell">
                <div class="day-number">Day 1</div>
                <span class="badge bg-pillar1">Pillar 1</span>
                <div class="post-content">
                    <div class="post-title">Launch Teaser</div>
                    The end of "DM for Price" is here. Introducing Cheapify: The bright side of choosing. Link in bio to browse the catalog.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 2</div></div>
            <div class="day-cell">
                <div class="day-number">Day 3</div>
                <span class="badge bg-pillar2">Pillar 2</span>
                <div class="post-content">
                    <div class="post-title">Merchant Spotlight</div>
                    Meet [Pilot Shop Name], one of our first verified local sellers. Quality guaranteed, prices upfront.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 4</div></div>
            <div class="day-cell">
                <div class="day-number">Day 5</div>
                <span class="badge bg-pillar3">Pillar 3</span>
                <div class="post-content">
                    <div class="post-title">Feature Ed: Single SKU</div>
                    Tired of duplicate listings? See how our smart app groups identical items so you instantly see the best deal.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 6</div></div>
            <div class="day-cell empty-day"><div class="day-number">Day 7</div></div>

            <!-- WEEK 2 -->
            <div class="day-cell">
                <div class="day-number">Day 8</div>
                <span class="badge bg-pillar1">Pillar 1</span>
                <div class="post-content">
                    <div class="post-title">Side-by-Side Savings</div>
                    Airpods Pro comparison. See the exact IQD savings when you choose the top-ranked seller on our Web Catalog.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 9</div></div>
            <div class="day-cell">
                <div class="day-number">Day 10</div>
                <span class="badge bg-pillar2">Pillar 2</span>
                <div class="post-content">
                    <div class="post-title">Behind the Shield</div>
                    How we vet our sellers. Only trusted merchants make it to the Cheapify catalog. No scams, just verified shops.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 11</div></div>
            <div class="day-cell">
                <div class="day-number">Day 12</div>
                <span class="badge bg-pillar3">Pillar 3</span>
                <div class="post-content">
                    <div class="post-title">Order via WhatsApp</div>
                    Found a deal? Ordering is easy. Click, confirm via WhatsApp, and get it delivered locally. Zero friction.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 13</div></div>
            <div class="day-cell empty-day"><div class="day-number">Day 14</div></div>

            <!-- WEEK 3 -->
            <div class="day-cell">
                <div class="day-number">Day 15</div>
                <span class="badge bg-pillar1">Pillar 1</span>
                <div class="post-content">
                    <div class="post-title">Deal of the Day</div>
                    Today's smartest choice: [Product Name]. Ranked #1 for value by our algorithm. Check the catalog link!
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 16</div></div>
            <div class="day-cell">
                <div class="day-number">Day 17</div>
                <span class="badge bg-pillar2">Pillar 2</span>
                <div class="post-content">
                    <div class="post-title">Local Delivery Partner</div>
                    We integrate with the best couriers in Duhok/KRI. Your item goes from a verified seller to your door securely.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 18</div></div>
            <div class="day-cell">
                <div class="day-number">Day 19</div>
                <span class="badge bg-pillar3">Pillar 3</span>
                <div class="post-content">
                    <div class="post-title">Customer Proof</div>
                    "Saved 15,000 IQD in 2 minutes." Real test orders are rolling in! Be the next smart shopper.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 20</div></div>
            <div class="day-cell empty-day"><div class="day-number">Day 21</div></div>

            <!-- WEEK 4 -->
            <div class="day-cell">
                <div class="day-number">Day 22</div>
                <span class="badge bg-pillar1">Pillar 1</span>
                <div class="post-content">
                    <div class="post-title">Tech/Fashion Compare</div>
                    Why pay more? Visual graphic showing an overpriced listing elsewhere vs. the Cheapify fair price.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 23</div></div>
            <div class="day-cell">
                <div class="day-number">Day 24</div>
                <span class="badge bg-pillar2">Pillar 2</span>
                <div class="post-content">
                    <div class="post-title">Merchant Call-Out</div>
                    Are you a local shop owner? Stop paying huge app fees. Join Cheapify's Web Catalog today. Flat & low rates.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 25</div></div>
            <div class="day-cell">
                <div class="day-number">Day 26</div>
                <span class="badge bg-pillar3">Pillar 3</span>
                <div class="post-content">
                    <div class="post-title">Monthly Wrap-Up</div>
                    The bright side of choosing is here to stay. Browse the top 5 deals of the month on our Web Catalog right now.
                </div>
            </div>
            <div class="day-cell empty-day"><div class="day-number">Day 27</div></div>
            <div class="day-cell empty-day"><div class="day-number">Day 28</div></div>
            
        </div>
    </div>

</body>
</html>
```

I have built the 30-day calendar matching your brand colors and strategic pillars. It targets 3 high-quality posts per week to keep the workload manageable while steadily driving traffic to your WhatsApp ordering system and Web Catalog MVP. 

To export it to PDF, you can just click the "Print to PDF" button at the top right of the file!

Whenever you are ready, let me know, and we can move on to the next step: generating the AI prompts for the copy and visuals for these specific calendar items!

---

# you asked

message time: 2026-09-22 14:03:50

Perfect. now let's create the first post

---

# gemini response

### Post Overview
* **Day & Pillar:** Day 1 — Pillar 1: Transparent Value
* **Theme:** Launch Teaser ("The End of 'DM for Price'")
* **Format:** Single High-Impact Image / Reel Cover (1080×1080 px for feed or 1080×1920 px for Stories/Reels)
* **Objective:** Introduce Cheapify, call out the frustration of hidden prices on social media, and direct initial traffic to the Web Catalog link.

---

### Copy & Caption

#### Caption (Primary / English)
> The end of "DM for price" is here. 🚫💬
>
> We have all spent hours asking for prices across different pages, only to find the same item listed with random markups. 
>
> Meet **Cheapify** — the bright side of choosing.
>
> Compare identical products from verified local sellers side by side, view real upfront prices instantly, and order directly to your door. No games. No hidden fees. No friction.
>
> 🔗 Tap the link in our bio to browse the launch catalog today!
>
> ---
> #Cheapify #SmartShopping #Duhok #Kurdistan #IraqShopping #TransparentPricing #ShopSmart

#### Localized Kurdish (Badini / Sorani option for Duhok & KRI)
> دووماهیا دەمێ "بۆ بهایی وەرە تایبەت (DM)" هات. 🚫💬
> 
> ئێدی چ پێدڤی ناکەت ب دەمژمێران ل دویڤ بهایێن دروست بگەڕی. ب ڕێکا **Cheapify** دشێی ب ساناهیترین شێوە بهایێن فرۆشیارێن باوەڕپێکری یێن باژێرێ خۆ هەڤبەر بکەی و ب بهایەکێ شەفاف و ئاشکرا داخواز بکەی.
>
> 🔗 لینکا کەتەلۆگێ د بایۆی دا ببینە!

---

### AI Generation Prompts

#### 1. Image Generation Prompt (Midjourney v6 / Ideogram / Flux)
Use this prompt in tools like Midjourney, Flux.1, or Ideogram (Ideogram is especially recommended if rendering exact text):

```text
A sleek, modern 3D brand reveal graphic on an ultra-clean studio background with soft studio lighting, subtle soft shadows, base color #F6F8FA Cloud white. In the center, a translucent frosted-glass smartphone floating upright displaying a minimalist e-commerce comparison card with clear numbers and a verified green checkmark badge. Behind the phone, an elegant stylized 3D shopping bag outline in bold Boston Blue and Azure Blue accents, featuring a crisp Jade Green upward arrow and a magnifying glass element integrated seamlessly. In the background, muted floating chat bubbles with closed lock icons and grey text "DM for price?" dissolving into thin air, contrasted by vibrant, sharp green price tags appearing with clear IQD currency labels. Ultra-clean UI elements, premium tech aesthetic, Apple-like design minimalism, Octane Render style, 8k resolution, no clutter, aspect ratio 1:1 --ar 1:1 --stylize 250
```

* **Negative Prompt (for Stable Diffusion / Leonardo):**
  `messy, blurry, low resolution, dirty, neon oversaturation, chaotic background, illegible distorted text, dark moody grunge, poor lighting, extra limbs`

---

#### 2. Short-Form Video Prompt (Runway Gen-3 Alpha / Kling / Luma Dream Machine)
If animating this teaser for Instagram Reels or TikTok:

```text
Cinematic smooth dolly-in shot of a floating modern smartphone against a minimalist studio background in light cool grey #F6F8FA. The screen lights up in vibrant Boston Blue and Jade Green, revealing an e-commerce price tag with numbers snapping into focus. Several translucent dark speech bubbles with question marks and "DM for price" fade out into soft smoke around the phone. As they disappear, an upward Jade Green glowing arrow smoothly animates through a crisp blue shopping bag silhouette. Sleek 3D motion graphics, 60fps, clean tech product commercial style, ultra-smooth motion.
```

---

### On-Graphic Text Overlay (Canva / Photoshop Specs)
If editing the generated graphic before publishing:
* **Headline Font:** Inter 800 / Plus Jakarta Sans Bold
* **Headline Copy:** *The End of "DM for Price"*
* **Sub-headline / Tagline:** *Introducing Cheapify: The bright side of choosing.*
* **Brand Assets:** Place the Cheapify primary bag/arrow/magnifier logo lockup centered at the top or bottom margin.

---

# you asked

message time: 2026-09-22 14:06:43

![Cheapify.png](images/image-001.png)

![Cheapify-2.png](images/image-002.png)

![Cheapify-2-2.png](images/image-003.png)

![Cheapify-white-bg.png](images/image-004.png)

Okay, generate it for me

---

# gemini response

I can create more images as soon as your limit resets. Check your usage in Settings.

---

# you asked

message time: 2026-09-22 16:10:05

Next post

---

# gemini response

### Post Overview
* **Day & Pillar:** Day 3 — Pillar 2: Reliability & Trust
* **Theme:** Merchant Spotlight
* **Format:** Single Image / Carousel Slide (1080×1080 px)
* **Objective:** Introduce one of your initial verified local pilot sellers to build buyer trust, showcase quality, and emphasize transparent pricing.

---

### Copy & Caption

#### Caption (Primary / English)
> Meet one of our first verified local sellers on Cheapify: **[Pilot Shop Name]**! 🛍️✨
>
> We believe that great shopping starts with trusted local businesses. That is why every merchant on our platform goes through a strict vetting process—so you never have to guess who is behind the screen.
>
> Quality guaranteed. Prices listed upfront. No hidden surprises.
>
> Support local, shop smart, and explore their latest arrivals on our Web Catalog today!
>
> 🔗 Tap the link in our bio to browse.
>
> ---
> #Cheapify #MerchantSpotlight #ShopLocal #Duhok #Kurdistan #VerifiedSellers #SmartShopping

#### Localized Kurdish (Badini / Sorani option for Duhok & KRI)
> ئێک ژ فرۆشیارێن مە یێن باوەڕپێکری ل سەر پلاتفۆرمێ Cheapify ناس بکە: **[ناڤێ فرۆشیاری]**! 🛍️✨
>
> مە باوەری هەیە کو کڕینا دروست ژ کێبڕکە و کارگەهـ و دوکانێن خۆمالی یێن باوەڕپێکری دەست پێ دکەت. ژبەر وێ چەندێ، هەمی فرۆشیار ل دەڤ مە د ڕێکارێن پشکداریا توند ڕا دەرباز دبن.
>
> کوالیتیا مسۆگەر، بها ل پێش ئاشکرا. لینکا کەتەلۆگێ د بایۆی دا ببینە!

---

### AI Generation Prompts

#### 1. Image Generation Prompt (Midjourney v6 / Ideogram / Flux)
```text
A professional lifestyle portrait of a friendly young local shop owner in Duhok smiling inside a bright, modern boutique retail store filled with neatly organized tech accessories and trendy lifestyle goods. Soft natural lighting, warm and welcoming atmosphere. In the foreground, a sleek smartphone is held up displaying the Cheapify web catalog interface featuring the verified green checkmark badge and clear IQD prices. Color palette features Boston Blue #0E82C4 and Jade Green #148C53 accents on signage or UI elements. High-end commercial photography style, shallow depth of field, sharp focus, 8k resolution, aspect ratio 1:1 --ar 1:1 --stylize 200
```

* **Negative Prompt (for Stable Diffusion / Leonardo):**
  `blurry, dark, gloomy, messy store, low quality, distorted hands, bad anatomy, harsh flash lighting, watermark`

---

### On-Graphic Text Overlay (Canva / Photoshop Specs)
* **Headline Font:** Plus Jakarta Sans Bold
* **Headline Copy:** *Verified Seller Spotlight*
* **Sub-headline:** *Trusted local shops. Upfront prices. Zero hidden fees.*
* **Badge Element:** Add a green verified badge graphic overlay next to the shop name placeholder.

---

Would you like to move forward to **Day 5 (Pillar 3: Single SKU Feature)** next?

---

# you asked

message time: 2026-09-24 15:14:30

Prompts for a carousel post (maybe 3rd post, or any other)

---

# gemini response

Here is a complete, ready-to-use carousel post prompt package for **Day 5 (Pillar 3: Smart Discovery / Single SKU Feature)** from your content plan. 

This 4-slide carousel layout is designed to break down your core competitive advantage: how Cheapify eliminates messy, duplicate listings by grouping identical products under a single master page.

---

### Carousel Structure (4 Slides Breakdown)

* **Slide 1 (The Hook):** Tired of scrolling through 10 different pages for the exact same item?
* **Slide 2 (The Problem):** Messy duplicate listings, random markups, and endless scrolling.
* **Slide 3 (The Solution / The Single-SKU Rule):** One master product page. Multiple verified sellers competing transparently.
* **Slide 4 (Call to Action):** Instantly see the best deal. Tap the link in our bio to browse.

---

### Copy & Caption

#### Caption (Primary / English)
> Tired of duplicate listings? 🛑📱
>
> When you are looking for a product online, scrolling through dozens of messy pages just to find a price is exhausting. 
>
> With **Cheapify**, our smart app automatically groups identical items together under a single master product page. That means you instantly see side-by-side pricing from verified local sellers, ranked by the best deal.
>
> No clutter. No guessing. Just the best price in seconds.
>
> 🔗 Tap the link in our bio to check out our smart catalog today!
>
> ---
> #Cheapify #SmartShopping #SingleSKU #PriceComparison #Duhok #Kurdistan #ShopSmart

---

### AI Generation Prompts (For Carousel Visuals)

Use these prompts in tools like Midjourney, Flux, or Ideogram to create your multi-slide visuals.

#### Slide 1 Prompt (The Hook / Problem)
```text
A clean social media carousel slide design, square 1:1 aspect ratio, modern tech startup style. Background color #F6F8FA Cloud white. In the center, a 3D graphic showing a chaotic stack of messy, overlapping smartphone screens displaying random duplicate e-commerce listings with different confusing prices. Dark grey moody UI elements, subtle warning icons. Clean typography layout space at the top, professional and sleek, 8k resolution --ar 1:1
```

#### Slide 2 Prompt (The Solution / Single-SKU Feature)
```text
A clean social media carousel slide design, square 1:1 aspect ratio, modern tech startup style. Background color #F6F8FA Cloud white. In the center, a sleek 3D smartphone floating upright displaying a single organized product page ("Single-SKU Master Page") with three clean, transparent price rows from verified local sellers side-by-side, highlighted with Boston Blue #0E82C4 and Jade Green #148C53 accents and a green checkmark badge. Clean minimalist aesthetic, professional product design, 8k resolution --ar 1:1
```

---

### On-Graphic Text Overlay Guide (Canva / Photoshop)
* **Font Family:** Inter or Plus Jakarta Sans (Bold for headers, Regular for body text)
* **Slide 1 Text:** *Tired of duplicate listings & messy scrolling?*
* **Slide 2 Text:** *The Single-SKU Rule: One master page. Multiple verified sellers.*
* **Slide 3 Text:** *Instantly compare prices & find the best deal automatically.*
* **Slide 4 Text:** *Browse the smart catalog today. Link in bio!*

---

Would you like to generate the content package for the next milestone, or focus on a specific post from your calendar?

---

# you asked

message time: 2026-09-24 16:16:05

Give me the arabic caption

---

# gemini response

Here is the Arabic caption for the launch teaser post (Day 1) based on your brand guidelines:

> انتهى عصر عبارة "أرسل رسالة لتتضح السعر" (DM) إلى الأبد 🚫💬
> 
> لقد أمضينا جميعا ساعات طويلة في السؤال عن الأسعار عبر صفحات مختلفة، لنكتشف في النهاية أن نفس المنتج يباع بفوارق عشوائية.
> 
> تعرفوا على **Cheapify** — الوجهة الأذكى للتسوق.
> 
> قارنوا الأسعار لنفس المنتجات من بائعين محليين موثوقين جنباً إلى جنب، واطلعوا على الأسعار الشفافة فوراً، واطلبوا مباشرة حتى باب منزلكم. بلا تعقيد، وبدون رسوم خفية.
> 
> 🔗 اضغط على الرابط في البايو لتصفح كتالوج الإطلاق اليوم!
> 
> ---
> #Cheapify #تسوق_بذكاء #العراق #كوردستان #أسعار_شفافة #تسوق_محلي

---

# you asked

message time: 2026-09-24 16:20:20

Give it to mee in the three languages
English | Arabic | Kurdish(badini)
As one caption for one post

---

# gemini response

Here is the Day 1 launch teaser caption formatted in all three languages for a single post:

***

### English
The end of "DM for price" is here. 🚫💬

We have all spent hours asking for prices across different pages, only to find the same item listed with random markups. 

Meet **Cheapify** — the bright side of choosing.

Compare identical products from verified local sellers side by side, view real upfront prices instantly, and order directly to your door. No games. No hidden fees. No friction.

🔗 Tap the link in our bio to browse the launch catalog today!

---

### Arabic
انتهى عصر عبارة "أرسل رسالة لتتضح السعر" (DM) إلى الأبد 🚫💬

لقد أمضينا جميعاً ساعات طويلة في السؤال عن الأسعار عبر صفحات مختلفة، لنكتشف في النهاية أن نفس المنتج يباع بفوارق عشوائية.

تعرفوا على **Cheapify** — الوجهة الأذكى للتسوق.

قارنوا الأسعار لنفس المنتجات من بائعين محليين موثوقين جنباً إلى جنب، واطلعوا على الأسعار الشفافة فوراً، واطلبوا مباشرة حتى باب منزلكم. بلا تعقيد، وبدون رسوم خفية.

🔗 اضغط على الرابط في البايو لتصفح كتالوج الإطلاق اليوم!

---

### Kurdish (Badini)
دووماهیا دەمێ "بۆ بهایی وەرە تایبەت (DM)" هات. 🚫💬

ئێدی چ پێدڤی ناکەت ب دەمژمێران ل دویڤ بهایێن دروست بگەڕی. ب ڕێکا **Cheapify** دشێی ب ساناهیترین شێوە بهایێن فرۆشیارێن باوەڕپێکری یێن باژێرێ خۆ هەڤبەر بکەی و ب بهایەکێ شەفاف و ئاشکرا داخواز بکەی.

🔗 لینکا کەتەلۆگێ د بایۆی دا ببینە!

---
#Cheapify #SmartShopping #Duhok #Kurdistan #IraqShopping #TransparentPricing #ShopSmart

---

# you asked

message time: 2026-09-27 16:00:50

fill this table with our plan:
8 Monthly Content Plan (posts + captions)
Plan a month of content. Write the post idea, a draft caption, and the platform for each.
#
Day / date
Post idea
Caption (draft)
Platform
1




2




3




4




5




6




7




8




9




10




11




12

---

# gemini response

Here is your complete 1-month content plan table populated with the exact post ideas, draft captions, and recommended platforms based on your strategy and calendar sources:

| # | Day / date | Post idea | Caption (draft) | Platform |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Day 1 | Launch Teaser | The end of "DM for Price" is here. Introducing Cheapify: The bright side of choosing. Link in bio to browse the catalog. | Instagram / TikTok |
| **2** | Day 3 | Merchant Spotlight | Meet [Pilot Shop Name], one of our first verified local sellers. Quality guaranteed, prices upfront. | Instagram / Facebook |
| **3** | Day 5 | Feature Ed: Single SKU | Tired of duplicate listings? See how our smart app groups identical items so you instantly see the best deal. | Instagram Carousel / TikTok |
| **4** | Day 8 | Side-by-Side Savings | Airpods Pro comparison. See the exact IQD savings when you choose the top-ranked seller on our Web Catalog. | Instagram / Facebook |
| **5** | Day 10 | Behind the Shield | How we vet our sellers. Only trusted merchants make it to the Cheapify catalog. No scams, just verified shops. | Instagram / TikTok |
| **6** | Day 12 | Order via WhatsApp | Found a deal? Ordering is easy. Click, confirm via WhatsApp, and get it delivered locally. Zero friction. | Instagram / Facebook |
| **7** | Day 15 | Deal of the Day | Today's smartest choice: [Product Name]. Ranked #1 for value by our algorithm. Check the catalog link! | Instagram Stories / Feed |
| **8** | Day 17 | Local Delivery Partner | We integrate with the best couriers in Duhok/KRI. Your item goes from a verified seller to your door securely. | Instagram / Facebook |
| **9** | Day 19 | Customer Proof | "Saved 15,000 IQD in 2 minutes." Real test orders are rolling in! Be the next smart shopper. | Instagram / TikTok |
| **10** | Day 22 | Tech/Fashion Compare | Why pay more? Visual graphic showing an overpriced listing elsewhere vs. the Cheapify fair price. | Instagram / Facebook |
| **11** | Day 24 | Merchant Call-Out | Are you a local shop owner? Stop paying huge app fees. Join Cheapify's Web Catalog today. Flat & low rates. | Instagram / Facebook |
| **12** | Day 26 | Monthly Wrap-Up | The bright side of choosing is here to stay. Browse the top 5 deals of the month on our Web Catalog right now. | Instagram / TikTok |

---

Would you like to start generating the AI copy and visual prompts for any specific day from this table?