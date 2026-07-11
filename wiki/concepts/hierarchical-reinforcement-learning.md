---
type: concept
title: "Hierarchical Reinforcement Learning (HRL)"
tags: [drl, hierarchy, skills, temporal-abstraction]
related:
  - "[[soft-actor-critic]]"
  - "[[federated-reinforcement-learning]]"
  - "[[wang-2024-hfrl-decentralized-navigation]]"
  - "[[tong-2026-uneven-terrain-uav-mec]]"
  - "[[bayessa-not-in-parse-uav-isac-secure-content-hdrl]]"
  - "[[action-masked-hierarchical-drl]]"
created: 2026-05-31
updated: 2026-07-11
---

# Hierarchical Reinforcement Learning (HRL)

A reinforcement-learning paradigm that decomposes control into multiple temporal levels: a higher-level policy selects abstract **skills** (a.k.a. options / sub-policies) while lower-level policies execute the primitive actions that realize each skill. Temporal abstraction shortens the effective decision horizon, improves exploration on long-horizon tasks, and lets learned skills transfer across agents or tasks.

In the wiki, [[wang-2024-hfrl-decentralized-navigation]] proposes the **soft hierarchical deep reinforcement learning network (SHDRLN)**, a maximum-entropy ([[soft-actor-critic|SAC]]-style) hierarchical net that abstracts atomic UAV actions into generic skills. The skill abstraction reduces policy divergence across **heterogeneous** UAVs, which is what makes the paper's dual-end [[federated-reinforcement-learning|federated RL]] knowledge-sharing (DFRL) effective when UAVs have different performance parameters.

[[tong-2026-uneven-terrain-uav-mec]] uses a different hierarchy: PH-DRL separates first-level 3D UAV flight control from second-level task-allocation ratio decisions, with the offloading level invoked according to the currently covered UE set. That hierarchy is architectural and decision-factorized rather than an options/skills abstraction.

[[bayessa-not-in-parse-uav-isac-secure-content-hdrl]] adds a multi-timescale wireless-control hierarchy: long-timescale caching and short-timescale association/deployment/beamforming are solved by DDQN variants, with [[action-masked-hierarchical-drl]] used to remove infeasible short-timescale choices.
