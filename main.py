#!/usr/bin/env python3
"""Write one funny line to /output/entry.txt.

The line is a single sentence of at most 200 characters: an everyday
moment (muting the family group chat) whose punchline lands on the last
few words, when the silence turns into 214 unread messages.
"""

import os

MAX_CHARS = 200

PARTS = (
    "I muted the family group chat for an hour, ",
    "and came back to 214 messages, a poll, ",
    "and a photo of my uncle's knee.",
)


def build_line():
    """Join the three clauses into the single entry line."""
    if len(PARTS) != 3 or not all(PARTS):
        raise ValueError("entry must be built from three non-empty clauses")
    line = "".join(PARTS)
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    return line


def check_line(line):
    """Raise unless the line satisfies the competition gate."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not line.endswith("."):
        raise ValueError("entry must end with a period")
    if line.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")


def main():
    line = build_line()
    check_line(line)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (line + "\n").encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    with open(path, "rb") as handle:
        if handle.read() != data:
            raise ValueError("written entry does not match the line")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
