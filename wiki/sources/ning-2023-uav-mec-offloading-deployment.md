---
type: source
title: "Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing"
authors: ["Zhaolong Ning", "Yuxuan Yang", "Xiaojie Wang", "Lei Guo", "Xinbo Gao", "Song Guo", "Guoyin Wang"]
year: 2023
url: "https://doi.org/10.1109/TMC.2021.3129785"
venue: "IEEE Transactions on Mobile Computing"
modeling_card: required
tags: [source, uav-mec, task-offloading, server-deployment, stochastic-game, nash-equilibrium, dynamic-environment]
related:
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[stochastic-game]]"
  - "[[nash-equilibrium]]"
  - "[[potential-game]]"
  - "[[wang-2019-todetas-deployment-scheduling]]"
  - "[[pervez-2024-acm-multiuav-mec]]"
  - "[[zhaolong-ning]]"
  - "[[xiaojie-wang]]"
  - "[[lei-guo]]"
created: 2026-07-07
updated: 2026-07-16
---

# Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing

## Citation

Ning, Z., Yang, Y., Wang, X., Guo, L., Gao, X., Guo, S., & Wang, G. (2023). *Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2021.3129785.

## TL;DR

Models a multi-UAV MEC network in which users decide whether to compute locally or offload to a UAV-MEC server, while UAVs choose hovering locations as mobile edge-server deployment decisions. The paper decomposes the system-wide computation-cost minimization into two stochastic games: one for user offloading and one for UAV location selection. Probability-based learning algorithms seek pure-strategy Nash equilibria for the two games, and a chess-like asynchronous update alternates between them.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ user devices generate computation tasks with time-varying probabilities and are served by $M$ UAV-MEC servers. A user either computes locally or offloads to one UAV, while each UAV chooses one of $L$ discrete hovering locations; uplink channels include Rician fading and co-server interference is avoided with orthogonal frequency resources.

**Problem & objective**: Jointly choose user strategies $\mathbf s$ and UAV locations $\mathbf a$ to minimize the system-wide weighted delay and energy cost, $\min_{\mathbf s,\mathbf a}\sum_i Z_i(\mathbf s,\mathbf a)$, under dynamic task arrivals and coupled communication and computation costs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UE processing choice | $s_i$ | discrete, $\{0\}\cup\mathcal M$ | Local computing when $s_i=0$, otherwise offload to UAV $s_i$ |
| UAV hovering choice | $a_j$ | discrete, $\mathcal L$ | Candidate location selected by UAV $j$ |
| Strategy probability | $\mathbf X_i,\mathbf Y_j$ | probability vectors | Learned selection probabilities for UE and UAV strategies |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| 9, UE | Each UE chooses at most one local or edge-processing option |
| 9, UAV | Each UAV selects exactly one candidate hovering location |
| Capacity | UAV $j$ can process at most $\bar D_j$ data in a period; the UAR mechanism redirects rejected UEs to local computing |
| Dynamic state | Task-generation indicators and Rician channel gains follow the stochastic environment used by both games |

**Algorithm**: Decompose the joint problem into a UE offloading game and a UAV location-selection game, shown respectively to be weighted and exact potential games with pure-strategy equilibria. Run probability-based strategy-selection learning for each game, and alternate the UE and UAV equilibrium updates in a chess-like asynchronous loop that accepts a new profile only when it improves the corresponding computation costs.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ning et al. [x] studied the coupled selection of computation-offloading strategies and UAV-MEC server locations under time-varying task arrivals. They formulated a system-wide weighted delay and energy objective and decomposed it into stochastic games for user processing choices and UAV hovering locations. The user game is equivalent to a weighted potential game and the UAV game to an exact potential game, enabling probability-based learning toward pure-strategy Nash equilibria. A chess-like asynchronous algorithm alternates the two learned strategy profiles and retains updates that reduce cost. In the Melbourne data-driven evaluation, the adaptive UAV-MEC design converged in about 25 outer iterations and reduced system-wide computation cost by 50% relative to fixed edge-server locations.

## Problem framing

The paper argues that offloading and server deployment are tightly coupled: changing UAV locations changes user channel conditions and therefore offloading choices, while user offloading choices determine UAV computation load. It targets a dynamic environment in which users generate tasks with time-varying probabilities and the objective is to reduce a system-wide computation cost combining delay and energy terms.

## System model

- Multiple UEs and multiple UAVs operate over a discretized service area; each UAV hovers at one candidate location and acts as a UAV-MEC server.
- Each UE either computes locally or chooses one UAV for edge computing.
- UE tasks arrive probabilistically at each period, with per-UE task-generation probability.
- UE cost combines transmission/computation delay and energy; UAV cost combines average processing delay and edge-computing energy for the UEs it serves.
- A UAV availability response mechanism rejects overload by assigning zero computation capability to some UEs when a UAV's data threshold is exceeded, causing those UEs to fall back to local computing.

## Method

The optimization is split into two game layers:

- **UE computation-offloading game:** with UAV locations fixed, users select local computing or a UAV server. The paper shows the UE game is equivalent to a weighted potential game.
- **UAV location-selection game:** with user strategies fixed, UAVs select hovering locations. The paper transforms this game into an exact potential game.
- **Learning algorithms:** UEPSSL and UAVPSSL update strategy-selection probabilities using received rewards and are proved to converge to pure-strategy NE under the stated dynamic-game assumptions.
- **Chess-like asynchronous update:** alternates UE and UAV updates, accepting strategy profiles only when the system-wide computation cost improves.

## Key findings

- The proposed learning algorithms converge in the simulation setting, while a short-sighted updating baseline does not converge under the dynamic environment because it reacts to instantaneous utilities.
- In the Melbourne-CBD data-driven scenario, UAV-MEC with adaptive deployment lowers the system-wide computation cost relative to fixed edge-server placement; the parse reports a roughly 50% reduction against the fixed-EC baseline in its Fig. 9 discussion.
- The UAV-MEC result grows more gently with the number of UEs than the fixed-EC baseline, which the paper uses as evidence of robustness under scaling.
- Increasing UAV data thresholds reduces cost until the threshold is high enough to satisfy all UEs' edge-computing requests; beyond that point additional threshold does not improve performance in the studied scenario.

## Limitations / future work

The model discretizes UAV hovering locations and omits signaling overhead, bandwidth overhead, and downlink result transmission. The parse uses simulation over a real-world Melbourne CBD data source but does not report hardware deployment. Publication venue/year are verified by DOI metadata because the parse itself does not include a clean venue line.

## Relation to the corpus

This source adds a game-theoretic server-deployment counterpart to the UAV-MEC offloading line. It is closer to [[pervez-2024-acm-multiuav-mec]] than to pure DRL trajectory papers: both put game-theoretic offloading inside a broader optimization loop. It also complements [[wang-2019-todetas-deployment-scheduling]], which handles UAV deployment with differential evolution and task scheduling, by making deployment and offloading mutually reactive through stochastic games.

## Raw artifacts

- Parse: `raw/sources/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing.md`
- Origin PDF: `raw/sources/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing.pdf`
- Figures: `raw/sources/Dynamic Computation Offloading and Server Deployment for UAV-Enabled Multi-Access Edge Computing/images/`
