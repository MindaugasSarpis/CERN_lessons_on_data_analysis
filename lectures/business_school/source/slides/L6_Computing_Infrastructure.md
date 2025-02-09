---
background: /intro_background.jpg

class: text-left
colorSchema: dark

theme: ./theme
drawings:
  persist: false

transition: fade

title: "Lecture 6: Computing Infrastructure"
layout: cover
---

# Dr. Mindaugas Šarpis

# Lessons on **Data Analysis** from **CERN**

## Lecture 6:

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
image: /cpu3.jpg
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

[press](https://www.youtube.com/watch?v=1vXFxEzozcE&ab_channel=NVIDIAGeForce)

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