import React from 'react';
import { Link } from 'react-router-dom';
import { Mail, Phone, ExternalLink } from 'lucide-react';

export const AboutPage: React.FC = () => {
  return (
    <>
      {/* Hero Header */}
      <section className="sec" style={{ padding: '16px 0 48px' }}>
        <div className="container">
          <div className="sec-head" style={{ marginBottom: '24px' }}>
            <div className="sec-tag">
              <span className="badge b-blue-soft">Our Story & Mission</span>
            </div>
            <h1 className="sec-title">
              Built to bring clarity to modern commerce.
            </h1>
            <p className="sec-desc">
              Cheapify unites shoppers and trusted stores on a single, transparent platform designed for speed, fairness, and confidence.
            </p>
          </div>

          {/* Stat Strip */}
          <div className="stat-strip">
            <div>
              <div className="stat-num tnum">1 Page</div>
              <div className="stat-label">
                per product with verified technical specifications and zero duplicate clutter
              </div>
            </div>
            <div>
              <div className="stat-num tnum">96%</div>
              <div className="stat-label">
                of sales kept by local merchants with transparent, low platform fees and direct payouts
              </div>
            </div>
            <div>
              <div className="stat-num tnum">48h</div>
              <div className="stat-label">
                buyer protection window on every delivered order with free return courier
              </div>
            </div>
          </div>

          {/* Story Narrative */}
          <div style={{ maxWidth: '800px', margin: '0 auto', fontSize: '16px', lineHeight: 1.75, color: 'var(--muted)' }}>
            <h2 style={{ fontFamily: 'var(--f-display)', fontSize: '24px', color: 'var(--ink)', margin: '40px 0 14px' }}>
              Why Cheapify was founded
            </h2>
            <p style={{ marginBottom: '20px' }}>
              Shopping online should be fast, transparent, and dependable. Yet across emerging markets, retail remains heavily fragmented across scattered social accounts and unorganized listings. The same product is often sold at conflicting prices, technical details are omitted, and buyers are forced to spend hours messaging stores simply to confirm prices and stock.
            </p>
            <p style={{ marginBottom: '20px' }}>
              Cheapify was built to modernize this experience from the ground up: creating a unified standard where products are cataloged once, verified merchants are compared side-by-side, and transactions are completed with total transparency.
            </p>

            <div className="quote-box">
              "Commerce shouldn't require sending twenty messages just to find out who has stock and what it costs. Cheapify brings transparent pricing and modern technology to local retail."
            </div>

            <h2 style={{ fontFamily: 'var(--f-display)', fontSize: '24px', color: 'var(--ink)', margin: '40px 0 14px' }}>
              One page per product & side-by-side comparison
            </h2>
            <p style={{ marginBottom: '20px' }}>
              Instead of endless duplicate cards for the same item, Cheapify organizes retail under a clean <strong>single-catalog standard</strong>. Every item has one master page with verified technical specifications, clear photography, and live variant selectors.
            </p>
            <p style={{ marginBottom: '20px' }}>
              Inside that page, all verified stores carrying the product are displayed side-by-side. Shoppers see live retail prices, standardized delivery times, and verified merchant ratings at a glance. Our intelligent <strong>Best Value</strong> selection highlights the top overall deal based on lowest total doorstep price and fastest delivery — ranking is completely merit-based and cannot be bought.
            </p>

            <h2 style={{ fontFamily: 'var(--f-display)', fontSize: '24px', color: 'var(--ink)', margin: '40px 0 14px' }}>
              The Merchant Dashboard: Empowering local retail
            </h2>
            <p style={{ marginBottom: '20px' }}>
              Cheapify is built to empower merchants, not displace them. Through our intuitive <strong>Merchant Dashboard</strong>, stores gain enterprise-grade tools with zero technical complexity: real-time stock management, live order tracking, and automated courier dispatch straight from their counter.
            </p>
            <p style={{ marginBottom: '20px' }}>
              Unlike traditional platforms that take aggressive commissions of 15% to 20%, Cheapify operates on a fair, progressive fee structure where merchants keep <strong>96% of their revenue</strong>, backed by fast, automated settlements.
            </p>

            <h2 style={{ fontFamily: 'var(--f-display)', fontSize: '24px', color: 'var(--ink)', margin: '40px 0 14px' }}>
              Our expansion vision
            </h2>
            <p style={{ marginBottom: '20px' }}>
              We are establishing a trusted network of verified merchants and standardizing fast doorstep delivery with Cash on Delivery and digital payments. From our initial launch hubs, Cheapify is engineered to expand across major metropolitan centers and define the future of retail across the region.
            </p>

            {/* Founder Card */}
            <div className="founder-card">
              <div className="founder-avatar">SB</div>
              <div>
                <div className="founder-name-row">
                  <h3 style={{ fontFamily: 'var(--f-display)', fontSize: '20px', color: 'var(--ink)' }}>Shakir Bashar</h3>
                  <span className="badge b-blue-soft">Founder & CEO</span>
                </div>
                <p style={{ fontSize: '14px', color: 'var(--muted)', lineHeight: 1.6, marginBottom: '14px' }}>
                  Computer engineer, operations leader, and technology entrepreneur based in Duhok, Kurdistan. A graduate in Computer Engineering from the University of Mosul with executive experience as Chief Operational Officer & IT Manager, Shakir focuses on systems architecture, digital platform ecosystems, and transparent commerce infrastructure to solve the fragmentation of Iraqi retail.
                </p>
                <div className="founder-contact-row">
                  <a
                    href="mailto:shbhky@gmail.com"
                    style={{ color: 'var(--blue)', fontWeight: 600, display: 'inline-flex', alignItems: 'center', gap: '6px' }}
                  >
                    <Mail className="lucide" />
                    <span>shbhky@gmail.com</span>
                  </a>
                  <span style={{ color: 'var(--line)' }}>•</span>
                  <a
                    href="tel:+9647825837179"
                    style={{ color: 'var(--muted)', display: 'inline-flex', alignItems: 'center', gap: '6px' }}
                  >
                    <Phone className="lucide" />
                    <span>+964 782 583 7179</span>
                  </a>
                  <span style={{ color: 'var(--line)' }}>•</span>
                  <a
                    href="https://linkedin.com/in/shakirbr"
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{ color: 'var(--muted)', display: 'inline-flex', alignItems: 'center', gap: '6px' }}
                  >
                    <ExternalLink className="lucide" />
                    <span>LinkedIn</span>
                  </a>
                </div>
              </div>
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
              Be part of our launch.
            </h2>
            <p style={{ fontSize: '16px', color: 'var(--muted)', maxWidth: '520px', margin: '0 auto 28px' }}>
              Whether you are a shopper looking for better prices or a store owner looking to grow, we welcome you to Cheapify.
            </p>
            <div style={{ display: 'flex', gap: '12px', justifyContent: 'center', flexWrap: 'wrap' }}>
              <Link to="/#waitlist" className="btn btn-primary btn-pill btn-lg">
                Join Shopper Waitlist
              </Link>
              <Link to="/#stores" className="btn btn-secondary btn-pill btn-lg">
                Apply as Merchant
              </Link>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};
