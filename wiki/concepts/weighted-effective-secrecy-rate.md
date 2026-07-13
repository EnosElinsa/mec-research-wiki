---
type: concept
title: "Weighted Effective Secrecy Rate"
tags: [physical-layer-security, finite-blocklength, short-packet, reliability, secrecy-rate]
related:
  - "[[feng-2026-secure-short-packet-noma-relay]]"
  - "[[finite-blocklength-urllc]]"
  - "[[physical-layer-security]]"
  - "[[noma]]"
  - "[[dual-phase-artificial-noise-uav-relaying]]"
created: 2026-07-14
updated: 2026-07-14
---

# Weighted Effective Secrecy Rate

Weighted effective secrecy rate aggregates users' confidential short-packet throughput while accounting for decoding failures. For user (i), the effective term is the finite-blocklength secrecy rate (R_i) multiplied by successful-decoding probability (1-\epsilon_i); user weights then form (sum_i \omega_i R_i(1-\epsilon_i)).

[[feng-2026-secure-short-packet-noma-relay]] uses this objective to couple blocklength, decoding-error targets, [[noma|NOMA]] power allocation, artificial-noise shares, and UAV relay placement. It therefore distinguishes nominal secrecy rate from confidential information expected to be decoded successfully.

This metric is not [[secrecy-energy-efficiency]] and does not include propulsion or transmit energy in its denominator. Its interpretation depends on the finite-blocklength normal approximation, the selected user weights and leakage tolerance, and the source's known-channel and ideal-SIC assumptions.
