---
type: concept
title: "LEO Handover Protocol (connection handover)"
tags: [leo-satellite, handover, non-terrestrial-network, protocol]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[seamless-handover]]"
  - "[[non-terrestrial-network]]"
  - "[[walker-star-constellation]]"
  - "[[lee-2024-dho-leo-handover]]"
created: 2026-06-01
updated: 2026-06-01
---

# LEO Handover Protocol (connection handover)

The signaling procedure by which a ground user equipment transfers its **network connection** from a departing LEO satellite (serving-gNB) to an incoming one (target-gNB) as satellites sweep overhead. Adapted from the 3GPP-NR three-phase HO (preparation → execution → completion), it is stressed in LEO networks by long propagation delay, large coverage areas, limited per-satellite resource blocks, and massive simultaneous access — causing outdated Measurement Reports (MRs), high uplink power, PRACH/preamble collisions, and prolonged access delay.

Distinct from the compute-state [[seamless-handover]] used in satellite federated learning (which hands over a partially-trained model + dataset): here it is the *connection* being handed over. In this wiki, [[lee-2024-dho-leo-handover]] redesigns this protocol with DRL — its DHO scheme skips the MR by predicting signal information — to minimize access delay and collision rate.
