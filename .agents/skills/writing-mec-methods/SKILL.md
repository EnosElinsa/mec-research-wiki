---
name: writing-mec-methods
description: Use when drafting, revising, or auditing a Method, Proposed Algorithm, or Solution section for MEC, UAV-MEC, HAP-UAV, vehicular edge/fusion, dispersed computing, or related optimization papers, especially when the solver is a population-based evolutionary algorithm or reinforcement learning method and the section lacks model-to-algorithm closure, clear novelty boundaries, constraint semantics, executable pseudocode, deployment details, or defensible complexity analysis.
---

# Writing MEC Method Sections

## Core principle

Write the Method section as an executable explanation of how the formulated problem becomes valid decisions. Its center-sentence spine must reveal:

`problem structure -> algorithm interface or representation -> overall framework -> scenario-specific mechanisms -> returned or executed decision -> computational cost`

The section is not an algorithm tutorial, a second problem formulation, or an implementation diary. Explain standard machinery only to the resolution required to understand the proposed design. Give the most space to the mechanisms that close difficulties already established by the model and problem formulation.

## Required resources and internal routing

Before every draft or audit, read `references/method-contract-and-quality-gates.md` in full. Then choose one internal route:

- **Evolutionary route:** read `references/reference-evolutionary-method-analysis.md` when the solver uses individuals, populations, genetic operators, Pareto dominance, CMOP/DCMOP search, evolutionary selection, repair, or population cooperation.
- **Reinforcement-learning route:** read `references/reference-reinforcement-learning-method-analysis.md` when the solver uses an MDP/POMDP, policy or value networks, state/observation-action-reward interaction, replay or trajectories, actor-critic learning, or centralized training with decentralized execution.
- **Combined method:** read both references when both solver families perform substantive optimization. This is not a third method type; apply each route only to the component it governs and state their execution order explicitly.

Do not force either route onto a classical optimization, game-theoretic, matching-only, or heuristic-only method. The shared quality gates remain useful, but the family-specific structure may not apply.

The bundled references are self-contained. They identify the benchmark papers bibliographically and do not require access to the original corpus or a machine-specific path.

## Required evidence before drafting

Read the target paper's abstract, Introduction, contribution list, system model, problem formulation, current method text, algorithm boxes, and relevant experimental claims. Recover the following facts from the manuscript rather than guessing from the title:

1. the exact problem class and complete decision vector;
2. the objective, horizon, uncertainty, and constraint families;
3. the structural difficulties that affect solver design;
4. the entity that runs the method, when it runs, and what information it has;
5. the output returned by the method and, if applicable, the decision actually executed;
6. the adopted baseline algorithm and every genuine modification;
7. the evidence that supports each claimed effect of a modification.

If one of these is unresolved, mark it as a method-model gap. Do not conceal it with generic optimization language.

## Workflow

### 1. Establish the problem-method contract

Answer each question in one sentence:

- Why is this solver family suitable for the formulated decision structure?
- What exact feature makes the standard solver insufficient?
- Which method component addresses each feature?
- Which constraints are satisfied by construction, transformed, masked, projected, repaired, penalized, or left to selection/learning?
- Which decisions remain coupled after those operations?
- What does one full run, generation, time-slot response, or training episode produce?
- How is a usable solution selected and executed?
- What happens when no feasible decision is available?

Build a traceability ledger before prose:

| Difficulty from the formulation | Model evidence | Baseline limitation | Proposed component | Component input | Component output | Constraint/objective effect | Supporting analysis or experiment |
|---|---|---|---|---|---|---|---|

Every first-level method component must occupy one row. Merge components that address the same difficulty through the same operation. Remove a component that has no model-side cause or evidence-supported role.

### 2. Separate inherited machinery from contribution

Create a novelty ledger:

| Method element | Standard/adopted | Adapted | New | Citation needed | Claimed role |
|---|---:|---:|---:|---:|---|

Treat standard genetic operators, Pareto dominance, PPO clipping, target networks, replay buffers, ordinary actor-critic losses, and generic network layers as inherited unless the paper changes them materially. Use `we adopt`, `we build on`, or `we employ` for inherited machinery. Reserve `we design`, `we introduce`, and contribution claims for scenario-specific changes.

### 3. Build the center-sentence spine

Draft only the opening sentence of each intended paragraph or functional block. The spine should normally cover:

1. problem-to-method transition and section roadmap;
2. representation or decision-process interface;
3. overall framework and execution setting;
4. each scenario-specific mechanism in dependency order;
5. returned/executed solution and failure behavior;
6. complexity and, where relevant, training-versus-inference cost.

Read those sentences as one passage. Repair missing causes, unmotivated modules, repeated tutorial material, and output gaps before adding equations or pseudocode.

### 4. Apply the selected internal route

#### Evolutionary route

Use this default order, omitting or merging only when the underlying function is genuinely absent:

1. **Method overview and minimal preliminaries.** Link to the formulated CMOP/DCMOP, preview the framework, and define only the dominance, constraint-violation, decomposition, or selection concepts subsequently used.
2. **Solution representation.** Map every chromosome segment to an existing decision variable and state which domain or structural constraints the representation satisfies automatically.
3. **Overall framework.** State the executor, inputs, outputs, adopted baseline, population roles, initialization, offspring generation, selection, termination, and information exchange.
4. **Scenario-specific mechanisms.** Give each mechanism a subsection when it performs a distinct operation such as dependency-aware reconstruction, feasibility repair, dynamic response, adaptive operator selection, or population cooperation.
5. **Operational output.** Identify the returned Pareto set, how one solution is selected for execution, the state carried forward in a dynamic setting, and the fallback when the feasible set is empty.
6. **Complexity.** Decompose the baseline search cost and every added mechanism, then state the dominant per-generation/per-slot and whole-horizon cost under explicit conditions.

Write repair or reconstruction rules in causal dependency order. If changing an upstream decision invalidates downstream decisions, update the upstream decision first and regenerate all dependents before evaluation.

#### Reinforcement-learning route

First determine where the MDP/POMDP is defined:

- If the formulation already defines agents, observations/states, actions, rewards, transitions, and horizon completely, cross-reference it and begin with the learner or architecture.
- Otherwise, define the decision-process interface before the learning updates.

Use this functional order:

1. **Problem-to-RL transition.** Name the sequential uncertainty, dimensionality, partial observability, or online decision requirement that motivates learning.
2. **Decision-process interface.** Define the controller/agents, state or local observations, action, reward, transition, horizon, terminal condition, and information availability.
3. **Action realization and constraint handling.** Explain normalization, bounded transforms, masks, projections, decoding, repair, or fallback rules. Distinguish a hard enforcement rule from a reward penalty.
4. **Base learner and architecture.** Introduce only the policy/value/Q concepts and update equations required by the chosen learner; state centralized/decentralized data flow and parameter sharing where applicable.
5. **Scenario-specific mechanisms.** Explain hybrid-action decomposition, matching, safety layers, policy distributions, attention, hierarchical decisions, or other genuine adaptations after the base learner is clear.
6. **Training algorithm.** Present experience or trajectory collection, target/advantage construction, loss updates, synchronization, stopping, and saved outputs in computational dependency order.
7. **Execution and deployment.** State where training occurs, where inference occurs, which observations are available online, how network outputs become physical decisions, and what happens under infeasible or unavailable actions.
8. **Complexity.** Separate offline training cost from online inference and auxiliary optimization cost. Account for network widths, agents, batches, episodes/steps, and non-neural modules as applicable.

For multi-agent methods, explicitly distinguish local observation, global training state, individual or shared reward, actor input, critic input, parameter sharing, and communication at execution. For hybrid actions, show which component selects the discrete action and which produces its continuous parameters.

### 5. Write equations in computational dependency order

Introduce a quantity immediately before the equation that computes it. After the equation, define remaining symbols and state why the quantity is needed by the next operation.

Typical valid chains are:

- evolutionary: `encoding -> constraint violation -> offspring -> repair/reconstruction -> evaluation -> selection -> returned set`;
- value-based RL: `next action -> target value -> critic/Q loss -> optimizer update -> target-network update`;
- policy-gradient RL: `trajectory/replay sample -> return or advantage -> critic loss -> policy objective -> entropy/regularization -> synchronization`;
- hybrid-action RL: `continuous parameters for each discrete choice -> discrete-action evaluation -> selected hybrid action -> target -> critic and actor updates`.

Do not rederive channel, delay, energy, queue, or reliability equations already established in the system model. Cross-reference them when calculating fitness or reward.

### 6. Make pseudocode and prose agree

Every algorithm box must identify inputs, outputs, initialization, main loop, decision branches, state or population updates, termination, and returned artifact. Use the same symbols and phase names in prose, equations, figures, and pseudocode.

Explain pseudocode by phases and rationale. Line references are useful when they connect prose to a non-obvious phase, but do not paraphrase every line. If a mechanism has its own algorithm box, the overall box should call it using matching inputs and outputs.

### 7. Close execution semantics

For every method, state:

- **executor:** control center, base station, UAV, HAP, distributed agents, or simulator;
- **decision instant:** before a mission, at each slot, after an environment change, or after offline training;
- **observations/inputs:** only information available at that instant;
- **output:** population, Pareto set, policy parameters, action, assignment, trajectory, or resource vector;
- **selection/decoding:** how an internal output becomes one physical decision;
- **fallback:** safe/default behavior when the output is unavailable or infeasible;
- **state carry-over:** what is retained for the next slot, episode, or execution cycle.

An algorithm that returns a Pareto set but never selects an executable solution is incomplete for an online control paper. A trained policy with no online observation and action-realization description is equally incomplete.

### 8. Run the quality gates

Apply every hard gate in `references/method-contract-and-quality-gates.md`, followed by the selected route's gates. In particular, verify:

- every method module has one exact problem-side cause;
- every decision variable appears in the representation/action interface or is solved by an explicitly named subroutine;
- every constraint has an honest handling status;
- standard machinery is not presented as novelty;
- pseudocode, equations, prose, and figures share one execution order;
- training and inference, or static evolution and dynamic response, are not conflated;
- the returned or executed decision is defined;
- the complexity expression includes added modules and states its scope.

## Paragraph and language rules

Use this mechanism-paragraph pattern:

`center sentence -> mechanism role -> inputs -> operation/update -> output -> exact difficulty or constraint closed -> optional transition`

- Give each paragraph one primary rhetorical job.
- Prefer three to six sentences for ordinary mechanism paragraphs.
- Split a paragraph that explains two independent modules or mixes problem motivation with implementation details.
- Use operational verbs such as `encodes`, `observes`, `generates`, `projects`, `repairs`, `evaluates`, `selects`, `updates`, `stores`, `returns`, and `executes`.
- Avoid empty claims such as `improves performance`, `ensures robustness`, `finds the optimal policy`, or `guarantees feasibility` unless the method or analysis establishes the stated scope.
- Put optimizer choices, layer sizes, learning rates, mutation probabilities, and other experimental hyperparameters in the experiment section unless they define the method itself.

## Output constraints

- Match the manuscript's language, notation, citation format, and target-venue section style.
- Preserve valid existing architecture and symbols; make the smallest structural change that closes a demonstrated failure.
- When auditing, report failures by method role and severity before proposing a replacement structure.
- When drafting, provide the complete requested Method text or outline rather than a solver-selection diary.
- Do not modify the system model, problem formulation, experiments, bibliography, or manuscript files unless the user authorizes those edits.
