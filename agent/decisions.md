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

