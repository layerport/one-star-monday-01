#!/usr/bin/env python3
"""One Star for Monday — a make.fun program/v1 entry.

Writes one line of plain text, a one-star review of Monday written as
though Monday were a restaurant, to /output/entry.txt.

The line is fixed: the program is deterministic, so every run produces
byte-identical output. Standard library only, no network, no secrets.
"""

from pathlib import Path

# The review itself. It reads like a real diner's complaint: a table
# (seated late), a dish gone wrong (a cold Monday, served), and a bill
# (charged the whole week) — and it could only be about Monday.
REVIEW = (
    "One star. Seated after forty minutes, served a cold Monday, "
    "and the waiter charged me the whole week."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = REVIEW.strip()
    # Gate limits from the bounty rules: 1-180 characters, at most
    # 25 words, a single line of plain text, no hashtags or explanation.
    assert 1 <= len(text) <= 180, "review must be 1-180 characters"
    assert len(text.split()) <= 25, "review must be at most 25 words"
    assert "\n" not in text, "review must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the review line.
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
