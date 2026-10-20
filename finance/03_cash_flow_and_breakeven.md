# Cheapify — Cash Flow Projection & Break-Even Analysis

## Month-by-Month Burn · Path to Self-Sustaining

**Pillar:** Finance Management (Pillar 3 — File 03)
**Status:** Assumption-Driven Model v1 — all inputs trace to [`01_operational_budget.md`](01_operational_budget.md) (A1–A12) and [`02_unit_economics.md`](02_unit_economics.md)
**Horizon:** 12 months — Phase A (2 mo dev/audience-building) → launch → pilot ramp (Months 1–10 post-launch)

---

## 1. Model Recap (Inputs)

| Input | Value | Source |
| :--- | :--- | :--- |
| **Dev-phase burn** (pre-launch) | ~210,000 IQD/mo (~$140) | §2 note — AI tools + SaaS + audience ads |
| **Operating burn** (post-launch) | 652,000 IQD (~$435); 790k from M6 | `01` §4 |
| Contribution per delivered order | ~+1,015 IQD | `01` §5.3 |
| Startup one-time | ~1.7M IQD | `01` §3 |
| Orders/mo ramp | planning (conservative) curve | §2 |
| Merchant ramp | 10 → 25 stores | §2 |

**Dev vs. operating burn:** the full 652k baseline only activates at launch — ads test budget, incentive pool, OTP signups, WhatsApp line, and Supabase Pro don't exist during development. Dev-phase burn ≈ **210k/mo**: AI assistant (90k) + tools/SaaS (30k) + modest audience-building ad boosts (75k — Phase A still needs some paid reach to build the waitlist; pure-organic assumed zero is unrealistic) + contingency (15k). Legal retainer deferred until registration work begins.

---

## 2. Volume Ramp Assumptions `[ASSUMPTION]`

**This is the planning scenario — deliberately conservative.** Cheapify captures only a share of each merchant's total volume (~10–30% early); aggressive targets live in the upside scenario (§4.1).

| Month | Orders (planning) | Merchants live | Basis |
| :--- | :--- | :--- | :--- |
| M-2, M-1 (Phase A) | 0 | 0 (10 recruiting) | Dev + waitlist building |
| M1 | 100 | 10 | Founding stores' first month — ~10 orders/store |
| M2 | 225 | 12 | Referrals + ads + 2nd cohort |
| M3 | 400 | 14 | Waitlist converts |
| M4 | 600 | 16 | Habit formation |
| M5 | 1,000 | 18 | Growth curve |
| M6 | 1,350 | 20 | |
| M7–M8 | 1,600–1,850 | 22–24 | |
| M9–M12 | ~2,000–2,100 | 25+ | Organic tail |

Note — *per-store load stays modest (~10–80 orders/mo), which is the honest expectation when the platform captures a slice of each merchant's DM-era volume, not all of it. Upside scenario doubles these figures — see §4.1.*

---

## 3. Monthly Cash Flow Table

IQD. Burn = 210k (Phase A) → 652k (launch→M5) → 790k (M6+, scale). Contribution = orders × ~1,015 (table products rounded at 1,025 for readability — delta <10k IQD/mo, immaterial).

| Month | Orders | Contribution | Burn | **Net cash flow** | Cumulative |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Startup | — | — | −1,700,000 | −1,700,000 | **−1,700,000** |
| M-2 | 0 | 0 | −210,000 | −210,000 | −1,910,000 |
| M-1 | 0 | 0 | −210,000 | −210,000 | **−2,120,000** ← launch day |
| M1 | 100 | +102,500 | −652,000 | −549,500 | −2,669,500 |
| M2 | 225 | +230,625 | −652,000 | −421,375 | −3,090,875 |
| M3 | 400 | +410,000 | −652,000 | −242,000 | −3,332,875 |
| M4 | 600 | +615,000 | −652,000 | −37,000 | **−3,369,875** ← trough |
| M5 | 1,000 | +1,025,000 | −652,000 | **+373,000** ← first green | −2,996,875 |
| M6 | 1,350 | +1,383,750 | −790,000 | +593,750 | −2,403,125 |
| M7 | 1,600 | +1,640,000 | −790,000 | +850,000 | −1,553,125 |
| M8 | 1,850 | +1,896,250 | −790,000 | +1,106,250 | −446,875 |
| **M9** | 2,000 | +2,050,000 | −790,000 | +1,260,000 | **+813,125** ← all-loss recovered |
| M10–12 | ~2,100 | ~+2,152,500 | −790,000 | +1.36M/mo | → ~+5M |

---

## 4. The Three Milestones

| Milestone | Month | What it means |
| :--- | :--- | :--- |
| **Cash-flow positive** | **M5** (~1,000 orders/mo) | Cheapify covers its own monthly burn — losses stop growing |
| **Peak loss** | **M4** (cumulative −3,369,875) | Deepest hole: ~3.37M IQD (~$2,250) total invested before recovery |
| **Full recovery** | **M9** (~2,000 orders/mo) | Cumulative cash positive — all losses paid back |

---

## 4.1 Upside Scenario — Target Ramp `[STRETCH CASE]`

The aggressive curve — assumes founding merchants push hard and Cheapify captures a larger share of their volume faster than planned (~2× the planning ramp):

| Month | Orders (upside) | Net cash flow | Cumulative |
| :--- | :--- | :--- | :--- |
| Startup → M-1 | 0 | −1,910,000 total | −2,120,000 at launch |
| M1 | 200 | −447,000 | −2,567,000 |
| M2 | 450 | −190,750 | **−2,757,750** ← trough |
| M3 | 800 | **+168,000** ← first green | −2,589,750 |
| M4 | 1,200 | +578,000 | −2,011,750 |
| M5 | 2,000 | +1,398,000 | −613,750 |
| **M6** | 2,700 | +1,977,500 | **+1,363,750** ← recovery |
| M7–M8 | 3,200–3,700 | +2.5–3.0M/mo | +3.85M → +6.86M |
| M9–M12 | 3,700–4,200 | +3.0–3.5M/mo | → +18M+ |

Planning vs. upside:

| Milestone | Planning ramp | Upside (2×) ramp | Delta |
| :--- | :--- | :--- | :--- |
| Cash-flow positive | M5 | M3 | −2 mo |
| Peak loss | −3.37M (~$2,250) | −2.76M (~$1,840) | −610k IQD |
| Full recovery | ~M9 | M6 | −3 mo |

**Read:** the plan is sized for the planning ramp; upside only accelerates the milestones by ~2–3 months and saves ~$400. Bounded difference either way — that's what "low-risk envelope" means.*

---

## 4.2 Slow-Adoption Floor — ~25% Ramp `[WORST CASE]`

The floor case: orders crawl. ~5 orders/store at launch, adoption stays weak:

| Month | Orders (floor) | Net cash flow | Cumulative |
| :--- | :--- | :--- | :--- |
| M1 | 50 | −600,750 | −2,720,750 |
| M2 | 115 | −534,125 | −3,254,875 |
| M3 | 200 | −447,000 | −3,701,875 |
| M4 | 300 | −344,500 | −4,046,375 |
| M5 | 500 | −139,500 | −4,185,875 |
| M6 | 675 | −98,125 | **−4,284,000** ← trough |
| M7 | 800 | **+30,000** ← first green | −4,254,000 |
| M8 | 925 | +158,125 | −4,095,875 |
| M9+ | ~1,000 | +235,000/mo | −3,860,875 → recovery ~M20+ |

*(Note: the M6 burn bump to 790k raises the break-even threshold from ~642 to ~771 orders/mo — which is why floor-ramp positivity lands at M7, not earlier.)*

**Read:** even at a crawl the venture doesn't hit a failure cliff — it degrades to a slow grind: peak hole ~4.28M IQD (~$2,850), losses stop growing at M7, recovery stretches past M20. The monthly loss is always capped by burn (~$435–525/mo), never by an order-volume cliff. **If the floor case is what reality looks like, the concierge pilot (§6.1) reveals it for ~30–50k IQD — before scale, not after.**

---

## 5. Break-Even Analysis

```
Monthly break-even = Operating burn ÷ Contribution/order
                   = 652,000 ÷ ~1,015
                   = ~642 orders/month  (~21 orders/day)
```

**Important honesty note:** ~642 orders is total platform volume, not per-store. It means ~4 top merchants at full velocity, ~10 decent ones, or all 20+ at half-throttle. The pilot target of 150 orders/store/mo is aggressive; the realistic path is more stores at moderate velocity.

### Sensitivity — break-even under different assumptions

| If... | Contribution/order | Break-even orders/mo |
| :--- | :--- | :--- |
| Baseline | ~+1,015 | ~642 |
| Courier at list price (no contract) = 3,000 | +525 | ~1,240 |
| AOV drops to 20,000 | +725 | ~900 |
| Incentives run 2× hot | +725 | ~900 |
| Surroundings charged flat city fee instead of zone fees | −500 to −1,500/order on those orders | **Zone fees required — see policies §2** |

### 5.1 Levers to lower break-even — `[OPTIONS — not adopted]`

Ways to pull break-even down if needed. Recorded as options only — none applied to the model.

| Lever | Effect | New break-even | Tradeoff |
| :--- | :--- | :--- | :--- |
| Commission 3.8% → 4.5% (still ≪ 10–15% incumbents) | Contribution → ~1,200 | ~540/mo | Slightly dulls the sharpest pitch to merchants — revisit at Phase 2, not now |
| Trim operating burn → ~520k (smaller ads test, tighter incentive cap) | — | ~480/mo combined w/ 4.5% | Slower growth inputs |
| Non-order revenue (merchant featured placements, Phase 2) | +100k/mo | ~350/mo combined | Post-pilot only; don't build model on it |
| **Preferred lever: order velocity** | — | unchanged | Positive contribution means more orders always help — grow via founding stores' bio-link audiences at ~zero CAC rather than restructuring fees |

**Why none adopted:** with positive unit economics the model doesn't need a lower break-even — it needs the volume curve to be real. Fee hikes are kept in reserve; burn trims would slow the very acquisition that makes the curve real.

---

## 6. What the Cash Flow Actually Says

1. **The courier number is now real** — Fast Delivery: 2,500/3,500/4,500 contract rates vs. 3,000/4,000/5,000 zone fees → +500 margin uniform across zones, *but only once the contract is signed* (unsigned: margin 0 in-city, break-even ~1,240/mo). Registration → contract → margin is now a critical path.
2. **Peak funding need ~3.37M IQD (~$2,250)** under the planning ramp — ~2.76M (~$1,840) if the upside case lands.
3. **Cash-positive in Month 5** — deliberately un-aggressive; if traction beats the plan it arrives M3 (§4.1).
4. **Recovery by ~M9** — under the planning curve; upside pulls it to M6.
5. **The real risk isn't the math — it's the volume curve.** The planning ramp already assumes only ~10–80 platform orders/merchant/mo (a slice of merchant volume, not all of it); the floor case (§4.2) shows even a ~5-order/store crawl degrades to a slow grind (~$2,850 peak), not a cliff. The true question — "can 20 stores each route ~1 order/day through the app?" — is what the concierge pilot (§6.1) answers cheaply, before scale.

### 6.1 Validation Experiments — How to De-Risk Before Scaling `[ACTION ITEMS]`

Documents can't reduce traction risk — only real-world tests can. Three cheap experiments convert the biggest assumptions into data:

| Experiment | Cost | What it proves |
| :--- | :--- | :--- |
| ~~**Courier quote**~~ — **DONE**: Fast Delivery 2,500/3,500/4,500 contracted | ~0 | Was the #1 unknown — now verified pending signature |
| **Concierge pilot** — manually run 10–20 real orders before building the app: founding merchant posts products, you coordinate order + delivery by hand | ~30–50k IQD | Real AOV, real courier cost, real shopper willingness — replaces A1/A4/A5/A6 with data |
| **Merchant audience audit** — ask the 10 founding stores their follower counts + engagement rates | ~0 | Measures the actual bio-link traffic pool = the true order source driving §2's ramp |

**Rule:** run these before treating any projection above as more than an envelope. The finance docs' job is to size the bet; these tests decide whether the bet is real.

---

## 7. Open Items Requiring Real-World Data

| Item | Needed input | Moves |
| :--- | :--- | :--- |
| ~~Courier cost (A1)~~ — done (Fast Delivery) | Contract signature | Contribution/order, break-even |
| Order ramp | Waitlist seeded: 74 shopper + 13 merchant contacts (survey n=199, Oct 2026) — conversion rate still unproven until launch | Whole cash curve |
| AOV | Seller price survey | Contribution/order |
| Return/failed-delivery rates | Pilot data | Variable-cost line |
| Merchant velocity (A9) | n=1 interview: ~30/mo total | Orders ramp realism — more interviews |
| Phase A ad efficiency | First boosted-post CPC/CPM data | Dev-burn realism |

**Bottom line:** peak exposure ranges ~2.76M–4.28M IQD (~$1,840–2,850) from upside to floor ramp — bounded and survivable at every speed, because the loss ceiling is burn (~$435/mo), not order volume. The venture's risk is **traction, not cash**, and the §6.1 experiments are the only real de-risking lever: they convert assumptions into data before scale. Everything else is tuning.
