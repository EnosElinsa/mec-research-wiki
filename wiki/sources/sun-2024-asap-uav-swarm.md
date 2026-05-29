---
type: source
title: "All-Sky Autonomous Computing in UAV Swarm"
tags:
  - source
  - uav-swarm
  - collaborative-inference
  - edge-computing
  - task-scheduling
related:
  - "[[collaborative-dl-inference]]"
  - "[[dnn-model-partition]]"
  - "[[data-partition-parallel-inference]]"
  - "[[pipeline-parallel-inference]]"
  - "[[dl-inference-latency-prediction]]"
  - "[[adaptive-intermediate-data-compression]]"
  - "[[elastic-task-scheduling]]"
  - "[[load-balancing-uav-mec]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[post-disaster-mec]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
created: 2026-05-29
updated: 2026-05-29
authors:
  - Hao Sun
  - Yuben Qu
  - Chao Dong
  - Haipeng Dai
  - Zhenhua Li
  - Lei Zhang
  - Qihui Wu
  - Song Guo
year: 2024
url: https://doi.org/10.1109/TMC.2024.3427420
venue: "IEEE Transactions on Mobile Computing (TMC)"
---

# All-Sky Autonomous Computing in UAV Swarm

## TL;DR
ASAP (All-Sky Autonomous comPuting) processes UAV sensory data entirely inside the swarm via [[collaborative-dl-inference]], rather than compressing models onboard (accuracy loss) or offloading raw data to a possibly-damaged ground station (high latency). It uses [[dnn-model-partition]] across UAV clusters, [[data-partition-parallel-inference]] within clusters, and [[pipeline-parallel-inference]] across clusters, balanced by a [[dl-inference-latency-prediction|latency predictor]] and kept robust by [[elastic-task-scheduling]]. On 24 airborne computers and 5 real quad-rotor UAVs it cuts computing latency by up to 92.66% vs data offloading and up to 98.50% vs state-of-the-art terrestrial collaborative computing while preserving accuracy.

## Problem
Emergency UAVs (earthquake search-and-rescue, forest-fire detection, mine exploration) generate large EO/IR/radar data, but airborne compute is scarce — a 720P frame through ResNet101 needs 14.47 GFLOPs (FP32) and 3.99 GB, while a Jetson Nano offers ~7.6 GFLOPS (FP32) and 4 GB. Onboard model compression can lose >10% accuracy; raw-data offloading is accurate but slow and depends on base stations that are often damaged. Even UAV-relayed backhaul is bandwidth-limited. ASAP's key observation is that relay UAVs are computationally idle during transmission, so the swarm's combined compute should process data in-flight to get both low latency and high accuracy — autonomously, with no central node, and resilient to node failures and changing link rates. This sits within [[mobile-edge-computing]] / [[multi-uav-assisted-mec]] for [[post-disaster-mec]] settings and is positioned against [[task-offloading]].

## System model
- Hierarchical UAV swarm organized into clusters; each cluster has a head and members; the task owner is a cluster head. No ground backhaul is assumed; only final results return to the ground.
- Both task UAVs and relay UAVs contribute compute; a [[heterogeneous-uav-fleet]] (Jetson Nano / TX2 / NX) gives differing per-node capability.
- Two-level split: model partitioned across clusters; per-layer feature map partitioned across members within a cluster; submodels run pipeline-parallel.
- Latency model: per-UAV l_i = D_i / C_i; cluster latency = max{l_i}; pipeline average latency = max over clusters — motivating latency-equalizing [[load-balancing-uav-mec]] (a [[makespan-minimization]] objective).
- Comms: WiFi (indoor testbed) / ad-hoc (real UAVs); inter-UAV rate smoothed with R = R_new·α + R_old·(1−α), α=0.2; SSDP-based discovery; 2 s "alive" heartbeats for failure detection.
- Assumptions: layer-granularity partitioning, TensorRT operator fusion matters, GPU accelerators present, single task flow; no formal channel/energy/optimization-program model.

## Method
- UAV-swarm-native architecture: [[dnn-model-partition]] across clusters + [[data-partition-parallel-inference]] within clusters, executed via [[pipeline-parallel-inference]], avoiding extra intra-cluster relays and the central-node requirement of prior data-partition systems ([[parallel-vs-serial-processing]] motivation).
- Elastic Efficient Scheduler (E2S): MRT (back-deduces minimal input range for a target output range), ICLB (intra-cluster data partition aligned to a target latency), ECLB (inter-cluster model partition equalizing per-cluster latency), and ES ([[elastic-task-scheduling]] that re-runs ECLB+ICLB online on node drop/recover).
- [[dl-inference-latency-prediction]]: operator-level prediction (config-pattern models for conv-like ops; FLOPs-linear for element-wise ops) plus a tiny latency-fusion fine-tuner (1 hidden layer, 16 neurons, Adam, 60 epochs, 6,000 TensorRT samples) that learns operator-fusion rules.
- [[adaptive-intermediate-data-compression]]: 8-bit quantization + gzip on intermediate features, with quantization scale chosen from the data-size/link-rate ratio before each transmission.
- Implementation: >4,000 lines of Python, open-sourced (github.com/snhao222/ASAP), with online custom padding for partitioned feature maps.

## Key findings
- Up to 92.66% lower computing latency vs data offloading; runs ResNet101/152 that cannot fit onboard (e.g., ResNet152 high-res: 2.32 s at 4 nodes → 1.32 s at 20 nodes, vs 5.75–14.36 s for offloading/Neurosurgeon).
- Up to 98.50% lower latency than MoDNN and 95.35% than DeepSlicing (11 computers); up to 96.84%/83.37% on 5 real UAVs; per-node compute/memory overhead down up to 90.56%/90.02%.
- Scaling saturates: ResNet152 latency −43.1% from 4→20 nodes, but too many nodes can rebound latency.
- Predictor accuracy beats a FLOPs baseline by 34.35% (Conv)/28.39% (Pool), ~95% on element-wise ops; block-level error −76.8% (pre-fine-tune) and a further −25.4% with the fine-tuner (FLOPs-based error up to 123.8%).
- Predictor speed: 12.3/28.0/13.7 ms vs nn-Meter's 292326.3/15530.9/9057.6 ms (82.0%–99.6% faster).
- E2S cuts average latency 2.8%–66.0% vs even scheduling; rescheduling after a cluster-head cutoff stays <1 s (989.30/415.58/616.05 ms).
- 8-bit quantization keeps ~32-bit accuracy at −75% data size; adaptive compressor cuts intermediate data 87.2%–92.7% with <0.15% accuracy reduction.

## Limitations
Hardware-validated but small scale (24 Jetson computers over WiFi; 5 quad-rotors over ad-hoc). Single task flow only; multi-flow handling is future work. Inference-only (no RL training; transformers only conceptual). No formal channel/energy/optimization model; gains shrink on non-GPU devices. Open: theoretically sufficient UAV count per task, and fault tolerance in volatile swarm networks.

## Relation to the corpus
ASAP is the corpus's clearest example of in-swarm [[collaborative-dl-inference]] and is the natural sibling of [[huang-2025-cmop-dispersed-computing]] (dispersed computation across aerial nodes). Its cluster/head hierarchy echoes [[nabi-2025-jour-hierarchical-aerial]], its [[heterogeneous-uav-fleet]] load balancing connects to [[zhang-2025-ssac-mgi-heterogeneous-uav]] and [[load-balancing-uav-mec]], and its [[elastic-task-scheduling]] on node failure parallels [[zhang-2025-mcma-task-migration]]. It is positioned against [[task-offloading]] approaches such as [[bao-2025-ddpg-video-offloading]], and shares the UAV-swarm resource setting of [[wang-2025-uav-swarm-stackelberg]], serving [[post-disaster-mec]] within the broader [[mobile-edge-computing]] / [[multi-uav-assisted-mec]] landscape. As one of only two hardware-validated sources in the corpus (with [[shao-2024-drl-antijamming-mec]]), it is an important reality check on the simulation-heavy literature.

## Raw artifacts
- `raw/sources/All-Sky_Autonomous_Computing_in_UAV_Swarm/full.md`
