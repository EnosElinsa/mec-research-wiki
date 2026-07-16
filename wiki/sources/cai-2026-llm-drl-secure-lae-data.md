---
type: source
title: "Large Language Model-Enhanced Deep Reinforcement Learning for Secure Data Collection in Low-Altitude Economy Networking"
authors: ["Lingyi Cai", "Ruichen Zhang", "Jiacheng Wang", "Yu Zhang", "Miaoran Peng", "Tao Jiang", "Dusit Niyato", "Wei Ni", "Abbas Jamalipour", "Dong In Kim"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3665241"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, Jul. 2026"
modeling_card: required
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
updated: 2026-07-16
---

# Large Language Model-Enhanced Deep Reinforcement Learning for Secure Data Collection in Low-Altitude Economy Networking

## Citation

Cai, L., Zhang, R., Wang, J., Zhang, Y., Peng, M., Jiang, T., Niyato, D., Ni, W., Jamalipour, A., & Kim, D. I. (2026). *Large Language Model-Enhanced Deep Reinforcement Learning for Secure Data Collection in Low-Altitude Economy Networking*. **IEEE Transactions on Mobile Computing**, 25(7), 10636-10650. DOI: 10.1109/TMC.2026.3665241.

## TL;DR

Uses an LLM to improve DRL-based secure data collection in a low-altitude economy network. A data-collection UAV and a jamming UAV coordinate data updates from edge devices under idle-channel sensing and eavesdropping risk. The LLM acts as a state processor, reward designer, and simulator; its generated state/reward pairs are pre-evaluated with Lipschitz feedback before DRL training with DDPG and TD3 backbones.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A primary UAV collects periodic updates from fixed edge devices over sensed idle channels while a second UAV broadcasts artificial noise against passive eavesdroppers. Both UAVs move at a fixed altitude in a bounded low-altitude space; the channel model includes energy-detection spectrum sensing, Rayleigh fading, secrecy rate, mobility energy, and AoI dynamics.

**Problem & objective**: Problem (18) is a finite-horizon nonconvex mixed-integer program that minimizes $\sum_{t=1}^{T}[\alpha E^{(t)}+\beta\Delta^{(t)}]$ over UAV positions, device scheduling, and idle-channel selection.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV positions | $\mathbf p_u^{(t)}$ | continuous, $\mathbf p_u^{(t)}\in\mathcal P$ | Position of the primary or jamming UAV in slot $t$ |
| Device scheduling | $\Pi_i^{(t)}$ | binary, $\{0,1\}$ | Whether edge device $i$ is selected in slot $t$ |
| Channel selection | $z_c^{(t)}$ | binary, $\{0,1\}$ | Whether idle channel $c$ is selected in slot $t$ |
| UAV displacement actions | $\Delta\mathbf p_a^{(t)},\Delta\mathbf p_b^{(t)}$ | continuous, $[-v_{\max},v_{\max}]^2$ | Horizontal movement of the collection and jamming UAVs |
| Soft device and channel actions | $\mathbf u^{(t)},\mathbf v^{(t)}$ | continuous probability simplexes | Differentiable TD3 actions mapped by argmax to $\Pi_i^{(t)}$ and $z_c^{(t)}$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 18b | Both UAVs remain in the operating region, $\mathbf p_u^{(t)}\in\mathcal P$ |
| 18c-18d | Scheduling is binary and exactly one edge device is selected, $\Pi_i^{(t)}\in\{0,1\}$ and $\sum_i\Pi_i^{(t)}=1$ |
| 18e-18f | Channel selection is binary and exactly one channel is selected, $z_c^{(t)}\in\{0,1\}$ and $\sum_cz_c^{(t)}=1$ |
| 18g | Only an idle channel may be used, $z_c^{(t)}\leq1-s_c^{(t)}$ |
| 18h | A scheduled transmission meets the secrecy threshold, $R_{s,i,c}^{(t)}\geq R_{\min}\Pi_i^{(t)}z_c^{(t)}$ |

**Algorithm**: The LLM first produces task-aligned states and intrinsic rewards, then acts as a virtual LAENet simulator that filters candidate state-reward pairs using their Lipschitz constants. The selected design is deployed in a DDPG or TD3 loop with replay, twin critics for TD3, delayed actor updates, and soft target-network updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Cai et al. [x] studied secure and fresh data collection in a low-altitude economy network with a primary UAV, a cooperative jamming UAV, edge devices, primary users, and passive eavesdroppers. They formulated a finite-horizon mixed-integer problem that minimizes a weighted sum of UAV mobility energy and cumulative AoI by jointly controlling both UAV trajectories, one-device scheduling, and idle-channel selection under operational-space and minimum-secrecy-rate constraints. Their framework uses an LLM as a state processor, intrinsic-reward designer, and virtual simulator, ranks candidate state-reward designs through Lipschitz feedback, and then trains DDPG or TD3 policies. Numerical results report about 35% faster convergence, AoI reductions of up to 95%, and energy reductions of up to 33% relative to the evaluated DRL baselines.

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
