"""Ridgeline plot of shifting distributions (Wilke fig 9.17).

Stacked density curves, each offset vertically, let the eye compare the
shapes and locations of many distributions in a compact space — more
informative than a grid of histograms once there are more than a handful
of groups.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

from cwilke.theme import OKABE_ITO, apply_base, open_axes, save


def render() -> None:
    apply_base()
    rng = np.random.default_rng(11)

    # Five distributions: shifting means, slightly varying widths.
    n = 400
    groups = [
        ("Group A", rng.normal(0.0, 1.0, n)),
        ("Group B", rng.normal(0.8, 1.1, n)),
        ("Group C", rng.normal(1.7, 0.9, n)),
        ("Group D", rng.normal(2.6, 1.2, n)),
        ("Group E", rng.normal(3.5, 1.0, n)),
    ]

    # Evaluate every KDE on a shared grid so we can stack them cleanly.
    lo = min(g.min() for _, g in groups) - 0.5
    hi = max(g.max() for _, g in groups) + 0.5
    xs = np.linspace(lo, hi, 400)

    densities = [gaussian_kde(vals)(xs) for _, vals in groups]
    peak = max(d.max() for d in densities)
    offset_step = peak * 0.55  # controls overlap

    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    # Draw from bottom (last group) to top (first) so later layers paint over earlier.
    for i, ((label, _), dens) in reversed(list(enumerate(zip(groups, densities)))):
        base = i * offset_step
        color = OKABE_ITO[(i % (len(OKABE_ITO) - 1)) + 1]
        ax.fill_between(xs, base, base + dens, color=color, alpha=0.82,
                        linewidth=0)
        ax.plot(xs, base + dens, color="white", linewidth=1.1)

    labels = [g[0] for g in groups]
    ax.set_yticks([i * offset_step for i in range(len(groups))])
    ax.set_yticklabels(labels)
    ax.set_xlabel("value")
    ax.set_title("Ridgeline plot · five shifting distributions")
    open_axes(ax)
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    save(fig, "distributions_ii", "ridgeline")


if __name__ == "__main__":
    render()
