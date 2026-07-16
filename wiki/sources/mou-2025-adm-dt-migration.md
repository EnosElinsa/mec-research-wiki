---
type: source
modeling_card: required
title: "Adaptive Digital Twin Migration in Vehicular Edge Computing and Networks"
authors: ["Fangyi Mou", "Jiong Lou", "Zhiqing Tang", "Yuan Wu", "Weijia Jia", "Yan Zhang", "Wei Zhao"]
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3492349"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags:
  - source
  - digital-twin
  - service-migration
  - vehicular-mec
  - deep-reinforcement-learning
  - actor-critic
  - imitation-learning
  - combinatorial-optimization
related:
  - "[[digital-twin]]"
  - "[[service-migration]]"
  - "[[vehicular-mec]]"
  - "[[expert-guided-warm-start-rl]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[yang-2024-taco-human-digital-twin-edge]]"
  - "[[zhao-2025-traj-offload-cache-migration]]"
  - "yuan-wu"
created: 2026-06-03
updated: 2026-07-16
---

# Adaptive Digital Twin Migration in Vehicular Edge Computing and Networks

## Citation
Fangyi Mou, Jiong Lou, Zhiqing Tang, Yuan Wu, Weijia Jia, Yan Zhang, Wei Zhao, "Adaptive Digital Twin Migration in Vehicular Edge Computing and Networks," *IEEE Transactions on Vehicular Technology*, 2025. DOI: 10.1109/TVT.2024.3492349. (Received 29 Feb 2024; accepted 1 Nov 2024; date of publication 7 Nov 2024; date of current version 5 Mar 2025 → year 2025 per the date-of-current-version convention. Corresponding author: Zhiqing Tang. Beijing Normal University / BNU-HKBU UIC + Shanghai Jiao Tong University + University of Macau + University of Oslo.)

## TL;DR
In Vehicular Edge Computing and Networks (VECONs), each moving vehicle is served by a [[digital-twin|digital twin (DT)]] hosted on a roadside-unit (RSU) server; as the vehicle moves, the DT must migrate between RSUs to keep latency low. This paper formulates **adaptive DT migration (ADM)** as a combinatorial optimization that minimizes total cost — communication latency + colocation cost + migration latency — under large-scale, complex DT communications, and solves it with an off-policy actor-critic RL agent bootstrapped by **expert demonstrations / warm-start policies**. On real-world Cologne vehicular-mobility traces, the reported reduction in total migration latency is about 39% on average over baseline algorithms.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Moving vehicles are represented by digital twins hosted on heterogeneous roadside-unit edge servers in a slotted vehicular edge network. Wired inter-RSU paths support twin cooperation, application interaction, synchronization, and migration, while the vehicle-to-twin pair includes a wireless uplink; each RSU has finite CPU, storage, memory, and placement capacity.

**Problem & objective**: Problem 1, an NP-hard binary nonlinear program and infinite-horizon MDP, minimizes total communication, colocation, and migration cost, $\min\sum_{t\in T}\mathcal L(t)$, equivalently maximizing $\eta(\pi)=\mathbb E[\sum_{t=0}^{\infty}\gamma^tr_t]$ with $r_t=-\mathcal L(t)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| DT-to-RSU placement | $\delta_{d,e}(t)$ | binary, $\{0,1\}$ | Whether digital twin $d$ runs on RSU $e$ at slot $t$ |
| Selected RSU | $a_e(t)$ | binary, $\{0,1\}$ | Whether RSU $e$ is selected at slot $t$ |
| Migration action | $a_t$ | discrete, $a_t\in\mathbf E$ | Destination RSU chosen by the ADM policy |
| Migration policy | $\pi(a\mid s;\theta)$ | stochastic policy | Maps RSU and digital-twin state features to a destination |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 14 | Pairwise communication latency satisfies $\mathcal L^{\mathrm{pair}}(t)<W_d$ |
| 15-16 | Exactly one RSU is selected and each digital twin runs on exactly one RSU |
| 17 | $\sum_d\delta_{d,e}(t)\le N_e$ limits the number of twins at RSU $e$ |
| 18 | $\sum_d z_d\delta_{d,e}(t)\le z_e$ enforces storage capacity |
| 19 | $\sum_d m_d\delta_{d,e}(t)\le m_e$ enforces memory capacity |

**Algorithm**: Embed and concatenate RSU and digital-twin features → collect greedy-policy expert demonstrations → pretrain an off-policy actor-critic agent from the demonstration replay buffer → progressively reduce the demonstration proportion while training on online transitions → choose the destination RSU from the learned policy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mou et al. [x] studied adaptive digital-twin migration in vehicular edge computing and networks. They modeled communication latency across twin cooperation, application interaction, and vehicle-to-twin communication together with colocation and migration latency. They formulated an NP-hard binary nonlinear problem that minimizes total cost under latency, unique-placement, RSU-count, storage, and memory constraints, and recast it as an infinite-horizon Markov decision process. Their ADM algorithm uses feature extraction, off-policy actor-critic reinforcement learning, and a warm-start schedule built from greedy-policy expert demonstrations. Experiments on Cologne vehicular-mobility traces report an average total migration-latency reduction of approximately 39% over the evaluated baseline algorithms.

## Problem framing
DTs improve service quality in VECONs but introduce heavy, recurring communication for synchronization. The paper identifies two challenges that prior work neglects: (1) **quantifying the complex latency** of DT communications, which involves three distinct flows — DT-to-DT cooperation, DT-to-user-application interaction, and DT-to-vehicle pair-wise communication; and (2) **making adaptive migration decisions** in a fast-changing environment where high vehicle mobility and varying DT connections leave the RL agent with sparse, partially-unseen states. Traditional heuristics use static strategies and cannot capture long-term reward; plain RL struggles to explore the sparse state space.

## System model
- **Entities:** a set of mobile vehicles **U**, heterogeneous RSU servers **E** (each with bandwidth, CPU, memory, storage, location), and DTs **D** deployed on RSUs in parallel with their vehicles. Requests arrive in discrete time slots.
- **Three communication-latency components:**
  - *Cooperation* `L^coop` — DT-to-DT data synchronization weighted by inter-RSU trust/interaction rate `f(d_i,d_j)`.
  - *Interaction* `L^inter` — DT-to-user-application across RSUs.
  - *Pair-wise* `L^pair` — uplink (vehicle→DT, via a log-rate wireless model) plus downlink (depends on synchronized-data size and shortest-path hop distance).
  - The system communication latency is the **max** of the three: `L^com(t) = max(L^coop, L^inter, L^pair)`.
- **Colocation cost** `L^colo` — resource-contention penalty when multiple DTs share an RSU, proportional to a DT's CPU demand over the serving RSU's workload.
- **Migration latency** `L^mig` — transmission latency (DT size / transfer rate) + propagation latency (coefficient × hop distance); zero when the DT stays put.
- **Objective:** minimize `L(t) = L^com + L^colo + L^mig` over time. The problem is shown to be **NP-hard** by reduction to the set cover problem.

## Method
- **ADM agent** — an off-policy **actor-critic** RL algorithm. A dedicated **feature-extraction network** captures the interdependent large-scale DT-communication features and folds them into the system state.
- **Expert warm-start** — the agent is pre-trained on **expert demonstrations** (the Greedy policy's trajectories are saved as the expert), then the demonstration proportion is progressively diminished during training so the agent converges toward, and past, the expert region. This addresses the sparse-state exploration problem and accelerates training (reported rapid actor-loss convergence in the first ~20 epochs; total loss stabilizes after ~100 epochs).

## Key findings
Reported on real-world Cologne, Germany vehicular-mobility traces (small-scale 500 / large-scale 2000 randomly selected traces):
- **Total migration latency** is reduced by approximately **39% on average** versus baseline algorithms (abstract / introduction).
- **Final training reward ordering:** ADM > DRL-PT > DRL > Greedy, i.e. both the expert pre-training (DRL-PT) and the full warm-start schedule (ADM) improve over plain actor-critic DRL and the Greedy heuristic.
- **Average DT migration latency (one reported table):** Greedy 26, NM (Never Migration) 28, RR (Round-Robin) 67 — illustrating that naive migration policies (always/never/round-robin) are far from cost-minimal.
- **Baselines compared:** Greedy, Never Migration, Round-Robin, Genetic Algorithm, plain DRL (actor-critic), and DRL-PT (expert pre-training only). ADM is reported to approach near-optimal results.

## Limitations / future work
- Evaluated in simulation on mobility traces; no physical RSU/vehicle testbed.
- The expert demonstrations come from the Greedy policy, so warm-start quality is bounded by that heuristic's quality (the paper notes heuristic effectiveness depends on predefined-rule quality).
- Centralized reward computation over all RSU data may become a bottleneck as the network scales (the paper discusses the centralized-vs-distributed variance/latency trade-off but does not fully resolve it).
- Specific numeric values for several results are figure-derived; treat the 39% headline as the paper's stated average rather than a per-scenario guarantee.
- Future work named in the conclusion: integrate DT-based complex task scheduling and edge caching, and explore hybrid local-centralized / global-distributed decision strategies.

## Relation to the corpus
This is a [[service-migration]] design in the [[vehicular-mec]] setting, distinct from the corpus's task-rerouting and offloading-migration work: it migrates the *[[digital-twin|digital twin]]* rather than a task or a service container, and its cost model is dominated by the three-way DT-communication structure. It complements [[yang-2024-taco-human-digital-twin-edge]] (human-digital-twin edge deployment trading accuracy vs cost) and [[zhao-2025-traj-offload-cache-migration]] (service migration vs task rerouting at the MEC edge). Its expert-warm-started actor-critic adds an [[expert-guided-warm-start-rl|imitation-bootstrapped]] data point to the corpus's [[drl-backbones-across-uav-mec-sources|DRL-backbone]] landscape — a contrast to the from-scratch on-policy and off-policy agents elsewhere. Shared authorship with the corpus via yuan-wu.

## Raw artifacts
- Parse: `raw/sources/Adaptive_Digital_Twin_Migration_in_Vehicular_Edge_Computing_and_Networks/full.md`
- Origin PDF: `raw/sources/Adaptive_Digital_Twin_Migration_in_Vehicular_Edge_Computing_and_Networks/72cf2610-67b7-4163-96d0-bba1843ff446_origin.pdf`
- Figures: `raw/sources/Adaptive_Digital_Twin_Migration_in_Vehicular_Edge_Computing_and_Networks/images/`
