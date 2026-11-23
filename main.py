#!/usr/bin/env python3
"""Make the Judge Smile — entry writer.

Writes a single warm line, at most 200 characters, about a small
good thing that happened today, to /output/entry.txt.
"""

import os

LINE = "The stray cat who hisses at the whole street climbed into my lap at dawn and purred through my entire first coffee."

MAX_CHARS = 200
OUT_PATH = "/output/entry.txt"


def tidy(text):
    """Collapse any stray whitespace so the entry stays one line."""
    return " ".join(text.split())


def check(text):
    cleaned = tidy(text)
    assert cleaned, "entry must not be empty"
    assert "\n" not in cleaned, "entry must be a single line"
    assert len(cleaned) <= MAX_CHARS, (
        f"entry is {len(cleaned)} characters, over the {MAX_CHARS} limit"
    )
    return cleaned


def read_back(path, expected):
    """Re-read the written file and confirm it holds exactly the entry."""
    with open(path, encoding="utf-8") as handle:
        stored = handle.read().rstrip("\n")
    assert stored == expected, "written file does not match the entry"
    return stored


def main():
    line = check(LINE)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    read_back(OUT_PATH, line)
    print(f"wrote {len(line)} characters to {OUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
