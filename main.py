import os

SENTENCE = "Tell make.fun your app idea in plain words and the AI agent hands you back a working first version you can open and try tonight."


def main():
    if not SENTENCE or SENTENCE.isspace():
        raise SystemExit("sentence is empty or whitespace-only")
    if len(SENTENCE) > 240:
        raise SystemExit("sentence is longer than 240 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()