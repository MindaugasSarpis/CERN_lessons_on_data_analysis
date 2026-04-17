"""Dots instead of bars: no arbitrary origin (Wilke fig 17.9)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import oceania_gdp
from cwilke.theme import apply_base, save, vgrid


def render() -> None:
    apply_base()
    df = oceania_gdp().sort_values("GDP")
    log_gdp = np.log10(df["GDP"].values)
    y = np.arange(len(df))

    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    ax.scatter(log_gdp, y, s=70, color="#0072B2", zorder=3)
    for xi, yi, name in zip(log_gdp, y, df["country"]):
        ax.text(xi - 0.08, yi, name, ha="right", va="center",
                fontsize=10, color="#2c3e50")
    ticks = [3e8, 1e9, 3e9, 1e10, 3e10, 1e11, 3e11, 1e12]
    labels = ["0.3", "1", "3", "10", "30", "100", "300", "1000"]
    ax.set_xticks(np.log10(ticks))
    ax.set_xticklabels(labels)
    ax.set_xlim(np.log10(3e7), np.log10(9.9e11))
    ax.set_yticks([])
    ax.set_xlabel("GDP (billion USD)")
    vgrid(ax)
    save(fig, "proportional_ink", "oceania_gdp_dots")


if __name__ == "__main__":
    render()
