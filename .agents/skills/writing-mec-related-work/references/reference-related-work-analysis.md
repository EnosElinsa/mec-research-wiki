# Reference-derived analysis of MEC Related Work sections

## Scope and portable source identification

This analysis is distilled from the Related Work sections of the following benchmark manuscripts. Titles and section labels, rather than machine-specific file paths, identify the evidence base.

1. **Demand-Aware Multi-Area Multi-UAV Empowered Mobile Edge Computing: A Joint Energy and Delay Optimization** — Section II, organized around multi-UAV MEC deployment and constrained multi-objective evolutionary algorithms.
2. **UAV-Enabled Multi-Source Data Fusion in Vehicular Networks: A Joint Optimization Approach for Reliability and Latency** — Section II, organized around fusion-platform architectures and dynamic constrained multi-objective evolutionary algorithms; DOI `10.1109/TWC.2026.3676831`.
3. **Terrain-Aware UAV-Enabled Mobile Edge Computing in Urban Environments: A Constrained Multi-Objective Approach With Task-Adaptive Mechanism** — Section II, organized around path-loss models, safe UAV trajectory design, and an explicit critical analysis; DOI `10.1109/TVT.2025.3604250`.
4. **Joint Latency and Charge Cost Minimization for Reliable Task Offloading in Dispersed Computing: A Multi-objective Optimization Approach** — Section II, a compact thematic review of task/resource allocation, workflow offloading, incentives, and multi-objective formulations; DOI `10.1109/TMC.2026.3679393`.
5. **HAP-UAV periodic data-collection planning manuscript** — author-supplied benchmark draft, Section II, organized around ground-to-air deployment evolution and dynamic constrained multi-objective evolutionary algorithms.

The fifth source is a non-public writing benchmark. No original paper is required at runtime: the reusable structural observations are recorded below.

## What is stable across the five sources

### Related Work mirrors the motivation axes

The section headings are not generic topic buckets. They correspond to the exact literature lines needed by the paper's scenario and solver motivation:

- deployment/service architecture plus optimization method in the demand-aware multi-UAV paper;
- fusion host architecture plus dynamic optimizer in the vehicular-fusion paper;
- channel abstraction plus flight-safety planning in the terrain-aware paper;
- heterogeneous processing/reliability/incentives plus multi-objective formulation in the dispersed-computing paper;
- deployment evolution plus dynamic optimizer in the HAP-UAV manuscript.

Thus, subsection design begins with the paper's claim chain, not with the bibliography.

### A category paragraph performs four jobs

Across the benchmark set, a useful category paragraph normally:

1. names or defines a mechanism family;
2. selects representative works within that family;
3. summarizes the shared capability of those works;
4. ends at a category-level limitation relevant to the present problem.

The literature evidence is detailed enough to support the limitation, but it does not reproduce each abstract. The desired resolution is usually one distinguishing mechanism per cited work.

### Gaps are synthesized, not accumulated

The benchmark papers do not treat every paper limitation as a separate novelty claim. Individual observations are first aggregated into a class-level boundary. The final paragraph then combines two or more class-level boundaries into the paper's motivation.

This produces a hierarchy:

`paper evidence -> mechanism family -> family boundary -> cross-family gap -> paper motivation`

### Algorithm literature is tied to the problem structure

The algorithm subsections do not end with a generic statement that existing algorithms perform poorly. They identify a structural mismatch:

- flexible allocation creates mixed, coupled feasibility conditions;
- cooperative perception creates cascaded variable dependencies;
- urban terrain creates constrained tasks with heterogeneous search behavior;
- HAP-UAV planning changes the environment through the previous cycle's decisions.

The final solver gap must therefore name the decision dependency, constraint geometry, or dynamic-state mechanism that the generic algorithm does not preserve.

## Source-by-source structural anatomy

## 1. Demand-aware multi-area multi-UAV MEC

The section announces two review themes at the start: multi-UAV MEC and constrained multi-objective evolutionary algorithms.

The multi-UAV MEC subsection classifies deployment by **how UAVs are assigned across areas**:

- sequential deployment, where UAVs visit or serve areas according to a schedule;
- fixed deployment, where each area receives a predetermined UAV allocation.

Each category starts with its operating principle, gives representative joint-optimization examples, and ends with the same scenario-relevant boundary: the number of UAVs per area remains fixed with respect to heterogeneous demand. The repeated boundary is deliberate because it supports the demand-aware allocation motivation.

The algorithm subsection reviews representative constraint-handling mechanisms, then synthesizes why generic methods are insufficient for the target mixed-integer coupling. The closest method is compared at the level of constraint structure rather than by a long performance narrative.

**Reusable lesson:** when two literature categories share one decisive assumption, state it at category level and merge it once into the scenario gap.

## 2. UAV-enabled multi-source fusion in vehicular networks

The scenario subsection classifies prior platforms by **which entity hosts fusion**:

- vehicle-to-vehicle fusion;
- infrastructure-based fusion;
- hybrid fusion.

For each class, the paragraph defines the hosting mechanism, selects representative systems, and ends with a platform-specific limitation such as occlusion, fixed spatial coverage, or coordination overhead. This is a strong MECE axis because each reviewed system can be placed by its fusion host.

The DCMOEA subsection then reviews dynamic-response mechanisms. Its closing synthesis does not merely claim a dynamic environment; it identifies cascaded dependencies among request response, data collection, and resource allocation.

**Reusable lesson:** a useful taxonomy exposes why the proposed scenario needs a different system role, while the algorithm review exposes why that role creates a different decision dependency.

## 3. Terrain-aware UAV-MEC in urban environments

The section separates two physical modeling lines:

- path-loss/channel models, classified as statistical, radio-map-based, and geographic/environment-explicit models;
- safe trajectory design, grouped by how environmental obstacles and flight safety are represented.

It then uses a dedicated **Critical Analysis** subsection to combine the remaining channel-estimation and trajectory-safety limitations. This is justified because the two reviewed lines are independently mature yet jointly incomplete for the target urban setting.

The critical analysis maps the two boundaries to corresponding proposed modules. It remains concise: the model and algorithm details are deferred to later sections.

**Reusable lesson:** use a separate synthesis subsection when the paper's central contribution arises at the intersection of multiple independently classified literatures.

## 4. Reliable task offloading in dispersed computing

This paper uses a compact thematic variant without multiple lettered subsections. Successive paragraphs cover:

- task assignment and resource allocation for computing efficiency;
- workflow and multi-hop offloading;
- incentive mechanisms;
- multi-objective optimization and task-dependency assumptions.

The closing comparison states how the target setting differs: heterogeneous parallel/serial processing, reliability through redundancy, charging policy, and joint multi-objective decisions.

**Reusable lesson:** subsection count is not a goal. A short Related Work may use thematic paragraphs if each paragraph still has a stable center and the closing comparison integrates them.

## 5. HAP-UAV periodic planning manuscript

The scenario review uses **deployment evolution** as its axis:

1. fixed terrestrial infrastructure;
2. mobile terrestrial support;
3. aerial-mothership deployment.

The sequence is meaningful because each architecture relaxes a limitation of the preceding one. Representative works remain subordinate to that evolution story.

The DCMOEA review moves from historical-response methods to the target difficulty. Its closing argument is causal: previous solutions summarize history, but in the HAP-UAV problem the current feasible region depends on a cycle state produced by earlier decisions, so blindly adapting historical solutions can yield infeasible candidates.

**Reusable lesson:** an evolution narrative is valid only when each stage changes the mechanism relevant to the paper; chronological publication order alone is insufficient.

## Paragraph-level story test

Read only the first sentence of every paragraph. In a benchmark-like section, those sentences should form a complete literature story such as:

1. This paper relates to two research lines.
2. Existing service architectures can be classified by a stated mechanism.
3. The first category achieves one capability under one assumption.
4. The second category changes that mechanism but retains another boundary.
5. Existing solvers employ several response strategies.
6. These strategies do not preserve the target dependency or feasibility condition.

Supporting sentences add evidence; they must not become a second, unrelated story.

## How this differs from the Introduction benchmark

Both sections may use the same categories, but their jobs differ:

| Introduction | Related Work |
|---|---|
| establishes importance and focus | establishes evidence and comparative boundary |
| names categories at field level | explains representative mechanisms inside categories |
| uses few citations per move | uses enough paper-level evidence to justify synthesis |
| moves quickly to scenario and algorithm motivation | remains on prior work until the evidence supports that motivation |
| avoids detailed paper descriptions | permits selective author/work-level descriptions |

If a paragraph can be copied unchanged between the two sections, at least one section is at the wrong resolution.

## Benchmark-consistent failure patterns

1. **Bibliography parade:** every sentence starts with an author and no class-level claim governs the paragraph.
2. **Abstract compression:** a cited work receives its setting, full formulation, algorithm architecture, and numerical results even though only one mechanism matters.
3. **Mixed taxonomy:** categories alternate among platform, objective, algorithm, and chronology without a common criterion.
4. **Claim before evidence:** a universal gap is asserted before the reviewed works establish it.
5. **Introduction replay:** background importance, complete scenario description, and full contributions are repeated.
6. **Closest-work tunnel vision:** one neighboring paper occupies most of the section and obscures the broader class boundary.
7. **Solver-name list:** algorithms are enumerated without explaining which target dependency or feasibility condition they fail to preserve.
8. **Unsupported novelty language:** "first," "no existing work," or "all prior studies" appears without comprehensive evidence.
