---
type: concept
title: CSRA (Cold Start Reputation Aggregation)
tags: [federated-learning, reputation, security]
related:
  - "[[federated-reinforcement-learning]]"
  - "[[fl-poisoning-attacks]]"
  - "[[ccvm-correction-voting]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-05-28
updated: 2026-05-28
---

# CSRA (Cold Start Reputation Aggregation)

A reputation-weighting scheme introduced in [[mao-2025-bcsa-frl]] for FL aggregation under poisoning threats. Two-phase reaction:

1. **Cold drop.** When an attack is detected on a participant, its aggregation weight is *sharply* knocked down, not smoothly reduced.
2. **Slow recovery.** The weight then ramps back up over a window matched to the participant's replay-buffer cleaning rate.

## Why "cold start"

The name nods to the cold-start problem in recommendation systems: a recovering satellite is essentially starting fresh — its recent gradient updates can't yet be trusted because its experience stream is still partially poisoned. Even if its current sub-model passes verification *now*, contributions from the next few rounds remain risky until the buffer flushes the bad transitions.

A naive smoothly-decaying reputation lets a "just-recovered" satellite contribute too much, dragging the global model. A binary in/out gate is too aggressive — it never lets the satellite re-enter at full strength even after full recovery. CSRA's hard drop + slow recovery splits the difference.

## Threat addressed

- [[fl-poisoning-attacks|Replay buffer poisoning]] — the satellite is honest but its experience is contaminated.
- [[fl-poisoning-attacks|Model parameter poisoning]] — active corruption of uploaded weights.

## Composition with [[ccvm-correction-voting|CCVM]]

CSRA operates at the *aggregation* layer (model weights). CCVM operates at the *consensus* layer (vote weights). The combination defends both surfaces — see [[mao-2025-bcsa-frl]].
