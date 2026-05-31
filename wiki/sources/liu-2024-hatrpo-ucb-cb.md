---
type: source
title: "UAV-Enabled Collaborative Beamforming via Multi-Agent Deep Reinforcement Learning"
authors: ["Saichao Liu", "Geng Sun", "Jiahui Li", "Shuang Liang", "Qingqing Wu", "Pengfei Wang", "Dusit Niyato"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3419915"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, collaborative-beamforming, virtual-antenna-array, multi-agent-reinforcement-learning, trust-region-policy-optimization, beta-policy-drl, multi-objective, energy-efficiency]
related:
  - "[[collaborative-beamforming]]"
  - "[[heterogeneous-agent-rl]]"
  - "[[trust-region-policy-optimization]]"
  - "[[beta-policy-drl]]"
  - "[[stochastic-game]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[air-to-ground-channel-model]]"
  - "[[mappo]]"
  - "[[maddpg]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[sun-2025-emoppo-vlh-aerial-cb]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
  - "[[zheng-2024-recmop-uav-cb]]"
  - "[[liang-2024-hmecmop-uav-cb]]"
  - "[[geng-sun]]"
  - "[[jiahui-li]]"
  - "[[shuang-liang]]"
  - "[[qingqing-wu]]"
  - "[[dusit-niyato]]"
created: 2026-06-01
updated: 2026-06-01
---

# UAV-Enabled Collaborative Beamforming via Multi-Agent Deep Reinforcement Learning

## Citation

Liu, S., Sun, G., Li, J., Liang, S., Wu, Q., Wang, P., & Niyato, D. (2024). *UAV-Enabled Collaborative Beamforming via Multi-Agent Deep Reinforcement Learning*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3419915. (Manuscript received 31 Aug 2023; accepted 23 Jun 2024; date of publication 27 Jun 2024; date of current version 5 Nov 2024.)

## TL;DR

Multiple UAVs form a **UAV-enabled virtual antenna array (UVAA)** and use [[collaborative-beamforming|collaborative beamforming]] (CB) to reach remote base stations on air-to-ground links. The paper formulates the **UAV-enabled CB multi-objective optimization problem (UCBMOP)** — simultaneously maximize the UVAA transmission rate and minimize total UAV energy consumption by optimizing UAV positions and excitation-current weights. Because the two objectives conflict, the variables are non-concave, and the system is dynamic, it is solved online with **MADRL**: a **HATRPO-UCB** algorithm that extends heterogeneous-agent trust region policy optimization (HATRPO) with three techniques (observation enhancement, agent-specific global state, and a Beta-distribution policy).

## Problem framing

A single UAV cannot reach a remote BS due to limited transmit power, and cannot fly close to the BS due to limited battery. CB lets a swarm act as one high-gain antenna array, but repositioning the array to serve different BSs costs flight energy — so rate and energy conflict. Traditional convex/evolutionary optimizers are ill-suited here: the parse argues UCBMOP is **non-convex, NP-hard** (reducible to a nonlinear multidimensional 0–1 knapsack), large-scale, and operates in a **dynamic** environment where a previously computed solution becomes invalid once the task (target BS) changes. This motivates a learning approach that responds in real time.

## System model

- **Actors.** $N$ UAVs (single omni-directional antenna each) in a square area of length $L$, communicating with far-field BSs at known positions; the UVAA serves one BS at a time ([[air-to-ground-channel-model]]).
- **Channel.** LoS probability sigmoid in the elevation angle; channel power gain combines LoS/NLoS attenuation with a path-loss exponent. Transmission rate follows from the **array factor / array gain** of the UVAA toward the BS.
- **Energy.** [[rotary-wing-propulsion-energy-model|Rotary-wing]] UAVs; total energy splits into propulsion (hovering + movement) and communication, with propulsion dominant.
- **Objectives (UCBMOP).** Maximize UVAA transmission rate $R_T$; minimize total UAV motion energy $E_{total}$; variables are the 3D coordinates and excitation-current weights of all UAVs, under flight-area, altitude, excitation-range, and minimum-separation (collision) constraints.

## Method

- **Markov game.** UCBMOP is cast as a Markov game ([[stochastic-game]]); each UAV is an agent with a local observation (its own spherical coordinate to a reference point, distance to the UVAA origin, excitation weight, and the weights/distances of other UAVs). Each episode is a **single time slot**.
- **Scalarized reward.** A weighted-sum reward combines a shared transmission-reward term ($r^{TR}=G P_t$), an altitude term, an energy-consumption penalty, a UAV-to-BS distance penalty, and a UAV-to-UAV concentration term, plus a separation-violation penalty. So the multi-objective problem is handled via **scalarization inside a single reward**, not a vectorial-reward Pareto set.
- **HATRPO-UCB.** Built on conventional **HATRPO** ([[heterogeneous-agent-rl]]), which applies trust-region learning ([[trust-region-policy-optimization]]) to MADRL with a sequential policy-update scheme and a monotonic-improvement guarantee. Three additions:
  1. **Observation enhancement** — replaces raw Cartesian coordinates with a reference-point-based representation so the state characterizes positional relationships across episodes/BSs.
  2. **Agent-specific global state** — a critic input that mixes agent-related features with environment-provided global information, instead of concatenating all local observations (which would blow up the critic input dimension for large swarms) ([[centralized-training-decentralized-execution]]).
  3. **Beta-distribution policy** — replaces the Gaussian actor with a Beta policy whose bounded $[0,1]$ support matches the finite action ranges, removing the boundary bias of Gaussian sampling ([[beta-policy-drl]]).

## Key findings

- **Convergence speed.** The paper states HATRPO-UCB converges fastest, at approximately **750 epochs**, with conventional HATRPO second and MADDPG/IPPO/MAPPO beginning to converge around **1,400 epochs** (verbatim from the parse; the per-method final reward magnitudes are figure-derived and indicative, and the convergence-figure text and its extracted table are not fully consistent on the final reward).
- **Energy at comparable rate.** In the reported numerical optimization results (Table III), HATRPO-UCB attains the **lowest energy consumption** among the learning methods while keeping transmission rate comparable — e.g. for the first BS ~13,401 J vs HATRPO 13,765 J and MADDPG 22,319 J at a rate of ~$1.029\times10^6$ bps; for the second BS ~10,261 J vs HATRPO 11,779 J at ~$1.825\times10^7$ bps. These are the paper's reported simulation values.
- **Baselines beaten.** HATRPO-UCB is compared against two classic antenna arrays (LAA, RAA), three baseline MADRL algorithms ([[maddpg|MADDPG]], IPPO, [[mappo|MAPPO]]), and conventional HATRPO, and ablation experiments confirm each of the three techniques contributes.
- **Robustness.** Under imperfect carrier-phase synchronization (phase errors modeled by a Tikhonov/von Mises distribution), the UVAA transmission rate degrades but recovers as the inverse-variance $\gamma$ grows (figure-derived, indicative).

## Limitations / future work

- The authors note (Remark 3) that **theoretical bounds and convergence of the MADRL algorithm are nearly infeasible to analyze** — the vast hyperparameter space, DNN approximation errors, and environment uncertainty mean performance is established by simulation rather than proof.
- Practical-deployment issues are discussed rather than solved: **UAV collision** is handled by a separation penalty plus off-the-shelf sense-and-avoid; **imperfect synchronization** is mitigated by existing closed-/open-loop methods. Results are simulation-only (Python 3.8 / PyTorch 1.10).

## Relation to the corpus

A **collaborative-beamforming / virtual-antenna-array** entry from the Jilin-University / NTU [[geng-sun]] group (with [[jiahui-li]], [[shuang-liang]], [[qingqing-wu]], [[dusit-niyato]]), and the CB source whose distinguishing feature is solving the rate-vs-energy UVAA problem with a **heterogeneous-agent trust-region MADRL** algorithm rather than evolutionary/swarm or diffusion methods. It is the MADRL counterpart within the [[collaborative-beamforming-in-aerial-mec]] track: distinct from the evolutionary-MORL [[sun-2025-emoppo-vlh-aerial-cb]], the diffusion-enhanced TD3 [[zhang-2024-gdmtd3-aerial-secure-cb]], and the metaheuristic energy-MOP siblings [[zheng-2024-recmop-uav-cb]] (gravitational search) and [[liang-2024-hmecmop-uav-cb]] (multiverse optimizer). Its [[trust-region-policy-optimization]] foundation and [[beta-policy-drl]] actor connect it to the corpus's PPO/MAPPO lineage, and it reinforces [[collaborative-beamforming]] and the [[rotary-wing-propulsion-energy-model]].

## Raw artifacts

- `raw/sources/UAV-Enabled_Collaborative_Beamforming_via_Multi-Agent_Deep_Reinforcement_Learning/full.md`
- Original PDF (`b2e661db-ca7f-4a77-afb9-eb2a0bd0d798_origin.pdf`) and extracted figures in the same folder's `images/`.
