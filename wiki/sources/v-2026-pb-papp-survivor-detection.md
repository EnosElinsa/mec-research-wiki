---
type: source
title: "PB-PAPP: An Efficient Mechanism for Real-Time Survivor Detection in Disaster Regions"
authors: ["Gowry Sailaja V", "Soumajit Pramanik", "Subhajit Sidhanta", "Nirnay Ghosh"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3649563"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 6, pp. 8655-8666"
tags: [source, disaster-response, survivor-detection, uav-path-planning, edge-intelligence, distributed-learning]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[prediction-based-priority-aware-path-planning]]"
  - "[[tree-structured-weight-synthesis]]"
  - "[[post-disaster-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[federated-learning]]"
created: 2026-07-14
updated: 2026-07-14
---

# PB-PAPP: An Efficient Mechanism for Real-Time Survivor Detection in Disaster Regions

## Citation

V, G. S., Pramanik, S., Sidhanta, S., & Ghosh, N. (2026). *PB-PAPP: An Efficient Mechanism for Real-Time Survivor Detection in Disaster Regions*. **IEEE Transactions on Mobile Computing, 25**(6), 8655-8666. DOI: 10.1109/TMC.2025.3649563.

## TL;DR

Combines online logistic-regression prediction of potential survivor locations, a priority-aware Clarke-Wright routing heuristic, and periodic model-weight averaging across mother drones to guide surveillance drones through a simulated disaster grid.

## Problem and system model

The disaster region is a directed grid whose cells have predicted survivor probabilities. Surveillance drones start and return to launch cells, scan with onboard cameras and compute, and must stay within path budgets without duplicate visits. The objective is to maximize expected detected survivors.

The deployment has surveillance drones, more capable mother drones, and a ground base station. Drones move in eight grid directions or hover; A* bypasses static obstacles and altitude changes handle dynamic ones. The framework assumes fair weather, GPS, and static survivors.

## Method

The first module trains logistic regression on neighborhood survivor counts, candidate-PSL counts, and traversal features. Its normalized probabilities become priority scores for [[prediction-based-priority-aware-path-planning|PB-PAPP]], which modifies Clarke-Wright savings and route merging so high-value cells are visited earlier.

The third module, [[tree-structured-weight-synthesis]], periodically averages mother-drone classifier coefficients at the ground station and redistributes them. Despite the decentralized data collection, this aggregation has a central authority and is closely related to FedAvg rather than a fully decentralized consensus protocol.

## Key findings

- In the reported grid experiment, PB-PAPP reaches 82.63% survivor identification by step 90, narrowly above A* at 82.31% and D* at 81.05%; its advantage is larger at several intermediate steps.
- PB-PAPP reports 0.0073 s elapsed time and 0.0076 s CPU time per iteration, the lowest of the evaluated methods, but also the highest average memory use at 137.54 MB.
- Relative elapsed-time reductions range from 39.11% against A* to 97.03% against Christofides; the paper's broader 84%-97% headline applies to selected slower baselines rather than every comparator.
- Weight synthesis, FedAvg, and FedProx have nearly comparable reported accuracies; weight synthesis shows only a slight standard-error reduction.

## Limitations

Evaluation uses synthetic Pygame grids rather than a disaster deployment. PB-PAPP is designed for sparse, non-uniform survivor distributions and may scale poorly to larger grids because PSL allocation depends on a radius hyperparameter. Survivors are static, collision handling is simplified, and the claimed onboard suitability is not validated on airborne hardware.

## Relation to the corpus

This source adds prediction-guided search to [[post-disaster-mec]] and complements SAGIN search-and-rescue papers that optimize offloading and flight control. Its edge contribution is the tight iteration between local observations, lightweight prediction, route reprioritization, and model aggregation rather than a communication-resource optimizer.

Within [[aerial-federated-aggregation-design-space]], [[zhong-2026-hierarchical-ota-fl]] supplies a mechanism-level contrast: PB-PAPP centrally averages complete logistic-regression coefficients and feeds them back into prediction-guided routing, while Zhong controls trajectory to improve analog partial-gradient aggregation.

## Raw artifacts

- Parse: `raw/sources/PB-PAPP_An_Efficient_Mechanism_for_Real-Time_Survivor_Detection_in_Disaster_Regions/PB-PAPP_An_Efficient_Mechanism_for_Real-Time_Survivor_Detection_in_Disaster_Regions.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
