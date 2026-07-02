---
background: /figures/background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "VS Code"
layout: cover
---

# Dr. Mindaugas Šarpis

# Data Analysis and Artificial Intelligence

## VS Code

---
hideInToc: true
layout: quote
---

# A good code editor is the cockpit of your workflow. Learn to fly it well, and everything — writing, running, debugging — becomes faster.

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

<div class="card card-primary card-glass pad-compact reveal-scale" v-click>

🆓 **Free & open-source** — works on Windows, macOS, Linux

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale" v-click>

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

🐧 **Linux tip:** install via your package manager (`apt`, `dnf`, `snap`) for automatic updates.

</div>

---
layout: section
hideInToc: true
---

# The VS Code **Interface**

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
- Syntax highlighting for 100+ languages
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

<div class="card card-primary card-glass pad-compact reveal-scale" v-click>

🔍 Type `theme` to change the colour theme

</div>

<div class="card card-secondary card-glass pad-compact reveal-scale" v-click>

🔍 Type `terminal` to open/close the terminal

</div>

<div class="card card-info card-glass pad-compact reveal-scale" v-click>

🔍 Type `markdown` to preview a `.md` file

</div>

<div class="card card-success card-glass pad-compact reveal-scale" v-click>

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

- **Color Theme** → pick one you like (Dark+ is the default)
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
- Jupyter notebook support built-in

Search: `ms-python.python`

</div>

<div class="card card-secondary card-glass pad-tight">

## 📝 **Markdown**

- Built-in preview: `Ctrl+Shift+V`
- Side-by-side editing + preview: `Ctrl+K V`
- Extensions: Markdown All in One, markdownlint

We'll use this in the **next lecture**.

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
python src/hello.py
```

</div>

---
hideInToc: true
---

# Key Takeaways

<div class="card card-primary card-glass pad-compact mt-md reveal-up" v-click>

📂 **Open a folder, not a file** — VS Code gets full project context: search, Git, and extensions all work better

</div>

<div class="card card-secondary card-glass pad-compact mt-md reveal-up" v-click>

🎯 **The Command Palette finds everything** — press `Ctrl+Shift+P` and describe what you want

</div>

<div class="card card-accent card-glass pad-compact mt-md reveal-up" v-click>

🖥️ **The integrated terminal** (`` Ctrl+` ``) opens directly in your project folder

</div>

<div class="card card-info card-glass pad-compact mt-md reveal-up" v-click>

🧩 **Extensions add language support** — Python, Markdown, and more

</div>

---
layout: quote
hideInToc: true
---

# VS Code is your workshop — the more tools you discover in it, the faster you build.

---
disabled: true
---
