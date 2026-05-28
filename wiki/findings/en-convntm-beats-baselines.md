---
type: finding
title: EN-ConvNTM beats j-PPO baselines on equilibrium efficiency
source: "[[liu-2026-jppo-en-convntm]]"
confidence: medium
replicated: null
tags: [drl, benchmark, mec]
related:
  - "[[en-convntm]]"
  - "[[j-ppo-en-convntm]]"
  - "[[equilibrium-efficiency-metric]]"
  - "[[neuralmap-loses-spatial-info]]"
created: 2026-05-28
updated: 2026-05-28
---

# EN-ConvNTM beats j-PPO baselines on equilibrium efficiency

In [[liu-2026-jppo-en-convntm]] (Fig. 4 / Fig. 5), `j-PPO+EN-ConvNTM` outperforms all four ablations — vanilla `j-PPO`, `j-PPO+ConvNTM`, `j-PPO+ConvLSTM`, `j-PPO+NeuralMap` — on the [[equilibrium-efficiency-metric]] $\Omega$ across all tested UAV counts (1–5) and charging-station counts (1–5).

Reported gains over `j-PPO+ConvNTM` (the strongest baseline) at fixed 2 charging stations:

| # UAVs | Δ Ω |
|---|---|
| 1 | +9.91% |
| 2 | +8.06% |
| 3 | +17.60% |
| 4 | +14.95% |
| 5 | +21.21% |

At fixed 2 UAVs, varying charging stations:

| # Stations | Δ Ω |
|---|---|
| 1 | +7.34% |
| 2 | +11.30% |
| 3 | +7.62% |
| 4 | +11.65% |
| 5 | +6.14% |

## Mechanism (per the authors)

- The [[stn]] front-end + attention-driven enhancement let EN-ConvNTM exploit longer histories than ConvNTM.
- The 3-D external memory keeps per-UAV identities distinguishable, unlike NeuralMap — see [[neuralmap-loses-spatial-info]].
- The whole stack still inherits PPO's stability via [[j-ppo]]'s clipped hybrid objective.

## Caveats

- Single-paper result — no independent replication yet, hence `confidence: medium`.
- Box-plots in the paper show overlap between EN-ConvNTM and ConvNTM at low UAV count (1 UAV); the gap widens with scale.
- Simulation only; no hardware-loop or wind/turbulence modeling.
