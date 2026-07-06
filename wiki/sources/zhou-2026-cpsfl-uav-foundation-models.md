---
type: source
title: "Communication-Pipelined Split Federated Learning for Foundation Model Fine-Tuning in UAV Networks"
authors: ["Zizhen Zhou", "Ying-Chang Liang", "Yanyu Cheng", "Wei Yang Bryan Lim"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3697889"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, split-federated-learning, federated-learning, distributed-foundation-models, resource-allocation, deep-reinforcement-learning, uav-trajectory-control, lora]
related:
  - "[[split-federated-learning]]"
  - "[[federated-learning]]"
  - "[[distributed-foundation-models]]"
  - "[[dnn-model-partition]]"
  - "[[pipeline-parallel-inference]]"
  - "[[uav-trajectory-control]]"
  - "[[du-2024-distributed-foundation-models-6g]]"
  - "[[han-2024-sagin-fl-handover]]"
  - "[[zhai-2023-fedleo-decentralized-fl]]"
created: 2026-07-06
updated: 2026-07-06
---

# Communication-Pipelined Split Federated Learning for Foundation Model Fine-Tuning in UAV Networks

## Citation

Zhou, Z., Liang, Y.-C., Cheng, Y., & Lim, W. Y. B. (2026). *Communication-Pipelined Split Federated Learning for Foundation Model Fine-Tuning in UAV Networks*. **IEEE Transactions on Mobile Computing**, 1-18. DOI: 10.1109/TMC.2026.3697889.

## TL;DR

Proposes CPSFL, a communication-pipelined split federated learning paradigm for LoRA fine-tuning of foundation models in UAV networks. Instead of parallel downlink gradient transmission, the server dedicates all downlink resources to the current client, schedules gradient transmission by priority, and allows intra-round asynchronous training. An attention-based DRL controller chooses the split point plus uplink bandwidth and server computing-frequency allocations using previous-round information, including UAV trajectories.

## Problem framing

UAVs collect images and videos that can adapt foundation models to low-altitude applications, but full fine-tuning is too heavy for UAV memory, compute, and energy. Federated learning keeps raw data local, and split federated learning moves part of the model to a server, but synchronous SFL is dominated by stragglers. In UAV networks, communication latency can dominate computation latency, so parallel downlink gradient transmission wastes resources and prolongs per-round training.

The paper minimizes a weighted sum of per-round training latency and worst-case client energy consumption by jointly optimizing split point selection and computing/communication resource allocation.

## System model

- A base station acts as the server and collaborates with multiple UAV clients.
- A foundation model is split into client-side and server-side parts; LoRA trainable parameters are fine-tuned while most pretrained weights are frozen.
- Each local iteration includes client forward propagation, smashed-data upload, server forward/backward propagation, downlink gradient transmission, client backward propagation, and model aggregation.
- UAV mobility affects per-slot channels within a training round, so the controller uses trajectory information rather than assuming a static round-level rate.

## Method

- Defines an SFL-PS paradigm where downlink gradient transmission is sequential: the server uses all downlink resources for one current gradient transmission.
- Builds CPSFL on SFL-PS through downlink gradient-transmission priority scheduling and intra-round asynchronous training.
- Formulates joint split-point selection, uplink bandwidth allocation, and server computing-frequency allocation.
- Uses an attention-based DRL framework in which the base-station agent consumes previous-round trajectory and training information to choose the next round's split point and resource allocations.

## Key findings

- CPSFL achieves the lowest average per-round latency across heterogeneous communication-rate, communication-overhead, and computing-capacity settings compared with SFL-PP, PipeSFL, and ablation variants.
- At split point $u=2$, the parse reports that CPSFL reduces average per-round latency by nearly 30% compared with PipeSFL.
- Under probabilistic gradient-transmission failures, the proposed scheduling calculation gives lower latency than the ablated variants in Table VI.
- In the Gauss-Markov mobility setting, the DRL-based CPSFL scheme reports an average objective value of 144.9 over the last 1000 rounds, versus 146.9 for the no-attention variant and 154.4/154.2 for equal and heuristic resource allocation.
- In the predefined-direction mobility setting, the corresponding objective values are 154.1, 158.4, 168.8, and 171.4.
- Policy-network inference latency remains below 0.1 s for 9 to 45 clients on the reported NVIDIA T400 GPU setup.

## Limitations / future work

The paper states that convergence analysis under transmission failures is left for future work. It also names multi-cell UAV deployments as a future extension for massive-scale settings.

## Relation to the corpus

This paper turns the wiki's [[distributed-foundation-models]] overview into a concrete UAV-network training protocol. It is a more specific instance of [[federated-learning]] because it combines federated aggregation with model partitioning; the reusable vocabulary is captured in [[split-federated-learning]]. Its trajectory-aware DRL controller also connects the foundation-model track back to [[uav-trajectory-control]] and wireless resource allocation.

## Raw artifacts

- `raw/sources/Communication-Pipelined Split Federated Learning for Foundation Model Fine-Tuning in UAV Networks/Communication-Pipelined Split Federated Learning for Foundation Model Fine-Tuning in UAV Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
