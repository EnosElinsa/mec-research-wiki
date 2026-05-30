---
type: source
title: "Joint Computation Offloading and Resource Allocation for Maritime MEC With Energy Harvesting"
authors: ["Zhen Wang", "Bin Lin", "Qiang Ye", "Yuguang Fang", "Xiaoling Han"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2024.3371049"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, maritime-mec, energy-harvesting, lyapunov-optimization, computation-offloading, resource-allocation, throughput-maximization]
related:
  - "[[maritime-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[energy-harvesting-mec]]"
  - "[[task-offloading]]"
  - "[[task-migration]]"
  - "[[zhang-2025-three-tier-maritime-offloading]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[dai-2023-hybrid-marine-mmwl]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
created: 2026-05-31
updated: 2026-05-31
---

# Joint Computation Offloading and Resource Allocation for Maritime MEC With Energy Harvesting

## Citation

Wang, Z., Lin, B., Ye, Q., Fang, Y., & Han, X. (2024). *Joint Computation Offloading and Resource Allocation for Maritime MEC With Energy Harvesting*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2024.3371049.

## TL;DR

An **MEC-enabled sea lane monitoring network (MSLMN)** with **energy harvesting (EH)** where green-energy-powered maritime information stations (MISs) serve sailing terminal units (TUs/vessels). It maximizes the **long-term average throughput** under **queue stability** and **energy consumption** constraints by jointly optimizing task offloading, subchannel allocation, computing-resource allocation, and task migration. Formulated as a stochastic program, solved via **Lyapunov optimization** (drift-plus-penalty) decoupled into independent low-complexity subproblems; the resulting algorithm is **JCORA**.

## Problem framing

Maritime services (sea lane monitoring, dynamic ship tracking, accident forensics, anti-fouling) generate compute-intensive, latency-sensitive image/video tasks on vessels with limited onboard compute. Terrestrial resources rarely reach the sea, and offshore maritime infrastructure is hard to connect to the power grid — so the paper powers edge servers with harvested solar + ocean-wave energy. The challenge: under time-varying channels, vessel mobility, random task arrivals, and uncertain harvested energy, schedule tasks and allocate resources to keep queues stable and energy within budget while maximizing throughput.

## System model

- **Two-tier architecture.** Tier 1: a single **coastal base station (CBS)**-centred macrocell along the coastline, backed by a main server with abundant compute. Tier 2: a set of **maritime information stations (MISs)** — e.g. green-energy-powered intelligent buoys with local MEC servers — anchored along sea lanes, each serving **terminal units (TUs)** such as vessels under its coverage.
- **Links.** CBS↔MIS over LTE; MIS↔TU over WiFi. When an MIS's compute/energy is insufficient, tasks are **migrated to the CBS/main server** for processing ([[task-migration]]).
- **Energy.** Each MIS harvests **solar + ocean-wave** energy (WECs + solar panels) — a renewable [[energy-harvesting-mec]] design, distinct from RF harvesting.
- **Objective.** Maximize the long-term average network throughput subject to per-queue stability (task transmission + processing buffers) and an energy budget.

## Method

- Formulate a **stochastic optimization** problem over two timescales (large interval for reservation, small slots for decisions).
- Apply **[[lyapunov-optimization]]** to convert the long-term problem into a per-slot **drift-plus-penalty** minimization, removing the need to predict future channel/energy/task dynamics.
- Decompose the per-slot upper bound into **independent subproblems** (offloading, subchannel allocation, computing-resource allocation, task migration) solved in a distributed manner → the **JCORA** algorithm.
- A performance analysis establishes an **[O(1/V), O(V)]** tradeoff between average throughput and queue backlog (Theorem 2), i.e. asymptotic optimality as the Lyapunov weight V grows.

## Key findings

- JCORA achieves **higher average throughput and lower average latency** than four benchmarks — FIFO-based (FRA), latency-based (LRA), priority-based (PRA), and TDMA-based (TRA) resource allocation — across number of TUs, task arrival rate, and maximal energy charging rate (the paper's stated comparisons; specific curves are read from Figs. 7–12, reported here qualitatively).
- Larger maximal energy charging rate raises throughput and lowers latency, since more harvested energy lets MISs process more tasks faster.

## Limitations / future work

Simulation-based, low-vessel-mobility assumption. Future work (stated): resource allocation and offloading for more complex/dynamic marine scenarios (e.g. environment monitoring) using **machine learning (e.g. DRL)** for decision-making.

## Relation to the corpus

A **maritime MEC** entry whose distinguishing feature is **renewable energy harvesting** powering the edge tier — complementing the LEO+OBS three-tier MINLP scheme of [[zhang-2025-three-tier-maritime-offloading]] and the UAV+LEO double-edge scheme of [[wang-2025-double-edge-samin]]. Methodologically it sits in the **Lyapunov-online** family alongside [[zhu-2025-lycnn-drl-wpt-mec]]. Shares Dalian-Maritime-University co-authors Bin Lin and lead author Zhen Wang with the maritime cluster, and co-author Qiang Ye (University of Calgary). Bin Lin also co-authors the within-batch marine paper [[dai-2023-hybrid-marine-mmwl]]. Anchors the new [[energy-harvesting-mec]] concept.

## Raw artifacts

- `raw/sources/Joint_Computation_Offloading_and_Resource_Allocation_for_Maritime_MEC_With_Energy_Harvesting/full.md`
- Original PDF and extracted figures in the same folder.
