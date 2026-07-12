---
type: concept
title: "Routing-VNF Scaling Control Loop"
tags: [nfv, service-function-chaining, routing, scaling, two-timescale-control, emergency-network]
related:
  - "[[pham-2026-vnf-control-loop]]"
  - "[[network-function-virtualization]]"
  - "[[service-function-chaining]]"
  - "[[maddpg]]"
  - "[[block-successive-upper-bound-minimization]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[post-disaster-mec]]"
created: 2026-07-13
updated: 2026-07-13
---

# Routing-VNF Scaling Control Loop

A routing-VNF scaling control loop connects a fast traffic-steering layer to a slower [[network-function-virtualization|VNF]] placement and replication layer. Routing exposes persistent congestion, delay, or feasibility failures; scaling changes the available function instances and link loads; the revised infrastructure then becomes the next routing environment.

[[pham-2026-vnf-control-loop]] applies this feedback in a UAV-aided emergency network. Distributed MADDPG actors update multipath [[service-function-chaining|SFC]] rates every slot, while a centralized [[block-successive-upper-bound-minimization|BSUM]] orchestrator is triggered only after sustained infeasibility. The simulation records many more routing decisions than scaling events, making the timescale separation explicit.

The architecture is broader than either solver. MADDPG supplies CTDE routing in this source and BSUM supplies relaxed placement optimization, but another implementation could preserve the same event-triggered feedback with different local and global controllers.
