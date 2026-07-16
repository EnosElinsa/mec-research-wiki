---
type: source
title: "A Correlated Data-Driven Collaborative Beamforming Approach for Energy-Efficient IoT Data Transmission"
authors: ["Yangning Li", "Hui Kang", "Jiahui Li", "Geng Sun", "Zemin Sun", "Jiacheng Wang", "Changyuan Zhao", "Dusit Niyato"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3553288"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags:
  - source
  - collaborative-beamforming
  - iot
  - wireless-sensor-network
  - routing
  - drl
  - ppo
  - lstm
  - energy-efficiency
  - virtual-antenna-array
related:
  - "[[collaborative-beamforming]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[omrp-overlap-routing]]"
  - "[[softppo-lstm]]"
  - "[[hot-spot-problem-iot]]"
  - "[[first-order-radio-energy-model]]"
  - "[[ppo]]"
  - "[[soft-actor-critic]]"
  - "[[ddpg]]"
  - "[[hardware-validation-and-sim-to-real-in-mec]]"
  - "[[decomposition-beats-end-to-end-drl-in-mec]]"
  - "[[sun-2021-temcmop-uav-cb]]"
  - "[[sun-2024-imssa-uav-secure-cb]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
  - "[[geng-sun]]"
  - "[[jiahui-li]]"
  - "[[hui-kang]]"
  - "[[zemin-sun]]"
  - "[[jiacheng-wang]]"
  - "[[dusit-niyato]]"
created: 2026-06-03
updated: 2026-07-16
modeling_card: required
---

# A Correlated Data-Driven Collaborative Beamforming Approach for Energy-Efficient IoT Data Transmission

## Citation
Yangning Li, [[hui-kang|Hui Kang]], [[jiahui-li|Jiahui Li]], [[geng-sun|Geng Sun]], [[zemin-sun|Zemin Sun]], [[jiacheng-wang|Jiacheng Wang]], Changyuan Zhao, [[dusit-niyato|Dusit Niyato]], "A Correlated Data-Driven Collaborative Beamforming Approach for Energy-Efficient IoT Data Transmission," *IEEE Internet of Things Journal*, 2025. DOI: 10.1109/JIOT.2025.3553288. (Corresponding authors: Jiahui Li; Geng Sun. Jilin University + Nanyang Technological University.)

## TL;DR
For a remotely-deployed static ground IoT network that must upload sensed data to a far-off base station (BS), this paper jointly designs (1) [[omrp-overlap-routing|OMRP]], a hierarchical clustering routing protocol that uses geometric **sensing-area overlap** as a proxy for data redundancy to drive cluster-head election, fusion order, and relay choice; and (2) [[softppo-lstm|SoftPPO-LSTM]], a [[ppo]]-based DRL method that selects which IoT nodes form a [[collaborative-beamforming|collaborative-beamforming]] virtual antenna array for the long uplink. Per the reported simulations, OMRP improves network lifetime by 17% over benchmark routing protocols and SoftPPO-LSTM raises CB throughput by 8.3% over benchmark algorithms, while mitigating the [[hot-spot-problem-iot|hot-spot problem]].

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Static energy-limited IoT nodes aggregate correlated sensing data with overlap-based multihop routing, then upload a fused packet to a remote BS through collaborative beamforming.

**Problem & objective**: Jointly manage routing roles and CB excitation over repeated rounds to maximize network lifetime and remote-BS throughput, $\max_{\mathbb I}(f_1,f_2)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Directed-link role | $x_{ji}$ | discrete in $\{0,1,2\}$ | No link, forwarding, or forwarding with data fusion at node $i$ |
| Fusion overlap factor | $\alpha_{i,j}$ | continuous in $[0,1]$ | Fraction of data retained after fusing node $i$ and neighbor $j$ |
| CB excitation weight | $I_{t,k}$ | continuous in $[0,1]$ | Current weight assigned to beamforming node $k$ at round $t$ |
| CB node score | $\upsilon_i(t)$ | continuous in $[0,1]$ | Score used to select the top beamforming nodes |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Excitation weights remain bounded, $0\leq I_{t,k}\leq1$. |
| C2 | Each directed link role is discrete, $x_{ji}\in\{0,1,2\}$. |
| C3 | Fusion factors are bounded, $0\leq\alpha_{i,j}\leq1$. |
| C4 | Selected routing links satisfy the maximum distance $d_{ij}\leq d_{\max}$. |
| C5 | The network lifetime threshold proportion is valid, $0<p\leq1$, and the top $N_{\mathrm{CB}}$ scores form the beamforming array. |

**Algorithm**: Run OMRP for overlap-aware cluster-head election, fusion order, and relay selection, then use SoftPPO-LSTM with softmax scoring and an LSTM feature network to choose beamforming nodes and transmit to the remote BS.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] proposed a data-driven IoT communication framework that combines overlap-based multihop routing with collaborative beamforming. OMRP chooses cluster heads, fusion order, and direct or relay links from sensing-area overlap and residual network structure, while SoftPPO-LSTM scores candidate beamforming nodes to optimize long-term lifetime and throughput. The formulation constrains routing roles, fusion factors, excitation weights, link distance, and the top-node selection process. Simulations report about 17% longer network lifetime than benchmark routing protocols and 8.3% higher CB throughput than PPO, with a Raspberry Pi deployment supporting practical inference.

## Problem framing
As IoT networks scale, devices generate massive, spatially/temporally correlated (redundant) data, and energy management becomes hard. When the BS/sink is far outside the monitored region, traditional routing makes the nodes nearest the BS carry the heaviest relay load over the longest last-hop link — the **hot-spot problem** — and long-distance single-node transmission is energy-expensive. Collaborative beamforming (CB) lets multiple nodes form a virtual antenna array (VAA) so that, for an ideal CB of N nodes, received power scales by N² (equivalently, required transmit power drops by 1/N²), decoupling which nodes transmit from their geographic position. The paper argues prior work treats routing, data fusion, and CB separately, and proposes a single data-driven framework that links data-redundancy estimation to all of routing, fusion ordering, and CB node selection over the network's lifetime.

## System model
- **Topology:** a large homogeneous cluster of static, energy-limited IoT nodes (no external recharge); each has one omnidirectional antenna and basic fusion capability, a known location, and a circular monitoring area of radius r. Node i's neighbor list is Fᵢ = {j : dᵢⱼ < 2r}.
- **Per-round operation (six steps):** BS broadcasts a query naming the round's sink node → nodes rebroadcast to find neighbors → run the hierarchical routing protocol to fix topology + TDMA schedule → route and fuse data toward the sink (fusion at the receiver) → sink runs CB node selection and broadcasts data/strategy to chosen beamforming nodes → beamforming nodes perform CB to the remote BS.
- **CB / communication model:** array factor AF(φ,θ,I) = Σ Iₖ e^{jΨₖ} e^{j(2π/λ)dₖ(φ,θ)} with phase Ψₖ = −(2π/λ)dₖ(φ,θ); two-ray multipath fading model for the long IoT-to-BS link.
- **Energy model:** the first-order radio model ([[first-order-radio-energy-model]]) for inter-node links — free-space (d²) below a threshold and multipath (d⁴) above — plus a data-fusion energy cost.
- **Data correlation/fusion:** redundancy is modeled geometrically — fusion rate αᵢⱼ derives from the overlap area |Aᵢ ∩ Aⱼ| of two nodes' sensing areas, and the overlap degree ρᵢ = (1/Aᵢ) Σⱼ∈Fᵢ |Aᵢ ∩ Aⱼ| ∈ [0,1] summarizes how redundant/central a node is.

## Method
**OMRP ([[omrp-overlap-routing]])** extends LEACH in three stages:
1. *Setup* — compute overlap degree ρ; CH-election threshold T(i) is multiplied by Kρᵢ (K ≥ 1) so geographically central (high-ρ) nodes are more likely elected, shortening cluster-member transmission distances.
2. *Formation* — each CH sorts member JOIN_IN messages by ρ descending to set the intra-cluster TDMA order, so more-redundant (more-compressible) data is fused earlier and downstream packets shrink.
3. *Routing* — a distance factor βᵢⱼ = dᵢₛ² − dᵢⱼ² − dⱼₛ² decides relay vs. direct to the sink; relay is chosen when βmax > 2Eelec/εfs.

**SoftPPO-LSTM ([[softppo-lstm]])** reformulates the 2^N combinatorial CB-node-selection as a continuous N-dimensional scoring MDP: state = per-node {residual energy eᵢ(t), distance to sink dᵢₛ(t)}; action = a continuous score vector, with the top NCB scored nodes chosen as beamforming nodes; reward = ζ₁Cₜ − ζ₂ Σᵢ(eᵢ(t) − eᵢ(t+1)) (throughput minus total energy drain). Two modifications on top of [[ppo]]: a **softmax** applied to the actor's output scores (compresses score variance, smooths gradients, guides exploration), and an **LSTM** in the feature network (handles long episodes and adapts to the heuristic OMRP environment).

## Key findings
Reported on a simulation of 400 homogeneous IoT nodes randomly deployed in a 200 m × 200 m region with the remote BS 1000 m outside at (100 m, 1200 m); node transmit power 0.1 W, bandwidth 100 kHz, NCB = 10 nodes giving SNR ≈ 24 dB, initial energy 4.0 J (routing study) / 6.0 J (CB study).

- **Network lifetime:** OMRP improves lifetime ~17% over benchmark routing protocols (abstract). Per Table III, OMRP reaches FND/HND/AND of 271/624/870 rounds vs. LEACH 187/473/733, D2CRP 236/499/743, IGHND 229/573/742, PEGASIS 21/41/155.
- **Energy-consumption rate (FND–HND phase):** OMRP is ~6%, 12%, 20%, and 92% lower than IGHND, D2CRP, LEACH, and PEGASIS respectively (Table IV: OMRP 2.215 J/round vs. PEGASIS 30.501 J/round).
- **Data-perception maintenance (rounds to retain 75%/50%/25% perception, Table V):** OMRP 608/674/723 vs. IGHND 508/601/672, D2CRP 453/554/641, LEACH 427/524/627, PEGASIS 36/40/70.
- **CB throughput:** SoftPPO-LSTM transmits ≈ 1.37×10⁹ bits — an 8.3% increase over PPO, 10.9% over SAC, and 19.5% over DDPG. Ablation: LSTM contributes +6.5% and softmax +2.6% over plain PPO.
- **Scalability:** evaluated at 200/400/600/800 nodes; lifetime and throughput hold.
- **Robustness:** with Tikhonov-distributed phase errors (parameter κ), performance loss is negligible.
- **Hardware feasibility:** SoftPPO-LSTM deployed on a Raspberry Pi 4B (ARM Cortex-A72 1.5 GHz, 8 GB). Model parameters 16 MB (full environment 835 MB); inference 10.9 s cold, 2.2 s with the Python program preloaded, 0.02 s with the model preloaded; peak memory 324 MB.
- **Real-world layout:** revalidated on a 200 m × 200 m area with 588 IoT nodes extracted from the Santander SIoT-IoT-Dataset; OMRP and SoftPPO-LSTM keep their advantage over all benchmarks.

## Limitations / future work
- Homogeneous, static nodes only; the authors note heterogeneous/dynamic extensions and richer fault-tolerance (electromagnetic interference, hardware failure) as future work.
- DRL is trained on simulated data, which may not capture real-world variability; the LSTM's partial-observability benefit is informal (OMRP is a deterministic heuristic, not a true POMDP).
- For CB the excitation current weight is fixed at the maximum value of 1 (sidelobe/radiation-interference control deemed unnecessary in this scenario), which limits direct comparability with the UAV CB entries that optimize sidelobe levels.
- The Raspberry Pi study validates inference feasibility, not a full physical radio testbed.

## Relation to the corpus
This is the corpus's only [[collaborative-beamforming]] entry applying CB to **static ground IoT nodes** — every other CB source ([[sun-2021-temcmop-uav-cb]], [[sun-2024-imssa-uav-secure-cb]], [[li-2024-emssa-uav-swarm-vaa]], and the others mapped in [[collaborative-beamforming-in-aerial-mec]]) uses UAV/aerial or ground-terminal-to-satellite arrays with mobility. Its heuristic-routing-plus-DRL-selection structure reinforces [[decomposition-beats-end-to-end-drl-in-mec]]: a hand-designed routing stage feeds a learned selection stage rather than one end-to-end policy. The Raspberry Pi 4B deployment adds a concrete data point to [[hardware-validation-and-sim-to-real-in-mec]] (model size, latency, memory). On the DRL side, [[softppo-lstm]] is a minimal, on-policy alternative to the hybrid discrete/continuous action treatments ([[hybrid-action-representation]], [[j-ppo-vs-pdqn]]): it keeps everything inside [[ppo]] and only reshapes the action output with softmax. The paper shares the Jilin-University / NTU authorship cluster around [[geng-sun]], [[jiahui-li]], [[zemin-sun]], [[hui-kang]], [[jiacheng-wang]], and [[dusit-niyato]].

## Raw artifacts
- Parse: `raw/sources/A_Correlated_Data-Driven_Collaborative_Beamforming_Approach_for_Energy-Efficient_IoT_Data_Transmission/full.md`
- Origin PDF: `raw/sources/A_Correlated_Data-Driven_Collaborative_Beamforming_Approach_for_Energy-Efficient_IoT_Data_Transmission/93114a44-ffd7-4880-a027-6fee2041613f_origin.pdf`
- Figures: `raw/sources/A_Correlated_Data-Driven_Collaborative_Beamforming_Approach_for_Energy-Efficient_IoT_Data_Transmission/images/`
