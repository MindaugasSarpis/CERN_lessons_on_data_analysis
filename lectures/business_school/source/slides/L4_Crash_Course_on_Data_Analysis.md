---
background: /intro_background.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Lecture 4: Introduction to Data Analysis"
layout: cover
---

# Dr. Mindaugas Šarpis
# Lessons on **Data Analysis** from **CERN**

## Lecture 4

## Introduction to Data Analysis

---
hideInToc: true
layout: fact
---

# What is **Data Analysis**? 

## <div v-click> What is **Data**? </div>

&nbsp;

#### <div v-after>  interactive exercise </div>

---
hideInToc: true
layout: quote
---

## **Data analysis** is a process of inspecting, cleaning, transforming, and modeling **data** with the goal of discovering useful **information**, informing conclusions, and supporting decision-making

&nbsp;

# Wikipedia

---
hideInToc: true
layout: fact
---

# What is **Data Science**?

---
hideInToc: true
layout: quote
---

## **Data science** is an interdisciplinary academic field that uses statistics, scientific computing, scientific methods, processing, scientific visualization, algorithms and systems to extract or extrapolate **knowledge and insights** from potentially noisy, structured, or unstructured data

&nbsp;

# Wikipedia

---
hideInToc: true
---

<v-clicks depth="2">

- # **Key Ideas** 

  - ## Any experiment (study or analysis) in any field of science will have a data analysis component

  - ## Normally, the **results of data analysis** appear in scientific **publications**

  - ## In business data analysis is imperative for **decision making**

</v-clicks>

---
layout: section
hideInToc: true
---

# Examples of **data analysis** in different fields of science and industry 

---
hideInToc: true
---

# **Bio medicine and Genomics**

- ## Genome Sequencing
  
- ## Clinical Trials

&nbsp;

### **23andMe** anyone (ancestry services)?

### Comparing against *reference populations*

---
hideInToc: true
---

# **Environmental Sciences**

- ## Climate Change Models

- ## Pollution Monitoring

- ## Biodiversity Studies

###### living analysis 

---
hideInToc: true
---

# **Social Sciences**

- ## Economic Forecasting
  
- ## Social Behavior Studies

###### may be qualitative analysis 

---
hideInToc: true
---

# **Astronomy** 

- ## Observational Data Analysis
  
- ## Gravitational Waves

- ## ...

---
hideInToc: true
---

# **Engineering**

- ## Predictive Maintenance

- ## Quality Control

- ## Structural Health Monitoring

---
hideInToc: true
---

# **Healthcare**

- ## Epidemiology
  
- ## Health Policy

- ## ... 
  
---
hideInToc: true
---

# **Finance** 

- ## Stock Market Analysis

- ## Risk Management

- ## Algorithmic Trading

---
hideInToc: true
---

# **Sports Analytics** 

- ## Performance Analysis
  
- ## Fan Engagement

---
layout: section
hideInToc: true
---

# **Steps of Data Analysis** 

---
hideInToc: true
---

- # 1. **Define the Problem or Research Question**

  - ## Formulation
  
    This might steer the choices in the following steps

  - ## Experimental Design

###### Interactive exercise 

---
hideInToc: true
---

- # 2. **Collect Data** 

  - ## How much data do you need?

  - ## What sort of data do you need?

  - ## What data formats should you chose?

  - ## Can you trust the data?

  - ## Can you collect the data?

---
hideInToc: true
---

- # 3. **Clean Data**

  - ## Data Selection

  - ## Data Stripping

  - ## Data Skimming

  - ## Data Wrangling

  - ## ...

---
hideInToc: true
---

- # 4. **Analyze Data**

  - ## Data Exploration

  - ## Statistical Analysis

  - ## Model Building

  - ## Machine Learning

  - ## Classification (...**AI**...)

---
hideInToc: true
---

- # 5. **Visualize the data**

  - ## What's your target audience?

  - ## What is the message you want to convey?

---
hideInToc: true
---

- # 6. **Interpret and report the results**

  - ## Draw Conclusions from Data

  - ## Report Findings

---
layout: section
hideInToc: true
---

# **Data Hygiene**

---
hideInToc: true
layout: section
---

# **F A I R**

--- 
layout: quote
hideInToc: true
---


## The first step in **(re)using data** is to find them. **Metadata** and data should be easy to find for both humans and computers. Machine-readable metadata are essential for automatic discovery of datasets and services, so this is an essential component of the FAIRification process.

---
hideInToc: true
---

# **Findable** data

- ## **F1.** (Meta)data are assigned a globally **unique** and persistent **identifier**

- ## **F2.** Data are described with **rich metadata**

- ## **F3.** **Metadata** clearly and explicitly **include the identifier** of the data they describe

- ## **F4.** (Meta)data are registered or indexed in a **searchable resource**

###### What's metadata?

---
hideInToc: true
---


# **Accessible** data

- ## **A1.** **(Meta)data** are retrievable by their **identifier** using a standardised communications protocol

  - ## **A1.1** The protocol is **open**, free, and universally implementable

  - ## **A1.2** The protocol allows for an **authentication** and **authorisation** procedure, where necessary

- ## **A2.** Metadata are accessible, even when the data are no longer available

---
hideInToc: true
---


# **Interoperable** data

- ## **I1.** (Meta)data use a formal, accessible, shared, and broadly applicable **language for knowledge representation**

- ## **I2.** (Meta)data use vocabularies that follow **FAIR principles**

- ## **I3.** (Meta)data include **qualified references** to other (meta)data

---
hideInToc: true
---

# **Reusable** data

- ## **R1.** (Meta)data are **richly described** with a plurality of accurate and relevant attributes

  - ## **R1.1.** (Meta)data are released with a clear and **accessible** data usage **license**

  - ## **R1.2.** (Meta)data are associated with detailed **provenance**

  - ## **R1.3.** (Meta)data meet **domain-relevant community standards**

---
layout: center
class: 'text-center'
---

<!-- Titles for the columns -->
<div class="grid grid-cols-2 gap-8 w-full mb-8">
  <h2 class="text-2xl font-bold">Proprietary Tools</h2>
  <h2 class="text-2xl font-bold">Programming Languages</h2>
</div>

<!-- Logos in two columns -->
<div class="grid grid-cols-2 gap-8 w-full">

  <!-- Column 1 -->
  <div class="flex flex-col items-center gap-6">
    <!-- Logo 1 -->
    <img src="/tableau_logo.png" alt="Logo 3" class="w-auto h-32" />
    <img src="/origin_logo.png" alt="Logo 1" class="w-auto h-32" />
    <img src="/excel_logo.png" alt="Logo 2" class="w-auto h-32" />
  </div>

  <!-- Column 2 -->
  <div class="flex flex-col items-center gap-6">
    <img src="/python_logo.png" alt="Logo 4" class="w-auto h-32" />
    <img src="/R_logo.png" alt="Logo 6" class="w-auto h-32" />
    <img src="/julia_logo.png" alt="Logo 5" class="w-auto h-32" />
  </div>

</div>
---
hideInToc: true
---

# **Proprietary** Tools 


- ## Expensive

- ## Limited in scope

- ## Lack compatibility

- ## Lack flexibility

- ## Easy to learn / use (GUI)

---
hideInToc: true
---


# **Programming** Languages

- ## Open Source

- ## Free

- ## Powerful

- ## Steep learning curve (CLI)

---
hideInToc: true
---

# **Discussion**  

- ## When to use proprietary tools?

- ## What should you be using?  

- ## Saturation of achieved proficiency
