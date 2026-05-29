---
type: comparison
title: "Blockchain-on-edge: BCSA-FRL vs BC-UAV-MASAC"
tags: [comparison, blockchain, security, mec]
related:
  - "[[mao-2025-bcsa-frl]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[zero-trust-architecture]]"
  - "[[federated-reinforcement-learning]]"
  - "[[ccvm-correction-voting]]"
  - "[[csra-cold-start-reputation-aggregation]]"
  - "[[fl-poisoning-attacks]]"
  - "[[lyapunov-optimization]]"
  - "[[masac]]"
  - "[[ddqn]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[air-ground-integrated-network]]"
created: 2026-05-29
updated: 2026-05-30
---

# Blockchain-on-edge: BCSA-FRL vs BC-UAV-MASAC

The wiki's two blockchain-integrated MEC sources — [[mao-2025-bcsa-frl]] and [[qin-2025-bcuav-masac]] — both bolt a permissioned blockchain onto an edge-compute system, but they attack *very different* problems with *very different* design philosophies. This page maps the two side-by-side so future readers (and future synthesis pages) don't conflate them.

## At-a-glance

| Aspect | [[mao-2025-bcsa-frl]] (BCSA-FRL) | [[qin-2025-bcuav-masac]] (BC-UAV-MASAC) |
|---|---|---|
| Edge platform | LEO satellites | UAVs over IoT terminals |
| Workload | Task offloading destination decisions | Joint sensing + offloading + trajectory + resource allocation |
| Why blockchain? | Substitute for trusted FL aggregator under [[zero-trust-architecture\|ZT]] | Tamper-proof audit trail of offload records |
| Consensus protocol | Group consensus (smart-contract voting) | DPoS for processor selection + PBFT for block finalization |
| Threat model centerpiece | Malicious voting + replay-buffer poisoning + parameter poisoning ([[fl-poisoning-attacks]]) | Privacy leakage + tamper / reverse of offloaded data |
| RL backbone | Per-satellite [[ddqn]] under FRL aggregation | Multi-agent [[masac]] (UAVs + terminals as agents) |
| Per-slot decomposition | None — full FRL round per aggregation | [[lyapunov-optimization\|Lyapunov]] decoupling → 3 sub-problems (CVX + MASAC + DOA) |
| Headline contribution | [[ccvm-correction-voting\|CCVM]] + [[csra-cold-start-reputation-aggregation\|CSRA]] mechanisms | AGIN-MASAC + DOA pipeline within Lyapunov framework |
| Headline result | Tolerates ~50% malicious satellites at flat ≈5% drop / ≈6 ms delay | +15.41% sensing rate / –30.73% queue delay vs MADDPG (vs PSO: +13.16% / –29.47%) |

## What each one actually solves

### BCSA-FRL — *trust at the consensus layer*

The problem: in a [[zero-trust-architecture|zero-trust]] LEO scenario, you can't designate a trusted aggregator for federated RL. Blockchain replaces the aggregator. But blockchain has its own attack surface: a malicious voter that always votes against the block can stall the entire system, regardless of how good the underlying ML is.

The novelty is two interlocking mechanisms:

- **[[ccvm-correction-voting|CCVM]]** down-weights consistent-negative voters, hardening the *consensus* layer.
- **[[csra-cold-start-reputation-aggregation|CSRA]]** sharply punishes just-attacked sub-models, then slowly recovers them in pace with replay-buffer cleaning — hardening the *aggregation* layer.

These are *security* mechanisms. The RL pipeline (DDQN under FedAvg-style FRL) is conventional. The blockchain is the protagonist.

### BC-UAV-MASAC — *audit + multi-objective optimization*

The problem: a UAV is offloading sensitive sensor data to terminals; the offload record needs to be tamper-evident and auditable for provenance. Blockchain provides this. *Separately*, the UAV is solving a hard joint optimization problem — sensing-rate maximization under long-term queue stability — that needs careful per-slot decomposition.

The novelty is the **optimization stack**:

- [[lyapunov-optimization|Lyapunov]] turns long-term constraints into per-slot virtual-queue penalties.
- The per-slot problem decomposes into:
  - CVX for sensing admission (convex sub-block).
  - [[masac|MASAC]] for transmission power + UAV trajectory (non-convex multi-agent sub-block).
  - DOA for resource allocation across compute + block generation + block verification.

The blockchain is treated as a *resource competitor* — block generation eats UAV CPU cycles that could have served compute tasks. The novelty is allocating that compute split adaptively, not the consensus mechanism itself.

## Where they agree

- **Permissioned blockchain over a small set of edge nodes**, not public chains. Both implicitly accept the latency / energy overhead of consensus as the price of tamper-evident records.
- **MEC compute and blockchain compute share the same hardware budget.** Both papers acknowledge this contention; BC-UAV-MASAC handles it explicitly via DOA, BCSA-FRL handles it implicitly by leaving the consensus rounds asynchronous to the FRL rounds.
- **[[zero-trust-architecture|Zero-trust]]-flavored framing**, even if BC-UAV-MASAC doesn't use the term. Both reject the assumption of a benevolent central server.
- **No real-hardware validation.** Simulation only. Both flag this as future work.

## Where they disagree (interesting tradeoff axes)

### 1. Where the blockchain bites

- **BCSA-FRL** bites at *aggregation time*. The consensus is what aggregates FL sub-models into a global model. Without consensus, no global model.
- **BC-UAV-MASAC** bites at *audit time*. The consensus records *what happened* after the fact. Without consensus, the system still functions; it just loses the audit trail.

Implication: BCSA-FRL is more vulnerable to consensus-layer attacks (which is why CCVM exists) but has less consensus-side latency overhead during normal operation (consensus is per-FL-round, not per-task).

### 2. Granularity of decision-making

- **BCSA-FRL** makes decisions at the *FL round* boundary — coarse, infrequent, but hardened by CCVM/CSRA.
- **BC-UAV-MASAC** makes decisions at the *time slot* boundary — fine, frequent, decomposed via Lyapunov.

If you're picking a pattern for a new system: BCSA-FRL's coarse-grained scheme works when the optimization variable changes slowly (offloading destinations don't churn millisecond-by-millisecond); BC-UAV-MASAC's fine-grained scheme is needed when sensing rate / trajectory / queue state churn fast.

### 3. RL action space

- **BCSA-FRL** — pure discrete (which satellite to offload to). DDQN is the natural choice.
- **BC-UAV-MASAC** — continuous (trajectory, power) plus discrete (block-processor participation). Multi-agent. MASAC is the natural choice.

This is actually downstream of what the blockchain does: the action space for "trust-aware offloading destination" is naturally categorical, while "joint sensing + trajectory + offloading + block resource" is naturally hybrid.

### 4. Failure modes

- **BCSA-FRL** breaks above 50% malicious majority (Byzantine consensus impossibility — no defense at the voting layer can survive this).
- **BC-UAV-MASAC** has no explicit malicious-actor model; its failure modes are non-convergence of the multi-agent learning loop and over-aggressive Lyapunov $V$ tuning that violates the long-term constraints.

In other words, BCSA-FRL has a **security failure curve** (graceful up to a threshold, then sudden), while BC-UAV-MASAC has a **performance failure curve** (degraded under bad hyperparameters, no security-induced cliff because security isn't its primary concern).

## Which one to learn from for which question

| If you care about… | Read this one first |
|---|---|
| Hardening FL aggregation against Byzantine voters | [[mao-2025-bcsa-frl]] — the CCVM/CSRA mechanism design is the lesson. |
| Reputation systems that handle slow recovery from poisoning | [[mao-2025-bcsa-frl]] — CSRA's hard-drop-then-slow-recovery is the lesson. |
| Decomposing a long-term-constrained MEC optimization | [[qin-2025-bcuav-masac]] — Lyapunov + multi-stage solver template. |
| Multi-agent SAC on UAV trajectory + power problems | [[qin-2025-bcuav-masac]] — AGIN-MASAC's CTDE setup is the lesson. |
| Coexistence of compute and blockchain workloads on a single node | [[qin-2025-bcuav-masac]] — explicit allocation across compute / block-gen / block-verify. |
| LEO-specific consensus over partially-connected satellite networks | [[mao-2025-bcsa-frl]] — coverage-time-aware consensus participation. |

## Composition opportunity

Nothing in either paper *prevents* combining them. A hypothetical follow-up:

- Take [[qin-2025-bcuav-masac]]'s Lyapunov-decomposed multi-objective MASAC pipeline.
- Insert [[ccvm-correction-voting|CCVM]] in the consensus layer to harden against malicious voters in the UAV swarm.
- Insert [[csra-cold-start-reputation-aggregation|CSRA]] for the per-UAV reputation that gates resource allocation.

This would address [[qin-2025-bcuav-masac]]'s gap (no explicit attacker model) by importing [[mao-2025-bcsa-frl]]'s defense layer wholesale. Whether the combined system's overhead remains within the per-slot Lyapunov budget is an open empirical question.

## Open questions surfaced by the comparison

- **What's the right granularity for blockchain consensus in MEC?** Per-FL-round (BCSA-FRL) is too coarse for fast-loop optimization; per-time-slot (implied by BC-UAV-MASAC) is probably too fine for energy budgets. Some intermediate "consensus on summary" pattern hasn't been proposed.
- **Is malicious-voting tolerance fundamental, or just one mechanism?** CCVM is one design; would Byzantine-fault-tolerant consensus families (HotStuff, Tendermint) handle this with no MEC-specific machinery? The corpus doesn't say.
- **How do these patterns extend to V2X / vehicular MEC?** Both papers target aerial/space MEC. Vehicular MEC has different mobility and trust assumptions (operators are usually fewer, but vehicles churn faster). Worth a curated source if one shows up.
