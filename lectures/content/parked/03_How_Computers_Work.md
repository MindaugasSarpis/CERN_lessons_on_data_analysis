<!-- Parked 2026-10-13 from Lecture 03, the two slides after 'Integers of Fixed Width' (section 'Numbers in Computers'): replaced by 'Negative Numbers: Count Back from Zero' and 'Overflow: 127 + 1 in 8 Bits', which explain two's complement with an odometer instead of the flip-and-add-one recipe and negative weights. -->

---
hideInToc: true
---

# Negative Numbers: **Two's Complement**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🧮 **The recipe, in 4 bits**

From 5 to −5:

1. Start: `0101`, which is 5
2. Flip every bit: `1010`
3. Add one: `1011`, which is −5

A set top bit means negative.

</div>

<div class="card card-accent card-glass pad-compact">

## ✨ **Addition just works**

```text
  0101   (+5)
+ 1011   (−5)
------
 10000 → 0000 = 0
```

The carry falls off the fixed width. No subtraction circuit is needed.

</div>

</div>

<div class="note-text mt-sm">8 bits hold −128 to +127: one more negative value than positive.</div>

<!--
**Say:** there is no minus sign in hardware. Negative integers are a convention, and two's complement is the one every processor uses.
(~2 min)
-->

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

The recipe agrees: flip `1101` to `0010`, add one, `0011` is 3. The pattern is −3.

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

⚠️ `11111111` is 255 as an unsigned integer and −1 as a signed one. The bits do not say which. The type says it, so the type is written down with the data.

</div>

<!--
**Say:** the weights are the reason the recipe works, and they make reading a pattern a sum.
(~2 min)
-->

<!-- Parked 2026-10-13 from Lecture 03, after the hex table, section 'Data Representation'. The lecturer skipped the binary and hex computations of the numbers part; the remaining computations use weather values (−16.3, 9.4, the bytes of weather.csv). -->

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


<!-- Parked 2026-10-13 from Lecture 03, after '0x2A in Decimal', section 'Data Representation'. The lecturer skipped the binary and hex computations of the numbers part; the remaining computations use weather values (−16.3, 9.4, the bytes of weather.csv). -->

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


<!-- Parked 2026-10-13 from Lecture 03, after 'Logical Operations', section 'How Computers Compute'. The lecturer skipped the binary and hex computations of the numbers part; the remaining computations use weather values (−16.3, 9.4, the bytes of weather.csv). -->

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


<!-- Parked 2026-10-13 from Lecture 03, after 'float32: Sign, Exponent, Mantissa', section 'Numbers in Computers'; replaced by '−16.3 as a float32'. The lecturer skipped the binary and hex computations of the numbers part; the remaining computations use weather values (−16.3, 9.4, the bytes of weather.csv). -->

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


<!-- Parked 2026-10-13 from Lecture 03, after 'Floating-Point Rounding' (now 'The Sum of the Nine Daily Means'), section 'Numbers in Computers'. The lecturer skipped the binary and hex computations of the numbers part; the remaining computations use weather values (−16.3, 9.4, the bytes of weather.csv). -->

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


<!-- Parked 2026-10-13 from Lecture 03, after 'The Steps Between Floats', section 'Numbers in Computers'. The lecturer skipped the binary and hex computations of the numbers part; the remaining computations use weather values (−16.3, 9.4, the bytes of weather.csv). -->

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
