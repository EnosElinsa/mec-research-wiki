---
type: source
title: "ACBFT: Adaptive Chained Byzantine Fault-Tolerant Consensus Protocol for UAV Ad Hoc Networks"
authors: ["Jingjing Wang", "Jiaxing Wang", "Ziheng Tong", "Zihan Jiao", "Mengyuan Zhang", "Chunxiao Jiang"]
year: 2025
url: "https://doi.org/10.1109/TVT.2025.3548281"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, blockchain, byzantine-fault-tolerance, uav-networks, consensus-protocol, pso]
related:
  - "[[blockchain-for-fl-aggregation]]"
  - "[[byzantine-fault-tolerant-consensus]]"
  - "[[zero-trust-architecture]]"
  - "[[particle-swarm-optimization]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[qin-2025-bcuav-masac]]"
created: 2026-05-29
updated: 2026-05-30
---

# ACBFT: Adaptive Chained Byzantine Fault-Tolerant Consensus Protocol for UAV Ad Hoc Networks

## Citation

Wang, J., Wang, J., Tong, Z., Jiao, Z., Zhang, M., & Jiang, C. (2025). *ACBFT: Adaptive Chained Byzantine Fault-Tolerant Consensus Protocol for UAV Ad Hoc Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2025.3548281.

## TL;DR

A blockchain consensus protocol tailored to UAV ad hoc networks. Traditional broadcast-based BFT protocols consume too much communication and worsen signal collisions for resource-constrained, highly mobile UAVs. **ACBFT** extends chain-based BFT and uses **[[particle-swarm-optimization|particle swarm optimization (PSO)]]** to compute the chain order from the real-time UAV network topology, cutting communication overhead and improving robustness. Sub-protocols handle malicious nodes (rechaining), dynamic node join/exit, and UAV loss.

## Problem framing

UAV networks are open wireless, mobile ad hoc systems without a central authority; transmitted inter-UAV data is vulnerable to tampering and malicious injection. Blockchain provides tamper-resistant, auditable record-keeping, but existing consensus protocols (PBFT-derived, broadcast-heavy) are too resource-hungry and collision-prone for UAVs, whose topology changes constantly. The paper treats the UAV ad hoc network as a special case of a consortium blockchain.

## System model

- **Network.** UAV set U as a P2P multi-hop network (partial-synchronous). A separate **authentication network** and **consensus network** — only authenticated UAVs that pass entry join the consensus node set P (a subset of U).
- **Topology.** A consensus-node distance matrix records shortest-hop routing distances between consensus nodes; atomic operations (join/exit/loss/topology change) update it.
- **Blockchain structure.** Standard block header (version, previous hash, timestamp, Merkle root) + body of non-financial UAV interaction transactions; signatures, MACs, and hash digests provide integrity.

## Method

- **Chain-based BFT** instead of broadcast: each node signals only after receiving from its predecessor, reducing communication complexity and signal collisions.
- **PSO-based chain ordering** computes the consensus chain order from the topology/distance matrix to minimize overhead.
- **Sub-protocols:** rechaining (detect/handle malicious nodes), joining/exiting protocols for dynamic membership, and accident handling for UAV loss; plus a reconfiguration-free scheme.

## Key findings

- The chain-propagation design trades a small latency increase under typical network conditions for **higher throughput** than broadcast-based BFT, and the PSO-based chain ordering reduces communication overhead. The paper's Fig. 6 reports throughput-vs-node-count curves where ACBFT leads the compared BFT protocols (BChain and others) at `N = 3f + 1`. (A specific "96.2%" headline figure is **not in the parse** — the comparative throughput/overhead advantage is read from the figures and is indicative, not an exact parsed number.)

## Limitations / future work

Evaluated by simulation and security analysis. The authors flag large-scale UAV networks and augmenting ACBFT with a machine-learning-based trust-management system as future work.

## Relation to the corpus

Extends the wiki's **trust / blockchain-on-edge** thread beyond aggregation and offloading: where [[mao-2025-bcsa-frl]] uses blockchain for federated-RL aggregation in zero-trust LEO networks and [[qin-2025-bcuav-masac]] embeds blockchain in secure aerial edge computing, this paper targets the **consensus protocol layer** itself for UAV ad hoc networks. It connects to [[zero-trust-architecture]] and introduces [[byzantine-fault-tolerant-consensus]] and [[particle-swarm-optimization]] to the corpus.

## Raw artifacts

- `raw/sources/ACBFT_Adaptive_Chained_Byzantine_Fault-Tolerant_Consensus_Protocol_for_UAV_Ad_Hoc_Networks/full.md`
- Original PDF and extracted figures in the same folder.
