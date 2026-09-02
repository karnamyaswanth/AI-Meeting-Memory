import { useState } from "react";

function Dashboard() {

    const [file, setFile] = useState(null);

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState(null);

    const [error, setError] = useState("");

    const handleFileChange = (event) => {

        setFile(event.target.files[0]);

        setError("");

        setResult(null);
    };


    const processMeeting = async () => {

        if (!file) {

            setError(
                "Please select an audio file first."
            );

            return;
        }

        setLoading(true);

        setError("");

        setResult(null);

        const formData = new FormData();

        formData.append(
            "file",
            file
        );

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/api/ai/process",
                {
                    method: "POST",
                    body: formData
                }
            );

            const data = await response.json();

            if (!response.ok) {

                throw new Error(
                    data.detail ||
                    "Meeting processing failed"
                );
            }

            setResult(data);

        } catch (error) {

            setError(
                error.message
            );

        } finally {

            setLoading(false);
        }
    };


    return (

        <div
            style={{
                minHeight: "100vh",
                background: "#f5f7fb",
                padding: "40px",
                fontFamily: "Arial"
            }}
        >

            <div
                style={{
                    maxWidth: "1000px",
                    margin: "auto"
                }}
            >

                <h1>
                    🤖 AI Meeting Memory
                </h1>

                <p>
                    Upload a meeting recording and let AI
                    remember everything.
                </p>


                {/* Upload */}

                <div
                    style={{
                        background: "white",
                        padding: "30px",
                        borderRadius: "15px",
                        marginTop: "30px"
                    }}
                >

                    <h2>
                        🎙️ Upload Meeting Recording
                    </h2>

                    <input
                        type="file"
                        accept=".wav,.mp3,.m4a,.ogg,.flac"
                        onChange={handleFileChange}
                    />

                    <br />
                    <br />

                    <button
                        onClick={processMeeting}
                        disabled={loading}
                        style={{
                            padding: "12px 25px",
                            border: "none",
                            borderRadius: "8px",
                            cursor: "pointer"
                        }}
                    >

                        {loading
                            ? "🤖 AI Processing..."
                            : "🚀 Process Meeting"
                        }

                    </button>


                    {file && (

                        <p>
                            Selected: <b>{file.name}</b>
                        </p>

                    )}


                    {error && (

                        <p>
                            ❌ {error}
                        </p>

                    )}

                </div>


                {/* Results */}

                {result && (

                    <div
                        style={{
                            marginTop: "30px"
                        }}
                    >

                        {/* Summary */}

                        <div
                            style={{
                                background: "white",
                                padding: "25px",
                                borderRadius: "15px",
                                marginBottom: "20px"
                            }}
                        >

                            <h2>
                                🧠 AI Summary
                            </h2>

                            <p>
                                {result.summary}
                            </p>

                        </div>


                        {/* Transcript */}

                        <div
                            style={{
                                background: "white",
                                padding: "25px",
                                borderRadius: "15px",
                                marginBottom: "20px"
                            }}
                        >

                            <h2>
                                📝 Transcript
                            </h2>

                            <p>
                                {result.transcript}
                            </p>

                        </div>


                        {/* Action Items */}

                        <div
                            style={{
                                background: "white",
                                padding: "25px",
                                borderRadius: "15px",
                                marginBottom: "20px"
                            }}
                        >

                            <h2>
                                ✅ Action Items
                            </h2>

                            {result.action_items.length === 0 ? (

                                <p>
                                    No action items detected.
                                </p>

                            ) : (

                                <ul>

                                    {result.action_items.map(
                                        (item, index) => (

                                            <li key={index}>
                                                {item}
                                            </li>

                                        )
                                    )}

                                </ul>

                            )}

                        </div>


                        {/* Decisions */}

                        <div
                            style={{
                                background: "white",
                                padding: "25px",
                                borderRadius: "15px"
                            }}
                        >

                            <h2>
                                🧠 Decisions
                            </h2>

                            {result.decisions.length === 0 ? (

                                <p>
                                    No decisions detected.
                                </p>

                            ) : (

                                <ul>

                                    {result.decisions.map(
                                        (decision, index) => (

                                            <li key={index}>
                                                {decision}
                                            </li>

                                        )
                                    )}

                                </ul>

                            )}

                        </div>

                    </div>

                )}

            </div>

        </div>
    );
}

export default Dashboard;