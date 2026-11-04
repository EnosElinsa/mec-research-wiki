---
type: source
modeling_card: required
title: "Learning-Based NOMA-Enabled Queue-Aware Task Offloading and AAV 3D Trajectory Planning for SAGIN"
authors: ["Peng Qin", "Hongjie Li", "Yang Fu", "Jinhui Hu", "Xue Wu", "Xianchao Zhang"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3552807"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, space-air-ground-integrated-network, noma, task-offloading, aav-trajectory, multi-agent-td3, lyapunov-optimization]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[noma]]"
  - "[[multi-agent-td3]]"
  - "[[lyapunov-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[wang-2024-hybrid-oma-noma-sagin]]"
  - "[[hsu-2025-drl-hues-hap-noma]]"
  - "[[fu-2025-otae-inference-lae-batching]]"
  - "[[lyapunov-guided-drl]]"
created: 2026-05-29
updated: 2026-11-03
---

# Learning-Based NOMA-Enabled Queue-Aware Task Offloading and AAV 3D Trajectory Planning for SAGIN

## Citation

Qin, P., Li, H., Fu, Y., Hu, J., Wu, X., & Zhang, X. (2025). *Learning-Based NOMA-Enabled Queue-Aware Task Offloading and AAV 3D Trajectory Planning for SAGIN*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3552807.

## TL;DR

A hierarchical **SAGIN** where AAVs provide access and satellites provide backhaul; **NOMA** reuses channels to raise spectrum utilization and throughput. The paper jointly plans AAV 3D trajectory, task offloading, task assignment, and computing-resource allocation to minimize system cost. Because queue-delay constraints couple with decisions, **Lyapunov optimization** splits the problem into three sub-problems solved by MTDTO, a CVX-based method, and GSCRA. The DRL backbone is **MATD3** (per the index terms).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A space-air-ground integrated network uses AAVs for access and satellites for backhaul. Users reach AAVs over NOMA links, each AAV computes part of a task and forwards the rest to one satellite, and user, AAV, and satellite queue backlogs evolve with the offloading and computing decisions.

**Problem & objective**: Problem P0 (42) minimizes total system cost, $\min_{\Psi(t),A(t),W(t),F_{AAV}(t),F_{sat}(t)}\sum_i\sum_tC_i(t)$, where (41) gives $C_i(t)=\delta_1E_i(t)+\delta_2T_i(t)$, a weighted sum of energy and delay.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| AAV 3-D coordinates | $\Psi(t)$ | continuous positions | AAV trajectory over slots |
| Task offloading | $a_{i,j}(t)\in A(t)$ | binary | User $i$ connects to AAV $j$ |
| AAV task proportion | $w_{j,k}^i(t)\in W(t)$ | continuous, $[0,1]$ | Share of user $i$'s task computed at AAV $j$; the rest, $1-w_{j,k}^i(t)$, goes to satellite $k$ |
| Computing resources | $F_{AAV}(t),F_{sat}(t)$ | continuous, bounded | CPU allocation at AAVs and satellites |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Task split limit $w_{j,k}^i(t)\in[0,1]$ |
| C2-C3 | Each user connects to at most one AAV per slot |
| C4-C5 | Each AAV connects to at most one satellite, $b_{j,k}(t)\in\{0,1\}$ |
| C6-C7 | Satellite and AAV computing allocations stay within available resources |
| C8 | Queue constraints (6)-(7) and (27) |
| C9 | AAV motion constraints (11)-(17): altitude, horizontal and vertical step, region, coverage separation, and minimum distance |

**Algorithm**: Construct virtual queues and a drift-plus-penalty bound → split each slot into SP1 (trajectory and offloading, learned by MATD3), SP2 (AAV task proportion and AAV computing, solved with CVX), and SP3 (satellite computing, solved by the greedy GSCRA allocation) → update the queues and repeat.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Qin et al. [x] studied queue-aware task offloading and three-dimensional AAV trajectory planning in a NOMA-enabled space-air-ground integrated network. They formulated a stochastic system-cost minimization problem that jointly considers AAV trajectories, user-AAV offloading, AAV-satellite task splitting, and computing-resource allocation under queue, connection, computing, and motion constraints. Lyapunov optimization decomposes the long-term problem into three subproblems solved by the MATD3-based trajectory/offloading module, a CVX-based resource module, and GSCRA task assignment. In the reported setting, the proposed method reduces total system cost by 18.76%, 29.40%, 35.38%, and 52.14% against MADDPG, MATD3-F, MATD3-P, and DDPG, respectively. The corresponding average queue-backlog reductions are 4.36%, 12.49%, 15.95%, and 30.38%.

## Problem framing

SAGIN serves users lacking ground base stations: AAVs give massive access, satellites give backhaul. NOMA improves channel reuse, but different AAV trajectories and task assignments yield different delay/energy; queue dynamics add high dynamicity, demanding a queue-aware, learning-based solution.

## System model

- **Hierarchy.** AAVs (access) + satellites (backhaul) cooperatively process offloaded tasks.
- **NOMA.** Channel reuse for spectrum efficiency/throughput.
- **Coupling.** Queue-delay constraints couple with decision-making → handled by [[lyapunov-optimization]].

## Method

- Lyapunov optimization splits into three sub-problems addressed by **MTDTO**, a **CVX-based** method, and **GSCRA** to minimize system cost; trajectory/offloading learning uses **MATD3** ([[multi-agent-td3]]).

## Key findings

- Against MADDPG, MATD3-F, MATD3-P, and DDPG, the proposed method lowers total system cost by **18.76%, 29.40%, 35.38%, and 52.14%**, respectively, in the Fig. 4 setting.
- The same benchmark order shows average queue-backlog reductions of **4.36%, 12.49%, 15.95%, and 30.38%** in Fig. 7.
- When the AAV computation capacity rises from 3 GHz to 8 GHz at $R_{LU}(t)=15$ Mbps, total system cost drops by **17.51%** in Fig. 9.

## Limitations / future work

Future work: integrate cache resources into the SAGIN network for more efficient service.

## Relation to the corpus

A **NOMA + SAGIN + DRL** entry that pairs with [[wang-2024-hybrid-oma-noma-sagin]] (hybrid OMA/NOMA mode selection) and the HAP-NOMA energy-harvesting scheduler [[hsu-2025-drl-hues-hap-noma]]. Its Lyapunov-decomposition + MATD3 echoes the queue-aware Lyapunov pattern in [[you-2025-uncertain-maritime-hasac]]. Shares authors Peng Qin / Yang Fu with the low-altitude edge-inference paper [[fu-2025-otae-inference-lae-batching]]. Reinforces [[noma]] and [[space-air-ground-integrated-network]].

## Raw artifacts

- `raw/sources/Learning-Based_NOMA-Enabled_Queue-Aware_Task_Offloading_and_AAV_3D_Trajectory_Planning_for_SAGIN/Learning-Based_NOMA-Enabled_Queue-Aware_Task_Offloading_and_AAV_3D_Trajectory_Planning_for_SAGIN.md`
- Original PDF and extracted figures in the same folder.
