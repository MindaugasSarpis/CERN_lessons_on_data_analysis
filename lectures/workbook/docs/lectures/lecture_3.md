# 3: How Computers Work

Lecture 2 defined data as a representation of information by a fixed rule,
and ended on a text file in which `100` sorted before `20`, because the editor
saw characters and not numbers. Lecture 3 is what lies underneath: how a
number, a letter and a whole file are written as bits.

## What the lecture covers

1. **The box** — input, algorithm, output; an algorithm worked through by
   hand, one instruction at a time.
2. **Data representation** — unary, binary and decimal counting; the bit and
   the byte; *n* bits give 2ⁿ values, and how many bits tell *k* things apart;
   hexadecimal; converting decimal to binary by repeated division and binary
   to hex in groups of four.
3. **How computers compute** — logic gates and bitwise operations; how the CPU
   runs an algorithm; the memory hierarchy.
4. **Numbers in computers** — integers of fixed width and overflow; two's
   complement as a recipe and as a sum of weights; floating point as
   scientific notation in base 2; why 0.1 has no exact float, derived by
   multiplying by 2; the step from one float to the next, and what it means
   for a stored measurement.
5. **Text & encodings** — ASCII, Unicode and UTF-8; how UTF-8 packs a code
   point, with `ą` encoded by hand; mojibake, with Lithuanian letters; the
   encoding and the line ending in the Status Bar of VS Code; what a
   spreadsheet does to a CSV file.
6. **Files & formats** — file sizes; byte order; the first bytes of a file
   say what it is; the hexdump of a small CSV file; one number as text and as
   a float32.
7. **Compression & integrity** — why text compresses well; a checksum worked
   by hand, what it catches and what it misses; CRC and SHA-256.

## The lecture in 90 minutes

The lecture is slides 1–79 and estimates about 116 min. Slides 80–84 are the
self-check quizzes and take no lecture time. For a 90-minute slot, skip the
slides in the second table. To jump, type the slide number and press Enter.

| Clock | Slides | Part |
|--|--|--|
| 0:00 | 1–6 | The box: input, algorithm, output |
| 0:09 | 8–38 | Bits, binary counting, bytes, hexadecimal, converting between bases |
| 0:39 | 40, 44 | How the CPU runs an algorithm |
| 0:42 | 46–56 | Integers, two's complement, floating point |
| 1:02 | 58–66 | Text and encodings |
| 1:16 | 67–72 | Files and formats |
| 1:26 | 74–79 | Compression, hashing, recap |
| 1:33 | | Move to the seminar |

| Skip | Slides | Saves |
|--|--|--|
| A Bit of Foresight | 7 | 2 min |
| Why Hex in Computing? | 39 | 1 min |
| Logic gates, Logical Operations, Bitwise Operations Example | 41–43 | 5 min |
| The Memory Hierarchy | 45 | 2 min |
| Worked Example: 5.75 as float32 | 52 | 2 min |
| Data Types in Practice | 57 | 2 min |
| Python for Encoding Conversions | 63 | 2 min |
| Endianness | 69 | 2 min |
| Image Quality vs Bit Depth | 73 | 2 min |
| A Checksum by Hand | 76 | 2 min |
| Key Takeaways, since the Recap follows | 78 | 2 min |

- **Do not cut** slides 59–62 and 64–66 (text and encodings) or 68 and 70–72
  (file sizes, formats, the hexdump, one number as text and as binary). The
  seminar measures and opens files in exactly these terms.
- **Slides 9–33 are fast.** Most are one word or one picture: counting in
  unary, binary and decimal. Together they take about ten minutes.
- **Slide 38** (From Decimal to Binary and Hex): do 37 on the board, then
  give the room 100 to convert on paper. The answers are `1100100` and `0x64`.
- **Slide 56** (Try It in Your Terminal) is done live in the VS Code
  terminal. Students who installed Python at home can follow on their own
  laptops.
- **Slide 65** (Encoding & Line Endings in VS Code) is done live: open a file
  with Lithuanian letters, select `UTF-8` in the Status Bar, reopen it as
  **Baltic (Windows 1257)** and back.
- **Slide 71** (Reading a Hexdump) shows the first bytes of the small table
  that was cleaned in Lecture 2.

## Check yourself

No quiz interrupts the lecture. The deck closes with a self-check section,
slides 80–84: four quiz slides for students to try afterwards. The same
questions, with their answers:

1. A detector writes each reading as a 16-bit unsigned integer. How many
   values can a reading take?
   *2¹⁶ = 65 536, from 0 to 65 535.*
2. In two's complement, what is the 4-bit pattern `1010`?
   *−6. By weights: −8 + 2. As an unsigned integer the same bits are 10.*
3. What is a file, at the simplest level?
   *A named sequence of bytes kept by the operating system. The ending of the
   name is only a hint at how to read them.*
4. The published SHA-256 of a file differs from the hash of your copy in every
   digit. What follows?
   *Your copy differs somewhere, by at least one bit. The hash says that
   something changed, never how much.*

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
- *n* bits hold 2ⁿ values. The same bits are different numbers under
  different types, so the type belongs to the description of the data.
- The step between neighbouring floats grows with the number. A float32 keeps
  about 7 significant digits; digits beyond them are rounding, not
  measurement.
