---
type: concept
title: Federated Learning Poisoning Attacks
tags: [security, federated-learning, threat-model]
related:
  - "[[federated-reinforcement-learning]]"
  - "[[csra-cold-start-reputation-aggregation]]"
  - "[[mao-2025-bcsa-frl]]"
created: 2026-05-28
updated: 2026-05-28
---

# Federated Learning Poisoning Attacks

Two distinct adversarial profiles attacked by [[mao-2025-bcsa-frl]] and recurring across FL / FRL literature:

## Replay buffer poisoning (passive)

A participant is not deliberately malicious, but its training data — for RL specifically, the replay buffer — is corrupted upstream. Symptoms:

- Local model slowly drifts.
- Sub-model passes structural integrity checks (no bizarre weights) but encodes a biased policy.
- Drift propagates to the global model via aggregation.

Detection is hard because each individual update looks reasonable; only the cumulative trajectory reveals the problem.

## Model parameter poisoning (active)

A participant deliberately uploads bad weights — random noise, biased values, or values designed to flip the global decision in a target region. Symptoms:

- Sub-model differs sharply from peers in the parameter space.
- Easier to detect via outlier checks at aggregation time.

## Why the distinction matters

Replay-buffer poisoning needs **time** to clean up — the buffer must flush the contaminated transitions before the participant can be trusted again. Parameter poisoning is instant: as soon as the satellite stops uploading bad weights, it's safe to re-aggregate.

[[csra-cold-start-reputation-aggregation|CSRA]]'s slow-recovery design specifically targets the replay-buffer case. A pure binary in/out gate handles parameter poisoning but mis-handles replay-buffer recovery.

## Other documented FL attack categories (not the focus of [[mao-2025-bcsa-frl]] but adjacent)

- Backdoor attacks — inject a trigger pattern.
- Membership-inference attacks — extract whether specific data was used.
- Free-rider attacks — participate without contributing.
