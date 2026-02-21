# L7: Data Visualisation

---

## Overview

**Duration**: 90-120 minutes (lecture + hands-on)

**Prerequisites**: L5 (Python basics), L6 (Concepts of Data Analysis)

**Learning Objectives**:
- Explain why visualisation is essential for data analysis
- Identify and use visual aesthetics: position, colour, shape, size
- Name and construct common plot types (bar, histogram, scatter, line, box)
- Apply Tufte's data-to-ink ratio principle
- Choose the right chart for a given data relationship
- Design accessible visualisations (colourblind-safe palettes, redundant encodings)

---

## Lecture Structure

### Part 1: Why Visualise? (10 min)
- Visual perception is our highest-bandwidth sense
- Anscombe's quartet — same statistics, different stories
- The power of pattern discovery
- Dangers: visualisation can also deceive

### Part 2: Aesthetics & Components (20 min)
- Aesthetic mappings: position, colour, shape, size, line style
- Plot anatomy: axes, labels, tick marks, legends, title
- Legend placement best practices
- Common axis mistakes (truncated axes, non-zero baselines)

### Part 3: Common Chart Types (25 min)
- **Amounts**: bar charts (vertical, horizontal, grouped, stacked), heatmaps
- **Distributions**: histograms (bin width matters!), box plots
- **Relationships**: scatter plots, line plots
- **Common errors gallery**: 3D effects, unsorted bars, poor colour choices, too many categories
- Interactive: "What's wrong with this chart?" exercise

### Part 4: Design Principles (20 min)
- Tufte's data-to-ink ratio: maximise data, minimise ink
- Chart junk vs clean design (before/after examples)
- Choosing the right chart (decision flowchart)
- When NOT to use a pie chart
- Accessibility: viridis/cividis palettes, redundant encodings

### Part 5: Practice (25 min)
- Students create 4 plots:
  1. Histogram with appropriate bin width
  2. Bar chart of categorical data
  3. Add proper labels, legend, title
  4. Critique and improve their own plot
- Seminar alternative: Use Plotly for interactive plots

---

## Teaching Tips

### Common Student Struggles

1. **"My histogram looks weird"**
   - Almost always a bin width issue
   - Too few bins: lose structure. Too many bins: noise dominates
   - Rule of thumb: start with √N bins, then adjust
   - Show the same data with 5, 20, 50, 200 bins

2. **"When do I use a bar chart vs a histogram?"**
   - Bar chart = categorical data (particle types, countries)
   - Histogram = continuous data binned into intervals (mass spectrum, energies)
   - Bars have gaps (discrete categories), histograms don't (continuous bins)

3. **"My plot is unreadable"**
   - Increase font size (default matplotlib is too small for presentations)
   - Use `plt.tight_layout()` to prevent label clipping
   - Limit to 5-7 colours maximum
   - Remove gridlines unless they add information

4. **"I can't tell the lines apart"**
   - Use different line styles (`-`, `--`, `-.`, `:`) AND colours
   - This is redundant encoding — essential for accessibility
   - Consider: if printed in black and white, can you still read it?

### Interactive Elements

- **"What's wrong?"**: Show bad visualisations, students identify problems
- **Before/after**: Show the same data plotted badly and well
- **Live matplotlib**: Build a plot step-by-step in a notebook
- **Peer review**: Students swap plots and critique each other's work

---

## Common Questions & Answers

**Q**: Should I always start my y-axis at zero?
**A**: For bar charts: yes, always (bar length encodes value). For line/scatter plots: it depends — sometimes zooming in reveals important variation. Always label clearly.

**Q**: Is matplotlib the best plotting library?
**A**: matplotlib is the foundation — everything else (seaborn, plotly, bokeh) builds on it. Learn matplotlib first, then explore higher-level libraries. For publication-quality plots, matplotlib is hard to beat.

**Q**: How do I choose colours?
**A**: Use established palettes: viridis (sequential), Set2 or tab10 (categorical). Avoid red-green combinations (8% of men are red-green colourblind). Use [ColorBrewer](https://colorbrewer2.org/) for guidance.

**Q**: When is a pie chart acceptable?
**A**: Almost never. Humans are bad at comparing angles. Use a bar chart instead. The only exception: showing 2-3 parts of a whole where the message is "this dominates" (e.g., 90% vs 10%).

---

## Key Reference Tables

### Chart Selection Guide

| Data Relationship | Recommended Chart | Avoid |
|-------------------|------------------|-------|
| **Comparison** (few categories) | Bar chart | Pie chart |
| **Comparison** (many categories) | Horizontal bar chart | Vertical bar (labels overlap) |
| **Trend over time** | Line plot | Bar chart (suggests discrete) |
| **Distribution** (one variable) | Histogram, box plot | Bar chart |
| **Relationship** (two variables) | Scatter plot | Line plot (implies continuity) |
| **Part of whole** | Stacked bar, treemap | Pie chart |

### Colourblind-Safe Palettes

| Palette | Type | Best For |
|---------|------|----------|
| **viridis** | Sequential | Heatmaps, continuous data |
| **cividis** | Sequential | Perceptually uniform, colourblind-safe |
| **plasma** | Sequential | High contrast sequential |
| **Set2** | Qualitative | Categorical (up to 8 categories) |
| **tab10** | Qualitative | Categorical (up to 10 categories) |

### Data-to-Ink Ratio Checklist

- [ ] Remove background colour (use white)
- [ ] Remove unnecessary gridlines
- [ ] Remove chart borders/boxes
- [ ] Remove redundant labels
- [ ] Use direct labelling instead of legends where possible
- [ ] Remove 3D effects
- [ ] Simplify tick marks

### Plot Anatomy Quick Reference

```
Title (what the plot shows)
│
├── Y-axis label (with units!)
│   ├── Tick marks (sensible intervals)
│   └── Tick labels (readable font)
│
├── Data area
│   ├── Data points / bars / lines
│   ├── Error bars (if applicable)
│   └── Annotations (sparingly)
│
├── X-axis label (with units!)
│   ├── Tick marks
│   └── Tick labels
│
└── Legend (if multiple series)
    └── Place inside plot area or to the right
```

---

## Time Estimates

- Lecture (Parts 1-4): 75 min
- Practice exercises: 25 min
- Peer review / critique: 10 min
- Q&A: 10 min
- **Total**: ~120 min

---

## Resources for Students

- [Fundamentals of Data Visualization — Claus O. Wilke](https://clauswilke.com/dataviz/) (free online book)
- [matplotlib tutorials](https://matplotlib.org/stable/tutorials/)
- [ColorBrewer 2.0](https://colorbrewer2.org/) — colour palette tool
- [Plotly Python docs](https://plotly.com/python/)
- Edward Tufte, *The Visual Display of Quantitative Information*

---

## Assessment Ideas

- **Quiz**: "What's wrong with this visualisation?" (show 3 bad plots)
- **Practical**: "Create a publication-quality plot from this dataset" (must include labels, legend, appropriate chart type)
- **Critique exercise**: Give students a data journalism article — identify 3 visualisation strengths and 3 weaknesses
- **Redesign challenge**: Give students a bad plot and its data — redesign it following best practices
