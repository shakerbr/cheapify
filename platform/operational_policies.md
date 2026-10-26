# Cheapify — Operational Policies

## Returns · Shipping · Packaging · Payments — Order-Lifecycle Rules

**Category:** Cross-Cutting Platform Specification
**Status:** Draft Working Standard (ADR-013) — *policy defaults proposed; assumptions flagged for founder verification*
Cross-References:

- Merchant Rulebook (GTM §2.4): [`../marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md)
- Catalog incentives: [`referral_and_growth_incentives.md`](referral_and_growth_incentives.md)
- Fee architecture: [`fee_structure_and_monetization.md`](fee_structure_and_monetization.md)
- Source checklist: [`../agent/to-consider.md`](../agent/to-consider.md)
- Catalog rules (listings, dedup): [`catalog_governance.md`](catalog_governance.md)

Each policy is marked **[Policy]** (decided rule) or **[Assumption]** (proposed default pending real-world quotes/founder confirmation).

---

## 1. Return Policy

[Policy] Two return classes, one rule each:

| Class | Trigger | Who pays return leg | Merchant consequence |
| :--- | :--- | :--- | :--- |
| **Fault return** | Wrong item, defective, or not-as-described | **Merchant** (courier cost deducted from the merchant's payout, or settled electronically if already paid out) | Reliability-score deduction |
| **Remorse return** | Customer changed mind, item unused | **Customer** (3,000 IQD Duhok courier fee) | None — neutral event |

Rules:

- **Window:** 48 hours from delivery confirmation. Items must be unused, in original packaging.
- **Process:** customer taps "Report issue" → photo evidence for fault claims → Cheapify dispatches return courier → merchant inspects on receipt → refund released.
- **Refund mechanics [Policy]:**
  - **Card orders:** refunded to the original card or e-wallet.
  - **Cash orders, change of mind:** Cheapify platform credit.
  - **Cash orders, faulty item:** electronic transfer to the shopper's card or e-wallet; if the shopper has none, the courier hands cash back at return pickup and nets it from its next transfer to Cheapify `[TO CONFIRM AT CONTRACT SIGNING]`.
  - Refunds raised inside the 48-hour window are deducted before the merchant payout.

- **Merchant protection:** serial returners (>30% return rate across 10+ orders) get flagged and lose remorse-return privilege.
- **No doorstep negotiation:** the courier never adjudicates condition — everything goes through the in-app flow. This protects couriers from disputes and produces data.

---

## 2. Shipping Policy

[Policy] Duhok pilot:

- **Zone A — Duhok city: flat 3,000 IQD** per order.
- **Zone B — Near surroundings (Sharya, Semel, Domiz, Khanke): flat 4,000 IQD** `[DECISION PROPOSED]`.
- **Zone C — Far Duhok metro (Zakho & similar): flat 5,000 IQD** `[DECISION PROPOSED]` — courier rate ~4,500 contracted.
- **Uniform margin rule:** every zone fee = courier contract rate +500 IQD — same delivery margin everywhere; fee always shown inside the Doorstep Total, never added later.
- **SLA:** same-day dispatch for orders before 17:00; next-day otherwise. Hyperlocal target 1–3h where courier availability allows.
- **Merchant rule (GTM Rule 4):** merchants may not add packaging or delivery surcharges — the Doorstep Total is the whole price.
- **Geographic scope:** Duhok pilot covers Zones A–C; inter-city shipping (Erbil, Baghdad, etc.) is a Phase 2 tariff question, not a launch feature.

**Cost basis [QUOTE-VERIFIED — Fast Delivery, Duhok]:** list 3,000 city / 4,000 surroundings → **contract discount −500/order → 2,500 city / 3,500 near / ~4,500 far (Zakho).** Zone fees hold the +500 margin *only under contract* — unsigned, delivery is a zero-margin passthrough. Contract requires business registration → now a critical-path dependency, not paperwork. *Zakho tier rate to confirm; second courier quote still wanted for negotiating leverage.*

Failed deliveries [Policy]:

- One free re-attempt next day; second failure → parcel returns to merchant, customer account flagged.
- Customers with ≥3 failed COD deliveries lose COD privilege (card-only or account suspension).

**[Assumption] Inter-city (Phase 2+):** ZMC-style linehaul estimated 5,000–8,000 IQD per parcel — *needs quotes*. Regional delivery fee becomes a separate published tariff, never blended into item price.

---

## 3. Packaging Policy

[Policy] Minimum standard (all orders):

- Opaque, sealed mailer or box sized to the item — no loose or bag-visible items.
- Cheapify waybill (thermal label from merchant dashboard) attached flat on the largest face.
- No third-party branding, phone numbers, or social handles on outer packaging — the parcel is Cheapify's touchpoint, not an ad channel for bypassing the platform.

**[Policy] Tamper evidence:** orders ≥ 50,000 IQD (or electronics/perfumes regardless of price) ship with Cheapify branded security tape — broken seal at delivery = automatic fault-return eligibility, no dispute needed.

**[Policy] Branded kit:** Cheapify mailers + security tape + waybill stock are supplied **at cost** to all merchants and **free to Founder's Circle merchants** during their first 90 days — packaging doubles as street-level marketing (see brandbook §11 collateral).

---

## 4. Payment Methods

[Policy] Phase 1–2 (Duhok + regional):

- **Cash on delivery is available from launch and is never removed** — cash is collected by the courier at handover.
- **Card / e-wallet payment** (local gateway, e.g. FIB, FastPay, Qi Card, Visa/Mastercard) is added **shortly after launch**, once the payment-gateway account is approved (this requires business registration). Card payments go to Cheapify's payment account at checkout.
- **Cheapify never collects or handles cash.** All money between Cheapify and businesses (merchants, couriers, partners) moves electronically.
- **Platform credit** (referral/catalog rewards) auto-applies at checkout before the COD amount is computed.
- **Prohibited:** any arrangement where the customer pays the merchant directly outside the platform — bypassing destroys the fee model, the Best Value integrity, and the reliability score's meaning.

**[Policy] Settlement flow:**

- **Cash orders:** the courier collects the cash and transfers the **full collected amount electronically to Cheapify** within the deadline in the courier contract (target: within 24 hours of delivery) `[TO CONFIRM AT CONTRACT SIGNING]`.
- **Card orders:** the shopper's payment goes to Cheapify's payment account at checkout.
- **Split:** Cheapify keeps its fee and delivery margin, pays the courier its contracted rate electronically (on the contract's payment cycle), and pays the merchant the item price minus the fee.
- **Merchant payout:** automatic and electronic, **once the 48-hour return window after delivery closes** (for cash orders, also after the courier's transfer has arrived). No weekly cycle.
- **Payment account:** every merchant must link a payment account (bank card or e-wallet) during onboarding — required to receive payouts and to settle amounts owed after payout (e.g. a fault-return courier leg).

**Card / e-wallet processing fees (FIB & Qi — desk-verified):** SuperQi is **0%** under Qi's 2026 merchant promo, FIB in-app QR is **0.3%** (~84 IQD on 28,000), and the Central Bank of Iraq caps card MDR at **1%** (`cbi.iq`, customer surcharge prohibited). Because pre-paid orders eliminate doorstep refusal risk — saving the **200 IQD/order** failed-delivery allowance — digital orders yield **≥ +1,115 IQD/order**, so the +1,115 IQD contribution holds across both COD and FIB/Qi orders.

---

## 5. Open Items Requiring Real-World Data

| Item | Needed input | Blocks |
| :--- | :--- | :--- |
| ~~True Duhok courier cost~~ — **done** (Fast Delivery) | Contract signature | Shipping margin — verified |
| Courier transfer deadline and cash-refund netting | Courier contract terms | Settlement and refund mechanics |
| ~~Card processing fees~~ — **desk-verified** (FIB 0.3% QR / 1% card; Qi 0% promo; CBI 1% cap) | Commercial onboarding after registration | None — unit contribution stays ≥ +1,115 IQD |
| Inter-city tariff | ZMC inter-city quote | Phase 2 Doorstep Total |
| Return-rate baseline | Pilot data (est. 3–5%) | Pillar 3 cash flow |
