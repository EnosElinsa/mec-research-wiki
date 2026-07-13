---
type: source
title: "Joint Trajectory and Power Design With Cooperative Jamming UAV Assistance Based on Reinforcement Learning"
authors: ["Yingkun Wen", "Fengshuan Wang", "Hui-Ming Wang", "Junhuai Li", "Jin Qian", "Kan Wang", "Huaijun Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3590170"
venue: "IEEE Transactions on Wireless Communications (TWC)"
tags: [source, physical-layer-security, cooperative-jamming, uav-mobile-relaying, maddpg, secrecy-outage-probability]
related:
  - "[[physical-layer-security]]"
  - "[[cooperative-jamming]]"
  - "[[friendly-jamming-uav]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-trajectory-control]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[secrecy-outage-probability]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
  - "[[guo-2024-multiuav-proactive-eavesdropping]]"
created: 2026-07-13
updated: 2026-07-13
---

# Joint Trajectory and Power Design With Cooperative Jamming UAV Assistance Based on Reinforcement Learning

## Citation

Wen, Y., Wang, F., Wang, H.-M., Li, J., Qian, J., Wang, K., & Wang, H. (2026). Joint trajectory and power design with cooperative jamming UAV assistance based on reinforcement learning. *IEEE Transactions on Wireless Communications, 25*, 1258-1271. https://doi.org/10.1109/TWC.2025.3590170

The local parse omits final publication metadata; the title-matched IEEE/Crossref record supplies the year, venue, DOI, volume, and pages.

## TL;DR

A relay UAV forwards confidential traffic while another legitimate UAV acts as a cooperative jammer against a mobile aerial eavesdropper. MAJDTP uses MADDPG to coordinate relay/jammer trajectories and powers under perfect or imperfect eavesdropper CSI.

## Problem and system model

A source reaches one ground user through a relay UAV; a malicious UAV approaches to intercept it. A control center monitors positions and assigns a second legitimate UAV to jam. The evaluated setup uses one user, one relay, one jammer, equal fixed altitudes, half-duplex roles, single-antenna LoS/free-space links, prescribed endpoints, speed and separation limits.

With perfect CSI, performance is worst-case secrecy rate. With imperfect wiretap CSI, Rayleigh statistics yield [[secrecy-outage-probability]]. Energy includes fixed-wing propulsion and jammer transmit energy while omitting communication-processing energy.

## Method

MAJDTP models relay and jammer control as a Markov game. Continuous actions contain motion and transmit power. [[maddpg]] provides one actor/critic pair per controllable UAV, joint critic information during training, replay, target networks, and soft updates under [[centralized-training-decentralized-execution]].

The parse inconsistently calls the eavesdropper an agent, while trainable state/action definitions are clearest for the relay and jammer. Displayed rewards also use communication-rate notation rather than consistently matching the secrecy objective.

## Key findings

- The learned relay initially moves away from the user as the eavesdropper approaches, then returns toward the user and its prescribed endpoint.
- The jammer approaches the user/eavesdropper region, then retreats to limit interference to the legitimate receiver.
- Simulated secrecy improves and secrecy-outage probability falls with relay power and training iterations.
- Reported travel distance and modeled energy fall with training; the jammer consumes more because its energy includes jamming power.
- MAJDTP reports better secrecy, faster convergence, and lower energy than its DDPG benchmark, without prose-level numerical gains.

## Limitations

Evidence is simulation-only with one user/relay/jammer, instantaneous monitoring, fixed altitude, single antennas, and a fixed-wing energy model. DDPG is the only named learning baseline. The perfect-CSI formulation contains an apparent role inconsistency, equations 42 and 44 are absent from the parse, and the imperfect-CSI section lacks a clearly extracted standalone optimization problem. No global-optimality or policy-convergence guarantee is provided.

## Relation to the corpus

This source combines [[physical-layer-security]], [[cooperative-jamming]], [[uav-mobile-relaying]], and [[maddpg]] without MEC computation. [[wang-2026-secure-lae-uav-scheduling]] studies a broader secrecy-energy-efficiency controller, while [[guo-2024-multiuav-proactive-eavesdropping]] treats aerial interception from the eavesdropping side.

## Raw artifacts

- Parse: `raw/sources/Joint_Trajectory_and_Power_Design_With_Cooperative_Jamming_UAV_Assistance_Based_on_Reinforcement_Learning/Joint_Trajectory_and_Power_Design_With_Cooperative_Jamming_UAV_Assistance_Based_on_Reinforcement_Learning.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
