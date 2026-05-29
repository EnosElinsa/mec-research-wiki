---
type: concept
title: "Edge User Allocation (EUA)"
tags: [edge-computing, resource-allocation, placement, game-theory]
related:
  - "[[he-2019-euagame-user-allocation]]"
  - "[[mobile-edge-computing]]"
  - "[[potential-game]]"
  - "[[matching-theory-for-resource-allocation]]"
created: 2026-05-29
updated: 2026-05-29
---

# Edge User Allocation (EUA)

The problem, framed from an **app vendor's** perspective, of allocating app users to hired edge servers so as to serve the maximum number of users at minimum overall system cost, subject to **proximity** (a user can only attach to a server whose coverage includes it) and **capacity** (multi-dimensional: CPU, memory, storage, bandwidth) constraints.

Finding the centralized optimum is NP-hard — EUA generalizes the variable-size vector bin-packing problem. In [[he-2019-euagame-user-allocation]] it is modeled as **EUAGame**, a [[potential-game]] that admits a [[nash-equilibrium]] and is solved by a decentralized algorithm. EUA is a *placement* problem (which server serves which user) and is distinct from, but closely related to, [[task-offloading]] decisions in [[mobile-edge-computing]].
