---
type: concept
title: "Directional Modulation"
tags: [physical-layer-security, symbol-level-precoding, constellation-shaping, beamforming]
related:
  - "[[li-2026-directional-modulation-irs-uav]]"
  - "[[physical-layer-security]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[air-to-ground-channel-model]]"
created: 2026-07-13
updated: 2026-07-13
---

# Directional Modulation

Directional modulation is a symbol-level physical-layer-security technique that preserves the intended constellation in authorized spatial directions while distorting amplitude or phase elsewhere. It differs from rate-only beamforming because receiver location and each transmitted symbol directly constrain the synthesized constellation geometry.

[[li-2026-directional-modulation-irs-uav]] combines the method with a passive [[intelligent-reflecting-surface]]: digital weights, UAV position, and discrete IRS phases align symbols for legitimate users while keeping a non-colluding eavesdropper's symbols weak and phase-disturbed. A constructive-interference region and probabilistic margin handle variance-bounded Gaussian channel/noise uncertainty.

The evaluation assumes one fixed, non-colluding point eavesdropper and LoS-dominant channels with imperfect CSI. Coarse phase hardware, CSI error, or a user and eavesdropper sharing nearly the same direction can weaken constellation separation; multiple or colluding eavesdroppers are outside the evaluated model.
