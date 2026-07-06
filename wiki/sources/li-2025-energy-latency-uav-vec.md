---
type: source
title: "Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing"
authors: ["Chunlin Li", "Jianyang Wu", "Yong Zhang", "Shaohua Wan"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3433457"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, vehicular-mec, federated-learning, energy-latency-tradeoff, ddqn, mixed-integer-nonlinear-programming, uav-assisted-vec]
related:
  - "[[vehicular-mec]]"
  - "[[federated-learning]]"
  - "[[energy-latency-tradeoff]]"
  - "[[ddqn]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[uav-trajectory-control]]"
  - "[[li-2024-airground-vec-offloading]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
  - "[[zhang-2025-mcma-task-migration]]"
created: 2026-07-07
updated: 2026-07-07
---

# Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing

## Citation

Li, C., Wu, J., Zhang, Y., & Wan, S. (2025). *Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2024.3433457. (Manuscript received 10 January 2024; accepted 18 July 2024; date of publication 25 July 2024; date of current version 21 May 2025 -> year 2025.)

## TL;DR

Optimizes **vehicle selection** and communication / computation resource allocation for **hierarchical federated learning** in a UAV-assisted VEC system. More vehicles can improve FL training but also increase uplink latency, bandwidth pressure, and energy consumption. The paper formulates a weighted **energy-latency tradeoff** with constraints on vehicle departure time, vehicle battery level, participant count, UAV bandwidth, and UAV compute resources. The resulting MINLP is modeled as an MDP and solved with **AB-DDQN**, a double-DQN variant trained with AdamW and tuned by the butterfly optimization algorithm.

## Problem framing

Vehicular FL protects raw driving data by keeping it local, but a UAV-assisted VEC deployment must decide which moving vehicles should participate before they leave coverage, and how much bandwidth / CPU resource each selected vehicle should receive. The paper targets this scheduling layer rather than the model-aggregation algorithm itself: it asks how to pick FL participants and allocate UAV resources so the training round stays energy- and latency-efficient.

## System model

- **Four layers.** Vehicles train local models; UAVs act as hovering local aggregators; an edge server performs higher-level aggregation; a cloud server provides global coordination.
- **Mobility.** Vehicle availability is bounded by departure time; hotspot regions guide UAV paths, with a TSP / genetic-algorithm trajectory planner used before resource allocation.
- **Learning task.** Vehicles participate in hierarchical FL; the experiments use the GTSDB traffic-sign dataset.
- **Decision variables.** Binary vehicle-selection variables, UAV bandwidth ratios, and UAV compute-resource ratios.
- **Objective.** Minimize $\alpha T_k + (1-\alpha)E_k$, where $T_k$ is FL latency and $E_k$ covers vehicle and UAV energy.

## Method

The MINLP is converted into an MDP whose state includes latency, compute resources, bandwidth, vehicle battery state, and zero-padded vehicle slots for a fixed action shape. The action jointly chooses participating vehicles and resource ratios. AB-DDQN uses Double DQN to reduce Q-value overestimation, AdamW for optimization, and butterfly optimization to tune hyperparameters such as hidden-neuron count, replay-buffer size, and discount factor. A mobility-aware participant filter based on departure time avoids selecting vehicles that cannot complete the round.

## Key findings

- AB-DDQN converges after roughly 450 iterations in the reported training curves.
- Across local-data-size, participant-count, model-size, and UAV-count sweeps, AB-DDQN reports lower weighted cost than DDPG-CRA, DQN-USCRA, and Q-US baselines.
- With local-data-size variation, reported energy reductions are 13.26% versus DDPG-CRA, 87.92% versus DQN-USCRA, and 91.45% versus Q-US.
- With participant-count variation, reported cost reductions are 18.91%, 87.02%, and 94.49% versus the same baselines.
- The method trades some latency against energy in participant-count settings: latency is lower than DDPG-CRA but higher than DQN-USCRA and Q-US, while total cost is lower.

## Limitations / future work

The evaluation is based on a campus-style experimental / emulation environment rather than a full real-UAV field deployment. The authors identify adversarial FL participants and stronger privacy protections as future work.

## Relation to the corpus

This is a **vehicular MEC + FL scheduling** source. It is closest to [[li-2024-airground-vec-offloading]] in its air-ground VEC substrate, but it narrows the decision problem to selecting FL participants and allocating UAV resources. It complements [[zhang-2025-mcma-task-migration]] and [[ma-2025-pdqn-vehicular-mec]] by making the energy-latency tradeoff explicit at the learning-round level rather than only at task offloading or migration time.

## Raw artifacts

- `raw/sources/Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing/Energy-Latency Tradeoff for Joint Optimization of Vehicle Selection and Resource Allocation in UAV-Assisted Vehicular Edge Computing.md`
- Original PDF and extracted figures (`images/`) in the same folder.
