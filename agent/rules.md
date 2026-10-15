# Agent Operating Rules

These are the strict, mandatory rules set by the user. The AI agent must adhere to them without exception.

---

1. **Pre-Action Context Verification:**
   - Before taking any action or executing any tasks in the workspace, you MUST view and inspect all files in `agent/` and [AGENTS.MD](../AGENTS.MD).

2. **Single-Purpose File Breakdown:**
   - Keep context and management files broken down, simple, and specific for ONE thing only. Do not combine disparate tracking concerns into a single file.

3. **Persistent User Rules:**
   - Whenever the user defines or states a rule, record it in this file (`agent/rules.md`) and in [AGENTS.MD](../AGENTS.MD) immediately and enforce it strictly.

4. **Persistent User Preferences & Methods:**
   - Whenever the user asks you to do something in a specific way, record that method or preference in [`preferences.md`](preferences.md) immediately so the user never has to repeat it.

5. **Updated Roadmap & Plan:**
   - Always maintain the high-level roadmap and milestone statuses in [`roadmap.md`](roadmap.md).

6. **Clear Current Task Focus:**
   - Always maintain immediate task items and current work state in [`active-tasks.md`](active-tasks.md). Always know what you are doing.

7. **Living Progress Tracking:**
   - Always log what has been done, including file changes and milestones, in [`progress.md`](progress.md).

8. **Build All 4 Pillars from Zero Before Pitch Deck:**
   - Do NOT rely on or treat archived pitch decks as final. Build all 4 pillars from the ground up first (1. Entrepreneurship, 2. Marketing, 3. Finance Management, 4. Business Modeling). The final presentation will be assembled only once all 4 pillars are complete.

9. **Strictly Relative Links in Repository Documents:**
   - For links inside documents, never use absolute paths or `file:///` URLs (e.g. `file:///media/shakerbr/...`). Always use clean relative links (e.g. `assets/evidence/...` or `../entrepreneurship/...`).


