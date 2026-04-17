"""Mauna Loa CO2 — the Keeling curve (Wilke fig 14.13)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save


def render() -> None:
    apply_base()
    df = D.keeling_curve()

    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    ax.plot(df["date_dec"], df["co2"], color=PRIMARY_BLUE, linewidth=1.0)
    ax.set_ylabel("CO$_2$ concentration (ppm)")
    ax.set_xlim(1958, 2019)
    ax.set_ylim(295, 418)
    grid(ax)
    save(fig, "trends", "keeling_curve")


if __name__ == "__main__":
    render()
