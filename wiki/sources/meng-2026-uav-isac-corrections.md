---
type: source
title: "Corrections to 'Throughput Maximization for UAV-Enabled Integrated Periodic Sensing and Communication'"
authors: ["Kaitao Meng", "Qingqing Wu", "Wen Chen"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3634306"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, correction, uav, isac, periodic-sensing, convex-optimization, trajectory-optimization]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-trajectory-control]]"
  - "[[device-association]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[qingqing-wu]]"
created: 2026-07-12
updated: 2026-07-12
---

# Corrections to "Throughput Maximization for UAV-Enabled Integrated Periodic Sensing and Communication"

## Citation

Meng, K., Wu, Q., & Chen, W. (2026). *Corrections to "Throughput Maximization for UAV-Enabled Integrated Periodic Sensing and Communication"*. **IEEE Transactions on Wireless Communications**, 25, 7873. DOI: 10.1109/TWC.2025.3634306.

## TL;DR

Repairs two convexification steps in the 2023 UAV periodic-sensing/communication paper: an extra user-association factor is removed from one rate bound, and an omitted auxiliary-variable/Taylor transformation replaces an incorrect negative-definiteness claim. The corrected subproblems are convex, and the note states that the original simulations already used the corrected transformed formulation.

## Correction scope

The note does not restate the full UAV-ISAC model. It addresses the original joint design over periodic sensing, communication, user association, beamforming, and UAV trajectory, and responds to a 2025 comments paper that challenged the convexity of subproblems P2.2 and P2.5.

## Corrected formulation

- The definition of the lower-bounded rate incorrectly repeats `alpha_k[n]`, which is already accounted for. Removing that factor makes P2.2 convex.
- The statement that `H_{k,j}` is negative definite is incorrect and irrelevant to the solution, so the correction removes that argument.
- For P2.5, a new auxiliary variable `u_{c,k}[n]` separates the logarithmic rate expression. A first-order Taylor expansion of `log_2(z_{c,k}[n])` produces the corrected surrogate rate.
- Corrected P2.5 maximizes average aggregate transformed rate over trajectory block `Q`, channel/slack variables, and the new auxiliary variables, subject to the original feasibility constraints plus the new inequality and per-user/per-period minimum-rate constraint.
- The note states that all corrected constraints are convex and that the transformed problem can be run in CVX; the untransformed original P2.5 cannot.

## Findings

No new experiment or performance comparison is introduced. The correction states that the simulations in the original paper were executed with the corrected transformed P2.5, so its reported simulation results remain unchanged.

## Limitations / parse caveats

The note depends on definitions and constraints numbered in the original article and does not reproduce them. It validates the repaired convex subproblem presentation rather than independently rerunning the original experiments. Equation OCR is noisy, so this page preserves the prose-level changes without attempting a symbol-perfect transcription. The DOI appears in the parse; final 2026 volume/page metadata was verified through its Crossref record.

## Relation to the corpus

This correction is a useful warning for [[alternating-optimization-sdr-sca]] pipelines: convexity must follow from the actual transformed variables and bounds, not an unsupported Hessian claim. It also preserves the coupling among [[device-association]], beamforming, and [[uav-trajectory-control]] inside periodic [[integrated-sensing-and-communication|UAV-ISAC]].

## Raw artifacts

- Parse: `raw/sources/Corrections_to_Throughput_Maximization_for_UAV-Enabled_Integrated_Periodic_Sensing_and_Communication-/Corrections_to_Throughput_Maximization_for_UAV-Enabled_Integrated_Periodic_Sensing_and_Communication-.md`
- Origin PDF: `raw/sources/Corrections_to_Throughput_Maximization_for_UAV-Enabled_Integrated_Periodic_Sensing_and_Communication-/Corrections_to_Throughput_Maximization_for_UAV-Enabled_Integrated_Periodic_Sensing_and_Communication-.pdf`
- Figures: `raw/sources/Corrections_to_Throughput_Maximization_for_UAV-Enabled_Integrated_Periodic_Sensing_and_Communication-/images/`
