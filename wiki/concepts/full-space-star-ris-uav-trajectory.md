---
type: concept
title: "Full-Space STAR-RIS UAV Trajectory"
tags: [star-ris, uav, trajectory, role-switching, physical-layer-security]
related:
  - "[[meng-2026-fullspace-star-ris-secure]]"
  - "[[star-ris]]"
  - "[[uav-trajectory-control]]"
  - "[[physical-layer-security]]"
  - "[[csi-estimation-error]]"
created: 2026-07-13
updated: 2026-07-13
---

# Full-Space STAR-RIS UAV Trajectory

A full-space STAR-RIS trajectory model allows a mobile node to cross the surface plane instead of remaining permanently on one reflecting or transmitting side. The node's side then changes which STAR-RIS coefficient and cascaded channel apply, coupling physical trajectory with reflection/transmission role assignment.

[[meng-2026-fullspace-star-ris-secure]] introduces a binary side variable and unified channel expressions for a UAV that can move through both half-spaces. Its DS-JO method alternates robust STAR-RIS coefficient and role optimization with trajectory SCA while maximizing worst-case secrecy rate under norm-bounded eavesdropper-CSI uncertainty.

This is narrower than generic [[star-ris]] coverage. Fixed-side STAR-RIS formulations can assign one stable transmission/reflection geometry for the mission; full-space motion must also handle plane crossings, side boundaries, and discrete role changes. Relaxation and Gaussian randomization make the resulting mixed-integer design local and approximate rather than a global trajectory guarantee.
