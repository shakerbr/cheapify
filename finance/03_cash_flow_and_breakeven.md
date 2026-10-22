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
| Contribution per delivered order | ~+1,115 IQD | `01` §5.3 (corrected — ADR-014) |
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

IQD. Burn = 210k (Phase A) → 652k (launch→M5) → 790k (M6+, scale). Contribution = orders × ~1,115.

| Month | Orders | Contribution | Burn | **Net cash flow** | Cumulative |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Startup | — | — | −1,700,000 | −1,700,000 | **−1,700,000** |
| M-2 | 0 | 0 | −210,000 | −210,000 | −1,910,000 |
| M-1 | 0 | 0 | −210,000 | −210,000 | **−2,120,000** ← launch day |
| M1 | 100 | +111,500 | −652,000 | −540,500 | −2,660,500 |
| M2 | 225 | +250,875 | −652,000 | −401,125 | −3,061,625 |
| M3 | 400 | +446,000 | −652,000 | −206,000 | **−3,267,625** ← trough |
| M4 | 600 | +669,000 | −652,000 | **+17,000** ← first green (break-even) | −3,250,625 |
| M5 | 1,000 | +1,115,000 | −652,000 | +463,000 | −2,787,625 |
| M6 | 1,350 | +1,505,250 | −790,000 | +715,250 | −2,072,375 |
| M7 | 1,600 | +1,784,000 | −790,000 | +994,000 | −1,078,375 |
| **M8** | 1,850 | +2,062,750 | −790,000 | +1,272,750 | **+194,375** ← all-loss recovered |
| M9 | 2,000 | +2,230,000 | −790,000 | +1,440,000 | +1,634,375 |
| M10–12 | ~2,100 | ~+2,341,500 | −790,000 | +1.55M/mo | → ~+6.3M |

---

## 4. The Three Milestones

| Milestone | Month | What it means |
| :--- | :--- | :--- |
| **Cash-flow positive** | **M4** (~600 orders/mo, just above the ~585 break-even; M5 is the first clearly positive month) | Cheapify covers its own monthly burn — losses stop growing |
| **Peak loss** | **M3** (cumulative −3,267,625) | Deepest hole: ~3.27M IQD (~$2,180) total invested before recovery |
| **Full recovery** | **M8** (~1,850 orders/mo) | Cumulative cash positive — all losses paid back |

---

## 4.1 Upside Scenario — Target Ramp `[STRETCH CASE]`

The aggressive curve — assumes founding merchants push hard and Cheapify captures a larger share of their volume faster than planned (~2× the planning ramp):

| Month | Orders (upside) | Net cash flow | Cumulative |
| :--- | :--- | :--- | :--- |
| Startup → M-1 | 0 | −2,120,000 total | −2,120,000 at launch |
| M1 | 200 | −429,000 | −2,549,000 |
| M2 | 450 | −150,250 | **−2,699,250** ← trough |
| M3 | 800 | **+240,000** ← first green | −2,459,250 |
| M4 | 1,200 | +686,000 | −1,773,250 |
| M5 | 2,000 | +1,578,000 | −195,250 |
| **M6** | 2,700 | +2,220,500 | **+2,025,250** ← recovery |
| M7–M8 | 3,200–3,700 | +2.8–3.3M/mo | +4.80M → +8.14M |
| M9–M12 | 3,700–4,200 | +3.3–3.9M/mo | → +20M+ |

Planning vs. upside:

| Milestone | Planning ramp | Upside (2×) ramp | Delta |
| :--- | :--- | :--- | :--- |
| Cash-flow positive | M4 | M3 | −1 mo |
| Peak loss | −3.27M (~$2,180) | −2.70M (~$1,800) | −570k IQD |
| Full recovery | ~M8 | M6 | −2 mo |

**Read:** the plan is sized for the planning ramp; upside only accelerates the milestones by ~1–2 months and saves ~$380. Bounded difference either way — that's what "low-risk envelope" means.*

---

## 4.2 Slow-Adoption Floor — ~25% Ramp `[WORST CASE]`

The floor case: orders crawl. ~5 orders/store at launch, adoption stays weak:

| Month | Orders (floor) | Net cash flow | Cumulative |
| :--- | :--- | :--- | :--- |
| M1 | 50 | −596,250 | −2,716,250 |
| M2 | 115 | −523,775 | −3,240,025 |
| M3 | 200 | −429,000 | −3,669,025 |
| M4 | 300 | −317,500 | −3,986,525 |
| M5 | 500 | −94,500 | −4,081,025 |
| M6 | 675 | −37,375 | **−4,118,400** ← trough |
| M7 | 800 | **+102,000** ← first green | −4,016,400 |
| M8 | 925 | +241,375 | −3,775,025 |
| M9+ | ~1,000 | +325,000/mo | −3,450,025 → recovery ~M20 |

*(Note: the M6 burn bump to 790k raises the break-even threshold from ~585 to ~709 orders/mo — which is why floor-ramp positivity lands at M7, not earlier.)*

**Read:** even at a crawl the venture doesn't hit a failure cliff — it degrades to a slow grind: peak hole ~4.12M IQD (~$2,750), losses stop growing at M7, recovery ~M20. The monthly loss is always capped by burn (~$435–525/mo), never by an order-volume cliff. **If the floor case is what reality looks like, the concierge pilot (§6.1) reveals it for ~30–50k IQD — before scale, not after.**

---

## 5. Break-Even Analysis

```
Monthly break-even = Operating burn ÷ Contribution/order
                   = 652,000 ÷ ~1,115
                   = ~585 orders/month  (~20 orders/day)
```

**Important honesty note:** ~585 orders is total platform volume, not per-store. It means ~4 top merchants at full velocity, ~10 decent ones, or all 20+ at half-throttle. The pilot target of 150 orders/store/mo is aggressive; the realistic path is more stores at moderate velocity.

### Sensitivity — break-even under different assumptions

| If... | Contribution/order | Break-even orders/mo |
| :--- | :--- | :--- |
| Baseline | ~+1,115 | ~585 |
| Courier at list price (no contract) = 3,000 | +615 | ~1,060 |
| AOV drops to 20,000 | +965 | ~676 |
| Incentive pool doubled (450k/mo) | +1,115 (burn 877k) | ~787 |
| Surroundings charged flat city fee instead of zone fees | −500 to −1,500/order on those orders | **Zone fees required — see policies §2** |

### 5.1 Levers to lower break-even — `[OPTIONS — not adopted]`

Ways to pull break-even down if needed. Recorded as options only — none applied to the model.

| Lever | Effect | New break-even | Tradeoff |
| :--- | :--- | :--- | :--- |
| Commission 3.8% → 4.5% (still ≪ 10–15% incumbents) | Contribution → ~1,290 | ~505/mo | Slightly dulls the sharpest pitch to merchants — revisit at Phase 2, not now |
| Trim operating burn → ~520k (smaller ads test, tighter incentive cap) | — | ~405/mo combined w/ 4.5% | Slower growth inputs |
| Non-order revenue (merchant featured placements, Phase 2) | +100k/mo | ~325/mo combined | Post-pilot only; don't build model on it |
| **Preferred lever: order velocity** | — | unchanged | Positive contribution means more orders always help — grow via founding stores' bio-link audiences at ~zero CAC rather than restructuring fees |

**Why none adopted:** with positive unit economics the model doesn't need a lower break-even — it needs the volume curve to be real. Fee hikes are kept in reserve; burn trims would slow the very acquisition that makes the curve real.

---

## 6. What the Cash Flow Actually Says

1. **The courier number is now real** — Fast Delivery: 2,500/3,500/4,500 contract rates vs. 3,000/4,000/5,000 zone fees → +500 margin uniform across zones, *but only once the contract is signed* (unsigned: margin 0 in-city, break-even ~1,060/mo). Registration → contract → margin is now a critical path.
2. **Peak funding need ~3.27M IQD (~$2,180)** under the planning ramp — ~2.70M (~$1,800) if the upside case lands.
3. **Cash-positive in Month 4** (break-even; clearly positive from M5) — deliberately un-aggressive; if traction beats the plan it arrives M3 (§4.1).
4. **Recovery by ~M8** — under the planning curve; upside pulls it to M6.
5. **The real risk isn't the math — it's the volume curve.** The planning ramp already assumes only ~10–80 platform orders/merchant/mo (a slice of merchant volume, not all of it); the floor case (§4.2) shows even a ~5-order/store crawl degrades to a slow grind (~$2,750 peak), not a cliff. The true question — "can 20 stores each route ~1 order/day through the app?" — is what the concierge pilot (§6.1) answers cheaply, before scale.

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
| Order ramp | Waitlist seeded: ~52 actionable shopper + ~8 merchant leads (survey n=199, Oct 2026, quality-audited) — conversion rate still unproven until launch | Whole cash curve |
| AOV | Seller price survey | Contribution/order |
| Return/failed-delivery rates | Pilot data | Variable-cost line |
| Merchant velocity (A9) | n=1 interview: ~30/mo total | Orders ramp realism — more interviews |
| Phase A ad efficiency | First boosted-post CPC/CPM data | Dev-burn realism |

**Bottom line:** peak exposure ranges ~2.70M–4.12M IQD (~$1,800–2,750) from upside to floor ramp — bounded and survivable at every speed, because the loss ceiling is burn (~$435/mo), not order volume. The venture's risk is **traction, not cash**, and the §6.1 experiments are the only real de-risking lever: they convert assumptions into data before scale. Everything else is tuning.
