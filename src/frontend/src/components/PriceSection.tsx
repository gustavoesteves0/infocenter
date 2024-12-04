import React from "react";
import Card from "./Card";

const PriceSection: React.FC = () => {
  return (
    <div>
      <h2 className="text-xl mb-2">Price</h2>
      <div className="flex gap-4">
        <Card />
      </div>
    </div>
  );
};

export default PriceSection;