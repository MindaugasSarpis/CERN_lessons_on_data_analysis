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

<div class="note-text mt-md">Every answer comes from a typed line in PowerShell 7, the same line on macOS and on Windows.</div>

<!--
**Say:** one question per part of the lecture. The answer column fills up as we go; it closes the lecture.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# The **Shell**

Step 1: one shell on every laptop, and the columns of the file.

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

A program that reads a typed line, runs what the line names, and waits for the next line: PowerShell, zsh, bash.

</div>

<div class="card card-accent card-glass pad-compact">

## ⚙️ **Program**

A file the computer can run: `pwsh`, `python`, `git`. The shell itself is one.

</div>

</div>

<div class="card card-info card-glass pad-compact table-compact mt-md">

| | Comes with the system | This course |
| --- | --- | --- |
| macOS | zsh, in the app Terminal | PowerShell 7, `pwsh` |
| Windows | Windows PowerShell 5.1 | PowerShell 7, `pwsh` |

</div>

<!--
**Say:** the terminal is only the window. The shell inside it does the work, and it can be changed without changing the window. One shell on both systems means one line on every slide.
**If asked:** PowerShell 7 is free and open source, made by Microsoft for Windows, macOS and Linux. Windows PowerShell 5.1 is no longer developed.
(~2 min)
-->

---
hideInToc: true
---

# What the Shell Does with a **Line**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Get-Content -TotalCount 2 data/raw/weather.csv
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| | The shell | On this line |
| --- | --- | --- |
| 1 | waits for `Enter`, then reads the line | the whole line |
| 2 | splits it into words at the spaces | 4 words; `"weather station.csv"` in quotes stays one |
| 3 | replaces what it knows: `$HOME`, `$file`, `( … )` | nothing here |
| 4 | finds the command the first word names | `Get-Content`, part of PowerShell |
| 5 | runs it with the other words, shows its output | the first 2 lines of the file |
| 6 | notes whether it worked, prints the prompt | `PS>` again |

</div>

<!--
**Say:** every line today goes through these six steps. Step 2 is why a space in a file name breaks a line: the shell sees two names.
**If asked:** `$?` holds the result of step 6: `True` when the last command worked.
(~2 min)
-->

---
hideInToc: true
---

# macOS: Homebrew, Then **PowerShell 7**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **In the app Terminal, which starts zsh**

```text
% /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Installation successful!
% brew install --cask powershell
🍺  powershell was successfully installed!
% pwsh
PowerShell 7.6.6
PS> $PSVersionTable.PSVersion.ToString()
7.6.6
```

</div>

<div class="note-text mt-md">Homebrew is a package manager for macOS: it installs a program by name. The first line installs Homebrew itself, the second PowerShell 7. <code>pwsh</code> starts it.</div>

<!--
**Say:** two lines, typed once per laptop. After them the Mac has the same shell as every Windows laptop in the room.
**If asked:** the Homebrew installer asks for the Mac's login password, and nothing appears while it is typed. On Apple Silicon it ends with "Next steps": two lines to paste, which put `/opt/homebrew/bin` on the list of folders the shell searches.
(~2 min)
-->

---
hideInToc: true
---

# Windows: **PowerShell 7** with winget

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🪟 **In Windows PowerShell 5.1: Start, `PowerShell`**

```text
PS C:\Users\smilte> winget install --id Microsoft.PowerShell --source winget
Found PowerShell [Microsoft.PowerShell] Version 7.6.6
…
Successfully installed
PS C:\Users\smilte> pwsh
PowerShell 7.6.6
PS C:\Users\smilte> $PSVersionTable.PSVersion.ToString()
7.6.6
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

🖥️ VS Code, both systems: `Ctrl+Shift+P` (macOS `Cmd+Shift+P`), **Terminal: Select Default Profile**, **pwsh**. Every new terminal of VS Code then starts PowerShell 7.

</div>

<!--
**Say:** winget is the package manager that comes with Windows; the line names the package by its id.
**If asked:** winget asks once to accept its source agreements: `Y`. A university laptop may ask for an administrator password. On Windows the list offers PowerShell (that is 7) and Windows PowerShell (5.1): pick PowerShell.
(~2 min)
-->

---
hideInToc: true
---

# Read the Prompt, List the **Folder**

<div class="card card-info card-glass pad-compact mt-sm">

```text
PS /Users/smilte/Documents/weather-project>        the prompt on macOS
PS C:\Users\smilte\Documents\weather-project>      the prompt on Windows
```

</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS**

```text
PS> Get-ChildItem

UnixMode    User   … Size Name
--------    ----     ---- ----
drwxr-xr-x  smilte …  128 data
drwxr-xr-x  smilte …   64 results
drwxr-xr-x  smilte …  128 scripts
-rw-r--r--  smilte …  688 README.md
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows**

```text
PS> Get-ChildItem

Mode    LastWriteTime  Length Name
----    -------------  ------ ----
d----   13/10/2026 …          data
d----   13/10/2026 …          results
d----   13/10/2026 …          scripts
-a---   13/10/2026 …      688 README.md
```

</div>

</div>

<div class="note-text mt-md">The prompt: <code>PS</code>, the folder the shell is in, the <strong>working directory</strong>, then <code>&gt;</code>. Every path on a line starts there. The slides shorten the prompt to <code>PS&gt;</code>.</div>

<!--
**Say:** the same command, the same four names. The table differs by system: `d` marks a folder on both, and the size of a file is `Size` on macOS, `Length` on Windows.
**If asked:** a folder's `Size` on macOS is the space its list of names takes, not its contents. `Get-ChildItem -Name` prints the names alone.
(~2 min)
-->

---
hideInToc: true
---

# The Commands of Lecture 03, in **PowerShell**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| To | Command | Short name, on both systems |
| --- | --- | --- |
| see where the shell is | `Get-Location` | `pwd` |
| list a folder | `Get-ChildItem data/raw` | `dir`, `gci` |
| change folder | `Set-Location data` | `cd` |
| make a folder | `New-Item -ItemType Directory backup` | `ni` |
| copy, move or rename | `Copy-Item`, `Move-Item FROM TO` | `copy`, `move` |
| delete, no undo | `Remove-Item backup -Recurse` | `del` |
| read a file | `Get-Content data/raw/weather.csv` | `gc`, `type` |
| measure a file | `(Get-Item data/raw/weather.csv).Length` | |

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ On macOS, `ls`, `cat`, `cp`, `mv`, `rm` and `mkdir` start the Mac's own programs, with other options and output. Write the names of this table.

</div>

<!--
**Say:** nothing new here: Lecture 03 typed these. PowerShell names a command Verb-Noun: what it does, then to what.
**If asked:** on Windows `ls` and `cat` are short names for `Get-ChildItem` and `Get-Content`; on macOS PowerShell leaves those words to the system's programs.
(~2 min)
-->

---
hideInToc: true
---

# Paths That Work on Every **Laptop**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| The terminal is in | Path to `weather.csv` |
| --- | --- |
| `weather-project` | `data/raw/weather.csv` |
| `weather-project/data` | `raw/weather.csv` |
| `weather-project/scripts` | `../data/raw/weather.csv` |
| anywhere, on Smiltė's Mac | `/Users/smilte/Documents/weather-project/data/raw/weather.csv` |
| anywhere, on Smiltė's Windows laptop | `C:\Users\smilte\Documents\weather-project\data\raw\weather.csv` |

</div>

<div class="card card-success card-glass pad-compact mt-md">

♻️ The terminal stays in `weather-project`, and every path starts there. A relative path is the same on every laptop; an absolute path names one user on one computer.

</div>

<!--
**Say:** `..` is the folder one level up, `.` the folder the shell is in, `~` the home folder. PowerShell on Windows reads `/` and `\` alike, so the slides write `/`.
(~2 min)
-->

---
hideInToc: true
---

# The Parts of a **Command**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Get-Content -TotalCount 2 data/raw/weather.csv
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ⚙️ **Command**

The first word: `Get-Content`.

</div>

<div class="card card-accent card-glass pad-compact">

## 🎚️ **Parameter**

How to work, a name with a dash and its value: `-TotalCount 2`.

</div>

<div class="card card-info card-glass pad-compact">

## 📄 **Argument**

What to work on: the path.

</div>

</div>

<!--
**Say:** the order of named parameters does not matter: `Get-Content data/raw/weather.csv -TotalCount 2` is the same line.
**If asked:** PowerShell ignores case, so `-totalcount` works too. `-Head` is another name for `-TotalCount`.
(~2 min)
-->

---
hideInToc: true
---

# A Variable Holds a **Value**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> $file = 'data/raw/weather.csv'
PS> $file
data/raw/weather.csv
PS> (Get-Content $file).Count
87673
PS> $HOME
/Users/smilte
PS> $PSVersionTable.PSVersion.ToString()
7.6.6
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

A **variable** is a name the shell keeps a value under: `$` and the name. `=` puts a value in; the name alone reads it. PowerShell sets some itself: `$HOME`, `$PSVersionTable`, and after every line `$?`.

</div>

<!--
**Say:** step 3 of the shell: `$file` is replaced by its value before `Get-Content` runs. A variable lasts until the terminal closes.
**If asked:** on Windows `$HOME` is `C:\Users\smilte`. `$env:PATH` reads a variable of the system, which every program sees.
(~2 min)
-->

---
hideInToc: true
---

# Complete Names with `Tab`

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⌨️ **Type a start, press `Tab`**

```text
Get-Con       Tab →  Get-Content
… -Tot        Tab →  … -TotalCount
… da          Tab →  … ./data
… ./data/r    Tab →  … ./data/raw
… ./data/raw/w  Tab →  … ./data/raw/weather.csv
```

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **No typing mistakes**

A name that `Tab` completed exists. If `Tab` adds nothing, no name fits: the line is wrong before it runs.

</div>

</div>

<div class="card card-info card-glass pad-compact table-compact mt-md">

| `↑` `↓` | `Ctrl+R` | `Ctrl+C` | `clear` |
| --- | --- | --- | --- |
| the earlier lines | search them | stop what runs | empty the window |

</div>

<!--
**Live:** type `Get-Con`, `Tab`, a space, `-Tot`, `Tab`, ` 2 da`, `Tab`, `/r`, `Tab`, `/w`, `Tab`, `Enter`; then `↑` brings the line back.
**Ask:** count the keys: how many were typed, how many did Tab add?
**If asked:** on Windows Tab writes `.\data\raw\weather.csv`. With two names that fit, Tab goes through them in turn; `Ctrl+Space` lists them.
(~3 min)
-->

---
hideInToc: true
---

# Find a Command and Its **Parameters**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔎 **Every command for files: noun `Item`**

```text
PS> Get-Command -Noun Item

CommandType     Name
-----------     ----
Cmdlet          Clear-Item
Cmdlet          Copy-Item
Cmdlet          Get-Item
Cmdlet          Move-Item
Cmdlet          New-Item
Cmdlet          Remove-Item
…
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📖 **The parameters of one**

```text
PS> Get-Help Get-Content

NAME
    Get-Content

SYNTAX
    Get-Content [-Path] <string[]>
    [-TotalCount <long>] [-Tail <int>]
    [-Raw] [-Encoding <Encoding>] …

ALIASES
    gc
    type
```

</div>

</div>

<!--
**Say:** the Verb-Noun names make PowerShell searchable: the verbs are few (Get, Set, New, Remove, Copy, Move), so a guess is often right.
**If asked:** PowerShell 7 ships without the long help texts. `Get-Help Get-Content -Online` opens them in the browser; `Update-Help` downloads them once. A cmdlet is a command built into PowerShell.
(~2 min)
-->

---
hideInToc: true
---

# Read an Error **Message**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Get-Contnt data/raw/weather.csv
Get-Contnt: The term 'Get-Contnt' is not recognized as a name of a cmdlet,
function, script file, or executable program.
PS> Get-Content data/raw/wether.csv
Get-Content: Cannot find path '/Users/smilte/Documents/weather-project/data/
raw/wether.csv' because it does not exist.
PS> Get-Content -TotalCount 2 weather station.csv
Get-Content: A positional parameter cannot be found that accepts argument
'station.csv'.
```

</div>

<div class="note-text mt-md">The word before the first colon says who complains: the shell found no command, or the command found no file, or the shell split a name in two.</div>

<!--
**Ask:** what went wrong in each line? Let the room read before you explain.
**Say:** an error message is an answer. Read it before retyping.
**If asked:** on Windows the path in the second message is `C:\Users\smilte\Documents\weather-project\data\raw\wether.csv`.
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

# The First and the Last **Lines**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Get-Content data/raw/weather.csv -TotalCount 3
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
2016-01-01T01:00,-4.8,95,2.6
PS> Get-Content data/raw/weather.csv -Tail 2
2025-12-31T22:00,-9.9,98,4.1
2025-12-31T23:00,-11.3,100,4.2
```

</div>

<div class="note-text mt-md">The header, the first hour and the last: the log runs from midnight of New Year 2016 to 23:00 on New Year's Eve 2025, one row per hour.</div>

<!--
**Say:** the ends of a file tell how far it goes. They do not tell whether an hour in the middle is missing; a count does.
(~2 min)
-->

---
hideInToc: true
---

# Count the **Lines**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> (Get-Content data/raw/weather.csv).Count
87673
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 How many hours do ten years hold? 2016, 2020 and 2024 are leap years:

7 × 365 + 3 × 366 = 3653 days, and 3653 × 24 = 87 672 hours.

One header line and one line per hour: 87 672 + 1 = **87 673**.

</div>

<!--
**Live:** `(Get-Content data/raw/weather.csv).Count`, before the slide.
**Say:** the count agrees with the calendar, so no hour is missing and none is there twice. Rows can still be wrong, but there are as many as there should be.
**If asked:** the round brackets run the command first; `.Count` counts the lines it returned. `Get-Content data/raw/weather.csv | Measure-Object -Line` gives 87 673 as well.
(~3 min)
-->

---
hideInToc: true
---

# Lines and **Bytes**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> (Get-Item data/raw/weather.csv).Length
2515215
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| Line | Characters | Bytes, with the line break `0a` |
| --- | --- | --- |
| `time,temp_c,humidity_pct,wind_ms` | 32 | 33 |
| `2016-01-01T00:00,-4.4,93,2.5` | 28 | 29 |
| all 87 673 lines | | 2 515 215, on average 28.7 a line |

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 2: 87 673 lines, every hour of ten years, in 2 515 215 bytes.

</div>

<!--
**Say:** a line is its characters plus one byte for the line break. Colder hours such as `-11.3` take a character more, warm ones such as `9.2` one less: hence 28.7 on average.
**If asked:** the file arrived with LF line endings, and copying it to Windows does not change its bytes.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Pipes & **Filters**

Step 3: which rows are not measurements?

<!--
**Say:** small commands, each doing one thing, joined so that one's output is the next one's input.
(~1 min)
-->

---
hideInToc: true
---

# Output and Errors Are Two **Streams**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Get-Content data/raw/weather.csv -TotalCount 3 > results/first.txt
PS> (Get-Item results/first.txt).Length
91
PS> Get-Content data/raw/wether.csv > results/none.txt
Get-Content: Cannot find path '…/data/raw/wether.csv' because it does not exist.
PS> (Get-Item results/none.txt).Length
0
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📤 **Output stream**

What a command returns. `>` writes it into a file, and first **empties** that file. `>>` adds at the end.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚠️ **Error stream**

Errors go on their own stream and still reach the screen. `2>` writes them into a file.

</div>

</div>

<!--
**Say:** 91 bytes are the three lines: 33 + 29 + 29. The failed line made an empty file: `>` emptied it before anything came.
**If asked:** on Windows `>` ends each line with CRLF: 94 bytes. Never write into the file a command reads: `>` empties it first.
(~2 min)
-->

---
hideInToc: true
---

# Which Hour Is on Line **5000**?

<div class="card card-info card-glass pad-compact mt-sm">

🧮 Line 1 is the header, line 2 the hour 2016-01-01 00:00. Line 5000 is 5000 − 2 = **4998 hours** later.

4998 = 208 × 24 + 6: **208 days and 6 hours**.

2016 is a leap year. January to June: 31 + 29 + 31 + 30 + 31 + 30 = 182 days, so 1 July is 182 days after 1 January, and 208 − 182 = 26 days after 1 July is **27 July**.

</div>

<div class="card card-warning card-glass pad-compact mt-md">

Prediction: line 5000 is `2016-07-27T06:00`. A typed line can check it.

</div>

<!--
**Ask:** before the arithmetic: in which month will line 5000 fall? Collect two or three guesses.
**Say:** a prediction worked out by hand, then checked by a command: the way every number today is checked.
(~2 min)
-->

---
hideInToc: true
---

# Join Two Commands: the **Pipe**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Get-Content data/raw/weather.csv -TotalCount 5000 | Select-Object -Last 1
2016-07-27T06:00,18.2,71,1.1
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔗 **`A | B`**

The output stream of `A` becomes the input of `B`. No file stands between them.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧩 **A filter**

A command that reads a pipe and passes on part of it. Here: 5000 lines in, 1 out, line 5000.

</div>

</div>

<!--
**Live:** `Get-Content data/raw/weather.csv -TotalCount 5000 | Select-Object -Last 1`, before the slide.
**Say:** two commands, each simple, together answer a question neither answers alone: what is on line 5000. A pipe composes them, as `f(g(x))` composes functions.
**If asked:** a line that ends in `|` goes on in the next line; PowerShell shows `>>` there.
(~3 min)
-->

---
hideInToc: true
---

# Lines or **Objects**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📃 **`Get-Content`: lines of text**

```text
PS> Get-Content data/raw/weather.csv |
>> Select-Object -First 2
time,temp_c,humidity_pct,wind_ms
2016-01-01T00:00,-4.4,93,2.5
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧱 **`Import-Csv`: one object per row**

```text
PS> Import-Csv data/raw/weather.csv |
>> Select-Object -First 2 time, temp_c

time             temp_c
----             ------
2016-01-01T00:00 -4.4
2016-01-01T01:00 -4.8
```

</div>

</div>

<div class="note-text mt-md"><code>Import-Csv</code> reads line 1 as the names. Each later row becomes an object with four <strong>properties</strong>, picked by name: <code>$_.temp_c</code> is the temperature of the row at hand.</div>

<!--
**Say:** a PowerShell pipe carries objects. A line of text is one kind of object; a row with named values is another, and that is what makes columns easy.
**If asked:** zsh and bash pipes carry only text: there a column is picked by its number, `cut -d, -f2`.
(~2 min)
-->

---
hideInToc: true
---

# Sort as Text or as **Numbers**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Import-Csv data/raw/weather.csv | Sort-Object humidity_pct |
>> Select-Object -First 1 -ExpandProperty humidity_pct
100
PS> Import-Csv data/raw/weather.csv | Sort-Object {[int]$_.humidity_pct} |
>> Select-Object -First 1 -ExpandProperty humidity_pct
34
```

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The lowest humidity: 100 %? `Import-Csv` reads every value as text, and text is compared character by character: `1` comes before `3`. `[int]` turns each value into a number first: 34 %.

</div>

<!--
**Say:** the braces hold a small piece of code run for each row; `$_` is the row at hand. `[int]` is a whole number, `[double]` a number with a decimal point.
**Ask:** where would `9` stand in a text sort of 34, 9 and 100? Last.
(~2 min)
-->

---
hideInToc: true
---

# The Coldest **Hours**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Import-Csv data/raw/weather.csv | Sort-Object {[double]$_.temp_c} -Stable |
>> Select-Object -First 3

time             temp_c humidity_pct wind_ms
----             ------ ------------ -------
2019-07-22T00:00 -999   76           3.2
2019-07-22T01:00 -999   81           3.0
2019-07-22T02:00 -999   80           3.4
```

</div>

<div class="card card-warning card-glass pad-compact mt-md">

❓ The coldest hours of ten years: −999 °C, at midnight in July. Nothing is that cold: −273.15 °C is the lowest temperature there is. −999 is a mark the logger wrote for "no value".

</div>

<!--
**Live:** build the line one filter at a time: `Import-Csv data/raw/weather.csv | Select-Object -First 3`, then `↑` and add `Sort-Object {[double]$_.temp_c} -Stable |` before `Select-Object`.
**Say:** a sorted column shows its ends first, and a wrong value usually sits at an end. The other columns of those rows look normal: only the thermometer was down.
**If asked:** `-Stable` keeps rows of equal value in file order. The warmest hour, the last after sorting, is 2018-06-18 at 15:00, 32.4 °C.
(~4 min)
-->

---
hideInToc: true
---

# Keep Rows by a Condition: `Where-Object`

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> (Import-Csv data/raw/weather.csv |
>> Where-Object { [double]$_.temp_c -lt -273.15 }).Count
120
PS> (Import-Csv data/raw/weather.csv |
>> Where-Object { [double]$_.temp_c -lt -50 -or [double]$_.temp_c -gt 50 }).Count
120
```

</div>

<div class="card card-info card-glass pad-compact table-compact mt-md">

| `-lt` | `-gt` | `-eq` | `-or` | `-and` |
| --- | --- | --- | --- | --- |
| less than | greater than | equal | either | both |

</div>

<div class="note-text mt-md">Physics, without knowing the mark: below absolute zero, −273.15 °C, is impossible. 120 rows. A wider test, outside −50 to 50 °C for a station like this, finds the same 120 and no others.</div>

<!--
**Say:** `Where-Object` keeps each row for which the code in braces is true. A test by what is possible finds a mark that nobody told us about.
**If asked:** PowerShell writes comparisons as words, because `<` and `>` belong to the shell: `>` writes into a file.
(~2 min)
-->

---
hideInToc: true
---

# Find Rows with a Text: `Select-String`

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> (Select-String ',-999,' data/raw/weather.csv).Count
120
PS> Select-String ',-999,' data/raw/weather.csv |
>> Select-Object -First 1 -Last 1 LineNumber, Line

LineNumber Line
---------- ----
     31154 2019-07-22T00:00,-999,76,3.2
     31273 2019-07-26T23:00,-999,66,1.9
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 Lines 31 154 to 31 273: 31 273 − 31 154 + 1 = 120 lines, 22 to 26 July 2019, five days of 24 hours. One block, no gap.

</div>

<!--
**Say:** `Select-String` keeps the lines that contain a text. Each match is an object with its line number and its line.
**If asked:** keep the commas in `',-999,'`: they make sure the whole value is −999, and not part of a longer number.
(~2 min)
-->

---
hideInToc: true
---

# Rows per **Year**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

```text
PS> Import-Csv data/raw/weather.csv |
>> Group-Object {$_.time.Substring(0,4)} -NoElement

Count Name
----- ----
 8784 2016
 8760 2017
 8760 2018
 8760 2019
 8784 2020
…
 8760 2025
```

</div>

<div class="card card-info card-glass pad-compact">

🧮 365 × 24 = 8760 rows, 366 × 24 = 8784 in a leap year.

`Substring(0,4)` takes the first four characters of `time`: the year. `Group-Object` counts the rows of each year.

</div>

</div>

<div class="note-text mt-md">2019 has all its 8760 rows: the 120 hours are there, with −999 in place of a temperature.</div>

<!--
**Say:** the mark does not remove a row; it sits where the number should be. Every program that reads the column reads −999 as a number.
(~2 min)
-->

---
hideInToc: true
---

# Every Day Has 24 **Hours**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> $days = Import-Csv data/raw/weather.csv |
>> Group-Object { $_.time.Substring(0,10) } -NoElement
PS> $days.Count
3653
PS> ($days | Where-Object Count -ne 24).Count
0
PS> (Import-Csv data/raw/weather.csv | Group-Object time -NoElement |
>> Where-Object Count -gt 1).Count
0
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 3: 3653 days, none with more or fewer than 24 rows, no hour twice. The only rows that are not measurements are the 120 of −999, 22 to 26 July 2019.

</div>

<!--
**Say:** the count of step 2 could also come out right with one hour missing and another twice. Grouping by day and by hour rules that out.
**If asked:** `Where-Object Count -ne 24` is the short form of `Where-Object { $_.Count -ne 24 }`.
(~2 min)
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

# Below Freezing: a Fixed Text or a **Pattern**

<div class="note-text mt-sm">In how many hours was it below freezing?</div>

<div class="card card-primary card-glass pad-compact mt-sm">

```text
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

## ✳️ **A pattern**

A minus, digits, a point, one digit. Such a text is a **regular expression**, regex for short.

</div>

</div>

<!--
**Say:** the temperatures have one decimal, −999 has none. The pattern uses that difference.
**If asked:** `Select-String` reads every pattern as a regular expression; `-SimpleMatch` makes it read a fixed text.
(~2 min)
-->

---
hideInToc: true
---

# Quotes Keep a Pattern from the **Shell**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Select-String ,-999, data/raw/weather.csv
ParserError:
Line |
   1 |  Select-String ,-999, data/raw/weather.csv
     |                ~
     | Missing argument in parameter list.
PS> echo '$HOME' "$HOME"
$HOME
/Users/smilte
```

</div>

<div class="card card-info card-glass pad-compact table-compact mt-md">

| Signs the shell reads before the command runs | `,` `$` `\|` `>` `;` `(` `{` `#` `@` space |
| --- | --- |
| `'single quotes'` | pass every character on unchanged |
| `"double quotes"` | keep spaces, but replace `$name` by its value |

</div>

<!--
**Say:** this is step 3 of the shell: it replaces what it knows before the command starts. `,` makes a list in PowerShell, so the shell stopped at it. A pattern goes in single quotes, always.
**If asked:** `$HOME` is a variable: a name the shell keeps a value under, here the home folder.
(~2 min)
-->

---
hideInToc: true
---

# Signs for **One Character**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Sign | Fits | Pattern | In `2016-01-01T00:00,-4.4,93,2.5` | Lines of `weather.csv` |
| --- | --- | --- | --- | --- |
| a digit, a letter, `,` | itself | `,93,` | `,93,` | 1 530 |
| `.` | any one character | `T..:` | `T00:` | 87 672 |
| `[0-9]` | one character from `0` to `9` | `,[0-9][0-9],` | `,93,` | 85 132 |
| `[^,]` | one character that is **not** `,` | `,[^,][^,],` | `,93,` | 85 132 |
| `\.` | a point and nothing else | `[0-9]\.[0-9]` | `4.4` | 87 672 |

</div>

<div class="note-text mt-md">A backslash takes the special meaning away from the sign after it: <code>.</code> fits any character, <code>\.</code> only a point.</div>

<!--
**Ask:** why do 85 132 lines, not all 87 672, have a two-digit value between commas? Humidity of 100 has three digits: 87 672 − 85 132 = 2540 hours at 100 %.
(~2 min)
-->

---
hideInToc: true
---

# A Point Fits **Any Character**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> (Select-String '7.16' data/raw/weather.csv).Count
600
PS> Select-String '7.16' data/raw/weather.csv | Select-Object -First 2
data/raw/weather.csv:162:2016-01-07T16:00,-0.3,72,4.4
data/raw/weather.csv:402:2016-01-17T16:00,0.5,80,5.6
PS> (Select-String '7\.16' data/raw/weather.csv).Count
0
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 `7.16` fits `7T16`: days 7, 17 and 27 at 16:00, 3 × 12 × 10 = 360 lines. And `7-16`: every hour of 16 July, 24 × 10 = 240. 360 + 240 = 600. No hour was 7.16 °C itself, which a temperature with one decimal cannot be.

</div>

<!--
**Ask:** before the count: how many lines will `'7.16'` find? The room usually says none.
**Say:** a pattern that "works" can still find the wrong lines. The count is the check, and a look at two of the lines.
**If asked:** `-SimpleMatch` reads the pattern as a fixed text: 0 lines too.
(~2 min)
-->

---
hideInToc: true
---

# Signs for **How Many** and **Where**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Sign | Meaning | Pattern | In `2016-01-01T00:00,-4.4,93,2.5` | Lines |
| --- | --- | --- | --- | --- |
| `+` | one or more of what stands before | `[0-9]+` | `2016` | 87 672 |
| `*` | none or more | `,.*,` | `,-4.4,93,` | 87 673 |
| `?` | none or one | `,-?[0-9]` | `,-4` | 87 672 |
| `{4}` | exactly four | `^[0-9]{4}` | `2016` | 87 672 |
| `^` | the start of the line | `^2016` | `2016` | 8 784 |
| `$` | the end of the line | `\.5$` | `.5` | 8 265 |
| `( )`, `\|` | a group, and "or" | `T(00\|12):` | `T00:` | 7 306 |

</div>

<div class="note-text mt-md"><code>+</code>, <code>*</code>, <code>?</code> and <code>{4}</code> repeat the one thing before them. <code>^</code> and <code>$</code> fit no character: they pin the pattern to an end of the line.</div>

<!--
**Say:** `T(00|12):` fits midnight and noon: two hours a day, 2 × 3653 = 7306. `^2016` fits the 8784 hours of 2016.
**Ask:** `,.*,` fits 87 673 lines, the header too. Why? The header has commas as well.
(~2 min)
-->

---
hideInToc: true
---

# The Forms of the **Lines**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Get-Content data/raw/weather.csv | Group-Object { $_ -replace '[0-9]', '9' } -NoElement |
>> Sort-Object Count -Descending | Select-Object Count, Name

Count Name
----- ----
34547 9999-99-99T99:99,99.9,99,9.9
30355 9999-99-99T99:99,9.9,99,9.9
19709 9999-99-99T99:99,-9.9,99,9.9
 1897 9999-99-99T99:99,-9.9,999,9.9
…
  120 9999-99-99T99:99,-999,99,9.9
…
    1 time,temp_c,humidity_pct,wind_ms
```

</div>

<div class="note-text mt-md"><code>-replace '[0-9]', '9'</code> writes every digit as 9, so lines of one form become one text. 13 forms: 11 with a temperature of one decimal, the 120 rows of <code>-999</code>, and the header.</div>

<!--
**Say:** 87 673 lines read as 13. Every form but two has the temperature as digits, a point and one digit; that is the pattern of a measured row.
**If asked:** the forms differ by the number of digits: `99.9` a warm hour, `-9.9` a frost, `999` humidity of 100 %, `99.9` in the last column wind of 10 m/s or more.
(~2 min)
-->

---
hideInToc: true
---

# Build the Pattern of a **Measured Row**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Add | Pattern so far | Lines it fits |
| --- | --- | --- |
| a date, `T` | `^[0-9-]+T` | 87 672 |
| the hour, a comma | `^[0-9-]+T[0-9:]+,` | 87 672 |
| a temperature: a minus or none, digits, a point, one digit | `^[0-9-]+T[0-9:]+,-?[0-9]+\.[0-9],` | 87 552 |
| humidity, wind, the end | `^[0-9-]+T[0-9:]+,-?[0-9]+\.[0-9],[0-9]+,[0-9]+\.[0-9]$` | 87 552 |

</div>

<div class="card card-info card-glass pad-compact mt-md">

```text
PS> (Select-String '^[0-9-]+T[0-9:]+,-?[0-9]+\.[0-9],[0-9]+,[0-9]+\.[0-9]$' `
>> data/raw/weather.csv).Count
87552
```

</div>

<!--
**Say:** one piece at a time, each checked by its count. The count drops by 120 at the temperature, and the last two columns drop nothing.
**If asked:** the backtick at the end of a line continues it on the next line.
(~2 min)
-->

---
hideInToc: true
---

# The Lines the Pattern Does Not **Fit**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> $row = '^[0-9-]+T[0-9:]+,-?[0-9]+\.[0-9],[0-9]+,[0-9]+\.[0-9]$'
PS> (Select-String $row data/raw/weather.csv -NotMatch).Count
121
PS> Select-String $row data/raw/weather.csv -NotMatch | Select-Object -First 2
data/raw/weather.csv:1:time,temp_c,humidity_pct,wind_ms
data/raw/weather.csv:31154:2019-07-22T00:00,-999,76,3.2
PS> (Select-String '^2019-07-2[2-6]T' data/raw/weather.csv).Count
120
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 4: 121 = the header + the 120 rows of −999, which fill 22 to 26 July 2019. Every other row, 87 552, is a measurement. −999 is the only mark.

</div>

<!--
**Say:** `$row` keeps the pattern under a name, so it is typed once. `-NotMatch` keeps the lines that do not fit.
**Ask:** what would a count of 125 have told us? Four more rows of some other form, to be read one by one.
(~2 min)
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

```text
PS> Select-String ',-999,' data/raw/weather.csv -NotMatch -Raw > data/processed/weather_valid.csv
PS> (Get-Content data/processed/weather_valid.csv).Count
87553
PS> (Select-String ',-999,' data/processed/weather_valid.csv).Count
0
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ 87 673 − 120 = 87 553 lines, the header and 87 552 hours, and no −999 left. `data/raw` stays as it arrived: delete the new file, run the line again, and it is back.

</div>

<!--
**Say:** `-NotMatch` keeps the lines without the mark; `-Raw` passes on only the text of each line, without file name and line number.
(~2 min)
-->

---
hideInToc: true
---

# The Mean With and Without the **−999 Rows**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 📥 **`data/raw/weather.csv`**

```text
PS> Import-Csv data/raw/weather.csv |
>> Measure-Object temp_c -Average

Count             : 87672
Average           : 5.78279610365909
```

</div>

<div class="card card-success card-glass pad-compact">

## ⚙️ **`weather_valid.csv`**

```text
PS> Import-Csv data/processed/weather_valid.csv |
>> Measure-Object temp_c -Average

Count             : 87552
Average           : 7.15996550621346
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 The 87 552 measured hours sum to 626 869.3 °C: 626 869.3 / 87 552 = **7.16**. The marks add 120 × (−999) = −119 880, and the count grows by 120: (626 869.3 − 119 880) / 87 672 = **5.78**.

</div>

<!--
**Say:** five lost days, 0.14 % of the rows, moved a ten-year mean by 1.38 °C. A mark written as a number is counted as a number by every program. Step 5: 7.16 without the marks, 5.78 with them.
**If asked:** `Measure-Object` also prints empty `Sum`, `Maximum`, `Minimum` lines and the property name; they are left out here.
(~2 min)
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

# A Program Is a **Text File**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📜 **`scripts/column_stats.py`, lines 32–48**

```python
reader = csv.DictReader(handle)
...
values = [float(row[column]) for row in reader]
...
print("rows   ", len(values))
print("min    ", min(values))
print("max    ", max(values))
print("mean   ", f"{math.fsum(values) / len(values):.6g}")
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| Line | What it does |
| --- | --- |
| 32 | reads the file row by row, line 1 as the names, like `Import-Csv` |
| 37 | turns every value of the column into a number, −999 too |
| 48 | the sum divided by the count, to six digits |

</div>

<!--
**Say:** nobody has to write Python today, but anyone can read what it does: it counts every row, so it will give 5.78 on the raw file.
(~2 min)
-->

---
hideInToc: true
---

# Where a Command **Comes From**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> Get-Command Get-Content, pwsh, python | Select-Object CommandType, Name, Source

CommandType Name        Source
----------- ----        ------
     Cmdlet Get-Content Microsoft.PowerShell.Management
Application pwsh        /usr/local/bin/pwsh
Application python      /opt/homebrew/Caskroom/miniforge/base/bin/python
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧱 **Cmdlet**

Part of PowerShell, on every laptop that has it.

</div>

<div class="card card-accent card-glass pad-compact">

## 📦 **Application**

A program in a folder that its installer made. Without Python installed, `python` is not found.

</div>

</div>

<!--
**Say:** step 4 of the shell, finding the command: its own cmdlets first, then programs in folders.
**If asked:** on Windows the sources are `C:\Program Files\PowerShell\7\pwsh.exe` and `C:\Users\smilte\miniforge3\python.exe`.
(~2 min)
-->

---
hideInToc: true
---

# How the Shell Finds a Program: **PATH**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> $env:PATH -split [IO.Path]::PathSeparator
/opt/homebrew/Caskroom/miniforge/base/bin
/opt/homebrew/Caskroom/miniforge/base/condabin
/opt/homebrew/bin
/usr/local/bin
/usr/bin
/bin
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ➡️ **Searched top to bottom**

`PATH` is a variable that holds a list of folders. The shell takes the first folder with a program of the typed name: of two Pythons, the first runs.

</div>

<div class="card card-info card-glass pad-compact">

## 📦 **What an install changes**

The program lands in a folder, and the folder goes on `PATH`. A terminal reads `PATH` when it opens: a new install needs a new terminal.

</div>

</div>

<!--
**Say:** "not recognized as a name of a cmdlet … or executable program" means: in none of these folders.
**If asked:** `-split` cuts the text at `:` on macOS and `;` on Windows; `[IO.Path]::PathSeparator` is the right one on each. A real laptop lists ten to twenty folders.
(~2 min)
-->

---
hideInToc: true
---

# What a **Package** Is

<div class="card card-primary card-glass pad-compact mt-sm">

```text
(weather) PS> conda install numpy
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
| Find a name | `brew search powershell` | `winget search powershell` |
| Install | `brew install --cask powershell` | `winget install --id Microsoft.PowerShell` |
| Install Git | `brew install git` | `winget install --id Git.Git` |
| Install Miniforge | `brew install --cask miniforge` | `winget install --id CondaForge.Miniforge3` |
| What is installed | `brew list` | `winget list` |
| Newer versions | `brew upgrade` | `winget upgrade --all` |
| Remove | `brew uninstall git` | `winget uninstall --id Git.Git` |

</div>

<div class="card card-success card-glass pad-compact mt-md">

📜 A package manager looks the name up in its repository, fetches the package and its dependencies, and puts the program where the shell finds it. The line can go into a README: on the next laptop it installs the same program.

</div>

<!--
**Say:** the same jobs in every package manager, with other words. Both lines run in PowerShell 7 too. Miniforge brings Python and `conda`, a package manager for Python's packages.
**If asked:** a cask is a Homebrew package for an app with an installer. Linux has `apt` or `dnf`, with the same jobs.
(~2 min)
-->

---
hideInToc: true
---

# `conda`: Packages for Python, in **Environments**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
(base) PS> conda --version
conda 26.7.2
(base) PS> conda config --show channels
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
**If asked:** after installing Miniforge, `conda init powershell` is typed once, then a new terminal shows `(base)`. Miniforge is conda with conda-forge as its only channel, free to use.
(~2 min)
-->

---
hideInToc: true
---

# One Environment per **Project**

<div class="card card-warning card-glass pad-compact mt-sm">

💥 A script written for numpy 1.26, run where numpy 2.5 is installed:

```text
PS> python -c "import numpy as np; print(np.float_)"
AttributeError: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.
```

</div>

<div class="card card-primary card-glass pad-compact mt-md">

```text
(base) PS> conda create -n weather python=3.14
(base) PS> conda activate weather
(weather) PS> (Get-Command python).Source
/opt/homebrew/Caskroom/miniforge/base/envs/weather/bin/python
```

</div>

<div class="note-text mt-md">Every project run in one shared Python imports the same numpy, and an upgrade for one breaks another. An environment per project keeps each its own. Activation puts its folder first on <code>PATH</code>.</div>

<!--
**Say:** nothing in the old script changed; a package on the laptop did. `-n` names the environment, `python=3.14` asks for its Python.
**If asked:** on Windows the environment is `C:\Users\smilte\miniforge3\envs\weather`. It holds 24 packages, 221 MB. `conda deactivate` returns to `base`; `conda env remove -n weather` deletes the folder.
(~2 min)
-->

---
hideInToc: true
---

# Write the Environment Down: `environment.yml`

<div class="card card-primary card-glass pad-compact mt-sm">

```text
(weather) PS> conda env export --from-history > environment.yml
(weather) PS> Get-Content environment.yml
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

# Two Programs, One **Mean**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
(weather) PS> python scripts/column_stats.py data/processed/weather_valid.csv temp_c
file    data/processed/weather_valid.csv
column  temp_c
rows    87552
min     -16.3
max     32.4
mean    7.15997
```

</div>

<div class="card card-secondary card-glass pad-compact table-compact mt-md">

| File | `Measure-Object` | `column_stats.py` |
| --- | --- | --- |
| `data/raw/weather.csv` | 5.78279610365909 | 5.7828 |
| `data/processed/weather_valid.csv` | 7.15996550621346 | 7.15997 |

</div>

<div class="note-text mt-md">Step 6: two programs, written apart, agree to the sixth digit. The script's line: the program <code>python</code>, its file, then two words for the script.</div>

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
PS> python scripts/clean_export.py `
>> data/raw/daily_export.csv data/processed/daily.csv
9 rows written to data/processed/daily.csv
PS> (Get-Item data/processed/daily.csv).Length
148
```

</div>

</div>

<div class="note-text mt-md">The repair done by hand in the editor in Lecture 02, 180 bytes to 148, as one line that runs again on the next export.</div>

<!--
**Say:** header `date,temp_c` and LF: 12 bytes. Eight rows like `2025-10-01,6.3`: 15 each. `2025-10-06,10.4`: 16. 12 + 8 × 15 + 16 = 148.
**If asked:** the script states the line ending, `newline="\n"`, so it writes the same 148 bytes on every system.
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

```text
PS> (Get-FileHash data/raw/weather.csv).Hash
3F1AD06D3BB5773EAC79DFC964CDF8AF998689EF58AA8623F25D2050FBE00756
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
**Ask:** Smiltė's README names `3F1A…0756`. Read the first and the last four digits of yours: the same file.
(~2 min)
-->

---
hideInToc: true
---

# What a Checksum **Tells**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> $sent = '3F1AD06D3BB5773EAC79DFC964CDF8AF998689EF58AA8623F25D2050FBE00756'
PS> (Get-FileHash data/raw/weather.csv).Hash -eq $sent
True
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
**Say:** `-eq` compares two texts and ignores case, so the lower-case digits of another program match as well.
**If asked:** nobody has found two different files with the same SHA-256. A checksum sent by the same e-mail as a forged file proves nothing: it must come by another route.
(~2 min)
-->

---
hideInToc: true
---

# A List of Checksums for `data/raw`

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> (Get-FileHash data/raw/*).Hash > data/checksums.txt
PS> Compare-Object (Get-Content data/checksums.txt) (Get-FileHash data/raw/*).Hash
PS>
```

After `6,3` became `6,4` in row 1 of the export:

```text
PS> Compare-Object (Get-Content data/checksums.txt) (Get-FileHash data/raw/*).Hash

InputObject                                                      SideIndicator
-----------                                                      -------------
13FBCAE6A7A4D67EC30FDF3BEDC0B666209F7A4DC453EA72FF6DE7370FFD6AEE =>
9D849815D88ECEB18366EE66AC72F26B72E195BEA8BB20AA9A1474372513BBDB <=
```

</div>

<div class="note-text mt-md">The list is written once, when the raw files arrive. <code>Compare-Object</code> prints only what differs: nothing means the same bytes. <code>&lt;=</code> is the list, <code>=&gt;</code> the file now.</div>

<!--
**Live (optional):** write the list; in VS Code change `6,3` to `6,4` in `daily_export.csv` and save; compare again. Change it back and save before going on.
**Say:** "raw is never edited" becomes a test that runs in a second. The list stands in `data`, not in `data/raw`, so `data/raw/*` never includes it.
(~2 min)
-->

---
hideInToc: true
---

# The Same Rows, Other **Bytes**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| File | Made by | macOS | Windows |
| --- | --- | --- | --- |
| `data/raw/weather.csv` | the station | 2 515 215 B, `3F1AD06D…` | the same |
| `data/processed/weather_valid.csv` | `Select-String … >` | 2 511 735 B, `85B1F38D…` | 2 599 288 B, `B166C09B…` |
| `data/processed/daily.csv` | `clean_export.py` | 148 B, `33FE5E77…` | the same |

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 `>` ends each line as the system does: LF on macOS, CRLF on Windows, one byte `0d` more per line. 2 511 735 + 87 553 = 2 599 288. The script states LF, so it writes the same bytes on both.

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ Step 7: the raw files are named by checksum. A file made by `>` is named by its 87 553 lines and its mean.

</div>

<!--
**Say:** same rows, same mean, different bytes. A checksum in the README is only promised for a file whose bytes are the same everywhere.
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

# The README: the Mark and the **Result**

<div class="card card-primary card-glass pad-compact mt-sm">

## ✏️ **In `README.md`**

```md
## Columns of `weather.csv`

| Column | Meaning | Unit |
|--|--|--|
| `time` | start of the hour | ISO 8601 |
| `temp_c` | air temperature | °C |

Missing value: `temp_c` is `-999` in 120 rows, 2019-07-22 to 07-26.
`data/raw/weather.csv`: 87 673 lines, SHA-256 `3f1ad06d…fbe00756`.

## Result

Mean `temp_c`, 2016 to 2025: **7.16 °C**, over 87 552 hours.
The 120 hours marked `-999` are left out.
```

</div>

<!--
**Say:** every number here came out of a typed line today. The unit did not: the file cannot say °C, so the README must.
(~2 min)
-->

---
hideInToc: true
---

# The Rebuild Lines as a **Script**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📜 **`scripts/rebuild.ps1`**

```text
New-Item -ItemType Directory -Force data/processed, results | Out-Null
Select-String ',-999,' data/raw/weather.csv -NotMatch -Raw > data/processed/weather_valid.csv
python scripts/clean_export.py data/raw/daily_export.csv data/processed/daily.csv
python scripts/column_stats.py data/processed/weather_valid.csv temp_c > results/temp_c.txt
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

```text
PS> Remove-Item data/processed, results -Recurse
PS> ./scripts/rebuild.ps1
9 rows written to data/processed/daily.csv
PS> Get-Content results/temp_c.txt | Select-Object -Last 1
mean    7.15997
```

</div>

<!--
**Live:** in VS Code make `scripts/rebuild.ps1` from the four lines and save; then `Remove-Item data/processed, results -Recurse`, `./scripts/rebuild.ps1`, `Get-Content results/temp_c.txt`.
**Say:** the lines are the ones typed today, brought back with `↑` and pasted, never retyped: each one has already run. `./` names the script's folder, because `scripts` is not on `PATH`.
**If asked:** `-Force` makes `New-Item` quiet when the folder exists; `Out-Null` drops its output. A `.ps1` downloaded from the web is blocked on Windows until `Unblock-File`.
(~4 min)
-->

---
hideInToc: true
---

# The README: How to **Rebuild**

<div class="card card-primary card-glass pad-compact mt-sm">

## ✏️ **In `README.md`**

```md
## How to rebuild

In the project folder, in PowerShell 7 on macOS or Windows,
with Miniforge installed:

    conda env create -f environment.yml
    conda activate weather
    ./scripts/rebuild.ps1

The last line of `results/temp_c.txt` reads `mean    7.15997`.
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

♻️ The test of a README: someone with the folder and an empty laptop gets the same files and the same 7.16, and asks nobody.

</div>

<!--
**Say:** three lines: the tools, from `environment.yml`; the steps, from the script; the number to compare with.
**Ask:** what would the stranger still have to ask? Usually: where to get Miniforge. One more line names it.
(~2 min)
-->

---
hideInToc: true
---

# Every Program Ends with a **Number**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> python scripts/column_stats.py data/raw/weather.csv temp_c > results/raw.txt
PS> $LASTEXITCODE
0
PS> python scripts/column_stats.py data/raw/wether.csv temp_c
no file data/raw/wether.csv
PS> $LASTEXITCODE
1
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔢 **Exit status**

A program ends by handing the shell a number: 0 for success, anything else for a failure. `$LASTEXITCODE` holds the last one.

</div>

<div class="card card-info card-glass pad-compact">

## ✅ **`$?`**

`True` when the last command worked, `False` when not: for cmdlets and programs alike.

</div>

</div>

<!--
**Say:** the program chooses its numbers: `column_stats.py` returns 1 for a missing file, 2 for a wrong number of words. A script reads them to know whether a line worked.
(~2 min)
-->

---
hideInToc: true
---

# Stop at the First **Error**

<div class="grid-2 mt-sm gap-md">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **A typo in line 3: `daily_exprt.csv`**

```text
PS> ./scripts/rebuild.ps1
no file data/raw/daily_exprt.csv
PS> $?
True
```

The script runs line 4 anyway and reports success.

</div>

<div class="card card-success card-glass pad-compact">

## 🛑 **Two lines on top**

```text
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
```

```text
PS> ./scripts/rebuild.ps1
no file data/raw/daily_exprt.csv
NativeCommandExitException: …/rebuild.ps1:5
     | Program "python" ended with
     | non-zero exit code: 1 (0x01).
PS> $?
False
```

</div>

</div>

<!--
**Say:** a script that goes on after a failed line hides the failure. `'Stop'` stops at a failing cmdlet; the second line makes a program's non-zero exit status a failure too.
**If asked:** the second line exists since PowerShell 7.4. In zsh and bash, `set -e` does the same.
(~2 min)
-->

---
hideInToc: true
---

# The Same Result, Byte for **Byte**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
PS> (Get-FileHash results/temp_c.txt).Hash
ADE2805B90FE64A0053FA65E28329EEE616AD0389F9CA55DB86400B1C7A9A18B
PS> ./scripts/rebuild.ps1
9 rows written to data/processed/daily.csv
PS> (Get-FileHash results/temp_c.txt).Hash
ADE2805B90FE64A0053FA65E28329EEE616AD0389F9CA55DB86400B1C7A9A18B
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 Run twice on one laptop: the same 113 bytes. On Windows, `>` writes the six lines of `temp_c.txt` with CRLF: 113 + 6 = 119 bytes, another checksum, the same `mean    7.15997`.

</div>

<!--
**Say:** a check that runs again and gives the same bytes is a check anyone can repeat. Across systems, compare the line that matters, not the checksum of a file made by `>`.
(~2 min)
-->

---
hideInToc: true
---

# A Script Is a **Record**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Someone asks about 7.16 | The answer is in |
| --- | --- |
| Which file? | `data/raw/weather.csv`, SHA-256 in the README and in `data/checksums.txt` |
| Which rows were left out? | `rebuild.ps1`, line 4: every row with `,-999,` |
| Which program computed the mean? | `rebuild.ps1`, line 6: `column_stats.py`, line 48 |
| With which Python? | `environment.yml`: Python 3.14 from conda-forge |
| Is it still 7.16? | `./scripts/rebuild.ps1`, then `results/temp_c.txt` |

</div>

<div class="note-text mt-md">An e-mail says what came out. A script says what was done, in order, and runs again: on the next laptop, the next file, next year.</div>

<!--
**Say:** the README tells a reader; the script tells the computer. Both are text, both can be read, compared line by line and kept with the data.
**Ask:** Ben got 7.11 from the same file. Where would his script differ from Smiltė's?
(~2 min)
-->

---
hideInToc: true
---

# 7.16, **Checked**

<div class="card card-success card-glass pad-compact table-compact mt-sm">

| Step | Question about 7.16 | Answer |
| --- | --- | --- |
| 1 | Which column is the temperature? | `temp_c`, column 2 of 4 |
| 2 | Every hour of ten years? | 87 673 lines = 87 672 hours + header |
| 3 | Which rows are not measurements? | 120 rows of −999, 22 to 26 July 2019 |
| 4 | Is every other row a measurement? | 87 552 rows fit the pattern |
| 5 | The mean without them, and with? | 7.16 and 5.78 °C |
| 6 | A second program? | 7.15997, to the sixth digit |
| 7 | The file Smiltė used? | SHA-256 `3F1AD06D…FBE00756` |
| 8 | Can anyone run it again? | `./scripts/rebuild.ps1` |

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

✅ Install **PowerShell 7** on macOS and Windows, and say what the shell does with a line

</div>

<div class="card card-success card-glass pad-compact">

✅ Read and count a file, and join commands with the **pipe**, `>` and `2>`

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
  question="`Get-Content data/raw/wether.csv > results/out.txt` runs. The file name has a typo. What happens?"
  :options="[
    'Nothing is printed, and out.txt holds the error message',
    'The error is printed on the screen, and out.txt is an empty file',
    'The error is printed, and out.txt is not made',
    'PowerShell corrects the name and copies weather.csv'
  ]"
  :correct="1"
  explanation="The error goes to the error stream, which still reaches the screen; only the output stream is written by >. And > empties or makes its file before the command runs, so out.txt exists with 0 bytes. 2> would write the error into a file."
/>

---
hideInToc: true
---

<MCQ
  question="notes.txt has five lines. Then `'done' > notes.txt` and `'checked' >> notes.txt` run in PowerShell 7. How many bytes does the file have on a Mac and on Windows?"
  :options="[
    'More than 13 on both, because the five old lines are kept',
    '13 and 13',
    '15 and 13',
    '13 and 15'
  ]"
  :correct="3"
  explanation="A single > empties the file first, so the five lines are gone, and >> adds a second line. The letters are 4 + 7 = 11. On macOS each line ends with LF, one byte: 13 bytes. On Windows each line ends with CRLF, two bytes: 15 bytes."
/>

---
hideInToc: true
---

<MCQ
  question="`Import-Csv weather.csv | Sort-Object humidity_pct | Select-Object -First 1` shows a humidity of 100 as the lowest. Why?"
  :options="[
    'The station measured 100 % most often',
    'Import-Csv reads values as text, and text is compared character by character: 1 comes before 3',
    'Sort-Object sorts from the largest down',
    'Select-Object -First 1 takes the last row'
  ]"
  :correct="1"
  explanation="Every value from Import-Csv is text. 100 starts with 1, 34 with 3, so 100 comes first. Sort-Object {[int]$_.humidity_pct} turns each value into a number before comparing and puts 34 first."
/>

---
hideInToc: true
---

<MCQ
  question="`Select-String ,-999, data/raw/weather.csv` stops with a ParserError. Why?"
  :options="[
    'Select-String cannot search for a minus sign',
    'The shell reads the comma itself, as the start of a list, before Select-String runs',
    'The file has no line with -999',
    'A pattern must be written in double quotes'
  ]"
  :correct="1"
  explanation="The shell reads a line before the command runs, and some signs mean something to it: in PowerShell a comma builds a list. In single quotes, ',-999,', every character reaches Select-String unchanged. Double quotes would work here too, but they replace a $name, so a pattern goes in single quotes."
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
  explanation="The pattern fits a whole line of digits and minus signs, a comma, a number, a point and one digit. The header has letters. The line with semicolons has a semicolon where the pattern allows only digits and minus signs, and no point. Select-String and the Find box of VS Code find the same two lines."
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
  question="Two folders on PATH hold a program named python: C:\Python312 is listed before C:\Python314. What does `python --version` print?"
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
  question="weather_valid.csv, made with `>` from the same raw file, has 2 511 735 bytes on a Mac and 2 599 288 on Windows. What follows?"
  :options="[
    'One of the two lost rows',
    'The same 87 553 lines, with LF on the Mac and CRLF on Windows: the checksums differ, the mean does not',
    'The same bytes, because Get-FileHash ignores line endings',
    'The Windows file holds the −999 rows'
  ]"
  :correct="1"
  explanation="2 599 288 − 2 511 735 = 87 553, one byte per line: the 0d of CRLF, which > writes on Windows. The rows and the mean are the same, the bytes and so the checksums are not. The README names such a file by its lines and its mean, and names by checksum only files whose bytes are the same everywhere."
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
  question="rebuild.ps1 has no stop lines. Its line 3 runs python and fails; line 4 works. What does `$?` print after the script?"
  :options="[
    'False, because line 3 failed',
    'True, because the script ran on and its last line worked',
    'Nothing: PowerShell asks first whether to go on',
    'Two values, one for each line'
  ]"
  :correct="1"
  explanation="Without the stop lines a script runs every line, and the failure of line 3 only shows as its message. The last line worked, so $? is True. With $ErrorActionPreference = 'Stop' and $PSNativeCommandUseErrorActionPreference = $true the script stops at line 3 and $? is False."
/>
