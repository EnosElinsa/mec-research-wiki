---
type: source
title: "Reliable and Energy-Efficient Communications via Collaborative Beamforming for UAV Networks"
authors: ["Xiaoya Zheng", "Geng Sun", "Jiahui Li", "Shuang Liang", "Qingqing Wu", "Minghao Yin", "Dusit Niyato", "Victor C. M. Leung"]
year: 2024
url: "https://doi.org/10.1109/TWC.2024.3400523"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, collaborative-beamforming, virtual-antenna-array, multi-objective-optimization, gravitational-search-algorithm, energy-efficiency, physical-layer-security, post-disaster-mec]
related:
  - "[[collaborative-beamforming]]"
  - "[[gravitational-search-algorithm]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[uav-data-collection]]"
  - "[[uav-mobile-relaying]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[liang-2024-hmecmop-uav-cb]]"
  - "[[sun-2024-imssa-uav-secure-cb]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
  - "[[huang-2025-dual-aav-maritime-secure-cb]]"
  - "[[geng-sun]]"
  - "[[jiahui-li]]"
  - "[[shuang-liang]]"
modeling_card: required
created: 2026-06-01
updated: 2026-07-16
---

# Reliable and Energy-Efficient Communications via Collaborative Beamforming for UAV Networks

## Citation

Zheng, X., Sun, G., Li, J., Liang, S., Wu, Q., Yin, M., Niyato, D., & Leung, V. C. M. (2024). *Reliable and Energy-Efficient Communications via Collaborative Beamforming for UAV Networks*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2024.3400523. (Manuscript received 3 December 2023; accepted 3 May 2024; date of publication 21 May 2024; date of current version 11 October 2024 → year 2024. An earlier version appeared at IEEE ISCC 2022, DOI 10.1109/ISCC55528.2022.9912883.)

## TL;DR

For an **emergency communication** scenario, a UAV-based relay system harvests data from ground users and then forms **UAV-enabled virtual antenna arrays (UVAAs)** to transmit the collected data to several remote base stations (BSs) via **collaborative beamforming (CB)**. Because the UVAA sidelobes interfere with neighbouring **aerial users (AUs)** carrying out other missions, the paper formulates a **reliable and energy-efficient communication multi-objective optimization problem (RECMOP)** that jointly (1) maximizes the **minimum receiving SNR of the BSs**, (2) minimizes the **maximum average receiving SNR of the AUs**, and (3) minimizes the **propulsion power consumption** of all UAVs, over UAV locations and excitation current weights (ECWs). The problem is proven **NP-hard and non-convex** with mixed (continuous + discrete) variables; an **improved multi-objective gravitational search algorithm (IMOGSA)** with three tailored designs solves it.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV relay fleet gathers emergency data from ground users, forms a UVAA, and serves remote BSs sequentially through collaborative beamforming while limiting sidelobe interference to neighboring aerial users. The UVAA-to-BS air-to-ground links use probabilistic LoS/NLoS path loss, and UVAA-to-AU air-to-air links use LoS propagation; the service order replaces simultaneous multiple access.

**Problem & objective**: RECMOP in (17), an NP-hard non-convex mixed-variable Pareto problem, minimizes $F=\{-f_1,f_2,f_3\}$, where $f_1=\min_j\mathrm{SNR}_{u,j}$, $f_2=\max_j\frac{1}{N_{AU}}\sum_k\mathrm{SNR}_{u,k}^{j}$, and $f_3=\sum_i\sum_j E_{i,j}(T_{i,j})$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV coordinates | $\mathbb C^{\mathcal U}$ | Continuous 3D coordinates | Configure the UVAA geometry for each BS transmission |
| Excitation current weights | $\mathbb I^{\mathcal U}=\{I_i\}$ | Continuous, $I_i\in[0,1]$ | Set each UAV element's beamforming weight |
| BS service order | $\mathbb O$ | Discrete permutation in $\mathcal{SO}$ | Order in which the UVAA transmits to the BSs |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Excitation weights satisfy $0\le I_i\le1$ |
| C2-C3 | Horizontal coordinates satisfy $L_{\min}\le x_i^U,y_i^U\le L_{\max}$ |
| C4 | Altitude satisfies $H_{\min}\le z_i^U\le H_{\max}$ |
| C5 | UAV speed satisfies $V_{\min}\le v_i\le V_{\max}$ |
| C6 | The service sequence is a valid BS permutation: $\mathbb O\in\mathcal{SO}$ |
| C7 | Collision avoidance requires $D_{i_1,i_2}\ge D_{\min}$ for every UAV pair |

**Algorithm**: Generate the initial population with quasi-opposition-based learning $\rightarrow$ evaluate Pareto objectives $\rightarrow$ update continuous and discrete solution dimensions with IMOGSA $\rightarrow$ maintain a nondominated archive $\rightarrow$ apply archive crossover and mutation until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zheng et al. [x] studied reliable and energy-efficient collaborative beamforming for UAV relay networks in an emergency communication scenario. They formulated RECMOP to maximize the minimum receiving SNR of remote BSs, minimize the maximum average receiving SNR of neighboring aerial users, and minimize UAV propulsion power. The decision vector contains UAV three-dimensional locations, excitation current weights, and the order in which the UVAA serves the BSs. They proposed IMOGSA with quasi-opposition-based learning, a discrete solution update strategy, and archive optimization to obtain Pareto solutions. Simulations report that IMOGSA produces solution sets closer to the Pareto-front direction than the evaluated metaheuristics in both eight-UAV and sixteen-UAV networks, and additional tests examine damaged UAVs, position jitter, and phase synchronization error.

## Problem framing

When terrestrial infrastructure fails, UAVs are dispatched for emergency communications, but a single UAV cannot reach remote BSs due to limited onboard transmit power. CB lets several UAVs form a UVAA whose received power scales with the square of the array element count ($N^2$-fold gain), enabling long-distance transmission and shorter transmission time, while requiring only small ECW/placement adjustments (energy-efficient). The catch: the UVAA's **sidelobe levels (SLLs)** interfere with unselected/adjacent aerial users. Good UVAA design (UAV locations + ECWs) must simultaneously sharpen the mainlobe toward BSs, suppress sidelobes toward AUs, and limit flight/propulsion energy — three conflicting objectives.

## System model

- **Actors.** A set of rotary-wing UAVs ($\mathcal{U}$) harvest data from ground users in a monitor area, then transmit to $N_{BS}$ remote BSs via CB; $N_{AU}$ neighbouring AUs (detected via cameras/radars) may be interfered. BS and AU locations are fixed and known. 3D Cartesian coordinates throughout.
- **Array factor.** Standard UVAA array factor summing per-UAV excitation-weighted phase terms over 3D positions; antenna-array efficiency $\eta \in [0,1]$.
- **Channels.** UVAA→AU is **air-to-air (A2A)**, modeled LoS; UVAA→BS is **air-to-ground (A2G)** with a probabilistic LoS/NLoS path-loss model (sigmoid LoS probability vs elevation angle).
- **SNR.** Receiving SNR (dB) to BS and AU computed from transmit power, beam gain, path loss, and noise power.
- **Propulsion energy.** [[rotary-wing-propulsion-energy-model|Rotary-wing]] propulsion-power model (blade-profile + induced + parasite terms), extended to 3D flights with added kinetic + potential terms.
- **Decision variables.** Per-UAV 3D positions and ECWs (the BS communication context makes the problem a mixed continuous/discrete one).
- **Objectives.** (1) max-min BS SNR, (2) min-max average AU SNR, (3) min total propulsion power — a three-objective Pareto problem.

## Method

- **IMOGSA** — an improved multi-objective **[[gravitational-search-algorithm]]** chosen over DRL (no costly training) and convex optimization (no problem transformation / solution-space distortion), and over other meta-heuristics because GSA is less prone to local optima and simple to implement on UAVs.
- **Three tailored designs:** (1) **quasi-opposition based learning (QBL)** to raise initial-solution quality for the large-scale problem; (2) a **discrete solution update strategy** to handle the discrete dimensions; (3) an **archive optimization method** (NSGA-II-inspired crossover/mutation on archive solutions) to improve archived-solution quality.
- Complexity and convergence analyses are provided; the algorithm emits a Pareto archive.

## Key findings

- IMOGSA effectively solves RECMOP and **outperforms other benchmark schemes in both smaller- and larger-scale UAV networks** (stated; comparative magnitudes live in the simulation figures and are indicative).
- A multi-hop relay baseline can achieve higher BS SNR (last-hop UAV is close to the BS, low path loss), but the proposed CB approach is preferred overall once AU interference and propulsion energy are jointly weighed (Table III comparison, parse).
- Robustness analysis under "unexpected circumstances" (e.g. imperfect phase synchronization) shows the CB approach is mildly affected but **still completes data transmission**; increasing the phase-error parameter $\gamma$ raises minimum BS SNR and lowers maximum average AU SNR (Fig. 13, figure-derived, indicative).

## Limitations / future work

Simulation-based; BS/AU locations assumed fixed and known. Future work (stated): extend the CB approach to more UAV-assisted scenarios — post-disaster wireless communications, **UAV-to-satellite** communications, and UAV-enabled **covert** communications.

## Relation to the corpus

A **collaborative-beamforming / virtual-antenna-array** entry from the Jilin-University / NTU [[geng-sun]] group (with [[jiahui-li]] and [[shuang-liang]]), and the CB source whose distinguishing feature is the explicit **AU-interference (max-min sidelobe-driven) objective** alongside BS-SNR and propulsion energy. It is a methodological sibling of [[liang-2024-hmecmop-uav-cb]] (hovering-vs-motion energy via [[multi-verse-optimizer]]) and [[li-2024-emssa-uav-swarm-vaa]] / [[sun-2024-imssa-uav-secure-cb]] (salp-swarm MOPs), but is the only one solved with the [[gravitational-search-algorithm]] (grounding that concept). Its dual relay + CB framing also connects to the UAV mobile-relaying line ([[uav-mobile-relaying]]) anchored by [[zeng-2016-throughput-relaying]]. Belongs to the [[collaborative-beamforming-in-aerial-mec]] track map; a communication-layer (SNR/energy) design rather than compute offloading.

## Raw artifacts

- `raw/sources/Reliable_and_Energy-Efficient_Communications_via_Collaborative_Beamforming_for_UAV_Networks/Reliable_and_Energy-Efficient_Communications_via_Collaborative_Beamforming_for_UAV_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
