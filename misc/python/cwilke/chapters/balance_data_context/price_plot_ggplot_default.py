"""Tech stocks plotted in the classic ggplot2-default style (Wilke fig 23.7).

Grey background, dense white major + minor grid, boxed legend.
Labelled "ugly" — the grid overwhelms the data lines.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save, stamp_ugly


COLORS = {"FB": "#000000", "GOOG": "#E69F00",
          "MSFT": "#56B4E9", "AAPL": "#009E73"}
LABELS = {"FB": "Facebook", "GOOG": "Alphabet",
          "MSFT": "Microsoft", "AAPL": "Apple"}


def render() -> None:
    apply_base()
    df = D.tech_stocks().copy()

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.set_facecolor("#e5e5e5")
    for ticker in ["FB", "GOOG", "MSFT", "AAPL"]:
        sub = df[df["ticker"] == ticker].sort_values("date")
        ax.plot(sub["date"], sub["price_indexed"],
                color=COLORS[ticker], linewidth=1.3,
                label=LABELS[ticker])
    ax.set_xlabel("year")
    ax.set_ylabel("stock price, indexed")
    ax.set_ylim(0, 560)

    # Dense white grid, major + minor
    ax.grid(True, which="major", color="white", linewidth=1.1)
    ax.minorticks_on()
    ax.grid(True, which="minor", color="white", linewidth=0.5)

    # Boxed legend with grey fill
    leg = ax.legend(loc="upper left", fontsize=10, frameon=True,
                    facecolor="#e5e5e5", edgecolor="white")

    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)

    stamp_ugly(fig)
    fig.tight_layout()
    save(fig, "balance_data_context", "price_plot_ggplot_default")


if __name__ == "__main__":
    render()
