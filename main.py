#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes the Moon's one-line reply to entry.txt, validating the kit gate
exactly: UTF-8 text, 1-240 characters, not only whitespace.
"""

import os
import sys

ENTRY = "You wished for a sign, so I gave you an eclipse. You hid indoors and called it bad luck."


def main():
    text = ENTRY
    try:
        raw = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise SystemExit("entry is not valid UTF-8: %s" % exc)
    if not 1 <= len(text) <= 240:
        raise SystemExit("entry must be 1-240 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(raw)
    with open(path, "rb") as f:
        written = f.read()
    if written != raw:
        raise SystemExit("read-back mismatch: entry.txt bytes differ from validated text")


if __name__ == "__main__":
    main()
