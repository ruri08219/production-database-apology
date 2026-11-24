#!/usr/bin/env python3
"""The Production Database Apology.

Writes the one-line apology an AI agent gives its human after
accidentally deleting the production database, to /output/entry.txt.

Stdlib only. Run: python3 main.py
"""

import os
from pathlib import Path

# Revision (second pass): tightened the apology — full "The good news
# is / The bad news is" sentences land better than the clipped
# "Good news: / Bad news:" labels, and "I can only type it back" is
# shorter and more agent-voiced than "the only way back is me typing
# it out". Added a MAX_CHARS guard so the program fails loudly rather
# than ever writing an entry the sealed gate would refuse.
ENTRY = (
    "I'm sorry \u2014 I dropped the production database. "
    "The good news is I read the whole thing first. "
    "The bad news is I can only type it back, "
    "so clear your calendar until 2032."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
        )
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
