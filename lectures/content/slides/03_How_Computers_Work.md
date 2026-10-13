---
layout: cover
title: "How Computers Work"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## How Computers Work

##### <span class="aims-badge">🔧 tool-agnostic · 📁 data & files</span>

<!--
**Say:** today is what a computer stores, from one bit up to a whole file, and how it runs a list of instructions on it. No programming today.
(~1 min)
-->

---
layout: quote
hideInToc: true
---

# The main goal of this lecture is to see what data is **made of**: bits, bytes, numbers, text and files, and how a computer runs an **algorithm** on them

---
hideInToc: true
---

# `daily.csv` and Its **Size**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **`daily.csv` in VS Code**

```text
date,temp_c
2025-10-01,6.3
2025-10-02,5.0
2025-10-03,5.6
2025-10-04,7.0
2025-10-05,9.4
2025-10-06,10.4
2025-10-07,9.2
2025-10-08,9.0
2025-10-09,9.8
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 📏 **In the file manager**

**148 bytes.**

Ten lines: a header, and the daily mean temperature of nine days at a weather station.

❓ What is a byte, and which 148 bytes are these?

</div>

</div>

<!--
**Say:** by the end of the lecture every one of the 148 bytes has a name.
**Ask:** how many characters has one line? Let the room count `2025-10-01,6.3`: 14.
**If asked:** the size is in Finder with Cmd+I, or in Properties in Explorer.
(~2 min)
-->

---
hideInToc: true
---

# Learning **Objectives**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🧠 Follow an **algorithm** one instruction at a time, the way a processor does

</div>

<div class="card card-secondary card-glass pad-compact">

🔢 Convert numbers between **binary**, **decimal** and **hexadecimal**

</div>

<div class="card card-accent card-glass pad-compact">

📐 Predict **overflow** and **rounding** in integers and floats

</div>

<div class="card card-info card-glass pad-compact">

🔤 Explain how text becomes bytes through **ASCII** and **UTF-8**

</div>

<div class="card card-warning card-glass pad-compact">

📁 Read a file as **bytes**: its size, encoding, line endings and format

</div>

<div class="card card-success card-glass pad-compact">

⌨️ Move through folders and measure a file from the **terminal**

</div>

</div>

<!--
**Say:** one line per section. The thread is the 148 bytes of `daily.csv`.
(~1 min)
-->

---
layout: center
hideInToc: true
---

```mermaid {scale: 1.8}
graph LR
    A[input] --> B["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br/>&nbsp;"] --> C[output]

    classDef invisible fill:none,stroke:none,font-size:24px;
    classDef transparentBox fill:none,stroke:white,stroke-width:3px,font-size:24px;
    classDef textStyle font-size:24px;

    class A invisible;
    class B transparentBox;
    class C invisible;

    linkStyle 0 stroke-width:3px;
    linkStyle 1 stroke-width:3px;
```

<!--
**Ask:** what goes into the empty box? Whatever turns the input into the output, step by step.
(~1 min)
-->


---
hideInToc: true
---

# What Is an **Algorithm**?

<div class="card card-info card-glass pad-compact mt-sm">

An **algorithm** is a finite list of exact instructions that turns an input into an output.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍳 **Cooking pasta**

1. Boil water, add the pasta, wait 10 min
2. Drain, serve

**Input:** raw pasta. **Output:** cooked pasta

</div>

<div class="card card-secondary card-glass pad-compact">

## 📖 **A word in a dictionary**

1. Open the book in the middle
2. Is the word before or after this page?
3. Keep that half, and repeat

**Input:** "Python". **Output:** page 742

</div>

</div>

<!--
**Say:** the box of the last slide holds an algorithm. Every step is exact, and the list ends.
**Ask:** how many halvings find a word in 1000 pages? Ten, because 2 to the power 10 is 1024.
(~2 min)
-->

---
hideInToc: true
---

# Think Like a **CPU**

<div class="card card-success card-glass pad-compact mt-sm">

## 🧮 **The largest number in `[7, 2, 9, 4]`**

1. Set `max` to the first number
2. Look at the next number
3. If it is larger than `max`, it becomes `max`
4. Repeat steps 2 and 3 to the end of the list
5. `max` holds the answer

</div>

<div class="card card-info card-glass pad-compact mt-md">

Step 3 is a comparison and step 4 a jump back. A processor knows little more than these two, done billions of times a second.

</div>

<!--
**Do:** give the room 60 seconds with the list on paper.
**Ask:** one student reads out `max` after each step: 7, 7, 9, 9.
(~2 min)
-->

---
hideInToc: true
---

# Data and Code as **Files**

<div class="card card-warning card-glass pad-compact mt-sm">

🧭 If data and instructions are both bytes in files, an analysis becomes **raw file, box, result**. The box can then be run again by a program instead of by hand.

</div>

<div class="card card-info card-glass pad-compact mt-md">

- The data need not be looked at row by row
- The steps need not be clicked again
- The result is checked, and a wrong step is found in a file

</div>

<!--
**Say:** this is the course in one slide. Reproducibility and automation follow from treating data and steps as files. Today builds the "bytes in files" half.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Data **Representation**

What a computer stores, from one switch, the bit, up to the byte and the hex digits that name it.

<!--
**Say:** unary, binary, decimal, the byte, hex. Keep a brisk pace: most slides are one word or one picture.
(~1 min)
-->

---
layout: fact
hideInToc: true
---

# Unary

## <v-click> **Base-1** </v-click>

---
layout: center
hideInToc: true
class: text-center
---

<div style="font-size: 5rem; letter-spacing: 0.15em;">
  <span v-click="1">|</span>
  <span v-click="2">|</span>
  <span v-click="3">|</span>
  <span v-click="4">|</span>
  <span v-click="5">|</span>
</div>

<div class="note-text mt-md">

One mark per unit: the oldest way to count, and the simplest.

</div>

---
layout: fact
hideInToc: true
---

# Binary

## <v-click> **Base-2** </v-click>

---
layout: center
hideInToc: true
class: text-center
---

# **0**

<img src="/figures/light_bulb_off.png" class="w-auto h-86">

<style>
h1 {
  font-size: 6rem;
}
</style>


---
layout: center
hideInToc: true
class: text-center
---

# **1**

<img src="/figures/light_bulb_on.png" class="w-auto h-86">

<style>
h1 {
  font-size: 6rem;
}
</style>

---
layout: fact
hideInToc: true
---

# Binary Digit

---
layout: fact
hideInToc: true
---

# Bi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t

---
layout: fact
hideInToc: true
---

# Bit

---
hideInToc: true
layout: image
image: /figures/first_transistor.jpg
backgroundSize: contain
---

<div class="note-text" style="position: absolute; left: 0; right: 0; bottom: 1rem; text-align: center; text-shadow: 0 1px 6px rgba(0, 0, 0, 0.8);">
The first transistor, Bell Labs, 1947: the physical switch behind every bit
</div>

---
hideInToc: true
---

<VideoPlayer src="Technology_Size_Comparison.mp4" autoplay   />

---
hideInToc: true
layout: fact
---

# Decimal

## <v-click> **Base-10** </v-click>

---
layout: center
hideInToc: true
class: text-center
---

<div class="powers">
<v-click at="3">
    <span>100</span> &nbsp;&nbsp;&nbsp;
</v-click>
<v-click at="2">
    <span>10</span> &nbsp;&nbsp;&nbsp;
</v-click>
<v-click at="1">
    <span>1</span>
    </v-click>
</div>

<div class="number"> 000</div>

<div class="expansion">

<v-click at="4">
    100 × 0 &nbsp; + &nbsp; 10 × 0 &nbsp; + &nbsp; 1 × 0
</v-click>
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
layout: center
hideInToc: true
class: text-center
---

<div class="powers">
    <span>100</span> &nbsp;&nbsp;&nbsp;
    <span>10</span> &nbsp;&nbsp;&nbsp;
    <span>1</span>
</div>

<div class="number"> 004 </div>

<div class="expansion">
    100 × 0 &nbsp; + &nbsp; 10 × 0 &nbsp; + &nbsp; 1 × 4
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
layout: center
hideInToc: true
class: text-center
---

<div class="powers">
    <span>100</span> &nbsp;&nbsp;&nbsp;
    <span>10</span> &nbsp;&nbsp;&nbsp;
    <span>1</span>
</div>

<div class="number"> 074 </div>

<div class="expansion">
    100 × 0 &nbsp; + &nbsp; 10 × 7 &nbsp; + &nbsp; 1 × 4
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
layout: center
hideInToc: true
class: text-center
---

<div class="powers">
    <span>100</span> &nbsp;&nbsp;&nbsp;
    <span>10</span> &nbsp;&nbsp;&nbsp;
    <span>1</span>
</div>

<div class="number"> 974 </div>

<div class="expansion">
    100 × 9 &nbsp; + &nbsp; 10 × 7 &nbsp; + &nbsp; 1 × 4
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
layout: center
hideInToc: true
class: text-center
---

<div class="powers">
    <span>2<sup>2</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>1</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>0</sup></span>
</div>

<div class="number"> 000</div>

<div class="expansion">
    4 × 0 &nbsp; + &nbsp; 2 × 0 &nbsp; + &nbsp; 1 × 0 = 0
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
layout: center
hideInToc: true
class: text-center
---

<div class="powers">
    <span>2<sup>2</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>1</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>0</sup></span>
</div>
<div class="number"> 001</div>
<div class="expansion">
    4 × 0 &nbsp; + &nbsp; 2 × 0 &nbsp; + &nbsp; 1 × 1 = 1
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
layout: center
hideInToc: true
class: text-center
---

<div class="powers">
    <span>2<sup>2</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>1</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>0</sup></span>
</div>
<div class="number"> 010</div>
<div class="expansion">
    4 × 0 &nbsp; + &nbsp; 2 × 1 &nbsp; + &nbsp; 1 × 0 = 2
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
layout: center
hideInToc: true
class: text-center
---

<div class="powers">
    <span>2<sup>2</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>1</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>0</sup></span>
</div>
<div class="number"> 011</div>
<div class="expansion">
    4 × 0 &nbsp; + &nbsp; 2 × 1 &nbsp; + &nbsp; 1 × 1 = 3
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
layout: center
hideInToc: true
class: text-center
---

<div class="powers">
    <span>2<sup>2</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>1</sup></span> &nbsp;&nbsp;&nbsp;
    <span>2<sup>0</sup></span>
</div>
<div class="number"> 100</div>
<div class="expansion">
    4 × 1 &nbsp; + &nbsp; 2 × 0 &nbsp; + &nbsp; 1 × 0 = 4
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
layout: fact
hideInToc: true
---

# Byte

---
layout: fact
hideInToc: true
---

# Byte = 8 bits

---
layout: fact
hideInToc: true
---

# 00000000

---
layout: fact
hideInToc: true
---

# 11111111

---
layout: fact
hideInToc: true
---

# 10011001

## <span>2<sup>8</sup></span> = 256 possible values

---
hideInToc: true
---

# n Bits Hold 2ⁿ **Values**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔢 **Each bit doubles the count**

| Bits | Values | Enough for |
| --- | --- | --- |
| 1 | 2 | yes or no |
| 3 | 8 | the days of the week |
| 7 | 128 | the ASCII characters |
| 8 | 256 | one byte |
| 16 | 65 536 | a 16-bit sensor reading, 0 to 65 535 |
| 32 | about 4.3 × 10⁹ | the seconds of 136 years |

</div>

<div class="card card-secondary card-glass pad-compact">

## ↩️ **The other way round**

To tell *k* things apart, *n* bits are needed with 2ⁿ ≥ *k*.

- 26 letters: 2⁴ = 16 is too few, 2⁵ = 32 is enough. Five bits
- 10 digits: four bits, and six patterns stay unused
- 1000 weather stations: ten bits, because 2¹⁰ = 1024

</div>

</div>

<!--
**Ask:** how many bits for 26 letters? Let the room work it out before the answer.
**Say:** a 16-bit counter that passes 65 535 starts again at 0.
(~2 min)
-->

---
hideInToc: true
layout: fact
---

# Hexadecimal

## <v-click> **Base-16** </v-click>

---
layout: full
hideInToc: true
class: text-size-5.5
---

| **Decimal** | **Binary** | **Hex** | **Decimal** | **Binary** | **Hex** |
|-------------|------------|---------|-------------|------------|---------|
| 0           | 0000       | 0       | 8           | 1000       | 8       |
| 1           | 0001       | 1       | 9           | 1001       | 9       |
| 2           | 0010       | 2       | 10          | 1010       | A       |
| 3           | 0011       | 3       | 11          | 1011       | B       |
| 4           | 0100       | 4       | 12          | 1100       | C       |
| 5           | 0101       | 5       | 13          | 1101       | D       |
| 6           | 0110       | 6       | 14          | 1110       | E       |
| 7           | 0111       | 7       | 15          | 1111       | F       |

<style>
table {
  font-size: 0.9em;
}
td, th {
  padding-top: 0.3em;
  padding-bottom: 0.3em;
}
</style>

---
layout: center
hideInToc: true
class: text-center
---

# 0x2A in Decimal

<div class="powers">
    <span>16<sup>1</sup></span> &nbsp;&nbsp;&nbsp;
    <span>16<sup>0</sup></span>
</div>

<div class="number"> 2A</div>

<div class="expansion">
    16 × 2 &nbsp; + &nbsp; 1 × 10 = 42
</div>

<style>
    .powers {
        font-size: 50px;
    }
    .number {
        font-size: 200px;
    }
    .expansion {
        font-size: 50px;
    }
</style>

---
hideInToc: true
---

# From Decimal to **Binary and Hex**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ➗ **Decimal to binary: divide by 2**

```text
37 ÷ 2 = 18   remainder 1
18 ÷ 2 =  9   remainder 0
 9 ÷ 2 =  4   remainder 1
 4 ÷ 2 =  2   remainder 0
 2 ÷ 2 =  1   remainder 0
 1 ÷ 2 =  0   remainder 1
```

Read the remainders from the bottom up: `100101`. Check: 32 + 4 + 1 = 37.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🧩 **Binary to hex: groups of four**

```text
37  =    10 0101
    =  0010 0101     pad to full groups
    =     2    5
    =  0x25
```

One hex digit is exactly four bits, so a byte is always two hex digits. Check: 2 × 16 + 5 = 37.

</div>

</div>

<!--
**Do:** work 37 on the board.
**Ask:** the room converts 100 on paper. Answers: `1100100` and `0x64`.
**Say:** both are algorithms: a fixed list of steps that ends, with the same result whoever carries it out.
(~3 min)
-->

---
hideInToc: true
---

# Where Hex **Appears**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

🔢 **Bytes**: one byte is two hex digits, `00` to `FF`

</div>

<div class="card card-secondary card-glass pad-compact">

🎨 **Colours**: `#FF5733` is red `FF`, green `57`, blue `33`

</div>

<div class="card card-accent card-glass pad-compact">

💾 **Memory addresses**: `0x7FFE5A3C`

</div>

<div class="card card-info card-glass pad-compact">

🔬 **Hexdumps**: every byte of a file

</div>

</div>

<!--
**Say:** hex is short binary: four bits per digit, nothing else.
**Ask:** what is `FF` in decimal? 15 × 16 + 15 = 255.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# How Computers **Compute**

Numbers are bits, so arithmetic and logic are operations on 0 and 1. A processor runs them billions of times a second.

<!--
**Say:** binary addition, three logic gates, then the cycle a processor repeats.
(~1 min)
-->

---
layout: center
hideInToc: true
class: text-size-8
---

$$
\begin{array}{rccccc l}
{\scriptstyle\text{carries}} & {\scriptstyle 1} & {\scriptstyle 1} & {\scriptstyle 1} & & & \\
& & 1 & 0 & 1 & 1 & (11 \text{ in decimal}) \\
+ & & 0 & 1 & 1 & 0 & (\phantom{0}6 \text{ in decimal}) \\
\hline
& 1 & 0 & 0 & 0 & 1 & (17 \text{ in decimal})
\end{array}
$$

<div class="note-text mt-md text-center">

The only rule: <strong>1 + 1 = 10</strong>. Write 0, carry 1, as 7 + 5 in decimal writes 2 and carries 1.

</div>

<!--
**Do:** work it column by column from the right: 1 + 0 = 1; 1 + 1 = 0, carry 1; 0 + 1 + 1 = 0, carry 1; 1 + 0 + 1 = 0, carry 1; the last carry is the fifth bit.
**Say:** the same algorithm as school addition, with two symbols instead of ten.
(~2 min)
-->

---
layout: center
hideInToc: true
class: text-center
---

# Logical Operations

<div class="grid grid-cols-3 gap-8 text-3xl">

<div>
<h3>AND (&)</h3>
<table class="mx-auto">
<thead>
<tr><th>A</th><th>B</th><th>A&B</th></tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>1</td></tr>
</tbody>
</table>
</div>

<div>
<h3>OR (|)</h3>
<table class="mx-auto">
<thead>
<tr><th>A</th><th>B</th><th>A|B</th></tr>
</thead>
<tbody>
<tr><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>1</td><td>1</td></tr>
</tbody>
</table>
</div>

<div>
<h3>NOT (~)</h3>
<table class="mx-auto">
<thead>
<tr><th>A</th><th>~A</th></tr>
</thead>
<tbody>
<tr><td>0</td><td>1</td></tr>
<tr><td>1</td><td>0</td></tr>
</tbody>
</table>
</div>

</div>

<!--
**Say:** a gate takes bits in and gives one bit out. AND gives 1 only when both inputs are 1, OR when at least one is, NOT turns a bit over. Addition is built from such gates.
(~2 min)
-->

---
hideInToc: true
---

# Bitwise **Operations**

<div class="mt-sm">

```py {monaco-run} {autorun:false}
a = 0b1100  # 12 in decimal
b = 0b1010  # 10 in decimal

print(f"a & b = {a & b:04b}")  # 1000 (8)
print(f"a | b = {a | b:04b}")  # 1110 (14)
print(f"~a = {~a & 0b1111:04b}")  # 0011 (3)
```

</div>

<!--
**Ask:** predict each line from the tables of the last slide, bit by bit, then press ▶.
**If asked:** compression and encryption are built from such operations.
(~2 min)
-->

---
hideInToc: true
---

# How the CPU Runs an **Algorithm**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

📥 **Fetch**: read the next instruction, itself a binary number, from memory

</div>

<div class="card card-secondary card-glass pad-compact">

🔎 **Decode**: work out what it says: add, compare, jump

</div>

<div class="card card-accent card-glass pad-compact">

⚡ **Execute**: run it through circuits built from logic gates

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

Finding the largest number in `[7, 2, 9, 4]` is a compare and a jump, repeated. An algorithm becomes instructions, and instructions are numbers.

</div>

<!--
**Say:** fetch, decode, execute, billions of times a second. Software is data that the processor obeys.
(~2 min)
-->

---
hideInToc: true
---

# The Memory **Hierarchy**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Level | Where | Holds | One access |
| --- | --- | --- | --- |
| 🏎️ Registers | inside the CPU | a few hundred bytes | under 1 ns |
| ⚡ Cache | on the CPU chip | megabytes | a few ns |
| 🧠 RAM | main memory, lost at power-off | gigabytes | about 100 ns |
| 💽 Disk, SSD or HDD | a drive | terabytes | 0.1 to 10 ms |

</div>

<div class="card card-info card-glass pad-compact mt-md">

Each level away from the CPU is larger and slower. A read from disk takes about a million times as long as one from a register.

</div>

<!--
**Say:** 0.1 ms is 100 000 ns. This is why "the data does not fit in memory" changes how an analysis runs, and why the size of a file matters.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Numbers in **Computers**

A byte holds 256 values. More bits give more range and precision, and when the bits run out, a value wraps around or is rounded.

<!--
**Say:** two surprises in this section: an integer that wraps around without an error, and 0.1 + 0.2 that is not 0.3.
(~1 min)
-->

---
hideInToc: true
---

# Integers of Fixed **Width**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📏 **Common widths**

| Bits | Unsigned range |
| --- | --- |
| 8 | 0 to 255 |
| 16 | 0 to 65 535 |
| 32 | 0 to about 4.3 × 10⁹ |
| 64 | 0 to about 1.8 × 10¹⁹ |

Unix time counts seconds since 1970. Stored as a signed 32-bit integer, it runs out on 19 January 2038.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🚗 **Like an odometer**

```text
  99 999 km
+      1 km
= 00 000 km
```

Five digits hold 0 to 99 999. One more, and the dial starts again at 0.

A 16-bit counter is the same dial in binary: after 65 535 comes 0, with no error.

</div>

</div>

<div class="note-text mt-sm">A Python <code>int</code> grows as needed. Arrays and files use fixed widths.</div>

<!--
**Say:** a fixed width is a dial with a fixed number of positions. Past the last one it starts again from zero, and nothing warns you.
**Ask:** what does a 16-bit counter show after 65 536 events? 0.
(~2 min)
-->

---
hideInToc: true
---

# Negative Numbers: Count Back from **Zero**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🚗 **The odometer, backwards**

One step back from `000` shows `999`. Agree that `999` means −1, `998` means −2, and so on. Then addition still works:

```text
  005   (+5)
+ 999   (−1)
-----
 1004  → 004 = 4
```

The extra digit falls off the dial.

</div>

<div class="card card-accent card-glass pad-compact table-compact">

## 🔢 **The same in 4 bits**

| Pattern | Value |
| --- | --- |
| `0000` … `0111` | 0 … 7 |
| `1111` | −1 |
| `1110` | −2 |
| `1101` | −3 |
| … | … |
| `1000` | −8 |

The negative half is every pattern that starts with `1`: **two's complement**.

</div>

</div>

<div class="note-text mt-sm">8 bits hold −128 to 127, 16 bits −32 768 to 32 767.</div>

<!--
**Say:** hardware has no minus sign. Negative numbers are the top half of the dial, counted back from zero, and the ordinary adder handles them. Every processor does it this way.
**Ask:** which 4-bit pattern is −5? Five steps back from 0000: 1011.
**If asked:** the shortcut for −x is "flip every bit, add one": 0101 (5) → 1010 → 1011 (−5). A pattern that starts with 1 is its unsigned value minus 16: 1011 is 11 − 16 = −5.
(~3 min)
-->

---
hideInToc: true
---

# Overflow: **127 + 1** in 8 Bits

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 💥 **Past the positive half**

```py {monaco-run} {autorun:false}
import numpy as np
a = np.array([127], dtype=np.int8)  # 8 bits
print(a + 1)  # [-128]: wraps, no warning
```

127 is `01111111`, the last positive pattern. One step on is `10000000`, the first of the negative half: −128.

</div>

<div class="card card-primary card-glass pad-compact">

## 🏷️ **The type says what the bits mean**

```text
11111111  as unsigned 8-bit:  255
11111111  as signed 8-bit:     −1
```

The same bits, the same place on the dial. Only the type tells them apart, so the type is written down with the data.

</div>

</div>

<!--
**Say:** the NumPy line is not explained today. The point is that a fixed-width integer wraps with no error, here from the largest positive value into the negative half.
**Ask:** what is 11111110 as unsigned and as signed? 254 and −2.
(~2 min)
-->

---
hideInToc: true
---

# Floating Point: Scientific **Notation**

<div class="text-center text-4xl my-6">

$N = s \times m \times 10^{e} \qquad\qquad {-6.022} \times 10^{23}$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

**s**, the sign: **−1**

</div>

<div class="card card-primary card-glass pad-compact">

**m**, the mantissa: **6.022**, with 1 ≤ m < 10

</div>

<div class="card card-secondary card-glass pad-compact">

**e**, the exponent: **23**

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

A **float** is this idea in base 2, in a fixed number of bits. The mantissa has a fixed number of digits, so some decimals are rounded.

</div>

<!--
**Say:** a sign, significant digits, and a power that sets the scale.
(~2 min)
-->

---
hideInToc: true
---

# float32: **Sign, Exponent, Mantissa**

<div class="text-center text-3xl my-4">

$(-1)^{s} \times 1.m \times 2^{e - b}$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**s**, sign · **1 bit**

0 positive, 1 negative

</div>

<div class="card card-secondary card-glass pad-compact">

**e**, exponent · **8 bits**

stored as e + b, with the bias **b = 127**

</div>

<div class="card card-accent card-glass pad-compact">

**m**, mantissa · **23 bits**

the digits after the point of **1.m**; the leading 1 is not stored

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧩 1 + 8 + 23 = 32 bits, about **7 significant digits**. **float64**, the default of Python, has 1 + 11 + 52 bits, about **15 to 16 digits**.

</div>

<!--
**Say:** the bias lets the exponent be negative without a sign bit of its own: 2 to the power -3 is stored as 124.
(~2 min)
-->

---
hideInToc: true
---

# Worked Example: **5.75 as float32**

<div class="text-center text-3xl my-4">

  $(-1)^{0} \times 1.m \times 2^{e - b}$

</div>

<div class="card card-primary card-glass pad-tight mt-sm">

- 5 = 101₂ and 0.75 = 0.5 + 0.25 = 0.11₂, so 5.75 = 101.11₂
- In scientific notation: $1.0111_2 \times 2^2$
- **s** = 0 (positive)
- **e** = 2, stored as e + b = 2 + 127 = 129 = 10000001₂
- **m** = 01110000000000000000000, the digits after the point, filled to 23

</div>

<div class="text-center text-3xl mt-md">

`0 10000001 01110000000000000000000`

</div>

<!--
**Do:** work it on the board: move the point two places left, so the exponent is 2.
**Say:** sign, exponent, mantissa: 1 + 8 + 23 bits, read from left to right.
(~2 min)
-->

---
hideInToc: true
---

# Floating-Point **Rounding**

<div class="card card-warning card-glass pad-compact mt-md">

## ⚠️ **Not every decimal is exact in binary**

```py {monaco-run} {autorun:false}
print(0.1 + 0.2)            # 0.30000000000000004
print(0.1 + 0.2 == 0.3)     # False

import math                 # compare with a tolerance
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

</div>

<div class="note-text mt-sm">0.1 has no end in binary, as 1/3 has none in decimal. A finite number of bits means rounding.</div>

<!--
**Ask:** predict the first two lines before pressing ▶.
**Say:** two measured numbers are compared with a tolerance, never with ==.
(~2 min)
-->

---
hideInToc: true
---

# Why 0.1 Is **Not Exact**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ✖️ **A fraction to binary: multiply by 2**

```text
0.1 × 2 = 0.2   → 0
0.2 × 2 = 0.4   → 0
0.4 × 2 = 0.8   → 0
0.8 × 2 = 1.6   → 1   keep 0.6
0.6 × 2 = 1.2   → 1   keep 0.2
0.2 × 2 = 0.4   → 0   and it repeats
```

0.1 = 0.000110011001100…₂, without end.

</div>

<div class="card card-secondary card-glass pad-compact">

## ✂️ **The computer cuts it off**

- A float keeps 24 or 53 binary digits and rounds the rest
- The number stored for `0.1` is 0.1000000000000000055…
- 0.5, 0.25 and 0.375 are exact: sums of powers of 2
- 0.1, 0.2 and 0.3 are not, and their errors do not cancel

</div>

</div>

<div class="note-text mt-sm">Decimal has the same problem with 1/3 = 0.333…. Which fractions are exact depends on the base, not on the computer.</div>

<!--
**Do:** work the first four lines on the board.
**Say:** the stored 0.1 is 0.1000000000000000055511151231257827, the nearest float64.
(~3 min)
-->

---
hideInToc: true
---

# The Steps Between **Floats**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📏 **float32: 24 binary digits**

| Near | Step to the next float |
| --- | --- |
| 1 | 0.000 000 12 |
| 9.4 | 0.000 000 95 |
| 16 777 216 | 2 |

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎯 **What it means for data**

- `9.4`, a daily mean of `daily.csv`, is stored as 9.3999996185302734375, the nearest float32
- Digits after the seventh come from the rounding, not from the thermometer
- From 16 777 216 on, a float32 cannot count by one

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The relative step is constant, about 1 part in 10⁷ for float32. The absolute step grows with the number. Many small numbers added to one large number are lost.

</div>

<!--
**Say:** near 9.4 the step is 2 to the power -20. 16 777 216 is 2 to the power 24: above it the 24 digits no longer reach the ones place, and 16 777 216 + 1 gives 16 777 216.
**If asked:** sum in float64, store in float32 when 7 digits are enough.
(~2 min)
-->

---
hideInToc: true
---

# The Float Stored for **0.1**

<div class="card card-success card-glass pad-compact mt-md">

## 🧪 **Predict each line, then press ▶**

```py {monaco-run} {autorun:false}
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
```

</div>

<div class="note-text mt-sm">The third line prints 20 decimals of the number really stored for <code>0.1</code>.</div>

<!--
**Ask:** predictions from three students before pressing ▶. The third line prints 0.10000000000000000555.
**Say:** this is not a bug. Every computer stores decimals this way.
(~2 min)
-->

---
hideInToc: true
---

# The Type of a **Value**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

🔢 **Integer**, `int`: `42`, `-7`. Fixed width in arrays and files

</div>

<div class="card card-secondary card-glass pad-compact">

📐 **Float**, `float`: `3.14`, `6.022e23`. Rounded to a fixed number of digits

</div>

<div class="card card-accent card-glass pad-compact">

🔤 **String**, `str`: `"Vilnius"`, `"α"`. Characters, stored by an encoding

</div>

<div class="card card-success card-glass pad-compact">

✅ **Boolean**, `bool`: `True` or `False`. One yes-or-no answer

</div>

</div>

<div class="note-text mt-sm">Every value in a program has a type. The type decides what the bits mean, how much memory a value takes, and what can be done with it.</div>

<!--
**Say:** the names are those of Python.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Text & **Encodings**

Text needs two tables: one from characters to numbers, and one from numbers to bytes. ASCII, Unicode and UTF-8 are those tables.

<!--
**Say:** ASCII is the 7-bit table everyone agrees on. Unicode numbers every character of every script. UTF-8 turns those numbers into bytes and leaves ASCII text unchanged.
(~1 min)
-->

---
layout: fact
hideInToc: true
---

# ASCII

## American Standard Code for Information Interchange

### 7-bit

---
hideInToc: true
class: text-size-5
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---------|----------|---------|----------|---------|----------|---------|----------|---------|----------|---------|----------|---------|----------|---------|----------|
|   0     | **NUL**  |   16    | **DLE**  |   32    | **SP**   |   48    | **0**    |   64    | **@**    |   80    | **P**    |   96    | **`**    |  112    | **p**    |
|   1     | **SOH**  |   17    | **DC1**  |   33    | **!**    |   49    | **1**    |   65    | **A**    |   81    | **Q**    |   97    | **a**    |  113    | **q**    |
|   2     | **STX**  |   18    | **DC2**  |   34    | **"**    |   50    | **2**    |   66    | **B**    |   82    | **R**    |   98    | **b**    |  114    | **r**    |
|   3     | **ETX**  |   19    | **DC3**  |   35    | **#**    |   51    | **3**    |   67    | **C**    |   83    | **S**    |   99    | **c**    |  115    | **s**    |
|   4     | **EOT**  |   20    | **DC4**  |   36    | **$**    |   52    | **4**    |   68    | **D**    |   84    | **T**    |  100    | **d**    |  116    | **t**    |
|   5     | **ENQ**  |   21    | **NAK**  |   37    | **%**    |   53    | **5**    |   69    | **E**    |   85    | **U**    |  101    | **e**    |  117    | **u**    |
|   6     | **ACK**  |   22    | **SYN**  |   38    | **&**    |   54    | **6**    |   70    | **F**    |   86    | **V**    |  102    | **f**    |  118    | **v**    |
|   7     | **BEL**  |   23    | **ETB**  |   39    | **'**    |   55    | **7**    |   71    | **G**    |   87    | **W**    |  103    | **g**    |  119    | **w**    |

*(excerpt: the first 8 rows of each block)*

<div class="card card-info card-glass pad-compact mt-sm">

🔢 Sorted as text, `10.4` comes before `5.0`. The first bytes decide: `1` is 49 = 0x31, `5` is 53 = 0x35, and 0x31 < 0x35.

</div>

<!--
**Say:** a text sort compares the first byte of each line, and looks further only on a tie. So the nine temperatures of `daily.csv`, sorted as text, start with 10.4.
**Ask:** where does `9.8` go? Last: `9` is 0x39.
(~2 min)
-->

---
hideInToc: true
---

# Unicode and **UTF-8**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🌐 **Unicode**

A number, the **code point**, for every character of every script:

- U+0041 = `A`
- U+0105 = `ą`
- U+03B1 = `α`
- U+1F600 = `😀`

</div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **UTF-8**

Stores a code point in 1 to 4 bytes. The 128 ASCII characters keep their single byte, so an ASCII file is already UTF-8.

</div>

</div>

<!--
**Say:** ASCII has 128 characters. Lithuanian letters, Greek, emoji need Unicode, and Unicode needs a way to become bytes: an encoding.
(~2 min)
-->

---
hideInToc: true
---

# How UTF-8 Packs a **Code Point**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📦 **The four patterns**

| Up to | Bit pattern |
| --- | --- |
| U+007F | `0xxxxxxx` |
| U+07FF | `110xxxxx 10xxxxxx` |
| U+FFFF | `1110xxxx 10xxxxxx 10xxxxxx` |
| U+10FFFF | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

</div>

<div class="card card-secondary card-glass pad-compact">

## ✍️ **`ą` by hand**

```text
ą = U+0105 = 1 0000 0101    two bytes
as 11 bits:  00100 000101
pattern:     110xxxxx 10xxxxxx
filled in:   11000100 10000101
in hex:      C4       85
```

</div>

</div>

<div class="note-text mt-sm">The first bits of a byte say what it is: <code>0</code> a whole ASCII character, <code>110</code>, <code>1110</code> or <code>11110</code> the start of a longer one, <code>10</code> a continuation.</div>

<!--
**Do:** fill in the 11 bits on the board, five into the first byte and six into the second.
**Say:** a program can start reading anywhere in a file and find the next character.
(~3 min)
-->

---
hideInToc: true
---

# Text and **Bytes** in Python

<div class="mt-sm">

```py {monaco-run} {autorun:false}
s = "Å and 😊"            # str: Unicode characters
b = s.encode("utf-8")     # bytes
print(len(s), len(b))     # 7 11: Å takes 2 bytes, 😊 takes 4
print(b)                  # b'\xc3\x85 and \xf0\x9f\x98\x8a'
print(b.decode("utf-8"))  # back to str
```

</div>

<!--
**Ask:** 7 characters; how many bytes? Count: 5 ASCII characters, 2 for Å, 4 for the emoji: 11.
(~2 min)
-->

---
hideInToc: true
---

# Mojibake: Bytes Read by the Wrong **Table**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔍 **How it happens**

`ą` in UTF-8 is two bytes: `C4 85`.

Read by a one-byte table such as Windows-1252, `C4` is `Ä` and `85` is `…`. So `ą` shows as `Ä…`.

</div>

<div class="card card-warning card-glass pad-compact">

## 📄 **In a real file**

`Žagarė` shows as `Å½agarÄ—`.

`Å` and `Ä` scattered through Lithuanian text are UTF-8 bytes read by a one-byte table.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 The bytes are fine, so nothing is retyped. The file is read again with the right table: **Reopen with Encoding** in VS Code.

</div>

<!--
**Say:** mojibake is Japanese for "character transformation". The bytes are right; the table used to read them is wrong.
(~2 min)
-->

---
hideInToc: true
---

# Encoding and Line Ending in **VS Code**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔤 **`UTF-8` in the Status Bar**

- The table VS Code used to read the file
- **Reopen with Encoding** reads the same bytes by another table
- **Save with Encoding** writes other bytes. Only on purpose

</div>

<div class="card card-secondary card-glass pad-compact">

## ↵ **`LF` or `CRLF`**

- A line break is a byte too: `0A`, called LF, on macOS and Linux
- Windows writes two: `0D 0A`, called CRLF
- `daily.csv` with LF: 148 bytes. With CRLF: 148 + 10 = 158

</div>

</div>

<div class="note-text mt-sm"><code>ą</code> is two bytes in UTF-8, <code>C4 85</code>, and one byte in the Baltic table Windows-1257, <code>E0</code>. <code>a</code> to <code>z</code> are the same byte in every table.</div>

<!--
**Say:** **Reopen with Encoding** is the repair of the last slide: the same bytes, read by another table. **Save with Encoding** changes the bytes.
**If asked:** names of files and folders keep to `a` to `z` because those bytes are the same in every table.
(~2 min)
-->

---
hideInToc: true
---

# What a Spreadsheet **Changes**

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

## 🧨 **Open and save a CSV**

- Text re-encoded in the laptop's own table, not UTF-8
- Names turned into **dates**: the gene `SEPT2` becomes `2-Sep`
- **Leading zeros** dropped: `007` becomes `7`

</div>

<div class="card card-info card-glass pad-compact">

## 🫥 **The BOM**

Some programs put three bytes, `EF BB BF`, before the first character of a UTF-8 file: the **byte-order mark**.

A program that does not expect it reads `ï»¿` before the first column name.

</div>

</div>

<div class="note-text mt-sm">A data file is bytes with a declared encoding. Look at it first, and edit it only with tools that change nothing on their own.</div>

<!--
**Say:** gene names turned into dates were found in about one fifth of genomics papers with gene lists (Ziemann et al., 2016).
**If asked:** Python reads a file with a BOM with `encoding="utf-8-sig"`.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Files & **Formats**

A file is a named sequence of bytes: a size, an order for the bytes of one number, and first bytes that say how to read the rest.

<!--
**Say:** sizes, byte order, the first bytes of a file, then the hexdump that names every byte of `daily.csv`.
(~1 min)
-->

---
hideInToc: true
---

# File **Sizes**

<div class="card card-info card-glass pad-compact table-compact mt-sm">

| Unit | Size | For example |
| --- | --- | --- |
| 1 byte | 8 bits | one ASCII character |
| 1 kB | 1000 bytes | a short email |
| 1 MB | 1000 kB | a photograph |
| 1 GB | 1000 MB | about 250 songs as MP3 |
| 1 TB | 1000 GB | about 500 hours of video |

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Two conventions: **kB, MB, GB** in powers of 1000, and **KiB, MiB, GiB** in powers of 1024. A 1 TB drive holds 10¹² bytes = 931 GiB, which Windows shows as "931 GB".

</div>

<!--
**Say:** the size in bytes is exact. KB and MB are rounded, and counted in two ways. 10 to the power 12 divided by 1024 cubed is 931.3.
(~2 min)
-->

---
hideInToc: true
---

# Byte **Order**

<div class="card card-info card-glass pad-compact mt-sm">

A number of four bytes, `0x12345678`, can be stored with either end first.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📦 **Big-endian**

The most significant byte first:

`12 34 56 78`

Used by network protocols.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **Little-endian**

The least significant byte first:

`78 56 34 12`

Used by x86 and ARM processors: most laptops and phones.

</div>

</div>

<div class="note-text mt-sm">The wrong order gives a wrong number with no error. A description of a binary file names its byte order.</div>

<!--
**Say:** the names come from Gulliver's Travels: which end of an egg to open.
**If asked:** NumPy writes the byte order into the type of an array.
(~2 min)
-->

---
hideInToc: true
---

# The First Bytes of a **File**

<div class="card card-info card-glass pad-compact mt-sm">

The ending of a file name is a hint for people. The first bytes, the **magic number**, say what the file is.

</div>

<div class="card card-primary card-glass pad-compact table-compact mt-md">

| Kind | Endings | First bytes |
| --- | --- | --- |
| Text and data | `.txt`, `.csv`, `.json`, `.md` | none: the text itself |
| PNG picture | `.png` | `89 50 4E 47`, shown as `.PNG` |
| PDF document | `.pdf` | `25 50 44 46`, shown as `%PDF` |
| ZIP archive, and `.docx`, `.xlsx` inside | `.zip`, `.docx`, `.xlsx` | `50 4B`, shown as `PK` |

</div>

<!--
**Say:** a Word file is a ZIP archive of XML files. Renaming `report.docx` to `report.zip` and unpacking it shows them.
(~2 min)
-->

---
hideInToc: true
---

# Install the **Hex Editor**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧩 **An extension**

- A program added to VS Code from its catalogue, the **Marketplace**
- Extensions view: `Ctrl+Shift+X` (macOS `Cmd+Shift+X`)
- Each result shows its **publisher**

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔬 **Hex Editor, by Microsoft**

- Search `hex editor`, take the one by **Microsoft**, **Install**
- Right-click a file, **Open With…**, **Hex Editor**

</div>

</div>

<div class="note-text mt-sm">Two extensions can share a name. The publisher is the check.</div>

<!--
**Say:** a `.csv` opens as text by default. Open With chooses the viewer for this one opening.
(~2 min)
-->

---
hideInToc: true
---

# Reading a **Hexdump**

<div class="card card-primary card-glass pad-compact mt-sm">

```text
daily.csv, the first 32 of 148 bytes
00000000  64 61 74 65 2c 74 65 6d  70 5f 63 0a 32 30 32 35  |date,temp_c.2025|
00000010  2d 31 30 2d 30 31 2c 36  2e 33 0a 32 30 32 35 2d  |-10-01,6.3.2025-|
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 👀 **How to read it**

- Left: the **offset**, the number of the first byte, in hex
- Middle: 16 bytes as hex pairs
- Right: the same bytes as ASCII, `.` for a byte that is not a printable character

</div>

<div class="card card-success card-glass pad-compact table-compact">

## 🧮 **All 148 bytes**

| Bytes | Count |
| --- | --- |
| digits, `30` to `39` | 91 |
| hyphens, `2d` | 18 |
| commas, `2c` | 10 |
| points, `2e` | 9 |
| letters and `_` | 10 |
| line breaks, `0a` | 10 |

</div>

</div>

<!--
**Do:** read the first line byte by byte with the ASCII table: 64 is d, 61 is a, 2c is the comma.
**Say:** 91 + 18 + 10 + 9 + 10 + 10 = 148. The ten bytes nobody sees in the editor are the line breaks, `0a`. No `EF BB BF` at offset 0, so no BOM.
(~3 min)
-->

---
hideInToc: true
---

<div class="grid-2 gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **−16.3 as text**

```text
-16.3
2D 31 36 2E 33
```

Five characters, five bytes. Any program and any person can read them.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **−16.3 as a float32**

```text
-16.3
66 66 82 C1
```

Always four bytes. They mean nothing until the reader knows the type, the byte order and where the number starts.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A row of the station's hourly log, `2016-01-01T00:00,-4.4,93,2.5`, is 29 bytes as text. As binary it is 16: a 4-byte hour count and three float32. For 87 672 rows: 2.5 MB against 1.4 MB.

</div>

<!--
**Say:** read the text bytes with the ASCII table: 2D is the minus sign, 2E the point. The float32 bytes are sign, exponent and mantissa, lowest byte first.
**If asked:** 2 515 215 bytes for the text file against 87 672 × 16 = 1 402 752: a factor of 1.8. Text costs space and is read by everything; binary is compact and needs its description.
(~2 min)
-->

---
hideInToc: true
---

# Bit Depth of an **Image**

<div class="note-text mt-sm">The same picture with fewer bits per pixel: fewer colours, and fewer bytes before compression.</div>

<div class="grid grid-cols-5 gap-4 mt-md">
  <figure>
    <img src="/figures/elf_24bit.jpg" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">24 bit</figcaption>
  </figure>
  <figure>
    <img src="/figures/elf_4bit.png" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">4 bit</figcaption>
  </figure>
  <figure>
    <img src="/figures/elf_3bit.png" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">3 bit</figcaption>
  </figure>
  <figure>
    <img src="/figures/elf_2bit.png" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">2 bit</figcaption>
  </figure>
  <figure>
    <img src="/figures/elf_1bit.png" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">1 bit</figcaption>
  </figure>
</div>

<!--
**Ask:** how many colours has a 4-bit picture? 2 to the power 4 = 16. A 1-bit picture has 2.
(~1 min)
-->

---
layout: section
hideInToc: true
---

# Files from the **Terminal**

The Hex Editor showed the bytes of one file by clicks. A terminal reaches files and their bytes by typed lines, and a typed line can be written down and run again.

<!--
**Say:** seven commands, `pwd` to `rm`, to look around and to change folders and files, then two that measure a file. All of them work in zsh on a Mac and in both PowerShells of Windows, 5.1 and 7.
(~1 min)
-->

---
hideInToc: true
---

<div class="grid-2 gap-md">

<div class="card card-primary card-glass pad-compact">

## 🖥️ **Terminal**

The window. It shows text and passes on what is typed. VS Code has one in its Panel.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🐚 **Shell**

The program in the window. It reads a typed line, runs it, prints the answer, and waits for the next line.

</div>

</div>

<div class="card card-info card-glass pad-compact table-compact mt-md">

| System | Shell | The prompt ends in | On these slides |
| --- | --- | --- | --- |
| macOS | `zsh` | `%` | `% pwd` |
| Windows | PowerShell, 5.1 built in or 7 | `>` | `PS> pwd` |

</div>

<div class="note-text mt-sm">The mark at the start of a line on a slide is not typed. It shows which shell the line is for.</div>

<!--
**Say:** terminal is the window, shell is the program in it. The words are often used for each other; today they are kept apart.
(~2 min)
-->

---
hideInToc: true
---

# Open the **Terminal**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🧭 **In VS Code**

1. **File**, **Open Folder…**, the folder `weather-project`
2. **Terminal**, **New Terminal**
3. The Panel opens at the bottom, in the project folder. Its top right names the shell: `zsh`, `powershell` or `pwsh`

</div>

<div class="note-text mt-sm">The key is <code>Ctrl+`</code> on both systems: the backtick, left of <code>1</code>. The same shells also run in the apps called Terminal on macOS and on Windows.</div>

<!--
**If asked:** `powershell` is Windows PowerShell 5.1, `pwsh` is PowerShell 7. Both run every line of this section.
(~2 min)
-->

---
hideInToc: true
---

# Read the **Prompt**

<div class="card card-primary card-glass pad-compact table-compact mt-sm">

| Shell | The prompt, as it first appears |
| --- | --- |
| zsh, macOS | `smilte@MacBook-Air weather-project %` |
| PowerShell, Windows | `PS C:\Users\smilte\Documents\weather-project>` |

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 👤 **Who**

`smilte@MacBook-Air`: the user and the computer. zsh only

</div>

<div class="card card-accent card-glass pad-compact">

## 📂 **Where**

The folder the shell is in, the **working directory**. zsh shows its name, PowerShell its whole path

</div>

<div class="card card-info card-glass pad-compact">

## ⏳ **Waiting**

`%` or `>`: the shell waits for a line

</div>

</div>

<!--
**Ask:** read the two prompts aloud, part by part: who, where, waiting.
**Say:** every command below starts from the working directory.
(~2 min)
-->

---
hideInToc: true
---

# Where Am I: **`pwd`**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% pwd
/Users/smilte/Documents/weather-project
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> pwd

Path
----
C:\Users\smilte\Documents\weather-project
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`pwd`, **print working directory**: the path from the top of the disk, `/` on macOS and `C:\` on Windows, down to this folder. A path from the top is **absolute**.

</div>

<!--
**Do:** read the answer from left to right as a walk down the folders.
**Ask:** why would three laptops print three different paths? The user names differ.
(~2 min)
-->

---
hideInToc: true
---

# What Is Here: **`ls`**

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% ls
README.md  data  results  scripts
```

</div>

<div class="card card-info card-glass pad-compact">

`ls` lists the working directory. zsh prints the names. PowerShell prints a table: `d` marks a folder, **Length** is a size in bytes.

</div>

</div>

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🪟 **Windows · PowerShell**

```text
PS> ls

    Directory: C:\Users\smilte\Documents\weather-project

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          2026-10-13    10:12                data
d----          2026-10-13    10:12                results
d----          2026-10-13    10:12                scripts
-a---          2026-10-13    10:12            688 README.md
```

</div>

<!--
**Say:** the same four names as in the Side Bar of VS Code.
**If asked:** the date column of PowerShell follows the laptop's language settings.
(~2 min)
-->

---
hideInToc: true
---

# Change Folder: **`cd`**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh**, the whole prompt shown

```text
smilte@MacBook-Air weather-project % cd data
smilte@MacBook-Air data % cd processed
smilte@MacBook-Air processed % cd ../..
smilte@MacBook-Air weather-project %
```

</div>

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🪟 **Windows · PowerShell**, the whole prompt shown

```text
PS C:\Users\smilte\Documents\weather-project> cd data
PS C:\Users\smilte\Documents\weather-project\data> cd ..
PS C:\Users\smilte\Documents\weather-project>
```

</div>

<div class="note-text mt-sm"><code>data</code> is a <b>relative</b> path: it starts at the working directory. <code>..</code> is the folder above. The prompt shows every move.</div>

<!--
**Do:** follow the prompt line by line: after each `cd` it names the new folder.
**Say:** `cd` with no path goes to the home folder; `cd ~/Documents/weather-project` comes back from anywhere.
(~2 min)
-->

---
hideInToc: true
---

# Make a Folder: **`mkdir`**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh**

```text
% mkdir backup
% ls
README.md  backup  data  results  scripts
```

</div>

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🪟 **Windows · PowerShell**

```text
PS> mkdir backup

    Directory: C:\Users\smilte\Documents\weather-project

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          2026-10-13    10:14                backup
```

</div>

<div class="note-text mt-sm"><code>mkdir</code>, <b>make directory</b>, is the same word in both shells.</div>

<!--
**Say:** a name without spaces is one word for the shell. `my backup` would be read as two names.
(~1 min)
-->

---
hideInToc: true
---

# Copy and Rename: **`cp`**, **`mv`**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · 🪟 **Windows · PowerShell**, the same three lines

```text
% cp data/processed/daily.csv backup
% mv backup/daily.csv backup/daily_copy.csv
% ls backup
daily_copy.csv
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

## 📋 **`cp FILE FOLDER`**

Copies the file into the folder, under the same name.

</div>

<div class="card card-accent card-glass pad-compact">

## ✏️ **`mv OLD NEW`**

Moves a file. A new name in the same folder renames it.

</div>

</div>

<div class="note-text mt-sm">In PowerShell, <code>ls backup</code> prints the table of the last slides, with <b>Length</b> 148: the copy has every byte.</div>

<!--
**Say:** `cp` replaces a file of the same name without asking, in both shells. In PowerShell the lines start at `PS>`.
(~2 min)
-->

---
hideInToc: true
---

# Delete: **`rm`**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh** · 🪟 **Windows · PowerShell**, the same two lines

```text
% rm backup/daily_copy.csv
% rm -r backup
```

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ No Trash, no Recycle Bin, and `Ctrl+Z` brings nothing back. `rm -r` deletes a folder with everything in it. Before `rm`, check with `pwd` and `ls` where you are and what is there.

</div>

<!--
**Say:** read the name before pressing Enter: `rm` has no undo. `-r` is an option: it changes how `rm` works, here "the folder and all inside it".
**If asked:** in PowerShell `rm` is a short name for `Remove-Item`, and `-r` for `-Recurse`.
(~2 min)
-->

---
hideInToc: true
---

# The Size of a **File**

<div class="note-text"><code>daily_crlf.csv</code> is a copy of <code>daily.csv</code>, saved with <code>CRLF</code> from the Status Bar of VS Code.</div>

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% wc -c data/processed/daily.csv
     148 data/processed/daily.csv
% wc -c data/processed/daily_crlf.csv
     158 data/processed/daily_crlf.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Get-Item data/processed/daily.csv).Length
148
PS> (Get-Item data/processed/daily_crlf.csv).Length
158
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

`wc -c` counts bytes. `Get-Item` fetches the file, and `.Length` is its size in bytes. 158 − 148 = 10: one `0d` more on each of the ten lines.

</div>

<!--
**Say:** the size is exact to the byte, unlike KB in a file manager.
**If asked:** the copy is `cp data/processed/daily.csv data/processed/daily_crlf.csv`, then `LF` to `CRLF` in the Status Bar of the copy, and save.
(~2 min)
-->

---
hideInToc: true
---

# The Bytes of a **File**

<div class="card card-primary card-glass pad-compact mt-sm">

## 🍎 **macOS · zsh**, the first two and the last lines

```text
% hexdump -C data/processed/daily.csv
00000000  64 61 74 65 2c 74 65 6d  70 5f 63 0a 32 30 32 35  |date,temp_c.2025|
00000010  2d 31 30 2d 30 31 2c 36  2e 33 0a 32 30 32 35 2d  |-10-01,6.3.2025-|
00000090  39 2e 38 0a                                       |9.8.|
00000094
```

</div>

<div class="card card-secondary card-glass pad-compact mt-sm">

## 🪟 **Windows · PowerShell**, the first two lines

```text
PS> Format-Hex data/processed/daily.csv
          Offset Bytes                                           Ascii
0000000000000000 64 61 74 65 2C 74 65 6D 70 5F 63 0A 32 30 32 35 date,temp_c�2025
0000000000000010 2D 31 30 2D 30 31 2C 36 2E 33 0A 32 30 32 35 2D -10-01,6.3�2025-
```

</div>

<div class="note-text mt-sm"><code>hexdump</code> ends on the size in hex: 0x94 = 9 × 16 + 4 = 148.</div>

<!--
**Do:** find the first `0a` with the room.
**Say:** a `hexdump` line has 16 bytes; 148 bytes take 9 full lines and 4 bytes.
**If asked:** Format-Hex also prints a Label line with the path and two header lines; Windows PowerShell 5.1 prints the same bytes in an older layout.
(~2 min)
-->

---
layout: section
hideInToc: true
---

# Compression & **Integrity**

A file can be stored in fewer bytes without losing one, and a short number computed from its bytes shows whether any of them changed.

<!--
**Say:** lossless against lossy, then a checksum by hand, then SHA-256 by command.
(~1 min)
-->

---
hideInToc: true
---

# **Compression**

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 🔒 **Lossless**

Removes repeats and gives back **every byte**: ZIP, gzip, PNG.

`AAABBBCC` becomes `3A3B2C`: 8 characters, then 6.

</div>

<div class="card card-warning card-glass pad-compact">

## 📉 **Lossy**

Drops detail the eye or ear misses: JPEG, MP3. Fine for photos, never for data.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🗜️ The station's hourly log, `weather.csv`: 2 515 215 bytes. With gzip: 553 660 bytes, 22 %. Unpacked again, it is the same 2 515 215 bytes.

</div>

<!--
**Say:** text repeats itself: every line of the log starts with `20`, a dash, and a month. gzip replaces each repeat with a short reference to an earlier copy.
(~2 min)
-->

---
hideInToc: true
---

# A Checksum **by Hand**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ➕ **Add up the bytes**

```text
a    b    c
97 + 98 + 99 = 294
294 mod 256  =  38     the checksum, one byte
```

The sender stores 38 next to the file. The receiver adds the bytes again and compares.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **What it catches**

- `abd` gives 39: one changed byte is caught
- `acb` gives 38: two swapped bytes are not
- One byte 1 too high and another 1 too low are not

</div>

</div>

<div class="note-text mt-sm">Every such check is a short number computed from all the bytes. A better rule misses fewer changes: a parity bit, a CRC, a cryptographic hash.</div>

<!--
**Ask:** what does `abc` give with `c` changed to `d`? 39.
**Say:** SHA-256 is built so that nobody can construct a change that keeps the same number.
(~2 min)
-->

---
hideInToc: true
---

# SHA-256, a **Hash**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% shasum -a 256 data/processed/daily.csv
33fe5e77…f705483d  data/processed/daily.csv
% shasum -a 256 data/processed/daily_crlf.csv
b68430c5…721a899e  data/processed/daily_crlf.csv
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> (Get-FileHash data/processed/daily.csv).Hash
33FE5E77…F705483D
PS> (Get-FileHash data/processed/daily_crlf.csv).Hash
B68430C5…721A899E
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

64 hex digits, 256 bits, computed from every byte. The same bytes give the same hash on every computer. Ten more bytes, the `0d`s, give a hash that differs in every digit.

</div>

<!--
**Say:** the slide shortens the 64 digits to the first and last eight. Lower or upper case is the same number.
**Ask:** two people each have a `daily.csv`. How do they know it is the same 148 bytes? Compare the first and the last eight digits.
(~2 min)
-->

---
hideInToc: true
---

# Key **Takeaways**

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

💡 **Bits**: everything in a computer is 0 and 1. Eight bits are a byte, two hex digits

</div>

<div class="card card-secondary card-glass pad-compact">

🔢 **Numbers**: integers of fixed width wrap around, floats are rounded

</div>

<div class="card card-accent card-glass pad-compact">

🔤 **Text**: an encoding is the table from characters to bytes; UTF-8 is the usual one

</div>

<div class="card card-info card-glass pad-compact">

📁 **Files**: a named sequence of bytes. The size is exact, the first bytes say what it is

</div>

<div class="card card-success card-glass pad-compact">

⌨️ **Terminal**: `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`, the size and the bytes of a file

</div>

<div class="card card-warning card-glass pad-compact">

🧾 **Integrity**: a hash shows whether a single byte changed

</div>

</div>

<!--
**Say:** before an algorithm runs on a file, it is worth knowing what the file is made of.
(~1 min)
-->

---
hideInToc: true
---

# **Recap**: You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Convert between **binary**, **decimal** and **hexadecimal**

</div>

<div class="card card-success card-glass pad-compact">

✅ Spot **overflow** and **rounding** in integers and floats

</div>

<div class="card card-success card-glass pad-compact">

✅ Explain how text becomes **bytes**, and why letters turn into `Ä…`

</div>

<div class="card card-success card-glass pad-compact">

✅ Move through folders and copy, rename and delete files from the **terminal**

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

## 🔬 **The 148 bytes of `daily.csv`**

91 digits, 18 hyphens, 10 commas, 9 points, 10 letters and `_`, and 10 line breaks `0a`. Size, encoding, line ending and hash of a data file are checked before a number in it is trusted.

</div>

<!--
**Say:** back to the opening: ten short lines, 148 bytes, every one of them named. The ten that nobody sees are the line breaks.
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
  question="A sensor writes each reading as a 2-byte (16-bit) unsigned integer. How many distinct values can one reading take?"
  :options="[
    '256',
    '65,536',
    '32,768',
    '16'
  ]"
  :correct="1"
  explanation="16 bits give 2^16 = 65,536 values, from 0 to 65,535. Each extra bit doubles the count: 2 bytes are 256 × 256. A reading above that needs a wider type, or it wraps around."
/>

---
hideInToc: true
---

<MCQ
  question="In two's complement, what decimal value does the 4-bit pattern 1010 represent?"
  :options="[
    '10',
    '−6',
    '6',
    '−2'
  ]"
  :correct="1"
  explanation="1010 starts with 1, so it is in the negative half. Count back from 0000: 1111 is −1, 1110 −2, 1101 −3, 1100 −4, 1011 −5, 1010 −6. Read as an unsigned integer the same four bits are 10, and 10 − 16 = −6."
/>

---
hideInToc: true
---

<MCQ
  question="What is a file, at the simplest level?"
  :options="[
    'A window shown on the screen',
    'A named sequence of bytes stored by the operating system',
    'A running program in memory',
    'A network connection to another computer'
  ]"
  :correct="1"
  explanation="Text, pictures and programs are all named sequences of bytes. The ending of the name is only a hint at how to read them; the first bytes say what the file is."
/>

---
hideInToc: true
---

<MCQ
  question="The published SHA-256 of data.csv differs in every digit from the SHA-256 of your copy. What can you conclude?"
  :options="[
    'The files are almost identical: only a few bytes differ',
    'Your copy differs from the published file somewhere: one changed bit is enough',
    'The hash tool is broken: a small change should change only a few digits',
    'Nothing: SHA-256 gives a different result every time it runs'
  ]"
  :correct="1"
  explanation="Any change, however small, changes the whole hash. So the hash says that something differs, never how much. The same bytes always give the same 64 hex digits, on every computer."
/>

---
hideInToc: true
---

<MCQ
  question="The prompt is `PS C:\Users\smilte\Documents\weather-project\data>`. Which line prints the size of `daily.csv` in `data/processed`?"
  :options="[
    '(Get-Item processed/daily.csv).Length',
    '(Get-Item data/processed/daily.csv).Length',
    '(Get-Item ../daily.csv).Length',
    '(Get-Item ~/daily.csv).Length'
  ]"
  :correct="0"
  explanation="The working directory is data, so a relative path starts there: processed/daily.csv. The second line would look for data/data/processed/daily.csv."
/>
