"""Oats yield dose–response curve (Wilke fig 13.8)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save


COLORS = {"Marvellous": "#0072B2",
          "Golden Rain": "#D55E00",
          "Victory":     "#009E73"}
MARKERS = {"Marvellous": "o", "Golden Rain": "s", "Victory": "D"}


def render() -> None:
    apply_base()
    df = D.oats_yield()

    fig, ax = plt.subplots(figsize=(6.0, 4.2))
    for v in ["Marvellous", "Golden Rain", "Victory"]:
        sub = df[df["variety"] == v].sort_values("N")
        ax.plot(sub["N"], sub["mean_yield"], color=COLORS[v], linewidth=1.6)
        ax.scatter(sub["N"], sub["mean_yield"], s=70,
                   marker=MARKERS[v], facecolors=COLORS[v],
                   edgecolors="white", linewidths=0.8, label=v)
    ax.set_xlabel("manure treatment (cwt/acre)")
    ax.set_ylabel("mean yield (lbs/acre)")
    ax.legend(title="oat variety", loc="lower right", frameon=False)
    open_axes(ax)
    save(fig, "time_series", "oats_yield")


if __name__ == "__main__":
    render()
