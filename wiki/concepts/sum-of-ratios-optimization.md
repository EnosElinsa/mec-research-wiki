---
type: concept
title: "Sum-of-Ratios Optimization"
tags: [optimization, fractional-programming, non-convex, resource-allocation]
related:
  - "[[wen-2024-iscc-edge-ai]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[discriminant-gain]]"
created: 2026-06-02
updated: 2026-06-02
---

# Sum-of-Ratios Optimization

A class of fractional-programming problems whose objective is a **sum of multiple ratios** (each a fraction of two functions), maximized or minimized over a feasible set. Unlike a single-ratio fractional program — solvable by the classic [[fractional-programming-dinkelbach|Dinkelbach transform]] — a *sum* of ratios is generally harder, but when each ratio is **quasi-linear** and the feasible region is **convex**, the problem admits an **optimal** iterative solution: an outer parametric step updates auxiliary variables (one per ratio) and an inner step solves a convex subproblem.

## In this wiki

[[wen-2024-iscc-edge-ai]] is the corpus's anchor for this method. After variable transformations, its [[discriminant-gain]] maximization is shown to be equivalent to a problem whose objective is a **sum of quasi-linear ratios over a convex feasible region**, so the sum-of-ratios method solves it **optimally and iteratively**: each iteration solves a convex problem minimizing the sum of weighted sensing + quantization distortion under given class-pair discriminant gains, then updates the discriminant gains from the solved distortion levels. This is what lets the paper claim an *optimal* (not merely heuristic) ISCC resource allocation despite the original problem being non-convex. It is a distinct fractional-programming tool from the single-ratio Dinkelbach approach used elsewhere in the corpus for energy-efficiency maximization.
