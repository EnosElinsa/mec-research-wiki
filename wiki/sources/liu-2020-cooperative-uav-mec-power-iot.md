---
type: source
title: "Cooperative Offloading and Resource Management for UAV-Enabled Mobile Edge Computing in Power IoT System"
authors: ["Yi Liu", "Shengli Xie", "Yan Zhang"]
year: 2020
url: "https://doi.org/10.1109/TVT.2020.3016840"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-mec, cooperative-offloading, resource-management, deep-reinforcement-learning, power-iot, semi-markov]
related:
  - "[[mobile-edge-computing]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[deep-q-network]]"
  - "[[semi-markov-decision-process]]"
  - "[[small-cell-mec]]"
  - "[[seid-2021-madrl-multiuav-iot-edge]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
created: 2026-05-31
updated: 2026-07-16
modeling_card: required
---

# Cooperative Offloading and Resource Management for UAV-Enabled Mobile Edge Computing in Power IoT System

## Citation

Liu, Y., Xie, S., & Zhang, Y. (2020). *Cooperative Offloading and Resource Management for UAV-Enabled Mobile Edge Computing in Power IoT System*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2020.3016840.

## TL;DR

A **cooperative UAV-enabled MEC** network for the power Internet of Things, where UAVs act as edge servers that not only serve local devices in their own small-cell but can **help neighboring UAVs** execute computation tasks. A cooperative offloading scheme (with interference mitigation from UAVs to devices) maximizes the network's long-term utility over offloading decisions and resource-management policies. Because device demands and channels are random and time-varying, the problem is cast as a **semi-Markov process** and solved with deep-reinforcement-learning algorithms in both **centralized** and **distributed** frameworks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A time-slotted cooperative UEC network has ground devices in UAV small-cells, hovering UAV edge servers, and a BS or edge server; a task can be processed locally, by a neighboring UAV, or at the BS.

**Problem & objective**: Choose a collaboration mode and communication/computation allocations to maximize long-term network utility, $\max_{\beta,\mathbf f,\Phi}\lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^{T}\sum_{k=1}^{K}U_k(t)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Collaboration mode | $\beta_k(t)$ | binary in $\{0,1\}$ | Whether UAV $k$ provides cooperative service or requests help |
| Computing rates | $\mathbf f_k(t)$ | continuous, nonnegative and capacity-bounded | CPU rates assigned to local, cooperative-UAV, and BS execution |
| Offloading durations | $\Phi_k(t)$ | continuous, nonnegative | Transmission durations for device, UAV, and BS paths |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | The communication durations fit one slot, $\sum\tau_{n_k,k}+\sum\tau_{k,j}+\tau_k^{BS}\leq\tau$. |
| C2 | Every device demand is offloaded within available link rates, as in the communication-capacity inequalities. |
| C3 | Executed bits fit local and cooperative computing capacities, including $\sum d_{n_k}\leq\sum\tau f$. |
| C4 | The collaboration decision remains discrete, $\beta_k(t)\in\{0,1\}$. |

**Algorithm**: Model stochastic demand and channel states as a semi-Markov process; solve centrally with two-phase DRL and state-representation learning, or distribute Q-value-transfer DQN policies across UAVs.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] proposed a cooperative UAV-enabled MEC architecture for power IoT in which each UAV serves its small-cell and can execute tasks from neighboring cells. The formulation jointly selects a collaboration mode, offloading durations, and computation rates to maximize long-term communication and computation utility under stochastic demands and time-varying channels. A centralized two-phase DRL method learns a compact state representation, while the distributed method transfers neighboring Q values so that UAVs can coordinate without a central information collector. Numerical comparisons show the centralized cooperative policy obtains the highest utility, and both cooperative policies reduce service drops as more UAVs participate. The study established an early semi-Markov DRL reference for cooperative multi-UAV MEC resource management.

## Problem framing

Remote power-IoT areas lack computation services; UAV-enabled MEC can supply them, but the service is constrained by UAV capacities and the distinct demands of power-IoT applications. The objective is to maximize long-term network utility under stochastic channel conditions and demand profiles, while mitigating UAV-to-device interference and allowing UAVs to cooperate rather than work in isolation.

## System model

- **Actors.** K UAVs (UAV-enabled edge computing, "UEC" network), each covering a small-cell with N_k devices; a base station.
- **Links.** Device→UAV, UAV→UAV (cooperation), and UAV→BS data rates, each modeled with state-transition probabilities over a channel-rate state space.
- **Decisions.** Per slot, computation-offloading decisions and resource management (local compute vs cooperative compute vs BS), with utility combining communication and computation terms.
- **Stochasticity.** Random device demands and time-varying channels make the long-term utility maximization a **semi-Markov process**.

## Method

- A **two-phase DRL-based offloading algorithm** for the centralized problem using representation learning.
- A **distributed DRL-based algorithm** using a Q-value transferring method, so UAVs need not send all information to the central operator.
- Both target the long-term utility of the cooperative UEC network.

## Key findings

- The proposed centralized and distributed DRL schemes achieve **better performance than non-cooperative UAV edge computing** methods (stated qualitatively; the figures report service drop rate vs UAV computation capability).
- Allowing UAVs to assist neighboring small-cells improves utility relative to isolated per-UAV operation.

## Limitations / future work

Simulation-only; explicit future work is not stated beyond the centralized/distributed comparison. Focused on the power-IoT setting with semi-Markov demand/channel dynamics. DOI date of publication 17 Aug 2020 / date of current version 22 Oct 2020 → year 2020.

## Relation to the corpus

An early **cooperative multi-UAV MEC + DRL** entry where UAVs help each other compute, adjacent to [[seid-2021-madrl-multiuav-iot-edge]] (clustered multi-UAV IoT-edge offloading as a stochastic game with MADDPG) and [[yu-2020-uav-ec-collaborative-offloading]] (collaborative UAV + edge-cloud offloading). It anchors the **power-IoT** application within the broader [[multi-uav-assisted-mec]] track and reinforces [[task-offloading]], [[deep-q-network]], and [[small-cell-mec]]. Co-author [[shengli-xie]] (Guangdong University of Technology) also appears in the CMOP-evolutionary lineage.

## Raw artifacts

- `raw/sources/Cooperative_Offloading_and_Resource_Management_for_UAV-Enabled_Mobile_Edge_Computing_in_Power_IoT_System/full.md`
- Original PDF and extracted figures in the same folder.
