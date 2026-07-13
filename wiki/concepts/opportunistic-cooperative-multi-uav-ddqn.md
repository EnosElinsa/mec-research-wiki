---
type: concept
title: "Opportunistic Cooperative Multi-UAV DDQN"
tags: [ddqn, multi-agent-reinforcement-learning, uav-swarm, intermittent-connectivity, data-collection]
related:
  - "[[qi-2026-ocma-ddqn-data-collection]]"
  - "[[ddqn]]"
  - "[[potential-game]]"
  - "[[experience-value-circles]]"
  - "[[lstm-interruption-compensation]]"
created: 2026-07-14
updated: 2026-07-14
---

# Opportunistic Cooperative Multi-UAV DDQN

Opportunistic cooperative multi-UAV DDQN lets independently acting UAVs exchange explored-map state and replay experience only when intermittent links and distance-conditioned value rules make sharing useful. A pairwise cooperation cost is embedded in an exact-potential-game model, while each agent executes a discrete [[ddqn]] policy.

The OCMA-DDQN-LSTM implementation in [[qi-2026-ocma-ddqn-data-collection]] augments missing neighbor state with short-horizon prediction. Its evidence is simulation on grid motion with at most four UAVs; task load is increased with swarm size, and coordination overhead under larger decentralized swarms remains unresolved.
