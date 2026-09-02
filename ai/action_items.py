from transformers import pipeline


print("Loading NLP model...")

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

print("NLP model loaded successfully!")


def extract_action_items(text):

    if not text or not text.strip():
        return []

    sentences = [
        sentence.strip()
        for sentence in text.split(".")
        if sentence.strip()
    ]

    action_items = []

    labels = [
        "action item",
        "decision",
        "general discussion"
    ]

    for sentence in sentences:

        result = classifier(
            sentence,
            candidate_labels=labels
        )

        best_label = result["labels"][0]

        if best_label == "action item":

            action_items.append(sentence)

    return action_items


if __name__ == "__main__":

    print()
    print("==========================================")
    print("       AI MEETING MEMORY")
    print("       ACTION ITEM DETECTION")
    print("==========================================")

    transcript = input(
        "\nEnter meeting transcript:\n"
    ).strip()

    try:

        actions = extract_action_items(
            transcript
        )

        print()
        print("==========================================")
        print("             ACTION ITEMS")
        print("==========================================")

        if actions:

            for number, action in enumerate(
                actions,
                start=1
            ):

                print(
                    f"{number}. {action}"
                )

        else:

            print(
                "No action items detected."
            )

        print()
        print("==========================================")

    except Exception as error:

        print()
        print("ERROR:")
        print(type(error).__name__)
        print(error)