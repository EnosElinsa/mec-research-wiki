---
type: source
title: "On-Demand Snapshot Migration: Accelerating Container Migration in Low-Bandwidth Networks"
authors: ["Zhiyuan Hu", "Jiannong Cao", "Zhaorui Zhang", "Yinfeng Cao", "Lei Yang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3720463"
venue: "IEEE Transactions on Mobile Computing, 25(11)"
modeling_card: not_applicable
tags: [source, container-migration, snapshot, file-access-prediction, edge-computing, low-bandwidth, testbed]
related:
  - "[[container-layered-storage-migration]]"
  - "[[stateful-edge-microservice-migration]]"
  - "[[service-migration]]"
  - "[[hardware-validation-and-sim-to-real-in-mec]]"
  - "[[zhang-2025-kubespt-stateful-pod-migration]]"
created: 2026-11-02
updated: 2026-11-03
---

# On-Demand Snapshot Migration: Accelerating Container Migration in Low-Bandwidth Networks

## Citation

Hu, Z., Cao, J., Zhang, Z., Cao, Y., & Yang, L. (2026). *On-Demand Snapshot Migration: Accelerating Container Migration in Low-Bandwidth Networks*. **IEEE Transactions on Mobile Computing, 25**(11). DOI: 10.1109/TMC.2026.3720463.

## TL;DR

Profiling shows that most snapshot files sent during container migration are never read after the container resumes. SEER transfers only the files predicted to be needed, using a learned file-access model with online revision of mispredictions and auto-profiling for unseen containers, integrated with Docker and Kubernetes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hu et al. [x] studied container migration for workload balancing, QoS management, and failure recovery, noting that existing approaches incur high network traffic and long migration time in low-bandwidth edge and IoT environments. By profiling existing methods, they found that most snapshot files transferred during migration are never accessed after resumption. They proposed SEER, an on-demand migration approach that transfers only the snapshot files required for resumption, guided by a learning-based file-access prediction model trained on access traces. An online prediction revision mechanism corrects mispredictions at runtime, and automatic profiling adapts the model to previously unseen containers. Experiments on an edge testbed with Docker and Kubernetes show that SEER significantly reduces both migration time and network traffic, including an 88.1% reduction in median traffic volume compared with an overlay-based approach, while the traffic gain over NFS-based Voyager is marginal.

## Scope and method

The prediction target maximizes a file-size-weighted Jaccard similarity between predicted and actually accessed files. Training traces come from 13 DockerHub containers, each launched 15 times with migrations at different offsets. This is a systems and prediction design without a network decision model.

## Key findings

- Snapshot transfer is the bottleneck of container migration.
- SEER cuts median migration traffic by 88.1% relative to Overlay.
- SEER also shortens migration time and downtime compared with state-of-the-art approaches.

## Limitations / future work

Prediction quality depends on container behavior and migration timing.

## Relation to the corpus

Complements [[container-layered-storage-migration]] and [[stateful-edge-microservice-migration]] with on-demand snapshot transfer validated on hardware.

## Raw artifacts

- Parse: `raw/sources/On-Demand_Snapshot_Migration_Accelerating_Container_Migration_in_Low-Bandwidth_Networks/On-Demand_Snapshot_Migration_Accelerating_Container_Migration_in_Low-Bandwidth_Networks.md`
- Origin PDF and extracted figures are in the same folder.
