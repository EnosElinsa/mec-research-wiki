---
type: concept
title: "Multi-Modal UAV Coverage-Backhaul Control"
tags: [uav-control, communication-coverage, wireless-backhaul, flocking, distributed-control, resilience]
related:
  - "[[wang-2026-multimodal-uav-coverage-backhaul]]"
  - "[[wireless-backhaul]]"
  - "[[uav-trajectory-control]]"
  - "[[autonomous-uav-swarms]]"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-Modal UAV Coverage-Backhaul Control

Multi-modal UAV coverage-backhaul control reallocates aerial access points among distinct operational roles instead of optimizing one common placement objective. UAVs can explore uncovered user clusters, remain near a cluster to provide access service, or form bridge paths that connect separated clusters through an aerial backhaul.

[[wang-2026-multimodal-uav-coverage-backhaul]] selects among those roles from coverage and served-user thresholds. Flocking potentials maintain separation and velocity coherence, local centroid estimates guide service, and a distributed minimum spanning tree supplies bridge targets. A positive Fiedler value measures whether the resulting UAV graph is connected.

The method makes [[wireless-backhaul]] an explicit mobility role rather than only a placement constraint. Its adaptation depends on fixed thresholds, known cluster centers, local observations, neighbor exchange, and enough surviving UAVs to span dispersed clusters.
