---
type: concept
title: "Virtual Machine Multiplexing"
tags: [mec, virtualization, parallel-computing, edge-server]
related:
  - "[[parallel-vs-serial-processing]]"
  - "[[mobile-edge-computing]]"
  - "[[liu-2022-maritime-uav-mec-virtualization]]"
created: 2026-05-31
updated: 2026-05-31
---

# Virtual Machine Multiplexing

A basic enabling technology for MEC in which a single physical machine hosts **multiple virtual machines (VMs)**, each configured with a share of hardware resources (CPU, memory, I/O bus), so an edge server can run several computing tasks in parallel. The catch is **I/O interference**: sharing one physical machine slows each VM, often modeled by a degradation factor D > 0 that captures the percentage increase in expected service time when a VM is multiplexed with others.

In the wiki, [[liu-2022-maritime-uav-mec-virtualization]] places the MEC server on a top-UAV and optimizes the **number of VMs** participating in parallel computing jointly with the UAV trajectory, explicitly handling the realistic case of tasks with **different** data sizes across VMs (most prior work assumed equal-sized tasks) under I/O interference. It connects to [[parallel-vs-serial-processing]] as the mechanism by which parallel edge computation is realized.
