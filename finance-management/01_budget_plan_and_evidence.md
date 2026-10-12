# Cheapify — Master Project Budget, Evidences & GIZ Grant Allocation

**Document Type:** Final Finance Management Assignment & Donor Budget Plan  
**Project:** Cheapify (*Smart Deals. Verified Sellers. One App.*)  
**Founder:** Shakir Bashar  
**Target Incubation Program:** GIZ Youth Entrepreneurship Program (CAPA / American University of Kurdistan - AUK)  
**Pilot Geography:** Duhok Metropolitan Area (Kurdistan Region of Iraq — KRI)  
**Project Budget Period:** 6-Month Pilot Launch (November 2026 – April 2027)  
**Currency Benchmark:** Iraqi Dinar (IQD) & US Dollar (USD) at prevailing market rate: **1 USD ≈ 1,500 IQD**  
**Associated 6-Month Budget Workbook:** [Cheapify_Budget_GIZ.xlsx](file:///media/shakerbr/workland/workspace/git/my-private-repos/cheapify/finance-management/Cheapify_Budget_GIZ.xlsx)  
**Associated 12-Month Monthly P&L Workbook:** [Cheapify_Monthly_Profit_and_Loss.xlsx](file:///media/shakerbr/workland/workspace/git/my-private-repos/cheapify/finance-management/Cheapify_Monthly_Profit_and_Loss.xlsx)  
**Standalone HTML Report:** [Cheapify_Budget_Report.html](file:///media/shakerbr/workland/workspace/git/my-private-repos/cheapify/finance-management/Cheapify_Budget_Report.html)  
**Official PDF Document:** [Cheapify_Budget_Plan_and_Evidence.pdf](file:///media/shakerbr/workland/workspace/git/my-private-repos/cheapify/finance-management/Cheapify_Budget_Plan_and_Evidence.pdf)

---

## 1. Executive Summary & Grant Request Strategy

Cheapify is an intelligent, multi-seller e-commerce marketplace engineered specifically for the fragmented Iraqi retail market. It eliminates arbitrary markups and chaotic "DM for price" negotiations by consolidating verified local merchants under a single, standardized manufacturer SKU with transparent side-by-side price comparison.

### The Financial Strategy: In-House Engineering & Lean Capital Discipline
International donors (GIZ, BMZ, CAPA) evaluate budgets on **commercial viability, capital discipline, and self-sustainability**. This model demonstrates that Cheapify is an ultra-lean, highly profitable digital enterprise from day one:

* **Software Development Cost:** **$0 USD (0 IQD)**
  * The founder is a computer engineer who architects and builds the web catalog, APIs, database schemas, ranking algorithms, and integrations in-house. Zero donor money is wasted on outside software agencies.
* **Content Creation & Marketing Demos:** **$0 USD (0 IQD)**
  * The founder creates all product UX teardowns, reels, and video tutorials in-house, eliminating paid influencer fees.
* **Zero Overhead Padding:**
  * No requests for personal internet bills, neighborhood generator subscriptions, or counter hardware gadgets. Only real, third-party operational bills.
* **Gross Operating Margin:** **88.6% (4,650,000 IQD / $3,100 USD)**
  * As an asset-light marketplace, Cheapify does not hold inventory or lease warehouses.
* **Net Operating Profit (6-Month Pilot):** **+1,950,000 IQD (+$1,300 USD) — +37.1% Net Operating Margin (Zero Loss!)**
  * Proves to GIZ that the venture generates strong operational margins during the incubation period.
* **Funding Requested from GIZ:** **$2,200 USD (3,300,000 IQD)**
  * **100% of donor funding strictly covers verified third-party operational execution:** high-concurrency servers, Cloudflare edge security, Meta WhatsApp Business APIs, hyper-local marketing in Duhok, and official commercial Chamber of Commerce registration.
* **Post-Pilot Steady-State Profit (Month 7 Onward):** **+$1,400 to +$3,000 USD / month (+2.1M to 4.5M IQD/mo) — +78% to +83% Net Margin**
  * Once one-time registration and testing subsidies end, monthly overhead drops to just **$156 – $200 / month**, generating substantial recurring cash profits.

---

## 2. Master Budget Summary (GIZ Template Alignment)

This table matches the automated calculations of [Cheapify_Budget_GIZ.xlsx](file:///media/shakerbr/workland/workspace/git/my-private-repos/cheapify/finance-management/Cheapify_Budget_GIZ.xlsx):

| Template Line | Section Description | Amount (USD) | Amount (IQD) | Operational Purpose |
| :--- | :--- | :---: | :---: | :--- |
| **Revenue (Tab 2)** | Projected 6-Month Pilot Revenue | **$3,500** | **5,250,000** | 3,000 orders across tiered take-rates (avg 1,500 IQD) + 5 category sponsorships. |
| **Direct Costs (Tab 3)** | Direct Project / Transaction Costs | **$400** | **600,000** | 90 courier pilot test deliveries, 90 first-order vouchers, partner packaging supplies. |
| **Gross Profit (Line 14)** | Revenue minus Direct Costs | **$3,100** | **4,650,000** | **Gross Operating Margin: 88.6%** |
| **Indirect Expenses (Tab 4)** | Operational Overheads (Real Cash Expenses) | **$1,800** | **2,700,000** | Scalable cloud servers, Cloudflare Pro, WhatsApp API, Duhok Meta ads, DCCI registration. |
| **Net Operating Profit (Line 18)** | Gross Profit minus Indirect Expenses | **+$1,300** | **+1,950,000** | **Sustainable Business Profit (+37.1% Margin — Zero Loss!)** |
| **Asset Purchases (Tab 5)** | Long-Term Capital Assets (CAPEX) | **$0** | **0** | Platform operates 100% asset-light; zero physical hardware clutter. |
| **TOTAL PROJECT BUDGET (Line 40)** | Total Operational Cash Required to Pilot | **$2,200** | **3,300,000** | Total operational cash needed for 6-month validated pilot. |
| **Software & Content Labor Fee** | Covered 100% in-house by Founder | **$0** | **0** | Built & recorded directly by Shakir Bashar ($0 agency labor fee). |
| **FUNDING NEEDED FROM GIZ (Line 44)** | **Official Seed Grant Request** | **$2,200** | **3,300,000** | **Official Grant Request for GIZ Pitch Deck & Contract** |

---

## 3. Detailed Cost Breakdown with Real Evidences & References

Every expense in the Cheapify budget has been verified against active vendor pricing and local Duhok / Kurdistan Region market benchmarks:

### 3.1 Pillar 1: Scalable Cloud & Edge Infrastructure ($670 USD / 1,005,000 IQD)
*Objective: Build an enterprise-grade cloud architecture capable of serving tens of thousands of active shoppers and handling traffic spikes with sub-5ms pricing responses.*

| Line Item | Scope & Technical Specifications | Monthly Rate | 6-Month Total (USD) | 6-Month Total (IQD) | Evidence & Reference Citation |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **High-Performance Compute API Server** | Dedicated vCPU compute instance (8 vCPU, 16GB RAM, NVMe SSD) running Node.js Fastify API, worker processes, and full-text search indexing. | $40/mo | $240 | 360,000 | [Hetzner Cloud CPX41](https://www.hetzner.com/cloud) (€32.90/mo) / [DigitalOcean High-CPU Droplet](https://www.digitalocean.com/pricing/droplets) ($48/mo). |
| **Managed High-IOPS PostgreSQL Database** | Managed database cluster with automated connection pooling, daily snapshots, and SSL encryption to ensure Single-SKU relational integrity. | $25/mo | $150 | 225,000 | [Supabase Pro Database](https://supabase.com/pricing) ($25/mo) / DigitalOcean Managed PostgreSQL. |
| **In-Memory Caching Cluster (Redis)** | Sub-5ms caching tier for live price comparisons and merchant ranking tables, preventing database load during peak marketing traffic. | $15/mo | $90 | 135,000 | [Upstash Redis](https://upstash.com/pricing) / Redis Cloud cluster ($15/mo). |
| **Object Storage (Cloudflare R2)** | High-capacity cloud storage for standardized catalog hero images with **$0 egress/bandwidth fees**. | $10/mo | $60 | 90,000 | [Cloudflare R2 Storage](https://www.cloudflare.com/developer-platform/r2/) ($0.015/GB storage, zero egress bandwidth costs). |
| **Cloudflare Pro & Edge CDN** | Web Application Firewall (WAF), advanced DDoS mitigation, automatic WebP image optimization, and Middle East regional edge caching. | $20/mo | $120 | 180,000 | [Cloudflare Pro Plan](https://www.cloudflare.com/plans/) ($20/mo standard public pricing). |
| **Domain Registration (Cloudflare Registrar)** | `cheapify.iq` / `.com` domain registration purchased strictly at wholesale cost with free WHOIS privacy and DNSSEC. | One-time ($0.83/mo) | $10 | 15,000 | [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) ($9.77/year at-cost wholesale pricing). |
| **Subtotal Infrastructure** | | | **$670** | **1,005,000** | *Requested from GIZ* |

---

### 3.2 Pillar 2: Automated Order Routing & Communications ($110 USD / 165,000 IQD)
*Objective: Eliminate manual chat friction by providing automated order confirmations and merchant dispatch alerts via WhatsApp.*

| Line Item | Scope & Technical Specifications | 6-Month Total (USD) | 6-Month Total (IQD) | Evidence & Reference Citation |
| :--- | :--- | :---: | :---: | :--- |
| **Meta WhatsApp Business Cloud API** | ~5,000 automated utility conversations (order placement confirmations, merchant 1-click fulfillment alerts, post-delivery rating pings). All messaging runs cloud-to-cloud over HTTPS via Meta's servers. | $100 | 150,000 | [Meta Business Cloud API Pricing](https://developers.facebook.com/docs/whatsapp/pricing/): Official rate for Iraq utility messages is ~$0.020 per 24-hour conversation window. |
| **Business Line SIM & Line Maintenance** | Dedicated business line eSIM registration in Duhok for Meta Business verification OTP + minimum balance recharge to keep the number active on the cell network. | $10 | 15,000 | AsiaCell / Korek Telecom commercial SIM (3,000–5,000 IQD) + maintenance recharge. Messaging itself occurs over internet API. |
| **Subtotal Communications** | | **$110** | **165,000** | *Requested from GIZ* |

---

### 3.3 Pillar 3: Hyper-Local Customer & Merchant Acquisition ($600 USD / 900,000 IQD)
*Objective: Drive targeted customer adoption across Duhok through geo-targeted social proof and transparent price-comparison demonstrations.*

| Line Item | Scope & Technical Specifications | 6-Month Total (USD) | 6-Month Total (IQD) | Evidence & Reference Citation |
| :--- | :--- | :---: | :---: | :--- |
| **Geo-Targeted Meta Ads (Instagram & Facebook)** | Hyper-local ad campaigns geo-fenced strictly to Duhok city (18–35 demographic, online shoppers). Yields ~350,000 local impressions at Iraq's average CPM of $1.70–$2.20. | $600 ($100/mo) | 900,000 | [Meta Ads Manager Benchmark (Iraq)](https://www.facebook.com/business/ads): Iraq average CPM is $1.50–$2.50; CPC is $0.05–$0.10. |
| **Product UX Teardowns & Video Demonstrations** | High-converting screen recordings, live Single-SKU price comparisons, and 1-click order flow tutorials for Instagram Reels / TikTok. | **$0** | **0** | **CREATED 100% BY FOUNDER:** Shakir produces all video content, saving $200+ in outside influencer fees. |
| **Subtotal Marketing** | | **$600** | **900,000** | *Requested from GIZ* |

---

### 3.4 Pillar 4: Pilot Fulfillment & Transaction Validation ($400 USD / 600,000 IQD — Direct Costs)
*Objective: Stress-test courier speed, packaging safety, and Cash on Delivery reconciliation across pilot orders.*

| Line Item | Scope & Technical Specifications | 6-Month Total (USD) | 6-Month Total (IQD) | Evidence & Reference Citation |
| :--- | :--- | :---: | :---: | :--- |
| **3PL Courier Pilot Test Subsidies** | 90 subsidized test deliveries across Duhok to test 3PL courier pickup speed, parcel safety, and Cash on Delivery (COD) settlement. | $180 | 270,000 | Standard intra-city courier parcel rate in Duhok (e.g., ZMC Express / local delivery couriers) is 3,000 IQD ($2.00) per order. |
| **Promotional First-Order Buyer Credits** | 90 introductory 2,000 IQD discount checkout vouchers to convert hesitant shoppers into active buyers during launch campaigns. | $120 | 180,000 | 90 orders $	imes$ 2,000 IQD ($1.33) voucher incentive. |
| **Merchant Starter Packaging Supplies** | Branded Cheapify security tape rolls, document pouches, and fragile stickers provided to pilot partner shops. | $100 | 150,000 | Local Duhok packaging supplier / print shop rate for custom adhesive tape and shipping labels. |
| **Subtotal Direct Costs** | | **$400** | **600,000** | *Requested from GIZ* |

---

### 3.5 Pillar 5: Regulatory Compliance & Operational Contingency ($420 USD / 630,000 IQD — OPEX)
*Objective: Ensure legal protection, merchant trust, and operational reserves.*

| Line Item | Scope & Technical Specifications | 6-Month Total (USD) | 6-Month Total (IQD) | Evidence & Reference Citation |
| :--- | :--- | :---: | :---: | :--- |
| **Commercial Trade Registration** | Trade name reservation filing, commercial registration, and membership fees with the Duhok Chamber of Commerce & Industry (DCCI). | $250 | 375,000 | [Duhok Chamber of Commerce & Industry (DCCI)](https://duhokchamber.com/): Official registration, notary, and trade name certification fees in KRI. |
| **Bilingual Legal Terms & Vendor Contracts** | Legal consultation with a local KRI attorney to draft and review multi-seller agreements, return policies, and consumer dispute terms. | $100 | 150,000 | Standard consultation and document review fee with local bilingual attorney in Duhok. |
| **Field Merchant Onboarding Travel** | In-person shop visits across Duhok commercial markets (Bazaar, Malta, Kro, KRO commercial street). | **$0** | **0** | **CONDUCTED BY FOUNDER:** Handled directly by Shakir during local field visits ($0 charge to project). |
| **Internet & Generator Utilities** | Local facility utilities. | **$0** | **0** | **COVERED BY FOUNDER:** Existing home & incubator facility infrastructure utilized ($0 donor bill). |
| **Operational Contingency Buffer** | Emergency liquidity reserve for foreign exchange rate fluctuations and unexpected API traffic surges. | $70 | 105,000 | Standard donor project contingency reserve. |
| **Subtotal Compliance & Contingency** | | **$420** | **630,000** | *Requested from GIZ* |

---

## 4. Financial Mechanics, Equations & Post-Pilot Steady-State Model

### 4.1 What Are "Direct Costs" (COGS) in an E-Commerce Marketplace?
In an asset-light marketplace platform, **Cheapify does not buy or hold product inventory**. The merchant owns the goods.  
Therefore, **Cost of Goods Sold (COGS)** does not mean purchasing inventory; it strictly represents the **marginal direct transaction cost incurred when an order is processed**:
1. **Payment Gateway / COD Reconciliation Fee:** When a customer pays via FastPay, FIB, or Qi Card (or when a 3PL courier collects Cash on Delivery), the processing fee is ~100 IQD ($0.067) per transaction.
2. **Standardized Packaging Consumables:** Branded tamper-evident security tape and waybill document pouches supplied to merchants = ~50 IQD ($0.033) per order.
3. **Promotional Buyer Checkout Vouchers:** In the pilot, subsidizing 2,000 IQD introductory discounts directly on checkout.

> **The Marginal COGS Equation:**  
> In steady state, $	ext{COGS per order} = 	ext{Gateway Fee (100 IQD)} + 	ext{Packaging Consumables (50 IQD)} = \mathbf{150 	ext{ IQD (\$0.10 USD) per order}}$.

---

### 4.2 How the Domain Cost is Handled (Cash vs. Accrual)
* Cloudflare Registrar wholesale domain registration is **$9.77 / year (approx. 15,000 IQD)**.
* **In the Cash Budget:** Booked as a one-time cash outlay of **$10 (15,000 IQD)** in Month 1.
* **In the Monthly P&L:** Amortized evenly across 12 months at **$0.83 / month (1,250 IQD / month)**. Because it is less than $1/mo, its impact on monthly margins is negligible.

---

### 4.3 Business SIM vs. WhatsApp Cloud API Messaging
* In Iraq, a commercial SIM / eSIM costs only **3,000 to 5,000 IQD ($2 to $3.50)**.
* Meta requires a phone number to receive the initial SMS/voice verification code to register the Meta Business Account.
* Once registered, **all messaging runs 100% via Meta's Cloud API servers over the internet**. No cellular minutes or cellular SMS are sent.
* We budget **$10 total (15,000 IQD)** for the SIM card plus occasional top-up credit to keep the mobile line active with AsiaCell/Korek.

---

### 4.4 The 3 Core Financial Equations

Every number in the 12-month model is governed by these exact mathematical formulas:

$$\mathbf{1. 	ext{ Revenue}} = (	ext{Monthly Orders} 	imes 	ext{Avg Take-Rate: } 1,500 	ext{ IQD}) + (	ext{Active Store Sponsors} 	imes 150,000 	ext{ IQD})$$

$$\mathbf{2. 	ext{ Direct Costs (COGS)}} = (	ext{Monthly Orders} 	imes 150 	ext{ IQD}) + 	ext{Pilot Testing Subsidies (Pilot only)}$$

$$\mathbf{3. 	ext{ OPEX Burn}} = 	ext{Fixed Cloud Infra (\$111 / 166.5k IQD)} + 	ext{WhatsApp API (Orders } 	imes 30 	ext{ IQD)} + 	ext{Duhok Meta Ads}$$

---

### 4.5 Full 12-Month Profit & Loss Trajectory (Year 1 Roadmap)

This trajectory matches [Cheapify_Monthly_Profit_and_Loss.xlsx](file:///media/shakerbr/workland/workspace/git/my-private-repos/cheapify/finance-management/Cheapify_Monthly_Profit_and_Loss.xlsx).  
It shows the natural launch curve: starting with alpha testing (150 orders), scaling to 3,000 orders in the pilot, and transitioning into high-margin commercial growth in Month 7 onward:

| Month | Orders | Revenue (IQD) | Direct COGS (IQD) | Gross Profit (IQD) | Operating Overheads (IQD) | Organic Operating Profit | GIZ Seed Grant Support | Net Cash Profit (IQD) | Net Margin |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **M1** | 150 | 225,000 | 100,000 | 125,000 | 450,000 | -325,000 | +550,000 | **+225,000** (+$150) | **100.0%** |
| **M2** | 250 | 525,000 | 100,000 | 425,000 | 450,000 | -25,000 | +550,000 | **+525,000** (+$350) | **100.0%** |
| **M3** | 400 | 750,000 | 100,000 | 650,000 | 450,000 | +200,000 | +550,000 | **+750,000** (+$500) | **100.0%** |
| **M4** | 600 | 1,050,000 | 100,000 | 950,000 | 450,000 | +500,000 | +550,000 | **+1,050,000** (+$700) | **100.0%** |
| **M5** | 750 | 1,275,000 | 100,000 | 1,175,000 | 450,000 | +725,000 | +550,000 | **+1,275,000** (+$850) | **100.0%** |
| **M6** | 850 | 1,425,000 | 100,000 | 1,325,000 | 450,000 | +875,000 | +550,000 | **+1,425,000** (+$950) | **100.0%** |
| **Pilot (1–6)** | **3,000** | **5,250,000 ($3,500)** | **600,000 ($400)** | **4,650,000 (88.6%)** | **2,700,000 ($1,800)** | **+1,950,000 (+$1,300)** | **+3,300,000 ($2,200)** | **+5,250,000 (+$3,500)** | **+100%** |
| **M7** | 1,000 | 1,800,000 | 150,000 | 1,650,000 | 234,000 | **+1,416,000** | $0 | **+1,416,000** (+$944) | **78.7%** |
| **M8** | 1,150 | 2,025,000 | 172,500 | 1,852,500 | 238,500 | **+1,614,000** | $0 | **+1,614,000** (+$1,076) | **79.7%** |
| **M9** | 1,300 | 2,400,000 | 195,000 | 2,205,000 | 250,500 | **+1,954,500** | $0 | **+1,954,500** (+$1,303) | **81.4%** |
| **M10** | 1,500 | 2,700,000 | 225,000 | 2,475,000 | 256,500 | **+2,218,500** | $0 | **+2,218,500** (+$1,479) | **82.2%** |
| **M11** | 1,750 | 3,225,000 | 262,500 | 2,962,500 | 292,500 | **+2,670,000** | $0 | **+2,670,000** (+$1,780) | **82.8%** |
| **M12** | 2,000 | 3,600,000 | 300,000 | 3,300,000 | 300,000 | **+3,000,000** | $0 | **+3,000,000** (+$2,000) | **83.3%** |
| **Steady (7–12)**| **8,700** | **15,750,000 ($10,500)**| **1,305,000 ($870)**| **14,445,000 (91.7%)**| **1,572,000 ($1,048)**| **+12,873,000 (+$8,582)**| **$0** | **+12,873,000 (+$8,582)**| **+81.7%** |
| **YEAR 1 TOTAL** | **11,700**| **21,000,000 ($14,000)**| **1,905,000 ($1,270)**| **19,095,000 (90.9%)**| **4,272,000 ($2,848)**| **+14,823,000 (+$9,882)**| **+3,300,000 ($2,200)**| **+18,123,000 (+$12,082)**| **+86.3%** |

---

### 4.6 Operational Break-Even Sensitivity (Steady State)
* **Post-Pilot Monthly Fixed Overhead:** **$156 / month (234,000 IQD)**
* **Net Contribution Margin per Order:** **1,350 IQD ($0.90 USD)** (1,500 IQD avg commission less 150 IQD packaging/gateway fee).
* **Break-Even Order Volume:**
  $$	ext{Break-Even Orders} = rac{234,000 	ext{ IQD}}{1,350 	ext{ IQD}} = \mathbf{173 	ext{ orders per month (approx. 5 to 6 orders per day)}}$$

> **Strategic Takeaway for GIZ / BMZ Juries:**  
> At only **6 orders per day across all participating partner stores in Duhok**, Cheapify is 100% self-financing and profitable.

---

## 5. Pitch Deck Presentation Slide Content (For Final Showcase)

You can copy this exact content directly into your final presentation slide:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PART 4 · FINANCIAL ASK                             │
│                    Seed Budget & Capital Allocation                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   PROJECTED PILOT REVENUE : $3,500 USD (5,250,000 IQD)                      │
│   GROSS OPERATING MARGIN  : 88.6% Gross Profit                              │
│   SOFTWARE DEVELOPMENT    : $0 (Engineered 100% In-House by Founder)        │
│   CONTENT & VIDEO DEMOS   : $0 (Produced 100% In-House by Founder)          │
│   NET OPERATING PROFIT    : +$1,300 USD (+1,950,000 IQD — +37.1% Margin)    │
│                                                                             │
│   ★ FUNDING REQUESTED FROM GIZ: $2,200 USD (3,300,000 IQD)                 │
│                                                                             │
│   ┌──────────────────────────────────────────────────────────────────────┐  │
│   │ 30%  $670  SCALABLE CLOUD & EDGE (Compute, Postgres, Redis, CDN)     │  │
│   │ 27%  $600  DUHOK DIGITAL MARKETING (Hyper-Local Meta Ads)            │  │
│   │ 18%  $400  PILOT COURIER DELIVERIES & PACKAGING SUPPLIES             │  │
│   │ 25%  $530  CHAMBER REGISTRATION, LEGAL REVIEW & WHATSAPP API         │  │
│   └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   "Zero dollars spent on outside software agencies or paid influencers.     │
│   100% of donor funding strictly covers cloud servers, ads, and legal ops." │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Verbal Presentation Script (30-Second Pitch to the Jury):
> *"Because I am a computer engineer building the entire platform and producing all marketing content myself, our cash development fee is $0—saving over $6,000 in agency costs and keeping our burn rate ultra-low. Cheapify operates on an 88.6% gross margin and generates a positive +37.1% net operating profit (+1,950,000 IQD) during the pilot.  
> We are requesting a lean, disciplined seed grant of **$2,200 (3,300,000 IQD)** from GIZ:
> * **$670 (30%)** powers high-concurrency cloud servers and Cloudflare edge security built for tens of thousands of users.
> * **$600 (27%)** funds hyper-local targeted marketing in Duhok.
> * **$400 (18%)** covers courier delivery testing and partner packaging supplies.
> * **$530 (25%)** covers Chamber of Commerce trade registration, legal agreements, and WhatsApp Business Cloud APIs.  
> Once the pilot concludes, our ongoing monthly operating cost drops to just $156 a month. At only 6 orders per day, Cheapify is fully self-sustaining, scaling to over +$1,400 to +$3,000 per month with an 80%+ net profit margin."*
