---
type: source
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
updated: 2026-06-09
---

# Joint Task Offloading and Resource Allocation in Aerial-Terrestrial UAV Networks With Edge and Fog Computing for Post-Disaster Rescue

## Citation

Sun, G., He, L., Sun, Z., Wu, Q., Liang, S., Li, J., Niyato, D., & Leung, V. C. M. (2024). *Joint Task Offloading and Resource Allocation in Aerial-Terrestrial UAV Networks With Edge and Fog Computing for Post-Disaster Rescue*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3350886. (Manuscript received 5 May 2023; accepted 2 January 2024; date of publication 8 January 2024; date of current version 6 August 2024. A small part appeared at IEEE MSN 2022, DOI 10.1109/MSN57253.2022.00030.)

## TL;DR

A **three-layer post-disaster rescue** computing architecture combining MEC and **vehicle fog computing (VFC)**: a vehicle fog layer, a UAV client layer, and a UAV edge layer. The joint task-offloading + resource-allocation problem (**JTRAOP**) maximizes time-average system utility. Since it is NP-hard, the **MVTORA** approach splits it into a game-theoretic algorithm for offloading decisions, a convex-optimization algorithm for MEC resource allocation, and an evolutionary-computation-based hybrid algorithm for VFC resource allocation.

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
