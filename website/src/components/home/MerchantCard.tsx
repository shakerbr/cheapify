import React from 'react';
import { Check, Store } from 'lucide-react';
import { WhatsAppIcon } from '../common/WhatsAppIcon';

const perks = [
  'Modern Merchant Dashboard',
  'Real-Time Inventory & Order Tracking',
  'Automated Courier Dispatch from Store',
  'Direct & Fast Payout Settlements',
  'Transparent, Low ~4% Platform Fee',
  '0% Commission in Month 1',
];

export const MerchantCard: React.FC = () => {
  return (
    <section className="sec" id="stores">
      <div className="container">
        <div className="merchant-card">
          <div className="merchant-grid">
            <div>
              <span className="badge badge-merchant-kicker">
                <Store className="lucide" />
                <span>For Store Owners & Merchants</span>
              </span>
              <h2>Sell on Cheapify. Keep 96% of your sales.</h2>
              <p>
                Grow your business with a platform built to empower retail. Manage your products effortlessly with our intuitive Merchant Dashboard, connect with ready buyers, and let our courier network handle daily doorstep pickups right from your counter.
              </p>

              <div className="merchant-perks">
                {perks.map((perk, i) => (
                  <div className="merchant-perk" key={i}>
                    <Check className="lucide" style={{ strokeWidth: 2.5 }} />
                    <span>{perk}</span>
                  </div>
                ))}
              </div>

              <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
                <a
                  href="https://wa.me/9647825837179?text=Hello%20Cheapify%20Team%2C%20I%20have%20a%20store%20and%20want%20to%20apply%20as%20a%20merchant."
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn btn-success btn-pill"
                >
                  <WhatsAppIcon className="lucide" size={18} />
                  <span>Chat on WhatsApp</span>
                </a>
                <a
                  href="mailto:shbhky@gmail.com?subject=Merchant%20Partnership%20Application"
                  className="btn btn-secondary btn-pill"
                >
                  <span>Email Store Details</span>
                </a>
              </div>
            </div>

            <div className="merchant-side-box">
              <h3>Empowering Local Retail</h3>
              <p>
                Whether you run an established retail storefront or a specialized boutique, Cheapify provides the modern software and logistics infrastructure to scale without technical friction.
              </p>

              <table className="tbl">
                <thead>
                  <tr>
                    <th>Platform</th>
                    <th>Take-Home on 25,000 IQD</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Traditional Marketplace (15–20%)</td>
                    <td className="tnum">20,000 – 21,250 IQD</td>
                  </tr>
                  <tr className="win-row">
                    <td>Cheapify (~4% fee)</td>
                    <td className="tnum">24,050 IQD (96%)</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
