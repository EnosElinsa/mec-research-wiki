---
type: source
title: "Efficient Deployment of Multiple Unmanned Aerial Vehicles for Optimal Wireless Coverage"
authors: ["Mohammad Mozaffari", "Walid Saad", "Mehdi Bennis", "Mérouane Debbah"]
year: 2016
url: "https://doi.org/10.1109/LCOMM.2016.2578312"
venue: "IEEE Communications Letters (IEEE LCOMM)"
modeling_card: required
tags: [source, uav-deployment, drone-cell, uav-base-station, coverage-optimization, circle-packing, air-to-ground-channel-model]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[mozaffari-2015-drone-small-cells]]"
created: 2026-06-04
updated: 2026-07-16
---

# Efficient Deployment of Multiple Unmanned Aerial Vehicles for Optimal Wireless Coverage

## Citation

Mozaffari, M., Saad, W., Bennis, M., & Debbah, M. (2016). *Efficient Deployment of Multiple Unmanned Aerial Vehicles for Optimal Wireless Coverage*. **IEEE Communications Letters**, 20(8). DOI: 10.1109/LCOMM.2016.2578312. (Received 6 May 2016; accepted 6 June 2016; published 8 June 2016; current version 10 August 2016.)

## TL;DR

Extends the single-DSC optimal-altitude framework to M UAVs. Derives the **downlink coverage probability** as a function of UAV altitude and directional antenna gain (accounting for inter-UAV interference). Uses **circle packing theory** to determine the 3D placement of M UAVs that jointly maximizes total coverage area while ensuring coverage regions do not overlap (eliminating inter-UAV interference). Also determines the **minimum number of UAVs** needed to guarantee a target coverage probability over a given geographical area.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $M$ symmetric stationary UAVs act as downlink aerial base stations over a circular region of radius $R_c$. Each UAV uses the same altitude and transmit power with a directional antenna of half-beamwidth $\theta_B$, and coverage probability accounts for probabilistic LoS/NLoS propagation and mean interference from the nearest UAV.

**Problem & objective**: Choose UAV ground positions $\mathbf r_j$, common altitude $h$, coverage radius $r_u$, and, when provisioning the system, the number $M$, to maximize $M r_u^2$ while using non-overlapping coverage disks and meeting a target coverage probability $\varepsilon$ with minimum transmit power.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Number of UAVs | $M$ | positive integer | Fleet size used to meet an area-coverage target |
| UAV ground position | $\mathbf r_j$ | continuous 2D vector | Center of UAV $j$'s coverage disk |
| Common altitude | $h$ | continuous, positive | Altitude shared by the symmetric UAVs |
| Coverage radius | $r_u$ | continuous, nonnegative | Largest radius satisfying the coverage-probability target |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| 9 | $r_u=\max\{r:P_{\mathrm{cov}}(r,P_t,\theta_B)\ge\varepsilon\}$ |
| 11 | Coverage disks do not overlap: $\lVert\mathbf r_j-\mathbf r_k\rVert\ge2r_u$ for $j\ne k$ |
| 12 | Every coverage disk stays inside the service region: $\lVert\mathbf r_j\rVert+r_u\le R_c$ |
| 13 | The directional footprint is feasible: $r_u\le h\tan(\theta_B/2)$ |

**Algorithm**: Evaluate the analytical coverage probability for candidate $M$, power, altitude, and beamwidth values. Map the placement problem to packing $M$ equal circles inside the service circle, obtain the maximum feasible $r_u$ and centers from the packing construction, set $h=r_u/\tan(\theta_B/2)$, and compute the minimum power meeting $\varepsilon$. Repeat over $M$ and select the smallest fleet that satisfies the required covered-area fraction and lifetime target.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mozaffari et al. [x] studied the three-dimensional deployment of multiple directional-antenna UAV base stations over a circular service area. They derived downlink coverage probability as a function of altitude, antenna gain, probabilistic LoS/NLoS propagation, and mean nearest-UAV interference. They then mapped coverage maximization to equal-circle packing, selecting non-overlapping ground footprints, common altitude, and minimum transmit power to improve both covered area and coverage lifetime. The resulting framework also determines the minimum fleet size needed for a prescribed area-coverage threshold, and the numerical analysis shows that the preferred altitude decreases as more UAVs are deployed.

## Problem framing

A single UAV has limited coverage footprint; deploying M UAVs can cover a larger area, but their transmissions interfere with each other, degrading coverage. Altitude adjustment trades off LoS probability against path loss and feasible coverage radius. The joint design of altitude, 2D placement, and the number of UAVs to use for a target coverage level is the core challenge. The companion conference paper [[mozaffari-2015-drone-small-cells]] treated at most two DSCs analytically; this letter scales to arbitrary M via a clean combinatorial framework.

## System model

- **M UAVs**, symmetric (same transmit power and altitude), each with a directional antenna of half-beamwidth θ_B. A user within range r ≤ h·tan(θ_B/2) of the projection can be served.
- **Coverage probability.** Derived as Theorem 1 (parse Eq. 7): a weighted sum of Q-functions combining LoS and NLoS probabilities, directional gain G_3dB, and mean interference from the nearest UAV.
- **Circle packing.** The deployment problem maps to the circle-packing-in-a-circle problem: find M non-overlapping circles of equal radius r_u inside a circle of radius R_c that maximize packing density. Solutions for M = 1…10 are tabulated (parse Table I).
- **Altitude and power.** Given r_u from the packing solution, altitude is set as h = r_u / tan(θ_B/2); minimum transmit power follows from coverage-SNR requirement.
- **Coverage lifetime.** Defined as proportional to the number of UAVs (each adding a lifetime increment); tradeoffs between coverage area and lifetime are analyzed.

## Method

- Analytical derivation of coverage probability under mean-interference approximation from the nearest UAV (justified by directional antennas making nearest-UAV interference dominant).
- Circle packing in a circle (NP-hard in general); for each M, a specific packing strategy is provided. For M = 3 the equilateral-triangle placement is optimal (parse Section III, r_u ≈ 0.464 R_c).
- Proposition 1 (parse): upper bound on UAV altitude that guarantees non-overlap, as a function of M and R_c.

## Key findings

- Coverage probability depends on UAV altitude through LoS probability, path loss, and feasible coverage radius; an optimal altitude exists for each M and θ_B (parse Theorem 1 and surrounding analysis).
- The circle-packing approach identifies 3D UAV locations that maximize total coverage; for M = 7 UAVs the packing achieves ~77.8% area coverage of a circular region (parse Table I).
- Increasing M beyond a certain point reduces per-UAV coverage radius faster than it adds coverage, so there is a sweet spot for coverage-vs-interference tradeoff (parse Fig. 3 and Table I).
- The minimum number of UAVs to guarantee a target coverage probability can be read off from the circle-packing table for a given R_c and θ_B.

## Limitations / future work

Static UAVs only (no trajectory); symmetric deployment (same altitude, power, beamwidth for all UAVs); mean-interference approximation (exact interference distribution not derived). Users are assumed uniformly distributed in the area; user mobility and dynamic demand are not modeled.

## Relation to the corpus

Journal companion to [[mozaffari-2015-drone-small-cells]] and a foundational reference for [[drone-cell-3d-placement]] across the corpus. The circle-packing framework and the closed-form coverage-probability expression are widely cited in multi-UAV deployment papers. Several corpus sources that optimize UAV placement for MEC coverage (e.g., [[bor-yaliniz-2016-3d-abs-placement]], [[al-hourani-2014-optimal-lap-altitude]]) build on the same air-to-ground channel and altitude-optimization ideas.

## Raw artifacts

- Parse: `raw/sources/Efficient_Deployment_of_Multiple_Unmanned_Aerial_Vehicles_for_Optimal_Wireless_Coverage/full.md`
- Origin PDF: `raw/sources/Efficient_Deployment_of_Multiple_Unmanned_Aerial_Vehicles_for_Optimal_Wireless_Coverage/b3ffb44c-8fe3-4661-904e-1af48c1094af_origin.pdf`
- Figures: `raw/sources/Efficient_Deployment_of_Multiple_Unmanned_Aerial_Vehicles_for_Optimal_Wireless_Coverage/images/`
