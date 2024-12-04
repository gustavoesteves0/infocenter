import React from "react";
import Card from "./Card";

const EmploymentSection: React.FC = () => {
  return (
    <div>
      <h2 className="text-xl mb-2">Employment</h2>
      <div className="flex gap-4">
        <Card />
      </div>
    </div>
  );
};

export default EmploymentSection;