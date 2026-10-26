# Cheapify — Decisions & Topics Parking Lot

**Purpose:** a lightweight scratchpad for ideas and open questions raised during development — *before* they are big enough to become documents, ADRs, or tasks. Anything here is **not decided yet**. When an item is settled, it moves to Resolved with a pointer to where it was decided, or it graduates into [`active-tasks.md`](active-tasks.md) / [`decisions.md`](decisions.md).

**How to use:** drop a bullet under Open Topics any time. No structure needed — a phrase is enough.

---

## Open Topics

- **Platform fee on returned orders** — keep the 950 IQD fee or refund it? Refunding costs ~38 IQD/order (break-even ~605/mo). Policy is silent today (`platform/operational_policies.md` §1, `finance/01` §8).
- **Legal-name language** — register the legal trade name in Kurdish/Arabic (Chamber fee ~540k) vs. English (~1,140k)? The grant budgets the English name; the Kurdish/Arabic option saves ~$400.
- **Catalog-bounty saturation at launch** — founding stores' SKU-creation bounties will exceed the 225k/mo pool; claims queue as a deferred credit liability. Consider a launch-month cap or paying founding stores' bounties inside the founding package.

---

## Resolved / Graduated

| Topic | Where it was decided | Reference |
| :--- | :--- | :--- |
| Return Policy | Two-class model: fault → merchant pays; remorse → customer pays; 48h window | [`../platform/operational_policies.md`](../platform/operational_policies.md) §1 (ADR-013) |
| Shipping Policy | Flat 3,000 IQD inside Doorstep Total; one free re-attempt | §2 (ADR-013) |
| Packaging Policy | Sealed opaque mailer + waybill; security tape ≥50k IQD | §3 (ADR-013) |
| Payment Methods | COD from launch, card / e-wallet shortly after; courier transfers cash electronically; merchant payout automatic after the 48h return window | §4 (ADR-013) |
| Listing Making Process | Barcode-first create/claim flow, QA gate <2h | [`../platform/catalog_governance.md`](../platform/catalog_governance.md) §1 (ADR-013) |
| Listing Rules & Policies | 8-rule enforceable listing standard | [`../platform/catalog_governance.md`](../platform/catalog_governance.md) §2 (ADR-013) |
| Listing Matching / Dedup | 4-layer defense: barcode block → fuzzy match → flags → merge | [`../platform/catalog_governance.md`](../platform/catalog_governance.md) §3 (ADR-013) |
| Referral system design | Transaction-gated, four directions, referrer-only rewards | [`../platform/referral_and_growth_incentives.md`](../platform/referral_and_growth_incentives.md) (ADR-012) |
| Catalog first-mover incentive | 1,000 IQD creation bounty + 250 IQD improvement bounty | Same doc, §4 (ADR-012) |

Items marked `[Assumption]` inside those documents still need real-world quotes or founder confirmation — see operational_policies.md §5 and catalog_governance.md §4.
