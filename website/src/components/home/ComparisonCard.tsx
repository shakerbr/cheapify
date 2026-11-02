import React, { useState } from 'react';
import { Sparkle, Clock, ShieldCheck, ShoppingBag, Banknote, CreditCard } from 'lucide-react';
import ankerProductImg from '../../assets/product-anker.png';

interface StoreOffer {
  id: string;
  name: string;
  itemPrice: number;
  deliveryFee: number;
  deliveryTime: string;
  rating?: string;
  reviews?: number;
  isVerified?: boolean;
  isBest?: boolean;
}

const storeOffers: StoreOffer[] = [
  {
    id: 'dna',
    name: 'DNA Iraq',
    itemPrice: 95000,
    deliveryFee: 3000,
    deliveryTime: 'Today · 2h Express',
    rating: '4.9',
    reviews: 382,
    isBest: true,
  },
  {
    id: 'shopini',
    name: 'Shopini',
    itemPrice: 118000,
    deliveryFee: 3000,
    deliveryTime: 'Tomorrow morning',
    isVerified: true,
  },
  {
    id: 'class_mobile',
    name: 'Class Mobile',
    itemPrice: 150000,
    deliveryFee: 5000,
    deliveryTime: '1–2 days tracked delivery',
    isVerified: true,
  },
  {
    id: 'social_avg',
    name: 'Instagram DM Sellers',
    itemPrice: 175000,
    deliveryFee: 5000,
    deliveryTime: 'Unverified · 3–5 days wait',
  },
];

export const ComparisonCard: React.FC = () => {
  const [selectedVariant, setSelectedVariant] = useState<'black' | 'blue' | 'silver'>('black');
  const [paymentMethod, setPaymentMethod] = useState<'cod' | 'credit'>('cod');

  const bestOffer = storeOffers[0];
  const otherOffers = storeOffers.slice(1);
  const bestTotal = bestOffer.itemPrice + bestOffer.deliveryFee;

  const handleOrderClick = () => {
    const input = document.getElementById('contactInput');
    if (input) {
      input.focus();
      input.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  };

  return (
    <div className="cmp-card-v2">
      {/* Product Master SKU Header */}
      <div className="cmp-v2-prod">
        <div className="prod-visual">
          <img
            src={ankerProductImg}
            alt="Anker Zolo 25,000mAh 165W Power Bank"
            className="prod-img-tag"
          />
        </div>
        <div className="prod-meta-box">
          <div className="prod-cat-row">
            <span className="badge b-blue-soft">Single Master SKU</span>
            <span className="prod-verified-count">4 Local Sellers Ranked</span>
          </div>
          <h3 className="prod-headline">Anker Zolo Power Bank (25,000mAh, 165W)</h3>
          <p className="prod-subline">Built-in Retractable USB-C Cables · Smart Digital Display</p>
          <div className="prod-variant-row">
            <button
              type="button"
              className={`color-pill pill-black ${selectedVariant === 'black' ? 'active' : ''}`}
              onClick={() => setSelectedVariant('black')}
              aria-label="Select Black"
            >
              <span className="color-piece black"></span>
              <span className="color-text">Black</span>
            </button>
            <button
              type="button"
              className={`color-pill pill-blue ${selectedVariant === 'blue' ? 'active' : ''}`}
              onClick={() => setSelectedVariant('blue')}
              aria-label="Select Ice Blue"
            >
              <span className="color-piece blue"></span>
              <span className="color-text">Ice Blue</span>
            </button>
            <button
              type="button"
              className={`color-pill pill-silver ${selectedVariant === 'silver' ? 'active' : ''}`}
              onClick={() => setSelectedVariant('silver')}
              aria-label="Select Silver"
            >
              <span className="color-piece silver"></span>
              <span className="color-text">Silver</span>
            </button>
          </div>
        </div>
      </div>

      {/* Best Deal Highlighted Offer */}
      <div className="cmp-v2-winner-wrap">
        <div className="cmp-v2-winner-box">
          <div className="winner-badge-row">
            <span className="badge b-best">
              <Sparkle className="lucide" />
              <span>Best Total Deal</span>
            </span>
            <span className="badge b-blue-soft">
              <Clock className="lucide" />
              <span>{bestOffer.deliveryTime}</span>
            </span>
          </div>

          <div className="winner-store-row">
            <div className="store-avatar">DNA</div>
            <div className="winner-store-info">
              <div className="store-title-line">
                <h4>{bestOffer.name}</h4>
                <span className="verified-tag">
                  <ShieldCheck className="lucide" />
                  <span>Verified Partner</span>
                </span>
              </div>
              <div className="store-sub-meta">
                <strong>{bestOffer.rating} ★</strong> ({bestOffer.reviews} verified orders)
              </div>
            </div>
          </div>

          {/* Clean Price Breakdown Bar */}
          <div className="winner-price-strip">
            <div className="price-breakdown-details">
              <div className="price-detail-item">
                <span className="lbl">Item Price</span>
                <span className="val tnum">{bestOffer.itemPrice.toLocaleString()} IQD</span>
              </div>
              <span className="math-plus">+</span>
              <div className="price-detail-item">
                <span className="lbl">Courier</span>
                <span className="val tnum">{bestOffer.deliveryFee.toLocaleString()} IQD</span>
              </div>
            </div>

            <div className="price-doorstep-total">
              <span className="lbl">Total Doorstep Price</span>
              <div className="val-total tnum">
                {bestTotal.toLocaleString()} <span className="cur">IQD</span>
              </div>
            </div>
          </div>

          {/* Payment Method Selector */}
          <div className="payment-method-row">
            <button
              type="button"
              className={`pay-method-pill ${paymentMethod === 'cod' ? 'active' : ''}`}
              onClick={() => setPaymentMethod('cod')}
              aria-label="Cash on Delivery"
            >
              <Banknote className="lucide" />
              <span>Cash on Delivery</span>
            </button>
            <button
              type="button"
              className={`pay-method-pill ${paymentMethod === 'credit' ? 'active' : ''}`}
              onClick={() => setPaymentMethod('credit')}
              aria-label="Credit Card or Electronic"
            >
              <CreditCard className="lucide" />
              <span>Credit / Card</span>
            </button>
          </div>

          {/* Primary CTA */}
          <button
            type="button"
            className="btn btn-primary btn-pill btn-order-v2"
            onClick={handleOrderClick}
          >
            <ShoppingBag className="lucide" />
            <span>Order Now</span>
          </button>

          {/* Clean Dynamic Reassurance */}
          <div className="winner-trust-strip">
            <ShieldCheck className="lucide" />
            <span className="trust-text-desktop">
              {paymentMethod === 'cod'
                ? 'Pay after inspecting at your door · 48-hour return window'
                : 'Secure electronic payment · 48-hour return window'}
            </span>
            <span className="trust-text-mobile">
              {paymentMethod === 'cod'
                ? 'Inspect at door · 48h return window'
                : 'Secure payment · 48h return window'}
            </span>
          </div>
        </div>
      </div>

      {/* Other Stores Comparison List */}
      <div className="cmp-v2-alternatives">
        <div className="alt-section-title">
          <span>Other Sellers Offering This SKU</span>
          <span className="alt-note">Ranked by total doorstep price</span>
        </div>

        <div className="alt-stores-list">
          {otherOffers.map((store) => {
            const storeTotal = store.itemPrice + store.deliveryFee;
            const delta = storeTotal - bestTotal;
            const isInstagram = store.id === 'social_avg';

            return (
              <div className={`alt-store-row ${isInstagram ? 'is-dm-seller' : ''}`} key={store.id}>
                <div className="alt-left">
                  <div className="alt-name-row">
                    <b>{store.name}</b>
                    {store.isVerified && (
                      <span className="alt-verified-tag">
                        <ShieldCheck className="lucide" />
                        <span>Verified</span>
                      </span>
                    )}
                    {isInstagram && (
                      <span className="alt-unverified-tag">Unverified</span>
                    )}
                  </div>
                  <div className="alt-breakdown">
                    {store.itemPrice.toLocaleString()} + {store.deliveryFee.toLocaleString()} IQD · {store.deliveryTime}
                  </div>
                </div>

                <div className="alt-right">
                  <div className="alt-total tnum">{storeTotal.toLocaleString()} IQD</div>
                  <div className={`alt-delta tnum ${isInstagram ? 'delta-high' : ''}`}>
                    +{delta.toLocaleString()} IQD {isInstagram ? 'markup' : 'more'}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
