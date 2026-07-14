---
type: concept
title: "Position-Gated Velocity Nearest-Neighbor Association"
tags: [target-association, trajectory-tracking, position, velocity]
related:
  - "[[yan-2026-uav-trajectory-monitoring]]"
  - "[[uav-trajectory-monitoring]]"
created: 2026-07-14
updated: 2026-07-14
---

# Position-Gated Velocity Nearest-Neighbor Association

A two-stage target-to-track association rule. A covariance-weighted position gate first removes implausible trajectories; among the survivors, minimum velocity difference selects the track. Velocity breaks ties when targets occupy similar positions, such as near crossing trajectories.

[[yan-2026-uav-trajectory-monitoring]] calls this WGVDNN and also uses consecutive-slot association to initialize new tracks. Correct association is demonstrated on constructed simulations rather than guaranteed for arbitrary target density, measurement error, or motion.
