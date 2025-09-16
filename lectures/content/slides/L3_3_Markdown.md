---
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Lecture 3.3: Markdown"
layout: cover
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Lecture 3:

## Markdown

---
hideInToc: true
---

# Markdown 

- ## **Lightweight markup language** with plain text formatting syntax

- ## **Converts** plain text to **HTML**

- ## **Easy to read** and **write**

- ## **Simple** and **intuitive**

---
hideInToc: true
layout: two-cols-header
---

# Markdown Syntax

::left::

## Headers

<div style="max-width: 350px;">
```
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```
</div>

- Use `#` for different header levels:

## Emphasis

### Italic, Bold, and Strikethrough

<div style="max-width: 350px;">
```
*Italic* or _Italic_
**Bold** or __Bold__
~~Strikethrough~~
```
</div>

::right::

# Header 1

## Header 2

### Header 3

#### Header 4

##### Header 5

###### Header 6

&nbsp;

## *Italic*

## **Bold**

## ~~Strikethrough~~

---
hideInToc: true
layout: two-cols
---

# Lists

## Unordered List

<div style="max-width: 350px;">
```
- Item 1
- Item 2
  - Subitem 1
  - Subitem 2
```
</div>

## Ordered List

<div style="max-width: 350px;">
```
1. First
2. Second
3. Third
```
</div>

# Task Lists

<div style="max-width: 350px;">
```
- [x] Task 1
- [ ] Task 2
- [ ] Task 3
```
</div>

::right::

&nbsp;

- Item 1
- Item 2
  - Subitem 1
  - Subitem 2

&nbsp;

1. First
2. Second
3. Third

&nbsp;

- [x]  Task 1
- [ ]  Task 2
- [ ]  Task 3

---
hideInToc: true
layout: two-cols
---

## Links

<div style="max-width: 350px;">
```
[OpenAI](https://openai.com)
```
</div>

&nbsp;

## [OpenAI](https://openai.com)

::right::

## Images

<div style="max-width: 350px">
```
![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
```

</div>

&nbsp;

![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg/258px-Microsoft_Office_Excel_%282019%E2%80%93present%29.svg.png)

---
hideInToc: true
---

# Code Blocks

## Inline Code

<div style="max-width: 350px">
```
Use `inline code` within a sentence.
```
</div>

## Code Block

- Use triple backticks to create "```" a code block

<div style="max-width: 350px">
```
  function hello() {
  console.log("Hello, world!");
  }
```
</div>

## Syntax Highlighting

- Add the language name after the first set of backticks
- For example, `python`
  
<div style="max-width: 350px">
```python
def hello():
    print("Hello, world!")
```
</div>

---
hideInToc: true
layout: two-cols
---

## Blockquotes

<div style="max-width: 350px">
```
> This is a blockquote.
> It can span multiple lines.
```
</div>

## Horizontal Rule

<div style="max-width: 350px">

```
---
```
</div>

# Tables

<div style="max-width: 350px">
```
| Syntax | Description |
|--------|------------|
| Header | Title      |
| Cell   | Data       |
```
</div>

::right::

&nbsp;

> This is a blockquote.
> It can span multiple lines

&nbsp;

***

&nbsp;

| Syntax | Description |
|--------|------------|
| Header | Title      |
| Cell   | Data       |
