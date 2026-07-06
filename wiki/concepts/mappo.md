---
type: concept
title: "MAPPO (Multi-Agent PPO)"
tags: [drl, multi-agent, on-policy]
related:
  - "[[kang-2023-mappo-hierarchical-aerial]]"
  - "[[ppo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[masac]]"
  - "[[ctde-actor-critic-backbones-in-mec]]"
  - "[[wang-2026-blockchain-lae-fl-mappo]]"
  - "[[chen-2026-hc-mappo-vehicle-twin-migration]]"
  - "[[zhao-2026-mappo-jscc-aec]]"
  - "[[wang-2026-llm-qos-multiuav-resource]]"
created: 2026-05-29
updated: 2026-07-07
---

# MAPPO (Multi-Agent PPO)

The multi-agent extension of [[ppo|Proximal Policy Optimization]]: each agent runs a clipped-objective on-policy actor, typically with a **centralized critic** during training under [[centralized-training-decentralized-execution|CTDE]], so agents act on local observations at execution time. MAPPO inherits PPO's training stability (trust-region-style clipping) and is a common choice when on-policy stability is preferred over the sample efficiency of off-policy methods like [[masac]].

In [[kang-2023-mappo-hierarchical-aerial]] MAPPO solves the joint GD-association, resource-allocation, and UAV-to-HAP offloading POMDP in a hierarchical aerial computing system, with state normalization and action masking to speed training.

[[wang-2026-blockchain-lae-fl-mappo]] uses an FL-MAPPO variant for low-altitude edge intelligence, coordinating offloading decisions, caching, and resource allocation across task UAVs and service UAVs under queueing, PV-energy, and blockchain-overhead terms.

[[chen-2026-hc-mappo-vehicle-twin-migration]] uses MAPPO in the upper layer of a hierarchical controller for vehicle-twin migration and UAV routing, while deterministic lower-layer controllers enforce migration and path-planning feasibility.

[[zhao-2026-mappo-jscc-aec]] uses MAPPO-JSCC for HAP-assisted collaborative aerial edge computing, embedding numerical sensing optimization plus SCA/Dinkelbach transmission-power solvers into a CTDE-style PPO multi-agent controller.

[[wang-2026-llm-qos-multiuav-resource]] uses MAPPO as the UAV-side student policy after a cloud-side LLM teacher generates QoS-aware resource-allocation guidance.
