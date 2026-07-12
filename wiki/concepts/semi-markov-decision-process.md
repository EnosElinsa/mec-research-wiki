---
type: concept
title: "Semi-Markov Decision Process (SMDP)"
tags: [drl, markov, stochastic-control, optimization]
related:
  - "[[pomdp]]"
  - "[[markov-reward-process]]"
  - "[[deep-q-network]]"
  - "[[liu-2020-cooperative-uav-mec-power-iot]]"
  - "[[le-2026-asynchronous-uav-data-collection]]"
  - "[[asynchronous-qmix]]"
created: 2026-05-31
updated: 2026-07-12
---

# Semi-Markov Decision Process (SMDP)

A generalization of a Markov decision process in which the time spent in each state (the **sojourn time**) is a random variable rather than a fixed unit step. SMDPs suit systems where decisions are taken at irregular, event-driven epochs and the inter-decision interval itself is stochastic — making them a natural fit for long-term reward optimization under random arrivals and time-varying channels.

In the wiki, [[liu-2020-cooperative-uav-mec-power-iot]] formulates cooperative UAV-enabled MEC for the power-IoT system as a semi-Markov process to capture random device demands and time-varying channel conditions, then maximizes long-term network utility with centralized and distributed deep-reinforcement-learning algorithms. It complements the [[markov-reward-process]] and [[pomdp]] formulations used elsewhere in the corpus.

[[le-2026-asynchronous-uav-data-collection]] uses the decentralized partially observable form: UAV flight and hover actions have unequal durations, and [[asynchronous-qmix]] advances the global process whenever the next agent finishes rather than forcing fixed synchronized steps.
