---
type: concept
title: "Ambient-Interference-Aided Covertness"
tags: [covert-communication, stochastic-geometry, interference, physical-layer-security]
related:
  - "[[chen-2026-air-ground-covert]]"
  - "[[covert-communication]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[air-to-ground-channel-model]]"
  - "[[cooperative-jamming]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
created: 2026-07-11
updated: 2026-07-11
---

# Ambient-Interference-Aided Covertness

Ambient-interference-aided covertness treats uncontrolled co-channel transmissions as the uncertainty that hides Alice's activity from Willie. It is the passive counterpart to [[cooperative-jamming]]: Alice does not coordinate a helper jammer, but exploits the distribution of environmental interference that Willie must observe through.

In [[chen-2026-air-ground-covert]], ground interferers follow a homogeneous PPP. Their aggregate power is approximated by a gamma distribution, allowing the paper to derive Willie's radiometer threshold, average covert probability, Bob's connection probability, and covert throughput under a location-uncertain Willie. The important tradeoff is explicit: more interferer density or power improves covertness but damages Bob's reliability.

This concept is useful whenever [[covert-communication]] is analyzed at network scale. It connects the covertness constraint to [[stochastic-geometry-network-analysis]] rather than to a single engineered jammer or beamformer.

[[aerial-observation-control-covertness-surveillance-and-monitoring]] places this uncontrollable interference baseline beside primary-signal, sensing-signal, and receiver-jamming masks without transferring their detector assumptions.
