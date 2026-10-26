# Cheapify — Operational Budget

## Startup Costs · Monthly Burn · Per-Order Variable Economics

**Pillar:** Finance Management (Pillar 3 — File 01)
**Status:** Assumption-Driven Model v1 — every unverified figure is marked `[ASSUMPTION]`; replace with real quotes to finalize
**Currency convention:** IQD primary, USD secondary. Exchange benchmark: **1 USD = 1,500 IQD** — see §1.1.
Cross-References:
- Order-lifecycle policies: [`../platform/operational_policies.md`](../platform/operational_policies.md)
- Incentive pool (cost source): [`../platform/referral_and_growth_incentives.md`](../platform/referral_and_growth_incentives.md) §5
- GTM volume targets: [`../marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md) §4–5

---

## 1. Budget Philosophy

Cheapify's structural advantage is that the two most expensive lines in a normal startup — **software development and creative production — are $0** (founder-built, per [`../marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md) §6). The budget therefore concentrates entirely on: infrastructure, order-fulfillment economics, growth spend, and legal/compliance.

> The model is built so any `[ASSUMPTION]` cell can be replaced by a real quote — the scenario tables in §5 recompute from it.

### 1.1 Exchange Rate `[VERIFIED — Oct 2026]`

| Rate | IQD per USD | Source |
| :--- | :--- | :--- |
| CBI purchase from Ministry of Finance | 1,500 | [CBI, 7 Oct 2026](https://cbi.iq/news/view/3355) |
| CBI sale to banks | 1,510 | same |
| CBI cash sale to the public | 1,520 | same (previous rate: 1,320) |
| Parallel market (Duhok, 24 Oct 2026) | ~1,685 | [kakdolar.com](https://kakdolar.com/cities); Erbil/Baghdad ~1,677–1,685 |

The model converts at **1,500**, the official base rate. All costs are in IQD, so a grant paid in dollars and converted at the bank rate (1,510) yields slightly *more* IQD than modeled.

**Exposure:** tools billed in USD — Supabase, the AI assistant, SaaS, and part of paid ads (~337,500 IQD/mo of the 652k burn) — cost ~12% more if dollars must be bought at the parallel rate (~+42,000 IQD/mo). Pay them by FIB/Qi card at the official rate where possible.

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
| A13 | Card / e-wallet processing fee (FIB & Qi, added shortly after launch) | **0% SuperQi promo · 0.3% FIB QR in-app · 0.5% FIB QR link · 1% card gateway (CBI cap)** `[DESK-VERIFIED]` | 0%–1% | FIB published schedule (`fib.iq/fees-and-charges/`); CBI MDR cap at 1%; Qi 2026 0% merchant initiative |

---

## 3. One-Time Startup Costs

| Item | Cost (IQD) | ~USD | Status |
| :--- | :--- | :--- | :--- |
| KRI business registration + Chamber of Commerce | **~695,000–1,295,000** `[DESK-VERIFIED]` | **$465–865** | Companies Reg. ~154.5k (`xizmet.gov.krd`, Decree 119/2017) + Chamber 540k Kurdish/Arabic name or 1,140k English trade name (`krg.eregulations.org`); lawyer filing adds ~200–300k if used |
| Apple Developer Program (annual) | 148,500 | $99 | Known |
| Google Play Developer (one-time) | 37,500 | $25 | Known |
| Domain `getcheapify.com` (year 1) | 15,000 | ~$10 | **Already paid by founder** |
| Founding-merchant packaging kits ×20 (A12) | 800,000 `[ASSUMPTION]` | ~$530 | Print quotes needed |
| Initial thermal waybill/label stock | 75,000 `[ASSUMPTION]` | $50 | Print quote |
| **Total startup** | **~1.76M–2.56M IQD** | **~$1,170–1,710** | **~1.70M IQD baseline in `03`** = Kurdish/Arabic legal name (695k) + kits (800k) + app stores (186k) + labels (75k); **grant in `04`** funds the English trade-name option instead: registration 1.5M (incl. filing) + launch setup 1.061M = 2.56M |

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

*Burn phasing:*
- **Dev / Phase A (M-2, M-1): ~210,000 IQD/mo (~$140)** — AI tooling (90k) + SaaS (30k) + modest audience-building ad boosts (75k) + contingency (15k). Represents the pre-award incubation phase already completed before the grant.
- **Launch → M5 operating baseline: 652,000 IQD/mo (~$435)** — table above. The Growth Incentives pool will be **full from launch**: founding stores creating the first master SKUs earn 1,000 IQD per SKU (e.g. 20 stores × 50 SKUs ≈ 1M IQD of claims vs. a 225k cap). The cap bounds cash; claims above it queue to later months as a deferred credit liability. The founding stores' 0%-commission first month is therefore **not** absorbed by the pool — it is funded as its own grant line (~190,000 IQD, `04` §2 line 4).
- **M6+ baseline: 790,000 IQD/mo (~$527)** — steps up by **+138,000 IQD/mo (~$92)** from **M6 by calendar, in every scenario** (conservative — applied even in the slow case at 675 orders): maps/geocoding & infra above free tier (+22,500 IQD), higher support/OTP baseline (+40,500 IQD), and expanded retention/organic marketing (+75,000 IQD). See `03` §1–3.
- **Hard survival floor if orders stall (~82,500 IQD/mo ≈ $55/mo on paid tiers, or <$15/mo on free tiers):** Of the 652,000 IQD/mo ($435/mo) operating burn, **569,500 IQD/mo (~$380/mo)** is discretionary growth and support spend funded by the grant or by order revenue (150k test ads + 225k incentives pool paid only on delivered orders + 75k accounting retainer + 120k paid AI/SaaS tiers). The baseline infrastructure and messaging lines in §4 (Supabase Pro 37.5k + WhatsApp base 30k + SMS OTP baseline 15k) total just **82,500 IQD/mo (~$55/mo)** — and on Supabase's free tier with near-zero orders, cash burn drops below **$15/mo**. The founder is never exposed to paying $435/mo out of pocket.

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

*Note on card / e-wallet orders (A13):* +1,115 IQD/order holds across both cash and digital payments — **card/wallet orders do not weaken profit:**
- **SuperQi / Qi POS & app:** **0%** merchant fee under Qi's 2026 initiative → full **+1,115 IQD** (or **+1,315 IQD** because pre-paid orders eliminate the 200 IQD failed-delivery cost).
- **FIB QR in-app:** **0.3%** (~84 IQD on 28,000) vs. **~0 failed-delivery cost** (saves ~200 IQD) → net contribution **~+1,231 IQD** (higher than COD).
- **FIB / Qi online card gateway:** capped at **1%** by Central Bank of Iraq (~280 IQD on 28,000), offset by the ~200 IQD failed-delivery saving → **~+1,035 IQD** even if Cheapify absorbs the fee, or **+1,115 IQD** if passed to the seller of record. Across Iraq's 85–90% COD / 10–15% digital mix, blended contribution stays **≥ +1,115 IQD/order**.
- **Outgoing payout transfers:** FIB P2P transfer fee is **0.1%** (~24 IQD on a 24,050 IQD merchant payout; courier settled in weekly batches). *Operational rule:* always disburse merchant payouts via standard P2P/automated transfer (0.1%) or Qi (0%), never via FIB's corporate Bulk Payments portal, which charges a 25,000 IQD minimum fee per batch.

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

*Authoritative timeline: [`03_cash_flow_and_breakeven.md`](03_cash_flow_and_breakeven.md) §3–4 — the table below mirrors its **planned ramp**; `03` also carries the fast (2×) and slow (half-pace) scenarios.*

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

The **deepest cumulative cash hole**, computed month-by-month in `03`, includes startup costs and the two development months — it is not only operating losses:

| Scenario | Low point | ~USD | When | Of which operating losses after launch |
| :--- | :--- | :--- | :--- | :--- |
| Planned ramp (default) | −3.27M IQD | ~$2,180 | M3 | 1.15M (~$765) |
| Fast (2× ramp) | −2.70M IQD | ~$1,800 | M2 | 0.58M (~$386) |
| Slow (half the planned pace) | −4.12M IQD | ~$2,750 | M6 | 2.00M (~$1,332) |

Each low point = startup 1.70M + development months 0.42M + operating losses. The grant (`04`) funds the startup items (upgraded to the English trade name), the operating losses sized to the slow case, and the growth push — each part once (ADR-015). The founder funds the development months before the award.

---

## 8. Open Items Requiring Real-World Data

| Item | Needed input | Impact if wrong |
| :--- | :--- | :--- |
| ~~A1 courier cost~~ — **DONE** (Fast Delivery) | Contract signature + Zakho-tier confirm + 2nd quote | Contract worth ~500 IQD/order |
| A4 return rate | Pilot data | Variable-cost line doubles if ~8% |
| A8 ad CPM | $20 test campaign | Paid-CAC accuracy |
| A5 AOV | Social-seller price survey | All contribution math |
| ~~Legal/registration~~ — **DESK-VERIFIED** (~695k–1.295M IQD official fees) | Confirm lawyer filing fee at registration | Startup line bounded within $1,000 grant allocation |
| Lawyer + accountant appointment | KRI registration requires both — get quotes | The 75k/mo legal/accounting retainer (§4) may be low |
| Company capital (1M IQD minimum) | Confirm whether usable as working capital once registered | Funded as `04` line 3 |
| Platform fee on returned orders | Policy decision: is the 950 IQD fee kept or refunded on returns? | If refunded: 4% × 950 ≈ −38 IQD/order → contribution ~1,077, break-even ~605/mo |
| USD-billed tools at parallel rate | Pay by card at the official rate where possible | Up to ~+42k IQD/mo burn (§1.1) |
| Packaging/waybill print | Local print quotes | A12 + startup line |
| A9 merchant velocity | Pilot data | Month-3/6 scenario realism |
