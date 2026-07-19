# Shared Method Contract and Quality Gates

## Contents

1. [Purpose and evidence boundary](#1-purpose-and-evidence-boundary)
2. [The method-section narrative contract](#2-the-method-section-narrative-contract)
3. [Required pre-draft ledgers](#3-required-pre-draft-ledgers)
4. [Choosing and ordering functional blocks](#4-choosing-and-ordering-functional-blocks)
5. [Paragraph construction](#5-paragraph-construction)
6. [Equation and notation discipline](#6-equation-and-notation-discipline)
7. [Constraint-handling semantics](#7-constraint-handling-semantics)
8. [Pseudocode and prose alignment](#8-pseudocode-and-prose-alignment)
9. [Execution and deployment closure](#9-execution-and-deployment-closure)
10. [Complexity analysis](#10-complexity-analysis)
11. [Citations, claims, and novelty language](#11-citations-claims-and-novelty-language)
12. [Hard quality gates](#12-hard-quality-gates)
13. [Audit output format](#13-audit-output-format)

## 1. Purpose and evidence boundary

A Method section must let a technically competent reader reconstruct the proposed decision procedure without inventing missing interfaces, constraint operations, state transitions, or output-selection rules. It should explain enough inherited machinery to make the proposed changes intelligible, while allocating its detail to the changes that are caused by the paper's problem structure.

The following material belongs elsewhere:

- physical channel, latency, energy, reliability, queue, or mobility derivations already established in the System Model;
- the complete mathematical statement of the optimization problem;
- paper-by-paper algorithm comparisons belonging to Related Work;
- network widths, population sizes, learning rates, mutation rates, and similar experimental settings that do not define the method;
- performance conclusions not yet established by analysis or experiments.

The method may cross-reference those sections. It should not recreate them.

## 2. The method-section narrative contract

The complete section must answer six questions in order:

1. **Why this family?** Which property of the formulated problem makes the solver family suitable?
2. **What is the interface?** How do model decisions and observations become chromosomes, states, actions, fitness/rewards, or subproblem inputs?
3. **What is inherited?** Which baseline framework performs the standard search or learning operations?
4. **What is changed?** Which scenario-specific mechanisms address the exact weaknesses of that baseline on this problem?
5. **What is used?** What population, Pareto solution, policy, decoded action, or fallback is ultimately returned or executed?
6. **What does it cost?** What is the cost per generation, update, slot, episode, inference, and full horizon as applicable?

The center sentences alone should reproduce this chain. A section that starts immediately with equations for a fashionable solver has not established the first question. A section that ends at a training loop or Pareto set without explaining execution has not answered the fifth.

## 3. Required pre-draft ledgers

### 3.1 Problem-method traceability ledger

| ID | Structural difficulty | Exact model/formulation source | Why baseline is insufficient | Method component | Output of component | Evidence for claimed effect |
|---|---|---|---|---|---|---|

Use structural difficulties, not adjectives. Examples include:

- an association decision changes which resource-allocation variables are meaningful;
- a new time slot invalidates a population because task requests and locations changed;
- a local actor cannot observe the global state needed for critic training;
- an action contains a discrete choice and continuous parameters conditional on that choice;
- bounded physical decisions are produced by an unbounded policy distribution;
- a feasible region is fragmented by logical, probabilistic, and capacity constraints.

`Non-convex`, `high-dimensional`, `dynamic`, and `complex` are insufficient unless the next sentence names the specific coupling or information pattern that creates the difficulty.

### 3.2 Decision-interface ledger

| Model decision/state | Domain and time index | Method representation | Transformation/decoder | Evaluated quantity | Final consumer |
|---|---|---|---|---|---|

Every optimized model decision must appear here. If a decision is produced by a deterministic subroutine instead of the main solver, name the subroutine and its inputs. Do not silently drop decisions from the formulation.

### 3.3 Constraint-ownership ledger

| Constraint | Physical role | Handling mode | Responsible operation | Guaranteed? | Residual violation behavior |
|---|---|---|---|---:|---|

Allowed handling modes are defined in Section 7. If several operations share responsibility, state their order. For example, encoding may satisfy one-hot association, projection may enforce bounds, repair may reconstruct resource feasibility, and selection pressure may only encourage a reliability constraint.

### 3.4 Novelty ledger

| Element | Baseline source | Used unchanged | Adapted | New | Paper-specific role |
|---|---|---:|---:|---:|---|

This ledger controls verbs. Standard elements receive factual descriptions and citations. Adapted or new elements receive mechanism-level explanation and bounded contribution claims.

### 3.5 Execution ledger

| Phase | Executor | Available information | Operation | Output | Next consumer | Failure/default branch |
|---|---|---|---|---|---|---|

Use separate rows for offline training, online inference, time-slot response, static evolution, solution selection, and physical execution when those phases exist.

## 4. Choosing and ordering functional blocks

Do not select subsections by copying another paper's headings. Select them by dependency.

### 4.1 Mandatory functions

Every complete method needs these functions, even when some are merged:

- problem-to-method transition;
- decision representation or decision-process interface;
- baseline framework and data/control flow;
- scenario-specific change;
- complete algorithm procedure;
- returned or executed output;
- cost analysis or an explicit, justified placement of that analysis elsewhere.

### 4.2 Optional functions

Include these only when needed:

- preliminaries for a dominance rule, decomposition, advantage estimator, or learner not already defined;
- a separate encoding subsection for a heterogeneous or structured decision vector;
- one subsection per repair, dynamic response, safety, matching, adaptation, or hybrid-action mechanism;
- convergence or theoretical analysis when the paper actually establishes it;
- a separate deployment subsection when training and execution have materially different entities or information.

### 4.3 Dependency rules

- Define a representation before applying operators to it.
- Define states/observations, actions, and rewards before deriving learner updates that consume them, unless the complete MDP has already been defined and is cross-referenced.
- Define the baseline before stating how it is modified.
- Explain an overall algorithm before drilling into a called subroutine, or clearly preview the subroutine when its output is needed first.
- Define a target, return, advantage, or fitness value before the loss or selection rule that uses it.
- Explain action decoding before claiming that a policy produces feasible physical decisions.
- Explain how candidates are evaluated before explaining how they are selected.

## 5. Paragraph construction

### 5.1 Default mechanism paragraph

Use:

`center sentence -> role -> inputs -> ordered operation -> output -> exact problem difficulty closed -> transition`

Example skeleton:

> The dependency-aware reconstruction mechanism restores consistency among association and resource decisions after an upstream assignment changes. Given an infeasible candidate, it first rebuilds the server assignment, then regenerates user associations from the valid server set, and finally normalizes the resources of each reconstructed group. The resulting candidate satisfies the assignment and capacity structure before objective evaluation, reducing the number of offspring discarded solely because downstream variables still reflect an obsolete assignment. The repaired candidate then enters environmental selection.

The example names the mechanism, input, order, output, boundary of the guarantee, and next phase. It does not claim that every remaining constraint is satisfied.

### 5.2 Paragraph roles

- **Opening paragraph:** link the problem to the method family and preview the section.
- **Interface paragraph:** explain what information or decision each representation component carries.
- **Framework paragraph:** describe the executor, phases, information flow, and returned artifact.
- **Mechanism paragraph:** give the scenario-specific transformation and its reason.
- **Algorithm paragraph:** group pseudocode lines into operational phases.
- **Closure paragraph:** explain selection, execution, fallback, and carry-over state.
- **Complexity paragraph:** decompose costs and identify the dominant scope.

Do not combine more than two roles unless the section is extremely short.

### 5.3 Sentence control

- Put the paragraph's governing claim first.
- Introduce one primary mechanism per paragraph.
- Prefer operational subjects: `the controller`, `the main population`, `each actor`, `the decoder`, or `the response mechanism`.
- Use a secondary center sentence only when it develops the same primary role.
- Split a paragraph when it contains a second independent problem, mechanism, or execution phase.

## 6. Equation and notation discipline

### 6.1 Before each equation

State:

- the quantity being computed;
- the operation or reason for computing it;
- the time/population/agent scope when ambiguity is possible.

### 6.2 After each equation

Define only symbols not already defined, then interpret the relation at method resolution. Explain which next operation consumes the result. Do not paraphrase every term.

### 6.3 Symbol inheritance

- Reuse the System Model's symbols for decisions, states, objectives, and constraints.
- Introduce method-only symbols for populations, network parameters, buffers, generations, or temporary variables.
- Do not change a model symbol's meaning in the method.
- Distinguish current, next, target, old-policy, executed, and relaxed variables typographically and consistently.
- Distinguish an agent index from the number of agents and a time-slot index from a training step when both exist.

### 6.4 Formula dependency audit

For every formula, record:

| Formula | Inputs already defined? | Produced quantity | Used by | Duplicates model equation? |
|---|---:|---|---|---:|

Move, revise, or remove a formula that fails the audit.

## 7. Constraint-handling semantics

Use the following vocabulary precisely.

| Handling mode | Meaning | Valid claim |
|---|---|---|
| Representation/encoding | Invalid structures cannot be represented | The named structural constraint is satisfied by construction |
| Bounded transformation | Raw output is mapped into an interval or simplex | The mapped domain constraint is satisfied |
| Masking | Invalid choices are removed before selection | Masked choices cannot be executed under the stated mask |
| Projection | Candidate/action is mapped to a defined feasible set | Only constraints included in the projection are enforced |
| Deterministic repair/reconstruction | Violating components are changed by explicit rules | The specifically checked/repaired constraints are enforced after successful repair |
| Feasible subproblem | A deterministic solver returns a feasible subdecision under stated assumptions | The subproblem constraints hold when the solver succeeds |
| Penalty/reward shaping | Violations reduce fitness or reward | Violations are discouraged; hard feasibility is not guaranteed |
| Selection pressure | Feasible or lower-violation candidates are preferred | Search is guided toward feasibility; individual outputs may remain infeasible |
| Rejection/fallback | Invalid output is not executed and a default is used | Executed behavior follows the fallback rule |

Hard-gate failures include:

- claiming that a penalty `ensures` a constraint;
- saying a repair produces a feasible solution while leaving an unchecked constraint that can still be violated;
- projecting bounds but implying coupled equalities or logical constraints are also enforced;
- rounding a continuous relaxation without resolving coupling among the resulting discrete variables;
- applying a mask whose required information is unavailable to the executing agent.

## 8. Pseudocode and prose alignment

### 8.1 Algorithm-box contract

An algorithm box must expose:

1. inputs and outputs;
2. initialization;
3. loop scope and termination;
4. calls to scenario-specific mechanisms;
5. evaluation or environment interaction;
6. selection or parameter updates;
7. state/population/buffer updates;
8. output selection and return.

### 8.2 Cross-artifact consistency

Audit the algorithm box against the prose, formulas, and figures:

| Phase | Prose | Equation | Pseudocode line | Figure block | Consistent? |
|---|---|---|---|---|---:|

Common defects are:

- a formula updates a target network that the pseudocode never initializes;
- a repair mechanism changes variables absent from the chromosome;
- prose claims decentralized execution while the actor consumes global state;
- pseudocode returns a population while prose claims it returns one executed solution;
- a terminal transition is stored with a bootstrapped target despite the algorithm text saying otherwise;
- complexity omits a matching, decoding, repair, or subproblem solver invoked in every loop.

### 8.3 Line-by-line explanation

Reference line ranges only to anchor phases or non-obvious branches. Explain why those lines exist and what state changes. Avoid prose of the form `Lines 1-3 initialize; Lines 4-6 update; Lines 7-9 repeat` without technical interpretation.

## 9. Execution and deployment closure

### 9.1 Static optimization

State the planning entity, environmental inputs, decision horizon, returned solution set, and decision-maker rule for selecting one plan when needed.

### 9.2 Dynamic evolutionary optimization

State:

- what changes between environments or slots;
- which population/state is carried forward;
- when the response mechanism is triggered;
- what is preserved and regenerated;
- how many static generations follow the response;
- which feasible solution is executed;
- the conservative action when the feasible set is empty;
- how the executed action updates the next state.

### 9.3 Reinforcement learning

Separate:

- **training:** simulator/physical environment, experience collection, learner location, critic/global information, updates, synchronization, saved parameters;
- **execution:** actor location, real-time observation, forward pass, action realization, communication required, fallback, and latency/cost scope.

Do not describe a centralized actor as decentralized execution. CTDE requires local actor inputs at execution even if global information is used by critics during training.

### 9.4 Output truthfulness

Use `optimal` only with a valid guarantee. Evolutionary and DRL papers generally return an approximate Pareto set, a learned policy, a near-optimal action, or the best solution under a stated selection rule. Match the claim to the evidence.

## 10. Complexity analysis

### 10.1 Scope first

State whether the expression covers:

- one offspring, generation, or complete evolutionary run;
- one gradient update, episode, or complete training process;
- one online inference step;
- one time slot or mission horizon;
- serial execution, parallel agents, or wall-clock assumptions.

### 10.2 Evolutionary decomposition

Count at least:

- population initialization/evaluation;
- offspring generation and objective/constraint evaluation;
- sorting, decomposition, or environmental selection;
- repair/reconstruction/adaptation;
- number of generations, slots, or environments.

Give the baseline cost, added mechanism cost, combined expression, and dominance condition. Do not delete an added term merely because it is often smaller.

### 10.3 Reinforcement-learning decomposition

Separate:

- actor and critic forward/backward propagation;
- target networks or multiple critics;
- number of agents and whether they execute in parallel;
- batch size, updates, episodes, and steps;
- replay/trajectory processing;
- masks, matching, projection, optimization subroutines, or hybrid-action evaluation;
- online actor forward pass and decoder cost.

Training complexity and inference complexity answer different deployment questions and should not be merged into one ambiguous expression.

### 10.4 Complexity language

Use `dominates when ...`, `per generation`, `per decision step`, and `over the horizon` with explicit conditions. Avoid `the complexity is low` without a comparator and scope.

## 11. Citations, claims, and novelty language

### 11.1 Citation roles

Method citations support:

- an adopted baseline algorithm;
- a standard operator, loss, estimator, or selection principle;
- an inherited theoretical result or recommended parameter choice.

They do not need paper-by-paper discussion. Cite the primary algorithm paper or authoritative source at the smallest relevant proposition.

### 11.2 Verb discipline

| Status | Preferred language |
|---|---|
| Adopted unchanged | `we employ`, `we adopt`, `following` |
| Adapted | `we adapt ... by`, `we modify ... to` |
| New mechanism | `we design`, `we introduce`, `the proposed mechanism` |
| Empirical effect | `is intended to`, or a bounded claim tied to a cited result/ablation |
| Proven effect | `guarantees` only under the stated assumptions and theorem |

### 11.3 Avoided language

- `state-of-the-art` as a substitute for solver motivation;
- `optimal` for an unconverged learned or evolutionary output;
- `ensures feasibility` for penalty-only handling;
- `robust` without a named uncertainty set, disturbance, or evaluation;
- `real-time` without online operations or latency/complexity support;
- `novel` attached to standard operators or a mere application of a baseline.

## 12. Hard quality gates

Mark each gate `PASS`, `FAIL`, or `NOT APPLICABLE`.

### 12.1 Shared gates

1. **Problem-link gate:** the opening names the exact formulated problem and solver-relevant difficulty.
2. **Interface gate:** every optimized decision is represented, generated, or delegated explicitly.
3. **Information gate:** every algorithm input is available to its executor at the stated time.
4. **Dependency gate:** formulas and mechanisms appear after their inputs and before their consumers.
5. **Constraint-ownership gate:** every constraint has an honest handling mode and guarantee boundary.
6. **Novelty gate:** inherited machinery is separated from adaptations and new mechanisms.
7. **Module-mapping gate:** every first-level module maps to one exact structural difficulty.
8. **Pseudocode gate:** inputs, outputs, loops, branches, updates, termination, and returns are complete.
9. **Artifact-consistency gate:** prose, formulas, figures, and pseudocode describe the same procedure.
10. **Execution gate:** executor, decision instant, inputs, output conversion, and fallback are explicit.
11. **Output gate:** returned and physically executed artifacts are not confused.
12. **Complexity gate:** the scope and all repeatedly invoked modules are counted.
13. **Claim gate:** feasibility, optimality, robustness, convergence, and real-time claims match evidence.
14. **Resolution gate:** standard theory is concise and scenario-specific mechanisms receive the detail.
15. **Section-boundary gate:** no duplicated System Model, Related Work, or experiment-only material remains.
16. **Center-sentence gate:** paragraph openings alone form a complete method story.

### 12.2 Delivery rule

Do not deliver a finished draft with a failed shared gate. For an audit, identify the failure and the smallest correction needed. If the manuscript lacks information required to pass a gate, report the missing contract instead of inventing it.

## 13. Audit output format

Lead with the center-sentence spine, then report failures in this order:

1. method-model or information mismatch;
2. invalid constraint/guarantee semantics;
3. missing execution or output closure;
4. novelty and module-mapping failures;
5. pseudocode/equation inconsistency;
6. complexity and style defects.

Use this table for actionable findings:

| Priority | Location | Failed gate | Evidence | Consequence | Minimal correction |
|---|---|---|---|---|---|

Finish with the full gate table and a corrected subsection/paragraph spine. Do not replace a valid method architecture merely because another organization is possible.
