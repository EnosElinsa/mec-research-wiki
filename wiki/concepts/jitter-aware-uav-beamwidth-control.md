---
type: concept
title: "Jitter-Aware UAV Beamwidth Control"
tags: [uav-communications, mmwave, beamwidth, jitter, beam-misalignment]
related:
  - "[[liu-2026-uav-hsr-jitter]]"
  - "[[directional-fanet-link-maintenance]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[air-to-ground-channel-model]]"
  - "[[jin-2026-jitter-aware-uav-comp]]"
created: 2026-07-13
updated: 2026-07-13
---

# Jitter-Aware UAV Beamwidth Control

Jitter-aware beamwidth control selects a directional-beam codebook entry from an explicit model of platform angular disturbance. Narrow beams offer more directivity but lose alignment faster; when scanning covers a fixed angular range, they can also require more training directions and allow more jitter to accumulate before the next realignment.

In [[liu-2026-uav-hsr-jitter]], UAV angular offset follows a Gaussian random walk and enters closed-form/approximated outage and ergodic-rate expressions for co-located and distributed train antennas. A continuous stationary beamwidth is bracketed by the two nearest implementable ULA-codebook widths; evaluating both gives the discrete CA optimum and a DA approximation.

This differs from [[control-assisted-uav-beam-tracking]], which predicts beam direction from flight-controller state, and [[directional-fanet-link-maintenance]], which adjusts range and beamwidth from predicted link breakage. Here the control variable is chosen from a statistical jitter-performance model over a beam-update period.

[[jin-2026-jitter-aware-uav-comp]] treats the same platform disturbance as CSI aging in distributed CoMP and predicts the next channel sample rather than widening a directional beam.
