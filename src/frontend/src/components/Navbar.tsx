import React from "react";

const Navbar: React.FC = () => {
  return (
    <div className="bg-primary p-4 flex justify-center items-center relative">
      {/* Search Bar */}
      <input
        type="text"
        placeholder="Search"
        className="bg-black text-white px-4 py-2 rounded-full w-1/3 mx-auto focus:outline-none"
      />
      {/* User Icon */}
      <img
        src="/img/USER.svg"
        className="w-8 absolute right-4"
        alt="User Icon"
      />
    </div>
  );
};

export default Navbar;