---
type: concept
title: "UAV-Enabled Intelligent Transportation Systems (ITS)"
tags: [its, uav, traffic, surveillance, data-fusion]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[multi-source-data-fusion]]"
  - "[[completion-time-difference]]"
  - "[[peng-2024-energy-time-uav-its]]"
created: 2026-05-29
updated: 2026-05-29
---

# UAV-Enabled Intelligent Transportation Systems (ITS)

Use of UAV swarms for traffic surveillance, accident reporting, parking-space detection, traffic-flow prediction, and similar transportation-management tasks. UAVs are dispatched to monitoring locations, collect surveillance data (image, video), and process it locally or via offloading to a ground edge server. Processing results then feed into a control center that fuses multi-source data to make centralized decisions.

Distinct from **vehicular MEC** ([[vehicular-mec]]) — vehicular MEC offloads tasks generated *by vehicles*; UAV-ITS offloads tasks generated *by UAVs observing vehicles*. The compute side looks similar but the workload differs.

Key wiki source: [[peng-2024-energy-time-uav-its]], which adds the **completion-time-difference** objective (synchronize finish times for fusion quality) on top of standard energy minimization.
