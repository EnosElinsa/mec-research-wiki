---
type: source
title: "Hierarchical Control Multi-Agent DRL for Vehicle Twin Migration with Workload Prediction in UAV-Assisted Vehicular Metaverses"
authors: ["Junlong Chen", "Yingkai Kang", "Jiawen Kang", "Minrui Xu", "Yongju Tong", "Fan Wu", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3674825"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-mec, vehicle-twin-migration, mappo, digital-twin, task-migration]
related:
  - "[[vehicle-twin-migration]]"
  - "[[vehicular-mec]]"
  - "[[digital-twin]]"
  - "[[task-migration]]"
  - "[[mappo]]"
  - "[[uav-trajectory-control]]"
  - "[[mou-2025-adm-dt-migration]]"
created: 2026-07-07
updated: 2026-07-07
---

# Hierarchical Control Multi-Agent DRL for Vehicle Twin Migration with Workload Prediction in UAV-Assisted Vehicular Metaverses

## Citation

Chen, J., Kang, Y., Kang, J., Xu, M., Tong, Y., Wu, F., & Niyato, D. (2026). *Hierarchical Control Multi-Agent DRL for Vehicle Twin Migration with Workload Prediction in UAV-Assisted Vehicular Metaverses*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3674825.

## TL;DR

Combines RSU workload prediction with hierarchical MAPPO to decide vehicle-twin migration and UAV routing in a UAV-assisted vehicular metaverse. ACB-LSTM predicts future RSU workload from noisy historical sequences; HC-MAPPO makes upper-layer vehicle/UAV decisions; deterministic lower-layer controllers map them to valid migration and UAV-route actions. The reported latency gains come from anticipating RSU congestion and using UAVs as mobile edge servers when terrestrial infrastructure is overloaded.

## Problem framing

Vehicle Twins (VTs) need low-latency service continuity while vehicles move across RSU coverage areas. Existing VT migration methods assume enough RSU capacity or use static UAV placement; overloaded RSUs, dynamic workload spikes, UAV energy limits, and trajectory choices create a coupled migration-routing problem. The paper addresses this by forecasting workload and coordinating VT migration with UAV routing.

## System model

The system contains RSUs, UAVs, and vehicles over discrete time slots. Vehicles generate VT tasks, may offload part of a task to the current RSU, and may pre-migrate the remaining part to a target RSU; when RSUs are overloaded, UAVs can serve as mobile edge servers. The objective minimizes VT service latency and UAV energy consumption under RSU workload, UAV workload, UAV energy, and assignment constraints. The latency model focuses on downlink result delivery, computation latency at RSUs/UAVs, and migration-related service continuity.

## Method

The framework has two main components:

- **ACB-LSTM workload prediction.** Historical RSU workload sequences are augmented with Gaussian noise, processed by CNN layers for local temporal features, and passed through BiLSTM to capture bidirectional temporal dependencies.
- **HC-MAPPO decision control.** The upper layer uses MAPPO over vehicle server-selection actions and UAV task-priority weights. The lower layer converts those high-level decisions into executable VT migration and UAV routing: vehicles choose UAVs when available or nearest/k-th RSUs, and UAV routing uses A* with task-priority-dependent costs.

## Key findings

- The abstract reports 25.70% average-latency reduction and 63.70% workload-prediction validation-loss reduction compared with baselines.
- ACB-LSTM validation loss improves over LSTM, BiLSTM, and CNN-BiLSTM by 75.00%, 61.54%, and 54.55%, respectively.
- ACB-LSTM reduces MSE by 80.48%, 71.42%, and 67.30% relative to LSTM, BiLSTM, and CNN-BiLSTM, and reduces MAE by 51.72%, 36.28%, and 28.92%.
- HC-MAPPO with UAV and prediction reduces average latency by 45.54% versus Random-uav, 32.93% versus Greedy-uav, 22.54% versus MASAC-uav, and 1.79% versus HC-MAPPO-uav.
- The paper reports RSU workload reduction up to 2.60% while increasing UAV serving time by 5.60%, plus a separate workload-reduction analysis of 2.34% versus baseline approaches.

## Limitations / future work

Evaluation uses a simulated urban road setting with Beijing GPS trajectories, nine RSUs, two UAVs, 150 random vehicles, and ten intelligent vehicles. The authors plan to extend evaluation to larger scales with higher vehicle densities and more frequent handovers.

## Relation to the corpus

This source extends [[digital-twin]] and [[task-migration]] into the more specific [[vehicle-twin-migration]] setting. Compared with [[mou-2025-adm-dt-migration]], it adds UAVs as mobile edge servers and couples migration with UAV routing. It also broadens the [[vehicular-mec]] track from task offloading and FL participant selection into metaverse-service continuity.

## Raw artifacts

- `raw/sources/Hierarchical Control Multi-Agent DRL for Vehicle Twin Migration with Workload Prediction in UAV-Assisted Vehicular Metaverses/Hierarchical Control Multi-Agent DRL for Vehicle Twin Migration with Workload Prediction in UAV-Assisted Vehicular Metaverses.md`
- Original PDF and extracted figures (`images/`) in the same folder.
