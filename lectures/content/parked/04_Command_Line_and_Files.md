<!--
Parked slides from slides/04_Command_Line_and_Files.md, taken out on 2026-10-06.

They left the deck when Git Bash was dropped: the terminal of the course is
zsh on macOS and PowerShell 7 on Windows, shown side by side, and only the
ideas both shells share stay in the lecture. The cleaning of the pendulum
table became the handed-out scripts/clean_pendulum.py. A comment before each
slide says where it stood. To restore one, move it back into the lecture file
and give it a PowerShell column.
-->

<!-- Parked 2026-10-06 from Lecture 04, section The Shell, after slide 'The Shell' (section): Git Bash dropped; the two shells are zsh and PowerShell 7 -->

---
hideInToc: true
---

# Open the **Terminal**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖥️ **In VS Code**

- **Terminal** > **New Terminal**. The Panel opens at the bottom, in the project folder
- The line that ends in `$` or `%` is the **prompt**: the terminal waits for a command
- Type a command and press `Enter`. It prints its answer, and the prompt comes back
- The `+` at the top right of the Panel opens one more terminal. The bin icon closes one

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows: Git Bash, set once**

1. `Ctrl+Shift+P`, type `default profile`
2. Select **Terminal: Select Default Profile**
3. Select **Git Bash**
4. Close the open terminal with the bin icon and open a new one. Its name at the top right reads `bash`

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔧 Git Bash came with the installation of Git. It gives Windows the commands that macOS and Linux have, so one set of commands serves every laptop. macOS and Linux need no change: their terminal runs `zsh` or `bash`.

</div>

<!--
Speaker: do the four steps on the projector even if your own laptop is a Mac:
open the Command Palette and show the entry. Ask who sees bash, who sees zsh,
and who still sees powershell. (~3 min)
-->


<!-- Parked 2026-10-06 from Lecture 04, section The Shell, after slide 'Keys That Save Typing': Git Bash dropped; the two shells are zsh and PowerShell 7 -->

---
hideInToc: true
---

# **Help**: `--help` and `man`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🪟 **Git Bash and Linux**

```text
$ wc --help
Usage: wc [OPTION]... [FILE]...
  or:  wc [OPTION]... --files0-from=F
...
```

Every program answers `--help` with its options. Git Bash has no `man`.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🍎 **macOS**

```text
$ man wc
NAME
     wc – word, line, character, and byte count
```

`man` opens the manual page. `Space` shows the next page, `/` and a word searches, `q` leaves.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

How to read the first line: `[OPTION]` in square brackets may be left out, `...` means that there may be several, and `FILE` in capitals is a place for your own value. `wc -l -c data/raw/D0_KPi.csv data/raw/pendulum.csv` fits the line: two options, two files.

</div>

<!--
Speaker: the programs are the same by name on macOS and in Git Bash, but they
come from two families, BSD and GNU. They differ in help and in a few options.
Where they differ in this lecture, both forms are on the slide. (~2 min)
-->



<!-- Parked 2026-10-06 from Lecture 04, section The Shell, after slide 'Read the Prompt': replaced by a side-by-side head -n 2 / Get-Content -Head 2 version; this ls -l version used the Git Bash $ prompt and its note claimed the room had read the byte size in Seminar 3 -->

---
hideInToc: true
---

# The Parts of a **Command**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ ls -l data/raw/D0_KPi.csv
-rw-r--r--  1 ada  staff  3926142 Sep 29 10:12 data/raw/D0_KPi.csv
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ⚙️ **Program**

`ls` is the first word. The shell looks for a program of that name and starts it.

</div>

<div class="card card-accent card-glass pad-compact">

## 🎚️ **Option**

`-l` changes how the program works: one line per file, with its size in bytes. An option starts with `-`.

</div>

<div class="card card-info card-glass pad-compact">

## 📄 **Argument**

`data/raw/D0_KPi.csv` says what to work on. A program can take several.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ A space ends an argument. `wc -l Pendulum Run 2.csv` names three files: `Pendulum`, `Run` and `2.csv`. This is the reason for the rule of Lecture 2: no spaces in names. Quotes hold a name with spaces together: `"Pendulum Run 2.csv"`.

</div>

<div class="note-text mt-sm">The <code>$</code> stands for the prompt and is not typed. Upper and lower case are different letters: <code>-l</code> is not <code>-L</code>.</div>

<!--
Speaker: the size, 3 926 142 bytes, is the number the room read off last week.
The user name and the date differ on every laptop. (~2 min)
-->


<!-- Parked 2026-10-06 from Lecture 04, section The Shell, after slide 'Help': replaced by two slides, A Command That Fails and A Path That Fails, for zsh and PowerShell 7; the cp data backup case has no PowerShell counterpart (Copy-Item without -Recurse succeeds and makes an empty folder) -->

---
hideInToc: true
---

# A Command That **Fails**

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ❓ **No such program**

```text
$ pyhton scripts/hello.py
zsh: command not found: pyhton
```

The first word is mistyped, or the program is not installed. The shell searched the folders listed in `PATH` and found none of that name.

</div>

<div class="card card-warning card-glass pad-compact">

## 📂 **No such file**

```text
$ wc -l data/raw/D0_KPi.cvs
wc: data/raw/D0_KPi.cvs: open:
No such file or directory
```

The path is wrong. Run `pwd`, then `ls`, and complete the name with `Tab`.

</div>

<div class="card card-warning card-glass pad-compact">

## 🧩 **Something is missing**

```text
$ cp data backup
cp: data is a directory
(not copied).
```

The program says what it could not do. Here it needs the option `-r`.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ The word before the first colon names who complains: the shell or a program. A command that works prints only what was asked for. `cp`, `mv`, `mkdir` and `rm` print nothing at all when they succeed.

</div>

<div class="note-text mt-sm">These are the messages of macOS. Git Bash words them differently: <code>bash: pyhton: command not found</code>.</div>

<!--
Speaker: make the three mistakes live and let the room read each message
aloud before you explain it. (~2 min)
-->


<!-- Parked 2026-10-06 from Lecture 04, section Pipes & Filters, after slide 'From data/raw to data/processed': the Unix-only text chain is dropped; the two shells are zsh and PowerShell 7, and only ideas both share stay in the lecture -->

---
hideInToc: true
---

# A Pipeline, **Stage by Stage**

<div class="card card-info card-glass pad-compact mt-sm">

Question: at which mass does the file have the most rows?

</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

1️⃣ `tail -n +2 data/raw/D0_KPi.csv` prints the rows without the header line

</div>

<div class="card card-secondary card-glass pad-compact">

2️⃣ `| cut -d, -f1` keeps the mass: `1880.649`

</div>

<div class="card card-accent card-glass pad-compact">

3️⃣ `| cut -c1-3` keeps its first three characters: `188`, which stands for 1880 to 1889.99

</div>

<div class="card card-success card-glass pad-compact">

4️⃣ `| sort | uniq -c` counts the rows in each step of 10 MeV/c²

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

```text
tail -n +2 data/raw/D0_KPi.csv | cut -d, -f1 | cut -c1-3 | sort | uniq -c
```

Run the line after every stage and read what comes out before the next stage is added.

</div>

<!--
Speaker: build it live, one stage at a time, with | head -n 3 at the end until
the last stage. Every mass in the file has four digits before the point, so
the first three characters are the same as a step of 10. (~3 min)
-->

<!-- Parked 2026-10-06 from Lecture 04, section Pipes & Filters, after slide 'A Pipeline, Stage by Stage': the cut | uniq histogram is zsh-only; the two shells are zsh and PowerShell 7 -->

---
hideInToc: true
---

# The Mass Column as a **Histogram**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧾 **The output**

```text
   1 176
   1 180
3716 181
7245 182
7384 183
7946 184
12207 185
17496 186
11388 187
7540 188
6790 189
6684 190
3183 191
   1 192
   1 245
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📊 **The same counts, drawn: █ = 600 rows**

```text
1760  ·
1800  ·
1810  ██████
1820  ████████████
1830  ████████████
1840  █████████████
1850  ████████████████████
1860  █████████████████████████████
1870  ███████████████████
1880  █████████████
1890  ███████████
1900  ███████████
1910  █████
1920  ·
2450  ·
```

</div>

</div>

<div class="card card-success card-glass pad-compact mt-sm">

The counts rise to 17 496 between 1860 and 1870 MeV/c²: the D⁰, whose mass is 1865. Below and above the peak about 7000 rows fall into each step. Four rows lie outside 1810 to 1920.

</div>

<!--
Speaker: five small programs and no plotting. The right-hand side is drawn by
hand from the left-hand numbers. Add | sort -n -r | head -n 3 to get the three
fullest steps: 186, 185, 187. (~2 min)
-->

<!-- Parked 2026-10-06 from Lecture 04, section Pipes & Filters, after slide 'The Mass Column as a Histogram': tr is zsh-only (Git Bash dropped; the two shells are zsh and PowerShell 7) -->

---
hideInToc: true
---

# Change Characters: `tr`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔁 **One character for another**

```text
$ head -n 2 data/raw/pendulum.csv | tr ',' '.'
nr;length_cm;t10_s
1;20;9.02
$ head -n 2 data/raw/pendulum.csv | tr ';' ','
nr,length_cm,t10_s
1,20,9,02
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **How it works**

- `tr A B` replaces every character `A` by the character `B`
- `tr -d A` deletes every `A`
- `tr -d '\r'` deletes the byte `0D`. A file with CRLF line endings comes out with LF
- `tr` takes no file name. It reads from a pipe

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`tr` is Replace All of Lecture 2 for single characters. The second command shows why the order mattered there: after `;` has become `,` the line `1,20,9,02` has three commas, and nothing tells the decimal one from the others.

</div>

<!--
Speaker: tr stands for translate. \r is how the shell writes the byte 0D, the
first half of the Windows line ending from Lecture 3. (~2 min)
-->

<!-- Parked 2026-10-06 from Lecture 04, section Pipes & Filters, after slide 'Change Characters: tr': the cleaning is now the handed-out scripts/clean_pendulum.py, run the same way in zsh and PowerShell 7 -->

---
hideInToc: true
---

# The Cleaning of Lecture 2, **in One Line**

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact table-compact">

## ✍️ **Edit by hand, and its filter**

| In the editor | In the shell |
| --- | --- |
| Delete the line with the mean | `grep -v mean` |
| Make every line ending LF | `tr -d '\r'` |
| Replace `,` by `.` | `tr ',' '.'` |
| Replace `;` by `,` | `tr ';' ','` |
| Delete the column `nr` | `cut -d, -f2,3` |

</div>

<div class="card card-primary card-glass pad-compact">

## ⌨️ **Joined by pipes**

```text
$ grep -v mean data/raw/pendulum.csv |
    tr -d '\r' | tr ',' '.' | tr ';' ',' |
    cut -d, -f2,3 | head -n 3
length_cm,t10_s
20,9.02
30,11.05
```

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

⚙️ Each filter does one edit to every line. The order is the order of Lecture 2: the decimal comma becomes a point while it is the only comma. The raw file is read and stays as it is. With `> data/processed/pendulum_script.csv` at the end, the output is a file.

</div>

<!--
Speaker: build it stage by stage as on the mass column and watch the last line
of the table change: 9;100;20,01 then 9;100;20.01 then 9,100,20.01 then
100,20.01. The stage tr -d does nothing on a Mac: the file has no 0D bytes.
On a Windows laptop it removes one per line. (~3 min)
-->


<!-- Parked 2026-10-06 from Lecture 04, section 'A First Script', after the section slide 'A First Script': Git Bash dropped; the two shells are zsh and PowerShell 7 (Lecture 2's cleaning as a bash script; replaced by the handed-out scripts/clean_pendulum.py) -->

---
hideInToc: true
---

# A Script Is a **File of Commands**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📜 **`scripts/clean_pendulum.sh`**

```bash
#!/usr/bin/env bash
# The hand edits of Lecture 2, as commands.
# Run from the project folder:
#   bash scripts/clean_pendulum.sh

grep -v mean data/raw/pendulum.csv |
  tr -d '\r' | tr ',' '.' | tr ';' ',' |
  cut -d, -f2,3 > data/processed/pendulum_script.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **What is in it**

- Plain text, made with **New File** in `scripts`. The name ends in `.sh`
- The commands stand as they were typed at the prompt
- `#` starts a comment. The shell skips the rest of that line
- Line 1 names the program that reads the file: `bash`

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

```text
$ bash scripts/clean_pendulum.sh
$ head -n 2 data/processed/pendulum_script.csv
length_cm,t10_s
20,9.02
```

</div>

<div class="note-text mt-sm">The script prints nothing: its output went into the file. Save a script with <code>LF</code> in the Status Bar. With <code>CRLF</code> the byte <code>0D</code> at the end of each line becomes part of the command.</div>

<!--
Speaker: make the file live, paste the pipeline from the terminal history, add
the comment lines. Point at LF in the Status Bar before saving. (~3 min)
-->

<!-- Parked 2026-10-06 from Lecture 04, section 'A First Script', after slide 'What 49 Rows Do to a Mean': Git Bash dropped; the two shells are zsh and PowerShell 7 (bash variables) -->

---
hideInToc: true
---

# **Variables**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🏷️ **A text under a name**

```bash
raw=data/raw/pendulum.csv
out=data/processed/pendulum_script.csv

grep -v mean "$raw" | tr -d '\r' |
  tr ',' '.' | tr ';' ',' |
  cut -d, -f2,3 > "$out"
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **The rules**

- `name=value` stores a text. No spaces around the `=`
- `$name` puts the text back in
- Inside double quotes, `"$name"`, the text stays one argument, also when it holds a space
- `$1` is the first word after the name of the script, `$2` the second

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

What may change stands once, at the top of the script: here the two paths. For the next table only two lines are edited, and the pipeline below them stays as it was tested.

</div>

<div class="note-text mt-sm">At the prompt: <code>name=pendulum</code>, then <code>echo "data/raw/$name.csv"</code> prints <code>data/raw/pendulum.csv</code>.</div>

<!--
Speaker: edit the script live to this form and run it again. The output file
is the same. (~2 min)
-->

<!-- Parked 2026-10-06 from Lecture 04, section 'A First Script', after slide 'Variables': Git Bash dropped; the two shells are zsh and PowerShell 7 (bash for loop) -->

---
hideInToc: true
---

# `for`: the Same Step for **Each File**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔂 **The loop**

```bash
for f in data/raw/*.csv; do
  echo "== $f"
  head -n 2 "$f"
done
```

- The wildcard gives the list of names
- The lines between `do` and `done` run once for each name
- `$f` holds the name of the turn

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧾 **What it prints**

```text
== data/raw/D0_KPi.csv
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
== data/raw/pendulum.csv
nr;length_cm;t10_s
1;20;9,02
```

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

⚙️ Two files or two thousand: the loop is the same four lines. Its output shows at a glance that the two raw files do not agree on the separator or on the decimal sign.

</div>

<!--
Speaker: type the four lines at the prompt. After the first line the prompt
changes: the shell waits for done. (~2 min)
-->

<!-- Parked 2026-10-06 from Lecture 04, section 'A First Script', after slide 'for: the Same Step for Each File': Git Bash dropped; the two shells are zsh and PowerShell 7 (bash-only script with a loop) -->

---
hideInToc: true
---

# A Script with a Loop: `ranges.sh`

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 📜 **`scripts/ranges.sh`**

```bash
#!/usr/bin/env bash
# Name, smallest and largest value
# of each of the four columns.
export LC_ALL=C
file=$1

for c in 1 2 3 4; do
  head -n 1 "$file" | cut -d, -f"$c"
  tail -n +2 "$file" | cut -d, -f"$c" |
    sort -g > results/column.txt
  head -n 1 results/column.txt
  tail -n 1 results/column.txt
done
rm results/column.txt
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧾 **What it prints**

```text
$ bash scripts/ranges.sh data/raw/D0_KPi.csv
M
1766.2096
2453.6584
PT
755.2686
64509.95
TAU
-100.0
0.5787994
IPCHI2
1.3600341e-05
891711.06
```

</div>

</div>

<!--
Speaker: read the script from the top with the room. Everything in the loop
body is a filter from the last section. The next slide takes the new parts one
by one. (~2 min)
-->

<!-- Parked 2026-10-06 from Lecture 04, section 'A First Script', after slide 'A Script with a Loop: ranges.sh': Git Bash dropped; the two shells are zsh and PowerShell 7 (reads the bash-only ranges.sh) -->

---
hideInToc: true
---

# Reading `ranges.sh`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🆕 **The new parts**

- `export LC_ALL=C` holds for every program the script starts: the decimal sign is the point
- `file=$1` takes the path from the command line
- `for c in 1 2 3 4` runs over four words. `-f"$c"` is the column of the turn
- `sort -g` reads `1.3600341e-05` as 0.000013600341. `sort -n` stops at the `e` and takes it for 1.36
- The sorted column goes into a file, because both its first and its last line are needed

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔎 **What the output says**

- `M` from 1766 to 2454: the two far rows again
- `PT` from 755 to 64 510
- `TAU` starts at `-100.0`: the mark for "no value" is the smallest "value" of the column
- `IPCHI2` from 0.0000136 to 891 711: over ten powers of ten, and a value written with an exponent

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Twelve lines of output are a description of the file: the names of the columns and the range of each. A mark for a missing value and a second way to write a number both show up at the ends.

</div>

<!--
Speaker: the exponent form is in two rows of the file. grep -n 'e-'
data/raw/D0_KPi.csv gives lines 40769 and 44745. (~3 min)
-->

<!-- Parked 2026-10-06 from Lecture 04, section Check Yourself, after the section slide 'Check Yourself': it tests shell globbing (the shell makes the list before ls starts), which holds in zsh but not in PowerShell, where Get-ChildItem expands the wildcard itself; the two shells are zsh and PowerShell 7 -->

---
hideInToc: true
---

<MCQ
  question="A folder contains run_1.log, run_12.log, run_A.log and notes.txt. What does `ls run_?.log` list?"
  :options="[
    'All four files',
    'run_1.log, run_12.log and run_A.log',
    'run_1.log and run_A.log',
    'Nothing, because ? is not a wildcard'
  ]"
  :correct="2"
  explanation="? fits exactly one character. run_1.log and run_A.log have one character between the underscore and the point. run_12.log has two, and notes.txt does not begin with run_. The shell makes this list before ls starts."
/>

<!-- Parked 2026-10-06 from Lecture 04, section Check Yourself, after the question 'The terminal is in analysis-project/results. Which path names the raw pendulum file?': the sort | uniq -c histogram chain is parked with the Unix-only text filters; the two shells are zsh and PowerShell 7 -->

---
hideInToc: true
---

<MCQ
  question="runs.txt has six lines: alpha, beta, alpha, gamma, alpha, beta. What does `sort runs.txt | uniq -c | sort -n -r | head -n 1` print?"
  :options="[
    '3 alpha',
    'alpha 3',
    '1 gamma',
    '6 runs.txt'
  ]"
  :correct="0"
  explanation="sort puts equal lines next to each other. uniq -c merges each group and writes the count in front. sort -n -r orders by the count, largest first, and head -n 1 keeps the first line. alpha occurs three times."
/>

<!-- Parked 2026-10-06 (final pass) from Lecture 04, section The Shell, after slide 'Keys That Save Typing': man and Get-Help are a detail the thread does not need; parked to bring the deck into the timing band -->

---
hideInToc: true
---

# **Help**: `man` and `Get-Help`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% man head
NAME
     head – display first lines of a file
SYNOPSIS
     head [-n count | -c bytes] [file ...]
```

`Space` shows the next page, `/` and a word searches, `q` leaves.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Help Get-Content
NAME
    Get-Content
SYNTAX
    Get-Content [-Path] <string[]>
    [-ReadCount <long>] [-TotalCount <long>]
    ...
```

`-Head` is a short name for `-TotalCount`.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Both pages use one notation. `[ ]` may be left out, `|` means one or the other, `...` and `[]` mean several, and `count` or `<long>` is a place for your own value. A fresh PowerShell has no help pages yet: it shows only this syntax and says so. `Get-Help Get-Content -Online` opens the full page in the browser. `Update-Help` downloads all pages once, and then `-Examples` prints the examples.

</div>

<!--
Speaker: read the SYNOPSIS line of head aloud and check that head -n 2 FILE
fits it. Programs that come from elsewhere answer --help in both shells the
same way: python --help, git --help. (~2 min)
-->

<!-- Parked 2026-10-06 (final pass) from Lecture 04, section Files & Folders, after slide 'Who Reads the `*`?': find by name and by size is off the thread of the lecture; parked to bring the deck into the timing band -->

---
hideInToc: true
---

# Search the Folders: `find` and `Get-ChildItem`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% find . -name '*.csv'
./data/processed/pendulum.csv
./data/raw/D0_KPi.csv
./data/raw/pendulum.csv
% find . -size +1M
./data/raw/D0_KPi.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-ChildItem -Recurse -Filter *.csv -Name
data\processed\pendulum.csv
data\raw\D0_KPi.csv
data\raw\pendulum.csv
PS> Get-ChildItem -Recurse -File |
>> Where-Object Length -gt 1MB |
>> Select-Object -ExpandProperty Name
D0_KPi.csv
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Both walk through the folder and every folder below it, at any depth. `data/*/*.csv` looks exactly two folders down. In zsh the quotes keep the shell from replacing `'*.csv'`, so `find` gets the pattern. PowerShell replaces nothing, so `-Filter *.csv` needs none.

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Windows has a `find` of its own, a program that searches for text inside files. Typed in PowerShell, `find . -name '*.csv'` answers `File not found - *.csv`.

</div>

<!--
Speaker: "where did I put it" for the whole home folder: find ~ -name
'pendulum*' or Get-ChildItem ~ -Recurse -Filter 'pendulum*'. It takes a while.
(~2 min)
-->

<!-- Parked 2026-10-06 (final pass) from Lecture 04, section Pipes & Filters, after slide 'The Ends of a Column': a side branch (locale) off the thread of bytes and checksums; parked to bring the deck into the timing band -->

---
hideInToc: true
---

# The **Decimal Sign** and the Language Setting

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cut -d, -f3 data/raw/D0_KPi.csv |
    LC_ALL=lt_LT.UTF-8 sort -n | head -n 1
-0.059467286
% cut -d, -f3 data/raw/D0_KPi.csv |
    LC_ALL=C sort -n | head -n 1
-100.0
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> [cultureinfo]::CurrentCulture = "lt-LT"
PS> [double]"1880.649"
1880,649
PS> [double]"1880,649"
1880649
```

</div>

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-warning card-glass pad-compact">

## 🇱🇹 **`sort -n` follows the language**

In Lithuanian the decimal sign is the comma, so `sort -n` does not take the point in `-0.059467286` as one, and the smallest value, `-100.0`, is not first. `LC_ALL=C` in front of a program switches the language rules off.

</div>

<div class="card card-warning card-glass pad-compact">

## 🌐 **`[double]` does not**

The cast reads the point on every computer, so `TAU` still sorts with `-100.0` first. Only the screen shows `1880,649`. A comma in the text is taken as a thousands separator: 1&nbsp;880&nbsp;649, and no error.

</div>

</div>

<div class="note-text mt-sm">The decimal comma of Lecture 2 again: there it was in a file, here it is a setting of the computer. <code>echo $LANG</code> and <code>(Get-Culture).Name</code> print the setting.</div>

<!--
Speaker: the left side is what sort -n does on a Mac set to Lithuanian; on a
laptop set to English both lines print -100.0. The first PowerShell line plays
a Windows laptop set to Lithuanian for this one window. Whole numbers are not
affected in either shell. (~3 min)
-->

<!-- Parked 2026-10-06 (final pass) from Lecture 04, section Regular Expressions, after slide 'Capture Groups': one regex slide fewer (greedy matching); parked to bring the deck into the timing band -->

---
hideInToc: true
---

# `.*` Takes **All It Can**

<div class="card card-info card-glass pad-compact mt-sm">

```text
1880.649,3000.9534,0.00041271152,1299.1675
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% grep -oE '^.*,' data/raw/D0_KPi.csv |
    head -n 2
M,PT,TAU,
1880.649,3000.9534,0.00041271152,
% grep -oE '^[^,]*' data/raw/D0_KPi.csv |
    head -n 2
M
1880.649
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Get-Content data/raw/D0_KPi.csv -Head 2 |
    Select-String '^.*,').Matches.Value
M,PT,TAU,
1880.649,3000.9534,0.00041271152,
PS> (Get-Content data/raw/D0_KPi.csv -Head 2 |
    Select-String '^[^,]*').Matches.Value
M
1880.649
```

</div>

</div>

<div class="card card-primary card-glass pad-compact mt-md">

`^.*,` runs to the **last** comma: three fields, not one. `*` and `+` take as many characters as they can while the rest of the pattern still fits. `^[^,]*` cannot run past a comma, so it stops at the **first** one. A pattern for one field says what the field may not contain.

</div>

<!--
Speaker: this is the usual first surprise with regular expressions. In the
table-row pattern of the last slide it did no harm, because the cleaned file
has one comma per line. Both shells print only the part that matched: grep
with -o, and PowerShell with .Matches.Value, the matched part of what
Select-String hands on. (~2 min)
-->

<!-- Parked 2026-10-06 (final pass) from Lecture 04, section Checksums & Backups, after slide 'The Script Against the Hand': a second copy.csv demo; its 107 bytes and C06D... checksum moved into 'Where 107 Bytes Come From' -->

---
hideInToc: true
---

# Same Numbers, **Other Bytes**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cat data/processed/pendulum.csv > copy.csv
% wc -c copy.csv
      97 copy.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Content data\processed\pendulum.csv |
>>   Set-Content copy.csv
PS> (Get-Item copy.csv).Length
107
```

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

```text
% shasum -a 256 copy.csv
be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  copy.csv

PS> (Get-FileHash copy.csv).Hash
C06D1344B6A39F3895FB0A7F0067EC0B2F4CA94D71F7F57F57981F5BF102106D
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

PowerShell on Windows ends every line it writes with CRLF, `0D 0A` (Lecture 3): ten lines, ten more bytes, another checksum. `clean_pendulum.py` writes LF on every system, so its output is `be05af03…` on every laptop.

</div>

<!--
Speaker: question first: "if I clean the table on Windows and you on a Mac,
do we get the same checksum?" Same ten lines, written by each shell: same
numbers, other bytes, other checksum. 107 bytes is also the size of the
Seminar 3 checkpoint pendulum_crlf.csv (same hash, C06D…): an editor on
Windows that saves with CRLF gives the same file. Delete copy.csv afterwards
(rm copy.csv or Remove-Item copy.csv). (~2 min)
-->

<!-- Parked 2026-10-06 (final pass) from Lecture 04, section Checksums & Backups, after slide 'Backups: the 3-2-1 Rule': backup routine details; parked to bring the deck into the timing band -->

---
hideInToc: true
---

# A Backup Is a **Routine**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📋 **Five answers, written down once**

| | For the project folder |
| --- | --- |
| What | The whole folder. It is small: 4 MB |
| When | At the end of every session of work |
| How | One command, the same every time |
| Check | The list of checksums, run on the copy |
| Test | Open the copy on another computer |

</div>

<div class="card card-warning card-glass pad-compact">

## ☁️ **A synced folder is not an older copy**

OneDrive, iCloud Drive, Google Drive or Dropbox keep a copy in another place. A file deleted or overwritten on the laptop is deleted or overwritten there within seconds. A dated folder on a drive stays as it was on that day.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

🧮 The laptop, a USB drive kept at home and a synced folder: three copies, on three kinds of storage, two of them in another place. That meets 3-2-1, and of the three only the USB drive keeps older copies.

</div>

<!--
Speaker: a backup that was never opened is a hope, not a backup. The five
answers go into the README; the next slide is the "How" and the "Check".
(~1 min)
-->

<!-- Parked 2026-10-06 (final pass) from Lecture 04, section Checksums & Backups, after slide 'A Backup Is a Routine' (also parked): backup routine details; parked to bring the deck into the timing band -->

---
hideInToc: true
---

# A Backup to a **USB Drive**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cp -R . /Volumes/USB/project_2026-10-13
% cd /Volumes/USB/project_2026-10-13
% shasum -a 256 -c data/checksums.txt
data/raw/D0_KPi.csv: OK
data/raw/pendulum.csv: OK
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Copy-Item -Recurse . E:\project_2026-10-13
PS> cd E:\project_2026-10-13
PS> $list = Get-Content data\checksums.txt
PS> $now = (Get-FileHash data\raw\*).Hash
PS> Compare-Object $list $now
PS>
```

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💾 `.` is the folder the terminal is in, the project. The copy is a new folder with the date in its name, so last week's copy stays as it was. The check on the copy takes a second: this is the moment the list of checksums was written for.

</div>

<div class="note-text mt-sm">macOS shows a drive named <code>USB</code> under <code>/Volumes/USB</code>; Windows gives it a letter, here <code>E:</code>. The terminal now stands on the drive: <code>cd</code> back to the project folder before the next command.</div>

<!--
Speaker: run it live to a stick if one is at hand. The checksum list travels
with the folder, because it is inside data. (~2 min)
-->
