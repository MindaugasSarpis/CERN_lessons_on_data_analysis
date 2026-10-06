#!/usr/bin/env python3
"""The four hand edits of Lecture 2, as a program.

Handed out in Lecture 4 and Seminar 4 as `scripts/clean_pendulum.py`. It is
run like any other command, and nobody has to read it yet. It needs nothing
but Python.

Usage, from the project folder (macOS: python3, Windows: python):

    python3 scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv

The edits are those written in the README in words:

1. the line with the mean is deleted,
2. `,` is replaced by `.` (the decimal sign),
3. `;` is replaced by `,` (the separator),
4. the column `nr` is deleted.

The output always ends its lines with LF, so it has the same bytes, and the
same checksum, on every system: 97 bytes for the table of Lecture 2.
"""
import sys


def clean(lines):
    out = []
    for line in lines:
        if "mean" in line:
            continue
        line = line.replace(",", ".").replace(";", ",")
        out.append(line.split(",", 1)[1])
    return out


def main(arguments):
    if len(arguments) != 2:
        print("usage: python clean_pendulum.py RAW_FILE CLEAN_FILE")
        return 2
    source, target = arguments
    try:
        with open(source, encoding="utf-8") as handle:
            lines = handle.read().splitlines()
    except FileNotFoundError:
        print(f"no file {source}")
        return 1
    rows = clean(line for line in lines if line)
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(rows) + "\n")
    print(f"{len(rows) - 1} rows written to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
