---
type: source
title: "Dual AAV Cluster-Assisted Maritime Physical-Layer Secure Communications via Collaborative Beamforming"
authors: ["Jiawei Huang", "Aimin Wang", "Geng Sun", "Jiahui Li", "Jiacheng Wang", "Hongyang Du", "Dusit Niyato"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2024.3521977"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
modeling_card: required
tags: [source, collaborative-beamforming, physical-layer-security, maritime-mec, multi-objective, friendly-jamming-uav, swarm-intelligence, energy-efficiency]
related:
  - "[[collaborative-beamforming]]"
  - "[[physical-layer-security]]"
  - "[[maritime-mec]]"
  - "[[friendly-jamming-uav]]"
  - "[[cooperative-jamming]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[salp-swarm-algorithm]]"
  - "[[secrecy-outage-probability]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[jiawei-huang]]"
  - "[[aimin-wang]]"
  - "[[sun-2024-imssa-uav-secure-cb]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
  - "[[li-2023-secure-marine-iot-jamming]]"
created: 2026-06-01
updated: 2026-07-16
---

# Dual AAV Cluster-Assisted Maritime Physical-Layer Secure Communications via Collaborative Beamforming

## Citation

Huang, J., Wang, A., Sun, G., Li, J., Wang, J., Du, H., & Niyato, D. (2025). *Dual AAV Cluster-Assisted Maritime Physical-Layer Secure Communications via Collaborative Beamforming*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2024.3521977. (Received 10 Oct 2024; revised 7 Dec 2024; accepted 19 Dec 2024; date of publication 23 Dec 2024; date of current version 25 Apr 2025. Presented in part at IEEE CSCWD 2023, DOI 10.1109/CSCWD57460.2023.10152552. Corresponding authors: Geng Sun, Jiahui Li.)

## TL;DR

Two clusters of **autonomous aerial vehicles (AAVs)** assist remote maritime communications using **collaborative beamforming (CB)**: one cluster forms a **maritime AAV-enabled virtual antenna array (MUVAA) relay** that forwards data to a legitimate vessel (Bob), and the other forms an **MUVAA jammer** that beams jamming toward a remote eavesdropper (Willie). The work formulates a **secure and energy-efficient maritime communication multi-objective optimization problem (SEMCMOP)** — maximize Bob's SINR, minimize Willie's SINR, and minimize total AAV flight energy — solved by an **improved multi-objective mayfly algorithm (IMOMA)** with chaotic solution initialization and hybrid solution-update strategies.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A shore-side base station sends data through a relay cluster of autonomous aerial vehicles to a legitimate vessel, while a separate aerial cluster emits collaborative friendly jamming toward a maritime eavesdropper. Each cluster acts as a virtual antenna array whose geometry and excitation weights jointly determine the legitimate and eavesdropping SINRs as well as fleet propulsion energy.

**Problem & objective**: The secure and energy-efficient maritime communication problem minimizes $\mathbf{F}=\{-f_1,f_2,f_3\}$, equivalently maximizing Bob's SINR $f_1$ while minimizing Willie's SINR $f_2$ and the total flight energy $f_3$ of the relay and jammer clusters.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Relay-cluster positions | $\mathbf{P}_r$ | continuous 3-D coordinates | Positions of relay AAVs forming the virtual array |
| Relay excitation weights | $\mathbf{I}_r$ | continuous, $[0,1]$ | Collaborative beamforming weights of relay AAVs |
| Jammer-cluster positions | $\mathbf{P}_j$ | continuous 3-D coordinates | Positions of friendly-jamming AAVs |
| Jammer excitation weights | $\mathbf{I}_j$ | continuous, $[0,1]$ | Collaborative jamming weights |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Relay and jammer excitation weights remain in $[0,1]$ |
| C2 | Every AAV remains inside its prescribed 3-D flight region |
| C3 | Any two AAVs in the same cluster maintain the collision-avoidance distance $D_{\min}$ |

**Algorithm**: IMOMA initializes a diverse Pareto population with a Tent chaotic map, then applies dimension-specific whale-inspired and arithmetic-optimization updates to the mayfly population. Non-dominated sorting and crowding-based archive management retain tradeoff solutions for legitimate SINR, eavesdropper SINR, and propulsion energy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] used separate autonomous-aerial-vehicle clusters as a collaborative relay array and a friendly-jamming array for remote maritime communication. Their three-objective model maximized Bob's SINR, minimized Willie's SINR, and minimized fleet flight energy over both clusters' 3-D positions and excitation weights under flight-region, weight-range, and collision-separation constraints. IMOMA combines Tent-map initialization with dimension-specific whale and arithmetic updates to generate Pareto tradeoffs. In the larger scenario, collaborative beamforming achieved Bob SINR 20.75 and Willie SINR -39.9, versus -2.26 and -4.17 without collaborative beamforming, while IMOMA had the best three reported objectives among the compared optimizers.

## Problem framing

The marine economy needs reliable maritime networks, but installing equipment at sea is hard and signal rates lag cellular networks. AAVs are flexible relay platforms, yet their high altitude implies long propagation distances and signal attenuation, and the open air channel invites eavesdropping. [[collaborative-beamforming|CB]] lets a cluster of AAVs act as a virtual antenna array (VAA) — $N_U$ elements yield up to $N_U^2$ gain — extending range without new hardware. Upper-layer encryption is too compute-heavy for energy-limited AAVs, so the paper uses [[physical-layer-security|PLS]] instead, adding a second AAV cluster as a **friendly jammer** ([[friendly-jamming-uav]]). Because beam patterns depend on AAVs' 3-D positions and excitation-current weights, and repositioning costs flight energy, transmission efficiency and AAV energy conflict — motivating a multi-objective formulation. The authors state this is the first work to treat dual-AAV-cluster maritime secure communication via CB.

## System model

- **Actors.** An MUVAA **relay** cluster (forwards data to the legitimate vessel Bob) and an MUVAA **jammer** cluster (beams jamming to the eavesdropping vessel Willie), over multipath-affected maritime channels.
- **Decision variables.** Each AAV's **3-D position** and **excitation-current weight** in both the relay and jammer VAAs — a large-scale variable set.
- **Objectives (SEMCMOP).** (1) maximize the **SINR of the legitimate vessel**; (2) minimize the **SINR of the eavesdropping vessel**; (3) minimize **total AAV flight energy consumption**. The problem is stated to be **NP-hard** and large-scale.

## Method

- **IMOMA** — an improved multi-objective **mayfly algorithm** (a swarm-intelligence evolutionary optimizer) with two tailored ingredients:
  1. **Chaotic solution initialization** to diversify the initial population.
  2. **Hybrid solution update strategies** that update solutions in different dimensions in a targeted manner.
- Produces a Pareto set trading off transmission efficiency, security, and energy; not a DRL method (related conceptually to the swarm-intelligence CB optimizers under [[salp-swarm-algorithm]] but using the mayfly metaheuristic).

## Key findings

- The **CB-based** approach achieves far better separation of legitimate vs eavesdropper SINR than **non-CB**, **single-CB**, and **multihop** baselines. In the larger-scale network (Fig. 5, parse), the CB-based scheme reaches Bob SINR ≈ **20.75** and Willie SINR ≈ **−39.9**, versus non-CB (Bob ≈ −2.26, Willie ≈ −4.17) and single-CB (Bob ≈ 10.18, Willie ≈ 8.31) — non-CB cannot close the long-distance link and single-CB fails to suppress the eavesdropper (verbatim figure table).
- IMOMA **outperforms comparison swarm-intelligence algorithms** (MODA, MALO, MOMVO, MOMA): in the single-CB objective table it attains the best Bob SINR (10.18), best Willie SINR (8.31), and **lowest AAV energy (64 370 J)** among the five (verbatim table). The abstract reports IMOMA improves the **security-related objective by up to 43.20%**.
- Convergence is confirmed via solution distribution, **IGD** (stabilizing after ~200 iterations), and **ACR** (→ 0) metrics (parse, Section VI).
- A discussion (Section VII) notes a master-node data-aggregation scheme cuts $(S\times N)$ receptions to $(S+N)$, and that the CB method saves **50%–90%** of the time versus multihop approaches with low (~10–20 s) overhead (the paper's discussion, citing ref. [73]).

## Limitations / future work

The parsed conclusion does not enumerate explicit limitations; the study is simulation-based. SINR/energy magnitudes are read from MinerU-parsed figures/tables and should be treated as indicative.

## Relation to the corpus

A **maritime + collaborative-beamforming + physical-layer-security** entry from the Jilin-University/NTU [[geng-sun]] cluster, sitting at the intersection of the [[maritime-mec]] track and the CB thread mapped in [[collaborative-beamforming-in-aerial-mec]]. Where [[sun-2024-imssa-uav-secure-cb]] secures CB against imperfect/unknown eavesdroppers with a **salp-swarm** optimizer and [[zhang-2024-gdmtd3-aerial-secure-cb]] uses a **diffusion-enhanced TD3** policy, this paper distinctively uses a **dual-cluster relay + jammer** architecture and a **mayfly** metaheuristic (IMOMA). Its friendly-jamming PLS framing also relates to the USV cooperative-jamming approach of [[li-2023-secure-marine-iot-jamming]]. Shares the Geng Sun / Jiahui Li / Jiacheng Wang / Hongyang Du / Dusit Niyato author cluster.

## Raw artifacts

- `raw/sources/Dual_AAV_Cluster-Assisted_Maritime_Physical-Layer_Secure_Communications_via_Collaborative_Beamforming/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
