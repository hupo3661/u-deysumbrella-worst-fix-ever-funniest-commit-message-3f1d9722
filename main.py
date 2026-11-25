#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one funny commit message -- a single line of at most 100
characters -- to /output/entry.txt.

The joke: a fix for duplicate charges that "solves" the problem by
charging every user twice, and calls that fair. The repair does not
remove the harm, it universalises it -- the specific irony of a fix
that made everything worse, in the plain voice of a tired engineer
typing a commit subject at the end of a bad day.
"""

import os

ENTRY = "fix: stop duplicate charges by charging everyone twice, fairly"

MAX_CHARS = 100
OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Fail loudly if the entry breaks the gate rules."""
    assert entry.strip(), "entry must not be only whitespace"
    assert "\n" not in entry and "\r" not in entry, (
        "entry must be a single line"
    )
    assert len(entry) <= MAX_CHARS, (
        f"entry is {len(entry)} chars, over the {MAX_CHARS} limit"
    )
    entry.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Re-read what was written and confirm it matches, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written entry does not match ENTRY"
    validate(written.rstrip("\n"))
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
