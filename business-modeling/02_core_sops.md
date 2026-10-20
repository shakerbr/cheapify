# Cheapify — Core Standard Operating Procedures (SOPs)

**Category:** Pillar 4 — Business Modeling
**Status:** Working Standard — operationalizes existing platform policies
**Date:** October 20, 2026

Cross-References:

- Order lifecycle policies (returns, shipping, packaging, payments): [`../platform/operational_policies.md`](../platform/operational_policies.md)
- Merchant rulebook & self-serve flow: [`../marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md) §2.4–2.5
- Listing creation & dedup: [`../platform/catalog_governance.md`](../platform/catalog_governance.md)
- Settlement mechanics: [`../platform/fee_structure_and_monetization.md`](../platform/fee_structure_and_monetization.md) §7
- Activation gates & credits: [`../platform/referral_and_growth_incentives.md`](../platform/referral_and_growth_incentives.md)

Each SOP is written for the pilot phase (founder + courier partner, minimal staff). Steps marked **[auto]** are platform-automated; **[manual]** require a human; **[courier]** belong to the 3PL partner.

---

## SOP-1: Merchant Onboarding

**Purpose:** convert a social seller into a verified, live, transacting merchant — self-serve, rules-gated, no manual page-building.
**Trigger:** merchant applies via portal, or accepts Founder's Circle / nomination invite.
**Done when:** merchant is verified, first listings live, bio link deployed, storefront receiving orders.

| # | Step | Actor | SLA |
| :--- | :--- | :--- | :--- |
| 1 | Invite/application received → merchant portal access issued | [auto] | instant |
| 2 | Merchant reviews Merchant Standards & Rulebook (4 rules: price integrity, media quality, live stock, standard 3PL) and accepts | [manual: merchant] | self-paced |
| 3 | Identity & shop verification: phone OTP, shop name, physical location/social page proof | [auto] + spot-check | <24h |
| 4 | Catalog setup: scan barcode → claim existing master page (1 tap: price, stock, variants) **or** create new listing via guided template | [manual: merchant] | self-paced |
| 5 | QA gate on every new/claimed listing — auto-checks + spot review → live, or returned with a specific fix note | [auto] + review | <2h |
| 6 | Bio link live: merchant places `getcheapify.com/@store` in bio/stories → orders open | [manual: merchant] | day 1 target |
| 7 | Free ad boost: merchant's Best Value-winning products featured in Cheapify paid social ads (Founder's Circle perk) | [auto] | first 90 days |
| 8 | Activation monitoring: merchant counts toward activation gate (**10 completed orders**) for referral/incentive purposes | [auto] | rolling |

**Edge cases & escalation:**

- **Listing rejected twice** → onboarding assist chat opens (WhatsApp support); still self-serve, but guided.
- **No sales in 14 days** → proactive check: is bio link live? are prices competitive vs. existing offers? → coaching nudge, never manual listing edits by staff.
- **Founder's Circle only:** the 13 survey-expressed merchants get priority QA queue + free packaging kit (first 90 days) — see `referral_and_growth_incentives.md` §4, `operational_policies.md` §3.
- **Suspension triggers:** watermark/phone-number media, price above social-media price (Rule 1), repeated out-of-stock cancellations (Rule 3), prohibited goods (Rule 7) — per `catalog_governance.md` §2.

**Metrics:** time-to-first-listing, listings/merchant, activation rate (merchants reaching 10 orders), suspension rate.

---

## SOP-2: Order → 3PL Courier → Delivery → Settlement

**Purpose:** move one paid-by-COD order from checkout to cash settlement, hands-free where possible.
**Trigger:** shopper checkout confirms order (COD default).

```text
[Checkout]─►[Merchant accept]─►[Pack per policy]─►[Courier pickup]─►[Delivery+COD]─►[Weekly settlement]
                │                                   │                  │
                ▼ decline/stale                     ▼                  ▼ fail ×2
           [auto-refund/alert]                [re-dispatch]      [return leg →
                                                                merchant + flags]
```

| # | Step | Actor | SLA |
| :--- | :--- | :--- | :--- |
| 1 | Order placed → merchant notified (app + WhatsApp) → accepts/declines | [manual: merchant] | accept within 2h or auto-alert |
| 2 | Merchant packs per packaging policy: opaque sealed mailer, waybill flat on largest face, security tape if ≥50,000 IQD or electronics/perfume, **no external branding/contacts** | [manual: merchant] | same day |
| 3 | Courier pickup dispatched via 3PL integration/notification | [auto]+[courier] | same-day if ordered <17:00, else next day |
| 4 | Delivery attempt → customer pays COD (item price + zone fee: A 3,000 / B 4,000 / C 5,000) | [courier] | target 1–3h hyperlocal |
| 5 | Delivery confirmed → order marked delivered → referral/incentive gates unlock (transaction-gated rewards) | [courier]+[auto] | on confirmation |
| 6 | Courier remits collected COD funds weekly | [courier] | weekly |
| 7 | Settlement: Cheapify deducts progressive fee + return legs + credit usage → net payout to merchant (bank transfer / e-wallet) + WhatsApp statement | [auto] | every Sunday |

**Failed-delivery branch:**

- Attempt fails (customer not home / unreachable) → **one free re-attempt next day** [Policy].
- Second failure → parcel returns to merchant; customer account flagged.
- ≥3 failed COD deliveries → customer loses COD privilege (prepaid-only or suspension).

**Edge cases & escalation:**

- **Courier SLA breach** (pickup >24h late) → escalate to Fast Delivery contact; log against courier scorecard — this is why the second-quote option stays warm.
- **Cash custody:** contract must fix *who holds COD cash and when it remits* [Assumption — see `operational_policies.md` §4]. Weekly remittance is the planning default.
- **Zone C ambiguity:** Zakho-tier rate (~4,500 contracted assumed) to be confirmed at contract signing; fee already set to 5,000 to hold +500 margin either way.

**Metrics:** delivery success rate, median delivery time (target ≤3h city), failed-delivery rate, settlement accuracy, courier SLA compliance.

---

## SOP-3: Returns & Refunds

**Purpose:** resolve post-delivery issues fairly without turning the courier into a dispute judge.
**Trigger:** customer taps "Report issue" within **48 hours** of delivery confirmation.
**Done when:** refund/credit issued, item back with merchant or case closed.

| # | Step | Actor | SLA |
| :--- | :--- | :--- | :--- |
| 1 | Customer reports issue → classifies as **fault** (wrong/defective/not-as-described — photo evidence required) or **remorse** (changed mind, unused, original packaging) | [manual: customer] | 48h window |
| 2 | Claim reviewed → return courier dispatched | [auto]+[courier] | next day |
| 3 | Merchant inspects item on receipt → confirms condition | [manual: merchant] | <48h |
| 4 | Refund released: **fault → cash/e-wallet refund, merchant pays return leg** (deducted from settlement) + reliability deduction; **remorse → platform credit, customer pays 3,000 IQD return leg** | [auto] | on inspection pass |

**Rules (from `operational_policies.md` §1 — all [Policy]):**

- No doorstep adjudication — the courier never decides; everything routes through the in-app flow.
- Broken security-tape seal at delivery = automatic fault eligibility, no dispute.
- Serial returners (>30% return rate across 10+ orders) flagged → lose remorse-return privilege.
- Remorse refunds are **platform credit** [recommended], fault refunds cash — keeps failed transactions inside the ecosystem while protecting buyers from real harm.

**Edge cases & escalation:**

- **Merchant disputes fault claim** → support reviews photo evidence + order record → adjudication log feeds reliability score.
- **Item returned used/damaged on remorse claim** → merchant photo evidence → claim denied, credit withheld, customer flagged.
- **COD refund rail** — the actual refund mechanics depend on courier remittance terms [open item in `operational_policies.md` §5]; platform-credit path works under any rail.

**Metrics:** return rate by class (baseline est. 3–5% — pilot data will replace), fault-return share per merchant (reliability input), dispute rate, refund cycle time.

---

## SOP Interdependencies

```text
SOP-1 produces ──► verified merchants with live listings ──► SOP-2 consumes
SOP-2 produces ──► delivery outcomes + COD cash ──► SOP-3 consumes (post-delivery issues)
SOP-3 produces ──► reliability/return signals ──► feeds SOP-1 monitoring + Best Value ranking
```

All three SOPs share one spine: **every state change is a logged event** — order status, delivery outcome, return class, settlement line. The data exhaust is the product: it tunes Best Value weights, fraud heuristics, and the financial model's assumptions.
