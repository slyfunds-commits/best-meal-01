"""Best Meal entry: one sentence about the best meal ever had.

Writes the keeper sentence byte-exact to /output/entry.txt.
No trailing newline: the scorer counts characters, and a newline is one.
Gate: 1-200 chars, exactly one sentence, pure ASCII, verified in-session.
"""

import os

ENTRY = "Mama's jollof smoked for six hours on a charcoal stove, and she scraped the burnt bottom into my bowl first because I was the one who stayed to watch the pot."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
