# Cheapify

We are building **Cheapify** from the ground up from zero.

---

## Mandatory Agent Operating Rules

Every AI agent working on **Cheapify** MUST follow these rules strictly:

1. **Pre-Action Context Verification (Always Read First):**
   - You MUST inspect and review [AGENTS.MD](AGENTS.MD) and all files in [agent/](agent/) before performing any work or executing any tasks in the workspace.
2. **Persistent User Rules:**
   - Whenever the user defines or states a rule, you MUST record it in [agent/rules.md](agent/rules.md) and [AGENTS.MD](AGENTS.MD) and enforce it strictly across all actions.
3. **Persistent User Preferences & Methods:**
   - Whenever the user asks you to do something in a specific way, you MUST immediately record it in [agent/preferences.md](agent/preferences.md) so the user never has to repeat instructions.
4. **Single-Purpose File Breakdown:**
   - Keep context, tracking, and management files broken down, simple, and specific for ONE thing only inside [agent/](agent/).
5. **Always Maintain an Updated Plan & Roadmap:**
   - You MUST maintain a real-time, comprehensive plan and roadmap in [agent/roadmap.md](agent/roadmap.md).
6. **Always Maintain Immediate Task Focus:**
   - You MUST maintain immediate actionable checklist and work items in [agent/active-tasks.md](agent/active-tasks.md) so you always know what you are doing right now.
7. **Always Maintain an Updated Progress Log:**
   - You MUST maintain a running chronological log of completed tasks, milestones, and architectural decisions in [agent/progress.md](agent/progress.md).
8. **Build All 4 Pillars from Zero Before Pitch Deck:**
   - Do NOT rely on or treat archived pitch decks as final. Build all 4 pillars from the ground up first (1. Entrepreneurship, 2. Marketing, 3. Finance Management, 4. Business Modeling). The final presentation will be assembled only once all 4 pillars are complete.
9. **Strictly Relative Links in Repository Documents:**
   - For links inside documents, never use absolute paths or `file:///` URLs (e.g. `file:///media/shakerbr/...`). Always use clean relative links (e.g. `assets/evidence/...` or `entrepreneurship/...`).

---

### Dedicated Management & Context Directory (`agent/`)
- **Rules:** [agent/rules.md](agent/rules.md) — Strict rules set by the user.
- **Preferences:** [agent/preferences.md](agent/preferences.md) — User working styles, methods, and habits.
- **Project Context:** [agent/project-context.md](agent/project-context.md) — Fast one-page executive overview.
- **Strategic Roadmap:** [agent/roadmap.md](agent/roadmap.md) — 4-pillar milestones and roadmap.
- **Active Tasks:** [agent/active-tasks.md](agent/active-tasks.md) — Current focus and task checklist.
- **Progress Log:** [agent/progress.md](agent/progress.md) — Chronological ledger of all completed work.
- **Decisions Log:** [agent/decisions.md](agent/decisions.md) — Architecture and business decision records (ADR).

---

### Cross-Cutting Platform Specifications (`platform/`)
Semi-general operational, economic, and technical specifications shared across pillars:
- **Platform Fee Structure & Monetization:** [platform/fee_structure_and_monetization.md](platform/fee_structure_and_monetization.md) — Progressive Marginal Tiering (5% Tier 1, 3% Tier 2, 1.5% Tier 3), mathematical elimination of the cliff effect, multi-category simulations, and weekly COD reconciliation workflow.
- **Hybrid "Best Value" Algorithm Strategy:** [platform/best_value_algorithm_strategy.md](platform/best_value_algorithm_strategy.md) — Total Landed Cost ($P_{\text{total}} = P_{\text{item}} + D_{\text{tariff}}$), proximity advantage protecting local bazaar shops, 3-tier deterministic hierarchy, diagnostic merchant dashboard, and TypeScript engine.

---

### Active Development: 4 Program Pillars
- **1. Entrepreneurship (Complete):** [01_problem_solution_value.md](entrepreneurship/01_problem_solution_value.md) | [02_market_opportunity_and_sizing.md](entrepreneurship/02_market_opportunity_and_sizing.md) | [03_customer_and_merchant_personas.md](entrepreneurship/03_customer_and_merchant_personas.md) | [04_competitive_landscape_matrix.md](entrepreneurship/04_competitive_landscape_matrix.md) | [05_market_validation_survey.md](entrepreneurship/05_market_validation_survey.md) | [06_value_proposition_and_founder_fit.md](entrepreneurship/06_value_proposition_and_founder_fit.md) — Built 100% from ground zero.
- **2. Marketing (Active Focus):** [01_two_sided_gtm_strategy.md](marketing/01_two_sided_gtm_strategy.md) (Complete) | [02_brand_identity_and_guidelines.md](marketing/02_brand_identity_and_guidelines.md) (Complete — Strict PMS colors, outline logo mark, Comfortaa+Inter+IBM Plex typography, dual-tier taglines) | Setting up 30-day content calendar (03).
- **3. Finance Management (Queued):** Will be built 100% fresh from ground zero (itemized operational budget, unit economics, cash flow, and break-even analysis). Past coursework files in `archive/finance-management/` are archived reference assignments only, not final budget figures.
- **4. Business Modeling (Later):** 9-Block Business Model Canvas, core SOPs, and operational risk matrix.

### Archive & Reference Materials
All past incubator research, GIZ program notes, pitch decks, and previous reference extractions are archived under `archive/`:
- `archive/extracted-reference/`: Extracted blueprint documents (Product spec, Brand guidelines, Technical architecture, Operations playbook, Logo SVG) for future reference if needed.
- `archive/program-giz-cheapify/`: Pitch decks, brand guideline presentations, assignments, and media screenshots.
- `archive/chats/`: Raw chat logs and problem/opportunity discussions.
