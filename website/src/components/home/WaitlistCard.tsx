import React, { useState } from 'react';
import { ArrowRight, CheckCircle2, RotateCcw } from 'lucide-react';
import { WhatsAppIcon } from '../common/WhatsAppIcon';

export const WaitlistCard: React.FC = () => {
  const [role, setRole] = useState<'shopper' | 'merchant'>('shopper');
  const [contact, setContact] = useState('');
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const trimmed = contact.trim();
    if (!trimmed) return;

    setLoading(true);
    setErrorMsg(null);

    // 1. Always save locally as immediate offline backup
    try {
      const existing = JSON.parse(localStorage.getItem('cheapify_waitlist') || '[]');
      existing.push({
        contact: trimmed,
        role,
        date: new Date().toISOString(),
      });
      localStorage.setItem('cheapify_waitlist', JSON.stringify(existing));
    } catch {
      // ignore localStorage quota errors
    }

    // 2. Transmit to server API
    try {
      const response = await fetch('/api/waitlist', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          contact: trimmed,
          role,
          timestamp: new Date().toISOString(),
        }),
      });

      if (!response.ok) {
        console.warn('Server response status:', response.status);
      }
    } catch (err) {
      console.warn('Network error saving to /api/waitlist, offline fallback used', err);
    } finally {
      setLoading(false);
      setSubmitted(true);
    }
  };

  const handleReset = () => {
    setSubmitted(false);
    setContact('');
    setErrorMsg(null);
  };

  const whatsappMessage =
    role === 'shopper'
      ? `Hello Cheapify! I just joined the early access waitlist as a shopper with phone: ${contact}`
      : `Hello Cheapify! I applied to join as a founding merchant with store/phone: ${contact}`;

  const whatsappUrl = `https://wa.me/9647825837179?text=${encodeURIComponent(whatsappMessage)}`;

  return (
    <div className="waitlist-card" id="waitlist">
      <div className="role-switcher">
        <button
          type="button"
          className={`role-tab ${role === 'shopper' ? 'active' : ''}`}
          onClick={() => {
            setRole('shopper');
            setErrorMsg(null);
          }}
        >
          I'm a Shopper
        </button>
        <button
          type="button"
          className={`role-tab ${role === 'merchant' ? 'active' : ''}`}
          onClick={() => {
            setRole('merchant');
            setErrorMsg(null);
          }}
        >
          I Own a Store
        </button>
      </div>

      {!submitted ? (
        <form onSubmit={handleSubmit} className="waitlist-form">
          <div className="input-pill-wrapper">
            <input
              type="text"
              id="contactInput"
              className="input-pill-field"
              placeholder={
                role === 'shopper'
                  ? 'Enter WhatsApp or phone number'
                  : 'Enter store name & WhatsApp number'
              }
              value={contact}
              onChange={(e) => setContact(e.target.value)}
              required
              autoComplete="tel"
              disabled={loading}
            />
            <button
              type="submit"
              className="btn btn-primary input-pill-btn"
              disabled={loading || !contact.trim()}
            >
              <span>{loading ? 'Joining...' : 'Get Early Access'}</span>
              <ArrowRight className="lucide" />
            </button>
          </div>

          {errorMsg && (
            <p style={{ color: 'var(--red)', fontSize: '13px', marginTop: '8px' }}>
              {errorMsg}
            </p>
          )}

          <div className="waitlist-meta">
            <span className="dot" />
            <span>
              {role === 'shopper'
                ? 'Limited early access · 5,000 IQD welcome voucher on your first order.'
                : 'Verified merchant partners · 0% commission in your first month.'}
            </span>
          </div>
        </form>
      ) : (
        <div style={{ textAlign: 'center', padding: '12px 4px' }}>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', marginBottom: '8px' }}>
            <span className="badge b-best-soft" style={{ fontSize: '13px', padding: '6px 14px' }}>
              <CheckCircle2 size={16} style={{ color: 'var(--green)' }} />
              <span>You're on the early access list!</span>
            </span>
          </div>

          <p style={{ fontSize: '14.5px', color: 'var(--ink)', fontWeight: 600, margin: '8px 0 4px' }}>
            {role === 'shopper'
              ? `Your 5,000 IQD welcome voucher is reserved for ${contact}.`
              : `Your store application has been recorded for ${contact}.`}
          </p>

          <p style={{ fontSize: '13.5px', color: 'var(--muted)', margin: '0 auto 16px', maxWidth: '420px' }}>
            {role === 'shopper'
              ? 'We will send your VIP launch link directly to your WhatsApp when ordering opens in your area.'
              : 'Our merchant onboarding team will contact you directly to set up your store and 0% launch rate.'}
          </p>

          <div style={{ display: 'flex', gap: '10px', justifyContent: 'center', flexWrap: 'wrap' }}>
            <a
              href={whatsappUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-success btn-pill btn-sm"
              style={{ display: 'inline-flex', alignItems: 'center', gap: '6px' }}
            >
              <WhatsAppIcon size={16} />
              <span>Confirm on WhatsApp</span>
            </a>
            <button
              type="button"
              className="btn btn-secondary btn-pill btn-sm"
              onClick={handleReset}
              style={{ display: 'inline-flex', alignItems: 'center', gap: '6px' }}
            >
              <RotateCcw size={14} />
              <span>Register another number</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
