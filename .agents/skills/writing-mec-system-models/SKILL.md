---
name: writing-mec-system-models
description: Use when drafting, revising, or auditing the System Model and Problem Formulation of MEC, UAV-MEC, HAP-UAV, vehicular edge/fusion, dispersed computing, service migration, or constrained/dynamic multi-objective optimization papers—especially when the model lacks a causal workflow, symbols appear before definition, state transitions are incomplete, constraints are detached from physical meaning, the formulation does not match the preceding model, or a rewrite unnecessarily redesigns an established reference architecture.
---

# Writing MEC System Models and Problem Formulations

## Purpose

Build a model section that reads in the order the system operates and a problem formulation that closes—rather than recreates—that model. Preserve an established architecture when one is supplied, introduce only the modules required by the new scenario, and make every state, decision, equation, constraint, and objective causally traceable.

This skill is derived from the System Model and Problem Formulation sections of five benchmark MEC-family manuscripts. Before drafting or auditing, read both bundled references in full:

- `references/reference-system-model-analysis.md` for source-by-source structural evidence.
- `references/modeling-and-formulation-gates.md` for symbol, causality, dimensional, and formulation checks.

The bundled analysis is self-contained. Do not require access to original machine-specific corpus paths.

## Highest-priority rule: inherit before extending

When the user supplies a reference architecture or an existing manuscript, do not redesign the system from scratch. First create an inheritance ledger:

| Model element | Inherited unchanged | Adapted | New | Evidence/reason |
|---|---:|---:|---:|---|

Track at least the entities, time model, operating workflow, communication/computing/energy equations, decision variables, state variables, objectives, and constraint families.

Preserve the backbone's section order and notation unless the new mechanism creates a real dependency conflict. Add scenario-specific modules at the point where their inputs are already defined. Never present inherited equations as new contributions.

## Required workflow

### 1. Recover the system contract

Before prose, identify:

1. actors and indexed sets;
2. operating region and topology;
3. static horizon, mission horizon, or slot/cycle timing;
4. exogenous parameters and observations;
5. system states at a precisely named instant;
6. decision variables and when they are chosen;
7. physical/service events within one decision interval;
8. derived performance measures;
9. feasibility constraints;
10. initial, boundary, terminal, success, and failure conditions.

If any item is missing, mark it as an unresolved model requirement. Do not hide it in an algorithm section.

### 2. Draw the dependency order

Arrange modules by operational and mathematical dependency. Common chains include:

- deployment -> association/channel -> transmission -> computing -> energy/delay;
- mobility -> observation -> uplink -> processing/fusion -> downlink -> reliability/latency;
- assignment -> queue/service -> state generation -> synchronization -> handover -> energy/safe return;
- task description -> heterogeneous processor models -> cost/reliability aggregation.

Prefer this order over a taxonomy of topics. A novel, self-contained model may appear after baseline modules when the benchmark style calls for it, but every forward reference must be explicit and no equation may depend on an undefined quantity.

Do not automatically split `System Model and Problem Formulation` into two top-level sections. The benchmark set supports both combined and separated variants; follow the manuscript's existing architecture and venue convention.

### 3. Write the overview as a model map

Open with one compact paragraph that:

1. states the considered system and controller;
2. names the entities, sets, and time horizon at the level needed to follow the workflow;
3. narrates one complete operating cycle in causal order;
4. states the modeling scope and excluded layer when necessary;
5. previews the model components.

For a dynamic model, define the slot/cycle interval and the exact decision instant before using a time index. For a static model, state what remains unchanged during the optimization horizon.

### 4. Draft each subsystem locally

Each subsystem should normally follow this sequence:

1. **Center sentence:** what operation or physical mechanism is modeled.
2. **Assumptions:** only those needed for the following equations, with source citations where appropriate.
3. **Primitive variables:** define symbols, indices, domains, and units before first use.
4. **Core relation:** present the equation after a sentence naming the quantity it computes.
5. **Derived relations:** build rate -> time -> energy, service -> queue, or state -> utility in dependency order.
6. **Interpretation:** explain the coupling or tradeoff that matters; do not paraphrase every algebraic term.
7. **Local constraints:** introduce each constraint with its physical purpose and explain remaining parameters immediately after it.
8. **Transition:** connect the subsystem's outputs to the next module.

Objectives may be defined inside the subsystem that produces them, as in the benchmarks, then collected in Problem Formulation.

### 5. Close dynamic state evolution

For every dynamic state, specify:

- whether it is measured at slot start, after arrivals, after service, or at slot end;
- initialization;
- update equation;
- the action and uncertainty realized before the update;
- mutually exclusive and exhaustive branch conditions;
- terminal or absorbing behavior when the process succeeds, fails, returns, or leaves service.

State the within-slot event order in prose before coupled recursions. A policy must not use information realized after its decision instant.

### 6. Formulate the optimization problem

Begin with `Based on the above models` or an equivalent logical transition. Then, in this order:

1. name and justify the problem class: static/dynamic, deterministic/stochastic, single/multi-objective, constrained, mixed discrete-continuous, and sequential when relevant;
2. define the complete decision vector or causal policy;
3. describe each component and its domain;
4. define objectives with clear minimization/maximization signs, aggregation horizon, normalization, and special cases;
5. collect all constraints without changing their semantics;
6. group constraints by physical role;
7. state the structural coupling or conflict that motivates the later algorithm.

Do not introduce a new physical assumption, state, or decision for the first time in the final optimization display. Do not describe algorithm operators, encodings, repair rules, neural architectures, or training procedures here.

### 7. Run traceability and consistency gates

Apply every hard gate in `references/modeling-and-formulation-gates.md`. Revise until:

- every symbol is defined before use and has one meaning;
- every decision influences a modeled quantity, objective, or constraint;
- every objective and constraint can be evaluated from the defined model;
- units, indices, time instants, and conditional branches are consistent;
- the final formulation contains exactly the model built above;
- the closing difficulty statement follows from explicit couplings rather than generic nonconvexity rhetoric.

## Writing style

Use compact technical prose with center sentences. Operational transitions such as `Upon arrival`, `After receiving the task`, `Following data collection`, and `At the end of each cycle` are useful when they encode actual event order.

Use citations to justify adopted models or assumptions, not to conduct a literature review. Prefer `Following the model in [x]` followed by the exact adapted relation. Keep novelty rhetoric out of baseline modules; reserve `we design` or `we introduce` for genuinely scenario-specific modeling components.

Do not let notation tables substitute for definitions in the text. Do not use `where` clauses to introduce a dozen unrelated symbols after an equation. Split the dependency chain into readable units.

## Output expectations

When drafting, provide a complete model-to-formulation chain at the requested scope. When auditing, lead with the inheritance ledger, retain the current subsection structure unless a dependency failure justifies changing it, and report a prioritized set of local corrections plus the hard-gate results. Do not produce a replacement model merely because a rewrite is possible. Distinguish architecture failures, causal/state failures, equation/notation failures, and formulation mismatches before proposing changes. Preserve valid existing symbols and equations; make the smallest architecture change that resolves a demonstrated dependency problem.

Do not modify manuscript files unless the user asks for edits.
