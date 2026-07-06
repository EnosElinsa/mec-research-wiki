---
type: concept
title: High-Altitude Platform Station (HAPS / HAS)
tags: [haps, has, aerial-network, ntn]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[air-ground-integrated-network]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[jia-2026-dro-lawn-trajectory]]"
  - "[[zhang-2026-dwell-time-aerial-vec]]"
created: 2026-05-28
updated: 2026-07-06
---

# High-Altitude Platform Station (HAPS / HAS)

A quasi-stationary aerial node operating in the stratosphere (typically 17–22 km altitude). Two main forms:

- **High-Altitude Airship (HAS)** — lighter-than-air, large payload, long endurance.
- **Solar-powered HAPS aircraft** (e.g. Loon-style balloons, Aquila-class fixed-wing) — smaller payload but indefinite endurance.

## Why MEC research keeps reaching for them

- **Wide footprint.** A single HAPS at 20 km altitude covers a footprint hundreds of kilometers wide — orders of magnitude bigger than a UAV at 100 m.
- **Persistent presence.** Unlike LEO satellites, a HAPS stays roughly station-keeping over a region for months.
- **Higher payload than UAVs.** Hosts much larger compute / battery resources than a battery-electric UAV.
- **Lower latency than satellite.** Round-trip is millisecond-scale, not tens of milliseconds.

This makes HAPS a natural **upper tier** in a hierarchical aerial MEC stack — UAVs cover dense pockets, HAPS provides the umbrella backstop. See [[hierarchical-aerial-mec]] and [[peng-2025-drudm-cfg]]. In [[jia-2026-dro-lawn-trajectory]], the HAP receives relayed tasks from UAVs under task-size uncertainty; in [[zhang-2026-dwell-time-aerial-vec]], the HAP is the broad-coverage fallback when vehicle-to-UAV dwell time is insufficient.

## Limitations

- Direct device→HAPS link is geometrically far and noisy; needs the UAV relay layer for delay-sensitive tasks.
- Wind and solar conditions affect station-keeping; not perfectly fixed.
- Spectrum coordination spans large geographic area, which complicates regulatory / interference management.
