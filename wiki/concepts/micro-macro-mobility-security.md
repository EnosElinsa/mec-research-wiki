---
type: concept
title: "Micro- and Macro-Mobility for Physical-Layer Security"
tags: [physical-layer-security, movable-antenna, uav-trajectory-control, beamforming]
related:
  - "[[li-not-in-parse-movable-antenna-pls]]"
  - "[[movable-antenna]]"
  - "[[physical-layer-security]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
created: 2026-07-12
updated: 2026-07-12
---

# Micro- and Macro-Mobility for Physical-Layer Security

Micro- and macro-mobility are two spatial control scales for shaping legitimate and eavesdropping channels. Micro-mobility repositions individual [[movable-antenna]] elements over wavelength-scale regions while the platform stays fixed; macro-mobility changes the UAV's flight geometry through [[uav-trajectory-control]].

[[li-not-in-parse-movable-antenna-pls]] compares the two under a common average-secrecy-rate objective. Its simulations show a regime choice rather than full substitutability: low-power operation can favor local antenna movement, while higher transmit power and larger arrays allow global UAV motion to exploit stronger geometry changes. A hybrid design can therefore treat antenna positions and aircraft trajectory as complementary [[physical-layer-security]] variables with very different energy and response-time costs.
