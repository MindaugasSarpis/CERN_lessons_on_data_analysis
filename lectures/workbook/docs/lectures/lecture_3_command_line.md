# Lecture 3 — Command Line & File Handling

!!! abstract "Overview"
    **Time:** 15:00–17:00, 110 min of teaching and a break of 10 min

    **Questions**

    - How do I move through folders and handle files without a mouse?
    - How do I ask a data file a question in one line?
    - How do I keep the commands, so that I can run them again?

    **After this lecture, students can**

    - say where they are in the file tree and move through it
    - make, copy, move and delete files and folders
    - read a file of any size with `head`, `tail`, `less`, `wc`
    - join `cut`, `grep`, `sort`, `uniq` with a pipe
    - save commands as a script and run it

    **Needs:** VS Code, a bash terminal, the `analysis-project` folder.
    Slides: `03-command-line-and-files`.

This lecture is typed. A slide names an idea, then you show it in the
terminal on `D0_KPi.csv`. Students may type along. It follows Software
Carpentry, [*The Unix Shell*](https://swcarpentry.github.io/shell-novice/),
episodes 1 to 4 and 6.

| Block | Clock | Min | Slides |
|--|--|--|--|
| [1. The shell](#shell) | 15:00 | 21 | 1–9 |
| [2. The file tree](#tree) | 15:21 | 20 | 10–15 |
| [3. Files and folders](#files) | 15:41 | 14 | 16–20 |
| Break | 15:55 | 10 | |
| [4. Looking inside a file](#inside) | 16:05 | 11 | 21–23 |
| [5. Pipes and filters](#pipes) | 16:16 | 32 | 24–31 |
| [6. A script](#script) | 16:48 | 12 | 32–35 |
| Break, then [Seminar 2](../seminars/seminar_02.md) | 17:00 | 15 | |

??? note "Before the session"
    - Your terminal: bash, in the `analysis-project` folder, font size set
      with `Ctrl+=`. Type `clear` before each block.
    - Windows laptops need Git Bash, which is installed with Git. Bring the
      Git installer on a USB stick.
    - The students of 2026 do not have `D0_KPi.csv` in `data/raw/` yet. In
      blocks 4 to 6 they watch, or follow if they have the file. Seminar 2
      starts by moving the file into place.
    - Start the slides: `node scripts/serve-local.mjs 8123`, then open
      `http://localhost:8123/03-command-line-and-files/`.

??? note "How to type in front of a room"
    - Say the command aloud before typing it, and say what you expect.
    - Type slowly. Use no shortcut that you have not shown.
    - After a command, wait and ask: who sees the same? Go on when about
      four in five do.
    - Leave your errors in. Read the message aloud, then correct the line.
    - Do not clear the screen while the room is still typing.

## 1. The shell { #shell }

<p class="block-meta">15:00 · 21 min · slides 1–9</p>

**Say.** Last week every question about the file was answered by clicking,
and nothing of it was recorded. A shell is a program that reads a line of
text and runs it. Everything typed today can be saved and run again.

**Check the room first.** Every laptop shows a prompt that ends in `$`.
Windows: arrow next to **+** in the terminal panel > **Git Bash**.

```bash title="Type"
whoami
date
echo hello
pwd
ls
```

```text title="Output"
you
Tue Oct  6 15:12:40 EEST 2026
hello
/c/Users/you/Documents/analysis-project
README.md  data  results  scripts
```

**Then show** the parts of a command on `ls -l -h data/raw`: the command,
the options, the argument.

**Make both errors on purpose** and read them aloud.

```bash title="Type"
pwdd
ls data/row
```

```text title="Output"
bash: pwdd: command not found
ls: cannot access 'data/row': No such file or directory
```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The prompt begins with `PS` | PowerShell. Choose **Git Bash** |
    | No **Git Bash** in the list | Git is not installed. The student shares a screen now and installs in the break |
    | `pwd` shows the home folder | VS Code has no folder open: **File** > **Open Folder...** |

!!! success "Key points"
    - The terminal is the window, the shell reads the line, a command is a
      program.
    - A command is a name, options that begin with `-`, and arguments,
      separated by spaces.
    - An error message names the program and what it complains about.

## 2. The file tree { #tree }

<p class="block-meta">15:21 · 20 min · slides 10–15</p>

**Say.** All files of a computer are in one tree of folders. A path names a
place in the tree. It is absolute if it starts at the root or at `~`, and
relative if it starts where you are.

```bash title="Type"
cd data/raw
pwd
ls
cd ..
pwd
cd ~
cd -
cd ..
```

```text title="Output"
/c/Users/you/Documents/analysis-project/data/raw
D0_KPi.csv
/c/Users/you/Documents/analysis-project/data
```

**Show Tab.** Type `cd da` and press Tab. The shell completes the name. A
name that does not complete does not exist.

```bash title="Type"
ls -l data/raw
```

```text title="Output"
total 3836
-rw-r--r-- 1 you you 3926142 Sep 29 20:51 D0_KPi.csv
```

**Read the line** with the room: kind and permissions, owner, size in
bytes, date, name.

!!! question "Exercise · slide 15 · 3 min"
    You are in `analysis-project/data/raw`. Which command takes you to
    `analysis-project/scripts`?

    1. `cd scripts`
    2. `cd ../scripts`
    3. `cd ../../scripts`
    4. `cd /scripts`

??? success "Solution"
    Number 3. The first `..` leads up to `data`, the second to
    `analysis-project`, and `scripts` is inside that.

!!! success "Key points"
    - `pwd` says where you are, `ls` what is there, `cd` moves.
    - `..` is one folder up, `~` is the home folder, `cd -` goes back.
    - Tab completes a name and checks its spelling.

## 3. Files and folders { #files }

<p class="block-meta">15:41 · 14 min · slides 16–20</p>

**Say.** Four commands make, copy, move and delete. The shell has no
recycle bin and no undo.

```bash title="Type"
mkdir -p data/processed/tmp
cp data/raw/D0_KPi.csv data/processed/tmp/
ls data/processed/tmp
cd data/processed/tmp
mv D0_KPi.csv copy.csv
cp copy.csv copy2.csv
ls *.csv
rm copy2.csv
cd ../../..
rm -r data/processed/tmp
```

```text title="Output"
D0_KPi.csv
copy.csv  copy2.csv
```

**Show the Side Bar of VS Code after each step.** It is the same folder.

**Ask before the last line:** what does `pwd` say now?

!!! warning "Watch for"
    A student who runs `rm -r data` in place of `rm -r data/processed/tmp`.
    The file is downloaded again in the seminar. Tell the room: this is
    the reason for running `ls` first.

!!! success "Key points"
    - `mkdir -p`, `cp`, `mv`, `rm`. `mv` with a new name is a rename.
    - `*` stands for any characters. Run `ls` with a pattern before `rm`
      with the same pattern.
    - `data/raw` is read, never written to.

## 4. Looking inside a file { #inside }

<p class="block-meta">16:05 · 11 min · slides 21–23</p>

**Say.** These commands read only what they show. They answer at once on a
file of any size.

```bash title="Type"
wc -l data/raw/D0_KPi.csv
wc -c data/raw/D0_KPi.csv
head -n 3 data/raw/D0_KPi.csv
tail -n 2 data/raw/D0_KPi.csv
```

```text title="Output"
91584 data/raw/D0_KPi.csv
3926142 data/raw/D0_KPi.csv
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
1860.6599,2803.4126,0.0001864154,0.34182164
1871.4323,2541.8845,0.0001756544,6.866581
1911.2631,2543.4617,0.00017650973,8.169813
```

**Ask:** 91 584 lines and 3 926 142 bytes. How many bytes is one line? Does
that fit the line on the screen? It is about 43, and it does.

!!! success "Key points"
    - `wc -l` counts lines, `wc -c` bytes.
    - `head` and `tail` show the two ends, `less` pages through, `q` leaves.
    - Check that the size of a file fits its number of rows.

## 5. Pipes and filters { #pipes }

<p class="block-meta">16:16 · 32 min · slides 24–31</p>

**Say.** A program reads lines from its input and writes lines to its
output. `>` sends the output to a file. `|` sends it to the next program.
Build a line one stage at a time, and look at the output after each stage.

### The smallest decay time

**Ask before the sort:** what is the smallest decay time you expect?

```bash title="Type"
cut -d, -f3 data/raw/D0_KPi.csv | head -n 3
cut -d, -f3 data/raw/D0_KPi.csv | sort -g | head -n 4
grep -c ',-100' data/raw/D0_KPi.csv
grep -n ',-100' data/raw/D0_KPi.csv | head -n 2
```

```text title="Output"
TAU
0.00041271152
0.0001864154
TAU
-100.0
-100.0
-100.0
49
343:1818.1002,2978.644,-100.0,9901.186
965:1902.8027,2740.8074,-100.0,45169.31
```

### Three sorts, three answers

Slide 29. The smallest `IPCHI2`, asked two ways:

| Command | First value |
|--|--|
| `sort -n` | `0.0001540074` |
| `sort -g` | `1.3600341e-05` |

Two rows in 91 583 are written with an exponent. `sort -n` stops reading at
the `e`.

### A histogram without a plot

```bash title="Type"
cut -d, -f1 data/raw/D0_KPi.csv | cut -c1-3 | sort | uniq -c
```

```text title="Output"
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
      1 M
```

**Say.** This is last week's histogram, in bins of 10 MeV/c², made without
a plot. The peak is in `186`.

!!! question "Exercise · slide 31 · 3 min"
    `runs.txt` holds six lines: alpha, beta, alpha, gamma, alpha, beta.
    What does this print?

    ```bash
    sort runs.txt | uniq -c | sort -nr | head -n 1
    ```

??? success "Solution"
    `3 alpha`. `sort` brings equal lines together, `uniq -c` writes each
    group as a count and a value, `sort -nr` puts the largest count first.

!!! warning "Watch for"
    | On the screen | Reason |
    |--|--|
    | Nothing happens, no prompt | The file name is missing and the command waits for the keyboard. `Ctrl+C` |
    | `sort data.csv > data.csv` | It empties the file. Say it, do not show it on the data file |

!!! success "Key points"
    - `cut` takes columns, `grep` takes lines, `sort` orders, `uniq -c`
      counts neighbours.
    - Measured values are sorted with `sort -g`.
    - `>` replaces a file. Write to a new name, never into `data/raw`.

## 6. A script { #script }

<p class="block-meta">16:48 · 12 min · slides 32–35</p>

**Say.** A script is a text file with the commands, one per line. It is the
record of what was done to the data.

**Write in the VS Code editor,** not in the terminal.

```bash title="scripts/explore.sh"
# First look at the example file.
# Run from the project folder:
#   bash scripts/explore.sh
FILE=data/raw/D0_KPi.csv

echo "Lines:"
wc -l $FILE
echo "Rows marked -100:"
grep -c ',-100' $FILE
echo "Rows per 10 MeV:"
cut -d, -f1 $FILE | cut -c1-3 | sort | uniq -c
```

```bash title="Type"
bash scripts/explore.sh
bash scripts/explore.sh > results/explore.txt
ls results
```

```text title="Output"
Lines:
91584 data/raw/D0_KPi.csv
Rows marked -100:
49
Rows per 10 MeV:
      1 176
...
explore.txt
```

!!! warning "Watch for"
    | On the screen | Reason |
    |--|--|
    | `$'\r': command not found` | Windows line endings. Select `CRLF` in the Status Bar, choose **LF**, save |
    | `FILE: command not found` | Spaces around `=` |

!!! success "Key points"
    - A line that begins with `#` is a comment.
    - `FILE=...` names the path, `$FILE` uses it.
    - `bash scripts/explore.sh` runs the file from top to bottom.

## If time runs short

| Half | Cut, in this order | Saves |
|--|--|--|
| First | The exercise on slide 15 | 3 min |
| First | In block 3 type `mkdir`, `cp`, `rm` only | 3 min |
| Second | The exercise on slide 31 | 3 min |
| Second | The typing in block 6. Seminar 2 writes the script | 7 min |

Do not cut block 5. Seminar 2 uses both pipelines.

## For students to read

- [*Research Software Engineering with Python*](https://third-bit.com/py-rse/),
  chapters 2 and 3
- Slides 36 to 73 of the deck are extra material: `find`, `grep` in depth,
  loops, file naming, backups
