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

## Computing Infrastructure

---
hideInToc: true
layout: quote
---

# Every data analysis depends on the hardware beneath it. Understanding **CPUs**, **memory**, **storage**, and **accelerators** helps you write faster code, choose the right tools, and make the most of the machines you work with.

---
layout: fact
hideInToc: true
---

#  What constitutes **computing infrastructure**?

---
hideInToc: true
---

# Hardware Components

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🖥️ **Core Processing**

- Central Processing Unit (**CPU**)
- Specialized Processors (**GPUs**, **TPUs**)

</div>

<div class="card card-secondary pad-tight">

## 💾 **Memory & Storage**

- Memory (**RAM**)
- Storage Devices (**HDD, SSD, NVMe**)

</div>

<div class="card card-accent pad-tight">

## 🔌 **I/O & Connectivity**

- Input/Output (**I/O**) Devices
- Networking

</div>

<div class="card card-info pad-tight">

## ⚡ **Infrastructure**

- Power and Cooling
- Monitoring and Management Tools

</div>

<div class="card card-warning pad-tight">

## 🔒 **Security**

- Physical and logical security
- Access control

</div>

</div>

---
hideInToc: true
---

# CPU (Central Processing Unit)

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🧠 **What It Does**

Basic arithmetic, logic, control, and input/output operations

</div>

<div class="card card-secondary pad-tight">

## 🔧 **CPU Sub-Components**

<div class="stack-tight">

<div class="card card-info pad-compact">⚙️ **Control Unit (CU)** — directs operations</div>

<div class="card card-accent pad-compact">➕ **Arithmetic Logic Unit (ALU)** — math & logic</div>

<div class="card card-success pad-compact">📋 **Registers** — fastest storage</div>

<div class="card card-warning pad-compact">💨 **Cache** — near-CPU memory</div>

<div class="card card-primary pad-compact">🔀 **Buses** — data pathways</div>

</div>

</div>

</div>

---
hideInToc: true
---

# CPU Performance Factors

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## ⏱️ **Clock Speed**

How many cycles per second the CPU can execute (measured in GHz)

</div>

<div class="card card-secondary pad-tight">

## 🔢 **Number of Cores**

More cores enable parallel execution of independent tasks

</div>

<div class="card card-info pad-tight">

## 💨 **Cache Size**

Larger caches reduce memory access latency for frequently used data

</div>

<div class="card card-accent pad-tight">

## 🔋 **Power Efficiency**

Performance per watt matters for sustained workloads and cooling

</div>

</div>

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

# RAM (Random Access Memory)

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📝 **Characteristics**

- **Volatile memory** — data lost on power-off
- **High-Speed Access** — orders of magnitude faster than disk
- **Temporary Storage** — working space for active processes

</div>

<div class="card card-secondary pad-tight">

## 📊 **Specifications**

- **Capacity** — measured in GB or TB
- **Performance** — measured in MHz or GHz
- Determines how much data can be processed simultaneously

</div>

</div>

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

# Storage Devices

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 💿 **Mechanical**

- **HDD** (Hard Disk Drive) — spinning platters, high capacity, slower

</div>

<div class="card card-secondary pad-tight">

## ⚡ **Solid State**

- **SSD** (Solid State Drive) — flash memory, faster, no moving parts
- **SSHD** (Solid State Hybrid Drive) — combines HDD + flash cache

</div>

<div class="card card-accent pad-tight" style="grid-column: 1 / -1;">

## 🚀 **NVMe** (Non-Volatile Memory Express)

Direct PCIe connection — fastest consumer storage available

</div>

</div>

<div style="margin-top: 2rem; text-align: center;">

```mermaid {scale: 1.5}
graph LR
    A[Caches] --> B[RAM] --> C[Drive Storage]

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

# Input/Output (I/O) **Devices**

---
hideInToc: true
---

# Specialized Processors

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🎮 **GPU** (Graphics Processing Unit)

Massively parallel — thousands of small cores for throughput

</div>

<div class="card card-secondary pad-tight">

## 🤖 **TPU** (Tensor Processing Unit)

Google-designed accelerator optimized for ML tensor operations

</div>

<div class="card card-accent pad-tight">

## 🔧 **FPGA** (Field-Programmable Gate Array)

Reconfigurable hardware — customizable logic for specific tasks

</div>

<div class="card card-info pad-tight">

## 🏭 **ASIC** (Application-Specific Integrated Circuit)

Fixed-function chip — maximum efficiency for a single task

</div>

</div>

---
hideInToc: true
---

# GPU (Graphics Processing Unit)

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🎯 **Primary Uses**

- Graphics Rendering
- Parallel Processing Power
- Video Processing and Encoding

</div>

<div class="card card-secondary pad-tight">

## 🔬 **Scientific Applications**

- Accelerating Machine Learning and AI
- Scientific and Data Analysis Computing
- Simulation and modelling

</div>

</div>

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

# Infrastructure & Operations

<div class="grid-3 mt-md gap-md">

<div class="card card-primary pad-tight">

## ⚡ **Power and Cooling**

Reliable power supply, UPS systems, and thermal management for sustained operation

</div>

<div class="card card-secondary pad-tight">

## 🌐 **Networking**

Interconnects, bandwidth, latency — moving data between components and systems

</div>

<div class="card card-info pad-tight">

## 📈 **Monitoring & Management**

System health, resource utilization, alerting, and capacity planning tools

</div>

</div>

---
hideInToc: true
---

# Security, Software & Cloud

<div class="grid-3 mt-md gap-md">

<div class="card card-warning pad-tight">

## 🔒 **Security**

Access control, encryption, firewalls, intrusion detection — protecting data and infrastructure

</div>

<div class="card card-accent pad-tight">

## 💻 **Software**

Operating systems, drivers, middleware, and application software that runs on the hardware

</div>

<div class="card card-success pad-tight">

## ☁️ **Virtualization & Cloud**

Abstract hardware into virtual machines and containers — scalable, on-demand resources

</div>

</div>

---
hideInToc: true
---

# Software Components

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🖥️ **Operating Systems**

<div class="stack-tight">

<div class="card card-info pad-compact">🪟 **Windows** — desktop, enterprise</div>

<div class="card card-accent pad-compact">🍎 **macOS** — Apple ecosystem</div>

<div class="card card-success pad-compact">🐧 **Linux** — servers, HPC, science</div>

</div>

</div>

<div class="card card-secondary pad-tight">

## 🔗 **Middleware & Applications**

- **Middleware** and Virtualization — bridges OS and applications
- **Application** Software — the tools you actually use for analysis

</div>

</div>

---
hideInToc: true
---

# The Memory Hierarchy

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

<div class="card card-info pad-tight mt-md">

## ⏱️ **Latency Comparison**

| **Storage Type** | **Access Time** | **Relative Cost** |
|------------------|-----------------|-------------------|
| CPU Register     | 1 ns            | 1x                |
| L1 Cache         | 2-4 ns          | 2-4x              |
| L2 Cache         | 10-20 ns        | 10-20x            |
| RAM              | 100-300 ns      | 100-300x          |
| SSD              | 100 μs          | 100,000x          |
| HDD              | 10 ms           | 10,000,000x       |

</div>

---
hideInToc: true
---

# Why This Matters for Data Analysis

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 📍 **Locality Matters**

Keep related data close together in memory — sequential access patterns are dramatically faster than random access

</div>

<div class="card card-secondary pad-tight">

## ⚡ **Vectorization**

Process arrays in chunks that fit in cache — SIMD instructions can operate on multiple data points simultaneously

</div>

<div class="card card-accent pad-tight">

## 📂 **File Formats**

Columnar formats (Parquet) are cache-friendly — read only the columns you need instead of entire rows

</div>

<div class="card card-warning pad-tight">

## 🧮 **Algorithm Choice**

Memory access patterns affect performance more than computation — an algorithm with better locality often beats a "faster" one

</div>

</div>

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
