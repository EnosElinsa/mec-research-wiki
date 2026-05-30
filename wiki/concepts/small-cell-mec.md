---
type: concept
title: "Small-Cell MEC"
tags: [mec, small-cell, terrestrial, edge-server, load-balancing]
related:
  - "[[mobile-edge-computing]]"
  - "[[mobility-aware-offloading]]"
  - "[[load-balancing-uav-mec]]"
  - "[[task-offloading]]"
  - "[[duan-2023-moto-smallcell-offloading]]"
created: 2026-05-31
updated: 2026-05-31
---

# Small-Cell MEC

Integration of [[mobile-edge-computing]] with **small-cell networks**: edge servers are deployed at small-cell base stations (SBSs), so mobile devices offload computation over a short communication distance for fast response and high throughput. The dense, short-range SBS layout is the terrestrial counterpart to the corpus's aerial/UAV edge deployments.

## Characteristic challenges

- **Uneven spatio-temporal load.** Because users are unevenly distributed and highly mobile, per-SBS edge-server loads vary sharply in space and time — motivating **load balancing** across servers ([[load-balancing-uav-mec]] is the UAV-side analogue).
- **Mobility.** Frequent association/log-out makes future loads and user positions unknown in advance, pushing solutions toward online/predictive methods ([[mobility-aware-offloading]]).

## In this wiki

- [[duan-2023-moto-smallcell-offloading]] (MOTO) is the corpus's anchor small-cell-MEC source: it decomposes mobility-aware online offloading into task-offloading control (LSTM) and server grouping for load balancing (Dueling Double DQN), validated on a real WiFi trace.
