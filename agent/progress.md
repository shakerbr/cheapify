# Cheapify — Progress Log

A running chronological log of completed actions, file creations, and achieved milestones.

---

## Chronological Entries

### [2026-10-16] — Two-Sided GTM Strategy & Execution Playbook Authored (Pillar 2 Milestone)
* **Action:** Authored and refined [`marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md) establishing Cheapify's go-to-market operational playbook:
  - **Platform Architecture Clarified:** Formalized that Cheapify is engineered as both a **mobile application (iOS & Android)** and an accessible **web platform** ([Preference 20](preferences.md)).
  - **Core Channels Refined:** Focused marketing and social commerce funnels on **Facebook, Instagram, and TikTok**, excluding Telegram from active focus ([Preference 21](preferences.md)).
  - **Self-Serve with Rules Onboarding:** Established that Cheapify sets strict quality standards, rules, and instructions, while merchants build and upload their own product listings and media via the self-serve merchant portal ([Preference 22](preferences.md)).
  - **Free Paid Ad Boosts for Founding Stores:** The first 20 verified stores receive 0% commission in Month 1 and get their products featured in Cheapify's paid ad campaigns across Facebook, Instagram, and TikTok ([Preference 23](preferences.md)).
  - **Broad Mass-Market Consumer Scope:** Expanded demand engine beyond university students to encompass young working professionals, household shoppers, civil servants, and deal-conscious families ([Preference 24](preferences.md)).
  - **Phased Geographic Horizon:** Structured the 3-phase rollout (Phase 1 Duhok Launchpad, Phase 2 Regional KRI/Nineveh Hubs, Phase 3 Nationwide All-Iraq Scale).


### [2026-10-16] — Stage 1 Merchant Onboarding Staged: Social Media Native Stores First
* **Action:** Recorded strategic operational milestone following founder guidance:
  - **Social Media Stores as Stage 1 Launchpad:** Prioritized Instagram, TikTok, and Telegram merchants over offline physical shops for the initial pilot phase.
  - **Key Advantages Formalized:** Zero catalog creation friction (ready photos, reels, specs), e-commerce native operational habits (courier booking, COD), acute DM exhaustion ("Interrogation Tax"), and organic two-sided traffic generation (merchants putting Cheapify links in bios).
  - **Governance Synchronized:** Added Preference 19 to [`agent/preferences.md`](preferences.md) and accepted ADR-008 in [`agent/decisions.md`](decisions.md).

### [2026-10-15] — Hybrid "Best Value" Algorithm Strategy Specification Authored
* **Action:** Authored [`platform/best_value_algorithm_strategy.md`](../platform/best_value_algorithm_strategy.md) establishing Cheapify's core product ranking architecture:
  - **Hybrid "Total Landed Cost + Proximity Advantage" Model:** Solved the trade-off between consumer doorstep affordability ($P_{\text{total}} = P_{\text{item}} + D_{\text{tariff}}$) and merchant transparency.
  - **Intra-City Bazaar Competition:** Documented that within the same metropolitan zone (e.g. Duhok to Duhok), flat courier tariffs (3,000 IQD) make Total Landed Cost ranking 100% identical to sticker price ranking, allowing local merchants to compete directly and transparently on retail prices.
  - **Inter-City Defense for Local Shops:** Demonstrated how distance tariffs create an organic economic defense for local neighborhood shops against out-of-city dumping, requiring distant vendors to provide authentic discounts that exceed the freight differential.
  - **Deterministic 3-Tier Multi-Attribute Priority Cascade:** Priority 0 (Lowest Total Landed Doorstep Price) $\rightarrow$ Priority 1 (Fastest Delivery Speed by Proximity Zone) $\rightarrow$ Priority 2 (Verified Merchant Operational Reliability & Quality Score).
  - **Logistics Distance Matrix:** Mapped 4 delivery zones (Hyperlocal 1–3h / 3k IQD, Intra-City 3–6h / 3k–3.5k IQD, Regional Inter-City 24–48h / 5k IQD, Nationwide 48–72h / 6k–7k IQD).
  - **Merchant Dashboard Diagnostics ("Why Didn't I Win?"):** Designed the wireframe and trilingual guidance (Badînî Kurdish, Arabic, English) giving merchants clear explanations and actionable pricing suggestions.
  - **Production TypeScript Engine:** Implemented pure, fully typed sorting function (`evaluateBestValueOffers`) with comprehensive unit interfaces.
* **Governance & Brand Identity Directives Updated:**
  - Formally updated ADR-007 in [`agent/decisions.md`](decisions.md) with the Hybrid Model.
  - Formally recorded Preference 18 in [`agent/preferences.md`](preferences.md) retiring all legacy brand colors ("Jade Green", `#148C53`, "Boston Blue") and mandating brand visual identity be built 100% fresh from ground zero in Pillar 2 (Marketing).
  - Synchronized [`AGENTS.MD`](../AGENTS.MD) and [`agent/active-tasks.md`](active-tasks.md).

### [2026-10-15] — Value Proposition Canvas, Innovation & Founder-Market Fit Authored
* **Action:** Authored [`entrepreneurship/06_value_proposition_and_founder_fit.md`](../entrepreneurship/06_value_proposition_and_founder_fit.md) providing the formal academic and incubator bridge between personas and solution architecture:
  - **Osterwalder Value Proposition Canvas (VPC):** Systematically mapped Customer Jobs, Pains, and Gains against Cheapify's Products, Pain Relievers, and Gain Creators for both the Deal-Seeking Shopper (Ahmad) and the Bazaar Merchant (Kak Kawa).
  - **Technological & Process Innovations:** Formulated Cheapify's 4 core innovations: Single-SKU aggregation vs feed clutter, the multi-variable "Best Value" algorithmic ranking engine, WhatsApp Cloud API automated waybill generation, and progressive marginal fee settlement.
  - **Founder-Market Fit & Execution Capabilities:** Documented founder background (Shakir Bashar, Computer Engineer, former IT Manager & COO), technical execution ($0 software development agency costs), capital discipline (available seed funding deployed 100% to external ops), and operational resilience in Iraqi COD retail.
  - **Pillar 1 Completeness Audit:** Formulated an 11-point audit matrix proving that every theoretical and practical requirement of the GIZ Youth Entrepreneurship curriculum is 100% fulfilled.

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
* **Action:** Standardized the 3-tier algorithm hierarchy for awarding the "Best Value" badge across [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md), [`agent/project-context.md`](project-context.md), [`agent/preferences.md`](preferences.md), and logged ADR-007 in [`agent/decisions.md`](decisions.md).
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
* **Legacy Coursework Note:** Past assignment exercise numbers only; not final venture budget. Real financials to be built in Pillar 3.

### [2026-10-11] — Project Foundation & Rebuild from Ground Zero
* **Action:** Commenced fresh ground-up construction of Cheapify.
* **Files:**
  - [`entrepreneurship/01_problem_solution_value.md`](../entrepreneurship/01_problem_solution_value.md) drafted.
  - Core brand assets imported into `assets/` (`cheapify-logo.svg`, `brand-tokens.json`).

