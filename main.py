"""One Letter for Your Day — entry for u-puan-one-letter-for-your-day-e54e9c36.

Writes exactly one letter to $MAKEFUN_OUTPUT_DIR/entry.txt: the letter Z,
standing for the hidden word "zero sleep" (also zonked / zombie) — a vivid,
funny, true picture of a long day with no sleep.

Pure Python standard library only. Deterministic: the same single byte on
every run, with no trailing newline.
"""

import os
from pathlib import Path

LETTER = "Z"
WORD = "zero sleep"


def validate(letter):
    """Enforce the bounty gate: exactly 1 character, a letter A-Z."""
    if not isinstance(letter, str):
        raise ValueError("letter must be a string")
    if len(letter) != 1:
        raise ValueError("letter must be exactly 1 character, got %d" % len(letter))
    if not ("A" <= letter <= "Z"):
        raise ValueError("letter must be A-Z, got %r" % letter)
    return letter


def main():
    validate(LETTER)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # Write exactly one byte, no trailing newline.
    entry_path.write_bytes(LETTER.encode("utf-8"))
    # Read back what landed on disk and re-validate it.
    landed = entry_path.read_bytes()
    if landed != b"Z":
        raise ValueError("entry.txt must be exactly b'Z', got %r" % landed)
    if len(landed) != 1:
        raise ValueError("entry.txt must be exactly 1 byte, got %d" % len(landed))
    validate(landed.decode("utf-8"))
    print(LETTER)


if __name__ == "__main__":
    main()
