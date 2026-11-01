---
type: source
title: "Optimum Distance for In-Flight UAV-to-UAV Wireless Charging"
authors: ["Hua Yan", "Yunfei Chen"]
year: 2025
url: "https://doi.org/10.1109/ACCESS.2025.3598733"
venue: "IEEE Access, 13"
modeling_card: required
tags: [source, uav-to-uav-wireless-charging, wireless-power-transfer, swipt, fresnel-zone, power-splitting]
related:
  - "[[in-flight-uav-energy-replenishment]]"
  - "[[wireless-power-transfer]]"
  - "[[simultaneous-wireless-information-and-power-transfer]]"
  - "[[near-field-communications]]"
  - "[[zhu-2022-aerial-refueling-uav-charging]]"
created: 2026-11-02
updated: 2026-11-02
---

# Optimum Distance for In-Flight UAV-to-UAV Wireless Charging

## Citation

Yan, H., & Chen, Y. (2025). *Optimum Distance for In-Flight UAV-to-UAV Wireless Charging*. **IEEE Access, 13**. DOI: 10.1109/ACCESS.2025.3598733.

## TL;DR

A discharging UAV (D-UAV) charges a charged UAV (C-UAV) by RF wireless power transfer while both also communicate. The paper finds the D-UAV to C-UAV distance that maximizes received energy under a minimum achievable rate, for an aligned scheme and a fly-by scheme, and shows the optimum lies in the Fresnel zone and grows with charging frequency.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: The D-UAV transmits RF energy with a directional aperture antenna of diameter $D_t$ and the C-UAV receives with an omnidirectional antenna of diameter $D_r$. The D-UAV has a fixed energy budget $E_0$ for charging and consumes propulsion power $P(v)$, so charging time obeys $T\le E_0/(P(v)+P_t)$. The C-UAV uses power splitting: a fraction $\rho$ of received power charges the battery and $1-\rho$ supports communications. Scheme 1 keeps the UAVs aligned; Scheme 2 lets them move relative to each other, crossing far-field and Fresnel-zone regions.

**Problem & objective**: P1 (Scheme 1): maximize received energy $E_{r-1}=\eta\rho P_r|h_1|^2T$ over the charging distance $d$, subject to the communications requirement on $C_1=T\log_2\left(1+\frac{(1-\rho)P_r|h_1|^2}{\delta_1^2}\right)$. Scheme 2 adds the relative movement speed.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Charging distance | $d$ | continuous, within the search range around the Fresnel zone | D-UAV to C-UAV separation |
| Power-splitting factor | $\rho$ | $0\le\rho\le1$ | Share of received power used for charging |
| Relative speed (Scheme 2) | $v$ | continuous | Relative motion during fly-by charging |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| Energy budget | $T\le E_0/(P(v)+P_t)$ at the D-UAV. |
| Rate requirement | $C_1$ must meet the minimum achievable rate $C_{\epsilon1}$. |
| Power split | $0\le\rho\le1$. |
| Fresnel zone | The search range spans $0.62\sqrt{D_t^3/\lambda}$ to $2D_t^2/\lambda$. |

**Algorithm**: Algorithm 1 computes wavelength, antenna gains, and charging time, sets a distance search range from the Fresnel-zone bounds, and runs a bisection-style search that compares $E_{r-1}$ at $SR_C\pm\epsilon$ to locate the maximizing distance. The optimal $\rho$ then follows from the rate requirement.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yan and Chen [x] studied the optimal distance for UAV-to-UAV in-flight wireless charging and communications. They proposed two schemes: in the first, the discharging UAV and the charged UAV are aligned and remain relatively stationary, and in the second, the two UAVs move during charging. For both schemes, they maximized the received energy at the charged UAV under the condition that the minimum achievable rate for communications is met, considering the energy limit of the discharging UAV, power splitting at the receiver, and alignment tolerance. Numerical results show that the optimal distance exists in the Fresnel zone and that it increases with the charging frequency. The results also show that the aligned scheme achieves higher received energy and rate, while the moving scheme offers more charging flexibility and is less affected by environmental fluctuations.

## Problem framing

Near the transmitter, beam collection efficiency is high but the transmit gain is not fully formed; far away, path loss dominates. The tradeoff creates an interior optimum distance.

## System model

- Defaults: $f=2.45$ GHz, $D_t=D_r=0.3$ m, $P_t=10$ W, RF-to-DC efficiency $\eta=0.5$, and noise powers 0.01.
- Rates are averaged over 10,000 channel realizations.
- D-UAV propulsion uses a rotary-wing energy model from prior work.

## Method

Closed-form energy and rate expressions are combined with a one-dimensional search inside the Fresnel-zone interval. Alignment tolerance due to turbulence is analyzed for Scheme 1.

## Key findings

- Received energy rises quickly with distance and then decays slowly, peaking inside the Fresnel zone.
- Received energy increases with $\rho$ for $\rho\in\{0.3,0.5,0.7\}$, which reduces the share for communications.
- An optimum combination of frequency and distance maximizes received power.

## Limitations / future work

The authors suggest THz charging with advanced antenna and path-loss models, beam-alignment methods for narrow beams under disturbance, and simultaneous charging of multiple UAVs by beam-splitting.

## Relation to the corpus

Provides link-level physics for [[in-flight-uav-energy-replenishment]], complementing the scheduling view in [[zhu-2022-aerial-refueling-uav-charging]], and extends [[simultaneous-wireless-information-and-power-transfer]] to the UAV-to-UAV Fresnel zone.

## Raw artifacts

- Parse: `raw/sources/Optimum_Distance_for_In-Flight_UAV-to-UAV_Wireless_Charging/Optimum_Distance_for_In-Flight_UAV-to-UAV_Wireless_Charging.md`
- Origin PDF and extracted figures are in the same folder.
