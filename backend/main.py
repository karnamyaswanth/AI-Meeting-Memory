import os
import sys
import shutil
from datetime import datetime

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware


# =========================================================
# PATH CONFIGURATION
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

AI_DIR = os.path.join(BASE_DIR, "ai")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

# Add AI folder to Python path
if AI_DIR not in sys.path:
    sys.path.insert(0, AI_DIR)


# =========================================================
# FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="AI Meeting Memory API",
    description="AI-powered meeting transcription, summarization and NLP analysis",
    version="1.0.0"
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# AI PIPELINE
# =========================================================

AI_AVAILABLE = False

transcribe_audio = None
generate_summary = None
classify_sentences = None


try:

    from meeting_ai import (
        transcribe_audio,
        generate_summary,
        classify_sentences
    )

    AI_AVAILABLE = True

    print("=" * 60)
    print("MEETING AI PIPELINE LOADED SUCCESSFULLY")
    print("=" * 60)

except Exception as e:

    print("=" * 60)
    print("AI PIPELINE IMPORT ERROR")
    print("=" * 60)
    print(str(e))
    print("=" * 60)

    AI_AVAILABLE = False


# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get("/")
def root():

    return {
        "message": "AI Meeting Memory API is running",
        "status": "success",
        "version": "1.0.0",
        "ai_available": AI_AVAILABLE
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/api/health")
def health():

    ffmpeg_available = False

    try:

        import imageio_ffmpeg

        ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

        if os.path.exists(ffmpeg_path):
            ffmpeg_available = True

    except Exception:
        ffmpeg_available = False


    return {
        "status": "healthy",
        "ffmpeg": ffmpeg_available,
        "ai_module": AI_AVAILABLE
    }


# =========================================================
# PROCESS MEETING
# =========================================================

@app.post("/api/ai/process")
async def process_meeting(
    file: UploadFile = File(...)
):

    # -----------------------------------------------------
    # Check AI
    # -----------------------------------------------------

    if not AI_AVAILABLE:

        raise HTTPException(
            status_code=500,
            detail="AI pipeline could not be loaded."
        )


    # -----------------------------------------------------
    # Check file
    # -----------------------------------------------------

    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="No audio file selected."
        )


    # -----------------------------------------------------
    # Supported formats
    # -----------------------------------------------------

    allowed_extensions = {
        ".wav",
        ".mp3",
        ".m4a",
        ".ogg",
        ".flac"
    }


    extension = os.path.splitext(
        file.filename
    )[1].lower()


    if extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported audio format. "
                "Supported formats: WAV, MP3, M4A, OGG, FLAC."
            )
        )


    # -----------------------------------------------------
    # Create uploads folder
    # -----------------------------------------------------

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )


    # -----------------------------------------------------
    # Generate unique filename
    # -----------------------------------------------------

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S_%f"
    )


    safe_filename = (
        f"meeting_{timestamp}{extension}"
    )


    audio_path = os.path.join(
        UPLOAD_DIR,
        safe_filename
    )


    # -----------------------------------------------------
    # Save uploaded audio
    # -----------------------------------------------------

    try:

        with open(
            audio_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Could not save audio file: {str(e)}"
        )


    # -----------------------------------------------------
    # AI PROCESSING
    # -----------------------------------------------------

    try:

        print()
        print("=" * 60)
        print("PROCESSING MEETING")
        print("=" * 60)

        print()
        print("Audio:")
        print(audio_path)

        # =================================================
        # STEP 1 - TRANSCRIPTION
        # =================================================

        print()
        print("1. Transcribing audio...")

        transcript = transcribe_audio(
            audio_path
        )


        if not transcript:

            transcript = "No transcript generated."


        print("Transcription completed.")


        # =================================================
        # STEP 2 - SUMMARY
        # =================================================

        print()
        print("2. Generating AI summary...")

        summary = generate_summary(
            transcript
        )


        if not summary:

            summary = "No summary generated."


        print("Summary generated.")


        # =================================================
        # STEP 3 - ACTION ITEMS + DECISIONS
        # =================================================

        print()
        print("3. Detecting action items and decisions...")

        action_items, decisions = classify_sentences(
            transcript
        )


        if action_items is None:
            action_items = []


        if decisions is None:
            decisions = []


        print("NLP analysis completed.")


        # =================================================
        # SAVE RESULT
        # =================================================

        output_dir = os.path.join(
            BASE_DIR,
            "output"
        )


        os.makedirs(
            output_dir,
            exist_ok=True
        )


        result_filename = (
            f"meeting_{timestamp}_result.txt"
        )


        result_path = os.path.join(
            output_dir,
            result_filename
        )


        with open(
            result_path,
            "w",
            encoding="utf-8"
        ) as result_file:

            result_file.write(
                "AI MEETING MEMORY\n"
            )

            result_file.write(
                "=" * 60 + "\n\n"
            )


            result_file.write(
                "FILE\n"
            )

            result_file.write(
                f"{file.filename}\n\n"
            )


            result_file.write(
                "TRANSCRIPT\n"
            )

            result_file.write(
                f"{transcript}\n\n"
            )


            result_file.write(
                "AI SUMMARY\n"
            )

            result_file.write(
                f"{summary}\n\n"
            )


            result_file.write(
                "ACTION ITEMS\n"
            )

            if action_items:

                for index, item in enumerate(
                    action_items,
                    start=1
                ):

                    result_file.write(
                        f"{index}. {item}\n"
                    )

            else:

                result_file.write(
                    "No action items detected.\n"
                )


            result_file.write("\n")


            result_file.write(
                "DECISIONS\n"
            )

            if decisions:

                for index, decision in enumerate(
                    decisions,
                    start=1
                ):

                    result_file.write(
                        f"{index}. {decision}\n"
                    )

            else:

                result_file.write(
                    "No decisions detected.\n"
                )


        # =================================================
        # SUCCESS RESPONSE
        # =================================================

        print()
        print("=" * 60)
        print("MEETING PROCESSED SUCCESSFULLY")
        print("=" * 60)


        return {

            "success": True,

            "message": (
                "Meeting processed successfully"
            ),

            "filename": file.filename,

            "saved_audio": audio_path,

            "transcript": transcript,

            "summary": summary,

            "action_items": action_items,

            "decisions": decisions,

            "output_file": result_path
        }


    # -----------------------------------------------------
    # AI ERROR
    # -----------------------------------------------------

    except Exception as e:

        print()
        print("=" * 60)
        print("AI PROCESSING ERROR")
        print("=" * 60)
        print(str(e))
        print("=" * 60)


        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================================================
# RUN DIRECTLY
# =========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )