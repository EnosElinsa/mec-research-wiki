---
type: concept
title: "Channel Inversion Power Control"
tags: [power-control, channel-state-information, covert-communication, reliability]
related:
  - "[[he-not-in-parse-cipc-covert-uav]]"
  - "[[covert-communication]]"
  - "[[physical-layer-security]]"
  - "[[csi-estimation-error]]"
  - "[[noma]]"
created: 2026-07-12
updated: 2026-07-12
---

# Channel Inversion Power Control

Channel inversion power control adjusts transmit power inversely with the instantaneous channel gain so a receiver sees a target power level. A truncated form suppresses transmission when the required power would exceed a transmitter's budget, trading availability against a more stable received signal.

[[he-not-in-parse-cipc-covert-uav]] uses truncated CIPC for a secret user whose strong signal also hides weaker NOMA covert signals. The target received power becomes a joint reliability, secrecy, and covertness variable: estimation error can trigger overcompensation, which may improve legitimate connection probability while also strengthening the adversary's observation.
