---
type: concept
title: "Dynamic Space-Time Graph With Virtual Edges"
tags: [graph-optimization, routing, caching, predictive-network]
related:
  - "[[li-2026-radio-map-predictive-routing]]"
  - "[[radio-map-assisted-predictive-routing]]"
  - "[[graph-based-resource-management]]"
  - "[[uav-mobile-relaying]]"
created: 2026-07-14
updated: 2026-07-14
---

# Dynamic Space-Time Graph With Virtual Edges

A dynamic space-time graph with virtual edges represents forwarding opportunities over a predictable moving network at a fixed graph depth. Edges between different node copies encode full-package forwarding during an interval; zero-cost edges between copies of the same node encode caching or waiting. The virtual edges preserve routes with different hop counts without changing the graph dimension.

[[li-2026-radio-map-predictive-routing]] weights forwarding edges by the minimum achievable worst-case interference leakage to protected neighboring nodes. Route selection is therefore a bottleneck-path problem, while a separate bisection routine allocates hop timing and power for a fixed route. The paper proves global optimality only for that fixed-route resource subproblem; the alternating route/resource procedure is convergent and empirically near exhaustive search.
