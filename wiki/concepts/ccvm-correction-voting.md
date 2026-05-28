---
type: concept
title: CCVM (Constrained Correction Voting Mechanism)
tags: [blockchain, voting, security, consensus]
related:
  - "[[blockchain-for-fl-aggregation]]"
  - "[[csra-cold-start-reputation-aggregation]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-05-28
updated: 2026-05-28
---

# CCVM (Constrained Correction Voting Mechanism)

A vote-weighting rule introduced in [[mao-2025-bcsa-frl]] for blockchain consensus inside an FRL aggregation pipeline. Replaces equal-weight voting with a correction factor that decreases as a participant's track record of negative votes against legitimate models grows.

## Threat addressed

**Malicious voting attack:** a Byzantine satellite always emits $V_F$ when validating peers' models and only emits $V_T$ for its own updates. With equal-weight voting, a small minority of such voters can stall block commission and prevent FL convergence.

## Mechanism

Each voter $s_k$ accumulates a profile of $V_T / V_F$ ratios across rounds. Voters whose negative-vote rate diverges sharply from the network mean are progressively penalized — their effective vote weight shrinks. Honest disagreements are tolerated; *consistent* disagreement is treated as adversarial.

## Empirical effect (from [[mao-2025-bcsa-frl]])

- Without CCVM under combined malicious-voting + data-poisoning attack: reward converges to <10.
- With CCVM: reward converges to ~25.

## Composition with [[csra-cold-start-reputation-aggregation|CSRA]]

CCVM cleans the *consensus layer*; CSRA cleans the *aggregation weights*. Together they handle both kinds of misbehavior — voting subversion and parameter poisoning — without one mechanism's false positives wrecking the other.
