---
type: comparison
title: "CTDE actor-critic backbones in cooperative MEC: MADDPG vs MATD3 vs MASAC vs MAPPO vs value-based"
tags: [comparison, drl, multi-agent, ctde, actor-critic, mec]
related:
  - "[[centralized-training-decentralized-execution]]"
  - "[[maddpg]]"
  - "[[multi-agent-td3]]"
  - "[[masac]]"
  - "[[mappo]]"
  - "[[multi-agent-q-learning]]"
  - "[[value-decomposition-network]]"
  - "[[ma-pomdp]]"
  - "[[seid-2021-madrl-multiuav-iot-edge]]"
  - "[[wang-2021-maddpg-multiuav-trajectory]]"
  - "[[peng-2020-maddpg-uav-vehicular]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[du-2023-maddpg-service-placement-agin]]"
  - "[[zhao-2022-matd3-multiuav-ec-offloading]]"
  - "[[shao-2024-drl-antijamming-mec]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[kang-2023-mappo-hierarchical-aerial]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
  - "[[raivi-2024-jdaco-postdisaster-iot]]"
  - "[[maddpg-vs-masac-in-mec]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
created: 2026-06-03
updated: 2026-06-03
---

# CTDE actor-critic backbones in cooperative MEC: MADDPG vs MATD3 vs MASAC vs MAPPO vs value-based

A large slice of the corpus solves cooperative multi-agent MEC under **[[centralized-training-decentralized-execution|centralized training, decentralized execution]] (CTDE)** — a centralized critic that sees joint observations/actions at training time, decentralized actors that run on local observations at deployment. Within that shared paradigm, the sources reach for different multi-agent backbones, and the choice is governed by the action space, the policy class (deterministic vs stochastic vs on-policy vs value-based), and whether the problem has a game-theoretic structure worth exploiting.

This page maps which backbone each source picks and why. It is the **family-wide** companion to the two-way [[maddpg-vs-masac-in-mec]] thesis (which argues *when entropy beats determinism* between exactly those two) and the [[drl-backbones-across-uav-mec-sources]] synthesis (which analyzes a different, mostly single-agent 2025–2026 DRL roster). The roster here is the corpus's **explicitly multi-agent** actor-critic / value-based cluster.

## Roster

| Source | Venue / year | Backbone | Policy class | Agent = | Action space |
|---|---|---|---|---|---|
| [[seid-2021-madrl-multiuav-iot-edge]] | TNSM 2021 | [[maddpg|MADDPG]] | Deterministic | per-UAV (cluster head) | Continuous (offload + resource) |
| [[peng-2020-maddpg-uav-vehicular]] | JSAC 2020 | [[maddpg|MADDPG]] | Deterministic | per-MEC-server (eNodeB + UAV) | Vehicle association + resource allocation |
| [[wang-2021-maddpg-multiuav-trajectory]] | TCCN 2021 | [[maddpg|MADDPG]] | Deterministic | per-UAV | Continuous trajectory (+ separate low-complexity offloading step) |
| [[he-2023-fairness-3d-multiuav-maddpg]] | — 2023 | [[maddpg|MADDPG]] | Deterministic | per-UAV | 3D trajectory (fairness objective) |
| [[du-2023-maddpg-service-placement-agin]] | — 2023 | [[maddpg|MADDPG]] | Deterministic | per-node | Service placement + offloading (air-ground) |
| [[zhao-2022-matd3-multiuav-ec-offloading]] | TWC 2022 | [[multi-agent-td3|MATD3]] | Deterministic (twin-Q, delayed) | per-UAV | High-dim continuous (trajectory + offloading) |
| [[shao-2024-drl-antijamming-mec]] | TMC 2024 | [[multi-agent-td3|PER-MATD3]] | Deterministic + [[prioritized-experience-replay|PER]] | per-UAV | CPU freq + bandwidth + channel selection (under jamming) |
| [[qin-2025-bcuav-masac]] | TWC 2025 | [[masac|MASAC]] | Stochastic (max-entropy) | per-UAV, per-terminal | Continuous trajectory + power (+ DOA for resources) |
| [[kang-2023-mappo-hierarchical-aerial]] | JIOT 2023 | [[mappo|MAPPO]] | On-policy (clipped) | per-agent | GD-association + resource + UAV→HAP offloading |
| [[li-2025-stochastic-game-uav-swarm]] | TGCN 2025 | [[multi-agent-q-learning|tabular MA-Q (RLDC)]] | Value-based + Q-sharing | per-UAV (dynamic cluster) | Discrete clustering + scheduling |
| [[raivi-2024-jdaco-postdisaster-iot]] | JIOT 2024 | [[value-decomposition-network|VD3QN]] (VDN + dueling-double-DQN) | Value-based + value decomposition | per-UAV | Discrete (energy + delay + IoT coverage) |

## The four policy classes, and what each is chosen for

### Deterministic actor-critic (MADDPG) — the default baseline

MADDPG is the **earliest and most common** CTDE backbone in the corpus: five sources span 2020–2023 ([[peng-2020-maddpg-uav-vehicular]], [[wang-2021-maddpg-multiuav-trajectory]], [[seid-2021-madrl-multiuav-iot-edge]], [[he-2023-fairness-3d-multiuav-maddpg]], [[du-2023-maddpg-service-placement-agin]]). It fits because multi-UAV trajectory + offloading + resource decisions are **coupled across agents but executed on local observations** ([[ma-pomdp]]), and the centralized critic resolves the non-stationarity of independent learners while keeping execution decentralized. Two recurring design choices: one agent per UAV (or per MEC server), and frequent pairing with a **separate low-complexity offloading step** ([[wang-2021-maddpg-multiuav-trajectory]] decomposes trajectory-then-offloading) rather than folding everything into one action vector.

### Twin-delayed deterministic (MATD3) — MADDPG with the overestimation fixes

[[zhao-2022-matd3-multiuav-ec-offloading]] and [[shao-2024-drl-antijamming-mec]] use MATD3, which adds TD3's **clipped double-Q, delayed actor updates, and target-policy smoothing** to curb the value-overestimation that destabilizes plain MADDPG on high-dimensional continuous actions. [[shao-2024-drl-antijamming-mec]]'s **PER-MATD3** further adds [[prioritized-experience-replay|prioritized replay]] and argues convergence via clipped double-Q even under adversarial jamming. MATD3 is the corpus's answer to "MADDPG is unstable but I don't want the entropy machinery."

### Stochastic max-entropy (MASAC) — when exploration and multi-objective rewards matter

[[qin-2025-bcuav-masac]] picks MASAC over MADDPG explicitly, reporting **+15.41% sensing rate and −30.73% queue delay vs MADDPG** at task data scale 8×10⁵ bit (verbatim; the corresponding figures vs the PSO baseline are +13.16% / −29.47% — a distinction the [[maddpg-vs-masac-in-mec]] thesis is careful about). The entropy bonus keeps exploration alive on a multi-objective sensing/queue/block-delay reward where deterministic policies collapse onto suboptimal coordination equilibria. This is the single direct head-to-head in the corpus and the empirical core of the [[maddpg-vs-masac-in-mec]] thesis.

### On-policy clipped (MAPPO) — stability over sample efficiency

[[kang-2023-mappo-hierarchical-aerial]] uses MAPPO for the joint GD-association / resource-allocation / UAV→HAP offloading POMDP, adding **state normalization and action masking** to speed training. MAPPO trades the sample efficiency of off-policy replay for PPO's trust-region-style stability — the right call when rollouts are cheap and off-policy backbones run into instability.

### Value-based (MA-Q-learning, value decomposition) — discrete actions and game structure

Two sources leave the actor-critic family entirely. [[li-2025-stochastic-game-uav-swarm]]'s **RLDC** is tabular multi-agent Q-learning with periodic Q-value sharing over a control channel, and proves convergence to a [[nash-equilibrium]] of the underlying [[stochastic-game]] via contraction mapping — classical RL married to equilibrium analysis, suited to discrete clustering/scheduling. [[raivi-2024-jdaco-postdisaster-iot]]'s **VD3QN** combines a [[value-decomposition-network|VDN]] with dueling-double-DQN so cooperative agents learn a decomposable joint value for a discrete energy/delay/coverage objective. Both fit **discrete** action spaces where a deterministic or stochastic *continuous* actor has nothing to parameterize.

## How to choose: the discriminating features

| If the problem is… | Lean toward | Why |
|---|---|---|
| Continuous joint control, stable single-objective-ish reward, limited tuning budget | **MADDPG** | Cheapest CTDE backbone; one critic, one deterministic actor; the corpus default |
| Continuous control but MADDPG is overestimating / unstable | **MATD3 (+ PER)** | Twin-Q + delayed updates curb overestimation without the entropy machinery |
| Continuous control, multi-objective reward, non-stationary peers, coordination equilibria | **MASAC** | Entropy bonus survives peer-policy churn and keeps gradient signal near Pareto fronts ([[maddpg-vs-masac-in-mec]]) |
| Rollouts cheap, off-policy backbones unstable, on-policy reasoning preferred | **MAPPO** | Clipped trust region gives the cleanest stability story |
| Discrete actions with exploitable game structure | **MA-Q-learning** | Equilibrium convergence guarantees via the game's structure ([[li-2025-stochastic-game-uav-swarm]]) |
| Fully cooperative discrete actions needing joint-value credit assignment | **Value decomposition (VDN / VD3QN)** | Decomposes a shared team value into per-agent contributions ([[raivi-2024-jdaco-postdisaster-iot]]) |

## Cross-cutting observations

1. **Deterministic-to-stochastic drift over time.** The MADDPG cluster is 2020–2023; the MASAC head-to-head win is 2025. The corpus's own trajectory mirrors the broader MARL field's shift toward entropy-regularized policies for cooperative continuous control — but note this is partly a **recency** effect, not a controlled comparison.
2. **One direct head-to-head, the rest are within-backbone.** Only [[qin-2025-bcuav-masac]] runs MADDPG and MASAC on the *same* instance. Every other source benchmarks its chosen backbone against non-CTDE baselines (heuristics, single-agent DRL, PSO), so the family ranking is assembled across papers, not measured on one bench.
3. **CTDE's scaling ceiling is unaddressed.** The [[centralized-training-decentralized-execution]] page notes the centralized critic's input dimension grows with agent count; none of these sources operates past ~10 cooperating agents, and none uses mean-field or attention-factorized critics. The dense (20+ agent) regime — where [[value-decomposition-network|value decomposition]]'s advantage is largest — is empty.
4. **Decomposition pairs with every backbone.** MADDPG with a separate offloading step, MASAC with a Lyapunov front-end + DOA sub-solver, MAPPO with action masking — the CTDE backbone almost never carries the whole problem alone.

## Gaps

- **No MAPPO-vs-MASAC head-to-head** — the on-policy-stability vs off-policy-sample-efficiency tradeoff is argued by problem shape, never measured on one instance (the standing open question in [[maddpg-vs-masac-in-mec]]).
- **No MATD3-vs-MASAC at small agent count** — whether MATD3's twin-Q + delayed updates close the stability gap without entropy at U=2–3 agents is untested.
- **No mean-field / attention-factorized critic** — the scaling fix for dense fleets has zero corpus examples.
- **Federated single-agent is a different animal.** [[mao-2025-bcsa-frl]] aggregates per-satellite DQN *parameters* rather than using a centralized critic — it is FRL, not CTDE MA-DRL, and is deliberately excluded from this roster.

## See also

- [[maddpg-vs-masac-in-mec]] — the two-way "when entropy beats determinism" thesis this page generalizes.
- [[drl-backbones-across-uav-mec-sources]] — the broader (mostly single-agent, 2025–2026) DRL-backbone map.
- [[centralized-training-decentralized-execution]] — the paradigm all rostered backbones share.
- [[game-theoretic-offloading-formulations]] — where [[li-2025-stochastic-game-uav-swarm]]'s learned-equilibrium backbone connects to the game-theory track.
