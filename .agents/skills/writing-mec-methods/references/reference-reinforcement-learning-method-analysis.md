# Reference-Derived Reinforcement-Learning Method Analysis

## Contents

1. [Corpus and scope](#1-corpus-and-scope)
2. [Cross-paper structural result](#2-cross-paper-structural-result)
3. [DDPG/PER with deterministic matching](#3-ddpgper-with-deterministic-matching)
4. [MAPPO for hierarchical aerial computing](#4-mappo-for-hierarchical-aerial-computing)
5. [MADDPG for mixed-integer air-ground MEC](#5-maddpg-for-mixed-integer-air-ground-mec)
6. [Beta-policy MAPPO for robust multi-UAV MEC](#6-beta-policy-mappo-for-robust-multi-uav-mec)
7. [P-DDQN for hybrid SAGIN decisions](#7-p-ddqn-for-hybrid-sagin-decisions)
8. [PPO and TD3 cross-checks](#8-ppo-and-td3-cross-checks)
9. [Stable invariants and legitimate variants](#9-stable-invariants-and-legitimate-variants)
10. [Default RL section architecture](#10-default-rl-section-architecture)
11. [Single-agent, multi-agent, and hybrid-action variants](#11-single-agent-multi-agent-and-hybrid-action-variants)
12. [Paragraph and wording patterns](#12-paragraph-and-wording-patterns)
13. [RL-specific hard gates](#13-rl-specific-hard-gates)
14. [Anti-patterns](#14-anti-patterns)

## 1. Corpus and scope

The primary corpus spans established and recent IEEE MEC-family papers with different RL interfaces. Complete algorithm sections were inspected so that the resulting rules reflect section and paragraph organization rather than abstract-level descriptions.

| Benchmark | Publication information | Method-writing role |
|---|---|---|
| *Deep Reinforcement Learning Based Dynamic Trajectory Control for UAV-Assisted Mobile Edge Computing* | IEEE Transactions on Mobile Computing, 2022, DOI 10.1109/TMC.2021.3059691 | DDPG/PER, deterministic matching subroutine, offline training versus fast deployment |
| *Cooperative UAV Resource Allocation and Task Offloading in Hierarchical Aerial Computing Systems: A MAPPO-Based Approach* | IEEE Internet of Things Journal, 2023, DOI 10.1109/JIOT.2023.3240173 | PPO preliminaries, CTDE MAPPO framework, trajectory collection and policy update phases |
| *MADDPG-Based Joint Service Placement and Task Offloading in MEC Empowered Air-Ground Integrated Networks* | IEEE Internet of Things Journal, DOI 10.1109/JIOT.2023.3326820 | complete MDP mapping, mixed-action realization, centralized replay, algorithm and complexity |
| *Robust Computation Offloading and Trajectory Optimization for Multi-UAV-Assisted MEC: A Multiagent DRL Approach* | IEEE Internet of Things Journal, 2024, DOI 10.1109/JIOT.2023.3300718 | agent-type-specific observations/actions/rewards, CTDE, Beta-distribution policy, complexity |
| *Mobile-Edge Computing in SAGINs: A Hybrid Action Space P-DDQN Algorithm for Joint Offloading and Resource Allocation* | IEEE Transactions on Wireless Communications, 2026, DOI 10.1109/TWC.2026.3706356 | parameterized hybrid action, DDQN/DDPG composition, update order, training complexity |

Two additional TMC papers are used as cross-checks:

- *Joint Positioning and Computation Offloading in Multi-UAV MEC for Low Latency Applications: A Proximal Policy Optimization Approach*, 2025, DOI 10.1109/TMC.2025.3562806.
- *UAV-Assisted Security-Aware Vehicular Edge Computing: A TD3-Enhanced Scheme*, 2026, DOI 10.1109/TMC.2026.3709174.

The benchmark set covers single-agent continuous control, CTDE multi-agent learning, mixed discrete-continuous decisions, policy-distribution adaptation, and RL combined with deterministic optimization. It therefore supports a shared RL writing contract without imposing one algorithm's accidental details on all papers.

## 2. Cross-paper structural result

The stable RL Method story is:

`sequential/online difficulty -> MDP/POMDP interface -> action realization and constraint semantics -> base learner -> scenario-specific adaptation -> training procedure -> online execution -> complexity`

The order of the MDP interface and learner preliminaries legitimately changes:

- **MDP already complete in Problem Formulation:** cross-reference state/action/reward and begin with learner preliminaries or CTDE architecture.
- **MDP not yet complete:** define agent, state/observation, action, reward, transition, horizon, and termination before learner updates.
- **Unusual action realization is the main contribution:** define the raw action interface, then give a dedicated decoding or hybrid-action subsection before the full training loop.

The benchmark papers allocate detail in two layers:

1. **standard learner layer:** enough equations to define the adopted PPO, DDPG, TD3, MAPPO, MADDPG, or DDQN update;
2. **problem-specific layer:** state/observation design, action mapping, reward construction, agent decomposition, matching, masks, policy distribution, or hybrid-action coupling.

A strong paper gives the second layer at least as much causal explanation as the first.

## 3. DDPG/PER with deterministic matching

### 3.1 Published organization

The RAT method in the TMC paper uses:

1. **Proposed RAT Algorithm**;
2. **Preliminaries**, split into DQN and DDPG;
3. **The RAT Algorithm**, containing state, action, reward, architecture, training, PER, pseudocode, matching, deployment, and inference complexity.

### 3.2 Center-sentence spine

1. RAT is introduced to make trajectory decisions quickly after training;
2. DQN is summarized to establish Q-value learning and its discrete-action limitation;
3. DDPG is introduced because UAV movement is continuous;
4. RAT defines UAV locations as state, movement as action, and negative UE energy plus boundary penalty as reward;
5. the actor controls trajectories while a matching subroutine deterministically solves association and resource allocation;
6. replay transitions train actor and critic networks, with PER emphasizing informative samples;
7. after offline training, the saved actor supports fast online action generation, followed by matching;
8. inference complexity includes both the network forward pass and matching over users and UAVs.

### 3.3 What each block contributes

**Preliminaries.** The DQN discussion exists mainly to explain why discretizing a continuous UAV trajectory becomes intractable. DDPG then introduces actor, critic, target networks, critic loss, and policy gradient. This is solver motivation by action structure, not popularity.

**Decision decomposition.** The actor does not output every decision in the original problem. It outputs UAV trajectory controls. Given those controls, a matching algorithm computes association and resource allocation. The Method section explicitly states that decomposition and shows how matching affects the reward. This closes variables that would otherwise disappear between formulation and action space.

**PER novelty.** The paper defines the priority score, sampling probability, importance-sampling weight, and resulting weighted critic loss. It explains both the intended benefit and the bias/oscillation issue addressed by importance weighting.

**Pseudocode and prose.** Algorithm 2 covers actor/critic initialization, target networks, replay, noisy action, environment transition, matching, reward, prioritized sampling, network updates, and target updates. The prose explains those phases and then gives Algorithm 3 for matching.

**Deployment.** The paper states that training may occur in a simulator with randomized take-off points and that only saved networks plus simple algebraic/matching operations are needed during testing. Complexity is therefore reported for online action generation, not only training.

### 3.4 Transferable lesson

If RL controls only part of the original decision vector, the Method section must identify the deterministic or optimization subroutine that produces the remaining decisions, place it inside the interaction loop, and include its cost in inference complexity.

## 4. MAPPO for hierarchical aerial computing

### 4.1 Published organization

The IoT-J method uses:

1. section roadmap;
2. **PPO** preliminaries;
3. **MAPPO Framework**;
4. **MAPPO Algorithm**.

The POMDP components were already established in Problem Formulation, so the Method section does not unnecessarily redefine the application state/action/reward before explaining the learner.

### 4.2 Center-sentence spine

1. PPO preliminaries are introduced before the MAPPO design;
2. the clipped objective addresses unstable policy steps and the critic estimates value;
3. MAPPO is appropriate because UAVs act on local observations but must cooperate;
4. centralized critics use global information during offline training, while actors use local observations online;
5. training collects complete UAV trajectories and then performs repeated mini-batch policy/value updates;
6. execution removes exploration and critics, leaving actor forward passes at UAVs.

### 4.3 What each block contributes

**PPO layer.** The paper gives the clipped surrogate, advantage estimate, value loss, and entropy-augmented objective. These equations establish the objects used in MAPPO training.

**CTDE data flow.** The framework paragraph names the offline centralized-training phase and the decentralized-execution phase. The centralized critic consumes global state and joint actions; each actor produces actions from its local observation. The paper also states that execution requires forward propagation only.

**Training algorithm.** The pseudocode separates two phases: trajectory collection and policy updates. It records observations, actions, returns/Q values, and advantages; shuffles data; trains in mini-batches for several epochs; updates policy/value parameters; and clears the buffer.

### 4.4 Transferable lesson

Do not repeat an application MDP that is already complete merely to follow a generic template. Cross-reference it, then spend the Method section on CTDE information flow, update equations, and the training-to-execution boundary.

## 5. MADDPG for mixed-integer air-ground MEC

### 5.1 Published organization

The IoT-J method uses:

1. method roadmap;
2. **Preliminaries of MADDPG**;
3. **Problem Reformulation**;
4. **Reformulating Actions to Adapt to MADDPG**;
5. **Joint Optimization Algorithm Framework Based on MADDPG for the MINLP**;
6. **Complexity Analysis**.

### 5.2 Center-sentence spine

1. the section introduces MADDPG, maps the MINLP into an MDP, adapts mixed actions, and presents the full framework;
2. MADDPG uses local deterministic actors, global critics, target networks, and centralized replay;
3. each UAV observes covered users while a primary UAV aggregates global state for training;
4. actions contain placement, offloading, access/instance selection, power, and CPU allocation;
5. the shared reward follows the system cost, with an explicit penalty branch for infeasible actions;
6. continuous outputs are normalized and discrete/coupled decisions are transformed differently in training and testing;
7. the algorithm collects, transforms, executes, stores, and learns from joint actions;
8. complexity counts actor/critic networks, agents, and mini-batch processing.

### 5.3 What each block contributes

**Learner preliminaries.** Actor input/output, critic global input, target networks, replay tuples, actor gradient, critic target/loss, and soft updates are defined before adaptation. This makes the later mixed-action procedure understandable.

**Complete MDP interface.** The reformulation defines local observations, global state aggregation, action components, shared reward, and next-state generation. Including next state is important because the environment contains service instances, task requests, path loss, and positions that evolve through different mechanisms.

**Action adaptation.** Continuous variables are mapped from normalized actor outputs into physical intervals. Integer values are rounded, binary decisions use sampling during training and deterministic selection during testing, and coupled binary variables are transformed jointly. The paper therefore distinguishes differentiable/raw actions from executed decisions.

**Full loop.** The pseudocode calls the action-reformulation step before environment execution and stores joint transitions for centralized learning. The prose then traces the same loop.

### 5.4 Transferable lesson

For an MINLP solved by a continuous-action learner, `the actor outputs all decisions` is insufficient. Each variable type needs a training-time realization rule, a testing-time realization rule, and a coupling-preservation rule. Reward penalties do not replace those mappings.

## 6. Beta-policy MAPPO for robust multi-UAV MEC

### 6.1 Published organization

The IoT-J method uses:

1. a problem-to-MAPPO motivation paragraph;
2. **Modeling of Multiagent MDP**;
3. **MAPPO-Based DRL Training Framework**;
4. **Beta Policy**;
5. **Complexity Analysis**.

### 6.2 Center-sentence spine

1. uncertainty, time variation, high-dimensional decisions, and synchronization cost motivate a multi-agent online framework;
2. UE and UAV agents receive different observations, actions, and rewards because they control different decision groups;
3. a CTDE framework trains shared policies for homogeneous agent types and downloads actors for distributed execution;
4. value, advantage, critic, and clipped actor objectives define MAPPO learning;
5. a Beta output distribution matches double-bounded physical actions and reduces Gaussian boundary effects;
6. training pseudocode orders observation, action, central reward/state processing, buffering, and policy updates;
7. complexity accounts for MLP structure, agent parallelism, episode length, and training episodes.

### 6.3 What each block contributes

**Agent decomposition.** UE agents control association/offloading; UAV agents control movement, beamforming, and CPU allocation. Each type has its own observation and reward construction. The global state is the product of local observation spaces, while the joint action is the product of agent actions.

**Constraint semantics.** Several invalid behaviors are discouraged through latency, boundary, and collision penalties. Those penalties guide learning but do not by themselves prove collision-free or deadline-feasible execution. A method written from this pattern must preserve that boundary unless it adds masking, projection, or a verified safety layer.

**CTDE deployment.** Agents send experience to a training center, critics evaluate merged global state, actor parameters are updated and downloaded, and homogeneous agents share parameters. This describes the actual communication and parameter flow.

**Beta-policy novelty.** The standard Gaussian action distribution is unbounded, whereas many actions have lower and upper limits. The paper defines the Beta density and explains how bounded support addresses clipping/boundary effects while retaining exploration. The novelty is the distribution-interface match, not MAPPO itself.

### 6.4 Transferable lesson

An architecture adaptation must identify the mismatch in the baseline interface, define the replacement mathematically, and show where it enters action sampling and training. Merely renaming MAPPO as `enhanced MAPPO` is not enough.

## 7. P-DDQN for hybrid SAGIN decisions

### 7.1 Published organization

The TWC method uses:

1. a problem-to-DRL transition;
2. **The MDP in SAGIN Scenario**;
3. **P-DDQN Algorithm for Hybrid Action Space**;
4. **Implementation Details of Algorithm 1**;
5. **Complexity Analysis**.

### 7.2 Center-sentence spine

1. the MINLP has time-varying, high-dimensional discrete and continuous decisions, motivating DRL;
2. the MDP state contains locations, workloads, satellite service time, and remaining system work;
3. each hybrid action pairs a discrete scheduling/association/movement choice with its continuous power, task, and trajectory parameters;
4. normalization and conditional fallback enforce task-split and coverage-time structures before reward evaluation;
5. P-DDQN uses a policy network to propose continuous parameters for discrete choices and DDQN to select among those choices;
6. targets, Q loss, actor loss, and soft updates are defined in computational order;
7. Algorithm 1 covers interaction, replay, terminal targets, gradient updates, and task-completion termination;
8. complexity counts episodes, steps, mini-batches, and actor/critic layers.

### 7.3 What each block contributes

**Hybrid interface.** The action is represented as a pair `(discrete choice, continuous parameters conditional on that choice)`. This avoids discretizing every continuous dimension or pretending a discrete decision is inherently continuous.

**Constraint realization.** If satellite service-time feasibility fails, the action falls back to local/UAV processing. Task ratios are normalized to a simplex so that their sum is valid. These operations have stronger semantics than a reward penalty and are described next to the MDP interface.

**Two-stage action generation.** For every discrete action, the policy network generates continuous parameters. The DDQN network then evaluates state-choice-parameter tuples and selects the discrete action with the largest Q-value. The section states this forward decision path before presenting Bellman and loss equations.

**Update order.** The target Q-value is defined first, then Q loss, policy loss, online-network gradient steps, and target-network soft updates. Pseudocode follows the same order and treats terminal next states separately.

**Implementation paragraph.** After the algorithm box, one paragraph groups action generation and policy update as the two main phases instead of paraphrasing each line.

### 7.4 Transferable lesson

Hybrid-action writing must expose conditionality: which continuous parameters belong to which discrete action, how invalid pairs are prevented, how the pair is selected during inference, and how both networks receive learning signals.

## 8. PPO and TD3 cross-checks

### 8.1 TMC PPO positioning/offloading paper

The section uses PPO preliminaries, state/action definition, reward, algorithm design, pseudocode, and complexity. It provides several useful patterns:

- a centralized manager is named as the agent and its global information is listed;
- UAV position and task allocation are mapped into a continuous action;
- a hard projection/scaling step is distinguished from energy/computation penalty terms;
- backhaul BFS and user association occur inside the learning loop and are included in complexity;
- complexity includes neural inference, fronthaul association, and backhaul formation.

The paper also uses an epsilon-greedy exploration description with PPO. This is an isolated implementation choice, not a general PPO writing convention. Do not copy it unless the target implementation actually uses and justifies that behavior.

### 8.2 TMC TD3 security-aware vehicular paper

The section first states that the contribution is the system-aware application and action interface, not a new TD3 algorithm. It then uses:

1. MDP transformation;
2. centralized training/distributed application context;
3. explicit bounded mappings for offloading and movement;
4. continuous association scores followed by execution-time argmax;
5. a security-aware latency reward;
6. standard TD3 twin-critic, smoothing, delayed-actor, and target updates.

Its strongest transferable feature is the contribution boundary. Standard TD3 equations are presented as the learner, while state design, action mappings, and security-aware system interaction are described as the paper-specific adaptation.

Its continuous relaxation also illustrates a caution: an argmax produces one-hot association, but it does not automatically enforce every other coupled association/resource constraint. Claim only the constraints established by the decoder.

## 9. Stable invariants and legitimate variants

### 9.1 Stable invariants

| Invariant | Function |
|---|---|
| Opening identifies the sequential/online cause for learning | prevents popularity-based solver selection |
| Agent/controller and information availability are explicit | makes the policy implementable |
| State/observation, action, reward, transition, and horizon are complete or cross-referenced | closes the decision process |
| Action outputs are mapped to physical domains | closes model-to-policy execution |
| Constraint handling distinguishes hard transformations from penalties | prevents false guarantees |
| Standard learner and scenario adaptation are separated | controls novelty claims |
| Update equations follow computational dependencies | makes training reproducible |
| Pseudocode includes collection, storage, target/advantage, updates, and termination | closes training flow |
| Training and execution entities/information are separated | makes deployment claims auditable |
| Deterministic subroutines are inside the interaction and complexity model | closes omitted decisions |
| Complexity separates training from inference | supports online-feasibility claims |

### 9.2 Legitimate variants

| Condition | Legitimate structure |
|---|---|
| MDP fully defined in Problem Formulation | begin with learner/architecture and cross-reference the MDP |
| MDP absent or partial | define the application MDP before learner updates |
| One central controller | one global state/action interface; no CTDE claims |
| Multiple homogeneous agents | shared actor parameters may be stated and justified |
| Heterogeneous agent types | separate observations, actions, rewards, and policies by type |
| Continuous bounded actions | affine/sigmoid/Beta mappings may directly enforce bounds |
| Mixed discrete-continuous actions | use a parameterized action, decoder, hierarchical policy, or deterministic subsolver |
| RL controls one subproblem only | state the remaining solver and execution order |
| On-policy learner | trajectory collection followed by repeated policy/value updates |
| Off-policy learner | replay, target construction, actor/critic update, and target-network synchronization |
| Training cost is very large but inference is small | report both rather than only the favorable one |

### 9.3 Non-transferable details

Do not universalize:

- PPO, TD3, MAPPO, MADDPG, or P-DDQN;
- CTDE when a central manager executes all decisions;
- replay for an on-policy method;
- target networks for a method that does not use them;
- a Gaussian, Beta, categorical, or deterministic policy distribution;
- epsilon-greedy exploration for policy-gradient algorithms;
- a reciprocal, negative-cost, or penalty reward form;
- an action mask, projection, rounding rule, or matching algorithm;
- global state availability during online decentralized execution.

## 10. Default RL section architecture

### 10.1 Opening: why RL and what is proposed

The opening paragraph should contain:

1. the exact sequential uncertainty, observation pattern, or online requirement;
2. why a static/offline solution is insufficient at execution time;
3. why the selected RL family matches the action and agent structure;
4. the genuine adaptation beyond the baseline;
5. the section roadmap.

Do not claim that DRL is required merely because the optimization is non-convex. A static non-convex problem may be better served by other solvers.

### 10.2 MDP/POMDP interface

Define or cross-reference:

| Component | Required content |
|---|---|
| Agent/controller | physical or logical decision maker and deployment location |
| State/global state | Markov information used by centralized learner/critic |
| Local observation | information actually available to each actor at execution |
| Action | one-to-one map to model decisions or named subroutines |
| Reward | objective alignment, constraint terms, scale, individual/shared scope |
| Transition | endogenous effect of action plus exogenous evolution |
| Horizon/discount | finite/infinite horizon and meaning of return |
| Initialization | initial-state source or reset distribution |
| Terminal condition | episode end, task completion, failure, or horizon |

State features must be available before the action and sufficient for the claimed Markov/partial-observation model. Do not include future arrivals or post-decision channel outcomes in a pre-decision observation.

### 10.3 Action realization and constraints

For every action component, state:

- raw network output;
- physical domain;
- mapping/decoder;
- coupling with other components;
- training-time stochasticity;
- execution-time rule;
- behavior when infeasible.

Use the constraint terminology from the shared reference. Penalties guide; mappings, masks, projections, feasible subproblems, or rejection/fallback enforce only their stated constraints.

### 10.4 Learner and architecture

Introduce architecture at the resolution required by the adaptation:

- actor/critic or Q-network inputs and outputs;
- online and target networks;
- global versus local information;
- parameter sharing;
- policy distribution;
- replay or on-policy trajectory buffer;
- auxiliary networks/subroutines;
- the exact point where the proposed mechanism is inserted.

Generic fully connected layer counts belong in experiments unless architecture itself is a contribution.

### 10.5 Update equations

Use one of these dependency chains.

**Off-policy actor-critic:**

`replay sample -> target action -> target value -> critic loss/update -> actor objective/update -> target-network update`

**PPO/MAPPO:**

`trajectory -> return/TD residual -> advantage -> clipped policy objective -> value loss -> entropy term -> repeated mini-batch updates -> policy synchronization`

**Value-based:**

`next-action selection -> target value -> TD loss -> online-network update -> target update`

**Parameterized hybrid action:**

`continuous parameter generation for each discrete action -> Q evaluation -> discrete selection -> target -> Q loss -> parameter-policy loss -> target updates`

Define update cadence such as delayed policy updates, target update frequency, PPO epochs, or buffer thresholds when it changes the algorithm.

### 10.6 Training pseudocode

Include:

1. network/buffer initialization;
2. environment reset;
3. observation collection;
4. exploration/action sampling;
5. decoding/masking/projection/subsolver;
6. environment execution;
7. reward and next observation;
8. transition storage or trajectory completion;
9. target/return/advantage calculation;
10. network updates and synchronization;
11. terminal handling;
12. saved parameters or returned policy.

### 10.7 Execution/deployment

After training, state:

- which parameters are retained;
- which physical entity holds each actor;
- which features it observes;
- whether exploration is removed;
- how the raw output is decoded;
- whether critics/training center are absent;
- communication and auxiliary computation required;
- fallback for an invalid, missing, or unsafe action.

### 10.8 Complexity

Report separately:

- full offline training or per-update training cost;
- online actor/Q inference;
- action decoding/masking;
- deterministic matching/optimization;
- communication or agent-parallel assumptions when central to the claim.

## 11. Single-agent, multi-agent, and hybrid-action variants

These are variants inside the RL route, not separate skills or top-level method types.

### 11.1 Single-agent continuous control

Required emphasis:

- centralized controller and global observation availability;
- continuous action bounds and physical mapping;
- critic target/loss and actor update;
- exploration during training versus deterministic execution;
- online inference plus any deterministic network-routing/resource subroutine.

Do not call central inference `decentralized` merely because actions are sent to several UAVs.

### 11.2 Multi-agent CTDE

Use this matrix:

| Item | Training | Execution |
|---|---|---|
| Actor input | local observation, unless explicitly centralized | local observation required for decentralized execution |
| Critic input | global state and possibly joint actions | critic normally absent |
| Communication | experience/global aggregation and parameter distribution | only communication supported by the deployment claim |
| Exploration | enabled according to learner | disabled or bounded operational exploration |
| Parameters | separate, shared by homogeneous type, or partially shared | downloaded/frozen/updated online as stated |

For heterogeneous agents, define each type's decision responsibility. For cooperative rewards, explain why a shared signal represents the joint objective. For individual rewards, explain coordination or credit assignment.

### 11.3 Hybrid discrete-continuous actions

The Method must answer:

1. Is a continuous parameter vector generated for every discrete choice or only the selected choice?
2. Which network/subroutine selects the discrete choice?
3. How are invalid discrete choices masked or rejected?
4. How are continuous parameters bounded and coupled?
5. Is the training-time relaxation the same as the executed action?
6. Which loss reaches the discrete selector and continuous generator?
7. What is the complexity in the number of discrete choices?

Rounding or argmax alone is not a complete hybrid-action design when decisions have cross-component constraints.

## 12. Paragraph and wording patterns

### 12.1 Problem-to-RL transition

- `Problem (P) requires slot-level decisions under [named uncertainty], whereas solving the full optimization after each change exceeds the decision interval.`
- `Because each UAV observes only [local information] while the objective depends on [global coupling], we adopt a CTDE multi-agent framework.`
- `The action combines [discrete choice] with [conditional continuous parameters], motivating a parameterized hybrid-action learner.`

### 12.2 MDP interface

- `At the beginning of slot t, agent i observes ...`
- `The observation contains ... because these quantities determine ...`
- `The action maps to the model decisions as follows ...`
- `The reward is the negative of [objective] plus [bounded terms]; these penalties discourage rather than preclude violations.`

### 12.3 Architecture

- `During centralized training, the critic receives ..., whereas actor i uses ...`
- `At execution, the critic and exploration process are removed, and each actor maps its local observation to ...`
- `We replace the baseline [interface] with [adaptation] because ...`

### 12.4 Action realization

- `The raw actor output is mapped to [domain] by ...`
- `The mask removes choices that violate ... before sampling.`
- `After the policy selects ..., the deterministic subroutine computes ...`
- `If decoding fails, the controller executes ...`

### 12.5 Training

- `Each interaction produces the transition ..., which is stored in ...`
- `The target is computed before the critic update as ...`
- `The actor is updated every ... critic steps, after which ...`
- `Algorithm 1 consists of experience collection and parameter-update phases.`

### 12.6 Avoided language

- `DRL can solve complex problems, so we use PPO.`
- `The penalty guarantees the energy/collision/deadline constraint.`
- `The agent learns the optimal policy` without a guarantee.
- `Centralized training and decentralized execution` when the actor uses global state online.
- `The continuous output represents the binary action` without decoder and coupling rules.
- `We propose TD3/PPO/MAPPO` when the algorithm is adopted unchanged.

## 13. RL-specific hard gates

Apply these after the shared gates.

1. **Decision-process completeness:** agent, state/observation, action, reward, transition, horizon, initialization, and termination are defined or cross-referenced.
2. **Observability:** every actor input is available at the stated decision time and deployment location.
3. **Markov/partial-observation honesty:** the claimed process matches the information actually supplied.
4. **Action closure:** every original decision is output, decoded, or solved by a named subroutine.
5. **Constraint semantics:** bounds, masks, projections, penalties, and fallback are not conflated.
6. **Reward alignment:** reward direction, aggregation, scaling, and shared/individual scope match the optimization objective.
7. **Learner consistency:** replay/trajectory use, target networks, losses, and update cadence belong to the selected algorithm.
8. **Training dependency:** targets/returns/advantages precede the losses and updates that consume them.
9. **CTDE consistency:** local actor input, global critic input, parameter sharing, and execution communication agree.
10. **Hybrid-action consistency:** discrete selector, conditional continuous parameters, decoder, and learning signals are complete when applicable.
11. **Training-execution separation:** exploration, critics, global information, and action realization are correctly separated.
12. **Terminal handling:** terminal transitions do not incorrectly bootstrap and completion/failure behavior is defined.
13. **Deployment closure:** saved model, inference entity, input, output, decoder, and fallback are explicit.
14. **RL complexity:** training, inference, agents, networks, batch/episode dimensions, and auxiliary modules are scoped.
15. **Novelty boundary:** standard learner equations are not presented as the paper's algorithmic contribution.

## 14. Anti-patterns

### 14.1 Generic DRL tutorial before the problem interface

**Symptom:** several pages define MDPs and neural networks before the reader knows the controller, information, or decisions.

**Repair:** open with the exact online/partial-observation/action-structure difficulty; retain only learner concepts used by the proposed adaptation.

### 14.2 State as a feature inventory

**Symptom:** every available parameter is placed in the state without timing or Markov justification.

**Repair:** state the decision instant, why each feature affects transition/reward, and whether the executing actor can observe it.

### 14.3 Missing decisions

**Symptom:** the formulation optimizes association, resources, and trajectory, but the action contains trajectory only.

**Repair:** identify the matching/optimization subroutine for the remaining variables and put it inside the step loop and complexity analysis.

### 14.4 Penalty-as-guarantee

**Symptom:** collision or deadline penalties are said to ensure safety/QoS.

**Repair:** use `discourages` or add an actual mask, projection, shield, feasible subproblem, or rejection fallback and state its exact scope.

### 14.5 CTDE label mismatch

**Symptom:** decentralized actors require global positions/actions or a central critic online.

**Repair:** change the deployment claim, restrict actor observations, or specify the online communication that makes global information available.

### 14.6 Training and execution mixed together

**Symptom:** exploration noise, replay sampling, or critic evaluation appears in the online control description.

**Repair:** write separate training and inference flows, including the saved parameters and decoder.

### 14.7 Hybrid action by naive rounding

**Symptom:** all binary/integer variables are rounded independently despite coupling constraints.

**Repair:** use joint decoding, masks, parameterized actions, a hierarchical selector, or a feasible deterministic subproblem.

### 14.8 Loss equations in textbook order rather than computation order

**Symptom:** actor loss is presented before the target/advantage or network inputs it requires.

**Repair:** reorder formulas to match one executable update.

### 14.9 Hyperparameter-heavy method

**Symptom:** layer sizes, learning rates, replay capacity, and episode count interrupt the mechanism story.

**Repair:** keep only method-defining quantities and move experimental values to the setup table.

### 14.10 Inference complexity omitted

**Symptom:** a paper claims real-time execution but reports only training convergence or asymptotic training cost.

**Repair:** count the actor/Q forward pass, action decoding, auxiliary solver, and required communication per decision step.
