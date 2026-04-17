"""Single facet of NYC weekday-departures plot (Wilke fig 29.6)."""

from __future__ import annotations

import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, hgrid, save


DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def render() -> None:
    apply_base()

    df = D.nyc_flights_weekdays()
    sub = df[(df["name"] == "United") & (df["origin"] == "EWR")]
    counts = [int(sub[sub["weekday"] == d]["count"].iloc[0]) for d in DAYS]

    fig, ax = plt.subplots(figsize=(4.2, 4.0))
    ax.bar(range(7), counts,
           color="#0072B2D0", edgecolor="white", linewidth=1.2)
    ax.set_xticks(range(7))
    ax.set_xticklabels(["M", "T", "W", "T", "F", "S", "S"])
    ax.set_title("United departures, EWR", fontsize=12)
    ax.set_ylim(0, 7500)
    ax.set_xlabel("weekday")
    hgrid(ax)

    fig.tight_layout()
    save(fig, "telling_a_story", "united_departures_weekdays")


if __name__ == "__main__":
    render()
