# Cheapify deck — v4 spec (post teacher review, finance ADR-015)

Status: DRAFT — **awaiting founder approval. Do not build or change the deck until the founder says go.** Founder choices made: **C1 = clean title cover**, **C2 = cut slide 8** → 14 main slides (current slides 9–15 become 8–14).

Inputs: teacher review of the v3 deck (Oct 2026, summarized in `agent/progress.md`), finance per ADR-015 (`finance/04`), speaker notes / Q&A data in `deck_data.py` (already updated for funding/finance; slide code in `slides_a.py` / `slides_b.py` is not yet).

## 0. Quality bar ("10/10")

Every slide must pass all of these before it ships:

1. **One focal point.** One idea, one dominant visual; the eye knows where to land in under 2 seconds.
2. **≤ ~25 words on the slide** (headline + labels), excluding header, footnote and numbers. Detail lives in the notes and the presenter guide.
3. **Headline = a full statement**, not a topic ("Profitable from month 4…", not "Financial feasibility").
4. **No half-empty slides.** Content fills the safe area (x 0.6–12.73 in, y 1.95–6.95 in) with balanced weight; no block of white larger than ~25% of the content area.
5. **Grid:** 12 columns, 0.25 in gutters; left edges align across slides; the same element (section label, headline, footnote) sits in the same place on every slide.
6. **Type scale:** headline 30 pt Comfortaa · key numbers 28–48 pt Inter bold · labels 14–16 pt · captions 11–12 pt · footnote 9 pt, ≤ 1 line.
7. **Color meaning is fixed:** blue = Cheapify / planned case; green = Best Value only; red = problem / cost; ink = neutral; grey = context. Never decorative.
8. **No overlaps, no clipping, nothing touching the header logos**, checked in every animation state, not just the final one.
9. **Animation explains, never decorates.** Each click reveals the next idea in speaking order; long sequences finish in < 1.2 s.
10. **Every number on a slide** is in the notes with its source and in `presenter-guide.md` with its calculation.

## 1. Global changes

- **Header logos to the template's proportions** (measured from `archive/GIZ-assets/template.jpg` while locking exact native image aspect ratios: `789:442` for German Cooperation and `905:276` for CAPA):
  - Cover + thank-you (exact template): German Cooperation 2.60 × 1.46 in at (0.47, 0.40); CAPA/AUK 1.76 × 0.54 in, right edge 12.88 in, top 1.20 in.
  - Content slides (same ratio at 75%): German Cooperation 1.95 × 1.09 in at (0.47, 0.30); CAPA/AUK 1.32 × 0.40 in, right edge 12.88 in, top 0.90 in.
  - Today CAPA is ~1.7× wider than the German Cooperation logo on content slides; after the change it is ~0.68× its width, as in the template, with 100% native aspect ratio preserved.
- **Animation pacing ~1.5× slower:** stagger 25 → 40 ms, effect 150 → 220 ms; single reveals 300 ms. Still click-by-click.
- **Runtime ≤ 5:40** at 140 wpm (current notes: 5:30; cutting slide 8 saves ~23 s; the funding script is 48 s and comes down to ~30 s → target ~5:00, leaving room for natural pauses).
- **Fonts:** All three font families — **Comfortaa**, **Inter**, and **IBM Plex Sans Arabic** (Regular + Bold) — are embedded directly into the `.pptx` (`ppt/fonts/*.fntdata` via `<p:embeddedFontLst>`) from project-local TTF files in `presentation/assets/fonts/`. Do not re-save the output `.pptx` in ONLYOFFICE (it strips embedded fonts); ship the PDF and `presentation/assets/fonts/` as fallback.
- **Pre-flight check on the presenting computer:** open the PPTX, click through every slide once, confirm fonts and animations.

## 2. Main slides

### Slide 1 — Cover (program title + small hook — founder choice)

- No product name, no logo (slide 2 owns the problem; slide 4 reveals Cheapify).
- Centered stack: **"Youth Entrepreneurship Program"** (Comfortaa bold, large `38 pt`) · **"One product, ten prices."** (`18 pt` Comfortaa, Brand Blue subtitle) · thin blue rule · "Shakir Bashar · Founder" · "4 November 2026".
- Exact template header sizes + the CAPA footer bar (cover template). Generous, balanced white space is intended here (rule 4 doesn't apply to the cover).
- Script (~6 s): name + "I'm here to show you a problem every online shopper in Kurdistan and Iraq faces."

### Slide 2 — Problem

- Headline (the problem statement, shown alone when the slide opens): **"Online in Iraq, you can't know the real price before you buy."**
- Visual: the Miswag screenshot alone, large (~60% of the slide width), the two listings side by side.
- Clicks: (1) Miswag screenshot + model context appear → (2) ring on 100,000 IQD → (3) ring on 200,000 IQD → (4) a "2× the price — same power bank" bracket and callout.
- Right side, one line under the image: "Same search. Same screen. Same model." No dot plot (the six-case price table stays in the appendix).
- Footnote: "Miswag app, 20 Oct 2026. Seller names blurred."

### Slide 3 — Problem, continued

- Headline: **"And it's the whole market."**
- Three evidence cards, one per click, each with one 3–5-word label:
  1. "Same item, listed twice" (iBazzar duplicate listings).
  2. "No price — just 'DM us'" (Instagram call-to-order post).
  3. "A fake 35% discount" (vacuum: 95,000 on Instagram vs Miswag 133,250 "was 205,000").
- Final click: one stat bar across the bottom: **"97% of 179 shoppers we surveyed see this."** The 55% merchant stat moves to the notes.

### Slide 4 — Solution (the reveal)

- Click 0 (auto): Cheapify logo + name zoom in, centered, with "The bright side of choosing." — the first time the brand appears.
- Click 1: logo/name fade out; headline appears alone: **"Cheapify puts every seller's real price for the same product on one page."**
- Click 2: 7 scattered duplicate listings appear.
- Click 3: scattered listings collapse into one product page; seller rows sort by doorstep total.
- Click 4: the green Best Value badge lands on the winner + right rail with three rules.
- Right rail keeps three icons: lowest doorstep total · fastest delivery · best seller rating — "Ranking can't be bought."

### Slide 5 — Value proposition

- No content change (teacher: good). Apply the global header/pacing only.

### Slide 6 — Duhok in numbers

- Headline: **"Duhok first: about 1 million people."**
- Keep the three zoom circles: Iraq 46.1M → Duhok governorate 1.60M → launch area 1.06M (Duhok · Semel · Zakho).
- Keep the two icon stats with "estimate" tags: ≈ 0.89M online · ≈ $30M a year online.
- **Replace the 0.4% pie** with one explicit number: **"We need ~390 regular shoppers to break even"**, with a small caption "≈ 585 orders a month · 0.4% of the launch area's online shopping".
- **Remove the expansion strip** (moves to slide 11). Use the freed space to enlarge the circles.

### Slide 7 — Who we serve

- Headline: **"Budget-conscious shoppers who already compare prices."**
- Two balanced side-by-side cards (Shoppers on the left, Merchants on the right):
  - **Left card — Shoppers (tag: "targeting plan"):** three horizontal segment rows with icon badge, behavior label, what they buy, and right-aligned age pill:
    - "Time-poor professionals" · "Chargers, perfume, gadgets" · 23–38 · icon briefcase.
    - "Household budget buyers" · "Kitchen, home, personal care" · 26–48 · icon shopping basket. ("Families" removed.)
    - "Students & deal hunters" · "Cables, earbuds, gaming" · 18–24 · icon graduation cap.
    - Bottom footer strip with ring gauge: **97% notice big price gaps** (179 surveyed shoppers; the 88% "would use it" stays in the notes).
  - **Right card — Merchants (tag: "Duhok social shops"):** three structured profile rows mirroring the left card:
    - "Social-commerce sellers" · "Sell via DMs with digital photos ready" · IG · FB · TikTok.
    - "1,500 – 50,000 followers" · "Active local audience per page" · 20–150 products.
    - "20 founding stores at launch" · "Signed in person · 0% fee in month 1" · ~8 leads ready.
    - Bottom footer strip with two ring gauges: **85% sell on IG / FB** · **75% want to try** (20 surveyed merchants).
- Footnote: "Age groups are our targeting plan — the survey did not ask age. Survey n=199 (179 shoppers, 20 merchants), Sep–Oct 2026."

### (former slide 8) Product — **cut (founder choice C2)**

- Removed. Slide 4's script absorbs one sentence: "You order in seconds, pay cash or card at the door, and the store is paid automatically 48 hours later."
- The order flow stays available as appendix A7 if asked. Saves ~23 s.
- From here on, slide numbers below are the *current* numbers; in the new deck each is one lower (9 → 8 … 15 → 14).

### Slide 9 — Business model

- Headline unchanged: **"We earn only when an order is delivered."**
- **Remove the 28,000 IQD split bar** (the crowding source). Two balanced halves only:
  - Left — "Our fee": the three tier bars 5% · 3% · 1.5% with "Lighter as prices rise" (revenue stream — kept against the teacher's suggestion; it's how we earn).
  - Right — "Per order": waterfall 1,450 → −90 messages → −25 logins → −20 returns → −200 re-delivery → **1,115 IQD kept**.
- One caption under the left half: "Typical 25,000 IQD order → 950 IQD fee + 500 delivery margin." The 28,000 split moves to the notes.

### Slide 10 — Competitors

- No content change (teacher: good). Global header/pacing only.

### Slide 11 — Growth

- Headline: **"We grow on two sides: stores and shoppers."**
- Keep the flywheel and the two fuel columns. **Numbers go inside the fuel items** (no separate chip row):
  - Stores: "Signed in person · 20 stores" · "0% in month 1" · "Free ads" · "Their followers · 1.5k–50k each".
  - Shoppers: "Targeted ads · $2,200" · "Short videos" · "Campus deals · 3 universities" · "Referrals · 52 on the waitlist".
- **Add the expansion roadmap** as a slim strip at the bottom (moved from slide 6): Duhok · Semel · Zakho → Erbil · Mosul · Sulaymaniyah → all of Iraq.
- Fee tiers are not repeated here.

### Slide 12 — Financial feasibility

- Headline (answers the teacher's question directly): **"Profitable from month 4. Everything earned back by month 8."**
- Keep the full-width chart (planned bold, fast blue, slow faint) with on-curve pills.
- Planned-curve pills: "Lowest −$2,180 · month 3" · "Monthly break-even · month 4" · **"All losses recovered · month 8 (payback)"**. Fast: "month 3" · "month 6". Slow: "profitable every month from month 7".
- Replace the top banner with three small tiles above the chart: **Costs $435 / month** (from month 6: $527) · **Break-even 585 orders / month ≈ 390 shoppers** · **Payback month 8**.
- No spend schedule here (it belongs to the funding slide).

### Slide 13 — Funding

- Headline: **"What $5,480 makes possible."**
- Visual 1 (main): a horizontal timeline bar M0 → M6 where five colored blocks drop in, in the real order, one per click: Pilot $100 → Register the company $1,000 → Launch 20 stores $840 → Runway to break-even $1,340 → Growth push $2,200. The bar's months show *when* each is spent.
- Visual 2 (small, right): "Less? Still a plan." — $3,280 launches with slow-case runway · $2,710 minimum self-funding launch.
- Bottom bar: "No salaries. No developers. I build the platform myself."
- Footnote: "Registration: official KRI fee schedule · USD at the CBI rate of 1,500 IQD."
- Script trimmed to ~30 s; all derivations and challenge answers already in the notes/guide (`deck_data.py`).

### (former slide 14) Funding is done — what now? — **cut (founder choice)**

- Removed from the main deck (its milestones `M0 pilot` → `M0–M1 registration` → `M1 20 stores` → `M4 monthly break-even` → `M8 payback & expansion` are already shown on the Growth, Financial feasibility, and Funding slides; monthly KPI reporting is kept in the Funding Q&A notes). Saves ~15 s; main deck is now **13 slides** (`cover` .. `thanks`).

### Slide 15 — Thank you

- Minimal & clean closing: Cheapify logo · **"Thank you"** · **"The bright side of choosing."** · `getcheapify.com` · "Shakir Bashar · Founder" (Arabic and Kurdish slogans removed per founder review). Exact template header sizes + CAPA footer.

## 3. Appendix (backup, shown only if asked)

Restyle all appendix slides to the same quality bar (no half-empty tables; key row highlighted; one takeaway line in blue), and update content:

- A1 Fee schedule — unchanged numbers.
- A2 Unit economics — add a small "Payment method" row: COD 1,115 · SuperQi 0% · FIB QR 0.3% · card ≤1% (CBI cap).
- A3 Three scenarios — label Slow as "half the planned pace"; add the low-point composition (startup 1.70M + dev 0.42M + operating losses).
- A4 Survey — unchanged.
- A5 Six price cases — unchanged.
- A6 Top risks — unchanged content, restyled.
- A7 Order flow — unchanged content, restyled as icons.
- A8 Duhok sizing — add "~390 regular shoppers" row.
- **A9 (new) Funding detail** — the seven lines with derivations (`finance/04` §2), the monthly release schedule (§2.1) and "runway released only against actual losses".

## 4. QA before delivery

- Render every slide in every click state; automated bounding-box check for overlaps, clipping and logo collisions; manual visual review of each state.
- Check every on-slide number against `finance/` and the survey analysis.
- Timing report ≤ 5:40; presenter guide regenerated (no "$7,500", "reserve", "~25%", "Families").
- LibreOffice animation smoke test; founder click-through in the real presenting app.

## Not doing (teacher asks rejected)

- Fee tiers on the growth slide — they are the revenue stream and stay on the business model slide.
- Deleting the "what now" slide — it's a required GIZ section (kept short).
