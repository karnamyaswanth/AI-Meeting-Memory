import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [history, setHistory] = useState([]);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];

    if (!selectedFile) {
      return;
    }

    setFile(selectedFile);
    setResult(null);
    setError("");
  };

  const processMeeting = async () => {
    if (!file) {
      setError("Please select an audio file first.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(
        `${API_URL}/api/ai/process`,
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Meeting processing failed."
        );
      }

      setResult(data);

      const meeting = {
        id: Date.now(),
        filename: data.filename || file.name,
        processedAt: new Date().toLocaleString(),
        summary: data.summary || "No summary available.",
        transcript: data.transcript || "",
        actionItems: data.action_items || [],
        decisions: data.decisions || [],
        savedAudio: data.saved_audio || "",
      };

      setHistory((previous) => [
        meeting,
        ...previous,
      ]);
    } catch (err) {
      setError(
        err.message ||
          "Unable to connect to the AI backend."
      );
    } finally {
      setLoading(false);
    }
  };

  const clearResults = () => {
    setResult(null);
    setFile(null);
    setError("");
  };

  return (
    <div className="app">

      {/* HEADER */}
      <header className="header">
        <div>
          <h1>🤖 AI Meeting Memory</h1>

          <p>
            Transform meeting recordings into intelligent,
            searchable insights.
          </p>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          AI System Online
        </div>
      </header>

      {/* MAIN */}
      <main className="container">

        {/* UPLOAD CARD */}
        <section className="upload-card">

          <div className="upload-icon">
            🎙️
          </div>

          <h2>
            Upload Meeting Recording
          </h2>

          <p>
            Upload an audio recording and let AI analyze
            your meeting automatically.
          </p>

          <label className="file-input">

            <input
              type="file"
              accept="audio/*"
              onChange={handleFileChange}
            />

            <span>
              {file
                ? `🎵 ${file.name}`
                : "Choose Audio File"}
            </span>

          </label>

          {file && (
            <div className="file-info">
              <strong>Selected:</strong>{" "}
              {file.name}
            </div>
          )}

          <button
            className="process-button"
            onClick={processMeeting}
            disabled={loading || !file}
          >
            {loading
              ? "⏳ Processing Meeting..."
              : "🚀 Process Meeting"}
          </button>

          {/* LOADING */}
          {loading && (
            <div className="loading-box">

              <div className="spinner"></div>

              <p>
                AI is analyzing your meeting...
              </p>

              <small>
                Whisper is transcribing the audio and
                generating intelligent insights.
              </small>

            </div>
          )}

          {/* ERROR */}
          {error && (
            <div className="error-box">
              ❌ {error}
            </div>
          )}

          {/* SUCCESS */}
          {result && (
            <div className="success-box">
              ✅ Meeting processed successfully!
            </div>
          )}

        </section>

        {/* RESULTS */}
        {result && (
          <section className="results-section">

            {/* SUMMARY */}
            <div className="result-card summary-card">

              <div className="result-title">
                <span>🧠</span>

                <h2>
                  AI Summary
                </h2>
              </div>

              <p>
                {result.summary ||
                  "No summary available."}
              </p>

            </div>

            {/* TRANSCRIPT */}
            <div className="result-card">

              <div className="result-title">
                <span>📝</span>

                <h2>
                  Transcript
                </h2>
              </div>

              <div className="transcript-box">
                {result.transcript ||
                  "No transcript available."}
              </div>

            </div>

            {/* ACTION ITEMS */}
            <div className="result-card">

              <div className="result-title">
                <span>✅</span>

                <h2>
                  Action Items
                </h2>
              </div>

              {result.action_items &&
              result.action_items.length > 0 ? (

                <div className="action-list">

                  {result.action_items.map(
                    (item, index) => (

                      <div
                        className="action-item"
                        key={index}
                      >

                        <span className="number">
                          {index + 1}
                        </span>

                        <span>
                          {item}
                        </span>

                      </div>

                    )
                  )}

                </div>

              ) : (

                <p className="empty-message">
                  No action items detected.
                </p>

              )}

            </div>

            {/* DECISIONS */}
            <div className="result-card">

              <div className="result-title">
                <span>💡</span>

                <h2>
                  Decisions
                </h2>
              </div>

              {result.decisions &&
              result.decisions.length > 0 ? (

                <div className="decision-list">

                  {result.decisions.map(
                    (decision, index) => (

                      <div
                        className="decision-item"
                        key={index}
                      >

                        <span className="number">
                          {index + 1}
                        </span>

                        <span>
                          {decision}
                        </span>

                      </div>

                    )
                  )}

                </div>

              ) : (

                <p className="empty-message">
                  No decisions detected.
                </p>

              )}

            </div>

            {/* MEETING INFORMATION */}
            <div className="result-card">

              <div className="result-title">
                <span>📁</span>

                <h2>
                  Meeting Information
                </h2>
              </div>

              <div className="meeting-info">

                <p>
                  <strong>File:</strong>{" "}
                  {result.filename ||
                    file?.name ||
                    "Unknown"}
                </p>

                <p>
                  <strong>Saved Audio:</strong>{" "}
                  {result.saved_audio ||
                    "Not available"}
                </p>

                <p>
                  <strong>Result:</strong>{" "}
                  {result.output_file ||
                    "Processed successfully"}
                </p>

              </div>

            </div>

            {/* PROCESS ANOTHER */}
            <button
              className="clear-button"
              onClick={clearResults}
            >
              🔄 Process Another Meeting
            </button>

          </section>
        )}

        {/* MEETING HISTORY */}
        <section className="history-section">

          <div className="history-header">

            <div>
              <h2>
                📚 Meeting History
              </h2>

              <p>
                Meetings processed during this session.
              </p>
            </div>

            <span className="history-count">
              {history.length}
            </span>

          </div>

          {history.length === 0 ? (

            <div className="empty-history">

              <div>
                📂
              </div>

              <p>
                No meetings processed yet.
              </p>

              <small>
                Upload an audio recording to create
                your first meeting memory.
              </small>

            </div>

          ) : (

            <div className="history-list">

              {history.map((meeting) => (

                <div
                  className="history-card"
                  key={meeting.id}
                >

                  <div className="history-icon">
                    🎵
                  </div>

                  <div className="history-content">

                    <h3>
                      {meeting.filename}
                    </h3>

                    <span className="history-date">
                      {meeting.processedAt}
                    </span>

                    <p>
                      {meeting.summary}
                    </p>

                    <div className="history-stats">

                      <span>
                        📝 Transcript
                      </span>

                      <span>
                        ✅{" "}
                        {meeting.actionItems.length}{" "}
                        Actions
                      </span>

                      <span>
                        💡{" "}
                        {meeting.decisions.length}{" "}
                        Decisions
                      </span>

                    </div>

                  </div>

                </div>

              ))}

            </div>

          )}

        </section>

      </main>

      {/* FOOTER */}
      <footer>

        <p>
          AI Meeting Memory • Powered by Whisper,
          Transformers & FastAPI
        </p>

      </footer>

    </div>
  );
}

export default App;