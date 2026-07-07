---
type: concept
title: "UAV Forest-Fire Detection"
tags: [uav-swarm, forest-fire-detection, edge-intelligence, robustness]
related:
  - "[[li-2026-tspf-forest-fire-uav-swarm]]"
  - "[[two-tier-submodel-partition]]"
  - "[[edge-intelligence]]"
  - "[[multi-uav-assisted-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# UAV Forest-Fire Detection

UAV forest-fire detection uses aerial sensing and onboard/edge inference to identify fire conditions while the aircraft operate in communication- and failure-constrained environments. In [[li-2026-tspf-forest-fire-uav-swarm]], the fire-detection workload is the motivating application for robust UAV-swarm learning: UAVs collect fire-scene images/videos, train a ResNet18-style detector on the FLAME dataset, and rely on [[two-tier-submodel-partition]] plus intragroup backup to retain training data after UAV destruction.

Within the wiki, this is a failure-resilience counterpart to UAV-swarm inference entries such as [[sun-2024-asap-uav-swarm]], [[qu-ecoei-uav-swarm]], and [[wang-2026-scalable-multiuav-analytics]].
