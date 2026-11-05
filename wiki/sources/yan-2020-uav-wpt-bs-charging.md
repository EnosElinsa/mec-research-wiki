---
type: source
title: "UAV-Enabled Wireless Power Transfer With Base Station Charging and UAV Power Consumption"
authors: ["Hua Yan", "Yunfei Chen", "Shuang-Hua Yang"]
year: 2020
url: "https://doi.org/10.1109/TVT.2020.3015246"
venue: "IEEE Transactions on Vehicular Technology, 69(11)"
modeling_card: required
tags: [source, wireless-power-transfer, uav-charger, sensor-networks, uav-placement, rotary-wing-energy]
related:
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[multi-location-hovering]]"
  - "[[yan-2025-in-flight-uav-charging-distance]]"
  - "[[hua-yan]]"
  - "[[yunfei-chen]]"
created: 2026-11-02
updated: 2026-11-03
---

# UAV-Enabled Wireless Power Transfer With Base Station Charging and UAV Power Consumption

## Citation

Yan, H., Chen, Y., & Yang, S.-H. (2020). *UAV-Enabled Wireless Power Transfer With Base Station Charging and UAV Power Consumption*. **IEEE Transactions on Vehicular Technology, 69**(11). DOI: 10.1109/TVT.2020.3015246.

## TL;DR

A rotary-wing UAV is first charged wirelessly by a base station, then flies to remote ground sensors and charges them by RF WPT. Including the BS loading stage, hovering and flight power, and RF-to-DC conversion loss, the paper finds the UAV location that maximizes the sum energy received by all sensors in 1D and 2D topologies under two charging schemes, and shows the optimum moves closer to the BS than in models that ignore these factors.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A BS near the UAV's start transmits power $P_t$; the UAV hovers above it for loading time $T_{loading}$, consuming $P(0)$ while harvesting. It then accelerates, flies at speed $V$, decelerates, and charges $K\ge2$ sensors in a 1D line or 2D field. Scheme 1 charges only while hovering above the sensors; Scheme 2 starts charging while approaching. Harvesting uses RF-to-DC efficiency $\eta$.

**Problem & objective**: Maximize the sum energy received by all sensors over the UAV hovering location, e.g. (20) $(x^*,0,H)=\arg\max_{x_h}E_{sum}^{1Ds1}(x_h,0,H)$ s.t. $E_{available}^{1Ds1}\ge0$, with analogues (41), (56), and (76) for 1D Scheme 2 and 2D Schemes 1 and 2.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV charging location | $x$ (1D) or $(x,y)$ (2D) | continuous, searched over candidate points | Where the UAV hovers to charge sensors |
| Charging start (Scheme 2) | $x_{start}$ | continuous, set by (22) | When charging begins during the approach |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (20b), (41b), (56b), (76b) | Energy left after loading, hovering, and flight is nonnegative: $E_{available}\ge0$ (1D/2D, Scheme 1/2; the parse labels (56b) with the 1D Scheme 2 symbol, so check the published paper) |
| Model rule | Loading at the BS is feasible only if the received DC power exceeds the hovering power: $\eta10^{P_{uav-r}/10}>P(0)$ |
| (21)–(22) | Scheme 2 starts charging once the received power at the first sensor reaches $P_\epsilon$ dB, which fixes the start point $x_{start}$ |
| Model rule | Flight has acceleration $a$, cruise at $V$, and deceleration; 2D splits velocity and acceleration by axis |

**Algorithm**: Algorithms 1 to 4 evaluate each candidate location: compute stored energy after loading and flight, check feasibility, accumulate the energy each sensor receives, and pick the location with the largest sum energy. The 2D algorithms decompose velocity and acceleration by axis.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yan et al. [x] studied the use of an unmanned aerial vehicle as a charger for wireless power transfer to battery-limited ground sensors. Unlike previous works, their model includes the power consumption of the UAV during hovering and flight, the charging process from a base station to the UAV, and the conversion loss of the energy harvester. Both one-dimensional and two-dimensional systems are considered, and two charging schemes are proposed in which the UAV charges sensors only while hovering above them or also while approaching them. The sum energy received by all sensors is maximized to find the optimal UAV deployment. Numerical results show that the sum energy depends on the sensor topology, the UAV flight speed, and the transmit power, and that the optimal UAV location is closer to the base station than in works that ignore the base station charging process and UAV power consumption; Scheme 2 is more energy efficient than Scheme 1 in both 1D and 2D.

## Problem framing

Earlier UAV-WPT studies assumed the UAV's energy was free and ignored how it was replenished. Counting both the BS-to-UAV charging and the UAV's own propulsion shifts the energy budget available to sensors.

## System model

- Defaults: BS power 35.68 dBW, BS gain 15 dBi, UAV and sensor gains 2 and 5 dBi, UAV transmit power 10 dBW, 915 MHz, $\eta=0.6$, $K=10$, and 600 s loading.
- Free-space RF propagation with altitude offsets between BS, UAV, and sensors.

## Method

Exhaustive one-dimensional or grid search over candidate positions using the closed-form energy expressions.

## Key findings

- Optimal UAV locations lie closer to the BS than those derived when BS charging or UAV consumption is ignored.
- Scheme 2 is more energy efficient than Scheme 1 in both 1D and 2D cases.
- Higher UAV speed and transmit power raise the sum energy.

## Limitations / future work

The model uses one UAV, one BS, and static sensors with a free-space link.

## Relation to the corpus

A charger-side counterpart to [[wireless-power-transfer]] and [[multi-location-hovering]] designs, by the same authors as the UAV-to-UAV link study [[yan-2025-in-flight-uav-charging-distance]].

## Raw artifacts

- Parse: `raw/sources/UAV-Enabled_Wireless_Power_Transfer_With_Base_Station_Charging_and_UAV_Power_Consumption/UAV-Enabled_Wireless_Power_Transfer_With_Base_Station_Charging_and_UAV_Power_Consumption.md`
- Origin PDF and extracted figures are in the same folder.
