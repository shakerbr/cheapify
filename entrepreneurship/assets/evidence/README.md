# Cheapify — Field Evidence Archive & Master Analysis

Real-market screenshot evidence collected Sep–Oct 2026 supporting the problem claims in `01_problem_solution_value.md` and `02_market_opportunity_and_sizing.md` (§5.4). Each case folder contains the raw screenshots plus a per-screenshot extraction (`README.md` inside each folder).

---

## 1. Case Summary — Price Variation

| Case | Folder | Lowest | Highest | Spread | Date |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Anker A1695 Power Bank 25K/165W** — flagship | [`Anker-Power-Bank/`](Anker-Power-Bank/) | 90,000 IQD (IG) | **200,000 IQD (Miswag)** | **~110,000 IQD / 122%** | 2026-10-20 |
| ASUS VA24EHF 24" monitor | [`asus-monitor/`](asus-monitor/) | 116,721 IQD (Amal — *now defunct*) | 163,350 IQD (Miswag) | ~46,600 IQD / 40% | 2026-09-20 |
| Newal VAC-3510 vacuum | [`vaccum-cleaner-vac3510/`](vaccum-cleaner-vac3510/) | 95,000 IQD (IG) | 133,250 IQD (Miswag) | ~38,250 IQD / 40% | 2026-10-21 |
| Hoco HX80 coffee machine | [`portable-coffee-hx80/`](portable-coffee-hx80/) | 25,000 IQD (IG) | 35,280 IQD (Miswag) | ~10,280 IQD / 41% | 2026-10-21 |
| Xiaomi 165W/10K power bank | [`xiaomi-power-bank/`](xiaomi-power-bank/) | 60,000 IQD | 70,000 IQD | ~10,000 IQD / 17% — *same app* | 2026-09-20 |

**Spread holds at every price point:** ~17–122% regardless of ticket size, and it cuts *both* ways — social sellers undercut marketplaces on 2 of 5 cases. The problem is opacity, not any single channel being "expensive."

**Platform UI signatures** (for attributing future captures — filenames are not reliable):

| Platform | Visual markers |
| :--- | :--- |
| **Miswag** | Red accent; brand chip → title → "Seller Delivery"/"Free Delivery" → red `-%` badge beside strikethrough → Aqsat Mall installment row → red "Add to Cart" pill; search grids show seller-name chips + bottom nav (Home/Categories/Cart/Account) |
| **iBazzar** | Light UI; "Sort \| Filter" bar; blue "Free delivery" text; product page has "Found Cheaper? Tell us!", "Installment Available — 10 Months" row, photo counter, "Search Electronics" header |
| **Elryan** | White cards, category-header back nav, bilingual AR/EN titles, product-code chip (e.g. "MON9"), outline "Buy Now" + quantity stepper |
| **Amal** *(defunct)* | Purple theme; checkout stepper Cart→Delivery→Payment; "Sold By: Amal"; coupon field |
| **Instagram/social** | Native IG/TikTok post chrome — Follow button, caption text, action rail |

## 2. Hidden-Price Evidence ("DM for Price")

| Case | Folder | What it shows |
| :--- | :--- | :--- |
| LePresso 4-in-1 coffee maker (luzineiq) | [`no-price-dm-for-price/`](no-price-dm-for-price/) | Full specs, **no price** — "call to order"; a commenter asking "how much?" in-frame |
| De'Longhi Magnifica Evo (hotiqdeals) | [`no-price-dm-for-price/`](no-price-dm-for-price/) | Paid "DISCOUNT" ad — **still no price**; WhatsApp/DM ordering only |

## 3. Full Issue Catalog — Everything the Evidence Shows

Beyond price spread, the screenshots document **14 distinct market defects**:

| # | Issue | Where observed | Cheapify's answer |
| :--- | :--- | :--- | :--- |
| 1 | **Cross-channel price spread** — same SKU, radically different prices across IG/stores/marketplaces | All 5 product cases (17–122%) | Single-SKU master page with all offers side-by-side |
| 2 | **Intra-platform duplicate listings** — same SKU as disconnected listings *inside one marketplace* — **documented on TWO of the three live competitors** | Miswag Anker grid (100k vs 200k same page); iBazzar Xiaomi grid (60k vs 70k same page) | Exact-barcode + multi-signal dedup; one page per SKU, offers compete on it |
| 3 | **Prices entirely hidden** — "DM/call for price" | no-price-dm-for-price/ (both posts) | Price is a structured field, always shown |
| 4 | **Price ranges sold as prices** — seller quotes "90–120k" instead of a number | Anker / panomobi IG post | Exact offer price required at listing; variants priced individually |
| 5 | **Prices as unstructured prose** — numbers buried in caption text, unsearchable | All 4 Anker IG posts; vacuum IG; coffee IG | Structured price field + audit vs. social price (Rule 1) |
| 6 | **Fake discount anchoring** — inflated "was" prices manufacturing fake deals | Miswag vacuum "was 205k −35%"; coffee "was 42k −16%"; monitor "was 165k"; Anker "was 140k" | Real cross-seller comparison defeats anchoring — a fake markdown can't survive beside a cheaper real offer |
| 7 | **Seller identity obscured** — marketplace lists itself as seller | Miswag ASUS listing ("Sold by: Miswag") | Named verified merchants; reliability score per seller |
| 8 | **Inconsistent delivery bundling** — some IG prices include delivery, others don't; totals incomparable | Anker dream_1phone "incl. delivery" vs. unspecified others | Doorstep Total = item + zone fee, always separated, always shown |
| 9 | **Sparse review signal** — 5★ ratings on 1–4 reviews | Miswag Anker listings | Verified-purchase reviews only |
| 10 | **Thin/sloppy listings** — model-name-only, meaningless variant fields ("Size" on a coffee machine) | Miswag ASUS (no specs); Miswag HX80 ("Size" selector) | QA gate + shared-ownership improvements + spec autofill from barcode |
| 11 | **Slow delivery normalized** | iBazzar Anker: 48–72h stated | Same-day/hyperlocal SLA (1–3h target) |
| 12 | **Manual ordering only** — call/WhatsApp/DM required to transact | no-price-dm-for-price/ both; all IG sellers | In-app checkout, COD, no conversation needed |
| 13 | **AI-generated seller content** — marketing posted under "AI content" label | vacuum / ghadeer_3130 IG post | Verified sellers + real-photo media rules + QA |
| 14 | **Installment/BNPL pushed on inflated prices** | Miswag vacuum — "Aqsat Mall 10×15,783"; Miswag monitor — "Aqsat Mall 10×19,349"; iBazzar Anker — 10×16,221 | Transparent pricing removes the inflation BNPL feeds on |
| 15 | **Competitors admit the problem** — iBazzar's literal "Found Cheaper? Tell us!" feature: a manual plea for the comparison Cheapify automates | iBazzar Anker listing | Automated Best Value — no user reporting needed |

## 4. What the Evidence Proves (for the pitch)

1. **The problem is photographed, not hypothesized.** 6 cases, dated, with source/seller/price extracted — including a **122% spread** and a **2× gap inside one marketplace's own search page**.
2. **The failure is systemic, not one bad seller.** Different channels fail differently: Instagram hides prices behind DMs/ranges; marketplaces duplicate listings, anchor fake discounts, and obscure seller identity. Every channel's failure mode is documented.
3. **Even competitors confess — and die.** iBazzar ships a literal "Found Cheaper? Tell us!" button asking shoppers to report better prices manually; Amal — the platform that listed the cheapest monitor — has since shut down entirely. The market is broken enough to kill players, and nobody has fixed it structurally.
4. **The gap persists at every ticket size.** 17% on a 60k power bank, 40–41% on appliances, 122% on electronics — variation isn't a luxury-goods artifact.

## 5. Survey Dataset

| File | Contents |
| :--- | :--- |
| [`market-validation-survey-oct2026.csv`](market-validation-survey-oct2026.csv) | n=199 responses (179 shoppers / 20 merchants), trilingual EN/AR/KU — analyzed in `../../05_market_validation_survey.md` §7 |

---

**Bottom line for evaluators:** this archive is what "the market is broken" looks like in pixels — 122% spreads, hidden prices, fake discounts, duplicate listings, and a competitor's own feature begging users to fix the opacity manually.
