---
type: synthesis
title: "MADDPG vs MASAC in cooperative MEC: when entropy beats determinism"
tags: [synthesis, drl, multi-agent, mec, comparison]
related:
  - "[[qin-2025-bcuav-masac]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[masac]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[hybrid-action-decision-making]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
created: 2026-05-29
updated: 2026-05-30
---

# MADDPG vs MASAC in cooperative MEC: when entropy beats determinism

Both **MADDPG** (Multi-Agent Deep Deterministic Policy Gradient) and **[[masac|MASAC]]** (Multi-Agent Soft Actor-Critic) are off-policy actor-critic algorithms that follow the [[centralized-training-decentralized-execution|CTDE]] template — centralized critic at training time, decentralized actors at deployment. Both target cooperative continuous-action [[ma-pomdp]] problems, which is most of the multi-agent UAV-MEC corpus.

The choice between them looks like a tuning detail. The corpus says it isn't: where the two have been compared head-to-head, MASAC family methods consistently win, and the **mechanism** behind the win matters for which problems benefit.

## Working thesis

> For cooperative MEC problems with **multi-objective rewards**, **non-stationary peer policies**, and **non-trivial coordination equilibria** (which describes most of the curated UAV-MEC corpus), MASAC-family methods outperform MADDPG. The gap widens as agent count and reward-axis count grow.

Confidence: **medium**, based on direct evidence from 2 curated sources and indirect support from a 3rd. Would upgrade to **high** with a controlled ablation study or a third independent paper running both algorithms on the same MEC environment.

## Direct evidence from the curated corpus

### [[qin-2025-bcuav-masac]] — MASAC beats MADDPG on AGIN-MEC

Qin et al.'s ablation includes MADDPG as one of four benchmark methods. They explicitly call out MASAC's advantages:

- **Stable convergence** — SAC's entropy-regularized objective avoids the symmetric-policy collapse that MADDPG's deterministic actors fall into.
- **Better multi-objective handling** — the long-term sensing-rate / queue-delay / block-creation-delay reward stack gets noisier value estimates under MADDPG.
- **Faster wall-clock training** — a side-effect of avoiding the unstable deterministic-gradient regime; MADDPG took meaningfully longer to converge to a comparable utility level.

Their final results report improvements over MADDPG specifically: **+15.41% sensing rate and –30.73% queue delay vs MADDPG** at task data scale 8×10⁵ bit (the corresponding figures vs the PSO baseline are +13.16% / –29.47%). A non-trivial chunk of the gap is attributed to the MASAC choice over MADDPG.

### [[zhang-2025-ssac-mgi-heterogeneous-uav]] — SSAC beats MADDPG (and even vanilla MASAC) on heterogeneous UAVs

Zhang et al. compare against both vanilla MASAC and MADDPG. **SSAC** (Shared Soft Actor-Critic — a SAC-family variant with a shared encoder for common features and per-UAV heads for heterogeneous capabilities) wins on combined miss-rate × energy × safety.

Two readings of this result:

1. **Anti-MADDPG signal:** consistent with [[qin-2025-bcuav-masac]]'s finding that MADDPG's deterministic policies underperform on multi-objective UAV-MEC.
2. **Anti-vanilla-MASAC signal:** even within the SAC family, the choice of *how* to share parameters across heterogeneous agents matters. Vanilla MASAC's per-agent-fully-independent design wastes the structural commonality.

The first reading directly supports the working thesis. The second is an orthogonal point about heterogeneity (see [[heterogeneous-uav-fleet]]).

### [[zhang-2025-mcma-task-migration]] — backbone-agnostic two-stage framework

Zhang et al.'s MCMA framework is *compatible* with MADDPG, MAPPO, MATD3, Qmix, COMA, and other CTDE backbones — they don't pick a single one as the universal answer. They do, however, demonstrate two-stage decompositions that have a Q-style head for the discrete sub-decision and a policy-gradient head for the continuous sub-decision.

Reading the corpus together: this is consistent with "use MASAC family for the continuous head". The paper doesn't run a head-to-head MADDPG-vs-MASAC ablation, so it doesn't directly support or refute the thesis — but the design freedom they preserve is what would let a future user plug MASAC in.

### [[peng-2025-drudm-cfg]] — MA-DRL (unspecified backbone)

The DRUDM-CFG paper uses MA-DRL with the [[adaptive-entropy-priority-replay|AEP]] replay augmentation. AEP's entropy-priority signal *requires* a stochastic policy — so the paper implicitly sits in the SAC/PPO family, not MADDPG. Indirect support for "stochastic policies dominate in this design space" but not a direct ablation.

### [[liu-2026-jppo-en-convntm]] — single-agent, but informative on policy stochasticity

Liu et al.'s baselines are DDPG / TD3 / A2C / DQN — *not* MADDPG (single-agent setting). But the broader finding [[hybrid-action-beats-pure-drl]] — DDPG / TD3 lose to stochastic-policy alternatives — is the single-agent analog of the multi-agent claim made here. The mechanism is the same: deterministic policies starve at the action-space corners that matter for hybrid or multi-objective decisions.

## Why MASAC wins, mechanically

Three reasons converge:

### 1. Entropy bonus survives non-stationarity better

MADDPG's deterministic policies are sensitive to peer-policy churn — a small change in another agent's policy shifts your local gradient by an amount proportional to how *peaky* your own policy is. SAC's entropy bonus keeps the policy distribution wide; the same peer-policy change moves the gradient less violently. Concretely, in cooperative MEC where every agent is still learning, MADDPG's training trajectory wanders more.

### 2. Stochastic policies handle Pareto-frontier rewards better

Multi-objective MEC rewards (energy + delay + fairness + security) often have Pareto frontiers where the gradient vanishes locally. A deterministic policy parked on the frontier has no signal to refine. A stochastic policy keeps sampling near the frontier, accumulates differential reward across the sample, and gets a meaningful gradient.

### 3. Replay buffer + entropy = robust off-policy learning

MADDPG also uses a replay buffer, but the deterministic actor is more sensitive to off-policy distribution shift (the actor doesn't bracket the data distribution; the data was generated by a different deterministic policy whose support may have moved). MASAC's stochastic actor naturally maintains support, so the replay buffer's data is closer to on-distribution for longer.

## When MADDPG would still be the right pick

The thesis is not "always MASAC". MADDPG is *cheaper* per step (one Q net, one deterministic actor; no log-policy term) and is the right pick when:

- **Action distribution is genuinely unimodal.** If the optimal policy has zero entropy at convergence and the environment is near-stationary, the entropy bonus is wasted compute.
- **Sample efficiency matters more than stability.** MADDPG with TD3 fixes (twin Q, delayed updates, target-policy smoothing) is a strong combination on single-objective continuous-control problems with stable rewards.
- **Hyperparameter budget is severely limited.** SAC's auto-temperature mechanism removes one knob, but SAC still has more knobs total than DDPG (entropy target, twin-Q Polyak, etc.). For deployments where you can't afford a sweep, MADDPG is more forgiving of "default everything".
- **You're not actually in MA-POMDP.** If the system has true global state and a single decision-maker, plain SAC or PPO is a better starting point than either multi-agent variant.

In the curated corpus, none of these caveats applies — every multi-agent source is genuinely partially observable, multi-objective, and willing to spend hyperparameter budget. So the corpus's MASAC-favoring signal is consistent with the underlying problem class, not a coincidence.

## Composition and hybrids worth knowing

- **MATD3** — twin-Q, delayed update extension of MADDPG. Closer to MASAC on stability without the entropy bonus. Mentioned by [[zhang-2025-mcma-task-migration]] as a viable backbone in their two-stage framework.
- **MAPPO** — on-policy alternative; trades sample efficiency for the cleanest stability story (clipped trust region). Worth considering when the environment is fast to roll out and slow-to-converge MADDPG / MASAC are running into instability.
- **SSAC ([[zhang-2025-ssac-mgi-heterogeneous-uav]])** — shared-encoder SAC for heterogeneous fleets. Strict superset of vanilla MASAC under heterogeneity.
- **MASAC + classical sub-solver** ([[qin-2025-bcuav-masac]]'s pattern) — let MASAC handle the non-convex sub-block and a classical solver (KKT, CVX, swarm intelligence) handle the convex / combinatorial sub-blocks. This is the strongest pattern in the corpus.

## Practical recommendations

If you're building a cooperative MEC controller and choosing between MADDPG and MASAC:

1. **Default to MASAC** unless the action space is verifiably unimodal and the reward is single-objective.
2. **If your fleet is heterogeneous, default to a shared-encoder variant** (SSAC pattern) rather than vanilla MASAC.
3. **Don't put MASAC on every layer.** Use it only for the non-convex sub-block; keep convex / combinatorial sub-blocks on classical solvers (Lyapunov / KKT / matching) to reduce variance.
4. **Sanity check with a single-objective reduction.** If MASAC isn't beating MADDPG on a stripped-down single-objective version of your problem, the gap is unlikely to widen at full complexity — investigate the reward design before changing algorithm.
5. **Budget for entropy-target tuning.** Auto-temperature works most of the time, but the default target entropy is often too high for tight UAV trajectory problems and needs lowering.

## Open questions

- **MAPPO vs MASAC** — MAPPO is the on-policy stability story. The corpus has no head-to-head curated source. Worth tracking.
- **MATD3 vs MASAC at small agent count** — MATD3's twin-Q + delayed updates close most of the stability gap without the entropy machinery. Whether that's enough for cooperative MEC at U=2..3 agents is an empirical open question.
- **Mean-field MASAC** — none of the curated sources scale past ~10 agents. Beyond that, the centralized critic input dimension dominates training cost. Mean-field MARL or attention-factorized critics are the standard fixes; corpus has zero examples so far.
- **Does the entropy bonus help or hurt under [[fl-poisoning-attacks|poisoning]] / [[zero-trust-architecture|zero-trust]] threat models?** Wider exploration may make a malicious agent's bad samples harder to filter. Cross-pollinating this synthesis with [[bcsa-frl-vs-bc-uav-masac]]'s threat model would be the natural next step.

## How this synthesis would be promoted to high confidence

- A controlled study running MADDPG, MATD3, MASAC, and SSAC on the same MEC environment with matched hyperparameter budget.
- A third curated source independently reporting MASAC > MADDPG on a different MEC sub-problem (e.g. vehicular MEC, post-disaster, LEO offloading).
- Failure to refute on the natural counter-cases — single-objective, near-stationary, agent-count-2.

Until then, this stays at medium confidence and the practical recommendations above are the operating advice rather than a settled finding.
