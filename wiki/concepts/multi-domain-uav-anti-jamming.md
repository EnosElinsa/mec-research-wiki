---
type: concept
title: "Multi-Domain UAV Anti-Jamming"
tags: [uav, anti-jamming, spectrum, power-control, multi-agent-drl]
related:
  - "[[chen-2026-maddpg-uav-swarm-antijamming]]"
  - "[[anti-jamming-mec]]"
  - "[[uav-enabled-its]]"
  - "[[maddpg]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[gauss-markov-mobility-model]]"
created: 2026-07-10
updated: 2026-07-10
---

# Multi-Domain UAV Anti-Jamming

A UAV-swarm radio-control pattern where the anti-jamming response spans multiple control domains at once: channel choice, frequency hopping, transmit power, and swarm communication success. In [[chen-2026-maddpg-uav-swarm-antijamming]], the goal is not only to avoid jammed spectrum, but to preserve U2U payload delivery and U2G reporting capacity while reducing energy and hopping overhead.

The key modeling step is to cast jammed UAV-swarm communication as a partially observable multi-agent decision problem. Each UAV sees local channel and interference information, while the reward depends on joint U2U/U2G behavior. That makes [[maddpg]] and other [[centralized-training-decentralized-execution]] actor-critic methods a natural fit: critics use a global training view, while actors run from local observations.

This concept is adjacent to [[anti-jamming-mec]]. The MEC variant protects offloading and computation service quality; the UAV-swarm ITS variant protects communication reliability and traffic-monitoring data flow. Both share [[spectrum-sensing-channel-selection]], but their optimization surfaces differ.
