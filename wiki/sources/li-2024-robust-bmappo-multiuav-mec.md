---
type: source
title: "Robust Computation Offloading and Trajectory Optimization for Multi-UAV-Assisted MEC: A Multiagent DRL Approach"
authors: ["Bin Li", "Rongrong Yang", "Lei Liu", "Junyi Wang", "Ning Zhang", "Mianxiong Dong"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2023.3300718"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, multi-uav-assisted-mec, multi-agent-drl, mappo, robust-optimization, csi-estimation-error, trajectory-optimization]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[mappo]]"
  - "[[beta-policy-drl]]"
  - "[[robust-offloading]]"
  - "[[csi-estimation-error]]"
  - "[[uav-trajectory-control]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[zhao-2022-matd3-multiuav-ec-offloading]]"
created: 2026-05-31
updated: 2026-05-31
---

# Robust Computation Offloading and Trajectory Optimization for Multi-UAV-Assisted MEC: A Multiagent DRL Approach

## Citation

Li, B., Yang, R., Liu, L., Wang, J., Zhang, N., & Dong, M. (2024). *Robust Computation Offloading and Trajectory Optimization for Multi-UAV-Assisted MEC: A Multiagent DRL Approach*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3300718. (Manuscript received 12 Jun 2023; date of publication 1 Aug 2023; date of current version 24 Jan 2024 → year 2024.)

## TL;DR

A multi-UAV-assisted MEC network with **both communication and computation uncertainties** — only partial CSI (imperfect UAV–UE channels) and inaccurate task-complexity estimates are available. The paper proposes a **robust** design that minimizes total weighted energy consumption by jointly optimizing UAV trajectory, task partition, and computation+communication resource allocation. It reformulates the problem as a multiagent MDP and solves it with **MAPPO using a Beta-distribution actor output (b-MAPPO)** to eliminate the boundary effects of Gaussian policies on bounded actions.

## Problem framing

UAV-MEC must serve UEs in remote/hotspot areas, but real deployments face uncertainty: heterogeneous networks cause unpredictable delivery time/packet loss; accurate CSI is hard to obtain; and task complexity is only known exactly after completion. A single UAV cannot serve many UEs, motivating multi-UAV cooperation, and most prior robust designs handled communication **or** computation uncertainty in isolation — this work treats both jointly.

## System model

- **Actors.** M UAVs (each a UPA antenna array) and K single-antenna UEs over N time slots of flight period T; UE–UAV matching factor α_{k,m} ∈ {0,1} with at most one UAV per UE.
- **Uncertainties.** Bounded imperfect CSI (channel estimation error ε_{k,m}) and bounded task-complexity estimation error (ε_z). See [[csi-estimation-error]], [[robust-offloading]].
- **Objective.** Minimize total weighted energy (UE + UAV) via joint optimization of UAV trajectory, UE–UAV matching, task partition, and CPU/communication resources, with UAV collision-avoidance and kinematic constraints.

## Method

- Reformulate as a **multiagent MDP** and solve with **MAPPO** under CTDE ([[mappo]], [[centralized-training-decentralized-execution]]).
- Replace the actor's Gaussian output with a **Beta distribution** (b-MAPPO) so the policy has bounded support matching double-bounded actions, improving early exploration and avoiding boundary bias. See [[beta-policy-drl]].

## Key findings

- Simulation: 1000 m × 1000 m region, K = 20 UEs, M = 5 UAVs, task sizes 3.5–4.5 Mb, 300 training episodes (200 steps each), γ = 0.98, Adam.
- **b-MAPPO** achieves the highest reward and faster convergence than Pure-MAPPO (Gaussian) and MADDPG; reported average UE-agent episode reward ≈ −3.05 (the highest observed).
- Against benchmarks (Pure-MAPPO, MADDPG, Greedy, DRL+CVX), b-MAPPO gives lower weighted energy than the learning/heuristic baselines and tracks the near-optimal DRL+CVX closely at lower complexity (Figs. 5–6, qualitative).
- Weighted energy rises with wider task-complexity intervals, larger estimation-error bounds, and larger data sizes, confirming robustness behavior under bounded errors (Figs. 8–9, indicative).

## Limitations / future work

Simulation-based; comparative magnitudes are read from bar/line figures (indicative) beyond the verbatim reward value. Future work (stated): allow different task types to use different offloading rates.

## Relation to the corpus

A **robust multi-agent UAV-MEC** entry whose novelty is jointly handling communication **and** computation uncertainty, and its **Beta-policy** twist on [[mappo]] (which it shares with the hierarchical-aerial [[kang-2023-mappo-hierarchical-aerial]]). It sits with the multi-agent UAV-MEC family — [[zhao-2022-matd3-multiuav-ec-offloading]], [[seid-2021-madrl-multiuav-iot-edge]], [[chang-2022-marl-multiuav-trajectory]] — and its CSI-uncertainty robustness complements the distributionally-robust [[jia-2025-dro-uav-hap-mec]] and terrain-aware [[wu-2026-terrain-aware-uav-mec]] approaches to channel uncertainty. Introduces the [[beta-policy-drl]] and [[robust-offloading]] concepts.

## Raw artifacts

- `raw/sources/Robust_Computation_Offloading_and_Trajectory_Optimization_for_Multi-UAV-Assisted_MEC_A_Multiagent_DRL_Approach/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
