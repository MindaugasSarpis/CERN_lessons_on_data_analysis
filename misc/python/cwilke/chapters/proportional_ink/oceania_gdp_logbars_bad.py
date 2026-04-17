"""Horizontal bars on a log axis, starting at 0.3 B USD — misleading (17.7)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import oceania_gdp
from cwilke.theme import PRIMARY_BLUE, apply_base, save, stamp_bad, vgrid


def render() -> None:
    apply_base()
    df = oceania_gdp().sort_values("GDP")
    x_start = np.log10(3.1e8)  # 0.3 B USD
    log_gdp = np.log10(df["GDP"].values)

    fig, ax = plt.subplots(figsize=(7.0, 3.6))
    ax.barh(df["country"], log_gdp - x_start, left=x_start,
            color=PRIMARY_BLUE, height=0.7,
            edgecolor="#2c3e50", linewidth=0.5)
    ticks = [3.1e8, 1e9, 3e9, 1e10, 3e10, 1e11, 3e11, 1e12]
    labels = ["0.3", "1", "3", "10", "30", "100", "300", "1000"]
    ax.set_xticks(np.log10(ticks))
    ax.set_xticklabels(labels)
    ax.set_xlim(x_start, np.log10(9.9e11))
    ax.set_xlabel("GDP (billion USD)")
    vgrid(ax)
    stamp_bad(fig)
    save(fig, "proportional_ink", "oceania_gdp_logbars_bad")


if __name__ == "__main__":
    render()
