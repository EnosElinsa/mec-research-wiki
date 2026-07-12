---
type: concept
title: "Embodied Anti-Jamming Resource Allocation"
tags: [embodied-intelligence, anti-jamming, uav, spectrum-allocation, power-control, reinforcement-learning]
related:
  - "[[yang-2026-embodied-antijamming-uav]]"
  - "[[anti-jamming-mec]]"
  - "[[multi-domain-uav-anti-jamming]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[ddqn]]"
  - "[[prioritized-experience-replay]]"
  - "[[chen-2026-maddpg-uav-swarm-antijamming]]"
created: 2026-07-13
updated: 2026-07-13
---

# Embodied Anti-Jamming Resource Allocation

Embodied anti-jamming resource allocation treats a physical radio platform as a perception-decision-action loop. A UAV observes channel and jammer conditions, selects spectrum and power controls, and applies those actions through its communication hardware while the environment and adversary continue to change.

[[yang-2026-embodied-antijamming-uav]] instantiates the pattern with one DDQN agent per U2U link. Agents choose a reused U2I sub-band and discrete power from local state, share a cooperative delay/energy/deadline reward, prioritize replay by TD error, and transfer experiences from a source MDP.

The embodiment claim should follow the implemented sensing surface. In the cited source, perception is channel/jammer state; vision, radar, and lidar are possible extensions rather than evaluated inputs. The concept overlaps [[multi-domain-uav-anti-jamming]] but emphasizes the physical perception-action loop and transferred value learning rather than an actor-critic controller.
