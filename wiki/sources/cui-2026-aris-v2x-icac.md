---
type: source
title: "ARIS-Aided Multi-UAV-Enabled V2X Communication and Computation: Resource Allocation and Performance Optimization"
authors: ["Jun Cui", "Shubin Wang", "Gerile Ge", "Xiaolong Wu", "Xueyan Cao"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3682488"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
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
updated: 2026-07-16
---

# ARIS-Aided Multi-UAV-Enabled V2X Communication and Computation: Resource Allocation and Performance Optimization

## Citation

Cui, J., Wang, S., Ge, G., Wu, X., & Cao, X. (2026). *ARIS-Aided Multi-UAV-Enabled V2X Communication and Computation: Resource Allocation and Performance Optimization*. **IEEE Transactions on Mobile Computing**, 1-14. DOI: 10.1109/TMC.2026.3682488.

## TL;DR

Builds an active-RIS-aided multi-UAV V2X integrated communication and computation system and optimizes a new effective-energy-efficiency objective over associations, ARIS coefficients, multi-antenna beamforming, task offloading, transmit power, and computation resources. The ECCRA algorithm uses BCD with Dinkelbach transformation, first-order Taylor approximation, convex optimization, and integer programming substeps.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One multi-antenna BS and multiple multi-antenna UAVs support single-antenna vehicles with the aid of multiple active RISs. Vehicles use V2V communication, V2U or V2B computation offloading, and local computation; OFDM separates V2I offloading links, while active reflecting elements jointly adjust phase and amplitude and introduce amplifier noise and power consumption.

**Problem & objective**: Problem (18) is a high-dimensional nonconvex fractional program that maximizes effective energy efficiency, $\max_{\omega,\Theta,\mathbf P,\alpha,\beta,\gamma,\mathbf r,\mathbf f} R/E$, where $R$ combines communication and offloading rates and $E$ aggregates vehicle, UAV, BS, and ARIS energy consumption.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Receive beamforming | $\omega_{i,k}$ | continuous complex vector | Beamformer for vehicle $i$ at UAV or BS $k$ |
| ARIS coefficients | $\Theta_q$ | continuous complex diagonal matrix | Active phase and amplitude configuration of ARIS $q$ |
| Vehicle transmit power | $P_i$ | continuous, $0\leq P_i\leq P_{\max}^{\mathrm V}$ | Power used by vehicle $i$ |
| Frequency multiplexing | $\alpha_{i,j}$ | binary, $\{0,1\}$ | Whether communication vehicle $j$ is multiplexed with vehicle $i$ |
| Communication or offloading association | $\beta_{i,j(k)}$ | binary, $\{0,1\}$ | Vehicle communication target or UAV and BS offloading target |
| ARIS association | $\gamma_{i,q}$ | binary, $\{0,1\}$ | Whether vehicle $i$ uses ARIS $q$ |
| Task offloading ratio | $r_i$ | continuous, $0\leq r_i\leq1$ | Fraction of vehicle $i$'s task offloaded for edge computation |
| Edge compute allocation | $f_{i,k}^{\mathrm{U(B)}}$ | continuous, nonnegative | UAV or BS CPU rate allocated to vehicle $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV and BS beamforming powers do not exceed $P_{\max}^{\mathrm U}$ and $P_{\max}^{\mathrm B}$ |
| C2 | ARIS power is bounded by $P_{\max}^{\mathrm{RIS}}$, with $\theta_n\in[0,2\pi]$ and active gain $a_n\geq1$ |
| C3 | Each offloading vehicle selects one communication vehicle for spectrum multiplexing, $\alpha_{i,j}\in\{0,1\}$ |
| C4 | Each vehicle is scheduled for communication or computation offloading through one target, $\beta_{i,j(k)}\in\{0,1\}$ |
| C5 | Each scheduled vehicle selects one ARIS, $\sum_q\gamma_{i,q}=1$ and $\gamma_{i,q}\in\{0,1\}$ |
| C6 | Offloading ratios satisfy $0\leq r_i\leq1$ |
| C7 | The maximum local, offloading, and communication latency is at most $t_{\max}$ |
| C8 | Allocated UAV or BS CPU rates remain within $f_{\max}^{\mathrm{U(B)}}$ |
| C9 | Vehicle power satisfies $0\leq P_i\leq P_{\max}^{\mathrm V}$ |

**Algorithm**: Apply Dinkelbach's transformation to replace the fractional objective by $R-\lambda E$; use BCD to alternate multiple-association, joint-beamforming, and computation-resource subproblems; solve binary associations with integer programming, transform coupled continuous terms through first-order Taylor approximation and semidefinite relaxation, solve the resulting convex programs, and update the blocks until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Cui et al. [x] studied energy-efficient active reconfigurable intelligent surface aided multi-UAV V2X integrated communication and computation. They introduced effective energy efficiency to capture network energy cost together with communication and computation utilities, and formulated a joint optimization over associations, active reflecting coefficients, beamforming, task offloading, transmit power, and computation resources. Their ECCRA scheme applies Dinkelbach's transformation and block coordinate descent, with integer programming, semidefinite relaxation, first-order Taylor approximation, and convex optimization for the resulting subproblems. Simulations show that ECCRA attains higher effective energy efficiency than the evaluated no-ARIS, passive-RIS, random-ARIS, and MRT schemes, and the random-association experiment stabilizes after about four iterations at 175.9.

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
