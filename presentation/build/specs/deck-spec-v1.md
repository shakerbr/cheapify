# Cheapify — GIZ Final Pitch Deck: Build Spec (lead-authored, authoritative)

All text, numbers and the script below are final. Implement verbatim. If something is
impossible as specified, stop and report — do not substitute your own content or numbers.

## 0. Hard rules

- Base file: copy `archive/program-giz-cheapify/Presentation-stuff/Modified template.pptx`.
  Do NOT reuse anything from the archived Cheapify decks (old styling is discarded): no
  "PART X ·" labels, no pill-shaped uppercase kickers, no three-text-card grids, no
  icon-in-tinted-square card headers.
- Template elements carried over EXACTLY (same image parts, positions, sizes):
  - Cover (template slide 1) and Thank-you (template slide 3): GIZ logo + CAPA/AUK logo +
    navy contact footer (bar, 4 icons, 3 texts) — keep the slides as they are and add content.
  - Every content slide: ONLY the two header logos at template-slide-2 positions/sizes:
    GIZ `image2.png` at x=723900 y=436205 cx=1428202 cy=800089 EMU;
    CAPA `image4.png` at x=8289593 y=351575 cx=3178503 cy=969350 EMU. No footer.
  - Keep the embedded Comfortaa font parts.
- No emojis anywhere (slides, notes, script file). Icons = Lucide SVG rendered to PNG.
- No internal process content on slides or notes (no pillar names, ADR numbers, file paths,
  "model v1", etc.).
- Kurdish only in Arabic script. Arabic/Kurdish runs: `IBM Plex Sans Arabic`, `rtl="1"`,
  `lang="ar-IQ"`, set both `a:latin` and `a:cs`.
- Fonts: headlines/hero numbers `Comfortaa` (b=1); everything else `Inter` (regular or b=1).
  Do NOT use weight-named families ("Inter SemiBold") — only Regular/Bold via b attribute.
- Slide size 13.333 x 7.5 in (template). All coordinates below are inches from top-left.
- Honesty labels are mandatory where specified (footnotes, "Illustration", "Concept").

## 1. Design tokens

| Token | Hex | Use |
| :--- | :--- | :--- |
| INK | #101820 | headlines, primary text |
| INK60 | #5A6672 | secondary text, section labels, footnotes |
| INK35 | #A9B1B9 | tertiary, axis ticks |
| BLUE | #298FC2 | brand accent, stat numbers, active states |
| BLUE12 | #E5F2F8 | light blue fills |
| BLUE50 | #94C7E0 | secondary series |
| GREEN | #228848 | ONLY Best Value badge + Cheapify checkmarks |
| GREEN8 | #EDF5F0 | Best Value row tint |
| RED | #D22730 | problem highlights (rings, crosses, +122%) |
| ORANGE | #FFA300 | iBazzar series dot, pilot donut slice |
| NEUTRAL | #DDE5ED | borders, dividers, light fills |
| SURFACE | #F4F6F8 | image wells |

- Card: white fill, 1 pt NEUTRAL border, rounded rectangle (~0.14 in radius), soft outer
  shadow (blur 8 pt, distance 2 pt, direction 90°, INK at 8–10% alpha). Never hard shadows.
- Section label (content slides): at (0.79, 1.56): a BLUE bar 0.30 x 0.05 in at
  (0.79, 1.66), then text 0.45 in to its right — Inter 13 pt INK60, sentence case.
- Headline: Comfortaa Bold 30 pt INK at (0.79, 1.86), width 11.75, height 0.62, one line.
- Visual zone: y 2.65 – 6.95. Footnote: Inter 9 pt INK60 at (0.79, 7.06), w 11.75, h 0.26.
- Nothing may overlap the header logos (keep content at y >= 1.50).

## 2. Animation vocabulary (must work in PowerPoint, Google Slides import, LibreOffice)

Allowed ONLY: Fade-in (entr presetID 10), Zoom-in (entr presetID 53 subtype 16 — scale
ppt_w/ppt_h from 0 + fade), Appear (entr presetID 1), Fade-out (exit presetID 10).
No motion paths, no Morph, no emphasis effects, no wipe/fly. Slide transition on every
slide: `<p:transition spd="fast"><p:fade/></p:transition>`.

Defaults: fade 450 ms, zoom 400 ms. "Stagger" = afterEffect with the given delay, or
withEffect with cumulative delays. Each click group = one `p:par` with
`delay="indefinite"`. "Auto on entry" = first group uses afterEffect with delay 0 so it
plays when the slide appears.

Prefer animating group shapes and pictures (no `bldP` needed). Any animated `p:sp` with a
text body needs `<p:bldP spid=".." grpId="0" animBg="1"/>`; if it also has an exit effect,
its exit cTn uses grpId="1" and it gets a second bldP with grpId="1".
Element order in slide XML: cSld, clrMapOvr, transition, timing.

Reference XML (ids/spid placeholders):

```xml
<!-- Fade-in -->
<p:par><p:cTn id="N" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" grpId="0" nodeType="clickEffect|withEffect|afterEffect">
  <p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>
  <p:set><p:cBhvr><p:cTn id="N" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>
    <p:tgtEl><p:spTgt spid="S"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>
    <p:to><p:strVal val="visible"/></p:to></p:set>
  <p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="N" dur="450"/><p:tgtEl><p:spTgt spid="S"/></p:tgtEl></p:cBhvr></p:animEffect>
</p:childTnLst></p:cTn></p:par>
<!-- Zoom-in: set visibility as above, then -->
<p:anim calcmode="lin" valueType="num"><p:cBhvr><p:cTn id="N" dur="400" fill="hold"/><p:tgtEl><p:spTgt spid="S"/></p:tgtEl>
  <p:attrNameLst><p:attrName>ppt_w</p:attrName></p:attrNameLst></p:cBhvr>
  <p:tavLst><p:tav tm="0"><p:val><p:fltVal val="0"/></p:val></p:tav><p:tav tm="100000"><p:val><p:strVal val="#ppt_w"/></p:val></p:tav></p:tavLst></p:anim>
<!-- same for ppt_h, plus animEffect transition="in" filter="fade" dur 400 -->
<!-- Fade-out (presetClass="exit"): animEffect transition="out" filter="fade" dur 450, then
     set style.visibility = hidden with cond delay="449" -->
```

Main sequence wrapper: tmRoot par → seq concurrent="1" nextAc="seek" mainSeq with
prevCondLst onPrev / nextCondLst onNext (standard PowerPoint structure).

## 3. Assets to produce (`presentation/assets/`)

Evidence source dir: `entrepreneurship/assets/evidence/`. Pixel boxes are approximate
(original resolution) — open each image, verify, adjust, and visually confirm every crop,
blur and ring position. Blur = Gaussian radius ~14 px over the whole box.

| Output | Source | Crop (x0,y0,x1,y1) | Blur | Ring targets (for slide overlay) |
| :--- | :--- | :--- | :--- | :--- |
| `ev-miswag-anker.jpg` | `Anker-Power-Bank/Screenshot_20261020_225824_Miswag.jpg` | bottom row of results, both tiles incl. prices + seller chips ≈ (0,1258,1080,2122) | both seller chips ≈ (41,2068,303,2115) and (566,2068,751,2115) | "200,000 IQD" ≈ (44,1888,226,1936); "100,000 IQD" ≈ (566,1888,751,1936) |
| `ev-ibazzar-xiaomi.jpg` | `xiaomi-power-bank/Screenshot_20260920_130923.jpg` | top two result rows ≈ (0,288,1080,1818) | none | "70,000 IQD" ≈ (581,924,771,970); "60,000 IQD" ≈ (62,1700,257,1747) |
| `ev-instagram-noprice.jpg` | `no-price-dm-for-price/Screenshot_20261021_122639_Instagram.jpg` | composite: ad image ≈ (57,108,1008,905) stacked above the comment row ≈ (36,2000,1028,2090), 24 px gap, dark bg | shop logo on ad ≈ (77,134,206,257); phone-number box on ad ≈ (553,846,771,905); commenter avatar+username ≈ (36,2000,386,2057) | the comment text "سعرها كم ؟" ≈ (771,2050,890,2090) in source coords |
| `ev-ibazzar-foundcheaper.jpg` | `Anker-Power-Bank/Screenshot_20261020_225624.jpg` | title → price → "Free delivery" → "Found Cheaper? Tell us!" → delivery box ≈ (0,1131,1080,1774) | none | "Found Cheaper? Tell us!" ≈ (36,1468,501,1518) |
| `product-anker.png` | `Anker-Power-Bank/Screenshot_20261020_225624.jpg` | product photo only ≈ (244,296,694,1016) | none | — |
| `cheapify-logo.png` | `assets/cheapify-logo.svg` | render 1400 px wide, transparent | — | — |
| `icons/*.png` | Lucide SVGs (current names), stroke 2, 256 px, recolored | — | — | — |

Icons needed (Lucide names may have changed — use the current repo names): shopping-bag,
store, eye, message-circle-off, banknote, package-check, layout-dashboard, percent, link,
users, trending-up, circle-check, circle-x, contrast (= "partly" half circle), truck,
search, sparkle (4-point star), calendar-check, chart-column, code, map-pin.
Colors: BLUE default; GREEN for sparkle + Cheapify checks; RED for circle-x; INK60 for
competitor checks and contrast.

Ring overlays = rounded-rectangle outlines, RED 2.25 pt, no fill, ~6 px padding, placed by
mapping crop pixels to the displayed picture box (keep aspect; "contain" fit).

## 4. Slides (main deck: 14 slides) + 7 appendix slides after Thank you

Times are the spoken budget. Script goes into speaker notes verbatim (first line
"Time: ~Ns", then the text). `[click]` marks a click; the first group of each slide plays
automatically on entry unless stated.

### Slide 1 — Cover (template slide 1)

Add, centered horizontally:
- Logo `cheapify-logo.png` width 1.25 (height auto, 7:9) at y 1.80.
- "Cheapify" Comfortaa Bold 54 pt INK, box y 3.45 h 0.95, centered.
- "The bright side of choosing." Comfortaa 22 pt BLUE, y 4.38 h 0.5.
- "Shakir Bashar · Founder" Inter Bold 14 pt INK, y 5.18 h 0.32.
- "Youth Entrepreneurship Program · Final Pitch" Inter 12 pt INK60, y 5.50 h 0.3.

Animation (auto on entry): logo Zoom-in; then wordmark Fade (after, 0); slogan Fade
(after, 0); both founder lines Fade (with slogan).

Notes — Time: ~8s
Good morning. I'm Shakir Bashar, a computer engineer — and this is Cheapify: the bright side of choosing.

### Slide 2 — Problem

Label "Problem". Headline "Same power bank. 100,000 or 200,000 IQD."

Left: card (0.79, 2.70, 4.10 x 3.70). Picture `ev-miswag-anker.jpg` contain-fit in well
(0.94, 2.85, 3.80 x 2.95) on SURFACE. Caption (0.94, 5.88, 3.8 x 0.4) Inter 11 pt INK60:
"Miswag app — same search, same screen (Oct 20, 2026)". Two RED rings over the two prices.

Right: dot chart, x 5.40 – 12.54.
- Title (5.40, 2.70) Inter Bold 13 pt INK60: "Every price we found for this model (IQD)".
- Legend (top-right, y 2.72): dots + Inter 11 pt: "Instagram" (INK), "Miswag" (BLUE),
  "iBazzar" (ORANGE).
- Axis line y 5.60 from x 5.60 (=80,000) to x 12.30 (=210,000), INK35 1 pt; ticks + labels
  at 80k,100k,120k,140k,160k,180k,200k (Inter 10 pt INK60, under the line).
- Dots, 0.24 in, colored by channel, sorted ascending, stacked upward (0.28 in per level)
  when |dx| < 0.26 in:
  90,000 IG · 95,000 IG · 99,000 IG · 100,000 IG · 100,000 Miswag · 121,000 Miswag ·
  134,000 iBazzar · 135,000 Miswag · 137,200 Miswag · 200,000 Miswag
- Bracket (RED 2 pt, with end ticks) above the dots from x(90,000) to x(200,000), y ~4.05.
- "+122%" Comfortaa Bold 40 pt RED centered over bracket (y ~3.05, h 0.6).
- "≈ 110,000 IQD more for the same model" Inter Bold 14 pt INK below it (y ~3.62).

Footnote: "Live app listings captured Oct 20, 2026 (Miswag, iBazzar); Instagram offers from seller posts dated Apr–Oct 2026. Seller names blurred."

Animation: entry auto — left card Fade. [click 1] ring 200,000 Zoom; ring 100,000 Zoom
(after, 150 ms). [click 2] axis + ticks + title + legend Fade; then dots Zoom one by one in
ascending order (after, 80 ms each). [click 3] bracket Fade; "+122%" Zoom (with);
sub-label Fade (after, 100 ms).

Notes — Time: ~30s
This is one power bank — the Anker 25,000, 165 watt. Same model. On one app's search page, it's listed at 100,000 dinars… [click] and right beside it, at 200,000. [click] Across Instagram and shopping apps, we found it anywhere from 90,000 to 200,000 dinars. [click] That's 122 percent more — for the exact same product.

### Slide 3 — Problem · evidence

Label "Problem · evidence". Headline "It's not one product. It's the whole market."

Three cards, w 3.55 h 3.30, y 2.70, x = 0.79 / 4.89 / 8.99. In each: image well
(x+0.15, y+0.15, 3.25 x 2.20) SURFACE, picture contain-fit; title (x+0.15, y+2.45,
3.25 x 0.36) Inter Bold 14 pt INK; sub (x+0.15, y+2.82, 3.25 x 0.36) Inter 10.5 pt INK60.
1. `ev-ibazzar-xiaomi.jpg` — "Same product, listed twice" / "iBazzar app · 60,000 vs 70,000 IQD" — rings on both prices.
2. `ev-instagram-noprice.jpg` — "No price: 'call to order'" / "Instagram · a buyer asks: “How much is it?”" — ring on the comment.
3. `ev-ibazzar-foundcheaper.jpg` — "An app asks you to report cheaper prices" / "iBazzar app · “Found Cheaper? Tell us!”" — ring on that line.

Stat band y 6.15 – 6.95:
- Left: "97%" Comfortaa Bold 34 pt BLUE at (0.79, 6.15, 1.45 x 0.7); text (2.30, 6.18,
  4.1 x 0.7) Inter 14 pt INK: "of 179 surveyed shoppers notice big price gaps on the same item".
- Right: "55%" at (6.90, 6.15); text (8.40, 6.18, 4.1 x 0.7): "of merchants pick answering “price?” messages as a top headache — the most common answer".

Footnote: "Screenshots Sep–Oct 2026 (shop names and phone numbers blurred) · Cheapify market survey, n=199 (179 shoppers, 20 merchants), Sep–Oct 2026."

Animation: [click 1] card 1 Fade + its rings Zoom (after, 150). [click 2] card 2 + ring.
[click 3] card 3 + ring. [click 4] "97%" Zoom + text Fade (with); "55%" Zoom (after, 200) +
text Fade (with).

Notes — Time: ~30s
And it's not one product — it's the whole market. [click] Apps list the same item twice, at two prices. [click] Many Instagram pages hide the price: "call to order" — and under the post, someone asks: "How much is it?" [click] One app even added a button: "Found it cheaper? Tell us." [click] We surveyed 199 people: 97 percent of shoppers see these gaps — and for merchants, answering "price?" messages is the most common headache.

### Slide 4 — Solution

Label "Solution". Headline "One product. One page. Every seller."

State A — "chaos" cards (7), each card 2.15 x 0.95, no rotation. Content: source label
Inter 10 pt INK60, "Anker 25K 165W" Inter 11 pt INK, price Inter Bold 16 pt INK.
Positions / source / price:
(1.00,2.95) Instagram 95,000 IQD · (4.10,3.35) Miswag 200,000 IQD · (7.60,2.85) iBazzar
134,000 IQD · (10.20,3.60) Instagram "Price? DM us" (Inter Bold 14 pt RED) · (2.20,5.30)
Miswag 100,000 IQD · (6.00,5.60) Instagram 99,000 IQD · (9.30,5.20) Miswag 121,000 IQD.

State B — master card (1.90, 2.75, 7.50 x 4.15), card style with elev-2 shadow (blur 24 pt,
distance 8 pt, 8%):
- `product-anker.png` contain-fit (2.15, 3.00, 1.30 x 1.55).
- Title (3.65, 3.00, 5.6 x 0.4) Inter Bold 17 pt INK "Anker Power Bank 25,000 mAh · 165 W";
  sub (3.65, 3.42, 5.6 x 0.3) Inter 12 pt INK60 "One page · every verified seller".
- Column headers y 4.02 Inter Bold 10.5 pt INK60: Seller (2.15) | Item (4.20, right-aligned
  w 1.15) | Delivery (5.45, right w 1.05) | Doorstep total (6.60, right w 1.45) | Arrives (8.20, w 1.05).
- Rows h 0.52 at y 4.32 / 4.86 / 5.40 / 5.94, NEUTRAL hairline separators,
  Inter 13 pt (totals Inter Bold):
  1. Store A · Duhok | 92,000 | +3,000 | 95,000 IQD | Today
  2. Store D · Erbil | 91,000 | +5,000 | 96,000 IQD | 1–2 days
  3. Store B · Duhok | 99,000 | +3,000 | 102,000 IQD | Today
  4. Store C · Duhok | 121,000 | +3,000 | 124,000 IQD | Today
- Row-1 highlight: GREEN8 rounded rect behind row 1 (2.05 – 9.25).
- Best Value pill: GREEN fill, white sparkle icon + "BEST VALUE" Inter Bold 10 pt white,
  (8.95, 4.36, 1.35 x 0.40), sticking out past the card's right edge.
- Ranking legend (10.60 – 12.54): three rows at y 4.30 / 4.90 / 5.50: BLUE circle
  (0.36) with white "1/2/3" + Inter Bold 12 pt INK text: "Lowest doorstep total" /
  "Fastest delivery" / "Best seller rating". Below at y 6.15: "Ranking can't be bought."
  Inter Bold 12.5 pt BLUE.

Footnote: "Illustration — store names and prices are examples."

Animation: entry auto — chaos cards Fade staggered (after, 80 ms each).
[click 1] all chaos cards Fade-out (with each other) + master card group (frame, picture,
title, sub, headers) Zoom-in (with, delay 200). [click 2] rows Fade one by one (after,
150). [click 3] row-1 tint Fade + pill Zoom (with); legend rows Fade (after, 150 each);
"Ranking can't be bought." Fade (after, 150).
Static/PDF variant: omit the chaos cards.

Notes — Time: ~30s
Today, one product is scattered across pages and apps. Cheapify's rule is simple: [click] one product, one page. [click] Every seller of that product sits on it, showing the doorstep total — item plus delivery. [click] Then our Best Value ranking picks the winner: lowest doorstep total, then fastest delivery, then seller rating. And the ranking can never be bought.

### Slide 5 — Value proposition

Label "Value proposition". Headline "Shoppers save. Merchants sell."

Vertical divider NEUTRAL 1 pt at x 6.665 from y 2.80 to 6.85. No card boxes.
Each half: header at y 2.78 = icon in BLUE12 circle (0.55) + Inter Bold 20 pt INK.
Rows at y 3.70 / 4.70 / 5.70: icon in BLUE12 circle (0.55) at x0; phrase Inter Bold 18 pt
INK at x0+0.75; sub-line Inter 13 pt INK60 below it. Left x0 = 0.95; right x0 = 7.05.
- Left header (shopping-bag) "For shoppers":
  eye — "Every price, side by side" / "No more checking ten pages"
  message-circle-off — "Order in 30 seconds" / "No “price?” DMs, no waiting"
  banknote — "Cash on delivery" / "Doorstep total shown upfront"
- Right header (store) "For merchants":
  package-check — "Orders, not interrogations" / "Ready orders with address and variant"
  layout-dashboard — "Free dashboard" / "Stock, orders and weekly payouts in one place"
  percent — "Fair, low fee" / "About 3.8% on a typical 25,000 IQD order"

Animation: entry auto — both headers + divider Fade. [click 1] left rows Fade (after,
150 each). [click 2] right rows Fade (after, 150 each).

Notes — Time: ~20s
For shoppers: [click] every price side by side, an order in thirty seconds, and cash at the door. For merchants: [click] real orders instead of "price?" messages, a free dashboard for stock and payouts, and a fair fee — about 3.8 percent on a typical order.

### Slide 6 — Target market & customers

Label "Target market & customers". Headline "Duhok first. Then all of Iraq."

Left — two cards x 0.79 w 5.60:
- Card 1 (y 2.75, h 1.85): shopping-bag icon + "Shoppers who buy on Instagram & Facebook"
  Inter Bold 16 pt; "88%" Comfortaa Bold 40 pt BLUE; "would use an app like Cheapify"
  Inter 14 pt INK; "179 surveyed shoppers" Inter 10 pt INK60.
- Card 2 (y 4.80, h 1.85): store icon + "Social-media sellers"; two stats side by side:
  "85%" / "sell on Instagram or Facebook" and "75%" / "want to try Cheapify";
  "20 surveyed merchants" Inter 10 pt INK60.

Right — expansion path (x 6.90 – 12.54), three circles linked by INK35 dotted connectors:
- c1 center (7.60, 3.40) r 0.38, BLUE fill, label right of it: "Duhok" Inter Bold 15 pt INK / "Launch" Inter 11 pt INK60.
- c2 center (9.20, 4.20) r 0.62, BLUE50 fill, label below (w 2.4): "Erbil · Mosul · Sulaymaniyah" / "Phase 2".
- c3 center (11.30, 5.00) r 0.95, BLUE12 fill + BLUE 1 pt border, label inside: "All of Iraq" Inter Bold 15 pt INK / "Phase 3".
- Stats row y 6.15 – 6.90: "39.6M" Comfortaa Bold 24 pt BLUE + "internet users in Iraq"
  Inter 12 pt INK at x 6.90; "$1.3B" + "e-commerce market (2025)" at x 9.80.

Footnote: "Cheapify market survey, n=199, Sep–Oct 2026 · Internet users: DataReportal, Digital 2026: Iraq (late 2025) · E-commerce revenue: ECDB, Iraq 2025 (US$1.32B)."

Animation: entry auto — both left cards Fade (after, 150). [click 1] c1 Zoom + label Fade.
[click 2] connector 1 Fade, c2 Zoom + label. [click 3] connector 2, c3 Zoom + label; then
stats row Fade (after, 150).

Notes — Time: ~25s
Our customers are shoppers who buy through Instagram and Facebook — 88 percent said they'd use an app like this — and the social sellers behind those pages: 85 percent sell there, and 75 percent want to try Cheapify. [click] We launch in Duhok, [click] grow to Erbil, Mosul and Sulaymaniyah, [click] then all of Iraq — 39.6 million internet users and a 1.3-billion-dollar e-commerce market.

### Slide 7 — Product

Label "Product". Headline "Order in 30 seconds. Pay at the door."

Left: one phone. Frame = INK rounded rect (1.35, 2.62, 2.20 x 4.30); screen inset 0.08 in,
white, rounded. Five screens drawn with native shapes, stacked in the same screen area
(each screen = one group). Keep text >= 8 pt; key numbers 13–14 pt bold.
- S1 Search: small Cheapify logo + search field "anker power bank"; 3 result rows (gray
  thumbnail square, name, "from 95,000 IQD · 4 sellers").
- S2 Compare: product thumb (`product-anker.png`) + "Anker 25K · 165 W"; 3 seller rows with
  doorstep totals 95,000 / 96,000 / 102,000; GREEN "BEST VALUE" pill on row 1.
- S3 Checkout: "Item 92,000" / "Delivery (Duhok) 3,000" / divider / "Doorstep total
  95,000 IQD" bold; payment radio "Cash on delivery" selected; BLUE button "Order now".
- S4 Merchant: header "Your store · Orders"; card "New order" / "Anker 25K · Black · ×1" /
  "95,000 IQD · cash on delivery" / "Duhok — Malta"; BLUE button "Accept" + outline button
  "Print waybill"; truck icon + "Courier pickup today".
- S5 Payout: card "Sunday payout" / "12 orders this week" / "Sales 1,104,000" /
  "Cheapify fee −35,520" / divider / "Paid to you 1,068,480 IQD" bold.

Right: stepper x 4.60 – 12.54, rows at y 2.75 + i·0.84 (i = 0..4), row h 0.76:
number circle (0.48) NEUTRAL fill INK60 number; title Inter Bold 18 pt INK; sub Inter 13 pt INK60.
1. "Search" / "Find any product in one place"
2. "Compare" / "Every seller on one page — Best Value on top"
3. "Order" / "Doorstep total upfront · cash on delivery"
4. "Merchant packs, courier picks up" / "The order lands on the dashboard and WhatsApp"
5. "Weekly payout" / "Paid every Sunday, minus our small fee"
Active-state overlay per row = BLUE12 rounded rect behind the row + BLUE circle with white
number on top of the gray one.

Footnote: "Concept screens — app in development."

Animation: entry auto — phone frame, S1, all stepper rows, row-1 active overlay Fade.
[click 1] S2 Fade-in + S1 Fade-out (with); row-2 overlay Fade-in + row-1 overlay Fade-out.
[click 2] S3 / row 3. [click 3] S4 / row 4. [click 4] S5 / row 5.
Static/PDF variant: show S2 only, no active overlays.

Notes — Time: ~30s
Here's how it works. A shopper searches for a product. [click] He sees every seller on one page, with Best Value on top. [click] He orders in under thirty seconds and pays cash on delivery. [click] The merchant gets a ready order on the dashboard and WhatsApp, packs it, and the courier picks it up. [click] Every Sunday, the merchant gets paid — minus our small fee.

### Slide 8 — Business model

Label "Business model". Headline "We earn only when an order is delivered."

Top:
- (0.79, 2.70) Inter Bold 16 pt INK "Shopper pays 28,000 IQD at the door" + same line
  Inter 12 pt INK60 "(25,000 item + 3,000 Duhok delivery)".
- Base bar (0.79, 3.15, 11.75 x 0.85) NEUTRAL fill, centered text "28,000 IQD" Inter Bold 16 pt INK.
- Segments over it (same y/h), left to right: Merchant 10.093 in BLUE; Courier 1.049 in
  INK60; Cheapify 0.608 in INK (24,050 / 2,500 / 1,450 of 28,000).
- Labels under the bar (y 4.10): "Merchant 24,050 IQD — keeps 96% of the item price"
  (left-aligned under its segment, Inter Bold 14 pt INK + BLUE for "96%"); "Courier
  2,500" and "Cheapify 1,450" right side with thin leader lines, Inter Bold 13 pt.
- Callout above the Cheapify segment (y 2.70 – 3.10, right-aligned at 12.54):
  "950 fee + 500 delivery margin" Inter 12 pt INK60.

Bottom (y 4.85 – 6.90):
- Left (0.79 – 6.40): "Our fee gets lighter as prices rise" Inter Bold 15 pt INK; three
  BLUE columns (w 1.2) bottom-aligned at y 6.55 with heights 1.35 / 0.81 / 0.41 (5 : 3 : 1.5);
  value labels above "5%" / "3%" / "1.5%" Comfortaa Bold 20 pt INK; captions below
  "first 10,000 IQD" / "10,001 – 100,000" / "above 100,000" Inter 11 pt INK60.
- Right (6.90 – 12.54): "≈ 1,100 IQD" Comfortaa Bold 44 pt INK; below Inter 13 pt INK60:
  "kept per delivered order after messaging, failed-delivery and return costs".

Footnote: "Example: 25,000 IQD item delivered in Duhok city; courier rate 2,500 IQD quoted by Fast Delivery (Duhok). The delivery margin applies once the courier contract is signed."

Animation: entry auto — top line + base bar Fade. [click 1] Merchant segment + label
Fade. [click 2] Courier segment + label. [click 3] Cheapify segment + label + callout.
[click 4] fee columns Zoom (after, 150 each) with labels; "≈ 1,100 IQD" Zoom + text Fade
(after, 200).

Notes — Time: ~25s
We only earn when an order is delivered. Take a 25,000-dinar order: the shopper pays 28,000 at the door. [click] 24,050 goes to the merchant — [click] 2,500 to the courier — [click] and 1,450 to Cheapify: our fee plus a small delivery margin. [click] Our fee gets lighter as prices rise, and after costs we keep about 1,100 dinars per order.

### Slide 9 — Competitor analysis

Label "Competitor analysis". Headline "Nobody else puts every seller on one page."

Grid: row-label column x 0.79 – 4.30 (Inter Bold 15 pt INK); five value columns from
x 4.50, each 1.60 wide. Header row y 2.80 (Inter Bold 13 pt INK, centered):
"Instagram / Facebook" · "Miswag" · "iBazzar" · "Elryan" · "Cheapify" (Cheapify in BLUE,
small logo left of the word). Rows at y 3.45 / 4.20 / 4.95 / 5.70 (h 0.75), NEUTRAL
separators. Marks = 0.36 in icons centered: yes = circle-check (INK60 for competitors,
GREEN for Cheapify); partly = contrast (INK60); no = circle-x (RED).

| Row | Instagram / Facebook | Miswag | iBazzar | Elryan | Cheapify |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Prices shown upfront | partly | yes | yes | yes | yes |
| One page per product | no | no | no | yes | yes |
| Every seller compared on that page | no | no | no | no | yes |
| Third-party sellers can join | yes | yes | yes | no | yes |

Cheapify column background: BLUE12 card with BLUE 1.5 pt border from y 2.70 to 6.50.
Legend y 6.55 Inter 11 pt INK60: "✓ yes" etc. must be drawn with the same icons
(no Unicode symbols): [circle-check] yes · [contrast] partly · [circle-x] no.

Footnote: "Based on in-app screenshots (Sep–Oct 2026) and public platform information."

Animation: entry auto — row labels + header row (except Cheapify) + separators Fade.
[click 1] the four competitor columns' marks Fade column by column (after, 200).
[click 2] Cheapify column card + header Zoom; its marks Zoom (after, 120 each).

Notes — Time: ~22s
Look at today's options. [click] On Instagram, prices are often hidden. Miswag and iBazzar show prices, but list the same product more than once. Elryan sells only its own stock. [click] Only Cheapify puts every seller of a product on one page — and compares them for you.

### Slide 10 — Growth strategy

Label "Growth strategy". Headline "Every merchant brings their followers."

Left — flywheel, center (3.90, 4.75): ring circle r 1.55, BLUE 2 pt, no fill; Cheapify
logo (w 0.55) at center. Four node cards (2.00 x 0.95, card style) centered at: top
(3.90, 3.20), right (6.00, 4.75), bottom (3.90, 6.30), left (1.80, 4.75). Each: icon
(0.32) + Inter Bold 13 pt INK (2 lines max):
- top (store): "A store joins"
- right (link): "Adds its Cheapify link to its bio"
- bottom (users): "Its followers order on Cheapify"
- left (trending-up): "More orders bring more stores"
Four small BLUE triangles on the ring between nodes, pointing clockwise.
Caption under the bottom node (3.90, 6.82) Inter 11 pt INK60: "≈ zero cost to acquire these shoppers".

Right — phases x 8.00 – 12.54, three cards (4.54 x 1.00) at y 2.80 / 3.95 / 5.10:
- "Phase 1 · Months 1–6" (Inter 11 pt BLUE) / "Duhok" (Inter Bold 16 pt INK) / "20 founding stores · 3,000+ orders" (Inter 12 pt INK60)
- "Phase 2 · Months 7–15" / "Erbil · Mosul · Sulaymaniyah" / "75 stores"
- "Phase 3 · Month 16+" / "All of Iraq" / "300+ stores"
Offer chip (8.00, 6.30, 4.54 x 0.45) BLUE12 fill, Inter Bold 12 pt INK: "Founding stores: 0% commission in month 1 + free ads".

Animation: entry auto — ring + logo Fade. [click 1] top node + triangle. [click 2] right
node + triangle. [click 3] bottom node + triangle + caption. [click 4] left node + triangle.
[click 5] phase cards Fade (after, 150 each) + offer chip.

Notes — Time: ~25s
Growth starts with merchants. [click] A store joins, [click] adds its Cheapify link to its bio, [click] and its followers order through us — at almost no cost. [click] More orders bring more stores. [click] We start with 20 founding stores in Duhok — first month commission-free, plus free ads — then Erbil, Mosul and Sulaymaniyah, then all of Iraq.

### Slide 11 — Financial feasibility

Label "Financial feasibility". Headline "Break-even at about 20 orders a day."

Left — three KPI tiles (card style) x 0.79 w 3.30 h 1.22 at y 2.75 / 4.10 / 5.45:
- "~585 orders / month" Comfortaa Bold 24 pt INK / "break-even · about 1 order per store per day" Inter 12 pt INK60
- "~1,115 IQD" / "kept per delivered order"
- "Month 4" / "monthly break-even (planning case)"

Right — cumulative cash chart from shapes. Plot x 4.90 → 12.30 (13 points equally spaced),
y = +$2,500 at 3.05 and −$3,000 at 6.55 (linear). Zero line INK 1 pt with label "0" and
"break-even line" (Inter 10 pt INK60, right end). Y labels (Inter 10 pt INK60) at x 4.30:
+$2k, +$1k, $0, −$1k, −$2k, −$3k. X labels (Inter 10 pt INK60) under plot: "Start",
"Launch" (3rd point), then "M2", "M4", "M6", "M8", "M10".

Data (USD, cumulative; points: Start, M-2, M-1/Launch, M1 … M10):
- Planning: −1,133, −1,273, −1,413, −1,774, −2,041, −2,178, −2,167, −1,858, −1,382, −719, +130, +1,090, +2,124
- Slow case (half speed): −1,133, −1,273, −1,413, −1,811, −2,160, −2,446, −2,658, −2,721, −2,746, −2,678, −2,517, −2,300, −2,083

Planning line = 12 straight segments, BLUE 3 pt (separate shapes so they can appear in
sequence). Slow case = one dashed INK35 2 pt polyline. Markers (0.16 in dots + Inter
11 pt labels):
- Planning M3: RED dot — "Lowest point −$2,180 (month 3)"
- Planning M4: BLUE dot — "Monthly break-even (month 4)"
- Planning M8: INK dot — "All losses recovered (month 8)"
- Slow M6: INK35 dot — "Worst case −$2,750 (half-speed growth)"

Footnote: "Planning case: orders grow 100 → 2,000 a month; costs 652,000 IQD/month after launch (790,000 from month 6); includes 1.7M IQD startup costs. Assumes 25,000 IQD average order and a signed courier contract. USD at 1,500 IQD."

Animation: entry auto — KPI tiles Fade (after, 150 each). [click 1] axes, labels, zero
line Fade; planning segments Start→M3 Appear (after, 70 each); M3 marker Zoom.
[click 2] segment M3→M4 Appear; M4 marker Zoom. [click 3] segments M4→M10 Appear
(after, 70); M8 marker Zoom. [click 4] slow-case line Fade; its marker Zoom.

Notes — Time: ~30s
Our numbers are deliberately conservative. We break even at about 585 orders a month — around 20 a day, roughly one order per store. [click] On our planning curve, the lowest cash point is about 2,200 dollars, in month three. [click] We break even in month four, [click] and recover everything by month eight. [click] Even at half the growth speed, the worst case stays under 2,800 dollars.

### Slide 12 — Funding

Label "Funding". Headline "$7,500 launches Duhok."

Left — donut from blockArc shapes, center (2.70, 4.75), outer r 1.75, inner r 1.05;
start at 12 o'clock, clockwise. Center: "$7,500" Comfortaa Bold 32 pt INK; "≈ 11.25M IQD"
Inter 12 pt INK60.

| Slice | USD | Degrees | Color |
| :--- | :--- | :--- | :--- |
| Launch gap (until break-even) | 2,200 | 105.6 | INK |
| Growth marketing | 2,500 | 120.0 | BLUE |
| Registration & legal | 1,000 | 48.0 | INK60 |
| Merchant kits & packaging | 900 | 43.2 | BLUE50 |
| Reserve | 800 | 38.4 | NEUTRAL (+ INK35 hairline) |
| Pilot test (10–20 orders) | 100 | 4.8 | ORANGE |

Legend x 4.80 – 8.20, rows at y 3.05 + i·0.48: color chip (0.22) + label Inter 13 pt INK
+ amount Inter Bold 13 pt INK right-aligned at 8.20.

Right x 8.60 – 12.54:
- "Every rank funds a complete plan" Inter Bold 15 pt INK (y 2.80).
- Three rows (card style, h 0.80) at y 3.25 / 4.15 / 5.05: "1st · $7,500" Inter Bold 15 pt
  BLUE + "Full plan: launch + growth marketing"; "2nd · $4,500" + "Launch, registration
  and pilot; slower growth"; "3rd · $2,500" + "Covers the launch gap; growth stays organic"
  (Inter 12 pt INK60).
- Callout (8.60, 6.05, 3.94 x 0.85) BLUE12 fill: code icon + "Built in-house: $0 to developers · $0 salaries" Inter Bold 13 pt INK; second line Inter 11 pt INK60 "Founder in-kind contribution ≈ $9,500 (equipment + build time)".

Animation: entry auto — center text Zoom. [click 1] slices Fade one by one with their
legend rows (after, 150). [click 2] callout Fade. [click 3] tier title + rows Fade (after, 150).

Notes — Time: ~25s
We're asking for 7,500 dollars. [click] It covers the launch gap, growth marketing, registration, merchant kits and a reserve. [click] I build the platform myself, so not one dollar goes to developers or salaries. [click] And at second place, 4,500, or third, 2,500, each amount still funds a complete plan.

### Slide 13 — Funding is done — what now?

Label "Funding is done — what now?". Headline "Grant → pilot → launch → break-even."

Timeline line y 4.40 from x 1.20 to 12.10, NEUTRAL 3 pt. Nodes (0.42 circles, BLUE fill,
white number Inter Bold 13 pt) at x 1.60 / 4.15 / 6.70 / 9.25 / 11.80.
Above each node (y 3.70): "when" Inter Bold 13 pt BLUE. Below each node: card (2.30 x 1.55,
top y 4.75): title Inter Bold 14 pt INK, sub Inter 11.5 pt INK60.
1. "First" — "Register & sign the courier contract" / "Rates already quoted"
2. "Next" — "Hand-run pilot: 10–20 real orders" / "Measure real order size and costs"
3. "Launch" — "20 founding stores go live in Duhok" / "0% commission in month 1 + free ads"
4. "Month 4" — "Monthly break-even" / "About 600 orders a month"
5. "Month 7+" — "Erbil · Mosul · Sulaymaniyah" / "Then all of Iraq"
KPI strip (0.79, 6.55, 11.75 x 0.35): chart-column icon + Inter 12 pt INK60
"We report monthly: delivered orders · sales volume · active stores · repeat orders · delivery time".

Animation: entry auto — line Fade. [click 1..5] node i Zoom + "when" + card Fade (with).
KPI strip Fade after node 5 (after, 200).

Notes — Time: ~20s
Once funded: [click] we register and sign the courier contract — the rates are already quoted. [click] We run 10 to 20 real orders by hand. [click] We launch with 20 founding stores. [click] We break even by month four, [click] and then we bring Cheapify to Erbil, Mosul and Sulaymaniyah.

### Slide 14 — Thank you (template slide 3)

Add, centered:
- Logo w 1.05 at y 1.70.
- "Thank you" Comfortaa Bold 46 pt INK, y 3.10 h 0.8.
- "The bright side of choosing." Comfortaa 20 pt BLUE, y 3.95.
- "ڕوویێ گەش یێ هەلبژارتنێ" IBM Plex Sans Arabic 20 pt INK, RTL, y 4.42.
- "الجانب المشرق للاختيار" IBM Plex Sans Arabic 20 pt INK, RTL, y 4.88.
- "getcheapify.com" Inter Bold 16 pt BLUE, y 5.42; "Shakir Bashar · Founder" Inter 13 pt INK60, y 5.75.
Animation: auto on entry — logo Zoom, then texts Fade (after, 0) as one group.

Notes — Time: ~6s
Cheapify — the bright side of choosing. Thank you.

### Appendix slides A1–A7 (after Thank you; Q&A only)

Header logos as content slides. Label "Appendix". Tables = native pptx tables: header row
Inter Bold 12 pt INK on NEUTRAL fill, body Inter 12 pt INK, NEUTRAL borders. One fade-in on
entry is enough. Notes: one short line each ("Backup for questions.").

A1 — Headline "Fee schedule: lighter as prices rise"
Line: "5% on the first 10,000 IQD · 3% on 10,001–100,000 · 1.5% above 100,000 — marginal, like tax brackets: a higher price never pays a lower fee."

| Item price (IQD) | Cheapify fee (IQD) | Effective rate |
| :--- | :--- | :--- |
| 5,000 | 250 | 5.0% |
| 10,000 | 500 | 5.0% |
| 25,000 | 950 | 3.8% |
| 45,000 | 1,550 | 3.4% |
| 100,000 | 3,200 | 3.2% |
| 150,000 | 3,950 | 2.6% |
| 350,000 | 6,950 | 2.0% |
| 1,200,000 | 19,700 | 1.6% |

A2 — Headline "Unit economics per order"

| Per 25,000 IQD order (Duhok city) | IQD |
| :--- | :--- |
| Platform fee | +950 |
| Delivery margin (3,000 charged − 2,500 courier) | +500 |
| WhatsApp notifications | −90 |
| Login codes (OTP) | −25 |
| Returns | −20 |
| Failed-delivery re-attempts | −200 |
| Kept per delivered order | +1,115 |

Second table "Break-even (monthly costs 652,000 IQD after launch, incl. a capped 225,000 incentive pool)":

| Case | Kept per order | Break-even orders / month |
| :--- | :--- | :--- |
| Base case | 1,115 | ~585 |
| Courier contract not signed | 615 | ~1,060 |
| Average order 20,000 IQD | 965 | ~676 |
| Incentive pool doubled | 1,115 | ~787 |

A3 — Headline "Three growth scenarios"

| Scenario | Orders by month 6 | Lowest cash point | Monthly break-even | All losses recovered |
| :--- | :--- | :--- | :--- | :--- |
| Fast (2× plan) | 2,700 / month | −$1,800 (month 2) | Month 3 | Month 6 |
| Planning | 1,350 / month | −$2,180 (month 3) | Month 4 | Month 8 |
| Slow (half of plan) | 675 / month | −$2,750 (month 6) | Month 7 | ~Month 20 |

Note line: "Includes 1.7M IQD startup costs and two build months before launch. USD at 1,500 IQD."

A4 — Headline "Survey: what 199 people told us"
Two columns of short lines (Inter 13 pt), no table:
- Shoppers (179): "97% notice price gaps on the same item (39% often see large gaps)" · "88% would use a side-by-side app · 10% maybe · 2% prefer DMs" · "Top annoyances: untrusted / duplicate pages ~52% · found it cheaper after buying ~47% · DM just to ask the price ~46% · delivery delays ~27%" · "~52 usable beta-waitlist contacts"
- Merchants (20): "85% sell on Instagram / Facebook" · "75% would try Cheapify · 15% maybe (depends on commission) · 10% no" · "Top headaches: “price?” DMs 55% · price conflicts 45% · cost of own app/site 35% · manual delivery coordination 35%" · "~8 valid pilot-store leads"
- Bottom line Inter 11 pt INK60: "Limits: self-selected sample; only 10 Kurdish-language responses; stated intent is not purchases — the hand-run pilot measures real behavior."

A5 — Headline "Six documented price cases"

| Product | Lowest | Highest | Gap | Where |
| :--- | :--- | :--- | :--- | :--- |
| Anker power bank 25K 165W | 90,000 (Instagram) | 200,000 (Miswag) | +122% | Instagram, iBazzar, Miswag |
| ASUS VA24EHF monitor | 135,000 (Elryan) | 163,350 (Miswag) | +21% | Elryan, Miswag |
| Hoco HX80 coffee maker | 25,000 (Instagram) | 35,280 (Miswag) | +41% | Instagram, Miswag |
| Newal 2000W vacuum | 95,000 (Instagram) | 133,250 (Miswag) | +40% | Instagram, Miswag |
| Xiaomi 165W power bank | 60,000 | 70,000 | +17% | Same app (iBazzar) |
| Coffee machines (two posts) | — | — | No price shown | Instagram: “call / DM to order” |

Note: "Screenshots Sep–Oct 2026; Instagram posts dated Apr–Oct 2026."

A6 — Headline "Top risks and how we handle them"

| Risk | How we handle it |
| :--- | :--- |
| Buyers and sellers bypass the app | Low fee (~3.8%), no contact details on parcels, credits and ratings count only on-platform |
| Slower growth than planned | Plan is already conservative; half-speed case capped at ~$2,750; hand-run pilot tests demand before spending |
| Courier contract delayed | Registration first (budgeted); second courier quote as fallback; without the margin, break-even ≈ 1,060 orders/month |
| Failed deliveries ("not at home") | One free re-attempt; 3 failures remove cash-on-delivery; WhatsApp reminder before delivery |
| Courier holds the cash | Contract fixes custody and timing; weekly settlement |

A7 — Headline "How an order flows"
Six-step horizontal flow (numbered circles + one line each, Inter 13 pt):
"Checkout (cash on delivery)" → "Merchant accepts" → "Sealed package + waybill" → "Courier pickup" → "Delivery + cash collected" → "Sunday settlement".
Under it, three short lines (Inter 12 pt INK60):
"Returns: 48 hours — faulty item: merchant pays the return; change of mind: customer pays 3,000 IQD."
"Failed delivery: one free re-attempt, then back to the merchant."
"Packaging: opaque and sealed; tamper tape on orders ≥ 50,000 IQD."

## 5. Outputs

- `presentation/Cheapify-GIZ-Pitch.pptx` — animated deck (21 slides).
- `presentation/Cheapify-GIZ-Pitch.pdf` — static variant (final states; chaos cards
  omitted; slide 7 shows S2 with no active overlay).
- `presentation/speaker-script.md` — title, timing table (slide, section, target seconds,
  word count, estimated seconds at 140 wpm), then the script per slide (same text as notes).
  Markdownlint-clean, no emojis.
- `presentation/build/build_deck.py` (+ helper modules if needed): one command rebuilds
  everything; all slide text/numbers in a clearly separated data section; `--static` flag.
- `presentation/assets/…` processed images and icons.
