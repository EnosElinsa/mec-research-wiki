# Modeling, formulation, and writing gates

## 1. Architecture inheritance ledger

Complete before revising an existing model:

| Element | Reference/current backbone | Keep | Adapt | Add | Remove | Reason and evidence |
|---|---|---:|---:|---:|---:|---|

Elements include:

- entities and roles;
- spatial topology;
- timing and decision cadence;
- workflow/event order;
- channel, rate, computing, queue, mobility, energy, and reliability models;
- state and action spaces;
- objective definitions;
- constraint families;
- success/failure/terminal behavior.

Any top-level reordering, section split, or notation replacement needs a dependency or correctness reason recorded in the ledger. Stylistic preference is insufficient.

## 2. Model contract table

Create a symbol ledger before prose:

| Symbol | Kind | Meaning | Indices | Domain/unit | Defined at | Observed/decided/realized when | Used by |
|---|---|---|---|---|---|---|---|

Kinds: set, index, parameter, exogenous observation, state, decision, auxiliary variable, metric, objective, constraint indicator.

Hard rules:

- one symbol has one meaning;
- singular/plural, scalar/vector, and set notation remain distinct;
- all index ranges are explicit;
- units are compatible across every sum, ratio, and update;
- binary, integer, and continuous domains are stated;
- a notation table may summarize but cannot be the first definition of a symbol used in prose or equations.

## 3. Causal dependency graph

For each equation, record its inputs and outputs. Topologically sort the graph. The prose/equation order should follow that sort except for a clearly signposted self-contained module.

Examples:

`position -> distance/elevation -> channel gain -> rate -> transmission time -> waiting time`

`CPU allocation -> processed bits -> queue update -> generated state -> sync backlog`

`assignment -> active user set -> bandwidth/CPU capacity -> cost`

`current position + action -> travel time -> arrival time -> service window -> next state`

Fail if an equation uses an undefined output from a later module without an explicit forward reference.

## 4. Paragraph and equation pacing

Use this local pattern:

> [Operational center sentence.] Under [necessary assumption], define [primitive quantity and domain]. The resulting [named metric] is
>
> \[\text{equation}\]
>
> where [only the remaining local parameters]. This relation shows [paper-relevant coupling]. To ensure [physical requirement], impose
>
> \[C_k: \text{constraint}.\]

Do not force every paragraph to use every role. Keep one dependency chain together and start a new paragraph when the physical operation changes.

## 5. Timing and state gates

For a dynamic model, answer all questions:

1. What interval does slot/cycle `t` denote?
2. At what instant is state `S[t]` measured?
3. Which exogenous variables are observed before the action?
4. Which decisions are selected at that instant?
5. In what order do movement, transmission, computation, state generation, confirmation, and energy accounting occur?
6. Which random quantities realize before and after the action?
7. What is the update to `S[t+1]`?
8. What is the initial state?
9. Are conditional branches mutually exclusive and exhaustive?
10. What happens after success, failure, return, deadline, or horizon end?

Fail if a policy depends on future arrivals/channel/outcomes not available at its decision instant. Fail if two simultaneous operations consume the same resource without an allocation rule. Fail if a quantity is counted both when reserved and when realized.

## 6. Physical and dimensional gates

Check every equation:

- distances use compatible coordinate dimensions;
- rates have data/time units;
- transmission time is data/rate with a defined zero-rate convention;
- CPU service is cycles-per-time times time divided by cycles-per-bit;
- energy is power times duration or a clearly sourced computing-energy relation;
- queue/state updates cannot serve or transmit more work than available unless the surplus convention is explicit;
- probability and reliability expressions stay in valid ranges;
- averages and normalized objectives define their denominators and zero-denominator cases;
- `max`, `min`, indicator, and positive-part operators have stated semantics where nonstandard;
- reserved, incurred, expected, worst-case, and upper-bound quantities are not conflated.

## 7. Constraint placement and closure

Each constraint needs three appearances at most:

1. local physical explanation and formula;
2. inclusion in the final problem display;
3. concise grouping by role.

Do not re-explain the full algebra in all three places. Number constraints continuously when the manuscript uses numbered constraints.

For every constraint, verify:

- all symbols and index sets are defined;
- its activation condition is defined;
- big-M or indicator semantics are valid for inactive cases;
- it is neither duplicated by an equivalent condition nor contradicted by another constraint;
- the constraint can be evaluated under every feasible branch;
- its role is correctly grouped: planning/assignment, kinematic/safety, communication/computing resource, QoS/deadline, energy, reliability, or variable domain.

## 8. Decision and objective traceability

Create the following matrix:

| Decision component | Physical equation affected | Constraint/domain | Objective path | Decision instant |
|---|---|---|---|---|

Fail if a decision has no downstream effect or if an objective depends on an uncontrolled quantity while the prose claims it is optimized.

For each objective, state:

- minimize or maximize;
- instantaneous, average, cumulative, worst-case, or terminal aggregation;
- horizon and population over which it is computed;
- normalization and units;
- special cases;
- why it conflicts with another objective, if a multi-objective problem is claimed.

Do not invent scalar weights when the benchmark formulation is Pareto multi-objective. Do not call a problem dynamic merely because it has time indices; the environment, state, feasible set, or objective must actually evolve.

## 9. Problem Formulation hard gates

Fail and revise if any condition holds:

- the formulation introduces a symbol, state, assumption, or physical relation not modeled earlier;
- the decision vector omits a variable that the paper claims to optimize;
- variable domains are missing or inconsistent with the algorithm representation;
- the objective sign conflicts with the prose;
- a cumulative objective uses future information in an online decision without a policy/expectation formulation;
- the constraint list changes a local constraint's meaning;
- stochastic variables appear without expectation, probability, scenario, robustness, or realization semantics;
- a dynamic/sequential problem is written as a one-shot open-loop vector without justification;
- the closing difficulty paragraph names only `nonconvexity` or `NP-hardness` instead of explicit couplings;
- algorithm-specific operations appear before the algorithm section.

## 10. Model-to-algorithm boundary

The model may define:

- system states and observations;
- physical decisions and domains;
- causal policy class when necessary;
- objectives, constraints, and failure events;
- structural dependencies that motivate a solver.

Defer these to the algorithm section:

- chromosome/neural encoding;
- action masking or repair implementation;
- population/archive operations;
- loss functions and policy updates;
- training schedules;
- heuristic candidate generation;
- complexity of algorithmic loops.

If an algorithm needs a feasibility certificate, the physical feasibility condition belongs in the model; the procedure for computing or enforcing it belongs in the algorithm.

## 11. Language and style

Use center sentences that name the modeled operation:

- `Once the controller determines the assignment, ...`
- `Upon receiving the offloaded tasks, ...`
- `Following data collection, ...`
- `At the end of each cycle, ...`
- `To ensure ..., constraint C_k requires ...`
- `Based on the above models, we formulate ...`

Use `we assume` for a modeling assumption, `we define` for notation, `is given by` for an adopted relation, and `we introduce/design` only for a genuine scenario-specific modeling component.

Avoid vague claims such as `for simplicity` without stating the consequence. Avoid surveying multiple papers inside a model paragraph. One source citation is usually enough to ground an adopted equation or assumption.

After an equation, explain physical meaning, coupling, or a boundary case. Do not simply translate each symbol into prose a second time.

## 12. Final audit sequence

Run in this order:

1. read only subsection headings: do they reproduce the operational flow?
2. read only first sentences: do they form a causal model story?
3. scan first symbol occurrences: is every symbol defined before use?
4. topologically check equation dependencies;
5. check units and domains;
6. simulate one interval by hand, including all branches;
7. trace each decision to objectives and constraints;
8. compare the final formulation against the local constraints;
9. remove duplicated explanations and algorithm leakage;
10. compare against the inheritance ledger to ensure the rewrite did not redesign validated modules without cause.
