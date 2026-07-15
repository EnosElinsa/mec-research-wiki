---
type: source
title: "Safe and Economical UAV Trajectory Planning in Low-Altitude Airspace A Hybrid DRL-LLM Algorithm With Compliance Awareness"
authors: ["Yanwei Gong", "Junchao Fan", "Ruichen Zhang", "Dusit Niyato", "Yingying Yao", "Xiaolin Chang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3668209"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, low-altitude-economy, uav-trajectory-control, safe-reinforcement-learning, soft-actor-critic, llm-assisted-control, compliance]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[compliance-aware-uav-trajectory]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
  - "[[uav-trajectory-control]]"
  - "[[safe-reinforcement-learning]]"
  - "[[soft-actor-critic]]"
  - "[[llm-assisted-resource-allocation]]"
  - "[[generative-ai-for-mec]]"
created: 2026-07-07
updated: 2026-07-14
---

# Safe and Economical UAV Trajectory Planning in Low-Altitude Airspace A Hybrid DRL-LLM Algorithm With Compliance Awareness

## Citation

Gong, Y., Fan, J., Zhang, R., Niyato, D., Yao, Y., & Chang, X. (2026). *Safe and Economical UAV Trajectory Planning in Low-Altitude Airspace A Hybrid DRL-LLM Algorithm With Compliance Awareness*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3668209. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Proposes a hybrid SAC-LLM trajectory planner for low-altitude data-collection UAVs. The POMDP includes obstacle avoidance, no-fly zones, residential-zone speed limits, landing, and energy constraints. During training, the LLM is invoked near obstacles to provide structured velocity guidance; after training, the LLM is removed and the lightweight SAC policy runs online.

## Problem

Low-altitude-economy UAVs must collect data while avoiding buildings, no-fly zones, other UAVs, and residential-zone speed restrictions. Standard DRL can learn from interaction but lacks explicit regulatory knowledge, while standalone LLM reasoning lacks real-time control efficiency. The paper targets safe, compliant, and economical trajectory planning under partial observability.

## System model

A data-collection UAV flies at fixed altitude from a takeoff area to a landing area, collecting data from ground equipment. It senses nearby obstacles within a perception radius, avoids building zones and other UAVs, must not enter no-fly zones, and must reduce speed in residential zones to satisfy noise-related compliance. The objective maximizes collected data subject to mobility, airspace, collision, landing, and energy constraints.

## Method

The trajectory task is formulated as a POMDP with a continuous velocity action. SAC provides the base control policy. When the sensed distance to a nearby obstacle or constrained region falls below a threshold, a prompt generator converts environment context, UAV status, and obstacle details into a chain-of-thought-style prompt. The LLM returns a strict JSON velocity vector, confidence score, and reasoning summary; an extractor retries invalid or over-speed actions up to 10 times and terminates the episode if valid control cannot be produced. The final online controller uses the trained SAC policy without LLM inference.

## Key findings

- The abstract reports data collection rate 99.50%, near-zero collision and regulation-violation rates, nearly 100% successful landing, and energy consumption rate 76.95%.
- Compared with the best baseline, the paper reports 2.9% higher data collection, near-zero collision and regulation violations, 100% successful landing, and 1.9% lower energy consumption.
- Under increasing other-UAV density, the proposed method keeps the highest data collection rate and the lowest collision and energy rates; SAC+LLM is reported to become unstable with collision rate exceeding 90% in that setting.
- Across increasing ground equipment, no-fly zones, building zones, and residential zones, the method maintains high data collection, low collision, and low regulation-violation rates in the reported figures.
- Sensitivity analysis identifies a 15 m LLM-invocation threshold as the best tradeoff; too small triggers the LLM too late, while too large increases energy through premature or frequent invocation.
- Prompt ablation shows that removing safety raises collision rate, removing compliance worsens regulation violation rate, removing data efficiency lowers data collection, and removing energy efficiency harms energy behavior and landing stability.

## Limitations / future work

The parse concludes that the method jointly considers obstacle avoidance, regulation awareness, and energy efficiency. Explicit future-work directions beyond that conclusion are not in parse.

## Relation to the corpus

This source extends [[low-altitude-intelligent-network]] and [[uav-trajectory-control]] with [[compliance-aware-uav-trajectory]]. It is related to [[cai-2026-llm-drl-secure-lae-data]] and [[wang-2026-llm-qos-multiuav-resource]] as another LLM-assisted control source, but its design is different: LLM reasoning is a training-time safety/compliance guide and is removed from the online loop.

## Comparison boundary

Its near-zero collision and regulation-violation rates are tested-simulator evidence. Because the LLM is removed online, the training-time guide is not a persistent shield like the intervention gate discussed in [[collision-avoidance-mgi]]; the distinction is summarized in [[uav-trajectory-safety-guarantee-ladder]].

## Raw artifacts

- `raw/sources/Safe_and_Economical_UAV_Trajectory_Planning_in_Low-Altitude_Airspace_A_Hybrid_DRL-LLM_Algorithm_With_Compliance_Awareness/Safe_and_Economical_UAV_Trajectory_Planning_in_Low-Altitude_Airspace_A_Hybrid_DRL-LLM_Algorithm_With_Compliance_Awareness.md`
- Original PDF and extracted figures (`images/`) in the same folder.
