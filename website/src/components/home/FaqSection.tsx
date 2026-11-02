import React, { useState } from 'react';
import { ChevronDown, HelpCircle } from 'lucide-react';

interface FaqItem {
  question: string;
  answer: string;
}

const faqs: FaqItem[] = [
  {
    question: 'How does Cheapify determine the "Best Value" store?',
    answer:
      'Our intelligent algorithm calculates the total doorstep price (Item Price + Standard Courier Delivery) combined with fulfillment speed and store rating. Ranking is strictly objective and merit-based — positions cannot be bought with advertising.',
  },
  {
    question: 'Can I inspect my order before paying the delivery driver?',
    answer:
      'Yes, 100%. Cheapify supports Cash on Delivery on all orders. Your parcel arrives in a tamper-evident sealed mailer with a unique waybill number. You pay the courier only after receiving and holding your package.',
  },
  {
    question: 'What happens if an item arrives damaged or wrong?',
    answer:
      'Every order is backed by our 48-Hour Return Guarantee. If an item is faulty, damaged, or does not match the product specifications, notify us within 48 hours. Our courier will collect the item directly from your doorstep at zero return cost to you.',
  },
  {
    question: 'How do local merchants and store owners sell on Cheapify?',
    answer:
      'Store owners can register directly through our Merchant Portal. There are zero technical setup fees. You get access to the intuitive Merchant Dashboard to manage inventory, receive automated order alerts, and benefit from daily courier pickups from your shop counter.',
  },
  {
    question: 'Which payment methods are supported?',
    answer:
      'Cash on Delivery is available on 100% of orders. We also support direct local electronic payments including FIB, SuperQi, FastPay, and international Visa/Mastercard.',
  },
];

export const FaqSection: React.FC = () => {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const toggle = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <section className="sec alt" id="faq">
      <div className="container">
        <div className="sec-head">
          <div className="sec-tag">
            <span className="badge b-blue-soft">
              <HelpCircle className="lucide" />
              <span>Got Questions?</span>
            </span>
          </div>
          <h2 className="sec-title">Frequently Asked Questions</h2>
          <p className="sec-desc">
            Everything you need to know about shopping, delivery protection, and selling on Cheapify.
          </p>
        </div>

        <div style={{ maxWidth: '820px', margin: '0 auto' }}>
          {faqs.map((faq, i) => {
            const isOpen = openIndex === i;
            return (
              <div
                key={i}
                style={{
                  background: 'var(--white)',
                  border: '1px solid var(--line)',
                  borderRadius: '18px',
                  marginBottom: '12px',
                  overflow: 'hidden',
                  transition: 'box-shadow 0.2s ease, border-color 0.2s ease',
                  boxShadow: isOpen ? 'var(--elev-1)' : 'none',
                }}
              >
                <button
                  type="button"
                  onClick={() => toggle(i)}
                  style={{
                    width: '100%',
                    padding: '20px 24px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    gap: '16px',
                    background: 'none',
                    border: 'none',
                    cursor: 'pointer',
                    textAlign: 'left',
                    fontFamily: 'inherit',
                  }}
                  aria-expanded={isOpen}
                >
                  <span
                    style={{
                      fontSize: '16.5px',
                      fontWeight: 600,
                      color: isOpen ? 'var(--blue)' : 'var(--ink)',
                      lineHeight: 1.4,
                    }}
                  >
                    {faq.question}
                  </span>
                  <ChevronDown
                    className="lucide"
                    style={{
                      color: isOpen ? 'var(--blue)' : 'var(--muted)',
                      transform: isOpen ? 'rotate(180deg)' : 'rotate(0deg)',
                      transition: 'transform 0.25s ease',
                      flexShrink: 0,
                    }}
                    size={20}
                  />
                </button>
                {isOpen && (
                  <div
                    style={{
                      padding: '0 24px 22px',
                      color: 'var(--muted)',
                      fontSize: '15px',
                      lineHeight: 1.65,
                      borderTop: '1px solid #F0F3F6',
                      paddingTop: '14px',
                    }}
                  >
                    {faq.answer}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};
