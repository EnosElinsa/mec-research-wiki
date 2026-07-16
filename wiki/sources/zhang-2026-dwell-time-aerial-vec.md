---
type: source
modeling_card: required
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
updated: 2026-07-16
---

# Dwell-Time-Constrained Joint Task Offloading and Resource Allocation for Multi-Layer Aerial Vehicular Edge Computing Networks

## Citation

Zhang, Y., Na, Z., Jiang, L., Nallanathan, A., & Liu, X. (2026). *Dwell-Time-Constrained Joint Task Offloading and Resource Allocation for Multi-Layer Aerial Vehicular Edge Computing Networks*. **IEEE Transactions on Intelligent Transportation Systems**. DOI: 10.1109/TITS.2026.3692669.

## TL;DR

Models a **multi-layer aerial vehicular edge computing** network where high-speed vehicles offload tasks either to UAVs or to a HAP. The key modeling addition is a **dwell-time constraint**: a vehicle can use a UAV only if the task can finish before the vehicle exits the UAV coverage region. The resulting mixed-integer resource-allocation problem minimizes weighted latency-plus-economic cost and is solved by a block-coordinate decomposition with Lagrangian duality, linear relaxation, and ADMM-style resource allocation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Vehicles on a bidirectional highway fully offload computation tasks to either a rotary-wing UAV for proximity service or a HAP for wide-area service. The two aerial tiers have heterogeneous coverage, bandwidth, computation capacity, and leasing prices, while UAV service must finish within each vehicle's mobility-dependent dwell time.

**Problem & objective**: Problem P1 is a mixed-integer nonlinear program that minimizes the aggregate weighted latency and leasing expenditure, $\min_{\alpha,\beta,f,\psi,\varpi}\sum_{k=1}^{K} C_k$ with $C_k=\omega_1T_k^{\mathrm{tot}}+\omega_2P_k^{\mathrm{tot}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV offloading decision | $\psi_{k,\mathrm U}$ | binary | Whether vehicle $k$ offloads to the UAV |
| HAP offloading decision | $\varpi_{k,\mathrm H}$ | binary | Whether vehicle $k$ offloads to the HAP |
| Bandwidth fractions | $\alpha_{k,\mathrm U},\beta_{k,\mathrm H}$ | continuous, $[0,1]$ | Fractions of UAV and HAP bandwidth assigned to vehicle $k$ |
| Computation resources | $f_{k,\mathrm U},f_{k,\mathrm H}$ | continuous, nonnegative | CPU resources allocated by the selected aerial platform |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C2 | Each task selects exactly one tier, $\psi_{k,\mathrm U}+\varpi_{k,\mathrm H}=1$, with binary decisions |
| C3 | UAV transmission plus execution must fit the contact interval, $\psi_{k,\mathrm U}(t_{k,\mathrm U}^{\mathrm{tr}}+t_{k,\mathrm U}^{\mathrm{exe}})\le T_{k,\mathrm U}^{\mathrm{dwell}}$ |
| C4-C7 | Allocated UAV and HAP bandwidth fractions are nonnegative and sum to at most one per tier |
| C8-C10 | Allocated CPU resources are nonnegative and remain within UAV and HAP computation capacities |
| C11 | The UAV serves no more than $N_{\max}$ concurrent vehicles |
| C12-C13 | Vehicle transmission energy and UAV execution plus hovering energy remain within their residual budgets |

**Algorithm**: Apply block coordinate descent → solve bandwidth allocation through Lagrangian dual updates → solve computation allocation as a convex program → relax and update offloading decisions with ADMM → repeat the three blocks until the relative cost change meets the tolerance.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied joint task offloading and resource allocation in a multi-layer aerial vehicular edge computing network integrating a HAP and multiple UAVs. They formulated a mixed-integer nonlinear programming problem that minimizes a weighted combination of task latency and leasing expenditure while enforcing a dwell-time feasibility constraint for UAV-assisted offloading. Their block coordinate descent algorithm decomposes bandwidth, computation-resource, and offloading decisions and applies Lagrangian duality, convex optimization, linear relaxation, and ADMM. When the UAV dwell-time constraint cannot be satisfied, the hierarchical service mechanism redirects the task to the HAP. Simulations report total-cost reductions of 8.26% to 58.11% relative to the evaluated benchmark strategies, with the reported gains being especially visible under high vehicle mobility.

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

- `raw/sources/Dwell-Time-Constrained_Joint_Task_Offloading_and_Resource_Allocation_for_Multi-Layer_Aerial_Vehicular_Edge_Computing_Networks/Dwell-Time-Constrained_Joint_Task_Offloading_and_Resource_Allocation_for_Multi-Layer_Aerial_Vehicular_Edge_Computing_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
