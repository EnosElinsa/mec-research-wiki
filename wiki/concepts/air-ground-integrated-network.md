---
type: concept
title: Air-Ground Integrated Network (AGIN)
tags: [architecture, uav, 6g, ntn]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[qin-2025-bcuav-masac]]"
created: 2026-05-28
updated: 2026-05-28
---

# Air-Ground Integrated Network (AGIN)

A multi-tier networking architecture that combines:

- **Ground layer** — terrestrial base stations, edge servers, IoT devices.
- **Air layer** — UAVs, balloons, HAPS as mobile / quasi-stationary relays and edge nodes.
- **Space layer** — LEO / MEO / GEO satellites for backhaul and global coverage.

In MEC research, AGIN is the umbrella that covers UAV-MEC, [[leo-satellite-edge-computing|LEO-MEC]], and their hybrids. The architecture motif is:

> Ground devices generate tasks → air or space nodes serve as flexible edge servers → all three layers cooperate to deliver compute under coverage / mobility / energy constraints.

## When to use AGIN framing vs single-layer

Single-layer (UAV-only or LEO-only) framing is sufficient when the offloading destinations don't span layers. AGIN framing matters when:

- Tasks may be forwarded across layers (UAV → LEO → cloud).
- Coverage gaps in one layer are filled by another (UAVs cover dense urban, LEOs cover remote terrain).
- The threat model differs by layer and the security architecture must be holistic.

## In this wiki

[[qin-2025-bcuav-masac]] explicitly frames its system as AGIN (devices + UAV edge servers, with future possibility of cloud handoff). [[mao-2025-bcsa-frl]] sits in the ground+space slice (terrestrial users + LEO edge). Future cross-layer sources should land here.
