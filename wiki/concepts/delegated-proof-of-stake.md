---
type: concept
title: "Delegated Proof of Stake (DPoS)"
tags: [blockchain, consensus, security, distributed-systems]
related:
  - "[[blockchain-on-edge-trust-layer]]"
  - "[[byzantine-fault-tolerant-consensus]]"
  - "[[reverse-auction-incentive]]"
  - "[[wang-2024-blockchain-uav-mec-dpos]]"
created: 2026-05-31
updated: 2026-05-31
---

# Delegated Proof of Stake (DPoS)

A blockchain consensus mechanism in which stakeholders **vote** to elect a small set of delegate nodes that take turns producing and validating blocks, rather than every node competing (as in Proof of Work) or staking directly (as in Proof of Stake). DPoS trades some decentralization for higher throughput and lower energy, but is exposed to **stakeholder voting collusion**.

In the wiki, [[wang-2024-blockchain-uav-mec-dpos]] proposes an *improved* DPoS for blockchain-integrated UAV-assisted MEC: UAVs act as light nodes that collect tasks and verify signatures to form an initial block, while ground blockchain nodes (full nodes) are selected from base stations through a **reputation incentive mechanism** (reputation + computing capacity) to perform final block generation — mitigating the voting-collusion weakness of vanilla DPoS. It sits in the [[blockchain-on-edge-trust-layer]] alongside other consensus schemes such as the chain-based [[byzantine-fault-tolerant-consensus|BFT]] of [[wang-2025-acbft-uav-consensus]].
