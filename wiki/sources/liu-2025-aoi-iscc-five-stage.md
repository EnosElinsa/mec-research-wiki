---
type: source
title: "Joint Sensing and Age of Information Optimization for Energy Constrained UAV-Assisted Integrated Sensing, Calculation, and Communication"
authors: ["Zechen Liu", "Xin Liu", "Wenyi Yang", "Xueyan Zhang"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3539108"
venue: "IEEE Transactions on Wireless Communications (TWC)"
tags: [source, integrated-sensing-computation-communication, age-of-information, alternating-optimization, uav-energy]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[age-of-information]]"
  - "[[radar-estimation-rate]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[zhou-2026-radar-energy-iscac]]"
created: 2026-07-13
updated: 2026-07-13
---

# Joint Sensing and Age of Information Optimization for Energy Constrained UAV-Assisted Integrated Sensing, Calculation, and Communication

## Citation

Liu, Z., Liu, X., Yang, W., & Zhang, X. (2025). Joint sensing and age of information optimization for energy constrained UAV-assisted integrated sensing, calculation, and communication. *IEEE Transactions on Wireless Communications, 24*(5), 4440-4453. https://doi.org/10.1109/TWC.2025.3539108

## TL;DR

One energy-limited UAV senses suburban targets, fuses detections locally, and sends the results to a collection center. A five-block alternating algorithm trades [[radar-estimation-rate|sensing-data amount]] against same-slot [[age-of-information|freshness]] by controlling target scheduling, repeated sensing, radar/communication power, CPU frequency, and motion.

## Problem and system model

The fixed-altitude UAV follows a fixed flight cycle divided into equal slots. Each slot schedules exactly one target and contains sensing, calculation, and communication stages. The model assumes that the fused result has the same size as one detection's sensing data.

The objective maximizes sensing-data amount plus a negatively weighted AoI term. Constraints cover radar SNR and success probability, transmission capacity, stage timing, energy, power/frequency bounds, kinematics, and periodic return. Its AoI is calculation plus transmission time inside a slot, not a queueing-age recursion across slots.

## Method

The MINLP is decomposed into scheduling, sensing count/time, transmit powers, CPU frequency, and motion blocks. The stages combine Lagrange multipliers and duality, subgradient updates, contraction iterations, conditional closed-form powers, and SCA lower bounds. They are alternated until the objective changes by less than a threshold.

Although the paper calls the returned variables optimal, the alternating approximations establish neither a global optimum nor equivalence to the original mixed-integer problem.

## Key findings

- Weighted-sum optimization retains substantially more sensing data than AoI-only minimization and substantially lower AoI than sensing-data-only maximization in the paper's plots.
- Increasing altitude reduces both sensing-data amount and AoI because weaker sensing yields less data to process and transmit.
- Increasing transmit power raises both metrics; increasing onboard energy raises sensing amount and lowers AoI until power/frequency limits bind.

The parse provides no headline percentage, and all evidence is simulation-only.

## Limitations

The setup assumes one UAV, fixed altitude and cycle, equal slots, known targets, exactly one target per slot, quasi-static within-slot geometry, deterministic channel/radar models, and a simplified fused-result size. It omits moving targets, clutter, uncertainty, queues, multi-UAV coordination, and field validation.

## Relation to the corpus

The paper connects [[integrated-sensing-computation-communication]] with [[age-of-information]] through an explicitly energy-constrained sensing/calculation/communication cycle. [[zhou-2026-radar-energy-iscac]] instead studies radar-energy tradeoffs without this same-slot freshness model.

## Raw artifacts

- Parse: `raw/sources/Joint_Sensing_and_Age_of_Information_Optimization_for_Energy_Constrained_UAV-Assisted_Integrated_Sensing_Calculation_and_Communication/Joint_Sensing_and_Age_of_Information_Optimization_for_Energy_Constrained_UAV-Assisted_Integrated_Sensing_Calculation_and_Communication.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
