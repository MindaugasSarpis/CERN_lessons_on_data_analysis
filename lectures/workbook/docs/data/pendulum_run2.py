#!/usr/bin/env python3
"""Write `pendulum_run2_raw.csv`: the lab partner's second series.

Lecture 12 opens on this file. It has the form of `pendulum_raw.csv` (`;`
between values, decimal commas, a column `nr`, a summary line at the end)
and two differences that a person sees at once and a program that edits
text does not:

1. the summary line is spelt `Mean`, with a capital M;
2. the time for 80 cm was not taken, and its cell is empty.

The partner's spreadsheet computed the summary line over the eight times
that are there: 118.41 / 8 = 14.80125, written `14,80`.

The values are example values, written for the exercise: the time of 10
swings for the nine lengths of the first series, close to
T = 2*pi*sqrt(L/g). The lengths 20, 40 and 60 cm are the `run2` of the
Reshape & Join slides of Lecture 12.

Usage:  python pendulum_run2.py      (needs nothing but Python)
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "pendulum_run2_raw.csv"

LENGTH_CM = [20, 30, 40, 50, 60, 70, 80, 90, 100]
T10_S = [8.97, 11.02, 12.74, 14.15, 15.58, 16.83, None, 19.08, 20.04]


def comma(value):
    """A number as the partner's spreadsheet writes it: two decimals, a comma."""
    return f"{value:.2f}".replace(".", ",")


def main():
    lines = ["nr;length_cm;t10_s"]
    for nr, (length, t10) in enumerate(zip(LENGTH_CM, T10_S), start=1):
        lines.append(f"{nr};{length};{'' if t10 is None else comma(t10)}")
    taken = [t for t in T10_S if t is not None]
    lines.append(f";Mean;{comma(sum(taken) / len(taken))}")
    OUT.write_bytes(("\n".join(lines) + "\n").encode("ascii"))
    print(f"{OUT.name}: {len(lines)} lines, {OUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
