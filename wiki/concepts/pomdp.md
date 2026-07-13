---
type: concept
title: POMDP (Partially Observable MDP)
tags: [drl, theory]
related:
  - "[[huang-2026-intelligent-jamming-maritime]]"
  - "[[ppo]]"
  - "[[j-ppo]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[ma-pomdp]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
created: 2026-05-28
updated: 2026-07-14
---

# POMDP (Partially Observable Markov Decision Process)

An MDP $(\mathcal{S}, \mathcal{A}, P, r, \gamma)$ where the agent does not directly observe state $\mathbf{s}_n$ but only an observation $\mathbf{o}_n \sim P_r(\mathbf{o}_n|\mathbf{s}_n)$. Decisions therefore must condition on the *history* $\mathbf{h}_n = (\mathbf{o}_0, \mathbf{a}_0, \ldots, \mathbf{o}_n)$ rather than the instantaneous observation.

In [[liu-2026-jppo-en-convntm]] the multi-UAV path-planning problem is cast as a POMDP because:

- Each UAV has only a partial view of the device population (the channels of the observation grid).
- IoT devices move stochastically per the [[gauss-markov-mobility-model]], so the *true* state is the full joint position/velocity vector — never directly observed.
- Charging-station availability and inter-UAV positions also need to be aggregated over time.

This is what motivates the [[en-convntm]] history integrator: it compresses the history $(\mathbf{o}_0, \ldots, \mathbf{o}_n)$ into $\mathbf{h}_n$ so [[j-ppo]] can act and value-estimate against a sufficient summary.
