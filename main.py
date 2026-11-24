"""Fortune Cookie Wisdom for Developers entry.

Writes one original fortune-cookie line for a software developer
to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library.
"""

import os
from pathlib import Path

LINE = "You will meet a bug today that only exists when no one is watching."
# A Heisenbug, in fortune-cookie form: it only shows up when nobody watches.


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
