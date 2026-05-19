import { useState } from "react";
import API from "../services/api";

export default function InterviewPDF() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState("");
  const [score, setScore] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [listening, setListening] = useState(false);
  const [recognitionInstance, setRecognitionInstance] = useState(null);

  // 🔊 AI बोले question
  const speakQuestion = (text) => {
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US";
    speech.rate = 0.9;

    window.speechSynthesis.cancel(); // stop previous
    window.speechSynthesis.speak(speech);
  };

  // 🎤 START LISTENING (NO DUPLICATION)
  const startListening = () => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Speech Recognition not supported");
      return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.continuous = true;
    recognition.interimResults = true;

    setListening(true);

    let finalTranscript = "";

    recognition.start();

    recognition.onresult = (event) => {
      let interimTranscript = "";

      for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcript = event.results[i][0].transcript;

        if (event.results[i].isFinal) {
          finalTranscript += transcript + " ";
        } else {
          interimTranscript += transcript;
        }
      }

      setAnswer(finalTranscript + interimTranscript); // ✅ no duplicate
    };

    recognition.onerror = () => {
      setListening(false);
    };

    recognition.onend = () => {
      setListening(false);
    };

    setRecognitionInstance(recognition);
  };

  // ⏹ STOP
  const stopListening = () => {
    if (recognitionInstance) {
      recognitionInstance.stop();
      setListening(false);
    }
  };

  // 📄 Upload PDF
  const uploadPDF = async () => {
    if (!file) {
      setError("Please select a PDF file first");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const formData = new FormData();
      formData.append("file", file);

      await API.post("/pdf-question-bank", formData);

      const res = await API.get("/next-question");

      const q = res.data.question || "No question found";
      setQuestion(q);

      speakQuestion(q); // 🔥 AI बोलेगा

    } catch (err) {
      setError("Error uploading PDF");
    } finally {
      setLoading(false);
    }
  };

  // 🎤 Submit Answer
  const submitAnswer = async () => {
    if (!answer) {
      setError("Please enter your answer");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const res = await API.post(
        `/submit-pdf-answer?answer=${encodeURIComponent(answer)}`
      );

      setScore(res.data.score);
      setFeedback(res.data.feedback);

      if (res.data.next_question) {
        const nextQ = res.data.next_question;

        setQuestion(nextQ);
        setAnswer("");

        speakQuestion(nextQ); // 🔥 next question बोलेगा

      } else {
        setQuestion("🎉 Interview Finished");
        speakQuestion("Interview Finished");
        setAnswer("");
      }

    } catch (err) {
      setError("Error submitting answer");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 text-white min-h-screen bg-black">

      <h1 className="text-3xl mb-6 text-center">📄 PDF Interview</h1>

      {error && (
        <p className="text-red-400 text-center mb-4">{error}</p>
      )}

      {/* Upload */}
      <div className="flex gap-2 justify-center">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button
          onClick={uploadPDF}
          disabled={loading}
          className="bg-blue-500 px-4 py-2 rounded"
        >
          {loading ? "Uploading..." : "Upload PDF"}
        </button>
      </div>

      {/* Question */}
      {question && (
        <div className="mt-8 max-w-2xl mx-auto">

          <h2 className="text-xl mb-4 bg-gray-800 p-4 rounded">
            ❓ {question}
          </h2>

          {/* 🔊 Repeat */}
          <button
            onClick={() => speakQuestion(question)}
            className="bg-yellow-500 px-3 py-2 w-full mb-2"
          >
            🔊 Repeat Question
          </button>

          <textarea
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            className="w-full p-3 text-black rounded"
            rows={5}
            placeholder="Type or speak your answer..."
          />

          {/* 🎤 Voice */}
          <div className="flex gap-2 mt-2">
            <button
              onClick={startListening}
              className="bg-purple-500 px-4 py-2 w-full"
            >
              🎤 Start
            </button>

            <button
              onClick={stopListening}
              className="bg-red-500 px-4 py-2 w-full"
            >
              ⏹ Stop
            </button>
          </div>

          {/* Submit */}
          <button
            onClick={submitAnswer}
            className="bg-green-500 px-4 py-2 mt-3 w-full"
          >
            Submit Answer
          </button>
        </div>
      )}

      {/* Result */}
      {score !== null && (
        <div className="mt-6 text-center">
          <p className="text-yellow-400 text-lg">⭐ Score: {score}</p>
          <p className="text-gray-300 mt-2">💬 {feedback}</p>
        </div>
      )}

    </div>
  );
}