---
type: concept
title: "Weighted K-Means UAV Deployment"
tags: [uav-deployment, clustering, kmeans, placement]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Weighted K-Means UAV Deployment

A simple, fast initial-deployment strategy: place $N$ UAVs at the centroids of $N$ clusters of ground users, where cluster membership is determined by **weighted** distance — the weight reflects task importance, latency sensitivity, or data volume per user. Standard K-means clusters by raw geometry; weighting biases the centroids toward important users.

Used in [[jia-2025-dro-uav-hap-mec]] (WKD = Weighted K-means Deployment) as a tractable first stage before the per-slot resource allocation. The weighting matters when users have heterogeneous priorities — without weights, two low-priority users near each other can pull a UAV away from a single high-priority user.

A pragmatic alternative to game-theoretic deployment ([[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]]) and to DRL-based trajectory control ([[liu-2026-jppo-en-convntm]]). Picks computational efficiency over optimality.
