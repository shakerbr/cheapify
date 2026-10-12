# Cheapify — Technical Architecture & Implementation Blueprint

**Version:** 1.0 (Engineering Architecture - Archived Reference)  
**Target Platform:** Web Catalog MVP -> PWA -> Hybrid Native Applications  
**Primary Locale:** Iraq / Kurdistan Region (KRI)  

---

## 1. Architectural Overview

Cheapify is designed as a **lean, high-throughput, event-driven multi-seller marketplace**. Because the platform prioritizes real-time price comparison and automated alerts, the architecture separates the master product catalog from individual merchant inventory listings.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             CLIENT LAYER (Web / PWA)                        │
│  - Single-SKU Catalog & Comparison Engine                                   │
│  - Frictionless Checkout (COD / FastPay / FIB / Qi Card)                    │
│  - Merchant Dashboard (Real-time price editor & order manager)               │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │ REST / WebSocket / Webhooks
┌─────────────────────────────────────▼───────────────────────────────────────┐
│                             API & SERVICE LAYER                             │
│  ┌──────────────────────┐ ┌─────────────────────┐ ┌──────────────────────┐  │
│  │ Catalog Service      │ │ Ranking & Pricing   │ │ Order & Fulfillment  │  │
│  │ - SKU & Barcodes     │ │ - Best-Value Ranker │ │ - Checkout Engine    │  │
│  │ - Single-SKU Resolver│ │ - Price Drop Alerts │ │ - Courier 3PL Dispatch│ │
│  └──────────────────────┘ └─────────────────────┘ └──────────────────────┘  │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
┌─────────────────────────────────────▼───────────────────────────────────────┐
│                      BACKGROUND JOBS & EVENT BROKER (Redis)                  │
│  - WhatsApp Business Cloud API Dispatch (Meta Webhooks)                     │
│  - Merchant Competitor Price Alert Workers                                   │
│  - Courier Tracking Status Webhook Consumers                                │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
┌─────────────────────────────────────▼───────────────────────────────────────┐
│                           DATABASE LAYER (PostgreSQL)                       │
│  - Master Products & SKUs    - Verified Merchants   - Inventory & Listings  │
│  - Customer Orders & Items   - Payout Settlements   - Price History Logs    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Relational Data Models (PostgreSQL Schema)

### 2.1 Master Catalog (`products`)
Enforces the **Single-SKU rule**. Products are defined once and referenced by all merchants.
```sql
CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sku VARCHAR(64) UNIQUE NOT NULL,
    barcode VARCHAR(64) UNIQUE,
    title VARCHAR(255) NOT NULL,
    brand VARCHAR(128) NOT NULL,
    category VARCHAR(64) NOT NULL,
    description TEXT,
    specs JSONB DEFAULT '{}',
    hero_image_url TEXT NOT NULL,
    additional_images TEXT[] DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_products_barcode ON products(barcode);
CREATE INDEX idx_products_category ON products(category);
```

### 2.2 Verified Merchants (`merchants`)
Stores verified physical stores and social media retailers.
```sql
CREATE TABLE merchants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(32) NOT NULL,
    whatsapp_number VARCHAR(32) NOT NULL,
    city VARCHAR(64) NOT NULL,            -- e.g., 'Duhok', 'Erbil', 'Sulaymaniyah'
    address TEXT NOT NULL,
    rating NUMERIC(3, 2) DEFAULT 5.00,
    is_verified BOOLEAN DEFAULT FALSE,
    status VARCHAR(32) DEFAULT 'active',   -- 'active', 'paused', 'suspended'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_merchants_city ON merchants(city);
```

### 2.3 Merchant Inventory & Pricing (`merchant_listings`)
Houses the competing prices and live stock for each product.
```sql
CREATE TABLE merchant_listings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    merchant_id UUID NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,
    price_iqd INTEGER NOT NULL CHECK (price_iqd > 0),
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    delivery_hours INTEGER DEFAULT 24,
    is_active BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    CONSTRAINT uq_product_merchant UNIQUE (product_id, merchant_id)
);

CREATE INDEX idx_listings_product ON merchant_listings(product_id, is_active, price_iqd);
```

### 2.4 Orders & Fulfillment (`orders` & `order_items`)
Handles structured order flow and fee calculations.
```sql
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_code VARCHAR(16) UNIQUE NOT NULL, -- e.g., 'CP-1042'
    customer_name VARCHAR(128) NOT NULL,
    customer_phone VARCHAR(32) NOT NULL,
    city VARCHAR(64) NOT NULL,
    delivery_address TEXT NOT NULL,
    payment_method VARCHAR(32) NOT NULL,     -- 'COD', 'FASTPAY', 'FIB', 'QI_CARD'
    status VARCHAR(32) DEFAULT 'pending',   -- 'pending', 'confirmed', 'dispatched', 'delivered', 'cancelled'
    total_goods_iqd INTEGER NOT NULL,
    delivery_fee_iqd INTEGER NOT NULL,
    platform_fee_iqd INTEGER NOT NULL,
    courier_tracking_code VARCHAR(64),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE order_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    listing_id UUID NOT NULL REFERENCES merchant_listings(id),
    product_id UUID NOT NULL REFERENCES products(id),
    merchant_id UUID NOT NULL REFERENCES merchants(id),
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price_iqd INTEGER NOT NULL
);
```

### 2.5 Price Alerts (`price_alerts`)
Logs competitive price triggers for merchant notification.
```sql
CREATE TABLE price_alerts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID NOT NULL REFERENCES products(id),
    outpriced_merchant_id UUID NOT NULL REFERENCES merchants(id),
    winning_merchant_id UUID NOT NULL REFERENCES merchants(id),
    winning_price_iqd INTEGER NOT NULL,
    outpriced_price_iqd INTEGER NOT NULL,
    notification_sent BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

## 3. Core Algorithms & Business Logic

### 3.1 Best-Value Ranking Algorithm
When a buyer views a product, all active listings are ranked dynamically:
```typescript
interface RankedListing {
  listingId: string;
  merchantId: string;
  merchantName: string;
  priceIqd: number;
  rating: number;
  deliveryHours: number;
  isBestValue: boolean;
}

export function rankListings(listings: Listing[], customerCity: string): RankedListing[] {
  // Sort primarily by lowest price, then by merchant rating, then delivery speed
  const sorted = [...listings]
    .filter(l => l.isActive && l.stockQuantity > 0)
    .sort((a, b) => {
      if (a.priceIqd !== b.priceIqd) return a.priceIqd - b.priceIqd;
      if (b.merchantRating !== a.merchantRating) return b.merchantRating - a.merchantRating;
      return a.deliveryHours - b.deliveryHours;
    });

  return sorted.map((listing, index) => ({
    ...listing,
    isBestValue: index === 0 // #1 ranked offer gets the Jade Green 'Best Value' chip
  }));
}
```

### 3.2 Tiered Platform Fee Calculator
Implements the exact fee matrix defined in the project business model:
```typescript
export function calculatePlatformFee(priceIqd: number): number {
  if (priceIqd < 9_000) {
    // 5% for items under 9,000 IQD
    return Math.round(priceIqd * 0.05);
  } else if (priceIqd <= 99_000) {
    // Flat 1,000 IQD for items between 10,000 and 99,000 IQD
    return 1_000;
  } else if (priceIqd <= 499_000) {
    // 2% for items between 100,000 and 499,000 IQD
    return Math.round(priceIqd * 0.02);
  } else {
    // 1.5% for high-ticket items (500,000+ IQD)
    return Math.round(priceIqd * 0.015);
  }
}
```

### 3.3 Live Competitive Price Alert Trigger
When a merchant modifies their price, the system executes an asynchronous worker:
```typescript
export async function onListingPriceUpdated(productId: string, updatedListing: Listing) {
  const allListings = await getActiveListingsForProduct(productId);
  const lowestPrice = Math.min(...allListings.map(l => l.priceIqd));

  if (updatedListing.priceIqd === lowestPrice) {
    // Identify merchants who were previously competitive but are now outpriced
    const outpricedMerchants = allListings.filter(
      l => l.merchantId !== updatedListing.merchantId && l.priceIqd > lowestPrice
    );

    for (const outpriced of outpricedMerchants) {
      await queuePriceAlertJob({
        productId,
        outpricedMerchantPhone: outpriced.whatsappNumber,
        productTitle: outpriced.productTitle,
        competitorPriceIqd: lowestPrice,
        currentMerchantPriceIqd: outpriced.priceIqd
      });
    }
  }
}
```

---

## 4. Integration Specifications

### 4.1 Meta WhatsApp Business Cloud API
* **Order Notification to Merchant:**
  ```text
  🛍️ New Cheapify Order: #CP-1042
  Product: ASUS VA24EHF 24" Gaming Monitor
  Price: 116,721 IQD
  Customer: Ahmad (Duhok - Sharya)
  Courier pickup scheduled: Today 3:00 PM.
  Reply 1 to confirm stock & ready for pickup.
  ```
* **Order Confirmation to Buyer:**
  ```text
  🎉 Order #CP-1042 Confirmed!
  Your order for [Product Name] has been received by TechZone Duhok.
  Total: 116,721 IQD + 3,000 IQD delivery (Cash on Delivery).
  Track your shipment here: cheapify.iq/track/CP-1042
  ```

### 4.2 Local Payment Gateways
1. **Cash on Delivery (COD):** Integrated with courier manifest; delivery agent collects cash and reconciles via 3PL settlement portal.
2. **FastPay API:** Server-to-server payment intent generation with mobile redirection and webhook callback on settlement.
3. **First Iraqi Bank (FIB):** Direct merchant payment QR generation and instant push-notification checkout.
4. **Qi Card:** Web gateway redirection for domestic debit transactions.

### 4.3 3PL Courier Logistics Partner API
* **Order Dispatch Payload:**
  ```json
  {
    "orderCode": "CP-1042",
    "pickup": {
      "merchantName": "TechZone Duhok",
      "phone": "+964750XXXXXXX",
      "address": "Bazaar St, Duhok"
    },
    "dropoff": {
      "customerName": "Ahmad",
      "phone": "+964750XXXXXXX",
      "address": "Sharya, Duhok"
    },
    "codAmountIqd": 119721
  }
  ```
* **Webhook Receiver:** Listens for `package_picked_up`, `in_transit`, `delivered`, and `failed_delivery`.

---

## 5. Technology Stack Recommendations

| Layer | Recommended Choice | Rationale |
| :--- | :--- | :--- |
| **Frontend** | **React / Vite or Next.js** | Fast static generation for catalog, lightweight client-side bundle, full RTL support. |
| **Styling** | **Vanilla CSS & Design Tokens** | Direct adherence to Brand Guidelines without heavy utility dependencies. |
| **Backend API** | **Node.js (TypeScript) / Express or Fastify** | High concurrency for I/O bound price checks, WebSockets, and webhook listeners. |
| **Database** | **PostgreSQL (Supabase / Managed VPS)** | Strict relational integrity for single-SKU architecture, JSONB for dynamic specs. |
| **Queue / Cache** | **Redis (Upstash / Local Redis)** | Real-time caching of "Best Value" listings and background WhatsApp workers. |
| **Hosting** | **Cloud VPS (Ubuntu / Docker) + Cloudflare** | Ultra-low monthly runway ($30–$50/mo), DDoS protection, and local caching. |
