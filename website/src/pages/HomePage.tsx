import React from 'react';
import { Hero } from '../components/home/Hero';
import { TrustGrid } from '../components/home/TrustGrid';
import { FeatureBento } from '../components/home/FeatureBento';
import { MerchantCard } from '../components/home/MerchantCard';
import { FaqSection } from '../components/home/FaqSection';

export const HomePage: React.FC = () => {
  return (
    <>
      <Hero />
      <TrustGrid />
      <FeatureBento />
      <MerchantCard />
      <FaqSection />
    </>
  );
};
