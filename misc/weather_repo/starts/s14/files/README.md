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
- **Source:** the station's operator, by e-mail
- **Received:** 2026-10-13

## Columns of `weather.csv`

| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | ISO 8601 |
| `temp_c` | air temperature | °C |
| `humidity_pct` | relative humidity | % |
| `wind_ms` | wind speed | m/s |

Missing value: `temp_c` is `-999` in 120 rows, 2019-07-22 to 07-26, when
the temperature sensor was down.

## Result

Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours. The 120 hours
marked `-999` are left out. The script writes it to `results/temp_c.txt`.

## Hill station

`scripts/clean_hill.py` cleans `data/raw/hill_station.csv` (2025, 4 km
away, 180 m higher). Over 361 days the hill is 1.19 °C colder than the
valley. The counts of each rule are in `results/hill.txt`.

## How to rebuild

In the project folder, in zsh on macOS or Git Bash on Windows, with Python
from Miniforge; the script needs no package beyond it.

    ./scripts/rebuild.sh

It writes `data/processed/weather_valid.csv`, `weather.csv` without the
120 rows marked `-999` (87 553 lines), and `data/processed/daily.csv`, the
cleaned export (148 bytes).
