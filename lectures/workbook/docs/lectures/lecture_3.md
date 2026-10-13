# 3: How Computers Work

Lecture 3 is what lies underneath a data file. It opens on a table of ten
short lines that takes 148 bytes on disk, and asks what a byte is and which
148 these are. On the way it builds up bits, numbers, text and files, and
the terminal commands that reach a file from a typed line. It closes with
every one of the 148 bytes named.

## What the lecture covers

1. **The box** — a table of 148 bytes; input, algorithm, output; an
   algorithm worked through by hand, one instruction at a time.
2. **Data representation**: unary, binary and decimal counting; the bit and
   the byte; *n* bits give 2ⁿ values, and how many bits tell *k* things apart;
   hexadecimal as the short way to write bytes, on the first five bytes of
   `weather.csv` (`74 69 6D 65 2C`, 40 bits as 10 hex digits); where hex
   appears.
3. **How computers compute**: one binary addition, an hour count from 7 to
   8; logic gates; how the CPU runs an algorithm, with the mean of `temp_c`
   (7.16) as a loop of load, compare, add and jump; the memory hierarchy.
4. **Numbers in computers**: integers of fixed width as a dial that wraps,
   like an odometer; negative numbers counted back from zero (two's
   complement); overflow from 127 to −128 and the type that gives bits their
   meaning; floating point as scientific notation in base 2, on −16.3, the
   coldest hour of the log; −16.3 as a float32, `C1 82 66 66`; the nine
   daily means of `daily.csv` added in Python, 71.69999999999999; the step
   from one float to the next near 9.4; the types of Python's values.
5. **Text & encodings**: ASCII, and why `10.4` sorts before `5.0` as text;
   Unicode and UTF-8, with `ą` encoded by hand; mojibake, with Lithuanian
   letters; the encoding and the line ending in the Status Bar of VS Code;
   what a spreadsheet does to a CSV file.
6. **Files & formats**: file sizes; byte order, on the four bytes of −16.3;
   the first bytes of a file say what it is; the Hex Editor extension by
   Microsoft; the hexdump of the 148-byte table, every byte counted; −16.3
   as text and as a float32.
7. **Files from the terminal**: terminal and shell, zsh on macOS and Git
   Bash on Windows; the terminal of VS Code; the prompt; `pwd`, `ls` and
   `cd` as one sequence that grows click by click; `mkdir`, `cp`, `mv` and
   `rm` as one sequence on a folder listing; the size of a file (`wc -c`) and
   its bytes (`xxd`), each predicted before the output appears. Each command
   is one line, the same in both shells.
8. **Compression & integrity**: lossless and lossy compression, with the
   gzip size of the station's hourly log; a checksum worked by hand, what it
   catches and what it misses; SHA-256 with `shasum -a 256` (macOS) and `sha256sum` (Git Bash), for the table
   with LF and with CRLF.

## The lecture in 90 minutes

The lecture is slides 1–85 and estimates about 129 min. Slides 86–91 are
the self-check quizzes and take no lecture time. For a 90-minute slot, skip
the slides in the second table. To jump, type the slide number and press
Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–7 | The table of 148 bytes; the box: input, algorithm, output |
| 0:11 | 9–38 | Bits, binary counting, bytes; hex on the first bytes of `weather.csv` |
| 0:31 | 40–41, 43 | Adding in binary; how the CPU computes the mean |
| 0:35 | 45–52 | Integers, two's complement, overflow; floats, −16.3 as a float32, the sum of the nine daily means |
| 0:52 | 55–59, 61–62 | Text and encodings; `10.4` before `5.0` answered in bytes at 57 |
| 1:03 | 64, 67, 69–70 | Files and formats; the 148 bytes counted at 69; −16.3 as text and as binary |
| 1:10 | 72–79 | Files from the terminal |
| 1:26 | 80, 83, 85 | SHA-256, recap |
| 1:30 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Data and Code as Files | 8 | 2 min |
| Where Hex Appears | 39 | 1 min |
| Logical Operations | 42 | 2 min |
| The Memory Hierarchy | 44 | 2 min |
| The Steps Between Floats, The Type of a Value | 53–54 | 4 min |
| Text and Bytes in Python | 60 | 3 min |
| What a Spreadsheet Changes, with its live moment | 63 | 6 min |
| File Sizes, Byte Order | 65–66 | 4 min |
| Install the Hex Editor | 68 | 2 min |
| Bit Depth of an Image | 71 | 1 min |
| Compression, A Checksum by Hand | 81–82 | 4 min |
| Key Takeaways | 84 | 2 min |

- **Do not cut** slide 3 (the table of 148 bytes) or slide 85 (the Recap,
  which names all 148). Slide 69 (Reading a Hexdump) is where the count is
  done; reach it by about minute 65.
- **Do not cut** slides 72–79, the terminal. The seminar uses exactly these
  commands.
- **Slides 10–34 are fast.** Most are one word or one picture: counting in
  unary, binary and decimal. Together they take about ten minutes.
- **Slide 38** (The First Five Bytes of `weather.csv`): hex is the short way
  to write bytes. One conversion only, `0x2C` = 2 × 16 + 12 = 44.
- **Slide 51** (−16.3 as a float32): the four bytes `C1 82 66 66` come back
  on slide 66 (byte order) and slide 70 (stored lowest byte first).
- **Slide 57** (the ASCII table): sorted as text, `10.4` comes before `5.0`,
  because `1` is 0x31 and `5` is 0x35.
- **Predict, then click.** Slides 38, 51, 76–79 grow step by step: a
  command or a row of bits first, its output or its next form on the click.
  Slides 59, 69 and 79 highlight one line per click. The runners of slides
  51, 52 and 60 print nothing until ▶. Before each click, ask the room for
  the prediction named under **Ask:** in the note.
- **The slides carry everything.** Every command is on its slide with its
  output, so nothing is opened beside the deck.

## Live in the lecture

Three planned moments, each marked **Live:** in its slide's note. On the
ASCII slide (57): a character typed by its code, and code 7, BEL, rung
instead of printed. Try the bell on the laptop of the room first: the
terminal of VS Code may stay silent. On the Unicode slide (58): a
Word document saved on Windows under the name 🗺️ (WORLD MAP, U+1F5FA,
picked with `Win+.`), and the bytes of that name.
On *What a Spreadsheet Changes* (63): a two-line CSV opened in Excel, one cell
retyped, saved, and compared with the copy kept before.

| | zsh · Git Bash | Output |
|--|--|--|
| Characters from codes | `printf '\x48\x69\n'` | `Hi` |
| One character | `printf '\x41\n'` | `A` |
| The code of a character | `printf '%d\n' "'A"` | `65` |
| TAB, code 9 | `printf 'A\tB\n'` | `A       B` |
| BEL, code 7 | `printf '\a'` | a beep, nothing printed |

### A file named 🗺️ (Unicode slide)

Before the lecture, in Git Bash: `mkdir ~/map-demo`.

1. In Word, open a blank document and press `F12`: the **Save As** box.
   Go to `map-demo` in your home folder.
2. Click into **File name**, press `Ctrl+A` and `Delete`. Press `Win+.`
   (the Windows key and the full stop): the emoji panel opens. Type `map`,
   click 🗺️ (WORLD MAP), press `Esc`. Keep the type **Word Document
   (*.docx)** and select **Save**.
3. In Git Bash:

    | Line | Output |
    |--|--|
    | `cd ~/map-demo` | |
    | `ls` | `🗺️.docx` (a box instead of the symbol is only the terminal's font) |
    | `printf '\U0001F5FA\n'` | 🗺 |
    | `ls *.docx \| xxd` | `00000000: f09f 97ba efb8 8f2e 646f 6378 0a` |

   `f0 9f 97 ba` is U+1F5FA in four bytes; `ef b8 8f` is U+FE0F, an
   invisible code point the emoji panel adds to ask for the emoji form. On
   a Mac the panel is `Ctrl+Cmd+Space`.

### A CSV through Excel (*What a Spreadsheet Changes*)

Before the lecture, in Git Bash: `mkdir ~/excel-demo`. In VS Code,
**File** > **New Text File**, paste the two lines, set `LF` and `UTF-8` in
the Status Bar, and save as `excel_test.csv` in `excel-demo`:

```text
nr,station,date,reading,place
007,SEPT2,1-2,12345678901234567,Užupis
```

Then in Git Bash, in `excel-demo`: `cp excel_test.csv excel_before.csv`.

In class:

1. In File Explorer, double-click `excel_test.csv` (or right-click,
   **Open with** > **Excel**). Not **Data** > **From Text/CSV**: that
   dialog lets you choose the types and the encoding, which is the repair.
2. If each whole line stands in column A, Windows uses `;` between values,
   as a Lithuanian region does: that is the first change already. Close
   Excel, replace every `,` by `;` in both files in VS Code, start again.
3. Point at row 2:

    | Typed | Excel shows | Why |
    |--|--|--|
    | `007` | `7` | read as a number: the leading zeros go |
    | `SEPT2`, `1-2` | dates, such as `2-Sep` and `2-Jan` | read as dates |
    | `12345678901234567` | `1.23457E+16`; the formula bar shows `12345678901234500` | 15 significant digits at most: the last two are gone |
    | `Užupis` | `UÅ¾upis` | a UTF-8 file without a BOM, read by the one-byte table of Windows |

4. Click the `UÅ¾upis` cell and type `Užupis`, as anyone would repair it.
   Press `Ctrl+S`; if a box warns about the CSV format, select **Keep
   Current Format** (or **Yes**). Close Excel, and **Don't Save** if it
   asks again.
5. In Git Bash, `cat excel_before.csv`, then
   `cat excel_test.csv`: `7`, the dates, `1.23457E+16`, and
   `U�upis`. `xxd excel_test.csv` shows `0d0a` at each line end and
   `ž` as one byte, `9E` on an English Windows or `FE` on a Lithuanian one:
   the file is no longer UTF-8.

Excel's version and the region settings change the details. Run it once on
the lecture laptop; that run is the one to show.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 86–91: five quiz slides for students to try afterwards. The same
questions, with their answers:

1. A sensor writes each reading as a 16-bit unsigned integer. How many
   values can a reading take?
   *2¹⁶ = 65 536, from 0 to 65 535.*
2. In two's complement, what is the 4-bit pattern `1010`?
   *−6: six steps back from `0000` (`1111` is −1). As an unsigned integer
   the same bits are 10, and 10 − 16 = −6.*
3. What is a file, at the simplest level?
   *A named sequence of bytes kept by the operating system. The ending of the
   name is only a hint at how to read them.*
4. The published SHA-256 of a file differs from the hash of your copy in every
   digit. What follows?
   *Your copy differs somewhere, by at least one bit. The hash says that
   something changed, never how much.*
5. The working directory is `~/Documents/weather-project/data`. Which
   line prints the size of `daily.csv` in `data/processed`?
   *`wc -c processed/daily.csv`. The working directory is
   `data`, so the relative path starts there.*

## Paired seminar

[Seminar 3](../seminars/seminar_03.md) works in the terminal of VS Code with
the commands of slides 72–79, in zsh or Git Bash: it moves around, makes and
changes folders and files, and measures files to the byte.

## Parked slides

On 13 October 2026, after the note that the binary and hex computations at
the end were skipped through, six slides left the numbers part for
`lectures/content/parked/03_How_Computers_Work.md`: 0x2A in Decimal, From
Decimal to Binary and Hex, Bitwise Operations, Worked Example: 5.75 as
float32, Why 0.1 Is Not Exact and The Float Stored for 0.1. Their place is
taken by the first five bytes of `weather.csv` in hex, an hour count added in
binary, −16.3 as a float32 and the sum of the nine daily means. The two
slides on two's complement of before 13 October are parked there too. The same night the eight one-command slides
of the terminal section (Where Am I, What Is Here, Change Folder, Make a
Folder, Copy and Rename, Delete, and the old size and bytes slides) were
parked; slides 76–79 replace them with sequences that grow click by click.

## Take-aways

- Everything in a computer is bits. A byte is eight of them and holds 256
  values, written as two hex digits.
- An integer of fixed width wraps around when it overflows, with no error.
- A float holds about 7 significant digits in 32 bits and about 15 in 64.
  Decimal fractions such as 9.4 are rounded: the nine daily means add up to
  71.69999999999999, so two floats are compared with a tolerance.
- An encoding is the table that turns bytes into characters. `a` to `z` are
  one byte in every table. `ą` is two bytes in UTF-8.
- Garbled letters mean the right bytes read with the wrong table. The file is
  reopened with the right encoding, not retyped.
- A file is a named sequence of bytes. The ending of its name is a hint; the
  first bytes say what it is.
- The terminal reaches files by typed lines: `pwd`, `ls` and `cd` look
  around, `mkdir`, `cp`, `mv` and `rm` change things, and `rm` cannot be
  undone.
- A hash is a fingerprint of the bytes. Any change gives a different one.
