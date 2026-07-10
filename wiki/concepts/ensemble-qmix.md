---
type: concept
title: "Ensemble QMIX (E-QMIX)"
tags: [marl, qmix, value-decomposition, ensemble, uav-swarm]
related:
  - "[[centralized-training-decentralized-execution]]"
  - "[[value-decomposition-network]]"
  - "[[multi-agent-q-learning]]"
  - "[[zhang-2026-ensemble-marl-uav-target-search]]"
created: 2026-07-11
updated: 2026-07-11
---

# Ensemble QMIX (E-QMIX)

A value-decomposition MARL pattern: train multiple QMIX networks independently, then let each agent choose its decentralized action by majority vote across the networks' greedy action suggestions.

[[zhang-2026-ensemble-marl-uav-target-search]] applies E-QMIX to heterogeneous UAV-swarm target search. QMIX supplies the [[centralized-training-decentralized-execution|CTDE]] value-decomposition backbone, while the ensemble vote suppresses isolated bad action estimates. The paper proves an accuracy-amplification condition: if each network selects the optimal action with probability greater than 0.5 and the ensemble has at least three networks, majority voting increases the probability of selecting the optimal action.

The tradeoff is overhead and recurrent-state consistency. E-QMIX trains and evaluates multiple DRQNs, and the parse notes that very large ensembles can degrade when the majority-voted action diverges from individual recurrent hidden-state histories.
