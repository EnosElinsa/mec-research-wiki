---
type: concept
title: "Differentiated UAV Service Market"
tags: [uav-services, market, pricing, differentiated-services, nash-equilibrium]
related:
  - "[[wang-2023-differentiated-uav-services]]"
  - "[[ning-2023-madrl-uav-trajectory-differentiated-services]]"
  - "[[nash-equilibrium]]"
  - "[[stochastic-game]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[fairness-metrics-in-mec]]"
created: 2026-07-13
updated: 2026-07-13
---

# Differentiated UAV Service Market

A differentiated UAV service market has multiple owners offering substitutable aerial services with different capabilities, prices, and operating costs. Users divide demand according to preferences and budgets, while each owner chooses service quantity or fleet size to maximize profit under competition.

[[wang-2023-differentiated-uav-services]] instantiates the market over geographic hotspots. Constant-elasticity utility models substitution among owners; a full-information game defines equilibrium quantities and prices; and a [[multi-agent-imitation-learning]] policy adjusts UAV counts when demand and competitor policies are unknown.

[[ning-2023-madrl-uav-trajectory-differentiated-services]] keeps the multiple-owner/differentiated-service setting but shifts the control variable from service quantity and fleet deployment to free-space UAV trajectories under probabilistic user preferences. The two sources therefore separate market provisioning from mobility control.
