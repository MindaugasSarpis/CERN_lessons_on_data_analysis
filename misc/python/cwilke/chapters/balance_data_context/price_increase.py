"""5-year % increase for four tech stocks — horizontal bars with vgrid (Wilke fig 23.11)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, save, vgrid


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
    ax.barh(labels, last["perc"], color=PRIMARY_BLUE, height=0.7)
    for label, perc in zip(labels, last["perc"]):
        ax.text(perc - 8, label, f"{int(round(perc))}%",
                va="center", ha="right", color="white", fontsize=11)
    ax.set_xlabel("percent increase")
    ax.set_xlim(0, max(last["perc"]) * 1.08)
    vgrid(ax)

    fig.tight_layout()
    save(fig, "balance_data_context", "price_increase")


if __name__ == "__main__":
    render()
