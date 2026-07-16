---
type: source
title: "A Predictive UAV Framework for Tracking Fast-Moving Vehicles in Dynamic Environments"
authors: ["Ananya Hazarika", "Mehdi Rahmati"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3639545"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
modeling_card: required
tags: [source, uav-isac, vehicular-networks, target-tracking, gaussian-process-regression, pomdp, maddpg, age-of-information, crlb]
related:
  - "[[dynamic-target-prioritization-metric]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[age-of-information]]"
  - "[[uav-enabled-its]]"
  - "[[cramer-rao-bound]]"
  - "[[maddpg]]"
  - "[[pomdp]]"
  - "[[ma-pomdp]]"
  - "[[angle-dependent-rician-fading]]"
  - "[[he-2026-lscr-uav-relay-tracking]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Predictive UAV Framework for Tracking Fast-Moving Vehicles in Dynamic Environments

## Citation

Hazarika, A., & Rahmati, M. (2026). *A Predictive UAV Framework for Tracking Fast-Moving Vehicles in Dynamic Environments*. **IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)**, 27(3), 3594-3604. DOI: 10.1109/TITS.2025.3639545.

## TL;DR

Proposes a predictive multi-UAV tracking framework for fast-moving vehicles. The framework combines DynaMo trajectory prediction, the Dynamic Target Prioritization Metric (DTPM), CRLB/FIM-based sensing and beamforming optimization, and POMDP-MADDPG control so UAVs prioritize targets whose state is stale, uncertain, off-trajectory, or communication-limited.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A decentralized UAV swarm uses multistatic radar sensing and multi-hop mesh communication to track fast-moving vehicles under occlusion, clutter, and partial observability. UAV-to-UAV links use bandwidth-limited rates with interference, noise, and Rician fading, while each UAV can transmit or receive radar echoes and steer an integrated sensing and communication waveform.

**Problem & objective**: Problem (21) minimizes DTPM-weighted estimation uncertainty, $\min_{\{\mathbf W_k(t),P_k(t)\}}\sum_{m=1}^{M}\operatorname{Tr}(\mathrm{CRLB}^{\mathrm{DTPM}}_m(t))$, and the cooperative POMDP extends this objective with penalties for staleness, CRLB, rate shortfall, and state-estimation error.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Beamforming matrix | $\mathbf W_k(t)$ | complex matrix, power-bounded | Sensing and communication beam of UAV $k$ |
| Transmit power | $P_k(t)$ | continuous, nonnegative and bounded | UAV transmit power used for tracking and mesh communication |
| Joint radar-communication waveform | $\mathbf r_{\mathrm{dfrc},k}(t)$ | complex waveform vector | Integrated sensing and communication signal selected by UAV $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Power | $\lVert\mathbf W_k(t)\rVert_F^2\leq P_k^{\max}$ |
| Data rate | $R_{k,m}(t)\geq R_{\min}$ for every required UAV-target communication link |
| Reliability | $\mathrm{SINR}_{k,m}(t)\geq\delta_{\mathrm{URLLC}}$ |
| Beam structure | $\mathbf W_k(t)=\mathbf a_k(\hat\theta_{m,k}(t))\mathbf w_k^H(t)$ aligns a rank-one beam with the predicted target direction |

**Algorithm**: Predict maneuvering target states and uncertainty with the DynaMo stochastic kinematic and Gaussian-process model; compute DTPM priorities from staleness, trajectory deviation, uncertainty, SINR, and distance; construct the DTPM-weighted FIM; update beamformers and powers by successive convex approximation of the inverse-FIM trace; use the optimized controls within Bayesian belief updates; and train a centralized-critic, decentralized-actor MADDPG policy with the POMDP reward.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hazarika and Rahmati [x] studied decentralized multi-UAV tracking of fast-moving vehicles in dynamic environments with integrated sensing and communication. They formulated DTPM-weighted CRLB minimization over beamforming and transmit power under power, rate, SINR, and beam-alignment constraints, and represented cooperative control as a POMDP. Their framework combines DynaMo motion prediction, freshness-aware target prioritization, successive convex approximation, Bayesian belief updates, and POMDP-MADDPG coordination. Simulations reported a DynaMo RMSE of 0.622 m in Table I, a 68.5 percent average-staleness improvement from DTPM, and nearly 15 percent higher average reward than DQN.

## Problem

Fast-moving vehicles can change speed and heading abruptly, disappear behind occlusions, and generate stale or uncertain tracking data. The paper argues that simple freshness metrics such as [[age-of-information]] are not enough because they ignore trajectory deviation, prediction uncertainty, and link quality.

The target problem is decentralized UAV-swarm tracking under partial observability, limited bandwidth/power, interference, and synchronization constraints.

## System model

- Multiple UAVs use multistatic radar sensing and multi-hop wireless mesh communications to track moving vehicles.
- UAVs can transmit and receive radar echoes.
- Communication quality is modeled with SINR, Rician fading, bandwidth, and rate.
- Target and UAV states include target position, velocity, heading, acceleration, angular velocity, and UAV position/altitude.
- The control problem is represented as a POMDP with Bayesian belief updates.

## Method

The framework has four main components:

- **DynaMo**, a hybrid kinematic-stochastic motion model using SDE dynamics plus Gaussian-process residuals for nonlinear maneuvers and state-dependent uncertainty.
- **DTPM**, a prioritization metric combining elapsed update time, Frechet-distance trajectory adherence, prediction uncertainty, SINR, and distance-aware quality.
- **CRLB/FIM-based sensing, power, and beamforming optimization**, solved through SCA-style linearization.
- **POMDP-MADDPG**, using centralized training and decentralized execution for multi-UAV control under partial observations.

## Key findings

- The parsed simulation uses 15 s runs with 0.1 s intervals; maneuvers at 3-4 s, 6-7 s, 9-10 s, and 12-13 s; Gaussian noise of 0.1 m; `K = 5` UAVs; altitude 30 m; a 500 square-meter area; and 100 training episodes.
- Table I reports DynaMo overall RMSE `0.622 m`, max `1.007 m`, std `0.310`; maneuver RMSE `0.580 m`, max `0.950 m`; MAE `0.601`; and P95 `0.854`.
- The narrative also states DynaMo RMSE `1.5070 m` and max `2.4894 m`, which conflicts with Table I. The table and narrative should be treated as separate reported values rather than merged.
- DTPM reports a 68.5% average staleness improvement. In the parsed comparisons, DTPM stays below 2.0 in one setting and below 3 during complex maneuvers, while UAI bursts exceed 6.
- POMDP-MADDPG reports about 15% higher average reward than DQN, over 25% higher than standard MARL, and 35% state-estimation-accuracy improvement, with training stabilizing around 70 episodes.
- In scalability tests, single-UAV RMSE rises from 0.68 m at `M = 5` to 1.10 m at `M = 40`; adding UAVs lowers RMSE to 0.938 at `K = 2` and 0.753 at `K = 4`.

## Limitations / future work

The local parse is silent on DOI, venue, and year; the bibliographic metadata above is title-matched DOI metadata. The parse has OCR artifacts and conflicting RMSE statements. Code and dataset availability are not present in the parse. Many weights and thresholds remain symbolic in the extracted text, and the reported evidence is primarily simulation-based. Future work in the parse includes non-Gaussian noise, clutter models, particle-filter variants, and broader MARL evaluation.

## Relation to the corpus

This source connects UAV-enabled ITS, ISAC sensing, and multi-agent DRL. Its [[dynamic-target-prioritization-metric]] is a richer freshness metric than plain [[age-of-information]], while its CRLB/FIM optimization links to the sensing-accuracy line represented by [[cramer-rao-bound]]. It is adjacent to [[he-2026-lscr-uav-relay-tracking]], which tracks relay handover in UAV-assisted vehicular networks, and to [[maddpg]]-based vehicular MEC control sources such as [[peng-2020-maddpg-uav-vehicular]].

## Raw artifacts

- Parse: `raw/sources/A_Predictive_UAV_Framework_for_Tracking_Fast-Moving_Vehicles_in_Dynamic_Environments/A_Predictive_UAV_Framework_for_Tracking_Fast-Moving_Vehicles_in_Dynamic_Environments.md`
- Origin PDF: `raw/sources/A_Predictive_UAV_Framework_for_Tracking_Fast-Moving_Vehicles_in_Dynamic_Environments/A_Predictive_UAV_Framework_for_Tracking_Fast-Moving_Vehicles_in_Dynamic_Environments.pdf`
- Figures: `raw/sources/A_Predictive_UAV_Framework_for_Tracking_Fast-Moving_Vehicles_in_Dynamic_Environments/images/`
