"""Good-and-bad family: four mistakes of lecture 07, each drawn twice from the
weather station's hourly log, `lectures/workbook/docs/data/weather.csv` -
once as it is often done, once as it should be.

- two y-axes against two panels: monthly mean temperature and humidity;
- a line through missing data against a gap: 19 to 29 July 2019, around the
  120 hours the temperature sensor did not record;
- a window chosen for its story against the whole series: the yearly means;
- ten overlapping lines against one in colour: the daily means of each year.

The data are read with the lecture's `weather.py` functions (handson.py).
Run directly to print every number the slides state.
"""
from datetime import datetime

import matplotlib.pyplot as plt

import style
from handson import PATH, MISSING, group, hours, mean, read_lines, temp_of

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _monthly(column):
    """The mean of a column (1 temperature, 2 humidity) for each month,
    over the hours with a measured temperature."""
    sums, counts = {}, {}
    for line in read_lines(PATH):
        if temp_of(line) == MISSING:
            continue
        key = line[5:7]
        value = float(line.split(",")[column])
        sums[key] = sums.get(key, 0.0) + value
        counts[key] = counts.get(key, 0) + 1
    return [sums[k] / counts[k] for k in sorted(sums)]


# ---------------------------------------------------------------------------
# Two y-axes against two panels
# ---------------------------------------------------------------------------

def _two_axes_bad():
    temp, hum = _monthly(1), _monthly(2)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(MONTHS, temp, "o-", color=style.ACCENT)
    ax.set_ylabel("temperature (°C)", color=style.ACCENT)
    ax2 = ax.twinx()
    ax2.plot(MONTHS, hum, "o-", color=style.CYCLE[1])
    ax2.set_ylabel("humidity (%)", color=style.CYCLE[1])
    ax2.set_ylim(68, 90)
    ax2.grid(False)
    ax.set_xticks(MONTHS[::2])
    ax.set_title("Temperature and Humidity by Month", color=style.BAD)
    style.save(fig, "viz_goodbad_two_axes_bad")


def _two_axes_good():
    temp, hum = _monthly(1), _monthly(2)
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(6, 4), sharex=True)
    top.plot(MONTHS, temp, "o-", color=style.ACCENT)
    top.set_ylabel("temperature\n(°C)")
    bottom.plot(MONTHS, hum, "o-", color=style.CYCLE[1])
    bottom.set_ylabel("humidity\n(%)")
    bottom.set_xticks(MONTHS[::2])
    top.set_title("Humid when cold: 87 % in January, 72 % in July")
    style.save(fig, "viz_goodbad_two_axes_good")


# ---------------------------------------------------------------------------
# A line through missing data against a gap
# ---------------------------------------------------------------------------

START, STOP = "2019-07-19T00:00", "2019-07-29T00:00"


def _july_2019(with_gap):
    times, values = [], []
    for line in read_lines(PATH):
        if not START <= line[0:16] < STOP:
            continue
        temp = temp_of(line)
        if temp == MISSING:
            if not with_gap:
                continue
            temp = float("nan")  # Matplotlib leaves a gap at a NaN
        times.append(datetime.fromisoformat(line[0:16]))
        values.append(temp)
    return times, values


def _gap_axes(ax):
    ax.set_ylabel("temperature (°C)")
    ax.set_ylim(8, 34)
    ax.set_xticks([datetime(2019, 7, d) for d in (19, 22, 25, 28)],
                  ["19 Jul", "22 Jul", "25 Jul", "28 Jul"])


def _gap_bad():
    times, values = _july_2019(with_gap=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(times, values, color=style.ACCENT, lw=1.2)
    _gap_axes(ax)
    ax.set_title("Hourly Temperature, July 2019", color=style.BAD)
    style.save(fig, "viz_goodbad_gap_bad")


def _gap_good():
    times, values = _july_2019(with_gap=True)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axvspan(datetime(2019, 7, 22), datetime(2019, 7, 27),
               color=style.DIM, alpha=0.18, lw=0)
    ax.text(datetime(2019, 7, 24, 12), 31, "not measured:\n120 hours",
            ha="center", va="top", color=style.FG)
    ax.plot(times, values, color=style.ACCENT, lw=1.2)
    _gap_axes(ax)
    ax.set_title("Five days of July 2019 were not measured")
    style.save(fig, "viz_goodbad_gap_good")


# ---------------------------------------------------------------------------
# A window chosen for its story against the whole series
# ---------------------------------------------------------------------------

def _yearly():
    years = group(PATH, 0, 4)
    return [int(y) for y in years], [mean(years[y]) for y in years]


def _window_bad():
    years, means = _yearly()
    i, j = years.index(2017), years.index(2023)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(years[i:j + 1], means[i:j + 1], "o-", color=style.BAD)
    ax.plot([years[i], years[j]], [means[i], means[j]], "--", color=style.FG, lw=1)
    ax.set_ylim(6.4, 8.4)
    ax.set_ylabel("mean temperature (°C)")
    ax.set_title(f"+{means[j] - means[i]:.1f} °C in six years", color=style.BAD)
    style.save(fig, "viz_goodbad_window_bad")


def _window_good():
    years, means = _yearly()
    all_hours = mean([v for v in _all_temps()])
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axhline(all_hours, color=style.CYCLE[1], lw=1.4)
    ax.plot(years, means, "o", color=style.ACCENT)
    ax.set_ylim(5, 9)
    ax.set_ylabel("mean temperature (°C)")
    ax.set_title("Ten years around 7.16 °C: no trend to read")
    style.save(fig, "viz_goodbad_window_good")


def _all_temps():
    _, values = hours(PATH)
    return values


# ---------------------------------------------------------------------------
# Ten overlapping lines against one in colour
# ---------------------------------------------------------------------------

def _daily_by_year():
    """{year: (day of the year, daily mean)} for every measured day."""
    days = group(PATH, 0, 10)
    out = {}
    for day, values in days.items():
        doy = datetime.fromisoformat(day).timetuple().tm_yday
        out.setdefault(day[0:4], ([], []))
        out[day[0:4]][0].append(doy)
        out[day[0:4]][1].append(mean(values))
    return out


def _spaghetti_bad():
    data = _daily_by_year()
    fig, ax = plt.subplots(figsize=(6, 4))
    for k, (year, (doy, dm)) in enumerate(data.items()):
        ax.plot(doy, dm, lw=0.8, color=plt.cm.rainbow(k / 9), label=year)
    ax.legend(ncol=2, fontsize=7, loc="lower center")
    ax.set_xlabel("day of the year")
    ax.set_ylabel("daily mean (°C)")
    ax.set_title("Daily Means, 2016–2025", color=style.BAD)
    style.save(fig, "viz_goodbad_spaghetti_bad")


def _highlight_good():
    data = _daily_by_year()
    fig, ax = plt.subplots(figsize=(6, 4))
    for year, (doy, dm) in data.items():
        if year != "2025":
            ax.plot(doy, dm, lw=0.6, color=style.DIM, alpha=0.45)
    doy, dm = data["2025"]
    ax.plot(doy, dm, lw=1.3, color=style.ACCENT)
    ax.text(70, -12.5, "2025", color=style.ACCENT, fontweight="bold")
    ax.set_xlabel("day of the year")
    ax.set_ylabel("daily mean (°C)")
    ax.set_title("2025: the coldest January and February of ten years")
    style.save(fig, "viz_goodbad_highlight_good")


FIGURES = {
    "viz_goodbad_two_axes_bad": _two_axes_bad,
    "viz_goodbad_two_axes_good": _two_axes_good,
    "viz_goodbad_gap_bad": _gap_bad,
    "viz_goodbad_gap_good": _gap_good,
    "viz_goodbad_window_bad": _window_bad,
    "viz_goodbad_window_good": _window_good,
    "viz_goodbad_spaghetti_bad": _spaghetti_bad,
    "viz_goodbad_highlight_good": _highlight_good,
}

if __name__ == "__main__":
    temp, hum = _monthly(1), _monthly(2)
    print("monthly temp", [round(v, 1) for v in temp])
    print("monthly humidity", [round(v, 1) for v in hum])
    years, means = _yearly()
    print("yearly", [(y, round(m, 2)) for y, m in zip(years, means)])
    print("2017 -> 2023:", round(means[years.index(2023)] - means[years.index(2017)], 2))
    data = _daily_by_year()
    for y, (doy, dm) in data.items():
        jf = [m for d, m in zip(doy, dm) if d <= 59]
        print(y, "Jan+Feb daily-mean average", round(sum(jf) / len(jf), 2), "days", len(dm))
