---
type: source
title: "Dwell-Time-Constrained Joint Task Offloading and Resource Allocation for Multi-Layer Aerial Vehicular Edge Computing Networks"
authors: ["Yue Zhang", "Zhenyu Na", "Laiwei Jiang", "Arumugam Nallanathan", "Xin Liu"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3692669"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, vehicular-mec, aerial-vec, high-altitude-platform, uav-assisted-mec, dwell-time, task-offloading, resource-allocation, admm]
related:
  - "[[vehicular-mec]]"
  - "[[dwell-time-constrained-offloading]]"
  - "[[high-altitude-platform-station]]"
  - "[[task-offloading]]"
  - "[[alternating-direction-method-of-multipliers]]"
created: 2026-07-06
updated: 2026-07-06
---

# Dwell-Time-Constrained Joint Task Offloading and Resource Allocation for Multi-Layer Aerial Vehicular Edge Computing Networks

## Citation

Zhang, Y., Na, Z., Jiang, L., Nallanathan, A., & Liu, X. (2026). *Dwell-Time-Constrained Joint Task Offloading and Resource Allocation for Multi-Layer Aerial Vehicular Edge Computing Networks*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2026.3692669.

## TL;DR

Models a **multi-layer aerial vehicular edge computing** network where high-speed vehicles offload tasks either to UAVs or to a HAP. The key modeling addition is a **dwell-time constraint**: a vehicle can use a UAV only if the task can finish before the vehicle exits the UAV coverage region. The resulting mixed-integer resource-allocation problem minimizes weighted latency-plus-economic cost and is solved by a block-coordinate decomposition with Lagrangian duality, linear relaxation, and ADMM-style resource allocation.

## Problem

Roadside infrastructure can be sparse or overloaded, and UAVs offer low-latency proximity compute but only while vehicles remain inside their coverage. A HAP offers broader coverage but different delay and price tradeoffs. The paper targets joint offloading and resource allocation under high mobility, where ignoring dwell time can assign tasks to UAVs that cannot complete service before the vehicle leaves coverage.

## System model

- **Architecture.** A bidirectional highway is served by one HAP and multiple rotary-wing UAVs; the paper focuses on a representative UAV-covered segment.
- **Tasks.** Each vehicle task is fully offloaded either to a UAV or to the HAP. UAV service is subject to the vehicle's dwell time in the UAV coverage area.
- **Cost.** The objective is a weighted sum of task latency and economic expenditure, reflecting heterogeneous pricing and resource costs across the UAV and HAP layers.

## Method

The formulated mixed-integer nonlinear problem is decomposed with block-coordinate descent. The offloading block handles binary assignment under dwell-time feasibility; bandwidth and computation-resource blocks are solved with convex-optimization tools including Lagrangian duality, linear relaxation, and an ADMM-style iteration. The bandwidth solution has a water-filling interpretation: vehicles with higher latency weights, tighter dwell constraints, or stricter energy budgets receive more bandwidth.

## Key findings

- The contribution summary reports **8.26%-58.11% total-cost reductions** relative to benchmark schemes.
- The proposed scheme has the lowest reported cost across bandwidth, transmit-power, UAV-compute-capacity, computation-density, vehicle-speed, and UAV-energy-budget sweeps.
- Dwell-time-aware HAP fallback improves robustness at high vehicle speeds: when a task cannot satisfy the UAV dwell-time constraint, it can be redirected to the HAP instead of becoming infeasible.
- The iterative algorithm drops cost rapidly in early iterations and plateaus after about 7 iterations in the reported K = 60, data-size = 2 MB case; larger K converges more slowly.

## Limitations / future work

The conclusion points to multi-HAP/multi-UAV extensions with inter-cell interference and cooperative beamforming, DRL for real-time trajectory optimization and proactive slicing, and physical-layer security or ISAC integration.

## Relation to the corpus

This page extends [[vehicular-mec]] and the air-ground VEC line beyond static server selection: the coverage time of a moving vehicle becomes a hard feasibility condition. It is closely related to [[li-2024-airground-vec-offloading]] through HAP/UAV vehicular offloading, but it makes [[dwell-time-constrained-offloading]] the central constraint and treats the HAP as a fallback tier for high-mobility cases.

## Raw artifacts

- `raw/sources/Dwell-Time-Constrained Joint Task Offloading and Resource Allocation for Multi-Layer Aerial Vehicular Edge Computing Networks/Dwell-Time-Constrained Joint Task Offloading and Resource Allocation for Multi-Layer Aerial Vehicular Edge Computing Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
