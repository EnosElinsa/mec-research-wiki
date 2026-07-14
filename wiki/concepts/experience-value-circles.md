---
type: concept
title: "Experience Value Circles"
tags: [uav-swarm, cooperative-learning, communication-cost, experience-sharing]
related:
  - "[[qi-2026-ocma-ddqn-data-collection]]"
  - "[[opportunistic-cooperative-multi-uav-ddqn]]"
  - "[[lstm-interruption-compensation]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Experience Value Circles

Experience value circles assign distance-dependent utility to exchanging UAV observations and replay experience. Very close agents tend to have redundant local views, whereas very distant agents incur communication cost and may contribute less relevant state; sharing is favored in an intermediate distance band.

In [[qi-2026-ocma-ddqn-data-collection]], two distance thresholds parameterize this probability/cost rule inside opportunistic cooperation. The thresholds are tuned through simulation and do not constitute a channel-capacity or information-value optimum.
