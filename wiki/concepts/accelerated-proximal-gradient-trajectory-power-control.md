---
type: concept
title: "Accelerated Proximal-Gradient Trajectory and Power Control"
tags: [optimization, accelerated-proximal-gradient, trajectory-optimization, power-control, non-convex]
related:
  - "[[shah-2026-cellfree-mimo-fap-control]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-13
---

# Accelerated Proximal-Gradient Trajectory and Power Control

An iterative continuous optimizer that combines gradient steps with projection/proximal operators and momentum over coupled UAV positions and transmit powers. [[shah-2026-cellfree-mimo-fap-control]] adds adaptive penalties for rate, power, capacity, and mobility violations, computes extrapolated and fallback projected candidates when needed, and retains the one with the lower objective.

The acceleration changes iteration behavior, not the non-convex problem's guarantee. The source gives sufficient step-size conditions under a Lipschitz-gradient assumption and stops on relative objective change, but does not prove recovery of the global trajectory/power optimum.
