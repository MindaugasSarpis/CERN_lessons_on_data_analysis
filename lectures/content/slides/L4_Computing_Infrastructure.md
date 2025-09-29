---
background: /background_intro.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Computing Infrastructure"
layout: cover
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Lecture 4:
  
## Computing Infrastructure

---
layout: fact
hideInToc: true
---

#  What constitutes **computing infrastructure**?
  
---
hideInToc: true
---

- # **Hardware Components**

  - ## Central Processing Unit (**CPU**)

  - ## Memory (**RAM**)

  - ## Storage Devices (**HDD, SSD, NVMe**)

  - ## Input/Output (**I/O**) Devices

  - ## Specialized Processors (**GPUs**, **TPUs**)

  - ## Power and Cooling

  - ## Networking

  - ## Monitoring and Management Tools

  - ## Security

---
hideInToc: true
---

- # **CPU** (Central Processing Unit)

  - ## Basic arithmetic, logic, control, and input/output operations

  - ## CPU sub-components

    - ### Control Unit (CU)

    - ### Arithmetic Logic Unit (ALU)

    - ### Registers

    - ### Cache

    - ### Buses

---
hideInToc: true
---

- # **CPU Performance** Factors:

  - ## Clock Speed

  - ## Number of Cores

  - ## Cache Size

  - ## Power Efficiency
    
---
hideInToc: true
layout: image
image: /cpu1.avif
---

---
hideInToc: true
layout: image
image: /cpu2.jpg
---

---
hideInToc: true
layout: image
image: /cpu_apple_M4.webp
---

---
hideInToc: true
---

- # **RAM** (Random Access Memory)

  - ## Volatile memory

  - ## High-Speed Access

  - ## Temporary Storage

  - ## Capacity (GB or TB)

  - ## Performance (MHz or GHz)

---
hideInToc: true
layout: image
image: https://miro.medium.com/v2/resize:fit:1400/format:webp/0*6k9X6LPiM4XKyssm.jpg
---

---
hideInToc: true
layout: image
image: https://www.pcworld.com/wp-content/uploads/2023/04/corsair-dominator-memory-100884308-orig-1.jpg?quality=50&strip=all
---

---
hideInToc: true
layout: center
---

<img src="/laptop_ram.png" class="w-auto">

---
hideInToc: true
---

- # **Storage** Devices:

  - ## **HDD** (Hard Disk Drive)

  - ## **SSD** (Solid State Drive)

  - ## **SSHD** (Solid State Hybrid Drive)

  - ## **NVMe** (Non-Volatile Memory Express)

<div style="margin-top: 5rem; text-align: center;">

```mermaid {scale: 1.5}
graph LR
    A[cashes] --> B[RAM] --> C[Drive Storage]
    
    classDef transparentBox fill:none,stroke:white,stroke-width:3px,font-size:24px;

    class A transparentBox;
    class B transparentBox;
    class C transparentBox;

```
</div>

---
hideInToc: true
layout: center
---

<img src="/hdd.png" class="w-auto">

---
hideInToc: true
layout: image
image: /hdd_schematic.png
backgroundSize: contain
---

---
hideInToc: true
layout: image
image: /hdd_magnetic_domains.png
backgroundSize: contain
---

---
hideInToc: true
layout: center
---

<img src="/ssd.png" class="w-auto">

---
hideInToc: true
layout: center
---

<img src="/nvme.png" class="w-auto">

---
hideInToc: true
layout: image
image: /ssd_floating_gate_3d.webp
backgroundSize: contain
---

---
hideInToc: true
layout: image
image: /ssd_floating_gate.png
backgroundSize: contain
---

---
hideInToc: true
layout: section
---

# Input/Output (**I/O**) Devices

---
hideInToc: true
---

- # Specialized **Processors**:

  - ## **GPU** (Graphics Processing Unit)

  - ## **TPU** (Tensor Processing Unit)

  - ## **FPGA** (Field-Programmable Gate Array)

  - ## **ASIC** (Application-Specific Integrated Circuit)

---
hideInToc: true
---

- # **GPU** (Graphics Processing Unit)

  - ## Graphics Rendering

  - ## Parallel Processing Power

  - ## Accelerating Machine Learning and AI

  - ## Scientific and Data Analysis Computing

  - ## Video Processing and Encoding

---
hideInToc: true
layout: center
---

<img src="/gpu1.webp" class="w-auto">

---
hideInToc: true
layout: image
image: https://cdn.mos.cms.futurecdn.net/xd2Hw9Cki3qhzbC2WxNBcA.jpg
---

---
hideInToc: true
layout: full
---

<div class="absolute inset-0 p-0 m-0">
  <iframe
    src="https://www.youtube.com/embed/1vXFxEzozcE?si=E6BKmW_vWHg0F0Pi&rel=0"
    class="w-full h-full"
    style="border:0;"
    allow="fullscreen"
    allowfullscreen>
  </iframe>
</div>



---
hideInToc: true
---

- # Power and Cooling

- # Networking

- # Monitoring and Management Tools

---
hideInToc: true
---

- # Security

- # Software

- # Virtualization and Cloud Computing

---
hideInToc: true
---

- # **Software** Components

  - ## Operating Systems (**OS**)

    - ### Windows

    - ### macOS

    - ### Linux

  - ## **Middleware** and Virtualization

  - ## **Application** Software

---
layout: section
hideInToc: true
---

# Memory Hierarchy
    A[CPU Registers<br/>~1 cycle<br/>Few KB] 
    B[L1 Cache<br/>~3 cycles<br/>32-64 KB]
    C[L2 Cache<br/>~10 cycles<br/>256 KB - 1 MB]
    D[L3 Cache<br/>~40 cycles<br/>8-32 MB]
    E[RAM<br/>~100-300 cycles<br/>4-32 GB]
    F[SSD<br/>~100,000 cycles<br/>256 GB - 4 TB]
    G[HDD<br/>~10,000,000 cycles<br/>1-10 TB]

---
hideInToc: true
---

# The Memory Pyramid


<div style="text-align: center;">

```mermaid
graph LR
    A[CPU Registers<br/>~1 cycle<br/>Few KB] --> 
    B[L1 Cache<br/>~3 cycles<br/>32-64 KB] -->
    C[L2 Cache<br/>~10 cycles<br/>256 KB - 1 MB] -->
    D[L3 Cache<br/>~40 cycles<br/>8-32 MB]    

    classDef box fill:none,stroke:white,stroke-width:3px,font-size:24px;

    class A box;
    class B box;
    class C box;
    class D box;
```

```mermaid {scale: 1}
graph LR
    E[RAM<br/>~100-300 cycles<br/>4-32 GB] -->
    F[SSD<br/>~100,000 cycles<br/>256 GB - 4 TB] -->
    G[HDD<br/>~10M cycles<br/>1-10 TB] 

    classDef box fill:none,stroke:white,stroke-width:3px,font-size:24px;

    class E box;
    class F box;
    class G box;

```

</div>

---
hideInToc: true
---

# Memory Access Times

| **Storage Type** | **Access Time** | **Relative Cost** |
|------------------|-----------------|-------------------|
| CPU Register     | 1 ns            | 1x                |
| L1 Cache         | 2-4 ns          | 2-4x              |
| L2 Cache         | 10-20 ns        | 10-20x            |
| RAM              | 100-300 ns      | 100-300x          |
| SSD              | 100 μs          | 100,000x          |
| HDD              | 10 ms           | 10,000,000x       |

---
hideInToc: true
---

# Why This Matters for Data Analysis

- ## **Locality matters**: Keep related data close together

- ## **Vectorization**: Process arrays in chunks that fit in cache

- ## **File formats**: Columnar formats (Parquet) are cache-friendly

- ## **Algorithm choice**: Memory access patterns affect performance more than computation

---
hideInToc: true
layout: full
---

<div class="absolute inset-0 p-0 m-0">
  <iframe
    src="https://www.youtube.com/embed/h9Z4oGN89MU?si=238qvmSpbhkseW2I"
    class="w-full h-full"
    style="border:0;"
    allow="fullscreen"
    allowfullscreen>
  </iframe>
</div>
