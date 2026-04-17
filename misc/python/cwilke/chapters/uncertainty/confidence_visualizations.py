"""Six-panel comparison of uncertainty visualisations (Wilke fig 16.9).

(a) graded error bars with caps
(b) single error bar with caps
(c) graded error bars without caps
(d) single error bar without caps
(e) confidence strip (density)
(f) confidence distribution (ridgeline-like)
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t as student_t

from cwilke.data import cacao_ratings
from cwilke.theme import apply_base, hgrid, save


def _contrasts():
    df = cacao_ratings()
    us = df[df["location"] == "US"]["rating"].values
    us_mean = us.mean()
    us_var = us.var(ddof=1)
    us_n = len(us)
    out = []
    for c in ["Austria", "Belgium", "Canada", "Peru"]:
        vals = df[df["location"] == c]["rating"].values
        n = len(vals)
        diff = vals.mean() - us_mean
        se = np.sqrt(vals.var(ddof=1) / n + us_var / us_n)
        dof = n + us_n - 2
        cis = {
            "99%": (diff - student_t.ppf(0.995, dof) * se,
                    diff + student_t.ppf(0.995, dof) * se),
            "95%": (diff - student_t.ppf(0.975, dof) * se,
                    diff + student_t.ppf(0.975, dof) * se),
            "80%": (diff - student_t.ppf(0.90, dof) * se,
                    diff + student_t.ppf(0.90, dof) * se),
        }
        out.append((c, diff, se, cis))
    out.sort(key=lambda r: r[1])
    return out


def _graded(ax, rows, caps):
    colors = {"99%": "#9fc1dd", "95%": "#4a87b3", "80%": "#0f4c75"}
    widths = {"99%": 1.0,       "95%": 1.7,       "80%": 2.5}
    ax.axvline(0, color="gray", linestyle="--", linewidth=0.8)
    for y, (c, diff, se, cis) in enumerate(rows):
        for lev in ("80%", "95%", "99%"):
            lo, hi = cis[lev]
            ax.hlines(y, lo, hi, colors=colors[lev], linewidth=widths[lev])
            if caps:
                cap_color = colors[lev]
                cap_h = 0.14
                ax.vlines([lo, hi], y - cap_h, y + cap_h,
                          colors=cap_color, linewidth=widths[lev])
        ax.plot(diff, y, "o", color="#D55E00", markersize=5)


def _single(ax, rows, caps):
    ax.axvline(0, color="gray", linestyle="--", linewidth=0.8)
    for y, (c, diff, se, cis) in enumerate(rows):
        lo, hi = cis["95%"]
        ax.hlines(y, lo, hi, colors="#2c3e50", linewidth=1.2)
        if caps:
            ax.vlines([lo, hi], y - 0.15, y + 0.15,
                      colors="#2c3e50", linewidth=1.2)
        ax.plot(diff, y, "o", color="#D55E00", markersize=6)


def _strip(ax, rows):
    ax.axvline(0, color="gray", linestyle="--", linewidth=0.8)
    xg = np.linspace(-0.8, 0.5, 200)
    for y, (c, diff, se, cis) in enumerate(rows):
        # draw semi-transparent strip that fades out
        dens = norm.pdf(xg, diff, se)
        dens = dens / dens.max()
        for i in range(len(xg) - 1):
            ax.fill_betweenx(
                [y - 0.35, y + 0.35],
                xg[i], xg[i + 1],
                color="#3a6fa3", alpha=float(dens[i]) * 0.6,
                linewidth=0,
            )
        ax.plot(diff, y, "|", color="#D55E00", markersize=16, mew=2)


def _distro(ax, rows):
    ax.axvline(0, color="gray", linestyle="--", linewidth=0.8)
    xg = np.linspace(-0.8, 0.5, 300)
    for y, (c, diff, se, cis) in enumerate(rows):
        dens = norm.pdf(xg, diff, se)
        dens = 0.6 * dens / dens.max()
        ax.fill_between(xg, y, y + dens,
                         color="#81A7D6", alpha=0.7, linewidth=0.4,
                         edgecolor="#0f4c75")
        ax.plot(diff, y, "|", color="#D55E00", markersize=16, mew=2)


def render() -> None:
    apply_base()
    rows = _contrasts()
    labels = [r[0] for r in rows]
    fig, axes = plt.subplots(3, 2, figsize=(9.0, 6.8), sharex=True)
    ((ax_a, ax_b), (ax_c, ax_d), (ax_e, ax_f)) = axes

    for ax in axes.flatten():
        hgrid(ax)
        ax.set_yticks(np.arange(len(rows)))
        ax.set_yticklabels(labels)
        ax.set_xlim(-0.75, 0.45)

    _graded(ax_a, rows, caps=True)
    ax_a.set_title("(a) graded, caps", loc="left", fontsize=10)
    _single(ax_b, rows, caps=True)
    ax_b.set_title("(b) single, caps", loc="left", fontsize=10)
    _graded(ax_c, rows, caps=False)
    ax_c.set_title("(c) graded, no caps", loc="left", fontsize=10)
    _single(ax_d, rows, caps=False)
    ax_d.set_title("(d) single, no caps", loc="left", fontsize=10)
    _strip(ax_e, rows)
    ax_e.set_title("(e) confidence strip", loc="left", fontsize=10)
    _distro(ax_f, rows)
    ax_f.set_title("(f) confidence distribution", loc="left", fontsize=10)

    for ax in (ax_e, ax_f):
        ax.set_xlabel("difference in mean rating")

    fig.tight_layout()
    save(fig, "uncertainty", "confidence_visualizations")


if __name__ == "__main__":
    render()
