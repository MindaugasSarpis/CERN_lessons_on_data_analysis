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

# Data analysis and Artificial Intelligence

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

<div class="note-text mt-sm">Remember creating <code>README.md</code> from the CLI in our earlier lectures? That was Markdown!</div>

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

<div class="card card-secondary pad-compact">

## 👁️ **Rendered Output**

<p style="font-size: 1.6em; font-weight: bold; margin: 0.15em 0;"><code>#</code> Header 1 — largest</p>
<p style="font-size: 1.35em; font-weight: bold; margin: 0.15em 0;"><code>##</code> Header 2</p>
<p style="font-size: 1.15em; font-weight: bold; margin: 0.15em 0;"><code>###</code> Header 3</p>
<p style="font-size: 1.0em; font-weight: bold; margin: 0.15em 0;"><code>####</code> Header 4</p>
<p style="font-size: 0.9em; font-weight: bold; margin: 0.15em 0;"><code>#####</code> Header 5 — getting small</p>
<p style="font-size: 0.8em; font-weight: bold; margin: 0.15em 0;"><code>######</code> Header 6 — smallest</p>

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

# Paragraphs & Line Breaks

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ✏️ **Paragraphs**

```
This is the first paragraph.

This is the second paragraph.
(Separated by a blank line.)
```

</div>

<div class="card card-secondary pad-tight">

## ↩️ **Line Breaks**

```
First line with two spaces at the end.··
Second line appears below.
```

<div class="note-text mt-sm">Add **two spaces** at the end of a line, or use `<br>`, to force a line break <em>within</em> the same paragraph. Without them, adjacent lines merge into one.</div>

</div>

</div>

<div class="card card-warning pad-tight mt-md">

## ⚠️ **Common Beginner Mistake**

Pressing Enter once does **not** create a new line in the output — Markdown joins adjacent lines into a single paragraph. Use a **blank line** for a new paragraph, or **two trailing spaces** for a line break.

</div>

---
hideInToc: true
---

# Lists: Ordered & Unordered

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

<div class="note-text mt-sm">You can use `-`, `*`, or `+` for unordered lists. Indent with 2 or 4 spaces for nesting.</div>

</div>

</div>

---
hideInToc: true
---

# Lists: Task Lists

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ✏️ **Task List Syntax**

```
- [x] Task 1 (completed)
- [ ] Task 2 (pending)
- [ ] Task 3 (pending)
```

<div class="note-text mt-sm">`[x]` marks a task as done, `[ ]` leaves it unchecked. Supported on GitHub, GitLab, and many editors.</div>

</div>

<div class="card card-secondary pad-tight">

## 👁️ **Rendered Output**

<div class="mt-md">

- [x]  Task 1 (completed)
- [ ]  Task 2 (pending)
- [ ]  Task 3 (pending)

</div>

</div>

</div>

<div class="card card-info pad-tight mt-md">

## 💡 **Where Task Lists Shine**

Task lists are widely used in **GitHub Issues** and **Pull Requests** to track progress on work items, code review steps, and release checklists.

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
![Markdown Logo](https://upload.wikimedia.org/
wikipedia/commons/4/48/Markdown-mark.svg)
```

<div class="mt-sm">

![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)

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

# Blockquotes & Horizontal Rules

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

</div>

<div class="card card-secondary pad-tight">

## 👁️ **Rendered Output**

> This is a blockquote.
> It can span multiple lines

<div class="mt-md">

***

</div>

<div class="note-text mt-sm">Blockquotes are great for highlighting quotations or important notes. Horizontal rules (`---`, `***`, or `___`) create visual separators between sections.</div>

</div>

</div>

---
hideInToc: true
---

# Tables

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ✏️ **Table Syntax**

```
| Syntax    | Description |
|-----------|-------------|
| Header    | Title       |
| Cell      | Data        |
```

<div class="note-text mt-sm">Use `|` to separate columns and `---` for the header row separator. Colons control alignment: `:---` left, `:---:` center, `---:` right.</div>

</div>

<div class="card card-secondary pad-tight">

## 👁️ **Rendered Output**

<div class="mt-md">

| Syntax | Description |
|--------|------------|
| Header | Title      |
| Cell   | Data       |

</div>

## ✏️ **Aligned Columns**

```
| Left   | Center | Right |
|:-------|:------:|------:|
| data   | data   | data  |
```

</div>

</div>

---
hideInToc: true
---

# Summary & Practice

<div class="card card-info pad-tight">

## 📋 **Key Takeaways**

- Markdown is a **simple, readable** syntax that converts plain text to formatted HTML
- Master the basics: **headers**, **emphasis**, **lists**, **links**, **images**, **code blocks**, and **tables**
- Line breaks need **two trailing spaces** or a **blank line** — a common gotcha
- Markdown is used everywhere: GitHub, Jupyter, Slidev, documentation sites

</div>

<div class="card card-success pad-tight mt-md">

## 🚀 **Practice Exercise**

Create a file called `about_me.md` and include the following:

1. A **level-1 header** with your name
2. A short **paragraph** about yourself (use bold and italic)
3. An **unordered list** of your hobbies
4. A **link** to your favourite website
5. A **code block** with a "Hello, World!" snippet in any language

</div>
