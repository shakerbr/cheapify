# Cheapify — Catalog Governance
## Listing Process · Listing Rules & Policies · Duplicate-Matching Strategy

**Category:** Cross-Cutting Platform Specification
**Status:** Draft Working Standard (ADR-013) — *split from [`operational_policies.md`](operational_policies.md)*
**Cross-References:**
- Catalog incentives & first-mover bounty: [`referral_and_growth_incentives.md`](referral_and_growth_incentives.md) §4
- Merchant Rulebook (GTM §2.4): [`../marketing/01_two_sided_gtm_strategy.md`](../marketing/01_two_sided_gtm_strategy.md)
- Best Value ranking (depends on Single-SKU integrity): [`best_value_algorithm_strategy.md`](best_value_algorithm_strategy.md)

---

## 1. Listing Creation Process

### 1.1 The First-Mover Problem Being Solved

In a Single-SKU catalog, the first merchant to list a product does the heavy work — photos, name, description, specs — while every later merchant claims the existing page in one tap and only adds price, stock, and variants. Without compensation, rational merchants wait for others to do the work, and the catalog never fills. The process below is designed so that creation is nearly free (barcode-first) *and* compensated (bounty — see §1.3).

### 1.2 The Four-Step Flow [Policy]

1. **Match first:** merchant scans barcode (EAN/UPC) or searches catalog. If the SKU exists → **claim it**: add price, stock, variants — done in one tap.
2. **Create:** if no match, barcode auto-fills name/specs/reference imagery from aggregated product databases; unbranded items use the guided template.
   - **Coverage is strong for branded goods** (chargers, cables, perfumes, branded accessories) — precisely the SKUs duplicated across merchants where the first-mover asymmetry hurts most.
   - **Local/unbranded goods** fall back to the guided template — barcode handles the high-duplication core; templates handle the tail.
3. **Merchant data:** their own price, stock count, available colors/measurements, optional own photos.
4. **QA gate (< 2h):** automated checks + spot review → live or returned with a specific fix note.

### 1.3 Creator Economics

Approved creation = **1,000 IQD commission-offset credit** + permanent attribution; approved improvements by other merchants = **250 IQD micro-bounty**; anchor offers get 7-day "New Arrival" visibility. Full bounty spec: [`referral_and_growth_incentives.md`](referral_and_growth_incentives.md) §4.

---

## 2. Listing Rules & Policies

**[Policy] Extends the Merchant Rulebook (GTM §2.4) — the full listing rule set:**

| # | Rule | Enforcement |
| :--- | :--- | :--- |
| 1 | **Price integrity:** Cheapify price ≤ merchant's social-media price | Periodic audit + shopper reports; violation = listing suspended |
| 2 | **Media quality:** real product photos, packaging visible, all variants shown | QA gate at creation |
| 3 | **No watermarks** containing phone numbers, social handles, or external store names | Auto-detection + QA |
| 4 | **Live stock accuracy** | Cancellation for unlisted out-of-stock = reliability deduction |
| 5 | **Honest condition:** New / Used / Refurbished labeled correctly | Fault returns auto-trigger on mislabel |
| 6 | **Variant honesty:** listed colors/sizes must be in stock | Order-level verification |
| 7 | **Prohibited goods:** weapons, prescription meds, counterfeit/branded fakes, adult items, anything illegal under Iraqi/KRI law | Immediate removal + account action |
| 8 | **No duplicate listings** — one SKU, one master page, always | §4 matching system |

---

## 3. Shared Ownership — Master Pages Are Infrastructure, Not Property

**[Policy]** The master page belongs to the platform, not to whoever typed first:

- The creator keeps permanent **"listed this product" attribution** on the page and their creation credit — never revoked.
- **Any verified merchant selling that product may propose improvements** (better photo, missing spec, corrected description, additional variants). Proposals queue for QA — nobody edits the page directly.
- **Approved improvements earn the 250 IQD micro-bounty**, so a weak first listing doesn't stay weak, and a merchant who finds a poor page profits by fixing it instead of duplicating it.
- **Full change history** on every master page — every edit attributed, reversible.

**Result:** being first is rewarded (credit + attribution + anchor visibility), but quality is communal — the catalog improves monotonically instead of rewarding first-come-low-effort listings.

---

## 4. Listing-Matching Strategy (Duplicate Prevention)

Single-SKU integrity is what makes Best Value possible — duplicates are the system's enemy #1. Four layers of defense:

**Layer 1 — Barcode exact match [Policy]:**
EAN/UPC scan returns the existing master page instantly. A barcode already in the catalog **cannot** spawn a second page — the create flow routes to claim. Hard block, no review needed.

**Layer 2 — Intelligent multi-signal match at creation [Policy]:**
For items without barcodes, creation requires searching first. An intelligent matching system scores the candidate against the catalog across **multiple signals**, not just the name:

| Signal | What it compares |
| :--- | :--- |
| **Text** | Normalized name + description across Kurdish/Arabic/Latin aliases; brand, model numbers, key specs |
| **Visual** | Image similarity — perceptual hashing + embeddings catch the same product photo'd differently |
| **Taxonomy** | Category, tags, and variant structure (e.g. two "20,000mAh power banks" in Electronics) |
| **Attributes** | Capacity, color set, size range, condition — spec-level overlap |

The engine combines these into a **confidence score**:

- **High confidence** → strong candidate list shown with *"Is this your product?"* — merchant must explicitly confirm "no match" before creating, and claiming is one tap. Creation without a claimed match is allowed but logged.
- **Medium confidence** → candidates shown + flagged for QA review alongside the listing approval.
- **Low confidence** → create proceeds normally.

The score thresholds and signal weights are tunable as real duplicate data accumulates during the pilot — start strict (favor false "possible match" prompts over missed duplicates), then relax.

**Phased intelligence [Policy]:**
- **Launch version:** barcode + normalized trilingual text + category/spec filters — deterministic, no ML dependency.
- **Post-pilot evolution:** add multilingual text embeddings (cross-lingual semantic match), vision embeddings (same product, different photos), and ML-extracted attributes from free-text descriptions — using off-the-shelf models, no custom training.
- **Learned thresholds:** every merchant claim/rejection during the pilot is labeled training data; the matcher's weights and thresholds are learned from real decisions, not guessed.
- **Why staged:** the simple version catches most duplication (barcode + search handles the high-duplication core) and never blocks launch; ML versions arrive when pilot data exists to tune them.

**Layer 3 — Community + QA detection [Policy]:**

- Merchants and shoppers can flag "this listing is a duplicate" → QA compares photos/specs/prices → merge if confirmed.
- The flag that found a true duplicate earns the reporter's goodwill (log as contribution; no cash reward — prevents flag-spam).

**Layer 4 — Merge process [Policy]:**

- Duplicates are merged onto the better master page (media/spec quality wins); offers migrate intact.
- The merged-away listing's creator loses the creation credit **only if the duplicate was created after the canonical page existed** (prevents farming credits via near-duplicates).
- Intentional repeat duplicators lose listing-creation privilege entirely.

**[Assumption] Alias table:** Kurdish/Arabic/English product-name aliases are maintained centrally and grow from claim behavior — over time the fuzzy match improves without extra work.

---

## 5. Open Items Requiring Real-World Data

| Item | Needed input | Blocks |
| :--- | :--- | :--- |
| Prohibited-goods legal review | KRI commerce regulation check | Compliance (§2 Rule 7) |
| Barcode database coverage | Test lookups on top 50 Duhok SKUs | §1 auto-fill reliability |
