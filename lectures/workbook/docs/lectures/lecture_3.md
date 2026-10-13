# 3: How Computers Work

Lecture 3 is what lies underneath a data file. It opens on a table of ten
short lines that takes 148 bytes on disk, and asks what a byte is and which
148 these are. On the way it builds up bits, numbers, text and files, and
the terminal commands that reach a file from a typed line. It closes with
every one of the 148 bytes named.

## What the lecture covers

1. **The box** — a table of 148 bytes; input, algorithm, output; an
   algorithm worked through by hand, one instruction at a time.
2. **Data representation** — unary, binary and decimal counting; the bit and
   the byte; *n* bits give 2ⁿ values, and how many bits tell *k* things apart;
   hexadecimal; converting decimal to binary by repeated division and binary
   to hex in groups of four.
3. **How computers compute** — binary addition, logic gates and bitwise
   operations; how the CPU runs an algorithm; the memory hierarchy.
4. **Numbers in computers** — integers of fixed width as a dial that wraps,
   like an odometer; negative numbers counted back from zero (two's
   complement); overflow from 127 to −128 and the type that gives bits their
   meaning; floating point as
   scientific notation in base 2; why 0.1 has no exact float, derived by
   multiplying by 2; the step from one float to the next, and what it means
   for a stored temperature.
5. **Text & encodings** — ASCII, and why `10.4` sorts before `5.0` as text;
   Unicode and UTF-8, with `ą` encoded by hand; mojibake, with Lithuanian
   letters; the encoding and the line ending in the Status Bar of VS Code;
   what a spreadsheet does to a CSV file.
6. **Files & formats** — file sizes; byte order; the first bytes of a file
   say what it is; the Hex Editor extension by Microsoft; the hexdump of the
   148-byte table, every byte counted; one number as text and as a float32.
7. **Files from the terminal** — terminal and shell; the terminal of VS
   Code; the prompt; `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`; the size of
   a file (`wc -c`, `(Get-Item FILE).Length`) and its bytes (`hexdump -C`,
   `Format-Hex`). Every line works in zsh and in both Windows PowerShells.
8. **Compression & integrity** — lossless and lossy compression, with the
   gzip size of the station's hourly log; a checksum worked by hand, what it
   catches and what it misses; SHA-256 by command, for the table with LF and
   with CRLF.

## The lecture in 90 minutes

The lecture is slides 1–93 and estimates about 142 min. Slides 94–99 are
the self-check quizzes and take no lecture time. For a 90-minute slot, skip
the slides in the second table. To jump, type the slide number and press
Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–7 | The table of 148 bytes; the box: input, algorithm, output |
| 0:08 | 9–39 | Bits, binary counting, bytes, hexadecimal, converting between bases |
| 0:34 | 41, 45 | How the CPU runs an algorithm |
| 0:37 | 47–52, 54–56 | Integers, two's complement, floating point |
| 0:52 | 59–63, 65–66 | Text and encodings; `10.4` before `5.0` answered in bytes at 61 |
| 1:03 | 68–69, 71–74 | Files and formats; the 148 bytes counted at 73 |
| 1:13 | 76–87 | Files from the terminal |
| 1:28 | 88, 91–93 | SHA-256, take-aways, recap |
| 1:33 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Data and Code as Files | 8 | 2 min |
| Where Hex Appears | 40 | 1 min |
| Binary addition, Logical Operations, Bitwise Operations | 42–44 | 7 min |
| The Memory Hierarchy | 46 | 2 min |
| Worked Example: 5.75 as float32 | 53 | 2 min |
| The Float Stored for 0.1, The Type of a Value | 57–58 | 5 min |
| Text and Bytes in Python | 64 | 3 min |
| What a Spreadsheet Changes | 67 | 2 min |
| Byte Order | 70 | 2 min |
| Bit Depth of an Image | 75 | 1 min |
| Compression, A Checksum by Hand | 89–90 | 4 min |

- **Do not cut** slide 3 (the table of 148 bytes) or slide 93 (the Recap,
  which names all 148). Slide 73 (Reading a Hexdump) is where the count is
  done; reach it by about minute 70.
- **Do not cut** slides 76–87, the terminal. The seminar uses exactly these
  commands, and the room has not seen a terminal before.
- **Slides 10–34 are fast.** Most are one word or one picture: counting in
  unary, binary and decimal. Together they take about ten minutes.
- **Slide 39** (From Decimal to Binary and Hex): do 37 on the board, then
  give the room 100 to convert on paper. The answers are `1100100` and `0x64`.
- **Slide 61** (the ASCII table): sorted as text, `10.4` comes before `5.0`,
  because `1` is 0x31 and `5` is 0x35.
- **The slides carry everything.** Every command is on its slide with its
  output in both shells, so nothing is opened beside the deck.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 94–99: five quiz slides for students to try afterwards. The same
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
5. The prompt is `PS C:\Users\smilte\Documents\weather-project\data>`. Which
   line prints the size of `daily.csv` in `data/processed`?
   *`(Get-Item processed/daily.csv).Length`. The working directory is
   `data`, so the relative path starts there.*

## Paired seminar

[Seminar 3 — Files and Bytes from the Terminal](../seminars/seminar_03.md)
hands out its own folder of seven everyday files, `inbox`. The room opens a
terminal, moves around with `pwd`, `ls` and `cd`, makes a folder, fixes a
name with a space, and sorts the files with `mkdir`, `mv`, `cp` and `rm`.
Then every file is measured to the byte: a letter of two bytes, a line
break of two bytes, a file in the old Baltic encoding, a picture whose name
ends in `.txt`, and two tables that differ in one byte, found by their
SHA-256.

## Take-aways

- Everything in a computer is bits. A byte is eight of them and holds 256
  values, written as two hex digits.
- An integer of fixed width wraps around when it overflows, with no error.
- A float holds about 7 significant digits in 32 bits and about 15 in 64.
  Decimal fractions such as 0.1 are rounded, so two floats are compared with
  a tolerance.
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
