# 电池轮换场景下无人机移动边缘计算有状态服务交接的终端可行性与在线调度

## I. 引言

移动边缘计算（mobile edge computing，MEC）把计算资源部署到网络边缘，使图像分析、设施巡检和环境感知等时延敏感业务能够在数据产生地点附近完成处理 [1]–[3]。当地面设施受损、覆盖不足或无法快速部署时，搭载计算模块的无人机（unmanned aerial vehicle，UAV）可以快速恢复无线接入和边缘计算服务。然而，单架 UAV 的覆盖范围、计算能力和电池容量均有限，持续时间超过单机续航的任务必须在服务过程中完成 UAV 轮换 [4]。

多机轮换能够延续无线覆盖和计算资源，却不能自动延续正在运行的应用。目标跟踪、事件检测和流式分析等有状态服务只有保留处理进度、去重标识和未提交结果，才能在另一计算节点继续处理后续输入 [5]。当源 UAV 必须离开任务区域时，替补 UAV 除了接替通信和计算职责，还必须获得与源端一致的应用状态；否则，服务虽仍有计算资源，却需要回退或重建其执行上下文。

按照交接时长是否由状态传输过程内生决定，最相关的工作可以分为参数化交接和过程化交接两类。参数化交接把替补起飞、服务迁移和源机返航组织为轮换流程，但将替换时间或交接时间作为给定量，再据此安排 UAV 数量、轮换次序或返航站点 [6]–[8]。过程化交接则显式描述运行状态的预拷贝、迭代更新和最终同步，使交接时长随待迁状态、写入速率和传输带宽变化 [9]–[11]。前一类能够处理电量触发的飞行平台替换，后一类能够刻画迁移期间的状态变化，但二者分别固定了本文需要联合决定的另一部分。

当任务处理本身会产生尚未同步的应用状态时，电量触发的 UAV 轮换把这两类边界连接起来。现有 UAV 轮换工作通常不展开交接期间的状态演化，固定边缘节点上的在线迁移则不要求源计算平台为强制返航预留时间和能量；最接近的 UAV 有状态微服务轮换架构已经给出镜像预传和最终检查点流程，但尚未把迁移开销展开为在线资源决策 [12]。因此，本文关注的不是电池轮换、有状态迁移或在线迁移本身，而是任务处理动作同时减少任务积压、增加未同步状态债务并消耗返航能量时，交接是否还能在硬离场期限前完成。

本文考虑采用应用辅助状态接口的流式 UAV-MEC 服务。应用镜像、模型参数和基础检查点预先部署在候选替补 UAV 上；源服务把尚未合并到检查点的必要更新写入可序列化增量日志，并保证这些记录在一次短交接窗口内只追加、不跨槽抵消。当源 UAV 接近返航能量边界时，上层轮换器给出一架已到达或可按时到达的替补 UAV。源 UAV 在继续处理任务的同时通过空空（air-to-air，A2A）链路传输增量日志，在选定时隙暂停服务并完成最终同步；替补确认接管后，源 UAV 立即返航。确认、唯一所有权和失败中止作为交接协议假设保留，不作为优化创新。

该场景的核心决策是服务暂停时刻以及逐时隙中央处理器（central processing unit，CPU）和 A2A 带宽。提高 CPU 频率可以减少任务积压，却会产生更多增量日志并降低返航储备；降低处理量能够减轻同步和能量压力，却可能使任务队列溢出。本文把在给定暂停时刻下仍存在一组后续 CPU 与带宽动作、能够同时保持队列、完成最终同步并满足安全返航约束的性质称为终端可行性。主问题固定一次交接及其候选替补，把多事件替补匹配和连续轮换留作扩展，从而集中研究“处理—状态债务—返航储备”的动态耦合。

求解该问题需要把终端可行性写成可计算条件，而不能只把它定义为未知后续动作序列的存在性。为此，本文在校准得到的任务到达上界、增量日志上界和 A2A 速率下界内，构造显式的终端安全约束，并将其嵌入终端可行性感知鲁棒模型预测控制（terminal-feasibility-aware robust model predictive control，TF-RMPC）。控制器枚举有限个可选暂停时刻，在每个时隙求解带终端日志清偿和返航储备约束的凸滚动子问题，只执行当前动作并用下一槽观测重新规划。分段仿射的速率下界和能耗上界把在线安全层实现为可热启动的二次规划；若安全层无解，控制器执行预先定义的停止处理和安全返航策略，而不下发已知会破坏终端可行性的动作。

本文的主要贡献概括如下：

1. 建立面向应用辅助流式服务的电池轮换交接模型，以预置基础检查点和窗口内只追加的增量日志界定可迁状态，并按时隙刻画任务处理、状态债务和返航能耗之间的因果关系。
2. 推导离场前的显式终端可行条件，以保守队列、日志和能量递推统一约束任务缓存、最终同步和安全返航；在分段仿射边界下，该条件可由有限时域凸二次规划直接检验。
3. 设计 TF-RMPC，在每个时隙重求满足终端条件的 CPU 与 A2A 带宽动作，并给出基于计划移位的递归可行性边界；实验首先检验处理量与新增日志量的模型前提，再评价在线控制和少量并发交接扩展。

本文其余内容安排如下。第 II 节综述 UAV 补能与轮换、有状态服务迁移以及终端约束在线控制；第 III 节建立系统、增量日志、能量与终端可行模型；第 IV 节介绍 TF-RMPC 的暂停时刻筛选、终端安全层和滚动执行；第 V 节给出模型前提与控制方法的实验设计；附录总结与最相关研究的区别及主要模型风险。

## II. 相关工作

与本文问题最相关的研究包括 UAV 续航条件下的服务接替、有状态服务迁移以及终端约束在线控制。前两类研究分别说明飞行平台和运行状态能够如何延续，第三类研究决定控制器如何在滚动执行时保留离场前的可行路径。

### A. UAV 续航与服务接替

按照补能前后是否仍由同一架 UAV 承担原任务，现有续航方法可分为同机续作和多机接替。前一类通过联合安排飞行、任务处理和换电时机，使 UAV 在完成当前阶段任务后补能并继续执行后续任务 [4]。这类方法协调了任务进度与补能需求，但补能前后仍由同一飞行平台提供服务，因而不涉及运行状态在不同 UAV 之间的转移。

多机接替方法则在一架 UAV 离场时，由另一架 UAV 继续承担其通信或计算职责。现有研究通过机群重组与任务委托 [13]、周期轮换与中继关系调整 [14]、多架中继 UAV 依次替换 [15]，或者联合规划交接双方的轨迹和带宽 [6]，维持任务区域的无线覆盖、端到端连接或任务接收能力。Tipantuña 等进一步把替补起飞、VNF 迁移、源 UAV 返航和换电统一为 replacement state，并优化 UAV 数量与轮换次序，但把迁移和往返过程合并为给定的替换时间 [8]。Ye 等根据带宽估计交接时间，再联合安排低电量 UAV、满电 UAV 和返航站点 [7]。这类研究已经覆盖“起飞—迁移—返航—换电”的平台轮换过程，其共同边界是交接工作量没有随窗口内的任务处理继续演化。

### B. 有状态服务迁移

按照状态传输是否与服务运行重叠，有状态迁移可分为停机迁移和在线迁移。停机迁移暂停源端服务后复制待迁状态，状态量越大，服务中断通常越长；在线迁移则在源端继续运行或目标端提前准备的同时传输大部分状态，仅在切换阶段同步剩余状态。固定边缘节点上的研究据此预热可复用状态、增量迁移内存和连接状态，或利用容器分层减少重复传输 [9], [16], [17]；PAM 和 MOSE 进一步按照状态写入、带宽和停机目标配置迭代迁移过程 [10], [11]。这些方法能够让交接时长随状态传输过程变化，但源节点由持续供电设施提供，不需要在同一期限内保留返航时间和能量。

直接面向 UAV 的研究已经把有状态迁移引入空中计算节点，但尚未闭合任务处理、状态生成与强制离场之间的关系。TOM 以虚拟机内存作为待迁状态量，并联合安排 UAV 位置、任务卸载和多项服务的迁移顺序 [5]；Frejo-Martín 等通过镜像预传和 CRIU 最终检查点实现电池轮换中的有状态微服务恢复，但把性能评估和在线资源优化留作后续工作 [12]。Rong 等表明应用辅助接口可以只同步永久、关键和易失状态中的必要部分，但其目标跟踪实例使用有限长度状态队列，旧状态可被覆盖，不能直接支持“处理量越大、待同步状态必然永久累积”的一般假设 [9]。因此，本文不把所有有状态服务统一为非负增量过程，而把研究对象限定为在短交接窗口内维护只追加增量日志的流式服务，并要求该日志模型先通过应用实验标定。

### C. 终端约束在线控制

随机到达、信道变化和状态写入使交接控制需要根据最新观测反复修正 CPU 与带宽。强化学习可以从交互中生成混合资源动作 [18]–[20]，约束策略优化也可以控制长期期望代价 [21], [22]；这些方法适合学习平均性能，却不能仅凭奖励、惩罚或一步动作投影证明某次交接在硬离场期限前仍然可完成。若学习策略用于本文场景，其作用只能是生成性能提案，最终执行动作仍需经过显式终端安全层。

模型预测控制在每个采样时刻求解有限时域问题，只执行首个动作并根据下一状态重新规划，能够直接处理硬状态和输入约束 [23]。其递归可行性依赖终端集合、计划移位以及不确定性边界，而不是把未来可行集记为一个未经求解的抽象集合。本文据此把增量日志清偿、任务队列和返航储备写入同一有限时域凸子问题，并在每次执行前检验尾部计划；多候选替补和多事件匹配只作为外层扩展，不进入主问题的终端保证。

## III. 系统模型与问题建模

本文沿用多区域、多 UAV、集中控制和分时隙运行的 UAV-MEC 架构 [1]–[3]。区域部署、用户关联、任务上行、安全航路和轮换触发由上层规划器给出，本文研究轮换事件触发后的服务运行过程。一次交接依次经历替补到达、增量日志预传、服务暂停、最终同步、确认接管和源 UAV 返航。下文按照这一过程建立系统描述、任务处理、有状态服务交接和能量消耗模型，最后给出在线优化问题。

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

本文先研究一个交接窗口内的一次轮换事件 $n$。其区域和源 UAV 分别记为 $r_n$ 和 $u_n$，源 UAV 必须开始返航的最晚绝对时刻为 $d_n^{\mathrm{dep}}$。上层轮换器根据待命状态、安全航路和到达时间，从候选集合 $\mathcal V_n$ 中给出本次使用的替补 UAV $v_n$；其到达时隙 $t_n^{\mathrm{arr}}$ 是主问题的已知输入。该边界把“选择哪架替补”与“替补到达后如何完成状态交接”分开，使主问题只决定服务暂停时隙 $c_n\in\mathcal W_\tau$、CPU 和 A2A 带宽。多个候选可以逐一代入主问题比较，多事件排他匹配则在第 V-D 节作为扩展评价。

替补到达后，A2A 链路即可用于状态同步；是否实际传输以及传输多少由逐时隙带宽决定。可选暂停时隙还必须满足

$$
t_n^{\mathrm{arr}}<c_n<\tau+T_{\mathrm w},
\qquad
(c_n+1)\Delta\le d_n^{\mathrm{dep}}.
$$

区域 $r$ 在时隙 $t$ 开始时的合法服务所有者记为 $o_r[t]$。窗口开始时有 $o_{r_n}[\tau]=u_n$；确认成功前，源 UAV 始终保有唯一提交权。服务在时隙 $c_n$ 暂停并完成最终同步，成功确认后，所有者在时隙 $c_n+1$ 更新为 $v_n$，源 UAV 同时进入返航模式。

在普通时隙开始时，控制器先观察任务队列、当期到达、同步欠账、电量和当前信道，再决定 CPU 与 A2A 带宽。随后，A2A 链路发送槽首已经封存的状态，CPU 同时处理任务；本槽计算产生的新状态在槽末封存，并与能量状态一同更新。停机时隙 $c_n$ 不再处理任务，只执行最终同步、状态载入和确认。该事件顺序保证控制决策不使用动作执行后才实现的信息。

### B. 任务处理模型

任务处理模型描述服务运行产生计算结果和新状态之前的队列变化。令 $Q_i[t]$ 表示时隙 $t$ 开始、接纳当期到达之前的任务积压，令 $A_i[t]$ 表示槽首已经完成上行的数据量，二者单位均为 bit。初始队列 $Q_i[\tau]$ 在窗口开始时可观测，未来到达在相应时隙开始前未知。

令 $\phi_i$ 表示处理 1 bit 数据所需的 CPU 周期数，$f_i[t]$ 表示分配给会话 $i$ 的 CPU 频率。为表示停机槽，定义

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

停机指示使暂停区域的 CPU 分配自动为零。提高 CPU 频率可以减少任务积压，但处理更多任务也会产生更多需要交接的运行状态。

### C. 有状态服务交接模型

本文只对能够通过应用接口完整序列化的增量日志建模。应用镜像、模型参数、运行库和基础检查点预先部署在替补 UAV 上；能够从保留输入重放的临时状态不参与同步 [9], [17]。源服务把尚未并入基础检查点、且接管后维持应用语义所必需的更新写入 write-ahead log。日志记录在本窗口内只追加，不因后续覆盖、压缩或检查点合并而从待同步对象中消失；不能满足该条件的应用不属于当前模型。

令 $W_n[t]\ge0$ 表示时隙 $t$ 的任务处理完成后新增并封存的日志量。其真实值可以随输入内容和应用阶段变化，本文不把它预设为严格线性函数，而要求应用标定给出分段仿射上界。为简化记号，在一个标定区间内写为

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

其中 $\overline W_n^{\mathrm{bg}}[t]\ge0$ 是与任务处理量无关的日志上界，$\overline\eta_{ni}[t]\ge0$ 是单位处理量的保守增量系数。两者只用训练/校准轨迹拟合，并在最终测试前冻结。$W_n[t]$ 到槽末才可观测，因而只能从下一时隙开始传输；停机槽不再处理任务，也不产生新日志。

令 $G_n[\tau]\ge0$ 表示窗口开始时尚未同步到替补 UAV 的日志债务。由于基础检查点已经预置，$G_n[\tau]$ 不包含镜像、模型或运行库；若这些对象不能预置，其传输时间和能量必须另行加入模型。事件 $n$ 在时隙 $t$ 获得的 A2A 带宽为 $b_n[t]$，系统总带宽为 $B^{\mathrm A}$。令 $h_n[t]$ 和 $P_n^{\mathrm A}$ 分别表示源 UAV 与已选替补 UAV 之间的信道功率增益和发射功率，$N_0$ 为噪声功率谱密度。实际 A2A 速率为

$$
C_n^{\mathrm A}[t]
=
b_n[t]\log_2\left(
1+
\frac{P_n^{\mathrm A}h_n[t]}
{N_0b_n[t]}
\right),
$$

其中 $b_n[t]=0$ 时定义 $C_n^{\mathrm A}[t]=0$。带宽只能在替补到达后至服务暂停槽（含该槽）分配，并满足

$$
0\le b_n[t]\le
B^{\mathrm A}
\mathbb 1\{t_n^{\mathrm{arr}}\le t\le c_n\}.
$$

在 $t_n^{\mathrm{arr}}\le t<c_n$ 的预拷贝阶段，A2A 链路只能发送槽首已经封存的数据。实际发送量和下一时隙的欠同步量分别为

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

该递推与 $L_n[t]$ 的定义等价，并明确表示本槽计算产生的 $W_n[t]$ 只能从下一时隙开始传输。源 UAV 在时隙 $c_n$ 开始时冻结服务，最终需要传输的数据量为

$$
D_n^{\mathrm{stop}}
=
G_n[c_n]+D_n^{\mathrm{meta}},
$$

其中 $D_n^{\mathrm{meta}}>0$ 是恢复和确认所需的协议元数据。

服务暂停后，源 UAV 依次完成日志冻结、最终状态传输、替补端状态载入和确认。相应固定时间分别为 $\tau_n^{\mathrm{freeze}}$、$\tau_n^{\mathrm{apply}}$ 和 $\tau_n^{\mathrm{ack}}$，其总和为

$$
\tau_n^{\mathrm{fix}}
=
\tau_n^{\mathrm{freeze}}
+
\tau_n^{\mathrm{apply}}
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

其中 $C_n^{\mathrm A}[c_n]=0$ 时规定 $T_n^{\mathrm{proto}}=+\infty$。本文采用整槽交接：服务在 $c_n\Delta$ 冻结，所有权只在下一时隙开始时更新。因此业务中断为一个时隙，并要求 $\Delta\le I_n^{\max}$。

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

$M_n\ge0$ 与 $T_n^{\mathrm{proto}}\le\Delta$ 等价。主模型要求替补先到达、固定协议阶段短于一个时隙、业务中断不超过上限，并使协议在离场期限前完成：

$$
t_n^{\mathrm{arr}}<c_n<\tau+T_{\mathrm w},
\qquad
(c_n+1)\Delta\le d_n^{\mathrm{dep}},
\qquad
\tau_n^{\mathrm{fix}}<\Delta\le I_n^{\max}.
$$

确认和所有权切换采用单写者协议。确认返回前，源 UAV 保留唯一提交权，替补只保存未提交副本；当 $M_n\ge0$ 且确认在固定的 $\tau_n^{\mathrm{ack}}$ 内返回时，$o_{r_n}[c_n+1]=v_n$。若确认超时，替补丢弃未提交副本，源 UAV 按预留能量立即返航。确认丢包、控制链故障和交接后的业务重建作为协议异常单独统计，不进入状态生成与资源调度的创新主张。

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

对选定的源—替补 UAV 对，令 $P_{un}^{\mathrm A,\mathrm{data}}[t]$ 表示端点 $u\in\{u_n,v_n\}$ 的数据无线功率，令 $E_{un}^{\mathrm{A,fix}}$ 表示冻结、载入和确认产生的固定能耗。对应的 A2A 能耗为

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

最后一项只在源 UAV 的停机槽预留，因此同一约束同时覆盖正常返航和确认失败后的中止返航。

### E. 问题建模

基于上述模型，主问题在已知源 UAV、替补 UAV 和到达时隙的条件下，联合决定暂停时隙以及逐槽 CPU 与 A2A 带宽。令 $\boldsymbol S[t]$ 表示由任务队列、日志债务、UAV 电量、当前信道和协议阶段组成的槽首状态。窗口开始时选择

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

未来任务到达、日志写入和信道只能在实现后进入 $\boldsymbol S[t+1]$。确认结果属于协议层异常，不作为控制器在槽首可预知的随机动作变量。

终端可行性通过一个可直接求解的保守计划定义。校准阶段为未来时隙给出任务到达上界 $\overline A_i[k]$、第 III-C 节的日志上界 $\overline W_n[k]$、满槽可靠传输量下界 $\underline s_n[k](b)$ 和能耗上界 $\overline E_u^{\mathrm{use}}[k]$，使

$$
A_i[k]\le\overline A_i[k],\qquad
C_n^{\mathrm A}[k]\Delta\ge\underline s_n[k](b_n[k]),
\qquad
E_u^{\mathrm{use}}[k]\le\overline E_u^{\mathrm{use}}[k]
$$

在声明的应用、负载和信道范围内成立。$\underline s_n[k](b)$ 由 Shannon 传输量在有限带宽分段上的弦线构成，因此是保守的凹分段仿射函数；$\overline E_u^{\mathrm{use}}[k]$ 对 CPU 能耗使用凸分段仿射上界。所有边界在最终测试前冻结。

在时隙 $t$ 和候选暂停时隙 $c\in\mathcal C_\tau$ 下，令 $\mathsf F_t(c)$ 表示以下计划变量的可行域：

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

其中 $k=t,\ldots,c-1$，且 $\widehat f_i[c]=0$。CPU 总量满足第 III-B 节的容量约束。日志债务上界从 $g_n[t]=G_n[t]$ 开始，并满足

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

第二个不等式对应预拷贝清空槽首债务后，本槽新增日志仍只能留到下一槽。暂停槽的最终同步必须满足

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

上述等式和不等式共同构成 $\mathsf F_t(c)$。由于日志和能量使用上界、传输使用凹下界，原始形式是凸可行性问题；采用前述分段仿射边界后，它由线性约束表示。因而，判断 $\mathsf F_t(c)$ 是否为空不再等价于重新求解一个未指定的随机控制问题，而是求解一个变量、约束和停止条件均明确的有限时域凸程序。

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

其中 $\lambda_Q,\lambda_E,\lambda_B,\lambda_M\ge0$ 在校准阶段冻结。离散变量只有有限个暂停时隙；枚举 $c$ 后，每个子问题都是凸程序，采用分段仿射边界和二次动作平滑项时可实现为二次规划。

该终端条件还给出递归可行性边界。若 $\mathsf F_t(c_n)$ 非空、当前执行其首个动作，且实际到达、日志、信道和能耗没有越过校准边界，则实际下一状态分别不劣于计划中的 $q_i[t+1]$、$g_n[t+1]$ 和剩余能量下界。删除已执行的首项后，原计划尾部仍属于 $\mathsf F_{t+1}(c_n)$；重复这一计划移位可使最终日志在暂停槽内完成同步，并保留返航储备。该结论只覆盖已建模边界内的资源与状态过程，不覆盖确认丢包、软件错误或未建模链路故障。

## IV. TF-RMPC 求解方法

问题 P1 的离散部分只有暂停时隙，连续部分则在每个时隙随队列、日志债务和信道观测更新。TF-RMPC 先枚举有限个暂停时隙并通过 $\mathsf F_\tau(c)$ 执行交接准入，再固定选中的 $c_n$ 滚动求解剩余 CPU 与 A2A 带宽。该方法不把模型预测控制本身写成创新；其场景特定部分是把“任务处理新增日志”与“硬离场前清偿日志并保留返航能量”写成可求解的终端安全层。

### A. 总体框架

集中控制器在 $t=\tau$ 收集源/替补电量、候选到达时隙、当前任务队列、当前日志债务和校准边界。对每个 $c\in\mathcal C_\tau$，控制器建立第 III-E 节的 $\mathsf F_\tau(c)$ 并求解 P1；不可行的暂停时隙直接删除。若至少有一个子问题可行，控制器选择目标值最小的 $c_n$ 和对应计划，向替补 UAV 发出交接准入指令；否则不启动该交接，并把候选更换或业务恢复交还上层轮换器。

一旦交接被准入，$c_n$ 在本窗口内固定。固定暂停时刻避免控制器通过反复后移截止时间掩盖资源不足，也使第 III-E 节的计划移位能够直接建立递归可行性。每个后续时隙只更新已经实现的队列、日志债务、信道和电量，未实现量继续使用冻结的校准边界。

TF-RMPC 的输入是槽首状态和剩余边界，输出是当前槽的 $\boldsymbol f[t]$ 与 $b_n[t]$。控制器不需要训练网络、价值函数或未来真实轨迹；所有在线信息都在动作产生前可用。上层若给出多个候选替补，则分别计算其可行暂停时隙和目标值，再选择一个候选，主问题本身不同时优化替补匹配。

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

其中 $\widehat{\boldsymbol a}[t]=(\{\widehat f_i[t]\},\widehat b_n[t])$ 是计划的首个资源动作。二次项只要求在安全允许时接近名义提案；$\mathsf F_t(c_n)$ 才负责 CPU、队列、带宽、日志终端量和返航能量约束。采用分段仿射日志、传输和能量边界后，P2 是具有线性约束和凸二次目标的二次规划。

安全层只执行 P2 的首个动作，余下变量是证明当前动作可延续到暂停时刻的见证计划。下一时隙到来后，控制器用实际观测重建 P2，而不是机械执行旧计划。若实际过程严格优于保守边界，滚动优化可以释放多余资源；若实际过程贴近边界，计划会逐步把 CPU 限制到队列所需范围，并把更多 A2A 资源留给日志清偿。

P2 的保证范围由 $\mathsf F_t(c_n)$ 中的约束决定。它保证校准边界内的队列、日志同步和返航能量，不保证边界外扰动、软件正确性或 ACK 可用性。若一个外部学习器提供 $\widetilde{\boldsymbol a}[t]$，学习器只影响二次距离和性能，不改变该边界，也不构成本文方法的必要组成。

### C. 滚动执行与回退

**算法 1：TF-RMPC 的交接准入与滚动执行**

**输入：** 第 III 节环境模型，源 UAV $u_n$，候选替补 $v_n$ 及到达时隙，冻结的任务、日志、信道和能量边界，代价权重与求解时限。

**输出：** 暂停时隙 $c_n$，逐槽 CPU 动作 $\boldsymbol f[t]$ 与 A2A 带宽 $b_n[t]$，以及准入拒绝、正常完成或协议异常状态。

1. 在 $t=\tau$ 观察 $\boldsymbol S[\tau]$，构造 $\mathcal C_\tau$。
2. 对每个 $c\in\mathcal C_\tau$ 建立 $\mathsf F_\tau(c)$ 并求解 P1，删除不可行候选。
3. 若没有可行暂停时隙，则拒绝启动交接并通知上层轮换器；否则选择目标值最小的 $c_n$，保存其计划作为热启动。
4. 对 $t=\tau,\ldots,c_n-1$，观察 $\boldsymbol S[t]$，更新剩余初始状态并求解 P2。
5. 执行 P2 的首个 $\boldsymbol f[t]$ 和 $b_n[t]$，在槽末记录实际 $A_i[t]$、$W_n[t]$、传输量和能耗，再滚动到下一时隙。
6. 在 $t=c_n$ 冻结服务，按 P2 的终端带宽完成最终日志和元数据传输；替补载入状态并返回 ACK 后更新所有权，源 UAV 开始返航。
7. 若实际量越过冻结边界或求解器未在时限内返回，停止使用递归可行性声明；控制器优先检查立即冻结是否仍可完成，不能完成时保留源端所有权并按协议进入安全返航和业务恢复流程。

步骤 2 是交接准入，步骤 4–5 是正常滚动路径，步骤 7 只处理模型边界失效。若边界成立且 P1 已准入，计划移位使 P2 在后续时隙保持可行，因此正常路径不需要依靠临时惩罚或未定义的搜索恢复动作。若实际边界失效，算法明确撤回保证并记录失败原因，而不是把协议异常计入优化器的可行性证明。

暂停槽结束后，在线求解器不再参与状态恢复。替补 UAV 依据应用接口重放增量日志，输出一致性由第 V-A 节的应用实验检验；源 UAV 的返航航路和补能由上层轮换器继续管理。由此，TF-RMPC 的执行边界止于“ACK 后所有权切换且源机保有返航储备”。

### D. 复杂度分析

TF-RMPC 的在线开销由暂停时隙枚举和二次规划组成。令 $H=c_n-t$ 表示剩余预拷贝时隙数，$I_n=|\mathcal I_{r_n}|$，每槽连续资源动作维数为 $d=I_n+1$。P2 的变量和约束数量均随 $H(I_n+1)$ 线性增长；若分段仿射边界总共引入 $S$ 个附加片段约束，则可分别记为

$$
n_z=O\big(H(I_n+1)\big),
\qquad
n_c=O\big(H(I_n+1)+S\big).
$$

采用通用原始—对偶内点法时，一个 QP 的保守算术复杂度可写为 $O((n_z+n_c)^3\log(1/\epsilon))$，其中 $\epsilon$ 是求解容差；实际成本还取决于稀疏结构和求解器实现。窗口开始时最多求解 $|\mathcal C_\tau|$ 个 P1 子问题，暂停时隙固定后每槽只求解一个 P2。相邻时隙的约束矩阵结构不变，上一槽的尾部计划可作为热启动。

该量级只说明扩展趋势，不能替代在线时延证据。第 V-D 节将以 batch size 为 1 测量建模、求解、日志记录和通信下发的完整链路，并分别报告不同预测时域、会话数和分段数下的 p50、p95、p99 时延及超时率。只有完整链路在声明硬件上持续小于 $\Delta$，才把相应规模称为可在线执行。

## V. 实验设计

本节按“模型前提—总体控制—机制消融—扩展与开销”的顺序验证三项贡献。第一组实验首先判断处理量与增量日志之间是否存在可用于终端约束的稳定上界；只有该前提成立，后续控制比较才具有应用含义。第二组实验在单次交接主问题上比较 TF-RMPC 与参数化交接、固定状态量和无终端约束方法。最后通过消融、多候选/少量并发扩展和完整动作链时延，限定终端安全层的作用与可部署规模。

### A. 实验设置与状态交接验证

状态模型验证选取一个具体的流式边缘应用作为主对象，并实现“预置基础检查点 + 窗口内只追加增量日志”的应用接口。实验逐独立轨迹改变输入批量、CPU 频率和输入内容，记录每槽处理量 $\mu_i[t]$、新增日志量 $W_n[t]$、日志记录数、序列化字节和处理阶段。拟合阶段分别比较线性、分段仿射和应用阶段相关上界；校准集用于选择分段和覆盖目标，最终保留测试集只检验经验覆盖、上界宽度及随负载变化的误差，不反向调整模型。

状态接口的正确性与日志大小拟合分开验证。在可控带宽、时延和丢包条件下重放同一输入轨迹，逐输入比较无迁移运行与交接后运行的输出、去重结果、提交顺序和服务世代，并记录最终同步量、暂停时间、恢复时间和 A2A 字节。任一保留轨迹出现语义不一致，都否定该应用上的当前接口；若 $W_n[t]$ 无法被有用的线性或分段仿射上界覆盖，则改用有界快照、应用阶段状态或传统脏页率模型，而不继续用惩罚项掩盖模型失配。

主问题采用三个由紧迫程度区分的单次交接实例，扩展问题另行标记：

| 测试实例 | 交接范围 | 主要变化 | 主要证据角色 |
| -------- | -------- | -------- | ------------ |
| Case 1 | 单事件、小会话集 | 宽松离场期限与稳定信道 | 建立离线参照并核对终端条件 |
| Case 2 | 单事件、中等会话集 | 任务负载、初始日志债务和返航余量 | 比较正常在线控制 |
| Case 3 | 单事件、紧期限 | 信道下界与日志产生上界接近容量边界 | 暴露准入拒绝和保证边界 |
| Extension | 两至三个事件 | 候选替补和共享 A2A 竞争 | 只评价扩展开销与失败模式 |

任务、信道、初始日志和初始电量轨迹划分为拟合、校准和最终测试三组；同一测试轨迹对所有方法配对复用。正式测试前冻结分段边界、代价权重、停止时刻候选、求解容差、时限和失败定义。物理违约、模型边界失配、准入拒绝、求解超时和协议 ACK 异常分别报告，不能合并为一个有利于方法的总失败率。

### B. 模型标定与总体性能

模型标定实验先回答第 III-E 节的保守边界是否既覆盖保留轨迹，又没有宽到使所有候选暂停时隙均不可行。分别报告任务到达、日志写入、A2A 传输量和能耗边界的测试覆盖率、绝对/相对松弛量，以及由各边界单独造成的准入拒绝率。该实验只支持模型适用范围和保守程度，不用于比较控制方法。

总体性能实验比较五类方法：把交接时间作为固定输入的轮换基线、把状态量固定为窗口初值的 MPC、只满足当前槽约束的 Myopic-QP、采用相同预测边界但删除日志终端约束的 RMPC-Local，以及完整 TF-RMPC。Case 1 另给出使用完整未来轨迹的离线解，作为信息占优的参照而非在线竞争者。所有在线方法获得相同槽首观测、相同测试轨迹、相同动作范围和相同单槽计算时限。

主指标包括交接完成率、任务队列溢出率、最终日志余量、源/替补最小返航余量和单位完成任务能耗；辅助指标包括暂停时刻、A2A 字节、带宽占用、协议完成时间、准入拒绝和求解超时。结果分析先比较 Case 1–3 中的系统指标，再检查 TF-RMPC 的模型内预测与实际轨迹是否一致。只有边界内保留测试上的配对结果支持控制结论，ACK 丢包和软件故障只作为协议可靠性结果单列。

### C. 组件消融与决策行为

消融实验只回答三个与贡献直接对应的问题。`w/o Update Coupling` 把新增日志量固定为与 CPU 无关的外生过程，用于检验处理动作改变未来交接工作量是否会改变调度结果；`w/o Terminal Constraint` 只保留当前槽队列、带宽和能量约束，用于检验显式终端条件是否减少离场前无法清偿的日志；`Nominal Boundary` 用条件均值替代保守上下界，用于检验边界保守性与物理违约之间的权衡。三个变体复用相同目标函数、停止时刻候选、求解器、测试轨迹和时限。

消融结果只把配对实验真正隔离的变化归因于相应组件。状态耦合对应 CPU、日志字节和任务队列之间的变化，终端约束对应最终日志余量与离场违约，保守边界对应准入率与边界外失败。再预先冻结一个 Case 2 轨迹，展示“槽首状态—名义动作—P2 修正—尾部计划—实际结果”的完整链条；该轨迹只解释机制，不替代跨实例统计。

### D. 少量并发扩展与在线开销

扩展实验先评价多个候选替补，而不改变单事件主问题。对每个候选分别计算可行暂停时隙、目标值和在线开销，再比较上层按最小目标选择与最早到达、最大电量两种启发式。随后把两至三个交接事件放入共享 A2A 资源下，比较顺序准入与联合凸资源计划；只要联合问题不再满足第 III-E 节的单事件计划移位条件，就把结果标记为扩展经验，不沿用主问题的递归可行性声明。

在线开销实验测量 batch size 为 1 时的完整动作链，包括状态读取、边界实例化、暂停时隙枚举、QP 建模、求解、日志记录和动作下发。报告不同预测时域、会话数、分段数和扩展事件数下的 p50、p95、p99 时延、峰值内存、热启动收益及超过 $\Delta$ 的时限违约率。若紧期限 Case 3 或并发扩展不能在单槽内稳定完成，则把可发表范围收缩到通过时限测试的会话数和事件数，不用渐近复杂度替代实测结论。

## 附录 A：Problem–Method–Insight、新颖性边界与模型风险

### A.1 Problem–Method–Insight

**Problem。** 电池触发的轮换要求源 UAV 在最晚离场时刻前把服务交给替补 UAV。为了维持业务质量，源 UAV 在预拷贝期间仍需处理任务；对采用只追加增量日志的流式服务，任务处理会增加尚未同步的应用状态并消耗返航能量。CPU 处理、日志同步、暂停时刻和返航储备因而共同决定交接能否在硬期限前完成。

**Method。** 系统预置应用镜像和基础检查点，只对经应用接口序列化、经轨迹校准且在交接窗口内不可抵消的增量日志建模。调度器枚举暂停时刻，并把队列上界、日志债务递推、可靠传输量下界和返航能量写成显式凸终端条件。TF-RMPC 在每槽求解带该终端条件的 QP，只执行首个 CPU 与 A2A 带宽动作，并用下一槽观测滚动更新。

**Insight。** 电池轮换下，当前资源动作可行不足以说明服务能够安全交接；决定终端可行性的量是“剩余不可重建关键更新”相对于“最晚离场前仍可保留的同步、协议和返航容量”的动态余量。当计算会产生新的不可合并更新时，增加计算既可降低队列，也可能扩大同步需求并消耗返航能量，因此安全调度必须保持未来终端路径，而不是只修正当前约束。

### A.2 与最近邻工作的正面边界

Tipantuña 等已经把新 UAV 起飞、VNF 迁移、旧 UAV 返航和换电统一为多机轮换流程，并优化 UAV 数量与轮换次序 [8]。本文不主张“首次研究电池轮换中的服务迁移”；区别在于其 replacement time 是包含迁移与往返过程的给定参数，而本文展开任务处理所产生的增量日志，并据此约束离场前的剩余同步工作量。

TOM 已经研究有状态 UAV-VEC，并联合决定轨迹、卸载和多服务并行迁移 [5]。其迁移工作量由固定虚拟机内存大小给出，源/目标资源锁决定并行分组；本文不主张“首次研究有状态 UAV 服务”或“首次联合计算和迁移”。本文与其区别限定为电池强制退出时，当前处理量同时改变任务队列、增量日志和返航储备所形成的终端可行性。

Ye 等已经研究低电量 UAV 与满电 UAV 之间的服务交接，并明确转移用户、计算任务及其当前状态 [7]。该方法根据剩余电量、飞行距离、站点容量和预估交接时间调度 UAV；本文不主张“首次研究电池触发的 UAV-MEC 服务交接”，区别在于把交接时间从给定输入展开为受任务处理、增量日志和 A2A 带宽共同影响的在线过程。

Frejo-Martín 等已经提出面向电池轮换的有状态微服务迁移架构 [12]。其流程预传容器存储层，在替补 UAV 起飞时停止源服务，再通过最终检查点恢复运行状态；迁移性能评估与资源优化仍留待后续工作。本文因而不主张“首次把有状态迁移用于 UAV 轮换”，而研究源服务在停止前继续处理任务时，如何在硬离场与安全返航约束下保持日志清偿可行。

Rong 等已经证明整个内存预拷贝可能因脏页速率超过链路速率而失败，并提出永久状态预热、关键状态同步和易失状态重放 [9]。本文继承应用辅助状态接口，不把预拷贝或状态拆分写成创新；同时承认其目标跟踪状态队列会覆盖旧记录，不能作为一般非负累积模型的证据。当前模型只适用于经实验确认在短窗口内保持只追加语义的日志对象。

KubeSPT 的故障语义分为三段 [16]：状态复制或迭代检查点阶段失败时可以终止迁移且源 Pod 仍运行；最终检查点、目标 Pod 创建和服务重定向阶段的通信失败可能丢失状态；Hot Data/Lazy-Restore 阶段的通信失败不影响恢复。本文不取代通用容器迁移系统，而把可验证的应用状态接口、单写者世代和中止分支嵌入 UAV 轮换调度；其有效性依赖具体应用和板卡实现。

容器分层存储可减少镜像文件迁移开销 [17]，但本文假设镜像和永久状态已预置。若替补 UAV 不能预置镜像，镜像层传输、拉取失败和启动时间必须加入候选方案与协议固定时间，当前模型不再直接适用。

### A.3 主要风险与缩小版本

第一项风险是关键状态识别。应用可能遗漏影响正确性的隐藏状态，复杂服务也可能无法用版本化增量日志表示。状态接口、输出一致性测试和保留轨迹是使用模型的前置条件；失败时应限定到可明确序列化关键上下文的流式服务。

第二项风险是更新上界。$W_n[t]$ 表示槽内覆盖合并后在槽末封存、跨槽不再抵消的非负增量，并非通用脏页率；若写入与 CPU、输入内容或应用阶段之间关系不能由分段仿射上界覆盖，或必须依赖跨槽压缩才可运行，应改用场景约束、分布鲁棒集合或扩展状态模型。

第三项风险是边界覆盖。递归可行性依赖任务到达、日志写入、可靠传输量和能耗没有越过校准边界；过窄的边界会产生物理违约，过宽的边界会使交接被大量拒绝。真实部署需要同时报告覆盖率和保守松弛量，并在边界失效时撤回保证；故障后的业务重建位于当前交接窗口之外，因此本文不声称绝对安全。

第四项风险是在线规模。TF-RMPC 每槽求解随预测时域、会话数和分段数增长的 QP；若 Case 3 无法在时隙内求解，可发表范围应缩小到通过完整链路时限测试的单事件规模，再把多事件联合资源计划留作后续工作。

第五项风险是系统边界。替补选择、安全航路、换电站库存和连续轮换由上层规划器处理，不进入单次交接的递归可行性证明。若实验表明这些上层状态主导失败，应把研究对象扩展为多时间尺度机群运维，不能用当前单窗口结论代替。

## 参考文献

[1] C. Peng, Y. Chen, X. Huang, Z. Wu, Y. Xu, and Y. Wu, “Demand-aware multi-area multi-UAV empowered mobile edge computing: A joint energy and delay optimization,” *IEEE Trans. Mobile Comput.*, early access, 2026, doi: 10.1109/TMC.2026.3697839.

[2] F. Pervez, A. Sultana, C. Yang, and L. Zhao, “Energy and latency efficient joint communication and computation optimization in a multi-UAV-assisted MEC network,” *IEEE Trans. Wireless Commun.*, vol. 23, no. 3, pp. 1728–1741, Mar. 2024.

[3] Z. Sun, G. Sun, Q. Wu, L. He, S. Liang, H. Pan, D. Niyato, C. Yuen, and V. C. M. Leung, “TJCCT: A two-timescale approach for UAV-assisted mobile edge computing,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 4, pp. 3130–3147, Apr. 2025.

[4] D. Ye, Z. Sun, W. Zhong, J. Kang, X. Huang, D. I. Kim, S. Xie, and C. Yuen, “Optimal flight speed scheduling and battery swapping in UAV-enabled mobile edge computing,” *IEEE Trans. Mobile Comput.*, vol. 25, no. 1, pp. 948–960, Jan. 2026.

[5] Q. Qiu, L. Li, Z. Xiao, Q. Lin, L. Ma, and Z. Ming, “TOM: Joint trajectory, offloading and migration optimization in stateful service-oriented UAV-enabled VEC system,” *IEEE Trans. Serv. Comput.*, vol. 18, no. 6, pp. 4261–4275, Nov.–Dec. 2025.

[6] N. Gupta, S. Agarwal, D. Mishra, and B. Kumbhani, “Trajectory and resource allocation for UAV replacement to provide uninterrupted service,” *IEEE Trans. Commun.*, vol. 71, no. 12, pp. 7288–7302, Dec. 2023, doi: 10.1109/TCOMM.2023.3307559.

[7] Z. Ye, P. N. Ji, and T. Wang, “Seamless service handover in UAV-based mobile edge computing,” in *Proc. IEEE Global Commun. Conf. (GLOBECOM)*, 2023, pp. 1113–1118, doi: 10.1109/GLOBECOM54140.2023.10437843.

[8] C. Tipantuña, X. Hesselbach, V. Sánchez-Aguero, F. Valera, I. Vidal, and B. Nogales, “An NFV-based energy scheduling algorithm for a 5G enabled fleet of programmable unmanned aerial vehicles,” *Wireless Commun. Mobile Comput.*, vol. 2019, Art. no. 4734821, 2019, doi: 10.1155/2019/4734821.

[9] C. Rong, J. H. Wang, J. Wang, Y. Zhou, and J. Zhang, “Live migration of video analytics applications in edge computing,” *IEEE Trans. Mobile Comput.*, vol. 23, no. 3, pp. 2078–2092, Mar. 2024.

[10] A. Calagna, Y. Yu, P. Giaccone, and C. F. Chiasserini, “Design, modeling, and implementation of robust migration of stateful edge microservices,” *IEEE Trans. Netw. Service Manag.*, vol. 21, no. 2, pp. 1877–1893, Apr. 2024, doi: 10.1109/TNSM.2023.3331750.

[11] A. Calagna, Y. Yu, P. Giaccone, and C. F. Chiasserini, “MOSE: A novel orchestration framework for stateful microservice migration at the edge,” *IEEE Trans. Netw. Service Manag.*, vol. 22, no. 5, pp. 4827–4841, 2025, doi: 10.1109/TNSM.2025.3579051.

[12] S. Frejo-Martín, A. García-López, J. M. Murillo, and J. Galán-Jiménez, “Live migration of stateful microservices in UAV-assisted networks for enhanced availability,” in *Proc. IEEE Symp. Comput. Commun. (ISCC)*, 2025, pp. 1–6, doi: 10.1109/ISCC65549.2025.11325941.

[13] J. Li, C. Yi, J. Chen, Y. Shi, T. Zhang, X. Li, R. Wang, and K. Zhu, “A reinforcement learning-based stochastic game for energy-efficient UAV swarm-assisted MEC with dynamic clustering and scheduling,” *IEEE Trans. Green Commun. Netw.*, vol. 9, no. 1, pp. 255–270, Mar. 2025.

[14] C. Liu, X. Xin, Y. Dai, and D. Xu, “Cost optimization of UAV swarm network for persistent emergency communication,” *IEEE Trans. Green Commun. Netw.*, vol. 10, pp. 1734–1748, 2026.

[15] G. Zhang, X. Ou, M. Cui, Q. Wu, S. Ma, and W. Chen, “Cooperative UAV enabled relaying systems: Joint trajectory and transmit power optimization,” *IEEE Trans. Green Commun. Netw.*, vol. 6, no. 1, pp. 543–557, Mar. 2022.

[16] H. Zhang, S. Wu, H. Fan, Z. Huang, W. Xue, C. Yu, S. Ibrahim, and H. Jin, “KubeSPT: Stateful pod teleportation for service resilience with live migration,” *IEEE Trans. Serv. Comput.*, vol. 18, no. 3, pp. 1500–1514, May–Jun. 2025.

[17] L. Ma, S. Yi, N. J. Carter, and Q. Li, “Efficient live migration of edge services leveraging container layered storage,” *IEEE Trans. Mobile Comput.*, vol. 18, no. 9, pp. 2020–2033, Sep. 2019.

[18] X. Zhang, C. Wang, Y. Zhu, J. Cao, and T. Liu, “Multi-agent deep reinforcement learning with trajectory prediction for task migration-assisted computation offloading,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 7, pp. 5839–5856, Jul. 2025.

[19] N. Zhao, Z. Ye, Y. Pei, Y.-C. Liang, and D. Niyato, “Multi-agent deep reinforcement learning for task offloading in UAV-assisted mobile edge computing,” *IEEE Trans. Wireless Commun.*, vol. 21, no. 9, pp. 6949–6960, Sep. 2022.

[20] C. Huang, G. Chen, P. Xiao, Y. Xiao, Z. Han, and J. A. Chambers, “Joint offloading and resource allocation for hybrid cloud and edge computing in SAGINs: A decision assisted hybrid action space deep reinforcement learning approach,” *IEEE J. Sel. Areas Commun.*, vol. 42, no. 5, pp. 1029–1043, May 2024.

[21] J. Achiam, D. Held, A. Tamar, and P. Abbeel, “Constrained policy optimization,” in *Proc. 34th Int. Conf. Mach. Learn. (ICML)*, vol. 70, pp. 22–31, 2017.

[22] A. Stooke, J. Achiam, and P. Abbeel, “Responsive safety in reinforcement learning by PID Lagrangian methods,” in *Proc. 37th Int. Conf. Mach. Learn. (ICML)*, vol. 119, pp. 9133–9143, 2020.

[23] D. Q. Mayne, J. B. Rawlings, C. V. Rao, and P. O. M. Scokaert, “Constrained model predictive control: Stability and optimality,” *Automatica*, vol. 36, no. 6, pp. 789–814, Jun. 2000, doi: 10.1016/S0005-1098(99)00214-9.
