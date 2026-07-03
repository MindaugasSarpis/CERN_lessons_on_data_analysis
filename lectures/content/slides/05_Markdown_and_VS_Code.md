---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false


title: "Markdown"
layout: cover
---

# Dr. Mindaugas Šarpis

# Best Research and Data Analysis Practices from CERN

## Markdown & VS Code

##### <span class="aims-badge">🔧 tool-agnostic · ♻️ reproducibility</span>

<!--
Speaker: two tools in one lecture — Markdown (what you write) and VS Code (the
workshop you write it in). Both are portable, tool-agnostic skills they'll use
for the rest of the course. (~1 min)
-->

---
hideInToc: true
layout: quote
---

# Markdown turns **plain text** into beautifully formatted documents. Learn the syntax once, and you can write READMEs, documentation, notebooks, presentations, and scientific reports — all from a simple text editor.

---
hideInToc: true
---

# Learning **Objectives**

<div class="note-text mt-sm">By the end of this lecture, you will be able to:</div>

<div class="stack-tight mt-sm">

<div class="card card-primary card-glass pad-compact">

📝 Write formatted documents in **Markdown** — headers, emphasis, lists

</div>

<div class="card card-secondary card-glass pad-compact">

📊 Add **tables**, **code blocks**, and **task lists** to your writing

</div>

<div class="card card-accent card-glass pad-compact">

🖥️ Navigate **VS Code** — the sidebar, editor, and integrated terminal

</div>

<div class="card card-success card-glass pad-compact">

🎯 Drive the editor from the **Command Palette**, not menus

</div>

<div class="card card-warning card-glass pad-compact">

🧩 Extend VS Code with **extensions** for Python, Markdown, and Git

</div>

</div>

<!--
Speaker: read these as promises, not a syllabus. Markdown first, then the VS Code
workshop where they write it. Point at Seminar 5, where they document their own
project's README. (~1 min)
-->

---
hideInToc: true
---

# <span class="gradient-text">Markdown</span>

<div class="card card-info card-glass pad-tight reveal-left">

## 📝 **What is Markdown?**

- **Lightweight markup language** with plain text formatting syntax
- **Converts** plain text to **HTML**
- **Easy to read** and **write**
- **Simple** and **intuitive**

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight reveal-up">

## 🎯 **Purpose**

📄 Documentation • 📓 Notebooks • 🖥️ Presentations • 🌐 Websites • 📊 Scientific reports

</div>

<div class="card card-secondary card-glass pad-tight reveal-up">

## 🔧 **Used In**

GitHub READMEs • Jupyter Notebooks • Slidev • Jekyll • Hugo • Obsidian • Notion

<div class="note-text mt-sm">Remember using <code>touch README.md</code> from the CLI? That file was Markdown!</div>

</div>

</div>

---
hideInToc: true
layout: section
---

# Markdown **Syntax**

<!--
Speaker: the whole language is a handful of symbols — #, *, -, [], `, |. By the
end of this section they will know ~90% of the Markdown they'll ever use. (~30 sec)
-->

---
hideInToc: true
---

# Markdown Syntax: Headers

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ✏️ **Syntax**

```
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

<div class="note-text mt-sm">Use <code>#</code> for different header levels — more <code>#</code> symbols mean smaller headers</div>

</div>

<div class="card card-secondary card-glass pad-compact">

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

<div class="card card-primary card-glass pad-tight">

## ✏️ **Syntax**

```
*Italic* or _Italic_
**Bold** or __Bold__
~~Strikethrough~~
```

<div class="note-text mt-sm">Combine them: <code>***bold italic***</code> or <code>**~~bold strikethrough~~**</code></div>

</div>

<div class="card card-secondary card-glass pad-tight">

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

<div class="card card-primary card-glass pad-tight">

## ✏️ **Paragraphs**

```
This is the first paragraph.

This is the second paragraph.
(Separated by a blank line.)
```

</div>

<div class="card card-secondary card-glass pad-tight">

## ↩️ **Line Breaks**

```
First line with two spaces at the end.··
Second line appears below.
```

<div class="note-text mt-sm">Add <strong>two spaces</strong> at the end of a line (shown as <code>··</code> in the example), or use <code>&lt;br&gt;</code>, to force a line break <em>within</em> the same paragraph. Without them, adjacent lines merge into one.</div>

</div>

</div>

<div class="card card-warning card-glass pad-tight mt-md">

## ⚠️ **Common Beginner Mistake**

Pressing Enter once does **not** create a new line in the output — Markdown joins adjacent lines into a single paragraph. Use a **blank line** for a new paragraph, or **two trailing spaces** for a line break.

</div>

---
hideInToc: true
---

# Lists: Ordered & Unordered

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

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

<div class="card card-secondary card-glass pad-tight">

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

<div class="note-text mt-sm">You can use <code>-</code>, <code>*</code>, or <code>+</code> for unordered lists. Indent with 2 or 4 spaces for nesting.</div>

</div>

</div>

---
hideInToc: true
---

# Lists: Task Lists

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ✏️ **Task List Syntax**

```
- [x] Task 1 (completed)
- [ ] Task 2 (pending)
- [ ] Task 3 (pending)
```

<div class="note-text mt-sm"><code>[x]</code> marks a task as done, <code>[ ]</code> leaves it unchecked. Supported on GitHub, GitLab, and many editors.</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## 👁️ **Rendered Output**

<div class="mt-md">

- [x] Task 1 (completed)
- [ ] Task 2 (pending)
- [ ] Task 3 (pending)

</div>

</div>

</div>

<div class="card card-info card-glass pad-tight mt-md">

## 💡 **Where Task Lists Shine**

Task lists are widely used in **GitHub Issues** and **Pull Requests** to track progress on work items, code review steps, and release checklists.

</div>

---
hideInToc: true
---

# Links & Images

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🔗 **Links**

```
[CERN](https://home.cern)
```

<div class="mt-sm">

## [CERN](https://home.cern)

</div>

<div class="note-text mt-sm">For a document with many links, <strong>reference style</strong> keeps prose readable: <code>[CERN][1]</code> in the text, <code>[1]: https://home.cern</code> at the bottom.</div>

</div>

<div class="card card-secondary card-glass pad-tight">

## 🖼️ **Images**

```
![Markdown Logo](figures/markdown_mark.svg)
```

<div class="mt-sm">

<img src="/figures/markdown_mark_light.svg" alt="Markdown Logo" class="h-24">

</div>

</div>

</div>

---
hideInToc: true
---

# Code Blocks

<div class="card card-info card-glass pad-tight">

## 💻 **Inline Code**

```
Use `inline code` within a sentence.
```

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📦 **Code Block**

- Wrap code in triple backticks to create a code block

```
function hello() {
  console.log("Hello, world!");
}
```

</div>

<div class="card card-accent card-glass pad-tight">

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

<div class="card card-primary card-glass pad-tight">

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

<div class="card card-secondary card-glass pad-tight">

## 👁️ **Rendered Output**

> This is a blockquote.
> It can span multiple lines.

<div class="mt-md">

***

</div>

<div class="note-text mt-sm">Blockquotes are great for highlighting quotations or important notes. Horizontal rules (<code>---</code>, <code>***</code>, or <code>___</code>) create visual separators between sections.</div>

</div>

</div>

---
hideInToc: true
---

# Tables

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ✏️ **Table Syntax**

```
| Syntax    | Description |
|-----------|-------------|
| Header    | Title       |
| Cell      | Data        |
```

<div class="note-text mt-sm">Use <code>|</code> to separate columns and <code>---</code> for the header row separator. Colons control alignment: <code>:---</code> left, <code>:---:</code> center, <code>---:</code> right.</div>

</div>

<div class="card card-secondary card-glass pad-tight">

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

# Where You'll Meet Markdown Again

<div class="stack-tight mt-md">

<div class="card card-primary card-glass pad-compact reveal-left">

📄 **Project READMEs** — the front page of every repository *(you'll version-control one in the Git lecture)*

</div>

<div class="card card-secondary card-glass pad-compact reveal-left">

📓 **Jupyter notebooks** — every text cell between your Python code is Markdown

</div>

<div class="card card-accent card-glass pad-compact reveal-left">

🖥️ **These very slides** — the deck you're looking at is written in Markdown (Slidev)

</div>

<div class="card card-success card-glass pad-compact reveal-left">

🌐 **Issues, wikis, chat** — GitHub/GitLab discussions, MkDocs sites, even Discord messages

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md reveal-up">

💡 One hour of Markdown pays off for the rest of your career — it's the *lingua franca* of technical writing.

</div>

---
hideInToc: true
---

# Key Takeaways

<div class="card card-info card-glass pad-tight glow reveal-up">

## 📋 **Key Takeaways**

- Markdown is a **simple, readable** syntax that converts plain text to formatted HTML
- Master the basics: **headers**, **emphasis**, **lists**, **links**, **images**, **code blocks**, and **tables**
- Line breaks need **two trailing spaces** or a **blank line** — a common gotcha
- Markdown is used everywhere: GitHub, Jupyter, Slidev, documentation sites

</div>

---
hideInToc: true
---

# Practice Exercise

<div class="card card-success card-glass pad-compact mt-md">

## 🚀 **Practice Exercise**

From the CLI, run `touch about_me.md` and open it in VS Code. Include:

1. A **level-1 header** with your name
2. A short **paragraph** about yourself (use bold and italic)
3. An **unordered list** of your hobbies
4. A **link** to your favourite website
5. A **code block** with a "Hello, World!" snippet in any language

Then preview it: open VS Code's Markdown preview with `Ctrl+Shift+V` (or `Cmd+Shift+V` on Mac).

<div class="note-text mt-sm">We will version-control this file with <strong>git</strong> very soon!</div>

</div>

---
disabled: true
---

---
hideInToc: true
---

# What is VS Code?

<div class="card card-info card-glass pad-tight mt-sm">

## 💡 **Text Editor vs IDE**

- A **text editor** edits plain text files (Notepad, nano, vim)
- An **IDE** (Integrated Development Environment) adds tools: debugging, build automation, version control
- **VS Code** sits in between — a lightweight editor with IDE-level features through extensions

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-scale">

🆓 **Free & open-source** — works on Windows, macOS, Linux

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale">

🧩 **Extensible** — thousands of extensions for any language or workflow

</div>

</div>

---
hideInToc: true
---

# Installing VS Code

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 💻 **Download & Install**

1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download for your OS
3. Run the installer

</div>

<div class="card card-secondary card-glass pad-tight">

## ⚡ **Verify from the CLI**

```bash
code --version
```

If this works, VS Code is ready and available from your terminal.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

🐧 **Linux tip:** install via `snap`, or via `apt`/`dnf` after adding Microsoft's package repository — both give automatic updates.

</div>

---
layout: section
hideInToc: true
---

# The VS Code **Interface**

<!--
Speaker: switch from writing to the workshop. Orient them on the three regions
they'll live in daily — sidebar, editor, terminal. (~30 sec)
-->

---
hideInToc: true
---

# Interface Overview

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 📂 **Sidebar** (left)

- **Explorer** — file tree of your project
- **Search** — find text across all files
- **Source Control** — Git integration
- **Extensions** — install add-ons
- **Run & Debug** — execute and debug code

Toggle with `Ctrl+B` / `Cmd+B`

</div>

<div class="card card-secondary card-glass pad-tight">

## ✏️ **Editor** (center)

- Tabs for open files
- Syntax highlighting for dozens of languages out of the box — 100+ with extensions
- Split view: drag a tab to the side
- Minimap on the right for quick navigation

</div>

</div>

<div class="card card-info card-glass pad-compact mt-md">

💡 **Open a folder, not a file.** `File → Open Folder` (or `code my_project/` from the CLI) gives VS Code full project context — search, Git, and extensions all work better.

</div>

---
hideInToc: true
---

# The Integrated Terminal

<div class="card card-primary card-glass pad-compact mt-md">

🖥️ Open with `` Ctrl+` `` (backtick) or `View → Terminal` — runs your system shell **inside** VS Code

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-secondary card-glass pad-compact">

📂 Automatically opens in your **project folder**

</div>

<div class="card card-accent card-glass pad-compact">

➕ Click `+` for multiple terminals, drag to **split** side-by-side

</div>

</div>

<div class="card card-success card-glass pad-tight mt-md">

## 🧪 **Try It**

1. Open VS Code and press `` Ctrl+` ``
2. Run `pwd` (or `Get-Location`) — you should see your project path
3. Run `ls` to see your files listed

</div>

---
hideInToc: true
---

# The <span class="gradient-text">Command Palette</span>

<div class="card card-accent card-glass pad-tight mt-sm glow">

## 🎯 **Your Most Powerful Tool**

Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the **Command Palette** — a searchable menu for every VS Code action.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-compact reveal-scale">

🔍 Type `theme` to change the colour theme

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale">

🔍 Type `terminal` to open/close the terminal

</div>

<div class="card card-info card-glass pad-compact reveal-scale">

🔍 Type `markdown` to preview a `.md` file

</div>

<div class="card card-success card-glass pad-compact reveal-scale">

🔍 Type `settings` to customise VS Code

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ Don't memorise menus — learn the Command Palette. If you can describe what you want, you can find it.

</div>

---
hideInToc: true
---

# Settings Worth Changing

<div class="card card-info card-glass pad-compact mt-sm">

Open settings: `Ctrl+,` (or `Cmd+,` on Mac), then search by name.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ⚙️ **Editor Settings**

- **Auto Save** → `afterDelay` (never lose work)
- **Word Wrap** → `on` (no horizontal scrolling)
- **Font Size** → `14`–`16` for comfort
- **Tab Size** → `4` (Python standard)

</div>

<div class="card card-secondary card-glass pad-tight">

## 🎨 **Appearance**

- **Color Theme** → pick one you like (Dark Modern is the default)
- **Icon Theme** → Material Icon Theme (clearer file icons)
- **Minimap** → turn off if it distracts you

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

💡 Settings are stored as JSON — you can copy them between machines or share them with collaborators.

</div>

---
layout: section
hideInToc: true
---

# Essential **Features**

<!--
Speaker: these are the "why VS Code feels fast" tricks — multi-cursor, find &
replace, shortcuts. Demo multi-cursor live if you can; it always gets a reaction. (~30 sec)
-->

---
hideInToc: true
---

# Editing Superpowers

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## ⌨️ **Multi-Cursor Editing**

- `Alt+Click` — add cursors anywhere
- `Ctrl+D` — select next occurrence of word
- `Ctrl+Shift+L` — select all occurrences

Edit multiple lines simultaneously!

</div>

<div class="card card-secondary card-glass pad-tight">

## 🔎 **Find & Replace**

- `Ctrl+F` — find in current file
- `Ctrl+H` — find and replace
- `Ctrl+Shift+F` — search across all files

Supports regex for powerful pattern matching.

</div>

</div>

---
hideInToc: true
---

# Keyboard Shortcuts Cheat Sheet

<div class="grid-2 mt-sm gap-md">

<div class="card card-info card-glass pad-compact">

| **Action** | **Windows/Linux** | **macOS** |
|------------|-------------------|-----------|
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Open terminal | `` Ctrl+` `` | `` Ctrl+` `` |
| Toggle sidebar | `Ctrl+B` | `Cmd+B` |
| Quick file open | `Ctrl+P` | `Cmd+P` |

</div>

<div class="card card-info card-glass pad-compact">

| **Action** | **Windows/Linux** | **macOS** |
|------------|-------------------|-----------|
| Find in file | `Ctrl+F` | `Cmd+F` |
| Find in project | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| Save file | `Ctrl+S` | `Cmd+S` |
| Comment line | `Ctrl+/` | `Cmd+/` |

</div>

</div>

<div class="card card-warning card-glass pad-compact mt-md">

⚠️ You don't need to memorise all of these. Start with **Command Palette**, **terminal toggle**, and **save**. The rest will come with practice.

</div>

<style>
table { font-size: 0.82em; }
td, th { padding-top: 0.28em; padding-bottom: 0.28em; }
</style>

---
layout: section
hideInToc: true
---

# **Extensions**

---
hideInToc: true
---

# Recommended Extensions

<div class="card card-info card-glass pad-compact mt-sm">

Open the Extensions panel with `Ctrl+Shift+X` and search by name. Click **Install**.

</div>

<div class="grid-2 mt-md gap-md">

<div class="card card-primary card-glass pad-tight">

## 🐍 **Python**

- Syntax highlighting, IntelliSense, linting
- Run scripts with a click or `Ctrl+F5`
- Notebooks via the companion **Jupyter** extension (one extra install)

Search: `ms-python.python`

</div>

<div class="card card-secondary card-glass pad-tight">

## 📝 **Markdown**

- Built-in preview: `Ctrl+Shift+V`
- Side-by-side editing + preview: `Ctrl+K V`
- Extensions: Markdown All in One, markdownlint

We used this earlier in the **Markdown** part of this lecture.

</div>

</div>

<div class="card card-accent card-glass pad-compact mt-md">

🧩 Other useful extensions: **GitLens** (Git blame/history), **Live Share** (real-time collaboration), **Remote - SSH** (edit files on a server)

</div>

---
layout: section
hideInToc: true
---

# Hands-On **Practice**

<!--
Speaker: hands on keyboards now. Walk the room while they scaffold the demo
project and run it from the integrated terminal — this is where it clicks. (~30 sec)
-->

---
hideInToc: true
---

# Practice: Your First VS Code Project

<div class="card card-success card-glass pad-tight mt-md">

## 🧪 **Hands-On** (5 min)

1. Open your terminal and create a project:

```bash
mkdir -p vs_code_demo/src
touch vs_code_demo/README.md vs_code_demo/src/hello.py
```

*(PowerShell: `mkdir vs_code_demo\src`, then `ni vs_code_demo/README.md, vs_code_demo/src/hello.py`)*

2. Open it in VS Code:

```bash
code vs_code_demo/
```

3. In the Explorer sidebar, click `hello.py` and type:

```python
print("Hello from VS Code!")
```

4. Open the integrated terminal (`` Ctrl+` ``) and run:

```bash
python src/hello.py      # macOS/Linux: python3
```

</div>

---
hideInToc: true
---

# Key Takeaways

<div class="card card-primary card-glass pad-compact mt-md reveal-up">

📂 **Open a folder, not a file** — VS Code gets full project context: search, Git, and extensions all work better

</div>

<div class="card card-secondary card-glass pad-compact mt-md reveal-up">

🎯 **The Command Palette finds everything** — press `Ctrl+Shift+P` and describe what you want

</div>

<div class="card card-accent card-glass pad-compact mt-md reveal-up">

🖥️ **The integrated terminal** (`` Ctrl+` ``) opens directly in your project folder

</div>

<div class="card card-info card-glass pad-compact mt-md reveal-up">

🧩 **Extensions add language support** — Python, Markdown, and more

</div>

---
hideInToc: true
---

<MCQ
  question="In Markdown, how do you force a line break within the same paragraph?"
  :options="[
    'Press Enter once at the end of the line',
    'End the line with two trailing spaces',
    'Leave a blank line between the two lines',
    'Start the second line with a backslash'
  ]"
  :correct="1"
  explanation="A single Enter merges adjacent lines into one paragraph; two trailing spaces force a break within a paragraph, while a blank line starts a whole new paragraph."
/>

---
hideInToc: true
---

# **Recap** — You Can Now…

<div class="grid-2 gap-md mt-sm">

<div class="card card-success card-glass pad-compact">

✅ Write and preview **Markdown** — headers, lists, links, code

</div>

<div class="card card-success card-glass pad-compact">

✅ Format data with **tables** and **task lists**

</div>

<div class="card card-success card-glass pad-compact">

✅ Work in **VS Code** — sidebar, editor, and integrated terminal

</div>

<div class="card card-success card-glass pad-compact">

✅ Move faster with the **Command Palette** and **extensions**

</div>

</div>

<div class="card card-accent card-glass pad-tight mt-md">

## 🔬 **Seminar 5 tie-in**

Write a real `README.md` for your project — documenting the data's **provenance**, its **columns and units**, and the **steps to rebuild** your results.

</div>

<!--
Speaker: the "you can now" beat — have them nod at each card. The Seminar 5 tie-in
makes it concrete: their own project gets a real README, written in Markdown, this
week. (~1 min)
-->

---
layout: quote
hideInToc: true
---

# VS Code is your workshop — the more tools you discover in it, the faster you build.

---
disabled: true
---
