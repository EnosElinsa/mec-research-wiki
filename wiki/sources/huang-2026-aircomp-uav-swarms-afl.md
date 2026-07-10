---
type: source
title: "AirComp-Assisted Asynchronous Federated Learning for UAV Swarms: A Self-Adaptive Aggregation Scheme to Tackle Model Staleness"
authors: ["Yansong Huang", "Xuan Li", "Lu Zhang", "Mugen Peng"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3693868"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, federated-learning, over-the-air-computation, uav-swarm, asynchronous-federated-learning, model-staleness, beamforming, edge-intelligence]
related:
  - "[[aircomp-assisted-asynchronous-fl]]"
  - "[[over-the-air-computation]]"
  - "[[federated-learning]]"
  - "[[autonomous-uav-swarms]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[du-2024-distributed-foundation-models-6g]]"
  - "[[zhou-2026-cpsfl-uav-foundation-models]]"
  - "[[two-tier-submodel-partition]]"
created: 2026-07-11
updated: 2026-07-11
---

# AirComp-Assisted Asynchronous Federated Learning for UAV Swarms: A Self-Adaptive Aggregation Scheme to Tackle Model Staleness

## Citation

Huang, Y., Li, X., Zhang, L., & Peng, M. (2026). *AirComp-Assisted Asynchronous Federated Learning for UAV Swarms: A Self-Adaptive Aggregation Scheme to Tackle Model Staleness*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3693868.

## TL;DR

Proposes [[aircomp-assisted-asynchronous-fl]], where UAV sensing nodes train local models, communication UAVs aggregate via [[over-the-air-computation]], and a layer-wise self-adaptive aggregation rule suppresses stale model components. The design targets faster convergence and lower aggregation cost for low-altitude UAV-swarm learning.

## Problem framing

Synchronous FL wastes time in UAV swarms because bandwidth, energy, channel quality, and onboard computation vary across nodes. Asynchronous FL avoids waiting for all UAVs but creates stale local models. AirComp can aggregate simultaneous model transmissions, but it introduces signal distortion and makes server-side per-client staleness correction difficult because the server receives superposed signals rather than individual updates.

## System model

- A UAV swarm has sensing UAVs and communication UAVs.
- Sensing UAVs collect data and train local models; communication UAVs act as parameter servers and swarm heads.
- Sensing UAVs communicate with communication UAVs in a star topology; communication UAVs maintain a connected backbone.
- AirComp superposes selected local model signals over a multiple-access channel, with receiver beamforming and transmitter scaling controlling mean-squared aggregation distortion.
- UAV trajectories are externally determined in the paper's model; simulations use Olfati-Saber swarm coordination in a `20 x 20 x 20` cubic-kilometer region.

## Method

The framework jointly chooses the sensing-UAV-to-communication-UAV linkage scheme and receive beamforming under AirComp distortion and power constraints. The scheduling problem maximizes the uploaded training-data volume; it is decomposed into a UAV selection subproblem and a beamforming design subproblem solved with branch-and-bound and alternating optimization. To reduce model staleness, each selected sensing UAV compares local and global model layers by cosine similarity and uploads local layers only when their similarity exceeds a threshold that increases during training.

## Key findings

- Simulation parameters include 1-20 sensing UAVs, 1-10 communication UAVs, 30 global epochs, 120 s global epoch duration, 90 s local training/data-sensing time, 30 s transmission time, 11.2-22.4 GB training data per epoch per UAV, and `1.88 x 10^9` model parameters.
- The paper evaluates MNIST and VisDrone2019; MNIST is split IID, while VisDrone2019 is treated as non-IID.
- The alternating beamforming algorithm stays close to the ACR-BB optimal bounds in the reported simulations.
- AFL reduces data, time, and energy consumption to reach 90% accuracy compared with SFL in the reported resource plot; the adaptive scheme slightly increases transmitted data because selected UAVs receive the latest global model.
- Table II reports time-to-90%-accuracy values of 61.998/62.019 for SFL without/with adaptation, 30.991 for AFL without adaptation, and 27.014 for AFL with adaptation.
- The adaptive rule reduces early-training accuracy/loss fluctuation caused by stale models and gives VisDrone target-detection results closer to ground truth in the reported cases.

## Limitations / future work

The conclusion does not state an explicit future-work item. Scope limitations visible from the parse include simulation-only validation, externally determined UAV trajectories, idealized AirComp synchronization assumptions, and a self-adaptation rule evaluated on two datasets rather than across many UAV-swarm tasks.

## Relation to the corpus

This source concretizes the [[over-the-air-computation]] and [[federated-learning]] link that [[du-2024-distributed-foundation-models-6g]] describes at survey level. It also complements [[zhou-2026-cpsfl-uav-foundation-models]]: both accelerate UAV-network training under communication bottlenecks, but Zhou et al. pipeline split-FL gradients, while this paper uses AirComp-assisted asynchronous FL and layer-wise staleness filtering.

## Raw artifacts

- `raw/sources/AirComp-Assisted_Asynchronous_Federated_Learning_for_UAV_Swarms_A_Self-Adaptive_Aggregation_Scheme_to_Tackle_Model_Staleness/AirComp-Assisted_Asynchronous_Federated_Learning_for_UAV_Swarms_A_Self-Adaptive_Aggregation_Scheme_to_Tackle_Model_Staleness.md`
- Original PDF and extracted figures (`images/`) in the same folder.

## Metadata notes

The parsed Markdown is silent on DOI/venue/year metadata. DOI, venue, and year were verified by exact-title DOI lookup; technical claims and numbers above are grounded in the local parse.
