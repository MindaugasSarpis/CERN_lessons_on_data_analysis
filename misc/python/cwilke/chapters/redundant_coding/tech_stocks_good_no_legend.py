"""Direct-labelled tech stock lines: no legend needed (Wilke fig 20.8)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save


ORDER = ["FB", "GOOG", "MSFT", "AAPL"]
LABELS = {"FB": "Facebook", "GOOG": "Alphabet",
          "MSFT": "Microsoft", "AAPL": "Apple"}
COLOURS = {"FB": "#000000", "GOOG": "#E69F00",
           "MSFT": "#56B4E9", "AAPL": "#009E73"}


def render() -> None:
    apply_base()

    df = D.tech_stocks()

    fig, ax = plt.subplots(figsize=(8.2, 4.4))
    end_x = df["date"].max()
    for ticker in ORDER:
        sub = df[df["ticker"] == ticker].sort_values("date")
        ax.plot(sub["date"], sub["price_indexed"],
                color=COLOURS[ticker], linewidth=1.8)
        ax.text(end_x, sub["price_indexed"].iloc[-1],
                f"  {LABELS[ticker]}",
                color=COLOURS[ticker], va="center", fontsize=10,
                fontweight="bold")

    ax.set_ylim(0, 560)
    ax.set_ylabel("stock price, indexed")
    ax.set_xlabel("year")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    hgrid(ax)

    fig.subplots_adjust(left=0.09, right=0.84, top=0.95, bottom=0.13)
    save(fig, "redundant_coding", "tech_stocks_good_no_legend")


if __name__ == "__main__":
    render()
