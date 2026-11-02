import React from 'react';
import { WaitlistCard } from './WaitlistCard';
import { ComparisonCard } from './ComparisonCard';

export const Hero: React.FC = () => {
  return (
    <section className="hero">
      <div className="container">
        <div className="hero-grid">
          <div className="hero-content">
            <div className="sec-tag">
              <span className="badge b-blue-soft">
                <span className="pulse-dot" />
                Early Access · Kurdistan Launch
              </span>
            </div>

            <h1 className="hero-title">
              One product.<br />
              Every seller.<br />
              <span className="brand-accent">The best price.</span>
            </h1>

            <p className="hero-desc">
              Stop checking ten Instagram accounts or waiting hours for a "price in DM". Cheapify compares verified stores on a single page so you always get the lowest price, delivered to your door with Cash on Delivery.
            </p>

            <WaitlistCard />
          </div>

          <ComparisonCard />
        </div>
      </div>
    </section>
  );
};
