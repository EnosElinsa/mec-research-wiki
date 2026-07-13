---
type: concept
title: "Sensing-Signal-Assisted Covertness"
tags: [security, covert-communication, isac, beamforming]
related:
  - "[[deng-2025-covert-isac-trajectory]]"
  - "[[covert-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[ambient-interference-aided-covertness]]"
created: 2026-07-13
updated: 2026-07-13
---

# Sensing-Signal-Assisted Covertness

An ISAC transmitter can use its legitimate sensing waveform as the received-power baseline that masks whether an additional information-bearing signal is present. In [[deng-2025-covert-isac-trajectory]], each warden's covertness constraint becomes a bound on the information covariance projected onto its channel relative to the sensing-only received power.

This differs from relying on uncontrollable ambient interference: sensing beamforming, communication beamforming, and platform position can all change the masking ratio. The same coupling also creates a tradeoff because stronger sensing cover may consume power or move the UAV away from the communication-favorable geometry.

The concept does not by itself guarantee undetectability. Its evidence depends on the detector, channel/location knowledge, prior assumptions, and uncertainty model used to derive the detection-error bound.
