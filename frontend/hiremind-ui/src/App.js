// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import Login from "./pages/Login";
// import Interview from "./pages/Interview";
// import Dashboard from "./pages/Dashboard";
// import Leaderboard from "./pages/Leaderboard";
// import Analytics from "./pages/Analytics";

// function App() {
//   return (
//     <Router>
//       <Routes>
//         <Route path="/" element={<Dashboard />} />
//         <Route path="/interview" element={<Interview />} />
//         <Route path="/leaderboard" element={<Leaderboard />} />
//         <Route path="/analytics" element={<Analytics />} />
//         <Route path="/login" element={<Login />} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import InterviewPDF from "./pages/InterviewPDF";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Interview from "./pages/Interview";
import Leaderboard from "./pages/Leaderboard";
import Analytics from "./pages/Analytics";

function App() {
  return (
    <Router>
      <Routes>

        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />

        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/interview" element={<Interview />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/pdf-interview" element={<InterviewPDF />} />

      </Routes>
    </Router>
  );
}

export default App;