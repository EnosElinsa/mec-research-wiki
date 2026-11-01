---
type: source
title: "On the Probability of Line-of-Sight in Urban Environments"
authors: ["Akram Al-Hourani"]
year: 2020
url: "https://doi.org/10.1109/LWC.2020.2984497"
venue: "IEEE Wireless Communications Letters, 9(8)"
modeling_card: not_applicable
tags: [source, los-probability, stochastic-geometry, urban-channel, uav-to-uav, channel-modeling]
related:
  - "[[air-to-ground-channel-model]]"
  - "[[3gpp-uav-los-probability-model]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
  - "[[al-hourani-2024-los-holding-distance-ntn]]"
  - "[[akram-al-hourani]]"
created: 2026-11-02
updated: 2026-11-02
---

# On the Probability of Line-of-Sight in Urban Environments

## Citation

Al-Hourani, A. (2020). *On the Probability of Line-of-Sight in Urban Environments*. **IEEE Wireless Communications Letters, 9**(8). DOI: 10.1109/LWC.2020.2984497.

## TL;DR

A stochastic-geometry model gives the geometric LoS probability between any two points in 3-D urban space from their heights, their distance, and four parameters describing the built environment. The analytic formulas match ray tracing on real geographic data.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Al-Hourani [x] presented a model for predicting the geometric line-of-sight probability in different urban environments based on stochastic geometry, motivated by applications ranging from UAV-to-UAV networks to land mobile satellite services and mmWave cellular coverage. For two points in three-dimensional space, the model takes the height of each point and the distance between them as inputs, together with four simple parameters that describe the geometric properties of the environment. The model combines a simple formulation with a high degree of accuracy compared with real-life geographic data. Its analytic results are consistent with ray tracing of the geographic data.

## Scope and method

The letter derives closed-form LoS probability from random building placement and heights and validates it against ray tracing. It defines no decision model.

## Key findings

- LoS probability between arbitrary heights follows simple analytic expressions.
- The model adapts to urban types through its environment parameters.

## Limitations / future work

The model captures geometric blockage only.

## Relation to the corpus

Generalizes the ground-to-air LoS used in [[al-hourani-2014-optimal-lap-altitude]] and [[air-to-ground-channel-model]] to arbitrary endpoint heights, a foundation reused by [[al-hourani-2024-los-holding-distance-ntn]].

## Raw artifacts

- Parse: `raw/sources/On_the_Probability_of_Line-of-Sight_in_Urban_Environments/On_the_Probability_of_Line-of-Sight_in_Urban_Environments.md`
- Origin PDF and extracted figures are in the same folder.
