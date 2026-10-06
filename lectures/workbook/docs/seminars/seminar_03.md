# Seminar 3 — A File as Bytes

**Paired lecture:** 03 How Computers Work · **Format:** follow-along · **~120 min**
in class

**Today's goal:** every student opens a file as bytes, counts them, and can
say which bytes are letters, which are commas and which are line breaks.

The tools are VS Code from Seminar 1 and one extension, the **Hex Editor**.
No terminal, no Python, no Git. The terminal comes after Lecture 04 has
named its parts.

??? note "Autumn 2026"
    This seminar ran as a terminal session that year, and its byte part moved
    to Part 3 of [Seminar 4](seminar_04.md#part-3). The page below is the seminar as
    it is meant to run.

## Run sheet

One screen for the front of the room. Each line links to its section.

| Clock | Section | On the projector | The room ends with |
|--|--|--|--|
| | **Part 1 · Text as bytes** · 45 min | | |
| 0:00 | [1. Install the Hex Editor](#hex) | Extensions, `hex editor`, **Install** | The extension installed |
| 0:10 | [2. Count the bytes of a text](#count) | `abc` → `abcą` → line break, in the hex view | 3, 5, then 6 or 7 bytes |
| 0:30 | [3. Read the bytes with the wrong encoding](#encoding) | **Reopen with Encoding** → Windows 1257 | `ą` shown as `Ä…`, and put right |
| | **Part 2 · A data file as bytes** · 50 min | | |
| 0:45 | [4. A small table](#small) | `pendulum.csv` in the hex view | Commas `2C` and line breaks `0A` found |
| 1:05 | [5. A large table](#large) | Size in Properties, last line with `Ctrl+End` | 43 bytes per row, factor 2.7 |
| 1:25 | [6. Text or binary](#binary) | A PNG in the hex view | `89 50 4E 47` read as `.PNG` |
| | **Part 3 · Write it down** · 25 min | | |
| 1:35 | [7. A File anatomy section](#readme) | `README.md`, then the preview | Two files described |
| 1:55 | [8. Wrap up](#wrap-up) | The list of what was learned | |

**If time runs short:** section 6 is the one to leave out. Every section
starts from files the room already has.

??? info "How to use this page"
    This page is written for the person at the front. Students follow the
    same page.

    - **Tell the room** is the paragraph to say before the steps.
    - The **numbered steps** are what to do on the projector. The room
      repeats each step on their own laptops.
    - **You should now see** closes a section. Ask for hands: "who sees
      this?" Go on when about four in five have it. The rest get help from a
      neighbour.
    - **Watch for** is the usual slip in that section.

    Keys are written for Windows, with macOS in brackets. Where a step
    differs between systems, it has a tab for each.

??? info "Before the session"
    For the room: the project folder of [Seminar 1](seminar_01.md) with
    `data/processed/pendulum.csv`, `results/pendulum_plot.png` and
    `data/raw/D0_KPi.csv`. A student who does not have
    [`D0_KPi.csv`](../data/D0_KPi.csv) downloads it now and drags it onto
    the `raw` folder. A student who missed Seminar 1 downloads
    [`project_after_s1.zip`](../data/project_after_s1.zip), unpacks it, and
    opens `analysis-project` with **File** > **Open Folder...**.

    For you:

    - Sections 2 to 4 done once on your own laptop, so that you know what
      your system writes for a line break.
    - The installer of VS Code on a USB stick for a laptop that lost it.

??? info "Files for this seminar"
    Each file shows what a step should produce, so a student can compare
    their own file with it in the hex view. A browser saves it under the
    name in the second column.

    | File | Saved as | What it is |
    |--|--|--|
    | [`bytes_utf8.txt`](../data/bytes_utf8.txt){ download="bytes.txt" } | `bytes.txt` | Section 2: `abcą` and LF in UTF-8, 6 bytes, `61 62 63 C4 85 0A` |
    | [`bytes_1257.txt`](../data/bytes_1257.txt){ download="bytes_1257.txt" } | `bytes_1257.txt` | Section 3, step 4: the same text saved as Windows 1257, 5 bytes, `61 62 63 E0 0A` |
    | [`pendulum.csv`](../data/pendulum.csv){ download="pendulum.csv" } | `pendulum.csv` | Section 4: the cleaned table with LF, 97 bytes |
    | [`pendulum_crlf.csv`](../data/pendulum_crlf.csv){ download="pendulum_crlf.csv" } | `pendulum_crlf.csv` | Section 4: the same table with CRLF, 107 bytes |
    | [`project_README_s3.txt`](../data/project_README_s3.txt){ download="README.md" } | `README.md` | Section 7: the README with the **File anatomy** section, for LF |
    | [`project_after_s3.zip`](../data/project_after_s3.zip) | `project_after_s3.zip` | The whole `analysis-project` folder at the end of this seminar |

    Open `bytes_1257.txt` in VS Code. It shows `abc` and a sign for an
    unknown character, because VS Code reads it as UTF-8. **Reopen with
    Encoding** and **Baltic (Windows 1257)** show `abcą`.

---

## Part 1 · Text as bytes { #part-1 }

**0:00 to 0:45 · sections 1 to 3**

The room builds a file of a few characters and looks at its bytes after
every change. The file is a scratch file. It is deleted at the end of the
part.

---

### 1. Install the Hex Editor { #hex }

**0:00 · 10 min**

**Tell the room.** An editor shows characters. A hex viewer shows the bytes
themselves, two hex digits for each byte. VS Code gets one as an extension,
a small added program. This is the first extension of the course.

1. Open the project folder in VS Code.

2. Select the **Extensions** icon in the Activity Bar, or press
   `Ctrl+Shift+X` (macOS `Cmd+Shift+X`). Type into the search box:

    ```text
    hex editor
    ```

3. Select **Hex Editor**, published by Microsoft, and then **Install**.

4. Go back to the Explorer with `Ctrl+Shift+E` (macOS `Cmd+Shift+E`).

!!! success "You should now see"
    **Hex Editor** in the list of installed extensions on every laptop.

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | Several extensions called Hex Editor | Take the one published by Microsoft, with the blue tick |
    | **Install** does nothing | The laptop is offline. Pair with a neighbour for this part |

---

### 2. Count the bytes of a text { #count }

**0:10 · 20 min**

**Tell the room.** A file is a sequence of bytes. For plain English text one
character is one byte. Other letters take more, and a line break is a byte
too. Before each look at the bytes, the room predicts how many there are.

1. In the Side Bar select the empty area below the folders, then
   **New File**, and name it:

    ```text
    bytes.txt
    ```

2. Type into the file, without pressing Enter, and save with `Ctrl+S`
   (macOS `Cmd+S`):

    ```text
    abc
    ```

3. Right-click `bytes.txt`, select **Open With...**, then **Hex Editor**.
   Count the cells on the left: three.

    ```text
    61 62 63
    a  b  c
    ```

    Find `a` in the ASCII table of the lecture: 97, which is `61` in hex.

4. Go back to the text tab. Add `ą` after the `c` and save. Ask the room
   for the number of bytes, then look in the hex view: five.

    ```text
    61 62 63 C4 85
    a  b  c  ą
    ```

    `ą` takes two bytes in UTF-8: `C4 85`. The column on the right shows
    `abc..`: the hex view prints a dot for every byte that is not a plain
    English character.

5. Press Enter at the end of the line and save. Ask who has 6 bytes and who
   has 7 in the hex view.

    === "macOS, Linux"

        ```text
        61 62 63 C4 85 0A
        ```

    === "Windows"

        ```text
        61 62 63 C4 85 0D 0A
        ```

6. Look at the right end of the Status Bar. It reads `LF` or `CRLF`. This is
   the line break: `0A`, or `0D 0A`. Select it, choose **LF**, save, and
   look at the hex view again. Every laptop now has 6 bytes.

!!! success "You should now see"
    The same table on every laptop.

    | Text in the file | Bytes | Reason |
    |--|--|--|
    | `abc` | 3 | One byte for each of these letters |
    | `abcą` | 5 | `ą` takes two bytes in UTF-8 |
    | `abcą` and a line break | 6 or 7 | LF is one byte, CRLF is two |

!!! warning "Watch for"
    | On the screen | What to do |
    |--|--|
    | The hex view does not change | The file was not saved. A dot on the tab means *not saved*. Save, then close and reopen the hex view |
    | One byte more than expected | A space or an extra line break. Look for `20` or a second `0A` |
    | A last cell with `+` after the bytes | It is a button for adding a byte, not part of the file. Do not count it, and do not select it |

---

### 3. Read the bytes with the wrong encoding { #encoding }

**0:30 · 15 min**

**Tell the room.** The bytes of a text mean nothing without the table that
maps bytes to characters. That table is the encoding. VS Code names the one
it used in the Status Bar: `UTF-8`. Reading the same bytes with another
table gives other characters.

1. In the text tab, select `UTF-8` in the Status Bar, then
   **Reopen with Encoding**, and type:

    ```text
    1257
    ```

    Choose **Baltic (Windows 1257)**.

2. The file now reads `abcÄ…`. The two bytes of `ą` are shown as two
   characters. The hex view still shows the same six bytes.

3. Select the encoding in the Status Bar again, **Reopen with Encoding**,
   **UTF-8**. The text is `abcą` again.

4. Now change the bytes. Select `UTF-8`, then **Save with Encoding**, and
   choose **Baltic (Windows 1257)**. Look at the hex view: one byte less.

    ```text
    61 62 63 E0 0A
    ```

    In that table `ą` is the single byte `E0`.

5. Put it back: select `Windows 1257` in the Status Bar, then
   **Save with Encoding**, **UTF-8**. The hex view shows `C4 85` again.

6. Delete `bytes.txt`: right-click it in the Side Bar and select **Delete**.

!!! success "You should now see"
    No `bytes.txt` in the Side Bar, and the room can say which two bytes are
    `ą` in UTF-8 and which one byte it is in Windows 1257.

**Say it in these words.** Reopen reads the same bytes in another way and is
safe. Save writes other bytes. A file that shows `Ä…` or `Å¾` is not
broken. It was read with the wrong table, and it is reopened, not retyped.

---

## Part 2 · A data file as bytes { #part-2 }

**0:45 to 1:35 · sections 4 to 6**

The same two tools, the Status Bar and the hex view, are now used on the
data files of the project.

---

### 4. A small table { #small }

**0:45 · 20 min**

**Tell the room.** `data/processed/pendulum.csv` has ten lines. Every one of
its bytes can be accounted for: the characters of the numbers, the commas,
the line breaks.

1. Open `data/processed/pendulum.csv` as text. Read the Status Bar:
   `UTF-8`, and `LF` or `CRLF`.

2. Count with the room. The ten lines hold 87 characters, 10 of them
   commas. Add one byte per line break for LF, or two for CRLF.

3. Read the exact size. Right-click the file and select
   **Reveal in File Explorer** (macOS **Reveal in Finder**). Then:

    === "macOS"

        Select the file, press `Cmd+I`. The size in bytes is the number
        after **Size**.

    === "Windows"

        Right-click the file, **Properties**. The size in bytes is the
        number in brackets after **Size**.

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

!!! success "You should now see"
    One of the four sizes on every laptop, and each student can say which of
    the four cases their file is.

The table of numbers is the same on every laptop, and the files differ by up
to 11 bytes. That is why two copies of a file are compared by their bytes
and not by how they look.

---

### 5. A large table { #large }

**1:05 · 20 min**

**Tell the room.** `D0_KPi.csv` cannot be counted by hand, and it does not
need to be. Its size and its number of lines give the bytes per row, and
that number says what it costs to store numbers as text.

1. Read the size of `data/raw/D0_KPi.csv` the way section 4 did:
   3 926 142 bytes. The file manager also shows it as about 3.74 MB on
   Windows and 3.9 MB on macOS: the same bytes, counted in units of 1024
   and of 1000.

2. Open the file as text. Read the Status Bar: `UTF-8`, `LF`. Do not change
   either.

3. Press `Ctrl+End` (macOS `Cmd+↓`). The last line is 91 585 and it is
   empty: the file has 91 584 lines.

4. Divide the size by the number of lines: 3 926 142 / 91 584 is about 43
   bytes per line. Check it on line 2. It has 42 characters and a line
   break.

    ```text
    1880.649,3000.9534,0.00041271152,1299.1675
    ```

5. Ask how many bytes the same row needs in binary. The four numbers are
   stored as `float32` in the original file: four bytes each, 16 bytes per
   row.

6. Work out the size of the whole table in binary: 91 583 rows of 16 bytes
   are 1 465 328 bytes. The text file is 2.7 times as large.

!!! success "You should now see"
    Three numbers on the board: 43 bytes per row as text, 16 as binary, and
    the factor 2.7.

Text costs space and can be read by every program and every person. Binary
is compact and needs a program that knows the format. The file in
`data/raw/` is text for that reason. The record's own file,
`MasterclassData.root`, is binary and has 1 289 541 bytes.

!!! warning "Watch for"
    The Status Bar reads `CRLF` for this file. Then it was opened and saved
    by another program, and it is no longer the file that was downloaded.
    Download it again.

---

### 6. Text or binary { #binary }

**1:25 · 10 min**

**Tell the room.** The ending of a file name is a hint for people and
programs. What a file is stands in its first bytes.

1. Right-click `results/pendulum_plot.png` and select **Open With...**,
   then **Hex Editor**.

2. Read the first four bytes. The column on the right shows them as
   `.PNG`. Every PNG picture begins this way.

    ```text
    89 50 4E 47
    ```

3. Right-click the file, select **Copy**, then right-click `results` and
   select **Paste**. The copy is called `pendulum_plot copy.png`. Rename it
   with `F2` (macOS `Enter`) to:

    ```text
    plot.txt
    ```

4. Open `plot.txt`. VS Code now treats it as text and shows signs without
   meaning, or declines to show it. The bytes are those of a picture
   whatever the name says.

5. Delete `plot.txt`.

!!! success "You should now see"
    Only `pendulum_plot.png` and `report.md` in `results`.

---

## Part 3 · Write it down { #part-3 }

**1:35 to 2:00 · sections 7 and 8**

---

### 7. A File anatomy section { #readme }

**1:35 · 20 min**

**Tell the room.** What was measured today belongs in the README, next to
where the file came from. Whoever opens the file later knows what to expect
before reading a single number.

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

3. Open the preview with `Ctrl+K`, then `V` (macOS `Cmd+K`, then `V`), and
   read both entries.

!!! success "You should now see"
    A **File anatomy** section with two files in the preview.

---

### 8. Wrap up { #wrap-up }

**1:55 · 5 min**

Read the list aloud. Ask on the way out which step was hardest.

- A file is a sequence of bytes. Its size in bytes is exact. KB and MB are
  rounded and counted in two ways.
- The letters `a` to `z` take one byte each. `ą` takes two in UTF-8.
- A line break is one byte or two, depending on the system that wrote it.
- The encoding is the table that turns bytes into characters. Reopening
  with another encoding is safe. Saving with another encoding changes the
  file.
- Numbers stored as text take about three times the space of binary, and
  every program can read them.
- What a file is stands in its first bytes, not in its name.

---

## Stretch goals

For students who finish a section early. Answers are given for the lecturer.

- Add an emoji to a scratch file (Windows `Win+.`, macOS
  `Ctrl+Cmd+Space`) and look at it in the hex view. Most emoji take 4
  bytes.
- Open your own dataset in the hex view and look at the first bytes. If
  they are `EF BB BF`, the file starts with a byte-order mark.
- Line 2 of `D0_KPi.csv` gives `M` as `1880.649`. A `float32` holds about 7
  significant digits. Ask whether a value written as `1880.6490001` would
  be more exact. It would not: the extra digits are not in the measurement.
- Compress a copy of `D0_KPi.csv` in the file manager (Windows **Send to** >
  **Compressed folder**, macOS **Compress**) and compare the sizes. The
  answer is about 1.7 MB, less than half of the 3.9 MB.

## If students ask for more

| Topic | Lecture |
|--|--|
| The terminal: measuring and counting files by command | 4 (Command Line) |
| Checksums: proving two files are identical | 4 (Command Line) |
| Reading a file in Python with a given encoding | 7 (Python for Data & NumPy) |

## Aims practised

📁 a data file known at the byte level · 🔧 the same view of bytes on every system · ♻️ what the file is, written down
