import React from "react";
import Card from "./Card";

const InterestSection: React.FC = () => {
  const interest = [
    { title: "Fed Funds Rate", value: "4,75-4,50%", category: "Interest", country: "USA" },
  ];

  return (
    <div className="mb-8">
      {/* Section Header */}
      <div className="ml-4 flex items-center mb-4">
        <span className="bg-green-500 rounded-full w-4 h-4"></span>
        <h2 className="text-2xl ml-3 text-white">Interest</h2>
      </div>

      {/* Cards */}
      <div className="flex ml-2 gap-4">
        {interest.map((item, index) => (
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

export default InterestSection;
