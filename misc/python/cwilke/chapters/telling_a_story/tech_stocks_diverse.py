"""Raw price line + percent-increase bar: diversified visuals (Wilke fig 29.11)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save, vgrid


def render() -> None:
    apply_base()

    df = D.tech_stocks()
    fb = df[df["ticker"] == "FB"].sort_values("date")

    fig = plt.figure(figsize=(7.6, 7.4))
    gs = fig.add_gridspec(2, 1, hspace=0.3)

    ax1 = fig.add_subplot(gs[0])
    ax1.plot(fb["date"], fb["price"], color="#0072B2", linewidth=1.8)
    last = fb.iloc[-1]
    ax1.text(last["date"], last["price"], "  Facebook",
             color="#0072B2", va="center", fontsize=11, fontweight="bold")
    ax1.set_ylabel("stock price (USD)")
    ax1.set_ylim(0, 155)
    ax1.set_xlabel("year")
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax1.text(0.01, 0.97, "a", transform=ax1.transAxes,
             fontsize=14, fontweight="bold", va="top")
    hgrid(ax1)

    # (b) percent increase bar
    tickers = ["FB", "GOOG", "AAPL", "MSFT"]
    labels = {"FB": "Facebook", "GOOG": "Alphabet",
              "AAPL": "Apple", "MSFT": "Microsoft"}
    pct = []
    for t in tickers:
        sub = df[df["ticker"] == t]
        first = sub["price"].iloc[0]
        lastp = sub["price"].iloc[-1]
        pct.append((t, 100 * (lastp - first) / first))
    pct.sort(key=lambda p: p[1])

    ax2 = fig.add_subplot(gs[1])
    names = [labels[t] for t, _ in pct]
    vals = [v for _, v in pct]
    colours = ["#0072B2D0" if t == "FB" else "#808080D0"
               for t, _ in pct]
    ax2.barh(names, vals, color=colours,
             edgecolor="white", linewidth=0.4)
    for i, v in enumerate(vals):
        ax2.text(v * 0.98, i, f"{int(round(v))}%",
                 va="center", ha="right",
                 color="white", fontsize=11, fontweight="bold")
    ax2.set_xlabel("percent increase")
    ax2.set_xlim(0, 499)
    ax2.text(0.01, 0.97, "b", transform=ax2.transAxes,
             fontsize=14, fontweight="bold", va="top")
    vgrid(ax2)

    fig.subplots_adjust(left=0.12, right=0.92, top=0.97, bottom=0.08)
    save(fig, "telling_a_story", "tech_stocks_diverse")


if __name__ == "__main__":
    render()
