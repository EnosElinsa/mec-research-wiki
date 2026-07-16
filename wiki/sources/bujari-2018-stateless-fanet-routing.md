---
type: source
title: "A Comparison of Stateless Position-based Packet Routing Algorithms for FANETs"
authors: ["Armir Bujari", "Claudio E. Palazzi", "Daniele Ronzani"]
year: 2018
url: "https://doi.org/10.1109/TMC.2018.2811490"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: not_applicable
tags: [source, fanet, routing, uav-communications, geographic-routing, packet-routing]
related:
  - "[[stateless-geographic-fanet-routing]]"
  - "[[uav-mobile-relaying]]"
  - "[[wireless-backhaul]]"
  - "[[zeng-2016-uav-comm-opportunities-challenges]]"
  - "[[fatemidokht-2021-vru-vanet-routing]]"
  - "[[uav-assisted-vanet-routing]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Comparison of Stateless Position-based Packet Routing Algorithms for FANETs

## Citation

Bujari, A., Palazzi, C. E., & Ronzani, D. (2018). *A Comparison of Stateless Position-based Packet Routing Algorithms for FANETs*. **IEEE Transactions on Mobile Computing**, 17(11), 2468-2482. DOI: 10.1109/TMC.2018.2811490.

## TL;DR

Compares stateless position-based packet routing protocols for 3-D flying ad hoc networks under a common simulation scenario. The paper organizes deterministic progress, randomized progress, face/projection, hybrid, and restricted-flooding strategies, then shows the delivery/path-dilation/scalability tradeoffs that arise when 2-D geographic-routing assumptions are moved into 3-D FANETs.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Bujari et al. [x] compared stateless position-based packet-routing algorithms for three-dimensional FANETs under a common simulation setup. They organized deterministic progress, randomized progress, face-based, hybrid, and restricted-flooding protocols and evaluated delivery rate, path dilation, traffic, and scalability in static 3-D topologies with 50 to 200 nodes. Their NS-2 experiments used IEEE 802.11g, free-space propagation, a 200 m transmission range, CBR traffic, and 512-byte packets. Results show that deterministic progress methods are highly scalable but vulnerable to local minima, PAB3D improves delivery in sparse cases, face methods trade higher delivery for long paths and traffic, and hybrid methods provide a stronger balance across network types.

## Problem

FANET nodes move in 3-D and change links quickly, making topology-based routing-table maintenance expensive and unreliable. Geographic routing is attractive because each forwarding decision can use positions without route state, but 3-D geometry weakens the planarization and face-routing assumptions that work in 2-D ad hoc networks.

## System model

- Evaluates static 3-D topologies with 50, 100, 150, and 200 nodes in a 1000 m by 1000 m by 1000 m area.
- Uses NS-2 2.35, IEEE 802.11g MAC, free-space propagation, 200 m transmission range, CBR traffic, and 512-byte packets.
- Metrics include delivery rate, path dilation, traffic, and scalability.
- Protocol families include Greedy, Compass, Most Forward, Ellipsoid, PAB3D, G-PAB3D-G, Projective Face, CFace(3), ALSP Face, GFG, PAB3D-CFace variants, LAR, and PAB3D-LAR.

## Method

- Builds a taxonomy for stateless 3-D position-based FANET routing.
- Compares protocols under a shared simulator setup rather than relying on heterogeneous prior evaluations.
- Separates delivery behavior by graph size, path length, TTL thresholds, and forwarding class.
- Summarizes each protocol family by delivery rate, path dilation, and scalability.

## Key findings

- Deterministic progress algorithms are highly scalable and have very low path dilation but low delivery when local minima appear.
- Randomized PAB3D improves delivery in sparse settings while keeping path dilation relatively low; in one 150-node worst case it reaches 80% delivery with path length at most three times the shortest path.
- Face-based algorithms can deliver more packets but often incur high path dilation and collision-prone traffic, especially when projection creates many crossing links.
- Hybrid methods such as GFG and PAB3D-CFace variants combine higher delivery, medium path dilation, and high scalability across broader network types.
- Protocols that rely on 2-D planarization are not efficient in 3-D environments because projected crossing links can drive unnecessary traffic.

## Limitations / future work

The comparison uses static topologies and a spherical/free-space-style communication abstraction. The paper identifies independent density/size studies, mobility effects, toroid-shaped antenna radiation patterns, and position-adjustment schemes as future work.

## Relation to the corpus

This is a networking foundation adjacent to MEC. The new [[stateless-geographic-fanet-routing]] concept complements [[uav-mobile-relaying]] and [[wireless-backhaul]] by focusing on packet forwarding among UAV nodes rather than compute offloading or relay trajectory optimization. The paper also anticipates the antenna-radiation realism that appears in [[huang-2026-aim-uav-relay-aor]].

## Raw artifacts

- `raw/sources/A_Comparison_of_Stateless_Position-based_Packet_Routing_Algorithms_for_FANETs/A_Comparison_of_Stateless_Position-based_Packet_Routing_Algorithms_for_FANETs.md`
- `raw/sources/A_Comparison_of_Stateless_Position-based_Packet_Routing_Algorithms_for_FANETs/A_Comparison_of_Stateless_Position-based_Packet_Routing_Algorithms_for_FANETs.pdf`
- Extracted figures in `raw/sources/A_Comparison_of_Stateless_Position-based_Packet_Routing_Algorithms_for_FANETs/images/`
