---
type: concept
title: "First-Order Radio Energy Model (Heinzelman)"
tags: [wireless-sensor-network, iot, energy-model, routing, channel-modeling]
related:
  - "[[omrp-overlap-routing]]"
  - "[[hot-spot-problem-iot]]"
  - "[[air-to-ground-channel-model]]"
  - "[[energy-latency-tradeoff]]"
  - "[[li-2025-omrp-cb-iot]]"
  - "[[guang-2026-hiswta-mcs]]"
created: 2026-06-03
updated: 2026-07-13
---

# First-Order Radio Energy Model (Heinzelman)

The first-order radio energy model is the canonical per-bit energy model used in WSN / IoT routing-protocol research, originating with Heinzelman's work on clustering protocols (LEACH). It is the inter-node energy model used in [[li-2025-omrp-cb-iot]].

## Formulation
Energy to **transmit** b bits over distance d:

> ETx(b, d) = b·Eelec + b·εfs·d²,  d < d₀  (free-space regime)
> ETx(b, d) = b·Eelec + b·εmp·d⁴,  d ≥ d₀  (multipath regime)

Energy to **receive** b bits:

> ERx(b) = b·Eelec

where Eelec is the per-bit transmitter/receiver electronics energy, εfs and εmp are the free-space and multipath amplifier coefficients, and d₀ is the crossover distance between the two regimes.

## Key properties
- **Symmetric receive cost:** receiving costs Eelec per bit regardless of distance.
- **Quadratic vs. quartic scaling:** short links are dominated by electronics; long links are dominated by amplifier energy with d⁴ scaling, making long transmissions very expensive.
- **Relay incentive:** for long source-to-sink distances, relaying through an intermediate node saves energy when the shorter-link savings outweigh the extra receive + re-transmit overhead.

The relay break-even criterion in [[omrp-overlap-routing]] follows directly: relay is preferred when βmax = dᵢₛ² − dᵢⱼ² − dⱼₛ² > 2Eelec/εfs.

## Limitations
- Models a single-frequency, single-antenna, homogeneous node; it does not capture MIMO, fading variance, or heterogeneous hardware.
- No mobility — energy is distance-deterministic.
- The d² / d⁴ boundary is a simplification; real propagation depends on terrain, frequency, and antenna height. For elevated nodes (UAVs), the [[air-to-ground-channel-model]] is more appropriate.

## Usage in the corpus
This model underlies the inter-node energy calculations in [[omrp-overlap-routing]] and [[li-2025-omrp-cb-iot]] (which pairs it with a two-ray multipath model for the long IoT-to-BS uplink). [[guang-2026-hiswta-mcs]] reuses it for member-to-head and inter-head communication in a mobile UAV sensing swarm. That reuse models radio traffic but still omits aircraft propulsion, so it should not be interpreted as whole-UAV mission energy.
