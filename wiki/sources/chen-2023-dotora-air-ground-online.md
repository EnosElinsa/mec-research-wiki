---
type: source
modeling_card: required
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
updated: 2026-07-16
---

# Energy Efficient Task Offloading and Resource Allocation in Air-Ground Integrated MEC Systems: A Distributed Online Approach

## Citation

Chen, Y., Li, K., Wu, Y., Huang, J., & Zhao, L. (2023). *Energy Efficient Task Offloading and Resource Allocation in Air-Ground Integrated MEC Systems: A Distributed Online Approach*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3346431.

## TL;DR

An aerial MEC system with one HAP and multiple UAVs serving ground devices (GDs) in infrastructure-free regions, minimizing GD energy consumption. Because task arrivals and channel quality are stochastic, the authors use **stochastic optimization** to split the problem into a local-computation-resource sub-problem (solved by convex optimization) and an offloading-resource sub-problem (solved by **game theory** over competing GDs). They propose **DGMS** (distributed game-theoretical multi-server selection), **TPA** (transmission power allocation), and the overall **DOTORA** distributed online algorithm with theoretical analysis.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground devices with stochastic task arrivals and queues obtain local computing or partial offloading service from one HAP and multiple hovering UAV edge servers over interference-coupled air-ground links in slotted time.

**Problem & objective**: Problem $\mathcal P_1$ is a stochastic mixed-integer program, $\min_{\mathcal Q(t)}\lim_{T\to\infty}\frac{1}{T}\sum_{t=0}^{T-1}\mathbb E\{E(t)\}$, minimizing long-term average ground-device energy while maintaining feasible local and offloaded processing.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Local CPU frequency | $f_n^l(t)$ | Continuous, $[0,f_n^{\max}]$ | Allocates local computing capacity to ground device $n$. |
| Server selection | $v_n^s(t)$ | Binary, $\{0,1\}$ | Indicates whether device $n$ offloads to HAP or UAV server $s$. |
| Transmission power | $p_n(t)$ | Continuous, $[0,p_n^{\max}]$ | Sets the uplink power used by device $n$ for offloading. |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Local CPU allocation satisfies $0\le f_n^l(t)\le f_n^{\max}$. |
| C2 | Server choices are binary and exclusive, $v_n^s(t)\in\{0,1\}$ and $\sum_{s=0}^{S}v_n^s(t)\le1$. |
| C3 | Uplink power satisfies $0\le p_n(t)\le p_n^{\max}$. |
| C4 | Processing cannot exceed the queue: $W_n^l(t)\le G_n(t)$ and $W_n^o(t)\le G_n(t)-W_n^l(t)$. |
| C5 | Queue evolution follows $G_n(t+1)=[G_n(t)-W_n^l(t)-W_n^o(t)]^++A_n(t)$ and is stabilized through drift-plus-penalty control. |

**Algorithm**: DOTORA applies Lyapunov drift-plus-penalty decomposition, solves local CPU frequency in closed form, obtains server choices through the potential-game DGMS procedure, refines uplink powers with TPA, and repeats online without future statistics.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied online task offloading and resource allocation for ground devices served cooperatively by one HAP and multiple UAV edge servers. They formulated a stochastic mixed-integer problem that minimizes long-term device energy subject to CPU-frequency, exclusive server-selection, transmit-power, queue-service, and stability constraints. DOTORA uses Lyapunov optimization to separate local computing from offloading, then combines a closed-form CPU decision with game-based server selection and iterative power allocation. Simulations report energy reductions of 15.73%, 15.95%, and 19.09% and queue-backlog reductions of 15.99%, 17.64%, and 88.84% relative to EUAG-20, GTCO-21, and full local computing, respectively.

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
