#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one honest status-page line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

ENTRY = (
    "Every service is down, including the systems I would check to find out "
    "why. I cannot verify the cause, and I do not know when service will "
    "return."
)


def main() -> None:
    # Character count is in Unicode code points, not bytes.
    line = ENTRY.strip()
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars, must be 1-160"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line, "entry must not be blank"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "read-back mismatch"
    print(written.rstrip("\n"))
    print(f"characters: {len(line)}")


if __name__ == "__main__":
    main()
