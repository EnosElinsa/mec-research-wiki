---
type: concept
title: High-Density Mobile Device Scenarios
tags: [iot, mobility, urban, scenario]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-06-01
---

# High-Density Mobile Device Scenarios

The operating regime that motivates [[liu-2026-jppo-en-convntm]]. Characterized by:

- many IoT devices per unit area (e.g. 256 devices in a 160 m × 160 m square in their simulation — that's 1 device per ~100 m²)
- non-trivial mobility — devices reposition between time slots according to a stochastic process such as the [[gauss-markov-mobility-model]]
- bursty / heterogeneous task demand
- LoS channel approximations remain reasonable because the UAV altitude $h_u$ provides geometric advantage

## Why this regime is hard for off-the-shelf MEC

- A static UAV deployment under-serves crowd shifts.
- A purely reactive controller can't anticipate user motion, so trajectories thrash.
- The [[spatial-equity-index]] degrades quickly because UAVs naturally drift toward whichever cluster has the highest instantaneous demand.
- [[ppo|Vanilla PPO]] handles either continuous *or* discrete actions cleanly but not both — see [[hybrid-action-beats-pure-drl]].

## Why the LLM Wiki cares

This is the scenario class the project's [[purpose|research question]] sits inside. Sources in the corpus differ in whether they assume static, low-mobility, or high-density conditions.
