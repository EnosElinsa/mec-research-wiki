---
type: concept
title: "Threshold-Based Antenna Selection"
tags: [antenna-selection, partial-csi, receiver-design, complexity-reduction]
related:
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[monitoring-success-probability]]"
  - "[[fully-connected-ris]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
created: 2026-07-14
updated: 2026-07-14
---

# Threshold-Based Antenna Selection

A sequential receiver-selection rule that examines candidate antenna-channel gains until one exceeds a prescribed threshold, falling back to the best examined candidate when none qualifies. Raising the threshold generally increases examination and channel-state overhead while approaching exhaustive maximum-gain selection.

In [[lin-2026-fc-ris-surveillance]], selection uses only FC-RIS-to-monitor reflecting-channel information before a single surface configuration is computed. Its reported performance-overhead continuum is specific to the paper's fading and surveillance model.

[[aerial-observation-control-covertness-surveillance-and-monitoring]] positions this authorized-receiver mechanism without equating its threshold or MSP with STAR-RIS service control, covert detection, or target tracking.
