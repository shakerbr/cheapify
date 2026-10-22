# Cheapify — Progress Log

A running chronological log of completed actions, file creations, and achieved milestones.

---

## Chronological Entries

### [2026-10-22] — Payment Model Updated + Pitch Deck v2 (founder review)

* **Payment model (founder decision):** Cheapify never handles cash; courier collects COD cash and transfers it electronically to Cheapify; card/e-wallet added shortly after launch (money to Cheapify at checkout); merchants paid automatically after the 48h return window; every merchant links a payment account. Synced across platform policies, fee structure §7, SOPs, canvas, risk matrix (R3 → late courier transfer), entrepreneurship/marketing docs; card processing fee logged as open assumption A13.
* **Duhok sizing:** 2024 census — launch area (Duhok + Semel + Zakho) 1,062,224, governorate 1,599,871 (replaces unverified "~1.45M"); population-share estimates ≈0.89M internet users / ≈$30M online shopping per year; break-even ≈0.4% of that.
* **Deck v2:** 15 main + 8 appendix slides; new Target market (Duhok in numbers) and Target customers slides; vacuum fake-deal evidence replaces "Found Cheaper?"; Elryan ✗ one page per product; growth rebuilt (stores + shoppers + loop); Fast/Planned/Slow chart with milestone table; funding shown as $2,500/$4,500/$7,500 jobs (no ranks, no in-kind line); animations ~4× faster; `presentation/presenter-guide.md` with script, key numbers, calculations, Q&A, references. Script ~5:11 at 140 wpm.

### [2026-10-21] — Final Pitch Deck Built + Evidence Re-Verification

* **Deck:** `presentation/Cheapify-GIZ-Pitch.pptx` (14 main slides + 7 appendix) and static `Cheapify-GIZ-Pitch.pdf`, built from the Modified template (GIZ/CAPA header on all slides, contact footer on cover/closing only). Fade/Zoom/Appear/Fade-out animations only, step-by-step builds, timed script in notes and `presentation/speaker-script.md` (~5:00 at 140 wpm). Rebuild: `presentation/build/build_deck.py` (`--static` for the PDF variant).
* **Market size:** verified DataReportal Digital 2026 Iraq (39.6M internet users, 83.8%) and ECDB Iraq e-commerce 2025 (US$1.32B); used on the Target Market slide. The $2.5–3.5B TAM in `entrepreneurship/02` could not be verified and was kept off slides.
* **Evidence corrections (re-checked against screenshots):** panomobi Anker post is 90,000 discounted from 120,000 (not a range; dated Apr 24); Miswag grid `225751` contains two "Anker Zolo" listings (120,000 model unconfirmed, 52,250 different model) plus A1695 at 137,200 and 135,000; Instagram Anker posts dated Apr–Oct 2026; HX80 Instagram seller is in Diwaniya, not Duhok; vacuum listed by Miswag as VAC351004. The "price ranges" defect was removed — catalog now 14 defects.

### [2026-10-21] — Finance Model Corrected (ADR-014) + Pitch Deck Green-Lit

* **Finance correction:** the per-order incentive accrual (−600) double-counted the capped incentive pool already in monthly burn; `finance/01` line items summed to −935 vs. the stated −425. Counted once → variable −335, **contribution +1,115 IQD/order**, break-even **~585/mo (~20/day)**. Planning: trough −3.27M (~$2,180) M3, break-even M4, recovery M8; upside ~$1,800; floor ~$2,750. Synced `finance/01–04`, canvas, SOPs, risk matrix. $7,500 ask unchanged.
* **Also fixed:** `finance/04` KPI said 3,000 orders *per month* (→ 3,000+ in the first 6 months; ~1,350/mo by M6); the canvas "promoted placement" revenue line contradicted the non-pay-to-play Best Value rule (→ off-platform social-ad showcases, ranking never for sale); stale survey counts in canvas/SOPs (41% / 13 → ~52 actionable / ~8 valid leads); `02` sensitivity rows recomputed.
* **Pitch rules updated (founder):** slide count flexible, total under 6 minutes; minimal text, visuals + step-by-step animations; archived deck styling not reused — only the template's GIZ/CAPA header + CAPA/AUK footer (full on cover/closing, smaller header only on content slides). Recorded in rules.md (13), AGENTS.MD, preferences.md (33), roadmap, active-tasks.

### [2026-10-21] — Survey Deep-Analysis + Contact-Quality Audit (corrections applied)
* Wrote full analysis at `entrepreneurship/assets/evidence/survey-analysis.md`: per-question normalization across 3 language blocks, frequency/awareness/intent cross-tabs, language cohorts, limitations.
* **Audit corrections propagated to all docs:** raw counts overstated leads — beta "74" → **~52 actionable** (38 phone + 14 IG handles; rest = names/refusals); pilot "13" → **~8–9 valid store leads** (refusals, one "keep it up" message, عالم الأطفال duplicate removed). Fixed in `05` §7, `04`, `03`, `business-modeling/01`+`03`, `active-tasks`.
* **Insight:** app-intent is highest (93%) among shoppers who *always* see price gaps — pain-awareness predicts demand.
* Platform UI attributions corrected per founder: Anker 225624 = **iBazzar** (not Amal), ASUS 132436 = **Elryan**, ASUS 132423 = **Amal (defunct — flagged everywhere)**; Xiaomi grid confirmed **iBazzar** → intra-app duplication now documented on 2 of 3 live competitors. UI-signature legend added to evidence README.

### [2026-10-20] — Evidence Archive Restructured & Expanded (founder) + Repo Wired
* **Founder restructured** screenshot evidence into `entrepreneurship/assets/evidence/<case>/` folders — 6 documented cases:
  * **Anker A1695 25K/165W (flagship):** 90,000–200,000 IQD across IG sellers, iBazzar (134k), Miswag — **122% spread**, incl. 100k vs 200k *inside Miswag's own search grid*. Corrections applied post-review: `225624.jpg` = **iBazzar** (not Amal); ASUS `132436.jpg` = **Elryan**; ASUS `132423.jpg` = **Amal — platform now defunct** (flagged as historical capture everywhere)
  * ASUS monitor 116,721–163,350 (40%, 3 sources) · Newal VAC-3510 95k vs 133,250 (40%, IG cheaper) · Hoco HX80 25k vs 35,280 (41%, IG cheaper) · Xiaomi 165W 60k vs 70k intra-app · +2 "DM for price" no-price posts (qualitative)
  * Survey CSV moved to `entrepreneurship/assets/evidence/`; **per-folder extraction notes** (`README.md` per case) + **master analysis** at `assets/evidence/README.md` cataloging **15 distinct market defects** (price spread, duplicates, hidden prices, price ranges, unstructured captions, fake anchors, obscured sellers, delivery bundling, sparse reviews, thin listings, slow delivery, manual ordering, AI-content sellers, BNPL-on-inflation, competitor self-admission) each mapped to Cheapify's mechanism
* **Path syncs:** all `assets/evidence/price-variation/` references updated in `01`, `02`, `04`; `02` §5.4 rewritten with all 6 cases; `05` dataset path updated; `rules.md`/`preferences.md` example paths corrected; `active-tasks` item closed.

### [2026-10-20] — Pillar 4 Complete: Business Modeling (All 4 Pillars Built)

* **Created `business-modeling/` — three documents:**
  * [`01_business_model_canvas.md`](../business-modeling/01_business_model_canvas.md): 9-block canvas, evidence-backed — survey stats (97%/88%/41%/13-merchant pilot), verified courier quote, waitlist as key resource. Records the moat = single-SKU catalog, and the one critical path: registration → courier contract → delivery margin.
  * [`02_core_sops.md`](../business-modeling/02_core_sops.md): SOP-1 merchant onboarding (self-serve 8-step, QA <2h, 10-order activation gate), SOP-2 order→3PL→delivery→weekly-settlement (failed-delivery branch, COD custody flag), SOP-3 returns (48h window, fault/remorse split, serial-returner flagging). Every step tagged [auto]/[manual]/[courier].
  * [`03_operational_risk_matrix.md`](../business-modeling/03_operational_risk_matrix.md): 17 risks scored Likelihood×Impact — top: R4 bypass (16), R1 traction (15), R2/R11 contract chain (12 each), R7 failed deliveries (12). Weekly/monthly/gate review cadence defined.
* **Milestone:** all 4 program pillars now built from ground zero — next deliverable per roadmap: the 6-minute pitch deck.
* **Founder deferrals noted in `active-tasks.md`:** pilot-merchant outreach, courier contract signing ("open anytime"), second Kurdish-boosted survey wave — all deferred to later; no blockers on deck work.

### [2026-10-20] — Market Validation Survey Analyzed (n=199) — First Large-Scale Evidence

* **Dataset:** [`assets/evidence/market-validation-survey-oct2026.csv`](../assets/evidence/market-validation-survey-oct2026.csv) — 199 responses (168 AR / 21 EN / 10 KU): **179 shoppers + 20 merchants**. Results written into `entrepreneurship/05` §7.
* **Shopper findings:** **97% notice price differences** (39% always see large gaps); **88% would use a comparison app** (2% prefer DMs); **74 left beta contacts (41%)** — real waitlist seed, zero CAC. Top annoyances: unverified/duplicate pages ~52%, cheaper-after-buying ~47%, DM price interrogation ~46%, delivery delays ~27%.
* **Merchant findings:** **75% platform-interested**; **13 signed up for the pilot (65%)** — founding cohort target (5–10) already met with spares; 85% sell via IG/FB. Top headaches: price-DM replies ~55%, random price competition ~45%, own-app cost ~35%, manual delivery coordination ~35%.
* **Syncs:** `marketing/01` §8 DM-ghost row → survey-verified; `finance/04` viability + KPI baselines now cite measured waitlist; `finance/03` order-ramp open item notes the seeded waitlist. The 13 merchant contacts = founding-cohort candidate list (extract for outreach).
* **Limitations recorded:** Kurdish sample thin (10/199) — Badînî underrepresented vs Duhok population; survey intent ≠ conversion — concierge pilot still decides.

### [2026-10-20] — Desk Research + First Merchant Interview (More Real Data)
* **OTP/messaging costs desk-verified:** OTPIQ (Iraqi-local provider) — WhatsApp OTP **40 IQD/msg**, SMS OTP **80–100 IQD (Korek/Asiacell), 250 (Zain)**; Meta moved to per-message pricing Jul 2025 (utility ~$0.01–0.02). SMS is 3× the assumed cost → OTP routing changed to WhatsApp-first with SMS fallback (blended ~50 IQD). A6/A7 marked `[DESK-VERIFIED]`.
* **Merchant interview n=1 (A9):** ~30 orders/mo total DM volume — 2× the planning assumption per store, but Cheapify capture is still a slice of it. Failed deliveries confirmed real ("buyer not home"); returns honesty-dependent.
* **Strategic finding:** merchant already runs a **competitor's affiliate bio link** — proves the bio-link acquisition channel exists AND is contested (bio slot is scarce real estate). No platform-commission baseline → our 3.8% has nothing to defend against. Positive reaction to the Cheapify concept.
* **ZMC Express verified via search:** Dubai-HQ international freight company **but Iraqi-founded with a real Duhok branch + COD services + 11 Iraq branches** → repositioned: Fast Delivery = pilot/intra-city partner, ZMC = inter-city/Phase-2 linehaul. ~20 doc references updated accordingly; entrepreneurship/02 evidence table now cites the real Fast Delivery quote.

### [2026-10-20] — A1 Courier Cost Verified: First Real Quote (Fast Delivery)
* **Fast Delivery (Duhok) quote:** list 3,000 city / 4,000 surroundings → **contract −500/order** → rates 2,500 / 3,500, far zones (Zakho) ~4,500. Three-zone fee structure proposed in `operational_policies` §2: **Zone A 3,000 / Zone B 4,000 / Zone C 5,000 — uniform +500 margin per zone** (customer pays cost+500).
* **Consequences:** A1 validated exactly; unsigned = zero margin in-city (contribution ~525, break-even ~1,240/mo) → **registration → contract is now critical-path**. Zakho tier confirmation + second courier quote still open for leverage.

### [2026-10-20] — Slow-Adoption Floor Scenario Added (03 §4.2)
* Founder pushed further: even the planning ramp felt optimistic → added **~25%-ramp floor case**: trough −4.28M IQD (~$2,850) at M6, first green M7 (M6 burn bump raises break-even ~642→771), recovery ~M20+. Key insight recorded: **loss ceiling is burn (~$435/mo), not order volume** — slow adoption degrades to a grind, not a cliff. `01` §7 and `04` synced ($2,250–2,850 range).

### [2026-10-20] — Cash-Flow Scenarios Flipped: Planning = Conservative Ramp
* Founder flagged order projections as too optimistic → **the 50% ramp became the planning scenario**, the former base became the upside stretch case in `03` (§4.1). Planning milestones: cash-positive M5 (~1,000 orders/mo), peak loss −3.37M IQD (~$2,250) at M4, recovery ~M9.
* `01` §6–7 mirror updated; `04` wording aligned ("planning-ramp trough") — the $7.5k ask was already derived from the conservative hole, so no tier changes needed. Per-store load note added: ~10–80 orders/merchant/mo, honest about Cheapify capturing a slice of DM-era volume.

### [2026-10-20] — Program Constraints Update: Ranked Awards + 6-Minute Pitch

* **New program facts recorded:** GIZ awards are ranked (1st > 2nd > 3rd prize amounts); final pitch has a hard 6-minute limit. Recorded as Rule 13 in `rules.md` + `AGENTS.MD`, added to `project-context.md`, `roadmap.md` (pitch-deck row: ~7–9 slides max, must win on merit), and `active-tasks.md`.
* `finance/04` tiers mapped to rank outcomes: Full ($7,500) = 1st place, Core ($4,500) = 2nd, Minimum ($2,500) = 3rd — any rank yields a complete plan.
* **Finance docs synced:** `01` §6–7 updated to match `03`'s current model — dev burn 210k/mo, M3 +168k, M6 +1.98M, break-even ~642 orders/mo, capital need restated as peak cumulative deficit (2.76M base / 3.37M conservative) with `03` marked as the authoritative timeline. (Earlier figures in this log reflect the pre-sync model.)

### [2026-10-20] — GIZ Funding Request (Pillar 3, File 04)

* **Created** [`finance/04_funding_request.md`](../finance/04_funding_request.md): competitive grant ask — top 3 of 20, envelope and criteria unknown → tiered ask ($7,500 full / $4,500 core / $2,500 minimum) derived bottom-up from the model (peak need $2,250 + validation $100 + growth $2,500 + registration $1,000 + onboarding $900 + 15% contingency).
* **Founder co-investment ~$9,500** (equipment, domain, sweat equity, dev burn) — grant ≈ 44% of total investment, the leverage frame.
* Use-of-funds tied to milestones (validation gate → launch → cash-positive → expansion); universal grant criteria covered; §6.1 experiments positioned as the de-risking differentiator; KPI table for funder reporting.

### [2026-10-20] — Cash Flow & Break-Even Model (Pillar 3 Complete, v1)

* **Created** [`finance/03_cash_flow_and_breakeven.md`](../finance/03_cash_flow_and_breakeven.md): 12-month projection — Phase A (2mo, ~210k/mo dev burn incl. modest audience ads) → launch (652k/mo operating burn) → pilot ramp. Milestones: first cash-positive month M3 (~800 orders), peak cumulative loss ~2.76M IQD (~$1,840) at M2, full recovery M6 (~2,700 orders/mo). Break-even = ~642 orders/mo (~21/day) at +1,025 IQD contribution; levers to lower it documented as options-not-adopted (commission kept at 3.8%).
* **Honest caveats recorded:** pilot target of 150 orders/store/mo is aggressive; model collapses if courier A1 > ~3,425 IQD. **Conservative scenario (50% ramp) added:** peak loss ~3.37M IQD (~$2,250), recovery ~M9 — bounded downside. **Validation experiments specified** (courier quote, 10–20-order concierge pilot, merchant audience audit) as the real de-risking lever, since modeling alone can't reduce traction risk.
* **Pillar 3 status:** all three finance docs complete at assumption-driven v1 — blocked only by real-world quotes, not modeling.

### [2026-10-20] — Unit Economics Model v1 (Pillar 3)

* **Created** [`finance/02_unit_economics.md`](../finance/02_unit_economics.md): shopper LTV ~11,100 IQD vs blended CAC ~1,500 (≈7.4:1, payback 1–2 orders); merchant LTV ~103,000 IQD vs CAC 5–10k (10–20:1); founding-store package (~65k IQD) justified as joint merchant+audience acquisition. Sensitivity table: A1 courier cost and AOV are the make-or-break inputs.

### [2026-10-20] — Pillar 3 Started: Operational Budget v1

* **Created** [`finance/01_operational_budget.md`](../finance/01_operational_budget.md) — assumption-driven model with a 12-item Assumptions Register (A1–A12), one-time startup costs (~1.5–1.9M IQD), monthly baseline burn (~562k IQD), per-order contribution math (+1,025 IQD/order at AOV 25k), break-even ~550 orders/mo, and 6-month capital need ~4.6M IQD (~$3,060).
* **Key sensitivity flagged:** if the real Duhok courier cost exceeds ~3,500 IQD/parcel, the 3,000 IQD flat delivery fee turns per-order contribution negative — the #1 quote to collect.
* **Added §3.1 Founder-Contributed Resources:** domain (paid), PC, smartphone, internet, electricity/workspace, founder labor — valued as in-kind contributions, $0 cash impact; they graduate to cash budget if they lapse.

### [2026-10-20] — Operational Policies Drafted (ADR-013)

* **Created** [`platform/operational_policies.md`](../platform/operational_policies.md) covering all items in the founder's `to-consider.md`: two-class returns (fault→merchant pays, remorse→customer pays, 48h window), flat 3,000 IQD Duhok shipping inside Doorstep Total, mandatory sealed packaging + security tape ≥50k IQD, COD-primary payments with weekly settlement + Phase-3 e-wallets, then split into a sibling doc [`platform/catalog_governance.md`](../platform/catalog_governance.md) holding listing process, the 8-rule listing policy, and the 4-layer duplicate-prevention strategy.
* Every section marked **[Policy]** vs **[Assumption]**; §5 lists the real-world data needed (courier quotes, remittance terms, return-rate baseline) — all feed Pillar 3 finance work.
* **Referral spec finalized:** referrer-only rewards (3k shopper / 3-free-deliveries merchant-nomination / growth points / flat 10k merchant-recruit credit); percentage rebate rejected as unbounded.
* **Assumption audit:** added "Open Items Requiring Real-World Data" registers to six docs — `01_two_sided_gtm_strategy.md` (§8), `fee_structure_and_monetization.md`, `referral_and_growth_incentives.md` (§9), `best_value_algorithm_strategy.md`, and both content plans — so every unverified figure (courier costs, competitor commissions, ghost rate, algorithm weights, KPI targets) is tracked in one place per doc.
* **Doc boundary cleanup:** catalog mechanism details (first-mover problem, barcode-first flow, shared-ownership/edit-proposal model) moved from `referral_and_growth_incentives.md` §4 into `catalog_governance.md` §1 & §3; the incentives doc retains only the bounty economics.

### [2026-10-18] — Referral & Catalog Incentive Architecture (ADR-012)

* **Designed the four-direction referral system** ([`platform/referral_and_growth_incentives.md`](../platform/referral_and_growth_incentives.md)): all rewards gated on completed courier-confirmed orders — never signups — paid in non-transferable platform credit. Directions: Shopper→Shopper (free 1st delivery + 3k credit), Shopper→Merchant (nominate a shop → 3 free deliveries after 10 orders), Merchant→Shopper (free delivery + growth points → ad boosts on Best Value winners), Merchant→Merchant (1% rebate 60d). Anti-fraud stack: OTP, velocity caps, device/address heuristics, courier failure signals.
* **Solved catalog first-mover asymmetry:** barcode-first creation (auto-fill from product DBs, template fallback for unbranded), 1,000 IQD creation bounty (commission-offset credit, founder-set), 250 IQD improvement micro-bounty, permanent creator attribution with shared editable-via-proposal master pages. Platform catalog seeding rejected by founder — catalog is 100% merchant-built.
* Cross-linked from the launch calendar (Week 6 referral push) and GTM playbook.

### [2026-10-18] — Two-Phase Social Content Strategy Complete (Pillar 2)

* **Decisions (founder):** post on social media *before* the MVP exists (audience-building only, no launch promises); same content published to Facebook + Instagram + TikTok; one multilingual post per drop (never separate-language posts); Duhok launch videos in Kurdish audio with a single Kurdish burned-subtitle track and Arabic in the caption; no English; two stacked subtitle tracks rejected. Recorded as ADR-011 and Preferences 28–30.
* **Created** [`marketing/03_pre_launch_content_plan.md`](../marketing/03_pre_launch_content_plan.md) — Phase A: repeatable weekly template (5 posts/wk) across five series (Price Detective, DM Hell, Founder's Circle, Build in Public, Bazaar Wisdom), 4-week starter cycle, unified cross-platform publishing model, language/subtitle policy, pre-publish brand checklist, Phase A KPIs, and the infrastructure needed before post 1 (waitlist page, profiles, templates).
* **Created** [`marketing/04_launch_content_calendar.md`](../marketing/04_launch_content_calendar.md) — Phase B: T-7 daily countdown, launch-week day-by-day plan, weeks 2–8 growth themes, merchant launch coordination, Phase B KPIs, and contingency rules.
* **New open tasks:** waitlist landing page, social profile setup, reusable series templates, start Phase A cadence.

### [2026-10-17] — Official Platform Domain Secured (`getcheapify.com`)

* **Milestone:** Secured **`getcheapify.com`** via Cloudflare Registrar as Cheapify's official root web domain, API host, and app download portal.
* **Strategic Selection:** Overcomes the unavailability of `cheapify.com` and `cheapify.app` while leveraging maximum `.com` subconscious trust across everyday Iraqi/Kurdish consumers, eliminating typo leakage risks, and establishing an action-oriented product verb (*"Get Cheapify"*).
* **Governance Sync:** Documented in [`agent/preferences.md`](preferences.md) (Preference 27) and [`agent/decisions.md`](decisions.md) (ADR-010).

### [2026-10-17] — Brandbook Moved to Root + White-on-Orange Rule

* **Structure:** `marketing/brandbook/` moved to [`brandbook/`](../brandbook/index.html) at repo root (a finished deliverable, not working docs). Made self-contained: referenced files copied to `brandbook/assets/` (logo SVGs, PDF, brand-tokens.json); all `../../` links replaced.
* **Color rule change (founder decision):** text on Flash `#FFA300` and Warning `#FF8200` surfaces is now Pure White instead of Ink — applied to badges (`b-flash`, `b-warn`), semantic swatches, and the misuse sticker. Contrast table updated: "White on Flash 137 C" shown as 2.00:1, "Display Only". Rule documented in spec §6.2 — restricted to large bold short-lived UI, never body copy.

### [2026-10-17] — Brandbook CSS Externalized & Cover Slogan Fix

* **Action:** Moved all 6 `<style>` blocks and all 541 inline `style` attributes out of [`brandbook/index.html`](../brandbook/index.html) into an external [`brandbook/brandbook.css`](../brandbook/brandbook.css) (design system + 322 extracted utility classes). Verified pixel-identical rendering across all 16 sections; 0 CSS diagnostics.
* **Cover:** Kurdish and Arabic slogans now both translate the headline ("The bright side of choosing"); the English tagline moved to its own line. Removed the extra blue stripe from the mug illustration.
* **Founder correction applied:** Kurdish term for Best Value changed to «هەری باش».
* **Scaling behavior:** responsive reflow replaced by proportional scaling — the page is laid out at a fixed 1414px design width and, below that viewport width, the whole layout (sidebar + content) scales down uniformly via `transform: scale()`. The 1280px/960px media-query blocks were removed from `brandbook.css`. Verified at 1600/1200/900px widths.

### [2026-10-17] — Brandbook Revision per Founder Review (11 Notes)

* **New rules recorded** (Rules 11–12 in [`rules.md`](rules.md), Rules 10–11 in [`AGENTS.MD`](../AGENTS.MD)): Kurdish always in Kurdish Arabic-based script; no internal development content in external deliverables.
* **Brandbook changes** ([`brandbook/index.html`](../brandbook/index.html)): removed all pillar/deliverable/ADR/preference/roadmap/file-path/source-of-truth content (incl. Section 15 Roadmap and Governance Records cards); converted every Kurdish string to Kurdish script (RTL, IBM Plex Sans Arabic); fixed nav pill wrapping; aligned Tier 2 tagline tables; split the logo's upward arrow from the bag into separate vector symbols and equalized the exploded-anatomy cards; black logo/wordmark on the kraft bag; white check seals on the security tape; decal spacing; do/don't text padding; redrawn polo and mug illustrations; renumbered sub-sections.
* **Spec sync:** Converted Kurdish strings in [`marketing/02_brand_identity_and_guidelines.md`](../marketing/02_brand_identity_and_guidelines.md) to Kurdish script and removed emoji check/cross marks.
* **Pending:** Native-speaker proofread of the Kurdish-script copy.

### [2026-10-17] — Official HTML Brandbook Published (Pillar 2 Milestone)

* **Action:** Built [`brandbook/index.html`](../brandbook/index.html) — a complete, single-file, interactive brandbook rendering the full brand specification from [`marketing/02_brand_identity_and_guidelines.md`](../marketing/02_brand_identity_and_guidelines.md), itself designed in the official "Clean Flat + Soft Depth" language.
  * **15 sections:** Foundations, Voice & Tone (trilingual matrix + lexicon), Taglines, Logo System (anatomy, exploded parts, outline vs. solid hierarchy, 6 lockups, 8 color variations, scaling, clear space), Logo Misuse (8 rendered violations), Color (PMS swatches, semantic + tint tokens, 60-30-10, computed WCAG contrast), Typography (3 live specimens, type scale, tabular numerals, currency formatting), UI Design Language (elevation, radius, prohibited treatments, bento + dark mode, Best Value badge, buttons, comparison card, phone mockup, app icon/favicon), Iconography (Zero-Emoji Rule, sources, grid, core library), Photography, Physical Collateral (mailer, kraft bag, security tape, window decal with QR, thermal waybill), Co-Branding & Social Ads (IG, FB, TikTok frames, spelling policy), Brand Applications (business cards, letterhead, email signature, splash screens, avatars, cover banner, brand pattern, billboard, merchandise), Governance (asset downloads, CSS tokens, interactive 10-point audit), and Roadmap.
  * **Logo variants** are generated live from the master SVGs in `assets/` via inline SVG symbols with CSS-variable recoloring — no hand-redrawn logos.
  * **Zero emojis**; all iconography via Lucide (pinned v0.460.0). All 89 icon names validated against the library.
  * **Accessibility finding:** Computed WCAG ratios show PMS 7731 C on white = **4.48:1** and PMS 7689 C on white = **3.62:1** (the Markdown spec lists 5.2:1 and 3.2:1). The brandbook shows the computed values.

### [2026-10-17] — Official UI Design Language Selected: "Clean Flat + Soft Depth" (ADR-009)

* **Action:** Researched current design-trend directions (Figma 2026 web design trends + industry e-commerce UI analyses) and built a live evaluation page, [`assets/design-style-previews/index.html`](../assets/design-style-previews/index.html), rendering the same product comparison card in **8 candidate styles** using the official PMS palette and brand fonts: Clean Flat + Soft Depth, Vibrant Dopamine, Neumorphic Fintech, Gamified Deal-Hunting, Bento Grid 2.0, Glassmorphism/Liquid Glass, Claymorphism, and Editorial Minimal/Zero-UI.
* **Founder Decision:** Selected **"Clean Flat + Soft Depth"** as Cheapify's official UI design language — flat white surfaces on neutral backgrounds, single diffuse shadows, generous 12–16px radii, and disciplined PMS blue/green accent usage, prioritizing price-table readability and trilingual accessibility for mass-market users.
* **Codified:** New Section **8.0** in [`marketing/02_brand_identity_and_guidelines.md`](../marketing/02_brand_identity_and_guidelines.md) defining core principles, the 3-level elevation scale, corner radius tokens, explicitly prohibited treatments (glassmorphism, neumorphism, claymorphism, neo-brutalist stickers, dopamine gradients, gamification HUD chrome), and approved optional patterns (flat bento stat tiles, dark-mode theme variant).
* **Governance:** Recorded **ADR-009** in [`agent/decisions.md`](decisions.md) and **Preference 25** in [`agent/preferences.md`](preferences.md).
* **Iconography Rule Established:** The founder mandated the **Zero-Emoji Rule** — emojis are banned across all UI, documents, marketing, and communications; only vector icons (custom-drawn per §9.1 spec or free CDN libraries: Lucide, Phosphor, Heroicons, Iconify) may be used. Recorded as **Rule 10** in [`AGENTS.MD`](../AGENTS.MD), **Preference 26** in [`agent/preferences.md`](preferences.md), and new **§9.0** in the brand guidelines. The style preview page was retrofitted to Lucide CDN icons for compliance.

### [2026-10-17] — Brand Identity & Visual Design Guidelines Authored (Pillar 2 Milestone)

* **Action:** Authored [`marketing/02_brand_identity_and_guidelines.md`](../marketing/02_brand_identity_and_guidelines.md) locking in Cheapify's visual identity and design system built collaboratively with the founder:
  * **Strict Pantone (PMS) Color System:** Standardized the 4 official PMS colors from `assets/Cheapify-LOGO.pdf`: Primary Blue (**PANTONE 7689 C** / `#298FC2`), Value Accent Green (**PANTONE 7731 C** / `#228848`), Dark Base Ink (**PANTONE BLACK 6 C** / `#101820`), and Light Surface Neutral (**PANTONE 656 C** / `#DDE5ED`).
  * **Logo Mark Hierarchy:** Confirmed the **Outline / Stroke construction** as the primary official brand mark across all digital applications, web platform, and mobile app launcher icons (with the solid silhouette reserved strictly for specialized physical manufacturing), defining the master 700x900px grid and exclusion zone.
  * **Tri-Font Typographic Architecture Deployed:** Deployed **Comfortaa** (Display & H1 headers), **Inter** (Latin UI, product specs, tabular numerals for pricing), and **IBM Plex Sans Arabic** (universal Kurdish Badînî/Sorani and Standard Arabic UI with complete native Unicode glyph support).

  * **Dual-Tier Tagline Architecture:** Formalized the Brand Soul (*The bright side of choosing* / *«Rûyê geş yê helbijartinê»* / *«الجانب المشرق للاختيار»*) and the Functional Conversion Hooks (*Find your best deal* / *Smart Deals. Verified Sellers. One App.*).
  * **UI Component & Ad Specs:** Defined the signature "Best Value" badge tokens, primary button states, comparison table styling, and co-branded merchant ad templates for Facebook, Instagram, and TikTok.

### [2026-10-16] — Two-Sided GTM Strategy & Execution Playbook Authored (Pillar 2 Milestone)

* **Action:** Authored and refined [`marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md) establishing Cheapify's go-to-market operational playbook:
  * **Platform Architecture Clarified:** Formalized that Cheapify is engineered as both a **mobile application (iOS & Android)** and an accessible **web platform** ([Preference 20](preferences.md)).
  * **Core Channels Refined:** Focused marketing and social commerce funnels on **Facebook, Instagram, and TikTok**, excluding Telegram from active focus ([Preference 21](preferences.md)).
  * **Self-Serve with Rules Onboarding:** Established that Cheapify sets strict quality standards, rules, and instructions, while merchants build and upload their own product listings and media via the self-serve merchant portal ([Preference 22](preferences.md)).
  * **Free Paid Ad Boosts for Founding Stores:** The first 20 verified stores receive 0% commission in Month 1 and get their products featured in Cheapify's paid ad campaigns across Facebook, Instagram, and TikTok ([Preference 23](preferences.md)).
  * **Broad Mass-Market Consumer Scope:** Expanded demand engine beyond university students to encompass young working professionals, household shoppers, civil servants, and deal-conscious families ([Preference 24](preferences.md)).
  * **Phased Geographic Horizon:** Structured the 3-phase rollout (Phase 1 Duhok Launchpad, Phase 2 Regional KRI/Nineveh Hubs, Phase 3 Nationwide All-Iraq Scale).

### [2026-10-16] — Stage 1 Merchant Onboarding Staged: Social Media Native Stores First

* **Action:** Recorded strategic operational milestone following founder guidance:
  * **Social Media Stores as Stage 1 Launchpad:** Prioritized Instagram, TikTok, and Telegram merchants over offline physical shops for the initial pilot phase.
  * **Key Advantages Formalized:** Zero catalog creation friction (ready photos, reels, specs), e-commerce native operational habits (courier booking, COD), acute DM exhaustion ("Interrogation Tax"), and organic two-sided traffic generation (merchants putting Cheapify links in bios).
  * **Governance Synchronized:** Added Preference 19 to [`agent/preferences.md`](preferences.md) and accepted ADR-008 in [`agent/decisions.md`](decisions.md).

### [2026-10-15] — Hybrid "Best Value" Algorithm Strategy Specification Authored

* **Action:** Authored [`platform/best_value_algorithm_strategy.md`](../platform/best_value_algorithm_strategy.md) establishing Cheapify's core product ranking architecture:
  * **Hybrid "Total Landed Cost + Proximity Advantage" Model:** Solved the trade-off between consumer doorstep affordability ($P_{\text{total}} = P_{\text{item}} + D_{\text{tariff}}$) and merchant transparency.
  * **Intra-City Bazaar Competition:** Documented that within the same metropolitan zone (e.g. Duhok to Duhok), flat courier tariffs (3,000 IQD) make Total Landed Cost ranking 100% identical to sticker price ranking, allowing local merchants to compete directly and transparently on retail prices.
  * **Inter-City Defense for Local Shops:** Demonstrated how distance tariffs create an organic economic defense for local neighborhood shops against out-of-city dumping, requiring distant vendors to provide authentic discounts that exceed the freight differential.
  * **Deterministic 3-Tier Multi-Attribute Priority Cascade:** Priority 0 (Lowest Total Landed Doorstep Price) $\rightarrow$ Priority 1 (Fastest Delivery Speed by Proximity Zone) $\rightarrow$ Priority 2 (Verified Merchant Operational Reliability & Quality Score).
  * **Logistics Distance Matrix:** Mapped 4 delivery zones (Hyperlocal 1–3h / 3k IQD, Intra-City 3–6h / 3k–3.5k IQD, Regional Inter-City 24–48h / 5k IQD, Nationwide 48–72h / 6k–7k IQD).
  * **Merchant Dashboard Diagnostics ("Why Didn't I Win?"):** Designed the wireframe and trilingual guidance (Badînî Kurdish, Arabic, English) giving merchants clear explanations and actionable pricing suggestions.
  * **Production TypeScript Engine:** Implemented pure, fully typed sorting function (`evaluateBestValueOffers`) with comprehensive unit interfaces.
* **Governance & Brand Identity Directives Updated:**
  * Formally updated ADR-007 in [`agent/decisions.md`](decisions.md) with the Hybrid Model.
  * Formally recorded Preference 18 in [`agent/preferences.md`](preferences.md) retiring all legacy brand colors ("Jade Green", `#148C53`, "Boston Blue") and mandating brand visual identity be built 100% fresh from ground zero in Pillar 2 (Marketing).
  * Synchronized [`AGENTS.MD`](../AGENTS.MD) and [`agent/active-tasks.md`](active-tasks.md).

### [2026-10-15] — Value Proposition Canvas, Innovation & Founder-Market Fit Authored

* **Action:** Authored [`entrepreneurship/06_value_proposition_and_founder_fit.md`](../entrepreneurship/06_value_proposition_and_founder_fit.md) providing the formal academic and incubator bridge between personas and solution architecture:
  * **Osterwalder Value Proposition Canvas (VPC):** Systematically mapped Customer Jobs, Pains, and Gains against Cheapify's Products, Pain Relievers, and Gain Creators for both the Deal-Seeking Shopper (Ahmad) and the Bazaar Merchant (Kak Kawa).
  * **Technological & Process Innovations:** Formulated Cheapify's 4 core innovations: Single-SKU aggregation vs feed clutter, the multi-variable "Best Value" algorithmic ranking engine, WhatsApp Cloud API automated waybill generation, and progressive marginal fee settlement.
  * **Founder-Market Fit & Execution Capabilities:** Documented founder background (Shakir Bashar, Computer Engineer, former IT Manager & COO), technical execution ($0 software development agency costs), capital discipline (available seed funding deployed 100% to external ops), and operational resilience in Iraqi COD retail.
  * **Pillar 1 Completeness Audit:** Formulated an 11-point audit matrix proving that every theoretical and practical requirement of the GIZ Youth Entrepreneurship curriculum is 100% fulfilled.

### [2026-10-15] — Trilingual Market Validation Survey Framework Authored (Milestone 1 Complete)

* **Action:** Authored [`entrepreneurship/05_market_validation_survey.md`](../entrepreneurship/05_market_validation_survey.md) capturing the live empirical research framework currently collecting responses:
  * **Clean Non-Code Presentation:** Documented the full survey instrument cleanly across Kurdish (Badînî), Arabic, and English without raw script code blocks, adhering to user direction.
  * **Dynamic Dual-Cohort Logic:** Formulated the branching architecture: Language Selection $\rightarrow$ Role Branching (Shopper vs. Merchant) $\rightarrow$ Targeted Problem/Solution Validation $\rightarrow$ Pilot Beta & Merchant Store Lead Capture.
  * **Hypothesis Testing Grounding:** Mapped each question directly to venture hypotheses (H1 Price Variation prevalence, H2 "Interrogation Tax" fatigue, H3 Single-SKU comparison demand, H4 Seller chat burnout, H5 Turnkey dashboard adoption).
  * **Live Distribution & Pipeline Feeder:** Documented outreach channels (AUK/UoD student Telegram groups, in-person Duhok bazaar merchant visits with QR codes, in-app social media links with Google sign-in toggled off) and mapped how incoming responses feed Marketing (Pillar 2), Finance (Pillar 3), and Business Modeling (Pillar 4).
* **Milestone 1 Achieved:** Pillar 1 (Entrepreneurship) is now **100% complete** across all 5 core foundation deliverables.

### [2026-10-15] — Competitive Landscape Matrix & Strategic Differentiation Authored

* **Action:** Authored [`entrepreneurship/04_competitive_landscape_matrix.md`](../entrepreneurship/04_competitive_landscape_matrix.md) establishing Cheapify's market positioning and defensibility:
  * **Head-to-Head Profiling:** Analyzed 4 incumbent alternatives across Iraq/KRI: Social Commerce DMs (Instagram/TikTok), Miswag (10%–15% commission, slow inter-city delivery), Elryan (closed 1P retail, rigid MSRP), and iBazzar (open 3P, duplicate SKU clutter, intra-app 10k price gaps).
  * **Comprehensive 12-Dimension Matrix:** Contrasted catalog architecture (Single-SKU master page), price transparency, variant chip selectors, 1-click checkout (<30s), local payment integrations (COD + FIB/FastPay/Qi Card), hyperlocal 3PL intra-city delivery (ZMC Express 3,000 IQD), take-rate (1.5%–5% progressive vs. Miswag 12%), and merchant dashboard.
  * **Core Moats Documented:** The Single-SKU flywheel (each new seller drives down price rather than adding visual clutter), in-house software agility ($0 dev fees by founder Shakir Bashar), asset-light 3PL courier integration, and merchant margin protection.
  * **Strategic Positioning Map:** Formulated 2x2 matrix (Price Transparency vs. Automated Structured Commerce), placing Cheapify firmly in the top-right quadrant.

### [2026-10-15] — Platform Fee Architecture & Monetization Specification Created

* **Action:** Created dedicated cross-cutting platform artifact [`platform/fee_structure_and_monetization.md`](../platform/fee_structure_and_monetization.md) in a new semi-general directory `platform/`:
  * **Progressive Marginal Tiering Model:** Formulated the 3-tier progressive take-rate to completely eliminate the cliff effect (where a higher price would otherwise pay a lower fee):
    * **Tier 1 (1 to 10,000 IQD):** 5.0% (max 500 IQD)
    * **Tier 2 (10,001 to 100,000 IQD):** 3.0% (max 2,700 IQD)
    * **Tier 3 (100,001+ IQD):** 1.5%
  * **Cliff Effect Mathematical Analysis:** Included proof of strict monotonicity ($\forall P_2 > P_1 \implies \text{Fee}(P_2) > \text{Fee}(P_1)$), demonstrating that an item at 14,500 IQD costs 635 IQD while an item at 16,000 IQD costs 680 IQD.
  * **Multi-Category Simulation Table:** Benchmarked across 12 product tiers from cables (5,000 IQD) to high-end laptops (1,200,000 IQD), demonstrating 58% to 86% margin savings compared to traditional 12% platforms (e.g., Miswag).
  * **Engineering Reference:** Added TypeScript implementation function (`calculateCheapifyFee`) for the web MVP checkout engine and documented COD weekly net-reconciliation flow.
* **Governance Updated:** Formally accepted ADR-005 in [`agent/decisions.md`](decisions.md) and logged Preferences 14 & 15 in [`agent/preferences.md`](preferences.md).

### [2026-10-15] — Multi-Category Scope & Nationwide Scaling Horizon Re-architected

* **Action:** Restructured [`entrepreneurship/02_market_opportunity_and_sizing.md`](../entrepreneurship/02_market_opportunity_and_sizing.md) based on founder direction:
  * **Multi-Category Retail Expansion:** Broadened the platform scope beyond electronics to all standardized retail categories with price variations (Electronics; Home, Kitchen, Garden; Luggage, Bags, Watches, Perfumes; Beauty & Self-Care; Health; Cleaning; Business & Industrial; Study; Gifts; Musical; and more).
  * **Updated Sizing Metrics:** TAM calibrated to $2.5B–$3.5B+ USD across all Iraq; SAM expanded to $600M–$800M USD across multi-category goods in initial expansion zones.
  * **Progressive Geographic Scaling Horizon:** Formulated a 3-stage geographic rollout: Launchpad (Duhok) ──► Northern Regional Hubs (Erbil, Mosul, Sulaymaniyah) ──► Complete Nationwide Coverage across ALL of Iraq (Baghdad, Basra, and all governorates).
* **Governance Updated:** Recorded Preferences 11 & 12 in [`agent/preferences.md`](preferences.md) and synchronized [`agent/project-context.md`](project-context.md).

### [2026-10-15] — Institutional References & Evidence Added to Market Sizing

* **Action:** Added Section 5 ("Statistical Sources, Evidences & Research References") to [`entrepreneurship/02_market_opportunity_and_sizing.md`](../entrepreneurship/02_market_opportunity_and_sizing.md) providing exact, verified citations for every metric:
  * **Demographics:** World Bank, Iraq Ministry of Planning, and Kurdistan Region Statistics Office (KRSO).
  * **Digital Penetration:** DataReportal / Kepios Digital 2024 Iraq report (33.5M internet users, 42.1M mobile connections).
  * **E-Commerce & Social Commerce:** KAPITA Research ("E-Commerce in Iraq" & "Digital Payments"), International Trade Centre (ITC), and GIZ PSD reports confirming >80% social commerce via DMs and 85–90% COD.
  * **Logistics:** ZMC Express standard intra-city tariff (3,000 IQD).
  * **Price Disparity Evidence:** Directly linked the 4 repository screenshots in [`entrepreneurship/assets/evidence/price-variation/`](../entrepreneurship/assets/evidence/price-variation/) proving the ~47,000 IQD monitor disparity and 10,000 IQD intra-app Xiaomi disparity.
* **Governance:** Added Preference 10 to [`agent/preferences.md`](preferences.md) establishing mandatory evidence and citation standards for all future venture documentation.

### [2026-10-15] — Dual-Persona Deep-Dive Document Created

* **Action:** Authored [`entrepreneurship/03_customer_and_merchant_personas.md`](../entrepreneurship/03_customer_and_merchant_personas.md) capturing in-depth behavioral profiles and journey maps:
  * **Consumer (Ahmad, 23):** Final-year university student & part-time assistant in Duhok. Budget-conscious, values side-by-side transparency, hates "DM for price" and arbitrary markups. Journey mapped before vs. after Cheapify.
  * **Merchant (Kak Kawa, 34):** Owner of "Kawa Tech" in central Duhok Bazaar + Instagram page. Exhausted by repetitive DMs, suffers from inventory chaos across notebooks, needs turnkey dashboard and pre-qualified orders without heavy commissions.
  * Built cross-persona alignment matrix harmonizing pricing, information, ordering, and trust incentives.

### [2026-10-15] — Market Opportunity & Sizing Document Created

* **Action:** Authored [`entrepreneurship/02_market_opportunity_and_sizing.md`](../entrepreneurship/02_market_opportunity_and_sizing.md) to define and quantify the market opportunity across Iraq, the Kurdistan Region, and Duhok:
  * **TAM (Total Addressable Market):** $2.5B – $3.0B USD / year (Iraqi e-commerce, 44M population, 33M internet users).
  * **SAM (Serviceable Available Market):** $150M USD / year (Standardized tech & lifestyle accessories in KRI & high-density urban youth hubs).
  * **SOM (Serviceable Obtainable Market):**
    * 6-Month Pilot (Duhok): 3,000 orders, ~$100,000 USD GMV, $3,500 USD platform revenue across 5–10 verified stores.
    * Year 1 Target (Duhok + Erbil): 11,700 orders, ~$350,000 USD GMV, $14,000 USD platform revenue.
  * Defined market growth drivers (exhaustion with "DM for price", e-wallets, 3PL courier maturity) and the standardized beachhead SKU strategy (chargers, earbuds, gaming accessories first).

### [2026-10-14] — Price Variation Re-anchored as Primary Problem & Catalyst

* **Action:** Refined Section 1 and Section 2 of [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md), [`agent/project-context.md`](project-context.md), and [`agent/preferences.md`](preferences.md) to explicitly declare **Price Variation & Arbitrary Markups** as the primary genesis and core focus of Cheapify.
* **Refinement Details:** While Cheapify also resolves the "Interrogation Tax", missing specs/variants, and merchant data chaos, eliminating wild price disparities remains the primary value anchor and founding catalyst.

### [2026-10-14] — Best-Value Ranking Priority Hierarchy Standardized

* **Action:** Standardized the 3-tier algorithm hierarchy for awarding the "Best Value" badge across [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md), [`agent/project-context.md`](project-context.md), [`agent/preferences.md`](preferences.md), and logged ADR-007 in [`agent/decisions.md`](decisions.md).
* **The Hierarchy:**
  * **Priority 0 (Most Important / Primary):** Price (lowest price in IQD).
  * **Priority 1 (Secondary):** Delivery Time (fastest local delivery window).
  * **Priority 2 (Tertiary):** Rating and reviews (merchant reputation score).

### [2026-10-14] — Seller Data Management & Merchant Dashboard Integrated

* **Action:** Updated [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md) based on founder direction:
  * Added **Manual Data Chaos & Operational Blindness** to Section 1.3 (The Seller's Pain): Sellers struggle managing orders, inventory, and addresses in paper notebooks, WhatsApp threads, and messy spreadsheets.
  * Added **2.4 Centralized Merchant Operations Dashboard** to Section 2 (The Solution): Equipping sellers with a digital dashboard for stock control, live order pipelines, competitor price-drop alerts, and revenue tracking.
  * Updated Section 3.2 (Core Value for Sellers) with Turnkey Data & Operations Dashboard benefits.

### [2026-10-14] — Governance Architecture Refactoring & Ground-Up Sequencing

* **Action:** Refactored project governance into single-purpose, simple files inside [`agent/`](agent/) and locked in the ground-up 4-pillar build sequence.
* **New Directive Added:** Archived pitch decks (e.g. `Cheapify Pitch Deck.pdf`) are confirmed non-final and partial; planning will NOT depend on them. We build all 4 pillars from ground zero first (1. Entrepreneurship, 2. Marketing, 3. Finance Management, 4. Business Modeling), and assemble the final presentation only after all 4 pillars are complete.
* **Governance Files Maintained:**
  * [`agent/rules.md`](rules.md): Added rule for 4-pillar build order before final deck.
  * [`agent/preferences.md`](preferences.md): Documented ground-up construction workflow.
  * [`agent/roadmap.md`](roadmap.md): Updated strategic phases and table.
  * [`agent/decisions.md`](decisions.md): Added ADR-006.
  * [`agent/active-tasks.md`](active-tasks.md): Focused strictly on Pillar 1 completion.

### [2026-10-12] — Finance Management Pillar Completion (Archived)

* **Action:** Finalized full GIZ budget plan and financial model.
* **Files:**
  * `archive/finance-management/assignment/01_budget_plan_and_evidence.md`
  * `archive/finance-management/assignment/Cheapify_Budget_GIZ.xlsx`
  * `archive/finance-management/assignment/Cheapify_Monthly_Profit_and_Loss.xlsx`
  * `archive/finance-management/assignment/Cheapify_Budget_Plan_and_Evidence.pdf`
  * `archive/finance-management/assignment/Cheapify_Budget_Report.html`
* **Legacy Coursework Note:** Past assignment exercise numbers only; not final venture budget. Real financials to be built in Pillar 3.

### [2026-10-11] — Project Foundation & Rebuild from Ground Zero

* **Action:** Commenced fresh ground-up construction of Cheapify.
* **Files:**
  * [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md) drafted.
  * Core brand assets imported into `assets/` (`cheapify-logo.svg`, `brand-tokens.json`).
