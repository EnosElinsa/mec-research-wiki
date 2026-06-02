---
type: methodology
title: "The discrete-then-continuous two-stage decomposition protocol for joint offloading + resource problems"
tags: [methodology, decomposition, hybrid-action, matching, drl, classical-solver]
related:
  - "[[two-stage-decomposition]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[gale-shapley-matching]]"
  - "[[hybrid-action-decision-making]]"
  - "[[ao-sdr-sca-convex-pipeline]]"
  - "[[lyapunov-guided-drl]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[drl-vs-evolutionary-vs-classical-solvers]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[j-ppo-vs-pdqn]]"
  - "[[end-to-end-vs-decomposition-in-drl-mec]]"
created: 2026-06-04
updated: 2026-06-04
---

# The discrete-then-continuous two-stage decomposition protocol

A recurring solver protocol across the wiki's joint-offloading-plus-resource-allocation sources: split a coupled mixed-integer problem into a **discrete stage** (which device offloads, which server/UAV/satellite serves it, which task migrates where) and a **continuous stage** (transmit power, CPU allocation, offloading ratio, trajectory), and solve each with the tool its structure invites. Where the [[two-stage-decomposition]] concept page gives the short definition, this page captures the **engineering protocol**: how to partition the stages, the per-stage solver menu the corpus actually uses, how the stages exchange information, and when to reach for this template instead of solving the joint problem at once. It sits alongside the [[ao-sdr-sca-convex-pipeline]] (the classical convex track's protocol) and [[lyapunov-guided-drl]] (the temporal-decoupling protocol) as the third reusable solver scaffold the corpus converges on.

## The problem shape it fits

A joint optimization whose decision vector is **mixed-integer**: a combinatorial part (binary offload local-vs-remote, device-to-server association, task-migration target, server/satellite selection) entangled with a continuous part (power, bandwidth, compute split, offloading fraction, trajectory). The two parts are coupled — the best power allocation depends on who is served, and the best association depends on what power is available — so neither can be solved in isolation to global optimality. The joint problem is typically NP-hard or a non-convex MINLP. The corpus's two recurring observations make the split pay off:

- **The discrete decisions dominate the structure** (who goes where), while
- **the continuous decisions are conditionally convex / closed-form-ish given the discrete choice** (resource allocation given a fixed matching).

When both hold, freezing the discrete choice first and then solving a near-convex continuous residual loses some joint optimality but buys tractability, modularity, and interpretability.

## The two-stage protocol

### Stage 1 — the discrete/combinatorial decision

Decide the integer variables first, with a solver suited to combinatorial structure:

- **Matching theory** — many-to-one or Gale-Shapley-style association. [[wang-2026-aerial-marine-msar]]'s JCORA opens with a **many-to-one matching** for UAV→{HAPS, MASS} edge-server selection; [[nabi-2025-jour-hierarchical-aerial]]'s GOUA stage does **Gale-Shapley-inspired** GU-offloading + GU-UAV association.
- **Metaheuristic search** — when the binary block is too large for branch-and-bound but small enough for population search. [[jia-2025-dro-uav-hap-mec]] solves the binary offloading subproblem with [[binary-whale-optimization|BWOA]] after primal decomposition of its MISOCP.
- **A discrete-action policy head** — when the discrete choice recurs every slot at deployment and should be *learned*. [[zhang-2025-mcma-task-migration]] decides task-migration-assisted offloading with **MAPPO** (discrete action space).

### Stage 2 — the continuous resource decision

Conditioned on the Stage-1 choice (concatenated into the solver's input/observation), solve the now-near-convex continuous residual:

- **Convex / quasi-convex / projected-gradient** — [[wang-2026-aerial-marine-msar]] splits Stage II into quasi-convex transmit-power, PGD edge-compute allocation, and convex local-compute allocation; [[jia-2025-dro-uav-hap-mec]] uses CVX for its continuous resource block.
- **A continuous-action policy** — [[nabi-2025-jour-hierarchical-aerial]] hands the offloading-ratio + UAV-CPU + HAP-CPU allocation to an **enhanced SAC with [[prioritized-experience-replay|PER]]** (ESAC); [[zhang-2025-mcma-task-migration]] hands bandwidth + compute allocation to **MADDPG**, conditioned on the Stage-1 migration decision.

### The seam: how the stages exchange information

The protocol's one design choice that lives *between* the stages is how Stage 1's decision reaches Stage 2. The corpus uses two styles:

- **Frozen hand-off** (classical pipelines): Stage 1 is solved to completion, its output fixes the integer variables, and Stage 2 optimizes the continuous block over that fixed structure. [[wang-2026-aerial-marine-msar]] and [[jia-2025-dro-uav-hap-mec]] are frozen hand-offs — Stage 2 cannot push back on the matching/binary choice.
- **Conditioned observation** (DRL pipelines): the Stage-1 decision is concatenated into the Stage-2 agent's observation so the continuous policy adapts to it, and both stages are trained together under [[centralized-training-decentralized-execution|CTDE]]. [[zhang-2025-mcma-task-migration]] does exactly this — the MADDPG resource stage sees the MAPPO migration decision in its state.

## Why the stages compose well

- **Each stage's action space is homogeneous.** Splitting an all-discrete stage from an all-continuous stage means neither solver faces a mixed action space — which is precisely the difficulty that the *joint* hybrid-action family ([[liu-2026-jppo-en-convntm|j-PPO]], [[ma-2025-pdqn-vehicular-mec|P-DQN]]) builds special machinery to handle. [[zhang-2025-mcma-task-migration]] makes the point explicitly: the split "keeps each stage's action space homogeneous (all-discrete vs all-continuous), easing learning."
- **The right tool per block.** Matching is the natural solver for association; convex optimization is the natural solver for a conditionally-convex resource block; a learned policy is the natural solver for a per-slot recurring decision. The protocol lets each block use its own.
- **Interpretability and debugging.** Once decomposed, the association decision and the resource decision can be inspected and tuned independently — the [[end-to-end-vs-decomposition-in-drl-mec]] page lists this as one of the main reasons decomposition-based design dominates the corpus.

## Where it appears in the corpus

| Source | Stage 1 (discrete) | Stage 2 (continuous) | Seam |
|---|---|---|---|
| [[wang-2026-aerial-marine-msar]] | Many-to-one matching (UAV→HAPS/MASS) | Quasi-convex power + PGD edge-compute + convex local-compute | Frozen |
| [[nabi-2025-jour-hierarchical-aerial]] | Gale-Shapley GU-offload + GU-UAV association (GOUA) | ESAC (SAC + PER) over offloading ratio + UAV/HAP CPU | Frozen (classical Stage 1, learned Stage 2) |
| [[jia-2025-dro-uav-hap-mec]] | BWOA binary offloading (after primal decomposition) | CVX continuous resource allocation | Frozen |
| [[zhang-2025-mcma-task-migration]] | MAPPO migration-assisted offloading | MADDPG bandwidth + compute allocation | Conditioned observation (CTDE) |

The contrast case — the **joint hybrid-action** family that deliberately does *not* split — is [[liu-2026-jppo-en-convntm|j-PPO]] and [[ma-2025-pdqn-vehicular-mec|P-DQN]], which emit the discrete and continuous actions from one policy network in a single stage (compared head-to-head in [[j-ppo-vs-pdqn]]). Reading the two families together is what the [[drl-vs-evolutionary-vs-classical-solvers]] and [[drl-backbones-across-uav-mec-sources]] syntheses call the most portable scaffold in the corpus.

## Limitations

- **Loss of joint optimality.** The stage boundary is fixed before the continuous stage runs, so (in the frozen-hand-off style) the continuous stage cannot revise the discrete choice. The joint optimum is generally unreachable; the protocol trades it for tractability. **No curated source measures this gap** against a true joint solve on the same instance — the optimality cost is argued from structure, not quantified (a standing gap noted in [[drl-vs-evolutionary-vs-classical-solvers]]).
- **Recomputation cost is often unmodeled.** When Stage 1 is re-solved every slot as the topology changes (e.g. [[nabi-2025-jour-hierarchical-aerial]] recomputes GU-UAV association each interval as GUs move), the cost of repeated handoffs / re-matching is typically not charged in the objective.
- **The "discrete dominates, continuous conditionally convex" premise can fail.** The protocol's payoff rests on that structure; problems where the continuous block stays non-convex after fixing the integers (e.g. coupled trajectory + power under non-convex rate constraints) push back toward the [[ao-sdr-sca-convex-pipeline|AO + SDR + SCA]] template or a joint hybrid-action policy instead.

## See also

- [[two-stage-decomposition]] — the concept-level definition this protocol expands.
- [[ao-sdr-sca-convex-pipeline]] — the classical convex track's protocol (for coupled *continuous* blocks).
- [[lyapunov-guided-drl]] — the temporal-decoupling protocol (for *long-term* constraints over per-slot decisions).
- [[end-to-end-vs-decomposition-in-drl-mec]] — why decomposition-based design dominates the corpus.
- [[decomposition-beats-end-to-end-drl-in-mec]] — the thesis this protocol is the strongest evidence for.
