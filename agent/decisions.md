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
* **Context:** Seed capital from GIZ ($2,200 ask) is limited. Traditional software agencies charge $5,000+ to build a marketplace.
* **Decision:** Founder Shakir Bashar (computer engineer) builds the entire web platform, APIs, database, and marketing demo videos in-house. 100% of donor funding goes directly to real third-party operational costs (servers, Cloudflare, WhatsApp Cloud API, Duhok ads, Chamber registration).

### ADR-004: Asset-Light 3PL Logistics Model
* **Date:** 2026-10-12
* **Status:** Accepted
* **Context:** Purchasing delivery motorbikes or hiring full-time drivers is capital-intensive and risky for an early pilot.
* **Decision:** Partner directly with established third-party logistics couriers in Duhok (e.g. ZMC Express / local delivery couriers) at standard market parcel rates (3,000 IQD / order), handling automated waybills and COD reconciliation.

### ADR-005: Tiered Value-Based Monetization
* **Date:** 2026-10-12
* **Status:** Accepted
* **Context:** Flat 10%–15% commission models alienate local retailers whose gross margins on electronics and accessories are narrow.
* **Decision:** Use an accessible tiered take-rate: 5% for items under 9,000 IQD, flat 1,000 IQD for 10,000–99,000 IQD, 2% for 100,000–499,000 IQD, and 1.5% for ≥500,000 IQD.

### ADR-006: Ground-Up 4-Pillar Construction Before Final Pitch Deck
* **Date:** 2026-10-14
* **Status:** Accepted
* **Context:** Archived pitch decks (`archive/program-giz-cheapify/Cheapify Pitch Deck.pdf`) were created as partial, non-final artifacts during early incubator assignments and do not represent the complete venture.
* **Decision:** Treat the project as starting from ground zero. Build all 4 program pillars completely in sequence (1. Entrepreneurship, 2. Marketing, 3. Finance Management, 4. Business Modeling). Assemble and design the final pitch deck and showcase presentation strictly after all 4 pillars are fully built.


