# Seminar 2 — Six Questions for One File

**Paired lecture:** 03 Command Line & File Handling · **Format:** exercises, in pairs · **~120 min**
(105 min in class, 15 min at home)

!!! abstract "Overview"
    **Time:** 17:15–19:00

    **Questions**

    - Can I answer a question about a data file with one line of my own?
    - Can someone else run my commands and get my answers?

    **After this seminar, students can**

    - move a downloaded file into the project with `mv`
    - build a pipeline of `cut`, `grep`, `sort`, `uniq` one stage at a time
    - save the pipelines in a script and write its output to a file

    **The room ends with:** `D0_KPi.csv` in `data/raw/`,
    `scripts/explore.sh`, `results/explore.txt`, and a **First look**
    section in the README.

    **Needs:** VS Code, a bash terminal, the `analysis-project` folder from
    [Seminar 1](seminar_01.md). No Python.

In the lecture the commands were typed at the front. Now the room types.
Blocks 1 and 2 are done together, step by step. From block 3 on the room
works in pairs and you walk round. After each block one pair shows its line
on the projector.

| Block | Clock | Min | The room ends with |
|--|--|--|--|
| [1. Check the terminal](#check) | 17:15 | 10 | A bash prompt in the project folder |
| [2. Put the data file in place](#data-file) | 17:25 | 15 | `D0_KPi.csv` in `data/raw/` |
| [3. Look at the file](#look) | 17:40 | 15 | Rows, bytes, first and last lines known |
| [4. Six questions](#questions) | 17:55 | 30 | Six answers, each from one line |
| [5. Save the commands](#script) | 18:25 | 15 | `scripts/explore.sh`, `results/explore.txt` |
| [6. Write it down](#readme) | 18:40 | 10 | A **First look** section in the README |
| [7. Wrap up](#wrap-up) | 18:50 | 10 | The homework known |

??? note "Before the session"
    - Check the solutions of blocks 3 and 4 on your own laptop.
    - A USB stick with `D0_KPi.csv` and the Git installer for Windows.
    - The terminal of VS Code at a font size that the last row can read:
      `Ctrl+=` (macOS `Cmd+=`).
    - Pairs: one laptop types, the other reads this page. They change
      places after each block.

## 1. Check the terminal { #check }

<p class="block-meta">17:15 · 10 min · together</p>

1. Open `analysis-project` in VS Code with **File** > **Open Folder...**.
2. Select **Terminal** > **New Terminal**.
3. **Windows only:** select the arrow next to the **+** of the terminal
   panel and choose **Git Bash**.

```bash title="Type"
pwd
ls
```

```text title="Output"
/c/Users/you/Documents/analysis-project
README.md  data  results  scripts
```

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The prompt begins with `PS` | This is PowerShell. Choose Git Bash as in step 3 |
    | No **Git Bash** in the list | Git is not installed. Install it from the USB stick, then close VS Code and open it again |
    | `pwd` shows the home folder | VS Code has no folder open. Repeat step 1 |
    | A student has no project folder | In **Documents**: `mkdir -p analysis-project/data/raw analysis-project/data/processed analysis-project/scripts analysis-project/results`, then step 1 |

!!! tip "Make Git Bash the default"
    Command Palette, type `default profile`, select
    **Terminal: Select Default Profile**, choose **Git Bash**.

## 2. Put the data file in place { #data-file }

<p class="block-meta">17:25 · 15 min · together</p>

The file is downloaded with the browser and moved with the shell. A student
who already has the file in `data/raw/` types the last line only.

1. Download [`D0_KPi.csv`](../data/D0_KPi.csv) with the browser. It lands in
   **Downloads**.

```bash title="Type"
ls ~/Downloads
mv ~/Downloads/D0_KPi.csv data/raw/
ls -l data/raw
```

```text title="Output"
total 3836
-rw-r--r-- 1 you you 3926142 Oct  6 17:31 D0_KPi.csv
```

**Check with the room:** the size is 3926142 on every laptop, and the Side
Bar of VS Code shows the file under `data/raw`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No such file or directory` | The browser saved the file under the name `D0_KPi (1).csv`, or elsewhere. `ls ~/Downloads` shows the name. A name with a space is written in quotes: `"D0_KPi (1).csv"` |
    | Another size than 3926142 | The download was cut off, or the file was saved from a spreadsheet. Download it again |
    | Windows: **Downloads** is not under `~` | OneDrive moved it. Drag the file onto `raw` in the Side Bar this once |

!!! success "Key points"
    - `mv` moves a file. Tab completes the names.
    - The size in bytes tells whether two copies can be the same file.

## 3. Look at the file { #look }

<p class="block-meta">17:40 · 15 min · in pairs</p>

Commands for this block: `wc`, `head`, `tail`, `less`.

!!! question "Exercise 3.1"
    How many lines does the file have? How many of them are rows of data?

??? success "Solution"
    ```bash
    wc -l data/raw/D0_KPi.csv
    ```

    91584 lines. One is the header, so 91583 rows.

!!! question "Exercise 3.2"
    What are the names of the columns? What are the last three rows?

??? success "Solution"
    ```bash
    head -n 1 data/raw/D0_KPi.csv
    tail -n 3 data/raw/D0_KPi.csv
    ```

    `M,PT,TAU,IPCHI2`. The last row begins with `1911.2631`.

!!! question "Exercise 3.3"
    How many bytes is one line, on average?

??? success "Solution"
    ```bash
    wc -c data/raw/D0_KPi.csv
    ```

    3926142 bytes in 91584 lines: about 43 bytes per line.

!!! question "Exercise 3.4"
    What does line 5000 of the file hold? `head -n 5000` gives lines 1 to
    5000. Send them on with a pipe.

??? success "Solution"
    ```bash
    head -n 5000 data/raw/D0_KPi.csv | tail -n 1
    ```

    `1868.8636,5537.248,0.0007151779,10.399748`

## 4. Six questions { #questions }

<p class="block-meta">17:55 · 30 min · in pairs</p>

Commands for this block: `cut`, `grep`, `sort`, `uniq`, `head`, `tail`,
`wc`, joined with `|`. Build each line one stage at a time and look at the
output after every stage.

For each question one pair shows its line. Two different lines with the
same answer are both right. Ask for them.

!!! question "Question 1"
    How many rows hold the code `-100`?

??? success "Solution"
    ```bash
    grep -c ',-100' data/raw/D0_KPi.csv
    ```

    49

!!! question "Question 2"
    On which line of the file is the first of them?

??? success "Solution"
    ```bash
    grep -n ',-100' data/raw/D0_KPi.csv | head -n 1
    ```

    Line 343.

!!! question "Question 3"
    What is the largest mass `M`, and on which line is it?

??? success "Solution"
    ```bash
    cut -d, -f1 data/raw/D0_KPi.csv | sort -g | tail -n 1
    grep -n '^2453.6584' data/raw/D0_KPi.csv
    ```

    2453.6584, on line 10048. It lies far outside the window of 1810 to
    1920 that holds all but four rows. Ask the room: is it an error, or a
    measurement? The file cannot say. The README should mention it.

!!! question "Question 4"
    What is the largest `PT`?

??? success "Solution"
    ```bash
    cut -d, -f2 data/raw/D0_KPi.csv | sort -g | tail -n 1
    ```

    64509.95

!!! question "Question 5"
    How many rows have a mass from 1860 to 1869? A line of such a row
    begins with `186`. In `grep`, `^` stands for the beginning of a line.

??? success "Solution"
    ```bash
    grep -c '^186' data/raw/D0_KPi.csv
    ```

    17496

!!! question "Question 6"
    Does the file hold the same row twice? `uniq -d` prints one line per
    group of equal neighbours.

??? success "Solution"
    ```bash
    sort data/raw/D0_KPi.csv | uniq -d
    ```

    It prints nothing. No row occurs twice.

!!! warning "Watch for"
    | On the screen | Reason |
    |--|--|
    | The largest mass is `M` | The header was sorted with the numbers. `sort -g` puts it first, plain `sort` puts it last |
    | `grep -c -100` gives an error | `grep` reads `-100` as an option. Write the text with the comma before it: `',-100'` |
    | Nothing happens and the prompt does not come back | The file name is missing, and the command waits for the keyboard. `Ctrl+C` |
    | `uniq -d` prints many lines | The lines were not sorted first |

!!! success "Key points"
    - A pipeline is built one stage at a time.
    - `sort -g` is the sort for measured values.
    - One question has several right lines.

## 5. Save the commands { #script }

<p class="block-meta">18:25 · 15 min · in pairs</p>

1. In the Side Bar create the file `scripts/explore.sh`.
2. **Windows only:** select `CRLF` in the Status Bar at the bottom right and
   choose **LF**.
3. Write a comment that says what the script is. Then, for each question, a
   line with `echo` that names it and the line that answers it.

```bash title="scripts/explore.sh, the beginning"
# First look at D0_KPi.csv. Run from the project folder:
#   bash scripts/explore.sh
FILE=data/raw/D0_KPi.csv

echo "1. Rows marked -100:"
grep -c ',-100' $FILE
```

```bash title="Type"
bash scripts/explore.sh
bash scripts/explore.sh > results/explore.txt
```

Open `results/explore.txt` in VS Code. It holds the six answers.

!!! warning "Watch for"
    | On the screen | Reason |
    |--|--|
    | `$'\r': command not found` | The file has Windows line endings. Step 2, then save |
    | `FILE: command not found` | Spaces around `=`. Write `FILE=data/raw/D0_KPi.csv` |
    | `No such file or directory` | The script was started from another folder. `pwd`, then `cd` to the project folder |

!!! success "Key points"
    - A script is the record of what was done to the file.
    - `>` writes the output of the whole script into one file.

## 6. Write it down { #readme }

<p class="block-meta">18:40 · 10 min · in pairs</p>

Add a section to `README.md` and fill it in from `results/explore.txt`.

```text title="README.md"
## First look

Made with `bash scripts/explore.sh`. The output is in `results/explore.txt`.

| Question | Answer |
|--|--|
| Rows of data | |
| Rows marked `-100` | |
| Largest mass | |
| Rows with a mass from 1860 to 1869 | |
| Rows that occur twice | |
```

!!! question "Exercise 6.1"
    Swap laptops with another pair. Run their script on your file. Does it
    print their answers?

??? success "Solution"
    It does, if their script uses the path `data/raw/D0_KPi.csv` and was
    started from the project folder. A script with a path such as
    `/c/Users/ona/...` works on one laptop only.

## 7. Wrap up { #wrap-up }

<p class="block-meta">18:50 · 10 min · together</p>

Put the homework on the projector. Then ask each pair for the command they
would not have guessed exists.

!!! success "Key points of the seminar"
    - The terminal and the Side Bar show the same folder.
    - A pipeline is built one stage at a time.
    - A script gives the same answers on another laptop.
    - Nothing was written into `data/raw/`.

!!! example "Homework · 15 min"
    1. Run three of the six questions on the dataset you chose after
       Seminar 1. Save them as `scripts/explore_mine.sh`.
    2. If the README has no record of where `D0_KPi.csv` came from, add the
       **Data** section from
       [Seminar 1, block 8](seminar_01.md#provenance).
    3. Read chapter 2 of
       [*Research Software Engineering with Python*](https://third-bit.com/py-rse/).

## Stretch goals

For pairs that finish a block early.

!!! question "Stretch 1"
    Write the 49 rows marked `-100` into
    `data/processed/invalid_tau.csv`, with the header as the first line.

??? success "Solution"
    ```bash
    head -n 1 data/raw/D0_KPi.csv > data/processed/invalid_tau.csv
    grep ',-100' data/raw/D0_KPi.csv >> data/processed/invalid_tau.csv
    wc -l data/processed/invalid_tau.csv
    ```

    50 lines.

!!! question "Stretch 2"
    Make a histogram of `M` in bins of 1 MeV in place of 10. Which three
    bins are the fullest?

??? success "Solution"
    ```bash
    cut -d, -f1 data/raw/D0_KPi.csv | cut -c1-4 | sort | uniq -c | sort -nr | head -n 3
    ```

    1862 with 1916 rows, 1865 with 1846, 1863 with 1830.

!!! question "Stretch 3"
    How many values in the file are written with an exponent, like
    `1.36e-05`? Show that `sort -n` and `sort -g` disagree on the smallest
    `IPCHI2`.

??? success "Solution"
    ```bash
    grep -c 'e-' data/raw/D0_KPi.csv
    cut -d, -f4 data/raw/D0_KPi.csv | sort -n | head -n 2
    cut -d, -f4 data/raw/D0_KPi.csv | sort -g | head -n 2
    ```

    Two values. `sort -n` gives 0.0001540074, `sort -g` gives
    1.3600341e-05.

!!! question "Stretch 4"
    Make a sample of the first 1000 rows, with the header, in
    `data/processed/sample_1000.csv`.

??? success "Solution"
    ```bash
    head -n 1001 data/raw/D0_KPi.csv > data/processed/sample_1000.csv
    wc -l data/processed/sample_1000.csv
    ```

    1001 lines.

## Aims practised

⚙️ commands saved as a script · ♻️ the same answers on another laptop · 📁 raw data read, never written · 🔧 the same shell on every system
