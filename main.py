"""The Absurd Clause Contest — make.fun bounty entry.

Writes one sentence (200 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

The sentence: in the event of a dispute, both parties agree to
settle the matter by a duel of rock-paper-scissors, best of three,
conducted in silence, in the company parking lot, at dawn, before
a jury of interns.
"""

import os
import sys

ENTRY = (
    "In the event of a dispute, both parties agree to settle the "
    "matter by a duel of rock-paper-scissors, best of three, "
    "conducted in silence, in the company parking lot, at dawn, "
    "before a jury of interns."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    if "\r" in text:
        sys.exit("entry must use plain LF line separators only")
    if "\n" in text:
        sys.exit("entry must be exactly one line")
    if text != text.strip():
        sys.exit("entry must not start or end with whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        sys.exit("entry must be exactly one sentence")
    if not 1 <= len(text) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(text))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes)" % (path, len(text), len(data)))


if __name__ == "__main__":
    main()
