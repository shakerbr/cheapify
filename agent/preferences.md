# User Preferences & Working Methods

This file documents the specific ways, working habits, and styling preferences requested by the user.

---

1. **Dedicated Directory for Management Files:**
   - Store all agent governance, rules, roadmaps, and progress logs inside the dedicated `agent/` directory rather than cluttering the workspace root.

2. **Single Responsibility for Workspace Files:**
   - Every management file must be as simple as possible and dedicated to exactly one specific concern (e.g., rules only, preferences only, roadmap only, active tasks only).

3. **Ground-Up Building:**
   - Build Cheapify cleanly from ground zero. Use past incubator research and docs in `archive/` purely as reference points, never copying over outdated or messy legacy structures.

4. **Regional & Financial Grounding:**
   - Always anchor business, finance, and marketing data in real local Iraqi / Kurdistan Region reality (Duhok geography, 1 USD ≈ 1,500 IQD, Cash on Delivery default, local 3PL courier rates of 3,000 IQD/parcel).

5. **In-House Engineering Framing:**
   - Highlight that software development ($0 cash cost) and UX video creation ($0 cash cost) are engineered 100% in-house by the founder (Shakir Bashar), demonstrating extreme capital discipline to donors (GIZ / CAPA).

6. **Two-Sided Marketplace Balance:**
   - When drafting business, marketing, or product specs, always balance both sides of the platform: everyday deal-seeking shoppers (demand) and local bazaar/social media merchants (supply).

7. **Ground-Up 4-Pillar Build Before Final Presentation:**
   - Archived pitch decks (such as `archive/program-giz-cheapify/Cheapify Pitch Deck.pdf`) are simple, non-final materials from an earlier partial phase; DO NOT depend on them in planning.
   - We must build all 4 pillars completely from ground zero first (1. Entrepreneurship, 2. Marketing, 3. Finance Management, 4. Business Modeling).
   - The final comprehensive pitch deck and presentation will be created only after all 4 pillars are fully built.

8. **"Best Value" Algorithm Ranking Hierarchy:**
   - Competing sellers on a single SKU must be evaluated and ranked strictly by:
     - **Priority 0 (Most Important):** Price (lowest price in IQD is paramount).
     - **Priority 1:** Delivery Time (fastest arrival time to the customer's area).
     - **Priority 2:** Rating and Reviews (merchant score and customer satisfaction).

9. **Primary Venture Focus & Genesis: Price Variation:**
   - While Cheapify resolves many operational headaches (the "Interrogation Tax", missing specs/variants, merchant data management), the **primary catalyst and foundational focus that created Cheapify is Price Variation & Arbitrary Markups**.
   - Always lead with Price Variation as the #1 problem and primary value anchor across all entrepreneurship, marketing, and business modeling documentation.

10. **Evidence & Institutional Citations Standard:**
    - Always provide verified references, institutional sources, and documented proof for all data, market sizing, demographics, and pricing claims (e.g., World Bank, DataReportal/Kepios, KRSO, KAPITA/GIZ Research, and local repository screenshots). Never use unsubstantiated assertions without methodological backing.

11. **Broad Multi-Category Marketplace Scope:**
    - Cheapify is NOT a niche electronics accessory app; it is a comprehensive multi-category marketplace. It encompasses all standardized retail sectors with price variations, including:
      - Electronics & Gadgets
      - Home, Kitchen & Garden
      - Luggage, Watches, Bags, Branded Perfumes
      - Beauty & Self-Care
      - Health & Personal Care
      - Cleaning Equipment
      - Business & Industrial Tools & Equipment
      - Study & Educational Gear
      - Gifts & Novelties
      - Musical Equipment
      - And all other standardized retail kinds.

12. **Progressive Geographic Scaling Horizon (Duhok to All Iraq):**
    - The rollout strategy follows three disciplined phases:
      - **Phase 1 (Pilot Launchpad):** Duhok metropolitan area (Duhok, Semel, Zakho).
      - **Phase 2 (Regional Hubs):** Erbil, Mosul (Nineveh), and Sulaymaniyah.
      - **Phase 3 (Nationwide All-Iraq Coverage):** Scaling to Baghdad, Basra, Kirkuk, Najaf, Karbala, and all Iraqi governorates. Covering the whole of Iraq is the core venture destination.

13. **Strictly Relative Links in Repository Documents:**
    - Always format internal markdown links using relative paths (e.g., `assets/evidence/price-variation/...`), NEVER absolute filesystem paths or `file:///` URLs.

14. **Dedicated Directory for Semi-General Artifacts (`platform/`):**
    - Cross-cutting, semi-general platform specifications that span across multiple pillars (such as fee structures, algorithm logic, and logistics protocols) must be housed in a dedicated directory like `platform/`, keeping specific pillar folders (e.g. `entrepreneurship/`) uncluttered and focused strictly on curriculum deliverables.

15. **Marketplace Fee Architecture — Progressive Marginal Tiering:**
    - Cheapify uses a 3-tier progressive marginal fee model to eliminate the cliff effect and protect merchant margins:
      - **Tier 1 (1 to 10,000 IQD):** 5.0%
      - **Tier 2 (10,001 to 100,000 IQD):** 3.0%
      - **Tier 3 (100,001+ IQD):** 1.5%
    - Detailed reference: [`platform/fee_structure_and_monetization.md`](../platform/fee_structure_and_monetization.md).

16. **Clean Presentation of Survey & Research Artifacts:**
    - When documenting market surveys, research instruments, or questionnaires, present them in a clean, structured, and human-readable format (e.g. trilingual tables, sections, and logic diagrams). Do not include raw Google Apps Script or code-like syntax in core venture documentation.





