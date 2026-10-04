# 3: How Computers Work

Lecture 2 defined data as a representation of information by a fixed rule,
and ended on a text file in which `100` sorted before `20`, because the editor
saw characters and not numbers. Lecture 3 is what lies underneath: how a
number, a letter and a whole file are written as bits.

## What the lecture covers

1. **The box** — input, algorithm, output; an algorithm worked through by
   hand, one instruction at a time.
2. **Data representation** — unary, binary and decimal counting; the bit and
   the byte; hexadecimal as the short way to write bytes.
3. **How computers compute** — logic gates and bitwise operations; how the CPU
   runs an algorithm; the memory hierarchy.
4. **Numbers in computers** — integers of fixed width and overflow; negative
   numbers in two's complement; floating point as scientific notation in
   base 2, and why `0.1 + 0.2` is not `0.3`.
5. **Text & encodings** — ASCII, Unicode and UTF-8; mojibake, with Lithuanian
   letters; the encoding and the line ending in the Status Bar of VS Code; what
   a spreadsheet does to a CSV file.
6. **Files & formats** — file sizes; byte order; the first bytes of a file
   say what it is; reading a hexdump of a small CSV file.
7. **Compression & integrity** — why text compresses well; checksums and
   SHA-256.

## The lecture in 90 minutes

The deck has 75 slides and estimates about 111 min. For a 90-minute slot,
skip the slides in the second table. To jump, type the slide number and press
Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–7 | The box: input, algorithm, output |
| 0:11 | 8–38 | Bits, binary counting, bytes, hexadecimal |
| 0:36 | 39–44 | How the computer computes |
| 0:44 | 45–54 | Integers and floating point |
| 0:58 | 55–62 | Text and encodings |
| 1:10 | 63–69 | Files and formats |
| 1:20 | 70–75 | Compression, hashing, recap |
| 1:30 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| Quiz: the 16-bit detector reading | 34 | 3 min |
| Bitwise Operations Example | 42 | 2 min |
| Quiz: two's complement | 48 | 3 min |
| Worked Example: 5.75 as float32 | 51 | 2 min |
| Python for Encoding Conversions | 59 | 2 min |
| Endianness | 65 | 2 min |
| Quiz: what is a file | 68 | 3 min |
| Quiz: the hash that differs | 73 | 3 min |

- **Do not cut** slides 56–62 (text and encodings) or 64, 66 and 67 (file
  sizes, formats, the hexdump). The seminar measures and opens files in
  exactly these terms.
- **Slides 9–33 are fast.** Most are one word or one picture: counting in
  unary, binary and decimal. Together they take about ten minutes.
- **Slide 53** (Try It in Your Terminal) is done live in the VS Code
  terminal. Students who installed Python at home can follow on their own
  laptops.
- **Slide 61** (Encoding & Line Endings in VS Code) is done live: open a file
  with Lithuanian letters, select `UTF-8` in the Status Bar, reopen it as
  **Baltic (Windows 1257)** and back.
- **Slide 67** (Reading a Hexdump) shows the first bytes of the small table
  that was cleaned in Lecture 2.

## Demos to run live

- A drawing of a cube on the whiteboard is read as a cube only by someone who
  knows the convention. A representation needs a rule: the opening for the
  section on data representation.
- The ASCII control characters still act. In the Python prompt,
  `print("\a")` rings the terminal bell, which is character 7, `BEL`.
- Floating point, in the Python prompt:

    ```python
    0.1 + 0.2 == 0.3                             # False
    import math
    math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-12)  # True
    ```

- Overflow of a fixed-width integer, for a room that has NumPy:

    ```python
    import numpy as np
    np.int8(127) + np.int8(1)                    # -128, with a warning
    ```

## Paired seminar

[Seminar 3 — A File as Bytes](../seminars/seminar_03.md) introduces the
terminal with three commands, `pwd`, `ls` and `cd`. The room then measures a
file of four characters in bytes, reads it with the wrong encoding, opens it
in a hex view, and does the same for the two data files of the project.

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
- A hash is a fingerprint of the bytes. Any change gives a different one.
