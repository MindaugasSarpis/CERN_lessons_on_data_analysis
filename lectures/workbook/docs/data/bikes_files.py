#!/usr/bin/env python3
"""Write the bike-counter files of Seminar 4 next to this script.

The files are generated, not measured: two made-up bicycle counters in a
city, one on a bridge and one on a park path, counting the bicycles that pass
in each hour of 2024 and 2025. They behave like real counters (rush hours on
weekdays, an outing at midday on weekends, few bicycles in winter, wet days
with fewer), and one of them was broken for a week: while it was broken, its
logger wrote 9999.

  bikes_hourly.csv          saved as bikes.csv: 35 088 rows, time,counter,bikes
  bikes_monthly_export.csv  saved as monthly_export.csv (an optional section):
                            the mean number of bicycles per day on the bridge
                            in each month of 2025, as a spreadsheet with
                            European settings exports it: `;` between the
                            values, a decimal comma, a column `nr`, and a
                            line with the mean
  bikes_README.txt          the README at the end of the seminar
  bikes_project.zip         the folder `bike-project` at the end of the core
                            of the seminar, for a student who lost a step:
                            the README, `bikes.csv`, `bikes_valid.csv` as zsh
                            writes it, `column_stats.py`, the two rebuild
                            scripts and `results/bikes_stats.txt`

The README is `.txt` because MkDocs turns every `.md` file in `docs/` into a
page. The random numbers are seeded and the zip carries a fixed date, so the
output is the same on every run. Reads `cli_column_stats.py`, which goes
into the zip.

Usage:  python3 bikes_files.py
"""
import hashlib
import subprocess
import sys
import tempfile
import math
import random
import zipfile
from datetime import datetime, timedelta
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATE = (2026, 10, 13, 12, 0, 0)
START = datetime(2024, 1, 1)
END = datetime(2026, 1, 1)
COUNTERS = {"bridge": 1.0, "park": 0.55}
BROKEN = ("park", datetime(2025, 3, 10), datetime(2025, 3, 17))
MARK = "9999"
REBUILD_SH = """\
#!/bin/zsh
grep -v ',9999$' data/raw/bikes.csv > data/processed/bikes_valid.csv
python3 scripts/column_stats.py data/processed/bikes_valid.csv bikes > results/bikes_stats.txt
"""
REBUILD_PS1 = """\
Select-String ',9999$' data/raw/bikes.csv -NotMatch -Raw > data/processed/bikes_valid.csv
python scripts/column_stats.py data/processed/bikes_valid.csv bikes > results/bikes_stats.txt
"""


def poisson(rng, mean):
    if mean > 30:
        return max(0, round(rng.gauss(mean, math.sqrt(mean))))
    limit, k, p = math.exp(-mean), 0, 1.0
    while True:
        p *= rng.random()
        if p <= limit:
            return k
        k += 1


def profile(ts):
    h = ts.hour
    if ts.weekday() < 5:
        return (0.04 + 1.6 * math.exp(-((h - 8) ** 2) / 1.5)
                + 1.4 * math.exp(-((h - 17) ** 2) / 2.5)
                + 0.45 * math.exp(-((h - 13) ** 2) / 8))
    return 0.03 + 1.0 * math.exp(-((h - 14) ** 2) / 10)


def rows():
    rng = random.Random(2026)
    day_factor = {}
    ts = START
    while ts < END:
        day = ts.date()
        if day not in day_factor:
            day_factor[day] = math.exp(rng.gauss(0, 0.35))
        year_angle = 2 * math.pi * (ts.timetuple().tm_yday - 15) / 365.25
        season = 0.55 - 0.40 * math.cos(year_angle)
        for name, size in COUNTERS.items():
            mean = 220 * size * season * profile(ts) * day_factor[day]
            count = poisson(rng, mean)
            broken = name == BROKEN[0] and BROKEN[1] <= ts < BROKEN[2]
            yield ts, name, count, (MARK if broken else str(count))
        ts += timedelta(hours=1)


def comma(value, places):
    q = Decimal(1).scaleb(-places)
    return str(Decimal(str(value)).quantize(q, rounding=ROUND_HALF_UP)).replace(".", ",")


def main():
    lines = ["time,counter,bikes"]
    per_day = {}
    for ts, name, count, text in rows():
        lines.append(f"{ts:%Y-%m-%dT%H:%M},{name},{text}")
        if name == "bridge" and ts.year == 2025:
            per_day.setdefault(ts.month, {}).setdefault(ts.day, 0)
            per_day[ts.month][ts.day] += count
    hourly = ("\n".join(lines) + "\n").encode()
    (HERE / "bikes_hourly.csv").write_bytes(hourly)

    export = ["nr;month;per_day"]
    means = []
    for month in range(1, 13):
        days = per_day[month].values()
        mean = float(Decimal(sum(days) / len(days)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
        means.append(mean)
        export.append(f"{month};2025-{month:02d};{comma(mean, 1)}")
    export.append(f";mean;{comma(sum(means) / len(means), 2)}")
    export_bytes = ("\n".join(export) + "\n").encode()
    (HERE / "bikes_monthly_export.csv").write_bytes(export_bytes)

    # The file the core of the seminar makes, as zsh writes it (LF).
    valid = ("\n".join(l for l in lines if not l.endswith("," + MARK)) + "\n").encode()

    # results/bikes_stats.txt, as the script writes it: column_stats.py run
    # on the valid rows.
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "data/processed/bikes_valid.csv"
        path.parent.mkdir(parents=True)
        path.write_bytes(valid)
        stats = subprocess.run(
            [sys.executable, str(HERE / "cli_column_stats.py"),
             "data/processed/bikes_valid.csv", "bikes"],
            cwd=tmp, capture_output=True, check=True).stdout

    digest = hashlib.sha256(hourly).hexdigest()
    readme = README.format(short=f"{digest[:8]}…{digest[-8:]}").encode()
    (HERE / "bikes_README.txt").write_bytes(readme)
    root = "bike-project/"
    with zipfile.ZipFile(HERE / "bikes_project.zip", "w", zipfile.ZIP_DEFLATED) as z:
        def put(name, data=None, mode=0o644):
            info = zipfile.ZipInfo(root + name, DATE)
            if data is None:
                info.external_attr = 0o40755 << 16
                z.writestr(info, b"")
            else:
                info.external_attr = mode << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, data)
        put("")
        put("README.md", readme)
        put("data/")
        put("data/raw/")
        put("data/raw/bikes.csv", hourly)
        put("data/processed/")
        put("data/processed/bikes_valid.csv", valid)
        put("scripts/")
        put("scripts/column_stats.py", (HERE / "cli_column_stats.py").read_bytes())
        put("scripts/rebuild.sh", REBUILD_SH.encode(), 0o755)
        put("scripts/rebuild.ps1", REBUILD_PS1.encode())
        put("results/")
        put("results/bikes_stats.txt", stats)


README = """\
# Bike Counters

Two bicycle counters, one on a bridge and one on a park path, counted
every hour of 2024 and 2025. How many bicycles pass in an hour?

## Folders

- `data/raw`: files as they arrived, never edited
- `data/processed`: files that commands make from `data/raw`
- `scripts`: programs
- `results`: numbers that the programs write

## Data

`data/raw/bikes.csv`: two bicycle counters, one row per counter and
hour of 2024 and 2025, 35 088 rows, SHA-256 `{short}`.
From [Seminar 4](https://mindaugassarpis.github.io/CERN_lessons_on_data_analysis/workbook/seminars/seminar_04/)
of the course workbook.

| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | YYYY-MM-DDTHH:MM |
| `counter` | `bridge` or `park` | none |
| `bikes` | bicycles that passed in that hour | bicycles |

Missing value: `bikes` is `9999` in 168 rows, the park counter from
2025-03-10 to 2025-03-16, while it was broken.

## How to rebuild

In the project folder: `./scripts/rebuild.sh` in zsh on macOS,
`./scripts/rebuild.ps1` in PowerShell 7 on Windows. They make:

- `data/processed/bikes_valid.csv`: `bikes.csv` without the rows
  marked `9999`, 34 921 lines
- `results/bikes_stats.txt`: rows, smallest, largest and mean of
  `bikes` in it
"""


if __name__ == "__main__":
    main()
