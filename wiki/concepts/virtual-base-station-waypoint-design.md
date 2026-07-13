---
type: concept
title: "Virtual Base-Station Waypoint Design"
tags: [uav-trajectory, waypoint-design, disk-cover, traveling-salesman, multicast]
related:
  - "[[geometric-disk-cover]]"
  - "[[minimum-connection-time-trajectory]]"
  - "[[lyu-2017-spiral-mbs-placement]]"
  - "[[zeng-2018-uav-multicasting-completion-time]]"
created: 2026-07-14
updated: 2026-07-14
---

# Virtual Base-Station Waypoint Design

A route-construction method that covers ground terminals with a smaller set of virtual base-station disks, orders those disks, and refines where an aerial platform enters and exits each shared coverage region. It replaces terminal-by-terminal visits with waypoints that can serve several receivers simultaneously.

[[zeng-2018-uav-multicasting-completion-time]] uses the spiral [[geometric-disk-cover]] heuristic from [[lyu-2017-spiral-mbs-placement]], an open TSP order, and convex entry/exit optimization over disk intersections.

Convex optimality applies only after clusters and their order are fixed. Disk placement and TSP ordering remain heuristic, so the construction is not a globally optimal waypoint solver.
