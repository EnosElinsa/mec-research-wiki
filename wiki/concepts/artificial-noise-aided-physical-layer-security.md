---
type: concept
title: "Artificial-Noise-Aided Physical-Layer Security"
tags: [physical-layer-security, artificial-noise, beamforming, secrecy-rate]
related:
  - "[[guo-2026-irs-uav-isac-secrecy]]"
  - "[[feng-2026-secure-short-packet-noma-relay]]"
  - "[[physical-layer-security]]"
  - "[[cooperative-jamming]]"
  - "[[secure-irs-uav-isac]]"
  - "[[dual-phase-artificial-noise-uav-relaying]]"
created: 2026-07-14
updated: 2026-07-14
---

# Artificial-Noise-Aided Physical-Layer Security

Artificial-noise-aided [[physical-layer-security]] reserves part of the transmit signal or power for structured interference that degrades an eavesdropper more than the legitimate receiver. With multiple antennas or controllable propagation, the noise can be placed in a legitimate channel's null space or steered toward an exposed receiver.

[[guo-2026-irs-uav-isac-secrecy]] uses artificial noise alongside active beams, IRS phases, and UAV motion in secure ISAC. [[feng-2026-secure-short-packet-noma-relay]] instead injects null-space noise at both the source and relay of a two-hop short-packet link, as captured by [[dual-phase-artificial-noise-uav-relaying]].

Artificial noise consumes power and can harm communication or sensing when channel estimates, spatial nulls, or hardware are imperfect. Its benefit therefore depends on channel knowledge and available spatial degrees of freedom; it is not equivalent to a secrecy guarantee, and it differs from [[cooperative-jamming]] by not requiring a separate helper jammer.
