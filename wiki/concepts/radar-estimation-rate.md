---
type: concept
title: "Radar Estimation Rate"
tags: [radar-sensing, information-theory, integrated-sensing-computation-communication]
related:
  - "[[liu-2025-aoi-iscc-five-stage]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[age-of-information]]"
created: 2026-07-13
updated: 2026-07-13
---

# Radar Estimation Rate

An information-theoretic proxy for the amount of target information carried by a radar echo. It maps radar-echo SNR into the rate-like quantity `log2(1 + Gamma_rad)`; multiplying this rate by the single-sensing interval gives the modeled data amount for one detection.

[[liu-2025-aoi-iscc-five-stage]] multiplies this per-detection quantity by repeated sensing decisions and trades the resulting data amount against same-slot [[age-of-information]]. It remains a modeled information measure rather than a directly validated payload size.
