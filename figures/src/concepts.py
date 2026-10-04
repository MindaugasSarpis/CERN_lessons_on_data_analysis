"""Figures of Lecture 14: Concepts of Data Analysis.

Every figure is computed from the two course files, `pendulum.csv` and
`D0_KPi.csv`, or from a seeded simulation (`np.random.default_rng(14)`).
The two fits follow Lecture 10 (`fitting.py`): the pendulum line is weighted
with sigma(t10) = 0.1 s, and the mass peak is fitted from 1820 to 1910 MeV/c²
in 45 bins of 2 MeV. The numbers the slides quote come from the same
functions:

    python figures/src/concepts.py --numbers     # print them
    python figures/src/concepts.py               # write the figures

  viz_concepts_two_cases          T² against the length with the line; the mass peak with its fit
  viz_concepts_uncertainty        one value of g, three uncertainties, three verdicts
  viz_concepts_stat_syst          statistical and systematic uncertainty against N
  viz_concepts_checks             g from six ways of doing the pendulum analysis
  viz_concepts_looks              chance of a false alarm against the number of looks
  viz_concepts_twenty_groups      the peak position in 20 groups drawn by lot
  viz_concepts_stopping           running z of analysts who test after every timing
  viz_concepts_drop_two           g from the 36 ways of dropping two points
  viz_concepts_selections         the peak position under 120 selections of rows
  viz_concepts_tau_ipchi2         decay time against IPCHI2 in the LHCb file
"""
import itertools
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data"
WARM = style.CYCLE[1]
GREEN = style.CYCLE[2]
PINK = style.CYCLE[3]

G_REF = 9.81            # m/s², the textbook value
SIGMA_T10 = 0.1         # s, assumed uncertainty of the time of 10 swings
M_PDG, M_PDG_ERR = 1864.84, 0.05   # MeV/c², Particle Data Group average
M_K, M_PI = 493.677, 139.570       # MeV/c²
SEED = 14


# --- the pendulum ---------------------------------------------------------

def pendulum():
    length_cm, t10 = np.loadtxt(DATA / "pendulum.csv", delimiter=",", skiprows=1).T
    return length_cm / 100, t10 / 10          # L in m, T in s


def line_fit(x, y, sy):
    """Weighted straight line y = m x + b, the closed formulas of Lecture 10.
    Returns (m, b), their uncertainties and the pulls."""
    w = 1 / sy ** 2
    S, Sx, Sy = w.sum(), (w * x).sum(), (w * y).sum()
    Sxx, Sxy = (w * x * x).sum(), (w * x * y).sum()
    D = S * Sxx - Sx ** 2
    m = (S * Sxy - Sx * Sy) / D
    b = (Sxx * Sy - Sx * Sxy) / D
    return (m, b), (np.sqrt(S / D), np.sqrt(Sxx / D)), (y - m * x - b) / sy


def sigma_t2(T):
    """Uncertainty of T² when the time of 10 swings is known to SIGMA_T10."""
    return 2 * T * SIGMA_T10 / 10


def g_from(L, T):
    (m, b), (dm, db), _ = line_fit(L, T ** 2, sigma_t2(T))
    g = 4 * np.pi ** 2 / m
    return g, g * dm / m


def drop_two():
    L, T = pendulum()
    out = []
    for i, j in itertools.combinations(range(len(L)), 2):
        keep = np.ones(len(L), bool)
        keep[[i, j]] = False
        g, dg = g_from(L[keep], T[keep])
        out.append((g, dg, int(round(L[i] * 100)), int(round(L[j] * 100))))
    return sorted(out)


def checks():
    """Six ways of getting g from the same nine rows."""
    L, T = pendulum()
    g_all, dg_all = g_from(L, T)
    w = 1 / sigma_t2(T) ** 2
    m0 = (w * L * T ** 2).sum() / (w * L * L).sum()      # line through the origin
    dm0 = 1 / np.sqrt((w * L * L).sum())
    g_i = 4 * np.pi ** 2 * L / T ** 2                    # one g per row
    dg_i = g_i * 2 * (SIGMA_T10 / 10) / T
    wi = 1 / dg_i ** 2
    short, long_ = L <= 0.6, L >= 0.6
    return [
        ("line with intercept, all nine rows", g_all, dg_all),
        ("line through the origin", 4 * np.pi ** 2 / m0, 4 * np.pi ** 2 / m0 * dm0 / m0),
        ("weighted mean of g, row by row", (wi * g_i).sum() / wi.sum(), 1 / np.sqrt(wi.sum())),
        ("the five shortest lengths", *g_from(L[short], T[short])),
        ("the five longest lengths", *g_from(L[long_], T[long_])),
    ]


# --- the mass peak --------------------------------------------------------

def d0_table():
    return np.loadtxt(DATA / "D0_KPi.csv", delimiter=",", skiprows=1)


LO, HI, WIDTH = 1820.0, 1910.0, 2.0


def peak_model(x, n_sig, mu, sigma, a, b):
    """Gaussian of n_sig candidates on a straight-line background, per bin."""
    gauss = n_sig * WIDTH / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    return gauss + a + b * (x - 1865.0)


def peak_fit(mass):
    edges = np.arange(LO, HI + 1e-9, WIDTH)
    counts, _ = np.histogram(mass, bins=edges)
    x = 0.5 * (edges[:-1] + edges[1:])
    err = np.sqrt(np.maximum(counts, 1))
    p0 = [0.23 * len(mass), 1865.0, 8.0, counts[:5].mean(), 0.0]
    popt, pcov = curve_fit(peak_model, x, counts, p0=p0, sigma=err, absolute_sigma=True)
    chi2 = (((counts - peak_model(x, *popt)) / err) ** 2).sum()
    return x, counts, err, popt, np.sqrt(np.diag(pcov)), chi2, len(x) - 5


def twenty_groups():
    """Each row gets a group number 0..19 by lot. The peak is fitted per group."""
    mass = d0_table()[:, 0]
    rng = np.random.default_rng(SEED)
    group = rng.integers(0, 20, len(mass))
    *_, popt, perr, _, _ = peak_fit(mass)
    mu_all = popt[1]
    rows = []
    for k in range(20):
        *_, p, e, _, _ = peak_fit(mass[group == k])
        rows.append((p[1], e[1], (p[1] - mu_all) / e[1]))
    return mu_all, np.array(rows)


PT_CUTS = [0, 2800, 3000, 3200, 3500, 4000]         # keep PT above
IP_CUTS = [np.inf, 50, 20, 10, 5]                    # keep IPCHI2 below
TAU_CUTS = [-np.inf, 0.0002, 0.0003, 0.0005]         # keep TAU above


def selections():
    """The peak fitted under every combination of three thresholds:
    6 × 5 × 4 = 120 selections of rows. Rows with TAU = -100 are left out.
    Returns rows (mu, error, pt, ip, tau, rows kept), sorted by mu."""
    tab = d0_table()
    tab = tab[tab[:, 2] != -100]
    mass, pt, tau, ip = tab.T
    out = []
    for cpt, cip, ctau in itertools.product(PT_CUTS, IP_CUTS, TAU_CUTS):
        keep = (pt > cpt) & (ip < cip) & (tau > ctau)
        *_, p, e, _, _ = peak_fit(mass[keep])
        out.append((p[1], e[1], cpt, cip, ctau, int(keep.sum())))
    return sorted(out)


# --- optional stopping ----------------------------------------------------

def stopping(n_analysts=10_000, n_max=100, first=5, sigma=0.09):
    """True g is 9.81. Each timing gives one value with spread sigma. The
    analyst computes z after every timing from the fifth on."""
    rng = np.random.default_rng(SEED)
    x = rng.normal(G_REF, sigma, (n_analysts, n_max))
    n = np.arange(1, n_max + 1)
    z = (np.cumsum(x, axis=1) / n - G_REF) / (sigma / np.sqrt(n))
    ever = (np.abs(z[:, first - 1:]) > 1.96).any(axis=1)
    at_end = np.abs(z[:, -1]) > 1.96
    return n, z, ever, at_end


# --- numbers --------------------------------------------------------------

def numbers():
    L, T = pendulum()
    (m, b), (dm, db), pulls = line_fit(L, T ** 2, sigma_t2(T))
    g, dg = g_from(L, T)
    print("PENDULUM")
    print(f"  slope      {m:.4f} ± {dm:.4f} s²/m")
    print(f"  intercept  {b:.4f} ± {db:.4f} s²  = an offset in L of {100 * b / m:.2f} ± {100 * db / m:.2f} cm")
    print(f"  pulls      {np.round(pulls, 2)}  chi2 = {(pulls ** 2).sum():.2f}, ndf = {len(L) - 2}")
    print(f"  relative   {100 * dg / g:.2f} %;  N for ±0.01: {9 * (dg / 0.01) ** 2:.0f};  equal to a 10° swing at N = {9 * (dg / (2 * np.radians(10) ** 2 / 16 * G_REF)) ** 2:.0f}")
    print(f"  g          {g:.3f} ± {dg:.3f} m/s²   z against {G_REF}: {(g - G_REF) / dg:+.2f}")
    for err in (0.005, dg, 0.3):
        print(f"    with ±{err:.3f}: z = {(g - G_REF) / err:+.2f}")
    print(f"  T at L = 1.5 m: {2 * np.pi * np.sqrt(1.5 / g):.3f} s")
    for deg in (5, 10, 20):
        f = np.radians(deg) ** 2 / 16
        print(f"  amplitude {deg:2d}°: T longer by {100 * f:.3f} %, g lower by {100 * 2 * f:.2f} % = {2 * f * G_REF:.3f} m/s²")
    for Lm, T1 in ((0.2, T[0]), (1.0, T[-1])):
        tl, tt = 0.005 / Lm, 2 * 0.01 / T1
        print(f"  one row, L = {Lm} m: dL/L = {100 * tl:.2f} %, 2 dT/T = {100 * tt:.2f} %, dg/g = {100 * np.hypot(tl, tt):.2f} %")
    print("  checks:")
    for name, gi, dgi in checks():
        print(f"    {name:34s} {gi:.3f} ± {dgi:.3f}")
    d2 = drop_two()
    print(f"  drop two: {len(d2)} ways, g from {d2[0][0]:.3f} (drop {d2[0][2]}, {d2[0][3]}) to {d2[-1][0]:.3f} ± {d2[-1][1]:.3f} (drop {d2[-1][2]}, {d2[-1][3]})")
    near = min(d2, key=lambda r: abs(r[0] - G_REF))
    print(f"    closest to {G_REF}: {near[0]:.3f} ± {near[1]:.3f} (drop {near[2]}, {near[3]})")
    print(f"    largest: z against {G_REF} = {(d2[-1][0] - G_REF) / d2[-1][1]:+.2f}")

    tab = d0_table()
    mass = tab[:, 0]
    x, counts, err, p, e, chi2, ndf = peak_fit(mass)
    print("D0 PEAK")
    print(f"  rows {len(mass)}, in the fit range {int(counts.sum())}")
    print(f"  N = {p[0]:.0f} ± {e[0]:.0f}, mu = {p[1]:.2f} ± {e[1]:.2f}, sigma = {p[2]:.2f} ± {e[2]:.2f}, chi2/ndf = {chi2:.1f}/{ndf}")
    z = (p[1] - M_PDG) / np.hypot(e[1], M_PDG_ERR)
    lever = (M_PDG ** 2 - M_K ** 2 - M_PI ** 2) / M_PDG
    print(f"  against {M_PDG} ± {M_PDG_ERR}: difference {p[1] - M_PDG:+.2f}, z = {z:+.1f}")
    print(f"  a momentum scale off by {100 * (M_PDG - p[1]) / lever:.3f} % moves the peak that far")
    for name, sel in (("first half", slice(None, len(mass) // 2)), ("second half", slice(len(mass) // 2, None))):
        *_, ph, eh, _, _ = peak_fit(mass[sel])
        print(f"  {name}: mu = {ph[1]:.2f} ± {eh[1]:.2f}")
    mu_all, rows = twenty_groups()
    k = np.abs(rows[:, 2]).argmax()
    print(f"  20 groups: largest deviation group {k + 1}: {rows[k, 0]:.2f} ± {rows[k, 1]:.2f}, z = {rows[k, 2]:+.2f}; beyond 1.96: {(np.abs(rows[:, 2]) > 1.96).sum()}")
    ok = tab[:, 2] != -100
    tau, ip = tab[ok, 2], tab[ok, 3]
    rank = lambda v: np.argsort(np.argsort(v))
    print(f"  Spearman(TAU, IPCHI2) = {np.corrcoef(rank(tau), rank(ip))[0, 1]:.2f} on {ok.sum()} rows")

    sel = selections()
    zpdg = lambda r: (r[0] - M_PDG) / np.hypot(r[1], M_PDG_ERR)
    plain = next(r for r in sel if r[2] == 0 and r[3] == np.inf and r[4] == -np.inf)
    print(f"  {len(sel)} selections: peak from {sel[0][0]:.2f} ± {sel[0][1]:.2f} (PT > {sel[0][2]}, IPCHI2 < {sel[0][3]}, TAU > {sel[0][4]}; {sel[0][5]} rows; z = {zpdg(sel[0]):+.1f})")
    print(f"      to {sel[-1][0]:.2f} ± {sel[-1][1]:.2f} (PT > {sel[-1][2]}, IPCHI2 < {sel[-1][3]}, TAU > {sel[-1][4]}; {sel[-1][5]} rows; z = {zpdg(sel[-1]):+.1f})")
    print(f"      no threshold: {plain[0]:.2f} ± {plain[1]:.2f} on {plain[5]} rows; spread {sel[-1][0] - sel[0][0]:.2f}")

    print("LOOKS")
    for k in (1, 5, 14, 20, 100):
        print(f"  {k:3d} looks: {100 * (1 - 0.95 ** k):.1f} %")
    rng = np.random.default_rng(SEED)
    sim = (np.abs(rng.standard_normal((10_000, 20))) > 1.96).any(axis=1).mean()
    print(f"  simulated, 10 000 × 20 looks: {100 * sim:.1f} %")
    n, zrun, ever, at_end = stopping()
    print(f"  stopping: ever beyond 1.96 = {100 * ever.mean():.1f} %, at the 100th timing only = {100 * at_end.mean():.1f} %")


# --- figures --------------------------------------------------------------

def _two_cases():
    L, T = pendulum()
    (m, b), _, _ = line_fit(L, T ** 2, sigma_t2(T))
    g, dg = g_from(L, T)
    mass = d0_table()[:, 0]
    x, counts, err, p, e, chi2, ndf = peak_fit(mass)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 3.9))
    xs = np.linspace(0, 1.1, 50)
    ax1.plot(xs, m * xs + b, color=WARM, linewidth=1.8)
    ax1.errorbar(L, T ** 2, yerr=sigma_t2(T), fmt="o", color=style.ACCENT, markersize=6,
                 elinewidth=1.2)
    ax1.set(xlabel=r"length $\ell$ (m)", ylabel="T² (s²)", xlim=(0, 1.1), ylim=(0, 4.5))
    ax1.set_title("Pendulum: nine rows", fontsize=13)
    ax1.text(0.05, 3.85, f"slope 4π²/g = {m:.3f} s²/m", color=WARM, fontsize=11)
    ax1.text(0.05, 3.40, f"g = {g:.2f} ± {dg:.2f} m/s²", color=style.FG, fontsize=12.5)

    xs = np.linspace(LO, HI, 400)
    ax2.errorbar(x, counts, yerr=err, fmt="o", color=style.ACCENT, markersize=3.5,
                 elinewidth=1, label="candidates per 2 MeV")
    ax2.plot(xs, peak_model(xs, *p), color=WARM, linewidth=1.8, label="Gaussian + line")
    ax2.plot(xs, p[3] + p[4] * (xs - 1865), color=style.DIM, linewidth=1.3,
             linestyle="--", label="background")
    ax2.set(xlabel=r"$K^-\pi^+$ mass M (MeV/c²)", ylabel="candidates per 2 MeV/c²",
            xlim=(LO, HI), ylim=(0, 4600))
    ax2.set_title("LHCb file: 91 583 rows", fontsize=13)
    ax2.text(1822, 4150, f"peak at {p[1]:.2f} ± {e[1]:.2f} MeV/c²", color=style.FG, fontsize=12.5)
    ax2.text(1822, 3750, f"width {p[2]:.2f} ± {e[2]:.2f} MeV/c²", color=style.DIM, fontsize=10.5)
    ax2.legend(loc="upper right", fontsize=9)
    style.save(fig, "viz_concepts_two_cases")


def _uncertainty():
    L, T = pendulum()
    g, dg = g_from(L, T)
    cases = [(0.005, f"{g:.3f} ± 0.005"), (dg, f"{g:.2f} ± {dg:.2f}"), (0.3, f"{g:.1f} ± 0.3")]
    verdict = ["disagrees with 9.81", "agrees with 9.81", "cannot tell 9.5 from 10.1"]
    colors = [style.BAD, GREEN, style.DIM]

    fig, ax = plt.subplots(figsize=(8.6, 2.3))
    ax.axvline(G_REF, color=WARM, linewidth=1.6)
    ax.text(G_REF - 0.02, 2.75, "reference 9.81", color=WARM, fontsize=12, ha="right")
    for i, ((err, label), v, c) in enumerate(zip(cases, verdict, colors)):
        yy = 2 - i
        ax.errorbar(g, yy, xerr=err, fmt="o", color=c, markersize=7, capsize=5,
                    elinewidth=2)
        z = (g - G_REF) / err
        ax.text(8.93, yy, label, color=style.FG, fontsize=13.5, va="center")
        ax.text(10.22, yy, rf"{abs(z):.1f}$\sigma$:  {v}", color=c, fontsize=13, va="center")
    ax.set(xlim=(8.9, 11.15), ylim=(-0.55, 3.1), xlabel="g (m/s²)")
    ax.tick_params(labelsize=11)
    ax.set_yticks([])
    ax.set_xticks([9.6, 9.7, 9.8, 9.9, 10.0])
    ax.yaxis.grid(False)
    ax.spines["left"].set_visible(False)
    style.save(fig, "viz_concepts_uncertainty")


def _stat_syst():
    L, T = pendulum()
    g, dg = g_from(L, T)
    syst = 2 * np.radians(10) ** 2 / 16 * G_REF          # a 10° swing
    n = np.logspace(np.log10(3), 3, 200)
    stat = dg * np.sqrt(9 / n)
    total = np.hypot(stat, syst)
    cross = 9 * (dg / syst) ** 2

    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.plot(n, stat, color=style.ACCENT, label="statistical: falls as 1/√N")
    ax.plot(n, np.full_like(n, syst), color=WARM, label="systematic: a 10° swing, 0.037")
    ax.plot(n, total, color=style.FG, linestyle="--", linewidth=1.6, label="both, added in quadrature")
    ax.plot([9], [dg], "o", color=style.ACCENT, markersize=8)
    ax.annotate("the nine rows", xy=(9, dg), xytext=(10.5, 0.105), color=style.FG, fontsize=10)
    ax.axvline(cross, color=style.DIM, linewidth=1, linestyle=":")
    ax.text(cross * 1.08, 0.0125, f"N = {cross:.0f}: equal", color=style.DIM, fontsize=10)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set(xlabel="number of lengths measured, N", ylabel="uncertainty of g (m/s²)",
           xlim=(3, 1000), ylim=(0.004, 0.2))
    ax.set_xticks([3, 10, 30, 100, 300, 1000])
    ax.set_xticklabels(["3", "10", "30", "100", "300", "1000"])
    ax.set_yticks([0.005, 0.01, 0.02, 0.05, 0.1, 0.2])
    ax.set_yticklabels(["0.005", "0.01", "0.02", "0.05", "0.1", "0.2"])
    ax.legend(loc="lower left", fontsize=9.5)
    style.save(fig, "viz_concepts_stat_syst")


def _checks():
    rows = checks()
    g_all, dg_all = rows[0][1], rows[0][2]

    fig, ax = plt.subplots(figsize=(8.4, 3.2))
    ax.axvspan(g_all - dg_all, g_all + dg_all, color=style.ACCENT, alpha=0.13, lw=0)
    ax.axvline(G_REF, color=WARM, linewidth=1.5)
    ax.text(G_REF - 0.004, len(rows) - 0.45, "9.81", color=WARM, fontsize=10.5, ha="right")
    for i, (name, g, dg) in enumerate(rows):
        yy = len(rows) - 1 - i
        ax.errorbar(g, yy, xerr=dg, fmt="o", color=style.ACCENT if i == 0 else style.FG,
                    markersize=6, capsize=4, elinewidth=1.6)
        ax.text(8.84, yy, name, color=style.FG, fontsize=11, va="center")
        ax.text(10.17, yy, f"{g:.2f} ± {dg:.2f}", color=style.DIM, fontsize=10.5, va="center")
    ax.set(xlim=(8.83, 10.45), ylim=(-0.6, len(rows) - 0.2), xlabel="g (m/s²)")
    ax.set_xticks([9.6, 9.7, 9.8, 9.9, 10.0, 10.1])
    ax.set_yticks([])
    ax.yaxis.grid(False)
    ax.spines["left"].set_visible(False)
    style.save(fig, "viz_concepts_checks")


def _looks():
    k = np.arange(1, 101)
    p = 1 - 0.95 ** k

    fig, ax = plt.subplots(figsize=(6.2, 3.5))
    ax.plot(k, 100 * p, color=style.ACCENT)
    for kk, dx, dy in ((1, 3, 3), (5, 3, -3), (20, 3, -5), (100, -16, -8)):
        v = 100 * (1 - 0.95 ** kk)
        ax.plot([kk], [v], "o", color=WARM, markersize=7)
        ax.text(kk + dx, v + dy, f"{kk}: {v:.0f} %", color=style.FG, fontsize=11)
    ax.set(xlabel="number of looks k", ylabel="chance of at least one\n" r"result beyond 2$\sigma$ (%)",
           xlim=(0, 104), ylim=(0, 105))
    style.save(fig, "viz_concepts_looks")


def _twenty_groups():
    mu_all, rows = twenty_groups()
    k = np.arange(1, 21)
    far = np.abs(rows[:, 2]) > 1.96

    fig, ax = plt.subplots(figsize=(8.6, 3.4))
    ax.plot([0.3, 20.6], [mu_all, mu_all], color=WARM, linewidth=1.5)
    ax.errorbar(k[~far], rows[~far, 0], yerr=rows[~far, 1], fmt="o", color=style.ACCENT,
                markersize=5, capsize=3, elinewidth=1.4)
    ax.errorbar(k[far], rows[far, 0], yerr=rows[far, 1], fmt="o", color=style.BAD,
                markersize=6, capsize=3, elinewidth=1.8)
    for i in np.flatnonzero(far):
        above = rows[i, 2] > 0
        ax.text(k[i] + 0.35, rows[i, 0] + (0.25 if above else -0.25),
                rf"{abs(rows[i, 2]):.1f}$\sigma$", color=style.BAD, fontsize=11,
                va="bottom" if above else "top")
    ax.text(20.75, mu_all, f"all rows\n{mu_all:.2f}", color=WARM, fontsize=10, va="center")
    ax.set(xlabel="group, drawn by lot", ylabel="fitted peak position\n(MeV/c²)",
           xlim=(0.3, 23.0))
    ax.set_xticks(k)
    ax.xaxis.grid(False)
    style.save(fig, "viz_concepts_twenty_groups")


def _stopping():
    n, z, ever, at_end = stopping()
    first = 5
    # Six analysts, in the order of the simulation: the first three who cross
    # the line between timing 20 and 95, and the first three who never do.
    when = np.array([first + np.argmax(np.abs(zi[first - 1:]) > 1.96) for zi in z])
    crossers = np.flatnonzero(ever & (when >= 20) & (when <= 95))[:3]
    quiet = np.flatnonzero(~ever)[:3]

    fig, ax = plt.subplots(figsize=(8.6, 3.5))
    ax.axhspan(-1.96, 1.96, color=style.ACCENT, alpha=0.08, lw=0)
    for v in (-1.96, 1.96):
        ax.axhline(v, color=style.DIM, linewidth=1, linestyle="--")
    for i in quiet:
        ax.plot(n[first - 1:], z[i, first - 1:], color=style.DIM, linewidth=1.1)
    for i in crossers:
        stop = first - 1 + np.flatnonzero(np.abs(z[i, first - 1:]) > 1.96)[0]
        ax.plot(n[first - 1:stop + 1], z[i, first - 1:stop + 1], color=style.BAD, linewidth=1.7)
        ax.plot(n[stop + 1:], z[i, stop + 1:], color=style.BAD, linewidth=0.9, alpha=0.35)
        ax.plot([n[stop]], [z[i, stop]], "o", color=style.BAD, markersize=7)
    ax.text(99, 2.25, r"2$\sigma$", color=style.DIM, fontsize=10, ha="right")
    ax.set(xlabel="number of timings so far", ylabel=r"z = (mean − 9.81) / $\sigma_{\rm mean}$",
           xlim=(first, 100), ylim=(-3.6, 3.6))
    style.save(fig, "viz_concepts_stopping")


def _drop_two():
    L, T = pendulum()
    g_all, dg_all = g_from(L, T)
    rows = drop_two()
    g = np.array([r[0] for r in rows])
    dg = np.array([r[1] for r in rows])
    k = np.arange(1, len(rows) + 1)
    near = int(np.abs(g - G_REF).argmin())

    fig, ax = plt.subplots(figsize=(8.6, 3.5))
    ax.axhspan(g_all - dg_all, g_all + dg_all, color=style.ACCENT, alpha=0.13, lw=0)
    ax.axhline(g_all, color=style.ACCENT, linewidth=1.3)
    ax.axhline(G_REF, color=WARM, linewidth=1.5)
    ax.errorbar(k, g, yerr=dg, fmt="o", color=style.FG, markersize=4, capsize=2,
                elinewidth=1, alpha=0.9)
    for i, c in ((near, WARM), (len(rows) - 1, style.BAD)):
        ax.errorbar(k[i], g[i], yerr=dg[i], fmt="o", color=c, markersize=7, capsize=3,
                    elinewidth=2)
    ax.text(0.8, g_all + dg_all + 0.012, f"all nine rows: {g_all:.2f} ± {dg_all:.2f}",
            color=style.ACCENT, fontsize=10.5)
    ax.text(36.7, G_REF - 0.035, "9.81", color=WARM, fontsize=10.5, ha="right")
    ax.annotate(f"drop {rows[near][2]} and {rows[near][3]} cm: {g[near]:.2f}",
                xy=(k[near], g[near]), xytext=(k[near] + 1.5, 9.585), color=WARM,
                fontsize=10.5, ha="center",
                arrowprops=dict(arrowstyle="-", color=WARM, lw=1))
    ax.annotate(f"drop {rows[-1][2]} and {rows[-1][3]} cm: {g[-1]:.2f}",
                xy=(k[-1], g[-1]), xytext=(29.5, 10.085), color=style.BAD, fontsize=10.5,
                ha="center", arrowprops=dict(arrowstyle="-", color=style.BAD, lw=1))
    ax.set(xlabel="the 36 ways of dropping two rows, sorted by the result",
           ylabel="g (m/s²)", xlim=(0, 37), ylim=(9.55, 10.13))
    ax.xaxis.grid(False)
    ax.set_xticks([1, 6, 12, 18, 24, 30, 36])
    style.save(fig, "viz_concepts_drop_two")


def _selections():
    sel = selections()
    mu = np.array([r[0] for r in sel])
    err = np.array([r[1] for r in sel])
    k = np.arange(1, len(sel) + 1)
    plain = next(i for i, r in enumerate(sel) if r[2] == 0 and r[3] == np.inf and r[4] == -np.inf)
    z = lambda i: abs(mu[i] - M_PDG) / np.hypot(err[i], M_PDG_ERR)

    fig, ax = plt.subplots(figsize=(8.6, 3.5))
    ax.axhspan(M_PDG - M_PDG_ERR, M_PDG + M_PDG_ERR, color=WARM, alpha=0.25, lw=0)
    ax.axhline(M_PDG, color=WARM, linewidth=1.5)
    ax.text(2, M_PDG + 0.075, "world average 1864.84 ± 0.05", color=WARM, fontsize=10.5)
    ax.errorbar(k, mu, yerr=err, fmt="o", color=style.FG, markersize=2.6, elinewidth=0.7,
                alpha=0.8)
    for i, c in ((0, style.BAD), (plain, style.ACCENT), (len(sel) - 1, GREEN)):
        ax.errorbar(k[i], mu[i], yerr=err[i], fmt="o", color=c, markersize=6.5,
                    capsize=3, elinewidth=2, zorder=5)
    ax.annotate(rf"PT > 3500: {z(0):.1f}$\sigma$ away", xy=(k[0], mu[0]), xytext=(9, 1864.02),
                color=style.BAD, fontsize=10.5, arrowprops=dict(arrowstyle="-", color=style.BAD, lw=1))
    ax.annotate("all rows", xy=(k[plain], mu[plain]), xytext=(k[plain] - 14, 1864.13),
                color=style.ACCENT, fontsize=10.5, ha="center",
                arrowprops=dict(arrowstyle="-", color=style.ACCENT, lw=1))
    ax.annotate(rf"three thresholds: {z(len(sel) - 1):.1f}$\sigma$ away", xy=(k[-1], mu[-1]),
                xytext=(98, 1864.13), color=GREEN, fontsize=10.5, ha="center",
                arrowprops=dict(arrowstyle="-", color=GREEN, lw=1))
    ax.set(xlabel="the 120 selections, sorted by the result",
           ylabel="fitted peak position\n(MeV/c²)", xlim=(0, 121), ylim=(1863.9, 1865.05))
    ax.set_xticks([1, 20, 40, 60, 80, 100, 120])
    ax.xaxis.grid(False)
    style.save(fig, "viz_concepts_selections")


def _tau_ipchi2():
    tab = d0_table()
    ok = (tab[:, 2] != -100) & (tab[:, 2] > 0)
    tau = tab[ok, 2]                                 # in the units of the file
    ip = tab[ok, 3]
    rank = lambda v: np.argsort(np.argsort(v))
    full = tab[:, 2] != -100
    rho = np.corrcoef(rank(tab[full, 2]), rank(tab[full, 3]))[0, 1]

    fig, ax = plt.subplots(figsize=(6.4, 3.7))
    xb = np.logspace(np.log10(1.2e-4), np.log10(3e-2), 70)
    yb = np.logspace(-2, 4, 70)
    h, _, _ = np.histogram2d(tau, ip, bins=[xb, yb])
    mesh = ax.pcolormesh(xb, yb, np.ma.masked_equal(h.T, 0), cmap="viridis",
                         norm="log", rasterized=True)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set(xlabel="decay time TAU (units of the file)", ylabel="IPCHI2")
    ax.grid(False)
    ax.text(1.4e-4, 2500, f"rank correlation {rho:.2f}", color=style.FG, fontsize=12)
    cbar = fig.colorbar(mesh, ax=ax, pad=0.02)
    cbar.outline.set_visible(False)
    cbar.ax.tick_params(colors=style.DIM, labelsize=9)
    cbar.set_label("candidates per cell", color=style.DIM, fontsize=9.5)
    style.save(fig, "viz_concepts_tau_ipchi2")


FIGURES = {
    "viz_concepts_two_cases": _two_cases,
    "viz_concepts_uncertainty": _uncertainty,
    "viz_concepts_stat_syst": _stat_syst,
    "viz_concepts_checks": _checks,
    "viz_concepts_looks": _looks,
    "viz_concepts_twenty_groups": _twenty_groups,
    "viz_concepts_stopping": _stopping,
    "viz_concepts_drop_two": _drop_two,
    "viz_concepts_selections": _selections,
    "viz_concepts_tau_ipchi2": _tau_ipchi2,
}


if __name__ == "__main__":
    if "--numbers" in sys.argv:
        numbers()
    else:
        style.use()
        for fn in FIGURES.values():
            fn()
