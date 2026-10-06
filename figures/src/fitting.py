"""Figures and numbers for Lecture 10, Data Fitting from First Principles.

Two data sets, both read from lectures/workbook/docs/data/:

  * pendulum.csv   nine lengths (cm) and the time of 10 swings (s). The fit is
                   T^2 against length in metres, a straight line with slope
                   4 pi^2 / g. Assumed uncertainty: 0.1 s on the time of 10
                   swings, so sigma(T) = 0.01 s and sigma(T^2) = 2 T sigma(T).
  * D0_KPi.csv     the mass column M, histogrammed from 1820 to 1910 MeV/c^2 in
                   45 bins of 2 MeV, uncertainties sqrt(n), fitted with a
                   Gaussian on a linear background.

Every number on the slides, the seminar page and the lecture page comes from
the functions in the first half of this file. Print them all with

    python figures/src/fitting.py

(needs numpy and scipy). The second half draws the figures
public/figures/viz_fitting_*.svg; build them with

    python figures/src/build.py --only fitting
"""
import warnings

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data"

SIGMA_T10 = 0.1                  # s, assumed uncertainty of the time of 10 swings
D0_WINDOW = (1820.0, 1910.0)     # MeV/c^2
D0_BINS = 45                     # 2 MeV per bin
D0_P0 = [2300, 1865, 8, 1400, 0]  # A, mu, sigma, c0, c1 read off the histogram
GD_START = (3.0, 0.0)
GD_ETA = 3e-5
GD_ETA_LARGE = 1e-4


# =============================================================================
# Numbers
# =============================================================================

def pendulum_data(sigma_t10=SIGMA_T10):
    """x = length (m), t10 (s), T (s), y = T^2 (s^2), sy = sigma(T^2)."""
    d = np.loadtxt(DATA / "pendulum.csv", delimiter=",", skiprows=1)
    x, t10 = d[:, 0] / 100, d[:, 1]
    T = t10 / 10
    return x, t10, T, T ** 2, 2 * T * sigma_t10 / 10


def line_fit(x, y, sy):
    """Weighted straight-line fit y = a x + b from the closed formulas."""
    w = 1 / sy ** 2
    S, Sx, Sy = w.sum(), (w * x).sum(), (w * y).sum()
    Sxx, Sxy = (w * x * x).sum(), (w * x * y).sum()
    D = S * Sxx - Sx ** 2
    a = (S * Sxy - Sx * Sy) / D
    b = (Sxx * Sy - Sx * Sxy) / D
    sa, sb, cov = np.sqrt(S / D), np.sqrt(Sxx / D), -Sx / D
    pulls = (y - a * x - b) / sy
    return dict(w=w, S=S, Sx=Sx, Sy=Sy, Sxx=Sxx, Sxy=Sxy, D=D, a=a, b=b,
                sa=sa, sb=sb, cov=cov, rho=cov / (sa * sb), pulls=pulls,
                chi2=(pulls ** 2).sum(), ndf=len(x) - 2)


def chi2_line(a, b, x, y, sy):
    return (((y - a * x - b) / sy) ** 2).sum()


def descent(x, y, sy, start=GD_START, eta=GD_ETA, steps=500):
    """Gradient descent on chi2(a, b). Rows: step, a, b, dchi2/da, dchi2/db, chi2."""
    f = line_fit(x, y, sy)
    a, b = start
    rows = []
    for k in range(steps + 1):
        ga = -2 * (f["Sxy"] - a * f["Sxx"] - b * f["Sx"])
        gb = -2 * (f["Sy"] - a * f["Sx"] - b * f["S"])
        rows.append((k, a, b, ga, gb, chi2_line(a, b, x, y, sy)))
        a, b = a - eta * ga, b - eta * gb
    return np.array(rows)


def d0_mass():
    return np.loadtxt(DATA / "D0_KPi.csv", delimiter=",", skiprows=1, usecols=0)


def d0_hist(lo=D0_WINDOW[0], hi=D0_WINDOW[1], bins=D0_BINS):
    """Bin centres, counts and sqrt(n) of the mass histogram."""
    n, edges = np.histogram(d0_mass(), bins=bins, range=(lo, hi))
    return 0.5 * (edges[:-1] + edges[1:]), n, np.sqrt(n)


def d0_model(m, A, mu, sigma, c0, c1):
    """A Gaussian on a linear background; the line is centred on 1865."""
    return A * np.exp(-(m - mu) ** 2 / (2 * sigma ** 2)) + c0 + c1 * (m - 1865)


def d0_fit(p0=None, lo=D0_WINDOW[0], hi=D0_WINDOW[1], bins=D0_BINS):
    m, n, s = d0_hist(lo, hi, bins)
    popt, pcov, info, _, _ = curve_fit(d0_model, m, n, p0=p0 or D0_P0, sigma=s,
                                       absolute_sigma=True, full_output=True)
    pulls = (n - d0_model(m, *popt)) / s
    return dict(m=m, n=n, s=s, popt=popt, pcov=pcov, err=np.sqrt(np.diag(pcov)),
                pulls=pulls, chi2=(pulls ** 2).sum(), ndf=bins - 5,
                nfev=info["nfev"])


def _d0_alt_models():
    """chi2 of models with fewer and more parameters, same histogram."""
    m, n, s = d0_hist()

    def chi2(f, p):
        return (((n - f(m, *p)) / s) ** 2).sum()

    def line(m, c0, c1):
        return c0 + c1 * (m - 1865)

    def gauss_const(m, A, mu, sigma, c0):
        return A * np.exp(-(m - mu) ** 2 / (2 * sigma ** 2)) + c0

    def gauss_parabola(m, A, mu, sigma, c0, c1, c2):
        return d0_model(m, A, mu, sigma, c0, c1) + c2 * (m - 1865) ** 2

    def two_gauss(m, A, mu, s1, f, s2, c0, c1):
        g = f * np.exp(-(m - mu) ** 2 / (2 * s1 ** 2)) \
            + (1 - f) * np.exp(-(m - mu) ** 2 / (2 * s2 ** 2))
        return A * g + c0 + c1 * (m - 1865)

    def fit(f, p0=None):
        p, c = curve_fit(f, m, n, p0=p0, sigma=s, absolute_sigma=True)
        return f, p, chi2(f, p), len(m) - len(p), np.sqrt(np.diag(c))

    return {"line": fit(line),
            "gauss_const": fit(gauss_const, D0_P0[:4]),
            "gauss_line": fit(d0_model, D0_P0),
            "gauss_parabola": fit(gauss_parabola, D0_P0 + [0]),
            "two_gauss": fit(two_gauss, [2300, 1865, 6, 0.7, 12, 1400, 0])}


def d0_plain_descent(steps=100_000):
    """Plain gradient descent on the D0 chi2, one learning rate for all five
    parameters (1 / largest curvature). Shows why curve_fit is needed."""
    f = d0_fit()
    m, n, s = f["m"], f["n"], f["s"]
    eig = np.linalg.eigvalsh(2 * np.linalg.inv(f["pcov"]))
    eta = 1 / eig.max()

    def chi2(p):
        return (((n - d0_model(m, *p)) / s) ** 2).sum()

    p = np.array(D0_P0, float)
    for _ in range(steps):
        g = np.zeros(5)
        for j in range(5):
            dp = np.zeros(5)
            dp[j] = 1e-5 * max(1, abs(p[j]))
            g[j] = (chi2(p + dp) - chi2(p - dp)) / (2 * dp[j])
        p = p - eta * g
    return eta, eig.max() / eig.min(), chi2(p)


def numbers():
    """Print every number quoted in the deck and on the workbook pages."""
    np.set_printoptions(precision=6, suppress=True, linewidth=150)
    x, t10, T, y, sy = pendulum_data()
    f = line_fit(x, y, sy)
    w = f["w"]

    print("== Pendulum: data and assumed uncertainties ==")
    print("x  t10  T  T^2  sigma(T^2)")
    for i in range(len(x)):
        print(f"{x[i]:.1f}  {t10[i]:.2f}  {T[i]:.3f}  {y[i]:.4f}  {sy[i]:.4f}")
    gi = 4 * np.pi ** 2 * x / y
    sgi = gi * sy / y
    wg = 1 / sgi ** 2
    print("g_i      ", np.round(gi, 3))
    print("sigma g_i", np.round(sgi, 3))
    print(f"weighted mean of g_i = {(wg * gi).sum() / wg.sum():.4f} "
          f"+- {1 / np.sqrt(wg.sum()):.4f}")
    print(f"slope expected for g = 9.81: {4 * np.pi ** 2 / 9.81:.4f}")

    print("\n== Pendulum: table of sums ==")
    print("x  w  w x  w y  w x^2  w x y")
    for i in range(len(x)):
        print(f"{x[i]:.1f}  {w[i]:.1f}  {w[i] * x[i]:.1f}  {w[i] * y[i]:.1f}  "
              f"{w[i] * x[i] ** 2:.2f}  {w[i] * x[i] * y[i]:.1f}")
    print(f"S = {f['S']:.2f}  Sx = {f['Sx']:.2f}  Sy = {f['Sy']:.2f}  "
          f"Sxx = {f['Sxx']:.2f}  Sxy = {f['Sxy']:.2f}  Delta = {f['D']:.0f}")
    print(f"a = {f['a']:.5f} +- {f['sa']:.5f}   b = {f['b']:.5f} +- {f['sb']:.5f}")
    print(f"cov(a, b) = {f['cov']:.6f}   rho = {f['rho']:.3f}")
    g = 4 * np.pi ** 2 / f["a"]
    sg = g * f["sa"] / f["a"]
    print(f"g = {g:.4f} +- {sg:.4f}   (g - 9.81) / sigma = {(g - 9.81) / sg:.2f}")
    print(f"chi2 = {f['chi2']:.4f}  ndf = {f['ndf']}  chi2/ndf = "
          f"{f['chi2'] / f['ndf']:.3f}  p = {stats.chi2.sf(f['chi2'], f['ndf']):.3f}")
    print("residuals", np.round(y - f["a"] * x - f["b"], 4))
    print("pulls    ", np.round(f["pulls"], 2))
    print(f"sigma(t10) that gives chi2/ndf = 1: "
          f"{SIGMA_T10 * np.sqrt(f['chi2'] / f['ndf']):.3f} s")

    print("\n== Pendulum: chi2 of candidate lines ==")
    for a, b in [(4.0, 0.0), (3.9, 0.05), (4.1, -0.05)]:
        print(f"a = {a}, b = {b}: chi2 = {chi2_line(a, b, x, y, sy):.2f}")
    print("pulls of (4, 0):", np.round((y - 4 * x) / sy, 2),
          "squared:", np.round(((y - 4 * x) / sy) ** 2, 2))

    print("\n== Pendulum: Delta chi2 = 1, centroid, predictions ==")
    for da in (+f["sa"], -f["sa"]):
        a = f["a"] + da
        b = (f["Sy"] - a * f["Sx"]) / f["S"]
        print(f"a = {a:.4f}, b re-minimised = {b:.4f}: chi2 = "
              f"{chi2_line(a, b, x, y, sy):.4f}")
    print(f"b fixed: sigma = 1/sqrt(Sxx) = {1 / np.sqrt(f['Sxx']):.4f}")
    xb = f["Sx"] / f["S"]
    print(f"centroid x = {xb:.4f}, y = {f['Sy'] / f['S']:.4f}, "
          f"sigma there = {1 / np.sqrt(f['S']):.4f}")
    for xx in (0.5,):
        v = xx ** 2 * f["sa"] ** 2 + f["sb"] ** 2
        print(f"T^2 at {xx} m = {f['a'] * xx + f['b']:.4f} +- "
              f"{np.sqrt(v + 2 * xx * f['cov']):.4f} (without covariance "
              f"{np.sqrt(v):.4f})")
    a0, sa0 = f["Sxy"] / f["Sxx"], 1 / np.sqrt(f["Sxx"])
    print(f"b = 0 fixed: a = {a0:.4f} +- {sa0:.4f}, g = {4 * np.pi ** 2 / a0:.4f} "
          f"+- {4 * np.pi ** 2 / a0 * sa0 / a0:.4f}, chi2 = "
          f"{chi2_line(a0, 0, x, y, sy):.3f}")

    print("\n== Pendulum: matrix form, polyfit, curve_fit ==")
    A = np.column_stack([x, np.ones_like(x)])
    N = A.T @ (A * w[:, None])
    print("A^T W A =\n", N, "\nA^T W y =", A.T @ (w * y))
    print("inverse =\n", np.linalg.inv(N))
    theta, *_ = np.linalg.lstsq(A / sy[:, None], y / sy, rcond=None)
    print("lstsq   ", theta)
    p, c = np.polyfit(x, y, 1, w=1 / sy, cov="unscaled")
    print("polyfit ", p, np.sqrt(np.diag(c)))

    def line(x, a, b):
        return a * x + b

    p, c = curve_fit(line, x, y, sigma=sy, absolute_sigma=True)
    print("curve_fit", p, np.sqrt(np.diag(c)))
    p, c = curve_fit(line, x, y, sigma=sy)
    print("curve_fit, absolute_sigma=False:", np.sqrt(np.diag(c)))
    A3 = np.column_stack([x ** 2, x, np.ones_like(x)])
    N3 = A3.T @ (A3 * w[:, None])
    th3 = np.linalg.solve(N3, A3.T @ (w * y))
    print("quadratic term:", th3, "+-", np.sqrt(np.diag(np.linalg.inv(N3))),
          "chi2", (((y - A3 @ th3) / sy) ** 2).sum())

    print("\n== Pendulum: gradient descent ==")
    for eta, steps in ((GD_ETA, 500), (GD_ETA_LARGE, 5)):
        rows = descent(x, y, sy, eta=eta, steps=steps)
        print(f"eta = {eta}")
        for k, a, b, ga, gb, c2 in rows:
            if k <= 5 or k in (10, 20, 50, 100, 200, 500):
                print(f"  {int(k):3d}  a = {a:.4f}  b = {b:.4f}  "
                      f"grad = ({ga:.1f}, {gb:.1f})  chi2 = {c2:.2f}")
    eig = np.linalg.eigvalsh(2 * N)
    print(f"largest stable eta = 2 / {eig.max():.0f} = {2 / eig.max():.2e}")
    H = 2 * N
    a, b = GD_START
    grad = np.array([-2 * (f["Sxy"] - a * f["Sxx"] - b * f["Sx"]),
                     -2 * (f["Sy"] - a * f["Sx"] - b * f["S"])])
    print("one Newton step from the start:", np.array([a, b]) - np.linalg.solve(H, grad))

    print("\n== Pendulum: polynomial degree, wrong model, outlier, scale error ==")
    for deg in range(0, 9):
        c = np.polyfit(x, y, deg, w=1 / sy)
        c2 = (((y - np.polyval(c, x)) / sy) ** 2).sum()
        print(f"degree {deg}: chi2 = {c2:.2f}, ndf = {8 - deg}, "
              f"T^2 at 1.2 m = {np.polyval(c, 1.2):.2f}")
    c = np.polyfit(x, T, 1, w=np.full(9, 100.0))
    pl = (T - np.polyval(c, x)) / 0.01
    print(f"T against length, straight line: chi2 = {(pl ** 2).sum():.1f}, pulls",
          np.round(pl, 1))
    t = t10.copy()
    t[2] = 16.21
    yo, so = (t / 10) ** 2, 2 * (t / 10) * 0.01
    fo = line_fit(x, yo, so)
    go = 4 * np.pi ** 2 / fo["a"]
    print(f"12.61 typed as 16.21: g = {go:.3f} +- {go * fo['sa'] / fo['a']:.3f}, "
          f"chi2 = {fo['chi2']:.1f}, largest pull = {fo['pulls'].max():.1f}")
    fs = line_fit(x * 1.01, y, sy)
    print(f"all lengths 1 % too long: g = {4 * np.pi ** 2 / fs['a']:.3f}, "
          f"chi2 = {fs['chi2']:.4f}")

    print("\n== D0: histogram and fit ==")
    M = d0_mass()
    d = d0_fit()
    print(f"rows {len(M)}, in window {d['n'].sum()}, bins {len(d['n'])}, "
          f"smallest {d['n'].min()}, largest {d['n'].max()}")
    for name, v, e in zip(("A", "mu", "sigma", "c0", "c1"), d["popt"], d["err"]):
        print(f"{name:6s} = {v:10.4f} +- {e:.4f}")
    print(f"chi2 = {d['chi2']:.2f}  ndf = {d['ndf']}  chi2/ndf = "
          f"{d['chi2'] / d['ndf']:.3f}  p = {stats.chi2.sf(d['chi2'], d['ndf']):.3f}"
          f"  model evaluations = {d['nfev']}")
    print(f"pulls: mean {d['pulls'].mean():.2f}, std {d['pulls'].std():.2f}, "
          f"largest |pull| {np.abs(d['pulls']).max():.2f}, "
          f"beyond 2: {(np.abs(d['pulls']) > 2).sum()}")
    corr = d["pcov"] / np.outer(d["err"], d["err"])
    print("correlation matrix\n", np.round(corr, 2))
    A_, _, sg_ = d["popt"][:3]
    J = np.array([sg_, 0, A_, 0, 0]) * np.sqrt(2 * np.pi) / 2.0
    print(f"signal events = {A_ * sg_ * np.sqrt(2 * np.pi) / 2:.0f} +- "
          f"{np.sqrt(J @ d['pcov'] @ J):.0f} (without covariance "
          f"{np.sqrt((J ** 2 * np.diag(d['pcov'])).sum()):.0f})")
    print("\n== D0: one histogram, k-parameter models (1820-1910, 45 bins) ==")
    alt = _d0_alt_models()
    for key, (_, p, c2, ndf, e) in alt.items():
        pv = stats.chi2.sf(c2, ndf)
        mu = f"{p[1]:.2f} +- {e[1]:.2f}" if len(p) > 2 else "-"
        print(f"model {key:14s}: k = {len(p)}, chi2 = {c2:.1f}, ndf = {ndf}, "
              f"chi2/ndf = {c2 / ndf:.2f}, p = "
              f"{f'{pv:.2f}' if pv >= 0.01 else f'{pv:.1e}'}, mu = {mu}")
    c2 = {k: v[2] for k, v in alt.items()}
    mus = {k: v[1][1] for k, v in alt.items() if k != "line"}
    p_line = stats.chi2.sf(c2["gauss_line"], alt["gauss_line"][3])
    print(f"Delta chi2: slope c1 {c2['gauss_const'] - c2['gauss_line']:.1f}, "
          f"second Gaussian {c2['gauss_line'] - c2['two_gauss']:.1f}; "
          f"p = {p_line:.3f} is 1 fit in {1 / p_line:.0f}")
    acc = [mus[k] for k in ("gauss_line", "gauss_parabola", "two_gauss")]
    gap = 1864.84 - mus["gauss_line"]
    print(f"mu shift of the constant background "
          f"{mus['gauss_line'] - mus['gauss_const']:.3f}; accepted models agree "
          f"within {max(acc) - min(acc):.3f}; PDG 1864.84 lies {gap:.2f} above "
          f"the reported mu, {gap / alt['gauss_line'][4][1]:.1f} times its error")

    print("\n== D0: move the window (mean of the rows against the fit) ==")
    means, sems = {}, {}
    for lo, hi in ((None, None), (1840, 1890), (1850, 1880), (1855, 1875),
                   (1854, 1874)):
        r = M if lo is None else M[(M > lo) & (M < hi)]
        means[lo], sems[lo] = r.mean(), r.std(ddof=1) / np.sqrt(len(r))
        label = "all rows" if lo is None else f"{lo} < M < {hi}"
        print(f"mean of the rows, {label}: N = {len(r)}, "
              f"mean = {r.mean():.2f} +- {sems[lo]:.2f}")
    l09 = [means[k] for k in (None, 1840, 1850, 1855)]
    spread = max(l09) - min(l09)
    print(f"Lecture 09 means lie {spread:.3f} apart, {spread / sems[1855]:.1f} "
          f"times the smallest error; window moved by 1 MeV moves the mean by "
          f"{means[1855] - means[1854]:.3f}")
    fits = []
    for shift in (-4, 0, 4):
        lo, hi = D0_WINDOW[0] + shift, D0_WINDOW[1] + shift
        dd = d0_fit(lo=lo, hi=hi)
        fits.append(dd["popt"][1])
        print(f"fit, window {lo:.0f}-{hi:.0f}, 45 bins: mu = {dd['popt'][1]:.2f} "
              f"+- {dd['err'][1]:.2f}, chi2 = {dd['chi2']:.1f}/{dd['ndf']}")
    print(f"fit window moved by 4 MeV moves mu by {fits[1] - fits[0]:.3f} "
          f"(down) and {fits[2] - fits[1]:.3f} (up)")
    for lo, hi, bins in ((1815, 1915, 50), (1820, 1910, 90), (1820, 1910, 30)):
        dd = d0_fit(lo=lo, hi=hi, bins=bins,
                    p0=[2300 * 45 / bins * (hi - lo) / 90, 1865, 8,
                        1400 * 45 / bins * (hi - lo) / 90, 0])
        print(f"window {lo}-{hi}, {bins} bins: mu = {dd['popt'][1]:.2f}, sigma = "
              f"{abs(dd['popt'][2]):.2f}, chi2 = {dd['chi2']:.1f}/{dd['ndf']}, "
              f"edge pulls {dd['pulls'][0]:.1f}, {dd['pulls'][-1]:.1f}")

    print("\n== D0: starting values ==")
    m, n, s = d["m"], d["n"], d["s"]
    for p0 in (D0_P0, [2300, 1850, 3, 1400, 0], [2300, 1840, 2, 1400, 0], None):
        with warnings.catch_warnings(record=True) as wlist:
            warnings.simplefilter("always")
            p, c = curve_fit(d0_model, m, n, p0=p0, sigma=s, absolute_sigma=True)
        c2 = (((n - d0_model(m, *p)) / s) ** 2).sum()
        print(f"p0 = {p0}: A = {p[0]:.0f}, mu = {p[1]:.2f} +- {np.sqrt(c[1, 1]):.2f},"
              f" sigma = {p[2]:.2f}, chi2 = {c2:.1f}",
              "| warning:", wlist[0].category.__name__ if wlist else "none")
    print(f"chi2 at the starting values {D0_P0}: "
          f"{(((n - d0_model(m, *D0_P0)) / s) ** 2).sum():.1f}")
    eta, cond, c2 = d0_plain_descent()
    print(f"plain gradient descent, eta = {eta:.4f}, curvature ratio {cond:.0f}: "
          f"chi2 = {c2:.1f} after 100 000 steps")

    print("\n== Counts: sqrt(n) as the uncertainty ==")
    c = np.array([2, 4, 6, 8])
    print(f"counts {c}: mean {c.mean()}, fit of a constant with sigma^2 = n: "
          f"{len(c) / (1 / c).sum():.2f}")
    sb = n[m > 1886]
    print(f"D0 bins above 1886: mean {sb.mean():.1f}, fit of a constant: "
          f"{len(sb) / (1 / sb).sum():.1f}")
    print(f"p-values: chi2.sf(2.65, 7) = {stats.chi2.sf(f['chi2'], 7):.3f}, "
          f"chi2.sf(53.4, 40) = {stats.chi2.sf(d['chi2'], 40):.3f}")


# =============================================================================
# Figures
# =============================================================================

C0, C1, C2, C3 = style.CYCLE[0], style.CYCLE[1], style.CYCLE[2], style.CYCLE[3]
ELL = r"length $\ell$ (m)"


def _pendulum_data_fig():
    x, t10, T, y, sy = pendulum_data()
    xs = np.linspace(0, 1.08, 200)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    ax1.plot(xs, 2 * np.pi * np.sqrt(xs / 9.81), color=style.DIM, lw=1.4, ls="--",
             label=r"$2\pi\sqrt{\ell/g}$ with $g$ = 9.81 m/s$^2$")
    ax1.errorbar(x, T, yerr=0.01, fmt="o", color=C0, ms=6, label="nine rows of the table")
    ax1.set(xlabel=ELL, ylabel=r"period $T$ (s)", xlim=(0, 1.08), ylim=(0, 2.3))
    ax1.set_title(r"$T$ against $\ell$: a curve")
    ax1.legend(loc="lower right")
    ax2.plot(xs, 4 * np.pi ** 2 / 9.81 * xs, color=style.DIM, lw=1.4, ls="--",
             label=r"$(4\pi^2/g)\,\ell$ with $g$ = 9.81 m/s$^2$")
    ax2.errorbar(x, y, yerr=sy, fmt="o", color=C1, ms=6, label=r"$T^2$ with its uncertainty")
    ax2.set(xlabel=ELL, ylabel=r"$T^2$ (s$^2$)", xlim=(0, 1.08), ylim=(0, 4.5))
    ax2.set_title(r"$T^2$ against $\ell$: a straight line")
    ax2.legend(loc="lower right")
    style.save(fig, "viz_fitting_pendulum_data")


CANDIDATES = [("A", 4.0, 0.0, C0), ("B", 3.9, 0.05, C1), ("C", 4.1, -0.05, C2)]


def _candidates():
    x, t10, T, y, sy = pendulum_data()
    xs = np.linspace(0.1, 1.1, 50)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    for name, a, b, col in CANDIDATES:
        lab = rf"{name}:  $a$ = {a},  $b$ = {b:g}".replace("-", "−")
        ax1.plot(xs, a * xs + b, color=col, lw=1.6, label=lab)
        ax2.plot(xs, (a - 4) * xs + b, color=col, lw=1.8, label=lab)
    ax1.errorbar(x, y, yerr=sy, fmt="o", color=style.FG, ms=5, zorder=5)
    ax1.set(xlabel=ELL, ylabel=r"$T^2$ (s$^2$)", xlim=(0.1, 1.1))
    ax1.set_title("Three candidate lines")
    ax1.legend(loc="upper left")
    ax2.errorbar(x, y - 4 * x, yerr=sy, fmt="o", color=style.FG, ms=5, zorder=5,
                 capsize=3)
    ax2.axhline(0, color=style.DIM, lw=0.8)
    ax2.set(xlabel=ELL, ylabel=r"$T^2 - 4\ell$ (s$^2$)", xlim=(0.1, 1.1),
            ylim=(-0.095, 0.095))
    ax2.set_title(r"The same, with $4\ell$ subtracted")
    style.save(fig, "viz_fitting_candidates")


def _likelihood():
    x, t10, T, y, sy = pendulum_data()
    f = line_fit(x, y, sy)
    zoom = 12
    xs = np.linspace(0.1, 1.1, 50)
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    ax.plot(xs, f["a"] * xs + f["b"], color=C0, lw=2, label=r"model $f(x;\theta)$")
    for i in (0, 2, 5, 8):
        mu = f["a"] * x[i] + f["b"]
        s = zoom * sy[i]
        t = np.linspace(mu - 3.2 * s, mu + 3.2 * s, 200)
        pdf = np.exp(-(t - mu) ** 2 / (2 * s ** 2))
        ax.fill_betweenx(t, x[i], x[i] + 0.11 * pdf, color=C1, alpha=0.25, lw=0)
        ax.plot(x[i] + 0.11 * pdf, t, color=C1, lw=1.5)
        ax.plot([x[i], x[i]], [mu - 3.2 * s, mu + 3.2 * s], color=style.DIM, lw=0.8)
        yi = mu + zoom * (y[i] - mu)
        ax.plot(x[i], yi, "o", color=style.FG, ms=7, zorder=6)
        ax.annotate("", xy=(x[i] - 0.035, mu + s), xytext=(x[i] - 0.035, mu),
                    arrowprops=dict(arrowstyle="<->", color=style.DIM, lw=1))
        ax.text(x[i] - 0.05, mu + 0.5 * s, r"$\sigma_i$", color=style.DIM,
                ha="right", va="center", fontsize=11)
    ax.plot([], [], "o", color=style.FG, ms=7, label=r"measured $y_i$")
    ax.plot([], [], color=C1, lw=1.5, label=r"probability density of $y_i$")
    ax.set(xlabel=r"$x$", ylabel=r"$y$", xlim=(0.08, 1.2), ylim=(0.2, 5.5))
    ax.legend(loc="upper left")
    ax.text(0.98, 0.04, f"distances and widths drawn {zoom} times larger",
            transform=ax.transAxes, ha="right", color=style.DIM, fontsize=9.5)
    style.save(fig, "viz_fitting_likelihood")


def _pendulum_fit():
    x, t10, T, y, sy = pendulum_data()
    f = line_fit(x, y, sy)
    xs = np.linspace(0, 1.08, 50)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    ax1.plot(xs, f["a"] * xs + f["b"], color=C0, lw=2,
             label=rf"$T^2$ = {f['a']:.3f} $\ell$ + {f['b']:.3f}")
    ax1.errorbar(x, y, yerr=sy, fmt="o", color=style.FG, ms=5, zorder=5, label="data")
    ax1.set(xlabel=ELL, ylabel=r"$T^2$ (s$^2$)", xlim=(0, 1.08), ylim=(0, 4.5))
    ax1.set_title("Data and fitted line")
    ax1.legend(loc="upper left")
    ax2.axhline(0, color=C0, lw=2)
    ax2.errorbar(x, y - f["a"] * x - f["b"], yerr=sy, fmt="o", color=style.FG, ms=5,
                 capsize=3, zorder=5)
    ax2.set(xlabel=ELL, ylabel=r"residual $y_i - f(x_i)$ (s$^2$)", xlim=(0.1, 1.1),
            ylim=(-0.075, 0.075))
    ax2.set_title(rf"Residuals:  $\chi^2$ = {f['chi2']:.2f} for {f['ndf']} degrees of freedom")
    style.save(fig, "viz_fitting_pendulum_fit")


def _ellipse(center, cov2, dchi2, n=400):
    """Points of the contour chi2(theta) = chi2_min + dchi2 for a 2x2 cov."""
    L = np.linalg.cholesky(cov2)
    t = np.linspace(0, 2 * np.pi, n)
    circle = np.vstack([np.cos(t), np.sin(t)])
    return center[:, None] + np.sqrt(dchi2) * (L @ circle)


def _chi2_curvature():
    x, t10, T, y, sy = pendulum_data()
    f = line_fit(x, y, sy)
    a, b, sa, sb = f["a"], f["b"], f["sa"], f["sb"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.3))

    aa = np.linspace(a - 2.3 * sa, a + 2.3 * sa, 200)
    prof = f["chi2"] + (aa - a) ** 2 / sa ** 2
    fixed = f["chi2"] + (aa - a) ** 2 * f["Sxx"]
    ax1.plot(aa, fixed, color=style.DIM, lw=1.5, ls="--",
             label=r"$b$ held at $\hat b$")
    ax1.plot(aa, prof, color=C0, lw=2.2, label=r"$b$ re-minimised for each $a$")
    ax1.axhline(f["chi2"], color=style.DIM, lw=0.8)
    ax1.axhline(f["chi2"] + 1, color=C1, lw=1.2)
    for v in (a - sa, a + sa):
        ax1.plot([v, v], [0, f["chi2"] + 1], color=C1, lw=1.2, ls=":")
    ax1.annotate("", xy=(a + sa, 1.2), xytext=(a, 1.2),
                 arrowprops=dict(arrowstyle="<->", color=C1, lw=1.2))
    ax1.text(a + sa / 2, 1.45, rf"$\sigma_a$ = {sa:.3f}", color=C1, ha="center", fontsize=11)
    ax1.text(a - 2.25 * sa, f["chi2"] + 1.15, r"$\chi^2_{\min} + 1$", color=C1, fontsize=11)
    ax1.text(a + 2.25 * sa, f["chi2"] - 0.5, rf"$\chi^2_{{\min}}$ = {f['chi2']:.2f}",
             color=style.DIM, fontsize=11, ha="right")
    ax1.set(xlabel=r"slope $a$ (s$^2$/m)", ylabel=r"$\chi^2$", ylim=(0, 8.5),
            xlim=(aa[0], aa[-1]))
    ax1.set_title(r"$\chi^2$ against the slope")
    ax1.legend(loc="lower left", fontsize=9.5)

    center = np.array([a, b])
    cov2 = np.array([[sa ** 2, f["cov"]], [f["cov"], sb ** 2]])
    e1, e2 = _ellipse(center, cov2, 1.0), _ellipse(center, cov2, 2.30)
    ax2.fill(e2[0], e2[1], color=C1, alpha=0.15, lw=0)
    ax2.plot(e2[0], e2[1], color=C1, lw=1.8, label=r"$\Delta\chi^2$ = 2.30")
    ax2.fill(e1[0], e1[1], color=C0, alpha=0.25, lw=0)
    ax2.plot(e1[0], e1[1], color=C0, lw=2.2, label=r"$\Delta\chi^2$ = 1")
    for v in (a - sa, a + sa):
        ax2.axvline(v, color=C0, lw=1.0, ls="--", alpha=0.8)
    for v in (b - sb, b + sb):
        ax2.axhline(v, color=C0, lw=1.0, ls="--", alpha=0.8)
    ax2.plot(a, b, "o", color=style.FG, ms=6, zorder=5, label="minimum")
    ax2.text(0.04, 0.06, rf"$\rho$ = {f['rho']:.2f}".replace("-", "−"),
             transform=ax2.transAxes, fontsize=12)
    ax2.set(xlabel=r"slope $a$ (s$^2$/m)", ylabel=r"intercept $b$ (s$^2$)",
            xlim=(a - 2.3 * sa, a + 2.3 * sa), ylim=(b - 2.3 * sb, b + 2.3 * sb))
    ax2.set_title(r"Contours of $\chi^2$ in the ($a$, $b$) plane")
    ax2.legend(loc="upper right")
    style.save(fig, "viz_fitting_chi2_curvature")


def _descent_fig():
    x, t10, T, y, sy = pendulum_data()
    f = line_fit(x, y, sy)
    good = descent(x, y, sy, eta=GD_ETA, steps=200)
    bad = descent(x, y, sy, eta=GD_ETA_LARGE, steps=4)
    levels = f["chi2"] + np.array([10, 50, 200, 500, 1500, 4000, 12000, 40000, 150000])

    def contours(ax, alim, blim):
        aa, bb = np.meshgrid(np.linspace(*alim, 220), np.linspace(*blim, 220))
        da, db = aa - f["a"], bb - f["b"]
        z = f["chi2"] + f["Sxx"] * da ** 2 + 2 * f["Sx"] * da * db + f["S"] * db ** 2
        ax.contour(aa, bb, z, levels=levels, colors=style.DIM, linewidths=0.8, alpha=0.7)
        ax.plot(f["a"], f["b"], "*", color=style.FG, ms=13, zorder=6)
        ax.set(xlabel=r"slope $a$", ylabel=r"intercept $b$", xlim=alim, ylim=blim)
        ax.grid(False)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11.6, 4.1),
                                        gridspec_kw={"width_ratios": [1, 1, 1.05]})
    contours(ax1, (2.9, 4.2), (-0.25, 0.65))
    ax1.plot(good[:, 1], good[:, 2], "-", color=C0, lw=1.3)
    ax1.plot(good[:6, 1], good[:6, 2], "o", color=C0, ms=5)
    ax1.plot(good[0, 1], good[0, 2], "o", color=C1, ms=8, zorder=5)
    ax1.text(good[0, 1] + 0.04, good[0, 2] - 0.05, "start", color=C1, fontsize=10)
    ax1.text(f["a"] - 0.03, f["b"] - 0.09, "minimum", color=style.FG, fontsize=10,
             ha="center")
    ax1.set_title(r"$\eta$ = 3 × 10$^{-5}$: 200 steps")
    contours(ax2, (0.0, 6.0), (-6.5, 4.5))
    ax2.plot(bad[:, 1], bad[:, 2], "o-", color=style.BAD, lw=1.4, ms=5)
    ax2.plot(bad[0, 1], bad[0, 2], "o", color=C1, ms=8, zorder=5)
    for k in range(1, 5):
        ax2.annotate(str(k), (bad[k, 1], bad[k, 2]), textcoords="offset points",
                     xytext=(7, 4), color=style.BAD, fontsize=10)
    ax2.set_title(r"$\eta$ = 1 × 10$^{-4}$: 4 steps")
    k = np.arange(201)
    ax3.semilogy(k, good[:, 5], color=C0, lw=2, label=r"$\eta$ = 3 × 10$^{-5}$")
    badlong = descent(x, y, sy, eta=GD_ETA_LARGE, steps=8)
    ax3.semilogy(badlong[:, 0], badlong[:, 5], "o-", color=style.BAD, lw=1.6, ms=4,
                 label=r"$\eta$ = 1 × 10$^{-4}$")
    ax3.axhline(f["chi2"], color=style.DIM, lw=1, ls="--")
    ax3.text(198, f["chi2"] * 1.5, rf"minimum {f['chi2']:.2f}", color=style.DIM,
             ha="right", fontsize=10)
    ax3.set(xlabel="step", ylabel=r"$\chi^2$", xlim=(-6, 200), ylim=(1, 3e8))
    ax3.set_title(r"$\chi^2$ against the step")
    ax3.legend(loc="upper right")
    style.save(fig, "viz_fitting_descent")


def _d0_data():
    M = d0_mass()
    n_all, edges = np.histogram(M, bins=65, range=(1800, 1930))
    m, n, s = d0_hist()
    fig, ax = plt.subplots(figsize=(11.0, 4.3))
    ax.stairs(n_all, edges, color=style.DIM, lw=1.2, label="all rows of the file, 2 MeV bins")
    ax.axvspan(1800, D0_WINDOW[0], color="#000000", alpha=0.28, lw=0)
    ax.axvspan(D0_WINDOW[1], 1930, color="#000000", alpha=0.28, lw=0)
    for v in D0_WINDOW:
        ax.axvline(v, color=C1, lw=1.2, ls="--")
    ax.errorbar(m, n, yerr=s, fmt="o", color=C0, ms=4, lw=1,
                label=r"45 bins used in the fit, with $\sqrt{n}$")
    ax.text(1865, 600, "fit window 1820 to 1910", color=C1, ha="center", fontsize=11)
    ax.set(xlabel=r"$M$ (MeV/$c^2$)", ylabel="entries per 2 MeV", xlim=(1800, 1930),
           ylim=(0, 4200))
    ax.legend(loc="upper left", bbox_to_anchor=(0.16, 1.0))
    style.save(fig, "viz_fitting_d0_data")


def _d0_fit_fig():
    d = d0_fit()
    m, n, s, p, e = d["m"], d["n"], d["s"], d["popt"], d["err"]
    ms = np.linspace(*D0_WINDOW, 400)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11.0, 4.9), sharex=True,
                                   gridspec_kw={"height_ratios": [3, 1]})
    bkg = p[3] + p[4] * (ms - 1865)
    ax1.fill_between(ms, bkg, d0_model(ms, *p), color=C1, alpha=0.25, lw=0,
                     label="Gaussian")
    ax1.plot(ms, bkg, color=C2, lw=1.6, ls="--", label="linear background")
    ax1.plot(ms, d0_model(ms, *p), color=C1, lw=2.2, label="fitted model")
    ax1.errorbar(m, n, yerr=s, fmt="o", color=style.FG, ms=3.5, lw=1,
                 label=r"data with $\sqrt{n}$")
    ax1.set(ylabel="entries per 2 MeV", ylim=(0, 4200), xlim=D0_WINDOW)
    ax1.text(0.015, 0.93,
             rf"$\mu$ = {p[1]:.2f} ± {e[1]:.2f} MeV/$c^2$" "\n"
             rf"$\sigma$ = {abs(p[2]):.2f} ± {e[2]:.2f} MeV/$c^2$" "\n"
             rf"$\chi^2$/ndf = {d['chi2']:.1f}/{d['ndf']}",
             transform=ax1.transAxes, va="top", fontsize=11, linespacing=1.5)
    ax1.legend(loc="upper right")
    ax2.axhspan(-2, 2, color=style.DIM, alpha=0.15, lw=0)
    ax2.axhline(0, color=style.DIM, lw=1)
    ax2.plot(m, d["pulls"], "o", color=C0, ms=4)
    ax2.set(xlabel=r"$M$ (MeV/$c^2$)", ylabel="pull", ylim=(-4, 4))
    style.save(fig, "viz_fitting_d0_fit")


def _chi2_dist():
    x, t10, T, y, sy = pendulum_data()
    f = line_fit(x, y, sy)
    d = d0_fit()
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0))
    cases = [(axes[0], 7, f["chi2"], "Pendulum, straight line", C0, 24, 2),
             (axes[1], 40, d["chi2"], r"$D^0$ peak, Gaussian on a line", C1, 85, 1)]
    for ax, ndf, obs, title, col, xmax, digits in cases:
        t = np.linspace(0.01, xmax, 500)
        pdf = stats.chi2.pdf(t, ndf)
        ax.plot(t, pdf, color=style.FG, lw=1.8)
        tail = t >= obs
        ax.fill_between(t[tail], pdf[tail], color=col, alpha=0.35, lw=0)
        ax.axvline(obs, color=col, lw=2)
        ax.axvline(ndf, color=style.DIM, lw=1, ls="--")
        top = pdf.max()
        ax.text(ndf, top * 1.08, f"mean = ndf = {ndf}", color=style.DIM, ha="center",
                fontsize=10)
        ax.text(0.97, 0.80, rf"observed $\chi^2$ = {obs:.{digits}f}" "\n"
                rf"area to the right: $p$ = {stats.chi2.sf(obs, ndf):.2f}",
                transform=ax.transAxes, ha="right", va="top", color=col, fontsize=11,
                linespacing=1.5)
        ax.set(xlabel=r"$\chi^2$", ylabel="probability density", xlim=(0, xmax),
               ylim=(0, top * 1.22))
        ax.set_title(title)
    style.save(fig, "viz_fitting_chi2_dist")


def _d0_models():
    m, n, s = d0_hist()
    alt = _d0_alt_models()
    rows = [("line", "Straight line, 2 parameters"),
            ("gauss_const", "Gaussian on a constant, 4 parameters"),
            ("gauss_line", "Gaussian on a line, 5 parameters")]
    fig, axes = plt.subplots(3, 1, figsize=(11.0, 5.0), sharex=True)
    for ax, (key, label) in zip(axes, rows):
        fn, p, c2, ndf, _ = alt[key]
        pulls = (n - fn(m, *p)) / s
        lim = 52 if key == "line" else 4.6
        if key != "line":
            ax.axhspan(-2, 2, color=style.DIM, alpha=0.15, lw=0)
        ax.axhline(0, color=style.DIM, lw=1)
        ax.plot(m, pulls, "o", color=C0 if key == "gauss_line" else C1, ms=4)
        ax.set(ylim=(-lim * 0.5 if key == "line" else -lim, lim), ylabel="pull",
               xlim=D0_WINDOW)
        ax.set_title(rf"{label}:  $\chi^2$/ndf = {c2:.1f}/{ndf}", loc="left",
                     fontsize=11, fontweight="normal")
    axes[-1].set_xlabel(r"$M$ (MeV/$c^2$)")
    style.save(fig, "viz_fitting_d0_models")


def _overfit():
    x, t10, T, y, sy = pendulum_data()
    f = line_fit(x, y, sy)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11.6, 4.2))

    c = np.polyfit(x, T, 1, w=np.full(9, 100.0))
    pl = (T - np.polyval(c, x)) / 0.01
    ax1.axhspan(-2, 2, color=style.DIM, alpha=0.15, lw=0)
    ax1.axhline(0, color=style.DIM, lw=1)
    ax1.plot(x, pl, "o", color=C1, ms=6)
    ax1.set(xlabel=ELL, ylabel="pull", ylim=(-8.5, 8.5), xlim=(0.1, 1.1))
    ax1.set_title(rf"Line through $T(\ell)$" "\n" rf"$\chi^2$/ndf = {(pl ** 2).sum():.1f}/7",
                  fontsize=12.5)

    ax2.axhspan(-2, 2, color=style.DIM, alpha=0.15, lw=0)
    ax2.axhline(0, color=style.DIM, lw=1)
    ax2.plot(x, f["pulls"], "o", color=C0, ms=6)
    ax2.set(xlabel=ELL, ylabel="pull", ylim=(-8.5, 8.5), xlim=(0.1, 1.1))
    ax2.set_title(rf"Line through $T^2(\ell)$" "\n" rf"$\chi^2$/ndf = {f['chi2']:.2f}/7",
                  fontsize=12.5)

    xs = np.linspace(0.13, 1.07, 600)
    c8 = np.polyfit(x, y, 8, w=1 / sy)
    ax3.plot(xs, (f["a"] - 4) * xs + f["b"], color=C0, lw=1.8, label="line")
    ax3.plot(xs, np.polyval(c8, xs) - 4 * xs, color=style.BAD, lw=1.8,
             label="polynomial of degree 8")
    ax3.errorbar(x, y - 4 * x, yerr=sy, fmt="o", color=style.FG, ms=5, capsize=3, zorder=5)
    ax3.set(xlabel=ELL, ylabel=r"$T^2 - 4\ell$ (s$^2$)", ylim=(-0.16, 0.16),
            xlim=(0.1, 1.1))
    ax3.set_title(r"Polynomial of degree 8 through $T^2(\ell)$" "\n" r"$\chi^2$/ndf = 0/0",
                  fontsize=12.5)
    ax3.legend(loc="lower center", fontsize=9)
    style.save(fig, "viz_fitting_overfit")


def _start_values():
    m, n, s = d0_hist()
    ms = np.linspace(*D0_WINDOW, 400)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), sharey=True)
    cases = [([2300, 1865, 8, 1400, 0], C0), ([2300, 1840, 2, 1400, 0], style.BAD)]
    for ax, (p0, col) in zip(axes, cases):
        p, _ = curve_fit(d0_model, m, n, p0=p0, sigma=s, absolute_sigma=True)
        c2 = (((n - d0_model(m, *p)) / s) ** 2).sum()
        ax.errorbar(m, n, yerr=s, fmt="o", color=style.FG, ms=3, lw=0.8)
        ax.plot(ms, d0_model(ms, *p0), color=style.DIM, lw=1.6, ls="--",
                label="model at the starting values")
        ax.plot(ms, d0_model(ms, *p), color=col, lw=2.2,
                label=rf"result, $\chi^2$ = {c2:.1f}")
        ax.set(xlabel=r"$M$ (MeV/$c^2$)", xlim=D0_WINDOW, ylim=(0, 4600))
        ax.set_title(rf"Start: $\mu$ = {p0[1]}, $\sigma$ = {p0[2]}")
        ax.legend(loc="upper right")
    axes[0].set_ylabel("entries per 2 MeV")
    style.save(fig, "viz_fitting_start_values")


D0_PARAMS = ["A", r"$\mu$", r"$\sigma$", r"$c_0$", r"$c_1$"]


def _covariance():
    """Correlation matrix of the D0 fit and the (A, sigma) ellipse."""
    d = d0_fit()
    popt, pcov, err = d["popt"], d["pcov"], d["err"]
    corr = pcov / np.outer(err, err)
    k = len(popt)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.4),
                                   gridspec_kw={"width_ratios": [1, 1.25]})

    cmap = mcolors.LinearSegmentedColormap.from_list(
        "diverging", [style.CYCLE[1], "#333b4a", style.ACCENT])
    norm = mcolors.Normalize(vmin=-1, vmax=1)
    im = ax1.imshow(corr, cmap=cmap, norm=norm)
    ax1.set_xticks(range(k))
    ax1.set_xticklabels(D0_PARAMS, fontsize=12)
    ax1.set_yticks(range(k))
    ax1.set_yticklabels(D0_PARAMS, fontsize=12)
    ax1.grid(False)
    for spine in ax1.spines.values():
        spine.set_visible(False)
    for i in range(k):
        for j in range(k):
            v = np.round(corr[i, j], 2) + 0.0   # kill "-0.00"
            r, g, b, _ = cmap(norm(v))
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            ax1.text(j, i, f"{v:+.2f}".replace("-", "−"), ha="center",
                     va="center", fontsize=11,
                     color="#0b0f14" if lum > 0.55 else style.FG)
    cbar = fig.colorbar(im, ax=ax1, shrink=0.8, pad=0.04)
    cbar.outline.set_visible(False)
    cbar.ax.tick_params(colors=style.DIM, labelsize=9)
    ax1.set_title(r"Correlation matrix of the $D^0$ fit")

    iA, iS = 0, 2
    center = popt[[iA, iS]]
    cov2 = pcov[np.ix_([iA, iS], [iA, iS])]
    e1 = _ellipse(center, cov2, 1.0)
    e2 = _ellipse(center, cov2, 2.30)
    ax2.fill(e2[0], e2[1], color=style.CYCLE[1], alpha=0.18, lw=0)
    ax2.plot(e2[0], e2[1], color=style.CYCLE[1], lw=2.0, label=r"$\Delta\chi^2$ = 2.30")
    ax2.fill(e1[0], e1[1], color=style.ACCENT, alpha=0.28, lw=0)
    ax2.plot(e1[0], e1[1], color=style.ACCENT, lw=2.2, label=r"$\Delta\chi^2$ = 1")
    for v in (center[0] - err[iA], center[0] + err[iA]):
        ax2.axvline(v, color=style.ACCENT, lw=1.0, ls="--", alpha=0.8)
    for v in (center[1] - err[iS], center[1] + err[iS]):
        ax2.axhline(v, color=style.ACCENT, lw=1.0, ls="--", alpha=0.8)
    ax2.plot(*center, "o", color=style.FG, ms=6, zorder=5, label="minimum")
    ax2.text(0.04, 0.06, rf"$\rho(A, \sigma)$ = {corr[iA, iS]:.2f}".replace("-", "−"),
             transform=ax2.transAxes, fontsize=12)
    ax2.set_xlim(center[0] - 2.3 * err[iA], center[0] + 2.3 * err[iA])
    ax2.set_ylim(center[1] - 2.3 * err[iS], center[1] + 2.3 * err[iS])
    ax2.set_xlabel(rf"height $A$:  {popt[iA]:.0f} ± {err[iA]:.0f} per 2 MeV")
    ax2.set_ylabel(rf"width $\sigma$:  {popt[iS]:.2f} ± {err[iS]:.2f} MeV/$c^2$")
    ax2.set_title(r"Contours of $\chi^2$ in the ($A$, $\sigma$) plane")
    ax2.legend(loc="upper right", fontsize=10)

    style.save(fig, "viz_fitting_covariance")


def _outlier():
    x, t10, T, y, sy = pendulum_data()
    f = line_fit(x, y, sy)
    t = t10.copy()
    t[2] = 16.21
    yo, so = (t / 10) ** 2, 2 * (t / 10) * 0.01
    fo = line_fit(x, yo, so)
    xs = np.linspace(0, 1.08, 50)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.1))
    ax1.plot(xs, f["a"] * xs + f["b"], color=C0, lw=1.8, label="fit to the correct table")
    ax1.plot(xs, fo["a"] * xs + fo["b"], color=style.BAD, lw=1.8,
             label="fit with 16.21 in place of 12.61")
    ax1.errorbar(x, yo, yerr=so, fmt="o", color=style.FG, ms=5, zorder=5)
    ax1.plot(x[2], yo[2], "o", color=style.BAD, ms=9, zorder=6)
    ax1.set(xlabel=ELL, ylabel=r"$T^2$ (s$^2$)", xlim=(0, 1.08), ylim=(0, 4.5))
    ax1.set_title("One mistyped value")
    ax1.legend(loc="upper left")
    ax2.axhspan(-2, 2, color=style.DIM, alpha=0.15, lw=0)
    ax2.axhline(0, color=style.DIM, lw=1)
    cols = [style.BAD if i == 2 else style.FG for i in range(9)]
    ax2.scatter(x, fo["pulls"], c=cols, s=40, zorder=5)
    ax2.set(xlabel=ELL, ylabel="pull", xlim=(0.1, 1.1), ylim=(-10, 32))
    ax2.set_title(rf"Pulls of that fit:  $\chi^2$ = {fo['chi2']:.1f} for 7")
    style.save(fig, "viz_fitting_outlier")


FIGURES = {
    "viz_fitting_pendulum_data": _pendulum_data_fig,
    "viz_fitting_candidates": _candidates,
    "viz_fitting_likelihood": _likelihood,
    "viz_fitting_pendulum_fit": _pendulum_fit,
    "viz_fitting_chi2_curvature": _chi2_curvature,
    "viz_fitting_descent": _descent_fig,
    "viz_fitting_d0_data": _d0_data,
    "viz_fitting_d0_fit": _d0_fit_fig,
    "viz_fitting_chi2_dist": _chi2_dist,
    "viz_fitting_d0_models": _d0_models,
    "viz_fitting_overfit": _overfit,
    "viz_fitting_start_values": _start_values,
    "viz_fitting_covariance": _covariance,
    "viz_fitting_outlier": _outlier,
}


if __name__ == "__main__":
    numbers()
