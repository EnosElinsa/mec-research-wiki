---
type: concept
title: "Collect-Store-Forward Relaying"
tags: [uav-communications, relaying, buffering, physical-layer-security]
related:
  - "[[xiao-2020-secrecy-energy-efficiency-relaying]]"
  - "[[uav-mobile-relaying]]"
  - "[[information-causality-constraint]]"
  - "[[physical-layer-security]]"
  - "[[secrecy-energy-efficiency]]"
created: 2026-07-14
updated: 2026-07-14
---

# Collect-Store-Forward Relaying

Collect-store-forward relaying separates reception and forwarding in space and time: a mobile relay collects data near the source, buffers it while moving, and forwards it from a more favorable location near the destination. The buffer induces an [[information-causality-constraint]] because cumulative forwarded bits cannot exceed bits already received.

[[xiao-2020-secrecy-energy-efficiency-relaying]] applies this protocol to a delay-tolerant, half-duplex fixed-wing [[uav-mobile-relaying|UAV relay]]. Its receive/forward schedule is optimized jointly with power and flight motion for [[secrecy-energy-efficiency]], so spatial channel gains must be balanced against buffering delay and propulsion cost.

The pattern is suited to delay-tolerant decode-and-forward traffic; it does not describe low-latency forwarding or amplify-and-forward relays. Any secrecy benefit also depends on the assumed eavesdropping model: the supporting source assumes the eavesdropper cannot correlate and combine the two transmissions carrying the same data.
