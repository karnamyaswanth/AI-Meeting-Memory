from transformers import pipeline


print("Loading decision detection model...")

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

print("Decision detection model loaded successfully!")


def extract_decisions(text):

    if not text or not text.strip():
        return []

    sentences = [
        sentence.strip()
        for sentence in text.split(".")
        if sentence.strip()
    ]

    decisions = []

    labels = [
        "decision",
        "action item",
        "general discussion"
    ]

    for sentence in sentences:

        result = classifier(
            sentence,
            candidate_labels=labels
        )

        best_label = result["labels"][0]

        if best_label == "decision":
            decisions.append(sentence)

    return decisions


if __name__ == "__main__":

    print()
    print("==========================================")
    print("       AI MEETING MEMORY")
    print("       DECISION DETECTION")
    print("==========================================")

    transcript = input(
        "\nEnter meeting transcript:\n"
    ).strip()

    try:

        decisions = extract_decisions(
            transcript
        )

        print()
        print("==========================================")
        print("              DECISIONS")
        print("==========================================")

        if decisions:

            for number, decision in enumerate(
                decisions,
                start=1
            ):
                print(
                    f"{number}. {decision}"
                )

        else:

            print(
                "No decisions detected."
            )

        print()
        print("==========================================")

    except Exception as error:

        print()
        print("ERROR:")
        print(type(error).__name__)
        print(error)