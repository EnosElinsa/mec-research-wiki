---
type: source
title: "Short-Packet NOMA Communication With Assistance of Active RIS and UAV: Analysis and Optimization"
authors: ["Le Thi Thanh Huyen", "Tran Manh Hoang", "Le The Dung", "Ba Cao Nguyen", "Xuan Nam Tran"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3628880"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 4, pp. 5364-5376"
modeling_card: required
tags: [source, active-ris, uav-mounted-ris, noma, finite-blocklength, imperfect-sic, block-error-rate, achievable-rate]
related:
  - "[[active-ris]]"
  - "[[uav-mounted-ris]]"
  - "[[finite-blocklength-urllc]]"
  - "[[noma]]"
  - "[[imperfect-sic-residual-interference]]"
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[feng-2026-secure-short-packet-noma-relay]]"
  - "[[xie-2023-wireless-powered-short-packet-uav]]"
  - "[[zhu-2026-fas-uav-fbl]]"
created: 2026-07-14
updated: 2026-07-16
---

# Short-Packet NOMA Communication With Assistance of Active RIS and UAV: Analysis and Optimization

## Citation

Huyen, L. T. T., Hoang, T. M., Dung, L. T., Nguyen, B. C., & Tran, X. N. (2026). *Short-Packet NOMA Communication With Assistance of Active RIS and UAV: Analysis and Optimization*. **IEEE Transactions on Mobile Computing, 25**(4), 5364-5376. DOI: 10.1109/TMC.2025.3628880.

## TL;DR

Analyzes a two-user downlink [[noma|NOMA]] link carried only through a UAV-mounted [[active-ris|active RIS]] under finite blocklength and imperfect SIC. Gamma-approximated cascaded channels yield BLER, asymptotic-diversity, and achievable-rate expressions; a one-dimensional golden-section search chooses the NOMA power split subject to the weak user's BLER constraint.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One base station serves two single-antenna ground users through an active RIS mounted on a UAV because the direct BS-user links are blocked. Downlink NOMA assigns more power to the weaker user, and the stronger user applies imperfect SIC. The finite-blocklength cascaded BS-RIS-user links comprise independent Rayleigh blocks and are approximated by a Gamma distribution; active elements add amplified thermal noise.

**Problem & objective**: Problem (P1) is a one-dimensional quasi-convex reliability optimization that minimizes the strong user's end-to-end block error rate, $\min_{a_1}\bar\epsilon_{D_1}$, subject to a block-error-rate requirement for the weak user.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Strong-user power coefficient | $a_1$ | continuous, $0\leq a_1\leq0.5$ | Fraction of BS power assigned to the stronger user |
| Weak-user power coefficient | $a_2=1-a_1$ | continuous, $0.5\leq a_2\leq1$ | Fraction of BS power assigned to the weaker user |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The weak user receives more power, $a_2>a_1$ |
| C2 | Power coefficients exhaust the budget, $a_1+a_2=1$ |
| C3 | The weak-user end-to-end BLER satisfies $\bar\epsilon_{D_2}\leq\bar\epsilon_{D_2}^{th}$ |
| C4 | The search domain for the independent variable is $0\leq a_1\leq0.5$ |

**Algorithm**: Approximate the coherent cascaded channel by a Gamma distribution, derive finite-blocklength BLER expressions with the piecewise-linear Q-function approximation, establish the power-allocation behavior, and apply golden-section search over $a_1$ until the interval width is below $10^{-3}$.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huyen et al. [x] studied short-packet downlink NOMA assisted by a UAV-mounted active RIS under imperfect successive interference cancellation. They derived exact and asymptotic block-error-rate expressions and average achievable-rate expressions using Gamma-approximated cascaded Rayleigh channels and a finite-blocklength normal approximation. The formal power-allocation problem minimizes the strong user's end-to-end block error rate subject to a weak-user reliability threshold and the NOMA power-sharing domain. A one-dimensional golden-section search obtains the power coefficient after the analytical expressions are evaluated. Monte Carlo simulations verify the analytical curves and report the effects of reflection-element count, blocklength, active gain, power allocation, UAV altitude, and imperfect SIC on reliability and achievable rate.

## Problem

A blocked BS-user path must support short-packet reliability through a UAV-mounted active surface. Active amplification can improve the cascaded link but also injects thermal noise, while NOMA introduces inter-user and residual-SIC interference. The paper studies these effects jointly and asks how the power split should protect the weak user while minimizing the strong user's end-to-end BLER.

## System model

- One BS serves two single-antenna ground users only through an `M`-element [[uav-mounted-ris|UAV-mounted active RIS]]; direct BS-user links are unavailable.
- The stronger user `D1` first decodes the weak user's signal and then its own. A fixed residual coefficient `0 <= xi <= 1` models [[imperfect-sic-residual-interference]]; the default is `xi=0.01`.
- The weaker user `D2` treats the strong user's signal as interference. Power coefficients satisfy `a2>a1` and `a1+a2=1`.
- Active elements apply coherent phases and a common gain `p>=1`, while adding RIS thermal noise. The corresponding passive surface is phase-only.
- BS-RIS and RIS-user small-scale channels are independent Rayleigh blocks, producing double-Rayleigh cascades. The squared coherent sum is approximated by a Gamma distribution before deriving BLER and rate expressions.
- The UAV follows a circular path at constant speed. The model assumes perfect CSI, continuous coherent phase alignment, perfect Doppler compensation, negligible wind, and locally static positions over short increments.

## Method

Finite-blocklength decoding error uses the normal approximation and a piecewise-linear approximation of the Gaussian Q-function. The strong user's end-to-end BLER sums its error when decoding the weak signal for SIC and its error when decoding its own signal; the weak user's BLER comes from decoding under NOMA interference. The paper derives average BLER expressions within the adopted Gamma and Q-function approximations, lower-complexity asymptotic forms, diversity behavior, and average achievable rate through Chebyshev-Gauss quadrature.

The formal optimization variable is `a1`, with `a2=1-a1`. It minimizes the strong user's end-to-end BLER subject to a weak-user BLER threshold and `0<=a1<=0.5`. A one-dimensional golden-section search uses tolerance `10^-3`. Element count, blocklength, active gain, altitude, SNR, and environment are sensitivity parameters, not jointly optimized variables. Although the paper discusses trajectory and optimal altitude, it formulates no trajectory optimizer and only sweeps altitude numerically.

## Key findings

- At `SNR=25 dB`, the paper reports a factor-`1000` BLER reduction when the active-element count increases from 2 to 4; exact and asymptotic curves closely match from `20 dB` upward.
- For `SNR=20 dB`, `B=256` bits, and `M=6`, the stated `10^-5` BLER target at `D1` requires `W=400` channel uses.
- The plotted power-allocation optimum is approximately `(a1,a2)=(0.3,0.7)` for the shown `M=6` and `M=8` cases.
- With `B=W=256`, plotted best altitudes are `105 m` for `M=4` and `110 m` for `M=8`; these are sweep results rather than outcomes of a trajectory or altitude optimizer.
- At `25 dB`, the reported achievable-rate gap between the two users is `22.8%`. Increasing `M` from 4 to 8 raises the shown sum-rate gap by `9.2%`, while increasing `W` from 256 to 512 changes achievable rate by only `1.1%` in the reported case.
- Increasing active gain from 1 to 6 initially raises rate, but the curves saturate beyond `p=3` as amplification also adds thermal noise.

## Limitations

The work is analytical and simulation-based, with no surface prototype, UAV flight experiment, measured channel, latency measurement, or hardware validation. It assumes one BS, one UAV surface, two fixed users, blocked direct links, perfect CSI and phase alignment, perfect Doppler compensation, and a circular path. Practical gain nonlinearities, phase quantization, coupling, control overhead, and a detailed UAV/RIS energy model are omitted. The formal optimizer selects only the NOMA power split. The analytical BLER is exact only after the Gamma channel approximation and Q-function linearization.

Several claims require caution. The paper's `290%` ARIS-versus-PRIS wording cannot be interpreted as a literal percentage reduction in BLER. Its reported diversity order of 6 at `M=8` conflicts with the stated ceiling formula when `k_hat` is approximately 1.6. The no-RIS/AF-relay baseline lacks a complete equal-budget definition, and the ARIS/PRIS equal-power construction is not fully itemized. The abstract's more-than-300-channel-use Shannon statement is supported in the body only as qualitative convergence toward Shannon rate.

## Relation to the corpus

This source combines [[active-ris]], [[uav-mounted-ris]], [[finite-blocklength-urllc]], [[noma]], and [[imperfect-sic-residual-interference]] in a closed-form reliability analysis. [[morshed-2026-active-ris-uav-noma-mappo]] studies the same active-RIS/UAV/NOMA intersection but learns decentralized movement, surface, and power controls under energy and fairness objectives. [[feng-2026-secure-short-packet-noma-relay]] instead uses a decode-forward UAV and artificial noise for finite-blocklength secrecy. [[zhu-2026-fas-uav-fbl]] provides an adjacent UAV short-packet BLER/diversity analysis based on fluid-antenna selection rather than an active surface.

## Raw artifacts

- Parse: `raw/sources/Short-Packet_NOMA_Communication_With_Assistance_of_Active_RIS_and_UAV_Analysis_and_Optimization/Short-Packet_NOMA_Communication_With_Assistance_of_Active_RIS_and_UAV_Analysis_and_Optimization.md`
- Origin PDF: `raw/sources/Short-Packet_NOMA_Communication_With_Assistance_of_Active_RIS_and_UAV_Analysis_and_Optimization/Short-Packet_NOMA_Communication_With_Assistance_of_Active_RIS_and_UAV_Analysis_and_Optimization.pdf`
- Figures: `raw/sources/Short-Packet_NOMA_Communication_With_Assistance_of_Active_RIS_and_UAV_Analysis_and_Optimization/images/`
