"""Empirical CDF of titanic passenger ages (Wilke fig 8.4)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = D.titanic()
    age = np.sort(df["age"].dropna().values)
    ecdf = np.arange(1, age.size + 1) / age.size

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.step(age, ecdf, where="post", color=PRIMARY_BLUE, linewidth=1.8)
    ax.set_xlabel("age (years)")
    ax.set_ylabel("cumulative frequency")
    ax.set_ylim(0, 1.02)
    hgrid(ax)
    save(fig, "distributions_i", "titanic_ecdf")


if __name__ == "__main__":
    render()
