---
type: source
title: "Load-Balanced Recipient Assignment and Time-Constrained Scheduling of Multiple Battery Mules for UAV Swarm Service Prolongation"
authors: ["Mingyu Li", "Xianglin Wei", "Xiaolong Xu", "Yangang Wang"]
year: 2026
url: "https://doi.org/10.1109/TAES.2026.3664811"
venue: "IEEE Transactions on Aerospace and Electronic Systems, 62"
modeling_card: required
tags: [source, battery-swapping, battery-mule, uav-swarm, service-continuity, mixed-integer-programming, traveling-salesman-problem, load-balancing]
related:
  - "[[in-flight-uav-energy-replenishment]]"
  - "[[battery-swapping-uav-mec]]"
  - "[[mixed-integer-linear-programming]]"
  - "[[generalized-traveling-salesman-problem]]"
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[zhu-2022-aerial-refueling-uav-charging]]"
created: 2026-11-02
updated: 2026-11-02
---

# Load-Balanced Recipient Assignment and Time-Constrained Scheduling of Multiple Battery Mules for UAV Swarm Service Prolongation

## Citation

Li, M., Wei, X., Xu, X., & Wang, Y. (2026). *Load-Balanced Recipient Assignment and Time-Constrained Scheduling of Multiple Battery Mules for UAV Swarm Service Prolongation*. **IEEE Transactions on Aerospace and Electronic Systems, 62**. DOI: 10.1109/TAES.2026.3664811.

## TL;DR

Battery mules are UAVs that carry fresh batteries and swap them into serving UAVs ("recipients") in the air. The paper schedules several mules for a swarm as a 0-1 mixed integer program that maximizes the continuous service ratio (CSR) and minimizes its variance across subswarms, solved in two stages: greedy load-balanced recipient assignment (ENS-RA) and time-constrained TSP-based single-mule scheduling (ITSP-MS).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV swarm $\mathcal U$ serves ground users from deployment positions $P_{U_j}(\tau)$ over $Q$ timeslots, while a set $\mathcal M$ of $L$ battery mules starts at a ground station $P_{GS}$. Each UAV's battery depletes through hovering, flying, and task execution. A mule flies a path $\mathcal P_i(\tau)$, reaches recipients at times $\mathcal T_i(\tau)$, and swaps batteries on board. CSR is a UAV's service time divided by total time.

**Problem & objective**: P0, a 0-1 mixed integer program: $\max_{\mathcal P_i(\tau),\mathcal T_i(\tau),\chi_{ij}(\tau)}\sum_{\tau=1}^Q\big(w_1C_{\mathcal U}(\tau)-w_2C_{\mathrm{var}}(\tau)\big)$, accumulating swarm CSR minus CSR variance across subswarms.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Recipient selection | $\chi_{ij}(\tau)$ | binary | Whether mule $M_i$ swaps the battery of UAV $U_j$ in slot $\tau$ |
| Mule path | $\mathcal P_i(\tau)$ | ordered set of recipients | Flight route of mule $M_i$ |
| Arrival times | $\mathcal T_i(\tau)$ | continuous | Time mule $M_i$ reaches each UAV on its path |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (49) | $\chi_{ij}(\tau)\in\{0,1\}$. |
| (5) | UAV deployment positions are restricted. |
| (8) | Mule horizontal flying velocity lies in its allowed range. |
| (9)-(12) | Arrival-time limits so a mule reaches a recipient before its battery is exhausted. |

**Algorithm**: Stage 1 (P1) minimizes accumulated CSR variance through ENS-RA, a greedy clustering that assigns recipients to mules with balanced load and splits the problem into single-mule subproblems. Stage 2 runs ITSP-MS, which inserts battery-swap time limits into a TSP solution to pick recipients and plan each mule's trajectory per timeslot.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied on-board battery swapping by battery mules to extend the service time of a UAV swarm, where the UAVs receiving the swapping service are called recipients. They formulated multimule scheduling as a 0-1 mixed integer programming problem that maximizes the accumulated continuous service ratio of the swarm while reducing its variance across subswarms. A two-stage framework is proposed: a greedy algorithm first clusters recipients and assigns them to all mules to achieve load balance, decomposing the problem into single-mule scheduling subproblems. A heuristic algorithm then integrates time constraints into the traveling salesman problem to schedule each mule. Simulation results show that the framework achieves at least 30.70% higher average continuous service ratio than the benchmarks.

## Problem framing

Battery limits interrupt swarm service, and returning to a station takes UAVs out of service. Swapping batteries in the air keeps UAVs on station, but several mules must share a large swarm without leaving some regions under-served.

## System model

- Energy model includes hovering, flight, and task-execution consumption per slot.
- A sustained decision paradigm spans many consecutive slots (100 in the experiments) rather than one decision.
- A UAVMove policy lets each UAV move within $\pm0.5$ m with 50% probability per slot to test mobility.

## Method

Decoupling the variance and CSR objectives makes the solution independent of $w_1$ and $w_2$. ITSP-MS is compared with five scheduling methods, and ENS-RA with RAP and K-Means++ assignment.

## Key findings

- ITSP-MS CSR stabilizes around 93%, and its average CSR exceeds ACO by 30.70%.
- The ratio of UAVs swapped by mules (RUSM) is 16.85% and 6.10% lower when ITSP uses RAP or K-Means++ assignment instead of ENS-RA.
- Under swarm mobility, ITSP's RUSM is at least 2.5 times that of the other algorithms.

## Limitations / future work

The authors plan DRL for the infinite search space of battery swapping, dynamic partition adjustment, and inter-subswarm mule coordination.

## Relation to the corpus

Airborne swapping is the battery-exchange branch of [[in-flight-uav-energy-replenishment]], while [[battery-swapping-uav-mec]] covers station-based swaps. Wireless in-flight charging by charging UAVs appears in [[zhu-2022-aerial-refueling-uav-charging]].

## Raw artifacts

- Parse: `raw/sources/Load-Balanced_Recipient_Assignment_and_Time-Constrained_Scheduling_of_Multiple_Battery_Mules_for_UAV_Swarm_Service_Prolongation/Load-Balanced_Recipient_Assignment_and_Time-Constrained_Scheduling_of_Multiple_Battery_Mules_for_UAV_Swarm_Service_Prolongation.md`
- Origin PDF and extracted figures are in the same folder.
