---
type: concept
title: "Directional Neighbor Discovery"
tags: [fanet, neighbor-discovery, directional-antenna, random-access]
related:
  - "[[fan-2026-directional-neighbor-discovery]]"
  - "[[directional-fanet-link-maintenance]]"
  - "[[stateless-geographic-fanet-routing]]"
created: 2026-07-13
updated: 2026-07-13
---

# Directional Neighbor Discovery

The process by which nodes with sectorized or beam-steered antennas identify reachable peers and their directions before routing or link maintenance can begin. Unlike omnidirectional discovery, each node must divide time among sector selection, transmission, reception, and listening while avoiding collisions with neighbors making independent choices.

[[fan-2026-directional-neighbor-discovery]] models synchronous slotted and asynchronous Poisson-like variants and optimizes these probabilities using power-delay surrogates. Its prior-topology assumption means it optimizes rediscovery/sector access over a potential-neighbor set rather than discovering completely unknown identities from scratch.
