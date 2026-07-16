---
type: source
modeling_card: required
title: "Multi-Agent Deep Reinforcement Learning for Task Offloading and Resource Allocation in Multi-UAV Enabled IoT Edge Network"
authors: ["Abegaz Mohammed Seid", "Gordon Owusu Boateng", "Bruce Mareri", "Guolin Sun", "Wei Jiang"]
year: 2021
url: "https://doi.org/10.1109/TNSM.2021.3096673"
venue: "IEEE Transactions on Network and Service Management (IEEE TNSM)"
tags: [source, multi-uav-assisted-mec, multi-agent-drl, maddpg, task-offloading, resource-allocation, stochastic-game, air-ground-integrated-network]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[stochastic-game]]"
  - "[[task-offloading]]"
  - "[[air-ground-integrated-network]]"
  - "[[energy-latency-tradeoff]]"
  - "[[dynamic-uav-clustering]]"
created: 2026-05-31
updated: 2026-07-16
---

# Multi-Agent Deep Reinforcement Learning for Task Offloading and Resource Allocation in Multi-UAV Enabled IoT Edge Network

## Citation

Seid, A. M., Boateng, G. O., Mareri, B., Sun, G., & Jiang, W. (2021). *Multi-Agent Deep Reinforcement Learning for Task Offloading and Resource Allocation in Multi-UAV Enabled IoT Edge Network*. **IEEE Transactions on Network and Service Management**. DOI: 10.1109/TNSM.2021.3096673. (Manuscript received October 22, 2020; date of publication July 12, 2021; date of current version December 9, 2021 → year 2021.)

## TL;DR

A **clustered multi-UAV** system provides computing **task offloading and resource allocation** to IoT devices in an aerial-to-ground (A2G) IoT edge network, where the ground edge BS may be overloaded or disaster-disabled. The paper proposes a **multi-agent DRL (MADRL)** approach to minimize overall long-term network **computation cost (energy + delay)** under QoS requirements, formulating the problem as a **stochastic game** (an extension of an MDP) with stochastic, time-varying UAV channel strength and dynamic resource requests. It is solved with **MADDPG** under centralized-training/decentralized-execution. Reported gains (verbatim from the abstract): average cost reduced by **38.643%** and **55.621%**, and reward increased by **58.289%** and **85.289%**, versus single-agent DRL and heuristic schemes, respectively.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: IoT devices in clustered multi-UAV aerial edge networks choose local execution or offloading to a base station or UAV computational node over stochastic channels and dynamic task requests.

**Problem & objective**: The resource-control formulation minimizes total computation cost, $\min_{\chi,\mathcal F,\mathcal P}\mathcal Z_{lx}(t)$, combining energy and delay across agents.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading or association | $\chi_{lx}^m(t)$ | binary or ternary, $\{-1,0,1\}$ | Select local execution or computational node $x$ |
| Computation resource | $f_{lx}(t)$ | discrete or continuous, bounded by $F_x^{max}$ | CPU resource assigned to device $l$ |
| Transmission power | $p_{lx}(t)$ | discrete or continuous, bounded by $P_x^{max}$ | Radio power for the selected node |
| Subchannel allocation | $s_x^m(t)$ | binary | Indicates available and allocated resource block |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Offloading, subchannel, and resource-block indicators are binary. |
| C2 | Each device selects at most one computational node: $\sum_x\alpha_{lx}(t)\leq1$. |
| C3 | A node's resource block is allocated consistently: $\sum_xs_x^m(t)=1$ in the parsed formulation. |
| C4 | Computation capacity is bounded: $\sum_xf_{lx}(t)\leq F_x^{max}$. |
| C5 | Transmission power is bounded: $\sum_xp_{lx}(t)\leq P_x^{max}$. |
| C6 | QoS must meet the threshold: $\gamma_{lx}(t)\geq\bar\gamma(t)$, with fairness $\Upsilon^u(t)\in[0,1]$. |

**Algorithm**: Cast the dynamic resource problem as a stochastic game and train MADDPG with centralized critics and decentralized actors, joint rewards, replay, and local observations containing task, SINR, power, and UAV status.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Seid et al. [x] formulate cooperative task offloading in a clustered multi-UAV edge network as a stochastic game. The MINLP minimizes energy, delay, and allocation cost through offloading choices, CPU resources, transmit powers, channel indicators, QoS, capacity, power, and fairness constraints. MADDPG uses centralized training with decentralized execution so each IoT agent can act from local task, SINR, power, and UAV-status observations. Against single-agent and heuristic baselines, the reported scheme reduces average cost by 38.643% and 55.621% and raises reward by 58.289% and 85.289%.

## Problem framing

IoT/edge UEs are constrained in compute and energy; a local BS+MEC server cannot serve massive simultaneous requests, and the ground BS is vulnerable to traffic spikes and disasters. UAVs as aerial base stations (ABSs) extend coverage and offload intensive tasks. Choosing the offloading node per time slot, with complex associations and high waiting times, is the core challenge; the paper argues a cooperative multi-agent (rather than single-agent) formulation fits the distributed observation structure.

## System model

- **Architecture.** Clustered multi-UAV ABSs serving IoT devices/UEs in an A2G network; channel strength is stochastic time-varying and resource requests are dynamic.
- **Objective.** Minimize long-term computation cost in terms of energy and delay while satisfying heterogeneous QoS.
- **Formulation.** Cast as a **stochastic game** — a natural extension of the MDP — where each agent decides from local real-time observations and current strategies (resource selection, task-offloading choice) and shares information with other agents.

## Method

- **MADDPG** (multi-agent deep deterministic policy gradient) with **centralized training, decentralized execution** ([[centralized-training-decentralized-execution]]) lets the multiple agents maximize long-term reward (lower computation cost, effective allocation) while reducing training cost.
- Contributions (per parse): (1) design a multi-UAV IoT edge network for cooperative dynamic offloading + allocation; (2) MADRL model of the cooperative offloading/allocation/association problem; (3) stochastic-game problem formulation; (4) MADDPG solution.

## Key findings

- Against single-agent DRL and heuristic baselines, the MADRL/MADDPG scheme reduces average costs by **38.643%** and **55.621%** and raises reward by **58.289%** and **85.289%** respectively (verbatim from the abstract).

## Limitations / future work

The captured parse does not enumerate explicit quantitative future-work targets in the conclusion section → `not in parse`.

## Relation to the corpus

A **MADDPG cooperative multi-UAV MEC** entry that sits with [[zhao-2022-matd3-multiuav-ec-offloading]] (MATD3), [[he-2023-fairness-3d-multiuav-maddpg]] (fairness MADDPG), [[chang-2022-marl-multiuav-trajectory]] (MARL trajectory), and [[wang-2021-maddpg-multiuav-trajectory]] (MADDPG trajectory) in the multi-agent UAV-MEC family. It is one of the **earlier** (2021) examples of casting multi-UAV offloading as a [[stochastic-game]] and grounds the standalone [[maddpg]] concept page. Distinct from the other MADDPG papers by venue, authors (UESTC/DFKI), and its clustered-IoT-edge framing.

## Raw artifacts

- `raw/sources/Multi-Agent_DRL_for_Task_Offloading_and_Resource_Allocation_in_Multi-UAV_Enabled_IoT_Edge_Network/full.md`
- Original PDF (`589beaa0-1417-4773-b24d-ced75e7f14e8_origin.pdf`) and extracted figures (`images/`) in the same folder.
