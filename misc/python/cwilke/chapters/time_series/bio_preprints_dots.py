"""Three biomedical preprint servers — dots only (Wilke fig 13.5, bad)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save, stamp_bad


COLORS = {"bioRxiv": "#0072B2", "arXiv q-bio": "#D55E00",
          "PeerJ Preprints": "#009E73"}
MARKERS = {"bioRxiv": "o", "arXiv q-bio": "s", "PeerJ Preprints": "D"}


def render() -> None:
    apply_base()
    df = D.preprints_three()
    df = df[df["date"] <= "2017-01-01"]

    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    for arch in ("bioRxiv", "arXiv q-bio", "PeerJ Preprints"):
        sub = df[df["archive"] == arch]
        ax.scatter(sub["date"], sub["count"], s=36,
                   marker=MARKERS[arch], facecolors=COLORS[arch],
                   edgecolors="white", linewidths=0.6, label=arch)
    ax.set_ylim(0, 600)
    ax.set_ylabel("preprints / month")
    ax.set_xlabel("year")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(loc="upper left", frameon=False)
    open_axes(ax)
    stamp_bad(fig)
    save(fig, "time_series", "bio_preprints_dots")


if __name__ == "__main__":
    render()
