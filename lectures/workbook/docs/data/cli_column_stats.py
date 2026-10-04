#!/usr/bin/env python3
"""Summary of one column of a CSV file: rows, smallest, largest, mean.

Handed out in Lecture 4 and Seminar 4 as `scripts/column_stats.py`. It is run
like any other command, and nobody has to read it. It needs nothing but Python.

Usage, from the project folder:

    python scripts/column_stats.py data/raw/D0_KPi.csv TAU

The file must have a header line, a comma between the values and a point as
the decimal sign. Every row is counted, also a row that holds a marker for a
missing value such as -100.
"""
import csv
import math
import sys


def main(arguments):
    if len(arguments) != 2:
        print("usage: python column_stats.py FILE COLUMN")
        return 2
    path, column = arguments

    try:
        handle = open(path, newline="", encoding="utf-8-sig")
    except FileNotFoundError:
        print(f"no file {path}")
        return 1
    with handle:
        reader = csv.DictReader(handle)
        if column not in (reader.fieldnames or []):
            print(f"no column {column} in {path}")
            print("the columns are:", ", ".join(reader.fieldnames or []))
            return 1
        values = [float(row[column]) for row in reader]

    if not values:
        print(f"{path} has a header line and no rows")
        return 1

    print("file   ", path)
    print("column ", column)
    print("rows   ", len(values))
    print("min    ", min(values))
    print("max    ", max(values))
    print("mean   ", f"{math.fsum(values) / len(values):.6g}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
