---
type: concept
title: "Finite-Blocklength URLLC"
tags: [urllc, finite-blocklength, short-packet, reliability, latency, channel-model]
related:
  - "[[wang-2026-covert-cognitive-radio]]"
  - "[[primary-signal-assisted-covertness]]"
  - "[[huyen-2026-short-packet-aris-noma]]"
  - "[[feng-2026-secure-short-packet-noma-relay]]"
  - "[[zhang-2026-irs-uav-covert-fbl]]"
  - "[[csi-estimation-error]]"
  - "[[energy-latency-tradeoff]]"
  - "[[task-offloading]]"
  - "[[wu-2024-urllc-uav-mec-latency]]"
  - "[[covert-communication]]"
  - "[[zhang-2026-air-ground-covert-jamming]]"
  - "[[xie-2023-wireless-powered-short-packet-uav]]"
  - "[[zhu-2026-fas-uav-fbl]]"
created: 2026-05-31
updated: 2026-07-14
---

# Finite-Blocklength URLLC

[[huyen-2026-short-packet-aris-noma]] derives average BLER and achievable-rate expressions for a two-user active-RIS NOMA link with imperfect SIC. The derivation relies on a Gamma approximation for the cascaded channel and a piecewise-linear Q-function approximation, so its later "exact" expressions remain conditional on those modeling approximations.

**Ultra-reliable low-latency communication (URLLC)** sends very **short packets** (e.g. 20–32 bytes), so the transmission blocklength and channel-code length are **finite** and the decoding-error probability cannot be ignored. As a result the **Shannon capacity formula** — which assumes infinite blocklength — overstates the achievable rate, and the finite-blocklength rate (a function of SNR, blocklength, and target decoding-error probability) must be used instead.

This matters for MEC offloading: using Shannon rates yields optimistic latency estimates, so an accurate finite-blocklength rate expression is needed to correctly optimize bandwidth, CPU frequency, and node placement for mission-critical tasks.

[[zhang-2026-air-ground-covert-jamming]] uses finite-blocklength decoding on a covert relay link, where decoding reliability and covert throughput are coupled with jammer redirection, RIS phase design, and UAV trajectory/user scheduling.

In the wiki, [[wu-2024-urllc-uav-mec-latency]] is the corpus's first UAV-MEC study to drop the infinite-blocklength assumption: it derives a finite-blocklength offloading rate under **angle-dependent Rician fading**, approximates it logarithmically, and shows a significant latency gap versus a Shannon-based scheme — demonstrating that the accurate expression is necessary for the optimization.

[[xie-2023-wireless-powered-short-packet-uav]] applies the same finite-blocklength rate penalty to WPT-powered IoT uploads, jointly allocating frame symbols, UAV hover location, and downlink charging power for communication-side energy efficiency.

[[zhu-2026-fas-uav-fbl]] adds receiver-side spatial selection to short-packet UAV relaying. Its effective fluid-antenna diversity lowers the access-hop BLER, but per-port probing consumes channel uses and energy, so useful port count is constrained by the same finite blocklength it is intended to protect. A fixed-power first hop also creates an end-to-end error floor that access-hop diversity cannot remove.
