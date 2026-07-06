---
type: concept
title: Blockchain for Federated Learning Aggregation
tags: [blockchain, federated-learning, security, consensus]
related:
  - "[[federated-reinforcement-learning]]"
  - "[[zero-trust-architecture]]"
  - "[[ccvm-correction-voting]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[wang-2026-blockchain-lae-fl-mappo]]"
created: 2026-05-28
updated: 2026-07-07
---

# Blockchain for Federated Learning Aggregation

Replacing the central FL aggregator with a permissioned blockchain. The attractive properties:

- **Distributed ledger** — every participant has the full audit trail of model updates and votes; tampering is detectable.
- **Smart-contract consensus** — aggregation rules are executed deterministically by the network, not by a single trusted server.
- **Traceability** — historical sub-model behavior is durably recorded and can drive reputation scores.

## The natural fit with [[zero-trust-architecture|ZT]]

Classical FL needs a central aggregator everyone trusts. ZT explicitly forbids this. Blockchain provides a way to *manufacture* consensus without a central point of trust, which is why most ZT MEC schemes (e.g. [[mao-2025-bcsa-frl]]'s BCSA-FRL) reach for it.

## Caveats

- **Block commission cost.** Every aggregation round becomes a consensus round — added latency and energy.
- **Smart-contract attack surface.** The contract itself is now part of the threat model. In particular, **malicious voting** — a Byzantine voter that always votes against the block — can stall the system if the contract weights every vote equally. See [[ccvm-correction-voting]] for one mitigation.
- **Resource contention.** On-chain operations compete with the underlying compute / offloading workload for satellite resources.

## Common patterns

- Off-chain ML training, on-chain *votes* over hashes of model updates.
- On-chain reputation scores fed back into per-round aggregation weights.
- Time-bounded synchronization rounds aligned with [[leo-satellite-edge-computing|LEO]] coverage windows.

[[wang-2026-blockchain-lae-fl-mappo]] uses blockchain as a trust/cooperation layer for SUAVs in a low-altitude FL-MAPPO offloading and caching network. Its BS still aggregates the FL global model, so it is a blockchain-assisted FL coordination pattern rather than a pure blockchain replacement for the central aggregator.
