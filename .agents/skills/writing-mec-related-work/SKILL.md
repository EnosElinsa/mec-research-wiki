---
name: writing-mec-related-work
description: Use when drafting, revising, or auditing a Related Work section for MEC, UAV-MEC, HAP-UAV, vehicular edge/fusion, dispersed computing, or constrained multi-objective optimization papers—especially when the section reads like a paper-by-paper bibliography, repeats the Introduction, uses an arbitrary taxonomy, overexplains citations, or fails to derive the scenario/model/algorithm gap from grouped evidence.
---

# Writing MEC Related Work

## Purpose

Write Related Work as the evidence layer of the paper's motivation. Organize prior work by mechanisms that matter to the target problem, establish what each research line can already do, and end each line at the exact assumption or capability boundary that motivates the paper.

This skill is derived from the Related Work sections of five benchmark MEC-family manuscripts. Before drafting or auditing, read both bundled references in full:

- `references/reference-related-work-analysis.md` for the source-by-source structural evidence.
- `references/evidence-and-quality-gates.md` for the drafting workflow, language rules, and final audit.

The bundled analysis is self-contained. Do not require access to any original local corpus path.

## Governing distinction

Keep the Introduction and Related Work at different resolutions:

- **Introduction:** category-level map used to establish importance, focus, and motivation.
- **Related Work:** paper-level evidence used to justify that map and delimit the unresolved boundary.

Do not replay the complete Introduction story. Begin from the paper's already-established focus, then deepen only the literature evidence needed to support it.

## Required workflow

### 1. Recover the paper's claim chain

Read the Introduction, contribution list, system model, proposed method, and bibliography entries relevant to the target section. Extract:

1. the scenario novelty or operating condition;
2. the modeled mechanism that existing work omits or simplifies;
3. the algorithmic difficulty created by that mechanism;
4. the proposed module that addresses each residual difficulty.

If any of these are unknown, mark them as evidence gaps. Do not invent them from the title alone.

### 2. Build a coverage matrix before prose

For every intended subsection, record:

| Literature axis | Classification criterion | Categories | Representative evidence | Residual boundary | Paper module motivated |
|---|---|---|---|---|---|

Every subsection must have one explicit comparison axis. Every residual boundary must be supported by the works discussed immediately before it. Every major scenario/model/algorithm motivation claimed by the paper must have a home in the matrix.

### 3. Choose motivation-aligned subsection axes

Use the smallest set of axes that mirrors the paper's motivation. The benchmark default is two main axes; use a third only when it carries an indispensable evidence line that cannot be integrated without mixing classification criteria. Common axes are:

1. scenario architectures or deployment/service mechanisms;
2. the closest task, communication, migration, reliability, or state mechanism;
3. the solver family when the algorithmic challenge is a contribution.

Do not create a subsection merely because many citations share a keyword. Merge axes when the section is short. As a benchmark-scale guardrail, target four to seven substantive paragraphs for the whole section; exceed that only when each extra paragraph supports a distinct class-level boundary. Add an explicit **Critical Analysis** subsection only when several independently reviewed lines must be synthesized into one cross-cutting gap.

### 4. Classify by one criterion at a time

Within a subsection, apply one stable criterion and make the categories MECE with respect to the literature actually covered:

- categories do not overlap under the stated criterion;
- together they cover the papers used to support the subsection's claim;
- the criterion exposes the target paper's unresolved boundary.

An architectural evolution sequence is acceptable when the benchmark story genuinely progresses from one hosting/deployment paradigm to another. A chronological list is not a taxonomy.

### 5. Draft category paragraphs

Use this paragraph logic:

1. **Category center sentence:** define the category and its shared mechanism.
2. **Representative evidence:** group papers that share that mechanism; state only the problem setting, distinguishing decision/mechanism, and the result needed for comparison.
3. **Category synthesis:** state what this line achieves as a class.
4. **Boundary sentence:** name the exact assumption or missing capability that matters under the target scenario.
5. **Transition, if needed:** point to the next category or to the paper-level motivation.

The center sentence must remain intelligible without its citations. Do not begin a paragraph with an author's name unless the paragraph is intentionally comparing one closest work.

### 6. Control citation resolution

Use grouped citations for background consensus and author-level discussion for representative or closest works. As a default, one representative work receives no more than one sentence. Expand a paper only when its precise assumption is necessary to establish the target boundary.

Prefer two to four evidence units per category paragraph. Multiple papers with the same mechanism may form one compact evidence unit. Two lightly evidenced categories may share one paragraph when the classification remains explicit. Omit implementation details, experiment settings, and performance numbers unless they distinguish the literature class.

Do not reuse a closest paper or its limitation across subsections merely to make every axis look complete. If a citation must appear under two axes, each occurrence must establish a different, explicitly named analytical fact; otherwise keep it where it provides the strongest evidence and refer to the resulting class-level boundary only once.

### 7. Close at the right level

End each subsection with a bounded synthesis:

`shared capability -> retained assumption -> consequence in the target setting`

End the entire section by combining the residual boundaries into the smallest defensible paper-level gap. Map that gap to the scenario/model/algorithm needs, but do not repeat the whole proposed system or contribution list.

Use restrained claims such as "these issues have not been jointly modeled in the reviewed settings." Do not claim "no work," "the first," or "none of the existing studies" unless the search evidence supports that universal statement.

### 8. Run the evidence audit

Apply every hard gate in `references/evidence-and-quality-gates.md`. Revise until:

- the subsection headings alone reproduce the literature-side logic of the paper;
- the first sentences alone form a coherent classification story;
- every cited paper belongs to the declared category;
- every limitation follows from described evidence rather than assertion;
- the section does not duplicate the Introduction or pre-write the method section.

## Output expectations

When drafting, provide the finished Related Work text, not a literature-search diary. When auditing, identify failures by subsection and paragraph role, then give a corrected structure or revision. Preserve the manuscript's citation keys, terminology, and venue conventions.

Do not alter source files or bibliography entries unless the user asks for edits.
