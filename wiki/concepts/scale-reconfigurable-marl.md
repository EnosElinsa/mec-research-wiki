---
type: concept
title: "Scale-Reconfigurable MARL"
tags: [marl, dynamic-topology, variable-width-network, ntn, scheduling]
related:
  - "[[kim-2026-scale-reconfigurable-marl]]"
  - "[[hidden-state-sharing-marl]]"
  - "[[non-terrestrial-network]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[ma-pomdp]]"
  - "[[quantum-marl-sagin-access]]"
created: 2026-07-14
updated: 2026-07-14
---

# Scale-Reconfigurable MARL

Scale-reconfigurable MARL adapts the active width of actor and critic networks to the number of currently observable devices. A fixed maximum architecture masks unused input and hidden units, applies normalization over active units, and excludes inactive paths from forward and backward computation instead of treating absent devices as zero-valued observations.

[[kim-2026-scale-reconfigurable-marl]] applies this design to ground-station scheduling over changing visible sets of CubeSats and UAVs. Reconfiguration remains bounded by a chosen worst-case width and relies on deterministic slot ordering rather than permutation invariance; its compute reduction assumes proportional input/hidden-width scaling and is demonstrated only in a small simulation.
