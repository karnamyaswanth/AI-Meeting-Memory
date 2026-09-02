import os
import whisper
import imageio_ffmpeg


# ============================================================
# SETUP FFMPEG
# ============================================================

FFMPEG_PATH = imageio_ffmpeg.get_ffmpeg_exe()

print("FFmpeg found at:")
print(FFMPEG_PATH)

# Put FFmpeg folder into PATH
ffmpeg_folder = os.path.dirname(FFMPEG_PATH)

os.environ["PATH"] = (
    ffmpeg_folder
    + os.pathsep
    + os.environ.get("PATH", "")
)


# ============================================================
# LOAD WHISPER
# ============================================================

print("\nLoading Whisper model...")

model = whisper.load_model("base")

print("Whisper model loaded successfully!")


# ============================================================
# TRANSCRIPTION FUNCTION
# ============================================================

def transcribe_audio(audio_path):

    if not os.path.isfile(audio_path):

        raise FileNotFoundError(
            f"Audio file not found: {audio_path}"
        )

    print("\nTranscribing:")
    print(audio_path)

    # Convert path to absolute path
    audio_path = os.path.abspath(audio_path)

    print("\nAbsolute path:")
    print(audio_path)

    # Whisper transcription
    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["text"].strip()


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("\n")
    print("==========================================")
    print("          AI MEETING MEMORY")
    print("          DEEP LEARNING")
    print("          SPEECH RECOGNITION")
    print("==========================================")

    audio_file = input(
        "\nEnter the path of your audio file: "
    ).strip()

    try:

        transcript = transcribe_audio(
            audio_file
        )

        print("\n")
        print("==========================================")
        print("              TRANSCRIPT")
        print("==========================================")
        print()

        print(transcript)

        print()
        print("==========================================")

    except Exception as error:

        print("\n")
        print("==========================================")
        print("                  ERROR")
        print("==========================================")
        print()

        print(type(error).__name__)
        print(error)

        print()