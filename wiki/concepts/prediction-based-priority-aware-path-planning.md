---
type: concept
title: "Prediction-Based Priority-Aware Path Planning (PB-PAPP)"
tags: [uav, path-planning, disaster-response, survivor-detection, heuristic]
related:
  - "[[v-2026-pb-papp-survivor-detection]]"
  - "[[tree-structured-weight-synthesis]]"
  - "[[post-disaster-mec]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-14
updated: 2026-07-14
---

# Prediction-Based Priority-Aware Path Planning (PB-PAPP)

A disaster-search routing heuristic that converts predicted survivor likelihoods into route priorities. In [[v-2026-pb-papp-survivor-detection]], logistic regression scores unvisited grid cells from neighboring observations, then a modified Clarke-Wright savings procedure sorts and merges route segments so higher-priority potential survivor locations are reached earlier. It is a lightweight heuristic with synthetic-grid evidence, not an optimal solver for the underlying multi-agent orienteering problem.
