---
type: finding
title: BCSA-FRL tolerates up to ~50% malicious LEO satellites with negligible degradation
source: "[[mao-2025-bcsa-frl]]"
confidence: medium
replicated: null
tags: [security, leo-satellite, federated-learning, benchmark]
related:
  - "[[ccvm-correction-voting]]"
  - "[[csra-cold-start-reputation-aggregation]]"
  - "[[fl-poisoning-attacks]]"
created: 2026-05-28
updated: 2026-05-28
---

# BCSA-FRL tolerates up to ~50% malicious LEO satellites with negligible degradation

In [[mao-2025-bcsa-frl]] Fig. 5, the BCSA-FRL framework holds:

- drop rate ≈ 5%
- average task processing delay ≈ 6 ms

across malicious-satellite proportions from 10% up to 50% — **nearly flat performance**. The FedAvg-FRL baseline degrades sharply across the same range.

## Why the threshold is 50%

Above 51%, the consensus mechanism itself is captured: malicious voters now hold a majority and can refuse to commit honest blocks. The system stalls in synchronization rollback and never trains. The authors note that >50% adversary majority is rare in practice.

## Mechanism breakdown

- [[ccvm-correction-voting|CCVM]] handles the consensus layer — malicious voters lose vote weight.
- [[csra-cold-start-reputation-aggregation|CSRA]] handles the aggregation layer — poisoned sub-models are sharply down-weighted, then recovered slowly.

Together they cover both attack surfaces. Without CCVM under combined attack, reward converges to <10. With CCVM, reward converges to ~25 (paper Fig. 4).

## vs traditional offloading baselines

| Algorithm | Drop rate @ load 150 | Avg delay @ load 150 |
|---|---|---|
| BCSA-FRL | 6.16% | 5.95 ms |
| Average Task Burden | 20.05% | 7.40 ms |
| Random | 40.54% | 9.31 ms |

At load 450, BCSA-FRL still holds at 8.29% / 6.08 ms.

## Caveats

- Single-paper result, simulation only — `confidence: medium`.
- The 50% threshold is a hard property of the underlying voting consensus, not of CCVM/CSRA. No defense at this layer can survive a true Byzantine majority.
- Compute / energy cost of the blockchain consensus itself is not separated out in the paper's latency numbers.
