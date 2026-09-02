import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Signup() {
    const navigate = useNavigate();

    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleSignup = async (e) => {
        e.preventDefault();

        setError("");
        setLoading(true);

        try {
            const response = await fetch(
                "http://127.0.0.1:8000/api/auth/signup",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                        "Accept": "application/json"
                    },

                    body: JSON.stringify({
                        name: name,
                        email: email,
                        password: password
                    })
                }
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.detail ||
                    "Signup failed"
                );
            }

            alert(
                "Account created successfully! Please login."
            );

            navigate("/login");

        } catch (error) {

            console.error(
                "Signup error:",
                error
            );

            setError(
                error.message ||
                "Unable to connect to server."
            );

        } finally {

            setLoading(false);
        }
    };

    return (
        <div
            style={{
                minHeight: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                background: "#f5f7fb",
                fontFamily: "Arial"
            }}
        >

            <div
                style={{
                    width: "400px",
                    background: "white",
                    padding: "35px",
                    borderRadius: "15px",
                    boxShadow:
                        "0 5px 25px rgba(0,0,0,0.1)"
                }}
            >

                <h1>
                    🤖 AI Meeting Memory
                </h1>

                <h2>
                    Create your account
                </h2>

                <form onSubmit={handleSignup}>

                    <label>
                        Name
                    </label>

                    <input
                        type="text"
                        value={name}
                        onChange={(e) =>
                            setName(e.target.value)
                        }
                        placeholder="Enter your name"
                        required
                        style={inputStyle}
                    />


                    <label>
                        Email
                    </label>

                    <input
                        type="email"
                        value={email}
                        onChange={(e) =>
                            setEmail(e.target.value)
                        }
                        placeholder="Enter your email"
                        required
                        style={inputStyle}
                    />


                    <label>
                        Password
                    </label>

                    <input
                        type="password"
                        value={password}
                        onChange={(e) =>
                            setPassword(e.target.value)
                        }
                        placeholder="Enter your password"
                        required
                        minLength="6"
                        style={inputStyle}
                    />


                    {error && (
                        <p
                            style={{
                                color: "red",
                                marginTop: "15px"
                            }}
                        >
                            ❌ {error}
                        </p>
                    )}


                    <button
                        type="submit"
                        disabled={loading}
                        style={{
                            width: "100%",
                            padding: "12px",
                            marginTop: "20px",
                            border: "none",
                            borderRadius: "8px",
                            cursor: loading
                                ? "not-allowed"
                                : "pointer"
                        }}
                    >

                        {loading
                            ? "Creating Account..."
                            : "Create Account"
                        }

                    </button>

                </form>


                <p
                    style={{
                        marginTop: "20px"
                    }}
                >
                    Already have an account?{" "}

                    <Link to="/login">
                        Login
                    </Link>

                </p>

            </div>

        </div>
    );
}


const inputStyle = {
    width: "100%",
    padding: "10px",
    marginTop: "7px",
    marginBottom: "15px",
    boxSizing: "border-box",
    border: "1px solid #ccc",
    borderRadius: "7px"
};


export default Signup;