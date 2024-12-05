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
      <div className="p-8">
        <h1 className="text-5xl mb-4 ml-10">
          Hello, <span className="text-green-500">User</span>. <br /> What are we looking for today?
        </h1>
        <div className="bg-white h-[1px] w-full mt-10"></div>
        <FavoritesSection />
        <EmploymentSection />
        <InterestSection />
        <PriceSection />
      </div>
    </div>
  );
};

export default Home;
