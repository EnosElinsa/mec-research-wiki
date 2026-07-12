---
type: source
title: "Digital Twins for Low-Altitude UAV Networks–Cooperation and Learning"
authors: ["Longyu Zhou", "Supeng Leng", "Yuchen Liu", "Zehui Xiong", "Tony Q. S. Quek"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3626747"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, digital-twin, uav-delivery, graph-matching, multi-agent-q-learning, edge-computing, collision-avoidance]
related:
  - "[[terminal-edge-multiscale-digital-twin]]"
  - "[[digital-twin]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[graph-neural-network]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[multi-agent-q-learning]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[tony-q-s-quek]]"
  - "[[zehui-xiong]]"
created: 2026-07-13
updated: 2026-07-13
---

# Digital Twins for Low-Altitude UAV Networks–Cooperation and Learning

## Citation

Zhou, L., Leng, S., Liu, Y., Xiong, Z., & Quek, T. Q. S. (2026). *Digital Twins for Low-Altitude UAV Networks–Cooperation and Learning*. **IEEE Transactions on Mobile Computing**, 25(4), 4839-4856. DOI: 10.1109/TMC.2025.3626747.

## TL;DR

Splits large UAV-delivery digital twins across edge and terminal scales. Edge UAVs use graph matching to assign parcel clusters to UAV groups, while terminal UAVs use competitive and cooperative Q-learning for energy-aware association, path planning, heavy-parcel cooperation, and collision avoidance.

## Problem

Centralized delivery twins become expensive and slow when parcel destinations, payloads, UAV energy, and topology change. A single large model must simultaneously assign missions and compute detailed collision-safe paths, while terminal UAVs have limited onboard resources. The paper separates strategic group assignment from local execution and exchanges decisions between the two scales.

## System model

- Warehouses send parcel missions through a data center to edge UAVs that manage groups of terminal UAVs.
- Parcel state includes latency, distance, weight, path position, and destination; UAV state includes position, velocity, posture, usable energy, and communication associations.
- Edge UAVs build group graphs, predict member positions, and trigger topology sharing when parcel count, latency, or related requirements change.
- Terminal UAVs use camera, IMU, ultrasonic, and lidar observations plus onboard computing to build local twins and send virtual decisions to physical controllers over CAN bus.
- Communication/resource models include sensing and transfer latency, Wi-Fi 6 beamformed UAV links, twin-construction latency and CPU energy, hover/cruise energy, payload effects, rate limits, and per-parcel energy budgets.

## Method

[[terminal-edge-multiscale-digital-twin]] begins with multimodal attention for macro-twin construction and lighter customized micro twins. The macro layer embeds UAV-group and parcel-cluster graphs, propagates features within and across graphs, aggregates graph representations, and scores graph similarity to choose group-to-cluster associations.

At the terminal layer, competitive Q-learning uses each UAV's energy, estimated mission time, UAV/parcel features, and the macro cooperation decision. Its action contains UAV-parcel association, velocity, and position, and its reward measures average neighbor energy reduction. Cooperative Q-learning consumes the joint state/action and combines delivery-time reduction with competitive rewards to shorten paths and avoid overlap or collision. The evaluation describes centralized training and distributed execution across ten agents split between the competitive and cooperative roles.

## Key findings

- With 20 UAVs and 40 parcels, graph-matching accuracy reaches `85%`; after disturbing `50%` of associations, it remains `80%`.
- Macro-twin imitation error is reported near `0.2%`, while converged micro-twin error remains at or below the adopted `0.5%` target.
- Competitive and cooperative training stabilize after about 800 episodes; at convergence threshold `0.0003`, CCRL uses the fewest reported samples, `3.6 x 10^4`.
- Depending on the sweep, energy reductions over energy-efficient, reactive, and GA baselines range from `1.9%-9.6%`.
- Successful delivery reaches `90%` in the parcel-count sweep and `94%` at 16 kg average parcel weight; the latter is `11.6%`, `14.3%`, and `23.1%` above the three baselines.
- Against DroneUp and MavBench, the method reports up to `90%` success, gains of `13.5%`/`23.7%`, and latency reductions of `30.5%`/`45.2%`.

## Limitations / parse caveats

Validation uses Gazebo/ROS, an NVIDIA 4070 GPU for virtual-space construction, and UAV/parcel datasets rather than physical delivery flights. The scenario assumes capable edge UAVs, event-triggered topology-state sharing when delivery requirements change, lightweight model-parameter exchange, no more than 10% changed destinations, and an adopted twin-synchronization target rather than a universal guarantee. The parse conflicts between a two-minute latency requirement and a later statement that delivery stays below two seconds; the latter is excluded. A figure caption and prose also disagree on 50 versus 55 UAVs. Several resource equations and the cooperative reward are OCR-damaged, and one paragraph prints `RRCL` where the paper otherwise uses CCRL. Publication metadata is absent from the parse and was verified through the exact-title Crossref record.

## Relation to the corpus

The source extends [[digital-twin]] from state synchronization and network planning into scale-separated UAV delivery control. Unlike [[multi-digital-twin-network-optimization]], which assigns different simulation/optimization roles to multiple network twins, this architecture partitions one delivery problem between macro edge association and micro terminal control. It also links [[graph-neural-network|graph matching]], [[multi-agent-q-learning]], and [[uav-delivery-pickup-dropoff|UAV delivery]]. Co-author [[tony-q-s-quek]] is part of the corpus's recurring SUTD edge-networking cluster.

## Raw artifacts

- Parse: `raw/sources/Digital_Twins_for_Low-Altitude_UAV_Networks-Cooperation_and_Learning/Digital_Twins_for_Low-Altitude_UAV_Networks-Cooperation_and_Learning.md`
- Origin PDF: `raw/sources/Digital_Twins_for_Low-Altitude_UAV_Networks-Cooperation_and_Learning/Digital_Twins_for_Low-Altitude_UAV_Networks-Cooperation_and_Learning.pdf`
- Figures: `raw/sources/Digital_Twins_for_Low-Altitude_UAV_Networks-Cooperation_and_Learning/images/`
