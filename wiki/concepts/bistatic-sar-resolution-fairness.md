---
type: concept
title: "Bistatic SAR Resolution Fairness"
tags: [synthetic-aperture-radar, sensing, fairness]
related:
  - "[[lv-2026-isac-sar-tlsp]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[jains-fairness-index]]"
created: 2026-07-13
updated: 2026-07-13
---

# Bistatic SAR Resolution Fairness

A mission-level imaging criterion that penalizes both poor average two-dimensional bistatic resolution and disparity in resolution across sensing areas. It is geometric sensing fairness rather than user-rate fairness such as [[jains-fairness-index]].

[[lv-2026-isac-sar-tlsp]] combines mean target-area resolution with its standard deviation, then weights that sensing term against UAV mission energy. The metric is evaluated at fixed area centers under the paper's static-target SAR model.
