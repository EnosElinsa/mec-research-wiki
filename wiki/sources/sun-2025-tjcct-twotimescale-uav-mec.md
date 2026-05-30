---
type: source
title: "TJCCT: A Two-Timescale Approach for UAV-Assisted Mobile Edge Computing"
authors: ["Zemin Sun", "Geng Sun", "Qingqing Wu", "Long He", "Shuang Liang", "Hongyang Pan", "Dusit Niyato", "Chau Yuen", "Victor C. M. Leung"]
year: 2025
url: "https://doi.org/10.1109/TMC.2024.3505155"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-mec, two-timescale-optimization, computation-offloading, uav-trajectory-control, matching-theory, mixed-integer-nonlinear-programming]
related:
  - "[[mobile-edge-computing]]"
  - "[[two-timescale-optimization]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[uav-trajectory-control]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[sun-2024-mvtora-postdisaster-vfc]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[yang-2022-stochastic-uav-mec-lyapunov]]"
created: 2026-05-31
updated: 2026-05-31
---

# TJCCT: A Two-Timescale Approach for UAV-Assisted Mobile Edge Computing

## Citation

Sun, Z., Sun, G., Wu, Q., He, L., Liang, S., Pan, H., Niyato, D., Yuen, C., & Leung, V. C. M. (2025). *TJCCT: A Two-Timescale Approach for UAV-Assisted Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3505155. (Received 6 Jan 2024; date of publication 22 Nov 2024; date of current version 6 Mar 2025. An earlier version appeared at IEEE INFOCOM 2024, DOI: 10.1109/INFOCOM52122.2024.10621095.)

## TL;DR

A **two-timescale** joint computing-resource-allocation, computation-offloading, and trajectory-control approach (**TJCCT**) for UAV-assisted MEC. The paper presents a **hierarchical architecture** coordinating mobile devices (MDs), terrestrial edge, aerial (UAV) edge, and a controller, then formulates a **system-utility maximization** problem that is a non-convex, NP-hard **MINLP**. In the **short timescale** it runs a **price-incentive model** for on-demand computing-resource allocation plus a **matching-mechanism** method for computation offloading; in the **long timescale** it runs a **convex-optimization** method for UAV trajectory control. Stability and polynomial complexity of TJCCT are theoretically proved.

## Problem framing

UAV-assisted MEC must meet computation-intensive, delay-sensitive task demands despite: the demand-supply contradiction between MDs and MEC servers, the demand-supply discrepancy between MDs and MEC servers, trajectory-control requirements on energy efficiency and timeliness, and the **different time-scale dynamics** of the network. The last point motivates a two-timescale formulation: fast resource/offloading decisions vs slow trajectory control.

## System model

- **Hierarchy.** Four-way collaboration — MDs, terrestrial edge, aerial (UAV) edge, and a controller ([[hierarchical-aerial-mec]]).
- **Objective.** Maximize the system utility; the problem is a non-convex NP-hard **MINLP** ([[mixed-integer-nonlinear-programming]]).
- **Timescales.** Short — computing-resource allocation + computation offloading; long — UAV trajectory control ([[two-timescale-optimization]]).

## Method

- **Short timescale:** a **price-incentive model** for on-demand computing-resource allocation, and a **matching-mechanism-based** method for computation offloading ([[matching-theory-for-resource-allocation]]).
- **Long timescale:** a **convex-optimization-based** method for UAV trajectory control ([[uav-trajectory-control]]).
- **Theory:** stability, optimality, and polynomial complexity of TJCCT are proved.

## Key findings

- TJCCT achieves superior **system utility, average processing rate, average completion delay, average completion ratio, and average cost**, while meeting energy constraints (the paper's reported metric set).
- A stated **trade-off**: TJCCT shows **inferior energy consumption** but maintains a balanced, superior **average cost** by optimizing the delay-vs-energy trade-off — well-suited to delay-sensitive, computation-intensive scenarios. It also shows good adaptability in heavy-loaded scenarios and scalability with more MDs (qualitative; specific curves in the paper).
- A supplemental analysis argues the costs of information gathering are minor, and TJCCT still outperforms comparators even when those costs are included (from the parse; supplemental material).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work; it notes the energy-consumption trade-off as the cost of the delay-focused design. Results are simulation-based.

## Relation to the corpus

A **two-timescale aerial-MEC** entry from the Jilin-University / NTU cluster around [[geng-sun]] (with [[zemin-sun]], [[shuang-liang]], [[dusit-niyato]], [[qingqing-wu]]). It complements that group's game-theoretic post-disaster offloading work [[sun-2024-mvtora-postdisaster-vfc]] (which also uses matching + convex methods) and the hierarchical-aerial matching/DRL works such as [[nabi-2025-jour-hierarchical-aerial]]. Its two-timescale decomposition contrasts with the single-timescale Lyapunov online approach of [[yang-2022-stochastic-uav-mec-lyapunov]]. Introduces [[two-timescale-optimization]]; reinforces [[hierarchical-aerial-mec]] and [[matching-theory-for-resource-allocation]].

## Raw artifacts

- `raw/sources/TJCCT_A_Two-Timescale_Approach_for_UAV-Assisted_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
