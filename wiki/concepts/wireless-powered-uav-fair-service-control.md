---
type: concept
title: "Wireless-Powered UAV Fair-Service Control"
tags: [uav, wireless-power-transfer, fairness, multi-agent-drl, trajectory-control]
related:
  - "[[wang-2026-wutf-fair-communication]]"
  - "[[wireless-power-transfer]]"
  - "[[jains-fairness-index]]"
  - "[[ma-pomdp]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[sequential-multi-agent-policy-generation]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-12
updated: 2026-07-12
---

# Wireless-Powered UAV Fair-Service Control

Wireless-powered UAV fair-service control couples aerial coverage with replenishment-aware mobility. A UAV moves toward underserved users while charging only when it hovers within tower coverage, so throughput, spatial service balance, propulsion cost, and charging opportunity become one sequential decision problem.

[[wang-2026-wutf-fair-communication]] implements the pattern as a [[ma-pomdp|multi-agent POMDP]]. Continuous speed/yaw actors use local observations, a centralized critic uses the global state during training, and WUTF updates the actors sequentially with a clipped PPO-style multi-agent objective derived from the MAPPO family. The reward combines [[jains-fairness-index|Jain fairness]], an underserved-user communication value, detailed rotary-wing energy, and collision/depletion penalties.

This pattern differs from device-side harvest-then-offload WPT: charging towers replenish the UAV infrastructure itself. It also exposes a deployment tension in [[centralized-training-decentralized-execution|CTDE]]: decentralized actors remain usable without a shared critic, but omitting neighboring-UAV state or messages can weaken coordination when coverage regions overlap.
