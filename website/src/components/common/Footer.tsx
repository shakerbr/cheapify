import React from 'react';
import { Link } from 'react-router-dom';
import { WhatsAppIcon } from './WhatsAppIcon';

export const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-top">
          <div className="footer-brand">
            <Link to="/" className="brand-link">
              <img src="/assets/cheapify-logo.svg" alt="Cheapify" className="logo-mark" />
              <span>Cheapify</span>
            </Link>
            <div className="footer-slogan">The bright side of choosing.</div>
            <p className="footer-desc">
              The multi-seller price comparison marketplace. Compare verified stores, find the best deal, and order with Cash on Delivery.
            </p>
          </div>

          <div className="footer-col">
            <h4>Platform</h4>
            <ul className="footer-links">
              <li><Link to="/how-it-works">How It Works</Link></li>
              <li><Link to="/about">About Cheapify</Link></li>
              <li><a href="/brand/">Brandbook & Assets</a></li>
              <li><a href="/#stores">Sell on Cheapify</a></li>
            </ul>
          </div>

          <div className="footer-col">
            <h4>Customer Care</h4>
            <ul className="footer-links">
              <li><Link to="/how-it-works#returns">48-Hour Return Policy</Link></li>
              <li><Link to="/how-it-works#delivery">Delivery & Coverage</Link></li>
              <li><Link to="/how-it-works#payment">Cash on Delivery</Link></li>
              <li><a href="mailto:shbhky@gmail.com">Help & Support</a></li>
            </ul>
          </div>

          <div className="footer-col">
            <h4>Contact & Headquarters</h4>
            <ul className="footer-links">
              <li><span style={{ color: 'var(--muted)', fontSize: '13.5px' }}>Kurdistan Region, Iraq</span></li>
              <li><a href="tel:+9647825837179">+964 782 583 7179</a></li>
              <li><a href="mailto:shbhky@gmail.com">shbhky@gmail.com</a></li>
              <li>
                <a
                  href="https://wa.me/9647825837179"
                  target="_blank"
                  rel="noopener noreferrer"
                  style={{ color: 'var(--green)', fontWeight: 600, display: 'inline-flex', alignItems: 'center', gap: '6px' }}
                >
                  <WhatsAppIcon className="lucide" size={15} />
                  <span>WhatsApp Support</span>
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="footer-bottom">
          <div>&copy; 2026 Cheapify Marketplace. All rights reserved.</div>
          <div>
            <span>Kurdistan Region, Iraq</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
