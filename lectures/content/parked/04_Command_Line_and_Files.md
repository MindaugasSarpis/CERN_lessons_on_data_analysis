

<!-- Parked 2026-10-11 from Lecture 04, section The Shell, after slide 'A Command That Fails': on the 90-minute skip list; the section Tools & Environments took its time -->

---
hideInToc: true
---

# A Path That **Fails**

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact">

## 🍎 **macOS · zsh**

```text
% cat data/raw/D0_KPi.cvs
cat: data/raw/D0_KPi.cvs: No such file or directory
```

</div>

<div class="card card-secondary card-glass pad-compact">

## 🪟 **Windows · PowerShell**

```text
PS> cat data/raw/D0_KPi.cvs
Get-Content: Cannot find path
'C:\Users\ada\Documents\analysis-project\
data\raw\D0_KPi.cvs' because it does not
exist.
```

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

The program complains this time, not the shell: `cat` on macOS, `Get-Content` behind the alias `cat` in PowerShell. PowerShell turns the relative path into an absolute one and shows where it looked. The fix is the same in both shells: `pwd`, then `ls`, and complete the name with `Tab`.

</div>

<!--
Speaker: the typo is cvs for csv. A command
that works prints only what was asked for; a message means something went
wrong, and its first word says who noticed. (~2 min)
-->


<!-- Parked 2026-10-11 from Lecture 04, section Checksums & Backups, first slide: the same derivation stands in Lecture 03 (A Checksum by Hand); on the 90-minute skip list -->

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
294 mod 256  =  38

a    c    b
97 + 99 + 98 = 294   →   38
```

The sum, kept to one byte, is 38. Swap two letters and it stays 38: this change goes unseen.

</div>

<div class="card card-secondary card-glass pad-compact">

## 🔐 **SHA-256 mixes every byte**

```text
abc   ba7816bf…f20015ad
acb   8e976608…e272fa57
```

The same three bytes in another order give other digits, all 64 of them. Nobody has found two different files with the same SHA-256.

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

🧮 A checksum is a short number computed from every byte of a file. The same bytes always give the same number. Other digits mean other bytes, and that is what the check rests on.

</div>

<!--
Speaker: work the sum on the board: a is 97, b 98, c 99 (the ASCII table of
Lecture 3). mod 256 keeps the remainder after dividing by 256, so the sum fits
one byte: 294 - 256 = 38. The hashes are the SHA-256 of the three bytes abc
and acb (printf abc | shasum -a 256 on a Mac); only the first and last eight
of 64 hex digits are shown. (~2 min)
-->

