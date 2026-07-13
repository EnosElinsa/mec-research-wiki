---
type: concept
title: "Gaussian-Process Moving-Horizon Traffic Estimation"
tags: [traffic-state-estimation, gaussian-process, moving-horizon-estimation, uav-sensing]
related:
  - "[[theocharides-2026-uav-traffic-estimation]]"
  - "[[uav-enabled-its]]"
  - "[[uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Gaussian-Process Moving-Horizon Traffic Estimation

Gaussian-process moving-horizon traffic estimation fills sparse road-traffic observations with uncertainty-aware virtual measurements, then estimates constrained traffic states over a finite history. GP predictive means supply missing observations and predictive variances weight their confidence inside the moving-horizon objective.

In [[theocharides-2026-uav-traffic-estimation]], UAV video-derived regional-density and transfer-flow measurements feed a macroscopic-fundamental-diagram model. Successive convexification turns the nonconvex moving-horizon problem into a sequence of convex quadratic programs, enabling aggregate regional-density and unobservable intended-destination-density estimation. The evaluation is macroscopic simulation; it does not validate the airborne video, communication, or sensing pipeline end to end.
