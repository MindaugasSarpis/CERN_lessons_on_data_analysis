"""Overly complex scatter: delay vs distance coloured by airline (Wilke fig 29.3, bad)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from cwilke.theme import apply_base, grid, save, stamp_bad


AIRLINE_COLOURS = {
    "American": "#56B4E9",
    "Delta":    "#E69F00",
    "other":    "#999999",
}


def _synth_destinations(seed: int = 11):
    rng = np.random.default_rng(seed)
    n_dest = 100
    dist = rng.uniform(150, 3050, n_dest)
    rows = []
    for d in dist:
        base = 3 + 0.0025 * d
        for airline in AIRLINE_COLOURS:
            shift = {"American": -1.5, "Delta": -2.5, "other": 2.5}[airline]
            if rng.random() < (0.6 if airline == "other" else 0.25):
                delay = base + shift + rng.normal(0, 4)
                count = int(rng.uniform(200, 12000))
                rows.append({"name": airline, "distance": d,
                             "arr_delay": delay, "count": count})
    return rows


def render() -> None:
    apply_base()

    rows = _synth_destinations()
    fig, ax = plt.subplots(figsize=(8.2, 5.0))

    for airline, col in AIRLINE_COLOURS.items():
        sub = [r for r in rows if r["name"] == airline]
        xs = [r["distance"] for r in sub]
        ys = [r["arr_delay"] for r in sub]
        ss = [max(25, r["count"] / 80) for r in sub]
        ax.scatter(xs, ys, s=ss, color=col + "80",
                   edgecolor=col, linewidth=0.8, label=airline)

        # trend line (simple mean in two bins)
        xs_arr = np.array(xs)
        ys_arr = np.array(ys)
        if len(xs_arr) > 8:
            order = xs_arr.argsort()
            xs_s, ys_s = xs_arr[order], ys_arr[order]
            window = max(5, len(xs_s) // 6)
            trend_y = np.convolve(ys_s, np.ones(window) / window,
                                  mode="valid")
            # trend_x aligned with centre of each window
            trend_x = xs_s[(window - 1) // 2:
                            (window - 1) // 2 + len(trend_y)]
            ax.plot(trend_x, trend_y, color=col, linewidth=1.4, alpha=0.8)

    ax.set_xlim(0, 3050)
    ax.set_xlabel("distance (miles)")
    ax.set_ylabel("mean arrival delay (min.)")
    ax.legend(title="airline", loc="upper right",
              fontsize=9, title_fontsize=10, frameon=False)
    grid(ax)

    fig.tight_layout()
    stamp_bad(fig)
    save(fig, "telling_a_story", "arrival_delay_vs_distance_bad")


if __name__ == "__main__":
    render()
