---
type: source
title: "Distributed Energy-Efficient Multi-UAV Navigation for Long-Term Communication Coverage by Deep Reinforcement Learning"
authors: ["Chi Harold Liu", "Xiaoxin Ma", "Xudong Gao", "Jian Tang"]
year: 2020
url: "https://doi.org/10.1109/TMC.2019.2908171"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, multi-uav, communication-coverage, deep-reinforcement-learning, energy-efficiency, trajectory-control, fairness]
related:
  - "[[uav-trajectory-control]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[ma-pomdp]]"
  - "[[ddpg]]"
  - "[[jains-fairness-index]]"
  - "[[wireless-backhaul]]"
  - "[[chi-harold-liu]]"
  - "[[he-2026-memdrl-uav-navigation]]"
  - "[[memory-augmented-multi-uav-navigation]]"
  - "[[ye-2023-graph-uav-coverage]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# Distributed Energy-Efficient Multi-UAV Navigation for Long-Term Communication Coverage by Deep Reinforcement Learning

## Citation

Liu, C. H., Ma, X., Gao, X., & Tang, J. (2020). *Distributed Energy-Efficient Multi-UAV Navigation for Long-Term Communication Coverage by Deep Reinforcement Learning*. **IEEE Transactions on Mobile Computing**, 19(6), 1274-1285. DOI: 10.1109/TMC.2019.2908171.

## TL;DR

Uses one continuous actor-critic controller per UAV to sustain fair communication coverage over a gridded service region while limiting movement energy and penalizing border or connectivity violations. Critics train from global state and joint actions, but each UAV executes its actor from local observations.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Fixed-altitude UAVs act as mobile base stations over a two-dimensional region of $K$ points of interest (PoIs) for $T$ slots, with peer links for network connectivity and an access point for backhaul.

**Problem & objective**: Navigate all UAVs to maximize temporal coverage and geographical fairness while minimizing movement energy, $\max c_T,\ \max f_T,\ \min e_T$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Flight direction | $\vartheta_i^t$ | continuous in $[0,2\pi)$ | Heading selected by UAV $i$ in slot $t$ |
| Flight distance | $l_i^t$ | continuous in $[0,l_{\max}]$ | Movement length, with zero denoting hover |
| Distributed policy | $\pi_i$ | local-observation policy | Maps each UAV observation to its direction-distance action |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | UAV positions remain inside the target region at every slot. |
| C2 | Each UAV keeps a peer connection, with inter-UAV distance no larger than the communication range $R$. |
| C3 | Actions obey $\vartheta_i^t\in[0,2\pi)$ and $0\leq l_i^t\leq l_{\max}$. |
| C4 | The fixed-altitude coverage radius satisfies $R'\leq R$ while movement energy is accumulated over $T$ slots. |

**Algorithm**: Formulate a multi-agent partially observable control problem with one actor and critic per UAV; train critics from global state and joint actions, then execute local actors with a shared coverage-fairness-per-energy reward and violation penalties.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] developed a distributed deep-reinforcement-learning controller for multiple UAV base stations that must maintain long-term communication coverage. Each UAV selects a continuous direction and flight distance, while the shared reward combines incremental coverage, Jain fairness, and movement energy with penalties for border and connectivity violations. Centralized critics use the global state and joint actions during training, whereas local actors control UAVs independently at execution. Simulations report energy-efficiency gains of 13.6% to 19.1% over DRL-EC3 across coverage radii, with a 13% coverage improvement at a representative movement-energy setting. The work is an early CTDE-style reference for fair, energy-aware multi-UAV navigation.

## Problem

Multiple UAVs act as mobile base stations for long-duration coverage without a continuously available ground controller. Coverage must remain geographically balanced across points of interest (PoIs), yet movement consumes energy and every UAV must remain inside the service area and connected to at least one peer.

## System model

- A two-dimensional area is divided into cells with one PoI at each cell center; fixed-altitude UAVs serve PoIs inside coverage radius `R'` and communicate inside radius `R`, where `R' <= R`.
- A task lasts `T` slots. Each UAV chooses a continuous movement direction and distance up to `l_max`, or hovers.
- Temporal coverage is the fraction of elapsed slots in which each PoI has been covered. Overall coverage averages this value across PoIs, and geographical equity uses [[jains-fairness-index|Jain's fairness index]].
- Movement energy is proportional to distance. Every UAV must stay within the region and retain at least one inter-UAV link; an access point provides onward [[wireless-backhaul|backhaul]].

## Method

The paper formulates a multi-agent partially observable control problem with one actor, critic, target actor, and target critic per UAV. During training, each critic consumes global state and joint actions, while an actor is updated for its own local observation. Execution therefore follows [[centralized-training-decentralized-execution|centralized training and distributed execution]], although the paper does not use that label.

Actions are direction-distance pairs. Invalid moves are cancelled and penalized. A shared reward multiplies fairness by incremental coverage and divides by incremental movement energy, then adds per-UAV penalties for leaving the border or becoming disconnected. Training uses off-policy deterministic actor-critic updates, a shared replay buffer, Gaussian exploration noise, and soft target-network updates.

## Key findings

- Simulations use a `10 x 10` region, communication radius `R=5`, 4,000 training episodes, and 500 slots per episode; checkpoints are tested 100 times.
- The selected configuration has two 160-unit hidden layers, replay-buffer size 1 million, and discount factor `0.83`.
- Across coverage radii from `1.75` to `3.0`, reported energy-efficiency gains over DRL-EC3 range from `13.6%` to `19.1%`; average gains are `12%` when varying UAV count and `17.7%` when varying movement-energy cost.
- Energy efficiency begins to saturate beyond six UAVs as coverage overlap grows.
- At movement-energy cost `0.4`, coverage is `0.92` versus `0.79` for DRL-EC3. The paper calls the `0.13` absolute difference a `13%` improvement, so the raw values are retained without reinterpreting the percentage.

## Limitations / parse caveats

Evidence is simulation-only; the GPU setup is training infrastructure, not airborne validation. Coverage is a binary in-range abstraction under an assumed SNR threshold, and physical-layer behavior is outside scope. The parse calls the formulation a POMDP but also describes the environment as fully observable. It also says inference needs no peer observations while a signaling discussion says UAVs exchange location and energy for a global view. Baseline counts drift across the abstract, introduction, and evaluation, and several equations, including hover energy, are OCR-damaged. The parse lacks top-level publication metadata; the final 2020 TMC record was verified through the exact-title Crossref entry.

## Relation to the corpus

This source is an early distributed [[uav-trajectory-control]] and [[ma-pomdp]] anchor for fair aerial coverage. Its coverage-fairness-per-movement-energy reward is distinct from the corpus's [[effective-energy-efficiency]] and [[overall-energy-efficiency]] definitions. It precedes [[zhang-2026-distance-attention-uav-navigation]], which adds history-conditioned obstacle sensing for dense urban navigation, and shares the recurring mobile-crowdsensing/DRL line represented by co-author [[chi-harold-liu]].

## Raw artifacts

- Parse: `raw/sources/Distributed_Energy-Efficient_Multi-UAV_Navigation_for_Long-Term_Communication_Coverage_by_Deep_Reinforcement_Learning/Distributed_Energy-Efficient_Multi-UAV_Navigation_for_Long-Term_Communication_Coverage_by_Deep_Reinforcement_Learning.md`
- Origin PDF: `raw/sources/Distributed_Energy-Efficient_Multi-UAV_Navigation_for_Long-Term_Communication_Coverage_by_Deep_Reinforcement_Learning/Distributed_Energy-Efficient_Multi-UAV_Navigation_for_Long-Term_Communication_Coverage_by_Deep_Reinforcement_Learning.pdf`
- Figures: `raw/sources/Distributed_Energy-Efficient_Multi-UAV_Navigation_for_Long-Term_Communication_Coverage_by_Deep_Reinforcement_Learning/images/`
