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

Checked in Python, `scripts/mean_temp.py`: 7.16 °C over 87 552 hours.
The coldest hour, `scripts/coldest_hour.py`: 2025-01-07T05:00, -16.3 °C.

## How to rebuild

In the project folder, in zsh on macOS or Git Bash on Windows, with Python
from Miniforge; the script needs no package beyond it.

    ./scripts/rebuild.sh

It writes `data/processed/weather_valid.csv`, `weather.csv` without the
120 rows marked `-999` (87 553 lines), and `data/processed/daily.csv`, the
cleaned export (148 bytes).

## Licence

Data: CC0, from the station's operator. Scripts and text: MIT, see
`LICENSE`.

## How sure is the mean

7.16 ± 0.22 °C. The ± is the standard error from the ten yearly means
(they scatter by 0.70 °C). The hours are not independent: one hour and
the next correlate by 0.996, so s/√N = 0.03 °C is too small.
`scripts/mean_error.py` computes it.

## The yearly cycle

Daily means fitted with c − A cos(2π(d − d0)/365.25) by
`scripts/fit_cycle.py`: A = 11.18 °C, coldest on day 15.9 (16 January).
The fit's ± 0.07 °C is too small: the residuals of neighbouring days
correlate by 0.875.

Trend of the ten yearly means, `scripts/fit_trend.py`: −0.6 ± 0.8 °C per
decade, compatible with zero.
