---
type: source
title: "Scale-Reconfigurable Multi-Agent Reinforcement Learning for Aerial Networks in Dynamic Environments"
authors: ["Gyu Seon Kim", "Emily Jimin Roh", "Soyi Jung", "Soohyun Park", "Joongheon Kim"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3709180"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), accepted author version/early access"
tags: [source, scale-reconfigurable-marl, non-terrestrial-network, cubesat, fixed-wing-uav, dynamic-topology, energy-balancing]
related:
  - "[[scale-reconfigurable-marl]]"
  - "[[hidden-state-sharing-marl]]"
  - "[[non-terrestrial-network]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[ma-pomdp]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[energy-balancing-uav]]"
  - "[[kim-2026-qmarl-sagin-access]]"
  - "[[gyu-seon-kim]]"
  - "[[soyi-jung]]"
  - "[[soohyun-park]]"
  - "[[joongheon-kim]]"
created: 2026-07-14
updated: 2026-07-14
---

# Scale-Reconfigurable Multi-Agent Reinforcement Learning for Aerial Networks in Dynamic Environments

## Citation

Kim, G. S., Roh, E. J., Jung, S., Park, S., & Kim, J. (2026). *Scale-Reconfigurable Multi-Agent Reinforcement Learning for Aerial Networks in Dynamic Environments*. **IEEE Transactions on Mobile Computing**, accepted author version/early access, manuscript pp. 1-18. DOI: 10.1109/TMC.2026.3709180.

## TL;DR

SR-MARL lets ground-station agents schedule a changing visible set of CubeSats and large fixed-wing/eVTOL UAVs with masked actor/critic networks whose active input and hidden widths follow the current device count. Layerwise hidden-state sharing supports cooperation, and the reward combines communication quality with balanced residual energy. The reported gains are from a 4-GS, 12-device simulation and lack statistical uncertainty or comparisons with the scalable MARL methods discussed in related work.

## Problem and system model

Multiple terrestrial ground stations select visible CubeSats and UAVs for aerial access service. Device type and count within each station's range change over time, while a conventional fixed-width policy assumes fixed observation and action dimensions. Scheduling must maintain link performance without depleting or unevenly consuming NTN-device energy.

The environment is a decentralized partially observable MDP. Ground-station observations include local state and visible-device positions, path loss, SNR, capacity, residual energy, and relevant angles. Actions are binary device-selection indicators, limited by visibility and each station's monitoring capacity.

CubeSat positions are propagated from real two-line elements, and the energy model distinguishes photovoltaic charging on sunlit orbital segments from stored-energy use on the dark side. UAVs are 2,177 kg fixed-wing/eVTOL-class aircraft modeled with Euler-coordinate motion and a [[fixed-wing-propulsion-energy-model]]; the results do not directly characterize small battery-powered multirotors.

## Method

[[scale-reconfigurable-marl]] retains a fixed maximum actor/critic architecture but activates only the input and hidden neurons required for the currently visible device count. Inactive nodes are masked from forward and backward computation rather than filled by zero padding. Layer normalization operates over active neurons, and device slots use a deterministic physical ordering rather than a permutation-invariant set encoder.

When both input and hidden widths shrink by ratio $r$, the paper gives linear-layer complexity $O(nm r^2)$ instead of $O(nm)$. This depends on the chosen proportional width reduction and does not include every centralized-critic, communication, masking, or action-output cost.

[[hidden-state-sharing-marl]] averages other stations' hidden representations at each layer, concatenates that communication vector with the local representation, and applies the next layer. Distributed actors and a centralized critic then use TD actor-critic updates. The reward combines network quality, capacity, CNR, CubeSat alignment or UAV LoS probability, residual energy, and penalties for residual-energy imbalance.

Experiments use four ground stations, six CubeSats, six UAVs, 10,000 epochs, and a PyTorch implementation on an RTX 4090. Evaluated baselines are fixed MARL with padding, SR-MARL without inter-station communication, and single-agent SR-RL; A-MAPPO, MF-QMIX, and GPMA are discussed but not tested.

## Key findings

- Table VI reports normalized DPO-MDP rewards of 0.775 for SR-MARL, 0.329 for padding MARL, 0.446 without communication, and 0.234 for single-agent SR-RL. FO-MDP values are 0.734, 0.391, 0.471, and 0.297, respectively.
- Table VII reports SR-MARL values of 0.7673 QoS, 0.7945 capacity, 0.8234 CNR, 0.7822 CubeSat residual energy, and 0.8261 UAV residual energy. All are normalized table values, not estimates digitized from plots.
- Against padding, those Table VII values correspond to 1.56x QoS, 1.37x capacity, 1.37x CNR, 2.34x CubeSat residual energy, and 2.44x UAV residual energy. The abstract's 1.64x average network performance and 2.39x average residual-energy claims are author-reported because the averaging operation is not defined.
- Figs. 5(j)-(k) are described as showing that only SR-MARL avoids dead CubeSats or UAVs and that the baselines leave larger per-device energy variation. This is figure-derived qualitative evidence; exact terminal per-device values are not reported.
- Figs. 5(g)-(i) qualitatively support simultaneous improvement in communication indicators and average residual energy across training phases. The parse provides no uncertainty intervals for those plots.

## Limitations

Evaluation is simulation-only, with imported TLE and aerodynamic data but no live CubeSat/UAV network or hardware-in-the-loop test. Scale evidence covers four stations and 12 NTN devices. The fixed maximum architecture still requires a worst-case dimension, while centralized-critic and inter-agent communication costs grow with scale.

The paper gives possible slot-ordering criteria but no exact canonical order, and the representation is not permutation invariant. It reports no ablation for layer normalization, width selection, or individual reward terms, and no seed count, confidence interval, standard deviation, or significance test. GS locations, satellite identities and TLE epoch, UAV routes, and a complete reproducibility package are absent from the parse.

The model assumes every ground station is always connected to at least one NTN device and excludes states with UAV connectivity but no CubeSat connectivity. Its CubeSat-GS distance construction combines a surface arc with altitude, while Lemma 2 assumes both coordinate-vector magnitudes equal Earth's radius; it is not a complete 3-D satellite slant-range derivation and should be checked before reuse.

The parsed long-run objective and energy equation contain severe OCR/math corruption, so their exact symbolic transcription is unreliable. Terminology also shifts: "global ANN" appears where the context indicates AAN, device-count and action symbols vary, and Soyi Jung's biography says "Member, Senior IEEE" although the title line says Senior Member, IEEE. These inconsistencies are retained rather than normalized into unsupported equations or credentials.

Publication metadata remains pre-publication. The PDF is an accepted author version/early-access manuscript with pages 1-18; its `PP;99` metadata is provisional and does not establish a final volume, issue, or journal page range.

## Relation to the corpus

This source extends [[non-terrestrial-network]] and [[space-air-ground-integrated-network]] scheduling with a classical variable-width policy. It is closely related to [[kim-2026-qmarl-sagin-access]] through [[gyu-seon-kim]], [[soyi-jung]], [[soohyun-park]], and [[joongheon-kim]], but replaces the earlier quantum policy representation with masked scale-reconfigurable actor/critic networks.

## Raw artifacts

- Parse: `raw/sources/Scale-Reconfigurable_Multi-Agent_Reinforcement_Learning_for_Aerial_Networks_in_Dynamic_Environments/Scale-Reconfigurable_Multi-Agent_Reinforcement_Learning_for_Aerial_Networks_in_Dynamic_Environments.md`
- Origin PDF: `raw/sources/Scale-Reconfigurable_Multi-Agent_Reinforcement_Learning_for_Aerial_Networks_in_Dynamic_Environments/Scale-Reconfigurable_Multi-Agent_Reinforcement_Learning_for_Aerial_Networks_in_Dynamic_Environments.pdf`
- Figures: `raw/sources/Scale-Reconfigurable_Multi-Agent_Reinforcement_Learning_for_Aerial_Networks_in_Dynamic_Environments/images/`
