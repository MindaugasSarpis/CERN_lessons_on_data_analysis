"""EWR departure delays — raw scatter with alpha (Wilke fig 18.5, bad)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save, stamp_bad


def render() -> None:
    apply_base()
    df = D.nycflights_delays()

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.axhline(0, color="#b0bec5", linewidth=0.8)
    ax.scatter(df["departure_time"], df["departure_delay"],
               s=6, color="black", alpha=0.1, edgecolors="none")
    ax.set_xlim(0, 24)
    ax.set_xticks([0, 6, 12, 18, 24])
    ax.set_xticklabels(["0:00", "6:00", "12:00", "18:00", "24:00"])
    ax.set_xlabel("departure time")
    ax.set_ylabel("departure delay (minutes)")
    open_axes(ax)
    stamp_bad(fig)
    save(fig, "overlapping_points", "nycflights_points")


if __name__ == "__main__":
    render()
