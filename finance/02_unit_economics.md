# Cheapify — Unit Economics

## CAC · LTV · Payback — Shoppers, Merchants, and the Referral Machine

**Pillar:** Finance Management (Pillar 3 — File 02)
**Status:** Assumption-Driven Model v1 — builds directly on [`01_operational_budget.md`](01_operational_budget.md) assumptions (A1–A12)
Cross-References:
- Referral/incentive economics: [`../platform/referral_and_growth_incentives.md`](../platform/referral_and_growth_incentives.md) §5
- GTM segments & CAC targets: [`../marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md) §3, §5
- Fee formula: [`../platform/fee_structure_and_monetization.md`](../platform/fee_structure_and_monetization.md)

---

## 1. The Two-Sided Unit-Economics Problem

A marketplace has **two** unit-economics questions, not one:

1. **Does a shopper pay for their acquisition?** (LTVₛ > CACₛ)
2. **Does a merchant pay for their acquisition?** (LTVₘ > CACₘ)

Both must hold *simultaneously* — Cheapify's design makes them unusually favorable because the merchant side partially *funds* the shopper side (bio-link traffic brings buyers at near-zero CAC).

---

## 2. Shopper Unit Economics

### 2.1 Revenue per shopper

From `01` §5.3: contribution per delivered order = **~+1,115 IQD** (fee 950 + delivery margin 500 − variable 335, at AOV 25,000).

| Parameter | Working value | Source |
| :--- | :--- | :--- |
| Orders per active shopper / month | **1.5** `[ASSUMPTION]` | Iraqi social-commerce cadence |
| Monthly contribution / active shopper | **~1,670 IQD** | ~1,115 × 1.5 |
| Expected active lifespan | **12 months** `[ASSUMPTION]` | Conservative for pilot |
| Retention haircut | **×0.6** `[ASSUMPTION]` | Churn-adjusted active months |
| **Shopper LTV (12-mo)** | **≈ 12,000 IQD (~$8.00)** | 1,670 × 12 × 0.6 |

### 2.2 Shopper CAC by channel

| Channel | CAC (IQD) | Mechanism |
| :--- | :--- | :--- |
| Organic / bio-link hijack | **~0** | Merchant's followers convert at $0 cost — GTM Play 1 |
| Shopper referral | **3,000** | Credit paid on first delivered order (referral spec §2.1) |
| Nominate-a-shop (as scout) | **9,000** | Only if the shop activates — a merchant-cost, not pure shopper CAC |
| Paid ads | **750–1,200** `[ASSUMPTION]` | A8 CPM → target CAC <$0.50–0.80 (GTM §5) |
| **Blended target** | **~1,500** | Mix-weighted |

### 2.3 The verdict

```
LTVₛ ≈ 12,000 IQD   vs   CACₛ ≈ 1,500 IQD   →   LTV:CAC ≈ 8 : 1
Payback: ~1–2 delivered orders
```

Healthy territory (≥3:1 is the usual bar). The number to watch is the **blended CAC** — if paid-ads share grows faster than organic+referral, CACₛ drifts up while LTV stays flat.

---

## 3. Merchant Unit Economics

### 3.1 Platform revenue per merchant

| Parameter | Working value | Source |
| :--- | :--- | :--- |
| Orders per merchant / month | **15** (A9) `[ASSUMPTION]` | Range 8–30 |
| Take-rate revenue / merchant / month | **14,250 IQD** | 15 × 950 |
| Servicing cost / merchant / month | **~2,000 IQD** `[ASSUMPTION]` | Support, QA, ads infra share |
| Monthly net / merchant | **~12,250 IQD** | |
| **Merchant LTV (12-mo, churn-haircut ×0.7)** | **≈ 102,900 IQD (~$69)** | |

### 3.2 Merchant CAC

| Path | Cost | Note |
| :--- | :--- | :--- |
| Direct outreach (founder) | **~5,000 IQD** `[ASSUMPTION]` | Time cost only; GTM target <$10 |
| Merchant→Merchant referral | **10,000 + ad points** | Per activated recruit |
| Shopper nomination | **9,000** | Paid to shopper, not merchant |
| **Founding Store package** (first 20 only) | **~65,000** `[ASSUMPTION]` | 0% month-1 (~14k foregone) + ad boost (~$10–20) + kit (40k) |

### 3.3 The verdict — normal path

```
LTVₘ ≈ 102,900 IQD   vs   CACₘ ≈ 5,000–10,000 IQD   →   LTV:CAC ≈ 10–20 : 1
Payback: < 1 month of active selling
```

### 3.4 Founding-store economics — deliberately unbalanced

A founding store *costs* ~65,000 IQD against ~103,000 LTV — still positive (~1.6:1), but that's not the real justification. The Founder's Circle is bought because **each onboarded store converts its own follower base into shoppers at ~$0 CAC** — the 65k isn't just acquiring a merchant, it's acquiring their audience. Treat founding-store spend as *joint merchant+shopper CAC*, where it looks like a bargain, not a subsidy.

---

## 4. Where Incentives Fit the Math

| Incentive | Booked as | Per-order drag (at A10) |
| :--- | :--- | :--- |
| Shopper referral credit | Shopper CAC | −30 IQD avg |
| Merchant recruit bounty | Merchant CAC | — |
| Catalog bounties | Content infrastructure | −10 IQD avg |
| Delivery margin subsidy | Variable cost | ±500 sensitivity |

The pool cap (225,000 IQD/mo in `01` §4) bounds worst-case incentive spend to ~7.5% of pilot-stage revenue — acceptable for a growth-phase subsidy, and it shrinks proportionally as volume grows.

Because incentives are budgeted as this capped pool (fixed burn), they are not deducted again in per-order contribution (ADR-014).

---

## 5. Sensitivity: What Breaks the Model

| Variable | Model breaks if | Current assumption |
| :--- | :--- | :--- |
| A1 courier cost | >3,000 IQD → delivery margin gone; >3,615 IQD → contribution per order turns negative | 2,500 (quote-verified, contract unsigned) |
| A5 AOV | Never negative per order (delivery margin covers variable cost); at 10,000 IQD contribution ~665 → break-even ~980/mo | 25,000 `[ASSUMPTION]` |
| Order frequency | <~0.37/mo → LTVₛ falls below the 3,000 IQD referral CAC | 1.5 `[ASSUMPTION]` |
| A10 incentive payout | Above the 225k/mo pool cap → rewards queue or get re-tuned; doubling the pool → break-even ~787/mo | 20 per 100 orders, capped by pool |
| Blended CACₛ | >~12,000 IQD → LTV:CAC <1 | ~1,500 |

**Single most important validation:** signing the courier contract (A1 is quote-verified but unsigned) — then real AOV and order frequency from the concierge pilot.

---

## 6. LTV:CAC Summary

| Side | LTV | CAC | Ratio | Payback | Health |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Shopper | ~12,000 IQD | ~1,500 IQD | **~8 : 1** | 1–2 orders | Strong |
| Merchant (normal) | ~102,900 IQD | ~5–10k IQD | **~10–20 : 1** | <1 month | Strong |
| Merchant (founding) | ~103,000 + audience | ~65,000 IQD | ~1.6 : 1 standalone | ~5 months | Justified by audience |

---

## 7. Open Items Requiring Real-World Data

| Item | Needed input | Impact |
| :--- | :--- | :--- |
| True courier cost (A1) | Courier quote | Flips delivery margin |
| Order frequency | Pilot cohort data | Drives both LTVs |
| Churn/retention | 90-day cohort | LTV haircut accuracy |
| AOV distribution | Seller price survey | Contribution/order |
| Blended CAC | First campaign data | Paid-channel weight |
