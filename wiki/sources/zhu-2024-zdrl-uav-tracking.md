---
type: source
title: "Collaborative Reinforcement Learning Based Unmanned Aerial Vehicle (UAV) Trajectory Design for 3D UAV Tracking"
authors: ["Yujiao Zhu", "Mingzhe Chen", "Sihua Wang", "Ye Hu", "Yuchen Liu", "Changchuan Yin"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3382913"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, unmanned-aerial-vehicle, uav-trajectory-control, distributional-reinforcement-learning, value-decomposition-network, multi-agent-q-learning, localization]
related:
  - "[[distributional-reinforcement-learning]]"
  - "[[value-decomposition-network]]"
  - "[[uav-trajectory-control]]"
  - "[[multi-agent-q-learning]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[air-to-ground-channel-model]]"
  - "[[chang-2022-marl-multiuav-trajectory]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[zhu-2024-sensing-comm-doppler-uav-swarm]]"
created: 2026-06-02
updated: 2026-06-02
---

# Collaborative Reinforcement Learning Based Unmanned Aerial Vehicle (UAV) Trajectory Design for 3D UAV Tracking

## Citation

Zhu, Y., Chen, M., Wang, S., Hu, Y., Liu, Y., & Yin, C. (2024). *Collaborative Reinforcement Learning Based Unmanned Aerial Vehicle (UAV) Trajectory Design for 3D UAV Tracking*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3382913. (Manuscript received 10 October 2023; revised 21 January 2024; accepted 22 March 2024; date of publication 28 March 2024; date of current version 5 November 2024 → year 2024.)

## TL;DR

A **collaborative-RL trajectory + power design** for **real-time 3D localization of a target UAV** using one **active** UAV and four **passive** UAVs. The active UAV transmits signals that reflect off the (possibly adversarial) target to the passive UAVs; each passive UAV estimates the active→target→passive transmission distance and forwards it to a ground BS, which fixes the target's 3D position via a two-stage weighted least-squares (TSWLS) TDOA method. Because the target moves and localization accuracy depends on SNR, each controlled UAV must optimize its trajectory and the active UAV its transmit power. The authors propose a **Z function decomposition based reinforcement learning (ZD-RL)** method: unlike value-function-decomposition RL (VD-RL), which estimates the expectation of the sum of future rewards, ZD-RL learns the **probability distribution** of that return (a distributional-RL idea) for more accurate value estimation. Reported result: ZD-RL **reduces positioning error by up to 39.4% vs VD-RL and 64.6% vs independent deep RL**.

## Problem framing

UAV localization supports military/industrial/assistance tasks, including tracking unauthorized UAVs in real time, but is hard because targets move fast, 3D positioning needs at least four sensors and complex algorithms, and dynamic wireless conditions (interference, power, resources) affect the localization pilot signals. Prior work largely ignored how sensor placement affects accuracy, assumed constant SNR, or assumed a central controller already knows all sensor positions and CSI — unrealistic when the controller lacks that information. RL-based localization removes the need for full prior information but typically routes all sensing data to a central controller (overhead, latency) and uses statically installed sensors unsuitable for fast targets. This paper uses mobile controlled UAVs with decentralized observation-driven decisions.

## System model

- **Actors.** A ground BS plus five controlled UAVs: one active (index 0) and four passive (1–4); the target UAV does not share its position (unknown to itself or adversarial).
- **Sensing chain.** Active→target→passive LoS links (reflection, SNR set by active transmit power and geometry); passive→BS links use probabilistic LoS/NLoS path loss and OFDMA. Distance measurements carry independent Gaussian error whose variance depends on geometry and power.
- **Positioning.** TDOA with TSWLS at the BS; four passive UAVs supply the four distances needed for a 3D fix.
- **Objective.** Minimize cumulative positioning error over a horizon by jointly optimizing the active UAV's transmit power and all controlled UAVs' trajectories, subject to delay and movement constraints; an analysis shows minimum positioning error is achieved when each controlled UAV's distance to the target is minimized.

## Method

- **ZD-RL (Z function decomposition based RL).** A collaborative-RL method where each controlled UAV decides its trajectory (and the active UAV its power) from individual local observations. It decomposes a global **Z function** (the return distribution) across agents, learning the **distribution of the sum of future rewards** rather than just its expected value as in [[value-decomposition-network|value-function decomposition]]; this is argued to improve estimation accuracy, efficiency, and training stability.
- **Decentralized execution.** Each UAV updates its own DNN parameters from local observations, avoiding the overhead of routing all sensing data to a central controller.

## Key findings

- ZD-RL reduces target positioning error by **up to 39.4% versus VD-RL** and **up to 64.6% versus independent deep RL** (the paper's headline simulation results, stated verbatim in the abstract).
- Analytical result: the minimum positioning error is attained when the distance between each controlled UAV and the target UAV is minimized, guiding the learned trajectories.
- The authors state this is the first framework to use one active + four passive UAVs for 3D UAV positioning.

## Limitations / future work

A localization / trajectory-design study, not an MEC offloading paper (no computation offloading). Results are simulation-based; the geometry is fixed at five controlled UAVs (one active + four passive) tracking a single target, and LoS is assumed for the active–target–passive reflection links.

## Relation to the corpus

A **distributional-RL** entry that anchors the new [[distributional-reinforcement-learning]] concept and contrasts with the corpus's expectation-based value-decomposition multi-agent methods ([[value-decomposition-network]], [[multi-agent-q-learning]]). Its multi-UAV trajectory-design framing connects to [[chang-2022-marl-multiuav-trajectory]] and [[he-2023-fairness-3d-multiuav-maddpg]]; its sensing/localization-via-reflection angle is adjacent to the sensing-communication co-design of [[zhu-2024-sensing-comm-doppler-uav-swarm]] (different author group despite the shared "Zhu" surname).

## Raw artifacts

- `raw/sources/Collaborative_Reinforcement_Learning_Based_Unmanned_Aerial_Vehicle_UAV_Trajectory_Design_for_3D_UAV_Tracking/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
