---
type: concept
title: "Anti-UAV Interference Base-Station Deployment"
tags: [anti-uav, jamming, deployment, gnss, potential-game]
related:
  - "[[ma-2026-game-ibs-deployment]]"
  - "[[potential-game]]"
  - "[[uav-localization-under-jamming]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-13
updated: 2026-07-13
---

# Anti-UAV Interference Base-Station Deployment

Anti-UAV interference base-station deployment chooses fixed ground jammer locations to disrupt an unauthorized UAV's navigation and communication while limiting interference to friendly infrastructure. The defender's placement and the UAV's least-disrupted feasible path form opposing spatial decisions.

[[ma-2026-game-ibs-deployment]] models directional IBS jamming against both GNSS and an operator link, with supportive-device performance included in each IBS utility. It presents the placement layer as a [[potential-game]], then evaluates every discretized placement combination by training a [[soft-actor-critic]] UAV path response and selecting the highest-scoring utility-table entry.

This concept reverses the viewpoint of [[uav-localization-under-jamming]] and ordinary anti-jamming control: the optimized network is the jammer, not the protected UAV. The distinction between the claimed game structure and the executed solver matters. Exhaustive placement plus learned path response is exponential in the number of IBS candidates, and an equilibrium-existence argument alone does not establish a unique or globally optimal deployment.
