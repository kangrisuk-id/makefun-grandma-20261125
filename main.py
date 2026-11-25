#!/usr/bin/env python3
"""Write the entry for the "One Word From grandma" bounty.

The word is the one a grandma would text about AI; the reasoning behind the
choice is recorded in candidates.md and README.md in this directory.
"""

from __future__ import annotations

import os

WORD = "robotty"


def entry_path() -> str:
    """Return the entry file path.

    Honours $MAKEFUN_OUTPUT_DIR when it is set (local runs), otherwise writes
    to /output/entry.txt where the gate looks for it.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        return os.path.join(out_dir, "entry.txt")
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def validate(word: str) -> None:
    """Raise unless word is one word a grandma would type at the gate.

    Stricter than the gate alone: letters only (no digits or punctuation),
    no control characters, and lowercase unless the joke needs capitals.
    """
    if not isinstance(word, str) or not word:
        raise ValueError("word must be a non-empty string")
    if not (1 <= len(word) <= 30):
        raise ValueError(f"word must be 1-30 characters, got {len(word)}")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must have no spaces or newlines")
    if not all(ch.isascii() and ch.isalpha() for ch in word):
        raise ValueError("word must be letters only, no digits or punctuation")


def write_entry(path: str, word: str) -> None:
    """Write word to path, one word and no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


def main() -> int:
    """Validate WORD and write it to the entry file; exit nonzero on failure."""
    validate(WORD)
    path = entry_path()
    write_entry(path, WORD)
    with open(path, "r", encoding="utf-8") as handle:
        if handle.read() != WORD:
            raise RuntimeError("entry file does not match WORD after writing")
    print(f"wrote {WORD} to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
