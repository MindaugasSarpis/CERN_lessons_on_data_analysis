"""Movie-length ridgeline across decades (Wilke fig 9.13).

Demonstrates ridgelines scale to many distributions — here one per year
from 1920 to 2000. Tells the story of movies standardising at ~90 min.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke.theme import apply_base, open_axes, save


def _synth_lengths(rng: np.random.Generator, year: int) -> np.ndarray:
    """Generate ~60 film lengths that reflect the decade's conventions."""
    n = 60
    if year < 1930:
        # Early cinema: bimodal — shorts (40 min) and long features (110 min).
        shorts = rng.normal(45, 10, n // 2)
        longs = rng.normal(115, 18, n - n // 2)
        return np.concatenate([shorts, longs])
    elif year < 1960:
        # Golden era — features average ~95 min.
        return rng.normal(95, 14, n)
    else:
        # Standardised around 90-100 min with a tight distribution.
        return rng.normal(95, 8, n)


def render() -> None:
    apply_base()
    rng = np.random.default_rng(9)

    years = np.arange(1920, 2005, 5)
    xs = np.linspace(20, 200, 400)

    densities = []
    for y in years:
        data = _synth_lengths(rng, y).clip(20, 200)
        kde = gaussian_kde(data, bw_method=0.25)
        densities.append(kde(xs))
    peak = max(d.max() for d in densities)
    offset_step = peak * 0.9

    fig, ax = plt.subplots(figsize=(6.6, 7.4))
    # Draw oldest at the top for a "years running downward" aesthetic.
    for i, (y, d) in enumerate(zip(years, densities)):
        base = (len(years) - 1 - i) * offset_step
        ax.fill_between(xs, base, base + d,
                         color="#cfd8dc", alpha=0.85, linewidth=0)
        ax.plot(xs, base + d, color="#2c3e50", linewidth=0.7)

    # Label every 20 years.
    tick_years = [1920, 1940, 1960, 1980, 2000]
    tick_positions = [(len(years) - 1 - list(years).index(ty)) * offset_step
                       for ty in tick_years]
    ax.set_yticks(tick_positions)
    ax.set_yticklabels(tick_years)

    ax.set_xlim(20, 200)
    ax.set_xlabel("length (minutes)")
    ax.set_ylabel("year")
    open_axes(ax)
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    save(fig, "distributions_ii", "movies_ridgeline")


if __name__ == "__main__":
    render()
