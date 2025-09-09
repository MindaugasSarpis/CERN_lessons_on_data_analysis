---
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Lecture 2: Crash Course on Computer Science"
layout: cover
download: true
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Lecture 2:

## Crash Course on Computer Science

---
layout: quote
hideInToc: true
---

# The main goal of this lecture is to promote algorithmic thinking and to provide a basic understanding of computer science concepts

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
layout: section
hideInToc: true
---

# Representation

---
layout: fact
hideInToc: true
---

# Unary

## <v-click> **Base-1** </v-click>

---
layout: center
hideInToc: true
class: text-size-64
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
layout: fact
hideInToc: true
---

# ASCII

## American Standard Code for Information Interchan

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
---

# File formats (extensions)

## Computer needs to know what a sequence of bits is supposed to mean

| **Text/Data** | **Documents** | **Media/Exec** |
|--------------|---------------|----------------|
| .txt        | .pdf          | .mp3           |
| .csv        | .docx         | .mp4           |
| .json       | .pptx         | .zip           |
| .xml        | .xlsx         | .rar           |
| .yaml       | .rtf          | .exe           |
| .md         | .odt          | .apk           |


---
hideInToc: true
---

# Image Quality vs Bit Depth

## Below are five versions of the same image, saved with **different bit depths**. Notice how fewer bits reduce both **image quality** and **file size**.

<div class="grid grid-cols-5 gap-4 mt-6">
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
layout: quote
hideInToc: true
---

# If you are interested in learning more basics of computer science, a great resource is an open course by Harward University called **CS50**
