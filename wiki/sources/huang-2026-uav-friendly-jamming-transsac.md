---
type: source
title: "Low-Altitude UAV Friendly-Jamming for Satellite-Maritime Communications via Generative AI-Enabled Deep Reinforcement Learning"
authors: ["Jiawei Huang", "Aimin Wang", "Geng Sun", "Jiahui Li", "Jiacheng Wang", "Dusit Niyato", "Victor C. M. Leung"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3631861"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, friendly-jamming, satellite-maritime, physical-layer-security, soft-actor-critic, transformer, multi-objective]
related:
  - "[[friendly-jamming-uav]]"
  - "[[physical-layer-security]]"
  - "[[soft-actor-critic]]"
  - "[[transformer-encoder]]"
  - "[[multi-armed-bandit-objective-weighting]]"
  - "[[maritime-mec]]"
  - "[[non-terrestrial-network]]"
  - "[[uav-trajectory-control]]"
  - "[[huang-2025-dual-aav-maritime-secure-cb]]"
  - "[[wen-2026-cooperative-jamming-uav]]"
  - "[[jiawei-huang]]"
  - "[[aimin-wang]]"
  - "[[geng-sun]]"
  - "[[jiahui-li]]"
  - "[[jiacheng-wang]]"
  - "[[dusit-niyato]]"
  - "[[victor-c-m-leung]]"
created: 2026-07-13
updated: 2026-07-13
---

# Low-Altitude UAV Friendly-Jamming for Satellite-Maritime Communications via Generative AI-Enabled Deep Reinforcement Learning

## Citation

Huang, J., Wang, A., Sun, G., Li, J., Wang, J., Niyato, D., & Leung, V. C. M. (2026). Low-altitude UAV friendly-jamming for satellite-maritime communications via generative AI-enabled deep reinforcement learning. *IEEE Transactions on Mobile Computing, 25*(4), 5509-5525. https://doi.org/10.1109/TMC.2025.3631861

## TL;DR

A rotary-wing UAV jointly chooses 3-D motion and jamming power to protect a satellite-to-vessel link from an eavesdropping vessel. TransSAC augments SAC with transformer sequence features and a multi-armed bandit that adapts secrecy-versus-energy scalarization weights.

## Problem and system model

One LEO satellite serves a legitimate vessel while one low-altitude UAV jams one eavesdropping vessel. Satellite and vessel trajectories are exogenous; the UAV controls position and power under flight-region, power, energy-budget, and interference-temperature constraints. Satellite-to-vessel and UAV-to-vessel links use Rician maritime channels. The two objectives maximize average secrecy rate and minimize average UAV propulsion energy.

The parse first calls the legitimate vessel Alice and later says Bob once; equations and subsequent prose consistently use Alice. Communication and acceleration/deceleration energy are omitted from the propulsion-centric model.

## Method

The MDP state contains legitimate/eavesdropping vessel motion, satellite position, and UAV position/power. The action contains UAV 3-D movement and transmit power. A [[soft-actor-critic|SAC]] backbone uses replay, entropy-regularized stochastic control, target networks, and soft updates. A [[transformer-encoder]] processes replayed state/action sequences, while [[multi-armed-bandit-objective-weighting]] uses epsilon-greedy arm selection to update the two objective weights.

## Key findings

- The prose reports higher secrecy with UAV friendly jamming than without it and ranks TransSAC above DDPG, PPO, SAC, and TD3 in the plotted secrecy/energy comparisons; exact curve values are not present in the parse.
- The tested setting identifies maximum jamming power `20` and interference threshold `-74 dBm` as suitable; below `-86 dBm`, some policies' secrecy rates approach zero.
- TransSAC converges at roughly 1,000 iterations in the reported curve, slower than the compared methods but to a higher reward.
- The main training uses one million iterations, replay batches of 128, eight attention heads, and evaluation every 80 iterations.

## Limitations

Main evidence is simulation-only. The idealized “optimal” secrecy comparison assumes no UAV interference at the legitimate vessel and maximum jamming at the eavesdropper; it is not a global optimum of the original problem. The method uses transformer attention but no generative model that samples solutions. Imperfect eavesdropper position, multiple UAVs, and fuller constraint treatment are deferred; a Raspberry Pi timing summary points to an unavailable appendix rather than an end-to-end maritime experiment. The energy-budget notation is ambiguous and comparative curves lack machine-readable values.

## Relation to the corpus

This source extends the maritime friendly-jamming thread from the evolutionary dual-cluster design in [[huang-2025-dual-aav-maritime-secure-cb]] to sequential [[soft-actor-critic]] control. [[wen-2026-cooperative-jamming-uav]] provides a non-satellite relay/jammer comparison, while [[wu-2024-satellite-maritime-spectrum-sharing]] supplies a satellite-maritime interference-control relation.

## Raw artifacts

- Parse: `raw/sources/Low-Altitude_UAV_Friendly-Jamming_for_Satellite-Maritime_Communications_via_Generative_AI-Enabled_Deep_Reinforcement_Learning/Low-Altitude_UAV_Friendly-Jamming_for_Satellite-Maritime_Communications_via_Generative_AI-Enabled_Deep_Reinforcement_Learning.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
