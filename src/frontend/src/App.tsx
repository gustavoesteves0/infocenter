import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import InsightPage from "./pages/InsightPage";
import LoginPage from "./pages/LoginPage";
import PersonalDashboard from "./pages/PersonalDashboard";
import RegisterPage from "./pages/RegisterPage";

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />}></Route>
        <Route path="/home" element={<Home />} />
        <Route path="/insight" element={<InsightPage />} />
        <Route path="/dashboard" element={<PersonalDashboard />} />
      </Routes>
    </Router>
  );
};

export default App;