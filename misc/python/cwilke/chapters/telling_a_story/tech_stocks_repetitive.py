"""Two stacked stock-price line plots — same type of vis twice (Wilke fig 29.10)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save, stamp_ugly


COLOURS = {"FB": "#0072B2", "GOOG": "#000000",
           "AAPL": "#E69F00", "MSFT": "#009E73"}


def render() -> None:
    apply_base()

    df = D.tech_stocks()
    fb = df[df["ticker"] == "FB"].sort_values("date")

    fig, axes = plt.subplots(2, 1, figsize=(7.6, 7.4), sharex=True)

    # (a) raw Facebook price
    ax = axes[0]
    ax.plot(fb["date"], fb["price"], color=COLOURS["FB"], linewidth=1.8)
    last = fb.iloc[-1]
    ax.text(last["date"], last["price"], "  Facebook",
            color=COLOURS["FB"], va="center", fontsize=11,
            fontweight="bold")
    ax.set_ylabel("stock price (USD)")
    ax.set_ylim(0, 155)
    ax.text(0.01, 0.97, "a", transform=ax.transAxes,
            fontsize=14, fontweight="bold", va="top")
    hgrid(ax)

    # (b) indexed price for all four companies
    ax = axes[1]
    end_x = df["date"].max()
    for ticker, col in COLOURS.items():
        sub = df[df["ticker"] == ticker].sort_values("date")
        ax.plot(sub["date"], sub["price_indexed"], color=col, linewidth=1.8)
        name = {"FB": "Facebook", "GOOG": "Alphabet",
                "AAPL": "Apple", "MSFT": "Microsoft"}[ticker]
        ax.text(end_x, sub["price_indexed"].iloc[-1], f"  {name}",
                color=col, va="center", fontsize=10, fontweight="bold")
    ax.set_ylabel("stock price, indexed")
    ax.set_ylim(0, 560)
    ax.set_xlabel("year")
    ax.text(0.01, 0.97, "b", transform=ax.transAxes,
            fontsize=14, fontweight="bold", va="top")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    hgrid(ax)

    fig.subplots_adjust(left=0.09, right=0.84, top=0.97,
                        bottom=0.07, hspace=0.2)
    stamp_ugly(fig)
    save(fig, "telling_a_story", "tech_stocks_repetitive")


if __name__ == "__main__":
    render()
