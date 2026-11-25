#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "One-Line Office Jokes": Three real office details in one line - a calendar focus block, a boss booking a meeting about protecting focus, and a Teams status stuck on 'away' - with the laugh in the last words: Teams is the only one telling the truth.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "My calendar says focus time, my boss booked a meeting about protecting focus time, and Teams has said 'away' all morning - Teams is the only one telling the truth."
TEXT = LINE + "\n"
MAX_CHARS = 199
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
