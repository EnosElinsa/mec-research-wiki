---
type: concept
title: "UAV-Enabled Computing Power Network"
tags: [computing-power-network, uav, stochastic-geometry, task-offloading, low-altitude-economy]
related:
  - "[[deng-2026-uav-cpn-energy]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[task-offloading]]"
  - "[[uav-mobile-relaying]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[hu-2026-segmented-irs-cpn]]"
created: 2026-07-07
updated: 2026-07-13
---

# UAV-Enabled Computing Power Network

A UAV-enabled Computing Power Network uses UAV communications to connect demand with a wider pool of computing capacity, mitigating the MEC "island effect" where nearby compute is insufficient while farther compute remains available. In [[deng-2026-uav-cpn-energy]], one UAV relays requests to Poisson-distributed computing nodes and task-completion probability depends on communication/computation latency plus UAV energy. [[hu-2026-segmented-irs-cpn]] uses several UAV compute servers instead and jointly allocates trajectories, user association, computing capacity, and dynamically partitioned IRS rows under a delay-energy objective.

The family spans relay-backed and UAV-hosted designs. [[deng-2026-uav-cpn-energy]] is close to [[uav-mobile-relaying]] because a UAV forwards tasks to remote ground computing nodes; [[hu-2026-segmented-irs-cpn]] instead executes fully offloaded tasks on the UAV servers themselves. The [[stochastic-geometry-network-analysis]] connection applies to the Deng variant before per-task scheduling or DRL control enters.
