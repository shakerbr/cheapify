import React from 'react';
import { Banknote, RotateCcw, ShieldCheck, Truck } from 'lucide-react';

interface TrustItem {
  icon: React.ReactNode;
  title: string;
  desc: string;
  tileType?: 'g' | 'k';
}

const trustItems: TrustItem[] = [
  {
    icon: <Banknote className="lucide" />,
    title: 'Cash on Delivery',
    desc: 'Pay at your door after inspecting',
    tileType: 'k',
  },
  {
    icon: <RotateCcw className="lucide" />,
    title: '48-Hour Return Window',
    desc: 'Full protection on wrong or faulty items',
  },
  {
    icon: <ShieldCheck className="lucide" />,
    title: '100% Verified Stores',
    desc: 'Every merchant is verified in person',
    tileType: 'g',
  },
  {
    icon: <Truck className="lucide" />,
    title: 'Fast Doorstep Courier',
    desc: 'Tracked delivery to your home or office',
  },
];

export const TrustGrid: React.FC = () => {
  return (
    <section className="trust-section">
      <div className="container">
        <div className="trust-grid">
          {trustItems.map((item, i) => (
            <div className="trust-item" key={i}>
              <div className={`icon-tile ${item.tileType ? item.tileType : ''}`}>
                {item.icon}
              </div>
              <div className="trust-text">
                <h4>{item.title}</h4>
                <p>{item.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
