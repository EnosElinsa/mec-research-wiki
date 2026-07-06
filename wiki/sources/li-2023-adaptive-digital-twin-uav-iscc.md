---
type: source
title: "Adaptive Digital Twin for UAV-Assisted Integrated Sensing, Communication, and Computation Networks"
authors: ["Bin Li", "Wenshuai Liu", "Wancheng Xie", "Ning Zhang", "Yan Zhang"]
year: 2023
url: "https://doi.org/10.1109/TGCN.2023.3298039"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, digital-twin, mobile-edge-computing, integrated-sensing-computation-communication, multi-uav-assisted-mec, task-offloading, mappo, beta-policy-drl, centralized-training-decentralized-execution, uav-trajectory-control]
related:
  - "[[digital-twin]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[mobile-edge-computing]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[mappo]]"
  - "[[beta-policy-drl]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-trajectory-control]]"
  - "[[li-2024-robust-bmappo-multiuav-mec]]"
  - "[[tang-2024-iscc-uav-feel]]"
  - "[[wen-2024-iscc-edge-ai]]"
  - "[[qin-2025-urllc-noma-uav-iscc]]"
  - "[[kang-2023-mappo-hierarchical-aerial]]"
  - "[[ning-zhang]]"
created: 2026-07-06
updated: 2026-07-06
---

# Adaptive Digital Twin for UAV-Assisted Integrated Sensing, Communication, and Computation Networks

## Citation

Li, B., Liu, W., Xie, W., Zhang, N., & Zhang, Y. (2023). *Adaptive Digital Twin for UAV-Assisted Integrated Sensing, Communication, and Computation Networks*. **IEEE Transactions on Green Communications and Networking**, 7(4), 1996-2009. DOI: 10.1109/TGCN.2023.3298039.

## TL;DR

Studies a digital-twin-empowered UAV-assisted ISCC network where users perform radar sensing and computation offloading over the same spectrum while UAVs provide edge computing. The paper balances MIMO radar beampattern quality against weighted computation/offloading/flying energy. Its ATB-MAPPO solver combines a DT-supported CTDE loop, MAPPO, Beta-distribution actors for bounded actions, and attention critics.

## Problem framing

UAV mobility helps ISCC in weak-coverage, disaster, remote, and hotspot scenarios, but it also couples sensing, communication, computation, offloading, CPU allocation, and UAV trajectory. Digital twins can support real-time decision-making, but only if the controller accounts for mapping and estimation deviation between the physical layer and the DT layer. The paper therefore treats DT estimation accuracy as part of the optimization problem rather than assuming a perfect twin.

## System model

- The network has $K$ users with dual-function radar/communication systems, $M$ UAVs carrying MEC servers, and a control center hosting the DT layer.
- UAV flight is slotted with position, speed, acceleration, fixed altitude, and inter-UAV collision-avoidance constraints.
- User DTs record location, task tuple, and estimated local compute resources; UAV DTs record position, association, and estimated compute allocation.
- Tasks use partial offloading, with one part processed locally and another part offloaded to a selected UAV.
- Energy includes user local computing and transmission energy plus UAV computation and flight energy; radar sensing is constrained by average INR and optimized through a beampattern objective.

## Method

- Formulates a multi-objective optimization problem minimizing radar waveform covariance mismatch and weighted energy under association, power, latency, CPU, offloading-ratio, UAV-speed/acceleration, and collision constraints.
- Reformulates the non-convex, nonlinear, mixed-variable problem as a multi-agent MDP.
- Decomposes agents into offloading-configuration agents, beampattern-configuration agents, and UAV agents.
- Uses DT-enabled CTDE: observations and actions are uploaded to the DT layer, virtual twins are updated, rewards are evaluated, and centralized critics consume merged global state.
- Replaces Gaussian actor outputs with Beta distributions for bounded actions and adds attention in critic networks to focus on relevant cross-agent features.

## Key findings

- ATB-MAPPO reaches the highest reward and faster convergence than Beta-MAPPO, Pure-MAPPO, and MADDPG in the reported convergence comparisons.
- Increasing DT estimation deviation from 0% to 25% increases average weighted energy consumption, supporting the paper's claim that DT-assisted control depends on twin accuracy.
- More users and larger task sizes increase energy, while larger bandwidth and more UAVs reduce the energy pressure.
- Increasing the sensing-communication weight shifts the optimized beams from communication-oriented directions toward the desired sensing beampattern.
- Learned UAV trajectories move toward denser user regions and hover slowly to save flight energy.

## Limitations / future work

The parse does not contain an explicit future-work paragraph. Grounded caveats are simulation-only evaluation, no convergence proof beyond empirical learning curves, and sensitivity to DT estimation deviation.

## Relation to the corpus

This is the wiki's cleanest bridge between [[digital-twin]], [[integrated-sensing-computation-communication]], and [[centralized-training-decentralized-execution]]. It complements [[tang-2024-iscc-uav-feel]] and [[wen-2024-iscc-edge-ai]] by adding a DT layer and multi-UAV trajectory/offloading decisions. On the DRL side it is close to [[li-2024-robust-bmappo-multiuav-mec]] because both use bounded Beta-policy MAPPO-style control, but this paper's distinctive variable is DT mapping/estimation deviation. [[ning-zhang]] is a recurring co-author in the corpus's air-ground and robust multi-UAV MEC line.

## Raw artifacts

- `raw/sources/Adaptive Digital Twin for UAV-Assisted Integrated Sensing- Communication- and Computation Networks/Adaptive Digital Twin for UAV-Assisted Integrated Sensing- Communication- and Computation Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
