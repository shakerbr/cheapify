import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Menu, X } from 'lucide-react';

export const Navbar: React.FC = () => {
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    setMobileMenuOpen(false);
  }, [location.pathname, location.hash]);

  const handleWaitlistClick = (e: React.MouseEvent) => {
    if (location.pathname === '/') {
      e.preventDefault();
      const input = document.getElementById('contactInput');
      if (input) {
        input.focus();
        input.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  };

  const handleFeaturesClick = (e: React.MouseEvent) => {
    if (location.pathname === '/') {
      e.preventDefault();
      const section = document.getElementById('features');
      if (section) {
        section.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  };

  return (
    <div className="navbar-float-wrap">
      <header className="navbar">
        <Link to="/" className="brand-link" onClick={() => setMobileMenuOpen(false)}>
          <img src="/assets/cheapify-logo.svg" alt="Cheapify" className="logo-mark" />
          <span>Cheapify</span>
        </Link>

        <nav>
          <ul className="nav-links">
            <li>
              <Link
                to="/how-it-works"
                className={`nav-link ${location.pathname === '/how-it-works' ? 'active' : ''}`}
              >
                How It Works
              </Link>
            </li>
            <li>
              <Link
                to="/#features"
                className="nav-link"
                onClick={handleFeaturesClick}
              >
                Features
              </Link>
            </li>
            <li>
              <Link to="/#stores" className="nav-link">
                For Stores
              </Link>
            </li>
            <li>
              <Link
                to="/about"
                className={`nav-link ${location.pathname === '/about' ? 'active' : ''}`}
              >
                About
              </Link>
            </li>
          </ul>
        </nav>

        <div className="nav-cta">
          <Link
            to="/#waitlist"
            className="btn btn-primary btn-pill btn-sm nav-cta-btn"
            onClick={handleWaitlistClick}
          >
            Join Waitlist
          </Link>
          <button
            type="button"
            className={`mobile-menu-toggle ${mobileMenuOpen ? 'open' : ''}`}
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label={mobileMenuOpen ? 'Close menu' : 'Open menu'}
            aria-expanded={mobileMenuOpen}
          >
            {mobileMenuOpen ? <X className="lucide" /> : <Menu className="lucide" />}
          </button>
        </div>
      </header>

      {mobileMenuOpen && (
        <div className="mobile-menu-dropdown">
          <nav className="mobile-nav">
            <Link
              to="/how-it-works"
              className={`mobile-nav-link ${location.pathname === '/how-it-works' ? 'active' : ''}`}
              onClick={() => setMobileMenuOpen(false)}
            >
              How It Works
            </Link>
            <Link
              to="/#features"
              className="mobile-nav-link"
              onClick={(e) => {
                setMobileMenuOpen(false);
                handleFeaturesClick(e);
              }}
            >
              Features
            </Link>
            <Link
              to="/#stores"
              className="mobile-nav-link"
              onClick={() => setMobileMenuOpen(false)}
            >
              For Stores
            </Link>
            <Link
              to="/about"
              className={`mobile-nav-link ${location.pathname === '/about' ? 'active' : ''}`}
              onClick={() => setMobileMenuOpen(false)}
            >
              About Cheapify
            </Link>
          </nav>
          <div className="mobile-menu-footer">
            <Link
              to="/#waitlist"
              className="btn btn-primary btn-pill btn-sm full-width"
              onClick={(e) => {
                setMobileMenuOpen(false);
                handleWaitlistClick(e);
              }}
            >
              Join Early Access Waitlist
            </Link>
          </div>
        </div>
      )}
    </div>
  );
};
