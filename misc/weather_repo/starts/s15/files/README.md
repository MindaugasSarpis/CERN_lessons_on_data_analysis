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
- `data/raw/hill_station.csv`: the hourly log of a second station, 2025,
  4 km away and 180 m higher; `;`-separated, decimal commas.
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

In zsh on macOS or Git Bash on Windows, with Miniforge, in the project folder:

    conda env create -f environment.yml
    conda activate s15
    python run_all.py

`run_all.py` makes `data/processed` and `results` from `data/raw`, runs the
tests and prints the checksum of every file it made.
