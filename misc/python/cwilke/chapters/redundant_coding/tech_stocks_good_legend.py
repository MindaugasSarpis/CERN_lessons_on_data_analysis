"""Tech stock prices; legend reordered to match visual order (Wilke fig 20.6)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save


# Top-to-bottom visual order at the end of the series
ORDER = ["FB", "GOOG", "MSFT", "AAPL"]
LABELS = {"FB": "Facebook", "GOOG": "Alphabet",
          "MSFT": "Microsoft", "AAPL": "Apple"}
COLOURS = {"FB": "#000000", "GOOG": "#E69F00",
           "MSFT": "#56B4E9", "AAPL": "#009E73"}


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
    save(fig, "redundant_coding", "tech_stocks_good_legend")


if __name__ == "__main__":
    render()
