---
type: concept
title: "Maritime MEC"
tags: [maritime, mec, msar, hap, mass, ocean]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[maritime-mec-architectures]]"
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[li-2026-cdto-inland-waterways]]"
  - "[[uav-usv-cooperative-mec]]"
  - "[[liao-2025-ris-uav-usv-resource-allocation]]"
created: 2026-05-29
updated: 2026-07-07
---

# Maritime MEC

Edge computing for maritime scenarios — search and rescue, vessel traffic management, oceanic IoT, environmental monitoring. The defining constraints:

- **No terrestrial infrastructure** at sea, so compute tiers come from aerial platforms (UAVs, [[high-altitude-platform-station|HAPS]]) or sea-surface vessels (Maritime Autonomous Surface Ships — MASSs).
- **Air-to-sea channel** is Rician fading with shadow fading from waves, plus a "ducting" propagation effect that lowers path-loss exponent below 2 over the sea surface.
- **CSI is partially deterministic** along known shipping routes (used in [[wang-2026-aerial-marine-msar]] to side-step CSI uncertainty).

The corpus has a substantial maritime track (sources tagged `maritime-mec`), spanning both communication and compute layers. Representative entries at the two ends of that span:

- [[wang-2026-aerial-marine-msar]] — three-tier MEC (UAV + HAPS + MASS) for **maritime search and rescue (MSAR)**, joint task offloading + resource allocation via matching + convex.
- [[liu-2025-haps-uav-maritime-iot]] — communication architecture (HAP-as-backhaul, UAV multicast, vessel unicast) without compute offloading.
- [[li-2026-cdto-inland-waterways]] — UAV-assisted inland-waterway task offloading where USVs form D2D computation-sharing clusters under UAV cluster heads.
- [[liao-2025-ris-uav-usv-resource-allocation]] — RIS-assisted [[uav-usv-cooperative-mec]] for inland waterways, with bidirectional USV tasks, hard time windows, UAV route selection, and RIS phase design.

The cross-source picture — tiering choices (three-tier aerial+surface+space vs two-edge air+space vs single mobile-edge platform), the classical-solver-heavy split, and the distinctive maritime constraints (known routes, backhaul scarcity, energy-as-headline-objective) — is mapped in [[maritime-mec-architectures]].
