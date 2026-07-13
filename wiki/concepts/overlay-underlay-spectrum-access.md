---
type: concept
title: Overlay vs Underlay Spectrum Access
tags: [cognitive-radio, spectrum-sharing, wireless]
related:
  - "[[wang-2025-uav-swarm-stackelberg]]"
  - "[[zhang-not-in-parse-cellular-uav-to-x]]"
  - "[[uav-to-x-communication]]"
  - "[[azari-2020-uav-to-uav-cellular]]"
  - "[[uav-to-uav-communication]]"
created: 2026-05-28
updated: 2026-07-14
---

# Overlay vs Underlay Spectrum Access

Spectrum-sharing terminology depends on the literature. The main mechanisms are:

| Mode | Resource use | Key requirement |
|---|---|---|
| Interweave | Secondary traffic uses detected primary-idle periods | Reliable activity sensing |
| Cognitive overlay | Secondary traffic transmits concurrently while exploiting primary-message or codebook knowledge, often assisting the primary link | Primary-side knowledge and cooperative encoding |
| Cellular overlay | Traffic classes receive disjoint time-frequency partitions | Resource partitioning |
| Underlay | Traffic classes reuse resources concurrently | Power or interference constraints |

[[wang-2025-uav-swarm-stackelberg]] calls its opportunistic idle-slot plus concurrent-reuse policy “hybrid overlay-underlay.” Under the conventional cognitive-radio taxonomy, its idle-slot component is interweave access; the page preserves the paper's label while keeping the mechanisms distinct.

[[zhang-not-in-parse-cellular-uav-to-x]] uses a cellular-UAV variant: U2N traffic is the direct network path, while U2U relay links reuse U2N and cellular-user subchannels as underlay, coupling all three interference classes.

[[azari-2020-uav-to-uav-cellular]] uses the cellular partitioning definition: overlay reserves disjoint PRB fractions for aerial U2U and ground uplink traffic, whereas underlay lets U2U pairs reuse uplink PRBs and creates cross-tier interference. Its analysis therefore compares orthogonal partition against concurrent reuse, not opportunistic sensing of idle primary slots.

## Why this matters for UAV swarms

UAV swarms generate dense U2U traffic that must coexist with command-and-control U2B links. A hybrid policy can exploit detected idle periods and permit constrained concurrent reuse when the primary link is active.

## Caveats

- Interweave or hybrid access requires reliable spectrum sensing; UAV mobility makes this harder than for static SUs.
- Mode-switching latency adds overhead that may dominate in highly dynamic swarms.
