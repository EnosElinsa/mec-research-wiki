# Experiment Contract and Quality Gates

## Contents

1. [Purpose](#purpose)
2. [Claim-to-experiment ledger](#claim-to-experiment-ledger)
3. [Chapter-level evidence architecture](#chapter-level-evidence-architecture)
4. [The experiment evidence unit](#the-experiment-evidence-unit)
5. [Center-sentence and paragraph logic](#center-sentence-and-paragraph-logic)
6. [Quantitative evidence discipline](#quantitative-evidence-discipline)
7. [Explanation and causal strength](#explanation-and-causal-strength)
8. [Style, wording, and transitions](#style-wording-and-transitions)
9. [Schematic rewrite example](#schematic-rewrite-example)
10. [Drafting procedure](#drafting-procedure)
11. [Audit procedure](#audit-procedure)
12. [Common failures and corrections](#common-failures-and-corrections)
13. [Hard quality gates](#hard-quality-gates)

## Purpose

Use this reference for every evolutionary-algorithm, reinforcement-learning, classical-optimization, or mixed-method experiment section. It governs the evidence logic shared by all solver families.

The experimental section does not merely describe figures. It tests the paper's contribution claims under disclosed conditions. The writing must let a reader recover four things without inspecting the code: what was tested, how it was controlled, what the evidence establishes, and where the conclusion stops.

## Claim-to-experiment ledger

Build the ledger before deciding subsection titles or writing prose:

| Claim | Experiment question | Comparison or independent variable | Held fixed | Metric and statistical unit | Artifact | Falsifying outcome | Maximum supported conclusion |
|---|---|---|---|---|---|---|---|

Use one claim per row. If two mechanisms are claimed independently, give them separate rows even when one ablation table tests both.

Apply these rules:

- Translate a contribution statement into a question that could receive a negative answer.
- Name the comparison or manipulated factor precisely; `different settings` is insufficient.
- Record controls that prevent an alternative explanation, such as equal computation budgets or identical channel realizations.
- Name the statistical unit: seed, independent run, episode, time slot, user, instance, or nondominated set.
- State what result would weaken or falsify the claim. This prevents post-hoc success criteria.
- Write the narrowest conclusion that would remain valid if an untested dimension changed.

An empty artifact cell marks an unsupported claim. An artifact with no ledger row is exploratory evidence and must be labeled as exploratory, assigned a claim, or removed.

## Chapter-level evidence architecture

Design the chapter at two levels.

### Global level

The global sequence normally performs these functions:

1. map experiment groups to contribution claims;
2. disclose common system, data, software, hardware, and algorithm settings;
3. define baselines, ablations, fairness controls, metrics, run protocol, and statistical reporting;
4. validate scenario assumptions, model behavior, or architecture when required;
5. compare overall outcomes;
6. isolate proposed components;
7. test sensitivity, scale, unseen conditions, failures, uncertainty, or cost.

Follow contribution order when it creates a clearer story. Do not preserve this list mechanically when a function is absent.

### Artifact level

Give each figure or table one primary evidentiary role. Examples include:

- a statistical table establishes aggregate performance and variability;
- a Pareto-front plot establishes distribution and trade-off structure in one representative run;
- a convergence curve establishes search or learning behavior over budget;
- a trajectory plot interprets a learned or optimized decision;
- an ablation table isolates a component;
- a sensitivity plot establishes dependence within a tested parameter range.

Do not make three artifacts repeat the same `better than baselines` claim. If two artifacts answer different parts of one question, say which part each answers.

## The experiment evidence unit

Treat the user's two-paragraph pattern as two rhetorical blocks.

### Block 1: Experiment contract

The opening sentence names the experiment question or purpose. The remaining sentences disclose the comparison and evidence protocol:

`question -> tested claim -> variants or independent variable -> controls -> run/aggregation protocol -> metric -> figure/table pointer`

Include only experiment-specific configuration. Cross-reference shared settings instead of repeating them. If no result artifact is yet available, stop after identifying the missing evidence.

Do not announce the outcome in this block. Result language in the contract obscures the boundary between design and interpretation and encourages confirmation bias.

### Block 2: Evidence to claim

The opening sentence gives the overall answer. The remaining sentences support and delimit it:

`overall answer -> quantitative/statistical anchors -> trend or exception -> explanation -> bounded conclusion`

Use at least one quantitative anchor when the artifact contains a discriminating value that materially supports the claim. Use a statistical result when the claim concerns aggregate superiority, variability, or reproducibility.

End by answering the experiment question under the tested conditions. Do not end only by repeating that the proposed method is superior.

### When two natural paragraphs are enough

Use one contract paragraph and one evidence paragraph for:

- a single-factor ablation;
- a mobile-versus-static scenario comparison;
- a runtime or deadline check;
- a single sensitivity curve;
- a simple architecture comparison;
- one focused robustness or failure experiment.

### When to repeat or split the unit

Repeat or split the unit when a subsection contains:

- aggregate statistics plus representative-run geometry;
- Pareto-front quality plus convergence speed;
- training convergence plus test-time system performance;
- several distinct ablations answering different mechanism questions;
- nominal performance plus unseen-condition or failure behavior;
- a main trend plus a scale-dependent reversal requiring a separate explanation.

Do not turn `two blocks` into `exactly two paragraphs` when doing so creates a dense catalogue of unrelated evidence.

## Center-sentence and paragraph logic

Each paragraph needs one primary rhetorical job and one primary center sentence at its beginning.

Valid primary jobs are:

- introduce the purpose and tested claim;
- define a controlled comparison;
- state an aggregate result;
- explain one evidence channel;
- identify an exception;
- interpret one mechanism;
- delimit the resulting conclusion.

A paragraph may contain a secondary center sentence when it introduces a subordinate point that depends on the primary result. For example, after stating the overall advantage, a secondary sentence may introduce an exception on the largest instance. It must not launch an unrelated experiment.

Read only the opening sentences of all paragraphs. They must form a complete evidence story. Repair these spine failures before polishing sentences:

- setup appears before the reader knows what it validates;
- a result appears without a declared comparison;
- an ablation appears before the full method is established;
- convergence and final performance are treated as the same claim;
- a paragraph changes from one metric or scale question to another without a new center sentence;
- the conclusion introduces a new mechanism not established earlier.

Paragraph length is a consequence of rhetorical load. Three to six sentences is a useful default for an ordinary unit, but the hard rule is one coherent job, not a sentence quota.

## Quantitative evidence discipline

### Reconcile before writing

For every number, retain a private trace containing:

`artifact -> row/panel/curve -> case -> metric -> direction -> aggregation -> reported value -> comparison value -> denominator`

Check units, signs, decimal precision, and whether the source reports a mean, median, best run, worst run, representative run, or individual realization.

### Relative changes

For a minimization metric, a reduction relative to baseline is:

\[
\frac{x_{\mathrm{base}}-x_{\mathrm{proposed}}}{x_{\mathrm{base}}}\times 100\%.
\]

For a maximization metric, an increase relative to baseline is:

\[
\frac{x_{\mathrm{proposed}}-x_{\mathrm{base}}}{x_{\mathrm{base}}}\times 100\%.
\]

Name the baseline or denominator in prose. Do not reverse the direction to produce a larger percentage. If a denominator is zero or undefined, report the absolute difference or another defined comparison.

Distinguish a relative percentage from a percentage-point change. Moving from 70% to 80% is a 10-percentage-point increase and approximately a 14.3% relative increase.

### Statistical claims

- Report the number of independent statistical units.
- Pair a mean with dispersion when variability matters.
- State the confidence level when reporting an interval.
- State the test, comparison family, and outcome before using `statistically significant`.
- Do not convert a nonsignificant difference into equivalence without an equivalence design.
- Do not infer stability from a mean, one curve, or a selected run.
- Do not compare overlapping smoothed bands as though they were a formal significance test.

### Select evidence rather than transcribing it

Use values that establish:

- the main effect against the closest baseline;
- the effect of the proposed component;
- a scale or operating-regime change;
- an exception or failure boundary;
- the magnitude relevant to the paper's practical claim.

Do not list every point, row, or algorithm when the artifact remains available to the reader.

## Explanation and causal strength

Match wording to experimental isolation.

### Descriptive observation

Use `shows`, `reports`, `is lower`, `increases with`, or `remains feasible` when the artifact establishes a pattern but not its cause.

### Model-consistent interpretation

Use `is consistent with`, `can be explained by`, `reflects`, or `is attributable in the model to` when the explanation follows from known equations or system behavior but was not isolated experimentally.

### Isolated mechanism effect

Use `demonstrates the contribution of`, `results from`, or `is driven by` only when an ablation or controlled comparison changes that mechanism while holding plausible alternatives fixed.

### Formal guarantee

Use `guarantees`, `proves`, or `ensures` only when a theorem, construction, or exhaustive condition establishes the scope. Empirical evidence alone does not prove optimality, universal feasibility, or convergence to a global optimum.

Always report competing explanations or exceptions that remain plausible. A mechanism-based explanation should connect the manipulated factor to an intermediate system effect and then to the measured metric.

## Style, wording, and transitions

### Preferred openings

- `We first examine whether ...`
- `This experiment isolates the effect of ...`
- `To evaluate performance as ... increases, ...`
- `Table X compares ... under the common budget in Section ...`
- `The results show that ... across ...`
- `The advantage narrows on ... because ...`

Use these as rhetorical patterns, not mandatory sentence templates.

### Preferred verbs

Use precise operations and observations: `varies`, `holds fixed`, `samples`, `averages`, `compares`, `reduces`, `increases`, `maintains`, `violates`, `converges`, `generalizes`, `recovers`, and `requires`.

Avoid promotional or empty verbs: `outperforms greatly`, `proves effectiveness`, `fully validates`, `works well`, and `achieves excellent performance`.

### Transitions

Use a transition only when it names the evidentiary relationship:

- full method to ablation: `Having established the aggregate advantage, we next isolate ...`
- nominal to scale: `We then examine whether this advantage persists as ...`
- convergence to system outcome: `Convergence establishes trainability; the next experiment evaluates the resulting policy on ...`
- result to exception: `This pattern changes on the largest instance, where ...`

Avoid mechanical enumeration such as `Next, Fig. 7 is analyzed`.

### Figure and table references

Introduce an artifact through its question, comparison, or evidentiary role. Do not open every paragraph with the artifact label. Do not restate axis labels or captions unless a nonstandard convention must be clarified.

## Schematic rewrite example

### Weak

> Figure 6 shows the results of different methods. Our method performs best in all cases and is more robust. As the load increases, all methods become worse. This proves the effectiveness and superiority of the proposed mechanism.

This paragraph lacks an experiment contract, quantitative/statistical scope, a defined meaning of robustness, a mechanism explanation, and a bounded conclusion.

### Stronger structure

> This experiment isolates whether the proposed feasibility mechanism preserves valid decisions as the offered load increases. The full method is compared with a variant that removes the mechanism under identical instances, evaluation budgets, and aggregation settings, and Fig. 6 reports their feasible-solution rates over the tested load range.
>
> The full method maintains the higher feasible-solution rate throughout the tested range, with the separation becoming more pronounced at high load. The widening gap is consistent with the mechanism repairing dependencies that are activated more frequently when resources become scarce. These results therefore support the mechanism's contribution to feasibility under the evaluated load conditions; they do not establish robustness to untested disturbances.

The stronger version illustrates structure and claim boundaries. Insert exact values only after reconciling them with the supplied artifact.

## Drafting procedure

1. Copy contribution claims into the ledger.
2. Convert each claim into a falsifiable experiment question.
3. Inventory figures, tables, logs, and result files.
4. Assign every artifact one primary role.
5. Separate common setup from experiment-specific controls.
6. Draft the paragraph-opening center-sentence spine.
7. Write each contract without result language.
8. Write each evidence block from overall answer to bounded conclusion.
9. Reconcile all values and statistical qualifiers.
10. Apply the relevant family-specific gates.
11. Read only the opening and closing sentence of every unit to verify question-answer closure.
12. Report missing evidence rather than smoothing it over with prose.

## Audit procedure

Audit in this order:

1. **Coverage:** Does every empirical contribution have a mapped experiment?
2. **Purpose:** Is every subsection's question stated before its configuration?
3. **Control:** Can the comparison isolate the stated effect?
4. **Fairness:** Are budgets, information, data, and stopping conditions comparable?
5. **Reproducibility:** Can a reader reconstruct the reported unit and aggregation?
6. **Traceability:** Does every number match an artifact and direction?
7. **Statistics:** Are variability and significance claims supported?
8. **Explanation:** Does the mechanism chain follow from the model or an ablation?
9. **Scope:** Is the conclusion limited to tested cases?
10. **Story:** Do center sentences form a coherent contribution-to-evidence sequence?

Classify failures:

- **Critical:** fabricated or irreconcilable number, unfair comparison, train/test leakage, missing statistical unit, unsupported causal or robustness claim.
- **Major:** missing experiment purpose, missing control, repeated setup, absent mechanism explanation, combined unrelated evidence channels.
- **Minor:** weak transition, caption repetition, excessive point listing, imprecise verb, avoidable paragraph density.

## Common failures and corrections

| Failure | Why it fails | Correction |
|---|---|---|
| Begin with `Figure X shows` | Hides the question and claim | Open with purpose or overall answer |
| Put results in the setup subsection | Mixes evidence production and interpretation | Move outcomes into an evidence block |
| Force a complex subsection into two paragraphs | Combines unrelated artifacts and claims | Repeat the two-block unit by evidence channel |
| Repeat all global parameters | Inflates every experiment contract | Cross-reference shared settings and state only changes |
| List every value | Replaces analysis with transcription | Select discriminating anchors and exceptions |
| Say `significant` colloquially | Implies an unreported statistical result | Use magnitude language or report the actual test |
| Attribute a trend directly to a mechanism | Alternative causes remain | Use model-consistent language or add an ablation |
| Call a smooth curve robust | Robustness was not tested | Reserve robustness for explicit perturbation evidence |
| End with generic superiority | Adds no scientific insight | State what the evidence supports under which conditions |
| Hide failed or infeasible cases | Distorts scope and reproducibility | Define and report failure semantics |

## Hard quality gates

Do not finalize the section unless all applicable gates pass:

- [ ] Every contribution-level empirical claim appears in the ledger.
- [ ] Every artifact has one primary experiment question and one primary claim.
- [ ] Each experiment contract states purpose before configuration and contains no result leakage.
- [ ] Each evidence block begins with the overall answer and ends with a bounded conclusion.
- [ ] Global setup, metric definitions, and baseline descriptions are not repeatedly reintroduced.
- [ ] Every number has been reconciled to its artifact, unit, aggregation, direction, baseline, and denominator.
- [ ] Relative percentages and percentage-point changes are labeled correctly.
- [ ] Statistical significance, stability, equivalence, and robustness are claimed only with matching evidence.
- [ ] Exceptions, infeasible cases, and scale-dependent changes are visible in prose.
- [ ] Causal verbs do not exceed the isolation provided by the experiment.
- [ ] Paragraph-opening center sentences form a complete evidence story.
- [ ] No paragraph performs two independent rhetorical jobs without a split.
- [ ] No caption, axis description, or conclusion is unnecessarily repeated.
- [ ] Missing evidence is disclosed rather than invented.
