---
type: concept
title: Overlay vs Underlay Spectrum Access
tags: [cognitive-radio, spectrum-sharing, wireless]
related:
  - "[[wang-2025-uav-swarm-stackelberg]]"
  - "[[zhang-not-in-parse-cellular-uav-to-x]]"
  - "[[uav-to-x-communication]]"
created: 2026-05-28
updated: 2026-07-12
---

# Overlay vs Underlay Spectrum Access

Two canonical modes for cognitive-radio spectrum sharing between **primary users (PUs)** who own the spectrum and **secondary users (SUs)** who want to share it.

| Aspect | Overlay | Underlay |
|---|---|---|
| When SU transmits | Only when PU is idle | Concurrently with PU |
| SU power | Up to license cap | Limited so SU appears as noise to PU |
| PU interference | Near-zero | Bounded by interference temperature |
| SU throughput | Bursty (depends on PU activity) | Steady (lower peak) |
| Sensing requirement | Strict — must detect PU activity reliably | Lax — just respect a power cap |

**Hybrid overlay-underlay** combines both: opportunistically use idle slots overlay-style; fall back to underlay during PU activity. Used by [[wang-2025-uav-swarm-stackelberg]] for U2U-on-U2B spectrum sharing.

[[zhang-not-in-parse-cellular-uav-to-x]] uses a cellular-UAV variant: U2N traffic is the direct network path, while U2U relay links reuse U2N and cellular-user subchannels as underlay, coupling all three interference classes.

## Why this matters for UAV swarms

UAV swarms generate dense U2U traffic that must coexist with command-and-control U2B links. Pure overlay would waste the moments when the U2B is idle but the swarm has data; pure underlay would constantly pollute the C2 link. Hybrid is the practical middle ground.

## Caveats

- Hybrid mode requires reliable spectrum sensing — UAV mobility makes this harder than for static SUs.
- Mode-switching latency adds overhead that may dominate in highly dynamic swarms.
