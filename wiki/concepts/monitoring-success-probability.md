---
type: concept
title: "Monitoring Success Probability"
tags: [metric, wireless-information-surveillance, physical-layer-security, probability]
related:
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[wireless-information-surveillance]]"
  - "[[fully-connected-ris]]"
  - "[[threshold-based-antenna-selection]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
created: 2026-07-14
updated: 2026-07-14
---

# Monitoring Success Probability

The probability that a legitimate monitor's achievable rate exceeds the suspicious destination's rate, so the monitor can decode the suspicious transmission. Its value depends on the assumed fading distributions, available channel state, receiver/surface configuration, and whether the suspicious link includes a direct path.

[[lin-2026-fc-ris-surveillance]] derives model-specific closed forms for three antenna-selection schemes under Nakagami fading and an approximation to the suspicious composite channel. The resulting asymptotic claims should not be read as hardware-robust finite-array guarantees.

It is kept separate from covert detection error, eavesdropping success, physical-monitoring throughput, secrecy rate, and trajectory-estimation error in [[aerial-observation-control-covertness-surveillance-and-monitoring]].
