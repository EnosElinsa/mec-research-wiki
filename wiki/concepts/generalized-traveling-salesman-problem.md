---
type: concept
title: "Generalized Traveling Salesman Problem"
tags: [routing, combinatorial-optimization, traveling-salesman-problem]
related:
  - "[[zhu-2023-aoi-transformer-trajectory]]"
  - "[[hovering-disk-data-collection]]"
  - "[[transformer-weighted-a-star-trajectory-planning]]"
  - "[[bi-traveling-salesman-problem-with-neighborhoods]]"
created: 2026-07-14
updated: 2026-07-14
---

# Generalized Traveling Salesman Problem

A routing problem in which candidate vertices are partitioned into groups and the tour must select one representative from each group. It is a discrete counterpart to traveling through continuous neighborhoods and remains combinatorial because both group order and representative choice affect cost.

In [[zhu-2023-aoi-transformer-trajectory]], each IoT cluster contributes a set of discretized feasible hovering points. The UAV must choose one point per cluster and an order that accounts for both flight and data-freshness cost.
