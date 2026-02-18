---
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Crash Course on Computer Science"
layout: cover
---

# Dr. Mindaugas Šarpis

# Data Analysis and Artificial Intelligence

## Crash Course on Computer Science

---
layout: quote
hideInToc: true
---

# The main goal of this lecture is to promote **algorithmic thinking** and to provide a basic understanding of **computer science** concepts

---
layout: center
hideInToc: true
---

```mermaid {scale: 2}
graph LR
    A[input] --> B[ ] --> C[output]

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

# A bit of foresight

<div class="card card-info pad-tight mt-sm">

- Applicable to data analysis routines of **arbitrary complexity**
- You don't have to "see" your data (Excel, Origin, ...)
- You don't have to "see" your code (Python, R, C++, ...)
- You look at the **results** (or interim results: tests, plots, ...)
- Everything is managed from the top (workflow, pipeline, config files)

</div>

<div class="mt-md" style="text-align: center;">

```mermaid {scale: 2}
graph LR
    A[input] --> B[ ] --> C[output]

    classDef invisible fill:none,stroke:none,font-size:24px;
    classDef transparentBox fill:none,stroke:white,stroke-width:3px,font-size:24px;
    classDef textStyle font-size:24px;

    class A invisible;
    class B transparentBox;
    class C invisible;

    linkStyle 0 stroke-width:3px;
    linkStyle 1 stroke-width:3px;
```

</div>

---
hideInToc: true
---

<div class="card card-accent pad-tight mt-sm">

## 🧭 **What's Next**

Before building pipelines, we need to understand how computers **represent data** — numbers, text, images — at the most fundamental level.

</div>

---
layout: section
hideInToc: true
---

# Data **Representation**

---
layout: fact
hideInToc: true
---

# Unary

## <v-click> **Base-1** </v-click>

---
layout: center
hideInToc: true
class: text-size-78
---

<div class="center-content">
  <span v-click="1">|</span>
  <span v-click="2">|</span>
  <span v-click="3">|</span>
  <span v-click="4">|</span>
  <span v-click="5">|</span>
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

<img src="/light_bulb_off.png" class="w-auto h-86">

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

<img src="/light_bulb_on.png" class="w-auto h-86">

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

# Why Hex in Computing?

<div class="stack-tight mt-sm">

<div class="card card-primary pad-compact">

🔢 **Compact** — 1 hex digit = 4 binary digits

</div>

<div class="card card-secondary pad-compact">

💾 **Memory addresses** — 0x1A2B3C4D

</div>

<div class="card card-accent pad-compact">

🎨 **Colors** — #FF5733 (red-green-blue)

</div>

<div class="card card-info pad-compact">

🐛 **Debugging** — Easier to read than long binary strings

</div>

</div>

---
hideInToc: true
layout: fact
---

# Binary

## <v-click> **Base-2** </v-click>

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

## <span>2<sup>8</sup></span> = 256

---
layout: section
hideInToc: true
---

# Binary **Operations**

---
layout: center
hideInToc: true
class: text-size-10
---

$$
\phantom{111}  1011 \;\;(11 \text{ in decimal}) \\
+ \phantom{0.}  0110 \;\;(\phantom{0}6  \text{ in decimal}) \\
$$

$$
 \phantom{11} 10001 \;\;(17 \text{ in decimal})
$$

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

<div class="card card-primary pad-tight mt-sm">

**Used in:** data compression, cryptography, bit manipulation

```python
a = 0b1100  # 12 in decimal
b = 0b1010  # 10 in decimal

print(f"a & b = {a & b:04b}")  # 1000 (8)
print(f"a | b = {a | b:04b}")  # 1110 (14)
print(f"~a = {~a & 0b1111:04b}")  # 0011 (3)
```

</div>

---
layout: fact
hideInToc: true
---

# ASCII

## American Standard Code for Information Interchange

### 7 bit

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

---
hideInToc: true
layout: section
---

# Text Beyond **ASCII**

---
hideInToc: true
---

# Unicode and UTF-8

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🌐 **Unicode**

Universally encodes characters as code points

- U+0041 = 'A'
- U+03B1 = 'α'
- U+1F600 = '😀'

</div>

<div class="card card-secondary pad-tight">

## 📦 **UTF-8**

Stores code points in 1–4 bytes, backward-compatible with ASCII

**Pitfalls in data:** smart quotes, emojis, mixed encodings, BOM

</div>

</div>

---
hideInToc: true
---

# Can use Python for conversions

<div class="card card-accent pad-tight mt-sm">

```python
# Python: bytes vs str and UTF-8
s = "Å and 😊"         # str = Unicode
b = s.encode("utf-8")  # bytes
len(s), len(b)         # chars vs bytes

b.decode("utf-8")      # back to str
```

</div>

---
hideInToc: true
---

# Endianness

<div class="card card-info pad-tight mt-sm">

## 🔄 **What is Endianness?**

The **order** in which bytes of a multibyte value are stored in memory. When a number needs more than one byte (e.g., a 32-bit integer uses 4 bytes), the system must decide which byte goes first.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📦 **Big-Endian**

Most significant byte stored **first** (at lowest address)

`0x12345678` → `12 34 56 78`

Used by: **network protocols** (TCP/IP), some file formats

</div>

<div class="card card-secondary pad-tight">

## 📦 **Little-Endian**

Least significant byte stored **first** (at lowest address)

`0x12345678` → `78 56 34 12`

Used by: **x86/x64**, **ARM** (most laptops and phones)

</div>

</div>

</div>

---
hideInToc: true
---

# ⚠️ Why Endianness Matters

<div class="card card-warning pad-tight mt-sm">

## ⚠️ **Why It Matters for Data Analysis**

When sharing binary data files across systems, the byte order must match. Tools like NumPy let you specify endianness (e.g., `dtype='>f4'` for big-endian float32). Mismatched endianness produces garbage values.

</div>

---
hideInToc: true
---

# File formats (extensions)

<div class="card card-info pad-tight mt-sm">

**Computer needs to know what a sequence of bits is supposed to mean**

| **Text/Data** | **Documents** | **Media/Exec** |
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

# Image Quality vs Bit Depth

<div class="card card-info pad-tight mt-sm">

Below are five versions of the same image, saved with **different bit depths**. Notice how fewer bits reduce both **image quality** and **file size**.

</div>

<div class="grid grid-cols-5 gap-4 mt-md">
  <figure>
    <img src="/elf_24bit.png" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">24 bit</figcaption>
  </figure>
  <figure>
    <img src="/elf_4bit.png" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">4 bit</figcaption>
  </figure>
  <figure>
    <img src="/elf_3bit.png" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">3 bit</figcaption>
  </figure>
  <figure>
    <img src="/elf_2bit.png" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">2 bit</figcaption>
  </figure>
  <figure>
    <img src="/elf_1bit.png" class="rounded shadow-md h-48 object-contain" />
    <figcaption class="text-center mt-2">1 bit</figcaption>
  </figure>
</div>

---
layout: section
hideInToc: true
---

# Numbers in **Computers**

---
hideInToc: true
---

# Floating-Point Basics (IEEE-754)

<div class="card card-info pad-tight mt-sm">

**Float** = sign + exponent + mantissa (binary scientific notation)

**Finite precision** — rounding error; some decimals not exact in binary

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-compact">

**Sign bit** (1 bit) — positive / negative

</div>

<div class="card card-secondary pad-compact">

**Exponent** (8 bits in float32) — scale (power of 2)

</div>

<div class="card card-accent pad-compact">

**Mantissa** (23 bits in float32) — precision bits (significant figures)

</div>

</div>

---
hideInToc: true
---

# Scientific Notation in Decimal

<div class="text-center text-5xl my-8">

$N = s \times m \times 10^e$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-compact">

**s** = sign (+1 or -1)

</div>

<div class="card card-secondary pad-compact">

**m** = mantissa (significant digits, 1 $\leq$ m $<$ 10)

</div>

<div class="card card-accent pad-compact">

**e** = exponent (integer power of 10)

</div>

</div>

---
hideInToc: true
---

# Scientific Notation in Decimal

<div class="text-center text-5xl my-8">

$-6.022 \times 10^{23}$

</div>

<div class="grid-3 mt-md gap-md">

<div class="card card-warning pad-compact">

**Sign** = negative

</div>

<div class="card card-primary pad-compact">

**Mantissa** = 6.022

</div>

<div class="card card-secondary pad-compact">

**Exponent** = 23

</div>

</div>

---
hideInToc: true
---

## Binary scientific notation (float32)

<div class="text-center text-3xl my-8">

  $(-1)^{s} \times 1.m \times 2^{e - b}$

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-compact">

**s** = sign (+1 or -1)

</div>

<div class="card card-secondary pad-compact">

**m** = mantissa (significant digits, 1 $\leq$ m $<$ 2 in binary)

</div>

<div class="card card-accent pad-compact">

**e** = exponent (integer power of 2)

</div>

<div class="card card-info pad-compact">

**b** = exponent bias (127 for float32)

</div>

</div>

---
hideInToc: true
---

## Binary scientific notation (float32)

<div class="text-center text-3xl my-4">

  $(-1)^{0} \times 1.m \times 2^{e - b}$

</div>

<div class="card card-primary pad-tight mt-sm">

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

<div class="card card-warning pad-tight mt-md">

## ⚠️ **Not all decimals are exact in binary**

```python
print(0.1 + 0.2)            # 0.30000000000000004 (!)
print(0.1 + 0.2 == 0.3)     # False

# Use tolerance for comparisons
import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

**Why?** 0.1 is a repeating fraction in binary (like 1/3 in decimal). Finite bits mean rounding.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-compact">

🔢 **float32** — ~7 significant digits

</div>

<div class="card card-secondary pad-compact">

🔢 **float64** — ~15 significant digits (Python default)

</div>

</div>

---
hideInToc: true
---

# Integers, Overflow, and Arrays

<div class="grid-2 mt-md gap-md">

<div class="stack-tight">

<div class="card card-primary pad-compact">

🐍 Python ints are **arbitrary precision** — no overflow possible

</div>

<div class="card card-secondary pad-compact">

📊 NumPy/C arrays use **fixed-width** ints (int8, int16, int32, int64)

</div>

<div class="card card-warning pad-compact">

⚠️ **Overflow** wraps silently in fixed-width types

</div>

</div>

<div class="card card-accent pad-tight">

## 🔢 **Overflow Example**

```python
import numpy as np

a = np.int8(127)   # max value for 8-bit signed
print(a + 1)       # -128 (wraps around!)

b = np.int8(-128)  # min value
print(b - 1)       # 127 (wraps around!)
```

This matters when choosing dtypes in NumPy (L11) — always use a wide enough type for your data range.

</div>

</div>

---
layout: section
hideInToc: true
---

# Compression & **Integrity**

---
hideInToc: true
---

# Compression Primer

<div class="grid-2 mt-md gap-md">

<div class="card card-success pad-tight">

## 🔒 **Lossless**

CSV, JSON, Parquet, PNG — exact recovery

</div>

<div class="card card-warning pad-tight">

## 📉 **Lossy**

JPEG, MP3 — small size, info loss acceptable for media

</div>

</div>

<div class="card card-info pad-tight mt-md">

💡 **Intuition:** remove redundancy (RLE, Huffman, dictionary coding)

</div>

<div class="card card-accent pad-compact mt-md">

🔤 **RLE example:** `AAABBBCC` → `3A3B2C` (8 chars → 6 chars)

</div>

---
hideInToc: true
---

# Error Detection & Hashing

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🔍 **Error Detection**

Parity, checksums, CRC detect transfer/storage errors

</div>

<div class="card card-secondary pad-tight">

## 🔐 **Hashing**

Cryptographic hashes (SHA-256) verify file integrity

</div>

</div>

---
hideInToc: true
---

# How These Concepts Connect

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🔗 **In This Course**

- **File formats** → L3.2 (file handling), L5 (Python I/O)
- **Floating-point** → L9 (numerical precision in statistics), L10 (fitting)
- **Binary/hex** → L4 (memory hierarchy), L8 (git hashes)
- **Compression** → L11 (data formats like Parquet, HDF5)

</div>

<div class="card card-secondary pad-tight">

## 📚 **Going Deeper**

If you are interested in learning more basics of computer science, a great resource is an open course by Harvard University called **CS50**

</div>

</div>
