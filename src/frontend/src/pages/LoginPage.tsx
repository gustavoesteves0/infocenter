import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const LoginPage: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await axios.post("http://localhost:8000/token", {
        username: email,
        password: password,
      }, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });
      const { access_token } = response.data;
      localStorage.setItem("token", access_token);
      setError("");
      navigate("/home"); 
    } catch (err) {
      setError("Invalid email or password");
    }
  };

  return (
    <div className="bg-background text-text min-h-screen flex justify-center items-center">
      <div className="bg-black p-8 rounded flex-col">
        {error && <div className="text-red-500 mb-4">{error}</div>}
        <div className="flex items-center bg-white text-gray-800 rounded mb-4 p-2">
          <img src="/img/login_email_img.svg" alt="Email Icon" className="w-6 h-6 mr-2" />
          <input
            type="email"
            placeholder="E-Mail"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full bg-transparent focus:outline-none focus:ring-0 text-black"
          />
        </div>
        <div className="flex items-center bg-white text-gray-800 rounded mb-4 p-2">
          <img src="/img/login_password_img.svg" alt="Password Icon" className="w-6 h-6 mr-2" />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full bg-transparent focus:outline-none focus:ring-0 text-black"
          />
        </div>
        <div className="flex justify-center">
          <button className="bg-primary text-white px-4 py-2 rounded" onClick={handleLogin}>
            Login
          </button>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;