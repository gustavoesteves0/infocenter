import React from "react";
import Navbar from "../components/Navbar";

const InsightPage: React.FC = () => {
  return (
    <div className="bg-background text-text min-h-screen">
      <Navbar />
      <div className="p-4">
        <h1 className="text-3xl mb-4">Consumer Price Index</h1>
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-white p-4">Graph 1</div>
          <div className="bg-white p-4">Graph 2</div>
        </div>
        <div className="mt-4">
          <h2>Frequency: Monthly</h2>
          <p className="mt-2">
            The Consumer Price Index for All Urban Consumers...
          </p>
        </div>
      </div>
    </div>
  );
};

export default InsightPage;
