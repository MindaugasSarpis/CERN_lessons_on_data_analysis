"""Bar chart with SE error bars: butterfat by breed (Wilke fig 16.10)."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from cwilke.data import cows_butterfat
from cwilke.theme import PRIMARY_BLUE, apply_base, hgrid, save


def render() -> None:
    apply_base()
    df = cows_butterfat()
    g = df.groupby("breed")["butterfat"]
    mean = g.mean()
    se = g.std(ddof=1) / np.sqrt(g.count())
    order = mean.sort_values(ascending=False).index
    mean = mean.loc[order]
    se = se.loc[order]

    fig, ax = plt.subplots(figsize=(5.8, 4.0))
    ax.bar(range(len(mean)), mean.values,
           color=PRIMARY_BLUE, alpha=0.8, width=0.65,
           edgecolor="#2c3e50", linewidth=0.5,
           yerr=1.96 * se.values,
           error_kw=dict(ecolor="#2c3e50", lw=0.9, capsize=3))
    ax.set_xticks(range(len(mean)))
    ax.set_xticklabels([b.replace("-", "-\n") for b in mean.index])
    ax.set_ylabel("mean butterfat contents")
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax.set_ylim(0, 6.0)
    hgrid(ax)
    fig.tight_layout()
    save(fig, "uncertainty", "butterfat_bars")


if __name__ == "__main__":
    render()
