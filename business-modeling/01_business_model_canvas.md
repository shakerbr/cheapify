# Cheapify — Business Model Canvas

**Category:** Pillar 4 — Business Modeling
**Status:** Working Standard — consolidated from Pillar 1–3 documents and platform specifications
**Date:** October 20, 2026

Cross-References:

- Value proposition detail: [`../entrepreneurship/06_value_proposition_and_founder_fit.md`](../entrepreneurship/06_value_proposition_and_founder_fit.md)
- Market sizing & personas: [`../entrepreneurship/02_market_opportunity_and_sizing.md`](../entrepreneurship/02_market_opportunity_and_sizing.md), [`../entrepreneurship/03_customer_and_merchant_personas.md`](../entrepreneurship/03_customer_and_merchant_personas.md)
- Fee architecture: [`../platform/fee_structure_and_monetization.md`](../platform/fee_structure_and_monetization.md)
- Order lifecycle policies: [`../platform/operational_policies.md`](../platform/operational_policies.md)
- Cost model: [`../finance/01_operational_budget.md`](../finance/01_operational_budget.md), [`../finance/03_cash_flow_and_breakeven.md`](../finance/03_cash_flow_and_breakeven.md)

---

## Canvas Overview

```text
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│ KEY PARTNERS    │ KEY ACTIVITIES  │ VALUE PROPOS.   │ CUSTOMER REL.   │ CUSTOMER SEGS   │
│                 │                 │                 │                 │                 │
│ • Fast Delivery │ • Catalog QA &  │ SHOPPERS:       │ • Self-serve    │ • Duhok social  │
│   (intra-city)  │   dedup defense │ • See all prices│   app, zero     │   shoppers      │
│ • ZMC Express   │ • Courier ops & │  side-by-side   │   DM free       │   (n=179: 97%   │
│   (Phase 2      │   dispatch      │ • "Best Value"  │ • Verified      │   notice price  │
│   linehaul)     │ • Merchant      │  picks itself   │   sellers,      │   gaps; 88%     │
│ • FIB / FastPay │   onboarding &  │ • COD default   │   reviews,      │   would use)    │
│   / Qi Card     │   support       │ • Trusted,      │   ratings       │                 │
│ • OTPIQ         │ • Fraud & abuse │  no DM "Price?" │ • Credits &     │ • Social sellers│
│   (OTP/msg)     │   monitoring    │ • Delivery in   │   referrals     │   (IG/FB: 85%   │
│ • Founder's     │ • Trilingual    │  hours, tracked │   (credit-only) │   of n=20; 75%  │
│   Circle stores │   content/brand │                 │ • Support via   │   interested;   │
│ • GIZ/CAPA      │                 │ MERCHANTS:      │   WhatsApp      │   ~8 pilot      │
│   program       │ KEY RESOURCES   │ • Free catalog  │ • Weekly        │   leads)        │
│                 │                 │  tools — no     │   settlement    │                 │
│ COST STRUCTURE  │ • Single-SKU    │  dev cost       │   statement     │ • Phase 2+:     │
│                 │   master        │ • DM relief —   │                 │   Erbil, Mosul, │
│ • Dev burn ~210k│   catalog (the  │  orders not     │ CHANNELS        │   Sulaymaniyah, │
│   IQD/mo        │   moat)         │  interrogations │ • App + mobile  │   Baghdad,      │
│ • Launch burn   │ • Merchant      │ • Progressive   │   web           │   Basra         │
│   ~652k IQD/mo  │   network &     │  fee 5/3/1.5%   │ • Bio links     │                 │
│ • Variable/order│   their social  │  (vs 10–15%     │  (getcheapify.  │                 │
│   ~courier+OTP  │   audiences     │  incumbents)    │  com/@store)    │                 │
│ • Incentives    │ • Courier       │ • New sales     │ • Trilingual    │                 │
│   pool (capped) │   contract      │  channel        │   social content│                 │
│ • Registration/ │   (Fast Del.)   │ • Merchant      │ • Parcel QR     │                 │
│   legal         │ • Founder build │  dashboard —    │ • WhatsApp      │                 │
│                 │  (app+dashboard)│  catalog, stock,│   notifications │                 │
│                 │ • Trilingual    │  orders, prices │                 │                 │
│                 │   brand system  │ • Verified      │                 │                 │
│                 │ • Waitlist: ~52 │  seller badge   │                 │                 │
│                 │   shoppers / ~8 │                 │                 │                 │
│                 │   merchants     │                 │                 │                 │
├─────────────────┴─────────────────┼─────────────────┴─────────────────┴─────────────────┤
│ REVENUE STREAMS                   │                                                 │
│ • Progressive commission 5%/3%/   │                                                 │
│   1.5% marginal (eff. ~3.8% at    │                                                 │
│   25k AOV ≈ 950 IQD)              │                                                 │
│ • Delivery margin +500 IQD/zone   │                                                 │
│   (contingent on courier contract)│                                                 │
│ • Future: promoted placement,     │                                                 │
│   premium merchant tools, e-      │                                                 │
│   wallet float (Phase 3+)         │                                                 │
└───────────────────────────────────┴─────────────────────────────────────────────────┘
```

---

## Block-by-Block Detail

### 1. Customer Segments

| Segment | Evidence | Why first |
| :--- | :--- | :--- |
| **Duhok social shoppers** — buy via Instagram/Facebook DMs today | Survey n=179: 97% notice price gaps, 88% would use a comparison app, 41% left beta contacts | Core problem is measured, not assumed |
| **Duhok social sellers** — IG/FB-first merchants, no dev budget | Survey n=20: 85% sell via IG/FB, 75% platform-interested, ~8 valid pilot leads | Supply side pre-validated; cohort exists on paper |
| Phase 2+: Erbil, Mosul, Sulaymaniyah, Baghdad, Basra | Identical social-commerce patterns per market sizing | Same playbook, bigger pools |

### 2. Value Propositions

**Shoppers — "The bright side of choosing":**

- All prices for the same product, side-by-side, on one master page — ends the "DM for price" interrogation
- Best Value badge resolves price + delivery time + seller rating into one decision
- COD default (no prepayment trust required), tracked delivery, verified sellers only
- Doorstep Total shown upfront — item price + zone delivery fee, never surcharges after

**Merchants — "Orders, not interrogations":**

- Merchant dashboard — free catalog, order, inventory & pricing tools in one place (their #3 headache: own-app cost; settlement transparency per `fee_structure_and_monetization.md` §7)
- Automated order pipeline replaces 50–100 daily price-DMs (their #1 headache)
- Progressive fee 5/3/1.5% marginal — effective ~3.8% at typical prices vs. incumbents' 10–15%
- Bio link becomes a revenue channel they own: `getcheapify.com/@store`
- Competitive price alerts (Best Value visibility) — they see where they stand

### 3. Channels

| Channel | Role | Stage |
| :--- | :--- | :--- |
| App + mobile web | Transaction core | Launch |
| Bio links (`@store`) | Merchant-driven acquisition — converts their existing audience | Launch |
| Trilingual social content (FB/IG/TikTok) | Demand generation, Phase A pre-launch → Phase B launch | Pre-launch |
| Parcel QR codes | Every delivery re-advertises the platform | Launch |
| WhatsApp notifications | Operational channel (order routing, OTP, statements) — not a storefront | Launch |

### 4. Customer Relationships

- **Self-serve by design** (ADR-008 / Preference 22): onboarding is rules-based, no manual service labor — keeps the model scalable
- **Trust layer:** verified-seller badges, ratings, reviews, fault-return enforcement — the relationship is mediated by platform policy, not personal trust
- **Retained via credit economy:** all rewards are platform credit (non-cash, 60-day expiry) — every incentive forces a second transaction
- **Merchant relationship:** weekly settlement statements, reliability scores, competitive pricing data — a tool they use daily, not a marketplace they tolerate

### 5. Revenue Streams

| Stream | Mechanics | Status |
| :--- | :--- | :--- |
| **Progressive commission** | 5% ≤10k · 3% 10–100k · 1.5% >100k IQD marginal; effective ~3.8% at 25k AOV ≈ ~950 IQD/order | Core — Phase 1 |
| **Delivery margin** | Zone fee = courier contract rate +500 IQD (3,000/4,000/5,000 customer-facing) | Core — **contingent on contract signature** |
| Promoted placement / ad boosts | Growth points → paid boosts for winning offers | Phase 2 |
| Premium merchant tools | Analytics, bulk tools | Phase 3 |
| Payment float / e-wallet margin | FIB/FastPay/Qi prepayment economics | Phase 3 |

**Contribution/order (current model): ~+1,015 IQD** after courier cost, OTP/messaging, packaging amortization. Break-even ~642 orders/month (~21/day, ~1 order/store/day at 20 stores).

### 6. Key Resources

| Resource | Status | Notes |
| :--- | :--- | :--- |
| **Single-SKU master catalog** | Being built — merchant-created, barcode-first, dedup-defended | *The moat* — compounds with every listing; no competitor offers it locally |
| Merchant network + their social audiences | ~8 valid pilot leads (survey), Founder's Circle 20-store target | Supply side = acquisition channel |
| Courier contract (Fast Delivery) | Quote verified (2,500/3,500/~4,500) — **unsigned** | Single gate to delivery margin |
| Platform surface: shopper app + **merchant dashboard** | In progress | The merchant's daily ops UI — catalog, pricing, orders, settlement, reliability score |
| Founder full-stack build | In progress | Cash-efficient, but real economic value (~$9,500 co-investment incl. equipment + labor) |
| Trilingual brand system (EN/AR/KU, IBM Plex Sans Arabic) | Complete — brandbook published | Local-language trust signal |
| **Waitlist** | ~52 actionable shopper + ~8 merchant contacts (survey, Oct 2026 — quality-audited) | Pre-seeded launch demand, zero CAC |
| Verification + reliability-score data | System designed | Becomes the trust moat over time |

### 7. Key Activities

1. **Catalog governance** — QA gate <2h, four-layer duplicate defense, shared-ownership improvements (see `catalog_governance.md`)
2. **Courier operations** — order routing, zone dispatch, failed-delivery handling, weekly COD reconciliation (see SOP-2)
3. **Merchant onboarding & support** — self-serve flow + verification + activation monitoring (see SOP-1)
4. **Fraud & abuse monitoring** — 7-layer anti-fraud stack (referral gaming, fake COD orders, bypass attempts)
5. **Trust enforcement** — return adjudication, reliability scores, prohibited-goods removal
6. **Trilingual content & demand generation** — Phase A/B content calendars
7. **Data loop** — every claim/flag/return feeds the matcher, reliability scores, and Best Value weights

### 8. Key Partnerships

| Partner | Role | Status |
| :--- | :--- | :--- |
| **Fast Delivery** (Duhok) | Intra-city 3PL pilot partner — zones A–C | Quote verified; contract pending registration |
| **ZMC Express** | Phase-2 inter-city linehaul (Duhok↔Erbil↔Baghdad), COD-capable, Duhok branch on Barzan Rd | Second quote for leverage; Phase 2 partner |
| **FIB / FastPay / Qi Card** | Phase-3 e-wallet prepayment | Integration planned; never required (COD default) |
| **OTPIQ** | WhatsApp-first OTP (40 IQD) + SMS fallback (80–250 IQD) | Desk-verified pricing |
| **Meta (WhatsApp Cloud API)** | Order notifications, order routing | Per-message pricing ~$0.01–0.02 |
| **Founder's Circle merchants** | Supply + co-marketing (bio links, free ad boosts) | 20-store target; 13 already expressed via survey |
| **GIZ / CAPA program** | Seed funding + institutional validation | Ranked awards pending pitch |

### 9. Cost Structure

| Layer | Amount | Notes |
| :--- | :--- | :--- |
| **Phase A dev burn** | ~210,000 IQD/mo | AI/SaaS tools + 75k audience-building ads |
| **Launch operating burn** | ~652,000 IQD/mo → ~790k at M6+ | Support, ops, tools, ads at scale |
| **Variable per order** | courier 2,500–4,500 (passed through) + ~50 IQD OTP/messaging + packaging | Margin holds via zone fees |
| **Growth incentives pool** | Capped marketing line | Credit-only, transaction-gated (anti-fraud) |
| **Registration + legal** | ~$1,000 one-time | Critical-path: unlocks courier contract → unlocks margin |
| **Peak funding need** | 3.37M IQD (~$2,250) planning case; 4.28M (~$2,850) floor | `finance/03` — bounded by burn ceiling, not order volume |

---

## What the Canvas Proves About the Model

1. **The moat is the catalog, not the app.** Anyone can build a marketplace app; a dedup-defended single-SKU catalog with communal improvement is structurally hard to copy and compounds daily.
2. **Supply and demand bootstrap each other.** Merchants bring audiences (bio links); the waitlist brings orders (~52 actionable contacts) — the cold-start problem is partially solved before launch.
3. **Every reward is engineered against fraud and churn.** Credits-only, transaction-gated, expiry-bounded — the model pays for delivered orders, never for signups.
4. **The unit economics work at small scale.** +1,015 IQD/order against ~652k burn = break-even at ~1 order/store/day — no growth-at-all-costs dependency.
5. **The single critical dependency is named:** registration → courier contract → delivery margin. Everything else is parallel work, not sequential risk.
