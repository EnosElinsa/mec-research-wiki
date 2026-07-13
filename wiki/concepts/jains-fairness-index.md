---
type: concept
title: "Jain's Fairness Index"
tags: [metrics, fairness, qoe]
related:
  - "[[xie-2026-uav-irs-eppo]]"
  - "[[theil-fairness-index]]"
  - "[[spatial-equity-index]]"
  - "[[service-experience-ratio]]"
  - "[[qoe-modeling-mec]]"
  - "[[gao-2024-service-experience-cache-uav]]"
  - "[[wang-2026-llm-qos-multiuav-resource]]"
  - "[[wang-2026-wutf-fair-communication]]"
  - "[[wireless-powered-uav-fair-service-control]]"
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[decentralized-active-ris-uav-noma-control]]"
  - "[[qin-2023-symmetry-augmented-uav-isac]]"
  - "[[liu-2020-distributed-uav-coverage-navigation]]"
  - "[[liu-2021-edivert-mobile-crowdsensing]]"
  - "[[he-2026-memdrl-uav-navigation]]"
  - "[[zhang-2022-solar-charging-uav-iot]]"
  - "[[chen-2026-hammurabi-cooperation]]"
  - "[[betalo-2026-meta-uav-scheduling]]"
  - "[[su-2026-three-tier-uav-capacity]]"
  - "[[ye-2023-graph-uav-coverage]]"
created: 2026-05-29
updated: 2026-07-13
---

# Jain's Fairness Index

A widely used fairness metric over a vector of per-user allocations $x_1,\dots,x_n$:

$$ J(x) = \frac{\left(\sum_i x_i\right)^2}{n \sum_i x_i^2} \in [1/n, 1] $$

It equals 1 when all users receive identical allocation (perfectly fair) and drops toward $1/n$ as the allocation concentrates on a few users. It is scale-independent and population-size-independent.

[[betalo-2026-meta-uav-scheduling]] uses Jain-index deviation to shape per-UAV sensor-service rewards. [[su-2026-three-tier-uav-capacity]] uses Jain's index to compare throughput-maximizing and satisfaction-maximizing multihop relay allocations.

In the wiki, [[gao-2024-service-experience-cache-uav]] applies Jain's index to per-UE average **service delay** and divides it by the average delay to form the [[service-experience-ratio]] — coupling fairness with latency in one [[qoe-modeling-mec]] objective. [[wang-2026-llm-qos-multiuav-resource]] uses Jain-style fairness inside a weighted delay-fairness objective for multi-UAV cooperative edge computing. It complements the corpus's other fairness measures, [[theil-fairness-index]] and [[spatial-equity-index]].

[[wang-2026-wutf-fair-communication]] applies the index to accumulated per-user throughput inside both its formal throughput-fairness-energy objective and learned reward. [[morshed-2026-active-ris-uav-noma-mappo]] instead includes Jain fairness in a shared MAPPO reward for active-RIS UAV-NOMA control alongside rate, energy efficiency, and outage.

[[he-2026-memdrl-uav-navigation]] applies the index to cumulative PoI visit counts, so geographically neglected sensing locations lower the same fairness score even when total collected data is high.

[[zhang-2022-solar-charging-uav-iot]] applies the index to cumulative per-terminal service counts inside a reward that also accounts for transmitted data, net energy, and battery depletion.

[[chen-2026-hammurabi-cooperation]] applies Jain fairness to cumulative PoI coverage in a multi-UAV area-coverage task. Its inequality-aversion policy improves fairness over several baselines but remains below the more cooperative F-First demonstrations, showing that better coverage/energy efficiency need not dominate every fairness comparator.
