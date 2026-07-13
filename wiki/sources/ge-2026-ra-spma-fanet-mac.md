---
type: source
title: "Reliable, Adaptive Flying Ad Hoc Multiple Access Protocol Based on Statistical Priority"
authors: ["Zhibin Ge", "Yongxin Feng", "Wenbo Zhang", "Yibin Feng"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3617981"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 1171-1183, 2026"
tags: [source, fanet, mac-protocol, statistical-priority, channel-occupancy, adaptive-backoff, priority-queues, qos]
related:
  - "[[statistical-priority-based-multiple-access]]"
  - "[[autonomous-uav-swarms]]"
  - "[[queueing-theory]]"
  - "[[bujari-2018-stateless-fanet-routing]]"
  - "[[deng-2026-eret-fanet-routing]]"
  - "[[song-2026-albpd-directional-fanet]]"
created: 2026-07-14
updated: 2026-07-14
---

# Reliable, Adaptive Flying Ad Hoc Multiple Access Protocol Based on Statistical Priority

## Citation

Ge, Z., Feng, Y., Zhang, W., & Feng, Y. (2026). *Reliable, Adaptive Flying Ad Hoc Multiple Access Protocol Based on Statistical Priority*. **IEEE Transactions on Green Communications and Networking**, 10, 1171-1183. DOI: 10.1109/TGCN.2025.3617981.

## TL;DR

Proposes RA-SPMA, a load-aware MAC protocol for multi-priority flying ad hoc networks. It combines subnet-scoped, time-weighted Channel Occupancy Statistics (COS), feedback-controlled access thresholds, and channel-state-dependent backoff to protect highest-priority traffic under changing load. MATLAB/OPNET simulations report higher highest-priority delivery and lower delay than the selected baselines, with reduced delivery for lower-priority traffic.

## Problem

UAV-cluster links have limited effective capacity under interference and mobility, while urgent traffic still requires differentiated delivery and latency. Existing SPMA designs treat load statistics, access thresholds, and backoff separately. The paper jointly adapts these three controls so that eight packet-priority queues can respond to subnet load without relying on fixed access parameters.

## System model

The motivating FANET is a hierarchical UAV cluster with local subnets and boundary relays. Within a subnet, each node counts one-hop channel traffic, and recent counting cycles receive larger weights in COS. Queued traffic is divided into priorities `P0` through `P7` using time sensitivity, QoS request, cyclicity, and data length. A frame may transmit only when its queue is pending and its priority threshold exceeds the current COS.

The COS counting period changes across low-, medium-, and high-load regions. The simulation combines a MATLAB physical layer with an OPNET link layer, using rate-1/2 LDPC coding, GMSK modulation, and a random interleaver. Table IV lists a 2 Mbps data rate, while the experiments vary offered load from 5 to 25 Mbps and the conclusion reports 10 Mbps throughput; the parse does not explain how these quantities map across nodes, subnets, or channels.

## Method

RA-SPMA forms a time-weighted COS from the most recent subnet-load cycles and changes the statistics period to limit overhead and collisions. Its three-stage dynamic-threshold controller first increases the highest-priority threshold rapidly, then additively, and finally uses short-amplitude feedback based on changes in highest-priority packet delivery. Lower-priority thresholds are derived after accounting for higher-priority queued traffic.

The Window Adaptive Backoff Algorithm assigns shorter waits to higher priorities under stable load and expands contention windows when the channel is busy. The integrated algorithm combines COS updates, threshold-controlled send flags, and backoff selection. The paper also gives a local stability argument for the final threshold-feedback stage and states linear-order protocol complexity, but does not derive every baseline complexity under a common operation model.

## Key findings

- In the parameter sweep, the authors identify the COS history length as having the largest effect on highest-priority delivery, followed by the low/high-load adjustment factors and then the feedback growth factor. This ranking is derived from Fig. 6 rather than a results table.
- At 10 Mbps offered traffic, the paper reports highest-priority delivery above 99%, near 100%, for RA-SPMA, while its other priorities fluctuate between 60% and 80%. The corresponding SPMA figure is described as reaching 96% for the highest priority and 80%-95% for other priorities. These are author readings of simulated curves and expose the lower-priority tradeoff.
- The authors report that RA-SPMA keeps highest-priority delivery above 99% at 64 nodes, while SPMA does so only below 32 nodes. They also report RA-SPMA average delay below 2 ms at 32 nodes and rising to 4.1 ms as node count increases. These values are figure-derived and scenario-specific.
- The paper recommends at most 32 nodes per subnet to jointly target 10 Mbps throughput, at least 99% highest-priority delivery, and under 2 ms average delay. This is a simulation-based design recommendation, not a proven capacity bound.
- The paper describes RA-SPMA as having lower and more stable average delay than SPMA, with a reported 0.1-0.3 ms difference after 500 simulation seconds. Jitter differences are described as slight; both claims come from plotted simulations.

## Limitations

Evidence is limited to MATLAB/OPNET co-simulation, with no airborne testbed, field channel trace, confidence intervals, or independent validation workload. The paper explicitly leaves physical-layer frequency hopping and node mobility insufficiently investigated. Its one-hop subnet statistics do not establish end-to-end behavior across interconnected subnets, and no fairness metric quantifies the delivery sacrificed by lower priorities.

The source describes a 2-byte frame-control field containing 2 priority bits while also defining eight `P0-P7` priority levels; 2 bits cannot directly encode eight values. This is preserved as a source inconsistency. The 2 Mbps table entry, 5-25 Mbps offered-load sweep, and 10 Mbps throughput claim are likewise retained as distinct quantities because their relationship is not established in the parse.

## Relation to the corpus

[[statistical-priority-based-multiple-access]] provides the link-layer access vocabulary for this source. [[bujari-2018-stateless-fanet-routing]] and [[deng-2026-eret-fanet-routing]] address FANET forwarding and route adaptation, whereas RA-SPMA controls contention after packets are queued. [[song-2026-albpd-directional-fanet]] manages mobility-driven directional-link breakage rather than channel occupancy and service-priority access. The priority queues provide a limited connection to [[queueing-theory]], while [[autonomous-uav-swarms]] supplies the broader cooperating-UAV context.

## Raw artifacts

- Parse: `raw/sources/Reliable_Adaptive_Flying_Ad_Hoc_Multiple_Access_Protocol_Based_on_Statistical_Priority/Reliable_Adaptive_Flying_Ad_Hoc_Multiple_Access_Protocol_Based_on_Statistical_Priority.md`
- Origin PDF: `raw/sources/Reliable_Adaptive_Flying_Ad_Hoc_Multiple_Access_Protocol_Based_on_Statistical_Priority/Reliable_Adaptive_Flying_Ad_Hoc_Multiple_Access_Protocol_Based_on_Statistical_Priority.pdf`
- Figures: `raw/sources/Reliable_Adaptive_Flying_Ad_Hoc_Multiple_Access_Protocol_Based_on_Statistical_Priority/images/`
