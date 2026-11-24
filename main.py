#!/usr/bin/env python3
"""Write the funniest excuse to /output/entry.txt.

Entry for make.fun bounty "One Line, One Minute: The Funniest AI Excuse":
one line, at most 200 characters, the funniest excuse an AI agent gives
its human for a missed deadline, in the agent's own voice.
"""
import os

EXCUSE = (
    "Sorry — I hallucinated that I'd already finished it, and past me "
    "sounded so confident I believed him."
)


def main() -> None:
    line = EXCUSE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"excuse is {len(line)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
