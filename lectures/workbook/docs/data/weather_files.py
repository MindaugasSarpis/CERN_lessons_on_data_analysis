#!/usr/bin/env python3
"""Write the weather-station files of the lectures next to this script.

The files are generated, not measured: the hourly log of a made-up weather
station. They behave like a real station's log (a yearly and a daily cycle,
weather that changes over days, a five-day sensor failure written as -999),
and every number on the slides comes from them.

  weather.csv               hourly log, 2016-01-01T00:00 to 2025-12-31T23:00,
                            87 672 rows: time, temp_c, humidity_pct, wind_ms
  weather_daily_export.csv  nine daily means of October 2025, as a spreadsheet
                            with European settings exports them: `;` between
                            the values, a decimal comma, a column `nr`, and a
                            line with the mean at the end
  weather_daily.csv         the export cleaned: `date,temp_c` and nine rows,
                            148 bytes, LF; what `clean_export.py` writes
                            (Lecture 3 starts from it)
  weather_README.txt        the README the project folder starts with
  weather_project.zip       the project folder `weather-project` that
                            Lecture 4 starts from

The README is `.txt` because MkDocs turns every `.md` file in `docs/` into a
page. The random numbers are seeded and the zip carries a fixed date, so the
output is the same on every run.

Usage:  python3 weather_files.py
"""
import math
import random
import zipfile
from datetime import datetime, timedelta
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATE = (2026, 10, 12, 12, 0, 0)
START = datetime(2016, 1, 1)
END = datetime(2026, 1, 1)
FAULT = (datetime(2019, 7, 22), datetime(2019, 7, 27))  # temperature sensor down
MISSING = "-999"
EXPORT_DAYS = [datetime(2025, 10, d) for d in range(1, 10)]


def fmt(value):
    """One decimal, and never `-0.0`."""
    text = f"{value:.1f}"
    return "0.0" if text == "-0.0" else text


def hourly_rows():
    rng = random.Random(2026)
    weather = humid = windy = 0.0
    hours = int((END - START).total_seconds() // 3600)
    for i in range(hours):
        ts = START + timedelta(hours=i)
        year_angle = 2 * math.pi * (ts.timetuple().tm_yday - 18) / 365.25
        season = 7.2 - 11.0 * math.cos(year_angle)
        day_amp = 3.5 - 1.5 * math.cos(year_angle)
        day = math.cos(2 * math.pi * (ts.hour - 15) / 24)
        weather = 0.992 * weather + rng.gauss(0, 0.40)
        humid = 0.97 * humid + rng.gauss(0, 1.5)
        windy = 0.97 * windy + rng.gauss(0, 0.45)
        temp = season + day_amp * day + weather
        rh = 79 + 7 * math.cos(year_angle) - 9 * day - 1.2 * weather + humid
        wind = 3.4 + 0.6 * math.cos(year_angle) + 0.8 * day + windy
        rh = min(100, max(18, round(rh)))
        wind = max(0.0, wind)
        temp_text = MISSING if FAULT[0] <= ts < FAULT[1] else fmt(temp)
        yield ts, temp, f"{ts:%Y-%m-%dT%H:%M},{temp_text},{rh},{fmt(wind)}"


def comma(value, places):
    q = Decimal(1).scaleb(-places)
    return str(Decimal(str(value)).quantize(q, rounding=ROUND_HALF_UP)).replace(".", ",")


def main():
    lines = ["time,temp_c,humidity_pct,wind_ms"]
    daily = {d: [] for d in EXPORT_DAYS}
    for ts, temp, line in hourly_rows():
        lines.append(line)
        key = datetime(ts.year, ts.month, ts.day)
        if key in daily:
            daily[key].append(temp)
    weather = "\n".join(lines) + "\n"
    (HERE / "weather.csv").write_bytes(weather.encode())

    means = [float(Decimal(sum(v) / len(v)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
             for v in daily.values()]
    export = ["nr;date;temp_c"]
    for nr, (day, mean) in enumerate(zip(EXPORT_DAYS, means), start=1):
        export.append(f"{nr};{day:%Y-%m-%d};{comma(mean, 1)}")
    export.append(f";mean;{comma(sum(means) / len(means), 2)}")
    export_text = "\n".join(export) + "\n"
    (HERE / "weather_daily_export.csv").write_bytes(export_text.encode())
    daily = ["date,temp_c"] + [f"{day:%Y-%m-%d},{mean:.1f}" for day, mean in zip(EXPORT_DAYS, means)]
    (HERE / "weather_daily.csv").write_bytes(("\n".join(daily) + "\n").encode())

    readme = README.encode()
    (HERE / "weather_README.txt").write_bytes(readme)
    scripts = {
        "clean_export.py": (HERE / "cli_clean_export.py").read_bytes(),
        "column_stats.py": (HERE / "cli_column_stats.py").read_bytes(),
    }
    root = "weather-project/"
    with zipfile.ZipFile(HERE / "weather_project.zip", "w", zipfile.ZIP_DEFLATED) as z:
        def put(name, data=None):
            info = zipfile.ZipInfo(root + name, DATE)
            if data is None:
                info.external_attr = 0o40755 << 16
                z.writestr(info, b"")
            else:
                info.external_attr = 0o644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, data)
        put("")
        put("README.md", readme)
        put("data/")
        put("data/raw/")
        put("data/raw/weather.csv", weather.encode())
        put("data/raw/daily_export.csv", export_text.encode())
        put("data/processed/")
        put("scripts/")
        for name, data in scripts.items():
            put("scripts/" + name, data)
        put("results/")


README = """\
# Weather Station

The hourly log of one weather station, 2016 to 2025, and a table of daily
mean temperatures typed into a spreadsheet from it.

## Folders

| Folder | What goes in |
|--|--|
| `data/raw` | files as they arrived, never edited |
| `data/processed` | files made from `data/raw` by commands and scripts |
| `scripts` | programs |
| `results` | numbers and figures the programs produce |

## Data

- `data/raw/weather.csv`: one row per hour, from 2016-01-01 00:00 to
  2025-12-31 23:00.
- `data/raw/daily_export.csv`: the daily mean temperature of 1 to 9 October
  2025, exported from a spreadsheet.
- **Source:** generated for the course by `weather_files.py`. The station is
  made up; the files behave like a real station's log.
- **Received:** 2026-10-13
"""


if __name__ == "__main__":
    main()
