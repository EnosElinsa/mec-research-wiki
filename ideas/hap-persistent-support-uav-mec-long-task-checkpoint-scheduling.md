# HAP 持久提交支持的 UAV-MEC 长任务检查点调度与崩溃恢复

## I. 引言

灾害现场的分区影像建图、有限视频片段分析和三维重建等业务，通常在输入采集结束后仍需经历多个计算阶段。搭载计算模块的无人机（unmanned aerial vehicle，UAV）靠近数据源，能够缩短初始执行路径并及时启动处理；高空平台（high-altitude platform，HAP）则以广域覆盖、较稳定的能源供给和较强算力，为空中移动边缘计算（mobile edge computing，MEC）提供跨区域协同能力 [1], [2]。本文把这类业务限定为有限输入长任务：任务已经接纳并在某架 UAV 上启动，不能在一个服务周期内必然完成，可以安全暂停，且能够从给定输入和保存下来的可恢复状态确定性重放；下文把这种状态称为检查点。任务不包括无限视频流，也不包括无法去重的外部副作用。

空中平台持续提供覆盖，并不等于某个任务的计算状态能够持续存在。受电池容量约束，UAV 需要按计划返航、换电或轮换 [3], [4]；突发硬件故障还可能使执行节点永久退出。AeroGuard 说明 UAV 故障可以由在线模型检测 [5]，但检测不能保住故障节点的易失内存；本文采用的崩溃即停语义是独立建模假设，并非由该文献推出。若任务只保存原始输入，执行节点退出后虽然可以从头重算，但此前完成的工作全部丢失。对于接近截止期的长任务，服务覆盖仍然连续，计算结果却可能因回滚而无法按时提交。

围绕节点离场与故障，现有研究大体形成三条与本文动机直接相关的路线。第一类在已知切换前完成分流，或根据移动预测迁移服务实例 [6], [7]；第二类在故障后激活任务备份 [8]，或为 UAV 业务保护数据与模型冗余 [9]；第三类通过检查点、恢复或有状态迁移保存运行状态 [10], [11]。这些路线分别回答了“离场前如何完成或迁移”“主节点失效后由谁接替”和“运行状态如何跨节点延续”，但尚未共同回答：在 UAV 计算、UAV–HAP 带宽和 HAP 恢复资源均受限时，何时提交哪个长任务的状态，才能同时控制检查点开销、故障回滚和截止期风险。

本文因此把 HAP 从协同计算节点进一步用作远端持久提交点。版本 0 的不可变输入归档由接纳层在本文控制时域开始前完成，其传输与存储成本是所有方法共同承担的外生项；本文不再声称检查点控制层省去了这次归档回传。初始任务仍在 UAV 上执行，是因为任务接纳层已根据近源启动时延和 HAP 预留算力完成放置，使任务可以就近启动且不占用 HAP 计算资源。本文不重新优化接纳与初始放置，并以“任务从一开始仅在 HAP 执行”作为必要基线；该基线使用同一版本 0 归档前提，并完整计入 HAP 计算资源。与仅保证链路或平台存活不同，本文关心的是 UAV 离场后，HAP 是否拥有一个经过确认、可被唯一恢复且能在截止期前继续执行的任务版本。

一次完整的任务生命周期包含 UAV 执行、状态序列化、检查点上传、HAP 持久写入、确认应答（ACK）返回、退出检测、状态恢复和最终结果提交。本文用当前剩余工作量表示执行节点易失内存中的最新进度，用已提交剩余工作量表示 HAP 最近确认的恢复点；两者之差是退出后需要重做的回滚量。检查点尝试只有在上传、写入和确认全部完成后才形成已提交版本。为防止双主提交，HAP 为每个任务维护执行世代（epoch）、当前执行者（owner）、租约（lease）和检查点版本（checkpoint version），并用隔离令牌（fencing token）拒绝过期状态与过期结果。链路失联本身不等同于 UAV 崩溃；租约到期后，旧执行者必须停止产生外部可见提交。HAP 只接受当前执行世代的第一个最终结果，因此“剩余工作量降为零”也不等于任务已经完成。

在上述协议语义下，本文研究任务接纳、初始 UAV 和轮换表给定后的在线调度。健康且未离场时，任务保持在初始 UAV；计划离场或已观测崩溃后，任务先按选定恢复配置占用 HAP 资源，恢复完成后只能由 HAP 接续。控制器在每个时隙观测当前进度、真实已提交进度、节点状态、电量、保守信道参数和短期故障概率，联合决定中央处理器（central processing unit，CPU）频率、检查点尝试及其带宽和已知事件后的恢复配置。目标函数最小化归一化服务能耗与概率加权回滚风险，同时硬性满足资源容量、持久存储、租约安全、计划离场边界、已知恢复中断、任务截止期和 UAV 返航电量。未来尚未发生的崩溃只进入风险项；本文不声称一个确定性滚动计划可以对所有未知故障路径给出硬时限保证。

该问题的困难来自协议事件、任务阶段和连续资源的跨时隙耦合。仅固定检查点尝试仍不足以得到凸子问题，还必须固定恢复配置、恢复起点、完成模式和任务阶段；执行者路径则由初始执行者、已知计划离场、已观测故障和恢复状态唯一导出。本文先用最优资源条件下的提交时延必要条件安全删除必然不可行的候选，再将完整模型写成混合整数凸规划（mixed-integer convex programming，MICP）。当全部离散模式固定后，连续资源子问题可由速率透视函数和凸上图表示；仅在强对偶条件满足时，才采用广义 Benders 分解生成有效对偶割。基于故障概率阈值的候选裁剪另列为启发式，因为它可能删除全局最优解。

本文的主要贡献如下。

1. **问题贡献：** 将 UAV 易失执行进度与 HAP 远端持久提交状态纳入同一长任务生命周期，并用执行世代、租约、版本确认和隔离令牌明确界定计划离场、崩溃恢复及最终结果唯一提交的可执行语义。
2. **方法贡献：** 区分可优化的检查点尝试 \(u\) 与执行后才观测到的提交确认 \(q\)，在完整剩余截止期范围内联合优化 CPU、带宽和离散整时隙恢复配置；给出安全候选筛选、精确 MICP 与条件成立时的广义 Benders 求解路径。
3. **认识贡献：** 提出可证伪的“检查点—主备”交叉条件：状态较小、恢复资源充足且回滚代价高时，远端检查点应优于故障后激活的完整主备；状态较大、链路拥塞或恢复窗口过短时，该优势应消失。

本文其余内容安排如下。第 II 节按离场前迁移、主备保护和有状态恢复三类路线评述相关研究。第 III 节定义协议语义、任务状态、恢复过程与优化问题。第 IV 节给出安全筛选、精确 MICP 和条件式广义 Benders 方法。第 V 节设计可复现实验。附录给出创新边界、风险收缩方案和可证伪命题。

## II. 相关工作

### A. 离场前完成与服务迁移

已知移动或切换边界时，最直接的做法是在边界到来前完成分流。Ren 等把车辆任务划分到车辆、路侧单元（roadside unit，RSU）和高空平台站（high-altitude platform station，HAPS），并要求 RSU 承担的部分在车辆离开覆盖区前完成，从而把计划切换转化为可计算的完成时限 [6]。该模型利用 HAPS 承接跨覆盖计算，但不保存离场节点上已经形成的运行时状态。Feng 等根据车辆移动预测联合优化多 UAV 服务迁移和轨迹，使服务实例跟随需求变化 [7]。其核心对象是实例位置与长期迁移开销，而不是崩溃后从已确认执行点继续一个有限输入长任务。

电池轮换研究进一步说明了离场边界的系统性。Ye 等联合调度飞行速度、计算卸载和换电，使 UAV 在能量约束下维持 MEC 服务 [3]；Liu 等通过周期轮换和替换航路维持应急通信覆盖 [4]。这类方法能够回答 UAV 何时离场、由谁接替，但任务通常需要在离场前完成或重新分配。本文把计划离场看作检查点必须完成确认的确定性边界，而不是假设未完成运行状态会自动随服务接替转移。

### B. 主备副本与故障后接替

主备机制通过预先配置冗余对象缩短故障后的接替时间。Long 等把主任务与备份任务放在不同边缘子网，并在主任务失败后启动备份，以故障容忍开销和业务时延为联合决策依据 [8]。这里的备份是故障后激活，而非持续并行执行；其保护成本主要来自副本放置和重启，未显式维护“当前进度—已提交进度”的差值。本文将这一故障后激活的主备（failure-activated primary–backup）机制保留为核心基线，避免把主备优势弱化为一个不真实的始终双执行方案。

UAV 鲁棒计算还关注数据、模型和故障发现。两层子模型划分方法通过数据备份和动态服务器选择保护森林火灾检测流程 [9]；AeroGuard 结合多类模型实现实时 UAV 故障检测 [5]。前者保护训练数据与模型子任务，不等同于任务主备或任意程序的可恢复运行状态；后者只支持“故障检测技术可用”这一事实，不支持本文的 crash-stop 语义，也不提供未来时隙的真实故障概率，更不能替代检查点持久确认。本文只把检测延迟作为已观测故障后的恢复组成，把另行校准的风险分数用作软权重。

### C. 检查点、恢复与有状态迁移

有状态迁移最接近本文的状态保护对象。KubeSPT 面向长时间运行的有状态容器，通过内存检查点、预拷贝和恢复迁移 Kubernetes 容器组（Pod），并指出脏页收敛、链路瓶颈和资源竞争会改变迁移时延 [10]。Rong 等把视频分析应用状态区分为永久、关键和临时状态，比较检查点恢复（checkpoint/restore）、预拷贝和后拷贝，说明状态大小和更新速率可能使实时迁移失去优势 [11]。这些工作证明了恢复状态并非抽象的零成本变量，但其目标主要是通用边缘/云系统中的迁移完成，不包含 UAV 电池轮换、HAP 共享恢复算力和概率加权回滚的联合调度。

任务进度预测可为检查点决策提供侧面证据。Yao 等根据神经网络处理器（neural processing unit，NPU）任务的完成比例预测剩余执行时间，并用软抢占调整单节点调度 [12]；其抢占不复制完整内存，因此不能直接证明跨节点恢复。另一方面，UAV–HAP 协同 MEC 已研究跨层任务卸载和通信、计算资源分配 [1], [2]，但通常把任务视为可分卸载工作量，而非带版本、租约和外部提交语义的运行实例。综上，检查点/恢复和双进度本身都不是本文首次提出；本文的研究位置是把远端提交协议、计划轮换、崩溃回滚、HAP 共享恢复和任务截止期闭合为一个可执行的 UAV–HAP 长任务调度问题。

## III. 系统模型与问题建模

### A. 网络对象、任务边界与剩余规划范围

考虑由 UAV 集合
$$
\mathcal M=\{1,\ldots,M\}
$$
和一架 HAP \(h\) 构成的空中 MEC 系统，可执行节点集合为
$$
\mathcal N=\mathcal M\cup\{h\}.
$$
时间被划分为长度为 \(\Delta\) 的时隙。控制器在时隙 \(\tau\) 只下发当前时隙动作，但优化范围覆盖所有活跃任务的完整剩余截止期：
$$
T_\tau=\max_{j\in\mathcal J_\tau}t_j^{\mathrm d},
\qquad
\mathcal H_\tau=\{\tau,\ldots,T_\tau-1\}.
$$
已经执行的历史动作和确认结果被冻结，下一时隙根据真实确认、故障和链路观测重新求解。由此，滚动求解不会因为固定短窗口截断而遗漏远端截止期。

任务 \(j\) 的接纳时刻、截止时刻、有限输入大小、初始计算量和最终输出大小分别为 \(t_j^{\mathrm a}\)、\(t_j^{\mathrm d}\)、\(D_j\)、\(C_j\) 和 \(O_j\)。任务由有限个可安全暂停的阶段 \(\mathcal S_j\) 构成。令 \(s_j[t]\in\mathcal S_j\) 表示时隙开始时的当前易失阶段，\(s_j^{-}[t]\) 表示本槽计算后的阶段；二者由任务的确定性阶段状态机与剩余工作共同确定。阶段 \(s\) 的可恢复状态大小、序列化周期和恢复周期分别记为 \(S_{j,s}\)、\(C_{j,s}^{\mathrm{ser}}\) 和 \(C_{j,s}^{\mathrm{rs}}\)，由离线剖析得到。任务必须满足确定性重放和结果幂等提交；无限流、不可回滚外部写入和跨任务不可分事务不在本文范围内。

任务接纳层已经指定初始执行 UAV，HAP 保存版本 0 的不可变输入对象。版本 0 使用独立的初始化阶段 \(s_j^{(0)}\)、恢复周期 \(C_{j,0}^{\mathrm{rs}}\) 和恢复配置集合，不把它伪装成某个运行时检查点阶段。近源预处理、接纳与初始放置不是本文决策变量。令 \(\bar s_j[t]\) 和 \(\widehat{\bar s}_j[t]\) 分别表示 HAP 真实已提交版本与名义预测已提交版本对应的阶段。初始时
$$
R_j[t_j^{\mathrm a}]=\bar R_j[t_j^{\mathrm a}]=C_j,
\qquad
v_j[t_j^{\mathrm a}]=0,
\qquad
\bar S_j[t_j^{\mathrm a}]=0,
\qquad
\bar s_j[t_j^{\mathrm a}]
=\widehat{\bar s}_j[t_j^{\mathrm a}]
=s_j^{(0)}.
$$
其中 \(R_j[t]\) 是当前执行者易失状态中的剩余周期，\(\bar R_j[t]\) 是 HAP 最近已确认版本对应的剩余周期，\(v_j[t]\) 是已提交检查点版本号。\(v_j[t]=0\) 时，\(\bar s_j=s_j^{(0)}\) 只选择版本 0 的专用恢复配置；\(v_j[t]>0\) 时，\(\bar s_j\) 才表示运行时检查点的 committed stage。

### B. 可用性、执行者、租约与隔离

令 \(\bar a_m[t]\in\{0,1\}\) 表示 UAV \(m\) 按既定轮换表是否在岗，计划离场边界集合为
$$
\mathcal D_m=\{d:\bar a_m[d-1]=1,\ \bar a_m[d]=0\}.
$$
令 \(F_m[t]\in\{0,1\}\) 表示进入时隙 \(t\) 前是否已经检测到崩溃即停（crash-stop）故障。它是外生观测状态并具有吸收性：
$$
F_m[t+1]\ge F_m[t],
\qquad
a_m[t]=\bar a_m[t](1-F_m[t]),
\qquad
a_h[t]=1.
$$
未来故障不被预先写入 \(F_m[t]\)。边界参数 \(\eta_j^{\mathrm{evt}}[e]\in\{0,1\}\) 只标记已知计划离场或在入口边界 \(e\) 已经观测到的崩溃，不是优化变量。链路暂时不可用只会使上传或确认失败，不自动令 \(F_m[t]=1\)。

槽末事件严格按以下顺序处理：先完成本槽协议；若 HAP 已持久写入并返回检查点 ACK，则记录 \(q_j[t]=1\)；若当前执行世代的结果已被持久接受，则记录 \(\zeta_j[t]=1\)；随后才应用进入下一时隙边界 \(t+1\) 的 crash-stop 观测 \(F_m[t+1]\) 和事件参数 \(\eta_j^{\mathrm{evt}}[t+1]\)。因此，边界崩溃可以使 UAV 易失状态失效，却不能撤销已经落账的检查点或最终结果。优化模型不允许槽内源节点崩溃（source crash）；槽内只允许链路或协议阶段失败。阶段级源节点崩溃仅作为超出模型保证的原型压力测试。

任务执行者不是可以逐槽任意切换的调度动作。令 \(m_j^0\) 为任务接纳时确定的初始 UAV，协议状态
$$
o_j[t]\in\{m_j^0,\mathrm{recover},h,\mathrm{terminal}\}
$$
按固定状态机演化：健康且未到计划离场边界时保持 \(m_j^0\)；已知离场或已观测崩溃后进入恢复态 \(\mathrm{recover}\)；恢复完成后只能转为 \(h\)；最终结果被接受后转为终态 \(\mathrm{terminal}\)。任务不能直接跳到另一架 UAV。记
$$
x_{j,m_j^0}[t]=\mathbb 1\{o_j[t]=m_j^0\},\quad
x_{j,h}[t]=\mathbb 1\{o_j[t]=h\},
$$
$$
r_j[t]=\mathbb 1\{o_j[t]=\mathrm{recover}\},\quad
y_j[t]=\mathbb 1\{o_j[t]=\mathrm{terminal}\}.
$$
其中 \(y_j[t]\) 是实际日志状态；未来名义时域使用对应的预测终态变量 \(\widehat y_j[t]\)，并取
$$
\widehat y_j[\tau]=y_j[\tau].
$$
执行模式 \(x,r\) 在时域起点由真实 \(o_j[\tau]\) 初始化，此后按名义状态机导出。它们是状态机的独热（one-hot）编码而非自由执行者决策，在规划时域满足
$$
x_{j,m_j^0}[t]+x_{j,h}[t]+r_j[t]+\widehat y_j[t]=1,
\qquad
x_{j,m_j^0}[t]\le a_{m_j^0}[t].
$$
终态具有吸收性：
$$
y_j[t+1]\ge y_j[t],
\qquad
\widehat y_j[t+1]\ge\widehat y_j[t].
$$
结合独热约束、\(u_j[t]\le x_{j,m_j^0}[t]\) 和后文的 \(z\) 门控，进入终态后执行、检查点、恢复和结果提交动作全部为零。

HAP 为任务维护 \((e_j,o_j,\ell_j,v_j)\)：执行世代、当前执行者、租约截止时刻和检查点版本。只有携带当前执行世代、当前执行者和合法前驱版本的消息才可被接受。若当前执行者未在 \(\ell_j\) 前续租，它必须停止产生外部可见提交；HAP 在进入恢复时递增 \(e_j\)，新执行世代充当隔离令牌。迟到的旧检查点和旧结果均被拒绝。该规则把双主提交（split-brain）安全从优化假设变成可验证协议条件。

### C. 槽首快照、任务进度与真实确认

任务在时隙 \(t\) 获得的有效计算周期为
$$
W_j[t]=\Delta\sum_{i\in\{m_j^0,h\}}f_{j,i}[t],
\qquad
0\le f_{j,i}[t]\le F_i^{\max}x_{j,i}[t],
$$
并满足
$$
0\le W_j[t]\le R_j[t],
\qquad
R_j^{-}[t]=R_j[t]-W_j[t].
$$
任务的确定性阶段状态机同时给出槽末易失阶段 \(s_j^{-}[t]\)。\(R_j^{-}[t]\) 与 \(s_j^{-}[t]\) 都在槽末协议和边界事件之前形成。

令 \(u_j[t]\in\{0,1\}\) 表示名义计划在时隙 \(t\) 发起一次检查点尝试，并满足
$$
u_j[t]\le x_{j,m_j^0}[t].
$$
本文采用保守的“槽首原子快照 + copy-on-write”语义：若 \(u_j[t]=1\)，源 UAV 在槽首对
$$
\mathcal X_j^{\mathrm{snap}}[t]
=\bigl(R_j[t],s_j[t]\bigr)
$$
建立不可变快照。该快照的大小与序列化周期分别为 \(S_{j,s_j[t]}\) 和 \(C_{j,s_j[t]}^{\mathrm{ser}}\)。快照后的任务计算可以与序列化、上传和 HAP 写入同槽并行，但任务 CPU 与序列化 CPU 仍共享总频率；copy-on-write 保证本槽后续计算不会改写快照。这是首版协议的适用假设：应用状态和运行时必须能够在槽首形成跨组件一致快照；若只能得到 torn snapshot 或无法隔离后续写入，则不得使用同槽并行语义，须退化为 stop-the-world 或显式分段时长模型。

令 \(\theta_j^{\mathrm{cp,up}}[t]\) 和 \(\theta_j^{\mathrm{cp,wr}}[t]\) 分别表示检查点上传与 HAP 持久写入时长，\(\rho_j^{\mathrm{cp,wr}}[t]\) 表示 HAP 分配的检查点写带宽。所有辅助资源受 \(u\) 门控：
$$
0\le f_{j,m_j^0}^{\mathrm{ser}}[t]
\le F_{m_j^0}^{\max}u_j[t],
\qquad
0\le b_j^{\mathrm{cp}}[t]
\le B^{\mathrm{up}}[t]u_j[t],
$$
$$
0\le\theta_j^{\mathrm{cp,up}}[t],
\theta_j^{\mathrm{cp,wr}}[t]\le\Delta u_j[t],
\qquad
0\le\rho_j^{\mathrm{cp,wr}}[t]
\le\nu_h^{\mathrm{wr}}u_j[t].
$$
因此 \(u_j[t]=0\) 时，上述序列化、通信和写入资源全部为零。这里的 \(f_{j,m_j^0}^{\mathrm{ser}}[t]\) 是本槽保守频率预留：CPU 容量和动态能耗按整槽频率上界计入，即使序列化实际只占本槽一部分时间，也不把该写法解释成精确的槽内占用。需要回收这部分保守裕度时，应改用子槽占用变量或预计算分段 profile。检查点和结果使用同一受测上行功率 \(P_{m_j^0}^{\mathrm{up}}\)，UAV \(m_j^0\) 到 HAP 的保守上行速率为
$$
\Gamma_{m_j^0,h}(b,t)
=b\log_2\!\left(
1+\frac{P_{m_j^0}^{\mathrm{up}}
\underline g_{m_j^0,h}[t]}{N_0b}
\right).
$$
名义计划只有在槽首快照的完整提交链能够在本槽完成时才允许 \(u_j[t]=1\)：
$$
u_j[t]=1\ \Longrightarrow\
\theta_j^{\mathrm{cp,up}}[t]\ge
\frac{S_{j,s_j[t]}}
{\Gamma_{m_j^0,h}(b_j^{\mathrm{cp}}[t],t)},
$$
$$
u_j[t]=1\ \Longrightarrow\
\theta_j^{\mathrm{cp,wr}}[t]\ge
\frac{S_{j,s_j[t]}}
{\rho_j^{\mathrm{cp,wr}}[t]},
$$
$$
u_j[t]=1\ \Longrightarrow\
\frac{C_{j,s_j[t]}^{\mathrm{ser}}}
{f_{j,m_j^0}^{\mathrm{ser}}[t]}
+\theta_j^{\mathrm{cp,up}}[t]
+\theta_j^{\mathrm{cp,wr}}[t]
+T_{j,m_j^0}^{\mathrm{cp,ack}}[t]
\le\Delta .
$$
这些指示约束在实现中用阶段 one-hot、传输时长透视形式和凸上图展开。

令 \(q_j[\tau]\in\{0,1\}\) 表示首个实际执行时隙结束后从 HAP 日志读到的真实检查点确认。只有槽首快照完成序列化、上传、持久写入和 ACK，且执行世代、当前执行者与租约检查通过，才记录 \(q_j[\tau]=1\)。\(q\) 不是未来优化变量。

当前窗口的真实 committed state 来自 HAP 日志。名义状态以
$$
\widehat{\bar R}_j[\tau]=\bar R_j[\tau],
\quad
\widehat v_j[\tau]=v_j[\tau],
\quad
\widehat{\bar S}_j[\tau]=\bar S_j[\tau],
\quad
\widehat{\bar s}_j[\tau]=\bar s_j[\tau]
$$
为初值，并按
$$
\widehat{\bar R}_j[t+1]=
\begin{cases}
R_j^{-}[t], & x_{j,h}[t]=1,\\
R_j[t], & u_j[t]=1,\\
\widehat{\bar R}_j[t], & \text{其他情况},
\end{cases}
$$
$$
\widehat{\bar S}_j[t+1]=
\begin{cases}
S_{j,s_j^{-}[t]}, & x_{j,h}[t]=1,\\
S_{j,s_j[t]}, & u_j[t]=1,\\
\widehat{\bar S}_j[t], & \text{其他情况},
\end{cases}
$$
$$
\widehat{\bar s}_j[t+1]=
\begin{cases}
s_j^{-}[t], & x_{j,h}[t]=1,\\
s_j[t], & u_j[t]=1,\\
\widehat{\bar s}_j[t], & \text{其他情况},
\end{cases}
\qquad
\widehat v_j[t+1]=\widehat v_j[t]+u_j[t].
$$
HAP 本地执行的槽末状态直接持久化；UAV 检查点只保存槽首 \(R_j[t]\) 与 \(s_j[t]\)。因此，即使名义 \(u=1\)，本槽新产生的 \(W_j[t]\) 仍属于未提交进度。

执行首时隙后，真实 committed state 只能由 HAP 本地持久执行或真实 \(q_j[\tau]\) 更新：
$$
\bar R_j[\tau+1]=
\begin{cases}
R_j^{-}[\tau], & x_{j,h}[\tau]=1,\\
R_j[\tau], & q_j[\tau]=1,\\
\bar R_j[\tau], & \text{其他情况},
\end{cases}
$$
$$
\bar S_j[\tau+1]=
\begin{cases}
S_{j,s_j^{-}[\tau]}, & x_{j,h}[\tau]=1,\\
S_{j,s_j[\tau]}, & q_j[\tau]=1,\\
\bar S_j[\tau], & \text{其他情况},
\end{cases}
$$
$$
\bar s_j[\tau+1]=
\begin{cases}
s_j^{-}[\tau], & x_{j,h}[\tau]=1,\\
s_j[\tau], & q_j[\tau]=1,\\
\bar s_j[\tau], & \text{其他情况},
\end{cases}
\qquad
v_j[\tau+1]=v_j[\tau]+q_j[\tau].
$$
旧版本在新版本 ACK 前一直保留，ACK 后才能回收。下一窗口用这组真实状态替换上一窗口的预测。

令 \(a_j^{\mathrm{evt}}[\tau+1]\) 表示第 III-D 节定义的下一时隙入口边界有效恢复触发。检查点确认与结果接受先落账，随后才应用边界事件：
$$
R_j[\tau+1]=
\begin{cases}
\bar R_j[\tau+1], & a_j^{\mathrm{evt}}[\tau+1]=1,\\
R_j^{-}[\tau], & a_j^{\mathrm{evt}}[\tau+1]=0,
\end{cases}
$$
$$
s_j[\tau+1]=
\begin{cases}
\bar s_j[\tau+1], & a_j^{\mathrm{evt}}[\tau+1]=1,\\
s_j^{-}[\tau], & a_j^{\mathrm{evt}}[\tau+1]=0.
\end{cases}
$$
$$
\widetilde L_j[\tau]
=a_j^{\mathrm{evt}}[\tau+1]
\bigl(\bar R_j[\tau+1]-R_j^{-}[\tau]\bigr)\ge0.
$$
对规划时域中的未来已知边界，使用完全对应的名义递推
$$
R_j[t+1]=
\begin{cases}
\widehat{\bar R}_j[t+1], & a_j^{\mathrm{evt}}[t+1]=1,\\
R_j^{-}[t], & a_j^{\mathrm{evt}}[t+1]=0,
\end{cases}
$$
$$
s_j[t+1]=
\begin{cases}
\widehat{\bar s}_j[t+1], & a_j^{\mathrm{evt}}[t+1]=1,\\
s_j^{-}[t], & a_j^{\mathrm{evt}}[t+1]=0.
\end{cases}
$$
因此恢复后的 current stage 与 committed stage 一致，事件时的易失阶段不会泄漏到恢复配置或后续阶段递推中。
若本槽槽首快照确认后立即发生边界崩溃，则回滚量恰含本槽新计算 \(W_j[\tau]\)，符合 copy-on-write 语义。

令 \(z_j[t]\in\{0,1\}\) 表示名义最终结果提交模式。结果必须在槽首已经完成，不能把本槽末才算出的结果在同槽上传：
$$
z_j[t]\le x_{j,m_j^0}[t]+x_{j,h}[t],
\qquad
z_j[t]=1\ \Longrightarrow\ R_j[t]=0.
$$
令 \(z_j^{\mathrm{up}}[t]\in\{0,1\}\) 表示结果由初始 UAV 上传，并用
$$
z_j^{\mathrm{up}}[t]\le z_j[t],
\quad
z_j^{\mathrm{up}}[t]\le x_{j,m_j^0}[t],
\quad
z_j^{\mathrm{up}}[t]\ge
z_j[t]+x_{j,m_j^0}[t]-1
$$
线性关联。结果上传时长、写入时长和 HAP 结果写带宽分别记为
\(\theta_j^{\mathrm{out,up}}[t]\)、
\(\theta_j^{\mathrm{out,wr}}[t]\) 和
\(\rho_j^{\mathrm{out,wr}}[t]\)，并满足
$$
0\le b_j^{\mathrm{out}}[t]
\le B^{\mathrm{up}}[t]z_j^{\mathrm{up}}[t],
\qquad
0\le\theta_j^{\mathrm{out,up}}[t]
\le\Delta z_j^{\mathrm{up}}[t],
$$
$$
0\le\theta_j^{\mathrm{out,wr}}[t]\le\Delta z_j[t],
\qquad
0\le\rho_j^{\mathrm{out,wr}}[t]
\le\nu_h^{\mathrm{wr}}z_j[t].
$$
UAV 结果需满足
$$
z_j^{\mathrm{up}}[t]=1\ \Longrightarrow\
\theta_j^{\mathrm{out,up}}[t]\ge
\frac{O_j}
{\Gamma_{m_j^0,h}(b_j^{\mathrm{out}}[t],t)},
$$
而所有结果模式均须满足
$$
z_j[t]=1\ \Longrightarrow\
\theta_j^{\mathrm{out,wr}}[t]\ge
\frac{O_j}{\rho_j^{\mathrm{out,wr}}[t]},
$$
$$
z_j[t]=1\ \Longrightarrow\
\theta_j^{\mathrm{out,up}}[t]
+\theta_j^{\mathrm{out,wr}}[t]
+T_j^{\mathrm{out,ack}}[t]\le\Delta .
$$
对 HAP 本地结果，\(\theta^{\mathrm{out,up}}=0\)，但结果仍占用持久写带宽。

预测终态按
$$
\widehat y_j[t+1]=\widehat y_j[t]\lor z_j[t]
$$
递推。令 \(\zeta_j[\tau]\in\{0,1\}\) 表示首个实际时隙结束后 HAP 日志中的真实结果接受记录；UAV 结果需要上传、写入和 ACK，HAP 本地结果需要持久写入。真实终态只能按
$$
y_j[\tau+1]=y_j[\tau]\lor\zeta_j[\tau]
$$
更新。\(q_j[\tau]\) 与 \(\zeta_j[\tau]\) 都先于边界 crash 落账；若任一真实确认失败，系统保留旧真实状态并在下一窗口重规划。

### D. 计划离场、有效事件与逐 offset 恢复配置

对 \(d\in\mathcal D_{m_j^0}\)，若任务在离场边界仍未名义完成，则离场后可用状态必须等于 HAP 名义 committed state：
$$
\widehat y_j[d]=0\ \Longrightarrow\
R_j^{-}[d-1]=\widehat{\bar R}_j[d].
$$
在槽首快照语义下，若最后服务槽 \(d-1\) 才执行检查点，则
\(\widehat{\bar R}_j[d]=R_j[d-1]\)。因此上式只有在
\(W_j[d-1]=0\)，等价于该任务的执行 CPU \(f_{j,m_j^0}[d-1]=0\) 时才能成立；最后一槽可以序列化并提交槽首快照，却不能同时产生新的未提交进度。
等价地，模型显式加入
$$
u_j[d-1]=1,\ \widehat y_j[d]=0
\ \Longrightarrow\
f_{j,m_j^0}[d-1]=0,
\qquad d\in\mathcal D_{m_j^0}.
$$

以下统一把 \(e\) 记为时隙 \(e\) 的入口边界，即协议槽 \(e-1\) 结束之后、恢复槽 \(e\) 开始之前。令 \(\eta_j^{\mathrm{evt}}[e]\in\{0,1\}\) 表示边界 \(e\) 是否存在已知计划离场或已经观测的 crash。令
\(x_{j,m_j^0}^{\mathrm{pre}}[e]=\mathbb 1\{o_j[e^-]=m_j^0\}\) 表示协议已落账但边界事件尚未生效时，任务是否仍由初始 UAV 持有；在名义路径中它由槽 \(e-1\) 的执行者和状态机确定。令
$$
y_j^{\mathrm{evt}}[e]=
\begin{cases}
y_j[e], & \text{当前已观测边界},\\
\widehat y_j[e], & \text{未来计划边界}.
\end{cases}
$$
由于 \(y_j[e]\) 与 \(\widehat y_j[e]\) 已分别吸收槽 \(e-1\) 的真实 \(\zeta_j[e-1]\) 与名义 \(z_j[e-1]\)，该门控使用的是 post-commit、pre-event 终态；同槽结果已接受的任务不会再触发恢复。
有效恢复触发定义为
$$
a_j^{\mathrm{evt}}[e]
=\eta_j^{\mathrm{evt}}[e]\,
x_{j,m_j^0}^{\mathrm{pre}}[e]\,
\bigl(1-y_j^{\mathrm{evt}}[e]\bigr).
$$
该三元积用标准 AND 线性化。它明确排除两类伪事件：任务已经终态，或任务早已恢复到 HAP、只是原初始 UAV 后来离场。只有 \(a_j^{\mathrm{evt}}[e]=1\) 才进入恢复态。

恢复对象只由 committed version 和 committed stage 决定。定义扩展阶段集合
$$
\mathcal S_j^{\mathrm{rs}}=\{0\}\cup\mathcal S_j,
$$
其中 \(s=0\) 专指版本 0，且
$$
Z_{j,0}=D_j,\qquad
C_{j,0}^{\mathrm{rs}}\ \text{由初始化恢复剖析给出};
$$
对运行时 committed stage \(s\in\mathcal S_j\)，
$$
Z_{j,s}=S_{j,s},\qquad
C_{j,s}^{\mathrm{rs}}\ \text{由该 committed stage 的剖析给出}.
$$
当前已观测事件使用真实 \((v_j[e],\bar s_j[e])\)，未来计划事件使用预测
\((\widehat v_j[e],\widehat{\bar s}_j[e])\)。令
\(\chi_{j,s}^{\mathrm{evt}}[e]\in\{0,1\}\) 为相应恢复阶段的 one-hot 指示：版本号为 0 时只允许 \(s=0\)，版本号大于 0 时只允许真实或预测 committed stage；事件前的易失阶段 \(s_j^{-}[e-1]\) 不参与恢复配置选择。

对每个 \(s\in\mathcal S_j^{\mathrm{rs}}\)，离线建立有限配置集合
\(\mathcal K_{j,s}^{\mathrm{rs}}\)。配置 \(k\) 给出常数恢复长度
\(L_{j,k,s}^{\mathrm{rs}}\) 和每个 offset
\(\ell=0,\ldots,L_{j,k,s}^{\mathrm{rs}}-1\) 的预计算数组
$$
\left(
\rho_{j,k,s,\ell}^{\mathrm{rd}},
\phi_{j,k,s,\ell}^{\mathrm{rs}},
E_{j,k,s,\ell}^{\mathrm{io}}
\right).
$$
三者分别是该恢复槽的 HAP 持久读取带宽、恢复 CPU 频率和不含 CPU 动态能耗的读取/固定恢复能耗。每个配置在进入候选集前必须满足
$$
\sum_{\ell=0}^{L_{j,k,s}^{\mathrm{rs}}-1}
\rho_{j,k,s,\ell}^{\mathrm{rd}}\Delta
\ge Z_{j,s},
$$
$$
\sum_{\ell=0}^{L_{j,k,s}^{\mathrm{rs}}-1}
\phi_{j,k,s,\ell}^{\mathrm{rs}}\Delta
\ge C_{j,s}^{\mathrm{rs}}.
$$
若恢复协议要求先读完再恢复，则配置生成器强制在读取完成前
\(\phi_{j,k,s,\ell}^{\mathrm{rs}}=0\)；读取完成后的 offset 可令
\(\rho_{j,k,s,\ell}^{\mathrm{rd}}=0\)。因此模型不会把串行阶段错误地写成整个恢复区间同时占满 CPU 和读取带宽。

令 \(g_{j,k,s}[e]\in\{0,1\}\) 表示事件边界 \(e\) 选择阶段 \(s\) 的配置 \(k\)。选择约束为
$$
g_{j,k,s}[e]\le
\chi_{j,s}^{\mathrm{evt}}[e],
\qquad
\sum_{s\in\mathcal S_j^{\mathrm{rs}}}
\sum_{k\in\mathcal K_{j,s}^{\mathrm{rs}}}
g_{j,k,s}[e]
=a_j^{\mathrm{evt}}[e].
$$
为线性展开资源占用，定义 offset 占用二元变量
\(\gamma_{j,k,s,\ell}[t]\)，并对有效索引施加
$$
\gamma_{j,k,s,\ell}[t]
=g_{j,k,s}[t-\ell].
$$
于是
$$
r_j[t]=
\sum_{s,k,\ell}\gamma_{j,k,s,\ell}[t].
$$
在同一任务至多一个有效恢复事件的假设下，上式仍为二元状态。最后一个 offset 结束后，任务执行者只能从 \(\mathrm{recover}\) 转为 HAP；不能转回原 UAV 或跳到另一架 UAV。

计划离场取 \(T_j^{\mathrm{det}}=0\)。对当前已经观测的 crash，
\(T_j^{\mathrm{det}}\) 是进入本窗口前已经耗掉的中断时间。中断约束为
$$
a_j^{\mathrm{evt}}[e]=1\ \Longrightarrow\
T_j^{\mathrm{det}}
+\sum_{s,k}
g_{j,k,s}[e]L_{j,k,s}^{\mathrm{rs}}\Delta
\le H_j^{\max}.
$$
名义计划还要求
$$
\widehat y_j[t_j^{\mathrm d}]=1.
$$
截止期由逐 offset 恢复占用、HAP 共享计算、结果写入与确认组成的完整剩余时域计划验证。未来尚未发生的未知 crash 没有确定事件边界，不施加全路径硬保证，只进入软风险并在真实事件发生后重规划。

### E. 共享资源、写入瓶颈、存储与能量

UAV \(m\) 的任务计算和快照序列化共享 CPU：
$$
\sum_j f_{j,m}[t]
+\sum_j f_{j,m}^{\mathrm{ser}}[t]
\le F_m^{\max}a_m[t].
$$
HAP 的任务计算与当前 offset 的恢复 CPU 共享同一频率预算。定义
$$
F_h^{\mathrm{agg}}[t]
=
\sum_j f_{j,h}[t]
+\sum_{j,k,s,\ell}
\phi_{j,k,s,\ell}^{\mathrm{rs}}
\gamma_{j,k,s,\ell}[t],
$$
并要求
$$
F_h^{\mathrm{agg}}[t]\le F_h^{\max}.
$$
持久存储读取同样只按当前 offset 计量：
$$
\sum_{j,k,s,\ell}
\rho_{j,k,s,\ell}^{\mathrm{rd}}
\gamma_{j,k,s,\ell}[t]
\le\nu_h^{\mathrm{rd}}.
$$

检查点与结果都要竞争 HAP 持久写带宽：
$$
\sum_j\rho_j^{\mathrm{cp,wr}}[t]
+\sum_j\rho_j^{\mathrm{out,wr}}[t]
\le\nu_h^{\mathrm{wr}}.
$$
检查点和 UAV 结果上传还共享 UAV–HAP 上行带宽：
$$
\sum_j b_j^{\mathrm{cp}}[t]
+\sum_j b_j^{\mathrm{out}}[t]
\le B^{\mathrm{up}}[t].
$$
\(\rho^{\mathrm{cp,wr}}\) 已由 \(u\) 门控，\(\rho^{\mathrm{out,wr}}\) 已由 \(z\) 门控；对应写时长分别受
\(S_{j,s_j[t]}/\rho_j^{\mathrm{cp,wr}}\) 和
\(O_j/\rho_j^{\mathrm{out,wr}}\) 约束。链路不可达令 \(u=0\)，并在结果位于 UAV 时令 \(z^{\mathrm{up}}=0\)；HAP 本地结果仍须竞争写带宽。

HAP 在检查点 ACK 前同时保留版本 0、旧 committed checkpoint 和在途快照。定义预测在途检查点峰值
\(\widehat S_j^{\mathrm{cp,fly}}[t]\)，它在 \(u_j[t]=1\) 的序列化、上传和写入阶段按 \(S_{j,s_j[t]}\) 计；定义预测在途结果
\(\widehat O_j^{\mathrm{fly}}[t]\)，它在 \(z_j[t]=1\) 的上传或写入阶段按 \(O_j\) 计。最终结果确认后，HAP 还需保留结果 \(L_j^{\mathrm{ret}}\) 个时隙，或直到外部消费者确认，以较晚者为准。令
\(\widehat\chi_j^{\mathrm{out,ret}}[t]\in\{0,1\}\) 为名义结果保留指示，由 \(z\) 的首次发生时隙线性递推；真实执行使用由 \(\zeta\) 更新的
\(\chi_j^{\mathrm{out,ret}}[t]\)。

可用存储 \(G_h^{\max}\) 必须覆盖阶段相关的峰值对象：
$$
\sum_j\Bigl(
D_j
+\widehat{\bar S}_j[t]
+\widehat S_j^{\mathrm{cp,fly}}[t]
+\widehat O_j^{\mathrm{fly}}[t]
+\widehat\chi_j^{\mathrm{out,ret}}[t]O_j
\Bigr)
\le G_h^{\max}.
$$
该式保守地保留 committed checkpoint；实现可在结果保留期结束后回收它。首时隙下发前，安全执行器使用真实 \(\bar S_j[\tau]\)、真实在途对象和真实结果保留指示复核同一峰值，避免把名义 \(u,z\) 当成实际 ACK。

CPU、无线、持久读写和协议能耗参数由平台测量校准。UAV \(m\) 的 CPU 动态能耗为
$$
E_m^{\mathrm{cpu}}[t]
=\kappa_m\Delta
\left(
\sum_j f_{j,m}[t]
+\sum_j f_{j,m}^{\mathrm{ser}}[t]
\right)^3.
$$
HAP 恢复 CPU 必须进入与任务计算相同的总频率立方：
$$
E_h^{\mathrm{cpu}}[t]
=\kappa_h\Delta
\left(F_h^{\mathrm{agg}}[t]\right)^3.
$$
逐 offset 参数
\(E_{j,k,s,\ell}^{\mathrm{io}}\) 只包含不在上述立方中计费的持久读取与固定恢复能耗，因此
$$
E_h^{\mathrm{rs,io}}[t]
=
\sum_{j,k,s,\ell}
E_{j,k,s,\ell}^{\mathrm{io}}
\gamma_{j,k,s,\ell}[t].
$$
检查点与结果持久写能耗按实际写入 bit 和固定提交开销计量；无线能耗按发送功率乘传输时长计量。由此，恢复 CPU 不会被漏算，也不会同时出现在 profile 总能耗和 CPU 立方中而重复计费。

UAV 的固定轨迹由上层给定，推进能耗虽是目标中的常数项，仍进入电池递推：
$$
B_m[t+1]
=B_m[t]-E_m^{\mathrm{fly}}[t]
-E_m^{\mathrm{cpu}}[t]
-E_m^{\mathrm{tx}}[t].
$$
每个仍在空中且可用的 UAV 都必须保留返航储备：
$$
a_m[t]=1\ \Longrightarrow\
B_m[t]\ge
E_m^{\mathrm{return}}[t]+B_m^{\mathrm{safe}}.
$$

### F. 优化问题

离散决策包括检查点尝试 \(u\)、当前/committed stage one-hot、恢复配置 \(g\)、逐 offset 占用 \(\gamma\) 和结果提交模式 \(z\)；执行者、恢复区间与预测终态由协议状态机导出。真实检查点确认 \(q\)、真实结果接受 \(\zeta\)、计划/已观测事件和可用性 \(F\) 都是观测或外生参数，不是未来控制变量。连续决策包括任务/序列化 CPU、UAV–HAP 带宽、HAP 持久读写带宽及相应传输时长。

对尚未发生的初始 UAV 崩溃，令 \(\widehat p_{m_j^0}[t]\) 为校准后的短期风险分数。定义动作后原始暴露量
$$
D_j^{\mathrm{post}}[t]
=\widehat{\bar R}_j[t+1]-R_j^{-}[t]\ge0.
$$
引入辅助变量 \(\Lambda_j[t]\)，用指示约束规定
$$
x_{j,m_j^0}[t]=1,\
\widehat y_j[t+1]=0
\ \Longrightarrow\
\Lambda_j[t]=D_j^{\mathrm{post}}[t],
$$
$$
x_{j,m_j^0}[t]=0\ \text{或}\
\widehat y_j[t+1]=1
\ \Longrightarrow\
\Lambda_j[t]=0.
$$
这些关系可由 \(0\le D_j^{\mathrm{post}}\le C_j\) 的已知上下界线性化。概率加权回滚风险为
$$
\mathcal R_\tau
=\sum_{t\in\mathcal H_\tau}
\sum_j
w_j\widehat p_{m_j^0}[t]\Lambda_j[t].
$$
若 \(z_j[t]=1\)，则 \(\widehat y_j[t+1]=1\)，名义完成任务不再被处罚。若 \(u_j[t]=1\)，槽首快照只把 \(\widehat{\bar R}[t+1]\) 更新为 \(R_j[t]\)，所以本槽新计算 \(W_j[t]\) 仍留在 \(\Lambda_j[t]\) 中；这是 copy-on-write 因果语义的预期结果。

滚动问题写为
$$
\begin{aligned}
\mathbf P_\tau:\quad
\min\quad&
\frac{\sum_{t\in\mathcal H_\tau}E^{\mathrm{svc}}[t]}{E_0}
+\lambda\frac{\mathcal R_\tau}{R_0}\\
\mathrm{s.t.}\quad&
\text{C1：执行者状态机、可用性、执行世代、租约与隔离；}\\
&\text{C2：槽首快照、真实/预测 committed state、stage 和终态递推；}\\
&\text{C3：模式门控的 CPU、上行、HAP 读写带宽、时长和峰值存储；}\\
&\text{C4：有效事件、逐 offset 恢复占用与计划离场边界；}\\
&\text{C5：电池递推、返航储备和中断上限；}\\
&\text{C6：}\widehat y_j[t_j^{\mathrm d}]=1,\ \forall j\in\mathcal J_\tau;\\
&\text{C7：变量定义与状态初值。}
\end{aligned}
$$
所有 \(L_{j,k,s}^{\mathrm{rs}}\)、\(\rho_{j,k,s,\ell}^{\mathrm{rd}}\)、\(\phi_{j,k,s,\ell}^{\mathrm{rs}}\) 和 \(E_{j,k,s,\ell}^{\mathrm{io}}\) 都是阶段剖析后预计算的常数；\(g\) 与 \(\gamma\) 由线性等式关联。配合阶段 one-hot、指示约束、速率透视形式和凸上图后，\(\mathbf P_\tau\) 是 MICP。若状态大小或恢复资源需求无法由有限阶段和验证过的凸上界表达，则不能沿用该结论。

## IV. 求解方法与可验证保证

### A. 安全候选筛选与精确 MICP

对任务 \(j\)、UAV \(m\)、时隙 \(t\) 和可能的槽首阶段 \(s\)，令 \(\Gamma_{m,h}^{\max}[t]\) 是把全部可用上行带宽分给该任务时的最大保守速率。把 HAP 全部持久写带宽 \(\nu_h^{\mathrm{wr}}\) 分给该快照，并把 UAV CPU 全部分给序列化，可得阶段候选的最乐观提交时间
$$
T_{j,m,s}^{\min}[t]
=
\frac{C_{j,s}^{\mathrm{ser}}}{F_m^{\max}}
+\frac{S_{j,s}}{\Gamma_{m,h}^{\max}[t]}
+\frac{S_{j,s}}{\nu_h^{\mathrm{wr}}}
+T_{j,m}^{\mathrm{cp,ack}}[t].
$$
令 \(\mathcal S_j^{\mathrm{cand}}[t]\) 为离散阶段递推允许在时隙 \(t\) 槽首出现的阶段集合。只有当
$$
\min_{s\in\mathcal S_j^{\mathrm{cand}}[t]}
T_{j,m,s}^{\min}[t]>\Delta,
$$
即所有兼容 stage 的最乐观时间都超过一个时隙时，才可安全删除整个 \(u_j[t]=1\) 候选。若当前阶段已经确定，集合只含一个元素。筛选不能因为某一个较大阶段不可行就删除其他阶段候选。筛选后的完整 MICP 由商业或开源混合整数凸求解器直接求解，作为小中规模的精确基准。

### B. 条件式广义 Benders 分解

广义 Benders 分解（generalized Benders decomposition，GBD）只有在固定离散模式后得到凸连续子问题时才适用。大规模场景把所有离散模式放入主问题：
$$
\boldsymbol\xi=
\{u,g,\gamma,z,
\text{current-stage},
\text{committed-stage}\}.
$$
固定 \(\boldsymbol\xi\) 后，执行者与逐 offset 恢复占用由状态机唯一导出，预测 remaining work、committed stage 和版本选择变为仿射递推，连续变量只剩 CPU、上行/读写带宽和传输时长；Shannon 速率用凹透视函数表示，时间和能量约束使用凸上图。若该连续子问题满足 Slater 条件或其他足以保证强对偶的正则条件，则其最优对偶变量产生 GBD 最优性割；不可行子问题通过对偶射线产生可行性割。

算法在主问题和连续子问题之间迭代，直至上下界间隙小于 \(\epsilon\)。有限候选集、子问题精确求解和有效对偶割同时成立时，广义 Benders 收敛到筛选后 MICP 的全局最优解。若强对偶、精确子问题或阶段固定条件不成立，本文不声称该保证，改用完整 MICP 或将结果标注为近似解。由于这里的子问题是连续凸规划，方法称为广义 Benders，而不是逻辑 Benders。

### C. 风险候选启发式与在线流程

为缩短在线时间，可另行使用风险启发式：只在计划离场邻域、回滚量超过阈值或 \(\widehat p_m[t]\) 超过阈值的时隙保留检查点候选。该规则可能删除全局最优时隙，不能与安全时延筛选混写。实验必须分别报告“精确候选”“风险启发式”两种版本相对精确 MICP 的目标差距和截止期可行率。

每个时隙执行以下流程。

1. 读取 HAP 持久日志、真实 \(q\)、真实结果接受 \(\zeta\)、执行世代、租约、当前执行者、故障与链路状态。
2. 冻结历史，并把规划范围扩展到全部活跃任务的最晚截止期。
3. 按 stage-candidate 的最大资源必要条件安全删除不可行检查点候选。
4. 小规模直接求解 MICP；大规模在条件满足时运行广义 Benders。
5. 对首时隙动作复核执行世代、资源、存储、恢复中断和返航储备。
6. 下发带隔离令牌的动作，只执行首时隙。
7. 在边界记录真实检查点 ACK、结果接受 \(\zeta\) 和故障事件，更新状态后重求解。

### D. 保证边界与复杂度

安全候选筛选只提供“不删除任何可行提交”的必要条件保证。精确 MICP 提供给定模型与候选集内的全局最优基准。条件式广义 Benders 的最优性依赖强对偶和精确割；风险候选版本只有经验性能。滚动执行只保证当前已下发动作满足当前观测下的硬约束，对尚未发生且未建场景树的崩溃不提供全路径保证。

主问题的二元变量规模为
$$
O\!\left(|\mathcal J_\tau||\mathcal H_\tau|
\bigl(1+K_{\mathrm{stage}}
+K_{\mathrm{rs}}K_{\mathrm{stage}}L_{\mathrm{rs}}^{\max}\bigr)\right),
$$
最坏情况仍具有指数复杂度。安全筛选、热启动（warm start）和风险启发式降低的是实际搜索规模，不改变最坏复杂度类别。

## V. 实验与验证设计

### A. 可复现场景与参数获取

实验只生成有限输入、可暂停、可确定性重放的长任务，包括分区影像建图、有限视频段分析和批量三维重建。\(C_j\)、各阶段的 \(S_{j,s}\)、\(C_{j,s}^{\mathrm{ser}}\)、\(C_{j,s}^{\mathrm{rs}}\)，以及版本 0 的初始化恢复开销，均由容器检查点原型与 UAV/HAP 计算板实测。对每个 committed stage 和离散恢复配置，原型逐 offset 记录 \(\rho^{\mathrm{rd}}\)、\(\phi^{\mathrm{rs}}\) 与不含 CPU 动态能耗的 \(E^{\mathrm{io}}\)，并复核累计读取 bit 与恢复周期不低于该阶段的实际需求。检查点写、结果写、结果保留、ACK 时延和 HAP 读写能耗也从同一日志校准；信道使用飞行轨迹上的保守下界。计划轮换来自预先生成的飞行与换电表，崩溃在时隙边界注入，链路中断单独注入并遵守“链路失联不等于崩溃”。每组随机场景至少运行 30 个种子，报告均值、95% 置信区间和不可行比例。

协议验证使用可重复故障注入：在序列化、检查点/结果上传、HAP 写入和 ACK 阶段注入进程或链路失败，源节点崩溃只在时隙边界注入，并分别测试 ACK 落账前后两种情况。专门构造 \(u=1\) 且任务同槽继续计算的轨迹，验证成功 \(q\) 提交的是槽首 \((R_j[t],s_j[t])\)，而本槽新增 \(W_j[t]\) 在随后的边界事件中仍计入回滚；最后服务槽才检查点的轨迹还必须验证任务计算频率为零。原型还要在多线程状态更新、页复制和外部输入边界注入一致性扰动，检查恢复后的校验和与槽首逻辑状态是否一致；一旦出现 torn snapshot，该工作负载必须切换到 stop-the-world/分段时长版本并单列性能，不能继续使用 copy-on-write 同槽并行结果。只有检查点持久写入与 ACK 均成功的尝试允许 \(q=1\)；只有槽首 \(R_j[t]=0\) 且当前执行世代的结果被 HAP 持久接受才允许 \(\zeta=1\)。任一确认失败时，下一窗口必须从旧真实状态重规划，不能按名义 \(u\) 或 \(z\) 提前推进 committed state 或终态。边界崩溃不得撤销已确认版本，旧执行世代恢复后也不得产生第二个可见结果。额外的阶段级源节点崩溃仅作超出优化模型保证的压力测试，结果单列。仿真模型与原型日志使用同一状态机字段，避免只在公式中声明隔离令牌。

### B. 对比方法

实验至少包含以下基线。

1. **No-Checkpoint：** 不预留恢复资源；UAV 退出后再竞争 HAP 读、CPU 和结果写资源，并从版本 0 原始输入冷启动重算。
2. **Periodic：** 以固定周期检查点，周期通过验证集选择。
3. **Departure-Only：** 只在已知离场前提交最新状态。
4. **Primary–Backup：** 在与初始 UAV 不同故障域的 HAP 持久保存版本 0 并预热运行镜像，预留激活/恢复 CPU 和必要存储，但故障前不执行任务进度；事件后仍须读取完整输入并从头执行，资源口径遵循 failure-activated 语义。
5. **KubeSPT-Style：** 依据已知离场窗口进行预拷贝/有状态迁移，不使用未来故障概率。
6. **HAP-Only：** 任务从接纳开始就在 HAP 上执行。
7. **Ground-Persistent：** 用地面持久边缘节点替代 HAP，检验广域上行与 HAP 位置的作用。
8. **Exact-MICP：** 使用全部安全候选的精确基准。
9. **GBD-ExactCandidates：** 相同候选集上的条件式广义 Benders。
10. **GBD-RiskHeuristic：** 采用概率/回滚阈值裁剪的在线版本。

为避免把资源口径差异误报成算法收益，三类核心容错方法按下表实现；版本 0 输入归档 \(D_j\) 是所有方法共同的外生存储项，表中只列控制时域内的增量资源。

| 方法 | 备份节点与故障域 | 持久对象与存储 | 预留 CPU | 网络与写入 | 事件后路径 | 优化强度 |
|---|---|---|---|---|---|---|
| No-Checkpoint | HAP，与初始 UAV 分属不同故障域 | 仅共同版本 0；不保存中间进度 | 不预留；事件后与其他任务竞争 HAP CPU | 无运行时检查点流量；结果传输与写入完整计费 | 检测、冷启动读取、从输入重算、结果提交 | 使用同一时域和同一资源优化器调度事件后资源 |
| Primary–Backup | HAP，与初始 UAV 分属不同故障域 | 共同版本 0 加预热运行镜像/元数据；增量存储完整计费，输入不免费常驻 RAM | 故障前逐槽扣除声明的 CPU 容量并计实测待机能耗，故障后才能用于该任务 | 无中间检查点流量；激活信令、结果传输与写入完整计费 | 检测后按专用 activation profile 支付 \(D_j\) 的持久读带宽、I/O 能耗和激活 CPU，再从输入执行并提交结果；不继承主节点中间进度 | 在同一时域联合优化预留量、激活时机和事件后资源，不使用更弱的固定策略 |
| 本文方法 | HAP，与初始 UAV 分属不同故障域 | 版本 0、committed checkpoint、在途快照、在途及保留期结果 | 不隐藏独占预留；恢复和任务执行共享 HAP CPU | 检查点上传/写入、结果上传/写入及 ACK 全部计费 | 读取 committed stage、逐 offset 恢复、HAP 接续执行、结果提交 | Exact-MICP 与 GBD-ExactCandidates 使用同一候选和连续资源模型 |

Primary–Backup 的预热对象只包括运行镜像和元数据；版本 0 仍驻留持久存储，不把 \(D_j\) 隐式放入免费 RAM。其 activation profile 与本文恢复 profile 一样逐 offset 校验累计读取 bit、CPU 周期和 I/O 能耗。Periodic 与 Departure-Only 复用本文方法的写带宽、峰值存储、CPU、网络和 ACK 口径，只改变 \(u\) 的生成规则。KubeSPT-Style 的预拷贝流量、脏页与切换停顿均按实测值计费。HAP-Only 从接纳起占用 HAP CPU，Ground-Persistent 使用相同计算、存储和能量容量归一化。所有方法使用相同任务、轨迹、故障、信道、截止期、返航储备和能量参数；不能让 HAP-Only 或 Primary–Backup 获得未计费资源或更宽松的完成条件。

### C. 消融与指标

关键消融包括：错误地把计划尝试 \(u\) 当作真实确认 \(q\)、关闭执行世代/租约/隔离令牌、固定带宽、固定 CPU、固定状态大小、移除计划离场信息、用连续恢复时间替代离散恢复配置的整时隙占用、关闭热启动，以及关闭风险候选裁剪。协议消融预期不会只改变目标值，还可能产生确认幻觉、双执行者或重复最终结果，必须单独计数。

核心指标包括任务完成率、截止期违约率、外部结果确认时延、平均/尾部回滚周期、单位任务服务能耗、检查点流量、HAP CPU/存储拥塞、恢复中断、UAV 返航储备违约、求解时间、最优性间隙和协议安全错误数。协议正确实现时，过期检查点接受、双执行者提交和重复可见结果三项必须为零。

### D. 压力场景与负面结果

压力变量包括状态/输入比 \(S_j/D_j\)、脏状态增长、UAV–HAP 带宽、HAP 读写速率、HAP CPU 负载、离场提前量、故障风险、检测时延、任务松弛度和并发任务数。实验同时设置连续多个轮换窗口，检验版本与租约是否跨多次恢复保持一致，而不是只验证一次交接。

以下负面结果需要主动报告。

1. 状态过大时，检查点流量抵消回滚收益，Periodic 或 No-Checkpoint 可能更优。
2. HAP CPU/存储拥塞时，Ground-Persistent 或 Primary–Backup 可能具有更短恢复尾时延。
3. 截止期极紧时，任何恢复方案都不可行，任务应在接纳层被拒绝。
4. 风险预测失准时，GBD-RiskHeuristic 可能增加能耗或漏掉关键提交。
5. UAV–HAP 链路频繁中断时，尝试数增多但确认数不增加，\(u\) 与 \(q\) 的差异成为主要性能因素。
6. 初始任务本就适合 HAP 时，HAP-Only 应占优，说明 UAV 初始执行不是普遍成立的前提。
7. 若检查点状态与输入同量级且恢复窗口很短，failure-activated Primary–Backup 可能跨过本文方法的收益边界。

## 附录 A：创新边界与 PMI 审计

本文不把检查点/恢复、HAP 协同计算、UAV 轮换、任务进度或 Benders 分解单独声明为新颖点。创新主张限定在“远端持久提交协议语义与受资源约束调度的闭合”：计划变量 \(u,z\)、执行后观测 \(q,\zeta\)、版本、执行世代、租约、当前执行者和恢复配置均可映射到实际协议事件；其中 \(q,\zeta\) 明确不属于优化器可选动作。

| 维度 | 可证伪表述 |
|---|---|
| Problem | 在初始 UAV 已给定、HAP 不作为初始执行节点但可在恢复后接续执行时，如何联合控制检查点开销、计划离场、崩溃回滚、共享恢复和截止期。若 HAP-Only 在全部场景占优，则该问题前提缺乏承载力。 |
| Method | MICP 规划检查点尝试 \(u\) 和结果提交模式 \(z\)，执行后由日志观测 \(q,\zeta\) 并替换预测状态；版本化状态机和恢复配置约束后续动作。仅在全部离散模式固定且连续子问题强对偶时使用广义 Benders。若协议注入出现旧版本接受或重复结果，方法闭环失败。 |
| Insight | 远端检查点相对主备的优势由状态传输成本、未提交工作量、恢复共享资源和截止期松弛共同决定。若扫参中不存在可重复交叉区间，该认识不成立。 |

## 附录 B：关键假设、风险与收缩方案

| 假设 | 失败风险 | 收缩方案 |
|---|---|---|
| 有限输入且可确定性重放 | 连续流或外部副作用无法从检查点一致恢复 | 收缩到分段封闭输入；外部写入经 HAP 幂等提交 |
| 运行时支持槽首原子快照与 copy-on-write | 多组件状态不一致或后续写入污染快照，导致恢复后状态不可重放 | 先做一致性故障注入；不通过时禁用同槽并行，退化为 stop-the-world 或显式分段时长模型 |
| 故障在时隙边界观测 | 时隙内故障会放大提交不确定性 | 缩短时隙，或扩展为阶段级场景模型 |
| HAP 本身高可用 | HAP 故障成为单点失效 | 仅讨论单 HAP 条件；扩展工作再做 HAP 复制 |
| 状态大小由离散阶段决定 | 连续脏页过程破坏凸子问题 | 使用分段上界；否则直接求解一般 MINLP |
| 风险分数已校准 | 失准导致错误候选裁剪 | 风险只进软目标；精确版本不使用概率裁剪 |
| HAP 可持久保存原始输入 | 输入不可用时版本 0 无法重放 | 接纳时验证输入对象与校验和，否则拒绝任务 |

## 附录 C：可证伪命题

1. **计划—确认分离命题：** 在相同故障轨迹下，用首槽真实 \(q\) 替换名义 \(u\) 的滚动模型，应比错误地把 \(u\) 当成确认结果的模型显著减少“被认为已保存但实际不可恢复”的任务；若两者在 ACK/写入故障注入下无差异，该分离没有实证必要。
2. **紧迫度单调性命题：** 其他条件固定时，未提交工作量增大或截止期松弛减小，不应推迟最早可行检查点；若存在稳定反例，应由资源竞争或状态阶段变化解释。
3. **检查点—主备交叉命题：** 随 \(S_j/D_j\) 增大、上行速率下降或恢复负载上升，远端检查点相对 failure-activated primary–backup 的优势应发生可重复反转。
4. **计划边界价值命题：** 在故障率相同条件下，已知离场边界应使 Departure-Only 或本文方法用更少检查点达到不低于纯风险策略的截止期完成率。
5. **提交语义命题：** 开启执行世代、租约和隔离令牌后，所有故障注入中的旧执行者提交和重复可见结果应为零，且名义 \(z=1\) 但真实 \(\zeta=0\) 时不得提前进入终态；关闭任一机制时至少一种构造场景应暴露错误。
6. **算法精确性命题：** 使用相同安全候选时，GBD-ExactCandidates 应在容差内复现 Exact-MICP 的目标值；若强对偶条件不满足，则不应继续报告该保证。
7. **HAP 承载力命题：** 相对 Ground-Persistent 和 HAP-Only，本文方法只有在广域可达性、近源初始计算和可接受恢复负载同时存在时才应占优；若这些因素去除后仍普遍占优，实验资源口径可能不公平。

## 参考文献

[1] Z. Jia, C. Cui, C. Dong, Q. Wu, Z. Ling, D. Niyato, and Z. Han, “Distributionally robust optimization for aerial multi-access edge computing via cooperation of UAVs and HAPs,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 10, pp. 10853–10867, Oct. 2025.

[2] M. Li, H. Wan, S. Lv, P. Si, H. Zhang, and F. R. Yu, “Joint optimization of latency and energy consumption for computing task offloading based on cooperative multi-UAV and HAP networks,” *IEEE Trans. Mobile Comput.*, early access, 2026, doi: 10.1109/TMC.2026.3683404.

[3] D. Ye, Z. Sun, W. Zhong, J. Kang, X. Huang, D. I. Kim, S. Xie, and C. Yuen, “Optimal flight speed scheduling and battery swapping in UAV-enabled mobile edge computing,” *IEEE Trans. Mobile Comput.*, vol. 25, no. 1, pp. 948–960, Jan. 2026.

[4] C. Liu, X. Xin, Y. Dai, and D. Xu, “Cost optimization of UAV swarm network for persistent emergency communication,” *IEEE Trans. Green Commun. Netw.*, vol. 10, pp. 1734–1748, 2026.

[5] T. Li, Z. Wei, Y. Feng, R. Yu, Z. Ma, Y. Shen, J. Ma, and Y. Liu, “AeroGuard: Towards real-time UAV fault detection with hybrid models,” *IEEE Trans. Mobile Comput.*, vol. 25, no. 6, pp. 9075–9088, Jun. 2026.

[6] Q. Ren, O. Abbasi, G. K. Kurt, H. Yanikomeroglu, and J. Chen, “Handoff-aware distributed computing in high altitude platform station (HAPS)–assisted vehicular networks,” *IEEE Trans. Wireless Commun.*, vol. 22, no. 12, pp. 8814–8827, Dec. 2023.

[7] W. Feng, W. Gao, J. Yao, L. Zhou, C. Yan, and T. Q. S. Quek, “Prediction-assisted multi-UAV online service migration and trajectory control for MEC-empowered vehicular networks,” *IEEE Trans. Mobile Comput.*, early access, 2026, doi: 10.1109/TMC.2026.3700894.

[8] S. Long, C. Rao, H. Liu, Y. Chen, Z. Li, J. Shang, and Q. Deng, “Fault-tolerant aware task offloading based on reinforcement learning in mobile edge computing,” *IEEE Trans. Mobile Comput.*, vol. 25, no. 5, pp. 6068–6082, May 2026.

[9] X. Li, W. Zhang, L. Liu, and P. Wang, “Two-tier submodel partition framework for enhancing UAV swarm robustness in forest fire detection,” *IEEE Trans. Mobile Comput.*, vol. 25, no. 1, pp. 1169–1183, Jan. 2026.

[10] H. Zhang, S. Wu, H. Fan, Z. Huang, W. Xue, C. Yu, S. Ibrahim, and H. Jin, “KubeSPT: Stateful pod teleportation for service resilience with live migration,” *IEEE Trans. Serv. Comput.*, vol. 18, no. 3, pp. 1500–1514, May–Jun. 2025.

[11] C. Rong, J. H. Wang, J. Wang, Y. Zhou, and J. Zhang, “Live migration of video analytics applications in edge computing,” *IEEE Trans. Mobile Comput.*, vol. 23, no. 3, pp. 2078–2092, Mar. 2024.

[12] Y. Yao, Y. Hu, Y. Dang, W. Tao, K. Hu, Q. Huang, Z. Peng, G. Yang, and X. Zhou, “Workload-aware performance model based soft preemptive real-time scheduling for neural processing units,” *IEEE Trans. Parallel Distrib. Syst.*, vol. 36, no. 6, pp. 1058–1070, Jun. 2025.
