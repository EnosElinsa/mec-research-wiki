# 电池轮换场景下无人机 MEC 有状态服务交接的可行性与在线调度

## I. 引言

移动边缘计算（mobile edge computing，MEC）把计算能力部署到网络边缘，为时延敏感业务提供近端处理。灾后巡检、输电线路监测和偏远设施观测会持续产生图像、视频和多源传感数据，其共同特点是任务连续到达，后续处理依赖已经形成的运行上下文。搭载计算模块的无人机（unmanned aerial vehicle，UAV）可在地面基础设施受损或覆盖不足时靠近任务区域提供计算服务；多区域、多无人机与分时隙集中控制也已成为 UAV-MEC 的常见架构 [1]–[3]。单架无人机受电池容量和载荷限制，难以在区域上空长期驻留，持续服务需要机群按电量状态轮换接替。

现有研究通过换电、动态机群调度和周期替换延长无人机服务时间 [4]–[7]。这些方案能够维持飞行平台、无线覆盖或计算资源供给。连续运行的 MEC 服务还保留任务队列、跟踪上下文、滑动窗口、缓存、输入处理位置和未确认结果；接替无人机只有取得这些运行状态，才能从源机已经完成的位置继续处理。平台接替与服务接续由此成为两个相互关联的过程。

本文把后续计算依赖既有运行状态的业务称为有状态服务。已有任务迁移和服务迁移研究证明了剩余输入、部分结果、服务实例和模型状态可以在边缘节点之间转移 [8]–[12]。电池轮换进一步引入了由返航安全决定的最晚离场时刻。源机在预拷贝期间仍处理持续到达的任务，CPU 分配会同时减少任务队列并产生新的待传状态；预拷贝持续越久，状态传输越充分，源机用于计算、通信和悬停的能量也越多，返航余量随之减小。因此，待传状态量是由调度决策和任务过程共同产生的动态状态，交接中断与返航安全需要在同一时域内协调。

本文考虑一个由多架无人机服务多个地理区域的 UAV-MEC 系统。每个区域由一架在役机接收任务、执行计算并返回结果，当前未承担区域服务、替补任务、返航或换电的无人机组成待命池。当在役机接近返航边界时，控制器从待命池中选择替补机。替补机到达后，源机在继续处理任务的同时通过无人机间（air-to-air，A2A）链路预拷贝运行状态；随后，源机在选定时刻暂停计算和状态更新，通过停机拷贝发送剩余状态，替补机确认状态版本后接管服务。多个区域的轮换窗口可能重叠，各事件共同占用有限的 A2A 带宽。提高 CPU 频率可以缩短任务队列，也会加快状态增长并增加能耗；增加 A2A 带宽可以加快状态传输，却会减少其他并发事件可用的带宽；延后暂停时刻可以延长预拷贝窗口，同时压缩源机的返航能量余量。

在上述场景中，控制器需要为每个轮换事件选择替补机和暂停时刻，并按时隙分配任务 CPU 与 A2A 带宽。本文以满足中断上限后仍可传输的额外状态量定义交接余量，并用初始状态规模进行归一化，目标是在限制完整轨迹失败概率的条件下提高最差轮换事件的相对交接余量。替补机排他选择、任务队列、计算能力、共享带宽、停机中断和安全返航共同限定可行域。随机任务到达和时变 A2A 信道又使控制器无法预先获得完整时域信息，问题由此形成一次性离散方案选择与逐时隙连续资源分配相结合的在线序贯决策。

该决策结构直接决定求解方法。窗口开始时的替补方案选择受到待命机排他约束，并确定后续预拷贝窗口、暂停时刻和连续动作的可行范围；窗口内的 CPU 与带宽动作持续改变任务队列、状态增长、能耗和下一时隙的可行域。在线重复求解完整混合整数随机优化的开销随事件数和候选数快速增加。已有工作分别采用离散—连续两阶段策略、连续动作多智能体策略和混合动作策略处理动态调度 [14]–[16]，但其模型没有同时包含本文的替补机排他、共享资源和安全返航约束，因而不能直接保证输出动作落入本文可行域。本文据此设计可行性引导的混合动作近端策略优化算法（feasibility-guided hybrid proximal policy optimization，FG-HPPO）：顺序候选掩码处理一次性离散排他关系，条件连续策略生成 CPU 和 A2A 带宽，可行性投影修正当前时隙的资源动作。单时隙投影无法保证未来可行域始终非空，因此算法把完整轨迹失败定义为约束代价，并通过自适应拉格朗日乘子控制经验失败概率 [18], [19]。

本文的主要贡献概括如下：

1. 在多区域多无人机 MEC 架构中建立电池轮换下的有状态服务交接模型，将任务处理引起的状态增长、预拷贝、停机拷贝和源机返航写入统一的状态演化过程。
2. 构建带完整轨迹失败概率约束的在线调度问题，给出替补机选择、任务处理、状态传输和安全返航条件，刻画计算速度、状态增长与离场时限之间的耦合关系。
3. 设计 FG-HPPO 算法，以顺序候选掩码、条件连续策略和可行性投影分别处理排他方案选择与逐时隙资源约束，并通过拉格朗日更新约束完整轨迹失败概率。

本文其余内容安排如下。第 II 节综述无人机持续服务、有状态迁移和深度强化学习调度方面的相关研究；第 III 节建立系统模型并给出问题表述；第 IV 节介绍 FG-HPPO 算法；第 V 节给出实验设计。新颖性边界和模型风险列于附录。

## II. 相关工作

本节围绕平台持续运行、计算状态迁移和在线约束调度三条证据线展开。第一类工作说明无人机补能和轮换能够延长服务时间；第二类工作给出任务或服务跨节点转移的方法；第三类工作提供动态混合决策的求解基础。各类研究已经解决的问题与其仍采用的假设共同界定本文的研究范围。

### A. 无人机持续服务与电池轮换

多无人机 MEC 研究已经联合处理区域部署、用户关联、任务卸载、计算资源和轨迹 [1]–[3]。在补能场景中，Ye 等进一步联合优化巡检航路、离散飞行速度、任务卸载和电池更换 [4]；Li 等通过动态聚类、应用放置、任务委托和能量补给维持无人机群的计算服务 [5]。这些模型说明计算决策会改变飞行能耗和补能安排，其任务在选定节点完成后结束，没有描述长时运行服务的内存状态、输入位置或提交权如何转移。

持续覆盖研究通过周期轮换延长机群运行时间。Liu 等规划固定翼无人机的替换航路、动态中继树和返航储备，以较小机群维持灾区通信 [6]；Zhang 等通过前后无人机的重叠飞行降低中继切换损失 [7]。这类方法延续了接入链路或中继拓扑，服务对象是通信连接。MEC 在役机同时保存任务队列与运行上下文，接替过程还需要恢复可继续执行的计算状态。

### B. 任务迁移与有状态服务交接

UAV-MEC 中的迁移研究主要处理尚未完成任务或服务实例的执行位置变化。Zhao 等联合优化轨迹、卸载、缓存和迁移 [8]；Wang 等转移剩余输入和部分计算结果，以减少移动用户的大结果回传时延 [9]；Feng 等结合车辆轨迹预测、服务迁移和多无人机轨迹控制 [10]。Shi 等在帧尺度选择服务迁移或任务重路由，在时隙尺度分配卸载、CPU 和带宽，并显式考虑服务恢复时延 [11]。Han 等在卫星覆盖窗口结束前转移训练数据和部分模型，使后继节点继续执行联邦学习 [12]。这些工作覆盖了任务输入、部分结果、服务实例和模型状态等迁移对象。

面向车联网边缘的迁移研究进一步考虑服务驻留位置和迁移资源成本。Mou 等把数字孪生迁移建模为带通信、共置和迁移时延的序贯决策，并在 CPU、内存和存储容量下选择目标边缘节点 [13]。Zhang 等利用车辆轨迹预测和两阶段多智能体强化学习联合处理任务迁移、带宽与计算资源 [14]。这类模型把服务或任务的迁移工作量作为输入，重点优化迁移目标及其通信、计算开销。

本文关注迁移工作量本身的演化。源机在预拷贝阶段继续处理流式任务，CPU 动作持续生成新的待传状态；暂停时刻同时决定剩余状态量、服务中断和返航能量。多个区域还会并发占用同一 A2A 资源池。上述关系把状态生成、状态复制、计算暂停和返航边界连接成一个闭环，超出了仅选择迁移目标或给定迁移开销的模型范围。

### C. 基于深度强化学习的在线调度

深度强化学习已经用于动态 UAV-MEC 的卸载、资源分配和迁移。Zhao 等以多智能体强化学习联合决定任务卸载和资源分配 [15]；Wang 等把 PPO 与模仿学习结合，用于动态多无人机网络中的卸载和迁移 [9]；Zhang 等分别用 MAPPO 和 MADDPG 处理离散迁移与连续资源动作 [14]；Huang 等针对空天地网络中的离散卸载和连续资源分配设计混合动作策略 [16]。这些方法说明混合动作可由分层或多头策略表示，但动作表示本身不能保证排他、带宽和返航约束成立。

约束强化学习把安全或资源违约表示为策略的期望代价约束。Achiam 等通过信赖域更新限制约束代价 [18]；Stooke 等研究自适应拉格朗日乘子对约束满足速度和训练稳定性的影响 [19]。这类方法适合控制轨迹级失败概率，逐时隙硬资源约束仍需显式可行化处理。

本文问题包含三个相互嵌套的结构：窗口开始时的一次性替补方案具有跨事件排他关系；方案选定后，CPU 与带宽动作受逐时隙资源和能量约束；当前可行动作仍可能在未来随机状态下导致交接失败。FG-HPPO 依次使用顺序候选掩码、条件连续策略与可行性投影处理前两类结构，再用拉格朗日更新约束完整轨迹的失败概率。该设计对应本文可行域的形成顺序。

## III. 系统模型与问题建模

本文沿用多区域、多无人机、集中控制和分时隙运行的 UAV-MEC 基础架构 [1]–[3]。区域部署、地面用户关联、任务上行和安全航路由上层规划器给出，本文固定这些关系并研究服务运行层。相对于已有架构，系统新增电池轮换模块和有状态交接模块：前者维护在役机、待命池、返航与换电状态，后者通过 A2A 预拷贝、停机拷贝和版本确认转移持续业务的运行状态。

具体而言，每个区域包含若干地面业务会话，并在任一时刻由一架在役无人机接收任务、执行计算和返回结果；当前未承担区域服务、替补任务、返航或换电的无人机组成待命池。系统按时隙运行。当某架在役机接近返航边界时，上层系统给出需要轮换的源机、可用待命机及其安全航路，逻辑控制器据此选择替补机和暂停时刻，并分配任务 CPU 与 A2A 带宽。替补机到达后，源机在继续处理任务的同时预拷贝运行状态；到达选定的暂停时刻后，源机停止计算和状态更新，通过停机拷贝发送剩余状态，替补机完成状态载入和版本确认后接管服务，源机保留返航能量离开区域。不同区域的交接窗口可以重叠，因此任务处理、状态增长、状态传输和电池消耗需要联合建模。控制器只收集队列、电量、状态规模和信道下界等调度信息，不汇集用户原始数据。下文依次给出网络与轮换过程、任务队列与计算、A2A 状态交接、能耗与交接可行性模型，并在此基础上建立在线优化问题。

### A. 网络对象与轮换过程

服务区域、无人机和业务会话的集合分别记为

$$
\mathcal R=\{1,\ldots,R\},\qquad
\mathcal U=\{1,\ldots,U\},\qquad
\mathcal I=\{1,\ldots,I\}.
$$

无人机集合 $\mathcal U$ 包含当前在役机、可用待命机、正在执行替补任务的无人机以及正在返航或换电的无人机。每个区域在任一时刻恰有一架在役机，因此持续轮换至少需要 $U>R$。候选替补机只从当前不负责任何区域且未被既有轮换任务占用的待命机中选择；已被派出、正在返航或换电的无人机在重新满足出发条件前不会进入候选集。

会话 $i\in\mathcal I$ 位于区域 $r(i)\in\mathcal R$，区域 $r$ 内的会话集合为

$$
\mathcal I_r=\{i\in\mathcal I:r(i)=r\}.
$$

时间被划分为长度为 $\Delta$ 秒的时隙。控制器在时隙 $\tau$ 优化由 $W$ 个时隙组成的滚动窗口

$$
\mathcal W_\tau=\{\tau,\ldots,\tau+W-1\}.
$$

窗口内的轮换交接事件构成集合 $\mathcal N_\tau$。本文只对 $|\mathcal N_\tau|\ge1$ 的窗口执行交接优化；若窗口内没有轮换事件，系统维持当前服务关系并进入下一滚动窗口。为避免在同一窗口内引入链式接替，每个区域至多包含一个轮换事件，即

$$
\sum_{n\in\mathcal N_\tau}\mathbb 1\{r_n=r\}\le1,
\qquad \forall r\in\mathcal R.
$$

对事件 $n\in\mathcal N_\tau$，服务区域 $r_n$ 和源机 $u_n$ 已由窗口开始时的服务关系确定。候选方案集合为 $\mathcal P_n$。方案 $p\in\mathcal P_n$ 指定一架可用待命机 $v_{np}$、预拷贝开始时隙 $s_{np}$ 和源机暂停写入时隙 $c_{np}$，并满足

$$
\tau\le s_{np}<c_{np}<\tau+W.
$$

每个候选方案均已通过待命状态、任务占用、航路、速度、到达能量和碰撞间距检查。令 $x_{np}\in\{0,1\}$ 表示事件 $n$ 是否采用方案 $p$。每个事件只选择一次方案；将其唯一选中的方案记为 $p_n$，并简记 $v_n=v_{np_n}$、$s_n=s_{np_n}$ 和 $c_n=c_{np_n}$。方案一经选定便不再撤销，以免引入旧预拷贝数据、沉没通信能耗和状态版本回滚等额外过程。选定方案后，区域 $r$ 在时隙 $t$ 的服务所有者记为 $o_r[t]$。交接成功时，$o_{r_n}[t]=u_n$ 对 $t\le c_n$ 成立，并从时隙 $c_n+1$ 起更新为 $o_{r_n}[t]=v_n$。因此，$o_r[t]$ 由交接结果递推，不是独立决策变量。

### B. 任务队列与计算模型

令 $A_i[t]$ 表示会话 $i$ 在时隙 $t$ 已完成上行传输并进入服务队列的数据量，单位为 bit。地面上行链路采用保守速率下界 $\underline C_i^{\mathrm{up}}[t]$，因此

$$
A_i[t]\le \Delta\underline C_i^{\mathrm{up}}[t].
$$

$A_i[t]$ 是控制器在时隙开始时观测到的外生输入，其到达过程参数记为 $\lambda_i^{\mathrm{arr}}$。终端或地面网关在收到结果确认前保留原始输入，替补机可以根据输入序号重放尚未完成的数据，A2A 链路只传输无法由输入重建的运行状态。

令 $Q_i[t]$ 表示时隙 $t$ 开始时会话 $i$ 的待处理数据量，$c_i$ 表示处理 1 bit 数据所需的 CPU 周期数，单位为 cycle/bit；$f_i[t]$ 表示分配给会话 $i$ 的 CPU 频率，单位为 cycle/s。停机拷贝期间暂停任务执行。用 $\mathbb 1\{\cdot\}$ 表示指示函数，定义区域服务指示量

$$
d_r[t]
=
1-
\sum_{n:r_n=r}
\sum_{p\in\mathcal P_n}
x_{np}\mathbb 1\{t=c_{np}\},
$$

其中同一区域在同一时隙至多进行一次交接。记 $[z]^+=\max\{z,0\}$，则队列按下式更新：

$$
Q_i[t+1]
=
\left[
Q_i[t]+A_i[t]
-\frac{d_{r(i)}[t]f_i[t]\Delta}{c_i}
\right]^+.
$$

无人机 $u$ 的最大 CPU 频率记为 $F_u^{\max}$。上述模型将整个停机时隙视为不可计算时间，实际系统若提前完成停机拷贝，可以在时隙结束前恢复服务。

### C. A2A 通信与状态交接模型

交接事件 $n$ 在时隙 $t$ 获得的 A2A 带宽记为 $b_n[t]$，系统可用于状态交接的总带宽为 $B^{\mathrm A}$，二者的单位均为 Hz。候选目标机和航路不同，其 A2A 信道也不同。对方案 $p$，令 $\underline h_{np}[t]$ 表示保守信道功率增益，$P_{np}^{\mathrm A}$ 表示源机发射功率，单位为 W；$N_0$ 表示噪声功率谱密度，单位为 W/Hz。对应的 A2A 速率 $C_{np}^{\mathrm A}[t]$ 以 bit/s 计，表示为

$$
C_{np}^{\mathrm A}[t]
=
b_n[t]\log_2\left(
1+\frac{P_{np}^{\mathrm A}\underline h_{np}[t]}
{N_0b_n[t]}
\right).
$$

当 $b_n[t]=0$ 时，按连续延拓定义 $C_{np}^{\mathrm A}[t]=0$。方案 $p$ 的传输窗口指示量为

$$
\omega_{np}[t]
=
\mathbb 1\{s_{np}\le t\le c_{np}\}.
$$

因此，事件 $n$ 只能在所选方案的预拷贝和停机拷贝窗口内占用 A2A 带宽。

**状态交接过程。**

令 $S_n[t]$ 表示源机在预拷贝开始前保存的完整运行状态上界，其中 $S_n[\tau]$ 由状态估计器在当前滚动窗口开始时测得。运行状态由背景写入和任务处理共同产生。令 $\overline\delta_n^0$ 表示背景状态增长率上界，$\overline\eta_n$ 表示每处理 1 bit 输入所产生状态量的上界，则时隙 $t$ 的状态增长率为

$$
\overline\delta_n[t]
=
\overline\delta_n^0
+\overline\eta_n
\sum_{i\in\mathcal I_{r_n}}\frac{f_i[t]}{c_i}.
$$

在替补机开始接收状态之前，源机的完整运行状态按下式增长：

$$
S_n[t+1]
=
S_n[t]+\overline\delta_n[t]\Delta,
\qquad
\tau\le t<s_n.
$$

令 $G_n[t]$ 表示选定方案下目标机尚未接收的状态量。预拷贝开始时，

$$
G_n[s_n]=S_n[s_n].
$$

为简化记号，定义选定方案的 A2A 速率 $C_n^{\mathrm A}[t]=C_{np_n}^{\mathrm A}[t]$。在 $s_n\le t<c_n$ 的预拷贝阶段，未传状态量递推为

$$
G_n[t+1]
=
\left[
G_n[t]
+\overline\delta_n[t]\Delta
-C_n^{\mathrm A}[t]\Delta
\right]^+.
$$

源机在时隙 $c_n$ 暂停写入。冻结、状态应用和确认所需的固定时间分别为 $\tau_n^{\mathrm{freeze}}$、$\tau_n^{\mathrm{apply}}$ 和 $\tau_n^{\mathrm{ack}}$，其总和记为

$$
\tau_n^{\mathrm{fix}}
=
\tau_n^{\mathrm{freeze}}
+\tau_n^{\mathrm{apply}}
+\tau_n^{\mathrm{ack}}.
$$

若协议元数据大小为 $S_n^{\mathrm{meta}}$，记停机时需要传输的总数据量为 $D_n^{\mathrm{stop}}=G_n[c_n]+S_n^{\mathrm{meta}}$。事件 $n$ 的服务中断时间定义为

$$
I_n
=
\begin{cases}
\displaystyle
\tau_n^{\mathrm{fix}}
+\frac{D_n^{\mathrm{stop}}}{C_n^{\mathrm A}[c_n]},
& C_n^{\mathrm A}[c_n]>0,\\[2mm]
\tau_n^{\mathrm{fix}},
& C_n^{\mathrm A}[c_n]=0,\ D_n^{\mathrm{stop}}=0,\\
+\infty,
& C_n^{\mathrm A}[c_n]=0,\ D_n^{\mathrm{stop}}>0.
\end{cases}
$$

交接协议采用单写者租约。源机在停机状态和元数据全部确认前保留写权限，目标机获得新服务世代后才能提交结果。服务世代、确认记录和输入去重表由协议执行器维护，不作为优化变量。

### D. 能耗与交接可行性模型

令 $P_u^{\mathrm{mode}}[t]$ 表示无人机 $u$ 在时隙 $t$ 的飞行、悬停和航电功率，单位为 W。该功率由无人机当前角色以及选定候选方案中的航路和飞行阶段确定，是方案选择和系统状态的已知派生量。计算能耗采用 DVFS 模型，$\kappa_u$ 为板卡标定的计算能耗系数，单位为 $\mathrm{W}/(\mathrm{cycle/s})^3$。对方案 $p$，$P_{unp}^{\mathrm A,tot}[t]$ 表示无人机 $u$ 参与事件 $n$ 时的总无线功率，单位为 W；源机侧包含发射功率与发射电路功率，目标机侧包含接收电路功率。无人机 $u$ 的时隙能耗 $E_u^{\mathrm{use}}[t]$ 以 J 计，表示为

$$
E_u^{\mathrm{use}}[t]
=
\Delta P_u^{\mathrm{mode}}[t]
+
\kappa_u\Delta
\left(
\sum_{i:o_{r(i)}[t]=u}f_i[t]
\right)^3
+
\Delta\sum_{n\in\mathcal N_\tau}
\sum_{p\in\mathcal P_n}
x_{np}\omega_{np}[t]
\mathbb 1\{u\in\{u_n,v_{np}\}\}
P_{unp}^{\mathrm A,tot}[t].
$$

三项分别对应飞行与航电、任务计算以及 A2A 收发。A2A 能耗按完整时隙计算，因而是实际传输能耗的保守上界。若 $E_u[t]$ 表示时隙开始时的剩余电量，$E_u^{\max}$ 表示电池容量，则

$$
E_u[t+1]=E_u[t]-E_u^{\mathrm{use}}[t],
\qquad
0\le E_u[t]\le E_u^{\max},
$$

换电完成后，电量恢复为 $E_u^{\max}$。对任一空中无人机 $u$，从其时隙 $t$ 的位置沿安全航路到达可用补能点所需的保守能量记为 $\overline E_u^{\mathrm{ret}}[t]$，预留安全余量记为 $E_u^{\mathrm{res}}$。停机拷贝产生的计算和通信能耗已计入 $E_{u_n}^{\mathrm{use}}[t]$。

**队列、中断与可行余量。**

每个会话的队列上限为 $Q_i^{\max}$。事件 $n$ 的业务中断上限为 $I_n^{\max}$。由于模型为停机拷贝预留一个时隙，实际采用的中断上限为

$$
\widetilde I_n^{\max}
=
\min\{I_n^{\max},\Delta\}.
$$

对事件 $n$ 的选定方案，定义交接可行余量

$$
M_n
=
\left(\widetilde I_n^{\max}-\tau_n^{\mathrm{fix}}\right)
C_n^{\mathrm A}[c_n]
-
\left(G_n[c_n]+S_n^{\mathrm{meta}}\right).
$$

$M_n$ 的单位为 bit。$M_n\ge0$ 表示选定方案能够在停机时隙传完剩余状态和协议元数据；$M_n$ 越大，该方案对状态增长误差和链路下降的容忍范围越大。根据上述状态递推，任一可行方案都必须满足

$$
S_n[\tau]
+
\sum_{t=\tau}^{c_n-1}
\overline\delta_n[t]\Delta
\le
\sum_{t=s_n}^{c_n-1}
C_n^{\mathrm A}[t]\Delta
+
\left(\widetilde I_n^{\max}-\tau_n^{\mathrm{fix}}\right)
C_n^{\mathrm A}[c_n]
-
S_n^{\mathrm{meta}}.
$$

左侧为暂停写入前累计需要同步的状态量，右侧为预拷贝和停机拷贝可承载的总状态量。该不等式给出传输侧的必要条件，源机返航能量还需满足后文给出的电池约束。

**模型假设与适用范围。**

模型将轮换事件、可用待命机和安全航路视为上层规划结果，连续轨迹、轮换触发、待命池补充和换电站库存由上层系统处理。候选替补机在当前窗口开始时不负责任何服务区域，同一窗口内至多接管一个区域；源机完成换电后只在后续窗口重新进入待命池。服务镜像预先部署在替补机上，终端或地面网关保存未确认输入，A2A 链路只传输不可重建的运行状态。若实际系统需要迁移服务镜像或队列数据，应将相应数据量并入 $S_n[\tau]$，并在 $\tau_n^{\mathrm{fix}}$ 中加入启动时间。

状态增长率、A2A 速率和返航能耗均采用保守边界。同一区域同一时刻至多发生一次交接，停机阶段按一个完整时隙计量。这些假设使状态递推、服务所有权和返航条件能够在同一时间尺度上表示。实际误差无法由确定性边界覆盖时，可将相关约束改写为机会约束或分布鲁棒约束；多目标复制、多时隙停机和换电站排队需要另行扩展状态空间。

### E. 优化问题建模

令

$$
\boldsymbol z_\tau
=
\left(
\boldsymbol x_\tau,
\boldsymbol f_\tau,
\boldsymbol b_\tau
\right)
$$

表示窗口 $\mathcal W_\tau$ 内的控制变量，其中 $\boldsymbol x_\tau=\{x_{np}\}$ 为交接方案选择，$\boldsymbol f_\tau=\{f_i[t]\}$ 为 CPU 分配，$\boldsymbol b_\tau=\{b_n[t]\}$ 为 A2A 带宽分配。队列 $Q_i[t]$、完整状态 $S_n[t]$、未传状态 $G_n[t]$、服务所有者 $o_r[t]$ 和电量 $E_u[t]$ 按前述状态方程递推，均为由控制动作和外生输入产生的系统状态。由于任务到达、状态增长和信道条件在决策时不能完全预知，控制器采用策略 $\pi$，根据每个时隙已经观测到的系统状态依次生成 $\boldsymbol z_\tau$ 中尚未执行的动作。

**优化目标。**

在满足任务队列、交接中断和安全返航要求的前提下，本文最大化所有轮换事件中的最小相对可行余量。事件 $n$ 的状态大小参考量取滚动窗口开始时测得的状态量，即

$$
S_n^{\mathrm{ref}}
=
S_n[\tau],
$$

并假设有状态服务满足 $S_n^{\mathrm{ref}}>0$。该取值在作出方案选择前即可确定，不受 CPU 和带宽决策影响。令 $\mathcal F_\tau^{\mathrm{traj}}$ 表示窗口内全部事件完成交接且 C1–C4 始终成立的轨迹可行事件，$\varepsilon_F\in[0,1)$ 表示允许的最大轨迹失败概率。定义窗口终端效用

$$
U_\tau
=
\begin{cases}
\displaystyle
\min_{n\in\mathcal N_\tau}
\frac{M_n}{S_n^{\mathrm{ref}}},
& \mathcal F_\tau^{\mathrm{traj}}\text{ 成立},\\[2mm]
0,
& \mathcal F_\tau^{\mathrm{traj}}\text{ 不成立}.
\end{cases}
$$

策略优化问题为

$$
\max_{\pi}
\quad
\mathbb E_{\pi}[U_\tau]
$$

并满足

$$
\Pr_{\pi}\!\left(
(\mathcal F_\tau^{\mathrm{traj}})^{\mathrm c}
\right)
\le\varepsilon_F.
$$

轨迹可行事件由下文的 C1–C4 定义。期望和失败概率由任务到达、状态增长和信道演化的随机性产生。目标值为无量纲量，衡量窗口内最紧张交接事件对状态增长和链路误差的承受能力；当 $\varepsilon_F=0$ 时，该表述要求轨迹几乎必然可行。

**决策变量。**

| 变量       | 类型与范围           | 时间尺度         | 实际含义                        |
| ---------- | -------------------- | ---------------- | ------------------------------- |
| $x_{np}$ | 二元                 | 每个轮换事件一次 | 为事件 $n$ 选择候选方案 $p$  |
| $f_i[t]$ | 连续，$f_i[t]\ge0$ | 每时隙           | 分配给会话 $i$ 的 CPU 频率     |
| $b_n[t]$ | 连续，$b_n[t]\ge0$ | 每时隙           | 分配给交接事件 $n$ 的 A2A 带宽 |

速率、状态增长率、中断时间、能耗和可行余量均由上述变量和前文定义的系统状态计算得到。

**约束条件。**

首先，每个轮换事件必须选择一个候选方案，并且同一架待命机在当前滚动窗口内至多接管一个区域：

$$
\mathrm{C1}:\quad
\begin{cases}
\displaystyle
\sum_{p\in\mathcal P_n}x_{np}=1,
&\forall n\in\mathcal N_\tau,\\[2mm]
\displaystyle
\sum_{n\in\mathcal N_\tau}
\sum_{\substack{p\in\mathcal P_n:\\v_{np}=u}}x_{np}\le1,
&\forall u\in\mathcal U,\\[2mm]
x_{np}\in\{0,1\},
&\forall n\in\mathcal N_\tau,\ p\in\mathcal P_n.
\end{cases}
$$

任务处理量不能超过当前可处理数据，区域停机时 CPU 分配为零，更新后的队列不能超过缓存上限，并且同一无人机上的总 CPU 频率不能超过其计算能力：

$$
\mathrm{C2}:\quad
\begin{cases}
0\le f_i[t]\Delta
\le d_{r(i)}[t]c_i\bigl(Q_i[t]+A_i[t]\bigr),\\
\displaystyle
0\le Q_i[t+1]
=
\left[Q_i[t]+A_i[t]-\frac{d_{r(i)}[t]f_i[t]\Delta}{c_i}\right]^+
\le Q_i^{\max},\\
\displaystyle
\sum_{i:o_{r(i)}[t]=u}f_i[t]\le F_u^{\max},
\end{cases}
\quad
\forall i,u,t.
$$

所有交接事件共享 A2A 带宽。事件只能在所选方案的传输窗口内占用带宽，停机时隙必须传完剩余状态和协议元数据：

$$
\mathrm{C3}:\quad
\begin{cases}
\displaystyle
\sum_{n\in\mathcal N_\tau}b_n[t]\le B^{\mathrm A},\\[1mm]
\displaystyle
0\le b_n[t]\le
B^{\mathrm A}
\sum_{p\in\mathcal P_n}x_{np}\omega_{np}[t],\\[1mm]
M_n\ge0,
\\[1mm]
\tau_n^{\mathrm{fix}}\le\widetilde I_n^{\max},
\end{cases}
$$

$G_n[t]$ 按选定方案对应的状态交接模型递推。固定开销等于中断上限时，只有 $D_n^{\mathrm{stop}}=0$ 的事件能够满足 C3。

最后，无人机的剩余电量必须保持在有效范围内。源机在交接完成前的每个时隙都要保留从当前位置返航所需的能量和安全余量：

$$
\mathrm{C4}:\quad
\begin{cases}
0\le E_u[t+1]
=E_u[t]-E_u^{\mathrm{use}}[t]
\le E_u^{\max},
&\forall u,\ t\in\mathcal W_\tau,\\[1mm]
E_{u_n}[t+1]
\ge
\overline E_{u_n}^{\mathrm{ret}}[t+1]
+E_{u_n}^{\mathrm{res}},
&\forall n,\ \tau\le t\le c_n.
\end{cases}
$$

约束 C1 确定替补机和暂停时刻，并防止同一待命机在窗口内重复接管；C2 保证任务队列与计算资源可行，C3 约束状态传输和服务中断，C4 保证源机始终保留安全返航能力。候选集已包含待命状态、任务占用、航路、到达时序和到达能量检查。时隙 $t$ 的资源动作只能依据当时已经观测到的队列、电量、信道和状态估计。若交接确认失败，目标机丢弃已接收但尚未确认的状态副本；该事件记为交接失败，并由上层应急机制处理，不在当前优化窗口内重新选择方案。

**问题性质。**

上述问题可以表示为带轨迹失败概率约束的有限时域马尔可夫决策过程。$x_{np}$ 为离散动作，$f_i[t]$ 和 $b_n[t]$ 为连续动作，因而动作空间具有混合结构。CPU 分配同时影响任务队列、状态增长和计算能耗，交接方案同时确定替补机、预拷贝长度和源机返航余量；当前动作还会通过 $Q_i[t]$、$S_n[t]$、$G_n[t]$ 和 $E_u[t]$ 改变后续可行域。状态转移概率事先未知，控制器只能依据当前观测在线决策。即使当前动作满足约束，也可能因后续任务突增或信道下降而进入空可行域。直接枚举窗口内的混合动作会随轮换事件和候选方案数量快速增长，因此本文采用深度强化学习近似从系统状态到调度动作的策略，并用候选掩码与可行性投影降低不可行动作的出现频率。

## IV. 基于深度强化学习的在线交接调度

本节给出求解第 III-E 节在线调度问题的 FG-HPPO 算法。首先将交接过程表示为有限时域马尔可夫决策过程，然后分别设计离散交接方案策略和连续资源分配策略。候选方案掩码处理待命机可用性与方案排他关系，可行性投影修正不满足当前时隙约束的 CPU 和带宽动作。最后说明策略训练、在线执行和计算复杂度。

### A. 马尔可夫决策过程建模

滚动窗口开始时，控制器已经获得 $\mathcal N_\tau$ 中全部轮换事件及其候选方案，并在时隙 $\tau$ 一次性完成方案选择；后续时隙只分配 CPU 与 A2A 带宽。仍处于等待预拷贝、预拷贝或等待停机阶段的事件记为 $\mathcal A[t]\subseteq\mathcal N_\tau$。候选方案 $p$ 在窗口开始时的可用标志为 $\chi_{np}[\tau]\in\{0,1\}$，距预拷贝开始和暂停写入的剩余时隙数分别为 $\ell_{np}^{\mathrm s}[t]=s_{np}-t$ 和 $\ell_{np}^{\mathrm c}[t]=c_{np}-t$。令 $E_{np}^{\mathrm{route}}$ 表示目标机执行候选航路所需的保守飞行能量。

候选航路采用直线匀速模型。源机在交接前悬停于 $\boldsymbol q_{r_n}$，目标机从 $\boldsymbol q_{v_{np}}[\tau]$ 飞向区域附近的安全悬停点 $\boldsymbol q_{np}^{\mathrm{hold}}$。若航路长度和速度分别为 $L_{np}$ 和 $V_{np}$，则

$$
\boldsymbol q_{v_{np}}[k]
=
\boldsymbol q_{v_{np}}[\tau]
+\min\!\left\{1,
\frac{(k-\tau)\Delta V_{np}}{L_{np}}
\right\}
\left(
\boldsymbol q_{np}^{\mathrm{hold}}-\boldsymbol q_{v_{np}}[\tau]
\right),
$$

$$
d_{np}[k]
=
\left\|\boldsymbol q_{r_n}-\boldsymbol q_{v_{np}}[k]\right\|_2.
$$

令 $\beta_0$ 表示 1 m 参考距离处的功率增益，$\alpha$ 表示路径损耗指数，$K_R$ 表示 Rician 因子，$\varrho_h\in[0,1)$ 表示相邻时隙的信道时间相关系数。归一化复衰落系数满足一阶 Gauss–Markov 递推

$$
g_{np}[k+1]
=
\mu_R+\varrho_h\bigl(g_{np}[k]-\mu_R\bigr)
+\sqrt{1-\varrho_h^2}\,\sigma_R w_{np}[k],
$$

其中 $w_{np}[k]\sim\mathcal{CN}(0,1)$，$\mu_R=\sqrt{K_R/(K_R+1)}$，$\sigma_R=1/\sqrt{K_R+1}$，并从平稳分布 $\mathcal{CN}(\mu_R,\sigma_R^2)$ 采样 $g_{np}[\tau]$。A2A 信道功率增益为

$$
h_{np}[k]
=
\beta_0d_{np}[k]^{-\alpha}|g_{np}[k]|^2.
$$

控制器在窗口开始时观测 $g_{np}[\tau]$。递推给出的条件分布满足

$$
g_{np}[k]\mid g_{np}[\tau]
\sim
\mathcal{CN}\!\left(
\mu_R+\varrho_h^{k-\tau}(g_{np}[\tau]-\mu_R),
\sigma_R^2(1-\varrho_h^{2(k-\tau)})
\right).
$$

将该条件分布下 $|g_{np}[k]|^2$ 的 5% 分位数记为 $q_{0.05}^{\mathrm{Rice}}(k\mid g_{np}[\tau])$。窗口开始时的条件信道下界预测为

$$
\widehat h_{np\mid\tau}[k]
=
\beta_0d_{np}[k]^{-\alpha}
q_{0.05}^{\mathrm{Rice}}(k\mid g_{np}[\tau]),
\qquad s_{np}\le k\le c_{np}.
$$

将该预测序列补零到长度 $W$，记为 $\widehat{\boldsymbol h}_{np\mid\tau}$。候选特征向量定义为

$$
\boldsymbol q_{np}[t]
=
\left(
v_{np},
\ell_{np}^{\mathrm s}[t],
\ell_{np}^{\mathrm c}[t],
\operatorname{Re}g_{np}[t],
\operatorname{Im}g_{np}[t],
\underline h_{np}[t],
\widehat{\boldsymbol h}_{np\mid\tau},
P_{np}^{\mathrm A},
E_{np}^{\mathrm{route}},
\chi_{np}[\tau]
\right),
$$

其中离散的目标机编号 $v_{np}$ 通过可训练嵌入向量输入网络。无人机 $u$ 的返航能量余量定义为

$$
e_u^{\mathrm{ret}}[t]
=
E_u[t]-\overline E_u^{\mathrm{ret}}[t]-E_u^{\mathrm{res}}.
$$

为使终端目标能够由当前状态递推，令 $\mathcal C[t]$ 表示在时隙 $t$ 完成状态确认的事件集合，$\zeta[t]\in\{0,1\}$ 表示此前是否已有事件完成。初始化 $\rho[\tau]=0$ 和 $\zeta[\tau]=0$，并按下式更新：

$$
\rho[t+1]
=
\begin{cases}
\rho[t], & \mathcal C[t]=\varnothing,\\
\displaystyle
\min_{n\in\mathcal C[t]}\frac{M_n}{S_n^{\mathrm{ref}}},
& \mathcal C[t]\ne\varnothing,\ \zeta[t]=0,\\
\displaystyle
\min\left\{\rho[t],
\min_{n\in\mathcal C[t]}\frac{M_n}{S_n^{\mathrm{ref}}}\right\},
& \mathcal C[t]\ne\varnothing,\ \zeta[t]=1,
\end{cases}
$$

$$
\zeta[t+1]
=
\mathbb 1\!\left\{\zeta[t]=1\ \text{或}\ \mathcal C[t]\ne\varnothing\right\}.
$$

因此，$\rho[t]$ 在首个事件完成后保存全部已完成事件中的最小相对交接余量，$\zeta[t]$ 用于区分“尚无事件完成”和“历史最小余量恰为零”两种情况。将会话、无人机和交接事件的固定模型参数分别记为

$$
\boldsymbol d_i
=
\left(r(i),c_i,Q_i^{\max},\lambda_i^{\mathrm{arr}}\right),
\qquad
\boldsymbol d_u
=
\left(F_u^{\max},E_u^{\max},\kappa_u,E_u^{\mathrm{res}}\right),
$$

$$
\boldsymbol d_n
=
\left(
r_n,
u_n,
\overline\delta_n^0,
\overline\eta_n,
\tau_n^{\mathrm{fix}},
S_n^{\mathrm{meta}},
\widetilde I_n^{\max},
S_n^{\mathrm{ref}}
\right).
$$

其中 $\lambda_i^{\mathrm{arr}}$ 为会话 $i$ 的任务到达强度，离散的区域和无人机编号均通过嵌入向量编码。若训练实例改变无线电路功率，则候选特征 $\boldsymbol q_{np}[t]$ 还包含源机和目标机的 $P_{unp}^{\mathrm A,tot}[t]$ 参数。

控制器状态写为

$$
\boldsymbol s[t]
=
\left(
\{Q_i[t],A_i[t],\boldsymbol d_i\},
\{E_u[t],e_u^{\mathrm{ret}}[t],P_u^{\mathrm{mode}}[t],\boldsymbol d_u\},
\{o_r[t]\},
\{x_{np},S_n[t],G_n[t],\boldsymbol d_n,\boldsymbol q_{np}[t]\},
\rho[t],\zeta[t],t
\right).
$$

对尚未开始预拷贝的事件使用 $S_n[t]$，对已经开始预拷贝的事件使用 $G_n[t]$，未启用的条目以零填充并由掩码排除。本文假设任务到达、信道和飞行模式的下一时隙分布在给定 $\boldsymbol s[t]$ 和动作后与更早历史无关。在该假设下，增广状态满足马尔可夫性；若实测过程具有更长记忆，可用固定长度历史编码器替换当前状态编码器。所有连续状态在输入策略网络前分别除以对应的容量或参考量。

策略网络采样的原始动作由离散部分和连续部分组成，记为

$$
\widetilde{\boldsymbol a}[t]
=
\left(
\boldsymbol a^{\mathrm d}[t],
\widetilde{\boldsymbol a}^{\mathrm c}[t]
\right).
$$

在 $t=\tau$ 时，离散动作 $\boldsymbol a^{\mathrm d}[\tau]$ 分别为 $\mathcal N_\tau$ 中的事件选择方案 $p_n$，由此确定替补机、预拷贝开始时刻和暂停时刻，并设置相应的 $x_{np_n}=1$；在 $t>\tau$ 时，离散动作为空。方案选择在当前窗口内不可撤销。原始连续动作 $\widetilde{\boldsymbol a}^{\mathrm c}[t]$ 给出 CPU 与 A2A 带宽的分配比例。第 IV-B 节的可行性投影将其映射为连续动作 $\boldsymbol a^{\mathrm c}[t]=(\{f_i[t]\},\{b_n[t]\})$，最终下发动作记为 $\boldsymbol a[t]=(\boldsymbol a^{\mathrm d}[t],\boldsymbol a^{\mathrm c}[t])$。环境使用 $\boldsymbol a[t]$，根据第 III 节的队列、状态和电量递推更新到 $\boldsymbol s[t+1]$。

每个滚动窗口构成一个训练回合。令 $t_\tau^{\mathrm{end}}=\tau+W-1$ 表示窗口的最后一个时隙。当候选掩码全零、当前投影不可行、任一约束被违反或窗口结束时仍有事件未完成，将当前轨迹判为失败并立即终止。基础回报和失败代价分别定义为

$$
r^{\mathrm{base}}[t]
=
\begin{cases}
0, & \text{轨迹在时隙 }t\text{ 失败并终止},\\
0, & t<t_\tau^{\mathrm{end}}\text{ 且轨迹尚未终止},\\
\rho[t+1],
& t=t_\tau^{\mathrm{end}}\text{ 且 }\mathcal F_\tau^{\mathrm{traj}}\text{ 成立},\\
\end{cases}
\qquad
g[t]=\mathbb 1\{\text{轨迹在时隙 }t\text{ 失败并终止}\}.
$$

约束 $\mathbb E_\pi[\sum_t g[t]]\le\varepsilon_F$ 与第 III-E 节的轨迹失败概率约束等价。为缓解终端回报稀疏问题，训练阶段采用势函数塑形。对活动事件定义尚待同步的状态量

$$
Y_n[t]
=
\begin{cases}
S_n[t], & t\le s_n,\\
G_n[t], & s_n<t\le c_n,
\end{cases}
$$

并令 $\lambda_Q\ge0$ 为队列权重。势函数为

$$
\Phi(\boldsymbol s[t])
=
-\max_{n\in\mathcal A[t]}
\frac{Y_n[t]}{S_n^{\mathrm{ref}}}
-\frac{\lambda_Q}{|\mathcal I|}
\sum_{i\in\mathcal I}\frac{Q_i[t]}{Q_i^{\max}},
$$

其中活动事件集合为空时，第一项取零。令 $\lambda_F\ge0$ 为轨迹失败概率约束的拉格朗日乘子，策略更新使用的即时回报为

$$
r_{\lambda}[t]
=
r^{\mathrm{base}}[t]
-\lambda_F g[t]
+\Phi(\boldsymbol s[t+1])
-\Phi(\boldsymbol s[t]),
$$

本文的窗口目标和失败概率均不折扣，因此固定取 $\gamma=1$，并将正常结束和失败终止状态的势函数置为零。该形式采用约束强化学习中的拉格朗日代理 [18], [19]：$\lambda_F$ 随经验失败概率自适应更新，避免用固定失败罚值在可行率与交接余量之间进行任意折中。

### B. 可行性引导的混合动作策略

FG-HPPO 将联合策略分解为离散策略和条件连续策略：

$$
\pi_{\boldsymbol\theta}
\left(\widetilde{\boldsymbol a}[t]\mid\boldsymbol s[t]\right)
=
\pi_{\boldsymbol\theta_{\mathrm d}}
\left(\boldsymbol a^{\mathrm d}[t]\mid\boldsymbol s[t],\boldsymbol m[t]\right)
\pi_{\boldsymbol\theta_{\mathrm c}}
\left(\widetilde{\boldsymbol a}^{\mathrm c}[t]\mid\boldsymbol s[t],\boldsymbol a^{\mathrm d}[t]\right),
$$

其中 $\boldsymbol\theta_{\mathrm d}$ 和 $\boldsymbol\theta_{\mathrm c}$ 分别为两部分策略网络的参数。候选方案掩码记为 $\boldsymbol m[t]=\{m_{np}[t]\}$。若方案 $p$ 的替补机当前不可用、已被其他事件选择、不能按时到达、固定协议开销超过中断上限，或在令任务 CPU 为零并分配最大可用 A2A 带宽的有利条件下仍无法满足第 III-D 节的传输必要条件与返航储备，则令 $m_{np}[t]=0$；其余候选取 $m_{np}[t]=1$。通过掩码只表示候选通过了必要性检查，并不保证其后续可行域始终非空。

令 $K_\tau=|\mathcal N_\tau|$，并将窗口内事件按返航边界从早到晚记为 $n_1,\ldots,n_{K_\tau}$。每选定一个方案便更新待命机占用状态，供下一次选择使用。第 $j$ 次选择的掩码记为 $\boldsymbol m^{(j)}[\tau]$，离散策略网络为候选方案 $p$ 输出未归一化分数 $z_{n_jp}^{(j)}[\tau]$，则

$$
\pi_{\boldsymbol\theta_{\mathrm d}}
\left(
p\mid\boldsymbol s[\tau],p_{n_1:j-1},\boldsymbol m^{(j)}[\tau]
\right)
=
\frac{m_{n_jp}^{(j)}[\tau]\exp(z_{n_jp}^{(j)}[\tau])}
{\sum_{p'\in\mathcal P_{n_j}}m_{n_jp'}^{(j)}[\tau]\exp(z_{n_jp'}^{(j)}[\tau])}.
$$

令 $J_\tau\le K_\tau$ 表示在完成全部选择或遇到全零掩码前实际采样的方案数。窗口开始时已采样离散动作前缀的联合概率为

$$
\pi_{\boldsymbol\theta_{\mathrm d}}
\left(\boldsymbol a^{\mathrm d}[\tau]\mid\boldsymbol s[\tau]\right)
=
\prod_{j=1}^{J_\tau}
\pi_{\boldsymbol\theta_{\mathrm d}}
\left(
p_{n_j}\mid
\boldsymbol s[\tau],p_{n_1:j-1},\boldsymbol m^{(j)}[\tau]
\right),
$$

可行轨迹满足 $J_\tau=K_\tau$。当 $t>\tau$ 时离散因子取 1。若第 $j$ 次选择的全部候选均被掩蔽，控制器在计算 softmax 前直接将该回合标记为不可行；若此前已经采样了方案，则保留该动作前缀的联合概率用于策略更新。顺序选择和逐步更新的掩码使完整离散动作满足 C1。连续策略以状态和已经选定的交接方案为输入，通过 Beta 分布输出 $[0,1]$ 区间内的 CPU 与带宽比例，再按照 $F_u^{\max}$ 和 $B^{\mathrm A}$ 映射为原始动作 $\widetilde{\boldsymbol f}[t]$ 与 $\widetilde{\boldsymbol b}[t]$。

原始连续动作在执行前进入可行性投影层。给定当前窗口已经选定的 $\boldsymbol x_\tau$，投影层求解

$$
\begin{aligned}
\min_{\boldsymbol f[t],\boldsymbol b[t]}
\quad &
\sum_{i\in\mathcal I}
\left(
\frac{f_i[t]-\widetilde f_i[t]}
{F_{o_{r(i)}[t]}^{\max}}
\right)^2
+\lambda_b
\sum_{n\in\mathcal A[t]}
\left(
\frac{b_n[t]-\widetilde b_n[t]}{B^{\mathrm A}}
\right)^2\\
\mathrm{s.t.}\quad &
(\boldsymbol f[t],\boldsymbol b[t])
\in\mathcal F_t(\boldsymbol x_\tau),
\end{aligned}
$$

其中 $\lambda_b>0$ 为无量纲权重，$\mathcal F_t(\boldsymbol x_\tau)$ 包含 C2 在时隙 $t$ 的全部条件、当前共享带宽条件、到达暂停时隙事件的停机传输条件以及 C4 的当前电量条件，即

$$
\begin{aligned}
\mathcal F_t(\boldsymbol x_\tau)=\biggl\{(\boldsymbol f,\boldsymbol b):
&\ \mathrm{C2}\text{ 在时隙 }t\text{ 成立};\\
&\ \sum_n b_n[t]\le B^{\mathrm A},\quad
0\le b_n[t]\le B^{\mathrm A}
\sum_p x_{np}\omega_{np}[t];\\
&\ M_n\ge0,\quad \forall n:c_n=t;\\
&\ \tau_n^{\mathrm{fix}}\le\widetilde I_n^{\max},
\quad \forall n:c_n=t;\\
&\ 0\le E_u[t+1]\le E_u^{\max},\quad \forall u;\\
&\ E_{u_n}[t+1]\ge
\overline E_{u_n}^{\mathrm{ret}}[t+1]+E_{u_n}^{\mathrm{res}},
\quad \forall n\in\mathcal A[t]:t\le c_n
\biggr\}.
\end{aligned}
$$

C2 在当前时隙的条件包括 $Q_i[t+1]\le Q_i^{\max}$。固定 $\boldsymbol x_\tau$ 后，CPU 容量和队列条件为线性约束，DVFS 能量预算为凸约束，$C_n^{\mathrm A}[t]$ 关于 $b_n[t]$ 为凹函数，因而暂停时隙的 $M_n\ge0$ 构成凸超水平集。$\mathcal F_t$ 因此是当前时隙的凸可行集，投影层返回归一化距离最小的动作。该投影不预先保证未来的 $\mathcal F_{t'}$ 非空；若当前投影不可行，则回合进入失败终止状态并调用模型外的应急返航机制，已经选定的方案不在本窗口内重选。

策略参数采用 PPO 的截断目标更新 [17]。训练缓冲区同时保存原始 Beta 动作、离散动作的选择顺序以及每一步使用的掩码。将实际采样了策略动作或离散动作前缀的时隙集合记为 $\mathcal T_\pi$，将其中投影成功并产生执行动作的时隙集合记为 $\mathcal T_{\mathrm{proj}}\subseteq\mathcal T_\pi$。在尚未采样任何方案时由全零掩码触发的强制失败转移不属于 $\mathcal T_\pi$；已经采样离散前缀后触发的失败以及投影不可行的转移属于 $\mathcal T_\pi$，但不属于 $\mathcal T_{\mathrm{proj}}$。令 $\pi_{\boldsymbol\theta_{\mathrm{old}}}$ 表示采样轨迹时的旧策略，概率比为

$$
\varrho_t(\boldsymbol\theta)
=
\frac{\pi_{\boldsymbol\theta}(\widetilde{\boldsymbol a}[t]\mid\boldsymbol s[t])}
{\pi_{\boldsymbol\theta_{\mathrm{old}}}(\widetilde{\boldsymbol a}[t]\mid\boldsymbol s[t])}.
$$

通常情况下，概率比使用原始连续动作与本时隙顺序离散动作的联合密度，不使用投影后的动作密度；若回合在连续动作采样前因全零掩码终止，则概率比只使用此前已采样的离散动作前缀。价值网络 $V_{\boldsymbol\psi}(\boldsymbol s[t])$ 由参数 $\boldsymbol\psi$ 表示，用于估计拉格朗日回报。令 $T_\tau\le t_\tau^{\mathrm{end}}$ 为当前回合的实际终止时隙，并将正常结束和失败终止后的状态价值均置为零。对 $\lambda_{\mathrm{GAE}}\in[0,1]$，广义优势估计为

$$
\delta_t
=
r_{\lambda}[t]+\gamma V_{\boldsymbol\psi_{\mathrm{old}}}(\boldsymbol s[t+1])
-V_{\boldsymbol\psi_{\mathrm{old}}}(\boldsymbol s[t]),
\qquad
\widehat A[t]
=
\sum_{l=0}^{T_\tau-t}
(\gamma\lambda_{\mathrm{GAE}})^l\delta_{t+l}.
$$

PPO 的截断策略目标为

$$
L^{\mathrm{clip}}(\boldsymbol\theta)
=
\mathbb E_{t\in\mathcal T_\pi}\left[
\min\left(
\varrho_t(\boldsymbol\theta)\widehat A[t],
\operatorname{clip}\bigl(\varrho_t(\boldsymbol\theta),1-\epsilon,1+\epsilon\bigr)\widehat A[t]
\right)
\right],
$$

其中 $\epsilon$ 为截断系数，$\boldsymbol\psi_{\mathrm{old}}$ 表示采样轨迹时的价值网络参数。价值回报目标为

$$
\widehat R[t]
=
\widehat A[t]
+V_{\boldsymbol\psi_{\mathrm{old}}}(\boldsymbol s[t]).
$$

为使投影辅助项对策略参数具有明确梯度，令 $\boldsymbol\mu_{\boldsymbol\theta}^{f}(\boldsymbol s[t],\boldsymbol a^{\mathrm d}[t])$ 和 $\boldsymbol\mu_{\boldsymbol\theta}^{b}(\boldsymbol s[t],\boldsymbol a^{\mathrm d}[t])$ 分别表示条件连续策略映射到物理量后的均值。对 $t\in\mathcal T_{\mathrm{proj}}$，轨迹中保存投影动作 $\boldsymbol f[t]$ 和 $\boldsymbol b[t]$，更新时对其停止梯度，记为 $\operatorname{sg}(\cdot)$。投影辅助距离定义为

$$
\begin{aligned}
D_{\mathrm{proj}}(\boldsymbol\theta;t)
=
&\sum_{i\in\mathcal I}
\left(
\frac{\mu_{\boldsymbol\theta,i}^{f}(\boldsymbol s[t],\boldsymbol a^{\mathrm d}[t])-\operatorname{sg}(f_i[t])}
{F_{o_{r(i)}[t]}^{\max}}
\right)^2\\
&+\lambda_b\sum_{n\in\mathcal A[t]}
\left(
\frac{\mu_{\boldsymbol\theta,n}^{b}(\boldsymbol s[t],\boldsymbol a^{\mathrm d}[t])-\operatorname{sg}(b_n[t])}
{B^{\mathrm A}}
\right)^2.
\end{aligned}
$$

令 $\mathcal H_t$ 为联合策略熵。总损失写为

$$
L(\boldsymbol\theta,\boldsymbol\psi)
=
-L^{\mathrm{clip}}(\boldsymbol\theta)
+c_v\mathbb E_t\!\left[
\bigl(V_{\boldsymbol\psi}(\boldsymbol s[t])-\widehat R[t]\bigr)^2
\right]
-c_h\mathbb E_{t\in\mathcal T_\pi}[\mathcal H_t]
+c_p\mathbb E_{t\in\mathcal T_{\mathrm{proj}}}
[D_{\mathrm{proj}}(\boldsymbol\theta;t)],
$$

其中 $c_v,c_h,c_p\ge0$ 分别为价值误差、策略熵和投影距离的权重；价值误差在包括强制失败转移在内的全部时隙上计算。$\mathcal T_{\mathrm{proj}}$ 为空时将投影辅助项置零；若整个批次的 $\mathcal T_\pi$ 为空，则将 $L^{\mathrm{clip}}$ 和策略熵项同时置零，只更新价值网络和失败约束乘子。投影距离促使连续策略均值接近采样轨迹中的投影动作，但不替代对完整轨迹约束可行性的测试。设一个训练批次包含 $B_{\mathrm{ep}}$ 个回合，经验失败概率和拉格朗日乘子按下式更新：

$$
\widehat J_F
=
\frac{1}{B_{\mathrm{ep}}}
\sum_{e=1}^{B_{\mathrm{ep}}}\sum_t g_e[t],
\qquad
\lambda_F
\leftarrow
\left[
\lambda_F+\alpha_\lambda(\widehat J_F-\varepsilon_F)
\right]^+,
$$

其中 $\alpha_\lambda>0$ 为对偶更新步长。采集同一批轨迹时保持 $\lambda_F$ 不变，策略和价值网络更新后再执行一次对偶更新。

### C. 策略训练与在线执行

训练环境由第 III 节的状态递推构成。任务到达、初始状态规模、状态增长率、A2A 信道、替补机到达时间、电池余量和返航能耗在给定范围内随机采样，使策略接触不同负载和并发交接条件。训练从单区域、单轮换事件开始，再逐步增加区域数量、并发事件数和参数扰动范围，以降低直接探索大规模混合动作空间的难度。

每轮训练按以下过程进行：

1. 重置任务队列、电量、服务所有者和轮换事件，并生成候选方案集合；
2. 读取 $\boldsymbol s[t]$，根据必要可行条件生成候选掩码 $\boldsymbol m[t]$；
3. 在窗口开始时由离散策略为全部事件顺序选择交接方案，并在每个时隙由连续策略输出 CPU 与带宽比例；
4. 可行性投影层修正连续动作；若投影不可行，则记录失败并终止当前回合；
5. 保存状态、原始动作、执行动作、回报、掩码和终止标志；
6. 回合结束后计算优势估计，并更新离散策略、连续策略、价值网络和失败约束乘子；
7. 在独立验证场景上选择策略参数，直至验证回报和可行率不再稳定改善。

训练在逻辑控制器或离线服务器上集中完成。在线运行时，控制器先完成状态归一化和候选掩码更新，再执行策略网络前向传播与可行性投影，最后下发当前时隙动作。交接确认后，控制器更新服务所有者和待命池。若候选集合或当前可行集为空，控制器停止执行学习策略，将事件交给独立的应急返航机制，并记录失败状态用于后续模型修正和再训练。

### D. 复杂度与可行性说明

设策略网络参数量为 $N_{\theta}$，当前活动事件的候选方案总数为 $P_t=\sum_{n\in\mathcal A[t]}|\mathcal P_n|$。一次在线决策的网络推理复杂度为 $O(N_{\theta})$，候选掩码更新复杂度为 $O(P_t)$。令可行性投影包含 $n_t=|\mathcal I|+|\mathcal A[t]|$ 个连续变量和 $m_t$ 个约束。对稠密线性代数实现，内点法每个 Newton 步的计算复杂度为 $O((n_t+m_t)^3)$，若共执行 $K_{\mathrm{ip}}$ 步，则投影复杂度为 $O(K_{\mathrm{ip}}(n_t+m_t)^3)$，内存复杂度为 $O((n_t+m_t)^2)$。实际实现可利用队列、无人机和事件之间的稀疏结构降低开销。与对所有候选组合和多时隙资源动作进行枚举相比，该方法的在线计算量不随候选组合的乘积增长。

候选掩码非空且 $\mathcal F_t(\boldsymbol x_\tau)$ 在窗口内每个时隙均非空，是 FG-HPPO 形成完整可行轨迹的必要条件。在该条件以及状态增长、A2A 速率、返航能耗和协议开销的保守边界成立时，顺序掩码满足 C1，各时隙投影满足当期 C2 和 C4，并在暂停时隙满足 C3，从而得到满足 C1–C4 的完整轨迹。单个时隙投影不能保证后续可行集非空，FG-HPPO 也不保证获得原序贯决策问题的全局最优策略。其训练稳定性、轨迹可行率和策略质量需要通过独立测试、精确小规模实例和多随机种子实验评估。

## V. 实验设计

本节给出用于检验系统模型和 FG-HPPO 算法的实验方案，包括测试实例、对比方法、评价指标、消融设置、鲁棒性测试和半实物验证流程。

### A. 实验设置

仿真环境按照第 III 节的状态方程逐时隙更新任务队列、未传状态和无人机电量。为考察算法随系统规模和交接竞争程度的变化，设置三类测试实例：

| 测试实例 | 服务区域数 | 无人机数 | 最大并发交接数 | 主要用途 |
|---|---:|---:|---:|---|
| Case 1 | 3 | 5 | 1 | 与离线上界比较，检查模型和实现正确性 |
| Case 2 | 6 | 9 | 3 | 评价常规多区域调度性能 |
| Case 3 | 10 | 15 | 5 | 评价高竞争条件下的扩展性与实时性 |

任务到达率、单位数据计算量、A2A 信道、飞行功率和返航能耗的基准范围参考相关无人机 MEC 研究 [2]–[6], [8]–[11]；初始运行状态规模、状态增长和协议时间通过第 V-F 节的板卡测量校准。仿真采用以下初始设置，并在鲁棒性实验中逐项扩大范围：

| 参数 | 初始设置 |
|---|---|
| 时隙与窗口 | $\Delta=1$ s，$W=30$ |
| 业务会话 | 每区域 4–8 个会话；每会话任务数服从泊松分布，强度为 0.5–2 task/s；单任务输入量服从 $[0.5,2]$ Mbit 均匀分布 |
| 轮换事件与候选 | 窗口开始时，除 $R$ 架在役机外的 $U-R$ 架无人机均初始化为待命状态。非空窗口的事件数在 1 与“表中最大并发数和 $U-R$ 的较小值”之间均匀采样，区域无放回抽取。生成器先为各事件无放回分配一架能够按时到达的锚定目标机，再从待命池为每个事件补充候选，使其拥有 2–4 架目标机；若到达和能量筛选后锚定匹配失效，则重新生成该窗口。候选航路长度服从 $[100,500]$ m 均匀分布，飞行速度服从 $[15,25]$ m/s 均匀分布，$s_{np}=\tau+\lceil L_{np}/(V_{np}\Delta)\rceil$；对每架可按时到达的目标机生成 $c_{np}\in\{s_{np}+3,s_{np}+6,s_{np}+9\}$ 中仍位于窗口内的方案 |
| 队列与计算 | $Q_i^{\max}=80$ Mbit，$Q_i[\tau]\sim\mathcal U[0.2,0.8]Q_i^{\max}$，$c_i\sim\mathcal U[500,1500]$ cycle/bit，$F_u^{\max}\sim\mathcal U[12,24]$ GHz，$\kappa_u\sim\mathcal U[0.5,1.5]\times10^{-28}$ $\mathrm{W}/(\mathrm{cycle/s})^3$ |
| 运行状态 | $S_n[\tau]\sim\mathcal U[64,256]$ MB，$\overline\delta_n^0\sim\mathcal U[0.2,1]$ MB/s，$\overline\eta_n\sim\mathcal U[0.01,0.08]$ bit/bit，$S_n^{\mathrm{meta}}\sim\mathcal U[0.1,0.5]$ MB |
| 中断参数 | $I_n^{\max}\sim\mathcal U[0.25,0.8]$ s，$\tau_n^{\mathrm{fix}}\sim\mathcal U[0.03,0.12]$ s |
| A2A 链路 | 无人机高度固定为 100 m；目标悬停点位于源机水平距离 50 m 处，方位角均匀采样，待命机初始位置再沿独立均匀方位角与悬停点相距 $L_{np}$，并按第 IV-A 节直线路径生成 $d_{np}[k]$。载频为 2.4 GHz，1 m 参考增益取自由空间增益；$B^{\mathrm A}=40$ MHz，$P_{np}^{\mathrm A}=1$ W，源机发射电路和目标机接收电路功率分别为 5 W 和 3 W，$N_0=-174$ dBm/Hz；路径损耗指数为 2.2，$K_R=10$ dB，$\varrho_h=0.9$；$\underline h_{np}[t]$ 取给定当前复信道观测的条件功率增益 5% 分位数 |
| 电池与飞行 | $E_u^{\max}\sim\mathcal U[0.8,1.6]$ MJ，$E_u[\tau]\sim\mathcal U[0.55,0.95]E_u^{\max}$，$P_u^{\mathrm{mode}}[t]\sim\mathcal U[160,260]$ W，$E_u^{\mathrm{res}}=0.08E_u^{\max}$；返航航路长度服从 $[200,800]$ m 均匀分布，返航能量按航路飞行时间与 260 W 功率上界的乘积计算 |

FG-HPPO 的训练配置如下。候选特征由共享的两层 128 单元多层感知机编码，并使用带掩码的均值汇聚；离散策略、连续策略和价值网络各使用两层 256 单元 ReLU 网络，目标机嵌入维度为 32。所有网络使用 Adam 优化器，策略与价值网络学习率均为 $3\times10^{-4}$。设置 $\gamma=1$、$\lambda_{\mathrm{GAE}}=0.95$、PPO 截断系数 $\epsilon=0.2$、$c_v=0.5$、$c_h=0.01$、$c_p=0.1$、$\lambda_Q=1$ 和 $\lambda_b=1$；对偶变量初始化为 $\lambda_F=0$，步长为 $\alpha_\lambda=10^{-3}$。每次更新收集 $B_{\mathrm{ep}}=128$ 个回合，采用 512 个转移的最小批次训练 10 轮，并将梯度范数截断为 0.5。总训练预算为 $2\times10^6$ 个环境时隙，前 30% 预算使用 Case 1，中间 30% 逐步增加到 Case 2，剩余 40% 在 Case 1–3 和完整扰动范围内混合采样。可行性投影使用 CVXPY 的 CLARABEL 求解器，相对和绝对容差均设为 $10^{-6}$，最大迭代次数为 100；实验同时记录求解器失败和超时。所有学习方法采用相同的网络参数上限、环境交互次数和 10 个训练随机种子。

主实验设置 $\varepsilon_F=0.01$，并比较 $\varepsilon_F\in\{0,0.01,0.05\}$ 时交接余量与失败概率的变化。每个训练随机种子都保留其验证回报最高的检查点，不跨种子挑选单一模型。随后，对每个训练模型使用相同的 30 个独立测试种子，每个测试种子生成 1000 个滚动窗口；因此，每种学习方法共评估 $10\times30\times1000=300000$ 条轨迹。每个窗口都独立重置队列、电量、轮换事件和外生随机过程，不继承前一窗口的状态。

连续指标和失败率使用两层自助法构造 95% 置信区间：外层重采样训练种子，内层在对应模型下重采样测试种子。由于窗口独立重置，每个训练模型的 30000 条轨迹还单独计算 Clopper–Pearson 失败率区间，并同时报告 10 个训练种子之间的分布。只有所有训练模型的单侧 95% 上置信界均不超过 $\varepsilon_F$ 时，才判定实验结果支持概率约束。对 $\varepsilon_F=0$ 的设置只报告观测失败数及其单侧 95% 上置信界，不将有限样本中的零失败解释为绝对安全保证。

### B. 对比方法

实验包括以下对比方法：

1. **Stop-and-Copy**：不执行预拷贝，源机暂停后一次性传输全部运行状态；
2. **Fixed-Lead-Time**：为所有事件使用 6 个时隙的目标预拷贝时长，并采用比例资源分配；
3. **Earliest-Safe-Handover**：选择通过掩码的最早暂停方案，并采用最早截止期优先的带宽分配；
4. **One-Step Greedy**：按下文给出的初始余量规则选择候选方案，并逐时隙求解只包含下一状态的一步资源分配问题；
5. **Clairvoyant Offline Optimization**：在 Case 1 中使用完整的未来任务、信道和能耗轨迹，枚举候选方案并求解连续资源子问题，作为离线性能上界；
6. **Hybrid-PPO-Penalty**：采用与 FG-HPPO 相同的混合动作策略，但不使用候选掩码和可行性投影，仅通过固定奖励惩罚处理约束；
7. **FG-HPPO**：采用第 IV 节给出的完整方法。

根据窗口开始时已知的航路条件预测 $\widehat h_{np\mid\tau}[k]$，定义候选方案 $p$ 独占 $B^{\mathrm A}$ 时的预测速率

$$
\overline C_{np}^{\max}[k]
=
B^{\mathrm A}\log_2\!\left(
1+\frac{P_{np}^{\mathrm A}\widehat h_{np\mid\tau}[k]}
{N_0B^{\mathrm A}}
\right).
$$

前三种启发式方法使用相同的队列比例 CPU 动作

$$
\widetilde f_i[t]
=
F_{o_{r(i)}[t]}^{\max}
\frac{Q_i[t]c_i}
{\sum_{j:o_{r(j)}[t]=o_{r(i)}[t]}Q_j[t]c_j},
$$

其中分母为零时令 $\widetilde f_i[t]=0$。Stop-and-Copy 对候选方案定义

$$
\widehat M_{np}^{\mathrm{SC}}
=
\left(\widetilde I_n^{\max}-\tau_n^{\mathrm{fix}}\right)
\overline C_{np}^{\max}[c_{np}]
-S_n[\tau]
-\sum_{k=\tau}^{c_{np}-1}\overline\delta_n^0\Delta
-S_n^{\mathrm{meta}},
$$

并按返航边界顺序选择 $\widehat M_{np}^{\mathrm{SC}}/S_n^{\mathrm{ref}}$ 最大的未占用候选，使用 $c_{np}$ 和候选编号顺序打破并列。该方法令 $b_n[t]=0$ 对所有 $t<c_n$ 成立，并在 $t=c_n$ 时使用

$$
\widetilde b_n[t]
=
B^{\mathrm A}
\frac{D_n^{\mathrm{stop}}}
{\sum_{j:c_j=t}D_j^{\mathrm{stop}}},
$$

其中分母为零时相应带宽取零。Fixed-Lead-Time 对每架目标机先选择使 $|(c_{np}-s_{np})-6|$ 最小的候选，再按第 (4) 种方法的初始余量评分选择目标机；其原始带宽动作为

$$
\widetilde b_n[t]
=
B^{\mathrm A}
\frac{Y_n[t]/\max\{1,c_n-t\}}
{\sum_{j\in\mathcal A[t]}Y_j[t]/\max\{1,c_j-t\}}.
$$

分母为零时所有 $\widetilde b_n[t]$ 取零。Earliest-Safe-Handover 在通过掩码且目标机未占用的候选中依次选择 $c_{np}$ 最小者，并以 $s_{np}$ 和候选编号顺序打破并列；每个时隙将全部 $B^{\mathrm A}$ 分配给 $c_n-t$ 最小的活动事件，并以 $Y_n[t]/S_n^{\mathrm{ref}}$ 和事件编号顺序打破并列。三种方法的原始连续动作均经过第 IV-B 节的同一可行性投影，投影为空时记为失败。

One-Step Greedy 的候选初始余量定义为

$$
\begin{aligned}
\widehat M_{np}^{\mathrm{G}}
=
&\sum_{k=s_{np}}^{c_{np}-1}
\overline C_{np}^{\max}[k]\Delta
+\left(\widetilde I_n^{\max}-\tau_n^{\mathrm{fix}}\right)
\overline C_{np}^{\max}[c_{np}]\\
&-S_n[\tau]
-\sum_{k=\tau}^{c_{np}-1}\overline\delta_n^0\Delta
-S_n^{\mathrm{meta}}.
\end{aligned}
$$

该基线按返航边界从早到晚处理事件，在尚未占用且通过候选掩码的方案中选择 $\widehat M_{np}^{\mathrm G}/S_n^{\mathrm{ref}}$ 最大者；并列时依次选择 $c_{np}$ 较早、候选编号较小的方案。完成方案选择后，每个时隙求解

$$
\min_{(\boldsymbol f[t],\boldsymbol b[t])\in\mathcal F_t(\boldsymbol x_\tau)}
\quad
\frac{\lambda_Q}{|\mathcal I|}
\sum_{i\in\mathcal I}\frac{Q_i[t+1]}{Q_i^{\max}}
+
\frac{1}{\max\{1,|\mathcal A[t+1]|\}}
\sum_{n\in\mathcal A[t+1]}
\frac{Y_n[t+1]}{S_n^{\mathrm{ref}}}.
$$

当 $\mathcal A[t+1]$ 为空时，第二项的求和取零。该方法选择候选时只使用窗口开始时可获得的航路条件预测，不使用未来实现的任务、信道或能量样本；资源分配也不进行 $t+1$ 之后的状态递推。

Clairvoyant Offline Optimization 枚举满足 C1 的全部候选组合。对每个固定组合，将完整未来轨迹代入第 III 节模型，并用 CVXPY/CLARABEL 求解连续凸子问题；相对和绝对容差均设为 $10^{-8}$。只有当最大约束残差不超过 $10^{-7}$ 且归一化原始—对偶间隙不超过 $10^{-6}$ 时，才将该实例的最优值作为已认证的离线上界，否则只报告求解失败而不计算最优差距。该方法使用未来实现值，因此不作为因果在线策略。

Hybrid-PPO-Penalty 使用以下四个归一化违约量：

$$
\begin{aligned}
\nu_1[t]
=
\mathbb 1\{t=\tau\}\min\Biggl\{1,
&\frac{1}{|\mathcal N_\tau|}
\sum_n\left|\sum_p x_{np}-1\right|\\
&+\frac{1}{U}\sum_u
\left[\sum_n\sum_{p:v_{np}=u}x_{np}-1\right]^+\\
&+\frac{1}{|\mathcal N_\tau|}
\sum_n\sum_p x_{np}(1-\chi_{np}[\tau])
\Biggr\},
\end{aligned}
$$

$$
\begin{aligned}
\nu_2[t]
=
\min\Biggl\{1,
&\frac{1}{|\mathcal I|}\sum_i
\frac{[Q_i[t+1]-Q_i^{\max}]^+}{Q_i^{\max}}\\
&+\frac{1}{|\mathcal I|}\sum_i
\frac{[f_i[t]\Delta-d_{r(i)}[t]c_i(Q_i[t]+A_i[t])]^+}
{F_{o_{r(i)}[t]}^{\max}\Delta}\\
&+\frac{1}{U}\sum_u
\frac{[\sum_{i:o_{r(i)}[t]=u}f_i[t]-F_u^{\max}]^+}
{F_u^{\max}}
\Biggr\},
\end{aligned}
$$

$$
\begin{aligned}
\nu_3[t]
=
\min\Biggl\{1,
&\frac{[\sum_n b_n[t]-B^{\mathrm A}]^+}{B^{\mathrm A}}\\
&+\frac{1}{|\mathcal N_\tau|}\sum_n
\frac{[b_n[t]-B^{\mathrm A}\sum_p x_{np}\omega_{np}[t]]^+}
{B^{\mathrm A}}\\
&+\frac{1}{|\mathcal N_\tau|}\sum_{n:c_n=t}
\left(
\frac{[-M_n]^+}{S_n^{\mathrm{ref}}}
+\frac{[\tau_n^{\mathrm{fix}}-\widetilde I_n^{\max}]^+}
{\widetilde I_n^{\max}}
\right)
\Biggr\},
\end{aligned}
$$

以及

$$
\begin{aligned}
\nu_4[t]
=
\min\Biggl\{1,
&\frac{1}{U}\sum_u
\frac{[-E_u[t+1]]^++[E_u[t+1]-E_u^{\max}]^+}
{E_u^{\max}}\\
&+\frac{1}{|\mathcal N_\tau|}\sum_{n:t\le c_n}
\frac{[\overline E_{u_n}^{\mathrm{ret}}[t+1]
+E_{u_n}^{\mathrm{res}}-E_{u_n}[t+1]]^+}
{E_{u_n}^{\max}}
\Biggr\}.
\end{aligned}
$$

上述求和分别覆盖当前窗口的全部事件、会话或无人机，并假设 $\widetilde I_n^{\max}>0$。该基线的训练回报为

$$
r^{\mathrm{pen}}[t]
=
r^{\mathrm{base}}[t]
+\Phi(\boldsymbol s[t+1])-\Phi(\boldsymbol s[t])
-50\sum_{k=1}^{4}\nu_k[t].
$$

该基线将连续动作裁剪到物理上下界，设置 $\lambda_F=0$，其余网络结构、PPO 参数和训练预算均与 FG-HPPO 相同。

### C. 整体性能与计算开销

整体性能实验首先比较不同方法的最小相对交接余量、完整轨迹可行率、交接成功率、平均与最大服务中断时间、队列超限率、源机返航能量余量、无人机总能耗和单时隙决策时间。Case 1 用于计算 FG-HPPO 与离线上界之间的目标差距；Case 2 和 Case 3 用于比较各方法在事件数量增加后的可行率、调度质量和推理时间。

该组实验需要回答三个问题：FG-HPPO 能否同时提高完整轨迹可行率和最紧张交接事件的余量；学习策略相对短视方法能否利用当前资源为后续交接保留空间；候选数量和并发事件增加后，策略推理与可行性投影能否在一个调度时隙内完成。

### D. 消融实验

为区分各组成部分的作用，设置以下消融版本：

1. **w/o State Growth in Training**：测试环境仍使用 $\overline\eta_n>0$ 更新真实状态，训练 FG-HPPO 的仿真环境只删除 $\overline\eta_n\sum_i f_i[t]/c_i$ 项，用于检验训练时忽略计算诱导状态增长造成的策略误差；
2. **w/o Candidate Mask**：保留策略网络，但允许其采样全部候选方案；
3. **w/o Feasibility Projection**：直接执行连续策略输出，并使用奖励惩罚处理约束；
4. **w/o Hierarchy**：由单个网络同时输出离散方案和连续资源；
5. **w/o Potential Shaping**：只使用窗口终止回报；
6. **w/o Curriculum**：从训练开始即使用最大规模和全部扰动范围。

消融实验分别记录目标值、可行动作比例、训练回报方差、达到稳定验证回报所需的环境交互次数和测试阶段约束违约率。候选掩码与可行性投影的作用通过轨迹可行率和投影距离判断；分层策略与课程训练的作用通过训练稳定性和规模泛化判断；状态增长模型的作用通过边界附近的误判率判断。

### E. 鲁棒性与扩展性实验

鲁棒性实验依次改变任务到达强度、初始状态规模、状态增长估计误差、A2A 信道衰减、替补机到达偏差、电池容量衰减和返航能耗估计误差。另设置 CPU 负载、状态增长系数 $\overline\eta_n$ 与初始返航能量余量的三因素实验，直接检验计算处理、状态增长和安全离场之间的核心耦合。并发交接数从 1 逐步增加到 Case 3 的上限，同时改变可用待命机数量和每个事件的候选暂停时刻数量，以分析状态维度与候选组合增长对决策时间和调度质量的影响。

分布外测试采用训练阶段未出现的突发任务负载、连续信道下降和候选替补机临时失效。实验记录投影距离、投影不可行率、应急机制使用比例和交接失败原因，用于判断策略何时仍能形成完整可行轨迹，何时需要重新训练或扩大保守边界。

### F. 半实物验证

半实物验证分三个阶段进行。第一阶段在两块边缘计算板卡上运行持续写入状态的视觉分析程序，测量不同 CPU 频率下的处理吞吐量、状态增长量、冻结时间、状态应用时间和确认时间。第二阶段使用网络仿真器或信道模拟器重放 A2A 速率、丢包和替补机到达过程，并验证模型计算的停机传输容量。第三阶段将两块计算板卡分别安装或映射为源机与替补机，执行预拷贝、停机拷贝、版本确认、服务恢复和返航电量检查。

该实验重点检验三项模型假设：状态增长率能否由 CPU 处理量给出稳定上界；保守速率和固定协议开销能否正确预测服务中断；模型判定可行的完整动作轨迹在实测系统中是否仍能完成状态交接并保留返航储备。若这些条件无法成立，应缩小模型适用范围或改用机会约束，而不能仅通过重新训练策略掩盖模型误差。

实验预先规定三类否定条件。在保守边界成立的测试中出现任一 C1–C4 违约，说明当前可行性处理不足；模型预测可行而半实物交接失败，说明状态增长、链路或协议边界需要修正；在高 CPU 负载、高状态增长和低返航余量场景中，FG-HPPO 若不能优于解耦或短视方法，且与 Case 1 离线上界保持较大差距，则不能支持其在强耦合条件下具有调度优势的假设。

## 附录 A：新颖性边界与模型风险

### A.1 与相邻研究方向的边界

本文的核心问题是电池轮换期间的有状态服务连续性。传统虚拟机或容器在线迁移主要处理计算状态在固定基础设施之间的复制，本文场景还包含移动源机的返航能量约束和多个交接事件共享的 A2A 资源。无人机持续覆盖与替换研究主要描述通信服务关系的延续，本文进一步刻画任务执行引起的状态增长、预拷贝和停机拷贝。相较于 MEC 服务迁移研究，本文将迁移完成时刻与电池安全离场边界直接关联。

本文的新颖性比较范围限定为第 II 节所综述的无人机 MEC、持续替换和服务迁移研究。虚拟机与容器预拷贝、移动云状态迁移和容错实时调度提供可复用的状态复制机制，但不作为本文主张研究优先性的依据。

### A.2 主要假设与失败风险

模型依赖四项关键条件：状态增长率能够由离线测量给出保守上界；A2A 速率存在可用于调度的下界；服务镜像已预置在替补机上；源机与替补机不会同时失效。任一条件长期不成立，都需要扩展当前状态模型，而不能仅通过重新训练 FG-HPPO 解决。

学习算法的主要风险包括训练分布不能覆盖实际并发模式、候选掩码过于保守、可行性投影频繁大幅修改策略输出、后续可行集变为空集以及分布外状态下价值估计失真。实验应分别报告掩码删除比例、投影距离、投影不可行率、应急机制触发率和失败原因，以区分策略学习问题与模型边界失效。

### A.3 简化场景

单区域、两架无人机和一个持续业务流构成本文模型的基本特例。该场景不包含多区域之间的 A2A 带宽竞争，决策仅包括暂停时刻、CPU 和 A2A 带宽，但仍保留状态增长、停机中断和返航储备之间的耦合关系。该特例可用于验证状态递推和交接协议，再与多区域并发实验区分单事件机制收益和共享资源调度收益。

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

[13] F. Mou, J. Lou, Z. Tang, Y. Wu, W. Jia, Y. Zhang, and W. Zhao, “Adaptive digital twin migration in vehicular edge computing and networks,” *IEEE Trans. Veh. Technol.*, vol. 74, no. 3, pp. 4839–4854, Mar. 2025.

[14] X. Zhang, C. Wang, Y. Zhu, J. Cao, and T. Liu, “Multi-agent deep reinforcement learning with trajectory prediction for task migration-assisted computation offloading,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 7, pp. 5839–5856, Jul. 2025.

[15] N. Zhao, Z. Ye, Y. Pei, Y.-C. Liang, and D. Niyato, “Multi-agent deep reinforcement learning for task offloading in UAV-assisted mobile edge computing,” *IEEE Trans. Wireless Commun.*, vol. 21, no. 9, pp. 6949–6960, Sep. 2022.

[16] C. Huang, G. Chen, P. Xiao, Y. Xiao, Z. Han, and J. A. Chambers, “Joint offloading and resource allocation for hybrid cloud and edge computing in SAGINs: A decision assisted hybrid action space deep reinforcement learning approach,” *IEEE J. Sel. Areas Commun.*, vol. 42, no. 5, pp. 1029–1043, May 2024.

[17] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” arXiv:1707.06347, 2017.

[18] J. Achiam, D. Held, A. Tamar, and P. Abbeel, “Constrained policy optimization,” in *Proc. 34th Int. Conf. Mach. Learn. (ICML)*, vol. 70, pp. 22–31, 2017.

[19] A. Stooke, J. Achiam, and P. Abbeel, “Responsive safety in reinforcement learning by PID Lagrangian methods,” in *Proc. 37th Int. Conf. Mach. Learn. (ICML)*, vol. 119, pp. 9133–9143, 2020.
