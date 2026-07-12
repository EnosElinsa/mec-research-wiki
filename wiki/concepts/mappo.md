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
  - "[[wang-2026-scalable-multiuav-analytics]]"
  - "[[zhu-2026-hab-mappo-target-search]]"
  - "[[wu-not-in-parse-aoi-sampling-buffering-routing]]"
  - "[[ning-2025-channel-aware-irs-uav]]"
  - "[[wang-2026-wutf-fair-communication]]"
  - "[[wireless-powered-uav-fair-service-control]]"
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[decentralized-active-ris-uav-noma-control]]"
  - "[[hu-2026-segmented-irs-cpn]]"
created: 2026-05-29
updated: 2026-07-13
---

# MAPPO (Multi-Agent PPO)

The multi-agent extension of [[ppo|Proximal Policy Optimization]]: each agent runs a clipped-objective on-policy actor, typically with a **centralized critic** during training under [[centralized-training-decentralized-execution|CTDE]], so agents act on local observations at execution time. MAPPO inherits PPO's training stability (trust-region-style clipping) and is a common choice when on-policy stability is preferred over the sample efficiency of off-policy methods like [[masac]].

In [[kang-2023-mappo-hierarchical-aerial]] MAPPO solves the joint GD-association, resource-allocation, and UAV-to-HAP offloading POMDP in a hierarchical aerial computing system, with state normalization and action masking to speed training.

[[wang-2026-blockchain-lae-fl-mappo]] uses an FL-MAPPO variant for low-altitude edge intelligence, coordinating offloading decisions, caching, and resource allocation across task UAVs and service UAVs under queueing, PV-energy, and blockchain-overhead terms.

[[chen-2026-hc-mappo-vehicle-twin-migration]] uses MAPPO in the upper layer of a hierarchical controller for vehicle-twin migration and UAV routing, while deterministic lower-layer controllers enforce migration and path-planning feasibility.

[[zhao-2026-mappo-jscc-aec]] uses MAPPO-JSCC for HAP-assisted collaborative aerial edge computing, embedding numerical sensing optimization plus SCA/Dinkelbach transmission-power solvers into a CTDE-style PPO multi-agent controller.

[[wang-2026-llm-qos-multiuav-resource]] uses MAPPO as the UAV-side student policy after a cloud-side LLM teacher generates QoS-aware resource-allocation guidance.

[[wang-2026-scalable-multiuav-analytics]] uses MAPPO inside MAPDP for distributed collaborative UAV video analytics at larger swarm scales, while [[zhu-2026-hab-mappo-target-search]] uses an attention-based MAPPO actor/critic with Beta-distribution actions and heuristic offloading for cooperative target search.

[[wu-not-in-parse-aoi-sampling-buffering-routing]] uses COMH-MAPPO for all-aerial AoI control, giving separate policy heads to sampling, buffer scheduling, and FANET next-hop routing while keeping CTDE-style training.

[[ning-2025-channel-aware-irs-uav]] uses shared-actor MAPPO for joint UAV movement and [[dynamic-irs-user-association]], with SCA handling transmit power after the multi-agent communication decisions.

[[wang-2026-wutf-fair-communication]] randomizes the actor-update order and lets later updates use preceding actors' newest policies for wireless-powered fair-service trajectories. [[morshed-2026-active-ris-uav-noma-mappo]] uses a different decomposition: BS, UAV, and active-RIS actors control NOMA power, movement, and element gain/phase under one shared critic and reward.
