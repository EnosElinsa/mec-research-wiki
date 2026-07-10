---
type: concept
title: "UAV-USV Cooperative MEC"
tags: [maritime, mec, uav, usv, cooperative-computing]
related:
  - "[[maritime-mec]]"
  - "[[uav-mounted-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[zhang-2026-fuzzy-observer-harbor-approach]]"
  - "[[event-triggered-fuzzy-state-observer]]"
  - "[[liao-2025-ris-uav-usv-resource-allocation]]"
  - "[[liao-2026-aoi-ris-uav-usv-mec]]"
  - "[[li-2026-cdto-inland-waterways]]"
  - "[[zeng-2024-usv-fleet-collaborative-offloading]]"
created: 2026-07-07
updated: 2026-07-10
---

# UAV-USV Cooperative MEC

A maritime MEC architecture in which UAVs and unmanned surface vehicles jointly provide communication, relaying, task transport, or edge-computing support. The design space differs from generic [[maritime-mec]] because air and surface agents have asymmetric mobility, energy, channel, and service-window constraints.

In [[liao-2025-ris-uav-usv-resource-allocation]], UAVs carry RIS elements to bridge blocked TBS-USV links in inland waterways, while USVs have bidirectional tasks with hard time windows. [[liao-2026-aoi-ris-uav-usv-mec]] extends the same architecture toward AoI-aware service, with a tethered UAV carrying the RIS and rotary-wing UAVs balancing USV freshness against flight energy. The corpus also includes [[li-2026-cdto-inland-waterways]], where USVs form D2D computation-sharing clusters under UAV cluster heads, and [[zeng-2024-usv-fleet-collaborative-offloading]], where UAVs offload tasks to USV fleets through an incentive mechanism.

[[zhang-2026-fuzzy-observer-harbor-approach]] is adjacent rather than an offloading paper: it treats cooperative USV-UAV harbor approach as a guidance/control problem, with [[event-triggered-fuzzy-state-observer]] estimating unmeasured states and reducing control-update frequency under nonlinear vehicle dynamics.
