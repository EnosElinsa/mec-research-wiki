---
type: concept
title: "Service Experience Ratio"
tags: [metrics, fairness, qoe, objective]
related:
  - "[[jains-fairness-index]]"
  - "[[qoe-modeling-mec]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[gao-2024-service-experience-cache-uav]]"
created: 2026-05-29
updated: 2026-05-29
---

# Service Experience Ratio

A composite MEC objective metric defined as **fairness divided by average delay** — specifically [[jains-fairness-index|Jain's fairness index]] over per-UE service delay, divided by the average service delay. Maximizing it pushes the system toward *both* low latency *and* equitable treatment across users, rather than optimizing aggregate latency alone (which can starve some users).

Because it is a ratio, maximizing it is a fractional program, naturally handled by [[fractional-programming-dinkelbach|Dinkelbach's method]]. In the wiki, [[gao-2024-service-experience-cache-uav]] introduces and maximizes this metric, jointly optimizing offloading, caching, trajectory, and resource allocation, and reports a 19–34% higher service experience ratio than baselines. It is a fairness-aware refinement of [[qoe-modeling-mec]].
