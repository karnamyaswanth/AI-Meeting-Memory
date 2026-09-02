# 🧠 AI Meeting Memory

AI Meeting Memory is a full-stack Artificial Intelligence application that transforms meeting recordings into intelligent, searchable insights.

Upload a meeting recording and the system automatically generates a transcript, AI summary, action items, and detected decisions.

## 🚀 Features

- 🎙️ Upload meeting recordings
- 📝 Automatic speech-to-text transcription
- 🧠 AI-powered meeting summarization
- ✅ Automatic action-item extraction
- 💡 Decision detection
- 📁 Meeting audio storage
- ⚡ FastAPI backend
- ⚛️ React frontend
- 🔄 REST API integration
- 📚 Swagger API documentation
- 🎨 Responsive web interface
- 🎵 Multiple audio format support

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- React.js
- Vite
- JavaScript
- HTML5
- CSS3
- OpenAI Whisper
- Hugging Face Transformers
- DistilBART
- Natural Language Processing
- FFmpeg
- imageio-ffmpeg

## 🏗️ Architecture

User → React Frontend → FastAPI Backend → FFmpeg → Whisper → Transcript → AI Summarization → Action Item & Decision Detection → React Dashboard

## 📂 Project Structure

AI-Meeting-Memory/
├── ai/
│   └── meeting_ai.py
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   └── ...
├── uploads/
├── output/
├── .gitignore
└── README.md

## ⚙️ Installation

### Clone the Repository

    git clone https://github.com/karnamyaswanth/AI-Meeting-Memory.git
    cd AI-Meeting-Memory

### Backend Setup

    cd backend
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt

If PowerShell blocks activation:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    .\venv\Scripts\Activate.ps1

### Start Backend

    cd D:\AI-Meeting-Memory\backend
    .\venv\Scripts\Activate.ps1
    python -m uvicorn main:app --reload

Backend URL:

http://127.0.0.1:8000

### Swagger API Documentation

Open:

http://127.0.0.1:8000/docs

## 💻 Frontend Setup

Open another PowerShell terminal:

    cd D:\AI-Meeting-Memory\frontend
    npm install
    npm run dev

Vite normally runs at:

http://localhost:5173

Open the URL displayed by Vite in your browser.

## 🎙️ How to Use

1. Start the FastAPI backend.
2. Start the React frontend.
3. Open the frontend URL.
4. Click "Choose Audio File".
5. Select a meeting recording.
6. Click "Process Meeting".
7. Wait while Whisper transcribes the recording.
8. The AI system generates the meeting summary.
9. The application extracts action items and decisions.
10. The results are displayed on the dashboard.

## 🔌 API Endpoints

GET /
GET /api/health
POST /api/ai/process

## 📡 Process Meeting API

Endpoint:

POST http://127.0.0.1:8000/api/ai/process

The endpoint accepts an audio file using multipart/form-data.

Example request:

    curl -X POST "http://127.0.0.1:8000/api/ai/process" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@meeting.wav;type=audio/wav"

## 📥 Example Response

    {
      "success": true,
      "filename": "meeting.wav",
      "saved_audio": "D:\\AI-Meeting-Memory\\uploads\\meeting.wav",
      "transcript": "Today we discussed the AI Meeting Memory Project. The team will test the back-end API tomorrow.",
      "summary": "Today we discussed the AI Meeting Memory Project and planned testing of the back-end API.",
      "action_items": [
        "Complete the Front-End dashboard.",
        "Test the back-end API tomorrow."
      ],
      "decisions": [],
      "output_file": ""
    }

## 🧠 AI Pipeline

Meeting Audio
↓
FFmpeg Audio Processing
↓
Whisper Speech Recognition
↓
Speech-to-Text Transcript
↓
Transformer Summarization
↓
AI Meeting Summary
↓
Sentence Classification
↓
Action Items + Decisions
↓
React Dashboard

## 🔍 Health Check

Endpoint:

GET /api/health

Example response:

    {
      "status": "healthy",
      "ffmpeg": true,
      "ai_module": true
    }

## 🎵 Supported Audio Formats

- WAV
- MP3
- M4A
- OGG
- FLAC

## 📊 Example Output

### AI Summary

Today we discussed the AI Meeting Memory Project. The team will test the back-end API tomorrow. We also discussed automatic meeting summaries and action items.

### Transcript

Today we discussed the AI Meeting Memory Project. Re-Show will complete the Front-End dashboard. The team will test the back-end API tomorrow. We also discussed automatic meeting summaries and action items.

### Action Items

1. Re-Show will complete the Front-End dashboard.
2. The team will test the back-end API tomorrow.

### Decisions

No decisions detected.

## 📁 Generated Files

During local execution, meeting recordings and generated results may be stored in:

- uploads/
- output/

These files should not be uploaded to GitHub.

## 🚫 Files to Exclude from GitHub

The following should be included in .gitignore:

venv/
ai/venv/
backend/venv/
frontend/node_modules/
__pycache__/
*.pyc
uploads/
output/
*.wav
*.mp3
*.m4a
*.ogg
*.flac
*.dll
*.exe
*.bin
*.pt
*.pth
*.safetensors
.env

## 🔐 Security

Do not upload API keys, passwords, authentication tokens, private credentials, or .env files to GitHub.

## 🎯 Project Objective

The objective of AI Meeting Memory is to automatically convert unstructured meeting recordings into structured and useful information.

Instead of manually listening to an entire meeting recording, users can upload the recording and receive:

Meeting Recording → Transcript → Summary → Action Items → Decisions

This makes meeting information easier to understand and helps users identify important tasks quickly.

# 🤖 AI Meeting Memory

Transform meeting recordings into intelligent, searchable insights.

## 📸 Application Screenshot

<img width="905" height="515" alt="Screenshot 2026-09-01 171428" src="https://github.com/user-attachments/assets/ae9aa6f8-772e-40ca-9043-06ca887de3ea" />


## 🌟 Key Highlights

- Full-Stack AI Application
- Speech Recognition
- Natural Language Processing
- Automatic Summarization
- Action Item Extraction
- Decision Detection
- React Frontend
- FastAPI Backend
- REST API
- FFmpeg Integration
- Whisper Integration
- Hugging Face Transformers

## 🔮 Future Enhancements

- Search previous meetings
- Meeting history
- Speaker identification
- Speaker-wise transcription
- User authentication
- Database integration
- Meeting analytics
- PDF report generation
- Action-item reminders
- Improved decision detection
- Cloud deployment
- Mobile-friendly interface

## 🎓 Educational Purpose

This project demonstrates the integration of Artificial Intelligence, Speech Recognition, Natural Language Processing, Machine Learning, React, FastAPI, REST APIs, and audio processing into a practical full-stack application.

## 👨‍💻 Author

Karnam Yaswanth

GitHub: https://github.com/karnamyaswanth

## 📌 Repository

AI Meeting Memory:
https://github.com/karnamyaswanth/AI-Meeting-Memory

## ⭐ Support

If you find this project useful, please give the repository a ⭐ on GitHub.

## 📜 License

This project is created for educational and project demonstration purposes.
