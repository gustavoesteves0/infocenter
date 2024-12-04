import React from "react";
import Navbar from "../components/Navbar";

const PersonalDashboard: React.FC = () => {
  return (
    <div className="bg-background text-text min-h-screen">
      <Navbar />
      <div className="p-4">
        <h1 className="text-3xl mb-4">My Dashboard</h1>
        <div className="grid grid-cols-4 gap-4">
          <div className="bg-black text-white p-4 flex justify-center items-center">
            + Add New
          </div>
        </div>
      </div>
    </div>
  );
};

export default PersonalDashboard;
