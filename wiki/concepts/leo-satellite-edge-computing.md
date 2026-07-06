---
type: concept
title: LEO Satellite Edge Computing
tags: [leo-satellite, mec, 6g, ntn]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[chen-2026-pddqn-sagin-mec]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[free-space-optical-isl]]"
created: 2026-05-28
updated: 2026-07-07
---

# LEO Satellite Edge Computing

[[mobile-edge-computing|MEC]] where a Low Earth Orbit constellation hosts the edge servers, complementing or replacing terrestrial infrastructure for users in remote / harsh / sparsely-populated regions. The development is driven by:

- Falling launch costs (SpaceX, OneWeb, etc.) making large LEO constellations economically viable.
- Onboard compute reaching levels where local task processing avoids the long round-trip to ground cloud.
- 6G use cases (immersive comms, intelligent transportation, metaverse) needing low-latency compute in places terrestrial BSes don't reach.

## Distinguishing properties vs terrestrial / UAV MEC

| Property | Implication |
|---|---|
| Predictable orbital geometry | Topology is deterministic; outages are scheduled, not random. |
| High dynamics (~7.5 km/s ground velocity) | Coverage of any single ground point is brief; handovers dominate. |
| Multi-operator constellations | A renting service provider can't trust every satellite — see [[zero-trust-architecture]]. |
| Inter-satellite links (often free-space optical) | Multi-hop forwarding is a natural offloading destination decision; see [[free-space-optical-isl]] (and the routing implications in [[mao-2024-fso-leo-hierarchical-routing]]). |
| Energy / compute heterogeneity | LEOs vary widely in onboard compute capacity. |

## Typical optimization formulations

- Joint trajectory + offloading at terrestrial vs LEO vs cloud — but trajectories are *not* free here; they're orbital mechanics.
- Coverage-time-aware FL aggregation — pick aggregator satellites that will still see participants when the round closes.
- Offload to "satellite that has just left" so training continues without dropout — a unique LEO trick.
- LEO-UAV cooperative MEC in remote regions, where a UAV handles flexible local access and LEO satellites add wide-area compute under coverage-time constraints, as in [[chen-2026-pddqn-sagin-mec]].

## Trust dimension

Because operators may rent across companies, classical "central trusted aggregator" patterns from FL break. This is the entry point for [[blockchain-for-fl-aggregation]] and [[zero-trust-architecture]] schemes such as [[mao-2025-bcsa-frl]]'s BCSA-FRL.
