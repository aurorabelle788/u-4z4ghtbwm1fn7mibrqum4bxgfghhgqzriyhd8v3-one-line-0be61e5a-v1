"""One Line, One Laugh — entry program.

Writes a single original one-liner to the output path the grader
provides (OUTPUT_PATH, default /output/entry.txt).

The line is a fixed constant: deterministic, stdlib-only, no network,
no randomness, so every run produces byte-identical output.
"""

import os

# The joke: a cosmic plea answered with the pettiest modern snub — a
# read receipt, timestamp and all. The setup promises the profound; the
# second half lands the mundane. The timestamp is the punch: the void
# didn't just ignore the plea, it opened it at 2:47 AM and said nothing.
JOKE = "I asked the void for a sign; it replied 'seen 2:47 AM'."


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
