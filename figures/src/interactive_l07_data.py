"""Data of the interactive figures of Lecture 7 (Data Visualisation).

Writes lectures/content/public/data/l07_*.json, read at run time by the
components in lectures/content/components/:

- l07_hist.json     BinWidthExplorer: the hours at each tenth of a degree (the
                    station writes tenths), which the component adds up into
                    bins of 0.05 to 10 °C over -17 to 33 °C.
- l07_heatmap.json  PaletteHeatmap: the ten-year mean temperature of each day
                    of the year x hour of the day (beyond.py's day_hour_grid),
                    in tenths of a degree, and the four palettes sampled from
                    Matplotlib (viridis, jet, RdBu_r, gray), 256 colours each.
- l07_daily.json    SmoothingWindow: the daily means of 2024 and 2025, as in
                    associations.py's raw/smooth figure, to 0.01 °C.

AxisStartBars needs no file: its five pass rates are amounts.py's
PASS_RATES, written into the component as the default of its `values` prop
(checked below).

    python3 figures/src/interactive_l07_data.py

writes the files (deterministic: the same bytes on every run) and prints every
number the components show, formatted as the components format them
(JavaScript's toFixed: halves away from zero; a minus sign; never "-0.0").
"""
import json
import sys
from datetime import date, timedelta
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib as mpl  # noqa: E402

import amounts  # noqa: E402
import beyond  # noqa: E402
import handson  # noqa: E402
import style  # noqa: E402

OUT = style.ROOT / "lectures" / "content" / "public" / "data"

# BinWidthExplorer. Bins are counted in fortieths of a degree (0.025 °C), the
# unit in which every edge is a whole number: a tenth k is 4k, half a bin of
# 0.05 °C is 1. Bins of 0.05 and 0.1 °C are centred on the tenths (so a bin of
# 0.05 °C between two tenths stays empty); wider bins start at -17 °C, and a
# tenth on an edge belongs to the bin on its right, as in np.histogram.
WIDTHS = [0.05, 0.1, 0.5, 1, 2, 5, 10]     # °C, the stops of the slider
FULL = (-680, 1320)                         # -17 to 33 °C
ZOOM = (0, 80)                              # 0 to 2 °C; half a bin wider for centred bins
# AxisStartBars: the values written into the component.
BAR_VALUES = [58.2, 54.7, 51.9, 50.3, 49.1]
BAR_STARTS = [0, 10, 20, 30, 40, 45, 48]
# PaletteHeatmap: the palettes and the two scales (°C).
PALETTES = {"viridis": "viridis", "jet": "jet", "diverging": "RdBu_r", "greys": "gray"}
SEQ, DIV = (-10, 30), (-30, 30)
# SmoothingWindow: the years and the windows printed below.
YEARS = ("2024", "2025")
WINDOWS = [1, 7, 21, 61]


def fmt(x, nd):
    """x to nd decimals as JavaScript's toFixed prints it, with a minus sign."""
    d = Decimal(x).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)
    s = str(d.copy_abs() if d == 0 else d)
    return s.replace("-", "\u2212")


def deg(e):
    """A position in fortieths of a degree, with as many decimals as it needs."""
    nd = 0 if e % 40 == 0 else 1 if e % 4 == 0 else 2 if e % 2 == 0 else 3
    return fmt(Decimal(e) / 40, nd)


def dump(name, data):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    path.write_text(json.dumps(data, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"  + {path.relative_to(style.ROOT)} ({path.stat().st_size} bytes)")


# ---------------------------------------------------------------------------
# BinWidthExplorer
# ---------------------------------------------------------------------------

def hist_data():
    values = handson.temps(handson.PATH)
    ks = [round(v * 10) for v in values]
    assert all(abs(v * 10 - k) < 1e-9 for v, k in zip(values, ks)), "not tenths"
    k0, k1 = min(ks), max(ks)
    counts = [0] * (k1 - k0 + 1)
    for k in ks:
        counts[k - k0] += 1
    return {"hours": len(values), "mean": round(handson.mean(values), 4), "k0": k0, "counts": counts}


def bins_of(data, width):
    """(left edge, right edge, hours) of every bin, edges in fortieths."""
    w = round(width * 40)
    off = w // 2 if width <= 0.1 else 0
    n = (FULL[1] - FULL[0]) // w
    counts = [0] * n
    for i, c in enumerate(data["counts"]):
        j = (4 * (data["k0"] + i) - FULL[0] + off) // w
        if c and 0 <= j < n:
            counts[j] += c
    return [(FULL[0] - off + j * w, FULL[0] - off + (j + 1) * w, counts[j]) for j in range(n)]


def window_of(width, zoom):
    """The x range shown: -17 to 33 °C, or 0 to 2 °C with the centred bins of
    0 and 2 °C whole (half a bin wider on each side)."""
    if not zoom:
        return FULL
    off = round(width * 40) // 2 if width <= 0.1 else 0
    return (ZOOM[0] - off, ZOOM[1] + off)


def describe(bins, width, window):
    """The component's readout for the bins that overlap the window."""
    view = [b for b in bins if b[1] > window[0] and b[0] < window[1]]
    empty = sum(1 for b in view if b[2] == 0)
    full = view[0]
    for b in view:                      # the first of the fullest, left to right
        if b[2] > full[2]:
            full = b
    if width <= 0.1:
        where = f"{fmt(Decimal((full[0] + full[1]) // 2) / 40, 1)} °C"
    else:
        where = f"{deg(full[0])} to {deg(full[1])} °C"
    gaps = f", {empty} empty" if empty else ""
    return f"{len(view)} bin{'' if len(view) == 1 else 's'}{gaps} · fullest {where}: {full[2]} hours"


def report_hist(data):
    k1 = data["k0"] + len(data["counts"]) - 1
    print(f"\nBinWidthExplorer: {data['hours']} hours, mean {fmt(data['mean'], 2)} °C, "
          f"{deg(4 * data['k0'])} to {deg(4 * k1)} °C, "
          f"{sum(1 for c in data['counts'] if c)} different values")
    for zoom, name in ((False, "−17 to 33 °C"), (True, "0 to 2 °C")):
        for width in WIDTHS:
            bins = bins_of(data, width)
            assert sum(b[2] for b in bins) == data["hours"], width
            print(f"  {name}, {width:>4g} °C: {describe(bins, width, window_of(width, zoom))}")
    one = {b[0]: b[2] for b in bins_of(data, 1)}
    print(f"  bins of 1 °C: −1 to 0 °C {one[-40]} hours, 7 to 8 °C {one[280]}, "
          f"11 to 12 °C {one[440]}")


# ---------------------------------------------------------------------------
# AxisStartBars
# ---------------------------------------------------------------------------

def report_bars():
    assert BAR_VALUES == amounts.PASS_RATES, "AxisStartBars default differs from amounts.py"
    v = [round(x * 10) for x in BAR_VALUES]          # tenths of a per cent
    print(f"\nAxisStartBars: {', '.join(f'{s} {fmt(x, 1)} %' for s, x in zip(amounts.SCHOOLS, BAR_VALUES))}")
    for start in BAR_STARTS:
        a, e = v[0] - 10 * start, v[-1] - 10 * start
        print(f"  axis from {start:>2}: bars {fmt(Decimal(a) / 10, 1)} ÷ {fmt(Decimal(e) / 10, 1)}"
              f" = {fmt(Decimal(a) / e, 2)} times · values {fmt(BAR_VALUES[0], 1)} ÷ "
              f"{fmt(BAR_VALUES[-1], 1)} = {fmt(Decimal(v[0]) / v[-1], 2)} times")


# ---------------------------------------------------------------------------
# PaletteHeatmap
# ---------------------------------------------------------------------------

def palette_hex(name):
    cmap = mpl.colormaps[name].resampled(256)
    return "".join(mpl.colors.to_hex(cmap(i))[1:] for i in range(256))


def heatmap_data():
    days, grid = beyond.day_hour_grid()
    assert len(days) == 366 and grid.shape == (24, 366)
    assert not any(v != v for v in grid.flat), "an empty cell"
    cells = [round(float(grid[h, d]) * 10) for h in range(24) for d in range(366)]
    return {"days": days, "cells": cells, "seq": list(SEQ), "div": list(DIV),
            "palettes": {k: palette_hex(v) for k, v in PALETTES.items()}}


def cell_label(days, h, d):
    month, day = days[d].split("-")
    return f"{int(day)} {beyond.MONTHS[int(month) - 1]}, {h:02d}:00"


def report_heatmap(data):
    days, cells = data["days"], data["cells"]
    hi = max(range(len(cells)), key=lambda i: cells[i])
    lo = min(range(len(cells)), key=lambda i: cells[i])
    print(f"\nPaletteHeatmap: 24 hours x {len(days)} days, each cell a mean of ten years")
    print(f"  warmest cell {cell_label(days, hi // 366, hi % 366)}: {fmt(Decimal(cells[hi]) / 10, 1)} °C")
    print(f"  coldest cell {cell_label(days, lo // 366, lo % 366)}: {fmt(Decimal(cells[lo]) / 10, 1)} °C")
    print(f"  scales: viridis, jet, greys {fmt(SEQ[0], 0)} to {fmt(SEQ[1], 0)} °C; "
          f"diverging {fmt(DIV[0], 0)} to {fmt(DIV[1], 0)} °C")
    for day, h in [("01-15", 3), ("04-15", 12), ("07-28", 15), ("10-15", 9), ("02-29", 12)]:
        d = days.index(day)
        print(f"  {cell_label(days, h, d)}: {fmt(Decimal(cells[h * 366 + d]) / 10, 1)} °C")


# ---------------------------------------------------------------------------
# SmoothingWindow
# ---------------------------------------------------------------------------

def daily_data():
    groups = handson.group(handson.PATH, 0, 10)
    keys = [d for d in sorted(groups) if d[:4] in YEARS]
    first = date.fromisoformat(keys[0])
    assert keys == [(first + timedelta(i)).isoformat() for i in range(len(keys))], "a day is missing"
    return {"first": keys[0], "temps": [round(handson.mean(groups[d]), 2) for d in keys]}


def running(temps, window):
    """Centred running mean, partial windows at the two ends (pandas
    rolling(window, center=True, min_periods=1)), summed left to right as the
    component sums."""
    h = window // 2
    out = []
    for i in range(len(temps)):
        part = temps[max(0, i - h): i + h + 1]
        total = 0.0
        for t in part:
            total += t
        out.append(total / len(part))
    return out


def report_daily(data):
    first = date.fromisoformat(data["first"])
    temps = data["temps"]

    def day(i):
        d = first + timedelta(i)
        return f"{d.day} {beyond.MONTHS[d.month - 1]} {d.year}"

    print(f"\nSmoothingWindow: {len(temps)} days from {data['first']}")
    for w in WINDOWS:
        s = running(temps, w)
        lo = min(range(len(s)), key=lambda i: s[i])
        hi = max(range(len(s)), key=lambda i: s[i])
        print(f"  window {w:>2} days: lowest {fmt(s[lo], 1)} °C ({day(lo)}), "
              f"highest {fmt(s[hi], 1)} °C ({day(hi)})")
    try:
        import pandas as pd
    except ImportError:
        print("  (pandas not installed: the comparison with the course figure is skipped)")
        return
    ref = pd.Series(temps).rolling(21, center=True, min_periods=1).mean()
    assert max(abs(a - b) for a, b in zip(ref, running(temps, 21))) < 1e-9, "differs from pandas"
    print("  window 21 = pandas rolling(21, center=True, min_periods=1), the course figure")


def main():
    hist = hist_data()
    heat = heatmap_data()
    daily = daily_data()
    dump("l07_hist.json", hist)
    dump("l07_heatmap.json", heat)
    dump("l07_daily.json", daily)
    report_hist(hist)
    report_bars()
    report_heatmap(heat)
    report_daily(daily)


if __name__ == "__main__":
    main()
