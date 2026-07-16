---
type: source
modeling_card: required
title: "Enhancing AIoT Device Association With Task Offloading in Aerial MEC Networks"
authors: ["Jingxuan Chen", "Peng Yang", "Siqiao Ren", "Zhongliang Zhao", "Xianbin Cao", "Dapeng Wu"]
year: 2023
url: "https://doi.org/10.1109/JIOT.2023.3300011"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, multi-uav-assisted-mec, device-association, computation-offloading, maddpg, uav-trajectory-control, qoe-modeling-mec]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[device-association]]"
  - "[[task-offloading]]"
  - "[[maddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[qoe-modeling-mec]]"
  - "[[air-ground-integrated-network]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[zhao-2022-matd3-multiuav-ec-offloading]]"
  - "[[li-2025-twohop-airground-drl-offloading]]"
created: 2026-06-02
updated: 2026-07-16
---

# Enhancing AIoT Device Association With Task Offloading in Aerial MEC Networks

## Citation

Chen, J., Yang, P., Ren, S., Zhao, Z., Cao, X., & Wu, D. (2023). *Enhancing AIoT Device Association With Task Offloading in Aerial MEC Networks*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3300011. (Manuscript received 15 May 2023; revised 2 July 2023; accepted 19 July 2023; date of publication 1 August 2023; date of current version 25 December 2023 → year 2023.)

## TL;DR

A **distributed multi-UAV MEC** scheme that jointly optimizes **device association**, **task offloading**, and **UAV trajectory** to maximize the **Quality of Experience (QoE)** of cost-sensitive IoT devices (IoTDs) — measured by average task **response time** and IoTD **cache-queue length**. Because the joint problem is combinatorial and non-convex, the paper splits it into three AI-based stages: a greedy **recursive selection and replacement transmission-rate-based (RSRT)** algorithm for IoTD↔station association; a **backtracking task offloading (BTO)** algorithm that recasts offloading as a **0-1 knapsack problem with variable value** and solves it with a pruning-guided backtracking search; and a **multi-agent deep deterministic policy gradient (MADDPG)** controller for UAV movement (each UAV is an agent). Simulations report reduced response time and cache-queue length versus benchmarks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple ground base stations and battery-limited UAV base stations with MEC servers serve queued, indivisible IoT tasks over OFDMA subchannels; UAV positions evolve in three dimensions under probabilistic air-to-ground links and propulsion-energy limits.

**Problem & objective**: Problem (21) is a combinatorial nonconvex joint association, offloading, and trajectory problem, $\max_{\mathcal M,\mathcal A,\mathcal B}\sum_{\tau=0}^{T}\frac{1}{N}\sum_i\mathrm{QoE}_i^p(\tau)\mathrm{QoE}_i^b(\tau)$, maximizing latency and cache-backlog satisfaction.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Device association | $a_{ij,k}(\tau)$ | Binary, $\{0,1\}$ | Assigns IoT device $i$ to server $j$ on subchannel $k$. |
| Task offloading | $\beta_i^t(\tau)$ | Binary, $\{0,1\}$ | Indicates whether queued indivisible task $t$ of device $i$ is offloaded at slot $\tau$. |
| Local processing | $b_i^t(\tau)$ | Continuous, $[0,1]$ | Represents the locally processed portion associated with queued task $t$. |
| UAV movement | $\mathcal M_j(\tau)=\{m_j,\alpha_j,\theta_j\}$ | Continuous within speed and angular bounds | Sets movement distance, azimuth, and pitch for UAV $j$. |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | OFDMA association limits each device to at most one server-subchannel and each server to at most $K$ occupied subchannels as in (9). |
| C2 | Server workload must not exceed $C_j(\tau)$ in (14), and each device's uploaded data must satisfy $\sum_t\beta_i^t(\tau)l_i^t\le\delta T R_i(\tau)$. |
| C3 | UAV movement must retain enough battery to return to its depot, with the maximum step determined by (4). |
| C4 | Offloading and local decisions obey $0\le\beta_i^t(\tau)+b_i^t(\tau)\le1$, while UAV coordinates remain inside horizontal and altitude bounds. |

**Algorithm**: RSRT recursively assigns each device to its highest-rate available server-subchannel, BTO solves the variable-value binary knapsack offloading stage with backtracking and pruning, and MADDPG learns coordinated UAV trajectories.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied joint device association, indivisible-task offloading, and three-dimensional UAV trajectory control in a distributed ground-and-aerial MEC network. They maximized a QoE product combining task-latency satisfaction and remaining cache capacity subject to subchannel, server-compute, upload-volume, movement-energy, and flight-region constraints. Their solution combines recursive rate-based association, a pruned backtracking solver for variable-value binary-knapsack offloading, and MADDPG trajectory control. At 100 IoT devices, the proposed scheme achieved reward improvements of 2.347, 2.126, 1.723, and 1.110 times over FUT, WKMC+NA, NA, and WKMC, respectively, while recording no task loss in the reported 80-to-100-device tests.

## Problem framing

Terrestrial infrastructure cannot keep up with the bandwidth- and QoS-heterogeneous demands of exploding IoTD populations; deploying edge servers **aerially** on UAVs augments ground base stations (GBSs), raises LoS probability (useful in disasters / complex terrain), and adds flexible compute. A **distributed** (vs centralized) MEC architecture reduces latency for geographically dispersed, time-sensitive users and avoids the communication-latency penalty of centralization. The hard part is **dynamically coordinating UAV trajectories and offloading** while respecting UAV-movement energy and MEC compute-capacity limits — and doing so with low enough complexity for real-time operation.

## System model

- **Network.** A distributed MEC network with multiple **ground base stations and UAV base stations**; cost-sensitive IoTDs generate tasks. UAVs act as movable base stations / MEC servers; residual (unassociated) IoTDs' operations are temporarily held in a **cache queue** until they secure communication resources.
- **Decisions.** (i) **Device association** — which station/subchannel each IoTD attaches to; (ii) **offloading decision** — where each task is processed; (iii) **UAV trajectory** — UAV movement, under UAV-movement-energy and MEC-compute-capacity constraints.
- **Objective.** Maximize long-term reward = QoE in terms of **average task response time** and **IoTD cache-queue length**.

## Method

- **RSRT (device association).** A greedy recursive algorithm: each IoTD seeks the station/subchannel giving the **maximal transmission rate**; on contention, the higher-rate IoTD wins the subchannel and others recurse to their next-best option. The problem is NP-hard and lacks optimal substructure, so the greedy + recursion heuristic is used.
- **BTO (task offloading).** The offloading problem is redefined as a **0-1 knapsack problem with variable value**; the solution-space priority order is derived and a **pruning strategy** based on the constraints guides a **backtracking** search to a low-time-complexity offloading strategy.
- **MADDPG (UAV trajectory).** UAV movement is modeled as an MDP and controlled by **MADDPG** (CTDE multi-agent actor-critic); each UAV is an autonomous learning agent generating minimal state data. Hyperparameters were tuned via extensive simulation.

## Key findings

- The integrated RSRT + BTO + MADDPG scheme **reduces both average response time and IoTD cache-queue length** relative to benchmark algorithms across the simulated IoTD populations (e.g., experiments up to 100 IoTDs over 300 time steps) — the paper's stated results. Specific margins are figure-derived; treat exact values as indicative.

## Limitations / future work

Simulation-only; the association and offloading stages are heuristic (greedy / backtracking) rather than provably optimal. The authors note future work on **refining and enhancing the joint optimization** to further improve aerial-MEC efficiency and effectiveness.

## Relation to the corpus

A **multi-UAV-MEC + DRL** entry distinguished by making **device association** a first-class decision alongside offloading and trajectory, and by **hybridizing** combinatorial heuristics (greedy RSRT + knapsack/backtracking BTO) with a learned UAV controller — rather than learning every decision end-to-end. Its **MADDPG** trajectory controller is shared with [[he-2023-fairness-3d-multiuav-maddpg]] and [[zhao-2022-matd3-multiuav-ec-offloading]], and its two-tier ground-plus-aerial offloading recalls [[li-2025-twohop-airground-drl-offloading]]. It introduces the corpus's [[device-association]] concept and grounds [[qoe-modeling-mec]] via its response-time + cache-queue objective.

## Raw artifacts

- `raw/sources/Enhancing_AIoT_Device_Association_With_Task_Offloading_in_Aerial_MEC_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
