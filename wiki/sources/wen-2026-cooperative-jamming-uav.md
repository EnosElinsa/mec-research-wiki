---
type: source
modeling_card: required
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
updated: 2026-11-03
---

# Joint Trajectory and Power Design With Cooperative Jamming UAV Assistance Based on Reinforcement Learning

## Citation

Wen, Y., Wang, F., Wang, H.-M., Li, J., Qian, J., Wang, K., & Wang, H. (2026). Joint trajectory and power design with cooperative jamming UAV assistance based on reinforcement learning. *IEEE Transactions on Wireless Communications, 25*, 1258-1271. https://doi.org/10.1109/TWC.2025.3590170

The local parse omits final publication metadata; the title-matched IEEE/Crossref record supplies the year, venue, DOI, volume, and pages.

## TL;DR

A relay UAV forwards confidential traffic while another legitimate UAV acts as a cooperative jammer against a mobile aerial eavesdropper. MAJDTP uses MADDPG to coordinate relay/jammer trajectories and powers under perfect or imperfect eavesdropper CSI.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A source sends confidential traffic through a relay UAV to a ground user while a second UAV jams a mobile eavesdropper; relay and jammer positions and powers change over time, with perfect or imperfect wiretap CSI.

**Problem & objective**: The perfect-CSI problem P1 (31), subject to (C1)-(C14), maximizes the worst-case secrecy rate, $\max_{\mathbf q_{m_r},\mathbf q_{m_j},p_{m_r},p_{m_j}}R_{m_r,n}^{sec}$, while the imperfect-CSI variant minimizes secrecy-outage risk.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Relay UAV trajectory | $\mathbf q_{m_r}(t)$ | continuous, kinetic bounds | Position of the forwarding UAV |
| Jammer UAV trajectory | $\mathbf q_{m_j}(t)$ | continuous, kinetic bounds | Position of the cooperative jammer |
| Relay transmit power | $p_{m_r}(t)$ | continuous, average and peak bounded | Confidential signal power |
| Jammer transmit power | $p_{m_j}(t)$ | continuous, average and peak bounded | Cooperative jamming power |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (C1)-(C5), (C10) | UAV role-allocation rules distinguishing the relay and jamming UAVs |
| (C6)-(C9) | Kinetic constraints on the UAV trajectories |
| (C11)-(C14) | Average and peak transmit-power limits for the source and the UAVs, e.g. $\frac1T\sum_tp_{m_a}[t]\le P_{UAV}^{ave}$ and $0\le p_{m_a}[t]\le P_{UAV}^{\max}$ |
| Imperfect CSI (38) | Security is evaluated by the secrecy outage probability $P_{out}=1-F_Z(\theta_1)$ instead of the secrecy rate |

**Algorithm**: Cast relay, jammer, and eavesdropper interactions as a Markov game, use centralized-training decentralized-execution MADDPG with actor and critic target networks and replay, and switch the reward between secrecy rate and outage minimization according to CSI availability.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wen et al. [x] study physical-layer security when a relay UAV and a cooperative-jamming UAV protect a ground user from an aerial eavesdropper. The design maximizes worst-case secrecy rate with perfect CSI and minimizes secrecy-outage risk with uncertain wiretap channels by controlling both UAV trajectories and powers under kinetic and average or peak power constraints. A multiagent Markov game and MADDPG coordinate the relay and jammer through centralized training and decentralized execution. The reported simulations compare the learned policies under perfect and imperfect CSI and report higher secrecy rate for the MAJDTP algorithm than a reference DDPG algorithm.

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
