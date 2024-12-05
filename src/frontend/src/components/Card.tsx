import React from "react";

interface CardProps {
  title: string;
  value: string;
  category: string;
  country: string;
}

const Card: React.FC<CardProps> = ({ title, value, category, country }) => {
  return (
    <div className="bg-black border border-green-500 rounded-md p-2 flex flex-col items-start justify-center text-white min-w-40 hover:cursor-pointer">
      <div className="flex">
        <h3 className="text-lg font-bold">{title}</h3>
        <p className="text-sm ml-10 mt-1">{value}</p>
      </div>
      <div className="mt-2 flex gap-2">
        <span className="text-xs bg-green-500 px-2 py-1 rounded-full">{category}</span>
        <span className="text-xs bg-gray-800 px-2 py-1 rounded-full">{country}</span>
      </div>
    </div>
  );
};

export default Card;