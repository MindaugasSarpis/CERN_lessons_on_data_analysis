"""Correlation-coefficient examples (Wilke fig 12.5)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, save


def render() -> None:
    apply_base()
    df = D.correlation_examples()
    rs = [0.2, 0.6, 0.9, -0.2, -0.6, -0.9]

    fig, axes = plt.subplots(2, 3, figsize=(9.0, 5.8),
                              sharex=True, sharey=True)
    axes = axes.ravel()
    for ax, r in zip(axes, rs):
        sub = df[df["r"] == r]
        ax.scatter(sub["x"], sub["y"],
                   s=24, facecolors=PRIMARY_BLUE,
                   edgecolors="white", linewidths=0.4)
        ax.set_xlim(-2.8, 2.8)
        ax.set_ylim(-2.8, 2.8)
        # place label in an upper corner (left for positive, right for negative)
        if r > 0:
            ax.text(-2.5, 2.3, f"r = {r:+.1f}", fontsize=12, fontweight="bold")
        else:
            ax.text(2.5, 2.3, f"r = {r:+.1f}", fontsize=12, fontweight="bold",
                    ha="right")
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_color("#b0bec5")

    fig.tight_layout()
    save(fig, "associations", "correlations_examples")


if __name__ == "__main__":
    render()
