import React from "react";
import Card from "./Card";

const PriceSection: React.FC = () => {
  const price = [
    { title: "CPI-US", value: "+0.2%", category: "Price", country: "USA" },
  ];

  return (
    <div className="mb-8">
      {/* Section Header */}
      <div className="ml-4 flex items-center mb-4">
        <span className="bg-green-500 rounded-full w-4 h-4"></span>
        <h2 className="text-2xl ml-3 text-white">Price</h2>
      </div>

      {/* Cards */}
      <div className="flex ml-2 gap-4">
        {price.map((item, index) => (
          <Card
            key={index}
            title={item.title}
            value={item.value}
            category={item.category}
            country={item.country}
          />
        ))}
      </div>
      <div className="bg-white h-[1px] w-full mt-10"></div>
    </div>
  );
};

export default PriceSection;