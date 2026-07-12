---
type: concept
title: "Ape-X Actor-Learner Replay"
tags: [deep-reinforcement-learning, distributed-training, actor-learner, prioritized-experience-replay]
related:
  - "[[liu-2021-edivert-mobile-crowdsensing]]"
  - "[[prioritized-experience-replay]]"
  - "[[centralized-training-decentralized-execution]]"
created: 2026-07-13
updated: 2026-07-13
---

# Ape-X Actor-Learner Replay

Ape-X actor-learner replay is a distributed DRL training architecture in which multiple environment actors collect experience asynchronously while a centralized learner samples shared replay and updates model parameters. It separates simulation throughput from gradient computation and periodically synchronizes learner parameters back to the actors.

[[liu-2021-edivert-mobile-crowdsensing]] uses five selected Ape-X actors, local per-vehicle buffers, global prioritized buffers, and one GPU learner for e-Divert. This is broader than [[prioritized-experience-replay]] alone: PER defines which transitions are sampled from a buffer, while Ape-X defines how actors, buffers, and a learner exchange experience and parameters.

The architecture can improve exploration and training throughput, but it is not decentralized learning. In the e-Divert study, excessive priority can over-replay a transition and overfit it, while too many actors can replace old transitions before they are learned sufficiently. Execution may still be distributed through local policies after centralized learning.
