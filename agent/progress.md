# Cheapify — Progress Log

A running chronological log of completed actions, file creations, and achieved milestones.

---

## Chronological Entries

### [2026-10-15] — Trilingual Market Validation Survey Framework Authored (Milestone 1 Complete)
* **Action:** Authored [`entrepreneurship/05_market_validation_survey.md`](../entrepreneurship/05_market_validation_survey.md) capturing the live empirical research framework currently collecting responses:
  - **Clean Non-Code Presentation:** Documented the full survey instrument cleanly across Kurdish (Badînî), Arabic, and English without raw script code blocks, adhering to user direction.
  - **Dynamic Dual-Cohort Logic:** Formulated the branching architecture: Language Selection $\rightarrow$ Role Branching (Shopper vs. Merchant) $\rightarrow$ Targeted Problem/Solution Validation $\rightarrow$ Pilot Beta & Merchant Store Lead Capture.
  - **Hypothesis Testing Grounding:** Mapped each question directly to venture hypotheses (H1 Price Variation prevalence, H2 "Interrogation Tax" fatigue, H3 Single-SKU comparison demand, H4 Seller chat burnout, H5 Turnkey dashboard adoption).
  - **Live Distribution & Pipeline Feeder:** Documented outreach channels (AUK/UoD student Telegram groups, in-person Duhok bazaar merchant visits with QR codes, in-app social media links with Google sign-in toggled off) and mapped how incoming responses feed Marketing (Pillar 2), Finance (Pillar 3), and Business Modeling (Pillar 4).
* **Milestone 1 Achieved:** Pillar 1 (Entrepreneurship) is now **100% complete** across all 5 core foundation deliverables.

### [2026-10-15] — Competitive Landscape Matrix & Strategic Differentiation Authored
* **Action:** Authored [`entrepreneurship/04_competitive_landscape_matrix.md`](../entrepreneurship/04_competitive_landscape_matrix.md) establishing Cheapify's market positioning and defensibility:
  - **Head-to-Head Profiling:** Analyzed 4 incumbent alternatives across Iraq/KRI: Social Commerce DMs (Instagram/TikTok), Miswag (10%–15% commission, slow inter-city delivery), Elryan (closed 1P retail, rigid MSRP), and iBazzar (open 3P, duplicate SKU clutter, intra-app 10k price gaps).
  - **Comprehensive 12-Dimension Matrix:** Contrasted catalog architecture (Single-SKU master page), price transparency, variant chip selectors, 1-click checkout (<30s), local payment integrations (COD + FIB/FastPay/Qi Card), hyperlocal 3PL intra-city delivery (ZMC Express 3,000 IQD), take-rate (1.5%–5% progressive vs. Miswag 12%), and merchant dashboard.
  - **Core Moats Documented:** The Single-SKU flywheel (each new seller drives down price rather than adding visual clutter), in-house software agility ($0 dev fees by founder Shakir Bashar), asset-light 3PL courier integration, and merchant margin protection.
  - **Strategic Positioning Map:** Formulated 2x2 matrix (Price Transparency vs. Automated Structured Commerce), placing Cheapify firmly in the top-right quadrant.

### [2026-10-15] — Platform Fee Architecture & Monetization Specification Created
* **Action:** Created dedicated cross-cutting platform artifact [`platform/fee_structure_and_monetization.md`](../platform/fee_structure_and_monetization.md) in a new semi-general directory `platform/`:
  - **Progressive Marginal Tiering Model:** Formulated the 3-tier progressive take-rate to completely eliminate the cliff effect (where a higher price would otherwise pay a lower fee):
    - **Tier 1 (1 to 10,000 IQD):** 5.0% (max 500 IQD)
    - **Tier 2 (10,001 to 100,000 IQD):** 3.0% (max 2,700 IQD)
    - **Tier 3 (100,001+ IQD):** 1.5%
  - **Cliff Effect Mathematical Analysis:** Included proof of strict monotonicity ($\forall P_2 > P_1 \implies \text{Fee}(P_2) > \text{Fee}(P_1)$), demonstrating that an item at 14,500 IQD costs 635 IQD while an item at 16,000 IQD costs 680 IQD.
  - **Multi-Category Simulation Table:** Benchmarked across 12 product tiers from cables (5,000 IQD) to high-end laptops (1,200,000 IQD), demonstrating 58% to 86% margin savings compared to traditional 12% platforms (e.g., Miswag).
  - **Engineering Reference:** Added TypeScript implementation function (`calculateCheapifyFee`) for the web MVP checkout engine and documented COD weekly net-reconciliation flow.
* **Governance Updated:** Formally accepted ADR-005 in [`agent/decisions.md`](decisions.md) and logged Preferences 14 & 15 in [`agent/preferences.md`](preferences.md).

### [2026-10-15] — Multi-Category Scope & Nationwide Scaling Horizon Re-architected
* **Action:** Restructured [`entrepreneurship/02_market_opportunity_and_sizing.md`](../entrepreneurship/02_market_opportunity_and_sizing.md) based on founder direction:
  - **Multi-Category Retail Expansion:** Broadened the platform scope beyond electronics to all standardized retail categories with price variations (Electronics; Home, Kitchen, Garden; Luggage, Bags, Watches, Perfumes; Beauty & Self-Care; Health; Cleaning; Business & Industrial; Study; Gifts; Musical; and more).
  - **Updated Sizing Metrics:** TAM calibrated to $2.5B–$3.5B+ USD across all Iraq; SAM expanded to $600M–$800M USD across multi-category goods in initial expansion zones.
  - **Progressive Geographic Scaling Horizon:** Formulated a 3-stage geographic rollout: Launchpad (Duhok) ──► Northern Regional Hubs (Erbil, Mosul, Sulaymaniyah) ──► Complete Nationwide Coverage across ALL of Iraq (Baghdad, Basra, and all governorates).
* **Governance Updated:** Recorded Preferences 11 & 12 in [`agent/preferences.md`](preferences.md) and synchronized [`agent/project-context.md`](project-context.md).

### [2026-10-15] — Institutional References & Evidence Added to Market Sizing
* **Action:** Added Section 5 ("Statistical Sources, Evidences & Research References") to [`entrepreneurship/02_market_opportunity_and_sizing.md`](../entrepreneurship/02_market_opportunity_and_sizing.md) providing exact, verified citations for every metric:
  - **Demographics:** World Bank, Iraq Ministry of Planning, and Kurdistan Region Statistics Office (KRSO).
  - **Digital Penetration:** DataReportal / Kepios Digital 2024 Iraq report (33.5M internet users, 42.1M mobile connections).
  - **E-Commerce & Social Commerce:** KAPITA Research ("E-Commerce in Iraq" & "Digital Payments"), International Trade Centre (ITC), and GIZ PSD reports confirming >80% social commerce via DMs and 85–90% COD.
  - **Logistics:** ZMC Express standard intra-city tariff (3,000 IQD).
  - **Price Disparity Evidence:** Directly linked the 4 repository screenshots in [`entrepreneurship/assets/evidence/price-variation/`](../entrepreneurship/assets/evidence/price-variation/) proving the ~47,000 IQD monitor disparity and 10,000 IQD intra-app Xiaomi disparity.
* **Governance:** Added Preference 10 to [`agent/preferences.md`](preferences.md) establishing mandatory evidence and citation standards for all future venture documentation.

### [2026-10-15] — Dual-Persona Deep-Dive Document Created
* **Action:** Authored [`entrepreneurship/03_customer_and_merchant_personas.md`](../entrepreneurship/03_customer_and_merchant_personas.md) capturing in-depth behavioral profiles and journey maps:
  - **Consumer (Ahmad, 23):** Final-year university student & part-time assistant in Duhok. Budget-conscious, values side-by-side transparency, hates "DM for price" and arbitrary markups. Journey mapped before vs. after Cheapify.
  - **Merchant (Kak Kawa, 34):** Owner of "Kawa Tech" in central Duhok Bazaar + Instagram page. Exhausted by repetitive DMs, suffers from inventory chaos across notebooks, needs turnkey dashboard and pre-qualified orders without heavy commissions.
  - Built cross-persona alignment matrix harmonizing pricing, information, ordering, and trust incentives.

### [2026-10-15] — Market Opportunity & Sizing Document Created
* **Action:** Authored [`entrepreneurship/02_market_opportunity_and_sizing.md`](../entrepreneurship/02_market_opportunity_and_sizing.md) to define and quantify the market opportunity across Iraq, the Kurdistan Region, and Duhok:
  - **TAM (Total Addressable Market):** $2.5B – $3.0B USD / year (Iraqi e-commerce, 44M population, 33M internet users).
  - **SAM (Serviceable Available Market):** $150M USD / year (Standardized tech & lifestyle accessories in KRI & high-density urban youth hubs).
  - **SOM (Serviceable Obtainable Market):** 
    - 6-Month Pilot (Duhok): 3,000 orders, ~$100,000 USD GMV, $3,500 USD platform revenue across 5–10 verified stores.
    - Year 1 Target (Duhok + Erbil): 11,700 orders, ~$350,000 USD GMV, $14,000 USD platform revenue.
  - Defined market growth drivers (exhaustion with "DM for price", e-wallets, 3PL courier maturity) and the standardized beachhead SKU strategy (chargers, earbuds, gaming accessories first).

### [2026-10-14] — Price Variation Re-anchored as Primary Problem & Catalyst
* **Action:** Refined Section 1 and Section 2 of [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md), [`agent/project-context.md`](project-context.md), and [`agent/preferences.md`](preferences.md) to explicitly declare **Price Variation & Arbitrary Markups** as the primary genesis and core focus of Cheapify.
* **Refinement Details:** While Cheapify also resolves the "Interrogation Tax", missing specs/variants, and merchant data chaos, eliminating wild price disparities remains the primary value anchor and founding catalyst.

### [2026-10-14] — Best-Value Ranking Priority Hierarchy Standardized
* **Action:** Standardized the 3-tier algorithm hierarchy for awarding the Jade Green "Best Value" badge across [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md), [`agent/project-context.md`](project-context.md), [`agent/preferences.md`](preferences.md), and logged ADR-007 in [`agent/decisions.md`](decisions.md).
* **The Hierarchy:**
  - **Priority 0 (Most Important / Primary):** Price (lowest price in IQD).
  - **Priority 1 (Secondary):** Delivery Time (fastest local delivery window).
  - **Priority 2 (Tertiary):** Rating and reviews (merchant reputation score).

### [2026-10-14] — Seller Data Management & Merchant Dashboard Integrated
* **Action:** Updated [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md) based on founder direction:
  - Added **Manual Data Chaos & Operational Blindness** to Section 1.3 (The Seller's Pain): Sellers struggle managing orders, inventory, and addresses in paper notebooks, WhatsApp threads, and messy spreadsheets.
  - Added **2.4 Centralized Merchant Operations Dashboard** to Section 2 (The Solution): Equipping sellers with a digital dashboard for stock control, live order pipelines, competitor price-drop alerts, and revenue tracking.
  - Updated Section 3.2 (Core Value for Sellers) with Turnkey Data & Operations Dashboard benefits.

### [2026-10-14] — Governance Architecture Refactoring & Ground-Up Sequencing
* **Action:** Refactored project governance into single-purpose, simple files inside [`agent/`]() and locked in the ground-up 4-pillar build sequence.
* **New Directive Added:** Archived pitch decks (e.g. `Cheapify Pitch Deck.pdf`) are confirmed non-final and partial; planning will NOT depend on them. We build all 4 pillars from ground zero first (1. Entrepreneurship, 2. Marketing, 3. Finance Management, 4. Business Modeling), and assemble the final presentation only after all 4 pillars are complete.
* **Governance Files Maintained:**
  - [`agent/rules.md`](rules.md): Added rule for 4-pillar build order before final deck.
  - [`agent/preferences.md`](preferences.md): Documented ground-up construction workflow.
  - [`agent/roadmap.md`](roadmap.md): Updated strategic phases and table.
  - [`agent/decisions.md`](decisions.md): Added ADR-006.
  - [`agent/active-tasks.md`](active-tasks.md): Focused strictly on Pillar 1 completion.


### [2026-10-12] — Finance Management Pillar Completion (Archived)
* **Action:** Finalized full GIZ budget plan and financial model.
* **Files:**
  - `archive/finance-management/assignment/01_budget_plan_and_evidence.md`
  - `archive/finance-management/assignment/Cheapify_Budget_GIZ.xlsx`
  - `archive/finance-management/assignment/Cheapify_Monthly_Profit_and_Loss.xlsx`
  - `archive/finance-management/assignment/Cheapify_Budget_Plan_and_Evidence.pdf`
  - `archive/finance-management/assignment/Cheapify_Budget_Report.html`
* **Key Numbers:** $2,200 GIZ seed grant ask, 88.6% gross margin, +37.1% net profit during pilot, break-even at 6 orders/day.

### [2026-10-11] — Project Foundation & Rebuild from Ground Zero
* **Action:** Commenced fresh ground-up construction of Cheapify.
* **Files:**
  - [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md) drafted.
  - Core brand assets imported into `assets/` (`cheapify-logo.svg`, `brand-tokens.json`).

