---
type: concept
title: "Jain's Fairness Index"
tags: [metrics, fairness, qoe]
related:
  - "[[theil-fairness-index]]"
  - "[[spatial-equity-index]]"
  - "[[service-experience-ratio]]"
  - "[[qoe-modeling-mec]]"
  - "[[gao-2024-service-experience-cache-uav]]"
created: 2026-05-29
updated: 2026-05-29
---

# Jain's Fairness Index

A widely used fairness metric over a vector of per-user allocations $x_1,\dots,x_n$:

$$ J(x) = \frac{\left(\sum_i x_i\right)^2}{n \sum_i x_i^2} \in [1/n, 1] $$

It equals 1 when all users receive identical allocation (perfectly fair) and drops toward $1/n$ as the allocation concentrates on a few users. It is scale-independent and population-size-independent.

In the wiki, [[gao-2024-service-experience-cache-uav]] applies Jain's index to per-UE average **service delay** and divides it by the average delay to form the [[service-experience-ratio]] — coupling fairness with latency in one [[qoe-modeling-mec]] objective. It complements the corpus's other fairness measures, [[theil-fairness-index]] and [[spatial-equity-index]].
