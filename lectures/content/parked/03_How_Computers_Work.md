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