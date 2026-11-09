"""Figures of Lecture 08: Data Quality and Uncertainty.

Every figure and every number of the lecture is computed here from the
weather station's hourly log, `lectures/workbook/docs/data/weather.csv`
(87 672 rows, 2016 to 2025; `temp_c` is -999 in the 120 hours of 22 to 26
July 2019). Simulations draw hours from the log with
`np.random.default_rng(seed)`, so every run gives the same numbers. Run the
module directly to print every number the slides state.

The opening and data quality
  viz_probability_every_row        every row in file order, -999 included
The distribution
  viz_probability_hist_mean        the hours in bins of 1 degree, the mean
  viz_probability_hist_sd          the same with mean +- s
Probability by counting
  viz_probability_running_share    the share of frost hours as hours are counted
  viz_probability_frost_months     P(frost) in each month
  viz_probability_frost_march      P(frost) at each hour of the day in March
The Gaussian
  viz_probability_gaussian         the curve and its 68 / 95 / 99.7 % areas
  viz_probability_hours_gauss      the hours against a Gaussian of the same mean and s
  viz_probability_means_random     means of 100 random hours: a Gaussian
The standard error
  viz_probability_intervals        50 means of 100 random hours, each +- s/10
Correlation
  viz_probability_temp_humidity    temperature and humidity of every hour
  viz_probability_pairs            random pairs of hours against an hour and the next
  viz_probability_day_of_year      daily means against the day of the year
Hours that are not independent
  viz_probability_random_vs_row    means of 1000 random hours and of 1000 in a row
  viz_probability_lag              r of two hours against the hours between them
  viz_probability_year_means       the ten yearly means
For the curious
  viz_probability_binomial         frost hours among 10: random against in a row
  viz_probability_poisson          hours of 30 degrees or more among 1000 random hours
"""
import math
from datetime import date, datetime

import matplotlib.pyplot as plt
import numpy as np

import style

PATH = style.ROOT / "lectures" / "workbook" / "docs" / "data" / "weather.csv"
WARM = style.CYCLE[1]      # overlays: the mean, a curve over bars
GREEN = style.CYCLE[2]
PINK = style.CYCLE[3]
TEMP_LABEL = "temperature (°C)"


# ---------------------------------------------------------------------------
# The log
# ---------------------------------------------------------------------------

_LOG = {}


def log():
    """The columns of weather.csv as arrays, read once."""
    if not _LOG:
        lines = open(PATH).read().splitlines()[1:]
        cols = [line.split(",") for line in lines]
        _LOG["time"] = [c[0] for c in cols]
        _LOG["temp"] = np.array([float(c[1]) for c in cols])
        _LOG["hum"] = np.array([float(c[2]) for c in cols])
        _LOG["wind"] = np.array([float(c[3]) for c in cols])
        _LOG["ok"] = _LOG["temp"] != -999
        _LOG["year"] = np.array([int(t[0:4]) for t in _LOG["time"]])
        _LOG["month"] = np.array([int(t[5:7]) for t in _LOG["time"]])
        _LOG["day"] = np.array([int(t[8:10]) for t in _LOG["time"]])
        _LOG["hour"] = np.array([int(t[11:13]) for t in _LOG["time"]])
    return _LOG


def measured():
    d = log()
    return d["temp"][d["ok"]]


def mean_sd(values):
    values = np.asarray(values, dtype=float)
    return values.mean(), values.std(ddof=1)


def gauss(x, mu, sigma):
    return np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))


def phi(z):
    """The share of a Gaussian below z standard deviations."""
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def pairs():
    """Frost in this hour (a) and in the hour before (b), over the 87 550
    neighbouring pairs whose two hours are both measured."""
    t = log()["temp"]
    now, before = t[1:], t[:-1]
    both = (now != -999) & (before != -999)
    return (now < 0)[both], (before < 0)[both]


def r(x, y):
    return float(np.corrcoef(x, y)[0, 1])


def lag_r(k):
    """r of the temperature of an hour and of the hour k hours later."""
    t = log()["temp"]
    x, y = t[:-k], t[k:]
    both = (x != -999) & (y != -999)
    return r(x[both], y[both])


def year_means():
    d = log()
    return [float(d["temp"][d["ok"] & (d["year"] == y)].mean()) for y in range(2016, 2026)]


def random_means(n, repeats=2000, seed=1):
    """Means of n hours drawn at random from the measured hours."""
    v = measured()
    rng = np.random.default_rng(seed)
    return np.array([rng.choice(v, n).mean() for _ in range(repeats)])


def row_means(n, repeats=2000, seed=2):
    """Means of n measured hours in a row, from random starts."""
    v = measured()
    rng = np.random.default_rng(seed)
    starts = rng.integers(0, len(v) - n, repeats)
    return np.array([v[k:k + n].mean() for k in starts])


def daily_means():
    """The day of the year and the mean temperature of each day whose 24
    hours are all measured."""
    d = log()
    sums, counts = {}, {}
    for t, temp, ok in zip(d["time"], d["temp"], d["ok"]):
        if not ok:
            continue
        key = t[0:10]
        sums[key] = sums.get(key, 0.0) + temp
        counts[key] = counts.get(key, 0) + 1
    days, means = [], []
    for key in sorted(sums):
        if counts[key] == 24:
            days.append(date.fromisoformat(key).timetuple().tm_yday)
            means.append(sums[key] / 24)
    return np.array(days), np.array(means)


def _bins(ax):
    ax.set_xlim(-17, 33)
    ax.set_xticks(range(-15, 35, 5))
    ax.xaxis.grid(False)


# ---------------------------------------------------------------------------
# Data quality
# ---------------------------------------------------------------------------

def _every_row():
    d = log()
    when = [datetime.fromisoformat(t) for t in d["time"]]
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    ax.plot(when, d["temp"], color=style.ACCENT, linewidth=0.5)
    i = int(np.argmax(~d["ok"]))
    ax.annotate("120 hours of −999\n22 to 26 July 2019", xy=(when[i], -999),
                xytext=(when[i - 9000], -700), color=WARM, fontsize=11,
                ha="right", arrowprops=dict(arrowstyle="->", color=WARM, lw=1.2))
    ax.set(xlabel="time", ylabel="temp_c as read (°C)", ylim=(-1080, 120))
    ax.set_yticks([-1000, -750, -500, -250, 0])
    style.save(fig, "viz_probability_every_row")


# ---------------------------------------------------------------------------
# The distribution
# ---------------------------------------------------------------------------

def _hist_axes(figsize):
    v = measured()
    fig, ax = plt.subplots(figsize=figsize)
    counts, _, _ = ax.hist(v, bins=50, range=(-17, 33), color=style.ACCENT)
    ax.set(xlabel=TEMP_LABEL, ylabel="hours per 1 °C", ylim=(0, 4500))
    _bins(ax)
    return fig, ax, v, counts


def _hist_mean():
    fig, ax, v, counts = _hist_axes((9.4, 3.3))
    m = v.mean()
    ax.axvline(m, color=WARM, linewidth=2)
    ax.text(m + 0.4, 4280, f"mean {m:.2f} °C", color=WARM, fontsize=12, va="top")
    ax.text(-0.5, counts[16] + 60, f"{int(counts[16])}", ha="center", fontsize=10,
            color=style.FG)
    ax.text(11.5, counts[28] + 60, f"{int(counts[28])}", ha="center", fontsize=10,
            color=style.FG)
    ax.annotate(f"{int(counts[24])}", xy=(7.5, counts[24] + 40), xytext=(4.6, 3560),
                fontsize=10, color=style.FG, ha="center",
                arrowprops=dict(arrowstyle="-", color=style.FG, lw=0.8))
    style.save(fig, "viz_probability_hist_mean")


def _hist_sd():
    fig, ax, v, counts = _hist_axes((9.4, 3.3))
    m, s = mean_sd(v)
    inside = ((v > m - s) & (v < m + s)).mean()
    ax.set_ylim(0, 4900)
    ax.fill_between([m - s, m + s], 0, 4050, color=WARM, alpha=0.16, linewidth=0, zorder=0)
    ax.vlines([m - s, m + s], 0, 4050, color=WARM, linewidth=1.4, linestyle="--")
    ax.vlines([m], 0, 4050, color=WARM, linewidth=2)
    ax.annotate("", xy=(m - s, 4150), xytext=(m + s, 4150),
                arrowprops=dict(arrowstyle="<->", color=WARM, lw=1.3))
    label = f"mean ± s: {m - s:.1f} to {m + s:.1f} °C, {100 * inside:.1f} % of the hours"
    ax.text(m, 4330, label.replace("-", "−"), color=WARM, fontsize=11.5, ha="center")
    style.save(fig, "viz_probability_hist_sd")


# ---------------------------------------------------------------------------
# Probability by counting
# ---------------------------------------------------------------------------

def _running_share():
    v = measured()
    frost = (v < 0).astype(float)
    n = np.arange(1, len(v) + 1)
    in_time = np.cumsum(frost) / n
    rng = np.random.default_rng(5)
    shuffled = frost[rng.permutation(len(v))]
    at_random = np.cumsum(shuffled) / n
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    ax.axhline(frost.mean(), color=style.DIM, linewidth=1.2, linestyle="--")
    ax.plot(n, in_time, color=WARM, linewidth=1.6, label="in time order, from 1 January 2016")
    ax.plot(n, at_random, color=style.ACCENT, linewidth=1.8, label="in random order")
    ax.text(1.2, frost.mean() + 0.03, f"{frost.mean():.3f}", color=style.DIM, fontsize=11)
    ax.set_xscale("log")
    ax.set_xticks([1, 10, 100, 1000, 10000, len(v)])
    ax.set_xticklabels(["1", "10", "100", "1000", "10 000", f"{len(v):,}".replace(",", " ")])
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.set(xlabel="hours counted", ylabel="share below 0 °C", xlim=(1, len(v)),
           ylim=(0, 1.05))
    ax.legend(loc="upper right")
    style.save(fig, "viz_probability_running_share")


MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def frost_by_month():
    d = log()
    out = []
    for k in range(1, 13):
        sel = d["ok"] & (d["month"] == k)
        out.append((int(sel.sum()), int((d["temp"][sel] < 0).sum())))
    return out


def _frost_months():
    shares = [f / n for n, f in frost_by_month()]
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.bar(MONTHS, shares, color=style.ACCENT, width=0.7)
    ax.axhline((measured() < 0).mean(), color=style.DIM, linewidth=1.2, linestyle="--")
    ax.text(6.5, 0.275, "all hours: 0.255", color=style.DIM, fontsize=10.5, ha="center")
    for i, p in enumerate(shares):
        label = "0" if p == 0 else ("<0.01" if p < 0.005 else f"{p:.2f}")
        ax.text(i, p + 0.015, label, ha="center", fontsize=9.5, color=style.FG)
    ax.set(ylabel="P(frost)", ylim=(0, 1))
    ax.xaxis.grid(False)
    style.save(fig, "viz_probability_frost_months")


def frost_march():
    d = log()
    return [float((d["temp"][d["ok"] & (d["month"] == 3) & (d["hour"] == h)] < 0).mean())
            for h in range(24)]


def _frost_march():
    shares = frost_march()
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.bar(range(24), shares, color=style.ACCENT, width=0.75)
    ax.axhline(frost_by_month()[2][1] / frost_by_month()[2][0], color=style.DIM,
               linewidth=1.2, linestyle="--")
    ax.text(15, 0.395, "all of March: 0.37", color=style.DIM, fontsize=10.5, ha="center")
    for h in (3, 14):
        ax.text(h, shares[h] + 0.015, f"{shares[h]:.2f}", ha="center", fontsize=10.5,
                color=WARM)
    ax.set_xticks(range(0, 24, 3))
    ax.set_xticklabels([f"{h:02d}:00" for h in range(0, 24, 3)])
    ax.set(xlabel="hour of the day", ylabel="P(frost) in March", ylim=(0, 0.8), xlim=(-0.7, 23.7))
    ax.xaxis.grid(False)
    style.save(fig, "viz_probability_frost_march")


# ---------------------------------------------------------------------------
# The Gaussian
# ---------------------------------------------------------------------------

def _gaussian():
    x = np.linspace(-4, 4, 500)
    y = gauss(x, 0, 1)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    for lim, alpha in [(3, 0.18), (2, 0.34), (1, 0.6)]:
        sel = np.abs(x) <= lim
        ax.fill_between(x[sel], y[sel], color=style.ACCENT, alpha=alpha, linewidth=0)
    ax.plot(x, y, color=style.FG, linewidth=1.6)
    ax.text(0, 0.17, "68.3 %", ha="center", fontsize=13, color="#0b0e14",
            fontweight="bold")
    for lim, label, yy in [(1, "", 0.415), (2, "95.4 %", 0.47), (3, "99.7 %", 0.535)]:
        ax.annotate("", xy=(-lim, yy), xytext=(lim, yy),
                    arrowprops=dict(arrowstyle="<->", color=style.DIM, lw=1.1))
        if label:
            ax.text(0, yy + 0.01, label, ha="center", fontsize=12, color=style.FG)
    ax.set_xticks(range(-3, 4))
    ax.set_xticklabels([r"$\mu - 3\sigma$", r"$\mu - 2\sigma$", r"$\mu - \sigma$", r"$\mu$",
                        r"$\mu + \sigma$", r"$\mu + 2\sigma$", r"$\mu + 3\sigma$"], fontsize=11)
    ax.set_yticks([])
    ax.set(xlim=(-4, 4), ylim=(0, 0.6), ylabel="f(x)")
    ax.grid(False)
    style.save(fig, "viz_probability_gaussian")


def _hours_gauss():
    fig, ax, v, counts = _hist_axes((9.4, 3.3))
    m, s = mean_sd(v)
    x = np.linspace(-17, 33, 400)
    ax.plot(x, len(v) * gauss(x, m, s), color=WARM, linewidth=2.4,
            label=rf"Gaussian: $\mu$ = {m:.2f}, $\sigma$ = {s:.2f} °C")
    ax.legend(loc="upper right")
    style.save(fig, "viz_probability_hours_gauss")


def _means_random():
    v = measured()
    m, s = mean_sd(v)
    means = random_means(100)
    se = s / 10
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.hist(means, bins=np.arange(3.9, 10.45, 0.25), color=style.ACCENT)
    x = np.linspace(3.9, 10.4, 300)
    ax.plot(x, len(means) * 0.25 * gauss(x, m, se), color=WARM, linewidth=2.2,
            label=rf"Gaussian: $\mu$ = {m:.2f}, $\sigma$ = s/10 = {se:.3f} °C")
    ax.set(xlabel="mean of 100 hours (°C)", ylabel="means per 0.25 °C", xlim=(3.9, 10.4),
           ylim=(0, 275))
    ax.xaxis.grid(False)
    ax.legend(loc="upper left", fontsize=9.5)
    style.save(fig, "viz_probability_means_random")


def interval_means(k=50, seed=11):
    """k means of 100 hours drawn at random."""
    v = measured()
    rng = np.random.default_rng(seed)
    return np.array([rng.choice(v, 100).mean() for _ in range(k)])


def _intervals():
    v = measured()
    m, s = mean_sd(v)
    se = s / 10
    means = interval_means()
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    ax.axvline(m, color=style.FG, linewidth=1.4)
    for i, x in enumerate(means):
        hit = abs(x - m) < se
        colour = style.ACCENT if hit else style.BAD
        ax.plot([x - se, x + se], [i, i], color=colour, linewidth=2.2, solid_capstyle="butt")
        ax.plot([x], [i], "o", color=colour, markersize=3.5)
    ax.text(m + 0.08, len(means) + 0.6, f"the mean of all hours, {m:.2f} °C", color=style.FG,
            fontsize=11)
    ax.set(xlabel="mean of 100 hours ± s/10 (°C)", xlim=(4.0, 10.3),
           ylim=(-1, len(means) + 2.4))
    ax.set_yticks([])
    ax.grid(False)
    ax.spines["left"].set_visible(False)
    style.save(fig, "viz_probability_intervals")


# ---------------------------------------------------------------------------
# Correlation
# ---------------------------------------------------------------------------

def _temp_humidity():
    d = log()
    t, h = d["temp"][d["ok"]], d["hum"][d["ok"]]
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    hb = ax.hexbin(t, h, gridsize=(46, 30), mincnt=1, cmap="viridis", bins="log",
                   linewidths=0)
    cb = fig.colorbar(hb, ax=ax, pad=0.02)
    cb.set_label("hours per cell")
    cb.set_ticks([1, 10, 100])
    cb.set_ticklabels(["1", "10", "100"])
    cb.outline.set_visible(False)
    ax.set(xlabel=TEMP_LABEL, ylabel="humidity (%)", xlim=(-17, 33), ylim=(32, 102))
    ax.grid(False)
    style.save(fig, "viz_probability_temp_humidity")


def pair_samples(n=4000, seed=3):
    v = measured()
    rng = np.random.default_rng(seed)
    i = rng.integers(0, len(v), n)
    j = rng.integers(0, len(v), n)
    k = rng.integers(0, len(v) - 1, n)
    return (v[i], v[j]), (v[k], v[k + 1])


def _pairs():
    (a, b), (c, e) = pair_samples()
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6), sharex=True, sharey=True)
    for ax, (x, y), title in [
        (axes[0], (a, b), f"two hours drawn at random: r = {r(a, b):+.2f}"),
        (axes[1], (c, e), f"an hour and the next: r = {r(c, e):+.3f}"),
    ]:
        ax.scatter(x, y, s=4, color=style.ACCENT, alpha=0.5, linewidth=0)
        ax.set_title(title.replace("-", "−"), fontsize=12)
        ax.set(xlim=(-17, 33), ylim=(-17, 33), xlabel="the first hour (°C)")
        ax.set_aspect("equal")
    axes[0].set_ylabel("the second hour (°C)")
    style.save(fig, "viz_probability_pairs")


def _day_of_year():
    days, means = daily_means()
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.scatter(days, means, s=4, color=style.ACCENT, alpha=0.55, linewidth=0)
    ax.set(xlabel="day of the year", ylabel="daily mean temperature (°C)",
           xlim=(1, 366), ylim=(-20, 30))
    ax.set_xticks([1, 60, 121, 182, 244, 305, 366])
    ax.set_title(f"r = {r(days, means):+.2f}", fontsize=13)
    style.save(fig, "viz_probability_day_of_year")


# ---------------------------------------------------------------------------
# Hours that are not independent
# ---------------------------------------------------------------------------

def _random_vs_row():
    v = measured()
    m, s = mean_sd(v)
    a, b = random_means(1000), row_means(1000)
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3), sharex=True)
    edges = np.arange(-8, 23, 0.5)
    for ax, values, title, colour in [
        (axes[0], a, f"1000 hours drawn at random: means scatter by {a.std(ddof=1):.2f} °C",
         style.ACCENT),
        (axes[1], b, f"1000 hours in a row: means scatter by {b.std(ddof=1):.2f} °C", WARM),
    ]:
        ax.hist(values, bins=edges, color=colour)
        ax.set_title(title, fontsize=11.5)
        ax.set(xlabel="mean of 1000 hours (°C)", xlim=(-8, 22.5))
        ax.xaxis.grid(False)
    axes[0].set_ylabel("means per 0.5 °C")
    style.save(fig, "viz_probability_random_vs_row")


LAG_MARKS = [(1, "1 h"), (24, "1 day"), (168, "1 week"), (720, "30 days"),
             (4368, "½ year"), (8760, "1 year")]


def lag_curve():
    """Every hour up to two days, then whole days up to two years, so that
    beyond two days the two hours always stand at the same time of day."""
    days = sorted(set(int(round(x)) for x in np.geomspace(3, 730, 150)))
    lags = list(range(1, 49)) + [24 * k for k in days]
    return np.array(lags), np.array([lag_r(k) for k in lags])


def _lag():
    lags, rs = lag_curve()
    fig, ax = plt.subplots(figsize=(9.4, 3.3))
    ax.axhline(0, color=style.DIM, linewidth=1)
    ax.plot(lags, rs, color=style.ACCENT, linewidth=2)
    for k, label in LAG_MARKS:
        val = lag_r(k)
        ax.plot([k], [val], "o", color=WARM, markersize=6)
        text = f"{val:+.3f}" if abs(val) > 0.99 else f"{val:+.2f}"
        ax.text(k * 1.15, val + (0.06 if val > 0 else -0.06), text.replace("-", "−"),
                ha="left", va="bottom" if val > 0 else "top", fontsize=10.5, color=WARM)
    ax.set_xscale("log")
    ax.set_xticks([k for k, _ in LAG_MARKS] + [17520])
    ax.set_xticklabels([label for _, label in LAG_MARKS] + ["2 years"])
    ax.xaxis.set_minor_locator(plt.NullLocator())
    ax.set(xlabel="time between the two hours", ylabel="r", xlim=(0.8, 21000),
           ylim=(-1.1, 1.2))
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    style.save(fig, "viz_probability_lag")


def _year_means():
    years = list(range(2016, 2026))
    ym = year_means()
    m, s = mean_sd(ym)
    se = s / math.sqrt(len(ym))
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.axhspan(m - s, m + s, color=style.DIM, alpha=0.16, linewidth=0)
    ax.axhspan(m - se, m + se, color=WARM, alpha=0.35, linewidth=0)
    ax.axhline(m, color=WARM, linewidth=1.6)
    ax.plot(years, ym, "o", color=style.ACCENT, markersize=8)
    for y, val in zip(years, ym):
        ax.text(y, val + (0.13 if val >= m else -0.24), f"{val:.2f}", ha="center",
                fontsize=9.5, color=style.FG)
    ax.text(2025.55, m + s - 0.04, f"± s = {s:.2f}", color=style.DIM, fontsize=10.5,
            ha="left", va="top")
    ax.text(2025.55, m + se - 0.03, f"± s/√10 = {se:.2f}", color=WARM, fontsize=10.5,
            ha="left", va="top")
    ax.set(ylabel="mean temperature (°C)", ylim=(5.5, 8.8), xlim=(2015.5, 2027.4))
    ax.set_xticks(years)
    ax.set_xticklabels([str(y) for y in years], rotation=0, fontsize=9)
    ax.xaxis.grid(False)
    style.save(fig, "viz_probability_year_means")


# ---------------------------------------------------------------------------
# For the curious
# ---------------------------------------------------------------------------

def binomial(n, p):
    return [math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]


def frost_counts(n=10, repeats=20000, seed=4):
    """The number of frost hours among n hours drawn at random and among n
    hours in a row, each repeated."""
    v = measured()
    frost = v < 0
    rng = np.random.default_rng(seed)
    random_k = np.array([frost[rng.integers(0, len(v), n)].sum() for _ in range(repeats)])
    starts = rng.integers(0, len(v) - n, repeats)
    row_k = np.array([frost[k:k + n].sum() for k in starts])
    return random_k, row_k


def _binomial():
    p = (measured() < 0).mean()
    expect = binomial(10, p)
    random_k, row_k = frost_counts()
    ks = np.arange(11)
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.3), sharey=True)
    for ax, k, title, colour in [
        (axes[0], random_k, "10 hours drawn at random", style.ACCENT),
        (axes[1], row_k, "10 hours in a row", WARM),
    ]:
        shares = [(k == i).mean() for i in ks]
        ax.bar(ks, shares, color=colour, width=0.75)
        ax.plot(ks, expect, "o", color=style.FG, markersize=5, label="binomial, p = 0.255")
        ax.set_title(title, fontsize=12)
        ax.set(xlabel="frost hours among the 10")
        ax.set_xticks(ks)
        ax.xaxis.grid(False)
    axes[0].set_ylabel("share of draws")
    axes[0].legend(loc="upper right")
    style.save(fig, "viz_probability_binomial")


def poisson(lam, kmax):
    return [lam ** k * math.exp(-lam) / math.factorial(k) for k in range(kmax + 1)]


def hot_counts(n=1000, repeats=20000, seed=6):
    v = measured()
    hot = v >= 30
    rng = np.random.default_rng(seed)
    return np.array([hot[rng.integers(0, len(v), n)].sum() for _ in range(repeats)])


def _poisson():
    v = measured()
    lam = 1000 * (v >= 30).mean()
    k = hot_counts()
    ks = np.arange(7)
    fig, ax = plt.subplots(figsize=(6.2, 4.3))
    ax.bar(ks, [(k == i).mean() for i in ks], color=style.ACCENT, width=0.75,
           label="1000 random hours, 20 000 times")
    ax.plot(ks, poisson(lam, 6), "o", color=WARM, markersize=7,
            label=rf"Poisson, $\lambda$ = {lam:.2f}")
    ax.set(xlabel="hours of 30 °C or more among the 1000", ylabel="share of draws")
    ax.set_xticks(ks)
    ax.xaxis.grid(False)
    ax.legend(loc="upper right")
    style.save(fig, "viz_probability_poisson")


FIGURES = {
    "viz_probability_every_row": _every_row,
    "viz_probability_hist_mean": _hist_mean,
    "viz_probability_hist_sd": _hist_sd,
    "viz_probability_running_share": _running_share,
    "viz_probability_frost_months": _frost_months,
    "viz_probability_frost_march": _frost_march,
    "viz_probability_gaussian": _gaussian,
    "viz_probability_hours_gauss": _hours_gauss,
    "viz_probability_means_random": _means_random,
    "viz_probability_intervals": _intervals,
    "viz_probability_temp_humidity": _temp_humidity,
    "viz_probability_pairs": _pairs,
    "viz_probability_day_of_year": _day_of_year,
    "viz_probability_random_vs_row": _random_vs_row,
    "viz_probability_lag": _lag,
    "viz_probability_year_means": _year_means,
    "viz_probability_binomial": _binomial,
    "viz_probability_poisson": _poisson,
}


# ---------------------------------------------------------------------------
# Every number of the slides
# ---------------------------------------------------------------------------

def _numbers():
    d = log()
    t = d["temp"]
    v = measured()
    n_all, n = len(t), len(v)
    m, s = mean_sd(v)
    print("== The log")
    print(f"rows {n_all}, measured {n}, marked -999: {n_all - n}")
    i = list(~d["ok"]).index(True)
    j = n_all - 1 - list(~d["ok"])[::-1].index(True)
    print(f"marks from {d['time'][i]} to {d['time'][j]}")
    print(f"sum of the measured hours {v.sum():.1f}, mean {m:.4f}")
    print(f"with the marks: ({v.sum():.1f} + {n_all - n} x (-999)) / {n_all} = "
          f"{(v.sum() - 999 * (n_all - n)) / n_all:.4f}; shift {m - t.mean():.3f}")
    print(f"marks are {100 * (n_all - n) / n_all:.2f} % of the rows")
    six = list(t[i - 4:i + 2])
    print(f"the six hours from {d['time'][i - 4]}: {six}")
    four = [x for x in six if x != -999]
    print(f"  mean with marks {sum(six) / 6:.2f}, without {sum(four) / 4:.3f}")
    print(f"  median with marks {np.median(six)}, without {np.median(four)}")

    print("== Checks")
    for name in ("temp", "hum", "wind"):
        col = d[name]
        good = col[col != -999]
        print(f"{name}: -999 in {(col == -999).sum()} rows; min {good.min()}, max {good.max()}")
    print("humidity outside 0..100:", int(((d["hum"] < 0) | (d["hum"] > 100)).sum()),
          "; wind < 0:", int((d["wind"] < 0).sum()),
          "; temp outside -50..50 (not -999):", int((d["ok"] & ((t < -50) | (t > 50))).sum()))
    times = d["time"]
    print("hours twice:", len(times) - len(set(times)), "; rows twice:",
          n_all - len(set(zip(times, t, d["hum"], d["wind"]))))
    steps = [datetime.fromisoformat(b) - datetime.fromisoformat(a)
             for a, b in zip(times, times[1:])]
    print("steps other than 1 hour:", sum(1 for x in steps if x.total_seconds() != 3600),
          "; days x 24 =", (date(2025, 12, 31) - date(2016, 1, 1)).days + 1, "x 24 =",
          ((date(2025, 12, 31) - date(2016, 1, 1)).days + 1) * 24)
    print(f"in F the coldest hour would be {(v.min() - 32) * 5 / 9:.1f} C, "
          f"the warmest {(v.max() - 32) * 5 / 9:.1f} C")
    sel = d["ok"] & (d["month"] == 7) & (d["day"] >= 22) & (d["day"] <= 26)
    fill = t[sel].mean()
    print(f"22-26 July of the other nine years: {sel.sum()} hours, mean {fill:.2f}")
    print(f"  filled with that: {(v.sum() + 120 * fill) / n_all:.3f}; filled with 0: "
          f"{v.sum() / n_all:.3f}; left out: {m:.3f}")

    print("== The distribution")
    counts, _ = np.histogram(v, bins=50, range=(-17, 33))
    print(f"bins: -1..0 {counts[16]}, 7..8 {counts[24]}, 11..12 {counts[28]}")
    cold = d["ok"] & np.isin(d["month"], [11, 12, 1, 2, 3])
    warm = d["ok"] & ~np.isin(d["month"], [11, 12, 1, 2, 3])
    mc, mw = t[cold].mean(), t[warm].mean()
    print(f"Nov-Mar {cold.sum()} hours, mean {mc:.2f}; Apr-Oct {warm.sum()} hours, mean {mw:.2f}; "
          f"weighted {(cold.sum() * mc + warm.sum() * mw) / n:.2f}")
    fm = sum(four) / 4
    dev = [x - fm for x in four]
    print(f"four hours: sum {sum(four):.1f}, mean {fm:.3f}")
    print("  deviations", [round(x, 3) for x in dev], "sum", round(sum(dev), 10))
    print("  squares", [round(x * x, 4) for x in dev], f"sum {sum(x * x for x in dev):.4f}")
    var4 = sum(x * x for x in dev) / 3
    print(f"  s2 = {var4:.4f}, s = {math.sqrt(var4):.4f}; dividing by N: {sum(x * x for x in dev) / 4:.4f}")
    print(f"log: sum of squares {((v - m) ** 2).sum():.0f} / {n - 1} = {s ** 2:.2f}, s = {s:.4f}, "
          f"mean - s = {m - s:.2f}, mean + s = {m + s:.2f}")
    var0 = v.var()
    halves = [(cold.sum(), t[cold].mean(), t[cold].var()), (warm.sum(), t[warm].mean(), t[warm].var())]
    within = sum(nk * vk for nk, mk, vk in halves) / n
    between = sum(nk * (mk - m) ** 2 for nk, mk, vk in halves) / n
    print(f"variance {var0:.2f} = within the halves {within:.2f} (s {math.sqrt(halves[0][2]):.2f}, "
          f"{math.sqrt(halves[1][2]):.2f}) + between them {between:.2f}")
    print("median", np.median(v), "percentiles 5 25 75 95:", np.percentile(v, [5, 25, 75, 95]))

    print("== Probability")
    frost = v < 0
    print(f"frost hours {frost.sum()} of {n}: P = {frost.mean():.4f}; not: {1 - frost.mean():.4f}")
    for k, (nh, nf) in enumerate(frost_by_month(), start=1):
        print(f"  month {k:2d}: {nf} of {nh} = {nf / nh:.3f}")
    a, b = pairs()
    print(f"pairs {len(a)}: A&B {(a & b).sum()}, A&~B {(a & ~b).sum()}, ~A&B {(~a & b).sum()}, "
          f"~A&~B {(~a & ~b).sum()}")
    print(f"  n(B) {b.sum()}, P(A|B) = {(a & b).sum() / b.sum():.4f}; n(~B) {(~b).sum()}, "
          f"P(A|~B) = {(a & ~b).sum() / (~b).sum():.4f}")
    print(f"  P(A and B) = {(a & b).mean():.4f}; P(A)P(B) = {a.mean() * b.mean():.4f}; "
          f"P(A or B) = {(a | b).mean():.4f} ({(a | b).sum()})")
    sel = d["ok"] & (d["month"] == 3) & (d["year"] == 2025) & (d["day"] == 10)
    day = [float(x) for x in t[sel]]
    before = sum(1 for i in range(1, 24) if day[i - 1] < 0)
    both = sum(1 for i in range(1, 24) if day[i - 1] < 0 and day[i] < 0)
    march = frost_march()
    print("March by hour", [round(x, 2) for x in march])
    print(f"10 March 2025: {day}")
    print(f"  frost hours {sum(1 for x in day if x < 0)}; both {both}, before {before}, "
          f"{both / before:.3f}")

    print("== The Gaussian")
    f0 = 1 / (s * math.sqrt(2 * math.pi))
    print(f"sqrt(2 pi) = {math.sqrt(2 * math.pi):.4f}; s sqrt(2 pi) = {s * math.sqrt(2 * math.pi):.2f}; "
          f"f(mu) = {f0:.4f}; x N = {n * f0:.0f}")
    print(f"  e^-1/2 = {math.exp(-0.5):.3f}: f = {f0 * math.exp(-0.5):.4f}, {n * f0 * math.exp(-0.5):.0f}; "
          f"e^-2 = {math.exp(-2):.3f}: f = {f0 * math.exp(-2):.4f}, {n * f0 * math.exp(-2):.0f}")
    for k in (1, 2, 3):
        inside = (v > m - k * s) & (v < m + k * s)
        print(f"  within {k} s: hours {inside.mean():.4f} ({inside.sum()}), Gaussian {2 * phi(k) - 1:.4f}")
    zc, zw = (v.min() - m) / s, (v.max() - m) / s
    print(f"  coldest z {zc:.2f}: Gaussian below {phi(zc):.4f} x N = {phi(zc) * n:.0f}; "
          f"warmest z {zw:.2f}: above {1 - phi(zw):.4f} x N = {(1 - phi(zw)) * n:.0f}")
    rm = random_means(100)
    print(f"means of 100 random hours: mean {rm.mean():.3f}, scatter {rm.std(ddof=1):.3f}, "
          f"s/10 = {s / 10:.3f}, within 1 se {(np.abs(rm - m) < s / 10).mean():.3f}, "
          f"within 2 se {(np.abs(rm - m) < 2 * s / 10).mean():.3f}")

    se = s / 10
    im = interval_means()
    print(f"50 intervals of +- {se:.3f}: {int((np.abs(im - m) < se).sum())} hold the mean, "
          f"{int((np.abs(im - m) < 2 * se).sum())} with +- 2 se")
    print("== Correlation")
    h4 = [float(x) for x in d["hum"][i - 4:i]]
    mh = sum(h4) / 4
    dh = [x - mh for x in h4]
    prod = [p * q for p, q in zip(dev, dh)]
    sxy = sum(prod)
    print(f"four hours humidity {h4}, mean {mh}, deviations {dh}")
    print("  products", [round(x, 4) for x in prod], f"sum {sxy:.4f}, s_xy {sxy / 3:.4f}")
    sx, sy = math.sqrt(var4), math.sqrt(sum(x * x for x in dh) / 3)
    print(f"  s_x {sx:.4f}, s_y {sy:.4f} (sum {sum(x * x for x in dh)}), r = {sxy / 3 / (sx * sy):.4f}")
    ok = d["ok"]
    print(f"r(T,H) {r(t[ok], d['hum'][ok]):.4f}; r(T,W) {r(t[ok], d['wind'][ok]):.4f}; "
          f"r(H,W) {r(d['hum'], d['wind']):.4f}")
    print(f"r(hour, next) {lag_r(1):.4f}; r(hour, a day later) {lag_r(24):.4f}")
    (pa, pb), (pc, pe) = pair_samples()
    print(f"pairs figure: random r {r(pa, pb):.3f}, neighbours r {r(pc, pe):.3f}")
    days, dm = daily_means()
    print(f"r(day of year, daily mean) {r(days, dm):.3f} over {len(days)} days")
    print("monthly means", [round(float(t[ok & (d['month'] == k)].mean()), 2) for k in range(1, 13)])

    print("== The standard error")
    rng = np.random.default_rng(3)
    x, y = rng.integers(0, n, 100000), rng.integers(0, n, 100000)
    k = rng.integers(0, n - 1, 100000)
    print(f"sum of two random hours: sd {np.std(v[x] + v[y], ddof=1):.2f}, "
          f"sqrt(2) s = {math.sqrt(2) * s:.2f}")
    rr = lag_r(1)
    print(f"sum of an hour and the next: sd {np.std(v[k] + v[k + 1], ddof=1):.2f}, "
          f"s sqrt(2 (1 + r)) = {s * math.sqrt(2 * (1 + rr)):.2f}, 2 s = {2 * s:.2f}")
    print(f"in F: s = 1.8 x {s:.2f} = {1.8 * s:.2f}; var = 3.24 x {s ** 2:.2f} = {3.24 * s ** 2:.1f}")
    print(f"sqrt(N) = {math.sqrt(n):.1f}; s / sqrt(N) = {s / math.sqrt(n):.4f}")
    for size in (100, 1000):
        rm = random_means(size)
        print(f"  N {size}: s/sqrt(N) {s / math.sqrt(size):.3f}, 2000 means scatter "
              f"{rm.std(ddof=1):.3f}")
    for size in (100, 400, 1600, 6400, 87552):
        print(f"  N {size}: {8.85 / size ** 0.5:.4f}")

    print("== Not independent")
    print(f"1000 in a row: scatter {row_means(1000).std(ddof=1):.2f}; random "
          f"{random_means(1000).std(ddof=1):.3f}")
    for k, label in LAG_MARKS:
        print(f"  r at {label}: {lag_r(k):.3f}")
    ym = year_means()
    my, sy_ = mean_sd(ym)
    print("yearly means", [round(x, 2) for x in ym], f"mean {my:.4f}")
    dy = [x - my for x in ym]
    print("  deviations", [round(x, 2) for x in dy])
    print("  squares", [round(x * x, 3) for x in dy], f"sum {sum(x * x for x in dy):.3f}")
    print(f"  s2 {sum(x * x for x in dy) / 9:.4f}, s {sy_:.4f}, s/sqrt(10) {sy_ / math.sqrt(10):.4f}")
    print(f"  as many independent hours as ({s:.2f} / {sy_ / math.sqrt(10):.3f})^2 = "
          f"{(s / (sy_ / math.sqrt(10))) ** 2:.0f}")
    print(f"  95 %: {my - 2 * sy_ / math.sqrt(10):.2f} to {my + 2 * sy_ / math.sqrt(10):.2f}")
    print(f"  s / sqrt(8760) = {s / math.sqrt(8760):.3f}")
    y25 = t[d["ok"] & (d["year"] == 2025)]
    print(f"  2025: {len(y25)} hours, mean {y25.mean():.2f}, s {y25.std(ddof=1):.2f}, "
          f"own se {y25.std(ddof=1) / math.sqrt(len(y25)):.3f}")
    own = [t[d["ok"] & (d["year"] == y)] for y in range(2016, 2026)]
    own_se = [x.std(ddof=1) / math.sqrt(len(x)) for x in own]
    print(f"  own se of the ten years: {min(own_se):.3f} to {max(own_se):.3f}")
    for hours in (1, 24, 24 * 7, 24 * 30, 24 * 365):
        kk = len(v) // hours
        blocks = v[:kk * hours].reshape(kk, hours).mean(axis=1)
        print(f"  blocks of {hours} h: {kk} blocks, s {blocks.std(ddof=1):.2f}, "
              f"se {blocks.std(ddof=1) / math.sqrt(kk):.3f}")

    print("== For the curious")
    pj = (d["ok"] & (d["month"] == 1)).sum() / n
    pfj = frost_by_month()[0][1] / frost_by_month()[0][0]
    print(f"P(Jan) {pj:.4f}, P(frost|Jan) {pfj:.4f}, Bayes {pfj * pj / frost.mean():.4f}, "
          f"counted {frost_by_month()[0][1] / frost.sum():.4f}")
    p = frost.mean()
    print("binomial(10, p):", [round(x, 3) for x in binomial(10, p)])
    rk, wk = frost_counts()
    print("  drawn at random:", [round(float((rk == i).mean()), 3) for i in range(11)])
    print("  in a row:", [round(float((wk == i).mean()), 3) for i in range(11)])
    hot = (v >= 30).sum()
    lam = 1000 * hot / n
    print(f"hours >= 30: {hot}; lambda = {lam:.3f}; Poisson:", [round(x, 3) for x in poisson(lam, 4)])
    hk = hot_counts()
    print("  drawn:", [round(float((hk == i).mean()), 3) for i in range(5)],
          f"mean {hk.mean():.3f}, var {hk.var():.3f}")
    print("  per year:", [int(((t >= 30) & d["ok"] & (d["year"] == y)).sum()) for y in range(2016, 2026)])
    print(f"F: 1.8 x 7.16 + 32 = {1.8 * 7.16 + 32:.2f} +- {1.8 * 0.22:.2f}")
    print(f"2023 - 2025 = {ym[7] - ym[9]:.2f} +- sqrt(2) x {sy_:.2f} = {math.sqrt(2) * sy_:.2f}")
    rng = np.random.default_rng(8)
    samples = rng.choice(v, (100000, 5))
    ss = ((samples - samples.mean(axis=1, keepdims=True)) ** 2).sum(axis=1)
    print(f"5 random hours, 100 000 times: mean of SS/5 {(ss / 5).mean():.1f}, SS/4 {(ss / 4).mean():.1f}, "
          f"s2 {s ** 2:.1f}, 4/5 s2 {0.8 * s ** 2:.1f}")


if __name__ == "__main__":
    _numbers()
