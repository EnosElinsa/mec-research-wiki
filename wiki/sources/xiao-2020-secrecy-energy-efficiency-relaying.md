---
type: source
title: "Secrecy Energy Efficiency Maximization for UAV-Enabled Mobile Relaying"
authors: ["Lin Xiao", "Yu Xu", "Dingcheng Yang", "Yong Zeng"]
year: 2020
url: "https://doi.org/10.1109/TGCN.2019.2949802"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), 4(1), 180-193"
modeling_card: required
tags: [source, secrecy-energy-efficiency, physical-layer-security, uav-mobile-relaying, fixed-wing-uav, trajectory-optimization, resource-allocation]
related:
  - "[[secrecy-energy-efficiency]]"
  - "[[physical-layer-security]]"
  - "[[uav-mobile-relaying]]"
  - "[[collect-store-forward-relaying]]"
  - "[[information-causality-constraint]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[xu-2021-secure-uav-mec-dual-uav]]"
  - "[[lin-xiao]]"
  - "[[yu-xu]]"
  - "[[dingcheng-yang]]"
  - "[[yong-zeng]]"
created: 2026-07-14
updated: 2026-07-16
---

# Secrecy Energy Efficiency Maximization for UAV-Enabled Mobile Relaying

## Citation

Xiao, L., Xu, Y., Yang, D., & Zeng, Y. (2020). *Secrecy Energy Efficiency Maximization for UAV-Enabled Mobile Relaying*. **IEEE Transactions on Green Communications and Networking, 4**(1), 180-193. DOI: 10.1109/TGCN.2019.2949802.

## TL;DR

Maximizes a fixed-wing relay UAV's confidential destination throughput per unit of propulsion energy by jointly optimizing receive/forward scheduling, source and relay powers, and the UAV trajectory. A block-alternating SCA/Dinkelbach method yields a monotonic, locally convergent suboptimal design; simulations show substantially higher secrecy energy efficiency than fixed flight-pattern and secrecy-throughput-maximizing baselines, including under disk-bounded eavesdropper-location uncertainty.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-wing UAV provides half-duplex delay-tolerant decode-and-forward relaying from a ground source to a destination in the presence of a passive eavesdropper, with the direct source-destination link blocked.

**Problem & objective**: Problem P1 maximizes secrecy bits per propulsion joule, $\max_{\lambda,\mathbf p_s,\mathbf p_r,\mathbf q,\mathbf v,\mathbf a}\frac{B\sum_n(r_{RD}[n]-r_{RE}[n])}{\sum_n[c_1\lVert\mathbf v[n]\rVert^3+\frac{c_2}{\lVert\mathbf v[n]\rVert}(1+\lVert\mathbf a[n]\rVert^2/g^2)]}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Receive-forward schedule | $\lambda[n]$ | Continuous, $[0,1]$ | Divide a slot between reception and forwarding |
| Source power | $p_s[n]$ | Continuous, nonnegative | Source transmission power |
| Relay power | $p_r[n]$ | Continuous, nonnegative | UAV forwarding power |
| Flight state | $\mathbf q[n],\mathbf v[n],\mathbf a[n]$ | Continuous vectors | UAV position, velocity, and acceleration |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Cumulative forwarded secrecy bits do not exceed previously received secrecy bits |
| C2 | Endpoints and discrete kinematics hold, including $\mathbf q[0]=\mathbf q_0$ and $\mathbf q[N]=\mathbf q_F$ |
| C3 | Flight limits hold, $\lVert\mathbf v[n]\rVert\leq V_{\max}$ and $\lVert\mathbf a[n]\rVert\leq a_{\max}$ |
| C4 | Average source and relay powers do not exceed $\bar P_s$ and $\bar P_r$ |
| C5 | Per-slot powers do not exceed $P_s^{\max}$ and $P_r^{\max}$ |

**Algorithm**: The solver alternates a convex scheduling block, an SCA power-allocation block, and an SCA trajectory block whose concave-over-convex surrogate is handled by Dinkelbach iterations; the outer objective is non-decreasing and converges to a suboptimal point.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xiao et al. [x] studied secrecy-energy-efficiency maximization for a fixed-wing UAV that buffers confidential data and relays it between a ground source and destination in the presence of an eavesdropper. They jointly optimized receive-forward scheduling, source and relay powers, and trajectory under secrecy information causality, flight dynamics, speed, acceleration, and power constraints. The proposed alternating method combines convex scheduling, successive convex approximation, and Dinkelbach fractional programming to obtain a monotonic suboptimal design. At a 200-second horizon, the reported design achieves 17.05 kbits/J, compared with 7.86 kbits/J for secrecy-capacity maximization and lower values for the fixed double-circular and running-track baselines.

## Problem

A mobile relay can exploit proximity to a source and destination to improve confidential delivery, but sharp or unnecessarily long maneuvers consume propulsion energy. The paper therefore optimizes [[secrecy-energy-efficiency]] (SEE), rather than secrecy throughput alone, over a prescribed mission horizon. The challenge is the coupling among half-duplex scheduling, two-hop secrecy rates, buffered information causality, transmit powers, and fixed-wing kinematics.

## System model

- One fixed-wing UAV acts as a half-duplex, TDD, delay-tolerant decode-and-forward relay between ground source `S` and destination `D`, in the presence of one passive ground eavesdropper `E`. The direct `S-D` link is assumed severely blocked.
- Under [[collect-store-forward-relaying]], the UAV receives near `S`, buffers confidential data, and forwards it near `D`. A one-slot processing delay imposes a cumulative [[information-causality-constraint|secrecy information-causality constraint]]: secret bits forwarded through slot `n` cannot exceed those received through slot `n-1`.
- The UAV flies at fixed altitude over `T = N delta_t`, with fixed endpoints, equal initial and final velocity, discrete position/velocity/acceleration dynamics, and maximum speed and acceleration.
- UAV-ground links use free-space LoS path loss. The ground source-eavesdropper link combines distance-dependent loss with unit-mean Rayleigh fading. Doppler is assumed perfectly compensated.
- `lambda[n] in [0,1]` allocates each slot between reception and forwarding. Source and relay powers obey average and peak constraints.
- The numerator is destination-hop secrecy throughput. The denominator is UAV propulsion energy from the [[fixed-wing-propulsion-energy-model]]; communication energy is excluded because propulsion is assumed dominant.
- The nominal model assumes global CSI and exact eavesdropper location. An extension places the eavesdropper in a known disk and substitutes worst-case source-eavesdropper and UAV-eavesdropper distances.

## Method

The paper alternates three variable blocks and claims a high-quality **suboptimal** solution, not a global optimum.

1. With powers and trajectory fixed, the scheduling block is a linear/convex program solved with CVX.
2. With scheduling and trajectory fixed, the power block introduces rate slacks and first-order upper bounds for eavesdropper-rate terms, yielding an SCA convex surrogate.
3. The trajectory/velocity block introduces distance, speed, and legitimate-rate slacks. First-order SCA bounds handle nonconvex rates, geometry, information causality, and inverse-speed terms; [[fractional-programming-dinkelbach|Dinkelbach's algorithm]] solves the remaining concave-over-convex ratio.

The outer block-alternating procedure updates scheduling, power, and trajectory until tolerance `epsilon`. Each block update is argued to be non-decreasing, and the finite objective gives convergence of the objective sequence. This does not establish global optimality or an initialization-independent solution. For uncertain eavesdropper location, the paper states that the same solver applies after worst-case distance substitution but omits the detailed reformulation.

## Key findings

- **Exact Table II values:** at `T = 100 s`, SEE is 15.86 kbits/J for the proposed design, 7.59 for secrecy-capacity maximization (SCM), 15.08 with uncertain eavesdropper location, 8.67 for double-circular flight (DCF), and 7.99 for running-track flight (RTF). At `T = 150 s`, the corresponding values are 16.88, 8.04, 15.87, 9.15, and 8.19 kbits/J. At `T = 200 s`, they are 17.05, 7.86, 16.09, 10.97, and 8.72 kbits/J.
- The highest clearly aligned proposed value in the parsed table is 17.05 kbits/J at `T = 200 s`. Later Table II rows lose alignment in the parse and are not treated here as exact results.
- The exact-location and 100 m uncertainty-disk designs differ modestly in the clear rows: at `T = 200 s`, 17.05 versus 16.09 kbits/J. Both remain above DCF and RTF in those rows.
- **Paper-stated trend from Fig. 6:** at `T = 200 s`, SEE initially rises with average source power and then saturates when relay forwarding power becomes the bottleneck. The prose does not give exact curve values.
- **Qualitative figure reading:** Figs. 5 and 7 show receive-first/forward-later operation. The optimized forwarding trajectory clusters near `D` while avoiding `E`; SCM exhibits sharp turns that the paper describes as energy-inefficient or physically infeasible for a fixed-wing UAV.
- **Qualitative figure reading:** Fig. 8 shows cumulative forwarded secrecy bits staying below buffered secrecy bits for `T = 150 s` and `250 s`, with equality reached during the final forwarding phase.
- The paper explains the rise and eventual decline of SEE with mission duration as a balance between approaching an energy-efficient speed and incurring repeated turning near `D` over longer horizons.

## Limitations / future work

The study is simulation-only and considers one source, one destination, one eavesdropper, one fixed-altitude fixed-wing UAV, and a prescribed mission duration. LoS UAV-ground channels, perfect Doppler compensation, global CSI, and sufficient endurance are strong assumptions. The eavesdropper is assumed unable to correlate or combine the two hop transmissions. The robust extension uses a conservative location disk and omits its detailed solver derivation.

Propulsion energy dominates the denominator, so communication and onboard processing energy are excluded. The AO/SCA/Dinkelbach method provides local monotonic convergence without a global-optimality bound and may depend on initialization. The paper identifies altitude/angle-dependent and probabilistic-LoS models as future extensions.

The formulation also contains defects that should not be silently repaired. Although `lambda[n]` is explicitly continuous in `[0,1]`, the paper calls the corresponding condition an integer constraint and labels the problem mixed-integer. The parse prints the eavesdropper coordinate as `[x_E,x_E]^T`, corrupts the altitude coordinate and several indices, and loses Table II row boundaries after `T = 200 s`; those later numerical entries require visual PDF verification before citation.

## Relation to the corpus

This paper combines the mobile-relay and information-causality structure of [[zeng-2016-throughput-relaying]] with the propulsion-aware trajectory design of [[zeng-2017-energy-efficient-uav-trajectory]], adding a passive eavesdropper and an SEE objective. [[xu-2021-secure-uav-mec-dual-uav]] shares authors [[yu-xu]] and [[dingcheng-yang]] and also couples security with UAV trajectory, but optimizes secure computation rather than two-hop relay SEE. Authors [[lin-xiao]], [[yu-xu]], [[dingcheng-yang]], and [[yong-zeng]] connect the source to the corpus's secure UAV, relaying, and energy-efficient trajectory lines.

Its uncertainty model is geometric: a location disk is reduced to worst-case link distances. This differs from bounded multi-link CSI uncertainty and LMI-based robust designs. Its kbits/J values also should not be compared directly with secrecy-rate or computation-efficiency objectives whose energy boundaries and protocols differ.

## Raw artifacts

- Parse: `raw/sources/Secrecy_Energy_Efficiency_Maximization_for_UAV-Enabled_Mobile_Relaying/Secrecy_Energy_Efficiency_Maximization_for_UAV-Enabled_Mobile_Relaying.md`
- Origin PDF: `raw/sources/Secrecy_Energy_Efficiency_Maximization_for_UAV-Enabled_Mobile_Relaying/Secrecy_Energy_Efficiency_Maximization_for_UAV-Enabled_Mobile_Relaying.pdf`
- Figures: `raw/sources/Secrecy_Energy_Efficiency_Maximization_for_UAV-Enabled_Mobile_Relaying/images/`
