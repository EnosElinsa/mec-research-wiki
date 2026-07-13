---
type: concept
title: "Deep Echo-State-Network Reinforcement Learning"
tags: [reinforcement-learning, echo-state-network, reservoir-computing, recurrent-neural-network, distributed-control]
related:
  - "[[challita-2019-cellular-uav-interference-drl]]"
  - "[[cellular-connected-uav]]"
  - "[[nash-equilibrium]]"
created: 2026-07-13
updated: 2026-07-13
---

# Deep Echo-State-Network Reinforcement Learning

Deep echo-state-network reinforcement learning uses stacked recurrent reservoirs as a fixed temporal feature extractor and trains mainly the output weights that estimate action values or utilities. Reservoir state gives the controller memory of past observations/actions without backpropagating through every recurrent connection, although stability and convergence still depend on reservoir and learning hyperparameters.

In [[challita-2019-cellular-uav-interference-drl]], each cellular UAV uses a deep ESN to estimate the utility of joint movement, cell-association, and power actions in a dynamic noncooperative game. UAVs broadcast actions during training so reservoir state can track other players; the resulting subgame-perfect-equilibrium claim is conditional on the learning algorithm converging.
