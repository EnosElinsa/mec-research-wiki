---
type: source
title: "MOALF-UAV-MEC: Adaptive Multiobjective Optimization for UAV-Assisted Mobile Edge Computing in Dynamic IoT Environments"
authors: ["Ali A. AL-Bakhrani", "Mingchu Li", "Mohammad S. Obaidat", "Gehad Abdullah Amran"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3544624"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
modeling_card: required
tags: [source, uav-mec, multi-objective-reinforcement-learning, model-predictive-control, particle-swarm-optimization, lyapunov-optimization, load-balancing]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[lyapunov-optimization]]"
  - "[[load-balancing-uav-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[song-2022-emorl-tcto-uav]]"
  - "[[multi-verse-optimizer]]"
created: 2026-05-29
updated: 2026-07-16
---

# MOALF-UAV-MEC: Adaptive Multiobjective Optimization for UAV-Assisted Mobile Edge Computing in Dynamic IoT Environments

## Citation

AL-Bakhrani, A. A., Li, M., Obaidat, M. S., & Amran, G. A. (2025). *MOALF-UAV-MEC: Adaptive Multiobjective Optimization for UAV-Assisted Mobile Edge Computing in Dynamic IoT Environments*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2025.3544624.

## TL;DR

A **multiobjective adaptive learning framework (MOALF-UAV-MEC)** for UAV-assisted MEC in dynamic IoT environments that integrates four techniques — **multiobjective RL (MORL)**, **model predictive control (MPC)**, **adaptive particle swarm optimization (APSO)**, and **Lyapunov optimization** — to optimize UAV trajectories, dynamic resource allocation, and system stability. A "burst mode" feature gives UAVs temporary performance boosts under high demand.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Dynamic IoT devices $D$ generate tasks for UAV edge nodes $U$ and ground edge servers $E$ over time slots $T$. Each UAV has position $\mathbf p_j(t)$, computing capacity $C_j$, energy state $E_j(t)$, velocity $\mathbf v_j(t)$, and optional burst-mode operation; tasks may be offloaded, resourced, or migrated among nodes.

**Problem & objective**: The mixed multiobjective problem minimizes $J=w_1J_{\mathrm{task}}+w_2J_{\mathrm{energy}}+w_3J_{\mathrm{completion}}+w_4J_{\mathrm{migration}}+w_5J_{\mathrm{util}}+w_6J_{\mathrm{coverage}}$ over the time horizon.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task offloading | $x_{ijk}(t)$ | binary, $\{0,1\}$ | Assign task $k$ from device $i$ to UAV $j$ |
| CPU allocation | $f_{ijk}(t)$ | continuous, $[0,C_j]$ | CPU resource for task $k$ from device $i$ on UAV $j$ |
| UAV trajectory | $\mathbf p_j(t)$ | continuous, $\mathbb R^3$ | Three-dimensional position of UAV $j$ |
| Task migration | $y_{ijkl}(t)$ | binary, $\{0,1\}$ | Migrate task $k$ from UAV $j$ to node $l$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | At most one UAV receives each task: $\sum_jx_{ijk}(t)\le1$ |
| C2 | Allocated CPU does not exceed UAV capacity: $\sum_{i,k}x_{ijk}(t)f_{ijk}(t)\le C_j$ |
| C3 | UAV energy stays above its minimum: $E_j(t)\ge E_{\min,j}$ |
| C4 | UAV speed is bounded: $\|\mathbf v_j(t)\|\le v_{\max,j}$ |
| C5 | Completion meets each task deadline: $T_{\mathrm{comp},ijk}(t)\le\tau_{i,k}$ |
| C6 | A task has at most one migration destination: $\sum_l y_{ijkl}(t)\le1$ |

**Algorithm**: Initialize MORL, MPC, APSO, and Lyapunov modules; at each slot observe $S_t$, let MORL choose $x_{ijk}(t)$ and initial $f_{ijk}(t)$, let MPC optimize $\mathbf p_j(t)$, let APSO refine $f_{ijk}(t)$, run a Lyapunov stability check and apply adjustments when needed, execute the actions, update the environment, and adapt the component weights.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

AL-Bakhrani et al. [x] studied multiobjective task offloading and resource control for UAV-assisted MEC serving dynamic IoT environments. They formulated a weighted objective over task time, energy, completion, migration, utilization, and coverage with binary offloading, resource, trajectory, and migration variables under capacity, energy, velocity, deadline, and migration constraints. Their MOALF-UAV-MEC chain combines MORL decisions, MPC trajectory optimization, APSO resource optimization, and Lyapunov stability checks with burst-mode adjustment. Simulations reported a 94.50% task completion rate, 96% load-balancing efficiency, an average of 1890 completed tasks per UAV, and a 55% task-completion increase during high-load periods.

## Problem framing

IoT proliferation strains network/compute resources. The paper targets several intertwined challenges at once: multiobjective optimization, adaptive resource allocation, energy efficiency, scalability, and QoS guarantees, in environments where demand fluctuates rapidly.

## System model / method

- Integrates **MORL + MPC + APSO + Lyapunov optimization** into one framework.
- **Burst mode:** UAVs temporarily boost performance in high-demand situations.

## Key findings

The paper reports specific figures (treated as the authors' stated results):
- Task completion rate **94.50%**, with an average of **1890 completed tasks per UAV** and **load-balancing efficiency 96%**.
- A **38% reduction** in UAV path length and a **55% increase in task completion** during high-load periods.
- Scalability evaluated by varying IoT devices from 50 to 500 and UAVs from 5 to 50 (Fig. 6), reporting graceful performance degradation vs MAPPO / MA-DRL and resource-consumption scaling — magnitudes are figure-derived.

These are the authors' reported numbers; some are figure/abstract-derived and should be read as indicative of claimed performance rather than independently verified.

## Limitations / future work

The extracted conclusion frames contributions but does not enumerate explicit limitations; the heavy integration of four techniques suggests complexity/tuning costs not quantified in the parse.

## Relation to the corpus

A **multiobjective + multi-technique** UAV-MEC entry that, like [[song-2022-emorl-tcto-uav]], combines multi-objective reinforcement learning with UAV trajectory/offloading — but layers in MPC, APSO, and Lyapunov optimization. Connects to [[load-balancing-uav-mec]], [[multi-objective-reinforcement-learning]], and [[lyapunov-optimization]].

## Raw artifacts

- `raw/sources/MOALF-UAV-MEC_Adaptive_Multiobjective_Optimization_for_UAV-Assisted_Mobile_Edge_Computing_in_Dynamic_IoT_Environments/full.md`
- Original PDF and extracted figures in the same folder.
