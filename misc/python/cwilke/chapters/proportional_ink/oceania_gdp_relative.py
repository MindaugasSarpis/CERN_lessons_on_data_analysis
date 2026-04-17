"""Log-scale bars showing GDP ratios vs Papua New Guinea (Wilke 17.10)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import oceania_gdp
from cwilke.theme import PRIMARY_BLUE, apply_base, save, vgrid


def render() -> None:
    apply_base()
    df = oceania_gdp()
    png = float(df.loc[df["country"] == "Papua New Guinea", "GDP"].iloc[0])
    df = df[df["country"] != "Papua New Guinea"].copy()
    df["ratio"] = df["GDP"] / png
    df = df.sort_values("ratio")
    log_r = np.log2(df["ratio"].values)

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    # Bars from log2(1) = 0, extending to log2(ratio). Negative values go left.
    widths = log_r
    ax.barh(df["country"], widths, left=0,
            color=PRIMARY_BLUE, height=0.7,
            edgecolor="#2c3e50", linewidth=0.5)
    ax.axvline(0, color="#2c3e50", linewidth=0.8)
    ticks = [1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16, 32, 64]
    labels = ["1/16", "1/8", "1/4", "1/2", "1", "2", "4", "8", "16", "32", "64"]
    ax.set_xticks(np.log2(ticks))
    ax.set_xticklabels(labels)
    ax.set_xlim(np.log2(0.055), np.log2(70))
    ax.set_xlabel("GDP relative to Papua New Guinea")
    vgrid(ax)
    save(fig, "proportional_ink", "oceania_gdp_relative")


if __name__ == "__main__":
    render()
