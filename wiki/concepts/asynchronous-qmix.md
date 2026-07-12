---
type: concept
title: "Asynchronous-QMIX"
tags: [marl, qmix, asynchronous, semi-markov, ctde, uav]
related:
  - "[[le-2026-asynchronous-uav-data-collection]]"
  - "[[qmix]]"
  - "[[semi-markov-decision-process]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-data-collection]]"
created: 2026-07-12
updated: 2026-07-12
---

# Asynchronous-QMIX

Asynchronous-QMIX (AQMIX) adapts [[qmix]] to cooperative agents whose actions finish at different times. It models global transitions at event-driven [[semi-markov-decision-process|semi-Markov]] epochs, maintains each agent's completion timestamp, and requests a new action only from the earliest-finishing agent while all other actions continue.

[[le-2026-asynchronous-uav-data-collection]] preserves QMIX's monotonic relationship between local utilities and the joint value, using global-state mixing during training and recurrent local policies at execution. In its remote-collection setting, opportunistic inter-UAV map exchange complements rather than replaces decentralized action selection.
