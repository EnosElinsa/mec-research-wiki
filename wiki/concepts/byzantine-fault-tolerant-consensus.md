---
type: concept
title: "Byzantine Fault-Tolerant (BFT) Consensus"
tags: [blockchain, consensus, security, distributed-systems]
related:
  - "[[wang-2025-acbft-uav-consensus]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[zero-trust-architecture]]"
created: 2026-05-29
updated: 2026-05-29
---

# Byzantine Fault-Tolerant (BFT) Consensus

A class of consensus protocols (rooted in PBFT) that let distributed nodes agree on a consistent, immutable state even when some nodes are malicious ("Byzantine"). Classical BFT is **broadcast-based** — every phase disseminates messages to all nodes — which is communication-heavy.

**Chain-based BFT** instead propagates signals along an ordered chain (each node signals after receiving from its predecessor), reducing communication complexity and, in wireless UAV networks, signal collisions. [[wang-2025-acbft-uav-consensus]] proposes ACBFT, a chain-based BFT protocol that uses [[particle-swarm-optimization]] to compute the chain order from the UAV network topology, with sub-protocols (rechaining) to handle malicious nodes and dynamic membership. BFT consensus underpins consortium-blockchain trust models such as those in [[mao-2025-bcsa-frl]] and [[qin-2025-bcuav-masac]].
