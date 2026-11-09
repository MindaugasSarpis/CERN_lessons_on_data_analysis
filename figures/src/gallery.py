"""The classics of data visualisation, redrawn from their data: Lecture 7,
after the slide "Time as One More Variable: an Animation".

- `viz_gallery_minard`: Charles Joseph Minard's map of Napoleon's Russian
  campaign of 1812 (drawn 1869). The band's width is the number of soldiers,
  tan on the way to Moscow, light grey on the way back (Minard's black on
  a dark slide), over longitude and
  latitude; below, the temperature on the retreat with its dates. Six
  variables: size of the army, longitude, latitude, direction, temperature,
  date.
- `viz_gallery_nightingale`: Florence Nightingale's two polar-area diagrams
  (1858) of the deaths in the British army in the East, April 1854 to March
  1856. Each month is a wedge of 30 degrees; the area of each coloured wedge,
  measured from the centre, is the number of deaths from preventable
  disease, wounds or other causes (radius = sqrt(deaths)), the three drawn
  over each other, the largest behind.
- `viz_gallery_cern`: CERN's accelerator chain drawn to scale (left: the
  rings as circles of their true circumference, at their approximate places)
  and as a schematic (right: the order of the machines and where the four
  experiments sit on the LHC, nothing else).

Pure vector: patches, lines and text (as outlines); no images.
Data in figures/data/gallery/ (sources and licences in its README.md).

    python figures/src/gallery.py

prints every number the slides state.
"""
import csv
import math
from datetime import date, timedelta
from pathlib import Path

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (Circle, ConnectionPatch, FancyArrowPatch,
                                Polygon, RegularPolygon, Wedge)

import style

RAW = Path(__file__).resolve().parents[1] / "data" / "gallery"
SIZE = (9.41, 3.56)
BG = style.BG                       # the slide background, for gaps and halos


def _rows(name):
    with open(RAW / name, newline="") as f:
        return list(csv.DictReader(f))


def _fig(name, layout="none"):
    return plt.figure(figsize=style.SIZES.get(name, SIZE), layout=layout)


def _num(n):
    """422000 -> '422 000' (a thin space, as the slides write numbers)."""
    return f"{n:,}".replace(",", " ")


# ---------------------------------------------------------------------------
# 1. Minard: Napoleon's army in Russia, 1812
# ---------------------------------------------------------------------------

TAN = "#d9b77e"                     # Minard's tan: the advance
RETREAT = "#c3ccd8"                 # the retreat: Minard's black, light on a dark slide
SLIDE_BG = "#050507"                # the theme's --bg, for the thin label halos
LON, LAT = (22.55, 38.45), (53.72, 56.16)
MAP_RECT = [0.05, 0.355, 0.94, 0.635]      # figure fractions
TEMP_RECT = [0.05, 0.095, 0.94, 0.20]
BAND = 0.42 / 340_000               # inches of band per soldier
MONTH_NO = {"Oct": 10, "Nov": 11, "Dec": 12}

# City labels: offset in points and alignment (default: above the dot).
CITY_LABEL = {
    "Kowno": (-5, 0, "right", "center"),
    "Wilna": (8, 21, "center", "bottom"),
    "Smorgoni": (-3, -5, "right", "top"),
    "Moiodexno": (6, -6, "center", "top"),
    "Gloubokoe": (0, 5, "center", "bottom"),
    "Minsk": (0, -5, "center", "top"),
    "Studienska": (-6, -15, "center", "top"),
    "Polotzk": (0, 6, "center", "bottom"),
    "Bobr": (5, 4, "left", "bottom"),
    "Witebsk": (0, 10, "center", "bottom"),
    "Orscha": (0, 5, "center", "bottom"),
    "Mohilow": (0, -5, "center", "top"),
    "Smolensk": (0, -19, "center", "top"),
    "Dorogobouge": (-3, 8, "right", "bottom"),
    "Wixma": (4, -5, "left", "top"),
    "Chjat": (0, 8, "center", "bottom"),
    "Mojaisk": (0, 8, "center", "bottom"),
    "Moscou": (-3, 6, "right", "bottom"),
    "Tarantino": (6, 3, "center", "bottom"),
    "Malo-Jarosewii": (0, -6, "center", "top"),
}
HALO = [pe.withStroke(linewidth=1.6, foreground=SLIDE_BG)]

# Temperature labels: offset in points and alignment (default: below).
TEMP_LABEL = {
    25.3: (-4, -2, "right", "top"),
    26.7: (0, -6, "center", "top"),
    27.2: (5, -2, "left", "top"),
}


def minard_paths():
    """[((group, direction), [(lon, lat, survivors), ...])] in file order."""
    paths = []
    for r in _rows("Minard.troops.csv"):
        key = (int(r["group"]), r["direction"])
        pt = (float(r["long"]), float(r["lat"]), int(r["survivors"]))
        if paths and paths[-1][0] == key:
            paths[-1][1].append(pt)
        else:
            paths.append((key, [pt]))
    return paths


def minard_cities():
    return [(float(r["long"]), float(r["lat"]), r["city"]) for r in _rows("Minard.cities.csv")]


def minard_temps():
    """[(lon, temperature in degrees Reaumur, date)] along the retreat.

    The column days is the number of days since the reading before; it gives
    the date of the one row without one (14 November + 10 days), and it is
    checked against every row that has a date."""
    out = []
    for r in _rows("Minard.temp.csv"):
        given = date(1812, MONTH_NO[r["date"][:3]], int(r["date"][3:])) if r["date"] else None
        derived = out[-1][2] + timedelta(days=int(r["days"])) if out else None
        if given and derived:
            assert given == derived, (given, derived)
        out.append((float(r["long"]), int(float(r["temp"])), given or derived))
    return out


def _band(pts, kx, ky):
    """The band along pts [(x, y, n)] as one polygon in data coordinates.

    The width on the page is n * BAND inches, n of the segment's first point;
    each joint is cut along the bisector of its turn, so the band steps where
    the number changes and has no gap or overlap where it turns. Built in
    inches (kx, ky: inches per degree), so the width does not depend on the
    direction of the segment."""
    pts = [p for i, p in enumerate(pts) if i == 0 or p[:2] != pts[i - 1][:2]]
    P = np.array([(x * kx, y * ky) for x, y, _ in pts])
    w = np.array([n for *_, n in pts], float) * BAND
    d = np.diff(P, axis=0)
    d /= np.hypot(*d.T)[:, None]
    nrm = np.column_stack([-d[:, 1], d[:, 0]])
    left, right = [], []
    for i in range(len(d)):
        for j in (i, i + 1):
            m = nrm[i]
            if 0 < j < len(P) - 1:
                s = nrm[j - 1] + nrm[j]
                if np.hypot(*s) > 1e-6:
                    m = s / np.hypot(*s)
            off = m * w[i] / 2 / max(m @ nrm[i], 0.3)
            left.append(P[j] + off)
            right.append(P[j] - off)
    poly = np.array(left + right[::-1])
    return np.column_stack([poly[:, 0] / kx, poly[:, 1] / ky])


def _retreat_lat(lon):
    """Latitude of the main retreat (group 1) at a longitude."""
    pts = [p for (g, dn), ps in minard_paths() if (g, dn) == (1, "R") for p in ps]
    xs = [p[0] for p in pts][::-1]
    ys = [p[1] for p in pts][::-1]
    return float(np.interp(lon, xs, ys))


def _minard():
    name = "viz_gallery_minard"
    fig = _fig(name)
    fw, fh = fig.get_size_inches()
    ax = fig.add_axes(MAP_RECT)
    at = fig.add_axes(TEMP_RECT, sharex=ax)
    kx = MAP_RECT[2] * fw / (LON[1] - LON[0])
    ky = MAP_RECT[3] * fh / (LAT[1] - LAT[0])

    paths = minard_paths()
    for direction, face, edge, lw in (("A", TAN, TAN, 0.3), ("R", RETREAT, RETREAT, 0.3)):
        for (g, dn), pts in paths:
            if dn == direction:
                ax.add_patch(Polygon(_band(pts, kx, ky), closed=True, facecolor=face,
                                     edgecolor=edge, linewidth=lw, joinstyle="miter", zorder=3))

    for lon, lat, city in minard_cities():
        dx, dy, ha, va = CITY_LABEL.get(city, (0, 6, "center", "bottom"))
        ax.plot(lon, lat, "o", ms=2.6, color=style.FG, mec=BG, mew=0.5, zorder=5)
        ax.annotate(city, (lon, lat), xytext=(dx, dy), textcoords="offset points",
                    ha=ha, va=va, fontsize=8.5, color=style.FG, zorder=6, path_effects=HALO)

    start = sum(pts[0][2] for (g, dn), pts in paths if dn == "A")
    moscow = max(pts[-1][2] for (g, dn), pts in paths if dn == "A")
    end = sum(pts[-1][2] for (g, dn), pts in paths if dn == "R" and pts[-1][0] < 24.5)
    ax.text(22.62, 55.3, f"{_num(start)}\nsoldiers", color=TAN, fontsize=10.5,
            ha="left", va="bottom", linespacing=1.0)
    ax.text(36.45, 55.87, f"{_num(moscow)} reach Moscow", color=TAN, fontsize=10.5,
            ha="right", va="center", path_effects=HALO)
    ax.text(22.62, 54.25, f"{_num(end)}\nreturn", color=RETREAT, fontsize=10.5,
            ha="left", va="top", linespacing=1.0)
    ax.text(31.55, 55.27, "to Moscow", color=TAN, fontsize=10, ha="left", va="bottom")
    ax.text(31.3, 54.38, "back", color=RETREAT, fontsize=10, ha="center", va="top")

    ax.set_xlim(LON)
    ax.set_ylim(LAT)
    ax.set_yticks([54, 55, 56], ["54°N", "55°N", "56°N"])
    ax.tick_params(labelbottom=False, length=0, labelsize=8.5)
    for s in ax.spines.values():
        s.set_visible(False)

    temps = minard_temps()
    xs = [t[0] for t in temps]
    ys = [t[1] for t in temps]
    at.plot(xs, ys, color=style.FG, linewidth=1.4, zorder=3)
    at.plot(xs, ys, "o", ms=3.2, color=style.FG, mec=BG, mew=0.6, zorder=4)
    for lon, t, day in temps:
        dx, dy, ha, va = TEMP_LABEL.get(lon, (0, -5, "center", "top"))
        label = f"{t}°".replace("-", "−") + f"\n{day.day} {day:%b}"
        at.annotate(label, (lon, t), xytext=(dx, dy), textcoords="offset points",
                    ha=ha, va=va, fontsize=8, color=style.FG, linespacing=1.05, zorder=5)
        fig.add_artist(ConnectionPatch(xyA=(lon, t), coordsA=at.transData,
                                       xyB=(lon, _retreat_lat(lon)), coordsB=ax.transData,
                                       color=style.DIM, linewidth=0.6, alpha=0.8, zorder=1))
    at.set_ylim(-46, 6)
    at.set_yticks([0, -15, -30], ["0°", "−15°", "−30°"])
    at.set_xticks(range(24, 39, 2), [f"{x}°E" for x in range(24, 39, 2)])
    at.tick_params(length=0, labelsize=8.5)
    at.text(22.62, 3.0, "temperature on the retreat, degrees Réaumur (× 1.25 = °C)",
            color=style.DIM, fontsize=8.5, ha="left", va="center", path_effects=HALO,
            zorder=6)
    for s in at.spines.values():
        s.set_visible(False)
    style.save(fig, name, tight=False)


# ---------------------------------------------------------------------------
# 2. Nightingale: the causes of death in the army in the East, 1854-56
# ---------------------------------------------------------------------------

CAUSES = [  # column, label, colour (her blue, red and black)
    ("Disease", "preventable disease", "#7fb8e6"),
    ("Wounds", "wounds", "#ef6a5f"),
    ("Other", "other causes", "#8a94a3"),
]
R_MAX = 1.62                        # inches: the radius of the largest wedge
ROSE_1 = (6.85, 1.9)                # April 1854 - March 1855, on the right ...
ROSE_2 = (2.25, 1.92)               # ... and the second year on the left, as hers


def nightingale():
    return _rows("Nightingale.csv")


def _wedge_angles(m):
    """Month m (0 = April) runs clockwise from nine o'clock, 30 degrees each."""
    return 180 - 30 * (m + 1), 180 - 30 * m


def _rose(ax, centre, months, k):
    cx, cy = centre
    for m, row in enumerate(months):
        a0, a1 = _wedge_angles(m)
        layers = sorted(((int(row[c]), col) for c, _, col in CAUSES), reverse=True)
        for n, col in layers:
            if n:
                ax.add_patch(Wedge(centre, k * math.sqrt(n), a0, a1, facecolor=col,
                                   edgecolor=BG, linewidth=0.7, zorder=2))
        top = k * math.sqrt(layers[0][0])
        mid = math.radians((a0 + a1) / 2)
        r = max(top, 0.45) + 0.09
        c, s = math.cos(mid), math.sin(mid)
        ha = "left" if c > 0.2 else "right" if c < -0.2 else "center"
        va = "bottom" if s > 0.3 else "top" if s < -0.3 else "center"
        ax.text(cx + r * c, cy + r * s, row["Month"], ha=ha, va=va, fontsize=8.5,
                color=style.DIM, zorder=4)


def _nightingale():
    name = "viz_gallery_nightingale"
    fig = _fig(name)
    fw, fh = fig.get_size_inches()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, fw), ylim=(0, fh))
    ax.axis("off")
    rows = nightingale()
    k = R_MAX / math.sqrt(max(int(r["Disease"]) for r in rows))
    _rose(ax, ROSE_1, rows[:12], k)
    _rose(ax, ROSE_2, rows[12:], k)
    ax.text(ROSE_1[0] - 0.25, fh - 0.12, "1   April 1854 – March 1855", ha="center", va="top",
            fontsize=11.5, color=style.FG)
    ax.text(ROSE_2[0], fh - 0.12, "2   April 1855 – March 1856", ha="center", va="top",
            fontsize=11.5, color=style.FG)

    # Direct labels, each a thin line in its label's colour: disease touches
    # the outer edge of February 1855 (a blue line inside blue would vanish),
    # other causes ends on the grey ring of the same wedge.
    feb = rows[10]
    a0, a1 = _wedge_angles(10)
    mid = math.radians((a0 + a1) / 2)
    radii = sorted(k * math.sqrt(int(feb[c])) for c, _, _ in CAUSES)   # wounds, other, disease
    inner = {"Wounds": radii[0] / 2, "Other": (radii[0] + radii[1]) / 2,
             "Disease": (radii[1] + radii[2]) / 2}
    # Wounds point into November 1854 instead, the largest red ring.
    nov = rows[7]
    a0n, a1n = _wedge_angles(7)
    r_nov = sorted(k * math.sqrt(int(nov[c])) for c, _, _ in CAUSES)
    renderer = fig.canvas.get_renderer()
    for (col, label, colour), (tx, ty) in zip(CAUSES, ((4.3, 0.55), (7.85, 0.6), (4.3, 1.3))):
        t = ax.text(tx, ty, label, ha="left", va="center", fontsize=10.5, color=colour,
                    zorder=6)
        bb = t.get_window_extent(renderer).transformed(ax.transData.inverted())
        if col == "Wounds":
            ang, r = math.radians((a0n + a1n) / 2), (r_nov[0] + r_nov[1]) / 2
            x1 = bb.x0 - 0.12
        elif col == "Disease":
            ang, r = math.radians(-125), radii[2] - 0.01
            x1 = bb.x1
        else:
            ang, r = mid, inner[col]
            x1 = bb.x1
        px, py = ROSE_1[0] + r * math.cos(ang), ROSE_1[1] + r * math.sin(ang)
        ax.plot([x1 + 0.06, px], [ty, py], color=colour, lw=1.0, zorder=5,
                solid_capstyle="round")
        if col != "Disease":
            ax.plot(px, py, "o", ms=3.2, color=colour, mec=BG, mew=0.8, zorder=6)

    top = rows[9]
    a0, a1 = _wedge_angles(9)
    mid = math.radians((a0 + a1) / 2)
    r = 0.78 * k * math.sqrt(int(top["Disease"]))
    ax.text(ROSE_1[0] + r * math.cos(mid), ROSE_1[1] + r * math.sin(mid), top["Disease"],
            ha="center", va="center", fontsize=10, color=BG, zorder=6)
    ax.text(0.12, 0.2, "area = deaths, each wedge measured from the centre",
            ha="left", va="center", fontsize=8.5, color=style.DIM)
    style.save(fig, name, tight=False)


# ---------------------------------------------------------------------------
# 3. CERN's accelerators: to scale and as a schematic
# ---------------------------------------------------------------------------

# Circumferences in metres (sources in the speaker note): LHC and PS from
# home.cern, the SPS (11 x the PS) and the Booster (4 rings, each 1/4 of the
# PS) from CERN's own course "CERN's accelerator complex" (R. Steerenberg,
# 27 Feb 2023); Linac4 is 86 m long (home.cern).
MACHINES = [  # name, label, circumference or length (m), colour
    ("Linac4", "Linac4", 86, "#a3acfb"),
    ("PSB", "Booster", 157, "#e88bc4"),
    ("PS", "PS", 628, "#66d9ab"),
    ("SPS", "SPS", 6900, "#f5b95f"),
    ("LHC", "LHC", 26659, "#7dd3fc"),
]
COLOUR = {m[0]: m[3] for m in MACHINES}
SIZE_M = {m[0]: m[2] for m in MACHINES}

# Approximate places in km, x east and y north of the LHC's centre (the
# midpoint of ATLAS and CMS, which face each other across the ring). The
# experiments from their published coordinates; the SPS and the Meyrin site
# (PS, Booster, Linac4) estimated from maps: good to a few hundred metres.
EXPERIMENTS = {"ATLAS": (-0.83, -4.11), "ALICE": (-3.54, -2.35),
               "CMS": (0.83, 4.11), "LHCb": (2.37, -3.49)}
SPS_C = (-0.16, -2.89)
PS_C = (-1.55, -4.28)
PSB_C = (-1.70, -4.18)
LINAC4 = ((-1.90, -4.25), (-1.78, -4.20))


def _fmt_size(m):
    return f"{m / 1000:.1f} km" if m >= 1000 else f"{m} m"


def _to_scale(ax, w_in, h_in):
    r_lhc = SIZE_M["LHC"] / 1000 / (2 * math.pi)
    km_per_in = 10.9 / h_in
    xc, yc = 0.35, -0.2
    ax.set(xlim=(xc - w_in / 2 * km_per_in, xc + w_in / 2 * km_per_in),
           ylim=(yc - h_in / 2 * km_per_in, yc + h_in / 2 * km_per_in))
    ax.axis("off")
    ax.add_patch(Circle((0, 0), r_lhc, fill=False, ec=COLOUR["LHC"], lw=2.4))
    ax.add_patch(Circle(SPS_C, SIZE_M["SPS"] / 1000 / (2 * math.pi), fill=False,
                        ec=COLOUR["SPS"], lw=2.0))
    ax.add_patch(Circle(PS_C, SIZE_M["PS"] / 1000 / (2 * math.pi), fill=False,
                        ec=COLOUR["PS"], lw=1.0))
    ax.add_patch(Circle(PSB_C, SIZE_M["PSB"] / 1000 / (2 * math.pi), fill=False,
                        ec=COLOUR["PSB"], lw=0.6))
    ax.plot(*zip(*LINAC4), color=COLOUR["Linac4"], lw=1.0, solid_capstyle="butt")
    for exp, (x, y) in EXPERIMENTS.items():
        a = math.atan2(y, x)
        px, py = r_lhc * math.cos(a), r_lhc * math.sin(a)
        ax.plot(px, py, "o", ms=5.5, color=style.FG, mec=BG, mew=1.0, zorder=5)
        out = r_lhc + 0.42
        c, s = math.cos(a), math.sin(a)
        ha = "left" if c > 0.35 else "right" if c < -0.35 else "center"
        va = "bottom" if s > 0.7 else "top" if s < -0.9 else "center"
        if exp == "ATLAS":
            ha, out = "left", r_lhc + 0.3
        ax.text(out * c, out * s, exp, ha=ha, va=va, fontsize=10, color=style.FG, zorder=6)
    a = math.radians(128)
    ax.text((r_lhc + 0.3) * math.cos(a), (r_lhc + 0.3) * math.sin(a),
            f"LHC  {_fmt_size(SIZE_M['LHC'])}", ha="right", va="bottom", fontsize=11,
            color=COLOUR["LHC"])
    ax.text(SPS_C[0], SPS_C[1] + 1.32, f"SPS  {_fmt_size(SIZE_M['SPS'])}", ha="center",
            va="bottom", fontsize=11, color=COLOUR["SPS"])
    # The three smallest machines: one label, pointing at the spot.
    tx, ty = -6.0, -5.25
    for i, key in enumerate(("PS", "PSB", "Linac4")):
        label = dict((m[0], m[1]) for m in MACHINES)[key]
        ax.text(tx, ty + 0.62 * (2 - i), f"{label}  {_fmt_size(SIZE_M[key])}", ha="left",
                va="center", fontsize=10, color=COLOUR[key])
    ax.annotate("", xy=(PS_C[0] - 0.12, PS_C[1] - 0.1), xytext=(tx + 2.35, ty + 1.24),
                arrowprops=dict(arrowstyle="-", color=style.DIM, lw=0.8, shrinkA=0, shrinkB=2))
    # Scale bar: 2 km.
    x0, y0 = 3.2, -5.45
    ax.plot([x0, x0 + 2], [y0, y0], color=style.FG, lw=1.6, solid_capstyle="butt")
    for x in (x0, x0 + 2):
        ax.plot([x, x], [y0 - 0.1, y0 + 0.1], color=style.FG, lw=1.2)
    ax.text(x0 + 1, y0 + 0.18, "2 km", ha="center", va="bottom", fontsize=9.5, color=style.FG)


def _arrow(ax, a, b, colour=style.DIM):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=11, lw=1.6,
                                 color=colour, shrinkA=0, shrinkB=0, zorder=3,
                                 joinstyle="miter"))


def _schematic(ax, w_in, h_in):
    """The chain top to bottom on the left; from the SPS one line runs under
    the LHC and branches at 45 degrees into Point 2 (ALICE) and Point 8
    (LHCb), where the two beams are injected."""
    ax.set(xlim=(0, w_in), ylim=(0, h_in))
    ax.axis("off")
    cx, cy, R = 3.38, 1.98, 1.05
    apo = R * math.cos(math.pi / 8)
    ax.add_patch(RegularPolygon((cx, cy), 8, radius=R, orientation=math.pi / 8,
                                fill=False, ec=COLOUR["LHC"], lw=3.2, joinstyle="miter",
                                zorder=2))
    point = {k: (cx + apo * math.cos(math.radians(t)), cy + apo * math.sin(math.radians(t)))
             for k, t in ((1, -90), (2, -135), (5, 90), (8, -45))}
    ax.text(cx, cy + 0.07, "LHC", ha="center", va="bottom", fontsize=12,
            color=COLOUR["LHC"])
    ax.text(cx, cy - 0.03, _fmt_size(SIZE_M["LHC"]), ha="center", va="top",
            fontsize=9.5, color=style.DIM)

    x0, ys = 0.42, {"Linac4": 2.88, "PSB": 2.2, "PS": 1.52, "SPS": 0.72}
    trunk = ys["SPS"]
    for a, b in (("Linac4", "PSB"), ("PSB", "PS"), ("PS", "SPS")):
        _arrow(ax, (x0, ys[a] - 0.16), (x0, ys[b] + 0.16))
    feet = {p: (point[p][0] + s * (point[p][1] - trunk), trunk) for p, s in ((2, -1), (8, 1))}
    ax.plot([x0 + 0.16, feet[8][0]], [trunk, trunk], color=style.DIM, lw=1.6, zorder=3,
            solid_capstyle="butt")
    for p, s in ((2, -1), (8, 1)):
        px, py = point[p]
        _arrow(ax, feet[p], (px + s * 0.07, py - 0.07))
    for key, label, size, colour in MACHINES[:4]:
        y = ys[key]
        if key == "Linac4":
            ax.plot([x0 - 0.14, x0 + 0.14], [y, y], color=colour, lw=7,
                    solid_capstyle="round", zorder=5)
        else:
            ax.add_patch(Circle((x0, y), 0.13, facecolor=BG, edgecolor=colour, lw=2.4,
                                zorder=5))
        ty = y if key != "SPS" else y - 0.27
        t = ax.text(x0 + 0.27, ty, label, ha="left", va="center", fontsize=10.5, color=colour)
        x1 = t.get_window_extent(ax.figure.canvas.get_renderer()).transformed(
            ax.transData.inverted()).x1
        ax.text(x1 + 0.1, ty, _fmt_size(size), ha="left", va="center", fontsize=9.5,
                color=style.DIM)
    for p, exp, (dx, dy, ha, va) in ((1, "ATLAS", (0, 0.16, "center", "bottom")),
                                     (2, "ALICE", (-0.16, 0, "right", "center")),
                                     (5, "CMS", (0, 0.16, "center", "bottom")),
                                     (8, "LHCb", (0.16, 0, "left", "center"))):
        px, py = point[p]
        ax.add_patch(Circle((px, py), 0.085, facecolor=style.FG, edgecolor=BG, lw=1.5,
                            zorder=6))
        ax.text(px + dx, py + dy, exp, ha=ha, va=va, fontsize=10, color=style.FG, zorder=6)


def _cern():
    name = "viz_gallery_cern"
    fig = _fig(name)
    fw, fh = fig.get_size_inches()
    split = 4.55                                       # inches: the left panel's width
    left = fig.add_axes([0, 0, split / fw, 1])
    right = fig.add_axes([split / fw, 0, 1 - split / fw, 1])
    _to_scale(left, split, fh)
    _schematic(right, fw - split, fh)
    for ax, title in ((left, "To scale"), (right, "As a schematic")):
        ax.text(0.02, 0.985, title, transform=ax.transAxes, ha="left", va="top",
                fontsize=12.5, color=style.FG)
    left.text(0.98, 0.985, "places approximate", transform=left.transAxes, ha="right",
              va="top", fontsize=8.5, color=style.DIM)
    fig.add_artist(plt.Line2D([split / fw] * 2, [0.05, 0.95], color=style.GRID, lw=1.0))
    style.save(fig, name, tight=False)


FIGURES = {
    "viz_gallery_minard": _minard,
    "viz_gallery_nightingale": _nightingale,
    "viz_gallery_cern": _cern,
}


# ---------------------------------------------------------------------------
# Every number a slide might state
# ---------------------------------------------------------------------------

def _report():
    paths = minard_paths()
    print("1. Minard")
    for (g, dn), pts in paths:
        print(f"  group {g} {dn}: {len(pts)} points, lon {pts[0][0]} -> {pts[-1][0]}, "
              f"survivors {pts[0][2]} -> {pts[-1][2]}")
    start = sum(pts[0][2] for (g, dn), pts in paths if dn == "A")
    moscow = max(pts[-1][2] for (g, dn), pts in paths if dn == "A")
    end = sum(pts[-1][2] for (g, dn), pts in paths if dn == "R" and pts[-1][0] < 24.5)
    print(f"  start (three groups at Kowno) {start}; at Moscow {moscow}; back at the Niemen "
          f"{end} = {end / start:.1%} of the start ({start / end:.0f} to 1)")
    lost = [(pts[i][2] - pts[i + 1][2], pts[i][0], pts[i + 1][0])
            for (g, dn), pts in paths if (g, dn) == (1, "R") for i in range(len(pts) - 1)]
    big = max(lost)
    print(f"  largest drop on the retreat: {big[0]} between lon {big[1]} and {big[2]}")
    print(f"  cities: {len(minard_cities())}")
    for lon, t, day in minard_temps():
        print(f"  {day:%d %b}: {t} °R = {t * 1.25:.1f} °C at lon {lon}")
    print(f"  bands: {BAND * 340_000:.2f} in for 340 000 soldiers; "
          f"4000 soldiers = {BAND * 4000 * 72:.2f} pt")

    rows = nightingale()
    print("2. Nightingale")
    for label, part in (("April 1854 - March 1855", rows[:12]), ("April 1855 - March 1856", rows[12:])):
        tot = {c: sum(int(r[c]) for r in part) for c, _, _ in CAUSES}
        allc = sum(tot.values())
        print(f"  {label}: {allc} deaths; " + ", ".join(
            f"{c} {tot[c]} ({tot[c] / allc:.1%})" for c in tot)
              + f"; army {part[0]['Army']} -> {part[-1]['Army']}")
    tot = {c: sum(int(r[c]) for r in rows) for c, _, _ in CAUSES}
    allc = sum(tot.values())
    print(f"  both years: {allc} deaths; disease {tot['Disease']} ({tot['Disease'] / allc:.1%}), "
          f"wounds {tot['Wounds']} ({tot['Wounds'] / allc:.1%}), other {tot['Other']}")
    top = max(rows, key=lambda r: int(r["Disease"]))
    print(f"  most deaths from disease: {top['Month']} {top['Year']}: {top['Disease']} "
          f"(wounds {top['Wounds']}, other {top['Other']}, army {top['Army']}, "
          f"rate {top['Disease.rate']} per 1000 per year)")
    topw = max(rows, key=lambda r: int(r["Wounds"]))
    print(f"  most deaths from wounds: {topw['Month']} {topw['Year']}: {topw['Wounds']}")
    for r in (rows[9], rows[21]):
        print(f"  {r['Month']} {r['Year']}: disease {r['Disease']}, wounds {r['Wounds']}, "
              f"other {r['Other']}, army {r['Army']}")
    k = R_MAX / math.sqrt(int(top["Disease"]))
    print(f"  radius scale: {k:.4f} in per sqrt(death); smallest wedge drawn: "
          f"{min(int(r[c]) for r in rows for c, _, _ in CAUSES if int(r[c]) > 0)} death(s)")

    print("3. CERN (circumference or length, m)")
    for key, label, m, _ in MACHINES:
        r = m / (2 * math.pi)
        print(f"  {label}: {m} m" + ("" if key == "Linac4" else f", radius {r:.0f} m")
              + f", {SIZE_M['LHC'] / m:.0f} x shorter than the LHC")
    print(f"  SPS / PS = {6900 / 628:.1f} (11 by design); PS / Booster = {628 / 157:.1f}")
    km_per_in = 10.9 / SIZE[1]
    px_per_in = 1280 / SIZE[0] * 0.92
    for key in ("PS", "PSB", "Linac4"):
        size_km = (SIZE_M[key] / math.pi if key != "Linac4" else SIZE_M[key]) / 1000
        print(f"  {key} on the left panel: {size_km / km_per_in * px_per_in:.1f} px across "
              f"on a 1280 px wide screen")
    for exp, (x, y) in EXPERIMENTS.items():
        print(f"  {exp}: {math.hypot(x, y):.2f} km from the centre, "
              f"angle {math.degrees(math.atan2(y, x)):.0f}°")


if __name__ == "__main__":
    _report()
