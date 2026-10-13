

<!-- Parked 2026-10-11 from Lecture 04, section The Shell, after slide 'A Command That Fails': on the 90-minute skip list; the section Tools & Environments took its time -->

---
hideInToc: true
---

# A Path That **Fails**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cat data/raw/D0_KPi.cvs
cat: data/raw/D0_KPi.cvs: No such file or directory
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> cat data/raw/D0_KPi.cvs
Get-Content: Cannot find path
'C:\Users\smilte\Documents\analysis-project\
data\raw\D0_KPi.cvs' because it does not
exist.
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The program complains this time, not the shell: `cat` on macOS, `Get-Content` behind the alias `cat` in PowerShell. PowerShell turns the relative path into an absolute one and shows where it looked. The fix is the same in both shells: `pwd`, then `ls`, and complete the name with `Tab`.

</div>

<!--
Speaker: the typo is cvs for csv. A command
that works prints only what was asked for; a message means something went
wrong, and its first word says who noticed. (~2 min)
-->


<!-- Parked 2026-10-11 from Lecture 04, section Checksums & Backups, first slide: the same derivation stands in Lecture 03 (A Checksum by Hand); on the 90-minute skip list -->

---
hideInToc: true
---

# A Checksum **by Hand**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ➕ **Add up the bytes**

```text
a    b    c
97 + 98 + 99 = 294
294 mod 256  =  38

a    c    b
97 + 99 + 98 = 294   →   38
```

The sum, kept to one byte, is 38. Swap two letters and it stays 38: this change goes unseen.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔐 **SHA-256 mixes every byte**

```text
abc   ba7816bf…f20015ad
acb   8e976608…e272fa57
```

The same three bytes in another order give other digits, all 64 of them. Nobody has found two different files with the same SHA-256.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 A checksum is a short number computed from every byte of a file. The same bytes always give the same number. Other digits mean other bytes, and that is what the check rests on.

</div>

<!--
Speaker: work the sum on the board: a is 97, b 98, c 99 (the ASCII table of
Lecture 3). mod 256 keeps the remainder after dividing by 256, so the sum fits
one byte: 294 - 256 = 38. The hashes are the SHA-256 of the three bytes abc
and acb (printf abc | shasum -a 256 on a Mac); only the first and last eight
of 64 hex digits are shown. (~2 min)
-->


<!-- Parked 2026-10-13 from Lecture 04, section Opening, slide 3 'Learning Objectives': the lecture now opens on the number to check, 7.16, and the table of its steps -->

---
hideInToc: true
---

# Learning **Objectives**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🐚 Set up the **shell** of your laptop, read its prompt, and move between folders

</div>

<div class="card card-secondary card-glass pad-compact">

📁 Read, count, copy, move and delete **files** with typed commands

</div>

<div class="card card-accent card-glass pad-compact">

🔗 Join commands with **pipes**, and find the mark for "no value" in 87 672 rows

</div>

<div class="card card-info card-glass pad-compact">

🔎 Describe a kind of text with a **regular expression**

</div>

<div class="card card-success card-glass pad-compact">

⚙️ Run a **script** someone else wrote, install a program and a package, and give a project its own **environment**

</div>

<div class="card card-warning card-glass pad-compact">

🛡️ Tell files apart by **checksum**, keep **backups**, and write down how every file is made again: in the README and in a **shell script**

</div>

</div>

<!--
**Say:** one line per part of the lecture. One small project folder runs through all of them.
(~1 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Opening, slide 6 '(no title)': the three questions became the steps of the check of 7.16; VS Code keys left with the clicking -->

---
hideInToc: true
---

<div class="card card-primary card-glass pad-compact table-compact">

| Question about `weather.csv` | In VS Code | Answer |
| --- | --- | --- |
| How many lines? | `Ctrl+End`, read the line number | 87 673 |
| What is on line 5000? | `Ctrl+G`, type `5000` | `2016-07-27T06:00,18.2,71,1.1` |
| What was the coldest hour? | no key does it | ? |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🖱️ **A click**

Leaves the answer on the screen. For the next file, every step is done again by hand.

</div>

<div class="card card-success card-glass pad-compact">

## ⌨️ **A typed line**

Answers all three. The line can be kept in the README and run again on the next file.

</div>

</div>

<!--
**Ask:** how would you find the coldest hour among 87 672?
**Say:** leave the question open. A typed line answers it in the middle of the lecture.
**If asked:** on a Mac the keys are `Cmd+↓` and `Ctrl+G`.
(~3 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Set Up the Shell, slide 9 '(no title)': the shell slide now names zsh on macOS and Git Bash on Windows (13 Oct 2026) -->

---
hideInToc: true
---

<div class="card card-primary card-glass pad-compact table-compact">

| Laptop | Shell of this course | Comes with the system? | Its prompt ends in |
| --- | --- | --- | --- |
| macOS | `zsh` | Yes, the default since macOS 10.15 (2019) | `%` |
| Windows | PowerShell 7 | No. Windows has the older Windows PowerShell 5.1 | `>` |

</div>

<div class="note-text mt-md">On these slides <code>%</code> starts a zsh line and <code>PS&gt;</code> a PowerShell line. Nobody types either: the shell prints it.</div>

<!--
**Say:** two shells, one per system. The ideas are the same in both, the words often differ. Every command slide shows both side by side.
**If asked:** Linux usually has bash. Almost every zsh line of this lecture runs there unchanged.
(~1 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Set Up the Shell, slide 10 'macOS: Check the Shell': replaced by the macOS install slide (Homebrew, Git, Miniforge); chsh is a note there -->

---
hideInToc: true
---

# macOS: Check the **Shell**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **Open Terminal**

`Cmd+Space`, type `Terminal`, `Enter`. Then:

```text
smilte@MacBook-Air ~ % echo $SHELL
/bin/zsh
```

`SHELL` is a **variable**: a name the shell keeps a value under. `$SHELL` reads it, `echo` prints it.

</div>

<div class="card card-warning card-glass pad-compact">

## 🔁 **If it prints `/bin/bash`**

```text
MacBook-Air:~ smilte$ chsh -s /bin/zsh
Changing shell for smilte.
Password for smilte:
```

`chsh` changes the shell, `-s` names the new one. Close the window, open a new one: `/bin/zsh`.

</div>

</div>

<!--
**Ask:** who sees `/bin/bash`? Their account is older than 2019.
**Say:** zsh is already on the disk at `/bin/zsh`; `chsh` only makes it the default.
**If asked:** bash prints "The default interactive shell is now zsh" when it starts. The password is the Mac's login password, and nothing appears while it is typed. bash prompts end in `$`, zsh prompts in `%`.
(~3 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Set Up the Shell, slide 12 'Open a Terminal in VS Code': step-by-step clicking left the lecture; one line on the Windows set-up slide names the default profile -->

---
hideInToc: true
---

# Open a Terminal in **VS Code**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS**

1. **File > Open Folder**: `weather-project`
2. **Terminal > New Terminal**
3. The Panel opens, in the project folder, with `zsh` at its top right

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows**

1. **File > Open Folder**: `weather-project`
2. `Ctrl+Shift+P`, **Terminal: Select Default Profile**, **PowerShell**
3. **Terminal > New Terminal**: `pwsh` at the top right

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ The terminal of VS Code opens in the folder that VS Code has open. Editor and terminal show the same files.

</div>

<!--
**Say:** on Windows the list offers PowerShell (that is 7) and Windows PowerShell (5.1). Pick PowerShell.
**If asked:** `Ctrl+`` (backtick) opens and closes the Panel.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section First Commands, slide 14 'Read the Prompt': Lecture 03 taught it; one recap slide holds the commands of Lecture 03 -->

---
hideInToc: true
---

# Read the **Prompt**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
smilte@MacBook-Air weather-project %
```

- `smilte@MacBook-Air`: user and computer
- `weather-project`: the folder the shell is in
- `%`: the shell waits

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS C:\Users\smilte\Documents\weather-project>
```

- `PS`: PowerShell
- `C:\…\weather-project`: the folder, as a whole path
- `>`: the shell waits

</div>

</div>

<div class="note-text mt-md">The folder in the prompt is the <strong>working directory</strong>. Every command starts there.</div>

<!--
**Ask:** read the two prompts on the slide aloud, part by part.
**Say:** zsh shows only the last folder, PowerShell the whole path. Both name the same thing.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section First Commands, slide 15 'Run a Command: `echo`': one recap slide holds the commands of Lecture 03 -->

---
hideInToc: true
---

# Run a Command: `echo`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% echo hello
hello
%
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> echo hello
hello
PS>
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

1. Type the line. Nothing happens yet
2. `Enter`: the shell runs it
3. The program prints its answer
4. The prompt comes back: the next line can be typed

</div>

<!--
**Say:** `echo` prints what follows it. The four steps are the same for every command today.
(~1 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section First Commands, slide 16 'Where Am I: `pwd`': Lecture 03 taught it; one recap slide holds the commands of Lecture 03 -->

---
hideInToc: true
---

# Where Am I: `pwd`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% pwd
/Users/smilte/Documents/weather-project
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> pwd

Path
----
C:\Users\smilte\Documents\weather-project
```

</div>

</div>

<div class="note-text mt-md"><code>pwd</code>, print working directory: the folder of the prompt, as a whole path. The same word in both shells.</div>

<!--
**Ask:** why would three laptops print three different answers? The user name differs.
**If asked:** in PowerShell `pwd` is a short name for `Get-Location`; it prints a small table with one column, `Path`.
(~1 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section First Commands, slide 17 'What Is Here: `ls`': Lecture 03 taught it; one recap slide holds the commands of Lecture 03 -->

---
hideInToc: true
---

# What Is Here: `ls`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% ls
README.md  data  results  scripts
% ls data
processed  raw
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> ls

    Directory: C:\Users\smilte\Documents\weather-project

Mode           LastWriteTime   Length Name
----           -------------   ------ ----
d----    2026-10-13  09:00            data
d----    2026-10-13  09:00            results
d----    2026-10-13  09:00            scripts
-a---    2026-10-13  09:00        688 README.md
```

</div>

</div>

<div class="note-text mt-md"><code>ls</code>, list: the names in a folder. Without a name it lists the working directory, with a name it lists that folder.</div>

<!--
**Say:** PowerShell prints a table: `d` marks a folder, `Length` is the size of a file in bytes.
**If asked:** the date column follows the laptop's date settings.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section First Commands, slide 18 'Change Folder: `cd`': Lecture 03 taught it; one recap slide holds the commands of Lecture 03 -->

---
hideInToc: true
---

# Change Folder: `cd`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
smilte@MacBook-Air weather-project % cd data
smilte@MacBook-Air data % ls
processed  raw
smilte@MacBook-Air data % cd ..
smilte@MacBook-Air weather-project %
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS C:\…\weather-project> cd data
PS C:\…\weather-project\data> ls -Name
processed
raw
PS C:\…\weather-project\data> cd ..
PS C:\…\weather-project>
```

</div>

</div>

<div class="note-text mt-md"><code>cd</code>, change directory: the prompt shows the new folder. <code>..</code> is the folder one level up.</div>

<!--
**Do:** follow the prompt: it changes after each `cd`.
**Say:** `-Name` makes PowerShell's `ls` print names only.
**If asked:** `cd` alone goes to the home folder in zsh; in PowerShell `cd ~` does it.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section First Commands, slide 19 'Absolute Paths': merged into Paths That Work on Every Laptop -->

---
hideInToc: true
---

# Absolute **Paths**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌳 **Folders form a tree**

```text
/                       C:\ on Windows
└─ Users
   └─ smilte
      └─ Documents
         └─ weather-project
            └─ data
               └─ raw
                  └─ weather.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📍 **On macOS and on Windows**

```text
/Users/smilte/Documents/weather-project/data/raw/weather.csv
C:\Users\smilte\Documents\weather-project\data\raw\weather.csv
```

An absolute path starts at the top: `/` on macOS, `C:\` on Windows.

</div>

</div>

<div class="note-text mt-md">It names one file on one computer. On another laptop the user name, and so the path, differs.</div>

<!--
**Say:** read the path from left to right as a walk down the tree. macOS separates folders with `/`, Windows with `\`.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section First Commands, slide 22 'Spaces in Names': merged into What the Shell Does with a Line -->

---
hideInToc: true
---

# Spaces in **Names**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% head -n 2 weather station.csv
head: weather: No such file or directory
head: station.csv: No such file or directory
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Content -Head 2 weather station.csv
Get-Content: A positional parameter cannot
be found that accepts argument 'station.csv'.
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ A space ends an argument: the shell reads two names. Quotes hold a name together, `"weather station.csv"`, and names without spaces need no quotes at all.

</div>

<!--
**Say:** this is why the project folder uses `_` and `-` and never a space.
(~1 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section First Commands, slide 24 'Keys for the Shell': merged into Complete Names with Tab -->

---
hideInToc: true
---

# Keys for the **Shell**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Key or line | What it does | zsh | PowerShell |
| --- | --- | --- | --- |
| `↑` `↓` | the earlier lines, one at a time | ✓ | ✓ |
| `Ctrl+R` | search the earlier lines | ✓ | ✓ |
| `Ctrl+C` | stop the program that runs | ✓ | ✓ |
| `clear` | empty the window; files stay as they are | ✓ | ✓ |
| start, end of line | move the cursor | `Ctrl+A`, `Ctrl+E` | `Home`, `End` |

</div>

<div class="note-text mt-md">The mouse does not move the cursor inside a line. The arrow keys do.</div>

<!--
**Say:** a line once typed is never typed again: ↑ brings it back.
**If asked:** in PowerShell `Ctrl+C` copies when text is selected.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Files & Folders, slide 29 'The Whole File: `cat`': the export is shown on the slide of its script -->

---
hideInToc: true
---

# The Whole File: `cat`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh** · 🪟 **PowerShell**

```text
% cat data/raw/daily_export.csv
nr;date;temp_c
1;2025-10-01;6,3
2;2025-10-02;5,0
3;2025-10-03;5,6
4;2025-10-04;7,0
5;2025-10-05;9,4
6;2025-10-06;10,4
7;2025-10-07;9,2
8;2025-10-08;9,0
9;2025-10-09;9,8
;mean;7,97
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧾 **A spreadsheet export**

- `;` between the values, a comma as decimal sign
- a column `nr` with the row number
- a last line with the mean

A spreadsheet with European settings writes this. Most programs expect `,` and `.` instead.

</div>

</div>

<div class="note-text mt-md"><code>cat</code> prints a whole file, in both shells. On a large file <code>Ctrl+C</code> stops it.</div>

<!--
**If asked:** `less FILE` (macOS) and `Get-Content FILE | more` show one screen at a time: Space goes on, q leaves.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Files & Folders, slide 31 'Count Bytes: `wc -c`': became Lines and Bytes -->

---
hideInToc: true
---

# Count Bytes: `wc -c`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc data/raw/daily_export.csv
      11      11     180 data/raw/daily_export.csv
% wc -c data/raw/weather.csv
 2515215 data/raw/weather.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Get-Item data/raw/daily_export.csv).Length
180
PS> (Get-Item data/raw/weather.csv).Length
2515215
```

</div>

</div>

<div class="note-text mt-md"><code>wc</code> alone prints lines, words and bytes. <code>Length</code> is the size of the file in bytes: 2 515 215 bytes, 2.5 MB.</div>

<!--
**Say:** the export has 11 lines, 11 words because no line has a space, and 180 bytes.
**If asked:** `Get-Content FILE | Measure-Object -Character` says 169 for the export: it drops the 11 line breaks, 169 + 11 = 180.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Files & Folders, slide 32 'Make a Folder, Copy a File': Lecture 03 taught it; one recap slide holds the commands of Lecture 03 -->

---
hideInToc: true
---

# Make a Folder, Copy a **File**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% mkdir backup
% cp data/raw/daily_export.csv backup
% ls backup
daily_export.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> mkdir backup
PS> cp data/raw/daily_export.csv backup
PS> ls backup -Name
daily_export.csv
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`mkdir` makes a folder. `cp FROM TO` copies a file; when `TO` is a folder, the copy keeps its name. The same words work in both shells.

</div>

<!--
**Say:** PowerShell's `mkdir` prints a short table with the new folder; zsh prints nothing.
**If asked:** in PowerShell `cp` is a short name, an alias, for `Copy-Item`.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Files & Folders, slide 33 'Move and Rename: `mv`': Lecture 03 taught it; one recap slide holds the commands of Lecture 03 -->

---
hideInToc: true
---

# Move and **Rename**: `mv`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% mv backup/daily_export.csv backup/export_copy.csv
% ls backup
export_copy.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> mv backup/daily_export.csv backup/export_copy.csv
PS> ls backup -Name
export_copy.csv
```

</div>

</div>

<div class="note-text mt-md"><code>mv FROM TO</code> moves a file. A new name in the same folder is a rename. A folder as <code>TO</code> moves it there.</div>

<!--
**Say:** `cp` leaves the original in place, `mv` does not.
**If asked:** `cp` overwrites a file of the same name without asking, in both shells. PowerShell's `mv` refuses to.
(~1 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Files & Folders, slide 34 'Delete: `rm`': Lecture 03 taught it; one recap slide holds the commands of Lecture 03 -->

---
hideInToc: true
---

# Delete: `rm`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% rm backup/export_copy.csv
% rm -r backup
% ls backup
ls: backup: No such file or directory
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> rm backup/export_copy.csv
PS> rm -r backup
PS> Test-Path backup
False
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ No Trash, no Recycle Bin, no `Ctrl+Z`. `-r` deletes a folder and everything in it. Before `rm`: `ls` with the same path, and read the names.

</div>

<!--
**Say:** say the folder name aloud before pressing Enter. What `rm` can take away for good is a file in `data/raw`, a script or the README.
**If asked:** `rm -rf`, seen on many web pages, fails in PowerShell: write `-r -Force`.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Files & Folders, slide 35 'Many Files at Once: Wildcards': off the line of the check; wildcards appear in the recap and in Get-FileHash data/raw/* -->

---
hideInToc: true
---

# Many Files at Once: **Wildcards**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -c data/raw/*.csv
     180 data/raw/daily_export.csv
 2515215 data/raw/weather.csv
 2515395 total
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Item data/raw/*.csv |
>> Select-Object Name, Length

Name              Length
----              ------
daily_export.csv     180
weather.csv      2515215
```

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ✳️ **`*`**

Any number of characters, none included. `*.csv` fits every name that ends in `.csv`.

</div>

<div class="card card-accent card-glass pad-compact">

## ❓ **`?`**

Exactly one character. `w?ather.csv` fits `weather.csv`.

</div>

</div>

<!--
**Say:** the two signs mean the same in both shells. The `|` in the PowerShell line passes the files on to `Select-Object`, which picks two columns.
**If asked:** zsh replaces `*` by the names before the program starts; PowerShell hands `*` to the command. `echo data/raw/*.csv` shows the difference.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Files & Folders, slide 36 'Where Commands Read and Write': the habits went into the caption of the paths slide -->

---
hideInToc: true
---

# Where Commands Read and **Write**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📁 **weather-project**

```text
weather-project/
├─ README.md
├─ data/
│  ├─ raw/
│  └─ processed/
├─ scripts/
└─ results/
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📐 **Habits at the prompt**

- The terminal stays in `weather-project`
- Commands **read** from `data/raw` and never write there
- What a command makes goes to `data/processed` or `results`
- No spaces in names

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The layout says which files can be made again. `data/processed` and `results` can, by a command. `data/raw`, `scripts` and the README cannot, and those are the files `rm` takes away for good.

</div>

<!--
(~1 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Pipes & Filters, slide 39 'Why the Sizes Differ: Line Endings': Lecture 03 showed LF and CRLF; the checksum section uses the difference -->

---
hideInToc: true
---

# Why the Sizes Differ: **Line Endings**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🔬 **The same two lines, byte by byte**

```text
% hexdump -C results/note.txt
00000000  6d 61 64 65 20 6f 6e 20  32 30 32 36 2d 31 30 2d  |made on 2026-10-|
00000010  31 33 0a 62 79 20 61 64  61 0a                    |13.by smilte.|
PS> Format-Hex results/note.txt
0000000000000000 6D 61 64 65 20 6F 6E 20 32 30 32 36 2D 31 30 2D made on 2026-10-
0000000000000010 31 33 0D 0A 62 79 20 61 64 61 0D 0A             13��by smilte��
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-info card-glass pad-compact">

## 🔢 **Count them**

`made on 2026-10-13` is 18 characters, `by smilte` 6: 24 in all.

</div>

<div class="card card-warning card-glass pad-compact">

## ↩️ **Line endings**

macOS ends a line with `0a` (LF): 24 + 2 = 26. Windows ends it with `0D 0A` (CRLF): 24 + 4 = 28.

</div>

</div>

<!--
**Do:** point at `0a` and at `0D 0A`.
**Say:** the text is the same, the bytes are not.
**If asked:** Format-Hex prints a byte that is no character as a replacement sign.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Pipes & Filters, slide 41 'zsh Pipes Text, PowerShell Pipes Objects': became Pick a Column: cut -->

---
hideInToc: true
---

# zsh Pipes **Text**, PowerShell Pipes **Objects**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -c data/raw/* | sort -n
     180 data/raw/daily_export.csv
 2515215 data/raw/weather.csv
 2515395 total
```

Lines of text. `sort -n` orders by the number at the start of each line.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> ls data/raw | Sort-Object Length |
>> Select-Object Length, Name

 Length Name
 ------ ----
    180 daily_export.csv
2515215 weather.csv
```

Objects: one per file, with properties such as `Name` and `Length`.

</div>

</div>

<!--
**Say:** the same question, which file is largest, by two routes. In zsh the size is the first word of a line; in PowerShell it is a property with a name.
**If asked:** zsh's `sort` knows nothing about the line `total` and sorts it with the files.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Pipes & Filters, slide 42 'Pick Columns: `cut` and `Import-Csv`': became Pick a Column: cut -->

---
hideInToc: true
---

# Pick Columns: `cut` and `Import-Csv`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cut -d, -f1,2 data/raw/weather.csv |
    head -n 3
time,temp_c
2016-01-01T00:00,-4.4
2016-01-01T01:00,-4.8
```

`-d,` the separator, `-f1,2` the fields, counted from 1.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Import-Csv data/raw/weather.csv |
>> Select-Object time, temp_c -First 2

time             temp_c
----             ------
2016-01-01T00:00 -4.4
2016-01-01T01:00 -4.8
```

Line 1 gives the names; columns are picked by name.

</div>

</div>

<!--
**Ask:** before running `cut`, which field number has `temp_c`? `head -n 1` shows the names in order.
**Say:** `cut` treats the header like any other line; `Import-Csv` reads it as the names.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Regular Expressions, slide 52 'Regex in VS Code's Find Box': step-by-step clicking left the lecture; the pattern is built in the shell -->

---
hideInToc: true
---

# Regex in VS Code's **Find Box**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **Switch it on**

- `Ctrl+F` opens Find (macOS `Cmd+F`)
- The button `.*` at the right end switches regular expressions on
- The counter shows the matches while the pattern is typed

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧪 **A pattern in three steps**

```text
In data/raw/daily_export.csv

Find          Matches
[0-9]+        56     every number
[0-9]+;       18     a number before a ;
^[0-9]+;       9     the first in a line
```

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ The third pattern fits the row number with its `;`, once in each of the nine rows. Replaced by nothing, the column `nr` is gone. Do it on a copy in `data/processed`, never in `data/raw`.

</div>

<!--
**Say:** the counter is the check: nine rows, nine matches.
(~3 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Regular Expressions, slide 53 'Replace with Capture Groups': capture groups are off the line of the check -->

---
hideInToc: true
---

# Replace with Capture **Groups**

<div class="card card-info card-glass pad-compact mt-sm">

Round brackets mark a part of the match, a capture group. In the Replace box `$1` puts back what the first pair matched, `$2` the second.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔁 **The decimal comma**

```text
Find      ([0-9]),([0-9])
Replace   $1.$2
```

`6,3` becomes `6.3`: 10 matches, the nine rows and the mean line. A `;` is never touched.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📋 **A row of a Markdown table**

```text
Find      ^([0-9]+);(.*);(.*)$
Replace   | $2 | $3 |
```

`1;2025-10-01;6,3` becomes `| 2025-10-01 | 6,3 |`: 9 matches.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Replace All changes every match, also the ones nobody looked at. Read the counter first.

</div>

<!--
**If asked:** PowerShell knows `$1` too: `(Get-Content data/raw/daily_export.csv) -replace '([0-9]),([0-9])', '$1.$2'`.
(~3 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Programs Someone Else Wrote, slide 55 'A Program Is a Text File': the program shown is now column_stats.py, which computes the mean -->

---
hideInToc: true
---

# A Program Is a **Text File**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📜 **`scripts/clean_export.py`, lines 27–34**

```python
def clean(lines):
    out = []
    for line in lines:
        if line.startswith(";"):
            continue
        line = line.replace(",", ".").replace(";", ",")
        out.append(line.split(",", 1)[1])
    return out
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| Line | Edit to the export |
| --- | --- |
| 30 | a line that starts with `;`, the mean line, is skipped |
| 32 | `,` becomes `.`, then `;` becomes `,` |
| 33 | only what follows the first comma is kept: `nr` goes |

</div>

<!--
**Say:** the order matters: the decimal comma becomes a point while it is still the only comma.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Programs Someone Else Wrote, slide 57 'PowerShell's `>` Adds CRLF': merged into The Same Rows, Other Bytes -->

---
hideInToc: true
---

# PowerShell's `>` Adds **CRLF**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **The shell copies, zsh**

```text
% cat data/processed/daily.csv > results/copy.csv
% wc -c results/copy.csv
     148 results/copy.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **The shell copies, PowerShell**

```text
PS> Get-Content data/processed/daily.csv > results/copy.csv
PS> (Get-Item results/copy.csv).Length
158
```

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔎 **10 bytes more**

158 − 148 = 10. PowerShell writes each of the ten lines itself and ends it with CRLF.

</div>

<div class="card card-success card-glass pad-compact">

## 🧷 **The script sets the line ending**

Line 49 of `clean_export.py`: `newline="\n"`. Every line ends with LF on every system, so the script wrote 148 bytes in both shells.

</div>

</div>

<!--
**Say:** neither shell is wrong; each writes text by its own rule. A file whose bytes must match everywhere is written by a program that states the rule.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Programs Someone Else Wrote, slide 58 'The Mean of a Column: `column_stats.py`': merged into The Mean With and Without the −999 Rows and Two Programs, One Mean -->

---
hideInToc: true
---

# The Mean of a Column: `column_stats.py`

<div class="card card-primary card-glass pad-compact mt-sm">

```text
% python3 scripts/column_stats.py data/raw/weather.csv temp_c
PS> python scripts/column_stats.py data/raw/weather.csv temp_c
file    data/raw/weather.csv
column  temp_c
rows    87672
min     -999.0
max     32.4
mean    5.7828
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧭 **The parts of the line**

The program, its file, then two words for the script: a file and a column name. The output is the same in both shells.

</div>

<div class="card card-warning card-glass pad-compact">

## ❓ **5.78 °C**

The mean of all 87 672 hours, the −999 rows included. Is that the mean temperature of the station?

</div>

</div>

<!--
**Say:** the shell counts and sorts lines. A mean takes a program: this one is 53 lines that someone else wrote.
**If asked:** on the raw export it answers `no column temp_c`: with `;` between the values it sees one column, `nr;date;temp_c`. On the cleaned `daily.csv` it gives a mean of 7.96667, the 7,97 of the mean line.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Checksums & Backups, slide 63 'A Changed File Fails the Check': merged into A List of Checksums for data/raw -->

---
hideInToc: true
---

# A Changed File Fails the **Check**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
% shasum -a 256 -c data/checksums.txt
data/raw/daily_export.csv: FAILED
data/raw/weather.csv: OK
shasum: WARNING: 1 computed checksum did NOT match
PS> $now = (Get-FileHash data/raw/*).Hash
PS> Compare-Object $list $now

InputObject                                                      SideIndicator
-----------                                                      -------------
13FBCAE6A7A4D67EC30FDF3BEDC0B666209F7A4DC453EA72FF6DE7370FFD6AEE =>
9D849815D88ECEB18366EE66AC72F26B72E195BEA8BB20AA9A1474372513BBDB <=
```

</div>

<div class="note-text mt-md">In a copy of the project, <code>6,3</code> in row 1 of the export became <code>6,4</code>. <code>&lt;=</code> marks the checksum in the list, <code>=&gt;</code> the one computed now.</div>

<!--
**Live (optional):** `shasum -a 256 data/raw/* > data/checksums.txt`; in VS Code change `6,3` to `6,4` in `daily_export.csv` and save; `shasum -a 256 -c data/checksums.txt`. Change it back and save before going on.
**Say:** zsh names the file. PowerShell shows the old and the new checksum; the old one is line 1 of the list, the export.
(~1 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Checksums & Backups, slide 64 'How Files Are Lost': merged into Backups: the 3-2-1 Rule -->

---
hideInToc: true
---

# How Files **Are Lost**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| What happens | What is lost | What brings it back |
| --- | --- | --- |
| `rm`, `>` or a spreadsheet save hits the wrong file | one file | an older copy |
| The disk fails, the laptop is stolen | everything on it | a copy on another device |
| Fire or theft where every copy is | every copy in that place | a copy in another place |
| A file changes unnoticed | unknown | a checksum to notice, an older copy |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔁 **Can be made again**

`data/processed`, `results`: the commands write them again.

</div>

<div class="card card-warning card-glass pad-compact">

## 🧱 **Cannot**

`data/raw`, `scripts`, the README: what a backup is for.

</div>

</div>

<!--
**Ask:** who has lost a file in one of these four ways? Usually every row gets a hand.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Tools & Environments, slide 67 'Where a Program Comes From': became Where a Program Comes From (type) -->

---
hideInToc: true
---

# Where a Program **Comes From**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
% which python3
/Users/smilte/miniforge3/bin/python3
PS> (Get-Command python).Source
C:\Users\smilte\miniforge3\python.exe
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧱 **Built in**

`ls`, `cat`, `Get-Content`: they came with the system.

</div>

<div class="card card-accent card-glass pad-compact">

## 📦 **An installer**

VS Code, and Miniforge, which brings Python and `conda`: downloaded and run once.

</div>

<div class="card card-info card-glass pad-compact">

## 🗂️ **A package manager**

A typed line: `winget` installed PowerShell 7 at the start.

</div>

</div>

<div class="note-text mt-md"><code>which</code> and <code>Get-Command</code> print where the shell found a program: in the folder its installer made.</div>

<!--
**Say:** a program is usable at the prompt when its folder is on the list the shell searches, `PATH`.
**If asked:** Miniforge installs into the folder `miniforge3` in the home folder. A Mac without it answers `/usr/bin/python3`, Apple's copy.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Tools & Environments, slide 70 'An Alias and a Prompt': shell settings are off the line of the check; the end of the lecture lost the room on 13 Oct 2026 -->

---
hideInToc: true
---

# An Alias and a **Prompt**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% alias ..='cd ..'
% PROMPT='%1~ %# '
weather-project % cd data
data % ..
weather-project %
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> function .. { Set-Location .. }
PS> function prompt { "$((Get-Item .).Name)> " }
weather-project> cd data
data> ..
weather-project>
```

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-info card-glass pad-compact">

## 🏷️ **An alias**

A short name for a longer command: `..` now means `cd ..`. The prompt now shows only the folder.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **How long they last**

Both last until this terminal closes, and exist only on this laptop. A README line uses the full command.

</div>

</div>

<!--
**Say:** two settings typed by hand. They change only this terminal.
**If asked:** `%1~` is the last folder of the path, `%#` the `%` sign. A PowerShell alias cannot carry an argument such as `..`, so a function does it.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Tools & Environments, slide 71 'A File the Shell Runs at Start': start-up files are off the line of the check; the end of the lecture lost the room on 13 Oct 2026 -->

---
hideInToc: true
---

# A File the Shell Runs at **Start**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **zsh: `~/.zshrc`**

```text
# run by every new zsh
alias ..='cd ..'
PROMPT='%1~ %# '
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **PowerShell: `$PROFILE`**

```text
# run by every new PowerShell
function .. { Set-Location .. }
function prompt { "$((Get-Item .).Name)> " }
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

```text
% echo ~/.zshrc
/Users/smilte/.zshrc
PS> $PROFILE
C:\Users\smilte\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
```

</div>

<div class="note-text mt-md">A new terminal reads the file. <code>source ~/.zshrc</code> or <code>. $PROFILE</code> reads it again in the open one.</div>

<!--
**Say:** the same lines as on the last slide, written once into a file: from now on every terminal starts with them.
**If asked:** neither file exists on a new laptop; the first save makes it. With OneDrive, `$PROFILE` lies under `OneDrive\Documents`.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Tools & Environments, slide 72 'Ready-Made Settings: Oh My Zsh': Oh My Zsh is off the line of the check; zsh left the course -->

---
hideInToc: true
---

# Ready-Made Settings: **Oh My Zsh**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧰 **What it is**

- Settings for zsh, shared on GitHub: 371 plugins and 143 prompt themes
- One line installs it. It writes a new `~/.zshrc` and keeps the old one

</div>

<div class="card card-secondary card-glass pad-compact">

## 📄 **Two lines of its `~/.zshrc`**

```text
ZSH_THEME="robbyrussell"
plugins=(git)
```

```text
➜  weather-project cd data
➜  data
```

</div>

</div>

<div class="note-text mt-md">PowerShell: Oh My Posh, or Starship for both shells. Each is one <code>winget</code> line and one line in <code>$PROFILE</code>.</div>

<!--
**Say:** a theme only changes the prompt, a plugin adds aliases. Nothing in this course needs either.
**If asked:** the arrow is green, red after a command that failed. In a Git project the prompt adds the branch. The `git` plugin adds `gst` for `git status`. Counts from October 2026.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Tools & Environments, slide 73 'What `conda init` Wrote': conda init internals are off the line of the check; one note line says to run conda init powershell once -->

---
hideInToc: true
---

# What `conda init` **Wrote**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **zsh: the end of `~/.zshrc`**

```text
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/smilte/miniforge3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
…
# <<< conda initialize <<<
```

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🪟 **PowerShell: `profile.ps1`, in the folder of `$PROFILE`**

```text
#region conda initialize
If (Test-Path "C:\Users\smilte\miniforge3\Scripts\conda.exe") {
    (& "C:\Users\smilte\miniforge3\Scripts\conda.exe" "shell.powershell" "hook") | … | Invoke-Expression
}
#endregion
```

</div>

<div class="note-text mt-md">Every new terminal runs the block: it asks <code>conda</code> for a few lines of shell code and runs them. The prompt then starts with <code>(base)</code>.</div>

<!--
**Say:** the Mac installer asks "Proceed with initialization?"; yes runs `conda init`, which writes these lines into the start-up file from two slides ago. On Windows, `conda init powershell`, typed once in the Miniforge Prompt, writes them.
**If asked:** a prompt line of your own, as two slides ago, hides `(base)`: in zsh write it above conda's block, in PowerShell start it with `$env:CONDA_PROMPT_MODIFIER`. `conda init --reverse zsh` takes the block out again; `conda config --set auto_activate false` keeps `(base)` off at start. Oh My Zsh writes a new `~/.zshrc` without the block: `conda init zsh` puts it back. The slides shorten every prompt to `%` and `PS>`.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Tools & Environments, slide 76 'An Environment Is a Folder': merged into One Environment per Project -->

---
hideInToc: true
---

# An Environment Is a **Folder**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **zsh** · 🪟 **PowerShell: the same lines**

```text
(base) % conda create -n weather python=3.14
  environment location: /Users/smilte/miniforge3/envs/weather
…
Proceed ([y]/n)? y
(base) % conda env list
# conda environments:
#
# * -> active
# + -> frozen
base                 *   /Users/smilte/miniforge3
weather                  /Users/smilte/miniforge3/envs/weather
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📁 **What is in it**

24 packages: Python 3.14.8, pip, and 22 that Python needs. 221 MB in 6135 files.

</div>

<div class="card card-info card-glass pad-compact">

## 🗑️ **Delete and make again**

`conda env remove -n weather` deletes the folder. One line makes it again.

</div>

</div>

<!--
**Say:** `-n` names the environment, `python=3.14` asks for its Python. Nothing is active yet: the `*` is still at `base`.
**If asked:** on Windows the folder is `C:\Users\smilte\miniforge3\envs\weather`. Counts and sizes measured on Linux with Miniforge 26.7.2; they differ a little by system.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Tools & Environments, slide 77 'Activation Changes PATH': merged into One Environment per Project -->

---
hideInToc: true
---

# Activation Changes **PATH**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
(base) % conda activate weather
(weather) % which python
/Users/smilte/miniforge3/envs/weather/bin/python
(weather) % python --version
Python 3.14.8
(weather) % conda deactivate
(base) %
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
(base) PS> conda activate weather
(weather) PS> (Get-Command python).Source
C:\Users\smilte\miniforge3\envs\weather\python.exe
(weather) PS> python --version
Python 3.14.8
(weather) PS> conda deactivate
(base) PS>
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔛 Activation puts the environment's folder first on `PATH`: `python` is now the environment's, and the prompt names it. `conda deactivate` undoes both.

</div>

<!--
**Say:** with `(weather)` in the prompt the word is `python` on both systems.
**If asked:** `echo $PATH | tr ':' '\n'` now starts with `/Users/smilte/miniforge3/envs/weather/bin`. On Windows the environment's folder holds `python.exe` itself; its `Scripts` follows on `PATH`.
(~3 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section Tools & Environments, slide 78 'Install numpy into One Environment': merged into What a Package Is -->

---
hideInToc: true
---

# Install numpy into **One Environment**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **zsh** · 🪟 **PowerShell: the same lines**

```text
(weather) % python -c "import numpy"
ModuleNotFoundError: No module named 'numpy'
(weather) % conda install numpy
…
Proceed ([y]/n)? y
(weather) % conda list numpy
# packages in environment at /Users/smilte/miniforge3/envs/weather:
#
# Name                     Version          Build            Channel
numpy                      2.5.4            py314hd3a7d6b_0  conda-forge
(weather) % conda deactivate
(base) % python -c "import numpy"
ModuleNotFoundError: No module named 'numpy'
```

</div>

<div class="note-text mt-md">numpy came with six more packages: OpenBLAS, a C library for linear algebra, and the Fortran runtime it uses. <code>base</code> did not change.</div>

<!--
**Say:** `-c` runs one line of Python: here it only tries the import.
**If asked:** measured on Linux with Miniforge 26.7.2; the build string and the extra packages differ by system. pip is in every environment: `python -m pip install NAME` in the activated environment, only for what conda-forge lacks, never into `base`.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section The README, slide 81 'What the README Must Answer': the open questions of the README became the steps of the check -->

---
hideInToc: true
---

# What the README Must **Answer**

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **Already in the README**

- A title and one paragraph
- The folders and what goes into each
- The two data files: source, date, what one row is

</div>

<div class="card card-warning card-glass pad-compact">

## ❓ **Still open**

- What is `temp_c`, in which unit?
- Why is `temp_c` −999 in 120 rows?
- Are the raw files the ones that arrived?
- Which lines make `data/processed`?
- May I copy the scripts?

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The test for a README: someone with the project folder and an empty laptop gets the same files and asks nobody.

</div>

<!--
**Do:** tick off the left card, line by line.
**Say:** the checksum list answers the third question.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section The README, slide 82 'The README: Columns and Units': became The README: the Mark and the Result -->

---
hideInToc: true
---

# The README: Columns and **Units**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **In the README**

```md
## Columns of `weather.csv`

| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | ISO 8601 |
| `temp_c` | air temperature | °C |
| `humidity_pct` | relative humidity | % |
| `wind_ms` | wind speed | m/s |

Missing value: `temp_c` is `-999`
in 120 rows, 2019-07-22 to 07-26.
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔎 **Checked by a command**

```text
% head -n 1 data/raw/weather.csv
time,temp_c,humidity_pct,wind_ms
% grep -c ',-999,' data/raw/weather.csv
120
```

The names and the 120 come out of the file. The units do not: the README has to hold them.

</div>

</div>

<!--
**Say:** every line of it except the units was checked by a command anyone can run again.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section The README, slide 84 'Test the Rebuild Lines': merged into The Same Rows, Other Bytes -->

---
hideInToc: true
---

# Test the Rebuild **Lines**

<div class="card card-info card-glass pad-compact mt-sm">

Delete the two files in `data/processed`, paste the lines of the README into the shell, and measure what came back.

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -c data/processed/*
     148 data/processed/daily.csv
 2511735 data/processed/weather_valid.csv
 2511883 total
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> ls data/processed | Select-Object Name, Length

Name              Length
----              ------
daily.csv            148
weather_valid.csv 2599288
```

</div>

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-success card-glass pad-compact">

🟰 `daily.csv`: 148 bytes in both shells. The README may promise its checksum.

</div>

<div class="card card-warning card-glass pad-compact">

🔀 `weather_valid.csv`: one `0D` more per line on Windows. The README promises its 87 553 lines, not its checksum.

</div>

</div>

<!--
**Say:** the script states its line ending, the filter and `>` do not. A file whose checksum goes into the README is made by a script.
(~3 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section The README, slide 87 'The README: Licence': the licence is off the line of the check -->

---
hideInToc: true
---

# The README: **Licence**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📥 **The licence of the data**

Set by whoever published the data. It decides whether the raw files may be passed on with the project. Here the station's operator chose CC0: free for any use.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📤 **The licence of your own work**

Without one, others may read but not copy, change or pass on. The text goes into a file `LICENSE`. Usual: MIT for scripts, CC BY 4.0 for text and figures.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

```md
## Licence

Data: CC0, from the station's operator.
Scripts and text: MIT, see `LICENSE`.
```

</div>

<!--
**Say:** the last question of the stranger, "may I copy the scripts?", has no answer until this section exists.
**If asked:** choosealicense.com has the text of each licence, ready to copy.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 04, section The README, slide 88 'Which Copy Is Right: Size and Checksum': merged into The Same Rows, Other Bytes -->

---
hideInToc: true
---

# Which Copy Is Right: Size and **Checksum**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Copy of the cleaned export | Bytes | SHA-256 | What differs |
| --- | --- | --- | --- |
| written by the script | 148 | `33fe5e77…f705483d` | nothing |
| copied by PowerShell's `>` | 158 | `b68430c5…721a899e` | CRLF line endings |
| one digit changed | 148 | `58709abc…fb40d36b` | `6.3` became `6.4` |

</div>

<div class="card card-success card-glass pad-compact mt-md">

```md
- **Cleaned export:** `data/processed/daily.csv`, 148 bytes,
  SHA-256 `33fe5e77a97900b6e8f94776f266da4d6e3c96590088d21bc9842987f705483d`
```

</div>

<div class="note-text mt-md">The size rules out the CRLF copy. Only the checksum rules out the copy with one digit changed.</div>

<!--
**Say:** all three look alike in VS Code. With size and checksum in the README, anyone checks a copy with one line, `shasum -a 256` or `Get-FileHash`.
(~2 min)
-->
