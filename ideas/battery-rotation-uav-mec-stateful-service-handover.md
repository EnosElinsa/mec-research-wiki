# 电池轮换场景下无人机 MEC 有状态服务交接的可行性与在线调度

## 1. 场景总述与核心创新

灾后巡检、输电线路监测和偏远地区观测需要持续运行的空中计算服务。地面终端不断上传图像、视频片段和传感数据，无人机在服务区内完成分析并返回结果。无人机受电池容量限制，必须周期性返站换电。当前服务无人机离场时，内存中的运行状态、尚未提交的结果和任务队列都需要由替补机接管。

本文采用有重叠时间的交接方式。替补机沿已经通过安全检查的航路进入服务区，当前无人机继续处理任务，并通过 A2A 链路逐步传输可变状态。源机随后暂停写入，传完最后一部分状态并完成确认；替补机取得服务所有权，源机返航。

核心矛盾来自三条同时变化的链路。较高的 CPU 频率能够更快地消化任务队列，也会更快地产生新的可变状态；更晚的暂停时刻能够延长预拷贝时间，同时压缩源机的返航电量；有限的 A2A 带宽还要在多个交接事件之间共享。一次交接只有在任务队列、状态传输、服务中断和安全返航四方面同时可行时才能执行。

本文只研究一个问题：在轮换事件、候选替补机和安全航路已经给定的条件下，如何联合选择交接方案、CPU 频率和 A2A 带宽，使每次交接都满足最大中断时间与返航电量要求，并尽可能增大最紧张交接事件的可行余量。

模型范围固定如下：所有进入系统的任务已经通过上层接入控制；每个轮换事件必须执行；源机由当前服务关系确定；候选方案只描述替补机和暂停时刻。任务接纳、连续航迹和轮换触发由上层系统处理。写租约、版本确认和结果去重属于交接协议的执行条件，不作为优化变量。

本文的核心贡献是建立“状态增长—交接时机—安全返航”的联合可行性边界。该边界能够回答一个直接问题：在给定状态大小、处理负载、A2A 链路和剩余电量时，当前轮换还能否在不中断业务过久的条件下完成。论文的理论部分给出可行性条件和资源下界，算法部分在滚动窗口内提高最紧张交接事件的可行余量，实验部分用真实板卡测量状态增长和停机拷贝开销。这个问题具有明确的工程对象、可证明的边界和可复现实验，适合作为完整论文的主线。

## 2. 与最近邻工作的关系

### 2.1 电池、轨迹与任务调度

Ye 等的 *Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing* [1] 联合安排无人机飞行速度、任务卸载和换电，说明飞行、处理与返航电量需要共同规划。该工作要求无人机离开任务点前完成相应任务，没有描述运行状态向替补机转移的过程。

Li 等的 *A Reinforcement Learning-Based Stochastic Game for Energy-Efficient UAV Swarm-Assisted MEC With Dynamic Clustering and Scheduling* [2] 研究无人机群的动态聚类、应用放置、任务委托和能量补给。首领机返场补能时，机群通过重新调度维持服务。其模型没有跟踪源机继续计算期间产生的可变状态。

Zhao 等的 *Joint Optimization of Trajectory, Offloading, Caching, and Migration for UAV-Assisted MEC* [3] 联合考虑轨迹、用户关联、卸载、缓存和迁移，为多资源联合建模提供了参照。论文将通信中断和低电量离场列为后续方向，未建立电池触发的有状态交接过程。

### 2.2 任务迁移与服务迁移

Wang 等的 *Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks* [4] 面向用户移动迁移进行中的任务，迁移内容包括剩余输入和部分计算结果。无人机位置在其模型中固定，迁移在一个时隙内完成，因此没有预拷贝、暂停写入和停机拷贝三个阶段。

Feng 等的 *Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks* [5] 根据车辆移动预测联合决定服务迁移和无人机轨迹，目标是降低服务时延与长期迁移开销。该工作没有同时描述状态持续增长、源机返航电量和硬中断上限。

Shi 等的 *Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC* [6] 在慢时间尺度决定接入和服务迁移，在快时间尺度分配卸载、CPU 与带宽。论文指出，服务恢复中断约束会使迁移事件与时隙资源重新耦合。本文把这项耦合具体化为可变状态的产生与传输，并增加电池返航形成的暂停时限。

Han 等的 *Orchestrating Federated Learning in Space-Air-Ground Integrated Networks: Adaptive Data Offloading and Seamless Handover* [7] 在卫星覆盖窗口结束时传递训练数据和部分模型，使后继卫星继续训练。该工作证明计算状态可以跨移动节点递交，其系统不包含无人机电池、地面任务队列和共享 A2A 资源。

### 2.3 持续替换与协同接力

Liu 等的 *Cost Optimization of UAV Swarm Network for Persistent Emergency Communication* [8] 研究能量受限无人机群的周期替换、持续覆盖和返航储备。服务对象是通信连接，模型没有计算状态及停机拷贝。

Zhang 等的 *Cooperative UAV Enabled Relaying Systems: Joint Trajectory and Transmit Power Optimization* [9] 通过前后无人机重叠运行降低中继切换影响。其模型关注无线中继，不涉及 MEC 队列和运行状态。

### 2.4 本文保留的研究问题

现有工作已经分别处理了换电调度、持续替换、任务迁移、服务迁移和移动节点交接。本文保留的研究问题由三个不可分割的关系组成：

1. CPU 处理任务的同时产生新的待传状态；
2. 替补机到达和暂停时刻共同决定预拷贝窗口；
3. 源机完成停机拷贝后仍须保留安全返航电量。

在本知识库及本轮核对范围内，尚未发现一篇论文把这三个关系写入同一个硬可行域。这个结论属于本地文献范围内的归纳，投稿前仍需系统检索 live migration、pre-copy 和实时状态交接等外部研究。

## 3. 系统模型

考虑一个由多架无人机持续提供计算服务的多区域 UAV-MEC 系统。系统包含若干服务区域，每个区域由一架无人机负责接收和处理地面业务。当在役无人机需要返航换电时，替补机先进入服务区域并与源机建立 A2A 链路，随后通过预拷贝和停机拷贝接管运行状态。控制器只收集队列长度、电池余量、状态大小和信道下界等调度信息，不传输用户原始数据。所有无人机沿上层规划器给出的安全航路飞行，本文研究给定轮换事件下的交接方案与资源分配。

除特别说明外，数据量、计算量、时间、带宽、功率和能量的单位分别为 bit、cycle、s、Hz、W 和 J。

### 3.1 网络对象、集合与时间模型

服务区域、无人机和业务会话的集合分别记为

$$
\mathcal R=\{1,\ldots,R\},\qquad
\mathcal U=\{1,\ldots,U\},\qquad
\mathcal I=\{1,\ldots,I\}.
$$

会话 $i\in\mathcal I$ 位于区域 $r(i)\in\mathcal R$，区域 $r$ 内的会话集合为

$$
\mathcal I_r=\{i\in\mathcal I:r(i)=r\}.
$$

时间被划分为长度为 $\Delta$ 秒的时隙。控制器在时隙 $\tau$ 优化由 $W$ 个时隙组成的滚动窗口

$$
\mathcal W_\tau=\{\tau,\ldots,\tau+W-1\}.
$$

窗口内的轮换交接事件构成集合 $\mathcal N_\tau$。对事件 $n\in\mathcal N_\tau$，服务区域 $r_n$ 和源机 $u_n$ 已由当前服务关系确定。候选方案集合为 $\mathcal P_n$。方案 $p\in\mathcal P_n$ 指定替补机 $v_{np}$、预拷贝开始时隙 $s_{np}$ 和源机暂停写入时隙 $c_{np}$，并满足

$$
\tau\le s_{np}<c_{np}<\tau+W.
$$

每个候选方案均已通过航路、速度和碰撞间距检查。令 $x_{np}\in\{0,1\}$ 表示事件 $n$ 是否采用方案 $p$。选定方案后，区域 $r$ 在时隙 $t$ 的服务所有者记为 $o_r[t]$；停机拷贝确认前 $o_{r_n}[t]=u_n$，确认后 $o_{r_n}[t]=v_{np}$。因此，$o_r[t]$ 由交接结果递推，不是独立决策变量。

### 3.2 任务产生、状态与处理流程

令 $A_i[t]$ 表示会话 $i$ 在时隙 $t$ 已完成上行传输并进入服务队列的数据量，单位为 bit。地面上行链路采用保守速率下界 $\underline C_i^{\mathrm{up}}[t]$，因此

$$
A_i[t]\le \Delta\underline C_i^{\mathrm{up}}[t].
$$

$A_i[t]$ 是控制器在时隙开始时观测到的外生输入。终端或地面网关在收到结果确认前保留原始输入，替补机可以根据输入序号重放尚未完成的数据，A2A 链路只传输无法由输入重建的运行状态。

令 $Q_i[t]$ 表示时隙 $t$ 开始时会话 $i$ 的待处理数据量，$c_i$ 表示处理 1 bit 数据所需的 CPU 周期数，$f_i[t]$ 表示分配给会话 $i$ 的 CPU 频率。停机拷贝期间暂停任务执行。用 $\mathbb 1\{\cdot\}$ 表示指示函数，定义区域服务指示量

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

### 3.3 通信模型

交接事件 $n$ 在时隙 $t$ 获得的 A2A 带宽记为 $b_n[t]$，系统可用于状态交接的总带宽为 $B^{\mathrm A}$。候选目标机和航路不同，其 A2A 信道也不同。对方案 $p$，令 $\underline h_{np}[t]$ 表示保守信道功率增益，$P_{np}^{\mathrm A}$ 表示源机发射功率，$N_0$ 表示噪声功率谱密度。对应的 A2A 速率为

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

### 3.4 计算状态与交接过程

由于候选方案的开始时刻不同，状态估计器分别给出各方案开始预拷贝时的状态上界 $S_{np}^0$。令 $G_n[t]$ 表示事件 $n$ 中目标机尚未接收的状态量。若选择方案 $p$，则

$$
G_n[s_{np}]=S_{np}^0.
$$

运行状态由背景写入和任务处理共同产生。令 $\overline\delta_n^0$ 表示背景状态增长率上界，$\overline\eta_n$ 表示每处理 1 bit 输入所产生状态量的上界，则时隙 $t$ 的状态增长率为

$$
\overline\delta_n[t]
=
\overline\delta_n^0
+\overline\eta_n
\sum_{i\in\mathcal I_{r_n}}\frac{f_i[t]}{c_i}.
$$

在 $s_{np}\le t<c_{np}$ 的预拷贝阶段，未传状态量递推为

$$
G_n[t+1]
=
\left[
G_n[t]
+\overline\delta_n[t]\Delta
-C_{np}^{\mathrm A}[t]\Delta
\right]^+.
$$

源机在时隙 $c_{np}$ 暂停写入。冻结、状态应用和确认所需的固定时间分别为 $\tau_n^{\mathrm{freeze}}$、$\tau_n^{\mathrm{apply}}$ 和 $\tau_n^{\mathrm{ack}}$，其总和记为

$$
\tau_n^{\mathrm{fix}}
=
\tau_n^{\mathrm{freeze}}
+\tau_n^{\mathrm{apply}}
+\tau_n^{\mathrm{ack}}.
$$

若协议元数据大小为 $S_n^{\mathrm{meta}}$，则事件 $n$ 的服务中断时间为

$$
I_n
=
\tau_n^{\mathrm{fix}}
+
\frac{G_n[c_{np}]+S_n^{\mathrm{meta}}}
{C_{np}^{\mathrm A}[c_{np}]}.
$$

交接协议采用单写者租约。源机在停机状态和元数据全部确认前保留写权限，目标机获得新服务世代后才能提交结果。服务世代、确认记录和输入去重表由协议执行器维护，不作为优化变量。

### 3.5 能耗模型

令 $P_u^{\mathrm{mode}}[t]$ 表示无人机 $u$ 在时隙 $t$ 的飞行、悬停和航电功率。计算能耗采用 DVFS 模型，$\kappa_u$ 为板卡标定的计算能耗系数。令 $z_{un}[t]\in\{0,1\}$ 表示无人机 $u$ 是否参与事件 $n$ 的 A2A 传输，$P_{un}^{\mathrm A,tot}[t]$ 表示相应的总无线功率；源机侧包含发射功率与发射电路功率，目标机侧包含接收电路功率。无人机 $u$ 的时隙能耗为

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
z_{un}[t]P_{un}^{\mathrm A,tot}[t].
$$

三项分别对应飞行与航电、任务计算以及 A2A 收发。A2A 能耗按完整时隙计算，因而是实际传输能耗的保守上界。若 $E_u[t]$ 表示时隙开始时的剩余电量，$E_u^{\max}$ 表示电池容量，则

$$
E_u[t+1]=E_u[t]-E_u^{\mathrm{use}}[t],
\qquad
0\le E_u[t]\le E_u^{\max},
$$

换电完成后，电量恢复为 $E_u^{\max}$。源机 $u_n$ 从区域 $r_n$ 返航所需的保守能量记为 $\overline E_{u_n}^{\mathrm{ret}}[t]$，安全余量记为 $E_{u_n}^{\mathrm{res}}$。停机拷贝产生的计算和通信能耗已计入 $E_{u_n}^{\mathrm{use}}[t]$。

### 3.6 队列、中断与可行余量

每个会话的队列上限为 $Q_i^{\max}$。事件 $n$ 的业务中断上限为 $I_n^{\max}$。由于模型为停机拷贝预留一个时隙，实际采用的中断上限为

$$
\widetilde I_n^{\max}
=
\min\{I_n^{\max},\Delta\}.
$$

对选定方案 $p$，定义事件 $n$ 的交接可行余量为

$$
M_n
=
\left(\widetilde I_n^{\max}-\tau_n^{\mathrm{fix}}\right)
C_{np}^{\mathrm A}[c_{np}]
-
\left(G_n[c_{np}]+S_n^{\mathrm{meta}}\right).
$$

$M_n$ 的单位为 bit。$M_n\ge0$ 表示停机时隙能够传完剩余状态和协议元数据；$M_n$ 越大，交接对状态增长误差和链路下降的容忍范围越大。

由第 3.4 节的状态递推可得，任一可行方案都必须满足

$$
S_{np}^0
+
\sum_{t=s_{np}}^{c_{np}-1}
\overline\delta_n[t]\Delta
\le
\sum_{t=s_{np}}^{c_{np}-1}
C_{np}^{\mathrm A}[t]\Delta
+
\left(\widetilde I_n^{\max}-\tau_n^{\mathrm{fix}}\right)
C_{np}^{\mathrm A}[c_{np}]
-
S_n^{\mathrm{meta}}.
$$

左侧为暂停写入前累计需要同步的状态量，右侧为预拷贝和停机拷贝可承载的总状态量。该不等式给出传输侧的必要条件，源机返航能量还需满足第 4.3 节的电池约束。

### 3.7 合理假设及现实偏差

模型将轮换事件、候选替补机和安全航路视为上层规划结果，连续轨迹、轮换触发和换电站库存由上层系统处理。服务镜像预先部署在替补机上，终端或地面网关保存未确认输入，A2A 链路只传输不可重建的运行状态。若实际系统需要迁移服务镜像或队列数据，应将相应数据量并入 $S_{np}^0$，并在 $\tau_n^{\mathrm{fix}}$ 中加入启动时间。

状态增长率、A2A 速率和返航能耗均采用保守边界。同一区域同一时刻至多发生一次交接，停机阶段按一个完整时隙计量。这些假设使状态递推、服务所有权和返航条件能够在同一时间尺度上表示。实际误差无法由确定性边界覆盖时，可将相关约束改写为机会约束或分布鲁棒约束；多目标复制、多时隙停机和换电站排队需要另行扩展状态空间。

## 4. 优化问题

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

表示窗口 $\mathcal W_\tau$ 内的控制变量，其中 $\boldsymbol x_\tau=\{x_{np}\}$ 为交接方案选择，$\boldsymbol f_\tau=\{f_i[t]\}$ 为 CPU 分配，$\boldsymbol b_\tau=\{b_n[t]\}$ 为 A2A 带宽分配。队列 $Q_i[t]$、未传状态 $G_n[t]$、服务所有者 $o_r[t]$ 和电量 $E_u[t]$ 按第 3 章的状态方程递推。

### 4.1 目标函数

在满足任务队列、交接中断和安全返航要求的前提下，本文最大化所有轮换事件中的最小相对可行余量。令 $S_n^{\mathrm{ref}}>0$ 表示事件 $n$ 的状态大小参考量，目标函数为

$$
\max_{\boldsymbol z_\tau}
\quad
\min_{n\in\mathcal N_\tau}
\frac{M_n}{S_n^{\mathrm{ref}}},
$$

该目标为无量纲量，直接衡量窗口内最紧张交接事件对状态增长和链路误差的承受能力。能耗、队列和中断均作为可行性条件处理，目标函数只保留交接可行余量。

### 4.2 决策变量

| 变量 | 类型与范围 | 时间尺度 | 实际含义 |
|---|---|---|---|
| $x_{np}$ | 二元 | 每个轮换事件一次 | 为事件 $n$ 选择候选方案 $p$ |
| $f_i[t]$ | 连续，$f_i[t]\ge0$ | 每时隙 | 分配给会话 $i$ 的 CPU 频率 |
| $b_n[t]$ | 连续，$b_n[t]\ge0$ | 每时隙 | 分配给交接事件 $n$ 的 A2A 带宽 |

速率、状态增长率、中断时间、能耗和可行余量均由上述变量和第 3 章定义的系统状态计算得到。

### 4.3 约束条件

首先，每个轮换事件必须选择一个候选方案：

$$
\mathrm{C1}:\quad
\sum_{p\in\mathcal P_n}x_{np}=1,\qquad
x_{np}\in\{0,1\},
\quad \forall n\in\mathcal N_\tau.
$$

任务处理量不能超过当前队列，区域停机时 CPU 分配为零，并且同一无人机上的总 CPU 频率不能超过其计算能力：

$$
\mathrm{C2}:\quad
\begin{cases}
0\le Q_i[t]\le Q_i^{\max},\\
0\le f_i[t]\Delta
\le d_{r(i)}[t]c_i\bigl(Q_i[t]+A_i[t]\bigr),\\
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
x_{np}=1\Rightarrow
G_n[c_{np}]+S_n^{\mathrm{meta}}
\le
\bigl(\widetilde I_n^{\max}-\tau_n^{\mathrm{fix}}\bigr)
C_{np}^{\mathrm A}[c_{np}],
\end{cases}
$$

其中第三个条件同时要求 $\widetilde I_n^{\max}>\tau_n^{\mathrm{fix}}$。对满足 $x_{np}=1$ 的方案，$G_n[t]$ 按第 3.4 节递推。

最后，无人机的剩余电量必须保持在有效范围内，源机完成停机拷贝后还应保留返航能量和安全余量：

$$
\mathrm{C4}:\quad
\begin{cases}
0\le E_u[t+1]
=E_u[t]-E_u^{\mathrm{use}}[t]
\le E_u^{\max},\\[1mm]
x_{np}=1\Rightarrow
E_{u_n}[c_{np}+1]
\ge
\overline E_{u_n}^{\mathrm{ret}}[c_{np}+1]
+E_{u_n}^{\mathrm{res}}.
\end{cases}
$$

约束 C1 确定替补机和暂停时刻，C2 保证任务队列与计算资源可行，C3 约束状态传输和服务中断，C4 保证电池安全。候选集已包含航路和到达时序检查。时隙 $t$ 的资源动作只能依据当时已经观测到的队列、电量、信道和状态估计；交接确认失败时，目标机丢弃影子状态，控制器根据源机的剩余返航时间重新求解。

### 4.4 问题性质与主要难点

上述问题是带有限候选方案的在线鲁棒混合整数优化问题。$x_{np}$ 为离散变量，$f_i[t]$ 和 $b_n[t]$ 为连续变量。CPU 分配同时影响任务队列、状态增长和计算能耗，暂停时刻同时决定预拷贝长度和源机返航余量，这两组关系构成主要耦合。

固定 $\boldsymbol x_\tau$ 后，第 3.3 节的速率函数关于带宽是凹函数，状态增长率关于 CPU 分配是仿射函数，DVFS 能耗是凸函数。正部递推可以用两个线性或凸上图约束等价表示，最大化最小值目标可通过一个辅助标量改写。因此，固定方案后的资源分配子问题可构造成凸优化，离散方案则由枚举、分支定界或逻辑 Benders 方法处理。滚动求解只执行当前窗口的第一个时隙动作，不提供整个任务生命周期的离线全局最优保证。

## 5. 方法总结

### 5.1 原问题处理

首先为每个轮换事件生成候选方案。候选方案来自安全航路、替补机到达时刻和若干离散暂停时刻。第 3.6 节的传输必要条件用于删除状态容量明显不足的方案；第 3.5 节的返航能量下界用于删除无法安全返航的方案。

随后把问题分成两个层次：

1. 离散主问题选择每个事件的交接方案；
2. 连续子问题分配 CPU 和 A2A 带宽，并验证队列、状态、中断和返航约束。

协议世代号、确认记录和结果去重由执行器维护，它们不会扩大优化问题。

### 5.2 算法框架

算法包含四个模块：

1. **状态估计器**读取队列、电量、状态大小和保守信道参数；
2. **候选方案生成器**组合替补机与暂停时刻，并执行到达、轨迹和单事件可行性筛选；
3. **交接规划器**选择方案，连续资源分配器求解 CPU 与带宽；
4. **安全执行器**在动作下发前重新核对中断容量、版本确认和返航余量。

连续子问题不可行时，规划器删除对应组合或向离散主问题返回可行性割。可行时，算法记录最小相对可行余量并继续比较其他方案。

### 5.3 在线求解流程

1. 在时隙开始读取 $Q_i[t]$、$E_u[t]$、当前所有者和 A2A 信道下界。
2. 更新各候选方案的起始状态上界 $S_{np}^0$ 与状态增长率上界。
3. 根据替补机到达时刻、候选暂停时刻和安全航路生成 $\mathcal P_n$。
4. 使用传输容量与返航能量必要条件删除不可行方案。
5. 求解离散方案选择与连续 CPU、带宽分配问题。
6. 对第一时隙动作重新计算队列、停机拷贝容量和槽末返航电量。
7. 下发通过检查的动作；交接确认后更新服务所有者，窗口向前移动。

### 5.4 可行性、收敛性与复杂度

若候选方案集合有限，固定方案后的连续子问题满足凸性与强对偶条件，逻辑 Benders 可以在有限次主问题迭代后得到当前滚动窗口的最优解。该结论只针对当前窗口，不代表整个任务生命周期的离线全局最优。

当实际状态增长不超过 $\overline\delta_n[t]$、实际 A2A 速率不低于模型值、实际返航能耗不高于 $\overline E_u^{\mathrm{ret}}[t]$，并且交接协议固定开销不超过标定值时，满足 C1–C4 的第一时隙动作能够保证队列、中断和返航安全。任一误差超出边界时，安全执行器应提前暂停新的状态写入或取消本次交接，并报告可行性失效。

一个明确的可行基线是：选择最早到达的替补机，使用最大可用 A2A 带宽，CPU 只分配到维持 $Q_i^{\max}$ 所需的最低水平，并选择满足返航约束的最早暂停时刻。该策略若仍不可行，说明当前候选集内不存在通过单纯增加资源即可完成的交接。

设事件 $n$ 有 $|\mathcal P_n|$ 个候选方案。直接枚举的组合规模为 $\prod_n|\mathcal P_n|$；逻辑 Benders 通过可行性割减少组合搜索。在线实现还可限制每个事件的候选暂停时刻数量，并使用上一窗口的解热启动。

## 6. 实验与验证设计

### 6.1 对比方法

1. **直接停机拷贝**：不进行预拷贝，暂停后传输全部状态。
2. **固定提前量**：替补机到达后经过固定时间暂停写入。
3. **最早暂停**：满足替补机到达后立即选择最早可用暂停时刻。
4. **最大计算优先**：CPU 优先消化队列，剩余资源用于交接。
5. **本文方法**：联合选择候选方案、CPU 和 A2A 带宽。
6. **小规模精确解**：对少量事件枚举全部候选方案，验证分解算法的最优性。

### 6.2 关键消融

- 令 $\overline\eta_n=0$，忽略计算引起的状态增长；
- 固定 A2A 带宽，取消跨事件资源协调；
- 删除返航余量约束，观察计划是否产生无法安全离场的动作；
- 用平均信道和平均状态增长替代保守边界；
- 固定暂停时刻，只优化 CPU 和带宽。

### 6.3 指标与压力场景

主要指标包括最小相对可行余量、交接中断时间、未传状态峰值、队列上限违约率、交接成功率、源机返航余量、系统能耗和在线求解时间。

压力场景包括高任务到达率、状态增长突增、A2A 带宽下降、多个交接窗口重叠、替补机延迟到达、电池容量衰减和返航能耗估计偏差。敏感性分析覆盖 $S_{np}^0$、$\overline\eta_n$、$I_n^{\max}$、$B^{\mathrm A}$、候选暂停时刻数量和保守误差界。

### 6.4 仿真到实体验证

先在两块边缘计算板卡上运行可持续写入的视觉任务，测量 CPU 频率、处理吞吐量、状态增长率、冻结时间、应用时间和确认时间。随后用网络仿真器重放 A2A 速率和替补机到达过程。最后搭建两台无人机计算节点的硬件在环平台，执行预拷贝、暂停写入、最后拷贝、租约切换和源机返航检查。

以下结果会直接削弱或否定本文主张：

1. 状态增长与 CPU 频率没有稳定关系，无法得到可用上界；
2. 在可行边界附近，模型频繁判断可行而实测交接失败；
3. 联合调度相对固定暂停策略不能提高最小可行余量；
4. 返航约束对暂停时刻和交接可行域几乎没有影响；
5. 停机拷贝固定开销长期大于业务允许的最大中断时间。

## 7. 新颖性边界、风险与备选收缩方案

最可能重叠的外部方向包括虚拟机或容器的 pre-copy/live migration、实时系统检查点、移动边缘服务迁移和电池驱动的无人机替换。投稿前需要确认是否已有工作同时把计算诱发的状态增长、替补机到达、停机中断和返航电量写入同一可行性条件。

模型最脆弱的假设是状态增长率可被保守估计、A2A 速率存在稳定下界、服务镜像已经预置，以及源机与目标机不会同时失效。算法风险主要来自候选方案数量过多、保守边界过紧和在线求解超时。

若多区域版本规模过大，可收缩为单区域、两架无人机和一个持续业务流。该版本只优化一个暂停时刻、CPU 和 A2A 带宽，证明状态增长、停机容量与返航储备的可行性定理，并在两块板卡上验证。它仍保留本文最关键的研究问题。

## 8. 证据来源

1. Dongmei Ye et al., “Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing,” IEEE Transactions on Mobile Computing, 2026, DOI: 10.1109/TMC.2025.3601743. 本地证据：wiki/sources/ye-2026-flight-speed-battery-swapping.md；raw/sources/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md。
2. Jialiuyuan Li et al., “A Reinforcement Learning-Based Stochastic Game for Energy-Efficient UAV Swarm-Assisted MEC With Dynamic Clustering and Scheduling,” IEEE Transactions on Green Communications and Networking, 2025, DOI: 10.1109/TGCN.2024.3424449. 本地证据：wiki/sources/li-2025-stochastic-game-uav-swarm.md。
3. Mingxiong Zhao et al., “Joint Optimization of Trajectory, Offloading, Caching, and Migration for UAV-Assisted MEC,” IEEE Transactions on Mobile Computing, 2025, DOI: 10.1109/TMC.2024.3486995. 本地证据：wiki/sources/zhao-2025-traj-offload-cache-migration.md。
4. Liang Wang et al., “Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks,” IEEE Transactions on Services Computing, 2025, DOI: 10.1109/TSC.2025.3576644. 本地证据：wiki/sources/wang-2025-ctmig-task-migration-uav.md。
5. Wei Feng et al., “Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks,” IEEE Transactions on Mobile Computing, 2026, DOI: 10.1109/TMC.2026.3700894. 本地证据：wiki/sources/feng-2026-prediction-service-migration.md。
6. You Shi et al., “Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC,” IEEE Transactions on Wireless Communications, 2023, DOI: 10.1109/TWC.2023.3290005. 本地证据：wiki/sources/shi-2023-two-timescale-migration-rerouting.md。
7. Dong-Jun Han et al., “Orchestrating Federated Learning in Space-Air-Ground Integrated Networks: Adaptive Data Offloading and Seamless Handover,” IEEE Journal on Selected Areas in Communications, 2024, DOI: 10.1109/JSAC.2024.3459090. 本地证据：wiki/sources/han-2024-sagin-fl-handover.md。
8. Changtong Liu et al., “Cost Optimization of UAV Swarm Network for Persistent Emergency Communication,” IEEE Transactions on Green Communications and Networking, 2026, DOI: 10.1109/TGCN.2025.3649278. 本地证据：wiki/sources/liu-2026-usp-nfrp-emergency-communication.md。
9. Guangchi Zhang et al., “Cooperative UAV Enabled Relaying Systems: Joint Trajectory and Transmit Power Optimization,” IEEE Transactions on Green Communications and Networking, 2022, DOI: 10.1109/TGCN.2021.3108147. 本地证据：wiki/sources/zhang-2022-uav-relay-substitution.md。

## 附录 A：检索与自我迭代记录

### A.1 证据范围

前期使用 3 个只读子代理，分别完成证据映射、最近邻反证和模型审计。共执行 23 次本地知识库检索，完整读取 34 个 Wiki 页面，并核对 15 份原始解析文档。检索模式为 hybrid，vectorHits 为 0，因此相关工作判断只覆盖本地词法与混合检索结果。

### A.2 方案收缩

前期比较了有状态撤离交接、换电库存协同和冗余执行三个方向。库存方向需要增加站点排队与电池库存，冗余执行方向容易转化为重复计算资源分配，最终保留有状态交接。

本轮进一步删除任务接纳、交接触发、源机选择、连续轨迹和协议状态优化。最终模型只保留交接方案、CPU 与 A2A 带宽三类控制量，以及方案选择、任务计算、状态传输和电池返航四类约束。

### A.3 完整性检查

- 各集合、索引、状态和单位均在首次使用前定义；
- 三类控制量都进入目标函数或硬约束；
- 任务队列、未传状态和电量形成闭合递推；
- 交接中断与返航储备都有直接可计算的硬约束；
- 行内公式统一使用单美元符号，块级公式统一使用双美元符号；
- 正文没有实验结果、性能提升比例或全局新颖性结论；
- 仍需外部核对 live migration、pre-copy 和实时检查点文献。
