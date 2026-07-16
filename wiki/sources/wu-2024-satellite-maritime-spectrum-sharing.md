---
type: source
modeling_card: required
title: "Intelligent Spectrum Sharing Strategy for Integrated Satellite-Maritime Heterogeneous Mobile Networks"
authors: ["Ruiwen Wu", "Zongwang Li", "Zhuochen Xie", "Xuwen Liang"]
year: 2024
url: "https://doi.org/10.1109/TVT.2023.3343720"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, non-terrestrial-network, maritime-mec, spectrum-sensing-channel-selection, pomdp, dueling-dqn, ddqn]
related:
  - "[[non-terrestrial-network]]"
  - "[[maritime-mec]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[pomdp]]"
  - "[[dueling-dqn]]"
  - "[[ddqn]]"
  - "[[deep-q-network]]"
  - "[[overlay-underlay-spectrum-access]]"
  - "[[wang-2024-twotier-satellite-marine]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[zhang-2025-vnf-sgin-dql]]"
created: 2026-06-02
updated: 2026-07-16
---

# Intelligent Spectrum Sharing Strategy for Integrated Satellite-Maritime Heterogeneous Mobile Networks

## Citation

Wu, R., Li, Z., Xie, Z., & Liang, X. (2024). *Intelligent Spectrum Sharing Strategy for Integrated Satellite-Maritime Heterogeneous Mobile Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2023.3343720. (Manuscript received 29 June 2023; revised 11 November 2023; accepted 11 December 2023; date of publication 18 December 2023; date of current version 16 May 2024 → year 2024.)

## TL;DR

A DRL-based **spectrum-sharing** strategy for an integrated satellite-maritime network built on the **VHF Data Exchange System (VDES)**, where a satellite component (**VDE-SAT**) and a terrestrial maritime component (**VDE-TER**) share the same channels. The satellite centrally allocates shared channels to maximize the combined VDE-TER + VDE-SAT throughput (with task-priority weighting for VDE-SAT) while respecting ITU-derived uplink/downlink **interference constraints**. Because the satellite cannot fully observe channel states, the problem is modeled as a **Partially Observable Markov Decision Process (POMDP)** and solved with **SCA-D3QN**, a Double + Dueling DQN architecture, deployed offline-train / online-implement. Simulations report higher throughput and stability than benchmark methods.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: VDE-SAT satellite stations and VDE-TER maritime networks share VDES frequency and time resources, while a satellite observes channel occupancy and task queues only partially and must protect both uplink and downlink interference thresholds.

**Problem & objective**: The spectrum-sharing problem maximizes weighted combined throughput, $\max_{U}\sum_i(D_i^{TER}+D_i^{SAT})$, subject to uplink and downlink interference limits.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Share-channel allocation | $U$ | subset or binary allocation | Share channels assigned to VDE-SAT |
| Logical-channel mapping | $A_t$ | discrete matrix | Maps tasks to share and logical channels |
| Task priority order | $\pi_t$ | discrete permutation | Orders VDE-SAT transmission tasks |
| Time-slot assignment | $\tau_{i,j}$ | continuous or discrete fraction | Busy or reserved share-channel slots |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Downlink interference is bounded: $\Phi_{DIC}^i\leq\Phi_{DIC}^{threshold}$. |
| C2 | Uplink interference is bounded: $\Phi_{UIC}^i\leq\Phi_{UIC}^{threshold}$. |
| C3 | Allocation respects VDES share-channel and logical-slot structure. |
| C4 | Satellite decisions use only the partially observed channel and task history. |

**Algorithm**: Model the satellite allocator as a POMDP, encode channel and task history in an LSTM observation state, and train an SCA-D3QN policy with Double DQN target evaluation and Dueling value and advantage streams for share-channel allocation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] formulate VDES spectrum sharing between satellite and maritime terrestrial systems as a partially observable throughput-allocation problem. The satellite chooses shared channels, logical time mappings, and task ordering while satisfying ITU-derived downlink and uplink interference limits. An LSTM-enhanced Double Dueling DQN learns channel allocations from historical observations and task queues, with offline training and online execution. Simulations report higher combined throughput and more stable allocation than the compared spectrum-sharing policies.

## Problem framing

Maritime communications still struggle to deliver reliable, high-rate links; integrated satellite-maritime networks extend coverage but the VDES standard permits spectrum sharing without specifying **how** to do it, and co-channel interference between heterogeneous VDE-SAT and VDE-TER systems limits spectral efficiency. Conventional optimization for this setting assumes a known environment model and full global state, which is unrealistic, and simple methods struggle to learn in partially observable settings. This work designs a centralized, interference-constrained spectrum-sharing strategy that handles **incomplete observability** and **heterogeneous-system interference**, gaps the authors note are left open by both the standard and prior research.

## System model

- **Network.** An offshore scenario with K independent VDE-TER self-organizing networks (SONs) of ship stations and V isolated ships forming the VDE-SAT with the satellite. VDES allocates 300 kHz total: eight 25 kHz **share channels** (usable by both VDE-TER and VDE-SAT) plus two 25 kHz bands reserved for VDE-SAT. VDES is a **TDMA** system distinguishing physical channels (center frequency + bandwidth) and logical channels (time-slot patterns); the strategy must allocate both frequency and time-slot resources.
- **Objective.** Maximize $\sum_U (D_i^{\mathrm{TER}} + D_i^{\mathrm{SAT}})$ — the combined data throughput on the shared channels — where the VDE-SAT term is weighted by task priority $\kappa_p \cdot p_{i,j}^{\mathrm{tsk}}$, subject to per-channel **downlink and uplink interference constraints** ($\Phi_{\mathrm{DIC}}^i \le \Phi_{\mathrm{DIC}}^{\mathrm{threshold}}$, $\Phi_{\mathrm{UIC}}^i \le \Phi_{\mathrm{UIC}}^{\mathrm{threshold}}$).
- **Interference constraints.** Derived from ITU/ECC rules: downlink uses an electromagnetic power-flux-density (PFD) mask and a C/I threshold (12 dB SINAD-based protection of land-mobile systems), with satellite-inclination-to-elevation-angle geometry and ship-antenna gain patterns; uplink constraints are similarly established to keep co-channel interference within acceptable thresholds.

## Method

- **POMDP formulation.** The throughput-maximization problem is cast as a POMDP because the satellite has only partial channel-status observations; the agent uses observation history to inform decisions.
- **SCA-D3QN.** A shared-channel resource-allocation algorithm combining **Dueling DQN** (value/advantage streams) and **Double DQN** (decoupled selection/evaluation) to evaluate channel-allocation actions, mitigate action-value over-estimation, and accelerate convergence.
- **Deployment.** Offline training, online implementation, to reduce online computational cost.

## Key findings

- Simulation results are reported to show the proposed strategy outperforming benchmark algorithms in **system throughput and stability**, while meeting varied transmission (task-priority) requirements within the interference constraints. Specific numeric margins are figure-derived; treat exact values as indicative.

## Limitations / future work

The evaluation is simulation-based and scoped to an **offshore** scenario (dense near-coast ship traffic, where satellite spectrum-sharing demand is low, is excluded). Explicit future-work statements beyond the proposed strategy are `not in parse`.

## Relation to the corpus

A **satellite-maritime** entry that, unlike the corpus's maritime-MEC offloading papers, addresses the **spectrum/communication layer** rather than computation offloading: it allocates shared VDES channels under interference constraints rather than placing tasks on edge servers. It complements the satellite-assisted marine offloading of [[wang-2024-twotier-satellite-marine]] and the HAP-UAV maritime-IoT network of [[liu-2025-haps-uav-maritime-iot]] from the spectrum-management side, and shares the **DQN-family learning + satellite-ground integration** pattern with the VNF-selection work [[zhang-2025-vnf-sgin-dql]]. Its [[pomdp]] formulation and [[dueling-dqn]] + [[ddqn|Double DQN]] backbone connect to the corpus's value-based DRL vocabulary, and its cognitive-radio framing relates to [[overlay-underlay-spectrum-access]] and [[spectrum-sensing-channel-selection]]; it grounds [[non-terrestrial-network]] from the maritime spectrum-sharing angle.

## Raw artifacts

- `raw/sources/Intelligent_Spectrum_Sharing_Strategy_for_Integrated_Satellite-Maritime_Heterogeneous_Mobile_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
