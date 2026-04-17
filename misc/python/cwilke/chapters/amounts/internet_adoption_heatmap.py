"""Heatmap of internet adoption by country and year (Wilke fig 6.16).

Rows are countries sorted by current internet adoption; columns are
years. Colour encodes % of the population online. Heatmaps are the
natural choice when you have many groups × many time points and no
single line plot would be readable.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import apply_base, save


# Plausible adoption curves, % internet users, 1994..2016 inclusive (23 yrs)
# for ~15 countries. Hand-drawn numbers — illustrative, not research-grade.
_COUNTRIES = [
    "Iceland", "Norway", "Canada", "UK", "Germany", "Japan",
    "USA", "France", "Israel", "Italy", "Argentina", "Chile",
    "Brazil", "China", "Mexico", "South Africa", "Algeria", "India",
    "Kenya",
]

def _curve(start_year: int, ceiling: float, steepness: float,
           years: np.ndarray) -> np.ndarray:
    out = ceiling / (1 + np.exp(-steepness * (years - start_year)))
    return np.clip(out, 0, 100)


def render() -> None:
    apply_base()
    years = np.arange(1994, 2017)

    # (country, adoption_start_year, plateau, steepness)
    params = {
        "Iceland":      (1996, 98, 0.65),
        "Norway":       (1996, 97, 0.60),
        "Canada":       (1996, 92, 0.55),
        "UK":           (1997, 94, 0.50),
        "Germany":      (1997, 90, 0.48),
        "Japan":        (1997, 93, 0.50),
        "USA":          (1995, 88, 0.48),
        "France":       (1999, 85, 0.45),
        "Israel":       (1999, 79, 0.42),
        "Italy":        (2000, 72, 0.38),
        "Argentina":    (2001, 71, 0.36),
        "Chile":        (2002, 66, 0.34),
        "Brazil":       (2002, 62, 0.32),
        "China":        (2003, 53, 0.30),
        "Mexico":       (2003, 60, 0.28),
        "South Africa": (2005, 54, 0.25),
        "Algeria":      (2005, 42, 0.25),
        "India":        (2007, 30, 0.22),
        "Kenya":        (2008, 26, 0.22),
    }

    rng = np.random.default_rng(1)
    data = []
    for country in _COUNTRIES:
        start, ceil, steep = params[country]
        c = _curve(start, ceil, steep, years)
        # Add slight noise to look less synthetic.
        c = np.clip(c + rng.normal(0, 1.5, c.size), 0, 100)
        data.append(c)

    data = np.array(data)

    # Sort by final (2016) value so most-adopted is on top.
    order = np.argsort(data[:, -1])
    data = data[order]
    countries = [_COUNTRIES[i] for i in order]

    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    im = ax.imshow(data, aspect="auto", cmap="magma",
                    vmin=0, vmax=100, origin="lower",
                    extent=(years[0] - 0.5, years[-1] + 0.5,
                            -0.5, len(countries) - 0.5))
    ax.set_yticks(range(len(countries)))
    ax.set_yticklabels(countries)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.set_xticks([1995, 2000, 2005, 2010, 2015])
    cbar = fig.colorbar(im, ax=ax, orientation="horizontal",
                         fraction=0.045, pad=0.12)
    cbar.set_label("internet users / 100 people")
    cbar.ax.xaxis.set_ticks_position("bottom")
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", length=0)
    for sp in ("top", "right", "left", "bottom"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout()
    save(fig, "amounts", "internet_adoption_heatmap")


if __name__ == "__main__":
    render()
