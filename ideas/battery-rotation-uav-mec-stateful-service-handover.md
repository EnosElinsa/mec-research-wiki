# 电池轮换场景下无人机移动边缘计算有状态服务交接的终端可行性与在线调度

## I. 引言

移动边缘计算（mobile edge computing，MEC）把计算资源部署到网络边缘，使图像分析、设施巡检和环境感知等时延敏感业务能够在数据产生地点附近完成处理 [1]–[3]。当地面设施受损、覆盖不足或无法快速部署时，搭载计算模块的无人机（unmanned aerial vehicle，UAV）可以快速提供无线接入和边缘计算服务 [1], [2]。然而，单架 UAV 的覆盖范围、计算能力和电池容量均有限，难以支撑分布范围较广或持续时间较长的任务 [1], [4]。因此，持续时间超过单机续航的任务通常依靠多架 UAV 轮换值守：在役 UAV 返回基地补能，替补 UAV 飞抵任务区域并接替服务 [5]–[7], [24], [25]。

多机轮换能够延续无线覆盖和计算资源，却不能自动保证正在运行的服务连续。目标跟踪、流式分析等有状态服务需要保留会话上下文、处理进度和中间结果，才能继续处理后续输入 [14]–[16], [26], [27]。当承载服务的 UAV 被替换时，替补 UAV 只有取得这些运行状态，才能延续原有处理；否则，服务只能回退或重建，从而产生额外中断 [25], [29]。因此，电池轮换不仅要更换飞行平台，还必须在源 UAV 离场前完成服务状态交接。

与这一问题直接相关的有状态交接研究可按源节点是否必须在给定截止时刻前停止服务并离场分为两类。无硬离场期限的方法多面向持续供电的云边节点，或不要求源 UAV 限时返航的迁移场景；它们能够刻画状态更新、迭代同步和资源配置，但无需为离场与返航预留时间和能量 [13]–[16], [26]–[28]。有硬离场期限的方法面向低电量 UAV 的替补接管与状态恢复，但或把交接时长作为给定输入，或停留在迁移架构设计，尚未联合优化状态同步与并发交接资源 [25], [29]。两类方法因而都未能判断，当持续计算不断产生新状态、多个事件共享替补 UAV 与空空链路资源、源 UAV 又必须限时返航时，当前动作是否仍为后续交接保留可完成路径。

这一共同边界引出本文的多区域 UAV-MEC 电池轮换场景。正常运行时，每个区域由一架在役 UAV 处理任务，其余满足起飞条件的 UAV 在基地待命；当在役 UAV 接近返航能量边界时，控制器为其选择替补 UAV。替补到达后，源 UAV 在继续处理任务的同时，通过空空（air-to-air，A2A）链路预拷贝无法由输入重建的关键状态，并在选定的暂停时刻完成最终同步。替补 UAV 载入状态并确认接管后，源 UAV 开始返航；若交接不能在最晚离场时刻前完成，系统中止本次交接并执行安全返航。

该场景使任务处理、状态同步和返航安全在同一有限时域内相互耦合。控制器需要联合确定替补 UAV、预拷贝开始时刻、服务暂停时刻以及逐时隙中央处理器（central processing unit，CPU）频率和 A2A 带宽。提高 CPU 频率虽可减少任务积压，却会产生更多关键状态并消耗更多能量；增加某一事件的 A2A 带宽则会压缩其他并发交接的传输能力。所有交接还必须在源 UAV 的最晚离场时刻前完成，并为参与轮换的 UAV 保留返航能量。本文把当前状态下仍存在一组后续动作、能够完成交接并满足返航要求的性质称为终端可行性，并将上述过程建模为有限时域随机混合整数序贯决策问题，在控制任务队列的同时提高最小交接余量并限制交接失败或硬约束违约的概率。

求解该问题需要在每个时隙维持离场前的终端可行性，仅满足当前约束不足以保证这一性质。混合动作强化学习能够联合生成离散替补选择和连续资源分配 [21]–[23]，约束强化学习也可控制训练分布上的经验违约率 [18], [19]。然而，即时动作掩码和单时隙投影无法判断当前替补选择是否占用后续事件唯一可用的 UAV，也无法判断当前 CPU 与带宽动作是否会使后续同步路径消失。为此，本文以 PPO [17] 为混合动作性能策略，提出匹配感知的未来可行性屏蔽混合近端策略优化方法（matching-aware viability-shielded hybrid proximal policy optimization，MV-HPPO）。其中，匹配感知的离散方案屏蔽在选择替补后检查剩余事件是否仍能获得互不冲突的替补；未来可行性屏蔽则修正 CPU 与 A2A 带宽动作，使离场前仍保留完成状态同步、确认和安全返航的后续路径。

本文的主要贡献概括如下：

1. 建立电池轮换下的有状态服务交接模型，统一描述替补到达、关键状态预拷贝、最终同步、确认接管、中止和安全返航，并按时隙刻画任务处理产生的关键状态增量。
2. 构建有限时域随机混合整数在线优化问题，联合决定替补方案、交接时序、CPU 与 A2A 资源，统一刻画状态演化、并发竞争、最晚离场和返航能量对终端可行性的共同约束。
3. 提出 MV-HPPO，以剩余替补匹配和未来可行性屏蔽处理离散与连续动作的跨时隙依赖，并给出单窗口、多窗口生命周期和半实物验证方案，用于检验交接完成率、任务积压与返航安全。

本文其余内容安排如下。第 II 节综述 UAV 补能与轮换、任务与服务迁移以及混合动作在线优化；第 III 节建立系统、状态、协议与优化模型；第 IV 节介绍 MV-HPPO 及未来可行性屏蔽；第 V 节给出实验设计与验证方案；附录总结与最相关研究的区别及主要模型风险。

## II. 相关工作

本节从 UAV 补能与轮换、任务与服务迁移以及混合动作在线优化三个方面综述相关研究，并分析现有方法在电池轮换有状态服务交接中的局限。

### A. UAV 补能与轮换

多 UAV-MEC 研究已经联合考虑区域部署、用户关联、任务卸载、计算资源和飞行轨迹。Peng 等根据各区域的用户密度和计算需求调整 UAV 数量与部署位置 [1]；Pervez 等联合分配多 UAV 的通信和计算资源，以降低系统能耗与任务时延 [2]；Sun 等通过双时间尺度方法协调 UAV 轨迹、任务处理和无线资源 [3]。这些方法提高了机群在单个运行周期内的服务效率，但通常假设承担区域服务的 UAV 在该周期内始终可用。

为支持持续时间超过单架 UAV 续航能力的任务，补能研究把返航和换电纳入飞行与计算调度。Ye 等在巡检任务中联合决定飞行速度、任务卸载和途中换电安排 [4]；Li 等允许机群中的领航 UAV 返回基地补能，并通过动态聚类、应用放置和任务委托重新组织计算服务 [5]。面向持续通信，Liu 等利用周期轮换航路安排 UAV 依次到达灾区并动态调整多跳中继关系 [6]；Zhang 等让多架中继 UAV 先后接替工作，以延长端到端通信时间 [7]；Gupta 等则联合规划在役 UAV 和替补 UAV 的三维轨迹与带宽，以维持替换期间的地面用户速率 [24]。这些方法在原 UAV 返航时由其他 UAV 继续为任务区域提供无线通信或接收新任务，但没有处理正在运行的应用状态。面向低电量 UAV 的服务交接工作进一步使新 UAV 接收用户、计算任务及其当前状态 [25]；该方法依据给定带宽下预估的交接时间安排新 UAV 的出发和原 UAV 的回收，没有描述任务继续执行时交接数据量如何变化。

### B. 任务迁移与有状态服务迁移

UAV-MEC 中的任务迁移主要在用户移动或网络状态变化后，为未完成任务重新选择计算节点。Zhao 等联合优化 UAV 轨迹、任务卸载、服务缓存和迁移位置 [8]；Wang 等在动态多 UAV 网络中转移尚未处理的输入和部分计算结果 [9]；Feng 等根据车辆轨迹预测选择承载服务的 UAV，并同步调整多 UAV 轨迹 [10]。在更一般的 MEC 和空天地网络中，Shi 等在较长时间尺度选择服务迁移或任务重路由，再在时隙尺度分配卸载、CPU 和带宽 [11]；Han 等在卫星覆盖窗口结束前转移训练数据和当前模型，使后继节点继续联邦学习 [12]。这些方法把待传输的任务数据、服务程序或模型参数作为迁移工作量，重点优化迁移目的地及相应的通信和计算资源。

Qiu 等进一步考虑 UAV 为车辆承载有状态服务的场景，并联合优化车辆任务的卸载比例、UAV 位置和多项服务的迁移顺序 [13]。该工作把每项服务的迁移数据量设为承载该服务的虚拟机内存大小，再根据 UAV 间带宽计算迁移时间；多个服务按照源端和目标端是否存在资源冲突被划分为若干并行迁移组。该模型能够比较不同迁移顺序和 UAV 位置的影响，但没有描述服务继续运行时新状态的产生过程，迁移数据量在决策期间保持不变。数字孪生迁移还可根据目标节点的通信、CPU、内存和存储容量选择迁移位置 [20]，多智能体方法则联合决定任务迁移与连续资源分配 [21]；这些模型同样没有把计算过程中新增的服务状态纳入迁移工作量的时隙演化。

固定云和边缘基础设施上的在线迁移更细致地研究了服务运行期间的状态变化。Rong 等测量视频分析应用后发现，完整内存检查点会造成较长停机，而预拷贝在内存修改速度高于传输速度时可能无法收敛；其方法在目标节点预热不变状态、同步保持应用上下文所需的关键状态，并通过重放视频帧重建临时状态 [14]。Ma 等利用容器分层存储减少应用镜像的传输开销，同时对运行时内存执行差分迁移 [16]；KubeSPT 则在 Kubernetes 重调度中迁移网络连接和内存状态，并协调最终检查点、目标 Pod 创建和服务重定向 [15]。Calagna 等进一步建立迭代预拷贝的迁移时间和停机时间模型 [26]，并在 MOSE 框架中根据指标目标配置迁移方式、带宽和迭代次数 [27]。Fernando 等比较了预拷贝和后拷贝的状态传输过程，并针对源节点、目标节点或网络故障设计增量检查点恢复机制 [28]。上述研究能够描述状态更新、同步过程和迁移性能，但其源节点和目标节点均为持续供电的固定计算设施。

面向电池轮换的状态交接也已有直接探索。Ye 等考虑低电量 UAV 向新 UAV 转移当前计算状态，但把交接时间作为 UAV 调度的已知输入 [25]。Frejo-Martín 等提出电池轮换下的有状态微服务迁移架构，通过预传容器存储层并在源服务停止后传输最终检查点来恢复服务；其工作尚未评估迁移时间、网络开销和能耗，也没有优化并发交接的资源分配 [29]。这些工作已经覆盖固定迁移量下的 UAV 有状态服务迁移、电池触发的计算状态交接和状态保存架构，尚未在同一在线模型中刻画任务处理产生的新状态、源 UAV 的最晚离场时刻、替补 UAV 与 A2A 带宽竞争以及成功和中止分支的返航能量。

### C. 混合动作在线优化

动态 UAV-MEC 通常需要同时决定任务卸载、服务迁移、节点选择和连续资源分配。多智能体强化学习可以根据用户轨迹和网络状态联合决定任务迁移与资源分配 [21]，也可以在多 UAV 系统中协调飞行轨迹、任务卸载和功率控制 [22]。混合动作策略则可在同一求解框架中生成离散卸载决策和连续通信、计算资源 [23]。近端策略优化（proximal policy optimization，PPO）为连续控制提供了稳定的策略更新方式 [17]，约束策略优化和拉格朗日方法还可把长期失败率或资源违约表示为策略代价 [18], [19]。

上述强化学习方法主要通过奖励函数或长期期望代价表示时延、能耗和资源约束 [18], [19], [21]–[23]。这类处理能够降低训练和运行中的违约，但没有判断当前决策是否会使后续交接失去可行方案。对于电池轮换，一次替补选择会改变其他事件可选的 UAV，当前 CPU 分配会改变后续需要传输的状态量，带宽和能量消耗则会缩短离场前的剩余传输能力。现有在线优化研究尚未给出同时考虑上述跨时隙影响、交接截止时刻和安全返航要求的调度方法。

## III. 系统模型与问题建模

本文沿用多区域、多无人机、集中控制和分时隙运行的 UAV-MEC 架构 [1]–[3]。区域部署、地面用户关联、任务上行、安全航路和轮换触发由上层规划器给出；本文固定这些关系，只研究轮换事件触发后的服务运行层。服务镜像及永久状态在待命 UAV 上预置并可提前预热，终端或地面网关保留尚未确认的输入，易失状态可从输入序号重放 [14]；A2A 链路只同步由应用明确标识、无法从输入重建的关键状态更新。下文依次定义网络与角色、任务队列、版本化状态同步、协议与能量，再建立在线决策问题。

### A. 网络对象、角色与轮换过程

服务区域、无人机和业务会话的集合分别记为

$$
\mathcal R=\{1,\ldots,R\},\qquad
\mathcal U=\{1,\ldots,U\},\qquad
\mathcal I=\{1,\ldots,I\}.
$$

每个区域在任一正常运行时刻恰有一架在役 UAV，因此持续轮换至少需要 $U>R$。无人机集合包含在役、待命、执行替补航路、返航和换电等角色。只有当前未承担区域服务、替补航路、返航或换电任务并满足起飞能量条件的 UAV 才属于待命池。

会话 $i\in\mathcal I$ 位于区域 $r(i)\in\mathcal R$，区域 $r$ 内的会话集合为

$$
\mathcal I_r=\{i\in\mathcal I:r(i)=r\}.
$$

时间划分为长度为 $\Delta$ 秒的时隙，时隙 $t$ 从绝对时刻 $t\Delta$ 开始。时隙 $\tau$ 触发、且必须在本次交接时域内完成的轮换事件构成集合 $\mathcal N_\tau$。只有当 $\mathcal N_\tau\ne\varnothing$ 时，控制器才开启并优化包含 $T_{\mathrm w}$ 个时隙的交接窗口

$$
\mathcal W_\tau=\{\tau,\ldots,\tau+T_{\mathrm w}-1\}.
$$

其中 $|\mathcal W_\tau|=T_{\mathrm w}$。若 $\mathcal N_\tau=\varnothing$，则不建立 $\mathcal W_\tau$，常规服务控制器继续处理任务，且不定义或求解第 III-E 节的交接效用。为避免同一区域在一个交接窗口内发生链式接替，规定

$$
\sum_{n\in\mathcal N_\tau}\mathbb 1\{r_n=r\}\le1,
\qquad \forall r\in\mathcal R.
$$

事件 $n$ 的区域 $r_n$ 和源 UAV $u_n$ 由窗口开始时的服务关系确定。源 UAV 必须开始返航的最晚绝对时刻记为 $d_n^{\mathrm{dep}}$，单位为秒。候选方案集合为 $\mathcal P_n$；方案 $p\in\mathcal P_n$ 指定一架待命 UAV $v_{np}$、其到达后可开始预拷贝的时隙 $s_{np}$ 以及源 UAV 暂停写入的时隙 $c_{np}$，并满足

$$
\tau\le s_{np}<c_{np}<\tau+T_{\mathrm w}.
$$

每个候选方案已经通过待命角色、替补航路、速度、碰撞间距和到达时能量检查。后文还会给出确认与中止返航的终端证书；未通过该证书的方案不进入 $\mathcal P_n$。

令 $x_{np}\in\{0,1\}$ 表示事件 $n$ 是否选择方案 $p$。每个事件只选一个方案，将唯一选中的方案记为 $p_n$，并简记

$$
v_n=v_{np_n},\qquad s_n=s_{np_n},\qquad c_n=c_{np_n}.
$$

区域 $r$ 在时隙 $t$ 的合法服务所有者记为 $o_r[t]$。确认成功前，事件区域的所有者仍为源 UAV；成功确认后，只在 $(c_n+1)\Delta$ 更新为替补 UAV。源 UAV 在整个停机槽保持服务点位置及相应飞行模式，其返航航路和位置递推从 $t=c_n+1$ 开始。$o_r[t]$ 由协议状态递推，不是独立决策变量。

### B. 任务队列与服务质量

令 $Q_i[t]$ 表示时隙 $t$ 开始、接纳本槽到达之前的积压量，令 $A_i[t]$ 表示槽首完成上行并等待本槽接纳的数据量，二者单位均为 bit。控制器先观察 $Q_i[t]$ 与当期 $A_i[t]$，再选择本槽资源动作；未来 $A_i[k]$ 仍未知。地面上行链路由上层接入控制器分配，并满足保守容量条件

$$
A_i[t]\le\Delta\underline C_i^{\mathrm{up}}[t],
$$

其中 $\underline C_i^{\mathrm{up}}[t]$ 为该时隙的上行速率下界。

令 $c_i$ 表示处理 1 bit 数据所需的 CPU 周期数，$f_i[t]$ 表示分配给会话 $i$ 的 CPU 频率，单位为 cycle/s。事件暂停写入的时隙不执行该区域任务。定义区域计算指示量

$$
d_r[t]
:=
1-
\sum_{n:r_n=r}
\sum_{p\in\mathcal P_n}
x_{np}\mathbb 1\{t=c_{np}\}.
$$

可行资源动作将在 C2 中满足停机时隙 $f_i[t]=0$。时隙 $t$ 实际处理的数据量为

$$
\mu_i[t]
:=
\frac{d_{r(i)}[t]f_i[t]\Delta}{c_i},
$$

A2A 与 CPU 使用独立资源，可在同一时隙内并行工作；信息因果关系是 A2A 只服务槽首已经封存的欠同步状态，CPU 处理本槽任务所产生的关键更新到槽末才封存。因此两类动作都使用同一个 $\Delta$，但新更新不能被本槽 A2A 传走。队列在槽末递推为

$$
Q_i[t+1]
:=
\left[Q_i[t]+A_i[t]-\mu_i[t]\right]^+.
$$

无人机 $u$ 的最大总 CPU 频率为 $F_u^{\max}$，会话缓存上限为 $Q_i^{\max}$。除逐时隙队列上限外，后文还把窗口平均归一化队列直接写入目标，使控制器不能仅靠降低 CPU 来扩大交接余量。

### C. 应用辅助的关键状态同步与 A2A 传输

每个有状态服务把恢复对象分成三类。永久状态包括应用镜像、模型参数和运行库，由替补 UAV 预置或预热；易失状态是可由保留输入重放的临时特征；关键状态是无法由输入重建、且替补 UAV 为保持正确上下文必须取得的数据，例如跟踪历史、版本化窗口摘要、去重记录和已确认的应用结果。只有关键状态进入 A2A 同步模型。

本文采用应用辅助的版本化增量日志，而不是把通用脏页物理大小等同于服务状态。应用在一个时隙内部合并同一键的覆盖写，并在槽末把合并结果封存为带单调序号、此后不可修改的增量记录。不同槽已经封存的增量不再相互合并、抵消或改写；更强的跨槽压缩不属于首版模型。时隙 $t$ 槽末形成的非负封存量记为 $W_n[t]$，单位为 bit。它由与任务处理无关的背景更新和处理输入引起的更新构成：

$$
W_n[t]
:=
d_{r_n}[t]
\left(
\widetilde W_n^{\mathrm{bg}}[t]
+
\sum_{i\in\mathcal I_{r_n}}
\widetilde\eta_{ni}[t]\mu_i[t]
\right),
$$

其中 $\widetilde W_n^{\mathrm{bg}}[t]\ge0$ 和 $\widetilde\eta_{ni}[t]\ge0$ 分别是本槽动作执行后实现的背景更新量与写入放大系数，后者单位为 bit/bit。由于跨槽封存记录不可抵消，欠同步量可以按非负标量 $W_n[t]$ 相加；这些带波浪号的随机量以及 $W_n[t]$ 都在本槽 CPU 动作后才实现并于槽末可观测，不能作为动作前策略状态。策略使用的 $\overline W_{n|t}^{\mathrm{bg}}[k]$ 与 $\overline\eta_{ni|t}[k]$ 只是基于既有历史校准的未来上界。

令 $H_n[\tau]>0$ 表示窗口开始时源 UAV 上尚未在替补端形成副本的初始关键状态快照大小，单位为 bit。预拷贝开始时，替补 UAV 仍缺少的同步工作量为

$$
G_n[s_n]
:=
H_n[\tau]
+
\sum_{t=\tau}^{s_n-1}W_n[t].
$$

交接事件 $n$ 在时隙 $t$ 获得的 A2A 带宽为 $b_n[t]$，系统用于状态交接的总带宽为 $B^{\mathrm A}$，二者单位均为 Hz。对候选方案 $p$，实际信道功率增益为无量纲量 $h_{np}[t]$，源 UAV 发射功率 $P_{np}^{\mathrm A}$ 的单位为 W，噪声功率谱密度 $N_0$ 的单位为 W/Hz。实际 A2A 速率为

$$
C_{np}^{\mathrm A}[t]
:=
b_n[t]\log_2\left(
1+\frac{P_{np}^{\mathrm A}h_{np}[t]}
{N_0b_n[t]}
\right),
$$

其中 $b_n[t]=0$ 时按连续延拓定义 $C_{np}^{\mathrm A}[t]=0$。选定方案的速率简记为 $C_n^{\mathrm A}[t]$。

在 $s_n\le t<c_n$ 的预拷贝阶段，A2A 链路只能发送时隙开始已经封存的欠同步量 $G_n[t]$。本槽 CPU 产生的 $W_n[t]$ 在槽末才封存，不能享用本槽完整 A2A 容量。该时隙实际发送的数据量和替补 UAV 下一时隙仍缺的同步工作量分别为

$$
L_n[t]
:=
\min\left\{G_n[t],C_n^{\mathrm A}[t]\Delta\right\},
$$

$$
G_n[t+1]
:=
G_n[t]-L_n[t]+W_n[t]
=
\left[G_n[t]-C_n^{\mathrm A}[t]\Delta\right]^+
+W_n[t].
$$

数据无线电的实际开启时间为

$$
\ell_n^{\mathrm A}[t]
:=
\begin{cases}
L_n[t]/C_n^{\mathrm A}[t],&C_n^{\mathrm A}[t]>0,\\
0,&C_n^{\mathrm A}[t]=0,
\end{cases}
$$

该定义用于 $s_n\le t<c_n$ 的预拷贝；$b_n[t]=0$ 或没有待传工作量时，预拷贝数据无线电不开启。

源 UAV 在时隙 $c_n$ 开始时冻结应用和版本日志，此时 $W_n[c_n]=0$。协议元数据大小记为 $D_n^{\mathrm{meta}}$，停机拷贝需发送的数据量为

$$
D_n^{\mathrm{stop}}
:=
G_n[c_n]+D_n^{\mathrm{meta}}.
$$

### D. 确认协议、离场边界与能量安全

冻结应用、替补端载入关键状态并重放恢复所需易失状态、以及交换确认所需的固定时间分别为 $\tau_n^{\mathrm{freeze}}$、$\tau_n^{\mathrm{apply}}$ 和 $\tau_n^{\mathrm{ack}}$，固定协议时间为

$$
\tau_n^{\mathrm{fix}}
:=
\tau_n^{\mathrm{freeze}}
+
\tau_n^{\mathrm{apply}}
+
\tau_n^{\mathrm{ack}}.
$$

事件 $n$ 在停机槽内完成冻结、数据发送、状态应用和确认所需的协议完成时间记为

$$
T_n^{\mathrm{proto}}
:=
\begin{cases}
\displaystyle
\tau_n^{\mathrm{fix}}
+\frac{D_n^{\mathrm{stop}}}{C_n^{\mathrm A}[c_n]},
&C_n^{\mathrm A}[c_n]>0,\\[2mm]
\tau_n^{\mathrm{fix}},
&C_n^{\mathrm A}[c_n]=0,\ D_n^{\mathrm{stop}}=0,\\
+\infty,
&C_n^{\mathrm A}[c_n]=0,\ D_n^{\mathrm{stop}}>0.
\end{cases}
$$

业务允许的最大中断为 $I_n^{\max}$。本文采用保守整槽协议：服务在 $c_n\Delta$ 冻结，整个时隙 $c_n$ 都不执行任务；即使协议提前完成，所有权和服务世代也只在 $(c_n+1)\Delta$ 原子生效。因此成功交接的服务中断按一个完整时隙 $\Delta$ 计，并要求

$$
T_n^{\mathrm{proto}}\le\Delta\le I_n^{\max}.
$$

源 UAV 冻结后，停机阶段的数据无线电运行到数据传完或本槽可用于数据发送的时间耗尽。其开启时间只用于能量计量，不产生槽内计算或提前接管：

$$
\ell_n^{\mathrm{stop}}
:=
\begin{cases}
\displaystyle
\min\left\{
\frac{D_n^{\mathrm{stop}}}{C_n^{\mathrm A}[c_n]},
\left[\Delta-\tau_n^{\mathrm{fix}}\right]^+
\right\},
&C_n^{\mathrm A}[c_n]>0,\\[2mm]
0,&C_n^{\mathrm A}[c_n]=0.
\end{cases}
$$

成功分支中，源 UAV 在停机槽内保持原候选方案指定的悬停/航电模式，只在槽末 $(c_n+1)\Delta$ 切换为返航模式；确认报文早到不改变这一槽末切换时刻。为保证失败分支也能按时离场，令 $\tau_n^{\mathrm{abort}}$ 表示槽末发现未确认后封存日志、撤销本次交接并进入返航模式的最长时间。候选方案必须满足

$$
(c_n+1)\Delta\le d_n^{\mathrm{dep}},
\qquad
(c_n+1)\Delta+\tau_n^{\mathrm{abort}}
\le d_n^{\mathrm{dep}}.
$$

在中断上限内仍可多承载的关键状态量定义为交接余量

$$
M_n
:=
\left(\Delta-\tau_n^{\mathrm{fix}}\right)
C_n^{\mathrm A}[c_n]
-
D_n^{\mathrm{stop}}.
$$

$M_n\ge0$ 表示停机拷贝和固定协议能够在整槽内完成；其值越大，对关键更新预测误差和链路下降的容忍空间越大。

令 $\xi_n^{\mathrm{ack}}\in\{0,1\}$ 表示数据和状态应用完成后，确认报文是否在停机槽结束前成功往返；它是控制链路的随机实现，不是决策变量。协议采用单写者租约。冻结前只有源 UAV 可以提交结果；停机拷贝完成后，替补 UAV 载入状态并请求新的服务世代。若 $T_n^{\mathrm{proto}}\le\Delta$ 且 $\xi_n^{\mathrm{ack}}=1$，控制器在 $(c_n+1)\Delta$ 原子地推进服务世代和所有者，替补 UAV 从下一时隙获得唯一提交权，源 UAV 同时进入返航模式。若协议未在槽内完成或 $\xi_n^{\mathrm{ack}}=0$，服务世代不推进，替补 UAV 丢弃未提交副本，源 UAV 在 $\tau_n^{\mathrm{abort}}$ 内封存最后合法世代和失败记录、终止继续写入并执行中止返航。此时当前交接窗口进入吸收终止态，即源 UAV 和替补 UAV 均不再写入，所有迟到结果均被拒绝，窗口内也不再选择新方案。故障后的业务重建与新租约建立发生在当前窗口之外，不属于本文的状态、动作或可行性保证。

令 $P_u^{\mathrm{mode}}[t]$ 表示 UAV $u$ 的飞行、悬停和航电功率，单位为 W；源 UAV 在 $t=c_n$ 的整个停机槽仍使用停机前指定模式，从 $t=c_n+1$ 起才使用返航模式。$\kappa_u$ 为动态电压频率调整（dynamic voltage and frequency scaling，DVFS）下的计算能耗系数，单位为 $\mathrm{W}/(\mathrm{cycle}/\mathrm{s})^3$。对方案 $p$，$P_{unp}^{\mathrm A,\mathrm{data}}[t]$ 表示 UAV $u$ 作为事件 $n$ 的发送端或接收端时的数据无线功率，单位为 W，其中包含发射或接收电路功率。$E_{unp}^{\mathrm{A,fix}}$ 是冻结、状态应用、确认和控制交换在成功与失败两条分支共同采用的保守能耗上界；失败后的封存与返航切换另由 $E_n^{\mathrm{abort}}$ 预留。$E_{unp}^{\mathrm{A,fix,act}}[t]\le E_{unp}^{\mathrm{A,fix}}$ 表示实验中按实际分支测得的对应能耗，单位均为 J。定义选定事件的数据无线电开启时间

$$
\ell_n^{\mathrm{radio}}[t]
:=
\begin{cases}
\ell_n^{\mathrm A}[t],&s_n\le t<c_n,\\
\ell_n^{\mathrm{stop}},&t=c_n,\\
0,&\text{其他时隙}.
\end{cases}
$$

时隙能耗为

$$
\begin{aligned}
E_u^{\mathrm{use}}[t]
:={}&
\Delta P_u^{\mathrm{mode}}[t]
+
\kappa_u\Delta
\left(
\sum_{i:o_{r(i)}[t]=u}f_i[t]
\right)^3\\
&+
\sum_{n\in\mathcal N_\tau}
\sum_{p\in\mathcal P_n}
x_{np}\mathbb 1\{u\in\{u_n,v_{np}\}\}
\left(
\ell_n^{\mathrm{radio}}[t]
P_{unp}^{\mathrm A,\mathrm{data}}[t]
+
\mathbb 1\{t=c_{np}\}E_{unp}^{\mathrm{A,fix,act}}[t]
\right).
\end{aligned}
$$

若 $E_u[t]$ 为时隙开始时的剩余电量，$E_u^{\max}$ 为电池容量，二者单位均为 J，则

$$
E_u[t+1]=E_u[t]-E_u^{\mathrm{use}}[t].
$$

该递推使用实际无线开启时间与实际分支固定能耗；安全规划和未来证书则使用完整时隙数据无线功率与 $E_{unp}^{\mathrm{A,fix}}$，避免把保守预算误报为实际能耗指标。

时隙 $t$ 仍在空中的 UAV 集合记为 $\mathcal U^{\mathrm{air}}[t]$。从 UAV $u$ 当前状态沿安全航路到达可用补能点所需的实际能量为 $E_u^{\mathrm{ret}}[t]$，安全余量为 $E_u^{\mathrm{res}}$，二者单位均为 J。所有空中 UAV，而不只是源 UAV，都必须在每个时隙保留返航储备。对活动事件的源 UAV，另以 $E_n^{\mathrm{abort}}$ 表示确认失败后封存记录和进入返航模式的能量上界，单位为 J。

实际任务到达 $A_i[t]$、净关键更新 $W_n[t]$、信道 $h_{np}[t]$ 和返航能量 $E_u^{\mathrm{ret}}[t]$ 驱动真实状态与轨迹失败。在线规划只使用基于当前信息得到的到达上界 $\overline A_{i|t}[k]$、更新上界 $\overline W_{n|t}[k]$、信道下界 $\underline h_{np|t}[k]$ 和返航能量上界 $\overline E_{u|t}^{\mathrm{ret}}[k]$。这些规划边界是未来可行性屏蔽的输入，不与随机实现值混用；其分位风险按整条轨迹分配，并在独立实现值上校准和检验。

### E. 在线优化问题

以下优化问题只对 $\mathcal N_\tau\ne\varnothing$ 的交接窗口定义。窗口内的控制变量为

$$
\boldsymbol z_\tau
:=
\left(
\boldsymbol x_\tau,
\boldsymbol f_\tau,
\boldsymbol b_\tau
\right),
$$

其中 $\boldsymbol x_\tau=\{x_{np}\}$ 为一次性候选方案选择，$\boldsymbol f_\tau=\{f_i[t]\}$ 为逐时隙 CPU 分配，$\boldsymbol b_\tau=\{b_n[t]\}$ 为逐时隙 A2A 带宽。队列 $Q_i[t]$、欠同步工作量 $G_n[t]$、服务所有者 $o_r[t]$ 和电量 $E_u[t]$ 由实际输入和控制动作递推。

事件 $n$ 的归一化交接余量以窗口开始时的关键快照为参考：

$$
R_n
:=
\min\left\{1,\frac{M_n}{H_n[\tau]}\right\}.
$$

窗口内的平均归一化队列为

$$
\overline Q_\tau
:=
\frac{1}{|\mathcal W_\tau||\mathcal I|}
\sum_{t\in\mathcal W_\tau}
\sum_{i\in\mathcal I}
\frac{Q_i[t+1]}{Q_i^{\max}}.
$$

令 $\mathcal F_\tau^{\mathrm{traj}}$ 表示全部事件均在未主动中止的情况下满足 $T_n^{\mathrm{proto}}\le\Delta$、$\xi_n^{\mathrm{ack}}=1$ 并成功推进服务世代，且实际随机实现下的 C1–C4 在交接窗口内始终成立。其补事件是物理系统失败：实际确认失败、主动中止后仍未确认，或实际硬约束违约。候选匹配拒绝和证书为空本身不属于该补事件；只有它们导致主动中止时，才按“中止后未确认”计入。由于 $\mathcal N_\tau\ne\varnothing$，下式对事件集合取最小值有定义。给定无量纲服务质量权重 $\lambda_Q>0$，窗口效用定义为

$$
U_\tau
:=
\begin{cases}
\displaystyle
\min_{n\in\mathcal N_\tau}R_n
-\lambda_Q\overline Q_\tau,
&\mathcal F_\tau^{\mathrm{traj}}\text{ 成立},\\[2mm]
-1-\lambda_Q,
&\mathcal F_\tau^{\mathrm{traj}}\text{ 不成立}.
\end{cases}
$$

该目标同时奖励最紧张事件的同步余量并惩罚持续任务排队，避免把 CPU 压到只满足缓存上限。策略 $\pi$ 根据当期已经观测到的状态生成尚未执行的动作，优化问题为

$$
\max_{\pi}\quad \mathbb E_\pi[U_\tau]
$$

并满足实际随机轨迹上的失败概率约束

$$
\Pr_\pi\!\left(
(\mathcal F_\tau^{\mathrm{traj}})^{\mathrm c}
\right)
\le\varepsilon_F,
\qquad 0<\varepsilon_F<1.
$$

约束 C1 要求每个事件选择一个方案，且同一待命 UAV 在窗口内至多接管一个区域：

$$
\mathrm{C1}:\quad
\begin{cases}
\displaystyle
\sum_{p\in\mathcal P_n}x_{np}=1,
&\forall n,\\[2mm]
\displaystyle
\sum_n\sum_{p:v_{np}=u}x_{np}\le1,
&\forall u,\\
x_{np}\in\{0,1\},
&\forall n,p.
\end{cases}
$$

约束 C2 保证处理量、队列和 CPU 容量可行：

$$
\mathrm{C2}:\quad
\begin{cases}
0\le\mu_i[t]\le Q_i[t]+A_i[t],
&\forall i,t,\\
0\le Q_i[t+1]\le Q_i^{\max},
&\forall i,t,\\
\displaystyle
\sum_{i:o_{r(i)}[t]=u}f_i[t]\le F_u^{\max},
&\forall u,t,\\
0\le f_i[t]\le
d_{r(i)}[t]F_{o_{r(i)}[t]}^{\max},
&\forall i,t.
\end{cases}
$$

C2 的最后一行使停机槽 $d_{r(i)}[t]=0$ 时必有 $f_i[t]=0$；因此该槽的处理量、CPU 引起的 $W_n[t]$ 和计算能耗同时为零。

约束 C3 限制共享带宽、传输窗口、停机拷贝和离场时刻：

$$
\mathrm{C3}:\quad
\begin{cases}
\displaystyle
\sum_{n\in\mathcal N_\tau}b_n[t]\le B^{\mathrm A},
&\forall t,\\[1mm]
\displaystyle
0\le b_n[t]\le
B^{\mathrm A}
\sum_{p\in\mathcal P_n}
x_{np}\mathbb 1\{s_{np}\le t\le c_{np}\},
&\forall n,t,\\[1mm]
M_n\ge0,\qquad
\tau_n^{\mathrm{fix}}\le\Delta\le I_n^{\max},
&\forall n,\\[1mm]
T_n^{\mathrm{proto}}\le\Delta,
&\forall n,\\[1mm]
(c_n+1)\Delta\le d_n^{\mathrm{dep}},
&\forall n,\\[1mm]
(c_n+1)\Delta+\tau_n^{\mathrm{abort}}
\le d_n^{\mathrm{dep}},
&\forall n.
\end{cases}
$$

约束 C4 保证电池有效，并为所有空中 UAV 保留安全返航能力：

$$
\mathrm{C4}:\quad
\begin{cases}
0\le E_u[t+1]\le E_u^{\max},
&\forall u,t,\\[1mm]
E_u[t+1]\ge
E_u^{\mathrm{ret}}[t+1]+E_u^{\mathrm{res}},
&\forall u\in\mathcal U^{\mathrm{air}}[t+1],\\[1mm]
E_{u_n}[c_n+1]\ge
E_{u_n}^{\mathrm{ret}}[c_n+1]
+E_{u_n}^{\mathrm{res}}+E_n^{\mathrm{abort}},
&\forall n.
\end{cases}
$$

C4 的最后一行在停机时隙能耗扣除后检查最坏失败分支；成功分支只需常规返航储备。候选航路还必须保证替补 UAV 到达、接收状态和接管后的每个空中时隙满足 C4。

该问题包含一次性二元方案选择和逐时隙连续资源动作。CPU 同时影响任务队列、净关键更新和计算能耗；方案选择同时确定替补占用、预拷贝时长、停机时刻和离场余量；未来到达、应用写入、信道和返航能耗又使后续可行域随机变化。即使当前动作满足 C1–C4，仍可能因剩余替补不再可匹配或终端同步容量不足而进入空可行域。因此，问题的求解核心是保持终端可达性，而不是只对当前动作做惩罚或投影。

## IV. 匹配感知的未来可行性屏蔽调度

本节给出 MV-HPPO。该方法把标准混合动作策略作为未知环境下的决策器，把可核验的匹配与终端可达性条件作为下发动作前的屏蔽层。离散屏蔽回答“当前选择后，其余事件是否仍有替补”；连续屏蔽回答“当前资源动作后，离场前是否仍存在一条完成同步并安全返航的路径”。单时隙凸投影只负责当前物理约束，不再承担未来安全的含义。

### A. 状态、动作与随机边界

滚动窗口开始时，控制器已经获得事件集合 $\mathcal N_\tau$、候选集合 $\{\mathcal P_n\}$、各源 UAV 的最晚离场时刻以及候选航路。窗口内仍等待替补、正在预拷贝或等待停机的事件集合记为 $\mathcal A[t]$。候选方案 $p$ 的可用标志为 $\chi_{np}[t]\in\{0,1\}$，距预拷贝开始、暂停和最晚离场的剩余时间分别由 $s_{np}-t$、$c_{np}-t$ 和 $d_n^{\mathrm{dep}}-t\Delta$ 给出。

确认链路的有限样本不确定性先在离线校准层处理，不能与在线运行风险共用同一个 $\alpha$。在查看校准结果之前，冻结有限的候选类别与相对停机时刻分层

$$
\mathcal S_{\mathrm{ack}}
:=
\left\{
\sigma=(\ell,\kappa):
\ell\in\mathcal L_{\mathrm{ack}},\quad
\kappa\in\mathcal C_{\mathrm{ack}}
\right\},
\qquad
S_{\mathrm{ack}}:=|\mathcal S_{\mathrm{ack}}|<\infty,
$$

其中有限集合 $\mathcal L_{\mathrm{ack}}$ 给出预先定义的航路、控制链路和候选类别，$\mathcal C_{\mathrm{ack}}\subseteq\{1,\ldots,T_{\mathrm w}-1\}$ 给出相对停机槽 $\kappa=c-\tau$；二者都不允许在看到成败数据后重新切分。同一冻结分层内的校准轨迹按独立同分布的 Bernoulli 试验采集。一次试验只有在 $T_n^{\mathrm{proto}}\le\Delta$ 且完整经历了 ACK 请求与响应的观测机会、因而没有右删失时才是合格 ACK 试验；成功量为 $\xi^{\mathrm{ack}}=1$。令 $N_\sigma$ 和 $X_\sigma$ 分别为分层 $\sigma$ 的合格试验数和成功数，预先固定最小样本数 $N_{\min}^{\mathrm{ack}}$ 与总校准错误概率 $\beta_{\mathrm{cal}}\in(0,1)$。当 $N_\sigma\ge N_{\min}^{\mathrm{ack}}$ 时，采用单侧 Clopper–Pearson 下置信界

$$
\underline p_{\sigma}^{\mathrm{ack}}
:=
\begin{cases}
\mathrm{Beta}^{-1}\!\left(
\dfrac{\beta_{\mathrm{cal}}}{S_{\mathrm{ack}}};
X_\sigma,N_\sigma-X_\sigma+1
\right),&X_\sigma>0,\\[3mm]
0,&X_\sigma=0,
\end{cases}
$$

其中 $\mathrm{Beta}^{-1}(q;a,b)$ 是 Beta 分布的 $q$ 分位数。Bonferroni 校正给出

$$
\Pr_{\mathrm{cal}}\!\left(
p_\sigma^{\mathrm{ack}}
\ge \underline p_\sigma^{\mathrm{ack}},
\ \forall\sigma\in\mathcal S_{\mathrm{ack}}
\text{ 且 }N_\sigma\ge N_{\min}^{\mathrm{ack}}
\right)
\ge1-\beta_{\mathrm{cal}}.
$$

候选 $(n,p,c_{np})$ 映射到其预注册分层后，记对应下界为 $\underline p_{np|t}^{\mathrm{ack}}[c_{np}]$。样本不足的分层标为“不可认证”，其候选从认证规划器中排除；这只是证据不足，不是结构不可行或自然不可行。若当前事件的全部候选都不可认证，则认证规划器不可用；任何经验成功率回退必须作为不带本文风险声明的独立运行模式报告。另以 $\alpha_{\mathrm{rem}}[t]$ 表示窗口在动作前尚未花费的运行风险预算，其初始化与递推在下文给出。

令 $K_h$ 为固定历史长度，并令 $\boldsymbol\omega_n[t]$ 收集到 $t-1$ 为止最近 $K_h$ 个已经封存并观测到的 $W_n$；历史不足时在左侧补零。控制器在时隙 $t$ 的动作前状态写为

$$
\begin{aligned}
\boldsymbol s[t]
:=\bigl(&
\{Q_i[t],A_i[t],c_i,Q_i^{\max},
\overline A_{i|t}[k]\}_{i,k},\\
&
\{E_u[t],o_r[t],P_u^{\mathrm{mode}}[k],
\overline E_{u|t}^{\mathrm{ret}}[k]\}_{u,r,k},\\
&
\{H_n[\tau],G_n[t],\boldsymbol\omega_n[t],
d_n^{\mathrm{dep}},\mathcal P_n,\chi_{np}[t],
h_{np}[t],\overline W_{n|t}^{\mathrm{bg}}[k],
\overline\eta_{ni|t}[k],
\underline h_{np|t}[k]\}_{n,p,i,k},\\
&
\{\underline p_{np|t}^{\mathrm{ack}}[c_{np}]\}_{n,p},\\
&
\text{已占用替补集合},
\text{协议阶段},\ \alpha_{\mathrm{rem}}[t],\ t
\bigr).
\end{aligned}
$$

尚未开始预拷贝的事件不使用 $G_n[t]$，而使用 $H_n[\tau]+\sum_{k=\tau}^{t-1}W_n[k]$ 表示当前待同步工作量；已经开始预拷贝的事件使用 $G_n[t]$。当前槽的 $A_i[t]$ 与 $h_{np}[t]$ 已观测，约定 $\overline A_{i|t}[t]:=A_i[t]$ 和 $\underline h_{np|t}[t]:=h_{np}[t]$，只有 $k\ge t+1$ 才使用随机到达与信道边界；当前槽的 $W_n[t]$ 尚未生成，绝不进入动作前状态，策略只能使用 $\boldsymbol\omega_n[t]$、写入预测参数与统一上界。未来 $P_u^{\mathrm{mode}}[k]$ 由候选航路、停机槽保持和槽末返航切换规则确定，不是对随机未来的偷看。连续状态在输入网络前除以相应容量、时间或初始快照进行归一化，UAV 和区域编号通过嵌入向量编码。

实际随机过程与规划边界分开维护。首先在窗口开始时为每个事件一次性分配运行期确认失败份额 $\alpha_n^{\mathrm{ack}}\ge0$；该份额在后续时隙不重算、不回收，也不等于校准置信参数 $\beta_{\mathrm{cal}}$。记

$$
\alpha_{\mathrm{ack}}^{\mathrm{win}}
:=\sum_{n\in\mathcal N_\tau}\alpha_n^{\mathrm{ack}},
\qquad
\alpha_{\mathrm{rem}}[\tau]
:=\alpha_{\mathrm{sh}}-\alpha_{\mathrm{ack}}^{\mathrm{win}},
\qquad
0<\alpha_{\mathrm{sh}}<\varepsilon_F.
$$

认证候选必须满足 $\underline p_{np|\tau}^{\mathrm{ack}}[c_{np}]\ge1-\alpha_n^{\mathrm{ack}}$。若 $\alpha_{\mathrm{rem}}[\tau]\le0$，则窗口没有可供预测边界使用的运行风险，认证规划器不可用并执行保守中止；这仍是认证能力不足，不称为自然物理不可行。

预测边界采用预先冻结的几何 alpha-spending 计划。给定 $\rho\in(0,1)$，令

$$
w_t:=
\frac{(1-\rho)\rho^{t-\tau}}
{1-\rho^{T_{\mathrm w}}},
\qquad
\delta_t:=w_t\alpha_{\mathrm{rem}}[\tau]
\le\alpha_{\mathrm{rem}}[t],
\qquad
t\in\mathcal W_\tau,
$$

故 $\sum_{t\in\mathcal W_\tau}\delta_t=\alpha_{\mathrm{rem}}[\tau]$。时隙 $t$ 的所有候选检查、初始证书或恢复证书共享同一组新边界及同一个 $\delta_t$，不能因重求解、回溯或更换候选而重置风险。令 $\mathcal B_t^{\mathrm{new}}$ 为本次证书首次使用的到达、更新、信道和返航边界索引集合，非负份额满足

$$
\sum_{(i,k)\in\mathcal B_t^{A}}\alpha_{i,k|t}^{A}
+\sum_{(n,k)\in\mathcal B_t^{W}}\alpha_{n,k|t}^{W}
+\sum_{(n,p,k)\in\mathcal B_t^{h}}\alpha_{np,k|t}^{h}
+\sum_{(u,k)\in\mathcal B_t^{E}}\alpha_{u,k|t}^{E}
\le\delta_t,
$$

其中四个索引集构成 $\mathcal B_t^{\mathrm{new}}$。执行本槽唯一的首个动作后，无论实际边界是否紧约束，都更新

$$
\alpha_{\mathrm{rem}}[t+1]
=\alpha_{\mathrm{rem}}[t]-\delta_t.
$$

因此风险不会随滚动重规划重复使用；若 $\delta_t>\alpha_{\mathrm{rem}}[t]$ 或剩余预算已经耗尽，控制器不得继续出具认证证书，只能记录认证不可用并保守中止。

给定当前历史 $\mathcal H_t$，规划边界满足

$$
\Pr\!\left(
A_i[k]\le\overline A_{i|t}[k]
\mid\mathcal H_t
\right)\ge1-\alpha_{i,k|t}^{A},
$$

$$
\Pr\!\left(
\forall\boldsymbol f\in\mathcal F_k^{\mathrm{adm}}:
W_n[k](\boldsymbol f)
\le\overline W_{n|t}[k](\boldsymbol f)
\mid\mathcal H_t
\right)\ge1-\alpha_{n,k|t}^{W},
$$

其中 $\mathcal F_k^{\mathrm{adm}}$ 是在生成边界前冻结的 C2 可容许 CPU 集。该同时界对证书随后选择的任意 $\boldsymbol f^{\mathrm{cert}}[k]$ 都有效；只对某个给定动作成立的点态条件分位数不足以支持“先预测、后优化动作”的证书。若实际系统不能校准这一统一上界，则必须改成先固定动作、再用与该动作条件有效的新数据出具边界，且仍消耗本槽同一个 $\delta_t$。

$$
\Pr\!\left(
h_{np}[k]\ge\underline h_{np|t}[k]
\mid\mathcal H_t
\right)\ge1-\alpha_{np,k|t}^{h},
$$

$$
\Pr\!\left(
E_u^{\mathrm{ret}}[k]\le
\overline E_{u|t}^{\mathrm{ret}}[k]
\mid\mathcal H_t
\right)\ge1-\alpha_{u,k|t}^{E}.
$$

运行期确认事件只在 $\tau$ 分配一次风险，并须满足

$$
p_{\sigma(n,p,c_{np})}^{\mathrm{ack}}
\ge
\underline p_{np|\tau}^{\mathrm{ack}}[c_{np}]
\ge1-\alpha_n^{\mathrm{ack}}.
$$

确认丢包是动作不可控制的外生故障，不能只靠拉格朗日乘子事后观察。以至少 $1-\beta_{\mathrm{cal}}$ 的校准置信度，上述所有可认证 ACK 分层的真实成功率同时不低于其下界；在该校准事件和各预测边界覆盖声明成立的条件下，Boole 并集界保证本窗口已经分配的 ACK 失败与新边界失效的运行概率之和不超过 $\alpha_{\mathrm{sh}}$，不要求各随机量相互独立。该结论不覆盖模型遗漏、实现错误或不可认证的经验回退模式；预测边界仍须在独立轨迹上检验，不能用每个时隙重新开始的一组分位数推断整轨迹风险。

原始策略动作由离散与连续两部分组成：

$$
\widetilde{\boldsymbol a}[t]
:=
\left(
\boldsymbol a^{\mathrm d}[t],
\widetilde{\boldsymbol a}^{\mathrm c}[t]
\right).
$$

在 $t=\tau$ 时，离散动作依次为各事件选择候选方案，由此确定替补 UAV、预拷贝开始时隙和暂停时隙；在 $t>\tau$ 时离散动作为空。原始连续动作给出 CPU 和 A2A 带宽比例。屏蔽层将其映射为执行动作

$$
\boldsymbol a[t]
=
\left(
\boldsymbol a^{\mathrm d}[t],
\{f_i[t]\},
\{b_n[t]\}
\right).
$$

本文假设实际到达、动作后关键更新、信道和飞行模式的下一时隙分布在给定 $\boldsymbol s[t]$ 与执行动作后与更早历史条件独立。特别地，$W_n[t]$ 在执行 $f_i[t]$ 后才实现并进入下一状态。若实测轨迹表现出更长记忆，则增加 $K_h$ 或改用注意力编码已经观测的历史，而不把动作后信息提前送入策略。

每个非空交接窗口构成一个训练回合。回合终端回报取第 III-E 节的 $U_\tau$，并用势函数

$$
\Phi(\boldsymbol s[t])
:=
-
\max_{n\in\mathcal A[t]}
\frac{Y_n[t]}{H_n[\tau]}
-
\frac{\lambda_\Phi}{|\mathcal I|}
\sum_i\frac{Q_i[t]}{Q_i^{\max}}
$$

进行训练塑形，其中

$$
Y_n[t]
:=
\begin{cases}
H_n[\tau]+\sum_{k=\tau}^{t-1}W_n[k],
&t\le s_n,\\
G_n[t],
&s_n<t\le c_n.
\end{cases}
$$

其中无量纲权重 $\lambda_\Phi\ge0$ 只控制训练塑形中队列项的相对强度。活动事件为空时势函数第一项取零，正常结束与失败终止状态的势函数均置零。令物理失败指示量 $g[t]$ 只在回合首次发生实际确认失败、主动中止导致未确认或实际 C1–C4 违约时取 1，其余时隙取 0。另以 $g^{\mathrm{match}}[t]$、$g^{\mathrm{cert}}[t]$ 和 $g^{\mathrm{trunc}}[t]$ 分别记录候选被匹配检查拒绝、完整组合证书为空和在线搜索被时限截断；这些方法诊断不直接进入 $g[t]$。若候选耗尽或搜索截断最终触发中止，$g[t]$ 因“中止后未确认”取 1。因为每个回合至多记录一次物理失败，

$$
\mathbb E_\pi\!\left[\sum_tg[t]\right]
=
\Pr_\pi\!\left(
(\mathcal F_\tau^{\mathrm{traj}})^{\mathrm c}
\right).
$$

策略学习使用的回报为终端效用、势函数差和失败拉格朗日代价之和，其中 $\gamma\in(0,1]$ 为回报折扣因子。本文取 $\gamma=1$，此时势函数差望远镜相消，不改变包含真实平均队列的原目标。

### B. 匹配感知的离散方案屏蔽

候选方案首先通过单事件终端必要性检查。对事件 $n$ 和方案 $p$，控制器用当前队列及未来到达上界计算维持队列不溢出所需的最小处理量。当前非停机时隙的最小 CPU 为

$$
f_i^{\min}[t]
:=
\frac{c_i}{\Delta}
\left[
Q_i[t]+A_i[t]-Q_i^{\max}
\right]^+,
$$

若区域在时隙 $t$ 停机，则要求 $Q_i[t]+A_i[t]\le Q_i^{\max}$，否则该方案当期不可行。任一 UAV 上的 $\sum_i f_i^{\min}[t]$ 还必须不超过其 $F_u^{\max}$。未来时隙用到达上界递推相同规则。对候选 $p$，令 $d_{np}[k]:=\mathbb 1\{k\ne c_{np}\}$。将最小 CPU 轨迹代入应用写入模型，得到仍需满足队列服务时的关键更新上界

$$
\overline W_{n|t}^{\min,p}[k]
:=
d_{np}[k]
\left(
\overline W_{n|t}^{\mathrm{bg}}[k]
+
\sum_{i\in\mathcal I_{r_n}}
\overline\eta_{ni|t}[k]
\frac{f_i^{\min}[k]\Delta}{c_i}
\right).
$$

其中 $\overline W_{n|t}^{\mathrm{bg}}[k]$ 是背景关键更新上界，$\overline\eta_{ni|t}[k]$ 是写入放大系数上界，二者均由当前历史下的校准模型给出。该量不是说较小 CPU 一定产生确定的最小更新，而是用经校准的写入系数上界评估“为维持服务质量至少要处理这些任务时，最多需要同步多少净更新”。

对方案 $p$，使用风险分配后的信道下界计算独占全部 A2A 带宽时的保守最大速率：

$$
\underline C_{np|t}^{\max}[k]
:=
B^{\mathrm A}\log_2\left(
1+\frac{P_{np}^{\mathrm A}\underline h_{np|t}[k]}
{N_0B^{\mathrm A}}
\right).
$$

候选只有同时满足以下必要条件才保留：替补当前可用并可按时到达；$\tau_n^{\mathrm{fix}}\le\Delta\le I_n^{\max}$；按“A2A 仅服务槽首欠账、并行 CPU 产生的 $W$ 在槽末加入”的逐槽递推计算时，最小 CPU 下的关键工作量能够被后续预拷贝与停机槽容量覆盖；确认成功率下界满足 $\underline p_{np|\tau}^{\mathrm{ack}}[c_{np}]\ge1-\alpha_n^{\mathrm{ack}}$；源 UAV 能在 $(c_{np}+1)\Delta$ 切换返航模式，且中止分支能在 $d_n^{\mathrm{dep}}$ 前结束；源、替补以及其他受该方案影响的空中 UAV 均保留返航储备。该检查不能把本槽末产生的 $W$ 计入本槽传输容量，也不能用总字节除以总容量替代逐槽因果递推。它只使用单事件独占资源条件，因此是必要条件，不声称已经解决多事件共享带宽。

单事件检查后，离散屏蔽还要保护剩余事件的替补匹配。令 $K_\tau:=|\mathcal N_\tau|$，并把事件按最晚离场时刻从早到晚排列为 $n_1,\ldots,n_{K_\tau}$。在为 $n_j$ 暂定方案 $p$ 后，从剩余未分配事件和未占用待命 UAV 构造二分图

$$
\mathcal G_j=(\mathcal N_j^{\mathrm{rem}},
\mathcal U_j^{\mathrm{rem}},\mathcal E_j).
$$

若某个剩余事件至少有一个指向待命 UAV $u$ 的方案通过上述单事件检查，则在 $\mathcal E_j$ 中加入对应边。只有当 $\mathcal G_j$ 的最大匹配覆盖全部 $\mathcal N_j^{\mathrm{rem}}$ 时，当前暂定方案才保留在掩码中。该规则检查 Hall 条件的算法等价形式，防止较早事件占用后续事件唯一可用的替补。

令 $m_{n_jp}^{(j)}[\tau]\in\{0,1\}$ 表示经过单事件与剩余匹配检查后的掩码，离散策略给候选输出分数 $z_{n_jp}^{(j)}$，则

$$
\pi_{\theta_{\mathrm d}}
\left(
p\mid\boldsymbol s[\tau],
p_{n_1:j-1}
\right)
:=
\frac{
m_{n_jp}^{(j)}
\exp(z_{n_jp}^{(j)})
}{
\sum_{p'\in\mathcal P_{n_j}}
m_{n_jp'}^{(j)}
\exp(z_{n_jp'}^{(j)})
}.
$$

每次选择后更新占用关系并重新构图。若某一步掩码全零，当前部分组合被拒绝并回溯到上一个仍有备选方案的事件，同时记录 $g^{\mathrm{match}}[\tau]$；掩码拒绝本身不是物理失败。记 $\boldsymbol m[\tau]$ 为本次顺序选择中全部掩码的集合；在 $t>\tau$ 时离散动作及其掩码均为空。

最大匹配只保证替补排他，不能保证并发事件共享带宽和能量后仍可行。记窗口末槽为 $T_\tau^{\mathrm{end}}:=\tau+T_{\mathrm w}-1$。每得到一个完整候选组合 $\boldsymbol x_\tau$，控制器都必须检查初始状态证书 $\mathcal V_\tau(\boldsymbol x_\tau)$。这里直接定义 $\mathcal V_\tau$ 为满足以下条件的窗口初始状态集合：存在与当前动作投影变量无关的 $\{Q_i^{\mathrm{cert}}[k],G_n^{\mathrm{cert}}[k],f_i^{\mathrm{cert}}[k],b_n^{\mathrm{cert}}[k]\}$，满足第 IV-C 节给出的队列、因果 A2A、停机、协议和能量前缀约束，并以

$$
Q_i^{\mathrm{cert}}[\tau]=Q_i[\tau],
$$

以及

$$
G_n^{\mathrm{cert}}[s_n]
=H_n[\tau]
+\sum_{k=\tau}^{s_n-1}
\overline W_{n|\tau}^{\mathrm{cert}}[k]
\bigl(\boldsymbol f^{\mathrm{cert}}[k]\bigr)
$$

为初始锚点；$s_n=\tau$ 时后一个和为空，$b_n^{\mathrm{cert}}[k]=0$ 对所有 $k=\tau,\ldots,s_n-1$ 成立，因果 A2A epigraph 只对 $k=s_n,\ldots,c_n-1$ 施加。为统一初始与滚动证书，对任一证书起点 $r\in\mathcal W_\tau$ 定义单槽凸能耗上界

$$
\begin{aligned}
\overline E_{u|r}^{\mathrm{use,cert}}[k]
:={}&
\Delta P_u^{\mathrm{mode}}[k]
+\kappa_u\Delta
\left(
\sum_{i:o_{r(i)}[k]=u}f_i^{\mathrm{cert}}[k]
\right)^3\\
&+\sum_{n,p}x_{np}
\mathbb 1\{u\in\{u_n,v_{np}\}\}
\left(
\mathbb 1\{s_{np}\le k\le c_{np}\}
\Delta P_{unp}^{\mathrm A,\mathrm{data}}[k]
+\mathbb 1\{k=c_{np}\}E_{unp}^{\mathrm{A,fix}}
\right).
\end{aligned}
$$

该上界把活动数据链路按完整时隙计量，并在成功与失败分支都采用固定协议能耗上界。初始证书的 CPU 与带宽索引从 $k=\tau$ 开始，能量前缀直接写为

$$
\sum_{k=\tau}^{q}
\overline E_{u|\tau}^{\mathrm{use,cert}}[k]
\le
E_u[\tau]
-\overline E_{u|\tau}^{\mathrm{ret}}[q+1]
-E_u^{\mathrm{res}},
\quad
q=\tau,\ldots,T_\tau^{\mathrm{end}},
$$

并对每个活动源 UAV 要求

$$
\sum_{k=\tau}^{c_n}
\overline E_{u_n|\tau}^{\mathrm{use,cert}}[k]
\le
E_{u_n}[\tau]
-\overline E_{u_n|\tau}^{\mathrm{ret}}[c_n+1]
-E_{u_n}^{\mathrm{res}}
-E_n^{\mathrm{abort}}.
$$

其余队列、CPU、共享带宽、停机和协议不等式使用第 IV-C 节显式给出的同一组证书式，并把起始索引替换为 $\tau$。也就是说，$\mathcal V_\tau$ 不是只检查匹配的别名，而是从实际窗口初态出发、包含首槽动作的完整确定性证书。

为使回溯结论可核验，先对通过单事件和 Hall 必要条件的完整叶节点集合 $\mathcal L_\tau$ 冻结一个全序 $\prec$；该全序由候选分数、最晚离场时刻和固定编号破除并列。搜索维护已访问叶集合 $\mathcal L_\tau^{\mathrm{vis}}$ 和尚未访问的有序前沿 $\mathcal L_\tau^{\mathrm{front}}$，并保持完备不变量

$$
\mathcal L_\tau^{\mathrm{vis}}
\cap\mathcal L_\tau^{\mathrm{front}}=\varnothing,
\qquad
\mathcal L_\tau^{\mathrm{vis}}
\cup\mathcal L_\tau^{\mathrm{front}}=\mathcal L_\tau.
$$

每个完整组合第一次从前沿取出时立即加入 $\mathcal L_\tau^{\mathrm{vis}}$，并且只求解一次 $\mathcal V_\tau$；证书为空则记录 $g^{\mathrm{cert}}[\tau]$，非空则提交并停止。beam 只把前沿中的若干叶并行求解和排序，不删除任何未访问叶，也不改变 $\prec$ 下的完备性。若未触发时限，算法最终满足：要么找到首个可认证叶，要么 $\mathcal L_\tau^{\mathrm{vis}}=\mathcal L_\tau$，从而所有通过必要条件的完整组合都恰好检查一次；被提前剪枝的分支则已有单事件不可行或 Hall 不成立的必要性证据。只有后一种穷尽状态才因规划边界下结构不可行而主动中止。若在线时限先耗尽，则单独记录 $g^{\mathrm{trunc}}[\tau]$ 并执行超时中止，不能宣称候选已经不可行。两类中止造成的物理失败都按“中止后未确认”统计。

### C. 连续动作的未来可行性屏蔽

方案选定后，条件连续策略通过 Beta 分布输出 $[0,1]$ 内的 CPU 与带宽比例，并映射为原始动作 $\widetilde{\boldsymbol f}[t]$ 和 $\widetilde{\boldsymbol b}[t]$。给定无量纲距离权重 $\lambda_b>0$，原始动作先经过局部投影，只修正当前时隙的处理量、队列、CPU、共享带宽和电池上下界：

$$
\begin{aligned}
\widehat{\boldsymbol a}^{\mathrm c}[t]
=
\arg\min_{\boldsymbol f,\boldsymbol b}\quad&
\sum_i
\left(
\frac{f_i-\widetilde f_i}{F_{o_{r(i)}[t]}^{\max}}
\right)^2
+
\lambda_b\sum_n
\left(
\frac{b_n-\widetilde b_n}{B^{\mathrm A}}
\right)^2\\
\mathrm{s.t.}\quad&
(\boldsymbol f,\boldsymbol b)
\in\mathcal F_t^{\mathrm{local}}
(\boldsymbol x_\tau).
\end{aligned}
$$

$\mathcal F_t^{\mathrm{local}}$ 包含当前 C2、当前电池和到达暂停时隙事件的实际停机条件，也显式包含当前 C3 的共享总带宽与传输窗口门控：

$$
\sum_{n\in\mathcal N_\tau}b_n[t]\le B^{\mathrm A},
\qquad
0\le b_n[t]
\le B^{\mathrm A}\mathbb 1\{s_n\le t\le c_n\},
\quad\forall n.
$$

为保持局部子问题凸性，电池条件对当前活动数据链路使用完整时隙无线能耗上界。对任意正在检查的当前动作 $(\boldsymbol f^0[t],\boldsymbol b^0[t])$，定义

$$
\begin{aligned}
\overline E_{u|t}^{\mathrm{use},0}
\bigl(\boldsymbol f^0[t],\boldsymbol b^0[t]\bigr)
:={}&
\Delta P_u^{\mathrm{mode}}[t]
+\kappa_u\Delta
\left(
\sum_{i:o_{r(i)}[t]=u}f_i^0[t]
\right)^3\\
&+\sum_{n,p}x_{np}
\mathbb 1\{u\in\{u_n,v_{np}\}\}
\left(
\mathbb 1\{s_{np}\le t\le c_{np}\}
\Delta P_{unp}^{\mathrm A,\mathrm{data}}[t]
+\mathbb 1\{t=c_{np}\}E_{unp}^{\mathrm{A,fix}}
\right).
\end{aligned}
$$

完整时隙无线项在数值上只由窗口门控决定，$\boldsymbol b^0[t]$ 通过上述 C3 约束进入可行域；这种保守写法避免引入非凸的无线电开关。在局部投影中取 $\boldsymbol f^0[t]=\boldsymbol f$、$\boldsymbol b^0[t]=\boldsymbol b$，$\mathcal F_t^{\mathrm{local}}$ 直接施加凸能量不等式

$$
\overline E_{u|t}^{\mathrm{use},0}
\bigl(\boldsymbol f^0[t],\boldsymbol b^0[t]\bigr)
\le
E_u[t]
-\overline E_{u|t}^{\mathrm{ret}}[t+1]
-E_u^{\mathrm{res}}
-\sum_{n:u_n=u}\mathbb 1\{t=c_n\}E_n^{\mathrm{abort}},
\qquad\forall u.
$$

局部投影求解完成后，动作已经固定，此时才数值计算

$$
E_u^{\mathrm{pred}}[t+1]
:=E_u[t]
-\overline E_{u|t}^{\mathrm{use},0}
\bigl(\widehat{\boldsymbol f}[t],
\widehat{\boldsymbol b}[t]\bigr).
$$

动作执行后的真实电量仍按 $\ell_n^{\mathrm{radio}}[t]$ 更新。局部投影不能证明未来可行；固定动作的未来能量证书从 $t+1$ 开始，因而既不漏计也不重复计算当前槽。

随后先检查已经固定的局部投影动作。记 $\boldsymbol f^{\mathrm{fix}}[t]:=\widehat{\boldsymbol f}[t]$、$\boldsymbol b^{\mathrm{fix}}[t]:=\widehat{\boldsymbol b}[t]$；此时可以按第 III 节因果递推数值计算 $Q_i^{\mathrm{pred}}[t+1]$、$G_n^{\mathrm{pred}}[t+1]$ 和 $E_u^{\mathrm{pred}}[t+1]$，其中尚未实现的本槽 $W_n[t]$ 使用时隙 $t$ 已分配的统一上界。沿用窗口末槽 $T_\tau^{\mathrm{end}}$，固定动作的未来证书声明与当前帽变量相互独立的变量

$$
\begin{aligned}
\mathcal Z_{t+1}^{\mathrm{cert}}
:=\bigl\{&
Q_i^{\mathrm{cert}}[k]
\bigr\}_{\substack{i\in\mathcal I,\\
k=t+1,\ldots,T_\tau^{\mathrm{end}}+1}}
\cup
\bigl\{
f_i^{\mathrm{cert}}[k]
\bigr\}_{\substack{i\in\mathcal I,\\
k=t+1,\ldots,T_\tau^{\mathrm{end}}}}\\
&\cup
\bigl\{
b_n^{\mathrm{cert}}[k]
\bigr\}_{\substack{n\in\mathcal A[t+1],\\
k=t+1,\ldots,T_\tau^{\mathrm{end}}}}
\cup
\bigl\{
G_n^{\mathrm{cert}}[k]
\bigr\}_{\substack{n\in\mathcal A[t+1],\\
k=\max\{s_n,t+1\},\ldots,c_n}}.
\end{aligned}
$$

定义 $\mathcal V_{t+1}(\boldsymbol x_\tau)$ 为存在 $\mathcal Z_{t+1}^{\mathrm{cert}}$ 满足下述约束的所有一步预测状态。队列首先锚定于当前动作产生的下一状态：

$$
Q_i^{\mathrm{cert}}[t+1]
=Q_i^{\mathrm{pred}}[t+1],
\qquad \forall i.
$$

对 $k=t+1,\ldots,T_\tau^{\mathrm{end}}$，队列证书满足

$$
\begin{aligned}
0\le Q_i^{\mathrm{cert}}[k+1]&\le Q_i^{\max},\\
Q_i^{\mathrm{cert}}[k+1]
&\ge
Q_i^{\mathrm{cert}}[k]
+\overline A_{i|t}[k]
-\frac{d_{r(i)}[k]f_i^{\mathrm{cert}}[k]\Delta}{c_i},\\
0\le\frac{d_{r(i)}[k]f_i^{\mathrm{cert}}[k]\Delta}{c_i}
&\le Q_i^{\mathrm{cert}}[k]+\overline A_{i|t}[k],\\
0\le f_i^{\mathrm{cert}}[k]
&\le d_{r(i)}[k]F_{o_{r(i)}[k]}^{\max},\\
\sum_{i:o_{r(i)}[k]=u}f_i^{\mathrm{cert}}[k]
&\le F_u^{\max},\qquad\forall u.
\end{aligned}
$$

其中停机槽的 $d_{r(i)}[k]=0$ 保证 CPU 为零。候选检查中的 $\overline W_{n|t}^{\min,p}[k]$ 只对应最小 CPU；证书允许重新选择未来 CPU，因此定义动作一致的统一上界

$$
\overline W_{n|t}^{\mathrm{cert}}[k]
\bigl(\boldsymbol f^{\mathrm{cert}}[k]\bigr)
:=
d_{r_n}[k]
\left(
\overline W_{n|t}^{\mathrm{bg}}[k]
+\sum_{i\in\mathcal I_{r_n}}
\overline\eta_{ni|t}[k]
\frac{f_i^{\mathrm{cert}}[k]\Delta}{c_i}
\right).
$$

对已经选定的方案 $p_n$，规划信道下界对应的证书速率为

$$
\underline C_{n|t}^{\mathrm{A,cert}}
\bigl(b_n^{\mathrm{cert}}[k]\bigr)
:=
b_n^{\mathrm{cert}}[k]\log_2\left(
1+\frac{P_{np_n}^{\mathrm A}\underline h_{np_n|t}[k]}
{N_0b_n^{\mathrm{cert}}[k]}
\right),
$$

并在 $b_n^{\mathrm{cert}}[k]=0$ 时按连续延拓取零。

欠同步状态必须从实际或一步预测状态接续，不能由求解器自由选择。若 $s_n\le t<c_n$，预拷贝已经开始，锚点为

$$
G_n^{\mathrm{cert}}[t+1]
=G_n^{\mathrm{pred}}[t+1].
$$

若 $t<s_n$，预拷贝尚未开始。定义动作下发前可用的一步累计上界

$$
Y_n^{\mathrm{pred}}[t+1]
:=
H_n[\tau]
+\sum_{j=\tau}^{t-1}W_n[j]
+\overline W_{n|t}^{\mathrm{cert}}[t]
\bigl(\boldsymbol f^{\mathrm{fix}}[t]\bigr),
$$

其中求和项均为已经观测并封存的记录；最后一项只覆盖尚未实现的当前槽，动作执行后由观测到的 $W_n[t]$ 替换。此时预拷贝开始状态锚定为

$$
G_n^{\mathrm{cert}}[s_n]
=Y_n^{\mathrm{pred}}[t+1]
+\sum_{k=t+1}^{s_n-1}
\overline W_{n|t}^{\mathrm{cert}}[k]
\bigl(\boldsymbol f^{\mathrm{cert}}[k]\bigr),
$$

其中 $s_n=t+1$ 时求和为空，并显式要求

$$
b_n^{\mathrm{cert}}[k]=0,
\qquad k=t+1,\ldots,s_n-1.
$$

因此 $s_n$ 之前没有 A2A。只有对

$$
k=\max\{s_n,t+1\},\ldots,c_n-1
$$

才施加因果 epigraph：

$$
G_n^{\mathrm{cert}}[k+1]
\ge
\overline W_{n|t}^{\mathrm{cert}}[k]
\bigl(\boldsymbol f^{\mathrm{cert}}[k]\bigr),
$$

$$
G_n^{\mathrm{cert}}[k+1]
\ge
G_n^{\mathrm{cert}}[k]
+\overline W_{n|t}^{\mathrm{cert}}[k]
\bigl(\boldsymbol f^{\mathrm{cert}}[k]\bigr)
-\underline C_{n|t}^{\mathrm{A,cert}}
\bigl(b_n^{\mathrm{cert}}[k]\bigr)\Delta.
$$

对 $k=t+1,\ldots,T_\tau^{\mathrm{end}}$，带宽变量还满足

$$
\sum_{n\in\mathcal A[t+1]}b_n^{\mathrm{cert}}[k]
\le B^{\mathrm A},
\qquad
0\le b_n^{\mathrm{cert}}[k]
\le B^{\mathrm A}\mathbb 1\{s_n\le k\le c_n\}.
$$

对每个 $n\in\mathcal A[t+1]$，整槽停机容量与协议条件为

$$
G_n^{\mathrm{cert}}[c_n]+D_n^{\mathrm{meta}}
\le
\left(\Delta-\tau_n^{\mathrm{fix}}\right)
\underline C_{n|t}^{\mathrm{A,cert}}
\bigl(b_n^{\mathrm{cert}}[c_n]\bigr),
$$

$$
\tau_n^{\mathrm{fix}}\le\Delta\le I_n^{\max},
\qquad
(c_n+1)\Delta+\tau_n^{\mathrm{abort}}
\le d_n^{\mathrm{dep}},
$$

并要求窗口开始时已经认证的 $\underline p_{np_n|\tau}^{\mathrm{ack}}[c_n]\ge1-\alpha_n^{\mathrm{ack}}$。这里停机容量只使用槽首欠同步量 $G_n^{\mathrm{cert}}[c_n]$；停机槽 CPU 为零，不会生成可偷用本槽容量的新 $W_n[c_n]$。

未来证书沿用上述单槽凸能耗上界。当前动作已经形成 $E_u^{\mathrm{pred}}[t+1]$，所以对每架空中 UAV $u$ 和每个未来前缀终点 $q$，证书要求

$$
\sum_{k=t+1}^{q}
\overline E_{u|t}^{\mathrm{use,cert}}[k]
\le
E_u^{\mathrm{pred}}[t+1]
-\overline E_{u|t}^{\mathrm{ret}}[q+1]
-E_u^{\mathrm{res}},
\qquad
q\in\mathcal W_\tau,\ q\ge t+1,
\quad u\in\mathcal U^{\mathrm{air}}[q+1].
$$

通用前缀在 $q=c_n$ 时给出成功分支的返航储备。对满足 $c_n\ge t+1$ 的活动源 UAV $u_n$，失败分支还要求

$$
\sum_{k=t+1}^{c_n}
\overline E_{u_n|t}^{\mathrm{use,cert}}[k]
\le
E_{u_n}^{\mathrm{pred}}[t+1]
-\overline E_{u_n|t}^{\mathrm{ret}}[c_n+1]
-E_{u_n}^{\mathrm{res}}
-E_n^{\mathrm{abort}}.
$$

因此成功与中止分支都在槽末 $c_n+1$ 的同一返航边界上检查；若当前槽本身就是停机槽，则其失败储备已经由上面的一步预测式检查，不再进入未来和式。这些约束共同检查状态锚定后的因果同步需求、共享 A2A 可传容量、服务所需 CPU、整槽协议时间和全机返航储备。

若固定的局部投影动作产生的 $\boldsymbol s^{\mathrm{pred}}[t+1]$ 属于 $\mathcal V_{t+1}$，则直接执行。这里的成员关系只是一项数值预检查：当前动作已经固定，$\boldsymbol s^{\mathrm{pred}}[t+1]$ 不再是优化变量。若预检查失败，恢复投影不能把非线性状态递推写成“$\boldsymbol s^{\mathrm{pred}}(\boldsymbol f,\boldsymbol b)\in\mathcal V_{t+1}$”并据此声称满足 DCP；它必须把当前动作与未来证书显式联立。

为此，令 $\boldsymbol f^0[t],\boldsymbol b^0[t]$ 为恢复投影中的当前动作变量，并定义当前槽的统一更新上界和保守速率

$$
\overline W_{n|t}^{0}[t]
\bigl(\boldsymbol f^0[t]\bigr)
:=
d_{r_n}[t]
\left(
\overline W_{n|t}^{\mathrm{bg}}[t]
+\sum_{i\in\mathcal I_{r_n}}
\overline\eta_{ni|t}[t]
\frac{f_i^0[t]\Delta}{c_i}
\right),
$$

$$
\underline C_{n|t}^{\mathrm{A},0}
\bigl(b_n^0[t]\bigr)
:=
b_n^0[t]\log_2\left(
1+\frac{P_{np_n}^{\mathrm A}h_{np_n}[t]}
{N_0b_n^0[t]}
\right),
$$

其中 $b_n^0[t]=0$ 时速率按连续延拓取零。联合恢复证书集合 $\mathcal K_t(\boldsymbol x_\tau)$ 由三部分组成。第一，$(\boldsymbol f^0[t],\boldsymbol b^0[t])\in\mathcal F_t^{\mathrm{local}}(\boldsymbol x_\tau)$，并用当前队列的凸 epigraph 锚定未来队列：

$$
\begin{aligned}
0\le Q_i^{\mathrm{cert}}[t+1]&\le Q_i^{\max},\\
Q_i^{\mathrm{cert}}[t+1]
&\ge Q_i[t]+A_i[t]
-\frac{d_{r(i)}[t]f_i^0[t]\Delta}{c_i},\\
0\le\frac{d_{r(i)}[t]f_i^0[t]\Delta}{c_i}
&\le Q_i[t]+A_i[t],
\qquad\forall i.
\end{aligned}
$$

第二，对已经处于预拷贝阶段的事件 $s_n\le t<c_n$，当前槽与未来欠同步变量直接联立为

$$
G_n^{\mathrm{cert}}[t+1]
\ge
\overline W_{n|t}^{0}[t]
\bigl(\boldsymbol f^0[t]\bigr),
$$

$$
G_n^{\mathrm{cert}}[t+1]
\ge
G_n[t]
+\overline W_{n|t}^{0}[t]
\bigl(\boldsymbol f^0[t]\bigr)
-\underline C_{n|t}^{\mathrm{A},0}
\bigl(b_n^0[t]\bigr)\Delta.
$$

对尚未开始预拷贝的事件 $t<s_n$，当前槽不能使用 A2A，且当前更新直接进入开始状态：

$$
\begin{aligned}
G_n^{\mathrm{cert}}[s_n]
={}&H_n[\tau]
+\sum_{j=\tau}^{t-1}W_n[j]
+\overline W_{n|t}^{0}[t]
\bigl(\boldsymbol f^0[t]\bigr)\\
&+\sum_{k=t+1}^{s_n-1}
\overline W_{n|t}^{\mathrm{cert}}[k]
\bigl(\boldsymbol f^{\mathrm{cert}}[k]\bigr).
\end{aligned}
$$

这里 $s_n=t+1$ 时最后一个和为空，当前 $b_n^0[t]=0$ 由 $\mathcal F_t^{\mathrm{local}}$ 的窗口门控保证。$\mathcal K_t$ 同时包含上文从 $k=t+1$ 开始的全部未来队列、CPU、A2A epigraph、带宽、停机与协议约束；其 $Q_i^{\mathrm{cert}}[t+1]$ 和 $G_n^{\mathrm{cert}}[t+1]$ 使用本段当前 epigraph，不再使用预测状态等式。

第三，联合证书不引入 $E_u^{\mathrm{pred}}[t+1]$ 等式，而是把当前凸能耗和未来凸能耗放入同一个前缀。对 $q=t,\ldots,T_\tau^{\mathrm{end}}$，取 $\sum_{k=t+1}^{t}(\cdot):=0$，并要求

$$
\begin{aligned}
&\overline E_{u|t}^{\mathrm{use},0}
\bigl(\boldsymbol f^0[t],\boldsymbol b^0[t]\bigr)
+\sum_{k=t+1}^{q}
\overline E_{u|t}^{\mathrm{use,cert}}[k]\\
&\qquad\le
E_u[t]
-\overline E_{u|t}^{\mathrm{ret}}[q+1]
-E_u^{\mathrm{res}},
\qquad
u\in\mathcal U^{\mathrm{air}}[q+1].
\end{aligned}
$$

对每个满足 $c_n\ge t$ 的活动源 UAV，失败分支还要求

$$
\begin{aligned}
&\overline E_{u_n|t}^{\mathrm{use},0}
\bigl(\boldsymbol f^0[t],\boldsymbol b^0[t]\bigr)
+\sum_{k=t+1}^{c_n}
\overline E_{u_n|t}^{\mathrm{use,cert}}[k]\\
&\qquad\le
E_{u_n}[t]
-\overline E_{u_n|t}^{\mathrm{ret}}[c_n+1]
-E_{u_n}^{\mathrm{res}}
-E_n^{\mathrm{abort}}.
\end{aligned}
$$

$q=t$ 的通用前缀对应 $\mathcal F_t^{\mathrm{local}}$ 中的当前常规返航储备；它在联合集合中作为前缀族的起点重复陈述，但当前能耗在每条不等式左端只出现一次。$c_n=t$ 时失败分支的未来和同样为空，并对应局部约束中的额外中止储备，因而当前停机槽不会被漏计或双计。

恢复投影因而显式求解当前动作与未来证书的联合问题：

$$
\begin{aligned}
\bigl(\boldsymbol f^{0,*}[t],
\boldsymbol b^{0,*}[t],
\mathcal Z_{t+1}^{\mathrm{cert},*}\bigr)
=
\arg\min_{\boldsymbol f^0,\boldsymbol b^0,
\mathcal Z_{t+1}^{\mathrm{cert}}}\quad&
\|\boldsymbol f^0-\widetilde{\boldsymbol f}[t]\|_{\mathrm N}^2
+\lambda_b
\|\boldsymbol b^0-\widetilde{\boldsymbol b}[t]\|_{\mathrm N}^2\\
\mathrm{s.t.}\quad&
(\boldsymbol f^0[t],\boldsymbol b^0[t],
\mathcal Z_{t+1}^{\mathrm{cert}})
\in\mathcal K_t(\boldsymbol x_\tau),
\end{aligned}
$$

并下发 $\boldsymbol a^{\mathrm c}[t]:=(\boldsymbol f^{0,*}[t],\boldsymbol b^{0,*}[t])$。归一化范数使用各 UAV 的 CPU 容量和系统 A2A 带宽。若 $\mathcal K_t$ 为空，先记录 $g^{\mathrm{cert}}[t]$；它只说明在当前边界下没有可证实的终端路径，本身不是物理失败。控制器随后主动中止，活动源 UAV 执行中止返航，替补 UAV 丢弃未提交副本，双方停止写入；此后因“中止后未确认”进入物理失败吸收态。故障后的业务重建不在本窗口内处理。

真实状态和性能指标仍按 $\ell_n^{\mathrm{radio}}[t]$ 与实际分支固定能耗计量。固定方案与风险边界后，$\mathcal F_t^{\mathrm{local}}$ 的带宽门控和队列约束为线性约束，当前与未来 DVFS 能量前缀是凸函数不超过常数；Shannon 速率关于带宽为凹函数，因此当前和未来的因果 epigraph 以及整槽停机条件都是凸约束。由此，固定动作后的 $\mathcal V_{t+1}$ 是带数值锚点的凸可行性检查，恢复阶段的 $\mathcal K_t$ 是显式的联合凸可行集；本文不把非线性状态映射等式当作 DCP 依据。若应用写入上界对 CPU 呈非凸关系，则用经测量验证的分段仿射上包络替代；不能直接宣称原非凸模型可由凸求解器处理。完整时隙无线能量上界可能较保守。第 V 节把“屏蔽拒绝、但用完整实现值求得可行延续”记为假阳性，把“屏蔽放行、随后因实际资源或协议时间导致 C1–C4 违约”记为假阴性；资源仍可行时的独立 ACK 丢失只计物理确认失败，不误记为屏蔽假阴性。

### D. 策略训练、在线执行与风险更新

MV-HPPO 的联合原始策略分解为

$$
\pi_{\boldsymbol\theta}
\left(
\widetilde{\boldsymbol a}[t]\mid\boldsymbol s[t]
\right)
=
\pi_{\theta_{\mathrm d}}
\left(
\boldsymbol a^{\mathrm d}[t]\mid
\boldsymbol s[t],\boldsymbol m[t]
\right)
\pi_{\theta_{\mathrm c}}
\left(
\widetilde{\boldsymbol a}^{\mathrm c}[t]\mid
\boldsymbol s[t],\boldsymbol a^{\mathrm d}[t]
\right).
$$

训练缓冲区保存状态、策略原始提出的完整离散组合、回溯/beam 评估过的组合、最终执行组合、各步掩码、原始连续动作、局部投影动作、最终执行动作、未来证书状态和终止原因。环境根据最终执行组合与动作以及实际随机实现值递推，策略概率比仍使用原始提案密度；离散回溯和连续投影都是策略后的确定性安全变换，不把变换后动作错误地当作 Beta 分布样本。该变换会改变执行分布，本文不声称由此得到无偏策略梯度，也不声称搜索得到全局最优组合。

策略参数采用 PPO 截断目标更新 [17]。令 $\lambda_F\ge0$ 为轨迹失败约束的乘子，使用的终端拉格朗日回报为

$$
U_\tau-\lambda_F\sum_tg[t],
$$

并加入前述势函数差缓解稀疏回报。价值网络估计该回报，策略损失由 PPO 截断项、价值误差、策略熵和一个停止梯度的屏蔽距离辅助项组成。辅助项只促使连续策略均值靠近最终执行动作，不承担安全保证。

若一个批次包含 $B_{\mathrm{ep}}$ 个回合，并令 $\alpha_\lambda>0$ 为乘子更新步长，则经验失败概率和乘子更新为

$$
\widehat J_F
:=
\frac{1}{B_{\mathrm{ep}}}
\sum_{e=1}^{B_{\mathrm{ep}}}\sum_tg_e[t],
$$

$$
\lambda_F
\leftarrow
\left[
\lambda_F
+\alpha_\lambda
\left(
\widehat J_F-\varepsilon_F
\right)
\right]^+.
$$

拉格朗日更新只控制训练分布上的经验物理失败率，不提供有限样本概率保证。测试阶段必须在实际随机实现值上报告物理失败率的单侧置信上界；匹配拒绝、完整组合证书为空、搜索截断、屏蔽假阳性和假阴性作为方法诊断另行计数，不能与确认失败或实际约束违约混成同一事件。

训练环境从第 III 节状态递推生成。课程从单区域、单事件开始，逐步增加区域数、并发轮换、替补稀缺度、更新放大系数和预测误差。状态写入模型先用板卡轨迹训练，再在未参与训练的应用和负载轨迹上检验；策略训练不能替代状态模型验证。

在线运行时，控制器在 $\tau$ 一次性冻结 ACK 份额、$\alpha_{\mathrm{rem}}[\tau]$ 和整窗 alpha-spending 序列，再更新本槽唯一的一组规划边界。随后依次执行匹配感知方案选择、完整组合回溯和初始 $\mathcal V_\tau$ 检查；同槽的全部候选与恢复求解复用这一边界族和 $\delta_t$。每个时隙由连续策略提出动作，局部投影修正当前物理限制，未来可行性屏蔽检查终端路径，最后才下发资源动作；执行首个实际动作后立即令 $\alpha_{\mathrm{rem}}[t+1]=\alpha_{\mathrm{rem}}[t]-\delta_t$，不能在下一槽重置。确认成功后在槽末更新服务世代、所有者和待命池。若风险预算耗尽或运行中恢复投影为空，先记录认证诊断，再执行主动中止；系统失败由随后“中止后未确认”触发，而不是由证书为空本身触发。

### E. 可解子问题、复杂度与保证边界

离散阶段的二分图包含剩余事件、待命 UAV 和可行候选边。对第 $j$ 步二分图 $\mathcal G_j$，一次最大匹配检查的复杂度为 $O(|\mathcal E_j|\sqrt{|\mathcal N_j^{\mathrm{rem}}|+|\mathcal U_j^{\mathrm{rem}}|})$；顺序选择会重复检查，可通过增量匹配和缓存候选证书降低开销。

令 $N_{\mathrm{comb}}:=|\mathcal L_\tau|$ 为通过单事件与 Hall 必要条件后必须访问的完整叶数，则

$$
N_{\mathrm{comb}}
\le
\prod_{n\in\mathcal N_\tau}|\mathcal P_n|.
$$

记一次初始证书 $\mathcal V_\tau$ 的求解成本为 $C_{\mathcal V_\tau}$，一次叶路径上全部匹配检查成本的上界为 $C_{\mathrm{match}}$。完备回溯的最坏时间为

$$
O\!\left(
N_{\mathrm{comb}}
\bigl(C_{\mathrm{match}}+C_{\mathcal V_\tau}\bigr)
\right),
$$

因为每个完整叶都必须恰好求解一次 $\mathcal V_\tau$；不能只报告匹配成本。已访问集合的直接存储为 $O(N_{\mathrm{comb}})$，前缀缓存和并行 beam 只改变常数与执行顺序，不改变这一最坏界或删除叶节点。

设未来证书含 $n_t$ 个连续变量、$m_t$ 个凸约束和 $K_{\mathrm{ip}}$ 个内点迭代。稠密实现的保守复杂度为 $O(K_{\mathrm{ip}}(n_t+m_t)^3)$，内存复杂度为 $O((n_t+m_t)^2)$。实际模型按会话、UAV 和事件呈稀疏块结构，可采用滚动缩短、热启动和提前不可行证书满足单时隙时限。

第 V-B 节定义的小规模 Case 1 使用全信息离线基线：固定满足 C1 的候选组合，并分别计算一个松弛上界和一个可执行解。欠同步递推必须写成

$$
G_n[k+1]\ge W_n[k],\qquad
G_n[k+1]\ge
G_n[k]+W_n[k]-C_n^{\mathrm A}[k]\Delta.
$$

在最大化交接余量且 $G_n$ 不出现在任何正向奖励项时，较小的 $G_n$ 总不劣，因此上述 epigraph 不等式在最优解处取紧，才与 $[G_n[k]-C_n^{\mathrm A}[k]\Delta]^++W_n[k]$ 的因果递推等价。持续时间相关的实际无线能耗可能破坏直接凸性：计算松弛上界时删除该能耗项以扩大原可行域，计算可执行解时改用完整时隙无线能耗上界以缩小原可行域；两个离线问题都使用整槽停机容量和槽末所有权生效条件。前者只提供性能上界，后者只提供保守可行值；二者之间的区间才包围原问题最优值。只有完成因果 epigraph 重写并通过原始残差与对偶间隙检查，才能把松弛子问题称为经认证的凸上界，不能把任一凸替代直接称为原问题精确最优。

若规划边界在其声明覆盖范围内成立、最终提交的完整候选组合满足初始 $\mathcal V_\tau(\boldsymbol x_\tau)\ne\varnothing$、每个执行动作均保持状态锚定的 $\mathcal V_{t+1}$ 非空，且实际协议开销不超过模型上界，则屏蔽层可对边界模型给出资源与离场终端可达性证书。最大匹配只用于替补排他，不能替代初始未来可行集检查；确认随机失败则由候选/时刻相关下界和一次性 $\alpha_n^{\mathrm{ack}}$ 控制，而不是由确定性证书消除。以至少 $1-\beta_{\mathrm{cal}}$ 的校准置信度，且在声明的条件覆盖假设下，整窗运行风险由不重置的 alpha-spending 控制在 $\alpha_{\mathrm{sh}}$ 内。该条件性结论不等于真实系统绝对安全：边界失配、未建模故障、确认丢包和状态接口遗漏仍会造成失败。MV-HPPO 不保证原随机混合整数问题的全局最优，也不从训练过程推出真实失败概率上界；这些性质分别由小规模离线上界、独立轨迹覆盖率和多随机种子统计检验评估。

## V. 实验设计

实验分为状态模型校准、单窗口在线调度、多窗口生命周期和半实物协议验证四层。所有结果均为待执行的实验计划，不预设算法优于基线。随机过程、实例生成、求解器失败、屏蔽假阳性/假阴性和协议失败均保留原始记录。

### A. 状态轨迹与半实物校准

第一层实验在两块异构边缘计算板卡上运行至少三类持续业务：目标跟踪与计数、滑动窗口多传感融合以及带去重提交的流式聚合。每个应用先由开发者和测试共同标识永久、关键与易失状态，再通过状态接口记录以下量：

- 初始关键快照 $H_n[\tau]$；
- 每时隙原始写入、槽内同键覆盖、槽末封存序号和不可变 delta 大小 $W_n[t]$；
- 任务处理量 $\mu_i[t]$ 与动作后实现的写入放大系数 $\widetilde\eta_{ni}[t]$；
- 预热、冻结、状态应用、候选/时刻相关确认结果和中止时间；
- 重放输入量、重放时延以及恢复后的逐输入输出一致性；
- A2A 数据字节、无线开启时间，以及成功/失败两条分支分别测得的收发与固定协议能耗。

数据按应用、负载和运行轨迹划分为训练、校准和最终保留测试集。状态与确认边界只用训练和校准集拟合，最终测试集用于检验 $\overline W$ 的覆盖率、停机拷贝字节误差、协议完成时间 $T_n^{\mathrm{proto}}$ 误差，以及 $\underline p_{np|t}^{\mathrm{ack}}[c_{np}]$ 的候选/时刻条件覆盖率。成功交接的服务中断由模型固定为 $\Delta$，不再把较短的协议完成时间误称为实际中断。关键状态参数不预设一个通用的 64–256 MB 区间，而由板卡轨迹的快照和不可变 delta 分布给出；不同应用分别报告数量级，不合并成一个缺乏语义的“运行状态规模”。确认样本不足的分层标为不可认证并从认证规划器排除；若某事件全部候选都不可认证，则报告认证规划器不可用，而不把它计为结构不可行。

半实物链路使用网络仿真器或可控无线链路重放带宽、时延、丢包与中断，并执行以下状态机：替补预热、预拷贝、源端冻结、停机拷贝、目标载入、世代确认、槽末成功接管，或未确认后的副本丢弃与中止返航。恢复正确性通过输入序号、跟踪标识、窗口输出、去重结果和提交世代逐项比较。若关键状态遗漏造成输出不一致，该应用不属于当前模型的支持范围。实验分别报告成功分支固定为 $\Delta$ 的服务中断，以及失败后从冻结到窗口外业务重建完成的无服务时长；观察结束仍未重建的样本按右删失处理，二者不合并。实际能耗按成功/失败分支测量，不用安全规划中的共同上界替代。

### B. 单窗口仿真与实例生成

单窗口保留三个规模，用于分别验证精确上界、常规并发和扩展性：

| 测试实例 | 服务区域数 | UAV 数 | 最大并发交接数 | 主要用途                     |
| -------- | ---------: | -----: | -------------: | ---------------------------- |
| Case 1   |          3 |      5 |              1 | 枚举方案并与认证离线上界比较 |
| Case 2   |          6 |      9 |              3 | 评价常规共享 A2A 调度        |
| Case 3   |         10 |     15 |              5 | 评价替补稀缺、并发和实时性   |

时隙长度和窗口长度的基准值分别取 $\Delta=1$ s 与 $T_{\mathrm w}=30$，并在敏感性实验中改变。每区域包含 4–8 个会话，任务到达采用由平稳、突发和相关三类轨迹构成的数据集；单位数据计算量与 UAV CPU 容量参考 UAV-MEC 文献 [1]–[5]，关键更新和协议参数只来自第 V-A 节实测轨迹。

窗口开始时，除 $R$ 架在役 UAV 外的其余 UAV 按待命、替补航路、返航和换电四种角色采样。事件区域无放回抽取，最晚离场时刻由当前电量、返航航路和安全储备共同生成。实例生成器先检查是否存在覆盖全部事件的二分匹配，再为每个事件保留 2–4 架通过单事件因果终端证书与 ACK 下界的替补，并枚举完整组合确认至少一个 $\mathcal V_\tau$ 非空。只有完整组合全部耗尽仍不可行的窗口才标为结构不可行；在线回溯被时限截断则计为算法截断诊断，不能混入结构不可行。

候选航路长度、飞行速度、路径损耗、CPU 能耗和飞行功率从文献支持范围采样；真实 A2A 信道按包含视距主径和随机散射的 Rician（莱斯）衰落过程生成。规划信道下界、更新上界、返航能量上界和候选/时刻 ACK 下界通过训练与校准数据构造，并使用显式整轨迹风险预算。测试环境始终用原始随机实现值递推，不用规划分位数或 ACK 下界替代真实信道与确认结果。

每个学习方法使用相同网络参数上限、环境交互预算和 10 个训练随机种子。每个训练模型在 30 个独立测试种子上运行，每个种子至少生成 1000 个窗口。连续指标用“训练种子—测试种子”两层自助法构造 95% 置信区间；物理失败率对每个训练模型报告 Clopper–Pearson 单侧 95% 上置信界。只有所有训练模型的上置信界均不超过 $\varepsilon_F$，才认为独立测试支持经验风险目标；有限样本中的零失败只报告其上置信界。

### C. 单窗口基线与消融

所有基线使用同一个物理系统失败事件：实际 ACK 失败、主动中止后未确认或实际 C1–C4 违约；匹配拒绝、证书为空、搜索截断和屏蔽真假阳性只作为方法诊断。候选角色、航路有效性、ACK 数据充足性和最低确认下界对所有方法一致，避免某个基线通过使用未校准候选获得表面收益。基线围绕固定迁移工作量、状态拆分、在线前瞻和安全屏蔽逐层增强：

1. **Stop-and-Copy**：不预拷贝，在暂停后发送全部需同步关键状态；
2. **Whole-Memory Pre-Copy**：把应用内存页作为统一对象执行传统预拷贝，用于暴露高脏页率下的不收敛与停机开销 [14], [15]；
3. **State-Decomposed Fixed-Time Sync**：采用永久状态预热、关键状态同步和易失状态重放，但固定预拷贝提前量并比例分配资源 [14]；
4. **TOM-Style Fixed-Memory Migration**：以固定虚拟机内存大小计算迁移时间，采用源/目标资源锁的并行分组，不使用净更新递推和返航边界 [13]；
5. **Earliest-Deadline Heuristic**：按最晚离场时刻排序，选择最早可确认方案，并用最早截止期优先分配 A2A；
6. **One-Step Greedy Projection**：使用与 MV-HPPO 相同的状态拆分和局部投影，但不检查剩余匹配与未来终端可行集；
7. **有限时域鲁棒模型预测控制（model predictive control，MPC）**：使用同一风险边界、状态模型和终端证书，逐窗口求解混合整数鲁棒模型；
8. **Clairvoyant Offline Bounds**：仅在 Case 1 使用完整未来实现值并枚举满足 C1 的候选组合；删除持续时间相关无线能耗得到凸松弛上界，采用完整时隙无线能耗上界得到保守可执行值，两者均使用因果 epigraph 状态递推与整槽停机条件；
9. **Hybrid-PPO-Penalty**：使用相同混合策略网络，仅以固定奖励惩罚处理约束；
10. **MV-HPPO**：完整方法。

关键消融包括：

- **w/o State Decomposition**：用整个内存脏页代替应用辅助净更新；
- **w/o Update Coupling**：训练时令预测写入上界中的 $\overline\eta_{ni|t}=0$，测试仍使用真实更新轨迹；
- **w/o Matching Check**：仅屏蔽当前不可用替补，不检查剩余最大匹配；
- **Local Projection Only**：删除未来终端可行集，只保留单时隙投影；
- **Source-Only Return Reserve**：仅保护源 UAV，用于验证全机储备的必要性；
- **w/o Abort Branch**：忽略确认失败后的中止时间和能量；
- **w/o Queue Objective**：删除 $\overline Q_\tau$，检验策略是否把 CPU 压至缓存边界；
- **w/o Risk Allocation**：独立使用固定单时隙分位数，检验其轨迹风险失配；
- **w/o Potential Shaping** 和 **w/o Curriculum**：分别检验训练稀疏性与规模课程的影响。

主要物理指标包括最小相对交接余量、平均归一化队列、任务完成量、成功交接的固定服务中断 $\Delta$、协议完成时间 $T_n^{\mathrm{proto}}$、失败后的无服务时长、成功确认率、物理轨迹失败率及单侧置信上界、源/替补最小返航余量、按分支实测的总能耗、A2A 字节和无线开启时间。方法诊断单独报告匹配拒绝率、完整组合证书为空率、搜索截断率、屏蔽修正距离、屏蔽假阳性、屏蔽假阴性和单时隙决策时间；不得把诊断事件直接累加到物理失败率。Case 1 还报告策略值相对离线松弛上界的差距、离线保守可执行值，以及两个凸子问题的原始残差和对偶间隙。

### D. 多窗口轮换生命周期

单窗口实验用于隔离交接机制，但不能证明持续轮换。多窗口生命周期实验使任务队列、服务所有者、关键状态版本、UAV 电量和角色跨窗口连续递推。替补接管后成为新的在役 UAV；源 UAV 沿实际返航航路到达换电站，经历换电时间和库存等待后恢复满电，再从补能点飞至待命位置并重新进入候选池。窗口之间不重置待命池和随机过程。

生命周期包含三类基础设施：地面固定换电站、由移动地面平台提供的换电点以及由高空平台站（high-altitude platform station，HAPS）维持的空中回传或协调覆盖。在相同任务到达、轮换触发和随机种子下，实验分别对照固定地面控制与回传、移动地面平台控制与回传、HAPS 协调与回传三种控制链。HAPS 版本只改变控制链路可用性、候选信息时延和 A2A 回传容量，不把 HAPS 计算能力无故加入状态交接。每个生命周期至少覆盖 20 次轮换或直到系统进入无法恢复状态，并重复不同任务强度、换电时间、备用机数量和并发强度。

生命周期指标包括单位时间完成任务量、长期队列尾部、连续服务比例、成功轮换的整槽中断、失败后的无服务时长、换电站排队、待命池枯竭率、交接吸收终止率、服务世代连续性、全机安全返航率和单位有效工作量能耗。实验分别比较单窗口训练直接部署、加入生命周期状态训练和滚动鲁棒 MPC，以判断局部策略是否会通过过早消耗替补或电量获得短期收益。

### E. 鲁棒性、分布外与扩展性

鲁棒性实验依次改变任务到达强度、初始关键快照、净更新放大系数、覆盖合并率、A2A 衰落、替补到达偏差、电池衰减、返航能耗误差、确认丢包和换电站等待。重点设置 CPU 负载、更新放大系数和初始返航余量的三因素实验，以检验“继续计算—新增同步工作量—返航安全”的交互是否真实存在。

分布外测试包含未见应用状态轨迹、持续信道下降、多个候选临时失效、确认报文丢失、换电站容量下降和相关突发任务。物理失败按确认失败、主动中止未确认和实际队列/带宽/时间/能量违约分类；输出不一致作为 H4 正确性失败单列。方法诊断另按状态边界低估、匹配拒绝、完整组合证书为空、在线搜索截断、屏蔽假阳性和假阴性分类。并发事件从 1 增至 Case 3 上限，并增加到 8 个事件的压力测试，以评价最大匹配、未来证书和恢复投影能否在一个时隙内完成。

### F. H1–H5 的待预注册判据

下表是提交正式预注册前的判据草案，不表示阈值已经由实验确定。$\lambda_Q$、状态覆盖目标、相对误差容限、最小效应量、等效界、屏蔽真假阳性容限和在线时限只能在训练集、校准集或单独的 pilot 集上选择，并须在打开最终保留测试集之前连同随机种子、检验方向和置信水平一起冻结。最终测试结果不得反向调整这些量。H4 的恢复正确性采用预先固定的零容忍标准，不需要 pilot 选择。

| 判据                 | 主指标                                                                 | 零假设或否定条件                                                                                   | 待冻结统计判据                                                                                              |
| -------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| H1：因果状态模型有效 | 不可变 delta、停机拷贝字节和$T_n^{\mathrm{proto}}$ 的覆盖率与误差    | 声明的上界覆盖不足，或上界宽到不能区分候选                                                         | 对覆盖率报告二项分布单侧下置信界，对相对误差报告分层自助置信区间；目标覆盖率与误差容限仅由校准/pilot 集确定 |
| H2：场景耦合存在     | 高、低耦合区的物理失败率、最小交接余量和队列差异                       | 高更新、强 A2A 竞争或紧离场区中，联合方法相对固定内存/解耦基线的预设交互效应不为正或小于最小效应量 | 使用配对实例和训练种子的分层自助交互对比；最小效应量在 pilot 后冻结                                         |
| H3：未来屏蔽有用     | 物理失败率、屏蔽假阳性/假阴性、搜索截断率和运行时间                    | 相比仅局部投影未降低物理失败，或假阳性、假阴性、截断率、性能损失或运行时间超过冻结容限             | 使用相同实例与随机种子的配对单侧置信区间；各容限和等效界在 pilot 后冻结                                     |
| H4：状态拆分正确     | 逐输入输出、去重结果和服务世代与无迁移运行的一致性                     | 任一保留测试轨迹出现不一致                                                                         | 零容忍：出现一次不一致即否定当前应用范围；A2A 字节和协议完成时间改善只作次级性能指标                        |
| H5：持续轮换成立     | 多窗口物理失败率、吸收终止率、服务世代连续性、返航储备和待命池枯竭趋势 | 随轮换次数出现预设不利趋势，或任一服务世代断裂/实际返航约束违约                                    | 对趋势斜率给出单侧置信区间，效应阈值在 pilot 后冻结；服务世代与实际返航硬约束按事件逐项审计                 |

无论效应阈值如何选择，以下结果都会要求修改模型或缩小结论：独立测试上的风险边界或 ACK 下界低于声明覆盖率；模型预测可行而半实物协议发生物理失败；任一 UAV 在失败分支无法保留返航储备；物理轨迹失败率的单侧上置信界超过 $\varepsilon_F$；或 Case 1 与认证离线上界长期保持大差距且简单短视基线并不更差。

## 附录 A：Problem–Method–Insight、新颖性边界与模型风险

### A.1 Problem–Method–Insight

**Problem。** 电池触发的轮换要求源 UAV 在最晚离场时刻前把服务交给待命 UAV。为了维持业务质量，源 UAV 在预拷贝期间仍需处理任务，而任务处理可能产生新的、不可由输入重建的关键状态更新；并发轮换又共享 A2A 资源。替补选择、计算进度、关键状态同步、确认协议和全机返航储备因而共同决定未来是否仍存在可完成交接的路径。

**Method。** 系统按永久、关键和易失三类状态恢复，只对应用辅助、经轨迹校准、槽末封存且跨槽不可改写的关键状态增量日志建模。调度器联合选择替补方案、暂停时刻、CPU 和 A2A 带宽；完整离散组合先通过初始未来可行集检查，连续动作再检查队列所需最小计算、因果关键更新、剩余传输容量、整槽协议时间和全机返航储备。混合 PPO 只学习未知随机过程下的性能策略。

**Insight。** 电池轮换下，当前资源动作可行不足以说明服务能够安全交接；决定终端可行性的量是“剩余不可重建关键更新”相对于“最晚离场前仍可保留的同步、协议和返航容量”的动态余量。当计算会产生新的不可合并更新时，增加计算既可降低队列，也可能扩大同步需求并消耗返航能量，因此安全调度必须保持未来终端路径，而不是只修正当前约束。

### A.2 与最近邻工作的正面边界

TOM 已经研究有状态 UAV-VEC，并联合决定轨迹、卸载和多服务并行迁移 [13]。其迁移工作量由固定虚拟机内存大小给出，源/目标资源锁决定并行分组；本文不主张“首次研究有状态 UAV 服务”或“首次并行迁移”。本文与其区别限定为电池强制退出、应用级关键增量在预拷贝期间演化、确认截止期、失败分支和全机返航储备共同形成的终端可行性。

Ye 等已经研究低电量 UAV 与满电 UAV 之间的服务交接，并明确转移用户、计算任务及其当前状态 [25]。该方法根据剩余电量、飞行距离、站点容量和预估交接时间调度 UAV；本文不主张“首次研究电池触发的 UAV-MEC 服务交接”，区别在于把交接时间从给定输入展开为受任务处理、关键状态增量和共享 A2A 带宽共同影响的在线过程。

Frejo-Martín 等已经提出面向电池轮换的有状态微服务迁移架构 [29]。其流程预传容器存储层，在替补 UAV 起飞时停止源服务，再通过最终检查点恢复运行状态；迁移性能评估与资源优化仍留待后续工作。本文因而不主张“首次把有状态迁移用于 UAV 轮换”，而研究该流程在硬离场、并发资源竞争和安全返航约束下的终端可行调度。

Rong 等已经证明整个内存预拷贝可能因脏页速率超过链路速率而失败，并提出永久状态预热、关键状态同步和易失状态重放 [14]。本文继承这一状态分解思想，不把预拷贝或状态拆分本身写成创新；新增问题是如何在移动 A2A、硬离场与多事件资源竞争下调度经验证的关键状态日志。

KubeSPT 的故障语义分为三段 [15]：状态复制或迭代检查点阶段失败时可以终止迁移且源 Pod 仍运行；最终检查点、目标 Pod 创建和服务重定向阶段的通信失败可能丢失状态；Hot Data/Lazy-Restore 阶段的通信失败不影响恢复。本文不取代通用容器迁移系统，而把可验证的应用状态接口、单写者世代和中止分支嵌入 UAV 轮换调度；其有效性依赖具体应用和板卡实现。

容器分层存储可减少镜像文件迁移开销 [16]，但本文假设镜像和永久状态已预置。若替补 UAV 不能预置镜像，镜像层传输、拉取失败和启动时间必须加入候选方案与协议固定时间，当前模型不再直接适用。

### A.3 主要风险与缩小版本

第一项风险是关键状态识别。应用可能遗漏影响正确性的隐藏状态，复杂服务也可能无法用版本化增量日志表示。状态接口、输出一致性测试和保留轨迹是使用模型的前置条件；失败时应限定到可明确序列化关键上下文的流式服务。

第二项风险是更新上界。$W_n[t]$ 表示槽内覆盖合并后在槽末封存、跨槽不再抵消的非负增量，并非通用脏页率；若写入与 CPU、输入内容或应用阶段之间关系不能由分段仿射上界覆盖，或必须依赖跨槽压缩才可运行，应改用场景约束、分布鲁棒集合或扩展状态模型。

第三项风险是预测覆盖与轨迹风险。风险分配只在规划边界校准正确时有意义，拉格朗日更新只控制经验失败率。真实部署仍需独立监测，并在模型边界失效时保守终止交接；故障后的业务重建位于当前交接窗口和本文保证之外，因此本文不声称绝对安全。

第四项风险是规模。未来可行性屏蔽比普通一步投影开销高；若 Case 3 无法在时隙内求解，可发表的缩小版本为单区域或少量并发事件，使用解析容量证书和确定性最晚离场边界验证核心机制，再把大规模学习调度留作后续工作。

第五项风险是长期系统边界。换电站库存、替补回补、连续轨迹和 HAPS 控制链路由生命周期实验显式递推，但不全部进入单窗口解析模型。若多窗口实验发现这些上层状态主导失败，应把研究对象从“交接窗口调度”扩展为多时间尺度机群运维，不能继续依靠独立窗口结论。

## 参考文献

[1] C. Peng, Y. Chen, X. Huang, Z. Wu, Y. Xu, and Y. Wu, “Demand-aware multi-area multi-UAV empowered mobile edge computing: A joint energy and delay optimization,” *IEEE Trans. Mobile Comput.*, early access, 2026, doi: 10.1109/TMC.2026.3697839.

[2] F. Pervez, A. Sultana, C. Yang, and L. Zhao, “Energy and latency efficient joint communication and computation optimization in a multi-UAV-assisted MEC network,” *IEEE Trans. Wireless Commun.*, vol. 23, no. 3, pp. 1728–1741, Mar. 2024.

[3] Z. Sun, G. Sun, Q. Wu, L. He, S. Liang, H. Pan, D. Niyato, C. Yuen, and V. C. M. Leung, “TJCCT: A two-timescale approach for UAV-assisted mobile edge computing,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 4, pp. 3130–3147, Apr. 2025.

[4] D. Ye, Z. Sun, W. Zhong, J. Kang, X. Huang, D. I. Kim, S. Xie, and C. Yuen, “Optimal flight speed scheduling and battery swapping in UAV-enabled mobile edge computing,” *IEEE Trans. Mobile Comput.*, vol. 25, no. 1, pp. 948–960, Jan. 2026.

[5] J. Li, C. Yi, J. Chen, Y. Shi, T. Zhang, X. Li, R. Wang, and K. Zhu, “A reinforcement learning-based stochastic game for energy-efficient UAV swarm-assisted MEC with dynamic clustering and scheduling,” *IEEE Trans. Green Commun. Netw.*, vol. 9, no. 1, pp. 255–270, Mar. 2025.

[6] C. Liu, X. Xin, Y. Dai, and D. Xu, “Cost optimization of UAV swarm network for persistent emergency communication,” *IEEE Trans. Green Commun. Netw.*, vol. 10, pp. 1734–1748, 2026.

[7] G. Zhang, X. Ou, M. Cui, Q. Wu, S. Ma, and W. Chen, “Cooperative UAV enabled relaying systems: Joint trajectory and transmit power optimization,” *IEEE Trans. Green Commun. Netw.*, vol. 6, no. 1, pp. 543–557, Mar. 2022.

[8] M. Zhao, R. Zhang, Z. He, and K. Li, “Joint optimization of trajectory, offloading, caching, and migration for UAV-assisted MEC,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 3, pp. 1981–1998, Mar. 2025.

[9] L. Wang, B. Shen, L. Ma, Y. Zhang, Y. Zhao, H. Guo, Z. Yu, and B. Guo, “Joint task offloading and migration optimization in UAV-enabled dynamic MEC networks,” *IEEE Trans. Serv. Comput.*, vol. 18, no. 4, pp. 2143–2157, Jul.–Aug. 2025.

[10] W. Feng, W. Gao, J. Yao, L. Zhou, C. Yan, and T. Q. S. Quek, “Prediction-assisted multi-UAV online service migration and trajectory control for MEC-empowered vehicular networks,” *IEEE Trans. Mobile Comput.*, early access, 2026, doi: 10.1109/TMC.2026.3700894.

[11] Y. Shi, C. Yi, R. Wang, Q. Wu, B. Chen, and J. Cai, “Service migration or task rerouting: A two-timescale online resource optimization for MEC,” *IEEE Trans. Wireless Commun.*, vol. 23, no. 2, pp. 1503–1519, Feb. 2024.

[12] D.-J. Han, W. Fang, S. Hosseinalipour, M. Chiang, and C. G. Brinton, “Orchestrating federated learning in space-air-ground integrated networks: Adaptive data offloading and seamless handover,” *IEEE J. Sel. Areas Commun.*, vol. 42, no. 12, pp. 3505–3520, Dec. 2024.

[13] Q. Qiu, L. Li, Z. Xiao, Q. Lin, L. Ma, and Z. Ming, “TOM: Joint trajectory, offloading and migration optimization in stateful service-oriented UAV-enabled VEC system,” *IEEE Trans. Serv. Comput.*, vol. 18, no. 6, pp. 4261–4275, Nov.–Dec. 2025.

[14] C. Rong, J. H. Wang, J. Wang, Y. Zhou, and J. Zhang, “Live migration of video analytics applications in edge computing,” *IEEE Trans. Mobile Comput.*, vol. 23, no. 3, pp. 2078–2092, Mar. 2024.

[15] H. Zhang, S. Wu, H. Fan, Z. Huang, W. Xue, C. Yu, S. Ibrahim, and H. Jin, “KubeSPT: Stateful pod teleportation for service resilience with live migration,” *IEEE Trans. Serv. Comput.*, vol. 18, no. 3, pp. 1500–1514, May–Jun. 2025.

[16] L. Ma, S. Yi, N. J. Carter, and Q. Li, “Efficient live migration of edge services leveraging container layered storage,” *IEEE Trans. Mobile Comput.*, vol. 18, no. 9, pp. 2020–2031, Sep. 2019.

[17] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” arXiv:1707.06347, 2017.

[18] J. Achiam, D. Held, A. Tamar, and P. Abbeel, “Constrained policy optimization,” in *Proc. 34th Int. Conf. Mach. Learn. (ICML)*, vol. 70, pp. 22–31, 2017.

[19] A. Stooke, J. Achiam, and P. Abbeel, “Responsive safety in reinforcement learning by PID Lagrangian methods,” in *Proc. 37th Int. Conf. Mach. Learn. (ICML)*, vol. 119, pp. 9133–9143, 2020.

[20] F. Mou, J. Lou, Z. Tang, Y. Wu, W. Jia, Y. Zhang, and W. Zhao, “Adaptive digital twin migration in vehicular edge computing and networks,” *IEEE Trans. Veh. Technol.*, vol. 74, no. 3, pp. 4839–4854, Mar. 2025.

[21] X. Zhang, C. Wang, Y. Zhu, J. Cao, and T. Liu, “Multi-agent deep reinforcement learning with trajectory prediction for task migration-assisted computation offloading,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 7, pp. 5839–5856, Jul. 2025.

[22] N. Zhao, Z. Ye, Y. Pei, Y.-C. Liang, and D. Niyato, “Multi-agent deep reinforcement learning for task offloading in UAV-assisted mobile edge computing,” *IEEE Trans. Wireless Commun.*, vol. 21, no. 9, pp. 6949–6960, Sep. 2022.

[23] C. Huang, G. Chen, P. Xiao, Y. Xiao, Z. Han, and J. A. Chambers, “Joint offloading and resource allocation for hybrid cloud and edge computing in SAGINs: A decision assisted hybrid action space deep reinforcement learning approach,” *IEEE J. Sel. Areas Commun.*, vol. 42, no. 5, pp. 1029–1043, May 2024.

[24] N. Gupta, S. Agarwal, D. Mishra, and B. Kumbhani, “Trajectory and resource allocation for UAV replacement to provide uninterrupted service,” *IEEE Trans. Commun.*, vol. 71, no. 12, pp. 7288–7302, Dec. 2023, doi: 10.1109/TCOMM.2023.3307559.

[25] Z. Ye, P. N. Ji, and T. Wang, “Seamless service handover in UAV-based mobile edge computing,” in *Proc. IEEE Global Commun. Conf. (GLOBECOM)*, 2023, pp. 1113–1118, doi: 10.1109/GLOBECOM54140.2023.10437843.

[26] A. Calagna, Y. Yu, P. Giaccone, and C. F. Chiasserini, “Design, modeling, and implementation of robust migration of stateful edge microservices,” *IEEE Trans. Netw. Service Manag.*, vol. 21, no. 2, pp. 1877–1893, Apr. 2024, doi: 10.1109/TNSM.2023.3331750.

[27] A. Calagna, Y. Yu, P. Giaccone, and C. F. Chiasserini, “MOSE: A novel orchestration framework for stateful microservice migration at the edge,” *IEEE Trans. Netw. Service Manag.*, vol. 22, no. 5, pp. 4827–4841, 2025, doi: 10.1109/TNSM.2025.3579051.

[28] D. K. Fernando, J. Terner, P. Yang, and K. Gopalan, “V-Recover: Virtual machine recovery when live migration fails,” *IEEE Trans. Cloud Comput.*, vol. 11, no. 3, pp. 3289–3300, Jul.–Sep. 2023, doi: 10.1109/TCC.2023.3282466.

[29] S. Frejo-Martín, A. García-López, J. M. Murillo, and J. Galán-Jiménez, “Live migration of stateful microservices in UAV-assisted networks for enhanced availability,” in *Proc. IEEE Symp. Comput. Commun. (ISCC)*, 2025, pp. 1–6, doi: 10.1109/ISCC65549.2025.11325941.
