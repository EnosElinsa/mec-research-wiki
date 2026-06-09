---
type: source
title: "Joint Trajectory Design and Radio Resource Management for UAV-Aided Vehicular Networks"
authors: ["Leonardo Spampinato", "Danila Ferretti", "Chiara Buratti", "Riccardo Marini"]
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3454955"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-base-station, vehicular-mec, trajectory-optimization, radio-resource-management, drl, v2x, ilp]
related:
  - "[[vehicular-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[multi-agent-q-learning]]"
created: 2026-06-04
updated: 2026-06-09
---

# Joint Trajectory Design and Radio Resource Management for UAV-Aided Vehicular Networks

## Citation

Spampinato, L., Ferretti, D., Buratti, C., & Marini, R. (2025). *Joint Trajectory Design and Radio Resource Management for UAV-Aided Vehicular Networks*. **IEEE Transactions on Vehicular Technology**, 74(1). DOI: 10.1109/TVT.2024.3454955. (Received 4 April 2023; accepted 10 August 2024; published 5 September 2024; current version 16 January 2025.)

## TL;DR

Studies an Unmanned Aerial Base Station (UABS) assisting a terrestrial mmWave macro-BS (MBS) network serving mobile connected vehicles (GUEs) with V2X extended-sensing applications. Jointly addresses: (i) **UABS trajectory design**, solved by a **Double Dueling Deep Q-Network (3DQN)** agent that learns to track GUEs in a complex urban road network (Bologna, Italy, simulated with SUMO); and (ii) **radio resource management (RRM)**, solved as an **Integer Linear Program (ILP)** that maximizes served users subject to service-window constraints. The two solvers are intertwined via a properly designed reward function: the DRL agent optimizes trajectory to maximize RRM benefit, and ILP provides the network reward signal. Evaluated in coverage-limited and capacity-limited scenarios.

## Problem framing

V2X extended-sensing applications require continuous, high-rate, low-latency service to vehicles. In complex urban environments, vehicle positions are unpredictable and MBSs alone may not guarantee coverage or capacity. A mobile UABS provides additional aerial coverage but must track fast-moving vehicles whose paths are not known a priori. Standard convex optimization assumes static users and full location knowledge, which is infeasible here. The joint trajectory + RRM problem couples the UABS position (which determines interference) with the resource scheduling (which maximizes served users given SINR). This coupling is captured via the DRL reward, enabling co-design without centralized full-state knowledge.

## System model

- **Urban area** (Bologna city street layout); **multiple MBSs** + **1 UABS** at fixed altitude flying in the mmWave band.
- **GUEs** (vehicles) move via SUMO mobility simulator at realistic speeds; V2X messages require defined service windows (data-rate x duration).
- **UABS mobility:** discrete action set (8 directions + hover) at variable speed; backhaul connection to MBS maintained with handover threshold.
- **3DQN trajectory agent:** receives observations of UABS position, GUE positions/signal strengths; outputs UABS movement; reward combines ILP outcome (fraction of served GUEs) with coverage metrics.
- **ILP RRM:** assigns channel resources (beamforming + time-frequency slots) to GUEs and MBSs jointly to maximize satisfied service windows; solved per time instant.
- **Two scenarios:** coverage-limited (urban canyon, few MBSs) and capacity-limited (dense users).

## Key findings

- Joint 3DQN trajectory + ILP RRM achieves a **higher percentage of satisfied GUEs** than benchmarks (random trajectory, fixed-altitude hover, MBS-only) in both coverage-limited and capacity-limited scenarios (parse Section VII).
- The DRL agent learns to follow GUEs proactively without prior knowledge of their positions, demonstrating adaptability in a highly dynamic urban environment (parse Section VII, Conclusion).
- The UABS provides more benefit in coverage-limited scenarios where terrestrial BSs have poor LoS to vehicles (parse discussion Section VII).

## Limitations / future work

Single UABS. Parse does not enumerate explicit numerical gain percentages. SUMO-based evaluation represents a simulation of Bologna but not a real deployment. ILP is computationally intensive per-slot; scalability to dense GUE counts is not analyzed.

## Relation to the corpus

Distinct in coupling DRL trajectory design with an ILP RRM solver; most corpus trajectory papers use AO or full-DRL. The V2X + UABS cooperation angle connects to [[peng-2020-maddpg-uav-vehicular]] and [[dai-2024-uav-vehicular-offloading-lyapunov]] in the Vehicular MEC track. The urban SUMO simulation methodology is shared with [[liu-2025-mad2rl-dnn-vec]].

## Raw artifacts

- `raw/sources/Joint_Trajectory_Design_and_Radio_Resource_Management_for_UAV-Aided_Vehicular_Networks/full.md`
- Original PDF (`8b0db62d-3368-4cba-84e8-60b9224fbb27_origin.pdf`) and extracted figures (`images/`) in the same folder.
