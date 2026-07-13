---
type: source
title: "Interference Management for Cellular-Connected UAVs: A Deep Reinforcement Learning Approach"
authors: ["Ursula Challita", "Walid Saad", "Christian Bettstetter"]
year: 2019
url: "https://doi.org/10.1109/TWC.2019.2900035"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, cellular-connected-uav, interference-management, path-planning, deep-reinforcement-learning, echo-state-network, game-theory, power-control]
related:
  - "[[deep-echo-state-network-reinforcement-learning]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[nash-equilibrium]]"
  - "[[walid-saad]]"
created: 2026-07-13
updated: 2026-07-13
---

# Interference Management for Cellular-Connected UAVs: A Deep Reinforcement Learning Approach

## Citation

Challita, U., Saad, W., & Bettstetter, C. (2019). *Interference Management for Cellular-Connected UAVs: A Deep Reinforcement Learning Approach*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2019.2900035.

> **Metadata grounding note.** DOI, venue, and year are absent from the parse and were verified through the exact-title Crossref record.

## TL;DR

Models multiple cellular-connected UAVs as players in a dynamic noncooperative game and trains a distributed deep echo-state-network controller. Each UAV jointly chooses its next grid location, serving cell, and transmit-power level to trade UAV energy efficiency and wireless latency against interference to terrestrial users.

## Problem framing

UAV uplinks are visible to many base stations and can strongly interfere with ground-user reception. Shortest paths ignore that externality; centralized trajectory/power/association control does not scale or match distributed UAV operation. The paper therefore embeds movement and radio decisions in each UAV's local utility and uses reservoir memory to react to the evolving joint actions.

## System model

- Multiple UAVs upload mission data through a terrestrial cellular network while ground users reuse resource blocks.
- Each UAV follows a discretized path between fixed endpoints at a fixed altitude for a given run and selects one of five power levels plus cell association.
- UAV-BS links use free-space loss with Rician fading; terrestrial links use a conventional path-loss model with Rayleigh fading. Wireless latency is modeled with an M/D/1 queue.
- Utility weights combine UAV energy efficiency, UAV latency, and terrestrial-user rate/interference.

## Method

The distributed controller is a stacked/deep echo state network: fixed recurrent reservoirs retain action history, while trainable output weights estimate action utilities. UAVs broadcast selected actions during training, update location/cell/power in parallel, and act greedily during testing. Analytical altitude bounds derived from latency, SINR, and interference constraints can prune the path space. Proposition 1 states only that **if** training converges, the resulting strategy profile is a subgame-perfect Nash equilibrium; the paper explicitly leaves convergence itself to simulation and hyperparameter choice.

## Key findings

- In one path example, both methods take 32 steps, but the learned path reports **6.5 ms** UAV latency versus **12.2 ms** for shortest path and **0.95 versus 0.76 Mbit/s** terrestrial-user rate.
- With five UAVs, the paper reports **37%** higher ground-user rate, **62%** lower UAV latency, and **14%** higher UAV energy efficiency than shortest-path planning.
- The reported altitude sweep exposes the expected conflict: higher altitude can improve terrestrial rate by reducing UAV transmit power/interference but worsens the UAV link and latency.
- Expanding local state from one to five neighboring base stations improves terrestrial rate by 28% for the interference-oriented objective, at increased model and convergence cost.

## Limitations / interpretation

Evidence is simulation-only. Paths are grid-discretized, altitude is fixed during each learned run, fading/queueing are simplified, Doppler is assumed compensated, and collision avoidance and propulsion energy are outside the formulation. Action broadcasting overhead is argued negligible from grid traversal time rather than measured. The equilibrium result is conditional on convergence; the paper observes convergence only for selected hyperparameters and notes that a learning rate of 0.1 fails in its test.

## Relation to the corpus

This paper is an early [[cellular-connected-uav]] interference-management instance and a concrete use of [[deep-echo-state-network-reinforcement-learning]]. It predates the corpus's DQN/actor-critic-heavy navigation designs and uses reservoir memory plus game structure to coordinate distributed trajectory, association, and power decisions.

## Raw artifacts

- `raw/sources/Interference_Management_for_Cellular-Connected_UAVs_A_Deep_Reinforcement_Learning_Approach/Interference_Management_for_Cellular-Connected_UAVs_A_Deep_Reinforcement_Learning_Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
