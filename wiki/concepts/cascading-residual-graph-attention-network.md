---
type: concept
title: "Cascading Residual Graph Attention Network"
tags: [graph-neural-network, graph-attention, neural-optimization, deployment, power-control]
related:
  - "[[lu-2026-multiuav-iscpt]]"
  - "[[graph-neural-network]]"
  - "[[graph-based-resource-management]]"
  - "[[integrated-sensing-communication-power-transfer]]"
created: 2026-07-13
updated: 2026-07-13
---

# Cascading Residual Graph Attention Network

A cascading residual graph attention network (CRGAT) solves coupled decisions in sequence while passing a learned representation of the first decision into the second graph stage. Residual projections stabilize the multi-head attention blocks; graph readout maps variable-cardinality node sets to fixed-size controls.

In [[lu-2026-multiuav-iscpt]], user type and coordinates are node features and pairwise distance is an edge feature. The first stage predicts UAV deployment; its encoded output augments every user node before the second stage predicts transmit powers. The model is trained directly against physical metrics, not an RL reward.
