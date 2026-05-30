---
type: concept
title: "Network Function Virtualization (NFV)"
tags: [nfv, sdn, virtualization, architecture, satellite, 6g]
related:
  - "[[service-function-chaining]]"
  - "[[network-slicing]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[zhang-2025-vnf-sgin-dql]]"
created: 2026-05-31
updated: 2026-05-31
---

# Network Function Virtualization (NFV)

Decoupling network functions (e.g. intrusion detection, network address translation) from dedicated function-specific middleboxes and running them as **virtual network functions (VNFs)** on generic commodity servers. Paired with **software-defined networking (SDN)** — which separates the control plane from the data plane for centralized control (e.g. via OpenFlow) — NFV lets operators instantiate, scale, and migrate functions flexibly across heterogeneous nodes.

NFV is the substrate for [[service-function-chaining]] (ordering VNFs into an end-to-end chain) and is closely related to [[network-slicing]] (carving rentable virtual resource slices). In integrated satellite-ground / [[space-air-ground-integrated-network|SAGIN]] settings, VNFs may run on satellites (global coverage, scarce compute) or ground nodes (rich compute, limited coverage), and satellite movement forces **VNF migration** decisions over time.

In the wiki, [[zhang-2025-vnf-sgin-dql]] builds an SDN/NFV-based 6G satellite-ground integrated network and learns dynamic VNF selection + chaining policies via deep Q-learning to maximize long-term network profit.
