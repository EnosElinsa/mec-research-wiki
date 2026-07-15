---
type: comparison
title: "UAV trajectory safety guarantee ladder"
tags: [comparison, uav, trajectory, safety, robustness, guarantees]
related:
  - "[[zhang-2021-safe-dqn-emergency]]"
  - "[[hsu-2022-collision-avoidance-trajectory]]"
  - "[[hua-2026-unpredictable-uav-trajectory]]"
  - "[[jia-2026-dro-lawn-trajectory]]"
  - "[[gong-2026-safe-economic-lae-trajectory]]"
  - "[[wang-2026-robust-multiuav-jtcra]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[li-2024-robust-bmappo-multiuav-mec]]"
  - "[[safe-reinforcement-learning]]"
  - "[[distributionally-robust-optimization]]"
  - "[[collision-avoidance-mgi]]"
  - "[[robust-offloading]]"
  - "[[safety-and-robustness-mechanisms-in-mec]]"
  - "[[explicit-constraints-beat-reward-shaping-in-mec-drl]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV trajectory safety guarantee ladder

## Protected object and meaning of guarantee

“Safety” in these sources names different protected objects. A collision-free simulator episode is not an expected-cost bound; an expected-cost bound is not a sample-path shield; a distributionally robust delay objective is not a flight-safety result; and service continuity after an energy failure is not collision avoidance. The ladder therefore orders enforcement and evidence scope, not papers by one numerical safety score.

## Hazard, enforcement, persistence, and evidence matrix

| Source | Protected object | Hazard / uncertainty | Enforcement locus | Training / deployment persistence | Proof scope | Evaluation evidence | Caveat |
|---|---|---|---|---|---|---|---|
| [[zhang-2021-safe-dqn-emergency]] | Ground-user cumulative energy and obstacle-free next position | Long-term UE energy; modeled circular obstacles | Lyapunov safe-policy inequality plus legal-action next-point filter | Safe-policy calculation and filter are used at action selection; neural approximations remain deployment artifacts | Expected cumulative cost for the surrogate CMDP; no sample-path or global-optimality proof | Numerical throughput, energy-efficiency, and obstacle-avoidance comparisons | The sum-of-per-slot maxima is a sufficient surrogate; the filter does not test continuous segment intersection |
| [[hsu-2022-collision-avoidance-trajectory]] | Inter-UAV separation while following a data-collection route | Locally sensed neighboring UAVs and obstacles | Distributed tabular Q-learning reward penalty and a fallback altitude rule | Offline table training, then online lookup | No formal collision-safety theorem | Ten-network simulator success probability and trajectory figures | At most two obstacles are represented in one state; success is simulator evidence |
| [[hua-2026-unpredictable-uav-trajectory]] | Mission progress and jammer-prediction difficulty | Mobile-jammer interference and trajectory predictability | Navigation MPC plus stochastic heading input | Slotwise controller; random input is disabled near the endpoint | Component bounds and local optimization statements, not end-to-end security or every-realization feasibility | One-step Kalman prediction-error and data-collection simulations | Gaussian stochastic input has unbounded support although finite component bounds are stated |
| [[gong-2026-safe-economic-lae-trajectory]] | Obstacles, no-fly zones, residential-zone compliance, landing, and energy | Partially observed urban obstacles and regulations | SAC reward terms with conditional LLM guidance during training | LLM is removed after training; SAC alone executes online | No formal guarantee from the LLM path; reported claims are algorithm/evaluation scope | Multi-scenario simulation with collision, violation, landing, data, and energy metrics | Near-zero rates are tested-simulator results, not universal safety bounds |
| [[zhang-2025-ssac-mgi-heterogeneous-uav]] | UAV-UAV and static-obstacle separation | Other UAVs and static obstacles under local observations | Per-UAV Safety Agent and binary Markov-Game-of-Intervention gate | Gate can override the Standard Agent during and after training | The paper reports a fixed-point/Q-learning result inherited from reference [37] under its approximation conditions; this is not a neural SSAC-MGI collision-freedom proof | Real-trace-driven simulations and safety-cost comparisons | The conclusion scopes any absolute-safety claim to real-time perception and online fine-tuning assumptions |
| [[jia-2026-dro-lawn-trajectory]] | Worst expected computation delay under task-size distributions | Unknown task-size distribution near historical data | DRO ambiguity sets (L1, L-infinity, Fortet-Mourier) with BD/SCA trajectory/offloading solver | Classical optimization at planning time; no learned deployment shield | Robust objective over the declared ambiguity set, not physical collision safety | Delay, energy, distribution-shift, and runtime simulations | Distributional robustness concerns task sizes; it does not transfer to obstacle or collision hazards |
| [[li-2024-robust-bmappo-multiuav-mec]] | Energy/delay under communication and computation errors | Bounded CSI and task-complexity estimation errors | Robust delay reformulation plus bounded-support Beta-policy MAPPO; collision/out-of-region terms remain penalties | Learned policy executes after training; no runtime projection enforces the robust delay constraints | Robust delay constraints hold within declared error bounds in the reformulation; no learned-policy worst-case or collision-safety proof | Numerical convergence and bounded-error sensitivity simulations | The robust object is CSI/task complexity, not trajectory collision safety |
| [[wang-2026-robust-multiuav-jtcra]] | Ground-user service continuity and fairness | UAV energy depletion and resulting coverage gaps | Dual trajectory/communication agents reassign coverage in the learned policy | Failure response is learned before deployment and executed without iterative re-optimization | No collision or physical-flight safety proof | Simulation trajectories, throughput, fairness, and energy results | Continuity is a service-level property, not a geometric safety guarantee |
| [[qi-2026-ocma-ddqn-data-collection]] | Grid data collection under intermittent cooperation | Directional jamming, obstacles, and short communication outages | Distance-conditioned exchange, DDQN collision/NFZ penalty plus return-to-current-cell reset, and LSTM neighbor-action prediction | Distributed inference; short-outage predictor adapts within an episode | Potential-game equilibrium and short-horizon predictor claims only | Up-to-four-UAV grid simulations | The discrete invalid-move reset does not certify continuous-flight or sample-path safety; long outages remain outside evidence |
| [[yin-2026-uav-antijamming-nfsp]] | Uplink communication against a learning jammer | Hidden opponent state and non-stationary pursuit-evasion | Neural fictitious self-play, recurrent history, and dueling double Q-learning | Independent policies adapt from local histories | No new proof for the complete recurrent architecture | One-UAV/one-jammer simulations | Anti-jamming adaptation is not a collision or secrecy guarantee |
| [[li-2026-full-duplex-noma-uav-relay]] | Rate and relay-ordering chance constraints | Gaussian UAV-position error | Bernstein safe approximation with SCA/BCD | Classical position/power optimization | Sufficient probabilistic feasibility for declared chance constraints | Numerical reliability margins and rate simulations | Static relay deployment and inactive tested constraint do not establish trajectory safety |

## Accepted cross-links

The reciprocal links below are mechanism-specific comparisons. Each sentence states what is shared and what must not be transferred.

| Pair | Mechanism-specific relation and boundary |
|---|---|
| [[zhang-2021-safe-dqn-emergency]] ↔ [[hsu-2022-collision-avoidance-trajectory]] | Expected surrogate plus next-point legality versus local tabular heading lookup; neither supplies the other's guarantee. |
| [[zhang-2021-safe-dqn-emergency]] ↔ [[distributed-tabular-q-learning-uav-collision-avoidance]] | Action-time expected-cost/legal filtering versus offline-learned online lookup; Hsu remains empirical collision evidence. |
| [[zhang-2021-safe-dqn-emergency]] ↔ [[navigation-stochastic-control-decomposition]] | Zhang separates expected UE-energy admissibility and next-point legality from mission reward; Hua separates navigation from a current-geometry stochastic anti-prediction input. Hua's Gaussian term is unbounded, and no guarantee transfers. |
| [[zhang-2021-safe-dqn-emergency]] ↔ [[connectivity-preserving-uav-behavioral-loss]] | Action admissibility at execution versus training-time pressure after total base-station-link loss; topology is outside Zhang's model. |
| [[hsu-2022-collision-avoidance-trajectory]] ↔ [[hua-2026-unpredictable-uav-trajectory]] | Planned route plus sensed encounter deviation versus navigation plus stochastic heading; no collision/security transfer. |
| [[hsu-2022-collision-avoidance-trajectory]] ↔ [[unpredictable-uav-trajectory-control]] | Local deterministic collision response versus deliberate anti-prediction perturbation; both are evidence-limited. |
| [[hsu-2022-collision-avoidance-trajectory]] ↔ [[navigation-stochastic-control-decomposition]] | Mission-directed route plus local modifier in both designs; Hsu is simulated and Hua's stated Gaussian bounds remain unresolved. |
| [[hsu-2022-collision-avoidance-trajectory]] ↔ [[qi-2026-ocma-ddqn-data-collection]] | Decentralized discrete data-collection navigation, with tabular sensing in Hsu and DDQN map/experience exchange in Qi; both collision results are simulation-only. |
| [[distributed-tabular-q-learning-uav-collision-avoidance]] ↔ [[opportunistic-cooperative-multi-uav-ddqn]] | Decentralized discrete Q control versus opportunistic map/replay exchange and short-outage prediction; no scalability or safety theorem follows. |
| [[distributed-tabular-q-learning-uav-collision-avoidance]] ↔ [[connectivity-preserving-uav-behavioral-loss]] | Deployed local action lookup versus disconnection-triggered training loss; neither guarantees collision or restored connectivity. |
| [[convex-tsp-uav-data-collection]] ↔ [[navigation-stochastic-control-decomposition]] | Nominal route optimization versus mission/stochastic heading decomposition; no joint global optimum is claimed. |
| [[hua-2026-unpredictable-uav-trajectory]] ↔ [[qi-2026-ocma-ddqn-data-collection]] | Mobile-pursuer stochastic path versus episode-static jammer and intermittent-link predictor; no anti-jamming guarantee transfers. |
| [[unpredictable-uav-trajectory-control]] ↔ [[yin-2026-uav-antijamming-nfsp]] | Known current jammer geometry plus random input versus hidden-state recurrent opponent modeling; neither is a security proof. |
| [[unpredictable-uav-trajectory-control]] ↔ [[implicit-opponent-modeling]] | Current-geometry randomized control versus history-conditioned adaptation; the information mechanisms protect different objects. |
| [[navigation-stochastic-control-decomposition]] ↔ [[implicit-opponent-modeling]] | Current-geometry stochastic mean versus historical greedy/average-policy mixture; do not call either a security guarantee. |
| [[qi-2026-ocma-ddqn-data-collection]] ↔ [[yin-2026-uav-antijamming-nfsp]] | Episode-static directional jammers and outage prediction versus an adaptive mobile opponent; both are simulation-only. |
| [[qi-2026-ocma-ddqn-data-collection]] ↔ [[connectivity-preserving-uav-behavioral-loss]] | Short-outage neighbor imputation versus post-disconnection base-station steering; prediction is not a topology guarantee. |
| [[opportunistic-cooperative-multi-uav-ddqn]] ↔ [[connectivity-preserving-uav-behavioral-loss]] | Opportunistic experience exchange plus confidence-filtered outage prediction versus disconnection-triggered behavioral shaping; evidence remains grid simulation. |
| [[bernstein-safe-approximation]] ↔ [[zhang-2021-safe-dqn-emergency]] | Sufficient Gaussian chance-constraint feasibility versus expected conservative surrogate cost after learned approximation; neither is a universal collision guarantee. |
| [[bernstein-safe-approximation]] ↔ [[distributed-tabular-q-learning-uav-collision-avoidance]] | Formal probability sufficiency under a declared Gaussian model versus empirical reward-shaped avoidance; Bernstein does not certify collisions. |

## Deferred edges

Three plausible-looking links were deliberately not accepted. [[zhang-2021-safe-dqn-emergency]] ↔ [[hua-2026-unpredictable-uav-trajectory]] collapses distinct hazards and duplicates the navigation-decomposition bridge. [[zhang-2021-safe-dqn-emergency]] ↔ [[multi-hop-uav-emergency-networking]] shares only an emergency setting and has no common protected object or enforcement locus. [[li-2026-full-duplex-noma-uav-relay]] ↔ [[zhang-2021-safe-dqn-emergency]] compares static relay rate chance constraints with moving emergency trajectory control, so the legitimate Bernstein bridge is kept at the concept level instead.

## Empirical reward-shaped avoidance

[[hsu-2022-collision-avoidance-trajectory]] learns local avoidance from reward penalties. [[qi-2026-ocma-ddqn-data-collection]] also penalizes collision/no-fly-zone actions, but its grid simulator deterministically returns an invalid move to the current cell. That discrete transition reset is stronger than a penalty alone while still not certifying continuous flight or sample-path safety. [[distributed-tabular-q-learning-uav-collision-avoidance]] therefore remains an empirical collision-avoidance mechanism, and neither source's simulator result transfers to a different hazard or flight model.

## Action filtering and constraint-aware policies

[[zhang-2021-safe-dqn-emergency]] combines an expected-cost Lyapunov policy set with a separate legal-action filter. The first constrains a long-horizon surrogate; the second rejects a next position inside the obstacle set. These are distinct loci and should not be collapsed into a universal geometric shield. [[navigation-stochastic-control-decomposition]] and [[convex-tsp-uav-data-collection]] provide planning decompositions around mission progress, not a new safety proof.

## Persistent intervention and shielding

[[zhang-2025-ssac-mgi-heterogeneous-uav]] is the strongest explicit intervention rung in this set: a Safety Agent can override the Standard Agent through a binary gate, and its intervention policy is optimized separately from mission reward. [[collision-avoidance-mgi]] and [[safe-reinforcement-learning]] document that separation. The persistence claim is about the MGI controller under its model; it cannot be transferred to reward-shaped Hsu/Qi policies, training-time LLM guidance, or a different hazard.

## Bounded and distributional robustness

[[li-2024-robust-bmappo-multiuav-mec]] handles bounded CSI and task-complexity errors with a robust reformulation and a Beta-policy actor. [[jia-2026-dro-lawn-trajectory]] instead optimizes worst expected delay over ambiguity sets for task-size distributions. [[distributionally-robust-optimization]] is the shared optimization vocabulary, not a shared guarantee: bounded error sets, distributional ambiguity, and geometric collision sets protect different objects. [[robust-offloading]] keeps the Li source's bounded-error scope explicit, while [[bernstein-safe-approximation]] gives a separate sufficient chance-constraint construction for relay position error.

## Unpredictability and service continuity

[[hua-2026-unpredictable-uav-trajectory]] uses stochastic control to make short-horizon motion harder to predict while preserving collection and endpoint progress. [[unpredictable-uav-trajectory-control]], [[yin-2026-uav-antijamming-nfsp]], and [[implicit-opponent-modeling]] address adversarial observation and adaptation at different control layers; none establishes a collision shield. [[wang-2026-robust-multiuav-jtcra]] protects a different object altogether: remaining UAVs reassign users after energy depletion to reduce service gaps. Its continuity evidence must not be read as proof of flight safety or anti-jamming robustness.

## Explicit non-comparability

- No guarantee transfers across hazards (obstacles, inter-UAV separation, energy, jammers, task-size distributions, CSI error, or service gaps).
- No guarantee transfers across enforcement loci (reward shaping, next-point filtering, Lyapunov expected cost, persistent intervention, classical chance constraints, or learned service reassignment).
- Training-time guidance is not deployment-time shielding: [[gong-2026-safe-economic-lae-trajectory]] removes the LLM from online control, while MGI keeps its gate in the acting policy.
- Proof, optimizer, and evaluation scopes remain separate. Simulator collision success, one-step prediction error, worst-case expected delay, bounded-error sensitivity, chance-constraint margins, and service-continuity trajectories are not one metric and are not ranked.

## Missing guarantees

This compared set lacks a flight-tested, continuous-time multi-UAV shield with a stated invariant; a controller that combines MGI-style persistent intervention with task-size DRO or CSI chance constraints; a learned policy with a distributional guarantee for adaptive jammers; and a service-continuity result that also proves geometric collision safety during replacement maneuvers. These are open design gaps within the compared set, not claims supplied by any listed source.
