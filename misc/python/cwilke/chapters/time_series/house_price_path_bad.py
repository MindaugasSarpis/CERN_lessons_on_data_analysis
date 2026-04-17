"""Connected scatter plot without time cues (Wilke fig 13.11, bad)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import PRIMARY_BLUE, apply_base, grid, save, stamp_bad


def render() -> None:
    apply_base()
    df = D.ca_house_unemployment()

    fig, ax = plt.subplots(figsize=(6.6, 4.8))
    ax.plot(df["unemploy_perc"],
            df["house_price_perc"] * 100,
            color=PRIMARY_BLUE, linewidth=1.8, solid_capstyle="round")
    ax.set_xlim(3.5, 14.5)
    ax.set_ylim(-32, 32)
    ax.set_xlabel("unemployment rate (%)")
    ax.set_ylabel("12-month change in house prices (%)")
    grid(ax)
    stamp_bad(fig)
    save(fig, "time_series", "house_price_path_bad")


if __name__ == "__main__":
    render()
