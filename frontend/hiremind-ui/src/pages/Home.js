import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="min-h-screen bg-animated flex flex-col justify-center items-center text-white">

      <h1 className="text-5xl font-bold mb-6 float">
        🚀 HireMind AI
      </h1>

      <p className="text-lg mb-8 text-center max-w-xl">
        Practice AI-powered interviews, get instant feedback, and track your performance like a pro.
      </p>

      <Link to="/login">
        <button className="bg-white text-blue-600 px-6 py-3 rounded-xl font-semibold hover:scale-105 transition">
          Get Started
        </button>
      </Link>

    </div>
  );
}