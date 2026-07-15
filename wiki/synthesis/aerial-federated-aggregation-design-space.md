---
type: synthesis
title: "Aerial federated aggregation design space"
tags: [synthesis, federated-learning, aggregation, aircomp, uav, learning-systems]
related:
  - "[[zhong-2026-hierarchical-ota-fl]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[qian-2026-federated-bandit-aircomp]]"
  - "[[dang-2026-uav-fl-energy]]"
  - "[[li-2026-clp-uav-hpfl]]"
  - "[[zhou-2026-cpsfl-uav-foundation-models]]"
  - "[[tang-2024-iscc-uav-feel]]"
  - "[[lim-2021-uav-iov-contract-matching]]"
  - "[[v-2026-pb-papp-survivor-detection]]"
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[aircomp-assisted-asynchronous-fl]]"
  - "[[federated-linear-bandit-learning]]"
  - "[[critical-learning-period]]"
  - "[[split-federated-learning]]"
  - "[[integrated-sensing-computation-communication]]"
created: 2026-07-14
updated: 2026-07-14
---

# Aerial federated aggregation design space

## Scope: what counts as aggregation

In an aerial learning system, “aggregation” is more than an averaging formula. A design also decides **what object is combined**, **where combination occurs**, **which participants contribute**, **when an update is allowed**, **how the wireless channel carries it**, and **whether UAV geometry is an input or a decision**. Those choices determine which performance claim is meaningful.

This page compares seven directly grounded designs:

- [[zhong-2026-hierarchical-ota-fl]] combines local gradients through synchronous, trajectory-segmented AirComp.
- [[huang-2026-aircomp-uav-swarms-afl]] combines selected model layers asynchronously through swarm-head AirComp.
- [[qian-2026-federated-bandit-aircomp]] combines contextual-bandit sufficient statistics only when an information-gain trigger fires.
- [[dang-2026-uav-fl-energy]] uploads models simultaneously but decodes users separately under inter-user interference.
- [[li-2026-clp-uav-hpfl]] performs digital device-UAV-server aggregation and changes participation, visits, and periods from learning-state signals.
- [[zhou-2026-cpsfl-uav-foundation-models]] pipelines split-learning gradients before federated aggregation of LoRA parameters.
- [[tang-2024-iscc-uav-feel]] makes successful sensing an upstream condition for FEEL participation and aggregation.

Two adjacent mechanisms clarify the boundary. In [[lim-2021-uav-iov-contract-matching]], [[multidimensional-contract-matching]] controls ex-ante service eligibility through private-cost screening and stable assignment. [[tree-structured-weight-synthesis]] centrally averages complete logistic-regression coefficients so that predictions can reprioritize UAV routes. They affect who contributes or how aggregation feeds mobility, but neither supplies an AirComp estimator or a general learning guarantee.

## System and guarantee matrix

| Design | Learning object and task | Aggregation topology | Synchronization and participation | Physical layer | Mobility control | Optimized objective | Proof and evidence boundary |
|---|---|---|---|---|---|---|---|
| [[zhong-2026-hierarchical-ota-fl|Hierarchical OTA-FL]] | Local gradients for supervised FL | One UAV parameter server forms partial sums at several positions, then aligns them into one global gradient | Synchronous selected-device uploads; tunable updates per flying round | Analog AirComp with phase compensation, receiver scaling, noise, selection bias, channel mismatch, and cross-device gradient correlation | Fixed-altitude trajectory optimized jointly with selection and aggregation coefficients | Sum of aggregation MSE terms | A gradient-norm stationarity bound is linked to aggregation MSE under stated assumptions; the AO/SCA/FP solver remains local/approximate and learning results are simulations |
| [[huang-2026-aircomp-uav-swarms-afl|AirComp AFL swarm]] | Local model layers for image classification and detection | Sensing UAVs connect to communication-UAV swarm heads; heads maintain a backbone | Asynchronous fixed-interval aggregation of a selected subset; stale layers filtered locally by cosine similarity | Analog AirComp with linkage selection, receive beamforming, distortion, and power constraints | UAV trajectories are external to the optimizer | Maximize uploaded training-data volume subject to AirComp constraints | Branch-and-bound bounds and alternating beamforming evidence concern the communication optimizer; learning and staleness claims are simulation evidence |
| [[qian-2026-federated-bandit-aircomp|Federated bandit AirComp]] | Gram matrices and reward vectors for a shared linear contextual bandit | Mobile UAV server aggregates cached sufficient-statistic increments | Determinant-ratio trigger initiates synchronization; otherwise clients continue locally | Single-antenna analog AirComp under fading, noise, peak/average power, accurate CSI, and tight synchronization | Fixed-altitude horizontal trajectory follows mobile device clusters | Minimize time-averaged AirComp MSE while the learning policy minimizes cumulative pseudo-regret | A channel-noise-aware pseudo-regret bound is provided; it is not an FL-loss convergence theorem. Mobility and MSE gains are simulated |
| [[dang-2026-uav-fl-energy|Interference-limited UAV FL]] | Local model updates for synchronous FL | One UAV server, with users decoded separately | Users upload simultaneously on the same time-frequency resource | Mixed LoS/NLoS A2G rates retain inter-user interference; this is not in-channel function computation | Offline 3-D placement and one movement transition, with velocity and safe-return energy | Minimize UE computation-plus-communication energy under accuracy and deadline constraints | Inner programs have stationary/KKT convergence and the alternating procedure is local; these are optimizer claims, not FL convergence. System evidence is simulation-only |
| [[li-2026-clp-uav-hpfl|CLP-aware hierarchical PFL]] | Personalized local models under non-IID and time-varying data | Devices aggregate at UAVs; UAV models aggregate at a central server | FKN/FDN threshold events change active participants, cluster revisits, and local/edge/global periods | Digital OFDMA links with LoS/NLoS expected gains | SAC selects active UAVs, positions, destinations, and training-sequence periods | Weighted flight energy plus a stale-gradient/data-drift proxy | FKN/FDN derivations and bounded-drift arguments motivate scheduling; the end-to-end policy evidence is simulation, and the local parse lacks the referenced online convergence appendices |
| [[zhou-2026-cpsfl-uav-foundation-models|CPSFL]] | LoRA fine-tuning of a split foundation model | UAV clients run the client partition; a BS runs server partitions and later aggregates client/server trainable parameters | Sequential downlink gradient transmission with priority scheduling and intra-round asynchronous progress; round-end aggregation remains federated | Digital uplink/downlink with slot-varying rates; no analog AirComp | Client trajectories are exogenous observations used by the DRL controller | Weighted per-round pipeline latency and worst-client energy via split-point and resource decisions | Scheduling optimality is conditional on simplifying assumptions; learning convergence under gradient-transmission failures is deferred. Latency/energy findings are simulated |
| [[tang-2024-iscc-uav-feel|Sensing-conditioned FEEL]] | A human-motion recognition model learned from newly sensed radar data | Successfully sensing UAV clients upload local updates to one edge server | Round-based partial participation determined by probabilistic sensing success | A time-divided ISAC transceiver senses by FMCW and communicates digitally with allocated bandwidth | Fixed-altitude horizontal deployment positions are optimized with bandwidth and batch size | Minimize total training time under an optimality-gap constraint | A FEEL-loss upper bound depends on successful-sensing probability; BBPO returns a suboptimal resource/deployment solution, and end performance is simulated |

The matrix is a map of assumptions, not a leaderboard. Accuracy, pseudo-regret, UE energy, training time, aggregation MSE, and pipeline latency answer different questions and cannot be converted into one ranking from the reported experiments.

### Reciprocal design-link rationale

Each new frozen-core relationship has one mechanism-specific reason. These are editorial comparisons grounded in the linked sources, not claims that the papers directly compare one another.

| Reciprocal pair | Rationale | Boundary |
|---|---|---|
| [[zhong-2026-hierarchical-ota-fl]] ↔ [[dang-2026-uav-fl-energy]] | Both expose simultaneous uplink and UAV geometry, but one aligns a wanted gradient sum while the other decodes users under IUI | Do not compare aggregation MSE with UE energy |
| [[zhong-2026-hierarchical-ota-fl]] ↔ [[li-2026-clp-uav-hpfl]] | Contrasts a one-UAV trajectory/time hierarchy with a digital device-UAV-server hierarchy | Cadence and topology only; not a metric ranking |
| [[dang-2026-uav-fl-energy]] ↔ [[li-2026-clp-uav-hpfl]] | Contrasts offline constraint-driven placement/resource control with learning-state-triggered visits and periods | Dang's placement is not an online mobility policy |
| [[zhong-2026-hierarchical-ota-fl]] ↔ [[simultaneous-interference-uav-federated-learning]] | Gives the source-to-concept form of wanted superposition versus unwanted simultaneous interference | Same medium does not imply the same receiver objective |
| [[zhong-2026-hierarchical-ota-fl]] ↔ [[critical-learning-period]] | Compares tunable updates per flying round with CLP-triggered cadence | Zhong neither detects CLPs nor optimizes `J` inside AO |
| [[zhong-2026-hierarchical-ota-fl]] ↔ [[federated-drift-norm]] | Separates same-round cross-device correlation from temporal drift used for revisits | The statistics have no shared numerical scale |
| [[zhong-2026-hierarchical-ota-fl]] ↔ [[federated-kl-divergence-norm]] | Separates gradient moments/correlation for estimator design from local-global parameter-distribution divergence for CLP detection | FKN is the displayed unweighted sum under its Gaussian approximation |
| [[dang-2026-uav-fl-energy]] ↔ [[hierarchical-over-the-air-federated-learning]] | Gives the source-to-concept physical-layer contrast between decoded IUI and analog partial sums | Energy and MSE remain separate |
| [[dang-2026-uav-fl-energy]] ↔ [[gradient-correlation-aware-aggregation-mse]] | Contrasts a UE-energy/deadline objective with a theorem-linked communication-error objective | Dang's KKT claim concerns the optimizer, not FL learning |
| [[dang-2026-uav-fl-energy]] ↔ [[critical-learning-period]] | Separates fixed-problem physical constraints from learning-state-triggered resource timing | No direct Dang-to-FKN/FDN mechanism is inferred |
| [[li-2026-clp-uav-hpfl]] ↔ [[hierarchical-over-the-air-federated-learning]] | Contrasts digital two-tier model averaging with analog trajectory-position partial-gradient aggregation | Both are hierarchical for different reasons |
| [[li-2026-clp-uav-hpfl]] ↔ [[simultaneous-interference-uav-federated-learning]] | Contrasts OFDMA allocation with explicit same-resource IUI | Li's bit-flip stress test is not an IUI model |
| [[hierarchical-over-the-air-federated-learning]] ↔ [[simultaneous-interference-uav-federated-learning]] | Captures the strongest concept-level split in the meaning of wireless superposition | Wanted computation versus rate-degrading interference |
| [[hierarchical-over-the-air-federated-learning]] ↔ [[critical-learning-period]] | Contrasts a tunable OTA aggregation frequency with learning-state-triggered aggregation periods | No CLP detector or AO-optimized `J` is attributed to Zhong |
| [[gradient-correlation-aware-aggregation-mse]] ↔ [[critical-learning-period]] | Compares two explicit communication-learning couplings: continuous error control and thresholded cadence control | MSE and detector thresholds are not compared numerically |
| [[multidimensional-contract-matching]] ↔ [[critical-learning-period]] | Contrasts ex-ante private-cost eligibility with intra-training learning-value eligibility | Incentive compatibility and stability do not imply learning performance |
| [[tree-structured-weight-synthesis]] ↔ [[hierarchical-over-the-air-federated-learning]] | Contrasts central averaging of complete classifier coefficients with in-channel partial-gradient sums | PB-PAPP supplies no AirComp estimator |
| [[v-2026-pb-papp-survivor-detection]] ↔ [[zhong-2026-hierarchical-ota-fl]] | Contrasts weights that guide later routing with trajectory that improves aggregation | The link concerns the aggregation-mobility causal loop, not simulation outcomes |

## Hierarchical synchronous AirComp

[[hierarchical-over-the-air-federated-learning]] uses hierarchy in **space and time**. During one training round, the UAV parameter server receives synchronous analog gradient sums at several trajectory positions. It then applies global aggregation coefficients to those partial sums. The hierarchy makes distant devices reachable without forcing all selected devices to align through one worst channel at one position.

The key communication-learning bridge is [[gradient-correlation-aware-aggregation-mse]]. It retains receiver noise, device-selection bias, channel mismatch, and same-round cross-device gradient correlation, and the learning analysis bounds a stationarity measure by the average aggregation error. This does not prove global minimization of the FL loss. It also does not make the tunable aggregation frequency an AO decision: the frequency is a design setting whose consequences are evaluated separately.

Two contrasts prevent “hierarchical” from becoming a generic link:

- [[li-2026-clp-uav-hpfl]] is hierarchical by **network tier**—device to UAV to central server—and uses digital averaging. Its aggregation periods respond to detected learning state.
- [[tree-structured-weight-synthesis]] is hierarchical by **organizational collection path**—surveillance drone to mother drone to ground authority—but the final operation is a central arithmetic mean of complete classifier coefficients.

## Asynchronous and staleness-aware AirComp

[[aircomp-assisted-asynchronous-fl]] removes the wait-for-all barrier, but analog superposition makes conventional server-side per-client staleness correction difficult. The swarm design therefore moves correction to each selected sensing UAV: it compares local and current global layers and transmits only sufficiently similar layers. Communication-UAV heads select feasible links and receive beamformers under AirComp distortion and power constraints.

The benefit and the limitation come from the same split. Asynchrony reduces idle waiting and AirComp shortens simultaneous upload, while the server loses access to individually separable stale updates. The paper's model uses externally determined trajectories and evaluates learning behavior in simulation; it does not provide a learning-convergence theorem comparable with the stationarity result in hierarchical OTA-FL or the regret result in federated bandits.

## Event-triggered, interference-limited, critical-period, split, and sensing-conditioned aggregation

These five branches intervene at different points in the aggregation pipeline:

1. **Event-triggered online learning.** [[federated-linear-bandit-learning]] synchronizes cached sufficient statistics only after an information-gain trigger. The UAV trajectory and AirComp controls reduce channel distortion when that event occurs. Its central theorem bounds cumulative pseudo-regret, so it should not be described as model-loss convergence.
2. **Interference-limited simultaneous upload.** [[simultaneous-interference-uav-federated-learning]] shares the simultaneous-medium premise with AirComp but assigns it the opposite receiver meaning. The UAV seeks each user's model signal while other users remain interference; the control objective is UE energy under deadlines and safe-return constraints.
3. **Learning-state-triggered cadence.** [[critical-learning-period]], [[federated-kl-divergence-norm]], and [[federated-drift-norm]] use local-global parameter divergence or temporal loss/gradient change to decide when extra participation and revisits have value. These statistics are not substitutes for AirComp MSE: they change the schedule rather than estimate a received analog sum.
4. **Split and pipelined training.** [[split-federated-learning]] places part of each forward/backward pass at the server. CPSFL focuses on sequential downlink gradient transmission and intra-round asynchronous progress before round-end parameter aggregation. Pipeline latency is therefore the relevant communication quantity.
5. **Sensing-conditioned participation.** [[integrated-sensing-computation-communication]] makes data acquisition part of the learning loop. In the FEEL case, UAV position changes both sensing success and uplink delay; only successful sensing clients train and upload in that round.

Two eligibility controls sit beside these branches. [[multidimensional-contract-matching]] screens UAVs by private service costs and assigns them to subregions before learning. CLP control instead changes participation during training from observed learning value. The former's incentive-compatibility and matching-stability results do not imply the latter's learning performance.

## Geometry and resource-control surfaces

The word “mobility” hides four different control surfaces:

- **Trajectory as an aggregation variable:** hierarchical OTA-FL chooses a slotwise fixed-altitude path so that selected analog gradients align across positions.
- **Trajectory as a channel-tracking variable:** federated bandit AirComp follows mobile device clusters while jointly adjusting power and receive normalization.
- **Placement as a resource variable:** interference-limited UAV FL chooses a 3-D endpoint and velocity subject to flight energy; sensing-conditioned FEEL chooses deployment positions that balance target sensing and server communication.
- **Mobility as a scheduling state:** CLP-aware HFL chooses active UAVs, destinations, and revisit periods; CPSFL observes client trajectories to predict slot-level communication conditions but does not control their mission paths.

These surfaces also expose different missing couplings. The asynchronous swarm model leaves path planning outside the optimizer. The energy-minimizing interference model treats one offline placement transition rather than online movement. CPSFL uses trajectory histories for resource decisions while taking mobility as given. No result from one surface automatically transfers to another.

## Guarantee boundaries

The seven papers supply three kinds of evidence that must remain separate.

**Learning guarantees.** Hierarchical OTA-FL bounds a gradient-norm stationarity measure through aggregation MSE. Federated bandit AirComp bounds cumulative pseudo-regret under its synchronization and noise conditions. Sensing-conditioned FEEL bounds training loss or the required rounds through successful-sensing probability. These guarantees have different targets and assumptions.

**Optimizer and scheduling guarantees.** The interference-limited design establishes stationary/KKT behavior for inner approximations and local convergence of its alternating procedure. CPSFL proves scheduling properties under stated simplifications. Such results describe solution procedures, not convergence of the learned model. AirComp swarm branch-and-bound bounds and alternating beamforming behavior likewise concern the communication subproblem.

**Simulation evidence.** Dataset accuracy, time-to-accuracy, resource curves, UAV-placement effects, drift-threshold behavior, pipeline latency, and robustness perturbations are scenario-specific observations. In particular, replacing some synchronized signals with random noise is not a physical timing-offset theorem, and random bit flips are not a modeled same-resource interference channel.

## Non-comparability and design-selection guide

Choose the branch by the system question, then compare methods only within a compatible evidence class:

| Design question | Relevant branch | Required caveat |
|---|---|---|
| Can the multiple-access channel directly compute a wanted gradient sum? | Hierarchical or asynchronous AirComp | Requires synchronization, channel handling, and an explicit distortion model |
| Should communication happen only when new information justifies it? | Federated bandit trigger or CLP detector | Regret triggers and learning-period detectors use different state and guarantees |
| Must user energy and realistic A2G interference remain explicit? | Simultaneous-interference UAV FL | Its optimizer convergence is not FL convergence |
| Is the bottleneck forward/backward pipeline communication for a large model? | CPSFL | Pipeline latency cannot be ranked against AirComp MSE or test accuracy |
| Does UAV position determine whether usable training data exists? | Sensing-conditioned FEEL | Sensing probability is upstream of aggregation and task-specific |
| Is eligibility controlled before training by privately known service cost? | Contract matching | Economic feasibility and stable matching do not guarantee learning quality |
| Does an aggregate model directly reprioritize later motion? | Tree-structured weight synthesis | Central coefficient averaging is not decentralized consensus or AirComp |

The corpus does not support numerical comparisons across accuracy, regret, energy, training time, aggregation MSE, and pipeline latency. Even when two papers report “convergence,” one may mean a learning bound, another local optimization convergence, and another only a plotted training curve.

## Open gaps

- **Learning-state-aware AirComp cadence:** combine a defensible CLP or information-gain signal with trajectory-segmented AirComp without pretending detector thresholds and aggregation MSE share one scale.
- **Online mobility with physical synchronization:** jointly model path decisions, timing/frequency offsets, CSI acquisition overhead, and propulsion energy instead of compensating or externalizing them.
- **Nonstationary and personalized analog aggregation:** extend cross-device correlation models to temporal drift and heterogeneous objectives while preserving an auditable learning bound.
- **End-to-end split-learning reliability:** analyze learning convergence when CPSFL gradient transmissions fail, rather than stopping at pipeline latency.
- **Sensing-to-aggregation uncertainty:** propagate sensing failures and data-quality uncertainty through communication errors and aggregation into a single assumption-explicit learning analysis.
- **Incentives during training:** connect private-cost participation controls with changing learning value while keeping economic, communication, and learning guarantees separate.
- **Security and robustness:** add poisoning, secure aggregation, privacy leakage, and adversarial wireless interference to aerial aggregation without erasing the underlying topology and timing distinctions.
- **Field evidence:** validate synchronization, channel estimation, model transport, onboard inference/control overhead, and energy accounting in an end-to-end airborne experiment.
