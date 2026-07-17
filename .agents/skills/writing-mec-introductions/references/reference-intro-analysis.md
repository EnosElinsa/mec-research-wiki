# Reference-derived analysis of MEC Introductions

This file records the structural evidence behind `writing-mec-introductions`. Use it to calibrate MEC-family Introductions, not to transplant facts or contributions from a benchmark paper into another manuscript. When the user supplies a current source, verify all factual and citation claims against that source.

## Contents

1. [Evidence base](#evidence-base)
2. [Shared narrative architecture](#shared-narrative-architecture)
3. [Citation-use evidence](#citation-use-evidence)
4. [Source-by-source anatomy](#source-by-source-anatomy)
5. [Introduction versus Related Work](#introduction-versus-related-work)
6. [Typical failures in migration and rotation papers](#typical-failures-in-migration-and-rotation-papers)
7. [Transferable conclusions](#transferable-conclusions)

## Evidence base

Identify the benchmark set by stable titles and identifiers, not machine-specific paths:

| Short name | Stable source identity | Sections analyzed |
|---|---|---|
| Demand-aware multi-UAV MEC | *Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing: A Joint Energy and Delay Optimization* | Introduction; Related Work |
| UAV multi-source fusion | *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks: A Joint Optimization Approach for Reliability and Latency*; DOI `10.1109/TWC.2026.3676831` | Introduction; Related Work |
| Terrain-aware UAV-MEC | *Terrain-Aware UAV-Enabled Mobile Edge Computing in Urban Environments: A Constrained Multi-Objective Approach With Task-Adaptive Mechanism*; DOI `10.1109/TVT.2025.3604250` | Introduction; Related Work |
| Dispersed computing | *Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing: A Multi-objective Optimization Approach*; DOI `10.1109/TMC.2026.3679393` | Introduction; Related Work |
| HAP-UAV planning | Author-supplied HAP-UAV periodic data-collection planning benchmark | Introduction; Related Work |

The final item is a non-public writing benchmark. This bundled analysis contains the reusable observations and does not require runtime access to that draft.

MinerU extraction introduces layout noise in some raw sources, including repeated fragments and page furniture. Recover logical paragraphs before analyzing structure. Transfer only patterns that recur across the set; do not copy extraction errors, awkward grammar, or accidental paragraph length.

## Shared narrative architecture

The benchmark papers vary in paragraph count and merging, but follow the same functional chain:

1. **Establish importance.** Introduce the application, concrete problem, and field position before discussing the method.
2. **Narrow the focus.** Move from the broad problem to the current hotspot and decisive difficulty.
3. **Map the research landscape.** Choose one motivation-relevant classification criterion or a small set of coequal difficulties.
4. **Derive the scenario.** Synthesize a category-level boundary and explain why it requires the operating mode studied in the paper.
5. **Turn the scenario into a problem.** Describe the workflow, decisions, objectives, conflicts, and major constraints.
6. **Derive the algorithm.** Identify the exact failure mode of a general solver under the scenario structure, then introduce the targeted mechanism.
7. **Close with contributions.** Map contributions to scenario, model, problem, algorithm, and actual evidence.

This is a functional order, not a seven-paragraph template. The dispersed-computing paper completes the chain in four body paragraphs; the fusion and HAP-UAV papers use roughly seven; the terrain-aware paper develops two coequal hotspots before merging them. Stability comes from causal order and paragraph responsibility.

| Paper | Research-status organization | Scenario motivation | Algorithm motivation |
|---|---|---|---|
| Demand-aware | Sequential versus fixed UAV deployment | Both fix the number of UAVs per area and cannot adapt to heterogeneous demand | Mixed decisions and interacting constraints make feasible solutions hard to locate |
| Multi-source fusion | V2V, V2I, and hybrid fusion hosts | Ground platforms face obstruction, fixed coverage, or deployment limitations | Request response, collection, and bandwidth decisions have cascaded dependencies |
| Terrain-aware | Channel-inference families plus a coequal flight-safety line | Existing channel models omit complex terrain while safe trajectories often fix the destination | Search behavior depends on task-appropriate operators |
| Dispersed computing | Parallel/serial processing, redundancy, and multi-objective tradeoffs | Heterogeneous volunteer devices require delay, price, and reliability to be considered together | Feasibility, convergence, and diversity must be handled jointly |
| HAP-UAV | Fixed-ground, mobile-ground, and aerial-mothership infrastructure | Preplanned mothership operations cannot adapt spatial resources to evolving mission state | Historical states cannot determine a feasible region shaped by the previous decision |

## Citation-use evidence

A mechanical audit expanded IEEE-style citation ranges and counted each numbered source within the benchmark Introductions:

| Introduction | Expanded occurrences | Unique sources | Excess occurrences | Repeated sources |
|---|---:|---:|---:|---:|
| Demand-aware multi-UAV MEC | 9 | 9 | 0 | 0 |
| UAV multi-source fusion | 23 | 22 | 1 | 1 |
| Terrain-aware UAV-MEC | 29 | 24 | 5 | 5 |
| Dispersed computing | 10 | 10 | 0 | 0 |
| HAP-UAV planning | 17 | 17 | 0 | 0 |

Three of the five benchmarks use every source once. The fusion paper reuses one source for two distinct claims. The terrain-aware paper first cites a five-paper cluster to establish a taxonomy and then repeats members of that cluster while describing individual categories; this is logically defensible but unnecessarily dense. It should not be copied as a citation habit.

The transferable standard is therefore stricter than occasional benchmark artifacts:

- assign one primary Introduction role to each source;
- cite the category sentence or the supporting category description, not both;
- never repeat a source several times within one paragraph;
- reuse a source across paragraphs only for materially independent facts when it is uniquely authoritative;
- prefer restructuring a claim over swapping in a weaker citation solely to eliminate a duplicate.

The bundled audit script detects numerical reuse. It cannot establish whether a source supports the claim; that requires the citation-role ledger and source reading.

## Source-by-source anatomy

### 1. Demand-aware multi-area multi-UAV MEC

**Center-sentence chain**

1. MEC addresses wireless computation and latency needs, but terrestrial deployment is costly and immobile.
2. UAV-MEC relaxes those limitations; a single UAV remains limited by coverage, computation, and energy, motivating multiple UAVs.
3. Multi-area service is classified into sequential and fixed deployment, both of which predetermine UAV counts per area.
4. Demand-aware allocation addresses this boundary but couples fleet size, positions, association, and resources.
5. Energy and delay conflict under these decisions and constraints, producing a CMOP.
6. Evolutionary optimization fits multi-objective search, but the mixed space and interacting constraints motivate constraint-guided reconstruction.

**Writing characteristics**

- Each paragraph opening reuses the prior paragraph's conclusion: `MEC -> UAV -> multi-UAV landscape -> demand-aware scenario -> CMOP -> CMOEA`.
- The classification uses only deployment strategy, and both categories converge on one shared boundary.
- The Introduction cites field-level claims without explaining author-level algorithms or variable sets.
- Scenario coupling appears before the paper announces its particular optimization problem.
- The algorithm paragraph first establishes why feasible search is difficult, then states what reconstruction does.
- All nine cited sources receive one Introduction role.

### 2. UAV-enabled multi-source fusion

**Center-sentence chain**

1. Cooperative perception matters to vehicular safety, and multi-source observations expand perceptual coverage.
2. Accuracy, completeness, heterogeneity, and conflict make a fusion platform necessary.
3. Platforms are classified by host as V2V, V2I, or hybrid.
4. Their obstruction, fixed-coverage, and deployment boundaries motivate an aerial fusion platform.
5. The UAV moves, responds, collects, fuses, and returns results in a cycle with five coupled decisions.
6. Reliability and waiting time conflict under flight, assignment, resource, and deadline constraints, producing a DCMOP.
7. Generic DCMOEA operators can break cascaded dependencies, motivating dependency-ordered variable generation.

**Writing characteristics**

- The first four paragraphs complete `importance -> data problem -> taxonomy -> scenario motivation` before the algorithm appears.
- The host-entity criterion directly determines coverage and communication limitations.
- The scenario paragraph includes only the workflow required to understand decision coupling.
- The algorithm mechanism maps one-to-one to a specific structural difficulty.
- Author-level platform results and dynamic-response mechanisms remain in Related Work.
- One source is reused for two different claims; the stricter reusable practice is to use a more direct source for one claim or merge the claims.

### 3. Terrain-aware UAV-enabled MEC

**Center-sentence chain**

1. UAV-MEC supports smart-city services, while QoS and safe flight govern reliability.
2. The first hotspot is QoS: statistical, radio-map, and geographic channel models each retain a terrain-related limitation.
3. The second hotspot is flight safety: region restriction and safe-path optimization leave the destination-safety relationship incomplete.
4. The two lines merge into a terrain-aware scenario with channel, trajectory, destination, and resource decisions.
5. CMOEA is appropriate, while task-dependent search behavior motivates an adaptive mechanism.

**Writing characteristics**

- A long classification paragraph remains coherent because every subordinate center sentence answers the channel-model question.
- The two hotspot lines explicitly merge before the scenario is proposed.
- Category-level principles and one relevant limitation stay in the Introduction; detailed predictors, constraints, and examples move to Related Work.
- The paper demonstrates that secondary center sentences are acceptable under one primary question.
- Its repeated taxonomy citations are not a model to copy: cite either the umbrella taxonomy or the category-specific evidence once.

### 4. Reliable task offloading in dispersed computing

**Center-sentence chain**

1. Dispersed computing uses idle IoT resources, while latency, failures, and self-interest require delay-price-reliability optimization.
2. Parallel versus serial execution, reliability redundancy, and multi-objective decision making form three coequal difficulties.
3. A batch edge server and volunteer devices create a delay-price conflict for which a weighted sum yields only one tradeoff.
4. Evolutionary optimization can produce multiple tradeoffs, while feasibility, convergence, and diversity motivate dual populations and repair.

**Writing characteristics**

- The paper does not force a literature taxonomy when the problem already has three clear difficulties.
- The first paragraph combines background and motivation without losing one controlling center.
- Weighted-sum limitations remain category-level.
- All ten cited sources receive one Introduction role.

### 5. HAP-UAV planning

**Center-sentence chain**

1. Low-altitude-economy networks make urban airspace a shared operational resource.
2. Spatial areas, admission windows, and onboard endurance require planners to decide where and when UAVs operate.
3. Recovery infrastructure is classified as fixed-ground, mobile-ground, or aerial-mothership.
4. Existing mothership plans are fixed before a mission, while evolving battery and data states make that allocation inefficient.
5. The HAP launches UAVs, supports regional collection, replans periodically, and recovers low-energy UAVs.
6. Each cycle couples waypoint, assignment, hover-position, and bandwidth decisions under energy and utility objectives.
7. Objective conflict, mixed feasibility, and decision-shaped dynamic feasible regions motivate current-state feasible-solution generation.

**Writing characteristics**

- The first two paragraphs establish field position and scientific difficulty before surveying approaches.
- One infrastructure criterion governs all three categories.
- Only the closest fixed-plan assumption is needed to derive the dynamic scenario.
- The algorithm chain is causal: `previous decision updates state -> new feasible region cannot be inferred from history -> historical candidates may be infeasible -> generate from current state`.
- All seventeen citations receive one Introduction role.

## Introduction versus Related Work

The same literature performs different jobs in the two sections:

| Content | Introduction | Related Work |
|---|---|---|
| Research taxonomy | Criterion, category names, motivation-relevant shared boundary | Representative works and within-category differences |
| Individual paper | Normally unnamed; at most one closest assumption when essential | Authors, methods, variables, objectives, evidence, and residual boundary |
| Technical mechanism | Only the first-order distinction needed to justify the paper's choice | Workflow, detailed mechanism, strengths, weaknesses, and conditions |
| Limitation | Category-level and scenario-relevant | Paper-level and assumption-specific |
| Citation role | Ground facts, taxonomy, and shared boundary | Build an auditable paper-level evidence chain |

Direct contrasts from the benchmarks:

1. The demand-aware Introduction summarizes sequential and fixed deployment in one paragraph; Related Work lists trajectory, resource, DRL, game, and fixed-position studies.
2. The fusion Introduction gives the three host categories in three sentences; Related Work supplies authors, systems, and outcomes.
3. The terrain-aware Introduction gives one relevant limitation per channel family; Related Work explains predictors, KNN, distance models, and safety constraints.
4. The HAP-UAV Introduction compares three infrastructure families and isolates static mothership planning; Related Work explains individual stations, vehicles, HAP communication, and mothership-routing methods.

A sentence usually belongs in Related Work if its subject can naturally become an author's name and the sentence continues with the algorithm, optimized variables, or experimental result. It may remain in the Introduction when it explains why a class matters and which shared condition limits it.

## Typical failures in migration and rotation papers

### Detouring into a migration tutorial

After establishing service continuity, a draft often explains stop-and-copy, pre-copy, post-copy, checkpoints, or acknowledgments in full. This diverts the center-sentence chain from why state handover is needed.

Compress the move to:

`category-level migration treatment -> shared source/workload/time assumption -> why the new operating condition invalidates it`

Leave mechanisms, representative papers, variables, and failure branches to Related Work or the System Model.

### Advancing too many ideas in one paragraph

Common overload includes moving from MEC to UAVs, fleets, charging, and rotation in one paragraph; defining stateful service, giving an application, explaining a protocol, and posing the optimization in another; or surveying solvers and detailing all proposed modules in the algorithm paragraph.

Count rhetorical advances, not characters. Split or compress paragraphs with multiple independent turns or new questions.

### Repeating sources along the argument chain

A neighboring paper may be cited for fleet rotation, state transfer, and the hard-deadline category in three successive paragraphs. Even if every use is individually plausible, the source is repeatedly supporting one continuous claim chain. Assign it to the narrowest, most important claim and derive the surrounding statements without reattaching the same citation.

Likewise, do not cite the same migration cluster once to define stateful service and again to establish the no-departure-deadline category. Use one accurately scoped evidence role per source.

### Repeating Related Work at paper resolution

When the Introduction gives authors, mechanisms, joint variables, fixed assumptions, or unevaluated metrics paper by paper, citations are performing Related Work's evidentiary job. Keep category capability and shared boundary in the Introduction; put exact closest-work comparisons in Related Work.

### Retaining the useful causal core

Migration and rotation papers may retain abstract chains such as:

- `runtime work changes migration volume + resource use changes remaining time/energy -> terminal conditions co-evolve -> the current action must preserve a completion path`;
- `discrete selection changes future matching + continuous resources change state/capacity -> immediate feasibility does not imply terminal feasibility -> targeted checking or correction is required`.

Instantiate states, resources, deadlines, and modules only from the target manuscript.

## Transferable conclusions

1. Draft the center-sentence chain before paragraphs.
2. Make classification serve the motivation.
3. Treat MECE as an argument constraint, not a claim to cover the entire field.
4. Discuss categories in the Introduction and papers in Related Work.
5. Assign one primary Introduction role to each citation and default to zero repeated reference numbers.
6. Keep the scenario at workflow resolution, not full model resolution.
7. Derive every algorithm module from a previously stated structural difficulty.
8. Allow subordinate center sentences only under one controlling paragraph role.
9. Treat length as a consequence of functional load, not as a paragraph template.
