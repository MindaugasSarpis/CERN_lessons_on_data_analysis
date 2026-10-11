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
up. Every command slide has two columns, macOS zsh and Windows PowerShell 7:
type the column of your own laptop, and read the other one aloud so that
both halves of the room hear their line. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# The main goal of this lecture is to work on files with **typed commands**: a step that was typed can be written down, checked and run again

<!--
Speaker: "typed" is the word that matters. A click leaves nothing behind; a
typed line can be pasted into a README, read by someone else and run again on
the next file. (~1 min)
-->

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🧭 Read the **prompt** of macOS `zsh` and of PowerShell 7, and name a file by its **path**

</div>

<div class="card card-secondary card-glass pad-compact">

📁 Read, count, make, copy, move and delete files with commands in both shells, and name many files with one **wildcard**

</div>

<div class="card card-accent card-glass pad-compact">

🔗 Count, search and sort a file of 91 583 rows, and join commands with **pipes** and `>`

</div>

<div class="card card-info card-glass pad-compact">

🔎 Describe text with a **regular expression**, in the Find box of VS Code and in the shell

</div>

<div class="card card-success card-glass pad-compact">

⚙️ Run a Python **script** that someone else wrote, install a program and a **package** by a typed line, and give a project its own **environment**

</div>

<div class="card card-warning card-glass pad-compact">

🛡️ Show with a **checksum** that two files hold the same bytes, keep **backups** by the 3-2-1 rule, and complete the **README**

</div>

</div>

<!--
Speaker: one line per section. The thread through all seven is the pendulum
table of Lecture 2: cleaned by hand on the projector then, cleaned by a typed
line today, and checked byte for byte at the end. (~1 min)
-->

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

The README lists the four edits Lecture 2 made in VS Code, in words. To clean the next file, someone reads the list and makes every edit again.

</div>

<div class="card card-primary card-glass pad-compact">

## ⌨️ **The same four edits, typed**

`scripts/clean_pendulum.py` is handed out with this lecture. It makes the four edits, and one typed line runs it. The line is the record of what was done, and it runs again on the next file.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

```text
% python3 scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv
9 rows written to data/processed/pendulum_script.csv
PS> python scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv
9 rows written to data/processed/pendulum_script.csv
```

Two lines, one per system. macOS names the program `python3`, Windows `python`. The three paths after it are the same.

</div>

<!--
Speaker: open the README and read the line "Cleaned copy" aloud. Then run the
typed line once, without explaining it: nine rows, the table of Lecture 2.
The script is not opened now; it is run like any other command, and the
section on programs opens it later. A laptop without Python answers
"Python was not found" to this line; the section Tools & Environments says
why, and installs it. (~2 min)
-->

---
hideInToc: true
---

# One Table, **Four Copies**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 👀 **What VS Code shows, in all four**

```text
length_cm,t10_s
20,9.02
30,11.05
…
100,20.01
```

Ten lines, the same characters in each file.

</div>

<div class="card card-warning card-glass pad-compact table-compact">

## 📏 **What the file manager shows**

| Copy | Size |
| --- | --- |
| A | 97 bytes |
| B | 96 bytes |
| C | 107 bytes |
| D | 105 bytes |

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

❓ Four copies of the cleaned table, saved on different laptops. The README says `Cleaned copy: data/processed/pendulum.csv` and lists the four edits, and all four copies fit those words. Which copy does it mean? The answer has to be something that can be written into the README and checked by anyone.

</div>

<!--
Speaker: the four files were made for this slide from the cleaned table: with
LF line breaks (97 bytes), the same without the last line break (96), with
CRLF (107), with CRLF and no last line break (105). Do not explain the sizes
now. Ask the room to guess why four copies of the same ten lines differ, and
leave the question on the board. Each size gets its reason during the
lecture, and the README gets its answer on the last slide before the Recap.
(~2 min)
-->

---
hideInToc: true
---

# Three Questions, **Clicked and Typed**

<div class="note-text mt-sm">Three questions about <code>data/raw/D0_KPi.csv</code>, asked in the project folder.</div>

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Question | VS Code | Typed: macOS zsh `%`, PowerShell `PS>` | Answer |
| --- | --- | --- | --- |
| How many lines? | `Ctrl+End` | `% wc -l data/raw/D0_KPi.csv`<br>`PS> (Get-Content data/raw/D0_KPi.csv).Count` | 91 584 |
| What is on line 5000? | `Ctrl+G` `5000` | `% head -n 5000 data/raw/D0_KPi.csv \| tail -n 1`<br>`PS> (Get-Content data/raw/D0_KPi.csv)[4999]` | `1868.8636,…` |
| How many rows have `-100`? | `Ctrl+F` `-100` | `% grep -c ',-100' data/raw/D0_KPi.csv`<br>`PS> (Select-String ',-100' data/raw/D0_KPi.csv).Count` | 49 |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🖱️ **What a click leaves**

The answer on the screen. The steps stay in the memory of whoever clicked, and they are done again by hand for the next file.

</div>

<div class="card card-success card-glass pad-compact">

## ⌨️ **What a typed line leaves**

The line itself. It goes into the README or into a script. The two shells use different words for the same question, and they print the same three answers.

</div>

</div>

<!--
Speaker: show the three answers in VS Code first, on the projector: VS Code
numbers 91 585 lines, the last one empty, so the file has 91 584; line 5000
begins with 1868.8636; 49 rows carry -100 in TAU. On a Mac the VS Code keys are
Cmd+↓, Ctrl+G and Cmd+F. The typed lines find nothing new.
The point is the column "Typed": each answer now has a line that can be
kept, one for each shell. Point out [4999]: PowerShell counts the lines
from 0, so line 5000 is number 4999. Every word of these lines is explained in the next hour. (~3 min)
-->

---
layout: section
hideInToc: true
---

# The **Shell**

A typed line can be kept. This section names the window where it is typed, the program that reads it, and the parts of the line.

<!--
Speaker: where commands are typed, what reads them, and how a file is named in
a command. Nothing is assumed: the terminal, the shell and the prompt are
named here before they are used. (~1 min)
-->

---
hideInToc: true
---

# Open the **Terminal**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

- In VS Code, **Terminal** > **New Terminal**. The Panel opens at the bottom, in the project folder
- The name at the top right of the Panel reads `zsh`. There is nothing to set

```text
% echo $ZSH_VERSION
5.9
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

- In VS Code, **Terminal** > **New Terminal**, the same menu
- The name at the top right of the Panel reads `powershell` or `pwsh`. The version line tells which

```text
PS> $PSVersionTable.PSVersion.Major
7
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔧 Windows has two PowerShells. **Windows PowerShell 5.1** is built in and answers `5`. **PowerShell 7** answers `7`, and it runs on macOS and Linux as well; the section Tools & Environments installs it with one typed line. Every Windows command on these slides is for PowerShell 7.

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

🪟 A terminal that answers `5` runs Windows PowerShell 5.1. Most lines of the PowerShell column work there too, and the slides say where 5.1 differs.

</div>

<!--
Speaker: open a terminal on the projector and type the version line. Ask the
room: who sees zsh, who sees powershell (5.1), who already has pwsh. A laptop
that answers 5 follows the PowerShell column; where 5.1 gives another answer
than 7, the slide says so. (~3 min)
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

The program that reads the line: `zsh` or PowerShell. It finds what the first word names, runs it, and shows the prompt again.

</div>

<div class="card card-accent card-glass pad-compact">

## ⚙️ **Program**

Does one job and prints text. In zsh most commands are program files. PowerShell has **cmdlets**, named Verb-Noun.

</div>

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% which ls cat cd
/bin/ls
/bin/cat
cd: shell built-in command
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Alias ls, cat, cd |
>> Select-Object Name, Definition

Name Definition
---- ----------
ls   Get-ChildItem
cat  Get-Content
cd   Set-Location
```

</div>

</div>

<!--
Speaker: the same word, two different things. On the Mac, ls is a file on the
disk. In PowerShell it is a short alias for the cmdlet Get-ChildItem, so the
same word works in both shells. A name with no alias does not
cross over: wc is a program of macOS, and PowerShell answers "The term 'wc' is
not recognized". The | is explained in the pipes section; here it picks two
columns. (~3 min)
-->

---
hideInToc: true
---

# Read the **Prompt**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Shell | The prompt, as it first appears | The folder it shows |
| --- | --- | --- |
| Windows PowerShell 5.1, built in | `PS C:\Users\ada\Documents\analysis-project>` | The whole path |
| PowerShell 7 | `PS C:\Users\ada\Documents\analysis-project>` | The same, letter for letter |
| macOS, `zsh` | `ada@MacBook-Air analysis-project %` | The last folder only |
| Python, started by `python3` or `python` | `>>>` | None. `exit()` gives the shell back |

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 👤 **Who and where**

zsh prints the user and the computer, `ada@MacBook-Air`. PowerShell prints `PS` and no name, so only the version line tells 5.1 from 7.

</div>

<div class="card card-accent card-glass pad-compact">

## 📂 **The working directory**

The folder the shell is in: the one `pwd` prints and `cd` changes. `~` is the home folder, `/Users/ada` or `C:\Users\ada`.

</div>

<div class="card card-info card-glass pad-compact">

## ⏳ **The mark**

`%` or `>` ends the prompt: the shell waits. Nobody types it. On these slides `%` is zsh and `PS>` is PowerShell.

</div>

</div>

<!--
Speaker: ask the room to read their own prompt aloud, part by part. The two
PowerShells print the same
prompt, which is why the first slide of this section checked the version. The folder in the
prompt is the working directory, and every relative path of the next slides
starts there. (~3 min)
-->

---
hideInToc: true
---

# The Parts of a **Command**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% head -n 2 data/raw/D0_KPi.csv
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Content -Head 2 data/raw/D0_KPi.csv
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
```

</div>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ⚙️ **Program**

The first word: `head` or `Get-Content`. The shell finds it and starts it.

</div>

<div class="card card-accent card-glass pad-compact">

## 🎚️ **Option**

`-n 2`, `-Head 2`: how to work, with a value. `-n` is not `-N`. PowerShell ignores case: `-head` works too.

</div>

<div class="card card-info card-glass pad-compact">

## 📄 **Argument**

`data/raw/D0_KPi.csv`: what to work on. The same path in both shells.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ A space ends an argument. `head -n 2 Pendulum Run 2.csv` names three files. `Get-Content` refuses the whole line: `A positional parameter cannot be found that accepts argument 'Run'`. This is the rule of Lecture 2: no spaces in names. Quotes hold a name together in both shells: `"Pendulum Run 2.csv"`.

</div>

<!--
Speaker: type both lines. The answer is the same two lines, letter for letter the
header and the first row that VS Code shows. In PowerShell an option is
called a parameter; the idea is the same. (~3 min)
-->

---
hideInToc: true
---

# Absolute **Paths**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌳 **Folders form a tree**

```text
/                 C:\ on Windows
└─ Users
   └─ ada
      └─ Documents
         └─ analysis-project
            └─ data
               └─ raw
                  └─ D0_KPi.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📍 **`pwd`, the same word in both shells**

```text
% pwd
/Users/ada/Documents/analysis-project
PS> pwd

Path
----
C:\Users\ada\Documents\analysis-project
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

An absolute path lists the folders from the top of the tree down to the file. On macOS the top is `/`, on Windows it is the drive `C:\`. `pwd` prints the working directory in this form: in PowerShell it is an alias of `Get-Location`.

</div>

<!--
Speaker: run pwd and read the answer from left to right as a walk down the
tree. Three laptops in the room give three different answers: the user name
differs. (~2 min)
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

- A relative path starts at the working directory. It does not start with `/` or `C:\`
- `.` is that folder, `..` the one above it. `cd ..` goes up one level, `cd ../..` two
- `~` is the home folder. `cd` alone goes there
- All of it works in both shells. PowerShell also takes `\`

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

♻️ The rule: the terminal stays in the project folder, and every command, every script and the README use paths that start there. Then the project runs on any laptop, in any shell and in any place on its disk. A path that begins with `/Users/ada` or `C:\Users\ada` exists on one computer.

</div>

<!--
Speaker: cd into scripts and run ls ../data/raw, then cd .. to come back, in
both shells: the same lines. From here on the terminal does not leave the
project folder. (~2 min)
-->

---
hideInToc: true
---

# Keys That **Save Typing**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Key | 🍎 zsh | 🪟 PowerShell |
| --- | --- | --- |
| `Tab` | `cd da` becomes `cd data/` | `cd da` becomes `cd .\data` |
| `Tab` again | Lists the names that fit, if there are several | The next name that fits. `Ctrl+Space` lists them all |
| `↑` `↓` | Earlier commands, one at a time | The same |
| `Ctrl+R` | Searches the earlier commands | The same |
| Start, end of line | `Ctrl+A`, `Ctrl+E` | `Home`, `End`. `Ctrl+A` selects the whole line |
| `Ctrl+C` | Stops the program that is running | The same. With text selected, it copies |
| `Ctrl+L` | Empties the Panel, like `clear`. Nothing is deleted | The same |

</div>

<div class="card card-info card-glass pad-compact mt-md">

A name completed by `Tab` has no typing mistake in it. If `Tab` adds nothing, no name fits what was typed so far: the path is wrong before it is run. PowerShell writes a completed path its own way, `.\data\raw\D0_KPi.csv`, and reads `/` just as well.

</div>

<!--
Speaker: type head -n 2 da, Tab, r, Tab, D, Tab, and let the room count the
keys for the path: seven instead of nineteen. Then the same in PowerShell with
Get-Content -Head 2: a folder completes without the slash, so / is typed
before r and before D, nine keys. PowerShell 7 may also show a guess in grey after the
cursor, taken from earlier commands: the right arrow accepts it. The mouse
does not move the cursor inside the line; the arrow keys do. (~2 min)
-->

---
hideInToc: true
---

# A Command That **Fails**

<div class="card card-warning card-glass pad-compact mt-sm">

## ❓ **No program of that name**

```text
% pyhton scripts/clean_pendulum.py
zsh: command not found: pyhton
PS> pyhton scripts/clean_pendulum.py
pyhton: The term 'pyhton' is not recognized as a name of a cmdlet,
function, script file, or executable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
% python scripts/clean_pendulum.py
zsh: command not found: python
PS> python scripts/clean_pendulum.py
Python was not found; run without arguments to install from the Microsoft Store,
or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

✅ The shell searched the folders listed in `PATH` and found no program of that name. The last message comes from a stand-in `python.exe` that Windows puts on `PATH`. On macOS the program is `python3`. On Windows the message stays until Python is installed with **Add python.exe to PATH** ticked.

</div>

<!--
Speaker: make the typo live in both shells and let the room read each message
aloud before you explain it. The word before the first colon names who
complains: zsh itself, or, in PowerShell, the word it could not find. The
python case is what every Windows laptop without Python answers today;
the Store message has no name before it because it is not PowerShell
speaking. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Files & **Folders**

A command is a program, its options and its arguments, and a path names the file it works on. The first commands work on whole files: read, count, copy, delete.

<!--
Speaker: the last section moved between folders. This section works on the files in
them: read, count, make, copy, move, delete, many at once. Every command slide has
macOS on the left and PowerShell on the right, run in the same project folder.
(~1 min)
-->

---
hideInToc: true
---

# Read a File: `head`, `tail`, `Get-Content`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% head -n 3 data/raw/D0_KPi.csv
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
1860.6599,2803.4126,0.0001864154,0.34182164
% tail -n 2 data/raw/D0_KPi.csv
1871.4323,2541.8845,0.0001756544,6.866581
1911.2631,2543.4617,0.00017650973,8.169813
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Content data/raw/D0_KPi.csv -Head 3
M,PT,TAU,IPCHI2
1880.649,3000.9534,0.00041271152,1299.1675
1860.6599,2803.4126,0.0001864154,0.34182164
PS> Get-Content data/raw/D0_KPi.csv -Tail 2
1871.4323,2541.8845,0.0001756544,6.866581
1911.2631,2543.4617,0.00017650973,8.169813
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The same five lines in both shells. `-Head 3` is short for `-TotalCount 3`, and it stops reading after line 3: on a Windows laptop that takes about 10 ms, reading all 91 584 lines 0.3 to 0.5 s.

</div>

<div class="note-text mt-sm"><code>cat FILE</code> prints a whole file in both shells: in PowerShell <code>cat</code> is another name for <code>Get-Content</code>. <code>Ctrl+C</code> stops it. <code>less FILE</code> (macOS) and <code>Get-Content FILE | more</code> show one screen at a time: <code>Space</code> goes on, <code>q</code> leaves.</div>

<!--
Speaker: run cat on D0_KPi.csv once in each shell and stop it with Ctrl+C.
Then the head line: the first lines appear at once, because the program reads
only as far as it prints. Measured on the lecturer's Windows laptop with
Measure-Command: -Head 3 takes 1-17 ms, (Get-Content ...).Count 340-550 ms.
(~2 min)
-->

---
hideInToc: true
---

# Count: `wc` and `Measure-Object`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc data/processed/pendulum.csv
      10      10      97 data/processed/pendulum.csv
% wc -l data/raw/D0_KPi.csv
   91584 data/raw/D0_KPi.csv
```

`wc` prints lines, words and **bytes**. `-l`, `-w` and `-c` print one of them.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Content data/processed/pendulum.csv |
>> Measure-Object -Line -Word -Character
Lines Words Characters Property
----- ----- ---------- --------
   10    10         87
PS> (Get-Item data/processed/pendulum.csv).Length
97
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🔢 **87 characters, 97 bytes.** `Get-Content` passes the file on line by line and drops the line breaks: 10 lines, 10 bytes `0A`. Characters are not bytes: the size on disk is the file's `Length`, the 97 bytes of Lecture 3. On the large file, `(Get-Content data/raw/D0_KPi.csv).Count` gives 91 584, as `wc -l` does.

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ `wc -l` counts the bytes `0A`. Copy B of the opening, 96 bytes, holds the same ten lines with no `0A` after the last one: `Measure-Object` counts 10 lines, `wc -l` counts 9. One byte more, 96 + 1 = 97, is copy A.

</div>

<!--
Speaker: wc stands for word count. Read the three numbers of the small file:
10 lines, 10 words because no line has a space in it, 97 bytes. PowerShell
says 87 for the same file, and the 10 missing are the 10 line breaks.
Get-Content data/processed/pendulum.csv -Raw | Measure-Object -Character keeps
them and prints 97. Copy B can be made live on the Mac: head -c 96 keeps the first 96 bytes of
data/processed/pendulum.csv; sent into results/copy_b.csv, wc -l gives 9.
(~3 min)
-->

---
hideInToc: true
---

# Make, Copy, Move: `mkdir`, `cp`, `mv`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% mkdir backup
% cp data/raw/pendulum.csv backup
% cp -r data backup
% mv backup/pendulum.csv backup/raw.csv
% ls backup
data    raw.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> mkdir backup
PS> cp data/raw/pendulum.csv backup
PS> cp -r data backup
PS> mv backup/pendulum.csv backup/raw.csv
PS> ls backup -Name
data
raw.csv
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The same words in both shells. In PowerShell `cp`, `mv` and `ls` are short names (**aliases**): `cp` stands for `Copy-Item`, `mv` for `Move-Item`, `ls` for `Get-ChildItem`. PowerShell also takes the start of a parameter name, so `-r` means `-Recurse`.

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Same word, other program. Without `-r`, macOS refuses a folder: `cp: data is a directory (not copied).` PowerShell's `cp data backup2` makes an empty folder `backup2` and says nothing. `cp` replaces a file of the target name without asking, in both shells; PowerShell's `mv` refuses: `Cannot create a file when that file already exists.`

</div>

<!--
Speaker: watch the folder appear in the Side Bar while you type. PowerShell's
mkdir answers with a short table that shows the new folder; zsh prints
nothing. (Get-Alias cp).Definition prints Copy-Item; mkdir is not an alias
but a small PowerShell function that calls New-Item. (~3 min)
-->

---
hideInToc: true
---

# Delete: `rm` and `Remove-Item`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% rm backup/raw.csv
% rmdir backup
rmdir: backup: Directory not empty
% rm -r backup
% ls backup
ls: backup: No such file or directory
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> rm backup/raw.csv
PS> rm -r backup
PS> Test-Path backup
False
```

`rm` is `Remove-Item`, and `-r` is `-Recurse`: the folder and all in it.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ `rmdir` is where the shells differ. On macOS it refuses a folder that is not empty. In PowerShell `rmdir` is `Remove-Item` as well, and it asks: `The item at ... has children and the Recurse parameter was not specified. ... (default is "Y"):`. `Enter` alone answers Yes and deletes it all.

</div>

<div class="card card-info card-glass pad-compact mt-sm">

No Recycle Bin, no Trash, and `Ctrl+Z` takes nothing back. Before `rm`: `pwd`, then `ls` with the same path. The `rm -rf` of many web pages fails in PowerShell: `A parameter cannot be found that matches parameter name 'rf'.`

</div>

<!--
Speaker: say the folder name aloud before pressing Enter. What rm can take
away for good is a file in data/raw, a script or the README; a file in
data/processed or results can be made again. (~3 min)
-->

---
hideInToc: true
---

# Many Files at Once: **Wildcards**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -c data/*/*.csv
      97 data/processed/pendulum.csv
 3926142 data/raw/D0_KPi.csv
     130 data/raw/pendulum.csv
 3926369 total
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Item data/*/*.csv |
>> Select-Object Name, Length
Name          Length
----          ------
pendulum.csv      97
D0_KPi.csv   3926142
pendulum.csv     130
```

</div>

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

<!--
Speaker: the three signs mean the same in both shells. data/*/*.csv: any
folder in data, then any name that ends in .csv. 97 bytes is the cleaned table
of the Count slide; the raw table has 130, the LHCb file 3 926 142. (~2 min)
-->

---
hideInToc: true
---

# Who Reads the `*`?

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% echo data/raw/*.csv
data/raw/D0_KPi.csv data/raw/pendulum.csv
```

zsh replaces the pattern by the names that fit, **before** the program starts. `echo` gets two names.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> echo data/raw/*.csv
data/raw/*.csv
```

PowerShell hands the pattern on as it is. Its own commands, `ls` and `Get-Item` among them, replace it **themselves**.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

```text
% python3 scripts/clean_pendulum.py data/raw/p*.csv data/processed/pendulum_script.csv
9 rows written to data/processed/pendulum_script.csv
PS> python scripts/clean_pendulum.py data/raw/p*.csv data/processed/pendulum_script.csv
Traceback (most recent call last):
...
OSError: [Errno 22] Invalid argument: 'data/raw/p*.csv'
```

⚠️ The line of the cleaning, with a `*` in it. In PowerShell, Python gets the `*` itself and finds no file of that name. Give a script the whole name: `Tab` completes it.

</div>

<!--
Speaker: echo prints its arguments, so echo PATTERN shows what a program
receives. In zsh, run it before rm PATTERN. A pattern that fits nothing is an
error in zsh (zsh: no matches found: *.txt); PowerShell passes it on silently.
The demo is the cleaning line of the start of the lecture with p* typed for
pendulum: zsh hands Python the full name, PowerShell the star. (~2 min)
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

- The prompt shows `analysis-project`: the terminal stays there
- Commands **read** from `data/raw`. No command writes there
- What a command makes goes to `data/processed` or to `results`
- Commands worth keeping go into `scripts`
- A name without spaces is one argument, in both shells

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The layout answers one question for every file: can it be made again? Files in `data/processed` and `results` can, by a command. Files in `data/raw` and `scripts` cannot, and those are the ones `rm` takes away for good.

</div>

<!--
Speaker: nothing new on this slide. It fixes where the commands of the next
sections read and where they write, in either shell. (~1 min)
-->

---
layout: section
hideInToc: true
---

# Pipes & **Filters**

Each command so far read a file and printed its answer to the terminal. That answer can also go into a file, or into the next command.

<!--
Speaker: the centre of the lecture. Small programs that each do one thing,
joined so that the output of one is the input of the next. Every slide shows
the same step in zsh and in PowerShell; the ideas are the same, the words
differ. (~1 min)
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
PS> Get-Content results/note.txt
made on 2026-10-13
by ada
PS> (Get-Item results/note.txt).Length
28
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A program prints to its **standard output**, normally the terminal. `> FILE` sends that output into a file: `>` makes the file, or **empties** it if it exists, and `>>` adds at its end. The two shells agree on the signs and on the text. They do not agree on the size: 26 bytes against 28.

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ The file after `>` is emptied before the command reads anything. `sort results/note.txt > results/note.txt` leaves 0 bytes, and so does `Get-Content results/note.txt | Sort-Object > results/note.txt`. A command never writes into the file it reads.

</div>

<!--
Speaker: type the three lines in both shells, side by side. echo is
PowerShell's short name for Write-Output. Ask the room to guess why the
sizes differ before the next slide. Then run the sort line and show the
empty file. (~2 min)
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
0000001a
PS> Format-Hex results/note.txt
   Label: C:\Users\ada\Documents\analysis-project\results\note.txt
          Offset Bytes                                           Ascii
                 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
          ------ ----------------------------------------------- -----
0000000000000000 6D 61 64 65 20 6F 6E 20 32 30 32 36 2D 31 30 2D made on 2026-10-
0000000000000010 31 33 0D 0A 62 79 20 61 64 61 0D 0A             13��by ada��
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-info card-glass pad-compact">

## 🔢 **Count them**

`made on 2026-10-13` has 18 characters, `by ada` 6. The Mac ends each line with `0a` (LF): 24 + 2 = 26. Windows ends each with `0D 0A` (CRLF): 24 + 4 = 28. Copies C and D of the opening: 97 + 10 = 107, 96 + 9 = 105.

</div>

<div class="card card-warning card-glass pad-compact">

## 🪟 **Which PowerShell**

PowerShell 7 writes UTF-8 without a BOM: the first byte is `6D`, the `m`. Windows PowerShell 5.1 writes UTF-16: 58 bytes. `$PSVersionTable.PSVersion` tells them apart.

</div>

</div>

<!--
Speaker: the line endings and encodings of Lecture 3, now made by a command
and measured. Point at 0a and at 0D 0A. Format-Hex prints the bytes it cannot
show as a character as a replacement sign. UTF-16 in 5.1: a 2-byte BOM and 2
bytes for each of the 28 characters, 2 + 56 = 58. (~3 min)
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
    F["D0_KPi.csv"]:::input --> A["the first 5000 lines"]
    A -->|"5000 lines"| B["the last of them"]
    B -->|"1 line"| T["terminal"]:::output

    classDef input fill:#0b2a4a,stroke:#5eead4,color:#e8f1ff
    classDef output fill:#063c34,stroke:#34d399,color:#d1fae5
```

</div>

<div class="grid-2 gap-md mt-sm">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% head -n 5000 data/raw/D0_KPi.csv | tail -n 1
1868.8636,5537.248,0.0007151779,10.399748
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-Content data/raw/D0_KPi.csv -Head 5000 |
    Select-Object -Last 1
1868.8636,5537.248,0.0007151779,10.399748
```

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-sm">

A program that takes input and passes output on is a **filter**. Given no file name, it reads what the pipe hands to it. A line that ends in `|` goes on in the next line.

</div>

<!--
Speaker: line 5000 is the line that Ctrl+G found in VS Code. Same pipe sign,
same line out. What travels through the pipe is not the same: next
slide. (~2 min)
-->

---
hideInToc: true
---

# The Pipe Carries **Text** or **Objects**

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -c data/*/*.csv | sort -n
      97 data/processed/pendulum.csv
     130 data/raw/pendulum.csv
 3926142 data/raw/D0_KPi.csv
 3926369 total
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-ChildItem data/*/*.csv |
    Sort-Object Length |
    Select-Object Length, Name
 Length Name
 ------ ----
     97 pendulum.csv
    130 pendulum.csv
3926142 D0_KPi.csv
```

</div>

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🧵 **Lines of text**

`wc` prints one line per file. `sort -n` reads the number at the start of each line and knows nothing else about it: the line `total` is sorted with the files.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧱 **Objects**

`Get-ChildItem` passes one object per file, with properties such as `Name`, `Length` and `LastWriteTime`. `Sort-Object Length` names the property. Text is made at the end, from the properties asked for.

</div>

</div>

<!--
Speaker: ask first: which CSV file of the project is the largest? The same
answer, D0_KPi.csv, by two routes. In zsh the size is the
first word of a line; in PowerShell it is a number with a name.
(Get-Item data/raw/D0_KPi.csv).Length / 1MB prints 3.74426078796387: it can be
computed with. (~3 min)
-->

---
hideInToc: true
---

# Columns: `cut` and `Import-Csv`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cut -d, -f1,3 data/raw/D0_KPi.csv |
    head -n 3
M,TAU
1880.649,0.00041271152
1860.6599,0.0001864154
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Import-Csv data/raw/D0_KPi.csv |
    Select-Object M, TAU -First 2
M         TAU
-         ---
1880.649  0.00041271152
1860.6599 0.0001864154
```

</div>

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## ✂️ **`cut` counts**

`-d,` names the separator and `-f1,3` the fields, counted from 1. `cut` knows no header: line 1 is cut like every other line. It cuts at every comma, also at one inside quoted text.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🏷️ **`Import-Csv` names**

Line 1 gives the names. Every row becomes an object with the properties `M`, `PT`, `TAU` and `IPCHI2`, picked by name and not by place. A quoted `"x, y"` stays one value.

</div>

</div>

<!--
Speaker: ask which field number TAU has before running cut: head -n 1 shows
the names in order. In PowerShell the question does not come up. For the raw
pendulum table the separator is ;, so cut -d';' and Import-Csv -Delimiter ';'.
(~2 min)
-->

---
hideInToc: true
---

# Order: `sort` and `Sort-Object`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% tail -n +2 data/processed/pendulum.csv |
    sort | head -n 2
100,20.01
20,9.02
% tail -n +2 data/processed/pendulum.csv |
    sort -n | head -n 2
20,9.02
30,11.05
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Import-Csv data/processed/pendulum.csv |
    Select-Object -ExpandProperty length_cm |
    Sort-Object | Select-Object -First 2
100
20
PS> Import-Csv data/processed/pendulum.csv |
    Select-Object -ExpandProperty length_cm |
    Sort-Object {[int]$_} | Select-Object -First 2
20
30
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`tail -n +2` prints from line 2 on, so the header stays out; `Import-Csv` takes it as the names. Both shells compare text character by character from the left: `1` comes before `2`, so `100` comes before `20`. `sort -n` reads the start of each line as a number. In PowerShell `[int]` turns each value into a whole number before it is compared.

</div>

<!--
Speaker: the last slide of the editing section of Lecture 2, now with a way
out in each shell. In the PowerShell line the braces hold a small piece of
code that runs once for every value; dollar-underscore is the value at hand.
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
% tail -n +2 data/raw/D0_KPi.csv |
    cut -d, -f1 | sort -n | head -n 2
1766.2096
1808.1385
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Import-Csv data/raw/D0_KPi.csv |
    Select-Object -ExpandProperty M |
    Sort-Object {[double]$_} |
    Select-Object -First 2
1766.2096
1808.1385
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The same four steps in both: the header off, the column `M` kept, ordered by value, the first two taken. `[double]` is a number with a decimal point. With `tail -n 2` and `-Last 2` at the end both give 1920.3453 and 2453.6584. The column runs from 1766.2096 to 2453.6584 MeV/c², and the second value from each end lies much closer in: one row at each end is far from all the others.

</div>

<div class="card card-success card-glass pad-compact mt-sm">

✅ A sorted column shows its ends first, and a wrong value is usually at an end. Looking at both ends of every column is the first check of a new data file.

</div>

<!--
Speaker: 91 583 values sorted in under a second in both shells (zsh 0.06 s,
PowerShell 0.5 s on the test laptop). Ask the room what 1766 and 2453 might
be: nobody knows yet, and that is the right answer. They get a line number in
the next section. (~2 min)
-->

---
hideInToc: true
---

# Count Repeats: `uniq -c` and `Group-Object`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cut -d, -f3 data/raw/D0_KPi.csv | sort |
    uniq -c | sort -n | tail -n 3
   2 0.0026546149
   2 0.0035111452
  49 -100.0
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Import-Csv data/raw/D0_KPi.csv |
    Group-Object TAU -NoElement |
    Sort-Object Count |
    Select-Object -Last 3
Count Name
----- ----
    2 0.0001520892
    2 0.00017826671
   49 -100.0
```

</div>

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-info card-glass pad-compact">

## 🧮 **Two ways to count**

`uniq -c` merges equal lines that stand next to each other and writes how many there were, so `sort` comes first. `Group-Object` collects equal values wherever they stand and counts them. The last sort orders by the count.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔎 **What it shows**

A measured decay time almost never comes twice: the most frequent real values occur 2 times. One value occurs 49 times, `-100.0`. A value that repeats like this is not a measurement. It is the mark for "no value".

</div>

</div>

<!--
Speaker: 191 values occur twice, so the two shells list different ones in
front of the 49. Nobody told either pipeline about -100: counting repeats
found it. This is how a missing-value mark is found in a file that comes
without a description. (~2 min)
-->

---
hideInToc: true
---

# Keep Lines: `grep` and `Select-String`

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% grep -c ',-100' data/raw/D0_KPi.csv
49
% grep -n ',-100' data/raw/D0_KPi.csv |
    head -n 1
343:1818.1002,2978.644,-100.0,9901.186
% grep -c 'm,pt' data/raw/D0_KPi.csv
0
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Select-String ',-100' data/raw/D0_KPi.csv).Count
49
PS> (Select-String 'm,pt' data/raw/D0_KPi.csv).Count
1
```

</div>

</div>

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Job | zsh | PowerShell |
| --- | --- | --- |
| Lines that contain a text | `grep TEXT FILE` | `Select-String TEXT FILE` |
| Count them | `-c` | `( … ).Count` |
| Line number in front | `-n` | always, after the file name: `data\raw\D0_KPi.csv:343:…` |
| Lines **without** the text | `-v` | `-NotMatch` |
| Upper and lower case | different, `-i` makes them equal | equal, `-CaseSensitive` makes them different |

</div>

<!--
Speaker: the count is the number found with Ctrl+F in VS Code. 'm,pt' finds
the header line M,PT,TAU,IPCHI2 in PowerShell and nothing in zsh. Keep the
comma and the quotes in ',-100': grep reads a first argument that starts with
- as an option, and grep -100 FILE then waits for input; Ctrl+C ends the
wait. (~2 min)
-->

---
hideInToc: true
---

# From `data/raw` to `data/processed`

<div class="card card-primary card-glass pad-compact mt-sm">

## ✍️ **Keep the rows that have a decay time**

```text
% grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv
PS> Select-String ',-100' data/raw/D0_KPi.csv -NotMatch -Raw > data/processed/D0_valid.csv
```

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -l data/processed/D0_valid.csv
   91535 data/processed/D0_valid.csv
% wc -c data/processed/D0_valid.csv
 3924368 data/processed/D0_valid.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Get-Content data/processed/D0_valid.csv).Count
91535
PS> (Get-Item data/processed/D0_valid.csv).Length
4015903
```

</div>

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-success card-glass pad-compact">

## 📥 **Read here, write there**

The raw file is read and stays as it is. Delete the new file, run the line again, and it is back. `-Raw` passes only the text of each line.

</div>

<div class="card card-warning card-glass pad-compact">

## 📏 **Same rows, other bytes**

91 535 lines in both. 4 015 903 − 3 924 368 = 91 535: one `0D` per line, so the checksums differ too.

</div>

</div>

<!--
Speaker: check the arithmetic with the room: 91 584 − 49 = 91 535 lines, the
header and 91 534 rows. Without -Raw every line would start with the file
name and its line number (data\raw\D0_KPi.csv:1:M,PT,TAU,IPCHI2). In Lecture
2 the README said in words what was done to a file; here the command says it
exactly. The two files hold
the same data and still do not match byte for byte: keep that for the
checksums at the end of the lecture. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Regular **Expressions**

`grep` and `Select-String` kept the lines that contain one fixed text, `,-100`. A pattern describes a kind of text instead, and the same pattern works in VS Code and in both shells.

<!--
Speaker: so far the Find box, grep and Select-String looked for a fixed text.
A regular expression describes a kind of text. The same patterns work in the
Find box of VS Code, in grep on macOS and in Select-String in PowerShell.
(~1 min)
-->

---
hideInToc: true
---

# A Pattern Instead of a **Text**

<div class="note-text mt-sm">Question: how many rows have a mass from 1865 up to 1866 MeV/c²?</div>

<div class="card card-info card-glass pad-compact mt-sm">

```text
% grep -c 1865 data/raw/D0_KPi.csv
1986
PS> (Select-String 1865 data/raw/D0_KPi.csv).Count
1986
% grep -c '^1865' data/raw/D0_KPi.csv
1846
PS> (Select-String '^1865' data/raw/D0_KPi.csv).Count
1846
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔎 **A fixed text finds too much**

`1865` is in 1986 lines, also inside other numbers: in `2561.1865`, a `PT`. 140 lines are of that kind.

</div>

<div class="card card-success card-glass pad-compact">

## ✳️ **A pattern says where**

`^` is the start of the line: 1846 masses begin with 1865. Such a text is a **regular expression**, regex for short.

</div>

</div>

<div class="note-text mt-sm">The signs of a regex stand for a kind of character, for a repetition or for a place in the line.</div>

<!--
Speaker: the line with % is macOS zsh, the line with PS is PowerShell. 1986 minus 1846 is
140: 73 in TAU, 30 in IPCHI2, 23 in PT, 1 in both PT and IPCHI2, 13 further
inside the mass. Show one
of them. zsh: grep 1865 data/raw/D0_KPi.csv | grep -v '^1865' | head -n 1.
PowerShell: Get-Content data/raw/D0_KPi.csv | Select-String 1865 |
Select-String '^1865' -NotMatch | Select-Object -First 1. Both print
1910.1326,2561.1865,0.00020346862,3.5583153. (~2 min)
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
Speaker: each row can be run as grep -E 'PATTERN' data/processed/pendulum.csv
in zsh and as Select-String 'PATTERN' data/processed/pendulum.csv in
PowerShell: the same lines come out. Let the room predict the lines for 1.0
before you run it. (~3 min)
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
The pattern ^; finds the mean line without the word mean. Every count in the
table is the same in grep -E and in Select-String. Remember 0$ and its two
lines: it comes back at the end of the section. (~3 min)
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
patterns. Read the counter aloud after each. The Find box is the same on
every laptop in the room. (~3 min)
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

`20,9.02` becomes `| 20 | 9.02 |`. One replacement on the 10 lines of the cleaned file does what the first two edits with many cursors did in Lecture 2.

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Replace All with a pattern changes every match at once, also the ones nobody looked at. Read the counter first. If the number is not the one expected, the pattern is wrong.

</div>

<!--
Speaker: do the first replacement on a fresh copy of the raw file in
data/processed, then Ctrl+Z. The 10 matches are the nine rows and the mean
line. PowerShell knows $1 too: (Get-Content data/raw/pendulum.csv) -replace
'([0-9]),([0-9])', '$1.$2' prints the table with points, for whoever asks.
(~3 min)
-->

---
layout: section
hideInToc: true
---

# Programs **Someone Else Wrote**

Filters count, sort and keep lines. The four edits of Lecture 2 and a mean take a program, and a program someone else wrote runs with one typed line, like any other command.

<!--
Speaker: at the start of the lecture one typed line cleaned the pendulum table.
This section opens that line: what the program is, what the file is, and why
its output has the same bytes in both shells. Then a second handed-out
program computes what no filter can: a mean. (~1 min)
-->

---
hideInToc: true
---

# A Program Is a **Text File**

<div class="card card-primary card-glass pad-compact mt-sm">

## 📜 **`scripts/clean_pendulum.py`, lines 25–32**

```python
def clean(lines):
    out = []
    for line in lines:
        if "mean" in line:
            continue
        line = line.replace(",", ".").replace(";", ",")
        out.append(line.split(",", 1)[1])
    return out
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ✍️ **The four edits of Lecture 2**

- Line 28: a line with `mean` is skipped
- Line 30, two edits: `,` becomes `.`, then `;` becomes `,`
- Line 31: only what follows the first comma is kept, so `nr` goes

</div>

<div class="card card-accent card-glass pad-compact">

## 🧭 **The line that runs it**

- `python3` on macOS, `python` on Windows: the program
- Its first argument: this file, 54 lines of text
- The next two: the file it reads and the file it writes

</div>

</div>

<!--
Speaker: open the file in VS Code. Nobody has to learn these words today;
point at the four edits. The order is the order of
Lecture 2: the decimal comma becomes a point while it is still the only comma.
The 54 is measured: wc -l scripts/clean_pendulum.py on macOS,
(Get-Content scripts/clean_pendulum.py).Count in PowerShell, 54 in both.
(~3 min)
-->

---
hideInToc: true
---

# Run It, Then **Measure** It

<div class="card card-info card-glass pad-compact mt-sm">

## ⌨️ **One run per shell**

```text
% python3 scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv
9 rows written to data/processed/pendulum_script.csv
% wc -c data/processed/pendulum_script.csv
      97 data/processed/pendulum_script.csv

PS> python scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv
9 rows written to data/processed/pendulum_script.csv
PS> (Get-Item data/processed/pendulum_script.csv).Length
97
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **97, byte by byte**

The header `length_cm,t10_s` is 15 characters and an LF: 16 bytes. `20,9.02` takes 8, the seven rows from 30 to 90 take 9 each, `100,20.01` takes 10. 16 + 8 + 7 × 9 + 10 = 97.

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **The same in both shells**

Nine rows and the header, one byte per character, one LF per line: 97 bytes on macOS and on Windows. Delete the file, run the line again, and the same 97 bytes are back.

</div>

</div>

<!--
Speaker: two lines, one per shell: python3 on macOS, python on Windows, and
the same paths after it. Run it on both laptops at the front and read out the two sizes. Then ask:
what if the file is copied by the shell instead? (~3 min)
-->

---
hideInToc: true
---

# Where **107** Bytes Come From

<div class="card card-primary card-glass pad-compact mt-sm">

## 📋 **The same ten lines, written by the shell**

```text
PS> Get-Content data/processed/pendulum_script.csv > results/copy.csv
PS> (Get-Item results/copy.csv).Length
107
PS> (Get-FileHash results/copy.csv).Hash
C06D1344B6A39F3895FB0A7F0067EC0B2F4CA94D71F7F57F57981F5BF102106D
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🔎 **Ten lines, ten bytes more**

107 − 97 = 10. `Get-Content` hands on ten lines of text, and PowerShell writes each line itself, ending it with CRLF: `>` and `Set-Content` alike. This is copy C of the opening. In zsh, `cat` with `>` copies the bytes as they are: 97.

</div>

<div class="card card-success card-glass pad-compact">

## 🧷 **The script sets its own bytes**

Line 47 of `clean_pendulum.py` opens the file it writes:

```python
open(target, "w", encoding="utf-8", newline="\n")
```

`newline="\n"`: every line ends with LF, on every system. So the script wrote 97 bytes in both shells.

</div>

</div>

<div class="note-text mt-sm">Windows PowerShell 5.1 writes 216 bytes: <code>FF FE</code>, then two bytes per character (UTF-16).</div>

<!--
Speaker: run the copy live in both shells and delete results/copy.csv
afterwards (rm, or Remove-Item). On the Mac: cat
data/processed/pendulum_script.csv into results/copy.csv with the redirect,
then wc -c gives 97. Measured in PowerShell 7.6 on Windows: Get-Content sent into
results/copy.csv with the redirect, and Get-Content piped to Set-Content, both
write 107 bytes, hash C06D..., the same file as copy C. What adds the 0D is
PowerShell writing lines of text itself; the output of a program redirected
into a file keeps its bytes in PowerShell 7.6. Python on Windows writes CRLF
itself when the newline is not stated: the same open(...) without newline="\n"
gave 107 bytes, measured. That is why the script states it.
In Windows PowerShell 5.1 the Get-Content line writes 2 + 2 x 107 = 216
bytes, UTF-16 LE with the byte-order mark FF FE. The point is not that one
shell is wrong: each writes text by its own rule, and a file whose bytes must
match everywhere is written by a program that states the rule. (~3 min)
-->

---
hideInToc: true
---

# Run a Program **Someone Else Wrote**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
% python3 scripts/column_stats.py data/raw/D0_KPi.csv TAU
PS> python scripts/column_stats.py data/raw/D0_KPi.csv TAU
file    data/raw/D0_KPi.csv
column  TAU
rows    91583
min     -100.0
max     0.5787994
mean    -0.0525221
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧭 **The same shape as `clean_pendulum`**

- The program, the file to run, then the words for the script: a path and a column name
- The output is the same in both shells
- The shell counts and sorts lines. A mean takes a program: this one is 53 lines that someone else wrote and tested

</div>

<div class="card card-warning card-glass pad-compact">

## 🧹 **Why the cleaning comes first**

On `data/raw/pendulum.csv` it answers `no column t10_s`: with `;` between the values it reads one column, `nr;length_cm;t10_s`. On the cleaned copy it gives 9 rows and a mean of 15.1389, the `15,14` of the deleted line.

</div>

</div>

<!--
Speaker: column_stats.py is in scripts, handed out with the lecture. Do not
open it. Run it for M as well: 91 583 rows, mean 1864.1. Then for t10_s on
data/raw/pendulum.csv and on data/processed/pendulum_script.csv. With Tab,
PowerShell completes the path as .\data\raw\D0_KPi.csv; the script prints
the path as it was typed, and the numbers are the same. (~3 min)
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
Speaker: run the script on both files, in either shell: the numbers are the
same. In PowerShell D0_valid.csv was written with CRLF, 4 015 903 bytes
against 3 924 368 on a Mac, one more byte for each of its 91 535 lines; the
program reads both alike. This is why the fifth question of Lecture 2, how
missing values are marked, is asked before any number is computed. (~3 min)
-->

---
layout: section
hideInToc: true
---

# Tools & **Environments**

The cleaning line starts with `python3` or `python`: a program that somebody installed. This section is about where programs come from, how the shell finds them, and how a project writes down which ones it needs.

<!--
Speaker: every command so far was a program that was already on the laptop.
Python was not: "Python was not found", from the Shell section, is where a
laptop without it stops. This section installs programs by typed lines and
ends with a list from which another laptop installs the same ones. (~1 min)
-->

---
hideInToc: true
---

# Where a Program **Comes From**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · 🪟 **Windows · PowerShell**

```text
% which python3
/Library/Frameworks/Python.framework/Versions/3.14/bin/python3
PS> (Get-Command python).Source
C:\Users\ada\AppData\Local\Programs\Python\Python314\python.exe
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🧱 **Built in**

`ls`, `cat`, `Get-Content`: they came with the system, in `/bin` or inside PowerShell.

</div>

<div class="card card-accent card-glass pad-compact">

## 📦 **An installer**

Python from python.org, VS Code: a file downloaded from a web page and clicked through. It copies the program into a folder of its own.

</div>

<div class="card card-info card-glass pad-compact">

## 🗂️ **A package manager**

One program that installs other programs by name, with a typed line: `winget` on Windows, Homebrew on macOS. Two slides on.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

`which` and `Get-Command` print where the shell found the program: the folder the installer made. A program is usable from the prompt when two things hold: its files are in a folder, and that folder is on the list the shell searches. The list is the next slide.

</div>

<!--
Speaker: the two paths are where the python.org installers put Python by
default, the framework folder on macOS and the per-user Programs folder on
Windows. They were not yet checked on the lecturer's own laptops: run the two
lines once before the lecture. A Mac without the python.org install answers
/usr/bin/python3, Apple's copy from the developer tools. (~2 min)
-->

---
hideInToc: true
---

# The List the Shell Searches: **PATH**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · 🪟 **Windows · PowerShell**, shortened

```text
% echo $PATH | tr ':' '\n'
/Library/Frameworks/Python.framework/Versions/3.14/bin
/usr/bin
PS> $env:PATH -split ';'
C:\Windows\system32
C:\Program Files\PowerShell\7\
C:\Users\ada\AppData\Local\Programs\Python\Python314\
C:\Users\ada\AppData\Local\Microsoft\WindowsApps
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## ➡️ **Left to right**

The shell takes the first folder on the list that holds a program of the typed name. Of two Pythons on the list, the first one runs.

</div>

<div class="card card-warning card-glass pad-compact">

## 🪟 **`Python was not found`**

`WindowsApps` holds a stand-in `python.exe` from Windows. **Add python.exe to PATH** puts `Python314` on the list before it; without the tick, the stand-in answers.

</div>

<div class="card card-accent card-glass pad-compact">

## 🍎 **`python3`, not `python`**

macOS ships no program named `python`. The installer adds `python3` and `python3.14`, so `python` stays `command not found`.

</div>

</div>

<!--
Speaker: a terminal reads PATH once, when it opens, so a program installed
while a terminal is open is found only in a new one. PATH is one text, folders separated by : on macOS and by ; on
Windows; tr and -split print one per line. The lists are shortened to the
folders that matter here; a real laptop shows ten to twenty. The Windows
order is real: the system's folders first, then the user's, and the Python
installer puts its two folders in front of WindowsApps. Let the room predict
what happens when the installer's folder is missing before you say it. (~3 min)
-->

---
hideInToc: true
---

# A Package **Manager**

<div class="card card-info card-glass pad-compact mt-sm">

A package manager is a program that installs other programs. It looks a name up in a **catalogue**, downloads the files, puts them in a folder, and puts the folder on `PATH`. It also lists what it installed, upgrades it, and removes it. Each of these is a typed line.

</div>

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Job | 🪟 `winget`, comes with Windows | 🍎 Homebrew, `brew` |
| --- | --- | --- |
| Find a name in the catalogue | `winget search powershell` | `brew search git` |
| Install | `winget install --id Microsoft.PowerShell` | `brew install git` |
| What is installed, with versions | `winget list` | `brew list --versions` |
| Newer versions | `winget upgrade --all` | `brew upgrade` |
| Remove | `winget uninstall --id Microsoft.PowerShell` | `brew uninstall git` |

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 📜 **Why a typed line**

The install line goes into the README, like the cleaning line. On the next laptop it installs the same program, and `winget list` shows which version. An installer clicked through leaves no line behind.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧭 **What this course installs**

PowerShell 7 by `winget`. Python from python.org on both systems. Git from git-scm.com on Windows, and on a Mac from Apple's developer tools, `xcode-select --install`. Homebrew is not needed for the course. Linux has `apt`, with the same five jobs.

</div>

</div>

<!--
Speaker: the five jobs are the same in every package manager; the table has
the two of this room. winget is part of Windows 10 and 11 (the App Installer).
Homebrew has to be installed first, from brew.sh, which is why the course
takes Python from python.org instead. A Homebrew Python also refuses pip
install with "externally-managed-environment": its packages come from brew.
(~3 min)
-->

---
hideInToc: true
---

# PowerShell 7, **by One Typed Line**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🪟 **In Windows PowerShell 5.1, the built-in one**

```text
PS> winget install --id Microsoft.PowerShell --source winget
Found PowerShell [Microsoft.PowerShell] Version 7.6.6
Downloading https://github.com/PowerShell/PowerShell/releases/download/v7.6.6/PowerShell-7.6.6-win-x64.msi
Successfully installed
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🏷️ **The line, read**

`--id Microsoft.PowerShell` is the name in the catalogue, `--source winget` the catalogue. The output names the version it found, the file it downloaded, and the result.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔍 **Afterwards**

`PATH` has `C:\Program Files\PowerShell\7\`, so a new terminal finds `pwsh`. VS Code is told once to open it: **Terminal: Select Default Profile**, then **PowerShell**. `$PSVersionTable.PSVersion.Major` answers `7`.

</div>

<div class="card card-info card-glass pad-compact">

## 🍎 **On a Mac**

`git --version` on a Mac without Git opens the installer of Apple's developer tools, the same as `xcode-select --install`. Python comes from the installer on python.org, with every default.

</div>

</div>

<div class="note-text mt-sm"><code>winget</code> asks once whether the source agreements are accepted: <code>Y</code>. A managed laptop may ask for an administrator password; the same <code>.msi</code> file, run by hand, installs the same version.</div>

<!--
Speaker: the three output lines are the ones winget prints for this package
(found, downloading, installed); its licence notice and progress bar are left
out. Not yet run on the lecturer's Windows laptop with 7.6.6: run it once
before the lecture and correct the version on the slide. The same line works
in PowerShell 7 to upgrade. (~2 min)
-->

---
hideInToc: true
---

# **pip**: the Package Manager of Python

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · 🪟 **Windows · PowerShell**

```text
% python3 -m pip --version
pip 26.2.1 from /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/pip (python 3.14)
PS> python -m pip --version
pip 26.2.1 from C:\Users\ada\AppData\Local\Programs\Python\Python314\Lib\site-packages\pip (python 3.14)
```

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📚 **The catalogue**

PyPI, pypi.org. A package has a name, a version, and the list of packages it needs itself. `numpy` is one of them.

</div>

<div class="card card-accent card-glass pad-compact">

## 🐍 **`python -m pip`**

pip is itself a Python program, and this form runs it inside a named Python. With more than one Python on a laptop it says which one gets the package. `pip` alone takes the first on `PATH`.

</div>

<div class="card card-info card-glass pad-compact">

## 📂 **Where packages go**

`site-packages`, a folder inside that Python. `import` searches a list of folders as the shell searches `PATH`; the list is `sys.path`, and `site-packages` is on it.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

Two levels. `winget` and Homebrew install programs for the whole system, Python among them. pip installs packages into one Python. Both answer the same five jobs: search, install, list, upgrade, remove.

</div>

<!--
Speaker: the two paths are the python.org defaults; pip comes with Python, so
nothing is installed to get it. The version was measured in Python 3.14.8 on
Linux; the pip bundled with a python.org 3.14 can be another one. Say "python
dash m pip" aloud once and keep that form on every slide. (~2 min)
-->

---
hideInToc: true
---

# `pip install numpy`, **Measured**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **`python3` on macOS** · 🪟 **`python` on Windows, the same lines**

```text
% python3 -c "import numpy"
ModuleNotFoundError: No module named 'numpy'
% python3 -m pip install numpy
Downloading numpy-2.5.4-….whl (16.7 MB)
Successfully installed numpy-2.5.4
% python3 -m pip list
Package Version
------- -------
numpy   2.5.4
pip     26.2.1
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📦 **What arrived**

One file, a *wheel*: numpy 2.5.4 built for this Python and this system, 16.7 MB. Unpacked into `site-packages/numpy`: 43 MB of files, and `import numpy` finds them.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔁 **The line again**

On a laptop that has it: `Requirement already satisfied: numpy … (2.5.4)`. One version is asked for with `==`: `pip install numpy==2.5.4`. `pip uninstall numpy` removes it.

</div>

</div>

<!--
Speaker: measured on Linux with Python 3.14.8; the wheel is another file on
macOS and on Windows, with another size, and the rest of the output is the
same. pip show numpy prints the Location, the site-packages folder. Ask the
room where the 43 MB are, and show the folder in the Side Bar if it is quick.
(~2 min)
-->

---
hideInToc: true
---

# One Python, **Every Project**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
% python3 -c "import numpy as np; print(np.float_)"
AttributeError: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## ⚠️ **One `site-packages`, one version**

Every project on the laptop imports the same numpy. A script written for numpy 1.26 uses `np.float_`. After `pip install --upgrade numpy` for another project, it stops with this message. The upgrade for one project broke the other.

</div>

<div class="card card-success card-glass pad-compact">

## ✅ **One Python per project**

A project gets a Python of its own, with its own `site-packages`: a **virtual environment**. Packages installed into it are seen by that project only, and the laptop's Python stays as it was.

</div>

</div>

<div class="note-text mt-sm">The message was produced with numpy 2.5.4. <code>np.float_</code> existed up to numpy 1.26 and was removed in 2.0, released in June 2024.</div>

<!--
Speaker: this is the usual way a working script stops working: nothing in the
script changed, a package on the laptop did. The two cards are the problem
and its fix; the next three slides do the fix. (~2 min)
-->

---
hideInToc: true
---

# A Virtual **Environment**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% python3 -m venv .venv
% ls .venv
bin        include    lib        pyvenv.cfg
% source .venv/bin/activate
(.venv) % which python
…/analysis-project/.venv/bin/python
(.venv) % deactivate
%
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> python -m venv .venv
PS> ls .venv -Name
Include
Lib
Scripts
pyvenv.cfg
PS> .venv\Scripts\Activate.ps1
(.venv) PS> (Get-Command python).Source
…\analysis-project\.venv\Scripts\python.exe
(.venv) PS> deactivate
```

</div>

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📁 **A folder**

`.venv` in the project: 14 MB, 891 files, most of them a copy of pip. `pyvenv.cfg` names the Python it was made from: `home = …`, `version = 3.14.8`.

</div>

<div class="card card-accent card-glass pad-compact">

## 🔛 **Activation**

The script puts `.venv/bin`, or `.venv\Scripts`, at the front of `PATH`. From then on `python` is the environment's Python in both shells, and the prompt shows `(.venv)`. `deactivate` takes it off the list.

</div>

<div class="card card-info card-glass pad-compact">

## 🚫 **Not a file to keep**

`.venv` is made again with one line, like `data/processed`. It is not copied to another laptop and not backed up.

</div>

</div>

<!--
Speaker: type the lines live. The sizes were measured on Linux for a fresh
environment of Python 3.14.8; a python.org Python gives numbers of the same
order. The activate script does one thing worth saying twice: it edits PATH,
the list of the slide before last, for this terminal only. In Windows
PowerShell 5.1 the activate script is refused by the execution policy;
PowerShell 7 runs it. (~3 min)
-->

---
hideInToc: true
---

# An Empty Environment, **Filled**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · 🪟 **Windows · PowerShell, the same lines**

```text
(.venv) % python -m pip list
Package Version
------- -------
pip     26.2.1
(.venv) % python -c "import numpy"
ModuleNotFoundError: No module named 'numpy'
(.venv) % python -m pip install numpy
Successfully installed numpy-2.5.4
(.venv) % python -m pip show numpy
Location: /Users/ada/Documents/analysis-project/.venv/lib/python3.14/site-packages
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 🧪 **The empty environment is a test**

The laptop has numpy; the environment does not see it. A script that runs in a fresh environment has named everything it needs, and nothing it needs is hidden somewhere on the laptop.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📂 **Inside the project**

The package went into `.venv/lib/python3.14/site-packages`, on Windows `.venv\Lib\site-packages`: 83 MB with numpy. The environment of another project holds numpy 1.26 next to it.

</div>

</div>

<!--
Speaker: with (.venv) in the prompt the word is python on both systems, so
the lines are the same. pip show prints seven lines; only Location is on the
slide, and on Windows it reads C:\Users\ada\...\.venv\Lib\site-packages. The
83 MB and 2228 files were measured on Linux. (~2 min)
-->

---
hideInToc: true
---

# **requirements.txt**: the List, Written Down

<div class="card card-primary card-glass pad-compact mt-sm">

```text
(.venv) % python -m pip freeze > requirements.txt
(.venv) % cat requirements.txt
numpy==2.5.4
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 💻 **On another laptop**

Three lines: `python3 -m venv .venv`, `source .venv/bin/activate` and `python -m pip install -r requirements.txt`; on Windows `python -m venv .venv` and `.venv\Scripts\Activate.ps1`. The same numpy 2.5.4 arrives, because the version stands in the file.

</div>

<div class="card card-success card-glass pad-compact">

## 📁 **What the project keeps**

`requirements.txt` is kept and passed on, like `scripts`. `.venv` is made again from it, like `data/processed` from `data/raw`. The section **How to rebuild** of the README starts with the three lines.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`pip freeze` writes every installed package with its exact version, `==`: one line here, one line per package in a larger project. The pinned versions are what makes the rebuild on another laptop give the same numbers.

</div>

<!--
Speaker: the file is the environment, written down, in the same sense as the
README lines are the cleaning, written down. Today's two scripts need no
package, so the project's own requirements.txt stays empty and the README
names the Python version instead; the file grows with the first import of an
installed package. (~2 min)
-->

---
layout: section
hideInToc: true
---

# Checksums & **Backups**

The script wrote 97 bytes in both shells, PowerShell's copy of the same ten lines 107. A checksum tells files apart by their bytes, however alike their text looks.

<!--
Speaker: a checksum is a short number computed from every byte of a file,
as Lecture 3 worked out by hand; here it is a command, in both shells, and it does
three jobs: it compares the script with the hand, it guards the raw data, and
it tells the copies of the opening apart. (~1 min)
-->

---
hideInToc: true
---

# The Checksum of a **File**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · 🪟 **Windows · PowerShell**

```text
% shasum -a 256 data/raw/D0_KPi.csv
25c3c97299ea844f27308fde20a00ecaa87580868f3c767d7ade5621c1505136  data/raw/D0_KPi.csv

PS> (Get-FileHash data/raw/D0_KPi.csv).Hash
25C3C97299EA844F27308FDE20A00ECAA87580868F3C767D7ADE5621C1505136
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 🔠 **The same 64 digits**

`shasum` writes the hex digits in lower case, `Get-FileHash` in upper case: `25c3` and `25C3` are one number. 64 hex digits are the 256 bits of SHA-256, computed from every byte of the file.

</div>

<div class="card card-accent card-glass pad-compact">

## 🧬 **One byte changes all of it**

```text
be05af03…fff0870b   20,9.02
17dbc893…a1440bc9   20,9.03
```

The cleaned pendulum table, and a copy with one digit changed.

</div>

</div>

<div class="note-text mt-sm">The 3 926 142 bytes of <code>D0_KPi.csv</code> give these digits on every laptop in the room, in either shell. A laptop that prints other digits has another file.</div>

<!--
Speaker: open with the question "is the D0 file on your laptop the same file
as on mine?" Four million bytes cannot be compared by eye. Ask the room to run
the line of their shell and read the first and the last four digits: 25c3 and
5136. Get-FileHash without the brackets prints a table: Algorithm SHA256, the
hash, the full path. (~2 min)
-->

---
hideInToc: true
---

# The Script **Against the Hand**

<div class="note-text mt-sm"><code>data/processed/pendulum.csv</code> is the table cleaned by hand in Lecture 2. <code>pendulum_script.csv</code> is what the script wrote next to it.</div>

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · 🪟 **Windows · PowerShell**

```text
% shasum -a 256 data/processed/pendulum*.csv
be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum.csv
be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b  data/processed/pendulum_script.csv

PS> (Get-FileHash data/processed/pendulum*.csv).Hash
BE05AF034937EF615C93B2FB5D8369C899DEF80D0472A6187C5DBD3AFFF0870B
BE05AF034937EF615C93B2FB5D8369C899DEF80D0472A6187C5DBD3AFFF0870B
```

</div>

<div class="card card-success card-glass pad-compact mt-md">

🟰 The table cleaned by hand in Lecture 2 and the table written by the script have one checksum: the same 97 bytes. The script does what the hands did, byte for byte. Copy A of the opening has this checksum too.

</div>

<!--
Speaker: the question is whether the handed-out script does exactly what the
four hand edits of Lecture 2 did. pendulum.csv in data/processed is the table
cleaned by hand on the projector in Lecture 2 (the answer key of the project
folder); the script wrote pendulum_script.csv next to it.
The wildcard pendulum*.csv takes both and leaves out other files in the
folder. (~2 min)
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
data/raw/D0_KPi.csv: OK
data/raw/pendulum.csv: OK
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Get-FileHash data/raw/*).Hash |
>>   Set-Content data/checksums.txt
PS> $list = Get-Content data/checksums.txt
PS> $now = (Get-FileHash data/raw/*).Hash
PS> Compare-Object $list $now
PS>
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

- The list is written once, when the raw files arrive. It is checked after every copy and before work is handed in
- `-c` reads the list, computes each checksum again and compares. `Compare-Object` prints only the lines that differ: nothing means the same
- `$list = …` keeps an output under a name for the next line

</div>

<div class="note-text mt-sm">The list stands in <code>data</code>, not in <code>data/raw</code>, so that <code>data/raw/*</code> never includes it.</div>

<!--
Speaker: Lecture 2 said raw is never edited. This list turns that rule into a
test that runs in a second. (~2 min)
-->

---
hideInToc: true
---

# One Digit **Changed**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · 🪟 **Windows · PowerShell**

```text
% shasum -a 256 -c data/checksums.txt
data/raw/D0_KPi.csv: OK
data/raw/pendulum.csv: FAILED
shasum: WARNING: 1 computed checksum did NOT match

PS> $now = (Get-FileHash data/raw/*).Hash
PS> Compare-Object $list $now

InputObject                                                      SideIndicator
-----------                                                      -------------
1E458098C942E174F4A9A3622A0D2BF3A4CE89CDFFC7B1CD4A6A7931D9E4C9BB =>
26B8B610C1191A6F3C9802605E247E6514344C684E5E5FAAF62A635A64FF31F8 <=
```

</div>

<div class="note-text mt-sm">In a copy of the project, <code>1;20;9,02</code> of the raw pendulum file became <code>1;20;9,03</code>. <code>=&gt;</code> marks a hash found only now, <code>&lt;=</code> one found only in the list: <code>26B8…</code> is the line of <code>pendulum.csv</code>.</div>

<!--
Speaker: change the digit in a copy of the project, never in the file itself.
zsh names the file. PowerShell shows the old and the new hash; the old one
is the second line of checksums.txt, the pendulum file. (~1 min)
-->

---
hideInToc: true
---

# How Files **Are Lost**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| What happens | What is lost | What brings it back |
| --- | --- | --- |
| A delete, a `>` or a move hits the wrong file. A spreadsheet is saved over a raw file | One file, at once | An older copy |
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
of the table gets a hand. The last row is the one the list of checksums was
for. (~2 min)
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
layout: section
hideInToc: true
---

# The **README**

A checksum names the exact bytes of a file, and the 3-2-1 rule keeps them. The README is where both are written down, with the lines that make every file again.

<!--
Speaker: the README of the project folder, as Lecture 2 showed it, says
where the data came from and lists the hand edits in words. This section
completes it with what the commands of today have found, and tests it the way
a stranger would. (~1 min)
-->

---
hideInToc: true
---

# What the README **Still Lacks**

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ✅ **Already in the README**

- A title, one paragraph, the author
- The folders and what goes into each
- For each data file: source, DOI, licence, date, size, what one row is
- The four edits made by hand, in words

</div>

<div class="card card-warning card-glass pad-compact">

## ❓ **What a stranger still asks**

- What is `TAU`, and in which unit?
- Why is `TAU` `-100.0` in 49 rows?
- Are the raw files the ones that were downloaded?
- Which Python, and which lines, make `data/processed`, and in which shell?
- Which of the four copies is the cleaned table?
- May I copy the scripts?

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The test for a README: someone with an empty laptop and the project folder gets the same files, and asks nobody. Each question on the right is one more message to the author. The rest of this section answers them.

</div>

<!--
Speaker: open README.md and its preview next to the slide (Ctrl+K, then V)
and tick the left-hand card off against it. The third question was answered
by the list of checksums a moment ago; Columns and Units, How to Rebuild
with its test, The Licence and the last slide before the Recap answer the
other five. (~2 min)
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

Source, DOI, licence, the date it was fetched, and the list of checksums of `data/raw`.

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

The Python, then the lines, in order, that make every file in `data/processed`, and the shell each one runs in.

</div>

<div class="card card-warning card-glass pad-compact">

## ⚖️ **Licence, contact**

What others may do with the work, and whom to ask.

</div>

</div>

<div class="note-text mt-md">Title, folders and the source of the data exist since Lecture 2, and the list of checksums since a few slides ago. Columns and rebuild are written now from commands that ran today; the licence is one decision.</div>

<!--
Speaker: six parts, in the order a stranger reads them: what is this, where
did it come from, what do the numbers mean, where is everything, how do I
make it again, what may I do with it. (~1 min)
-->

---
hideInToc: true
---

# Columns and **Units**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✏️ **In the README**

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

## 🔎 **Checked by a command**

```text
% head -n 1 data/raw/D0_KPi.csv
M,PT,TAU,IPCHI2
PS> Get-Content data/raw/D0_KPi.csv -First 1
M,PT,TAU,IPCHI2
% grep -c ',-100' data/raw/D0_KPi.csv
49
PS> (Select-String ',-100' data/raw/D0_KPi.csv).Count
49
```

The names and the 49 come out of the file. The units do not: no command finds MeV/c² in `D0_KPi.csv`. They are on the record page, so the README has to hold them.

</div>

</div>

<!--
Speaker: run the four lines, zsh and PowerShell, and type the table into the
README with the preview open. The table is the Markdown of Lecture 2; what is
new is that every line of it except the units was checked by a command that
anyone can run again. (~2 min)
-->

---
hideInToc: true
---

# How to **Rebuild**

<div class="card card-primary card-glass pad-compact mt-sm">

## ✏️ **In the README**

```md
## How to rebuild

Run in the project folder: zsh on macOS, PowerShell 7 on Windows.
Python 3.14 from python.org; the scripts need no package beyond it.

1. The cleaned pendulum table, 97 bytes, SHA-256 `be05af03…fff0870b`:
   - zsh: `python3 scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv`
   - PowerShell: `python scripts/clean_pendulum.py data/raw/pendulum.csv data/processed/pendulum_script.csv`
2. `D0_KPi.csv` without the 49 rows marked `-100`, 91 535 lines:
   - zsh: `grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv`
   - PowerShell: `Select-String ',-100' data/raw/D0_KPi.csv -NotMatch -Raw > data/processed/D0_valid.csv`
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## ♻️ **The work, not a story of it**

The README of Lecture 2 says "Mean line deleted, `,` replaced by `.`". That describes the work. These lines **are** the work: copied out of the terminal history, not typed from memory.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔀 **One line per shell**

The program is `python3` on macOS and `python` on Windows, and a filter is spelled differently in each shell. So each step has two lines. Do the two lines make the same file?

</div>

</div>

<!--
Speaker: scroll the terminal history (Up key) to the clean_pendulum line and
paste it, do not retype it. A line that was copied and ran has been tested; a
line typed into the README from memory has not. End on the question of the
right card. (~2 min)
-->

---
hideInToc: true
---

# Test the **Section**

<div class="card card-info card-glass pad-compact mt-sm">

Delete `pendulum_script.csv` and `D0_valid.csv`, paste the lines of the README into the shell, then measure what came back.

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -c data/processed/*.csv
 3924368 data/processed/D0_valid.csv
      97 data/processed/pendulum.csv
      97 data/processed/pendulum_script.csv
 3924562 total
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> Get-ChildItem data/processed |
>>   Select-Object Name, Length

Name                 Length
----                 ------
D0_valid.csv        4015903
pendulum_script.csv      97
pendulum.csv             97
```

</div>

</div>

<div class="grid-2 gap-md mt-md">

<div class="card card-success card-glass pad-compact">

🟰 `pendulum_script.csv`: 97 bytes in both shells, SHA-256 `be05af03…`. The README may promise this checksum.

</div>

<div class="card card-warning card-glass pad-compact">

🔀 `D0_valid.csv`: one `0D` more on each of its 91 535 lines in PowerShell, as with `copy.csv`. The README can promise its lines, not its checksum.

</div>

</div>

<!--
Speaker: delete the two files (zsh: rm data/processed/pendulum_script.csv
data/processed/D0_valid.csv; PowerShell: Remove-Item with the two paths
separated by a comma), paste the README lines from its preview, measure. The
two D0_valid.csv files hold the same rows; their checksums are d9192e57… on
macOS and F824C1E6… on Windows. The script sets its own line ending, LF, so
its file is the same 97 bytes everywhere: a file whose checksum goes into the
README is made by a script, not by a filter and a redirect.
(~3 min)
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
Speaker: the last question of the stranger, "may I copy the scripts?", has
no answer until this section exists. choosealicense.com has the text of each
licence, ready to copy into the file. MIT allows any use as long as the
notice stays in the file. CC BY asks that the author is named. (~2 min)
-->

---
hideInToc: true
---

# Which Copy? **The README Says**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Copy of the opening | Bytes | SHA-256 | What differs |
| --- | --- | --- | --- |
| A | 97 | `be05af03…fff0870b` | nothing: the script's file |
| B | 96 | `139c90c8…18ddfe54` | no `0A` after the last line |
| C | 107 | `c06d1344…f102106d` | CRLF, as PowerShell writes it |
| D | 105 | `12c5c5ca…3afb291b` | CRLF, and no line break after the last line |
| E, with `20,9.03` | 97 | `17dbc893…a1440bc9` | one digit |

</div>

<div class="card card-success card-glass pad-compact mt-md">

```md
- **Cleaned copy:** `data/processed/pendulum.csv`, 97 bytes,
  SHA-256 `be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b`
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

✅ The size rules out B, C and D. A copy with one digit changed, E, has 97 bytes as well, and only the checksum rules it out. With both written into the README, anyone can check a copy with one line: `shasum -a 256` or `Get-FileHash`.

</div>

<!--
Speaker: do not cut this slide: it answers the question of the opening. Go
back to the four sizes: 96 was the missing last line break (the Count
slide), 107 and 105 were CRLF (24 Characters, Where 107 Bytes). E is new
here: the same ten lines with one digit changed, the copy of "One byte
changes all of it". The size alone cannot tell A from E; SHA-256 can. Add
the line to README.md live, then run the checksum line of your shell on
data/processed/pendulum.csv and read the first and last eight digits. (~2 min)
-->

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="stack-tight mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Read the **prompt** of macOS `zsh` and of PowerShell 7, and name a file by an **absolute** or a **relative path**

</div>

<div class="card card-success card-glass pad-compact">

✅ Read, count, make, copy, move and delete files in both shells, and name many with one **wildcard**

</div>

<div class="card card-success card-glass pad-compact">

✅ Count, search and sort 91 583 rows, keep the result with `>`, and join commands with **pipes**

</div>

<div class="card card-success card-glass pad-compact">

✅ Write a **regular expression** with `[ ]`, `+`, `^`, `$` and groups, in the Find box and in the shell

</div>

<div class="card card-success card-glass pad-compact">

✅ Run a Python **script** that someone else wrote, install a program with `winget` and a package with `pip`, and give a project a **virtual environment** with `requirements.txt`

</div>

<div class="card card-success card-glass pad-compact">

✅ Show with a **checksum** that two files hold the same bytes, and keep copies by the **3-2-1** rule

</div>

<div class="card card-success card-glass pad-compact">

✅ Complete a **README**, and name the copy it means by size and SHA-256: 97 bytes, `be05af03…fff0870b`

</div>

</div>

<!--
Speaker: one line per section of the lecture. The four hand edits of
Lecture 2 became one typed line, and a checksum showed that it writes the
same 97 bytes as the hands did, on macOS and on Windows. The question of the
opening, which of four copies the README means, is answered by the last
line: its size and its SHA-256. (~1 min)
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
  question="The terminal is in analysis-project/results. Which path names the raw pendulum file, in zsh and in PowerShell alike?"
  :options="[
    '<code>data/raw/pendulum.csv</code>',
    '<code>../data/raw/pendulum.csv</code>',
    '<code>/data/raw/pendulum.csv</code>',
    '<code>~/data/raw/pendulum.csv</code>'
  ]"
  :correct="1"
  explanation="A relative path starts at the folder the terminal is in. Two points go up one level, from results to analysis-project, and from there the path goes down into data and raw. Both shells read it, and PowerShell also takes backslashes. A path that starts with a slash starts at the top of the disk, and the tilde stands for the home folder."
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
  explanation="A single > empties the file first, so the five lines are gone, and >> adds a second line. The letters are 4 + 7 = 11. zsh ends each line with LF, one byte: 13 bytes. PowerShell on Windows ends each line with CRLF, two bytes: 15 bytes. The same two lines make two different files."
/>

---
hideInToc: true
---

<MCQ
  question="In PowerShell, `Get-ChildItem data/raw | Sort-Object Length` lists pendulum.csv (130 bytes) before D0_KPi.csv. What does the pipe carry?"
  :options="[
    'File objects, each with properties such as Name and Length',
    'Lines of text, in which Sort-Object finds the size as the fifth word',
    'The bytes of the two files',
    'Only the two names, and Sort-Object opens each file to measure it'
  ]"
  :correct="0"
  explanation="A PowerShell pipe carries objects. Get-ChildItem hands on two file objects, and Sort-Object reads the property Length of each. A zsh pipe carries lines of text: ls -l data/raw | sort -n -k5 has to find the size as the fifth word of each line."
/>

---
hideInToc: true
---

<MCQ
  question="A file has four lines: 20,9.02 and 100,20.01 and length_cm,t10_s and 7;80;17,90. Which lines does the pattern `^[0-9]+,[0-9]+\.[0-9]+$` find?"
  :options="[
    'All four lines',
    'The lines 20,9.02 and 100,20.01',
    'Only the line 20,9.02',
    'The lines 20,9.02 and 100,20.01 and 7;80;17,90'
  ]"
  :correct="1"
  explanation="The pattern fits a whole line that is a number, a comma, a number, a point and a number. The header line has letters. The line with semicolons has no point, and it does not start with a number followed by a comma. The plus sign lets the first number have two digits or three. grep -E, Select-String and the Find box of VS Code find the same two lines."
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
  question="On a Mac, `shasum -a 256 pendulum.csv` prints be05af03…fff0870b. On Windows, `Get-FileHash pendulum.csv` prints BE05AF03…FFF0870B. What follows?"
  :options="[
    'Nothing, because the two programs compute different checksums',
    'The two files hold the same values, but their line endings may differ',
    'The two files hold the same 97 bytes',
    'The Windows file is larger, because of CRLF'
  ]"
  :correct="2"
  explanation="Get-FileHash computes SHA-256 too and writes the hex digits in capitals: the digits are the same. A checksum is computed from every byte, so the line endings count. The same table with CRLF line endings has 107 bytes and the checksum c06d1344…, not be05af03…."
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
  explanation="The shell goes through PATH from left to right and runs the first program of that name it finds. The order of the folders decides, and a newer version further down the list is never reached. That is why the Python installer puts its folder in front, and why a stand-in python.exe in a folder listed earlier answers in its place."
/>

---
hideInToc: true
---

<MCQ
  question="A colleague receives the project folder without .venv. requirements.txt holds the line numpy==2.5.4. Which lines give them the same environment?"
  :options="[
    '<code>pip install numpy</code>, nothing else',
    'Copy the .venv folder from your laptop into theirs',
    '<code>python -m venv .venv</code>, activate it, then <code>python -m pip install -r requirements.txt</code>',
    'Open requirements.txt in VS Code: the packages install themselves'
  ]"
  :correct="2"
  explanation="A virtual environment is made on the laptop it runs on, with one line, and filled from the file. The -r reads every line of requirements.txt, and the == pins the version, so numpy 2.5.4 arrives and not the newest one. A copied .venv holds paths of the other laptop and a Python built for it. pip install numpy without the file installs whatever version is newest that day."
/>
