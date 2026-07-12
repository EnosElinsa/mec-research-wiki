---
type: concept
title: "CRB-Guided Angular-Confidence Beamforming"
tags: [isac, beamforming, cramer-rao-bound, angle-estimation, uncertainty]
related:
  - "[[lu-2026-icsn-beamforming]]"
  - "[[cramer-rao-bound]]"
  - "[[integrated-communication-sensing-navigation]]"
  - "[[su-2024-sensing-aided-isac-pls]]"
  - "[[jitter-aware-uav-beamwidth-control]]"
created: 2026-07-13
updated: 2026-07-13
---

# CRB-Guided Angular-Confidence Beamforming

A sensing-feedback pattern that converts an angle estimate's [[cramer-rao-bound|CRB]] into an uncertainty interval, uses that interval as the next sensing mainlobe region, and reoptimizes communication and sensing covariances until the angular region stabilizes.

[[lu-2026-icsn-beamforming]] begins with an ISMR-constrained acquisition beam, then uses `angle estimate +/- confidence width` regions during weighted AO/FP refinement. This is distinct from [[jitter-aware-uav-beamwidth-control]], whose uncertainty comes from platform jitter rather than estimator information.
