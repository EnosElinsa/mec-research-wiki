---
type: source
title: "Holt-Based Prediction Correction Dynamic Multiobjective Evolutionary Algorithm for IoT With AAV in Aerial Edge Computing"
authors: ["Lanlan Kang", "Yiyong Wang", "Zhilin Liu"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3527999"
venue: "IEEE Internet of Things Journal, 12(9)"
modeling_card: not_applicable
tags: [source, dynamic-multiobjective-optimization, evolutionary-algorithm, prediction, aerial-edge-computing, benchmark]
related:
  - "[[dynamic-constrained-multi-objective-optimization]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[hierarchical-aerial-mec]]"
created: 2026-11-02
updated: 2026-11-02
---

# Holt-Based Prediction Correction Dynamic Multiobjective Evolutionary Algorithm for IoT With AAV in Aerial Edge Computing

## Citation

Kang, L., Wang, Y., & Liu, Z. (2025). *Holt-Based Prediction Correction Dynamic Multiobjective Evolutionary Algorithm for IoT With AAV in Aerial Edge Computing*. **IEEE Internet of Things Journal, 12**(9). DOI: 10.1109/JIOT.2025.3527999.

## TL;DR

Treating AAV-assisted aerial edge computing as a dynamic multiobjective problem, the paper proposes HDMOEA: a Wilcoxon signed-rank test with an environment-perception operator detects changes and their intensity, Holt-based prediction with reference-point correction moves the population, and a bi-mutation step keeps diversity. It outperforms six prediction-based DMOEAs on benchmark suites.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Kang et al. [x] regarded autonomous aerial vehicle-assisted aerial edge computing as a dynamic multiobjective optimization problem and proposed a Holt-based prediction correction dynamic multiobjective evolutionary algorithm to continuously track the moving Pareto set. The algorithm uses the Wilcoxon signed-rank test to detect environmental change and a new environment perception operator to measure its intensity. A Holt-based prediction correction mechanism predicts individual positions in the next time window and corrects them with a reference point to improve prediction accuracy and search speed. A bi-mutation method maintains population diversity according to the intensity of change and reduces the risk of local optima. Compared with six state-of-the-art prediction-based dynamic multiobjective algorithms on multiple benchmark test sets, the algorithm tracks the Pareto front faster and obtains more accurate Pareto sets.

## Scope and method

The application is motivated by a three-layer AEC network, but the evaluation uses generic dynamic multiobjective benchmark functions, so the contribution is a foundational algorithm rather than a specific decision model.

## Key findings

- HDMOEA tracks moving Pareto fronts faster and more accurately than six compared algorithms.
- Ablation shows the bi-mutation strategy contributes to the best overall results.

## Limitations / future work

Performance on type II problems still needs improvement as the intensity of environmental change grows. The authors plan to target acceptable Pareto sets for AEC with AAV problems under cost and energy limits.

## Relation to the corpus

An algorithmic companion to [[dynamic-constrained-multi-objective-optimization]] and [[constrained-multi-objective-evolutionary-algorithm]] work motivated by aerial edge computing.

## Raw artifacts

- Parse: `raw/sources/Holt-Based_Prediction_Correction_Dynamic_Multiobjective_Evolutionary_Algorithm_for_IoT_With_AAV_in_Aerial_Edge_Computing/Holt-Based_Prediction_Correction_Dynamic_Multiobjective_Evolutionary_Algorithm_for_IoT_With_AAV_in_Aerial_Edge_Computing.md`
- Origin PDF and extracted figures are in the same folder.
