---
type: concept
title: Zero Trust Architecture (ZT / ZTA)
tags: [security, trust, architecture]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-05-28
updated: 2026-05-28
---

# Zero Trust Architecture (ZT / ZTA)

A security stance that abandons the traditional "trusted perimeter" — *no* device or service is implicitly trusted because of where it sits in the network. Every interaction must be continuously authenticated, authorized, and monitored. Slogan: **"never trust, always authenticate."**

## Why MEC research cares

In multi-tenant edge systems — particularly [[leo-satellite-edge-computing]] where service providers rent satellites from multiple operators — the classical FL "trusted central server" assumption fails. ZT pushes researchers toward:

- Decentralized, consensus-based aggregation (often via [[blockchain-for-fl-aggregation|blockchain]]).
- Per-round model verification rather than per-session authentication.
- Reputation systems that can survive adversarial votes.

## Common attack surfaces in ZT MEC

- Identity spoofing (mitigated by blockchain-based DID / hashed-public-key schemes).
- Federated-learning poisoning — see [[fl-poisoning-attacks]].
- Consensus subversion — malicious validators voting against legitimate updates. Addressed by mechanisms like [[ccvm-correction-voting]].

## Trust restoration

A practical sub-question: once a satellite recovers from poisoning, how do you let it re-contribute *without* its still-tainted replay buffer poisoning the global model? See [[csra-cold-start-reputation-aggregation]] for one answer.
