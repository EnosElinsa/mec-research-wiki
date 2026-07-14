---
type: source
title: "Online Altitude Control and Scheduling Policy for Minimizing AoI in UAV-Assisted IoT Wireless Networks"
authors: ["Moataz Samir", "Chadi Assi", "Sanaa Sharafeddine", "Ali Ghrayeb"]
year: 2022
url: "https://doi.org/10.1109/TMC.2020.3042925"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 21, no. 7, pp. 2493-2505"
tags: [source, age-of-information, altitude-control, uav-relay, iot, scheduling, ppo]
related:
  - "[[aoi-aware-uav-altitude-scheduling]]"
  - "[[age-of-information]]"
  - "[[ppo]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-data-collection]]"
  - "[[hybrid-action-decision-making]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[samir-2021-uav-cell-free-coverage]]"
  - "[[moataz-samir]]"
  - "[[sanaa-sharafeddine]]"
  - "[[chadi-assi]]"
  - "[[ali-ghrayeb]]"
created: 2026-07-13
updated: 2026-07-14
---

# Online Altitude Control and Scheduling Policy for Minimizing AoI in UAV-Assisted IoT Wireless Networks

## Citation

Samir, M., Assi, C., Sharafeddine, S., & Ghrayeb, A. (2022). *Online Altitude Control and Scheduling Policy for Minimizing AoI in UAV-Assisted IoT Wireless Networks*. **IEEE Transactions on Mobile Computing, 21**(7), 2493-2505. DOI: 10.1109/TMC.2020.3042925.

## TL;DR

Uses online PPO to alternate between scheduling one IoT-to-UAV or UAV-to-BS status transmission and moving a relay UAV vertically, minimizing expected weighted Age of Information over unreliable probabilistic-LoS links.

## Problem and system model

IoT devices send status updates through a half-duplex UAV relay to a base station. Each virtual relay queue retains only the newest packet. Altitude changes both hops' elevation angles, LoS probabilities, path losses, and decoding success; scheduling determines which source is received or forwarded.

The general formulation supports multiple clusters, but simulations use one UAV with fixed horizontal coordinates. Destination AoI rises every slot unless a queued update is delivered, then falls to that packet's relay-queue age plus one.

## Method

The original stochastic MINLP combines binary scheduling with continuous altitude. [[aoi-aware-uav-altitude-scheduling]] discretizes vertical movement into `+10 m`, `-10 m`, or hover and concatenates movement and transmission choices into one discrete action set. A slot performs either movement or transmission, not both.

The PPO state contains stream AoI, relay-queue occupancy and age, and both-hop rates. The controller needs no prior channel-transition model but observes instantaneous rate/CSI online. Constraint violations are penalized and invalid altitude moves are cancelled.

## Key findings

- Across four simulated environment classes, achievable rate first increases and then decreases with altitude because LoS probability and propagation distance compete.
- For 50 devices, the paper's concurrent construction has 300 action combinations; the restricted one-action-per-slot representation learns better in the displayed experiment.
- For selected streams in a 20-device urban case, PPO maintains lower AoI than random deployment/random scheduling and heuristic deployment/greedy scheduling.
- Expected weighted sum AoI increases with device count; PPO is lowest among the three plotted methods.
- The paper provides a learning curve but no analytical convergence result or prose-level exact improvement margin.

## Limitations

Evidence is simulation-only. Horizontal UAV position is fixed, evaluation uses one cluster/UAV with equal stream weights, and no global-optimality or PPO-convergence guarantee is given. The action reduction forbids simultaneous motion and transmission, so part of its learning advantage comes from a more restrictive model. Several equations/tables are OCR-damaged, including an ambiguous `3M samples` statement.

## Relation to the corpus

This source complements [[samir-2021-uav-cell-free-coverage]] by controlling altitude and two-hop freshness rather than horizontal multi-UAV highway coverage. It connects [[age-of-information]] to [[uav-mobile-relaying]] through latest-packet queues and unreliable links.

## Raw artifacts

- Parse: `raw/sources/Online_Altitude_Control_and_Scheduling_Policy_for_Minimizing_AoI_in_UAV-Assisted_IoT_Wireless_Networks/Online_Altitude_Control_and_Scheduling_Policy_for_Minimizing_AoI_in_UAV-Assisted_IoT_Wireless_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
