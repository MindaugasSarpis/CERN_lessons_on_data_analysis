# Seminar 3 — A File as Bytes

**Paired lecture:** 03 How Computers Work · **Format:** follow-along · **~120 min**
in class

The seminar has four parts, in this order.

1. **Three terminal commands.** The room opens the terminal inside VS Code
   and learns `pwd`, `ls` and `cd`. `ls` gives the size of a file in bytes,
   which the rest of the session needs.
2. **Text as bytes.** A file of four characters is measured, read with the
   wrong encoding, and opened as bytes.
3. **A data file as bytes.** The same view on the two data files of the
   project: separators, line endings, size per row.
4. **A note in the README.** What was found is written down.

The new tool of the session is the terminal, with three commands. Everything
else is VS Code from Seminar 1. No Python and no Git are needed.

## How to use this page

This page is written for the person at the front. Students can follow the
same page.

- The **paragraph at the top of a section** is what to tell the room.
- The **numbered steps** are what to do on the projector. The room repeats
  each step on their own laptops.
- **You should now see** closes a section. Ask for hands: "who sees this?"
  Go on when about four in five have it. The rest get help from a neighbour.
- **Watch for** is the usual slip in that section.

Keys are written for Windows, with macOS in brackets. Where a command
differs between systems, both forms are given.

| Clock | Section | The room ends with |
|--|--|--|
| | **Part 1 · Three terminal commands** · 20 min | |
| 0:00 | [1. Open the terminal](#terminal) | A prompt in the project folder |
| 0:08 | [2. Move between folders](#cd) | The size of a file read in bytes |
| | **Part 2 · Text as bytes** · 40 min | |
| 0:20 | [3. Count the bytes of a text](#count) | A table of texts and their sizes |
| 0:35 | [4. Read the bytes with the wrong encoding](#encoding) | `ą` shown as `Ä…`, and put right |
| 0:45 | [5. Look at the bytes](#hex) | The file in the Hex Editor |
| | **Part 3 · A data file as bytes** · 40 min | |
| 1:00 | [6. A small table](#small) | Commas and line breaks found as bytes |
| 1:15 | [7. A large table](#large) | Bytes per row, and the cost of text |
| 1:30 | [8. Text or binary](#binary) | The first bytes of a picture |
| | **Part 4 · A note in the README** · 20 min | |
| 1:40 | [9. Write down what the file is](#readme) | A **File anatomy** section |
| 1:55 | [10. Wrap up](#wrap-up) | The homework known |

In a 90-minute slot, stop after section 7 and go to the wrap-up. Sections 8
and 9 are then done at home.

## Prerequisites

For the room: the project folder of [Seminar 1](seminar_01.md) with
`data/processed/pendulum.csv` and `results/pendulum_plot.png`, and
`D0_KPi.csv` in `data/raw/`. A student who does not have
[`D0_KPi.csv`](../data/D0_KPi.csv) downloads it now and drags it onto the
`raw` folder.

For you, before the session:

- Sections 3 to 5 done once on your own laptop, so that you know what your
  system writes for a line break.
- The **Hex Editor** extension installed, and the installer of VS Code on a
  USB stick for a laptop that lost it.

A student who missed Seminar 1 downloads
[`project_after_s1.zip`](../data/project_after_s1.zip), unpacks it, and
opens `analysis-project` with **File** > **Open Folder...**.

## Files for this seminar { #files }

Each file shows what a step should produce, so a student can compare their
own file with it in the terminal or in the hex view. A browser saves it under
the name in the second column.

| File | Saved as | What it is |
|--|--|--|
| [`bytes_utf8.txt`](../data/bytes_utf8.txt){ download="bytes.txt" } | `bytes.txt` | Sections 3 and 5: `abcą` and LF in UTF-8, 6 bytes, `61 62 63 C4 85 0A` |
| [`bytes_1257.txt`](../data/bytes_1257.txt){ download="bytes_1257.txt" } | `bytes_1257.txt` | Section 4, step 4: the same text saved as Windows 1257, 5 bytes, `61 62 63 E0 0A` |
| [`pendulum.csv`](../data/pendulum.csv){ download="pendulum.csv" } | `pendulum.csv` | Section 6: the cleaned table with LF, 97 bytes |
| [`pendulum_crlf.csv`](../data/pendulum_crlf.csv){ download="pendulum_crlf.csv" } | `pendulum_crlf.csv` | Section 6: the same table with CRLF, 107 bytes |
| [`project_README_s3.txt`](../data/project_README_s3.txt){ download="README.md" } | `README.md` | Section 9: the README with the **File anatomy** section, for LF |
| [`project_after_s3.zip`](../data/project_after_s3.zip) | `project_after_s3.zip` | The whole `analysis-project` folder at the end of this seminar |

Open `bytes_1257.txt` in VS Code. It shows `abc` and a sign for an unknown
character, because VS Code reads it as UTF-8. **Reopen with Encoding** and
**Baltic (Windows 1257)** show `abcą`.

## Part 1 · Three terminal commands { #part-1 }

**0:00 to 0:20 · sections 1 and 2**

The terminal is a window in which commands are typed instead of clicked.
Three commands are enough today: where am I, what is here, go there.

## 1. Open the terminal { #terminal }

**0:00 · 8 min**

VS Code has a terminal built in. It opens in the project folder, so there is
nothing to find first. Everything typed here could also be done by clicking.
The difference is that a typed command can be written down and repeated.

1. Open the project folder in VS Code and select **Terminal** >
   **New Terminal**. The Panel opens at the bottom with a line that ends in
   `>` or `%` or `$`. This line is the **prompt**: the terminal waits for a
   command.

2. Type `pwd` and press Enter. The terminal prints the folder it is in. The
   name stands for *print working directory*.

3. Type `ls` and press Enter. It lists what is in that folder: `data`,
   `results`, `scripts`, `README.md`. Compare the list with the Side Bar.
   They show the same folder.

4. Press `↑`. The last command comes back. Press Enter to run it again.

5. Type `clear` and press Enter. The Panel is emptied. Nothing is deleted.

You should now see an empty Panel with a prompt, and the room can say what
`pwd` and `ls` printed.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Windows: `ls` is not recognized | The terminal is Command Prompt. Open the list beside the `+` at the top right of the Panel and select **PowerShell** |
    | The prompt shows another folder | VS Code has a single file open, not the folder. **File** > **Open Folder...** |

## 2. Move between folders { #cd }

**0:08 · 12 min**

The terminal is always in one folder. `cd` changes it. `ls` then shows the
files of that folder, and on request their size in bytes.

1. Type `cd data` and press Enter. The prompt now ends in `data`.

2. Type `cd r` and press `Tab`. The terminal completes the name to `raw`.
   Press Enter.

3. List the files with their sizes.

    ```text
    Windows          ls
    macOS, Linux     ls -l
    ```

    One line per file. The number before the date is the size in bytes:
    `3926142` for `D0_KPi.csv`.

4. Type `cd ..` and press Enter. Two dots mean the folder above. Run it a
   second time. `pwd` shows the project folder again.

5. Go straight to a folder two levels down, and back.

    ```text
    cd data/processed
    ls
    cd ../..
    ```

You should now see the project folder in `pwd`, and every student can read
the size of `D0_KPi.csv` in bytes: 3 926 142.

The file manager showed this file as about 3 835 KB on Windows and 3.9 MB on
macOS. Both are the same 3 926 142 bytes, counted in units of 1024 and of
1000. The terminal gives the number itself.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | `cd raw` says the folder does not exist | The terminal is not in `data`. Run `pwd`, then `ls`, and go one folder at a time |
    | Windows: `ls -l` prints an error | PowerShell needs `ls` alone. Its list has the size in the column **Length** |

## Part 2 · Text as bytes { #part-2 }

**0:20 to 1:00 · sections 3 to 5**

The room builds a file of a few characters and measures it after every
change. The file is a scratch file. It is deleted at the end.

## 3. Count the bytes of a text { #count }

**0:20 · 15 min**

A file is a sequence of bytes. For plain English text one character is one
byte. Other letters take more, and a line break is a byte too. The room
predicts each size before measuring it.

1. In the Side Bar select the empty area below the folders, then
   **New File**, and type `bytes.txt`.

2. Type `abc` into the file. Do not press Enter. Save with `Ctrl+S` (macOS
   `Cmd+S`).

3. In the terminal run `ls` (macOS, Linux `ls -l`) in the project folder.
   `bytes.txt` has 3 bytes.

4. Add `ą` after the `c`, save, and ask the room for the size before
   running `ls` again. It is 5 bytes: `ą` takes two.

5. Press Enter at the end of the line, save and measure again. Ask who has
   6 bytes and who has 7.

6. Look at the right end of the Status Bar. It reads `LF` on macOS and Linux
   and `CRLF` on Windows. This is the line break: one byte or two. Select
   it, choose **LF**, save and measure. Every laptop now has 6 bytes.

You should now see the same table on every laptop:

| Text in the file | Bytes | Reason |
|--|--|--|
| `abc` | 3 | One byte for each of these letters |
| `abcą` | 5 | `ą` takes two bytes in UTF-8 |
| `abcą` and a line break | 6 or 7 | LF is one byte, CRLF is two |

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The size does not change | The file was not saved. A dot on the tab means *not saved* |
    | The size is 1 or 2 bytes larger than expected | There is a space or an extra line break. Select all with `Ctrl+A` and look |

## 4. Read the bytes with the wrong encoding { #encoding }

**0:35 · 10 min**

The bytes of a text mean nothing without the table that maps bytes to
characters. That table is the encoding. VS Code names the one it used in the
Status Bar: `UTF-8`. Reading the same bytes with another table gives other
characters.

1. Select `UTF-8` in the Status Bar, then **Reopen with Encoding**, and
   choose **Baltic (Windows 1257)**. Type `1257` to find it.

2. The file now reads `abcÄ…`. The two bytes of `ą` are shown as two
   characters. Nothing in the file has changed.

3. Select the encoding in the Status Bar again, **Reopen with Encoding**,
   **UTF-8**. The text is `abcą` again.

4. Now change the bytes. Select `UTF-8`, then **Save with Encoding**, and
   choose **Baltic (Windows 1257)**. Measure the file: it has one byte less.
   In that table `ą` is a single byte.

5. Put it back: select the encoding, **Save with Encoding**, **UTF-8**.
   Measure again. The file has 6 bytes.

You should now see `abcą` and `UTF-8` in the Status Bar, and 6 bytes in the
terminal.

Say it in these words: Reopen reads the same bytes in another way and is
safe. Save writes other bytes. A file that shows `Ä…` or `Å¾` is not
broken. It was read with the wrong table, and it is reopened, not retyped.

## 5. Look at the bytes { #hex }

**0:45 · 15 min**

An editor shows characters. A hex viewer shows the bytes themselves, two hex
digits for each. VS Code gets one as an extension, a small added program.
This is the first extension of the course.

1. Select the **Extensions** icon in the Activity Bar, or press
   `Ctrl+Shift+X` (macOS `Cmd+Shift+X`). Type `hex editor` into the search
   box. Select **Hex Editor**, published by Microsoft, and then **Install**.

2. Go back to the Explorer. Right-click `bytes.txt`, select **Open With...**
   and then **Hex Editor**.

3. Read the bytes with the room.

    ```text
    61 62 63 C4 85 0A
    a  b  c  ą     line break
    ```

4. Find `a` in the ASCII table of the lecture: 97, which is `61` in hex.
   `b` and `c` follow as `62` and `63`.

5. Close the hex view. Open `bytes.txt` as text, add a second `ą`, save, and
   open the hex view again. The pair `C4 85` is there twice.

6. Delete `bytes.txt`: right-click it in the Side Bar and select **Delete**.

You should now see no `bytes.txt` in the Side Bar, and the room can say
which two bytes are `ą`.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The line break shows as `0D 0A` | The file still has CRLF. Both forms are correct |
    | **Open With...** has no Hex Editor | The extension is still installing. Wait for the **Install** button to change |

## Part 3 · A data file as bytes { #part-3 }

**1:00 to 1:40 · sections 6 to 8**

The same three tools, `ls`, the Status Bar and the hex view, are now used
on the data files of the project.

## 6. A small table { #small }

**1:00 · 15 min**

`data/processed/pendulum.csv` has ten lines. Every one of its bytes can be
accounted for: the characters of the numbers, the commas, the line breaks.

1. Open `data/processed/pendulum.csv` as text. Read the Status Bar: `UTF-8`,
   and `LF` or `CRLF`.

2. Count with the room. The ten lines hold 87 characters, 10 of them
   commas. Add one byte per line break for LF, or two for CRLF.

3. Measure the file in the terminal.

    ```text
    cd data/processed
    ls                  (macOS, Linux: ls -l)
    cd ../..
    ```

    | The file has | Bytes |
    |--|--|
    | LF, and a line break after the last line | 97 |
    | LF, no line break after the last line | 96 |
    | CRLF, and a line break after the last line | 107 |
    | CRLF, no line break after the last line | 105 |

4. Open the file in the hex view. Find the first comma, `2C`, and the first
   line break, `0A` or `0D 0A`.

5. Ask what share of the file is structure and not data. With LF it is 10
   commas and 10 line breaks: 20 bytes of 97, about one fifth.

You should now see one of the four sizes on every laptop, and each student
can say which of the four cases their file is.

The table of numbers is the same on every laptop and the files differ by up
to 11 bytes. That is why two copies of a file are compared by their bytes
and not by how they look.

## 7. A large table { #large }

**1:15 · 15 min**

`D0_KPi.csv` cannot be counted by hand, and it does not need to be. Its size
and its number of lines give the bytes per row, and that number says what it
costs to store numbers as text.

1. Open `data/raw/D0_KPi.csv` as text. Read the Status Bar: `UTF-8`, `LF`.
   Do not change either.

2. Press `Ctrl+End` (macOS `Cmd+↓`). The last line is 91 585 and it is
   empty: the file has 91 584 lines.

3. Divide the size by the number of lines: 3 926 142 / 91 584 is about 43
   bytes per line. Check it on line 2. It has 42 characters and a line
   break.

    ```text
    1880.649,3000.9534,0.00041271152,1299.1675
    ```

4. Ask how many bytes the same row needs in binary. The four numbers are
   stored as `float32` in the original file: four bytes each, 16 bytes per
   row.

5. Work out the size of the whole table in binary: 91 583 rows of 16 bytes
   are 1 465 328 bytes. The text file is 2.7 times as large.

You should now see three numbers on the board: 43 bytes per row as text, 16
as binary, and the factor 2.7.

Text costs space and can be read by every program and every person. Binary
is compact and needs a program that knows the format. The file in
`data/raw/` is text for that reason. The record's own file,
`MasterclassData.root`, is binary and has 1 289 541 bytes.

!!! warning "Watch for"
    The Status Bar reads `CRLF` for this file. Then it was opened and saved
    by another program, and it is no longer the file that was downloaded.
    Download it again.

## 8. Text or binary { #binary }

**1:30 · 10 min**

The ending of a file name is a hint for people and programs. What a file is
stands in its first bytes.

1. Right-click `results/pendulum_plot.png` and select **Open With...**, then
   **Hex Editor**.

2. Read the first four bytes: `89 50 4E 47`. The column on the right shows
   them as `.PNG`. Every PNG picture begins this way.

3. Right-click the file, select **Copy**, then right-click `results` and
   select **Paste**. Rename the copy to `plot.txt` with `F2` (macOS
   `Enter`).

4. Open `plot.txt`. VS Code now treats it as text and shows signs without
   meaning, or declines to show it. The bytes are those of a picture
   whatever the name says.

5. Delete `plot.txt`.

You should now see only `pendulum_plot.png` and `report.md` in `results`.

## Part 4 · A note in the README { #part-4 }

**1:40 to 2:00 · sections 9 and 10**

## 9. Write down what the file is { #readme }

**1:40 · 15 min**

What was measured today belongs in the README, next to where the file came
from. Whoever opens the file later knows what to expect before reading a
single number.

1. Open `README.md` and add a section under **Data**. The room types the
   labels and fills in the values from today.

    ```text
    ## File anatomy

    `data/raw/D0_KPi.csv`

    - **Encoding:** UTF-8, no letters outside ASCII
    - **Line ending:** LF
    - **Separator:** comma. **Decimal sign:** point
    - **Size:** 3 926 142 bytes
    - **Lines:** 91 584, one header line and 91 583 rows
    - **Bytes per row:** about 43 as text, 16 as float32
    ```

2. Add the same six lines for `data/processed/pendulum.csv`, with the
   student's own line ending and size.

3. Open the preview with `Ctrl+K`, then `V`, and read both entries.

You should now see a **File anatomy** section with two files in the preview.

## 10. Wrap up { #wrap-up }

**1:55 · 5 min**

Put the tasks of the next section on the projector and read them aloud. Ask
on the way out which step was hardest.

What the room has learned:

- `pwd`, `ls` and `cd`: where am I, what is here, go there.
- A file is a sequence of bytes. Its size in bytes is exact, and KB and MB
  are rounded and counted in two ways.
- The letters `a` to `z` take one byte each. `ą` takes two in UTF-8.
- A line break is one byte or two, depending on the system that wrote it.
- The encoding is the table that turns bytes into characters. Reopening
  with another encoding is safe. Saving with another encoding changes the
  file.
- Numbers stored as text take about three times the space of binary, and
  every program can read them.

## Next steps, at home

**30 min, before the next session**

1. Add a **File anatomy** entry for your own dataset: encoding, line ending,
   separator, decimal sign, size in bytes, number of lines, bytes per row.

2. Open your dataset in the hex view and look at the first 16 bytes. If they
   are `EF BB BF`, the file starts with a byte-order mark. Write that into
   the entry.

3. If your dataset has letters outside `a` to `z`, find one of them in the
   hex view and write down its bytes.

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Add an emoji to a scratch file (Windows `Win+.`, macOS
  `Ctrl+Cmd+Space`) and measure it. The answer is 4 bytes for most emoji.
- Type `python` in the terminal (macOS `python3`), then `0.1 + 0.2`. The
  answer is `0.30000000000000004`. `exit()` leaves Python.
- Line 2 of `D0_KPi.csv` gives `M` as `1880.649`. A `float32` holds about 7
  significant digits. Ask whether a value written as `1880.6490001` would be
  more exact. It would not: the extra digits are not in the measurement.
- Compress a copy of `D0_KPi.csv` in the file manager (Windows **Send to** >
  **Compressed folder**, macOS **Compress**) and compare the sizes. The
  answer is about 1.7 MB, less than half of the 3.9 MB.

## If students ask for more

| Topic | Lecture |
|--|--|
| More terminal commands: making, copying, moving and deleting files | 4 (Command Line) |
| Checksums: proving two files are identical | 4 (Command Line) |
| Reading a file in Python with a given encoding | 7 (Python for Data & NumPy) |

## Aims practised

📁 a data file known at the byte level · 🔧 the same three commands on every system · ♻️ what the file is, written down
