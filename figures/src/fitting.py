"""Figures and numbers for Lecture 9, Parameter Estimation and Fitting.

The main path uses the weather log, lectures/workbook/docs/data/weather.csv,
read with the plain functions of the course module weather.py (copied
below):

  * the four measured hours of 21 July 2019, 20:00 to 23:00 (27.3, 25.6,
    24.6 and 23.6 degC), fitted with one number;
  * the ten yearly means, 2016 to 2025, with x = years since 2016 and an
    uncertainty of sigma = 0.70 degC on each (the scatter of the ten,
    Lecture 8), fitted with a straight line;
  * the 3648 daily means (the days with 24 measured hours), fitted with the
    yearly cycle c - A cos(2 pi (d - d0) / 365.25), d = days since
    1 January 2016.

For the Curious adds two older examples, both read from the same folder:

  * pendulum.csv   nine lengths (cm) and the time of 10 swings (s): T^2
                   against the length, slope 4 pi^2 / g, with 0.1 s assumed
                   on the time of 10 swings;
  * D0_KPi.csv     the mass column M of the LHCb file, 1820 to 1910 MeV/c^2
                   in 45 bins of 2 MeV, a Gaussian on a straight line.

Every number on the slides, the seminar page and the lecture page comes from
the functions in the first half of this file. Print them all with

    python figures/src/fitting.py

(needs numpy and scipy). The second half draws the figures
public/figures/viz_fitting_*.svg; build them with

    python figures/src/build.py --only fitting
"""
from datetime import date, timedelta

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data"
PATH = DATA / "weather.csv"

HOURS = [27.3, 25.6, 24.6, 23.6]   # 21 July 2019, 20:00 to 23:00
SIGMA = 0.70                       # degC, the uncertainty of one yearly mean
GUESS_A = (0.0, 7.16)              # a flat line at the mean
GUESS_B = (0.1, 6.7)               # rising 1 degC per decade
OMEGA = 2 * np.pi / 365.25         # one turn per year, per day
CYCLE_START = (7.0, 11.0, 15.0)    # c, A, d0 read off the plot of the daily means
GD_HOURS = (20.0, 0.1, 0.3)        # start, a good step size, a step size too large
GD_LINE = ((0.0, 7.0), 0.003)      # start (a, b) and step size for the line
GD_CYCLE_ETA = 0.5                 # step size for the cycle (mean squared residual)

SIGMA_T10 = 0.1                    # s, assumed uncertainty of the time of 10 swings
D0_WINDOW = (1820.0, 1910.0)       # MeV/c^2
D0_BINS = 45                       # 2 MeV per bin
D0_P0 = [2300, 1865, 8, 1400, 0]   # A, mu, sigma, c0, c1 read off the histogram


# =============================================================================
# weather.py, as the course writes it
# =============================================================================

MISSING = -999.0


def read_lines(path):
    return open(path).read().splitlines()[1:]


def temp_of(line):
    return float(line.split(",")[1])


def group(path, start, stop):
    groups = {}
    for line in read_lines(path):
        temp = temp_of(line)
        if temp == MISSING:
            continue
        key = line[start:stop]
        if key not in groups:
            groups[key] = []
        groups[key].append(temp)
    return groups


def mean(values):
    return sum(values) / len(values)


# =============================================================================
# Numbers
# =============================================================================

def sum_squares(mu, values=HOURS):
    """S(mu): the sum of the squared deviations of the values from mu."""
    total = 0.0
    for v in values:
        total = total + (v - mu) ** 2
    return total


def yearly_means():
    """x = years since 2016 (0 to 9), y = the mean of each year's measured hours."""
    years = group(PATH, 0, 4)
    y = np.array([mean(years[k]) for k in years])
    return np.arange(len(y), dtype=float), y, list(years)


def line_fit(x, y, sigma=SIGMA):
    """The straight line y = a x + b by the five sums (equal sigma)."""
    n = len(x)
    sx, sy = x.sum(), y.sum()
    sxx, sxy = (x * x).sum(), (x * y).sum()
    d = n * sxx - sx ** 2
    a = (n * sxy - sx * sy) / d
    b = (sxx * sy - sx * sxy) / d
    r = y - a * x - b
    sa, sb = sigma * np.sqrt(n / d), sigma * np.sqrt(sxx / d)
    cov = -sigma ** 2 * sx / d
    return dict(n=n, sx=sx, sy=sy, sxx=sxx, sxy=sxy, d=d, a=a, b=b, r=r,
                chi2=(r ** 2).sum() / sigma ** 2, sa=sa, sb=sb, cov=cov,
                rho=cov / (sa * sb))


def chi2_line(a, b, x, y, sigma=SIGMA):
    return (((y - a * x - b) / sigma) ** 2).sum()


def chi2_profile(a, x, y, sigma=SIGMA):
    """chi2 at slope a with the intercept re-minimised: b = mean(y - a x)."""
    b = (y - a * x).mean()
    return chi2_line(a, b, x, y, sigma)


def descent_hours(start, eta, steps):
    """Gradient descent on S(mu) of the four hours. Rows: mu, dS/dmu."""
    mu, rows = start, []
    for _ in range(steps + 1):
        g = -2 * (sum(HOURS) - len(HOURS) * mu)
        rows.append((mu, g))
        mu = mu - eta * g
    return rows


def descent_line(x, y, start=GD_LINE[0], eta=GD_LINE[1], steps=1000):
    """Gradient descent on S(a, b) = sum (a x + b - y)^2. Rows: step, a, b, S."""
    a, b = start
    rows = [(0, a, b, ((a * x + b - y) ** 2).sum())]
    for k in range(1, steps + 1):
        r = a * x + b - y
        ga, gb = 2 * (r * x).sum(), 2 * r.sum()
        a, b = a - eta * ga, b - eta * gb
        rows.append((k, a, b, ((a * x + b - y) ** 2).sum()))
    return np.array(rows)


def daily_means():
    """d = days since 2016-01-01 and T = the daily means, days with 24 hours only."""
    temps = np.array([temp_of(line) for line in read_lines(PATH)])
    days = temps.reshape(-1, 24)
    good = (days != MISSING).all(axis=1)
    return np.arange(len(days))[good].astype(float), days[good].mean(axis=1)


def cycle(d, c, amp, d0):
    return c - amp * np.cos(OMEGA * (d - d0))


def cycle_fit(d, T):
    """Least squares for c + alpha cos(wd) + beta sin(wd), turned into c, A, d0."""
    A = np.column_stack([np.ones_like(d), np.cos(OMEGA * d), np.sin(OMEGA * d)])
    (c, al, be), *_ = np.linalg.lstsq(A, T, rcond=None)
    amp = np.hypot(al, be)
    d0 = ((np.arctan2(be, al) + np.pi) / OMEGA) % 365.25   # the coldest day
    r = T - cycle(d, c, amp, d0)
    s = r.std(ddof=3)
    V = np.linalg.inv(A.T @ A) * s ** 2
    J = np.array([0.0, al / amp, be / amp])
    return dict(c=c, alpha=al, beta=be, amp=amp, d0=d0, r=r, s=s,
                sc=np.sqrt(V[0, 0]), samp=np.sqrt(J @ V @ J),
                lag1=np.corrcoef(r[:-1], r[1:])[0, 1])


def descent_cycle(d, T, start=CYCLE_START, eta=GD_CYCLE_ETA, steps=400):
    """Gradient descent on the mean squared residual of the cycle, in c, A, d0."""
    c, amp, d0 = start
    rows = []
    for k in range(steps + 1):
        ph = OMEGA * (d - d0)
        r = c - amp * np.cos(ph) - T
        rows.append((k, c, amp, d0, np.sqrt((r ** 2).mean())))
        gc = 2 * r.mean()
        ga = 2 * (r * -np.cos(ph)).mean()
        gd = 2 * (r * -amp * OMEGA * np.sin(ph)).mean()
        c, amp, d0 = c - eta * gc, amp - eta * ga, d0 - eta * gd
    return np.array(rows)


def year_amplitudes(d, T):
    """The cycle fitted to each year alone: amplitude and coldest day."""
    out = []
    for k in range(10):
        sel = (d >= 365.25 * k) & (d < 365.25 * (k + 1))
        f = cycle_fit(d[sel], T[sel])
        out.append((f["amp"], (f["d0"] - 365.25 * k) % 365.25))
    return np.array(out)


def day_of(d):
    return date(2016, 1, 1) + timedelta(days=float(d))


def polynomials(x, y, sigma=SIGMA):
    """Polynomials of degree 0 to 9 through the ten yearly means."""
    rows = []
    for deg in range(10):
        c = np.polyfit(x, y, deg)
        chi2 = (((y - np.polyval(c, x)) / sigma) ** 2).sum()
        rows.append((deg, deg + 1, chi2, len(x) - deg - 1, np.polyval(c, 10.0)))
    return rows


def years_needed(sigma=SIGMA, ns=(10, 15, 20, 30, 40)):
    """sigma of the slope, per decade, for N yearly means one year apart."""
    return [(n, 10 * sigma * np.sqrt(12 / (n * (n * n - 1)))) for n in ns]


def pendulum_data(sigma_t10=SIGMA_T10):
    """x = length (m), t10 (s), T (s), y = T^2 (s^2), sy = sigma(T^2)."""
    d = np.loadtxt(DATA / "pendulum.csv", delimiter=",", skiprows=1)
    x, t10 = d[:, 0] / 100, d[:, 1]
    T = t10 / 10
    return x, t10, T, T ** 2, 2 * T * sigma_t10 / 10


def weighted_line(x, y, sy):
    """Weighted straight-line fit y = a x + b from the closed formulas."""
    w = 1 / sy ** 2
    S, Sx, Sy = w.sum(), (w * x).sum(), (w * y).sum()
    Sxx, Sxy = (w * x * x).sum(), (w * x * y).sum()
    D = S * Sxx - Sx ** 2
    a = (S * Sxy - Sx * Sy) / D
    b = (Sxx * Sy - Sx * Sxy) / D
    pulls = (y - a * x - b) / sy
    return dict(a=a, b=b, sa=np.sqrt(S / D), sb=np.sqrt(Sxx / D), cov=-Sx / D,
                pulls=pulls, chi2=(pulls ** 2).sum(), ndf=len(x) - 2)


def d0_mass():
    return np.loadtxt(DATA / "D0_KPi.csv", delimiter=",", skiprows=1, usecols=0)


def d0_hist(lo=D0_WINDOW[0], hi=D0_WINDOW[1], bins=D0_BINS):
    """Bin centres, counts and sqrt(n) of the mass histogram."""
    n, edges = np.histogram(d0_mass(), bins=bins, range=(lo, hi))
    return 0.5 * (edges[:-1] + edges[1:]), n, np.sqrt(n)


def d0_model(m, A, mu, sigma, c0, c1):
    """A Gaussian on a linear background; the line is centred on 1865."""
    return A * np.exp(-(m - mu) ** 2 / (2 * sigma ** 2)) + c0 + c1 * (m - 1865)


def d0_fit():
    m, n, s = d0_hist()
    popt, pcov = curve_fit(d0_model, m, n, p0=D0_P0, sigma=s, absolute_sigma=True)
    pulls = (n - d0_model(m, *popt)) / s
    return dict(m=m, n=n, s=s, popt=popt, pcov=pcov, err=np.sqrt(np.diag(pcov)),
                pulls=pulls, chi2=(pulls ** 2).sum(), ndf=D0_BINS - 5)


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


def numbers():
    """Print every number quoted in the deck and on the workbook pages."""
    np.set_printoptions(precision=4, suppress=True, linewidth=120)

    print("== 1. One number for four hours ==")
    print("hours", HOURS, "sum", round(sum(HOURS), 3), "mean", round(mean(HOURS), 4))
    for mu in (20, 24, 25, mean(HOURS), 26):
        print(f"S({mu:g}) = {sum_squares(mu):.4f}")
    print("deviations from 25:", [round(v - 25, 1) for v in HOURS],
          "squares:", [round((v - 25) ** 2, 2) for v in HOURS])
    print("sum of |y - mu|:", {mu: round(sum(abs(v - mu) for v in HOURS), 2)
                               for mu in (24, 24.6, 25, 25.275, 25.6, 26)})
    h = 0.001
    print(f"nudge at 25: (S(25.001) - S(25)) / 0.001 = "
          f"{(sum_squares(25 + h) - sum_squares(25)) / h:.4f}; "
          f"formula -2 sum(y - mu) = {-2 * (sum(HOURS) - 4 * 25):.4f}")
    print(f"nudge at 25.275: {(sum_squares(25.275 + h) - sum_squares(25.275)) / h:.4f}")
    dd, hh = 2.3, 0.01
    print(f"square: ((2.3 - 0.01)^2 - 2.3^2) / 0.01 = {((dd - hh) ** 2 - dd ** 2) / hh:.4f}"
          f" = -2 x 2.3 + 0.01")
    print(f"sd of the four hours {np.std(HOURS, ddof=1):.3f}")

    print("\n== 2. The ten yearly means ==")
    x, y, names = yearly_means()
    for k in range(10):
        print(f"{names[k]}  x = {int(x[k])}  y = {y[k]:.6f}  ({y[k]:.3f}, {y[k]:.2f})")
    print(f"mean of the ten {y.mean():.4f}, scatter s = {y.std(ddof=1):.4f} "
          f"-> sigma = {SIGMA}, s / sqrt(10) = {y.std(ddof=1) / np.sqrt(10):.3f}")
    print(f"2017 -> 2023: {y[7] - y[1]:+.3f}   2023 -> 2025: {y[9] - y[7]:+.3f}")

    print("\n== 3. Likelihood ==")
    z = (y[0] - GUESS_A[1]) / SIGMA
    p0 = np.exp(-z * z / 2) / (SIGMA * np.sqrt(2 * np.pi))
    print(f"2016: (7.60 - 7.16) / 0.70 = {z:.3f}, exp(-z^2/2) = {np.exp(-z * z / 2):.3f}, "
          f"sigma sqrt(2 pi) = {SIGMA * np.sqrt(2 * np.pi):.4f}, p = {p0:.3f} per degC")
    ps = np.exp(-((y - GUESS_A[1]) / SIGMA) ** 2 / 2) / (SIGMA * np.sqrt(2 * np.pi))
    print("p of each year:", np.round(ps, 2), f"product L = {np.prod(ps):.3e}")
    lnL = np.log(ps).sum()
    print(f"ln L = {lnL:.3f}; -2 ln L = {-2 * lnL:.3f} = chi2 {chi2_line(0, 7.16, x, y):.3f}"
          f" + 20 ln(sigma sqrt(2 pi)) {20 * np.log(SIGMA * np.sqrt(2 * np.pi)):.3f}")

    print("\n== 4. Two guessed lines (sigma = 0.70) ==")
    for name, (a, b) in (("A", GUESS_A), ("B", GUESS_B)):
        pulls = (y - a * x - b) / SIGMA
        print(f"line {name}: a = {a}, b = {b}: chi2 = {chi2_line(a, b, x, y):.3f}")
        print("   residuals", np.round(y - a * x - b, 2))
        print("   pulls    ", np.round(pulls, 2))
        print("   squares  ", np.round(pulls ** 2, 2))

    print("\n== 5. The best line: five sums ==")
    f = line_fit(x, y)
    print("x  y(3 dec)  x^2  x*y(3 dec)")
    for k in range(10):
        y3 = round(y[k], 3)
        print(f"{int(x[k])}  {y3:.3f}  {int(x[k] ** 2)}  {x[k] * y3:.3f}")
    y3 = np.round(y, 3)
    print(f"sums of the rounded table: Sy = {y3.sum():.3f}, Sxy = {(x * y3).sum():.3f}")
    print(f"N = {f['n']}, Sx = {f['sx']:.0f}, Sy = {f['sy']:.4f}, Sxx = {f['sxx']:.0f}, "
          f"Sxy = {f['sxy']:.4f}, Delta = {f['d']:.0f}")
    print(f"N Sxy = {f['n'] * f['sxy']:.3f}, Sx Sy = {f['sx'] * f['sy']:.3f}, "
          f"difference {f['n'] * f['sxy'] - f['sx'] * f['sy']:.3f}")
    print(f"with the sums as shown: 10 x 317.62 - 45 x 71.60 = {10 * 317.62 - 45 * 71.60:.2f}"
          f" -> a = {(10 * 317.62 - 45 * 71.60) / 825:.5f}")
    print(f"Sxx Sy = {f['sxx'] * f['sy']:.2f}, Sx Sxy = {f['sx'] * f['sxy']:.2f}; "
          f"with the sums as shown: {285 * 71.60:.1f} - {45 * 317.62:.1f} = "
          f"{285 * 71.60 - 45 * 317.62:.1f} -> b = {(285 * 71.60 - 45 * 317.62) / 825:.4f}")
    print(f"a = {f['a']:.6f} degC per year = {10 * f['a']:.4f} per decade; b = {f['b']:.5f}")
    print(f"chi2 min = {f['chi2']:.4f} (ndf 8, chi2/ndf {f['chi2'] / 8:.3f}); "
          f"sum of squares {(f['r'] ** 2).sum():.4f}")
    print(f"centroid: x = {f['sx'] / 10:.1f}, y = {f['sy'] / 10:.4f}; "
          f"line there {f['a'] * 4.5 + f['b']:.4f}")
    print("residuals", np.round(f["r"], 2), "sum", round(f["r"].sum(), 10))
    print("pulls    ", np.round(f["r"] / SIGMA, 2))
    print("polyfit  ", np.polyfit(x, y, 1))
    hh = 1e-4
    ga = -2 * (x * (y - 7.16)).sum() / SIGMA ** 2
    print(f"d chi2 / da at line A: formula {ga:.3f}, nudge 1e-4: "
          f"{(chi2_line(hh, 7.16, x, y) - chi2_line(0, 7.16, x, y)) / hh:.3f}")
    gb = -2 * (y - 7.16).sum() / SIGMA ** 2
    print(f"d chi2 / db at line A: formula {gb:.4f}")

    print("\n== 6. The uncertainty of the slope ==")
    print(f"sigma_a = 0.70 sqrt(10 / 825) = 0.70 x {np.sqrt(10 / 825):.4f} = {f['sa']:.5f} "
          f"per year = {10 * f['sa']:.3f} per decade")
    print(f"sigma_b = {f['sb']:.4f}, cov = {f['cov']:.5f}, rho = {f['rho']:.3f}")
    print(f"slope {10 * f['a']:.2f} +- {10 * f['sa']:.2f} per decade; a / sigma_a = "
          f"{f['a'] / f['sa']:.3f}")
    for s in (-1, 1):
        aa = f["a"] + s * f["sa"]
        print(f"chi2 at a = {aa:.5f} (b re-minimised {(y - aa * x).mean():.4f}): "
              f"{chi2_profile(aa, x, y):.4f}")
    print(f"Sum (x - xbar)^2 = {((x - 4.5) ** 2).sum():.1f}, sqrt = {np.sqrt(82.5):.3f}")
    for n, s in years_needed():
        print(f"N = {n} years: sigma per decade {s:.3f}; 2 sigma {2 * s:.3f}")

    print("\n== 6b. More about the line ==")
    yrs = YEARS.astype(float)
    sx_y, sxx_y = yrs.sum(), (yrs ** 2).sum()
    print(f"x = the year: Sx = {sx_y:.0f}, Sxx = {sxx_y:.0f}, N Sxx = {10 * sxx_y:.0f}, "
          f"Sx^2 = {sx_y ** 2:.0f}, Delta = {10 * sxx_y - sx_y ** 2:.0f}; "
          f"intercept (year 0) = {f['b'] - 2016 * f['a']:.2f}")
    sxs, sys_ = np.std(x, ddof=1), np.std(y, ddof=1)
    r_xy = np.corrcoef(x, y)[0, 1]
    print(f"s_x = {sxs:.4f}, s_y = {sys_:.4f}, r(x, y) = {r_xy:.4f}, r s_y / s_x = "
          f"{r_xy * sys_ / sxs:.5f}")
    print(f"centred: sum (x - 4.5)(y - ybar) = {((x - 4.5) * (y - y.mean())).sum():.4f}, "
          f"/ 82.5 = {((x - 4.5) * (y - y.mean())).sum() / 82.5:.5f}")
    print(f"sigma_b = 0.70 sqrt(285 / 825) = 0.70 x {np.sqrt(285 / 825):.4f} = {f['sb']:.4f}")
    f26 = f["a"] * 10 + f["b"]
    vf = SIGMA ** 2 / 10 + (10 - 4.5) ** 2 * f["sa"] ** 2
    print(f"2026: line {f26:.4f}; sigma^2/N = {SIGMA ** 2 / 10:.4f}, (10 - 4.5)^2 sigma_a^2 = "
          f"{(10 - 4.5) ** 2 * f['sa'] ** 2:.4f}, sigma = {np.sqrt(vf):.4f}; with one year's "
          f"scatter {np.sqrt(vf + SIGMA ** 2):.4f}; range {f26 - np.sqrt(vf + SIGMA ** 2):.2f}"
          f" to {f26 + np.sqrt(vf + SIGMA ** 2):.2f}")
    pulls = f["r"] / SIGMA
    print(f"pulls of the line: {np.round(pulls, 2)}; within 1: {(abs(pulls) < 1).sum()}, "
          f"beyond 2: {(abs(pulls) > 2).sum()}, sd {pulls.std(ddof=2):.3f}")
    shifted = y + np.where(x >= 5, 0.5, 0.0)
    fs = line_fit(x, shifted)
    print(f"0.5 degC added from 2021: slope {10 * fs['a']:+.3f} +- {10 * fs['sa']:.3f} per "
          f"decade, chi2 {fs['chi2']:.2f}; weights of 2021-2025 add to "
          f"{((10 * x[5:] - 45) / 825).sum():.5f}")
    typo = y.copy()
    typo[3] = round(y[3], 2) - 5          # 7.27 typed as 2.27
    ft = line_fit(x, typo)
    print(f"2019 typed as {typo[3]:.2f}: slope {10 * ft['a']:+.2f} per decade, chi2 "
          f"{ft['chi2']:.1f} for 8, pull of 2019 {ft['r'][3] / SIGMA:.2f}")
    july, y2019 = [], []
    for line in read_lines(PATH):
        t = temp_of(line)
        if t == MISSING:
            continue
        if line[5:10] in ("07-22", "07-23", "07-24", "07-25", "07-26"):
            july.append(t)
        if line[:4] == "2019":
            y2019.append(t)
    filled = (sum(y2019) + 120 * mean(july)) / (len(y2019) + 120)
    print(f"22-26 July of the other years: {len(july)} hours, mean {mean(july):.3f}; 2019 "
          f"{mean(y2019):.4f}, with the gap filled {filled:.4f} ({filled - mean(y2019):+.3f})")
    print(f"gap factor 1 - 2 N eta: eta 0.1 -> {1 - 8 * 0.1:.2f}, 0.25 -> {1 - 8 * 0.25:.2f}, "
          f"0.3 -> {1 - 8 * 0.3:.2f}, 0.01 -> {1 - 8 * 0.01:.2f}")

    print("\n== 7. Gradient descent ==")
    start, eta, big = GD_HOURS
    for e in (eta, 0.25, big):
        rows = descent_hours(start, e, 4)
        print(f"eta = {e}: " + "  ".join(f"mu = {m:.4f} (slope {g:.4f})" for m, g in rows))
    print("curvature d2S/dmu2 = 2 N = 8; largest stable step 2 / 8 = 0.25")
    rows = descent_line(x, y)
    for k in (0, 1, 2, 3, 10, 100, 200, 300, 500, 1000):
        print(f"line, step {k:4d}: a = {rows[k, 1]:.5f}  b = {rows[k, 2]:.4f}  S = {rows[k, 3]:.4f}")
    H = 2 * np.array([[f["sxx"], f["sx"]], [f["sx"], f["n"]]])
    ev = np.linalg.eigvalsh(H)
    print(f"Hessian eigenvalues {ev}; largest stable step 2 / {ev.max():.1f} = {2 / ev.max():.5f};"
          f" curvature ratio {ev.max() / ev.min():.0f}")
    for e in (0.004,):
        r2 = descent_line(x, y, eta=e, steps=10)
        print(f"eta = {e}: S after 1, 2, 3, 10 steps", np.round(r2[[1, 2, 3, 10], 3], 1))
    a0, b0 = GD_LINE[0]
    g = np.array([2 * ((a0 * x + b0 - y) * x).sum(), 2 * (a0 * x + b0 - y).sum()])
    print(f"gradient at the start (0, 7): dS/da = {g[0]:.3f}, dS/db = {g[1]:.3f}")
    newton = np.array([a0, b0]) - np.linalg.solve(H, g)
    print("one Newton step from (0, 7):", newton)

    print("\n== 8. The yearly cycle ==")
    d, T = daily_means()
    cf = cycle_fit(d, T)
    print(f"{len(d)} days with 24 hours; mean of the daily means {T.mean():.4f}")
    print(f"c = {cf['c']:.4f}, alpha = {cf['alpha']:.4f}, beta = {cf['beta']:.4f}, "
          f"A = {cf['amp']:.4f}, d0 = {cf['d0']:.3f}")
    warm = cf["d0"] + 365.25 / 2
    print(f"coldest: day {cf['d0']:.2f} = {day_of(cf['d0'])}, {cf['c'] - cf['amp']:.3f} degC; "
          f"warmest: day {warm:.2f} = {day_of(warm)}, {cf['c'] + cf['amp']:.3f} degC")
    print(f"amplitude: the warmest minus the coldest {2 * cf['amp']:.2f}")
    c0, A0, d00 = CYCLE_START
    for dd in (0, 15, 198):
        print(f"start values at day {dd} ({day_of(dd)}): cos = "
              f"{np.cos(OMEGA * (dd - d00)):.4f}, model {cycle(dd, c0, A0, d00):.3f}; "
              f"fit {cycle(dd, cf['c'], cf['amp'], cf['d0']):.3f}")
    for name, pars in (("start", CYCLE_START), ("fit", (cf["c"], cf["amp"], cf["d0"])),
                       ("constant", (T.mean(), 0.0, 0.0))):
        r = T - cycle(d, *pars)
        print(f"{name}: sum of squares {(r ** 2).sum():.1f}, rms {np.sqrt((r ** 2).mean()):.4f}")
    rows = descent_cycle(d, T)
    for k in (0, 1, 2, 10, 50, 100, 200, 300, 400):
        print(f"cycle descent, step {k:3d}: c = {rows[k, 1]:.4f}  A = {rows[k, 2]:.4f}  "
              f"d0 = {rows[k, 3]:.3f}  rms {rows[k, 4]:.4f}")
    print(f"residuals: sd {cf['s']:.3f}, lag-1 correlation {cf['lag1']:.3f}")
    print(f"naive uncertainties (days independent): c +- {cf['sc']:.3f}, A +- {cf['samp']:.3f}")
    ya = year_amplitudes(d, T)
    print("amplitude of each year", np.round(ya[:, 0], 2),
          f"mean {ya[:, 0].mean():.3f}, scatter {ya[:, 0].std(ddof=1):.3f}, "
          f"+- {ya[:, 0].std(ddof=1) / np.sqrt(10):.3f}; "
          f"ratio {ya[:, 0].std(ddof=1) / np.sqrt(10) / cf['samp']:.1f}")
    print("coldest day of each year", np.round(ya[:, 1], 1))
    print(f"constant model: residual sd {T.std(ddof=1):.3f}")
    A2 = np.column_stack([np.ones_like(d), np.cos(OMEGA * d), np.sin(OMEGA * d),
                          np.cos(2 * OMEGA * d), np.sin(2 * OMEGA * d)])
    th2, *_ = np.linalg.lstsq(A2, T, rcond=None)
    print(f"two harmonics (k = 5): residual sd {(T - A2 @ th2).std(ddof=5):.4f}, "
          f"second amplitude {np.hypot(th2[3], th2[4]):.3f}; the cycle alone "
          f"{cf['s']:.4f}")
    A3 = np.column_stack([A2[:, :3], d / 3652.5])
    th3, *_ = np.linalg.lstsq(A3, T, rcond=None)
    r3 = T - A3 @ th3
    V3 = np.linalg.inv(A3.T @ A3) * r3.std(ddof=4) ** 2
    print(f"cycle + trend: {th3[3]:.3f} +- {np.sqrt(V3[3, 3]):.3f} per decade (days "
          f"taken as independent)")

    print("\n== 9. Too few and too many parameters ==")
    for deg, k, chi2, ndf, pred in polynomials(x, y):
        print(f"degree {deg}: k = {k}, chi2 = {chi2:.2f}, ndf = {ndf}, 2026 = {pred:.2f}")
    print(f"line: chi2 {f['chi2']:.2f} for 8, p = {stats.chi2.sf(f['chi2'], 8):.3f}")

    print("\n== 10. For the curious ==")
    fc = line_fit(x - 4.5, y)
    print(f"x centred on 2020.5: a = {fc['a']:.5f} +- {fc['sa']:.4f}, b = {fc['b']:.4f} "
          f"+- {fc['sb']:.4f}, cov = {fc['cov']:.2e}")
    print(f"weights c_i = (N x_i - Sx) / Delta:", np.round((10 * x - 45) / 825, 4),
          f"sum c_i^2 = {(((10 * x - 45) / 825) ** 2).sum():.5f} = N / Delta "
          f"{10 / 825:.5f}")
    M = np.array([[f["sxx"], f["sx"]], [f["sx"], f["n"]]])
    print("normal equations: matrix", M.tolist(), "right side",
          [round(f["sxy"], 3), round(f["sy"], 3)], "solution", np.linalg.solve(M, [f["sxy"], f["sy"]]))
    print("inverse times sigma^2:", np.linalg.inv(M) * SIGMA ** 2)
    xs, t10, Tp, yp, syp = pendulum_data()
    pf = weighted_line(xs, yp, syp)
    g = 4 * np.pi ** 2 / pf["a"]
    print(f"pendulum: a = {pf['a']:.4f} +- {pf['sa']:.4f}, b = {pf['b']:.4f} +- {pf['sb']:.4f},"
          f" chi2 = {pf['chi2']:.2f}/{pf['ndf']}; g = {g:.3f} +- {g * pf['sa'] / pf['a']:.3f}")
    dfit = d0_fit()
    p, e = dfit["popt"], dfit["err"]
    print(f"D0: {dfit['n'].sum()} rows in 45 bins; mu = {p[1]:.2f} +- {e[1]:.2f}, "
          f"sigma = {abs(p[2]):.2f} +- {e[2]:.2f}, A = {p[0]:.0f}, c0 = {p[3]:.0f}, "
          f"c1 = {p[4]:.3f}, chi2 = {dfit['chi2']:.1f}/{dfit['ndf']}, "
          f"p = {stats.chi2.sf(dfit['chi2'], dfit['ndf']):.3f}")
    M = d0_mass()
    print(f"D0 file: {len(M)} rows, {M.min():.1f} to {M.max():.1f}; window 1820-1910: "
          f"{dfit['n'].sum()} rows; smallest bin {dfit['n'].min()}, largest {dfit['n'].max()}")
    for key, (_, pp, c2, ndf, e) in _d0_alt_models().items():
        mu = f"{pp[1]:.2f} +- {e[1]:.2f}" if len(pp) > 2 else "-"
        print(f"D0 model {key:14s}: k = {len(pp)}, chi2 = {c2:.1f}, ndf = {ndf}, mu = {mu}")


# =============================================================================
# Figures
# =============================================================================

C0, C1, C2, C3 = style.CYCLE[0], style.CYCLE[1], style.CYCLE[2], style.CYCLE[3]
BOX = dict(boxstyle="round,pad=0.2", facecolor=style.BG, edgecolor="none", alpha=0.75)
TEMP = "temperature (°C)"
YEAR_MEAN = "yearly mean (°C)"
YEARS = np.arange(2016, 2026)


def _minus(text):
    return text.replace("-", "−")


def _year_axis(ax, extra=0):
    ax.set_xticks(range(0, 10 + extra, 1))
    ax.set_xticklabels([str(2016 + k) if k % 2 == 0 else "" for k in range(10 + extra)])
    ax.set_xlabel("year")


def _year_means_fig():
    """The opening: ten points, the mean of all hours, two picked differences."""
    x, y, _ = yearly_means()
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.axhline(y.mean(), color=style.DIM, lw=1.2, ls="--")
    ax.text(2025.85, y.mean() + 0.06, "7.16", color=style.DIM, ha="right", fontsize=11)
    ax.plot(YEARS, y, "o", color=C0, ms=8, zorder=5)
    arrow = dict(arrowstyle="->", lw=1.6, shrinkA=6, shrinkB=6)
    ax.annotate("", xy=(2023, y[7]), xytext=(2017, y[1]),
                arrowprops=dict(arrow, color=C2))
    ax.text(2019.6, 7.75, "+1.80 °C", color=C2, fontsize=13, ha="center", rotation=12)
    ax.annotate("", xy=(2025, y[9]), xytext=(2023, y[7]),
                arrowprops=dict(arrow, color=style.BAD))
    ax.text(2024.35, 7.55, _minus("-2.33 °C"), color=style.BAD, fontsize=13, ha="left")
    ax.set(xlabel="year", ylabel=YEAR_MEAN, ylim=(5.5, 8.8), xlim=(2015.4, 2025.9))
    ax.set_xticks(YEARS[::1])
    ax.set_xticklabels([str(v) if v % 2 == 0 else "" for v in YEARS])
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_year_means")


def _three_models():
    """A model with 1, 2 and 3 parameters."""
    x, y, _ = yearly_means()
    f = line_fit(x, y)
    d, T = daily_means()
    cf = cycle_fit(d, T)
    fig, axes = plt.subplots(1, 3, figsize=(9.4, 3.1),
                             gridspec_kw={"width_ratios": [1, 1, 1.25]})
    ax = axes[0]
    ax.plot(x, y, "o", color=style.FG, ms=5, zorder=5)
    ax.axhline(y.mean(), color=C0, lw=2.2)
    ax.set_title(r"$T = \mu$: one parameter", fontsize=12.5, fontweight="normal")
    ax.set(ylabel=YEAR_MEAN, ylim=(5.5, 8.8))
    _year_axis(ax)
    ax = axes[1]
    ax.plot(x, y, "o", color=style.FG, ms=5, zorder=5)
    ax.plot([-0.5, 9.5], [f["b"] - 0.5 * f["a"], f["b"] + 9.5 * f["a"]], color=C1, lw=2.2)
    ax.set_title(r"$T = a\,x + b$: two", fontsize=12.5, fontweight="normal")
    ax.set(ylim=(5.5, 8.8))
    _year_axis(ax)
    ax = axes[2]
    sel = d < 3 * 365.25
    dates = [day_of(v) for v in d[sel]]
    ax.plot(dates, T[sel], ".", color=style.FG, ms=2.2, alpha=0.8)
    dd = np.linspace(0, 3 * 365.25, 600)
    ax.plot([day_of(v) for v in dd], cycle(dd, cf["c"], cf["amp"], cf["d0"]), color=C2, lw=2.2)
    ax.set_title(r"$T = c - A\cos\frac{2\pi(d - d_0)}{365.25}$: three", fontsize=12.5,
                 fontweight="normal")
    ax.set(ylabel="daily mean (°C)", xlabel="day, 2016 to 2018")
    ax.set_xticks([date(2016, 1, 1), date(2017, 1, 1), date(2018, 1, 1), date(2019, 1, 1)])
    ax.set_xticklabels(["2016", "2017", "2018", "2019"])
    for a in axes:
        a.xaxis.grid(False)
    style.save(fig, "viz_fitting_three_models")


def _parts_fig():
    """The three parts of a fit: a model with open parameters, data with their
    scatter, the misses of one line."""
    x, y, _ = yearly_means()
    xs = np.array([-0.5, 9.5])
    fig, axes = plt.subplots(1, 3, figsize=(9.4, 3.5), sharey=True)
    ax = axes[0]
    for a, b in ((0.15, 6.4), (0.0, 7.16), (-0.12, 7.7), (0.07, 6.6), (-0.05, 7.6)):
        ax.plot(xs, a * xs + b, color=C0, lw=1.3, alpha=0.75)
    ax.set_title(r"a model: $a\,x + b$, $a$ and $b$ open", fontsize=12, fontweight="normal",
                 loc="left", color=C0)
    ax = axes[1]
    ax.errorbar(x, y, yerr=SIGMA, fmt="o", color=style.FG, ms=5, capsize=3, lw=1)
    ax.set_title(r"data: ten yearly means, $\pm\sigma$ = 0.70", fontsize=12,
                 fontweight="normal", loc="left", color=style.FG)
    ax = axes[2]
    a, b = GUESS_A
    ax.plot(xs, a * xs + b, color=C1, lw=2)
    for k in range(10):
        ax.plot([x[k], x[k]], [y[k], a * x[k] + b], color=C1, lw=1.4, alpha=0.8)
    ax.plot(x, y, "o", color=style.FG, ms=5, zorder=5)
    ax.set_title("the misses of one line", fontsize=12, fontweight="normal", loc="left",
                 color=C1)
    axes[0].set_ylabel(YEAR_MEAN)
    for ax in axes:
        ax.set(ylim=(4.9, 9.2))
        _year_axis(ax)
        ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_parts")


def _slope_gauss_fig():
    """The slope's Gaussian: 68 % within one sigma, 95 % within two, zero inside both."""
    x, y, _ = yearly_means()
    f = line_fit(x, y)
    a, sa = 10 * f["a"], 10 * f["sa"]
    t = np.linspace(a - 3.6 * sa, a + 3.6 * sa, 500)
    pdf = np.exp(-(t - a) ** 2 / (2 * sa ** 2)) / (sa * np.sqrt(2 * np.pi))
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    two = np.abs(t - a) <= 2 * sa
    one = np.abs(t - a) <= sa
    ax.fill_between(t[two], pdf[two], color=C0, alpha=0.18, lw=0, label=r"95 %: $\pm 2\sigma$")
    ax.fill_between(t[one], pdf[one], color=C0, alpha=0.40, lw=0, label=r"68 %: $\pm 1\sigma$")
    ax.plot(t, pdf, color=C0, lw=2.2)
    ax.axvline(0, color=style.FG, lw=1.2, ls="--")
    ax.text(0.06, pdf.max() * 1.02, "no trend", color=style.FG, fontsize=11.5)
    ax.text(a, pdf.max() * 0.45, _minus("-0.56"), color=style.FG, fontsize=13, ha="center")
    ax.set(xlabel="slope (°C per decade)", ylabel="likelihood of the slope (per °C/decade)",
           ylim=(0, pdf.max() * 1.15), xlim=(t[0], t[-1]))
    ax.legend(loc="upper left", fontsize=10.5)
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_slope_gauss")


def _amplitudes_fig():
    """The amplitude of each year alone against the fit of all days."""
    d, T = daily_means()
    cf = cycle_fit(d, T)
    amps = year_amplitudes(d, T)[:, 0]
    m, sem = amps.mean(), amps.std(ddof=1) / np.sqrt(10)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.axhspan(m - sem, m + sem, color=C2, alpha=0.25, lw=0)
    ax.axhline(m, color=C2, lw=1.6, label=f"ten years: {m:.2f} ± {sem:.2f}")
    ax.axhspan(cf["amp"] - cf["samp"], cf["amp"] + cf["samp"], color=C1, alpha=0.6, lw=0,
               label=f"days as independent: ± {cf['samp']:.2f}")
    ax.plot(YEARS, amps, "o", color=style.FG, ms=7, zorder=5, label="one year alone")
    ax.set(xlabel="year", ylabel="amplitude A (°C)", ylim=(9.0, 13.0), xlim=(2015.4, 2025.6))
    ax.set_xticks(YEARS)
    ax.set_xticklabels([str(v) if v % 2 == 0 else "" for v in YEARS])
    ax.xaxis.grid(False)
    ax.legend(loc="lower right", fontsize=10.5)
    style.save(fig, "viz_fitting_amplitudes")


def _sum_squares_fig():
    """S(mu) of the four hours: a parabola, lowest at the mean."""
    mus = np.linspace(23.4, 27.2, 300)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.plot(mus, [sum_squares(m) for m in mus], color=C0, lw=2.2)
    places = {24: (24.12, 13.4, "left"), 25: (25.0, 9.0, "center"),
              26: (26.1, 8.6, "left"), 25.275: (25.275, 5.6, "center")}
    for m, col in ((24, style.FG), (25, style.FG), (26, style.FG), (25.275, C1)):
        s = sum_squares(m)
        ax.plot(m, s, "o", color=col, ms=8, zorder=5)
        label = f"{s:.2f}" if m != 25.275 else f"{s:.2f} at the mean, 25.275"
        tx, ty, ha = places[m]
        ax.text(tx, ty, label, color=col, fontsize=12, ha=ha)
    ax.axvline(25.275, color=C1, lw=1.0, ls=":", ymax=0.25)
    ax.set(xlabel=r"$\mu$ (°C)", ylabel=r"$S(\mu) = \sum\,(y_i - \mu)^2$  (°C²)",
           ylim=(0, 21), xlim=(23.4, 27.2))
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_sum_squares")


def _tangent_fig():
    """The slope of S(mu): -2.2 at 25, zero at the mean."""
    mus = np.linspace(24.0, 26.6, 300)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.plot(mus, [sum_squares(m) for m in mus], color=C0, lw=2.2)
    for m, slope, col, txt, pos in ((25.0, -2.2, C1, _minus("slope -2.2 at 25"), (24.08, 7.0)),
                                    (25.275, 0.0, C2, "slope 0 at 25.275", (25.5, 7.05))):
        s = sum_squares(m)
        t = np.linspace(m - 0.75, m + 0.75, 10)
        ax.plot(t, s + slope * (t - m), color=col, lw=2.0)
        ax.plot(m, s, "o", color=col, ms=8, zorder=5)
        ax.text(*pos, txt, color=col, fontsize=13)
    ax.set(xlabel=r"$\mu$ (°C)", ylabel=r"$S(\mu)$  (°C²)", ylim=(5.6, 12.0), xlim=(24.0, 26.6))
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_tangent")


def _gauss_fig():
    """The ten yearly means around a flat line, each with its Gaussian of 0.70."""
    x, y, _ = yearly_means()
    mu = GUESS_A[1]
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    ax.axhline(mu, color=C0, lw=2, label="model: 7.16 every year")
    t = np.linspace(mu - 2.7 * SIGMA, mu + 2.7 * SIGMA, 200)
    pdf = np.exp(-(t - mu) ** 2 / (2 * SIGMA ** 2))
    for k in range(10):
        ax.fill_betweenx(t, x[k], x[k] + 0.42 * pdf, color=C1, alpha=0.22, lw=0)
        ax.plot(x[k] + 0.42 * pdf, t, color=C1, lw=1.2)
        p = np.exp(-(y[k] - mu) ** 2 / (2 * SIGMA ** 2))
        ax.plot([x[k], x[k] + 0.42 * p], [y[k], y[k]], color=C1, lw=1.4, ls=":")
    ax.plot(x, y, "o", color=style.FG, ms=6, zorder=6, label="measured yearly mean")
    ax.plot([], [], color=C1, lw=1.2, label=r"Gaussian, $\sigma$ = 0.70 °C")
    ax.set(ylabel=YEAR_MEAN, ylim=(5.0, 10.1), xlim=(-0.4, 9.9))
    ax.set_yticks([5, 6, 7, 8, 9])
    _year_axis(ax)
    ax.xaxis.grid(False)
    ax.legend(loc="upper left", ncol=3, fontsize=10.5)
    style.save(fig, "viz_fitting_gauss")


def _guesses_fig():
    """Two guessed lines with their residuals and chi2."""
    x, y, _ = yearly_means()
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3), sharey=True)
    for ax, (name, (a, b), col) in zip(axes, (("A", GUESS_A, C0), ("B", GUESS_B, C1))):
        xs = np.array([-0.5, 9.5])
        ax.plot(xs, a * xs + b, color=col, lw=2.2)
        for k in range(10):
            ax.plot([x[k], x[k]], [y[k], a * x[k] + b], color=style.DIM, lw=1.2)
        ax.plot(x, y, "o", color=style.FG, ms=6, zorder=5)
        title = (f"A: flat at 7.16,  $\\chi^2$ = {chi2_line(a, b, x, y):.2f}" if name == "A" else
                 f"B: +0.1 °C a year from 6.7,  $\\chi^2$ = {chi2_line(a, b, x, y):.2f}")
        ax.set_title(title, fontsize=12.5, fontweight="normal", color=col, loc="left")
        ax.set(ylim=(5.5, 8.8))
        _year_axis(ax)
        ax.xaxis.grid(False)
    axes[0].set_ylabel(YEAR_MEAN)
    style.save(fig, "viz_fitting_guesses")


def _best_line_fig():
    """The best line, its residuals drawn in."""
    x, y, _ = yearly_means()
    f = line_fit(x, y)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    xs = np.array([-0.5, 9.5])
    for (a, b) in (GUESS_A, GUESS_B):
        ax.plot(xs, a * xs + b, color=style.DIM, lw=1.0, ls="--")
    ax.plot(xs, f["a"] * xs + f["b"], color=C2, lw=2.4)
    for k in range(10):
        ax.plot([x[k], x[k]], [y[k], f["a"] * x[k] + f["b"]], color=style.DIM, lw=1.2)
    ax.plot(x, y, "o", color=style.FG, ms=7, zorder=5)
    ax.plot(4.5, y.mean(), "+", color=C2, ms=14, mew=2, zorder=6)
    ax.text(4.65, y.mean() - 0.42, "(4.5, 7.16)", color=C2, fontsize=11)
    ax.text(0.03, 0.95, _minus("slope -0.056 °C a year") + f"\n$\\chi^2$ = {f['chi2']:.2f}",
            transform=ax.transAxes, va="top", color=C2, fontsize=12.5, linespacing=1.5)
    ax.set(ylabel=YEAR_MEAN, ylim=(5.5, 8.8), xlim=(-0.5, 9.5))
    _year_axis(ax)
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_best_line")


def _chi2_slope_fig():
    """chi2 against the slope, b re-minimised: a parabola, +1 at one sigma."""
    x, y, _ = yearly_means()
    f = line_fit(x, y)
    a, sa = 10 * f["a"], 10 * f["sa"]          # per decade
    aa = np.linspace(a - 2.6 * sa, a + 2.6 * sa, 300)
    prof = [chi2_profile(v / 10, x, y) for v in aa]
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.plot(aa, prof, color=C0, lw=2.4)
    ax.axhline(f["chi2"], color=style.DIM, lw=0.9)
    ax.axhline(f["chi2"] + 1, color=C1, lw=1.3)
    for v in (a - sa, a + sa):
        ax.plot([v, v], [6.0, f["chi2"] + 1], color=C1, lw=1.3, ls=":")
    ax.annotate("", xy=(a + sa, 6.45), xytext=(a - sa, 6.45),
                arrowprops=dict(arrowstyle="<->", color=C1, lw=1.4))
    ax.text(a, 6.65, _minus(f"-0.56 ± 0.77"), color=C1, ha="center", fontsize=13)
    ax.text(a - 2.5 * sa, f["chi2"] + 1.12, r"$\chi^2_{\min} + 1$", color=C1, fontsize=12)
    ax.text(a + 2.5 * sa, f["chi2"] - 0.48, rf"$\chi^2_{{\min}}$ = {f['chi2']:.2f}", color=style.DIM,
            fontsize=11.5, ha="right")
    ax.axvline(0, color=style.FG, lw=1.0, ls="--", alpha=0.6)
    ax.text(0.04, 13.6, "no trend", color=style.FG, fontsize=11, alpha=0.8)
    ax.set(xlabel="slope (°C per decade)", ylabel=r"$\chi^2$", ylim=(6.0, 15.0),
           xlim=(aa[0], aa[-1]))
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_chi2_slope")


def _band_fig():
    """Lines whose chi2 lies within 1 of the minimum: rising and falling."""
    x, y, _ = yearly_means()
    f = line_fit(x, y)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    xs = np.array([-0.5, 9.5])
    for s in np.linspace(-1, 1, 9):
        a = f["a"] + s * f["sa"]
        b = (y - a * x).mean()
        ax.plot(xs, a * xs + b, color=C1, lw=1.0, alpha=0.55)
    for s, ls in ((-1, "--"), (1, "--")):
        a = f["a"] + s * f["sa"]
        b = (y - a * x).mean()
        ax.plot(xs, a * xs + b, color=C1, lw=1.8, ls=ls)
    ax.plot(xs, f["a"] * xs + f["b"], color=C2, lw=2.4)
    ax.plot(x, y, "o", color=style.FG, ms=7, zorder=5)
    up, down = f["a"] + f["sa"], f["a"] - f["sa"]
    ax.text(9.4, (y - up * x).mean() + up * 9.4 + 0.12, f"+{10 * up:.1f} °C per decade",
            color=C1, ha="right", fontsize=12)
    ax.text(9.4, (y - down * x).mean() + down * 9.4 - 0.32,
            _minus(f"{10 * down:.1f} °C per decade"), color=C1, ha="right", fontsize=12)
    ax.set(ylabel=YEAR_MEAN, ylim=(5.5, 8.8), xlim=(-0.5, 9.5))
    _year_axis(ax)
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_band")


def _years_needed_fig():
    """sigma of the slope per decade against the number of years."""
    ns = np.arange(5, 61)
    s = 10 * SIGMA * np.sqrt(12 / (ns * (ns ** 2 - 1)))
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.plot(ns, s, color=C0, lw=2.4)
    ax.axhline(0.28, color=C1, lw=1.2, ls="--")
    ax.text(59, 0.31, r"0.28: a slope of 0.56 at 2$\sigma$", color=C1, ha="right", fontsize=11)
    for n in (10, 20, 40):
        v = 10 * SIGMA * np.sqrt(12 / (n * (n * n - 1)))
        ax.plot(n, v, "o", color=style.FG, ms=7, zorder=5)
        ax.text(n + 1.2, v + 0.05, f"{n} years: ± {v:.2f}", color=style.FG, fontsize=11.5)
    ax.set(xlabel="years of yearly means", ylabel=r"$\sigma$ of the slope (°C per decade)",
           ylim=(0, 1.6), xlim=(5, 60))
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_years_needed")


def _descent_hours_fig():
    """Steps on S(mu): eta = 0.1 settles, eta = 0.3 swings out."""
    start, eta, big = GD_HOURS
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3))
    cases = ((axes[0], eta, C2, 4, (18.6, 27.6), (0, 135)),
             (axes[1], big, style.BAD, 3, (13.0, 41.0), (0, 900)))
    for ax, e, col, n, xlim, ylim in cases:
        mus = np.linspace(*xlim, 400)
        ax.plot(mus, [sum_squares(m) for m in mus], color=C0, lw=1.8)
        rows = descent_hours(start, e, n)
        pts = [(m, sum_squares(m)) for m, _ in rows]
        for (m1, s1), (m2, s2) in zip(pts[:-1], pts[1:]):
            ax.annotate("", xy=(m2, s2), xytext=(m1, s1),
                        arrowprops=dict(arrowstyle="->", color=col, lw=1.5,
                                        shrinkA=4, shrinkB=4))
        for m, s in pts:
            ax.plot(m, s, "o", color=col, ms=6, zorder=5)
        path = "  →  ".join(["20"] + [f"{m:.2f}" for m, _ in rows[1:4]])
        ax.set_title(rf"$\eta$ = {e}:  {path}", fontsize=12, fontweight="normal",
                     color=col, loc="left")
        ax.set(xlabel=r"$\mu$ (°C)", xlim=xlim, ylim=ylim)
        ax.xaxis.grid(False)
    axes[0].set_ylabel(r"$S(\mu)$  (°C²)")
    style.save(fig, "viz_fitting_descent_hours")


def _descent_line_fig():
    """The descent on S(a, b) of the ten years: contours, the path, S per step."""
    x, y, _ = yearly_means()
    f = line_fit(x, y)
    rows = descent_line(x, y, steps=1000)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.3),
                                   gridspec_kw={"width_ratios": [1.25, 1]})
    aa, bb = np.meshgrid(np.linspace(-0.12, 0.05, 240), np.linspace(6.85, 7.75, 240))
    S = ((y[None, None, :] - aa[..., None] * x - bb[..., None]) ** 2).sum(axis=2)
    smin = (f["r"] ** 2).sum()
    ax1.contour(10 * aa, bb, S, levels=smin + np.array([0.05, 0.2, 0.5, 1, 2, 4]),
                colors=style.DIM, linewidths=0.8)
    ax1.plot(10 * rows[:, 1], rows[:, 2], "-", color=C1, lw=1.4)
    ax1.plot(10 * rows[:4, 1], rows[:4, 2], "o", color=C1, ms=4)
    ax1.plot(10 * rows[0, 1], rows[0, 2], "o", color=C1, ms=8, zorder=5)
    ax1.text(10 * rows[0, 1] - 0.05, rows[0, 2] - 0.06, "start (0, 7)", color=C1, fontsize=11,
             ha="right", va="top")
    ax1.plot(10 * f["a"], f["b"], "*", color=C2, ms=15, zorder=6)
    ax1.text(10 * f["a"] + 0.06, f["b"] + 0.04, _minus("(-0.56, 7.41)"), color=C2, fontsize=11)
    ax1.set(xlabel="slope a (°C per decade)", ylabel="intercept b (°C)",
            xlim=(-1.2, 0.5), ylim=(6.85, 7.75))
    ax1.grid(False)
    k = rows[:, 0]
    ax2.semilogy(k, rows[:, 3] - smin, color=C1, lw=2)
    ax2.set(xlabel="step", ylabel="S − S at the minimum (°C²)", xlim=(0, 600),
            ylim=(1e-6, 3))
    style.save(fig, "viz_fitting_descent_line")


def _daily_fig():
    """The 3648 daily means, ten waves."""
    d, T = daily_means()
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    ax.plot([day_of(v) for v in d], T, ".", color=C0, ms=2.4, alpha=0.9)
    ax.set(ylabel="daily mean (°C)", ylim=(-16, 30))
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_daily")


def _cycle_parts_fig():
    """The ten years folded on one year, the fitted curve and its three parameters."""
    d, T = daily_means()
    cf = cycle_fit(d, T)
    doy = d % 365.25
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.plot(doy, T, ".", color=style.DIM, ms=1.8, alpha=0.55)
    t = np.linspace(0, 365.25, 400)
    ax.plot(t, cycle(t, cf["c"], cf["amp"], cf["d0"]), color=C2, lw=2.6)
    ax.axhline(cf["c"], color=C0, lw=1.4, ls="--")
    ax.text(362, cf["c"] + 0.7, f"c = {cf['c']:.2f}", color=C0, ha="right", fontsize=12.5,
            bbox=BOX)
    warm = cf["d0"] + 365.25 / 2
    ax.annotate("", xy=(warm, cf["c"] + cf["amp"]), xytext=(warm, cf["c"]),
                arrowprops=dict(arrowstyle="<->", color=C1, lw=1.6, shrinkA=0, shrinkB=0))
    ax.text(warm + 6, cf["c"] + cf["amp"] / 2, f"A = {cf['amp']:.2f}", color=C1, fontsize=12.5,
            va="center", bbox=BOX)
    ax.axvline(cf["d0"], color=C3, lw=1.4, ls=":")
    ax.text(cf["d0"] + 6, 25.5, f"d₀ = {cf['d0']:.1f}\n16 January", color=C3, fontsize=12,
            va="top", linespacing=1.4, bbox=BOX)
    ax.set(xlabel="day of the year", ylabel="daily mean (°C)", xlim=(0, 365.25), ylim=(-16, 30))
    ax.set_xticks([0, 91, 182, 274, 365])
    ax.set_xticklabels(["1 Jan", "1 Apr", "1 Jul", "1 Oct", "31 Dec"])
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_cycle_parts")


def _cycle_fit_fig():
    """The daily means with the fitted cycle over ten years."""
    d, T = daily_means()
    cf = cycle_fit(d, T)
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    ax.plot([day_of(v) for v in d], T, ".", color=style.DIM, ms=2.2, alpha=0.7)
    dd = np.linspace(0, 3653, 3000)
    ax.plot([day_of(v) for v in dd], cycle(dd, cf["c"], cf["amp"], cf["d0"]), color=C2, lw=2.0)
    ax.set(ylabel="daily mean (°C)", ylim=(-16, 30))
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_cycle_fit")


def _line_resid_fig():
    """The ten residuals of the best line, with the band of one sigma."""
    x, y, _ = yearly_means()
    f = line_fit(x, y)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.axhspan(-SIGMA, SIGMA, color=style.DIM, alpha=0.15, lw=0)
    ax.axhline(0, color=C2, lw=2)
    ax.vlines(x, 0, f["r"], color=style.DIM, lw=1.2)
    ax.plot(x, f["r"], "o", color=style.FG, ms=7, zorder=5)
    for k in (1, 7, 9):
        ax.text(x[k] + 0.18, f["r"][k], _minus(f"{f['r'][k]:+.2f}"), color=style.FG,
                fontsize=11.5, va="center")
    ax.text(9.4, SIGMA + 0.06, r"$\pm\sigma$ = ±0.70", color=style.DIM, ha="right", fontsize=11)
    ax.set(ylabel="residual (°C)", ylim=(-1.6, 1.6), xlim=(-0.5, 9.7))
    _year_axis(ax)
    ax.xaxis.grid(False)
    style.save(fig, "viz_fitting_line_resid")


def _cycle_resid_fig():
    """The residuals of the cycle: runs of warm and cold weeks; day against next day."""
    d, T = daily_means()
    cf = cycle_fit(d, T)
    r = cf["r"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.3),
                                   gridspec_kw={"width_ratios": [2.1, 1]})
    sel = (d >= 365.25 * 8) & (d < 365.25 * 9)
    ax1.axhline(0, color=C2, lw=1.6)
    ax1.plot([day_of(v) for v in d[sel]], r[sel], "-", color=C0, lw=1.0)
    ax1.plot([day_of(v) for v in d[sel]], r[sel], ".", color=C0, ms=3)
    ax1.set(ylabel="residual (°C)", ylim=(-12, 12), xlabel="day of 2024")
    ax1.set_xticks([date(2024, m, 1) for m in (1, 3, 5, 7, 9, 11)])
    ax1.set_xticklabels(["Jan", "Mar", "May", "Jul", "Sep", "Nov"])
    ax1.xaxis.grid(False)
    ax2.plot(r[:-1], r[1:], ".", color=C1, ms=1.6, alpha=0.4)
    ax2.set(xlabel="residual of a day (°C)", ylabel="of the next day (°C)",
            xlim=(-14, 14), ylim=(-14, 14))
    ax2.set_aspect("equal")
    ax2.text(-13, 11.5, f"r = {cf['lag1']:.3f}", color=C1, fontsize=12.5)
    style.save(fig, "viz_fitting_cycle_resid")


def _too_few_fig():
    """Residuals of a constant and of the cycle, folded on one year."""
    d, T = daily_means()
    cf = cycle_fit(d, T)
    doy = d % 365.25
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3), sharey=True)
    for ax, r, title, col in ((axes[0], T - T.mean(), "a constant, k = 1", style.BAD),
                              (axes[1], cf["r"], "the cycle, k = 3", C2)):
        ax.axhline(0, color=style.FG, lw=1.0)
        ax.plot(doy, r, ".", color=col, ms=1.8, alpha=0.5)
        ax.set_title(f"{title}:  sd {r.std(ddof=1):.2f} °C", fontsize=12.5,
                     fontweight="normal", color=col, loc="left")
        ax.set(xlabel="day of the year", xlim=(0, 365.25), ylim=(-25, 22))
        ax.set_xticks([0, 91, 182, 274, 365])
        ax.set_xticklabels(["1 Jan", "1 Apr", "1 Jul", "1 Oct", "31 Dec"])
        ax.xaxis.grid(False)
    axes[0].set_ylabel("residual (°C)")
    style.save(fig, "viz_fitting_too_few")


def _too_many_fig():
    """A line and a polynomial of degree 9 through the ten yearly means, to 2026."""
    x, y, _ = yearly_means()
    xs = np.linspace(-0.3, 10.0, 600)
    c9 = np.polyfit(x, y, 9)
    f = line_fit(x, y)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.axvspan(9.5, 10.6, color=style.DIM, alpha=0.12, lw=0)
    ax.plot(xs, f["a"] * xs + f["b"], color=C2, lw=2.2, label="degree 1: 2 parameters")
    ax.plot(xs, np.polyval(c9, xs), color=style.BAD, lw=1.8, label="degree 9: 10 parameters")
    ax.plot(x, y, "o", color=style.FG, ms=7, zorder=5)
    ax.plot(10, f["a"] * 10 + f["b"], "o", color=C2, ms=7, zorder=5)
    ax.text(9.85, 6.55, "2026", color=style.FG, fontsize=11, ha="right")
    ax.annotate(f"degree 9 in 2026: {np.polyval(c9, 10):.0f} °C", xy=(9.75, 11.9),
                xytext=(4.6, 10.9), color=style.BAD, fontsize=12, ha="center",
                arrowprops=dict(arrowstyle="->", color=style.BAD, lw=1.4))
    ax.set(ylabel=YEAR_MEAN, ylim=(3.5, 12.0), xlim=(-0.4, 10.6))
    ax.set_xticks(range(0, 11))
    ax.set_xticklabels([str(2016 + k) if k % 2 == 0 else "" for k in range(11)])
    ax.set_xlabel("year")
    ax.xaxis.grid(False)
    ax.legend(loc="lower left", fontsize=10.5)
    style.save(fig, "viz_fitting_too_many")


def _ellipse(center, cov2, dchi2, n=400):
    """Points of the contour chi2(theta) = chi2_min + dchi2 for a 2x2 cov."""
    L = np.linalg.cholesky(cov2)
    t = np.linspace(0, 2 * np.pi, n)
    return center[:, None] + np.sqrt(dchi2) * (L @ np.vstack([np.cos(t), np.sin(t)]))


def _ellipse_fig():
    """The Delta chi2 = 1 contour of (a, b): x from 2016 (tilted), x centred (upright)."""
    x, y, _ = yearly_means()
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3))
    for ax, shift, title in ((axes[0], 0.0, "x = years since 2016"),
                             (axes[1], 4.5, "x = years since mid-2020")):
        f = line_fit(x - shift, y)
        c = np.array([10 * f["a"], f["b"]])
        cov = np.array([[100 * f["sa"] ** 2, 10 * f["cov"]], [10 * f["cov"], f["sb"] ** 2]])
        e = _ellipse(c, cov, 1.0)
        ax.fill(e[0], e[1], color=C0, alpha=0.25, lw=0)
        ax.plot(e[0], e[1], color=C0, lw=2)
        ax.plot(*c, "o", color=style.FG, ms=6, zorder=5)
        ax.set_title(f"{title}:  $\\rho$ = {np.round(f['rho'], 2) + 0.0:.2f}".replace("-", "−"), fontsize=12,
                     fontweight="normal", loc="left")
        ax.set(xlabel="slope a (°C per decade)", xlim=(-1.6, 0.5))
        ax.set_ylim(c[1] - 0.75, c[1] + 0.75)
    axes[0].set_ylabel("intercept b (°C)")
    style.save(fig, "viz_fitting_ellipse")


def _chi2_dist():
    """The chi2 distribution for 8 and for 40 degrees of freedom, with the observed values."""
    x, y, _ = yearly_means()
    f = line_fit(x, y)
    d = d0_fit()
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3))
    cases = [(axes[0], 8, f["chi2"], "The line through ten years", C0, 26, 2),
             (axes[1], 40, d["chi2"], r"The $D^0$ peak, Gaussian on a line", C1, 85, 1)]
    for ax, ndf, obs, title, col, xmax, digits in cases:
        t = np.linspace(0.01, xmax, 500)
        pdf = stats.chi2.pdf(t, ndf)
        ax.plot(t, pdf, color=style.FG, lw=1.8)
        tail = t >= obs
        ax.fill_between(t[tail], pdf[tail], color=col, alpha=0.35, lw=0)
        ax.axvline(obs, color=col, lw=2)
        ax.text(0.97, 0.9, rf"$\chi^2$ = {obs:.{digits}f} for {ndf}" "\n"
                rf"$p$ = {stats.chi2.sf(obs, ndf):.2f}",
                transform=ax.transAxes, ha="right", va="top", color=col, fontsize=11.5,
                linespacing=1.5)
        ax.set(xlabel=r"$\chi^2$", xlim=(0, xmax), ylim=(0, pdf.max() * 1.25))
        ax.set_title(title, fontsize=12, fontweight="normal", loc="left")
    axes[0].set_ylabel("probability density")
    style.save(fig, "viz_fitting_chi2_dist")


ELL = r"length $\ell$ (m)"


def _pendulum_fit():
    x, t10, T, y, sy = pendulum_data()
    f = weighted_line(x, y, sy)
    xs = np.linspace(0, 1.08, 50)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.3))
    ax1.plot(xs, f["a"] * xs + f["b"], color=C0, lw=2,
             label=rf"$T^2$ = {f['a']:.3f} $\ell$ + {f['b']:.3f}")
    ax1.errorbar(x, y, yerr=sy, fmt="o", color=style.FG, ms=5, zorder=5, label="data")
    ax1.set(xlabel=ELL, ylabel=r"$T^2$ (s$^2$)", xlim=(0, 1.08), ylim=(0, 4.5))
    ax1.legend(loc="upper left")
    ax2.axhline(0, color=C0, lw=2)
    ax2.errorbar(x, y - f["a"] * x - f["b"], yerr=sy, fmt="o", color=style.FG, ms=5,
                 capsize=3, zorder=5)
    ax2.set(xlabel=ELL, ylabel=r"residual (s$^2$)", xlim=(0.1, 1.1), ylim=(-0.075, 0.075))
    ax2.set_title(rf"$\chi^2$ = {f['chi2']:.2f} for {f['ndf']}", fontsize=12,
                  fontweight="normal", loc="left")
    style.save(fig, "viz_fitting_pendulum_fit")


def _d0_fit_fig():
    d = d0_fit()
    m, n, s, p, e = d["m"], d["n"], d["s"], d["popt"], d["err"]
    ms = np.linspace(*D0_WINDOW, 400)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.4, 3.6), sharex=True,
                                   gridspec_kw={"height_ratios": [3, 1]})
    bkg = p[3] + p[4] * (ms - 1865)
    ax1.fill_between(ms, bkg, d0_model(ms, *p), color=C1, alpha=0.25, lw=0, label="Gaussian")
    ax1.plot(ms, bkg, color=C2, lw=1.6, ls="--", label="straight line")
    ax1.plot(ms, d0_model(ms, *p), color=C1, lw=2.2, label="fitted model")
    ax1.errorbar(m, n, yerr=s, fmt="o", color=style.FG, ms=3.5, lw=1, label=r"data, $\sqrt{n}$")
    ax1.set(ylabel="entries per 2 MeV", ylim=(0, 4200), xlim=D0_WINDOW)
    ax1.text(0.015, 0.93, rf"$\mu$ = {p[1]:.2f} ± {e[1]:.2f} MeV/$c^2$" "\n"
             rf"$\chi^2$ = {d['chi2']:.1f} for {d['ndf']}",
             transform=ax1.transAxes, va="top", fontsize=11, linespacing=1.5)
    ax1.legend(loc="upper right", fontsize=9.5)
    ax2.axhspan(-2, 2, color=style.DIM, alpha=0.15, lw=0)
    ax2.axhline(0, color=style.DIM, lw=1)
    ax2.plot(m, d["pulls"], "o", color=C0, ms=4)
    ax2.set(xlabel=r"$M$ (MeV/$c^2$)", ylabel="pull", ylim=(-4, 4))
    style.save(fig, "viz_fitting_d0_fit")


D0_PARAMS = ["A", r"$\mu$", r"$\sigma$", r"$c_0$", r"$c_1$"]


def _covariance():
    """Correlation matrix of the D0 fit and the (A, sigma) ellipse (a parked slide)."""
    d = d0_fit()
    popt, pcov, err = d["popt"], d["pcov"], d["err"]
    corr = pcov / np.outer(err, err)
    k = len(popt)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.4),
                                   gridspec_kw={"width_ratios": [1, 1.25]})
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "diverging", [style.CYCLE[1], "#333b4a", style.ACCENT])
    norm = mcolors.Normalize(vmin=-1, vmax=1)
    # pcolormesh, not imshow: every cell a vector rectangle, each edge in its
    # own colour so no seam shows between neighbours
    edges = np.arange(k + 1) - 0.5
    im = ax1.pcolormesh(edges, edges, corr, cmap=cmap, norm=norm, edgecolors="face",
                        linewidth=0.5)
    ax1.set(xlim=(-0.5, k - 0.5), ylim=(k - 0.5, -0.5), aspect="equal")
    ax1.set_xticks(range(k))
    ax1.set_xticklabels(D0_PARAMS, fontsize=12)
    ax1.set_yticks(range(k))
    ax1.set_yticklabels(D0_PARAMS, fontsize=12)
    ax1.grid(False)
    for spine in ax1.spines.values():
        spine.set_visible(False)
    for i in range(k):
        for j in range(k):
            v = np.round(corr[i, j], 2) + 0.0
            r, g, b, _ = cmap(norm(v))
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            ax1.text(j, i, f"{v:+.2f}".replace("-", "−"), ha="center", va="center",
                     fontsize=11, color="#0b0f14" if lum > 0.55 else style.FG)
    cbar = fig.colorbar(im, ax=ax1, shrink=0.8, pad=0.04)
    # a colour bar of 256 colours is drawn as an image unless told otherwise
    cbar.solids.set_rasterized(False)
    cbar.solids.set_edgecolor("face")
    cbar.outline.set_visible(False)
    cbar.ax.tick_params(colors=style.DIM, labelsize=9)
    ax1.set_title(r"Correlation matrix of the $D^0$ fit")
    iA, iS = 0, 2
    center = popt[[iA, iS]]
    cov2 = pcov[np.ix_([iA, iS], [iA, iS])]
    e1, e2 = _ellipse(center, cov2, 1.0), _ellipse(center, cov2, 2.30)
    ax2.fill(e2[0], e2[1], color=style.CYCLE[1], alpha=0.18, lw=0)
    ax2.plot(e2[0], e2[1], color=style.CYCLE[1], lw=2.0, label=r"$\Delta\chi^2$ = 2.30")
    ax2.fill(e1[0], e1[1], color=style.ACCENT, alpha=0.28, lw=0)
    ax2.plot(e1[0], e1[1], color=style.ACCENT, lw=2.2, label=r"$\Delta\chi^2$ = 1")
    ax2.plot(*center, "o", color=style.FG, ms=6, zorder=5, label="minimum")
    ax2.set_xlim(center[0] - 2.3 * err[iA], center[0] + 2.3 * err[iA])
    ax2.set_ylim(center[1] - 2.3 * err[iS], center[1] + 2.3 * err[iS])
    ax2.set_xlabel(rf"height $A$:  {popt[iA]:.0f} ± {err[iA]:.0f} per 2 MeV")
    ax2.set_ylabel(rf"width $\sigma$:  {popt[iS]:.2f} ± {err[iS]:.2f} MeV/$c^2$")
    ax2.set_title(r"Contours of $\chi^2$ in the ($A$, $\sigma$) plane")
    ax2.legend(loc="upper right", fontsize=10)
    style.save(fig, "viz_fitting_covariance")


def _d0_data():
    M = d0_mass()
    n_all, edges = np.histogram(M, bins=65, range=(1800, 1930))
    m, n, s = d0_hist()
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
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


def _d0_models():
    """Pulls of three models of the D0 histogram: too few terms show a pattern."""
    m, n, s = d0_hist()
    alt = _d0_alt_models()
    rows = [("line", "a straight line, k = 2"),
            ("gauss_const", "Gaussian on a constant, k = 4"),
            ("gauss_line", "Gaussian on a line, k = 5")]
    fig, axes = plt.subplots(1, 3, figsize=(9.4, 3.3))
    for ax, (key, label) in zip(axes, rows):
        fn, p, c2, ndf, _ = alt[key]
        pulls = (n - fn(m, *p)) / s
        lim = 60 if key == "line" else 4.6
        ax.axhspan(-2, 2, color=style.DIM, alpha=0.15, lw=0)
        ax.axhline(0, color=style.DIM, lw=1)
        ax.plot(m, pulls, "o", color=C2 if key == "gauss_line" else C1, ms=3.5)
        ax.set(ylim=(-lim * 0.5 if key == "line" else -lim, lim), xlim=D0_WINDOW,
               xlabel=r"$M$ (MeV/$c^2$)")
        ax.set_title(f"{label}\n" + rf"$\chi^2$ = {c2:.1f} for {ndf}", loc="left",
                     fontsize=11, fontweight="normal", linespacing=1.4)
        ax.xaxis.grid(False)
    axes[0].set_ylabel("pull")
    style.save(fig, "viz_fitting_d0_models")


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


def _outlier():
    x, t10, T, y, sy = pendulum_data()
    f = weighted_line(x, y, sy)
    t = t10.copy()
    t[2] = 16.21
    yo, so = (t / 10) ** 2, 2 * (t / 10) * 0.01
    fo = weighted_line(x, yo, so)
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
    "viz_fitting_year_means": _year_means_fig,
    "viz_fitting_three_models": _three_models,
    "viz_fitting_parts": _parts_fig,
    "viz_fitting_slope_gauss": _slope_gauss_fig,
    "viz_fitting_amplitudes": _amplitudes_fig,
    "viz_fitting_sum_squares": _sum_squares_fig,
    "viz_fitting_tangent": _tangent_fig,
    "viz_fitting_gauss": _gauss_fig,
    "viz_fitting_guesses": _guesses_fig,
    "viz_fitting_best_line": _best_line_fig,
    "viz_fitting_chi2_slope": _chi2_slope_fig,
    "viz_fitting_band": _band_fig,
    "viz_fitting_years_needed": _years_needed_fig,
    "viz_fitting_descent_hours": _descent_hours_fig,
    "viz_fitting_descent_line": _descent_line_fig,
    "viz_fitting_daily": _daily_fig,
    "viz_fitting_cycle_parts": _cycle_parts_fig,
    "viz_fitting_cycle_fit": _cycle_fit_fig,
    "viz_fitting_line_resid": _line_resid_fig,
    "viz_fitting_cycle_resid": _cycle_resid_fig,
    "viz_fitting_too_few": _too_few_fig,
    "viz_fitting_too_many": _too_many_fig,
    "viz_fitting_ellipse": _ellipse_fig,
    "viz_fitting_chi2_dist": _chi2_dist,
    "viz_fitting_pendulum_fit": _pendulum_fit,
    "viz_fitting_d0_fit": _d0_fit_fig,
    "viz_fitting_covariance": _covariance,
    "viz_fitting_d0_data": _d0_data,
    "viz_fitting_d0_models": _d0_models,
    "viz_fitting_start_values": _start_values,
    "viz_fitting_outlier": _outlier,
}


if __name__ == "__main__":
    numbers()
