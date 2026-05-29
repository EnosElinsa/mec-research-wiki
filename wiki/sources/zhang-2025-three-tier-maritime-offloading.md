---
type: source
title: "Energy Oriented Three-Tier Computation Offloading Scheme in Maritime Edge Computing Network"
authors: ["Hongxia Zhang", "Shiyu Xi", "Bodong Shang", "Peiying Zhang", "Sheng Wu", "Chunxiao Jiang"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3526213"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, leo-satellite-edge-computing, computation-offloading, minlp, three-tier, energy-efficiency]
related:
  - "[[maritime-mec]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[zhang-2024-dlrl-maritime-usv]]"
created: 2026-05-29
updated: 2026-05-29
---

# Energy Oriented Three-Tier Computation Offloading Scheme in Maritime Edge Computing Network

## Citation

Zhang, H., Xi, S., Shang, B., Zhang, P., Wu, S., & Jiang, C. (2025). *Energy Oriented Three-Tier Computation Offloading Scheme in Maritime Edge Computing Network*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3526213.

## TL;DR

A **three-tier maritime edge computing** system where a LEO satellite and an offshore base station (OBS) provide communication/computing to maritime wireless devices (MWDs). It minimizes system energy under latency constraints by optimizing association, task partitioning, transmission power, and computing-resource allocation. Formulated as a **MINLP**, decomposed into four sub-problems with tailored solvers. Reported headline result: **39.3% system-energy savings** versus benchmarks.

## Problem framing

Large-scale MWDs run computation-intensive, resource-sensitive maritime IoT tasks, but have limited compute and energy. A LEO+OBS three-tier architecture supplies offshore compute; the challenge is to transmit and process tasks energy-efficiently under deadlines.

## System model

- **Tiers.** MWDs (device) → OBS (edge) → LEO satellite, a maritime [[three-tier-cloud-edge-end]] structure.
- **Decision variables.** Association variable, task partitioning, transmission power, computing-resource allocation.
- **Objective.** Minimize system energy consumption subject to latency constraints — a non-convex [[mixed-integer-nonlinear-programming|MINLP]].

## Method

Decompose the MINLP into four sub-problems:
1. **Association** — slack-variable method → convex.
2. **Transmission power** (MWDs + LEO) — quadratic transformation + difference-of-convex algorithm.
3. **Task partitioning** — derive upper/lower bounds on offloaded task size, then standard convex method.
4. **Joint computing-resource allocation** (LEO + OBS) — Lagrangian dual + coordinate transformation.

An iterative algorithm jointly optimizes all four to minimize system energy.

## Key findings

- The proposed algorithm **saves 39.3% of system energy consumption** compared to benchmark schemes (the paper's stated headline number).

## Limitations / future work

Simulation-based. Future work: complexity analysis, scaling/deployment factors (e.g., spectrum resources), dynamic satellite-marine scenarios, and UAV-assisted maritime edge computing.

## Relation to the corpus

A **maritime MEC** entry that, unlike the double-edge UAV+LEO scheme of [[wang-2025-double-edge-samin]], uses a LEO+OBS three-tier architecture and a fully optimization-based MINLP decomposition. Complements the DRL maritime work [[zhang-2024-dlrl-maritime-usv]] and the HAP-UAV maritime IoT study [[liu-2025-haps-uav-maritime-iot]]. Shares co-author Chunxiao Jiang with several aerial/space sources. Reinforces [[mixed-integer-nonlinear-programming]] and [[three-tier-cloud-edge-end]].

## Raw artifacts

- `raw/sources/Energy_Oriented_Three-Tier_Computation_Offloading_Scheme_in_Maritime_Edge_Computing_Network/full.md`
- Original PDF and extracted figures in the same folder.
