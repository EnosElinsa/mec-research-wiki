---
type: source
title: "ARIS-Aided Multi-UAV-Enabled V2X Communication and Computation: Resource Allocation and Performance Optimization"
authors: ["Jun Cui", "Shubin Wang", "Gerile Ge", "Xiaolong Wu", "Xueyan Cao"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3682488"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-mec, v2x, active-ris, uav-computation, resource-allocation, energy-efficiency]
related:
  - "[[effective-energy-efficiency]]"
  - "[[active-ris]]"
  - "[[vehicular-mec]]"
  - "[[task-offloading]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[integrated-sensing-computation-communication]]"
created: 2026-07-10
updated: 2026-07-10
---

# ARIS-Aided Multi-UAV-Enabled V2X Communication and Computation: Resource Allocation and Performance Optimization

## Citation

Cui, J., Wang, S., Ge, G., Wu, X., & Cao, X. (2026). *ARIS-Aided Multi-UAV-Enabled V2X Communication and Computation: Resource Allocation and Performance Optimization*. **IEEE Transactions on Mobile Computing**, 1-14. DOI: 10.1109/TMC.2026.3682488.

## TL;DR

Builds an active-RIS-aided multi-UAV V2X integrated communication and computation system and optimizes a new effective-energy-efficiency objective over associations, ARIS coefficients, multi-antenna beamforming, task offloading, transmit power, and computation resources. The ECCRA algorithm uses BCD with Dinkelbach transformation, first-order Taylor approximation, convex optimization, and integer programming substeps.

## Problem

V2X communication and computation face LoS blockage, propagation loss, latency, and energy pressure. UAVs can provide flexible communication/computation support, while active RISs can amplify reflected links, but jointly tuning V2V communication, V2U/V2B offloading, ARIS association, vehicle scheduling, beamforming, and computation allocation produces a high-dimensional non-convex resource-allocation problem.

## System model

- One M-antenna BS, K M-antenna UAVs, L single-antenna vehicles, and Q ARISs with N active reflecting elements.
- Vehicles have communication and offloading-computation functions.
- V2U/V2B offloading links share the V2V band, while OFDM separates V2I offloading links.
- Vehicle mobility is quasi-static within a coherent block.
- ARIS elements actively tune both phase and amplitude, with amplifier noise and ARIS power consumption modeled.

## Method

- Defines [[effective-energy-efficiency]] to jointly represent communication utility, computation utility, and network energy cost.
- Maximizes that metric under UAV/BS/ARIS/vehicle power budgets, multiplexing, scheduling, ARIS association, task-offloading-ratio, latency, and computation-capacity constraints.
- Applies Dinkelbach's algorithm to handle the fractional objective.
- Decomposes the problem into multiple-association, joint beamforming, and computation-resource subproblems inside a BCD framework.
- Uses convex optimization, integer programming, and first-order Taylor approximations to solve the subproblems.

## Key findings

- The proposed ECCRA scheme converges to higher effective energy efficiency than no-ARIS, passive-RIS, random-ARIS, and MRT-style baselines in the reported simulations.
- With random frequency multiplexing and association baselines, the proposed scheme stabilizes after about four iterations and reaches an energy-efficiency value of 175.9 in the parsed figure discussion.
- The proposed scheme consumes less energy than the offloading-computation-only scheme because it balances local and offloaded computation.
- Energy efficiency increases with the number of active reflecting elements and UAV/BS antennas, and the optimized ARIS/association choices widen the gap from random baselines as N grows.
- Increasing vehicle-to-ARIS distance degrades performance; the paper notes that higher vehicle power or more active reflecting elements can compensate.

## Limitations / future work

The parse presents simulation-based results for a small urban setup with two UAVs, two ARISs, and five vehicles. It does not report hardware validation, online mobility adaptation across blocks, or robustness to imperfect ARIS/UAV channel estimates beyond the simulated model.

## Relation to the corpus

This source extends [[vehicular-mec]] and [[active-ris]] toward integrated V2X communication/computation rather than pure offloading. Its solver stack reuses the corpus's [[fractional-programming-dinkelbach]] and [[alternating-optimization-sdr-sca]] vocabulary, while the metric page [[effective-energy-efficiency]] captures the paper's combined communication/computation/energy objective.

## Raw artifacts

- `raw/sources/ARIS-Aided_Multi-UAV-Enabled_V2X_Communication_and_Computation_Resource_Allocation_and_Performance_Optimization/ARIS-Aided_Multi-UAV-Enabled_V2X_Communication_and_Computation_Resource_Allocation_and_Performance_Optimization.md`
- `raw/sources/ARIS-Aided_Multi-UAV-Enabled_V2X_Communication_and_Computation_Resource_Allocation_and_Performance_Optimization/ARIS-Aided_Multi-UAV-Enabled_V2X_Communication_and_Computation_Resource_Allocation_and_Performance_Optimization.pdf`
- Extracted figures in `raw/sources/ARIS-Aided_Multi-UAV-Enabled_V2X_Communication_and_Computation_Resource_Allocation_and_Performance_Optimization/images/`
