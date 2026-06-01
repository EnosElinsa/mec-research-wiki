---
type: concept
title: "Counterfactual Multi-Agent Policy Gradient (COMA)"
tags: [multi-agent-rl, credit-assignment, actor-critic, ctde]
related:
  - "[[centralized-training-decentralized-execution]]"
  - "[[maddpg]]"
  - "[[multi-agent-q-learning]]"
  - "[[zhang-2024-coma-satellite-offloading]]"
created: 2026-06-02
updated: 2026-06-02
---

# Counterfactual Multi-Agent Policy Gradient (COMA)

A multi-agent actor-critic method that solves the **credit-assignment** problem — how to tell each agent's contribution to a shared team reward — by having a **centralized critic** compute a per-agent **counterfactual baseline**: it compares the realized team return against the return that would result if the agent had taken a default action while the others held theirs fixed. Subtracting this baseline isolates each agent's marginal effect, giving a lower-variance policy-gradient signal. COMA fits the [[centralized-training-decentralized-execution|CTDE]] pattern: a centralized critic during training, decentralized actors at execution.

In [[zhang-2024-coma-satellite-offloading]], COMA optimizes collaborative task offloading across autonomous LEO satellites: a centralized critic trained on the terrestrial cloud computes the counterfactual baseline for each satellite agent (with parameter sharing to cut complexity), while the learned actor — redesigned with an attention-based bidirectional LSTM to capture the periodic LEO topology — executes onboard from local observations.

Sits alongside the corpus's other CTDE multi-agent backbones such as [[maddpg]].
