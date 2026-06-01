---
type: concept
title: "Virtual Network Embedding (VNE)"
tags: [virtualization, resource-allocation, nfv, sdn, np-hard]
related:
  - "[[network-function-virtualization]]"
  - "[[network-slicing]]"
  - "[[service-function-chaining]]"
  - "[[space-air-ground-ocean-integrated-network]]"
  - "[[zhang-2024-qos-vne-sagoin]]"
  - "[[zhang-2025-vnf-sgin-dql]]"
created: 2026-06-02
updated: 2026-06-02
---

# Virtual Network Embedding (VNE)

The resource-allocation problem of mapping a **virtual network request (VNR)** — a graph of virtual nodes (with CPU/compute-delay demands) and virtual links (with bandwidth/delay demands) — onto a shared **physical substrate network**, subject to capacity and delay constraints, while maximizing an objective such as long-term revenue, the revenue-to-cost ratio, or the request acceptance rate. VNE is the core mechanism by which [[network-function-virtualization|NFV]] / SDN substrates rent out slices of physical infrastructure; it is NP-hard, and is usually split into **node mapping** (which physical node hosts each virtual node) followed by **link mapping** (which physical path carries each virtual link, e.g. via k-shortest-path).

In non-terrestrial / multi-domain settings the substrate is **heterogeneous and time-varying** (satellites and aerial platforms move, links hand over), and each infrastructure provider exposes only limited information — making cross-domain VNE harder than the well-studied terrestrial case.

## In this wiki

[[zhang-2024-qos-vne-sagoin]] performs **QoS-aware multi-domain VNE** over a three-layer [[space-air-ground-ocean-integrated-network|SAGOI-Net]] substrate: it classifies VNRs by K-means into compute / bandwidth / delay QoS categories, switches the reinforcement-learning agent's reward function per category, maps virtual nodes with a convolutional policy network, and embeds links by k-shortest-path. It is the resource-orchestration sibling of [[zhang-2025-vnf-sgin-dql]] (dynamic VNF selection + [[service-function-chaining|chaining]] via deep Q-learning over a satellite-ground substrate), and connects to [[network-slicing]].
