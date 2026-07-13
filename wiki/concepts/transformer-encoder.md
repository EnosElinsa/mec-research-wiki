---
type: concept
title: "Transformer Encoder"
tags: [deep-learning, attention, encoder, trajectory-planning]
related:
  - "[[yao-2026-transformer-mean-field-isac-sagin]]"
  - "[[guo-2026-aot-uav-inspection-offloading]]"
  - "[[graph-neural-network]]"
  - "[[probsparse-self-attention-prediction]]"
  - "[[knowledge-distillation-for-drl]]"
created: 2026-07-07
updated: 2026-07-13
---

# Transformer Encoder

A stack of self-attention and feed-forward blocks that maps an input sequence into contextual token representations without an autoregressive decoder. In wireless/MEC optimization, encoder-only Transformers are attractive when the input is a set or sequence of locations, tasks, users, channels, or demands and the downstream decision can be handled by a smaller output head.

In [[guo-2026-aot-uav-inspection-offloading]], the AGI-oriented Transformer uses one shared encoder for two different inputs: sensor-cluster locations for [[uav-trajectory-control]] and task features for [[task-offloading]]. The encoded representation is sent to task-specific MLP heads, keeping the model lighter than separate full encoder-decoder Transformers for each decision problem.

This is related to the broader attention/graph-learning family in the corpus: [[probsparse-self-attention-prediction]] uses sparse attention for traffic prediction, while [[graph-neural-network]] pages capture relational encoders when the natural structure is a graph rather than a sequence.
