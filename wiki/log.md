# Research Log

Reverse-chronological activity log (newest first). Curation and audit passes are kept in full; the LLM-Wiki desktop app's automated raw-file deletion events are consolidated under [Raw-source housekeeping](#raw-source-housekeeping) at the foot of this file.

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
