---
type: source
title: "Towards Reliable Service Provisioning for Dynamic UAV Clusters in Low-Altitude Economy Networks"
authors: ["Yanwei Gong", "Ruichen Zhang", "Xiaoqing Wang", "Xiaolin Chang", "Bo Ai", "Junchao Fan", "Bocheng Ju", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3676757"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-16"
modeling_card: not_applicable
tags: [source, low-altitude-economy, uav-cluster, authentication, privacy-preservation, session-key-update, service-reliability]
related:
  - "[[uav-cluster-authentication]]"
  - "[[dynamic-uav-clustering]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[trajectory-privacy]]"
  - "[[privacy-sensitive-data-partitioning]]"
created: 2026-07-07
updated: 2026-07-16
---

# Towards Reliable Service Provisioning for Dynamic UAV Clusters in Low-Altitude Economy Networks

## Citation

Gong, Y., Zhang, R., Wang, X., Chang, X., Ai, B., Fan, J., Ju, B., & Niyato, D. (2026). *Towards Reliable Service Provisioning for Dynamic UAV Clusters in Low-Altitude Economy Networks*. **IEEE Transactions on Mobile Computing**, 1-16. DOI: 10.1109/TMC.2026.3676757. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Introduces LP2-CASKU, a lightweight privacy-preserving authentication and session-key-update scheme for dynamic UAV clusters. It batch-authenticates new UAVs, authenticates existing UAVs across clusters with anonymity/unlinkability, and updates cluster session keys for forward and backward secrecy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Gong et al. [x] studied reliable service provisioning for dynamic UAV clusters through lightweight privacy-preserving authentication and session-key updates. They proposed LP2-CASKU with setup, registration, join, cross-cluster, and cluster-session-key-update phases, including message aggregation for batch authentication, lightweight cross-cluster authentication, and forward- and backward-secure key updates. The scheme was analyzed for unforgeability, confidentiality, anonymity, unlinkability, and session-key secrecy under the stated Dolev-Yao threat model. Simulations report about 82.8% to 89.5% lower join latency than the no-aggregation baseline as new-UAV count increases from three to seven, together with lower cluster energy consumption.

## Problem

Low-altitude UAV services rely on clusters that must admit new UAVs and recruit existing UAVs from other clusters as demand changes. Reliability is threatened when authentication is too slow for dynamic swarms, when cross-cluster movement exposes UAV identity or movement patterns, or when cluster session keys do not preserve secrecy across joins and leaves.

## System model

The system includes GBSs, cluster heads, cluster members, new UAVs, and existing UAVs. Cluster heads coordinate task execution and manage a shared cluster session key; GBSs oversee multiple clusters, distribute instructions, and support registration/cross-cluster coordination. The threat model follows Dolev-Yao channel control and considers data eavesdropping, tampering, entity impersonation, identity inference, EUAV movement inference, and cluster-session-key inference; denial-of-service is out of scope.

## Method

LP2-CASKU has five phases: setup, registration, join, cross-cluster, and cluster session key update. Its three core mechanisms are:

- **MAm**, message aggregation for batch authentication of multiple NUAVs;
- **LC2Am**, lightweight cross-cluster authentication that uses single-sign-on style logic to authenticate EUAVs while preserving anonymity and unlinkability;
- **CSKUm**, cluster session key update to preserve forward secrecy when UAVs join and backward secrecy when UAVs leave.

The scheme uses ElGamal/hash-based primitives and is analyzed formally and illustratively for unforgeability, confidentiality, anonymity, unlinkability, and session-key secrecy.

## Key findings

- Compared with the no-aggregation baseline, MAm reduces join-phase latency by about 82.8%-89.5% as the number of NUAVs increases from 3 to 7.
- As the number of cluster members or cluster heads increases from 3 to 7, MAm keeps latency around 9.60-12.02 ms or 9.95-12.00 ms, while the no-aggregation baseline rises above 120 ms in the parse.
- Across 1-54 Mbps bitrates, MAm keeps latency low and achieves reductions above 88%; at 1 Mbps, the parse reports 59.72 ms with MAm versus 566.51 ms without it.
- Energy simulations show large reductions for CHs, CMs, and other CHs; the text reports about 37.6%-72.6% aggregate energy reduction and detailed reductions near 72% for the joined CH, nearly 60% for CMs, and over 62% for other CHs in specific scenarios.
- The authors provide a demonstration video/source-code link in the parse: `https://github.com/BJTU-STIC/UAV-simulation-demonstration`.

## Limitations / future work

The scheme assumes trusted GBSs for registration and cross-cluster coordination. The parse says a compromised GBS can affect identity issuance and token management, although established cluster session keys remain protected by forward/backward secrecy. DoS attacks are explicitly out of scope.

## Relation to the corpus

This source gives [[dynamic-uav-clustering]] a security layer through [[uav-cluster-authentication]]. It complements privacy/security pages such as [[trajectory-privacy]] and [[privacy-sensitive-data-partitioning]] by focusing on swarm-membership authentication, EUAV unlinkability, and session-key continuity rather than trajectory hiding or data partition placement.

## Raw artifacts

- `raw/sources/Towards Reliable Service Provisioning for Dynamic UAV Clusters in Low-Altitude Economy Networks/Towards Reliable Service Provisioning for Dynamic UAV Clusters in Low-Altitude Economy Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
