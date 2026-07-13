---
type: concept
title: "Access-Backhaul Rate Matching"
tags: [iab, outage, rate-matching, queue-stability, uav-relay]
related:
  - "[[yu-2026-ris-uav-iab-outage]]"
  - "[[integrated-access-and-backhaul]]"
  - "[[wireless-backhaul]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-07-14
updated: 2026-07-14
---

# Access-Backhaul Rate Matching

A reliability condition for relays whose access traffic must be drained by a finite-capacity backhaul. [[yu-2026-ris-uav-iab-outage]] treats a user cluster as non-outage only when every access rate exceeds its service requirement yet remains below the associated UAV backhaul rate. UAV altitude and RIS phases are then alternated to reduce access, backhaul, and data-accumulation failures together.
