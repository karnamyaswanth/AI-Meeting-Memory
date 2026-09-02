import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function CreateMeeting() {
    const navigate = useNavigate();

    const [title, setTitle] = useState("");
    const [meetingDate, setMeetingDate] = useState("");
    const [participants, setParticipants] = useState("");
    const [description, setDescription] = useState("");

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const token = localStorage.getItem("token");

    const handleSubmit = async (e) => {
        e.preventDefault();

        setError("");

        if (!title || !meetingDate) {
            setError("Please enter the meeting title and date.");
            return;
        }

        if (!token) {
            navigate("/login");
            return;
        }

        try {
            setLoading(true);

            await axios.post(
                "http://127.0.0.1:8000/api/meetings",
                {
                    title: title,
                    meeting_date: meetingDate,
                    participants: participants,
                    description: description
                },
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            );

            alert("Meeting created successfully!");

            navigate("/dashboard");

        } catch (err) {
            console.error(err);

            if (err.response?.status === 401) {
                localStorage.removeItem("token");
                localStorage.removeItem("user");
                navigate("/login");
            } else {
                setError(
                    err.response?.data?.detail ||
                    "Failed to create meeting."
                );
            }

        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="create-meeting-page">

            <div className="create-meeting-container">

                <button
                    className="back-button"
                    onClick={() => navigate("/dashboard")}
                >
                    ← Back to Dashboard
                </button>

                <div className="form-header">

                    <h1>
                        ➕ Create Meeting
                    </h1>

                    <p>
                        Save important information about your meeting.
                    </p>

                </div>

                {error && (
                    <div className="error-message">
                        {error}
                    </div>
                )}

                <form onSubmit={handleSubmit}>

                    <div className="form-group">

                        <label>
                            Meeting Title
                        </label>

                        <input
                            type="text"
                            placeholder="Example: Project Discussion"
                            value={title}
                            onChange={(e) =>
                                setTitle(e.target.value)
                            }
                            required
                        />

                    </div>


                    <div className="form-group">

                        <label>
                            Meeting Date
                        </label>

                        <input
                            type="date"
                            value={meetingDate}
                            onChange={(e) =>
                                setMeetingDate(e.target.value)
                            }
                            required
                        />

                    </div>


                    <div className="form-group">

                        <label>
                            Participants
                        </label>

                        <input
                            type="text"
                            placeholder="Example: Reshu, Team Lead, Developer"
                            value={participants}
                            onChange={(e) =>
                                setParticipants(e.target.value)
                            }
                        />

                    </div>


                    <div className="form-group">

                        <label>
                            Meeting Description
                        </label>

                        <textarea
                            placeholder="Describe what was discussed in the meeting..."
                            value={description}
                            onChange={(e) =>
                                setDescription(e.target.value)
                            }
                            rows="6"
                        />

                    </div>


                    <button
                        type="submit"
                        className="primary-button create-button"
                        disabled={loading}
                    >
                        {loading
                            ? "Creating..."
                            : "Create Meeting"
                        }
                    </button>

                </form>

            </div>

        </div>
    );
}

export default CreateMeeting;