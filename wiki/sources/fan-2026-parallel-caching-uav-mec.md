---
type: source
title: "Multi-Task Parallel Execution-Oriented Content Caching, Computation Offloading and Channel Allocation in UAV-Assisted MEC Network"
authors: ["Chaoqiong Fan", "Jichao Zhan", "Jing Wang", "Shiwen Mao"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3674329"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, uav-mec, caching, task-offloading, dqn, regret-minimization-learning, parallel-processing]
related:
  - "[[parallel-vs-serial-processing]]"
  - "[[service-caching-mec]]"
  - "[[task-offloading]]"
  - "[[stochastic-game]]"
  - "[[regret-minimization-learning]]"
  - "[[computational-task-caching]]"
  - "[[zhao-2024-caching-service-placement-uav]]"
created: 2026-07-07
updated: 2026-07-16
---

# Multi-Task Parallel Execution-Oriented Content Caching, Computation Offloading and Channel Allocation in UAV-Assisted MEC Network

## Citation

Fan, C., Zhan, J., Wang, J., & Mao, S. (2026). *Multi-Task Parallel Execution-Oriented Content Caching, Computation Offloading and Channel Allocation in UAV-Assisted MEC Network*. **IEEE Transactions on Mobile Computing**, 25(8), 12591-12607. DOI: 10.1109/TMC.2026.3674329. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Introduces a UAV-assisted MEC task model where multiple MD tasks can be processed in parallel instead of serialized. The paper jointly optimizes content caching, computation offloading, and channel allocation through a two-layer RLTL scheme: lower-layer DQN handles each UAV's caching/offloading decisions, while upper-layer [[regret-minimization-learning]] handles inter-UAV channel allocation as a [[stochastic-game]].

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: MEC-equipped UAVs serve mobile devices outside terrestrial coverage while a remote GBS stores all content and offers stronger computation. Receive, compute, and result-transmission stages of compatible tasks may overlap, but caching, execution location, and reused A2G channels jointly determine service duration.

**Problem & objective**: Minimize each UAV's parallel service duration, $\min_{\mathbf A,\mathbf B,\mathbf C}T_n$ for every $n\in\mathcal N$, over binary content caching, UAV-versus-GBS computation, and channel allocation.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Content caching | $a_{n,k}$ | binary | Whether UAV $n$ caches content $k$ |
| Computation mode | $b_{n,m}$ | binary | Whether task $m$ executes at UAV $n$ rather than the GBS |
| A2G channel | $c_{n,l}$ | binary, one-hot | Whether UAV $n$ uses channel $l$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Cached content fits UAV storage: $\sum_k a_{n,k}v_k\leq V_n$. |
| C2 | Each UAV selects exactly one A2G channel: $\sum_l c_{n,l}=1$. |
| C3 | Caching, computation-mode, and channel indicators are binary. |
| C4 | Task-stage start times respect receive, compute, and transmit precedence while allowing conflict-free stages to overlap. |
| C5 | The task class induced by cached content determines which tasks are locally executable and which require GBS retrieval. |

**Algorithm**: Decompose the system problem into per-UAV caching and computation and a coupled inter-UAV channel game. Use a DQN lower layer to minimize the local completion time implied by parallel task-stage scheduling, then use regret-minimization learning in the partially observable upper layer to approach a correlated-equilibrium channel allocation; alternate the two layers in RLTL.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Fan et al. [x] investigated parallel execution in UAV-assisted MEC by jointly controlling cached content, UAV-versus-GBS computation, and inter-UAV channel allocation. They minimized each UAV's service duration over binary caching, offloading, and one-hot channel decisions subject to storage capacity and noninterruptible execution precedence and resource conditions. RLTL uses a DQN lower layer for intra-UAV caching and offloading and a regret-minimization upper layer for the partially observable channel-allocation game. Simulations reported 12.6% and 21.6% latency reductions from parallel execution in sparse and dense device cases, and RLTL performed close to exhaustive search.

## Problem framing

Most UAV-MEC service-duration models assume tasks are effectively executed one by one. The parse argues that UAV servers can simultaneously receive data, transmit results, and compute different tasks if resource conflicts are avoided, so serial execution leaves latency gains unused. The hard part is that content caching, local-vs-GBS offloading, and A2G channel reuse are coupled.

## System model

Multiple UAVs with lightweight MEC servers serve associated mobile devices outside GBS coverage. A remote GBS stores all content and has stronger computation, while each UAV caches only a subset of popular contents and has limited CPU/storage. MD tasks require content sets, CPU cycles, and result return; tasks are classified by whether required contents are cached at the associated UAV and whether they should execute at the UAV or be forwarded to the GBS.

## Method

The paper defines a parallel execution paradigm that separates MDs into task classes whose receive/compute/transmit stages can overlap. It decomposes the joint optimization into intra-UAV content caching plus computation offloading and inter-UAV channel allocation. The RLTL architecture uses a DQN-based lower layer for large local action spaces and an RM-based upper layer that targets correlated-equilibrium channel allocation under partial observability.

## Key findings

- Fig. 8 reports that parallel execution reduces average service duration relative to serial execution, with the parsed examples showing 12.6% latency reduction in a sparse MD case and 21.6% in a dense MD case.
- Fig. 9 reports that proactive UAV content caching reduces service duration relative to no caching, with a wider gap as MD density rises or fewer UAVs are available.
- Fig. 10 reports that hybrid UAV-GBS computing lowers task-completion latency versus full GBS offloading and full UAV-local computing.
- The proposed RLTL method is reported to perform close to exhaustive search and above DQN-greedy, Q-learning/RM, and Stackelberg-game learning baselines in Fig. 11.

## Limitations / future work

The paper evaluates through simulations. The conclusion states future work will extend the parallel execution framework to task priorities and dependencies, and explore meta-RL and decentralized multi-agent coordination for dynamic and uncertain environments.

## Relation to the corpus

This source broadens the caching track from service/content placement into execution scheduling: [[service-caching-mec]] determines whether required content is already at the UAV, while [[parallel-vs-serial-processing]] explains why overlapping receive/compute/transmit stages changes service duration. It complements [[zhao-2024-caching-service-placement-uav]] and [[gao-2024-service-experience-cache-uav]] by optimizing content caching together with offloading and channel allocation, and it adds [[regret-minimization-learning]] to the wiki's game-learning vocabulary.

## Raw artifacts

- `raw/sources/Multi-Task Parallel Execution-Oriented Content Caching- Computation Offloading and Channel Allocation in UAV-Assisted MEC Network/Multi-Task Parallel Execution-Oriented Content Caching- Computation Offloading and Channel Allocation in UAV-Assisted MEC Network.md`
- Original PDF and extracted figures (`images/`) in the same folder.
