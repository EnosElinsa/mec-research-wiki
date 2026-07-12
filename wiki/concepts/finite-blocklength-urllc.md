---
type: concept
title: "Finite-Blocklength URLLC"
tags: [urllc, finite-blocklength, short-packet, reliability, latency, channel-model]
related:
  - "[[csi-estimation-error]]"
  - "[[energy-latency-tradeoff]]"
  - "[[task-offloading]]"
  - "[[wu-2024-urllc-uav-mec-latency]]"
  - "[[covert-communication]]"
  - "[[zhang-2026-air-ground-covert-jamming]]"
  - "[[xie-2023-wireless-powered-short-packet-uav]]"
created: 2026-05-31
updated: 2026-07-13
---

# Finite-Blocklength URLLC

**Ultra-reliable low-latency communication (URLLC)** sends very **short packets** (e.g. 20–32 bytes), so the transmission blocklength and channel-code length are **finite** and the decoding-error probability cannot be ignored. As a result the **Shannon capacity formula** — which assumes infinite blocklength — overstates the achievable rate, and the finite-blocklength rate (a function of SNR, blocklength, and target decoding-error probability) must be used instead.

This matters for MEC offloading: using Shannon rates yields optimistic latency estimates, so an accurate finite-blocklength rate expression is needed to correctly optimize bandwidth, CPU frequency, and node placement for mission-critical tasks.

[[zhang-2026-air-ground-covert-jamming]] uses finite-blocklength decoding on a covert relay link, where decoding reliability and covert throughput are coupled with jammer redirection, RIS phase design, and UAV trajectory/user scheduling.

In the wiki, [[wu-2024-urllc-uav-mec-latency]] is the corpus's first UAV-MEC study to drop the infinite-blocklength assumption: it derives a finite-blocklength offloading rate under **angle-dependent Rician fading**, approximates it logarithmically, and shows a significant latency gap versus a Shannon-based scheme — demonstrating that the accurate expression is necessary for the optimization.

[[xie-2023-wireless-powered-short-packet-uav]] applies the same finite-blocklength rate penalty to WPT-powered IoT uploads, jointly allocating frame symbols, UAV hover location, and downlink charging power for communication-side energy efficiency.
