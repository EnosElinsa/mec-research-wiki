---
type: source
title: "User-Centric Beam-Delay Alignment Transmission for Low-Altitude Coverage via Wideband Cell-Free Massive MIMO"
authors: ["Ziyao Hong", "Ting Li", "Shu Xu", "Chunguo Li", "Dongming Wang", "Xiaohu You"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3601587"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 3106-3120"
modeling_card: required
tags: [source, beam-delay-alignment, cell-free-massive-mimo, low-altitude-uav, asynchronous-downlink, wideband-beamforming, graph-neural-network, true-time-delay]
related:
  - "[[beam-delay-alignment-transmission]]"
  - "[[semi-synchronized-path-set]]"
  - "[[wideband-asynchronous-cell-free-massive-mimo]]"
  - "[[dual-purpose-time-delay-network]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[graph-neural-network]]"
  - "[[fang-2026-cellfree-uav-predictive-beamforming]]"
  - "[[wang-2026-6dara-cellfree]]"
  - "[[team-mmse-receive-combining]]"
  - "[[shi-2026-vhetnet-comp-coverage]]"
  - "[[aerial-terrestrial-cell-free-massive-mimo]]"
  - "[[mobility-asynchrony-and-geometry-in-aerial-coverage]]"
  - "[[chunguo-li]]"
  - "[[dongming-wang]]"
  - "[[xiaohu-you]]"
created: 2026-07-14
updated: 2026-07-16
---

# User-Centric Beam-Delay Alignment Transmission for Low-Altitude Coverage via Wideband Cell-Free Massive MIMO

## Citation

Hong, Z., Li, T., Xu, S., Li, C., Wang, D., & You, X. (2026). *User-Centric Beam-Delay Alignment Transmission for Low-Altitude Coverage via Wideband Cell-Free Massive MIMO*. **IEEE Transactions on Wireless Communications, 25**, 3106-3120. DOI: 10.1109/TWC.2025.3601587. (Published online 1 September 2025; current version 22 December 2025; final volume year 2026.)

## TL;DR

A wideband ground-AP cell-free downlink aligns selected UAV paths in both beam and delay. [[semi-synchronized-path-set|Semi-synchronized path sets]] exclude delay-incompatible combinations, a geometric-scattering GCN ranks clique candidates, and a [[dual-purpose-time-delay-network]] reuses beam-split delay modules before a fixed-structure max-min power-allocation stage.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Distributed millimeter-wave ground APs with hybrid precoding serve single-antenna UAVs over wideband multipath channels whose propagation-delay spread can exceed the cyclic prefix. Selected paths receive beam and time-delay alignment, and delay-compatible path groups suppress ICI, ISI, and asynchronous multiuser interference.

**Problem & objective**: Maximize worst-UAV received SNR or SINR, $\max_{\boldsymbol\alpha,\mathbf f,\boldsymbol\eta}\min_k\mathrm{SINR}_k$, by selecting AP-user paths, setting hybrid precoders and delay compensation, and allocating per-path power.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Path selection | $\alpha_{l,k,p}$ | binary | Whether AP $l$ serves UAV $k$ through path $p$ |
| Semi-synchronized path set | $\mathcal C_l$ | discrete clique subset | Delay-compatible paths selected at AP $l$ |
| Precoder | $\mathbf f_{l,k,p}$ | complex continuous | Beam that suppresses mismatched signals |
| Delay compensation | $\Delta_{l,k,p}$ | hardware-quantized delay | Alignment applied to the selected path |
| Per-path power | $\eta_{l,k,p}$ | continuous, nonnegative | Power allocated after precoder structure is fixed |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Precoding zero-forces selected intra-user and inter-user asynchronous terms outside the tolerated delay window. |
| C2 | Paths in each SSP-Set form a clique with pairwise mismatch $\lvert\nu\rvert\leq T_{\mathrm{CP}}/2$. |
| C3 | Per-AP selected streams do not exceed available RF chains and data-stream capacity. |
| C4 | Per-AP path powers satisfy $\sum_{k,p}\alpha_{l,k,p}\eta_{l,k,p}\leq P_{\mathrm{AP}}$. |
| C5 | Digital or analog delay settings remain implementable by the available delay modules and branch counts. |
| C6 | Path selection uses statistical path gain and delay information rather than unavailable instantaneous small-scale CSI. |

**Algorithm**: Build a path-compatibility graph at each AP, use a geometric-scattering GCN to rank maximal-clique candidates, and retain strong paths subject to RF-chain and delay-branch limits. Configure beam and delay alignment locally, derive zero-space precoders, upload aggregate gains to the CPU, and solve the fixed-structure max-min power allocation by feasibility bisection and a convex linear or fractional subproblem.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hong et al. [x] designed beam-delay alignment transmission for asynchronous wideband cell-free coverage of low-altitude UAV users. They maximized worst-user received SNR or SINR over delay-compatible path selection, hybrid precoding, time-delay compensation, and per-path power under zero-forcing, RF-chain, data-stream, delay-hardware, and per-AP power constraints. A geometric-scattering GCN ranks maximal-clique SSP candidates, distributed AP processing configures beams and delays, and centralized feasibility bisection allocates power. With 20 UAVs, max-min power allocation improved spectral efficiency by more than threefold over uniform power, and the gain remained about twofold in denser cases.

## Problem

In wide-area low-altitude coverage, propagation and multipath delays can exceed the cyclic-prefix tolerance. The resulting asynchronous phase shifts, inter-carrier interference, and inter-symbol interference undermine conventional cell-free designs that ignore propagation delay or assume synchronization. The paper asks how distributed millimeter-wave access points can serve UAVs with path-level delay alignment while respecting statistical CSI, RF-chain, data-stream, delay-module, per-AP power, and fronthaul constraints.

## System model

- `L` distributed ground APs jointly serve `K` single-antenna UAV users; UAVs are users rather than aerial access points or relays.
- Each AP has an `N`-element half-wavelength uniform linear array and fewer RF chains than antennas. The finite-path Saleh-Valenzuela channel contains at most `P` paths, with one LoS path and optional NLoS paths.
- The final design uses path departure angles, delays, and large-scale statistics rather than instantaneous small-scale channel coefficients. Delay mismatch outside the paper's half-CP tolerance can create modeled ICI and ISI.
- Hybrid precoding includes analog phase shifters and true-time-delay modules for wideband beam-split mitigation. Per-AP power, finite RF chains, finite data streams, and finite delay branches constrain the selected user paths.
- The objective is max-min received SNR/SINR across UAV users rather than sum-rate maximization.

## Method

[[beam-delay-alignment-transmission]] delays path `(l,k,p)` by the difference between that user's maximum path delay and the path's own delay, so selected components arrive at a common symbol reference. The ideal digital-delay derivation combines this timing rule with zero forcing, but it requires enough RF chains, instantaneous processing, and separate digital and analog delay resources that are unattractive for distributed cell-free deployment.

The final analog architecture instead forms an AP-local [[semi-synchronized-path-set]]: selected user paths must be pairwise compatible under the residual-delay criterion derived from the cyclic prefix. A [[dual-purpose-time-delay-network]] then reuses the analog modules needed for beam-split calibration to perform symbol synchronization. One RF-chain-modulated user signal can feed multiple selected path branches through a one-to-more selector.

For path selection, each AP maps user-path pairs to graph nodes and connects delay-compatible pairs. A geometric-scattering [[graph-neural-network]] refines node scores; a greedy routine starts from the highest-ranked nodes, constructs up to `kappa` maximal-clique candidates, and filters them by large-scale gain and hardware resources. This is a learned/greedy proposal mechanism, not exact maximum-clique optimization and not an end-to-end radio controller.

After SSP sets, equivalent gains, analog beams, and delays are fixed, the CPU solves max-min power allocation by bisection over a linear-feasibility problem. The paper's global-solution claim applies only to this conditioned power subproblem. It does not cover the preceding GCN/greedy path selection or the joint path, association, beam, delay, and power design.

APs estimate local path statistics, construct their SSP sets, and configure beams and delays; the CPU performs power allocation. The reported AP-side complexity is `O(K^2 N)` when `P`, `kappa`, and the delay-set count are treated as small, while CPU complexity is `O(-log(epsilon) L^3 K^3)`.

## Key findings

- Simulations use an area of `1 km x 1 km`, 18 APs with 128 antennas each, 20/30/40 UAV users, at most three paths, 10 RF chains per AP, 20 delay sets, 16 delay modules per set, and a `2.34 microsecond` cyclic prefix.
- In the tested CDFs, max-min power allocation gives more than a threefold improvement for 20 users and about a twofold improvement in the ultra-dense setting over uniform power. These are scenario- and distribution-dependent statements, not universal rate multipliers.
- Spectral efficiency increases with the tested antenna counts from 32 to 256. Optimized allocation also yields higher modeled energy efficiency and lower transmit power, but the paper does not state an exact percentage in its prose.
- The reused-delay architecture outperforms a design that combines BDAT with a separate beam-split delay network in the tested spectral-efficiency CDFs; the authors attribute this to retained multipath cross-term gains and avoided digital delay modules.
- With `kappa=20`, the GCN-assisted routine empirically finds the optimal maximal clique in the simulated graphs when compared with Bron-Kerbosch enumeration. This is an experimental result, not a maximum-clique guarantee.

## Limitations

Evaluation is analytical and simulation-only, with no hardware prototype, over-the-air synchronization test, UAV flight experiment, or measured urban channel. The design assumes available path angles, delays, and large-scale statistics; imperfect departure-angle and delay acquisition, joint precoding and power allocation, and richer mobility effects are left unresolved.

The hardware model does not quantify component power, insertion loss, delay or phase quantization, calibration error, or switching latency. The GCN description omits a complete dataset protocol, split, seed policy, and cross-topology generalization study. Its greedy clique construction has no global selection guarantee.

Fronthaul is reduced by local path-set and beam/delay construction, but it is not independent of scale: the reported upload expression is `L N_D^2 + L N_D + K`, including a user-count term. CPU power allocation also has cubic dependence on both AP and user counts under the stated complexity expression.

## Relation to the corpus

This paper places [[wideband-asynchronous-cell-free-massive-mimo]] within the [[low-altitude-intelligent-network]] track. It complements [[fang-2026-cellfree-uav-predictive-beamforming]]: both use distributed ground APs to serve UAVs, but Fang et al. predict mobility-driven LoS channels and reduce training overhead, whereas this work aligns asynchronous multipath components and reuses analog delay hardware. It also contrasts with [[aerial-terrestrial-cell-free-massive-mimo]], where UAVs act as access points serving ground users.

## Raw artifacts

- Parse: `raw/sources/User-Centric_Beam-Delay_Alignment_Transmission_for_Low-Altitude_Coverage_via_Wideband_Cell-Free_Massive_MIMO/User-Centric_Beam-Delay_Alignment_Transmission_for_Low-Altitude_Coverage_via_Wideband_Cell-Free_Massive_MIMO.md`
- Origin PDF: `raw/sources/User-Centric_Beam-Delay_Alignment_Transmission_for_Low-Altitude_Coverage_via_Wideband_Cell-Free_Massive_MIMO/User-Centric_Beam-Delay_Alignment_Transmission_for_Low-Altitude_Coverage_via_Wideband_Cell-Free_Massive_MIMO.pdf`
- Extracted figures: `raw/sources/User-Centric_Beam-Delay_Alignment_Transmission_for_Low-Altitude_Coverage_via_Wideband_Cell-Free_Massive_MIMO/images/`
