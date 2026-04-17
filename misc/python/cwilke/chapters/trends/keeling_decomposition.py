"""Keeling curve decomposition: trend, seasonal, remainder
(Wilke fig 14.14)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.keeling_curve()
    df = df[df["date_dec"] >= 1989].copy()

    fig, axes = plt.subplots(4, 1, figsize=(8.6, 8.0), sharex=True)
    titles = ["monthly average", "long-term trend",
              "seasonal fluctuations", "remainder"]
    series = [df["co2"], df["trend"], df["seasonal"], df["remainder"]]
    for ax, title, s in zip(axes, titles, series):
        ax.plot(df["date_dec"], s, color=PRIMARY_BLUE, linewidth=1.0)
        ax.set_title(title, loc="left", fontsize=11)
        ax.set_ylabel("CO$_2$ (ppm)")
        grid(ax)
    axes[-1].set_xlabel("year")
    fig.tight_layout()
    save(fig, "trends", "keeling_decomposition")


if __name__ == "__main__":
    render()
