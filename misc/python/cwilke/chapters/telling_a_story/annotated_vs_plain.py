"""Side-by-side: plain vs. annotated scatter (Wilke fig 29.3 concept).

Two panels of the same data. Left: no annotations, generic title —
the reader is on their own. Right: callout arrow, highlighted point,
and a clearer framing — the viewer is guided to the finding.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke import data as D
from cwilke.theme import MUTED, PRIMARY_BLUE, WARN, apply_base, open_axes, save


def render() -> None:
    apply_base()

    df = D.corrupt().reset_index(drop=True)
    # Pick a specific "highlight" point — the highest HDI in the dataset.
    hi_idx = int(df["hdi"].idxmax())
    hi = df.loc[hi_idx]

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.2), sharey=True)

    # ------------------------ Left: plain ------------------------
    ax = axes[0]
    ax.scatter(df["cpi"], df["hdi"], s=42, color=PRIMARY_BLUE,
               edgecolor="white", linewidth=0.5, alpha=0.85)
    ax.set_xlabel("CPI")
    ax.set_ylabel("HDI")
    ax.set_title("HDI vs CPI", fontsize=12)
    open_axes(ax)

    # ------------------------ Right: annotated ------------------------
    ax = axes[1]
    # Non-highlight points first, smaller and faded
    mask = np.arange(len(df)) != hi_idx
    ax.scatter(df.loc[mask, "cpi"], df.loc[mask, "hdi"], s=38,
               color=PRIMARY_BLUE, edgecolor="white", linewidth=0.4,
               alpha=0.55)
    # Highlighted point
    ax.scatter([hi["cpi"]], [hi["hdi"]], s=140, color=WARN,
               edgecolor="#2c3e50", linewidth=1.2, zorder=5)

    # Callout text + arrow
    ax.annotate(
        "Top performer:\nhighest HDI in sample",
        xy=(hi["cpi"], hi["hdi"]),
        xytext=(hi["cpi"] - 40, hi["hdi"] - 0.08),
        fontsize=10, color="#2c3e50", fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="#2c3e50",
                        connectionstyle="arc3,rad=0.2", linewidth=1.2),
    )

    ax.set_xlabel("Corruption Perceptions Index (higher = cleaner)")
    ax.set_title("Clean-government leader stands out on HDI", fontsize=12)
    open_axes(ax)

    fig.text(0.5, 0.02,
             "Same data, two treatments. Annotation directs the reader's attention.",
             fontsize=9, color=MUTED, ha="center", style="italic")

    fig.subplots_adjust(top=0.90, bottom=0.13, left=0.07, right=0.98, wspace=0.12)
    save(fig, "telling_a_story", "annotated_vs_plain")


if __name__ == "__main__":
    render()
