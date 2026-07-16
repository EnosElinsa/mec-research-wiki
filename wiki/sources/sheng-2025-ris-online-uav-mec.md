---
type: source
modeling_card: required
title: "Online Trajectory Planning and Resource Allocation of UAV-Enabled MEC Networks Empowered by RIS"
authors: ["Zhichao Sheng", "Hao Hu", "Ali A. Nasir", "Yong Fang", "Daniel B. da Costa"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3503687"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, ris, uav-mec, lyapunov-optimization, uav-trajectory-control, energy-efficiency, outage-constraint]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[lyapunov-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
  - "[[wu-2026-model-based-ppo-ris-uav-mec]]"
created: 2026-07-07
updated: 2026-07-16
---

# Online Trajectory Planning and Resource Allocation of UAV-Enabled MEC Networks Empowered by RIS

## Citation

Sheng, Z., Hu, H., Nasir, A. A., Fang, Y., & da Costa, D. B. (2025). *Online Trajectory Planning and Resource Allocation of UAV-Enabled MEC Networks Empowered by RIS*. **IEEE Transactions on Green Communications and Networking**, 9(3), 1224-1238. DOI: 10.1109/TGCN.2024.3503687. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

An online [[intelligent-reflecting-surface]]-assisted UAV-MEC controller for mobile ground users with random task arrivals. The method uses [[lyapunov-optimization]] to convert a long-term queue-stability and energy-efficiency objective into per-slot problems, then applies Dinkelbach, BCD, SCA, and Bernstein-type outage approximations to jointly optimize offloading/computation bits, bandwidth/time allocation, UAV trajectory, and RIS phase shifts.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Mobile ground users generate random tasks for a UAV MEC server that communicates with a powerful AP through a building-mounted RIS, with blocked direct links, finite UAV energy, queue backlogs, and a prescribed final destination.

**Problem & objective**: The online stochastic program minimizes energy per processed bit, $\min \eta_{EE}=\overline E/\overline L$, over offloading, computation, radio, trajectory, and RIS controls.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| GU-to-UAV offloading bits | $l_{u,n}^{off}[t]$ | continuous, queue bounded | Bits sent from user $n$ to the UAV |
| Computed bits | $l_{u,n}^{comp}[t]$ | continuous, CPU bounded | Bits processed at the UAV |
| Bandwidth allocation | $B_n[t]$ | continuous, nonnegative | User bandwidth share |
| Transmission times | $\tau_{n,1}[t],\tau_{n,2}[t]$ | continuous, slot bounded | GU-UAV and UAV-AP durations |
| UAV trajectory | $\mathbf q[t]$ | continuous, speed bounded | UAV position |
| RIS phase shifts | $\Theta[t]$ | discrete or continuous phase set | RIS reflection configuration |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Offloaded bits obey data causality: $l_{u,n}^{off}[t]\leq Q_n[t]+A_n[t]$. |
| C2 | Computed and forwarded bits do not exceed queued data and CPU capacity. |
| C3 | GU-UAV and UAV-AP offloading obey their rate and time limits. |
| C4 | User and UAV queues are stable in the long term. |
| C5 | Average UAV energy respects its budget: $\lim_TT^{-1}\sum_t\mathbb E[e_f[t]]\leq E_u$. |
| C6 | Trajectory speed and final-destination reachability are bounded. |
| C7 | Outage probability constraints are enforced through the per-slot robust approximation. |

**Algorithm**: Apply Lyapunov drift-plus-penalty for online queue-aware decisions, Dinkelbach for the fractional energy-efficiency objective, and block coordinate descent with successive convex approximation and Bernstein-type outage reformulation for the four control blocks.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sheng et al. [x] study online RIS-assisted UAV MEC for mobile users with stochastic task arrivals and blocked direct links. Their fractional objective minimizes energy per processed bit while enforcing data causality, computation and communication capacity, queue stability, energy budget, mobility, destination, and outage constraints. Lyapunov optimization supplies online queue-aware decisions, while Dinkelbach, block coordinate descent, successive convex approximation, and Bernstein approximations solve the coupled resource blocks. The parsed simulations report better energy-efficiency behavior than equal-resource and non-predictive schemes and further gains as the RIS grows.

## Problem framing

Offline UAV-RIS-MEC designs assume future task arrivals and user positions are known. This paper targets a more dynamic setting where mobile users move randomly and tasks arrive stochastically, so the UAV must plan trajectory and resources online while maintaining task-queue stability, UAV energy-budget feasibility, and offloading outage constraints.

## System model

A UAV equipped with an MEC server assists multiple mobile ground users and relays offloaded data through a building-mounted RIS to an AP with a powerful MEC server. Direct GU-RIS and GU-AP links are blocked. Users follow a Gauss-Markov mobility model and generate random tasks; the UAV has a finite energy budget and must move from an initial to a final position within the task duration.

## Method

The long-term stochastic objective minimizes energy consumption per processed bit while maintaining user/UAV queue stability. The paper uses Dinkelbach to handle the fractional objective and Lyapunov drift-plus-penalty to obtain per-slot online decisions. Each per-slot problem is decomposed into four subproblems over computation/offloading bits, bandwidth/time allocation, UAV trajectory, and RIS phases; non-convex outage constraints are approximated using Bernstein-type inequalities and SCA.

## Key findings

- The optimized trajectory moves closer to task-generating users and sometimes stays near the center to relay unprocessed tasks to the AP, depending on the Lyapunov control parameter `V`.
- The parse reports that `V` balances energy efficiency against queue backlog; large `V` increases the objective emphasis but can worsen queue stability.
- In the parsed simulation discussion, the proposed online algorithm outperforms resource-equal and non-predictive benchmark schemes in energy-efficiency behavior.
- Increasing RIS reflecting elements improves system energy efficiency by strengthening the UAV-to-AP channel and giving the UAV more flexibility to reduce energy consumption.

## Limitations / future work

The paper assumes known channel state information in the main formulation and uses simulation evaluation. The conclusion names robust online trajectory and resource allocation under imperfect CSI as a future extension.

## Relation to the corpus

This source links the classical online-control line in [[lyapunov-optimization]] to RIS-aided UAV-MEC. It complements [[qin-2023-ris-uav-mec-ee]], which is a mostly offline RIS-assisted UAV-MEC energy-efficiency formulation, and [[wu-2026-model-based-ppo-ris-uav-mec]], which uses decentralized model-based PPO. Here the distinctive contribution is online queue-stable control under user mobility, random arrivals, and offloading outage probability.

## Raw artifacts

- `raw/sources/Online Trajectory Planning and Resource Allocation of UAV-Enabled MEC Networks Empowered by RIS/Online Trajectory Planning and Resource Allocation of UAV-Enabled MEC Networks Empowered by RIS.md`
- Original PDF and extracted figures (`images/`) in the same folder.
