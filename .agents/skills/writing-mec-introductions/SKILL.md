---
name: writing-mec-introductions
description: Use when drafting, revising, or auditing an Introduction for MEC, UAV-MEC, HAP-UAV, vehicular edge computing, or related scenario-driven optimization papers—especially when paragraphs are bloated, the Introduction reads like Related Work, scenario-to-algorithm motivation is weak, citations are repeatedly reused, or designated benchmark papers must be matched.
---

# Writing MEC Introductions

## Core principle

Build the Introduction as a causal chain advanced by paragraph-opening center sentences. Reading only those opening sentences should reveal why the problem matters, which issue the paper focuses on, how relevant research is classified, why its shared boundary motivates the scenario, what decision difficulty the scenario creates, and why the proposed algorithm needs its specific modules.

Do not write a compressed Related Work section, a system-model manual, or an algorithm summary. Give each paragraph one primary rhetorical job. A subordinate center sentence is acceptable only when it develops the paragraph's primary claim.

## Required resources

Before every draft or audit:

1. Read the target abstract, current Introduction, Related Work, system model, method, contributions, and bibliography.
2. Read complete benchmark Introductions and their Related Work sections when the user supplies source papers; do not infer style from titles or abstracts.
3. Read `references/style-and-quality-gates.md` in full.
4. Read `references/reference-intro-analysis.md` when matching the bundled benchmark family.
5. Use only verifiable scenario, model, algorithm, and result claims.

For a Markdown manuscript with IEEE-style numbered citations, run:

```powershell
python -X utf8 scripts/audit_intro_citations.py <manuscript.md>
```

The command exits with code `1` when any reference number occurs more than once in the Introduction. Treat that result as a revision gate, not as proof of citation accuracy.

## Workflow

### 1. Establish the problem-method contract

Answer each question in one sentence before drafting:

- Why is the application or domain important?
- What precise problem does the paper study, and why does it arise?
- Which single criterion classifies the directly relevant research?
- What can each category do, and which condition limits them collectively?
- Why does that boundary naturally produce this paper's scenario?
- What are the scenario's actors, trigger, operating sequence, and completion boundary?
- Which decisions are coupled, and what are the objectives and hard constraints?
- Which scenario structure defeats or weakens a standard solver?
- Which proposed module addresses each structural difficulty?
- What do the completed experiments or analyses actually support?

Continue inspecting the manuscript and evidence until every answer is grounded.

### 2. Build a citation-role ledger

Before prose, assign each source one primary Introduction role:

| Claim ID | Exact claim | Source | Exact supporting passage/section | Evidence role | Used elsewhere in Introduction? |
|---|---|---|---|---|---|

Apply these rules:

- Verify the claimed fact in the cited source itself; title-level relevance is insufficient.
- Prefer a primary or authoritative source for a factual claim. Do not cite a neighboring optimization paper merely because it is already in the bibliography.
- Use the smallest citation cluster that fully supports the sentence.
- Give each source one primary evidence role in the Introduction.
- Do not use the same source repeatedly to support successive steps of one argument.
- Do not replace a correct repeated citation with a weaker source merely to satisfy deduplication. Merge or restructure the claims instead.

The default delivery gate is zero repeated reference numbers within the Introduction. A genuine exception requires two materially independent claims, a uniquely authoritative source, and an explicit audit note; never make such an exception silently.

### 3. Draft only the center-sentence spine

Use this functional order, merging adjacent functions when helpful but preserving causality:

1. background, concrete problem, and field position;
2. current focus and decisive difficulty;
3. motivation-aligned, MECE overview of the research landscape;
4. shared category boundary and scenario motivation;
5. scenario workflow, decisions, objectives, and major constraints;
6. algorithm motivation derived from scenario-specific state, resource, dependency, or feasibility structure;
7. proposed solver and modules mapped to those difficulties;
8. contributions and paper organization.

Read the opening sentences as one passage. Repair conceptual jumps, literature detours, an unmotivated scenario, or method-first reasoning before filling the paragraphs.

### 4. Fill each paragraph at Introduction resolution

Use:

`primary center sentence -> cause/fact -> necessary evidence or consequence -> optional subordinate center sentence -> optional transition`

- Prefer 3–5 sentences for ordinary paragraphs.
- Allow 5–7 sentences for classification or algorithm-motivation paragraphs only when they retain one primary job.
- Split or compress a paragraph with more than seven sentences, two independent turns, or two new questions.
- Keep protocol branches, symbols, formulas, and detailed boundary conditions in the system model.
- Keep paper-by-paper mechanisms, variables, and results in Related Work.

### 5. Control literature resolution and citation placement

Use citations in the Introduction to support field facts, category existence, category-level capabilities, shared assumptions, and solver-level boundaries. Place each citation immediately after the smallest proposition it supports.

Do not:

- name a sequence of authors or algorithms;
- describe the internal workflow or optimized variables of multiple papers;
- attach one large citation cluster to a sentence containing several unsupported claims;
- repeat the same citation cluster in background, classification, and gap paragraphs;
- cite one paper several times because it happens to discuss the whole topic.

One closest paper may receive one sentence when its exact assumption directly produces the scenario motivation. Put detailed `work -> method -> decisions -> residual boundary` comparisons in Related Work.

### 6. Derive the algorithm from the scenario

Proceed in this order:

1. name the exact decision structure created by the scenario;
2. explain why the general solver family is suitable;
3. identify why its standard form is insufficient for this structure;
4. introduce each scenario-specific module and map it to one stated difficulty;
5. claim only effects established by the manuscript.

Do not motivate a solver because reinforcement learning or evolutionary optimization is popular. The solver is the carrier; the scenario-specific mechanism is the narrative focus.

### 7. Write contributions and run all gates

Use two to four contributions spanning `scenario/model -> problem -> algorithm/evidence`. Start each item with an action and new object, then state its bounded effect or validation scope.

Before delivery:

1. run the center-sentence, MECE, paragraph, evidence, and module-mapping gates in `references/style-and-quality-gates.md`;
2. run `scripts/audit_intro_citations.py` for Markdown numbered citations;
3. inspect every flagged repeated source against the citation-role ledger;
4. revise until every citation is accurate, locally placed, necessary, and non-redundant;
5. confirm that no paper-level discussion belongs in Related Work.

## Output constraints

- Match the manuscript's language, terminology, and citation format.
- Deliver only the requested prose or audit by default.
- When explaining an audit, lead with the center-sentence spine and highest-impact failures.
- Do not modify Related Work, the system model, or the bibliography unless the user authorizes those changes.
