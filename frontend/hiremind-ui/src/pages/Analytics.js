import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

export default function Analytics() {

  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const username = localStorage.getItem("username");

      const res = await axios.get(
        `http://127.0.0.1:8000/history?username=${username}`
      );

      const formatted = res.data.map((item, index) => ({
        name: `Attempt ${index + 1}`,
        score: item[1]
      }));

      setData(formatted);

    } catch (error) {
      console.error(error);
    }
  };

  // 🔥 Average Score
  const avg =
    data.length > 0
      ? data.reduce((sum, item) => sum + item.score, 0) / data.length
      : 0;

  return (
    <div className="min-h-screen flex justify-center items-center bg-animated relative overflow-hidden">

      {/* 🌟 Glow */}
      <div className="absolute w-72 h-72 bg-white/10 rounded-full blur-3xl top-10 left-10 float"></div>
      <div className="absolute w-72 h-72 bg-purple-300/20 rounded-full blur-3xl bottom-10 right-10 float"></div>

      {/* 💎 Card */}
      <div className="backdrop-blur-xl bg-white/20 border border-white/30 shadow-2xl rounded-2xl p-8 w-full max-w-3xl text-center">

        {/* BACK */}
        <Link to="/dashboard">
          <button className="mb-4 text-white hover:underline">
            ⬅ Back to Dashboard
          </button>
        </Link>

        <h1 className="text-3xl font-bold text-white mb-2">
          📊 Analytics
        </h1>

        {/* 📊 EMPTY STATE */}
        {data.length === 0 ? (
          <div className="mt-6 text-white">
            <p className="text-lg">🚫 No interview data yet</p>
            <p className="text-sm text-gray-200 mt-2">
              Start an interview to see your performance here
            </p>

            <Link to="/interview">
              <button className="mt-4 bg-blue-600 hover:bg-blue-700 px-5 py-2 rounded-lg transition">
                Start Interview
              </button>
            </Link>
          </div>
        ) : (
          <>
            {/* 📈 AVG */}
            <p className="text-gray-200 mb-6">
              Average Score: <b className="text-white">{avg.toFixed(1)}/10</b>
            </p>

            {/* 📉 CHART */}
            <ResponsiveContainer width="100%" height={320}>
              <LineChart data={data}>
                <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />

                <XAxis dataKey="name" stroke="#fff" />
                <YAxis domain={[0, 10]} stroke="#fff" />

                <Tooltip
                  contentStyle={{
                    backgroundColor: "#fff",
                    borderRadius: "10px",
                    border: "1px solid #ccc"
                  }}
                />

                <Line
                  type="monotone"
                  dataKey="score"
                  stroke="#22c55e"
                  strokeWidth={3}
                  dot={{ r: 5 }}
                  activeDot={{ r: 8 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </>
        )}

      </div>
    </div>
  );
}