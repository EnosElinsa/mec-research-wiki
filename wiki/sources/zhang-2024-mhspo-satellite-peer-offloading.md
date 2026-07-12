---
type: source
title: "Energy-Efficient Computation Peer Offloading in Satellite Edge Computing Networks"
authors: ["Xinyuan Zhang", "Jiang Liu", "Ran Zhang", "Yudong Huang", "Jincheng Tong", "Ning Xin", "Liang Liu", "Zehui Xiong"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3269801"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, leo-satellite-edge-computing, computation-peer-offloading, lyapunov-optimization, load-balancing-uav-mec, free-space-optical-isl, non-terrestrial-network]
related:
  - "[[computation-peer-offloading]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[lyapunov-optimization]]"
  - "[[free-space-optical-isl]]"
  - "[[walker-star-constellation]]"
  - "[[load-balancing-uav-mec]]"
  - "[[task-offloading]]"
  - "[[non-terrestrial-network]]"
  - "[[cheng-2025-dos-satellite-edge-computing]]"
  - "[[zhang-2024-coma-satellite-offloading]]"
  - "[[han-2024-ground-satellite-fl]]"
  - "[[mao-2024-fso-leo-hierarchical-routing]]"
  - "[[zehui-xiong]]"
created: 2026-06-02
updated: 2026-07-13
---

# Energy-Efficient Computation Peer Offloading in Satellite Edge Computing Networks

## Citation

Zhang, X., Liu, J., Zhang, R., Huang, Y., Tong, J., Xin, N., Liu, L., & Xiong, Z. (2024). *Energy-Efficient Computation Peer Offloading in Satellite Edge Computing Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3269801. (Manuscript received 2 September 2022; revised 3 February 2023; accepted 18 April 2023; date of publication 25 April 2023; date of current version 6 March 2024 → year 2024.)

## TL;DR

A **multi-hop computation peer-offloading** scheme for **MEC-enabled LEO satellite networks**: rather than each satellite processing all the tasks within its line of sight (which overloads satellites over dense regions and wastes resources over sparse ones), an access satellite offloads tasks **horizontally to peer satellites several ISL hops away**. The **Multi-Hop Satellite Peer Offloading (MHSPO)** problem jointly minimizes weighted **delay + energy consumption** under resource and backlog constraints. Because future task arrivals are unknown and the topology is time-varying, the long-term problem is converted via the **Lyapunov** drift-plus-penalty framework into per-slot optimization, and a **delayed online learning** method predicts per-task processing delay/energy (with a provably upper-bounded prediction loss). A **gap-preserving reduction** decomposes the network-wide per-slot problem into per-satellite subproblems, giving a practical **online distributed** algorithm proven to be close-to-optimal.

## Problem framing

Satellite networks increasingly do in-orbit computing, but most prior schemes assume **single-satellite** computation — users offload only to a line-of-sight satellite that processes everything itself, creating uneven workloads (overload over populated areas, idle resources over sparse ones). Terrestrial cooperative-offloading methods do not transfer: satellite networks have distinct channels, high-speed-motion mobility, and more variable/uneven global workloads. Peer offloading among satellites is hard because (1) traffic varies with geography and time zone so limited compute must be jointly leveraged; (2) satellite power is restricted (solar panels not always sunlit, finite battery cycle life), so continuous overwork of one satellite must be avoided; (3) offloading to lighter-loaded satellites multiple hops away cuts computation delay only at the expense of transmission overhead, requiring joint communication + computation optimization.

## System model

- **Constellation.** A **Walker constellation** of N satellites over P orbital planes (S per plane, phasing factor F); a time-varying topology graph $\mathcal{G}=(V,E)$ where each satellite is an MEC node with neighbor set $N_n$.
- **Offloading.** Network-side scheduling: the access satellite admits tasks and offloads them along **multi-hop ISL paths** to cooperative satellites; users are unaware of the offloading schedule and can be served by satellites out of sight. Per-task per-slot decisions are local-computing indicator $\alpha_n^i(t)$ and node-to-neighbor offloading decision $\beta_{nm}^i(t)$.
- **Queues / links.** Per-satellite arrival, forwarding, and computing queues; **laser (FSO) ISLs** as the inter-satellite links (high bandwidth, unlicensed, smaller antennas, better security; subject to Doppler, acquisition/tracking, background radiation). Result-return transmission to ground is neglected (small output).
- **Objective.** Minimize the long-term weighted sum of system delay ($\rho_d$) and energy consumption ($\rho_e$) subject to backlog stability and scheduling/offloading-capacity constraints ($E_n$ per-slot dispatch cap, link rate cap $B_{nm}$).

## Method

- **Lyapunov transformation.** The long-term MHSPO objective is recast by drift-plus-penalty into a per-slot optimization; the weight V trades queue stability against system overhead.
- **Delayed online learning.** Because future workloads (and hence per-task processing delay/energy) are unknown, a prediction policy estimates them per slot; the prediction loss is proven to be upper-bounded.
- **Gap-preserving decomposition.** The network-wide per-slot cost minimization is reduced to several per-satellite subproblems, yielding an **online distributed** decision scheme with analyzed close-to-optimal performance.

## Key findings

- Extensive simulations show that **multi-hop peer offloading among satellites** improves edge-computing performance efficiently and **significantly outperforms baseline solutions** in system delay/energy (the paper's stated results; specific margins are figure-derived, so treat exact values as indicative).
- The online distributed algorithm is proven to achieve **close-to-optimal** performance with a bounded online-learning prediction loss.

## Limitations / future work

Simulation-based over a Walker constellation; result-return transmission ignored; relies on FSO-ISL availability and the per-slot decomposition. Explicit future-work targets beyond the multi-hop peer-offloading framework are `not in parse`.

## Relation to the corpus

A **LEO satellite-edge-computing** entry that introduces the corpus's [[computation-peer-offloading]] (horizontal edge-to-edge) pattern and the **load-balancing** motivation across a constellation, distinct from the vertical user→satellite offloading of [[cheng-2025-dos-satellite-edge-computing]] and the agent-per-satellite scheme of [[zhang-2024-coma-satellite-offloading]]. It shares the **Lyapunov online** machinery of [[cheng-2025-dos-satellite-edge-computing]], the **FSO-ISL** substrate of [[mao-2024-fso-leo-hierarchical-routing]] and [[han-2024-ground-satellite-fl]], and the energy-constrained-satellite framing common to the SAGIN/satellite track.

## Raw artifacts

- `raw/sources/Energy-Efficient_Computation_Peer_Offloading_in_Satellite_Edge_Computing_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
