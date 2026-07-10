---
type: concept
title: "Event-Triggered Fuzzy State Observer"
tags: [control, event-triggered-control, fuzzy-observer, uav, usv]
related:
  - "[[zhang-2026-fuzzy-observer-harbor-approach]]"
  - "[[uav-usv-cooperative-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[control-parameterized-uav-trajectory]]"
created: 2026-07-10
updated: 2026-07-10
---

# Event-Triggered Fuzzy State Observer

An event-triggered fuzzy state observer estimates unmeasured nonlinear vehicle states while transmitting or updating control signals only when a trigger condition is met. The fuzzy observer handles uncertain nonlinear dynamics; the event-triggered layer reduces communication and actuator update load relative to continuous command updates.

In [[zhang-2026-fuzzy-observer-harbor-approach]], the observer supports cooperative USV-UAV harbor approach. The page is adjacent to [[uav-usv-cooperative-mec]] and [[control-parameterized-uav-trajectory]] because it highlights the lower-level dynamics and update-frequency constraints that service-level maritime and UAV-MEC models often compress into simple trajectory constraints.
