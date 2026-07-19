# Reference-Derived Evolutionary Method Analysis

## Contents

1. [Corpus and scope](#1-corpus-and-scope)
2. [Cross-paper structural result](#2-cross-paper-structural-result)
3. [Demand-aware multi-area multi-UAV MEC](#3-demand-aware-multi-area-multi-uav-mec)
4. [Dynamic multi-source vehicular data fusion](#4-dynamic-multi-source-vehicular-data-fusion)
5. [Terrain-aware urban UAV-MEC](#5-terrain-aware-urban-uav-mec)
6. [Reliable dispersed computing](#6-reliable-dispersed-computing)
7. [Dynamic HAP-UAV planning manuscript](#7-dynamic-hap-uav-planning-manuscript)
8. [Stable invariants and legitimate variants](#8-stable-invariants-and-legitimate-variants)
9. [Default evolutionary section architecture](#9-default-evolutionary-section-architecture)
10. [Paragraph and wording patterns](#10-paragraph-and-wording-patterns)
11. [Evolutionary-specific hard gates](#11-evolutionary-specific-hard-gates)
12. [Anti-patterns](#12-anti-patterns)

## 1. Corpus and scope

This analysis is derived from the complete Method/Proposed Algorithm sections of the following benchmark manuscripts, not from their abstracts or titles.

| Benchmark | Publication information | Solver structure emphasized |
|---|---|---|
| *Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing: A Joint Energy and Delay Optimization* | IEEE Transactions on Mobile Computing, 2026, DOI 10.1109/TMC.2026.3697839 | mixed decision encoding, MTCMO baseline, constraint-guided reconstruction |
| *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks: A Joint Optimization Approach for Reliability and Latency* | IEEE Transactions on Wireless Communications, 2026, DOI 10.1109/TWC.2026.3676831 | dynamic CMOP, outer slot loop, cascaded dependency generation, safe default |
| *Terrain-Aware UAV-Enabled Mobile Edge Computing in Urban Environments: A Constrained Multi-Objective Approach With Task-Adaptive Mechanism* | IEEE Transactions on Vehicular Technology, 2026, DOI 10.1109/TVT.2025.3604250 | pre-mission planning, dual populations, history-based adaptive operators |
| *Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing: A Multi-Objective Optimization Approach* | accepted by IEEE Transactions on Mobile Computing, DOI 10.1109/TMC.2026.3679393 | explicit difficulty-to-module mapping, dual populations, partial repair boundary |
| *Dynamic Constrained Multi-Objective Evolutionary Framework for HAP-UAV Planning* | benchmark author manuscript | dynamic response, feasibility injection, one executed solution, horizon complexity |

The first four sources establish the published-paper pattern. The HAP-UAV manuscript is used as an additional architecture benchmark for a dynamic online planning section. No runtime rule depends on a local source path.

## 2. Cross-paper structural result

The benchmark sections consistently tell two nested stories.

### 2.1 Section-level story

`formulated CMOP/DCMOP -> representation of model decisions -> adopted evolutionary framework -> scenario-specific search difficulty -> mechanism that addresses it -> usable output -> computational cost`

### 2.2 Algorithm-level story

`initialize -> generate/evaluate candidates -> apply scenario-specific transformation -> exchange/select -> terminate -> return Pareto set or execute one decision`

The first story explains why the algorithm has its modules. The second explains how those modules run. A strong Method section keeps both visible and aligned.

The shared section hierarchy is not a fixed list of headings. It is a dependency structure:

1. introduce only the evolutionary concepts that the later selection logic needs;
2. define how the problem's decisions are stored in an individual;
3. establish the baseline loop and executor;
4. expand the novel mechanism at the point where it is called;
5. state the handling boundary of every constraint;
6. close the output and cost.

## 3. Demand-aware multi-area multi-UAV MEC

### 3.1 Published organization

The Method section uses:

1. section roadmap and CMOP/Pareto/constraint-violation preliminaries;
2. **Solution Encoding Scheme**;
3. **Proposed Algorithm**;
4. **Constraint-Guided Solution Reconstruction Mechanism**;
5. **Complexity Analysis**.

### 3.2 Center-sentence spine

The opening sentences perform these functions:

1. the section solves the previously formulated bi-objective problem and previews all method blocks;
2. a mixed-integer representation encodes deployment, position, association, bandwidth, and CPU decisions;
3. some constraints are satisfied by the representation or boundary handling, so later repair can focus on the remaining ones;
4. an MTCMO-based two-set framework supplies the standard search, while reconstruction is the paper-specific change;
5. reconstruction follows the causal hierarchy from area assignment to position, association, and resources;
6. complexity equals the baseline evolutionary cost plus reconstruction over infeasible offspring.

Reading this spine alone reveals the whole method logic.

### 3.3 What each block contributes

**Opening and preliminaries.** The paper defines constraint violation, feasibility, Pareto dominance, and the objective vector because those objects are used immediately by CDP, the adaptive epsilon rule, and the returned Pareto set. It does not present a general history of evolutionary optimization.

**Encoding.** Each chromosome component maps directly to a model variable. The text then states which constraints are structurally satisfied: direct user-to-UAV indexing enforces single association, valid deployment gates association, and boundary repair enforces variable bounds. This is more useful than merely listing chromosome length.

**Overall framework.** The control center is identified as the executor. The text distinguishes the adopted MTCMO machinery from the new reconstruction mechanism, then explains two solution sets, genetic generation, information exchange, CDP selection, adaptive epsilon selection, and the returned non-dominated set.

**Reconstruction.** The operation order mirrors decision dependency:

`UAV-to-area assignment -> UAV position -> user-UAV association -> bandwidth/CPU allocation -> re-evaluation`

The paper also states that some constraints are not directly repairable and remain under evolutionary selection pressure. The mechanism therefore has a bounded, auditable guarantee.

**Complexity.** The analysis first gives baseline MTCMO cost, then counts reconstruction of assignment, position, association, and resources, combines the terms, and notes that repair frequency decreases as infeasible offspring become rarer. This last observation explains practical overhead without deleting the worst-case term.

### 3.4 Transferable lesson

When a heterogeneous chromosome contains an upstream assignment and several downstream allocations, the encoding subsection and reconstruction subsection must use the same dependency graph. Changing the assignment without rebuilding the dependent variables produces internally inconsistent candidates even if every scalar remains within bounds.

## 4. Dynamic multi-source vehicular data fusion

### 4.1 Published organization

The Method section uses:

1. section roadmap plus DCMOP/Pareto/constraint-violation concepts;
2. **Key Algorithm Design**;
3. **Proposed Dynamic Response Mechanism**;
4. **Computational Time Complexity**.

There is no separate encoding subsection because the decision vector has already been established and the important method issue is its cross-slot dependency.

### 4.2 Center-sentence spine

1. a DCMOEA extends constrained NSGA-II with a cascaded dependency generation strategy;
2. the UAV runs the method at every slot and centrally produces trajectory, response, collection, compression, and resource decisions;
3. the full algorithm combines an outer dynamic-response loop with an inner static evolutionary loop;
4. a task-status state makes request carry-over explicit;
5. the response mechanism preserves independent components and regenerates dependent decisions in cascade order;
6. after evolution, one feasible solution is selected and executed, or a conservative default is used;
7. complexity combines response cost with static NSGA-II evolution per slot and across the mission.

### 4.3 What each block contributes

**Execution context.** The paper names the UAV as the real-time decision provider and lists the decisions it outputs. This prevents ambiguity about whether the algorithm is an offline planner or an online controller.

**Outer and inner loops.** Algorithm 1 shows a complete time-slot lifecycle: generate requests, respond to environment change, evolve for a fixed number of generations, obtain feasible solutions, select or fall back, execute, update task status, and advance the slot.

**Persistent state.** The task-status vector records requests that remain unanswered. Its initialization and recursion close the connection between the executed response decision and the next slot's arrivals.

**Fallback.** When the evolved population contains no feasible solution, the UAV retains its previous location and sets other decision vectors to zero. This is not an implementation footnote; it is part of operational correctness.

**Dynamic response.** The mechanism preserves UAV location and compression variables because they are outside the dependency cascade. It then regenerates response, collection, and bandwidth decisions in that order. Each formula exists because its output constrains the next decision.

**Complexity.** The paper separately counts static evolution and population response, then states the condition under which static evolution dominates and extends the expression over all time slots.

### 4.4 Transferable lesson

A dynamic evolutionary paper needs more than a static optimizer repeated in a loop. It must identify what changed, what state carries over, how the old population is adapted, what single decision is executed, and how that execution changes the next state.

## 5. Terrain-aware urban UAV-MEC

### 5.1 Published organization

The Method section uses:

1. overview, with lengthy CMOP preliminaries moved to supplementary material;
2. **Representation of the Genetic Encoding Scheme**;
3. **Core Algorithm Design**;
4. **Proposed Task-Adaptive Mechanism**.

The main paper does not include a dedicated complexity subsection. This is a legitimate space-driven variant, not evidence that complexity is generally unnecessary.

### 5.2 Center-sentence spine

1. the section presents encoding, the overall multi-tasking CMOEA, and the adaptive mechanism;
2. a floating-point individual combines B-spline trajectory control points and per-task computing resources;
3. the ground base station performs global planning before the mission using terrain and user information;
4. main and auxiliary populations serve feasibility/convergence and broader exploration roles;
5. historical records connect individual characteristics with effective crossover and mutation choices;
6. the task-adaptive mechanism reuses operators from similar individuals while retaining scheduled random exploration.

### 5.3 What each block contributes

**Preliminary placement.** Standard CMOP background is placed in the supplement, preserving method-section space for the problem-specific representation and adaptation. This supports a general rule: background detail should be proportional to what the reader needs to follow the proposed mechanism.

**Encoding.** The representation reflects the continuous problem: B-spline control points determine the path, while CPU variables determine resource allocation. The representation is described before DE and mutation operate on it.

**Deployment context.** The ground base station runs the algorithm before flight, with DEM data and user distribution as inputs. The output is a complete trajectory and allocation plan. This one paragraph establishes executor, timing, input, and output.

**Framework roles.** The main population prioritizes feasible non-dominated solutions; the auxiliary population relaxes feasibility to explore promising regions. Their cooperation is stated before the record queues and adaptive operators are expanded.

**Adaptive mechanism.** Records contain the individual, constraint-violation vector, objective vector, DE factor, and mutation type. Operator reuse depends on similarity, while the probability of random generation changes over evolution. The mechanism then explains the actual mutation pool, including terrain/smoothness-aware operators, and how successful records are retained.

### 5.4 Transferable lesson

An adaptive-operator contribution needs four explicit elements:

1. what history is recorded;
2. how a new individual retrieves or selects a record;
3. when exploration overrides reuse;
4. how operator success updates the record.

Saying that the algorithm `dynamically selects operators` without this loop is not a method description.

## 6. Reliable dispersed computing

### 6.1 Published organization

The Method section uses:

1. an unusually strong opening that maps two problem difficulties to two method components;
2. **Representation of Encoding Scheme**;
3. **Proposed Constrained Multi-Objective Evolutionary Algorithm Framework**;
4. **Dual-Population Cooperative Mechanism**;
5. **Repairing Constraint-Handling Technique**;
6. **Complexity Analysis**.

### 6.2 Center-sentence spine

1. the CMOP is difficult because convergence, diversity, and feasibility must be balanced;
2. variable/constraint coupling traps feasible search patterns, motivating complementary population roles and offspring sharing;
3. heterogeneous logical, reliability, and capacity constraints fragment the feasible region, motivating direct structural repair;
4. a mixed binary-float individual represents offloading, bandwidth, and CPU decisions;
5. the CMOEA/D-CDP baseline supplies decomposition and neighborhood search;
6. the main population uses CDP, the auxiliary population uses ASF, and both can share offspring;
7. repair directly handles structural assignment and capacity constraints but does not claim to repair reliability;
8. complexity aggregates evaluation, neighbor updates, chromosome length, population size, and generations.

### 6.3 What each block contributes

**Difficulty-to-module opening.** Before any encoding or pseudocode, the paper explains two exact search failures. A small task-assignment change requires coordinated bandwidth/CPU changes and may destroy feasibility. Separately, logical, probabilistic, and capacity constraints make feasible solutions sparse. The two modules then have distinct jobs rather than generic `performance improvement` roles.

**Encoding.** Binary task assignments and floating-point resource decisions occupy separate chromosome portions. The paper states the chromosome length, which is later used in complexity.

**Baseline boundary.** CMOEA/D-CDP decomposition, weight vectors, neighborhoods, and CDP are introduced as adopted machinery. The paper then names the dual-population cooperation and repair as the changes.

**Population cooperation.** Parent selection may be local or global; offspring can update neighbors belonging to either population. Replacement uses CDP for the main population and ASF for the auxiliary population. Thus `cooperation` has a precise information-transfer operation.

**Repair boundary.** The repair directly fixes assignment and resource structure. It explicitly does not verify the probabilistic reliability constraint because that constraint depends on the combination of assigned devices. Reliability remains subject to subsequent evolutionary refinement. This is exemplary guarantee discipline.

**Closing synthesis.** The method section states how CDP, ASF, stochastic repair, and offspring sharing jointly contribute to convergence, diversity, and feasibility. The synthesis follows the operations instead of preceding them as an unsupported promise.

### 6.4 Transferable lesson

When a repair does not cover every constraint, name the uncovered constraint and the operation that still handles it. Rename `feasible-solution repair` to `structural repair` or another bounded term if full feasibility is not established.

## 7. Dynamic HAP-UAV planning manuscript

### 7.1 Organization

The benchmark method uses:

1. a problem link and compact baseline description;
2. **Proposed DCMOEA Framework**;
3. **Feasibility-Driven Dynamic Response Mechanism**;
4. **Computational Complexity Analysis**.

### 7.2 Center-sentence spine

1. the framework solves the previously formulated dynamic constrained multi-objective HAP-UAV planning problem;
2. a standard dynamic constrained NSGA-II variant supplies the baseline selection and variation machinery;
3. the HAP/controller uses current-cycle observations to run dynamic response, static evolution, and one-solution selection;
4. the response mechanism injects diversity while explicitly restoring feasibility of scenario-dependent decisions;
5. each adjustment rule is assigned to the constraint and decision component it controls, with safe fallback behavior;
6. a weighted decision rule chooses one current-cycle plan from the feasible non-dominated set;
7. complexity separates one-generation evolution, response overhead, and the full horizon.

### 7.3 Transferable lesson

For an operational multi-objective controller, returning a non-dominated set is only an intermediate output. The Method section must define the decision rule that chooses the plan executed in the current cycle. The selection weights are operational preferences, not a replacement for multi-objective search.

## 8. Stable invariants and legitimate variants

### 8.1 Stable invariants

The following occur across the benchmark family and should be treated as defaults:

| Invariant | Why it matters |
|---|---|
| Opening links to the exact formulated problem | prevents method-first reasoning |
| Only necessary evolutionary preliminaries are included | preserves resolution for the contribution |
| Representation is explicit for heterogeneous decisions | closes model-to-chromosome mapping |
| Executor, inputs, outputs, and timing are stated | closes deployment semantics |
| Baseline and modification are separated | prevents novelty inflation |
| Scenario-specific mechanisms correspond to named structural difficulties | makes the design causal |
| Constraint ownership is divided among encoding, repair, selection, and fallback | prevents false feasibility claims |
| Overall pseudocode precedes or calls detailed mechanisms | makes control flow reconstructable |
| Prose groups algorithm phases and explains their rationale | avoids a code transcription |
| Dynamic methods select one executable solution and carry state forward | closes the online loop |
| Complexity counts both baseline and added mechanisms | makes scalability claims auditable |

### 8.2 Legitimate variants

| Condition | Legitimate structure |
|---|---|
| Simple, already-defined decision vector | merge encoding into the framework opening |
| Standard preliminaries would consume space | move them to a supplement and retain only used definitions |
| Static pre-mission planning | no outer environment loop or fallback is required unless planning can fail |
| Dynamic time-varying problem | response mechanism before static evolution, followed by execution and state update |
| One genuinely novel mechanism | one dedicated subsection may be sufficient |
| Several mechanisms with different inputs/outputs | one subsection per mechanism in call order |
| Target venue places complexity elsewhere | cross-reference it; do not leave cost claims unsupported |
| No one physical solution must be executed | return the Pareto set, archive, or approximation set explicitly |

### 8.3 Non-transferable details

Do not universalize:

- two populations; some problems need one, more, or a decomposition archive;
- CDP, ASF, epsilon-constraint selection, or NSGA-II;
- SBX, DE, polynomial mutation, or a particular operator pool;
- a repair probability or random threshold;
- weighted-sum selection of one Pareto solution;
- a separate encoding subsection;
- the absence of complexity in one space-constrained paper.

These are selected only when the target problem and baseline require them.

## 9. Default evolutionary section architecture

### 9.1 Opening: problem and roadmap

The opening paragraph should:

1. name the problem number/type;
2. state the exact evolutionary difficulty;
3. name the adopted baseline family;
4. preview representation, framework, proposed mechanisms, output, and complexity.

Use CMOP definitions only if dominance, constraint violation, decomposition, or relaxation is used later and not already defined.

### 9.2 Representation/encoding

For every chromosome segment state:

- corresponding model variable;
- data type and range;
- index order and optional length;
- decode operation;
- constraints satisfied by construction;
- downstream variables invalidated when it changes.

Finish with a constraint-ownership sentence that names what remains for repair or selection.

### 9.3 Overall framework

State in this order:

1. executor and planning/decision time;
2. input information and output artifact;
3. baseline and its inherited steps;
4. population/archive roles;
5. initialization;
6. mating and variation;
7. calls to proposed mechanisms;
8. evaluation and environmental selection;
9. termination;
10. return or executed-decision rule.

### 9.4 Scenario-specific mechanism

Open with the exact failure it addresses. Then specify:

- trigger;
- input candidate/population/state;
- preserved components;
- changed components in dependency order;
- formulas or subroutines;
- constraint boundary;
- output and next consumer;
- update to memory/history, if adaptive.

### 9.5 Operational closure

For static planning, name the returned set or selected plan. For dynamic control, include:

`environment change -> population response -> static evolution -> feasible-set extraction -> one-solution selection/fallback -> physical execution -> next-state update`

### 9.6 Complexity

Use:

`baseline cost + added mechanism cost = combined cost -> dominant term under condition -> full run/slot/horizon cost`

Define population size, objectives, chromosome length, neighbors, generations, slots, and entities before using them.

## 10. Paragraph and wording patterns

### 10.1 Suitable opening language

- `This section develops an evolutionary solution to Problem (P), whose [named coupling] makes direct feasibility preservation difficult.`
- `We build on [baseline] and introduce [mechanism] to address [exact failure].`
- `The method is executed by [entity] at [time] using [inputs] and returns [output].`

### 10.2 Encoding language

- `An individual comprises ...`
- `The first segment encodes ..., whereas the second segment represents ...`
- `This representation satisfies [constraint] by construction because ...`
- `The remaining constraints are handled by ...`

### 10.3 Framework language

- `The main population ...; the auxiliary population ...`
- `At each generation, the method first ..., then ..., and finally ...`
- `The offspring produced in one population may update ... according to ...`

### 10.4 Mechanism language

- `When [trigger], the mechanism preserves ... and regenerates ...`
- `Because [downstream variable] depends on [upstream variable], reconstruction proceeds in the order ...`
- `The rule directly enforces [constraints]; [remaining constraint] is instead handled through ...`

### 10.5 Output language

- `The final population approximates the feasible Pareto set.`
- `The controller selects one feasible non-dominated solution according to the current operating preference.`
- `If the feasible set is empty, the controller executes [defined conservative action].`

### 10.6 Avoided language

- `Genetic algorithms are powerful and widely used. Therefore, we use ...`
- `The repair mechanism guarantees feasibility` when any constraint remains unchecked.
- `The algorithm finds the optimal solution` for an approximate evolutionary search.
- `SBX and polynomial mutation are our innovations` when adopted unchanged.
- `The two populations improve performance` without distinct roles and an exchange operation.

## 11. Evolutionary-specific hard gates

Apply these after the shared gates.

1. **Chromosome closure:** every optimized variable is encoded or delegated to a named subroutine.
2. **Decode closure:** every chromosome can be converted to the exact model decision domains.
3. **Constraint partition:** representation, boundary handling, repair, selection, and fallback have non-overstated responsibilities.
4. **Dependency repair:** upstream changes trigger all required downstream regeneration.
5. **Baseline boundary:** inherited selection and variation are separated from contributions.
6. **Population-role clarity:** every population/archive has a distinct criterion and information exchange operation.
7. **Dynamic-response closure:** changed environment, retained state, response trigger, executed solution, and next state are explicit when dynamic.
8. **Pareto-output closure:** the approximation set and any one-solution execution rule are distinguished.
9. **Fallback closure:** an empty feasible set cannot produce an undefined physical action.
10. **Evolutionary complexity:** evaluation, selection/sorting, proposed mechanisms, generations, and horizon are counted.

## 12. Anti-patterns

### 12.1 Algorithm-brand opening

**Symptom:** the section starts with a tutorial on NSGA-II, DE, or CMOEA/D.

**Repair:** start from the target problem's decision/constraint structure, then introduce the baseline as the carrier of the proposed changes.

### 12.2 Chromosome inventory without semantics

**Symptom:** variables are listed in a vector, but no decode rule or automatically satisfied constraint is stated.

**Repair:** map each segment to the model, domain, consumer, and constraint effect.

### 12.3 Repair in arbitrary constraint-number order

**Symptom:** constraints are repaired C1, C2, C3 only because of numbering.

**Repair:** order repair by causal dependency among decisions, and identify constraints enforced at each stage.

### 12.4 Novelty hidden in generic loop prose

**Symptom:** the proposed mechanism appears as one line inside a long account of tournament selection and mutation.

**Repair:** summarize inherited operations, call the mechanism explicitly in the overall algorithm, and expand it in a dedicated block.

### 12.5 Population labels without cooperation

**Symptom:** `main` and `auxiliary` populations evolve independently or have indistinguishable selection rules.

**Repair:** define distinct roles, selection criteria, and the exact offspring/knowledge exchange.

### 12.6 Dynamic optimizer without execution

**Symptom:** each slot returns a Pareto set but no decision affects the next slot.

**Repair:** add feasible-set extraction, one-solution selection, fallback, physical execution, and state recursion.

### 12.7 Complexity copied from the baseline

**Symptom:** the paper reports only NSGA-II or CMOEA/D complexity despite invoking repair or dynamic response for every candidate.

**Repair:** add each mechanism's cost and state when the baseline term dominates.
