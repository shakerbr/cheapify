# Cheapify — Architectural & Strategic Decisions (ADR)

This file records key decisions, their context, rationale, and consequences for **Cheapify**.

---

## Decision Index

### ADR-001: Dedicated `agent/` Directory with Single-Responsibility Files
* **Date:** 2026-10-14
* **Status:** Accepted
* **Context:** The workspace needed rules, preferences, roadmaps, task lists, and progress logs without cluttering the project root or mixing different concerns in one file.
* **Decision:** Group all governance files in `agent/`, breaking each down into a simple, single-purpose document (`rules.md`, `preferences.md`, `project-context.md`, `roadmap.md`, `active-tasks.md`, `progress.md`, `decisions.md`).

### ADR-002: Single-SKU Catalog Architecture
* **Date:** 2026-10-11
* **Status:** Accepted
* **Context:** Traditional Iraqi e-commerce platforms (like iBazzar) allow each seller to upload their own duplicate listing for the same item, causing visual clutter and preventing direct price comparison.
* **Decision:** Enforce a strict Single-SKU layout. Exactly one master product page per barcode/SKU, with all verified sellers listed underneath in a side-by-side comparison table.

### ADR-003: In-House Software Engineering & Zero Agency Dev Fees
* **Date:** 2026-10-12
* **Status:** Accepted
* **Context:** Seed capital is limited, and traditional software development agencies charge substantial fees to build a marketplace.
* **Decision:** Founder Shakir Bashar (computer engineer) builds the entire web platform, APIs, database, and marketing demo videos in-house. 100% of available seed funding goes directly to real third-party operational costs (servers, Cloudflare, WhatsApp Cloud API, Duhok marketing, Chamber registration).

### ADR-004: Asset-Light 3PL Logistics Model
* **Date:** 2026-10-12
* **Status:** Accepted
* **Context:** Purchasing delivery motorbikes or hiring full-time drivers is capital-intensive and risky for an early pilot.
* **Decision:** Partner directly with established third-party logistics couriers in Duhok (e.g. ZMC Express / local delivery couriers) at standard market parcel rates (3,000 IQD / order), handling automated waybills and COD reconciliation.

### ADR-005: Progressive Marginal Tiering Fee Architecture
* **Date:** 2026-10-15
* **Status:** Accepted
* **Context:** Traditional 10%–15% commissions destroy 15%–20% bazaar retail margins. Step-tiered brackets cause regressive cliff effects (e.g. 14,500 IQD at 5% producing 725 IQD vs. 16,000 IQD at 3% producing 480 IQD). Flat fees are ruled out by the founder.
* **Decision:** Implement **Progressive Marginal Tiering** across 3 price tranches:
  - **Tier 1 (1 to 10,000 IQD):** 5.0% marginal rate (max 500 IQD).
  - **Tier 2 (10,001 to 100,000 IQD):** 3.0% marginal rate (max 2,700 IQD).
  - **Tier 3 (100,001+ IQD):** 1.5% marginal rate.
  Documented in detail in [`../platform/fee_structure_and_monetization.md`](../platform/fee_structure_and_monetization.md). Completely eliminates the cliff effect, ensuring strictly monotonic fee scaling.

### ADR-006: Ground-Up 4-Pillar Construction Before Final Pitch Deck
* **Date:** 2026-10-14
* **Status:** Accepted
* **Context:** Archived pitch decks (`archive/program-giz-cheapify/Cheapify Pitch Deck.pdf`) were created as partial, non-final artifacts during early incubator assignments and do not represent the complete venture.
* **Decision:** Treat the project as starting from ground zero. Build all 4 program pillars completely in sequence (1. Entrepreneurship, 2. Marketing, 3. Finance Management, 4. Business Modeling). Assemble and design the final pitch deck and showcase presentation strictly after all 4 pillars are fully built.

### ADR-007: Hybrid "Best Value" Ranking Algorithm Architecture (Total Landed Cost + Proximity Advantage)
* **Date:** 2026-10-15 (Updated)
* **Status:** Accepted
* **Context:** When multiple verified merchants offer the exact same Single-SKU product, the system must algorithmically select the winning offer to award the signature "Best Value" chip. A pure sticker-price model creates checkout friction if a distant seller has high shipping fees. Conversely, a pure landed-cost model without geographical explanation confuses local merchants.
* **Decision:** Implement the **Hybrid Total Landed Cost + Proximity Advantage** model governed by a deterministic 3-tier hierarchy:
  1. **Priority 0 (Primary / Hard Cut — Total Doorstep Price):** Lowest Total Landed Price ($P_{\text{total}} = P_{\text{item}} + D_{\text{tariff}}$).
     - **Intra-City (Same Zone, e.g. Duhok to Duhok):** Courier shipping is flat (3,000 IQD), making Total Landed Price ranking 100% identical to sticker price ranking. Local bazaar merchants compete directly on retail sticker price.
     - **Inter-City (Cross-Zone, e.g. Erbil vs Duhok):** Protects local merchants against out-of-city dumping. An out-of-town merchant must offer a discount large enough to overcome higher inter-city delivery tariffs (e.g. 5,000 IQD vs 3,000 IQD) to genuinely save the buyer total money at the door.
  2. **Priority 1 (Secondary / Tie-Breaker — Delivery Speed by Proximity):**
     - Hyperlocal (1–3h) beats Intra-City Standard (3–6h) beats Inter-City (24–48h).
  3. **Priority 2 (Tertiary / Tie-Breaker — Merchant Quality & Reviews):**
     - Highest verified merchant review rating (stars) and fulfillment fulfillment rate.
  - **Dual Transparency:** Shopper sees full item + shipping breakdown; Merchant Dashboard provides diagnostic clarity showing exactly why an offer won or lost. Full platform specification: [`../platform/best_value_algorithm_strategy.md`](../platform/best_value_algorithm_strategy.md).

### ADR-008: Stage 1 Merchant Onboarding — Social Commerce Native Sellers First (Self-Serve with Rules)
* **Date:** 2026-10-16 (Updated)
* **Status:** Accepted
* **Context:** Traditional physical bazaar stores lack digital product photography, pre-written specifications, and digital inventory workflows. Furthermore, manual catalog extraction by platform staff does not scale.
* **Decision:** 
  1. Focus initial merchant acquisition exclusively on **online social media merchants (Instagram, Facebook, and TikTok shops)**. Telegram is excluded from current focus.
  2. Enforce a **Self-Serve with Rules Onboarding Model**: Cheapify defines clear quality standards, catalog rules, and onboarding instructions; merchants build their stores and upload their own product media and data.
  3. **Founding Merchant Ad Boost:** The first 20 verified stores receive 0% commission in Month 1 and get their products featured in Cheapify's paid ad campaigns (Facebook, Instagram, TikTok), providing them free advertising and commercial boosts.
  4. Platform access is delivered across **both Mobile App (iOS & Android) and Web**.

### ADR-009: Official UI Design Language — "Clean Flat + Soft Depth"
* **Date:** 2026-10-17
* **Status:** Accepted
* **Context:** With the PMS color system, tri-font typography, and logo hierarchy locked, Cheapify still lacked a formal UI design *style* — the surface treatment, depth model, and overall visual character governing every screen, card, and component across the mobile app and web platform. Eight candidate styles drawn from current design-trend research (Figma 2026 trends, industry e-commerce analyses) were rendered as live visual samples using the official PMS palette and brand fonts in [`../assets/design-style-previews/index.html`](../assets/design-style-previews/index.html) and evaluated by the founder.
* **Decision:** Adopt **"Clean Flat + Soft Depth"** as the official Cheapify UI design language:
  1. **Flat white surfaces** (`#FFFFFF`) floating on light neutral backgrounds (`#DDE5ED` / `#F4F6F8`).
  2. **Soft depth model:** single diffuse shadow (`0 8px 24px rgba(16,24,32,.08)` max) + hairline `1px` borders; a strict 3-level elevation scale (base → card → modal). No hard offset shadows, no color-tinted shadows.
  3. **Generous radii:** `12px–16px` cards, `10px–12px` buttons, pill-shaped badges — matching Comfortaa's rounded geometry.
  4. **Disciplined accent usage:** PMS Blue reserved for primary CTAs/active states; PMS Green reserved exclusively for Best Value badges, savings, and verified signals.
* **Rejected styles:** Vibrant Dopamine (visual fatigue, brand-color drift risk), Neumorphic Fintech (fails contrast/accessibility), Glassmorphism (readability + old-device performance), Claymorphism (undermines operational precision), Gamified Deal-Hunting (HUD clutter conflicts with Everyman accessibility), Bento Grid (adopted only as an *optional layout pattern* for stat tiles, not a surface style), Editorial Zero-UI (too austere for deal-hunting energy).
* **Consequence:** All UI components, merchant dashboard screens, and marketing mockups must follow the tokens defined in Section 8.0 of [`../marketing/02_brand_identity_and_guidelines.md`](../marketing/02_brand_identity_and_guidelines.md). Recorded as Preference 25 in [`preferences.md`](preferences.md).

### ADR-010: Official Platform Domain Selection — `getcheapify.com`
* **Date:** 2026-10-17
* **Status:** Accepted (Purchased on Cloudflare Registrar)
* **Context:** With `cheapify.com` and `cheapify.app` already taken by third parties, Cheapify required a permanent, authoritative primary web domain and digital hub to serve its dual-sided marketplace (iOS/Android mobile app and web platform). The domain needed to convey instant trust to everyday consumers in Iraq and the Kurdistan Region, prevent typo-leakage, and integrate seamlessly with Cloudflare's zero-markup DNS and security infrastructure.
* **Decision:** Acquire and standardize on **`getcheapify.com`** as the official primary root domain:
  1. **`.com` Subconscious Authority:** Everyday shoppers across Iraq instinctively trust `.com` over newer or less familiar TLDs.
  2. **Active Conversion Verb:** The `"Get"` prefix functions as an active invitation to download the app and unlock savings (*"Get Cheapify on App & Web"*), following the proven path of top consumer platforms like Dropbox (`getdropbox.com`) and Pocket (`getpocket.com`).
  3. **Zero Typo-Leakage:** Protects brand traffic from accidental typos that occur with `.co` (where users instinctively type `.com` and land on squatted pages).
  4. **Cloudflare Infrastructure:** Managed directly on Cloudflare Registrar at wholesale cost with free DNSSEC, SSL, and DDoS mitigation.
* **Consequence:** All production endpoints (`api.getcheapify.com`), merchant web portals (`merchant.getcheapify.com`), customer links, packaging print collateral, and marketing CTAs will standardize on `getcheapify.com`. Recorded as Preference 27 in [`preferences.md`](preferences.md).



### ADR-011: Content Marketing Strategy — Pre-Launch Audience Building & Two-Phase Plan
* **Date:** 2026-10-18
* **Status:** Accepted
* **Context:** With the brand identity complete and the MVP 1–3 months away, Cheapify needed a publishing strategy for Facebook, Instagram, and TikTok covering both the empty period before launch and the launch itself.
* **Decision:**
  1. **Start posting before the MVP exists** — framed strictly as audience-building (documenting the price-variation problem, recruiting founding merchants, building the waitlist). Never as a product launch; no hard feature promises or dates until the MVP date is locked.
  2. **Two-phase structure:** Phase A ([`../marketing/03_pre_launch_content_plan.md`](../marketing/03_pre_launch_content_plan.md)) is a repeatable weekly template cycled until MVP; Phase B ([`../marketing/04_launch_content_calendar.md`](../marketing/04_launch_content_calendar.md)) is a fixed T-7 countdown → launch week → 8-week post-launch calendar, activated when the launch date is confirmed and ≥10 founding merchants are committed.
  3. **Unified cross-platform model (Preference 28):** one concept → one 9:16 master file → three native uploads. No platform-exclusive content; captions adapted per platform norms; no cross-platform watermarks.
  4. **Language policy (Preference 29):** Kurdish (Badînî) audio + a single burned-in Kurdish subtitle track + Kurdish-first/Arabic caption on one post. No separate-language posts, no dual subtitle tracks, no English in launch content.
  5. **Verification & brand guardrails (Preference 30):** real verifiable prices only; store identities blurred; zero emojis; PMS palette and trilingual font system enforced via a pre-publish checklist.
* **Consequence:** All social content produced for Cheapify follows the series system (Price Detective, DM Hell, Founder's Circle, Build in Public, Bazaar Wisdom), the weekly template, and the language/subtitle rules defined in the two plan documents.

### ADR-012: Referral System & Catalog First-Mover Incentive Architecture
* **Date:** 2026-10-18
* **Status:** Accepted
* **Context:** Two growth-design problems needed solving before launch: (1) referral rewards are trivially farmed if they pay on signup, and the program must work in all four directions (shopper↔merchant); (2) in the Single-SKU catalog, the first merchant to create a listing does all the work while later merchants claim it in one tap — an asymmetry that discourages anyone from going first.
* **Decision:**
  1. **Transaction-gated referrals (Preference 31):** every reward in every direction unlocks only on a completed, courier-confirmed order — never on signup. All rewards are non-transferable platform credit (60-day expiry, one per order). Four-direction grid: Shopper→Shopper (free first delivery + 3k credit), Shopper→Merchant (nominate a shop → 3 free deliveries after the shop completes 10 orders), Merchant→Shopper (free first delivery + growth points → ad boosts, Best Value winners as default creative), Merchant→Merchant (1% take-rate rebate for 60 days). Anti-fraud stack: OTP identity, velocity caps, device/address heuristics, courier delivery signals, manual review.
  2. **Catalog first-mover incentive (Preference 32):** barcode-first listing creation (auto-fill from product databases, template fallback for unbranded goods); 1,000 IQD creation bounty per approved master listing (commission-offset credit); 250 IQD micro-bounty for approved improvements to existing listings; creator attribution is permanent but the master page is shared infrastructure — improvements are QA-approved proposals, never direct edits. No platform-side catalog seeding (founder decision — catalog is 100% merchant-driven).
* **Consequence:** Full specification in [`../platform/referral_and_growth_incentives.md`](../platform/referral_and_growth_incentives.md). Reward values are founder-tunable (§8 of the spec); incentive spend is a capped marketing budget line in the operational budget.
