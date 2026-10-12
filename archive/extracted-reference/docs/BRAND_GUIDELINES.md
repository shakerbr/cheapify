# Cheapify — Brand Identity & Design System Guidelines

**Version:** 3.0 (Master Brand Architecture - Archived Reference)  
**Standard:** Enterprise Digital & Interface Implementation  
**Brand Slogan:** *The bright side of choosing.*  
**Brand Promise:** *Smart Deals. Verified Sellers. One App.*  

---

## 1. Brand Strategic Essence

Cheapify is engineered to bring absolute clarity, intelligence, and transparency to Iraqi digital commerce. The brand name does not imply cheap, disposable, or counterfeit merchandise; it represents the **active verb of outsmarting arbitrary markups** to surface legitimate fair-market value.

### The Brand Triad
* **Transparent:** Clear, upfront pricing across competing stores. No unlisted prices, hidden delivery surcharges, or private DM negotiations.
* **Smart:** Algorithmic product grouping, automatic best-price prioritization, and merchant price alerts.
* **Reliable:** Authenticated merchant verification, structured order fulfillment, and dependable local logistics.

---

## 2. Master Color Architecture

The Cheapify color palette balances technological precision with commercial confidence and trust. All color pairings comply with **WCAG AAA** contrast standards.

### 2.1 Core Palette

| Role | Color Name | HEX | RGB | CMYK | Usage & UI Application |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Brand** | **Boston Blue** | `#0E82C4` | `14, 130, 196` | `82, 40, 0, 0` | Shopping bag vector, primary CTA buttons, active navigation, search triggers. |
| **Accent / Trust** | **Jade Green** | `#148C53` | `20, 140, 83` | `85, 15, 85, 3` | Growth arrow, discovery magnifier, "Verified Partner" badges, "Best Value" tags. |
| **Neutral Dark** | **Slate Charcoal** | `#292F33` | `41, 47, 51` | `70, 60, 55, 60` | Wordmark, primary headings, body copy, card borders. |
| **Surface Dark** | **Jet Squircle** | `#1B1C1E` | `27, 28, 30` | `72, 65, 62, 75` | Mobile app icon background, dark mode surfaces, merchant analytics headers. |
| **Neutral Light** | **Cloud Gray** | `#F6F8FA` | `246, 248, 250` | `2, 1, 0, 0` | Master page background, secondary cards, pricing table alternating rows. |
| **Base Surface** | **Pure White** | `#FFFFFF` | `255, 255, 255` | `0, 0, 0, 0` | Product card surfaces, modal viewports, input backgrounds. |

### 2.2 Secondary Functional Palette (UI States)

| Role | Color Name | HEX | Purpose |
| :--- | :--- | :--- | :--- |
| **Warning / Rating** | **Sunset Amber** | `#F5A623` | Merchant rating stars, low stock warnings ("Only 2 left"), countdown timers. |
| **Error / Alert** | **Crimson Alert** | `#D0021B` | Out of stock alerts, destructive actions, checkout validation errors. |
| **Muted Metadata** | **Slate Mid-Gray**| `#8795A1` | Inactive icons, placeholder inputs, timestamps, SKU metadata. |

### 2.3 Proportional Balance (60-30-10 Rule)
* **60% Base Canvas:** Clean White (`#FFFFFF`) and Cloud Gray (`#F6F8FA`) maintain breathable negative space for complex product comparisons.
* **30% Structure & Copy:** Slate Charcoal (`#292F33`) for high-contrast typography, dividers, and table grids.
* **10% Brand Accents:** Boston Blue (`#0E82C4`) strictly for interactive triggers; Jade Green (`#148C53`) strictly for trust signals and winning price badges.

---

## 3. Logo Anatomy & Visual Rules

The Cheapify mark synthesizes three core retail symbols:
1. **The Commerce Hub (Shopping Bag in Boston Blue):** Represents the centralized digital marketplace sheltering verified local shops.
2. **The Growth Vector (Upward Arrow in Jade Green):** Represents merchant economic growth and consumer financial savings.
3. **The Discovery Engine (Magnifier in Jade Green):** Communicates smart search, barcode matching, and transparent price comparison.
4. **The Wordmark:** Set in geometric sans-serif (Slate Charcoal) with a signature **Boston Blue dot (tittle) over the "i"**.

```
Master SVG Location: assets/cheapify-logo.svg
```

### 3.1 Clear Space & Sizing Limits
* **Clear Space Rule:** Keep a boundary equal to the height of the letter **"C"** in the Cheapify wordmark completely clear of text, borders, or clutter.
* **Minimum Digital Dimensions:**
  - Full Primary Stack Lockup: **120 px width**
  - Standalone App Icon: **32 × 32 px**
* **Minimum Print Dimensions:**
  - Full Stack Lockup: **28 mm width**
  - Icon Only: **10 mm width**

### 3.2 Visual Violations
* **DO NOT** rotate or decouple the magnifying glass or arrow from the shopping bag.
* **DO NOT** alter the color assignment (the bag must never be green, and the arrow must never be blue).
* **DO NOT** use heavy gradients, drop shadows, or 3D bevels on flat branding surfaces.
* **DO NOT** distort, stretch, or skew the logo vector aspect ratio.

---

## 4. Typography Hierarchy

### 4.1 Typeface Families
* **English / Latin Primary:**
  - **Brand & Display Headlines:** **Comfortaa** (Rounded, modern, friendly) or **Outfit / Plus Jakarta Sans**.
  - **High-Density UI & Pricing Tables:** **Inter** (Clean grotesque for maximum readability in tables).
* **Kurdish (Badini / Sorani) & Arabic Primary:**
  - **IBM Plex Sans Arabic** (Superior structural weight balance with Latin fonts).
  - Alternative: **Noto Sans Arabic**.

### 4.2 Type Scale

| Level | Size (Desktop / Web) | Size (Mobile) | Weight | Application |
| :--- | :--- | :--- | :--- | :--- |
| **Display (H1)** | 36–40 px | 28–32 px | Bold (700) | Landing page hero, major billboard headers |
| **Section (H2)** | 24–28 px | 20–24 px | SemiBold (600) | Category headers, merchant storefront names |
| **Card Head (H3)**| 18–20 px | 16–18 px | Medium (500) | Product SKU names, modal titles |
| **Body Text** | 14–16 px | 14 px | Regular (400) | Descriptions, specs, policy copy |
| **Pricing / Data**| 20–24 px | 18–20 px | Bold (700) | IQD price tags, side-by-side comparison figures |
| **Badges / Micro**| 11–12 px | 10–11 px | SemiBold (600) | "Verified Partner", "Best Value", delivery ETAs |

---

## 5. UI Component & Interaction Standards

### 5.1 The Single-SKU Comparison Table
Every unique product has one master card. All competing verified sellers are listed in a structured sub-table:
```
┌────────────────────────────────────────────────────────────────────────┐
│ [Product Photo]   ASUS VA24EHF 24" 100Hz Gaming Monitor                │
│                   SKU: ASUS-VA24EHF-24                                 │
│                   Lowest Market Price: 116,721 IQD                     │
├────────────────────────────────────────────────────────────────────────┤
│ COMPARE VERIFIED MERCHANTS (3 Offers)                                  │
├─────────────────┬───────────┬──────────────┬──────────────┬────────────┤
│ MERCHANT        │ TRUST     │ PRICE (IQD)  │ DELIVERY     │ ACTION     │
├─────────────────┼───────────┼──────────────┼──────────────┼────────────┤
│ TechZone Duhok  │ Verified✓ │ 116,721 [BEST]│ Today        │ [Select]   │
│ FastRetail KRI  │ Verified✓ │ 135,000      │ Tomorrow     │ [Select]   │
│ Prime Store     │ Verified✓ │ 163,350      │ 2 Days       │ [Select]   │
└─────────────────┴───────────┴──────────────┴──────────────┴────────────┘
```

* **The "Best Value" Badge:** The lowest verified price must display a solid Jade Green chip (`#148C53`) with white text reading **"Best Value"**.
* **The "Verified Seller" Checkmark:** A green verified checkmark badge (`#148C53`) placed adjacent to every vetted merchant name.
* **Component Styling:**
  - Border radius: **12 px** for product cards, containers, and modals.
  - Border: **1 px solid `#E2E8F0`**.
  - Elevation: Soft shadow `0 4px 15px rgba(0, 0, 0, 0.05)`.

---

## 6. Voice, Tone & Editorial Matrix

Cheapify speaks like a sharp, trusted consumer advisor. We replace emotional marketing hype with objective numerical proof.

| Communication Point | What Cheapify Says (On-Brand) | What Cheapify Never Says (Off-Brand) |
| :--- | :--- | :--- |
| **Value Proposition** | "Save 25,000 IQD instantly on the identical SKU from verified local stores." | "Crazy cheap prices! Lowest prices in the universe!" (Sounds fake/counterfeit) |
| **Product Discovery** | "Stop asking for prices in the DMs. Live, transparent prices listed upfront." | "DM us for a secret discount price, dear." (Validates broken habits) |
| **Merchant Outreach** | "Expand your Duhok storefront digitally with predictable orders and flat fees." | "Dump your extra stock online fast!" (Disrespects partner retailers) |
| **Order Confirmation**| "Order #1042 confirmed. Dispatched to [Store] with local courier tracking." | "Order received! We'll check with the shop if they have it." |
