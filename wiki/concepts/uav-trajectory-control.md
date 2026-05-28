---
type: concept
title: UAV Trajectory Control
tags: [uav, control, path-planning]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-charging-scheduling]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# UAV Trajectory Control

The continuous-action portion of the [[multi-uav-assisted-mec]] decision vector: choosing the per-step displacement of each UAV. In [[liu-2026-jppo-en-convntm]] the controller assumes:

- constant cruise speed $v_u = 10$ m/s during data-collection mode
- hover during charging
- fixed flight altitude $h_u = 35$ m
- per-step displacement bounded by $D_{\max}$

The objective is shaped by the [[equilibrium-efficiency-metric]] — coverage and fairness pull the UAV outward toward sparsely-visited regions, while the energy term and obstacle/inter-UAV penalties pull it back. Trajectories are sampled from a Gaussian policy head; see [[j-ppo]] for how this couples with the discrete decisions.
