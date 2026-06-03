---
type: concept
title: "Communication-Constrained Multi-Agent Reinforcement Learning"
tags: [reinforcement-learning, multi-agent, communication, mec, scheduling]
related:
  - "[[centralized-training-decentralized-execution]]"
  - "[[maddpg]]"
  - "[[soft-actor-critic]]"
  - "[[task-offloading]]"
  - "[[li-2024-smdrl-resource-constrained-mec]]"
created: 2026-06-03
updated: 2026-06-03
---

# Communication-Constrained Multi-Agent Reinforcement Learning

A family of multi-agent reinforcement learning (MARL) designs that treat the **inter-agent communication channel as a scarce, contested resource** rather than as free, instantaneous coordination. Standard cooperative MARL (e.g. [[maddpg]]) assumes agents can exchange observations or messages at no cost; that assumption breaks when agents are devices sharing a bandwidth-limited wireless medium, where messaging competes with the data traffic the agents are trying to schedule.

Recurring ingredients:

- **Learned message encoding.** Instead of broadcasting raw observations, each agent learns *what* to transmit — the actor network is extended to encode a compact message, so the limited channel carries only the most decision-relevant information.
- **Communication scheduling / medium arbitration.** Because simultaneous transmissions collide, a scheduling mechanism decides *which* agents may speak each round. A TopK rule (only the K most-significant agents broadcast) is one such arbitration that keeps coordination tractable under tight bandwidth.
- **[[centralized-training-decentralized-execution|Centralized training, decentralized execution]].** Training can use global information offline, but at run time each agent acts (and communicates) using only locally available messages.

In the wiki, [[li-2024-smdrl-resource-constrained-mec]] is the anchor: its Scheduled Multi-agent DRL (SMDRL) learns message encoding, action selection, and self-scheduling under a TopK broadcast limit so that [[task-offloading|computation offloading]] still reaches near-optimal QoE when the shared medium is bandwidth-constrained — distinct from MARL offloading work that assumes cost-free coordination.
