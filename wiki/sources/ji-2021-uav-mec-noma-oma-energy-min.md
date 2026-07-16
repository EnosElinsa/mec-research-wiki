---
type: source
title: "Energy Consumption Minimization in UAV-Assisted Mobile-Edge Computing Systems: Joint Resource Allocation and Trajectory Design"
authors: ["Jiequ Ji", "Kun Zhu", "Changyan Yi", "Dusit Niyato"]
year: 2021
url: "https://doi.org/10.1109/JIOT.2020.3046788"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, energy-minimization, trajectory-optimization, resource-allocation, noma, oma, partial-offloading, successive-convex-approximation]
related:
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[dusit-niyato]]"
  - "[[li-2020-energy-efficient-uav-mec-admm]]"
created: 2026-06-04
updated: 2026-07-16
modeling_card: required
---

# Energy Consumption Minimization in UAV-Assisted Mobile-Edge Computing Systems: Joint Resource Allocation and Trajectory Design

## Citation

Ji, J., Zhu, K., Yi, C., & Niyato, D. (2021). *Energy Consumption Minimization in UAV-Assisted Mobile-Edge Computing Systems: Joint Resource Allocation and Trajectory Design*. **IEEE Internet of Things Journal**, 8(10). DOI: 10.1109/JIOT.2020.3046788. (Received 29 October 2020; accepted 15 December 2020; published 23 December 2020; current version 7 May 2021.)

## TL;DR

Studies a fixed-wing UAV carrying a MEC server and serving user devices (UDs) with **partial offloading** (split between local and UAV compute). Minimizes the **weighted-sum energy consumption of both the UAV and UDs** under OMA and NOMA access modes via joint trajectory + resource allocation. Develops alternating iterative algorithms (block alternating descent + SCA for trajectory; Lagrange duality for resource allocation). Key finding: OMA achieves **lower total energy than NOMA** in this setting; the joint design significantly outperforms benchmarks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude fixed-wing UAV MEC server serves user devices that split each task between local execution and UAV offloading through either OMA or NOMA.

**Problem & objective**: Jointly choose partial offloading, CPU frequencies, and the UAV path to minimize weighted UAV and user energy, $\min_{\mathbf F,\mathbf L,\mathbf Q}\sum_n(\sum_s\omega_sE_{s,n}+\omega_uE_{u,n})$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Local CPU frequency | $f_s[n]$ | nonnegative continuous | Local processing rate of user device $s$ |
| UAV CPU frequency | $f_{u,s}[n]$ | nonnegative continuous | Cloudlet processing rate for user $s$ |
| Offloaded bits | $L_{s,u}^{\mathrm{off}}[n]$ | nonnegative continuous | Input bits sent from user $s$ to the UAV |
| Returned bits | $L_{u,s}^{\mathrm{don}}[n]$ | nonnegative continuous | Output bits sent from the UAV to user $s$ |
| UAV trajectory | $\mathbf q_u[n]$ | continuous 2-D positions | Fixed-altitude UAV location per slot |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Computation and downlink causality prevent use of bits before uplink receipt or computation |
| C2 | Local plus offloaded bits complete each user task and returned bits match output size |
| C3 | All CPU frequencies and bit allocations are nonnegative, with terminal-slot timing restrictions |
| C4 | Weighted UAV communication, computation, and propulsion energy remains feasible |
| C5 | The UAV starts and ends at prescribed points and satisfies per-slot displacement $\|\mathbf q_u[n+1]-\mathbf q_u[n]\|\leq D_{\max}$ |

**Algorithm**: Alternate a convex resource-allocation block solved by Lagrange duality with an SCA trajectory block, deriving separate update procedures for OMA and NOMA interference structures.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ji et al. [x] formulated partial offloading for a fixed-wing UAV MEC server as a joint resource-allocation and trajectory problem under OMA and NOMA. Their objective minimizes weighted UAV and user energy over local and offloaded bits, CPU frequencies, and UAV positions subject to causality, completion, mobility, and energy conditions. A block-alternating method solves resource allocation by Lagrange duality and trajectory updates by successive convex approximation. Simulations show the joint design is the lowest-energy scheme in both access modes, and at UAV weight 0.2 it reduces user energy from about $2.2\times10^5$ J for local computing to 19 J while preserving the weighted objective.

## Problem framing

Most prior UAV-MEC works either minimize user energy alone or assume full offloading. This paper jointly minimizes weighted-sum energy of the UAV (mechanical + compute) and all UDs under a partial offloading model (each UD decides how many bits to offload vs. process locally), and does so for both OMA and NOMA access modes. NOMA allows multiple UDs to share spectrum via SIC but introduces additional intra-channel interference, creating a complex interaction with the trajectory design. The paper notes it is the first to study the weighted-sum energy problem in UAV-MEC with joint local-and-offload task partition.

## System model

- **Single fixed-wing UAV** with a MEC server; K UDs, each with a computation task of B_k bits; partial offloading (L_s,k bits offloaded, rest local).
- **Two access modes:** OMA (TDMA-based, orthogonal time slots) and NOMA (SIC-based, simultaneous transmission decoded in power order).
- **Communication:** uplink (UD→UAV) for task offloading; downlink (UAV→UD) for result return. Channels are LoS-dominated.
- **Energy components:** UD transmit energy + local compute energy + UAV flight energy (propulsion model) + UAV compute energy.
- **Objective:** minimize ω_UAV × E_UAV + Σ_k ω_k × E_k (weighted sum), subject to computation-causality constraints (bits offloaded + computed ≥ task size) and UAV trajectory kinematics.

## Method

- **Block alternating descent:** split variables into (resource allocation block) and (trajectory block).
- **Resource allocation subproblem** (fixed trajectory): convex → solved by Lagrange duality, obtaining closed-form optimal CPU frequencies and offloading bits.
- **Trajectory subproblem** (fixed resource): non-convex → SCA approximation.
- Separate algorithms derived for OMA and NOMA (different interference structures).

## Key findings

- The proposed joint design achieves **significant energy savings** over benchmarks (separate optimization of trajectory and resources; UAV-only or UD-only energy optimization) for both access modes (parse abstract + Section V).
- **Weighted-sum energy decreases as task-completion time budget increases**, revealing a time–energy tradeoff (parse contribution item 4 / Section V).
- **OMA achieves lower sum energy than NOMA** in the simulated settings — attributed to NOMA's SIC processing overhead and intra-cell interference affecting the tradeoff (parse contribution item 4 / Section V).

## Limitations / future work

Single UAV; LoS channel assumed throughout. The NOMA decoding order is fixed (sorted by channel gain); optimal order selection is not explored. Parse does not enumerate explicit numerical gains beyond the qualitative observations above.

## Relation to the corpus

Dusit Niyato ([[dusit-niyato]]) is a co-author. Complements [[li-2020-energy-efficient-uav-mec-admm]] (which maximizes energy efficiency) with an energy minimization objective; and [[jeong-2018-uav-cloudlet-bit-allocation]] which also examines OMA vs NOMA for UAV-MEC. The OMA-beats-NOMA finding in the energy minimization setting is a notable counterpoint to NOMA's spectral-efficiency advantage in rate-maximization contexts.

## Raw artifacts

- `raw/sources/Energy_Consumption_Minimization_in_UAV-Assisted_Mobile-Edge_Computing_Systems_Joint_Resource_Allocation_and_Trajectory_Design/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
