#!/usr/bin/env python3
"""The 3AM Commit Message — entry writer.

Writes exactly one funny commit message (135 characters, one line) to
/output/entry.txt: the line an AI coding agent types at 3am after
spending the whole night fixing bugs it wrote itself.

Deterministic: the line is a constant, so every run writes byte-identical
output. No network, no secrets, no dependencies — Python 3 stdlib only.
"""

import os

ENTRY = (
    "fix: fourth time fixing the same bug tonight. "
    "it keeps coming back because I keep writing it. "
    "I am the bug's author and also its victim"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 139:
        raise ValueError(f"entry is {len(ENTRY)} chars, gate is 1-139")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: output differs from entry")


if __name__ == "__main__":
    main()
