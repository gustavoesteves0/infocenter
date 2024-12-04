import React from "react";
import Card from "./Card";

const FavoritesSection: React.FC = () => {
  return (
    <div>
      <div className="flex">
        <img
          src="/img/favorited.svg"
          className="w-8"
        />
        <h2 className="text-2xl ml-3">Favorites</h2>
        </div>
        <div className="flex gap-4">
          <Card />
        </div>
    </div>
  );
};

export default FavoritesSection;