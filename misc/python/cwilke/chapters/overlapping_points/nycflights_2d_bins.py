"""EWR departure delays — 2D histogram of flights (Wilke fig 18.6)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save


def render() -> None:
    apply_base()
    df = D.nycflights_delays()

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    h = ax.hist2d(df["departure_time"], df["departure_delay"],
                  bins=[50, 50], cmap="cividis", cmin=1)
    ax.set_xlim(0, 24)
    ax.set_xticks([0, 6, 12, 18, 24])
    ax.set_xticklabels(["0:00", "6:00", "12:00", "18:00", "24:00"])
    ax.set_xlabel("departure time")
    ax.set_ylabel("departure delay (minutes)")
    cb = fig.colorbar(h[3], ax=ax, pad=0.02)
    cb.set_label("departures")
    open_axes(ax)
    save(fig, "overlapping_points", "nycflights_2d_bins")


if __name__ == "__main__":
    render()
