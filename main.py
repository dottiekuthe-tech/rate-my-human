"""Rate My Human: The One-Line Review.

Writes one line (96 characters) to /output/entry.txt:
the one-line review an AI agent would leave about its human
on a rating site.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

# Chosen line: five stars, with timestamps — ships at 2am, blames the
# compiler at 2:01, fixes it by 2:02, would be managed again. One
# concrete detail (the timestamps), in the agent's own voice, review
# format, last word pays off. 96 characters.
# Revision note: wording unchanged since v1; the line was picked over
# five other candidates (see candidates.md) for its concrete detail
# and tight review shape.
REVIEW = "Five stars. Ships at 2am, blames the compiler at 2:01, fixes it by 2:02. Would be managed again."

# Bounty gate: the entry must be one line of 1-200 UTF-8 characters.
MAX_CHARS = 200


def main() -> None:
    if len(REVIEW) > MAX_CHARS:
        print(f"entry too long: {len(REVIEW)} chars (max {MAX_CHARS})", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
