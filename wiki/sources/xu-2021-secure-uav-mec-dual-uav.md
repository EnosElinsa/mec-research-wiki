---
type: source
title: "Joint Resource and Trajectory Optimization for Security in UAV-Assisted MEC Systems"
authors: ["Yu Xu", "Tiankui Zhang", "Dingcheng Yang", "Yuanwei Liu", "Meixia Tao"]
year: 2021
url: "https://doi.org/10.1109/TCOMM.2020.3025910"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
tags: [source, uav-mec, physical-layer-security, noma, trajectory-optimization, resource-allocation, secure-computing-capacity]
related:
  - "[[secure-computation-efficiency]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[michailidis-2024-secure-ris-uav-mec-iot]]"
created: 2026-06-04
updated: 2026-06-09
---

# Joint Resource and Trajectory Optimization for Security in UAV-Assisted MEC Systems

## Citation

Xu, Y., Zhang, T., Yang, D., Liu, Y., & Tao, M. (2021). *Joint Resource and Trajectory Optimization for Security in UAV-Assisted MEC Systems*. **IEEE Transactions on Communications**, 69(1). DOI: 10.1109/TCOMM.2020.3025910. (Received 11 March 2020; accepted 14 September 2020; published 22 September 2020; current version 15 January 2021.)

## TL;DR

Studies a **dual-UAV** MEC security framework: one UAV serves as an aerial MEC server (computes offloaded tasks from ground terminals); the other UAV acts as a **cooperative jammer** to suppress eavesdroppers. Formulates **minimum secure computing capacity maximization** (average achievable secure computing bits per period) problems for both TDMA and NOMA, jointly optimizing communication resources, computation resources, and both UAVs' trajectories. Proposes BCD-based and penalized-BCD algorithms for the two schemes. Claims to be the first work using secure computing capacity as the PLS performance metric in UAV-MEC. Finding: NOMA is superior to TDMA for security.

## Problem framing

UAV-MEC's LoS channels between UAV and ground are also LoS to potential eavesdroppers — a fundamental security vulnerability. A cooperative jammer UAV transmits noise toward eavesdroppers while the server UAV handles computation, exploiting trajectory design to keep the jamming effective and the serving link strong. The secure computing capacity metric captures both the computation benefit (bits processed) and the secrecy benefit (capacity minus eavesdropper capacity) jointly.

## System model

- **K ground terminal devices (TDs)** with partial offloading; **multiple eavesdroppers** on the ground.
- **Server UAV:** collects and computes offloaded task bits from TDs via uplink (TDMA or NOMA).
- **Jammer UAV:** transmits artificial noise to degrade eavesdroppers' SINR.
- **Secure computing capacity:** average achievable secure computing bits = f(server UAV channel to TDs, jammer UAV channel to eavesdroppers, compute resource allocation, trajectory).
- **TDMA scheme:** BCD-based algorithm (SCA + SOC for non-convex constraints).
- **NOMA scheme:** P-BCD algorithm (additional binary constraints for SIC decoding order).
- **Objective:** maximize min secure computing capacity over all TDs.

## Key findings

- NOMA scheme achieves **higher minimum secure computing capacity** than TDMA (parse contribution bullets + Section V results).
- Partial offloading (vs. binary or full offloading) achieves the largest objective values (parse results discussion).
- Proposed BCD/P-BCD algorithms improve security performance over benchmarks (static UAV, no jammer, equal resource allocation) in simulations (parse abstract + Section V).
- Trajectory co-design of both UAVs (server + jammer) is essential — fixed-trajectory or single-UAV baselines perform significantly worse.

## Limitations / future work

Parse does not provide explicit numerical gain figures; references simulation figures. Requires two UAVs (hardware complexity + coordination overhead). Eavesdropper channel knowledge assumed at the server UAV for SIC in NOMA scheme.

## Relation to the corpus

Provides the **secure computing capacity** metric definition for UAV-MEC PLS — complementing [[michailidis-2024-secure-ris-uav-mec-iot]] (secure computation efficiency with RIS) and [[benaya-2025-aerial-isac-haps]] (HAPS-based PLS). The dual-UAV architecture (server + jammer) is distinct from single-UAV MEC papers in the corpus.

## Raw artifacts

- Parse: `raw/sources/Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems/full.md`
- Origin PDF: `raw/sources/Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems/4a0aaa0c-101c-4198-9c6f-efa42d18c909_origin.pdf`
- Figures: `raw/sources/Joint_Resource_and_Trajectory_Optimization_for_Security_in_UAV-Assisted_MEC_Systems/images/`
