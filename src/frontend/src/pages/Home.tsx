import React from "react";
import Navbar from "../components/Navbar";
import FavoritesSection from "../components/FavoritesSection";
import EmploymentSection from "../components/EmploymentSection";
import InterestSection from "../components/InterestSection";
import PriceSection from "../components/PriceSection";

const Home: React.FC = () => {
  return (
    <div className="bg-background text-text min-h-screen">
      <Navbar />
      <div className="p-4">
        <h1 className="text-3xl mb-4">Hello, User. <br />
            What are we looking for today?</h1>
        <FavoritesSection />
        <EmploymentSection />
        <PriceSection />
        <InterestSection />
      </div>
    </div>
  );
};

export default Home;
