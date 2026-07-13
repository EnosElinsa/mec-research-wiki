---
type: concept
title: "Secrecy Outage Probability"
tags: [security, metric, physical-layer-security, fading, secrecy]
related:
  - "[[wen-2026-cooperative-jamming-uav]]"
  - "[[physical-layer-security]]"
  - "[[secure-computation-efficiency]]"
  - "[[csi-estimation-error]]"
  - "[[michailidis-2024-secure-ris-uav-mec-iot]]"
  - "[[he-not-in-parse-cipc-covert-uav]]"
  - "[[channel-inversion-power-control]]"
created: 2026-05-31
updated: 2026-07-12
---

# Secrecy Outage Probability

**Secrecy outage probability (SOP)** is a physical-layer-security metric: the probability that the achievable **secrecy rate** (legitimate-link capacity minus eavesdropper-link capacity) falls below a target threshold, i.e. that secure transmission fails. It is the security analogue of the ordinary outage probability and is usually derived analytically from the fading statistics of the legitimate and eavesdropper channels.

## In this wiki

- [[michailidis-2024-secure-ris-uav-mec-iot]] derives analytical, closed-form, and asymptotic SOP expressions over independent non-identical **Nakagami-m** fading channels for a UAV-RIS-MEC-IoT network with colluding aerial eavesdroppers (maximum-ratio combining) and ground eavesdroppers, then balances SOP against energy when maximizing [[secure-computation-efficiency]]. SOP grounds the security side of the [[physical-layer-security]] thread.
- [[he-not-in-parse-cipc-covert-uav]] derives SOP jointly with secret/covert connection and detection-error probabilities, exposing how [[channel-inversion-power-control]] and covert-user interference affect both confidentiality and covertness.
