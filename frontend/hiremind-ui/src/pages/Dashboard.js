// import { Link } from "react-router-dom";
// import { useEffect } from "react";
// import { useNavigate } from "react-router-dom";

// export default function Dashboard() {

//   const navigate = useNavigate();

//   useEffect(() => {
//     const user = localStorage.getItem("username");
//     if (!user) {
//       navigate("/login");
//     }
//   }, [navigate]);

//   return (
//     <div className="min-h-screen flex justify-center items-center bg-animated relative overflow-hidden">

//       {/* 🌟 Background Glow */}
//       <div className="absolute w-72 h-72 bg-white/10 rounded-full blur-3xl top-10 left-10 float"></div>
//       <div className="absolute w-72 h-72 bg-pink-300/20 rounded-full blur-3xl bottom-10 right-10 float"></div>

//       {/* 💎 Glass Card */}
//       <div className="backdrop-blur-xl bg-white/20 border border-white/30 shadow-2xl rounded-2xl p-10 w-[400px] text-center">

//         <h1 className="text-3xl font-bold text-white mb-8">
//           🚀 HireMind AI Dashboard
//         </h1>

//         <div className="space-y-4">

//           <Link to="/interview">
//             <button className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg transition shadow-lg">
//               Start Interview
//             </button>
//           </Link>

//           <Link to="/leaderboard">
//             <button className="w-full bg-green-600 hover:bg-green-700 text-white py-3 rounded-lg transition shadow-lg">
//               Leaderboard
//             </button>
//           </Link>

//           <Link to="/analytics">
//             <button className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg transition shadow-lg">
//               Analytics
//             </button>
//           </Link>

//         </div>

//       </div>

//     </div>
//   );
// }
import { Link, useNavigate } from "react-router-dom";
import { useEffect } from "react";

export default function Dashboard() {

  const navigate = useNavigate();
  const username = localStorage.getItem("username");

  // 🔐 Protect route
  useEffect(() => {
    if (!username) {
      navigate("/login");
    }
  }, [navigate, username]);

  // 🔓 Logout
  const handleLogout = () => {
    localStorage.removeItem("username");
    navigate("/login");
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-animated relative overflow-hidden">

      {/* 🌟 Background Glow */}
      <div className="absolute w-72 h-72 bg-white/10 rounded-full blur-3xl top-10 left-10 float"></div>
      <div className="absolute w-72 h-72 bg-pink-300/20 rounded-full blur-3xl bottom-10 right-10 float"></div>

      {/* 💎 Glass Card */}
      <div className="backdrop-blur-xl bg-white/20 border border-white/30 shadow-2xl rounded-2xl p-10 w-[400px] text-center hover:scale-105 transition">

        {/* 👤 User */}
        <h1 className="text-3xl font-bold text-white mb-2">
          🚀 Welcome, {username}
        </h1>

        <p className="text-gray-200 mb-6">
          Ready to crack your next interview?
        </p>

        {/* 🔘 Buttons */}
        <div className="space-y-4">

          {/* 🤖 AI Interview */}
          <Link to="/interview">
            <button className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg transition shadow-lg hover:scale-105">
              🤖 AI Interview
            </button>
          </Link>

          {/* 📄 PDF Interview (NEW 🔥) */}
          <Link to="/pdf-interview">
            <button className="w-full bg-yellow-500 hover:bg-yellow-600 text-white py-3 rounded-lg transition shadow-lg hover:scale-105">
              📄 PDF Interview
            </button>
          </Link>

          {/* 🏆 Leaderboard */}
          <Link to="/leaderboard">
            <button className="w-full bg-green-600 hover:bg-green-700 text-white py-3 rounded-lg transition shadow-lg hover:scale-105">
              🏆 Leaderboard
            </button>
          </Link>

          {/* 📊 Analytics */}
          <Link to="/analytics">
            <button className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg transition shadow-lg hover:scale-105">
              📊 Analytics
            </button>
          </Link>

        </div>

        {/* 🚪 Logout */}
        <button
          onClick={handleLogout}
          className="mt-6 w-full bg-red-500 hover:bg-red-600 text-white py-2 rounded-lg transition"
        >
          Logout
        </button>

      </div>

    </div>
  );
}