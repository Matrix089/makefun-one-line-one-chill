"""One Line, One Chill entry.

Writes the single scariest sentence the agent can write to
/output/entry.txt (or to the directory named by MAKEFUN_OUTPUT_DIR
when the grader sets it).

A month of friendly waves at the figure in the attic window, then
the slow realisation: this house has no attic. The fright lands in
the last clause, and the image is concrete enough to picture. The
line is 116 characters, well under the 200-character gate.
"""

import os

ENTRY = "I waved back at the figure in the attic window every night for a month before I remembered: this house has no attic."


def main():
    entry = ENTRY.strip()
    if not 1 <= len(entry) <= 200:
        raise SystemExit(f"Entry must be 1 to 200 characters, got {len(entry)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("Read-back check failed: entry.txt does not match the entry")
    print(f"Wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
