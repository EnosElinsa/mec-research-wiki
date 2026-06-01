---
type: methodology
title: "Lyapunov-guided DRL: decoupling long-term constraints from the per-slot learned policy"
tags: [methodology, lyapunov, drl, online-control, queue-stability]
related:
  - "[[lyapunov-optimization]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[zhou-2024-jdl-abs-postdisaster-rescue]]"
  - "[[gao-2024-sagin-perception-offloading]]"
  - "[[qin-2025-matd3-noma-queue-sagin]]"
  - "[[you-2025-uncertain-maritime-hasac]]"
  - "[[masac]]"
  - "[[ddpg]]"
  - "[[multi-agent-td3]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[two-timescale-optimization]]"
  - "[[safe-reinforcement-learning]]"
  - "[[collision-avoidance-mgi]]"
  - "[[safety-and-robustness-mechanisms-in-mec]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[drl-simulation-with-pomdp-formulation]]"
created: 2026-06-02
updated: 2026-06-02
---

# Lyapunov-guided DRL

A recurring solver protocol across the wiki's DRL sources: use [[lyapunov-optimization|Lyapunov drift-plus-penalty]] to strip the **long-term constraints** out of a stochastic MEC problem, then hand the residual **per-slot** decision to a learned policy. Where [[ao-sdr-sca-convex-pipeline]] captures the classical convex track's dominant template and [[drl-simulation-with-pomdp-formulation]] captures the single-source j-PPO simulation protocol, this page captures the **Lyapunov + DRL hybrid** that six curated sources converge on independently — the design pattern flagged as the corpus's best-supported cross-source methodology.

The [[lyapunov-optimization]] concept page covers the Neely-style mechanics (virtual queues, the $O(1/V)$–$O(V)$ tradeoff). This page is about the *engineering pattern* of bolting DRL onto that frame: why the two compose, what each side is responsible for, and how the corpus tunes the seam.

## The problem shape it fits

A **time-coupled stochastic** optimization — random task arrivals and time-varying channels, a per-slot decision (offloading, trajectory, power, resource split), and one or more **long-term average constraints**: queue stability, an average energy/flight-energy budget, an average delay cap. The coupling is the difficulty: the constraint spans the whole horizon, but the decision is made slot by slot with no future knowledge. A plain DRL agent must encode the long-term constraint into its reward (fragile), and a plain convex solver cannot react to the stochastic dynamics online.

## The two-layer protocol

### Layer 1 — Lyapunov strips the temporal coupling

Map each long-term constraint to a **virtual queue**, form the Lyapunov function over those queues, and at each slot minimize the **drift-plus-penalty** upper bound $\Delta L(\Theta(t)) - V\cdot f(t)$ (utility $f$, tradeoff weight $V$). This converts the horizon-spanning stochastic program into a sequence of **per-slot deterministic** problems whose solution provably keeps the queues stable — no future channel/arrival knowledge required. [[qin-2025-bcuav-masac]] does exactly this, introducing virtual queues for task-offloading, edge-computing, and block-creation-delay constraints and deriving the drift-plus-penalty bound with a balancing weight (the parse's $\lambda > 0$ "for balancing penalty minimization and queue stability").

### Layer 2 — DRL solves the per-slot residual

The per-slot problem is still non-convex (coupled trajectory + power + admission, hybrid action spaces, multi-agent interaction). This is where the learned policy enters: the DRL agent optimizes the per-slot drift-plus-penalty objective as its reward, while Layer 1's virtual queues — *not* the reward — carry the long-term feasibility. The corpus plugs in whichever backbone the action space demands (see [[drl-backbones-across-uav-mec-sources]]):

| Source | What Lyapunov decouples | Per-slot DRL backbone | Other per-slot solvers |
|---|---|---|---|
| [[qin-2025-bcuav-masac]] | queue-delay + block-creation-delay caps | [[masac\|MASAC]] (power + trajectory) | CVX (admission), DOA (resource split) |
| [[zhu-2025-lycnn-drl-wpt-mec]] | queue stability of a WPT-MEC system | CNN actor-critic (binary offloading) | golden-search + KKT/Lagrange (continuous sub) |
| [[zhou-2024-jdl-abs-postdisaster-rescue]] | long-term ABS flight-energy budget | actor DNN (ABS-GU association) | **SCA inside the critic** (trajectory + offloading) |
| [[gao-2024-sagin-perception-offloading]] | task-queue stability across tiers | [[ddpg\|DDPG]] (offloading) + DQN (association) | SGHS metaheuristic (BS resource) |
| [[qin-2025-matd3-noma-queue-sagin]] | queue-delay coupling in a NOMA SAGIN | [[multi-agent-td3\|MATD3]] (trajectory + offloading) | CVX + GSCRA |
| [[you-2025-uncertain-maritime-hasac]] | long-term constraints under uncertain arrivals | heterogeneous-agent SAC (Markov game) | — |

## Why the two compose well

- **Separation of concerns.** Lyapunov owns *feasibility over time*; DRL owns *quality within a slot*. Each is doing what it is good at, and the seam is clean — the agent never has to learn the long-term constraint, only to optimize a slot.
- **No future knowledge.** Both layers are online by construction: drift-plus-penalty needs only the current queue backlogs, and the policy needs only the current observation.
- **The per-slot problem is small.** [[you-2025-uncertain-maritime-hasac]] makes the point explicitly — Lyapunov "yields small-scale problems" per slot, which is what makes a heterogeneous-agent learner tractable. [[zhu-2025-lycnn-drl-wpt-mec]] reports its Lyapunov-guided CNN actor matching the classical iterative solver's utility (>97%) at roughly two orders of magnitude lower latency, because the per-slot residual is cheap once the temporal coupling is gone.

## The seam: tuning V (and what the corpus shows)

The $V$ weight is the one knob that lives *between* the two layers — it sets how aggressively the per-slot reward (which the DRL agent maximizes) is traded against queue growth (which Lyapunov bounds). Larger $V$ chases utility at the cost of longer backlogs; smaller $V$ keeps queues short but leaves utility on the table — the standard $O(1/V)$ violation / $O(V)$ optimality-gap tradeoff. [[gao-2024-sagin-perception-offloading]]'s drift-plus-penalty objective carries this $V$ explicitly as the balancing parameter, and the classical-solver sibling [[zhao-2025-traj-offload-cache-migration]] shows the queue-backlog-vs-throughput sweep directly (larger $V$ lowers throughput and grows backlog, stabilizing within $[O(1/V), O(V)]$). The practical implication for a Lyapunov-guided DRL design: $V$ is set *outside* the policy, so retuning the optimality–stability balance does **not** require retraining the agent — a deployment advantage over folding the constraint into a reward weight.

## Why not just shape the reward?

The alternative is to add the long-term constraint as a penalty term in the DRL reward. The corpus's Lyapunov-guided sources implicitly reject this, and the reasoning generalizes: a reward penalty gives only a soft, untunable, *average-case* nudge with no stability guarantee, whereas the virtual queue gives a provable time-average bound and a clean $V$ knob. This is the queue-stability analog of the safety argument that [[zhang-2025-ssac-mgi-heterogeneous-uav]]'s [[collision-avoidance-mgi|MGI]] makes for hard safety constraints — in both cases an explicit constraint-handling mechanism beats baking the constraint into the reward (the cross-family view is in [[safety-and-robustness-mechanisms-in-mec]]). The cross-source recommendation distilled in [[drl-backbones-across-uav-mec-sources]] — "use Lyapunov for long-term constraints, not reward shaping" — is exactly this pattern.

## Variations worth noting

- **SCA-in-the-critic.** [[zhou-2024-jdl-abs-postdisaster-rescue]] is the unusual one: instead of a model-free value network, its critic *analytically* solves the trajectory + offloading subproblem via SCA, so the learned actor only handles the discrete association. It is a Lyapunov + DRL + convex three-way hybrid.
- **Two-timescale split.** [[zhou-2024-jdl-abs-postdisaster-rescue]] also runs trajectory planning on a large timescale and offloading on a small one ([[two-timescale-optimization]]) — a second decoupling layered on top of Lyapunov's temporal one.
- **Objective reshaping before Lyapunov.** [[zhu-2025-lycnn-drl-wpt-mec]] first linearizes a fractional energy-efficiency objective via [[fractional-programming-dinkelbach|Dinkelbach]], *then* applies Lyapunov, *then* learns — fractional programming and Lyapunov are orthogonal transforms that stack.
- **Metaheuristic per-slot helper.** [[gao-2024-sagin-perception-offloading]] and [[qin-2025-bcuav-masac]] both keep a cheap swarm/heuristic solver (SGHS, DOA) for one per-slot sub-block alongside the DRL agent — DRL is not asked to learn every variable.

## Limitations

- **Stability is asymptotic.** The $O(1/V)$–$O(V)$ guarantee is a time-average statement; transient backlog can be large, and the learned policy can still misbehave within a slot.
- **Guarantee is on the queue, not the policy.** Lyapunov bounds constraint violation regardless of the policy's quality, but a poorly trained agent still yields poor *utility* — the feasibility guarantee does not rescue a bad reward.
- **Queue modeling is an assumption.** Every source models the long-term constraint as a stable queue; constraints that do not admit a virtual-queue form (e.g. hard per-slot safety) need a different mechanism such as [[collision-avoidance-mgi|MGI]] or robust optimization (see [[safety-and-robustness-mechanisms-in-mec]]).
- **No head-to-head on V-tuning.** No curated source compares learned-policy performance across a $V$ sweep against a reward-penalty-weight sweep on the same problem, so the "tune $V$ without retraining" advantage is structural rather than empirically benchmarked here.
