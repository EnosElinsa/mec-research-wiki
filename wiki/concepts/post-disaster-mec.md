---
type: concept
title: Post-Disaster MEC
tags: [mec, scenario, emergency, resilience]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[erasure-coded-edge-storage]]"
  - "[[huang-2026-erasure-coded-uav-storage]]"
  - "[[liu-2026-usp-nfrp-emergency-communication]]"
  - "[[persistent-emergency-uav-swarm-service]]"
  - "[[pham-2026-vnf-control-loop]]"
  - "[[routing-vnf-scaling-control-loop]]"
  - "[[tian-2026-joint-localization-communication]]"
  - "[[joint-localization-and-communication]]"
created: 2026-05-28
updated: 2026-07-13
---

# Post-Disaster MEC

The MEC operating regime where ground infrastructure is partially or wholly destroyed (earthquake, flood, war) and aerial / satellite platforms must temporarily replace or augment it.

## Distinguishing properties

- **Heterogeneous user density** — survivor clusters at refugee camps and triage points coexist with sparsely distributed search-and-rescue teams. Service must be fair across both.
- **Mission-critical urgency** — many tasks are delay-sensitive (medical telemetry, location pings). Pure throughput optimization can starve high-priority workloads.
- **Asymmetric uplink** — IMDs have weak transmit power; aerial relays must work hard to close the link.
- **Energy scarcity** — UAVs are battery-bound and recharge stations may not exist. Aerial endurance is the binding constraint.

## Common architectural responses

- **Two-tier (UAV + HAPS)** — UAVs as low-altitude relays, HAPS as long-endurance umbrella. See [[hierarchical-aerial-mec]].
- **Urgency-aware admission** — instead of FCFS, sort tasks by deadline / criticality before admitting to the UAV queue. See DRUDM in [[peng-2025-drudm-cfg]].
- **Fairness regularizers** — explicit reward shaping to avoid UAV "camping" over the densest cluster. See [[theil-fairness-index]] and the corresponding regularizers in [[peng-2025-drudm-cfg]] and [[liu-2026-jppo-en-convntm]].
- **Resilient edge storage** — UAVs can cache coded data blocks so users recover files even when only a subset of UAVs is reachable. See [[erasure-coded-edge-storage]] and [[huang-2026-erasure-coded-uav-storage]].
- **Persistent rotating backhaul** - [[liu-2026-usp-nfrp-emergency-communication]] uses [[persistent-emergency-uav-swarm-service]] to rotate fixed-wing aircraft through access/relay tasks while repairing the aerial tree topology during replacements.

## Open questions

- How does post-disaster traffic actually distribute? Most simulation studies use synthetic uniformly-random or Gaussian-mixture clusters; real disaster traces would be more bursty and irregular.
- How robust are these algorithms to *intermittent* aerial loss (UAV crash, HAPS station-keeping failure)?
