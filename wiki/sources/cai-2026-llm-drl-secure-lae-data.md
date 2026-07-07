---
type: source
title: "Large Language Model-Enhanced Deep Reinforcement Learning for Secure Data Collection in Low-Altitude Economy Networking"
authors: ["Lingyi Cai", "Ruichen Zhang", "Jiacheng Wang", "Yu Zhang", "Miaoran Peng", "Tao Jiang", "Dusit Niyato", "Wei Ni", "Abbas Jamalipour", "Dong In Kim"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3665241"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, Jul. 2026"
tags: [source, low-altitude-economy, llm, deep-reinforcement-learning, physical-layer-security, uav-data-collection, age-of-information]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[generative-ai-for-mec]]"
  - "[[llm-assisted-resource-allocation]]"
  - "[[llm-assisted-mec-optimization-control-plane]]"
  - "[[llm-state-reward-secure-lae-data]]"
  - "[[prompt-engineering]]"
  - "[[td3]]"
  - "[[ddpg]]"
  - "[[age-of-information]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[uav-data-collection]]"
created: 2026-07-07
updated: 2026-07-07
---

# Large Language Model-Enhanced Deep Reinforcement Learning for Secure Data Collection in Low-Altitude Economy Networking

## Citation

Cai, L., Zhang, R., Wang, J., Zhang, Y., Peng, M., Jiang, T., Niyato, D., Ni, W., Jamalipour, A., & Kim, D. I. (2026). *Large Language Model-Enhanced Deep Reinforcement Learning for Secure Data Collection in Low-Altitude Economy Networking*. **IEEE Transactions on Mobile Computing**, 25(7), 10636-10650. DOI: 10.1109/TMC.2026.3665241.

## TL;DR

Uses an LLM to improve DRL-based secure data collection in a low-altitude economy network. A data-collection UAV and a jamming UAV coordinate data updates from edge devices under idle-channel sensing and eavesdropping risk. The LLM acts as a state processor, reward designer, and simulator; its generated state/reward pairs are pre-evaluated with Lipschitz feedback before DRL training with DDPG and TD3 backbones.

## Problem

Secure LAE data collection has competing objectives: keep information fresh, reduce UAV energy, and protect uplink updates from eavesdroppers. Manually engineered DRL state and reward designs can converge slowly or miss relevant physical/security structure. The paper asks whether LLM-guided state/reward/simulation design can make DRL controllers more effective for secure UAV data collection.

## System model

- The network contains edge devices, eavesdroppers, a primary data-collection UAV, and a jamming UAV.
- Devices update data through idle channels sensed by the UAV system.
- The controller balances AoI, UAV energy consumption, and secrecy constraints.
- Friendly jamming is used to suppress eavesdropping while the primary UAV collects updates.

## Method

The LLM is embedded into the DRL loop in three roles:

- State processor: helps structure the environment state for the DRL policy.
- Reward designer: generates reward formulations tied to freshness, security, and energy goals.
- Simulator: generates candidate state/reward pairs, which are filtered by a Lipschitz-feedback pre-evaluation step.

The paper evaluates the LLM-enhanced setup with both DDPG and TD3, comparing it to manually designed DRL baselines and partial LLM-ablation variants.

## Key findings

- The introduction reports about 35% faster convergence, 89% lower AoI, and 29% lower energy than the compared DRL baseline.
- The reported objective improvement is about 35% over the baseline.
- Across secrecy-threshold settings, the TD3+LLM variant reports AoI roughly 89%-85% lower than TD3 with manual design and 95%-93% lower than DDPG with manual design.
- Energy is reported about 15%-8% lower than TD3 with manual design and 33%-27% lower than DDPG with manual design across the same secrecy-threshold settings.
- At idle channel ratio 0.4, the parse reports about 88.02% AoI reduction versus manually designed TD3.
- Table III reports full-model objective values of 312.97, 353.35, and 525.81, outperforming reward-only and state-only LLM ablations.

## Limitations / future work

The authors name LLM computational overhead and prompt-engineering dependence as limitations. Future work targets lightweight LLMs and multi-agent AI frameworks. The evaluation is simulation-based.

## Relation to the corpus

This source expands [[generative-ai-for-mec]] from problem formulation and LLM-assisted scheduling into DRL state/reward/simulator design. It is security-oriented, linking [[low-altitude-intelligent-network]], [[physical-layer-security]], [[friendly-jamming-uav]], [[age-of-information]], and [[uav-data-collection]]. The reported state-reward improvement is summarized in [[llm-state-reward-secure-lae-data]], and the cross-source method role is captured by [[llm-assisted-mec-optimization-control-plane]]. It complements [[ji-2026-llm-iov-uav-offloading]], where the LLM handles runtime long-tail resource reallocation, and [[wen-2026-hybridrag-low-carbon-lae]], where LLM agents formulate a low-carbon optimization problem before a solver handles control.

## Raw artifacts

- `raw/sources/Large Language Model-Enhanced Deep Reinforcement Learning for Secure Data Collection in Low-Altitude Economy Networking/Large Language Model-Enhanced Deep Reinforcement Learning for Secure Data Collection in Low-Altitude Economy Networking.md`
- Original PDF and extracted figures (`images/`) in the same folder.
