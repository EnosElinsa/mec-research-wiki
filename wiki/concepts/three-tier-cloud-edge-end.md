---
type: concept
title: "Three-Tier Cloud-Edge-End Offloading"
tags: [architecture, cloud, edge, end-device, offloading]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Three-Tier Cloud-Edge-End Offloading

An offloading architecture with three vertically-stacked compute tiers:

- **End device** — the user equipment (vehicle, smartphone, IoT). Cheapest energy and latency for small tasks; insufficient compute for large ones.
- **Edge** — proximal MEC server (RSU, base station, UAV). Strong compute, low latency.
- **Cloud** — distant data center. Massive compute, high latency.

A task is offloaded to whichever tier minimizes a weighted sum of latency, energy, and monetary cost. Different from two-tier (edge-only) offloading because the cloud option absorbs the **edge overflow** when MEC servers are saturated, at the price of higher latency.

Used as the formal model in [[ma-2025-pdqn-vehicular-mec]] (vehicle → RSU MEC → cloud). Most other wiki sources are two-tier (user → UAV-MEC, user → HAP-MEC, etc.). The three-tier framing matters when **edge capacity is genuinely a bottleneck** — a single small cell rarely is, but a saturated RSU during rush hour very much is.
