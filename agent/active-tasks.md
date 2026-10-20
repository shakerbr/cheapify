# Cheapify — Active Tasks & Immediate Work Items

This document tracks immediate actionable tasks, active work items, and current blockers.

---

## Current Active Focus

* **Active Pillar:** All 4 pillars complete — next deliverable is the **final pitch deck** (`presentation/`, 6-min limit, ~7–9 slides)
* **Lead File:** `business-modeling/` docs finalized; deck assembly per `agent/roadmap.md` sequence

---

## Immediate Checklist

### Cross-Cutting Platform Specifications (`platform/`)

* [x] Formulate Progressive Marginal Tiering Fee Structure & Cliff-Effect elimination ([fee_structure_and_monetization.md](../platform/fee_structure_and_monetization.md))
* [x] Formulate Hybrid "Best Value" Algorithm Strategy (Total Landed Cost + Proximity Advantage) ([best_value_algorithm_strategy.md](../platform/best_value_algorithm_strategy.md))

### Milestone 1: Complete Pillar 1 (Entrepreneurship) — 100% Complete

* [x] Define Problem ("Interrogation Tax", missing colors/measures, information vacuum) ([01_problem_solution_value.md](../entrepreneurship/01_problem_solution_value.md))
* [x] Define Solution (Single-SKU catalog, Best-Value side-by-side comparison) ([01_problem_solution_value.md](../entrepreneurship/01_problem_solution_value.md))
* [x] Define Dual-Sided Value Proposition (Shoppers, Local Merchants, Iraqi Market) ([01_problem_solution_value.md](../entrepreneurship/01_problem_solution_value.md))
* [x] Add Market Sizing: TAM, SAM, SOM in Iraq & KRI ([02_market_opportunity_and_sizing.md](../entrepreneurship/02_market_opportunity_and_sizing.md))
* [x] Add Dual-Persona Deep-Dive: Consumer (Ahmad) & Merchant (Kak Kawa) ([03_customer_and_merchant_personas.md](../entrepreneurship/03_customer_and_merchant_personas.md))
* [x] Add Competitive Landscape Matrix: Direct/indirect competitors (Miswag, Elryan, iBazzar, Instagram commerce) vs Cheapify ([04_competitive_landscape_matrix.md](../entrepreneurship/04_competitive_landscape_matrix.md))
* [x] Add Trilingual Market Validation Survey Framework (Kurdish Badini, Arabic, English) ([05_market_validation_survey.md](../entrepreneurship/05_market_validation_survey.md))
* [x] Deploy survey + analyze results — **n=199 (179 shoppers / 20 merchants)**: 97% notice price gaps, 88% app intent, 74 beta contacts, 13 pilot-merchant signups (05 §7; CSV in `assets/evidence/`)
* [ ] Extract & contact the 13 pilot-merchant candidates + 74 shopper beta contacts from survey responses → founding-cohort outreach list *(deferred by founder — will do later)*
* [ ] Restore missing `assets/evidence/price-variation/` screenshots referenced by entrepreneurship/01–02 (folder absent from repo — pull from source device; target 5–6 total comparisons across categories)
* [ ] Second survey wave (deferred — later): Kurdish-boosted via Meta ads; ask AOV, COD preference, delivery-fee tolerance (gaps survey 1 left)
* [x] Synthesize Value Proposition Canvas (VPC), Innovation & Founder-Market Fit ([06_value_proposition_and_founder_fit.md](../entrepreneurship/06_value_proposition_and_founder_fit.md))

### Milestone 2: Execute Pillar 2 (Marketing) Deliverables

* [x] Set up `marketing/` directory structure
* [x] Synthesize two-sided GTM strategy (shopper acquisition vs. social merchant onboarding) ([01_two_sided_gtm_strategy.md](../marketing/01_two_sided_gtm_strategy.md))
* [x] Finalize brand guidelines, visual identity & design tokens from ground zero ([02_brand_identity_and_guidelines.md](../marketing/02_brand_identity_and_guidelines.md))
* [x] Select official UI design language via live visual style evaluation — "Clean Flat + Soft Depth" chosen (ADR-009, Preference 25, §8.0)
* [x] Publish complete interactive HTML brandbook ([brandbook/index.html](../brandbook/index.html))
* [x] Revise brandbook per founder review (Kurdish script, remove internal content, visual fixes)
* [x] Sync PMS 7731 C / 7689 C computed contrast values (4.48:1 / 3.62:1) in Markdown spec (§6)
* [ ] Native-speaker proofread of Kurdish-script copy (brandbook + brand spec)
* [x] Synthesize two-phase social content strategy — Phase A pre-launch plan ([03_pre_launch_content_plan.md](../marketing/03_pre_launch_content_plan.md)) + Phase B launch calendar ([04_launch_content_calendar.md](../marketing/04_launch_content_calendar.md)) (ADR-011, Preferences 28–30)
* [ ] Build waitlist landing page on getcheapify.com (required CTA endpoint before first post)
* [ ] Create Cheapify profiles on Facebook, Instagram, TikTok (brand-compliant bios/avatars)
* [ ] Produce reusable content templates per series (Price Detective card, Founder's Circle motion card)
* [ ] Begin Phase A posting cadence (5 posts/week per weekly template)

### Milestone 3: Execute Pillar 3 (Finance) Deliverables

* [x] Draft operational budget v1 — assumption-driven model ([01_operational_budget.md](../finance/01_operational_budget.md))
* [~] Collect real quotes: ~~Duhok courier~~ **A1 DONE — Fast Delivery: zones 2,500/3,500/4,500 contracted** (contract signing deferred — open anytime; confirm Zakho tier + 2nd quote for leverage); remaining: print (A12), legal registration, ad CPM test
* [x] Build unit economics doc (per-order & per-merchant LTV/CAC) — `finance/02_unit_economics.md`
* [x] Build cash-flow projection + break-even — `finance/03_cash_flow_and_breakeven.md`
* [x] Draft GIZ funding request — tiered ask mapped to ranked awards ([04_funding_request.md](../finance/04_funding_request.md))

### Milestone 4: Complete Pillar 4 (Business Modeling) — Complete

* [x] 9-Block Business Model Canvas — evidence-backed, survey + courier-quote integrated ([01_business_model_canvas.md](../business-modeling/01_business_model_canvas.md))
* [x] 3 Core SOPs — merchant onboarding, 3PL order flow→settlement, returns/refunds ([02_core_sops.md](../business-modeling/02_core_sops.md))
* [x] Operational risk matrix — 17 risks scored L×I, top risks R4 bypass/R1 traction/R2+R11 contract chain ([03_operational_risk_matrix.md](../business-modeling/03_operational_risk_matrix.md))

### Program Constraints (from GIZ updates)

* Ranked awards: 1st > 2nd > 3rd prize amounts (envelope unknown) — tiered ask in `finance/04` maps to any rank outcome.
* **Pitch deck hard limit: 6 minutes** — final deliverable must be designed to ~7–9 slides / 6-min runtime.
