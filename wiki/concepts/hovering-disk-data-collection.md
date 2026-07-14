---
type: concept
title: "Hovering-Disk Data Collection"
tags: [uav, data-collection, coverage-disk, trajectory-planning]
related:
  - "[[zhu-2023-aoi-transformer-trajectory]]"
  - "[[uav-data-collection]]"
  - "[[generalized-traveling-salesman-problem]]"
  - "[[air-to-ground-channel-model]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Hovering-Disk Data Collection

A route abstraction in which each ground cluster can be served from any hover point inside a channel-feasible disk rather than only from the point directly above its cluster head. Moving toward a disk boundary may shorten flight distance but can reduce link rate and increase hover time.

[[zhu-2023-aoi-transformer-trajectory]] derives each disk from a fixed-altitude SNR threshold under an average probabilistic LoS/NLoS channel, then discretizes it into candidate points for [[generalized-traveling-salesman-problem|GTSP]] routing.
