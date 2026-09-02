from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


MODEL_NAME = "sshleifer/distilbart-cnn-12-6"


print("Loading summarization model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)

print("Summarization model loaded successfully!")


def summarize_text(text):

    if not text or not text.strip():
        return "No transcript available."

    # Clean text
    text = text.strip()

    # Tokenize
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    # Generate summary
    summary_ids = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=120,
        min_length=25,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )

    return summary


if __name__ == "__main__":

    print()
    print("==========================================")
    print("       AI MEETING MEMORY")
    print("       TEXT SUMMARIZATION")
    print("==========================================")

    transcript = input(
        "\nEnter meeting transcript:\n"
    ).strip()

    try:

        summary = summarize_text(
            transcript
        )

        print()
        print("==========================================")
        print("              AI SUMMARY")
        print("==========================================")
        print()

        print(summary)

        print()
        print("==========================================")

    except Exception as error:

        print()
        print("==========================================")
        print("                  ERROR")
        print("==========================================")
        print()

        print(type(error).__name__)
        print(error)