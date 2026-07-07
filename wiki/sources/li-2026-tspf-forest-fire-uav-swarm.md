---
type: source
title: "Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection"
authors: ["Xingyu Li", "Wenzhe Zhang", "Linfeng Liu", "Ping Wang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3599384"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 1, pp. 1169-1183, Jan. 2026"
tags: [source, uav-swarm, forest-fire-detection, federated-learning, robustness, edge-intelligence]
related:
  - "[[two-tier-submodel-partition]]"
  - "[[uav-forest-fire-detection]]"
  - "[[federated-learning]]"
  - "[[split-federated-learning]]"
  - "[[task-redundancy-for-reliability]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[edge-intelligence]]"
created: 2026-07-07
updated: 2026-07-07
---

# Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection

## Citation

Li, X., Zhang, W., Liu, L., & Wang, P. (2026). *Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection*. **IEEE Transactions on Mobile Computing**, 25(1), 1169-1183. DOI: 10.1109/TMC.2025.3599384. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Proposes [[two-tier-submodel-partition|TSPF]] for robust UAV-swarm [[uav-forest-fire-detection|forest-fire detection]]. UAVs are graph-colored into spatially dispersed groups, back up data within each group, select group servers dynamically, and train partitioned submodels through two-tier federated aggregation so the swarm can keep training when some UAVs are destroyed.

## Problem

Forest-fire detection needs fast edge inference in harsh, failure-prone environments. Centralized learning can be communication-heavy, while standard [[federated-learning|FL]] and distributed learning can lose data and accuracy when fire-damaged UAVs disappear. The paper asks how a UAV swarm can preserve detection accuracy, reduce communication delay, and remain trainable after node destruction.

## System model

The model uses a swarm of UAVs that collect fire-scene data and carry local model parameters, mission data, and backups for UAVs in the same group. A balanced graph-coloring step assigns UAVs to groups so same-group UAVs are spatially separated; each group has a group server, and the whole swarm has a swarm server. The simulations use a 100-UAV swarm split into 10 groups, with ResNet18 on the FLAME dataset and a reported Jetson Xavier NX feasibility discussion.

## Method

TSPF combines four pieces:

- balanced graph coloring for spatially dispersed group membership;
- intragroup data backup for robustness against destroyed UAVs;
- Dynamic Server Selection (DSS), which chooses group servers using state of charge and spatial-uniformity criteria;
- Two-Tier Federated Learning (TFL), where lower-tier group aggregation handles selected layers and the upper-tier swarm aggregation concatenates partitioned submodels.

## Key findings

- TSPF reports detection accuracy comparable to centralized learning and better than the distributed-learning, FL, and personalized-FL baselines in the parsed experiments.
- The communication-overhead table reports 5.59 MB of transmitted selected parameters for TSPF/PFL versus 11.18 MB full-model transmission for FL/HFL.
- TSPF reduces communication delay and training time relative to centralized and standard-FL baselines, which the paper frames as important for delay-sensitive fire detection.
- Intragroup backup preserves destroyed UAVs' data, while FL/distributed baselines lose the affected local datasets.
- The reported ablation selects group count chi = 10 and partition number tau = 2 as strong operating points; larger tau values increase fluctuations or degrade accuracy in the parsed figures.
- Robustness declines as fewer UAVs survive, but TSPF maintains model training under reduced surviving-node counts better than the baselines.

## Limitations / future work

The paper names three follow-up directions: a more specific backup mechanism, topology recovery and path planning when destroyed UAVs disrupt connectivity, and privacy-preserving erasure-coding-style backup.

## Relation to the corpus

This source adds robust [[uav-forest-fire-detection]] and [[two-tier-submodel-partition]] to the UAV-swarm line. It complements [[sun-2024-asap-uav-swarm]] and [[qu-ecoei-uav-swarm]], which focus on in-swarm inference, and [[wang-2026-scalable-multiuav-analytics]], which partitions video-analytics DAGs across UAVs. Its redundancy mechanism is data-preservation-oriented, distinct from [[task-redundancy-for-reliability]] where redundant task execution mitigates stochastic processor failures.

## Raw artifacts

- `raw/sources/Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection/Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection.md`
- Original PDF and extracted figures (`images/`) in the same folder.
