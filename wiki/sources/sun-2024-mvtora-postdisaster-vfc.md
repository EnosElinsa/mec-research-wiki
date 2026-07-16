---
type: source
modeling_card: required
title: "Joint Task Offloading and Resource Allocation in Aerial-Terrestrial UAV Networks With Edge and Fog Computing for Post-Disaster Rescue"
authors: ["Geng Sun", "Long He", "Zemin Sun", "Qingqing Wu", "Shuang Liang", "Jiahui Li", "Dusit Niyato", "Victor C. M. Leung"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3350886"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, post-disaster-mec, vehicle-fog-computing, task-offloading, game-theory, three-tier, uav]
related:
  - "[[post-disaster-mec]]"
  - "[[vehicle-fog-computing]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[potential-game]]"
  - "[[task-offloading]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[sun-2023-bargain-match-vec]]"
  - "[[kang-2023-mappo-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-07-16
---

# Joint Task Offloading and Resource Allocation in Aerial-Terrestrial UAV Networks With Edge and Fog Computing for Post-Disaster Rescue

## Citation

Sun, G., He, L., Sun, Z., Wu, Q., Liang, S., Li, J., Niyato, D., & Leung, V. C. M. (2024). *Joint Task Offloading and Resource Allocation in Aerial-Terrestrial UAV Networks With Edge and Fog Computing for Post-Disaster Rescue*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3350886. (Manuscript received 5 May 2023; accepted 2 January 2024; date of publication 8 January 2024; date of current version 6 August 2024. A small part appeared at IEEE MSN 2022, DOI 10.1109/MSN57253.2022.00030.)

## TL;DR

A **three-layer post-disaster rescue** computing architecture combining MEC and **vehicle fog computing (VFC)**: a vehicle fog layer, a UAV client layer, and a UAV edge layer. The joint task-offloading + resource-allocation problem (**JTRAOP**) maximizes time-average system utility. Since it is NP-hard, the **MVTORA** approach splits it into a game-theoretic algorithm for offloading decisions, a convex-optimization algorithm for MEC resource allocation, and an evolutionary-computation-based hybrid algorithm for VFC resource allocation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A three-layer post-disaster architecture contains vehicle fog nodes, UAV clients, and UAV edge servers. Rescue tasks can move among the vehicle, UAV, and edge layers, and the controller allocates computation resources across the heterogeneous nodes.

**Problem & objective**: JTRAOP, an NP-hard joint offloading and resource-allocation problem, maximizes time-average system utility, $\max\lim_{T\to\infty}T^{-1}\sum_t U(t)$, over task destinations and MEC/VFC resources.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task offloading | $o_i(t)$ | discrete/binary | Execution layer selected for task $i$ |
| MEC resource allocation | $f_{i,k}^{\mathrm{MEC}}(t)$ | continuous, nonnegative | CPU resource assigned by UAV edge node $k$ |
| VFC resource allocation | $f_{i,v}^{\mathrm{VFC}}(t)$ | continuous, nonnegative | CPU resource assigned by vehicle fog node $v$ |
| Server matching | $m_{i,s}(t)$ | binary | Task-to-server association |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each task is assigned to one feasible vehicle, UAV, or edge execution layer |
| C2 | MEC and VFC CPU allocations do not exceed node capacities |
| C3 | Offloading links, task sizes, and execution delays remain feasible |
| C4 | Time-average utility and resource constraints are respected over the rescue horizon |
| C5 | The three-layer coordination maintains service connectivity after the disaster |

**Algorithm**: Solve task offloading with the MVTORA game-theoretic algorithm → solve MEC resource allocation by convex optimization → solve VFC allocation with the evolutionary hybrid algorithm → alternate the blocks and evaluate time-average utility, delay, and energy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sun et al. [x] studied joint task offloading and resource allocation in a three-layer aerial-terrestrial UAV network for post-disaster rescue. The vehicle fog, UAV client, and UAV edge layers cooperate to maximize time-average system utility under heterogeneous compute and communication capacities. They formulated the NP-hard JTRAOP and decomposed it into a game-theoretic offloading block, a convex MEC resource-allocation block, and an evolutionary-computation VFC block. The resulting MVTORA scheme separates the three blocks while retaining their utility coupling. Simulations report higher time-average utility, lower average task-completion delay, and lower total energy than the evaluated baseline approaches.

## Problem framing

UAVs are valuable for fast-response disaster rescue but have limited battery/compute, which shortens endurance and raises response delay for mission-critical tasks. Combining aerial (UAV MEC) and terrestrial (vehicle fog) compute capabilities addresses this.

## System model

- **Three layers.** Vehicle fog layer (VFC), UAV client layer, UAV edge layer.
- **Objective.** Maximize the time-average system utility via joint task offloading + computing-resource allocation (the JTRAOP), proven NP-hard.

## Method

- **MVTORA** (MEC-VFC-aided task offloading and resource allocation), low-complexity, separating offloading from resource allocation:
  - **Task-offloading decision:** game-theoretic algorithm.
  - **MEC resource allocation:** convex optimization.
  - **VFC resource allocation:** evolutionary-computation-based hybrid algorithm.

## Key findings

- Simulations show MVTORA's superiority in time-average system utility, average task completion delay, and total energy consumption versus baselines (qualitative; specific curves in the paper).

## Limitations / future work

Future work: extend to include UAV trajectory optimization. The discussion also notes additional hardware overhead from the three-layer structure and that energy consumption is not always optimal against some baselines because the objective weights latency more heavily for disaster rescue.

## Relation to the corpus

A **post-disaster MEC** entry alongside [[peng-2025-drudm-cfg]] (fairness-aware multi-agent DRL for post-disaster AMEC), but using a game-theory + convex + evolutionary hybrid rather than DRL, and introducing **vehicle fog computing** to the corpus. Its game-theoretic offloading links to [[potential-game]]; the Geng Sun / Zemin Sun / Jiahui Li cluster connects it to [[sun-2023-bargain-match-vec]] and other Jilin/NTU sources. Reinforces [[post-disaster-mec]] and [[three-tier-cloud-edge-end]].

## Raw artifacts

- `raw/sources/Joint_Task_Offloading_and_Resource_Allocation_in_Aerial-Terrestrial_UAV_Networks_With_Edge_and_Fog_Computing_for_Post-Disaster_Rescue/full.md`
- Original PDF (`c83b18ed-ed3b-4ee8-98d0-5f04b355c25e_origin.pdf`) and extracted figures (`images/`) in the same folder.
