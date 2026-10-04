---
layout: cover
title: "Command Line & File Handling"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Command Line & File Handling

##### <span class="aims-badge">⚙️ automation · 📁 data & files · 🔧 tool-agnostic</span>

<!--
Speaker: the lecture is shown live. Keep VS Code open beside the slides, with
the project folder and a terminal, and type each command as its slide comes
up. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# The main goal of this lecture is to work on files with **typed commands**: a step that was typed can be written down, checked and run again

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🧭 Open a **terminal** with the same shell on Windows, macOS and Linux, and name a file by its **path**

</div>

<div class="card card-secondary card-glass pad-compact">

📁 Make, copy, move and delete files with commands, and name many files with one **wildcard**

</div>

<div class="card card-accent card-glass pad-compact">

🔗 Join small programs with **pipes** to count, sort and filter a file of 91 583 rows

</div>

<div class="card card-info card-glass pad-compact">

🔎 Describe text with a **regular expression**, in VS Code and with `grep -E`

</div>

<div class="card card-success card-glass pad-compact">

⚙️ Save commands as a **script**, and run a script that someone else wrote

</div>

<div class="card card-warning card-glass pad-compact">

🛡️ Compare files by **checksum**, keep **backups** by the 3-2-1 rule, and complete the **README**

</div>

</div>

---
hideInToc: true
---

# A Step, **Written Down**

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ✍️ **Lecture 2: four edits by hand**

```md
- **Cleaned copy:** `data/processed/pendulum.csv`.
  Mean line deleted, `,` replaced by `.`,
  `;` replaced by `,`, column `nr` deleted
```

The README lists the edits in words. To clean the next file, someone reads the list and makes every edit again.

</div>

<div class="card card-primary card-glass pad-compact">

## ⌨️ **The same four edits, typed**

```text
grep -v mean data/raw/pendulum.csv |
  tr ',' '.' | tr ';' ',' | cut -d, -f2,3
```

Each edit is one small program. The line is the record of what was done, and it runs again on the next file.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

This lecture builds that line part by part: the terminal, files and folders, pipes, patterns, scripts. The examples are the two files of the project folder: the pendulum table and `D0_KPi.csv` with its 91 583 rows.

</div>

<!--
Speaker: open the README of the project folder and read the line "Cleaned
copy" aloud. Then run the typed line once in the terminal, without explaining
it: the cleaned table appears. Every part of it is explained in the next hour.
(~2 min)
-->

---
hideInToc: true
---

# Three Questions, **Clicked and Typed**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Question about `D0_KPi.csv` | In VS Code, Lecture 2 | As a command | Answer |
| --- | --- | --- | --- |
| How many lines? | `Ctrl+End`, read the line number | `wc -l data/raw/D0_KPi.csv` | 91 584 |
| What is on line 5000? | `Ctrl+G`, then `5000` | `head -n 5000 data/raw/D0_KPi.csv \| tail -n 1` | `1868.8636,…` |
| How many rows have no decay time? | `Ctrl+F`, then `-100` | `grep -c ',-100' data/raw/D0_KPi.csv` | 49 |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🖱️ **What a click leaves**

The answer on the screen. The steps stay in the memory of whoever clicked, and they are done again by hand for the next file.

</div>

<div class="card card-success card-glass pad-compact">

## ⌨️ **What a typed line leaves**

The line itself. It goes into the README or into a script. It gives the same answer on Windows, macOS and Linux, and on a file of 10 GB that no editor opens.

</div>

</div>

<!--
Speaker: the room has found the three answers by hand in VS Code: 91 584 lines,
line 5000 begins with 1868.8636, and 49 rows carry -100. Nothing new is found here. The
point is the third column: each answer now has a line that can be kept. (~2 min)
-->

---
layout: section
hideInToc: true
---

# The **Shell**

<!--
Speaker: where commands are typed, what reads them, and how a file is named in
a command. pwd, ls and cd are known from Lecture 3. (~1 min)
-->

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

---
hideInToc: true
---

# Terminal, Shell, **Program**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖥️ **Terminal**

The window. It shows text and passes on what is typed. VS Code has one in the Panel.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🐚 **Shell**

The program that reads the line. It finds the program named by the first word, starts it, waits until it ends, and shows the prompt again.

</div>

<div class="card card-accent card-glass pad-compact">

## ⚙️ **Program**

It does one job and prints text. `ls` lists, `wc` counts, `sort` sorts. Each is a file on the disk, like any other program.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The shell of Git Bash and of Linux is `bash`. The shell of macOS is `zsh`. Both read every command of this lecture in the same way. PowerShell, used for `pwd`, `ls` and `cd` in Lecture 3, is a third shell. It has other names for most commands, `Get-Content` and `Select-String` among them, so its lines do not run on macOS or Linux.

</div>

<!--
Speaker: three words that are used as one in everyday talk. The distinction
matters once: when a command is "not found", it is the shell that could not
find a program of that name. (~2 min)
-->

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

---
hideInToc: true
---

# Absolute **Paths**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌳 **Folders form a tree**

```text
/
└─ Users
   └─ ada
      └─ Documents
         └─ analysis-project
            ├─ README.md
            └─ data
               └─ raw
                  └─ D0_KPi.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📍 **From the top to the file**

- An absolute path lists the folders from the top of the tree down to the file, with `/` between them
- It starts with `/`
- `pwd` prints the folder the terminal is in, as an absolute path
- `~` stands for the home folder, here `/Users/ada`

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

```text
macOS      /Users/ada/Documents/analysis-project/data/raw/D0_KPi.csv
Git Bash   /c/Users/ada/Documents/analysis-project/data/raw/D0_KPi.csv
Windows    C:\Users\ada\Documents\analysis-project\data\raw\D0_KPi.csv
```

</div>

<div class="note-text mt-sm">Git Bash writes the drive <code>C:</code> as <code>/c</code> and uses <code>/</code> where Windows uses <code>\</code>. On Linux the home folders are in <code>/home</code>.</div>

<!--
Speaker: run pwd and read the answer from left to right as a walk down the
tree. Three laptops in the room give three different answers. (~2 min)
-->

---
hideInToc: true
---

# Relative **Paths**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🧭 **One file, seen from four places**

| The terminal is in | Path to the file |
| --- | --- |
| the project folder | `data/raw/D0_KPi.csv` |
| its folder `scripts` | `../data/raw/D0_KPi.csv` |
| its folder `data/raw` | `D0_KPi.csv` |
| any folder | `~/Documents/analysis-project/data/raw/D0_KPi.csv` |

</div>

<div class="card card-secondary card-glass pad-compact">

## ✏️ **Three short names**

- A relative path starts at the folder the terminal is in. It does not start with `/`
- `.` is that folder itself
- `..` is the folder above it. `cd ..` goes up one level, `cd ../..` two
- `~` is the home folder. `cd` alone goes there

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

♻️ The rule: the terminal stays in the project folder, and every command, every script and the README use paths that start there. Then the project runs on any laptop and in any place on its disk. A path that begins with `/Users/ada` exists on one computer.

</div>

<!--
Speaker: cd into scripts and run ls ../data/raw, then cd .. to come back. From
here on the terminal does not leave the project folder. (~2 min)
-->

---
hideInToc: true
---

# Keys That **Save Typing**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## ⌨️ **In the command line**

| Key | What it does |
| --- | --- |
| `Tab` | Completes a name: `cd da`, `Tab` gives `cd data/` |
| `Tab` again | Lists the names that fit, if there are several |
| `↑` `↓` | Earlier commands, one at a time |
| `Ctrl+A` `Ctrl+E` | To the start and to the end of the line |
| `Ctrl+C` | Stops the program that is running |

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧹 **Around it**

- `history` lists the commands typed so far, with numbers
- `clear` empties the Panel. Nothing is deleted
- `q` leaves a program that shows one page at a time
- Paste with `Ctrl+V` (macOS `Cmd+V`)
- The mouse does not move the cursor inside the line. The arrow keys do

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A name completed by `Tab` has no typing mistake in it. If `Tab` adds nothing, no name fits what was typed so far: the path is wrong before it is run.

</div>

<!--
Speaker: type wc -l da, Tab, r, Tab, D, Tab, and let the room count the keys
for the path: seven instead of nineteen. (~2 min)
-->

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

---
layout: section
hideInToc: true
---

# Files & **Folders**

<!--
Speaker: everything the Side Bar of VS Code does with files, as commands:
look, count, make, copy, move, delete, find. (~1 min)
-->

---
hideInToc: true
---

# Read a File: `cat`, `head`, `tail`, `less`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 👀 **The first and the last lines**

```text
$ head -n 3 data/raw/D0_KPi.csv
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
1860.6599,2803.4126,0.0001864154,0.34182164
$ tail -n 2 data/raw/D0_KPi.csv
1871.4323,2541.8845,0.0001756544,6.866581
1911.2631,2543.4617,0.00017650973,8.169813
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📖 **Four programs**

- `cat FILE` prints the whole file. Right for the ten lines of `pendulum.csv`
- `head -n 3 FILE` prints the first 3 lines, `tail -n 2 FILE` the last 2
- `tail -n +2 FILE` prints from line 2 on: the file without its header line
- `less FILE` shows one screen at a time. `Space` goes on, `q` leaves

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`cat data/raw/D0_KPi.csv` prints 91 584 lines. `Ctrl+C` stops it. `head` reads only as far as it prints, so the first lines of a file of 10 GB appear at once.

</div>

<!--
Speaker: run cat on the large file once and stop it with Ctrl+C. Then head.
(~2 min)
-->

---
hideInToc: true
---

# Count: `wc`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔢 **Lines, words, bytes**

```text
$ wc data/processed/pendulum.csv
      10      10      97 data/processed/pendulum.csv
$ wc -l data/raw/D0_KPi.csv
   91584 data/raw/D0_KPi.csv
$ wc -c data/raw/D0_KPi.csv
 3926142 data/raw/D0_KPi.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **What the numbers are**

- `wc` prints lines, words and bytes. `-l`, `-w` and `-c` print one of them
- 97 bytes: the size counted by hand in Lecture 3
- 91 584 lines: one header line and 91 583 rows
- 3 926 142 / 91 584 = 42.9 bytes per line

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ `wc -l` counts line breaks, the byte `0A`. A file whose last line has no line break after it counts one line fewer than the editor shows.

</div>

<div class="note-text mt-sm">macOS puts spaces before the numbers. Git Bash does not.</div>

<!--
Speaker: wc stands for word count. The three numbers of the small file are
10 lines, 10 words, because no line has a space in it, and 97 bytes. (~2 min)
-->

---
hideInToc: true
---

# Make and Copy: `mkdir`, `cp`, `mv`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📂 **A folder with two copies**

```text
$ mkdir backup
$ cp data/raw/pendulum.csv backup
$ cp -r data backup
$ ls backup
data            pendulum.csv
$ mv backup/pendulum.csv backup/pendulum_raw.csv
$ ls backup
data                    pendulum_raw.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📋 **Three programs**

- `mkdir NAME` makes a folder. `mkdir -p a/b/c` also makes the folders above it
- `cp FROM TO` copies a file. If `TO` is a folder, the copy goes into it under the same name
- `cp -r` copies a folder with all that is in it
- `mv FROM TO` moves a file or a folder. A new name in the same folder renames it

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ `cp` and `mv` replace a file that already has the target name, and they do not ask. `cp -i` and `mv -i` ask first.

</div>

<!--
Speaker: watch the folder appear in the Side Bar while you type. The terminal
and the Side Bar show the same disk. (~2 min)
-->

---
hideInToc: true
---

# Delete: `rm`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🗑️ **A file, then a folder**

```text
$ rm backup/pendulum_raw.csv
$ rmdir backup
rmdir: backup: Directory not empty
$ rm -r backup
$ ls
data        README.md   results     scripts
```

</div>

<div class="card card-secondary card-glass pad-compact">

## ✂️ **Three forms**

- `rm FILE` deletes a file
- `rmdir FOLDER` deletes a folder that is empty
- `rm -r FOLDER` deletes a folder and all that is in it
- `rm -i` asks before each file

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The shell has no Recycle Bin and no Trash, and `Ctrl+Z` takes nothing back. Before `rm`: run `pwd` to see where the terminal is, then `ls` with the same path to see what will go.

</div>

<div class="card card-info card-glass pad-compact mt-sm">

What `rm` can take away for good is a file in `data/raw`, a script or the README. A file in `data/processed` or `results` can be made again.

</div>

<!--
Speaker: rmdir refuses a folder that still holds something. That refusal is a
safety net, and rm -r is the way round it. Say the folder name aloud before
pressing Enter. (~2 min)
-->

---
hideInToc: true
---

# Many Files at Once: **Wildcards**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ echo data/*/*.csv
data/processed/pendulum.csv data/raw/D0_KPi.csv data/raw/pendulum.csv
$ wc -l data/*/*.csv
      10 data/processed/pendulum.csv
   91584 data/raw/D0_KPi.csv
      11 data/raw/pendulum.csv
   91605 total
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ✳️ **`*`**

Any number of characters, also none. `*.csv` fits every name that ends in `.csv`.

</div>

<div class="card card-accent card-glass pad-compact">

## ❓ **`?`**

Exactly one character. `D?_KPi.csv` fits `D0_KPi.csv`.

</div>

<div class="card card-info card-glass pad-compact">

## 🔤 **`[pr]`**

One of the characters listed. `data/[pr]*` fits `data/processed` and `data/raw`.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

The shell replaces the pattern by the list of names that fit, before the program starts. `wc` never sees the `*`: it gets three file names. `echo` prints its arguments, so `echo PATTERN` shows what a pattern stands for. Run it before `rm PATTERN`.

</div>

<!--
Speaker: the pattern is the shell's work, not the program's. That is why the
same three signs work with every program. (~2 min)
-->

---
hideInToc: true
---

# Search the Folders: `find`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔍 **By name, by size**

```text
$ find . -name '*.csv'
./data/processed/pendulum.csv
./data/raw/D0_KPi.csv
./data/raw/pendulum.csv
$ find . -size +1M
./data/raw/D0_KPi.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **How to read it**

- `find FOLDER` walks through the folder and every folder below it. `.` is the folder the terminal is in
- `-name '*.csv'` keeps the names that fit the pattern
- `-size +1M` keeps files larger than 1 MB
- `-type d` keeps folders, `-type f` files

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The pattern stands in quotes here. Quotes stop the shell from replacing it, so `find` gets the pattern itself and tries it in every folder. A wildcard such as `data/*/*.csv` looks two folders down and no further. `find` looks at every depth.

</div>

<!--
Speaker: find answers "where did I put it" for a whole disk: find ~ -name
'pendulum*' searches the home folder. It takes a while. (~2 min)
-->

---
hideInToc: true
---

# The Project Folder, **from the Shell**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📁 **The layout of Lecture 2**

```text
analysis-project/
├─ README.md
├─ data/
│  ├─ raw/         D0_KPi.csv  pendulum.csv
│  └─ processed/   pendulum.csv
├─ scripts/
└─ results/        report.md  pendulum_plot.png
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Its rules, as habits at the prompt**

- The terminal stays in `analysis-project`
- Commands **read** from `data/raw`. No command writes there
- What a command makes goes to `data/processed` or to `results`
- Commands worth keeping go into `scripts`
- A name without spaces is one argument. A date written `2026-10-13` sorts in `ls`

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The layout answers one question for every file: can it be made again? Files in `data/processed` and `results` can, by a command. Files in `data/raw` and `scripts` cannot.

</div>

<!--
Speaker: nothing new on this slide. It fixes where the commands of the next
sections read and where they write. (~1 min)
-->

---
layout: section
hideInToc: true
---

# Pipes & **Filters**

<!--
Speaker: the centre of the lecture. Small programs that each do one thing to
lines of text, joined so that the output of one is the input of the next.
(~1 min)
-->

---
hideInToc: true
---

# Output into a File: `>` and `>>`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📤 **Redirect**

```text
$ head -n 4 data/raw/D0_KPi.csv > results/sample.csv
$ wc -l results/sample.csv
       4 results/sample.csv
$ echo "first lines of D0_KPi.csv" > results/note.txt
$ echo "made on 2026-10-13" >> results/note.txt
$ cat results/note.txt
first lines of D0_KPi.csv
made on 2026-10-13
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧾 **What happens**

- A program prints to its **standard output**. Normally that is the terminal
- `> FILE` sends the output into a file. Nothing appears on the screen
- `>` makes the file, or **empties** it if it exists. `>>` adds at its end
- `echo` prints its arguments. With `>` it writes one line into a file

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The shell empties the file named after `>` before the program starts. `sort results/sample.csv > results/sample.csv` therefore sorts an empty file, and `wc -l` then counts 0 lines. A command never writes into the file it reads.

</div>

<!--
Speaker: run the sort line on results/sample.csv and count again: 0. Then
delete both scratch files with rm. (~2 min)
-->

---
hideInToc: true
---

# Program to Program: the Pipe `|`

<div class="card card-info card-glass pad-compact mt-sm">

`A | B` starts both programs. What `A` prints becomes the input of `B`. No file stands between them.

</div>

<div class="mt-sm" style="text-align: center;">

```mermaid {scale: 0.8}
graph LR
    F["D0_KPi.csv"]:::input --> A["head -n 5000"]
    A -->|"5000 lines"| B["tail -n 1"]
    B -->|"1 line"| T["terminal"]:::output

    classDef input fill:#0b2a4a,stroke:#5eead4,color:#e8f1ff
    classDef output fill:#063c34,stroke:#34d399,color:#d1fae5
```

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

```text
$ head -n 5000 data/raw/D0_KPi.csv | tail -n 1
1868.8636,5537.248,0.0007151779,10.399748
$ ls data/raw | wc -l
       2
```

</div>

<div class="card card-secondary card-glass pad-compact">

A program that takes lines in and prints lines out is a **filter**: `head`, `tail`, `cut`, `sort`, `uniq`, `grep`, `tr`, `wc`. Given no file name, a filter reads what the pipe hands to it.

</div>

</div>

<!--
Speaker: line 5000 is the line that Ctrl+G found in VS Code. The second
example counts the files in data/raw: ls prints two names,
wc -l counts two lines. (~2 min)
-->

---
hideInToc: true
---

# Columns: `cut`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✂️ **Fields 1 and 3, then field 3 alone**

```text
$ cut -d, -f1,3 data/raw/D0_KPi.csv | head -n 3
M,TAU
1880.649,0.00041271152
1860.6599,0.0001864154
$ tail -n +2 data/raw/D0_KPi.csv |
    cut -d, -f3 | head -n 3
0.00041271152
0.0001864154
0.00018464602
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **The options**

- `-d,` names the sign that separates the values. For the raw pendulum file it is `-d';'`
- `-f1,3` names the fields to keep, counted from 1
- `-c1-3` keeps characters 1 to 3 of each line instead
- `cut` does not know what a header is. `tail -n +2` drops line 1 before it

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A line that ends in `|` goes on in the next line. `cut -d, -f2,3` is the deleted first column of Lecture 2, on any number of lines. It cuts at every separator: a CSV file with a comma inside quoted text needs a program that knows CSV.

</div>

<!--
Speaker: ask which field number TAU has before running the second command.
head -n 1 shows the names in order. (~2 min)
-->

---
hideInToc: true
---

# Order: `sort`

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔤 **As text**

```text
$ tail -n +2 data/processed/pendulum.csv |
    sort | head -n 3
100,20.01
20,9.02
30,11.05
```

`sort` compares characters from the left. `1` comes before `2`, so `100` comes before `20`. The editor did the same in Lecture 2.

</div>

<div class="card card-success card-glass pad-compact">

## 🔢 **As numbers**

```text
$ tail -n +2 data/processed/pendulum.csv |
    sort -n | head -n 3
20,9.02
30,11.05
40,12.61
```

`-n` reads the start of each line as a number and orders by its value.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`-r` reverses the order. `-t, -k2` orders by field 2 of lines whose fields are separated by `,`. `sort -t, -k2 -n -r` puts the row with the largest second value first.

</div>

<!--
Speaker: this is the last slide of the editing section of Lecture 2, now with
a way out: the option -n. (~2 min)
-->

---
hideInToc: true
---

# The Ends of a **Column**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⬇️ **The two smallest masses**

```text
$ tail -n +2 data/raw/D0_KPi.csv |
    cut -d, -f1 | sort -n | head -n 2
1766.2096
1808.1385
```

</div>

<div class="card card-secondary card-glass pad-compact">

## ⬆️ **The two largest masses**

```text
$ tail -n +2 data/raw/D0_KPi.csv |
    cut -d, -f1 | sort -n | tail -n 2
1920.3453
2453.6584
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Three filters: drop the header, keep field 1, order by value. Then `head` or `tail` takes one end. The column `M` runs from 1766.2096 to 2453.6584 MeV/c². The second value from each end is 1808.1385 and 1920.3453: one row at each end lies far from all the others.

</div>

<div class="card card-success card-glass pad-compact mt-sm">

✅ A sorted column shows its ends first, and a wrong value is usually at an end. Looking at both ends of every column is the first check of a new data file.

</div>

<!--
Speaker: 91 583 values are sorted in well under a second. Ask the room what
the values 1766 and 2453 might be before going on: nobody knows yet, and that
is the right answer. They get a line number later in the lecture. (~2 min)
-->

---
hideInToc: true
---

# `sort -n` and the **Decimal Sign**

<div class="card card-info card-glass pad-compact mt-sm">

```text
$ tail -n +2 data/raw/D0_KPi.csv | cut -d, -f3 > results/tau.txt
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🇱🇹 **A Mac set to Lithuanian**

```text
$ LC_ALL=lt_LT.UTF-8 sort -n results/tau.txt |
    head -n 3
-0.059467286
-0.09811119
-0.13715266
```

</div>

<div class="card card-success card-glass pad-compact">

## 🌐 **With no language rules**

```text
$ LC_ALL=C sort -n results/tau.txt |
    head -n 3
-100.0
-100.0
-100.0
```

</div>

</div>

<div class="card card-primary card-glass pad-compact mt-md">

`sort -n` takes the decimal sign from the language the computer is set to. In Lithuanian it is the comma, so the point in `-0.059467286` is not read as part of the number, and the smallest value, `-100.0`, is not first. `LC_ALL=C` before a program switches the language rules off: the decimal sign is the point on every computer. `echo $LANG` prints the setting, for example `lt_LT.UTF-8`.

</div>

<div class="note-text mt-sm">This is the decimal comma of Lecture 2 again. There it was in a file. Here it is in a setting of the computer.</div>

<!--
Speaker: the left side is what plain sort -n prints on a Mac whose language is
Lithuanian. On a laptop set to English both commands give the right side.
Whole numbers are not affected. (~2 min)
-->

---
hideInToc: true
---

# Count Repeats: `sort | uniq -c`

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ cut -d, -f3 data/raw/D0_KPi.csv | sort | uniq -c | sort -n | tail -n 3
   2 0.0026546149
   2 0.0035111452
  49 -100.0
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧮 **Stage by stage**

- `uniq` merges equal lines that stand next to each other. `-c` writes in front how many there were
- Equal lines stand together only after `sort`. Without it `uniq` gives all 91 584 lines back
- The second `sort -n` orders by the count, and `tail -n 3` keeps the three largest

</div>

<div class="card card-accent card-glass pad-compact">

## 🔎 **What it shows**

A measured decay time almost never comes twice: the most frequent real values occur 2 times. One value occurs 49 times, `-100.0`. A value that repeats like this is not a measurement. It is the mark for "no value".

</div>

</div>

<!--
Speaker: nobody told the pipeline about -100. Counting repeats found it. This
is how a missing-value mark is found in a file that comes without a
description. (~2 min)
-->

---
hideInToc: true
---

# Keep Lines: `grep`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔍 **Lines that contain a text**

```text
$ grep -c ',-100' data/raw/D0_KPi.csv
49
$ grep -n ',-100' data/raw/D0_KPi.csv |
    head -n 2
343:1818.1002,2978.644,-100.0,9901.186
965:1902.8027,2740.8074,-100.0,45169.31
$ grep -v ',-100' data/raw/D0_KPi.csv | wc -l
   91535
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🚩 **The options**

- `grep TEXT FILE` prints the lines that contain the text
- `-c` counts them instead
- `-n` puts the line number in front
- `-v` prints the lines **without** it: 91 535 here
- `-i` takes upper and lower case as equal

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The text is `',-100'`, with the comma and in single quotes. A first argument that starts with `-` is read as an option, and `grep -100 FILE` then waits for input that never comes. `Ctrl+C` ends the wait.

</div>

<!--
Speaker: the count is the number found with Ctrl+F in VS Code. grep
-c counts lines, the Find box counts matches. Here the two agree. (~2 min)
-->

---
hideInToc: true
---

# From `data/raw` to `data/processed`

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv
$ wc -l data/raw/D0_KPi.csv data/processed/D0_valid.csv
   91584 data/raw/D0_KPi.csv
   91535 data/processed/D0_valid.csv
  183119 total
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📥 **Read here, write there**

- The command reads the raw file and changes nothing in it
- Its output is a new file in `data/processed`: the header line and the 91 534 rows that have a decay time
- Delete the new file, run the line again, and the file is back

</div>

<div class="card card-success card-glass pad-compact">

## 📝 **The line is the description**

In Lecture 2 the README said in words what was done to a file by hand. Here the command says it, exactly: every line that contains `,-100` was left out. Whoever has the raw file and this line has the processed file.

</div>

</div>

<!--
Speaker: check the arithmetic with the room: 91 584 minus 49 is 91 535, and
one of those lines is the header. (~2 min)
-->

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

---
layout: section
hideInToc: true
---

# Regular **Expressions**

<!--
Speaker: so far Find and grep looked for a fixed text. A regular expression
describes a kind of text. The same patterns are used in the Find box of VS
Code and in grep. (~1 min)
-->

---
hideInToc: true
---

# A Pattern Instead of a **Text**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔎 **A fixed text finds too much**

```text
$ grep -c 1865 data/raw/D0_KPi.csv
1986
```

1986 lines contain `1865` somewhere: at the start of the mass, but also inside `PT`, `TAU` or `IPCHI2`. Wanted are the lines whose mass **starts** with 1865.

</div>

<div class="card card-success card-glass pad-compact">

## ✳️ **A pattern says where**

```text
$ grep -c '^1865' data/raw/D0_KPi.csv
1846
```

`^` stands for the start of the line. 1846 rows have a mass from 1865 up to 1866. The other 140 lines had `1865` in another place.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A **regular expression**, regex for short, is a text in which some signs do not stand for themselves. They stand for a kind of character, for a repetition or for a place in the line. The same signs work in `grep`, in the Find box of VS Code and in most programming languages.

</div>

<!--
Speaker: 1986 minus 1846 is 140. Show one of the 140 with
grep 1865 data/raw/D0_KPi.csv | grep -v '^1865' | head -n 1. (~2 min)
-->

---
hideInToc: true
---

# Signs for **One Character**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Sign | Fits | Pattern | Lines it fits in `data/processed/pendulum.csv` |
| --- | --- | --- | --- |
| a letter, a digit, `,` | itself | `20` | 2: `20,9.02` and `100,20.01` |
| `.` | any one character | `1.0` | 2: `30,11.05` and `100,20.01` |
| `\.` | a point | `1\.0` | 1: `30,11.05` |
| `[0-9]` | one character from `0` to `9` | `[0-9]0,` | all 9 rows |
| `[a-z]` | one lower-case letter | `[a-z]` | 1: the header line |
| `[^0-9]` | one character that is **not** listed | `[^0-9,.]` | 1: the header line |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔡 **Square brackets**

`[ ]` lists the characters that may stand in one place. `[0-9]` is short for `[0123456789]`. A `^` as the first sign inside turns the list round: every character except these.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **The point**

`.` fits any character, so `1.0` also fits `100`. A backslash takes the special meaning away: `\.` is a point and nothing else.

</div>

</div>

<!--
Speaker: each row can be run as grep -E 'PATTERN' data/processed/pendulum.csv.
Let the room predict the lines for 1.0 before you run it. (~3 min)
-->

---
hideInToc: true
---

# Signs for **How Many** and **Where**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Sign | Meaning | Pattern | Lines it fits in `data/raw/pendulum.csv` |
| --- | --- | --- | --- |
| `+` | one or more of what stands before it | `[0-9]+;` | 9: the rows, at `1;` and at `20;` |
| `*` | none or more | `;.*;` | all 11 |
| `{3}` | exactly three | `;[0-9]{3};` | 1: `9;100;20,01` |
| `^` | the start of the line | `^;` | 1: `;mean;15,14` |
| `$` | the end of the line | `0$` | 2: `7;80;17,90` and `8;90;19,10` |
| `( )` and `\|` | a group, and "or" inside it | `(01\|02)$` | 2: `1;20;9,02` and `9;100;20,01` |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔁 **Repetition**

`+`, `*` and `{3}` act on the one thing before them: a character, a `[ ]` or a group in `( )`. `[0-9]+` is a whole number of any length.

</div>

<div class="card card-accent card-glass pad-compact">

## 📌 **Place**

`^` and `$` fit no character. They pin the pattern to an end of the line. `^[0-9]+$` fits a line that is one whole number and nothing else.

</div>

</div>

<!--
Speaker: the raw file has 11 lines: the header, nine rows and the mean line.
The pattern ^; finds the mean line without the word mean. (~3 min)
-->

---
hideInToc: true
---

# Regex in the **Find Box** of VS Code

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **Switch it on**

- `Ctrl+F` opens Find (macOS `Cmd+F`)
- The button `.*` at the right end of the box switches regular expressions on: `Alt+R` (macOS `Cmd+Option+R`)
- The counter shows the number of matches while the pattern is typed

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧪 **A pattern, built in three steps**

```text
In data/raw/pendulum.csv

Find          Matches
[0-9]+        39     every number
[0-9]+;       18     a number before a ;
^[0-9]+;       9     the first one in a line
```

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ The third pattern fits the row number with its semicolon, once in each of the nine rows. The counter is the check: nine rows, nine matches. Replaced by nothing, the column `nr` is gone from the rows. In Lecture 2 this took a cursor on every line.

</div>

<div class="note-text mt-sm">A file in <code>data/raw</code> is searched, never replaced in. Replace on a copy in <code>data/processed</code>.</div>

<!--
Speaker: open the raw pendulum file, switch the button on and type the three
patterns. Read the counter aloud after each. (~3 min)
-->

---
hideInToc: true
---

# Capture **Groups**

<div class="card card-info card-glass pad-compact mt-sm">

Round brackets mark a part of the match. In the Replace box `$1` stands for what the first pair of brackets matched, and `$2` for the second.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔁 **The decimal comma**

```text
Find      ([0-9]),([0-9])
Replace   $1.$2
```

`9,02` becomes `9.02`: both digits are put back, with a point between them. The raw file has 10 matches. A semicolon is never touched, so this replacement can come before or after the other one.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📋 **A row of a Markdown table**

```text
Find      ^(.*),(.*)$
Replace   | $1 | $2 |
```

`20,9.02` becomes `| 20 | 9.02 |`. One replacement on the 10 lines of the cleaned file does what three edits with many cursors did in Lecture 2.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Replace All with a pattern changes every match at once, also the ones nobody looked at. Read the counter first. If the number is not the one expected, the pattern is wrong.

</div>

<!--
Speaker: do the first replacement on a fresh copy of the raw file in
data/processed, then Ctrl+Z. The 10 matches are the nine rows and the mean
line. (~3 min)
-->

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

<div class="card card-warning card-glass pad-compact">

## 🐘 **`^.*,`**

```text
$ grep -oE '^.*,' data/raw/D0_KPi.csv |
    head -n 2
M,PT,TAU,
1880.649,3000.9534,0.00041271152,
```

`.*` runs to the **last** comma of the line: three fields, not one.

</div>

<div class="card card-success card-glass pad-compact">

## 🎯 **`^[^,]*`**

```text
$ grep -oE '^[^,]*' data/raw/D0_KPi.csv |
    head -n 2
M
1880.649
```

`[^,]*` cannot run past a comma: it stops at the **first** one.

</div>

</div>

<div class="card card-primary card-glass pad-compact mt-md">

`*` and `+` take as many characters as they can while the rest of the pattern still fits. A pattern for one field says what the field may not contain: `[^,]*` is "any characters except the separator". The option `-o` makes `grep` print only the part that matched, not the whole line.

</div>

<!--
Speaker: this is the usual first surprise with regular expressions. In the
table-row pattern of the last slide it did no harm, because the cleaned file
has one comma per line. (~2 min)
-->

---
hideInToc: true
---

# The Same Patterns in the Shell: `grep -E`

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ grep -cE '[0-9],[0-9]' data/raw/pendulum.csv
10
$ grep -cE '^18[5-7]' data/raw/D0_KPi.csv
41091
$ grep -nE '^(17|180|19[2-9]|2)' data/raw/D0_KPi.csv
10048:2453.6584,755.2686,0.2276815,1.0500937
43608:1808.1385,3632.4104,0.06656479,11200.344
67877:1920.3453,4999.695,0.00015124853,1.0319226
89861:1766.2096,12493.022,0.0037266747,214.38336
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🚩 **`-E` and the quotes**

- `-E` switches on the full set of signs: `+`, `{ }`, `( )`, `|`
- The pattern stands in single quotes. Without them the shell reads `*`, `[ ]`, `$` and `|` itself

</div>

<div class="card card-accent card-glass pad-compact">

## 🔎 **What the three lines found**

- 10 lines of the raw table have a decimal comma
- 41 091 rows, 45% of the file, have a mass from 1850 to 1880
- The four rows outside 1810 to 1920, with their line numbers

</div>

</div>

<!--
Speaker: the last command gives the two ends of the sorted mass column a line
number each. Ctrl+G in VS Code goes to line 10048. (~3 min)
-->

---
hideInToc: true
---

# Wildcards Are Not **Regular Expressions**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| | Wildcard | Regular expression |
| --- | --- | --- |
| Read by | the shell, for file names | `grep -E`, the Find box of VS Code |
| Any one character | `?` | `.` |
| Any number of characters | `*` | `.*` |
| One of a list | `[pr]` | `[pr]` |
| Must fit | the whole name | any part of the line, unless `^` and `$` pin it |
| Every CSV file | `*.csv` | `.*\.csv$` |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **`\d` is not everywhere**

VS Code and `grep` on macOS read `\d` as a digit. `grep` in Git Bash and on Linux does not: there `grep -cE '\d,\d' data/raw/pendulum.csv` gives 0 where 10 is right. `[0-9]` works in all of them.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **`$` and Windows line endings**

In a file with CRLF line endings the byte `0D` stands before every line break. For `grep` it is the last character of the line, and `0$` fits nothing. `tr -d '\r'` in front of `grep` removes it.

</div>

</div>

<!--
Speaker: both warnings are the same lesson as the decimal sign: a pattern that
works on one laptop is tested on the other system before it goes into a
script. The Find box of VS Code handles both line endings. (~2 min)
-->

---
layout: section
hideInToc: true
---

# A First **Script**

<!--
Speaker: a line that is typed twice goes into a file. The file is run with one
command, today and next month. (~1 min)
-->

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

---
hideInToc: true
---

# Run a Program **Someone Else Wrote**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🐍 **A script in Python**

```text
$ python scripts/column_stats.py data/raw/D0_KPi.csv TAU
file    data/raw/D0_KPi.csv
column  TAU
rows    91583
min     -100.0
max     0.5787994
mean    -0.0525221
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **The same shape as `bash FILE`**

- `python` is a program. Its first argument is the file to run
- The words after the file name go to the script: a path and a column name
- On macOS the program is called `python3`
- `column_stats.py` is handed out with this lecture. It is used like `wc`: it is run, and nobody has to read it

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`bash FILE.sh` and `python FILE.py` are the two forms a README needs. `wc` and `sort` count and order. They do not compute a mean: that takes a program, and this one is about 50 lines that someone else wrote and tested.

</div>

<!--
Speaker: the file is in scripts, put there before the lecture. Run it for M as
well: 91 583 rows, mean 1864.1. Do not open the file. (~2 min)
-->

---
hideInToc: true
---

# What 49 Rows Do to a **Mean**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📥 **`data/raw/D0_KPi.csv`**

```text
rows    91583
min     -100.0
max     0.5787994
mean    -0.0525221
```

The mean decay time is negative. No particle decays before it is made.

</div>

<div class="card card-success card-glass pad-compact">

## ⚙️ **`data/processed/D0_valid.csv`**

```text
rows    91534
min     -0.13715266
max     0.5787994
mean    0.000981802
```

Without the 49 marked rows the mean is 0.00098 ns.

</div>

</div>

<div class="card card-primary card-glass pad-compact mt-md">

49 rows are 0.05% of the file. Each puts −100 into the sum: 49 × (−100) / 91 583 = −0.0535. That moves the mean from +0.00098 to −0.0525, more than fifty times its own size and with the wrong sign. A mark for "no value" that is written as a number is counted as a number by every program.

</div>

<div class="note-text mt-sm">The smallest value left is −0.137 ns. Three rows have a small negative time. They are not marks, and whether to keep them is a question about the measurement.</div>

<!--
Speaker: run the script on both files. This is why the fifth question of
Lecture 2, how missing values are marked, is asked before any number is
computed. (~3 min)
-->

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

---
layout: section
hideInToc: true
---

# Checksums & **Backups**

<!--
Speaker: Lecture 3 worked a checksum by hand and named SHA-256. Here it is a
command, used for three things: comparing two files, guarding the raw data,
checking a backup. (~1 min)
-->

---
hideInToc: true
---

# The Checksum of a **File**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ shasum -a 256 data/raw/D0_KPi.csv
25c3c97299ea844f27308fde20a00ecaa87580868f3c767d7ade5621c1505136  data/raw/D0_KPi.csv
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ⌨️ **Two names for one program**

```text
macOS             shasum -a 256 FILE
Git Bash, Linux   sha256sum FILE
```

Both print the SHA-256 of Lecture 3: 64 hex digits, which are 256 bits, computed from every byte of the file.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧬 **One byte changes all of it**

```text
be05af03…aff0870b   20,9.02
17dbc893…a1440bc9   20,9.03
```

The checksum of the cleaned pendulum table, and of a copy in which one digit was changed.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ The 3 926 142 bytes of `D0_KPi.csv` give these 64 digits on every laptop in the room. A laptop that prints other digits has another file.

</div>

<!--
Speaker: ask the room to run the command and compare the first four and the
last four digits with the slide: 25c3 and 5136. (~2 min)
-->

---
hideInToc: true
---

# The Script **Against the Hand**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
$ shasum -a 256 data/processed/pendulum.csv data/processed/pendulum_script.csv
be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum.csv
be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum_script.csv
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 🟰 **The same 97 bytes**

The table cleaned by hand in Lecture 2 and the table written by `clean_pendulum.sh` have the same checksum. The script does exactly what the hands did.

</div>

<div class="card card-secondary card-glass pad-compact">

## 💻 **On every laptop**

The files cleaned by hand in the room have 96, 97, 105 or 107 bytes: the line ending and the last line break differ (Lecture 3). The script writes LF and a final line break on every system, so its output is `be05af03…` everywhere.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A checksum says whether two files differ. `diff A B` says where: it prints the lines that differ, and nothing at all when the files are the same.

</div>

<!--
Speaker: this is the result the lecture was built towards. A procedure that
was done by hand and described in words is now a file, and a checksum shows
that the file reproduces the hand work byte for byte. (~3 min)
-->

---
hideInToc: true
---

# A List of Checksums for `data/raw`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📝 **Write the list, check the list**

```text
$ shasum -a 256 data/raw/*.csv > data/checksums.txt
$ shasum -a 256 -c data/checksums.txt
data/raw/D0_KPi.csv: OK
data/raw/pendulum.csv: OK
```

</div>

<div class="card card-warning card-glass pad-compact">

## 🚨 **After a change in a raw file**

```text
$ shasum -a 256 -c data/checksums.txt
data/raw/D0_KPi.csv: OK
data/raw/pendulum.csv: FAILED
shasum: WARNING: 1 computed checksum
did NOT match
```

</div>

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

- `-c` reads the list, computes each checksum again and compares
- The list is written once, when the raw files arrive. It is checked after a copy to another disk, and before work that will be handed in
- Git Bash and Linux: `sha256sum data/raw/*.csv > data/checksums.txt`, then `sha256sum -c data/checksums.txt`

</div>

<div class="note-text mt-sm">The list is one line per file: the 64 digits, two spaces, the path. It stands in <code>data</code>, not in <code>data/raw</code>, so that <code>data/raw/*</code> never includes it.</div>

<!--
Speaker: add a character to a copy of the raw pendulum file to show FAILED,
not to the file itself. "Raw is never edited" now has a test. (~2 min)
-->

---
hideInToc: true
---

# How Files **Are Lost**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| What happens | What is lost | What brings it back |
| --- | --- | --- |
| `rm`, `>` or `mv` hits the wrong file. A spreadsheet is saved over a raw file | One file, at once | An older copy |
| The disk fails. The laptop is lost or stolen | Everything on it | A copy on another device |
| Laptop and USB stick are in one bag. Fire or theft in the room | Every copy in that place | A copy in another place |
| A file changes without notice: a broken copy, a sync conflict | Unknown, and noticed late | A checksum to notice it, an older copy to go back to |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔁 **What can be made again**

`data/processed` and `results`: the scripts write them again from `data/raw`.

</div>

<div class="card card-warning card-glass pad-compact">

## 🧱 **What cannot**

`data/raw`, `scripts`, the README and a written report. These are the files a backup is for.

</div>

</div>

<!--
Speaker: ask who has lost a file in one of these four ways. Usually every row
of the table gets a hand. (~2 min)
-->

---
hideInToc: true
---

# Backups: the **3-2-1 Rule**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 3️⃣ **Three copies**

The working copy on the laptop, and two more. One copy is no backup: the first row of the table needs an older one.

</div>

<div class="card card-secondary card-glass pad-compact">

## 2️⃣ **Two kinds of storage**

The disk of the laptop, and an external drive or a server. A second folder on the same disk fails together with the first.

</div>

<div class="card card-accent card-glass pad-compact">

## 1️⃣ **One in another place**

University storage, a cloud service, or a drive kept at home. A drive in the laptop bag is stolen with the laptop.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 Suppose one copy is lost within a year with probability 1 in 20. Two copies that fail independently are both lost with probability (1/20)² = 1 in 400, three with (1/20)³ = 1 in 8000. The numbers hold only for independent copies. Two copies on one disk, or in one bag, are lost together: that is what the 2 and the 1 of the rule are for.

</div>

<!--
Speaker: the 1 in 20 is an assumption for the arithmetic, not a measured rate.
The point is the exponent, and the condition under which it applies. (~2 min)
-->

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

<div class="card card-secondary card-glass pad-compact">

## 💾 **To a USB drive**

```text
$ cp -r . /Volumes/USB/analysis-project_2026-10-13
$ cd /Volumes/USB/analysis-project_2026-10-13
$ shasum -a 256 -c data/checksums.txt
data/raw/D0_KPi.csv: OK
data/raw/pendulum.csv: OK
$ cd ~/Documents/analysis-project
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ A folder that syncs, such as OneDrive, Google Drive or Dropbox, is a copy in another place. It is not an older copy: a file deleted or overwritten on the laptop is deleted or overwritten there within seconds. The dated folder on the drive stays as it was on that day.

</div>

<div class="note-text mt-sm">Git Bash names the drive <code>E:</code> as <code>/e</code>: <code>cp -r . /e/analysis-project_2026-10-13</code>.</div>

<!--
Speaker: a backup that was never opened is a hope, not a backup. The check
with the list of checksums takes a second and is the reason the list exists.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The **README**

<!--
Speaker: the README of the project folder has grown for three weeks. This
section completes it, with what the commands of today have found. (~1 min)
-->

---
hideInToc: true
---

# What the README **Still Lacks**

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **Written in Lectures 2 and 3**

- A title, one paragraph, the author
- The folders and what goes into each
- For each data file: source, DOI, licence, date, size, what one row is
- The edits made by hand
- File anatomy: encoding, line ending, separator

</div>

<div class="card card-warning card-glass pad-compact">

## ❓ **A stranger still cannot tell**

- What each column means, and its unit
- How a missing value is marked
- Whether the raw files are the ones that were downloaded
- Which commands make `data/processed` and `results`, and in which order
- What may be done with the scripts and the text

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The test for a README: someone with an empty laptop and the project folder gets the same results, and asks nobody. Each line of the right-hand card is a question that person would have to ask.

</div>

<!--
Speaker: open the README of the project folder next to the slide and tick the
left-hand card off against it. (~2 min)
-->

---
hideInToc: true
---

# Anatomy of a **README**

<div class="grid-3 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🏷️ **Title, one paragraph**

What the project is, in words that someone outside the field understands.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🗂️ **Data**

Source, DOI, licence, the date it was fetched, and the checksum of every raw file.

</div>

<div class="card card-accent card-glass pad-compact">

## 📏 **Columns and units**

One line per column: name, meaning, unit, and the mark for a missing value.

</div>

<div class="card card-info card-glass pad-compact">

## 📁 **Folders**

What is in `data/raw`, `data/processed`, `scripts` and `results`.

</div>

<div class="card card-success card-glass pad-compact">

## ▶️ **How to rebuild**

The commands, in order, that make every file in `data/processed` and `results`.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚖️ **Licence, contact**

What others may do with the work, and whom to ask.

</div>

</div>

<div class="note-text mt-md">The first, second and fourth part exist since Lecture 2. The other three are written from what was run in this lecture.</div>

---
hideInToc: true
---

# Columns and **Units**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **Source**

```md
## Columns of `D0_KPi.csv`

| Column | Meaning | Unit |
|--|--|--|
| `M` | mass of the K⁻π⁺ pair | MeV/c² |
| `PT` | transverse momentum | MeV/c |
| `TAU` | decay time | ns |
| `IPCHI2` | χ² of the impact parameter | none |

Missing value: `TAU` is `-100.0` in 49 rows.
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 👁️ **Preview**

<div class="rendered-md">
<p class="rendered-section">Columns of <code>D0_KPi.csv</code></p>
<table>
<thead>
<tr><th>Column</th><th>Meaning</th><th>Unit</th></tr>
</thead>
<tbody>
<tr><td><code>M</code></td><td>mass of the K⁻π⁺ pair</td><td>MeV/c²</td></tr>
<tr><td><code>PT</code></td><td>transverse momentum</td><td>MeV/c</td></tr>
<tr><td><code>TAU</code></td><td>decay time</td><td>ns</td></tr>
<tr><td><code>IPCHI2</code></td><td>χ² of the impact parameter</td><td>none</td></tr>
</tbody>
</table>
<p>Missing value: <code>TAU</code> is <code>-100.0</code> in 49 rows.</p>
</div>

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Every line can be checked by a command: the names by `head -n 1`, the 49 rows by `grep -c ',-100'`, the ranges by `scripts/ranges.sh`. The units are the one thing no command finds. The file does not hold them, so the README has to.

</div>

<!--
Speaker: the table is the Markdown of Lecture 2. What is new is where its
content comes from: from commands that anyone can run again. (~2 min)
-->

---
hideInToc: true
---

# How to **Rebuild**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **In the README**

```md
## How to rebuild

Run in the project folder, in Git Bash
(Windows) or the terminal (macOS, Linux).

1. `bash scripts/clean_pendulum.sh`
   writes `data/processed/pendulum_script.csv`
2. `bash scripts/ranges.sh data/raw/D0_KPi.csv`
   prints the range of each column
3. `shasum -a 256 -c data/checksums.txt`
   checks the raw files
   (Git Bash: `sha256sum -c data/checksums.txt`)
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧪 **Test the section**

1. Delete `data/processed/pendulum_script.csv`
2. Copy each command out of the README into the terminal, in order
3. Compare the checksum of the new file with the old one: `be05af03…`

A command that was copied out of the README and ran has been tested. A command typed into the README from memory has not.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

♻️ The entry "Mean line deleted, `,` replaced by `.`" of Lecture 2 described the work. This section **is** the work: three lines that run.

</div>

<!--
Speaker: run the test live. rm the file, copy command 1 from the preview of
the README, paste, run, then shasum. (~3 min)
-->

---
hideInToc: true
---

# The **Licence**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📥 **The licence of the data**

- Set by whoever published the data. Lecture 2 read it off the record: CC0 for record 401
- It decides whether the raw file may be passed on with the project
- If it may not, the folder is passed on without the file, and the README says where to fetch it

</div>

<div class="card card-secondary card-glass pad-compact">

## 📤 **The licence of your own work**

- Without a licence the law reserves every right: others may read the scripts and the text, and may not copy, change or pass them on
- The text of the licence goes into a file named `LICENSE` in the project folder
- Usual choices: MIT for scripts, CC BY 4.0 for text and figures, CC0 for data you measured yourself

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

```md
## Licence

Data: CC0, CERN Open Data Portal, record 401.
Scripts and text: MIT, see `LICENSE`.
```

</div>

<!--
Speaker: choosealicense.com has the text of each licence, ready to copy into
the file. MIT allows any use as long as the notice stays in the file. CC BY
asks that the author is named. (~2 min)
-->

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Open a terminal with `bash` or `zsh`, and name a file by an **absolute** or a **relative path**

</div>

<div class="card card-success card-glass pad-compact">

✅ Read, count, make, copy, move, delete and find files with commands, and name many with a **wildcard**

</div>

<div class="card card-success card-glass pad-compact">

✅ Join `cut`, `sort`, `uniq -c`, `grep` and `tr` with **pipes**, and write the result into `data/processed`

</div>

<div class="card card-success card-glass pad-compact">

✅ Write a **regular expression** with `[ ]`, `+`, `^`, `$` and groups, in the Find box and with `grep -E`

</div>

<div class="card card-success card-glass pad-compact">

✅ Put commands into a **script** with variables and a `for` loop, and run it with `bash`

</div>

<div class="card card-success card-glass pad-compact">

✅ Show with a **checksum** that two files are the same, and keep copies by the **3-2-1** rule

</div>

<div class="card card-success card-glass pad-compact">

✅ Complete a **README**: columns and units, how to rebuild, licence

</div>

</div>

<!--
Speaker: one line per section of the lecture. The hand edits of Lecture 2
became a script, and a checksum showed that the script does the same. (~1 min)
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

---
hideInToc: true
---

<MCQ
  question="The terminal is in analysis-project/results. Which path names the raw pendulum file?"
  :options="[
    '<code>data/raw/pendulum.csv</code>',
    '<code>../data/raw/pendulum.csv</code>',
    '<code>/data/raw/pendulum.csv</code>',
    '<code>~/data/raw/pendulum.csv</code>'
  ]"
  :correct="1"
  explanation="A relative path starts at the folder the terminal is in. Two points go up one level, from results to analysis-project, and from there the path goes down into data and raw. The first answer is right only when the terminal is in the project folder. A path that starts with a slash starts at the top of the disk, and the tilde stands for the home folder."
/>

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

---
hideInToc: true
---

<MCQ
  question="notes.txt has five lines. Then two commands run: `echo done > notes.txt` and `echo checked >> notes.txt`. What does `wc -l notes.txt` count now?"
  :options="[
    '7 lines',
    '6 lines',
    '2 lines',
    '1 line'
  ]"
  :correct="2"
  explanation="A single > empties the file before the new line is written, so the five lines are gone and the file holds one line. The double >> adds a second line at the end. A single > on a file that is still needed is one of the ways files are lost."
/>

---
hideInToc: true
---

<MCQ
  question="A file has four lines: 20,9.02 and 100,20.01 and length_cm,t10_s and 7;80;17,90. Which lines does `grep -E '^[0-9]+,[0-9]+\.[0-9]+$'` print?"
  :options="[
    'All four lines',
    'The lines 20,9.02 and 100,20.01',
    'Only the line 20,9.02',
    'The lines 20,9.02 and 100,20.01 and 7;80;17,90'
  ]"
  :correct="1"
  explanation="The pattern fits a whole line that is a number, a comma, a number, a point and a number. The header line has letters. The line with semicolons has no point, and it does not start with a number followed by a comma. The plus sign lets the first number have two digits or three."
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
  explanation="The sum of the 990 real values is 1980. The ten marks add -9990. The mean of all rows is (1980 - 9990) / 1000 = -8.01. One row in a hundred is enough to give the mean the wrong sign. The marked rows are taken out first."
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
