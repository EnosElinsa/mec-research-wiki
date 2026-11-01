---
type: source
title: "Automating CSI Measurement with UAVs: from Problem Formulation to Energy-Optimal Solution"
authors: ["Sixu Piao", "Zhongjie Ba", "Lu Su", "Dimitrios Koutsonikolas", "Shi Li", "Kui Ren"]
year: 2019
url: "not in parse"
venue: "IEEE INFOCOM 2019 - IEEE Conference on Computer Communications"
modeling_card: required
tags: [source, csi-fingerprinting, indoor-localization, uav-motion-planning, generalized-traveling-salesman-problem, energy-minimization, testbed]
related:
  - "[[generalized-traveling-salesman-problem]]"
  - "[[uav-trajectory-control]]"
  - "[[hardware-validation-and-sim-to-real-in-mec]]"
created: 2026-11-02
updated: 2026-11-02
---

# Automating CSI Measurement with UAVs: from Problem Formulation to Energy-Optimal Solution

## Citation

Piao, S., Ba, Z., Su, L., Koutsonikolas, D., Li, S., & Ren, K. (2019). *Automating CSI Measurement with UAVs: from Problem Formulation to Energy-Optimal Solution*. **IEEE INFOCOM 2019 - IEEE Conference on Computer Communications**. DOI not in parse.

## TL;DR

Building a CSI fingerprint map for indoor localization takes a lot of manual effort. The paper lets a drone collect CSI at measurement points, models flight, turning, and measurement actions on a graph, and casts the Minimum-Energy Motion Planning (MEMP) problem as a Generalized Traveling Salesman Problem, saving 37.8% energy over coverage path planning on a real drone.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A commodity programmable drone with a CSI measurement module must visit every required measurement location in an indoor area. A grid graph $G=(V,E,w)$ expands each physical location into a widget $\mathcal W_\eta$ of four vertices for the UAV's four orientations, replicated per access point; edge weights $w_{ij}$ are the energy of moving between grids, turning within a widget, and switching access points.

**Problem & objective**: MEMP: $\min\sum_{i,j\in V}w_{ij}f_{ij}$, the total energy of the drone's walk on the graph.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Edge traversals | $f_{ij}$ | nonnegative integer | Number of times the walk uses edge $(i,j)$ |
| Vertex choice | $v_i$ | binary | Vertex $i$ is chosen to represent its widget |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (16) | Exactly one vertex per widget, $\sum_{i\in\mathcal W_\eta}v_i=1$. |
| (17) | Flow conservation, inflow equals outflow at every vertex. |
| (18) | Connectivity, every cut separating chosen vertices is crossed, $\sum f_{ij}+f_{ji}\ge1$. |
| (19) | $f_{ij}\in\mathbb N$, $v_i\in\{0,1\}$. |

**Algorithm**: Show MEMP is equivalent to the Generalized Traveling Salesman Problem on the partitioned vertex set and solve it with an existing GTSP solver.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Piao et al. [x] explored automating CSI fingerprint map construction for indoor localization with an unmanned aerial vehicle, addressing the large human effort that limits fingerprinting approaches. Given the limited battery of commodity UAVs, they formulated an energy optimization problem on a graph model that includes the cost of the UAV's possible actions. The formulated problem is transformed into the classic Generalized Traveling Salesman Problem, which can be solved efficiently. The system was implemented on an off-the-shelf programmable drone equipped with a CSI measurement module. Experiments show a 37.8% energy saving over a conventional coverage path planning algorithm, and the collected CSI data support accurate indoor localization.

## Problem framing

Coverage path planning treats measurement as passing over points, but a drone also spends energy turning and hovering to measure. Modeling these actions explicitly changes which route is cheapest.

## System model

- Each location becomes a widget of four orientation vertices; inter-widget edges follow the flying orientation.
- Widgets are replicated per access point, with switching edges between them.

## Method

The MEMP integer program is shown equivalent to GTSP, so existing solvers return energy-optimal walks.

## Key findings

- The solution saves 37.8% energy relative to the baseline coverage planner.
- With the UAV-built map, 64.85% of localization errors are within 2 m, compared with 66.21% for manually collected training data.

## Limitations / future work

The study is limited to indoor CSI collection with one drone.

## Relation to the corpus

An early hardware-validated use of [[generalized-traveling-salesman-problem]] for UAV motion planning, relevant to [[hardware-validation-and-sim-to-real-in-mec]].

## Raw artifacts

- Parse: `raw/sources/Automating_CSI_Measurement_with_UAVs_from_Problem_Formulation_to_Energy-Optimal_Solution/Automating_CSI_Measurement_with_UAVs_from_Problem_Formulation_to_Energy-Optimal_Solution.md`
- Origin PDF and extracted figures are in the same folder.
