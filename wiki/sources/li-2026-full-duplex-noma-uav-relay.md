---
type: source
title: "Robust Position and Power Optimization for Full-Duplex UAV Relay-Assisted Cellular Network Enhanced by NOMA"
authors: ["Huan Li", "Daosen Zhai", "Ruonan Zhang", "Lei Liu", "Dusit Niyato", "Yan Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3634617"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 7955-7969"
tags: [source, uav-relay, full-duplex, noma, chance-constraint, robust-optimization, power-allocation, deployment]
related:
  - "[[full-duplex-noma-uav-relay]]"
  - "[[bernstein-safe-approximation]]"
  - "[[uav-trajectory-safety-guarantee-ladder]]"
  - "[[robust-uav-position-power-optimization]]"
  - "[[noma]]"
  - "[[chance-constraint]]"
  - "[[uav-mobile-relaying]]"
  - "[[daosen-zhai]]"
  - "[[ruonan-zhang]]"
  - "[[dusit-niyato]]"
  - "[[wang-2026-diffusion-semantic-uav-edge]]"
created: 2026-07-14
updated: 2026-07-14
---

# Robust Position and Power Optimization for Full-Duplex UAV Relay-Assisted Cellular Network Enhanced by NOMA

## Citation

Li, H., Zhai, D., Zhang, R., Liu, L., Niyato, D., & Zhang, Y. (2026). *Robust Position and Power Optimization for Full-Duplex UAV Relay-Assisted Cellular Network Enhanced by NOMA*. **IEEE Transactions on Wireless Communications, 25**, 7955-7969. DOI: 10.1109/TWC.2025.3634617.

## TL;DR

Jointly places a full-duplex decode-and-forward UAV relay and allocates relay power under Gaussian position error, using Bernstein safe approximations and alternating SCA subproblems to enforce probabilistic user-rate and relay-ordering constraints.

## Problem and system model

One terrestrial base station serves cell-edge users through a rotary-wing [[full-duplex-noma-uav-relay]] whose expected 3-D position is optimized. The relay is periodically redeployed but remains fixed during each static solve. Aerial links use time-averaged free-space LoS gains, direct BS-user links use 3GPP urban-macro NLoS loss, and BS per-user powers are fixed.

The BS sends message D(t) to both relay and user. In the next slot, the UAV forwards D(t) while the BS sends D(t+1); the user applies SIC and maximal-ratio combining to direct and relayed observations. Perfect UAV self-interference cancellation and perfect SIC are assumed. The realized UAV position equals its expected position plus independent isotropic zero-mean Gaussian error.

The objective maximizes average user spectral efficiency over expected relay position and per-user UAV powers. Chance constraints require each user's rate and the relay-hop SINR ordering used to remove the decode-and-forward minimum to hold with prescribed probabilities, alongside position bounds and per-user and total relay-power limits.

## Method

[[bernstein-safe-approximation]] converts quadratic Gaussian [[chance-constraint|chance constraints]] into deterministic sufficient conditions. This guarantees feasibility for the requested probabilities but can be conservative. [[robust-uav-position-power-optimization]] then applies block coordinate descent: an SCA position block uses first-order rate lower bounds, and an SCA power block convexifies a quadratic-over-linear term. A feasible power program initializes the iterations from the user centroid at minimum altitude.

The paper proves a bounded, monotonically non-decreasing objective sequence for the alternating approximations. This is convergence of objective values, not global optimality of the original nonconvex chance-constrained problem.

## Key findings

- In the Fig. 3 scenario, direct BS service gives 4.8 bps/Hz against a 6 bps/Hz requirement. Both robust and non-robust joint designs make all users meet 6 bps/Hz; the robust design gives lower ideal/no-error rates because it reserves reliability margin. The 4.8 and 6 values are figure-derived and quoted in the text.
- At tolerance 0.01, Fig. 4 reports average inner iteration counts of 2.67 for position and 1.33 for power, three outer iterations, and about 8-16 seconds runtime. Tighter tolerances add iterations with negligible reported objective gain.
- For the four Fig. 5 combinations of 5 m or 10 m position error and outage target 0.1 or 0.01, the robust method meets the requested success probability. Its measured margins above target are about 5.44%, 0.20%, 4.67%, and 0.10%, indicating scenario-dependent conservatism; the non-robust design violates targets more often.
- In Fig. 6, both designs satisfy the relay-ordering chance constraint, which appears inactive under the tested parameters. This does not establish tightness for other settings.
- The qualitative Fig. 7 ordering is FD NOMA first, Bernstein-robust FD OMA second, worst-case FD OMA next, and half-duplex schemes lower as user count and relay power vary. The parse supplies no exact percentage gain for these curves.
- In Fig. 8, joint robust optimization ranks above variants without position optimization, without power allocation, or with initialization only. At higher user density, power appears to become the dominant bottleneck; this is a qualitative figure-derived interpretation.

## Limitations

The model assumes perfect self-interference cancellation and SIC, static users during each solve, known isotropic independent Gaussian position error, and time-averaged LoS aerial channels. It omits residual cancellation errors, small-scale fading, blockage, correlated or biased motion error, UAV trajectory dynamics, redeployment time and energy, and propulsion energy.

The Bernstein reformulation is sufficient but conservative, and one reported chance constraint is inactive. BCD/SCA yields a local solution to approximated subproblems rather than a globally optimal original design. The parse also contains sign and auxiliary-variable inconsistencies around the relay SINR difference and initialization mapping, so those equations require PDF checking before reuse. Validation is simulation-only; multi-UAV cooperation, mobility, and learning-assisted large-scale control remain future work.

## Relation to the corpus

This source combines [[noma]] and [[uav-mobile-relaying]] with probabilistic deployment robustness. It complements learning-based aerial optimization such as [[wang-2026-diffusion-semantic-uav-edge]] by using explicit Gaussian uncertainty and safe convex approximations rather than a learned control policy.

## Comparison boundary

Its Bernstein construction is a sufficient chance-constraint approximation for static relay rate and ordering under Gaussian position error. It does not establish moving-trajectory or collision safety; the comparison ladder keeps that protected-object boundary explicit in [[uav-trajectory-safety-guarantee-ladder]].

## Raw artifacts

- Parse: `raw/sources/Robust_Position_and_Power_Optimization_for_Full-Duplex_UAV_Relay-Assisted_Cellular_Network_Enhanced_by_NOMA/Robust_Position_and_Power_Optimization_for_Full-Duplex_UAV_Relay-Assisted_Cellular_Network_Enhanced_by_NOMA.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
