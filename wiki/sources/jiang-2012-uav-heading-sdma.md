---
type: source
title: "Optimization of UAV Heading for the Ground-to-Air Uplink"
authors: ["Feng Jiang", "A. Lee Swindlehurst"]
year: 2012
url: "https://doi.org/10.1109/JSAC.2012.120614"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, uav-base-station, beamforming, sdma, heading-optimization, air-to-ground-channel-model, multi-antenna-uav]
related:
  - "[[air-to-ground-channel-model]]"
  - "[[collaborative-beamforming]]"
  - "[[drone-cell-3d-placement]]"
  - "[[zhan-2011-uav-relay-heading-optimization]]"
created: 2026-06-04
updated: 2026-07-16
modeling_card: required
---

# Optimization of UAV Heading for the Ground-to-Air Uplink

## Citation

Jiang, F., & Swindlehurst, A. L. (2012). *Optimization of UAV Heading for the Ground-to-Air Uplink*. **IEEE Journal on Selected Areas in Communications**, 30(5). DOI: 10.1109/JSAC.2012.120614. (Received 13 July 2011; revised 30 April 2012.)

## TL;DR

Considers a **multi-antenna fixed-wing UAV** acting as an airborne relay collecting uplink data from N co-channel mobile ground nodes via **SDMA** (space-division multiple access using beamforming). The UAV's **heading direction** controls the spatial arrangement of ground node angles of arrival (AoAs), which determines the inter-user interference in the beamforming channel. Develops an adaptive algorithm that adjusts the UAV heading at each discrete time step to **maximize the approximate ergodic sum rate** of the uplink, using a prediction filter to estimate future ground node positions. Asymptotic analysis for strong LoS channels yields simplified low-SNR and high-SNR algorithms with near-optimal performance.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude fixed-wing UAV with a multi-antenna array receives simultaneous uplinks from mobile ground nodes and changes heading to shape their angles of arrival for SDMA beamforming.

**Problem & objective**: Select the next heading to maximize predicted approximate ergodic uplink sum rate, $\max_{\delta_n}\sum_i\log_2(1+\mathbb E_l\{\mathrm{SINR}_{i,n}\})$, or a proportional-fair weighted variant.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV heading | $\delta_n$ | continuous angle in $[0,2\pi]$ | Orientation of the fixed-wing antenna array at step $n$ |
| Fairness weights | $w_{i,n}$ | nonnegative derived weights | Optional proportional-fair emphasis for user $i$ |
| Prediction state | $(\hat x_{i,n},\hat y_{i,n})$ | continuous estimates | One-step ground-node positions used by the heading objective |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Heading slew is bounded, $\|\delta_n-\delta_{n-1}\|\leq\Delta\delta$ |
| C2 | Fixed-wing motion maintains the prescribed altitude and forward speed |
| C3 | The selected heading keeps the UAV within the empirical center-of-gravity distance limit when that safeguard is active |
| C4 | Beamforming and channel assumptions use the available antenna and channel state for the scheduled users |

**Algorithm**: Predict mobile-user positions with a Kalman-like filter, evaluate the sum-rate or proportional-fair heading objective, perform a one-dimensional line search with slew and center-of-gravity safeguards, and use low- and high-SNR asymptotic candidates when appropriate.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Jiang and Swindlehurst [x] optimized the heading of a fixed-wing multi-antenna UAV receiving co-channel uplinks from mobile ground nodes. They maximize predicted approximate ergodic sum rate or a proportional-fair variant over the heading angle under a bounded turn-rate and fixed-altitude, forward-flight model. A position-prediction filter feeds a one-dimensional line search, with center-of-gravity safeguards and low- and high-SNR closed-form approximations. In the reported proportional-fair simulation, SDMA reaches 1.6968 bps/Hz versus 0.5139 bps/Hz for TDMA, an approximately 3.3-fold gain, while both asymptotic methods remain essentially identical to the numerical search across tested SNRs.

## Problem framing

A fixed-wing UAV cannot hover; it must maintain forward velocity. The antenna array at the UAV uses beamforming to separate co-channel ground users. The array's ability to decorrelate user channels depends on the angular separation of the users as seen from the UAV — which changes as the UAV changes heading. Optimizing the heading direction is therefore equivalent to optimizing the geometric configuration of the array relative to the users, which controls interference and sum rate. Prior work assumed static users or interference-free scenarios; this paper adds user mobility and co-channel interference.

## System model

- **UAV:** M-antenna array (fixed-wing, constant altitude and velocity); uses maximum-SINR beamformer per user. **N ground nodes:** single-antenna, mobile, co-channel.
- **Channel:** correlated Rician fading (deterministic LoS + Rayleigh multipath), large-scale path loss ∝ d^{-α}.
- **SINR** at the UAV for user i: SINR_{i,n} = P_t h_{i,n}^H Q_{i,n}^{-1} h_{i,n} (parse Eq. 1), where Q_{i,n} is the interference + noise matrix from other users.
- **Heading optimization:** at each step n, select UAV heading to maximize the approximate ergodic sum rate at step n+1, given predicted user positions (Kalman-like prediction filter).
- **Two multiple access modes compared:** TDMA (time-division) vs SDMA (spatial beamforming).

## Key findings

- Adapting UAV heading in response to ground node positions significantly improves uplink sum rate via SDMA compared to fixed-heading operation (parse abstract + simulation results).
- SDMA with heading optimization dramatically outperforms TDMA (where users share time slots rather than spatial channels) (parse abstract + Section VI).
- Asymptotic analysis yields simplified closed-form heading optimization at low and high SNR, with near-optimal performance relative to the full algorithm (parse Section V + VI).
- The prediction filter enables heading optimization to track mobile users with reasonable accuracy even with noisy position feedback (parse Section IV).

## Limitations / future work

Fixed-wing UAV (cannot hover or change altitude). Perfect channel knowledge at the UAV is assumed (beyond the prediction filter for positions). Results are for a single-cell single-UAV setup.

## Relation to the corpus

An early (2012) UAV heading/trajectory optimization paper for multi-antenna uplink — related to [[zhan-2011-uav-relay-heading-optimization]] from the same era. The SDMA + beamforming approach at the UAV connects to [[collaborative-beamforming]] and multi-antenna aerial platforms. The Rician LoS channel model and multi-user interference management recur in later corpus sources on multi-UAV trajectory and beamforming design.

## Raw artifacts

- `raw/sources/Optimization_of_UAV_Heading_for_the_Ground-to-Air_Uplink/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
