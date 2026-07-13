---
type: concept
title: "Conditional-Judgment Binary Search"
tags: [optimization, integer-search, uav-mounted-ris]
related:
  - "[[zhao-2026-uav-irs-data-collection]]"
  - "[[uav-mounted-ris]]"
  - "[[mixed-integer-nonlinear-programming]]"
created: 2026-07-13
updated: 2026-07-13
---

# Conditional-Judgment Binary Search

An integer-search procedure that first determines a feasible interval, classifies the objective over that interval as monotone or decrease-then-increase, and then selects an endpoint or performs binary search around the turning point.

[[zhao-2026-uav-irs-data-collection]] uses it to choose the number of active reflecting elements for a fixed hover position. Its scalar global-optimum claim depends on an imported unimodality premise and does not extend to the paper's coupled hover-location and visit-order problem.
