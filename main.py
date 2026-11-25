#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt, roasting lawmakers
who regulate AI, crypto or the internet but cannot convert a file to PDF.
"""

import os

ENTRY = (
    "The senator who wrote the law deciding what your chatbot is allowed "
    "to say just printed the bill, signed it, scanned it back in, and "
    "emailed the scan to his staff asking if anyone could please turn it "
    "into a PDF."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 320
    # characters, not only whitespace, and a single sentence.
    assert 1 <= len(ENTRY) <= 320, "entry must be 1-320 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
