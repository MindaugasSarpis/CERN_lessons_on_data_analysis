# CERN Lessons on Data Analysis

This repository contains lectures and materials for data analysis courses at CERN.

## Setup

### Prerequisites

- Node.js v25.1.0 (or later)
- pnpm v10.12.3 (or later)

### Installation

```bash
pnpm install
```

This will install all dependencies and automatically apply a compatibility patch for Slidev on Node.js v25.

## Running the Lectures

### Development Server

To start the Slidev development server for the Probability and Statistics lecture:

```bash
pnpm dev
```

This will start the server at http://localhost:3030/ with:
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
│   └── content/
│       └── slides/
│           └── L9_Probability_and_Statistics.md
├── scripts/
│   └── patch-slidev.sh
├── package.json
└── README.md
```

## Features

The Probability and Statistics lecture includes:

- Interactive Python code execution (via slidev-addon-python-runner)
- Mermaid diagrams for visualizing concepts
- Interactive demos for:
  - Dice rolling simulations
  - Bayes' theorem calculator
  - Central Limit Theorem demonstrations
  - Confidence interval visualizations
  - And more!

## Technologies

- **Slidev**: Modern slide deck framework
- **Python Runner**: Execute Python code directly in slides
- **Mermaid**: Create diagrams and flowcharts
- **UnoCSS**: Utility-first CSS engine
