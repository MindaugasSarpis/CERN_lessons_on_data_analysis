"""Figures and numbers for Lecture 12, Pandas & Data Cleaning.

Two files, both read from lectures/workbook/docs/data/:

  * pendulum_raw.csv  the table as received in week 2 (semicolons, decimal
                      commas, a row-number column, a line with the mean), and
                      pendulum.csv, the copy that was cleaned by hand.
  * D0_KPi.csv        91 583 rows, columns M, PT, TAU, IPCHI2. TAU = -100 is
                      the file's code for a missing decay time.

Every number on the slides, the seminar page and the lecture page comes from
`numbers()` below. Print them all with

    python figures/src/cleaning.py          (needs numpy and pandas)

The figures public/figures/viz_cleaning_*.svg need NumPy and Matplotlib only;
build them with

    python figures/src/build.py --only cleaning
"""
import hashlib
import io

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

import style

DATA = style.ROOT / "lectures" / "workbook" / "docs" / "data"

MONO = "DejaVu Sans Mono"
AMBER, GREEN, PINK, VIOLET = style.CYCLE[1], style.CYCLE[2], style.CYCLE[3], style.CYCLE[4]
CELL = "#131926"

CODE = -100.0                # the file's code for a missing TAU
M_WINDOW = (1800.0, 1930.0)  # MeV/c^2: every row but two lies inside
PEAK = (1840.0, 1890.0)      # MeV/c^2: the region called "peak"


# =============================================================================
# Numbers
# =============================================================================

def d0():
    """The four columns of D0_KPi.csv as float64 arrays, TAU with the code."""
    return np.loadtxt(DATA / "D0_KPi.csv", delimiter=",", skiprows=1, unpack=True)


def clean_pendulum(pd):
    """The cleaning of the pendulum table, as on the slides."""
    df = pd.read_csv(DATA / "pendulum_raw.csv", sep=";", decimal=",")
    df = df[df["nr"].notna()]
    df = df.drop(columns="nr")
    df["length_cm"] = df["length_cm"].astype(int)
    return df


def clean_d0(pd):
    """The cleaning of the LHCb file, as on the slides. Returns (clean, log)."""
    df = pd.read_csv(DATA / "D0_KPi.csv")
    n_in = len(df)
    n_code = int((df["TAU"] == CODE).sum())
    df["TAU"] = df["TAU"].replace(CODE, np.nan)
    bad_tau = df["TAU"] < 0
    bad_m = ~df["M"].between(*M_WINDOW)
    dup = df.duplicated()
    clean = df[~bad_tau & ~bad_m & ~dup]
    log = dict(rows_in=n_in, code=n_code, bad_tau=int(bad_tau.sum()),
               bad_m=int(bad_m.sum()), dup=int(dup.sum()), rows_out=len(clean))
    return clean, log


def numbers():
    import pandas as pd

    out = []
    p = out.append

    # --- the pendulum table --------------------------------------------
    raw = DATA / "pendulum_raw.csv"
    hand = DATA / "pendulum.csv"
    p(f"pandas {pd.__version__}, numpy {np.__version__}")
    p("== pendulum_raw.csv")
    p(f"plain read_csv:      shape {pd.read_csv(raw).shape}")
    p(f"sep=';':             dtypes {pd.read_csv(raw, sep=';').dtypes.astype(str).to_dict()}")
    first = pd.read_csv(raw, sep=";", decimal=",")
    p(f"sep, decimal:        dtypes {first.dtypes.astype(str).to_dict()}")
    p(f"empty cells:         {first.isna().sum().to_dict()}")
    df = clean_pendulum(pd)
    p(f"cleaned:             shape {df.shape}, dtypes {df.dtypes.astype(str).to_dict()}")
    default = df.to_csv(index=False, lineterminator="\n").encode()
    fixed = df.to_csv(index=False, float_format="%.2f", lineterminator="\n").encode()
    by_hand = hand.read_bytes()
    p(f"bytes: by hand {len(by_hand)}, to_csv default {len(default)}, with float_format {len(fixed)}")
    p(f"identical to the hand-cleaned file: default {default == by_hand}, float_format {fixed == by_hand}")
    p(f"equal as tables: {pd.read_csv(io.BytesIO(default)).equals(pd.read_csv(hand))}")
    p(f"sha256 by hand   {hashlib.sha256(by_hand).hexdigest()}")
    p(f"sha256 by script {hashlib.sha256(fixed).hexdigest()}")
    df["g"] = 4 * np.pi ** 2 * (df["length_cm"] / 100) / (df["t10_s"] / 10) ** 2
    p(f"g per row: {df['g'].round(2).tolist()}")
    p(f"g mean {df['g'].mean():.3f}, std n-1 {df['g'].std():.3f}, std n {df['g'].std(ddof=0):.3f}, "
      f"standard error {df['g'].sem():.3f}")
    p(f"mean of t10_s {df['t10_s'].mean():.4f} (the file's mean line says 15,14)")

    # --- the LHCb file ---------------------------------------------------
    df = pd.read_csv(DATA / "D0_KPi.csv")
    tau = df["TAU"]
    p("== D0_KPi.csv")
    p(f"shape {df.shape}, dtypes {df.dtypes.astype(str).to_dict()}")
    p(f"bytes in memory: {df.memory_usage(index=False).sum()} + index {df.memory_usage()['Index']}")
    p(f"describe TAU: mean {tau.mean():.6f}, std {tau.std():.4f}, min {tau.min()}, "
      f"median {tau.median():.6f}, max {tau.max():.6f}")
    p(f"TAU == -100: {(tau == CODE).sum()} rows = {100 * (tau == CODE).mean():.3f} %")
    p(f"sum TAU with code {tau.sum():.3f}, without {tau[tau != CODE].sum():.3f}")
    nan = tau.replace(CODE, np.nan)
    p(f"after NaN: count {nan.count()}, mean {nan.mean():.6f}, std {nan.std():.6f}, min {nan.min():.6f}")
    p(f"comparisons: (TAU >= 0) {(nan >= 0).sum()}, (TAU < 0) {(nan < 0).sum()}, NaN {nan.isna().sum()}")
    gap = nan.isna()
    p(f"IPCHI2 median: rows with TAU {df.loc[~gap, 'IPCHI2'].median():.2f}, "
      f"rows without {df.loc[gap, 'IPCHI2'].median():.1f}")
    p(f"IPCHI2 > 1000: {(df.loc[gap, 'IPCHI2'] > 1000).sum()} of {gap.sum()} rows without TAU, "
      f"{100 * (df['IPCHI2'] > 1000).mean():.1f} % of all rows")
    p(f"negative TAU: {df.index[nan < 0].tolist()} -> {nan[nan < 0].tolist()}")
    out_m = df[~df["M"].between(*M_WINDOW)]
    p(f"M outside {M_WINDOW}: rows {out_m.index.tolist()}, M {out_m['M'].tolist()}, PT {out_m['PT'].tolist()}")
    inside = df.loc[df["M"].between(*M_WINDOW), "M"]
    p(f"all other M between {inside.min()} and {inside.max()}")
    p(f"M <= 0: {(df['M'] <= 0).sum()}, PT <= 0: {(df['PT'] <= 0).sum()}, IPCHI2 < 0: {(df['IPCHI2'] < 0).sum()}")
    for name, col in (("M", df["M"]), ("TAU", nan)):
        q1, q3 = col.quantile(0.25), col.quantile(0.75)
        lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
        n = ((col < lo) | (col > hi)).sum()
        p(f"IQR rule on {name}: Q1 {q1:.6g}, Q3 {q3:.6g}, fences {lo:.6g} and {hi:.6g}, "
          f"flags {n} rows = {100 * n / col.count():.1f} %")
    p(f"TAU > 0.01 ns: {(nan > 0.01).sum()} rows = {100 * (nan > 0.01).sum() / nan.count():.2f} %")
    p(f"duplicate rows {df.duplicated().sum()}, repeated M {df['M'].duplicated().sum()}, "
      f"distinct M {df['M'].nunique()}")
    p(f"M median {df['M'].median():.2f}, TAU median {nan.median() * 1000:.3f} ps")

    clean, log = clean_d0(pd)
    p(f"cleaning log: {log}")
    text = clean.to_csv(index=False, lineterminator="\n").encode()
    p(f"d0_clean.csv: {len(text)} bytes, sha256 {hashlib.sha256(text).hexdigest()}")
    p(f"raw file:     {(DATA / 'D0_KPi.csv').stat().st_size} bytes, "
      f"sha256 {hashlib.sha256((DATA / 'D0_KPi.csv').read_bytes()).hexdigest()}")
    back = pd.read_csv(io.BytesIO(text))
    p(f"read back: equals {back.equals(clean.reset_index(drop=True))}, NaN {back.isna().sum().to_dict()}")
    clean = clean.copy()
    clean["tau_ps"] = clean["TAU"] * 1000
    clean["region"] = np.where(clean["M"].between(*PEAK), "peak", "side")
    p(clean.groupby("region")["tau_ps"].agg(["size", "count", "median"]).round(3).to_string())
    return "\n".join(out)


# =============================================================================
# Figures
# =============================================================================

def _cell(ax, x, y, text="", w=1.0, h=1.0, fc=CELL, ec=style.DIM, tc=style.FG,
          size=11, mono=True, lw=1.0, weight="normal"):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, linewidth=lw))
    if text != "":
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=tc,
                fontsize=size, family=MONO if mono else None, weight=weight)


def _arrow(ax, p, q, color=style.DIM, lw=1.2):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=10,
                                 color=color, linewidth=lw, shrinkA=0, shrinkB=0))


def _dataframe():
    """The parts of a DataFrame, on the first rows of the pendulum table."""
    rows = [("0", "20", "9.02"), ("1", "30", "11.05"), ("2", "40", "12.61"),
            ("…", "…", "…"), ("8", "100", "20.01")]
    fig, ax = plt.subplots(figsize=(6.0, 4.1))
    ax.set(xlim=(0, 12.0), ylim=(0, 8.2))
    ax.set_aspect("equal")
    ax.axis("off")

    x0, wi, wc, h = 3.3, 1.1, 2.3, 0.9          # left edge, index width, column width, row height
    top = 6.0                                    # y of the header row
    size = 12.5
    # header: the column names
    _cell(ax, x0 + wi, top, "length_cm", w=wc, h=h, ec=style.ACCENT, tc=style.ACCENT, size=11.5)
    _cell(ax, x0 + wi + wc, top, "t10_s", w=wc, h=h, ec=style.ACCENT, tc=style.ACCENT, size=11.5)
    # body
    for i, (lab, a, b) in enumerate(rows):
        y = top - h * (i + 1)
        _cell(ax, x0, y, lab, w=wi, h=h, ec=AMBER, tc=AMBER, size=size)
        _cell(ax, x0 + wi, y, a, w=wc, h=h, size=size)
        _cell(ax, x0 + wi + wc, y, b, w=wc, h=h, size=size)
    # dtype line under the table
    yb = top - h * len(rows) - 0.75
    ax.text(x0 + wi + wc / 2, yb, "int64", ha="center", va="center", color=GREEN,
            fontsize=size, family=MONO)
    ax.text(x0 + wi + wc * 1.5, yb, "float64", ha="center", va="center", color=GREEN,
            fontsize=size, family=MONO)
    # one column = a Series
    ax.add_patch(Rectangle((x0 + wi + wc, top - h * len(rows)), wc, h * (len(rows) + 1),
                           facecolor="none", edgecolor=PINK, linewidth=2.4))
    # one row = one observation
    ax.add_patch(Rectangle((x0, top - h * 3), wi + 2 * wc, h, facecolor="none",
                           edgecolor=VIOLET, linewidth=2.4, linestyle=(0, (4, 2))))

    # labels
    ax.text(x0 + wi + wc, top + h + 0.55, "columns: the names", ha="center", va="center",
            color=style.ACCENT, fontsize=13)
    ax.text(0.0, top - h * 0.5, "index:\nrow labels", ha="left", va="center", color=AMBER, fontsize=13)
    _arrow(ax, (2.45, top - h * 0.5), (x0 - 0.1, top - h * 0.5), color=AMBER)
    ax.text(0.0, top - h * 2.5, "one row:\none\nobservation", ha="left", va="center",
            color=VIOLET, fontsize=13)
    _arrow(ax, (2.75, top - h * 2.5), (x0 - 0.1, top - h * 2.5), color=VIOLET)
    xr = x0 + wi + 2 * wc
    ax.text(xr + 0.75, top - h * 1.5, "one\ncolumn:\na Series", ha="left", va="center",
            color=PINK, fontsize=13)
    _arrow(ax, (xr + 0.65, top - h * 1.5), (xr + 0.1, top - h * 1.5), color=PINK)
    ax.text(0.0, yb, "dtype: one\nper column", ha="left", va="center", color=GREEN, fontsize=13)
    _arrow(ax, (2.6, yb), (x0 + wi + 0.2, yb), color=GREEN)
    style.save(fig, "viz_cleaning_dataframe")


def _tau_code():
    """TAU as stored, with the code -100, and after the code became NaN."""
    tau = d0()[2]
    real = tau[tau != CODE]
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.5))

    a.hist(tau, bins=np.arange(-105, 10, 5), color=style.ACCENT)
    a.set_yscale("log")
    a.set_ylim(0.5, 6e5)
    a.set_xlabel("TAU as stored (ns)")
    a.set_ylabel("rows per 5 ns")
    a.set_title("With the code", fontsize=12)
    a.annotate(f"{(tau == CODE).sum()} rows\nTAU = −100", xy=(-100, 49), xytext=(-84, 3e3),
               color=style.BAD, fontsize=10.5, ha="center",
               arrowprops=dict(arrowstyle="-|>", color=style.BAD))
    a.annotate(f"{len(real):,} rows\n−0.14 to 0.58 ns".replace(",", " "), xy=(0, 9e4), xytext=(-42, 6e4),
               color=style.FG, fontsize=10.5, ha="center", va="center",
               arrowprops=dict(arrowstyle="-|>", color=style.DIM))
    a.text(-50, 1.2, f"mean {tau.mean():.4f} ns\nstd {tau.std(ddof=1):.2f} ns", color=AMBER,
           fontsize=10.5, va="bottom", ha="center")

    ps = real * 1000
    b.hist(ps, bins=np.linspace(0, 3, 61), color=style.ACCENT)
    b.set_xlabel("TAU with −100 as NaN (ps)")
    b.set_ylabel("rows per 0.05 ps")
    b.set_title("With NaN", fontsize=12)
    b.axvline(np.median(ps), color=GREEN, linewidth=1.6)
    b.axvline(ps.mean(), color=AMBER, linewidth=1.6)
    top = b.get_ylim()[1]
    b.text(np.median(ps) + 0.04, top * 0.93, f"median {np.median(ps):.2f} ps", color=GREEN, fontsize=10.5)
    b.text(ps.mean() + 0.04, top * 0.78, f"mean {ps.mean():.2f} ps", color=AMBER, fontsize=10.5)
    b.text(2.95, top * 0.5, f"{(ps > 3).sum()} rows lie beyond 3 ps,\n{(ps < 0).sum()} rows below 0",
           color=style.DIM, fontsize=10, ha="right")
    style.save(fig, "viz_cleaning_tau_code")


def _missing_rows():
    """IPCHI2 of the rows with a decay time and of the 49 rows without one."""
    _, _, tau, ip = d0()
    gap = tau == CODE
    bins = np.logspace(-5, 6, 56)
    fig, ax = plt.subplots(figsize=(8.8, 3.5))
    ax.hist(ip[~gap], bins=bins, weights=np.full((~gap).sum(), 100 / (~gap).sum()),
            color=style.ACCENT, alpha=0.85, label=f"{(~gap).sum():,} rows with TAU".replace(",", " "))
    ax.hist(ip[gap], bins=bins, weights=np.full(gap.sum(), 100 / gap.sum()),
            histtype="step", color=style.BAD, linewidth=2.2, label=f"{gap.sum()} rows without TAU")
    ax.set_xscale("log")
    ax.set_xlabel("IPCHI2 (each step of the axis is a factor 10)")
    ax.set_ylabel("share of the group (%)")
    for group, color, side in ((ip[~gap], style.ACCENT, "left"), (ip[gap], style.BAD, "right")):
        m = np.median(group)
        ax.axvline(m, color=color, linewidth=1.4, linestyle=(0, (4, 2)))
        ax.text(m * (1.3 if side == "left" else 0.77), 23.5, f"median\n{m:,.1f}".replace(",", " "),
                color=color, fontsize=10.5, va="top", ha=side)
    ax.set_ylim(0, 25)
    ax.legend(loc="upper left")
    style.save(fig, "viz_cleaning_missing_rows")


def _outlier_rule():
    """The 1.5 x IQR rule on a bell-shaped column (M) and on a long tail (TAU)."""
    m, _, tau, _ = d0()
    ps = tau[tau != CODE] * 1000
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.5))

    q1, q3 = np.percentile(m, [25, 75])
    lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
    a.hist(m, bins=np.arange(1750, 2475, 5), color=style.ACCENT)
    a.set_yscale("log")
    a.set_ylim(0.5, 3e4)
    for f in (lo, hi):
        a.axvline(f, color=AMBER, linewidth=1.4, linestyle=(0, (4, 2)))
    flagged = m[(m < lo) | (m > hi)]
    a.plot(flagged, np.full(len(flagged), 1.0), "v", color=style.BAD, markersize=9, zorder=5)
    for v in flagged:
        a.text(v + 8, 2.6, f"{v:.2f}", color=style.BAD, fontsize=10, ha="right")
    a.set_xlim(1660, 2490)
    a.text(hi + 12, 4e3, f"fences\n{lo:.1f} and {hi:.1f}", color=AMBER, fontsize=10.5, va="center")
    a.set_xlabel("M (MeV/c²)")
    a.set_ylabel("rows per 5 MeV/c²")
    a.set_title(f"M: the rule flags {len(flagged)} rows", fontsize=12)

    q1, q3 = np.percentile(ps, [25, 75])
    hi = q3 + 1.5 * (q3 - q1)
    bins = np.logspace(np.log10(0.15), np.log10(600), 60)
    b.hist(ps[ps > 0], bins=bins, color=style.ACCENT)
    b.hist(ps[ps > hi], bins=bins, color=style.BAD)
    b.set_xscale("log")
    b.set_yscale("log")
    b.axvline(hi, color=AMBER, linewidth=1.4, linestyle=(0, (4, 2)))
    b.text(hi * 1.25, 1.2e4, f"fence {hi:.2f} ps", color=AMBER, fontsize=10.5)
    n = (ps > hi).sum()
    b.text(4.5, 1.6e3, f"{n:,} rows above the fence,\n{100 * n / len(ps):.1f} % of the column".replace(",", " "),
           color=style.BAD, fontsize=10.5)
    b.set_xlabel("TAU (ps, each step of the axis is a factor 10)")
    b.set_ylabel("rows per bin")
    b.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:g}"))
    b.set_title("TAU: the same rule flags one row in eight", fontsize=12)
    style.save(fig, "viz_cleaning_outlier_rule")


def _regions():
    """groupby on a derived column: the mass regions and their decay times."""
    m, _, tau, _ = d0()
    keep = ((tau == CODE) | (tau >= 0)) & (m >= M_WINDOW[0]) & (m <= M_WINDOW[1])
    m, tau = m[keep], tau[keep]
    peak = (m >= PEAK[0]) & (m <= PEAK[1])
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.5))

    bins = np.arange(1800, 1932, 2)
    a.hist(m[peak], bins=bins, color=style.ACCENT, label=f"peak: {peak.sum():,} rows".replace(",", " "))
    a.hist(m[~peak], bins=bins, color=AMBER, label=f"side: {(~peak).sum():,} rows".replace(",", " "))
    a.set_xlabel("M (MeV/c²)")
    a.set_ylabel("rows per 2 MeV/c²")
    a.set_title("Split: the column region", fontsize=12)
    a.set_ylim(0, a.get_ylim()[1] * 1.22)
    a.legend(loc="upper left", ncols=2, columnspacing=1.2)

    has = tau != CODE
    edges = np.linspace(0.15, 1.5, 46)
    for sel, color, name in ((peak & has, style.ACCENT, "peak"), (~peak & has, AMBER, "side")):
        ps = tau[sel] * 1000
        b.hist(ps, bins=edges, weights=np.full(len(ps), 100 / len(ps)), histtype="step",
               color=color, linewidth=2)
        med = np.median(ps)
        b.axvline(med, color=color, linewidth=1.4, linestyle=(0, (4, 2)))
        b.text(0.55, 17 if name == "peak" else 13.5, f"{name}: median {med:.3f} ps", color=color, fontsize=11)
    b.set_xlabel("decay time (ps)")
    b.set_ylabel("share of the region (%)")
    b.set_title("Apply: the median of each group", fontsize=12)
    style.save(fig, "viz_cleaning_regions")


FIGURES = {
    "viz_cleaning_dataframe": _dataframe,
    "viz_cleaning_tau_code": _tau_code,
    "viz_cleaning_missing_rows": _missing_rows,
    "viz_cleaning_outlier_rule": _outlier_rule,
    "viz_cleaning_regions": _regions,
}


if __name__ == "__main__":
    print(numbers())
