# Reinforcement-Learning Experimental Sections

## Contents

1. [Scope and provenance](#scope-and-provenance)
2. [Why learning experiments need an extra evidence layer](#why-learning-experiments-need-an-extra-evidence-layer)
3. [Recommended chapter organization](#recommended-chapter-organization)
4. [Learning evidence ledger](#learning-evidence-ledger)
5. [Reproducible setup](#reproducible-setup)
6. [Training credibility](#training-credibility)
7. [Hyperparameter and checkpoint selection](#hyperparameter-and-checkpoint-selection)
8. [Learning-component ablation](#learning-component-ablation)
9. [Algorithm comparison](#algorithm-comparison)
10. [Test-time physical performance](#test-time-physical-performance)
11. [Learned-decision interpretation](#learned-decision-interpretation)
12. [Sensitivity, generalization, robustness, and resilience](#sensitivity-generalization-robustness-and-resilience)
13. [Efficiency and deployment cost](#efficiency-and-deployment-cost)
14. [Artifact-specific evidence units](#artifact-specific-evidence-units)
15. [Multi-agent and hybrid-action cases](#multi-agent-and-hybrid-action-cases)
16. [Wording and claim boundaries](#wording-and-claim-boundaries)
17. [Common invalid claims](#common-invalid-claims)
18. [Reinforcement-learning-route audit](#reinforcement-learning-route-audit)

## Scope and provenance

Use this route for value-based, policy-gradient, actor-critic, deep reinforcement learning, multi-agent reinforcement learning, centralized-training/decentralized-execution, hierarchical learning, hybrid-action learning, and learning-assisted online control.

The structural rules were calibrated against representative experimental sections including:

- *Deep Reinforcement Learning Based Dynamic Trajectory Control for UAV-Assisted Mobile Edge Computing*;
- *Cooperative UAV Resource Allocation and Task Offloading in Hierarchical Aerial Computing Systems: A MAPPO-Based Approach*;
- *Robust Computation Offloading and Trajectory Optimization for Multi-UAV-Assisted MEC: A Multiagent DRL Approach*;
- *MADDPG-Based Joint Service Placement and Task Offloading in MEC Empowered Air-Ground Integrated Networks*;
- *Mobile-Edge Computing in SAGINs: A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation*;
- *Joint Trajectory, RIS, and Computation Offloading Optimization Via Decentralized Model-Based PPO in Urban Multi-UAV Mobile Edge Computing*;
- *UAV-Assisted Security-Aware Vehicular Edge Computing: A TD3-Enhanced Scheme*.

These papers supply representative DDPG, replay-based, MAPPO, MADDPG, PPO, TD3, and value-based patterns. They are provenance, not runtime dependencies.

## Why learning experiments need an extra evidence layer

An evolutionary experiment evaluates a stochastic optimizer's returned solutions. A learning paper must additionally establish that the reported policy was trained and selected credibly. A high reward can reflect reward scaling, smoothing, leakage, or a different objective rather than a better physical system decision.

Organize the evidence as a ladder:

1. **Reproducibility:** define environment distributions, model architecture, training budget, seeds, and evaluation protocol.
2. **Trainability:** show that learning progresses under the declared protocol.
3. **Selection validity:** tune hyperparameters and select checkpoints without using final test outcomes.
4. **Mechanism evidence:** isolate the proposed learning components.
5. **System evidence:** evaluate the frozen policy on physical objectives and constraints.
6. **Behavior evidence:** interpret trajectories, task splits, resource allocations, or other decisions.
7. **Scope evidence:** test unseen conditions, uncertainty, failures, and scale.
8. **Deployment evidence:** separate offline training from online inference and auxiliary computation.

Do not skip from setup to reward superiority and treat the ladder as complete.

## Recommended chapter organization

Use this functional order when supported by the paper:

1. **Experiment roadmap.** Map learning and system experiments to contribution claims.
2. **Environment and system setup.** Define topology, arrivals, mobility, channel/task distributions, horizons, and constraints.
3. **Learning and implementation setup.** Define observations/actions, network architecture, optimizer, learning schedule, hardware/software, seeds, and budget.
4. **Data or scenario protocol.** Define train/validation/test generation and whether initial states or scenarios are shared.
5. **Training credibility.** Report convergence, variability, and diagnostic agent/critic behavior when relevant.
6. **Hyperparameter selection.** Show how settings were selected on training or validation evidence.
7. **Learning-component ablation.** Isolate replay, masks, normalization, policy distributions, attention, decoders, safety layers, or other proposed elements.
8. **Algorithm comparison.** Compare learning baselines under equivalent training and information budgets.
9. **Test-time system performance.** Report original physical objectives, constraints, QoS, and feasibility.
10. **Policy interpretation.** Explain learned trajectories, placements, offloading, caching, scheduling, or resources.
11. **Generalization, robustness, resilience, and scale.** Test the exact scope claimed.
12. **Efficiency.** Separate offline training cost, online inference latency, and auxiliary solver cost.

The order may combine adjacent functions, but training credibility must precede conclusions about the learned policy unless the paper evaluates a fixed pretrained model without making a training contribution.

## Learning evidence ledger

Extend the shared claim-to-experiment ledger with:

| Field | Required meaning |
|---|---|
| Training distribution | How states, scenarios, tasks, channels, or users are generated during training |
| Validation distribution | Data/scenarios used for hyperparameters and checkpoint selection |
| Test distribution | Held-out cases used only for final reporting |
| Seeds or runs | Independently initialized training runs and environment randomness |
| Training budget | Episodes, steps, interactions, updates, wall-clock, or simulator calls |
| Evaluation protocol | Evaluation frequency, episodes, stochastic/deterministic policy, and environment seeds |
| Checkpoint rule | Final, best validation, moving-average, or predeclared selection rule |
| Smoothing | Window and whether smoothing affects only visualization |
| Uncertainty | Standard deviation, standard error, confidence interval, or quantiles and their statistical unit |
| Information budget | Observations, global state, communication, model knowledge, or privileged training information |
| Generalization axis | The exact unseen factor, distribution shift, perturbation, or failure tested |

Never infer these entries from an algorithm name. Recover them from the target manuscript or mark them missing.

## Reproducible setup

### Environment and system

State:

- spatial region, mobility, initial-state distribution, and horizon;
- task arrivals, sizes, deadlines, computation intensities, and dependencies;
- channel, blockage, interference, energy, queue, and resource distributions;
- constraints, penalties, termination, and failure behavior;
- how scenarios differ across training, validation, and testing.

Separate default parameters from distributions. A table of fixed means is insufficient when the policy trains on randomized values.

### Learning implementation

Report when relevant:

- policy, value, critic, target, attention, or recurrent network sizes and activations;
- optimizer, learning rates, discount, target-update, replay, batch, clipping, entropy, and normalization settings;
- episodes, steps per episode, update frequency, warm-up, replay capacity, and exploration schedule;
- parameter sharing, centralized critic, communication, recurrent-state handling, and agent count;
- software framework, hardware, and precision when training or inference cost is claimed.

Put long ordinary defaults in a table or supplement. Explain settings that materially define the proposed method or fairness.

### Randomness and aggregation

State independent training seeds, environment seeds, and whether test scenarios are common across algorithms. Clarify whether plotted bands aggregate seeds, episodes, users, or time steps.

One long training run does not become many independent runs because it contains many episodes. Evaluation episodes from one checkpoint measure environment variability, not training variability.

## Training credibility

Training evidence answers whether the learning procedure reliably reaches a useful policy under the declared budget. It does not by itself answer whether the policy improves the physical system.

### Convergence contract

State:

- which training or evaluation return is plotted;
- whether the curve uses on-policy episodes, replay updates, or periodic deterministic evaluation;
- number of independent seeds;
- horizontal-axis unit and common budget;
- aggregation, interval, and smoothing window;
- the algorithm variants or hyperparameters compared;
- figure pointer.

### Convergence evidence

Analyze separately:

- early learning or exploration behavior;
- speed to a declared return or performance level;
- final evaluation level at a common budget;
- variance or failures across seeds;
- oscillation, collapse, overfitting, or agent imbalance;
- whether a component reduces sensitivity to a training setting.

Use `converges empirically under the tested settings` rather than claiming theoretical or global convergence.

Do not call a curve stable because its moving average is smooth. Stability requires across-run or across-seed evidence and a defined criterion.

### Diagnostic curves

Actor loss, critic loss, Q values, entropy, or agent-specific returns are useful only when they answer a diagnostic question. Loss magnitude alone is rarely a performance metric. Explain what behavior a curve detects and connect it to a downstream result.

## Hyperparameter and checkpoint selection

Treat hyperparameter sweeps as model-selection experiments, not final test comparisons.

### Valid protocol

1. define the candidate set before inspecting test results;
2. train candidates under comparable budgets and seeds;
3. select by a declared validation metric;
4. freeze the selected setting;
5. evaluate the frozen policy on held-out test scenarios.

If no separate validation set exists, say so and narrow the claim. Do not describe test-guided selection as generalization evidence.

### Writing the experiment

The contract states the candidate values, validation scenarios, common budget, seeds, selection metric, and figure/table. The evidence block identifies the selected value, reports the trade-off or sensitivity, notes whether adjacent values perform similarly, and limits the conclusion to the tested range.

Do not choose a learning rate merely because its smoothed training reward has the highest transient peak.

### Checkpoints

State whether final results use the last checkpoint, the best validation checkpoint, an average, or an ensemble. Use the same selection rule across algorithms. Selecting each method's best test checkpoint leaks test information and biases comparisons.

## Learning-component ablation

Use ablations for contribution-bearing components such as prioritized replay, action masking, normalization, policy distributions, attention, recurrent memory, hierarchical decomposition, hybrid decoders, model-based rollouts, safety projections, or reward components.

The contract must define exactly what changes in each variant and keep network capacity, training interactions, seeds, scenario distributions, and selection rules comparable. If removing a component changes action feasibility or network size, disclose that coupled change.

The evidence block should answer:

1. Does the component change training credibility?
2. Does it change held-out physical performance?
3. Under which scale or uncertainty does the effect appear?
4. Does it trade one metric for another?
5. Is the effect independent or interactive with another component?

Do not justify a system mechanism only with training reward if the component alters reward shaping or scale.

## Algorithm comparison

### Comparable budgets

Equalize or disclose:

- environment interactions and training updates;
- number of seeds and scenario realizations;
- hyperparameter tuning budget;
- network capacity when it materially differs;
- observation and global-state access;
- centralized communication or model knowledge;
- checkpoint rule and evaluation episodes.

Equal episodes do not guarantee equal interactions when horizons or early termination differ. Equal wall-clock does not guarantee equal data when simulators or hardware differ.

### Reward comparability

Compare returns directly only when reward definitions, scaling, normalization, discounting, and horizons are commensurate. When algorithms optimize different surrogate rewards, compare them on the original physical objectives and constraint outcomes.

### Baseline roles

Include, when supported:

- the adopted base learner;
- learning algorithms suited to the same action-space and multi-agent structure;
- component ablations;
- classical optimization or heuristic baselines that reveal solution quality or online cost;
- architecture baselines such as UAV-only, HAP-only, static, centralized, or decentralized variants.

State what each baseline diagnoses rather than summarizing its source paper.

## Test-time physical performance

Final system claims should use metrics defined by the system model and problem formulation, such as:

- latency, energy, charge cost, utility, reliability, completion rate, AoI, throughput, or revenue;
- constraint violation, infeasible-action rate, outage, missed deadlines, or queue stability indicators;
- fairness or per-agent performance where aggregate reward can hide imbalance;
- runtime or decision latency required for online operation.

### Test contract

State the frozen policy/checkpoint, held-out scenario generation, evaluation episodes or cases, common randomness, stochastic or deterministic action rule, baselines, metrics, aggregation, uncertainty, and artifact.

### Evidence block

Begin with the physical answer, not the reward. Quantify the closest comparison and any constraint trade-off. Explain the decision behavior causing the metric change. Report cases where reward improves but one physical objective worsens.

Training reward is not sufficient evidence of lower latency, lower energy, higher feasibility, reliability, or QoS unless the reward equals that metric without transformation and evaluation uses held-out cases.

## Learned-decision interpretation

Use policy visualizations to explain how the learned decisions produce measured outcomes. Examples include:

- UAV/HAP trajectories and hover locations;
- service placement and task-offloading splits;
- association, scheduling, power, spectrum, CPU, cache, or altitude choices;
- agent cooperation, division of labor, or communication;
- adaptation after failures or state changes.

The contract states the selected test case, checkpoint, initial condition, and comparison. The evidence block links:

`observed state -> learned decision -> intermediate physical effect -> objective or constraint outcome`.

Do not generalize one trajectory to all scenarios. Label it as a case study or representative test and state its selection rule.

## Sensitivity, generalization, robustness, and resilience

Use these terms as different claims.

### Sensitivity

Vary one parameter or resource within a tested range. A low response indicates low sensitivity in that range. It does not establish behavior under a distribution shift.

### Generalization

Evaluate a frozen policy on conditions not used for training or selection, such as unseen initial positions, loads, user counts, topologies, or task distributions. State the distance or nature of the shift. Test-time random samples from the training distribution measure expected performance, not out-of-distribution generalization.

### Robustness

Apply explicit perturbations, uncertainty, estimation errors, adversarial variation, or model mismatch. Define perturbation magnitude and whether the policy was trained with matching randomization. A smooth nominal reward curve is not robustness evidence.

### Resilience

Introduce component failures, UAV loss, link outage, or resource removal and evaluate degradation and recovery. Report the failure time, information available to the policy, recovery criterion, and post-failure performance.

### Scalability

Increase agents, users, satellites, tasks, action dimension, or network size. State whether the same trained policy transfers, the policy is retrained, parameters are shared, or architecture size changes. Retraining at every scale demonstrates scalable training experiments, not zero-shot scale generalization.

Do not combine these claims under a generic `robustness analysis` heading unless the subsection explicitly distinguishes them.

## Efficiency and deployment cost

Separate:

1. **offline data/simulation cost;**
2. **offline training wall-clock and hardware;**
3. **online neural inference latency and memory;**
4. **online decoding, projection, matching, optimization, or safety-layer cost;**
5. **communication cost for centralized or multi-agent execution.**

Report batch and single-decision latency separately where relevant. A fast forward pass does not establish real-time operation if action realization solves a large subproblem or waits for centralized state.

Compare online cost under the same hardware and batch conditions. Use asymptotic complexity to explain scaling, not as a substitute for measured latency when real-time feasibility is claimed.

## Artifact-specific evidence units

### Training-return curve

**Contract:** identify training or periodic evaluation return, budget, seeds, aggregation, interval, smoothing, variants, and figure.

**Evidence:** report trainability, speed/final level under the common budget, across-seed variability, collapse or oscillation, and the limited training conclusion. Do not infer physical superiority.

### Validation hyperparameter plot

**Contract:** identify candidates, validation distribution, metric, seeds, budget, and selection rule.

**Evidence:** name the selected region, quantify material differences, report flat or unstable regions, and freeze the selection before test results.

### Test metric table

**Contract:** identify frozen checkpoints, held-out scenarios, evaluation episodes, physical metrics, uncertainty, baselines, and significance procedure.

**Evidence:** begin with the system-level answer, compare the closest baseline, report constraint outcomes and exceptions, explain policy behavior, and state the bounded conclusion.

### Component ablation plot

**Contract:** define removed component, capacity/budget controls, seeds, validation/test protocol, and artifact.

**Evidence:** distinguish effects on learning dynamics from effects on final physical metrics. Attribute causality only to differences isolated by the variant.

### Policy or trajectory visualization

**Contract:** state case and checkpoint selection, initial state, scenario, and comparator.

**Evidence:** trace state to decision to physical effect to metric. Treat the visualization as interpretive evidence, not aggregate proof.

### Uncertainty or failure curve

**Contract:** define perturbation/failure, magnitude, timing, whether seen during training, recovery metric, and test protocol.

**Evidence:** quantify degradation and recovery, identify thresholds or failures, compare nominal and perturbed behavior, and use robustness or resilience language only within that definition.

## Multi-agent and hybrid-action cases

### Multi-agent learning

Report:

- number and type of agents;
- local observations and global training state;
- individual, shared, or mixed rewards;
- actor and critic inputs;
- parameter sharing and communication;
- centralized-training information unavailable during execution;
- per-agent and system-level evaluation.

When reporting convergence, check whether one agent type learns earlier or dominates the shared return. An aggregate curve can conceal poor coordination or unfair performance.

### Hybrid actions

State which component selects the discrete action, which produces continuous parameters, how invalid combinations are masked or decoded, and whether baseline algorithms support the same action space naturally.

Evaluate discrete feasibility, continuous quality, and end-to-end physical outcomes. A baseline forced through a lossy discretization or incompatible decoder is not automatically a fair comparison.

### Hierarchical learning

Separate high-level and low-level horizons, rewards, update schedules, and checkpoints. Explain whether lower-level policies are pretrained, frozen, or jointly trained. Attribute gains through ablations that isolate hierarchy rather than merely comparing different network sizes.

## Wording and claim boundaries

Prefer:

- `the evaluation return stabilizes within the tested training budget`;
- `across the reported seeds, the policy attains ...`;
- `the frozen policy reduces test-time latency on the held-out scenarios`;
- `the action mask eliminates invalid choices by construction`;
- `the policy generalizes to the unseen user counts evaluated here`;
- `performance degrades gradually under the tested estimation errors`;
- `online inference meets the reported decision deadline on the stated hardware`.

Avoid:

- `the agent converges to the optimal policy` without proof;
- `the curve proves stability`;
- `higher reward proves lower energy and delay`;
- `the policy is robust` after only nominal or sensitivity tests;
- `the method generalizes well` when test cases come from the training distribution;
- `real-time` when only training time or batched GPU inference is reported;
- `fair comparison` when observations, tuning budgets, or action representations differ.

## Common invalid claims

| Tempting claim | Why invalid | Required correction or evidence |
|---|---|---|
| `One smooth reward curve proves stable convergence` | Smoothing and one seed hide variability | Report independent seeds, intervals, and criterion |
| `Higher reward proves better MEC performance` | Reward may be scaled or surrogate | Compare held-out physical metrics and constraints |
| `Best test checkpoint is the final policy` | Test-guided selection leaks information | Select by a predeclared validation rule |
| `Same episodes means equal training budget` | Horizons and updates may differ | Report interactions, steps, and updates |
| `Sensitivity proves robustness` | No explicit uncertainty or shift was tested | Narrow the term or add perturbation tests |
| `Random test episodes prove generalization` | They may share the training distribution | Define a genuinely unseen axis |
| `Failure performance proves robustness` | Failure and recovery are resilience questions | Name resilience protocol and recovery metric |
| `Fast inference makes the method real-time` | Decoder/communication cost may dominate | Measure the full online decision pipeline |
| `Aggregate reward proves agent cooperation` | One agent may dominate | Report agent-level outcomes or coordination evidence |

## Reinforcement-learning-route audit

- [ ] Environment distributions and fixed system parameters are distinguished.
- [ ] Train/validation/test scenarios and their roles are explicit.
- [ ] Network architecture, optimizer, interactions, updates, and stopping budget are reproducible.
- [ ] Independent training seeds are distinguished from evaluation episodes.
- [ ] Every curve is labeled as training or evaluation and states aggregation, interval, and smoothing.
- [ ] Hyperparameters and checkpoints are selected without final-test leakage.
- [ ] Baselines have comparable training, tuning, action, observation, and information budgets.
- [ ] Reward comparisons are commensurate or replaced by physical system metrics.
- [ ] Learning-component ablations preserve other capacities and budgets or disclose coupled changes.
- [ ] Final system claims use frozen policies and held-out physical metrics and constraints.
- [ ] Policy visualizations identify their case-selection rule and remain interpretive.
- [ ] Sensitivity, generalization, robustness, resilience, and scalability are named according to the actual protocol.
- [ ] Multi-agent studies disclose local/global information, rewards, sharing, and execution communication.
- [ ] Hybrid-action comparisons account for action representation and decoding fairness.
- [ ] Offline training, online inference, auxiliary optimization, and communication costs are separated.
- [ ] No claim of optimality, stability, robustness, or real-time feasibility exceeds the evidence.
