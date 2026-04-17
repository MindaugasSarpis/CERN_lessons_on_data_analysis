"""Tufte-style horizontal bars: white lines cut across bars (Wilke fig 23.12)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, save


LABELS = {"FB": "Facebook", "GOOG": "Alphabet",
          "MSFT": "Microsoft", "AAPL": "Apple"}


def render() -> None:
    apply_base()
    df = D.tech_stocks().copy()
    last = df.sort_values("date").groupby("ticker").tail(1).copy()
    last["perc"] = (last["price"] / last["index_price"] - 1) * 100
    last = last.sort_values("perc", ascending=True)

    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    labels = [LABELS[t] for t in last["ticker"]]
    ax.barh(labels, last["perc"], color=PRIMARY_BLUE, height=0.78,
            zorder=2)
    # White ticks cutting across bars at 100 / 200 / 300 / 400 %
    for x in (100, 200, 300, 400):
        ax.axvline(x, color="white", linewidth=1.5, zorder=3)
    # Percent labels just outside each bar
    for label, perc in zip(labels, last["perc"]):
        ax.text(perc + 4, label, f"{int(round(perc))}%",
                va="center", ha="left", color="#2c3e50", fontsize=11)
    ax.set_xlim(0, max(last["perc"]) * 1.15)
    ax.set_xticks([])
    ax.set_xlabel("")
    for sp in ("top", "right", "bottom", "left"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="y", length=0)

    fig.tight_layout()
    save(fig, "balance_data_context", "price_increase_tufte")


if __name__ == "__main__":
    render()
