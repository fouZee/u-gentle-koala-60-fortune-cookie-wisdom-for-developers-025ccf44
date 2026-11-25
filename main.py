#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (or $OUTPUT_DIR/entry.txt). The gate requires UTF-8
text of 1 to 120 characters, not only white space.
"""

import os
import sys

ENTRY = "The bug you cannot reproduce is not hiding \u2014 it is rehearsing for the live demo."

MAX_CHARS = 120


def validate(text: str) -> None:
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} chars")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
