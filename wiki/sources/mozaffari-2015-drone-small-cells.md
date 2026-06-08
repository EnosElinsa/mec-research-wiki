---
type: source
title: "Drone Small Cells in the Clouds: Design, Deployment and Performance Analysis"
authors: ["Mohammad Mozaffari", "Walid Saad", "Mehdi Bennis", "Merouane Debbah"]
year: 2015
url: ""
venue: "IEEE Global Communications Conference (IEEE GLOBECOM)"
tags: [source, uav-deployment, drone-cell, uav-base-station, coverage-optimization, air-to-ground-channel-model]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[mozaffari-2016-efficient-multi-uav-coverage]]"
created: 2026-06-04
updated: 2026-06-08
---

# Drone Small Cells in the Clouds: Design, Deployment and Performance Analysis

## Citation

Mozaffari, M., Saad, W., Bennis, M., & Debbah, M. (2015). *Drone Small Cells in the Clouds: Design, Deployment and Performance Analysis*. **IEEE Global Communications Conference (GLOBECOM)**. DOI: not in parse. (Supported by NSF Grant AST-1506297.)

## TL;DR

Derives the **optimal altitude** for a single drone small cell (DSC) that maximizes ground coverage or minimizes required transmit power using the standard air-to-ground (LoS/NLoS) channel model. Extends to two DSCs, finding the **optimal inter-DSC distance** that maximizes combined coverage in both interference-free and full-interference scenarios. Proves analytically that the path-loss function has exactly one local minimum as a function of altitude, so the optimum is unique and efficiently findable.

## Problem framing

Drone small cells (DSCs) — UAVs acting as aerial base stations — offer flexible, rapid deployment for disaster relief, events, and overloaded cells. Unlike ground BSs, their altitude is a controllable degree of freedom that trades off free-space path loss (increases with altitude) against LoS probability (increases with altitude). Finding the optimal altitude that balances these is non-trivial. With multiple DSCs, interference between them further affects coverage, making joint altitude and placement optimization necessary.

## System model

- **Single DSC.** Static low-altitude platform (LAP, below 10 km). Air-to-ground channel: LoS and NLoS components with environment-dependent probabilities P(LoS) = f(elevation angle). Coverage is defined as SNR ≥ threshold γ_th.
- **Coverage probability.** Derived analytically as a function of altitude h and coverage radius R; optimal h found by solving dP_t/dh = 0 (Eq. 8 in parse).
- **Two DSCs.** Both interference-free (maximize coverage area, minimize overlap) and full-interference (account for mutual SINR degradation) scenarios. Optimal inter-DSC distance D derived analytically.
- **Objective.** Maximize coverage area (or equivalently, minimize required transmit power for a fixed coverage radius).

## Method

- Analytical derivation using the standard ITU air-to-ground path loss model (LoS/NLoS with additive shadowing).
- **Proposition 1** (parse Section II-B): proves the path-loss–vs–altitude function has at most one local minimum, establishing uniqueness of the optimal altitude.
- For two DSCs: geometric analysis gives closed-form expressions for maximum coverage area when circles overlap vs. do not overlap (Eqs. 12–13 in parse).
- For the interference case: optimal DSC separation derived accounting for SINR degradation from the other DSC.

## Key findings

- There exists a **unique optimal altitude** for a single DSC that maximizes coverage radius for a fixed transmit power (parse Proposition 1 and Section II-B).
- For two interference-free DSCs, coverage is maximized when each is at its individual optimal altitude and their coverage circles are as far apart as possible while staying within the target area (parse Section III-A).
- In the interference case, the optimal inter-DSC distance is shorter than the interference-free case, reflecting the need to increase SINR by reducing path loss (parse Section III-B).
- Numerical results confirm the existence of an optimal altitude/separation and provide insights on deployment parameter tuning.

## Limitations / future work

Conference paper; limited to static DSCs (no trajectory), at most two DSCs in the analytical treatment, and static ground users. The more general multi-UAV deployment with M > 2 is addressed in the companion journal paper [[mozaffari-2016-efficient-multi-uav-coverage]]. No energy consumption model for UAV propulsion.

## Relation to the corpus

Companion/precursor to [[mozaffari-2016-efficient-multi-uav-coverage]], which extends to M > 2 UAVs via circle packing theory. Together these papers establish the foundational [[drone-cell-3d-placement]] framework and [[air-to-ground-channel-model]] used throughout the UAV-communication corpus. The optimal-altitude result (unique, analytically tractable) is widely cited in UAV deployment papers across the corpus.

## Raw artifacts

- Parse: `raw/sources/Drone_Small_Cells_in_the_Clouds_Design_Deployment_and_Performance_Analysis/full.md`
- Origin PDF: `raw/sources/Drone_Small_Cells_in_the_Clouds_Design_Deployment_and_Performance_Analysis/b019ad77-4751-4aa5-af30-e76dc961c962_origin.pdf`
- Figures: `raw/sources/Drone_Small_Cells_in_the_Clouds_Design_Deployment_and_Performance_Analysis/images/`
