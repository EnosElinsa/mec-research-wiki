---
type: concept
title: Event-Driven vs Slot-Driven Offloading
tags: [task-offloading, design-choice, scheduling]
related:
  - "[[task-offloading]]"
  - "[[hao-2025-priority-aware-task-driven-co]]"
created: 2026-05-28
updated: 2026-05-28
---

# Event-Driven vs Slot-Driven Offloading

Two timing disciplines for offloading decisions:

| Aspect | Slot-Driven | Event-Driven (Task-Driven) |
|---|---|---|
| Decision trigger | Fixed time slot boundary | Task arrival |
| Per-decision latency | ≥ slot interval (10–100 ms) | Near-zero waiting |
| Implementation cost | Low (one decision per slot) | Higher (decision per arrival) |
| Channel-state coupling | Slots align with coherence time | Decoupled — needs implicit channel modeling |
| Common in | Most published MEC literature | Recently growing, e.g. [[hao-2025-priority-aware-task-driven-co]] |

## Why event-driven helps

In dense / bursty IoT scenarios, the slot-driven discipline forces a queueing delay equal to half the slot interval on average. For 100 ms slots, that's a permanent 50 ms penalty on every task — well beyond what's tolerable for ADAS, control, or AR/VR workloads.

Event-driven removes this penalty by acting at task arrival. The cost is more frequent decisions and a tighter coupling to the agent's inference latency.

## Implementation considerations

- **Stateful inference.** Each event must be served quickly, so the policy network needs to be small or distilled.
- **Channel model.** Without slot synchronization, channel state must be tracked continuously, e.g., via a lightweight Kalman or moving-average filter.
- **Concurrency.** Multiple near-simultaneous arrivals need a deterministic tiebreak rule.

## In this wiki

[[hao-2025-priority-aware-task-driven-co]] is the first source in the corpus making this design choice explicit. Most other curated sources use the slot-driven default.
