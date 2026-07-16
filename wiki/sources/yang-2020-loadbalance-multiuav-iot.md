---
type: source
modeling_card: required
title: "Multi-UAV-Enabled Load-Balance Mobile-Edge Computing for IoT Networks"
authors: ["Lei Yang", "Haipeng Yao", "Jingjing Wang", "Chunxiao Jiang", "Abderrahim Benslimane", "Yunjie Liu"]
year: 2020
url: "https://doi.org/10.1109/JIOT.2020.2971645"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, multi-uav-assisted-mec, load-balancing-uav-mec, task-offloading, differential-evolution, deep-q-network, generalized-assignment-problem]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[load-balancing-uav-mec]]"
  - "[[differential-evolution]]"
  - "[[generalized-assignment-problem]]"
  - "[[deep-q-network]]"
  - "[[task-offloading]]"
  - "[[wang-2019-todetas-deployment-scheduling]]"
  - "[[seid-2021-madrl-multiuav-iot-edge]]"
created: 2026-05-31
updated: 2026-07-16
---

# Multi-UAV-Enabled Load-Balance Mobile-Edge Computing for IoT Networks

## Citation

Yang, L., Yao, H., Wang, J., Jiang, C., Benslimane, A., & Liu, Y. (2020). *Multi-UAV-Enabled Load-Balance Mobile-Edge Computing for IoT Networks*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2020.2971645. (Date of publication 4 Feb 2020; date of current version 12 Aug 2020; year 2020.)

## TL;DR

A multi-UAV-aided MEC system where several UAVs act as MEC nodes serving ground IoT nodes with limited local computing. The goal is to **balance the computing load across UAVs** while honoring coverage and QoS. The design has three parts: a **differential-evolution (DE)** UAV-deployment algorithm, a **generalized-assignment-problem (GAP)** model for IoT-node-to-UAV association (solved by an LP-relaxation + bipartite-rounding near-optimal approximation), and a **deep-reinforcement-learning (DQN)** task-scheduling scheme that minimizes the average task slowdown on each UAV.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAV MEC servers cover heterogeneous ground IoT nodes over orthogonal OFDMA access. Nonuniform offloading demand creates server-load imbalance, while per-UAV queues determine task slowdown after node association and deployment.

**Problem & objective**: P1 is a mixed deployment, assignment, and scheduling problem that minimizes $\min \bar S+\lambda_L\sigma(L_1,\ldots,L_N)+\lambda_C C_{\mathrm{tx}}$, combining average slowdown, load imbalance, and transmission cost.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV deployment | $\mathbf q_n$ | continuous 2-D position | Horizontal location of UAV $n$ |
| IoT-UAV assignment | $x_{k,n}$ | binary | UAV serving IoT node $k$ |
| Task schedule | $\pi_n(t)$ | discrete queue action | Next task executed by UAV $n$ |
| Reference load | $L_n$ | continuous/nonnegative | Aggregate offloading level assigned to UAV $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every IoT node is assigned to exactly one covering UAV |
| C2 | Per-UAV assigned load and node count remain within capacity |
| C3 | IoT-UAV distance and transmission cost satisfy coverage/QoS conditions |
| C4 | Each UAV executes at most one scheduled task at a decision step |
| C5 | UAV deployment coordinates remain inside the service region |

**Algorithm**: Generate reference loads → relax the generalized assignment problem to an LP → construct a bipartite graph and round a min-cost perfect matching → train one DQN scheduler per UAV to reduce task slowdown → evolve all horizontal UAV coordinates with differential evolution under the joint objective → repeat assignment and evaluation for each candidate deployment.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yang et al. [x] studied load-balanced multi-UAV mobile edge computing for IoT networks. They formulated a joint objective combining average task slowdown, per-UAV load imbalance, and transmission cost over UAV deployment, IoT-node assignment, and task scheduling. Node assignment is modeled as a generalized assignment problem and approximated through LP relaxation, bipartite-graph construction, and deterministic rounding. Per-UAV DQN schedulers select tasks to reduce slowdown, while differential evolution updates all UAV positions. Simulations report lower average slowdown and better load balance than the evaluated first-come-first-serve, shortest-job-first, round-robin, and deployment baselines.

## Problem framing

IoT devices have limited power and compute and cannot run high-complexity tasks (AR, face recognition, online games) under latency constraints. UAVs equipped with MEC servers extend coverage to large-scale IoT, but their carrying capacity (compute) is limited, so under non-uniform IoT distributions some UAVs overload while others sit idle. Both **UAV deployment** (affects transmission delay + load balance) and **task scheduling** (affects waiting time) drive MEC efficiency, motivating a joint load-balancing deployment + latency-aware scheduling design.

## System model

- **Architecture.** K ground IoT nodes (heterogeneous "offloading levels") and N UAVs at fixed altitude H; each IoT node connects to exactly one UAV; OFDMA access (intra-link interference neglected); LoS-dominated channel with gain ∝ d⁻².
- **Load-balance metric.** Standard deviation of per-UAV total offloading level (smaller ⇒ more balanced); plus average transmission cost. Combined objective P1 minimizes average task slowdown + weighted load-balance term + weighted transmission cost.
- **Task slowdown.** Ratio of actual completion time (ideal + queueing delay) to ideal completion time (≥ 1).

## Method

- **Reference-load assignment** then **GAP-based node assignment** (P2): each UAV is an agent, each IoT node a task; profit depends on distance/traffic; the integer program is NP-hard, solved by an approximation in three steps — LP relaxation, bipartite-graph construction, and deterministic rounding to an integral min-cost perfect matching. See [[generalized-assignment-problem]].
- **DQN task scheduling** (Algorithm 1): per-UAV deep Q-network minimizing average slowdown; action space reduced to M+1 via sub-step scheduling; reward ∝ −1/(ideal completion time). See [[deep-q-network]].
- **DE-based multi-UAV deployment** (Algorithm 2): population dimension 2N (UAV xy-positions); mutation/crossover/selection iterate to near-optimal positions under the P1 objective. See [[differential-evolution]].

## Key findings

- Simulation in a 400 × 400 m area with 100 IoT nodes and 5 UAVs (B = 1 MHz, H = 100 m, R_c = 100 m, f = 2.4 GHz). The DRL scheduler's reward rises and average slowdown falls with training iterations (read from Figs. 5–6, indicative).
- The DRL-aided scheduler is reported to beat first-come-first-serve, shortest-job-first, and round-robin on average slowdown (Fig. 9, stated qualitatively).
- Average slowdown rises with the Poisson task-arrival rate as expected under limited per-UAV capacity (Figs. 7–8, indicative).

## Limitations / future work

The parse's conclusion does not enumerate explicit quantitative future-work targets: `not in parse`. All results are simulation-based; numbers in Figs. 4–10 are MinerU-rendered curves and are treated as indicative, not exact.

## Relation to the corpus

An early (2020) **load-balance-first** multi-UAV-MEC entry that grounds the [[load-balancing-uav-mec]] concept and contributes the new [[generalized-assignment-problem]] page. It pairs a classical metaheuristic ([[differential-evolution]], shared with [[wang-2019-todetas-deployment-scheduling]]'s two-layer DE deployment) with single-agent [[deep-q-network|DQN]] scheduling — a precursor to the later multi-agent clustered-IoT-edge offloading of [[seid-2021-madrl-multiuav-iot-edge]]. Reinforces [[multi-uav-assisted-mec]] and [[task-offloading]].

## Raw artifacts

- `raw/sources/Multi-UAV-Enabled_Load-Balance_Mobile-Edge_Computing_for_IoT_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
