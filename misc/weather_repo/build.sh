#!/usr/bin/env bash
# The repository github.com/MindaugasSarpis/weather-project, which Seminar 5
# clones: the weather project of Lectures 1 to 4 with seven commits by two
# people. Commit 6 (Tomas) makes the mean read the raw file, -999 rows and
# all, and writes 5.78 into the README; the seminar finds it and reverts it.
#
# Author and committer, name, e-mail and date are fixed, so every run makes
# the same commit ids, the ids printed on the Seminar 5 page. The shell of
# the course is PowerShell 7 on macOS and Windows: one script, rebuild.ps1.
#
# Usage: bash misc/weather_repo/build.sh [outdir]
#   writes outdir/weather-project (default: misc/weather_repo/run/, gitignored)
#   GIT=/path/to/git selects the git binary.
# To publish after a change (rewrites the public history; only before the
# room has cloned it):
#   cd run/weather-project
#   git remote add origin https://github.com/MindaugasSarpis/weather-project.git
#   git push --force origin main
set -eu
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${1:-$HERE/run}"
DATA="$HERE/../../lectures/workbook/docs/data"
GIT="${GIT:-git}"
R="$OUT/weather-project"
rm -rf "$R" && mkdir -p "$R"
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1 TZ=Europe/Vilnius LC_ALL=C
cd "$R"
"$GIT" init -q -b main
"$GIT" config core.autocrlf false

commit() {  # commit WHO DATE MESSAGE [BODY]
  local name email
  case "$1" in
    smilte) name="Smiltė" email="smilte@example.org" ;;
    tomas) name="Tomas" email="tomas@example.org" ;;
  esac
  "$GIT" add -A
  GIT_AUTHOR_NAME="$name" GIT_AUTHOR_EMAIL="$email" GIT_AUTHOR_DATE="$2" \
  GIT_COMMITTER_NAME="$name" GIT_COMMITTER_EMAIL="$email" GIT_COMMITTER_DATE="$2" \
    "$GIT" commit -q -m "$3" ${4:+-m "$4"}
}

# --- 1. the data as it arrived --------------------------------------------
mkdir -p data/raw
cp "$DATA/weather.csv" data/raw/weather.csv
cp "$DATA/weather_daily_export.csv" data/raw/daily_export.csv
cat > .gitattributes <<'EOF'
# Check out every file with the bytes it was committed with:
# no CRLF line endings on Windows, the same checksums on every laptop.
* -text
EOF
cat > README.md <<'EOF'
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
EOF
commit smilte "2026-10-13T10:05:00+03:00" "Add the station's hourly log and the spreadsheet export"

# --- 2. the two scripts -----------------------------------------------------
mkdir -p scripts
cp "$DATA/cli_clean_export.py" scripts/clean_export.py
cp "$DATA/cli_column_stats.py" scripts/column_stats.py
commit smilte "2026-10-13T11:20:00+03:00" "Add the two scripts handed out with the data"

# --- 3. the columns ---------------------------------------------------------
cat >> README.md <<'EOF'

## Columns of `weather.csv`

| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | ISO 8601 |
| `temp_c` | air temperature | °C |
| `humidity_pct` | relative humidity | % |
| `wind_ms` | wind speed | m/s |

Missing value: `temp_c` is `-999` in 120 rows, 2019-07-22 to 07-26, when
the temperature sensor was down.
EOF
commit smilte "2026-10-14T09:40:00+03:00" "Describe the columns and the -999 rows"

# --- 4. the rebuild script ---------------------------------------------------
cat > scripts/rebuild.ps1 <<'EOF'
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
New-Item -ItemType Directory -Force data/processed, results | Out-Null
Select-String ',-999,' data/raw/weather.csv -NotMatch -Raw > data/processed/weather_valid.csv
python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
EOF
cat >> README.md <<'EOF'

## How to rebuild

In the project folder, in PowerShell 7 on macOS or Windows, with Python from
Miniforge; the script needs no package beyond it.

    ./scripts/rebuild.ps1

It writes `data/processed/weather_valid.csv`, `weather.csv` without the
120 rows marked `-999` (87 553 lines), and `data/processed/daily.csv`, the
cleaned export (148 bytes).
EOF
commit smilte "2026-10-15T14:30:00+03:00" "Add the rebuild script"

# --- 5. the mean -------------------------------------------------------------
echo 'python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt' >> scripts/rebuild.ps1
python3 - <<'EOF'
from pathlib import Path
p = Path("README.md")
text = p.read_text(encoding="utf-8")
result = """## Result

Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours. The 120 hours
marked `-999` are left out. The script writes it to `results/temp_c.txt`.

## How to rebuild"""
p.write_text(text.replace("## How to rebuild", result), encoding="utf-8")
EOF
commit smilte "2026-10-16T16:10:00+03:00" "Write the mean temperature into results and the README"

# --- 6. the change that the seminar finds ------------------------------------
sed -i 's|data/processed/weather_valid.csv temp_c|data/raw/weather.csv temp_c|' scripts/rebuild.ps1
python3 - <<'EOF'
from pathlib import Path
p = Path("README.md")
text = p.read_text(encoding="utf-8")
old = """Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours. The 120 hours
marked `-999` are left out. The script writes it to `results/temp_c.txt`."""
new = """Mean `temp_c`, 2016 to 2025: **5.78 °C**, over all 87 672 hours of
`weather.csv`. The script writes it to `results/temp_c.txt`."""
assert old in text
p.write_text(text.replace(old, new), encoding="utf-8")
EOF
commit tomas "2026-10-19T11:45:00+03:00" "Take the mean over all rows of weather.csv" \
  "The valid file leaves 120 hours out. The raw file has every hour."

# --- 7. a licence --------------------------------------------------------------
cat > LICENSE <<'EOF'
MIT License

Copyright (c) 2026 Smiltė

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF
cat >> README.md <<'EOF'

## Licence

Data: CC0, from the station's operator. Scripts and text: MIT, see
`LICENSE`.
EOF
commit smilte "2026-10-19T17:05:00+03:00" "Add a licence"

"$GIT" log --format='%h %an %ad %s' --date=short
