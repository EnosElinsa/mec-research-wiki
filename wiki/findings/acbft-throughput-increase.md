---
type: finding
title: ACBFT raises UAV-consensus throughput by up to 96.2% over existing chaining protocols
source: "[[wang-2025-acbft-uav-consensus]]"
confidence: medium
replicated: null
tags: [blockchain, byzantine-fault-tolerant-consensus, uav-networks, benchmark, throughput]
related:
  - "[[byzantine-fault-tolerant-consensus]]"
  - "[[particle-swarm-optimization]]"
created: 2026-05-31
updated: 2026-05-31
---

# ACBFT raises UAV-consensus throughput by up to 96.2% over existing chaining protocols

In [[wang-2025-acbft-uav-consensus]], the paper's contribution list states that ACBFT **"achieves an increase in throughput of up to 96.2%, while simultaneously reducing communication overhead compared to existing chaining protocols"** (parse L35).

The number is the headline evaluation result for the protocol's chain-propagation design: each consensus node signals only after receiving from its predecessor (instead of all-to-all broadcast), and a [[particle-swarm-optimization|PSO]]-derived chain order is computed from the real-time UAV topology distance matrix.

## Mechanism

- **Chain-based, not broadcast-based BFT.** Broadcast-heavy PBFT-derived protocols cause communication blow-up and signal collisions for mobile, resource-constrained UAVs. Chaining linearizes the message pattern, cutting overhead.
- **PSO chain ordering.** The order in which nodes are chained is optimized from the consensus-node distance matrix, minimizing propagation cost as the topology changes.
- The result is reported against other chaining BFT protocols; Fig. 6 shows throughput-vs-node-count curves where ACBFT leads the compared protocols at `N = 3f + 1`.

## Caveats

- Single-paper result, simulation + security analysis only — `confidence: medium`.
- "Up to 96.2%" is a best-case headline; the per-node-count Fig. 6 curves (read from the parsed figure) are the indicative shape behind it.
- Throughput is gained partly at the cost of a small latency increase under typical conditions (chain propagation is serial), as the source page notes.

## Relation to the corpus

This is the consensus-layer member of the wiki's **trust / blockchain-on-edge** thread. It complements the aggregation-layer result in [[bcsa-frl-tolerates-up-to-half-malicious-satellites]] ([[mao-2025-bcsa-frl]]) and the secure-aerial-MEC result in [[masac-beats-maddpg-sensing-queue]] ([[qin-2025-bcuav-masac]]) — three different blockchain-on-edge mechanisms (consensus ordering / correction-voting + reputation aggregation / Lyapunov-coupled MASAC), each validated on its own metric.

> Note: this finding was deferred in the 2026-05-30 pass because the 96.2% figure was then believed to be absent from the parse. The 2026-05-31 audit located it verbatim at parse L35 and restored it; this finding records the now-grounded result.
