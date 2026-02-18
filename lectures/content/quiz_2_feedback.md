---
theme: ./theme
background: /figures/background_intro.jpg
class: text-left
transition: fade
title: "Quiz 2 – Git, Data Visualization & Data Types"
layout: cover
---

# 🧠 Quiz 2

## Git, Data Visualization & Data Types

---

<MCQ
  question="What is the primary purpose of version control systems like Git?"
  :options="[
    'To compile code faster',
    'To track changes in files and enable collaboration',
    'To execute programs automatically',
    'To compress files for storage'
  ]"
  :correct="1"
  explanation="Version control systems like Git track every modification to files in a special database. If a mistake is made, you can compare earlier versions and revert changes. They also enable multiple people to collaborate on the same project without overwriting each other's work."
/>

---

<MCQ
  question="What is the primary purpose of data visualization?"
  :options="[
    'To clean data',
    'To explore, understand, and communicate data insights',
    'To store data',
    'To collect raw data'
  ]"
  :correct="1"
  explanation="Data visualization transforms raw numbers into visual representations (charts, graphs, plots) that make patterns, trends, and outliers easier to spot and communicate to others."
/>

---

<MCQ
  question="Which of the following is an example of continuous data?"
  :options="[
    'Number of students in a class',
    'Heights of patients',
    'Blood type categories',
    'Customer feedback ratings'
  ]"
  :correct="1"
  explanation="Continuous data can take any value within a range (e.g., 170.5 cm, 171.23 cm). Heights are continuous because they can be measured to arbitrary precision. Student counts are discrete (whole numbers only), blood types are nominal categories, and ratings are ordinal."
/>

---

<MCQ
  question="What does the .gitignore file do?"
  :options="[
    'Lists files and directories that Git should not track',
    'Stores commit messages',
    'Configures user credentials',
    'Lists all branches in the repository'
  ]"
  :correct="0"
  explanation="The .gitignore file specifies files and directories that Git should ignore (not track). Common entries include compiled code, log files, temporary files, and sensitive data like API keys or passwords."
/>

---

<MCQ
  question="What should axes in a plot include to be properly labeled?"
  :options="[
    'Only numbers',
    'Variable names, units, and appropriate tick marks',
    'Just the variable names',
    'Color codes'
  ]"
  :correct="1"
  explanation="Good axis labels include: the variable name (what is being measured), units in parentheses or brackets (e.g., 'Temperature (°C)'), and clear tick marks at sensible intervals. This ensures the plot is self-explanatory."
/>

---

<MCQ
  question="What type of data are categories without a natural order, such as blood type?"
  :options="[
    'Nominal',
    'Ordinal',
    'Interval',
    'Ratio'
  ]"
  :correct="0"
  explanation="Nominal data consists of categories with no inherent order (blood type A is not 'greater than' type B). Ordinal data has order but unequal intervals (e.g., satisfaction ratings). Interval and ratio are for numerical data."
/>

---

<MCQ
  question="What is the Git staging area used for?"
  :options="[
    'To permanently delete files',
    'To prepare files before committing them to the repository',
    'To store remote repository URLs',
    'To configure Git settings'
  ]"
  :correct="1"
  explanation="The staging area (also called the 'index') is an intermediate area where you prepare changes before committing. Using <code>git add</code> moves changes to the staging area, and <code>git commit</code> saves them to the repository history."
/>

---

<MCQ
  question="Which chart type is most appropriate for visualizing the relationship between two continuous variables?"
  :options="[
    'Bar chart',
    'Scatter plot',
    'Pie chart',
    'Histogram'
  ]"
  :correct="1"
  explanation="Scatter plots show each data point as a dot positioned by its x and y values, revealing correlations, clusters, and outliers between two continuous variables. Bar charts compare categories, pie charts show parts of a whole, and histograms show single-variable distributions."
/>

---

<MCQ
  question="Which flavour of analytics answers the question 'What happened?'"
  :options="[
    'Descriptive',
    'Diagnostic',
    'Predictive',
    'Prescriptive'
  ]"
  :correct="0"
  explanation="Descriptive analytics summarizes historical data to understand what happened. Diagnostic asks 'why did it happen?', Predictive asks 'what will happen?', and Prescriptive recommends 'what should we do?'."
/>

---

<MCQ
  question="Which command stages all changes for the next Git commit?"
  :options="[
    'git commit -a',
    'git add --all',
    'git status',
    'git push'
  ]"
  :correct="1"
  explanation="<code>git add --all</code> (or <code>git add -A</code>) stages all changes including new, modified, and deleted files. Note: <code>git commit -a</code> only commits tracked modified files, not new untracked files."
/>

---

<MCQ
  question="What does a histogram display?"
  :options="[
    'Relationships between two variables',
    'The frequency distribution of a single continuous variable',
    'Categorical comparisons',
    'Time series trends'
  ]"
  :correct="1"
  explanation="A histogram divides continuous data into bins (intervals) and shows how many values fall into each bin using bar heights. It reveals the shape of the distribution: whether it's symmetric, skewed, unimodal, or bimodal."
/>

---

<MCQ
  question="What does the 'F' in FAIR data principles stand for?"
  :options="[
    'Fast',
    'Findable',
    'Flexible',
    'Formatted'
  ]"
  :correct="1"
  explanation="FAIR stands for Findable, Accessible, Interoperable, and Reusable. These principles guide scientific data management to maximize the value and usability of research data."
/>

---

<MCQ
  question="What does the command git clone do?"
  :options="[
    'Deletes a repository from a remote server',
    'Copies a repository from a remote server to your local machine',
    'Creates a new branch',
    'Merges branches'
  ]"
  :correct="1"
  explanation="<code>git clone &lt;url&gt;</code> creates a local copy of a remote repository, including all files, branches, and commit history. It's typically the first command you run when starting to work on an existing project."
/>

---

<MCQ
  question="When creating a histogram, what is a 'bin'?"
  :options="[
    'A range of values that groups data points into intervals',
    'The mean value of the data',
    'A marker for the median',
    'The total count of data points'
  ]"
  :correct="0"
  explanation="A bin is an interval that groups continuous values (e.g., 0–10, 10–20). The number and width of bins affects how the distribution appears—too few bins hide details, too many create noise."
/>

---

<MCQ
  question="What is metadata?"
  :options="[
    'Data about data, describing its context and properties',
    'The largest values in a dataset',
    'Mathematical transformations of data',
    'Deleted or corrupted data'
  ]"
  :correct="0"
  explanation="Metadata describes the data itself: when it was collected, by whom, what units are used, how it was processed, etc. Good metadata is essential for data to be findable and reusable by others."
/>

---

<MCQ
  question="What does the command git pull do?"
  :options="[
    'Pushes local changes to the remote repository',
    'Fetches and integrates changes from a remote branch to the current branch',
    'Deletes the current branch',
    'Displays the commit history'
  ]"
  :correct="1"
  explanation="<code>git pull</code> is essentially <code>git fetch</code> + <code>git merge</code>. It downloads changes from the remote repository and automatically merges them into your current branch."
/>

---

<MCQ
  question="In a histogram, what do the heights of the bars represent?"
  :options="[
    'The sum of all values',
    'The frequency or count of data points within each interval',
    'The standard deviation',
    'The cumulative percentage'
  ]"
  :correct="1"
  explanation="Each bar's height shows how many data points (frequency) or what proportion fall within that bin's range. Taller bars indicate more common values in the dataset."
/>

---

<MCQ
  question="What is reproducibility in data analysis?"
  :options="[
    'Running the same code multiple times',
    'The ability for others to obtain the same results using the same data and methods',
    'Making copies of your data files',
    'Repeating experiments with different datasets'
  ]"
  :correct="1"
  explanation="Reproducibility means another researcher (or your future self) can run your analysis on the same data and get identical results. This requires clear documentation, version control, and sharing code and data."
/>

---

<MCQ
  question="Which command displays the commit history in Git?"
  :options="[
    'git history',
    'git log',
    'git commits',
    'git show'
  ]"
  :correct="1"
  explanation="<code>git log</code> shows the commit history with commit hashes, authors, dates, and messages. Useful options include <code>--oneline</code> for a compact view and <code>--graph</code> for branch visualization."
/>

---

<MCQ
  question="Which chart type is most useful for showing data distribution across different categories?"
  :options="[
    'Scatter plot',
    'Bar chart',
    'Line chart',
    'Heatmap'
  ]"
  :correct="1"
  explanation="Bar charts use rectangular bars to compare values across categories. The length of each bar represents the value for that category, making comparisons easy to see at a glance."
/>
