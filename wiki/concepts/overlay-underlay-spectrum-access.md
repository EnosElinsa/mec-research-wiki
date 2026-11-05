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
updated: 2026-11-03
---

# Overlay vs Underlay Spectrum Access

Spectrum-sharing terminology depends on the literature. The main mechanisms are:

| Mode | Resource use | Key requirement |
|---|---|---|
| Interweave | Secondary traffic uses detected primary-idle periods | Reliable activity sensing |
| Cognitive overlay | Secondary traffic transmits concurrently while exploiting primary-message or codebook knowledge, often assisting the primary link | Primary-side knowledge and cooperative encoding |
| Cellular overlay | Traffic classes receive disjoint time-frequency partitions | Resource partitioning |
| Underlay | Traffic classes reuse resources concurrently | Power or interference constraints |

[[wang-2025-uav-swarm-stackelberg]] calls its policy “hybrid overlay-underlay,” but it is not a switch between modes. Every U2U link reuses the U2B link's reusable spectrum as underlay, with transmit power kept below an interference threshold, while U2U links sharing one U2B link buy mutually orthogonal resource blocks and so do not interfere with one another. Access is negotiated with the U2B link rather than found by sensing idle slots, so the scheme combines underlay toward the primary with cellular-overlay partitioning among secondaries and has no interweave component.

[[zhang-not-in-parse-cellular-uav-to-x]] uses a cellular-UAV variant: U2N traffic is the direct network path, while U2U relay links reuse U2N and cellular-user subchannels as underlay, coupling all three interference classes.

[[azari-2020-uav-to-uav-cellular]] uses the cellular partitioning definition: overlay reserves disjoint PRB fractions for aerial U2U and ground uplink traffic, whereas underlay lets U2U pairs reuse uplink PRBs and creates cross-tier interference. Its analysis therefore compares orthogonal partition against concurrent reuse, not opportunistic sensing of idle primary slots.

## Why this matters for UAV swarms

UAV swarms generate dense U2U traffic that must coexist with command-and-control U2B links. Conditional-switching hybrids use idle periods when the primary is silent and constrained reuse when it is active; partition-based hybrids such as the one above avoid sensing by negotiating orthogonal blocks under an interference cap.

## Caveats

- Interweave access and conditional-switching hybrids require reliable spectrum sensing; UAV mobility makes this harder than for static SUs.
- Mode-switching latency adds overhead that may dominate in highly dynamic swarms.
