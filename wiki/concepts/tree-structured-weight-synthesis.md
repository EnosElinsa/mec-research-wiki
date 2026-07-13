---
type: concept
title: "Tree-Structured Weight Synthesis"
tags: [distributed-learning, model-aggregation, logistic-regression, disaster-response, uav]
related:
  - "[[v-2026-pb-papp-survivor-detection]]"
  - "[[prediction-based-priority-aware-path-planning]]"
  - "[[federated-learning]]"
created: 2026-07-14
updated: 2026-07-14
---

# Tree-Structured Weight Synthesis

Periodic averaging of logistic-regression coefficients learned by mother drones from their attached surveillance drones. In [[v-2026-pb-papp-survivor-detection]], a ground base station collects the mother-drone weights, computes their mean, and returns the aggregate for the next potential-survivor-location prediction round. The data collection is hierarchical, but aggregation still uses a central authority and behaves more like simple [[federated-learning|federated averaging]] than decentralized peer consensus.
