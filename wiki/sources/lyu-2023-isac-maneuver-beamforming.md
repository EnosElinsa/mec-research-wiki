---
type: source
title: "Joint Maneuver and Beamforming Design for UAV-Enabled Integrated Sensing and Communication"
authors: ["Zhonghao Lyu", "Guangxu Zhu", "Jie Xu"]
year: 2023
url: "https://doi.org/10.1109/TWC.2022.3211533"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav, isac, trajectory-optimization, beamforming, sca, sdr, feasibility]
related:
  - "[[sensing-feasible-uav-reachability]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[successive-hover-and-fly-trajectory]]"
  - "[[guangxu-zhu]]"
  - "[[jie-xu]]"
modeling_card: required
created: 2026-07-13
updated: 2026-07-16
---

# Joint Maneuver and Beamforming Design for UAV-Enabled Integrated Sensing and Communication

## Citation

Lyu, Z., Zhu, G., & Xu, J. (2023). *Joint Maneuver and Beamforming Design for UAV-Enabled Integrated Sensing and Communication*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2022.3211533.

> **Metadata grounding note.** The parse contains the title and authors but no final DOI, venue, or year. Those fields were verified through the exact-title Crossref record; technical claims below remain parse-grounded.

## TL;DR

Jointly controls a fixed-altitude UAV's horizontal maneuver and its communication/sensing transmit covariances. Sensing-only SDPs identify feasible locations, graph reachability checks endpoint connectivity, and alternating SCA/SDR updates trade weighted user rate against minimum illumination at prescribed sensing points.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude UAV with a vertical ULA serves $K$ ground users and illuminates prescribed ground sensing points over a slotted mission, in either a quasi-stationary location or a mobile endpoint-constrained trajectory.

**Problem & objective**: For the mobile case, maximize average weighted sum rate, $\max_{\{\mathbf q[n]\},\{\mathbf w_k[n],\mathbf R_s[n]\}}\frac1N\sum_n\sum_k\alpha_k\log_2(1+\gamma_k[n])$, while meeting sensing beampattern gains.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV path | $\mathbf q[n]$ | continuous 2-D position | Horizontal location at slot $n$ |
| User beams | $\mathbf w_k[n]$ | complex vectors | Information beam for user $k$ |
| Sensing covariance | $\mathbf R_s[n]$ | positive semidefinite matrix | Dedicated sensing signal covariance |
| Lifted covariance | $\mathbf W_k[n]$ | positive semidefinite, rank one before relaxation | Lift of $\mathbf w_k[n]\mathbf w_k[n]^H$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Sensing points receive minimum beampattern gain, $\mathbf a^H(\mathbf q[n],\mathbf m_j)(\sum_k\mathbf W_k[n]+\mathbf R_s[n])\mathbf a(\mathbf q[n],\mathbf m_j)\geq d^2(\mathbf q[n],\mathbf m_j)\Gamma$. |
| C2 | Total transmit power is bounded, $\sum_k\|\mathbf w_k[n]\|^2+\mathrm{tr}(\mathbf R_s[n])\leq P_{\max}$. |
| C3 | The mobile path has fixed endpoints and per-slot displacement $\|\mathbf q[n+1]-\mathbf q[n]\|\leq V_{\max}$. |
| C4 | Information covariances are positive semidefinite and rank one before SDR; the sensing covariance is positive semidefinite. |

**Algorithm**: Use sensing-only SDPs to build feasible locations and graph DFS reachability between endpoints, update beam covariances with SCA and SDR, update the trajectory with trust-region SCA, and alternate the two blocks until the weighted-rate increase is below tolerance.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lyu et al. [x] studied a UAV-enabled ISAC access point with a vertical ULA that serves ground users while illuminating prescribed sensing locations. They formulated weighted sum-rate maximization over the UAV location or trajectory and communication and sensing covariances, subject to beampattern, power, endpoint, and flight-step constraints. Sensing-only semidefinite programs and graph reachability first test feasible deployment paths, after which alternating SCA and SDR updates refine beamforming and a trust-region SCA trajectory block. Numerical results show that the joint maneuver design outperforms straight-flight and other heuristic trajectories while exposing the expected rate loss as the sensing threshold increases.

## Problem and system model

- One UAV carries a vertically mounted uniform linear array, serves fixed single-antenna users, and illuminates fixed ground sensing locations over a slotted horizon.
- Transmission combines one beam per user with a general-rank dedicated sensing covariance. Both components contribute to the transmit beampattern, while users treat other beams and the sensing signal as interference.
- The quasi-stationary problem optimizes one horizontal location and the beam covariances. The mobile problem adds fixed endpoints and a per-slot displacement bound and maximizes average weighted sum rate.
- Sensing is a minimum transmit-beampattern-gain constraint. The model has no echo channel, receiver, reflection coefficient, detection probability, or estimation-error metric.

## Method

At each candidate location, a sensing-only SDP decides whether available power can illuminate every sensing point. [[sensing-feasible-uav-reachability]] connects candidate feasible locations within one-slot movement distance and uses depth-first search to test endpoint connectivity. Given a location, the beamforming block lifts information covariances, lower-bounds rates by SCA, and drops rank constraints by SDR. Proposition 4.1 recovers rank-one information beams by moving residual covariance into the dedicated sensing signal.

The mobile solver alternates per-slot beamforming with trust-region SCA trajectory updates initialized from a fly-hover-fly path. The objective is bounded and nondecreasing under accepted updates, but the paper does not prove a global optimum, uniqueness, or convergence to a stationary point of the original problem. The reachability argument establishes graph connectivity as written, without explicitly bounding path hops by the available `N-1` movements.

## Key findings

- The text reports convergence in about **12 iterations**; Fig. 5 visually rises from roughly 7.64 to 8.27 bit/s/Hz.
- At a `-10 dBm` sensing threshold, Fig. 10 visually shows about **8.0 bit/s/Hz** for the proposed trajectory, 7.8 for fly-hover-fly, and 5.6 for straight flight.
- At 20 antennas, Fig. 11 visually shows roughly **15.5**, **15.2**, and **7.4 bit/s/Hz** for the same three designs.

Except for the iteration count, these are plot-read estimates rather than exact text-reported values. The default simulation uses a 1 km square, 8 users, 18 sensing locations, 12 antennas, 100 m altitude, 30 m/s maximum speed, and 0.5 W power.

## Limitations / interpretation

The study is simulation-only and assumes one UAV, fixed altitude, fixed users/targets, deterministic LoS propagation, and perfect geometry/channel knowledge. It omits blockage, fading, CSI error, propulsion energy, orientation dynamics, and target mobility. Computational complexity, location-search resolution, mission duration, solver/hardware details, seeds, and run counts are not in the parse.

The paper mixes the dimensionless no-sensing case `Gamma=0` with thresholds stated in dBm and labels a modeled transmit beampattern as “receive” gain in captions. The trust-region prose and pseudocode also differ on when the radius shrinks and how the inner loop terminates. Rank-one recovery is exact for each convex surrogate, not a global guarantee for the original joint design.

## Relation to the corpus

This source adds a feasibility layer to [[integrated-sensing-and-communication]]: it first asks where sensing illumination is possible and reachable, then performs [[alternating-optimization-sdr-sca]]. Its maneuver is geometry-driven [[uav-trajectory-control]], while the fly-hover-fly path is an initialization/baseline rather than the full multi-location [[successive-hover-and-fly-trajectory]] construction.

## Raw artifacts

- Parse: `raw/sources/Joint_Maneuver_and_Beamforming_Design_for_UAV-Enabled_Integrated_Sensing_and_Communication/Joint_Maneuver_and_Beamforming_Design_for_UAV-Enabled_Integrated_Sensing_and_Communication.md`
- Origin PDF and extracted figures (`images/`) in the same folder.
