import React from 'react';
import { Layers, ArrowLeftRight, Sparkles, LayoutDashboard, Tag, ShieldCheck } from 'lucide-react';

export const FeatureBento: React.FC = () => {
  return (
    <section className="sec alt" id="features">
      <div className="container">
        <div className="sec-head">
          <div className="sec-tag">
            <span className="badge b-blue-soft">Built for Smart Shoppers</span>
          </div>
          <h2 className="sec-title">Built for clarity, speed, and confidence.</h2>
          <p className="sec-desc">
            Cheapify redefines shopping and selling by bringing transparency, intelligent comparison, and modern tools to local retail.
          </p>
        </div>

        <div className="feature-grid">
          <div className="feature-card">
            <div className="icon-tile">
              <Layers className="lucide" />
            </div>
            <h3>One Page per Product</h3>
            <p>
              Every product has a single, definitive page with verified technical specifications and clear photos. No duplicate listings, no confusion.
            </p>
            <span className="chip">Single Catalog Standard</span>
          </div>

          <div className="feature-card">
            <div className="icon-tile g">
              <ArrowLeftRight className="lucide" />
            </div>
            <h3>Side-by-Side Store Comparison</h3>
            <p>
              Compare verified sellers carrying the exact same item in real time. See retail prices, delivery speed, and customer ratings at a glance.
            </p>
            <span className="chip">Complete Transparency</span>
          </div>

          <div className="feature-card">
            <div className="icon-tile">
              <Sparkles className="lucide" />
            </div>
            <h3>Best Value Selection</h3>
            <p>
              Our intelligent algorithm highlights the best overall deal based on lowest total doorstep price and fastest delivery. Ranking cannot be bought.
            </p>
            <span className="chip">Fair & Deterministic</span>
          </div>

          <div className="feature-card">
            <div className="icon-tile g">
              <LayoutDashboard className="lucide" />
            </div>
            <h3>Merchant Dashboard</h3>
            <p>
              A turnkey operating system for merchants to manage their product catalog, track orders in real time, and schedule courier pickups effortlessly.
            </p>
            <span className="chip">Store Management</span>
          </div>

          <div className="feature-card">
            <div className="icon-tile">
              <Tag className="lucide" />
            </div>
            <h3>Upfront Doorstep Pricing</h3>
            <p>
              Clear, transparent pricing before you order. You always see the item price plus standard delivery fee upfront with zero hidden fees.
            </p>
            <span className="chip">Item + Delivery = Total</span>
          </div>

          <div className="feature-card">
            <div className="icon-tile g">
              <ShieldCheck className="lucide" />
            </div>
            <h3>48-Hour Buyer Protection</h3>
            <p>
              Inspect your package at your doorstep with Cash on Delivery or Card, backed by our 48-hour return window for wrong or damaged items.
            </p>
            <span className="chip">Zero Upfront Risk</span>
          </div>
        </div>
      </div>
    </section>
  );
};
