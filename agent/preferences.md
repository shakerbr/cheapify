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
    - Always format internal markdown links using relative paths (e.g., `assets/evidence/<case>/...` under `entrepreneurship/`), NEVER absolute filesystem paths or `file:///` URLs.

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

17. **No Unfinalized Financial or Budget Placeholders:**
    - Do not hardcode or mention specific grant amounts (e.g. $2,200), arbitrary budget breakdowns, or unverified operational burn rates from past incubator assignments. Those legacy figures were temporary placeholders created only to pass earlier coursework. Real financial metrics, budgets, and unit economics will be constructed fresh from ground zero during Pillar 3 (Finance Management).

18. **Retirement of Legacy Brand Colors & Ground-Up Identity Rebuild:**
    - Jade Green, `#148C53`, Boston Blue, and any previous color tokens from past incubator exercises, old pitch decks, or archives are strictly retired and are no longer part of the Cheapify brand.
    - Brand visual identity, design language, color palette, and UI tokens will be built 100% fresh from ground zero in Pillar 2 (Marketing).
    - In the interim, UI badges, buttons, and visual highlights must be referred to neutrally (e.g., "highlighted 'Best Value' chip / badge", "prominent deal card") without referencing or hardcoding obsolete color names.

19. **Merchant Acquisition Staging — Online Social Media Stores First:**
    - The first stage of merchant onboarding targets **online social media stores** (Instagram, Facebook, and TikTok sellers; currently not Telegram), NOT offline physical bazaar retail stores.
    - **Strategic Rationale:**
      1. **Asset Readiness:** Social sellers already possess digital photos, showcase video reels, written specs, and product lists. Catalog ingestion is fast with zero photography friction.
      2. **Operational E-Commerce Familiarity:** They are already accustomed to remote selling, 3PL courier coordination (local fleets e.g. Fast Delivery; inter-city networks e.g. ZMC Express), and COD reconciliation.
      3. **Acute DM Exhaustion ("Interrogation Tax"):** They experience the most severe pain from answering hundreds of repetitive DMs ("Bihayê wê çende?", "Parve bike", "What colors?"), with 80%+ drop-off. Cheapify acts as an instant relief tool, converting DMs into 1-click structured checkouts.
      4. **Built-in Audience & Organic Shopper Acquisition:** Social sellers will put their Cheapify store/product links in their social media bios and stories, funnelling their existing followers directly into Cheapify as free, organic buyer traffic.
    - Traditional physical bazaar shops will be integrated in subsequent phases once platform liquidity, catalog depth, and simplified barcode-scanning tools are established.

20. **Platform Form Factor — Web Platform + Mobile App:**
    - Cheapify is engineered as both a **mobile app (iOS & Android)** and an accessible **web platform**. Never describe Cheapify as website-only.

21. **Primary Social Media Marketing Channels:**
    - Marketing campaigns, social commerce funnels, and merchant recruitment prioritize **Facebook, Instagram, and TikTok**. Telegram is excluded from active marketing focus for the current phase.

22. **Self-Serve Merchant Onboarding with Strict Guidelines:**
    - The Cheapify team does **NOT** manually scrape, extract media assets, or build product pages for merchants.
    - Instead, Cheapify provides clear rules, standards, quality guidelines, and an intuitive self-serve merchant portal/workflow where sellers upload their own media and configure their own store listings.

23. **Founding Merchants Incentive — Free Paid Ad Boosts:**
    - The first 20 verified founding stores in Duhok receive not only 0% commission for month 1, but their products are directly **featured in Cheapify's paid advertising campaigns** (Facebook, Instagram, and TikTok sponsored ads). This gives them free commercial visibility, traffic boosts, and guaranteed sales exposure.

24. **Broad Consumer Audience Scope (Beyond Campus/Students):**
    - While university students are a great viral launchpad cohort, Cheapify is a broad mass-market consumer platform for all Iraqi and Kurdish shoppers: young working professionals, civil servants, household shoppers, tech enthusiasts, and budget-conscious families seeking upfront price transparency and verified deals.

25. **Official UI Design Language — "Clean Flat + Soft Depth":**
    - Cheapify's user interface design style is **Clean Flat + Soft Depth**, selected by the founder after live visual evaluation of 8 candidate styles (Clean Flat + Soft Depth, Vibrant Dopamine, Neumorphic Fintech, Gamified Deal-Hunting, Bento Grid 2.0, Glassmorphism/Liquid Glass, Claymorphism, Editorial Minimal/Zero-UI) rendered in `assets/design-style-previews/index.html`.
    - **Core traits:** Flat, pure-white surfaces on light neutral backgrounds; generous `12px–16px` corner radii; subtle single soft shadows (never hard, colored, or multiple stacked shadows); hairline `1px` borders in PANTONE 656 C; disciplined PMS blue/green accent usage only for CTAs and Best Value signals.
    - **Rejected directions (do NOT use):** Sticker/offset-shadow neo-brutalism, saturated dopamine gradients, heavy glassmorphism/blur, puffy claymorphism, dense gamification HUDs (streaks/points/meters), and bare editorial zero-chrome layouts. Gamified *elements* (badge, savings copy) may appear as content, never as the visual language itself.
    - **Rationale:** Maximizes clarity, price-table readability, and trilingual accessibility for a broad mass-market audience including low-digital-literacy users; aligns with the Radically Transparent and Operationally Precise personality attributes.

26. **No Emojis — Icons Only:**
    - Cheapify NEVER uses emojis in any UI, document, marketing material, social content, or communication — no exceptions.
    - Instead, use proper iconography: custom-drawn icons matching Cheapify's icon construction spec (§9.1 of the brand guidelines), or icons sourced from free CDN icon libraries.
    - Approved free sources: **Lucide** (lucide.dev — clean 2px-stroke open source set matching the icon spec), **Phosphor Icons**, **Heroicons**, or **Iconify** CDN as an aggregator.
    - **Rationale:** Emojis render inconsistently across devices/locales, look unprofessional for a trust-driven marketplace, and break the disciplined PMS color system. Vector icons stay on-brand, recolorable, and consistent at any size.

27. **Official Platform Domain — `getcheapify.com`:**
    - The official primary web domain, app download hub, API root, and public digital address for Cheapify is **`getcheapify.com`**, secured via Cloudflare Registrar.
    - **Strategic Rationale:**
      1. **Universal Subconscious Trust:** `.com` is the gold standard of trust for everyday shoppers, students, and bazaar merchants in Iraq and Kurdistan.
      2. **Action-Oriented Product Verb:** The *"Get"* prefix creates a natural imperative for a dual **Mobile App + Web Marketplace** (*"Get Cheapify on iOS, Android, and Web"*), mirroring proven Silicon Valley playbooks (Dropbox, Pocket).
      3. **Zero Typo-Leakage:** Eliminates the risk of users accidentally typing `.com` when trying to reach alternate TLDs like `.co`.
      4. **Enterprise Infrastructure:** Managed directly on Cloudflare with zero-markup at-cost renewals, free WHOIS privacy, DNSSEC, automatic SSL, and enterprise DDoS mitigation.

28. **Unified Cross-Platform Content — One Set for Facebook, Instagram, and TikTok:**
    - Cheapify publishes the **same content to all three platforms** — no platform-exclusive content. One concept is produced as a single vertical 9:16 master file (or 1:1 for static cards) and uploaded natively to each platform; captions are adapted per platform norms, and watermarked cross-posts are prohibited.
    - **Rationale:** A founder-led team cannot sustain three separate content pipelines, and the Duhok launch audience is active on all three platforms anyway.

29. **Content Language Policy — Kurdish-First, One Post Multilingual:**
    - Video audio is **Badînî Kurdish** (Duhok launch market). Videos carry **one burned-in subtitle track in Kurdish script** (for muted autoplay) — two stacked subtitle tracks are prohibited (they consume ~25% of a 9:16 frame).
    - Captions are **Kurdish first, Arabic second within the same post** — separate posts per language are prohibited (they split engagement and triple feed noise).
    - **English is excluded** from consumer-facing launch content; it is reserved for later investor/B2B material. For Phase 3 expansion audiences (Baghdad/Basra), the same footage is re-exported with Arabic subtitles.

30. **Two-Phase Content Plan — Template Before Launch, Calendar After:**
    - **Phase A (pre-launch):** a repeatable weekly posting template ([`../marketing/03_pre_launch_content_plan.md`](../marketing/03_pre_launch_content_plan.md)) cycled until MVP, since its duration is unknown (1–3 months).
    - **Phase B (launch):** a fixed T-7 countdown → launch week → 8-week calendar ([`../marketing/04_launch_content_calendar.md`](../marketing/04_launch_content_calendar.md)) activated when the MVP date is confirmed and ≥10 founding merchants are committed.
    - Pre-launch content must never announce features on a hard date, promise unshipped functionality, or name/shame specific shops — price-variation posts blur store identities and use real verifiable prices only.

31. **Referral Rewards — Transaction-Gated, Four-Direction:**
    - Referral rewards fire ONLY on completed, courier-confirmed transactions — never on account signup. Rewards are non-transferable platform credit, never cash (60-day expiry).
    - All four referral directions are supported: Shopper→Shopper, Shopper→Merchant ("nominate a shop"), Merchant→Shopper, Merchant→Merchant. A recruited merchant "activates" only after 10 completed orders.
    - **Rationale:** signup-gated rewards are farmed by fake accounts; a delivered COD order can't be faked cheaply. Full spec: [`../platform/referral_and_growth_incentives.md`](../platform/referral_and_growth_incentives.md).

32. **Catalog First-Mover Incentive — Paid, Shared, Improvable:**
    - First merchant to create an approved master listing earns a **1,000 IQD commission-offset credit** plus permanent attribution; later merchants claiming the same SKU only add price/stock/variants.
    - Approved improvements to existing listings earn a **250 IQD micro-bounty** — master pages are shared infrastructure, and edits are QA-approved proposals, never direct edits.
    - Listing creation is **barcode-first** (scan → auto-fill name/specs from product databases; guided template for unbranded goods).
    - **No platform-seeded catalog** (founder decision): Cheapify staff never pre-create product pages; the catalog spine is 100% merchant-built.

33. **Pitch Deck Design (GIZ Final Pitch):**
    - Any number of slides is fine — the hard constraint is total runtime: the full pitch must fit in under 6 minutes.
    - Understandable at a glance: minimal text, visuals first, one idea per slide.
    - Animations and step-by-step animated sequences are encouraged to explain mechanisms (e.g., how Best Value ranks offers, how an order flows).
    - Follow the GIZ proposed section order where it serves the story; deviations are allowed when they make the pitch clearer.
    - Do NOT reuse the archived decks' styling (old, discarded). The only template elements carried over are the German Cooperation (GIZ) + CAPA/AUK logo header and the CAPA/AUK contact footer: both appear on the cover and Thank-You slides; content slides carry only the header, slightly smaller — exactly as in `archive/program-giz-cheapify/Presentation-stuff/Modified template.pptx`.
    - **The CAPA/AUK logo is smaller than the German Cooperation logo**, in the proportions of `archive/GIZ-assets/template.jpg` (CAPA ≈ 0.68× the German Cooperation logo's width; exact sizes in the v4 spec §1).
    - **Visual over text, always:** when slides drift into text cards or tables, restore illustrations (circles, avatars, waterfalls, flywheels, charts with on-curve labels). The founder rejected text-heavy redesigns.
    - **Visual perfection is the bar:** "no matter how many slides it takes, make it visually perfect" — no half-empty slides, no visual crowding, one focal point per slide (full checklist: v4 spec §0).
    - **Animations:** click-by-click; long sequences fast but not rushed (~40 ms stagger / ~220 ms effect after the founder's "a little slower" note).
    - **Story rules from the teacher & founder reviews:** the cover shows no product name or logo — Cheapify is revealed on the Solution slide; the cover leads with `Youth Entrepreneurship Program` (large) and `One product, ten prices.` (small subtitle) + `4 November 2026`; problem slides carry an explicit problem statement (`Online in Iraq, you can't know the real price before you buy.`); the solution headline states the outcome explicitly; numbers beat bare percentages (e.g. "~390 regular shoppers", not "0.4%"); target customers are behavior-based and budget-conscious ("Household budget buyers", never "Families"); expansion roadmap belongs to Growth, not Market; the Product slide and the redundant "Funding is done — what now?" slide are cut; the Thank You slide is English-only (no Kurdish/Arabic slogans).
    - **Founder disagreements kept:** fee tiers (5% / 3% / 1.5%) stay on the Business Model slide (they are the revenue stream), not Growth.
    - **Every on-slide number** must have its source and calculation in the speaker notes and `presenter-guide.md`, plus ready answers to likely judge questions — slides stay clean; detail lives in the notes.
    - **Embed all deck fonts in the `.pptx`:** `Comfortaa`, `Inter`, and `IBM Plex Sans Arabic` (Regular + Bold) are stored inside the project at `presentation/assets/fonts/` and embedded directly into the `.pptx` (`ppt/fonts/*.fntdata` under `<p:embeddedFontLst>`) so the presentation renders identically without installing fonts on the presenting computer.

34. **Finance & Funding Presentation:**
    - No unallocated "reserve" or "contingency" lines in the grant ask — every dollar has one named, computed use, and each cost is funded only once (ADR-015).
    - Show both break-even points and name them clearly: monthly break-even (month 4) and cumulative recovery / payback (month 8).
    - Judges want "how much is spent, each month, and when it comes back" — keep a month-by-month release schedule.
    - Prefer verified public sources (official fee schedules, central-bank rates, provider price pages) over estimates; label estimates as estimates. Exact derived numbers are fine; round numbers are fine when the derivation is shown.
    - Profit must stay strong: present card/e-wallet fees with their offsets (pre-paid orders remove failed-delivery cost), never as an unexplained drag.
