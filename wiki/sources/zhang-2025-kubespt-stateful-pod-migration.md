---
type: source
title: "KubeSPT: Stateful Pod Teleportation for Service Resilience With Live Migration"
authors: ["Hansheng Zhang", "Song Wu", "Hao Fan", "Zhuo Huang", "Weibin Xue", "Chen Yu", "Shadi Ibrahim", "Hai Jin"]
year: 2025
url: "https://doi.org/10.1109/TSC.2025.3564888"
venue: "IEEE Transactions on Services Computing"
modeling_card: not_applicable
tags: [source, live-migration, stateful-migration, container-migration, kubernetes, criu, lazy-restore, testbed]
related:
  - "[[stateful-edge-microservice-migration]]"
  - "[[container-layered-storage-migration]]"
  - "[[service-migration]]"
  - "[[calagna-2024-robust-stateful-migration]]"
  - "[[hu-2026-seer-on-demand-container-migration]]"
  - "[[frejo-martin-2025-uav-stateful-microservice-live-migration]]"
  - "[[hardware-validation-and-sim-to-real-in-mec]]"
  - "[[hai-jin]]"
created: 2026-11-03
updated: 2026-11-03
---

# KubeSPT: Stateful Pod Teleportation for Service Resilience With Live Migration

## Citation

Zhang, H., Wu, S., Fan, H., Huang, Z., Xue, W., Yu, C., Ibrahim, S., & Jin, H. (2025). *KubeSPT: Stateful Pod Teleportation for Service Resilience With Live Migration*. **IEEE Transactions on Services Computing**. DOI: 10.1109/TSC.2025.3564888. The parse gives no venue, year, or DOI; they follow the first author's ORCID record.

## TL;DR

Kubernetes reschedules a pod by killing it and recreating it, which loses the runtime state of stateful long-running applications. KubeSPT live-migrates stateful pods with CRIU: it keeps pod and container network state synchronized so TCP connections survive, restores only hot memory pages before restart and the rest on demand, and decouples migration from normal pod creation and deletion. Downtime falls by 86% to 93% against current rescheduling.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] addressed live migration of stateful pods for Kubernetes rescheduling, which is triggered by system upgrades, node failures, and load-balancing optimizations. They identified three obstacles: pod network namespace initialization breaks the network state shared with internal containers, restoring the full memory state prolongs downtime, and Kubernetes pod operations do not preserve application state. Their KubeSPT system synchronizes the network state of pods and internal containers by controlling packet flow and implements fast service redirection. It also uses iterative pre-copy checkpointing that tracks hot memory pages, restores only the hot data at the destination, and lazily restores the remaining pages on demand. Pod migration operations are decoupled from other Kubernetes operations through a Custom Resource Definition so that migration remains compatible with existing controllers. Experiments with Redis and FFmpeg workloads on a three-node Kubernetes 1.18.20 cluster show that KubeSPT reduces downtime by 86% to 93% compared with current rescheduling methods.

## Scope and method

Each migration request is a Custom Resource Definition object. A controller picks the target node through the scheduler and reserves resources, and a per-node Migration Daemon runs three modules. T-Checkpointer pre-pulls images on the target and iteratively checkpoints memory, tracking the ACCESSED bit in page-table entries to find the hot set. It then removes the original pod and takes a final checkpoint while the controller creates the new pod and T-Proxy redirects the service. T-Restorer restores hot pages first and serves the remaining pages from the checkpoint files on page faults after restart.

The testbed is a Kubernetes 1.18.20 cluster of three nodes (Intel Xeon E5-2680 v4, 64 GB RAM, 3 Gbps links). Workloads are Redis with 1 to 8 GB of data, which is storage-intensive, and FFmpeg decoding for 2 to 20 clients, which is compute-intensive. The baseline is the current Kubernetes rescheduling method, and each experiment is averaged over ten runs. This is a systems design without a network decision model.

## Key findings

- With hot-data preloading plus lazy restore, downtime falls by 86% to 93%; the 8 GB Redis workload has 10.76 s of downtime and FFmpeg workloads at most 26.47 s.
- Connection redirection takes 93 to 139 ms. A straightforward CRIU and overlay-network migration broke established TCP connections, with an interruption probability above 90%, while KubeSPT kept them in every test.
- Hot-data and lazy restore cuts memory-restoration downtime by 40% for the heaviest Redis workload and by 38% for the heaviest FFmpeg workload.
- Total migration time reaches 79.81 s for 8 GB Redis and 128.74 s for 20-client FFmpeg; inter-node bandwidth is the main bottleneck, and fast-changing FFmpeg memory keeps final checkpoints large.
- Deployments, StatefulSets, and the Tapp controller keep their specified pod state after migration.

## Limitations / future work

The memory method suits applications with skewed, stable memory footprints and needs prior knowledge of their access patterns. Checkpoint traffic contends with co-located applications. Control-plane latency when dozens of pods migrate concurrently was not quantified. A communication failure while final checkpoint files are transferred can lose pod state, and the authors propose backing these files up in source-node memory as future work. The evaluation is a data-center cluster rather than an edge or aerial deployment.

## Relation to the corpus

KubeSPT is an orchestrator-level implementation of [[stateful-edge-microservice-migration]]. It shares the CRIU connection-preservation problem with [[calagna-2024-robust-stateful-migration]], and it addresses memory restoration where [[container-layered-storage-migration]] addresses image layers and [[hu-2026-seer-on-demand-container-migration]] addresses snapshot-file transfer. Its downtime decomposition is a reference point for UAV replacement with live migration in [[frejo-martin-2025-uav-stateful-microservice-live-migration]].

## Raw artifacts

- Parse: `raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md`
- Origin PDF and extracted figures are in the same folder.
