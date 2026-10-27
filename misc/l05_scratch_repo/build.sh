#!/usr/bin/env bash
# Scratch repository for Lecture 05: the weather project as Lecture 04 leaves
# it, put under Git on 20 Oct 2026 by Smiltė, with a colleague, Tomas, who
# clones it and pushes one commit that edits a raw file, then a reworded
# paragraph that conflicts with Smiltė's, and Rūta, who forks it and sends
# a column of ranges by a pull request (Lecture 6). Every git and
# shell output on the L05 slides comes from one run of this script. Shell
# lines run in bash, whose GNU tools are those of Git Bash; zsh on macOS
# prints the same, `wc` and `ls` up to padding and order.
# Author and committer dates are fixed, so the commit ids are the same on
# every run. (Seminar 5 clones another repository, misc/weather_repo/.)
#
# Usage: bash misc/l05_scratch_repo/build.sh [outdir]
#   needs git (2.56 for the slides' wording), python3, sha256sum, xxd,
#   unzip. It writes outdir/run/ and prints every command with its output,
#   and writes lectures/workbook/docs/data/weather_project_git.zip, the
#   project before `git init`: the folder the lecturer opens for the live
#   moments of Lecture 6.
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
sh_() {  # one shell line, run by bash in the current folder
  echo "\$ $1"
  bash -c "$1" 2>&1 | fix
}
shasum() { sha256sum "${@:3}"; }   # `shasum -a 256 F` on macOS = `sha256sum F`
export -f shasum

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

In the project folder, in zsh on macOS or Git Bash on Windows, with Python
from Miniforge; the script needs no package beyond it.

    ./scripts/rebuild.sh

It writes `data/processed/weather_valid.csv`, `weather.csv` without the
120 rows marked `-999` (87 553 lines), and `data/processed/daily.csv`, the
cleaned export (148 bytes, SHA-256 `33fe5e77…f705483d`).

## Licence

Data: CC0, from the station's operator.
Scripts and text: MIT, see `LICENSE`.
EOF
cat > scripts/rebuild.sh <<'EOF'
#!/usr/bin/env bash
set -e
mkdir -p data/processed
grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
EOF
chmod 755 scripts/rebuild.sh
sh_ './scripts/rebuild.sh'

# The lecturer's live folder: this project before `git init`, as a zip with
# fixed dates and modes, so a rerun writes the same bytes (lecture_6.md).
python3 - "$DATA/weather_project_git.zip" <<'EOF'
import os, sys, zipfile
out = sys.argv[1]
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk("."):
        dirs.sort()
        rel = os.path.relpath(root, ".")
        names = [rel] if rel != "." else []
        names += [os.path.join(rel, f) for f in sorted(files)]
        for n in names:
            arc = os.path.normpath(os.path.join("weather-project", n))
            info = zipfile.ZipInfo(arc + ("/" if os.path.isdir(n) else ""), (2026, 10, 20, 10, 0, 0))
            if os.path.isdir(n):
                info.external_attr = (0o40755 << 16) | 0x10
                z.writestr(info, b"")
            else:
                info.external_attr = (0o100755 if os.access(n, os.X_OK) else 0o100644) << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, open(n, "rb").read())
EOF

say SIZES
find . -type f -printf '%s %p\n' | sort -k2
du -sb . data/raw data/processed
sh_ 'python scripts/column_stats.py data/processed/weather_valid.csv temp_c'
sh_ 'python scripts/column_stats.py data/raw/weather.csv temp_c'
sed -n 1,4p data/raw/daily_export.csv

# ---- the two copies of the opening ---------------------------------------
say HOOK
mkdir -p "$S/run/copies/smilte" "$S/run/copies/tomas"
cp data/raw/daily_export.csv "$S/run/copies/smilte/daily_export.csv"
sed 's/^1;2025-10-01;6,3$/1;2025-10-01;6,4/' data/raw/daily_export.csv > "$S/run/copies/tomas/daily_export.csv"
( cd "$S/run/copies"
  sh_ 'shasum -a 256 smilte/daily_export.csv tomas/daily_export.csv'
  sh_ 'wc -c smilte/daily_export.csv tomas/daily_export.csv'
  run git diff --no-index smilte/daily_export.csv tomas/daily_export.csv )

say HELLO
sh_ 'echo "hello" | git hash-object --stdin'
sh_ 'echo "hallo" | git hash-object --stdin'
sh_ 'printf "hello\r\n" | git hash-object --stdin'
sh_ 'echo "hello" | xxd'
sh_ 'printf "hello\r\n" | xxd'

say BLOB
run git hash-object data/raw/weather.csv
run git hash-object data/raw/daily_export.csv
cp data/raw/weather.csv "$S/run/copy-of-weather.csv"
run git hash-object "$S/run/copy-of-weather.csv"
sh_ 'shasum -a 256 data/raw/weather.csv'
sh_ 'shasum -a 256 data/raw/*'

# ---- first commits -------------------------------------------------------
say INIT
run git init
sh_ 'LC_ALL=C ls -a'
run git status
T 10:15
run git add README.md
run git status --short
run git commit -m "Add the README"
run git status --short
cat > .gitignore <<'EOF'
# made by the operating system
.DS_Store
Thumbs.db

# made by scripts/rebuild.sh
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
sh_ 'cat .git/HEAD'
sh_ 'cat .git/refs/heads/main'
sh_ 'wc -c .git/refs/heads/main'

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
run git status --short
C4=$(git rev-parse --short HEAD)
sh_ 'cat .git/refs/heads/main'
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
sh_ './scripts/rebuild.sh; echo "exit $?"'
T 10:50
run git revert --no-edit "$BAD"
run git log --oneline -3
run git show --stat HEAD
sh_ './scripts/rebuild.sh'

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
# push sends commits only: a staged edit stays on the laptop
echo "Draft: the wind column." >> README.md
git add README.md
run git status --short
run git push
git restore --staged README.md && git restore README.md

say CLONE
mkdir -p "$S/run/tomas" && cd "$S/run/tomas"
( export HOME="$S/run/tomas-home"
  run git clone "$URL"
  cd weather-project
  run git log --oneline -1
  sh_ 'ls data'
  sh_ './scripts/rebuild.sh'
  sh_ 'ls data'
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

# ---- two people, one repository: a push refused, a conflict ---------------
say REFUSED
( export HOME="$S/run/tomas-home"
  cd "$S/run/tomas/weather-project"
  sed -i '3,4c Ten years of hourly readings from one weather station, and the daily\nmeans of nine days of October 2025, typed into a spreadsheet from them.' README.md
  T 11:45
  git add README.md
  run git commit -m "Reword the first paragraph"
  run git push )
cd "$P"
sed -i '3,4c The hourly log of one weather station, 2016 to 2025, 87 672 hours, and a\ntable of daily mean temperatures typed into a spreadsheet from it.' README.md
T 11:50
git add README.md
run git commit -m "Give the number of hours in the first paragraph"
run git push
T 11:55
run git pull --no-edit
run git status
run git status --short
sed -n 1,10p README.md
python3 - <<'EOF'
import re
t = open("README.md", encoding="utf-8").read()
t = re.sub(r"<<<<<<< HEAD\n.*?>>>>>>> [0-9a-f]{40}\n",
           "Ten years of hourly readings from one weather station, 87 672 hours, and\n"
           "the daily means of nine days of October 2025, typed into a spreadsheet\nfrom them.\n",
           t, flags=re.S)
open("README.md", "w", encoding="utf-8").write(t)
EOF
sed -n 1,7p README.md
run git add README.md
# the message names the remote by its local path; GitHub's address in its place
sed -i "s#${REMOTE%.git}#${URL%.git}#" .git/MERGE_MSG
run git commit --no-edit
run git cat-file -p HEAD
run git log --oneline --graph -5
run git status
run git push
run git log --oneline --graph -4

# ---- a fork and a pull request -------------------------------------------
# GitHub's Fork button is a bare copy of the remote under Rūta's name; the
# merge button of the pull request is a merge commit by Smiltė, committed
# by GitHub. The lines `remote: ...` that GitHub adds to a push are not
# printed by a local remote: the slides add them as GitHub prints them.
say FORK
FORKURL="https://github.com/ruta-example/weather-project.git"
FORK="$S/run/remote/ruta-weather-project.git"
git clone -q --bare "$REMOTE" "$FORK"
mkdir -p "$S/run/ruta-home" "$S/run/ruta"
gitconfig "$S/run/ruta-home" "Rūta" "ruta@example.org"
printf '[url "%s"]\n\tinsteadOf = %s\n' "$FORK" "$FORKURL" >> "$S/run/ruta-home/.gitconfig"
fixf() { sed -e "s#$FORK#$FORKURL#g" -e "s#${FORK%.git}#${FORKURL%.git}#g" | fix; }
( export HOME="$S/run/ruta-home"
  cd "$S/run/ruta"
  echo "\$ git clone $FORKURL"; git clone "$FORKURL" 2>&1 | fixf
  cd weather-project
  echo "\$ git remote -v"; git remote -v 2>&1 | fixf
  run git switch -c ranges
  python3 - <<'EOF'
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
EOF
  run git diff --stat
  T 12:30
  git add README.md
  run git commit -m "Give the range of each column"
  echo "\$ git push -u origin ranges"; git push -u origin ranges 2>&1 | fixf
  run git status )
# the pull request #1, merged on GitHub by Smiltė
W="$S/run/github-merge"
git clone -q "$URL" "$W"
( cd "$W"
  git fetch -q "$FORK" ranges
  T 12:40
  GIT_COMMITTER_NAME=GitHub GIT_COMMITTER_EMAIL=noreply@github.com \
    git merge -q --no-ff -m "Merge pull request #1 from ruta-example/ranges" -m "Give the range of each column" FETCH_HEAD
  git push -q origin main
  run git cat-file -p HEAD )
cd "$P"
T 12:45
run git pull
run git log --oneline --graph -3

# ---- who edited the raw file ---------------------------------------------
say CLOSE
run git log --oneline -- data/raw
run git log --oneline -- data/raw/daily_export.csv
run git blame -s -L 2,2 data/raw/daily_export.csv
run git blame -L 2,2 data/raw/daily_export.csv
run git show "$TOM"
sh_ './scripts/rebuild.sh'
sh_ 'shasum -a 256 data/processed/daily.csv'
T 12:50
run git revert --no-edit "$TOM"
run git show --stat HEAD
sed -n 2p data/raw/daily_export.csv
sh_ './scripts/rebuild.sh'
sh_ 'shasum -a 256 data/processed/daily.csv'
run git push

say TAG
T 12:55
run git tag -a v1.0 -m "Data as received; mean 7.16 °C"
run git log --oneline -3
run git push origin v1.0
run git show v1.0 --stat
run git log --oneline --graph --all

say SIZE
du -sb .git; git count-objects -vH; git log --oneline | wc -l
