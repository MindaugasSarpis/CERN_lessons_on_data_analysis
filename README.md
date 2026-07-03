# Best Research and Data Analysis Practices from CERN

This repository contains lectures and materials for data analysis courses at CERN.

## Setup

### Prerequisites

- Node.js (v20+ recommended)
- pnpm
- Conda or Mamba (for Python environment)

### Installation

```bash
# Node.js dependencies (Slidev, theme, addons)
pnpm install

# Python environment (for workbook and lecture examples)
conda env create -f env.yaml
conda activate lecture
```

## Running the Lectures

### Development Server

```bash
pnpm dev
```

This will start the Slidev server at http://localhost:3030/ with:
- Public slide show: http://localhost:3030/
- Presenter mode: http://localhost:3030/presenter/
- Slides overview: http://localhost:3030/overview/

### Building for Production

```bash
pnpm build
```

### Exporting to PDF

```bash
pnpm export
```

## Project Structure

```
.
├── lectures/
│   ├── content/
│   │   ├── lessons_on_data_analysis_from_CERN.md  # Master deck entry point
│   │   ├── slides/           # Individual lecture files (L1–L12)
│   │   └── theme/            # Custom Slidev theme
│   └── workbook/             # Student workbook (MkDocs)
├── env.yaml                  # Conda environment (Python deps)
├── package.json              # Node.js dependencies
└── README.md
```

## Technologies

- **Slidev** — Markdown-based slide framework
- **slidev-addon-python-runner** — Interactive Python code execution in slides
- **Mermaid** — Diagrams and flowcharts
- **UnoCSS** — Utility-first CSS engine
- **MkDocs** — Student workbook
