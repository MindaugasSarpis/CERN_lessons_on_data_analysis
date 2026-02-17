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

# Data analysis and Artificial Intelligence

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

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-primary pad-compact" style="background: rgba(0,0,0,0.7);">

A modern multi-core CPU die — the complex circuitry visible on the silicon wafer integrates billions of transistors for processing, cache, and I/O.

</div>
</div>

---
hideInToc: true
layout: image
image: /cpu2.jpg
---

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-primary pad-compact" style="background: rgba(0,0,0,0.7);">

Close-up of a CPU package mounted on a motherboard. The metal heat spreader covers the silicon die and conducts heat to the cooler above.

</div>
</div>

---
hideInToc: true
layout: image
image: /cpu_apple_M4.webp
---

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-primary pad-compact" style="background: rgba(0,0,0,0.7);">

Apple M4 system-on-chip (SoC) — integrates CPU, GPU, Neural Engine, and unified memory on a single die for maximum efficiency.

</div>
</div>

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

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-secondary pad-compact" style="background: rgba(0,0,0,0.7);">

Desktop RAM modules (DIMMs) — each stick contains multiple memory chips that provide fast, volatile storage for active programs and data.

</div>
</div>

---
hideInToc: true
layout: image
image: https://www.pcworld.com/wp-content/uploads/2023/04/corsair-dominator-memory-100884308-orig-1.jpg?quality=50&strip=all
---

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-secondary pad-compact" style="background: rgba(0,0,0,0.7);">

High-performance DDR memory with heat spreaders. Overclocking-grade RAM uses custom PCB designs and binned chips for higher clock speeds.

</div>
</div>

---
hideInToc: true
layout: center
---

<img src="/laptop_ram.png" class="w-auto">

<div class="card card-secondary pad-compact mt-md">

Laptop SO-DIMM RAM modules — smaller form factor than desktop DIMMs, but same underlying technology. Often soldered directly onto the motherboard in modern ultrabooks.

</div>

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

```mermaid {scale: 1.0}
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

<div class="card card-accent pad-compact mt-md">

Inside a hard disk drive (HDD) — spinning magnetic platters with a read/write head on an actuator arm. Typical speeds are 5400-7200 RPM.

</div>

---
hideInToc: true
layout: image
image: /hdd_schematic.png
backgroundSize: contain
---

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-accent pad-compact" style="background: rgba(0,0,0,0.7);">

HDD schematic — data is stored in concentric tracks on the platter surface. The actuator arm positions the head over the correct track to read or write data.

</div>
</div>

---
hideInToc: true
layout: image
image: /hdd_magnetic_domains.png
backgroundSize: contain
---

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-accent pad-compact" style="background: rgba(0,0,0,0.7);">

Magnetic domains on an HDD platter — each bit is stored as the orientation of a tiny magnetic region. Smaller domains allow higher storage density.

</div>
</div>

---
hideInToc: true
layout: center
---

<img src="/ssd.png" class="w-auto">

<div class="card card-accent pad-compact mt-md">

A solid-state drive (SSD) in the standard 2.5-inch form factor. No moving parts means faster access, lower latency, and better shock resistance than HDDs.

</div>

---
hideInToc: true
layout: center
---

<img src="/nvme.png" class="w-auto">

<div class="card card-accent pad-compact mt-md">

An NVMe M.2 drive — connects directly to the PCIe bus, bypassing the slower SATA interface. Sequential read speeds can exceed 7 GB/s on modern drives.

</div>

---
hideInToc: true
layout: image
image: /ssd_floating_gate_3d.webp
backgroundSize: contain
---

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-accent pad-compact" style="background: rgba(0,0,0,0.7);">

3D NAND flash architecture — memory cells are stacked vertically in layers, dramatically increasing storage density without shrinking individual cell sizes.

</div>
</div>

---
hideInToc: true
layout: image
image: /ssd_floating_gate.png
backgroundSize: contain
---

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-accent pad-compact" style="background: rgba(0,0,0,0.7);">

Floating gate transistor — the core storage mechanism of flash memory. Electrons trapped on the floating gate change the transistor's threshold voltage to represent 0 or 1.

</div>
</div>

---
hideInToc: true
layout: section
---

# Input/Output (I/O) **Devices**

---
hideInToc: true
---

# Input/Output (I/O) Devices

<div class="grid-2 mt-md gap-md">

<div class="card card-primary pad-tight">

## 🔌 **What Is I/O?**

Any transfer of data **into** or **out of** the CPU — reading files from disk, receiving network packets, or sending output to a display.

</div>

<div class="card card-secondary pad-tight">

## 🚌 **Common I/O Interfaces**

- **PCIe** — high-speed internal bus (GPUs, NVMe, network cards)
- **USB** — universal external connectivity
- **SATA** — storage device interface
- **Ethernet / InfiniBand** — network data transfer

</div>

<div class="card card-accent pad-tight">

## 🚧 **The I/O Bottleneck**

I/O is typically the **slowest link** in the data pipeline. A fast CPU waiting on a slow disk read is effectively idle — this is why SSDs, caching, and async I/O matter.

</div>

<div class="card card-info pad-tight">

## 📊 **Why It Matters for Analysis**

Reading a large dataset from disk or over a network often dominates total runtime. Choosing the right storage, format, and access pattern can cut I/O time by orders of magnitude.

</div>

</div>

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

<div class="card card-primary pad-compact mt-md">

A modern GPU board — the large die under the cooler contains thousands of parallel cores designed for high-throughput computation.

</div>

---
hideInToc: true
layout: image
image: https://cdn.mos.cms.futurecdn.net/xd2Hw9Cki3qhzbC2WxNBcA.jpg
---

<div class="absolute bottom-4 left-4 right-4">
<div class="card card-primary pad-compact" style="background: rgba(0,0,0,0.7);">

GPU die shot — the highly regular grid pattern reflects the SIMD architecture: thousands of identical cores executing the same instruction on different data in parallel.

</div>
</div>

---
hideInToc: true
---

# CPU vs GPU — Visualized

<div class="card card-info pad-compact mt-md">

## 🎬 **Video: Mythbusters Demo — CPU vs GPU**

A visual demonstration of serial vs. parallel processing. The CPU paints one pixel at a time, while the GPU paints thousands simultaneously — illustrating why GPUs excel at data-parallel workloads.

</div>

<div class="mt-md" style="text-align: center;">
  <iframe
    src="https://www.youtube.com/embed/1vXFxEzozcE?si=E6BKmW_vWHg0F0Pi&rel=0"
    width="720" height="340"
    style="border:0; border-radius: 8px;"
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
---

# How Computer Memory Works

<div class="card card-info pad-compact mt-md">

## 🎬 **Video: How Computer Memory Works — TED-Ed**

An animated explanation of the memory hierarchy — from CPU registers to hard drives — and why balancing speed, size, and cost shapes every computer system.

</div>

<div class="mt-md" style="text-align: center;">
  <iframe
    src="https://www.youtube.com/embed/h9Z4oGN89MU?si=238qvmSpbhkseW2I"
    width="720" height="340"
    style="border:0; border-radius: 8px;"
    allow="fullscreen"
    allowfullscreen>
  </iframe>
</div>
