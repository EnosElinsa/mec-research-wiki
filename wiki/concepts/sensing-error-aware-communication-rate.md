---
type: concept
title: "Sensing-Error-Aware Communication Rate"
tags: [isac, sensing-error, achievable-rate, beamforming, robust-scheduling]
related:
  - "[[wu-2026-sensing-error-uav-scheduling]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[air-to-ground-channel-model]]"
  - "[[adaptive-td-isac-sensing-period]]"
created: 2026-07-14
updated: 2026-07-14
---

# Sensing-Error-Aware Communication Rate

An expected communication-rate metric that incorporates the positioning or sensing error used by a beamformer or scheduler. Rather than evaluating a link at the sensed position as if it were exact, the metric maps position uncertainty into angular steering error, derives the resulting rate distribution, and averages rate over that error model.

[[wu-2026-sensing-error-uav-scheduling]] constructs this rate for multi-UAV [[integrated-sensing-and-communication|ISAC]]. A circular location-error region produces a bounded angular-error interval, the angle is assumed uniform, and the induced rate density is integrated to form the scheduling objective. The resulting controller jointly adapts UAV locations, user association, bandwidth, and an [[adaptive-td-isac-sensing-period]].

The metric is only as robust as its sensing-error model. The source uses CRB/MSE to bound a circular region and assumes a uniform angular error; it does not establish robustness to biased, correlated, noncircular, or empirically measured localization errors.
