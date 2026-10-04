# L9: Concepts of Data Analysis

---

## Overview

**Duration**: ~120 minutes (2 h slot)

**Prerequisites**: L7-L8 (Python basics), general scientific literacy

**Learning Objectives**:
- Define data analysis, data science, and distinguish them from related fields
- Describe the end-to-end data analysis lifecycle
- Classify data by type, structure, and level of measurement
- Apply data quality criteria to assess a dataset
- Explain the FAIR principles and why they matter for reproducibility
- Identify common biases and pitfalls in data analysis

---

## Lecture Structure

### Part 1: What Is Data Analysis? (15 min)
- Data vs information vs knowledge vs wisdom (DIKW hierarchy)
- Data analysis vs data science vs statistics vs machine learning
- Four flavours of analytics: descriptive, diagnostic, predictive, prescriptive
- Interactive: "What data do you encounter daily?" discussion

### Part 2: The Data Analysis Lifecycle (20 min)
- 6-phase simplified lifecycle: Question → Collect → Clean → Analyse → Visualise → Communicate
- 9-stage detailed lifecycle (for reference)
- Key insight: the lifecycle is iterative, not linear
- Mermaid diagram walkthrough

### Part 3: Data Fundamentals (20 min)
- Data shapes: tabular, hierarchical (JSON/XML), graph, spatial, multimedia
- Structured vs semi-structured vs unstructured
- Levels of measurement: nominal, ordinal, interval, ratio (with examples)
- Continuous vs discrete, granularity, time dimension
- Metadata: "data about data"

### Part 4: Data Quality & Common Issues (20 min)
- Quality dimensions: completeness, consistency, validity, accuracy, timeliness, uniqueness
- Missing data types: MCAR, MAR, MNAR
- Outliers: when to keep, when to investigate
- Biases: sampling bias, survivorship bias, confirmation bias
- The p-hacking problem (preview for L11)

### Part 5: FAIR Principles & Ethics (15 min)
- Findable (persistent identifiers, metadata)
- Accessible (open protocols, authentication where needed)
- Interoperable (common vocabularies, linked data)
- Reusable (clear licences, provenance, community standards)
- Data ethics: consent, privacy, GDPR/HIPAA, responsible use

### Part 6: Tools & Putting It All Together (10 min)
- Analytics stack: spreadsheets → SQL → Python/R → specialised tools
- Case study: CERN Open Data Portal
- Discussion: "Plan your own analysis" exercise

---

## Teaching Tips

### Common Student Struggles

1. **"This is too abstract — when do we code?"**
   - Frame this lecture as building vocabulary: "You need to know what to ask for before you can code it"
   - Use CERN examples to ground every concept
   - Promise: "L10 (visualisation) and L12 (fitting) are where theory meets code"

2. **"What's the difference between nominal and ordinal?"**
   - Nominal = labels with no order (particle type: electron, muon, tau)
   - Ordinal = labels with order but unequal spacing (education level: BSc, MSc, PhD)
   - Use concrete physics examples throughout

3. **"Why do FAIR principles matter to me?"**
   - "Can you reproduce your lab partner's analysis from last month?"
   - Show a real example of irreproducible research
   - Connect to L14 (Reproducible Workflows)

4. **"What's the difference between data analysis and data science?"**
   - Data analysis: answering specific questions with data
   - Data science: broader field including ML, engineering, product decisions
   - In practice, there's significant overlap — don't stress the boundary

### Interactive Elements

- **Think-pair-share**: "What data do you interact with daily?" → classify by type
- **Data audit exercise**: Take a dataset, evaluate it against the quality criteria
- **Discussion**: "Is this ethical?" — present borderline data-use scenarios
- **Plan-your-analysis**: Students outline all 6 lifecycle phases for a hypothetical experiment

---

## Common Questions & Answers

**Q**: Is Excel data analysis?
**A**: Yes! Spreadsheets are data analysis tools. The concepts (cleaning, filtering, summarising, visualising) are the same whether you use Excel or Python. Python is better for reproducibility, scale, and automation.

**Q**: What's the difference between structured and semi-structured data?
**A**: Structured = rigid schema, every row has the same columns (database table, CSV). Semi-structured = flexible schema, records can have different fields (JSON, XML). Unstructured = no schema (text, images, audio).

**Q**: How do I know if my data has bias?
**A**: Ask: "Who/what is missing from this dataset?" and "How was this data collected?" Survivorship bias, selection bias, and measurement bias are the most common. There's no automated test — it requires domain knowledge and critical thinking.

**Q**: Do FAIR principles mean all data must be open?
**A**: No! FAIR is about making data findable, accessible, interoperable, and reusable — but "accessible" can mean "available with authentication." Medical data can be FAIR without being publicly open.

---

## Key Reference Tables

### The DIKW Hierarchy

| Level | Definition | Example |
|-------|-----------|---------|
| **Data** | Raw facts, numbers, signals | Detector voltage readings |
| **Information** | Data with context and meaning | "Particle hit at position (x,y) at time t" |
| **Knowledge** | Information interpreted with expertise | "This pattern indicates a muon decay" |
| **Wisdom** | Knowledge applied to decisions | "We need more shielding in sector 4" |

### Four Types of Analytics

| Type | Question | Example |
|------|----------|---------|
| **Descriptive** | What happened? | "Average beam intensity was 2.3×10¹¹" |
| **Diagnostic** | Why did it happen? | "Intensity dropped because of magnet quench" |
| **Predictive** | What will happen? | "Model predicts 15% signal increase at higher energy" |
| **Prescriptive** | What should we do? | "Optimise collimator settings to maximise luminosity" |

### Levels of Measurement

| Level | Properties | Operations | Example |
|-------|-----------|-----------|---------|
| **Nominal** | Categories only | =, ≠ | Particle type (e, μ, τ) |
| **Ordinal** | Categories + order | =, ≠, <, > | Energy range (low, medium, high) |
| **Interval** | Order + equal spacing | =, ≠, <, >, +, − | Temperature in °C |
| **Ratio** | Interval + true zero | All operations | Mass in GeV |

### Data Quality Checklist

- [ ] **Complete**: Are there missing values? How many? Why?
- [ ] **Consistent**: Do related fields agree? (e.g., city matches postal code)
- [ ] **Valid**: Do values fall within expected ranges?
- [ ] **Accurate**: Do values reflect the true state?
- [ ] **Timely**: Is the data current enough for the analysis?
- [ ] **Unique**: Are there duplicate records?

---

## Further domain examples

The lecture slides walk through five domains in depth (Biomedicine & Genomics,
Environmental Sciences, Astronomy, Particle Physics, Finance). The same
decision-first analysis mindset applies across many more fields:

- **Social sciences** — economic forecasting from macro indicators and behavioural
  data; survey and text analysis for sentiment, misinformation, and community
  wellbeing; informs policy, marketing, and civic planning
- **Engineering** — predictive maintenance on turbines, trains, and manufacturing
  lines; quality control with computer vision and statistical process control;
  structural health monitoring with sensors plus physics-informed models
- **Healthcare operations** — epidemiology tracking outbreaks and transmission
  dynamics; hospital patient flow, staffing, and supply-chain optimisation; strong
  ethical constraints (privacy, bias, explainability)
- **Sports analytics** — performance analysis from tracking sensors and video;
  strategy optimisation and opponent scouting; data-driven coaching, recruitment,
  and ticket pricing
- **Product & business** — growth funnels (acquisition → retention → revenue);
  A/B testing and causal inference; customer segmentation and lifetime value
- **Public policy & urban planning** — smart-city sensors for transport, energy,
  and waste; open data portals for transparency; geospatial analysis for zoning
  and emergency response
- **Education & learning analytics** — LMS logs revealing engagement patterns;
  early-warning systems for student support; balancing personalisation with
  fairness and privacy

---

## Time Estimates

- Lecture (Parts 1-5): 80 min
- Discussion and exercises: 20 min
- Case study walkthrough: 10 min
- Q&A: 10 min
- **Total**: ~120 min

---

## Resources for Students

- [CERN Open Data Portal](https://opendata.cern.ch/)
- [FAIR Principles (GO FAIR)](https://www.go-fair.org/fair-principles/)
- [Data Carpentry lessons](https://datacarpentry.org/lessons/)
- Hadley Wickham, "Tidy Data" (Journal of Statistical Software, 2014)

---

## Assessment Ideas

- **Quiz**: "Classify these variables by level of measurement" / "Which FAIR principle does this violate?"
- **Data audit**: Give students a messy dataset — identify 5 quality issues and propose fixes
- **Discussion essay**: "A researcher shares their analysis code but not the data. Is the analysis reproducible? Is it FAIR?"
- **Lifecycle planning**: Students write a 1-page plan for an analysis following the 6-phase lifecycle
