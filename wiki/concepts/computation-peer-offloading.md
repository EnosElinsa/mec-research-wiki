---
type: concept
title: "Computation Peer Offloading"
tags: [task-offloading, edge-computing, load-balancing, satellite]
related:
  - "[[task-offloading]]"
  - "[[load-balancing-uav-mec]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[lyapunov-optimization]]"
  - "[[zhang-2024-mhspo-satellite-peer-offloading]]"
created: 2026-06-02
updated: 2026-06-02
---

# Computation Peer Offloading

**Horizontal**, edge-to-edge offloading: instead of an edge node processing every task it admits, it forwards some tasks **sideways to peer edge nodes** that have spare compute. This contrasts with the **vertical** user→edge (or edge→cloud) offloading that the [[task-offloading]] concept usually describes — here both the sender and the receiver are peer servers at the same tier.

The motivation is **load balancing**: when the offered workload is uneven across nodes (some overloaded, others idle), peer offloading redistributes it so limited aggregate compute is used efficiently. The cost is the **transmission overhead** of moving a task to a peer, so peer-offloading designs jointly optimize communication and computation rather than computation alone.

In the wiki, [[zhang-2024-mhspo-satellite-peer-offloading]] applies this pattern to a [[leo-satellite-edge-computing|LEO satellite-edge]] constellation: an access satellite offloads tasks along **multi-hop inter-satellite-link paths** to peer satellites several hops away, because traffic varies with geography and time zone (dense over populated regions, sparse elsewhere). It minimizes a weighted delay + energy objective under backlog stability via [[lyapunov-optimization]] and a per-satellite distributed decomposition. The same horizontal load-spreading idea appears in terrestrial [[small-cell-mec]] and multi-UAV [[load-balancing-uav-mec]] settings, but satellite peer offloading is distinguished by its time-varying topology and tight per-node power budgets.
