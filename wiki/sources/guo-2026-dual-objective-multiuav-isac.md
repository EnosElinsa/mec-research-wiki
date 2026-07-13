---
type: source
title: "Integrated Sensing and Communications in Multi-UAV Networks: A Dual-Objective Optimization Perspective"
authors: ["Xu Guo", "Jingcheng Shi", "Jianjun Wu", "Rongqing Zhang", "Xiang Cheng"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3641375"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, multi-uav, isac, multi-objective-optimization, trajectory-optimization, user-association, target-association, moea-d]
related:
  - "[[dual-objective-multi-uav-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[cramer-rao-bound]]"
  - "[[uav-trajectory-control]]"
  - "[[particle-swarm-optimization]]"
  - "[[genetic-algorithm]]"
  - "[[non-dominated-sorting-genetic-algorithm]]"
  - "[[rongqing-zhang]]"
  - "[[xiang-cheng]]"
  - "[[lu-2026-multiuav-iscpt]]"
created: 2026-07-13
updated: 2026-07-13
---

# Integrated Sensing and Communications in Multi-UAV Networks: A Dual-Objective Optimization Perspective

## Citation

Guo, X., Shi, J., Wu, J., Zhang, R., & Cheng, X. (2026). *Integrated Sensing and Communications in Multi-UAV Networks: A Dual-Objective Optimization Perspective*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3641375.

> **Metadata grounding note.** The parse contains the title and author list but no DOI, venue, or publication year. Those fields were verified through the exact-title Crossref record; the technical claims below remain parse-grounded.

## TL;DR

Jointly optimizes multiple UAVs' 3-D trajectories, transmit powers, communication-user associations, and sensing-target associations without collapsing communication and sensing into one fixed-weight score. The proposed SC-DO-MUOA uses archive-guided MOEA/D plus an adaptive PSO/GA operator to approximate the Pareto front between average communication sum rate and aggregate target-location [[cramer-rao-bound|CRB]].

## Problem framing

In multi-UAV ISAC, moving a UAV toward communication users can improve rate while moving it toward sensing targets can improve localization. Inter-UAV communication and sensing interference, collision/altitude/speed constraints, per-frame rate requirements, and mixed continuous/discrete decisions couple those objectives. A single weighted sum exposes only one preference; this paper keeps both objectives explicit and returns non-dominated alternatives.

## System model

- Multiple UAVs serve independent downlink users and sense independent targets over shared spectrum under centralized ground control.
- Each slot assigns at most one user and one target to each UAV; each user is associated with at most one UAV, and every target must be sensed once per ISAC frame.
- The decision vector combines 3-D trajectories, transmit powers, user association, and target association under power, rate, mobility, altitude, and collision constraints.
- Communication quality is average sum rate. Sensing quality is the sum of target-position CRBs derived from the echo model.

## Method

SC-DO-MUOA decomposes the constrained bi-objective problem into scalar subproblems as in MOEA/D, while an external archive preserves non-dominated feasible solutions. A mixed-variable encoding and repair step handle continuous flight/power variables and discrete associations. When hypervolume improvement remains small for five iterations, the search switches its hybrid update between PSO-style movement and GA-style crossover/mutation. The paper treats this as an evolutionary approximation for an NP-hard problem; it does not prove global optimality.

## Key findings

- In the paper's largest reported case (100 UAVs, 100 users, 20 targets), SC-DO-MUOA reports runtime **5.71 s**, memory **10.97 MB**, convergence at **550 iterations**, and hypervolume **0.88**. EAG-MOEA/D reports 9.05 s / 11.01 MB / 900 / 0.72, while NSGA-II reports 11.39 s / 10.56 MB / 1000 / 0.63 (parse Table III).
- Across the reported scale sweep, the proposed method reaches higher hypervolume in fewer iterations than EAG-MOEA/D and NSGA-II. The exact table values are more informative than the paper's headline percentage comparisons, whose baseline changes between runtime and quality claims.
- The returned archive exposes communication-rate versus sensing-CRB tradeoffs rather than selecting one operating point in advance.

## Limitations / interpretation

Evidence is Monte Carlo simulation only. The model assumes centralized control, known user locations and estimated target positions, simplified LoS/free-space propagation, and omits control-link overhead and field-test latency. Propulsion energy is discussed only in a feasibility study, not optimized. The default-duration prose is OCR-inconsistent (`338` versus 33 s in the parameter table), so 33 s should be treated as table-grounded rather than reconciled silently. Convergence is empirical/termination-based, and the search space can grow exponentially.

## Relation to the corpus

This is an explicit [[dual-objective-multi-uav-isac]] instance: unlike sensing-constrained sum-rate designs, it maintains an inspectable Pareto archive. It extends the corpus's [[integrated-sensing-and-communication]] and [[cramer-rao-bound]] threads with joint multi-UAV movement, association, and power decisions, using a hybrid evolutionary solver rather than DRL or SCA.

## Raw artifacts

- `raw/sources/Integrated_Sensing_and_Communications_in_Multi-UAV_Networks_A_Dual-Objective_Optimization_Perspective/Integrated_Sensing_and_Communications_in_Multi-UAV_Networks_A_Dual-Objective_Optimization_Perspective.md`
- Original PDF and extracted figures (`images/`) in the same folder.
