---
type: concept
title: "Hidden-State Sharing in MARL"
tags: [marl, agent-communication, representation-sharing, cooperation]
related:
  - "[[kim-2026-scale-reconfigurable-marl]]"
  - "[[scale-reconfigurable-marl]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[ma-pomdp]]"
  - "[[non-terrestrial-network]]"
created: 2026-07-14
updated: 2026-07-14
---

# Hidden-State Sharing in MARL

Hidden-state sharing in MARL lets agents exchange intermediate neural representations rather than raw observations or final actions. Layerwise aggregation can provide each policy with a compact summary of peer state before the next transformation, supporting coordinated decisions under partial observation.

[[kim-2026-scale-reconfigurable-marl]] averages other ground stations' hidden variables, concatenates that communication vector with each station's own representation, and continues the actor/critic computation. The no-communication ablation supports this mechanism only within the reported simulation; bandwidth, latency, packet loss, privacy, synchronization, and scaling with agent count are not modeled, so it should not be read as communication-free [[centralized-training-decentralized-execution|CTDE]].
