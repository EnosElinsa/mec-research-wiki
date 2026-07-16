---
type: source
title: "Distributed and Energy-Efficient Mobile Crowdsensing with Charging Stations by Deep Reinforcement Learning"
authors: ["Chi Harold Liu", "Zipeng Dai", "Yinuo Zhao", "Jon Crowcroft", "Dapeng Wu", "Kin K. Leung"]
year: 2021
url: "https://doi.org/10.1109/TMC.2019.2938509"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, mobile-crowdsensing, unmanned-vehicles, charging-stations, deep-reinforcement-learning, ape-x, energy-efficiency]
related:
  - "[[ape-x-actor-learner-replay]]"
  - "[[uav-assisted-mobile-crowd-sensing]]"
  - "[[uav-charging-scheduling]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[ma-pomdp]]"
  - "[[prioritized-experience-replay]]"
  - "[[jains-fairness-index]]"
  - "[[uav-trajectory-control]]"
  - "[[chi-harold-liu]]"
  - "[[he-2026-memdrl-uav-navigation]]"
  - "[[memory-augmented-multi-uav-navigation]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# Distributed and Energy-Efficient Mobile Crowdsensing with Charging Stations by Deep Reinforcement Learning

## Citation

Liu, C. H., Dai, Z., Zhao, Y., Crowcroft, J., Wu, D., & Leung, K. K. (2021). *Distributed and Energy-Efficient Mobile Crowdsensing with Charging Stations by Deep Reinforcement Learning*. **IEEE Transactions on Mobile Computing**, 20(1), 130-146. DOI: 10.1109/TMC.2019.2938509.

## TL;DR

Introduces e-Divert, a CTDE actor-critic system for unmanned-vehicle crowdsensing with obstacles and charging stations. CNN spatial features, LSTM history, N-step returns, distributed prioritized replay, and an Ape-X actor-learner architecture jointly target collected data, geographic fairness, and total vehicle-plus-charging energy.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Unmanned vehicles navigate a bounded two-dimensional area containing obstacles, finite-data PoIs, and powered charging stations for $T$ sensing slots, starting from a common origin with full batteries.

**Problem & objective**: Learn a distributed navigation policy that maximizes collected data and geographical fairness while minimizing vehicle and charging energy, $\max D_T(\pi),\ \max\omega_T(\pi),\ \min e_T(\pi)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Vehicle heading | $\theta_t^v$ | continuous in $[0,2\pi)$ for UAVs | Movement direction of vehicle $v$ in slot $t$ |
| Movement distance | $l_t^v$ | continuous in $[0,l_{\max}]$ | Distance traveled by vehicle $v$ |
| Charging action | $f_t^v(c)$ | nonnegative station supply | Energy obtained by vehicle $v$ from station $c$ in slot $t$ |
| Control policy | $\pi_v$ | local-observation policy | Maps each vehicle observation to a movement or charging decision |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Vehicle positions remain within the fixed target-area border. |
| C2 | Vehicles avoid obstacles and incur penalties for collision or for taking a slot with neither valid collection nor charging. |
| C3 | Movement actions satisfy $\theta_t^v\in[0,2\pi)$ and $0\leq l_t^v\leq l_{\max}$. |
| C4 | Collected data, fairness, and vehicle plus station energy evolve over the finite horizon, with charging limited by station supply and vehicle battery state. |

**Algorithm**: Use distributed multi-agent actor-critic learning with CNN spatial encoding, LSTM N-step temporal modeling, prioritized replay, and Ape-X multiple actors feeding one learner under centralized training and local execution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] introduced e-Divert, a distributed multi-agent controller for unmanned-vehicle mobile crowdsensing with obstacles and charging stations. The policy chooses continuous movement actions while balancing data collection, Jain fairness, and energy consumed by vehicles and charging stations. CNN spatial features, LSTM history, N-step returns, prioritized replay, and Ape-X asynchronous actors are combined to capture delayed spatial and temporal effects. In simulations, e-Divert improves energy efficiency over MADDPG by 3.62 times when varying vehicle count and 2.36 times when varying charging-station count. The study provides a practical CTDE reference for joint navigation, sensing, and replenishment decisions.

## Problem

Unmanned aerial vehicles and driverless cars can sense more reliably than human-carried devices, but their navigation must coordinate finite data at PoIs, obstacles, limited onboard energy, and charging-station visits. The controller must collect data fairly without spending energy on idle or redundant movement.

## System model

- A bounded two-dimensional area contains obstacles, PoIs with finite remaining data, multiple unmanned vehicles, and charging stations with sufficient supply.
- Vehicles start fully charged at a common origin. A continuous action specifies movement direction and distance; low-flying UAVs avoid tall obstacles, while a driverless-car implementation would use road-constrained discrete directions.
- A vehicle observes in-range PoIs, its own position and energy, and global charging-station information, but not hidden PoIs or other vehicles.
- Total energy includes travel, sensing/data collection, and energy supplied by charging stations. The objectives maximize collection and [[jains-fairness-index|Jain fairness]] while minimizing this total.

## Method

e-Divert gives each vehicle actor, critic, target actor, and target critic networks. CNNs encode three spatial state channels, and critics train from global state and joint actions while actors execute locally. [[ape-x-actor-learner-replay]] adds asynchronous environment actors and a single GPU learner; local experience moves into per-vehicle global [[prioritized-experience-replay|prioritized buffers]], and updated parameters synchronize back to actors.

N-step returns look forward across delayed collection or charging rewards, while an LSTM encodes recent movement history. The reward combines fairness-weighted collected-data-per-energy and charging benefit, then penalizes obstacle collisions and slots with neither valid collection nor charging.

## Key findings

- The main simulation uses a `16 x 16` area, 256 uniformly distributed PoIs, 50 initial energy units per vehicle, and `20%` of a PoI's data collected per visit.
- The selected setting uses five Ape-X actors, priority exponent `0.5`, and LSTM sequence length 3; its table row reports collection `0.943`, fairness `0.958`, energy `4.000`, and efficiency `0.181`.
- Across sensing ranges, e-Divert reports average efficiency gains of `27%` over no-Ape-X, `1.58x` over no-LSTM, `4.84x` over MADDPG, and `57.67x` over GA.
- Across one to five vehicles, the corresponding gains are `53%`, `76%`, `3.62x`, and `14.93x`; relative to no-Ape-X it reports `23%` more collection, `17%` more fairness, and `15%` less energy.
- Across one to five charging stations, average gains are `33%`, `48%`, `2.36x`, and `28.77x` over those same baselines.

## Limitations / parse caveats

Evaluation is synthetic simulation; the DJI M100 discussion is feasibility context, not a hardware deployment. Transfer to another city requires retraining rather than demonstrated zero-shot generalization. The GA baseline is run once and lacks native obstacle/charging support in the main 256-PoI case; in the smaller obstacle-free case, its collection and fairness improve substantially but energy remains high. Training is centralized through global critics and one learner, so the system is distributed at execution rather than fully decentralized in training. Several equations and one energy list are OCR-damaged, and terminology alternates between navigation and scheduling. The parse lacks top-level publication metadata; the final 2021 TMC record was verified through the exact-title Crossref entry.

## Relation to the corpus

This source extends [[uav-assisted-mobile-crowd-sensing]] to unmanned vehicles that perform the sensing themselves rather than only assisting human participants. It complements [[shi-2025-aoi-energy-replenishment-multiuav]], where UAVs recharge both sensor nodes and themselves, and [[zhou-2026-a2g-madrl-air-ground-vcs]], which uses UAV-UGV pairs for freshness-aware vehicular crowdsensing. Co-author [[chi-harold-liu]] links this source specifically to the UAV-UGV setting.

## Raw artifacts

- Parse: `raw/sources/Distributed_and_Energy-Efficient_Mobile_Crowdsensing_with_Charging_Stations_by_Deep_Reinforcement_Learning/Distributed_and_Energy-Efficient_Mobile_Crowdsensing_with_Charging_Stations_by_Deep_Reinforcement_Learning.md`
- Origin PDF: `raw/sources/Distributed_and_Energy-Efficient_Mobile_Crowdsensing_with_Charging_Stations_by_Deep_Reinforcement_Learning/Distributed_and_Energy-Efficient_Mobile_Crowdsensing_with_Charging_Stations_by_Deep_Reinforcement_Learning.pdf`
- Figures: `raw/sources/Distributed_and_Energy-Efficient_Mobile_Crowdsensing_with_Charging_Stations_by_Deep_Reinforcement_Learning/images/`
