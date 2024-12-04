import React from "react";

const LoginPage: React.FC = () => {
  return (
    <div className="bg-background text-text min-h-screen flex justify-center items-center">
      <div className="bg-black p-8 rounded flex-col">
        {/* Email Input */}
        <div className="flex items-center bg-white text-gray-800 rounded mb-4 p-2">
          <img
            src="/img/login_email_img.svg"
            alt="Email Icon"
            className="w-6 h-6 mr-2"
          />
          <input
            type="email"
            placeholder="E-Mail"
            className="w-full bg-transparent focus:outline-none focus:ring-0 text-white"
          />
        </div>
        {/* Password Input */}
        <div className="flex items-center bg-white text-gray-800 rounded mb-4 p-2">
          <img
            src="/img/login_password_img.svg"
            alt="Password Icon"
            className="w-6 h-6 mr-2"
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full bg-transparent focus:outline-none focus:ring-0 text-white"
          />
        </div>
        {/* Login Button */}
        <div className="flex justify-center">
          <button className="bg-primary text-white px-4 py-2 rounded">
            Login
          </button>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;