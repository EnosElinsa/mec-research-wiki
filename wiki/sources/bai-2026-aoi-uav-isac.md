---
type: source
title: "Age of Information Minimization in UAV-Enabled Integrated Sensing and Communication Systems"
authors: ["Yu Bai", "Yifan Zhang", "Boxuan Xie", "Zheng Chang", "Yanru Zhang", "Riku Jantti", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3709576"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, age-of-information, integrated-sensing-and-communication, uav-trajectory-control, soft-actor-critic, beamforming, deep-reinforcement-learning, target-tracking]
related:
  - "[[aoi-centric-uav-isac-beam-control]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[age-of-information]]"
  - "[[soft-actor-critic]]"
  - "[[uav-trajectory-control]]"
  - "[[cramer-rao-bound]]"
  - "[[hazarika-2026-dynamo-uav-vehicle-tracking]]"
  - "[[dynamic-target-prioritization-metric]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[networked-isac]]"
  - "[[zhu-han]]"
created: 2026-07-10
updated: 2026-07-10
---

# Age of Information Minimization in UAV-Enabled Integrated Sensing and Communication Systems

## Citation

Bai, Y., Zhang, Y., Xie, B., Chang, Z., Zhang, Y., Jantti, R., & Han, Z. (2026). *Age of Information Minimization in UAV-Enabled Integrated Sensing and Communication Systems*. **IEEE Transactions on Mobile Computing**, 1-16. DOI: 10.1109/TMC.2026.3709576.

## TL;DR

Makes AoI the objective for UAV-enabled ISAC: a UAV senses a moving target and downlinks fresh target updates to ground users. SAC chooses UAV motion and beam activation priorities, while Kalman prediction, RZF precoding, and waveform post-processing translate the policy output into sensing and communication beams.

## Problem

ISAC studies often optimize sensing accuracy and communication rate without asking whether users receive fresh target-state updates. Prior AoI-UAV-ISAC work is limited by time-division, data-collection, or single-link assumptions, and classical optimization is hard to adapt to user/target dynamics. The paper targets long-term average AoI under UAV motion, sensing, and downlink communication constraints.

## System model

- One fixed-altitude UAV performs target sensing and downlink communication for $K$ ground users.
- The moving target state is unknown and evolves in the horizontal plane.
- The UAV carries a uniform planar array with $M_x M_y$ antennas and obeys velocity/acceleration limits.
- The transmitted waveform superimposes communication and target-sensing components under a power cap.
- A Kalman filter predicts target state, and successful AoI reset requires both reliable sensing of the latest target state and successful decoding by the user.
- The objective minimizes long-term average AoI subject to mobility, power, sensing, communication, and AoI constraints.

## Method

The controller uses SAC for continuous decisions. The action representation contains UAV motion plus beam-priority logits and an adaptive activation threshold; post-processing maps these logits into physical waveforms. The environment update applies Kalman target prediction, channel generation, softmax power allocation, regularized zero-forcing precoding, and SINR evaluation. The reward balances AoI reduction with sensing and communication feasibility.

## Key findings

- In training, SAC converges quickly and reaches the highest final return among the parsed baselines.
- Average AoI increases as the SINR threshold becomes stricter; SAC keeps slightly lower AoI across thresholds.
- Stricter sensing accuracy makes the UAV track the target more closely and increases AoI, while relaxed sensing accuracy improves downlink SINR.
- As $\sigma_{\rm req}$ changes from 0.1 m to 4 m, the parsed table reports radar SNR decreasing from 15.35 dB to -4.28 dB, sensing threshold from 10.57 dB to -21.47 dB, and user SINR increasing from 14.40 dB to 16.24 dB.
- Larger UPA sizes reduce AoI; a 6 by 6 UPA serves all users in the parsed snapshot, while a 3 by 3 UPA leaves only two users above threshold.
- AoI rises as users increase from 3 to 15; SAC and PPO remain competitive, while A2C and heuristic baselines degrade more.
- In a consecutive 300-slot stress test, SAC's cumulative average AoI stays around 1.62 without an increasing trend.

## Limitations / future work

The validation is simulation-only. Future work named in the parse includes 3-D UAV trajectory design, cooperative multi-UAV ISAC, mobile users, and more general target-motion models. The local parse header does not provide final DOI/venue metadata; the citation metadata was verified against the DOI record.

## Relation to the corpus

This source adds [[aoi-centric-uav-isac-beam-control]] to the [[integrated-sensing-and-communication]] and [[age-of-information]] branches. It complements [[ye-2026-deeplsc-lae-isac]], [[ye-2026-meta-deepesc-lae-isac]], and [[ye-2026-mode-lae-isac]], which optimize LAE-ISAC communication/sensing objectives without AoI as the central target. It is also adjacent to [[hazarika-2026-dynamo-uav-vehicle-tracking]], where target-prioritization freshness is combined with prediction uncertainty and link quality.

## Raw artifacts

- Parse: `raw/sources/Age_of_Information_Minimization_in_UAV-Enabled_Integrated_Sensing_and_Communication_Systems/Age_of_Information_Minimization_in_UAV-Enabled_Integrated_Sensing_and_Communication_Systems.md`
- Origin PDF: `raw/sources/Age_of_Information_Minimization_in_UAV-Enabled_Integrated_Sensing_and_Communication_Systems/Age_of_Information_Minimization_in_UAV-Enabled_Integrated_Sensing_and_Communication_Systems.pdf`
- Figures: `raw/sources/Age_of_Information_Minimization_in_UAV-Enabled_Integrated_Sensing_and_Communication_Systems/images/`
