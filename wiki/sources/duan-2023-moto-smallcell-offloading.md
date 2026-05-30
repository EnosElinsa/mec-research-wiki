---
type: source
title: "MOTO: Mobility-Aware Online Task Offloading With Adaptive Load Balancing in Small-Cell MEC"
authors: ["Sijing Duan", "Feng Lyu", "Huaqing Wu", "Wenxiong Chen", "Huali Lu", "Zhe Dong", "Xuemin Shen"]
year: 2023
url: "https://doi.org/10.1109/TMC.2022.3220720"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, small-cell-mec, mobility-aware-offloading, task-offloading, load-balancing, deep-reinforcement-learning, lstm, trace-driven]
related:
  - "[[small-cell-mec]]"
  - "[[mobility-aware-offloading]]"
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[ddqn]]"
  - "[[deep-q-network]]"
  - "[[load-balancing-uav-mec]]"
created: 2026-05-31
updated: 2026-05-31
---

# MOTO: Mobility-Aware Online Task Offloading With Adaptive Load Balancing in Small-Cell MEC

## Citation

Duan, S., Lyu, F., Wu, H., Chen, W., Lu, H., Dong, Z., & Shen, X. (2023). *MOTO: Mobility-Aware Online Task Offloading With Adaptive Load Balancing in Small-Cell MEC*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2022.3220720. (Manuscript received 24 June 2022; date of publication 8 November 2022; date of current version 5 December 2023 → year 2023 per the date-of-current-version convention.)

## TL;DR

In a **small-cell MEC** system, mobile-device mobility produces uneven spatio-temporal loads on edge servers. The paper investigates **mobility-aware online task offloading with adaptive load balancing** to minimize total computation cost. The intractable Task Offloading Optimization (TOO) problem is decomposed into two sub-problems — **Task offloading Control (ToC)** and **Server Grouping (SeG)** — and solved online by **MOTO**, which pairs an **LSTM**-based predictor (ToC) with a **Dueling Double DQN (D3QN)**-based scheme (SeG). Trace-driven experiments on a real WiFi dataset show lower computation cost and better load balancing than the benchmarks (qualitative; specific curves in the paper).

## Problem framing

Mobile users in small-cell networks are unevenly distributed with differentiated, time-varying request patterns, so edge-server loads fluctuate as devices frequently associate/log out. The paper argues prior work studies either offloading *or* load balancing, rarely both, and rarely accounts for user mobility or a data-driven model design. It motivates the study with analytics over a real WiFi dataset (per the parse: 29,284,966 association records from 21,725 users across 4,045 APs), observing that (1) most association durations are short (>80% under ~600 s, read from the parse's CDF figure) and (2) loads are spatially and temporally uneven.

## System model

- **Setting.** Small-cell MEC: edge servers deployed at small-cell base stations; mobile devices offload computation-intensive tasks under reduced communication distance.
- **Objective.** Minimize total computation cost of mobile devices subject to dynamic, unknown future mobility and server loads.
- **Decomposition.** The original TOO problem is transformed and split into **ToC** (offloading decisions adapting to user mobility) and **SeG** (grouping MEC servers to balance spatially/temporally uneven loads).
- **Complexity (per parse).** ToC and SeG time costs are stated as within $O(\log(n/m))$ and $O(m)$ respectively (n users, m servers), so the scheme is described as adaptive online with low time complexity.

## Method

- **ToC — LSTM-based algorithm.** A Long Short-Term Memory model predicts future conditions to drive online offloading control.
- **SeG — Dueling Double DQN (D3QN).** Server grouping for load balancing is cast as a learning problem and solved with a D3QN agent (a dueling-network double-DQN variant; see [[ddqn]] and [[deep-q-network]]).
- The two components are combined into the online control scheme MOTO (Algorithm 1 in the parse).

## Key findings

- Extensive **trace-driven experiments** on the real-world WiFi dataset show MOTO reduces device computation cost and improves load balancing versus state-of-the-art benchmarks (stated qualitatively; the parse reports comparative curves rather than a single headline number in text).

## Limitations / future work

The parse's introduction states future work is directed at the end of the paper; the conclusion section is not fully captured in the parse beyond the established framing. No explicit quantitative future-work targets are grounded here → `not in parse`.

## Relation to the corpus

A **non-UAV, terrestrial small-cell** MEC entry — distinct from the corpus's UAV-MEC bulk — that nonetheless shares the **DRL-for-offloading** machinery. Its [[ddqn|Double-DQN]] lineage connects to the [[wang-2022-cat-rat-fmec-trajectory|RAT (twin-DQN + PER)]] approach, while its **mobility-aware** framing and **adaptive load balancing** theme give the corpus its first dedicated [[small-cell-mec]] and [[mobility-aware-offloading]] pages; the load-balancing objective parallels the UAV-side [[load-balancing-uav-mec]] notion. Co-author Xuemin Shen also anchors the batch-5 vehicular paper [[peng-2020-maddpg-uav-vehicular]].

## Raw artifacts

- `raw/sources/MOTO_Mobility-Aware_Online_Task_Offloading_With_Adaptive_Load_Balancing_in_Small-Cell_MEC/full.md`
- Original PDF (`657f07e6-4a0e-42c1-80a6-7a7ba943dbe4_origin.pdf`) and extracted figures (`images/`) in the same folder.
