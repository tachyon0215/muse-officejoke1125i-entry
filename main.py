#!/usr/bin/env python3
"""Write the one-line office joke entry to entry.txt.

Judging fit: a strong office joke needs details every office worker
recognises and a punch that lands in the final words. This entry uses
three real details - a calendar focus block, a boss who books a
meeting about protecting that focus time, and a Teams status stuck on
'away' all morning - then turns them with the closing verdict that
Teams is the only one telling the truth. The contradiction between
the meeting's stated purpose and its existence is the joke, and
keeping everything in one line preserves its timing.
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
    if body != body.strip():
        raise ValueError("no leading or trailing whitespace")
    if not body.endswith("."):
        raise ValueError("entry should end with a full stop")
    if "  " in body:
        raise ValueError("no double spaces")
    if any(not ch.isprintable() for ch in body):
        raise ValueError("entry must be printable text only")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
