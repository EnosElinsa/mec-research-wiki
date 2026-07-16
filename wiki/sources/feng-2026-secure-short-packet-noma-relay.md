---
type: source
title: "Secure Short-Packet Transmission of UAV Relaying via NOMA"
authors: ["Zhaoxin Feng", "Zhutian Yang", "Huabing Lu", "Chengwen Xing", "Nan Zhao", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3632873"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 7635-7648"
modeling_card: required
tags: [source, finite-blocklength, physical-layer-security, noma, uav-relay, artificial-noise, block-coordinate-descent, successive-convex-approximation]
related:
  - "[[weighted-effective-secrecy-rate]]"
  - "[[dual-phase-artificial-noise-uav-relaying]]"
  - "[[artificial-noise-aided-physical-layer-security]]"
  - "[[finite-blocklength-urllc]]"
  - "[[noma]]"
  - "[[physical-layer-security]]"
  - "[[uav-mobile-relaying]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[huabing-lu]]"
  - "[[chengwen-xing]]"
  - "[[dusit-niyato]]"
  - "[[li-2026-full-duplex-noma-uav-relay]]"
  - "[[zhu-2026-fas-uav-fbl]]"
  - "[[zhang-2026-irs-uav-covert-fbl]]"
created: 2026-07-14
updated: 2026-07-16
---

# Secure Short-Packet Transmission of UAV Relaying via NOMA

## Citation

Feng, Z., Yang, Z., Lu, H., Xing, C., Zhao, N., & Niyato, D. (2026). *Secure Short-Packet Transmission of UAV Relaying via NOMA*. **IEEE Transactions on Wireless Communications, 25**, 7635-7648. DOI: 10.1109/TWC.2025.3632873.

## TL;DR

Maximizes two users' [[weighted-effective-secrecy-rate]] in a half-duplex short-packet NOMA link relayed by a hovering UAV. Both the BS and relay inject spatially suppressed artificial noise, and a BCD/SCA method jointly selects blocklength, decoding-error targets, two-phase NOMA allocations, information/AN shares, and horizontal relay position; the result is a local stationary design under ideal CSI and SIC assumptions.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna BS sends confidential finite-blocklength packets to two users through a fixed-altitude decode-and-forward UAV relay because direct links are blocked. A passive eavesdropper combines observations from both half-duplex phases, while the BS and relay inject spatially suppressed artificial noise.

**Problem & objective**: Maximize weighted effective secrecy rate, $\max_{M,\mathbf R,\boldsymbol\alpha,\boldsymbol\phi,\mathbf q_R}\hat{\mathcal R}=\sum_{i=1}^{2}\omega_i\mathcal R_i$, over packet length, rates or error targets, NOMA shares, information-to-noise splits, and relay position.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Total blocklength | $M$ | positive integer | Symbols shared equally by the two relay phases |
| User secrecy rate or error target | $R_i$ or $\varepsilon_i$ | continuous | Finite-blocklength reliability and secrecy operating point |
| NOMA power shares | $\alpha_i,\hat\alpha_i$ | continuous, positive | Phase-I and phase-II user allocations |
| Information-power fractions | $\phi_{\mathrm I},\phi_{\mathrm{II}}$ | continuous, $(0,1)$ | Power retained for information rather than artificial noise |
| Relay horizontal position | $\mathbf q_R$ | continuous 2-D position | Hovering location of the UAV relay |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each user's secrecy block error probability is at most $\varepsilon_i^{\max}$. |
| C2 | Each user rate satisfies $R_i\geq R_i^{\min}$. |
| C3 | Blocklength satisfies $M\in\mathbb N^+$ and $M\leq BT_{\max}$. |
| C4 | NOMA shares sum to one in each phase and give the first user no less power than the second. |
| C5 | All NOMA shares are positive and $0<\phi_{\mathrm I},\phi_{\mathrm{II}}<1$. |
| C6 | Legitimate receivers apply the specified SIC order, and the eavesdropper is conservatively modeled with perfect SIC and two-phase combining. |

**Algorithm**: Replace rates by finite-blocklength decoding-error variables and exploit the monotonic benefit of the largest feasible blocklength. Apply block-coordinate descent: update error targets with a convex subproblem, then use SCA for phase-wise NOMA shares, information and artificial-noise fractions, and horizontal relay position until the weighted effective secrecy rate converges to a stationary design.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Feng et al. [x] optimized secure finite-blocklength NOMA transmission from a multi-antenna BS through a hovering decode-and-forward UAV to two users under a two-hop eavesdropper. They maximized weighted effective secrecy rate over integer blocklength, user rates or error targets, two-phase NOMA allocations, information-to-artificial-noise shares, and relay position under error, minimum-secrecy-rate, latency, allocation, and ordering constraints. Their BCD method fixes the maximal feasible blocklength and alternates a convex error update with SCA updates for power, artificial noise, and relay position. The reported design converged in about three outer iterations and moved the relay away from the eavesdropper while outperforming random-position and fixed-allocation baselines.

## Problem

A terrestrial BS must deliver confidential finite-blocklength packets to two remote trusted users through a UAV relay when direct links are blocked. A passive eavesdropper hears both hops and is conservatively allowed to combine them. The design must balance short-packet reliability, leakage, NOMA allocation, artificial-noise strength, and relay placement rather than optimizing a Shannon-rate relay alone.

## System model

- A multi-antenna BS communicates with two single-antenna users through one multi-antenna decode-and-forward UAV. One single-antenna ground eavesdropper overhears both phases.
- The relay is half-duplex and hovers at fixed altitude. Phase I is BS-to-relay and Phase II is relay-to-users; each uses `M/2` symbols, with total integer blocklength `M <= B T_max`.
- BS-relay and relay-user channels are Rician, BS-eavesdropper is Rayleigh, and relay-eavesdropper is Rician. Channels are quasi-static within a fading block and independent across blocks.
- Both phases use power-domain [[noma]] and SIC. The eavesdropper is assumed to perform perfect SIC and combines its two phase SINRs by addition.
- [[dual-phase-artificial-noise-uav-relaying]] uses fixed spatial constructions: Phase-I AN occupies the remaining right-singular-vector directions and is suppressed after the relay combiner (`v_b` is orthogonal to `H_SR V_2`), while Phase-II AN lies in the joint user-channel null space. The associated information beams are also fixed rather than jointly optimized.
- Legitimate end-to-end SINR is the weaker hop. Reliable and leakage rates use finite-blocklength normal approximations, including decoding-error and information-leakage penalties. Effective secrecy multiplies each secrecy rate by successful-decoding probability and weights the two users.

## Method

The original nonconvex problem optimizes integer blocklength, user transmission rates, per-phase NOMA powers, information-versus-AN shares, and the relay's horizontal position. Constraints impose user error and minimum secrecy-rate requirements, a latency/blocklength cap, normalized NOMA powers, and ordering that favors the weaker user. No explicit horizontal flight region, propulsion-energy budget, or placement bound appears in the displayed problem.

The reformulation replaces transmission rates with decoding-error variables. An outer block-coordinate method alternates four blocks:

1. The paper argues effective secrecy increases with blocklength and sets `M*=B T_max`; small-error concavity then permits a CVX error-probability subproblem.
2. Slack variables, difference-of-convex decompositions, and first-order lower bounds convexify the two-phase NOMA allocation block.
3. Analogous SCA bounds optimize the two information/AN power shares.
4. Distance-power auxiliaries and first-order approximations produce a convex relay-position update.

The objective sequence is claimed to be non-decreasing and bounded. The stated guarantee is convergence to a KKT/local solution under SCA regularity conditions, not global optimality.

## Key findings

- Exact default settings include four antennas at both BS and relay, `B=1 MHz`, `M=100`, leakage tolerance `10^-5`, BS/relay powers printed as `20/10 dB`, relay altitude `100 m`, and user weights `(0.6,0.4)`.
- **Figure-read approximate:** for `M=100,200,300`, weighted effective secrecy stabilizes in about three outer iterations near `3.00`, `3.15`, and `3.12-3.16 bit/s/Hz`. This supports fast convergence for the shown initialization only.
- **Figure-read approximate:** at `M=100`, proposed/initial/random-position/fixed-allocation results are about `3.00/1.88/2.48/2.23 bit/s/Hz`; near `M=275`, they are about `3.20/2.03/2.68/2.40`.
- **Figure-read approximate:** loosening leakage tolerance from `10^-5` to `10^-1` at `M=100` raises optimized secrecy from about `3.00` to `3.08 bit/s/Hz`.
- **Figure-read approximate:** the optimized relay moves from `(0,500,100) m` to roughly `(125,515,100) m`, away from the eavesdropper and toward the second user.
- The tested altitude range is only `80-100 m`; its slight secrecy decrease does not establish a general monotone altitude law. Likewise, BS-power curves rise through about `20 dB` and then plateau or slightly decline because Phase II becomes the bottleneck.

## Limitations

The model has one fixed BS, one hovering relay, two trusted users, and one passive eavesdropper at a known location. It assumes known channels, ideal legitimate SIC, perfect eavesdropper SIC, and perfect AN nulling. It omits trajectory dynamics, collision and no-fly constraints, propulsion energy, CSI acquisition error, direct BS-user links, queueing, processing delay, and relay decoding delay. Validation is simulation-only, and sensitivity to initialization, random realizations, runtime, and confidence intervals is not reported.

The finite-blocklength dispersion approximation `V_b=1` assumes legitimate SINR above `5 dB`, but the optimization does not visibly enforce that condition. The integer constraint on `M` is also not reconciled with `M*=B T_max` when the product is non-integer.

Several paper-side inconsistencies must be preserved. Baseline 2 prints `alpha_1=0.8` and `alpha_2=0.9`, violating the stated sum-to-one constraint; the intended hatted variable or value cannot be inferred. Algorithm 1 uses an `OR` stopping condition and an inconsistent index. Fig. 9 varies BS power but its explanation refers to more power at the relay. Powers and noise are printed in `dB`, not unambiguously `dBm`, and multiple equations are damaged in the parse.

## Relation to the corpus

This source joins [[finite-blocklength-urllc]], [[noma]], and [[artificial-noise-aided-physical-layer-security]] in a static two-hop relay design. [[li-2026-full-duplex-noma-uav-relay]] is the closest NOMA UAV-relay comparator, but it emphasizes full-duplex operation and robust position uncertainty under an infinite-blocklength rate model. [[zhu-2026-fas-uav-fbl]] also studies half-duplex finite-blocklength UAV relaying, but uses a single-user fluid antenna and energy-efficiency objective. [[zhang-2026-irs-uav-covert-fbl]] addresses finite-blocklength confidentiality through covert communication, an IRS, and trajectory design rather than dual-phase relay-generated AN.

## Raw artifacts

- Parse: `raw/sources/Secure_Short-Packet_Transmission_of_UAV_Relaying_via_NOMA/Secure_Short-Packet_Transmission_of_UAV_Relaying_via_NOMA.md`
- Origin PDF: `raw/sources/Secure_Short-Packet_Transmission_of_UAV_Relaying_via_NOMA/Secure_Short-Packet_Transmission_of_UAV_Relaying_via_NOMA.pdf`
- Figures: `raw/sources/Secure_Short-Packet_Transmission_of_UAV_Relaying_via_NOMA/images/`

## Metadata notes

The article was accepted and published online in November 2025 and lists a current-version date of 22 December 2025. The journal header places it in volume 25 (2026), pages 7635-7648, so 2026 is the citation year. No issue number is printed in the supplied paper.
