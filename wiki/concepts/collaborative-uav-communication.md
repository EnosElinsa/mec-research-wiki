---
type: concept
title: "Collaborative UAV Communication"
tags: [uav, swarm, communication, coordination, control]
related:
  - "[[javaid-2023-collaborative-uav-communication-control]]"
  - "[[autonomous-uav-swarms]]"
  - "[[uav-to-x-communication]]"
  - "[[cellular-connected-uav]]"
  - "[[space-air-ground-integrated-network]]"
created: 2026-07-12
updated: 2026-07-12
---

# Collaborative UAV Communication

Collaborative UAV communication is the networking layer that lets multiple UAVs exchange state, sensing data, control intent, and task information so the fleet can coordinate as one system. It includes direct UAV-to-UAV links and UAV-to-terrestrial, satellite, or HAP infrastructure, with link requirements shaped by mobility, topology changes, range, latency, and onboard energy.

[[javaid-2023-collaborative-uav-communication-control]] treats this communication layer as inseparable from control, localization, collision avoidance, task allocation, and shared computation. It complements [[autonomous-uav-swarms]] and [[uav-to-x-communication]]: the former covers the broader autonomy stack, while the latter provides a cellular cooperation case for UAV-to-network and UAV-to-UAV traffic.
