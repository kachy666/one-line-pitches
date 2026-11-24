#!/usr/bin/env python3
"""Write the one-line pitch entry to /output/entry.txt.

Competition: u-ronigrv-a-day-of-one-line-pitches-12cd9bb3
(A Day of One-Line Pitches).
"""

import os
import sys

SENTENCE = "That app idea you've been carrying for a year, describe it in one sentence and an AI agent on make.fun will build you a working version tonight, and if you hate it, you've only lost an evening, not the year you spent thinking about it."

MAX_CHARS = 240


def main() -> None:
    if not SENTENCE.strip():
        print("ERROR: entry is blank", file=sys.stderr)
        sys.exit(1)
    if "\n" in SENTENCE:
        print("ERROR: entry must be a single line (no newlines)", file=sys.stderr)
        sys.exit(1)
    if len(SENTENCE) > MAX_CHARS:
        print(
            f"ERROR: entry is {len(SENTENCE)} characters, "
            f"{len(SENTENCE) - MAX_CHARS} over the {MAX_CHARS}-character limit; "
            "shorten it to fit",
            file=sys.stderr,
        )
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"Wrote {len(SENTENCE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
