---
type: concept
title: "Open Radio Access Network"
tags: [architecture, open-ran, virtualization, orchestration]
related:
  - "[[ammar-2026-oran-maritime-slicing]]"
  - "[[network-slicing]]"
  - "[[network-function-virtualization]]"
  - "[[service-function-chaining]]"
created: 2026-07-13
updated: 2026-07-13
---

# Open Radio Access Network

Open Radio Access Network (O-RAN) disaggregates radio-access functions into interoperable components with open interfaces, virtualized execution, and RAN Intelligent Controllers. The non-real-time controller trains policies and manages analytics, while the near-real-time controller applies policies and collects operational state.

[[ammar-2026-oran-maritime-slicing]] uses this architecture as the control substrate for maritime [[network-slicing]] and [[network-function-virtualization]] across mobile UAVs, tethered UAVs, and buoys. Its evaluation models the orchestration logic in simulation rather than deploying an O-RAN stack.
