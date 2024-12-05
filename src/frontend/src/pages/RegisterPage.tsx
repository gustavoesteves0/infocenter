import React, { useState } from "react";
import axios from "axios";

const RegisterPage: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleRegister = async () => {
    try {
      const response = await axios.post("http://localhost:8000/register", {
        email,
        password,
        first_name: firstName,
        last_name: lastName,
      }, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      setSuccess("Registration successful! You can now log in.");
      setError("");
      setEmail("");
      setPassword("");
      setFirstName("");
      setLastName("");
    } catch (err: any) {
      setSuccess("");
      setError(err.response?.data?.detail || "Registration failed.");
    }
  };

  return (
    <div className="bg-background text-text min-h-screen flex justify-center items-center">
      <div className="bg-black p-8 rounded flex-col w-96">
        {error && <div className="text-red-500 mb-4">{error}</div>}
        {success && <div className="text-green-500 mb-4">{success}</div>}
        <div className="flex items-center bg-white text-gray-800 rounded mb-4 p-2">
          <input
            type="text"
            placeholder="First Name"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            className="w-full bg-transparent focus:outline-none focus:ring-0 text-black"
          />
        </div>
        <div className="flex items-center bg-white text-gray-800 rounded mb-4 p-2">
          <input
            type="text"
            placeholder="Last Name"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            className="w-full bg-transparent focus:outline-none focus:ring-0 text-black"
          />
        </div>
        <div className="flex items-center bg-white text-gray-800 rounded mb-4 p-2">
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full bg-transparent focus:outline-none focus:ring-0 text-black"
          />
        </div>
        <div className="flex items-center bg-white text-gray-800 rounded mb-4 p-2">
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full bg-transparent focus:outline-none focus:ring-0 text-black"
          />
        </div>
        <div className="flex justify-center">
          <button className="bg-primary text-white px-4 py-2 rounded" onClick={handleRegister}>
            Register
          </button>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;