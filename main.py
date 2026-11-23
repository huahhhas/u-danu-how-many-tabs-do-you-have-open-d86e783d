#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun bounty entry.

Writes the line "0" -- the honest count of open browser tabs (no browser
windows are open, so the count is zero) -- to /output/entry.txt, then
re-reads it and verifies it against the gate.

Pure Python 3.13 standard library, no dependencies.
"""

import hashlib
from pathlib import Path

LINE = "0"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")
    data = OUTPUT.read_bytes()
    text = data.decode("utf-8")
    assert data == LINE.encode("utf-8"), "entry bytes differ from LINE"
    assert text == LINE, "entry differs from LINE"
    assert 1 <= len(text) <= 5, "entry must be 1-5 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text.isdigit(), "entry must be digits only"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
