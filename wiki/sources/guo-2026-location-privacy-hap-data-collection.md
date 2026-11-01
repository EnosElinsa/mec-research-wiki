---
type: source
title: "Location Privacy-Aware High-Altitude Platforms Data Collection and Trajectory Optimization"
authors: ["Zhiqi Guo", "Fengxiao Tang", "Linfeng Luo", "Ming Zhao", "Nei Kato"]
year: 2026
url: "https://doi.org/10.1109/TCOMM.2025.3649357"
venue: "IEEE Transactions on Communications, 74"
modeling_card: required
tags: [source, high-altitude-platform-station, location-privacy, differential-privacy, iot-data-collection, td3, trajectory-optimization]
related:
  - "[[high-altitude-platform-station]]"
  - "[[trajectory-privacy]]"
  - "[[uav-data-collection]]"
  - "[[td3]]"
  - "[[nei-kato]]"
created: 2026-11-02
updated: 2026-11-02
---

# Location Privacy-Aware High-Altitude Platforms Data Collection and Trajectory Optimization

## Citation

Guo, Z., Tang, F., Luo, L., Zhao, M., & Kato, N. (2026). *Location Privacy-Aware High-Altitude Platforms Data Collection and Trajectory Optimization*. **IEEE Transactions on Communications, 74**. DOI: 10.1109/TCOMM.2025.3649357.

## TL;DR

A HAP collects IoT data over a wide area and relays it in real time through LEO satellites, but its transmissions can reveal its location and trajectory. The paper adds a differential-privacy perturbation to the collection process and learns the HAP's steering decisions with PDCTO, a TD3-based DRL scheme, to maximize collected data under energy, mission, and steering limits.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A HAP at fixed altitude $h_h$ flies from $H_{start}$ to $H_{target}$ over $N$ slots, collecting data from IoT sensors and forwarding it to a data center through satellites. A differential-privacy perturbation alters the transmission rates so an observer cannot infer the HAP's location. Energy covers flight and collection, bounded by capacity $E_{max}$.

**Problem & objective**: P2: $\max_{\Delta\theta_n,f}C^f$, the total data collected under the privacy perturbation, where without privacy P1 maximizes $C=\sum_n C^n_{h,i}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Steering change | $\Delta\theta_n$ | $\lvert\Delta\theta_n\rvert\le\theta_{max}$ | Turning-angle change of the HAP in slot $n$ |
| Heading | $\theta_n$ | $0<\theta_n\le2\pi$ | Flight direction in slot $n$ |
| Privacy perturbation | $f$ | perturbation setting | Location-privacy mechanism applied to transmissions |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (16a)-(16b) | Mission endpoints, $H_h(0)=H_{start}$ and $H_h(N)=H_{target}$. |
| Energy | $E^f\le E_{max}$ for flight and collection under perturbation. |
| (16d) | Heading range, $0<\theta_n\le2\pi$. |
| (16e) | Steering-rate limit, $\lvert\Delta\theta_n\rvert\le\theta_{max}$, for flight stability. |

**Algorithm**: Model P2 as an MDP whose state includes sensor data volumes and HAP status, whose action is the steering change, and whose reward reflects collected data. PDCTO builds on TD3 with twin critics, delayed policy updates, and target smoothing to learn continuous steering actions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Guo et al. [x] proposed a location privacy-aware high altitude platform data collection and trajectory design scheme for Internet of Things devices with limited storage and transmission range. The scheme uses HAPs to cover the collection area quickly and to transmit data in real time via satellites. A differential privacy-based perturbation mechanism is applied to reduce the risk of location information leakage. The privacy-aware trajectory optimization problem, which maximizes data collection under energy and steering constraints, is modeled as a Markov decision process and solved with deep reinforcement learning to determine the movement decisions of the HAP. Experimental results demonstrate that the scheme protects location privacy while maintaining data collection performance close to an unperturbed TD3 baseline across sensor scales and energy capacities.

## Problem framing

Inference attacks on transmission patterns can reveal a data-collecting platform's position. Adding noise reduces leakage but lowers effective collection, so trajectory and privacy must be designed together.

## System model

- Flight altitude is fixed, so only the turning angle is optimized.
- The HAP-satellite-data center path provides real-time delivery.

## Method

PDCTO uses TD3 for the continuous steering action. The optimum of P2 is an upper bound on collection under the privacy mechanism.

## Key findings

- PDCTO keeps data collection close to unperturbed TD3 while protecting location privacy.
- Data collected rises with HAP energy capacity for all compared algorithms.

## Limitations / future work

The authors suggest stronger privacy mechanisms, robustness to sensor localization and channel estimation errors, and POMDP or Bayesian RL formulations.

## Relation to the corpus

Applies [[trajectory-privacy]] to [[high-altitude-platform-station]] data collection, extending the [[uav-data-collection]] vocabulary to stratospheric platforms.

## Raw artifacts

- Parse: `raw/sources/Location_Privacy-Aware_High-Altitude_Platforms_Data_Collection_and_Trajectory_Optimization/Location_Privacy-Aware_High-Altitude_Platforms_Data_Collection_and_Trajectory_Optimization.md`
- Origin PDF and extracted figures are in the same folder.
