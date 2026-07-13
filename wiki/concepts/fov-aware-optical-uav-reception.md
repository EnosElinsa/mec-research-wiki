---
type: concept
title: "Field-of-View-Aware Optical UAV Reception"
tags: [fso, uav, receiver-design, field-of-view, pointing-error]
related:
  - "[[kamatchi-2025-slipt-uav-fso]]"
  - "[[ground-to-uav-fso-channel]]"
  - "[[simultaneous-lightwave-information-and-power-transfer]]"
created: 2026-07-14
updated: 2026-07-14
---

# Field-of-View-Aware Optical UAV Reception

Field-of-view-aware optical UAV reception selects the receiver acceptance angle by balancing orientation tolerance against admitted background light. A wider field of view reduces interruptions when platform motion pushes the angle of arrival off axis, but eventually raises noise or interference enough to worsen outage and symbol errors.

[[kamatchi-2025-slipt-uav-fso]] shows that the preferred field of view changes with angle-of-arrival spread rather than being universally fixed. Its optima are parameter-sweep results for one analytical [[ground-to-uav-fso-channel]]; they do not account for adaptive optics, measured background-light statistics, receiver tracking dynamics, or hardware switching costs.
