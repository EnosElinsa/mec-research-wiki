---
type: concept
title: "Radar Mutual Information Rate"
tags: [radar, sensing-metric, mutual-information, isac]
related:
  - "[[huang-2026-star-ris-nearfield-isac]]"
  - "[[near-field-star-ris-isac]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[wang-2026-rmaddpg-dda-uav-isac-vehicular]]"
created: 2026-07-14
updated: 2026-07-14
---

# Radar Mutual Information Rate

Radar mutual information rate measures how much information a received echo carries about an uncertain target response under a specified signal and noise model. In an ISAC optimizer it provides a rate-like sensing utility that can be constrained or weighted beside communication rates.

[[huang-2026-star-ris-nearfield-isac]] uses this metric for the target echo in a weighted communication-and-sensing objective. [[wang-2026-rmaddpg-dda-uav-isac-vehicular]] combines radar mutual information with served-user and energy terms inside a multi-UAV control objective. The metric is model-dependent and is not interchangeable with detection probability, localization error, or tracking performance.
