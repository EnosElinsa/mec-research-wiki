---
type: concept
title: "Branch-Reduce-and-Bound"
tags: [global-optimization, branch-and-bound, monotonic-optimization]
related:
  - "[[samir-2020-time-constrained-data-collection]]"
  - "[[monotonic-optimization]]"
  - "[[mixed-integer-nonlinear-programming]]"
created: 2026-07-14
updated: 2026-07-14
---

# Branch-Reduce-and-Bound

A global-optimization framework that partitions a bounded search region, removes portions that cannot improve the incumbent, and maintains lower and upper objective bounds until their gap reaches a tolerance. Reduction rules can make the search tighter than naive branch-and-bound, but complexity still grows rapidly with dimension.

[[samir-2020-time-constrained-data-collection]] applies a customized BRB method to a monotonic reformulation of joint device admission, trajectory, and resource allocation. Its global result is tolerance-qualified for the formulated small-instance problem; the paper uses SCA instead for scalable suboptimal solutions.
