"""Three biomedical preprint servers — lines with direct labels
(Wilke fig 13.7)."""

from __future__ import annotations

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from cwilke import data as D
from cwilke.theme import apply_base, open_axes, save


COLORS = {"bioRxiv": "#0072B2", "arXiv q-bio": "#D55E00",
          "PeerJ Preprints": "#009E73"}


def render() -> None:
    apply_base()
    df = D.preprints_three()
    df = df[df["date"] <= "2017-01-01"]

    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    end_label_x = df["date"].max()
    for arch in ("bioRxiv", "arXiv q-bio", "PeerJ Preprints"):
        sub = df[df["archive"] == arch].sort_values("date")
        ax.plot(sub["date"], sub["count"], color=COLORS[arch], linewidth=1.8)
        # direct label at the right end.
        last = sub.iloc[-1]
        ax.text(end_label_x, last["count"], f"  {arch}",
                color=COLORS[arch], va="center", fontsize=10)
    ax.set_xlim(df["date"].min(), end_label_x)
    ax.set_ylim(0, 600)
    ax.set_ylabel("preprints / month")
    ax.set_xlabel("year")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    open_axes(ax)
    save(fig, "time_series", "bio_preprints_direct_label")


if __name__ == "__main__":
    render()
