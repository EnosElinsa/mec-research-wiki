---
type: source
title: "Efficient Live Migration of Edge Services Leveraging Container Layered Storage"
authors: ["Lele Ma", "Shanhe Yi", "Nancy Carter", "Qun Li"]
year: 2019
url: "https://doi.org/10.1109/TMC.2018.2871842"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), 18(9), 2020-2033"
modeling_card: not_applicable
tags: [source, edge-computing, container-migration, docker, layered-storage, service-handoff]
related:
  - "[[container-layered-storage-migration]]"
  - "[[service-migration]]"
  - "[[mobile-edge-computing]]"
  - "[[calagna-2024-robust-stateful-migration]]"
created: 2026-08-27
updated: 2026-08-27
---

# Efficient Live Migration of Edge Services Leveraging Container Layered Storage

## Citation

Ma, L., Yi, S., Carter, N., & Li, Q. (2019). *Efficient Live Migration of Edge Services Leveraging Container Layered Storage*. **IEEE Transactions on Mobile Computing, 18**(9), 2020-2033. DOI: 10.1109/TMC.2018.2871842.

## TL;DR

This paper builds a Docker-based edge service-handoff prototype that shares immutable container image layers before migration and transfers only the writable layer plus incremental runtime memory during handoff. Pipelining, compression, and parallel transfer reduce WAN handoff time and user-perceived interruption for workloads such as OpenFace.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ma et al. [x] developed a Docker-based edge service-handoff system for mobile users whose offloading service should follow the nearest edge server. Their prototype shares immutable image layers before migration and transfers only the writable layer and incremental runtime memory during the final handoff. Pipelined processing, compression, and parallel transfer are evaluated with Busybox and the OpenFace face-recognition workload under WAN bandwidth and latency settings. The system reduces OpenFace handoff time by 56% to 80% relative to the compared VM-handoff approach, depending on network bandwidth. The cloud-side decision policy is outside the paper's scope, so the work is an implementation and measurement study rather than a solved optimization model.

## Problem

Container migration tools that package the whole file system transfer redundant Docker base layers and become impractical over low-bandwidth WAN links. The target is to keep a moving user in service at a nearby edge server while reducing transfer volume and interruption time.

## System model

The architecture has a cloud control center, distributed edge nodes, and mobile end users. Both source and target edge nodes pre-download common base image layers. During handoff, a controller coordinates storage-layer synchronization, layer-ID remapping, pre-dump and dirty-memory synchronization, final transfer, and restoration without changing the mobile client application.

## Method

The prototype exploits Docker's copy-on-write layered storage, identifies equal layer content despite different local cache IDs, and transfers only the mutable container layer. It synchronizes memory differences ahead of the final handoff, compresses selected artifacts, and overlaps image and memory transfers through pipeline and parallel processing. Four tunable metrics are exposed: inter-server bandwidth, network latency, compression, and iteration count.

## Key findings

- Under 5 Mbps WAN conditions, OpenFace handoff takes about 49 seconds in the reported experiment; the compared VM handoff takes 247 seconds.
- The measured handoff-time reduction against that VM baseline is 56% to 80% over the tested bandwidth range.
- Pipelining saves about 58 seconds in the OpenFace migration experiment without changing the mobile client.
- More than two pre-synchronization iterations often fail to help OpenFace because dirty memory remains concentrated in a similar region while extra iterations add hardware load.

## Limitations / future work

The cloud control center's migration go/no-go, destination, and scheduling optimization is explicitly outside scope. Results depend on Docker storage-driver behavior, tested workloads, and a prototype tool; the paper does not provide a formal optimality proof or a universal interruption guarantee.

## Relation to the corpus

This is the container-storage counterpart to [[calagna-2024-robust-stateful-migration]]: it reduces file-system transfer overhead, whereas COAT focuses on transport-connection preservation and PAM timing. Both support the [[service-migration]] requirement of keeping mobile edge workloads close to users.

## Raw artifacts

- Parse: `raw/sources/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
