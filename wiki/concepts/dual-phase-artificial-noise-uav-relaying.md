---
type: concept
title: "Dual-Phase Artificial-Noise UAV Relaying"
tags: [uav-relaying, artificial-noise, physical-layer-security, noma, finite-blocklength]
related:
  - "[[feng-2026-secure-short-packet-noma-relay]]"
  - "[[artificial-noise-aided-physical-layer-security]]"
  - "[[uav-mobile-relaying]]"
  - "[[finite-blocklength-urllc]]"
  - "[[noma]]"
  - "[[imperfect-sic-residual-interference]]"
created: 2026-07-14
updated: 2026-07-14
---

# Dual-Phase Artificial-Noise UAV Relaying

Dual-phase artificial-noise UAV relaying protects both hops of a half-duplex relay path: the ground source injects artificial noise during source-to-relay transmission, and the UAV injects it again while forwarding to users. Receive combining or channel-null-space projection suppresses the noise at intended receivers while exposing an eavesdropper on both phases.

[[feng-2026-secure-short-packet-noma-relay]] applies this pattern to a two-user [[noma|NOMA]] decode-and-forward link under [[finite-blocklength-urllc|finite blocklength]]. In Phase I the source uses the non-dominant right singular vectors and the relay combiner rejects their contribution; only the Phase-II noise is explicitly placed in the joint user-channel null space. The eavesdropper is conservatively allowed perfect SIC and combines both phase SINRs.

The pattern requires enough transmit antennas and accurate legitimate-channel knowledge to form the null spaces. The supporting model assumes perfect nulling, ideal legitimate SIC, a known passive eavesdropper, fixed beam constructions, and a hovering relay; residual interference such as [[imperfect-sic-residual-interference]] and channel-estimation overhead are outside its scope.
