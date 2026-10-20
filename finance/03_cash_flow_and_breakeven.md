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
| Contribution per delivered order | +1,025 IQD | `01` §5.3 |
| Startup one-time | ~1.7M IQD | `01` §3 |
| Orders/mo ramp | pilot assumption curve | §2 |
| Merchant ramp | 10 → 30 stores (faster curve) | §2 |

**Dev vs. operating burn:** the full 652k baseline only activates at launch — ads test budget, incentive pool, OTP signups, WhatsApp line, and Supabase Pro don't exist during development. Dev-phase burn ≈ **210k/mo**: AI assistant (90k) + tools/SaaS (30k) + modest audience-building ad boosts (75k — Phase A still needs some paid reach to build the waitlist; pure-organic assumed zero is unrealistic) + contingency (15k). Legal retainer deferred until registration work begins.

---

## 2. Volume Ramp Assumptions `[ASSUMPTION]`

Faster merchant curve than v0 — recruitment pushes harder post-launch; order ramp nudged up on the larger store base:

| Month | Orders | Merchants live | Basis |
| :--- | :--- | :--- | :--- |
| M-2, M-1 (Phase A) | 0 | 0 (10 recruiting) | Dev + waitlist building |
| M1 | 200 | 10 | Founding stores' first month |
| M2 | 450 | 15 | Referrals + ads + 2nd cohort |
| M3 | 800 | 18 | Waitlist converts |
| M4 | 1,200 | 20 | Habit formation |
| M5 | 2,000 | 22 | Growth curve |
| M6 | 2,700 | 25 | Approaching pilot target |
| M7–M8 | 3,200–3,700 | 28–30 | Pilot target territory |
| M9–M12 | 3,700–4,200 | 30+ | Organic tail |

Note — *merchant count grows ~2–3 stores/mo after the founding cohort; more realistic if recruitment is active, not passive.*

---

## 3. Monthly Cash Flow Table

IQD. Burn = 210k (Phase A) → 652k (launch→M5) → 790k (M6+, scale). Contribution = orders × 1,025.

| Month | Orders | Contribution | Burn | **Net cash flow** | Cumulative |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Startup | — | — | −1,700,000 | −1,700,000 | **−1,700,000** |
| M-2 | 0 | 0 | −210,000 | −210,000 | −1,910,000 |
| M-1 | 0 | 0 | −210,000 | −210,000 | **−2,120,000** ← launch day |
| M1 | 200 | +205,000 | −652,000 | −447,000 | −2,567,000 |
| M2 | 450 | +461,250 | −652,000 | −190,750 | **−2,757,750** ← trough |
| M3 | 800 | +820,000 | −652,000 | **+168,000** ← first green | −2,589,750 |
| M4 | 1,200 | +1,230,000 | −652,000 | +578,000 | −2,011,750 |
| M5 | 2,000 | +2,050,000 | −652,000 | +1,398,000 | −613,750 |
| **M6** | 2,700 | +2,767,500 | −790,000 | +1,977,500 | **+1,363,750** ← all-loss recovered |
| M7 | 3,200 | +3,280,000 | −790,000 | +2,490,000 | +3,853,750 |
| M8 | 3,700 | +3,792,500 | −790,000 | +3,002,500 | +6,856,250 |
| M9–12 | 3,700–4,200 | ~+3.8–4.3M | −790,000 | +3.0–3.5M/mo | → +18M+ |

---

## 4. The Three Milestones

| Milestone | Month | What it means |
| :--- | :--- | :--- |
| **Cash-flow positive** | **M3** (~800 orders/mo) | Cheapify covers its own monthly burn — losses stop growing |
| **Peak loss** | **M2** (cumulative −2,757,750) | Deepest hole: ~2.76M IQD total invested before recovery — earlier and shallower than v0's 3.7M because dev months don't pay operating burn |
| **Full recovery** | **M6** (~2,700 orders/mo) | Cumulative cash positive — all losses paid back, one month sooner on the faster merchant ramp |

---

## 4.1 Conservative Scenario — 50% of Ramp `[STRESS TEST]`

The base curve assumes founding merchants bring their full order flow to Cheapify. In reality Cheapify captures a share of each merchant's volume (~10–30% early), so this scenario runs **half the order ramp** — the more likely near-term outcome:

| Month | Orders (50%) | Net cash flow | Cumulative |
| :--- | :--- | :--- | :--- |
| Startup → M-1 | 0 | −1,910,000 total | −2,120,000 at launch |
| M1 | 100 | −549,500 | −2,669,500 |
| M2 | 225 | −421,375 | −3,090,875 |
| M3 | 400 | −242,000 | −3,332,875 |
| M4 | 600 | −37,000 | **−3,369,875** ← trough |
| M5 | 1,000 | **+373,000** ← first green | −2,996,875 |
| M6 | 1,350 | +593,750 | −2,403,125 |
| M7 | 1,600 | +850,000 | −1,553,125 |
| M8 | 1,850 | +1,106,250 | −446,875 |
| **M9** | 2,000 | +1,260,000 | **+813,125** ← recovery |

Base vs. conservative:

| Milestone | Base ramp | 50% ramp | Delta |
| :--- | :--- | :--- | :--- |
| Cash-flow positive | M3 | M5 | +2 mo |
| Peak loss | −2.76M (~$1,840) | −3.37M (~$2,250) | +610k IQD |
| Full recovery | M6 | ~M9 | +3 mo |

**Read:** even at half the ramp the venture survives — the downside costs ~$400 more and ~3 months later recovery. The financial risk is bounded; the model doesn't collapse, it just slides right.

---

## 5. Break-Even Analysis

```
Monthly break-even = Operating burn ÷ Contribution/order
                   = 652,000 ÷ 1,025
                   = ~636 orders/month  (~21 orders/day)
```

**Important honesty note:** ~636 orders is total platform volume, not per-store. It means ~4 top merchants at full velocity, ~10 decent ones, or all 20+ at half-throttle. The pilot target of 150 orders/store/mo is aggressive; the realistic path is more stores at moderate velocity.

### Sensitivity — break-even under different assumptions

| If... | Contribution/order | Break-even orders/mo |
| :--- | :--- | :--- |
| Baseline | +1,025 | ~636 |
| Courier A1 = 3,000 (no delivery margin) | +525 | ~1,240 |
| AOV drops to 20,000 | +725 | ~900 |
| Incentives run 2× hot | +725 | ~900 |
| Courier A1 = 3,500 (margin gone) | −75 | **Never — loses money per order** |

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

1. **The model is fragile on ONE number** — the courier cost. Everything else is second-order. If A1 lands at ≤3,000, the projection holds; at 3,500+, per-order economics go negative and volume makes it *worse*, not better.
2. **Peak funding need ~2.76M IQD (~$1,840)** — shallower than v0 because dev months burn ~210k, not 652k.
3. **Cash-positive in Month 3** — if the ramp holds; at half the curve, positivity slides to ~M5 but doesn't break the model.
4. **Recovery by M6** — under the faster merchant curve; a slower ramp pushes recovery to M8–9.
5. **The real risk isn't the math — it's the volume curve.** ~90–130 orders/merchant/month across the early cohort assumes Cheapify captures a large share of merchant volume; at 10–30% capture the 50% scenario (§4.1) is the realistic near-term path — and it still recovers by ~M9.

### 6.1 Validation Experiments — How to De-Risk Before Scaling `[ACTION ITEMS]`

Documents can't reduce traction risk — only real-world tests can. Three cheap experiments convert the biggest assumptions into data:

| Experiment | Cost | What it proves |
| :--- | :--- | :--- |
| **Courier quote** (call ZMC/local couriers for intra-Duhok + inter-city rates) | ~0 | Kills the #1 unknown — the single number that can break the model |
| **Concierge pilot** — manually run 10–20 real orders before building the app: founding merchant posts products, you coordinate order + delivery by hand | ~30–50k IQD | Real AOV, real courier cost, real shopper willingness — replaces A1/A4/A5/A6 with data |
| **Merchant audience audit** — ask the 10 founding stores their follower counts + engagement rates | ~0 | Measures the actual bio-link traffic pool = the true order source driving §2's ramp |

**Rule:** run these before treating any projection above as more than an envelope. The finance docs' job is to size the bet; these tests decide whether the bet is real.

---

## 7. Open Items Requiring Real-World Data

| Item | Needed input | Moves |
| :--- | :--- | :--- |
| Courier cost (A1) | ZMC/local quote | Contribution/order, break-even |
| Order ramp | Waitlist conversion + launch data | Whole cash curve |
| AOV | Seller price survey | Contribution/order |
| Return/failed-delivery rates | Pilot data | Variable-cost line |
| Merchant velocity (A9) | First-90-day data | Orders ramp realism |
| Phase A ad efficiency | First boosted-post CPC/CPM data | Dev-burn realism |

**Bottom line:** peak exposure is ~2.76–3.37M IQD (~$1,840–2,250) across base and 50%-ramp scenarios — bounded and survivable either way. The venture's risk is **traction, not cash**, and the §6.1 experiments are the only real de-risking lever: they convert assumptions into data before scale. Everything else is tuning.
