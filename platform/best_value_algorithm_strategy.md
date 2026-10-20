# Cheapify Platform Architecture — Hybrid "Best Value" Algorithm Strategy

## Balancing Total Landed Doorstep Price, Proximity Advantage, and Merchant Transparency

---

## 1. Executive Summary & Strategic Rationale

On traditional Iraqi and regional e-commerce marketplaces, buyers and sellers are plagued by two opposing failure modes in product pricing:

1. **The "Bait-and-Switch" Sticker Price Trap (Pure Sticker Price Model):** Platforms rank offers solely by the product's headline price. A distant seller in another city lists an item for 25,000 IQD with a hidden 5,000 IQD shipping fee, beating a local bazaar merchant listing the same item for 26,000 IQD with a 3,000 IQD local courier fee. The buyer only discovers at final checkout that the distant seller actually costs **30,000 IQD total** versus the local seller's **29,000 IQD total**, resulting in checkout abandonment, delivery delays (2–3 days vs 2 hours), and buyer frustration.
2. **The "Black Box" Distance Penalty (Opaque Landed Cost Model):** Platforms hide delivery calculations behind an opaque proprietary algorithm. Local merchants see their offers de-ranked without understanding why, breeding distrust, accusations of platform favoritism, and merchant churn.

### The Solution: The Hybrid "Best Value" Model

Cheapify implements a **Hybrid "Total Landed Cost + Proximity Advantage" Model** built on four unyielding principles:

1. **Total Landed Doorstep Affordability ($P_{\text{total}}$):** The winning offer must genuinely save the consumer money at the door when the delivery driver hands over the parcel. No surprise courier tariffs at checkout.
2. **Natural Proximity Advantage for Local Merchants:** Intra-city delivery (e.g., within Duhok) carries a flat, standardized 3PL courier rate (3,000 IQD). Because shipping is identical across local sellers, **Total Landed Cost ranking is 100% equivalent to sticker price ranking**. Local bazaar merchants compete directly and fairly on retail price, while out-of-city merchants must offer deep, authentic discounts to overcome higher inter-city shipping tariffs.
3. **Radical Dual Transparency:**
   - **For Shoppers:** The product page and checkout explicitly break down: `Item Price + Delivery Tariff = Total Doorstep Price`. The winning offer receives the signature highlighted **"Best Value"** badge.
   - **For Merchants:** The Merchant Dashboard provides a clear, real-time diagnostic panel ("Why Didn't I Win?") showing the exact price and delivery differential, offering actionable pricing guidance in plain Badînî Kurdish and Arabic.
4. **Deterministic & Non-Pay-to-Play:** Cheapify does not sell sponsored product placements, ad boosts, or algorithmic favoritism. Offers are evaluated on a strict, mathematically deterministic 3-tier hierarchy.

---

## 2. The 3-Tier Multi-Attribute Priority Hierarchy

When multiple verified merchants list offers under the exact same Single-SKU product page, Cheapify's ranking engine evaluates and sorts all active offers using a strict sequential priority cascade:

```text
[ Incoming SKU Offers for Buyer Location ]
                   │
                   ▼
       ┌────────────────────────┐
       │ Priority 0: Total Cost │
       │ P_total = Item + Ship  │
       └────────────────────────┘
                   │
       Is there a clear winner?
      ┌────────────┴────────────┐
     YES                        NO (Tied Total Cost)
      │                         │
      ▼                         ▼
[ Award Best Value ] ┌────────────────────────┐
                     │ Priority 1: Delivery   │
                     │ Proximity / Speed Tier │
                     └────────────────────────┘
                                │
                    Is there a clear winner?
                   ┌────────────┴────────────┐
                  YES                        NO (Same Speed Zone)
                   │                         │
                   ▼                         ▼
             [ Award Best Value ] ┌────────────────────────┐
                                  │ Priority 2: Quality    │
                                  │ Verified Rating & Perf │
                                  └────────────────────────┘
                                             │
                                             ▼
                                    [ Award Best Value ]
```

### Priority 0: Lowest Total Landed Doorstep Price ($P_{\text{total}}$) — *Primary / Hard Cut*

The absolute primary ranking attribute is the **Total Landed Price** delivered to the buyer's doorstep:

$$P_{\text{total}} = P_{\text{item}} + D_{\text{tariff}}(\text{origin}, \text{destination})$$

Where:

- $P_{\text{item}}$ is the merchant's active listed price in Iraqi Dinar (IQD) for the verified SKU.
- $D_{\text{tariff}}$ is the standardized, system-calculated third-party courier tariff between the merchant's physical fulfillment hub (shop/warehouse) and the buyer's delivery district.

Intra-City Dynamics (e.g. Duhok to Duhok):
When the buyer and merchants are located in the same metropolitan zone, the delivery tariff is identical ($D_{\text{tariff}} = 3,000\text{ IQD}$). Therefore:

$$P_{\text{total}, A} - P_{\text{total}, B} = (P_{\text{item}, A} + 3,000) - (P_{\text{item}, B} + 3,000) = P_{\text{item}, A} - P_{\text{item}, B}$$

In intra-city trade, the delivery variable completely cancels out. **Local merchants compete 100% on their retail sticker price**, preserving full bazaar competition simplicity.

Inter-City Dynamics (e.g. Erbil Merchant vs. Duhok Merchant delivering to a Duhok Buyer):

- Duhok Merchant: $D_{\text{tariff}} = 3,000\text{ IQD}$.
- Erbil Merchant: $D_{\text{tariff}} = 5,000\text{ IQD}$.
- Shipping Differential: $\Delta D = +2,000\text{ IQD}$.

To win the "Best Value" badge for a Duhok buyer, the Erbil merchant must offer a product discount strictly greater than 2,000 IQD:

$$P_{\text{item}, \text{Erbil}} < P_{\text{item}, \text{Duhok}} - 2,000\text{ IQD}$$

This creates an inherent, organic economic defense for local neighborhood merchants: out-of-city sellers cannot undercut a local bazaar shop by 500 or 1,000 IQD if doing so forces the buyer to pay more total money for delivery.

---

### Priority 1: Delivery Speed by Geographic Distance — *Secondary / First Tie-Breaker*

If two or more merchants offer the **exact same Total Landed Price** ($P_{\text{total}, A} = P_{\text{total}, B}$), the ranking engine breaks the tie in favor of the **fastest fulfillment time** based on physical proximity:

$$\text{Speed Rank: } \text{Zone 1 (Hyperlocal 1–3h)} > \text{Zone 2 (Intra-City 3–6h)} > \text{Zone 3 (Inter-City 24–48h)} > \text{Zone 4 (Nationwide 48–72h)}$$

**Rationale:** When two offers cost the customer the exact same total sum at the door, the customer universally prefers receiving the item in 2 hours rather than waiting 2 days. This strongly incentivizes merchants located closest to the buyer.

---

### Priority 2: Verified Merchant Quality & Reliability Score — *Tertiary / Final Tie-Breaker*

If multiple merchants offer the exact same Total Landed Price AND belong to the same delivery speed zone, the tie is broken by **Merchant Quality & Operational Reliability**:

$$Q_{\text{merchant}} = w_1 \cdot R_{\text{rating}} + w_2 \cdot F_{\text{fulfillment}} + w_3 \cdot (1 - D_{\text{defect}})$$

Where:

- $R_{\text{rating}}$: Verified buyer customer review rating (normalized 0.0 to 1.0, minimum threshold of 5 completed orders to qualify).
- $F_{\text{fulfillment}}$: Order acceptance and dispatch rate (percentage of orders successfully fulfilled without merchant-side cancellation).
- $D_{\text{defect}}$: Return/defect rate due to wrong item, damaged packaging, or customer dispute.
- Default weights: $w_1 = 0.50$, $w_2 = 0.35$, $w_3 = 0.15$.

---

## 3. Delivery Logistics Distance & Tariff Matrix

To eliminate shipping fraud and hidden fees, **merchants never set custom delivery fees**. Delivery tariffs are fixed, standardized contract rates negotiated directly by Cheapify with local 3PL courier partners (e.g. Fast Delivery in Duhok and certified local courier fleets; ZMC Express for inter-city).

The platform maintains a deterministic distance and zone routing matrix:

| Delivery Zone | Geographic Scope | Typical 3PL Partner | Estimated Delivery Window | Standard Courier Tariff (IQD) | Primary Coverage Area |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Zone 1: Hyperlocal** | Same city core (within 5 km radius) | Local on-demand motorbike couriers | **1 – 3 Hours** | **3,000 IQD** | Duhok City Center, Malta, Bazar, Shakhke |
| **Zone 2: Intra-City Metropolitan** | Greater metropolitan area (5 – 25 km) | Scheduled van / courier fleet | **3 – 6 Hours** (Same-Day) | **3,000 – 3,500 IQD** | Duhok Suburbs, Semel, Masike, Zakho Corridor |
| **Zone 3: Regional Inter-City** | Cross-governorate within KRI & Nineveh | Inter-city hub linehauls (ZMC Express) | **24 – 48 Hours** (Next-Day) | **5,000 IQD** | Erbil $\leftrightarrow$ Duhok, Mosul $\leftrightarrow$ Duhok, Sulaymaniyah |
| **Zone 4: Nationwide All-Iraq** | Central & Southern Iraq linehaul | National courier network | **48 – 72 Hours** (2–3 Days) | **6,000 – 7,000 IQD** | Baghdad, Basra, Najaf, Karbala, Kirkuk |

Note: In the Phase 1 Duhok pilot, 100% of orders are routed within Zone 1 and Zone 2, where courier tariffs are standardized at 3,000 IQD.

---

## 4. Concrete Real-World Commercial Scenarios

The following scenarios illustrate how the Hybrid Best-Value Algorithm performs across everyday bazaar situations in Kurdistan and Iraq:

### Scenario A: Pure Intra-City Bazaar Competition (Duhok to Duhok)

- **Product:** Anker 20W USB-C Fast Charger (Single-SKU)
- **Buyer Location:** Duhok Malta District
- **Merchant Offers:**
  - **Merchant 1 (Kawa Tech — Central Bazaar, Duhok):** Item: 14,000 IQD | Delivery: 3,000 IQD | Rating: 4.8★
  - **Merchant 2 (Sipan Mobile — KRO, Duhok):** Item: 15,500 IQD | Delivery: 3,000 IQD | Rating: 4.9★
  - **Merchant 3 (Avin Electronics — Bazar, Duhok):** Item: 16,000 IQD | Delivery: 3,000 IQD | Rating: 4.7★
- **Algorithm Computation:**
  - Merchant 1 Total: $14,000 + 3,000 = \mathbf{17,000\text{ IQD}}$
  - Merchant 2 Total: $15,500 + 3,000 = 18,500\text{ IQD}$
  - Merchant 3 Total: $16,000 + 3,000 = 19,000\text{ IQD}$
- **Outcome:** **Merchant 1 (Kawa Tech) wins the "Best Value" badge** at Priority 0.
- **Key Takeaway:** Because delivery is identical (3,000 IQD), ranking is 100% identical to sticker price. Local merchants compete on fair, open retail margins.

---

### Scenario B: Local Bazaar Merchant vs. Out-of-City Wholesaler (Proximity Advantage in Action)

- **Product:** Xiaomi 20,000mAh Power Bank (Single-SKU)
- **Buyer Location:** Duhok University Campus (AUK)
- **Merchant Offers:**
  - **Merchant A (Duhok Bazaar Shop):** Item: 28,000 IQD | Delivery: 3,000 IQD (Zone 1, 2 hours) | Rating: 4.8★
  - **Merchant B (Erbil Wholesale Vendor):** Item: 27,000 IQD | Delivery: 5,000 IQD (Zone 3, 24–48 hours) | Rating: 4.9★
- **Algorithm Computation:**
  - Merchant A (Duhok Local): $28,000 + 3,000 = \mathbf{31,000\text{ IQD Total Doorstep}}$
  - Merchant B (Erbil Wholesaler): $27,000 + 5,000 = \mathbf{32,000\text{ IQD Total Doorstep}}$
- **Outcome:** **Merchant A (Duhok Local) wins the "Best Value" badge**, despite having a sticker price 1,000 IQD higher than the Erbil seller!
- **Key Takeaway:** The algorithm protects the local Duhok shop. Even though the Erbil vendor attempted to undercut on sticker price, their higher inter-city shipping would have forced the buyer to pay 1,000 IQD more total cash. Cheapify ensures the buyer gets the best real deal ($31,000 < $32,000) and gets it in 2 hours instead of 2 days.

---

### Scenario C: Legitimate Deep Out-of-City Discount (Consumer Savings Protected)

- **Product:** Samsung 24-inch IPS Monitor (Single-SKU)
- **Buyer Location:** Duhok
- **Merchant Offers:**
  - **Merchant A (Duhok Retail Shop):** Item: 155,000 IQD | Delivery: 3,000 IQD | Rating: 4.9★
  - **Merchant B (Erbil Importer / Direct Distributor):** Item: 135,000 IQD | Delivery: 5,000 IQD | Rating: 4.8★
- **Algorithm Computation:**
  - Merchant A (Duhok): $155,000 + 3,000 = 158,000\text{ IQD}$
  - Merchant B (Erbil): $135,000 + 5,000 = \mathbf{140,000\text{ IQD}}$
- **Outcome:** **Merchant B (Erbil) wins the "Best Value" badge**.
- **Key Takeaway:** The Erbil importer's discount (20,000 IQD lower) overwhelmingly exceeds the 2,000 IQD shipping differential, delivering a **net 18,000 IQD savings** to the consumer. Cheapify will never artificially shield an uncompetitive local markup when an authentic, high-value alternative genuinely saves the family money.

---

### Scenario D: Price Tie Broken by Distance & Speed

- **Product:** Baseus 65W GaN Fast Charger (Single-SKU)
- **Buyer Location:** Duhok Malta District
- **Merchant Offers:**
  - **Merchant 1 (Duhok Central Bazaar, 2 km away):** Item: 32,000 IQD | Delivery: 3,000 IQD (Zone 1, 1–2 hours) | Rating: 4.7★
  - **Merchant 2 (Semel Suburb Shop, 18 km away):** Item: 31,500 IQD | Delivery: 3,500 IQD (Zone 2, 4–6 hours) | Rating: 4.9★
- **Algorithm Computation:**
  - Merchant 1 Total: $32,000 + 3,000 = \mathbf{35,000\text{ IQD}}$
  - Merchant 2 Total: $31,500 + 3,500 = \mathbf{35,000\text{ IQD}}$
  - *Priority 0 Result:* Exact Tie ($35,000\text{ IQD} == 35,000\text{ IQD}$).
  - *Priority 1 Evaluation:* Merchant 1 is in Zone 1 (1–2h delivery); Merchant 2 is in Zone 2 (4–6h delivery).
- **Outcome:** **Merchant 1 wins the "Best Value" badge** based on delivery proximity.
- **Key Takeaway:** When total money spent is identical, the buyer gets the faster delivery.

---

### Scenario E: Price & Proximity Tied Broken by Merchant Quality

- **Product:** Kingston 64GB USB 3.2 Flash Drive (Single-SKU)
- **Buyer Location:** Duhok Center
- **Merchant Offers:**
  - **Merchant A (Shop in Bazaar):** Item: 8,000 IQD | Delivery: 3,000 IQD | Total: 11,000 IQD | Speed: Zone 1 (2h) | Rating: 4.9★ (42 reviews, 99% fulfillment)
  - **Merchant B (Shop in Bazaar):** Item: 8,000 IQD | Delivery: 3,000 IQD | Total: 11,000 IQD | Speed: Zone 1 (2h) | Rating: 4.2★ (8 reviews, 88% fulfillment)
- **Algorithm Computation:**
  - *Priority 0:* Tied at 11,000 IQD.
  - *Priority 1:* Tied in Zone 1 (Hyperlocal 2h).
  - *Priority 2:* Merchant A score ($0.975$) beats Merchant B score ($0.812$).
- **Outcome:** **Merchant A wins the "Best Value" badge**.
- **Key Takeaway:** Trust and customer service break deadlocks, encouraging bazaar shopkeepers to maintain high standards and prompt order dispatch.

---

## 5. Dual-Sided Radical Transparency Architecture

### 5.1 Consumer UX & Product Page Representation

On the Single-SKU product view, the winning offer is featured prominently in the hero section:

- **Highlighted "Best Value" Chip:** Clearly displayed above the merchant name and price, indicating that this offer represents the lowest total doorstep cost.
- **Transparent Price Breakdown:**

  ```text
  ┌──────────────────────────────────────────────────────────┐
  │  ★ BEST VALUE                                            │
  │  28,000 IQD                                              │
  │  + 3,000 IQD local delivery  •  Total at Door: 31,000 IQD│
  │  Sold by: Kawa Tech (Duhok Bazaar) • 4.8 ★ (34 reviews)  │
  │  ⚡ Delivery: Within 2 hours (Hyperlocal Courier)         │
  │  [ ADD TO CART / BUY NOW ]                               │
  └──────────────────────────────────────────────────────────┘
  ```

- **"Other Verified Sellers" Comparison Drawer:** Below the primary buy box, an expandable list displays all alternative verified merchants selling the exact same barcode:

  ```text
  ┌──────────────────────────────────────────────────────────┐
  │ Other Verified Sellers for this Item (2)                 │
  ├──────────────────────────────────────────────────────────┤
  │ Sipan Mobile (KRO, Duhok) • 4.9 ★                        │
  │ 29,500 IQD (+ 3,000 IQD delivery = 32,500 IQD Total)     │
  │ ⚡ Delivery: Today (3–5 hours)                            │
  │ [ Choose This Seller ]                                   │
  ├──────────────────────────────────────────────────────────┤
  │ Erbil Wholesale Hub (Erbil) • 4.7 ★                      │
  │ 27,000 IQD (+ 5,000 IQD delivery = 32,000 IQD Total)     │
  │ 📦 Delivery: Tomorrow (24–48 hours)                      │
  │ [ Choose This Seller ]                                   │
  └──────────────────────────────────────────────────────────┘
  ```

- Buyers retain full autonomy: if a buyer prefers their cousin's shop or a seller with 4.9 stars for 1,000 IQD more, they can select any verified seller with one tap.

---

### 5.2 Merchant Dashboard & Commercial Communication

Traditional algorithms alienate local shopkeepers like Kak Kawa because they feel like opaque computer games. Cheapify translates algorithmic math into **actionable commercial intelligence** rendered in clear Kurdish (Badînî) and Arabic:

#### The "Competitive Position" Diagnostic Card (Merchant Portal Wireframe)

When Kak Kawa logs into his dashboard or opens his WhatsApp vendor summary:

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ SKU: Anker 20W USB-C Charger (White)                                    │
│ Your Current Price: 16,000 IQD                                          │
│ Your Status: 2nd of 3 Verified Sellers (Rank #2 in Duhok)               │
├─────────────────────────────────────────────────────────────────────────┤
│ 🔍 Why Didn't Your Offer Win the "Best Value" Badge?                    │
│                                                                         │
│ • Winning Offer (Kawa Tech):   14,000 IQD + 3,000 ship = 17,000 IQD     │
│ • Your Offer (Your Shop):      16,000 IQD + 3,000 ship = 19,000 IQD     │
│ • Price Gap: You are 2,000 IQD above the leading offer.                │
│                                                                         │
│ 💡 Actionable Recommendation:                                           │
│ Lower your price to 13,750 IQD to capture the #1 "Best Value" badge    │
│ and receive an estimated +25 orders this week.                          │
│                                                                         │
│ [ Match Lowest (13,750 IQD) ]    [ Keep Current Price ]                 │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Trilingual Explanations for Common Questions

1. **"Why did an Erbil shop lose even though their sticker price was 1,000 IQD cheaper than mine?"**
   - **Badînî Kurdish:** *«Firoşgeha Hewlêrê bihayê kelûpelî 1,000 D.Î kêmtir danabû, lê belê heqê gehandina wê 5,000 D.Î bû. Bihayê te yê gehandinê li Dihokê tenê 3,000 D.Î ye. Ji ber hindê, bihayê te yê dawî li ber dergehê muşterî erzantir bû!»*
   - **Arabic:** *«المتجر في أربيل عرض سعر السلعة أقل بـ 1,000 دينار، ولكن كلفة التوصيل من أربيل 5,000 دينار بينما كلفة توصيلك داخل دهوك 3,000 دينار فقط. لذلك كان سعرك الإجمالي عند باب الزبون أرخص وفزت بالعرض الأفضل!»*
2. **"Why did two shops with the same price get different ranks?"**
   - **Badînî Kurdish:** *«Herdu biha wekhev bûn, lê firoşgeha nêzîktir di navbera 1-2 seetan de digehe muşterî, lewma pêşengî wergirt.»*
   - **Arabic:** *«الأسعار كانت متطابقة تماماً، ولكن المتجر الأقرب يوصل الطلب خلال ساعة إلى ساعتين، لذلك حصل على الأولوية للسرعة.»*

---

## 6. Anti-Gaming, Governance & Edge Cases

To maintain platform trust and prevent deceptive commercial practices, the algorithm enforces strict governance guardrails:

### 6.1 Phantom Stock & Cancellation Penalties

- **Vulnerability:** A merchant lists an unrealistically low price to capture the "Best Value" badge and hoard order volume, then cancels orders or delays dispatch when stock is unavailable.
- **Enforcement:** If a merchant cancels an order due to "out of stock" after winning the badge, they incur an immediate **Reliability Score Deduction** ($F_{\text{fulfillment}} - 15\%$). If cancellation rate exceeds 5% in a rolling 14-day window, their store is temporarily disqualified from winning the Best Value badge for 7 days.

### 6.2 Strict Single-SKU Verification (No Sub-Tier Dilution)

- **Vulnerability:** A rogue seller lists a refurbished, open-box, or knock-off variant under a brand-new master SKU to show an artificially cheap price.
- **Enforcement:** Every seller offer mapped to a Single-SKU must match the exact barcode, manufacturer model number, and condition grade ("Brand New / Sealed"). Open-box or refurbished items are segregated into separate condition listings and cannot compete directly with brand-new retail SKUs.

### 6.3 Multi-Item Cart Shipping Consolidation

- **Mechanism:** When a buyer adds multiple items to their cart:
  - If multiple items are fulfilled by the **same merchant**, the buyer pays only **one** delivery tariff (3,000 IQD total).
  - If items are fulfilled by **different merchants**, each merchant requires an independent 3PL dispatch pickup, generating separate delivery tariffs clearly itemized at checkout.
  - The algorithm dynamically highlights: *"Buy both from Kawa Tech to save 3,000 IQD in combined shipping!"*

---

## 7. Production TypeScript Implementation Engine

The following pure, deterministic TypeScript module implements the complete Hybrid Best-Value Algorithm. It will be incorporated directly into the Cheapify MVP core routing service:

```typescript
/**
 * Cheapify Marketplace Engine
 * Hybrid "Best Value" Algorithm Specification
 * platform/best_value_algorithm_strategy.md
 */

export interface LocationCoordinates {
  latitude: number;
  longitude: number;
  city: 'Duhok' | 'Erbil' | 'Mosul' | 'Sulaymaniyah' | 'Baghdad' | 'Other';
  district: string;
}

export type DeliveryZoneTier = 'hyperlocal' | 'intra_city' | 'inter_city' | 'nationwide';

export interface DeliveryZoneRule {
  zone: DeliveryZoneTier;
  maxTransitHours: number;
  standardTariffIQD: number;
}

export interface MerchantOffer {
  offerId: string;
  merchantId: string;
  merchantName: string;
  skuBarcode: string;
  itemPriceIQD: number;
  stockAvailable: number;
  merchantLocation: LocationCoordinates;
  merchantRating: number;         // 1.0 to 5.0
  totalDeliveredOrders: number;   // Count of verified delivered orders
  fulfillmentSuccessRate: number; // 0.0 to 1.0 (acceptance without cancellation)
  defectRate: number;             // 0.0 to 1.0 (returns / damaged items)
  isActive: boolean;
}

export interface EvaluatedOffer extends MerchantOffer {
  deliveryZone: DeliveryZoneTier;
  deliveryTariffIQD: number;
  totalLandedPriceIQD: number;
  estimatedTransitHours: number;
  qualityScore: number;
  isBestValue: boolean;
  rank: number;
  priceDeltaVsBestValueIQD: number;
}

export interface BestValueEvaluationResult {
  skuBarcode: string;
  buyerCity: string;
  buyerDistrict: string;
  winningOffer: EvaluatedOffer | null;
  rankedOffers: EvaluatedOffer[];
  totalActiveSellers: number;
}

/**
 * Standard 3PL Logistics Tariff & Speed Matrix
 */
export function calculateDeliveryTariff(
  origin: LocationCoordinates,
  destination: LocationCoordinates
): DeliveryZoneRule {
  // Case 1: Same City & Same District / Neighborhood (Hyperlocal)
  if (origin.city === destination.city && origin.district === destination.district) {
    return {
      zone: 'hyperlocal',
      maxTransitHours: 3,
      standardTariffIQD: 3000,
    };
  }

  // Case 2: Same City (Intra-City Metropolitan)
  if (origin.city === destination.city) {
    return {
      zone: 'intra_city',
      maxTransitHours: 6,
      standardTariffIQD: 3000, // Standard 3PL city rate in Duhok pilot
    };
  }

  // Case 3: Regional Inter-City within KRI / Nineveh
  const isKriRegional =
    ['Duhok', 'Erbil', 'Mosul', 'Sulaymaniyah'].includes(origin.city) &&
    ['Duhok', 'Erbil', 'Mosul', 'Sulaymaniyah'].includes(destination.city);

  if (isKriRegional) {
    return {
      zone: 'inter_city',
      maxTransitHours: 48,
      standardTariffIQD: 5000,
    };
  }

  // Case 4: Nationwide All-Iraq
  return {
    zone: 'nationwide',
    maxTransitHours: 72,
    standardTariffIQD: 7000,
  };
}

/**
 * Calculates normalized merchant operational quality score
 */
export function calculateQualityScore(offer: MerchantOffer): number {
  if (offer.totalDeliveredOrders < 5) {
    // Default baseline score for new onboarded merchants
    return 0.70;
  }

  const normalizedRating = Math.min(Math.max((offer.merchantRating - 1) / 4, 0), 1);
  const fulfillmentScore = Math.min(Math.max(offer.fulfillmentSuccessRate, 0), 1);
  const defectScore = Math.max(1 - offer.defectRate, 0);

  // Weighted scoring: 50% rating, 35% fulfillment reliability, 15% low defect rate
  return (normalizedRating * 0.50) + (fulfillmentScore * 0.35) + (defectScore * 0.15);
}

/**
 * Delivery Zone Priority Rank (Lower is faster/closer)
 */
function getZonePriority(zone: DeliveryZoneTier): number {
  switch (zone) {
    case 'hyperlocal': return 1;
    case 'intra_city': return 2;
    case 'inter_city': return 3;
    case 'nationwide': return 4;
    default: return 99;
  }
}

/**
 * Core Deterministic Ranking Engine
 * Implements Priority 0 (Total Cost) -> Priority 1 (Proximity/Speed) -> Priority 2 (Quality)
 */
export function evaluateBestValueOffers(
  offers: MerchantOffer[],
  buyerLocation: LocationCoordinates
): BestValueEvaluationResult {
  // Filter active offers with verified inventory
  const eligibleOffers = offers.filter(o => o.isActive && o.stockAvailable > 0);

  if (eligibleOffers.length === 0) {
    return {
      skuBarcode: offers[0]?.skuBarcode || '',
      buyerCity: buyerLocation.city,
      buyerDistrict: buyerLocation.district,
      winningOffer: null,
      rankedOffers: [],
      totalActiveSellers: 0,
    };
  }

  // Map each offer with its distance delivery tariff and landed cost
  const evaluated: EvaluatedOffer[] = eligibleOffers.map(offer => {
    const delivery = calculateDeliveryTariff(offer.merchantLocation, buyerLocation);
    const totalLandedPriceIQD = offer.itemPriceIQD + delivery.standardTariffIQD;
    const qualityScore = calculateQualityScore(offer);

    return {
      ...offer,
      deliveryZone: delivery.zone,
      deliveryTariffIQD: delivery.standardTariffIQD,
      totalLandedPriceIQD,
      estimatedTransitHours: delivery.maxTransitHours,
      qualityScore,
      isBestValue: false,
      rank: 0,
      priceDeltaVsBestValueIQD: 0,
    };
  });

  // Strict 3-Tier Multi-Attribute Sorting
  evaluated.sort((a, b) => {
    // Priority 0: Lowest Total Landed Price (Hard cut)
    if (a.totalLandedPriceIQD !== b.totalLandedPriceIQD) {
      return a.totalLandedPriceIQD - b.totalLandedPriceIQD;
    }

    // Priority 1: Delivery Proximity / Speed Zone
    const zoneDiff = getZonePriority(a.deliveryZone) - getZonePriority(b.deliveryZone);
    if (zoneDiff !== 0) {
      return zoneDiff;
    }

    // Priority 2: Highest Merchant Quality Score
    if (b.qualityScore !== a.qualityScore) {
      return b.qualityScore - a.qualityScore;
    }

    // Deterministic fallback: earlier registration / ID sorting
    return a.merchantId.localeCompare(b.merchantId);
  });

  // Assign Best Value badge and rankings
  const winningOffer = evaluated[0];
  winningOffer.isBestValue = true;

  evaluated.forEach((offer, idx) => {
    offer.rank = idx + 1;
    offer.priceDeltaVsBestValueIQD = offer.totalLandedPriceIQD - winningOffer.totalLandedPriceIQD;
  });

  return {
    skuBarcode: winningOffer.skuBarcode,
    buyerCity: buyerLocation.city,
    buyerDistrict: buyerLocation.district,
    winningOffer,
    rankedOffers: evaluated,
    totalActiveSellers: evaluated.length,
  };
}
```

---

## 8. Summary of Strategic Advantages

| Venture Dimension | Naive Sticker-Price Model | Opaque Distance Model | Cheapify Hybrid Best-Value Model |
| :--- | :--- | :--- | :--- |
| **Consumer Protection** | ❌ Deceptive; surprise delivery costs at checkout | ⚠️ Confusing; cannot tell why one item is favored | ✅ **100% Doorstep Certainty; total price guaranteed** |
| **Local Merchant Defense** | ❌ Vulnerable to out-of-city dumping with high shipping | ❌ Local sellers penalized by black-box metrics | ✅ **Organic freight buffer protects local bazaar shops** |
| **Bazaar Simplicity** | ⚠️ Merchants try to compensate with fake low prices | ❌ Merchants frustrated by lack of transparency | ✅ **Identical local shipping allows pure sticker competition** |
| **Delivery Speed** | ❌ Slower (distant sellers favored if sticker is cheap) | ⚠️ Inconsistent delivery windows | ✅ **Hyperlocal & intra-city prioritized on equal pricing** |
| **Merchant Relations** | ❌ High merchant churn and disputes | ❌ Sellers suspect admin bias and hidden fees | ✅ **Full diagnostic transparency in Kurdish & Arabic** |

---

## 9. Governance & Cross-Pillar Roadmap

- **Pillar 1 (Entrepreneurship):** Harmonizes with the Single-SKU catalog architecture ([01_problem_solution_value.md](../entrepreneurship/01_problem_solution_value.md)) and Persona incentives ([03_customer_and_merchant_personas.md](../entrepreneurship/03_customer_and_merchant_personas.md)).
- **Pillar 2 (Marketing):** Provides the core commercial narrative for merchant onboarding ("Cheapify protects local Duhok shops from out-of-city dumping") and consumer acquisition campaigns ("Never pay a surprise shipping markup again").
- **Pillar 3 (Finance Management):** Directly drives unit economics by standardizing 3PL parcel tariffs (3,000 IQD) and anchoring COD weekly settlement calculations.
- **Pillar 4 (Business Modeling):** Forms the core defensible technology asset within the Value Proposition and Key Activities blocks of the Business Model Canvas.


---

## Appendix — Open Items Requiring Real-World Data

| Figure used in this doc | Source status | Needs |
| :--- | :--- | :--- |
| Default weights w1=0.50 / w2=0.35 / w3=0.15 | Design judgment | Validate against pilot conversion + complaint data |
| Min-5-orders rating threshold | Chosen cutoff | Recalibrate with real merchant order velocity |
| Proximity scoring buckets (1–3h / 3–6h / 24–48h) | Assumed courier performance bands | Real courier SLA data from pilot |
