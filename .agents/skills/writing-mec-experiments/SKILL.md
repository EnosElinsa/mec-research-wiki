---
name: writing-mec-experiments
description: Use when drafting, revising, or auditing Experimental Studies, Simulation Results, Performance Evaluation, ablation, convergence, sensitivity, robustness, or numerical-results sections for MEC, UAV-MEC, HAP-UAV, vehicular edge/fusion, dispersed computing, or related optimization papers, especially when the method uses multiobjective evolutionary algorithms, reinforcement learning, or both and the evidence-to-claim logic, evaluation fairness, training credibility, or paragraph organization is weak.
---

# Writing MEC Experimental Sections

## Core principle

Write the experimental section as a sequence of bounded tests of the paper's claims. Its center-sentence spine must reveal:

`claim map -> reproducible setup -> experiment question -> controlled comparison -> reported evidence -> mechanism-based interpretation -> bounded conclusion`

Use a two-block rhetorical unit, not a compulsory two-paragraph quota:

1. **Experiment contract:** state what is tested, why it matters, what changes, what remains fixed, how evidence is measured, and where it is reported.
2. **Evidence-to-claim:** answer the question, support the answer with discriminating evidence, explain the observation, and end at the strongest conclusion the experiment permits.

A simple ablation or scenario comparison normally realizes the two blocks as two natural paragraphs. A subsection with a statistical table, Pareto fronts, and convergence curves should repeat or split the unit by evidence channel rather than bury all results in one oversized paragraph.

## Required resources and internal routing

Before every draft or audit, read `references/experiment-contract-and-quality-gates.md` in full. Then choose one internal route:

- **Evolutionary route:** read `references/evolutionary-algorithm-experiments.md` when the method uses populations, genetic operators, constrained multiobjective optimization, Pareto dominance, IGD, HV, nondominated solutions, repair, decomposition, or evolutionary selection.
- **Reinforcement-learning route:** read `references/reinforcement-learning-experiments.md` when the method uses an MDP/POMDP, rewards or returns, policy/value/Q networks, replay, trajectories, actor-critic learning, centralized training with decentralized execution, or learned online control.
- **Combined method:** read both family references when evolution and learning each make substantive decisions. This remains one experiment section: assign each experiment to the claim and component it actually tests, and state the execution and evaluation order.

Do not force either family route onto a purely classical optimization, matching, game-theoretic, or heuristic method. Apply the shared contract, then adopt only the family-specific gates supported by the method.

The references are self-contained and identify their calibration papers bibliographically. They do not require the original corpus or any machine-specific path.

## Required evidence before drafting

Inspect the target manuscript's abstract, contribution list, system model, problem formulation, method, current experiment text, captions, tables, figures, supplementary material, and available result files. Recover rather than guess:

1. each contribution claim and the exact mechanism or model feature behind it;
2. each experiment's question, independent variable or comparison, and held-fixed variables;
3. global versus experiment-specific configuration;
4. baselines, ablations, budgets, information access, stopping rules, and failure semantics;
5. metrics, optimization direction, statistical unit, run or seed count, aggregation, uncertainty, and significance procedure;
6. the source value behind every quantitative statement;
7. whether a statement is an observation, an inferred explanation, or an isolated causal effect;
8. the maximum conclusion supported under the tested conditions.

If a required fact is unavailable, mark an evidence gap. Do not fabricate a value, run count, seed, confidence interval, baseline configuration, significance result, or causal mechanism.

## Workflow

### 1. Build the claim-to-experiment ledger

Create one row for every contribution-level empirical claim:

| Claim | Experiment question | Comparison or independent variable | Held fixed | Metric and statistical unit | Artifact | Falsifying outcome | Maximum supported conclusion |
|---|---|---|---|---|---|---|---|

Add the family-specific fields required by the selected reference. A claim without an experiment is unsupported; an experiment without a claim is either exploratory and must be labeled as such or should be removed.

### 2. Build the chapter evidence map

Assign each figure and table one primary question and one primary claim. Organize subsections by evidentiary function rather than by the order in which simulations happened. A typical map contains:

1. a short section roadmap linking experiments to contributions;
2. shared setup, data, instances, baselines, fairness controls, metrics, and statistics;
3. scenario/model validation or architectural comparison;
4. overall performance and behavior evidence;
5. component ablation;
6. sensitivity, scalability, generalization, robustness, or efficiency as justified.

Avoid duplicating one conclusion across a table, a plot, and prose. Give each artifact a distinct role or merge redundant evidence.

### 3. Separate global setup from experiment contracts

Report shared system parameters, datasets, hardware/software, algorithm budgets, baseline definitions, run protocol, metric definitions, and statistical tests once. In an individual experiment contract, report only the settings changed for that experiment and cross-reference the shared setup.

Keep results out of setup paragraphs. A setup paragraph defines how evidence was produced; it does not announce that the proposed method wins.

### 4. Draft the center-sentence spine

Write only the opening sentence of every intended paragraph or evidence block. Read them consecutively. They must tell the complete empirical story without detailed values:

`why this experiment is needed -> how it isolates the question -> what the evidence shows -> why the behavior occurs -> what can be concluded`

Give each paragraph one primary center sentence. Add a secondary center sentence only for a subordinate and directly related point, such as a scale-dependent exception after the overall result.

### 5. Write each experiment as one or more evidence units

For the **experiment contract**, state in this order when available:

`question/purpose -> tested claim -> variants or independent variable -> controls -> repetitions and aggregation -> metric -> figure/table pointer`

For the **evidence-to-claim block**, state:

`overall answer -> key numerical/statistical anchors -> trend and exception -> model/mechanism explanation -> bounded conclusion`

Do not repeat the caption or narrate every plotted point. Use the smallest sufficient set of values that distinguishes the proposed explanation from alternatives.

### 6. Apply the family route

For the **Evolutionary route**, reconcile the function-evaluation budget, population and generation settings, independent runs, feasibility failures, reference-front or reference-point construction, representative-run rule, Pareto evidence, convergence behavior, and statistical comparisons.

For the **Reinforcement-learning route**, establish reproducibility and training credibility before system-level claims. Separate train/validation/test roles, training and evaluation curves, reward and physical metrics, hyperparameter and checkpoint selection, seeds and uncertainty, generalization, robustness, resilience, and offline versus online cost.

### 7. Reconcile every quantitative claim

For each retained number, record its artifact, row/panel, metric direction, aggregation, comparison baseline, and denominator. Recompute relative changes. Distinguish percentage change from percentage-point change. Check whether lower or higher is better and whether the text reports a mean, median, best run, representative run, or individual case.

Do not call a result significant without the stated test and outcome. Do not call a method stable from one run or a mean alone. Do not call an effect robust unless explicit perturbation, uncertainty, or distribution-shift evidence supports that term.

### 8. Run the final audit

Apply every hard gate in the shared reference and then the selected family reference. In particular, verify:

- every contribution claim maps to evidence and every artifact has one primary role;
- every comparison is fair on the budget and information dimensions relevant to the method;
- paragraph-opening center sentences form a coherent evidence story;
- global setup is not repeated inside experiment contracts;
- every exact value and trend matches its source artifact;
- exceptions, infeasible cases, and scale-dependent reversals are reported;
- explanation strength does not exceed the experimental isolation;
- the final sentence of each unit is a bounded conclusion rather than a promotional restatement;
- learning credibility and test-time system performance are not conflated;
- no result required by a claim is silently missing.

## Paragraph and language rules

Use direct IEEE-style technical prose.

- Open a contract paragraph with the experiment question or purpose, not `Figure X shows`.
- Open an evidence paragraph with the overall empirical answer, then point to the supporting artifact.
- Prefer operational verbs: `compares`, `isolates`, `varies`, `holds`, `reports`, `reduces`, `increases`, `converges`, `violates`, `maintains`, and `reveals`.
- Reserve explanatory verbs such as `results from`, `is driven by`, and `demonstrates that` for mechanisms supported by the model or an isolating experiment.
- Prefer three to six sentences for an ordinary evidence unit, but split by rhetorical job rather than by a fixed sentence count.
- Report a few discriminating values, not every coordinate or table entry.
- Name the tested range when ending with a practical or algorithmic insight.
- Avoid `obviously`, `remarkably`, `significantly` without a statistical meaning, `proves optimality`, `always`, `fully validates`, and generic endings such as `therefore, our algorithm is superior`.

## Output constraints

- Match the manuscript's language, notation, citation format, tense, figure/table labels, and target-venue section style.
- Preserve correct existing data and configuration; make the smallest structural change that closes a demonstrated evidence failure.
- When drafting, return the complete requested section or subsection rather than only a writing diary.
- When auditing, report failures by claim and severity before proposing a replacement evidence map.
- Keep the ledger as working evidence unless the user requests it in the manuscript.
- Do not alter the method, system model, bibliography, figures, tables, raw data, or manuscript files outside the user's authorized scope.
- Do not turn the experimental section into Related Work or repeat paper-by-paper literature explanations.
