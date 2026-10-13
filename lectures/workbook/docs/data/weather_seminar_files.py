#!/usr/bin/env python3
"""Write the zips that Seminars 1, 3 and 4 hand out from the Releases page.

Before Seminar 6 the room has no Git, so files come as zips from
https://github.com/MindaugasSarpis/weather-project/releases. Each zip unpacks
into one folder of the same name in the home folder.

  weather-files.zip       Seminar 1: the two files of the station, as they
                          arrived by e-mail, and the e-mail itself
                          (weather-files/weather.csv, daily_export.csv,
                          message.txt)
  weather-project-s1.zip  Seminars 3 and 4, for a student without the folder
                          of Seminar 1: weather-project/ as Seminar 1 leaves
                          it (README with Folders, Data, Columns; data/raw;
                          data/processed/daily.csv repaired by hand;
                          results/daily.md; an empty scripts/)
  weather-scripts.zip     Seminar 4: the two handed-out programs
                          (weather-scripts/clean_export.py, column_stats.py)

Everything is built from the outputs of weather_files.py (run it first) and
the two cli_*.py scripts. Every entry carries a fixed date and fixed
permissions, so the zips are the same bytes on every run.

Usage:  python3 weather_seminar_files.py [outdir]
        (default outdir: misc/weather_repo/release/ of the repository)
"""
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_OUT = HERE.parents[3] / "misc" / "weather_repo" / "release"
RECEIVED = (2026, 10, 13, 9, 30, 0)   # the e-mail of the station's operator
SEMINAR1 = (2026, 10, 13, 12, 0, 0)   # the folder as Seminar 1 leaves it
SCRIPTS = (2026, 10, 13, 11, 20, 0)   # the two programs

MESSAGE = """\
13 October 2026

Hello,

here are the two files of our weather station:

weather.csv        the hourly log, 1 January 2016 to 31 December 2025
daily_export.csv   the daily mean temperature of 1 to 9 October 2025,
                   typed into a spreadsheet and exported from it

You may use them for anything, with no conditions (CC0).

Best regards,
the station's operator
"""

# The README as Seminar 1 leaves it: the README of weather_files.py with one
# line on the hand-made copy, and the columns. Seminar 4 deletes the line
# "Cleaned copy" when a script makes that file.
CLEANED = """\
- **Cleaned copy:** `data/processed/daily.csv`. Mean line deleted, `,` to
  `.`, `;` to `,`, column `nr` deleted.
"""

COLUMNS = """
## Columns of `weather.csv`

| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | ISO 8601 |
| `temp_c` | air temperature | °C |
| `humidity_pct` | relative humidity | % |
| `wind_ms` | wind speed | m/s |

Missing value: `temp_c` is `-999` in 120 rows, 2019-07-22 to 07-26, when
the temperature sensor was down.
"""


def daily_md(daily_csv):
    """daily.csv as the Markdown table of the Task of Seminar 1, Part 3."""
    lines = daily_csv.decode().splitlines()
    rows = ["| " + " | ".join(line.split(",")) + " |" for line in lines]
    return ("\n".join([rows[0], "|--|--|"] + rows[1:]) + "\n").encode()


def write_zip(path, root, date, entries):
    """entries: list of (name, bytes or None for a folder)."""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in [("", None)] + entries:
            info = zipfile.ZipInfo(root + name, date)
            info.create_system = 3  # Unix, so the permissions below are read
            if data is None:
                info.external_attr = (0o40755 << 16) | 0x10
                z.writestr(info, b"")
            else:
                info.external_attr = 0o644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, data)


def main(out):
    out.mkdir(parents=True, exist_ok=True)
    weather = (HERE / "weather.csv").read_bytes()
    export = (HERE / "weather_daily_export.csv").read_bytes()
    daily = (HERE / "weather_daily.csv").read_bytes()
    readme0 = (HERE / "weather_README.txt").read_text(encoding="utf-8")
    clean_py = (HERE / "cli_clean_export.py").read_bytes()
    stats_py = (HERE / "cli_column_stats.py").read_bytes()

    write_zip(out / "weather-files.zip", "weather-files/", RECEIVED, [
        ("weather.csv", weather),
        ("daily_export.csv", export),
        ("message.txt", MESSAGE.encode()),
    ])

    readme1 = (readme0 + CLEANED + COLUMNS).encode()
    write_zip(out / "weather-project-s1.zip", "weather-project/", SEMINAR1, [
        ("README.md", readme1),
        ("data/", None),
        ("data/raw/", None),
        ("data/raw/weather.csv", weather),
        ("data/raw/daily_export.csv", export),
        ("data/processed/", None),
        ("data/processed/daily.csv", daily),
        ("results/", None),
        ("results/daily.md", daily_md(daily)),
        ("scripts/", None),
    ])

    write_zip(out / "weather-scripts.zip", "weather-scripts/", SCRIPTS, [
        ("clean_export.py", clean_py),
        ("column_stats.py", stats_py),
    ])
    for name in ("weather-files.zip", "weather-project-s1.zip", "weather-scripts.zip"):
        print(f"{(out / name).stat().st_size:>9} {out / name}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT)
