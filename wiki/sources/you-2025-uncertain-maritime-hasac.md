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
updated: 2026-07-16
---

# Joint Computation Offloading and Resource Allocation for Uncertain Maritime MEC via Cooperation of AAVs and Vessels

## Citation

You, J., Jia, Z., Dong, C., Wu, Q., & Han, Z. (2025). *Joint Computation Offloading and Resource Allocation for Uncertain Maritime MEC via Cooperation of AAVs and Vessels*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3581970.

## TL;DR

Maritime MEC via cooperation of autonomous aerial vehicles (AAVs) and vessels, minimizing total task execution time under **uncertain** task arrivals. **Lyapunov optimization** converts the long-term constraints into per-slot short-term ones, yielding small-scale problems; the heterogeneity of AAV/vessel actions and resources is then captured as a **Markov game (MG)**, solved by a **heterogeneous-agent soft actor-critic** that sequentially updates the agents' networks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Maritime IoT devices with uncertain task arrivals offload to cooperative autonomous aerial vehicles and vessels that have heterogeneous mobility, communication, and computing resources. Queues and long-term resource budgets evolve across slots.

**Problem & objective**: A stochastic long-term control problem minimizes total task-execution time, $\min \limsup_{T\to\infty}\frac{1}{T}\sum_{t,k}T_k(t)$, under queue stability and time-average resource constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading destination | $x_{k,j}(t)$ | discrete/binary | AAV or vessel selected for task $k$ |
| Transmit resource | $p_k(t),b_k(t)$ | continuous, bounded | Uplink power and bandwidth allocated to a task |
| Computing allocation | $f_{k,j}(t)$ | continuous, nonnegative | Processor resource assigned by server $j$ |
| AAV movement | $\Delta\mathbf q_j(t)$ | continuous bounded action | Aerial server trajectory update |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Task assignment and processing conserve each arrival workload |
| C2 | Device and server queues remain mean-rate stable |
| C3 | Per-slot radio and computing allocations stay within capacity |
| C4 | Time-average AAV and vessel resource or energy budgets are respected |
| C5 | Heterogeneous actions remain within each agent's movement and resource domain |

**Algorithm**: Introduce virtual queues for long-term constraints → apply Lyapunov drift-plus-penalty to obtain per-slot problems → formulate each slot as a heterogeneous-agent Markov game → let AAV and vessel SAC actors select their distinct actions → update agent networks sequentially and advance real and virtual queues.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

You et al. [x] studied joint computation offloading and resource allocation for uncertain maritime MEC through cooperation between autonomous aerial vehicles and vessels. They formulated long-term task-execution-time minimization under uncertain arrivals, queue stability, and heterogeneous communication and computing constraints. Lyapunov optimization converts the time-average problem into smaller per-slot decisions with virtual queues. Each per-slot problem is represented as a heterogeneous-agent Markov game and solved by a soft actor-critic method that updates the distinct AAV and vessel agents sequentially. Simulations report lower execution time and improved computation rate, offloaded data, and task-completion ratio relative to the evaluated baselines.

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

- `raw/sources/Joint_Computation_Offloading_and_Resource_Allocation_for_Uncertain_Maritime_MEC_via_Cooperation_of_AAVs_and_Vessels/full.md`
- Original PDF and extracted figures in the same folder.
