---
type: source
title: "RIS-Based Communication Enhancement and Location Privacy Protection in UAV Networks"
authors: ["Ziqi Chen", "Jun Du", "Chunxiao Jiang", "Tony Q. S. Quek", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3655342"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 11270-11285"
modeling_card: required
tags: [source, active-ris, location-privacy, artificial-noise, virtual-partition, uav-network, crlb]
related:
  - "[[virtual-partitioned-active-ris-location-privacy]]"
  - "[[active-ris]]"
  - "[[cramer-rao-bound]]"
  - "[[physical-layer-security]]"
  - "[[jun-du]]"
  - "[[chunxiao-jiang]]"
  - "[[tony-q-s-quek]]"
  - "[[zhu-han]]"
created: 2026-07-14
updated: 2026-07-16
---

# RIS-Based Communication Enhancement and Location Privacy Protection in UAV Networks

## Citation

Chen, Z., Du, J., Jiang, C., Quek, T. Q. S., & Han, Z. (2026). *RIS-Based Communication Enhancement and Location Privacy Protection in UAV Networks*. **IEEE Transactions on Wireless Communications, 25**, 11270-11285. DOI: 10.1109/TWC.2026.3655342.

## TL;DR

Adds an artificial-noise generator to an active RIS and virtually partitions its elements between legitimate-UAV communication and malicious-UAV RSS-localization interference, trading sum rate against source-location error.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna source UAV communicates with legitimate single-antenna receiver UAVs through an active RIS, while colluding malicious UAVs estimate the source location from RSS. The RIS partitions elements and power between communication enhancement (ARIS-CE) and localization interference (ARIS-LI), with artificial-noise generation.

**Problem & objective**: Problem $P_0$ maximizes $Q_1=\sum_{k=1}^{K}\log_2(1+\gamma_k)+\omega\sum_{e=1}^{E}\kappa_e$ over source beamforming, ARIS-CE and ARIS-LI precoders, artificial-noise vectors, partition ratios, and power ratios subject to legitimate-user SINR, malicious-user localization-interference or CRLB, source/RIS power, and partition constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Source beamforming | $\mathbf w_k$ | complex vector | Beam for legitimate receiver $k$ |
| ARIS-CE precoder | $\boldsymbol\Theta$ | diagonal complex matrix | Active reflection and amplification for communication |
| ARIS-LI precoder | $\boldsymbol\Theta_e$ | diagonal complex matrix | Reflection used to interfere with malicious UAV $e$ |
| Artificial noise | $\mathbf v_e$ | complex vector | Noise injected into the ARIS-LI branch |
| Element partition ratio | $\rho_0,\rho_e$ | nonnegative, sum to $1$ | Fractions assigned to ARIS-CE and each ARIS-LI branch |
| Power partition ratio | $\eta_0,\eta_e$ | nonnegative, sum to $1$ | Source power shares for CE and LI branches |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each malicious UAV meets the localization-interference requirement derived from the RSS Fisher information and CRLB. |
| C2 | Each legitimate receiver meets the SINR target: $\operatorname{SINR}_k\ge\gamma_{st}$. |
| C3 | Each malicious-UAV localization error metric satisfies $\varrho_e\ge\varrho_{st}$. |
| C4 | Source power is bounded: $\sum_k\lVert\mathbf w_k\rVert^2\le P_S^{\max}$. |
| C5 | ARIS-CE power is bounded by $P_0=\eta_0P_R^{\max}$. |
| C6 | ARIS-LI power for branch $e$ is bounded by $P_e=\eta_eP_R^{\max}$. |
| C7 | Element partitions sum to one: $\rho_0+\sum_e\rho_e=1$. |
| C8 | Power partitions sum to one: $\eta_0+\sum_e\eta_e=1$. |

**Algorithm**: Derive the RSS localization CRLB, initialize partition and power ratios from average-channel formulas, then alternate fractional-programming updates for auxiliary variables, source beamforming, and ARIS-CE reflection with FP and semidefinite-programming updates for each ARIS-LI branch until the objective change is small.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied active-RIS communication enhancement and source-location privacy in a UAV network with colluding malicious UAVs. They formulated a weighted sum-rate and localization-interference problem over source beamforming, ARIS partition ratios, reflection precoders, artificial-noise vectors, and power allocations under legitimate-user SINR, malicious-user interference or CRLB, source and RIS power, and partition constraints. Their solution first derives average-channel partition and power allocations, then alternates fractional-programming updates for communication beamforming with semidefinite-programming localization-interference precoding. Simulations reported a 37.65% increase in malicious-UAV localization RMSE with a 3.69% sum-rate reduction beyond 400 m compared with fixed partition and power.

## Problem and system model

A multi-antenna source UAV communicates with legitimate single-antenna receiver UAVs through an active RIS. Colluding malicious UAVs use received signal strength and their known locations to estimate the source position. The source, RIS, and legitimate receivers share location information; the quasi-static source is sufficiently distant for a plane-wave model.

Unlike designs requiring the source to emit artificial noise, the RIS contains its own controllable phase, reflection amplifier, noise generator, and power supply.

## Method

[[virtual-partitioned-active-ris-location-privacy]] divides elements and power between ARIS-CE for communication and one ARIS-LI partition per malicious UAV. An RSS Fisher-information derivation supplies the localization CRLB. Closed-form average-channel allocation chooses partition sizes and power; fractional-programming alternating optimization updates source beamforming and ARIS-CE precoding, while FP and semidefinite programming update ARIS-LI precoding and artificial-noise factors.

## Key findings

- Beyond 400 m malicious-UAV distance, adaptive partitioning raises localization RMSE by 37.65% while reducing legitimate sum rate by 3.69% relative to fixed partition/power.
- Relative to an unpartitioned baseline, the same case gives 4.41 times larger localization error at 9.96% lower sum rate.
- At 200 m, localization RMSE rises 148.53% while sum rate falls 21.21% relative to fixed partitioning.
- With 200 RIS elements, adaptive partitioning increases localization RMSE by 138.64% relative to fixed partitioning. With 14 malicious UAVs, the proposed scheme increases RMSE by 258.16% at a 12.8% sum-rate cost; the comparison sentence does not explicitly identify its baseline.
- Increasing the privacy weight changes the partition until the communication constraint becomes active around weight 0.8 in the tested setup.

## Limitations

Evidence is analytical and simulation-only. The model assumes quasi-static geometry, shared legitimate locations, colluding malicious receivers, available channel feedback, ideal controllable active-RIS noise generation, and no mobility/trajectory dynamics. Closed-form partitioning relies on average-channel approximations and neglected small terms; alternating FP/SDP is computationally heavy and does not prove global optimality.

## Relation to the corpus

This source protects position rather than message secrecy: the adversary may receive signals but should estimate the source location poorly. It therefore complements [[physical-layer-security]] and is distinct from [[trajectory-privacy]], which constrains where a UAV route exposes sensitive areas.

## Raw artifacts

- Parse: `raw/sources/RIS-Based_Communication_Enhancement_and_Location_Privacy_Protection_in_UAV_Networks/RIS-Based_Communication_Enhancement_and_Location_Privacy_Protection_in_UAV_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
