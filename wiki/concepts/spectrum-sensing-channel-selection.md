---
type: concept
title: "Spectrum Sensing & Channel Selection"
tags: [communication, spectrum, anti-jamming, sensing]
related:
  - "[[anti-jamming-mec]]"
  - "[[overlay-underlay-spectrum-access]]"
  - "[[shao-2024-drl-antijamming-mec]]"
  - "[[temporal-spectrum-cartography]]"
  - "[[zhao-2026-temporal-spectrum-cartography]]"
  - "[[information-driven-uav-spectrum-mapping]]"
  - "[[wang-2026-bayesian-uav-spectrum-mapping]]"
  - "[[yang-2026-embodied-antijamming-uav]]"
  - "[[embodied-anti-jamming-resource-allocation]]"
created: 2026-05-29
updated: 2026-07-13
---

# Spectrum Sensing & Channel Selection

Energy-detection-based **spectrum sensing** that detects whether subchannels are occupied by jammers (or by co-channel interferers) and approximately locates them, followed by **channel selection** that switches transmission to a jamming-free subchannel. A fraction of each slot is spent sensing (reducing the time available for transmission), trading sensing overhead against avoided interference.

[[wang-2026-bayesian-uav-spectrum-mapping]] adds an [[information-driven-uav-spectrum-mapping]] variant where sensing is used to construct a 3-D radio environment map rather than to choose one communication channel in the current slot.

In the wiki, [[shao-2024-drl-antijamming-mec]] calls this its "JSC" (jamming-sensing-and-communication) mechanism: sensing feeds the per-UAV channel-selection action, and the paper shows it keeps latency near-flat as the number of jammers grows (1→5) where non-selecting baselines degrade sharply. Core enabler of [[anti-jamming-mec]]; related to dynamic spectrum access ideas in [[overlay-underlay-spectrum-access]]. [[zhao-2026-temporal-spectrum-cartography]] extends the sensing side into [[temporal-spectrum-cartography]], where sparse measurements are used to reconstruct time-varying RF maps and plan where mobile UAV sensors should move next.
