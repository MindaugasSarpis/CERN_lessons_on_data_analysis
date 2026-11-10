"""Anatomy of a scientific figure: the D0 mass peak of the LHCb file, built
part by part for a v-click slide (Lecture 7, "The Parts of a Figure").

The lecturer, 10 Nov 2026, on the version that showed the twelve monthly
means of the weather log with a fitted cosine: "Rework, more expressed error
bars, more complicated curve, 16:9 ratio". The weather log gives neither
honestly: its monthly means are known to 0.3 degC on a range of 30, and every
structure in it is one cosine. So the figure uses the course's other real
file, the K- pi+ pairs of LHCb (D0_KPi.csv, 91 583 rows):

  * the points: the mass M of the first N_ROWS rows of the file, those from
    1820 to 1910 MeV/c^2 (the window of Lecture 9), counted in BINS bins;
  * the error bars: sqrt(n) for a count n. With every row of the file a bar
    is shorter than its marker (sqrt(5400) / 5400 = 1.4 %), which is why the
    figure takes the first N_ROWS rows: a bar is 10 % of its count at the
    top of the peak and 15 to 20 % beside it, so every bar shows;
  * the curve: a Gaussian (the D0 decays) on a straight line (all other
    pairs), five parameters, fitted by weighted least squares with
    sigma = sqrt(n) (Lecture 9's model and method; Levenberg-Marquardt, here
    in NumPy). It is drawn in its parts: the sum as a solid line, the
    straight line dashed, the Gaussian as the filled area between the two;
  * the reference line: the known D0 mass, 1864.84 +- 0.05 MeV/c^2 (Particle
    Data Group);
  * the residual panel: the pulls (data - fit) / sigma.

Seven stages of IDENTICAL geometry (fixed margins, a solid 16:9 canvas), each
stage adding its parts: the frame; the data points; the error bars; the
fitted curve, its two components and the fit result; the reference line, the
annotation, the legend and the title; the residual panel; callouts naming
each part.

The lecturer, 10 Nov 2026, while this version was drawn: "legend with no
frame". The legend has none, and the fit result is plain text without a box.

Every number on the figure is computed here. Print them with

    python figures/src/anatomy.py
"""
import numpy as np

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data" / "D0_KPi.csv"
N_ROWS = 1500                    # the first rows of the file
WINDOW = (1820.0, 1910.0)        # MeV/c^2
BINS = 30
BIN_W = (WINDOW[1] - WINDOW[0]) / BINS   # 3 MeV/c^2
PIVOT = 1865.0                   # the straight line is c0 + c1 (m - PIVOT)
PDG_MASS, PDG_ERR = 1864.84, 0.05        # the known D0 mass, MeV/c^2
NAME = "viz_anatomy_stage{}"
N_STAGES = 7

_CACHE = {}


def histogram(rows=N_ROWS):
    """The counts n of the mass in BINS bins of the window, for the first
    `rows` rows of the file (None: every row), and sigma = sqrt(n)."""
    m = np.loadtxt(DATA, delimiter=",", skiprows=1, usecols=0, max_rows=rows)
    n, edges = np.histogram(m, bins=BINS, range=WINDOW)
    n = n.astype(float)
    return dict(rows=len(m), pairs=int(n.sum()), x=(edges[:-1] + edges[1:]) / 2, n=n,
                s=np.sqrt(n))


def gauss(m, A, mu, sigma):
    return A * np.exp(-(m - mu) ** 2 / (2 * sigma ** 2))


def line(m, c0, c1):
    return c0 + c1 * (m - PIVOT)


def model(m, A, mu, sigma, c0, c1):
    """A Gaussian on a straight line: the model of Lecture 9's D0 fit."""
    return gauss(m, A, mu, sigma) + line(m, c0, c1)


def jacobian(m, A, mu, sigma, c0, c1):
    g = np.exp(-(m - mu) ** 2 / (2 * sigma ** 2))
    return np.column_stack([g, A * g * (m - mu) / sigma ** 2,
                            A * g * (m - mu) ** 2 / sigma ** 3,
                            np.ones_like(m), m - PIVOT])


def fit(x, n, s):
    """Weighted least squares by Levenberg-Marquardt: the step solves
    (J'J + lambda diag(J'J)) d = J'r for the residuals r = (n - model) / s;
    lambda falls after a step that lowers chi2 and rises after one that does
    not. The covariance is (J'J)^-1 at the minimum (sigma taken as known)."""
    p = np.array([n.max() - np.median(n), PIVOT, 8.0, np.median(n), 0.0])
    r = (n - model(x, *p)) / s
    chi2, lam = r @ r, 1e-3
    for _ in range(500):
        J = jacobian(x, *p) / s[:, None]
        H = J.T @ J
        trial = p + np.linalg.solve(H + lam * np.diag(np.diag(H)), J.T @ r)
        rt = (n - model(x, *trial)) / s
        if rt @ rt < chi2:
            gain = chi2 - rt @ rt
            p, r, chi2, lam = trial, rt, rt @ rt, lam / 10
            if gain < 1e-12:
                break
        else:
            lam *= 10
            if lam > 1e12:
                break
    J = jacobian(x, *p) / s[:, None]
    V = np.linalg.inv(J.T @ J)
    err = np.sqrt(np.diag(V))
    A, mu, sigma, c0, c1 = p
    # the number of D0 decays: the area of the Gaussian in units of one bin
    k = np.sqrt(2 * np.pi) / BIN_W
    grad = np.array([k * sigma, 0, k * A, 0, 0])
    return dict(p=p, err=err, V=V, pulls=r, chi2=chi2, ndf=len(x) - len(p),
                A=A, mu=mu, sigma=sigma, c0=c0, c1=c1,
                sA=err[0], smu=err[1], ssigma=err[2], sc0=err[3], sc1=err[4],
                signal=k * A * sigma, ssignal=np.sqrt(grad @ V @ grad))


def numbers():
    if not _CACHE:
        h = histogram()
        _CACHE.update(h, fit=fit(h["x"], h["n"], h["s"]))
    return _CACHE


# ---------------------------------------------------------------------------
# The figure
# ---------------------------------------------------------------------------

# The canvas, in inches: the 16:9 box of the slide (sizes.json), else this.
W, H = style.SIZES.get(NAME.format(1), (9.30, 5.23))
LEFT, RIGHT, TOP, BOTTOM = 0.80, 0.30, 0.50, 0.62   # margins around the panels (in)
RES_H = 0.95                                        # residual panel height (in)
MAIN_BOTTOM = BOTTOM + RES_H
YLIM, PULL_LIM = (0, 125), (-3.5, 3.5)
Y_MAJOR, Y_MINOR = 25, 5
MS = 4.5
MASS_UNIT = r"MeV/$c^2$"


def _box(bottom, height):
    return [LEFT / W, bottom / H, (W - LEFT - RIGHT) / W, height / H]


def _mass_axis(ax, labels: bool):
    from matplotlib.ticker import MultipleLocator
    ax.set_xlim(*WINDOW)
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.xaxis.set_minor_locator(MultipleLocator(2))
    ax.tick_params(axis="x", labelbottom=labels)
    if labels:
        ax.set_xlabel(rf"mass of the $K^-\pi^+$ pair ({MASS_UNIT})")


def build(n: int):
    """The figure up to stage n (1..7), and its parts by name.

    The stages are stacked as v-click layers on the slide, so each is an
    OPAQUE canvas of identical geometry: the panels are placed by hand (no
    constrained layout, no tight bbox), so every part sits at the same pixel
    in every stage, and a solid background makes stage n cover stage n-1.
    Until the residual panel comes (stage 6) the main panel carries the
    mass labels itself."""
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MultipleLocator

    d = numbers()
    f = d["fit"]
    x, cnt, s = d["x"], d["n"], d["s"]
    fg, dim, bg = style.FG, style.DIM, style.BG
    c_fit, c_bkg = style.CYCLE[1], style.CYCLE[2]

    fig = plt.figure(figsize=(W, H), layout="none")
    ax = fig.add_axes(_box(MAIN_BOTTOM, H - TOP - MAIN_BOTTOM))
    ax.set_ylim(*YLIM)
    ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR))
    ax.yaxis.set_minor_locator(MultipleLocator(Y_MINOR))
    ax.set_ylabel(rf"pairs per {BIN_W:.0f} {MASS_UNIT}")
    _mass_axis(ax, labels=n < 6)
    parts = dict(ax=ax)

    if n >= 2:      # the data points
        parts["points"], = ax.plot(x, cnt, "o", ms=MS, color=fg, zorder=5)
    if n >= 3:      # their error bars
        parts["bars"] = ax.errorbar(x, cnt, yerr=s, fmt="none", ecolor=fg, elinewidth=1.3,
                                    capsize=3, capthick=1.3, zorder=4)
    if n >= 4:      # the fitted curve, its two components, the fit result
        mm = np.linspace(*WINDOW, 600)
        total, bkg = model(mm, *f["p"]), line(mm, f["c0"], f["c1"])
        parts["fill"] = ax.fill_between(mm, bkg, total, color=c_fit, alpha=0.22, lw=0,
                                        zorder=1)
        parts["bkg"], = ax.plot(mm, bkg, color=c_bkg, ls=(0, (6, 3)), zorder=2)
        parts["curve"], = ax.plot(mm, total, color=c_fit, lw=1.8, zorder=3)
        parts["box"] = ax.annotate(
            "\n".join([
                rf"$\mu = {f['mu']:.1f} \pm {f['smu']:.1f}$ {MASS_UNIT}",
                rf"$\sigma = {f['sigma']:.1f} \pm {f['ssigma']:.1f}$ {MASS_UNIT}",
                rf"$\chi^2/\mathrm{{ndf}} = {f['chi2']:.1f}\,/\,{f['ndf']}$",
            ]),
            xy=(1, 1), xycoords="axes fraction", xytext=(-12, -12), textcoords="offset points",
            ha="right", va="top", multialignment="left", linespacing=1.3, zorder=6)
    if n >= 5:      # reference line, annotation, legend, title
        parts["ref"] = ax.axvline(PDG_MASS, color=dim, lw=1.2, ls=(0, (2, 2.5)), zorder=2)
        parts["note"] = ax.annotate(
            rf"${f['signal']:.0f} \pm {f['ssignal']:.0f}$ $D^0$ decays",
            xy=(f["mu"] + 6.5, line(f["mu"] + 6.5, f["c0"], f["c1"]) + 0.45 * f["A"]),
            xytext=(1884.5, 0.50 * YLIM[1]), color=fg, fontsize=12, ha="left", va="center",
            arrowprops=dict(arrowstyle="-|>,head_length=0.5,head_width=0.22", color=fg,
                            lw=0.9, shrinkA=3, shrinkB=0, relpos=(0, 0.5),
                            connectionstyle="arc3,rad=0.2"))
        from matplotlib.patches import Patch
        parts["legend"] = ax.legend(
            [(parts["bars"], parts["points"]), parts["curve"],
             Patch(facecolor=c_fit, alpha=0.3, edgecolor="none"), parts["bkg"], parts["ref"]],
            [rf"data, error bar $\sqrt{{n}}$",
             "fit: Gaussian + straight line",
             r"$D^0 \to K^-\pi^+$ decays (Gaussian)",
             "other pairs (straight line)",
             rf"known $D^0$ mass, {PDG_MASS} {MASS_UNIT}"],
            loc="upper left", bbox_to_anchor=(0.008, 0.985), borderaxespad=0.2,
            handlelength=2.2, frameon=False)
        parts["title"] = ax.set_title(
            rf"LHCb: the $D^0$ meson is a peak at {f['mu']:.1f} {MASS_UNIT} "
            rf"in the mass of $K^-\pi^+$ pairs")
    if n >= 6:      # the residual panel
        rax = fig.add_axes(_box(BOTTOM, RES_H), sharex=ax)
        _mass_axis(rax, labels=True)
        rax.set_ylim(*PULL_LIM)
        rax.yaxis.set_major_locator(MultipleLocator(2))
        rax.yaxis.set_minor_locator(MultipleLocator(1))
        rax.axhline(0, color=dim, lw=0.9, zorder=1)
        rax.plot(x, f["pulls"], "o", ms=MS, color=fg, zorder=4)
        rax.set_ylabel("(data − fit)/σ")
        fig.align_ylabels([ax, rax])
        parts["rax"] = rax
    if n >= 7:
        _callouts(fig, parts)
    return fig, parts


def _stage(n: int):
    fig, _ = build(n)
    style.save(fig, NAME.format(n), opaque=True, tight=False)


def _callouts(fig, p):
    """Stage 7: the name of each part in the accent colour, a thin leader
    from the name to a dot on the part. Positions are in inches on the
    canvas; a part drawn by Matplotlib (title, legend, labels) is found by
    its box after a draw, so the dot sits on it at any size."""
    from matplotlib.lines import Line2D
    from matplotlib.patches import Rectangle
    from matplotlib.text import Annotation, Text

    ax, rax, d = p["ax"], p["rax"], numbers()
    f, x, cnt, s = d["fit"], d["x"], d["n"], d["s"]
    acc, bg = style.ACCENT, style.BG
    inch = fig.dpi_scale_trans
    fig.draw_without_rendering()
    r = fig.canvas.get_renderer()

    def at(axes, mx, v):                      # data -> canvas inches
        return tuple(inch.inverted().transform(axes.transData.transform((mx, v))))

    def on(artist, fx, fy, text_only=False):  # a point of an artist's box, inches
        b = (Text.get_window_extent(artist, r) if text_only else artist.get_window_extent(r))
        b = b.transformed(inch.inverted())
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

    tick = 5 / 72                             # major tick length, inches
    top = YLIM[1]
    x_left, x_right = at(ax, WINDOW[0], 0)[0], at(ax, WINDOW[1], 0)[0]

    # the canvas: a dashed frame along its edge, named in its corner
    e = 0.035
    fig.add_artist(Rectangle((e, e), W - 2 * e, H - 2 * e, transform=inch, fill=False,
                             edgecolor=acc, lw=0.8, ls=(0, (4, 3)), zorder=19))
    fig.text(0.12, 0.15, "Figure", transform=inch, ha="left", va="center", color=acc,
             fontsize=11, fontweight="bold", zorder=20)

    # around the panels
    title_end = on(p["title"], 1, 0.45)
    callout("Title", (title_end[0] + 0.04, title_end[1]), (title_end[0] + 0.32, title_end[1]),
            rel=(0, 0.5))
    ylab = on(ax.yaxis.label, 0.5, 1)
    callout("y-axis label", (ylab[0], ylab[1] + 0.03), (0.12, H - 0.19), rel=(0.22, 0.5))
    label = next(t for t in rax.get_xticklabels() if t.get_text() == "1840")
    lab = on(label, 0.5, 0)
    callout("Tick label", (lab[0], lab[1] - 0.02), (lab[0], 0.14), ha="center")
    xlab = on(rax.xaxis.label, 1, 0.5)
    callout("x-axis label", (xlab[0] + 0.04, xlab[1]), (xlab[0] + 0.4, xlab[1]), rel=(0, 0.5))
    callout("Residual panel", at(rax, 1904.0, -2.6), (W - 1.39, 0.14), rel=(0.5, 0.5))

    # left of the peak: the legend, a spine, the curve
    leg = on(p["legend"], 0.42, 0.0)
    callout("Legend", (leg[0], leg[1] + 0.03), (leg[0], leg[1] - 0.30), ha="center")
    spine = at(ax, WINDOW[0], 0.50 * top)
    callout("Spine", spine, (spine[0] + 0.35, spine[1]), rel=(0, 0.5))
    m_c = f["mu"] - 1.45 * f["sigma"]
    curve = at(ax, m_c, model(m_c, *f["p"]))
    callout("Fitted curve", curve, (curve[0] - 0.28, curve[1] + 0.22), ha="right", rel=(1, 0.5))

    # above the peak: an error bar, the reference line
    i = int(np.argmax(cnt))
    cap = at(ax, x[i], cnt[i] + s[i])
    callout("Error bar", (cap[0] - 0.02, cap[1] + 0.01), (cap[0] - 0.24, at(ax, 0, 0.93 * top)[1]),
            ha="right", rel=(1, 0.5))
    ref = at(ax, PDG_MASS, 0.93 * top)
    callout("Reference line", ref, (ref[0] + 0.30, ref[1]), rel=(0, 0.5))

    # right of the peak: the fit result, a data point, the annotation, the ticks
    box = on(p["box"], 0, 0.5)
    callout("Fit result", (box[0] - 0.05, box[1]), (box[0] - 0.33, box[1]), ha="right",
            rel=(1, 0.5))
    j = int(np.argmin(np.abs(x - (f["mu"] + 0.9 * f["sigma"]))))
    pt = at(ax, x[j], cnt[j])
    callout("Data point (marker)", (pt[0] + 0.03, pt[1] + 0.03), (pt[0] + 0.36, pt[1] + 0.42),
            rel=(0, 0.5))
    note = on(p["note"], 0.42, 1, text_only=True)
    callout("Annotation", (note[0], note[1] + 0.05), (note[0], note[1] + 0.30), ha="center")
    for name, v in (("Major tick", 0.60 * top), ("Minor tick", 0.68 * top)):
        length = tick if name == "Major tick" else tick / 2
        y_t = at(ax, 0, v)[1]
        callout(name, (x_right - length, y_t), (x_right - 0.32, y_t), ha="right", rel=(1, 0.5))

    # under the points: the two components of the fit, the axes
    m_b = f["mu"] - 0.95 * f["sigma"]
    y_band = at(ax, 0, 0.075 * top)[1]
    bkg = at(ax, m_b, line(m_b, f["c0"], f["c1"]))
    callout("Fit component", bkg, (bkg[0], y_band), ha="center")
    m_f = f["mu"] + 0.45 * f["sigma"]
    area = at(ax, m_f, line(m_f, f["c0"], f["c1"]) + 0.13 * f["A"])
    callout("Filled area", area, (area[0] + 0.08, y_band), ha="left", rel=(0.1, 0.5))
    axes = at(ax, 1893.0, 0.115 * top)
    callout("Axes", axes, (axes[0] - 0.42, y_band), ha="right", rel=(1, 0.5))


FIGURES = {NAME.format(n): (lambda n=n: _stage(n)) for n in range(1, N_STAGES + 1)}


if __name__ == "__main__":
    d = numbers()
    f = d["fit"]
    print(f"first {d['rows']} rows of {DATA.name}: {d['pairs']} pairs from {WINDOW[0]:.0f} to "
          f"{WINDOW[1]:.0f} MeV/c^2, {BINS} bins of {BIN_W:.0f} MeV/c^2")
    print("mass     n    sqrt(n)   fit     pull")
    for xi, ni, si, pi in zip(d["x"], d["n"], d["s"], f["pulls"]):
        print(f"{xi:6.1f}  {ni:4.0f}  {si:6.2f}  {model(xi, *f['p']):7.2f}  {pi:+.2f}")
    print(f"fit: A = {f['A']:.2f} +- {f['sA']:.2f}, mu = {f['mu']:.3f} +- {f['smu']:.3f}, "
          f"sigma = {f['sigma']:.3f} +- {f['ssigma']:.3f} MeV/c^2, "
          f"c0 = {f['c0']:.2f} +- {f['sc0']:.2f}, c1 = {f['c1']:.3f} +- {f['sc1']:.3f}")
    print(f"chi2 = {f['chi2']:.2f} for ndf = {f['ndf']}; largest |pull| = "
          f"{np.abs(f['pulls']).max():.2f}; {int((np.abs(f['pulls']) > 2).sum())} beyond 2")
    print(f"D0 decays: {f['signal']:.1f} +- {f['ssignal']:.1f}; other pairs: "
          f"{d['pairs'] - f['signal']:.0f}")
    print(f"mu - known mass = {f['mu'] - PDG_MASS:+.2f} MeV/c^2 = "
          f"{(f['mu'] - PDG_MASS) / np.hypot(f['smu'], PDG_ERR):+.2f} sigma")
    print(f"error bar at the top of the peak: sqrt({d['n'].max():.0f}) = {d['s'].max():.1f} "
          f"({100 * d['s'].max() / d['n'].max():.1f} %); smallest count {d['n'].min():.0f}")
    a = histogram(None)
    g = fit(a["x"], a["n"], a["s"])
    print(f"every row ({a['rows']}): {a['pairs']} pairs, top count {a['n'].max():.0f} +- "
          f"{a['s'].max():.0f} ({100 * a['s'].max() / a['n'].max():.1f} %), mu = {g['mu']:.2f} +- "
          f"{g['smu']:.2f}, sigma = {g['sigma']:.2f} +- {g['ssigma']:.2f}, "
          f"{g['signal']:.0f} +- {g['ssignal']:.0f} decays, chi2 = {g['chi2']:.1f} / {g['ndf']}")
