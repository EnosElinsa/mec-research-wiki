---
type: concept
title: "Computation-to-Communication Ratio"
tags: [mec, computation-offloading, energy-efficiency, mobile-cloud-computing]
related:
  - "[[task-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[mobile-edge-computing]]"
  - "[[miettinen-2010-mcc-energy-efficiency]]"
created: 2026-06-02
updated: 2026-06-02
---

# Computation-to-Communication Ratio

The **computation-to-communication ratio** is the foundational quantity that decides whether **offloading a task saves energy** (or time): roughly, the number of CPU cycles a workload needs **per byte** of data that must be transferred to and from the remote server. Offloading pays off only when the cost of moving the data is **smaller** than the cost of computing locally — i.e. when $E_{cloud} < E_{local}$ — which translates into a threshold on this ratio that depends on the device's processing efficiency and the wireless link's energy efficiency.

The practical consequences are that (1) **compute-heavy, data-light** workloads are good offloading candidates while light-weight apps are better run locally; (2) the threshold **shifts with the radio technology** (e.g. WLAN vs cellular give very different crossovers); and (3) not just data **volume** but data **traffic pattern** matters — bursts are cheaper than many small packets.

In the wiki, this is the central analytical lens of [[miettinen-2010-mcc-energy-efficiency]], the corpus's earliest (mobile-cloud-computing) anchor, which measures contemporary handhelds over WLAN and 3G to map the crossover empirically. The same local-vs-offload energy balance is later formalized and optimized in MEC resource-allocation work such as [[you-2017-meco-resource-allocation]] (priority/threshold structure) and underlies the [[energy-latency-tradeoff]] throughout the offloading literature.
