---
type: source
title: "Interference Management in ISAC-SAGINs Based on Transformer-Enabled Mean-Field Reinforcement Learning Method"
authors: ["Yu Yao", "Zekun Lu", "Gaojie Chen", "Chong Huang", "Chenyuan Feng", "Tony Q. S. Quek"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3707527"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, sagin, interference-management, mean-field-marl, transformer, stackelberg-game, beamforming, uav-trajectory-control]
related:
  - "[[transformer-encoded-mean-field-reinforcement-learning]]"
  - "[[post-decision-state-stackelberg-actor-critic]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[mean-field-game]]"
  - "[[stackelberg-game]]"
  - "[[transformer-encoder]]"
  - "[[uav-trajectory-control]]"
  - "[[device-association]]"
  - "[[spatially-separated-uav-isac-role-scheduling]]"
  - "[[cooperative-isac-transceiver-beamforming]]"
  - "[[tony-q-s-quek]]"
created: 2026-07-13
updated: 2026-07-13
---

# Interference Management in ISAC-SAGINs Based on Transformer-Enabled Mean-Field Reinforcement Learning Method

## Citation

Yao, Y., Lu, Z., Chen, G., Huang, C., Feng, C., & Quek, T. Q. S. (2026). *Interference Management in ISAC-SAGINs Based on Transformer-Enabled Mean-Field Reinforcement Learning Method*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3707527.

## TL;DR

Models spectrum-sharing interference in an integrated sensing-and-communication space-air-ground network as a satellite-leader, UAV-follower Stackelberg game. A shared actor-critic architecture uses a Transformer to encode the unordered follower state-action population and a post-decision state to connect leader and follower updates. The reported gains are simulation results for the learned policy; the paper does not establish existence, uniqueness, or convergence to a Stackelberg equilibrium.

## Problem

A LEO satellite tier and a multi-UAV ISAC tier reuse spectrum, so satellite users, UAV users, sensing transmissions, echoes, and clutter create coupled cross-tier and intra-tier interference. The paper seeks long-term rate improvements while preserving user-rate, power, sensing-SINR, association, role-selection, mobility, and collision constraints under imperfect satellite CSI.

## System model

- One multi-antenna LEO satellite serves $M$ satellite users, while $N$ multi-antenna UAVs serve $K$ UAV users and sense one target.
- One UAV is selected to receive sensing echoes; the remaining UAVs transmit communication and sensing signals. User association and the sensing-receiver role are decision variables.
- Satellite links include directional gain, free-space and rain attenuation, outdated CSI, and Gaussian channel-estimation error. UAV-user links use a line-of-sight model.
- The satellite leader optimizes its beamforming for time-average satellite-user sum rate under total-power and worst-case minimum-rate constraints.
- UAV followers jointly choose 3-D trajectories, communication and sensing beamformers, association, sensing role, and receive filtering to improve worst-CSI time-average UAV-user sum rate.

## Method

- **Transformer-enabled mean-field RL.** [[transformer-encoded-mean-field-reinforcement-learning]] represents follower interactions with self-attention over state-action tokens instead of an explicit full joint-action model. Leader and followers use shared actor-critic components, replay buffers, and target networks.
- **Post-decision coupling.** [[post-decision-state-stackelberg-actor-critic]] inserts a state after the leader action and before the follower response, allowing the follower policy and value updates to condition on the leader's committed decision.
- **Constraint handling.** The reward combines rate objectives with penalties for power, minimum rate, sensing, assignment, movement, and collision violations.

The paper presents empirical reward convergence. It does not prove that the learned policies recover a Stackelberg equilibrium, and Transformer attention retains quadratic complexity in the follower-token count, $O(N^2d)$, rather than sublinear scaling.

## Key findings

- In the reported reward comparison, T-MFRL improves the converged reward by 18.4% over MAPPO, 21.3% over MFRL, and 54.2% over DQN-MARL. The abstract describes the 54.2% value as a rate improvement, but the corresponding result is presented as reward; the stronger rate interpretation is therefore not adopted here.
- At a 1 dB sensing-SINR threshold, the reported UAV-user sum-rate gain is 20.8% over trajectory-only optimization and 28.5% over scheduling-only optimization.
- The prose reports UAV-tier sum rate rising from 20.2 to 32.5 bit/s/Hz when the UAV count grows from 5 to 15, while the plotted bars appear closer to 21 and 31.5 bit/s/Hz. The prose values and figure are not numerically consistent.
- Table V reports training latency of 29.99, 50.97, 268.76, 312.59, and 399.85 ms for 5, 10, 15, 20, and 25 UAVs; execution latency is 2.1, 3.3, 4.3, 7.4, and 8.2 ms. This conflicts with prose claiming roughly 200 ms training latency at 25 UAVs.

The default simulation covers a 4 km square with 5 UAVs, 10 satellite users, 10 UAV users, 20 GHz carrier frequency, a 50 s flight horizon divided into 0.5 s slots, and a 10 m minimum UAV separation.

## Limitations

The evaluation is simulation-only and does not report random seeds, run counts, hardware, or software. The Gaussian CSI-error model is minimized over in the formulation without a bounded uncertainty set or confidence region, so it should not be read as a quantified worst-case robustness guarantee. The paper motivates decentralization and privacy, but its deployment description uses a central controller that gathers state and outputs the joint action. Additional internal inconsistencies include T-MFRL/T-SMFRL naming, embedding-dimension descriptions, correlation-parameter ranges, and attention-head/layer settings that extend beyond the stated search limits.

## Relation to the corpus

This source connects [[integrated-sensing-and-communication]] and satellite-air-ground interference management to [[mean-field-game|mean-field learning]] and [[stackelberg-game|leader-follower control]]. Unlike the population distribution in [[mean-field-game]], its learned mean field is encoded from follower tokens by [[transformer-encoded-mean-field-reinforcement-learning]]. Its sensing role selection is adjacent to [[spatially-separated-uav-isac-role-scheduling]], while its coupled transmit/receive design relates to [[cooperative-isac-transceiver-beamforming]].

## Raw artifacts

- Parse: `raw/sources/Interference_Management_in_ISAC-SAGINs_Based_on_Transformer-Enabled_Mean-Field_Reinforcement_Learning_Method/Interference_Management_in_ISAC-SAGINs_Based_on_Transformer-Enabled_Mean-Field_Reinforcement_Learning_Method.md`
- Origin PDF: `raw/sources/Interference_Management_in_ISAC-SAGINs_Based_on_Transformer-Enabled_Mean-Field_Reinforcement_Learning_Method/Interference_Management_in_ISAC-SAGINs_Based_on_Transformer-Enabled_Mean-Field_Reinforcement_Learning_Method.pdf`
- Figures: `raw/sources/Interference_Management_in_ISAC-SAGINs_Based_on_Transformer-Enabled_Mean-Field_Reinforcement_Learning_Method/images/`
