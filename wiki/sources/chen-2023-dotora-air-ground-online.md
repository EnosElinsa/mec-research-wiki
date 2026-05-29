---
type: source
title: "Energy Efficient Task Offloading and Resource Allocation in Air-Ground Integrated MEC Systems: A Distributed Online Approach"
authors: ["Ying Chen", "Kaixin Li", "Yuan Wu", "Jiwei Huang", "Lian Zhao"]
year: 2023
url: "https://doi.org/10.1109/TMC.2023.3346431"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, air-ground-integrated-network, hierarchical-aerial-mec, task-offloading, stochastic-optimization, game-theory, hap, uav]
related:
  - "[[air-ground-integrated-network]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[lyapunov-optimization]]"
  - "[[potential-game]]"
  - "[[energy-latency-tradeoff]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[chen-2024-ulse-game]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Energy Efficient Task Offloading and Resource Allocation in Air-Ground Integrated MEC Systems: A Distributed Online Approach

## Citation

Chen, Y., Li, K., Wu, Y., Huang, J., & Zhao, L. (2023). *Energy Efficient Task Offloading and Resource Allocation in Air-Ground Integrated MEC Systems: A Distributed Online Approach*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3346431.

## TL;DR

An aerial MEC system with one HAP and multiple UAVs serving ground devices (GDs) in infrastructure-free regions, minimizing GD energy consumption. Because task arrivals and channel quality are stochastic, the authors use **stochastic optimization** to split the problem into a local-computation-resource sub-problem (solved by convex optimization) and an offloading-resource sub-problem (solved by **game theory** over competing GDs). They propose **DGMS** (distributed game-theoretical multi-server selection), **TPA** (transmission power allocation), and the overall **DOTORA** distributed online algorithm with theoretical analysis.

## Problem framing

Remote areas (wilderness, desert, ocean) lack ground communication infrastructure, so an air-based MEC network with HAP+UAV edge nodes provides over-the-air compute for energy/compute-limited GDs. Task arrivals and wireless quality are both random and dynamic, motivating an online, distributed solution that minimizes GD energy while satisfying offloading-resource constraints.

## System model

- **Tiers.** HAP + multiple UAVs as aerial edge nodes; GDs offload to them.
- **Stochasticity.** Random task arrivals and time-varying channel quality.
- **Decomposition.** (1) local computation resource allocation; (2) offloading resource allocation among competing GDs.

## Method

- **Sub-problem 1 (local):** convex optimization.
- **Sub-problem 2 (offloading):** model GD competition as a game; solve with **DGMS** (server selection) and **TPA** (transmit power).
- **DOTORA:** a distributed online algorithm combining the two, with theoretical performance analysis.

## Key findings

- Experiments include HAP-UAV vs. UAV-Only and HAP-Only framework comparisons and comparisons against other algorithms under the HAP-UAV framework; results validate the framework and DOTORA's ability to ensure performance while reducing device energy (qualitative; specific curves in the paper).

## Limitations / future work

Simulation-based, distributed-online setting. The parse does not enumerate explicit limitations beyond the stated framework assumptions.

## Relation to the corpus

A **HAP+UAV hierarchical aerial MEC** entry that uses stochastic optimization + game theory rather than DRL — pairing well with [[jia-2025-dro-uav-hap-mec]] (DRO over the same UAV+HAP setting) and [[kang-2023-mappo-hierarchical-aerial]] (MAPPO). Its game-theoretic offloading-competition framing links to [[chen-2024-ulse-game]] and [[potential-game]]; it shares co-authors Ying Chen / Yuan Wu / Jiwei Huang with [[chen-2024-ulse-game]] and [[huang-2023-mu-aec-task-energy]]. Reinforces [[air-ground-integrated-network]].

## Raw artifacts

- `raw/sources/Energy_Efficient_Task_Offloading_and_Resource_Allocation_in_Air-Ground_Integrated_MEC_Systems_A_Distributed_Online_Approach/full.md`
- Original PDF and extracted figures in the same folder.
