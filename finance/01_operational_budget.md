# Cheapify — Operational Budget

## Startup Costs · Monthly Burn · Per-Order Variable Economics

**Pillar:** Finance Management (Pillar 3 — File 01)
**Status:** Assumption-Driven Model v1 — every unverified figure is marked `[ASSUMPTION]`; replace with real quotes to finalize
**Currency convention:** IQD primary, USD secondary. Exchange benchmark: **1 USD ≈ 1,500 IQD** (per [`../entrepreneurship/02_market_opportunity_and_sizing.md`](../entrepreneurship/02_market_opportunity_and_sizing.md))
Cross-References:
- Order-lifecycle policies: [`../platform/operational_policies.md`](../platform/operational_policies.md)
- Incentive pool (cost source): [`../platform/referral_and_growth_incentives.md`](../platform/referral_and_growth_incentives.md) §5
- GTM volume targets: [`../marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md) §4–5

---

## 1. Budget Philosophy

Cheapify's structural advantage is that the two most expensive lines in a normal startup — **software development and creative production — are $0** (founder-built, per [`../marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md) §6). The budget therefore concentrates entirely on: infrastructure, order-fulfillment economics, growth spend, and legal/compliance.

> The model is built so any `[ASSUMPTION]` cell can be replaced by a real quote — the scenario tables in §5 recompute from it.

---

## 2. Assumptions Register

All external figures live here. Replace values (not formulas) when real quotes arrive.

| ID | Assumption | Working value | Range sanity check | Source status |
| :--- | :--- | :--- | :--- | :--- |
| A1 | Courier cost per delivered parcel (contract rate) | **2,500 city / 3,500 near / 4,500 far IQD** `[QUOTE-VERIFIED]` | list +500 | Fast Delivery (Duhok) — zones in operational_policies §2 |
| A2 | Customer delivery fee (charged) | **3,000 IQD** | Policy-fixed | Set (operational_policies §2) |
| A3 | Failed-delivery re-attempts per 100 orders | **8** `[ASSUMPTION]` | 5–15 | Pilot data |
| A4 | Return rate (all classes) | **4%** `[ASSUMPTION]` | 3–8% | Pilot data |
| A5 | Avg order value (AOV) | **25,000 IQD** `[ASSUMPTION]` | 15,000–40,000 | Social-seller price survey |
| A6 | WhatsApp Cloud API cost/message | **~$0.01–0.02 (~15–30 IQD)** `[DESK-VERIFIED]` | Meta per-message since Jul 2025 | OTPIQ WhatsApp OTP = 40 IQD/msg (local benchmark) |
| A7 | SMS OTP cost per message | **80–100 IQD (Korek/Asiacell), 250 (Zain)** `[DESK-VERIFIED]` | OTPIQ Iraq pricing | Route OTP via WhatsApp first (40 IQD) → blended ~50 IQD |
| A8 | Meta/TikTok effective CPM (Duhok) | **$2.00** `[ASSUMPTION]` | $1–4 | First test campaign |
| A9 | Orders per merchant per month (mature store) | **~30 reported** `[INTERVIEW n=1]` | total DM volume | Cheapify capture = slice of this; first merchant interview |
| A10 | Referral/incentive payout rate (per 100 orders) | **20 credits** `[ASSUMPTION]` | 10–30 | Post-launch data — paid from the capped Growth Incentives pool (§4), not per order |
| A11 | Effective take-rate on AOV 25,000 | **3.8%** | computed | 500 + 3%×15,000 = 950 IQD → 3.8% |
| A12 | Founding-merchant packaging kit subsidy | **~40,000 IQD per store** `[ASSUMPTION]` | 25k–60k | Print quotes |
| A13 | Card / e-wallet processing fee (card orders only, added shortly after launch) | `[OPEN — gateway quote needed]` | not yet quoted | Payment-gateway quote; requires business registration |

---

## 3. One-Time Startup Costs

| Item | Cost (IQD) | ~USD | Status |
| :--- | :--- | :--- | :--- |
| KRI business registration + Chamber of Commerce | 450,000–900,000 `[ASSUMPTION]` | $300–600 | Needs legal quote |
| Apple Developer Program (annual) | 148,500 | $99 | Known |
| Google Play Developer (one-time) | 37,500 | $25 | Known |
| Domain `getcheapify.com` (year 1) | 15,000 | ~$10 | **Already paid by founder** |
| Founding-merchant packaging kits ×20 (A12) | 800,000 `[ASSUMPTION]` | ~$530 | Print quotes needed |
| Initial thermal waybill/label stock | 75,000 `[ASSUMPTION]` | $50 | Print quote |
| **Total startup** | **~1.48M–1.93M IQD** | **~$985–1,285** | |

Design/brand/dev work: $0 — all in-house.

### 3.1 Founder-Contributed Resources (Already Covered — In-Kind)

Assets and services already paid for or owned by the founder — **real economic value, $0 incremental cash cost.** Listed so the budget reflects true operating cost vs. cash burn, and to document founder contribution.

| Resource | Est. value | Coverage | Notes |
| :--- | :--- | :--- | :--- |
| Domain `getcheapify.com` | ~15,000 IQD/yr | Paid through ~Oct 2027 | Cloudflare Registrar |
| Development PC/workstation | 850,000 IQD | Owned outright | All software/design work |
| Smartphones: Android + iPhone | 550,000 + 600,000 IQD | Owned | Test coverage both OSes + content capture |
| Internet (home) | 39,000 IQD/mo | Personal subscription | Confirmed |
| Electricity + workspace | ~30,000 IQD/mo `[ASSUMPTION]` | Household | Home office |
| Founder labor (dev, design, content, ops) | — | Ongoing | Sweat equity; market-rate value tracked for pitch honesty |
| **In-kind monthly equivalent** | **~69,000+ IQD/mo** | | Plus one-time assets ~2.0M IQD |

If any of these lapse (domain renewal, hardware replacement, dedicated workspace), they graduate into the cash budget — currently $0 cash impact.

---

## 4. Monthly Recurring Costs (Pre-Launch Baseline)

Costs that run regardless of order volume:

| Line | IQD/mo | ~USD/mo | Notes |
| :--- | :--- | :--- | :--- |
| Supabase (Pro) + hosting | 37,500 `[ASSUMPTION]` | $25 | Free tier covers dev; Pro at launch (see §4.2) |
| Cloudflare (DNS/CDN/security) | 0 | $0 | Free tier |
| WhatsApp Cloud API base + support line | 30,000 `[ASSUMPTION]` | ~$20 | Conversation-based, scales in §5 |
| SMS OTP baseline (waitlist signups) | 15,000 `[ASSUMPTION]` | ~$10 | A7 × ~500 signups |
| Maps/geocoding | 0–22,500 `[ASSUMPTION]` | $0–15 | Free tier likely suffices |
| Paid ads (Phase A organic; test budget) | 150,000 `[ASSUMPTION]` | $100 | A8 — small test campaigns only |
| Growth incentives pool cap | 225,000 `[ASSUMPTION]` | $150 | Referral/catalog bounty ceiling/mo — all incentives are paid from this pool (not per order, see §5.2) |
| Software & AI tooling | 90,000 `[ASSUMPTION]` | ~$60 | AI dev assistant + paid SaaS; see §4.1 |
| Tools & SaaS (email, analytics) | 30,000 `[ASSUMPTION]` | $20 | Mostly free tiers |
| Legal/accounting retainer | 75,000 `[ASSUMPTION]` | $50 | Compliance bookkeeping |
| Founder labor | 0 | $0 | Sweat equity — real but uncosted |
| **Monthly baseline burn** | **~652,000 IQD** | **~$435** | |

*Burn phasing:* this baseline is the **operating** burn — ads test budget, incentive pool, OTP signups, WhatsApp line, and Supabase Pro activate at launch. During development/Phase A the real burn is ~210k/mo (AI tooling + SaaS + modest audience-building ad boosts). See `03` §1 for the split.

### 4.1 Software & AI Tooling Breakdown

| Tool | Cost | Status |
| :--- | :--- | :--- |
| AI dev assistant (Devin-tier) | ~60–120k IQD/mo `[ASSUMPTION]` | Paid — functions as the eng team |
| GitHub, VS Code, Figma, Canva, CapCut, Google Workspace | $0 | Free tiers suffice at this stage |
| AI API credits (catalog matching, moderation) | ~0 → scales | Phase-dependent; post-pilot |
| Video/design paid assets (stock, music) | 0 for now | In-house production |

**Principle:** pay only for tools that replace headcount. AI coding assistance replaces an engineering hire — high leverage. Design/video/content stays in-house per the capital-discipline model.

### 4.2 Infrastructure Scaling Ladder

Infra spend grows with scale, not ahead of it. Current lines cover the entire Duhok pilot; bottlenecks are per-message costs (variable, §5) and photo storage (slow-growing), never compute.

| Stage | Infra spend | Trigger to move up |
| :--- | :--- | :--- |
| **Dev → pre-launch** | ~$0–15/mo (free tiers) | Launch: Pro needed for no-pause + backups |
| **Pilot (Phase 1)** | ~$25/mo (Supabase Pro + free CDN) | Phase 2: multi-city, >1,000 SKUs, >10k users |
| **Regional (Phase 2+)** | ~$60–120/mo `[ASSUMPTION]` | Storage/bandwidth growth; evaluate per quotes |

---

## 5. Per-Order Variable Economics

What each delivered order actually costs vs. earns. **This table is the core of the model** — everything else is noise until per-order contribution is positive.

### 5.1 Per-order revenue (platform take-rate)

| AOV | Progressive fee | Effective rate |
| :--- | :--- | :--- |
| 10,000 IQD | 500 IQD | 5.0% |
| 25,000 IQD (A5) | 950 IQD | 3.8% |
| 50,000 IQD | 1,700 IQD | 3.4% |
| 100,000 IQD | 3,200 IQD | 3.2% |
| 200,000 IQD | 4,700 IQD | 2.35% |

### 5.2 Per-order variable costs `[ASSUMPTION-heavy]`

| Cost element | Per-order cost | Basis |
| :--- | :--- | :--- |
| Courier delivery (A1) | −2,500 IQD | Passthrough-ish |
| Customer delivery fee (A2) | +3,000 IQD | Revenue, not cost |
| → **Delivery margin per order** | **+500 IQD** | Verified at contract rate, uniform across all 3 zones — zero margin if unsigned |
| WhatsApp notifications ×2 (A6) | −90 IQD | Confirm + delivered |
| OTP amortized (A7 blended ~50) | −25 IQD | ~1 per 2 orders, WhatsApp-first routing |
| Return absorption (A4 × ~500) | −20 IQD | Merchant-pays model limits exposure |
| Failed-delivery absorption (A3/100 × A1) | −200 IQD | Re-attempts we eat |
| Incentives (A10) | 0 per order | Paid from the capped Growth Incentives pool — already a fixed 225,000 IQD/mo line in §4; charging it per order too would double-count |
| **Variable cost per order** | **−335 IQD** (excl. delivery) | 90 + 25 + 20 + 200 |

*Note: the +1,115 IQD/order contribution is the cash-on-delivery case; card processing fees (A13) are not yet quoted and are not included.*

*Correction (Oct 21, 2026): earlier versions stated −425 / +1,015 IQD, but the line items summed to −935 because a −600 per-order incentive line double-counted the pool in §4. Counting incentives once gives −335 / +1,115 (ADR-014).*

### 5.3 Contribution per delivered order

```
Platform fee (A5)        +950 IQD
Delivery margin          +500 IQD
Variable costs            −335 IQD
────────────────────────────────
Contribution / order   ~+1,115 IQD  (~$0.74)
```

Two sensitivities dominate:
1. A1 is quote-verified (Fast Delivery): contract rates 2,500/3,500/4,500 by zone vs. fees 3,000/4,000/5,000 → **+500 margin uniform everywhere — but only once signed.** Unsigned, city cost = 3,000 = fee → margin 0 → contribution ~615 (break-even ~1,060/mo). *The contract — which requires registration — is now a revenue-critical milestone, not paperwork.*
2. If incentive payouts run hotter than A10, the pool cap (225k/mo, §4) binds — rewards queue to the next month or values get re-tuned. Raising the cap raises fixed burn: a doubled pool (450k/mo) moves break-even to ~787/mo.

---

## 6. Monthly Burn Scenarios

*Authoritative timeline: [`03_cash_flow_and_breakeven.md`](03_cash_flow_and_breakeven.md) §3–4 — the table below mirrors its **planning (conservative) ramp**; `03` also carries the 2× upside scenario.*

| Scenario | Orders/mo | Merchants | Contribution | Burn | **Net** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase A dev months | 0 | 0 live | 0 | −210,000 | **−210,000 IQD (~$140)** |
| Month 1 post-launch | 100 | 10 | +111,500 | −652,000 | **−540,500 IQD (~$360)** |
| Month 3 | 400 | 14 | +446,000 | −652,000 | **−206,000 IQD (−$137)** |
| Month 4 | 600 | 16 | +669,000 | −652,000 | **+17,000 IQD (~$11)** ← break-even |
| Month 5 | 1,000 | 18 | +1,115,000 | −652,000 | **+463,000 IQD (~$309)** |
| Month 6 | 1,350 | 20 | +1,505,250 | −790,000 | **+715,250 IQD (~$477)** |

Burn phases: ~210k/mo during dev (AI tooling + SaaS + modest audience ads) → 652k/mo operating at launch (ads, incentives, OTP, WhatsApp, Supabase Pro activate) → 790k/mo from M6 (scale).

**Break-even point:** ~**585 orders/month** at current assumptions (~20 orders/day; ~709/mo once burn steps up to 790k at M6). At the stated AOV and delivery margin the model turns contribution-positive surprisingly early; the risk is not the math but the A1/A4/A10 assumptions inside it.

---

## 7. Capital Requirement

The number that matters is the **deepest cumulative cash hole**, computed month-by-month in `03`:

| Scenario | Peak cumulative deficit | ~USD | When |
| :--- | :--- | :--- | :--- |
| Planning ramp (default) | −3.27M IQD | ~$2,180 | M3 |
| Upside (2× ramp) | −2.70M IQD | ~$1,800 | M2 |
| Slow-adoption floor (~25% ramp) | −4.12M IQD | ~$2,750 | M6 |

**Plan for ~$2,200–2,750 of founder-covered funds** before any grant — keeps the venture alive even at the slow-adoption floor. Anything beyond that (the `04` grant ask) buys speed: growth budget, registration, merchant materials, contingency — not survival.

Deliberately small either way — the founder-built stack keeps this in "savings + small grant" territory rather than raise-dependent.

---

## 8. Open Items Requiring Real-World Data

| Item | Needed input | Impact if wrong |
| :--- | :--- | :--- |
| ~~A1 courier cost~~ — **DONE** (Fast Delivery) | Contract signature + Zakho-tier confirm + 2nd quote | Contract worth ~500 IQD/order |
| A4 return rate | Pilot data | Variable-cost line doubles if ~8% |
| A8 ad CPM | $20 test campaign | Paid-CAC accuracy |
| A5 AOV | Social-seller price survey | All contribution math |
| Legal/registration | KRI registration quote | Startup line |
| Packaging/waybill print | Local print quotes | A12 + startup line |
| A9 merchant velocity | Pilot data | Month-3/6 scenario realism |
