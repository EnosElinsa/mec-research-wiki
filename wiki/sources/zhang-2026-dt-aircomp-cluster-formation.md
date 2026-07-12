---
type: source
title: "Digital-Twin-Empowered Cluster Formation via Over-the-Air Computation in UAV Swarm Networks"
authors: ["Lu Zhang", "Xuan Li", "Yuhang Zhang", "Yansong Huang", "Haiyan Li", "Zixuan Zhang", "Mugen Peng"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3646641"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, digital-twin, aircomp, uav-swarm, cluster-formation, energy-efficiency, bcd]
related:
  - "[[aircomp-aware-uav-device-cluster-formation]]"
  - "[[digital-twin]]"
  - "[[over-the-air-computation]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[autonomous-uav-swarms]]"
created: 2026-07-12
updated: 2026-07-12
---

# Digital-Twin-Empowered Cluster Formation via Over-the-Air Computation in UAV Swarm Networks

## Citation

Zhang, L., Li, X., Zhang, Y., Huang, Y., Li, H., Zhang, Z., & Peng, M. (2026). *Digital-Twin-Empowered Cluster Formation via Over-the-Air Computation in UAV Swarm Networks*. **IEEE Transactions on Wireless Communications**, 25, 9940-9954. DOI: 10.1109/TWC.2025.3646641.

## TL;DR

Uses a digital-twin control loop to jointly form UAV-to-IoE-device-group clusters, coordinate AirComp receiver scaling and device power, and plan collision-safe UAV trajectories. A four-block BCD solver maximizes aggregated data per UAV-plus-twin energy under AirComp distortion constraints.

## Problem

UAV swarms can aggregate measurements from groups of IoE devices through over-the-air superposition, but mobility, group assignment, coherent-signal distortion, device power, propulsion, and digital-twin update overhead are coupled. The resulting mixed-integer nonlinear fractional program must preserve aggregation quality while avoiding collisions and limiting energy use.

## System model

- Multiple fixed-altitude UAVs serve disjoint IoE device groups over time slots while a digital-twin layer receives delayed physical state and returns optimized policies.
- Devices in one selected group transmit simultaneously; the serving UAV computes an arithmetic average from their superposed signals.
- AirComp MSE includes signal misalignment, inter-cluster interference, and noise. Each selected group must stay below its distortion threshold.
- Binary association permits at most one serving UAV per group and at most one group per UAV in a slot.
- UAV energy follows a rotary-wing speed-dependent propulsion model. Digital-twin overhead grows with swarm/device scale and update frequency.
- Energy efficiency divides total aggregated transmission data by UAV propulsion energy plus twin-update overhead.

## Method

The GIO-BCD solver cycles through four blocks. UDCF-RLP relaxes binary UAV-group assignments and greedily recovers a feasible formation. FPO-ACSF applies [[fractional-programming-dinkelbach|Dinkelbach iteration]] to AirComp receiver scale factors. DB-DPA substitutes the square root of device power and solves another fractional program. SDB-USTD uses SCA/Taylor bounds plus an inner Dinkelbach loop for rate-to-propulsion trajectory design under movement, collision, and MSE constraints.

The objective sequence is argued to be non-decreasing and bounded. This establishes convergence of generated objective values, not global optimality for the original mixed-integer problem; assignment recovery and SCA remain approximation steps.

## Key findings

- At high device-power levels in the three-UAV setting, AirComp cluster formation reaches up to `6x` the throughput of orthogonal-transmission cluster formation.
- As device density varies, the proposed method reaches up to `6.2x` the energy efficiency of the orthogonal-transmission baseline.
- Against static pre-set AirComp, DT-CF-AirComp is reported about `42%` higher in energy efficiency and `34%` higher in throughput.
- DT-CF-OT is reported about `44%` higher in energy efficiency and `245%` higher in throughput than pre-set orthogonal transmission.
- The stated `10-15` global iterations and “few seconds” per cycle are algorithmic feasibility assertions; no processor or measured runtime trace is supplied.

## Limitations / parse caveats

Evaluation is simulation-only. The model assumes fixed altitude and device positions, LoS-dominant reciprocal channels, coherent transmission, perfect synchronization and Doppler compensation, independent normalized device signals, and straight-line motion inside each slot. Twin uncertainty is represented mainly through delayed state and update overhead rather than an explicit estimation-error constraint. The parse contains damaged set/time notation, shifted constraint labels, a missing equation body, and a table label inconsistent with the system definition. Publication metadata is absent from the parse and was verified through the exact-title Crossref record; technical claims come only from the parse.

## Relation to the corpus

[[aircomp-aware-uav-device-cluster-formation]] connects [[digital-twin]] synchronization to physical-layer [[over-the-air-computation]] and swarm mobility. It complements [[huang-2026-aircomp-uav-swarms-afl]], which aggregates learning updates under staleness, by optimizing IoE measurement aggregation and UAV propulsion energy with classical BCD/SCA rather than reinforcement learning.

## Raw artifacts

- Parse: `raw/sources/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks.md`
- Origin PDF: `raw/sources/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks.pdf`
- Figures: `raw/sources/Digital-Twin-Empowered_Cluster_Formation_via_Over-the-Air_Computation_in_UAV_Swarm_Networks/images/`
