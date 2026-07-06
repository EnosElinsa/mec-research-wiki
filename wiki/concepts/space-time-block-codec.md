---
type: concept
title: "Space-Time Block Codec"
tags: [isac, cooperative-sensing, stbc, ofdm]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[networked-isac]]"
  - "[[cramer-rao-bound]]"
  - "[[wang-2026-stbc-cooperative-isac]]"
created: 2026-07-07
updated: 2026-07-07
---

# Space-Time Block Codec

A coding structure that spreads transmitted symbols across antennas, base stations, time, or OFDM symbols so a receiver can separate the contributing signals after propagation. In cooperative ISAC, the same idea can turn reflected inter-BS interference into separable bistatic sensing echoes.

In [[wang-2026-stbc-cooperative-isac]], multiple BSs transmit ISAC signals over the same time-frequency resources. A space-time block codec lets receiving BSs decode echo components associated with different transmitting BSs, enabling shared-resource cooperative sensing rather than forcing BSs onto orthogonal resources.
