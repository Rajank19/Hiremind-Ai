import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

export default function Interview() {

  const [domain, setDomain] = useState("python");
  const [difficulty, setDifficulty] = useState("Easy");
  const [questionData, setQuestionData] = useState(null);
  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState("");
  const [confidence, setConfidence] = useState("");
  const [time, setTime] = useState(30);

  // 🔊 TEXT → SPEECH
  const speak = (text) => {
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US";
    speech.rate = 0.9;
    speech.pitch = 1.1;
    window.speechSynthesis.speak(speech);
  };

  // 🎤 SPEECH → TEXT
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

  const recognition = new SpeechRecognition();
  recognition.continuous = false;
  recognition.lang = "en-US";

  const startListening = () => {
    recognition.start();

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;

      const words = transcript.split(" ").length;

      let level = "Low";
      if (words > 10) level = "Medium";
      if (words > 20) level = "High";

      setConfidence(level);   // 🔥 NEW
      setAnswer(transcript);
    };
  };

  // 🎯 GET QUESTION
  const getQuestion = async () => {
    try {
      const res = await axios.get(
        `http://127.0.0.1:8000/question?domain=${domain}&difficulty=${difficulty}`
      );

      setQuestionData(res.data);
      setAnswer("");
      setResult("");
      setConfidence("");

    } catch (error) {
      console.error(error);
      alert("Error fetching question");
    }
  };

  // 🔊 SPEAK QUESTION
  useEffect(() => {
    if (questionData?.question) {
      speak(questionData.question);
    }
  }, [questionData]);

  // ⏳ TIMER
  useEffect(() => {
    if (!questionData) return;

    setTime(30);

    const timer = setInterval(() => {
      setTime((prev) => {
        if (prev === 1) {
          clearInterval(timer);
          submitAnswer();  // 🔥 AUTO SUBMIT
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);

  }, [questionData]);

  // 🧠 SUBMIT ANSWER
  const submitAnswer = async () => {

    if (!answer.trim()) {
      alert("Please enter your answer");
      return;
    }

    const username = localStorage.getItem("username");

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/answer",
        null,
        {
          params: {
            answer,
            expected_answer: questionData.expected_answer,
            username,
            domain
          }
        }
      );

      setResult(res.data);

      // 🔥 AUTO NEXT QUESTION
      setTimeout(() => {
        getQuestion();
      }, 3000);

    } catch (error) {
      console.error(error);
      alert("Error submitting answer");
    }
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-animated relative overflow-hidden">

      <div className="absolute w-72 h-72 bg-white/10 rounded-full blur-3xl top-10 left-10 float"></div>
      <div className="absolute w-72 h-72 bg-purple-300/20 rounded-full blur-3xl bottom-10 right-10 float"></div>

      <div className="backdrop-blur-xl bg-white/20 border border-white/30 shadow-2xl rounded-2xl p-8 w-full max-w-xl">

        <Link to="/dashboard">
          <button className="mb-4 text-white hover:underline">
            ⬅ Back
          </button>
        </Link>

        <h1 className="text-2xl font-bold text-white text-center mb-6">
          🎤 AI Voice Interview
        </h1>

        {/* ⏳ TIMER */}
        {questionData && (
          <p className="text-center text-red-300 mb-2">
            ⏳ Time Left: {time}s
          </p>
        )}

        {/* DOMAIN */}
        <select
          className="w-full mb-3 p-3 rounded-lg bg-white/80"
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
        >
          <option value="python">Python</option>
          <option value="javascript">JavaScript</option>
          <option value="react">React</option>
          <option value="dbms">DBMS</option>
          <option value="ml">AI/ML</option>
        </select>

        {/* BUTTON */}
        <button
          onClick={getQuestion}
          className="w-full bg-blue-600 text-white py-3 rounded-lg"
        >
          🎯 Start Interview
        </button>

        {/* QUESTION */}
        {questionData && (
          <div className="mt-5">

            <h3 className="text-white mb-3">
              {questionData.question}
            </h3>

            <textarea
              className="w-full p-3 rounded-lg"
              rows="4"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
            />

            {/* 🎤 */}
            <button
              onClick={startListening}
              className="mt-2 w-full bg-purple-600 text-white py-2 rounded"
            >
              🎤 Speak
            </button>

            {/* 📊 CONFIDENCE */}
            <p className="text-white mt-2">
              Confidence: <b>{confidence}</b>
            </p>

            <button
              onClick={submitAnswer}
              className="mt-3 w-full bg-green-600 text-white py-3 rounded"
            >
              Submit
            </button>
          </div>
        )}

        {/* RESULT */}
        {result && (
          <div className="mt-4 text-white">
            <p>Score: {result.score}/10</p>
            <p>{result.feedback}</p>
          </div>
        )}

      </div>
    </div>
  );
}