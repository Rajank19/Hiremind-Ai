import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [username, setUsername] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    if (!username.trim()) {
      alert("Enter username");
      return;
    }

    localStorage.setItem("username", username);
    navigate("/dashboard"); // ✅ FIXED REDIRECT
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-gradient-to-br from-blue-500 via-purple-500 to-pink-500 relative overflow-hidden">

      {/* 🔥 Background Glow */}
      <div className="absolute w-[500px] h-[500px] bg-white opacity-10 rounded-full blur-3xl top-10 left-10"></div>
      <div className="absolute w-[400px] h-[400px] bg-pink-300 opacity-20 rounded-full blur-3xl bottom-10 right-10"></div>

      {/* 💎 Glass Card */}
      <div className="backdrop-blur-xl bg-white/20 border border-white/30 shadow-2xl rounded-2xl p-10 w-80 text-center transition hover:scale-105">

        <h1 className="text-3xl font-bold text-white mb-6 tracking-wide">
          🚀 HireMind AI
        </h1>

        <input
          type="text"
          placeholder="Enter your name"
          className="w-full p-3 rounded-lg bg-white/80 focus:outline-none mb-4 text-gray-700"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleLogin(); // ✅ Enter key support
          }}
        />

        <button
          onClick={handleLogin}
          className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-purple-600 hover:to-pink-500 text-white py-3 rounded-lg transition duration-300 shadow-lg hover:shadow-2xl active:scale-95"
        >
          Enter
        </button>

      </div>

    </div>
  );
}