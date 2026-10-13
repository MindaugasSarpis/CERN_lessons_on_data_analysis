---
layout: cover
title: "Command Line & File Handling"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Command Line & File Handling

##### <span class="aims-badge">⚙️ automation · 📁 data & files · 🔧 tool-agnostic</span>

<!--
**Say:** today one number is checked, and every step of the check is a typed line.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# A step that was typed can be written down, checked and run again. Today **7.16 °C** is checked by typed lines

<!--
**Say:** a click leaves nothing behind. A typed line can be pasted into a README, read by someone else and run again on the next file.
(~1 min)
-->

---
hideInToc: true
---

# The Number to **Check**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📁 **weather-project**

```text
weather-project/
├─ README.md
├─ data/
│  ├─ raw/        weather.csv
│  │              daily_export.csv
│  └─ processed/
├─ scripts/       clean_export.py
│                 column_stats.py
└─ results/
```

The whole folder: <a href="../workbook/data/weather_project.zip" download>weather_project.zip</a>, 565 KB

</div>

<div class="card card-warning card-glass pad-compact">

## ✉️ **Smiltė's e-mail**

The mean air temperature at the station, 2016 to 2025: **7.16 °C**.

`weather.csv` has one row per hour. Some hours had no reading; I left them out.

</div>

</div>

<!--
**Say:** Smiltė's number from the first lecture, and the folder she sent with it. `data/raw` holds the files as they arrived; nothing writes there.
**Ask:** what would you do first to check 7.16?
(~2 min)
-->

---
hideInToc: true
---

# The Check, Step by **Step**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Step | Question about 7.16 | Answer |
| --- | --- | --- |
| 1 | Which columns does `weather.csv` have, and which one is the temperature? | ? |
| 2 | Does it hold every hour of ten years? | ? |
| 3 | Which rows are not measurements? | ? |
| 4 | Is every other row a measurement? | ? |
| 5 | What is the mean without those rows, and with them? | ? |
| 6 | Does a second program give the same mean? | ? |
| 7 | Is my `weather.csv` the file Smiltė used? | ? |
| 8 | Can anyone run the whole check again? | ? |

</div>

<div class="note-text mt-md">Every answer comes from a typed line: in zsh on macOS, in Git Bash on Windows, almost always the same line.</div>

<!--
**Say:** one question per part of the lecture. The answer column fills up as we go; it closes the lecture.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The **Shell**

Step 1: a shell on every laptop, and the columns of the file.

<!--
(~1 min)
-->

---
hideInToc: true
---

<div class="grid-3 gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖥️ **Terminal**

The window. It passes what is typed to the shell and shows what comes back.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🐚 **Shell**

A program that reads a typed line, runs what the line names, and waits for the next line: zsh, bash.

</div>

<div class="card card-accent card-glass pad-compact">

## ⚙️ **Program**

A file the computer can run: `head`, `grep`, `python`, `git`. The shell itself is one.

</div>

</div>

<div class="card card-info card-glass pad-compact table-compact mt-md">

| | Comes with the system | This course |
| --- | --- | --- |
| macOS | zsh, in the app Terminal | zsh |
| Windows | Windows PowerShell 5.1 | Git Bash: bash and the Unix commands, installed with Git |

</div>

<!--
**Say:** the terminal is only the window. The shell inside it does the work. zsh and bash are close relatives: almost every line of today runs in both unchanged.
**If asked:** Linux usually has bash. Windows PowerShell is a different family of shell; the course uses it only for the first install lines on Windows.
(~2 min)
-->

---
hideInToc: true
---

# What the Shell Does with a **Line**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ head -n 2 data/raw/weather.csv
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| | The shell | On this line |
| --- | --- | --- |
| 1 | waits for `Enter`, then reads the line | the whole line |
| 2 | splits it into words at the spaces | 4 words; `"weather station.csv"` in quotes stays one |
| 3 | replaces what it knows: `$HOME`, `~`, `*.csv` | nothing here |
| 4 | finds the program the first word names | `head`, the file `/usr/bin/head` |
| 5 | starts it with the other words, shows its output | the first 2 lines of the file |
| 6 | keeps its exit status in `$?`, prints the prompt | `$` again |

</div>

<!--
**Say:** every line today goes through these six steps. Step 2 is why a space in a file name breaks a line: the shell sees two names.
**If asked:** `cd` is no program: the shell does it itself, a builtin. A program cannot change the shell's folder.
(~2 min)
-->

---
hideInToc: true
---

# macOS: Homebrew, Git and **Miniforge**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **In the app Terminal**

```text
% echo $SHELL
/bin/zsh
% /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Installation successful!
% brew install git
% brew install --cask miniforge
% conda init zsh
```

</div>

<div class="note-text mt-md">zsh is the shell of every Mac since 2019. Homebrew is a package manager for macOS: it installs a program by name. Then Git, then Miniforge, which brings Python and <code>conda</code>.</div>

<!--
**Say:** typed once per laptop. `conda init zsh` lets zsh find `conda` and `python` in every new terminal.
**If asked:** the Homebrew installer asks for the Mac's login password, and nothing appears while it is typed. On Apple Silicon it ends with "Next steps": two lines to paste, which put `/opt/homebrew/bin` on the list of folders the shell searches. An account older than 2019 may still start bash: `chsh -s /bin/zsh`.
(~3 min)
-->

---
hideInToc: true
---

# Windows: Git Bash with **winget**

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🪟 **In Windows PowerShell: Start, `PowerShell`**

```text
PS C:\Users\smilte> winget install --id Git.Git -e
Found Git [Git.Git] Version 2.56.0
…
Successfully installed
PS C:\Users\smilte> winget install --id CondaForge.Miniforge3 -e
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

🖥️ Then in VS Code: `Ctrl+Shift+P`, **Terminal: Select Default Profile**, **Git Bash**. In the new Git Bash terminal: `conda init bash`, and open a new terminal.

</div>

<!--
**Say:** winget is the package manager that comes with Windows; `--id` names the package, `-e` asks for that exact id. Git for Windows brings Git Bash: bash with `ls`, `grep`, `head` and the rest. After this, Windows PowerShell is not needed again.
**If asked:** winget asks once to accept its source agreements: `Y`. A university laptop may ask for an administrator password. Git's installer offers many choices; the defaults are right.
(~3 min)
-->

---
hideInToc: true
---

# Read the **Prompt**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
smilte@MacBook-Air weather-project % ls
README.md  data  results  scripts
```

User and computer, the folder, `%`.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · Git Bash**

```text
smilte@LAPTOP MINGW64 ~/Documents/weather-project
$ ls
README.md  data/  results/  scripts/
```

User and computer, `MINGW64`, the folder; `$` on the next line.

</div>

</div>

<div class="note-text mt-md">The folder in the prompt is the <strong>working directory</strong>: every path on a line starts there. On the slides a line starts with <code>$</code> and works in both shells; zsh prints <code>%</code> there.</div>

<!--
**Ask:** read the two prompts aloud, part by part.
**Say:** `~` is the home folder. Git Bash marks folders with `/` in `ls`.
**If asked:** MINGW64 names the Unix layer that Git for Windows runs on.
(~2 min)
-->

---
hideInToc: true
---

# The Commands of Lecture 03

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| To | zsh · Git Bash |
| --- | --- |
| see where the shell is | `pwd` |
| list a folder | `ls data/raw` |
| change folder, one up, home | `cd data`, `cd ..`, `cd ~` |
| make a folder | `mkdir -p data/processed` |
| copy, move or rename | `cp FROM TO`, `mv FROM TO` |
| delete, no undo | `rm FILE`, `rm -r FOLDER` |
| read a file | `cat data/raw/daily_export.csv` |
| measure a file in bytes | `wc -c data/raw/weather.csv` |
| look at its bytes | `xxd data/processed/daily.csv` |

</div>

<!--
**Say:** nothing new here: Lecture 03 typed these. They are the same words in zsh and in Git Bash.
**If asked:** `-p` makes `mkdir` quiet when the folder exists and makes the folders above it too. `hexdump` is on a Mac but not in Git Bash; `xxd` is in both.
(~2 min)
-->

---
hideInToc: true
---

# Move Around: `pwd`, `ls`, `cd`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ pwd
/Users/smilte/Documents/weather-project
$ ls
README.md  data  results  scripts
```
```text
$ pwd
/Users/smilte/Documents/weather-project
$ cd data/raw
$ pwd
/Users/smilte/Documents/weather-project/data/raw
$ ls
daily_export.csv  weather.csv
```
```text
$ pwd
/Users/smilte/Documents/weather-project/data/raw
$ cd ../..
$ pwd
/Users/smilte/Documents/weather-project
$ head -n 1 data/raw/weather.csv
time,temp_c,humidity_pct,wind_ms
```
````

</div>

<div class="note-text mt-md"><code>data/raw</code> and <code>../..</code> are <strong>relative</strong> paths: they start at the working directory, so they are the same on every laptop. An <strong>absolute</strong> path names one user on one computer: <code>/Users/smilte/…</code> on a Mac, <code>/c/Users/smilte/…</code> in Git Bash.</div>

<!--
**Ask:** after `cd data/raw`, what will `pwd` print? And after `cd ../..`?
**Say:** the terminal stays in `weather-project` from here on, and every path on the slides starts there.
**If asked:** `.` is the folder the shell is in, `..` the one above, `~` the home folder.
(~3 min)
-->

---
hideInToc: true
---

# The Parts of a **Command**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ head -n 2 data/raw/weather.csv
```

<v-click>

```text
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
```

</v-click>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ⚙️ **Program**

The first word: `head`.

</div>

<div class="card card-accent card-glass pad-compact">

## 🎚️ **Option**

How to work, a dash and a letter, often with a value: `-n 2`.

</div>

<div class="card card-info card-glass pad-compact">

## 📄 **Argument**

What to work on: the path.

</div>

</div>

<!--
**Ask:** what will this print? The first two lines of the file.
**Say:** options come before the arguments. `-n` and `-N` are different options: case counts.
**If asked:** every option of a program is in its help: `man head` on a Mac, `head --help` in Git Bash, which has no `man`.
(~2 min)
-->

---
hideInToc: true
---

# What the Shell **Replaces**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ file=data/raw/weather.csv
$ echo $file
data/raw/weather.csv
$ head -n 1 $file
time,temp_c,humidity_pct,wind_ms
```
```text
$ echo $HOME
/Users/smilte
$ echo ~
/Users/smilte
$ echo data/raw/*.csv
data/raw/daily_export.csv data/raw/weather.csv
```
````

</div>

<div class="card card-info card-glass pad-compact mt-md">

A **variable** is a name the shell keeps a value under: `name=value`, no spaces around `=`; `$name` reads it. Before the program starts, the shell replaces `$name`, `~` and `*`.

</div>

<!--
**Ask:** what will `echo data/raw/*.csv` print? The shell, not `echo`, finds the two names.
**Say:** step 3 of the shell, made visible with `echo`: `echo` only prints its arguments, and they arrive already replaced.
**If asked:** in Git Bash `$HOME` is `/c/Users/smilte`.
(~3 min)
-->

---
hideInToc: true
---

# Complete Names with `Tab`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⌨️ **Type a start, press `Tab`**

```text
head -n 2 da          Tab →  head -n 2 data/
head -n 2 data/r      Tab →  head -n 2 data/raw/
head -n 2 data/raw/w  Tab →  …/raw/weather.csv
```

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **No typing mistakes**

A name that `Tab` completed exists. If `Tab` adds nothing, no name fits: the line is wrong before it runs.

</div>

</div>

<div class="card card-info card-glass pad-compact table-compact mt-md">

| `↑` `↓` | `Ctrl+R` | `Ctrl+C` | `Ctrl+A`, `Ctrl+E` | `clear` |
| --- | --- | --- | --- | --- |
| the earlier lines | search them | stop what runs | start, end of the line | empty the window |

</div>

<!--
**Live:** type `head -n 2 da`, then `Tab` three times, `Enter`; then `↑` brings the line back.
**Ask:** count the keys: how many were typed, how many did Tab add?
**If asked:** with two names that fit, a second Tab lists them.
(~3 min)
-->

---
hideInToc: true
---

# Read an Error **Message**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% hed -n 2 data/raw/weather.csv
zsh: command not found: hed
% head -n 2 data/raw/wether.csv
head: data/raw/wether.csv: No such
file or directory
% head -n 2 weather station.csv
head: weather: No such file or directory
head: station.csv: No such file or
directory
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · Git Bash**

```text
$ hed -n 2 data/raw/weather.csv
bash: hed: command not found
$ head -n 2 data/raw/wether.csv
head: cannot open 'data/raw/wether.csv'
for reading: No such file or directory
$ head -n 2 weather station.csv
head: cannot open 'weather' for reading:
No such file or directory
head: cannot open 'station.csv' for
reading: No such file or directory
```

</div>

</div>

<div class="note-text mt-md">The word before the first colon says who complains: the shell found no program, or the program found no file. The third line: a space split one name into two.</div>

<!--
**Ask:** what went wrong in each line? Let the room read before you explain.
**Say:** an error message is an answer. Read it before retyping.
(~2 min)
-->

---
hideInToc: true
---

# The Columns of `weather.csv`

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Column | Value on line 2 | Meaning |
| --- | --- | --- |
| `time` | `2016-01-01T00:00` | the hour, as year-month-day, `T`, hour:minute |
| `temp_c` | `-4.4` | air temperature, °C |
| `humidity_pct` | `93` | relative humidity, % |
| `wind_ms` | `2.5` | wind speed, m/s |

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 1: four columns, separated by commas, named on line 1. The temperature is column 2, `temp_c`.

</div>

<!--
**Say:** the time is written largest unit first, ISO 8601. That order also sorts correctly as text.
**Ask:** what does `T` stand for? Time: it separates the date from the hour.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Read and **Count**

Step 2: does the file hold every hour of ten years?

<!--
(~1 min)
-->

---
hideInToc: true
---

# Read the Two Ends of a **File**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ head -n 3 data/raw/weather.csv
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
```
```text
$ tail -n 2 data/raw/weather.csv
2025-12-31T22:00,-9.9,98,4.1
2025-12-31T23:00,-11.3,100,4.2
```
````

</div>

<div class="note-text mt-md">The header, the first hour and the last: the log runs from midnight of New Year 2016 to 23:00 on New Year's Eve 2025, one row per hour.</div>

<!--
**Ask:** what will the last line of the file be? Midnight before New Year 2026 is 2025-12-31 at 23:00.
**Say:** the ends of a file tell how far it goes. They do not tell whether an hour in the middle is missing; a count does.
(~2 min)
-->

---
hideInToc: true
---

# One Line, Byte by **Byte**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ sed -n 2p data/raw/weather.csv | xxd
```

<v-click>

```text
00000000: 3230 3136 2d30 312d 3031 5430 303a 3030  2016-01-01T00:00
00000010: 2c2d 342e 342c 3933 2c32 2e35 0a         ,-4.4,93,2.5.
```

</v-click>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 16 + 13 = 29 bytes: 28 characters, each one byte in ASCII, and `0a`, the line break LF. `,` is `2c`, `-` is `2d`, `.` is `2e`. `wc -l` counts the `0a` bytes; `wc -c` counts all bytes.

</div>

<!--
**Ask:** how many bytes will this line take? Count the characters with the room: 28, and one more.
**Say:** `sed -n 2p` prints line 2 only; `xxd` shows each byte in hex, 16 to a row, and the characters on the right, with `.` for the line break.
**If asked:** a file written with CRLF would end the line in `0d 0a`, 30 bytes.
(~3 min)
-->

---
hideInToc: true
---

# How Many Lines? Predict, Then **Count**

<div class="card card-info card-glass pad-compact mt-sm">

🧮 2016, 2020 and 2024 are leap years: 7 × 365 + 3 × 366 = 3653 days, and 3653 × 24 = 87 672 hours. With the header: **87 673 lines**.

</div>

<v-click>

<div class="card card-primary card-glass pad-compact mt-md">

## 💻 **zsh · Git Bash**

```text
$ wc -l data/raw/weather.csv
87673 data/raw/weather.csv
$ wc -c data/raw/weather.csv
2515215 data/raw/weather.csv
```

</div>

</v-click>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 2: 87 673 lines, every hour of ten years. 2 515 215 bytes: a line such as `2016-01-01T00:00,-4.4,93,2.5` is 28 characters and its LF, 29 bytes; 28.7 on average.

</div>

<!--
**Live:** `wc -l data/raw/weather.csv`, after the prediction.
**Ask:** how many lines should a file of ten years of hours have? Work it out with the room before the click.
**Say:** the count agrees with the calendar, so no hour is missing and none is there twice. Rows can still be wrong, but there are as many as there should be.
**If asked:** on a Mac `wc` pads its number with spaces. `wc`, word count: `-l` lines, `-w` words, `-c` bytes.
(~4 min)
-->

---
layout: section
hideInToc: true
---

# Pipes & **Filters**

Step 3: which rows are not measurements?

<!--
**Say:** small programs, each doing one thing, joined so that one's output is the next one's input.
(~1 min)
-->

---
hideInToc: true
---

# Output and Errors Are Two **Streams**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ head -n 3 data/raw/weather.csv > results/first.txt
$ wc -c results/first.txt
91 results/first.txt
$ head -n 3 data/raw/wether.csv > results/none.txt
head: cannot open 'data/raw/wether.csv' for reading: No such file or directory
$ wc -c results/none.txt
0 results/none.txt
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📤 **Standard output**

What a program prints. `>` writes it into a file, and first **empties** that file. `>>` adds at the end.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Standard error**

Errors go on their own stream and still reach the screen. `2>` writes them into a file.

</div>

</div>

<!--
**Say:** 91 bytes are the three lines: 33 + 29 + 29. The failed line made an empty file: `>` emptied it before anything came. Every program also reads a third stream, standard input: the keyboard, or a pipe.
**If asked:** never write into the file a command reads: `>` empties it first.
(~2 min)
-->

---
hideInToc: true
---

# Standard Input: `<` and the **Pipe**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ wc -l data/raw/weather.csv
87673 data/raw/weather.csv
```
```text
$ wc -l data/raw/weather.csv
87673 data/raw/weather.csv
$ wc -l < data/raw/weather.csv
87673
```
```text
$ wc -l data/raw/weather.csv
87673 data/raw/weather.csv
$ wc -l < data/raw/weather.csv
87673
$ cat data/raw/weather.csv | wc -l
87673
```
````

</div>

<div class="card card-info card-glass pad-compact mt-md">

📥 Every program has three streams: **standard input**, standard output, standard error. Given a file name, `wc` opens the file and prints its name. With `<`, the shell opens the file and hands it to `wc` as standard input; with `|`, another program's output is its input. Then `wc` never learns a name.

</div>

<!--
**Ask:** before the second step: why would the name disappear from the output?
**Say:** a filter reads standard input and writes standard output, so it fits anywhere in a pipe. That is the whole idea of the pipe.
**If asked:** the keyboard is standard input when nothing else is given: `wc -l` alone waits for typed lines, `Ctrl+D` ends them.
(~3 min)
-->

---
hideInToc: true
---

# Which Hour Is on Line **5000**?

<div class="grid-2 mt-sm gap-md">

<div class="card card-info card-glass pad-compact">

🧮 Line 2 is 2016-01-01 00:00, so line 5000 is 4998 hours later: 4998 = 208 × 24 + 6.

January to June 2016: 31 + 29 + 31 + 30 + 31 + 30 = 182 days. 208 − 182 = 26 days after 1 July: **27 July, 06:00**.

</div>

<div class="card card-primary card-glass pad-compact">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ head -n 5000 data/raw/weather.csv
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
…
2016-07-27T06:00,18.2,71,1.1
```
```text
$ head -n 5000 data/raw/weather.csv | tail -n 1
2016-07-27T06:00,18.2,71,1.1
```
````

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔗 **`A | B`**

The standard output of `A` becomes the standard input of `B`. No file stands between them.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧩 **A filter**

A program that reads its input and passes on part of it: 5000 lines in, 1 out.

</div>

</div>

<!--
**Live:** `head -n 5000 data/raw/weather.csv`, then `↑` and add `| tail -n 1`.
**Ask:** before the arithmetic: in which month will line 5000 fall? Collect two or three guesses.
**Say:** a prediction worked out by hand, then checked by a pipe. Two programs, each simple, answer a question neither answers alone, as `f(g(x))` composes functions. Both run at once: `tail` reads while `head` writes.
(~4 min)
-->

---
hideInToc: true
---

# The Lowest Humidity: Text or **Numbers**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ tail -n +2 data/raw/weather.csv | cut -d, -f3 | sort | head -n 1
```

<v-click>

```text
100
```

</v-click>

<v-click>

```text
$ tail -n +2 data/raw/weather.csv | cut -d, -f3 | sort -n | head -n 1
34
```

</v-click>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ `sort` compares text character by character, and `1` comes before `3`. `sort -n` compares numbers. `tail -n +2` leaves out the header; `cut -d, -f3` keeps field 3, humidity.

</div>

<!--
**Ask:** what is the lowest humidity in ten years? Then: why does the line say 100?
**Say:** a pipe carries lines of text. Each program in it reads lines and writes lines.
**Ask:** where would `9` stand in a text sort of 34, 9 and 100? Last.
(~3 min)
-->

---
hideInToc: true
---

# The Coldest Hour, Filter by **Filter**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ cut -d, -f2 data/raw/weather.csv | head -n 3
temp_c
-4.4
-4.8
```
```text
$ tail -n +2 data/raw/weather.csv | cut -d, -f2 | head -n 3
-4.4
-4.8
-5.5
```
```text
$ tail -n +2 data/raw/weather.csv | cut -d, -f2 | sort -n | head -n 3
-999
-999
-999
```
```text
$ sort -t, -k2,2n data/raw/weather.csv | head -n 3
2019-07-22T00:00,-999,76,3.2
2019-07-22T01:00,-999,81,3.0
2019-07-22T02:00,-999,80,3.4
```
````

</div>

<div class="card card-warning card-glass pad-compact mt-md">

❓ The coldest hours of ten years: −999 °C, at midnight in July. Nothing is that cold: −273.15 °C is the lowest temperature there is. −999 is a mark the logger wrote for "no value".

</div>

<!--
**Live:** build it in the terminal, `↑` and one filter more each time.
**Ask:** before the third step: what will the coldest hour of ten years be? Most say about −20 °C.
**Say:** a sorted column shows its ends first, and a wrong value usually sits at an end. The last step sorts whole rows by field 2 as a number: `-t,` the separator, `-k2,2n` the key. The other columns of those rows look normal: only the thermometer was down.
**If asked:** `tail -n 1` in place of `head -n 3` gives the warmest hour, 2018-06-18 at 15:00, 32.4 °C.
(~4 min)
-->

---
hideInToc: true
---

# Keep Rows by a Condition: `awk`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ awk -F, '$2 < -273.15' data/raw/weather.csv | wc -l
120
$ awk -F, 'NR > 1 && ($2 < -50 || $2 > 50)' data/raw/weather.csv | wc -l
120
```

</div>

<div class="card card-info card-glass pad-compact table-compact mt-md">

| `-F,` | `$2` | `NR` | `<` `>` `==` | `&&` | `\|\|` |
| --- | --- | --- | --- | --- | --- |
| the separator | field 2 | the line number | compare | both | either |

</div>

<div class="note-text mt-md">Physics, without knowing the mark: below absolute zero, −273.15 °C, is impossible. 120 rows. A wider test, outside −50 to 50 °C for a station like this, finds the same 120 and no others.</div>

<!--
**Say:** `awk` runs a small program on every line and prints the lines for which the condition is true. A test by what is possible finds a mark that nobody told us about.
**If asked:** `NR > 1` leaves out the header: compared as text, `temp_c` counts as greater than 50. On macOS `wc -l` pads the 120 with spaces.
(~2 min)
-->

---
hideInToc: true
---

# Find Rows with a Text: `grep`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ grep -c ',-999,' data/raw/weather.csv
120
$ grep -n ',-999,' data/raw/weather.csv | head -n 1
31154:2019-07-22T00:00,-999,76,3.2
$ grep -n ',-999,' data/raw/weather.csv | tail -n 1
31273:2019-07-26T23:00,-999,66,1.9
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 Lines 31 154 to 31 273: 31 273 − 31 154 + 1 = 120 lines, 22 to 26 July 2019, five days of 24 hours. One block, no gap.

</div>

<!--
**Say:** `grep` keeps the lines that contain a text: `-c` counts them, `-n` puts the line number in front.
**If asked:** keep the commas in `',-999,'`: they make sure the whole value is −999, and not part of a longer number.
(~2 min)
-->

---
hideInToc: true
---

# Every Year, Every Day, Every **Hour**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ cut -c1-4 data/raw/weather.csv | uniq -c
      1 time
   8784 2016
   8760 2017
   8760 2018
   8760 2019
   8784 2020
   …
```
```text
$ tail -n +2 data/raw/weather.csv | cut -c1-10 | uniq | wc -l
3653
```
```text
$ tail -n +2 data/raw/weather.csv | cut -c1-10 | uniq -c | grep -vc ' 24 '
0
```
```text
$ cut -d, -f1 data/raw/weather.csv | sort | uniq -d | wc -l
0
```
````

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 3: 8760 rows a year, 8784 in a leap year; 3653 days, none with more or fewer than 24 rows; no hour twice. The only rows that are not measurements are the 120 of −999, 22 to 26 July 2019.

</div>

<!--
**Say:** `cut -c1-4` keeps the year, `cut -c1-10` the date. `uniq -c` counts equal lines that stand next to each other; `uniq -d` prints only lines that occur twice; `grep -v` keeps the lines without the text. The count of step 2 could come out right with one hour missing and another twice: these lines rule that out. 2019 has all its 8760 rows: the mark sits where the number should be.
**If asked:** on a Mac `uniq -c` pads its counts less.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Regular **Expressions**

Step 4: is every other row a measurement?

<!--
**Say:** `',-999,'` found one fixed text. A different mark, an empty value or `NA` would have been missed. A pattern describes what a good row looks like.
(~1 min)
-->

---
hideInToc: true
---

# Hours Below **Freezing**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ grep -c ',-' data/raw/weather.csv
22472
```

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ `,-` is also in the 120 rows of `,-999,`. A fixed text cannot say "a minus, then a number with a decimal". A **regular expression** can.

</div>

<!--
**Ask:** is 22 472 the number of hours below freezing? Wait for "the −999 rows".
**Say:** a regular expression, regex for short, is a text with signs in it that describe many texts.
(~2 min)
-->

---
hideInToc: true
---

# Signs for **One Character**

<div class="card card-primary card-glass pad-compact mt-sm">

| Sign | Fits | Example |
| --- | --- | --- |
| `7`, `T`, `,` | itself | `T16` fits `T16` |
| `.` | any one character | `T..:` fits `T00:`, `T23:` |
| `[0-9]` | one digit | `,[0-9]` fits `,9` |
| `\.` | a point, nothing else | `4\.4` fits `4.4` only |

</div>

<div class="note-text mt-md">The backslash takes the special meaning away from the sign after it.</div>

<!--
**Say:** read the table row by row with the example line `2016-01-01T00:00,-4.4,93,2.5` on the board.
(~2 min)
-->

---
hideInToc: true
---

# A Point Fits **Any Character**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ grep -c '7.16' data/raw/weather.csv
600
$ grep -n '7.16' data/raw/weather.csv | head -n 2
162:2016-01-07T16:00,-0.3,72,4.4
402:2016-01-17T16:00,0.5,80,5.6
$ grep -c '7\.16' data/raw/weather.csv
0
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 `7.16` fits `7T16` (days 7, 17, 27 at 16:00: 360 lines) and `7-16` (every hour of 16 July: 240 lines).

</div>

<!--
**Ask:** before the count: how many lines will `'7.16'` find? The room usually says none.
**Say:** a pattern that runs can still find the wrong lines. Check the count, and look at two of the lines.
(~2 min)
-->

---
hideInToc: true
---

# Signs for **How Many** and **Where**

<div class="card card-primary card-glass pad-compact mt-sm">

| Sign | Means | Example |
| --- | --- | --- |
| `+` | one or more of the sign before | `[0-9]+` fits `4`, `93`, `2016` |
| `?` | the sign before, or nothing | `-?4` fits `4` and `-4` |
| `^` | the start of the line | `^2016` fits the 8 784 hours of 2016 |

</div>

<div class="note-text mt-md"><code>grep -E</code> reads <code>+</code> and <code>?</code> as signs; plain <code>grep</code> takes them as text.</div>

<!--
**Say:** `+` and `?` act on the one sign just before them.
**If asked:** `*` is "none or more", `$` the end of the line, `{4}` exactly four.
(~2 min)
-->

---
hideInToc: true
---

# Below Freezing, One Sign at a **Time**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ grep -c ',-' data/raw/weather.csv
22472
```
```text
$ grep -cE ',-[0-9]+,' data/raw/weather.csv
120
```
```text
$ grep -cE ',-[0-9]+\.[0-9],' data/raw/weather.csv
22352
```
````

</div>

<v-click>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| Pattern | Fits | Lines |
| --- | --- | --- |
| `,-` | a comma and a minus | 22 472 |
| `,-[0-9]+,` | a minus and digits, no point | 120 |
| `,-[0-9]+\.[0-9],` | a minus, digits, a point, one digit | 22 352 |

</div>

</v-click>

<div class="note-text mt-md">22 472 − 120 = 22 352 hours below freezing. The middle pattern finds exactly the −999 rows.</div>

<!--
**Ask:** before each click: more lines or fewer than the step before?
**Say:** one sign added at a time, each step checked by its count.
(~3 min)
-->

---
hideInToc: true
---

# Put a Pattern in **Single Quotes**

<div class="card card-warning card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh**, without quotes

```text
% grep -cE ,-[0-9]+\.[0-9], data/raw/weather.csv
zsh: no matches found: ,-[0-9]+.[0-9],
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ The shell reads `[ ]`, `*`, `?` and `\` itself before `grep` starts. In `'single quotes'` every sign reaches `grep` unchanged.

</div>

<!--
**Say:** zsh took `[0-9]` as part of a file name, found no such file and stopped.
**If asked:** Git Bash passes the line on but drops the backslash, so `.` fits any character and the count is 22 472, with no warning. That is worse than an error.
(~2 min)
-->

---
hideInToc: true
---

# Is Every Other Row a **Measurement**?

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ grep -cE ',-?[0-9]+\.[0-9],' data/raw/weather.csv
87552
```
```text
$ grep -vcE ',-?[0-9]+\.[0-9],' data/raw/weather.csv
121
```
```text
$ grep -vnE ',-?[0-9]+\.[0-9],' data/raw/weather.csv | head -n 3
1:time,temp_c,humidity_pct,wind_ms
31154:2019-07-22T00:00,-999,76,3.2
31155:2019-07-22T01:00,-999,81,3.0
```
````

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 4: a temperature with one decimal, below zero or not, is in 87 552 rows. The other 121 are the header and the 120 rows of −999. −999 is the only mark.

</div>

<!--
**Ask:** 87 673 lines, 87 552 fit. How many will `-v` find, and which? 121: the header and the 120 marks.
**Say:** `-?` lets the minus be there or not. `-v` keeps the lines that do not fit, `-n` adds their line numbers.
**Ask:** what would a count of 125 have told us? Four rows of another form, to be read one by one.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# The **Mean**

Step 5: the mean without the 120 rows, and with them.

<!--
(~1 min)
-->

---
hideInToc: true
---

# Keep the Measured Rows in `data/processed`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
$ grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
$ wc -l data/processed/weather_valid.csv
87553 data/processed/weather_valid.csv
$ grep -c ',-999,' data/processed/weather_valid.csv
0
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ 87 673 − 120 = 87 553 lines, the header and 87 552 hours, and no −999 left. `data/raw` stays as it arrived: delete the new file, run the line again, and it is back.

</div>

<!--
**Say:** `-v` keeps the lines without the mark.
(~2 min)
-->

---
hideInToc: true
---

# The Mean With and Without the **−999 Rows**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ awk -F, '{ print $2 }' data/raw/weather.csv | head -n 3
temp_c
-4.4
-4.8
```
```text
$ awk -F, 'NR > 1 { s += $2; n++ } END { print n, s / n }' data/raw/weather.csv
87672 5.7828
```
```text
$ awk -F, 'NR > 1 { s += $2; n++ } END { print n, s / n }' data/raw/weather.csv
87672 5.7828
$ awk -F, 'NR > 1 { s += $2; n++ } END { print n, s / n }' data/processed/weather_valid.csv
87552 7.15997
```
````

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 The 87 552 measured hours sum to 626 869.3 °C: 626 869.3 / 87 552 = **7.16**. The marks add 120 × (−999) = −119 880, and the count grows by 120: (626 869.3 − 119 880) / 87 672 = **5.78**.

</div>

<!--
**Ask:** before the second step: will the mean of all rows be higher or lower than 7.16, and by how much?
**Say:** `awk` runs its program on every line: `{ print $2 }` prints field 2; `NR > 1 { s += $2; n++ }` adds field 2 into `s` and counts in `n` for every line after the header; `END { … }` runs once, at the end. Step 5: 7.16 without the marks, 5.78 with them; five lost days moved a ten-year mean by 1.38 °C.
(~4 min)
-->

---
hideInToc: true
---

# What One Mark Does to a **Mean**

<div class="card card-info card-glass pad-compact mt-sm">

🧮 n values with mean m, and k marks of value M added. The new mean:

(n·m + k·M) / (n + k) = m + k·(M − m) / (n + k)

</div>

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Marks k | Shift k · (−999 − 7.15997) / (87 552 + k) | Mean |
| --- | --- | --- |
| 0 | 0 | 7.16 |
| 1 | −0.0115 | 7.15 |
| 10 | −0.115 | 7.05 |
| 120 | −1.377 | 5.78 |

</div>

<div class="note-text mt-md">One row of −999 among 87 553 already changes the second decimal. A mark is found before any mean is taken.</div>

<!--
**Say:** the shift is the distance of the mark from the mean, −1006, times the share of marked rows. A mark far from the data weighs a thousand times a normal value.
**Ask:** what would 120 rows of 0 instead of −999 have done? 120 × (0 − 7.16) / 87 672 = −0.0098: a shift nobody would notice by eye.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Programs and **Packages**

Step 6: a second program for the same mean. It needs Python, and Python comes in a package.

<!--
**Say:** two Python programs came with the folder. A second program that agrees is a check of the first; to run it, the laptop needs Python.
(~1 min)
-->

---
hideInToc: true
---

# Where a Program **Comes From**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh**

```text
% type head git python
head is /usr/bin/head
git is /opt/homebrew/bin/git
python is /opt/homebrew/Caskroom/miniforge/base/bin/python
```

</div>

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🪟 **Windows · Git Bash**

```text
$ type head git python
head is /usr/bin/head
git is /mingw64/bin/git
python is /c/Users/smilte/miniforge3/python
```

</div>

<div class="card card-info card-glass pad-compact mt-sm">

📦 `head` came with the system, or with Git Bash. `git` and `python` are in folders their installers made. Without Miniforge installed: `python: not found`.

</div>

<!--
**Say:** step 4 of the shell, finding the program: each lives in a folder, and the shell knows where to look.
(~2 min)
-->

---
hideInToc: true
---

# How the Shell Finds a Program: **PATH**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% echo $PATH | tr ':' '\n'
/opt/homebrew/Caskroom/miniforge/base/bin
/opt/homebrew/Caskroom/miniforge/base/condabin
/opt/homebrew/bin
/usr/bin
/bin
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · Git Bash**

```text
$ echo $PATH | tr ':' '\n'
/c/Users/smilte/miniforge3
/c/Users/smilte/miniforge3/Scripts
/mingw64/bin
/usr/bin
/c/Windows/system32
```

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ➡️ **Searched top to bottom**

`PATH` holds a list of folders, separated by `:`. The shell takes the first folder with a program of the typed name: of two Pythons, the first runs.

</div>

<div class="card card-info card-glass pad-compact">

## 📦 **What an install changes**

The program lands in a folder, and the folder goes on `PATH`. A terminal reads `PATH` when it opens: a new install needs a new terminal.

</div>

</div>

<!--
**Say:** "command not found" means: in none of these folders. `tr ':' '\n'` puts each folder on its own line.
**If asked:** the lists are shortened; a real laptop shows ten to twenty folders.
(~2 min)
-->

---
hideInToc: true
---

# What a **Package** Is

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
(weather) $ conda install numpy
The following NEW packages will be INSTALLED:

  libblas            …::libblas-3.11.0-…
  libcblas           …::libcblas-3.11.0-…
  …
  libopenblas        …::libopenblas-0.3.34-…
  numpy              …::numpy-2.5.4-…
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| A package holds | For numpy |
| --- | --- |
| files | the numpy library for Python |
| a name and a version | `numpy 2.5.4` |
| its **dependencies**: the packages it needs | Python; OpenBLAS for linear algebra, which needs the Fortran runtime: 6 more packages |
| a source: a **repository** | conda-forge |

</div>

<!--
**Say:** one package asked for, seven installed: the package manager reads the dependencies and fetches them too. A package is not only Python: OpenBLAS is a C and Fortran library.
**If asked:** the `…` hide the channel and the build of each file, such as `conda-forge/osx-arm64::numpy-2.5.4-…`. Measured with Miniforge 26.7.2; the extra packages differ a little by system.
(~2 min)
-->

---
hideInToc: true
---

# A Package **Manager**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Job | 🍎 Homebrew, `brew` | 🪟 `winget`, part of Windows |
| --- | --- | --- |
| Find a name | `brew search git` | `winget search git` |
| Install Git | `brew install git` | `winget install --id Git.Git -e` |
| Install Miniforge | `brew install --cask miniforge` | `winget install --id CondaForge.Miniforge3 -e` |
| What is installed | `brew list` | `winget list` |
| Newer versions | `brew upgrade` | `winget upgrade --all` |
| Remove | `brew uninstall git` | `winget uninstall --id Git.Git -e` |

</div>

<div class="card card-success card-glass pad-compact mt-md">

📜 A package manager looks the name up in its repository, fetches the package and its dependencies, and puts the program where the shell finds it. The line can go into a README: on the next laptop it installs the same program.

</div>

<!--
**Say:** the same jobs in every package manager, with other words. Miniforge brings Python and `conda`, a package manager for Python's packages.
**If asked:** a cask is a Homebrew package for an app with an installer. winget also runs in Git Bash once Git is there. Linux has `apt` or `dnf`, with the same jobs.
(~2 min)
-->

---
hideInToc: true
---

# `conda`: Packages for Python, in **Environments**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
(base) $ conda --version
conda 26.7.2
(base) $ conda config --show channels
channels:
  - conda-forge
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📦 **A package manager**

Installs from a **channel**, conda's word for a repository: here conda-forge. A package can be Python itself, a Python library, or a C library that one needs.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧪 **An environment manager**

An **environment** is a folder with one Python and its packages. The installer made the first one, `base`: the prompt names it.

</div>

</div>

<!--
**Say:** brew and winget install a program for the whole laptop; conda installs into one environment at a time.
**If asked:** `conda init zsh` on a Mac and `conda init bash` in Git Bash, once, then a new terminal shows `(base)`. Miniforge is conda with conda-forge as its only channel, free to use.
(~2 min)
-->

---
hideInToc: true
---

# One Environment per **Project**

<div class="card card-warning card-glass pad-compact mt-sm">

💥 A script written for numpy 1.26, run where numpy 2.5 is installed:

```text
$ python -c "import numpy as np; print(np.float_)"
AttributeError: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.
```

</div>

<div class="card card-primary card-glass pad-compact mt-md">

```text
(base) $ conda create -n weather python=3.14
(base) $ conda activate weather
(weather) $ type python
python is /opt/homebrew/Caskroom/miniforge/base/envs/weather/bin/python
```

</div>

<div class="note-text mt-md">Every project run in one shared Python imports the same numpy, and an upgrade for one breaks another. An environment per project keeps each its own. Activation puts its folder first on <code>PATH</code>.</div>

<!--
**Say:** nothing in the old script changed; a package on the laptop did. `-n` names the environment, `python=3.14` asks for its Python.
**If asked:** in Git Bash the environment is `/c/Users/smilte/miniforge3/envs/weather`. It holds 24 packages, 221 MB. `conda deactivate` returns to `base`; `conda env remove -n weather` deletes the folder.
(~2 min)
-->

---
hideInToc: true
---

# Activation Changes **PATH**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · Git Bash: the same lines, the paths under `/c/Users/smilte/miniforge3`

````md magic-move
```text
(base) $ type python
python is /opt/homebrew/Caskroom/miniforge/base/bin/python
(base) $ echo $PATH | tr ':' '\n' | head -n 1
/opt/homebrew/Caskroom/miniforge/base/bin
```
```text
(base) $ conda activate weather
(weather) $ type python
python is /opt/homebrew/Caskroom/miniforge/base/envs/weather/bin/python
(weather) $ echo $PATH | tr ':' '\n' | head -n 1
/opt/homebrew/Caskroom/miniforge/base/envs/weather/bin
```
```text
(weather) $ conda deactivate
(base) $ type python
python is /opt/homebrew/Caskroom/miniforge/base/bin/python
```
````

</div>

<div class="note-text mt-md">Activation puts the environment's folder first on <code>PATH</code> and its name in the prompt. The shell then finds that environment's <code>python</code> first. Nothing is copied or installed.</div>

<!--
**Ask:** after `conda activate weather`, which `python` will `type` find?
**Say:** the rule of `PATH` from a few slides back, used by conda: first folder wins.
**If asked:** in Git Bash the environment's folder is `/c/Users/smilte/miniforge3/envs/weather`, and `python` sits in it directly.
(~3 min)
-->

---
hideInToc: true
---

# Write the Environment Down: `environment.yml`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
(weather) $ conda env export --from-history > environment.yml
(weather) $ cat environment.yml
name: weather
channels:
  - conda-forge
dependencies:
  - python=3.14
prefix: /opt/homebrew/Caskroom/miniforge/base/envs/weather
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 💻 **On another laptop**

Delete the line `prefix:`, which names this laptop. `conda env create -f environment.yml` makes `weather` there.

</div>

<div class="card card-success card-glass pad-compact">

## 🧭 **Why `--from-history`**

It keeps what was asked for, which works on every system. The full export pins each package to a build of one system.

</div>

</div>

<!--
**Say:** the file is the environment written down, as the README lines will be the check written down. The two scripts need nothing beyond Python, so the file lists only `python=3.14`.
**If asked:** `numpy=2.5.4` under `dependencies` would ask for one version.
(~2 min)
-->

---
hideInToc: true
---

# The Mean from `column_stats.py`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

```text
(weather) $ python scripts/column_stats.py data/processed/weather_valid.csv temp_c
file    data/processed/weather_valid.csv
column  temp_c
rows    87552
min     -16.3
max     32.4
mean    7.15997
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| File | `awk` | `column_stats.py` |
| --- | --- | --- |
| `data/raw/weather.csv` | 5.7828 | 5.7828 |
| `data/processed/weather_valid.csv` | 7.15997 | 7.15997 |

</div>

<div class="note-text mt-md">Step 6: two programs, written apart, agree to six digits. The script's line: the program <code>python</code>, its file, then two words for the script.</div>

<!--
**Say:** an agreement between two independent programs rules out a slip in either one. The coldest hour of the valid rows, −16.3 °C, is a plausible winter night.
(~2 min)
-->

---
hideInToc: true
---

# The Second Script: the Spreadsheet **Export**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📥 **`data/raw/daily_export.csv`**

```text
nr;date;temp_c
1;2025-10-01;6,3
2;2025-10-02;5,0
…
9;2025-10-09;9,8
;mean;7,97
```

`;` between values, a decimal comma, a column `nr`, a mean line: 180 bytes.

</div>

<div class="card card-success card-glass pad-compact">

## ⚙️ **Cleaned by one line**

```text
$ python scripts/clean_export.py \
    data/raw/daily_export.csv \
    data/processed/daily.csv
9 rows written to data/processed/daily.csv
$ wc -c data/processed/daily.csv
148 data/processed/daily.csv
```

</div>

</div>

<div class="note-text mt-md">The repair done by hand in the editor in Lecture 02, 180 bytes to 148, as one line that runs again on the next export.</div>

<!--
**Say:** header `date,temp_c` and LF: 12 bytes. Eight rows like `2025-10-01,6.3`: 15 each. `2025-10-06,10.4`: 16. 12 + 8 × 15 + 16 = 148.
**If asked:** a `\` at the end of a line continues the command on the next line. The script states the line ending, `newline="\n"`, so it writes the same 148 bytes on every system.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Checksums & **Backups**

Step 7: is my `weather.csv` the file Smiltė used?

<!--
**Say:** two copies of a file of 2.5 million bytes cannot be compared by eye. A checksum is a short number computed from every byte.
(~1 min)
-->

---
hideInToc: true
---

# The Checksum of `weather.csv`

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh**

```text
% shasum -a 256 data/raw/weather.csv
3f1ad06d3bb5773eac79dfc964cdf8af998689ef58aa8623f25d2050fbe00756  data/raw/weather.csv
```

</div>

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🪟 **Windows · Git Bash**

```text
$ sha256sum data/raw/weather.csv
3f1ad06d3bb5773eac79dfc964cdf8af998689ef58aa8623f25d2050fbe00756  data/raw/weather.csv
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔠 **64 hex digits**

The 256 bits of SHA-256, computed from all 2 515 215 bytes. The same bytes give the same digits on every computer.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧬 **One byte changed**

Another 64 digits, all of them, as Lecture 03 showed: `6.3` against `6.4` in one row.

</div>

</div>

<!--
**Say:** two program names, one checksum, in the same form: 64 digits, two spaces, the file.
**Ask:** Smiltė's README names `3f1a…0756`. Read the first and the last four digits of yours: the same file.
(~2 min)
-->

---
hideInToc: true
---

# Check Against the **Source**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **Git Bash** · on macOS `shasum -a 256 -c`

```text
$ cat weather.sha256
3f1ad06d3bb5773eac79dfc964cdf8af998689ef58aa8623f25d2050fbe00756  data/raw/weather.csv
$ sha256sum -c weather.sha256
data/raw/weather.csv: OK
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **It tells**

The same digits: the same bytes, every one of 2 515 215. Other digits: at least one byte differs.

</div>

<div class="card card-warning card-glass pad-compact">

## ❓ **It does not tell**

Which byte, or which copy is right. That takes the checksum from the source: from Smiltė, written down when the file arrived.

</div>

</div>

<!--
**Say:** `-c` reads a list of checksums and file names, computes each one again and compares. The two programs write and read the same format, so a list made on a Mac checks on Windows.
**If asked:** a checksum sent by the same e-mail as a forged file proves nothing: it must come by another route.
(~2 min)
-->

---
hideInToc: true
---

# A List of Checksums for `data/raw`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **Git Bash** · on macOS `shasum -a 256`

```text
$ sha256sum data/raw/* > data/checksums.txt
$ sha256sum -c data/checksums.txt
data/raw/daily_export.csv: OK
data/raw/weather.csv: OK
```

After `6,3` became `6,4` in row 1 of the export:

```text
$ sha256sum -c data/checksums.txt
data/raw/daily_export.csv: FAILED
data/raw/weather.csv: OK
sha256sum: WARNING: 1 computed checksum did NOT match
```

</div>

<div class="note-text mt-md">The list is written once, when the raw files arrive, and checked after every copy. It stands in <code>data</code>, not in <code>data/raw</code>, so <code>data/raw/*</code> never includes it.</div>

<!--
**Live (optional):** `shasum -a 256 data/raw/* > data/checksums.txt`; in VS Code change `6,3` to `6,4` in `daily_export.csv` and save; `shasum -a 256 -c data/checksums.txt`. Change it back and save before going on.
**Say:** "raw is never edited" becomes a test that runs in a second.
(~3 min)
-->

---
hideInToc: true
---

# Which Files Have the Same **Bytes** on Both Systems

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| File | Made by | macOS | Windows |
| --- | --- | --- | --- |
| `data/raw/weather.csv` | the station | 2 515 215 B, `3f1ad06d…` | the same |
| `data/processed/weather_valid.csv` | `grep -v … >` | 2 511 735 B, `85b1f38d…` | the same |
| `data/processed/daily.csv` | `clean_export.py` | 148 B, `33fe5e77…` | the same |
| `results/temp_c.txt` | `column_stats.py … >` | 113 B, `ade2805b…` | 119 B |

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 `grep` copies each line's bytes, LF included. Python's `print` ends a line as the system does: LF on macOS, CRLF on Windows, one byte `0d` more on each of the 6 lines: 113 + 6 = 119. `clean_export.py` states LF, so it writes the same bytes on both.

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 7: the raw files are named by checksum. A result is named by what it says: `mean    7.15997`.

</div>

<!--
**Say:** same mean, different bytes. A checksum in the README is only promised for a file whose bytes are the same everywhere.
(~2 min)
-->

---
hideInToc: true
---

# Backups: the **3-2-1 Rule**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 3️⃣ **Three copies**

The working copy and two more.

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **Two kinds of storage**

The laptop's disk, and an external drive or a server.

</div>

<div class="card card-accent card-glass pad-compact">

## 1️⃣ **One elsewhere**

University storage, a cloud service, a drive at home.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 Suppose one copy is lost within a year with probability 1 in 20. Two independent copies are both lost with (1/20)² = 1 in 400, three with (1/20)³ = 1 in 8000. Copies on one disk or in one bag are not independent: that is what the 2 and the 1 are for.

</div>

<div class="note-text mt-md">What a backup is for: <code>data/raw</code>, <code>scripts</code>, the README. <code>data/processed</code> and <code>results</code> are made again by commands.</div>

<!--
**Say:** the 1 in 20 is an assumption for the arithmetic, not a measured rate. The point is the exponent, and when it applies.
**Ask:** who has lost a file: a wrong save, a dead disk, a stolen bag?
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Make It **Repeatable**

Step 8: anyone runs the whole check again with one line.

<!--
**Say:** every step so far was a typed line. Written down in order, they are the check.
(~1 min)
-->

---
hideInToc: true
---

# The README: the Result and How to **Rebuild**

<div class="card card-primary card-glass pad-compact mt-sm">

## ✏️ **In `README.md`**

```md
Missing value: `temp_c` is `-999` in 120 rows, 2019-07-22 to 07-26.
`data/raw/weather.csv`: 87 673 lines, SHA-256 `3f1ad06d…fbe00756`.

## Result

Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours.
The 120 hours marked `-999` are left out.

## How to rebuild

    conda env create -f environment.yml
    conda activate weather
    ./scripts/rebuild.sh
```

</div>

<!--
**Say:** every number here came out of a typed line today. The README tells a reader what the result is and which line makes it again; the script holds the steps.
**If asked:** the unit, °C, cannot come out of the file: the column table of the README holds it.
(~2 min)
-->

---
hideInToc: true
---

# `rebuild.sh`, Line by **Line**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📜 **`scripts/rebuild.sh`**

````md magic-move
```bash
#!/usr/bin/env bash
```
```bash
#!/usr/bin/env bash
mkdir -p data/processed results
```
```bash
#!/usr/bin/env bash
mkdir -p data/processed results
grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
```
```bash
#!/usr/bin/env bash
mkdir -p data/processed results
grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
```
````

</div>

<v-click>

<div class="card card-success card-glass pad-compact mt-md">

```text
$ chmod +x scripts/rebuild.sh
$ rm -r data/processed results
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
$ tail -n 1 results/temp_c.txt
mean    7.15997
```

</div>

</v-click>

<!--
**Live:** in VS Code make `scripts/rebuild.sh` from the lines on the slide and save; then `chmod +x scripts/rebuild.sh`, `rm -r data/processed results`, `./scripts/rebuild.sh`, `tail -n 1 results/temp_c.txt`.
**Say:** line 1 names the program that runs the file, bash, on both systems. Then the lines typed today, in order, brought back with `↑` and pasted, never retyped. The two `python` lines run the programs that came with the folder.
**Ask:** after `rm -r`, what will the last line of `results/temp_c.txt` be?
**If asked:** `chmod +x` marks the file as a program; `./` names its folder, because `scripts` is not on `PATH`. In Git Bash `chmod +x` changes nothing and the script runs anyway.
(~4 min)
-->

---
hideInToc: true
---

# Exit Status and `set -e`

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **zsh · Git Bash**

````md magic-move
```text
$ grep -c ',-999,' data/raw/weather.csv
120
$ echo $?
0
$ grep -c ',-999,' data/processed/weather_valid.csv
0
$ echo $?
1
```
```text
$ ./scripts/rebuild.sh            # a typo: daily_exprt.csv
no file data/raw/daily_exprt.csv
$ echo $?
0
```
```text
$ ./scripts/rebuild.sh            # with set -e as line 2
no file data/raw/daily_exprt.csv
$ echo $?
1
```
````

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔢 A program ends by handing the shell a number, its **exit status**: 0 for success, anything else for "no" or a failure; `$?` holds the last one. Without `set -e` a script runs every line and reports the status of its last line. `set -e` as line 2 stops it at the first line that fails.

</div>

<!--
**Ask:** before the second step: the script hit a typo in its third command. What will `$?` be? Most say 1; it is 0.
**Say:** `grep` says 1 when it found nothing. A script that goes on after a failed line hides the failure; with `set -e` it ends there and reports it.
**If asked:** a line that may say 1 on purpose, such as `grep -c`, needs `|| true` after it in a script with `set -e`.
(~3 min)
-->

---
hideInToc: true
---

# Rebuild Twice, Compare the **Checksums**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💻 **Git Bash** · on macOS `shasum -a 256`

```text
$ sha256sum results/temp_c.txt
ade2805b90fe64a0053fa65e28329eee616ad0389f9ca55db86400b1c7a9a18b  results/temp_c.txt
$ ./scripts/rebuild.sh
9 rows written to data/processed/daily.csv
$ sha256sum results/temp_c.txt
ade2805b90fe64a0053fa65e28329eee616ad0389f9ca55db86400b1c7a9a18b  results/temp_c.txt
```

</div>

<div class="note-text mt-md">Run twice on one laptop: the same 113 bytes. On Windows the same six lines take 119 bytes, so across systems compare the line that matters, <code>mean    7.15997</code>.</div>

<!--
**Say:** a check that runs again and gives the same bytes is a check anyone can repeat.
(~2 min)
-->

---
hideInToc: true
---

# The Eight Steps, **Answered**

<div class="card card-success card-glass pad-compact table-compact mt-sm">

| Step | Question about 7.16 | Answer |
| --- | --- | --- |
| 1 | Which column is the temperature? | `temp_c`, column 2 of 4 |
| 2 | Every hour of ten years? | 87 673 lines = 87 672 hours + header |
| 3 | Which rows are not measurements? | 120 rows of −999, 22 to 26 July 2019 |
| 4 | Is every other row a measurement? | 87 552 rows fit the pattern |
| 5 | The mean without them, and with? | 7.16 and 5.78 °C |
| 6 | A second program? | 7.15997, to six digits |
| 7 | The file Smiltė used? | SHA-256 `3f1ad06d…fbe00756` |
| 8 | Can anyone run it again? | `./scripts/rebuild.sh` |

</div>

<!--
**Say:** 7.16 is right, and now it is more than a number in an e-mail: the file, the steps, the program and the line that runs them are in the folder.
(~2 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Name the shell of your laptop, zsh or Git Bash, and say what it does with a line

</div>

<div class="card card-success card-glass pad-compact">

✅ Read and count a file, and join programs with the **pipe**, `>` and `2>`

</div>

<div class="card card-success card-glass pad-compact">

✅ Build a **regular expression** piece by piece, each piece checked by a count

</div>

<div class="card card-success card-glass pad-compact">

✅ Install programs with a **package manager**, and give a project its own **conda environment**

</div>

<div class="card card-success card-glass pad-compact">

✅ Name a file by its **SHA-256**, and keep copies by the **3-2-1** rule

</div>

<div class="card card-success card-glass pad-compact">

✅ Write the check as a **script** that stops at the first error, and read its **exit status**

</div>

</div>

<!--
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Check **Yourself**

Questions on this lecture, for after it. They are not part of the lecture time.

---
hideInToc: true
---

<MCQ
  question="The terminal is in weather-project/results. Which path names the raw weather file on every laptop?"
  :options="[
    '<code>data/raw/weather.csv</code>',
    '<code>../data/raw/weather.csv</code>',
    '<code>/data/raw/weather.csv</code>',
    '<code>~/data/raw/weather.csv</code>'
  ]"
  :correct="1"
  explanation="A relative path starts at the folder the terminal is in. Two points go up one level, from results to weather-project, and from there the path goes down into data and raw. A path that starts with a slash starts at the top of the disk, and the tilde stands for the home folder."
/>

---
hideInToc: true
---

<MCQ
  question="`head -n 3 data/raw/wether.csv > results/out.txt` runs. The file name has a typo. What happens?"
  :options="[
    'Nothing is printed, and out.txt holds the error message',
    'The error is printed on the screen, and out.txt is an empty file',
    'The error is printed, and out.txt is not made',
    'The shell corrects the name and copies weather.csv'
  ]"
  :correct="1"
  explanation="The error goes to standard error, which still reaches the screen; > writes only standard output. And > makes or empties its file before the program runs, so out.txt exists with 0 bytes. 2> would write the error into a file."
/>

---
hideInToc: true
---

<MCQ
  question="notes.txt has five lines. Then `echo done > notes.txt` and `echo checked >> notes.txt` run. How many bytes does notes.txt have?"
  :options="[
    'More than 13, because the five old lines are kept',
    '13',
    '11, because echo writes no line break',
    '26, because >> writes the file twice'
  ]"
  :correct="1"
  explanation="A single > empties the file first, so the five lines are gone, and >> adds a second line. The letters are 4 + 7 = 11, and echo ends each line with LF, one byte: 13 bytes, in zsh and in Git Bash alike."
/>

---
hideInToc: true
---

<MCQ
  question="`cut -d, -f3 weather.csv | sort | head -n 1` prints 100 as the lowest humidity. Why?"
  :options="[
    'The station measured 100 % most often',
    'sort compares text character by character, and 1 comes before 3',
    'cut took the wrong column',
    'head prints the last line'
  ]"
  :correct="1"
  explanation="Without -n, sort compares the values as text, from the left. 100 starts with 1, 34 with 3, so 100 comes first. sort -n compares numbers and puts 34 first."
/>

---
hideInToc: true
---

<MCQ
  question="In zsh, `grep -cE ,-[0-9]+\.[0-9], weather.csv` stops with `no matches found`. Why?"
  :options="[
    'grep cannot search for a minus sign',
    'The shell reads [0-9] as a pattern for file names before grep runs, and no file fits',
    'The file has no temperature below zero',
    'A pattern must be written in double quotes'
  ]"
  :correct="1"
  explanation="The shell reads a line before the program runs, and brackets, stars and backslashes mean something to it. zsh stops when a file-name pattern fits no file; bash passes it on but drops the backslash, and the count comes out wrong. In single quotes every character reaches grep unchanged."
/>

---
hideInToc: true
---

<MCQ
  question="A file has four lines: 2025-10-01,6.3 and 2025-10-06,10.4 and date,temp_c and 7;2025-10-07;9,2. Which lines does `^[0-9-]+,[0-9]+\.[0-9]$` find?"
  :options="[
    'All four lines',
    'The lines 2025-10-01,6.3 and 2025-10-06,10.4',
    'Only the line 2025-10-01,6.3',
    'The first two and 7;2025-10-07;9,2'
  ]"
  :correct="1"
  explanation="The pattern fits a whole line of digits and minus signs, a comma, a number, a point and one digit. The header has letters. The line with semicolons has a semicolon where the pattern allows only digits and minus signs, and no point. grep -E and the Find box of VS Code find the same two lines."
/>

---
hideInToc: true
---

<MCQ
  question="A column has 1000 rows. In 10 of them the value is the mark -999 for a missing value. The other 990 values have the mean 2.0. What is the mean of all 1000 values?"
  :options="[
    '2.0',
    '1.98',
    '-8.01',
    '-999'
  ]"
  :correct="2"
  explanation="The sum of the 990 real values is 1980. The ten marks add -9990. The mean of all rows is (1980 - 9990) / 1000 = -8.01. One row in a hundred gives the mean the wrong sign. The marked rows are taken out first."
/>

---
hideInToc: true
---

<MCQ
  question="PATH lists /opt/a/bin before /opt/b/bin. Both folders hold a program named python, 3.12 in a and 3.14 in b. What does `python --version` print?"
  :options="[
    'Python 3.14, because the newer version wins',
    'Python 3.12, because the shell stops at the first folder that holds the name',
    'Both print a line, one after the other',
    'Neither: two programs of one name on PATH is an error'
  ]"
  :correct="1"
  explanation="The shell goes through PATH in order and runs the first program of that name it finds. A newer version further down the list is never reached. That is why conda activate puts the folder of the environment first."
/>

---
hideInToc: true
---

<MCQ
  question="A colleague receives the project folder with environment.yml, which lists python=3.14 and numpy=2.5.4. Which lines give them the same environment?"
  :options="[
    '<code>conda install numpy</code> in base, nothing else',
    'Copy the folder envs/weather from your laptop into theirs',
    '<code>conda env create -f environment.yml</code>, then <code>conda activate weather</code>',
    'Open environment.yml in VS Code: the packages install themselves'
  ]"
  :correct="2"
  explanation="An environment is made on the laptop it runs on, from the file. conda env create reads the channel and the packages, and numpy=2.5.4 pins the version, so 2.5.4 arrives and not the newest one. A copied environment folder holds paths of the other laptop, and base is shared by every project."
/>

---
hideInToc: true
---

<MCQ
  question="results/temp_c.txt, written by `python scripts/column_stats.py … > results/temp_c.txt`, has 113 bytes on a Mac and 119 on Windows. What follows?"
  :options="[
    'One of the two runs lost a row',
    'The same six lines, with LF on the Mac and CRLF on Windows: the checksums differ, the mean does not',
    'The same bytes, because a checksum ignores line endings',
    'The Windows run used the raw file'
  ]"
  :correct="1"
  explanation="119 − 113 = 6, one byte per line: the 0d of CRLF, which Python's print writes on Windows. The lines and the mean are the same, the bytes and so the checksums are not. The README names such a file by what it says, and names by checksum only files whose bytes are the same everywhere."
/>

---
hideInToc: true
---

<MCQ
  question="A project is kept in three copies: the working folder on a laptop, a second folder on the same laptop, and a USB stick in the laptop bag. Which part of the 3-2-1 rule is not met?"
  :options="[
    'The 3: there are fewer than three copies',
    'The 2: all copies are on one kind of storage',
    'The 1: no copy is in another place',
    'None: the rule is met'
  ]"
  :correct="2"
  explanation="There are three copies, and the stick is a second kind of storage. But all three travel in one bag, so one theft or one fire takes them all. A copy on university storage, in a cloud service or on a drive kept at home meets the 1."
/>

---
hideInToc: true
---

<MCQ
  question="rebuild.sh has no `set -e`. Its python line for the export fails; the last line works. What does `echo $?` print after the script?"
  :options="[
    '1, because a line failed',
    '0, because the script ran on and its last line worked',
    'Nothing: the shell asks first whether to go on',
    'Two numbers, one for each line'
  ]"
  :correct="1"
  explanation="Without set -e a script runs every line, and its exit status is that of its last line. The last line worked, so the script reports 0, success, and the failure shows only as its message. With set -e it stops at the failing line and reports 1."
/>
