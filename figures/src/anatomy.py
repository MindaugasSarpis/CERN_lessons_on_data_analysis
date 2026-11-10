"""Anatomy of a scientific figure: the yearly temperature cycle of the weather
log, built part by part for a v-click slide (Lecture 7, "The Parts of a
Figure").

The data are the 87 552 measured hours of weather.csv (2016-2025), read with
the lecture's functions (handson.py):

  * the points: the mean of all hours of each calendar month, drawn at the
    middle of the month (t in months of 365.25 / 12 days since 1 January:
    15.5 days = 0.51 for January, 2.46 for March after the short February);
  * the error bars: the standard error of each monthly mean, s / sqrt(10),
    s the scatter of the ten yearly means of that month;
  * the curve: T(t) = c - A cos(2 pi (t - t0) / 12), a weighted least-squares
    (chi2) fit to the twelve points, so t0 is the coldest time of the year
    (Lecture 9's convention; its fit to the 3648 daily means gives
    c = 7.18, A = 11.18, coldest on 16 January);
  * the residual panel: the pulls (data - fit) / sigma.

Seven stages of IDENTICAL geometry (fixed margins, a solid canvas), each
stage adding its parts: the frame; the data points; the error bars; the
fitted curve and the fit box; the reference line, the annotation, the legend
and the title; the residual panel; callouts naming each part.

Every number on the figure is computed here. Print them with

    python figures/src/anatomy.py
"""
from datetime import date, timedelta

import numpy as np

import style
from handson import MISSING, PATH, read_lines

MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
MONTH_DAYS = np.array([31, 28.25, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])  # 365.25
DAYS_PER_MONTH = 365.25 / 12
EDGES = np.concatenate([[0], MONTH_DAYS.cumsum()]) / DAYS_PER_MONTH  # month starts, t
T_MID = (EDGES[:-1] + EDGES[1:]) / 2  # the middle of each month, in months since 1 January
OMEGA = 2 * np.pi / 12                # one cycle per twelve months
NAME = "viz_anatomy_stage{}"
N_STAGES = 7

_CACHE = {}


def monthly():
    """The twelve monthly means of all valid hours, the ten yearly means of
    each month, and the standard error s / sqrt(10) of each monthly mean."""
    sums, counts = {}, {}
    for line in read_lines(PATH):
        stamp, temp = line.split(",")[:2]
        temp = float(temp)
        if temp == MISSING:
            continue
        key = (int(stamp[:4]), int(stamp[5:7]))
        sums[key] = sums.get(key, 0.0) + temp
        counts[key] = counts.get(key, 0) + 1
    years = sorted({y for y, _ in counts})
    means = np.array([sum(sums[y, m] for y in years) / sum(counts[y, m] for y in years)
                      for m in range(1, 13)])
    yearly = np.array([[sums[y, m] / counts[y, m] for y in years] for m in range(1, 13)])
    s = yearly.std(axis=1, ddof=1)
    hours = sum(counts.values())
    total = sum(sums.values()) / hours
    return dict(years=years, means=means, yearly=yearly, s=s, se=s / np.sqrt(len(years)),
                hours=hours, mean_all=total)


def model(t, c, amp, t0):
    return c - amp * np.cos(OMEGA * (t - t0))


def fit(t, y, sigma):
    """Weighted least squares for y = c + alpha cos(wt) + beta sin(wt), turned
    into c, A, t0 with their uncertainties (sigma taken as known)."""
    X = np.column_stack([np.ones_like(t), np.cos(OMEGA * t), np.sin(OMEGA * t)])
    w = 1 / sigma ** 2
    V = np.linalg.inv(X.T @ (X * w[:, None]))
    c, al, be = V @ (X.T @ (w * y))
    amp = np.hypot(al, be)
    # c - A cos(w (t - t0)): alpha = -A cos(w t0), beta = -A sin(w t0)
    t0 = (np.arctan2(-be, -al) / OMEGA) % 12
    J = np.array([[1, 0, 0],
                  [0, al / amp, be / amp],
                  [0, -be / (OMEGA * amp ** 2), al / (OMEGA * amp ** 2)]])
    err = np.sqrt(np.diag(J @ V @ J.T))
    pulls = (y - model(t, c, amp, t0)) / sigma
    return dict(c=c, amp=amp, t0=t0, sc=err[0], samp=err[1], st0=err[2], pulls=pulls,
                chi2=(pulls ** 2).sum(), ndf=len(t) - 3)


def day_label(t):
    """A time in months since 1 January as a day of the year, '18 Jan'."""
    d = date(2025, 1, 1) + timedelta(days=float(t) * DAYS_PER_MONTH)
    return f"{d.day} {MONTHS[d.month - 1]}"


def numbers():
    if not _CACHE:
        m = monthly()
        _CACHE.update(m, fit=fit(T_MID, m["means"], m["se"]))
    return _CACHE


def minus(s: str) -> str:
    return s.replace("-", style.MINUS)


# ---------------------------------------------------------------------------
# The figure
# ---------------------------------------------------------------------------

# The canvas, in inches: the box of the slide (sizes.json), else this.
W, H = style.SIZES.get(NAME.format(1), (9.64, 4.03))
LEFT, RIGHT, TOP = 0.74, 0.16, 0.45     # margins around the panels (in)
RES_H, MAIN_BOTTOM = 0.66, 1.28         # residual panel height, main panel bottom (in)
YLIM, PULL_LIM = (-8, 22), (-3, 3)
MS = 4                                  # markers: an error bar of 0.34 degC still shows


def _box(bottom, height):
    return [LEFT / W, bottom / H, (W - LEFT - RIGHT) / W, height / H]


def _month_axis(ax, labels: bool):
    from matplotlib.ticker import FixedLocator
    ax.set_xlim(0, 12)
    ax.set_xticks(T_MID, MONTHS if labels else [])      # major: mid-month
    ax.xaxis.set_minor_locator(FixedLocator(EDGES))     # minor: where a month starts
    ax.tick_params(axis="x", labelbottom=labels)
    if labels:
        ax.set_xlabel("month")


def _stage(n: int):
    """Build the figure up to stage n (1..7) and save viz_anatomy_stage{n}.

    The stages are stacked as v-click layers on the slide, so each is an
    OPAQUE canvas of identical geometry: the panels are placed by hand (no
    constrained layout, no tight bbox), so every part sits at the same pixel
    in every stage, and a solid background makes stage n cover stage n-1.
    Until the residual panel comes (stage 6) the main panel carries the
    month labels itself."""
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MultipleLocator

    d = numbers()
    f = d["fit"]
    fg, dim, bg = style.FG, style.DIM, style.BG

    fig = plt.figure(figsize=(W, H), layout="none")
    ax = fig.add_axes(_box(MAIN_BOTTOM, H - TOP - MAIN_BOTTOM))
    ax.set_ylim(*YLIM)
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.set_ylabel("temperature (°C)")
    _month_axis(ax, labels=n < 6)
    parts = dict(ax=ax)

    if n >= 2:      # the data points
        parts["points"], = ax.plot(T_MID, d["means"], "o", ms=MS, color=fg, zorder=4)
    if n >= 3:      # their error bars
        parts["bars"] = ax.errorbar(T_MID, d["means"], yerr=d["se"], fmt="none", ecolor=fg,
                                    capsize=2.5, zorder=3)
    if n >= 4:      # the fitted curve and the fit result
        tt = np.linspace(0, 12, 400)
        parts["curve"], = ax.plot(tt, model(tt, f["c"], f["amp"], f["t0"]),
                                  color=style.CYCLE[1], zorder=2)
        parts["box"] = ax.annotate(
            "\n".join([
                rf"$c = {f['c']:.2f} \pm {f['sc']:.2f}$ °C",
                rf"$A = {f['amp']:.2f} \pm {f['samp']:.2f}$ °C",
                rf"$t_0 = {f['t0']:.2f} \pm {f['st0']:.2f}$ month",
                rf"$\chi^2/\mathrm{{ndf}} = {f['chi2']:.1f}\,/\,{f['ndf']}$",
            ]),
            xy=(1, 1), xycoords="axes fraction", xytext=(-12, -12), textcoords="offset points",
            ha="right", va="top", multialignment="left", linespacing=1.25, zorder=6,
            bbox=dict(boxstyle="square,pad=0.35", facecolor=bg, edgecolor=dim, linewidth=0.8))
    if n >= 5:      # reference line, annotation, legend, title
        parts["ref"] = ax.axhline(d["mean_all"], color=dim, lw=1.2, ls=(0, (5, 3)), zorder=1)
        lo = f["c"] - f["amp"]
        parts["note"] = ax.annotate(
            minus(f"fitted minimum: {day_label(f['t0'])}, {lo:.1f} °C"),
            xy=(f["t0"] + 0.09, lo - 0.5), xytext=(1.45, -6.4), color=fg, fontsize=11,
            ha="left", va="center",
            arrowprops=dict(arrowstyle="-|>,head_length=0.45,head_width=0.2", color=fg,
                            lw=0.9, shrinkA=2, shrinkB=0, relpos=(0, 0.5),
                            connectionstyle="arc3,rad=-0.25"))
        parts["legend"] = ax.legend(
            [(parts["bars"], parts["points"]), parts["curve"], parts["ref"]],
            [r"monthly mean, error bar $s/\sqrt{10}$ (ten years)",
             r"fit $c - A\,\cos\,[2\pi(t - t_0)/12]$",
             f"mean of all hours, {d['mean_all']:.2f} °C"],
            loc="upper left", bbox_to_anchor=(0.006, 0.985), borderaxespad=0.2,
            handlelength=2.2)
        parts["title"] = ax.set_title("All twelve monthly means lie on one cosine, "
                                      "within their error bars")
    if n >= 6:      # the residual panel
        rax = fig.add_axes(_box(MAIN_BOTTOM - RES_H, RES_H), sharex=ax)
        _month_axis(rax, labels=True)
        rax.set_ylim(*PULL_LIM)
        rax.yaxis.set_major_locator(MultipleLocator(2))
        rax.yaxis.set_minor_locator(MultipleLocator(1))
        rax.axhline(0, color=dim, lw=0.9, zorder=1)
        rax.plot(T_MID, f["pulls"], "o", ms=MS, color=fg, zorder=4)
        rax.set_ylabel("(data − fit)/σ")
        fig.align_ylabels([ax, rax])
        parts["rax"] = rax
    if n >= 7:
        _callouts(fig, parts)
    style.save(fig, NAME.format(n), opaque=True, tight=False)


def _callouts(fig, p):
    """Stage 7: the name of each part in the accent colour, a thin leader
    from the name to a dot on the part. Positions are in inches on the
    canvas; a part drawn by Matplotlib (title, legend, labels) is found by
    its box after a draw, so the dot sits on it at any size."""
    from matplotlib.lines import Line2D
    from matplotlib.patches import Rectangle
    from matplotlib.text import Annotation

    ax, rax, f, d = p["ax"], p["rax"], numbers()["fit"], numbers()
    acc, bg = style.ACCENT, style.BG
    inch = fig.dpi_scale_trans
    fig.draw_without_rendering()
    r = fig.canvas.get_renderer()

    def at(axes, x, y):                       # data -> canvas inches
        return tuple(inch.inverted().transform(axes.transData.transform((x, y))))

    def on(artist, fx, fy):                   # a point of an artist's box, inches
        b = artist.get_window_extent(r).transformed(inch.inverted())
        return (b.x0 + fx * b.width, b.y0 + fy * b.height)

    def callout(label, target, text, ha="left", va="center", rel=None, dot=True):
        ann = Annotation(label, xy=target, xycoords=inch, xytext=text, textcoords=inch,
                         ha=ha, va=va, color=acc, fontsize=11, fontweight="bold", zorder=20,
                         bbox=dict(boxstyle="square,pad=0.12", facecolor=bg, edgecolor="none"),
                         arrowprops=dict(arrowstyle="-", color=acc, lw=0.8, shrinkA=0,
                                         shrinkB=0, relpos=rel or (0.5, 0.5)))
        fig.add_artist(ann)
        if dot:
            fig.add_artist(Line2D([target[0]], [target[1]], transform=inch, marker="o",
                                  ms=3.2, color=acc, ls="none", zorder=21))

    tick = 5 / 72                              # major tick length, inches
    # the canvas: a dashed frame along its edge, named in its corner
    e = 0.035
    fig.add_artist(Rectangle((e, e), W - 2 * e, H - 2 * e, transform=inch, fill=False,
                             edgecolor=acc, lw=0.8, ls=(0, (4, 3)), zorder=19))
    fig.text(0.12, 0.15, "Figure", transform=inch, ha="left", va="center", color=acc,
             fontsize=11, fontweight="bold", zorder=20)

    title_end = on(p["title"], 1, 0.45)
    callout("Title", (title_end[0] + 0.04, title_end[1]), (title_end[0] + 0.45, title_end[1]),
            rel=(0, 0.5))
    ylab = on(ax.yaxis.label, 0.5, 1)
    callout("y-axis label", (ylab[0], ylab[1] + 0.03), (0.12, H - 0.19), rel=(0.22, 0.5))
    # inside the main panel, upper left (under the legend)
    leg = on(p["legend"], 0.3, 0.0)
    callout("Legend", (leg[0], leg[1] + 0.02), at(ax, 1.8, 9.9), rel=(0.3, 0.5))
    x0 = at(ax, 0, 0)[0]
    callout("Major tick", (x0 + tick, at(ax, 0, 10)[1]), at(ax, 0.42, 9.9), rel=(0, 0.5))
    callout("Minor tick", (x0 + tick / 2, at(ax, 0, 4)[1]), at(ax, 0.42, 4.0), rel=(0, 0.5))
    # the empty middle, under the curve
    callout("Reference line", at(ax, 5.2, d["mean_all"]), at(ax, 4.55, 3.6), rel=(0.45, 0.5))
    callout("Axes", at(ax, 6.55, -1.0), at(ax, 5.5, -2.6), rel=(1, 0.5))
    note_end = on(p["note"], 1, 0.5)
    callout("Annotation", (note_end[0] + 0.03, note_end[1]),
            (note_end[0] + 0.35, note_end[1]), rel=(0, 0.5))
    nov = at(ax, T_MID[10], d["means"][10])
    callout("Data points (markers)", (nov[0] - 0.04, nov[1] - 0.01), at(ax, 7.35, 1.0),
            rel=(1, 0.5))
    # right: an error bar, the fit box, the curve, the top spine
    cap = at(ax, T_MID[11], d["means"][11] - d["se"][11])
    callout("Error bar", (cap[0], cap[1] - 0.01), at(ax, 10.0, -6.3), rel=(1, 0.5))
    text = at(ax, 8.42, 18.6)
    callout("Fit result", (on(p["box"].get_bbox_patch(), 0, 0)[0], text[1]), text,
            rel=(1, 0.5))
    callout("Fitted curve", at(ax, 9.95, model(9.95, f["c"], f["amp"], f["t0"])),
            at(ax, 10.25, 5.0), rel=(0, 0.5))
    top = at(ax, 11.75, YLIM[1])
    callout("Spine", top, (W - 0.12, title_end[1]), ha="right", rel=(0.45, 0.5))
    # under the panels
    mar = on(rax.get_xticklabels()[2], 0.5, 0)
    callout("Tick label", (mar[0], mar[1] - 0.02), (mar[0], 0.14), ha="center")
    month = on(rax.xaxis.label, 1, 0.5)
    callout("x-axis label", (month[0] + 0.04, month[1]), (month[0] + 0.4, month[1]),
            rel=(0, 0.5))
    callout("Residual panel", at(rax, 11.0, -2.0), (W - 1.39, 0.14), rel=(0.5, 0.5))


FIGURES = {NAME.format(n): (lambda n=n: _stage(n)) for n in range(1, N_STAGES + 1)}


if __name__ == "__main__":
    d = numbers()
    f = d["fit"]
    print(f"{d['hours']} valid hours, {d['years'][0]}-{d['years'][-1]}; "
          f"mean of all hours {d['mean_all']:.4f} degC")
    print("month  mean     s      s/sqrt(10)  fit     pull")
    for m in range(12):
        print(f"{MONTHS[m]}  {d['means'][m]:7.3f}  {d['s'][m]:5.3f}  {d['se'][m]:6.3f}  "
              f"   {model(T_MID[m], f['c'], f['amp'], f['t0']):7.3f}  {f['pulls'][m]:+.2f}")
    print(f"fit: c = {f['c']:.3f} +- {f['sc']:.3f} degC, A = {f['amp']:.3f} +- {f['samp']:.3f} degC, "
          f"t0 = {f['t0']:.4f} +- {f['st0']:.4f} month "
          f"(day {f['t0'] * DAYS_PER_MONTH:.1f} +- {f['st0'] * DAYS_PER_MONTH:.1f}: {day_label(f['t0'])})")
    print(f"chi2 = {f['chi2']:.2f} for ndf = {f['ndf']}, chi2/ndf = {f['chi2'] / f['ndf']:.3f}")
    print(f"fitted minimum {f['c'] - f['amp']:.2f} degC on {day_label(f['t0'])}, "
          f"maximum {f['c'] + f['amp']:.2f} degC on {day_label(f['t0'] + 6)}")
    print("Lecture 9, the 3648 daily means: c = 7.18, A = 11.18, coldest on 16 January; "
          f"a month's mean flattens a cosine by sin(pi/12)/(pi/12) = "
          f"{np.sin(np.pi / 12) / (np.pi / 12):.4f}: 11.18 -> "
          f"{11.18 * np.sin(np.pi / 12) / (np.pi / 12):.2f}")
    g = fit(np.arange(12) + 0.5, d["means"], d["se"])
    print(f"with every month at k + 0.5 instead of its middle: c = {g['c']:.3f}, "
          f"A = {g['amp']:.3f}, coldest {day_label(g['t0'])}, chi2 = {g['chi2']:.2f}")
