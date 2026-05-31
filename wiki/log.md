# Research Log

Reverse-chronological activity log (newest first). Curation and audit passes are kept in full; the LLM-Wiki desktop app's automated raw-file deletion events are consolidated under [Raw-source housekeeping](#raw-source-housekeeping) at the foot of this file.

## 2026-06-01 — Audit pass (non-source layer — concept batch 10; no new papers)

Continues the non-source-layer audit into **concept batch 10** (20 pages, alphabetical rotary-wing-propulsion-energy-model → stochastic-game, positions 181–200 of `.curation-out/concept_slugs.txt`). Tree clean at `4797ddd`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 10)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded mechanism — recurring MGI overclaim):** [[safe-reinforcement-learning]] described the Markov Game of Intervention as a "game-theoretic intervention that asymmetrically assigns one UAV as the deflector when two UAVs threaten collision … avoids the symmetric-swerve failure mode" — **not in the [[zhang-2025-ssac-mgi-heterogeneous-uav]] parse**, the same inter-UAV-deflection mischaracterization already corrected on [[collision-avoidance-mgi]] (concept batch 2) and the source page (source batch 11). MGI is a **per-UAV** two-agent design: a stochastic reward-maximizing **Standard Agent** paired with a deterministic **Safety Agent** and a binary gating policy $\mathbf{g}(s)\in\{0,1\}$ that *overrides* the Standard Agent on trigger ($\tilde a=\mathbf{g}\cdot a^{\mathrm{safe}}+(1-\mathbf{g})\cdot a$), with a per-intervention cost keeping overrides selective. Rewrote both the "In this wiki" paragraph and the standard-formulations table row (was "Game-theoretic intervention / asymmetric — can break symmetry"). `updated`→2026-06-01.
- **Correctness fix (false cross-corpus negative):** [[service-caching-mec]] claimed "None of the other wiki sources currently model service caching explicitly." **False** — service/content caching is explicitly modeled in [[gao-2024-service-experience-cache-uav]] (each UAV caches a service subset via a priority-based placement heuristic), [[zhao-2024-caching-service-placement-uav]] (joint content caching + service placement via Gibbs sampling), and [[mao-2024-ntn-hierarchical-caching-cav]] (hierarchical content caching). Rewrote to name those sources and cross-link [[computational-task-caching]]; added the four pages to `related`. `updated`→2026-06-01.
- **Soft-overclaim fix (unverifiable cross-corpus "first"):** [[semantic-communication]] called [[sun-2024-mfris-semantic-antijamming]] "the corpus's first multi-antenna semantic-MEC source" — the parse grounds only the paper's **own** literature positioning (prior semantic-MEC limited to single-antenna; prior RIS-MEC bit-level), not a corpus-wide first. Rewrote to that grounded self-positioning (same precedent as the dropped "first" claims in batches 5/6/7). `updated`→2026-06-01.
- **Grounding spot-checks (verbatim against parses):** [[self-adaptive-global-best-harmony-search]] (gao-2024-sagin: SGHS solves subproblem P3, DDPG solves P1; Fig. 2(b) four-config HMCR∈{0.4,0.9}/PAR∈{0.1,0.4} study, HMCR=0.9 advantageous — verbatim); [[spectrum-sensing-channel-selection]] (shao-2024 Fig. 7: jammers 1→5 at 8 UAVs/users, PER-MATD3-JSC latency ~flat ~11.2 — verbatim); [[service-experience-ratio]] (gao-2024-service: Jain/avg-delay ratio + 19–34% / +78.6% U4→U6 — verbatim); [[rotary-wing-propulsion-energy-model]] (zeng-2019 three-term model; li-2024-rldc applies $P^{pro}(v)$ to leader+follower, "description follows [10]" — grounded); [[stochastic-game]] (li-2025: five interconnected stochastic games + NE via stage-game reduction — verbatim); [[stackelberg-game]] (wang-2025-uav-swarm single-leader, multi-leader noted as the paper's own future work — matches source limitation); [[secrecy-outage-probability]] + [[secure-computation-efficiency]] (michailidis-2024: min-SCE max over Nakagami-m SOP — grounded).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): rotary-wing-propulsion-energy-model, salp-swarm-algorithm, seamless-handover, secrecy-outage-probability, secure-computation-efficiency, self-adaptive-global-best-harmony-search, semi-markov-decision-process, service-experience-ratio, service-function-chaining, small-cell-mec, soft-actor-critic, space-air-ground-integrated-network, spatial-equity-index, spectrum-sensing-channel-selection, stackelberg-game, stn, stochastic-game (plus the three corrected: safe-reinforcement-learning, service-caching-mec, semantic-communication).

### Gates (concept batch 10)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph baseline **513 / 4455** (service-caching-mec gained four `related` links to already-present pages; node count unchanged, edge count refreshes on next rescan). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 10 — recorded, not filled)

- **Swarm/metaheuristic-family synthesis (standing, reinforced).** [[salp-swarm-algorithm]] + [[self-adaptive-global-best-harmony-search]] rejoin the standing swarm/metaheuristic family ([[whale-optimization-algorithm]], [[binary-whale-optimization]], [[multi-verse-optimizer]], [[particle-swarm-optimization]], [[gravitational-search-algorithm]], [[ant-colony-optimization]]); a family synthesis/comparison page may be worth minting (not a merge).
- **Game-theory family (standing, reinforced).** [[stackelberg-game]] + [[stochastic-game]] join [[nash-equilibrium]] / [[potential-game]] / [[bargaining-game]] / coalition-formation-game / [[double-auction]] / [[contract-theory]] / [[prospect-theory]] / [[reverse-auction-incentive]]; standing game-theory-mechanisms synthesis/comparison candidate.
- **Caching cluster.** [[service-caching-mec]] + [[computational-task-caching]] + content-caching across [[gao-2024-service-experience-cache-uav]] / [[zhao-2024-caching-service-placement-uav]] / [[zhao-2025-traj-offload-cache-migration]] / [[mao-2024-ntn-hierarchical-caching-cav]] / [[peng-2024-energy-time-uav-its]] form a comparable caching/placement/migration cluster with no single synthesis page; candidate for a synthesizer synthesis page.
- **SAC / safe-RL family.** [[soft-actor-critic]] + [[safe-reinforcement-learning]] + [[masac]] tie into the multi-agent actor-critic comparison candidate flagged in batch 7.
- No new tag fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 9; no new papers)

Continues the non-source-layer audit into **concept batch 9** (20 pages, alphabetical perception-aided-offloading → robust-offloading, positions 161–180 of `.curation-out/concept_slugs.txt`). Tree clean at `4bb87a5`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 9)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded ranking):** [[perception-aided-offloading]] claimed [[gao-2024-sagin-perception-offloading]]'s "Perception-Free" ablation is "consistently second-worst" — not grounded. In the parse, the consistently-worst scheme is **Complete-Offloading** (Fig. 3 cost 120, Fig. 4 ~79, Fig. 6 ~112); the Perception-Free method's rank varies (second-worst only in Fig. 4: 51 vs Random 50; in Fig. 3 it is 55 vs Random 75 and in Fig. 6 it is 82 vs Random 112, beating Random there). Rewrote to the grounded statement that Perception-Free (the same scheme with mmWave radar + visual sensors removed) consistently underperforms the full perception-aided approach on network cost and processed data size. `updated`→2026-06-01.
- **Correctness fix (wrong reward form):** [[qoe-modeling-mec]] stated [[bao-2025-ddpg-video-offloading]] uses $QoE=-\alpha\cdot\text{delay}-\beta\cdot(1-\text{bitrate}/\text{original})$ (two weights, linear bitrate term) — the parse (Eqs. 18/19/23) defines $QoE(i)=Q(i)-\alpha T^{\text{sys}}(i)$ with a **single** weight α and $Q(i)$ a **natural-logarithm** function of the transcoding ratio (α=0.05 in sims). Rewrote to the grounded single-weight log form. `updated`→2026-06-01.
- **Soft-overclaim fix:** [[physical-layer-security]] said [[benaya-2025-aerial-isac-haps]] "combines all three" secrecy levers (beamforming + jamming + cooperative relays) — the parse uses only **two** (transmit/receive beamforming nulls + a friendly-jamming AAV), with ISAC sensing as the eavesdropper-detection mechanism (no source-masking cooperative relay). Rewrote to "combines two of these levers". `updated`→2026-06-01.
- **Grounding spot-checks (verbatim against parses):** [[priority-based-delay-utility]] (hao-2024 Eqs. 24–25: high-priority $U^H=\log_2(1+v-T)$ on-time / $-P^H$ penalty; low-priority $U^L=P^L$ on-time / $P^L e^{-\rho(T-v)}$ decaying — exact); [[prioritized-experience-replay]] (nabi-2025: "Prioritized experience replay (PER) with soft actor-critic" inside the ESAC algorithm — grounded, ESAC naming confirmed); [[privacy-sensitive-data-partitioning]] (han-2024 §II: $\alpha_k=|D_k^o|/|D_k|$ non-sensitive portion, α=0.8 baseline + α sweep — exact); [[potential-game]] (chen-2024-ulse Theorem 2: LUTO-Game proved a potential game, potential function given, distributed JULTO → NE, PoA defined — exact); [[probsparse-self-attention-prediction]] (chen-2024-thoas: "combines probsparse self-attention and self-attention distillation" for traffic prediction + adaptive slicing — verbatim); [[proactive-eavesdropping]] (guo-2024 abstract: multiple full-duplex legitimate UAVs jam multiple suspicious UAV→destination links, joint jamming-power + trajectory — exact); [[robust-offloading]] (li-2024-robust §II: robust design "classified into three types: scheduling / channel / computation robustness" — verbatim taxonomy; Beta-policy b-MAPPO grounded); [[reverse-auction-incentive]] (zeng-2024: "first-price sealed reverse auction with reserve price", reserve = UAV benefit guarantee, symmetric equilibrium bids derived — verbatim); [[prompt-engineering]] (ye-2025: prompt-optimization level as one of four resource dimensions; +8%/+2% quality, +22% latency — verbatim, audited clean in source batch 10).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): perception-aided-offloading (corrected), physical-layer-security (corrected), pipeline-parallel-inference, pomdp, post-disaster-mec, potential-game, ppo, prioritized-experience-replay, priority-based-delay-utility, privacy-sensitive-data-partitioning, proactive-eavesdropping, probsparse-self-attention-prediction, prompt-engineering, prospect-theory, qcqp-sdr-probabilistic-mapping, qoe-modeling-mec (corrected), queueing-theory, reverse-auction-incentive, rf-energy-harvesting, robust-offloading.

### Gates (concept batch 9)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors (513 all-types, 0 errors). Graph **513 / 4455** (prose-only edits on already-present wikilinks; node/edge counts unchanged). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 9 — recorded, not filled)

- **Security/PLS tag fragmentation.** [[physical-layer-security]] tags `security`/`secrecy-rate`/`eavesdropper`, [[proactive-eavesdropping]] tags `physical-layer-security`, and [[privacy-sensitive-data-partitioning]] tags `privacy`; the PLS/secrecy/privacy family would benefit from a one-slug tag normalization (pick one). Left for the synthesizer.
- **Game-theory family (standing, reinforced).** [[potential-game]], [[reverse-auction-incentive]], and [[prospect-theory]] join [[nash-equilibrium]] / [[stackelberg-game]] / [[stochastic-game]] / [[bargaining-game]] / coalition-formation-game / [[double-auction]] / [[contract-theory]]; a game-theory-mechanisms synthesis/comparison page may be worth minting (not a merge).
- **Prediction-engine pair.** [[probsparse-self-attention-prediction]] + [[informer-trajectory-prediction]] share the Informer lineage with different targets (traffic vs trajectory); candidate for a short synthesis tie.
- No new tag fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 8; no new papers)

Continues the non-source-layer audit into **concept batch 8** (20 pages, alphabetical multi-functional-ris → penalty-dual-decomposition, positions 141–160 of `.curation-out/concept_slugs.txt`). Tree clean at `98aeb4d`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 8)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **All 20 pages verified clean — no corrections needed.** Definitions accurately reflect how each concept is used in the referencing source(s)/parse; no invented numbers, overclaims, false cross-corpus "first" claims, or stale counts; `related`/wikilinks resolve and are non-self-referential; tags reused; wording already evergreen. This is the second all-clean concept batch (like batch 3) — the audit converges rather than churns.
- **Grounding spot-checks (verbatim against parses):**
  - [[multi-objective-reinforcement-learning]] — [[song-2024-mol-aoi-energy]] parse: **MOL-AET** is a multi-objective PPO trained over uniformly-spread preference-weight vectors then refined with policy-network genetic operators, maintaining a nondominated set Q* (verbatim, incl. the m=2 / β=29 → 30-weights initialization).
  - [[noma]] — [[qin-2025-bcuav-masac]] §III channel model: "we adopt the NOMA method and the spectrum resources between UAVs are orthogonal", SINR $\gamma_{j,k}$ with intra-cluster interference $I_j^k=\sum_{i\ne j}a_{i,k}p_{i,k}g_{i,k}$ and per-slot transmit power $p_{j,k}(t)$ as a decision variable — matches the page verbatim (NOMA within a UAV cluster, orthogonal between UAVs).
  - [[multi-uav-assisted-mec]] — [[liu-2026-jppo-en-convntm]]: "j-PPO+EN-ConvNTM" jointly controls UAV flight trajectory, task-offloading strategy, and **charging indicators** to minimize energy / maximize data-collection / ensure fairness in high-density mobile-device scenarios (verbatim contributions list); the hybrid continuous-discrete action framing motivating [[j-ppo]] is grounded.
  - [[multi-tasking-evolutionary-algorithm]] — [[wu-2026-terrain-aware-uav-mec]] title + body: "task-adaptive mechanism" that retains historically-effective genetic operators per individual (bandit-style operator selection) — grounded.
  - [[particle-swarm-optimization]] — APSO verbatim in [[albakhrani-2025-moalf-uav-mec]] (Algorithm 4 + §IV-G "Adaptive Particle Swarm Optimization (APSO) for Dynamic Resource Allocation"); chain-ordering PSO in [[wang-2025-acbft-uav-consensus]]; IPSO in [[zhang-2024-uav-task-offloading-ddpg]].
  - [[order-preserving-quantization]] (wu-2025 OPPO extends the DROO order-preserving candidate-generation, each candidate scored after WOA phase optimization), [[parameterized-dqn]] ([[ma-2025-pdqn-vehicular-mec]] hybrid discrete-server + continuous-power), [[over-the-air-computation]] ([[fu-2025-otae-inference-lae-batching]] superposition aggregation + spatial-correlation-aware beamforming), [[network-function-virtualization]] ([[zhang-2025-vnf-sgin-dql]] SDN/NFV 6G satellite-ground VNF selection+chaining via DQL), and [[penalty-dual-decomposition]] ([[hu-2019-pdd-uav-mec-offloading]] inner CCCP / outer multiplier+penalty with binary-to-equality conversion) — all grounded.
- **Verified clean** (full list): multi-functional-ris, multi-objective-mdp-vectorial-reward, multi-objective-reinforcement-learning, multi-source-data-fusion, multi-tasking-evolutionary-algorithm, multi-uav-assisted-mec, multi-verse-optimizer, nash-equilibrium, network-function-virtualization, network-slicing, noma, non-terrestrial-network, ntm, order-preserving-quantization, over-the-air-computation, overlay-underlay-spectrum-access, parallel-vs-serial-processing, parameterized-dqn, particle-swarm-optimization, penalty-dual-decomposition.

### Gates (concept batch 8)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (no page edits this batch). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 8 — recorded, not filled)

- **Swarm/metaheuristic-family synthesis (standing, reinforced).** [[multi-verse-optimizer]] and [[particle-swarm-optimization]] join the standing swarm/metaheuristic family ([[whale-optimization-algorithm]], [[binary-whale-optimization]], [[salp-swarm-algorithm]], [[gravitational-search-algorithm]], [[ant-colony-optimization]], self-adaptive-global-best-harmony-search). A family synthesis/comparison page tying these distinct-but-comparable derivative-free metaheuristics together may be worth minting (not a merge).
- **Hybrid-action family (standing, reinforced).** [[parameterized-dqn]] joins [[hybrid-action-decision-making]] / [[hybrid-action-representation]] / [[j-ppo]] / [[soft-actor-critic]] as another way to handle coupled discrete-continuous actions; same standing hybrid-action synthesis candidate flagged in batch 6.
- **NTN/LEO cluster (standing).** [[non-terrestrial-network]] joins the LEO/NTN concept cluster flagged in batch 6 ([[leo-satellite-edge-computing]] / [[leo-satellite-coverage-time]] / [[leo-handover-protocol]] / [[space-air-ground-integrated-network]]); candidate for a synthesizer synthesis page.
- No new tag fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 7; no new papers)

Continues the non-source-layer audit into **concept batch 7** (20 pages, alphabetical low-altitude-intelligent-network → multi-agent-td3, positions 121–140 of `.curation-out/concept_slugs.txt`). Tree clean at `d5adff0`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 7)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (stale cross-corpus undercount):** [[maritime-mec]] stated "The wiki has **two** maritime sources" and listed only [[wang-2026-aerial-marine-msar]] + [[liu-2025-haps-uav-maritime-iot]] — a stale undercount. The corpus carries a substantial maritime track (**18 sources** tagged `maritime-mec`) and already has a [[maritime-mec-architectures]] synthesis page mapping seven of them. Rewrote to describe the track without a hard count (kept the two as representative communication/compute endpoints) and cross-linked the synthesis page; added [[maritime-mec-architectures]] to `related`. `updated`→2026-06-01.
- **Evergreen-wording fix:** [[lyapunov-optimization]] ended its "In this wiki" note with "Expect more sources to use the same template" (forward-looking process-narration). Rewrote to the evergreen fact that the drift-plus-penalty template recurs across the corpus's online-control sources, with named cross-links ([[dai-2024-uav-vehicular-offloading-lyapunov]], [[yang-2022-stochastic-uav-mec-lyapunov]], [[wang-2024-maritime-eh-jcora]], [[mao-2016-lodco-eh-mec-offloading]] — all `lyapunov`-tagged). `updated`→2026-06-01. (Soft case `process_refs.py` does not pattern-match; fixed by hand.)
- **Grounding spot-checks (verbatim against parses):** [[majorization-minimization]] (chu-2024 parse §III-C: MM pursues "a convex surrogate function that locally lower bounds it … Utilizing the first-order Taylor expansion" for the RIS-reflection term, alongside SDR + FP — verbatim); [[monotonic-optimization]] (sun-2024-mfris parse §III + abstract: "fast-converging monotonic optimization … combined with decoupling second-order cone programming (MO-DSOCP) … globally optimal solution with fewer feasibility evaluations" over a quasi-convex objective with MINLP constraints — verbatim); [[masac]] (qin-2025 Findings: MASAC chosen over MADDPG, entropy-regularized objective gives more stable convergence + higher final sensing rate — grounded); [[mappo]] (kang-2023: MAPPO under CTDE solves the UAV+HAP offloading POMDP with state normalization + action masking — grounded); [[markov-reward-process]] (niazmand-2025: stochastic IIoT problem recast as an MRP with per-time-slot delay/accuracy constraints, solved by hybrid-action SAC — grounded); [[markov-approximation]] (dai-2024: per-slot Markov-chain search after Lyapunov decoupling of the long-term UAV-energy constraint — grounded); [[multi-agent-q-learning]] (li-2025-stochastic-game: RLDC tabular multi-agent Q-learning with Q-value exchange, NE via contraction-mapping — matches the source page); [[makespan-minimization]] (huang-2023: makespan as one of two CMOP objectives over DAG dependencies — grounded).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): the remaining 18 batch-7 concepts (low-altitude-intelligent-network [idempotent — batch-9 wording fix intact], ma-pomdp, maddpg, majorization-minimization, makespan-minimization, mappo, markov-approximation, markov-reward-process, masac, matching-theory-for-resource-allocation, mixed-integer-nonlinear-programming, mmwave-radar-sensing, mobile-aigc-network, mobile-edge-computing, mobility-aware-offloading, monotonic-optimization, multi-agent-q-learning, multi-agent-td3).

### Gates (concept batch 7)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph baseline **513 / 4455** (the two corrected pages added a few intra-corpus wikilinks between already-present pages; node count unchanged, edge count refreshes on next rescan). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 7 — recorded, not filled)

- **Maritime track is well-covered** — [[maritime-mec-architectures]] synthesis + [[maritime-three-tier-energy-saving]] finding already exist; that synthesis page's own "Gaps" note (no maritime security/trust source, CSI-uncertainty mostly side-stepped, no classical-vs-DRL head-to-head on a maritime benchmark) is the standing maritime routing note. No new maritime page needed from this batch.
- **Multi-agent actor-critic family.** [[maddpg]], [[multi-agent-td3]], [[masac]], [[mappo]], and [[multi-agent-q-learning]] each have a clean per-method concept page with overlapping rosters and explicit "vs siblings" prose, but there is no single synthesis/comparison page tying the CTDE actor-critic family (deterministic MADDPG/MATD3 vs stochastic MASAC vs on-policy MAPPO vs value-based multi-agent Q-learning) together across the corpus. Candidate for a synthesizer comparison page (not a merge).



Continues the non-source-layer audit into **concept batch 6** (20 pages, alphabetical hybrid-action-decision-making → local-search-evolutionary, positions 101–120 of `.curation-out/concept_slugs.txt`). Tree clean at `539f30a`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 6)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded number — same overclaim caught in the batch-6 source audit):** [[load-balancing-uav-mec]] claimed [[nabi-2025-jour-hierarchical-aerial]] "shows that the max-min UAV-load gap shrinks substantially vs greedy baselines" — **not in the parse**, which reports **average load per UAV** (Fig. 8: JOUR 0.30 vs GOUA+SAC/PPO/DDPG/HA 0.32/0.40/0.41/0.44 at 30 GUs), not a max-min gap. Rewrote to the grounded average-load result with the verbatim figures; the per-UAV-load reward term (cycles ÷ capacity, Eq. 25a) and GU-capping-by-capacity (parse L107/125) are confirmed grounded.
- **Correctness fix (false cross-corpus "first"):** [[intelligent-reflecting-surface]] ended "This is the corpus's first IRS entry" — **false**: the corpus carries many IRS/RIS sources. Replaced with a grounded cross-link to the anti-jamming / secure-beamforming IRS family ([[sun-2024-active-passive-ris-receiver]], [[sun-2024-mfris-semantic-antijamming]], [[michailidis-2024-secure-ris-uav-mec-iot]], [[mao-2025-irs-noma-fl-secrecy]], [[zhang-2025-gan-td3-isac-active-ris]]).
- **Ungrounded-number fix:** [[informer-trajectory-prediction]] illustrated the attention-cost argument with "$O(H^2)$ for $H = 24$ h history × thousands of vehicles" for [[zhang-2025-mcma-task-migration]] — the **24 h / thousands-of-vehicles** scale is **not in that parse** (which states only an Informer-based multi-step vehicular trajectory predictor). Rewrote to the grounded mechanism (ProbSparse keeps long-sequence attention tractable as the horizon grows). Informer's own architecture facts (ProbSparse top-$\log L$, distilling encoder, $O(L\log L)$, $L=720$+) are correct general ML facts about Zhou et al. AAAI 2021 and left intact.
- **Soft-superlative fix (unverifiable cross-corpus "first"):** [[knowledge-distillation-for-drl]] called [[chen-2024-thoas-traffic-aware-sagin]] "the corpus's first explicit treatment of on-platform model-size constraints" — softened to "brings on-platform model-size constraints into the corpus as a first-class design concern" + cross-link to the DNN-pruning angle in [[niazmand-2025-jopa-dnn-pruning-iiot]] (consistent with the batch-5/7 precedent). The distillation numbers (~6%/73%, ~90%@12%, ~97%@50%) are grounded (verbatim in the chen-2024 parse + source page).
- **Grounding spot-checks (verbatim against parses):** [[interdependent-tasks-dag]] (huang-2023 intro: "According to the statistic of the Alibaba data trace, more than 75% of 4 million applications contain interdependent tasks [8]"; DAG examples face recognition + vehicular navigation grounded L91); [[impala]] (lee-2024 L29/398: IMPALA + V-trace, parallel actor-learners + importance sampling, "stable training … large state and action spaces", advantages over DQN/A3C/PPO — verbatim); [[j-ppo]]/[[j-ppo-en-convntm]]/[[hybrid-action-decision-making]] (liu-2026 hybrid clip $g^{hybrid}=c_3·\text{cont}+(1-c_3)·\text{disc}$, $c_1=0.1$/$c_2=0.01$/$c_3=0.5$ Table I); [[information-causality-constraint]] (zeng-2016 staircase water-filling consequence).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): the remaining 16 batch-6 concepts (hybrid-action-decision-making, hybrid-action-representation, impala, infeasible-individual-utilization, information-causality-constraint, integrated-sensing-and-communication, integrated-sensing-computation-communication, interdependent-tasks-dag, intra-swarm-task-delegation, j-ppo-en-convntm, j-ppo, jains-fairness-index, leo-handover-protocol, leo-satellite-coverage-time, leo-satellite-edge-computing, local-search-evolutionary).

### Gates (concept batch 6)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors (513 all-types, 0 errors). Graph baseline **513 / 4455** (the four corrected pages added a few intra-corpus wikilinks between already-present pages; node count unchanged, edge count refreshes on next rescan). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 6 — recorded, not filled)

- **Hybrid-action family synthesis.** [[hybrid-action-decision-making]], [[hybrid-action-representation]] (HyAR latent space), [[j-ppo]] (dual-head PPO), [[parameterized-dqn]], and (cross-batch) [[soft-actor-critic]] + niazmand's SAC hybrid action describe distinct ways to handle coupled discrete-continuous action spaces. A synthesis/comparison page tying the hybrid-action family together may be worth minting (not a merge).
- **LEO-satellite / NTN concept cluster.** [[leo-satellite-edge-computing]], [[leo-satellite-coverage-time]], [[leo-handover-protocol]], [[walker-star-constellation]], [[seamless-handover]], [[free-space-optical-isl]], [[non-terrestrial-network]] form a dense, comparable LEO/NTN cluster with no single synthesis page; candidate for a synthesizer synthesis page.
- **Evolutionary-family tag fragmentation (standing).** infeasible-individual-utilization + local-search-evolutionary tag `evolutionary`, while [[differential-evolution]]/[[constraint-violation-evaluation]] use `evolutionary-algorithm`. Same standing normalization flagged in batches 2/4; no new fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 5; no new papers)

Continues the non-source-layer audit into **concept batch 5** (20 pages, alphabetical finite-blocklength-urllc → high-density-mobile-device-scenarios, positions 81–100 of `.curation-out/concept_slugs.txt`). Tree clean at `7584c2a`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 5)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded architectural detail):** [[heterogeneous-uav-fleet]] described [[zhang-2025-ssac-mgi-heterogeneous-uav]]'s **SSAC** as a "(shared backbone + per-UAV head)" architecture and called it "the first source explicitly addressing heterogeneity" — the per-UAV-head split is **not in the parse**, which defines SSAC (Shared Soft Actor-Critic) as a **policy-sharing** design that extracts *dimension-invariant* features so heterogeneous UAVs (varying service type / resource capacity) learn a **unified** policy (three shared SAC modules: standard/safety/intervention). Rewrote to the grounded policy-sharing mechanism and dropped the unverifiable cross-corpus "first" claim.
- **Evergreen-wording fix:** [[high-density-mobile-device-scenarios]] ended with "Subsequent sources should be tagged for whether they assume static, low-mobility, or high-density conditions" — a forward-looking instruction to a later curation run. Rewrote to the evergreen fact "Sources in the corpus differ in whether they assume static, low-mobility, or high-density conditions."
- **Grounding spot-checks (verbatim against parses):** [[finite-blocklength-urllc]] (wu-2024 parse: short packets "20 or 32 bytes", Shannon overstates rate, **angle-dependent Rician fading**, logarithmic rate approximation — all verbatim); [[fractional-programming-dinkelbach]] (zhu-2025 parse: fractional-programming theory + Lyapunov transform the **LSEM** EE-max into a per-slot MINLP — acronym and combination grounded); [[gale-shapley-matching]] (nabi-2025 parse: GOUA is a "matching-game-based algorithm inspired by the Gale-Shapley algorithm" for GU-UAV association by mutual preference scores); [[gauss-markov-mobility-model]] (liu-2026 parse §III-A + ref [31]: GM speed/direction first-order chains, **256** IoT devices in a **160 m × 160 m** arena); [[friendly-jamming-uav]] (benaya-2025 parse: jamming AAV degrades eavesdropper reception; transmit/receive beamforming + AAV trajectory jointly optimized via **alternating optimization** with HAPS); [[gravitational-search-algorithm]] (zheng-2024 IMOGSA: quasi-opposition learning + discrete update + NSGA-II-style archive, chosen vs DRL/convex).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): the remaining 18 batch-5 concepts (finite-blocklength-urllc, fixed-wing-propulsion-energy-model, fl-poisoning-attacks, fractional-programming-dinkelbach, free-space-optical-isl, friendly-jamming-uav, gae, gale-shapley-matching, gauss-markov-mobility-model, generalized-assignment-problem, generative-adversarial-network, generative-ai-for-mec, generative-diffusion-model, gravitational-search-algorithm, heterogeneous-agent-rl, hierarchical-aerial-mec [idempotent — batch-9 wording fix intact], hierarchical-reinforcement-learning, high-altitude-platform-station).

### Toolkit ratchet (concept batch 5)

- Generalized `process_refs.py`'s forward-looking-placement pattern from `future …` only to also catch `subsequent | later | upcoming | forthcoming … sources/pages/entity-pages should/will/must/land/belong/be tagged`, so the [[high-density-mobile-device-scenarios]] leak above is caught by the tool going forward. README updated. Regression-checked: still does **not** flag a paper's own "future work" / "future research directions" (noun = work/research, not curation vocabulary).

### Gates (concept batch 5)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (prose-only edits, no new links/pages). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 5 — recorded, not filled)

- **Swarm/metaheuristic family synthesis (standing, reinforced).** [[gravitational-search-algorithm]] joins the spread of distinct mixed-variable aerial metaheuristics ([[multi-verse-optimizer]], [[salp-swarm-algorithm]], [[whale-optimization-algorithm]], [[binary-whale-optimization]], [[particle-swarm-optimization]], [[ant-colony-optimization]], [[self-adaptive-global-best-harmony-search]]) — all chosen to emit a one-run Pareto set for NP-hard MINLP collaborative-beamforming/CB problems, explicitly motivated against DRL (no training) and convex (no space distortion). These are genuinely different algorithms (not duplicates); a synthesis/comparison page tying the swarm-metaheuristic family together remains worth minting (flagged in concept batch 1; not a merge).
- **Tag fragmentation in the generative-AI family.** [[generative-adversarial-network]]/[[generative-diffusion-model]] tag `generative-ai`, while [[generative-ai-for-mec]] tags `gai` and [[generative-diffusion-model]]/[[diffusion-model-as-optimizer]] also use `diffusion`. A tag-vocabulary normalization (pick one umbrella slug, e.g. `generative-ai`) would de-fragment the family. Flagged only — no merge/delete/retag here.

## 2026-06-01 — Audit pass (non-source layer — concept batch 4; no new papers)

Continues the non-source-layer audit into **concept batch 4** (20 pages, alphabetical dual-population-evolutionary-algorithm → federated-reinforcement-learning, positions 61–80 of `.curation-out/concept_slugs.txt`). Tree clean at `8f0b593`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 4)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded mechanism / misclassification):** [[energy-balancing-uav]] had two defects vs the parses. (1) It described [[huang-2023-mu-aec-task-energy]]'s energy-balancing index as a "sum of pairwise differences"; the parse Eq. 13 defines it as a **sum of squared normalized deviations** from the swarm mean, $G_2=\sum_j((TE_j-\overline{TE})/\psi)^2$ — matching the batch-3 source-page correction. Rewrote with the actual formula. (2) It listed [[nabi-2025-jour-hierarchical-aerial]] as an energy-balancing "Variance / max-min penalty in DRL reward"; the batch-6 source audit established nabi-2025's third SAC-reward term is per-UAV **load** (computed cycles ÷ compute capacity, Eq. 25a) — i.e. **load balancing**, not energy balancing. Moved nabi-2025 to the load-balancing contrast and corrected the framing.
- **Evergreen-wording fix:** [[federated-learning]] called itself "the base concept underlying the wiki's **prior**, narrower [[federated-reinforcement-learning]]/[[blockchain-for-fl-aggregation]] pages" — "prior" narrates page-creation order; dropped to "the wiki's narrower …". (Soft case fixed by hand; not added to `process_refs.py` to avoid false-positives on a paper's own "prior work".)
- **Grounding spot-checks (verbatim against parses):** [[dual-population-evolutionary-algorithm]] (huang-2025 parse: "dual-population cooperative mechanism between two populations and a repairing constraint-handling technique" — attribution + repairing-CH correct); [[dynamic-confidence-interval-clipping]] (chen-2024-thoas Eq. 31–32: two-layer confidence interval, dynamic factor α_t scaled by κ adapting to the **sign** of the TD error δ — fully grounded); [[elastic-task-scheduling]] (sun-2024-asap §IV-C + Table IV: ECLB/ICLB online reschedule on cluster-head cutoff/recovery, rescheduling latency "within 1 second", latency returns to baseline after recovery).
- **Verified clean** (definition grounded, no invented numbers/overclaims, links resolve & non-self-referential, tags reused, evergreen): the remaining 18 batch-4 concepts (dual-population-evolutionary-algorithm, dynamic-confidence-interval-clipping, dynamic-constrained-multi-objective-optimization, dynamic-qos-constraints, dynamic-uav-clustering, edge-user-allocation, elastic-task-scheduling, en-convntm, end-to-end-vs-decomposition-in-drl-mec [idempotent — batch-1 wording fix intact], energy-expenditure-coefficient, energy-harvesting-mec, energy-latency-tradeoff, equilibrium-efficiency-metric, event-driven-vs-slot-driven-offloading, evolutionary-reinforcement-learning, fairness-metrics-in-mec, fault-tolerant-relay-network, federated-reinforcement-learning).

### Gates (concept batch 4)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (prose-only edits, no new links/pages). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 4 — recorded, not filled)

- **Tag fragmentation in the evolutionary-algorithm family (standing).** The same fragmentation flagged in concept batch 2 recurs here — `dual-population-evolutionary-algorithm`, `dynamic-constrained-multi-objective-optimization`, and `evolutionary-reinforcement-learning` tag `evolutionary`, while [[differential-evolution]]/[[constraint-violation-evaluation]] use `evolutionary-algorithm`. A tag-vocabulary normalization (pick one slug) would de-fragment the family. Flagged only — no merge/delete/retag here; no new fragmentation introduced this batch.

## 2026-06-01 — Audit pass (non-source layer — concept batch 3; no new papers)

Continues the non-source-layer audit into **concept batch 3** (20 pages, alphabetical cooperative-perception → drone-cell-3d-placement, positions 41–60 of `.curation-out/concept_slugs.txt`). Tree clean at `18dc945`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 3)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **All 20 verified clean — no corrections needed.** Definitions reflect how each concept is used in the source(s) they cite; no invented numbers/overclaims; `related`/wikilinks resolve and are non-self-referential; tags reused; evergreen wording (no process-narration). Grounding spot-checks against the parses: [[cross-entropy-method]] (li-2023 "Code bAsed croSs Entropy (CASE-Algorithm)" + Polyblock-Approximation/bisection "PAS-Algorithm" solving the bottom problem via canonical [[monotonic-optimization]] — verbatim); [[cooperative-perception]] (xie-2026 abstract: cooperative perception fuses multi-source observations over V2X, vehicle-based suffers occlusion, infrastructure-based has coverage gaps — matches the V2V/V2I/V2U platform table). The batch-1 evergreen-wording fix on [[cooperative-perception]] ("is the wiki's source bringing cooperative perception in") is intact — idempotent re-check, no change.
- Pages: cooperative-perception, cramer-rao-bound, cross-entropy-method, csi-estimation-error, csra-cold-start-reputation-aggregation, data-partition-parallel-inference, ddpg, ddqn, decentralized-federated-learning, deep-q-network, delegated-proof-of-stake, differential-evolution, diffusion-model-as-optimizer, dispersed-computing, distributed-foundation-models, distributionally-robust-optimization, dl-inference-latency-prediction, dnn-model-partition, double-auction, drone-cell-3d-placement.

### Gates (concept batch 3)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (no page edits this batch). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 3 — recorded, not filled)

- **Tag fragmentation in the CSI/robust-optimization family.** [[csi-estimation-error]] tags `channel-state-information` while [[robust-offloading]] and [[distributionally-robust-optimization]] tag `csi` (and `robust` vs `robust-optimization` across the same cluster). A tag-vocabulary normalization (pick one slug each) would de-fragment the family. Flagged only — no merge/delete/retag here.

## 2026-06-01 — Audit pass (non-source layer — concept batch 2; no new papers)

Continues the non-source-layer audit into **concept batch 2** (20 pages, alphabetical blockchain-for-fl-aggregation → cooperative-jamming, positions 21–40 of `.curation-out/concept_slugs.txt`). Tree clean at `cb14bb1`. Phase 0 reconciled clean: `curation_status.py --dupes` = **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Correctness & consistency audit (Phase B — concept batch 2)

Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Correctness fix (ungrounded mechanism):** [[collision-avoidance-mgi]] described MGI as a *two-agent inter-UAV* "intervention agent vs non-intervention agent" game with a "symmetric-swerve collision" failure mode, a Nash-equilibrium "stable separation maneuver", and role assignment "by UAV ID / speed / heading" — **none of which is in the parse**. This is the same mischaracterization the batch-11 source audit corrected on [[zhang-2025-ssac-mgi-heterogeneous-uav]]: the parse (§V-B, Eqs. 32–34) defines MGI as a **per-UAV** two-agent game — a stochastic reward-maximizing **Standard Agent** plus a deterministic **Safety Agent** with a **binary gating policy** g(s)∈{0,1} that *overrides* the Standard Agent when an intervention triggers (ã = g·a_safe + (1−g)·a), giving safety guarantees during and after training. Rewrote the body to the grounded gating mechanism + the constant-altitude (2-D, 500×500) scope; dropped the invented Nash/symmetric-swerve story.
- **Consistency fix (grounding):** [[chance-constraint]] said the [[jia-2025-dro-uav-hap-mec]] reformulation "yields a tractable second-order cone program"; the parse reformulates the chance constraint into a **mixed-integer** SOCP (**MISOCP**), matching the [[conditional-value-at-risk]] page. Tightened to MISOCP.
- **Verified clean** (definition grounded, no invented numbers, links resolve & non-self-referential, tags reused, evergreen): the remaining 18 batch-2 concepts (blockchain-for-fl-aggregation, byzantine-fault-tolerant-consensus, ccvm-correction-voting, cellular-connected-uav, centralized-training-decentralized-execution, cmoea-d-cdp, coalition-formation-game, collaborative-beamforming, collaborative-dl-inference, completion-time-difference, computational-task-caching, conditional-gan, conditional-value-at-risk, constrained-multi-objective-evolutionary-algorithm, constraint-violation-evaluation, contract-theory, convlstm, cooperative-jamming).

### Gates (concept batch 2)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py --type concept`** = 234 pages, 0 errors. Graph unchanged **513 / 4455** (prose-only edits, no new links/pages). `log.md` edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 2 — recorded, not filled)

- **Tag fragmentation in the evolutionary-algorithm family.** Most pages use the tag `evolutionary` (cmoea-d-cdp, constrained-multi-objective-evolutionary-algorithm, dual-population-evolutionary-algorithm, infeasible-individual-utilization, local-search-evolutionary, multi-tasking-evolutionary-algorithm, evolutionary-reinforcement-learning, salp-swarm-algorithm, dynamic-constrained-multi-objective-optimization) while [[differential-evolution]] and [[constraint-violation-evaluation]] use `evolutionary-algorithm`. A tag-vocabulary normalization (pick one) would de-fragment the family. Flagged only — no merge/delete here.

## 2026-06-01 — Audit pass (non-source layer — concept batch 1; no new papers)

First invocation of the **non-source-layer** audit, beginning the concept pages now that all 171 source pages are audited (batches 1–12 below). Phase 0 reconciled clean: `curation_status.py --dupes` reports **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator`). Tree clean at `159bd17`; `corpus_counts.py` confirms 171 / **234 concepts** / 71 entities / 14 findings / 11 synthesis / 4 comparisons / 2 methodology / 5 queries / 1 thesis. LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4455 edges**.

### Non-source coverage plan

- Split the non-source layer into **concepts (234) → entities (71) → derived (37)** ≈ 342 pages. Concept list (`.curation-out/concept_slugs.txt`) batched with `make_batches.py --size 20` → **12 concept batches** of 20 (last 14). Tracker: `.curation-out/audit-coverage.md`.

### Correctness & consistency audit (Phase B — concept batch 1)

Audited **concept batch 1** (20 pages, alphabetical action-space-explosion-in-multi-uav-mec → blockage-aware-channel-model). Concept-page checks: definition grounded in the source(s)/parse it cites, no invented numbers/overclaims, `related`/wikilinks resolve and are non-self-referential, tags reused, evergreen wording.

- **Evergreen-wording fixes (forward-looking curation-workflow placement → fact):**
  - [[air-ground-integrated-network]] — dropped trailing "Future cross-layer sources should land here."
  - [[cooperative-perception]] — "[[xie-2026-uav-multisource-fusion]] is the **first** source … Future curated perception-class sources should land here." → "is the wiki's source bringing cooperative perception in" (placement instruction removed).
  - synthesis [[drl-backbones-across-uav-mec-sources]] — dropped trailing "Future sources should treat it as the default."
  - `index.md` Tools note — "Future entity pages should land here as more authors recur." → dropped (kept the evergreen "entity pages exist for the central recurring contributors").
- **Grounding spot-checks (verbatim against parses):** [[active-ris]] scaling (Theorem 5: receive power ∝ N_A²·N_P², asymptotic SINR ∝ N_A·N_P, vs (N_P+N_A)² / (N_P+N_A) for single-layer active RIS); [[adaptive-intermediate-data-compression]] (ASAP 8-bit quantization + gzip lossless; 87.2%–92.7% data-size reduction, accuracy reduction within 0.15%); [[b-spline-trajectory]] (3λ control-point parameterization). All confirmed grounded.
- **Verified clean** (definition grounded, no invented numbers, links resolve & non-self-referential, tags reused): the remaining 16 batch-1 concepts (action-space-explosion-in-multi-uav-mec, adaptive-entropy-priority-replay, adaptive-inter-layer-data-offloading, age-of-information, aigc-service-provider, air-to-ground-channel-model, alternating-direction-method-of-multipliers, alternating-optimization-sdr-sca, ant-colony-optimization, anti-jamming-mec, aoi-energy-tradeoff, bargaining-game, beta-policy-drl, binary-vs-partial-offloading, binary-whale-optimization, blockage-aware-channel-model).

### Toolkit

- **Extended `process_refs.py`** (+ README) with two forward-looking-placement patterns (`(should|will|would) land here`; `future … sources/pages/entity-pages (should|will|would|land|belong)`). Regression-checked: it does **not** flag the legit evergreen "## Limitations / future work" sections on source pages (a paper's own future work is domain content). Caught exactly the 4 leaks above; all fixed → tool exits 0.

### Gates (concept batch 1)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors (`--type concept`: 234, 0 errors). Graph unchanged **513 / 4455** (prose-only edits, no link changes). Meta docs (`index.md`, `log.md`) edited with file tools, verified mojibake-free.

### Routing to `mec-wiki-synthesizer` (concept batch 1 — recorded, not filled)

- **Swarm-metaheuristic family** is spread across distinct algorithm pages (binary-whale-optimization, whale-optimization-algorithm, multi-verse-optimizer, salp-swarm-algorithm, particle-swarm-optimization, ant-colony-optimization, gravitational-search-algorithm, self-adaptive-global-best-harmony-search). These are genuinely different algorithms (no merge), but a synthesis/comparison page tying the swarm-metaheuristic family together — when each is used and against what baselines — may be worth minting.

## 2026-06-01 — Audit pass (meta-doc cleanup + correctness batches 1–12/12; no new papers)

First invocation of a multi-invocation batched audit over the fully-curated 171-source corpus. Phase 0 reconciled clean: `curation_status.py --dupes` reports **171 raw = 171 curated, 0 uncurated, 0 genuinely-new** (no routing to `mec-wiki-curator` needed). Tree clean at `f81cbb4`. LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **513 nodes / 4449 edges**.

### Meta-doc cleanup (Phase A)

- **`index.md`** — added 6 concept pages that existed on disk but were uncatalogued ([[value-decomposition-network]], [[impala]] under DRL backbones; [[majorization-minimization]] under optimization techniques; [[proactive-eavesdropping]] under sensing & security; [[leo-handover-protocol]] + [[fault-tolerant-relay-network]] under aerial/network architectures). Fixed the stale reference-DB count (2981 → **5054**, matching the scout-owned [[reference-database]]). Every catalogue-able wiki page is now indexed exactly once (verified with the new `index_audit.py`); the remaining multi-listed slugs are deliberate entity-roster / `>` cross-reference mentions, not duplicate bullets.
- **`overview.md`** — added the previously-missing 5th query ([[end-to-end-drl-feasibility-large-scale-mec]]) to Open questions. Snapshot counts re-verified exact via `corpus_counts.py` (171 / 234 / 71 / 14 findings / 11 synthesis / 4 comparisons / 2 methodology / 5 queries / 1 thesis); the "70 author pages + [[pytorch]] = 71" split confirmed (70 author-tagged + 1 tool).
- **`log.md`** — already consolidated (single [Raw-source housekeeping](#raw-source-housekeeping) section, strict reverse-chronological order, normalized `## YYYY-MM-DD — <title>` headers); this pass only prepended this entry. Meta docs edited with the file tools (never PowerShell redirection); verified mojibake-free at the byte level.

### Correctness & consistency audit (Phase B — batch 1/12)

Audited the just-converted **end-to-end-DRL English cluster** + **source-page batch 1** (15 pages, alphabetical al-hourani-2014 → cheng-2025; batch plan tracked in `.curation-out/audit-coverage.md`).

- **Ungrounded-number fix:** [[albakhrani-2025-moalf-uav-mec]] claimed "92.8% efficiency at double-scale / 83.5% at ten-fold scale" — **92.8% is absent from the parse** and 83.5% is a single per-system-load figure datapoint, not a scale-multiplier result. Rewrote to the parse's actual scalability framing (IoT devices 50→500, UAVs 5→50; figure-derived degradation), keeping the grounded 94.50% / 1890 / 96% / 38% / 55% claims.
- **DOI provenance fix:** [[bao-2025-ddpg-video-offloading]] cited `10.1007/s40747-025-02106-1` as if parse-grounded, but the Springer parse carries no DOI line. Added a metadata note marking the DOI + venue **web-confirmed** (Springer record), parse supplies only title/dates/year.
- **Evergreen-wording fix:** [[drl-vs-evolutionary-vs-classical-solvers]] scope note said "not a current census of all **134**" — a stale hardcoded corpus size. Rewrote to "not a current census of the full corpus" (evergreen).
- **Verified clean** (DOI/venue/year against parse; headline numbers grounded; frontmatter valid; slugs/tags/`related` consistent): the 4 end-to-end-DRL cluster pages, al-hourani-2014, apostolopoulos-2021, bai-2024, benaya-2025, bi-2025 (empty url/venue correct — no pub metadata in parse), bor-yaliniz-2016 (web-confirmed note already present), chang-2022, chen-2023, chen-2024-thoas, chen-2024-three-party, chen-2024-ulse, chen-2025. Spot-checked precise numbers verbatim: cheng-2025 "5.72% / >1.88× / 37.4% vs GE", chen-2024-ulse execution-time magnitudes.

### Toolkit

- Added **`tools/wiki/index_audit.py`** (+ README entry) — reconciles the wiki page inventory against `index.md`: reports pages on disk not catalogued and slugs linked more than once; exit non-zero on either. Promoted from what would otherwise be an ad-hoc one-off, per the toolkit ratchet.

### Gates

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 pages unindexed. Frontmatter diagnostics clean on every touched page.

### Routing to `mec-wiki-synthesizer` (coverage gaps — recorded, not filled)

- **Stale roster needs re-tally:** [[drl-vs-evolutionary-vs-classical-solvers]] still reasons over a 26-source family roster; a full re-census across the 171-source corpus is owed (wording made evergreen here, but the analytical broadening is the synthesizer's job).
- **Candidate synthesis:** the "multi-agent-policy-gradient as a Stackelberg-equilibrium solver" pattern appears in [[bi-2025-sg-mapg]] and relates to [[wang-2025-uav-swarm-stackelberg]] / the [[game-theoretic-offloading-formulations]] comparison — worth a synthesis page if a third source uses it.
- **Remaining audit scope:** 11 source-page batches (~156 pages) plus concepts/entities/most derived pages are unaudited; later invocations continue from `.curation-out/audit-coverage.md`.

### Correctness & consistency audit (Phase B — batch 2/12)

Audited **source-page batch 2** (15 pages, alphabetical chu-2024 → gao-2024-service-experience-cache-uav). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `ecc04aa`; baseline graph **513 nodes / 4455 edges**.

- **All 15 pages verified clean** — DOIs/venues/years confirmed against each parse; headline numbers grounded against the parse text, no ungrounded numbers found. Spot-checked verbatim: [[gao-2024-service-experience-cache-uav]] "19–34% higher / 78.6% (U=4→6) / average service delay [24.1, 40.4] s (mean 33.4) / 54%·32%·23% vs GCR·FRA·NCOA"; [[dai-2023-hybrid-marine-mmwl]] "≤3% gap / >90% time saving vs LINGO"; [[chu-2024-secure-ris-isac]] "2 dB radar SNR gain w/ RIS"; [[du-2024-d2sac-aigc-asp-selection]] "seven DRL baselines (DQN/DRQN/Prioritized-DQN/Rainbow/REINFORCE/PPO/SAC)"; [[du-2024-gdm-network-optimization-tutorial]] "WoS GDM papers 12 (2014) → 257 (2023)"; [[duan-2023-moto-smallcell-offloading]] "29,284,966 records / 21,725 users / 4,045 APs". [[gao-2024-sagin-perception-offloading]] numeric setup/curves are figure-derived and already marked indicative on the page.
- **Tag-vocabulary consistency fix (corpus-wide sweep):** added the required `source` tag to **26** source pages that `frontmatter_audit.py` flagged as missing it (`updated` bumped to 2026-06-01 on each). `frontmatter_audit.py` now exits 0 over all 513 typed pages.

### Toolkit

- **Sharpened `tools/wiki/index_audit.py`** (+ README) to separate true **duplicate primary listings** (a slug that leads more than one bullet — a real defect) from deliberate cross-reference mentions (entity rosters, finding/methodology bullets citing their source, explicit `>` cross-refs). The previous "any slug linked >1x" heuristic flagged 45 deliberate cross-refs and could never reach exit 0; the refined check surfaced exactly **one genuine defect** — [[liu-2020-wpt-cooperative-uav-mec]] had a full primary bullet under both *Energy efficiency & WPT* and *Classical / convex / optimization-based UAV-MEC*. Gave it one primary home (the convex/optimization section) and a `>` cross-ref note under WPT.

### Gates (batch 2)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primary listings (45 cross-ref mentions reported informationally). **`frontmatter_audit.py`** = 0 errors over 513 pages. `index.md` verified mojibake-free at the byte level after the cross-ref edit.

### Routing to `mec-wiki-synthesizer` (batch 2 — recorded, not filled)

- **Candidate comparison:** the marine multi-access offloading pair [[dai-2023-hybrid-marine-mmwl]] (FDMA-offshore + NOMA-aerial, min-max latency, IEEE TCOMM) and [[dai-2023-hybrid-noma-fdma-marine]] (NOMA-underwater + FDMA-aerial, energy + secrecy, IEEE TNSE) align on a comparable hybrid-multiple-access marine-MEC setup validated vs the LINGO solver — worth a comparison page.
- **Candidate synthesis:** the **diffusion-model-as-optimizer / GDM-for-network-optimization** thread is now dense ([[du-2024-d2sac-aigc-asp-selection]], [[du-2024-gdm-network-optimization-tutorial]], [[fu-2025-otae-inference-lae-batching]], [[ye-2025-aigc-diffusion-contract]], [[peng-2025-drudm-cfg]], survey [[khoramnejad-2025-gai-wireless-optimization-survey]]) — a cross-source synthesis page would consolidate it.
- **Foundational-method finding:** [[fujimoto-2018-td3-actor-critic]] is the TD3 method ancestor of a large in-corpus lineage but has no finding page capturing its three overestimation-bias fixes as the grounding for downstream TD3/MATD3/CLP claims.

### Correctness & consistency audit (Phase B — batch 3/12)

Audited **source-page batch 3** (15 pages, alphabetical guo-2023-mccco-multiuav-5g-offloading → jeong-2018-uav-cloudlet-bit-allocation). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `0973591`; baseline graph **513 nodes / 4455 edges**.

- **Ungrounded-number fix:** [[huang-2023-mu-aec-task-energy]] Findings claimed "one UAV's energy hits zero ~25% earlier than the others; here, all UAVs land within ~5%" — **absent from the parse**, which reports IGD/HV Pareto metrics over a makespan-vs-energy-balancing-index front (Table I, Fig. 5), not any energy-depletion-timing margin. Rewrote to the parse's actual IGD/HV result and marked the timing margin `not in parse`. Also corrected the G₂ energy-balancing-index formula: the page wrote a pairwise `Σ|E_j−E_j'|`, but parse Eq. 13 defines `Σ_j ((TE_j−mean)/ψ)²` (sum of squared normalized deviations from the swarm mean).
- **Evergreen-wording fix:** [[hu-2019-pdd-uav-mec-offloading]] relation note said [[wu-2018-multiuav-minrate-trajectory]] "is curated in this same batch" → rewrote to "is also in the corpus". `process_refs.py` had no "same batch" pattern; **extended the tool** to catch `same batch` / `in this|that|the same batch` process-narration (regression-checked it leaves domain "batch processing" / "in a batch" untouched).
- **Verified clean** (DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim; frontmatter valid; slugs/tags/`related` consistent): guo-2023 (`TWC.2023.3277801`), guo-2024 (`TMC.2023.3311484`), han-2024-ground-satellite (`JSAC.2024.3365901`), han-2024-sagin (`JSAC.2024.3459090`; config K=50/1200 m/N=5/20 km, 80 sats / 5 orbits / 800 km / 85° / 15°, α=0.8 all verbatim), hao-2024-clp (`TMC.2024.3350078`; system gains 78/70/64/58/54, ablation 84/80/63, 600/1500 episodes, 183→141 ms verbatim), hao-2025 (`TWC.2025.3564356`; 10–100 ms coherence-time slot grounded), he-2019 (`TPDS.2019.2938944`), he-2023 (`JIOT.2023.3241087`), hsu-2025 (`TCCN.2025.3629973`), hu-2019-pdd (`JIOT.2018.2878876`; dates→2019), hu-2019-relay (`TWC.2019.2928539`; vol 18(10) 4738–4752 web-consistent with in-parse Oct-2019 current-version), huang-2025-cmop-dispersed (venue/DOI correctly `not in parse`, misattribution note intact), huang-2025-dual-aav (`JIOT.2024.3521977`; SINR 20.75/−39.9, 64 370 J, 43.20%, 50–90% verbatim), jeong-2018 (`TVT.2017.2706308`; dates→2018).

### Toolkit (batch 3)

- Extended **`process_refs.py`** with a `same batch` / `in this|that|the same batch` process-narration pattern (+ README update); caught the leaked phrasing in [[hu-2019-pdd-uav-mec-offloading]] that the prior pattern set missed.

### Gates (batch 3)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on the edited page.

### Routing to `mec-wiki-synthesizer` (batch 3 — coverage gaps, recorded not filled)

- **Candidate finding:** [[huang-2023-mu-aec-task-energy]] is the corpus's canonical **DAG-aware multi-UAV-MEC** source (interdependent-task scheduling + energy balancing) yet has no finding page; pairs with the [[peng-2022-cmop-uav-path-planning]] → [[huang-2025-cmop-dispersed-computing]] CMOP-evolutionary lineage.
- **Candidate synthesis:** the **ground/space FL-over-satellite** thread is now several sources deep ([[han-2024-ground-satellite-fl]], [[han-2024-sagin-fl-handover]], [[zhai-2023-fedleo-decentralized-fl]], [[mao-2025-bcsa-frl]]) — a cross-source synthesis page on satellite/SAGIN federated learning would consolidate it.
- **Candidate comparison:** the early classical/convex single-UAV-MEC offloading sources ([[jeong-2018-uav-cloudlet-bit-allocation]], [[hu-2019-pdd-uav-mec-offloading]], [[hu-2019-uav-relay-edge-computing]], [[zhang-2019-uav-iot-comp-comm]], [[yu-2020-uav-ec-collaborative-offloading]]) align on objective family (energy/delay) and solver (SCA/PDD/AO) and could anchor a methodology or comparison page.

### Correctness & consistency audit (Phase B — batch 4/12)

Audited **source-page batch 4** (15 pages, alphabetical jia-2022-hierarchical-aerial-matching → li-2025-twohop-airground-drl-offloading). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `f37a5ce`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fixes:** [[jia-2025-dro-uav-hap-mec]] carried four ungrounded/incorrect claims against its own parse. (1) Findings "robust solutions cost ~10–20% more energy than nominal" — **not in parse** (Fig. 7 states only qualitatively that CSI errors raise energy vs the ideal-CSI case); rewrote and marked the margin `not in parse`. (2) "WKD beats vanilla **K-means**" — parse Fig. 6 compares WKD vs random-deploy+random-connect (**R&R**), not K-means; corrected. (3) "scales to ~50 UAVs / ~200 users on commodity hardware" — **not in parse**; the evaluated scales are 30 GUs / 6 UAVs (Fig. 3) and M(GUs)=10, N(UAVs)=2–5 (Figs. 4–5), HAP capacity H=10; replaced. (4) BWOA "justified vs greedy and pure **GA**" — parse compares BWOA vs exhaustive-optimal, greedy, and **simulated annealing (SAA)** (Fig. 4); corrected. DOI `TMC.2025.3571023` / year 2025 verified.
- **Ungrounded-number fix:** [[li-2024-robust-bmappo-multiuav-mec]] Findings stated a UE-agent reward ≈ −3.05; parse Fig. 3 converges to ≈ **−3.1**; softened to −3.1 (figure-read, indicative). Config K=20 / M=5 / 1000 m / 3.5–4.5 Mb / 300 episodes / γ=0.98 verified verbatim.
- **Verified clean** (DOI/venue/year against each paper's own parse; headline numbers grounded verbatim; frontmatter valid; slugs/tags/`related` consistent): jia-2022 (`JIOT.2022.3151639`), jiang-2025 (`MCOM.001.2400685`; IAGN/MBCM/CNPC/PC/ACCP/ARDCP verbatim), kang-2023 (`JIOT.2023.3240173`), khoramnejad-2025 (`COMST.2025.3535554`), lee-2024 (`TWC.2023.3342975`; 6.86×/4.18× verbatim from abstract, dates→2024), lei-2024 (`TVT.2024.3388499`), li-2023-secure-marine (`TVT.2022.3231295`; 27.32% + 0.28 W verbatim), li-2024-emodrl (`JSAC.2024.3459029`; "saves 30% handover frequency" verbatim from abstract), li-2024-emssa (`TMC.2023.3298888`), li-2024-rldc (WCNC 2024 DOI grounded via the journal cross-reference; figure values flagged as trends), li-2024-twohop-iort (`JIOT.2024.3393444`), li-2025-stochastic-game (`TGCN.2024.3424449`; five games + NE proof verbatim; figure values flagged trends), li-2025-twohop-airground (`JIOT.2025.3548088`).

### Gates (batch 4)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able, 45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on both edited pages.

### Routing to `mec-wiki-synthesizer` (batch 4 — coverage gaps, recorded not filled)

- **Candidate synthesis:** the **collaborative-beamforming / virtual-antenna-array** thread from the Geng Sun / Jiahui Li group is now dense ([[li-2024-emssa-uav-swarm-vaa]], [[li-2024-emodrl-ground-space-cb]], [[sun-2025-emoppo-vlh-aerial-cb]], [[song-2022-emorl-tcto-uav]], [[zhang-2024-gdmtd3-aerial-secure-cb]]) — a cross-source synthesis on aerial/ground CB and its evolutionary-multi-objective-RL line would consolidate it.
- **Candidate comparison:** the two-hop air-ground IoRT pair from the same Guilin group — [[li-2024-twohop-iort-packet-scheduling]] (packet-queue delay, MADDPG + MADDQN + adaptive PER) and [[li-2025-twohop-airground-drl-offloading]] (partial-offloading delay, MADDPG-IPER + NV-IPPO) — align on a comparable two-hop UAV+HAP setup and could anchor a comparison page.
- **Candidate finding:** [[li-2025-stochastic-game-uav-swarm]] (and its conference precursor [[li-2024-rldc-uav-swarm-clustering]]) is the corpus's canonical **dynamic-clustering UAV-swarm stochastic-game** source with a Nash-equilibrium proof, but has no finding page capturing the RLDC energy-efficiency result.
- **Entity gap:** Ziye Jia recurs as lead/co-author across [[jia-2022-hierarchical-aerial-matching]], [[jia-2025-dro-uav-hap-mec]], and (co-author) [[you-2025-uncertain-maritime-hasac]]; worth an entity page (note possible affiliation drift to confirm, not resolved here).

### Correctness & consistency audit (Phase B — batch 5/12)

Audited **source-page batch 5** (15 pages, alphabetical liang-2024-hmecmop-uav-cb → mao-2024-fso-leo-hierarchical-routing). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `220eaaa`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fixes:** [[liu-2025-haps-uav-maritime-iot]] carried two ungrounded claims against its own parse. (1) Findings "EMOMVO-CGD beats baseline MVO and **NSGA-II** on Pareto-front quality" — **NSGA-II is not in the parse** (the evolutionary benchmarks are MOJS / MOSMA / MOEA/D / conventional MOMVO, plus the C-C-O / P-A-O / P-O / Fixed C-P-P ablations), and the page's own "Why this matters" already noted the paper does not compare against NSGA-II; rewrote the finding to the parse's actual Table II–III result (EMOMVO-CGD best on sum-backhaul-rate f₂; JCCPAPO best on sum-access-rate f₁; similar UAV energy f₃; values indicative). (2) "Backhaul rate scales much faster with UAV altitude than with HAP transmit power once a coverage threshold is crossed — placement, not power, is the bottleneck" — **not in parse**; UAVs are fixed at 100 m altitude with no altitude/power sweep, so the claim was removed. Removed the matching "doesn't head-to-head compare against them [BWOA/NSGA-II]" tail in observation 3 (kept the grounded BWOA note).
- **Verified clean** (DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim; frontmatter valid; slugs/tags/`related` consistent): liang-2024-hmecmop (`JIOT.2023.3315708`; HMECMOP + NP-hard-via-TSP + IMOMVO verbatim; dates→2024), liu-2020-cooperative-power-iot (`TVT.2020.3016840`; dates→2020), liu-2020-wpt (`JIOT.2019.2958975`; SCA/DAI convergence + trajectory-dominance verbatim; dates→2020), liu-2022-maritime-virtualization (`TVT.2022.3141799`; DDPG ">37%" / DQN "31%" vs center-hover baseline verbatim from conclusion), liu-2022-miso (`TVT.2022.3140833`), liu-2024-hatrpo (`TMC.2024.3419915`; 750 vs ~1,400 epochs + Table III energy 13,401/10,261 J + MADDPG 22,319 J verbatim), liu-2026-jppo (no DOI/venue — correctly empty; 21.21% energy-eff @5 UAVs + 76.2% vs NeuralMap @2 UAVs verbatim), lyu-2023 (`JIOT.2023.3348164`; CGTO vs LC/OCG/HOCO/IOJRA/DDPG + ground-disaster scalability grounded), ma-2025 (`TVT.2025.3574783`; P-DQN vs DQN/DDPG/convex + handoff-cost grounded), mach-2017 (`COMST.2017.2682318`; AR latency "up to 88%" / UE energy "up to 93%" correctly attributed to the survey's cited testbed reference), mahboob-2024 (`COMST.2023.3347145`; 1 Tbps peak / µs latency / GEO 35,786 km ~270 ms / LEO ~600 km verbatim; dates→2024), mao-2016 (`JSAC.2016.2611964`; vol 34(12) 3590–3605 web-consistent; LODCO asymptotic optimality + monotonic CPU/power-vs-battery grounded), mao-2017 (`COMST.2017.2745201`), mao-2024-fso (`JSAC.2024.3365880`; dual-layer MEO/LEO + MO-DRL routing + APT-terminal adaptivity grounded; dates→2024).

### Gates (batch 5)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able, 45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on the edited page; graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 5 — coverage gaps, recorded not filled)

- **Candidate synthesis — `hap-roles-in-mec`:** [[liu-2025-haps-uav-maritime-iot]] (HAP-as-backhaul) joins HAP-as-compute ([[peng-2025-drudm-cfg]], [[wang-2026-aerial-marine-msar]]) and HAP-as-relay-with-NOMA ([[hsu-2025-drl-hues-hap-noma]]); all three distinct HAP roles are now in the corpus and warrant a synthesis page (the page itself flags this).
- **Candidate comparison — hybrid-action DRL:** [[ma-2025-pdqn-vehicular-mec]] (P-DQN, value-based) and [[liu-2026-jppo-en-convntm]] (j-PPO, policy-gradient) solve the same discrete-destination + continuous-power/ratio hybrid-action MEC problem from opposite corners; both pages already call for a `j-ppo-vs-pdqn` comparison once a deciding factor emerges.
- **Candidate finding — foundational green-MEC anchor:** [[mao-2016-lodco-eh-mec-offloading]] originates the Lyapunov-per-slot online-offloading pattern that recurs corpus-wide but has no finding page capturing LODCO's asymptotic-optimality + monotonic-structure result as the grounding for downstream Lyapunov-MEC claims.
- **Foundational-survey cluster:** the four MEC/NTN survey anchors ([[mach-2017-mec-survey-architecture]], [[mao-2017-mec-survey-communication]], [[mahboob-2024-ai-ntn-survey]], [[wang-2025-lae-network-survey]]) span terrestrial→aerial→non-terrestrial and could anchor a methodology/synthesis page on how the corpus's MEC scope has migrated skyward.
- **Entity gap:** Yong Zeng recurs (co-author of [[liu-2020-wpt-cooperative-uav-mec]] and lead/co-author across the zeng-2016/2017/2019 trajectory lineage); flagged for an entity page on a later batch that covers those sources.

### Correctness & consistency audit (Phase B — batch 6/12)

Audited **source-page batch 6** (15 pages, alphabetical mao-2024-ntn-hierarchical-caching-cav → pervez-2024-acm-multiuav-mec). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `61e435a`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fixes:** [[nabi-2025-jour-hierarchical-aerial]] carried several claims unsupported by its own parse. (1) Findings cited baselines "DDPG, **MAPPO**, and **SAC-no-PER**" — the parse's learning baselines are GOUA+SAC / GOUA+PPO / GOUA+DDPG plus a GOUA+heuristic (HA); **MAPPO appears only as related work [8], and there is no SAC-no-PER ablation**. Rewrote to the parse's actual baseline set and Fig. 5–13 results. (2) "Load-balancing variance reduction… max-min UAV energy gap shrinks ~30% vs greedy baselines" — **not in parse**; the third objective term (Eq. 25a) is per-UAV **load = computed cycles / compute capacity**, not remaining-energy variance, and no ~30%/greedy metric exists; replaced with the grounded objective + average-per-UAV-load result. (3) "stable associations even under highly **heterogeneous UAV capacities**" — parse states UAVs are **homogeneous** (identical capacity within a scenario); corrected the Method/Findings and added the homogeneous-UAV limitation. (4) Limitation "GUs do not move" **contradicts** the parse ("the GUs are not static; however, the UAVs and HAP positions are static"); rewrote to fixed UAV/HAP positions with mobile GUs and recomputed-each-slot association.
- **Verified clean** (DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim; frontmatter valid; slugs/tags/`related` consistent): mao-2024-ntn-hierarchical-caching-cav (`JSAC.2024.3460063`; WMVC→TSP NP-hard + DM-ACO + MADRL-HCAU + qualitative CHR/delay vs popularity/LIFO grounded; dates→2024), mao-2025-bcsa-frl (`JSAC.2025.3560003`; drop/delay 6.16%/5.95 ms @150, 8.29%/6.08 ms @450, Avg-Task-Burden 20.05%/7.40 ms, Random 40.54%/9.31 ms, ≈5%/≈6 ms ≤50% malicious, CCVM ablation reward <10 vs ~25, optimal reward 26 all verbatim; >51% majority breaks consensus), mao-2025-irs-noma-fl-secrecy (`TCCN.2024.3454256`; max-min secrecy-rate + DDPG + IRS-improves-secrecy grounded, gains correctly indicative; dates→2025), meng-2024-uav-isac-overview (`MWC.131.2200442`; overview, no original numbers — correctly stated), miao-2022-gaglpp-drone-swarm-iiot (`TII.2022.3196392`; GAGLPP global+local split + energy-efficiency result grounded; dates→2023), michailidis-2024-secure-ris-uav-mec-iot (`TCOMM.2024.3372877`; SOP-over-Nakagami-m + Dinkelbach/BCD/bisection + ~57/~60-element thresholds figure-derived/indicative; dates→2024), mozaffari-2017-uav-iot-energy-efficient (`TWC.2017.2751045`; 45% transmit-power + 28% reliability verbatim from abstract; dates→2017), mozaffari-2019-uav-wireless-tutorial (`COMST.2019.2902862`; HAP>17 km, US 122 m/Australia 120 m regulatory table verbatim), niazmand-2025-jopa-dnn-pruning-iiot (`TCCN.2025.3529688`; JOPA/JOPAV1/AGDM + <1% drop + p=0.7 pruning grounded), peng-2020-maddpg-uav-vehicular (`JSAC.2020.3036962`; converges within 200 episodes + higher delay/QoS satisfaction vs SADDPG/random verbatim; dates→2020), peng-2022-cmop-uav-path-planning (`LWC.2022.3149007`; ToP/PPS baselines, 3×10⁴ function evals, I=1 device, IGD/HV Table I verbatim), peng-2024-energy-time-uav-its (`TITS.2024.3395993`; CMOEA/D-CDP + completion-time-difference + service-caching grounded), peng-2025-drudm-cfg (no DOI/venue — correctly empty; only reference-list DOIs present), pervez-2024-acm-multiuav-mec (`TWC.2023.3291692`; potential-game NE + GWF + SCA + ~9 iterations + ~12%/~10% vs two prior methods verbatim; dates→2024).

### Gates (batch 6)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able, 45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on the edited page; graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 6 — coverage gaps, recorded not filled)

- **Candidate finding — synchronization-as-objective:** the "everyone-finish-together" objective recurs across [[peng-2024-energy-time-uav-its]] (pairwise completion-time-difference), [[mao-2025-bcsa-frl]] (FRL round synchronization), and [[xie-2026-uav-multisource-fusion]] (multi-source fusion timing). A [[completion-time-difference]] concept exists but no finding/synthesis ties the cross-source pattern together.
- **Candidate finding — Bomin Mao NWPU non-terrestrial/security cluster:** [[mao-2024-ntn-hierarchical-caching-cav]], [[mao-2025-bcsa-frl]], and [[mao-2025-irs-noma-fl-secrecy]] (all on [[bomin-mao]]'s roster, with [[nei-kato]]) form a coherent LEO/NTN caching+offloading+security thread with no cross-source synthesis page yet.
- **Entity gap:** Walid Saad and Mérouane Debbah recur across [[mozaffari-2017-uav-iot-energy-efficient]] and [[mozaffari-2019-uav-wireless-tutorial]] (and the broader UAV-comms foundational anchors); [[walid-saad]] and [[mohammad-mozaffari]] entity pages exist, but a Debbah page does not — flagged, not created.
- **Entity gap:** Qiang Ye recurs as the cross-cutting author of [[niazmand-2025-jopa-dnn-pruning-iiot]], [[wang-2024-maritime-eh-jcora]], and [[zhang-2025-vnf-sgin-dql]]; worth an entity page on a later pass.

### Correctness & consistency audit (Phase B — batch 7/12)

Audited **source-page batch 7** (15 pages, alphabetical qi-2024-msar-minmax-latency → sun-2024-imssa-uav-secure-cb). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `efe92e4`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fix (cross-corpus count):** [[sun-2024-asap-uav-swarm]] claimed it was "one of only **two** hardware-validated sources in the corpus (with [[shao-2024-drl-antijamming-mec]])". This undercounts: the corpus has at least four hardware-validated sources — ASAP (24 Jetson computers + 5 real UAVs), [[shao-2024-drl-antijamming-mec]] (Raspberry Pi 4B / USRP testbed), [[zhang-2020-response-delay-uav-swarm]] (real DJI M100 UAVs + 5G NR mmWave testbed; itself tagged `hardware-validated` and already enumerating this exact 4-source set), and [[qu-ecoei-uav-swarm]] (airborne Jetson Nano/TX2 proof-of-concept) — and [[sun-2024-imssa-uav-secure-cb]] adds a Raspberry Pi implementation. Rewrote to "one of the few hardware-validated sources … alongside [shao-2024, zhang-2020, qu-ecoei]"; `updated` → 2026-06-01.
- **Verified clean** (DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim; figure-/abstract-derived numbers marked indicative; frontmatter valid; slugs/tags/`related` consistent): qi-2024-msar (`TVT.2024.3384570`; min-max-latency S-UAV/R-UAV, linearization+SCA+BnB; dates→2024), qin-2025-bcuav (`TWC.2025.3582151`; **13.16%↑ sensing rate / 29.47%↓ queue delay vs the strongest baseline PSO** — verbatim, MinerU rendered the digits spaced as `$1 3 . 1 6 \%$`; NT-MASAC/NP-MASAC/MADDPG/PSO baselines + DOA + DPoS/PBFT all grounded; dates→2025), qin-2025-matd3 (`TVT.2025.3552807`; MATD3 + Lyapunov + MTDTO/GSCRA qualitative), qu-ecoei (`MCOM.002.2300129`; year correctly `not in parse`; 0.8→2.9 FPS scaling + 3→2 FPS failover + Jetson PoC verbatim), raivi-2024 (`JIOT.2024.3354950`; 20% / 11.4% / 5.6% / 11.2% / 98% all verbatim incl. Qmix/COMA/HGA baselines; dates→2024), schulman-2017-ppo (arXiv:1707.06347; DOI/venue correctly `not in parse` + web-confirmed note; ε=0.2 clip, 0.82 vs −0.39 surrogate scores; MuJoCo/Atari curves indicative), seid-2021 (`TNSM.2021.3096673`; 38.643% / 55.621% / 58.289% / 85.289% verbatim from abstract+conclusion; dates→2021), shao-2024 (`TMC.2024.3432491`; PER-MATD3, ξ=0.5; Raspberry Pi/USRP testbed magnitudes figure-derived/indicative), song-2022-emorl (`TMC.2022.3208457`; EMORL-TCTO vs NSGA-II/MOEA-D/EDDPG/ETD3/EMORL grounded; pub Sept-2022 / current-version Nov-2023 → 2022 defensible), song-2024-mol (`TMC.2024.3394568`; 39.8% / 2.1% / 15.3% + AAoI 50.6/46.3/52.2/45.9/39.9% + AEC/AC sequences all verbatim; dates→2024), su-2024 (`TWC.2023.3306029`; sensing-aided-PLS CRB/secrecy mutual-benefit qualitative; pub Aug-2023 / current-version Apr-2024 → 2024 defensible), sun-2023-bargain-match (`TMC.2023.3239339`; bargaining+matching, stable/weak-Pareto/polynomial verbatim), sun-2024-active-passive-ris (`TWC.2023.3325813`; PSR 32.8% vs 75.9% / 2.78× / ~0 dB vs −10 dB SINR / −50 dB jammer all verbatim; pub Oct-2023 / current-version Jun-2024 → 2024), sun-2024-asap (`TMC.2024.3427420`; 92.66% / 98.50% / 95.35% / 96.84% / 83.37% all verbatim — see correctness fix above), sun-2024-imssa (`TMC.2023.3273293`; IMSSA vs MOPSO/NSGA-II/MODE/MSSA/IMODACH + Raspberry Pi impl + ISCC-2022 precursor noted; pub May-2023 / current-version Mar-2024 → 2024).

### Gates (batch 7)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 0 unindexed / 0 duplicate primaries (515 catalogue-able, 45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Diagnostics clean on the edited page; graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 7 — coverage gaps, recorded not filled)

- **Candidate finding — hardware-validated reality check:** four corpus sources carry real-hardware validation ([[sun-2024-asap-uav-swarm]], [[shao-2024-drl-antijamming-mec]], [[zhang-2020-response-delay-uav-swarm]], [[qu-ecoei-uav-swarm]]) in a heavily simulation-only literature; a finding/synthesis page consolidating what the testbeds actually demonstrate (and where they diverge from simulation) would be valuable.
- **Candidate synthesis — in-swarm collaborative DL inference:** [[sun-2024-asap-uav-swarm]] (ASAP) and [[qu-ecoei-uav-swarm]] (eCoEI) are the same NUAA group's system + architecture pair on swarm-internal DNN partition/pipeline inference, siblings of [[huang-2025-cmop-dispersed-computing]]; no cross-source synthesis page ties the collaborative-inference thread together.
- **Candidate synthesis — multi-objective evolutionary-vs-RL for UAV trajectory/energy:** [[song-2022-emorl-tcto-uav]] and [[song-2024-mol-aoi-energy]] (Fuhong Song lineage; EMORL/MOL hybrids) sit alongside the pure-CMOP [[peng-2022-cmop-uav-path-planning]] / [[peng-2024-energy-time-uav-its]] and feed the existing [[drl-vs-evolutionary-vs-classical-solvers]] comparison — a focused multi-objective-RL synthesis could deepen that thread.
- **Entity gap:** the Geng Sun / Zemin Sun / Jiahui Li Jilin-University collaborative-beamforming cluster recurs across [[sun-2024-imssa-uav-secure-cb]], [[sun-2023-bargain-match-vec]], [[sun-2024-mvtora-postdisaster-vfc]], [[liu-2024-hatrpo-ucb-cb]] and more; [[geng-sun]] exists but Zemin Sun / Jiahui Li entity pages were not checked-for/created here.

### Correctness & consistency audit (Phase B — batch 8/12)

Audited **source-page batch 8** (15 pages, alphabetical sun-2024-mfris-semantic-antijamming → wang-2025-acbft-uav-consensus). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `986512d`; baseline graph **513 nodes / 4455 edges**.

- **All 15 pages verified clean** — every DOI/venue/year confirmed against the paper's own parse; headline numbers grounded verbatim or marked figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent (no self-references). No ungrounded numbers found this batch.
- **Headline-number cross-check focus — [[wang-2025-acbft-uav-consensus]] "96.2% throughput":** the value is **genuinely grounded** — stated verbatim in the paper's contributions list ("ACBFT achieves an increase in throughput of up to 96.2%", parse L35) and the page already carries a metadata note distinguishing it from the per-node-count Fig. 6 curves (which remain indicative). This is a real paper-stated number, **not** the fabricated-96.2% anti-pattern; left as-is.
- **Verified verbatim / grounded:** sun-2024-mfris (`JSAC.2024.3459028`; MF-RIS + semantic anti-jamming + MO-DSOCP/GPI; benchmarks qualitative; WCSP-Hefei-2024 precursor + dates→2024 grounded), sun-2024-mvtora (`TMC.2024.3350886`; MVTORA game+convex+evolutionary, NP-hard, MSN-2022 precursor in parse), sun-2024-ues (`TVT.2023.3344281`; "doubling of the system's lifetime" verbatim abstract; pub Dec-2023 / current-version 16 May 2024 → 2024 convention correct), sun-2025-emoppo (`TMC.2025.3536093`; EMOPPO-VLH IGD/HV qualitative; the in-paper "MOPPO-PLE" naming-inconsistency note is accurate), sun-2025-tjcct (`TMC.2024.3505155`; two-timescale price-incentive+matching+convex; INFOCOM-2024 precursor DOI `10.1109/INFOCOM52122.2024.10621095` grounded verbatim; dates→2025), tang-2024-iscc (`TWC.2024.3523381`; ISCC + FEEL + BBPO alternating-opt), wang-2019-todetas (`TCYB.2019.2935466`; ToDeTaS two-layer DE+greedy, up to 1000 users), wang-2021-maddpg (`TCCN.2020.3027695`; MADDPG dual-fairness+energy; pub Sept-2020 / current-version Mar-2021 → 2021), wang-2022-cat-rat (`TMC.2021.3059691`; CAT/BCD + RAT/twin-DQN+PER; pub Feb-2021 / current-version Aug-2022 → 2022), wang-2024-blockchain (`TVT.2023.3306740`; consortium DPoS + Stackelberg + SCA; pub Aug-2023 / current-version Jan-2024 → 2024), wang-2024-hfrl (`TMC.2024.3439696`; SHDRLN+DFRL; 2.7 KB/J @100/200/300-ep + 2.4 KB/J @50/100-ep all figure-read from Table II curves and flagged indicative), wang-2024-hybrid-oma-noma (`TVT.2024.3452477`; SCA+Lagrange / DQN mode-selection; pub Aug-2024 → 2024), wang-2024-maritime-eh (`JIOT.2024.3371049`; JCORA Lyapunov drift-plus-penalty + [O(1/V),O(V)] tradeoff + FRA/LRA/PRA/TRA baselines qualitative), wang-2024-twotier (`JIOT.2024.3523527`; Stackelberg+bargaining marine NOMA/FDMA), wang-2025-acbft (`TVT.2025.3548281`; PSO chain-ordering + 96.2% throughput grounded — see above).

### Gates (batch 8)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. No pages required edits this batch, so graph is unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 8 — coverage gaps, recorded not filled)

- **Candidate comparison — convex-baseline-vs-learned-solver UAV-MEC trajectory:** [[wang-2022-cat-rat-fmec-trajectory]] explicitly pairs a convex solver (CAT/BCD) with a DRL solver (RAT/twin-DQN+PER) on the same energy-minimization problem; it aligns closely with [[zhang-2024-uav-task-offloading-ddpg]] (decomposition + DDPG) and [[liu-2022-miso-uav-mec-trajectory]] (alternating optimization) for a focused comparison page.
- **Candidate synthesis — blockchain/trust layer for aerial MEC:** the [[blockchain-on-edge-trust-layer]] thread now spans the consensus-protocol layer ([[wang-2025-acbft-uav-consensus]]), DPoS-secured offloading ([[wang-2024-blockchain-uav-mec-dpos]]), secure UAV-MEC ([[qin-2025-bcuav-masac]]), and FRL aggregation ([[mao-2025-bcsa-frl]]) — dense enough that a synthesis page consolidating the consensus-vs-aggregation-vs-offloading uses would help.
- **Candidate synthesis — game-theoretic maritime offloading:** the Wang/Lin/Ye maritime cluster ([[wang-2024-twotier-satellite-marine]] Stackelberg+bargaining, [[wang-2024-maritime-eh-jcora]] Lyapunov-EH, [[wang-2025-double-edge-samin]] optimization, [[you-2025-uncertain-maritime-hasac]] DRL) covers the same satellite-marine offloading problem with four different solver families — a comparison/synthesis page is warranted.
- **Entity gaps (recurring authors, not created here):** Geng Sun / Zemin Sun anchor four batch-8 Jilin sources ([[sun-2024-mvtora-postdisaster-vfc]], [[sun-2025-emoppo-vlh-aerial-cb]], [[sun-2025-tjcct-twotimescale-uav-mec]], plus co-authorship on [[wang-2024-hfrl-decentralized-navigation]]); [[zemin-sun]] is now referenced by `sun-2025-tjcct` but its entity page was not checked-for here. Kezhi Wang corresponds on both [[wang-2021-maddpg-multiuav-trajectory]] and [[wang-2022-cat-rat-fmec-trajectory]] ([[kezhi-wang]] referenced). Qiang Ye recurs across [[wang-2024-maritime-eh-jcora]] + [[wang-2024-twotier-satellite-marine]] (re-flagged from batch 6).

### Correctness & consistency audit (Phase B — batch 9/12)

Audited **source-page batch 9** (15 pages, alphabetical wang-2025-double-edge-samin → xu-2024-mobile-aigc-survey). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `e5157e2`; baseline graph **513 nodes / 4455 edges**.

- **Correctness/consistency fix — [[wang-acve-constraint-violation-cmop]] self-contradictory metadata.** The page's frontmatter, Citation, and metadata note correctly ground venue/year/DOI **cross-corpus** (`TEVC.2025.3569722`, cited verbatim as reference [8] in [[huang-2025-cmop-dispersed-computing]]), but its Limitations section still claimed the metadata "could not be confirmed … left as `not in parse`". Rewrote Limitations to agree with the grounded note (the paper's own parse has no publication line; metadata grounded cross-corpus).
- **Evergreen-wording fixes — curation ingest-order narration removed corpus-wide.** Six leaks rewritten into statements of fact about the corpus: [[wang-2025-uav-swarm-stackelberg]] ("recurring in the queue … upcoming low-altitude-economy paper" + "upcoming paper #10 (Toward Low-Altitude Economy)" → named links to [[wang-2025-lae-network-survey]]); [[peng-2025-drudm-cfg]] and concept [[hierarchical-aerial-mec]] ("paper #8 SG-MAPG, paper #10 low-altitude economy" → [[bi-2025-sg-mapg]] / [[wang-2025-lae-network-survey]]); concept [[low-altitude-intelligent-network]] (heading "(likely covered by paper #10)" dropped); [[zhang-2025-mcma-task-migration]] ("later in the queue" → track-fit statement); [[jiang-2025-isac-lae-overview]] ("upcoming LAE-MEC papers" → "LAE-MEC work across the corpus"). `updated` bumped to 2026-06-01 on the edited pages.
- **All 15 source pages verified clean** — DOI/venue/year confirmed against each paper's own parse (or correctly `not in parse` with cross-corpus/web-confirmed provenance); headline numbers grounded verbatim or flagged figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent (no self-refs). Spot-checked verbatim: wang-gai-isac 1.03° DoA MSE + NMSE −7.05 vs −2.46 dB @ CR 1/64; wu-2025-iopo 32.8% vs DDPG / 823.32 vs 1225.47 / OPPO 1247.98 vs 1408.36 / 127,966 improved decisions; xu-2018-uav-wpt D≤5.77 m threshold + β₀=−30 dB/H=5 m/P=40 dBm (near-far ~0.19 vs ~0.013 mW figure-derived, indicative). DOIs confirmed: `TVT.2025.3561346`, `TCCN.2025.3601015`, `JIOT.2025.3542025`, `TVT.2025.3595972`, `TCCN.2025.3642113`, `MWC.013.2300485`, `TWC.2017.2789293`, `TWC.2023.3307154`, `TMC.2024.3461719`, `TVT.2025.3604250`, `TWC.2026.3676831`, `TWC.2018.2838134`, `COMST.2024.3353265`. `wang-gai-isac` and `xiang-sac-mapless` carry correct `not in parse` year/venue notes (the latter with an IEEE Xplore doc-8996652 note, no guess).

### Toolkit (batch 9)

- **Extended `process_refs.py`** with a `paper\s+#\d+` pattern — curation ingest-order references ("paper #8", "paper #10") that the prior pattern set missed. It surfaced 4 leaks across 4 pages; all fixed, tool now exits 0. The "queue"/"upcoming" phrasing was deliberately **not** added to the tool (too much domain overlap with priority/task-queue and ordinary "upcoming" usage) and was fixed by hand instead.

### Gates (batch 9)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits (after the fixes). **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. Prose-only edits, no new pages — graph unchanged at **513 nodes / 4455 edges** (API re-pulled post-edit to confirm). Edited pages verified mojibake-free at the byte level (file tools, never PowerShell redirection).

### Routing to `mec-wiki-synthesizer` (batch 9 — coverage gaps, recorded not filled)

- **Candidate comparison — UAV-MEC solver families on the maritime offloading problem:** the Wang/Lin/Ye maritime cluster is now four-deep with distinct solvers — [[wang-2025-double-edge-samin]] (alternating optimization), [[wang-2026-aerial-marine-msar]] (matching + convex + PGD), [[wang-2024-twotier-satellite-marine]] (Stackelberg + bargaining), [[you-2025-uncertain-maritime-hasac]] (HASAC DRL) — reinforcing the batch-8 routing note that a comparison/synthesis page across these solver families is warranted.
- **Candidate comparison — CMOP-evolutionary UAV trajectory lineage:** [[wu-2026-terrain-aware-uav-mec]] (multi-tasking CMOEA, DEM terrain-aware), [[peng-2022-cmop-uav-path-planning]], [[peng-2024-energy-time-uav-its]], [[huang-2025-cmop-dispersed-computing]] (dual-population), and the methods anchor [[wang-acve-constraint-violation-cmop]] (ACVE/DDCo) form a tight constrained-multi-objective family; the existing [[cmop-evolutionary-uav-mec-lineage]] synthesis may be due a re-census as this lineage has grown.
- **Candidate finding — foundational UAV-comm/WPT anchors:** [[wu-2018-multiuav-minrate-trajectory]] (max-min-rate BCD+SCA) and [[xu-2018-uav-wpt-trajectory]] (single-location-hover-optimal sum-energy + successive hover-and-fly) are heavily-cited foundational anchors with no finding page capturing their canonical results.
- **Entity ambiguity (noted, not resolved):** [[xu-2018-uav-wpt-trajectory]] first author **Jie Xu** (Guangdong University of Technology) is flagged on-page as distinct from the existing [[jie-xu]] entity (CUHK-Shenzhen, ISAC); namesake disambiguation is the synthesizer's call. Bin Lin / Qiang Ye (maritime cluster) already have entity pages.

### Correctness & consistency audit (Phase B — batch 10/12)

Audited **source-page batch 10** (15 pages, alphabetical yang-2019-sum-power-uav-mec → zhang-2013-energy-optimal-mcc-stochastic). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `25a9c54`; baseline graph **513 nodes / 4455 edges**.

- **All 15 source pages verified clean** — no corrections needed. DOI/venue/year confirmed against each paper's own parse; headline numbers grounded verbatim or flagged figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent (no self-refs). DOIs confirmed: `TWC.2019.2927313`, `JIOT.2020.2971645`, `TWC.2022.3142365`, `TMC.2024.3406607`, `LWC.2025.3588758`, `TVT.2024.3463420`, `TVT.2025.3581970`, `JIOT.2020.2965898`, `TCOMM.2016.2611512`, `TWC.2017.2688328`, `TWC.2019.2902559`, `JPROC.2019.2952892`, `TVT.2024.3359310`, `TMC.2023.3304988`, `TWC.2013.072513.121842`.
- **Headline numbers spot-checked verbatim against parses:** yang-2019 IACL/SCAFAH/ECC/EXH, fuzzy-c-means initializer, ">1000 W initial → ~420 W after three iterations" (figure-read, flagged indicative on-page); yang-2020 400×400 m / B=1 MHz / H=100 m / N=5 UAVs / K=100 IoT, DRL vs FCFS/SJF/RR; ye-2025 ρ-coefficients (9.7417/0.0978/0.7647/0.5158/3497.8463/0.0307), s^A,min=4, prompt-opt +8%/+2% quality and +22% latency-reduction, 380% correctly attributed to cited work [7]; zeng-2024 participation degree +28.27%/+25.74% (vs RBS/GBS over task size) and +27.84%/+21.14% (over fleet count), convergence ~1500 iter (sharpest first ~800); zhai-2023 FedLEO up-to-41% lower delay / up-to-9.39% higher accuracy; zhang-2013 κ=10⁻¹¹, λ=1.5 → κ/λ=6.67×10⁻¹² (correctly computed). yang-2022 / yang-2024-taco / yao-2025 / you-2025 / yu-2020 / zeng-2016 / zeng-2017 / zeng-2019-rotary / zeng-2019-tutorial verified clean (DOI/method/qualitative results grounded; figure values flagged indicative). Year-disambiguation re-confirmed against publication dates (e.g. yao-2025 LWC pub 15 Jul 2025; zeng-2016 TCOMM date-of-current-version Dec 2016; zeng-2019-rotary current version Apr 2019).

### Gates (batch 10)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. No page edits this batch — graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 10 — coverage gaps, recorded not filled)

- **Candidate findings — foundational Zeng/Zhang UAV-communications anchors:** [[zeng-2016-throughput-relaying]] (UAV mobile relaying + "staircase" water-filling + information-causality), [[zeng-2017-energy-efficient-uav-trajectory]] (first fixed-wing propulsion-energy model + bits/Joule), and [[zeng-2019-rotary-wing-energy-min]] (canonical rotary-wing propulsion model) are heavily-cited foundational anchors with no finding page capturing their canonical results; [[zeng-2019-uav-comm-tutorial-5g]] is a foundational survey similarly without a finding/synthesis tie.
- **Candidate synthesis — propulsion-energy model lineage:** the fixed-wing ([[fixed-wing-propulsion-energy-model]], zeng-2017) vs rotary-wing ([[rotary-wing-propulsion-energy-model]], zeng-2019) split is referenced widely across the energy-aware [[uav-trajectory-control]] sources; a short synthesis tying which corpus sources adopt which model would consolidate a recurring thread.
- **Candidate comparison — LEO-satellite + federated learning:** [[zhai-2023-fedleo-decentralized-fl]] (server-free decentralized aggregation + offloading), [[mao-2025-bcsa-frl]] (blockchain-aggregated FRL), and [[han-2024-sagin-fl-handover]] (FL over SAGIN with handover) form a 3-source FL-over-satellite cluster with no comparison/synthesis page.
- **Candidate comparison — maritime AAV/USV offloading solver families (reinforced):** [[you-2025-uncertain-maritime-hasac]] (Lyapunov → Markov game → heterogeneous-agent SAC) and [[zeng-2024-usv-fleet-collaborative-offloading]] (reverse-auction + ADMM/BCD) add two more solver styles to the Wang/Lin/Ye maritime cluster flagged in batches 8–9; the comparison page remains owed.

### Correctness & consistency audit (Phase B — batch 11/12)

Audited **source-page batch 11** (15 pages, alphabetical zhang-2019-stochastic-offloading-uav-mec → zhao-2025-traj-offload-cache-migration). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `c3bc07c`; baseline graph **513 nodes / 4455 edges**.

- **Correctness fix — [[zhang-2025-mcma-task-migration]]** had two method-level errors vs its parse. (1) The two-stage decision framework was described as "Stage 1 (coarse) discrete migration target — naturally Q-style" + "Stage 2 (fine) offloading + resource allocation"; the parse (Sec. IV-C) states both stages are policy-gradient — **MAPPO** for the discrete migration-assisted *offloading* decision (stage 1) and **MADDPG** for the continuous *resource allocation* (stage 2), neither Q-style. Rewrote TL;DR + Method to match, and folded the base-model-agnostic note (MADDQN/Qmix/MATD3/COMA) into stage 3. (2) Findings cited a "**MADDPG-only** and migration-without-prediction" baseline pair that is **not in the parse**; the actual baselines are heuristics (VE/EO/PO-x/RE), DRL methods (M-DRL, AB-MAPPO, MADDQN, MATD3), and ablations (w/o-{m&p}/{a}/{co}). Rewrote Findings to the grounded baselines + ablations.
- **Correctness fix — [[zhang-2025-ssac-mgi-heterogeneous-uav]]** mischaracterized the MGI mechanism. The page framed MGI as an *inter-UAV* subgame ("when two UAVs are on a near-collision trajectory, one acts as intervention agent and the other non-intervention", with a "symmetric-deflection failure mode" and a "Nash equilibrium guarantees collision avoidance"). The parse (Sec. V-B) defines MGI as a **per-UAV** two-agent game: each UAV is jointly controlled by a stochastic **Standard Agent** (reward-maximizing) and a deterministic **Safety Agent** with a binary gating policy `g(s)` that overrides the standard action when triggered (Eq. 32–34), giving safety guarantees during and after training. Rewrote the MGI description (TL;DR + Method) accordingly. Also corrected Findings — the real baselines are SSAC, STRPO, SCPO, SSAC-MGI-FCFS, and a MANUAL trajectory policy (not "vanilla MASAC and MADDPG"; the "symmetric collision-avoidance heuristics" claim was removed) — and the Limitations (UAVs fly at constant altitude so the trajectory is effectively 2-D, which **is** grounded; parse future work is multi-modal perception + online fine-tuning).
- **Verified clean** (DOI/venue/year against own parse; headline numbers grounded verbatim or flagged figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent, no self-refs): zhang-2019-stochastic-offloading (JIOT.2018.2890133; MAES/MAEU benchmarks + Lyapunov/ADMM/interior-point/CVX verbatim), zhang-2019-uav-iot-comp-comm (TII.2019.2948406; Lagrangian-duality + SCA, "dozen iterations" verbatim), zhang-2020-response-delay-uav-swarm (TVT.2020.2964821; 10%–20% delay decrease + 89.9% packet reduction + 7.84 Mbit→775.9 kbit + DJI M100/28 GHz/64-element testbed all verbatim; hardware-validated), zhang-2024-dlrl-maritime-usv (TVT.2024.3521393; DLRL = outer DDPG + inner Q-learning, PSO-G/PSO-DDQN/DQN baselines verbatim), zhang-2024-gdmtd3-aerial-secure-cb (TMC.2024.3502685; ASCEE-MOP + GDMTD3, four deployment policies + five DRL benchmarks grounded; "GDMDRL" appears verbatim in the parse conclusion), zhang-2024-uav-task-offloading-ddpg (JIOT.2024.3488210; UTOM = KKT + IPSO + DDPG verbatim), zhang-2025-gan-td3-isac-active-ris (JIOT.2025.3527441; GAN-TD3 better/stabler at higher complexity + slower convergence verbatim), zhang-2025-three-tier-maritime-offloading (TVT.2025.3526213; "saves 39.3% of system energy" verbatim, four-subproblem MINLP decomposition grounded), zhang-2025-vnf-sgin-dql (TVT.2024.3454438; <6% earth-surface coverage + VSCP/SR/DDVSC verbatim; dates→2025), zhao-2019-uav-emergency-disasters (MWC.2018.1800160; DOI in parse, venue/vol/pages web-confirmed note intact; AF/DF Nakagami-m + SOCP + SPR D2D grounded), zhao-2022-matd3-multiuav-ec-offloading (TWC.2022.3153316; cooperative MATD3 under CTDE, 2 ECs/30 UEs/400×400 m grounded), zhao-2024-caching-service-placement-uav (JSAC.2024.3460049; average-QoE = cache-hit + delay-shrinkage, Gibbs-sampling + matching-game, "especially when caching/computation limited" verbatim), zhao-2025-traj-offload-cache-migration (TMC.2024.3486995; throughput +10%–45% / scheduling cost −15%–30% / exec time −8%–37% all verbatim; Table I running-times 1000-user PA 3.72 / RSA 0.36 / K-B&B 18.85 / K-GA 9.34 / TSOUD-B&B 18.54 / TSOUD-GA 8.30 verbatim).

### Gates (batch 11)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. The two corrected pages re-validated clean (no diagnostics); edits were prose-only (no new wikilinks) — graph unchanged at **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 11 — coverage gaps, recorded not filled)

- **Candidate findings — Zhao caching/migration anchors:** [[zhao-2024-caching-service-placement-uav]] (average-QoE = cache-hit + delay-shrinkage via Gibbs + matching) and [[zhao-2025-traj-offload-cache-migration]] (the corpus's clearest **computational task caching** + joint trajectory/offload/migration source, with concrete +10–45% / −15–30% / −8–37% results) are headline-rich sources with no finding page.
- **Candidate comparison — UAV task-migration cluster:** [[zhang-2025-mcma-task-migration]] (Informer-prediction + MAPPO/MADDPG two-stage), [[zhao-2025-traj-offload-cache-migration]] (Lyapunov + QCQP/SDR), and the vehicular/aerial migration sources already in the corpus could anchor a task-migration comparison page.
- **Candidate synthesis — safe-RL / collision-aware UAV control:** [[zhang-2025-ssac-mgi-heterogeneous-uav]]'s intervention-based safety layer (Standard + Safety agent) is a distinctive safe-RL pattern with no synthesis tie to the other multi-UAV trajectory-control sources.
- **Entity gaps (recurring authors, not created here):** **Geng Sun / Jiahui Li / Qingqing Wu / Dusit Niyato** anchor [[zhang-2024-gdmtd3-aerial-secure-cb]] (existing entities, rosters not re-tallied here). **Nan Zhao** is first author of both [[zhao-2019-uav-emergency-disasters]] and [[zhao-2022-matd3-multiuav-ec-offloading]] — two corpus sources, no entity page yet (namesake check vs other "Zhao" authors advised). **Chunxiao Jiang** (three-tier maritime) and **Qiang Ye** (VNF-SGIN; re-flagged from batches 6/9) recur across the aerial/space and maritime clusters.

### Correctness & consistency audit (Phase B — batch 12/12, final source batch)

Audited the **final source-page batch 12** (6 pages, alphabetical zheng-2024-recmop-uav-cb → zhu-2025-lycnn-drl-wpt-mec). Phase 0 re-reconciled clean (`curation_status.py --dupes`: **171 raw = 171 curated, 0 uncurated, 0 genuinely-new**); tree clean at `13cf2de`; baseline graph **513 nodes / 4455 edges**. With this batch **all 171 source pages are audited.**

- **Ungrounded-number + baseline fix — [[zhu-2025-lycnn-drl-wpt-mec]]** Findings claimed LyCNN-DRL beats classical MINLP solvers "by orders of magnitude (**sub-millisecond inference** vs seconds per iteration)" — **not in the parse**, which consistently reports execution latency of **~50 ms** (ten-WD) up to **137 ms (0.137 s)** at $N=40$, ≈two orders of magnitude / ~250× below LyCD's **35.184 s** (Table III + conclusion, verbatim). Rewrote to the grounded latency figures and the **97%-of-LyCD-utility** result. Also corrected the DRL-baseline claim: the page said it "beats prior DRL approaches (e.g. the OFDMA-based scheme)", but the OFDMA scheme (ref. [26]) is cited as motivating *prior work*, not benchmarked; the actual DRL baselines are **HA2C** (non-convergent for $N\ge10$) and **LyPG-DRL** (≈47.8% worse $\eta$ at $N=10$, non-convergent for $N\ge30$) — rewrote to these.
- **Evergreen-wording fix — [[zhu-2025-lycnn-drl-wpt-mec]]** cross-link note said "Future curated UAV+WPT papers will fold cleanly into this thread" (process-narration) → rewrote to an evergreen tie to the classical/convex WPT-MEC anchor [[zhou-2018-uav-wireless-powered-mec]] (same computation-rate problem solved without learning). Added the reciprocal `[[zhou-2018-uav-wireless-powered-mec]]` link to `related` (zhou-2018 already linked here — fixed the asymmetry); `updated`→2026-06-01.
- **Verified clean** (DOI/venue/year against own parse; headline numbers grounded verbatim or flagged figure-/abstract-derived indicative; frontmatter valid; slugs/tags/`related` consistent, no self-refs): zheng-2024-recmop-uav-cb (TWC.2024.3400523; ISCC-2022 precursor DOI 10.1109/ISCC55528.2022.9912883 grounded; RECMOP NP-hard/non-convex + IMOGSA with QBL/discrete-update/archive-optimization; results qualitative, Fig. 13 phase-error γ trend figure-derived), zheng-2024-semcom-sec-offloading (JSAC.2024.3365879; ICC-2022 DDINS Workshop precursor DOI 10.1109/ICCWorkshops53468.2022.9814494 grounded; PSFed saves **40.50%** communication + reduces privacy risk **51.43%** verbatim from conclusion+Fig.5/6; CTPS = Rubinstein bargaining + Lagrangian dual decomposition), zhou-2018-uav-wireless-powered-mec (JSAC.2018.2864426; "first work" on UAV-enabled WPT-MEC computation-rate maximization verbatim; partial two-stage + binary three-stage algorithms grounded), zhou-2024-jdl-abs-postdisaster-rescue (TWC.2024.3479709; JDL = Lyapunov + actor-critic with model-based SCA critic; 2.5 km circular-trajectory benchmark + SDQN baseline grounded; figure-read curves flagged indicative), zhu-2024-sensing-comm-doppler-uav-swarm (TVT.2023.3315868; sensing accuracy **>30%** + communication **>20%** verbatim from abstract+conclusion; DE-based min-max-CRLB solver grounded).

### Gates (batch 12)

- **`linkcheck.py`** = NO DANGLING LINKS. **`process_refs.py`** = 0 files / 0 hits. **`index_audit.py`** = 515 catalogue-able, 0 unindexed / 0 duplicate primaries (45 cross-ref mentions informational). **`frontmatter_audit.py`** = 513 pages, 0 errors. The corrected [[zhu-2025-lycnn-drl-wpt-mec]] re-validated clean (no diagnostics); the added reciprocal link does not change graph cardinality (target already present) — graph **513 nodes / 4455 edges**.

### Routing to `mec-wiki-synthesizer` (batch 12 — coverage gaps, recorded not filled)

- **Candidate findings — headline-rich sources with no finding page:** [[zheng-2024-semcom-sec-offloading]] (PSFed saves 40.50% communication / 51.43% privacy risk — the corpus's semantic-communication-for-satellite-offloading anchor) and [[zhu-2024-sensing-comm-doppler-uav-swarm]] (>30% sensing / >20% communication via Doppler-aware DE co-design).
- **Candidate synthesis — WPT-MEC computation-rate thread:** [[zhou-2018-uav-wireless-powered-mec]] (classical/convex, "first work") and [[zhu-2025-lycnn-drl-wpt-mec]] (Lyapunov-guided CNN-DRL) bracket the same WPT-MEC computation-rate problem across the classical→DRL solver divide — a natural synthesis tie, also linking [[qin-2025-bcuav-masac]]'s Lyapunov template.
- **Candidate comparison — collaborative-beamforming MOP solvers:** [[zheng-2024-recmop-uav-cb]] is the only corpus CB source solved with the **gravitational search algorithm** (IMOGSA); it sits alongside [[liang-2024-hmecmop-uav-cb]] (multi-verse optimizer), [[li-2024-emssa-uav-swarm-vaa]] / [[sun-2024-imssa-uav-secure-cb]] (salp-swarm) — a CB-MOP-by-metaheuristic comparison remains owed.
- **Entity gaps (recurring authors, not created here):** **Guhan Zheng** (semcom-SEC) and **Xiaoya Zheng** (RECMOP-CB, Geng-Sun group) are distinct first-author "Zheng" namesakes — neither has an entity page; flag the namesake split if entity pages are minted. **Fuhui Zhou** (zhou-2018) recurs in the WPT-MEC line. The [[geng-sun]] / [[jiahui-li]] / [[shuang-liang]] CB cluster is reinforced by [[zheng-2024-recmop-uav-cb]] (existing entities, rosters not re-tallied here).

### Audit status after batch 12

**All 171 source pages audited (batches 1–12 complete).** Remaining unaudited: the **non-source layer** — concepts (234), entities (71), and the derived pages (findings/synthesis/comparisons/methodology/queries/thesis) beyond the handful already touched (the end-to-end-DRL cluster, [[drl-vs-evolutionary-vs-classical-solvers]], and the two LAE concept pages from batch 9). Subsequent invocations continue from `.curation-out/audit-coverage.md` against that non-source layer.

## 2026-06-01 — Cleanup: duplicate-ingest removal + end-to-end-DRL derived pages converted to English

Repository hygiene pass following the 6-batch curation run.

- **Removed two duplicate MinerU re-ingests.** Deleted the space-named raw folders `Optimizing Spectrum Sharing in UAV Swarms A Stackelberg Game-Based Incentive Mechanism` and `UAV-Enabled Multi-Source Data Fusion in Vehicular Networks A Joint Optimization Approach for Reliab` — duplicate parses (different UUIDs) of papers already curated under their underscore-named originals ([[wang-2025-uav-swarm-stackelberg]], [[xie-2026-uav-multisource-fusion]]). `curation_status.py --dupes` now reports **171 raw = 171 curated, 0 uncurated, 0 duplicates**. No source page referenced the removed folders; `wiki/references/**` still carries stale provenance to those folder names, to be refreshed on the next reference-scout pass.
- **Committed missing raw artifacts** for two already-curated sources ([[wang-2025-sac-tma-mec-dc]], [[wang-2021-maddpg-multiuav-trajectory]]) whose `raw/sources/` parses/PDFs/images had never been version-controlled.
- **Converted an end-to-end-DRL analytical cluster from Chinese to English** and grounded it in the corpus: concepts [[end-to-end-vs-decomposition-in-drl-mec]] and [[action-space-explosion-in-multi-uav-mec]], finding [[no-true-end-to-end-drl-in-corpus]] (grounded in [[drl-vs-evolutionary-vs-classical-solvers]]), and query [[end-to-end-drl-feasibility-large-scale-mec]]. Two accidental chat-save files (a prompt-titled query page and a non-paper "source" page) were removed; their substance is preserved in these four evergreen pages. Indexed in `index.md`; `overview.md` snapshot reconciled to concepts 234 / findings 14 / queries 5. `linkcheck.py` and `process_refs.py` both clean.

## 2026-06-01 — Curation pass (batch 6/6: 2 new sources + audit) — FINAL BATCH, run complete

Sixth and **final** batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers. This run curated **only** the 2 assigned batch-6 folders from `.curation-out/batches.json` (`UAV-Enabled_Collaborative_Beamforming_via_Multi-Agent_Deep_Reinforcement_Learning`, `UAV-Enabled_Wireless_Power_Transfer_Trajectory_Design_and_Energy_Optimization`). Corpus grows **169 → 171 curated sources**. State reconciled clean at `05e61c6` (batch 5) before starting; `curation_status.py --dupes` re-confirmed **2 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched). Confirmed neither paper already had a source page before writing. The stale `.curation-out/batch4-meta.md` artifact was ignored — `batches.json` is authoritative. **After this batch, `curation_status.py --dupes` reports zero genuinely-new uncurated papers — the 6-batch run is complete.**

### New source pages (2)

- [[liu-2024-hatrpo-ucb-cb]] — Saichao Liu, Geng Sun, Jiahui Li, Shuang Liang, Qingqing Wu, Pengfei Wang, Dusit Niyato 2024 (**IEEE TMC**, `10.1109/TMC.2024.3419915`). UAV **collaborative beamforming** (UVAA → remote BSs); multi-objective **UCBMOP** (max transmission rate / min UAV energy) over UAV positions + excitation-current weights, scalarized into a single weighted reward; cast as a Markov game (single-slot episodes) and solved by **HATRPO-UCB** — heterogeneous-agent trust-region MADRL with observation enhancement + agent-specific global state + Beta-distribution policy. Convergence ~750 epochs (vs ~1,400 for MADDPG/IPPO/MAPPO) stated verbatim; Table III energy/rate numbers reported (e.g. first-BS ~13,401 J at ~1.029×10⁶ bps); per-method final-reward magnitudes + phase-error robustness figure-derived (and the convergence figure's extracted table is not fully consistent with the text on final reward — flagged on the page). pub 27 Jun 2024 / current version 5 Nov 2024 → 2024.
- [[xu-2018-uav-wpt-trajectory]] — Jie Xu, Yong Zeng, Rui Zhang 2018 (**IEEE TWC**, `10.1109/TWC.2018.2838134`). Foundational **UAV-enabled WPT** trajectory design: one UAV-mounted ET charges K≥2 ground ERs over a finite period under a max-speed constraint. **Sum-energy** optimum = provably **single-location hovering** (induces near-far fairness gap; closed-form for K=2 with the 2H/√3 = 5.77 m threshold). **Min-energy (max-min)** optimum, speed ignored, = **multi-location hovering** via Lagrange dual; with speed constraint, a **successive hover-and-fly** trajectory (optimal for K=2, asymptotically optimal for K>2) + an **SCP** refinement. Sim setup verbatim (β₀=−30 dB, H=5 m, P=40 dBm); per-ER power magnitudes figure-derived. pub 25 May 2018 / current version 10 Aug 2018 → 2018. GLOBECOM-2017 / APCC-2017 workshop earlier versions noted.

### New concept stubs (2)

- [[trust-region-policy-optimization]] — KL-trust-region policy-gradient with monotonic-improvement guarantee (TRPO) + its sequential-update multi-agent extension (HATRPO); anchors [[liu-2024-hatrpo-ucb-cb]], cross-linked to the [[ppo]]/[[mappo]]/[[heterogeneous-agent-rl]] family.
- [[successive-hover-and-fly-trajectory]] — hover-at-optimal-locations + fly-at-max-speed-between-them UAV trajectory primitive; anchors [[xu-2018-uav-wpt-trajectory]], cross-linked to [[uav-trajectory-control]] / [[wireless-power-transfer]] / SCP ([[alternating-optimization-sdr-sca]]).

All other referenced concepts reused existing slugs (e.g. [[collaborative-beamforming]], [[heterogeneous-agent-rl]], [[beta-policy-drl]], [[stochastic-game]], [[centralized-training-decentralized-execution]], [[rotary-wing-propulsion-energy-model]], [[air-to-ground-channel-model]], [[mappo]], [[maddpg]], [[wireless-power-transfer]], [[rf-energy-harvesting]], [[uav-trajectory-control]], [[fairness-metrics-in-mec]]).

### Entities — 0 new + 6 roster updates

- **Roster updates (HATRPO-UCB):** [[geng-sun]] (15→16), [[jiahui-li]] (12→13), [[shuang-liang]] (6→7), [[qingqing-wu]] (9→10, SJTU-email-matched), [[dusit-niyato]] (19→20) — all +[[liu-2024-hatrpo-ucb-cb]].
- **Roster update (UAV-WPT):** [[yong-zeng]] (5→6) +[[xu-2018-uav-wpt-trajectory]] (NUS; co-author with Jie Xu and Rui Zhang).
- **Deferred / not created** (single corpus source / identity not confirmable from parse, correctness over completeness): Saichao Liu (Jilin University), Pengfei Wang (Dalian University of Technology — already a deferred co-author of [[wang-2024-hfrl-decentralized-navigation]] and the LAE survey), Rui Zhang (NUS). **Jie Xu** (first author of [[xu-2018-uav-wpt-trajectory]]) is at **Guangdong University of Technology** — explicitly **distinct** from the existing [[jie-xu]] entity (CUHK-Shenzhen, ISAC Fellow); treated as a separate identity, **no entity link embedded** for this Jie Xu (flagged on the source page). No author-entity links embedded in source-page bodies beyond the confirmed roster set (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 2 batch-6 folders.
- [[liu-2024-hatrpo-ucb-cb]] (UCBMOP, rate-vs-energy, **HATRPO-UCB trust-region MADRL**) is **distinct** from the other [[geng-sun]]-group CB sources: [[zheng-2024-recmop-uav-cb]] (RECMOP, gravitational search), [[liang-2024-hmecmop-uav-cb]] (multiverse optimizer), [[sun-2025-emoppo-vlh-aerial-cb]] (evolutionary MORL), [[zhang-2024-gdmtd3-aerial-secure-cb]] (diffusion-TD3) — different solver family + objective set — cross-linked via [[collaborative-beamforming-in-aerial-mec]], not duplicated.
- [[xu-2018-uav-wpt-trajectory]] (UAV-WPT energy-delivery trajectory, **no compute/offloading layer**) is **distinct** from the WPT-MEC sources [[zhou-2018-uav-wireless-powered-mec]] (computation-rate max) and [[liu-2020-wpt-cooperative-uav-mec]] (idle-SD cooperative WPT-MEC, SCA/DAI) — it is the WPT-only precursor — cross-linked, not duplicated.

### Audit

- **DOI/venue/year** verified verbatim against each parse: TMC `10.1109/TMC.2024.3419915` (Digital Object Identifier line + supplementary-material DOI both present; dates of publication 27 Jun 2024 / current version 5 Nov 2024 → 2024); TWC `10.1109/TWC.2018.2838134` (Digital Object Identifier line present; dates of publication 25 May 2018 / current version 10 Aug 2018 → 2018). No web lookups needed — both parses carry full metadata.
- **Headline numbers grounded**: HATRPO-UCB ~750-epoch convergence and Table III energy/rate values quoted from the parse text/table; per-method final reward + phase-error curves flagged indicative (figure-derived), with the convergence figure/text inconsistency on final reward noted on the page. UAV-WPT 5.77 m threshold and sim parameters quoted verbatim; per-ER power magnitudes flagged figure-derived.
- **Counts** reconciled: committed corpus is sources 171, concepts 232, entities 71 (no new entity). `corpus_counts.py` reports higher on-disk counts because unrelated untracked pages from a separate in-progress effort sit in the working tree; those are **not** part of this batch and were not staged. `overview.md` snapshot + CB/energy track rows + simulation-only "3 of 171" updated to the committed corpus. `index.md` updated (CB + Energy/WPT source rows; DRL-backbones + UAV-control concept lists).
- **`linkcheck.py`**: no NEW dangling links introduced by this batch (see run result below).
- **`process_refs.py`**: clean — no batch/pass process-narration leaked into any page except this log.

## 2026-06-01 — Curation pass (batch 5/6: 7 new sources + audit)

Fifth batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-5 folders from `.curation-out/batches.json`; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **162 → 169 curated sources**. (Confirmed none of the 7 already had a source page before writing.) State reconciled clean at `42c0c25` (batch 4) before starting; `curation_status.py --dupes` re-confirmed **9 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched), leaving **batch 6 = 2 papers** after this run. The stale `.curation-out/batch4-meta.md` artifact was ignored — `batches.json` is authoritative.

### New source pages (7)

- [[zheng-2024-recmop-uav-cb]] — Xiaoya Zheng, Geng Sun, Jiahui Li, Shuang Liang, Qingqing Wu, Minghao Yin, Dusit Niyato, Victor C. M. Leung 2024 (**IEEE TWC**, `10.1109/TWC.2024.3400523`). UAV **collaborative beamforming** (UVAA relay → remote BSs) in emergency comms; multi-objective **RECMOP** (max-min BS SNR / min-max average AU SNR / min propulsion energy) over UAV locations + excitation-current weights; NP-hard non-convex mixed-variable; solved by **improved multi-objective gravitational search algorithm (IMOGSA)** (QBL + discrete-update + NSGA-II archive). "Outperforms benchmarks at both scales" + robustness under phase-error stated; magnitudes figure-derived. pub 21 May 2024 / current version 11 Oct 2024 → 2024. ISCC-2022 earlier version noted.
- [[mahboob-2024-ai-ntn-survey]] — Shadab Mahboob, Lingjia Liu 2024 (**IEEE COMST**, `10.1109/COMST.2023.3347145`). **Survey** of AI-empowered satellite-based NTN for 6G; NTN/AI background + AI-per-challenge research-thrust taxonomy (channel/Doppler estimation, beam/resource management, handover, spectrum sharing, routing, slicing, offloading, security) + distributed-learning paradigms (FL / decentralized / split) + O-RAN/RIC/SDR implementation. No original numbers (survey). pub 19 Jan 2024 / current version 23 May 2024 → 2024.
- [[zheng-2024-semcom-sec-offloading]] — Guhan Zheng, Qiang Ni, Keivan Navaie, Haris Pervaiz 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3365879`). **Semantic communication** in a LEO **satellite-borne edge cloud** (SemCom-SEC) for offloading; coders on TSTs + satellites; **PSFed** (adaptive pruning-split federated learning, coder components intact) for in-maintenance coder updating; **CTPS** (Rubinstein bargaining game → complete-info MINLP → Lagrangian dual decomposition) for in-service delay/energy under privacy + fairness. Verbatim: PSFed **saves 40.50% communication** + **reduces privacy risk 51.43%**, accuracy/convergence ~unchanged. pub 26 Feb 2024 / current version 9 May 2024 → 2024. ICC-2022 DDINS earlier version noted.
- [[zeng-2016-throughput-relaying]] — Yong Zeng, Rui Zhang, Teng Joon Lim 2016 (**IEEE TCOMM**, `10.1109/TCOMM.2016.2611512`). Foundational **UAV mobile-relaying** throughput maximization over relay trajectory + source/relay power under mobility + **information-causality** constraints; optimal power = **"staircase" water-filling** (non-increasing source / non-decreasing relay level); trajectory via SCA; closed-form free-endpoint solution (unidirectional max-speed or stationary). "Significant throughput gain vs static relaying" stated; curves figure-derived. pub 20 Sep 2016 / current version 15 Dec 2016 → 2016.
- [[zhao-2019-uav-emergency-disasters]] — Nan Zhao, Weidang Lu, Min Sheng, Yunfei Chen, Jie Tang, F. Richard Yu, Kai-Kit Wong 2019 (`10.1109/MWC.2018.1800160`). Magazine **framework** for UAV-assisted emergency networks in disasters: (1) joint trajectory + scheduling with surviving BSs; (2) SOCP transceiver + multihop **D2D** (SPR, PPP outage) coverage extension; (3) multihop UAV relaying (AF/DF, Nakagami-m) connecting disaster area to outside; NOMA discussion for single-antenna UAVs. **Metadata caveat:** parse carries the **DOI only** — year/venue/volume/pages = `not in parse`, **web-confirmed via dblp** (IEEE Wireless Communications, vol. 26, no. 1, pp. 45–51, 2019) and flagged on the page.
- [[dai-2023-hybrid-noma-fdma-marine]] — Minghui Dai, Yuan Wu, Liping Qian, Zhou Su, Bin Lin, Nan Chen 2023 (**IEEE TNSE**, `10.1109/TNSE.2022.3205303`). Two-segment **marine multi-access offloading**: USNs upload to USV via **NOMA** (underwater acoustic), USV offloads to hovering **UAVs** via **FDMA** (RF), with an eavesdropper; minimize **total USN+USV energy** over USN uploading time + USV offloading decision/time + **secrecy provisioning**; layered top/sub-problem + 2-D line search. Validated vs **LINGO** global optimum (gap stated qualitatively → figure-derived). pub 9 Sep 2022 / current version 6 Jan 2023 → 2023.
- [[hu-2019-uav-relay-edge-computing]] — Xiaoyan Hu, Kai-Kit Wong, Kun Yang, Zhongbin Zheng 2019 (**IEEE TWC**, `10.1109/TWC.2019.2928539`). First UAV-MEC where one cellular-connected UAV is an **MEC server AND a relay** to the AP simultaneously; minimize **weighted-sum energy** of UAV + UEs over computation scheduling + bandwidth allocation + trajectory under **information-causality**; alternating optimization (closed-form Lagrange-dual scheduling/bandwidth + SCA trajectory), guaranteed convergence. "Significant + more stable gains vs preset-traj/offload-only/equal-BW/local" stated; magnitudes figure-derived. pub 19 Jul 2019 / current version 9 Oct 2019 → 2019.

### New concept stubs (3)

- [[gravitational-search-algorithm]] — gravity-law population metaheuristic; anchors [[zheng-2024-recmop-uav-cb]]'s IMOGSA; cross-linked from the corpus's other mixed-variable aerial-MOP metaheuristics ([[multi-verse-optimizer]], [[salp-swarm-algorithm]], [[whale-optimization-algorithm]]).
- [[uav-mobile-relaying]] — UAV-borne high-mobility relay with trajectory as a design variable; anchors [[zeng-2016-throughput-relaying]], reused by [[hu-2019-uav-relay-edge-computing]] and [[zhao-2019-uav-emergency-disasters]].
- [[information-causality-constraint]] — forward-only-received-data buffering constraint; the information-domain analogue of energy-causality; anchors [[zeng-2016-throughput-relaying]] (staircase water-filling) and [[hu-2019-uav-relay-edge-computing]].

All other referenced concepts reused existing slugs (e.g. [[collaborative-beamforming]], [[multi-objective-reinforcement-learning]], [[rotary-wing-propulsion-energy-model]], [[mixed-integer-nonlinear-programming]], [[uav-data-collection]], [[uav-trajectory-control]], [[alternating-optimization-sdr-sca]], [[energy-latency-tradeoff]], [[non-terrestrial-network]], [[space-air-ground-integrated-network]], [[leo-satellite-edge-computing]], [[seamless-handover]], [[federated-learning]], [[decentralized-federated-learning]], [[network-slicing]], [[task-offloading]], [[semantic-communication]], [[bargaining-game]], [[privacy-sensitive-data-partitioning]], [[dnn-model-partition]], [[mobile-edge-computing]], [[maritime-mec]], [[noma]], [[two-stage-decomposition]], [[physical-layer-security]], [[multi-uav-assisted-mec]], [[post-disaster-mec]], [[air-to-ground-channel-model]]).

### Entities — 1 new + 9 roster updates

- **New:** [[yong-zeng]] — NUS UAV-communications/trajectory-optimization anchor; now at **5** sources ([[zeng-2016-throughput-relaying]] + the already-curated [[zeng-2017-energy-efficient-uav-trajectory]], [[zeng-2019-rotary-wing-energy-min]], [[zeng-2019-uav-comm-tutorial-5g]], [[wu-2018-multiuav-minrate-trajectory]]) → single identity (NUS), created rather than deferred.
- **Roster updates (RECMOP):** [[geng-sun]] (14→15), [[jiahui-li]] (11→12), [[shuang-liang]] (5→6), [[qingqing-wu]] (8→9, SJTU-email-matched), [[victor-c-m-leung]] (5→6), [[dusit-niyato]] (18→19) — all +[[zheng-2024-recmop-uav-cb]].
- **Roster updates (marine NOMA/FDMA):** [[minghui-dai]] (3→4), [[yuan-wu]] (9→10), [[liping-qian]] (3→4), [[zhou-su]] (2→3), [[bin-lin]] (8→9) — all +[[dai-2023-hybrid-noma-fdma-marine]].
- **Deferred / not created** (single corpus source each / identity not confirmable from parse, correctness over completeness): Xiaoya Zheng, Minghao Yin (Northeast Normal Univ.; 2 sources but minted via cluster leads); Rui Zhang + Teng Joon Lim (NUS); Shadab Mahboob + Lingjia Liu (Virginia Tech); Guhan Zheng + Qiang Ni + Keivan Navaie (Lancaster) + Haris Pervaiz (Essex); Xiaoyan Hu (UCL) + Kai-Kit Wong + Kun Yang + Zhongbin Zheng; Nan Zhao + Weidang Lu + Min Sheng + Yunfei Chen + Jie Tang + F. Richard Yu; Nan Chen (Tennessee Tech). No author-entity links embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 7 batch-5 folders.
- [[dai-2023-hybrid-noma-fdma-marine]] (**IEEE TNSE**, **total-energy minimization + secrecy provisioning**, NOMA-underwater (USN→USV) + FDMA-aerial (USV→UAV)) is **distinct** from the existing same-lead-author [[dai-2023-hybrid-marine-mmwl]] (**IEEE TCOMM**, **max-workloads-latency MMWL**, FDMA-offshore + NOMA-aerial) — different venue, objective, and access-mode assignment — cross-linked, not duplicated.
- [[hu-2019-uav-relay-edge-computing]] (first author **Xiaoyan Hu**, UCL; UAV as MEC-server + relay, weighted-sum-energy, info-causality + SCA) is **distinct** from the existing [[hu-2019-pdd-uav-mec-offloading]] (first author **Qiyu Hu**, Zhejiang University; single-UAV min-max-delay, penalty-dual-decomposition) — different author + objective + method — cross-linked, not duplicated.
- [[zheng-2024-recmop-uav-cb]] (RECMOP, AU-interference objective, IMOGSA gravitational search) is **distinct** from the other [[geng-sun]]-group CB sources [[liang-2024-hmecmop-uav-cb]] (hovering-vs-motion energy, multiverse optimizer), [[li-2024-emssa-uav-swarm-vaa]]/[[sun-2024-imssa-uav-secure-cb]] (salp-swarm) — different objective set + solver — cross-linked, not duplicated.
- [[zheng-2024-semcom-sec-offloading]] (Guhan Zheng; SemCom + satellite-borne edge cloud + PSFed + bargaining) is **distinct** from [[zheng-2024-recmop-uav-cb]] (Xiaoya Zheng; CB) despite the shared romanized surname — different author/affiliation/topic — and from the satellite-offloading sources [[cheng-2025-dos-satellite-edge-computing]] / [[wang-2025-double-edge-samin]] — cross-linked, not duplicated.
- [[zeng-2016-throughput-relaying]] is the method-ancestor of [[hu-2019-uav-relay-edge-computing]] (shared info-causality + SCA), and a communications-framing sibling of [[zeng-2017-energy-efficient-uav-trajectory]] / [[wu-2018-multiuav-minrate-trajectory]] — not duplicates.
- [[zhao-2019-uav-emergency-disasters]] (magazine emergency-network framework) is **distinct** from the optimization-heavy post-disaster sources [[zhou-2024-jdl-abs-postdisaster-rescue]] / [[raivi-2024-jdaco-postdisaster-iot]] — cross-linked, not duplicated.
- [[mahboob-2024-ai-ntn-survey]] is a high-level AI-NTN survey, complementary to (not duplicative of) the application-specific NTN sources.

### Audit (correctness-first)

- **DOI / venue / year** — 6 of 7 papers carry an explicit `Digital Object Identifier` line, **verified verbatim** against the parse (TWC `10.1109/TWC.2024.3400523`; COMST `10.1109/COMST.2023.3347145`; JSAC `10.1109/JSAC.2024.3365879`; TCOMM `10.1109/TCOMM.2016.2611512`; TNSE `10.1109/TNSE.2022.3205303`; TWC `10.1109/TWC.2019.2928539`); years follow date-of-current-version (both dates recorded). **[[zhao-2019-uav-emergency-disasters]]** is the only partial-metadata case — the parse has the **DOI** (`10.1109/MWC.2018.1800160`) but no publication date/venue/volume; year/venue/volume/pages **web-confirmed via dblp** (IEEE Wireless Communications, 26(1):45–51, 2019) and explicitly flagged on the page.
- **Grounded headline claims only:** SemCom-SEC −40.50% comm / −51.43% privacy risk (conclusion, verbatim); all RECMOP / relaying / marine / Hu-relay-edge comparative magnitudes stated qualitatively as the papers state them, with figure-derived numbers flagged indicative; the survey carries no original numbers.
- **Wikilink integrity:** `linkcheck.py` = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this batch (7 sources + 3 concepts + 1 entity).
- **Process-narration:** `process_refs.py` = **0 files / 0 hits** outside `log.md`; sources / concepts / entities / index / overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated (no diagnostics) on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 3 new concepts + 1 new entity + index/overview.
- **Counts reconciled** (`corpus_counts.py`): **169 sources / 230 concepts / 70 author entities (+[[pytorch]] = 71 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis / 2 references. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-5 folders were curated; **1 batch (2 papers) remains** for a separate invocation (batch6).

## 2026-06-01 — Curation pass (batch 4/6: 7 new sources + audit)

Fourth batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-4 folders from `.curation-out/batches.json`; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **155 → 162 curated sources**. (Confirmed none of the 7 already had a source page before writing.) State reconciled clean at `0b849b2` (batch 3) before starting; `curation_status.py --dupes` re-confirmed **16 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched). The stale `.curation-out/batch4-meta.md` artifact (a 43-folder list from an earlier planning session) does **not** match the current `batches.json` batch-4 allowlist and was ignored — `batches.json` is authoritative.

### New source pages (7)

- [[jeong-2018-uav-cloudlet-bit-allocation]] — Seongah Jeong, Osvaldo Simeone, Joonhyuk Kang 2018 (**IEEE TVT**, `10.1109/TVT.2017.2706308`). Early **UAV-mounted cloudlet** MEC; minimize total mobile energy under latency + UAV-energy budget by jointly optimizing **bit allocation** (uplink / cloudlet-compute / downlink) + UAV trajectory; FDD with orthogonal access or **NOMA**; two flying-energy models (velocity-only / +acceleration); non-convex solved by **SCA** (converges to local optimum). Headline energy-savings-vs-local/partial stated qualitatively (magnitudes are figure-derived). pub 19 May 2017 / current version 15 Mar 2018 → 2018.
- [[mozaffari-2017-uav-iot-energy-efficient]] — Mohammad Mozaffari, Walid Saad, Mehdi Bennis, Mérouane Debbah 2017 (**IEEE TWC**, `10.1109/TWC.2017.2751045`). Energy-efficient uplink **IoT data collection** via multiple mobile UAVs; joint 3D placement + device-UAV association + uplink power control (iterative decomposition) + closed-form **update-times** + energy-minimizing 3D trajectory; Beta-distribution (bursty) + periodic activation models; constrained K-means channel assignment. Abstract (verbatim): **−45%** device total transmit power and up to **+28%** reliability vs stationary ABS; update-vs-mobility-vs-power tradeoff. pub 15 Sep 2017 / current version 9 Nov 2017 → 2017.
- [[liang-2024-hmecmop-uav-cb]] — Shuang Liang, Minghao Yin, Geng Sun, Jiahui Li 2024 (**IEEE IoT-J**, `10.1109/JIOT.2023.3315708`). UAV-swarm **collaborative beamforming** (virtual antenna array) to remote BSs; **HMECMOP** simultaneously minimizes total hovering + motion energy over UAV positions + excitation-current weights + BS-communication order; proven NP-hard hybrid (continuous+discrete) MOP; solved by **improved multiobjective multiverse optimizer (IMOMVO)** (vertical-horizontal renewal + nearest-neighbor procedure). Comparative gains qualitative (figure-derived). pub 15 Sep 2023 / current version 6 Feb 2024 → 2024.
- [[mao-2024-fso-leo-hierarchical-routing]] — Bomin Mao, Xueming Zhou, Jiajia Liu, Nei Kato 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3365880`). Hierarchical **routing** for ultra-dense **free-space-optical (FSO) LEO** constellations; dual-layer MEO/LEO architecture + region division (MEO controllers compute paths, LEO forwards) + multi-objective DRL utility routing for differentiated QoS (latency / packet-loss / throughput) + reward-monotonicity **cooperative mechanism**; **adaptive to APT-terminal count** (hence FSO-link count). Networking/routing, not offloading. "Outperforms benchmarks across QoS metrics" stated qualitatively (magnitudes figure-derived). pub 19 Feb 2024 / current version 9 May 2024 → 2024.
- [[sun-2024-ues-video-analytics-disaster]] — Hui Sun, Xiuye Zhang, Bo Zhang, Kewei Sha, Weisong Shi 2024 (**IEEE TVT**, `10.1109/TVT.2023.3344281`). **Battery-aware** UAV-mounted-edge-server (UES) collaborative **video analytics** for **disaster rescue**; variable-length time slots (fly-then-hover); nested optimizations — **differential-evolution** per-slot offloading (0–1 decision + channel/resource allocation) + **DDQN** trajectory planning (MDP) — targeting the smart-camera-network **lifetime**. Headline: **doubles** the system lifetime; offloading "high accuracy / fast convergence vs 4 SOTA" (stated; curves figure-derived). pub 19 Dec 2023 / current version 16 May 2024 → 2024.
- [[mao-2025-irs-noma-fl-secrecy]] — Bomin Mao, Yingying Wu, Jiajia Liu, Hongzhi Guo, Jiadai Wang, Nei Kato 2025 (**IEEE TCCN**, `10.1109/TCCN.2024.3454256`). **IRS-assisted** physical-layer security for the **NOMA-based federated-learning** model-uploading phase; secrecy rate = device→BS minus device→Eve rate; **max-min secrecy-rate** over device transmit power + IRS phase shift under a power budget; non-convex coupled problem solved with **DDPG** (actor-critic + target nets + replay). "IRS improves secrecy rate" stated qualitatively (magnitudes figure-derived). pub 4 Sep 2024 / current version 9 Apr 2025 → 2025.
- [[schulman-2017-ppo]] — John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov 2017 (OpenAI). **Origin paper for PPO**; **clipped surrogate objective** ($\epsilon{=}0.2$) enabling multi-epoch first-order minibatch updates with TRPO-like stability; adaptive-KL variant included as a (worse) baseline; combined CLIP+VF+S loss; truncated-GAE actor-critic algorithm. Results: clipping-$\epsilon$=0.2 best (0.82 norm. score, Table 1); beats TRPO/A2C/CEM/vanilla-PG on MuJoCo (Fig. 3, figure-derived); Atari wins per Table 2. **Metadata caveat:** the parse carries **no DOI / venue / date** line — DOI/venue = `not in parse`; arXiv:1707.06347 (2017) **web-confirmed** and flagged as such on the page. Grounds the [[ppo]] concept like [[fujimoto-2018-td3-actor-critic]] grounds TD3.

### New concept stubs (1)

- [[free-space-optical-isl]] — laser inter-satellite link (high bandwidth, but APT-terminal- and visibility-limited and dynamic); anchors [[mao-2024-fso-leo-hierarchical-routing]] and backlinked from [[leo-satellite-edge-computing]].

All other referenced concepts reused existing slugs (e.g. [[ppo]], [[gae]], [[j-ppo]], [[mappo]], [[mobile-edge-computing]], [[uav-trajectory-control]], [[alternating-optimization-sdr-sca]], [[noma]], [[energy-latency-tradeoff]], [[rotary-wing-propulsion-energy-model]], [[fixed-wing-propulsion-energy-model]], [[drone-cell-3d-placement]], [[air-to-ground-channel-model]], [[uav-data-collection]], [[weighted-kmeans-uav-deployment]], [[collaborative-beamforming]], [[multi-verse-optimizer]], [[salp-swarm-algorithm]], [[mixed-integer-nonlinear-programming]], [[leo-satellite-edge-computing]], [[non-terrestrial-network]], [[walker-star-constellation]], [[multi-objective-reinforcement-learning]], [[dynamic-qos-constraints]], [[post-disaster-mec]], [[video-analytics-offloading]], [[ddqn]], [[differential-evolution]], [[task-offloading]], [[federated-learning]], [[intelligent-reflecting-surface]], [[physical-layer-security]], [[ddpg]]).

### Entities — 2 new + 6 roster updates

- **New:** [[mohammad-mozaffari]] + [[walid-saad]] — the Virginia Tech (Wireless@VT) UAV-communications cluster; each anchors **2** sources ([[mozaffari-2017-uav-iot-energy-efficient]] + the already-curated tutorial [[mozaffari-2019-uav-wireless-tutorial]]), affiliation-verified (identical Virginia Tech / Wireless@VT and email across both parses; Mozaffari-Saad-Bennis-Debbah roster stable) → single identity, created rather than deferred. The tutorial source was bumped to backlink both entities + the 2017 IoT paper.
- **Roster updates:** [[geng-sun]] (13→14), [[jiahui-li]] (10→11), [[shuang-liang]] (4→5, now lead author of the CB energy-MOP) — all +[[liang-2024-hmecmop-uav-cb]]; [[bomin-mao]] (2→4, +FSO routing +IRS-FL-secrecy), [[jiajia-liu]] (3→5), [[nei-kato]] (2→4) — +both new Mao papers; [[hongzhi-guo]] (3→4) + [[jiadai-wang]] (2→3) — +[[mao-2025-irs-noma-fl-secrecy]].
- **Deferred / not created** (single corpus source each / identity not confirmable from parse, correctness over completeness): Seongah Jeong + Osvaldo Simeone + Joonhyuk Kang (Harvard / King's College London / KAIST); Mehdi Bennis + Mérouane Debbah (Oulu / Huawei-CentraleSupélec — co-authors on the two Mozaffari papers but not minted this batch as their wiki-presence is via the cluster leads); Minghao Yin (Northeast Normal Univ.); Xueming Zhou (NWPU); Hui Sun + Xiuye Zhang + Bo Zhang + Kewei Sha + Weisong Shi (Anhui Univ. / Univ. of Houston-Clear Lake / Wayne State); Yingying Wu (NWPU); John Schulman + Filip Wolski + Prafulla Dhariwal + Alec Radford + Oleg Klimov (OpenAI). No author-entity links embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 7 batch-4 folders.
- [[jeong-2018-uav-cloudlet-bit-allocation]] (UAV *moving cloudlet*, bit-allocation+trajectory, SCA) is **distinct** from the other classical/convex UAV-MEC sources [[zhang-2019-uav-iot-comp-comm]] and the trajectory-optimization line — cross-linked, not duplicated. It is also a *compute-offloading* paper, unlike the *placement/relay/coverage* role surveyed in [[mozaffari-2019-uav-wireless-tutorial]].
- [[mozaffari-2017-uav-iot-energy-efficient]] (3D placement + mobility + uplink-power for IoT collection) is **distinct** from the same-group tutorial [[mozaffari-2019-uav-wireless-tutorial]] and from [[bor-yaliniz-2016-3d-abs-placement]] (coverage-max placement) — same air-to-ground channel family, different objective — cross-linked, not duplicated.
- [[liang-2024-hmecmop-uav-cb]] (hovering-vs-motion-energy MOP, multiverse optimizer) is **distinct** from the other CB sources [[li-2024-emssa-uav-swarm-vaa]] (salp-swarm, time/eavesdropper/energy) and [[sun-2025-emoppo-vlh-aerial-cb]] (evolutionary multi-objective PPO) — different objective + optimizer — cross-linked, not duplicated.
- [[mao-2024-fso-leo-hierarchical-routing]] (LEO routing, networking) is **distinct** from [[mao-2024-ntn-hierarchical-caching-cav]] (NTN caching) and [[lee-2024-dho-leo-handover]] (handover protocol) — same NWPU group / overlapping authors, different problem — cross-linked, not duplicated.
- [[sun-2024-ues-video-analytics-disaster]] (battery-aware video-analytics, DE+DDQN) is **distinct** from [[bao-2025-ddpg-video-offloading]] (UAV+HAP video offload, transcoding, DDPG) and the post-disaster sources — cross-linked, not duplicated.
- [[mao-2025-irs-noma-fl-secrecy]] (IRS PLS for FL aggregation, DDPG) is **distinct** from [[mao-2025-bcsa-frl]] (blockchain-secured FRL) and the ISAC-PLS sources — cross-linked, not duplicated.
- [[schulman-2017-ppo]] is the **method-ancestor** PPO paper, complementary to [[fujimoto-2018-td3-actor-critic]] (TD3) — both foundational-DRL-method anchors, not duplicates.

### Audit (correctness-first)

- **DOI / venue / year** — the 6 IEEE papers each carry an explicit `Digital Object Identifier` line, **verified verbatim** against the parse (TVT `10.1109/TVT.2017.2706308`; TWC `10.1109/TWC.2017.2751045`; IoT-J `10.1109/JIOT.2023.3315708`; JSAC `10.1109/JSAC.2024.3365880`; TVT `10.1109/TVT.2023.3344281`; TCCN `10.1109/TCCN.2024.3454256`); years follow date-of-current-version (both dates recorded in each citation). **[[schulman-2017-ppo]]** is the only `not in parse` metadata case — no DOI/venue/date in the parse; arXiv:1707.06347 (2017) web-confirmed and explicitly flagged on the page.
- **Grounded headline claims only:** Mozaffari-2017 −45% tx-power / +28% reliability (abstract verbatim); PPO clipping-0.2 = 0.82 (Table 1), Atari wins (Table 2), MuJoCo superiority (Fig. 3, flagged figure-derived); Sun-2024 "doubles lifetime" (abstract); Jeong/Liang/Mao-FSO/Mao-secrecy comparative magnitudes stated qualitatively as the papers state them, with figure-derived numbers flagged indicative.
- **Wikilink integrity:** `linkcheck.py` = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this batch (7 sources + 1 concept + 2 entities).
- **Process-narration:** `process_refs.py` = **0 files / 0 hits** outside `log.md`; sources / concepts / entities / index / overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated (no diagnostics) on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the new concept + 2 new entities.
- **Counts reconciled** (`corpus_counts.py`): **162 sources / 227 concepts / 69 author entities (+[[pytorch]] = 70 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-4 folders were curated; **2 batches (9 papers) remain** for separate invocations (batch5 7 / batch6 2).

## 2026-06-01 — Curation pass (batch 3/6: 7 new sources + audit)

Third batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-3 folders from `.curation-out/batches.json`; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **148 → 155 curated sources**. (Confirmed none of the 7 already had a source page before writing.) State reconciled clean at `2e0acc9` (batch 2) before starting; `curation_status.py --dupes` re-confirmed **23 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched).

### New source pages (7)

- [[yang-2019-sum-power-uav-mec]] — Zhaohui Yang, Cunhua Pan, Kezhi Wang, Mohammad Shikh-Bahaei 2019 (**IEEE TWC**, `10.1109/TWC.2019.2927313`). Multi-UAV-MEC **sum-power minimization** of UEs + UAVs (incl. UAV propulsion power) over user association + power control + computation-capacity allocation + UAV location/altitude/beamwidth; iterative three-subproblem algorithm — compressive-sensing $\ell_0$ association + closed-form capacity + 1-D location search — with a fuzzy-c-means feasibility initializer. Findings: IACL beats SCAFAH/ECC, approaches EXH; converges ~3 iters, init >1000 W → ~420 W (figure-read, flagged indicative). pub 16 Jul 2019 / current version 10 Sep 2019 → 2019.
- [[mach-2017-mec-survey-architecture]] — Pavel Mach, Zdenek Becvar 2017 (**IEEE COMST**, `10.1109/COMST.2017.2682318`). The **architecture + computation-offloading** MEC survey: MCC-vs-edge comparison, integrated architectures (SCC/MMC/MobiScud/FMC/CONCERT) + ETSI standardization, and the three offloading research areas (decision / resource allocation / mobility management). Survey, no original numbers. pub 15 Mar 2017 / current version 21 Aug 2017 → 2017.
- [[raivi-2024-jdaco-postdisaster-iot]] — Asif Mahmud Raivi, Sangman Moh 2024 (**IEEE IoT-J**, `10.1109/JIOT.2024.3354950`). **JDACO** — joint data aggregation + computation offloading for multi-UAV post-disaster IoT; two-tier LT-UAV/HT-UAV; minimize aggregation+offload energy/delay + max IoT coverage; **VD3QN** = dueling double DQN + value-decomposition network. Abstract (verbatim): +20% training-time reduction / +11.4% processed data / +5.6% energy efficiency / +11.2% mission duration vs conventional, up to 98% IoT devices served. pub 16 Jan 2024 / current version 25 Apr 2024 → 2024.
- [[lee-2024-dho-leo-handover]] — Ju-Hyung Lee, Chanyoung Park, Soohyun Park, Andreas F. Molisch 2024 (**IEEE TWC**, `10.1109/TWC.2023.3342975`). **DHO** — DRL-based LEO-satellite **connection-handover protocol** that skips the Measurement Report by prediction; minimizes access delay + collision rate; trained with **IMPALA** (V-trace). Up to **6.86× / 4.18×** lower access delay than conventional HO / heuristic (abstract+intro, attributed to Tables IV–V). Networking/handover, not offloading. pub 21 Dec 2023 / current version 12 Jul 2024 → 2024.
- [[chu-2024-secure-ris-isac]] — Jinjin Chu, Zhiping Lu, Rang Liu, Ming Li, Qian Liu 2024 (**IEEE TVT**, correspondence, `10.1109/TVT.2023.3328192`). **Secure RIS-ISAC**: maximize radar output SNR s.t. per-user comm SINR + eavesdropping-SINR ceiling + power budget + RIS unit-modulus; AO/BCD + SDR + Dinkelbach FP + **majorization-minimization**. **~2 dB** radar gain vs no-RIS (abstract, verbatim). PHY secure-ISAC anchor, not MEC. pub 27 Oct 2023 / current version 14 Mar 2024 → 2024.
- [[guo-2024-multiuav-proactive-eavesdropping]] — Delin Guo, Lan Tang, Xinggan Zhang, Ying-Chang Liang 2024 (**IEEE TMC**, `10.1109/TMC.2023.3311484`). **Multi-UAV proactive eavesdropping** (legitimate surveillance): full-duplex UAVs jam multiple mobile suspicious UAV→destination links while planning trajectories; MDP decoupled (proven optimality-preserving) into a non-learning **jamming-power solver** + per-UAV **decentralized RL moving policy**. Guarantees eavesdrop rate/success with fewer UAVs (qualitative). Surveillance/PLS anchor, not MEC. pub 4 Sep 2023 / current version 4 Apr 2024 → 2024.
- [[lei-2024-hvmappo-maritime-sar]] — Chengjia Lei, Shaohua Wu, Yi Yang, Jiayin Xue, Qinyu Zhang 2024 (**IEEE TVT**, `10.1109/TVT.2024.3388499`). **Heterogeneous-vehicle maritime SAR** (observation UAVs + relay UAVs + ASV MEC servers, no BS); joint trajectory + offloading + routing topology minimizing time/energy while maximizing relay **fault tolerance**; Dec-POMDP + **HVMAPPO** (MAPPO/CTDE + parameter-sharing + normalized GAE + Pop-Art + mixed-heterogeneous-reward). Outperforms baselines in efficiency + fault tolerance (qualitative). pub 15 Apr 2024 / current version 19 Sep 2024 → 2024.

### New concept stubs (6)

- [[leo-handover-protocol]] — the LEO-satellite *connection* handover signaling procedure (vs compute-state [[seamless-handover]]); anchors [[lee-2024-dho-leo-handover]].
- [[impala]] — distributed off-policy actor-learner DRL with V-trace; the trainer behind DHO.
- [[majorization-minimization]] — surrogate-bound iterative optimization (MM); used in [[chu-2024-secure-ris-isac]]'s RIS-reflection update.
- [[value-decomposition-network]] — cooperative MARL value factorization (VDN); the cooperative-learning half of JDACO's VD3QN.
- [[fault-tolerant-relay-network]] — redundant multi-hop relay topology metric; the co-equal objective in [[lei-2024-hvmappo-maritime-sar]].
- [[proactive-eavesdropping]] — jamming-assisted legitimate surveillance; anchors [[guo-2024-multiuav-proactive-eavesdropping]].

All other referenced concepts reused existing slugs (e.g. [[multi-uav-assisted-mec]], [[task-offloading]], [[edge-user-allocation]], [[binary-vs-partial-offloading]], [[energy-latency-tradeoff]], [[weighted-kmeans-uav-deployment]], [[drone-cell-3d-placement]], [[mobile-edge-computing]], [[mobility-aware-offloading]], [[small-cell-mec]], [[virtual-machine-multiplexing]], [[post-disaster-mec]], [[uav-data-collection]], [[ddqn]], [[centralized-training-decentralized-execution]], [[rotary-wing-propulsion-energy-model]], [[hierarchical-aerial-mec]], [[leo-satellite-edge-computing]], [[non-terrestrial-network]], [[walker-star-constellation]], [[ppo]], [[integrated-sensing-and-communication]], [[intelligent-reflecting-surface]], [[physical-layer-security]], [[alternating-optimization-sdr-sca]], [[fractional-programming-dinkelbach]], [[friendly-jamming-uav]], [[cooperative-jamming]], [[ma-pomdp]], [[pomdp]], [[mappo]], [[gae]], [[heterogeneous-uav-fleet]], [[maritime-mec]]).

### Entities — 0 new + 1 roster update

- **Roster update:** [[kezhi-wang]] (3→4, +[[yang-2019-sum-power-uav-mec]] multi-UAV-MEC sum-power; Northumbria identity confirmed by in-parse affiliation).
- **No new entity pages.** Deferred / not created (correctness over completeness, single corpus source each / identity not confirmable from parse): Zhaohui Yang + Cunhua Pan + Mohammad Shikh-Bahaei (King's College London / Queen Mary); Pavel Mach + Zdenek Becvar (CTU Prague); Asif Mahmud Raivi + Sangman Moh (Chosun Univ.); Ju-Hyung Lee + Chanyoung Park + Soohyun Park + Andreas F. Molisch (USC / Korea Univ.); Jinjin Chu + Zhiping Lu + Rang Liu + Ming Li + Qian Liu (Dalian Univ. of Technology / CATT — "Ming Li"/"Rang Liu"/"Qian Liu" are common names needing disambiguation); Delin Guo + Lan Tang + Xinggan Zhang + Ying-Chang Liang (Nanjing Univ. / UESTC); Chengjia Lei + Shaohua Wu + Yi Yang + Jiayin Xue + Qinyu Zhang (HIT Shenzhen / Peng Cheng Lab). No author-entity links embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 7 batch-3 folders.
- [[raivi-2024-jdaco-postdisaster-iot]] (Chosun Univ., joint aggregation+offload, VD3QN) is **distinct** from the other post-disaster sources [[zhou-2024-jdl-abs-postdisaster-rescue]] (single-ABS queuing-delay min, Lyapunov + SCA-critic) and [[sun-2024-mvtora-postdisaster-vfc]] (game/VFC) — cross-linked, not duplicated.
- [[lei-2024-hvmappo-maritime-sar]] (HIT/PCL, HVMAPPO + fault-tolerant relay) is **distinct** from the maritime SAR sources [[qi-2024-msar-minmax-latency]] (min-max latency, linearization+SCA+BnB) and [[wang-2026-aerial-marine-msar]] (UAV+HAPS+MASS JCORA) — different authors, objective, and solver — cross-linked, not duplicated.
- [[chu-2024-secure-ris-isac]] is **distinct** from the other RIS/ISAC sources [[zhang-2025-gan-td3-isac-active-ris]] (GAN-TD3, double active RIS) and [[su-2024-sensing-aided-isac-pls]] / [[yao-2025-secure-isac-dual-eavesdropping]] — passive-RIS radar-SNR-max via AO+SDR+FP+MM — cross-linked, not duplicated.
- [[lee-2024-dho-leo-handover]] (connection-handover protocol, networking) is **distinct** from the compute-state handover work [[han-2024-sagin-fl-handover]] (FL model/data handover) — different "handover" meaning — cross-linked, not duplicated.
- [[guo-2024-multiuav-proactive-eavesdropping]] is a **surveillance/PLS** paper (jamming for legitimate eavesdropping), distinct from the anti-jamming-MEC sources; cross-linked to the jamming concepts, not duplicated.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI/venue/year above is parse-grounded from the manuscript date-of-publication / date-of-current-version lines (year follows date-of-current-version for the straddling TWC/TVT/TMC/IoT-J papers, with both dates recorded in each citation). **Zero `not in parse` metadata fields this batch.** No web lookups were needed.
- **Grounded headline claims only:** JDACO +20% / +11.4% / +5.6% / +11.2% + 98% coverage (abstract verbatim); DHO 6.86× / 4.18× access-delay (abstract+intro, attributed to Tables IV–V); Chu RIS-ISAC ~2 dB radar gain (abstract verbatim); Yang-2019 IACL-beats-SCAFAH/ECC/near-EXH stated qualitatively with the ~3-iter / >1000→~420 W convergence figure-read flagged indicative; Guo proactive-eavesdropping (guarantee rate/success with fewer UAVs) and Lei HVMAPPO (outperforms baselines, efficiency-vs-fault-tolerance trade-off) stated qualitatively as the papers state them.
- **Wikilink integrity:** `linkcheck.py` = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this batch (7 sources + 6 concepts).
- **Process-narration:** `process_refs.py` = **0 files / 0 hits** outside `log.md`; sources/concepts/entities/index/overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated (no diagnostics) on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 6 concepts and the touched entity.
- **Counts reconciled** (`corpus_counts.py`): **155 sources / 226 concepts / 67 author entities (+[[pytorch]] = 68 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-3 folders were curated; **3 batches (16 papers) remain** for separate invocations (batch4 7 / batch5 7 / batch6 2).

## 2026-06-01 — Curation pass (batch 2/6: 7 new sources + audit)

Second batch of the deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-2 folders from `.curation-out/batches.json`; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **141 → 148 curated sources**. (Confirmed none of the 7 already had a source page before writing.) State reconciled clean at `388dcf8` (batch 1) before starting; `curation_status.py --dupes` re-confirmed **30 genuinely-new** remaining (the two space-named re-ingests stay correctly flagged as duplicates and were not touched).

### New source pages (7)

- [[zhou-2024-jdl-abs-postdisaster-rescue]] — Chengyi Zhou et al. 2024 (**IEEE TWC**, `10.1109/TWC.2024.3479709`). Post-disaster ABS computation offloading + communication assistance; min task-queuing-delay over ABS-GU association + offloading ratio + trajectory under ABS energy; **JDL** = Lyapunov + actor-critic DRL with a **model-based SCA critic** (vs a model-free critic DNN). Two-timescale (large-timescale trajectory, small-timescale offloading). Findings figure-read & flagged indicative (vs SDQN / circular-trajectory benchmarks). pub 21 Oct 2024 / current version 12 Dec 2024 → 2024.
- [[huang-2025-dual-aav-maritime-secure-cb]] — Jiawei Huang et al. 2025 (**IEEE IoT-J**, `10.1109/JIOT.2024.3521977`). Dual AAV cluster maritime secure communications via CB: MUVAA **relay** (data to Bob) + MUVAA **jammer** (jamming to Willie); multi-objective SEMCMOP (Bob SINR / Willie SINR / flight energy) solved by **IMOMA** (improved multi-objective mayfly algorithm, chaotic init + hybrid update). Abstract: security objective improved up to **43.20%**; CB-based SINR separation (Bob ≈20.75 / Willie ≈−39.9) verbatim from Fig. 5; IMOMA lowest energy 64 370 J among 5 (verbatim table). Presented in part at IEEE CSCWD 2023. pub 23 Dec 2024 / current version 25 Apr 2025 → 2025.
- [[mao-2016-lodco-eh-mec-offloading]] — Yuyi Mao, Jun Zhang, Khaled B. Letaief 2016 (**IEEE JSAC** 34(12) 3590–3605, `10.1109/JSAC.2016.2611964`). Green MEC with **energy-harvesting** devices; execution-cost (delay + task failure) min via the **LODCO** Lyapunov online algorithm (offloading + DVFS CPU-freq + transmit power from current state only); proven asymptotically optimal; monotonic CPU-freq/power vs battery level. pub 20 Sep 2016 / current version 29 Dec 2016 → 2016.
- [[yang-2024-taco-human-digital-twin-edge]] — Yuye Yang et al. 2024 (**IEEE TMC**, `10.1109/TMC.2024.3406607`). First **human digital twin (HDT)** edge-deployment study under end-edge-cloud; two-timescale accuracy-aware online optimization (**TACO**) jointly placing/updating generic+customized virtual twins + task offloading + ES access selection; improved Lyapunov + **piecewise McCormick envelopes** + BCD; closed-form gap-to-optimum + polynomial complexity. pub 28 May 2024 / current version 5 Nov 2024 → 2024.
- [[bor-yaliniz-2016-3d-abs-placement]] — R. Irem Bor-Yaliniz, Amr El-Keyi, Halim Yanikomeroglu (**IEEE ICC 2016**, `10.1109/ICC.2016.7510820`). First **3-D placement** of a drone-cell (ABS): jointly choose altitude + coverage location/size to maximize covered users; quadratically-constrained MINLP via altitude-to-radius bisection + MOSEK interior-point. **Metadata caveat:** the parse has **no** venue/year/DOI line (refs run to 2015); venue/DOI **web-confirmed** (IEEE Xplore doc 7510820 / arXiv 1603.00300) and explicitly flagged as not-in-parse on the page.
- [[zeng-2017-energy-efficient-uav-trajectory]] — Yong Zeng, Rui Zhang 2017 (**IEEE TWC** 16(6) 3747–3760, `10.1109/TWC.2017.2688328`). Energy-efficient UAV communication via trajectory optimization; first **fixed-wing propulsion-energy model** (speed + acceleration) + bits/Joule EE; shows unconstrained rate-max/energy-min give vanishing EE; circular + generally-constrained SCA trajectories. pub 28 Mar 2017 / current version 8 Jun 2017 → 2017.
- [[zhang-2013-energy-optimal-mcc-stochastic]] — Weiwen Zhang et al. 2013 (**IEEE TWC** 12(9) 4569–4581, `10.1109/TWC.2013.072513.121842`). Energy-optimal mobile cloud computing under a **stochastic (Gilbert-Elliott) channel**; mobile vs cloud execution via DVS CPU-freq / transmission-rate scheduling; closed-form policies + a **threshold policy** on data-consumption-rate $L/T$; $\kappa/\lambda = 6.67\times10^{-12}$ example (verbatim). accepted 24 Jun 2013 → 2013.

### New concept stubs (2)

- [[drone-cell-3d-placement]] — joint altitude + coverage location/size placement of an aerial base station; anchors [[bor-yaliniz-2016-3d-abs-placement]].
- [[fixed-wing-propulsion-energy-model]] — closed-form fixed-wing propulsion power vs speed + acceleration (power → ∞ as V→0, cannot hover); the counterpart to [[rotary-wing-propulsion-energy-model]]; originates in [[zeng-2017-energy-efficient-uav-trajectory]].

All other referenced concepts reused existing slugs (e.g. [[post-disaster-mec]], [[lyapunov-optimization]], [[two-timescale-optimization]], [[energy-harvesting-mec]], [[collaborative-beamforming]], [[physical-layer-security]], [[friendly-jamming-uav]], [[cooperative-jamming]], [[salp-swarm-algorithm]], [[maritime-mec]], [[air-to-ground-channel-model]], [[mixed-integer-nonlinear-programming]], [[alternating-optimization-sdr-sca]], [[task-offloading]], [[energy-latency-tradeoff]], [[binary-vs-partial-offloading]], [[service-caching-mec]], [[task-migration]], [[three-tier-cloud-edge-end]], [[edge-user-allocation]], [[mobility-aware-offloading]], [[virtual-machine-multiplexing]], [[cellular-connected-uav]], [[high-altitude-platform-station]], [[weighted-kmeans-uav-deployment]], [[uav-trajectory-control]]).

### Entities — 0 new + 6 roster updates

- **Roster updates:** [[geng-sun]] (12→13, +dual-AAV maritime secure CB, corresponding author), [[jiahui-li]] (9→10, +dual-AAV maritime secure CB, corresponding author), [[jiacheng-wang]] (7→8, +dual-AAV maritime secure CB), [[dusit-niyato]] (16→18, +dual-AAV maritime secure CB +HDT-TACO), [[jiawen-kang]] (11→12, +HDT-TACO), [[xuemin-shen]] (3→4, +HDT-TACO).
- **No new entity pages.** Deferred / not created (correctness over completeness): Yuyi Mao + Jun Zhang + Khaled B. Letaief (LODCO, HKUST — Yuyi Mao co-authored the existing [[mao-2017-mec-survey-communication]], but identity-vs-namesake and first-author-vs-survey-author handling left for human confirmation); Yong Zeng + Rui Zhang (energy-efficient UAV trajectory — recurring across [[zeng-2017-energy-efficient-uav-trajectory]], [[zeng-2019-rotary-wing-energy-min]], [[zeng-2019-uav-comm-tutorial-5g]], [[wu-2018-multiuav-minrate-trajectory]], but "Rui Zhang" is a common name needing affiliation disambiguation — flagged for human confirmation, no entity minted); Bor-Yaliniz / El-Keyi / Yanikomeroglu (Carleton; single corpus source each); Weiwen Zhang et al. (MCC; single source); Chengyi Zhou / Junyu Liu / Min Sheng / Jiandong Li / Weihua Zhuang (Xidian/Waterloo; single source); Yuye Yang / Changyan Yi / Jun Cai (NUAA/Concordia; single source). No author-entity links embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- No same-paper/different-UUID duplicate ingests among the 7 batch-2 folders.
- [[zhou-2024-jdl-abs-postdisaster-rescue]] (Xidian, Chengyi Zhou) is **distinct** from the other post-disaster sources [[peng-2025-drudm-cfg]] (DRUDM-CFG, generative-DRL urgency admission) and [[sun-2024-mvtora-postdisaster-vfc]] (game/VFC) — different authors, objective (queuing-delay min), and solver (Lyapunov + SCA-critic actor-critic) — cross-linked, not duplicated.
- [[huang-2025-dual-aav-maritime-secure-cb]] is **distinct** from the other secure-CB sources [[sun-2024-imssa-uav-secure-cb]] (salp-swarm, imperfect/unknown eavesdroppers) and [[zhang-2024-gdmtd3-aerial-secure-cb]] (diffusion-TD3): dual-cluster relay+jammer maritime architecture + **mayfly** metaheuristic. Same Geng-Sun cluster, cross-linked.
- [[mao-2016-lodco-eh-mec-offloading]] (EH-MEC) and [[zhang-2013-energy-optimal-mcc-stochastic]] (stochastic-channel MCC) are **distinct** early offloading-theory anchors (different author sets/venues/years), cross-linked to each other and to [[mao-2017-mec-survey-communication]].

### Audit (correctness-first)

- **DOI / venue / year** — 6 of 7 carry an explicit DOI line in their own parse; every DOI/venue/year for those 6 is parse-grounded (manuscript date-of-publication / current-version lines, with year following date-of-current-version for the straddling TWC/JSAC/TMC/IoT-J papers). The **7th** ([[bor-yaliniz-2016-3d-abs-placement]]) has **no** venue/year/DOI in the parse → recorded as **not in parse** and **web-confirmed** (IEEE ICC 2016, doc 7510820 / arXiv 1603.00300), with the caveat stated verbatim on the page. No fabricated metadata.
- **Grounded headline claims only:** Dual-AAV 43.20% security-objective improvement + Fig. 5 SINR table (Bob 20.75 / Willie −39.9) + IMOMA 64 370 J table (verbatim); LODCO "significantly outperforms greedy / reduces failures at minor delay cost" and Zhang-2013 "significant energy saved in some cases" + threshold policy quoted as stated; JDL queuing-delay-vs-SDQN/circular curves flagged figure-read/indicative; TACO accuracy/delay/energy superiority stated qualitatively.
- **Wikilink integrity:** `linkcheck.py` after the pass = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this batch (7 sources + 2 concepts).
- **Process-narration:** `process_refs.py` = **0 hits** outside `log.md`; sources/concepts/entities/index/overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 2 concepts.
- **Counts reconciled** (`corpus_counts.py`): **148 sources / 220 concepts / 67 author entities (+[[pytorch]] = 68 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-2 folders were curated; **4 batches (23 papers) remain** for separate invocations (batch3 7 / batch4 7 / batch5 7 / batch6 2).

## 2026-06-01 — Curation pass (batch 1/6: 7 new sources + audit)

First batch of a deliberately-split **6-batch** curation run over the **37 genuinely-new** raw papers currently uncurated (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-1 folders; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **134 → 141 curated sources**. (Confirmed none of the 7 already had a source page before writing.)

> **Scope note.** `wiki/references/recommendations.md` named two "ready to curate now" picks — *Optimizing Spectrum Sharing in UAV Swarms…* and *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks…* — but `curation_status.py --dupes` correctly flagged both raw folders as **duplicate MinerU ingests** (space-named) of already-curated underscore-named papers ([[wang-2025-uav-swarm-stackelberg]] and [[xie-2026-uav-multisource-fusion]]). They were **skipped, not re-curated**; the recommendations file is stale on these two. Reconciliation: `raw/sources` 173 folders, 134 curated, 39 uncurated → 2 duplicates → **37 genuinely-new**. `make_batches.py --size 7` → 6 batches (7/7/7/7/7/2).

### New source pages (7)

- [[mozaffari-2019-uav-wireless-tutorial]] — Mozaffari et al. 2019 (**IEEE COMST**, `10.1109/COMST.2019.2902862`). Tutorial on UAVs for wireless networks: UAVs as aerial base stations vs cellular-connected UAVs; 3D deployment, channel modeling, energy efficiency; analytical toolbox (optimization, ML, stochastic geometry, transport theory, game theory). *Not MEC — UAV-communications tutorial anchor.* Manuscript pub 5 Mar 2019 / current version 20 Aug 2019 → year 2019.
- [[sun-2024-active-passive-ris-receiver]] — Yifu Sun et al. 2024 (**IEEE TWC**, `10.1109/TWC.2023.3325813`). Active-passive cascaded RIS receiver for anti-jamming; worst-case rate max under imperfect angular jammer CSI; UM-ZF (passive) + AMM/C-M-CCD (active) semi-closed-form solutions. Reports PSR 32.8% vs 75.9% (2.78×) and ~0 dB vs ~−10 dB receive SINR at the BS direction (verbatim). *Not MEC — PHY RIS-receiver anchor.* pub 25 Oct 2023 / current version 12 Jun 2024 → 2024.
- [[wang-2024-blockchain-uav-mec-dpos]] — Die Wang et al. 2024 (**IEEE TVT**, `10.1109/TVT.2023.3306740`). Blockchain-integrated UAV-assisted MEC; improved **DPoS** (UAV light nodes + reputation-voted ground full nodes) + two-stage **Stackelberg** game over UAV trajectory/comm-resources and ground compute, solved via KKT + SCA. pub 21 Aug 2023 / current version 17 Jan 2024 → 2024.
- [[han-2024-ground-satellite-fl]] — Dong-Jun Han et al. 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3365901`). Cooperative FL over ground-to-satellite networks; LEO satellites as edge-compute units + intra-cluster aggregators + ISL relays; solar-battery-aware data offloading + non-convex convergence proof + latency minimizer. pub 13 Feb 2024 / current version 9 May 2024 → 2024.
- [[liu-2020-cooperative-uav-mec-power-iot]] — Yi Liu, Shengli Xie, Yan Zhang 2020 (**IEEE TVT**, `10.1109/TVT.2020.3016840`). Cooperative UAV-enabled MEC for power IoT (UAVs help neighboring small-cells); long-term utility max as a **semi-Markov** process; two-phase centralized + Q-value-transfer distributed DRL. pub 17 Aug 2020 / current version 22 Oct 2020 → 2020.
- [[wang-2024-hfrl-decentralized-navigation]] — Pengfei Wang et al. 2024 (**IEEE TMC**, `10.1109/TMC.2024.3439696`). Decentralized navigation for **heterogeneous** UAV-MEC; soft hierarchical DRL (SHDRLN, skill abstraction) + dual-end **federated RL** (DFRL) maximizing task-offloading energy efficiency. DFRL/FedAvg reach 2.7 KB/J at 100/200 episodes = original SHDRLN at 300; DFRL eventually surpasses original SHDRLN (verbatim figure-read). pub 7 Aug 2024 / current version 5 Nov 2024 → 2024.
- [[liu-2022-maritime-uav-mec-virtualization]] — Ying Liu, Junjie Yan, Xiaohui Zhao 2022 (**IEEE TVT**, `10.1109/TVT.2022.3141799`). Two-layer maritime UAV-MEC (T-UAV MEC server over B-UAVs) with **VM-multiplexing** parallel computing under I/O interference (unequal task sizes); latency min via DQN + DDPG over T-UAV trajectory + VM count. DDPG cuts total avg latency >37%, DQN 31% vs hover-center-no-parallel-computing (verbatim). pub 11 Jan 2022 / current version 2 May 2022 → 2022.

### New concept stubs (5)

- [[active-ris]] — RIS with phase + amplitude (amplifying) control; anchors [[sun-2024-active-passive-ris-receiver]].
- [[delegated-proof-of-stake]] — DPoS voting-elected delegate consensus; the improved DPoS of [[wang-2024-blockchain-uav-mec-dpos]].
- [[hierarchical-reinforcement-learning]] — skill/option temporal abstraction; the SHDRLN of [[wang-2024-hfrl-decentralized-navigation]].
- [[virtual-machine-multiplexing]] — multiple VMs per physical edge server with I/O interference; the parallel-compute mechanism of [[liu-2022-maritime-uav-mec-virtualization]].
- [[semi-markov-decision-process]] — random-sojourn-time MDP generalization; the formulation behind [[liu-2020-cooperative-uav-mec-power-iot]].

All other referenced concepts reused existing slugs (e.g. [[intelligent-reflecting-surface]], [[anti-jamming-mec]], [[physical-layer-security]], [[csi-estimation-error]], [[alternating-optimization-sdr-sca]], [[stackelberg-game]], [[blockchain-on-edge-trust-layer]], [[federated-learning]], [[federated-reinforcement-learning]], [[soft-actor-critic]], [[heterogeneous-uav-fleet]], [[leo-satellite-edge-computing]], [[privacy-sensitive-data-partitioning]], [[leo-satellite-coverage-time]], [[makespan-minimization]], [[maritime-mec]], [[multi-uav-assisted-mec]], [[deep-q-network]], [[ddpg]], [[parallel-vs-serial-processing]], [[cellular-connected-uav]], [[air-to-ground-channel-model]], [[high-altitude-platform-station]], [[stochastic-geometry-network-analysis]], [[uav-trajectory-control]], [[task-offloading]], [[small-cell-mec]]).

### Entities — 3 new + 3 roster updates

- **Created (3):** [[kaoru-ota]] (Muroran Inst. of Technology, `ota@csse.muroran-it.ac.jp`; 2 sources — [[wang-2024-blockchain-uav-mec-dpos]] + [[li-2024-twohop-iort-packet-scheduling]], with [[mianxiong-dong]]); [[dong-jun-han]] (Purdue, `han762@purdue.edu`; 2 sources — [[han-2024-ground-satellite-fl]] + [[han-2024-sagin-fl-handover]], first author both); [[christopher-brinton]] (Purdue, `cgb@purdue.edu`; 2 sources — same two, senior author both).
- **Roster updates:** [[mianxiong-dong]] (2→3, +blockchain-DPoS, corresponding author), [[shengli-xie]] (2→3, +power-IoT cooperative MEC; GDUT, `shlxie@gdut.edu.cn` consistent — same identity), [[geng-sun]] (11→12, +decentralized-navigation co-author; Jilin Univ.).
- No author-entity links were embedded in source-page bodies (house convention).

### Duplicate / near-duplicate check

- The two recommendations picks are duplicate ingests of already-curated papers — skipped (see scope note above).
- [[han-2024-ground-satellite-fl]] is **distinct** from the same Purdue group's [[han-2024-sagin-fl-handover]]: two-tier ground-to-satellite with solar-battery-aware offloading + convergence proof vs three-tier SAGIN adding a UAV/air layer and a seamless-handover offloading optimizer — cross-linked, not duplicated.
- [[liu-2020-cooperative-uav-mec-power-iot]] (Yi Liu, GDUT), [[liu-2022-maritime-uav-mec-virtualization]] (Ying Liu, Jilin Univ.) are **distinct authors** from each other and from existing Liu entities ([[lihan-liu]], [[yangbo-liu]], [[jiajia-liu]], [[yanheng-liu]]); no entity created for either first author (each has 1 corpus source).
- [[sun-2024-active-passive-ris-receiver]] (Yifu Sun, NUDT) is a **different author** from the Geng-Sun / Zemin-Sun / Hao-Sun entities and from [[sun-2024-mfris-semantic-antijamming]]'s author — no roster change.
- No same-paper/different-UUID duplicate ingests among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch.** Year follows date-of-current-version for the straddling TWC/TVT/JSAC/TMC papers, with both dates recorded in each citation.
- **Grounded headline claims only:** RIS PSR 32.8%/75.9% (2.78×) and ~0 dB vs ~−10 dB SINR; maritime DDPG >37% / DQN 31% latency reduction; HFRL 2.7 KB/J at 100/200 vs 300 episodes — all quoted from the parse (figure-read curves flagged indicative). Blockchain-DPoS "superior delay", cooperative power-IoT "better than non-cooperative", and ground-satellite-FL "significantly speeds up convergence" stated qualitatively as the papers state them.
- **Wikilink integrity:** `linkcheck.py` after the pass = **NO DANGLING LINKS** (Obsidian-faithful). All new wikilinks target existing slugs or pages created in this same batch (7 sources + 5 concepts + 3 entities).
- **Process-narration:** `process_refs.py` = **0 hits** outside `log.md`; sources/concepts/entities/index/overview kept evergreen.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 5 concepts and 3 entities.
- **Counts reconciled** (`corpus_counts.py`): **141 sources / 218 concepts / 67 author entities (+[[pytorch]] = 68 entity pages)**, 13 findings / 11 synthesis / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-1 folders were curated; **5 batches (30 papers) remain** for separate invocations.



## 2026-06-01 — Synthesis pass (collaborative-beamforming track: +1 synthesis, +1 finding, cross-links; no new papers)

No-new-papers coverage-growth pass over the **collaborative-beamforming (CB)** cluster. Phase 0 confirmed the corpus is fully curated: `curation_status.py --dupes` reports **0 genuinely-new** folders (the two space-vs-underscore re-ingests — *Optimizing Spectrum Sharing…* and *UAV-Enabled Multi-Source Data Fusion…* — remain correctly classified as duplicate MinerU ingests, no page needed). Tree clean at `f3c67fb`. LLM Wiki API reachable (`allowUnauthenticated:true`, v0.4.16); baseline graph **446 nodes / 3717 edges** → **448 / 3751** after this pass.

The CB track had a [[collaborative-beamforming]] concept page and 5 source pages but **no synthesis page** and an under-counted track row in `overview.md` (4 of 5 sources) — the highest-leverage, cleanly-bounded gap. Each claim was grounded in the source parses before writing (GVAA+AVAA dual-array framing verified in the EMSSA parse; "save 30% handover frequency" verified verbatim in the EMODRL ground-space parse abstract).

### New derived pages (2)

- **Synthesis** [[collaborative-beamforming-in-aerial-mec]] — maps the 5 CB sources ([[sun-2025-emoppo-vlh-aerial-cb]], [[li-2024-emodrl-ground-space-cb]], [[li-2024-emssa-uav-swarm-vaa]], [[sun-2024-imssa-uav-secure-cb]], [[zhang-2024-gdmtd3-aerial-secure-cb]]) by array→receiver geometry (aerial-to-ground / ground-to-space / dual GVAA+AVAA), multi-objective trade (rate/secrecy vs flight energy, with SLL + leakage axes for the secure variants), and solver family (pure swarm-intelligence salp-swarm vs evolutionary-MORL vs diffusion-DRL) — a tidy microcosm of the [[drl-vs-evolutionary-vs-classical-solvers]] debate. Notes the gaps: no CB source carries a compute/offloading objective; single author cluster ([[geng-sun]] group); uneven eavesdropper threat models.
- **Finding** [[dcb-cuts-satellite-handover-frequency]] — distributed CB cuts LEO handover frequency ~30% at matched uplink rate ([[li-2024-emodrl-ground-space-cb]], `confidence: medium`, parse abstract); the clearest quantified CB result in the corpus.

### Refreshed / cross-linked pages

- [[collaborative-beamforming]] concept — added the dual GVAA+AVAA flavor row (was missing [[li-2024-emssa-uav-swarm-vaa]]) and a pointer to the new synthesis.
- 5 CB source pages — added `[[collaborative-beamforming-in-aerial-mec]]` to `related` (and the new finding to the EMODRL source); bumped `updated`.
- [[drl-vs-evolutionary-vs-classical-solvers]] synthesis — added the CB microcosm to `related`.
- `overview.md` — analytical-layer tally 12→13 findings / 10→11 synthesis; CB track row corrected 4→5 sources and linked to the synthesis; new finding listed in Open/analytical layer narrative.
- `index.md` — new finding under Findings, new synthesis under Synthesis.

### Entities

None created. The CB cluster authors ([[geng-sun]], [[jiahui-li]], [[zemin-sun]], [[qingqing-wu]], [[dusit-niyato]], [[jiawen-kang]], [[victor-c-m-leung]]) already have entity pages; no new clearly-recurring author surfaced in this slice.

### Self-check

- `linkcheck.py` — **NO DANGLING LINKS** (Obsidian-faithful). `process_refs.py` — **0 files / 0 hits** (no process-narration leaked outside this log). `corpus_counts.py` — sources 134, concepts 213, entities 65, findings 13, synthesis 11, comparisons 4, methodology 2, queries 4, thesis 1.
- Frontmatter validated on both new pages (no diagnostics). Counts in `overview.md`/`index.md` reconciled to the tool output.
- Toolkit unchanged this pass — the existing scripts covered every check; nothing warranted a new flag or script.

## 2026-05-31 — Curation pass (batch 8/8: 3 new sources + audit; multi-batch run complete)

Eighth and final batch of the deliberately-split 8-batch curation run over the 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 3 assigned batch-8 folders. Corpus grows **131 → 134 curated sources**, completing the 52-paper run (the two space-vs-underscore re-ingests — *Optimizing Spectrum Sharing…* and *UAV-Enabled Multi-Source Data Fusion…* — were correctly identified as duplicates of already-curated sources and skipped). (Confirmed none of the 3 already had a source page before writing.)

> **Note (orchestration):** this batch-8 run was interrupted after writing its pages, concepts, entities, and `index.md`/roster updates but before reconciling `overview.md`/`log.md` and committing. The interrupted work was inspected and completed (overview/log reconciliation + this entry + commit) rather than re-run, to avoid duplication. All three source pages and supporting pages were verified complete and parse-grounded before finishing.

### New source pages (3)

- [[sun-2024-imssa-uav-secure-cb]] — Sun et al. 2024 (**IEEE TMC**, `10.1109/TMC.2023.3273293`). UAV-enabled **secure communications** via **collaborative beamforming** (UVAA) against **known eavesdroppers with imperfect location info + unknown eavesdroppers**; multi-objective SCMOP (maximize worst-case secrecy rate / minimize max sidelobe level / minimize flight energy) proven non-convex & NP-hard, solved by an **improved multi-objective salp swarm algorithm (IMSSA)** with circle-map init + discrete update + migration/adaptive-mutation operators; Raspberry-Pi demonstration. Earlier version at IEEE ISCC 2022. DOI pub 5 May 2023 / current version 6 Mar 2024 → year 2024.
- [[xu-2024-mobile-aigc-survey]] — Xu et al. 2024 (**IEEE COMST**, `10.1109/COMST.2024.3353265`). **Survey** of edge-cloud generative-AI / **AIGC services** in mobile networks (**mobile AIGC networks**): generative-model fundamentals, the AIGC service lifecycle (data collection → pre-training → fine-tuning → inference → product management), the collaborative cloud-edge-mobile infrastructure, applications/case studies, and implementation challenges (edge resource allocation, task/computation offloading, edge caching, mobility management, incentive mechanisms). DOI pub 12 Jan 2024 / current version 23 May 2024 → year 2024.
- [[zeng-2024-usv-fleet-collaborative-offloading]] — Zeng et al. 2024 (**IEEE TVT**, `10.1109/TVT.2024.3359310`). UAVs offload marine-monitoring tasks **to USV fleets**; a **first-price sealed reverse auction with reserve price** incentivizes fleet participation (reserve = UAV valuation; symmetric-equilibrium bidding derived with existence + uniqueness proofs), then an energy-minimization problem is decomposed by **BCD** into two subproblems each solved by an **ADMM** improved with dynamic penalty coefficients. Participation degree improves **28.27%/25.74% over RBS/GBS** across task sizes and **27.84%/21.14%** across fleet counts (verbatim). Earlier version at IWCMC 2022. DOI pub 27 Feb 2024 / current version 17 Oct 2024 → year 2024.

### New concept stubs (3)

- [[mobile-aigc-network]] — the edge-cloud architecture for *serving* AIGC as the workload (distinct from [[generative-ai-for-mec]], which uses generative models to optimize the MEC system); anchors [[xu-2024-mobile-aigc-survey]].
- [[reverse-auction-incentive]] — first-price sealed reverse auction with reserve price (single buyer, lowest-bidding seller wins); the incentive layer of [[zeng-2024-usv-fleet-collaborative-offloading]].
- [[alternating-direction-method-of-multipliers]] — the ADMM augmented-Lagrangian block-splitting solver, complementing [[two-stage-decomposition]] / [[alternating-optimization-sdr-sca]] / [[penalty-dual-decomposition]].

All other referenced concepts reused existing slugs (e.g. [[collaborative-beamforming]], [[physical-layer-security]], [[salp-swarm-algorithm]], [[uav-trajectory-control]], [[air-to-ground-channel-model]], [[generative-ai-for-mec]], [[aigc-service-provider]], [[three-tier-cloud-edge-end]], [[generative-diffusion-model]], [[task-offloading]], [[service-caching-mec]], [[mobility-aware-offloading]], [[federated-learning]], [[maritime-mec]], [[double-auction]], [[nash-equilibrium]], [[energy-latency-tradeoff]]).

### Entities — 2 new + roster updates

- **Created (2):** [[zhou-su]] (Xi'an Jiaotong Univ., `zhousu@ieee.org`; 2 sources — [[zeng-2024-usv-fleet-collaborative-offloading]] (corresponding author) + [[dai-2023-hybrid-marine-mmwl]]); [[yanheng-liu]] (Jilin Univ., `yhliu@jlu.edu.cn`; 2 sources — [[sun-2024-imssa-uav-secure-cb]] + [[sun-2023-bargain-match-vec]], in the [[geng-sun]] cluster).
- **Roster updates (existing entities):** [[victor-c-m-leung]] (3→5, +IMSSA secure-CB +AIGC survey), [[minghui-dai]] (2→3, +USV-fleet co-author), [[dusit-niyato]] (15→16, +AIGC survey), [[jiawen-kang]] (10→11, +AIGC survey), [[zhu-han]] (6→7, +AIGC survey), [[xuemin-shen]] (2→3, +AIGC survey), plus the IMSSA secure-CB co-authors [[geng-sun]], [[zemin-sun]], [[jiahui-li]], [[qingqing-wu]] (the IMSSA paper positively **confirms** the SJTU Qingqing Wu in the Geng-Sun collaborative-beamforming cluster).
- No author-entity links were embedded in source-page bodies (matching the established house convention).

### Duplicate / near-duplicate check

- [[sun-2024-imssa-uav-secure-cb]] is **distinct** from the existing secure-CB source [[zhang-2024-gdmtd3-aerial-secure-cb]] (swarm-intelligence IMSSA optimizer + imperfect/unknown-eavesdropper modeling vs diffusion-enhanced TD3 DRL) and from the other Geng-Sun CB papers ([[sun-2025-emoppo-vlh-aerial-cb]], [[li-2024-emodrl-ground-space-cb]], [[li-2024-emssa-uav-swarm-vaa]]) — cross-linked, not duplicated.
- [[zeng-2024-usv-fleet-collaborative-offloading]] is **distinct** from the same-cluster marine papers [[dai-2024-multiuav-marine-welfare]] (double-auction OBS selection) and [[dai-2023-hybrid-marine-mmwl]] (MMWL hybrid FDMA/NOMA) — different architecture (USV-fleet-as-helper), incentive (reverse auction), and solver (BCD/ADMM).
- [[xu-2024-mobile-aigc-survey]] is the anchor **survey** for the generative-AI thread, distinct from the methodological tutorial [[du-2024-gdm-network-optimization-tutorial]] and the concrete ASP-selection source [[du-2024-d2sac-aigc-asp-selection]].
- No same-paper/different-UUID duplicate ingests found among the 3.

### Audit (correctness-first)

- **DOI / venue / year** — all 3 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year is grounded (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch.** Year follows date-of-current-version for the straddling TMC/TVT papers, with both dates recorded in each citation.
- **Grounded headline claims only:** USV-fleet participation-degree percentages (28.27%/25.74%; 27.84%/21.14%) quoted verbatim from the parse; IMSSA "outperforms MOPSO/NSGA-II/MODE/MSSA/IMODACH" stated as the paper states it (Pareto/metric curves are figure-derived, flagged indicative); the AIGC survey's claims framed as organizing claims, not measured results.
- **Wikilink integrity:** wiki-wide check after the pass = **ZERO dangling links** introduced this batch; all new wikilinks target existing slugs or pages created in this same batch. (Two pre-existing dangling references — `hp-mobility-models` and a root-level `purpose` link inside meta-doc narrative — are tracked for the next audit pass and were not introduced here.)
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 3 source pages; `type`/`title`/`tags`/dates/H1 on the 3 concepts and 2 entities.
- **Counts reconciled:** **134 sources / 213 concepts / 64 author entities (+[[pytorch]] = 65 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 3 assigned batch-8 folders were curated; the 52-paper multi-batch run is now complete.

## 2026-05-31 — Curation pass (batch 7/8: 7 new sources + audit)

Seventh batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-7 folders; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **124 → 131 curated sources**. (Confirmed none of the 7 already had a source page before writing.)

### New source pages (7)

- [[su-2024-sensing-aided-isac-pls]] — Su, Liu & Masouros 2024 (**IEEE TWC**, `10.1109/TWC.2023.3306029`). **Sensing-aided physical-layer security** for ISAC: a dual-functional BS emits an omnidirectional waveform to estimate eavesdropper directions (**CAML**), then jointly minimizes the **CRB** of targets/Eves and maximizes the **AN-aided secrecy rate** via alternating optimization (maximizing the FIM determinant) + a **fractional-programming** solver; robustness via a wide main beam sized by the prior-iteration CRB. Key result: secrecy rate improves as CRB decreases (single- and multi-Eve). *Not a UAV/MEC paper* — curated as a sensing-PLS anchor. DOI pub 23 Aug 2023 / current version 11 Apr 2024 → year 2024.
- [[zhu-2024-sensing-comm-doppler-uav-swarm]] — Zhu et al. 2024 (**IEEE TVT**, `10.1109/TVT.2023.3315868`). **Sensing-communication co-design** for UAV-swarm-assisted vehicular networks in perspective of **Doppler**; models Doppler's effect on comms (SNR loss) vs sensing (velocity estimation); minimizes ground-vehicles' **maximum CRLB** under an SNR-loss constraint via a **differential-evolution** algorithm. Abstract reports >30% sensing-accuracy gain + >20% communication gain vs SOTA (verbatim). *Sensing/comms only — no MEC offloading.* DOI pub 15 Sep 2023 / current version 13 Feb 2024 → year 2024.
- [[zhang-2019-stochastic-offloading-uav-mec]] — Zhang et al. 2019 (**IEEE IoT-J**, `10.1109/JIOT.2018.2890133`). **Stochastic** computation offloading + resource allocation + trajectory scheduling for single-UAV MEC; minimizes average weighted SMD+UAV energy; **Lyapunov** decomposition into three subproblems solved by **ADMM + interior-point + CVX**; the V and w_c parameters tune the queue-stability-vs-utility compromise. DOI pub 28 Dec 2018 / current version 8 May 2019 → year 2019.
- [[sun-2025-tjcct-twotimescale-uav-mec]] — Sun et al. 2025 (**IEEE TMC**, `10.1109/TMC.2024.3505155`). **TJCCT** — a **two-timescale** approach for UAV-assisted MEC; hierarchical MD/terrestrial-edge/aerial-edge/controller architecture; non-convex NP-hard MINLP system-utility maximization solved by short-timescale **price-incentive** resource allocation + **matching** offloading and long-timescale **convex** trajectory control; stability + polynomial complexity proved. Stated trade-off: superior delay/processing-rate/completion/cost metrics at the cost of higher energy consumption. Earlier version at INFOCOM 2024. DOI pub 22 Nov 2024 / current version 6 Mar 2025 → year 2025.
- [[li-2024-twohop-iort-packet-scheduling]] — Li et al. 2024 (**IEEE IoT-J**, `10.1109/JIOT.2024.3393444`). Two-hop **packet scheduling** + resource allocation + UAV trajectory design for **IoRT** in an air-ground integrated network (HAP→UAV→device); minimizes average packet **queue** delay; MDP with hybrid action space split into continuous (**MADDPG**) and discrete (**MADDQN**) sub-actions + **adaptive PER** → **MADDPG-APER**. DOI pub 25 Apr 2024 / current version 25 Jul 2024 → year 2024.
- [[dai-2024-uav-vehicular-offloading-lyapunov]] — Dai et al. 2024 (**IEEE TMC**, `10.1109/TMC.2023.3259394`). UAV relieves **overloaded RSUs** in vehicular edge computing; minimizes time-average vehicular task delay under a long-term UAV energy budget via **Lyapunov** decoupling + a **Markov-approximation** online offloading algorithm with a proven close-to-optimal gap. First author **Xingxia** Dai (Hunan University). DOI pub 20 Mar 2023 / current version 6 Mar 2024 → year 2024.
- [[liu-2020-wpt-cooperative-uav-mec]] — Liu et al. 2020 (**IEEE IoT-J**, `10.1109/JIOT.2019.2958975`). UAV-enabled **wireless-powered cooperative** MEC (UAV energy transmitter + MEC server; **idle SDs** harvest energy and help **active SDs** compute); minimizes total UAV required energy over CPU frequencies + offloading bits + transmit power + trajectory via an **SCA**-based algorithm and a lower-complexity **decomposition-and-iteration (DAI)** alternative. Trajectory optimization is the dominant energy factor (verbatim). DOI pub 20 Dec 2019 / current version 14 Apr 2020 → year 2020.

### New concept stubs (3)

- [[cramer-rao-bound]] — the CRB/CRLB sensing figure of merit (inverse Fisher Information), anchoring the two ISAC/Doppler sources ([[su-2024-sensing-aided-isac-pls]] CRB-vs-secrecy, [[zhu-2024-sensing-comm-doppler-uav-swarm]] min-max CRLB).
- [[two-timescale-optimization]] — fast (slot-level) vs slow (trajectory) decision decomposition; the short/long-timescale split behind TJCCT ([[sun-2025-tjcct-twotimescale-uav-mec]]).
- [[markov-approximation]] — Gibbs/log-sum-exp Markov-chain search over discrete configurations; the per-slot combinatorial solver in [[dai-2024-uav-vehicular-offloading-lyapunov]].

All other referenced concepts reused existing slugs (e.g. [[mobile-edge-computing]], [[task-offloading]], [[lyapunov-optimization]], [[uav-trajectory-control]], [[integrated-sensing-and-communication]], [[physical-layer-security]], [[fractional-programming-dinkelbach]], [[alternating-optimization-sdr-sca]], [[differential-evolution]], [[vehicular-mec]], [[uav-enabled-its]], [[hierarchical-aerial-mec]], [[matching-theory-for-resource-allocation]], [[mixed-integer-nonlinear-programming]], [[air-ground-integrated-network]], [[high-altitude-platform-station]], [[maddpg]], [[ddqn]], [[hybrid-action-decision-making]], [[prioritized-experience-replay]], [[wireless-power-transfer]], [[rf-energy-harvesting]], [[rotary-wing-propulsion-energy-model]], [[energy-latency-tradeoff]]).

### Entities — 5 new + roster updates + 1 affiliation-move deferral

- **Created (5):** [[shichao-li]] (Guilin Univ. of Electronic Technology, `shichaoli@guet.edu.cn`; 2 sources — [[li-2024-twohop-iort-packet-scheduling]] + the already-curated [[li-2025-twohop-airground-drl-offloading]]); [[hongbin-chen]] (GUET, `chbscut@guet.edu.cn`; 3 sources — the two two-hop IoRT papers + [[wang-2024-hybrid-oma-noma-sagin]]); [[mianxiong-dong]] (Muroran Inst. of Technology, `mx.dong@csse.muroran-it.ac.jp`; 2 sources — IoRT packet scheduling + [[li-2024-robust-bmappo-multiuav-mec]]); [[ning-zhang]] (Univ. of Windsor, `ning.zhang@uwindsor.ca`; 2 sources — same two as Dong); [[victor-c-m-leung]] (Shenzhen MSU-BIT / Shenzhen Univ. / UBC, `vleung@ieee.org`; 3 sources — [[sun-2025-tjcct-twotimescale-uav-mec]] + [[sun-2024-mvtora-postdisaster-vfc]] + [[li-2024-emodrl-ground-space-cb]]).
- **Roster updates (existing entities):** [[geng-sun]] (9→10, +TJCCT, corresponding author), [[zemin-sun]] (4→5, +TJCCT lead author), [[qingqing-wu]] (6→7, +TJCCT, SJTU-email-matched), [[dusit-niyato]] (14→15, +TJCCT), [[shuang-liang]] (3→4, +TJCCT corresponding author).
- **Deferred — Chau Yuen affiliation move.** "Chau Yuen" co-authors [[jia-2022-hierarchical-aerial-matching]] (Singapore Univ. of Technology and Design, `yuenchau@sutd.edu.sg`) and [[sun-2025-tjcct-twotimescale-uav-mec]] (Nanyang Technological Univ., `chau.yuen@ntu.edu.sg`). Same name, different listed institution/email — a plausible affiliation move rather than a namesake, but **not** minted as an entity pending human confirmation.
- The recurring TJCCT co-authors **Long He** and **Hongyang Pan** (Jilin University) each appear in only 1–2 corpus sources via the [[geng-sun]] cluster; no standalone entity pages were created (Long He appears in MVTORA + TJCCT but has no first-author corpus source — left for a future pass).
- No author-entity links were embedded in source-page bodies (matching the established house convention).

### Duplicate / near-duplicate check (the assigned watch item)

The brief warned that an already-curated "Stochastic … UAV … MEC" paper and vehicular-edge-computing papers could be confused with these. Verified each batch-7 paper is **genuinely new** and distinct:
- [[zhang-2019-stochastic-offloading-uav-mec]] (Zhang et al., NUDT, **IoT-J 2019**, ADMM/interior-point/CVX, joint SMD+UAV energy) is **distinct** from the already-curated [[yang-2022-stochastic-uav-mec-lyapunov]] (Yang/Bi/Zhang, **TWC 2022**, two-stage-vs-joint, user energy) — different authors, venue, year, DOI, and solver, despite near-identical titles. Both reuse [[lyapunov-optimization]].
- [[li-2024-twohop-iort-packet-scheduling]] (**packet-queue** delay, MADDPG+MADDQN+adaptive PER, IoT-J 2024) is **distinct** from the same lead author's [[li-2025-twohop-airground-drl-offloading]] (**task-offloading** delay, MADDPG-IPER+NV-IPPO/JPTORAUTD, IoT-J 2025) — different objective, action-space split, algorithm, year, DOI. Not a duplicate ingest.
- [[dai-2024-uav-vehicular-offloading-lyapunov]] (**Xingxia** Dai, Hunan Univ., vehicular VEC, Lyapunov+Markov-approximation, TMC) is **distinct** from the marine-welfare paper by **Minghui** Dai ([[dai-2024-multiuav-marine-welfare]]) and from the other vehicular sources ([[ma-2025-pdqn-vehicular-mec]], [[zhang-2025-mcma-task-migration]], [[sun-2023-bargain-match-vec]], [[peng-2020-maddpg-uav-vehicular]]) — different first author, method, and framing.
- [[sun-2025-tjcct-twotimescale-uav-mec]] (two-timescale price-incentive+matching+convex, TMC 2025) is **distinct** from the same group's [[sun-2024-mvtora-postdisaster-vfc]] (post-disaster game+convex+evolutionary, TMC 2024) — different architecture, objective, method, year.
- [[liu-2020-wpt-cooperative-uav-mec]] (idle-SD **cooperative** WPT-MEC, UAV-energy min, SCA/DAI, IoT-J 2020) is **distinct** from [[zhou-2018-uav-wireless-powered-mec]] (computation-rate max, JSAC 2018) — different objective + idle-SD cooperation.
- [[su-2024-sensing-aided-isac-pls]] (sensing-aided PLS, CRB-vs-secrecy, no UAV) is **distinct** from [[yao-2025-secure-isac-dual-eavesdropping]] (UAV-trajectory secure ISAC).
- No same-paper/different-UUID duplicate ingests were found among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded in the parse (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch** — all 7 source pages have full title/authors/year/url/venue. **Year convention:** for papers whose publication vs current-version dates straddle two years, year follows date-of-current-version (the wiki's established convention), with both dates recorded in each citation (2018→2019 stochastic, 2019→2020 WPT-cooperative, 2023→2024 Doppler + UAV-VEC, 2024→2025 TJCCT).
- **Grounded headline claims only:** the verbatim figures — Zhu Doppler ">30% sensing / >20% communication" gains, Liu WPT "trajectory optimization is the dominant factor" + "converge within several iterations" — are quoted from the parse. Su CRB-vs-secrecy mutual improvement, TJCCT metric set + energy-consumption trade-off, Zhang stochastic V/w_c compromise, Li MADDPG-APER delay reduction, and Dai delay-reduction + multi-UAV energy trade-off are stated **qualitatively** as the papers state them, with figure-only magnitudes flagged as indicative.
- **Wikilink integrity:** wiki-wide link check after the pass = **no NEW dangling links** introduced (verified — see below). All wikilinks introduced this batch target existing slugs or pages created in this same batch (7 sources + 3 concepts + 5 entities). Pre-existing dangling-link status unchanged.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 3 concept stubs and 5 entity pages. No self-references or duplicate `related` entries.
- **Counts reconciled:** **131 sources / 210 concepts / 62 author entities (+[[pytorch]] = 63 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-7 folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.


## 2026-05-31 — Curation pass (batch 6/8: 7 new sources + audit)

Sixth batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-6 folders; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **117 → 124 curated sources**. (Clean retry: a prior attempt was cancelled before writing; confirmed none of the 7 already had a source page.)

### New source pages (7)

- [[yang-2020-loadbalance-multiuav-iot]] — Yang et al. 2020 (**IEEE IoT-J**, `10.1109/JIOT.2020.2971645`). Multi-UAV **load-balance** MEC for IoT: **differential-evolution** UAV deployment + **generalized-assignment-problem** node assignment (LP-relax + bipartite rounding) + single-agent **DQN** task scheduling minimizing average slowdown. DOI pub 4 Feb 2020 / current version 12 Aug 2020 → year 2020.
- [[dai-2024-multiuav-marine-welfare]] — Dai et al. 2024 (**IEEE TCOMM**, `10.1109/TCOMM.2024.3388501`). Multi-UAV multi-access marine MEC (UAVs + **ocean beacon stations**); maximizes **system revenue** (system welfare − energy) by jointly optimizing OBS selection, offloading ratio, transmission duration; vertical 3-layer decomposition with a **double-auction** OBS-selection game. Reported trade-off: higher revenue **and** higher energy vs DOS/ROS benchmarks (Figs. 7–9, qualitative). DOI pub 15 Apr 2024 / current version 18 Sep 2024 → year 2024.
- [[al-hourani-2014-optimal-lap-altitude]] — Al-Hourani, Kandeepan & Lardner 2014 (**IEEE WCL**, `10.1109/LWC.2014.2342736`). Foundational **air-to-ground channel** letter: closed-form sigmoid **LoS-probability vs elevation angle** (ITU P.1410 parameters) + **optimal LAP altitude** maximizing ground coverage. *Not an MEC paper* — curated as a channel-model anchor. DOI pub 24 Jul 2014 / current version 17 Dec 2014 → year 2014.
- [[michailidis-2024-secure-ris-uav-mec-iot]] — Michailidis et al. 2024 (**IEEE TCOMM**, `10.1109/TCOMM.2024.3372877`). Secure UAV-**RIS**-MEC-IoT partial offloading vs **aerial + ground eavesdroppers**; UAV is both aerial MEC server and DF relay to a MEC-AP; derives **SOP** over Nakagami-m and maximizes **min secure computation efficiency** via Dinkelbach + BCD + bisection. UAV trajectory **not** optimized (fixed straight-line). DOI pub 1 Mar 2024 / current version 19 Jul 2024 → year 2024.
- [[zhang-2020-response-delay-uav-swarm]] — Zhang et al. 2020 (**IEEE TVT**, `10.1109/TVT.2020.2964821`). **Response-delay** optimization for a MEC-enabled UAV swarm (MEC top-UAV + bottom-UAVs); **stochastic geometry** (3-D PPP) + **queueing theory** closed-form delay. **Hardware-validated** on 2 DJI M100 UAVs + 5G NR mmWave (28 GHz). Reports 10–20% response-delay cut vs no-MEC; 89.9% fewer transmitted packets via on-T-UAV video key-frame extraction (verbatim). DOI pub 8 Jan 2020 / current version 12 Mar 2020 → year 2020.
- [[li-2024-robust-bmappo-multiuav-mec]] — Li et al. 2024 (**IEEE IoT-J**, `10.1109/JIOT.2023.3300718`). **Robust** multi-UAV-MEC offloading under joint communication (imperfect CSI) + computation (task-complexity error) uncertainty; weighted-energy min via **MAPPO with a Beta-distribution actor policy (b-MAPPO)**; beats Pure-MAPPO/MADDPG/Greedy, tracks DRL+CVX (avg UE reward ≈ −3.05 verbatim). DOI pub 1 Aug 2023 / current version 24 Jan 2024 → year 2024.
- [[li-2023-secure-marine-iot-jamming]] — Li et al. 2023 (**IEEE TVT**, `10.1109/TVT.2022.3231295`). **Secure** marine-IoT offloading: **USVs** upload to a **HAP** via NOMA then provide **cooperative jamming** (PLS); system-energy min via layered decomposition — **monotonic-optimization (Polyblock) + bisection (PAS)** for the bottom problem and **cross-entropy (CASE)** for USV positions. Reduces energy by **27.32%** on average vs fixed jamming (verbatim). DOI pub 22 Dec 2022 / current version 18 May 2023 → year 2023.

### New concept stubs (10)

- [[generalized-assignment-problem]] — capacity-constrained NP-hard task-to-agent assignment (the GAP behind the load-balance node-assignment of [[yang-2020-loadbalance-multiuav-iot]]).
- [[double-auction]] — many-to-many buyer/seller market mechanism (the OBS-selection game of [[dai-2024-multiuav-marine-welfare]]).
- [[air-to-ground-channel-model]] — the LoS/NLoS mixture ATG model + sigmoid LoS-probability-vs-elevation-angle, anchored by [[al-hourani-2014-optimal-lap-altitude]].
- [[secure-computation-efficiency]] — securely-computed bits per weighted energy (the SCE objective of [[michailidis-2024-secure-ris-uav-mec-iot]]).
- [[secrecy-outage-probability]] — probability that the secrecy rate falls below target (the SOP analysis of the secure-RIS source).
- [[queueing-theory]] — delay/queue-length analysis backbone of [[zhang-2020-response-delay-uav-swarm]].
- [[beta-policy-drl]] — Beta-distribution actor output for bounded actions (the b-MAPPO refinement).
- [[robust-offloading]] — bounded-uncertainty robust offloading (scheduling/channel/computation robustness).
- [[cooperative-jamming]] — reusing network nodes as helper jammers for PLS (the USV jamming of [[li-2023-secure-marine-iot-jamming]]).
- [[cross-entropy-method]] — sampling-based stochastic metaheuristic (the CASE algorithm of the secure-marine source).

All other referenced concepts reused existing slugs (e.g. [[mobile-edge-computing]], [[task-offloading]], [[multi-uav-assisted-mec]], [[maritime-mec]], [[load-balancing-uav-mec]], [[differential-evolution]], [[deep-q-network]], [[noma]], [[physical-layer-security]], [[intelligent-reflecting-surface]], [[monotonic-optimization]], [[fractional-programming-dinkelbach]], [[alternating-optimization-sdr-sca]], [[rotary-wing-propulsion-energy-model]], [[mappo]], [[csi-estimation-error]], [[centralized-training-decentralized-execution]], [[stochastic-geometry-network-analysis]], [[mmwave-radar-sensing]], [[two-stage-decomposition]], [[high-altitude-platform-station]], [[low-altitude-intelligent-network]], [[blockage-aware-channel-model]], [[terrain-aware-channel-model]], [[post-disaster-mec]], [[energy-latency-tradeoff]], [[uav-trajectory-control]]).

### Entities — 3 new + roster updates + 1 namesake deferral

- **Created (3):** [[liping-qian]] (Zhejiang Univ. of Technology, `lpqian@zjut.edu.cn`; 3 sources — [[dai-2024-multiuav-marine-welfare]] + [[dai-2023-hybrid-marine-mmwl]] + [[li-2023-secure-marine-iot-jamming]]); [[minghui-dai]] (Univ. of Macau, `minghuidai@um.edu.mo`; first author of 2 — [[dai-2024-multiuav-marine-welfare]] + [[dai-2023-hybrid-marine-mmwl]]); [[zhiyong-feng]] (Beijing Univ. of Posts and Telecommunications, `fengzy@bupt.edu.cn`; 2 — [[zhang-2020-response-delay-uav-swarm]] + [[meng-2024-uav-isac-overview]], affiliation confirmed in both parses).
- **Roster updates (existing entities):** [[bin-lin]] (7→8, +secure-marine-jamming), [[yuan-wu]] (7→9, +marine-welfare +secure-marine-jamming), [[tony-q-s-quek]] (4→5, +marine-welfare), [[chunxiao-jiang]] (3→4, +load-balance IoT), [[zhu-han]] (5→6, +UAV-swarm response delay).
- **Deferred — Jingjing Wang namesake.** The "Jingjing Wang" co-authoring [[yang-2020-loadbalance-multiuav-iot]] is at **Tsinghua University** (`chinaeephd@gmail.com`, Shuimu Tsinghua Scholar), **not** the existing **Beihang** [[jingjing-wang]] entity (`drwangjj@buaa.edu.cn`). Different institution + email ⇒ treated as a genuine namesake and **not** merged; the Beihang entity roster was left unchanged and no Tsinghua entity was minted (the Tsinghua Jingjing Wang has only this one corpus source).
- The "Chunxiao Jiang" on [[yang-2020-loadbalance-multiuav-iot]] **is** the existing Tsinghua entity (`jchx@tsinghua.edu.cn`-matched) — roster bumped.
- No author-entity links were embedded in source-page bodies (matching the established house convention).

### Duplicate / near-duplicate check

Verified each batch-6 paper is **genuinely new** and distinct from existing pages:
- [[yang-2020-loadbalance-multiuav-iot]] (load-balance via DE+GAP+DQN, IoT-J 2020) is distinct from the other multi-UAV-MEC sources ([[seid-2021-madrl-multiuav-iot-edge]] MADDPG clustered IoT-edge, [[zhao-2022-matd3-multiuav-ec-offloading]] MATD3) — different method (classical metaheuristic + single-agent DQN), objective (load balance), authors, year.
- [[dai-2024-multiuav-marine-welfare]] (double-auction system-welfare, TCOMM 2024) and [[dai-2023-hybrid-marine-mmwl]] (hybrid FDMA/NOMA MMWL, TCOMM 2023, already curated in batch 4) are the **same group** (Minghui Dai / Yuan Wu / Liping Qian) but **distinct papers** — different objective (system-revenue vs min-max-latency), mechanism (double auction vs layered convex), year, DOI.
- [[li-2023-secure-marine-iot-jamming]] (USV cooperative jamming, TVT 2023) is distinct from the other maritime sources — unique NOMA-via-HAP + cooperative-jamming PLS framing.
- [[michailidis-2024-secure-ris-uav-mec-iot]] (secure UAV-RIS-MEC, TCOMM 2024) is distinct from [[yao-2025-secure-isac-dual-eavesdropping]] (ISAC dual-eavesdropping) — RIS + MEC + SOP-over-Nakagami-m vs ISAC secrecy/sensing.
- [[zhang-2020-response-delay-uav-swarm]] (stochastic-geometry/queueing response delay, TVT 2020) is distinct from the DRL/game-theoretic UAV-swarm sources — analytical PPP + queueing backbone, hardware-validated.
- [[li-2024-robust-bmappo-multiuav-mec]] (robust b-MAPPO, IoT-J 2024) is distinct from the other MAPPO/MADDPG UAV-MEC sources by its joint communication+computation uncertainty robustness + Beta policy.
- No same-paper/different-UUID duplicate ingests were found among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded in the parse (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch** — all 7 source pages have full title/authors/year/url/venue. **Year convention:** for papers whose publication vs current-version dates straddle two years, year follows date-of-current-version (the wiki's established convention), with both dates recorded in each citation.
- **Grounded headline claims only:** the verbatim figures — Zhang 10–20% response-delay cut + 89.9% packet reduction (52 s/7.84 Mbit → 9 key frames/775.9 kbit), Li b-MAPPO avg UE reward ≈ −3.05, Li secure-marine 27.32% energy reduction vs fixed jamming — are quoted from the parse text. Dai marine-welfare revenue/energy trade-off, Michailidis SCE/SOP behavior (element-count thresholds ~57/~60), Yang DRL-vs-FCFS/SJF/RR advantage, and Al-Hourani altitude/elevation-angle results are stated **qualitatively** as the papers state them, with figure-only magnitudes flagged as indicative.
- **Wikilink integrity:** wiki-wide link check after the pass = **ZERO dangling links** (verified — see below). All wikilinks introduced this batch target existing slugs or pages created in this same batch (7 sources + 10 concepts + 3 entities). Pre-existing dangling-link status unchanged (none). Two drafting-time fragmentations were caught before audit (an over-split `line-of-sight-probability-model` folded into [[air-to-ground-channel-model]]; a `response-delay-optimization-uav-swarm` finding reference removed since no finding page was created; a stray `qixun-zhang` author wikilink converted to plain text).
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 10 concept stubs and 3 entity pages. No diagnostics issues; no self-references or duplicate `related` entries.
- **Counts reconciled:** **124 sources / 207 concepts / 57 author entities (+[[pytorch]] = 58 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-6 folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 5/8: 7 new sources + audit)

Fifth batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned batch-5 folders; the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **110 → 117 curated sources**. (Clean retry: a prior attempt was cancelled before writing; confirmed none of the 7 already had a source page.)

### New source pages (7)

- [[duan-2023-moto-smallcell-offloading]] — Duan et al. 2023 (**IEEE TMC**, `10.1109/TMC.2022.3220720`). **MOTO** — mobility-aware online task offloading + adaptive load balancing in terrestrial **small-cell MEC**; decomposes the intractable TOO problem into Task offloading Control (LSTM) + Server Grouping (Dueling Double DQN); trace-driven on a real WiFi dataset. DOI pub 8 Nov 2022 / current version 5 Dec 2023 → year 2023.
- [[qi-2024-msar-minmax-latency]] — Qi et al. 2024 (**IEEE TVT**, `10.1109/TVT.2024.3384570`). Multi-UAV maritime **search & rescue** (S-UAVs + R-UAV); minimizes the **maximum total latency** among S-UAVs over offloading + R-UAV deployment + S-UAV–target association; iterative decomposition: linearization + **SCA** + **Branch-and-Bound**. DOI pub 3 Apr 2024 / current version 19 Sep 2024 → year 2024.
- [[seid-2021-madrl-multiuav-iot-edge]] — Seid et al. 2021 (**IEEE TNSM**, `10.1109/TNSM.2021.3096673`). Clustered multi-UAV IoT-edge offloading + resource allocation as a **stochastic game**; **MADDPG** (MADRL) minimizing energy+delay cost. Reports (verbatim) cost ↓ 38.643% / 55.621% and reward ↑ 58.289% / 85.289% vs single-agent DRL / heuristic. DOI pub 12 Jul 2021 / current version 9 Dec 2021 → year 2021.
- [[wang-2021-maddpg-multiuav-trajectory]] — Wang et al. 2021 (**IEEE TCCN**, `10.1109/TCCN.2020.3027695`). **MADDPG** per-UAV trajectory planning for multi-UAV MEC; jointly optimizes geographical fairness + UE-load fairness + UE energy; low-complexity offloading step given trajectories. DOI pub 29 Sep 2020 / current version 8 Mar 2021 → year 2021.
- [[peng-2020-maddpg-uav-vehicular]] — Peng & Shen 2020 (**IEEE JSAC**, `10.1109/JSAC.2020.3036962`). **MADDPG** multi-dimensional resource management (vehicle association + allocation) for MEC- and UAV-assisted vehicular networks; converges within ~200 episodes (verbatim), higher delay/QoS satisfaction than SADDPG/random. DOI pub 10 Nov 2020 / current version 16 Dec 2020 → year 2020.
- [[sun-2024-mfris-semantic-antijamming]] — Sun et al. 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3459028`). **Multi-functional RIS** + **semantic** anti-jamming communication and computing for an MEC integrated aerial-ground network; worst-case imperfect-jammer-CSI; semantic-computation-rate maximization via a fast-converging **monotonic optimization + decoupling SOCP (MO-DSOCP)** (global optimum) + low-complexity **GPI**. DOI pub 12 Sep 2024 / current version 22 Nov 2024 → year 2024 (earlier WCSP 2024 version noted).
- [[li-2024-emssa-uav-swarm-vaa]] — Li et al. 2024 (**IEEE TMC**, `10.1109/TMC.2023.3298888`). **Virtual antenna arrays** for UAV-swarm-assisted IoT data harvesting/dissemination; introduces collaborative beamforming into *both* sensors (GVAA) and UAVs (AVAA); multi-objective (completion time / eavesdropper signal / UAV energy) proven NP-hard, solved by the **enhanced multi-objective salp swarm algorithm (EMSSA)**. DOI pub 26 Jul 2023 / current version 4 Apr 2024 → year 2024.

### New concept stubs (7)

- [[maddpg]] — the standalone Multi-Agent Deep Deterministic Policy Gradient backbone page (deterministic-policy CTDE), distinct from [[multi-agent-td3]] / [[masac]]; grounds the three batch-5 MADDPG papers plus the pre-existing [[he-2023-fairness-3d-multiuav-maddpg]] / [[du-2023-maddpg-service-placement-agin]].
- [[small-cell-mec]] — MEC integrated with small-cell SBS networks; uneven spatio-temporal load + mobility challenges (grounds MOTO).
- [[mobility-aware-offloading]] — offloading control that accounts for user mobility / unknown future loads via online prediction.
- [[semantic-communication]] — 6G key-information (vs bit) transmission; robustness + data compression for MEC.
- [[multi-functional-ris]] — RIS with reflection + refraction + amplification + energy harvesting (full-space, self-sustaining).
- [[monotonic-optimization]] — global-optimization framework exploiting monotonicity (the MO-DSOCP solver behind the MF-RIS source).
- [[salp-swarm-algorithm]] — leader/follower swarm-intelligence metaheuristic; EMSSA multi-objective variant grounds the VAA source.

All other referenced concepts reused existing slugs (e.g. [[mobile-edge-computing]], [[task-offloading]], [[multi-uav-assisted-mec]], [[vehicular-mec]], [[maritime-mec]], [[centralized-training-decentralized-execution]], [[stochastic-game]], [[ddqn]], [[deep-q-network]], [[ddpg]], [[collaborative-beamforming]], [[uav-data-collection]], [[physical-layer-security]], [[intelligent-reflecting-surface]], [[anti-jamming-mec]], [[air-ground-integrated-network]], [[csi-estimation-error]], [[mixed-integer-nonlinear-programming]], [[multi-objective-reinforcement-learning]], [[fairness-metrics-in-mec]], [[jains-fairness-index]], [[two-stage-decomposition]], [[uav-trajectory-control]], [[binary-vs-partial-offloading]], [[load-balancing-uav-mec]], [[dynamic-qos-constraints]], [[uav-enabled-its]], [[video-analytics-offloading]]).

### Entities — 4 new + roster updates (no deferrals this batch)

- **Created (4):** [[kezhi-wang]] (Northumbria University, `kezhi.wang@northumbria.ac.uk`; 3 sources — [[wang-2022-cat-rat-fmec-trajectory]] + [[wang-2021-maddpg-multiuav-trajectory]] + [[wang-2019-todetas-deployment-scheduling]], frequently corresponding author, anchors the Northumbria UAV-MEC group); [[xuemin-shen]] (University of Waterloo, `sshen@uwaterloo.ca`; 2 sources — [[peng-2020-maddpg-uav-vehicular]] + [[duan-2023-moto-smallcell-offloading]]); [[yuguang-fang]] (City University of Hong Kong, `my.fang@cityu.edu.hk`; 2 sources — [[wang-2024-maritime-eh-jcora]] + [[qi-2024-msar-minmax-latency]], in the [[bin-lin]] maritime cluster); [[haixia-peng]] (University of Waterloo → Xi'an Jiaotong University; 2 sources — [[peng-2020-maddpg-uav-vehicular]] + [[wang-2024-twotier-satellite-marine]], the affiliation move is documented in both parses so treated as one researcher, not a namesake).
- **Roster updates (existing entities):** [[geng-sun]] (8→9 sources, +VAA), [[jiahui-li]] (7→8, +VAA as lead author), [[qingqing-wu]] (5→6, +VAA — **confirms the SJTU [[qingqing-wu]]** `qingqingwu@sjtu.edu.cn` on this paper, unrelated to the deferred NUS namesake), [[bin-lin]] (6→7, +MSAR min-max-latency).
- No author-entity links were embedded in source-page bodies (matching the established house convention).

### Duplicate / near-duplicate check (the assigned watch item)

The brief warned that several already-curated "Multi-Agent … Multi-UAV … MEC" papers could be confused with these. Verified each batch-5 paper is **genuinely new** and distinct:
- [[wang-2021-maddpg-multiuav-trajectory]] (*…Trajectory Planning…*, **IEEE TCCN 2021**, MADDPG, dual-fairness + energy) is **distinct** from the same group's already-curated [[wang-2022-cat-rat-fmec-trajectory]] (*Dynamic Trajectory Control…*, **IEEE TMC 2022**, CAT/RAT single twin-DQN agent) — different venue, DOI, year, and single-vs-multi-agent method — and from [[chang-2022-marl-multiuav-trajectory]] (TNSE).
- [[seid-2021-madrl-multiuav-iot-edge]] (UESTC/DFKI, **TNSM 2021**, MADDPG, clustered IoT-edge) is **distinct** from [[zhao-2022-matd3-multiuav-ec-offloading]] (MATD3, TWC 2022) and [[he-2023-fairness-3d-multiuav-maddpg]] (MADDPG fairness 3D) — different authors, venue, year.
- [[peng-2020-maddpg-uav-vehicular]] (Peng/Shen, **JSAC 2020**) is a new vehicular-MEC entry distinct from the corpus's other vehicular papers ([[ma-2025-pdqn-vehicular-mec]], [[zhang-2025-mcma-task-migration]], [[sun-2023-bargain-match-vec]]).
- [[qi-2024-msar-minmax-latency]] (S-UAV/R-UAV min-max latency, TVT 2024) is **distinct** from [[wang-2026-aerial-marine-msar]] (UAV+HAPS+MASS three-tier JCORA, matching+convex+PGD) despite both being Bin-Lin-group maritime SAR papers — different architecture, objective, method, venue, year.
- [[li-2024-emssa-uav-swarm-vaa]] (salp-swarm CB virtual antenna arrays, TMC) is **distinct** from [[sun-2025-emoppo-vlh-aerial-cb]] / [[li-2024-emodrl-ground-space-cb]] (evolutionary-RL CB) — pure swarm-intelligence optimizer, IoT data-harvesting framing.
- No same-paper/different-UUID duplicate ingests were found among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded in the parse (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch** — all 7 source pages have full title/authors/year/url/venue. **Year convention:** for the TMC/TVT/TCCN/JSAC/TNSM papers whose publication vs current-version dates straddle two years, year follows date-of-current-version (the wiki's established convention), with both dates recorded in each citation.
- **Grounded headline claims only:** Seid MADRL percentages (38.643% / 55.621% cost, 58.289% / 85.289% reward) and Peng "converges within 200 episodes" are verbatim from the abstracts; MOTO load-balancing/cost advantage, MSAR effectiveness, MF-RIS superiority, and EMSSA "reduce time and energy costs significantly" are stated **qualitatively** as the papers state them (no figure-only magnitudes asserted as exact). The MOTO dataset scale (29,284,966 records / 21,725 users / 4,045 APs) and the >80%-under-600 s CDF observation are from the parse (CDF flagged as read-from-figure).
- **Wikilink integrity:** wiki-wide Obsidian-faithful link check after the pass = **ZERO dangling links** (verified — see below). All wikilinks introduced this batch target existing slugs or pages created in this same batch (7 sources + 7 concepts + 4 entities). Pre-existing dangling-link status unchanged (none).
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 7 concept stubs and 4 entity pages. No diagnostics issues; no self-references or duplicate `related` entries.
- **Counts reconciled:** **117 sources / 197 concepts / 54 author entities (+[[pytorch]] = 55 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned batch-5 folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 4/8: 7 new sources + audit)

Fourth batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned `batch4` folders (per `.curation-out/batches.json`); the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **103 → 110 curated sources**.

### New source pages (7)

- [[wang-2024-maritime-eh-jcora]] — Wang et al. 2024 (**IEEE IoT-J**, `10.1109/JIOT.2024.3371049`). Energy-harvesting maritime MEC: a two-tier sea-lane-monitoring network (CBS + solar/ocean-wave-powered maritime information stations / buoys serving vessels); maximizes long-term throughput under queue-stability + energy constraints via **Lyapunov** drift-plus-penalty decomposition → **JCORA**. Beats FRA/LRA/PRA/TRA benchmarks (curves read from Figs. 7–12, reported qualitatively). DOI pub 28 Feb 2024 / current version 23 May 2024 → year 2024.
- [[hu-2019-pdd-uav-mec-offloading]] — Hu et al. 2019 (**IEEE IoT-J**, `10.1109/JIOT.2018.2878876`). Single-UAV MEC; minimizes the sum of per-slot **max delay** by jointly optimizing offloading ratio + UAV trajectory + binary user scheduling via **penalty dual decomposition (PDD)** (inner CCCP, outer AL-multiplier/penalty update) + a simplified l0-norm variant. DOI pub 31 Oct 2018 / current version 8 May 2019 → year 2019.
- [[niazmand-2025-jopa-dnn-pruning-iiot]] — Niazmand & Ye 2025 (**IEEE TCCN**, `10.1109/TCCN.2025.3529688`). Joint task offloading + **DNN model pruning** + edge resource allocation (JOPA) for industrial-washing-machine fault detection; maximizes long-term resource utilization under **time-varying delay/accuracy QoS**; formulated as a **Markov reward process**, solved with a hybrid-action **SAC**. Highest utilization + lowest task-dropping (<1%) vs JOPAV1/AGDM (Figs. 9–12, qualitative). DOI pub 14 Jan 2025 / current version 8 Oct 2025 → year 2025.
- [[wu-2018-multiuav-minrate-trajectory]] — Wu, Zeng & Zhang 2018 (**IEEE TWC**, `10.1109/TWC.2017.2789293`, 17(3):2109–2121). Foundational multi-UAV-as-base-station **max-min-rate** design; joint scheduling/association + trajectory + power via **BCD + SCA** with circle-packing initialization; reveals throughput-access-delay tradeoff. DOI pub 5 Jan 2018 / current version 8 Mar 2018 → year 2018. (Vol/issue/pages from in-parse reference list entry [9].)
- [[dai-2023-hybrid-marine-mmwl]] — Dai et al. 2023 (**IEEE TCOMM**, `10.1109/TCOMM.2023.3306581`). Hybrid offshore (FDMA) + aerial-UAV (NOMA) multi-access offloading; **Minimize Maximum Workloads Latency (MMWL)** via a layered 3-subproblem decomposition. Within ~3% of LINGO's global optimum with >90% time saving (verbatim). DOI pub 18 Aug 2023 / current version 20 Nov 2023 → year 2023.
- [[wu-2024-urllc-uav-mec-latency]] — Wu et al. 2024 (**IEEE TWC**, `10.1109/TWC.2023.3307154`). First UAV-MEC study to drop the infinite-blocklength assumption: **URLLC / finite-blocklength** offloading under angle-dependent **Rician fading**; min-max latency via **BCD + SCA** over UAV 3D location + bandwidth + CPU frequency (semi-closed-form). DOI pub 28 Aug 2023 / current version 11 Apr 2024 → year 2024.
- [[zhang-2025-vnf-sgin-dql]] — Zhang et al. 2025 (**IEEE TVT**, `10.1109/TVT.2024.3454438`). **NFV/SDN service-function-chaining** for 6G satellite-ground integrated networks; dynamic VNF selection + chaining (DDVSC) via **deep Q-learning** with load-clustered greedy action space; maximizes long-term network profit (provisioning + migration cost vs performance). DOI pub 30 Sep 2024 / current version 16 Jan 2025 → year 2025.

### New concept stubs (7)

- [[energy-harvesting-mec]] — MEC powered by harvested renewable energy (solar/wind/ocean-wave), distinct from RF-harvesting/WPT; grounds the maritime-EH source.
- [[penalty-dual-decomposition]] — the PDD framework (binary→equality reformulation + augmented-Lagrangian + two-layer CCCP iteration) for non-convex coupled problems.
- [[markov-reward-process]] — MDP variant with action-independent state transitions; the formulation behind the IIoT DNN-pruning source.
- [[dynamic-qos-constraints]] — time-varying per-task delay/accuracy requirements tied to changing criticality levels.
- [[finite-blocklength-urllc]] — short-packet URLLC where the Shannon formula overstates rate; the angle-dependent-Rician finite-blocklength rate of the URLLC source.
- [[network-function-virtualization]] — NFV/SDN substrate (VNFs on commodity servers) for the SGIN VNF-chaining source.
- [[service-function-chaining]] — ordered VNF chains (SFC) + VSCP selection/mapping, with satellite-movement-driven VNF migration.

All other referenced concepts reused existing slugs (e.g. [[maritime-mec]], [[lyapunov-optimization]], [[task-offloading]], [[task-migration]], [[noma]], [[mixed-integer-nonlinear-programming]], [[two-stage-decomposition]], [[alternating-optimization-sdr-sca]], [[uav-trajectory-control]], [[multi-uav-assisted-mec]], [[binary-vs-partial-offloading]], [[soft-actor-critic]], [[hybrid-action-decision-making]], [[dnn-model-partition]], [[knowledge-distillation-for-drl]], [[deep-q-network]], [[leo-satellite-edge-computing]], [[non-terrestrial-network]], [[space-air-ground-integrated-network]], [[fairness-metrics-in-mec]], [[network-slicing]]).

### Entities — roster updates + 2 deferrals (no new entity pages)

- **Roster updates (existing entities):** [[qiang-ye]] (3→6 sources — the **cross-cutting thread of batch 4**, on 4 of the 7 papers: maritime-EH, IIoT DNN-pruning, VNF/SGIN; University of Calgary, `qiang.ye@ucalgary.ca`), [[bin-lin]] (4→6, +maritime-EH +hybrid-marine; Dalian Maritime Univ.), [[zhen-wang]] (3→4, +maritime-EH; same Dalian Maritime/Neusoft dual affiliation + `wangzhen_jsj@neusoft.edu.cn`), [[yuan-wu]] (6→7, +hybrid-marine; Univ. of Macau, corresponding author), [[qingqing-wu]] (4→5, +URLLC; **SJTU** `qingqingwu@sjtu.edu.cn`-matched).
- **Deferred — Qingqing Wu namesake (again).** The batch-4 [[wu-2018-multiuav-minrate-trajectory]] is **first-authored** by a "Qingqing Wu" at the **National University of Singapore** (`elewuqq@nus.edu.sg`), not the SJTU [[qingqing-wu]] entity (`qingqingwu@sjtu.edu.cn`). Consistent with the batch-1 deferral on the 2019 NUS tutorial, this 2018 NUS paper was **not** added to the SJTU roster — noted on the entity page; plausibly the same person earlier in his career, flagged for human confirmation.
- **Deferred — Yong Zeng / Rui Zhang entity creation.** "Yong Zeng" now recurs in 3 sources ([[wu-2018-multiuav-minrate-trajectory]], [[zeng-2019-uav-comm-tutorial-5g]], [[zeng-2019-rotary-wing-energy-min]]) and "Rui Zhang" likewise, both NUS-affiliated. They clear the recurrence bar for entity pages, but affiliation verification across all three parses was not completed this pass, so no entity was minted — flagged for a future pass / human confirmation rather than created hastily.
- No author-entity links were embedded in source-page bodies (matching the established house convention — three accidental author wikilinks introduced during drafting were caught and converted to plain text before the audit).

### Duplicate / near-duplicate check (the assigned watch item)

The batch brief warned that several already-curated "Joint … UAV … MEC" papers could be confused with these. Verified each batch-4 paper is **genuinely new** and distinct from existing pages:
- [[hu-2019-pdd-uav-mec-offloading]] (Hu/Cai/Yu, *Joint Offloading and Trajectory Design …*, IoT-J 2018/2019, PDD) is **distinct** from the already-curated [[yu-2020-uav-ec-collaborative-offloading]] (Yu/Gong, *Joint Task Offloading and Resource Allocation …*, IoT-J 2020, SCA) — different authors, DOI, year, method.
- [[wu-2018-multiuav-minrate-trajectory]] (*Joint Trajectory and Communication Design for Multi-UAV …*, TWC 2018, BCD+SCA, communications/max-min-rate) is **distinct** from [[chang-2022-marl-multiuav-trajectory]] (*Trajectory Design and Resource Allocation for Multi-UAV …*, TNSE 2022, DRL) — different title, authors, venue, year, method.
- [[wang-2024-maritime-eh-jcora]] and [[dai-2023-hybrid-marine-mmwl]] are new maritime sources distinct from the existing 8 maritime pages (different architectures: EH-buoys+Lyapunov vs FDMA/NOMA hybrid offshore+aerial).
- No same-paper/different-UUID duplicate ingests were found among the 7.

### Audit (correctness-first)

- **DOI / venue / year** — all 7 carry an explicit `Digital Object Identifier` line in their own parse; every DOI, venue, and year above is grounded in the parse (manuscript date-of-publication / date-of-current-version lines). **Zero `not in parse` metadata fields this batch** — all 7 source pages have full title/authors/year/url/venue. **Year convention:** for the five TVT/TWC/TCOMM/IoT-J papers whose publication vs current-version dates straddle two years, year follows date-of-current-version (the wiki's established convention), with both dates recorded in each citation.
- **Grounded headline claims only:** maritime-EH JCORA throughput/latency advantages stated qualitatively (Figs. 7–12 are MinerU-rendered tables, not verbatim text); hybrid-marine "≤3% from LINGO global optimum" + ">90% time saving" verbatim from the parse abstract/contributions; URLLC bottleneck insight + "finite-blocklength necessary" from the conclusion; IIoT JOPA "<1% dropping" + "p=0.7 balances" from Sec. V; PDD/min-max-rate/VNF-DQL results stated as the papers state them ("significantly outperform", "approaches the upper bound"). No figure-only magnitudes asserted as exact.
- **Wikilink integrity:** wiki-wide Obsidian-faithful check after the pass = **ZERO dangling links** (`.curation-out/linkcheck2.py`). All wikilinks introduced this batch target existing slugs or pages created in this same batch (7 sources + 7 concepts). Pre-existing dangling-link status unchanged (none).
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 7 concept stubs. No diagnostics issues; no self-references or duplicate `related` entries.
- **Counts reconciled:** **110 sources / 190 concepts / 50 author entities (+[[pytorch]] = 51 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned `batch4` folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 3/8: 7 new sources + audit)

Third batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned `batch3` folders (per `.curation-out/batches.json`); the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **96 → 103 curated sources**.

### New source pages (7)

- [[qu-ecoei-uav-swarm]] — Qu et al. (**IEEE Communications Magazine**, `10.1109/MCOM.002.2300129`). **eCoEI** — OODA-loop-based elastic collaborative DL inference for UAV swarms, robust to node/A2A-link failure; proof-of-concept on 4 airborne Jetson devices (Faster R-CNN; ≈0.8→2.9 FPS with more UAVs; keeps running at ≈2 FPS when one UAV drops). **Year: not in parse** (magazine parse has no manuscript-date/volume line); DOI from parse, venue from parse.
- [[cheng-2025-dos-satellite-edge-computing]] — Cheng et al. 2025 (**IEEE TVT**, `10.1109/TVT.2024.3483203`). **DOS** — energy-constrained LEO satellite edge computing for STINs; Lyapunov + convex decomposition under satellite solar-harvest/eclipse dynamics + location-dependent stochastic task arrivals; near-optimal, beats GE/OPT/GS/DFO; 37.4% completion-time cut vs GE with UD assistance. DOI pub 17 Oct 2024 / current version 14 Feb 2025 → year 2025 (current-version convention); earlier ICC 2022 version noted.
- [[li-2024-rldc-uav-swarm-clustering]] — Li et al. 2024 (**IEEE WCNC 2024**, `10.1109/WCNC57260.2024.10570678`). **Conference precursor** of the already-curated journal paper [[li-2025-stochastic-game-uav-swarm]] (see duplicate decision). Energy-efficient UAV-swarm MEC with dynamic clustering as **six** coupled multi-agent stochastic games + RLDC Q-learning; **no** NE/convergence proof; 6 authors (NUAA+Concordia); 2500 m × 2500 m region. Own parse has **no** DOI/venue/year line — metadata grounded in the journal version's explicit WCNC-2024 cross-reference (DOI included) + web-confirmed title (arXiv:2402.18936).
- [[zeng-2019-rotary-wing-energy-min]] — Zeng, Xu & Zhang 2019 (**IEEE TWC**, `10.1109/TWC.2019.2902559`, 18(4):2329–2345). Foundational **rotary-wing UAV propulsion-energy model** + energy-minimizing trajectory; fly-hover-communicate (TSPN + convex) and communicate-while-flying (path discretization + SCA). Metadata grounded in the parse's `Digital Object Identifier` line + corpus reference DB (vol/issue/pages).
- [[pervez-2024-acm-multiuav-mec]] — Pervez et al. 2024 (**IEEE TWC**, `10.1109/TWC.2023.3291692`). Multi-UAV + BS MEC weighted energy+latency minimization via three-layer **ACM** (potential-game offloading/server-selection with proven NE + GWF power + SCA trajectory + gradient-descent CPU); ~10–12% cost cut vs two prior joint methods. DOI pub 11 Jul 2023 / current version 12 Mar 2024 → year 2024.
- [[du-2024-gdm-network-optimization-tutorial]] — Du et al. 2024 (**IEEE COMST**, `10.1109/COMST.2024.3400011`). **Tutorial** on generative diffusion models (GDMs) for network optimization, focused on enhancing DRL; case studies on DRL / incentive-mechanism / ISAC / SemCom / IoV; worked sum-rate example. DOI pub 10 May 2024 / current version 22 Nov 2024.
- [[wang-gai-isac-physical-layer]] — Wang et al. (**IEEE Wireless Communications**, `10.1109/MWC.013.2300485`). Overview of **generative AI for ISAC** from the physical-layer perspective; five GAI models (GAN/NF/VAE/DFM/Transformer) + a diffusion **SSG** near-field DoA case study (MSE ≈ 1.03°). **Year: not in parse** (magazine parse has no manuscript-date/volume line); DOI + venue from parse.

### New concept stub (1)

- [[rotary-wing-propulsion-energy-model]] — the closed-form rotary-wing propulsion power model (blade-profile + induced + parasite terms; finite hover power; neither convex nor concave) from [[zeng-2019-rotary-wing-energy-min]], reused as the propulsion reference across the corpus's UAV-MEC energy formulations (e.g. [[li-2024-rldc-uav-swarm-clustering]]).

All other referenced concepts reused existing slugs (e.g. [[stochastic-game]], [[dynamic-uav-clustering]], [[multi-agent-q-learning]], [[intra-swarm-task-delegation]], [[collaborative-dl-inference]], [[dnn-model-partition]], [[pipeline-parallel-inference]], [[elastic-task-scheduling]], [[leo-satellite-edge-computing]], [[lyapunov-optimization]], [[potential-game]], [[nash-equilibrium]], [[alternating-optimization-sdr-sca]], [[generative-diffusion-model]], [[diffusion-model-as-optimizer]], [[integrated-sensing-and-communication]], [[conditional-gan]]).

### Entities — 2 new + roster updates + 1 deferral

- **Created (2):** [[yuben-qu]] and [[hao-sun]] — both **Nanjing University of Aeronautics and Astronautics (NUAA)**, Key Laboratory of Dynamic Cognitive System of Electromagnetic Spectrum Space; each recurs in 2 corpus sources ([[qu-ecoei-uav-swarm]] + [[sun-2024-asap-uav-swarm]]) with identical `@nuaa.edu.cn` emails (`quyuben@`, `sunhaosn@`). Unambiguous, affiliation-consistent (same bar as batch-1's boxiong-wang/hui-kang). Note: Hao **Sun** (NUAA) is distinct from the Jilin/NTU [[geng-sun]] — surname-only collision, no relation implied.
- **Roster updates (existing entities):** [[chao-dong]] (4→5 sources, +eCoEI), [[qihui-wu]] (5→6, +eCoEI), [[jiawen-kang]] (7→10, +eCoEI/+GDM-tutorial/+GAI-ISAC), [[dusit-niyato]] (12→14, +GDM-tutorial/+GAI-ISAC), [[jiacheng-wang]] (5→7, +GDM-tutorial/+GAI-ISAC), [[tony-q-s-quek]] (3→4, +satellite-DOS).
- **Deferred (human confirmation, again):** **Hongyang Du** — lead author of [[du-2024-gdm-network-optimization-tutorial]] (parse defers affiliations to an acknowledgment section not present in the body) and co-author of [[wang-gai-isac-physical-layer]] (lists him at **NTU**). His affiliation has varied across the corpus (NTU vs University of Hong Kong in earlier batches), so — consistent with the batch-2 deferral — **no entity page was minted**; flagged for human confirmation.
- No author-entity links were embedded in source pages (matching the established house convention).

### Duplicate decision — folder #3 (the assigned watch item)

`Energy-Efficient_UAV_Swarm_Assisted_MEC_With_Dynamic_Clustering_and_Scheduling` is **NOT a duplicate** of the already-curated [[li-2025-stochastic-game-uav-swarm]] (raw folder `A_Reinforcement_Learning-Based_Stochastic_Game_...`). It is its **conference precursor**: the journal version (IEEE TGCN, 8 authors, **five** stochastic games, with NE-existence proof + convergence/complexity analysis) explicitly states it "was presented in part at the IEEE WCNC 2024, Dubai, UAE [DOI: 10.1109/WCNC57260.2024.10570678]." The conference paper differs materially — **6 authors** (Li, Chen, Yi, Zhang, Zhu, **Cai**; NUAA + **Concordia**), **six** games (separate leader/follower trajectory games LTSG/FTSG), a larger **2500 m × 2500 m** region, and **no** NE/convergence proof. Curated as a distinct page [[li-2024-rldc-uav-swarm-clustering]] and bidirectionally cross-linked with the journal version.

### Audit (correctness-first)

- **DOI / venue / year** verified against each parse. Five of seven carry a usable metadata line: Cheng/TVT (`Digital Object Identifier 10.1109/TVT.2024.3483203` + manuscript dates), Zeng/TWC (`10.1109/TWC.2019.2902559` + dates + corpus-DB vol/issue/pages), Pervez/TWC (`10.1109/TWC.2023.3291692` + dates), Du/COMST (`10.1109/COMST.2024.3400011` + dates), Wang/MWC (`10.1109/MWC.013.2300485`, DOI only — **no** year line), Qu/MCOM (`10.1109/MCOM.002.2300129`, DOI only — **no** year line). The two IEEE-magazine papers ([[qu-ecoei-uav-swarm]], [[wang-gai-isac-physical-layer]]) have **no manuscript-date/volume line in the parse**, so `year` is left **empty (not in parse)** with the absence noted in each citation; web search did not provide an authoritative parse-overriding year, so none was invented. [[li-2024-rldc-uav-swarm-clustering]] has **no** metadata line at all in its own parse → grounded via the journal version's in-parse WCNC-2024 cross-reference + web-confirmed title.
- **Year convention:** for the TVT/TWC papers whose date-of-publication and date-of-current-version straddle two years, the year follows the date-of-current-version (the wiki's established convention), with both dates recorded in the citation.
- **Grounded headline claims only:** eCoEI FPS figures and the drop/recover behavior are from the parsed Figs. 5–6 (flagged read-from-figure); DOS "37.4% on average vs GE" and "5.72% improvement needs >1.88× energy" are verbatim from the parse; Zeng results stated qualitatively (figure curves, no fabricated magnitudes); Pervez "~10–12% vs [39]/[40]" and "converges in ~9 iterations" verbatim from the parse; Wang SSG "MSE ≈ 1.03°" and CSI "−7.05 dB vs −2.46 dB" verbatim. UAV-swarm-clustering energy-efficiency magnitudes flagged as read from MinerU figure tables (units unlabeled).
- **Wikilink integrity:** Obsidian-faithful wiki-wide check (`.curation-out/linkcheck2.py`, root indexed + inline-code spans stripped) = **ZERO dangling links** after the pass. All wikilinks introduced this batch target existing slugs or pages created/edited in this same batch.
- **Frontmatter:** `type`/`title`/`authors`/`year`/`url`/`venue`/`tags`/`related`/dates/H1 validated via diagnostics on all 7 source pages (the two magazine pages have intentionally empty `year`/`url`-present); `type`/`title`/`tags`/dates/H1 on the 1 concept + 2 entities. No diagnostics issues.
- **Counts reconciled:** **103 sources / 183 concepts / 50 author entities (+[[pytorch]] = 51 entity pages)**. `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned `batch3` folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 2/8: 7 new sources + audit)

Second batch of the deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned `batch2` folders (per `.curation-out/batches.json`); the other uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **89 → 96 curated sources**.

### New source pages (7)

- [[lyu-2023-noma-marine-emergency-offloading]] — Lyu et al. 2023 (**IEEE IoT-J**, `10.1109/JIOT.2023.3348164`). NOMA-based UAV emergency communication for marine IoT; MINLP minimizing device computation overhead (time + energy), decomposed into quasi-convex/convex resource allocation + a **coalition formation game** offloading algorithm (CGTO) reaching a Nash-stable solution.
- [[xiang-sac-mapless-robot-navigation]] — Xiang, Li, Dong & Ren (Beihang Univ.). Mapless mobile-robot navigation via **Soft Actor-Critic** with LSTM value/Q networks; laser+target→continuous velocity; Gazebo/ROS Turtlebot3. **Venue / year / DOI: not in parse** (parse has no publication line; an IEEE Xplore record exists for the title but its venue/year are not stated in the parse, so left blank rather than guessed). Foundational SAC entry.
- [[apostolopoulos-2021-prospect-theory-uav-offloading]] — Apostolopoulos et al. 2021 (**IEEE TMC**, `10.1109/TMC.2021.3069911`). Risk-aware partial data offloading across local / ground-MEC / UAV-MEC servers via **prospect theory**; non-cooperative game with proven unique Pure Nash Equilibrium. DOI grounded from an in-parse appendix link + web-confirmed (no header DOI line).
- [[wang-2022-cat-rat-fmec-trajectory]] — Wang et al. 2022 (**IEEE TMC**, `10.1109/TMC.2021.3059691`). Flying-MEC UAV trajectory + user association + resource allocation to minimize total UE energy; **CAT** (BCD convex) and **RAT** (twin-DQN actor-critic + Prioritized Experience Replay + matching). DOI publication 16 Feb 2021, current version 31 Aug 2022 → year 2022 per the current-version convention.
- [[bai-2024-delay-aware-cooperative-edge-cloud]] — Bai et al. 2024 (**IEEE TMC**, `10.1109/TMC.2022.3232375`). Delay-minimizing **cooperative** multi-UAV edge-cloud offloading; convex approximation + Lyapunov online decisions; cooperative-parallel-computing (slowest-node) delay model; model verified on a real UAV-edge platform. DOI publication 27 Dec 2022, current version 8 Jan 2024 → year 2024.
- [[du-2024-d2sac-aigc-asp-selection]] — Du et al. 2024 (**IEEE TMC**, `10.1109/TMC.2024.3356178`). Edge AIGC-as-a-Service provider selection; diffusion decision generator (AGOD) embedded in SAC → **D2SAC**; outperforms 7 DRL baselines. DOI publication 19 Jan 2024, current version 6 Aug 2024 → year 2024.
- [[miao-2022-gaglpp-drone-swarm-iiot]] — Miao et al. 2023 (**IEEE TII**, `10.1109/TII.2022.3196392`). Drone-swarm path planning for Industrial-IoT MEC; ground-station global + onboard local path planning (**GAGLPP**); priority/residual-energy/distance scheduling. DOI publication 4 Aug 2022, current version 4 May 2023 → year 2023.

### New concept stubs (2)

- [[soft-actor-critic]] — base single-agent **SAC** (maximum-entropy off-policy actor-critic), distinct from the existing multi-agent [[masac]]; grounds the navigation, D2SAC, and SAC-SK sources.
- [[prospect-theory]] — risk-aware decision-making under uncertainty (gain/loss value function, loss aversion), grounding the prospect-theoretic offloading game.

All other referenced concepts reused existing slugs (e.g. [[noma]], [[coalition-formation-game]], [[lyapunov-optimization]], [[deep-q-network]], [[prioritized-experience-replay]], [[diffusion-model-as-optimizer]], [[generative-diffusion-model]], [[nash-equilibrium]], [[two-stage-decomposition]], [[matching-theory-for-resource-allocation]], [[load-balancing-uav-mec]], [[parallel-vs-serial-processing]], [[mixed-integer-nonlinear-programming]]).

### Entities — roster updates + 1 deferral (no new entity pages)

- **Roster updates (existing entities):** [[dusit-niyato]] (11→12 sources, +[[du-2024-d2sac-aigc-asp-selection]]), [[jiawen-kang]] (6→7, +d2sac), [[zhu-han]] (4→5, +[[lyu-2023-noma-marine-emergency-offloading]]).
- **Deferred (human confirmation):** **Hongyang Du**, lead/equal-first author of [[du-2024-d2sac-aigc-asp-selection]], recurs in [[ye-2025-aigc-diffusion-contract]], but the two parses list **different affiliations** — d2sac: School of Computer Science and Engineering, **NTU** (`hongyang001@e.ntu.edu.sg`); ye-2025: Department of EEE, **University of Hong Kong** (`duhy@eee.hku.hk`, with a PhD-from-NTU bio). Plausibly the same person after a move, but to stay faithful to the house convention no entity page was minted; flagged here for human confirmation.
- No author-entity links were embedded in source pages (matching the established house convention).

### Audit (correctness-first)

- **DOI / venue / year** verified against each parse. Five of the seven carry a `Digital Object Identifier` line (Lyu/JIOT, Wang/TMC, Bai/TMC, Du/TMC, Miao/TII). [[apostolopoulos-2021-prospect-theory-uav-offloading]] has **no header DOI**, but an in-parse appendix link gives `10.1109/TMC.2021.3069911` (IEEE TMC), web-confirmed against the authors' record. [[xiang-sac-mapless-robot-navigation]] has **no venue/year/DOI in the parse at all**, web search did not authoritatively reveal the venue name/year → left **blank / not in parse** (year field empty, url/venue empty strings), with the absence noted in the citation.
- **Year convention:** for the four TMC/TII papers whose date-of-publication and date-of-current-version straddle two years, the year follows the date-of-current-version (the wiki's established convention), with both dates recorded in each citation line.
- **Grounded headline claims only:** CGTO "lowest computation overhead vs LC/OCG/HOCO/IOJRA/DDPG" (parse Section V); D2SAC "outperforms seven DRL algorithms" with the seven named (DQN/DRQN/Prioritized-DQN/Rainbow/REINFORCE/PPO/SAC) verbatim from the parse; RAT "≈ CAT, generalizes to any take-off point" (parse abstract/Sec. 7); GAGLPP "more offloading services + shorter path + greater energy efficiency" (parse abstract); Bai "near-optimal delay, platform-verified model" (parse abstract/contributions). No figure-only magnitudes were stated as exact.
- **Wikilink integrity:** all wikilinks introduced this batch target existing slugs or pages created in this same batch; two accidental self-referential `related` entries were caught and removed during writing. No NEW dangling links introduced (full wiki-wide check below).
- **Frontmatter:** `type`/`title`/`authors`/`year`/`venue`/`tags`/`related`/dates/H1 present on all 7 source pages (the navigation page's `year` is intentionally empty and `url`/`venue` empty strings = not in parse); `type`/`title`/`tags`/dates/H1 on the 2 concepts.
- **Counts reconciled:** 96 sources / 182 concepts / 48 author entities (+[[pytorch]] = 49 entity pages). `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned `batch2` folders were curated; other untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Curation pass (batch 1/8: 7 new sources + audit)

First batch of a deliberately-split 8-batch curation run over 52 newly-ingested raw papers (split to keep context clean and avoid misinformation). This run curated **only** the 7 assigned folders; the other 45 uncurated folders are owned by separate batch runs and were left untouched. Corpus grows **82 → 89 curated sources**.

### New source pages (7)

- [[zhou-2018-uav-wireless-powered-mec]] — Zhou et al. 2018 (**IEEE JSAC**, `10.1109/JSAC.2018.2864426`). Computation-rate maximization in UAV-enabled wireless-powered MEC; partial + binary offloading; two-stage / three-stage closed-form optimization. Classical-optimization + WPT anchor.
- [[fujimoto-2018-td3-actor-critic]] — Fujimoto, van Hoof & Meger 2018 (**ICML / PMLR 80**; **no DOI in parse**). Origin paper for **TD3** (clipped double-Q, delayed policy updates, target smoothing). Foundational DRL-method entry that grounds the wiki's TD3/MATD3 lineage.
- [[zeng-2019-uav-comm-tutorial-5g]] — Zeng, Wu & Zhang 2019 (**Proceedings of the IEEE**, `10.1109/JPROC.2019.2952892`). Tutorial on UAV communications for 5G+; UAV-assisted-comms vs cellular-connected-UAV taxonomy. Foundational survey anchor.
- [[wang-2025-sac-tma-mec-dc]] — Wang et al. 2025 (**IEEE IoT-J**, `10.1109/JIOT.2025.3542025`). Joint multi-AAV MEC + data collection; SAC + two-phase matching-based association (SAC-TMA). Geng Sun / Jilin-NTU cluster.
- [[chen-2024-three-party-hierarchical-game-pls]] — Chen et al. (**IEEE TWC**, `10.1109/TWC.2023.3322776`; date of publication 16 Oct 2023, date of current version 10 May 2024). Three-party hierarchical game for PLS with dynamic trilateral coalitions; HCSF + DRL.
- [[sun-2025-emoppo-vlh-aerial-cb]] — Sun et al. 2025 (**IEEE TMC**, `10.1109/TMC.2025.3536093`). AAV-swarm collaborative beamforming to a terrestrial mobile user; evolutionary multi-objective PPO (EMOPPO-VLH). Geng Sun / Jilin cluster.
- [[li-2024-emodrl-ground-space-cb]] — Li et al. 2024 (**IEEE JSAC**, `10.1109/JSAC.2024.3459029`). Distributed collaborative beamforming for ground-space (terminal-to-LEO) uplink; EMODRL; saves 30% handover frequency. Geng Sun / Jilin cluster.

### New concept stubs (4)

- [[collaborative-beamforming]] — virtual-antenna-array beamforming (aerial UVAA / distributed DCB / secure CB), tying together the 3 CB sources.
- [[coalition-formation-game]] — cooperative/hedonic coalition games, grounded in the PLS three-party source.
- [[cellular-connected-uav]] — the "UAV as network user" paradigm from the Zeng tutorial, distinct from UAV-as-edge-server.
- [[uav-data-collection]] — UAV-as-data-sink mission pattern, paired with the MEC-DC joint source.

All other referenced concepts reused existing slugs (e.g. [[masac]], [[td3]], [[matching-theory-for-resource-allocation]], [[wireless-power-transfer]], [[binary-vs-partial-offloading]], [[multi-objective-reinforcement-learning]], [[evolutionary-reinforcement-learning]], [[physical-layer-security]], [[gauss-markov-mobility-model]]).

### New entities (2) + roster updates

- **Created:** [[boxiong-wang]] and [[hui-kang]] — both **College of Computer Science and Technology, Jilin University**; each recurs in 2 sources ([[wang-2025-sac-tma-mec-dc]] + the already-curated [[chen-2025-swipt-mec-sac]]) with identical email (`wangbx0320@163.com` / `kanghui@jlu.edu.cn`). Unambiguous, affiliation-consistent.
- **Roster updates (existing entities):** [[geng-sun]] (5→8 sources), [[jiahui-li]] (4→7), [[dusit-niyato]] (8→11), [[jiacheng-wang]] (3→5), [[jiawen-kang]] (4→6), [[zemin-sun]] (3→4), [[qingqing-wu]] (+[[li-2024-emodrl-ground-space-cb]], SJTU-email-matched).
- **Deferred (human confirmation):** a "Qingqing Wu" in [[zeng-2019-uav-comm-tutorial-5g]] is listed at **NUS** (`elewuqq@nus.edu.sg`), while the [[qingqing-wu]] entity is **SJTU** (`qingqingwu@sjtu.edu.cn`). Plausibly the same person earlier in his career, but the affiliation/email differ, so the tutorial was **not** added to his roster — noted on the entity page. No author-entity links were embedded in source pages (matching the established house convention).

### Audit (correctness-first)

- **DOI / venue / year** verified against each parse's `Digital Object Identifier` line (or, for Fujimoto, the ICML/PMLR proceedings line — that parse has no DOI, left as "not in parse"). Years follow the wiki's DOI/publication-year convention. The TWC paper's DOI embeds 2023 but its date-of-current-version is May 2024; year set to 2024 per the current-version convention, with the publication dates noted in the citation.
- **Algorithm-name inconsistency flagged, not hidden:** [[sun-2025-emoppo-vlh-aerial-cb]]'s parse names the method **EMOPPO-VLH** throughout (title/abstract/algorithm/complexity), but one intro sentence calls it "MOPPO-PLE". The page uses EMOPPO-VLH (dominant in-parse name) and notes the discrepancy rather than inventing a reconciliation.
- **Grounded headline numbers only:** the ground-space CB "saves 30% handover frequency" is stated verbatim in [[li-2024-emodrl-ground-space-cb]]'s abstract; CB received-power "∝ square of the number of AAVs" is from [[sun-2025-emoppo-vlh-aerial-cb]]; the Zeng tutorial's 3GPP link figures (60–100 kb/s CNPC, up to 50 Mbps payload, $10^{-3}$ PER, 50 ms) are from its Table 1. No figure-only numbers were stated as exact.
- **Wikilink integrity:** all wikilinks introduced this batch target existing slugs or pages created in this same batch; no NEW dangling links introduced. (Full wiki-wide Obsidian-faithful check run after writing — see verification below.)
- **Frontmatter:** `type` / `title` / `authors` / `year` / `venue` / `tags` / `related` / dates / H1 present on all 7 source pages; `type`/`title`/`tags`/dates/H1 on the 4 concepts + 2 entities.
- **Counts reconciled:** 89 sources / 180 concepts / 48 author entities (+[[pytorch]] = 49 entity pages). `index.md` and `overview.md` updated to agree.
- **LLM Wiki API:** not queried this batch (headless shell); not required for correctness.
- **Raw-folder scope:** only the 7 assigned folders were curated; the other 45 untracked `raw/sources/**` folders were intentionally left for their own batch runs.

## 2026-05-31 — Audit & coverage pass (no new raw papers)

Maintenance pass over the existing 82-source corpus. No new papers were curated. Focus: re-verify correctness end-to-end (DOIs/venues, ungrounded numbers, link integrity), broaden the analytical layer where the corpus already supports it, and reconcile a stale derived count in the meta-docs.

### Correctness audit

- **Misattributed DOI fixed (the pass's main correctness find).** [[huang-2025-cmop-dispersed-computing]] carried `url`/`venue` = `10.1109/TEVC.2025.3569722` / *IEEE Trans. Evolutionary Computation*. That DOI is **not** this paper's — it is the DOI of **reference [8]** in huang-2025's own reference list, namely the Wang/Guo/Liu/Wang **ACVE** paper (verbatim title + all four authors match; cross-checked against Bing-Chuan Wang's publication record by web search, verification-only). huang-2025's own parse has **no `Digital Object Identifier` line**, so its venue/DOI were reset to `not in parse` with a corrective note.
- **ACVE metadata now grounded within the corpus.** As a consequence, [[wang-acve-constraint-violation-cmop]] — whose own parse also lacks a DOI line and was previously `not in parse` for venue/year/DOI — is now grounded by huang-2025's reference [8]: *IEEE Transactions on Evolutionary Computation*, early access, `doi:10.1109/TEVC.2025.3569722`, 2025. Frontmatter + citation updated with a provenance note.
- **3 genuinely-missing DOIs added**, each grounded in its own parse's `Digital Object Identifier` line: [[hao-2025-priority-aware-task-driven-co]] (`10.1109/TWC.2025.3564356`, IEEE TWC), [[zhang-2025-mcma-task-migration]] (`10.1109/TMC.2025.3539945`, IEEE TMC), [[zhang-2025-ssac-mgi-heterogeneous-uav]] (`10.1109/TMC.2025.3632884`, IEEE TMC). Venues follow the wiki's DOI-prefix → journal convention (TWC/TMC), consistent with sibling pages.
- **ACBFT "96.2% throughput" restored as grounded (prior-pass correction).** The 2026-05-30 pass had softened [[wang-2025-acbft-uav-consensus]] and flagged the 96.2% figure as *not in parse*. That was wrong: the figure is stated verbatim in the paper's contributions list (parse L35 — *"ACBFT achieves an increase in throughput of up to 96.2%…"*). Restored the claim with the L35 quote + a metadata note explaining the correction.
- **Headline numbers re-verified.** The 4 findings added in the prior pass were re-checked against their parses and all hold: maritime 39.3% energy saving (L165), FedLEO 41% delay / 9.39% accuracy (L39), ASAP 92.66% latency cut (L161, hardware-validated), MASAC +15.41% sensing / −30.73% queue-delay vs MADDPG (L725/L709 — the MADDPG-vs-PSO ordering confirmed correct). Note: MinerU renders some percentages with intra-number spaces (`1 5 . 4 1 %`), which can fool naive grep — verified by reading the parse lines directly.
- **Remaining no-DOI source pages confirmed legitimately blank:** [[bi-2025-sg-mapg]], [[peng-2025-drudm-cfg]], [[liu-2026-jppo-en-convntm]], [[du-2024-distributed-foundation-models-6g]] — none has a `Digital Object Identifier` line in its parse; left `not in parse`.
- **Wikilink integrity:** Obsidian-faithful wiki-wide check (root `purpose.md` indexed; inline-code spans + table-escaped `\|` aliases stripped) = **ZERO dangling links** after the pass. Orphans = only `README.md` and `schema.md` (repo-root structural docs with no wikilinks — expected, not errors).
- **Frontmatter:** `type`/`title`/`tags`/dates/H1 + `related` validated on every touched/new page; no self-references, no duplicate `related` entries.
- **Graph stats (file-derived):** 346 nodes / 5071 resolved edges (up from 336 / 4932 at the start of the pass). The LLM Wiki API was **not** reachable for authoritative graph stats — `GET /health` returned `authConfigured:true, allowUnauthenticated:false` and the graph endpoint returned **401** in this headless shell (no `LLM_WIKI_API_TOKEN`), the documented headless case. Fell back to the local file/search tools throughout; correctness grounded in the parses and committed files.

### Meta-doc reconciliation

- **Stale reference count fixed.** `index.md` and `overview.md` both said the reference DB held **1567** unique refs; the scout-owned [[reference-database]] now reports **2981** (its `Generated: 2026-05-30` summary). Updated both meta-docs to 2981. The scout's `wiki/references/**` files were **not** modified.
- **Counts reconciled to exact verified numbers:** 82 sources / 176 concepts / **47 entities** (46 authors + [[pytorch]]) / **12 findings** / **10 synthesis** / 4 comparisons / 2 methodology / 4 queries / 1 thesis. `index.md` and `overview.md` agree; every page on disk is indexed and every index link has a backing page.
- **`log.md`** already consolidated in the prior pass (the 89 automated "external batch delete" events live under [Raw-source housekeeping](#raw-source-housekeeping)); this pass only prepended this entry. Verified mojibake-free at the byte level (em-dashes/curly quotes intact) — meta-docs were edited with the file tools, never PowerShell redirection.

### Coverage added (analytical layer)

- **Findings (+1 → 12):** [[acbft-throughput-increase]] — up to 96.2% consensus-throughput increase vs existing chaining protocols, grounded at [[wang-2025-acbft-uav-consensus]] parse L35 (the finding deferred in the prior pass, now mintable because the number is confirmed in-parse).
- **Synthesis (+1 → 10):** [[blockchain-on-edge-trust-layer]] — maps the 3 blockchain-on-edge sources ([[mao-2025-bcsa-frl]], [[qin-2025-bcuav-masac]], [[wang-2025-acbft-uav-consensus]]) by **which layer the chain defends** (consensus-protocol / aggregation / audit). Complements the existing pairwise [[bcsa-frl-vs-bc-uav-masac]] comparison by adding the consensus-layer source.

### Entity coverage (+8 → 47)

Computed author recurrence across all 82 source pages and verified affiliations against the parses (author-bio + correspondence lines). **Created 8 entity pages** where the identity is unambiguous and affiliation-consistent:

- [[shuang-liang]] — Northeast Normal Univ.; identical email `liangshuang@nenu.edu.cn` across all 3 sources ([[chen-2025-swipt-mec-sac]], [[sun-2024-mvtora-postdisaster-vfc]], [[wang-2025-lae-network-survey]]); [[geng-sun]] aerial-MEC/LAE cluster.
- [[weifeng-zhong]] & [[shengli-xie]] — Guangdong Univ. of Technology, School of Automation (`wfzhongs@gdut.edu.cn` / `shlxie@gdut.edu.cn`); CMOP-evolutionary lineage with [[xumin-huang]] / [[jiawen-kang]] / [[chaoda-peng]].
- [[qiqi-xie]] — South China Agricultural Univ., College of Mathematics & Informatics; both sources ([[wu-2026-terrain-aware-uav-mec]], [[xie-2026-uav-multisource-fusion]]); previously a lower-priority candidate, now confirmed.
- [[nei-kato]] (Tohoku Univ., identical email), [[jiadai-wang]], [[yijie-xun]], [[yangbo-liu]] (all Northwestern Polytechnical Univ., the integrated aero-space-ground-ocean lab) — the [[bomin-mao]] NTN cluster, stable across [[mao-2024-ntn-hierarchical-caching-cav]] + [[mao-2025-bcsa-frl]].

**Still deferred (not created):** "Nan Zhao" (genuine namesake — Hubei Univ. of Technology vs Dalian Univ. of Technology, different emails). Lower-priority cross-cutting seniors with topically-divergent 2-source pairs (Mohsen Guizani, Dong In Kim) and tight-cluster 2-source co-authors (Hongbin Chen / Fangqing Tan, Guangxu Zhu) left as candidates for a future pass — affiliation-plausible but not minted this pass to avoid over-linking.

### Raw-folder reconciliation

84 raw folders vs 82 source pages. The 2 unmatched folders are again confirmed **duplicate MinerU ingests** (space-named variants) of already-curated papers — `Optimizing Spectrum Sharing in UAV Swarms…` (= [[wang-2025-uav-swarm-stackelberg]]) and `UAV-Enabled Multi-Source Data Fusion…` (= [[xie-2026-uav-multisource-fusion]]); byte-identical titles/abstracts. No uncurated paper exists, so nothing was routed to `mec-wiki-curator`.

## 2026-05-30 — Audit, refinement & coverage-expansion pass

Full audit + refinement pass on the existing 82-source corpus (no new raw papers). Focus: tidy the meta-docs, broaden the analytical layer, resolve deferred author identities, and re-verify correctness end-to-end.

### Meta-doc cleanup

- **`log.md`** de-noised and reordered. The 89 automated "external batch delete" blocks (machine-generated raw-artifact prune events, ~386 files, **0 wiki pages** ever deleted) were consolidated into the single [Raw-source housekeeping](#raw-source-housekeeping) section at the foot of the file. Entries reordered strictly newest-first; date headers normalized to `## YYYY-MM-DD — <title>`. File shrank from 1184 lines to a readable curation/audit history.
- **`index.md`** de-duplicated. Removed the second copy of the "Joint trajectory / caching / migration" source section; gave each of the 4 cross-listed sources ([[zhu-2025-lycnn-drl-wpt-mec]], [[wu-2025-iopo-irs-uav-thz-mec]], [[chen-2024-ulse-game]], [[hao-2025-priority-aware-task-driven-co]]) a single primary home with a `>` cross-reference note where useful; de-duplicated the three twice-listed concepts ([[generative-ai-for-mec]], [[edge-user-allocation]], [[collaborative-dl-inference]]); folded the single-item "Generic offloading techniques" section into "Compute offloading & DRL"; added the previously-unindexed [[j-ppo-en-convntm]] concept. Verified all 82 source / 176 concept / 34 entity pages resolve and are indexed.
- **`overview.md`** reconciled to exact counts (82 / 176 / 34), refreshed the analytical-layer line, and noted the new derived pages.

### Coverage expansion (analytical layer)

- **Findings (+4 → 11):** [[maritime-three-tier-energy-saving]] (39.3% energy saving, [[zhang-2025-three-tier-maritime-offloading]] — grounded verbatim in the parse abstract); [[fedleo-delay-accuracy-tradeoff]] (up to 41% delay reduction / 9.39% accuracy gain, [[zhai-2023-fedleo-decentralized-fl]] — grounded in the parse abstract + per-dataset breakdown); [[asap-swarm-inference-speedup]] (up to 92.66% computing-latency reduction vs raw-data offloading, hardware-validated on 24 airborne computers + 5 UAVs, [[sun-2024-asap-uav-swarm]]); [[masac-beats-maddpg-sensing-queue]] (+15.41% sensing rate / −30.73% queue delay vs MADDPG, [[qin-2025-bcuav-masac]] — grounded at parse L709/L725).
- **Synthesis (+3 → 9):** [[sagin-satellite-offloading-landscape]] (8 SAGIN/satellite sources); [[isac-sensing-in-aerial-mec]] (7 ISAC/sensing sources); [[maritime-mec-architectures]] (7 maritime sources).
- **Comparisons (+1 → 4):** [[game-theoretic-offloading-formulations]] (potential vs Stackelberg vs bargaining vs matching, across the game-theoretic sources).
- **Queries (+2 → 4):** [[query-when-does-dro-beat-drl-for-csi-uncertainty]]; [[query-video-vs-cooperative-perception-offloading-shape]].
- **Methodology (+1 → 2):** [[ao-sdr-sca-convex-pipeline]] (the alternating-optimization + SDR + SCA convex pipeline recurring across the ISAC/secure-beamforming sources).

Every new page grounds its claims in specific parses; figure-derived or unlabeled magnitudes are flagged indicative. A planned ACBFT-throughput finding was **dropped**: the "96.2% throughput" figure is **not in the [[wang-2025-acbft-uav-consensus]] parse** (see Correctness audit below), so no finding was minted on an ungrounded number.

### Entity coverage (+5 → 39)

Re-examined the 5 deferred namesake-risk authors against parse affiliations (first ~40 lines of each source). **Created 5 entity pages** where the identity proved unambiguous and affiliation-consistent; **kept 1 deferred** as a genuine namesake.

- **Created:**
  - [[ying-chen]] — Beijing Information Sci. & Tech. Univ.; `chenying@bistu.edu.cn` identical across [[chen-2023-dotora-air-ground-online]] and [[chen-2024-ulse-game]] (shared co-authors [[yuan-wu]] + Jiwei Huang).
  - [[jie-xu]] — CUHK-Shenzhen (SSE); consistent ISAC affiliation across [[meng-2024-uav-isac-overview]] and [[yao-2025-secure-isac-dual-eavesdropping]].
  - [[fuhong-song]] — first author of [[song-2022-emorl-tcto-uav]] (SWJTU) and [[song-2024-mol-aoi-energy]] (Guizhou Univ. of Finance & Economics); a student→faculty move confirmed by the shared co-author Huanlai Xing (`hxx@home.swjtu.edu.cn` in both) and the shared evolutionary-MORL niche.
  - [[yong-wang]] — School of Automation, Central South Univ.; `ywang@csu.edu.cn` **identical** in both [[wang-2019-todetas-deployment-scheduling]] and [[wang-acve-constraint-violation-cmop]] (the shared email overrides the earlier "different topics" deferral).
  - [[wei-zhang]] — Shandong Computer Science Center (Nat'l Supercomputer Center in Jinan); identical lab + identical co-author roster ([[hao-hao]], Changqiao Xu, Shujie Yang, Gabriel-Miro Muntean) across [[hao-2024-clp-multiuav-priority-offloading]] and [[hao-2025-priority-aware-task-driven-co]].
- **Still deferred (genuine namesake — do NOT merge):** "Nan Zhao" — [[zhao-2022-matd3-multiuav-ec-offloading]] is **Hubei Univ. of Technology** (`nzhao@mail.hbut.edu.cn`, Member) while [[zhang-2025-gan-td3-isac-active-ris]] is **Dalian Univ. of Technology** (`zhaonan@dlut.edu.cn`, Senior Member). Different institutions and emails → two different people; no entity created.

### Correctness audit

- **Raw-folder reconciliation:** 84 raw folders vs 82 source pages. The 2 unmatched folders are confirmed **duplicate ingests** (space-named MinerU variants) of already-curated papers — `Optimizing Spectrum Sharing in UAV Swarms...` (= [[wang-2025-uav-swarm-stackelberg]], curated from the underscore-named folder) and `UAV-Enabled Multi-Source Data Fusion...` (= [[xie-2026-uav-multisource-fusion]]). Byte-identical titles/abstracts; no uncurated paper. No action beyond noting it here.
- **Ungrounded-number fixes (2 found):**
  1. [[wang-2025-acbft-uav-consensus]] asserted "increases throughput by up to **96.2%**" — that figure is **not in the parse** (only image references + a generic "higher throughput" statement at L37) and is not web-confirmable for this paper. Softened the source page to the parse-supported claim (chain propagation trades latency for higher throughput; Fig. 6 shows ACBFT leading other BFT protocols at `N=3f+1`) and explicitly flagged "96.2%" as not in parse.
  2. [[maddpg-vs-masac-in-mec]] and [[bcsa-frl-vs-bc-uav-masac]] quoted "+13.16% sensing / −29.47% queue delay" as the margin **vs MADDPG**. The parse (qin-2025-bcuav-masac L709/L725) shows those are the **PSO** comparison figures; the margins **vs MADDPG** are **+15.41% / −30.73%**. Corrected both pages.
- **Wikilink integrity:** Obsidian-faithful wiki-wide check (root `purpose.md` indexed, inline-code spans + table-escaped `\|` aliases handled) = **ZERO dangling links** after this pass (the new derived pages were forward-referenced from the log, then created).
- **DOI / venue spot-checks:** sampled source pages re-verified against parses; the only metadata issue found was the ACBFT throughput number above (a claim, not a venue/DOI error — DOI `10.1109/TVT.2025.3548281` and venue IEEE TVT are correct).
- **Frontmatter:** `type` / `title` / `tags` / dates / H1 validated via diagnostics on every page created or edited this pass.
- **LLM Wiki API:** not queried (headless shell); not required for correctness.

## 2026-05-29 — Follow-up cleanup pass (dangling links + author identities + references)

Scoped cleanup pass (no new sources curated). Three tasks:

### Task 1 — dangling wikilink resolution (now ZERO real dangling links)

- **`[[hp-mobility-models]]`** in [[liu-2026-jppo-en-convntm]] (System model table, IoT-mobility Reference cell) → replaced with **`[31]`**. Grounded in the parse (`raw/sources/Multi-UAV_Path_Planning_for_Mobile_Edge_Computing_With_High-Density_Mobile_Devices/full.md`, "Gauss-Markov (GM) mobility model … as [31]"), matching the bracketed-cite style of the other rows (`[5], [32]`, `[10]`, `[33]`). No `hp-mobility-models` page was invented.
- **`[[fairness-metrics-in-mec]]`** in [[peng-2025-drudm-cfg]] → **created** `wiki/concepts/fairness-metrics-in-mec.md` as a synthesis concept tying together the existing fairness vocabulary ([[jains-fairness-index]], [[theil-fairness-index]], [[spatial-equity-index]], [[service-experience-ratio]], [[energy-balancing-uav]]) and grounded in how the corpus uses them (liu-2026 Jain-style f_n in [[equilibrium-efficiency-metric]]; peng-2025 Theil regularizer; he-2023 fairness-among-UAVs; gao-2024 service-experience ratio). Dropped the "when that page exists" qualifier in the peng-2025 sentence.
- **`[[purpose]]`** in [[high-density-mobile-device-scenarios]] — **FALSE POSITIVE, left as-is.** Verified `purpose.md` exists at repo root and is indexed in `.llm-wiki/file-snapshot.json` (`purpose.md`, size 816). Obsidian resolves `[[purpose]]` by basename to the root file, so the link is valid. The earlier "dangling" report came from a `wiki/`-scoped integrity checker that does not index repo-root files.
- **Integrity re-check:** an Obsidian-faithful re-check (root indexed + inline-code spans stripped) reports **NO DANGLING LINKS**. The two real dangling links are fixed; the third was never real.

### Task 2 — deferred author identities confirmed (21 created, 5+ deferred)

Computed author recurrence across all 82 source pages and verified affiliations against each paper's parse (first ~40 lines). **Created 21 entity pages** for recurring authors whose identity is unambiguous and affiliation-consistent across their sources (schema mirrors [[geng-sun]]):

- Jilin-University / NTU aerial-MEC cluster: [[zemin-sun]], [[jiahui-li]] (Jilin Univ), [[jiacheng-wang]], [[dusit-niyato]] (NTU), [[qingqing-wu]] (Shanghai Jiao Tong Univ).
- NUAA aerial-computing cluster: [[ziye-jia]], [[chao-dong]], [[qihui-wu]] (NUAA), [[zhu-han]] (Univ of Houston / Kyung Hee).
- Dalian-Maritime-University maritime cluster: [[bin-lin]] (DMU), [[zhen-wang]] (DMU / Dalian Neusoft — same email `wangzhen_jsj@neusoft.edu.cn` across all 3 papers confirms one identity despite the common name), [[qiang-ye]] (Univ of Calgary).
- NWPU non-terrestrial-network cluster: [[bomin-mao]], [[hongzhi-guo]], [[jiajia-liu]] (Northwestern Polytechnical Univ, `@nwpu.edu.cn`).
- NCEPU aerial-edge cluster: [[peng-qin]], [[yang-fu]] (North China Electric Power Univ, `qinpeng@ncepu.edu.cn`); [[jingjing-wang]] (Beihang Univ, `drwangjj@buaa.edu.cn` — shared email confirms one identity).
- SCAU evolutionary UAV-MEC cluster: [[zexiong-wu]] (South China Agricultural Univ).
- Cross-cutting seniors: [[chunxiao-jiang]] (Tsinghua, `jchx@tsinghua.edu.cn`), [[tony-q-s-quek]] (SUTD, `tonyquek@sutd.edu.sg`).

Updated [[geng-sun]] to note its previously-deferred co-authors now have confirmed pages.

**Deferred — needs human confirmation** (not created at the time):

- **Yong Wang** (wang-2019-todetas, wang-acve) — common name; the ACVE paper is an evolutionary-computation work, wang-2019 is a different topic/affiliation; no shared affiliation in the parses.
- **Nan Zhao** (zhao-2022-matd3, zhang-2025-gan-td3-isac) — zhao-2022's Nan Zhao is at Hubei Univ of Technology; the zhang-2025 Nan Zhao affiliation is not confirmed identical → namesake risk.
- **Wei Zhang** (hao-2024, hao-2025) — extremely common name; affiliation not verified.
- **Ying Chen** (chen-2023-dotora, chen-2024-ulse-game) — common name; affiliation not verified this pass. *(Resolved 2026-05-30: shared `bistu.edu.cn` email → entity created.)*
- **Jie Xu** (meng-2024-uav-isac-overview, yao-2025-secure-isac) — common name; both point to CUHK-Shenzhen + ISAC. *(Resolved 2026-05-30: entity created.)*
- Lower-priority 2-source co-authors with consistent affiliation (candidates for a future pass, not ambiguous): Qiqi Xie (SCAU), Yijie Xun / Jiadai Wang / Yangbo Liu (NWPU), Nei Kato (Tohoku).

Cross-linking convention: entity→source links live in each entity page's `related` + roster (Obsidian auto-generates the backlinks); existing source pages do not embed author-entity links, so none were added, matching the established [[geng-sun]] pattern.

### Task 3 — references files committed

Staged and committed the prior reference-scout outputs: `wiki/references/recommendations.md`, `wiki/references/reference-database.json`, `wiki/references/reference-database.md`. Scanned for secrets/tokens — none present. Added a **References** section to `wiki/index.md` linking [[reference-database]] and [[recommendations]].

### Audit

- **Frontmatter:** validated `type`/`title`/`tags`/dates/H1 on all touched pages (1 concept + 21 entities + 2 sources + index + overview) via diagnostics — no issues.
- **Wikilink integrity:** Obsidian-faithful check = **NO DANGLING LINKS**. Pre-existing dangling links eliminated: `hp-mobility-models` (fixed) and `fairness-metrics-in-mec` (created); `purpose` confirmed as a valid root-file link.
- **Counts reconciled:** 82 sources, 176 concepts, 34 entity pages (33 authors + pytorch) — matched `overview.md` at the time.
- **LLM Wiki API:** not queried this pass (headless shell); graph stats unavailable — not required for correctness.

## 2026-05-29 — Curation pass (batch 4: 43 new sources + audit)

Curated all 43 newly-ingested raw papers (corpus 39 → 82 sources). Metadata extracted faithfully from each MinerU parse; DOIs/venues verified against the parse text. Year convention follows the existing wiki (DOI-embedded year).

- **New source pages (43):** [[he-2019-euagame-user-allocation]], [[mao-2017-mec-survey-communication]], [[wang-2025-acbft-uav-consensus]], [[wang-acve-constraint-violation-cmop]], [[sun-2023-bargain-match-vec]], [[faisal-2025-cgan-ris-isac-channel]], [[kang-2023-mappo-hierarchical-aerial]], [[du-2024-distributed-foundation-models-6g]], [[wang-2025-double-edge-samin]], [[chen-2023-dotora-air-ground-online]], [[zhang-2025-three-tier-maritime-offloading]], [[song-2022-emorl-tcto-uav]], [[he-2023-fairness-3d-multiuav-maddpg]], [[zhai-2023-fedleo-decentralized-fl]], [[zhang-2025-gan-td3-isac-active-ris]], [[khoramnejad-2025-gai-wireless-optimization-survey]], [[jia-2022-hierarchical-aerial-matching]], [[wang-2024-hybrid-oma-noma-sagin]], [[tang-2024-iscc-uav-feel]], [[you-2025-uncertain-maritime-hasac]], [[zhang-2019-uav-iot-comp-comm]], [[zhao-2024-caching-service-placement-uav]], [[wang-2019-todetas-deployment-scheduling]], [[chen-2025-swipt-mec-sac]], [[sun-2024-mvtora-postdisaster-vfc]], [[yu-2020-uav-ec-collaborative-offloading]], [[qin-2025-matd3-noma-queue-sagin]], [[du-2023-maddpg-service-placement-agin]], [[albakhrani-2025-moalf-uav-mec]], [[zhang-2024-dlrl-maritime-usv]], [[zhao-2022-matd3-multiuav-ec-offloading]], [[zhang-2024-gdmtd3-aerial-secure-cb]], [[guo-2023-mccco-multiuav-5g-offloading]], [[mao-2024-ntn-hierarchical-caching-cav]], [[yang-2022-stochastic-uav-mec-lyapunov]], [[fu-2025-otae-inference-lae-batching]], [[liu-2022-miso-uav-mec-trajectory]], [[chang-2022-marl-multiuav-trajectory]], [[li-2025-twohop-airground-drl-offloading]], [[wang-2024-twotier-satellite-marine]], [[zhang-2024-uav-task-offloading-ddpg]], [[meng-2024-uav-isac-overview]], [[yao-2025-secure-isac-dual-eavesdropping]].
- **New concept stubs (17):** [[edge-user-allocation]], [[byzantine-fault-tolerant-consensus]], [[particle-swarm-optimization]], [[constraint-violation-evaluation]], [[bargaining-game]], [[conditional-gan]], [[generative-adversarial-network]], [[mappo]], [[decentralized-federated-learning]], [[integrated-sensing-computation-communication]], [[heterogeneous-agent-rl]], [[differential-evolution]], [[vehicle-fog-computing]], [[non-terrestrial-network]], [[ant-colony-optimization]], [[over-the-air-computation]], [[distributed-foundation-models]]. All other referenced concepts reused existing slugs.
- **New entity (1):** [[geng-sun]] — Jilin University, confirmed consistent across 5 sources. Other recurring batch-4 authors (Zhen Wang / Bin Lin maritime cluster, Ziye Jia / Chao Dong / Zhu Han aerial cluster, Peng Qin / Yang Fu) deferred for human identity confirmation rather than minting/merging entities.
- **Navigation:** refreshed `wiki/index.md` (new groupings: Foundational surveys & overviews, Classical/convex optimization UAV-MEC, Game-theoretic offloading & allocation, Multi-UAV cooperative computing & deployment, Pure optimization methods, ISAC/sensing/PLS; plus GAI / maritime / hierarchical additions and the 17 new concepts) and `wiki/overview.md` (counts 39 → 82, expanded track table, corrected hardware-validated count).

### Audit (correctness-first)

- **DOI / venue / year:** verified against each parse's `Digital Object Identifier` line; year set to the DOI-embedded year per existing wiki convention.
- **`not in parse` handling:** [[wang-acve-constraint-violation-cmop]] — venue, year, and DOI genuinely absent from the parse and unconfirmable by web search (author homepage lists no matching publication); left blank / `not in parse` rather than guessed. [[du-2024-distributed-foundation-models-6g]] — DOI absent from parse; venue "IEEE Wireless Communications" web-confirmed; DOI left empty.
- **Claims:** headline numbers reproduced only where explicit in the parse (e.g. ACBFT "up to 96.2% throughput increase", FedLEO "up to 41% delay / 9.39% accuracy", three-tier maritime "39.3% energy saving"). Figure/abstract-derived numbers (e.g. MOALF percentages) flagged as indicative.
- **Wikilink integrity:** wiki-wide check shows **no NEW dangling links**. Pre-existing dangling links remained and were reported: `[[fairness-metrics-in-mec]]`, `[[hp-mobility-models]]`, `[[purpose]]` (all resolved in the 2026-05-29 follow-up pass).
- **Frontmatter:** `type` / `title` / `tags` / dates / H1 validated on touched pages via diagnostics (no issues).
- **LLM Wiki API:** not queried this pass (headless shell); graph stats unavailable — not required for correctness.

## 2026-05-29 — Audit pass (batch-3 verification)

Correctness-first audit of the 13 batch-3 source pages and refreshed navigation:

- **DOIs verified against parses.** All 13 new source DOIs cross-checked against `Digital Object Identifier` lines in their `full.md`. Two needed manual confirmation because a regex first-match picked up a precursor/reference DOI: [[li-2025-stochastic-game-uav-swarm]] (parse confirms `10.1109/TGCN.2024.3424449`; the WCNC 2024 `10570678` is a conference precursor) and [[shao-2024-drl-antijamming-mec]] (parse confirms `10.1109/TMC.2024.3432491`; the GLOBECOM 2023 hit was a reference). Both page DOIs are correct.
- **Frontmatter valid** on all 39 source pages (`type/title/authors/year/venue/tags/related/created/updated` + H1 present).
- **Wikilink integrity:** no NEW dangling links introduced by this batch. The only unresolved targets remained the three pre-existing ones (`fairness-metrics-in-mec`, `hp-mobility-models`, `purpose`).
- **Counts reconciled:** 39 sources, 158 concepts, 12 entities — matched `overview.md`.
- Created a reusable workspace agent `.kiro/agents/mec-wiki-curator.md` to standardize this curate-then-audit workflow for future raw-paper drops.

## 2026-05-29 — Curation pass (batch 3: 13 new sources)

User dropped 13 new folders into `raw/sources/` and asked to construct the wiki from them. Curated all 13 in one pass (4 had pre-existing extraction drafts in `.curation-out/`; the remaining 9 were extracted by sub-agents against `.curation-context.md`). Corpus grows **26 → 39 curated sources**.

**SAGIN / satellite offloading (4 new):**

- [[gao-2024-sagin-perception-offloading]] — Gao et al. 2024 (JSAC). Perception-aided SAGIN offloading; mmWave radar + YOLOv7 feed a Lyapunov + DDPG + DQN + SGHS pipeline. **First perception-driven offloading entry.**
- [[chen-2024-thoas-traffic-aware-sagin]] — Chen et al. 2024 (JSAC). THOAS: traffic-aware slicing-enabled SAGIN; probsparse-attention prediction + lightweight distilled PPO.
- [[chen-2024-ulse-game]] — Chen et al. 2024 (TMC). Multi-user UAV-LEO offloading as a potential game (LUTO-Game / JULTO).
- [[han-2024-sagin-fl-handover]] — Han et al. 2024 (JSAC). Federated learning across SAGIN with adaptive inter-layer data offloading + satellite seamless handover. **First plain-FL entry.**

**UAV-swarm collaborative computing (2 new):**

- [[sun-2024-asap-uav-swarm]] — Sun et al. 2024 (TMC). ASAP: in-swarm collaborative DL inference (model + data partition, pipeline-parallel). **Hardware-validated** (24 Jetson computers + 5 real UAVs).
- [[li-2025-stochastic-game-uav-swarm]] — Li et al. 2025 (TGCN). Energy-efficient UAV-swarm MEC as five stochastic games with dynamic clustering; RLDC multi-agent Q-learning.

**IRS / THz / anti-jamming (2 new):**

- [[wu-2025-iopo-irs-uav-thz-mec]] — Wu et al. 2025 (TMC). IRS-assisted multi-UAV THz MEC; two-stage IOPO (order-preserving offloading + WOA phases). **First IRS/THz entry.**
- [[shao-2024-drl-antijamming-mec]] — Shao et al. 2024 (TMC). Anti-jamming UAV-MEC; PER-MATD3. **Hardware-validated** (Raspberry Pi/USRP). **First anti-jamming entry.**

**Trajectory / caching / fairness / priority / AoI / AIGC (5 new):**

- [[hao-2024-clp-multiuav-priority-offloading]] — Hao et al. 2024 (TMC). Multi-UAV priority offloading; CLP (TD3 + hybrid-action latent space). Companion to [[hao-2025-priority-aware-task-driven-co]].
- [[zhao-2025-traj-offload-cache-migration]] — Zhao et al. 2025 (TMC). Joint trajectory + offloading + migration + computational-task caching; Lyapunov + BCD + QCQP-SDR.
- [[gao-2024-service-experience-cache-uav]] — Gao & Zhai 2024 (TMC). Fairness-aware cache-enabled UAV-MEC; service-experience ratio (Jain / delay); Dinkelbach + 4-stage AO.
- [[song-2024-mol-aoi-energy]] — Song et al. 2024 (TMC). AoI-vs-energy aerial-ground MEC via multi-objective RL (MOL-AET). **First AoI / MORL entry.**
- [[ye-2025-aigc-diffusion-contract]] — Ye et al. 2025 (TVT). Edge AIGC via contract theory + prompt engineering; generative diffusion model as the contract-item optimizer.

### Concept pages added (55)

- **DRL / learning:** [[td3]], [[multi-agent-td3]], [[deep-q-network]], [[multi-agent-q-learning]], [[hybrid-action-representation]], [[knowledge-distillation-for-drl]], [[dynamic-confidence-interval-clipping]], [[multi-objective-reinforcement-learning]], [[multi-objective-mdp-vectorial-reward]], [[evolutionary-reinforcement-learning]], [[generative-diffusion-model]], [[diffusion-model-as-optimizer]].
- **Game theory / optimization:** [[stochastic-game]], [[potential-game]], [[nash-equilibrium]], [[contract-theory]], [[mixed-integer-nonlinear-programming]], [[whale-optimization-algorithm]], [[self-adaptive-global-best-harmony-search]], [[order-preserving-quantization]], [[qcqp-sdr-probabilistic-mapping]].
- **Communication / sensing / channel:** [[anti-jamming-mec]], [[spectrum-sensing-channel-selection]], [[mmwave-radar-sensing]], [[yolov7-object-detection]], [[perception-aided-offloading]], [[intelligent-reflecting-surface]], [[terahertz-communication]], [[network-slicing]], [[traffic-aware-offloading]], [[probsparse-self-attention-prediction]].
- **Distributed inference (ASAP):** [[collaborative-dl-inference]], [[dnn-model-partition]], [[data-partition-parallel-inference]], [[pipeline-parallel-inference]], [[dl-inference-latency-prediction]], [[adaptive-intermediate-data-compression]], [[elastic-task-scheduling]].
- **Federation / satellite:** [[federated-learning]], [[seamless-handover]], [[adaptive-inter-layer-data-offloading]], [[privacy-sensitive-data-partitioning]], [[walker-star-constellation]], [[leo-satellite-coverage-time]].
- **Scheduling / caching / swarm:** [[computational-task-caching]], [[priority-based-delay-utility]], [[intra-swarm-task-delegation]], [[dynamic-uav-clustering]].
- **Metrics / freshness / fairness / AIGC:** [[age-of-information]], [[aoi-energy-tradeoff]], [[energy-latency-tradeoff]], [[jains-fairness-index]], [[service-experience-ratio]], [[prompt-engineering]], [[aigc-service-provider]].

### Entity pages added (1)

- [[hao-hao]] — first author of [[hao-2024-clp-multiuav-priority-offloading]] and [[hao-2025-priority-aware-task-driven-co]] (identical co-author roster), anchoring the task-priority + hybrid-action thread.

### What this changed about the corpus

- **Corpus size:** 26 → 39 curated sources.
- **New tracks:** SAGIN/satellite offloading (4), UAV-swarm collaborative computing (2), game-theoretic offloading (now spans potential/stochastic/Stackelberg games), generative-AI MEC (2), anti-jamming security-DRL (1).
- **First hardware-validated sources** enter the corpus: [[sun-2024-asap-uav-swarm]] and [[shao-2024-drl-antijamming-mec]].
- **New formulation families:** potential/stochastic games + Nash-equilibrium analysis, multi-objective RL (vectorial reward), contract theory, IRS/THz channels, in-swarm collaborative DL inference, federated learning over SAGIN.
- **Diffusion-as-optimizer** now has two sources ([[ye-2025-aigc-diffusion-contract]], [[peng-2025-drudm-cfg]]).

### Issues flagged for follow-up

- **Synthesis refresh overdue.** The synthesis/findings/thesis pages still reflected the 26-source view at the time.
- **Figure-derived numbers:** several magnitudes in [[li-2025-stochastic-game-uav-swarm]] and [[han-2024-sagin-fl-handover]] were read from MinerU-parsed figure tables with unlabeled axes — treat as indicative trends; verify against the PDFs before citing exactly.

## 2026-05-29 — Deep synthesis audit (26-source era)

Read each new synthesis page paragraph by paragraph and cross-checked every factual claim against the underlying papers. Found seven concrete corrections plus several softening edits.

### `cmop-evolutionary-uav-mec-lineage`

- **Overclaim: "B-spline trajectory ... in every paper".** Verified against papers: only [[peng-2022-cmop-uav-path-planning]] and [[wu-2026-terrain-aware-uav-mec]] (the trajectory-design entries) actually use B-splines. [[huang-2023-mu-aec-task-energy]] (DAG scheduling), [[peng-2024-energy-time-uav-its]] (UAV-ITS), [[huang-2025-cmop-dispersed-computing]] (dispersed computing), [[xie-2026-uav-multisource-fusion]] (cooperative perception) don't have a UAV path to plan. Demoted B-spline to "trajectory-subset's shared tool, not a lineage-wide constant".
- **Overclaim: "CMOEA/D-CDP backbone in every paper".** Verified: peng-2022, huang-2023, peng-2024, huang-2025 use CMOEA/D-CDP; xie-2026 extends NSGA-II for the dynamic CMOO setting; wu-2026 uses a multi-tasking dual-population scheme with the constrained-domination principle but not strictly CMOEA/D-CDP. Softened to "CMOEA family backbone — even where the specific framework shifts" with the framework breakdown spelled out.
- **Overclaim: "Compare against the previous lineage entry plus 1-2 external baselines (typically ToP, PPS, NSGA-II, NSGA-III)".** Verified the actual baselines: peng-2022 used ToP, PPS; huang-2023 added NSGA-II; peng-2024 only PPS; huang-2025 used CCMO/BiCo/CMaO/CTAEA (none of those four); xie-2026 used NSGA-II/C-NSGA/C-MOEA; wu-2026 used CMOEMT/URCMO/ICMA/DPPPS. The lineage entries do *not* run head-to-head against each other on a common benchmark. Rewrote the template step to reflect "compare against external CMOEA baselines of the relevant generation" with explicit naming.
- **Overclaim: "All entries run 10^4-10^5 function evaluations".** Only [[peng-2022-cmop-uav-path-planning]] explicitly states 3x10^4 FE. The others report only generations x population. Softened.
- **Overclaim: "all reporting Pareto-front improvements over both DRL-style and prior-CMOEA baselines".** None of the lineage papers compares against a DRL controller. Removed the "DRL-style" half. Confidence on the working thesis reduced from "high" to "medium-high" with the caveat made explicit.
- **Inheritance graph: speculative.** Verified citations: peng-2024 cites peng-2022; huang-2025 cites peng-2022 but does **not** cite peng-2024 directly. Rewrote the graph caption to mark it as interpretive (technique reuse via shared authors), not direct citation.

### `hierarchical-aerial-mec-design-space`

- **Off-by-one: "Two of five (`bao-2025`, `nabi-2025`, `peng-2025`) use DRL".** That's three sources, not two. Fixed.
- **Wrong: "[[jia-2025-dro-uav-hap-mec]] optimizes trajectory jointly with offloading via WKD pre-stage".** WKD is a one-shot UAV deployment scheme; UAVs are quasi-stationary after deployment. So jia-2025 has placement, not trajectory. Reclassified as "in between" — placement, not full trajectory — with the distinction spelled out.
- **Stale "four-source roster" / "the four sources".** The roster has five sources. Updated to "five-source roster" everywhere.
- **Misleading objective table: jia-2025 latency = (chance-constraint), energy = checked.** The chance constraint *is* on latency, while energy is the actual sole objective. Clarified the cell to make this unambiguous.

### `drl-vs-evolutionary-vs-classical-solvers`

- **Wrong: "[[liu-2025-haps-uav-maritime-iot]]'s EMOMVO-CGD ... used to handle binary subproblems after a convex relaxation".** Verified: EMOMVO-CGD is the *whole MOP* solver for liu-2025 — same role as a CMOEA. Only [[jia-2025-dro-uav-hap-mec]]'s BWOA fits the "binary subproblem after relaxation" pattern. Split the two cases explicitly.
- **Fabricated number: "[[jia-2025-dro-uav-hap-mec]] reports ~10–20% energy overhead vs nominal solutions".** That number is not in the paper; the paper validates robustness empirically without pinning down a percentage. Removed and softened to "the paper's simulations validate the robustness benefit but don't pin down a precise overhead percentage".
- **Family-roster table cleanup.** [[jia-2025-dro-uav-hap-mec]]'s primary classification is classical (DRO + CVaR + primal decomposition + CVX). BWOA is a sub-block solver inside it, not a separate evolutionary entry. Restructured the table: 12 DRL + 7 evolutionary/metaheuristic + 5 classical (with BWOA called out as a sub-block in the classical row).

### Verified clean (no changes needed)

- **`drl-backbones-across-uav-mec-sources`.** The DDPG/TD3/DQN underperformance attribution to hybrid-action limitations matches the paper's own wording verbatim. The DOA reference (Dingo Optimization Algorithm — verified) is correct.
- **`maddpg-vs-masac-in-mec`.** The +13.16% sensing rate / −29.47% queue delay numbers are from the qin-2025 abstract — verified against the parsed paper.
- **`design-recipe-multi-uav-mec`.** Ten checklist items, all anchored to specific liu-2026 results — re-read and consistent.

### Schema and link integrity after edits

- 26 source pages, 103 concept pages, 11 entity pages, 6 synthesis pages — all schema-clean.
- 3 dangling wikilinks remained (hp-mobility-models, fairness-metrics-in-mec, purpose) — all pre-existing, none introduced or worsened by the audit.

## 2026-05-29 — Audit pass (three corrections, 26-source era)

Reviewed all 14 new source pages against the parsed papers. Three issues found, all fixed:

### bao-2025-ddpg-video-offloading

- **Venue was wrong.** I had marked it as "Journal of Supercomputing / Cluster Computing (Springer; preprint, accepted Sep 2025)" because the MinerU parse didn't capture publication metadata. The actual venue is **Complex & Intelligent Systems** (Springer), DOI `10.1007/s40747-025-02106-1`. Confirmed via web search of the title; updated frontmatter and citation.
- **Findings claim was wrong.** I wrote "DDPG converges faster than PPO baselines on this problem". The actual paper compares DDPG against **AC** and **DQN** baselines (no PPO baseline in the paper). DQN explicitly fails to converge in continuous action space; AC trains but is unstable. Updated the Findings section and added a note that the wiki's broader [[ddpg-vs-jppo]] comparison should be read as cross-source rather than internal to this paper.

### huang-2025-cmop-dispersed-computing

- **Venue was wrong.** I had marked it as "IEEE / preprint (Huang/Peng group, 2025)". The actual venue is **IEEE Transactions on Evolutionary Computation**, DOI `10.1109/TEVC.2025.3569722`. Confirmed by grepping the parsed full.md for the DOI. Updated frontmatter and citation.

### Other checks that passed

- Cross-checked DOIs for the 12 other new source pages against their parsed papers — all match.
- Schema lint: 26 source pages, 103 concept pages, 11 entity pages, 6 synthesis pages all have valid frontmatter (`type`, `title`, `tags`, h1 heading, etc.).
- Method/findings claims spot-checked for: JCORA (wang-2026, two-stage matching+convex+PGD), EMOMVO-CGD/JCCPAPO (liu-2025), ESAC=SAC+PER (nabi-2025), three-tier+binary-offloading+P-DQN (ma-2025), DEM+B-spline+multi-tasking (wu-2026), repair-CHT (peng-2024), dual-population+repair (huang-2025), I>=J standby UAVs (peng-2024), ACCP/ARDCP/MBCM/SRCON (jiang-2025). All consistent with the papers.
- Three dangling wikilinks remained (`hp-mobility-models`, `fairness-metrics-in-mec`, `purpose`) — all pre-existing, not introduced by either the curation or audit pass.
- Graph: 161 nodes, 1073 edges (LLM Wiki API).

## 2026-05-29 — Synthesis + entity follow-up (26-source era)

Closed the follow-up items flagged at the end of the 14-source curation pass.

### Author entity pages (4 added)

The CMOP-evolutionary lineage has four recurring authors. Promoted them to entity pages:

- [[chaoda-peng]] — first author of lineage seed; on 6 of 6 lineage sources.
- [[xumin-huang]] — first/lead author on 2 lineage sources, co-author on 4 more.
- [[yuan-wu]] — senior co-author across all 6 lineage sources.
- [[jiawen-kang]] — co-author on 4 lineage sources.

Each page lists their roster and notes which methodological knobs they're associated with.

### Synthesis pages (3 added, 1 refreshed)

**Added:**

- [[cmop-evolutionary-uav-mec-lineage]] — maps the Peng/Huang group's 6-paper thread (2022-2026), the shared template, the per-paper methodological knob, the inheritance graph, and when to pick CMOEA vs DRL.
- [[hierarchical-aerial-mec-design-space]] — cross-compares the 5 UAV+HAP hierarchical-MEC sources on backbone, decomposition, channel model, objective stack, HAP role. Identifies [[two-stage-decomposition]] as the most portable scaffold and HAP-link / security as gaps.
- [[drl-vs-evolutionary-vs-classical-solvers]] — corpus-wide solver-family synthesis. Operating guide for picking each, plus the gap analysis: no head-to-head between families, robustness only in classical so far.

**Refreshed:**

- [[drl-backbones-across-uav-mec-sources]] — extended the at-a-glance table to cover the 4 new DRL sources (P-DQN, DDPG video, ESAC, HAP-PPO) and added a "What the 2026-05-29 batch changes" section: a clean three-way hybrid-action taxonomy; DDPG's niche (single-agent + scalar + pure-continuous); PER + entropy-regularized policy as the default off-policy baseline; SAGIN-tier scheduling as its own optimization shape.

### Index updates

- Synthesis section then listed 6 pages.
- Entities section split into Authors / Tools subsections.

### Still not done (intentional, scope-bound at the time)

- **Findings / methodology / thesis pages** still anchored to the original 12-source corpus. Claims like [[hybrid-action-memory-augmented-drl-wins-uav-mec]] are framed as *theses about [[liu-2026-jppo-en-convntm]]'s framework*, not corpus-wide.
- **No `evolutionary-design-recipe`** companion to [[design-recipe-multi-uav-mec]] yet.
- **No fresh queries** raised in this pass; open questions flagged inside the new synthesis pages await promotion to formal `query-*` pages.

## 2026-05-29 — Curation pass (14 new sources)

User dropped 16 new folders into `raw/sources/`; two were duplicate ingests of papers already curated ([[wang-2025-uav-swarm-stackelberg]] and [[xie-2026-uav-multisource-fusion]] each appeared twice with different MinerU UUIDs). Curated the remaining 14 in one pass:

**Hierarchical aerial MEC (UAV + HAP) — 3 new sources:**

- [[nabi-2025-jour-hierarchical-aerial]] — Nabi & Moh 2025 (TMC). Gale-Shapley matching + ESAC for joint offloading, association, resource allocation.
- [[bao-2025-ddpg-video-offloading]] — Bao et al. 2025. UAV+HAP video-analytics offloading with adaptive transcoding; DDPG over a QoE reward. **First video-analytics workload in the wiki.**
- [[jia-2025-dro-uav-hap-mec]] — Jia et al. 2025 (TMC). Distributionally robust UAV-HAP MEC under uncertain CSI; CVaR + primal decomposition + BWOA. **First DRO entry in the wiki.**

**Maritime MEC track (new) — 2 new sources:**

- [[wang-2026-aerial-marine-msar]] — Wang et al. 2026 (TCCN). UAV+HAPS+MASS three-tier MEC for maritime search & rescue. Classical solver (matching + convex + PGD).
- [[liu-2025-haps-uav-maritime-iot]] — Liu et al. 2025 (TMC). HAP-UAV-vessel comm: HAP-as-backhaul, UAV multicast, vessel unicast. Multi-verse optimizer + classical step-wise alternative.

**CMOP / evolutionary UAV-MEC lineage (Peng/Huang group) — 4 new sources:**

- [[peng-2022-cmop-uav-path-planning]] — **Lineage seed** (LWC 2022). CMOP for UAV path planning + offloading; infeasibility-utilization CMOEA.
- [[peng-2024-energy-time-uav-its]] — Peng et al. 2024 (TITS). UAV-ITS energy + completion-time-difference.
- [[huang-2023-mu-aec-task-energy]] — Huang et al. 2023 (IoTJ). Multi-UAV interdependent (DAG) tasks; makespan + energy balancing.
- [[huang-2025-cmop-dispersed-computing]] — Huang et al. 2025. Dispersed computing with task-redundancy reliability; dual-population CMOEA.
- [[wu-2026-terrain-aware-uav-mec]] — Wu et al. 2026 (TVT). Urban UAV-MEC with terrain-aware DEM channel; multi-tasking CMOEA.

(The lineage then had 6 entries including [[xie-2026-uav-multisource-fusion]].)

**HAP / SAGIN foundations — 1 new source:**

- [[hsu-2025-drl-hues-hap-noma]] — Hsu et al. 2025 (TCCN). HAP transmission + RF energy harvesting in NOMA SAGINs; PPO-based DRL-HUES.

**ISAC track — 2 new sources:**

- [[benaya-2025-aerial-isac-haps]] — Benaya et al. 2025 (TGCN). HAPS-mounted FD ISAC + friendly-jamming UAV + ground MEC; AO + SDR + SCA.
- [[jiang-2025-isac-lae-overview]] — Jiang et al. 2025 (ComMag). ISAC-for-LAE survey: IAGN architecture, MBCM channel model, stochastic-geometry analysis.

**Vehicular MEC — 1 new source:**

- [[ma-2025-pdqn-vehicular-mec]] — Ma et al. 2025 (TVT). P-DQN for hybrid-action three-tier vehicular MEC.

### Concept pages added (44)

- **Communication / sensing / security:** [[integrated-sensing-and-communication]], [[physical-layer-security]], [[friendly-jamming-uav]], [[space-air-ground-integrated-network]], [[rf-energy-harvesting]], [[unicast-multicast-cooperation]], [[wireless-backhaul]].
- **DRL:** [[ddpg]], [[parameterized-dqn]], [[prioritized-experience-replay]].
- **Optimization (classical / metaheuristic):** [[alternating-optimization-sdr-sca]], [[chance-constraint]], [[conditional-value-at-risk]], [[distributionally-robust-optimization]], [[binary-whale-optimization]], [[multi-verse-optimizer]], [[weighted-kmeans-uav-deployment]], [[two-stage-decomposition]], [[gale-shapley-matching]].
- **Evolutionary methods:** [[constrained-multi-objective-evolutionary-algorithm]], [[cmoea-d-cdp]], [[infeasible-individual-utilization]], [[dual-population-evolutionary-algorithm]], [[multi-tasking-evolutionary-algorithm]], [[local-search-evolutionary]], [[b-spline-trajectory]].
- **Channel modeling:** [[blockage-aware-channel-model]], [[terrain-aware-channel-model]], [[stochastic-geometry-network-analysis]], [[csi-estimation-error]].
- **Workload classes / scheduling:** [[video-analytics-offloading]], [[video-transcoding-tradeoff]], [[qoe-modeling-mec]], [[dispersed-computing]], [[task-redundancy-for-reliability]], [[parallel-vs-serial-processing]], [[interdependent-tasks-dag]], [[makespan-minimization]], [[completion-time-difference]], [[multi-source-data-fusion]].
- **Architecture / metrics:** [[three-tier-cloud-edge-end]], [[maritime-mec]], [[uav-enabled-its]], [[service-caching-mec]], [[load-balancing-uav-mec]], [[energy-balancing-uav]].

## 2026-05-29 — Synthesis pass (continued)

- Added [[maddpg-vs-masac-in-mec]] — synthesis on the recurring "MASAC beats MADDPG" pattern in the cooperative-MEC corpus. Working thesis at medium confidence based on direct evidence from [[qin-2025-bcuav-masac]] and [[zhang-2025-ssac-mgi-heterogeneous-uav]], indirect support from [[peng-2025-drudm-cfg]] and [[liu-2026-jppo-en-convntm]]. Documents the mechanism, when MADDPG is still preferable, and what would promote the thesis to high confidence.
- Updated `wiki/index.md` synthesis section.

## 2026-05-29 — Cross-source synthesis pass

- Added [[drl-backbones-across-uav-mec-sources]] — cross-corpus synthesis covering 9 of 12 sources, mapping action-space shape → backbone choice, single vs multi-agent, memory/prediction patterns, and DRL-vs-classical composition. Distills 6 practical recommendations.
- Added [[bcsa-frl-vs-bc-uav-masac]] — head-to-head comparison of the two blockchain-integrated MEC sources.
- Updated `wiki/index.md` so both pages are reachable from the type-grouped directory.

## 2026-05-28 — Initial corpus build (papers 1-12)

The wiki's first curation arc: 12 raw papers ingested and curated, with the analytical scaffolding (concepts, findings, methodology, thesis, queries, comparisons, synthesis, entities) built around the seed paper.

**Paper 1/12 — project creation + seed graph.**

- Project created. Repo initialized as a GitHub repo (private) under `EnosElinsa/mec-research-wiki`.
- Ingested first source: [[liu-2026-jppo-en-convntm]] — Liu et al., *Multi-UAV Path Planning for MEC with High-Density Mobile Devices*.
- Constructed the initial wiki graph: 16 concept pages (MEC, UAV decisions, Gauss-Markov mobility, PPO/GAE/POMDP, NTM/ConvLSTM/STN, the three evaluation metrics); 6 finding pages; 1 methodology page; 1 thesis page; 2 query pages; 2 comparison pages + 1 synthesis page (design recipe); 7 entity pages for authors plus PyTorch.
- Baseline `purpose.md` and `schema.md` left untouched — schema-compliant.

**Paper 2/12 — [[mao-2025-bcsa-frl]]** — Mao et al. 2025, *Blockchain-Enabled Cold Start Aggregation Scheme for FRL-Based Task Offloading in Zero Trust LEO Satellite Networks* (IEEE JSAC). Added concept pages [[leo-satellite-edge-computing]], [[zero-trust-architecture]], [[federated-reinforcement-learning]], [[blockchain-for-fl-aggregation]], [[ccvm-correction-voting]], [[csra-cold-start-reputation-aggregation]], [[fl-poisoning-attacks]], [[ddqn]]; finding [[bcsa-frl-tolerates-up-to-half-malicious-satellites]].

**Paper 3/12 — [[qin-2025-bcuav-masac]]** — Qin et al. 2025, *Cooperative UAV Trajectory Design and Resource Allocation in Blockchain-Enabled Secure Aerial Edge Computing Network* (IEEE TWC). Added [[lyapunov-optimization]], [[masac]], [[noma]], [[air-ground-integrated-network]]. Cross-linked with [[mao-2025-bcsa-frl]] (blockchain-on-edge) and [[liu-2026-jppo-en-convntm]] (multi-UAV-DRL).

**Paper 4/12 — [[peng-2025-drudm-cfg]]** — Peng et al. 2025, *DRUDM-CFG: A Fairness-Aware Multi-Agent DRL for AMEC-Assisted TO in Post-Disaster Scenarios*. Added [[high-altitude-platform-station]], [[post-disaster-mec]], [[theil-fairness-index]], [[hierarchical-aerial-mec]], [[adaptive-entropy-priority-replay]], [[ma-pomdp]].

**Paper 5/12 — [[zhu-2025-lycnn-drl-wpt-mec]]** — Zhu et al. 2025, *Enhancing Energy Efficiency in WPT-MEC Through Lyapunov-Guided DRL* (IEEE TWC). Added [[wireless-power-transfer]], [[binary-vs-partial-offloading]], [[fractional-programming-dinkelbach]].

**Paper 6/12 — [[zhang-2025-mcma-task-migration]]** — Zhang et al. 2025, *Multi-Agent DRL With Trajectory Prediction for Task Migration-Assisted Computation Offloading*. Added [[vehicular-mec]], [[task-migration]], [[informer-trajectory-prediction]], [[centralized-training-decentralized-execution]].

**Paper 7/12 — [[wang-2025-uav-swarm-stackelberg]]** — Wang et al. 2025, *Optimizing Spectrum Sharing in UAV Swarms: A Stackelberg Game-Based Incentive Mechanism* (IEEE TVT). Added [[stackelberg-game]], [[overlay-underlay-spectrum-access]], [[matching-theory-for-resource-allocation]], [[low-altitude-intelligent-network]]. First wireless-foundations track entry.

**Paper 8/12 — [[zhang-2025-ssac-mgi-heterogeneous-uav]]** — Zhang et al. 2025, *Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled MEC*. Added [[heterogeneous-uav-fleet]], [[safe-reinforcement-learning]], [[collision-avoidance-mgi]].

**Paper 9/12 — [[bi-2025-sg-mapg]]** — Bi et al. 2025, *SG-MAPG: A Three-Layer Hierarchical Model for Service Fairness and Cost Optimization in UAV-Assisted MEC*. No new concept pages — reuses [[stackelberg-game]], [[ma-pomdp]], [[hierarchical-aerial-mec]], [[matching-theory-for-resource-allocation]].

**Paper 10/12 — [[hao-2025-priority-aware-task-driven-co]]** — Hao et al. 2025, *Task-Driven Priority-Aware Computation Offloading Using DRL*. Added [[event-driven-vs-slot-driven-offloading]], [[task-priority-in-mec]].

**Paper 11/12 — [[wang-2025-lae-network-survey]]** — Wang et al. 2025, *Toward Realization of Low-Altitude Economy Networks* (IEEE TCCN). Added [[generative-ai-for-mec]] (placeholder for future GAI-MEC sources). Anchors the wiki's LAE thread.

**Paper 12/12 — [[xie-2026-uav-multisource-fusion]]** — Xie et al. 2026, *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks* (IEEE TWC). Added [[cooperative-perception]], [[dynamic-constrained-multi-objective-optimization]]. All 12 initial raw sources curated.

## Raw-source housekeeping

The LLM-Wiki desktop app emits an automated "external batch delete" log entry every time it prunes raw MinerU artifacts (origin PDFs, `full.md`, and `origin_file.html` files) for papers that were ingested, parsed, and curated. These are bookkeeping events, not curation decisions — **every block recorded "0 wiki pages" deleted**. The 89 verbose per-file blocks that previously interleaved with the curation history have been consolidated here:

- **2026-05-28:** 15 automated prune events (~34 raw artifact files), across the first wave of curated papers (HAP-NOMA, Aerial-ISAC, vehicular P-DQN, aerial-marine SAR, CMOP path-planning, DRO aerial-MEC, HAP-UAV video offloading, maritime IoT, ISAC-for-LAE, dispersed-computing, hierarchical aerial computing, interdependent-task scheduling, spectrum-sharing, terrain-aware MEC, multi-source fusion).
- **2026-05-29:** 74 automated prune events (~352 raw artifact files, including one 108-file bulk event), across the batch-3 and batch-4 curated papers (UAV-swarm stochastic game, AoI/energy tradeoff, UAV-LEO game, SAGIN FL handover, traffic-aware SAGIN, IRS two-stage energy, perception-aided SAGIN, trajectory/caching/migration, multi-UAV priority offloading, AIGC diffusion contract, ASAP swarm, anti-jamming, service-experience caching, satellite-marine offloading, double-edge SAMIN, three-tier maritime, SWIPT-MEC, and the rest of batches 3-4).

Net effect across all events: **0 wiki pages deleted**; only redundant raw parse/PDF artifacts were pruned by the app. The authoritative raw parses for all 82 curated sources remain under `raw/sources/<Folder>/full.md`.
- **2026-05-31:** 1 automated prune event (5 raw artifact files) for the two duplicate MinerU re-ingests removed during cleanup (the space-named Stackelberg spectrum-sharing and UAV multi-source vehicular fusion folders); the underscore-named curated originals are unaffected.
