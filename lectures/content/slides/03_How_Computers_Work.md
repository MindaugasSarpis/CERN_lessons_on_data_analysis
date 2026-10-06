---
layout: cover
title: "How Computers Work"
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## How Computers Work

##### <span class="aims-badge">🔧 tool-agnostic · 📁 data & files</span>

<!--
Speaker: this lecture is the foundation layer — how a computer actually stores
the data you'll analyse. No coding today; it's the mental model everything else
rests on. Tool-agnostic and file-literate is the goal. The previous lecture
ended on a text file in which 100 sorted before 20, because the editor saw
characters. Today is what characters and numbers are underneath. (~1 min)
-->

---
layout: quote
hideInToc: true
---

# The main goal of this lecture is to understand what data is **made of** — bits, bytes, numbers, text, files — and how a computer turns an **algorithm** into operations on them

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🧠 Trace how data is represented — **bits → bytes → numbers → text → files** — with a nod to how the CPU executes an **algorithm**

</div>

<div class="card card-secondary card-glass pad-compact">

🔢 Convert numbers between **binary**, **decimal**, and **hexadecimal**

</div>

<div class="card card-accent card-glass pad-compact">

🔤 Explain how text becomes bytes through **ASCII** and **UTF-8**

</div>

<div class="card card-success card-glass pad-compact">

📐 Predict **overflow** and **rounding** in fixed-width ints and floats

</div>

<div class="card card-warning card-glass pad-compact">

📁 See a file as a named sequence of **bytes** — format, size, encoding

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. Today is the mental model —
bits up to files — of what a computer stores and how. (~1 min)
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

---
hideInToc: true
---

# What is an <span class="gradient-text">Algorithm</span>?

<div class="card card-info card-glass pad-compact mt-sm glow">

An **algorithm** is a **finite sequence of well-defined instructions** to solve a problem — the recipe inside the "box."

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-scale">

## 🍳 **Everyday Example**

1. Boil water → add pasta → wait 10 min
2. Drain → serve

**Input:** raw pasta → **Output:** cooked pasta

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale">

## 📖 **Finding a Word in a Dictionary**

1. Open to the middle
2. Is your word before or after?
3. Go to the correct half, repeat

**Input:** "Python" → **Output:** page 742

</div>

</div>

---
hideInToc: true
---

# **Try It** — Think Like a CPU

<div class="card card-success card-glass pad-tight mt-sm">

## 🧮 **Find the Maximum, Step by Step**

Given a list, e.g. `[7, 2, 9, 4]` — work through it **one instruction at a time**, the way a processor would:

1. Set `max` = the first number
2. Look at the next number
3. Is it bigger than `max`? If yes, replace `max`
4. Repeat steps 2–3 until the list is exhausted
5. `max` now holds the answer

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 No shortcuts, no "just looking at it" — every step is explicit and repeatable. That is an algorithm. A CPU does exactly this — we'll meet its **fetch–decode–execute** cycle in the *How Computers Compute* section — just with circuits instead of pen and paper.

</div>

<!--
Speaker: give them 60 seconds with the list on paper; ask one student to read
out the value of `max` after each step. The point is that "repeat until the
list is exhausted" is a loop and step 3 is a comparison — the two things a CPU
actually knows how to do. (~2 min)
-->

---
hideInToc: true
---

# A Bit of **Foresight**

<div class="card card-warning card-glass pad-compact mt-sm glow">

🧭 **Why care?** Once data and code are just **bytes in files**, a whole analysis becomes **raw file → box → plots** — and the box can be re-run by a *script* instead of by hand.

</div>

<div class="card card-info card-glass pad-tight mt-md">

- Applicable to data analysis routines of **arbitrary complexity**
- You don't have to "see" your data (Excel, Origin, ...)
- You don't have to "see" your code (Python, R, C++, ...)
- You look at the **results** (or interim results: tests, plots, ...)
- Everything is managed from the top (workflow, pipeline, config files)

</div>

<!--
Speaker: this is the course in one slide — reproducibility and automation both
follow from treating data and code as files a script can act on. Don't dwell;
the rest of the lecture builds the "bytes in files" half of the claim. (~1 min)
-->

---
layout: section
hideInToc: true
---

# Data **Representation**

Before we can write algorithms, we need to know what their inputs and outputs are made of — how data is actually stored inside the computer, from individual bits up to whole files.

<!--
Speaker: we build up from the smallest unit — bit → byte → number bases →
hexadecimal. Keep the pace brisk; the tally-marks and light-bulb slides land the
core idea that everything is just on/off switches. (~1 min)
-->

---
layout: fact
hideInToc: true
---

# Unary

## <v-click> **Base-1** </v-click>

<div class="note-text mt-md">

Already fluent in binary? Skim ahead to the hex slide — the payoff is how files decode.

</div>

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

Humans have always counted with tally marks — one mark per unit. It's the simplest possible number system, and a useful contrast before we meet the base computers actually use: binary.

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
The first transistor (Bell Labs, 1947) — the physical switch behind every bit
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

# n Bits, 2ⁿ **Values**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 🔢 **Each bit doubles the count**

| Bits | Values | Enough for |
| --- | --- | --- |
| 1 | 2 | yes or no |
| 3 | 8 | the days of the week |
| 7 | 128 | the ASCII characters |
| 8 | 256 | one byte |
| 16 | 65 536 | a 16-bit reading, 0 to 65 535 |
| 32 | about 4.3 × 10⁹ | |

</div>

<div class="card card-secondary card-glass pad-compact">

## ↩️ **The other way round**

To tell *k* things apart, *n* bits are needed with 2ⁿ ≥ *k*.

- 26 letters: 2⁴ = 16 is too few, 2⁵ = 32 is enough. Five bits
- 10 digits: four bits, and six patterns stay unused
- 1000 detector channels: ten bits, because 2¹⁰ = 1024

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A bit is the answer to one yes-or-no question. *n* bits are *n* such answers in a row, and every added answer splits each case in two. That is where 2ⁿ comes from.

</div>

<!--
Speaker: let the room work out the 26 letters before showing the answer. The
16-bit row is the detector reading: a counter that passes 65 535 starts again
at 0. (~2 min)
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

# Hex Example: 0x2A

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

One hex digit stands for exactly four bits, so a byte is always two hex digits. Check: 2 × 16 + 5 = 37.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Both are algorithms in the sense of the first slides: a fixed list of steps that ends, and gives the same result whoever carries it out.

</div>

<!--
Speaker: do 37 on the board, then give the room 100 to convert on paper:
1100100, 0x64. (~3 min)
-->

---
hideInToc: true
---

# Why Hex in Computing?

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

🔢 **Compact** — 1 hex digit = 4 binary digits

</div>

<div class="card card-secondary card-glass pad-compact">

💾 **Memory addresses** — 0x1A2B3C4D

</div>

<div class="card card-accent card-glass pad-compact">

🎨 **Colors** — #FF5733 (red-green-blue)

</div>

<div class="card card-info card-glass pad-compact">

🐛 **Debugging** — Easier to read than long binary strings

</div>

</div>

---
layout: section
hideInToc: true
---

# How Computers **Compute**

Once numbers are bits, arithmetic and logic become operations on 0s and 1s — and a processor is a machine that grinds through them, billions of times a second.

<!--
Speaker: the payoff slide is fetch–decode–execute — an algorithm becomes numbers
that AND/OR/NOT circuits grind through. Tie the logic gates back to "software is
just data the CPU obeys." (~1 min)
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

The only rule: <strong>1 + 1 = 10</strong> — write 0, carry 1 — exactly like 7 + 5 in decimal: write 2, carry 1.

</div>

<!--
Speaker: work it column by column from the right: 1+0 = 1; 1+1 = 0 carry 1;
0+1+carry = 0 carry 1; 1+0+carry = 0 carry 1; the last carry lands as the
fifth bit. Same algorithm as primary-school addition, two symbols instead of
ten. (~2 min)
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

---
hideInToc: true
---

# Bitwise Operations Example

<div class="note-text">

*Written in Python. Reading it needs no Python: the comment on each line gives the result.*

</div>

<div class="card card-primary card-glass pad-compact mt-sm">

**Used in:** data compression, cryptography, bit manipulation

</div>

<div class="mt-md">

```py {monaco-run} {autorun:false}
a = 0b1100  # 12 in decimal
b = 0b1010  # 10 in decimal

print(f"a & b = {a & b:04b}")  # 1000 (8)
print(f"a | b = {a | b:04b}")  # 1110 (14)
print(f"~a = {~a & 0b1111:04b}")  # 0011 (3)
```

</div>

---
hideInToc: true
---

# How the CPU Runs an Algorithm

<div class="card card-info card-glass pad-compact mt-sm glow">

🔄 A processor does one astonishingly simple thing, billions of times per second — the **fetch–decode–execute** cycle.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

📥 **Fetch** — read the next instruction (itself just a binary number) from memory

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

🔎 **Decode** — work out what it says: "add these", "compare those", "jump there"

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

⚡ **Execute** — run it through circuits built from exactly the logic gates you just saw

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md reveal-up">

💡 That's the whole trick: an **algorithm** becomes a list of instructions, instructions become **numbers**, and AND/OR/NOT circuits grind through them. Software is just data the CPU knows how to obey — the "find the maximum" recipe you traced by hand is a compare and a jump, repeated.

</div>

---
hideInToc: true
---

# The Memory Hierarchy

<div class="card card-info card-glass pad-compact mt-sm">

⏱️ Not all storage is equal — each step away from the CPU is **bigger but dramatically slower**.

</div>

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

🏎️ **Registers** — inside the CPU · a few hundred bytes · < 1 ns

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

⚡ **Cache** — on the CPU chip · megabytes · a few ns

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

🧠 **RAM** — main memory · gigabytes · ~100 ns · gone at power-off

</div>

<div class="card card-warning card-glass pad-compact reveal-left">

💽 **Disk (SSD/HDD)** — terabytes · ~0.1–10 ms · **a million times slower than registers**

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md reveal-up">

💡 This is why "my dataset doesn't fit in memory" changes everything — and why the *format* and *size* of your files (this lecture!) directly set how fast your analysis can possibly run.

</div>

---
layout: section
hideInToc: true
---

# Numbers in **Computers**

A byte holds 256 values — more bits buy more range and precision, and when the bits run out, values wrap or round.

<!--
Speaker: the two big gotchas live here — fixed-width integer overflow (values
wrap silently) and floating-point rounding (0.1 + 0.2 ≠ 0.3). Both bite real
analyses; the slide after the recipe reads a fresh pattern by its weights. (~1 min)
-->

---
hideInToc: true
---

# Integers: Fixed Width

<div class="card card-info card-glass pad-compact mt-sm">

🔢 Hardware stores whole numbers in a **fixed number of bits** — the width decides the range (smaller = less memory per value, larger = more headroom), and stepping past it **wraps around** (overflow).

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📏 **Common widths**

| bits | unsigned range |
|------|----------------|
| 8    | 0 … 255 |
| 16   | 0 … 65,535 |
| 32   | 0 … ~4.3 × 10⁹ |
| 64   | 0 … ~1.8 × 10¹⁹ |

The famous **Y2K38 problem**: 32-bit Unix time runs out on 19 Jan 2038.

</div>

<div class="card card-warning card-glass pad-tight">

## 💥 **Overflow**

At 8 bits, `255 + 1 = 0` — silently:

```py {monaco-run} {autorun:false}
import numpy as np
a = np.array([127], dtype=np.int8)  # int8 max
print(a + 1)  # [-128]: wraps, no warning
```

*Python's own `int` grows as needed — but NumPy arrays and files use fixed widths, so pick a type wide enough for your data range.*

</div>

</div>

<style>
table { font-size: 0.85em; }
td, th { padding-top: 0.25em; padding-bottom: 0.25em; }
</style>

<!--
Speaker: the NumPy lines are not explained here — the point
is only that a fixed-width value wraps with no error. Ask: what happens to a
16-bit event counter on the 65,536th event? (~2 min)
-->

---
hideInToc: true
---

# Negative Numbers: Two's Complement

<div class="card card-info card-glass pad-compact mt-sm">

➖ There is no minus sign in hardware — negative integers are encoded by convention. The winner: **two's complement**.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🧮 **The recipe** *(4-bit example)*

To get −5 from 5:

1. Start: `0101` (= 5)
2. Flip every bit: `1010`
3. Add one: `1011` (= −5)

Top bit set ⇒ negative.

</div>

<div class="card card-accent card-glass pad-tight">

## ✨ **Why it's clever**

Addition just works — no special subtraction circuit:

```text
  0101   (+5)
+ 1011   (−5)
------
 10000 → 0000 = 0 ✓
```

*(the carry falls off the fixed width)*

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

📏 Signed ranges are asymmetric: 8 bits → **−128 … +127** — one more negative than positive.

</div>

---
hideInToc: true
---

# Two's Complement: **Reading a Pattern**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⚖️ **The top bit has a negative weight**

```text
weights   −8   4   2   1
pattern    1   1   0   1
value     −8 + 4 + 0 + 1  =  −3
```

The recipe agrees: flip `1101` to `0010`, add one to get `0011`, which is 3. The pattern is −3.

</div>

<div class="card card-secondary card-glass pad-compact table-compact">

## 📏 **Ranges**

| Bits | Smallest | Largest |
| --- | --- | --- |
| 4 | −8 | 7 |
| 8 | −128 | 127 |
| 16 | −32 768 | 32 767 |
| *n* | −2ⁿ⁻¹ | 2ⁿ⁻¹ − 1 |

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The eight bits `11111111` are 255 as an unsigned integer and −1 as a signed one. The bits do not say which. The type of the column says it, and the type has to be written down with the data.

</div>

<!--
Speaker: the weights are the reason the recipe works, and they make reading a
pattern a sum. The warning card is the definition of data again: the same
symbols under two rules. (~2 min)
-->

---
hideInToc: true
---

# Floating-Point: Scientific **Notation**

<div class="card card-info card-glass pad-compact mt-sm">

📐 A **float** is a number written in *scientific notation* — a sign, some significant digits, and a power that sets the scale:

</div>

<div class="text-center text-4xl my-6">

$N = s \times m \times 10^{e} \qquad\qquad {-6.022} \times 10^{23}$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-warning card-glass pad-compact">

**s** = sign → **negative** (−1)

</div>

<div class="card card-primary card-glass pad-compact">

**m** = mantissa → **6.022** (significant digits, 1 ≤ m < 10)

</div>

<div class="card card-secondary card-glass pad-compact">

**e** = exponent → **23** (integer power of 10)

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 IEEE-754 is the same idea in **base 2**, squeezed into a fixed number of bits — so the mantissa has finite digits, and some decimals get **rounded**.

</div>

---
hideInToc: true
---

# Float32 Anatomy: **Sign, Exponent, Mantissa**

<div class="text-center text-3xl my-4">

$(-1)^{s} \times 1.m \times 2^{e - b}$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

**s** — sign bit · **1 bit**

0 = positive, 1 = negative

</div>

<div class="card card-secondary card-glass pad-compact">

**e** — exponent · **8 bits**

power of 2, stored as **e + b** with bias **b = 127** — so negative powers need no sign of their own

</div>

<div class="card card-accent card-glass pad-compact">

**m** — mantissa · **23 bits**

fraction bits of the significand **1.m** (1 ≤ 1.m < 2); the leading 1 is implied, so it costs nothing

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧩 `[ s: 1 ][ e: 8 ][ m: 23 ]` = 32 bits ≈ **7 significant digits**. **float64** (Python's default) spends 1 + 11 + 52 bits ≈ **15 significant digits**.

</div>

---
hideInToc: true
---

# Worked Example: 5.75 as float32

<div class="text-center text-3xl my-4">

  $(-1)^{0} \times 1.m \times 2^{e - b}$

</div>

<div class="card card-primary card-glass pad-tight mt-sm">

- 5.75 → 101.11₂
- In scientific notation: $1.0111_2 \times 2^2$
- **s** = 0 (positive)
- **m** = 01110000000000000000000
- **e** = 2, stored as e + bias = 2 + 127 = 129 = 10000001₂
- **b** = 127 (float32 exponent bias)

</div>

<div class="text-center text-3xl mt-md">

`0 10000001 01110000000000000000000`

</div>

---
hideInToc: true
---

# Floating-Point Gotchas

<div class="card card-warning card-glass pad-tight mt-md">

## ⚠️ **Not all decimals are exact in binary**

```py {monaco-run} {autorun:false}
print(0.1 + 0.2)            # 0.30000000000000004 (!)
print(0.1 + 0.2 == 0.3)     # False

# Use tolerance for comparisons
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

**Why?** 0.1 is a repeating fraction in binary (like 1/3 in decimal). Finite bits mean rounding.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

🔢 **float32** — ~7 significant digits

</div>

<div class="card card-secondary card-glass pad-compact">

🔢 **float64** — ~15 significant digits (Python default)

</div>

</div>

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
- 0.5, 0.25 and 0.375 are exact: they are sums of powers of 2
- 0.1, 0.2 and 0.3 are not, and their rounding errors do not cancel. `0.1 + 0.2` gives 0.30000000000000004

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Decimal has the same problem with 1/3 = 0.333…: no finite number of digits writes it. Which fractions are exact depends on the base, not on the computer.

</div>

---
hideInToc: true
---

# The Steps Between **Floats**

<div class="card card-info card-glass pad-compact mt-sm">

A float32 has 24 binary digits, wherever the point stands. So the step from one float to the next grows with the size of the number.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact table-compact">

## 📏 **float32**

| Near | Step to the next float |
| --- | --- |
| 1 | 0.000 000 12 |
| 1880.649 | 0.000 12 |
| 16 777 216 | 2 |

</div>

<div class="card card-secondary card-glass pad-compact">

## 🎯 **What this means for data**

- `1880.649`, the first M in the LHCb file `D0_KPi.csv`, is stored as 1880.6490478515625, the nearest float32
- Digits after the seventh are not information. They come from the rounding
- A float32 cannot count by one from 16&nbsp;777&nbsp;216 on: 16&nbsp;777&nbsp;216&nbsp;+&nbsp;1 gives 16&nbsp;777&nbsp;216

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ The relative precision is constant: about 1 part in 10⁷ for float32 and 1 part in 10¹⁶ for float64. The absolute precision is not. Adding many small numbers to one large number loses the small ones.

</div>

<!--
Speaker: 1880.649 is the invariant mass, in MeV/c², in the first data row of
D0_KPi.csv: 1880.649,3000.9534,0.00041271152,1299.1675. Its float32 neighbours
are 0.000 12 apart (2 to the power -13), so the stored value differs from the
written one in the ninth significant digit.
16 777 216 is 2 to the power 24. Above it the 24 digits no longer
reach down to the ones place. The practical rule: sum in float64, store in
float32 if 7 digits are enough. (~2 min)
-->

---
hideInToc: true
---

# Try It **Here**

<div class="card card-success card-glass pad-tight mt-md">

## 🧪 **Live Demo**

Two lines from Floating-Point Gotchas, and a third that prints 20 decimals of the number really stored for `0.1`. Predict each line, then press ▶:

```py {monaco-run} {autorun:false}
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
```

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 These are not bugs. Every computer stores decimals this way, and it matters whenever two measured numbers are compared.

</div>

---
hideInToc: true
---

# Data Types in Practice

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-scale">

🔢 **Integers** (`int`) — `42`, `-7`, `0` — fixed-width binary, overflow wraps silently (arbitrary precision in Python)

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale">

📐 **Floats** (`float`) — `3.14`, `6.022e23` — IEEE-754, watch for rounding!

</div>

<div class="card card-accent card-glass pad-compact reveal-scale">

🔤 **Strings** (`str`) — `"Hello"`, `"α"` — Unicode characters, encoded as UTF-8 (next section)

</div>

<div class="card card-success card-glass pad-compact reveal-scale">

✅ **Booleans** (`bool`) — `True` / `False` — conceptually a single bit, the basis of all decisions

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 Every piece of data in your programs is one of these types. Choosing the right one matters for correctness, memory, and performance.

</div>

---
layout: section
hideInToc: true
---

# Text & **Encodings**

Numbers were the easy part — text needs a convention that maps characters to numbers, and then numbers to bytes: ASCII, Unicode, UTF-8.

<!--
Speaker: ASCII is the 7-bit table everyone agrees on; Unicode extends it to
every script; UTF-8 is the byte encoding that keeps ASCII files unchanged.
The pay-off is mojibake and the Excel trap — real ways data gets mangled. (~1 min)
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

*(excerpt — first 8 rows of each block)*

<div class="card card-info card-glass pad-compact mt-sm">

🔢 In Lecture 2, Sort Lines put `100` before `20` because `1` comes before `2`. One level down: `1` is stored as 49 = 0x31 and `2` as 50 = 0x32. The sort compares these numbers, and 0x31 < 0x32.

</div>

<!--
Speaker: this takes Lecture 2's answer one level down. There, 100 sorted
before 20 because the character 1 comes before 2; here "comes before" is a
comparison of two numbers. Point at 49 and 50 in the table. A text sort compares the first byte of
each line and looks further only on a tie; 30 (0x33) comes after both. (~1 min)
-->

---
hideInToc: true
---

# Unicode and UTF-8

<div class="card card-info card-glass pad-compact mt-sm">

🌍 ASCII covers 128 characters — the rest of the world's alphabets, symbols and emoji need **Unicode**, and Unicode needs a byte **encoding**.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🌐 **Unicode**

Universally encodes characters as code points

- U+0041 = 'A'
- U+03B1 = 'α'
- U+1F600 = '😀'

</div>

<div class="card card-secondary card-glass pad-tight">

## 📦 **UTF-8**

Stores code points in 1–4 bytes, backward-compatible with ASCII

**Pitfalls in data:** smart quotes, emojis, mixed encodings, BOM (a hidden byte-order marker at the start of a file that can break parsing)

</div>

</div>

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

<div class="card card-info card-glass pad-compact mt-md">

The first bits of a byte say what it is: `0` is a whole ASCII character, `110`, `1110` or `11110` start a longer one, `10` continues it. A program can begin reading anywhere in a file and find the next character. Plain ASCII text is valid UTF-8 without any change.

</div>

---
hideInToc: true
---

# Python for Encoding Conversions

<div class="note-text">

*Written in Python. Reading it needs no Python: the comment on each line gives the result.*

</div>

<div class="mt-sm">

```py {monaco-run} {autorun:false}
# Python: bytes vs str and UTF-8
s = "Å and 😊"            # str = Unicode
b = s.encode("utf-8")     # bytes
print(len(s), len(b))     # 7 11 — 7 characters, 11 bytes: Å = 2, 😊 = 4
print(b)                  # b'\xc3\x85 and \xf0\x9f\x98\x8a'
print(b.decode("utf-8"))  # back to str
```

</div>

---
hideInToc: true
---

# Mojibake: When Encodings Collide

<div class="card card-info card-glass pad-compact mt-sm">

👾 **Mojibake** — garbled text from reading bytes with the **wrong encoding**. The bytes are fine; the interpretation isn't.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔍 **How it happens**

`ą` in UTF-8 is **two bytes**: `C4 85`

Read them by a one-byte table such as Windows-1252:

`C4` → `Ä`, `85` → `…`, so `ą` shows as `Ä…`

</div>

<div class="card card-warning card-glass pad-tight">

## 📄 **In real CSV files**

`Žagarė` → `Å½agarÄ—`

`Å` and `Ä` scattered through Lithuanian text are the usual symptom: UTF-8 bytes read by a one-byte table.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 The bytes are fine, so nothing is retyped. The file is read again with the right encoding: **Reopen with Encoding** in VS Code, `open(f, encoding="utf-8")` in Python.

</div>

---
hideInToc: true
---

# Encoding & Line Endings in **VS Code**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔤 **`UTF-8` in the Status Bar**

- The Status Bar names the encoding VS Code used to read the file
- Click it. **Reopen with Encoding** reads the same bytes by another table
- **Save with Encoding** writes different bytes. Use it only on purpose

</div>

<div class="card card-secondary card-glass pad-compact">

## ↵ **`LF` or `CRLF`**

- A line break is a byte as well: `0A`, called LF, on macOS and Linux
- Windows writes two bytes: `0D 0A`, called CRLF
- The same ten lines saved on Windows are ten bytes longer

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

📁 `ą` is two bytes in UTF-8, `C4 85`, and one byte in the older Baltic table Windows-1257, `E0`. The letters `a` to `z` are the same single byte in every table. That is why names of files and folders keep to them.

</div>

<!--
Speaker: open a file with Lithuanian letters, click UTF-8 in the Status Bar and
reopen it as Baltic (Windows 1257): the letters turn to Ä and Å. Reopen as UTF-8
and they are back. Nothing in the file changed. (~2 min)
-->

---
hideInToc: true
---

# The Excel Trap (and the BOM)

<div class="grid-2 mt-md gap-md">

<div class="card card-warning card-glass pad-tight">

## 🧨 **"Just open it in Excel"**

Opening and re-saving a CSV can silently:

- re-encode text in your **locale's** encoding, not UTF-8
- turn identifiers into **dates** — gene `SEPT2` → `2-Sep`, an error found in ~20% of genomics papers with gene lists
- strip **leading zeros** from IDs (`007` → `7`)

</div>

<div class="card card-info card-glass pad-tight">

## 🫥 **The BOM gotcha**

Some tools prepend a **byte-order mark** — `EF BB BF` — to UTF-8 files.

Symptom: a ghost `ï»¿` glued to your first column name.

Python's `encoding="utf-8-sig"` reads (and strips) it.

</div>

</div>

<div class="card card-success card-glass pad-compact mt-md">

💡 Treat data files as **bytes with a declared encoding** — inspect first, and edit with tools that don't "help".

</div>

---
layout: section
hideInToc: true
---

# Files & **Formats**

A character takes one to four bytes, a 32-bit number takes four — in what order? A file is just a named sequence of such bytes: its size, its byte order, and the first bytes that say how to read the rest.

<!--
Speaker: sizes, byte order, magic numbers, a real hexdump. Land "a file is a
named sequence of bytes" here. (~1 min)
-->

---
hideInToc: true
---

# File Sizes: From Bits to Terabytes

<div class="card card-info card-glass pad-tight mt-sm">

| **Unit** | **Size** | **Everyday Reference** |
|----------|----------|------------------------|
| 1 byte   | 8 bits   | A single ASCII character |
| 1 kB     | ~1,000 bytes | A short email      |
| 1 MB     | ~1,000 kB | A photograph          |
| 1 GB     | ~1,000 MB | ~250 songs (MP3)      |
| 1 TB     | ~1,000 GB | ~500 hours of video   |

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Two conventions coexist: **decimal** kB/MB/GB (powers of 1,000 — SI, drive makers, this table) and **binary** KiB/MiB/GiB (powers of 1,024 — what Windows and many CLI tools report). A "1 TB" drive holds 10¹² bytes ≈ 931 GiB, which Windows then displays as "931 GB" — same bytes, different unit.

</div>

---
hideInToc: true
---

# Endianness

<div class="card card-info card-glass pad-compact mt-sm">

## 🔄 **What is Endianness?**

The **order** in which bytes of a multibyte value are stored in memory.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📦 **Big-Endian**

Most significant byte stored **first** (lowest address)

`0x12345678` → `12 34 56 78`

Used by: **network protocols** (TCP/IP)

</div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **Little-Endian**

Least significant byte stored **first** (lowest address)

`0x12345678` → `78 56 34 12`

Used by: **x86/x64** and (typically) **ARM** — most PCs & phones

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-sm">

⚠️ Mismatched endianness → garbage values. NumPy, a Python library for arrays of numbers, lets you say which you mean: `dtype='>f4'` (big) or `dtype='<f4'` (little).

</div>

---
hideInToc: true
---

# File Formats (Extensions)

<div class="card card-info card-glass pad-tight mt-sm">

**A file is a named sequence of bytes.** The extension is a *hint* for humans and the OS; the real signature is the first bytes (the *magic number*): PNG `89 50 4E 47`, PDF `%PDF`, ZIP/docx/xlsx `PK`. A hex viewer shows them.

| **Text/Data** | **Documents** | **Media/Archives/Exec** |
|--------------|---------------|----------------|
| .txt        | .pdf          | .mp3           |
| .csv        | .docx         | .mp4           |
| .json       | .pptx         | .zip           |
| .xml        | .xlsx         | .rar           |
| .yaml       | .rtf          | .exe           |
| .md         | .odt          | .apk           |

</div>

---
hideInToc: true
---

# Reading a **Hexdump**

<div class="card card-info card-glass pad-compact mt-sm">

🔬 A hex viewer shows the raw bytes of *any* file: the offset, 16 bytes as hex pairs, and the same bytes as ASCII (a `.` for anything unprintable). In VS Code it is the **Hex Editor** extension, in a terminal `hexdump -C` (macOS, Linux) or `Format-Hex` (Windows).

</div>

<div class="card card-primary card-glass pad-compact mt-md">

```text
pendulum.csv, 97 bytes
00000000  6c 65 6e 67 74 68 5f 63  6d 2c 74 31 30 5f 73 0a  |length_cm,t10_s.|
00000010  32 30 2c 39 2e 30 32 0a  33 30 2c 31 31 2e 30 35  |20,9.02.30,11.05|
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-compact">

## 👀 **What you can read off**

- `6c` = `l`, `65` = `e` — one byte per character: pure ASCII, so UTF-8-safe
- `2c` is the comma; `0a` ends each line (LF), `0d 0a` would mean Windows line endings
- no `EF BB BF` at offset 0 → no BOM
- offsets count bytes: the last one is the file size

</div>

<div class="card card-accent card-glass pad-compact">

## 🎯 **Why bother**

This is the one view where *nothing* is interpreted for you. Encoding, line endings, size and format of a raw file are checked here, at the byte level, before a single number in it is trusted.

</div>

</div>

<!--
Speaker: this is the two-column table from the previous lecture's editing
example. Walk the first line byte by byte with the ASCII table still in their
heads — 6c is l, 65 is e, 2c is the comma. Then point at 0a: that is the
newline, invisible in any editor but plainly a byte here. (~2 min)
-->

---
hideInToc: true
---

# One Number, **Two Files**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 📄 **As text**

```text
1880.649
31 38 38 30 2E 36 34 39
```

Eight characters, eight bytes. Any program and any person can read them. Another number may need more bytes, or fewer.

</div>

<div class="card card-secondary card-glass pad-compact">

## 📦 **As a float32**

```text
1880.649
C5 14 EB 44
```

Always four bytes. They mean nothing until the reader knows three things: the type, the byte order, and where the number starts.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

A row of the example file has four numbers. As text it takes about 43 bytes, as four float32 values 16. For 91 583 rows that is 3.9 MB against 1.5 MB. Text costs space and is read by everything. Binary is compact and needs its description.

</div>

<!--
Speaker: read the text bytes with the ASCII table: 31 is the character 1, 2E is
the point. The four float bytes are the sign, exponent and mantissa of the
float32 slides, lowest byte first. (~2 min)
-->

---
hideInToc: true
---

# Image Quality vs Bit Depth

<div class="card card-info card-glass pad-tight mt-sm">

Below are five versions of the same image, saved with **different bit depths**. Notice how fewer bits per pixel mean fewer colours — the **raw** size scales with bit depth, while the on-disk size depends on compression (next section). Fewer bits reduce **image quality** and **file size**.

</div>

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

---
layout: section
hideInToc: true
---

# Compression & **Integrity**

Throwing away bits per pixel is the crude way to shrink a file. The clever way reorganizes the same bits to take less space — and checks that none of them were corrupted along the way.

<!--
Speaker: short section. Lossless vs lossy, then checksums and hashes for
integrity. Land the point that a SHA-256 hash is how you prove a file arrived
intact — directly relevant to trusting a downloaded dataset. (~1 min)
-->

---
hideInToc: true
---

# Compression Primer

<div class="grid-2 mt-md gap-md">

<div class="card card-success card-glass pad-tight">

## 🔒 **Lossless**

Remove **redundancy**, recover the data **exactly** — RLE, Huffman, DEFLATE (inside PNG, ZIP, gzip)

🔤 **RLE example:** `AAABBBCC` → `3A3B2C` (8 chars → 6 chars)

</div>

<div class="card card-warning card-glass pad-tight">

## 📉 **Lossy**

JPEG, MP3 — small size, information loss acceptable for media

JPEG throws away detail your eye can't see — fine for photos, **never for data**

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

💡 Plain-text formats like CSV and JSON aren't compressed at all — every byte stored as-is. That's exactly why they zip so well: **gzip halves a CSV of measured numbers**, and shrinks one with many repeated values to a tenth.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## ⚙️ **How DEFLATE finds the redundancy**

A CSV repeats separators, column values and digit patterns thousands of times. DEFLATE replaces each repeat with a short back-reference ("copy 12 bytes from 340 bytes ago") and gives frequent bytes shorter codes (Huffman).

</div>

<div class="card card-accent card-glass pad-compact">

## 🔁 **In your workflow**

`gunzip` returns the **byte-identical** file — same size, same hash. Many tools read `.csv.gz` directly (`zcat`, pandas), so you can keep raw data compressed and never unpack it by hand.

</div>

</div>

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

The sender stores 38 next to the file. The receiver adds up the bytes again and compares.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔍 **What it catches**

- `abd` gives 39: one changed byte is caught
- `acb` gives 38: two bytes that changed places are not
- One byte too high by 1 and another too low by 1 are not

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

Every check of this kind is a short number computed from all the bytes. A better rule misses fewer changes. A parity bit catches one flipped bit. A CRC catches bursts of errors. A cryptographic hash such as SHA-256 is built so that nobody can construct a change that slips through.

</div>

---
hideInToc: true
---

# Error Detection & Hashing

<div class="grid-2 mt-sm gap-md">

<div class="card card-primary card-glass pad-compact">

## 🔍 **Error Detection**

Parity, checksums, CRC detect transfer/storage errors — e.g. a **parity bit** keeps the count of 1s even, so any single flipped bit is caught

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔐 **Hashing**

A cryptographic hash (**SHA-256**) boils any file down to a 256-bit fingerprint — same bytes in, same fingerprint out, on every machine

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🧾 **In practice**

```text
pendulum.csv, 97 bytes        SHA-256, 64 hex digits = 256 bits
be05af034937ef615c93b2fb5d8369c899def80d0472a6187c5dbd3afff0870b
```

- Flip **one bit** anywhere in the file → a **completely different** hash (it never says "how close")
- **Publish the hash next to the file**: is the copy on your laptop these same 97 bytes? Yes, if all 64 hex digits match.

</div>

<!--
Speaker: the lecture's most practical minute. Every dataset you publish should
ship with its hash; every dataset you download should be checked against one.
"Different in every digit" is the expected symptom of *any* change. The hash
shown is that of pendulum.csv, the 97-byte table of the hexdump slide; it is
the same on every system. (~2 min)
-->

---
hideInToc: true
---

# Key <span class="gradient-text">Takeaways</span>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact reveal-up">

💡 **Bits** — everything in a computer is 0s and 1s; a bit is the smallest unit of information

</div>

<div class="card card-secondary card-glass pad-compact reveal-up">

🔢 **Numbers** — place value (binary, hex) plus finite precision (fixed-width ints, IEEE-754 floats)

</div>

<div class="card card-accent card-glass pad-compact reveal-up">

🔤 **Text** — encodings (ASCII, Unicode/UTF-8) map characters to bytes

</div>

<div class="card card-info card-glass pad-compact reveal-up">

📁 **Files** — formats, byte order, and bit depth tell the computer what a sequence of bits means

</div>

<div class="card card-success card-glass pad-compact reveal-up">

🗜️ **Compression & integrity** — remove redundancy to shrink data; checksums and hashes catch corruption

</div>

</div>

<div class="grid-2 mt-md gap-md items-center">

<div class="card card-warning card-glass pad-compact reveal-up">

🧭 Back to the "box": before writing algorithms, you need to know what their **inputs** and **outputs** are made of — and now you do.

</div>

<div class="text-center">

```mermaid {scale: 1}
graph LR
    A[input] --> B["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br/>&nbsp;"] --> C[output]

    classDef invisible fill:none,stroke:none,font-size:24px;
    classDef transparentBox fill:none,stroke:white,stroke-width:3px,font-size:24px;

    class A invisible;
    class B transparentBox;
    class C invisible;

    linkStyle 0 stroke-width:3px;
    linkStyle 1 stroke-width:3px;
```

</div>

</div>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Convert between **binary**, **decimal**, and **hexadecimal**

</div>

<div class="card card-success card-glass pad-compact">

✅ Reason about **bits**, **bytes**, and real file sizes

</div>

<div class="card card-success card-glass pad-compact">

✅ Explain how text and numbers are encoded as **bytes**

</div>

<div class="card card-success card-glass pad-compact">

✅ Spot **overflow** and **rounding** limits in ints and floats

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Before trusting a number in a file**

Look at the file as bytes: its character encoding, its line endings, its exact size and its format.

</div>

<!--
Speaker: the "you can now" beat — have them nod along to each. The last card is
the habit to take away: open a data file at the byte level and
verify its encoding, size, and format before trusting any number. (~1 min)
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
  question="A detector writes each reading as a 2-byte (16-bit) unsigned integer. How many distinct values can one reading take?"
  :options="[
    '256',
    '65,536',
    '32,768',
    '16'
  ]"
  :correct="1"
  explanation="16 bits give 2^16 = 65,536 distinct values (0 … 65,535). Each extra bit doubles the count — 2 bytes is 256 × 256. If your sensor can exceed that, you need a wider type or values silently wrap."
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
  explanation="By weights: −8 + 0 + 2 + 0 = −6. By the recipe: flip 1010 to 0101, add one to get 0110, which is 6, so the pattern is −6. Read as an unsigned integer the same four bits would be 10."
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
  explanation="Everything on disk — text, images, programs — is ultimately a named blob of bytes the OS keeps track of. A file extension is only a convention for how to interpret those bytes; a hexdump is that blob with nothing interpreted."
/>

---
hideInToc: true
---

<MCQ
  question="You download data.csv; its published SHA-256 is 3b1f…e9, but the SHA-256 of your copy differs from it in every digit. What can you conclude?"
  :options="[
    'The file is almost identical — only a few bytes must differ',
    'Your copy differs from the published file somewhere — even a single flipped bit would do this',
    'The hash tool is broken: a small change should change only a few digits',
    'Nothing — SHA-256 gives a different result every time you run it'
  ]"
  :correct="1"
  explanation="A cryptographic hash is deliberately avalanche-like: any change, however small, scrambles the whole digest. So the hash tells you that something differs, never how much. The same bytes always give the same 64 hex digits — on every machine — which is what makes it a fingerprint."
/>
