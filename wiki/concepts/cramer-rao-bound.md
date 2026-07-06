---
type: concept
title: Cramér-Rao Bound (CRB / CRLB)
tags: [sensing, estimation-theory, isac, metric]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[su-2024-sensing-aided-isac-pls]]"
  - "[[zhu-2024-sensing-comm-doppler-uav-swarm]]"
  - "[[li-2026-isac-vec-beamforming-deployment]]"
  - "[[wang-2026-stbc-cooperative-isac]]"
created: 2026-05-31
updated: 2026-07-07
---

# Cramér-Rao Bound (CRB / CRLB)

A lower bound on the variance of any unbiased estimator of a deterministic parameter, given by the inverse of the **Fisher Information Matrix (FIM)**. In sensing and ISAC systems it is the standard figure of merit for **estimation accuracy** — a smaller CRB means a tighter achievable bound on the error of an angle, range, velocity, or location estimate.

## Why ISAC research keeps reaching for it

- It turns "how well can we sense?" into a single optimizable scalar (or matrix determinant/trace), so beamforming and waveform design can be cast as CRB-minimization or CRB-constrained problems.
- It composes with communication objectives: a joint design can minimize a (normalized) CRB while constraining or maximizing a communication metric, exposing the sensing-vs-communication trade-off.

## In this wiki

- [[su-2024-sensing-aided-isac-pls]] minimizes (via an FIM-determinant criterion) the CRB of the eavesdroppers'/targets' angle estimates while maximizing secrecy rate — the estimation accuracy directly shapes the secrecy-rate expression, so the CRB and the secrecy metric improve together over iterations.
- [[zhu-2024-sensing-comm-doppler-uav-swarm]] minimizes the ground vehicles' **maximum Cramér-Rao lower bound (CRLB)** for (Doppler-based velocity + position) estimation under an SNR-loss constraint, trading sensing accuracy against communication quality.
- [[li-2026-isac-vec-beamforming-deployment]] uses CRB-style sensing metrics inside an ISAC effectiveness function for UAV-assisted vehicular edge computing, where deployment and beamforming must balance road coverage, radar mutual information, and UAV energy.
- [[wang-2026-stbc-cooperative-isac]] derives and plots CRLB behavior for AoA estimation in multi-BS cooperative ISAC, using it to corroborate the observed angular-estimation RMSE trends.

Distinct from outcome metrics like [[secrecy-outage-probability]]; the CRB bounds estimator variance, not an outage event.
