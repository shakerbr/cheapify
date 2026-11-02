import React from 'react';
import { Link } from 'react-router-dom';
import { RotateCcw, Truck, Banknote, Store, LayoutDashboard, CheckCircle2 } from 'lucide-react';

export const HowItWorksPage: React.FC = () => {
  return (
    <>
      {/* Hero Header */}
      <section className="sec" style={{ padding: '16px 0 48px' }}>
        <div className="container">
          <div className="sec-head" style={{ marginBottom: '40px' }}>
            <div className="sec-tag">
              <span className="badge b-blue-soft">Transparent Commerce</span>
            </div>
            <h1 className="sec-title">How Cheapify Works</h1>
            <p className="sec-desc">
              We eliminated the biggest frustrations of online retail: hidden prices, duplicate listings, communication delays, and unpredictable delivery.
            </p>
          </div>

          {/* 3-Step Walkthrough */}
          <div style={{ maxWidth: '860px', margin: '0 auto' }}>
            {/* Step 1 */}
            <div className="step-card">
              <div className="step-num">01</div>
              <div className="step-body">
                <h3>One master page per product.</h3>
                <p>
                  On traditional platforms, searching for an item shows dozens of duplicate listings with conflicting titles and messy photos. On Cheapify, every identical product is organized under <strong>one single master page</strong> with verified technical specifications and clear imagery.
                </p>
                <div style={{ display: 'flex', gap: '8px', marginTop: '14px', flexWrap: 'wrap' }}>
                  <span className="chip">Single Catalog Standard</span>
                  <span className="chip">Zero Duplicates</span>
                  <span className="chip">Verified Specifications</span>
                </div>
              </div>
            </div>

            {/* Step 2 */}
            <div className="step-card">
              <div className="step-num">02</div>
              <div className="step-body">
                <h3>Side-by-side store comparison.</h3>
                <p>
                  Inside the product page, every verified merchant carrying that item is displayed side-by-side. Our <strong>Best Value</strong> selection highlights the top overall deal based on lowest total doorstep cost and delivery speed. No hidden fees, no sponsored bias.
                </p>
                <div style={{ display: 'flex', gap: '8px', marginTop: '14px', flexWrap: 'wrap' }}>
                  <span className="badge b-best-soft">Best Value Tag</span>
                  <span className="chip">Item + Delivery = Doorstep Price</span>
                  <span className="chip">Real-Time Stock</span>
                </div>
              </div>
            </div>

            {/* Step 3 */}
            <div className="step-card">
              <div className="step-num">03</div>
              <div className="step-body">
                <h3>Seamless ordering & reliable delivery.</h3>
                <p>
                  Select your preferred store, confirm your delivery address, and place your order in seconds. Our integrated courier partner collects the sealed package directly from the store and delivers it to your door. You inspect the item before paying.
                </p>
                <div style={{ display: 'flex', gap: '8px', marginTop: '14px', flexWrap: 'wrap' }}>
                  <span className="chip">Doorstep COD & Card</span>
                  <span className="chip">48-Hour Return Window</span>
                  <span className="chip">Tamper-Evident Seal</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* For Merchants: How Selling Works */}
      <section className="sec" style={{ padding: '24px 0 56px' }}>
        <div className="container">
          <div className="sec-head">
            <div className="sec-tag">
              <span className="badge b-blue-soft">
                <Store className="lucide" />
                <span>For Store Owners</span>
              </span>
            </div>
            <h2 className="sec-title">How Selling Works for Merchants</h2>
            <p className="sec-desc">
              Manage your business effortlessly with a turnkey platform built to empower retail.
            </p>
          </div>

          <div className="flow-grid">
            <div className="flow-box">
              <div className="icon-tile g">
                <LayoutDashboard className="lucide" />
              </div>
              <h4>Turnkey Merchant Dashboard</h4>
              <p>
                Manage your product catalog, toggle available colors and sizes, and track stock in real time without technical complexity.
              </p>
            </div>

            <div className="flow-box">
              <div className="icon-tile">
                <Truck className="lucide" />
              </div>
              <h4>Automated Courier Dispatch</h4>
              <p>
                When an order arrives, simply package it with our tamper-evident seal. Our couriers pick it up straight from your counter.
              </p>
            </div>

            <div className="flow-box">
              <div className="icon-tile k">
                <CheckCircle2 className="lucide" />
              </div>
              <h4>Keep 96% with Fast Payouts</h4>
              <p>
                Benefit from a transparent, low platform fee structure. Earn more per sale and receive fast, automated payouts directly to your account.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Trust & Policy Details */}
      <section className="sec alt" id="returns">
        <div className="container">
          <div className="sec-head">
            <div className="sec-tag">
              <span className="badge b-best-soft">Buyer Guarantees</span>
            </div>
            <h2 className="sec-title">Built on total buyer protection.</h2>
            <p className="sec-desc">
              Cheapify is engineered to make online shopping as safe, clear, and reliable as walking into your favorite local store.
            </p>
          </div>

          <div className="flow-grid">
            <div className="flow-box">
              <div className="icon-tile">
                <RotateCcw className="lucide" />
              </div>
              <h4>48-Hour Return Window</h4>
              <p>
                If an item arrives faulty, damaged, or wrong, you have a full 48 hours to request a return. The merchant covers return delivery.
              </p>
            </div>

            <div className="flow-box" id="delivery">
              <div className="icon-tile">
                <Truck className="lucide" />
              </div>
              <h4>Tamper-Evident Delivery</h4>
              <p>
                Every order is dispatched in an opaque, security-taped mailer with a unique waybill number. Couriers do not open packages.
              </p>
            </div>

            <div className="flow-box" id="payment">
              <div className="icon-tile k">
                <Banknote className="lucide" />
              </div>
              <h4>Zero Upfront Risk</h4>
              <p>
                You never pay before holding the item. Cash on Delivery is available on all orders, with electronic payment (FIB, Qi, FastPay) fully integrated.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Centered CTA Box */}
      <section className="sec" style={{ padding: '48px 0 64px' }}>
        <div className="container">
          <div
            style={{
              background: 'var(--white)',
              border: '1px solid var(--line)',
              borderRadius: '26px',
              padding: '52px 36px',
              textAlign: 'center',
              boxShadow: 'var(--elev-1)',
              maxWidth: '860px',
              margin: '0 auto',
            }}
          >
            <h2 style={{ fontFamily: 'var(--f-display)', fontSize: '32px', color: 'var(--ink)', marginBottom: '12px' }}>
              Ready to shop smarter?
            </h2>
            <p style={{ fontSize: '16px', color: 'var(--muted)', maxWidth: '520px', margin: '0 auto 28px' }}>
              Join early shoppers waiting for our launch and get a 5,000 IQD voucher on your first order.
            </p>
            <Link to="/#waitlist" className="btn btn-primary btn-pill btn-lg">
              Join the Early Access Waitlist
            </Link>
          </div>
        </div>
      </section>
    </>
  );
};
