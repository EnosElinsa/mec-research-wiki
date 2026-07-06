---
type: source
title: "Coded Caching Enabled D2D Content Delivery in UAV-Assisted Marine Edge Networks"
authors: ["Zhaoxiang Huang", "Zhiwen Yu", "Liang Wang", "Huan Zhou", "Fei Xiong", "Bin Guo"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3708365"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, maritime-mec, coded-caching, device-to-device-communication, uav-trajectory-control, lyapunov-optimization, content-delivery, resource-allocation]
related:
  - "[[maritime-mec]]"
  - "[[coded-caching]]"
  - "[[device-to-device-communication]]"
  - "[[service-caching-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[dai-2023-hybrid-marine-mmwl]]"
  - "[[dai-2023-hybrid-noma-fdma-marine]]"
  - "[[qian-2022-uav-maritime-iot-noma]]"
created: 2026-07-06
updated: 2026-07-06
---

# Coded Caching Enabled D2D Content Delivery in UAV-Assisted Marine Edge Networks

## Citation

Huang, Z., Yu, Z., Wang, L., Zhou, H., Xiong, F., & Guo, B. (2026). *Coded Caching Enabled D2D Content Delivery in UAV-Assisted Marine Edge Networks*. **IEEE Transactions on Mobile Computing**, 1-16. DOI: 10.1109/TMC.2026.3708365.

## TL;DR

Introduces OJC3D, an online joint coded-caching and content-delivery algorithm for UAV-assisted marine edge networks. A UAV carries complete files, buoys bridge RF and underwater acoustic links, and AUVs cache MDS-coded chunks so nearby AUVs can serve requests through underwater D2D links. Lyapunov optimization handles the long-term UAV energy budget, while per-slot convex subproblems optimize UAV trajectory, caching placement, and request decisions.

## Problem framing

Marine content delivery differs from terrestrial caching because shore networks have limited coverage, satellite links can be too latent for real-time access, and underwater acoustic links are bandwidth-limited and intermittent. If a UAV simply sends full files through buoys to every AUV request, the RF/acoustic dual-hop path and buoy transcoding become bottlenecks. Coded caching addresses that bottleneck by spreading coded content blocks across AUVs and exploiting D2D delivery when acoustic neighbors are available.

The paper formulates a future-dependent NP-hard long-term optimization problem: minimize content request latency under a long-term UAV energy constraint while jointly choosing UAV trajectory, AUV caching, and request-source decisions.

## System model

- A rotary-wing UAV communicates with surface buoys through RF links.
- Buoys act as gateways and transcoders between the UAV and underwater acoustic channels.
- AUVs can request content, cache coded chunks, and serve neighboring AUVs through D2D underwater acoustic communication.
- A content library is encoded with an $(n,k)$ MDS code; each AUV can cache at most one chunk per file, while the UAV caches full files.
- AUV mobility follows a Gauss-Markov model; UAV, buoy, and AUV connectivity is represented through coverage, connectivity, and adjacency indicators.

## Method

- Converts the long-term energy-constrained problem into per-slot decisions using a virtual energy queue and Lyapunov drift-plus-penalty.
- Splits each per-slot problem into three stages: UAV trajectory planning, content caching placement, and content request scheduling.
- Uses convex-optimization-based transformations inside the stages to make the online decisions tractable.
- Coordinates coded caching with D2D retrieval so requests can be served by a sufficient set of coded chunks rather than by one full-file transfer.

## Key findings

- The abstract reports that OJC3D reduces content access latency by up to 20% and UAV energy consumption by 35% compared with benchmark schemes.
- The paper reports near-optimal delay performance while maintaining low energy consumption.
- Its ablation framing attributes the gain to jointly considering D2D coded delivery, UAV trajectory planning, and online resource allocation rather than optimizing those components in isolation.
- The coded-D2D design is specifically useful under intermittent underwater connectivity, where full-file transfer over a single acoustic link may be infeasible.

## Limitations / future work

The evaluation is simulation-based and depends on modeled AUV mobility, acoustic/RF channels, content popularity, and convex subproblem structure. The parse does not state a separate future-work section beyond the scoped marine content-delivery formulation.

## Relation to the corpus

This is a marine edge-network entry adjacent to [[maritime-mec]]: it is about content delivery rather than computation offloading, but it uses the same UAV/buoy/AUV ocean setting and the same scarcity of offshore infrastructure. It extends the wiki's caching vocabulary from [[service-caching-mec]] and [[computational-task-caching]] to [[coded-caching]], and links that caching layer to [[device-to-device-communication]] under underwater acoustic constraints. The Lyapunov queue for UAV energy also reinforces [[lyapunov-optimization]] as an online-control pattern beyond compute offloading.

## Raw artifacts

- `raw/sources/Coded Caching Enabled D2D Content Delivery in UAV-Assisted Marine Edge Networks/Coded Caching Enabled D2D Content Delivery in UAV-Assisted Marine Edge Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
