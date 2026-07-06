---
type: concept
title: "Backscatter Communication"
tags: [backscatter, wireless-power-transfer, energy-harvesting, mec]
related:
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[mobile-edge-computing]]"
  - "[[he-2024-backscatter-wpmec-cooperation]]"
  - "[[uav-backscatter-identification]]"
  - "[[zeng-2026-fmcw-isibc-lae]]"
created: 2026-06-02
updated: 2026-07-07
---

# Backscatter Communication

**Backscatter communication (BackCom)** is a passive transmission mode in which a device sends data by **modulating and reflecting an incident radio signal** rather than generating its own carrier. Because it skips the power-hungry RF chain, BackCom consumes very little energy and can harvest energy from the ambient signal to run its circuitry — at the cost of a **lower data rate** than active transmission.

In wireless-powered MEC it is contrasted with **active communication (AC)** under the harvest-then-transmit (HTT) protocol: AC first harvests RF energy and then spends it to transmit, achieving a higher rate but consuming more energy. There is therefore an **energy-vs-throughput trade-off** between the two, so designs often **integrate BackCom + AC** and split time/resources between them to maximize computation throughput or [[secure-computation-efficiency|energy efficiency]].

In the wiki, [[he-2024-backscatter-wpmec-cooperation]] integrates BackCom and AC in a **user-cooperation** WPMEC system (source node + helper-relay + HAP-with-MEC), adaptively allocating more time to BackCom when the backscatter link is strong and to AC otherwise, to maximize user energy efficiency. The concept sits alongside [[wireless-power-transfer]] and [[rf-energy-harvesting]] in the corpus's energy-sustainability track.

[[zeng-2026-fmcw-isibc-lae]] uses BackCom for identity rather than MEC data upload: a UAV-mounted backscatter device modulates low-rate symbols onto an FMCW sensing echo so the ground base station can recover both motion parameters and a UAV identifier.
