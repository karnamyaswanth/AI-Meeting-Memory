import os
import sys
import re

# =========================================================
# AI MEETING MEMORY
# DEEP LEARNING PIPELINE
# =========================================================

print("\n==========================================")
print("       AI MEETING MEMORY")
print("       DEEP LEARNING PIPELINE")
print("==========================================\n")


# =========================================================
# FFMPEG
# =========================================================

try:
    import imageio_ffmpeg

    FFMPEG_PATH = imageio_ffmpeg.get_ffmpeg_exe()

    os.environ["PATH"] = (
        os.path.dirname(FFMPEG_PATH)
        + os.pathsep
        + os.environ.get("PATH", "")
    )

    print("FFmpeg found:")
    print(FFMPEG_PATH)

except Exception as e:
    print("FFmpeg error:", e)
    FFMPEG_PATH = None


# =========================================================
# WHISPER
# =========================================================

print("\n==========================================")
print("       LOADING WHISPER MODEL")
print("==========================================")

try:
    import whisper

    whisper_model = whisper.load_model("tiny")

    print("Whisper model loaded successfully!")

except Exception as e:
    print("Whisper error:", e)
    whisper_model = None


# =========================================================
# LIGHTWEIGHT SUMMARY
# =========================================================

print("\n==========================================")
print("       LOADING SUMMARY SYSTEM")
print("==========================================")

print("Lightweight summary system ready!")


# =========================================================
# TRANSCRIPTION
# =========================================================

def transcribe_audio(audio_path):

    if whisper_model is None:
        raise RuntimeError(
            "Whisper model could not be loaded."
        )

    if not os.path.exists(audio_path):
        raise FileNotFoundError(
            f"Audio file not found: {audio_path}"
        )

    print("\nTranscribing audio...")

    result = whisper_model.transcribe(
        audio_path,
        fp16=False
    )

    transcript = result.get(
        "text",
        ""
    ).strip()

    if not transcript:
        raise RuntimeError(
            "No speech detected."
        )

    return transcript


# =========================================================
# SENTENCE SPLITTER
# =========================================================

def split_sentences(text):

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text.strip()
    )

    return [
        s.strip()
        for s in sentences
        if s.strip()
    ]


# =========================================================
# LIGHTWEIGHT AI SUMMARY
# =========================================================

def generate_summary(transcript):

    if not transcript:
        return "No summary available."

    sentences = split_sentences(
        transcript
    )

    if len(sentences) <= 3:
        return " ".join(sentences)

    # Select important sentences based on
    # meeting-related keywords.

    keywords = [
        "discussed",
        "project",
        "complete",
        "test",
        "meeting",
        "decision",
        "agreed",
        "action",
        "important",
        "tomorrow",
        "deadline",
        "develop",
        "implement"
    ]

    scored = []

    for index, sentence in enumerate(sentences):

        score = 0

        lower = sentence.lower()

        for keyword in keywords:

            if keyword in lower:
                score += 1

        # Slight preference for early sentences
        score += max(
            0,
            3 - index
        )

        scored.append(
            (score, index, sentence)
        )

    scored.sort(
        reverse=True
    )

    selected = sorted(
        scored[:3],
        key=lambda x: x[1]
    )

    summary = " ".join(
        item[2]
        for item in selected
    )

    return summary


# =========================================================
# ACTION ITEM DETECTION
# =========================================================

def detect_action_items(transcript):

    sentences = split_sentences(
        transcript
    )

    keywords = [
        "will",
        "should",
        "need to",
        "needs to",
        "must",
        "complete",
        "finish",
        "test",
        "prepare",
        "develop",
        "create",
        "implement",
        "submit",
        "update",
        "review",
        "check",
        "tomorrow",
        "deadline"
    ]

    action_items = []

    for sentence in sentences:

        lower = sentence.lower()

        if any(
            keyword in lower
            for keyword in keywords
        ):

            if sentence not in action_items:
                action_items.append(sentence)

    return action_items


# =========================================================
# DECISION DETECTION
# =========================================================

def detect_decisions(transcript):

    sentences = split_sentences(
        transcript
    )

    keywords = [
        "decided",
        "decision",
        "agreed",
        "we agreed",
        "approved",
        "selected",
        "choose",
        "chosen",
        "will use",
        "we will use",
        "plan to use"
    ]

    decisions = []

    for sentence in sentences:

        lower = sentence.lower()

        if any(
            keyword in lower
            for keyword in keywords
        ):

            if sentence not in decisions:
                decisions.append(sentence)

    return decisions


# =========================================================
# CLASSIFY SENTENCES
# =========================================================

def classify_sentences(transcript):

    action_items = detect_action_items(
        transcript
    )

    decisions = detect_decisions(
        transcript
    )

    return (
        action_items,
        decisions
    )


# =========================================================
# COMPLETE MEETING PROCESSOR
# =========================================================

def process_meeting(audio_path):

    print("\n==========================================")
    print("       PROCESSING MEETING")
    print("==========================================")

    # STEP 1
    transcript = transcribe_audio(
        audio_path
    )

    print("\n==========================================")
    print("              TRANSCRIPT")
    print("==========================================")

    print(transcript)

    # STEP 2
    print("\nGenerating AI summary...")

    summary = generate_summary(
        transcript
    )

    print("\n==========================================")
    print("              AI SUMMARY")
    print("==========================================")

    print(summary)

    # STEP 3
    print("\nAnalyzing action items...")

    action_items = detect_action_items(
        transcript
    )

    print("\n==========================================")
    print("             ACTION ITEMS")
    print("==========================================")

    if action_items:

        for i, item in enumerate(
            action_items,
            1
        ):
            print(
                f"{i}. {item}"
            )

    else:

        print(
            "No action items detected."
        )

    # STEP 4
    print("\nAnalyzing decisions...")

    decisions = detect_decisions(
        transcript
    )

    print("\n==========================================")
    print("               DECISIONS")
    print("==========================================")

    if decisions:

        for i, decision in enumerate(
            decisions,
            1
        ):
            print(
                f"{i}. {decision}"
            )

    else:

        print(
            "No decisions detected."
        )

    return {
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items,
        "decisions": decisions
    }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    audio_path = input(
        "\nEnter audio file path: "
    ).strip()

    try:

        result = process_meeting(
            audio_path
        )

        print("\n==========================================")
        print("          PROCESSING COMPLETE")
        print("==========================================")

    except Exception as e:

        print("\n==========================================")
        print("                  ERROR")
        print("==========================================")

        print(
            type(e).__name__
        )

        print(
            str(e)
        )