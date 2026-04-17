"""Both axis titles omitted — bad (Wilke fig 30.5)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save, stamp_bad


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
    # Both axis titles omitted; reader left guessing
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(loc="upper left", fontsize=10, frameon=False)
    hgrid(ax)

    fig.tight_layout()
    stamp_bad(fig)
    save(fig, "figure_titles_captions", "tech_stocks_minimal_labeling_bad")


if __name__ == "__main__":
    render()
