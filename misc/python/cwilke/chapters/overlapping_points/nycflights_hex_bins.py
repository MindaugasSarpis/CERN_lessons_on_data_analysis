"""EWR departure delays — hexagonal binning (Wilke fig 18.7)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.nycflights_delays()

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    hb = ax.hexbin(df["departure_time"], df["departure_delay"],
                   gridsize=50, cmap="cividis", mincnt=1)
    ax.set_xlim(0, 24)
    ax.set_xticks([0, 6, 12, 18, 24])
    ax.set_xticklabels(["0:00", "6:00", "12:00", "18:00", "24:00"])
    ax.set_xlabel("departure time")
    ax.set_ylabel("departure delay (minutes)")
    cb = fig.colorbar(hb, ax=ax, pad=0.02)
    cb.set_label("departures")
    open_axes(ax)
    save(fig, "overlapping_points", "nycflights_hex_bins")


if __name__ == "__main__":
    render()
