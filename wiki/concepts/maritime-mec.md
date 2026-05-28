---
type: concept
title: "Maritime MEC"
tags: [maritime, mec, msar, hap, mass, ocean]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
created: 2026-05-29
updated: 2026-05-29
---

# Maritime MEC

Edge computing for maritime scenarios — search and rescue, vessel traffic management, oceanic IoT, environmental monitoring. The defining constraints:

- **No terrestrial infrastructure** at sea, so compute tiers come from aerial platforms (UAVs, [[high-altitude-platform-station|HAPS]]) or sea-surface vessels (Maritime Autonomous Surface Ships — MASSs).
- **Air-to-sea channel** is Rician fading with shadow fading from waves, plus a "ducting" propagation effect that lowers path-loss exponent below 2 over the sea surface.
- **CSI is partially deterministic** along known shipping routes (used in [[wang-2026-aerial-marine-msar]] to side-step CSI uncertainty).

The wiki has two maritime sources:

- [[wang-2026-aerial-marine-msar]] — three-tier MEC (UAV + HAPS + MASS) for **maritime search and rescue (MSAR)**, joint task offloading + resource allocation via matching + convex.
- [[liu-2025-haps-uav-maritime-iot]] — communication architecture (HAP-as-backhaul, UAV multicast, vessel unicast) without compute offloading.

Together they describe both layers (communication + compute) of a maritime MEC stack.
