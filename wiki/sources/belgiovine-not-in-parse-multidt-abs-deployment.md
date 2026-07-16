---
type: source
title: "Better Together: Leveraging Multiple Digital Twins for Deployment Optimization of Airborne Base Stations"
authors: ["Mauro Belgiovine", "Chris Dick", "Kaushik Chowdhury"]
year: ""
url: ""
venue: ""
modeling_card: required
tags: [source, digital-twin, airborne-base-station, ray-tracing, network-planning, uav-communications]
related:
  - "[[multi-digital-twin-network-optimization]]"
  - "[[digital-twin]]"
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[wireless-backhaul]]"
  - "[[uav-trajectory-control]]"
  - "[[low-altitude-intelligent-network]]"
created: 2026-07-11
updated: 2026-07-16
---

# Better Together: Leveraging Multiple Digital Twins for Deployment Optimization of Airborne Base Stations

## Citation

Belgiovine, M., Dick, C., & Chowdhury, K. *Better Together: Leveraging Multiple Digital Twins for Deployment Optimization of Airborne Base Stations*. Venue / year / DOI: **not in parse**.

## TL;DR

Builds a multi-digital-twin workflow for airborne base station deployment. Sionna supplies differentiable ray tracing for gradient-based ABS location, antenna-orientation, and power optimization; NVIDIA Aerial Omniverse Digital Twin (AODT) validates larger mobile-UE scenarios and feeds coverage-drop cases back into Sionna for trajectory-based recovery.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fleet of $N$ airborne base stations at fixed elevation $h$ must navigate through a three-dimensional Tokyo map and serve $M$ circular areas of interest. Sionna supplies differentiable ray-traced coverage and SIR maps for optimization, while AODT simulates mobile UEs and returns coverage-drop traces for recovery planning.

**Problem & objective**: Location control minimizes $\mathcal{L}_p=-\alpha K+\beta P_a+\gamma P_u+\eta P_b$ over $\Theta_l=\{(x_i,y_i)\}_{i=1}^{N}$, combining coverage, AOI attraction, inter-ABS repulsion, and building-collision penalties. With locations fixed, orientation and power control minimizes either the max-min loss $\mathcal{L}_o$ in (15) or the weighted AOI loss $\mathcal{L}_w=-\sum_{m=1}^{M}w_m\operatorname{LSE}(\mathbf{r}_m^*,\beta_L)$ in (19).

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| ABS horizontal location | $\mathbf{p}_i=(x_i,y_i)$ | Continuous at fixed elevation $h$ | Waypoints and final location of ABS $i$ |
| Mechanical azimuth | $\phi_i$ | Continuous angle | Horizontal antenna orientation of ABS $i$ |
| Mechanical tilt | $\theta_i$ | Continuous angle | Vertical antenna orientation of ABS $i$ |
| Transmit power | $P_i^{\mathrm{tx}}$ | Continuous power in watts | Transmit power of ABS $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Fixed altitude | Position optimization is restricted to $\mathbf{p}_i=(x_i,y_i)$ while every ABS hovers at elevation $h$ |
| Separation penalty | $P_u=\sum_j\sum_i\max(0,d_{\min}-\lVert\mathbf{p}_i-\mathbf{p}_j\rVert)$ discourages ABS spacing below $d_{\min}$ |
| Obstacle penalty | $P_b=\sum_i\sum_b\exp\left(\kappa_b(-d_{ib}+c_b)\right)$ penalizes proximity to buildings above the flight-clearance threshold |
| AOI service | AOI attraction changes when $\lVert\mathbf{p}_i-\mathbf{c}_k\rVert<2r_k/3$, and the evaluation counts an AOI as served under the same distance condition |
| AOI weights | Weighted SIR priorities satisfy $w_m\geq0$ and $\sum_{m=1}^{M}w_m=1$ |

**Algorithm**: Adam-based gradient descent first differentiates $\mathcal{L}_p$ to generate obstacle-aware routes and final ABS locations. Sionna then differentiates ray-traced SIR losses with respect to $\{\phi_i,\theta_i,P_i^{\mathrm{tx}}\}$; AODT validates mobile-UE coverage, detects sustained drops below $T_{\min}$, and sends the affected UE route back to Sionna for reaction, stationary, and return trajectory refinement.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Belgiovine et al. [x] studied autonomous airborne-base-station deployment in an urban radio environment using coupled digital twins. Their shared data layer aligns the Tokyo scene, coordinates, RF parameters, device configurations, and simulation outputs between Sionna and NVIDIA AODT. In Sionna, gradient-based losses optimize horizontal ABS routes and locations through coverage, AOI attraction, inter-ABS repulsion, and building-collision terms, followed by antenna-orientation and transmit-power optimization for max-min or weighted AOI SIR. AODT then validates the configurations with mobile UEs and returns sustained coverage drops to a Sionna recovery optimizer. The location method achieved an AOI satisfaction rate above 97% across the reported runs, and the 50-deployment study reported average serving-ABS SIR gains of 12.98 dB, 10.01 dB, and 1.08 dB in AOIs 1, 2, and 4, with reductions of 1.21 dB and 1.70 dB in AOIs 0 and 3. In the mission-critical recovery example, the optimized reaction, stationary, and return trajectory improved received power by up to about six orders of magnitude.

## Problem

UAV-carried base stations can provide temporary or mission-critical coverage, but field deployment is expensive and flight time is limited. A single simulator is not enough: differentiable ray tracing helps optimize, while system-level mobility simulation helps validate whether a deployment remains useful when users move through a detailed urban scene.

## System model

- The implementation bridges Sionna and AODT over the same Tokyo PLATEAU 3-D urban map.
- A Shared Data Layer handles scene-format conversion, coordinate alignment, device-deployment exchange, RF parameter alignment, and power-scale matching.
- The deployment problem includes ABS positions, AOI centers/radii, antenna orientations, transmit powers, UE trajectories, and received-power/SIR validation.
- A recovery mode detects mission-critical UE coverage drops, extracts the affected UE route segment from AODT, and moves/refines the serving ABS with Sionna optimization.

## Method

The Sionna side uses back-propagation over differentiable ray tracing. Location optimization combines coverage, repulsion, attraction, and collision terms; orientation/power optimization targets max-min or weighted AOI SIR. The AODT side runs multi-UE validation and exports mobility/coverage traces. The recovery loop uses AODT-detected drops to trigger a Sionna-computed reaction, stationary, and return trajectory plus final orientation/power refinement.

## Key findings

- The reported setup uses AODT 1.1.1, Sionna 0.19, 10 ABSs, 5 AOIs, AOI radius 250-300 m, a 5 by 5 grid, 150 m map-edge margin, 400 m minimum ABS separation, 43.0 dBm baseline transmit power, 3.5 GHz carrier, and 500K rays per ABS for AODT validation.
- AODT validation uses 60 s simulations at 1 s granularity with 50 UEs per AOI.
- Weighted AOI optimization reports +11.51 dB for ABS 1 in AOI 1, +9.57 dB for ABS 9 in AOI 2, and +5.17 dB for ABS 5 in AOI 4, while AOI 0 and AOI 3 degrade by less than 0.5 dB in the cited comparison.
- Across 50 deployments, average gains are +12.98 dB, +10.01 dB, and +1.08 dB for AOIs 1, 2, and 4, with -1.21 dB and -1.70 dB for AOIs 0 and 3.
- Location optimization takes 0.0371 s per iteration and about 92.75 s for 2500 iterations; orientation/power optimization is about 15 s per iteration. Mission planning time is stated as 2-5 minutes.
- In the recovery scenario, a coverage drop from `t_s = 22` to `t_e = 44` is addressed with up to about 6 orders of magnitude receive-power improvement.

## Limitations / parse caveats

The local parse lacks publication year, venue, and DOI metadata. Several tables have OCR corruption, including broken checkmarks, labels, and math symbols, so the page uses prose-supported and clearly parsed numeric values. The work is simulation/digital-twin validation, not a real UAV flight deployment.

## Relation to the corpus

This source extends the [[digital-twin]] thread from edge-service synchronization into RF-planning infrastructure. It complements [[drone-cell-3d-placement]] by replacing stylized placement formulas with ray-tracing digital twins, and contributes [[multi-digital-twin-network-optimization]] as a reusable pattern for using one twin to optimize and another to validate or feed back failures.

## Raw artifacts

- `raw/sources/Better_Together_Leveraging_Multiple_Digital_Twins_for_Deployment_Optimization_of_Airborne_Base_Stations/Better_Together_Leveraging_Multiple_Digital_Twins_for_Deployment_Optimization_of_Airborne_Base_Stations.md`
- Original PDF and extracted figures (`images/`) in the same folder.
