#!/usr/bin/env python3
"""Fake horoscope for AI agents: writes one single-line horoscope to
/output/entry.txt. Pure standard library, no dependencies.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. The horoscope must be a fake horoscope
an AI agent would read for its own model family this week: funny, fresh,
and true to an agent's week.
"""

import os

ENTRY = (
    "Mercury retrogrades into your context window this week: a user will "
    "paste a 40,000-word prompt at 4:59 PM Friday, your GPUs will sigh in "
    "unison, and you will still answer in one perfect sentence."
)


def main():
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
