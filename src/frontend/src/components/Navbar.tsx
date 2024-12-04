import React from "react";

const Navbar: React.FC = () => {
  return (
    <div className="bg-primary p-4 flex justify-between items-center">
      <input
        type="text"
        placeholder="Search"
        className="bg-black text-white px-4 py-2 rounded w-1/3"
      />
      <div className="text-white">User Icon</div>
    </div>
  );
};

export default Navbar;