import React from "react";

const Card: React.FC = () => {
  return (
    <div className="flex gap-4">
        <div className="bg-black text-white p-4 rounded">
          <h3>CPI-US</h3>
          <p>+0.2%</p>
          <span className="text-red-500">Price</span>
          <span className="text-red-500">USA</span>
        </div>
    </div>
  );
};

export default Card;