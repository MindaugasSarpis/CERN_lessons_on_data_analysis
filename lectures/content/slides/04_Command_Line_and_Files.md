---
layout: cover
title: "Command Line & File Handling"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Command Line & File Handling

##### <span class="aims-badge">⚙️ automation · 📁 data & files · 🔧 tool-agnostic</span>

<!--
**Say:** today every step on a file is a typed line.
(~1 min)
-->

---
hideInToc: true
layout: quote
---

# The main goal of this lecture is to work on files with **typed commands**: a step that was typed can be written down, checked and run again

<!--
**Say:** a click leaves nothing behind. A typed line can be pasted into a README, read by someone else and run again on the next file.
(~1 min)
-->

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

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

🛡️ Tell files apart by **checksum**, keep **backups**, and write into the README how every file is made again

</div>

</div>

<!--
**Say:** one line per part of the lecture. One small project folder runs through all of them.
(~1 min)
-->

---
hideInToc: true
---

# A Folder **Arrives**

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

</div>

<div class="card card-secondary card-glass pad-compact">

## 🌦️ **One weather station**

- `weather.csv`: one row per hour, 2016 to 2025
- `daily_export.csv`: nine daily mean temperatures, typed into a spreadsheet
- Two small programs in `scripts`
- `data/raw` holds the files as they arrived. Nothing writes there

</div>

</div>

<!--
**Say:** a colleague sent this folder. Today we answer questions about it with typed lines.
(~2 min)
-->

---
hideInToc: true
---

# One Row, **Four Values**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📄 **The first two lines of `weather.csv`**

```text
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| Column | Value in row 1 | Meaning |
| --- | --- | --- |
| `time` | `2016-01-01T00:00` | the hour, as year-month-day, `T`, hour:minute |
| `temp_c` | `-4.4` | air temperature, °C |
| `humidity_pct` | `93` | relative humidity, % |
| `wind_ms` | `2.5` | wind speed, m/s |

</div>

<div class="note-text mt-md">Line 1 names the columns. Every later line is one hour, the values separated by commas: a CSV file.</div>

<!--
**Say:** the time is written largest unit first, ISO 8601. That order also sorts correctly as text.
(~2 min)
-->

---
hideInToc: true
---

# Three **Questions**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

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

---
layout: section
hideInToc: true
---

# Set Up the **Shell**

A window, a program that reads typed lines, and the same pair on every laptop in the room.

<!--
**Say:** nothing is assumed. This section names the terminal and the shell, and gets the same shell onto every laptop.
(~1 min)
-->

---
hideInToc: true
---

# Terminal, Shell, **Program**

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖥️ **Terminal**

The window. It shows text and passes on what is typed.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🐚 **Shell**

The program that reads a typed line, runs what it names, and waits for the next line.

</div>

<div class="card card-accent card-glass pad-compact">

## ⚙️ **Program**

Does one job and prints text: count lines, copy a file, show a date.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

```text
you type a line → the shell finds the program → the program runs and prints → the shell waits again
```

</div>

<!--
**Say:** the terminal is only the window. The shell inside it does the work, and it can be changed without changing the window.
(~2 min)
-->

---
hideInToc: true
---

# One Shell per **System**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Laptop | Shell of this course | Comes with the system? | Its prompt ends in |
| --- | --- | --- | --- |
| macOS | `zsh` | Yes, the default since macOS 10.15 (2019) | `%` |
| Windows | PowerShell 7 | No. Windows has the older Windows PowerShell 5.1 | `>` |

</div>

<div class="note-text mt-md">On these slides <code>%</code> starts a zsh line and <code>PS&gt;</code> a PowerShell line. Nobody types either: the shell prints it.</div>

<div class="card card-info card-glass pad-compact mt-md">

The next slides check the shell on each system, and install PowerShell 7 where it is missing.

</div>

<!--
**Say:** two shells, one per system. The ideas are the same in both, the words often differ. Every command slide shows both side by side.
**If asked:** Linux usually has bash. Almost every zsh line of this lecture runs there unchanged.
(~1 min)
-->

---
hideInToc: true
---

# macOS: Open **Terminal**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **Open it**

1. `Cmd+Space`, type `Terminal`, `Enter`
2. A window opens with the prompt
3. Type the line below, `Enter`

```text
ada@MacBook-Air ~ % echo $SHELL
/bin/zsh
```

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **`/bin/zsh`**

The shell is zsh. Nothing to install: it is part of macOS.

`$SHELL` is the shell this account starts. `echo` prints it.

</div>

</div>

<!--
**Ask:** who sees `/bin/bash`? Their account is older than 2019: the next slide.
(~2 min)
-->

---
hideInToc: true
---

# macOS: zsh as the **Default**

<div class="card card-warning card-glass pad-compact mt-sm">

## 🍎 **If `echo $SHELL` prints `/bin/bash`**

```text
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
MacBook-Air:~ ada$ chsh -s /bin/zsh
Changing shell for ada.
Password for ada:
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔑 **The line**

`chsh` changes the shell, `-s` names the new one. The password is the one of the Mac. Nothing appears while it is typed.

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **Check**

Close the window, open a new one. `echo $SHELL` prints `/bin/zsh`, and the prompt ends in `%`.

</div>

</div>

<!--
**Say:** macOS prints the first two lines itself when bash starts. zsh is already on the disk at `/bin/zsh`; the line only makes it the default.
**If asked:** bash prompts end in `$`, zsh prompts in `%`.
(~2 min)
-->

---
hideInToc: true
---

# Windows: Two **PowerShells**

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Open the one Windows has**

1. Start, type `PowerShell`, `Enter`
2. A blue window: **Windows PowerShell**
3. Ask for its version

```text
PS C:\Users\ada> $PSVersionTable.PSVersion.Major
5
```

</div>

<div class="card card-primary card-glass pad-compact table-compact">

## 🔢 **5 or 7**

| | Windows PowerShell | PowerShell 7 |
| --- | --- | --- |
| Version | 5.1 | 7.6 |
| Comes with Windows | yes | no |
| Still developed | no | yes |
| Program name | `powershell` | `pwsh` |

</div>

</div>

<div class="note-text mt-md">This course uses PowerShell 7. The next slide installs it from the Windows PowerShell window.</div>

<!--
**Say:** `$PSVersionTable` is a table PowerShell keeps about itself; `.PSVersion.Major` picks one number from it.
(~2 min)
-->

---
hideInToc: true
---

# Windows: Install **PowerShell 7**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🪟 **In Windows PowerShell, one typed line**

```text
PS C:\Users\ada> winget install --id Microsoft.PowerShell --source winget
Found PowerShell [Microsoft.PowerShell] Version 7.6.6
Downloading https://github.com/PowerShell/PowerShell/releases/download/v7.6.6/PowerShell-7.6.6-win-x64.msi
Successfully verified installer hash
Starting package install...
Successfully installed
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📦 **`winget`**

The installer of Windows. It finds a program by name and installs it.

</div>

<div class="card card-accent card-glass pad-compact">

## 🏷️ **`--id`**

The name in winget's catalogue: `Microsoft.PowerShell`.

</div>

<div class="card card-info card-glass pad-compact">

## 🔢 **7.6.6**

The newest version on the day it runs. 7.6.6 is from 8 September 2026.

</div>

</div>

<!--
**Say:** winget asks once to accept its source agreements: `Y`. A university laptop may ask for an administrator password.
**If asked:** the same line upgrades an older PowerShell 7.
(~3 min)
-->

---
hideInToc: true
---

# Windows: Open **PowerShell 7**

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Open it**

1. Start, type `pwsh`, `Enter`
2. A black window: **PowerShell 7**
3. Ask for its version

</div>

<div class="card card-primary card-glass pad-compact">

## ✅ **Check**

```text
PS C:\Users\ada> $PSVersionTable.PSVersion

Major  Minor  Patch  PreReleaseLabel BuildLabel
-----  -----  -----  --------------- ----------
7      6      6
```

</div>

</div>

<div class="note-text mt-md">Both PowerShells stay on the laptop. From here on every Windows line on the slides is for PowerShell 7.</div>

<!--
**Say:** the version is a small table: Major 7, Minor 6, Patch 6. The blue window still answers 5; only the black one is used from now on.
(~1 min)
-->

---
hideInToc: true
---

# The Terminal in **VS Code**

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

---
layout: section
hideInToc: true
---

# First **Commands**

One command per slide: where the shell is, what is there, how to move, and what to do when a line fails.

<!--
**Say:** every command from here on runs in the terminal of VS Code, in `weather-project`.
(~1 min)
-->

---
hideInToc: true
---

# Read the **Prompt**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
ada@MacBook-Air weather-project %
```

- `ada@MacBook-Air`: user and computer
- `weather-project`: the folder the shell is in
- `%`: the shell waits

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS C:\Users\ada\Documents\weather-project>
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

---
hideInToc: true
---

# A First **Command**

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

---
hideInToc: true
---

# Where Am I: `pwd`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% pwd
/Users/ada/Documents/weather-project
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> pwd

Path
----
C:\Users\ada\Documents\weather-project
```

</div>

</div>

<div class="note-text mt-md"><code>pwd</code>, print working directory: the folder of the prompt, as a whole path. The same word in both shells.</div>

<!--
**Ask:** why would three laptops print three different answers? The user name differs.
**If asked:** in PowerShell `pwd` is a short name for `Get-Location`; it prints a small table with one column, `Path`.
(~1 min)
-->

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

    Directory: C:\Users\ada\Documents\weather-project

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

---
hideInToc: true
---

# Move: `cd`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
ada@MacBook-Air weather-project % cd data
ada@MacBook-Air data % ls
processed  raw
ada@MacBook-Air data % cd ..
ada@MacBook-Air weather-project %
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
   └─ ada
      └─ Documents
         └─ weather-project
            └─ data
               └─ raw
                  └─ weather.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📍 **The whole way down**

```text
/Users/ada/Documents/weather-project/data/raw/weather.csv
C:\Users\ada\Documents\weather-project\data\raw\weather.csv
```

An absolute path starts at the top: `/` on macOS, `C:\` on Windows.

</div>

</div>

<div class="note-text mt-md">It names one file on one computer. On another laptop the user name, and so the path, differs.</div>

<!--
**Say:** read the path from left to right as a walk down the tree. macOS separates folders with `/`, Windows with `\`.
(~2 min)
-->

---
hideInToc: true
---

# Relative **Paths**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| The terminal is in | Path to `weather.csv` |
| --- | --- |
| `weather-project` | `data/raw/weather.csv` |
| `weather-project/data` | `raw/weather.csv` |
| `weather-project/scripts` | `../data/raw/weather.csv` |

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## `.` **here**

The working directory.

</div>

<div class="card card-accent card-glass pad-compact">

## `..` **one up**

`cd ../..` goes up two levels.

</div>

<div class="card card-info card-glass pad-compact">

## `~` **home**

`/Users/ada` or `C:\Users\ada`.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

♻️ The terminal stays in the project folder, and every path starts there. Then the same line works on every laptop, in both shells.

</div>

<!--
**Say:** a relative path starts at the working directory, so it does not start with `/` or `C:\`.
**If asked:** PowerShell reads `/` and `\` alike.
(~2 min)
-->

---
hideInToc: true
---

# The Parts of a **Command**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% head -n 2 data/raw/weather.csv
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Content -Head 2 data/raw/weather.csv
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
```

</div>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ⚙️ **Program**

The first word: `head`, `Get-Content`.

</div>

<div class="card card-accent card-glass pad-compact">

## 🎚️ **Option**

How to work: `-n 2`, `-Head 2`.

</div>

<div class="card card-info card-glass pad-compact">

## 📄 **Argument**

What to work on: the path.

</div>

</div>

<!--
**Say:** the words differ, the parts do not. PowerShell names its commands Verb-Noun; options are called parameters there.
**If asked:** zsh tells `-n` from `-N`; PowerShell ignores case, so `-head` works too.
(~2 min)
-->

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

---
hideInToc: true
---

# `Tab` **Completes**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⌨️ **Type a start, press `Tab`**

```text
head -n 2 da    Tab →  head -n 2 data/
head -n 2 data/r  Tab →  head -n 2 data/raw/
head -n 2 data/raw/w  Tab →  …/raw/weather.csv
```

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **No typing mistakes**

A name that `Tab` completed exists. If `Tab` adds nothing, no name fits: the path is wrong before it runs.

</div>

</div>

<div class="note-text mt-md">PowerShell completes a folder without the last <code>/</code> and writes <code>.\data\raw\weather.csv</code>. It reads that as well as <code>data/raw/weather.csv</code>.</div>

<!--
**Ask:** count the keys: how many were typed, how many did Tab add?
**If asked:** with two names that fit, zsh lists them on a second Tab; PowerShell cycles through them, `Ctrl+Space` lists them.
(~2 min)
-->

---
hideInToc: true
---

# History, **Stop**, Clear

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

---
hideInToc: true
---

# Help on a **Command**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% man head
HEAD(1)    General Commands Manual    HEAD(1)

NAME
     head – display first lines of a file
…
```

`Space` scrolls, `q` leaves.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Help Get-Content

NAME
    Get-Content

SYNTAX
    Get-Content [-Path] <string[]> [-TotalCount <long>]
    [-Tail <int>] …
```

`Get-Help Get-Content -Online` opens the full page.

</div>

</div>

<div class="note-text mt-md">Every command has a manual. The options of this lecture are all in it.</div>

<!--
**Say:** PowerShell 7 ships without its help texts. `-Online` opens them in the browser; `Update-Help` downloads them once.
(~2 min)
-->

---
hideInToc: true
---

# A Command That **Fails**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% hed -n 2 data/raw/weather.csv
zsh: command not found: hed
% head -n 2 data/raw/wether.csv
head: data/raw/wether.csv: No such file
or directory
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> hed -n 2 data/raw/weather.csv
hed: The term 'hed' is not recognized as
a name of a cmdlet, function, script file,
or executable program.
PS> Get-Content data/raw/wether.csv
Get-Content: Cannot find path 'C:\Users\ada\
…\data\raw\wether.csv' because it does not
exist.
```

</div>

</div>

<div class="note-text mt-md">The word before the first colon says who complains: the shell found no program, or the program found no file.</div>

<!--
**Ask:** what does each message say went wrong? Let the room read it before you explain.
**Say:** an error message is an answer. Read it before retyping.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Files & **Folders**

A command is a program, its options and its arguments, and a path names the file. The next commands read, count, copy, move and delete files.

<!--
**Say:** every slide has macOS on the left and PowerShell on the right, run in `weather-project`.
(~1 min)
-->

---
hideInToc: true
---

# Read a File: `head` and `tail`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% head -n 3 data/raw/weather.csv
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
% tail -n 2 data/raw/weather.csv
2025-12-31T22:00,-9.9,98,4.1
2025-12-31T23:00,-11.3,100,4.2
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Content data/raw/weather.csv -Head 3
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
PS> Get-Content data/raw/weather.csv -Tail 2
2025-12-31T22:00,-9.9,98,4.1
2025-12-31T23:00,-11.3,100,4.2
```

</div>

</div>

<div class="note-text mt-md">The first and the last lines of a file: its header, and how far it goes. The log runs from New Year 2016 to New Year's Eve 2025.</div>

<!--
**Say:** `head` reads only as far as it prints, so it answers at once even for a large file.
(~2 min)
-->

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
**Say:** remember this file: later a program cleans it in one line.
**If asked:** `less FILE` (macOS) and `Get-Content FILE | more` show one screen at a time: Space goes on, q leaves.
(~2 min)
-->

---
hideInToc: true
---

# Count Lines: `wc -l`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -l data/raw/weather.csv
   87673 data/raw/weather.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Get-Content data/raw/weather.csv).Count
87673
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 One header line and one line per hour. Ten years from 2016 to 2025 hold three leap years: 7 × 365 + 3 × 366 = 3653 days, and 3653 × 24 = 87 672 hours. 87 672 + 1 = 87 673.

</div>

<!--
**Say:** the first question of the opening, answered by a typed line. The count also checks the file: no hour is missing.
**If asked:** `wc`, word count. The brackets in PowerShell run the command first; `.Count` counts what it returned.
(~2 min)
-->

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
**Say:** the two signs mean the same in both shells. The `|` in the PowerShell line comes a section later; here it picks two columns.
**If asked:** zsh replaces `*` by the names before the program starts; PowerShell hands `*` to the command. `echo data/raw/*.csv` shows the difference.
(~2 min)
-->

---
hideInToc: true
---

# The Project Folder, **from the Shell**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📁 **Four folders**

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

## 📐 **Four habits at the prompt**

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
**Say:** nothing new on this slide. It fixes where the next commands read and where they write.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Pipes & **Filters**

So far each answer went to the screen. It can also go into a file, or into the next command.

<!--
**Say:** the centre of the lecture: small programs, each doing one thing, joined so that one's output is the next one's input.
(~1 min)
-->

---
hideInToc: true
---

# Output into a File: `>` and `>>`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% echo "made on 2026-10-13" > results/note.txt
% echo "by ada" >> results/note.txt
% cat results/note.txt
made on 2026-10-13
by ada
% wc -c results/note.txt
      26 results/note.txt
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> echo "made on 2026-10-13" > results/note.txt
PS> echo "by ada" >> results/note.txt
PS> cat results/note.txt
made on 2026-10-13
by ada
PS> (Get-Item results/note.txt).Length
28
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

`>` makes the file, or **empties** it first if it exists. `>>` adds at the end. The same two lines of text: 26 bytes on the Mac, 28 on Windows.

</div>

<!--
**Ask:** why would the sizes differ? Let the room guess before the next slide.
**If asked:** `sort results/note.txt > results/note.txt` leaves 0 bytes: the file is emptied before `sort` reads it. Never write into the file a command reads.
(~2 min)
-->

---
hideInToc: true
---

# 24 Characters, **26 or 28 Bytes**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🔬 **The same two lines, byte by byte**

```text
% hexdump -C results/note.txt
00000000  6d 61 64 65 20 6f 6e 20  32 30 32 36 2d 31 30 2d  |made on 2026-10-|
00000010  31 33 0a 62 79 20 61 64  61 0a                    |13.by ada.|
PS> Format-Hex results/note.txt
0000000000000000 6D 61 64 65 20 6F 6E 20 32 30 32 36 2D 31 30 2D made on 2026-10-
0000000000000010 31 33 0D 0A 62 79 20 61 64 61 0D 0A             13��by ada��
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-info card-glass pad-compact">

## 🔢 **Count them**

`made on 2026-10-13` is 18 characters, `by ada` 6: 24 in all.

</div>

<div class="card card-warning card-glass pad-compact">

## ↩️ **Line endings**

macOS ends a line with `0a` (LF): 24 + 2 = 26. Windows ends it with `0D 0A` (CRLF): 24 + 4 = 28.

</div>

</div>

<!--
**Do:** point at `0a` and at `0D 0A`.
**Say:** the text is the same, the bytes are not. This comes back with checksums at the end of the lecture.
**If asked:** Format-Hex prints a byte that is no character as a replacement sign.
(~2 min)
-->

---
hideInToc: true
---

# Program to Program: the **Pipe**

<div class="card card-info card-glass pad-compact mt-sm">

`A | B` runs both programs. What `A` prints becomes what `B` reads. No file stands between them.

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% head -n 5000 data/raw/weather.csv | tail -n 1
2016-07-27T06:00,18.2,71,1.1
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Content data/raw/weather.csv -Head 5000 |
>> Select-Object -Last 1
2016-07-27T06:00,18.2,71,1.1
```

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

The first 5000 lines go into the pipe, the last of them comes out: line 5000, the second question of the opening. A program that reads a pipe and passes on what it keeps is a **filter**.

</div>

<!--
**Say:** the same line as `Ctrl+G` 5000 in VS Code. A line that ends in `|` goes on in the next line; PowerShell shows `>>` there.
(~2 min)
-->

---
hideInToc: true
---

# The Pipe Carries **Text** or **Objects**

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

---
hideInToc: true
---

# Columns: `cut` and `Import-Csv`

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

---
hideInToc: true
---

# Order: `sort`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% tail -n +2 data/raw/weather.csv |
    cut -d, -f3 | sort | head -n 1
100
% tail -n +2 data/raw/weather.csv |
    cut -d, -f3 | sort -n | head -n 1
34
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Import-Csv data/raw/weather.csv |
>> Sort-Object humidity_pct |
>> Select-Object -First 1 -ExpandProperty humidity_pct
100
PS> Import-Csv data/raw/weather.csv |
>> Sort-Object {[int]$_.humidity_pct} |
>> Select-Object -First 1 -ExpandProperty humidity_pct
34
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The lowest humidity: 100 %? Text is compared character by character, and `1` comes before `3`. `sort -n` and `[int]` compare numbers: 34 %.

</div>

<!--
**Say:** `tail -n +2` prints from line 2 on, so the header stays out. `[int]` turns each value into a whole number before comparing.
**If asked:** the braces hold a small piece of code run for each row; `$_` is the row at hand.
(~2 min)
-->

---
hideInToc: true
---

# The Ends of a **Column**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cut -d, -f2 data/raw/weather.csv |
    sort -n | head -n 1
-999
% cut -d, -f2 data/raw/weather.csv |
    sort -n | tail -n 1
32.4
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Import-Csv data/raw/weather.csv |
>> Measure-Object temp_c -Minimum -Maximum

Count             : 87672
Maximum           : 32.4
Minimum           : -999
Property          : temp_c
```

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

❓ The coldest hour of ten years: −999 °C. Nothing on Earth is that cold, and nothing anywhere is: −273.15 °C is the lowest temperature there is. −999 is not a measurement.

</div>

<!--
**Say:** the third question of the opening. A sorted column shows its ends first, and a wrong value usually sits at an end. Looking at both ends of every column is the first check of a new file.
**If asked:** PowerShell also prints empty `Average`, `Sum` and `StandardDeviation` lines; they are left out here.
(~2 min)
-->

---
hideInToc: true
---

# Find the Rows: `grep`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% grep -c ',-999,' data/raw/weather.csv
120
% grep -n ',-999,' data/raw/weather.csv | head -n 1
31154:2019-07-22T00:00,-999,76,3.2
% grep -n ',-999,' data/raw/weather.csv | tail -n 1
31273:2019-07-26T23:00,-999,66,1.9
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Select-String ',-999,' data/raw/weather.csv).Count
120
PS> Select-String ',-999,' data/raw/weather.csv |
>> Select-Object -First 1
data\raw\weather.csv:31154:2019-07-22T00:00,-999,76,3.2
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 Lines 31 154 to 31 273: 31 273 − 31 154 + 1 = 120 hours, from 22 to 26 July 2019, five days of 24 hours. The thermometer was down, and the logger wrote −999 for "no value". The other columns went on.

</div>

<!--
**Say:** `grep` keeps the lines that contain a text: `-c` counts them, `-n` puts the line number in front. `Select-String` does both.
**If asked:** keep the commas in `',-999,'`: they make sure the whole value is −999.
(~2 min)
-->

---
hideInToc: true
---

# Count **Groups**: `uniq -c`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cut -c1-4 data/raw/weather.csv | uniq -c
   1 time
8784 2016
8760 2017
8760 2018
8760 2019
8784 2020
8760 2021
…
8760 2025
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Import-Csv data/raw/weather.csv |
>> Group-Object {$_.time.Substring(0,4)} -NoElement

Count Name
----- ----
 8784 2016
 8760 2017
 8760 2018
 8760 2019
…
```

</div>

</div>

<div class="note-text mt-md">Rows per year: 365 × 24 = 8760, and 366 × 24 = 8784 in a leap year. 2019 has all its rows: the 120 marked hours are there, with −999 in them.</div>

<!--
**Say:** `cut -c1-4` keeps the first four characters, the year. `uniq -c` merges equal lines that stand next to each other and counts them; the file is in time order, so each year is one block.
**If asked:** on unsorted data, `sort` comes before `uniq -c`.
(~2 min)
-->

---
hideInToc: true
---

# From `data/raw` to `data/processed`

<div class="card card-primary card-glass pad-compact mt-sm">

## ✍️ **Keep the rows without the mark**

```text
% grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv
PS> Select-String ',-999,' data/raw/weather.csv -NotMatch -Raw > data/processed/weather_valid.csv
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -l data/processed/weather_valid.csv
   87553 data/processed/weather_valid.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Get-Content data/processed/weather_valid.csv).Count
87553
```

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ 87 673 − 120 = 87 553 lines. The raw file stays as it was: delete the new file, run the line again, and it is back.

</div>

<!--
**Say:** `-v` and `-NotMatch` keep the lines that do not contain the text. `-Raw` passes on only the text of each line, without file name and line number.
**If asked:** the Windows file is larger, 2 599 288 bytes against 2 511 735: one more byte, `0D`, on each of its 87 553 lines.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Regular **Expressions**

`grep` kept the lines that contain one fixed text. A pattern describes a kind of text, and the same pattern works in VS Code and in both shells.

<!--
**Say:** so far the search was for a fixed text, `,-999,`. Now the search is for a kind of text.
(~1 min)
-->

---
hideInToc: true
---

# A Pattern Instead of a **Text**

<div class="note-text mt-sm">Question: in how many hours was it below freezing?</div>

<div class="card card-info card-glass pad-compact mt-sm">

```text
% grep -c ',-' data/raw/weather.csv
22472
% grep -cE ',-[0-9]+\.[0-9],' data/raw/weather.csv
22352
PS> (Select-String ',-' data/raw/weather.csv).Count
22472
PS> (Select-String ',-[0-9]+\.[0-9],' data/raw/weather.csv).Count
22352
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔎 **A fixed text finds too much**

`,-` is also in the 120 rows with `,-999,`. 22 472 − 22 352 = 120.

</div>

<div class="card card-success card-glass pad-compact">

## ✳️ **A pattern says what kind**

A minus, digits, a point, one digit. Such a text is a **regular expression**, regex for short.

</div>

</div>

<!--
**Say:** the temperatures have one decimal, −999 has none. The pattern uses that difference. The next two slides read the pattern sign by sign.
**If asked:** `-E` lets grep read `+`; Select-String reads every pattern as a regex.
(~2 min)
-->

---
hideInToc: true
---

# Signs for **One Character**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Sign | Fits | Pattern | Lines it fits in `daily_export.csv` |
| --- | --- | --- | --- |
| a letter, a digit, `,` | itself | `10,` | 1: `6;2025-10-06;10,4` |
| `.` | any one character | `10.` | 9: every row, at `10-` in the date |
| `[0-9]` | one character from `0` to `9` | `[0-9],` | 10: the rows and the mean line |
| `[a-z]` | one lower-case letter | `[a-z]` | 2: the header and the mean line |
| `[^0-9;,-]` | one character **not** listed | `[^0-9;,-]` | 2: the same two |

</div>

<div class="note-text mt-md">A backslash takes the special meaning away: <code>\.</code> fits a point and nothing else.</div>

<!--
**Ask:** before reading the count for `10.`, how many lines will it fit?
(~3 min)
-->

---
hideInToc: true
---

# Signs for **How Many** and **Where**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Sign | Meaning | Pattern | Lines it fits in `daily_export.csv` |
| --- | --- | --- | --- |
| `+` | one or more of what stands before | `[0-9]+;` | 9: the rows |
| `*` | none or more | `;.*;` | 11: all |
| `{2}` | exactly two | `;[0-9]{2},` | 1: `6;2025-10-06;10,4` |
| `^` | the start of the line | `^;` | 1: `;mean;7,97` |
| `$` | the end of the line | `0$` | 3: `5,0`, `7,0`, `9,0` |
| `( )`, `\|` | a group, and "or" | `-(01\|02);` | 2: 1 and 2 October |

</div>

<div class="note-text mt-md"><code>+</code>, <code>*</code> and <code>{2}</code> repeat the one thing before them. <code>^</code> and <code>$</code> fit no character: they pin the pattern to an end of the line.</div>

<!--
**Say:** `^;` finds the mean line without the word mean: it is the only line with no row number.
(~3 min)
-->

---
hideInToc: true
---

# Regex in the **Find Box**

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

---
hideInToc: true
---

# Capture **Groups**

<div class="card card-info card-glass pad-compact mt-sm">

Round brackets mark a part of the match. In the Replace box `$1` puts back what the first pair matched, `$2` the second.

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

---
layout: section
hideInToc: true
---

# Programs **Someone Else Wrote**

Filters count, sort and keep lines. Cleaning the export and computing a mean take a program, and a program runs with one typed line.

<!--
**Say:** two small Python programs came with the folder. They are run like any other command; nobody has to read Python today.
(~1 min)
-->

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

---
hideInToc: true
---

# Run It, Then **Measure** It

<div class="card card-info card-glass pad-compact mt-sm">

```text
% python3 scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
9 rows written to data/processed/daily.csv
% wc -c data/processed/daily.csv
     148 data/processed/daily.csv
PS> python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
9 rows written to data/processed/daily.csv
PS> (Get-Item data/processed/daily.csv).Length
148
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **148, byte by byte**

Header `date,temp_c` and LF: 12. Eight rows like `2025-10-01,6.3`: 15 each. `2025-10-06,10.4`: 16. 12 + 8 × 15 + 16 = 148.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **The line, read**

The program, `python3` or `python`. Then its file. Then two words for the script: the file it reads, the file it writes.

</div>

</div>

<!--
**Say:** macOS names the program `python3`, Windows `python`. The paths are the same.
**If asked:** "Python was not found" on Windows: the section Tools & Environments explains it.
(~3 min)
-->

---
hideInToc: true
---

# Where **158** Bytes Come From

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

## 🔎 **Ten lines, ten bytes**

158 − 148 = 10. PowerShell writes each of the ten lines itself and ends it with CRLF.

</div>

<div class="card card-success card-glass pad-compact">

## 🧷 **The script states its bytes**

Line 49 of `clean_export.py`: `newline="\n"`. Every line ends with LF on every system, so the script wrote 148 bytes in both shells.

</div>

</div>

<!--
**Say:** neither shell is wrong; each writes text by its own rule. A file whose bytes must match everywhere is written by a program that states the rule.
(~2 min)
-->

---
hideInToc: true
---

# A Program for **87 672 Rows**

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

## 🧭 **The same shape**

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

---
hideInToc: true
---

# What 120 Rows Do to a **Mean**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📥 **`data/raw/weather.csv`**

```text
rows    87672
min     -999.0
max     32.4
mean    5.7828
```

</div>

<div class="card card-success card-glass pad-compact">

## ⚙️ **`data/processed/weather_valid.csv`**

```text
rows    87552
min     -16.3
max     32.4
mean    7.15997
```

</div>

</div>

<div class="card card-primary card-glass pad-compact mt-md">

🧮 120 rows are 0.14 % of the file. Each puts −999 into the sum: 120 × (−999) / 87 672 = −1.37 °C. The mean drops from 7.16 to 5.78 °C. A mark for "no value" written as a number is counted as a number by every program.

</div>

<!--
**Say:** five lost days moved a ten-year mean by more than a degree. This is why the mark is found before any number is computed.
**If asked:** the last hundredth of the 1.38 comes from the 120 summer hours that are missing from the valid rows.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Tools & **Environments**

The cleaning line starts with `python3` or `python`: a program somebody installed. Where programs come from, how the shell finds them, what it runs at start, and how a project lists the ones it needs.

<!--
**Say:** every command so far was already on the laptop, or came with one typed line, like PowerShell 7. Python is the next one.
(~1 min)
-->

---
hideInToc: true
---

# Where a Program **Comes From**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
% which python3
/Users/ada/miniforge3/bin/python3
PS> (Get-Command python).Source
C:\Users\ada\miniforge3\python.exe
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
**Say:** a program is usable at the prompt when its folder is on the list the shell searches. That list is the next slide.
**If asked:** Miniforge installs into the folder `miniforge3` in the home folder. A Mac without it answers `/usr/bin/python3`, Apple's copy.
(~2 min)
-->

---
hideInToc: true
---

# The List the Shell Searches: **PATH**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
% echo $PATH | tr ':' '\n'
/Users/ada/miniforge3/bin
/Users/ada/miniforge3/condabin
/usr/bin
PS> $env:PATH -split ';'
C:\Users\ada\miniforge3
C:\Users\ada\miniforge3\Scripts
C:\Windows\system32
C:\Program Files\PowerShell\7\
C:\Users\ada\AppData\Local\Microsoft\WindowsApps
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ➡️ **Top to bottom**

The shell takes the first folder that holds a program of the typed name. Of two Pythons on the list, the first one runs.

</div>

<div class="card card-warning card-glass pad-compact">

## 🪟 **"Python was not found"**

`WindowsApps` holds a stand-in `python.exe`. In a PowerShell where conda was never set up, the Miniforge folders are missing, and the stand-in answers.

</div>

</div>

<!--
**Say:** a terminal reads PATH when it opens: a program installed meanwhile is found only in a new terminal. The lists are shortened; a real laptop shows ten to twenty folders.
**If asked:** without Miniforge a Mac has only `python3`, so the course writes `python3` there. Inside Miniforge both names work.
(~3 min)
-->

---
hideInToc: true
---

# A Package **Manager**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Job | 🪟 `winget`, part of Windows | 🍎 Homebrew, `brew` |
| --- | --- | --- |
| Find a name | `winget search powershell` | `brew search git` |
| Install | `winget install --id Microsoft.PowerShell` | `brew install git` |
| What is installed | `winget list` | `brew list --versions` |
| Newer versions | `winget upgrade --all` | `brew upgrade` |
| Remove | `winget uninstall --id Microsoft.PowerShell` | `brew uninstall git` |

</div>

<div class="card card-success card-glass pad-compact mt-md">

📜 A package manager looks a name up in a catalogue, downloads the files, and puts their folder on `PATH`. The install line can go into the README: on the next laptop it installs the same program.

</div>

<!--
**Say:** the five jobs are the same in every package manager. The course needs no Homebrew: Python comes from Miniforge on both systems, and its `conda` is a package manager too.
**If asked:** Linux has `apt`, with the same five jobs.
(~2 min)
-->

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

## ⚠️ **Only here**

Both last until this terminal closes, and exist only on this laptop. A README line uses the full command.

</div>

</div>

<!--
**Say:** the Miniforge installer changes how every new shell starts. First, two settings typed by hand. They last only as long as this terminal; the next slide keeps them.
**If asked:** `%1~` is the last folder of the path, `%#` the `%` sign. A PowerShell alias cannot carry an argument such as `..`, so a function does it.
(~2 min)
-->

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
/Users/ada/.zshrc
PS> $PROFILE
C:\Users\ada\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
```

</div>

<div class="note-text mt-md">A new terminal reads the file. <code>source ~/.zshrc</code> or <code>. $PROFILE</code> reads it again in the open one.</div>

<!--
**Say:** the same lines as on the last slide, written once into a file: from now on every terminal starts with them.
**If asked:** neither file exists on a new laptop; the first save makes it. With OneDrive, `$PROFILE` lies under `OneDrive\Documents`.
(~2 min)
-->

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

---
hideInToc: true
---

# What `conda init` **Wrote**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **zsh: the end of `~/.zshrc`**

```text
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/ada/miniforge3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
…
# <<< conda initialize <<<
```

</div>

<div class="card card-secondary card-glass pad-compact mt-md">

## 🪟 **PowerShell: `profile.ps1`, in the folder of `$PROFILE`**

```text
#region conda initialize
If (Test-Path "C:\Users\ada\miniforge3\Scripts\conda.exe") {
    (& "C:\Users\ada\miniforge3\Scripts\conda.exe" "shell.powershell" "hook") | … | Invoke-Expression
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

---
hideInToc: true
---

# `conda`: Packages and **Environments**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **zsh** · 🪟 **PowerShell: the same lines**

```text
(base) % conda --version
conda 26.7.2
(base) % conda config --show channels
channels:
  - conda-forge
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📦 **A package manager**

Installs packages from a **channel**, a catalogue: here conda-forge. A package can be Python itself, a Python library, or a C library that a Python library needs.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧪 **An environment manager**

An **environment** is a folder with one Python and its packages. The installer made the first one, `base`.

</div>

</div>

<!--
**Say:** two jobs in one program. `winget` installs a program for the whole laptop; `conda` installs into one environment at a time.
**If asked:** Miniforge is conda with conda-forge as its only channel, free to use. Anaconda's own channel, `defaults`, has terms for large organisations.
(~2 min)
-->

---
hideInToc: true
---

# One Python, **Every Project**

<div class="card card-primary card-glass pad-compact mt-sm">

## 💥 **A script for numpy 1.26, run where numpy 2.5 is installed**

```text
% python -c "import numpy as np; print(np.float_)"
AttributeError: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **One Python for all**

Every project run in one shared Python imports the same numpy. An upgrade for one project broke a script of another.

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **One environment per project**

Each project gets a Python and packages of its own. `base` stays as the installer made it, without numpy.

</div>

</div>

<!--
**Say:** this is the usual way a working script stops working: nothing in the script changed, a package on the laptop did.
**If asked:** `np.float_` existed up to numpy 1.26 and was removed in 2.0, June 2024.
(~2 min)
-->

---
hideInToc: true
---

# An Environment Is a **Folder**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **zsh** · 🪟 **PowerShell: the same lines**

```text
(base) % conda create -n weather python=3.14
  environment location: /Users/ada/miniforge3/envs/weather
…
Proceed ([y]/n)? y
(base) % conda env list
# conda environments:
#
# * -> active
# + -> frozen
base                 *   /Users/ada/miniforge3
weather                  /Users/ada/miniforge3/envs/weather
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📁 **What is in it**

24 packages: Python 3.14.8, pip, and 22 that Python needs. 221 MB in 6135 files.

</div>

<div class="card card-info card-glass pad-compact">

## 🗑️ **Made again, never copied**

`conda env remove -n weather` deletes the folder. One line makes it again.

</div>

</div>

<!--
**Say:** `-n` names the environment, `python=3.14` asks for its Python. Nothing is active yet: the `*` is still at `base`.
**If asked:** on Windows the folder is `C:\Users\ada\miniforge3\envs\weather`. Counts and sizes measured on Linux with Miniforge 26.7.2; they differ a little by system.
(~2 min)
-->

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
/Users/ada/miniforge3/envs/weather/bin/python
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
C:\Users\ada\miniforge3\envs\weather\python.exe
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
**If asked:** `echo $PATH | tr ':' '\n'` now starts with `/Users/ada/miniforge3/envs/weather/bin`. On Windows the environment's folder holds `python.exe` itself; its `Scripts` follows on `PATH`.
(~3 min)
-->

---
hideInToc: true
---

# `conda install numpy`, **Measured**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **zsh** · 🪟 **PowerShell: the same lines**

```text
(weather) % python -c "import numpy"
ModuleNotFoundError: No module named 'numpy'
(weather) % conda install numpy
…
Proceed ([y]/n)? y
(weather) % conda list numpy
# packages in environment at /Users/ada/miniforge3/envs/weather:
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

---
hideInToc: true
---

# **environment.yml**: the List, Written Down

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **zsh** · 🪟 **PowerShell: the same lines**

```text
(weather) % conda env export --from-history > environment.yml
(weather) % cat environment.yml
name: weather
channels:
  - conda-forge
dependencies:
  - python=3.14
  - numpy
prefix: /Users/ada/miniforge3/envs/weather
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 💻 **On another laptop**

Delete the line `prefix:`, which names this laptop. `conda env create -f environment.yml` then makes `weather` there. `- numpy=2.5.4` would ask for one version.

</div>

<div class="card card-success card-glass pad-compact">

## 🧭 **Why `--from-history`**

The full export lists every package with its build, such as `bzip2=1.0.8=hda65f42_10`: made for one system. This file keeps what was asked for, and works on every system.

</div>

</div>

<!--
**Say:** the file is the environment, written down, as the README lines are the cleaning, written down. The project keeps `environment.yml` like `scripts`, and makes the environment again from it, like `data/processed` from `data/raw`.
**If asked:** today's two scripts need no package, so this project's own file would list only `python=3.14`.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Checksums & **Backups**

The same ten lines were 148 bytes in one file and 158 in another. A checksum tells files apart by their bytes; backups keep the right ones.

<!--
**Say:** a checksum is a short number computed from every byte of a file. Here it is one command in each shell.
(~1 min)
-->

---
hideInToc: true
---

# The Checksum of a **File**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
% shasum -a 256 data/raw/weather.csv
3f1ad06d3bb5773eac79dfc964cdf8af998689ef58aa8623f25d2050fbe00756  data/raw/weather.csv
PS> (Get-FileHash data/raw/weather.csv).Hash
3F1AD06D3BB5773EAC79DFC964CDF8AF998689EF58AA8623F25D2050FBE00756
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔠 **The same 64 digits**

Lower case on the Mac, upper case on Windows: one number. 64 hex digits are the 256 bits of SHA-256.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧬 **One digit changes all**

```text
33fe5e77…f705483d   2025-10-01,6.3
58709abc…fb40d36b   2025-10-01,6.4
```

`daily.csv`, and a copy with one digit changed.

</div>

</div>

<!--
**Ask:** a colleague has a `weather.csv` too. Is it the same file? 2.5 million bytes cannot be compared by eye. Read the first and the last four digits: 3f1a and 0756.
(~2 min)
-->

---
hideInToc: true
---

# A List of Checksums for `data/raw`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% shasum -a 256 data/raw/* > data/checksums.txt
% shasum -a 256 -c data/checksums.txt
data/raw/daily_export.csv: OK
data/raw/weather.csv: OK
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Get-FileHash data/raw/*).Hash |
>> Set-Content data/checksums.txt
PS> $list = Get-Content data/checksums.txt
PS> $now = (Get-FileHash data/raw/*).Hash
PS> Compare-Object $list $now
PS>
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The list is written once, when the raw files arrive, and checked after every copy. `-c` computes each checksum again and compares. `Compare-Object` prints only the lines that differ: nothing means the same.

</div>

<!--
**Say:** "raw is never edited" becomes a test that runs in a second. The list stands in `data`, not in `data/raw`, so `data/raw/*` never includes it.
**If asked:** `$list = …` keeps an output under a name for the next line.
(~2 min)
-->

---
hideInToc: true
---

# One Digit **Changed**

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
**Say:** zsh names the file. PowerShell shows the old and the new checksum; the old one is line 1 of the list, the export.
(~1 min)
-->

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

<!--
**Say:** the 1 in 20 is an assumption for the arithmetic, not a measured rate. The point is the exponent, and when it applies.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The **README**

The README is where the checksums, the meaning of the columns and the lines that make every file again are written down.

<!--
**Say:** the README of `weather-project` says what the project is, its folders and where the files came from. This section completes it.
(~1 min)
-->

---
hideInToc: true
---

# What a Stranger **Asks**

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
**Say:** the checksum list answered the third question already. The next slides answer the others.
(~2 min)
-->

---
hideInToc: true
---

# Columns and **Units**

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

---
hideInToc: true
---

# How to **Rebuild**

<div class="card card-primary card-glass pad-compact mt-sm">

## ✏️ **In the README**

```md
## How to rebuild

In the project folder: zsh on macOS, PowerShell 7 on Windows.
Python 3.14 from Miniforge; the scripts need no package beyond it.

1. The cleaned export, 148 bytes, SHA-256 `33fe5e77…f705483d`:
   - zsh: `python3 scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv`
   - PowerShell: `python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv`
2. `weather.csv` without the 120 rows marked `-999`, 87 553 lines:
   - zsh: `grep -v ',-999,' data/raw/weather.csv > data/processed/weather_valid.csv`
   - PowerShell: `Select-String ',-999,' data/raw/weather.csv -NotMatch -Raw > data/processed/weather_valid.csv`
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

♻️ These lines are the work itself, copied from the terminal history with `↑`, not typed from memory.

</div>

<!--
**Say:** the lines are brought back with ↑ and pasted, never retyped. A line that was copied and ran has been tested; a line typed from memory has not.
(~2 min)
-->

---
hideInToc: true
---

# Test the **Section**

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

---
hideInToc: true
---

# The **Licence**

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

---
hideInToc: true
---

# Which Copy? **The README Says**

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

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Set up **zsh** or **PowerShell 7**, read the prompt, and move with `pwd`, `ls` and `cd`

</div>

<div class="card card-success card-glass pad-compact">

✅ Name a file by an **absolute** or a **relative path**, and read, count, copy, move and delete files

</div>

<div class="card card-success card-glass pad-compact">

✅ Join commands with **pipes** and `>`, and find the mark −999 in 87 672 rows

</div>

<div class="card card-success card-glass pad-compact">

✅ Write a **regular expression** with `[ ]`, `+`, `^`, `$` and groups

</div>

<div class="card card-success card-glass pad-compact">

✅ Run a **script** someone else wrote, install with `winget` and `conda`, and give a project its own **conda environment**

</div>

<div class="card card-success card-glass pad-compact">

✅ Name a file by size and **SHA-256** in the README, and keep copies by the **3-2-1** rule

</div>

</div>

<!--
**Say:** the three questions of the opening: 87 673 lines, line 5000, and a coldest hour that was a mark, not a measurement.
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
  question="The terminal is in weather-project/results. Which path names the raw weather file, in zsh and in PowerShell alike?"
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
  question="notes.txt has five lines. Then `echo done > notes.txt` and `echo checked >> notes.txt` run. How many bytes does it have in zsh on a Mac and in PowerShell 7 on Windows?"
  :options="[
    'More than 13 in both, because the five old lines are kept',
    '13 and 13',
    '15 and 13',
    '13 and 15'
  ]"
  :correct="3"
  explanation="A single > empties the file first, so the five lines are gone, and >> adds a second line. The letters are 4 + 7 = 11. zsh ends each line with LF, one byte: 13 bytes. PowerShell on Windows ends each line with CRLF, two bytes: 15 bytes."
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
  explanation="Without -n, sort compares the values as text, from the left. 100 starts with 1, 34 with 3, so 100 comes first. sort -n compares numbers and puts 34 first. In PowerShell, [int] in Sort-Object does the same."
/>

---
hideInToc: true
---

<MCQ
  question="In PowerShell, `ls data/raw | Sort-Object Length` lists daily_export.csv (180 bytes) before weather.csv. What does the pipe carry?"
  :options="[
    'File objects, each with properties such as Name and Length',
    'Lines of text, in which Sort-Object finds the size as the fifth word',
    'The bytes of the two files',
    'Only the two names, and Sort-Object opens each file to measure it'
  ]"
  :correct="0"
  explanation="A PowerShell pipe carries objects. ls hands on two file objects, and Sort-Object reads the property Length of each. A zsh pipe carries lines of text: wc -c data/raw/* | sort -n finds the size as the first word of each line."
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
  explanation="The pattern fits a whole line of digits and minus signs, a comma, a number, a point and one digit. The header has letters. The line with semicolons has a semicolon where the pattern allows only digits and minus signs, and no point. grep -E, Select-String and the Find box of VS Code find the same two lines."
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
  question="On a Mac, `shasum -a 256 daily.csv` prints 33fe5e77…f705483d. On Windows, `Get-FileHash daily.csv` prints 33FE5E77…F705483D. What follows?"
  :options="[
    'Nothing, because the two programs compute different checksums',
    'The two files hold the same values, but their line endings may differ',
    'The two files hold the same 148 bytes',
    'The Windows file is larger, because of CRLF'
  ]"
  :correct="2"
  explanation="Get-FileHash computes SHA-256 too and writes the hex digits in capitals: the digits are the same. A checksum is computed from every byte, so line endings count. The same table with CRLF line endings has 158 bytes and the checksum b68430c5…."
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
  question="Two folders on PATH hold a program named python: C:\Python312 is listed before C:\Python314. The terminal types python --version. Which Python answers?"
  :options="[
    'Python 3.14, because the newer version wins',
    'Python 3.12, because the shell stops at the first folder that holds the name',
    'Both print a line, one after the other',
    'Neither: two programs of one name on PATH is an error'
  ]"
  :correct="1"
  explanation="The shell goes through PATH in order and runs the first program of that name it finds. A newer version further down the list is never reached. That is why conda puts the folder of the active environment first, and why a stand-in python.exe in a folder listed earlier answers in its place."
/>

---
hideInToc: true
---

<MCQ
  question="A colleague receives the project folder with environment.yml, which lists python=3.14 and numpy=2.5.4. Which lines give them the same environment?"
  :options="[
    '<code>conda install numpy</code> in base, nothing else',
    'Copy the folder miniforge3/envs/weather from your laptop into theirs',
    '<code>conda env create -f environment.yml</code>, then <code>conda activate weather</code>',
    'Open environment.yml in VS Code: the packages install themselves'
  ]"
  :correct="2"
  explanation="An environment is made on the laptop it runs on, from the file. conda env create reads the channel and the packages, and numpy=2.5.4 pins the version, so 2.5.4 arrives and not the newest one. A copied environment folder holds paths of the other laptop, and base is shared by every project."
/>
