# Cheapify — Referral System & Growth Incentive Architecture

**Category:** Cross-Cutting Platform Specification
**Status:** Approved Working Standard (ADR-012)
**Target Market:** Duhok Pilot ──► Regional Hubs ──► All Iraq
**Cross-References:**

- Fee architecture (credit source): [`fee_structure_and_monetization.md`](fee_structure_and_monetization.md)
- Merchant onboarding (Self-Serve with Rules): [`../marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md) §2.4, ADR-008
- Content plans (referral campaign hooks): [`../marketing/03_pre_launch_content_plan.md`](../marketing/03_pre_launch_content_plan.md), [`../marketing/04_launch_content_calendar.md`](../marketing/04_launch_content_calendar.md)
- Decisions: [`../agent/decisions.md`](../agent/decisions.md) (ADR-012) | Preferences: [`../agent/preferences.md`](../agent/preferences.md) (Preferences 31–32)

---

## 1. Design Philosophy: Pay for Transactions, Never for Signups

A referral reward that fires on account creation is fraud-bait: creating an account costs nothing, so farming accounts (family members, spare SIMs, bots) is free money. Cheapify's system is built on one principle:

> **Every reward in every direction unlocks only on a completed, courier-confirmed transaction — a real order, delivered, COD collected.**

A fake account can register, but it cannot fake a delivery: a completed order requires a real phone number, a real Duhok address, a real courier run, and real cash changing hands. Fraud that still attempts it burns a real 3,000 IQD delivery attempt and generates a delivery-failure flag — the system self-reports its own abuse.

All rewards are **platform credit** — never cash, non-transferable, one reward per order, expiring after **60 days**. Credits keep value inside the ecosystem and force a second transaction.

---

## 2. The Four-Direction Referral Grid

Cheapify's referral system runs in all four directions — shoppers and merchants can each refer both shoppers and merchants. This turns the entire user base into a distributed acquisition team.

```text
                        REFEREE
                   ┌───────────┬────────────┐
                   │  SHOPPER  │  MERCHANT  │
        ┌──────────┼───────────┼────────────┤
        │ SHOPPER  │  Free 1st │  3 free    │
 R      │          │  delivery │ deliveries │
 E ┌───►│          │  + 3k cr. │ (≈9k IQD)  │
 F │    ├──────────┼───────────┼────────────┤
 E │    │ MERCHANT │  Free 1st │ Commission │
 R │    │          │  delivery │ rebate or  │
 R │    │          │  + growth │ ad-boost   │
 E │    │          │  points   │ credit     │
 R │    └──────────┴───────────┴────────────┘
 E │
 R │   Activation gates (reward fires ONLY when):
   └──►  Shopper: first order DELIVERED & completed
        Merchant: verified + 10 completed orders
```

### 2.1 Shopper → Shopper

- **Referee gets:** free first delivery (3,000 IQD shipping credit applied automatically at checkout).
- **Referrer gets:** 3,000 IQD shipping credit, unlocked the moment the referee's first order is marked delivered.
- **Why it survives fraud:** the referrer earns nothing until real money moves. A family member who signs up but never shops produces zero rewards.

### 2.2 Shopper → Merchant ("Nominate a Shop")

- **Mechanics:** any shopper can submit a social seller's @handle/link from the app ("this shop should be on Cheapify").
- **Shopper gets:** 3 free deliveries (~9,000 IQD credit) once the nominated merchant is verified **and completes 10 real orders**.
- **Strategic value:** converts the customer base into a merchant-scouting network and naturally extends the "Report a Price Variation" bounty — the crowd already finds stores; now it gets paid when they perform.

### 2.3 Merchant → Shopper

- **Mechanics:** the merchant's storefront link (`getcheapify.com/@store`) and in-parcel QR code double as referral links — no extra work, the bio-link play (GTM Play 1) already drives this traffic.
- **Shopper gets:** the standard free first delivery.
- **Merchant gets:** growth points per activated shopper, redeemable for **ad boosts** (see §5). When redeeming, their **Best Value-winning products are the default recommended creative** — the ad can truthfully say "this offer won on price, speed, and rating."

### 2.4 Merchant → Merchant

- **Mechanics:** merchants share a referral link/code with other social sellers.
- **Recruiter gets:** commission rebate — **1% take-rate reduction for 60 days** — or an equivalent ad-boost credit, once the recruited shop is verified and completes 10 orders.
- **Recruited merchant gets:** priority onboarding assistance (faster QA queue).

---

## 3. Anti-Fraud Stack

Layered controls, cheapest first; escalation is automatic:

| Layer | Mechanism | Kills |
| :--- | :--- | :--- |
| 1. Transaction gate | Reward fires only on **delivered** order status | Signup farming, ghost accounts |
| 2. Identity | Phone OTP — one account per SIM; duplicate numbers blocked | Multi-accounting |
| 3. Credit design | Non-transferable, non-cash, one reward per order, 60-day expiry | Cash-out schemes, reward stacking |
| 4. Velocity caps | Max **5 referral rewards / account / month**; lifetime cap 20 | Industrial farming |
| 5. Heuristic flags | Same-device account clusters, same-address referral rings, accounts that refer but never order | Organized fraud |
| 6. Courier signal | Undelivered/fake orders burn real 3,000 IQD attempts and flag both parties | Fake COD orders |
| 7. Manual review | Outlier accounts held for review before payout | Edge cases |

**Rules of engagement:**

- A referral chain that fails delivery verification rewards nobody — both sides lose pending credit.
- Self-referral (same phone, device, or verified address) credits nothing.
- Referral credits may not be combined with other promotional credits on the same order.

---

## 4. Catalog-First-Mover Incentive ("First to List")

### 4.1 The Problem Being Solved

In a Single-SKU catalog, the first merchant to list a product does the heavy work — photos, name, description, specs — while every later merchant claims the existing page in one tap and only adds price, stock, and variants. Without compensation, rational merchants wait for others to do the work, and the catalog never fills.

### 4.2 Layer 1 — Shrink the Work: Barcode-First Creation

The primary fix is making creation nearly free, not merely paying for it:

- Merchant scans the product's **manufacturer barcode (EAN/UPC)** → the master page auto-fills name, specs, and reference imagery from aggregated product databases.
- **Coverage is strong for branded goods** (chargers, cables, perfumes, branded accessories) — precisely the SKUs duplicated across merchants where the first-mover asymmetry hurts most.
- **Local/unbranded goods** fall back to a guided creation template — barcode handles the high-duplication core; templates handle the tail.
- The merchant then only adds their own data: price, stock, color/measurement variants, and optional shop-specific photos.

### 4.3 Layer 2 — Pay the Creator: The Catalog Bounty

| Action | Reward | Gate |
| :--- | :--- | :--- |
| **Create an approved master listing** | **1,000 IQD catalog credit** | QA approval (photos clear, specs accurate, price transparent) |
| **Improve an existing listing** | **250 IQD micro-bounty** | QA approval of proposed edit |
| **Be the anchor offer** | 7-day "New Arrival" visibility | Competitive pricing vs. existing offers |

- Credits are usable **only as commission offset** — they reduce the merchant's take-rate bill, never cash out.
- Cap: **10 new master listings per merchant per day** (prevents junk-listing farming).
- Only **verified merchants** may create master listings.

### 4.4 Layer 3 — Shared Ownership, Not a Land-Grab

The master page is platform infrastructure, not the creator's property:

- The creator keeps permanent **"listed this product" attribution** on the page and their credit — never revoked.
- **Any verified merchant selling that product may propose improvements** (better photo, missing spec, corrected description, additional variants). Proposals queue for QA — nobody edits the page directly.
- **Approved improvements earn the 250 IQD micro-bounty**, so a weak first listing doesn't stay weak, and a merchant who finds a poor page profits by fixing it instead of duplicating it.
- **Full change history** on every master page — every edit attributed, reversible.

**Result:** being first is rewarded (credit + attribution + anchor visibility), but quality is communal — the catalog improves monotonically instead of rewarding first-come-low-effort listings.

---

## 5. Reward Economics

All incentive credits draw from a single **Growth Incentives pool**, funded as a marketing cost line (not from merchant margins):

| Reward | Cost (IQD) | Cost basis |
| :--- | :--- | :--- |
| Shopper referral (both sides) | 6,000 total | ≈ 2 delivery fees per acquired active buyer |
| Shopper → Merchant nomination | 9,000 | ≈ 3 delivery fees per performing merchant |
| Merchant → Merchant recruitment | ~1% take-rate for 60 days | Foregone commission, capped by cap |
| Catalog creation | 1,000 per SKU | One-time per SKU forever — every later merchant's claim is free |
| Catalog improvement | 250 per edit | Marginal quality spend |

**Sanity check vs. CAC targets:** the GTM shopper CAC target is <$0.50. A 6,000 IQD (~$4.60) full-cycle referral cost exceeds that on paper — but it buys an *activated* buyer (one who already completed a real order), not an install. It is therefore booked as **activation + retention spend**, not acquisition spend, and is reviewed against blended CAC at the Month-2 report. If it outperforms paid CAC on a cost-per-ordering-customer basis, the pool grows; if not, the per-reward values are tuned down.

**Monthly guardrail:** total incentive payout is capped at a fixed budget line in the operational budget; if the cap is hit, referral rewards queue to the next month rather than unbounded spend. (Exact cap set in [`../finance/01_operational_budget.md`](../finance/01_operational_budget.md).)

---

## 6. Abuse Scenarios & Responses

| Scenario | Response |
| :--- | :--- |
| Family/friends sign up but never order | No reward — nothing was ever paid |
| Fake COD orders to farm credit | Courier marks undelivered → no reward, delivery-failure flag, account review |
| Merchant mass-creates junk listings | QA rejects; 10/day cap; repeat offenders lose creation privilege |
| Rival merchants sabotage listings with bad edits | Proposals, never direct edits — QA rejects; edit history attributed |
| Referral rings (mutual referrals to farm) | Heuristic clustering flags; manual review before payout |
| Reward claims disputes | Support adjudicates from order/delivery records; credits are platform-granted and revocable for fraud |

---

## 7. Marketing Integration

- **Phase A (pre-launch):** the "send us shops" mechanic already exists as the Report-a-Price-Variation bounty — the nomination feature formalizes it at launch.
- **Phase B Week 6** ([`../marketing/04_launch_content_calendar.md`](../marketing/04_launch_content_calendar.md)): the "referral push" content announces the four-direction grid publicly — "refer a friend, refer a shop, get free delivery."
- **Parcel collateral:** every delivered parcel carries a QR code linking to the shopper referral program (merchant→shopper channel made physical).
- **Terminology:** marketed as "Refer & Earn" (EN) / localized per the trilingual lexicon; never "referral bonus cash" — credits, not money.

---

## 8. Open Configuration Values (Founder-Tunable)

| Parameter | Current value | Notes |
| :--- | :--- | :--- |
| Shopper referral credit | 3,000 IQD each side | = one delivery fee |
| Merchant nomination reward | 3 free deliveries | ≈ 9,000 IQD |
| Merchant→Merchant rebate | 1% take-rate, 60 days | Alternative: ad-boost credit |
| Catalog creation bounty | 1,000 IQD | Founder-set |
| Improvement micro-bounty | 250 IQD | Founder-set |
| Monthly referral cap / account | 5 rewards | Anti-fraud |
| Credit expiry | 60 days | Forces re-engagement |
| Merchant activation gate | 10 completed orders | Proves real seller, not shell |
