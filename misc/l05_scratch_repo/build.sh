#!/usr/bin/env bash
# Scratch repository for Lecture 05: the project folder after Seminar 4,
# put under Git on 20 Oct 2026 by the lecturer. Every git output on the
# slides comes from one run of this script.
#
# Usage: bash misc/l05_scratch_repo/build.sh [outdir]   (needs git, python3,
# shasum, unzip). It writes outdir/run/ and prints every command with its
# output. Rerun it whenever lectures/workbook/docs/data/cli_clean_pendulum.py
# changes: the tree and commit ids on the L05 slides depend on its bytes.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
S="${1:-$HERE}"   # output folder: run/ is made inside it (gitignored)
DATA="$HERE/../../lectures/workbook/docs/data"
rm -rf "$S/run" && mkdir -p "$S/run/home"
export HOME="$S/run/home" GIT_CONFIG_NOSYSTEM=1 LC_ALL=C TZ=Europe/Vilnius
cat > "$HOME/.gitconfig" <<'EOF'
[user]
	name = Mindaugas Sarpis
	email = mindaugas.sarpis@cern.ch
[init]
	defaultBranch = main
[pull]
	rebase = false
[core]
	autocrlf = false
	pager = cat
[advice]
	detachedHead = true
[log]
	decorate = short
EOF
P="$S/run/analysis-project"
mkdir -p "$P"/data/raw "$P"/data/processed "$P"/scripts "$P"/results
cd "$P"
unzip -p "$DATA/project_after_s1.zip" analysis-project/results/report.md > results/report.md
cp "$DATA/pendulum_plot.png" results/pendulum_plot.png
cp "$DATA/D0_KPi.csv" data/raw/D0_KPi.csv
cp "$DATA/pendulum_raw.csv" data/raw/pendulum.csv
cp "$DATA/pendulum.csv" data/processed/pendulum.csv
cp "$DATA/cli_clean_pendulum.py" scripts/clean_pendulum.py
cp "$DATA/cli_column_stats.py" scripts/column_stats.py
printf 'print("ready")\n' > scripts/hello.py
python3 scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv
grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv
shasum -a 256 data/raw/* > data/checksums.txt
cat > README.md <<'EOF'
# Analysis Project

Seminar exercises for the course
*Best Research and Data Analysis Practices from CERN*.

The example data is from the [CERN Open Data Portal](https://opendata.cern.ch).

## About

- **Author:** Mindaugas Sarpis
- **Started:** 2026-09-29

## Folders

| Folder | What goes in |
|--|--|
| `README.md` | what the project is and where the data came from |
| `data/raw` | files exactly as downloaded, never edited |
| `data/processed` | cleaned versions, made by scripts |
| `scripts` | code |
| `results` | figures and numbers that the code produces |

## Data

- **Source:** CERN Open Data Portal, record 401
- **Address:** https://opendata.cern.ch/record/401
- **DOI:** 10.7483/OPENDATA.LHCb.E7EJ.JUWR
- **Licence:** CC0
- **Fetched:** 2026-09-29
- **File:** `data/raw/D0_KPi.csv`, converted from the record's
  `MasterclassData.root` by the course's `root_to_csv.py`
- **Size:** 3 926 142 bytes, 91 583 rows, 4 columns
- **One row:** one candidate pair of a kaon and a pion from one collision

- **File:** `data/raw/pendulum.csv`, from a lab partner, 2026-09-29
- **Cleaned copy:** `data/processed/pendulum.csv`, 97 bytes,
  SHA-256 `be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b`

Checksums of `data/raw`: `data/checksums.txt`.

## Columns of `D0_KPi.csv`

| Column | Meaning | Unit |
|--|--|--|
| `M` | mass of the K⁻π⁺ pair | MeV/c² |
| `PT` | transverse momentum | MeV/c |
| `TAU` | decay time | ns |
| `IPCHI2` | χ² of the impact parameter | none |

Missing value: `TAU` is `-100.0` in 49 rows.

## How to rebuild

Run in the project folder: zsh on macOS, PowerShell 7 on Windows.
On macOS the program is `python3`.

1. The cleaned pendulum table, 97 bytes, SHA-256 `be05af03…`:
   `python scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv`
2. `D0_KPi.csv` without the 49 rows marked `-100`, 91 535 lines:
   - zsh: `grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv`
   - PowerShell: `Select-String ',-100' data/raw/D0_KPi.csv -NotMatch -Raw > data/processed/D0_valid.csv`
EOF
T() { export GIT_AUTHOR_DATE="2026-10-20T$1:00+0300" GIT_COMMITTER_DATE="2026-10-20T$1:00+0300"; }
say() { echo; echo "##### $*"; }
run() { echo "\$ $*"; "$@" 2>&1; }

say SIZES
find . -type f -not -path './.git/*' -printf '%s %p\n' | sort -k2
du -sb --exclude=.git .
ls data/raw; wc -l README.md
run git hash-object data/raw/D0_KPi.csv
run git hash-object data/processed/pendulum.csv

say HOOK
mkdir -p "$S/run/copies/13oct" "$S/run/copies/20oct"
cp data/processed/pendulum.csv "$S/run/copies/13oct/pendulum.csv"
sed 's/^20,9.02$/20,9.03/' data/processed/pendulum.csv > "$S/run/copies/20oct/pendulum.csv"
( cd "$S/run/copies" && run shasum -a 256 13oct/pendulum.csv 20oct/pendulum.csv && wc -c 13oct/pendulum.csv 20oct/pendulum.csv && run git diff --no-index 13oct/pendulum.csv 20oct/pendulum.csv )
( cd "$S/run/copies" && cp "$DATA/pendulum_crlf.csv" copy.csv && cp 13oct/pendulum.csv pendulum.csv && run git hash-object pendulum.csv copy.csv && run git diff --no-index --stat pendulum.csv copy.csv )
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

# made by the commands in README.md
data/processed/D0_valid.csv
data/processed/pendulum_script.csv
EOF
T 10:20
run git add .gitignore
run git commit -m "Add .gitignore"
run git add .
run git status
run git status --ignored --short
T 10:25
run git commit -m "Add the data, the report and the scripts"
C3=$(git rev-parse HEAD)
say MODEL
run git cat-file -p HEAD
run git cat-file -p 'HEAD^{tree}'
run git cat-file -p HEAD:data
run git cat-file -p HEAD:data/raw
cat data/checksums.txt
run git cat-file -s HEAD
run git cat-file -p HEAD~2
git cat-file commit HEAD | git hash-object -t commit --stdin
echo "obj D0:"; ls -l .git/objects/4a/
run git log --oneline
for c in HEAD HEAD~1 HEAD~2; do git rev-parse "$c^{tree}"; git ls-tree "$c" README.md; done
cat .git/HEAD; cat .git/refs/heads/main; wc -c .git/refs/heads/main

say FETCH
cat >> README.md <<'EOF'

## Data not stored here

- **File:** `MasterclassData.root`, 1 289 541 bytes, the original of `D0_KPi.csv`
- **Fetch from:** https://opendata.cern.ch/record/401
- **SHA-256:** `8694a2ed518472b02994629154de3077fdff4aef1065691fa13ae9f6b23b039b`
EOF
T 10:30
git add README.md
run git commit -m "Say how to fetch the ROOT file"
cat .git/refs/heads/main

say DIFF
sed -i 's/^Time of 10 swings for nine lengths\.$/Time of 10 swings of a pendulum for nine lengths./' results/report.md
run git diff
T 10:40
git add results/report.md
run git diff --staged --stat
run git commit -m "Name the pendulum in the report"
run git log --oneline
run git log -1 HEAD
run git show --stat --oneline HEAD
run git blame -s -L 1,5 results/report.md
run git log --oneline -- results/report.md

say RESTORE
sed -i '/^| [2-6]0 |/d' results/report.md
run git diff --stat
run git restore results/report.md
run git status

say AMEND
sed -i 's/^20,9.02$/20,9.03/' data/processed/pendulum.csv
run git diff
run shasum -a 256 data/processed/pendulum.csv
T 10:45
git add data/processed/pendulum.csv
run git commit -m "Use 9.03 s for 20 cm, as in teh lab book"
BAD1=$(git rev-parse --short HEAD)
export GIT_COMMITTER_DATE="2026-10-20T10:46:00+0300"
run git commit --amend -m "Use 9.03 s for 20 cm, as in the lab book"
BAD=$(git rev-parse --short HEAD)
say REVERT
T 10:55
run git revert --no-edit "$BAD"
run git log --oneline -3
run git cat-file -p HEAD
run shasum -a 256 data/processed/pendulum.csv

say STASH
echo "draft" >> results/report.md
run git stash
run git status
run git stash pop
git restore results/report.md
say PUSH
mkdir -p "$S/run/remote"
git init -q --bare "$S/run/remote/analysis-project.git"
run git remote add origin "$S/run/remote/analysis-project.git"
run git remote -v
run git push --progress -u origin main
run git count-objects -vH

say CLONE
cd "$S/run" && mkdir laptop2 && cd laptop2
run git clone --progress "$S/run/remote/analysis-project.git"
cd analysis-project
run git log --oneline -1
ls data/raw
sed -i 's/^- \*\*Started:\*\* 2026-09-29$/- **Started:** 2026-09-29\n- **Under Git since:** 2026-10-20/' README.md
T 11:00
git add README.md
run git commit -m "Note when version control started"
run git push
cd "$P"
T 11:02
run git pull

say BRANCH
run git switch -c table-units
run git branch
cat .git/HEAD
sed -i 's/^| length_cm | t10_s |$/| length (cm) | time of 10 swings (s) |/' results/report.md
T 11:05
git add results/report.md
run git commit -m "Write the units into the table header"
run git switch main
run git merge table-units
run git branch -d table-units

say CONFLICT
run git switch -c wording
sed -i '3s/.*/Ten swings of a pendulum, timed for nine lengths./' results/report.md
T 11:10
git add results/report.md
run git commit -m "Reword the first sentence"
run git switch main
sed -i '3s/.*/Time of 10 swings of a pendulum for nine lengths from 20 cm to 100 cm./' results/report.md
T 11:15
git add results/report.md
run git commit -m "Give the range of lengths"
run git log --oneline --graph --all -4
T 11:20
run git merge wording
sed -n 1,9p results/report.md
sed -i '3,7d' results/report.md
sed -i '3i Ten swings of a pendulum, timed for nine lengths from 20 cm to 100 cm.' results/report.md
sed -n 1,6p results/report.md
git add results/report.md
run git commit -m "Merge branch 'wording'"
run git cat-file -p HEAD
run git log --oneline --graph -5
run git status
run git log --oneline --all
say TAG
T 11:25
run git push
run git tag -a v1.0 -m "Report as shown on 20 October"
run git log --oneline -2
run git push origin v1.0
say CLOSE
run git log --oneline -- data/processed/pendulum.csv
run git log -2 -- data/processed/pendulum.csv
run git show --stat --oneline "$BAD"
run git blame -s -L 2,2 data/processed/pendulum.csv
say SIZE
du -sb .git; du -sk .git; git count-objects -v
git log --oneline | wc -l
