---
type: concept
title: "Attentive Memory-Integrated Information Exchange"
tags: [multi-agent-reinforcement-learning, attention, memory, communication]
related:
  - "[[zhao-2026-uav-carrier-vcs]]"
  - "[[hidden-state-sharing-marl]]"
  - "[[sequential-multi-agent-policy-generation]]"
  - "[[uav-assisted-mobile-crowd-sensing]]"
  - "[[lstm-interruption-compensation]]"
  - "[[opportunistic-cooperative-multi-uav-ddqn]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-14
updated: 2026-07-14
---

# Attentive Memory-Integrated Information Exchange

A heterogeneous-MARL communication mechanism that attends over link-qualified neighbor representations and already selected actions while carrying persistent per-agent memory across decisions. Sequential action sharing lets later active agents condition on earlier choices, while memory preserves context for agents whose actions last multiple timeslots.

[[zhao-2026-uav-carrier-vcs]] uses this mechanism for UAV scouts and road-bound UGV carriers with unequal action durations. It extends broad [[hidden-state-sharing-marl]] with attention, historical memory, active/inactive vehicle state, and ordered action propagation; it does not provide a formal robustness guarantee under arbitrary message delay or loss.
