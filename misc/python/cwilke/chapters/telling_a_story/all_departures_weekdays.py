"""Small-multiples NYC weekday-departures matrix (Wilke fig 29.7)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, save


AIRLINES = ["United", "ExpressJet", "JetBlue", "Delta", "American",
            "Endeavor", "Envoy", "US Airways", "Southwest", "other"]
ORIGINS = ["EWR", "JFK", "LGA"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def render() -> None:
    apply_base()

    df = D.nyc_flights_weekdays()
    n_rows, n_cols = len(ORIGINS), len(AIRLINES)

    fig, axes = plt.subplots(n_rows, n_cols,
                             figsize=(13, 4.0),
                             sharey=True, sharex=True)
    for i, origin in enumerate(ORIGINS):
        for j, airline in enumerate(AIRLINES):
            ax = axes[i, j]
            sub = df[(df["name"] == airline) & (df["origin"] == origin)]
            counts = [int(sub[sub["weekday"] == d]["count"].iloc[0])
                      for d in DAYS]
            ax.bar(range(7), counts,
                   color="#0072B2D0", edgecolor="white", linewidth=0.7)
            ax.set_facecolor("#E6E6E6")
            ax.set_ylim(0, 7500)
            ax.grid(True, axis="y", color="white", linewidth=0.7)
            ax.set_axisbelow(True)
            if i == 0:
                ax.set_title(airline, fontsize=10, fontweight="bold")
            if j == 0:
                ax.set_ylabel(origin, fontsize=10, fontweight="bold")
            ax.set_xticks(range(7))
            if i == n_rows - 1:
                ax.set_xticklabels(["M", "", "W", "", "F", "", "S"],
                                   fontsize=8)
            else:
                ax.set_xticklabels([])
            for spine in ("top", "right"):
                ax.spines[spine].set_visible(False)
            ax.tick_params(axis="both", length=0)

    fig.supxlabel("weekday", fontsize=11)
    fig.subplots_adjust(left=0.045, right=0.995, top=0.90,
                        bottom=0.12, wspace=0.1, hspace=0.15)
    save(fig, "telling_a_story", "all_departures_weekdays")


if __name__ == "__main__":
    render()
