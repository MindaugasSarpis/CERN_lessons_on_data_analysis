# Seminar 4 — Work on Files from the Shell

**Paired lecture:** 04 Command Line & File Handling · **Format:** follow-along · **~120 min**
in class, 30 min at home

The seminar has five parts, in this order.

1. **One shell for the room.** Windows laptops switch the terminal of VS Code
   to Git Bash. Then files and folders are made, copied, renamed and deleted
   by command.
2. **Pipes on the data file.** The room counts, sorts and filters
   `D0_KPi.csv`, finds the mark for a missing value, and gets a histogram of
   the mass column out of five small programs.
3. **Patterns.** A regular expression in the Find box of VS Code, and the
   same patterns with `grep -E`.
4. **A first script.** The hand cleaning of Seminar 1 becomes one line, the
   line becomes a script, and a checksum shows that the script writes the
   same file on every laptop.
5. **The README, completed.** Columns and units, how to rebuild, a list of
   checksums, the licence.

Everything is typed in the terminal of VS Code, in the project folder of
Seminars 1 and 3. Python is used once, to run a script that is handed out.
Nobody writes Python today, and Git is not used.

## How to use this page

This page is written for the person at the front. Students can follow the
same page.

- The **paragraph at the top of a section** is what to tell the room.
- The **numbered steps** are what to do on the projector. The room repeats
  each step on their own laptops.
- **You should now see** closes a section. Ask for hands: "who sees this?"
  Go on when about four in five have it. The rest get help from a neighbour.
- **Watch for** is the usual slip in that section.

Commands are the same on Windows, macOS and Linux unless the step gives two
forms. Keys are written for Windows, with macOS in brackets. In the blocks,
a line is typed as it stands and ended with Enter. Output is shown under
"You should now see" or beside the step. macOS puts spaces in front of the
numbers that `wc` prints, and Git Bash does not.

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · One shell for the room** · 20 min | |
| 0:00 | [1. Switch to Git Bash](#shell) | The same kind of prompt on every laptop |
| 0:08 | [2. Files and folders by command](#files) | A folder made, filled, and deleted again |
| | **Part 2 · Pipes on the data file** · 35 min | |
| 0:20 | [3. Look and count](#count) | 91 584 lines and line 5000, by command |
| 0:28 | [4. Columns and order](#sort) | The smallest and largest mass |
| 0:38 | [5. Count repeats, keep lines](#grep) | The mark `-100.0` found, and `D0_valid.csv` |
| 0:48 | [6. A histogram from five programs](#histogram) | `results/mass_bins.txt` |
| | **Part 3 · Patterns** · 20 min | |
| 0:55 | [7. A regular expression in the Find box](#regex) | The raw table cleaned with four replacements |
| 1:05 | [8. The same patterns with grep](#grep-e) | Four far rows found by line number |
| | **Part 4 · A first script** · 25 min | |
| 1:15 | [9. From one line to a script](#script) | `scripts/clean_pendulum.sh` and its output |
| 1:30 | [10. Compare by checksum, run a Python script](#checksum) | One checksum in the whole room, two means |
| | **Part 5 · The README, completed** · 20 min | |
| 1:40 | [11. Complete the README](#readme) | Columns, how to rebuild, checksums, licence |
| 1:55 | [12. Wrap up](#wrap-up) | The homework known |

In a 90-minute slot, leave out sections 6 and 8 and stop after section 10.
Section 11 is then done at home. Every part starts from files the room
already has.

## Prerequisites

For the room: the project folder of [Seminar 1](seminar_01.md) and
[Seminar 3](seminar_03.md), with `data/raw/D0_KPi.csv`,
`data/raw/pendulum.csv`, `data/processed/pendulum.csv` and `README.md`.
Python and Git installed at home, as in
[Install Python and Git](install_python_git.md). On Windows, Git Bash came
with Git.

For you, before the session:

- All sections done once on your own laptop, and sections 1, 9 and 10 once
  on a Windows laptop with Git Bash if you can borrow one.
- [`column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" }
  on a USB stick, with the installers of Git and Python.
- The lecture slide *Keys That Save Typing* ready to put on the projector.

## Part 1 · One shell for the room { #part-1 }

**0:00 to 0:20 · sections 1 and 2**

The room ends this part with the same shell on every laptop, and has made
and deleted a folder without touching the Side Bar.

## 1. Switch to Git Bash { #shell }

**0:00 · 8 min**

In Seminar 3 the terminal on Windows was PowerShell. It has its own names
for most commands, so from today Windows uses Git Bash, which reads the same
commands as the terminal of macOS and Linux. The change is made once. On
macOS and Linux nothing changes.

1. Open the project folder in VS Code.

2. **Windows only.** Press `Ctrl+Shift+P`, type `default profile` and select
   **Terminal: Select Default Profile**. In the list select **Git Bash**.

3. If a terminal is open, close it with the bin icon at the top right of the
   Panel. Then select **Terminal** > **New Terminal**.

4. Read the name at the top right of the Panel. It is `bash` on Windows and
   `zsh` on macOS.

5. Type the two commands of Seminar 3.

    ```text
    pwd
    ls
    ```

    `pwd` prints the project folder: `/c/Users/...` in Git Bash, `/Users/...`
    on macOS. `ls` prints `data`, `results`, `scripts` and `README.md`.

6. Check that Python answers. It is used once today.

    ```text
    Windows, Linux    python --version
    macOS             python3 --version
    ```

You should now see a prompt that ends in `$` or `%` on every laptop, in the
project folder, and a line that starts with `Python 3`.

From here on the terminal stays in the project folder. Every path on this
page starts there.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | **Git Bash** is not in the list | Git is not installed, or VS Code was open while it was installed. Close VS Code and start it again. If it is still missing, the student works with a neighbour today and installs Git at home |
    | The name still reads `powershell` | The old terminal is still open. Close it with the bin icon and open a new one |
    | `pwd` shows another folder | VS Code has a single file open. **File** > **Open Folder...** |
    | Windows: `python` opens the Microsoft Store, or is not found | Try `py --version`. The student uses `py` in place of `python` today |

## 2. Files and folders by command { #files }

**0:08 · 12 min**

Everything the Side Bar does with files can be typed. The room makes a
folder, copies a file into it twice, renames one copy and deletes it all
again. Keep the Side Bar in view: it shows the same disk.

1. Make a folder and copy the raw pendulum table into it.

    ```text
    mkdir scratch
    cp data/raw/pendulum.csv scratch
    ls scratch
    ```

    `ls` prints `pendulum.csv`. The folder is in the Side Bar as well.

2. Copy the file again under another name, then rename the copy.

    ```text
    cp data/raw/pendulum.csv scratch/pendulum_copy.csv
    mv scratch/pendulum_copy.csv scratch/table.csv
    ls scratch
    ```

    `ls` prints `pendulum.csv` and `table.csv`.

3. Name both files with one pattern.

    ```text
    echo scratch/*.csv
    wc -l scratch/*.csv
    ```

    `echo` prints `scratch/pendulum.csv scratch/table.csv`: the shell has
    replaced the pattern by the names that fit. `wc -l` counts 11 lines in
    each file and 22 in total.

4. Type a long path with few keys: `wc -l da`, then `Tab`, `r`, `Tab`, `D`,
   `Tab`, Enter. The line reads `wc -l data/raw/D0_KPi.csv` and prints
   91584.

5. Delete one file, then try to delete the folder.

    ```text
    rm scratch/table.csv
    rmdir scratch
    ```

    `rmdir` answers `Directory not empty` and deletes nothing.

6. Delete the folder with what is left in it. Say the name of the folder
   aloud before pressing Enter.

    ```text
    rm -r scratch
    ls
    ```

You should now see `data`, `results`, `scripts` and `README.md`, and no
`scratch`.

Say it in these words: `cp`, `mv` and `rm` print nothing when they work, and
`rm` has no Recycle Bin. Before `rm`, run `ls` with the same path and read
what will go.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `No such file or directory` | The path is mistyped, or the terminal is not in the project folder. Run `pwd`, then complete the path with `Tab` |
    | `wc -l` counts 10 lines, not 11 | The raw file has no line break after its last line. `wc -l` counts line breaks. Both numbers are right |
    | A student ran `rm -r` on `data` | Download the files again from Seminar 1, sections 7 and 10. Nothing else can bring them back |

## Part 2 · Pipes on the data file { #part-2 }

**0:20 to 0:55 · sections 3 to 6**

The room asks `D0_KPi.csv` four questions. Each answer is one line of small
programs joined by `|`. Build every line stage by stage: run it, read the
output, press `↑`, add the next stage.

## 3. Look and count { #count }

**0:20 · 8 min**

The numbers of this section are known: the room found them by hand in
Seminars 1 and 3. Now each has a command that can be written down.

1. Print the first and the last lines.

    ```text
    head -n 3 data/raw/D0_KPi.csv
    tail -n 2 data/raw/D0_KPi.csv
    ```

    `head` prints the header and two rows. The last line of the file is
    `1911.2631,2543.4617,0.00017650973,8.169813`.

2. Count the lines, then the bytes.

    ```text
    wc -l data/raw/D0_KPi.csv
    wc -c data/raw/D0_KPi.csv
    ```

    91584 lines and 3926142 bytes.

3. Print line 5000. The first program hands 5000 lines to the second, and
   the second keeps the last of them.

    ```text
    head -n 5000 data/raw/D0_KPi.csv | tail -n 1
    ```

    It prints `1868.8636,5537.248,0.0007151779,10.399748`.

4. Print the whole file with `cat data/raw/D0_KPi.csv` and stop it with
   `Ctrl+C`.

You should now see the prompt again, and the room can say three numbers:
91 584 lines, 3 926 142 bytes, and the mass on line 5000.

## 4. Columns and order { #sort }

**0:28 · 10 min**

`cut` takes a column out of the table and `sort` orders it. The two ends of
a sorted column are the first place to look for a wrong value.

1. Take the first column.

    ```text
    cut -d, -f1 data/raw/D0_KPi.csv | head -n 3
    ```

    It prints `M`, `1880.649` and `1860.6599`. The header is a line like any
    other.

2. Drop the header first: `tail -n +2` prints from line 2 on.

    ```text
    tail -n +2 data/raw/D0_KPi.csv | cut -d, -f1 | head -n 3
    ```

3. Sort the small table as text, then as numbers.

    ```text
    tail -n +2 data/processed/pendulum.csv | sort | head -n 3
    tail -n +2 data/processed/pendulum.csv | sort -n | head -n 3
    ```

    The first command begins with `100,20.01`, as the editor did in
    Seminar 1. The second begins with `20,9.02`.

4. Sort the mass column and look at its low end.

    ```text
    tail -n +2 data/raw/D0_KPi.csv | cut -d, -f1 | sort -n | head -n 2
    ```

    It prints `1766.2096` and `1808.1385`.

5. Press `↑` and change the last `head` to `tail`. The high end is
   `1920.3453` and `2453.6584`.

6. The room does this step alone: the smallest and the largest value of
   `PT`, which is field 2. The answers are `755.2686` and `64509.95`.

You should now see the two ends of two columns on the board: `M` from
1766.2096 to 2453.6584, `PT` from 755.2686 to 64509.95.

Ask what is odd about the mass column. The second value from each end is
1808 and 1920: one row at each end lies far from all the others. Section 8
finds these rows.

!!! warning "Watch for"
    A laptop whose language is set to Lithuanian reads the comma as the
    decimal sign, and `sort -n` then misplaces numbers with a point. The
    two columns of this section come out right all the same. If a sorted
    column looks wrong, write `LC_ALL=C sort -n` in place of `sort -n`.

## 5. Count repeats, keep lines { #grep }

**0:38 · 10 min**

`sort | uniq -c` counts how often each value occurs. A measured value almost
never occurs twice. A value that occurs many times is a mark, and `grep`
then keeps or drops the lines that carry it.

1. Count the repeats in the decay time, field 3, and show the three most
   frequent values.

    ```text
    cut -d, -f3 data/raw/D0_KPi.csv | sort | uniq -c | sort -n | tail -n 3
    ```

    ```text
       2 0.0026546149
       2 0.0035111452
      49 -100.0
    ```

2. Count the lines that carry the mark. The pattern has the comma in front
   and stands in single quotes.

    ```text
    grep -c ',-100' data/raw/D0_KPi.csv
    ```

    49, the number found with `Ctrl+F` in Seminar 1.

3. Show the first two of them with their line numbers.

    ```text
    grep -n ',-100' data/raw/D0_KPi.csv | head -n 2
    ```

    Lines 343 and 965. Open the file in the editor, press `Ctrl+G`, type
    `343` and check.

4. Write every line **without** the mark into a new file. `-v` turns the
   choice round, and `>` sends the output into a file.

    ```text
    grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv
    wc -l data/processed/D0_valid.csv
    ```

    91535 lines: 91 584 less 49.

5. Check the new file: `grep -c ',-100' data/processed/D0_valid.csv` prints
   0.

You should now see `D0_valid.csv` in `data/processed`, with 91 535 lines.

Say it in these words: the raw file was read and not changed. The new file
can be deleted and made again with one line, and that line says exactly
what was done.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The terminal waits and prints nothing | The pattern was typed as `-100` without the comma, and `grep` took it for an option. Press `Ctrl+C` |
    | `uniq -c` prints thousands of lines of `1` | `sort` is missing before `uniq`. `uniq` only merges lines that stand next to each other |
    | `D0_valid.csv` is empty | The line had `> data/raw/...` or the same file on both sides. Check that `D0_KPi.csv` still has 91 584 lines |

## 6. A histogram from five programs { #histogram }

**0:48 · 7 min**

Every mass in the file has four digits before the point. Its first three
characters therefore say in which step of 10 MeV/c² it lies: `186` stands
for 1860 to 1869.99. Counting how often each of them occurs gives a
histogram.

1. Start with the mass column, without the header.

    ```text
    tail -n +2 data/raw/D0_KPi.csv | cut -d, -f1 | head -n 3
    ```

2. Press `↑` and put `cut -c1-3 |` before `head`. The output is `188`,
   `186`, `191`.

3. Replace `head -n 3` by `sort | uniq -c`.

    ```text
    tail -n +2 data/raw/D0_KPi.csv | cut -d, -f1 | cut -c1-3 |
      sort | uniq -c
    ```

    A line that ends in `|` goes on in the next line.

4. Press `↑` and add `> results/mass_bins.txt` at the end. Then
   `cat results/mass_bins.txt`.

You should now see 15 lines in `results/mass_bins.txt`:

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

Read it with the room. The counts rise to 17 496 between 1860 and 1870: the
D⁰, whose mass is 1865 MeV/c². Away from the peak about 7000 rows fall into
each step. Four rows lie outside 1810 to 1920.

## Part 3 · Patterns { #part-3 }

**0:55 to 1:15 · sections 7 and 8**

So far Find and `grep` looked for a fixed text. A regular expression
describes a kind of text: a number, a comma between two digits, a line that
starts with a semicolon.

## 7. A regular expression in the Find box { #regex }

**0:55 · 10 min**

The room cleans the raw pendulum table a second time, on a new copy. In
Seminar 1 this took a cursor on every line and two replacements in the right
order. With patterns it takes four replacements, and their order is free.

1. Make a copy to work on, and open it in the editor.

    ```text
    cp data/raw/pendulum.csv data/processed/pendulum_regex.csv
    ```

2. Press `Ctrl+H` (macOS `Cmd+Option+F`). Switch on the button `.*` at the
   right end of the **Find** box, or press `Alt+R` (macOS `Cmd+Option+R`).

3. Build a pattern for the first column in four steps. Type each one and
   read the counter.

    | Find | Matches | What it fits |
    |--|--|--|
    | `[0-9]+` | 39 | Every number |
    | `[0-9]+;` | 18 | A number in front of a `;` |
    | `^[0-9]+;` | 9 | The first of them in a line: the row number |
    | `^(nr|[0-9]+);` | 10 | The row number, or `nr` in the header line |

4. Leave **Replace** empty and select **Replace All**. The first column is
   gone from the header and from the nine rows.

5. Type `([0-9]),([0-9])` into **Find**. The counter ends in `of 10`. Type
   `$1.$2` into **Replace** and select **Replace All**. Every decimal comma
   is now a point, and every semicolon is where it was.

6. Click in the line `;mean;15.14` and delete it with `Ctrl+Shift+K` (macOS
   `Cmd+Shift+K`).

7. Type `;` into **Find** and `,` into **Replace**. The counter ends in
   `of 10`. Select **Replace All**, close the boxes with `Esc` and save.

8. Compare the result with the file cleaned by hand in Seminar 1.

    ```text
    diff data/processed/pendulum.csv data/processed/pendulum_regex.csv
    ```

You should now see no output from `diff`: the two files are the same, line
for line. The new file begins with `length_cm,t10_s` and `20,9.02`.

Say why the order is free now. `([0-9]),([0-9])` fits a comma only between
two digits, so it cannot touch a comma that separates two values.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The counter says `No results` for `[0-9]+` | The button `.*` is off |
    | `$1.$2` appears in the file as text | The button `.*` was switched off before **Replace All**. `Ctrl+Z`, switch it on, replace again |
    | `diff` prints lines | The two files differ. A last line `\ No newline at end of file` means that one of them has no line break after `100,20.01`. Any other line is a real difference: read it |

## 8. The same patterns with grep { #grep-e }

**1:05 · 10 min**

`grep -E` reads the same patterns as the Find box. The pattern stands in
single quotes, because the shell would otherwise read `*`, `[`, `$` and `|`
itself.

1. Count the lines of the raw table that have a decimal comma, and print
   the line that starts with a semicolon.

    ```text
    grep -cE '[0-9],[0-9]' data/raw/pendulum.csv
    grep -E '^;' data/raw/pendulum.csv
    ```

    10, and `;mean;15,14`.

2. Count the lines that contain `1865`, then those that start with it.

    ```text
    grep -c 1865 data/raw/D0_KPi.csv
    grep -c '^1865' data/raw/D0_KPi.csv
    ```

    1986 and 1846. In 140 lines `1865` stands inside another number.

3. Count the rows with a mass from 1850 to 1880.

    ```text
    grep -cE '^18[5-7]' data/raw/D0_KPi.csv
    ```

    41091, which is 45% of the file.

4. Find the rows outside 1810 to 1920, with their line numbers.

    ```text
    grep -nE '^(17|180|19[2-9]|2)' data/raw/D0_KPi.csv
    ```

    ```text
    10048:2453.6584,755.2686,0.2276815,1.0500937
    43608:1808.1385,3632.4104,0.06656479,11200.344
    67877:1920.3453,4999.695,0.00015124853,1.0319226
    89861:1766.2096,12493.022,0.0037266747,214.38336
    ```

5. The room does this step alone: the number of rows with a mass from 1860
   to 1870. The answer is `grep -c '^186' data/raw/D0_KPi.csv`, which prints
   17496, the highest count of the histogram.

You should now see four lines with their numbers. These are the four far
values of sections 4 and 6. The row with the largest mass, line 10048, is
also the row with the smallest `PT`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | macOS: `no matches found` | The quotes round the pattern are missing, and the shell read the square brackets as a wildcard |
    | Git Bash, Linux: a pattern with `\d` finds nothing | `grep` there does not read `\d` as a digit. Write `[0-9]` |
    | Windows: a pattern that ends in `$` finds nothing in a file made in VS Code | The file has CRLF line endings, and the byte `0D` stands before each line break. `D0_KPi.csv` has LF and is not affected |

## Part 4 · A first script { #part-4 }

**1:15 to 1:40 · sections 9 and 10**

The README of Seminar 1 says what was done to the pendulum table by hand:
mean line deleted, `,` replaced by `.`, `;` replaced by `,`, column `nr`
deleted. Each of these edits is one small program. The room joins them and
keeps the line in a file.

## 9. From one line to a script { #script }

**1:15 · 15 min**

`grep -v` drops the line with the mean. `tr` replaces one character by
another, and `tr -d` deletes one. `cut` keeps fields 2 and 3. The order is
the order of Seminar 1: the decimal comma becomes a point while it is the
only comma.

1. Build the line stage by stage, with `↑`. Read the last rows after each
   stage.

    ```text
    grep -v mean data/raw/pendulum.csv
    grep -v mean data/raw/pendulum.csv | tr ',' '.'
    grep -v mean data/raw/pendulum.csv | tr ',' '.' | tr ';' ','
    ```

    The last row changes from `9;100;20,01` to `9;100;20.01` and then to
    `9,100,20.01`.

2. Add `| cut -d, -f2,3` at the end. The last row is `100,20.01`, and the
   output is the cleaned table.

3. Select the `scripts` folder in the Side Bar, then **New File**, and type
   `clean_pendulum.sh`.

4. **Before typing**, look at the right end of the Status Bar. If it reads
   `CRLF`, select it and choose **LF**. A script has LF line endings on
   every system.

5. Type the script and save it.

    ```text
    #!/usr/bin/env bash
    # clean_pendulum.sh: the hand edits of Seminar 1, as commands.
    # Run from the project folder:  bash scripts/clean_pendulum.sh

    raw=data/raw/pendulum.csv
    out=data/processed/pendulum_script.csv

    grep -v mean "$raw" | tr -d '\r' | tr ',' '.' | tr ';' ',' |
      cut -d, -f2,3 > "$out"
    ```

    Say what is new in it. A line that starts with `#` is a comment. Line 1
    names the program that reads the file. `raw` and `out` are variables:
    `name=value` without spaces, and `"$name"` puts the value back in.
    `tr -d '\r'` deletes the byte `0D`, so that the output has LF line
    endings also when the raw file was made on Windows.

6. Run the script, then look at what it wrote.

    ```text
    bash scripts/clean_pendulum.sh
    cat data/processed/pendulum_script.csv
    wc -c data/processed/pendulum_script.csv
    ```

You should now see no output from the script itself, the table of ten lines
from `cat`, and 97 bytes on every laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `$'\r': command not found`, or a syntax error in a line that looks right | The script has CRLF line endings. Select `CRLF` in the Status Bar, choose **LF**, save, run again. Delete a file in `data/processed` whose name ends in a strange sign |
    | `No such file or directory` | The terminal is not in the project folder, or a path in the script is mistyped |
    | `raw: command not found` | There is a space before or after the `=` |
    | The size is not 97 bytes | The raw file is not the block of Seminar 1. Compare it with [`pendulum_raw.csv`](../data/pendulum_raw.csv) |

## 10. Compare by checksum, run a Python script { #checksum }

**1:30 · 10 min**

A checksum is computed from every byte of a file. Two files with the same
checksum are the same, byte for byte. The room uses it to compare the
script's output across all laptops, and then runs a program that was handed
out.

1. Compute the checksum of the file the script wrote.

    ```text
    macOS             shasum -a 256 data/processed/pendulum_script.csv
    Git Bash, Linux   sha256sum data/processed/pendulum_script.csv
    ```

    Read the first eight digits aloud: `be05af03`. The last eight are
    `aff0870b`. Ask who has other digits.

2. Compute the checksum of the file cleaned by hand, with `↑` and the name
   changed to `pendulum.csv`. Ask who has `be05af03` again.

    Some have, some have not. The files cleaned by hand have 96, 97, 105 or
    107 bytes, as Seminar 3 found: the line ending and the last line break
    differ. The script writes the same 97 bytes on every system.

3. Download
   [`column_stats.py`](../data/cli_column_stats.py){ download="column_stats.py" }
   and drag it from **Downloads** onto the `scripts` folder. Do not open it.

4. Run it on the raw file, for the column `TAU`.

    ```text
    Windows, Linux   python scripts/column_stats.py data/raw/D0_KPi.csv TAU
    macOS            python3 scripts/column_stats.py data/raw/D0_KPi.csv TAU
    ```

    ```text
    file    data/raw/D0_KPi.csv
    column  TAU
    rows    91583
    min     -100.0
    max     0.5787994
    mean    -0.0525221
    ```

5. Press `↑` and change the path to `data/processed/D0_valid.csv`. The mean
   is now `0.000981802`, and the smallest value `-0.13715266`.

You should now see two means on the board: −0.0525 ns with the 49 marked
rows, +0.00098 ns without them.

Say it in these words: 49 rows of 91 583 are 0.05% of the file, and they
give the mean decay time the wrong sign. A mark for "no value" that is
written as a number is counted as a number by every program. That is why
the marked rows were taken out in section 5, by a line that is written down.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The checksum of `pendulum_script.csv` differs from `be05af03…` | The raw file or the script differs from this page. `diff` against a neighbour's output shows where |
    | `no column tau` | Column names are written as in the header: `TAU` |
    | The file is named `column_stats (1).py` | It was downloaded twice. Delete both and download once |

## Part 5 · The README, completed { #part-5 }

**1:40 to 2:00 · sections 11 and 12**

## 11. Complete the README { #readme }

**1:40 · 15 min**

The README says where the data came from and what the files look like. A
stranger still cannot tell what the columns mean, whether the raw files are
intact, or how the files in `data/processed` were made. The room adds these
parts, and each of them comes from a command of today.

1. Write a list of checksums for the raw files, and check it at once.

    ```text
    macOS             shasum -a 256 data/raw/* > data/checksums.txt
                      shasum -a 256 -c data/checksums.txt
    Git Bash, Linux   sha256sum data/raw/* > data/checksums.txt
                      sha256sum -c data/checksums.txt
    ```

    The check prints one line per file, each ending in `OK`. The line for
    `D0_KPi.csv` in `data/checksums.txt` starts with `25c3c972` on every
    laptop.

2. Open `README.md` and the preview (`Ctrl+K`, then `V`). Add a section on
   the columns under **Data**.

    ```text
    ## Columns of `D0_KPi.csv`

    | Column | Meaning | Unit |
    |--|--|--|
    | `M` | mass of the K⁻π⁺ pair | MeV/c² |
    | `PT` | transverse momentum | MeV/c |
    | `TAU` | decay time | ns |
    | `IPCHI2` | χ² of the impact parameter | none |

    Missing value: `TAU` is `-100.0` in 49 rows.
    ```

3. Add a section that says how every file in `data/processed` and `results`
   is made. Copy each command from the terminal, do not retype it.

    ```text
    ## How to rebuild

    Run in the project folder, in Git Bash (Windows) or in the
    terminal (macOS, Linux).

    1. `bash scripts/clean_pendulum.sh`
       writes `data/processed/pendulum_script.csv`
    2. `grep -v ',-100' data/raw/D0_KPi.csv > data/processed/D0_valid.csv`
       leaves out the 49 rows without a decay time
    3. `sha256sum -c data/checksums.txt`
       checks the raw files (macOS: `shasum -a 256 -c data/checksums.txt`)
    ```

4. Add the licence. The data keeps the licence of its record. The scripts
   and the text are the student's own.

    ```text
    ## Licence

    Data: CC0, CERN Open Data Portal, record 401.
    Scripts and text: MIT.
    ```

5. Test the section **How to rebuild**. Delete the two files, then copy
   commands 1 and 2 out of the preview into the terminal.

    ```text
    rm data/processed/pendulum_script.csv data/processed/D0_valid.csv
    ```

6. Compute the checksum of `data/processed/pendulum_script.csv` again, as in
   section 10.

You should now see `be05af03…` again, 91 535 lines in `D0_valid.csv`, and
three new sections in the preview of the README.

Say it in these words: the entry "Mean line deleted, `,` replaced by `.`"
described the work. The new section is the work itself, as lines that run.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The check prints `FAILED` for a file | The file changed after the list was written. If the list is seconds old, the file is open in a spreadsheet or was saved by one |
    | The table shows as text with `|` signs | An empty line is missing before the table, or the line `|--|--|--|` is missing |
    | `rm` reports a missing file | It was deleted before. Go on with the next step |

## 12. Wrap up { #wrap-up }

**1:55 · 5 min**

Put the tasks of the next section on the projector and read them aloud. Ask
on the way out which step was hardest.

What the room has learned:

- Git Bash on Windows and the terminal of macOS and Linux read the same
  commands.
- `mkdir`, `cp`, `mv` and `rm` do what the Side Bar does. `rm` has no
  Recycle Bin.
- A wildcard is replaced by the shell with the names that fit.
- `head`, `tail`, `wc`, `cut`, `sort`, `uniq -c`, `grep` and `tr` each do
  one thing to lines of text. A pipe joins them.
- The ends of a sorted column and the count of repeated values find a wrong
  value and a mark for a missing one.
- A regular expression describes a kind of text. `[0-9]`, `+`, `^`, `$` and
  groups in `( )` work in the Find box and in `grep -E`.
- A script is a text file of commands, saved with LF and run with `bash`.
- A checksum shows whether two files are the same, on one laptop or across
  the room.
- Commands read from `data/raw` and write to `data/processed` or `results`.
- The README lists the commands that make every processed file.

## Next steps, at home

**30 min, before the next session**

1. **Your own dataset.** Print its first lines with `head`, count its lines
   with `wc -l`, and find the smallest and the largest value of one numeric
   column with `cut`, `sort -n`, `head` and `tail`. If the file has `;`
   between the values, the option is `-d';'`.

2. Look for a mark for a missing value: run `sort | uniq -c | sort -n |
   tail -n 3` on a numeric column. Write into the README what you found,
   also if it is nothing.

3. Write `scripts/clean_mydata.sh`, with your own name for it: one pipeline
   that reads your file in `data/raw` and writes a file to `data/processed`.
   Dropping lines with `grep -v` or keeping some columns with `cut` is
   enough.

4. Add your dataset to the README: its columns and units, the command that
   runs your script under **How to rebuild**, and a new
   `data/checksums.txt` that includes it.

5. Copy the project folder to a second place: a USB drive or the storage of
   the university. Run the check of `data/checksums.txt` on the copy.

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Add `| sort -n -r | head -n 3` to the pipeline of section 6 before the
  `>`. The answer is the three fullest steps: `17496 186`, `12207 185`,
  `11388 187`.
- Count how many different values the column `TAU` has:
  `tail -n +2 data/raw/D0_KPi.csv | cut -d, -f3 | sort | uniq | wc -l`. The
  answer is 91344 for 91 583 rows.
- Two rows of the file write a number with an exponent. Find their line
  numbers with `grep -n 'e-' data/raw/D0_KPi.csv`. The answer is lines 40769
  and 44745, with `1.3600341e-05` and `9.40878e-05` in the last column.
- Type the script `ranges.sh` from the lecture slide into `scripts` and run
  `bash scripts/ranges.sh data/raw/D0_KPi.csv`. The answer is twelve lines:
  `M` 1766.2096 and 2453.6584, `PT` 755.2686 and 64509.95, `TAU` -100.0 and
  0.5787994, `IPCHI2` 1.3600341e-05 and 891711.06.
- After the marked rows are gone, three rows still have a negative decay
  time. Show them with `grep ',-0' data/raw/D0_KPi.csv`. The answer is three
  rows with `TAU` of -0.137, -0.059 and -0.098. They are not marks.
- Find every file of the project that is larger than 1 MB with
  `find . -size +1M`. The answer is `D0_KPi.csv` and `D0_valid.csv`, and
  the student's own dataset if it is large.
- Add a file `LICENSE` to the project folder with the text of the MIT
  licence from [choosealicense.com](https://choosealicense.com/licenses/mit/),
  with the year and the student's name filled in.

## If students ask for more

| Topic | Week |
|--|--|
| Keeping older versions of the scripts and the README | 5 (Version Control with Git) |
| Writing a program like `column_stats.py` | 6 and 7 (Python) |
| Plotting the histogram of section 6 | 8 (Data Visualisation) |
| Cleaning a table with a program, not with `tr` and `cut` | 12 (Pandas & Data Cleaning) |
| One command that rebuilds everything | 13 (Reproducible Workflows) |

Leave out altogether, even if asked: `awk`, `vim`, aliases, the shell's
start-up files, remote login.

## Aims practised

⚙️ a step typed once and run again · 📁 raw data read, never written · 🔧 one set of commands on every system · ♻️ a README that rebuilds the files
