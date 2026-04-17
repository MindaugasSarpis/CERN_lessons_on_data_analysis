"""Tech stock prices where legend order ≠ visual order (Wilke fig 20.5, bad)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save, stamp_bad


# Alphabetical (legend order, not visual order)
ORDER = ["GOOG", "AAPL", "FB", "MSFT"]
LABELS = {"GOOG": "Alphabet", "AAPL": "Apple",
          "FB": "Facebook",  "MSFT": "Microsoft"}
COLOURS = {"GOOG": "#000000", "AAPL": "#E69F00",
           "FB":   "#56B4E9", "MSFT": "#009E73"}


def render() -> None:
    apply_base()

    df = D.tech_stocks()

    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    for ticker in ORDER:
        sub = df[df["ticker"] == ticker].sort_values("date")
        ax.plot(sub["date"], sub["price_indexed"],
                color=COLOURS[ticker], linewidth=1.8,
                label=LABELS[ticker])

    ax.set_ylim(0, 560)
    ax.set_ylabel("stock price, indexed")
    ax.set_xlabel("year")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    hgrid(ax)

    fig.tight_layout()
    stamp_bad(fig)
    save(fig, "redundant_coding", "tech_stocks_bad_legend")


if __name__ == "__main__":
    render()
