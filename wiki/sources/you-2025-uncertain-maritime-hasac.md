---
type: source
modeling_card: required
title: "Joint Computation Offloading and Resource Allocation for Uncertain Maritime MEC via Cooperation of AAVs and Vessels"
authors: ["Jiahao You", "Ziye Jia", "Chao Dong", "Qihui Wu", "Zhu Han"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3581970"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, computation-offloading, lyapunov-optimization, markov-game, heterogeneous-agent-sac, aav]
related:
  - "[[maritime-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[masac]]"
  - "[[heterogeneous-agent-rl]]"
  - "[[stochastic-game]]"
  - "[[task-offloading]]"
  - "[[wang-2025-double-edge-samin]]"
  - "[[wang-2024-twotier-satellite-marine]]"
  - "[[jia-2022-hierarchical-aerial-matching]]"
  - "[[lyapunov-guided-drl]]"
created: 2026-05-29
updated: 2026-11-03
---

# Joint Computation Offloading and Resource Allocation for Uncertain Maritime MEC via Cooperation of AAVs and Vessels

## Citation

You, J., Jia, Z., Dong, C., Wu, Q., & Han, Z. (2025). *Joint Computation Offloading and Resource Allocation for Uncertain Maritime MEC via Cooperation of AAVs and Vessels*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3581970.

## TL;DR

Maritime MEC via cooperation of autonomous aerial vehicles (AAVs) and vessels, minimizing total task execution time under **uncertain** task arrivals. **Lyapunov optimization** converts the long-term constraints into per-slot short-term ones, yielding small-scale problems; the heterogeneity of AAV/vessel actions and resources is then captured as a **Markov game (MG)**, solved by a **heterogeneous-agent soft actor-critic** that sequentially updates the agents' networks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Maritime IoT devices (MIoTs) with uncertain task arrivals offload to AAVs, which can forward tasks to vessels. Each MIoT, AAV, and vessel keeps a task queue, (10)-(16), and AAVs and vessels have limited computing resources.
**Problem & objective**: Problem $\mathscr P0$ (20) minimizes the long-term average time cost of all tasks, $\min_{\mathcal O,\mathcal S,\mathcal F^u,\mathcal F^v}\lim_{T\to\infty}\frac1T\sum_t\mathbb E[\Phi(t)]$, with $\Phi(t)=\sum_iT_i^a(t)$ (18).
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| MIoT-to-AAV offloading | $\mathcal O=\{o_{i,j}(t)\}$ | binary | MIoT $i$ offloads to AAV $j$ |
| AAV-to-vessel offloading | $\mathcal S=\{s_{j,k}(t)\}$ | binary | AAV $j$ forwards to vessel $k$ |
| AAV computing | $\mathcal F^u=\{f_{i,j}^u(t)\}$ | continuous | CPU allocated by AAV $j$ to MIoT $i$ |
| Vessel computing | $\mathcal F^v=\{f_{j,k}^v(t)\}$ | continuous | CPU allocated by vessel $k$ to AAV $j$ |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (6)-(7) | Binary MIoT offloading with at most one AAV, $\sum_jo_{i,j}(t)\le1$ |
| (8)-(9) | Binary AAV forwarding with at most one vessel, $\sum_ks_{j,k}(t)\le1$ |
| (12) | AAV computing $\sum_if_{i,j}^u(t)\le f_j^{umax}$ |
| (15) | Vessel computing $\sum_jf_{j,k}^v(t)\le f_k^{vmax}$ |
| (20a)-(20c) | Mean-rate stability of MIoT, AAV, and vessel queues |
**Algorithm**: Lyapunov drift-plus-penalty turns $\mathscr P0$ into per-slot problems $\mathscr P1$ subject to (6)-(9), (12), (15); each slot is a heterogeneous-agent Markov game solved by heterogeneous-agent SAC that updates the AAV and vessel agents sequentially.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

You et al. [x] studied joint computation offloading and resource allocation for uncertain maritime MEC through cooperation between autonomous aerial vehicles and vessels. They formulated long-term task-execution-time minimization under uncertain arrivals, single-destination offloading, AAV and vessel computing capacity, and queue-stability constraints. Lyapunov optimization converts the time-average problem into smaller per-slot decisions with virtual queues. Each per-slot problem is represented as a heterogeneous-agent Markov game and solved by a soft actor-critic method that updates the distinct AAV and vessel agents sequentially. Simulations report shorter average completion and response times and a higher edge-computing percentage than five benchmark algorithms across task densities, AAV counts, and bandwidths.

## Problem framing

Maritime IoT (MIoT) compute demand is rising, and AAVs + vessels can supply MEC. But maritime tasks arrive unpredictably and resource availability varies, making efficient offloading/allocation hard. The objective is to minimize total execution time despite this uncertainty.

## System model

- **Actors.** MIoT devices, AAVs, vessels — a cooperative MEC framework.
- **Uncertainty.** Unpredictable task arrivals and varying computational-resource availability handled via [[lyapunov-optimization]] (long-term → short-term constraints).
- **Heterogeneity.** AAVs and vessels differ in actions and resources → modeled as a Markov game ([[stochastic-game]]).

## Method

- **Lyapunov optimization** to decompose into per-slot small-scale problems.
- Reformulate each as a **Markov game** and solve with a **heterogeneous-agent soft actor-critic** (sequentially updates each agent's neural networks) ([[masac]] / [[heterogeneous-agent-rl]]).

## Key findings

- The algorithm outperforms baselines in convergence, execution time, computation rate, offloaded data, and percentage of task execution across various environmental conditions (qualitative; specific curves in the paper).

## Limitations / future work

Simulation-based. The parse's conclusion does not enumerate explicit limitations beyond the modeled assumptions.

## Relation to the corpus

A **DRL** treatment of maritime offloading that contrasts with the optimization-based [[wang-2025-double-edge-samin]] and game-theoretic [[wang-2024-twotier-satellite-marine]] approaches to the same maritime/AAV-vessel setting. Its Lyapunov-then-MG-then-heterogeneous-SAC pipeline echoes the Lyapunov+MASAC pattern in [[qin-2025-bcuav-masac]] and the heterogeneous-agent angle of [[zhang-2025-ssac-mgi-heterogeneous-uav]]. Shares co-authors Ziye Jia / Chao Dong / Qihui Wu / Zhu Han with [[jia-2022-hierarchical-aerial-matching]]. Reinforces [[maritime-mec]] and [[lyapunov-optimization]].

## Raw artifacts

- `raw/sources/Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels/Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels.md`
- Original PDF and extracted figures in the same folder.
