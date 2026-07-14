---
type: source
title: "Data Collection Maximization in IoT-Sensor Networks via an Energy-Constrained UAV"
authors: ["Yuchen Li", "Weifa Liang", "Wenzheng Xu", "Zichuan Xu", "Xiaohua Jia", "Yinlong Xu", "Haibin Kan"]
year: 2023
url: "https://doi.org/10.1109/TMC.2021.3084972"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav, data-collection, iot, orienteering, approximation-algorithm, energy-constraint]
related:
  - "[[energy-constrained-uav-data-collection-orienteering]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
created: 2026-07-12
updated: 2026-07-14
---

# Data Collection Maximization in IoT-Sensor Networks via an Energy-Constrained UAV

## Citation

Li, Y., Liang, W., Xu, W., Xu, Z., Jia, X., Xu, Y., & Kan, H. (2023). *Data Collection Maximization in IoT-Sensor Networks via an Energy-Constrained UAV*. **IEEE Transactions on Mobile Computing**, 22(1), 159-174. DOI: 10.1109/TMC.2021.3084972.

## TL;DR

Models battery-limited UAV collection as a depot-returning orienteering problem over discretized hover locations. It provides an ILP and approximation-based algorithms when coverage sets do not overlap, then marginal-data-per-added-energy heuristics for overlapping full or partial collection.

## Problem

Sparse aggregate IoT sensors store their own and neighboring data, but a UAV cannot necessarily visit every useful hovering region and return to its depot within one battery budget. The controller must jointly choose where to hover, how long to collect, and how to connect those locations into a closed tour so that collected data volume, not merely visited-node count, is maximized.

## System model

- One constant-speed, fixed-altitude UAV starts and ends at a depot. Flight and hovering/data-transfer time both consume energy.
- OFDMA lets all sensors inside a hovering coverage circle upload simultaneously over orthogonal channels at a common modeled data rate.
- The continuous plane is divided into square cells whose centers become candidate hovering locations.
- Full collection takes all covered data at a selected location. Partial collection divides each full sojourn into `K` virtual levels so the tour may collect only part of a location's data.
- Binary location and edge variables maximize collected volume under travel-plus-hover energy, flow, one-visit, depot-return, subtour-elimination, and domain constraints. Both full and partial variants are NP-hard by reduction from orienteering.

## Method

For small or moderate no-overlap instances, the paper gives an exact integer linear formulation. Algorithm 1 builds a metric auxiliary graph whose edge cost combines flight energy with half of each endpoint's hover energy, adds a dummy depot, applies metric orienteering, and converts the path into a closed UAV tour. Algorithm 2 expands each hover point into `K` virtual sojourn increments and repairs selected levels so earlier increments are included first; its proof states a value of at least one third of optimum.

When hover coverage overlaps, Algorithms 3 and 4 greedily add the physical or virtual location with the best marginal uncollected-data gain per added hover-plus-tour energy. Tour cost is recomputed through a Christofides TSP construction and residual sensor data is updated after each choice. These overlap algorithms are heuristics and do not inherit the no-overlap approximation guarantee.

## Key findings

- In the no-overlap full-collection experiments, Algorithm 1 collects at least 80% of the ILP optimum; at energy `3 x 10^5 J`, it collects about twice the benchmark's volume.
- At the same energy, partial Algorithm 2 with `K=4` collects `149.8 GB`, versus `131.9 GB` for full Algorithm 1.
- With overlapping coverage and grid size `5 m`, Algorithm 3 collects `132.8 GB`, Algorithm 4 with `K=2` collects `147.7 GB`, and the benchmark collects `74.14 GB`; the paper reports `79.1%` and `99%` improvements.
- Raising `K` from 2 to 4 increases Algorithm 4's collected data from `147.7 GB` to `150.7 GB`, but the printed runtime rises to `54.1` minutes versus `1.61` minutes for Algorithm 3.

## Limitations / parse caveats

The evaluation uses synthetic random deployments and no flight experiment. Constant speed/altitude and power rates, fixed sensor range, equal data rates, orthogonal channels, and grid-center discretization abstract away channel variation and interference. Higher partial-collection granularity improves volume but sharply increases runtime. The parse damages several equations, pseudocode lines, and the exact fraction in one theorem heading; the clearly printed one-third statement for Algorithm 2 is retained, while the uncertain Algorithm 1 guarantee is not. The prose calls `54.1/1.61` minutes "around 50 times" even though the ratio is about 33.6, so both printed times are preserved without endorsing the multiplier. The parse omits publication metadata; an exact-title Crossref record supplies the 2023 TMC citation. Technical claims come only from the parse.

## Relation to the corpus

[[energy-constrained-uav-data-collection-orienteering]] makes the route-and-hover energy budget explicit within [[uav-data-collection]]. Unlike freshness-driven MARL or communication-rate trajectory control, it treats collection as a closed combinatorial tour with full/partial rewards and distinguishes provable no-overlap algorithms from overlap heuristics.

## Raw artifacts

- Parse: `raw/sources/Data_Collection_Maximization_in_IoT-Sensor_Networks_via_an_Energy-Constrained_UAV/Data_Collection_Maximization_in_IoT-Sensor_Networks_via_an_Energy-Constrained_UAV.md`
- Origin PDF: `raw/sources/Data_Collection_Maximization_in_IoT-Sensor_Networks_via_an_Energy-Constrained_UAV/Data_Collection_Maximization_in_IoT-Sensor_Networks_via_an_Energy-Constrained_UAV.pdf`
- Figures: `raw/sources/Data_Collection_Maximization_in_IoT-Sensor_Networks_via_an_Energy-Constrained_UAV/images/`
