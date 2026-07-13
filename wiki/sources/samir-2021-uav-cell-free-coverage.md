---
type: source
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
created: 2026-07-13
updated: 2026-07-13
---

# Leveraging UAVs for Coverage in Cell-Free Vehicular Networks: A Deep Reinforcement Learning Approach

## Citation

Samir, M., Ebrahimi, D., Assi, C., Sharafeddine, S., & Ghrayeb, A. (2021). Leveraging UAVs for coverage in cell-free vehicular networks: A deep reinforcement learning approach. *IEEE Transactions on Mobile Computing, 20*(9), 2835-2847. https://doi.org/10.1109/TMC.2020.2991326

The parse omits publication metadata; the exact-title Crossref record supplies the year, venue, DOI, volume, issue, and pages.

## TL;DR

A centralized DDPG controller dispatches and moves UAV base stations along a highway where terrestrial coverage is unavailable. Its weighted reward trades vehicle coverage against the number of active UAVs and their return-to-charge energy margin.

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
