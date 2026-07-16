---
type: source
title: "Drone Small Cells in the Clouds: Design, Deployment and Performance Analysis"
authors: ["Mohammad Mozaffari", "Walid Saad", "Mehdi Bennis", "Merouane Debbah"]
year: 2015
url: ""
venue: "IEEE Global Communications Conference (IEEE GLOBECOM)"
modeling_card: required
tags: [source, uav-deployment, drone-cell, uav-base-station, coverage-optimization, air-to-ground-channel-model]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[mozaffari-2016-efficient-multi-uav-coverage]]"
created: 2026-06-04
updated: 2026-07-16
---

# Drone Small Cells in the Clouds: Design, Deployment and Performance Analysis

## Citation

Mozaffari, M., Saad, W., Bennis, M., & Debbah, M. (2015). *Drone Small Cells in the Clouds: Design, Deployment and Performance Analysis*. **IEEE Global Communications Conference (GLOBECOM)**. DOI: not in parse. (Supported by NSF Grant AST-1506297.)

## TL;DR

Derives the **optimal altitude** for a single drone small cell (DSC) that maximizes ground coverage or minimizes required transmit power using the standard air-to-ground (LoS/NLoS) channel model. Extends to two DSCs, finding the **optimal inter-DSC distance** that maximizes combined coverage in both interference-free and full-interference scenarios. Proves analytically that the path-loss function has exactly one local minimum as a function of altitude, so the optimum is unique and efficiently findable.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One or two low-altitude drone small cells provide downlink coverage to ground users in a bounded target area. Air-to-ground links follow a probabilistic LoS/NLoS mean-pathloss model; a single-cell link is noise limited, while the two-cell model treats both interference-free and full-interference operation.

**Problem & objective**: For one DSC, choose altitude $h$ to maximize coverage radius $R(h)$ at fixed transmit power, or equivalently minimize $P_t$ for a required radius $R_c$. For two DSCs, choose feasible altitudes and separation $D$ to maximize their combined covered area.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| DSC altitude | $h$ | continuous, $0<h\le h_{\max}$ | Altitude controlling elevation angle, LoS probability, and pathloss |
| Transmit power | $P_t$ | continuous, positive | Power required to meet the coverage threshold |
| DSC ground position | $\mathbf r_j$ | continuous 2D vector | Horizontal placement of DSC $j$ in the target area |
| DSC separation | $D$ | continuous, nonnegative | Distance between the two DSC ground projections |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| 6 | A ground point is covered when $\gamma(R,h)=P_r/N\ge\gamma_{\mathrm{th}}$ |
| Altitude | The feasible single-DSC solution is $\hat h_{\mathrm{opt}}=\min\{h_{\max},h_{\mathrm{opt}}\}$ |
| 11 | In the interference-free two-DSC case, both coverage disks remain inside the target rectangle and are placed to minimize overlap |
| Interference case | Each covered point must satisfy the DSC downlink SINR threshold while $D$ remains compatible with the target area |

**Algorithm**: Solve the scalar stationarity equation for $\mu_{\mathrm{opt}}=h_{\mathrm{opt}}/R$, apply the altitude cap, and compute the minimum required power from the coverage-boundary pathloss. For two cells, place both DSCs at their feasible optimum altitudes and use the geometric coverage formulas in the interference-free case; with full interference, evaluate the SINR-based coverage as a function of $D$ and select the maximizing separation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mozaffari et al. [x] studied altitude and placement optimization for drone small cells providing downlink coverage over a bounded ground region. They derived the single-DSC altitude that maximizes coverage radius at fixed power, or minimizes transmit power for a prescribed radius, under a probabilistic LoS/NLoS air-to-ground model. Their analysis established that the pathloss has only one local minimum with respect to elevation angle, which makes the feasible altitude optimum unique after applying the platform-height limit. For two DSCs, they characterized the coverage-maximizing separation in both interference-free and full-interference settings and showed numerically that the preferred separation scales with the target-area size.

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
