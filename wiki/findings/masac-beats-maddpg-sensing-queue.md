---
type: finding
title: MASAC beats MADDPG on secure aerial MEC by +15.41% sensing rate / -30.73% queue delay
source: "[[qin-2025-bcuav-masac]]"
confidence: medium
replicated: null
tags: [drl, multi-agent, masac, benchmark, sensing]
related:
  - "[[masac]]"
  - "[[maddpg-vs-masac-in-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[age-of-information]]"
created: 2026-05-30
updated: 2026-06-07
---

# MASAC beats MADDPG on secure aerial MEC by +15.41% sensing rate / -30.73% queue delay

In [[qin-2025-bcuav-masac]], the MASAC-based controller is compared against NT-MASAC, NP-MASAC, MADDPG, and PSO baselines. The parse reports the per-baseline margins explicitly (at task data scale 8×10⁵ bit):

- **Sensing rate** improved by 27.59% / 36.27% / **15.41%** / 13.16% vs NT-MASAC / NP-MASAC / **MADDPG** / PSO respectively (parse L725).
- **Queue delay** reduced by 30.77% / 35.71% / **30.73%** / 29.47% vs the same baseline ordering (parse L709).

So against **MADDPG** specifically, the proposed MASAC method gives **+15.41% sensing rate** and **−30.73% queue delay**.

## Mechanism

The problem couples long-term queue-delay and security constraints with short-term per-slot decisions (UAV trajectory, transmission power, edge resource allocation, sensing rate). [[lyapunov-optimization]] decouples the long-term constraints into a per-slot drift-plus-penalty objective, which MASAC then optimizes. SAC's entropy-regularized stochastic policy is credited with the stability advantage over MADDPG's deterministic actors — see [[maddpg-vs-masac-in-mec]] for the cross-source mechanism analysis.

## Caveats

- Single-paper result, simulation only — `confidence: medium`.
- The margins are quoted at one task-data scale (8×10⁵ bit); the gap narrows or widens with scale (parse Fig. 9).
- The blockchain-consensus compute cost is part of the system but not separated out in these specific margin numbers.

## Relation to the corpus

The direct-evidence anchor for the [[maddpg-vs-masac-in-mec]] working thesis, alongside the [[zhang-2025-ssac-mgi-heterogeneous-uav]] SSAC-vs-MADDPG result.
