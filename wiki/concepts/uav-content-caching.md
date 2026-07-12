---
type: concept
title: "UAV Content Caching"
tags: [uav, caching, content-delivery, backhaul, trajectory-control]
related:
  - "[[hua-2026-ddrl-content-delivery]]"
  - "[[wireless-backhaul]]"
  - "[[uav-trajectory-control]]"
  - "[[particle-swarm-optimization]]"
  - "[[secure-caching-uav-mec]]"
  - "[[service-caching-mec]]"
  - "[[coded-caching]]"
created: 2026-07-12
updated: 2026-07-12
---

# UAV Content Caching

UAV content caching stores popular files on an aerial platform so user requests can be served over a short access link instead of retrieving every object through [[wireless-backhaul]]. The cache changes the mobility problem: a UAV's location affects user delay, but its route toward a base station also affects the penalty for a miss and the opportunity to refresh stored content.

In [[hua-2026-ddrl-content-delivery]], each cache-enabled UAV serves users across three base-station regions. A hit is delivered directly; a miss adds UAV-BS retrieval delay. A PSO-tuned replacement score combines content popularity, object-size ratio, and request frequency, while PPO jointly controls movement and transmission behavior under cache and energy limits.

This concept is distinct from [[service-caching-mec]], which places executable service programs, and from computational-task caching, which reuses computation inputs or outputs. It is also broader than [[secure-caching-uav-mec]], where cache placement is coupled to adversarial or confidentiality constraints, and different from [[coded-caching]], which coordinates encoded fragments and multicast opportunities across nodes.

## Design questions

- Which popularity signal remains useful when requests move or change over time?
- Should replacement optimize hit rate alone, or end-to-end acquisition delay including backhaul and flight energy?
- Can a UAV refresh opportunistically at any base station, and how does that choice alter its route?
- Does the communication model expose power as a real action, or hold it fixed while the policy learns only motion and caching?
