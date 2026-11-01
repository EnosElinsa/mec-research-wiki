---
type: source
title: "Line-of-Sight Probability and Holding Distance in Non-Terrestrial Networks"
authors: ["Akram Al-Hourani"]
year: 2024
url: "https://doi.org/10.1109/LCOMM.2024.3357285"
venue: "IEEE Communications Letters, 28(3)"
modeling_card: not_applicable
tags: [source, los-probability, holding-distance, markov-chain, non-terrestrial-network, channel-modeling, measurement]
related:
  - "[[air-to-ground-channel-model]]"
  - "[[3gpp-uav-los-probability-model]]"
  - "[[non-terrestrial-network]]"
  - "[[al-hourani-2020-urban-los-probability]]"
  - "[[akram-al-hourani]]"
created: 2026-11-02
updated: 2026-11-02
---

# Line-of-Sight Probability and Holding Distance in Non-Terrestrial Networks

## Citation

Al-Hourani, A. (2024). *Line-of-Sight Probability and Holding Distance in Non-Terrestrial Networks*. **IEEE Communications Letters, 28**(3). DOI: 10.1109/LCOMM.2024.3357285.

## TL;DR

Beyond the probability that a satellite or UAV link is LoS, a moving user needs to know how long LoS lasts. The letter measures LoS with a camera across elevation angles in several urban settings, models LoS probability with stochastic geometry, and models LoS/NLoS transitions as a continuous-space Markov chain with a mean holding distance, releasing algorithms to emulate 1-D LoS sequences and 2-D LoS maps.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Al-Hourani [x] presented a framework for quantifying line-of-sight probability for non-terrestrial networks, including satellite and UAV links, in diverse urban settings using a practical camera-based approach across elevation angles. The letter introduced a technique that characterizes LoS states through a continuous-space Markov chain, including the mean holding distance of the LoS state and its distribution. It also outlined a practical method for emulating transitions between LoS and non-LoS states as users move through the propagation environment. Measurements in rural or highway, suburban, and dense urban environments validate the approach, with model parameters of 103, 74, and 28 for the mean holding distance in meters, respectively. Two open-source algorithms are provided to simulate LoS states along a one-dimensional path and to generate two-dimensional LoS maps.

## Scope and method

The letter combines stochastic-geometry LoS probability, a continuous-space Markov chain for state durations, and camera-based field measurements. It is a channel and measurement model without a decision problem.

## Key findings

- LoS probability and holding distance both depend on elevation angle and clutter density.
- Mean holding distance falls from rural to dense urban environments.
- The emulation algorithms reproduce LoS transitions for mobility studies.

## Limitations / future work

Measurements cover a limited set of urban settings.

## Relation to the corpus

Extends the static LoS models used in [[air-to-ground-channel-model]] and [[3gpp-uav-los-probability-model]] with state duration, building on [[al-hourani-2020-urban-los-probability]].

## Raw artifacts

- Parse: `raw/sources/Line-of-Sight_Probability_and_Holding_Distance_in_Non-Terrestrial_Networks/Line-of-Sight_Probability_and_Holding_Distance_in_Non-Terrestrial_Networks.md`
- Origin PDF and extracted figures are in the same folder.
