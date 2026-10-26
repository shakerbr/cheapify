# Cheapify Deck — v2 Change Spec (lead-authored, authoritative)

Applies on top of `deck-spec-v1.md`. Everything not mentioned here stays as
built. All text/numbers below are final — implement verbatim; if impossible, stop and report.

## 0. Canonical payment model (founder decisions, Oct 2026)

Use these statements as the single source of truth in docs and deck.

- P1. Shoppers pay **cash on delivery** from launch. **Card / e-wallet** payment (local
  gateway: e.g. FIB, FastPay, Qi Card, Visa/Mastercard) is added **shortly after launch**,
  once the payment-gateway account is approved (requires business registration). Cash on
  delivery is never removed.
- P2. **Cheapify never collects or handles cash.** All money between Cheapify and businesses
  (merchants, couriers, partners) moves electronically.
- P3. Cash orders: the **courier collects the cash** at delivery and **transfers the full
  collected amount electronically to Cheapify** within the deadline set in the courier
  contract (target: within 24 hours of delivery — `[TO CONFIRM AT CONTRACT SIGNING]`).
- P4. Card orders: the shopper's payment goes **to Cheapify's payment account at checkout**.
- P5. Split: Cheapify keeps its fee + delivery margin, pays the courier its contracted rate
  electronically (on the contract's payment cycle), and pays the merchant item price minus fee.
- P6. **Merchant payout is automatic and electronic, once the 48-hour return window after
  delivery closes** (for cash orders, also after the courier's transfer has arrived). Any
  refund raised inside the window is deducted before payout. No weekly/Sunday cycle.
- P7. **Every merchant must link a payment account** (bank card or e-wallet) to their
  Cheapify account during onboarding — required to receive payouts and to settle amounts
  owed after payout (e.g. a fault-return courier leg).
- P8. Refunds: card orders → back to the original card/e-wallet. Cash orders → change of
  mind: Cheapify credit; faulty item: electronic transfer to the shopper's card/e-wallet, or
  — if the shopper has none — cash handed back by the courier at return pickup and netted
  from the courier's next transfer `[TO CONFIRM AT CONTRACT SIGNING]`.
- P9. Card processing fees: **not yet quoted** `[OPEN — gateway quote needed]`. The
  +1,115 IQD/order contribution is the cash-on-delivery case; do not invent a card-fee number.

## 1. Verified Duhok figures (lead-checked)

- 2024 national census (Iraqi Ministry of Planning; reported by Peregraf and
  citypopulation.de): Iraq 46,118,793; Duhok governorate 1,599,871 (80% urban);
  districts: Duhok 497,029 · Zakho 398,876 · Semel 166,319 → launch area
  (Duhok + Semel + Zakho) **1,062,224 ≈ 1.06M**.
- Iraq internet users 39.6M, 83.8% (DataReportal, Digital 2026: Iraq, data late 2025).
- Iraq e-commerce revenue US$1,317M in 2025 (ECDB).
- Estimates (population-share method, label "estimate" everywhere):
  - Duhok governorate internet users ≈ 1,599,871 × 83.8% ≈ **1.34M**; launch area ≈ 1,062,224 × 83.8% ≈ **0.89M**.
  - Duhok governorate e-commerce ≈ 3.47% × $1,317M ≈ **$46M/yr**; launch area ≈ 2.30% × $1,317M ≈ **$30M/yr**.
  - Break-even share of launch-area e-commerce: 585 orders × 25,000 IQD = 14.625M IQD/mo = $9,750/mo = $117,000/yr ≈ **0.4%** of ≈$30M.

## 2. Global animation speed change

- Any sequence of 4+ similar items (dots, chaos cards, rows, segments, chart pieces, slices,
  legend rows, marks): per-item effect 150 ms, stagger 25 ms.
- Sequences of 2–3 items: per-item 250 ms, stagger 80 ms.
- Single effects: Fade 300 ms, Zoom 300 ms. Exits: 250 ms.
- Slide 2 dots, slide 4 chaos cards/rows, slide 11 line segments must each finish in < 1 s.

## 3. Slide changes (main deck becomes 15 slides; appendix becomes 8)

New order: 1 Cover · 2 Problem · 3 Problem·evidence · 4 Solution · 5 Value proposition ·
6 Target market (Duhok in numbers) · 7 Target customers (who we serve) · 8 Product ·
9 Business model · 10 Competitor analysis · 11 Growth strategy · 12 Financial feasibility ·
13 Funding · 14 What now · 15 Thank you · A1–A8.

### Slide 3 — card 3 replaced

- New asset `ev-vacuum-fakedeal.jpg`: side-by-side composite, light gap, from
  `vaccum-cleaner-vac3510/`: left = Instagram ad image only (`Screenshot_20261021_120338_Instagram.jpg`,
  the ad with the "95,000 IQD" badge; exclude handle/caption); right = Miswag price block
  (`Screenshot_20261021_120334_Miswag.jpg`: product photo + "133,250 IQD", struck "205,000 IQD",
  "−35%"). Rings: the 95,000 badge; the 133,250 / 205,000 / −35% block.
- Title: "A fake “deal”". Sub: "Same Newal vacuum: 95,000 on Instagram · “−35%” at 133,250 on Miswag".
- Drop `ev-ibazzar-foundcheaper.jpg` from the deck (keep the file).
- Notes: replace the third sentence with:
  "[click] And a marketplace shows a vacuum as a 35 percent “deal” at 133,250 — while an Instagram page sells the same model for 95,000."

### Slide 5 — Value proposition

- Shopper row 3: phrase "Cash on delivery or card" / sub "Doorstep total shown upfront".
- Merchant row 2: sub "Stock, orders and payouts in one place".
- Notes: "For shoppers: [click] every price side by side, an order in thirty seconds, and cash on delivery — or card. For merchants: [click] real orders instead of “price?” messages, a free dashboard for stock and payouts, and a fair fee — about 3.8 percent on a typical order."

### Slide 6 — Target market: Duhok in numbers (replaces old slide 6)

Label "Target market". Headline "Duhok first: about 1 million people."

Main visual: three side-by-side columns (cards), narrowing left→right in visual weight,
x 0.79 – 12.54, y 2.70 – 5.75. Column headers: "Iraq" · "Duhok governorate" ·
"Launch area: Duhok · Semel · Zakho" (launch-area card highlighted: BLUE12 fill + BLUE
1.5 pt border). Three rows inside each card; each value = big number (Comfortaa Bold) +
row label (Inter 12 pt INK60) + small source tag pill (Inter 9 pt: "census" / "published" /
"estimate"; estimate tags in ORANGE-outline, others NEUTRAL):

| Row | Iraq | Duhok governorate | Launch area |
| :--- | :--- | :--- | :--- |
| People | 46.1M (census) | 1.60M (census) | 1.06M (census) |
| Internet users | 39.6M (published) | ≈ 1.34M (estimate) | ≈ 0.89M (estimate) |
| Online shopping / year | $1.32B (published) | ≈ $46M (estimate) | ≈ $30M (estimate) |

Under the cards (y 5.90 – 6.40), Inter Bold 14 pt INK centered: "Break-even needs only about 0.4% of the launch area's online shopping."

Expansion strip (y 6.45 – 6.90): three small BLUE dots joined by INK35 line with labels
Inter 12 pt: "Launch: Duhok · Semel · Zakho" → "Next: Erbil · Mosul · Sulaymaniyah" → "Then: all of Iraq".

Footnote: "Population: 2024 national census (Iraqi Ministry of Planning). Internet users: DataReportal, Digital 2026: Iraq. E-commerce: ECDB, Iraq 2025. Duhok figures marked “estimate” = Iraq rate × Duhok population share."

Animation: entry auto — Iraq card Fade. [click 1] Duhok governorate card Fade. [click 2]
launch-area card Zoom + break-even line Fade (after, 80). [click 3] expansion strip Fade.

Notes — Time: ~25s
We launch in Duhok — specifically Duhok city, Semel and Zakho. Iraq has 46 million people and 39.6 million internet users. [click] Duhok governorate has 1.6 million people. [click] Our launch area alone has about 1.06 million people — roughly 890,000 online and about 30 million dollars a year of online shopping. To break even we need about 0.4 percent of that. [click] Then Erbil, Mosul and Sulaymaniyah, then all of Iraq.

### Slide 7 — Target customers: who we serve (new)

Label "Target customers". Headline "Who we serve."

Left (x 0.79 – 7.40): heading "Shoppers" Inter Bold 16 pt + small tag "target groups" (Inter 10 pt INK60).
Three cards (6.61 x 1.05) at y 3.10 / 4.25 / 5.40, each: icon in BLUE12 circle + line 1
Inter Bold 15 pt INK + line 2 Inter 12 pt INK60:
- briefcase — "Young professionals · 23–38" / "Tech, gadgets, perfume — no time for DMs"
- house — "Families · 26–48" / "Kitchen, home, personal care — savings and reliable delivery"
- graduation-cap — "Students & deal hunters · 18–24" / "Chargers, cables, gaming — refuse to overpay"
Stat under cards (y 6.50): "88%" Comfortaa Bold 26 pt BLUE + "of 179 surveyed shoppers would use an app like Cheapify" Inter 13 pt INK.

Right (x 7.80 – 12.54): heading "Merchants" Inter Bold 16 pt. One card (4.74 x 2.25, y 3.10):
store icon + "Social-media shops in Duhok" Inter Bold 15 pt INK; lines Inter 12.5 pt INK60:
"Instagram · Facebook · TikTok" / "1,500–50,000 followers" / "20–150 products" /
"Tech, accessories, beauty, home, perfume".
Stats (y 5.55 – 6.90): "85%" + "sell on Instagram or Facebook"; "75%" + "want to try Cheapify" (Comfortaa Bold 26 pt BLUE + Inter 13 pt INK), and "of 20 surveyed merchants" Inter 10 pt INK60.

Footnote: "Age groups are our targeting plan — the survey did not ask age. Survey: Cheapify market survey, n=199 (179 shoppers, 20 merchants), Sep–Oct 2026."

Animation: entry auto — left heading + three cards Fade (stagger 80) + 88% Zoom (after).
[click 1] right card Fade + both stats Zoom (after, 80).

Notes — Time: ~22s
Who exactly? Three groups of shoppers: young professionals with no time for DMs, families who want savings and reliable delivery, and students who refuse to overpay. 88 percent of the shoppers we surveyed would use an app like this. [click] And Duhok's Instagram, Facebook and TikTok shops: 85 percent sell there, and 75 percent want to try Cheapify.

### Slide 8 — Product (was 7)

- Stepper 3 sub: "Doorstep total upfront · cash or card".
- Stepper 5: title "Automatic payout" / sub "Paid 48 hours after delivery, minus our fee".
- Screen S3: two payment options — "Cash on delivery" (selected) and "Card / e-wallet" (unselected).
- Screen S5 replaced: card "Payout sent" / "Order #1042 · delivered" / "Return window closed (48 h)" / "Item 92,000" / "Cheapify fee −2,960" / divider / "Paid to you 89,040 IQD" (bold).
- Screen S1 result rows 2–3: keep the builder's placeholders but REMOVE the seller counts
  (rows read "Anker 10K · 30 W — from 35,000 IQD" and "Xiaomi 10K · 165 W — from 60,000 IQD").
- Notes: "Here's how it works. A shopper searches for a product. [click] He sees every seller on one page, with Best Value on top. [click] He orders in under thirty seconds and pays cash on delivery — or by card. [click] The merchant gets a ready order on the dashboard and WhatsApp, packs it, and the courier picks it up. [click] 48 hours after delivery, once the return window closes, the merchant is paid automatically — minus our small fee."

### Slide 9 — Business model (was 8)

- Top line: "Shopper pays 28,000 IQD" + "(25,000 item + 3,000 Duhok delivery)".
- Replace the bottom-right block. New block (6.90 – 12.54): heading "From our 1,450 IQD" Inter
  Bold 14 pt INK; rows Inter 12.5 pt (amounts right-aligned, Inter Bold):
  "WhatsApp order messages −90" / "Login codes −25" / "Share of returns −20" /
  "Re-sending failed deliveries −200"; divider; "Profit per delivered order" + "1,115 IQD"
  (Comfortaa Bold 30 pt INK).
- Animation: [click 4] fee columns (as before, faster). [click 5] new block: heading Fade, cost
  rows Fade (stagger 80), profit line Zoom (after).
- Footnote: "Example: 25,000 IQD item, cash on delivery, Duhok city; courier rate 2,500 IQD quoted by Fast Delivery (Duhok). The delivery margin applies once the courier contract is signed. Card processing fees not yet quoted."
- Notes: "We only earn when an order is delivered. Take a 25,000-dinar order: the shopper pays 28,000. [click] 24,050 goes to the merchant — [click] 2,500 to the courier — [click] and 1,450 to Cheapify: our fee plus a small delivery margin. [click] Our fee gets lighter as prices rise. [click] From our 1,450, we pay about 335 for messages, login codes, returns and re-sending failed deliveries — leaving 1,115 dinars of profit per order."

### Slide 10 — Competitor analysis (was 9)

- Elryan "One page per product" → no (circle-x).
- Cheapify header cell: logo (w 0.42) centered on top, "Cheapify" below it in Comfortaa Bold
  13 pt BLUE, centered; header area taller as needed; ≥ 0.15 in padding from the card border
  on all sides.
- Notes: "Look at today's options. [click] On Instagram, prices are often hidden. Miswag, iBazzar and Elryan show prices — but the same product shows up in several listings, and Elryan sells only its own stock. [click] Only Cheapify puts every seller of a product on one page — and compares them for you."

### Slide 11 — Growth strategy (was 10; fully replaced)

Label "Growth strategy". Headline "We grow on two sides: stores and shoppers."

Two columns of rows (icon in BLUE12 circle 0.50 + line 1 Inter Bold 15 pt INK + line 2
Inter 12 pt INK60), row pitch 0.82:
- Left (x 0.79 – 6.40) heading "Stores" Inter Bold 16 pt BLUE (y 2.75):
  1. handshake — "I sign the first 20 stores in person" / "Bazaar visits, Instagram outreach, a 45-second demo video"
  2. gift — "A founding offer they can't ignore" / "0% commission in month 1 + their products in our paid ads"
  3. link — "Their followers come too" / "Store link in bio and in replies to “price?” comments"
- Right (x 6.93 – 12.54) heading "Shoppers" (y 2.75):
  1. megaphone — "Targeted ads across Duhok" / "Facebook, Instagram, TikTok — real products, real prices"
  2. clapperboard — "Short videos" / "“The old way vs the Cheapify way”"
  3. graduation-cap — "Campus & workplace deals" / "UoD, AUK, Nawroz and office hubs"
  4. users — "Waitlist & referrals" / "~52 contacts ready · credits only after a delivered order"
- Loop strip (y 6.30 – 6.90), centered, Inter Bold 13 pt INK with BLUE arrow glyphs drawn as
  shapes: "More stores" → "Lower prices" → "More shoppers" → "More orders" → back to "More stores" (return arrow).

Animation: entry auto — both headings Fade. [click 1] store rows Fade (stagger 80).
[click 2] shopper rows Fade (stagger 80). [click 3] loop strip pieces Fade (stagger 60).

Notes — Time: ~28s
We grow on two sides. [click] Stores: I sign the first 20 in person — in the bazaar and on Instagram — with zero commission in month one and their products in our paid ads. They also send their own followers to their Cheapify page. [click] Shoppers: targeted ads across Duhok, short videos comparing the old way with ours, campus and workplace deals, and our waitlist with referral credits. [click] Then the loop: more stores mean lower prices, lower prices bring more shoppers, and more orders bring more stores.

### Slide 12 — Financial feasibility (was 11; chart reworked)

Headline unchanged. Left panel:
- Tile 1: "~585 orders / month" / "break-even · about 20 a day"
- Tile 2: "1,115 IQD" / "profit per delivered order"
- Milestone table below tiles (native table, Inter 11.5 pt; header NEUTRAL):

| | Fast | Planned |
| :--- | :--- | :--- |
| Lowest cash point | −$1,800 (month 2) | −$2,180 (month 3) |
| Monthly break-even | Month 3 | Month 4 |
| All losses recovered | Month 6 | Month 8 |

Chart: y range −$3,000 (6.55) to +$3,500 (3.05); x points Start, M-2, Launch(M-1), M1…M10.
Series (USD cumulative):
- Fast (BLUE 3 pt, separate segments), Start…M7 only, then a small BLUE up-arrow at M7 with
  label "keeps rising": −1,133, −1,273, −1,413, −1,699, −1,800, −1,640, −1,182, −130, +1,350, +3,202
- Planned (INK 2.5 pt, separate segments), Start…M10: −1,133, −1,273, −1,413, −1,774, −2,041, −2,178, −2,167, −1,858, −1,382, −719, +130, +1,090, +2,124
- Slow (INK35 dashed 1.5 pt, single polyline), Start…M10: −1,133, −1,273, −1,413, −1,811, −2,160, −2,446, −2,658, −2,721, −2,746, −2,678, −2,517, −2,300, −2,083 — NO trough marker, NO number; label at its right end, Inter 10.5 pt INK60: "Slow case: profitable every month from month 7".
- Milestone dots (0.15 in) in the series color, no text labels on the chart: Fast M2 (lowest),
  M3 (break-even month — dot on the line), M6 (crosses 0); Planned M3, M4, M8.
- Legend top-right: Fast · Planned · Slow (line swatches, Inter 11 pt).
Footnote: "Planned: orders grow 100 → 2,000 a month; Fast: twice that pace; Slow: half. Costs 652,000 IQD/month after launch (790,000 from month 6), incl. 1.7M IQD startup. Assumes 25,000 IQD average order and a signed courier contract. USD at 1,500 IQD."

Animation: entry auto — tiles Fade. [click 1] axes/zero line/legend + Planned segments
(fast stagger) + Planned dots + table Planned column. [click 2] Fast segments + dots + arrow
+ table Fast column. [click 3] Slow line + its label Fade.

Notes — Time: ~30s
We break even at about 585 orders a month — around 20 a day, roughly one per store. [click] On our planned pace, the lowest cash point is about 2,200 dollars in month three; we break even in month four and recover everything by month eight. [click] With a strong growth push, the fast case breaks even in month three and recovers everything by month six. [click] And even if growth is slow, we're still profitable every month from month seven.

### Slide 13 — Funding (was 12; right side replaced)

Headline "What $7,500 makes possible."
- Keep the donut + legend (left/middle) exactly as built.
- Remove the "Every rank funds a complete plan" panel and the "Founder in-kind" line.
- Right (x 8.60 – 12.54): heading "Each amount has a job" Inter Bold 15 pt INK; three
  stacked step cards (h 0.95), visually rising (largest at top):
  - "$7,500 — Grow fast" (Inter Bold 15 pt BLUE) / "+ growth marketing and founding-store kits → aims for the fast case" (Inter 11.5 pt INK60)
  - "$4,500 — Launch properly" / "+ hand-run pilot, company registration (unlocks the courier contract and card payments), larger reserve"
  - "$2,500 — Reach break-even safely" / "Covers the cash gap until monthly break-even"
  Build order bottom-up ($2,500 first).
- Callout (BLUE12, bottom right): code icon + "No salaries. No developers. I build the platform myself." Inter Bold 13 pt INK.
- Animation: entry auto — center Zoom. [click 1] slices + legend rows (fast stagger).
  [click 2] $2,500 card. [click 3] $4,500 card. [click 4] $7,500 card. [click 5] callout.
- Notes — Time: ~30s
  We're asking for 7,500 dollars, and every dollar has a job. [click] It covers the cash gap to break-even, growth marketing, registration, store kits, a pilot and a reserve. [click] 2,500 alone carries us safely to break-even. [click] 4,500 also funds the pilot and registers the company — which unlocks the courier contract and card payments. [click] The full 7,500 adds a real growth push — aiming for the fast case: break-even in month three. [click] And none of it goes to salaries or developers: I build the platform myself.

### Slide 14 — What now (was 13)

- Node 1 title "Register the company & sign the courier contract" / sub "Rates already quoted".
- Node 3 sub "Cash on delivery; card soon after".
- Notes unchanged.

### Cover / Thank you — unchanged.

### Appendix

- A6 risks: replace row "Courier holds the cash" with: "Courier transfers cash late" / "Contract sets a transfer deadline (target 24 h); merchants are paid only after the money arrives; card payments reduce cash".
- A7 flow → 7 steps: "Checkout (cash or card)" → "Merchant accepts" → "Sealed package + waybill" → "Courier pickup" → "Delivery (cash collected)" → "Courier transfers to Cheapify" → "Merchant paid after 48 h". Lines below:
  "Returns: 48 hours — faulty item: merchant pays the return; change of mind: customer pays 3,000 IQD."
  "Refunds: card → back to the card; cash orders → Cheapify credit, or electronic transfer for faulty items."
  "Failed delivery: one free re-attempt, then back to the merchant."
  "Packaging: opaque and sealed; tamper tape on orders ≥ 50,000 IQD."
- New A8 — headline "How we sized Duhok"; table:

| Figure | Value | How | Source |
| :--- | :--- | :--- | :--- |
| Launch-area population | 1,062,224 | Duhok 497,029 + Zakho 398,876 + Semel 166,319 | 2024 census |
| Duhok governorate population | 1,599,871 | — | 2024 census |
| Launch-area internet users | ≈ 0.89M | 1,062,224 × 83.8% | DataReportal rate (Iraq) |
| Launch-area online shopping | ≈ $30M / year | 2.30% of Iraq's population × $1.32B | ECDB Iraq 2025 |
| Break-even sales | ≈ $117,000 / year | 585 orders × 25,000 IQD × 12 ÷ 1,500 | Cheapify model |
| Share needed | ≈ 0.4% | $117,000 ÷ $30M | — |

  Note line: "No official Duhok internet or e-commerce figures exist; estimates use Iraq-wide rates. Duhok is 80% urban, so these are likely conservative."

## 4. Presenter guide (`presentation/speaker-script.md` → rename to `presentation/presenter-guide.md`)

Structure (markdownlint-clean, no emojis, plain tables):

1. Title + "How to use this guide" (3 bullets).
2. Timing table (slide, section, target s, words, est. s at 140 wpm, cumulative time).
3. For each main slide, a section with exactly these sub-headings:
   - **Say** — the notes script (with [click] markers).
   - **Key numbers** — table: Number · What it means · Source.
   - **How it's calculated** — short bullet math (only where a number is derived).
   - **If they ask** — the Q&A pairs from §5 for that slide.
4. Appendix slides: one line each on when to show them.
5. **References** — numbered list from §6.

PowerPoint notes per main slide: "Time: ~Ns", the script, then a blank line and
"Key numbers:" with 2–5 one-line "number — source" items (from the Key numbers tables).

## 5. Q&A content (verbatim answers)

Slide 2
- Q: Are these really the same product? A: Yes — every listing on the chart states 25,000 mAh and 165 W (Anker A1695 class). Listings whose model we couldn't confirm were left out.
- Q: Maybe the 200,000 listing is old or a mistake? A: It was live in Miswag's search on Oct 20, 2026, right beside the 100,000 one. That's exactly the problem: the shopper can't tell which price is right.
- Q: Some Instagram posts are older? A: Yes — they're dated April to October 2026. Even using only same-day app listings, the gap is 100,000 vs 200,000.

Slide 3
- Q: How was the survey done? A: An online form in Arabic, Kurdish and English, Sep–Oct 2026: 199 responses — 179 shoppers and 20 merchants.
- Q: Is it representative? A: It's self-selected and mostly Arabic-language (168 of 199; only 10 in Kurdish), so we treat it as strong direction, not proof. The hand-run pilot measures real buying.
- Q: Is the vacuum the same model? A: Same Newal 2000W vacuum and design; Miswag lists it as VAC351004, the Instagram post as VAC-3510.

Slide 4
- Q: How do you know two listings are the same product? A: Barcode first. Without a barcode, we match name, specs and photos, and a reviewer approves. Merchants join the existing product page instead of creating a new one.
- Q: Can a store pay to rank first? A: No. Ranking is lowest doorstep total, then delivery speed, then seller rating. It is never for sale.

Slide 5
- Q: Why would merchants pay a fee when Instagram is free? A: Instagram costs them hours of “price?” messages every day. We send ready orders with address and variant, handle delivery, and charge only on delivered orders — about 3.8% on a 25,000 IQD order.
- Q: What does “order in 30 seconds” mean? A: Our checkout design target: pick the seller, confirm the address, choose cash or card.

Slide 6
- Q: Which Duhok — the whole governorate? A: We start with Duhok city, Semel and Zakho — about 1.06 million people in the 2024 census. Akre, Amedi, Shekhan and Bardarash come later.
- Q: Where do 890,000 and $30 million come from? A: They're estimates. No official Duhok figures exist, so we apply Iraq's 83.8% internet rate to the launch-area population, and Iraq's $1.32B e-commerce market by population share (2.3%). Duhok is 80% urban, so the real figures are probably higher.
- Q: How much of that market do you need? A: About 0.4%. Break-even is ~585 orders a month at 25,000 IQD — about $117,000 a year.

Slide 7
- Q: Where do the age groups come from? A: They're our targeting plan, based on what each group buys. The survey didn't ask age — our next survey will.
- Q: How many merchants are there in Duhok? A: Not measured yet. We have about 8 valid store leads from the survey and target 20 founding stores.

Slide 8
- Q: Is the app built? A: It's in development — I'm building it myself. These are concept screens.
- Q: Why pay merchants after 48 hours, not instantly? A: That's the return window. Paying once it closes means we never have to take money back.
- Q: Who handles the cash? A: Never us. The courier collects it and transfers it to Cheapify electronically; we pay merchants and couriers electronically. Every merchant links a payment account when joining.
- Q: When do card payments start? A: Shortly after launch, once our payment-gateway account is approved — that needs the company registration.

Slide 9
- Q: What is the 335? A: Per order: WhatsApp messages 90, login codes 25, share of returns 20, re-sending failed deliveries 200.
- Q: Is the 500 delivery margin real? A: Fast Delivery quoted 3,000 IQD in the city with a 500 contract discount, so 2,500. We charge 3,000. The contract needs company registration — our first step after funding.
- Q: And without the contract? A: Profit drops to about 615 IQD per order and break-even rises to about 1,060 orders a month — slower, but still positive.
- Q: What about card fees? A: Not quoted yet; these figures are for cash-on-delivery orders.

Slide 10
- Q: Why can't Miswag just copy you? A: Their catalog is built as one listing per seller; rebuilding it around one page per product is hard. We're local, merchant-first and low-fee from day one.
- Q: What about Elryan? A: It sells its own stock, and the same products still appear in more than one listing.

Slide 11
- Q: What if stores refuse? A: The founding offer is strong: zero commission in month one and free ads, and they keep their Instagram. 75% of surveyed merchants want to try it, and we have about 8 leads.
- Q: What if shoppers don't come? A: The bio link is only one channel — we also run targeted ads, videos, campus deals and referrals. And a hand-run pilot (about $100) tests real demand before any big spending.

Slide 12
- Q: What are the assumptions? A: 25,000 IQD average order; costs of 652,000 IQD a month after launch (790,000 from month 6); a signed courier contract; orders growing from 100 to 2,000 a month on the planned pace.
- Q: What does the slow case look like? A: Half the planned orders: the lowest cash point is about $2,750 in month 6, we're profitable every month from month 7, and full recovery takes about 20 months. Slower, but the business survives.

Slide 13
- Q: Why $7,500? A: Cash gap to break-even $2,200, growth marketing $2,500, registration $1,000, store kits $900, reserve $800, pilot $100.
- Q: What if you receive less? A: $2,500 still gets us to break-even; $4,500 adds the pilot, registration and a reserve. Growth is just slower.
- Q: What have you invested yourself? A: My equipment and my time — I'm building the whole platform myself, so there are no developer costs.

Slide 14
- Q: What's the riskiest step? A: Registration and the courier contract, because the delivery margin depends on them. That's why they're step one and budgeted.

## 6. References (for the guide)

1. Cheapify market survey, n=199 (179 shoppers, 20 merchants), Sep–Oct 2026 — `../entrepreneurship/assets/evidence/survey-analysis.md`
2. Price evidence screenshots (Miswag, iBazzar, Elryan, Instagram), Sep–Oct 2026 — `../entrepreneurship/assets/evidence/README.md`
3. Iraqi Ministry of Planning, 2024 national census (governorate and district figures) — reported by Peregraf: https://peregraf.com/en/news/10297 ; district table: https://www.citypopulation.de/en/iraq/admin/11__dah%C5%ABk/
4. DataReportal, “Digital 2026: Iraq” (data late 2025) — https://datareportal.com/reports/digital-2026-iraq
5. ECDB, Iraq e-commerce market (revenue 2025: US$1,317M) — https://ecdb.com/resources/sample-data/market/iq/all
6. Fast Delivery (Duhok) courier quote, Oct 2026 — `../finance/01_operational_budget.md`
7. Cheapify financial model — `../finance/03_cash_flow_and_breakeven.md`, `../finance/04_funding_request.md`
8. Go-to-market plan (segments, merchant profile, channels) — `../marketing/01_two_sided_gtm_strategy.md`

## 7. Timing target

Main deck total at 140 wpm must stay ≤ 5:40. If it exceeds, report — do not cut content yourself.
