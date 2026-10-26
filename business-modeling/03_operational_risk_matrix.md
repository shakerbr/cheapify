# Cheapify — Operational Risk Matrix

**Category:** Pillar 4 — Business Modeling
**Status:** Working Standard — consolidates risks identified across Pillars 1–3 and platform specs
**Date:** October 20, 2026
**Method:** Likelihood (1–5) × Impact (1–5) → Score. H ≥15 · M 8–14 · L ≤7. Each risk carries a mitigation, an early-warning signal, and a status.

Cross-References:

- Financial downside cases: [`../finance/03_cash_flow_and_breakeven.md`](../finance/03_cash_flow_and_breakeven.md) §4–4.2
- Anti-fraud stack: [`../platform/referral_and_growth_incentives.md`](../platform/referral_and_growth_incentives.md) §3
- Dedup defense: [`../platform/catalog_governance.md`](../platform/catalog_governance.md) §4
- Order lifecycle rules: [`../platform/operational_policies.md`](../platform/operational_policies.md)
- Survey evidence (n=199): [`../entrepreneurship/05_market_validation_survey.md`](../entrepreneurship/05_market_validation_survey.md) §7

---

## 1. Risk Register

| ID | Risk | Cat. | L | I | Score | Mitigation | Early-warning signal | Status |
| :--- | :--- | :--- | :-: | :-: | :-: | :--- | :--- | :--- |
| R1 | **Traction shortfall** — order volume lands below even the slow case (half the planned pace) | Market | 3 | 5 | **15 H** | Slow case modeled (loss ceiling = ~$435/mo burn, no cliff); break-even needs ~390 regular shoppers; ~52-shopper actionable waitlist seeded; concierge pilot tests conversion and the new-vs-re-routed shopper split pre-scale; more stores if per-store velocity is low; monthly cohort review vs. slow curve | Week-over-week orders below the slow line; waitlist conversion <20% | Open — the venture's #1 risk |
| R2 | **Courier contract unsigned/delayed** — +500 IQD/order delivery margin evaporates | Partner | 3 | 4 | **12 M** | Contract open per founder; zone fees hold margin only under contract; ZMC second quote = fallback + leverage; zero-margin passthrough survivable (break-even ~1,060/mo, bounded) | Registration stalling; renegotiated rates | Open — critical path via R11 |
| R3 | **Courier transfers cash late / fails to transfer** — cash collected on delivery is not transferred to Cheapify on time | Financial | 3 | 4 | **12 M** | Courier contract sets a transfer deadline (target 24h after delivery) `[TO CONFIRM AT CONTRACT SIGNING]`; per-order reconciliation; merchants are paid only after the money arrives (and after the 48h return window); card payments (added shortly after launch) reduce cash exposure; Cheapify never handles cash | First transfer late; reconciliation gaps | Open — contract language decides |
| R4 | **Platform bypass (disintermediation)** — merchant + shopper take deals to DMs to dodge commission | Integrity | 4 | 4 | **16 H** | Fee kept low enough that bypass isn't worth it (~3.8% eff.); no contacts on packaging [Policy]; credits only spendable on-platform; reliability score counts only platform orders; Best Value only rewards compliant sellers | Merchants active but order-flat; same-SKU price drift vs. social pages | Mitigated by design — monitor |
| R5 | **Referral/credit fraud** — farming, self-referral, fake COD orders | Integrity | 3 | 3 | **9 M** | 7-layer anti-fraud stack: transaction-gated rewards, OTP identity, credit-only, velocity caps, heuristics, courier signal, manual review | Flagged-account rate >5%; delivery-failure clusters | Mitigated by design |
| R6 | **Merchant fraud** — counterfeits, mislabeled condition, bait-and-switch | Integrity | 3 | 4 | **12 M** | Verification gate; Rule 5 honest-condition labeling; fault returns auto-trigger + reliability deduction; prohibited-goods list (Rule 7) | Fault-return rate per merchant >baseline; photo-evidence patterns | Mitigated — enforced via SOP-3 |
| R7 | **Failed deliveries** — "buyer not home" pattern (confirmed real by merchant interview) | Operational | 4 | 3 | **12 M** | One free re-attempt; 3 failures → COD privilege revoked; address confirmation at checkout; WhatsApp pre-delivery notification | Failed-delivery rate >10% of attempts | Mitigated by policy |
| R8 | **Catalog pollution** — duplicate listings, junk-creation farming for credits | Operational | 3 | 3 | **9 M** | Four-layer dedup (barcode hard-block → multi-signal match → community flags → merge); credit revoked on post-existing duplicates; 10 listings/day cap | Duplicate-flag rate rising; creation spikes | Mitigated by design |
| R9 | **CAC above model** — ads underperform, bio links don't convert | Market | 3 | 3 | **9 M** | $20 paid-ad test planned before scale spend; referral channel as fallback; CAC:LTV reviewed monthly vs. ≥3:1 floor | Test CPC/CPM >targets; bio-link CTR low | Open — ad test pending |
| R10 | **Grant not awarded / smaller award** — envelope smaller than ask | Financial | 4 | 3 | **12 M** | Tiered ask — each amount a complete self-funding plan ($5,480 / $3,280 / $2,710, `finance/04` §1) with $0 out-of-pocket operating losses for the founder; baseline infra/messaging floor is ~$55/mo (~82.5k IQD/mo, or <$15/mo on free tiers) if discretionary burn lines are paused | Non-selection; award below the minimum tier | Open — pitch decides |
| R11 | **Registration/legal delay** — blocks courier contract → blocks delivery margin (gateway to R2) | Regulatory | 3 | 4 | **12 M** | Registration is identified critical-path; ~$1,000 budgeted; process startable now, parallel to build | Registration stuck >30 days | Open — sequential gate |
| R12 | **Founder key-person dependency** — illness, burnout, competing demands | Team | 2 | 5 | **10 M** | This repo externalizes all knowledge — SOPs, policies, model, brand; documentation-first culture makes the venture legible to a successor/partner | Velocity drops; single-point bottlenecks observed | Partially mitigated |
| R13 | **Competitor response** — Miswag/Elryan push into Duhok or poach merchants via affiliate deals (precedent: interviewee already runs a competitor's affiliate bio link) | Competitive | 2 | 4 | **8 M** | First-mover on single-SKU catalog; local focus incumbents lack; Founder's Circle locks early supply; affiliate displacement needs better economics — founding perks priced to win the bio slot | Competitor Duhok marketing; merchant poaching reports | Open — monitor |
| R14 | **WhatsApp/Meta API change** — pricing or policy shift breaks notification layer | Technical | 2 | 3 | **6 L** | OTPIQ multi-channel (WhatsApp 40 IQD + SMS fallback 80–250 IQD); utility messages already cheap (~$0.01–0.02); abstraction layer isolates provider | Meta pricing announcements; delivery-rate drops | Mitigated |
| R15 | **Kurdish-market blind spot** — survey n=10 Kurdish vs 168 Arabic; Badînî underrepresented | Market | 3 | 3 | **9 M** | Second survey targeted Kurdish-boosted via Meta ads (planned); native-speaker proofread pending on brand materials; Kurdish-first content in Phase A | Kurdish user engagement lags at launch | Open — known bias |
| R16 | **AOV assumption wrong** — 25,000 IQD drives contribution/order and break-even math | Financial | 3 | 3 | **9 M** | Concierge pilot measures real AOV; contribution scales linearly with AOV so error is bounded; model re-runs on pilot data | Pilot AOV deviates >30% | Open — pilot decides |
| R17 | **Demand shocks** — Eid spikes, economic events, connectivity disruptions | External | 3 | 2 | **6 L** | Asset-light: no fleet, no warehouse, no fixed capacity to strand; burn flexible monthly | Regional events; traffic anomalies | Accepted — low severity |

---

## 2. Risk Map

```text
IMPACT
  5 │        │           │   R12    │   R1     │
    │        │           │          │          │
  4 │        │           │R2 R3 R6  │   R4     │
    │        │           │R11 R13   │          │
  3 │        │           │R5 R8 R9  │   R7     │
    │        │           │R10 R15 16│          │
  2 │        │           │          │   R17    │
    │        │           │          │          │
  1 │        │           │          │          │
    └────────┴───────────┴──────────┴──────────┘
         1          2          3          4         5   LIKELIHOOD
        Rare      Unlikely   Possible   Likely   Almost
                                                  certain
```

---

## 3. Top-Ranked Risks (What to Watch)

**R1 — Traction shortfall (15).** Everything else is survivable; this is the venture. The mitigation is sequencing: concierge pilot → founding cohort → scaled spend. The model already plans at half-speed — the floor shows even quarter-speed degrades to a grind, not a death.

**R4 — Bypass (16).** Highest raw score. The design answer is making honesty cheaper than cheating: ~3.8% effective fee vs. the platform's discovery + trust + delivery + records value. Watch for merchants who list but never transact — the bypass signature.

**R2 + R11 — The contract chain (12+12).** Registration → contract → margin is the one true critical path. Both are fully controllable — they're execution, not luck.

**R7 — Failed deliveries (12).** Confirmed real by the merchant interview ("buyer says they aren't home"). Policy answer exists (re-attempt, COD revocation); the WhatsApp pre-delivery notification is the cheap preventive.

---

## 4. Monitoring Cadence

| Review | Contents | Trigger |
| :--- | :--- | :--- |
| **Weekly (pilot)** | Orders vs. floor ramp, delivery success %, fault-return rate | Every Sunday review (ops cadence, not a payout cycle) |
| **Monthly** | CAC:LTV vs. 3:1 floor, flagged-account rate, merchant activation (10-order gate), burn vs. budget | Month close |
| **Gate reviews** | Contract signed? Registration filed? Concierge pilot data in? | Before growth spend unlocks |
| **Re-score** | Full matrix re-rating | Quarterly, or on any risk event |

**Reporting note for GIZ:** this matrix doubles as the risk section of the funding narrative — a founder who names their own risks (and already modeled the downside) is the applicant evaluators trust.

---

## 5. Open Items Requiring Real-World Data

| Item | Needed | Resolves |
| :--- | :--- | :--- |
| Real order velocity | Concierge pilot (10–20 orders) | R1, R16 |
| Courier transfer deadline and cash-refund netting | Courier contract negotiation | R3 |
| Second courier quote | ZMC Express inquiry | R2 (leverage) |
| Real CPM/CPC | ~$20 Meta ad test | R9 |
| Kurdish demand signal | Kurdish-boosted survey wave | R15 |
| Registration timeline + cost | Initiate process / GIZ-CAPA guidance | R11 |
