---
type: concept
title: "Hierarchical Reinforcement Learning (HRL)"
tags: [drl, hierarchy, skills, temporal-abstraction]
related:
  - "[[soft-actor-critic]]"
  - "[[federated-reinforcement-learning]]"
  - "[[wang-2024-hfrl-decentralized-navigation]]"
created: 2026-05-31
updated: 2026-05-31
---

# Hierarchical Reinforcement Learning (HRL)

A reinforcement-learning paradigm that decomposes control into multiple temporal levels: a higher-level policy selects abstract **skills** (a.k.a. options / sub-policies) while lower-level policies execute the primitive actions that realize each skill. Temporal abstraction shortens the effective decision horizon, improves exploration on long-horizon tasks, and lets learned skills transfer across agents or tasks.

In the wiki, [[wang-2024-hfrl-decentralized-navigation]] proposes the **soft hierarchical deep reinforcement learning network (SHDRLN)**, a maximum-entropy ([[soft-actor-critic|SAC]]-style) hierarchical net that abstracts atomic UAV actions into generic skills. The skill abstraction reduces policy divergence across **heterogeneous** UAVs, which is what makes the paper's dual-end [[federated-reinforcement-learning|federated RL]] knowledge-sharing (DFRL) effective when UAVs have different performance parameters.
