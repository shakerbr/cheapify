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
        │ SHOPPER  │ Referrer: │ Referrer:  │
 R      │          │ 3k credit │ 3 free     │
 E ┌───►│          │ Referee:  │ deliveries │
 F │    │          │    —      │ (≈9k IQD)  │
 E │    ├──────────┼───────────┼────────────┤
 R │    │ MERCHANT │ Referrer: │ Referrer:  │
 R │    │          │ growth pts│ 10k credit │
 E │    │          │ → boosts  │ + ad pts   │
 R │    └──────────┴───────────┴────────────┘
 E │
 R │   Activation gates (reward fires ONLY when):
   └──►  Shopper: first order DELIVERED & completed
        Merchant: verified + 10 completed orders
```

### 2.1 Shopper → Shopper

- **Referee gets:** no material reward — the platform itself is the reward (transparent prices, real savings on the first order). Attribution is frictionless: the shared link auto-associates, and a code can also be applied after signup so the referrer never loses credit to a bypassed link.
- **Referrer gets:** 3,000 IQD shipping credit, unlocked the moment the referee's first order is marked delivered.
- **Why it survives fraud:** the referrer earns nothing until real money moves. A family member who signs up but never shops produces zero rewards.
- **Cost efficiency:** paying only the referrer halves the per-acquisition incentive cost — ~3,000 IQD (~$2.30) per *activated* shopper.

### 2.2 Shopper → Merchant ("Nominate a Shop")

- **Mechanics:** any shopper can submit a social seller's @handle/link from the app ("this shop should be on Cheapify").
- **Shopper gets:** 3 free deliveries (~9,000 IQD credit) once the nominated merchant is verified **and completes 10 real orders**.
- **Strategic value:** converts the customer base into a merchant-scouting network and naturally extends the "Report a Price Variation" bounty — the crowd already finds stores; now it gets paid when they perform.

### 2.3 Merchant → Shopper

- **Mechanics:** the merchant's storefront link (`getcheapify.com/@store`) and in-parcel QR code double as referral links — no extra work, the bio-link play (GTM Play 1) already drives this traffic.
- **Shopper gets:** no material reward — same referrer-only model as §2.1.
- **Merchant gets:** growth points per activated shopper, redeemable for **ad boosts** (see §5). When redeeming, their **Best Value-winning products are the default recommended creative** — the ad can truthfully say "this offer won on price, speed, and rating."

### 2.4 Merchant → Merchant

- **Mechanics:** merchants share a referral link/code with other social sellers.
- **Recruiter gets:** a flat **10,000 IQD commission-offset credit + ad-boost points**, once the recruited shop is verified and completes 10 orders.
- **Why flat, not percentage:** a take-rate rebate scales with the *recruiter's* sales volume (45k–360k+ IQD over 60 days) — unbounded cost paying for the wrong thing. A flat bounty reflects the value of the *recruited shop* and stays inside the merchant-CAC target (<$10/store).
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

## 4. Catalog Creation & Improvement Bounties ("First to List")

**The incentive problem:** in a Single-SKU catalog, the first merchant to list a product does all the work while later merchants claim it in one tap. The bounty below compensates that asymmetry; the *mechanics* — barcode-first creation, QA gate, shared-ownership/edit-proposal model — live in [`catalog_governance.md`](catalog_governance.md) §1 & §3.

| Action | Reward | Gate |
| :--- | :--- | :--- |
| **Create an approved master listing** | **1,000 IQD catalog credit** | QA approval (photos clear, specs accurate, price transparent) |
| **Improve an existing listing** | **250 IQD micro-bounty** | QA approval of proposed edit |
| **Be the anchor offer** | 7-day "New Arrival" visibility | Competitive pricing vs. existing offers |

- Credits are usable **only as commission offset** — they reduce the merchant's take-rate bill, never cash out.
- Cap: **10 new master listings per merchant per day** (prevents junk-listing farming).
- Only **verified merchants** may create master listings.

---

## 5. Reward Economics

All incentive credits draw from a single **Growth Incentives pool**, funded as a marketing cost line (not from merchant margins):

| Reward | Cost (IQD) | Cost basis |
| :--- | :--- | :--- |
| Shopper referral (referrer only) | 3,000 | ≈ 1 delivery fee per activated buyer |
| Shopper → Merchant nomination | 9,000 | ≈ 3 delivery fees per performing merchant |
| Merchant → Merchant recruitment | 10,000 flat | Inside the <$10 merchant-CAC target |
| Catalog creation | 1,000 per SKU | One-time per SKU forever — every later merchant's claim is free |
| Catalog improvement | 250 per edit | Marginal quality spend |

**Sanity check vs. CAC targets:** the GTM shopper CAC target is <$0.50. A 3,000 IQD (~$2.30) referral cost exceeds that on paper — but it buys an *activated* buyer (one who already completed a real order), not an install. It is therefore booked as **activation + retention spend**, not acquisition spend, and is reviewed against blended CAC at the Month-2 report. If it outperforms paid CAC on a cost-per-ordering-customer basis, the pool grows; if not, the per-reward values are tuned down.

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
| Shopper referral credit | 3,000 IQD (referrer only) | = one delivery fee |
| Merchant nomination reward | 3 free deliveries | ≈ 9,000 IQD |
| Merchant→Merchant bounty | 10,000 IQD + ad points | Flat; bounded by CAC target |
| Catalog creation bounty | 1,000 IQD | Founder-set |
| Improvement micro-bounty | 250 IQD | Founder-set |
| Monthly referral cap / account | 5 rewards | Anti-fraud |
| Credit expiry | 60 days | Forces re-engagement |
| Merchant activation gate | 10 completed orders | Proves real seller, not shell |
