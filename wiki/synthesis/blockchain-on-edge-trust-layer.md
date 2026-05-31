---
type: synthesis
title: "Blockchain-on-edge: which layer does the chain defend?"
tags: [synthesis, blockchain, security, mec, comparison]
related:
  - "[[mao-2025-bcsa-frl]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[wang-2025-acbft-uav-consensus]]"
  - "[[byzantine-fault-tolerant-consensus]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[zero-trust-architecture]]"
  - "[[ccvm-correction-voting]]"
  - "[[csra-cold-start-reputation-aggregation]]"
  - "[[particle-swarm-optimization]]"
  - "[[bcsa-frl-vs-bc-uav-masac]]"
  - "[[acbft-throughput-increase]]"
created: 2026-05-31
updated: 2026-06-02
---

# Blockchain-on-edge: which layer does the chain defend?

Three curated sources bolt a permissioned blockchain onto an aerial/space edge-compute system. The useful axis for telling them apart is **which layer of the stack the blockchain actually operates at** — because that determines the threat it defends against and the overhead it costs. The pairwise design-philosophy contrast for the first two lives in [[bcsa-frl-vs-bc-uav-masac]]; this page adds the consensus-protocol-layer source ([[wang-2025-acbft-uav-consensus]]) and maps all three on one axis.

## Roster

| Source | Venue / year | Edge platform | Blockchain operates at… | Headline result |
|---|---|---|---|---|
| [[mao-2025-bcsa-frl]] (BCSA-FRL) | LEO satellites | the **aggregation** layer (replaces the FL aggregator) | tolerates ~50% malicious satellites at flat ≈5% drop / ≈6 ms delay ([[bcsa-frl-tolerates-up-to-half-malicious-satellites]]) |
| [[qin-2025-bcuav-masac]] (BC-UAV-MASAC) | UAVs over IoT terminals | the **audit** layer (tamper-evident offload records) | +15.41% sensing / −30.73% queue delay vs MADDPG ([[masac-beats-maddpg-sensing-queue]]) |
| [[wang-2025-acbft-uav-consensus]] (ACBFT) | UAV ad hoc network | the **consensus-protocol** layer itself | up to 96.2% throughput increase vs existing chaining protocols ([[acbft-throughput-increase]]) |

(Venues for the first two are tabulated in [[bcsa-frl-vs-bc-uav-masac]]; ACBFT is IEEE TVT 2025.)

## The three layers

1. **Consensus-protocol layer — [[wang-2025-acbft-uav-consensus]].** ACBFT redesigns the consensus mechanism *itself* for resource-constrained, fast-moving UAVs: chain-based propagation instead of all-to-all broadcast, with a [[particle-swarm-optimization|PSO]]-derived chain order computed from the live topology distance matrix. The contribution is throughput/overhead of the protocol, not what is being agreed upon. This is the layer the other two sources take as a given.

2. **Aggregation layer — [[mao-2025-bcsa-frl]].** Here consensus *is* the FL aggregator: in a [[zero-trust-architecture|zero-trust]] LEO setting with no trustable central server, the chain decides which sub-models become the global model. Its added machinery ([[ccvm-correction-voting|CCVM]] + [[csra-cold-start-reputation-aggregation|CSRA]]) hardens that aggregation against malicious voters and poisoned models.

3. **Audit layer — [[qin-2025-bcuav-masac]].** The chain records *what happened* after the fact for tamper-evidence; the system still runs without it. The novelty is the optimization stack (Lyapunov → CVX + MASAC + DOA), with the blockchain treated as a compute-resource competitor rather than a protagonist.

## Cross-cutting observations

- **The deeper the layer, the more general the source.** ACBFT (consensus-protocol) is reusable by any blockchain-on-edge system; BCSA-FRL (aggregation) is specific to federated learning; BC-UAV-MASAC (audit) is specific to its offloading pipeline. A system could in principle run all three: ACBFT as the consensus engine, CCVM/CSRA at aggregation, and an audit trail on top.
- **Consensus cost vs MEC compute is an explicit concern for two of the three.** ACBFT attacks it at the protocol level (less communication — `O(n)` chain synchronization vs the `O(n²)` of broadcast BFT like PBFT), and BC-UAV-MASAC at the allocation level (a long-term block-creation-delay constraint, with DOA splitting UAV CPU across task-compute / block-generation / block-verification). BCSA-FRL does not analyze blockchain compute overhead against the offloading latency budget — its own limitations flag the smart-contract cost as unquantified — so on the cost axis it is the least characterized of the three.
- **Byzantine tolerance shows up in two forms.** BCSA-FRL's ~50% threshold is a *property of the voting consensus*; ACBFT's `N = 3f + 1` operating point is the *classic BFT bound* made efficient. They are complementary statements about the same underlying limit.

## Gaps

- **No source combines the layers.** The composition opportunity flagged in [[bcsa-frl-vs-bc-uav-masac]] (import CCVM/CSRA into the MASAC pipeline) extends naturally to "run it over ACBFT" — but no curated source does this.
- **No real-hardware blockchain validation.** All three are simulation + analysis; the consensus overhead numbers are not measured on flying UAVs.
- **Maritime and vehicular tracks have no blockchain source** — see the gap noted in [[maritime-mec-architectures]].
