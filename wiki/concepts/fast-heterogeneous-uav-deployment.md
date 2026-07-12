---
type: concept
title: "Fast Heterogeneous UAV Deployment"
tags: [uav-deployment, wireless-coverage, heterogeneous-uav, approximation-algorithm, fairness]
related:
  - "[[zhang-2019-fast-uav-deployment]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[drone-cell-3d-placement]]"
  - "[[geometric-disk-cover]]"
  - "[[fairness-metrics-in-mec]]"
created: 2026-07-13
updated: 2026-07-13
---

# Fast Heterogeneous UAV Deployment

Fast heterogeneous UAV deployment assigns aerial base stations final service positions so their coverage regions span a target area while travel-to-service delay is minimized. Fleet members may differ in speed, altitude, radius, and origin, so placement and dispatch cannot be separated.

[[zhang-2019-fast-uav-deployment]] distinguishes two objectives. Min-max deployment time protects the last-covered location and represents service fairness in disasters; min-sum time reduces average activation delay for crowds. It provides exact algorithms for same-origin min-max deployment, an order-preserving FPTAS for different origins, a bounded same-origin min-sum heuristic, and a pseudo-polynomial dynamic program for order-preserving min-sum deployment.

Unlike [[drone-cell-3d-placement]], the fleet is already given and travel time is the objective. Unlike [[geometric-disk-cover]], the task is not to minimize the number of disks. The concept is a coverage-specific instance of [[heterogeneous-uav-fleet]] planning where capability variation changes both feasibility and approximation quality.
