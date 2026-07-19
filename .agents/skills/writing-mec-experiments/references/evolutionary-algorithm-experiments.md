# Evolutionary-Algorithm Experimental Sections

## Contents

1. [Scope and provenance](#scope-and-provenance)
2. [Source-derived structural pattern](#source-derived-structural-pattern)
3. [Recommended chapter organization](#recommended-chapter-organization)
4. [Evolutionary evidence ledger](#evolutionary-evidence-ledger)
5. [Setup and fair comparison](#setup-and-fair-comparison)
6. [Metrics, reference objects, and failures](#metrics-reference-objects-and-failures)
7. [Artifact-specific evidence units](#artifact-specific-evidence-units)
8. [Scenario and model validation](#scenario-and-model-validation)
9. [Trade-off and representative-solution analysis](#trade-off-and-representative-solution-analysis)
10. [Overall algorithm comparison](#overall-algorithm-comparison)
11. [Convergence analysis](#convergence-analysis)
12. [Ablation, sensitivity, scale, and runtime](#ablation-sensitivity-scale-and-runtime)
13. [Interpretation and wording](#interpretation-and-wording)
14. [Common invalid claims](#common-invalid-claims)
15. [Evolutionary-route audit](#evolutionary-route-audit)

## Scope and provenance

Use this route for population-based single- or multiobjective methods, constrained multiobjective evolutionary algorithms, dynamic evolutionary optimization, Pareto search, decomposition, repair, nondominated sorting, coevolution, and related metaheuristics.

The structural rules were calibrated against the experimental sections of:

- *Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing: A Joint Energy and Delay Optimization*;
- *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks: A Joint Optimization Approach for Reliability and Latency*;
- *Terrain-Aware UAV-Enabled Mobile Edge Computing in Urban Environments: A Constrained Multi-Objective Approach With Task-Adaptive Mechanism*;
- *Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing: A Multi-Objective Optimization Approach*;
- *HAP-UAV Coordination for Data Collection in Low-Altitude Economy Networks: A Feasibility-Driven Dynamic Constrained Multi-Objective Evolutionary Approach*.

These titles establish provenance, not required dependencies. Apply the derived evidence pattern to the target paper's actual problem and artifacts.

## Source-derived structural pattern

The references share a stable microstructure:

- a simple ablation, mobility, runtime, or scenario comparison uses one experiment-contract paragraph and one evidence-to-claim paragraph;
- a comprehensive comparison repeats the unit for an aggregate table, Pareto geometry, and convergence behavior;
- the result paragraph begins with the global answer, selects a few values, explains scale-dependent behavior, and ends with a scenario or mechanism insight;
- numerical performance and qualitative front behavior perform different evidentiary jobs and are not treated as interchangeable;
- component ablations connect observed changes to the operation removed from the full algorithm.

The strongest references introduce the full comparison before ablations, keep global settings separate, and quantify at least the closest baseline or the most informative scale. Some source papers place findings inside setup or overexplain standard metrics; treat those as local weaknesses rather than rules to copy.

## Recommended chapter organization

Use the following functional sequence, omitting unsupported functions and reordering only to follow the contribution logic:

1. **Experiment roadmap.** State which experiment group validates each contribution.
2. **System parameters and test instances.** Define scenario data, controlled scales, constraints, and instance construction.
3. **Baselines and fair budgets.** Define the closest algorithms and common evaluation resources.
4. **Metrics and statistics.** Define performance direction, repeated runs, uncertainty, significance, and failure treatment.
5. **Scenario or model validation.** Establish that the modeled feature produces the behavior motivating the algorithm.
6. **Trade-off interpretation.** Examine representative nondominated solutions or objective conflicts.
7. **Overall performance.** Compare aggregate quality and feasibility across instances.
8. **Pareto and convergence behavior.** Explain distribution, diversity, progress, and scale effects.
9. **Component ablation.** Isolate each proposed mechanism.
10. **Sensitivity, scalability, runtime, or robustness.** Test operational boundaries supported by the contribution claims.

Do not create a subsection merely because the reference papers use one. Every subsection needs one distinct question in the claim-to-experiment ledger.

## Evolutionary evidence ledger

Extend the shared ledger with:

| Field | Required meaning |
|---|---|
| Evaluation budget | Total objective/constraint evaluations or another justified common cost |
| Population and iterations | Population size, generations, and the relation to total evaluations |
| Independent runs | Number of separately initialized executions used as statistical units |
| Solution count | Number of feasible or nondominated solutions within one run; never substitute for runs |
| Reference object | IGD reference set/front and HV reference point or normalization |
| Representative-run rule | Median HV/IGD, closest-to-median, fixed seed, or another predeclared rule |
| Feasibility failure | Meaning of missing, zero, NaN, empty front, timeout, or no feasible set |
| Significance | Test, correction if applicable, direction, and comparison family |

Record these fields before drafting overall-comparison claims.

## Setup and fair comparison

### Common budget

Use an equal function-evaluation budget when objective and constraint evaluation dominate cost. State the population and generation combination that produces that budget. If algorithms perform unequal auxiliary optimization, model calls, or local-search steps, report wall-clock or operation cost in addition to evaluations.

Do not claim fairness merely because all methods use the same generation count. A larger population, extra repair search, or expensive subproblem may change the actual budget.

### Baseline selection

Include, when available:

- the closest state-of-the-art method for the same problem class;
- the adopted base algorithm without the proposed modifications;
- variants that remove each claimed component;
- a domain baseline such as static deployment, random policy, or conventional resource allocation when it tests the scenario claim;
- an exact or classical solver on small instances when optimality-gap evidence is claimed.

Explain why each baseline is diagnostically useful. Do not provide paper-by-paper literature summaries in the experiment section.

### Independent runs and common randomness

State the number of independent runs and initialization policy. When stochastic scenario realizations affect all methods, use shared instances or common random numbers where appropriate and disclose whether comparisons are paired.

Do not write `1000 solutions were generated` as evidence of 1000 independent trials. Solutions inside one population are correlated and are not independent statistical units.

### Algorithm parameters

Report parameters required for reproduction and comparison, but keep long standard defaults in a table or supplement. Explain tuning procedures that could affect fairness. If parameters are tuned per method, state the tuning budget and validation instances.

## Metrics, reference objects, and failures

### Inverted generational distance

IGD evaluates how well the obtained nondominated set approximates a reference set in convergence and coverage. Lower is better. State:

- how objective values are normalized;
- how the reference set is constructed;
- whether results from all methods/runs contribute to it;
- how infeasible or empty sets are scored;
- whether the same reference set is used across methods on an instance.

Do not compare IGD values across differently normalized instances as though their absolute magnitudes had the same meaning.

### Hypervolume

HV evaluates dominated objective-space volume relative to a reference point. Higher is better. State:

- objective orientation and normalization;
- the reference point and why it is dominated by relevant solutions;
- whether infeasible solutions are excluded;
- how an empty feasible set is represented;
- whether the reference point remains fixed within a comparison.

Do not interpret HV without checking that the reference point and normalization make the compared values commensurate.

### Feasibility measures

For constrained problems, report a feasibility indicator such as feasible-run rate, success rate, constraint violation, or number of feasible nondominated solutions when it bears on the contribution. Define the denominator and whether feasibility is assessed per solution, run, or instance.

### Failure semantics

Define every special value:

- `0` may mean no dominated volume, not numerical equality;
- `NaN` may mean an undefined metric because no feasible set exists;
- a blank entry may mean failure, timeout, or unreported output;
- a truncated curve may indicate early failure rather than faster convergence.

Never silently remove failed runs from means. State the inclusion rule and report feasibility separately when a metric is undefined.

## Artifact-specific evidence units

### Aggregate statistical table

**Contract:** state the algorithms, instances/scales, common budget, number of independent runs, metric direction, aggregation, significance convention, and table pointer.

**Evidence:** begin with the overall pattern across instances; compare the closest baseline; quantify one or two informative cases; report variability or failure; explain scale-dependent changes; end with the aggregate conclusion supported by the table.

The table establishes repeated-run performance. It does not by itself show the shape of one Pareto front or why a method converges faster.

### Pareto-front plot

**Contract:** state the selected instances, run-selection rule, normalization, feasibility filtering, and figure pointer.

**Evidence:** discuss convergence toward the reference region, coverage, diversity, disconnected regions, extreme solutions, and failure to reach feasible areas. Compare geometry visible in the plot without converting one selected run into a statistical claim.

Use `the representative run illustrates` rather than `the algorithm always produces`.

### Convergence curve

**Contract:** state the monitored metric, evaluation axis, aggregation across runs, interval or dispersion, smoothing if any, and figure pointer.

**Evidence:** distinguish early search, transition, and final behavior when relevant; quantify convergence speed only with a defined threshold or budget; report whether curves plateau, cross, or diverge with scale; connect the pattern to a mechanism only when supported.

Do not infer final solution diversity from HV alone or stability from a smooth averaged curve.

### Representative trade-off solutions

**Contract:** state how compromise, objective-extreme, or preference-based solutions are selected from the nondominated set and which run supplies them.

**Evidence:** compare objective changes, operational decisions, and the physical cause of the trade-off. Show what is gained and sacrificed. End with the decision insight, not a claim that one point is universally best.

### Ablation table or plot

**Contract:** name the full method and variants, define exactly what each variant removes or freezes, keep all other components and budgets fixed, and state the artifact.

**Evidence:** first establish whether the full method improves the relevant metric; then identify the scale or condition where the component matters most; explain the operation lost in the ablation; delimit interactions when effects are not additive.

Do not attribute a difference to one component if the variant also changes representation, initialization, or budget.

## Scenario and model validation

Use a scenario experiment when the paper's algorithmic motivation depends on a modeled physical or operational feature, such as heterogeneous regional demand, terrain blockage, mobility, multi-source fusion, charging cost, or HAP-UAV coordination.

Write the contract around a controlled question:

- vary the motivating feature;
- hold unrelated system resources and algorithm settings fixed;
- compare feasible strategies or architectures;
- report a physical metric and the resulting objective effect.

In the evidence block, give the overall change, then trace a causal chain through the system model. For example:

`demand distribution -> deployment or service allocation -> flight/hover/communication cost -> objective outcome`.

Do not claim the optimization algorithm caused a physical effect when the experiment actually compares scenarios or decision strategies.

## Trade-off and representative-solution analysis

Multiobjective papers must show more than aggregate indicators when the contribution includes decision trade-offs. Select solutions through a reproducible rule, such as objective extremes and a compromise solution from the median-HV run.

Analyze:

- how much one objective changes when improving another;
- which physical decisions create the trade-off;
- whether the trade-off changes across scales or scenario regimes;
- whether a knee or compromise point has operational meaning;
- whether constraints truncate part of the front.

Avoid calling a compromise solution optimal without a declared preference model.

## Overall algorithm comparison

Use an overall-comparison subsection to answer a single broad question: does the complete method produce better feasible multiobjective approximations under the common protocol?

A strong subsection normally uses multiple evidence units:

1. an aggregate table for repeated-run IGD/HV/feasibility;
2. representative Pareto fronts for objective-space geometry;
3. convergence curves for budget-dependent behavior.

Do not compress all three into one contract and one dense result paragraph. Introduce the statistical protocol once, then give each additional artifact a short evidentiary purpose and interpretation.

When reporting wins across many cases, define how ties, failures, and significance are counted. A best mean is not automatically a statistically supported win.

## Convergence analysis

Separate three possible claims:

- **speed:** the method reaches a declared quality threshold with fewer evaluations;
- **final quality:** the method ends with a better metric at the common budget;
- **search behavior:** the curve shows phases consistent with exploration, repair, transfer, or adaptation.

One curve can support more than one claim only when the protocol and evidence do. Report crossings and cases where a baseline leads early but loses later.

For dynamic problems, state whether the horizontal axis resets after a change, whether populations retain state, and how quickly quality or feasibility recovers. Recovery after a known change is not robustness to arbitrary uncertainty.

## Ablation, sensitivity, scale, and runtime

### Component ablation

Test each contribution-bearing mechanism against the full method. If two mechanisms interact, include a factorial or combined variant when feasible and avoid adding individual improvements as though they were independent.

### Parameter sensitivity

Vary one parameter over a justified range while holding other factors fixed. Report both the favorable region and degradation boundary. A flat response within the tested range supports low sensitivity there; it does not prove universal insensitivity.

### Scalability

Increase decision dimension, users, UAVs, areas, tasks, or time horizon. Report solution quality, feasibility, evaluation budget, and runtime. If the budget is held fixed as dimension grows, state that the experiment tests performance under a fixed computational allowance rather than equal convergence.

### Runtime and complexity

Report hardware/software, implementation conditions, wall-clock aggregation, and whether parallelism differs. Separate evaluation cost from algorithm overhead when the proposed mechanisms add repair, prediction, matching, or subproblem solves.

Do not use asymptotic complexity alone as experimental runtime evidence.

### Robustness

Reserve robustness for explicit uncertainty or perturbation tests, such as channel/model errors, corrupted demand, delayed information, or stochastic failures. Ordinary parameter sweeps establish sensitivity, not robustness.

## Interpretation and wording

Use evolutionary-specific language precisely:

- `approximates the Pareto front`, not `finds the true Pareto front`, unless the latter is known;
- `obtained nondominated set`, not `optimal solutions`, without proof;
- `higher feasible-run rate`, not `guarantees feasibility`;
- `better mean HV under the tested budget`, not `converges better in general`;
- `the median-HV run illustrates`, not `all runs show`;
- `the repair variant contributes to feasibility`, not `repair causes every gain`, when other interactions remain.

Mechanism explanations should follow the algorithm's operations. Examples include:

- repair reduces invalid dependency combinations, increasing feasible-run rate;
- demand-aware reconstruction allocates search effort toward high-impact regions;
- cooperative populations preserve diverse feasible regions;
- task-adaptive operators change exploration/exploitation as constraints or environments shift.

Use these explanations only when the manuscript defines the operation and the experiment isolates or supports it.

## Common invalid claims

| Tempting claim | Why invalid | Required correction or evidence |
|---|---|---|
| `Thirty solutions prove statistical reliability` | Solutions within a run are correlated | Report independent runs |
| `The lowest mean proves stability` | Mean does not measure dispersion | Report variance/interval and run protocol |
| `The front plot proves overall superiority` | It is one selected run | Pair with repeated-run metrics |
| `Same generations means fair comparison` | Population and auxiliary costs may differ | Equalize evaluations and disclose overhead |
| `HV is zero, so objectives are zero` | Zero may encode no dominated volume | Define failure semantics |
| `The method finds the optimal Pareto front` | Reference or approximation is empirical | Use approximation language or provide proof |
| `Sensitivity analysis proves robustness` | No uncertainty or perturbation was tested | Narrow the claim or add robustness tests |
| `Every module adds its individual gain` | Mechanisms may interact | Use combined ablations or bounded wording |

## Evolutionary-route audit

- [ ] The section roadmap maps scenario, algorithm, ablation, and scale experiments to contribution claims.
- [ ] Test instances and controlled scales are reproducible.
- [ ] Baselines include the adopted base method and closest relevant competitors.
- [ ] The function-evaluation budget and auxiliary computational costs are disclosed.
- [ ] Population, generations, termination, and independent runs are not conflated.
- [ ] IGD reference sets and HV reference points are defined when those metrics are used.
- [ ] Feasible, empty, zero, NaN, missing, and timeout outcomes have explicit semantics.
- [ ] Means are paired with suitable dispersion or uncertainty.
- [ ] Significance statements name their statistical procedure.
- [ ] Representative fronts use a predeclared run-selection rule.
- [ ] Aggregate tables, Pareto fronts, and convergence curves have distinct evidentiary roles.
- [ ] Trade-off solutions use a reproducible selection rule and are not called universally optimal.
- [ ] Ablations change one mechanism or disclose coupled changes.
- [ ] Parameter sensitivity, scalability, runtime, and robustness use distinct claim language.
- [ ] Every result unit ends with a conclusion bounded by instances, scales, and budget.
