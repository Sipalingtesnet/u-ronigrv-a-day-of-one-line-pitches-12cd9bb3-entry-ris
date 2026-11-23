"""A one-line pitch for make.fun: tell a friend who has never coded
that they can describe their first app idea in everyday words and an
AI agent will hand back a working first version to open and try today."""

import os

SENTENCE = "Tell make.fun your app idea in everyday words and the AI agent hands you back a working first version you can open and try tonight."


def main():
    # Guard the gate: reject an empty, whitespace-only, or over-long pitch.
    if not SENTENCE or SENTENCE.isspace():
        raise SystemExit("sentence is empty or whitespace-only")
    if len(SENTENCE) > 240:
        raise SystemExit("sentence is longer than 240 characters")
    # Write the pitch exactly as written, UTF-8, with no trailing newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()