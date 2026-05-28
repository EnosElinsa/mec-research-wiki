---
type: finding
title: UAV count vs energy expenditure follows an inverted-U curve
source: "[[liu-2026-jppo-en-convntm]]"
confidence: medium
replicated: null
tags: [uav, energy, scaling]
related:
  - "[[energy-expenditure-coefficient]]"
  - "[[charging-stations-improve-efficiency]]"
  - "[[uav-charging-scheduling]]"
created: 2026-05-28
updated: 2026-05-28
---

# UAV count vs energy expenditure follows an inverted-U curve

At a fixed number of charging stations, increasing the UAV count first **decreases** $\kappa_n$ (load is shared, fairness improves, less duplicated coverage), then **increases** $\kappa_n$ once UAVs start contending for the same charging stations and flying longer detours. See [[liu-2026-jppo-en-convntm]] Fig. 4(b).

## Mechanism

- **Below the optimum:** more UAVs = better territorial division + shorter average flight to nearest device cluster.
- **At the optimum:** marginal UAV adds enough fairness gain to offset its own flight-energy.
- **Above the optimum:** charging-station throughput becomes the bottleneck; UAVs detour to free stations, which inflates $E^{\text{Fly}}$ disproportionately.

## Practical reading

- For a given coverage target, there is a *finite* optimal fleet size — bigger isn't strictly better.
- The optimum shifts upward as charging-station count grows ([[charging-stations-improve-efficiency]]). Co-design fleet and infrastructure.
