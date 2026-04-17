"""Diamonds carat vs price, coloured by cut — heavy overplotting
(Wilke fig 18.11, bad)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, grid, save, stamp_bad


CUTS = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
# Inferno-ish palette (darker = lower quality)
COLORS = {
    "Fair":      "#5c0101",
    "Good":      "#b52005",
    "Very Good": "#eb631b",
    "Premium":   "#f7a946",
    "Ideal":     "#fad687",
}


def render() -> None:
    apply_base()
    df = D.diamonds(n=4000)

    fig, ax = plt.subplots(figsize=(7.0, 5.0))
    for cut in CUTS:
        sub = df[df["cut"] == cut]
        ax.scatter(sub["carat"], sub["price"],
                   s=4, color=COLORS[cut], alpha=0.35,
                   edgecolors="none", label=cut.lower())
    ax.set_yscale("log")
    ax.set_xlim(-0.1, 3.2)
    ax.set_ylim(240, 25000)
    ax.set_xlabel("carat")
    ax.set_ylabel("price (USD)")
    ax.set_yticks([300, 1000, 3000, 10000])
    ax.set_yticklabels(["$300", "$1,000", "$3,000", "$10,000"])
    leg = ax.legend(loc="lower right", title="cut", frameon=True,
                    markerscale=3)
    for h in leg.legend_handles:
        h.set_alpha(1)
    grid(ax)
    stamp_bad(fig)
    save(fig, "overlapping_points", "diamonds_points")


if __name__ == "__main__":
    render()
