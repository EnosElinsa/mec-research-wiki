---
type: source
title: "An Energy Effective RIS-Assisted Multi-UAV Coverage Scheme for Fairness-Aware Ground Terminals"
authors: ["Na Lin", "Tianxiong Wu", "Liang Zhao", "Ammar Hawbani", "Shaohua Wan", "Mohsen Guizani"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3424980"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 9, no. 1, pp. 164-176, Mar. 2025"
tags: [source, ris, multi-uav, coverage, fairness, tdqn, dqn, uav-trajectory-control, energy-efficiency]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[k-dbscan-uav-deployment]]"
  - "[[triple-deep-q-network]]"
  - "[[deep-q-network]]"
  - "[[ddqn]]"
  - "[[dueling-dqn]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[drone-cell-3d-placement]]"
  - "[[weighted-kmeans-uav-deployment]]"
created: 2026-07-11
updated: 2026-07-11
---

# An Energy Effective RIS-Assisted Multi-UAV Coverage Scheme for Fairness-Aware Ground Terminals

## Citation

Lin, N., Wu, T., Zhao, L., Hawbani, A., Wan, S., & Guizani, M. (2025). *An Energy Effective RIS-Assisted Multi-UAV Coverage Scheme for Fairness-Aware Ground Terminals*. **IEEE Transactions on Green Communications and Networking**, 9(1), 164-176. DOI: 10.1109/TGCN.2024.3424980. DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record; technical claims are grounded in the local parse.

## TL;DR

Studies emergency/temporary communications where facade-mounted RIS panels assist multiple UAV mobile BSs serving known ground terminals. K-DBSCAN partitions GTs and removes outliers, TDQN jointly chooses 3D UAV trajectory and GT scheduling, and a fair-screening rule prevents the UAVs from repeatedly serving only high-channel-gain terminals while maximizing energy efficiency.

## Problem

The paper jointly optimizes UAV 3D trajectory, GT service order, and RIS phase shifts to maximize summed UAV energy efficiency under UAV movement, altitude, energy, speed, TDMA, and cumulative-throughput fairness constraints. The hard part is that energy-efficient service can become unfair: a UAV may keep choosing the easiest high-channel-gain GT and starve the rest.

## System model

GT coordinates are known. K-DBSCAN partitions GTs into service regions, marks outliers, and assigns one UAV plus one RIS to each region. Direct UAV-GT links may be blocked; RIS-reflected UAV-RIS-GT links provide an assisted path. The model includes UAV propulsion energy, channel gain, transmission rate, throughput, and per-GT cumulative throughput fairness.

## Method

K-DBSCAN supplies cluster centers and movement radii, reducing the trajectory search region before DRL training. The MDP state includes UAV location and a fairness vector; actions combine horizontal movement, vertical movement, and GT scheduling. The [[triple-deep-q-network|TDQN]] controller uses original, target, and auxiliary target networks with asynchronous updates and expectation-based target estimation to reduce overestimation. A fair-screening step removes actions that would serve GTs whose cumulative throughput already exceeds the local average.

## Key findings

- RIS support nearly doubles the average energy efficiency versus the no-RIS DQN baseline in the reported table: 10.8169 Kbits/J for DQN-RIS-DBSCAN-Fair versus 5.7678 for DQN-noRIS-DBSCAN-Fair.
- TDQN improves over DQN, DDQN, and Dueling DQN in the same RIS/DBSCAN/fair setting: 11.3573 Kbits/J versus 10.8169, 11.0393, and 10.9498.
- K-DBSCAN gives the best reported average energy efficiency among clustering choices: 11.5723 Kbits/J for TDQN-RIS-K-DBSCAN-Fair versus 10.9124 with K-means++ and 10.8974 with K-means.
- The parse reports TDQN as 2.9% more energy efficient than the baseline and K-DBSCAN as speeding TDQN training by 59.4%.
- Fair screening sharply reduces per-region throughput variance: for UAV1, 97.11 with fair screening versus 100187.96 without; for UAV2, 21.56 versus 133261.15; for UAV3, 22.12 versus 108850.61.

## Limitations / future work

The model does not consider inter-region UAV collaboration or interference. Outlier GTs are excluded from service. The conclusion names future work on improving DRL generalization when GT distributions change and deploying more UAVs in different roles to ensure global GT fairness.

## Relation to the corpus

This is a communications-coverage source rather than a computation-offloading source. It connects [[intelligent-reflecting-surface]], [[drone-cell-3d-placement]], [[uav-trajectory-control]], and [[fairness-metrics-in-mec]] through a concrete RIS-assisted multi-UAV coverage controller. Its [[k-dbscan-uav-deployment]] step is the clustering counterpart to [[weighted-kmeans-uav-deployment]], while [[triple-deep-q-network]] extends the wiki's DQN/DDQN/dueling-DQN family.

## Raw artifacts

- `raw/sources/An_Energy_Effective_RIS-Assisted_Multi-UAV_Coverage_Scheme_for_Fairness-Aware_Ground_Terminals/An_Energy_Effective_RIS-Assisted_Multi-UAV_Coverage_Scheme_for_Fairness-Aware_Ground_Terminals.md`
- Original PDF and extracted figures (`images/`) in the same folder.
