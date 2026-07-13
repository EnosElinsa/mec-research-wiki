---
type: concept
title: "Imperfect SIC Residual Interference"
tags: [noma, successive-interference-cancellation, residual-interference, wireless]
related:
  - "[[huyen-2026-short-packet-aris-noma]]"
  - "[[li-2026-noma-uav-relay-planning]]"
  - "[[noma-af-uav-relaying]]"
  - "[[noma]]"
created: 2026-07-13
updated: 2026-07-14
---

# Imperfect SIC Residual Interference

Imperfect successive interference cancellation leaves a fraction of a decoded user's signal in the receiver after cancellation. NOMA analyses commonly represent this leakage with a residual coefficient: zero gives ideal SIC, while a positive coefficient adds residual power to later users' SINR denominators.

In [[li-2026-noma-uav-relay-planning]], residual SIC is part of the two-hop [[noma-af-uav-relaying]] rate model and is fixed at 0.01 in the default simulation. It couples NOMA power coefficients to beamforming, relay amplification, and trajectory because geometry and power changes alter both the desired signal and uncancelled interference.

This page refines the error-propagation caveat in [[noma]]. A fixed residual coefficient is a sensitivity model; without estimation-error statistics or receiver measurements, it is not an experimentally calibrated SIC-error guarantee.

[[huyen-2026-short-packet-aris-noma]] uses the same fixed residual-coefficient abstraction in a finite-blocklength active-RIS downlink. Its default value is 0.01, but no receiver-estimation statistics or hardware calibration support that choice.
