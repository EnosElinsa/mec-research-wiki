---
type: source
title: "Meta-Learning-Enhanced Task Assignment and Resource Scheduling for UAV-Assisted WSNs in 6G-Enabled ITS"
authors: ["Mesfin Leranso Betalo", "Amr Mohamed", "Amin Sharafian", "Zongze Wu", "Jianqiang Li", "Xiaoshan Bai"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3696005"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), accepted manuscript, pp. 1-18"
tags: [source, uav-enabled-its, wireless-sensor-network, meta-learning, maddpg, fairness, resource-allocation]
related:
  - "[[mw-mad3pg]]"
  - "[[meta-deep-reinforcement-learning]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-enabled-its]]"
  - "[[uav-trajectory-control]]"
  - "[[jains-fairness-index]]"
created: 2026-07-13
updated: 2026-07-13
---

# Meta-Learning-Enhanced Task Assignment and Resource Scheduling for UAV-Assisted WSNs in 6G-Enabled ITS

## Citation

Betalo, M. L., Mohamed, A., Sharafian, A., Wu, Z., Li, J., & Bai, X. (2026). *Meta-Learning-Enhanced Task Assignment and Resource Scheduling for UAV-Assisted WSNs in 6G-Enabled ITS*. **IEEE Transactions on Mobile Computing**, accepted manuscript, 1-18. DOI: 10.1109/TMC.2026.3696005.

## TL;DR

Combines MAML-style adaptation with fairness-aware multi-agent deterministic actor-critic learning. UAVs jointly choose movement, sensor-node assignment, and communication resources in a 6G ITS data-collection network under power, QoS, latency, range, and airspace constraints.

## Problem and system model

Multiple UAVs collect traffic-sensor data and relay it to a ground control station. The model couples rotary-wing mobility, air-to-ground rates, interference-aware scheduling, communication and processing energy, and binary UAV-sensor association. The stated energy-efficient-data-throughput objective is formally a weighted throughput-minus-power expression rather than a throughput/energy ratio.

The formulation is a non-convex MINLP. It separates deployment, sensor selection, and resource scheduling while retaining a stochastic-game/CMDP view whose state includes position, residual energy, sensor activity, and link rates.

## Method

[[mw-mad3pg]] augments [[maddpg]] with MAML-style inner/outer updates across traffic, energy, sensor-distribution, and channel tasks. Local actors choose movement, sensor selection, and resources; critics and replay aggregation support coordination. Jain-index reward shaping favors under-served sensors, while target networks and soft updates stabilize training.

## Key findings

- Table III reports 95.2% reliability, 92.4% deployment efficiency, and 88.9% offloading capacity for MW-MAD3PG, above the displayed MADDPG, Meta-SGD, and Meta-QL values; the denominators for the latter two percentage metrics are not defined in the parse.
- Table IV reports 0.98 s training time per episode, 6.5 ms inference latency per action, and a 38 MB model.
- The paper's headline claims of up to 25% better coordination/deployment and 30% greater offloading capacity are narrative or figure-level claims rather than directly reproducible table differences.

## Limitations / parse caveats

Evaluation is simulation-only. The parse conflicts on fixed versus variable altitude, Rician versus Rayleigh fading, two versus three decomposed subproblems, and MW-MAD3PG versus MW-MADDPG naming. It also gives incompatible training hardware/timing descriptions. Security mechanisms are discussed and evaluated in parts of the paper, but the conclusion says they are not integrated into the core algorithm. The accepted-manuscript banner warns that content may change.

## Relation to the corpus

This source joins [[meta-deep-reinforcement-learning]] with fairness-aware multi-UAV control in [[uav-enabled-its]]. Unlike conventional MEC offloading papers, its formal decisions center on sensor assignment, data collection, flight, and communication resources rather than a detailed local-versus-edge execution model.

## Raw artifacts

- `raw/sources/Meta-Learning-Enhanced_Task_Assignment_and_Resource_Scheduling_for_UAV-Assisted_WSNs_in_6G-Enabled_ITS/Meta-Learning-Enhanced_Task_Assignment_and_Resource_Scheduling_for_UAV-Assisted_WSNs_in_6G-Enabled_ITS.md`
- Original PDF and extracted figures (`images/`) are in the same folder.
