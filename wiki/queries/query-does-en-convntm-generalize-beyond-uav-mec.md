---
type: query
title: Does EN-ConvNTM generalize beyond UAV-MEC, or is it tightly fit to the 3-channel grid observation?
tags: [open-question, generalization]
related:
  - "[[en-convntm]]"
  - "[[ntm]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# Does EN-ConvNTM generalize beyond UAV-MEC?

The architecture in [[liu-2026-jppo-en-convntm]] was designed around a *very specific* observation: a 3-channel spatial grid of UAV / station / device occupancy. Open questions:

- Does the [[stn]] front-end help on a non-grid observation (e.g. graph-structured device topology)?
- Does the 3-D external memory still beat a transformer once the transformer is size-matched?
- How does training cost scale with arena size? The cited convergence bound is sublinear in iteration count but doesn't account for the per-step cost of NTM read/write.

## What would settle this

A direct port of EN-ConvNTM to:

- A non-UAV mobility task (e.g. multi-robot pursuit-evasion).
- A non-spatial observation (e.g. tabular / graph) to test whether the gain is from "external memory" generally or from "spatial-aware external memory".
