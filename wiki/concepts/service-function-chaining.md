---
type: concept
title: "Service Function Chaining (SFC)"
tags: [sfc, nfv, sdn, routing, satellite, vnf-migration]
related:
  - "[[network-function-virtualization]]"
  - "[[network-slicing]]"
  - "[[task-migration]]"
  - "[[deep-q-network]]"
  - "[[zhang-2025-vnf-sgin-dql]]"
  - "[[pham-2026-vnf-control-loop]]"
  - "[[routing-vnf-scaling-control-loop]]"
created: 2026-05-31
updated: 2026-07-13
---

# Service Function Chaining (SFC)

An **SFC** steers a traffic flow through a **predefined ordered sequence of VNFs** (interconnected by virtual links) to deliver a composite end-to-end service. Realizing an SFC requires two coupled decisions: **VNF selection** (map each VNF in the chain to a node hosting that instance) and **virtual-link mapping** (allocate physical transmission resources to interconnect the selected instances) — together a **VNF selection and chaining policy (VSCP)**.

In wired 5G networks, SFC orchestration is usually posed as ILP/MILP with heuristics. In time-varying [[space-air-ground-integrated-network|SGIN/SAGIN]] settings, satellite movement changes the topology, so SFC mappings must be re-determined over time, which triggers costly **[[task-migration|VNF migrations]]** — motivating learning-based, profit-aware re-mapping.

In the wiki, [[zhang-2025-vnf-sgin-dql]] formulates dynamic VNF selection and chaining as an MDP and trains a [[deep-q-network|DQN]] (the DDVSC algorithm) to balance resource provisioning + migration costs against service-performance gain, clustering historical load to build a compact action space of VSCP sets. [[pham-2026-vnf-control-loop]] keeps routing and VNF scaling as separate timescales: distributed routing reacts each slot, while an event-triggered orchestrator changes replicas and placement after persistent SFC infeasibility. Both are built on [[network-function-virtualization]].
