# MEC Experimental-Section Writing Skill Design

**Date:** 2026-07-19
**Status:** Approved architecture; awaiting written-spec review
**Repository:** `mec-research-wiki`

## Objective

Create one repository-local skill, `writing-mec-experiments`, for drafting, revising, and auditing Experimental Studies, Simulation Results, Performance Evaluation, and numerical-results sections in MEC, UAV-MEC, HAP-MEC, vehicular edge computing, and related optimization papers.

The skill must route internally between evolutionary-algorithm and reinforcement-learning evidence patterns while preserving one shared writing discipline. It must reproduce the organization, evidence density, and bounded claim style found in the approved reference papers without depending on repository-local or machine-specific source paths.

## Approved Decisions

- Create one skill at `.agents/skills/writing-mec-experiments/`; do not create separate evolutionary and reinforcement-learning skills.
- Use a concise router in `SKILL.md` plus three one-level reference files.
- Treat the user's proposed two-paragraph pattern as a reusable rhetorical unit, not an inflexible paragraph count.
- Define that unit as an **experiment contract block** followed by an **evidence-to-claim block**.
- Let a simple experiment use one two-block unit; let a complex subsection repeat the unit for each distinct evidence artifact or subquestion.
- Require reinforcement-learning papers to establish training credibility before using learned-policy results to support system-level claims.
- Keep all instructions and reference material in English so the skill matches the repository's other MEC writing skills.
- Record reference provenance bibliographically rather than by absolute or repository-relative source paths, making the skill publishable.
- Include no audit script in the initial version. Evidence semantics and causal restraint require judgment; deterministic structural checks will validate the skill package itself.

## Alternatives Considered

### 1. Router plus shared and family-specific references — selected

Keep the operational workflow in `SKILL.md`, common evidence rules in one reference, and evolutionary and reinforcement-learning rules in separate references. This provides progressive disclosure, keeps the trigger surface unified, and prevents one algorithm family from diluting the other.

### 2. One monolithic `SKILL.md` — rejected

A single file would be easy to distribute but would load both families for every task, become unnecessarily long, and make shared rules and family-specific rules difficult to maintain independently.

### 3. Router and references plus an automatic prose auditor — deferred

A script could count figure mentions, numerical anchors, or paragraphs, but those proxies cannot determine whether budgets are fair, a statistic supports the stated claim, or a causal explanation is warranted. Such a script could create false confidence. It may be added later only for narrowly deterministic checks.

## Source-Grounded Findings

### Evolutionary-algorithm references

The design is grounded in the experimental sections of:

- *Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing: A Joint Energy and Delay Optimization*;
- *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks: A Joint Optimization Approach for Reliability and Latency*;
- *Terrain-Aware UAV-Enabled Mobile Edge Computing in Urban Environments: A Constrained Multi-Objective Approach With Task-Adaptive Mechanism*;
- *Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing: A Multi-Objective Optimization Approach*;
- the HAP manuscript supplied with the task.

Across these sources, simple ablation, mobility, runtime, and scenario-comparison experiments generally use two natural paragraphs. The first identifies the question, controlled comparison, metric, repetition protocol, and figure or table. The second gives the overall answer, selected quantitative evidence, trend or exception, physical or algorithmic explanation, and a bounded takeaway.

Overall algorithm comparisons often contain several evidence channels: an aggregate statistical table, Pareto-front plots, and convergence curves. These subsections repeat the same contract/evidence logic for each channel rather than fitting the entire subsection into exactly two paragraphs.

### Reinforcement-learning references

Representative local papers using DDPG, MADDPG, MAPPO, PPO, TD3, and value-based deep reinforcement learning show an additional evidence layer. Before system-performance claims, they establish whether learning is credible through convergence behavior, hyperparameter selection, component ablation, and variability across runs or seeds. They then evaluate the learned policy with physical system metrics, interpret its decisions, and test generalization or robustness.

The sources also expose recurring weaknesses that the skill must correct: conflating training reward with system performance, omitting training/test distinctions, selecting hyperparameters on reported test cases, reporting smoothed curves without seeds or uncertainty, and calling sensitivity results robustness.

## Core Rhetorical Unit

### Block 1: Experiment contract

Open with the experiment's question or hypothesis. State the contribution claim being tested, the compared variants or changed factor, the variables held fixed, the evaluation metric, the run and aggregation protocol, and the relevant figure or table. Refer to global settings instead of repeating them. Do not reveal the result in this block.

### Block 2: Evidence to claim

Open with the answer to the experiment question. Support it with the smallest sufficient set of exact values, statistically meaningful differences, trends, and exceptions. Explain the observation through the modeled system or proposed mechanism. End with a conclusion bounded by the tested conditions and the evidence actually reported.

Do not force exactly two natural paragraphs. Split or repeat the unit when a subsection answers multiple questions or contains statistically distinct artifacts. Do not combine unrelated tables, Pareto fronts, convergence curves, and policy visualizations into one oversized result paragraph.

## Skill Layout

```text
.agents/skills/writing-mec-experiments/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── experiment-contract-and-quality-gates.md
    ├── evolutionary-algorithm-experiments.md
    └── reinforcement-learning-experiments.md
```

### `SKILL.md`

Provide the trigger, routing decision, required reference-loading rules, end-to-end drafting and audit workflow, output contract, and compact stop conditions. Route mixed methods to both family references while maintaining one claim-to-experiment ledger.

### Shared reference

Define the experiment contract, evidence-to-claim block, claim-to-experiment ledger, chapter-level evidence map, quantitative writing rules, causal-language boundaries, paragraph organization, vocabulary, common failure modes, and final audit.

### Evolutionary reference

Define the expected chapter sequence, fair function-evaluation budgets, population and generation reporting, independent runs, IGD and HV construction, feasibility failures, representative-run selection, Pareto-front interpretation, convergence analysis, ablation, sensitivity, scalability, runtime, and multiobjective claim boundaries.

### Reinforcement-learning reference

Define the expected chapter sequence, environment and training reproducibility, train/validation/test separation, random seeds, checkpoint and hyperparameter selection, convergence evidence, learning-component ablation, test-time physical metrics, policy interpretation, generalization, robustness, failure resilience, distribution shift, and offline-versus-online complexity.

## Required Workflow

1. Inspect the manuscript's stated contributions, model, objective, constraints, algorithm family, available figures, tables, logs, and numerical data.
2. Classify the method as evolutionary, reinforcement learning, or mixed and load the shared reference plus the applicable family reference or references.
3. Build a claim-to-experiment ledger before drafting. For every contribution claim, record the experiment question, comparison or independent variable, controls, metric and statistical unit, artifact, falsifying outcome, and maximum supported conclusion.
4. Build an evidence map for the whole section. Assign every figure and table one primary question and one primary claim; remove duplicate artifacts and unsupported claims.
5. Draft setup information once. Keep global parameters, datasets, hardware, baselines, budgets, repeated-run protocol, and metric definitions out of individual experiment contracts unless the experiment changes them.
6. Draft each experiment using one or more contract/evidence units.
7. Reconcile every number, comparison direction, unit, denominator, percentage, and significance claim against the source artifact.
8. Audit chapter order, paragraph-opening center sentences, evidence coverage, family-specific fairness, causal restraint, and conclusion boundaries.
9. Return the revised section together with a compact audit of unresolved evidence gaps; never invent missing values or experimental procedures.

## Chapter Organization

### Evolutionary-algorithm route

Use experiment-to-contribution roadmap; settings and instances; datasets or scenario construction; baselines and fair budgets; metrics and statistics; scenario or model validation; trade-off and representative-solution analysis; overall performance; Pareto-front and convergence evidence; component ablation; and sensitivity, scalability, runtime, or robustness as supported by the paper.

The order may follow the paper's contribution order, but every subsection must have a distinct evidentiary function.

### Reinforcement-learning route

Use experiment-to-contribution roadmap; environment and system setup; neural and training setup; data or scenario splits; training credibility and hyperparameter selection; learning-component ablation; test-time system performance; learned-decision interpretation; generalization, resilience, robustness, and scalability; and offline training versus online inference efficiency.

Training credibility must precede system-level performance claims unless the paper uses a non-learning inference method. Reward curves alone cannot establish superiority on latency, energy, feasibility, reliability, or QoS.

## Evidence Ledgers

Every route must record:

| Claim | Experiment question | Comparison or independent variable | Held fixed | Metric and statistical unit | Artifact | Falsifying outcome | Maximum supported conclusion |
|---|---|---|---|---|---|---|---|

The evolutionary route additionally records evaluation budget, population, independent runs, reference-front or HV-reference construction, representative-run rule, feasibility-failure semantics, and significance test.

The reinforcement-learning route additionally records train/validation/test definition, seeds or independent runs, training budget, checkpoint rule, smoothing and interval construction, evaluation episodes, and generalization axis.

## Quality Gates

### Shared gates

- Give every experiment one explicit question and every figure or table one primary role.
- Begin each paragraph or evidence block with a center sentence that advances the section's evidence story.
- Keep one primary center sentence per paragraph; add a secondary center sentence only when it develops a subordinate, directly related point.
- State the overall answer before listing detailed values.
- Use a small number of discriminating quantitative anchors rather than narrating every plotted point.
- Distinguish relative improvement from percentage-point change and name the denominator.
- Treat statistical association, modeled explanation, and experimentally isolated causality as different claim strengths.
- Report exceptions and scale-dependent reversals instead of hiding them.
- End with an insight tied to the tested conditions, not a generic superiority claim.
- Do not repeat captions, global setup, metric definitions, or the same conclusion across subsections.
- Do not invent values, baselines, seeds, budgets, confidence intervals, significance, or causal mechanisms.

### Evolutionary gates

- Check equal function-evaluation or equivalent computational budgets.
- Distinguish independent runs from solutions in a nondominated set.
- Define the IGD reference set and HV reference point when they affect reproducibility.
- State how a representative run was chosen.
- Define zero, NaN, missing, and infeasible outcomes.
- Do not infer stability from a mean or a single run.

### Reinforcement-learning gates

- Label every curve as training or evaluation return and state aggregation and smoothing.
- Keep hyperparameter and checkpoint selection separate from final testing.
- Compare learning methods under equivalent training and information budgets.
- Evaluate physical objectives and constraint outcomes in addition to reward.
- Require multiple runs or seeds and uncertainty before claiming stability.
- Reserve generalization for unseen conditions, robustness for explicit perturbations or uncertainty, and resilience for failures and recovery.
- Separate offline training cost from online inference, decoding, and embedded optimization cost.

## Style and Portability

Write the skill and all references in English. Use direct IEEE-style technical prose: purpose-led center sentences, controlled comparisons, precise numerical anchors, mechanism-based explanations, and bounded conclusions. Avoid promotional adjectives, caption paraphrases, exhaustive point-by-point narration, and paper-by-paper literature exposition.

Do not include absolute paths, local usernames, repository-only links, or instructions requiring the original raw corpus. Identify provenance with paper titles and the structural observations derived from them. A published copy of the skill must remain usable without this repository.

## Verification Strategy

Because subagent forward-testing is unavailable under the active collaboration policy, use deterministic contract tests and manual forward tests with fresh task fixtures.

### RED baseline

Before creating the skill, run checks that require the approved folder, trigger metadata, router, three references, core rhetorical unit, evolutionary gates, reinforcement-learning gates, portability rules, and test prompts. Confirm that these checks fail because the skill does not yet exist.

### GREEN and refactor

After implementation:

1. run the same contract checks and require all assertions to pass;
2. run `quick_validate.py` against the skill directory;
3. verify `agents/openai.yaml` against the final skill and its trigger;
4. scan for unfinished markers, placeholder text, machine-specific paths, and raw-source path dependencies;
5. verify every reference is linked directly from `SKILL.md` and every reference longer than 100 lines has a table of contents;
6. forward-test an evolutionary prompt, a reinforcement-learning prompt, and an adversarial audit prompt against the written rules;
7. run `git diff --check` and inspect the scoped diff before committing.

The adversarial audit fixture must include tempting but invalid claims such as stability from one run, robustness from a smooth reward curve, superiority from reward alone, unequal evaluation budgets, and a relative-improvement percentage with an unstated denominator. The skill must direct the agent to reject or qualify each claim.

## Acceptance Criteria

The implementation is complete when:

1. one discoverable `writing-mec-experiments` skill routes correctly among evolutionary, reinforcement-learning, and mixed methods;
2. simple experiments follow the contract/evidence unit without forcing complex subsections into exactly two paragraphs;
3. evolutionary outputs enforce fair multiobjective evaluation and reproducible Pareto evidence;
4. reinforcement-learning outputs separate learning credibility from test-time system performance;
5. all quantitative and causal claims are traceable to supplied artifacts and bounded by tested conditions;
6. the package contains no machine-specific or repository-dependent source paths;
7. metadata, references, structural checks, manual forward tests, and `quick_validate.py` pass;
8. only the new skill and its approved design artifacts are committed, leaving unrelated manuscript changes untouched.

## Delivery Boundary

Implementation changes are limited to this design specification and the new `.agents/skills/writing-mec-experiments/` directory. No manuscript section, raw source, existing writing skill, or unrelated dirty file may be modified. The design specification is committed separately before implementation. The implemented skill will be committed and pushed only after all validation gates pass.
