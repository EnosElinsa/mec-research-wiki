# 电池轮换场景下无人机移动边缘计算有状态服务交接的终端可行性与在线调度

## I. 引言

移动边缘计算（mobile edge computing，MEC）把计算资源部署到网络边缘，使图像分析、设施巡检和环境感知等时延敏感业务能够就近处理 [1]–[3]。当地面设施受损、覆盖不足或无法快速部署时，搭载计算模块的无人机（unmanned aerial vehicle，UAV）可以临时提供无线接入和边缘计算。受机载电池限制，持续时间超过单机续航的任务需要安排 UAV 返航补能或由其他 UAV 接替 [4], [6]。

UAV 接替可以延续覆盖和计算能力，却不一定能够延续有状态服务的处理结果。对于相互独立的请求，替补 UAV 部署相同程序后即可处理后续请求；对于目标跟踪、事件处理和流式分析等服务，后续请求还可能依赖此前已经确认的状态 [7]。如果这些状态没有一同交接，替补 UAV 可能重复处理请求、丢失已确认结果或从错误版本继续运行。因此，持续服务不仅需要替换飞行平台，还需要把影响后续处理的运行状态交给替补 UAV，并让后续请求只在这份状态基础上继续确认和写入。

按照交接期间源服务是否继续处理请求，现有有状态迁移可以分为停服迁移和在线迁移。停服迁移先停止源服务，再传输状态并在替补节点恢复；在线迁移则让源服务继续处理请求，先传输大部分状态，最后再同步停止前产生的更新 [8], [9], [12], [16]。在线迁移更适合连续服务，但处理期间产生的新状态也必须继续同步。现有模型通常把这些更新表示为脏页、外部输入或预先标定的迁移量，尚未同时处理请求完成量、状态生成和 UAV 返航之间的关系。

电池轮换使上述关系必须在同一个交接窗口内处理。面向低电量 UAV 的有状态微服务迁移已经给出镜像预置、A2A 检查点传输、替补恢复和源 UAV 返站的完整流程 [10]；真实任务队列上的迁移与资源控制 [24]、处理进度相关的 UAV 任务迁移 [26] 以及动作前返航能量检查 [19] 也分别已有研究。现有证据因而不能支持“首次研究 UAV 有状态迁移”或“首次让处理进度影响迁移量”这类宽泛主张。仍需研究的是：当源 UAV 完成并确认请求会产生替补必须继承的跨请求状态时，继续处理请求是否会使交接在最晚开始返航时刻前变得不可完成。

本文研究一次替补 UAV 已经选定的电池轮换交接。替补 UAV 到达前，系统预先部署应用镜像、模型和基础检查点；替补到达后，源 UAV 一边处理请求，一边通过空空（air-to-air，A2A）链路传输基础检查点之后产生的必要状态。控制器随后选择停止源端处理的时隙，完成最后一次状态传输、状态载入、版本确认和连接重定向，再让后续请求改由替补 UAV 确认和写入。替补 UAV 能够从源 UAV 最后确认的结果继续服务，并且源 UAV 仍有足够电量沿既定路线返航时，本次交接完成。

这一交接要求控制器联合决定源 UAV 的请求处理量、A2A 状态传输资源和停止处理时隙。提高中央处理器（central processing unit，CPU）频率可以减少等待请求，却可能产生更多未同步状态，并消耗原本可用于状态传输和返航的电量；过早停止处理则可能使请求队列溢出。本文只考虑能够把已确认更新序列化、去重和排序，且这些更新在短交接窗口内不可丢弃或覆盖的流式服务。对这类服务，当前动作满足 CPU、带宽和电量约束，并不代表后续仍能按时完成全部交接步骤。

模型预测控制能够根据队列、未同步状态、信道和电量的最新观测滚动调整资源，但其当前动作还需要保留一条通往完整交接的后续可行路径 [15]。为此，本文构造终端可行性感知鲁棒模型预测控制（terminal-feasibility-aware robust model predictive control，TF-RMPC）：控制器在交接准入时筛选可行的停止处理时隙，随后固定所选时隙，并在每一时隙求解包含队列上限、最终状态同步和返航电量条件的凸子问题。任务到达、状态生成、A2A 传输和能耗使用预先校准的保守边界；实际过程超出这些边界时，控制器撤回模型内保证并转入预设的停止处理、返航或上层恢复流程。

本文的主要贡献概括如下：

1. 建立面向跨请求持久状态的电池轮换交接模型，以预置基础检查点和窗口内不可丢弃的增量记录界定可迁状态，并按时隙刻画请求处理、未同步状态和返航电量之间的关系。
2. 推导交接前的显式终端可行条件，以保守队列、状态和能量递推统一约束请求缓存、完整状态交接和安全返航；在分段仿射边界下，该条件可由有限时域凸二次规划检验。
3. 设计 TF-RMPC，在每个时隙重求满足终端条件的 CPU 与 A2A 带宽动作，并给出基于计划移位的持续可行边界；实验首先检验处理量与新增必要状态之间的模型前提，再评价在线控制和少量并发交接扩展。

本文其余内容安排如下。第 II 节综述 UAV 补能与接替、有状态服务迁移以及队列与交接期限下的在线控制；第 III 节建立请求、状态、能量与交接可行模型；第 IV 节介绍 TF-RMPC 的停止时隙筛选、终端约束和滚动执行；第 V 节给出模型前提与控制方法的实验设计。研究阶段的全文证据、最近邻边界和模型风险集中记录在 [battery-rotation-uav-mec-research-foundation.md](battery-rotation-uav-mec-research-foundation.md)，待应用验证完成后再将必要内容纳入论文正文。

## II. 相关工作

与本文问题最相关的研究包括 UAV 续航条件下的服务接替、有状态服务迁移，以及队列与交接期限下的在线控制。前两条研究线分别说明飞行平台和运行状态如何延续，第三条研究线说明资源控制如何处理到达、迁移工作量和完成期限。

### A. UAV 续航与服务接替

按照补能前后是否仍由同一架 UAV 承担原任务，现有续航方法可以分为同机续作和多机接替。同机续作联合安排飞行速度、任务卸载和换电站访问，使同一架 UAV 补能后继续执行任务 [4]；动作前返航检查则根据当前动作能耗和下一位置的返航能耗决定 UAV 是否应中止任务 [19]。这类方法已经刻画任务执行与返航电量的关系，但不涉及运行状态在两架 UAV 之间的转移。

多机接替在一架 UAV 离场时由另一架 UAV 继续提供服务。轨迹与资源联合优化可以使满电 UAV 到达服务位置并让低电量 UAV 返回充电站，从而维持覆盖和吞吐率 [6]；在线多 UAV 服务迁移还可以根据用户移动联合调整服务 UAV 和飞行轨迹 [20]。UAV 辅助 MEC 也可以把待处理任务缓存、迁移、轨迹和 A2A 带宽放在同一个资源问题中，但迁移对象仍是任务而不是运行状态 [25]。此外，UAV 文献中的 service placement 可能指应用、运行库和数据库的静态部署 [27]，service hand-off 也可能指不同服务商之间的区域责任转移 [28]。这些研究覆盖了平台、任务或服务责任的接替，但没有直接给出跨请求运行状态的完整交接条件。

最接近本文场景的工作已经在低电量触发后预取容器镜像，并通过 A2A 链路传输最终检查点，使替补 UAV 恢复有状态微服务、源 UAV 返回补能站 [10]。电量感知的 UAV 微服务迁移也会在放置决策中预留飞往充电站所需的能量 [29]。前者证明电池轮换中的有状态微服务交接流程已经存在，后者证明返航能量能够进入微服务调度；两者均未联合控制交接窗口内的请求处理量、必要状态生成、A2A 传输和停止处理时隙。

### B. 有状态服务迁移

按照迁移工作量的形成方式，有状态迁移可以分为预先给定或标定的运行状态，以及迁移期间继续变化的运行状态。第一类模型以虚拟机内存、容器可写层、应用大小或服务数据量描述迁移对象，并联合配置带宽、迭代次数、放置或计算资源 [8], [9], [11], [12], [13], [17], [21], [22], [23]。这些工作已经覆盖内存与脏页迁移、容器分层、连接保持、有状态/无状态微服务编排、服务实例中的运行数据和用户上下文，以及迁移能耗；其优化模型中的迁移量通常由配置、测量或外部参数给出。

第二类模型显式处理迁移期间产生的数据。应用辅助视频分析把状态划分为永久、关键和可重放部分，源端在同步期间继续处理帧，但关键跟踪状态采用会覆盖旧值的有限窗口 [7]；ReSync 在检查点后复制新到输入并在目的端按序回放，其增量由外部输入到达产生 [16]；AIGC 上下文迁移允许控制器少迁移历史内容，并以推理准确率下降计价 [18]。这些机制分别适合可覆盖状态、外部输入回放和可舍弃上下文，不能直接等同于由已完成并确认请求产生、且后续请求必须完整继承的跨请求状态。

UAV 任务与服务迁移进一步缩小了本文可以主张的边界。TOM 已联合优化有状态服务迁移、任务卸载和 UAV 轨迹，但迁移工作量由固定虚拟机内存给出 [5]；CTMiG 根据单个任务的执行进度迁移剩余输入和部分结果，已经覆盖“处理进度改变迁移工作量” [26]；电池轮换中的有状态微服务恢复流程也已由 [10] 给出。因此，本文只研究跨多个请求持续存在、在交接窗口内不能丢弃或被后续记录覆盖的必要状态，并要求真实应用实验先验证这类状态及其增量模型。

### C. 终端约束在线控制

队列、资源和交接期限的在线控制已经覆盖本文问题的多个组成部分。OSHM 在固定迁移数据量下联合处理网络排队、交接期限和逐基站传输能量预算 [14]；OASTR 在真实任务队列上联合决定服务迁移或任务重路由、CPU、带宽和长期平均能耗 [24]；Energy-Aware 方法在执行动作前检查下一位置的返航能量 [19]。这些方法能够处理期限、队列、资源和能量，但迁移工作量仍由给定服务数据、应用大小或当前动作之外的过程确定，也没有要求一次 UAV 交接同时完成状态载入、版本确认、连接重定向和后续请求写入方切换。

模型预测控制在每个采样时刻求解有限时域问题，只执行首个动作并根据下一状态重新规划，适合直接处理硬状态和输入约束 [15]。其持续可行性需要由终端条件、计划移位和不确定性边界建立，而不是由惩罚项或单步资源检查推出。本文据此把等待请求、未同步状态、完整交接步骤和返航电量写入同一有限时域问题；与既有工作相比，待验证的区别仅在于当前请求处理动作会改变后续必须传输的跨请求状态，并由此改变交接能否按时完成。

## III. 系统模型与问题建模

本文沿用多区域、多 UAV、集中控制和分时隙运行的 UAV-MEC 架构 [1]–[3]。区域部署、用户关联、任务上行、安全航路和轮换触发由上层规划器给出，本文研究轮换事件触发后的服务运行过程。一次交接依次经历替补到达、增量状态预传、停止源端处理、最终同步、状态载入、版本确认、连接重定向、后续请求写入方切换和源 UAV 返航。下文按照这一过程建立系统描述、任务处理、有状态服务交接和能量消耗模型，最后给出在线优化问题。

### A. 系统描述

系统由多个服务区域、UAV 和业务会话组成，轮换窗口内的交接决策由集中控制器下发。三类对象的集合分别记为

$$
\mathcal R=\{1,\ldots,R\},\qquad
\mathcal U=\{1,\ldots,U\},\qquad
\mathcal I=\{1,\ldots,I\}.
$$

会话 $i\in\mathcal I$ 位于区域 $r(i)\in\mathcal R$，并由该区域当前的服务 UAV 处理。区域 $r$ 的会话集合记为 $\mathcal I_r=\{i\in\mathcal I:r(i)=r\}$。正常运行时，每个区域恰有一架服务 UAV，其余满足起飞条件的 UAV 在基地待命，因此持续轮换要求 $U>R$。

时间被划分为长度为 $\Delta$ 秒的时隙。若时隙 $\tau$ 有 UAV 接近返航能量边界，控制器开启包含 $T_{\mathrm w}$ 个时隙的交接窗口

$$
\mathcal W_\tau=\{\tau,\ldots,\tau+T_{\mathrm w}-1\},
$$

本文先研究一个交接窗口内的一次轮换事件 $n$。其区域和源 UAV 分别记为 $r_n$ 和 $u_n$，源 UAV 必须开始返航的最晚绝对时刻为 $d_n^{\mathrm{dep}}$。上层轮换器根据待命状态、安全航路和到达时间，从候选集合 $\mathcal V_n$ 中给出本次使用的替补 UAV $v_n$；其到达时隙 $t_n^{\mathrm{arr}}$ 是主问题的已知输入。该边界把“选择哪架替补”与“替补到达后如何完成状态交接”分开，使主问题只决定停止源端处理的时隙 $c_n\in\mathcal W_\tau$、CPU 和 A2A 带宽。多个候选可以逐一代入主问题比较，多事件排他匹配则在第 V-D 节作为扩展评价。

替补到达后，A2A 链路即可用于状态同步；是否实际传输以及传输多少由逐时隙带宽决定。可选停止处理时隙还必须满足

$$
t_n^{\mathrm{arr}}<c_n<\tau+T_{\mathrm w},
\qquad
(c_n+1)\Delta\le d_n^{\mathrm{dep}}.
$$

区域 $r$ 在时隙 $t$ 开始时的合法服务所有者记为 $o_r[t]$。窗口开始时有 $o_{r_n}[\tau]=u_n$；确认成功前，源 UAV 始终保有唯一提交权。源 UAV 在时隙 $c_n$ 停止处理请求并完成最终同步，替补 UAV 随后载入状态、核对版本并完成连接重定向；确认成功后，所有者在时隙 $c_n+1$ 更新为 $v_n$，源 UAV 同时进入返航模式。

在普通时隙开始时，控制器先观察任务队列、当期到达、未同步状态量、电量和当前信道，再决定 CPU 与 A2A 带宽。随后，A2A 链路发送槽首已经封存的状态，CPU 同时处理任务；本槽计算产生的新状态在槽末封存，并与能量状态一同更新。停止处理时隙 $c_n$ 不再处理请求，只执行最终同步、状态载入、版本确认、连接重定向和接管确认。该事件顺序保证控制决策不使用动作执行后才实现的信息。

### B. 任务处理模型

任务处理模型描述服务运行产生计算结果和新状态之前的队列变化。令 $Q_i[t]$ 表示时隙 $t$ 开始、接纳当期到达之前的任务积压，令 $A_i[t]$ 表示槽首已经完成上行的数据量，二者单位均为 bit。初始队列 $Q_i[\tau]$ 在窗口开始时可观测，未来到达在相应时隙开始前未知。

令 $\phi_i$ 表示处理 1 bit 数据所需的 CPU 周期数，$f_i[t]$ 表示分配给会话 $i$ 的 CPU 频率。为表示停止处理槽，定义

$$
a_i^{\mathrm{cmp}}[t]
=
\begin{cases}
0,&r_n=r(i),\ t=c_n,\\
1,&\text{其他情况}.
\end{cases}
$$

时隙 $t$ 实际处理的数据量为

$$
\mu_i[t]
=
\min\left\{
Q_i[t]+A_i[t],
\frac{a_i^{\mathrm{cmp}}[t]f_i[t]\Delta}{\phi_i}
\right\},
$$

相应的槽末队列为

$$
Q_i[t+1]
=
Q_i[t]+A_i[t]-\mu_i[t].
$$

无人机 $u$ 的最大总 CPU 频率为 $F_u^{\max}$，会话 $i$ 的缓存上限为 $Q_i^{\max}$。CPU 分配必须满足

$$
0\le f_i[t]
\le a_i^{\mathrm{cmp}}[t]F_{o_{r(i)}[t]}^{\max},
\qquad
\sum_{i:o_{r(i)}[t]=u}f_i[t]\le F_u^{\max},
$$

并保持

$$
Q_i[t+1]\le Q_i^{\max}.
$$

停止处理指示使交接区域的 CPU 分配自动为零。提高 CPU 频率可以减少任务积压，但处理更多任务也会产生更多需要交接的运行状态。

### C. 有状态服务交接模型

本文只对能够通过应用接口完整序列化的增量状态记录建模。应用镜像、模型参数、运行库和基础检查点预先部署在替补 UAV 上；能够从保留输入重放的临时状态不参与同步 [7], [16]。源服务把尚未并入基础检查点、且接管后维持应用语义所必需的更新写入 write-ahead log。状态记录在本窗口内只追加，不因后续覆盖、压缩或检查点合并而从待同步对象中消失；不能满足该条件的应用不属于当前模型。

令 $W_n[t]\ge0$ 表示时隙 $t$ 的请求处理完成后新增并封存的必要状态量。其真实值可以随输入内容和应用阶段变化，本文不把它预设为严格线性函数，而要求应用标定给出分段仿射上界。为简化记号，在一个标定区间内写为

$$
0\le W_n[t]\le \overline W_n[t](\boldsymbol\mu[t])
=
\mathbb 1\{t<c_n\}
\left(
\overline W_n^{\mathrm{bg}}[t]
+
\sum_{i\in\mathcal I_{r_n}}
\overline\eta_{ni}[t]\mu_i[t]
\right),
$$

其中 $\overline W_n^{\mathrm{bg}}[t]\ge0$ 是与任务处理量无关的状态写入上界，$\overline\eta_{ni}[t]\ge0$ 是单位处理量的保守增量系数。两者只用训练/校准轨迹拟合，并在最终测试前冻结。$W_n[t]$ 到槽末才可观测，因而只能从下一时隙开始传输；停止处理槽不再处理请求，也不产生新状态。

令 $G_n[\tau]\ge0$ 表示窗口开始时尚未同步到替补 UAV 的必要状态量。由于基础检查点已经预置，$G_n[\tau]$ 不包含镜像、模型或运行库；若这些对象不能预置，其传输时间和能量必须另行加入模型。事件 $n$ 在时隙 $t$ 获得的 A2A 带宽为 $b_n[t]$，系统总带宽为 $B^{\mathrm A}$。令 $h_n[t]$ 和 $P_n^{\mathrm A}$ 分别表示源 UAV 与已选替补 UAV 之间的信道功率增益和发射功率，$N_0$ 为噪声功率谱密度。实际 A2A 速率为

$$
C_n^{\mathrm A}[t]
=
b_n[t]\log_2\left(
1+
\frac{P_n^{\mathrm A}h_n[t]}
{N_0b_n[t]}
\right),
$$

其中 $b_n[t]=0$ 时定义 $C_n^{\mathrm A}[t]=0$。带宽只能在替补到达后至停止处理槽（含该槽）分配，并满足

$$
0\le b_n[t]\le
B^{\mathrm A}
\mathbb 1\{t_n^{\mathrm{arr}}\le t\le c_n\}.
$$

在 $t_n^{\mathrm{arr}}\le t<c_n$ 的预传阶段，A2A 链路只能发送槽首已经封存的数据。实际发送量和下一时隙的未同步量分别为

$$
L_n[t]
=
\min\left\{
G_n[t],
C_n^{\mathrm A}[t]\Delta
\right\},
$$

$$
G_n[t+1]
=
\left[G_n[t]-C_n^{\mathrm A}[t]\Delta\right]^+
+W_n[t].
$$

该递推与 $L_n[t]$ 的定义等价，并明确表示本槽计算产生的 $W_n[t]$ 只能从下一时隙开始传输。源 UAV 在时隙 $c_n$ 开始时停止处理请求，最终需要传输的数据量为

$$
D_n^{\mathrm{stop}}
=
G_n[c_n]+D_n^{\mathrm{meta}},
$$

其中 $D_n^{\mathrm{meta}}>0$ 是状态版本、连接重定向和所有权确认所需的协议元数据。

源 UAV 停止处理请求后，系统依次完成状态记录冻结、最终状态传输、替补端状态载入、版本确认、连接重定向和接管确认。除最终状态传输外，相应固定时间分别为 $\tau_n^{\mathrm{freeze}}$、$\tau_n^{\mathrm{apply}}$、$\tau_n^{\mathrm{verify}}$、$\tau_n^{\mathrm{redir}}$ 和 $\tau_n^{\mathrm{ack}}$，其总和为

$$
\tau_n^{\mathrm{fix}}
=
\tau_n^{\mathrm{freeze}}
+
\tau_n^{\mathrm{apply}}
+
\tau_n^{\mathrm{verify}}
+
\tau_n^{\mathrm{redir}}
+
\tau_n^{\mathrm{ack}}.
$$

事件 $n$ 的协议完成时间为

$$
T_n^{\mathrm{proto}}
=
\tau_n^{\mathrm{fix}}
+
\frac{D_n^{\mathrm{stop}}}
{C_n^{\mathrm A}[c_n]},
$$

其中 $C_n^{\mathrm A}[c_n]=0$ 时规定 $T_n^{\mathrm{proto}}=+\infty$。本文采用整槽交接：源 UAV 在 $c_n\Delta$ 停止处理请求，唯一更新权只在下一时隙开始时切换。因此业务中断为一个时隙，并要求 $\Delta\le I_n^{\max}$。

最终同步对链路下降和状态预测误差的容忍程度由交接余量表示：

$$
M_n
=
\left(
\Delta-\tau_n^{\mathrm{fix}}
\right)
C_n^{\mathrm A}[c_n]
-
D_n^{\mathrm{stop}}.
$$

$M_n\ge0$ 与 $T_n^{\mathrm{proto}}\le\Delta$ 等价。主模型要求替补先到达、固定协议阶段短于一个时隙、业务中断不超过上限，并使协议在源 UAV 最晚开始返航时刻前完成：

$$
t_n^{\mathrm{arr}}<c_n<\tau+T_{\mathrm w},
\qquad
(c_n+1)\Delta\le d_n^{\mathrm{dep}},
\qquad
\tau_n^{\mathrm{fix}}<\Delta\le I_n^{\max}.
$$

确认和所有权切换采用单写者协议。确认返回前，源 UAV 保留唯一提交权，替补只保存未提交副本；只有必要状态已经载入、版本检查通过、连接已经重定向，且确认在固定的 $\tau_n^{\mathrm{ack}}$ 内返回时，才有 $o_{r_n}[c_n+1]=v_n$。若任一步骤失败或确认超时，替补丢弃未提交副本，源 UAV 按保留的返航电量立即返航。确认丢包、控制链故障和交接后的业务重建作为协议异常单独统计，不进入状态生成与资源调度的创新主张。

### D. 能量消耗模型

完成状态交接并安全返航还受到 UAV 电量限制。令 $P_u^{\mathrm{mode}}[t]$ 表示 UAV $u$ 的飞行、悬停和航电功率，$\kappa_u$ 表示 DVFS 计算能耗系数。事件 $n$ 的数据无线电开启时间为

$$
\ell_n[t]
=
\begin{cases}
L_n[t]/C_n^{\mathrm A}[t],
&t_n^{\mathrm{arr}}\le t<c_n,\
C_n^{\mathrm A}[t]>0,\\[1mm]
\displaystyle
\min\left\{
\frac{D_n^{\mathrm{stop}}}
{C_n^{\mathrm A}[c_n]},
\left[
\Delta-\tau_n^{\mathrm{fix}}
\right]^+
\right\},
&t=c_n,\
C_n^{\mathrm A}[c_n]>0,\\[2mm]
0,&\text{其他情况}.
\end{cases}
$$

对选定的源—替补 UAV 对，令 $P_{un}^{\mathrm A,\mathrm{data}}[t]$ 表示端点 $u\in\{u_n,v_n\}$ 的数据无线功率，令 $E_{un}^{\mathrm{A,fix}}$ 表示冻结、载入、版本确认、连接重定向和接管确认产生的固定能耗。对应的 A2A 能耗为

$$
E_u^{\mathrm A}[t]
=
\mathbb 1\{u\in\{u_n,v_n\}\}
\left(
P_{un}^{\mathrm A,\mathrm{data}}[t]\ell_n[t]
+
\mathbb 1\{t=c_n\}
E_{un}^{\mathrm{A,fix}}
\right).
$$

UAV $u$ 在时隙 $t$ 的总能耗为

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
E_u^{\mathrm A}[t].
$$

若 $E_u[t]$ 是槽首剩余电量，则槽末电量更新为

$$
E_u[t+1]
=
E_u[t]-E_u^{\mathrm{use}}[t].
$$

令 $E_u^{\mathrm{ret}}[t]$ 表示 UAV $u$ 从当前状态沿安全航路返回补能点所需的能量，$E_u^{\mathrm{res}}$ 表示安全余量，$E_n^{\mathrm{abort}}$ 表示事件 $n$ 失败后封存记录和切换返航的能量上界。所有仍在空中的 UAV 都必须满足

$$
E_u[t+1]
\ge
E_u^{\mathrm{ret}}[t+1]
+
E_u^{\mathrm{res}}
+
\mathbb 1\{u=u_n,\ t=c_n\}
E_n^{\mathrm{abort}}.
$$

最后一项只在源 UAV 的停止处理槽预留，因此同一约束同时覆盖正常返航和确认失败后的中止返航。

### E. 问题建模

基于上述模型，主问题在已知源 UAV、替补 UAV 和到达时隙的条件下，联合决定停止处理时隙以及逐槽 CPU 与 A2A 带宽。令 $\boldsymbol S[t]$ 表示由任务队列、未同步状态量、UAV 电量、当前信道和协议阶段组成的槽首状态。窗口开始时选择

$$
c_n\in\mathcal C_\tau
=
\left\{
c\in\mathbb Z:
t_n^{\mathrm{arr}}<c<\tau+T_{\mathrm w},
\ (c+1)\Delta\le d_n^{\mathrm{dep}}
\right\},
$$

并在每个 $t<c_n$ 根据当前可观测状态产生资源动作

$$
\boldsymbol a[t]
=
(\boldsymbol f[t],b_n[t]).
$$

未来任务到达、状态写入和信道只能在实现后进入 $\boldsymbol S[t+1]$。确认结果属于协议层异常，不作为控制器在槽首可预知的随机动作变量。

终端可行性通过一个可直接求解的保守计划定义。校准阶段为未来时隙给出任务到达上界 $\overline A_i[k]$、第 III-C 节的状态写入上界 $\overline W_n[k]$、满槽可靠传输量下界 $\underline s_n[k](b)$ 和能耗上界 $\overline E_u^{\mathrm{use}}[k]$，使

$$
A_i[k]\le\overline A_i[k],\qquad
C_n^{\mathrm A}[k]\Delta\ge\underline s_n[k](b_n[k]),
\qquad
E_u^{\mathrm{use}}[k]\le\overline E_u^{\mathrm{use}}[k]
$$

在声明的应用、负载和信道范围内成立。$\underline s_n[k](b)$ 由 Shannon 传输量在有限带宽分段上的弦线构成，因此是保守的凹分段仿射函数；$\overline E_u^{\mathrm{use}}[k]$ 对 CPU 能耗使用凸分段仿射上界。所有边界在最终测试前冻结。

在时隙 $t$ 和候选停止处理时隙 $c\in\mathcal C_\tau$ 下，令 $\mathsf F_t(c)$ 表示以下计划变量的可行域：

$$
\widehat{\boldsymbol z}_t(c)
=
\left\{
\widehat f_i[k],\widehat b_n[k],
q_i[k],g_n[k]
\right\}_{k=t}^{c}.
$$

队列预测从当前观测开始，并按到达上界递推：

$$
q_i[t]=Q_i[t],\qquad
\widehat\mu_i[k]
=
\frac{\widehat f_i[k]\Delta}{\phi_i},
$$

$$
0\le\widehat\mu_i[k]
\le q_i[k]+\overline A_i[k],
\qquad
q_i[k+1]
=
q_i[k]+\overline A_i[k]-\widehat\mu_i[k]
\le Q_i^{\max},
$$

其中 $k=t,\ldots,c-1$，且 $\widehat f_i[c]=0$。CPU 总量满足第 III-B 节的容量约束。未同步状态量上界从 $g_n[t]=G_n[t]$ 开始，并满足

$$
g_n[k+1]
\ge
g_n[k]-\underline s_n[k](\widehat b_n[k])
+\overline W_n[k](\widehat{\boldsymbol\mu}[k]),
$$

$$
g_n[k+1]\ge\overline W_n[k](\widehat{\boldsymbol\mu}[k]),
\qquad k=t,\ldots,c-1.
$$

第二个不等式对应预传清空槽首状态后，本槽新增状态仍只能留到下一槽。停止处理槽的最终同步必须满足

$$
g_n[c]+D_n^{\mathrm{meta}}
\le
\frac{\Delta-\tau_n^{\mathrm{fix}}}{\Delta}
\underline s_n[c](\widehat b_n[c]).
$$

同时，$0\le\widehat b_n[k]\le B^{\mathrm A}$，到达前带宽为零，并对每个 $u\in\{u_n,v_n\}$ 和 $k=t,\ldots,c$ 施加累计能量条件

$$
\sum_{j=t}^{k}
\overline E_u^{\mathrm{use}}[j]
\le
E_u[t]-E_u^{\mathrm{ret}}[k+1]-E_u^{\mathrm{res}}
-\mathbb 1\{u=u_n,\ k=c\}E_n^{\mathrm{abort}}.
$$

上述等式和不等式共同构成 $\mathsf F_t(c)$。由于状态写入和能量使用上界、传输使用凹下界，原始形式是凸可行性问题；采用前述分段仿射边界后，它由线性约束表示。因而，判断 $\mathsf F_t(c)$ 是否为空不再等价于重新求解一个未指定的随机控制问题，而是求解一个变量、约束和停止条件均明确的有限时域凸程序。

在可行域内，控制器权衡队列、能耗、带宽和最终同步余量。令

$$
\widehat M_n(c)
=
\frac{\Delta-\tau_n^{\mathrm{fix}}}{\Delta}
\underline s_n[c](\widehat b_n[c])
-g_n[c]-D_n^{\mathrm{meta}},
$$

则窗口开始时的问题为

$$
\begin{aligned}
\text{(P1)}\qquad
\min_{c\in\mathcal C_\tau,\,
\widehat{\boldsymbol z}_\tau(c)\in\mathsf F_\tau(c)}
\quad
&\sum_{k=\tau}^{c-1}
\left[
\lambda_Q\sum_{i\in\mathcal I_{r_n}}
\frac{q_i[k+1]}{Q_i^{\max}}
+\lambda_E\sum_{u\in\{u_n,v_n\}}
\frac{\overline E_u^{\mathrm{use}}[k]}{E_u[\tau]}
+\lambda_B\frac{\widehat b_n[k]}{B^{\mathrm A}}
\right]\\
&-\lambda_M
\frac{\widehat M_n(c)}{G_n[\tau]+D_n^{\mathrm{meta}}},
\end{aligned}
$$

其中 $\lambda_Q,\lambda_E,\lambda_B,\lambda_M\ge0$ 在校准阶段冻结。离散变量只有有限个停止处理时隙；枚举 $c$ 后，每个子问题都是凸程序，采用分段仿射边界和二次动作平滑项时可实现为二次规划。

该终端条件还给出递归可行性边界。若 $\mathsf F_t(c_n)$ 非空、当前执行其首个动作，且实际到达、状态写入、信道和能耗没有越过校准边界，则实际下一状态分别不劣于计划中的 $q_i[t+1]$、$g_n[t+1]$ 和剩余能量下界。删除已执行的首项后，原计划尾部仍属于 $\mathsf F_{t+1}(c_n)$；重复这一计划移位可使最终状态同步和后续协议步骤在停止处理槽内完成，并保留源 UAV 返航所需的电量和安全余量。该结论只覆盖已建模边界内的资源与状态过程，不覆盖确认丢包、软件错误或未建模链路故障。

## IV. TF-RMPC 求解方法

问题 P1 的离散部分只有停止处理时隙，连续部分则在每个时隙随队列、未同步状态量和信道观测更新。TF-RMPC 先枚举有限个停止处理时隙并通过 $\mathsf F_\tau(c)$ 执行交接准入，再固定选中的 $c_n$ 滚动求解剩余 CPU 与 A2A 带宽。该方法不把模型预测控制本身写成创新；其场景特定部分是把“任务处理产生新增必要状态”与“最晚开始返航前完成状态同步并保留返航电量”写成可求解的终端安全层。

### A. 总体框架

集中控制器在 $t=\tau$ 收集源/替补电量、候选到达时隙、当前任务队列、当前未同步状态量和校准边界。对每个 $c\in\mathcal C_\tau$，控制器建立第 III-E 节的 $\mathsf F_\tau(c)$ 并求解 P1；不可行的停止处理时隙直接删除。若至少有一个子问题可行，控制器选择目标值最小的 $c_n$ 和对应计划，向替补 UAV 发出交接准入指令；否则不启动该交接，并把候选更换或业务恢复交还上层轮换器。

一旦交接被准入，$c_n$ 在本窗口内固定。固定停止处理时刻避免控制器通过反复后移返航界限掩盖资源不足，也使第 III-E 节的计划移位能够直接建立递归可行性。每个后续时隙只更新已经实现的队列、未同步状态量、信道和电量，未实现量继续使用冻结的校准边界。

TF-RMPC 的输入是槽首状态和剩余边界，输出是当前槽的 $\boldsymbol f[t]$ 与 $b_n[t]$。控制器不需要训练网络、价值函数或未来真实轨迹；所有在线信息都在动作产生前可用。上层若给出多个候选替补，则分别计算其可行停止处理时隙和目标值，再选择一个候选，主问题本身不同时优化替补匹配。

### B. 终端安全动作生成

终端安全层把一个仅追求即时队列性能的资源提案转换为满足完整尾部计划的动作。令 $\widetilde{\boldsymbol a}[t]$ 表示由队列权重、当前信道和能量价格得到的名义动作；它可以来自简单的单槽优化，也可以由其他性能控制器给出，但不承担终端保证。给定动作尺度矩阵 $\boldsymbol D$，安全层求解

$$
\begin{aligned}
\text{(P2)}\qquad
\min_{\widehat{\boldsymbol z}_t(c_n)\in\mathsf F_t(c_n)}
\quad
&\rho_a
\left\|
\boldsymbol D^{-1}
\left(
\widehat{\boldsymbol a}[t]
-\widetilde{\boldsymbol a}[t]
\right)
\right\|_2^2\\
&+\sum_{k=t}^{c_n-1}
\left[
\lambda_Q\sum_{i\in\mathcal I_{r_n}}
\frac{q_i[k+1]}{Q_i^{\max}}
+\lambda_E\sum_{u\in\{u_n,v_n\}}
\frac{\overline E_u^{\mathrm{use}}[k]}{E_u[t]}
+\lambda_B\frac{\widehat b_n[k]}{B^{\mathrm A}}
\right]
-\lambda_M\widehat M_n(c_n),
\end{aligned}
$$

其中 $\widehat{\boldsymbol a}[t]=(\{\widehat f_i[t]\},\widehat b_n[t])$ 是计划的首个资源动作。二次项只要求在安全允许时接近名义提案；$\mathsf F_t(c_n)$ 才负责 CPU、队列、带宽、未同步状态终端量和返航电量约束。采用分段仿射状态写入、传输和能量边界后，P2 是具有线性约束和凸二次目标的二次规划。

安全层只执行 P2 的首个动作，余下变量是证明当前动作可延续到停止处理时刻的见证计划。下一时隙到来后，控制器用实际观测重建 P2，而不是机械执行旧计划。若实际过程严格优于保守边界，滚动优化可以释放多余资源；若实际过程贴近边界，计划会逐步把 CPU 限制到队列所需范围，并把更多 A2A 资源留给状态同步。

P2 的保证范围由 $\mathsf F_t(c_n)$ 中的约束决定。它保证校准边界内的队列、状态同步和返航电量，不保证边界外扰动、软件正确性或 ACK 可用性。若一个外部学习器提供 $\widetilde{\boldsymbol a}[t]$，学习器只影响二次距离和性能，不改变该边界，也不构成本文方法的必要组成。

### C. 滚动执行与回退

**算法 1：TF-RMPC 的交接准入与滚动执行**

**输入：** 第 III 节环境模型，源 UAV $u_n$，候选替补 $v_n$ 及到达时隙，冻结的任务、状态写入、信道和能量边界，代价权重与求解时限。

**输出：** 停止处理时隙 $c_n$，逐槽 CPU 动作 $\boldsymbol f[t]$ 与 A2A 带宽 $b_n[t]$，以及准入拒绝、正常完成或协议异常状态。

1. 在 $t=\tau$ 观察 $\boldsymbol S[\tau]$，构造 $\mathcal C_\tau$。
2. 对每个 $c\in\mathcal C_\tau$ 建立 $\mathsf F_\tau(c)$ 并求解 P1，删除不可行候选。
3. 若没有可行停止处理时隙，则拒绝启动交接并通知上层轮换器；否则选择目标值最小的 $c_n$，保存其计划作为热启动。
4. 对 $t=\tau,\ldots,c_n-1$，观察 $\boldsymbol S[t]$，更新剩余初始状态并求解 P2。
5. 执行 P2 的首个 $\boldsymbol f[t]$ 和 $b_n[t]$，在槽末记录实际 $A_i[t]$、$W_n[t]$、传输量和能耗，再滚动到下一时隙。
6. 在 $t=c_n$ 停止源端处理，按 P2 的终端带宽完成最终状态和元数据传输；替补载入状态、核对版本、完成连接重定向并返回 ACK 后更新所有权，源 UAV 开始返航。
7. 若实际量越过冻结边界或求解器未在时限内返回，停止使用递归可行性声明；控制器优先检查立即冻结是否仍可完成，不能完成时保留源端所有权并按协议进入安全返航和业务恢复流程。

步骤 2 是交接准入，步骤 4–5 是正常滚动路径，步骤 7 只处理模型边界失效。若边界成立且 P1 已准入，计划移位使 P2 在后续时隙保持可行，因此正常路径不需要依靠临时惩罚或未定义的搜索恢复动作。若实际边界失效，算法明确撤回保证并记录失败原因，而不是把协议异常计入优化器的可行性证明。

停止处理槽结束后，在线求解器不再参与状态恢复。替补 UAV 依据应用接口载入增量状态，完成版本核对和连接重定向；输出一致性由第 V-A 节的应用实验检验；源 UAV 的返航航路和补能由上层轮换器继续管理。由此，TF-RMPC 的执行边界止于“ACK 后所有权切换且源机保有返航所需电量和安全余量”。

### D. 复杂度分析

TF-RMPC 的在线开销由停止处理时隙枚举和二次规划组成。令 $H=c_n-t$ 表示剩余预传时隙数，$I_n=|\mathcal I_{r_n}|$，每槽连续资源动作维数为 $d=I_n+1$。P2 的变量和约束数量均随 $H(I_n+1)$ 线性增长；若分段仿射边界总共引入 $S$ 个附加片段约束，则可分别记为

$$
n_z=O\big(H(I_n+1)\big),
\qquad
n_c=O\big(H(I_n+1)+S\big).
$$

采用通用原始—对偶内点法时，一个 QP 的保守算术复杂度可写为 $O((n_z+n_c)^3\log(1/\epsilon))$，其中 $\epsilon$ 是求解容差；实际成本还取决于稀疏结构和求解器实现。窗口开始时最多求解 $|\mathcal C_\tau|$ 个 P1 子问题，停止处理时隙固定后每槽只求解一个 P2。相邻时隙的约束矩阵结构不变，上一槽的尾部计划可作为热启动。

该量级只说明扩展趋势，不能替代在线时延证据。第 V-D 节将以 batch size 为 1 测量建模、求解、状态记录和通信下发的完整链路，并分别报告不同预测时域、会话数和分段数下的 p50、p95、p99 时延及超时率。只有完整链路在声明硬件上持续小于 $\Delta$，才把相应规模称为可在线执行。

## V. 实验设计

本节按“模型前提—总体控制—机制消融—扩展与开销”的顺序验证三项贡献。第一组实验首先判断已确认请求量与新增必要状态之间是否存在可用于终端约束的稳定上界；只有该前提成立，后续控制比较才具有应用含义。第二组实验在单次交接主问题上比较 TF-RMPC 与参数化交接、固定状态量和无终端约束方法。最后通过消融、多候选/少量并发扩展和完整动作链时延，限定终端安全层的作用与可部署规模。

### A. 实验设置与状态交接验证

状态模型验证选取一个具体的流式边缘应用作为主对象，并实现“预置基础检查点 + 窗口内只追加必要状态记录”的应用接口。实验逐独立轨迹改变输入批量、CPU 频率和输入内容，记录每槽处理量 $\mu_i[t]$、新增状态量 $W_n[t]$、记录版本、序列化字节和处理阶段。拟合阶段分别比较线性、分段仿射和应用阶段相关上界；校准集用于选择分段和覆盖目标，最终保留测试集只检验经验覆盖、上界宽度及随负载变化的误差，不反向调整模型。

状态接口的正确性与状态量拟合分开验证。在可控带宽、时延和丢包条件下重放同一输入轨迹，逐输入比较无迁移运行与交接后运行的输出、去重结果、提交顺序、版本确认和服务世代，并记录最终同步量、停止处理时间、状态载入、连接重定向和 A2A 字节。任一保留轨迹出现语义不一致，都否定该应用上的当前接口；若 $W_n[t]$ 无法被有用的线性或分段仿射上界覆盖，则改用有界快照、应用阶段状态或传统脏页率模型，而不继续用惩罚项掩盖模型失配。

主问题采用三个由紧迫程度区分的单次交接实例，扩展问题另行标记：

| 测试实例 | 交接范围 | 主要变化 | 主要证据角色 |
| -------- | -------- | -------- | ------------ |
| Case 1 | 单事件、小会话集 | 宽松返航时限与稳定信道 | 建立离线参照并核对终端条件 |
| Case 2 | 单事件、中等会话集 | 任务负载、初始未同步状态和返航电量余量 | 比较正常在线控制 |
| Case 3 | 单事件、紧期限 | 信道下界与状态产生上界接近容量边界 | 暴露准入拒绝和保证边界 |
| Extension | 两至三个事件 | 候选替补和共享 A2A 竞争 | 只评价扩展开销与失败模式 |

任务、信道、初始未同步状态和初始电量轨迹划分为拟合、校准和最终测试三组；同一测试轨迹对所有方法配对复用。正式测试前冻结分段边界、代价权重、停止时刻候选、求解容差、时限和失败定义。物理违约、模型边界失配、准入拒绝、求解超时和协议 ACK 异常分别报告，不能合并为一个有利于方法的总失败率。

### B. 模型标定与总体性能

模型标定实验先回答第 III-E 节的保守边界是否既覆盖保留轨迹，又没有宽到使所有候选停止处理时隙均不可行。分别报告任务到达、状态写入、A2A 传输量和能耗边界的测试覆盖率、绝对/相对松弛量，以及由各边界单独造成的准入拒绝率。该实验只支持模型适用范围和保守程度，不用于比较控制方法。

总体性能实验比较五类方法：把交接时间作为固定输入的轮换基线、把状态量固定为窗口初值的 MPC、只满足当前槽约束的 Myopic-QP、采用相同预测边界但删除状态终端约束的 RMPC-Local，以及完整 TF-RMPC。Case 1 另给出使用完整未来轨迹的离线解，作为信息占优的参照而非在线竞争者。所有在线方法获得相同槽首观测、相同测试轨迹、相同动作范围和相同单槽计算时限。

主指标包括交接完成率、任务队列溢出率、最终未同步状态量、源/替补最小返航电量余量和单位完成任务能耗；辅助指标包括停止处理时刻、A2A 字节、带宽占用、状态载入与连接重定向时间、协议完成时间、准入拒绝和求解超时。结果分析先比较 Case 1–3 中的系统指标，再检查 TF-RMPC 的模型内预测与实际轨迹是否一致。只有边界内保留测试上的配对结果支持控制结论，ACK 丢包和软件故障只作为协议可靠性结果单列。

### C. 组件消融与决策行为

消融实验只回答三个与贡献直接对应的问题。`w/o Update Coupling` 把新增状态量固定为与 CPU 无关的外生过程，用于检验处理动作改变未来交接工作量是否会改变调度结果；`w/o Terminal Constraint` 只保留当前槽队列、带宽和能量约束，用于检验显式终端条件是否减少返航前无法完成的状态同步；`Nominal Boundary` 用条件均值替代保守上下界，用于检验边界保守性与物理违约之间的权衡。三个变体复用相同目标函数、停止时刻候选、求解器、测试轨迹和时限。

消融结果只把配对实验真正隔离的变化归因于相应组件。状态耦合对应 CPU、状态字节和任务队列之间的变化，终端约束对应最终状态余量与返航违约，保守边界对应准入率与边界外失败。再预先冻结一个 Case 2 轨迹，展示“槽首状态—名义动作—P2 修正—尾部计划—实际结果”的完整链条；该轨迹只解释机制，不替代跨实例统计。

### D. 少量并发扩展与在线开销

扩展实验先评价多个候选替补，而不改变单事件主问题。对每个候选分别计算可行停止处理时隙、目标值和在线开销，再比较上层按最小目标选择与最早到达、最大电量两种启发式。随后把两至三个交接事件放入共享 A2A 资源下，比较顺序准入与联合凸资源计划；只要联合问题不再满足第 III-E 节的单事件计划移位条件，就把结果标记为扩展经验，不沿用主问题的递归可行性声明。

在线开销实验测量 batch size 为 1 时的完整动作链，包括状态读取、边界实例化、停止处理时隙枚举、QP 建模、求解、记录和动作下发。报告不同预测时域、会话数、分段数和扩展事件数下的 p50、p95、p99 时延、峰值内存、热启动收益及超过 $\Delta$ 的时限违约率。若紧期限 Case 3 或并发扩展不能在单槽内稳定完成，则把可发表范围收缩到通过时限测试的会话数和事件数，不用渐近复杂度替代实测结论。


## 参考文献

[1] C. Peng, Y. Chen, X. Huang, Z. Wu, Y. Xu, and Y. Wu, “Demand-aware multi-area multi-UAV empowered mobile edge computing: A joint energy and delay optimization,” *IEEE Trans. Mobile Comput.*, early access, 2026, doi: 10.1109/TMC.2026.3697839.

[2] F. Pervez, A. Sultana, C. Yang, and L. Zhao, “Energy and latency efficient joint communication and computation optimization in a multi-UAV-assisted MEC network,” *IEEE Trans. Wireless Commun.*, vol. 23, no. 3, pp. 1728–1741, Mar. 2024.

[3] Z. Sun, G. Sun, Q. Wu, L. He, S. Liang, H. Pan, D. Niyato, C. Yuen, and V. C. M. Leung, “TJCCT: A two-timescale approach for UAV-assisted mobile edge computing,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 4, pp. 3130–3147, Apr. 2025.

[4] D. Ye, Z. Sun, W. Zhong, J. Kang, X. Huang, D. I. Kim, S. Xie, and C. Yuen, “Optimal flight speed scheduling and battery swapping in UAV-enabled mobile edge computing,” *IEEE Trans. Mobile Comput.*, vol. 25, no. 1, pp. 948–960, Jan. 2026.

[5] Q. Qiu, L. Li, Z. Xiao, Q. Lin, L. Ma, and Z. Ming, “TOM: Joint trajectory, offloading and migration optimization in stateful service-oriented UAV-enabled VEC system,” *IEEE Trans. Serv. Comput.*, vol. 18, no. 6, pp. 4261–4275, Nov.–Dec. 2025.

[6] N. Gupta, S. Agarwal, D. Mishra, and B. Kumbhani, “Trajectory and resource allocation for UAV replacement to provide uninterrupted service,” *IEEE Trans. Commun.*, vol. 71, no. 12, pp. 7288–7302, Dec. 2023, doi: 10.1109/TCOMM.2023.3307559.

[7] C. Rong, J. H. Wang, J. Wang, Y. Zhou, and J. Zhang, “Live migration of video analytics applications in edge computing,” *IEEE Trans. Mobile Comput.*, vol. 23, no. 3, pp. 2078–2092, Mar. 2024.

[8] A. Calagna, Y. Yu, P. Giaccone, and C. F. Chiasserini, “Design, modeling, and implementation of robust migration of stateful edge microservices,” *IEEE Trans. Netw. Service Manag.*, vol. 21, no. 2, pp. 1877–1893, Apr. 2024, doi: 10.1109/TNSM.2023.3331750.

[9] A. Calagna, Y. Yu, P. Giaccone, and C. F. Chiasserini, “MOSE: A novel orchestration framework for stateful microservice migration at the edge,” *IEEE Trans. Netw. Service Manag.*, vol. 22, no. 5, pp. 4827–4841, 2025, doi: 10.1109/TNSM.2025.3579051.

[10] S. Frejo-Martín, A. García-López, J. M. Murillo, and J. Galán-Jiménez, “Live migration of stateful microservices in UAV-assisted networks for enhanced availability,” in *Proc. IEEE Symp. Comput. Commun. (ISCC)*, 2025, pp. 1–6, doi: 10.1109/ISCC65549.2025.11325941.

[11] H. Zhang, S. Wu, H. Fan, Z. Huang, W. Xue, C. Yu, S. Ibrahim, and H. Jin, “KubeSPT: Stateful pod teleportation for service resilience with live migration,” *IEEE Trans. Serv. Comput.*, vol. 18, no. 3, pp. 1500–1514, May–Jun. 2025.

[12] L. Ma, S. Yi, N. J. Carter, and Q. Li, “Efficient live migration of edge services leveraging container layered storage,” *IEEE Trans. Mobile Comput.*, vol. 18, no. 9, pp. 2020–2033, Sep. 2019.

[13] M. Adeppady, Y. Yu, A. Rahmanian, A. A.-E. Hassan, and C. F. Chiasserini, “Efficient management of composite heterogeneous applications at the network edge,” *IEEE Trans. Netw. Service Manag.*, early access, 2026.

[14] N. Sharghivand, L. Mashayekhy, W. Ma, and S. Dustdar, “Time-constrained service handoff for mobile edge computing in 5G,” *IEEE Trans. Serv. Comput.*, 2023.

[15] D. Q. Mayne, J. B. Rawlings, C. V. Rao, and P. O. M. Scokaert, “Constrained model predictive control: Stability and optimality,” *Automatica*, vol. 36, no. 6, pp. 789–814, Jun. 2000, doi: 10.1016/S0005-1098(99)00214-9.

[16] R. Scheuer, Y. Pi, and X. Wang, “ReSync: Coordinated live-migration for stateful containers in mobile edge computing,” *IEEE Trans. Mobile Comput.*, early access, 2026.

[17] A. Calagna, S. Maxenti, L. Bonati, S. D’Oro, T. Melodia, and C. F. Chiasserini, “CORMO-RAN: Energy efficiency at the near-RT RIC via lossless migration of O-RAN xApps,” *IEEE Trans. Mobile Comput.*, early access, 2026.

[18] J. Wang, Y. Hao, R. Wang, L. Hu, K. Huang, D. Niyato, and M. Chen, “Context-aware AIGC service migration in edge intelligence networks via Transformer DRL,” *IEEE Trans. Serv. Comput.*, early access, 2026.

[19] J. Mei, J. Xu, Z. Tong, and K. Li, “Energy-aware multi-UAV collaboration for data collection and trajectory planning with MADDPG,” *IEEE Trans. Netw. Service Manag.*, early access, 2026.

[20] W. Feng, W. Gao, J. Yao, L. Zhou, C. Yan, and T. Q. S. Quek, “Prediction-assisted multi-UAV online service migration and trajectory control for MEC-empowered vehicular networks,” *IEEE Trans. Mobile Comput.*, early access, 2026.

[21] Z. Liang, Y. Liu, T.-M. Lok, and K. Huang, “Multi-cell mobile edge computing: Joint service migration and resource allocation,” *IEEE Trans. Wireless Commun.*, 2021.

[22] Z. Chen, S. Huang, G. Min, Z. Ning, J. Li, and Y. Zhang, “Mobility-aware seamless service migration and resource allocation in multi-edge IoV systems,” *IEEE Trans. Mobile Comput.*, 2025.

[23] Y. Hou, L. Yang, and Y. Dai, “Service migration strategies based on partially observable and multi-objective optimization,” *IEEE Trans. Mobile Comput.*, early access, 2026.

[24] Y. Shi, C. Yi, R. Wang, Q. Wu, B. Chen, and J. Cai, “Service migration or task rerouting: A two-timescale online resource optimization for MEC,” *IEEE Trans. Wireless Commun.*, vol. 23, no. 2, pp. 1503–1519, Feb. 2024, doi: 10.1109/TWC.2023.3290005.

[25] M. Zhao, R. Zhang, Z. He, and K. Li, “Joint optimization of trajectory, offloading, caching, and migration for UAV-assisted MEC,” *IEEE Trans. Mobile Comput.*, 2025.

[26] L. Wang, B. Shen, L. Ma, Y. Zhang, Y. Zhao, H. Guo, Z. Yu, and B. Guo, “Joint task offloading and migration optimization in UAV-enabled dynamic MEC networks,” *IEEE Trans. Serv. Comput.*, vol. 18, no. 4, pp. 2143–2157, Jul.–Aug. 2025, doi: 10.1109/TSC.2025.3576644.

[27] Y. Zhao, C. Liu, X. Hu, J. He, M. Peng, D. W. K. Ng, and T. Q. S. Quek, “Joint content caching, service placement, and task offloading in UAV-enabled mobile edge computing networks,” *IEEE J. Sel. Areas Commun.*, 2025.

[28] A. Roy, V. M. R. Tummala, and V. Yadam, “Serv-HU: Service hand-off for UAV-as-a-service,” *IEEE Trans. Serv. Comput.*, 2025.

[29] S. García-Gil, D. Ramos-Ramos, J. Berrocal, J. M. Murillo, and J. Galán-Jiménez, “Microservices migration: A pathway to improved energy efficiency in UAV networks,” *Internet of Things*, 2025.
