---
type: source
title: "Data Center-Enabled High Altitude Platforms: A Green Computing Alternative"
authors: ["Wiem Abderrahim", "Osama Amin", "Basem Shihada"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3316204"
venue: "IEEE Transactions on Mobile Computing, 23(5)"
modeling_card: not_applicable
tags: [source, high-altitude-platform-station, data-center, green-computing, solar-energy-harvesting, computation-offloading]
related:
  - "[[high-altitude-platform-station]]"
  - "[[hap-solar-propulsion-energy-balance]]"
  - "[[task-offloading]]"
  - "[[basem-shihada]]"
created: 2026-11-02
updated: 2026-11-02
---

# Data Center-Enabled High Altitude Platforms: A Green Computing Alternative

## Citation

Abderrahim, W., Amin, O., & Shihada, B. (2024). *Data Center-Enabled High Altitude Platforms: A Green Computing Alternative*. **IEEE Transactions on Mobile Computing, 23**(5). DOI: 10.1109/TMC.2023.3316204.

## TL;DR

The paper places a flying data center on a HAP to support terrestrial data centers. An analytical study of cooling, solar harvesting, payload capacity, server utilization, and offloading links shows the HAP can save up to 14% of energy while avoiding the offloading outage and delay of distributed servers.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Abderrahim et al. [x] proposed a data center-enabled high altitude platform system in which a flying data center supports the operation of terrestrial data centers as a greener computing alternative. They conducted a detailed analytical study of the energy benefits and communication requirements of this approach, including solar energy harvesting, the low stratospheric temperature, payload capacity, and server utilization. The analysis shows that a data center-enabled HAP is more energy-efficient than a traditional terrestrial data center because of the naturally low temperature and the ability to harvest solar energy. Adopting such a HAP can save up to 14% of energy requirements while overcoming the offloading outage problem and the associated delay caused by server distribution. The study also finds that energy savings increase when the workload arrival rate to the HAP is reduced or the number of hosted servers is increased.

## Scope and method

Solar harvesting follows latitude- and day-dependent irradiance and daylight models. Cooling, server, and propulsion consumption are compared with a terrestrial data center. Payload and utilization limits determine the admissible workload arrival rate. The paper evaluates an architecture analytically and does not pose a decision, objective, and constraint model for optimization.

## Key findings

- Low stratospheric temperature and solar power make the HAP a favorable environment for servers.
- Energy savings reach about 14% and vary with workload, location, and season.
- Reliable links for retransmitting dropped workloads are needed to raise reliability and savings.

## Limitations / future work

The results depend on assumed payload limits, communication reliability, and the modeled workload process.

## Relation to the corpus

Extends [[high-altitude-platform-station]] from a communication relay to a computing host, and adds a data-center load to [[hap-solar-propulsion-energy-balance]].

## Raw artifacts

- Parse: `raw/sources/Data_Center-Enabled_High_Altitude_Platforms_A_Green_Computing_Alternative/Data_Center-Enabled_High_Altitude_Platforms_A_Green_Computing_Alternative.md`
- Origin PDF and extracted figures are in the same folder.
