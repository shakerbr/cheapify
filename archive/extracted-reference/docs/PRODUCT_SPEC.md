# Cheapify — Product Specification & Master Vision

**Version:** 1.0 (Archived Reference)  
**Founder:** Shakir Bashar  
**Market:** Iraq / Kurdistan Region (KRI — Duhok, Erbil, Sulaymaniyah, Baghdad)  
**Core Slogan:** *The bright side of choosing.*  
**Tagline:** *Smart Deals. Verified Sellers. One App.*  

---

## 1. Executive Summary & Problem Space

In the Iraqi retail and e-commerce ecosystem, shopping online is highly fragmented, disorganized, and opaque:
1. **Cross-Platform & Intra-App Price Disparity:** The exact same branded product sells at wildly conflicting prices across different platforms (e.g., Miswag, Simma, Elryan) and even inside multi-seller platforms like iBazzar.
   - *Documented Evidence:* ASUS 24" 100Hz Gaming Monitor ranged from **116,721 IQD** to **163,350 IQD** (~47,000 IQD difference for the identical model).
   - *Duplicate Clutter:* On iBazzar, identical Xiaomi 165W power banks were listed by competing vendors at **60,000 IQD** vs **70,000 IQD** without unified product grouping.
2. **The "How Much?" / "B chande?" Friction:** Over 80% of local digital transactions occur via Instagram, Facebook, and TikTok DMs where prices are concealed, forcing consumers into tedious chat threads and hours of waiting for quotes.
3. **Trust & Verification Void:** Online buyers hesitate due to counterfeit fears, non-transparent return policies, and unverified accounts.
4. **Merchant Bottlenecks:** Physical retail owners and boutique page sellers want digital reach but cannot afford custom software development ($5,000+) or high platform commission fees (10–15%+).

### The Solution: Cheapify
Cheapify is an intelligent multi-seller marketplace that organizes fragmented local retail into a single, transparent, and structured catalog. By enforcing a strict **Single-SKU layout**, Cheapify displays every verified seller offering an identical item side by side, automatically prioritizing the best-value deal while giving merchants real-time pricing intelligence alerts.

---

## 2. Core Stakeholders & Personas

### 2.1 The Consumer Persona: "The Smart Deal-Seeker"
* **Representative Persona:** Ahmad, 23 years old.
* **Profile:** Final-year university student (Business Administration) & part-time office assistant living in Duhok.
* **Shopping Behavior:** Mobile-first user active on Instagram, TikTok, and WhatsApp. Buys tech gadgets, mobile accessories, study tools, and lifestyle items.
* **Payment Preference:** Cash on Delivery (COD) as primary trust builder, along with local digital wallets (FastPay, FIB, Qi Card).
* **Pain Points:** 
  - Frustrated by arbitrary 5,000–25,000 IQD markups across different Instagram pages.
  - Hates asking "Price?" in DMs and waiting hours for replies.
  - Fears overpaying or receiving counterfeit goods.
* **Emotional Value:** Cheapify makes him feel **smart, relieved, and empowered** knowing he secured the verifiable best market deal.

### 2.2 The Merchant Persona: "The Local Retailer / Boutique Seller"
* **Profile:** Physical store owners in commercial bazaars/malls and active social commerce page owners.
* **Pain Points:**
  - Spends hours replying to repetitive, non-serious "Price?" inquiries.
  - Has no automated tool to monitor competitor market rates.
  - Squeezed by heavy commissions on legacy delivery/marketplace apps.
* **Value Received:**
  - Turn-key digital storefront with zero upfront development fees.
  - Automatic pricing alerts when competing stores drop prices.
  - Structured order fulfillment and courier integration.
  - Fair, tiered fee structure that preserves profit margins.

---

## 3. Core Product Mechanics & Architectural Innovations

### 3.1 The Single-SKU Architecture (No Duplicate Listings)
Unlike legacy marketplaces that let every seller create an independent product card (resulting in 20 duplicate listings for one iPhone model), Cheapify enforces **one master product listing per unique SKU/barcode**:
* **Catalog Standardization:** Standardized hero image, specs, and descriptions.
* **Merchant Comparison Table:** Beneath the master product card, every verified seller listing this SKU is presented side by side with:
  - Seller Store Name & Verified Checkmark
  - Selling Price in IQD
  - Stock Availability
  - Estimated Delivery Time
  - Direct Action Button ("Buy Now" / "Select Seller")

### 3.2 The Best-Price & Value Ranking Engine
The platform automatically highlights the optimal offer using a transparent algorithm:
* **The "Best Value" Badge:** Displayed in solid Jade Green (`#148C53`) on the winning seller card.
* **Ranking Factors:**
  1. Lowest verified price in IQD
  2. Merchant verification status & fulfillment rating
  3. Delivery speed / availability in the customer's region

### 3.3 Live Merchant Pricing Intelligence Alerts
* When a competing merchant lists an identical SKU at a lower price, the system dispatches an automated notification (via WhatsApp / Merchant Dashboard) to outpriced sellers:
  > *"Notice: Another verified seller updated [Product Name] to 62,000 IQD (your price: 65,000 IQD). Adjust your price to win the Best Value position."*

### 3.4 Localized Iraqi Checkout & Fulfillment Handshake
* **Payments:**
  - Cash on Delivery (COD) — essential default for regional trust.
  - FastPay API integration.
  - First Iraqi Bank (FIB) payment gateway.
  - Qi Card integration.
* **Logistics (Asset-Light 3PL Model):**
  - Direct API / Webhook dispatch to local couriers (e.g., ZMC Express, local courier partners in Duhok/Erbil/Baghdad).
  - Automated waybill generation with customer phone and address.
  - Real-time order tracking and status updates.

### 3.5 Automated WhatsApp Order Routing & Verification
* For rapid MVP adoption, orders trigger an instant automated WhatsApp message to both the buyer and merchant:
  - Buyer receives instant order confirmation with SKU, total IQD, and courier ETA.
  - Merchant receives 1-click order fulfillment confirmation.
  - Post-delivery 1-click rating ping: *"Did you receive the correct item at the agreed price?"*

---

## 4. Monetization & Business Model

Cheapify rejects the predatory 10%–15% commission model that scares away local retailers. Instead, it utilizes an accessible **Tiered Pricing Structure**:

| Item Price Range (IQD) | Platform Fee Model | Example Fee |
| :--- | :--- | :--- |
| **< 9,000 IQD** | **5%** variable fee | 350 IQD on a 7,000 IQD item |
| **10,000 – 99,000 IQD** | **Flat 1,000 IQD** | 1,000 IQD on a 45,000 IQD item |
| **100,000 – 499,000 IQD** | **2%** variable fee | 3,000 IQD on a 150,000 IQD item |
| **≥ 500,000 IQD** | **1.5%** capped fee | Fair scaling for high-ticket items |

### Future Expansion Revenue Streams
1. **Featured Seller Placement:** Sponsored "Store Spotlight" banners on high-traffic category pages (without distorting fair price sorting on product pages).
2. **Merchant Intelligence Suite:** Advanced inventory turnover and regional price-elasticity analytics subscriptions.
3. **Courier Partner Integration Rebates:** Modest volume-based dispatch commissions from integrated 3PL logistics partners.

---

## 5. MVP Product Boundaries & Rollout Phasing

### MVP Phase (Current Scope)
* **Standardized SKUs Only:** Initial inventory restricted to items with standard manufacturer barcodes and serial numbers (Consumer Electronics, Mobile Accessories, Personal Audio, Packaged Goods). Unbarcoded clothing or unstandardized fashion is excluded from the MVP.
* **Pilot Geography:** Duhok & Erbil metropolitan hubs.
* **Pilot Merchants:** 5 to 10 verified local stores.
* **Core Deliverable:** Web Catalog MVP with single-SKU side-by-side pricing, WhatsApp order routing, and Cash on Delivery / local wallet checkout.

### Phase 2: Native App & Expansion
* Native iOS & Android applications.
* Automated 3PL courier API dispatch dashboard.
* Dynamic seller dashboard with live price editing and automated inventory syncing.
