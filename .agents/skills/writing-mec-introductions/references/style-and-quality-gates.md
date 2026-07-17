# MEC Introduction style, evidence, and quality gates

Apply this document whenever `writing-mec-introductions` drafts, revises, or audits an Introduction.

## Contents

1. [Paragraph centers and hierarchy](#paragraph-centers-and-hierarchy)
2. [Paragraph functions and length](#paragraph-functions-and-length)
3. [MECE classification](#mece-classification)
4. [Citation accuracy, placement, and deduplication](#citation-accuracy-placement-and-deduplication)
5. [Scenario motivation and description](#scenario-motivation-and-description)
6. [Algorithm motivation and module mapping](#algorithm-motivation-and-module-mapping)
7. [Language and expression](#language-and-expression)
8. [Contributions](#contributions)
9. [Hard failures and scoring](#hard-failures-and-scoring)

## Paragraph centers and hierarchy

### Primary center sentence

The first sentence states the paragraph's main conclusion or advance. It should answer one question: why the topic matters, what the concrete problem is, how research is classified, which boundary remains, what the paper's scenario is, why it is hard to solve, or how the paper responds.

Avoid empty centers:

- Weak: `Recently, UAV-MEC has attracted extensive attention.`
- Strong: `UAV-MEC can restore computing service when terrestrial infrastructure is unavailable, but limited endurance makes long missions depend on multi-UAV rotation.`

### Subordinate center sentences

A paragraph may use one or two subordinate centers for parallel branches or causal substeps. They must satisfy all conditions:

1. without the primary center, they do not form an unrelated paragraph topic;
2. every supporting sentence points back to the primary center;
3. subordinate centers are coequal or causally ordered;
4. none introduces a separate literature set, scenario, or method.

### Recommended microstructure

```text
Primary center: the paragraph's advance.
Support 1: why it holds or why the problem arises.
Support 2: necessary fact, category, or operational consequence.
Subordinate center (optional): one directly related branch.
Support 3: why that branch matters to the primary conclusion.
Transition (optional): pass the result to the next paragraph.
```

Copy all paragraph-opening sentences into one block. Repair their logic and order before polishing transitions.

## Paragraph functions and length

Sentence count is a soft constraint; number of rhetorical jobs is a hard constraint.

| Paragraph function | Must answer | Normally excludes | Typical sentences |
|---|---|---|---:|
| Background and position | What matters and why | Method details, long application lists | 3–5 |
| Hotspot and difficulty | What is currently difficult and where this paper focuses | Every possible challenge | 3–5 |
| Research classification | Criterion, categories, and relevant capability | Author lists, internal algorithms | 4–7 |
| Synthesis and scenario motivation | Shared boundary and why it requires this scenario | A second literature review | 3–5 |
| Scenario description | Actors, trigger, sequence, completion boundary | Formulas, symbols, every protocol branch | 4–6 |
| Problem form | Joint decisions, objective conflict, hard constraints | Full mathematical formulation | 3–6 |
| Algorithm motivation and method | Structural difficulty, general-solver boundary, module mapping | Pseudocode, training hyperparameters | 4–7 |
| Contribution item | New object/action and bounded effect | Background restatement, inflated result | 1–2 |

Split or compress when:

- one paragraph needs two unrelated function labels;
- two separate uses of `however`, `moreover`, or `on the other hand` introduce new problems;
- a classification paragraph begins describing the complete proposed scenario;
- a scenario paragraph defines several terms and explains the algorithm;
- an algorithm paragraph surveys multiple solver families before detailing the method;
- the paragraph cannot be summarized by one contribution to the next paragraph.

Do not force equal paragraph lengths. Classification and algorithm-motivation paragraphs may be longer while retaining one controlling center.

## MECE classification

### Select the classification axis

Choose a criterion that directly determines the capability or boundary motivating the paper, for example:

- UAV deployment strategy;
- entity hosting a fusion or computing platform;
- launch and recovery infrastructure;
- method used to infer channel state;
- state-transfer timing relative to service takeover;
- decision timescale.

Do not mix levels:

- Wrong: `fixed-cloud methods, UAV methods, and recent methods`—platform and chronology overlap.
- Wrong: `migration mechanisms, scheduling algorithms, and experimental systems`—process, solver, and validation form are different levels.
- Correct: `According to when state is transferred relative to takeover, migration can be grouped into stop-and-copy, pre-copy, and post-copy.`

### MECE checks

1. **Mutually exclusive:** Does each work have one primary category under the stated criterion?
2. **Collectively exhaustive:** Do the categories cover the literature needed for this argument, without claiming to cover the whole field?
3. **Coequal:** Do category names answer the same question at the same level?
4. **Useful:** Would deleting a category break the scenario motivation?
5. **Synthesizable:** Can the categories lead to one shared boundary rather than unrelated paper-level criticism?

For a binary axis such as `whether X is present`, the categories must be strict complementary values. Do not replace one side with a narrower application subtype. For example, `battery-triggered UAV handover` is only one instance of `handover with a hard departure deadline`; it is not the logical complement of `handover without a hard deadline`.

### Maximum category resolution

In the Introduction, each category normally needs only:

```text
category definition or shared mechanism
+ one capability or limitation directly relevant to this paper
+ citation
```

Do not continue with authors, algorithm names, optimized variables, and experimental results.

## Citation accuracy, placement, and deduplication

### Accuracy before quantity

For every cited proposition, record:

| Claim | Source | Exact supporting passage/section | Direct or indirect evidence | Scope match | Citation used elsewhere? |
|---|---|---|---|---|---|

Require all of the following:

1. The source text directly supports the proposition at the same scope.
2. A method paper is not used as generic evidence merely because its Introduction mentions the topic.
3. A review may establish a field-level taxonomy; a primary paper should establish its own mechanism or result.
4. A citation cluster contains only sources supporting the same grammatical claim.
5. Negative comparisons are limited to what the source actually assumes or models.
6. Publication status, year, venue, and citation key match the bibliography.

Title relevance, a search snippet, or another paper's description is not sufficient evidence.

### Allowed citation functions in an Introduction

- establish field importance, a representative application, or a recognized problem;
- establish a taxonomy and category-level characteristic;
- support one shared assumption or boundary of an existing paradigm;
- support the capability or known limitation of a general solver family;
- when indispensable, identify one closest paper's decisive assumption in one sentence.

### Content that belongs in Related Work

- `Author et al. proposed/designed/jointly optimized/demonstrated ...`;
- a paper's algorithm name, full network entity set, decision vector, or loss;
- fixed workload values, known handover time, hardware details, or experiment numbers;
- sequential explanations of two or more papers;
- complete mechanism workflows, multiple advantages/disadvantages, or failure cases;
- paper-level novelty comparisons.

### Citation placement

Place a citation immediately after the smallest complete proposition it supports. Avoid end-of-paragraph citation piles that appear to support several different claims.

For a taxonomy, choose one of these patterns:

- cite the umbrella taxonomy sentence once, then describe categories without repeating those same sources; or
- cite each category sentence with its specific evidence and omit a redundant umbrella cluster.

Do not use both patterns with the same references.

### One-source-one-primary-role rule

Assign every source one primary Introduction claim. The default is one appearance per reference number across the entire Introduction.

Hard rules:

- Never cite the same reference more than once in one paragraph.
- Do not repeat a source in successive paragraphs to support adjacent steps of one argument.
- Do not repeat an identical citation cluster in background, classification, and gap paragraphs.
- Do not cite a closest paper once as a scenario example and again for the same limiting assumption.
- Do not swap in a weaker or only tangentially relevant paper merely to achieve unique numbering.

If one source is uniquely authoritative for two materially independent claims, an exception may be defensible. Record the two exact claims and why no equally accurate source can support either one. The default publishable draft still aims for zero repeated references.

### Mechanical duplicate audit

For Markdown with IEEE-style numeric citations, run from the skill directory or pass the full script path:

```powershell
python -X utf8 scripts/audit_intro_citations.py <manuscript.md>
```

The script:

- finds the `Introduction` or `I. Introduction`/equivalent heading;
- stops at the next heading of equal or higher level;
- expands ranges such as `[1]–[3]`;
- reports total occurrences, unique references, excess occurrences, lines, and paragraph IDs;
- exits `1` when any source repeats.

Interpret every duplicate:

1. **Same paragraph, same claim family:** consolidate; this is redundant.
2. **Adjacent paragraphs, continuous argument:** assign the source to the narrowest claim and remove the other use.
3. **Different sections of the argument but same evidence fact:** merge or move the paper-level comparison to Related Work.
4. **Materially independent facts with unique authority:** document the exception explicitly; do not silently pass it.

The script proves only non-repetition. It does not prove that citations are accurate, sufficient, or primary.

### Quick granularity test

Move a sentence toward Related Work when:

- two or more author names appear in one paragraph;
- `for example` introduces papers more than once;
- the main information is which variables one paper optimized;
- explaining a limitation requires the paper's internal workflow;
- the citation is being used to prove novelty against one paper rather than motivate the scenario.

Citation count alone does not determine granularity. A concise background sentence can carry a small accurate cluster, while a two-citation algorithm narrative may still be Related Work.

### Compression example

Too detailed for the Introduction:

> One study jointly optimized migration order, UAV position, and task offloading while fixing migration data to VM memory; another scheduled low-energy UAV state handover using a known handover duration.

Introduction resolution:

> Existing UAV service-migration models generally treat state volume or handover duration as given, and therefore do not represent the joint evolution of runtime state growth and departure resources.

Support the second sentence with one minimal, accurately scoped citation cluster and reserve paper-level comparison for Related Work.

## Scenario motivation and description

### Derive the scenario from the literature boundary

Do not introduce a scenario merely because it is `more complex` or `more realistic`. Use three causal steps:

1. state the condition under which an existing paradigm works;
2. identify the state, resource, timing, or feasibility relation changed by the target environment;
3. explain why that change requires the proposed operating scenario or joint decision.

Functional pattern:

```text
Existing methods optimize X under condition A.
When B changes with task execution, platform motion, or the previous decision, X and Y can no longer be determined independently.
Therefore, this paper considers scenario C, in which B evolves jointly with decisions X and Y.
```

### Minimum complete scenario information

Include only:

- **Actors:** relevant platforms, users, servers, services, or tasks;
- **Trigger:** event initiating a cycle, migration, rotation, or replanning;
- **Main sequence:** necessary operations in time order;
- **Completion boundary:** success, failure, departure, or next-cycle condition;
- **Decisions:** what the controller chooses and at which timescale.

Move state symbols, set definitions, channel formulas, every protocol branch, repair operations, and pseudocode to later sections. If a detail does not help explain why the decisions are necessary, omit it from the scenario paragraph.

### State concrete MEC difficulties

Describe how a relationship changes instead of saying the scenario is complex:

- mobility changes channel and association feasibility;
- arrivals change queues, computation load, and state generation;
- UAV movement changes coverage, links, energy, and remaining service time;
- shared bandwidth or CPU couples tasks and handovers;
- a current action consumes the only UAV, energy, time, or feasible path needed later;
- a previous decision updates the state and reshapes the next feasible region.

## Algorithm motivation and module mapping

### Correct order

```text
scenario structure
-> exact consequence for optimization
-> why the general solver family is suitable
-> why its standard mechanism is limited here
-> proposed module
-> capability restored by that module
```

### Difficulty-module matrix

Build this matrix before drafting the algorithm paragraph:

| Scenario difficulty | Effect on a general method | Paper module | Verifiable role |
|---|---|---|---|
| Cascaded variable dependency | Independent variation propagates violations | Dependency-ordered generation | Reduces infeasibility caused by predecessor decisions |
| Future replacement conflict | Immediate masks check only the current selection | Residual matching check | Preserves conflict-free assignments for later events |
| Decision-shaped dynamic feasible region | Historical candidates may be infeasible now | Current-state repair/generation | Produces candidates satisfying current constraints |

Every highlighted module must map to one row. Do not claim that a difficulty is solved when no corresponding module exists.

The Introduction states only first-order modules. Give each module at most one sentence explaining what it checks, generates, or corrects and which capability it restores. Put subchecks, certificate construction, predictive bounds, risk allocation, update equations, and execution order in the method section.

### Invalid algorithm motivations

- `Recently, DRL/evolutionary algorithms have been widely used ...`
- `Because the problem is NP-hard, an intelligent algorithm is adopted.`
- `Traditional methods cannot handle this complex environment.`
- introducing an acronym first and reverse-engineering the motivation;
- calling PPO, a Transformer, attention, or multi-agent control itself the scenario innovation.

Claims involving NP-hardness, convergence, optimality, guaranteed safety, or reduced complexity require model, proof, or experimental evidence.

## Language and expression

### Prefer concrete causal language

| Prefer | Avoid or qualify | Reason |
|---|---|---|
| `Existing methods assume ...` | `A research gap remains` | States a verifiable boundary |
| `When B changes, X changes Y` | `In a complex dynamic scenario` | Explains why the difficulty arises |
| `This makes the current action affect future feasibility` | `This creates a huge challenge` | Names the changed relation |
| `This paper studies/considers ...` | `This paper is the first to ...` | Avoids unsupported novelty |
| `According to criterion Z, studies fall into A and B` | `Studies approach the topic from many angles` | Declares the classification axis |
| `The controller must jointly determine ...` | `An efficient solution is urgently needed` | Derives the actual decision need |
| `The module checks/corrects/generates ...` | `The module significantly improves ...` | Avoids pre-claiming results |

Do not place internal writing vocabulary such as `storyline`, `narrative tension`, `coordinate system`, `fill the gap`, or `close the loop` in the manuscript prose. State the problem, cause, boundary, and advance directly.

Control sentence burden:

- express one core causal relation per sentence;
- keep one term for one concept;
- expand an abbreviation only at first use;
- avoid long stacked modifiers;
- do not use transition words to insert unrelated topics;
- use `therefore` only for a real causal consequence.

### Functional English sentence patterns

- Background: `X has emerged as ... because ...`
- Narrowing: `However, X remains constrained by ...`
- Classification: `Existing studies can be categorized according to ...`
- Synthesis: `Across these approaches, ...`
- Scenario: `To address this limitation, this study considers ...`
- Problem: `In this scenario, the controller jointly determines ...`
- Algorithm motivation: `Solving the formulated problem poses ...`
- Method: `To address this challenge, we propose ...`

Use these as functional prompts, not fill-in-the-blank prose. Avoid:

- `Recently, many researchers have paid increasing attention to ...`
- `It is worth noting that ...`
- `As is well known ...`
- opening every paragraph with `However`;
- repeated `significantly`, `novel`, `efficient`, or `superior` without evidence;
- nominalization that hides the acting subject.

### Transitions

Prefer reusing the prior paragraph's concluding entity or relation:

```text
Prior conclusion: Both deployment families predetermine the UAV count per area.
Next opening: Allowing UAV counts to follow regional demand requires the controller to determine fleet allocation, positions, and resources jointly.
```

This is clearer than `Based on the above analysis` unless only one immediately preceding problem exists.

## Contributions

Use this order when applicable:

1. **Scenario/model:** new operating scenario, architecture, or state process;
2. **Problem:** joint decisions and newly modeled coupling, objective, or constraint;
3. **Algorithm:** module and corresponding structural difficulty;
4. **Evidence:** only conclusions supported by completed experiments, analysis, or proof.

Write each item as `action + object + bounded distinction/role + evidence scope`.

Avoid:

- treating `first` as a contribution;
- treating use of a standard algorithm as a contribution;
- packing model, algorithm, and experiments into one item;
- claiming superiority in a research idea without results;
- contributions that do not correspond to the preceding problem.

## Hard failures and scoring

### Hard failures

Revise rather than deliver if any item occurs:

1. Opening sentences do not form a complete causal chain.
2. Classification mixes criteria, overlaps, or uses inconsistent levels.
3. A binary taxonomy does not use complementary values.
4. The Introduction describes two or more papers sequentially.
5. The scenario does not follow from the synthesized boundary.
6. The algorithm appears only because it is popular, general, or the problem is `complex`.
7. A highlighted module has no previously stated structural difficulty.
8. The Introduction includes internal subchecks, equations, pseudocode, training settings, or experiment details.
9. `First`, `optimal`, `guaranteed`, or `significantly better` lacks evidence.
10. A citation cannot be traced to direct supporting text at the claimed scope.
11. One citation cluster contains papers supporting different claims.
12. A reference number repeats in the Introduction without an explicit, defensible independent-role exception.
13. The same reference appears twice in one paragraph.
14. A duplicate is hidden by replacing it with a weaker or inaccurate source.

### Scoring table

Score each item from 0 to 2: 0 missing/incorrect, 1 present but vague, 2 clear and evidenced. Require at least 24/28 and no hard failure.

| Item | Two-point standard |
|---|---|
| Importance | Background, concrete problem, and field position form a causal argument |
| Focus | Hotspot and difficulty narrow to the paper's actual object |
| Classification | One criterion, MECE categories, motivation relevance |
| Status synthesis | Existing capability and shared limiting condition are explicit |
| Scenario motivation | The scenario follows naturally from that condition |
| Scenario completeness | Actors, trigger, sequence, boundary, and decisions are sufficient |
| Problem form | Decision coupling, objective conflict, and hard constraints are clear without full modeling |
| Algorithm motivation | Exact failure of a general method under the scenario structure |
| Module mapping | Every core module maps to one prior difficulty |
| Paragraph organization | One primary advance with clear subordinate centers |
| Citation accuracy | Every source directly supports the exact local claim |
| Citation economy | Minimal clusters; one primary role per source; zero unjustified repeats |
| Introduction/RW boundary | Category-level evidence stays here; paper-level evidence moves to Related Work |
| Expression | Concrete actors and causal relations replace vague or inflated prose |

### Final reverse audit

Trace backward from the algorithm paragraph:

1. Does each module address a difficulty stated immediately before it?
2. Does that difficulty arise from the scenario workflow?
3. Does the scenario arise from a shared boundary of existing research?
4. Is that boundary supported by a coherent classification or difficulty set?
5. Does each cited source have one verified role in that chain?
6. Can any repeated citation be removed by assigning it to the narrowest supported claim?

The Introduction is closed only when every answer points to the preceding layer and the citation audit is clean.
