---
type: concept
title: "Fault-Tolerant Relay Network"
tags: [communication, reliability, multi-hop, uav-relay]
related:
  - "[[uav-trajectory-control]]"
  - "[[maritime-mec]]"
  - "[[task-redundancy-for-reliability]]"
  - "[[lei-2024-hvmappo-maritime-sar]]"
created: 2026-06-01
updated: 2026-06-01
---

# Fault-Tolerant Relay Network

A multi-hop relay topology engineered with **path redundancy** so that communication survives the temporary failure of individual relay nodes or links. Fault tolerance is quantified as the ratio of currently-available relay paths to the number of possible paths, averaged over the source nodes — higher redundancy means a node disconnection is less likely to cut a source off from the destination.

This redundancy directly tensions against coverage: in UAV relay swarms, spreading nodes out to cover more area lengthens or breaks relay paths, lowering fault tolerance. In this wiki, [[lei-2024-hvmappo-maritime-sar]] makes relay-network fault tolerance a co-equal optimization objective (alongside time and energy) for heterogeneous maritime-SAR vehicles, trading it against mission immediacy via a learned multi-agent policy. Related in spirit to [[task-redundancy-for-reliability]] (redundant *computation* for reliability).
