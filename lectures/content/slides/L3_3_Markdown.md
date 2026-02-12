---
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Markdown"
layout: cover
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Markdown

---
hideInToc: true
layout: quote
---

# Markdown turns **plain text** into beautifully formatted documents. Learn the syntax once, and you can write READMEs, documentation, notebooks, presentations, and scientific reports — all from a simple text editor.

---
hideInToc: true
---

# Markdown

<div class="card card-info pad-tight">

## 📝 **What is Markdown?**

- **Lightweight markup language** with plain text formatting syntax
- **Converts** plain text to **HTML**
- **Easy to read** and **write**
- **Simple** and **intuitive**

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🎯 **Purpose**

📄 Documentation • 📓 Notebooks • 🖥️ Presentations • 🌐 Websites • 📊 Scientific reports

</div>

<div class="card card-secondary pad-tight">

## 🔧 **Used In**

GitHub READMEs • Jupyter Notebooks • Slidev • Jekyll • Hugo • Obsidian • Notion

</div>

</div>

---
hideInToc: true
---

# Markdown Syntax: Headers

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ✏️ **Syntax**

```
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

<div class="note-text mt-sm">Use `#` for different header levels — more `#` symbols mean smaller headers</div>

</div>

<div class="card card-secondary pad-tight">

## 👁️ **Rendered Output**

# Header 1

## Header 2

### Header 3

#### Header 4

##### Header 5

###### Header 6

</div>

</div>

---
hideInToc: true
---

# Markdown Syntax: Emphasis

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ✏️ **Syntax**

```
*Italic* or _Italic_
**Bold** or __Bold__
~~Strikethrough~~
```

<div class="note-text mt-sm">Combine them: `***bold italic***` or `**~~bold strikethrough~~**`</div>

</div>

<div class="card card-secondary pad-tight">

## 👁️ **Rendered Output**

<div class="mt-md">

## *Italic*

## **Bold**

## ~~Strikethrough~~

</div>

</div>

</div>

---
hideInToc: true
---

# Lists

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ✏️ **Unordered List**

```
- Item 1
- Item 2
  - Subitem 1
  - Subitem 2
```

## ✏️ **Ordered List**

```
1. First
2. Second
3. Third
```

## ✏️ **Task Lists**

```
- [x] Task 1
- [ ] Task 2
- [ ] Task 3
```

</div>

<div class="card card-secondary pad-tight">

## 👁️ **Rendered Output**

- Item 1
- Item 2
  - Subitem 1
  - Subitem 2

<div class="mt-sm">

1. First
2. Second
3. Third

</div>

<div class="mt-sm">

- [x]  Task 1
- [ ]  Task 2
- [ ]  Task 3

</div>

</div>

</div>

---
hideInToc: true
---

# Links & Images

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🔗 **Links**

```
[OpenAI](https://openai.com)
```

<div class="mt-sm">

## [OpenAI](https://openai.com)

</div>

</div>

<div class="card card-secondary pad-tight">

## 🖼️ **Images**

```
![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
```

<div class="mt-sm">

![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg/258px-Microsoft_Office_Excel_%282019%E2%80%93present%29.svg.png)

</div>

</div>

</div>

---
hideInToc: true
---

# Code Blocks

<div class="card card-info pad-tight">

## 💻 **Inline Code**

```
Use `inline code` within a sentence.
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📦 **Code Block**

- Use triple backticks to create "```" a code block

```
  function hello() {
  console.log("Hello, world!");
  }
```

</div>

<div class="card card-accent pad-tight">

## 🎨 **Syntax Highlighting**

- Add the language name after the first set of backticks
- For example, `python`

```python
def hello():
    print("Hello, world!")
```

</div>

</div>

---
hideInToc: true
---

# Blockquotes, Rules & Tables

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ✏️ **Blockquotes**

```
> This is a blockquote.
> It can span multiple lines.
```

## ✏️ **Horizontal Rule**

```
---
```

## ✏️ **Tables**

```
| Syntax | Description |
|--------|------------|
| Header | Title      |
| Cell   | Data       |
```

</div>

<div class="card card-secondary pad-tight">

## 👁️ **Rendered Output**

> This is a blockquote.
> It can span multiple lines

<div class="mt-sm">

***

</div>

<div class="mt-sm">

| Syntax | Description |
|--------|------------|
| Header | Title      |
| Cell   | Data       |

</div>

</div>

</div>
