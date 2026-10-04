#!/usr/bin/env python3
"""Make ml_two_class.csv, the two-class file of Lecture 16 and Seminar 16.

600 rows, three columns:

    x1, x2   two measured quantities, in different units and on different
             scales (x1 around 5, x2 around 30)
    label    the class of the row, 0 or 1

Class 1 is a round cloud of 300 points. Class 0 is a ring of 300 points
around it. The two overlap where the cloud meets the ring, so no rule
separates them without error, and no straight line separates them at all.

The data are simulated: every run with the same seed writes the same file.

Usage:  python ml_two_class.py            (needs NumPy; writes next to itself)
"""
from pathlib import Path

import numpy as np

SEED = 16
N_PER_CLASS = 300
CENTRE = np.array([5.0, 30.0])     # centre of both classes, in the units of x1, x2
SCALE = np.array([1.0, 10.0])      # one unit of radius, in the units of x1, x2


def make():
    rng = np.random.default_rng(SEED)
    # class 1: a round cloud, standard deviation 0.6 radius units
    cloud = rng.normal(0.0, 0.6, (N_PER_CLASS, 2))
    # class 0: a ring of radius 2.0 with a spread of 0.35
    angle = rng.uniform(0.0, 2 * np.pi, N_PER_CLASS)
    radius = rng.normal(2.0, 0.35, N_PER_CLASS)
    ring = np.column_stack([radius * np.cos(angle), radius * np.sin(angle)])
    x = np.vstack([cloud, ring]) * SCALE + CENTRE
    label = np.concatenate([np.ones(N_PER_CLASS, int), np.zeros(N_PER_CLASS, int)])
    order = rng.permutation(2 * N_PER_CLASS)        # mix the two classes
    return x[order], label[order]


def main():
    x, label = make()
    out = Path(__file__).with_name("ml_two_class.csv")
    with open(out, "w", newline="\n") as f:
        f.write("x1,x2,label\n")
        for (x1, x2), lab in zip(x, label):
            f.write(f"{x1:.3f},{x2:.2f},{lab}\n")
    print(f"{out.name}: {len(label)} rows, {int(label.sum())} of class 1")


if __name__ == "__main__":
    main()
