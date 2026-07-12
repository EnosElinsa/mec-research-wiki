---
type: concept
title: "Target Level of Safety"
tags: [safety, risk, uav, trajectory-planning, low-altitude-economy]
related:
  - "[[jiang-2026-bi-level-uav-delivery-safety]]"
  - "[[compliance-aware-uav-trajectory]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[safe-reinforcement-learning]]"
  - "[[explicit-constraints-beat-reward-shaping-in-mec-drl]]"
created: 2026-07-11
updated: 2026-07-11
---

# Target Level of Safety

Target level of safety (TLS) is a hard risk threshold for UAV operation. Instead of adding risk as one weighted term in an objective, TLS requires every accepted path segment or waypoint to remain below a preset acceptable risk value.

In [[jiang-2026-bi-level-uav-delivery-safety]], TLS appears as the lower-level trajectory constraint `R(X_k) <= R_TLS`. The RG-FMT* planner is evaluated by TLS compliance rate, not only by total path risk, because minimizing global risk can still leave locally unsafe segments.

Within this wiki, TLS is the explicit-threshold counterpart to broader [[compliance-aware-uav-trajectory]] planning. It also illustrates the thesis behind [[explicit-constraints-beat-reward-shaping-in-mec-drl]]: safety-critical constraints should often remain constraints rather than becoming soft reward terms.
