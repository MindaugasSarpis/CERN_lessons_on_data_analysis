#!/usr/bin/env bash
# Scratch repository for Lecture 05: the weather project as Lecture 04 leaves
# it, put under Git on 20 Oct 2026 by Smiltė, with a colleague, Tomas, who
# clones it and pushes one commit that edits a raw file. Every git and
# PowerShell output on the L05 slides comes from one run of this script.
# Author and committer dates are fixed, so the commit ids are the same on
# every run. (Seminar 5 clones another repository, misc/weather_repo/.)
#
# Usage: bash misc/l05_scratch_repo/build.sh [outdir]
#   needs git (2.56 for the slides' wording), pwsh (PowerShell 7), python3,
#   unzip. It writes outdir/run/ and prints every command with its output.
# Rerun it whenever weather_files.py, cli_clean_export.py or
# cli_column_stats.py change: the blob, tree and commit ids depend on them.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
S="${1:-$HERE}"   # output folder: run/ is made inside it (gitignored)
DATA="$HERE/../../lectures/workbook/docs/data"
URL="https://github.com/smilte-example/weather-project.git"
rm -rf "$S/run" && mkdir -p "$S/run/home" "$S/run/tomas-home" "$S/run/bin"
ln -s "$(command -v python3)" "$S/run/bin/python"   # the course says `python`
export PATH="$S/run/bin:$PATH"
export GIT_CONFIG_NOSYSTEM=1 LC_ALL=C.UTF-8 TZ=Europe/Vilnius
REMOTE="$S/run/remote/weather-project.git"
gitconfig() {  # $1 home, $2 name, $3 e-mail
  cat > "$1/.gitconfig" <<EOF
[user]
	name = $2
	email = $3
[init]
	defaultBranch = main
[pull]
	rebase = false
[core]
	autocrlf = false
	pager = cat
	quotepath = false
[log]
	decorate = short
[url "$REMOTE"]
	insteadOf = $URL
EOF
}
gitconfig "$S/run/home" "Smiltė" "smilte@example.org"
gitconfig "$S/run/tomas-home" "Tomas" "tomas@example.org"
export HOME="$S/run/home"
T() { export GIT_AUTHOR_DATE="2026-10-20T$1:00+0300" GIT_COMMITTER_DATE="2026-10-20T$1:00+0300"; }
say() { echo; echo "##### $*"; }
fix() { sed -e "s#$REMOTE#$URL#g" -e "s#${REMOTE%.git}#${URL%.git}#g" -e "s#$S/run/#/Users/smilte/#g"; }
run() { echo "\$ $*"; "$@" 2>&1 | fix; }
ps() {  # one PowerShell line, run in the current folder
  printf '%s\n' "$1" > "$S/run/cmd.ps1"
  echo "PS> $1"
  timeout 120 pwsh -NoProfile -File "$S/run/cmd.ps1" < /dev/null 2>&1 | fix
}

# ---- the project folder as Lecture 04 leaves it -------------------------
P="$S/run/weather-project"
cd "$S/run" && unzip -q "$DATA/weather_project.zip"
cd "$P"
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

## Columns of `weather.csv`

| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | ISO 8601 |
| `temp_c` | air temperature | °C |
| `humidity_pct` | relative humidity | % |
| `wind_ms` | wind speed | m/s |

Missing value: `temp_c` is `-999` in 120 rows, 2019-07-22 to 07-26.

## How to rebuild

In the project folder, in PowerShell 7 on macOS or Windows, with Python from
Miniforge; the script needs no package beyond it.

    ./scripts/rebuild.ps1

It writes `data/processed/weather_valid.csv`, `weather.csv` without the
120 rows marked `-999` (87 553 lines), and `data/processed/daily.csv`, the
cleaned export (148 bytes, SHA-256 `33fe5e77…f705483d`).

## Licence

Data: CC0, from the station's operator.
Scripts and text: MIT, see `LICENSE`.
EOF
cat > scripts/rebuild.ps1 <<'EOF'
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
New-Item -ItemType Directory -Force data/processed | Out-Null
Select-String ',-999,' data/raw/weather.csv -NotMatch -Raw > data/processed/weather_valid.csv
python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
EOF
ps './scripts/rebuild.ps1'

say SIZES
find . -type f -printf '%s %p\n' | sort -k2
du -sb . data/raw data/processed
ps 'python scripts/column_stats.py data/processed/weather_valid.csv temp_c'
ps 'python scripts/column_stats.py data/raw/weather.csv temp_c'
sed -n 1,4p data/raw/daily_export.csv

# ---- the two copies of the opening ---------------------------------------
say HOOK
mkdir -p "$S/run/copies/smilte" "$S/run/copies/tomas"
cp data/raw/daily_export.csv "$S/run/copies/smilte/daily_export.csv"
sed 's/^1;2025-10-01;6,3$/1;2025-10-01;6,4/' data/raw/daily_export.csv > "$S/run/copies/tomas/daily_export.csv"
( cd "$S/run/copies"
  ps '(Get-FileHash smilte/daily_export.csv, tomas/daily_export.csv).Hash'
  ps 'Get-ChildItem smilte, tomas -File | Select-Object Directory, Name, Length'
  run git diff --no-index smilte/daily_export.csv tomas/daily_export.csv )

say HELLO
ps '"hello" | git hash-object --stdin'
ps '"hallo" | git hash-object --stdin'
run sh -c 'printf "hello\r\n" | git hash-object --stdin'

say BLOB
run git hash-object data/raw/weather.csv
run git hash-object data/raw/daily_export.csv
cp data/raw/weather.csv "$S/run/copy-of-weather.csv"
run git hash-object "$S/run/copy-of-weather.csv"
ps '(Get-FileHash data/raw/weather.csv).Hash'
ps '(Get-FileHash data/raw/*).Hash'

# ---- first commits -------------------------------------------------------
say INIT
run git init
run git status
T 10:15
run git add README.md
run git commit -m "Add the README"
cat > .gitignore <<'EOF'
# made by the operating system
.DS_Store
Thumbs.db

# made by scripts/rebuild.ps1
data/processed/
EOF
run git status --short
T 10:20
run git add .gitignore
run git commit -m "Add .gitignore"
cat > .gitattributes <<'EOF'
# Check out every file with the bytes it was committed with:
# no CRLF line endings on Windows, the same checksums on every laptop.
* -text
EOF
T 10:22
run git add .gitattributes
run git commit -m "Keep the committed bytes of every file on checkout"
run git add .
run git status
run git status --short --ignored
T 10:25
run git commit -m "Add the data and the scripts"
run git count-objects -v
B=$(git hash-object data/raw/weather.csv)
ls -l ".git/objects/${B:0:2}/"

say MODEL
run git cat-file -p HEAD
run git cat-file -s HEAD
run sh -c 'git cat-file commit HEAD | git hash-object -t commit --stdin'
run git cat-file -p 'HEAD^{tree}'
run git cat-file -p HEAD:data
run git cat-file -p HEAD:data/raw
run git cat-file -p HEAD:scripts
run git log --oneline
for c in HEAD HEAD~1 HEAD~2 HEAD~3; do git rev-parse "$c^{tree}"; git ls-tree "$c" README.md; done
ps 'Get-Content .git/HEAD'
ps 'Get-Content .git/refs/heads/main'
ps '(Get-Item .git/refs/heads/main).Length'

# ---- a change and its diff -----------------------------------------------
say DIFF
python3 - <<'EOF'
from pathlib import Path
p = Path("README.md")
t = p.read_text(encoding="utf-8")
new = """## Result

- **Mean air temperature, 2016 to 2025:** 7.16 °C
- **From:** `column_stats.py` on `data/processed/weather_valid.csv`, 87 552 hours

## Licence"""
p.write_text(t.replace("## Licence", new), encoding="utf-8")
EOF
run git status --short
run git status
run git diff
run git diff --stat
T 10:35
run git add README.md
run git status --short
run git diff
run git diff --staged --stat
run git commit -m "Give the mean temperature in the README"
C4=$(git rev-parse --short HEAD)
ps 'Get-Content .git/refs/heads/main'
run git log --oneline
run git log -1
run git show --stat "$C4"
L=$(grep -n "Mean air" README.md | cut -d: -f1)
run git blame -s -L "$L,$((L+1))" README.md
run git log --oneline -- README.md

say RESTORE
python3 - <<'EOF'
import re
from pathlib import Path
p = Path("README.md")
t = p.read_text(encoding="utf-8")
p.write_text(re.sub(r"## Columns of.*?Missing value[^\n]*\n\n", "", t, flags=re.S), encoding="utf-8")
EOF
run git diff --stat
run git restore README.md
run git status

say AMEND
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
T 10:40
git add LICENSE
run git commit -m "Add teh LICENSE named in the README"
export GIT_COMMITTER_DATE="2026-10-20T10:41:00+0300"
run git commit --amend -m "Add the LICENSE named in the README"
run git log --oneline -2

say REVERT
T 10:45
run git rm data/raw/daily_export.csv
run git commit -m "Remove the raw export, daily.csv replaces it"
BAD=$(git rev-parse --short HEAD)
rm -rf data/processed
ps './scripts/rebuild.ps1'
T 10:50
run git revert --no-edit "$BAD"
run git log --oneline -3
run git show --stat HEAD
ps './scripts/rebuild.ps1'

# ---- the remote ----------------------------------------------------------
say PUSH
mkdir -p "$S/run/remote"
git init -q --bare "$REMOTE"
run git remote add origin "$URL"
run git remote -v
echo "\$ git push -u origin main"
git push --progress -u origin main 2>&1 | tr '\r' '\n' | grep -v '([0-9]*/[0-9]*)$' | fix
run git push
run git status

say CLONE
mkdir -p "$S/run/tomas" && cd "$S/run/tomas"
( export HOME="$S/run/tomas-home"
  run git clone "$URL"
  cd weather-project
  run git log --oneline -1
  ps 'Get-ChildItem data -Name'
  ps './scripts/rebuild.ps1'
  ps 'Get-ChildItem data -Name'
  sed -i 's/^1;2025-10-01;6,3$/1;2025-10-01;6,4/' data/raw/daily_export.csv
  run git diff
  T 11:30
  git add data/raw/daily_export.csv
  run git commit -m "Correct 1 October to 6,4" -m "The station's paper log says 6,4 for 1 October 2025."
  run git push )
cd "$P"
T 11:35
run git pull
run git log --oneline -3
TOM=$(git rev-parse --short HEAD)

# ---- branches ------------------------------------------------------------
say BRANCH
run git switch -c ranges
run git branch
ps 'Get-Content .git/HEAD'
ps 'Get-ChildItem .git/refs/heads -Name'
python3 - <<'PY'
t = open("README.md", encoding="utf-8").read()
old = """| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | ISO 8601 |
| `temp_c` | air temperature | °C |
| `humidity_pct` | relative humidity | % |
| `wind_ms` | wind speed | m/s |
"""
new = """| Column | Meaning | Unit | Range |
|--|--|--|--|
| `time` | start of the hour | ISO 8601 | 2016-01-01T00:00 to 2025-12-31T23:00 |
| `temp_c` | air temperature | °C | -16.3 to 32.4 |
| `humidity_pct` | relative humidity | % | 34 to 100 |
| `wind_ms` | wind speed | m/s | 0.0 to 12.0 |
"""
assert old in t
open("README.md", "w", encoding="utf-8").write(t.replace(old, new))
PY
run git diff --stat
T 11:40
git add README.md
run git commit -m "Give the range of each column"
ps 'Get-ChildItem .git/refs/heads -Name'
run git switch main
run git merge ranges
run git branch -d ranges

say CONFLICT
run git switch -c wording
sed -i '3,4c Ten years of hourly readings from one weather station, and the daily\nmeans of nine days of October 2025, typed into a spreadsheet from them.' README.md
run git diff
T 11:45
git add README.md
run git commit -m "Reword the first paragraph"
run git switch main
sed -i '3,4c The hourly log of one weather station, 2016 to 2025, 87 672 hours, and a\ntable of daily mean temperatures typed into a spreadsheet from it.' README.md
T 11:50
git add README.md
run git commit -m "Give the number of hours in the first paragraph"
run git log --oneline --graph --all -4
T 11:55
run git merge wording
run git status
sed -n 1,10p README.md
python3 - <<'EOF'
import re
t = open("README.md", encoding="utf-8").read()
t = re.sub(r"<<<<<<< HEAD\n.*?>>>>>>> wording\n",
           "Ten years of hourly readings from one weather station, 87 672 hours, and\n"
           "the daily means of nine days of October 2025, typed into a spreadsheet\nfrom them.\n",
           t, flags=re.S)
open("README.md", "w", encoding="utf-8").write(t)
EOF
sed -n 1,7p README.md
run git add README.md
run git commit --no-edit
run git cat-file -p HEAD
run git log --oneline --graph -5
run git status
run git push

# ---- who edited the raw file ---------------------------------------------
say CLOSE
run git log --oneline -- data/raw
run git log --oneline -- data/raw/daily_export.csv
run git blame -s -L 2,2 data/raw/daily_export.csv
run git blame -L 2,2 data/raw/daily_export.csv
run git show "$TOM"
ps 'python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv; (Get-FileHash data/processed/daily.csv).Hash'
T 12:05
run git revert --no-edit "$TOM"
run git show --stat HEAD
sed -n 2p data/raw/daily_export.csv
ps './scripts/rebuild.ps1; (Get-FileHash data/processed/daily.csv).Hash'
run git push

say TAG
T 12:10
run git tag -a v1.0 -m "Data as received; mean 7.16 °C"
run git log --oneline -3
run git push origin v1.0
run git show v1.0 --stat
run git log --oneline --graph --all

say SIZE
du -sb .git; git count-objects -vH; git log --oneline | wc -l
