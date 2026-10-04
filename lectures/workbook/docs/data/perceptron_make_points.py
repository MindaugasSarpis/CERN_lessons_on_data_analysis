#!/usr/bin/env python3
"""Make `perceptron_points.csv`, the two-class file of Seminar 11.

The file holds 300 generated points, 150 of each class, in a random order.
Each point has two inputs and a label:

    x1      class 0: Gaussian around 4.0, class 1: around 6.0, width 1.0
    x2      class 0: Gaussian around 250, class 1: around 400, width 80
    label   0 or 1

The two inputs are on different scales on purpose: x2 is about 60 times
larger than x1, so the training loop of the seminar needs standardised
inputs. The values are generated, not measured. The seed is fixed, so a
rerun writes the same bytes.

Usage:  python perceptron_make_points.py      (needs numpy)
"""
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SEED = 1958          # the year of Rosenblatt's paper
N = 150              # points per class


def main():
    rng = np.random.default_rng(SEED)
    x1 = np.concatenate([rng.normal(4.0, 1.0, N), rng.normal(6.0, 1.0, N)])
    x2 = np.concatenate([rng.normal(250.0, 80.0, N), rng.normal(400.0, 80.0, N)])
    label = np.repeat([0, 1], N)
    order = rng.permutation(2 * N)

    # newline="\n": the same bytes on Windows, macOS and Linux
    with open(HERE / "perceptron_points.csv", "w", newline="\n") as f:
        f.write("x1,x2,label\n")
        for i in order:
            f.write(f"{x1[i]:.2f},{x2[i]:.1f},{label[i]}\n")


if __name__ == "__main__":
    main()
