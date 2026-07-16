---
type: source
modeling_card: required
title: "Leveraging UAVs for Coverage in Cell-Free Vehicular Networks: A Deep Reinforcement Learning Approach"
authors: ["Moataz Samir", "Dariush Ebrahimi", "Chadi Assi", "Sanaa Sharafeddine", "Ali Ghrayeb"]
year: 2021
url: "https://doi.org/10.1109/TMC.2020.2991326"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-coverage, vehicular-networks, ddpg, trajectory-control, energy-aware-control]
related:
  - "[[ddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-enabled-its]]"
  - "[[air-to-ground-channel-model]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[ebrahimi-not-in-parse-autonomous-uav-localization-rl]]"
  - "[[mozaffari-2016-efficient-multi-uav-coverage]]"
  - "[[peng-2020-maddpg-uav-vehicular]]"
  - "[[samir-2022-aoi-altitude-scheduling]]"
  - "[[moataz-samir]]"
  - "[[sanaa-sharafeddine]]"
  - "[[chadi-assi]]"
  - "[[ali-ghrayeb]]"
created: 2026-07-13
updated: 2026-07-16
---

# Leveraging UAVs for Coverage in Cell-Free Vehicular Networks: A Deep Reinforcement Learning Approach

## Citation

Samir, M., Ebrahimi, D., Assi, C., Sharafeddine, S., & Ghrayeb, A. (2021). Leveraging UAVs for coverage in cell-free vehicular networks: A deep reinforcement learning approach. *IEEE Transactions on Mobile Computing, 20*(9), 2835-2847. https://doi.org/10.1109/TMC.2020.2991326

The parse omits publication metadata; the exact-title Crossref record supplies the year, venue, DOI, volume, issue, and pages.

## TL;DR

A centralized DDPG controller dispatches and moves UAV base stations along a highway where terrestrial coverage is unavailable. Its weighted reward trades vehicle coverage against the number of active UAVs and their return-to-charge energy margin.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Mobile vehicles traverse a highway outside terrestrial coverage and are served by fixed-altitude UAV base stations connected to an ingress station, with propulsion energy and residual return-to-charge energy modeled.

**Problem & objective**: The deployment formulation minimizes the number of dispatched UAVs, $\min\sum_m\gamma_m$, while preserving vehicle coverage and service quality.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV deployment | $\gamma_m$ | binary, $\{0,1\}$ | Whether UAV $m$ is dispatched |
| Service assignment | $y_{i,m}^n$ | binary | UAV $m$ serves vehicle $i$ in slot $n$ |
| Coverage indicator | $c_{i,m}^n$ | binary | Vehicle meets the rate threshold |
| Return-energy indicator | $z_m^n$ | binary | Residual energy is enough to reach charging |
| UAV trajectory | $w_m^n$ | continuous 2-D position | Horizontal location at slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Coverage requires acceptable rate: $\sum_m y_{i,m}^n r_{i,m}^n\geq r_{min}$. |
| C2 | Each vehicle is served by at most one UAV in a slot. |
| C3 | Movement is speed bounded: $\lVert w_m^{n+1}-w_m^n\rVert\leq v_{max}\Delta t$. |
| C4 | Service assignments require deployment: $y_{i,m}^n\leq\gamma_m$. |
| C5 | A deployed UAV retains enough residual energy to serve and return to its charging station. |
| C6 | Initial UAV positions are fixed by the deployment scenario. |

**Algorithm**: Train a centralized DDPG policy with continuous travel-distance and direction actions, using coverage, deployment, energy, and boundary penalties together with replay, target networks, and exploration noise.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Samir et al. [x] formulate highway coverage as a deployment and trajectory problem for mobile vehicles outside terrestrial service. The model minimizes dispatched UAVs while enforcing rate coverage, one-UAV service, speed, deployment, residual-energy, and initial-position constraints. A centralized DDPG controller selects continuous movement actions and uses penalties to coordinate coverage with return-to-charge energy. The paper reports nearly full coverage with fewer UAVs, a 16% energy reduction at 80% coverage in one setting, and an average 40% coverage gain over fixed or random baselines.

## Problem and system model

A unidirectional highway is divided into slots. Vehicles leave a fixed base station's coverage and are served by UAVs connected to an ingress station through assumed high-capacity FSO or mmWave fronthaul. Vehicle count is Poisson, vehicle speeds follow a truncated Gaussian model, and UAVs move horizontally at fixed altitude.

The model uses orthogonal resources within each UAV and disjoint spectrum between neighboring UAVs, so it does not optimize interference. A vehicle is covered when its instantaneous UAV-served rate reaches a threshold. Links are LoS-dominant with inverse-square large-scale gain; small-scale fading and communication energy are omitted. Propulsion energy determines when a UAV must return to its station.

## Method

The nonstationary MDP state contains vehicle positions and coverage indicators plus UAV positions, deployment status, and residual energy. Each continuous action gives a UAV's travel distance and direction; hovering is allowed. The controller adapts [[ddpg|DDPG]] with actor/critic and target networks, replay, minibatch updates, soft target replacement, and decaying exploration noise. Separate dispatch logic penalizes activating unnecessary UAVs, while closest-distance admission marks vehicles that meet the rate requirement.

## Key findings

- The simulation uses a 5 km highway, 2.4 million slot snapshots, 100 m UAV altitude, and a 50 m/s maximum UAV speed.
- At 12 vehicles/km, the prose reports that 78% average coverage needs two UAVs at an 11 bps/Hz rate threshold and five UAVs at 12 bps/Hz.
- At 12 bps/Hz with five UAVs and 80% average coverage, the energy-aware reward reduces modeled energy by 16% while retaining nearly the same coverage.
- The conclusion reports an average 40% coverage gain over fixed/random deployment and static placement, but does not state the averaging domain or a per-baseline breakdown.

## Limitations

Evidence is simulation-only. The model omits interference, handover, fronthaul impairment, communication energy, small-scale fading, and real traffic traces. “Cell-free” denotes infrastructure-free highway coverage, not cooperative cell-free massive MIMO. The weighted DDPG policy has no global-optimality proof, the optimization display is OCR-damaged, exploration-noise decay conflicts between prose and table, and one figure's density comparator is corrupted. Backhaul stability and seamless handover are future work.

## Relation to the corpus

This source adds energy-aware [[uav-trajectory-control]] for drive-through vehicular coverage. [[mozaffari-2016-efficient-multi-uav-coverage]] supplies an optimization-based coverage contrast, while [[peng-2020-maddpg-uav-vehicular]] studies multi-agent vehicular control with a related actor-critic family.

## Raw artifacts

- Parse: `raw/sources/Leveraging_UAVs_for_Coverage_in_Cell-Free_Vehicular_Networks_A_Deep_Reinforcement_Learning_Approach/Leveraging_UAVs_for_Coverage_in_Cell-Free_Vehicular_Networks_A_Deep_Reinforcement_Learning_Approach.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
