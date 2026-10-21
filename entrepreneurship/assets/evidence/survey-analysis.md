# Market Validation Survey — Full Analysis

**Dataset:** [`market-validation-survey-oct2026.csv`](market-validation-survey-oct2026.csv) · 199 responses · collected Sep–Oct 2026 · trilingual form (EN / AR / KU-Badînî), one language block per respondent — blocks normalized, never double-counted.
**Analyzed:** Oct 20–21, 2026 · summary lives in [`../../05_market_validation_survey.md`](../../05_market_validation_survey.md) §7

---

## 1. Sample Structure

| Cohort | n | Share |
| :--- | :--- | :--- |
| **Shoppers** ("I mainly use social media to shop/buy") | **179** | 90% |
| **Merchants** ("sell products / manage a shop") | **20** | 10% |
| Arabic block | 168 | 84% |
| English block | 21 | 11% |
| Kurdish (Badînî) block | 10 | 5% |

**Bias flags:** Kurdish speakers are underrepresented vs. Duhok's Badînî-majority population — Kurdish-market conclusions are directional only. Merchants n=20 is adequate for signal, not for tight confidence intervals. Self-selected respondents (survey circulated in the founder's network) — expect favorable skew vs. cold population.

---

## 2. Shopper Findings (n=179)

### Q — Online shopping frequency

| Frequency | n | % |
| :--- | :--- | :--- |
| Rarely | 80 | 45% |
| A few times a month | 76 | 42% |
| Weekly | 19 | 11% |
| Never | 4 | 2% |

96% buy online at least occasionally — the addressable pool is the whole sample, not a niche.

### Q — Price-difference awareness (the problem signal)

| Response | n | % |
| :--- | :--- | :--- |
| **Yes — constantly, large gaps** | 70 | **39%** |
| Sometimes | 103 | 58% |
| Rarely / never noticed | 6 | 3% |

**97% notice price variation on identical items.** The core problem is visible to essentially everyone — and 4 in 10 see *large* gaps routinely.

### Q — Biggest annoyances (top-2 picks per shopper)

| Pain point (normalized across 3 languages) | n | % of shoppers |
| :--- | :--- | :--- |
| Untrusted sellers / duplicate pages clutter | ~92 | ~52% |
| "Found the same item cheaper right after buying" | ~84 | ~47% |
| "DM just to ask the price" + hours waiting | ~83 | ~46% |
| Delivery delays / disorganized manual ordering | ~48 | ~27% |

*Counts are normalized sums across language variants; ±1 rounding per merged option.*

### Q — "Would you use an app showing every local seller's price side-by-side?"

| Response | n | % |
| :--- | :--- | :--- |
| **Definitely yes / probably yes** | 157 | **88%** |
| Maybe — depends on delivery/speed | 18 | 10% |
| No — I prefer direct DMs | 4 | **2%** |

### Q — Early beta contact field — **contact-quality audit**

Raw count of non-empty fields: 74 (41% of shoppers). **Not all are usable:**

| Contact type | n | Notes |
| :--- | :--- | :--- |
| Phone / WhatsApp number | 38 | Real dialable numbers |
| Instagram handle / link | 14 | e.g., `gilan_hussein`, `h__anali`, IG profile URLs |
| Names / text without handle | ~8 | e.g., "Nazhan K. Hammo" — uncontactable as-is |
| Explicit refusals ("no"/"لا"/"No") | ~14 | Answered "no" in the contact field |
| **Actionable beta list** | **~52–60** | Phone + IG contacts; ~29–34% of shoppers |

### Cross-tabs (who wants it most?)

| Segment | App-intent "yes" rate |
| :--- | :--- |
| **Shoppers who *always* see price gaps (n=70)** | **93%** — the people who feel the pain most want it most |
| Sometimes-notice cohort (n=103) | 85% |
| Weekly shoppers (n=19) | 89% |
| Rare shoppers (n=80) | 89% — flat across frequency: demand isn't dependent on heavy users |

Intent is high *and* evenly distributed — the app isn't only for power shoppers.

---

## 3. Merchant Findings (n=20)

### Q — Current sales channels

| Channel mix | n |
| :--- | :--- |
| Instagram/Facebook page (alone or in combos) | **17 (85%)** |
| + Physical shop also | 5 |
| + TikTok | 4 |
| Other apps/marketplaces | 4 |
| Physical only | 1 |

Social-first sellers confirmed as the dominant supply type.

### Q — Biggest operational headache (top-2 picks)

| Pain point (normalized) | n | % of merchants |
| :--- | :--- | :--- |
| Hours answering "what's the price?" DMs from non-serious buyers | 11 | **55%** |
| Random competition & conflicting prices | 9 | 45% |
| High cost of building own website/app | 7 | 35% |
| Manually coordinating addresses & couriers via WhatsApp | 7 | 35% |

### Q — Would you join a unified-listing platform (no setup fee, competitor price alerts)?

| Response | n | % |
| :--- | :--- | :--- |
| Yes — very interested / definitely | 15 | **75%** |
| Maybe — depends on commission | 3 | 15% |
| No — satisfied with current setup | 2 | 10% |

*Commission-sensitivity is the only stated hesitation — reinforces keeping the effective take-rate visibly low.*

### Q — Pilot-shop signups — **contact-quality audit**

Raw non-empty entries: 13 (65%). **After dedup & noise filtering:**

| Status | Entries | Notes |
| :--- | :--- | :--- |
| **Valid merchant leads** | **~8–9** | Ello Store, Eillo Store, يوڤا شوب, عالم الأطفال (entered twice — counted once), اسم محل أنور, ar__design.1, +2 bare numbers |
| Explicit refusals | 3 | "لا" / "No" / "لا شكرا" |
| Non-lead message | 1 | "Good doing bro keep achieving" |

**Realistic pilot pipeline: ~8 merchants** — still inside the 5–10 Founder's Circle target, but thinner than the raw 13 suggested.

---

## 4. Language-Cohort View

| Cohort | Shoppers | App-intent yes | Beta contacts |
| :--- | :--- | :--- | :--- |
| Arabic (n=168) | 149 | 89% | 65 raw |
| English (n=21) | 20 | 80% | 6 |
| Kurdish (n=10) | 10 | 80% | 3 |

Demand holds across languages — no cohort shows resistance. Kurdish n=10 is too thin to conclude behavior; direction is positive.

---

## 5. What the Survey Proves vs. What It Doesn't

**Proven (with caveats above):**

- The problem is *seen* by ~97% of shoppers — no awareness-building needed
- Stated demand is overwhelming (88%) and flat across usage frequency
- Pain priorities are ranked: trust/clutter > post-purchase regret > DM tax > delivery delays
- Merchant pull exists: 75% interested, ~8 real pilot leads, social-first supply confirmed
- Only 2% are DM-loyal — the "people won't switch" objection is marginal

**Not proven:**

- Conversion (intent ≠ orders — concierge pilot decides)
- AOV, delivery-fee tolerance, COD preference — *not asked* in this instrument
- Kurdish-market behavior (thin sample)
- Daily-DM volumes (merchants' 50–100/day figure remains anecdotal)

**Corrections vs. first-pass reporting:** beta leads are ~52–60 actionable (not 74); pilot leads are ~8 valid merchants (not 13) after filtering refusals, text noise, and a duplicate entry.
