---
type: concept
title: "Situation-Aware Hybrid ISAC Sensing"
tags: [isac, event-triggered-sensing, periodic-sensing, uav-control]
related:
  - "[[lyu-2026-situation-aware-uav-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[adaptive-td-isac-sensing-period]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-14
updated: 2026-07-14
---

# Situation-Aware Hybrid ISAC Sensing

A phase-dependent sensing policy that combines scheduled sensing with event-triggered sensing and selects a control response from the observed communication state. It is hybrid in both timing and actuation: one operating phase may sense periodically, while another senses only after a rate or estimation-quality trigger; the resulting correction may adjust antenna pointing alone or also move the platform.

[[lyu-2026-situation-aware-uav-isac]] applies this pattern to a two-phase UAV relay. The remote center tracks the AGV and UAV throughout Phase I, then activates UAV sensing in Phase II when the estimated UAV-to-center rate falls below a derived threshold. Beam-overlap and misalignment tests select between angle-only correction and combined angle/position control, linking [[integrated-sensing-and-communication|ISAC]] measurements to [[control-assisted-uav-beam-tracking]].

The trigger is not a general optimal sensing policy. In the source it is derived under LoS-dominant channels, simplified state and misalignment models, and fixed rule-based activation; the combined design produces a suboptimal solution of the original mixed-integer problem. It also differs from [[adaptive-td-isac-sensing-period]], which optimizes a time-division sensing duration rather than switching sensing from communication-rate degradation.
