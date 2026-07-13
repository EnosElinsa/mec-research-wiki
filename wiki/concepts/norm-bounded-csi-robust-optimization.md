---
type: concept
title: "Norm-Bounded CSI Robust Optimization"
tags: [robust-optimization, csi-uncertainty, beamforming, physical-layer-security]
related:
  - "[[yao-2026-secure-maritime-sutn]]"
  - "[[csi-estimation-error]]"
  - "[[s-procedure-for-csi-uncertainty]]"
  - "[[physical-layer-security]]"
created: 2026-07-14
updated: 2026-07-14
---

# Norm-Bounded CSI Robust Optimization

A deterministic robust-design model in which an uncertain channel is written as an estimate plus an unknown error whose norm is bounded by a prescribed radius. The optimizer enforces QoS or secrecy constraints for every channel inside that uncertainty set.

[[yao-2026-secure-maritime-sutn]] applies this model to outdated satellite-related and eavesdropper CSI in a maritime satellite-UAV-terrestrial network. Its guarantee is limited to the selected uncertainty balls; it does not cover arbitrary model mismatch or an incorrectly chosen radius.
