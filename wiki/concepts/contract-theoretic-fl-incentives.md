---
type: concept
title: "Contract-Theoretic FL Incentives"
tags: [federated-learning, incentive-mechanism, contract-theory, client-selection]
related:
  - "[[contract-theory]]"
  - "[[federated-learning]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[zhao-2026-uav-fl-inspection-incentives]]"
created: 2026-07-11
updated: 2026-07-11
---

# Contract-Theoretic FL Incentives

An FL client-selection pattern where a model owner uses contract terms to attract self-interested clients, then selects participants by expected contribution, cost, and feasibility rather than inviting every client.

[[zhao-2026-uav-fl-inspection-incentives]] makes the pattern concrete for UAV-assisted intelligent inspection. UAVs have private and heterogeneous data, battery, sensing, computation, and communication conditions. The MDS scheme builds a candidate UAV pool with [[contract-theory]] and residual-battery management, then uses Bayesian optimization to choose participants for each federated-training round. The result is an FL incentive mechanism rather than a pure accuracy-only client selector.
