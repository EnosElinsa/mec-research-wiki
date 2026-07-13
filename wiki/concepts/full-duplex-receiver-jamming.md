---
type: concept
title: "Full-Duplex Receiver Jamming"
tags: [covert-communication, full-duplex, cooperative-jamming, self-interference]
related:
  - "[[cooperative-jamming]]"
  - "[[sensing-signal-assisted-covertness]]"
  - "[[covert-communication]]"
  - "[[wang-2026-fd-covert-isac]]"
created: 2026-07-14
updated: 2026-07-14
---

# Full-Duplex Receiver Jamming

A legitimate receiver simultaneously receives a covert payload and emits randomized artificial noise to confuse a warden. Stronger jamming improves the modeled detection-error bound but increases residual self-interference at the same receiver and may interfere with sensing or other legitimate functions.

[[wang-2026-fd-covert-isac]] combines this mechanism with a sensing waveform present under both warden hypotheses. Its guarantee depends on the assumed radiometer, channel distributions, jamming-power law, and bounded location uncertainty.
