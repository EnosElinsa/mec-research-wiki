---
type: finding
title: NeuralMap loses spatial information when a single agent controls multiple UAVs
source: "[[liu-2026-jppo-en-convntm]]"
confidence: medium
replicated: null
tags: [drl, ablation, memory]
related:
  - "[[en-convntm]]"
  - "[[j-ppo-en-convntm]]"
  - "[[en-convntm-beats-baselines]]"
created: 2026-05-28
updated: 2026-06-07
---

# NeuralMap loses spatial information when a single agent controls multiple UAVs

The `j-PPO+NeuralMap` baseline performed worst among the four ablations in [[liu-2026-jppo-en-convntm]]. At 2 UAVs and 2 charging stations, `j-PPO+EN-ConvNTM` reports an [[equilibrium-efficiency-metric|Ω]] **76.2% higher** than NeuralMap.

## Author's explanation

NeuralMap stores one 1-D vector per 2-D world-grid cell. When multiple UAVs occupy or pass through the same cell, their distinct identities/states get collapsed into the same vector slot, losing critical per-UAV information. Compressing 3-D observations (UAV channel, station/energy channel, visit-history channel) into a 1-D vector amplifies the loss.

[[en-convntm]]'s 3-D memory blocks plus the [[stn]]-driven attention avoid this collapse.

## Design implication

If a project wants to reuse NeuralMap, it likely needs per-UAV memory partitions or an attention-based identity disambiguation step.
