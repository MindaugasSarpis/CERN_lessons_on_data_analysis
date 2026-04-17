"""Tech stocks with no grid at all — lines float (Wilke fig 23.8)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save, stamp_bad


COLORS = {"FB": "#000000", "GOOG": "#E69F00",
          "MSFT": "#56B4E9", "AAPL": "#009E73"}
LABELS = {"FB": "Facebook", "GOOG": "Alphabet",
          "MSFT": "Microsoft", "AAPL": "Apple"}


def render() -> None:
    apply_base()
    df = D.tech_stocks().copy()

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    for ticker in ["FB", "GOOG", "MSFT", "AAPL"]:
        sub = df[df["ticker"] == ticker].sort_values("date")
        ax.plot(sub["date"], sub["price_indexed"],
                color=COLORS[ticker], linewidth=1.6,
                label=LABELS[ticker])
    ax.set_xlabel("year")
    ax.set_ylabel("stock price, indexed")
    ax.set_ylim(0, 560)
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    open_axes(ax)

    stamp_bad(fig)
    fig.tight_layout()
    save(fig, "balance_data_context", "price_plot_no_grid")


if __name__ == "__main__":
    render()
