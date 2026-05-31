---
type: concept
title: Hierarchical Aerial MEC
tags: [architecture, aerial-network, mec]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[air-ground-integrated-network]]"
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-28
updated: 2026-06-01
---

# Hierarchical Aerial MEC

A multi-tier aerial MEC stack where each tier handles tasks suited to its compute / coverage / endurance profile. Typical 2-tier:

- **Lower tier:** UAVs at 50–500 m, dense local coverage, limited compute and battery.
- **Upper tier:** [[high-altitude-platform-station|HAPS / HAS]] at ~20 km, wide footprint, abundant compute and energy.

Optionally extended with a third tier (LEO satellite) for global backhaul.

## Routing pattern

```
IMD ─── (admission) ──→ UAV ─── (overflow) ──→ HAPS ─── (offload) ──→ Cloud
                            ↓                       ↓
                     compute locally        compute on HAPS
```

UAVs handle small / urgent tasks; HAPS handles large / non-urgent overflow. The admission and overflow decisions are the optimization variables; trajectories add another layer of design freedom.

## Why hierarchy beats flat

- **Latency:** small jobs stay local; large jobs that would crush a UAV go up where there's compute headroom.
- **Energy:** UAVs are spared from running long compute jobs that would force more recharge cycles.
- **Coverage:** HAPS umbrella catches IMDs that no UAV can reach.

## In this wiki

[[peng-2025-drudm-cfg]] is the canonical example here — UAVs admit via DRUDM, overflow upward to a HAS via priority queue. Other hierarchical-aerial sources such as [[bi-2025-sg-mapg]] (SG-MAPG) and the low-altitude-economy survey [[wang-2025-lae-network-survey]] sit in this design space too.

## Open question

How should the **upper-tier compute** be partitioned across UAV-overflow tasks vs IMD direct-offloads? The papers we've seen so far choose extreme positions (one or the other). A balanced split is a worthwhile thesis to interrogate as more sources accumulate.
