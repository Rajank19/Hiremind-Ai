import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

export default function Leaderboard() {

  const [data, setData] = useState([]);

  useEffect(() => {
    fetchLeaderboard();
  }, []);

  const fetchLeaderboard = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/leaderboard");
      console.log("LEADERBOARD DATA:", res.data); // 🔥 debug
      setData(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-animated relative overflow-hidden">

      {/* 🌟 Glow Effects */}
      <div className="absolute w-72 h-72 bg-white/10 rounded-full blur-3xl top-10 left-10 float"></div>
      <div className="absolute w-72 h-72 bg-yellow-300/20 rounded-full blur-3xl bottom-10 right-10 float"></div>

      {/* 💎 Glass Card */}
      <div className="backdrop-blur-xl bg-white/20 border border-white/30 shadow-2xl rounded-2xl p-8 w-full max-w-2xl">

        {/* 🔙 BACK */}
        <Link to="/dashboard">
          <button className="mb-4 text-white hover:underline">
            ⬅ Back to Dashboard
          </button>
        </Link>

        {/* 🏆 TITLE */}
        <h1 className="text-3xl font-bold text-center text-white mb-6">
          🏆 Leaderboard
        </h1>

        {/* TABLE */}
        {data.length === 0 ? (
          <p className="text-center text-white">No data available</p>
        ) : (
          <div className="overflow-hidden rounded-lg border border-white/30">
            <table className="w-full text-white">

              <thead className="bg-white/20">
                <tr>
                  <th className="p-3">Rank</th>
                  <th className="p-3">User</th>
                  <th className="p-3">Score</th>
                </tr>
              </thead>

              <tbody>
                {data.map((user, index) => (
                  <tr
                    key={index}
                    className="text-center hover:bg-white/10 transition"
                  >
                    <td className="p-3 font-bold">
                      {index === 0 ? "🥇" : index === 1 ? "🥈" : index === 2 ? "🥉" : index + 1}
                    </td>

                    {/* 🔥 FIX HERE */}
                    <td className="p-3 font-semibold">
                      {user.username}
                    </td>

                    <td className="p-3 text-yellow-300 font-semibold">
                      {user.score}/10
                    </td>
                  </tr>
                ))}
              </tbody>

            </table>
          </div>
        )}

      </div>
    </div>
  );
}