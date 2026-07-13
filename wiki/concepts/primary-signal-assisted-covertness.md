---
type: concept
title: "Primary-Signal-Assisted Covertness"
tags: [covert-communication, cognitive-radio, masking-interference, finite-blocklength]
related:
  - "[[wang-2026-covert-cognitive-radio]]"
  - "[[cooperative-cognitive-radio]]"
  - "[[covert-communication]]"
  - "[[cooperative-jamming]]"
created: 2026-07-14
updated: 2026-07-14
---

# Primary-Signal-Assisted Covertness

A useful primary-user waveform masks a secondary covert waveform at a warden while continuing to carry primary data. This differs from dedicated [[cooperative-jamming]] because the masking power also serves a communication obligation rather than only generating artificial interference.

[[wang-2026-covert-cognitive-radio]] uses the forwarded primary signal in this role. Its covertness statement comes from a conservative finite-blocklength KL-divergence bound under the paper's channel and detector assumptions; it is not a detector-independent guarantee.
