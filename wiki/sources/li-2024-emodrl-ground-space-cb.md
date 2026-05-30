---
type: source
title: "Collaborative Ground-Space Communications via Evolutionary Multi-Objective Deep Reinforcement Learning"
authors: ["Jiahui Li", "Geng Sun", "Qingqing Wu", "Dusit Niyato", "Jiawen Kang", "Abbas Jamalipour", "Victor C. M. Leung"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3459029"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, leo-satellite, distributed-collaborative-beamforming, multi-objective-reinforcement-learning, evolutionary-reinforcement-learning, virtual-antenna-array, non-terrestrial-network]
related:
  - "[[collaborative-beamforming]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[non-terrestrial-network]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[evolutionary-reinforcement-learning]]"
  - "[[multi-objective-mdp-vectorial-reward]]"
  - "[[seamless-handover]]"
  - "[[sun-2025-emoppo-vlh-aerial-cb]]"
  - "[[song-2022-emorl-tcto-uav]]"
created: 2026-05-31
updated: 2026-05-31
---

# Collaborative Ground-Space Communications via Evolutionary Multi-Objective Deep Reinforcement Learning

## Citation

Li, J., Sun, G., Wu, Q., Niyato, D., Kang, J., Jamalipour, A., & Leung, V. C. M. (2024). *Collaborative Ground-Space Communications via Evolutionary Multi-Objective Deep Reinforcement Learning*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3459029.

## TL;DR

Proposes a **Distributed Collaborative Beamforming (DCB)**-based **uplink** paradigm for **ground-space** (terminal-to-LEO-satellite) direct communications. Terminals that cannot establish efficient direct links to LEO satellites act as **distributed antennas**, forming a virtual antenna array that boosts terminal-to-satellite uplink achievable rate and connection duration. The authors formulate a **long-term multi-objective optimization problem** balancing uplink rate, terminal energy consumption, and satellite **switching (handover) frequency**, reformulate it as an action-space-reduced, scale-universal **MOMDP**, and solve it with an **Evolutionary Multi-Objective Deep Reinforcement Learning (EMODRL)** algorithm that masks low-value actions to speed training.

## Problem framing

LEO constellations enable direct terminal-satellite connections, but many deployed terminals are energy-sensitive with coarse, low-gain antennas, so their uplinks are low-efficiency and stable only at short range — forcing frequent satellite switches and vexing **ping-pong handovers**. Improving terminal-to-satellite uplink quality is the goal, and it requires jointly trading off rate, terminal energy, and handover frequency, which vary with terminal-cluster scale.

## System model

- **Actors.** Ground terminals (energy-sensitive, coarse antennas) cooperating as a distributed virtual antenna array → LEO satellites.
- **Paradigm.** DCB treats terminals unable to reach efficient direct links as distributed antennas to enhance uplink achievable rate and duration ([[collaborative-beamforming]]).
- **Objectives (long-term MOP).** Maximize terminal-satellite uplink achievable rate; minimize terminal energy consumption; minimize satellite switching frequency ([[seamless-handover]]).
- **Formulation.** Reformulated into an action-space-reduced and scale-universal **MOMDP** ([[multi-objective-mdp-vectorial-reward]]).

## Method

- **EMODRL.** An evolutionary multi-objective DRL algorithm that obtains **multiple** trade-off policies in one run; **low-value actions are masked** to speed up training ([[evolutionary-reinforcement-learning]] + [[multi-objective-reinforcement-learning]]).

## Key findings

- DCB lets terminals that individually cannot meet the uplink-rate threshold achieve efficient direct uplink transmission.
- The proposed algorithm outperforms various baselines and **saves 30% handover frequency** at a similar uplink achievable rate compared with the rate-greedy method (the parse's abstract states "saves 30% handover frequency").

## Limitations / future work

The parse's introduction/abstract does not enumerate explicit limitations; evaluation is simulation-based.

## Relation to the corpus

The **satellite / ground-space** sibling of the aerial collaborative-beamforming work [[sun-2025-emoppo-vlh-aerial-cb]] from the same Geng Sun / Jiahui Li group, and part of the broader evolutionary-multi-objective-RL lineage with [[song-2022-emorl-tcto-uav]]. It extends [[collaborative-beamforming]] to a **distributed** (terminal-side) virtual antenna array and ties into the wiki's NTN / LEO thread ([[leo-satellite-edge-computing]], [[non-terrestrial-network]]). Reinforces [[multi-objective-reinforcement-learning]], [[evolutionary-reinforcement-learning]], and [[seamless-handover]].

## Raw artifacts

- `raw/sources/Collaborative_Ground-Space_Communications_via_Evolutionary_Multi-Objective_Deep_Reinforcement_Learning/full.md`
- Original PDF and extracted figures in the same folder.
