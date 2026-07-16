---
type: concept
title: "面向处理后信息新鲜度的 HAPS-UAV ISAC 在线资源分配"
tags: [haps, uav, isac, age-of-information, queue, resource-allocation, deep-reinforcement-learning]
related:
  - "[[kanani-2026-haps-uav-isac]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[zhao-2026-mappo-jscc-aec]]"
  - "[[bai-2026-aoi-uav-isac]]"
  - "[[liu-2025-aoi-iscc-five-stage]]"
  - "[[age-of-information]]"
  - "[[high-altitude-platform-station]]"
  - "[[integrated-sensing-and-communication]]"
created: 2026-07-14
updated: 2026-07-16
---

# HAPS 辅助多无人机 ISAC 中面向处理后信息新鲜度的在线资源分配

## I. 引言

集成感知与通信（integrated sensing and communication，ISAC）通过共享频谱、射频前端和阵列处理能力，使无线网络能够同时提供数据传输与环境感知。低空交通管理、灾区监测和远程设施巡检等应用既要维持地面用户的通信连接，也要持续更新移动目标的位置或状态。无人机（unmanned aerial vehicle，UAV）具有灵活部署和视距链路优势，能够作为低空 ISAC 接入点；单架无人机的覆盖、阵列规模和计算能力有限，多无人机协同已成为扩大感知范围和通信容量的重要方式 [1]。

高空平台站（high-altitude platform station，HAPS）可为多架无人机提供大范围回传、集中控制与计算资源。现有 HAPS-UAV ISAC 架构已经让多架 MIMO 无人机同时服务通信用户和感知地面目标，并经 D 波段定向链路把回波上传至 HAPS [2]；相邻研究还考虑了 HAPS 全双工 ISAC、感知数据卸载和多无人机通信—感知联合优化 [3]–[5]。这些工作主要用回波功率、雷达估计精度、通信速率或用户 SINR 评价一个时隙内的物理层质量。

目标状态只有经过回波传输和融合计算后才能被控制系统使用。多架无人机同时产生感知更新时，有限的 UAV-HAPS 回传带宽和 HAPS 计算能力会形成等待与抢占。较高的感知频率可以生成更多更新，也可能反复替换尚未传完或尚未处理的旧更新，造成传输与计算资源浪费；即使某次回波功率很高，排队过久的处理结果仍可能失去时效。已有 UAV-ISAC 研究已经把信息年龄（age of information，AoI）用于衡量目标状态的新鲜度 [6], [7]，HAP-UAV 感知计算研究也考虑了卸载和处理时延 [8]–[10]，但这些模型尚未把多无人机 ISAC 回波、UAV 回传缓冲、HAPS 计算缓冲和处理完成后的 AoI 刷新写入同一状态过程。

本文沿用文献 [2] 的两层 HAPS-UAV ISAC 架构。多架无人机在第一阶段向各自关联的地面用户发送数据，并从预先分配的目标集合中选择目标进行感知；第二阶段使用共享 D 波段带宽向 HAPS 回传回波数据。HAPS 对已接收的更新进行融合计算，只有处理完成的更新才能刷新相应目标的 AoI。为避免陈旧更新持续占用资源，UAV 与 HAPS 均采用按目标划分的最新更新保留缓冲：同一目标的新更新到达时，尚未完成的旧更新被替换。用户关联、无人机位置和波束方向由较慢时间尺度的部署与波束模块给出，本文只优化目标激活、感知功率、回传带宽和 HAPS CPU。

上述资源共同决定端到端新鲜度。提高目标感知功率能够满足感知 SNR 门限，却会压缩同一无人机的通信功率；增加某个目标的回传带宽可以缩短 UAV 缓冲时间，同时减少其他更新可用的 D 波段资源；增加 HAPS CPU 可以促使一个更新尽快完成，也会延后其他目标的 AoI 重置。当前感知动作还会改变两个缓冲区的后续状态。本文以长期加权平均处理后 AoI 为唯一优化目标，在通信 SINR、感知 SNR、无人机功率、共享回传带宽和 HAPS 计算容量约束下进行在线调度。

该问题包含离散目标激活与连续功率、带宽和 CPU 分配，且离散激活结果先决定连续动作的维度与可行域。直接输出全部变量的策略容易选择物理层不可感知的目标，或产生通信功率不足、带宽和 CPU 超配等动作。AoI 又在更新完成时才重置，动作收益会经过回传和计算两个缓冲区延迟显现。已有动态 UAV-ISAC 与多目标强化学习方法能够处理时变状态 [14]–[17]，但没有利用上述“目标激活—物理层可行性—双缓冲完成”的依赖顺序。本文据此设计队列感知的可行性引导混合动作 PPO（queue-aware feasibility-guided hybrid PPO，QF-HPPO）：离散策略先在物理可行候选中选择感知目标，条件连续策略再生成资源动作，小型凸投影在执行前满足当前帧的硬资源约束，价值网络则显式接收两个缓冲区的剩余工作量、时间戳和 AoI。

本文的主要贡献概括如下：

1. 在已有 HAPS-UAV ISAC 架构上增加端到端感知更新生命周期，建立 UAV 最新更新缓冲、HAPS 最新更新缓冲和处理完成后 AoI 重置模型，使回波质量、回传等待和融合计算可以在同一状态递推中评价。
2. 构建长期处理后 AoI 最小化问题，只保留目标激活、感知功率、UAV-HAPS 带宽和 HAPS CPU 四类运行层决策，并以通信、感知和资源约束限定可行域。
3. 设计 QF-HPPO 算法，以物理可行候选掩码处理离散目标激活，以条件连续策略和凸投影分配功率、带宽与 CPU，并通过双缓冲状态训练策略学习延迟完成收益。

本文其余内容安排如下。第 II 节回顾 HAPS-UAV ISAC、感知计算新鲜度和在线资源调度方面的研究；第 III 节建立系统模型并给出问题表述；第 IV 节介绍 QF-HPPO；第 V 节给出实验设计。新颖性边界与模型风险列于附录。

## II. 相关工作

本节按照引言中的问题链回顾三类工作。HAPS-UAV ISAC 研究给出本文继承的网络架构；AoI 与感知计算研究说明感知结果需要经过传输和处理才能产生时效价值；在线资源调度研究提供混合决策的求解基础。各小节分别说明已有能力和仍未建模的状态关系。

### A. HAPS-UAV 与多无人机 ISAC 架构

Kanani 等研究由多架 MIMO 无人机和一架 HAPS 组成的两层 ISAC 系统。无人机同时向地面用户发送通信信号和目标探测信号，并将接收的回波经 D 波段链路传至 HAPS；优化变量包括无人机位置、通信波束和感知波束，目标是提高 HAPS 接收回波功率和最小用户 SINR [2]。Benaya 等让 HAPS 搭载全双工 ISAC 基站，并把部分感知数据卸载到地面 MEC 服务器，在雷达、保密、卸载和功率约束下联合优化收发波束与友好干扰无人机轨迹 [3]。前者为本文提供直接的 UAV 感知与 HAPS 接收架构，后者说明感知数据会形成实际计算负载。

多无人机 ISAC 研究进一步联合考虑通信用户、感知目标和空中资源。Guo 等优化三维轨迹、功率、用户关联和目标关联，保持通信和感知两个独立目标并输出 Pareto 解集 [4]；Zhu 等利用目标定位 CRB 初始化多无人机 Q 表，再学习用户和功率分配 [5]；Lyu 等联合优化单无人机机动与波束成形，在通信和感知约束之间分配阵列与功率资源 [19]。这些模型能够刻画通信—感知物理层权衡，其感知价值在回波接收或估计质量计算时确定，没有继续追踪回波进入 HAPS 后的等待和处理完成时刻。

### B. 感知计算与信息新鲜度

Bai 等研究单无人机跟踪移动目标并向多个地面用户发送目标更新，以长期平均 AoI 为目标联合控制轨迹和通信/感知波束 [6]。Liu 等把雷达感知、本地计算和结果传输安排在同一时隙，联合优化感知数据量和 AoI [7]。这两项工作表明感知精度、传输资源和信息新鲜度存在直接耦合；前者没有 HAPS 与计算队列，后者把计算和传输限制在一个时隙内，没有跨时隙积压。

HAP-UAV 感知计算研究已经引入分层处理。Zhao 等在 HAP 辅助的多无人机系统中联合优化感知次数、轨迹、功率、卸载比例和子载波，以降低任务完成时间并稳定能耗 [8]；Zhou 等让多架无人机处理或向 HAP 卸载雷达感知数据，在感知数据量和系统能耗之间进行优化 [9]；Song 等研究单 UAV 与 HAP 协同 MEC 的 AoI—能耗权衡，并用多目标 PPO 输出非支配策略 [10]。这些工作分别覆盖 HAP 处理、雷达数据卸载和 HAP-UAV AoI，但其感知输入来自地面传感任务或在数据收集时刷新 AoI。本文把 AoI 重置延后到 HAPS 完成回波融合计算的时刻，并显式保留 UAV 回传缓冲与 HAPS 计算缓冲。

### C. 动态混合资源调度

分层空中计算中的混合决策通常采用分解或学习方法。Jia 等以匹配和启发式方法处理 IoT-UAV-HAP 的任务关联与计算位置 [11]；Nabi 和 Moh 先用匹配确定用户卸载与 UAV 关联，再用 SAC 分配 UAV-HAP 卸载比例和两层 CPU [12]；Jia 等在不确定信道下通过分布鲁棒机会约束、CVaR 和原始分解处理 UAV-HAP 任务卸载与资源分配 [13]。这些方法为 HAPS 资源分配提供了成熟基础，也说明离散关联与连续资源可以按依赖顺序处理。

在线 UAV-ISAC 研究已采用多智能体强化学习应对移动目标和时变信道。Wang 等联合控制多无人机信道、运动和功率，以兼顾车辆服务、感知信息和能耗 [14]；Wu 等将定位误差映射为预期通信速率，再联合调整感知周期、用户关联、位置和带宽 [15]；Qin 等用深度强化学习处理多无人机 ISAC 的关联、轨迹和功率 [16]。Ye 等进一步以偏好权重为输入，用混合专家网络适应不同通信—感知目标权重 [17]。因此，动态环境、多目标偏好或通用 DRL 均不足以构成本文的方法差异。

本文算法针对的是双缓冲处理链产生的决策顺序：目标激活决定所需感知功率和后续回传对象，连续资源决定更新在两个缓冲区中的完成速度，只有 HAPS 计算完成才产生 AoI 收益。QF-HPPO 用候选掩码和可行性投影处理前两层硬约束，并把缓冲工作量、生成时间戳和处理后 AoI 共同输入价值网络，以学习延迟完成收益。

## III. 系统模型与问题建模

本文对文献 [2] 的 HAPS-UAV ISAC 架构作运行层扩展。基础架构保留多架 MIMO 无人机、地面通信用户、地面感知目标、sub-6 GHz 空地接入、D 波段 UAV-HAPS 回传以及 HAPS 集中控制。用户关联、目标归属、无人机位置和波束方向由上层部署与物理层模块更新，在一个运行窗口内作为已知输入。本文新增按目标划分的 UAV 回传缓冲、HAPS 计算缓冲和处理后 AoI 状态，并在每帧调度目标激活、感知功率、回传带宽与 HAPS CPU。

### A. 网络对象与时间模型

无人机、通信用户和感知目标的集合分别记为

$$
\mathcal M=\{1,\ldots,M\},\qquad
\mathcal K=\{1,\ldots,K\},\qquad
\mathcal J=\{1,\ldots,J\}.
$$

无人机 $m\in\mathcal M$ 服务的用户集合和目标集合分别为 $\mathcal K_m\subseteq\mathcal K$ 与 $\mathcal J_m\subseteq\mathcal J$。目标集合满足

$$
\mathcal J_m\cap\mathcal J_{m'}=\varnothing,
\quad m\ne m',
\qquad
\bigcup_{m\in\mathcal M}\mathcal J_m=\mathcal J,
$$

即一个运行窗口内每个目标由一架预先指定的无人机负责。目标 $j$ 的负责无人机记为 $m(j)$。固定归属减少频繁跨无人机切换，目标重分配可由较慢时间尺度的部署模块完成。

系统在连续帧序列上运行，帧索引集合为

$$
\mathcal T=\mathbb Z_{\ge0}.
$$

每帧长度为 $\Delta=\tau^{\mathrm I}+\tau^{\mathrm H}$ 秒。第一阶段长度为 $\tau^{\mathrm I}$，无人机同时执行地面通信和目标感知；第二阶段长度为 $\tau^{\mathrm H}$，无人机向 HAPS 回传回波数据，HAPS 并行处理此前已经完整接收的更新。当前帧完成回传的更新从下一帧开始获得 CPU 服务，这一帧级流水线避免在同一阶段内假设零时延串行回传与计算。

帧 $t$ 开始时，无人机 $m$、用户 $k$、目标 $j$ 和 HAPS 的三维位置分别记为 $\boldsymbol q_m[t]$、$\boldsymbol u_k[t]$、$\boldsymbol v_j[t]$ 与 $\boldsymbol q_{\mathrm H}$。HAPS 位置在运行窗口内固定；无人机和地面对象的位置由导航与跟踪模块提供。为描述移动过程的一阶状态，分别用 $\boldsymbol\xi_m^{q}[t]$、$\boldsymbol\xi_k^{u}[t]$ 和 $\boldsymbol\xi_j^{v}[t]$ 记录相应对象的速度、航向及移动模型所需的其他参数；恒速转弯模型中的转弯角速度也包含在 $\boldsymbol\xi_j^{v}[t]$ 中。控制器观测当前信道、位置、移动状态、缓冲工作量、更新生成时间戳和处理后 AoI，然后生成本帧动作。

### B. 地面通信与目标感知模型

无人机 $m$ 配备 $G_m$ 阵元天线。根据当前用户信道和目标预测方向，物理层模块分别生成单位范数通信波束 $\overline{\boldsymbol w}_{mk}[t]\in\mathbb C^{G_m}$ 和感知波束 $\overline{\boldsymbol r}_{mj}[t]\in\mathbb C^{G_m}$。这些方向可由正则化零迫和阵列导向方法得到 [6], [19]，本文不把复波束向量作为在线决策变量。

二元变量 $a_j[t]\in\{0,1\}$ 表示是否在帧 $t$ 感知目标 $j$。分配给该目标的感知功率记为 $p_j^{\mathrm S}[t]$，单位为 W。无人机 $m$ 的最大射频功率为 $P_m^{\max}$，其剩余通信功率定义为

$$
p_m^{\mathrm C}[t]
=
P_m^{\max}
-\sum_{j\in\mathcal J_m}p_j^{\mathrm S}[t].
$$

用户 $k\in\mathcal K_m$ 获得的通信功率比例为 $\eta_{mk}\ge0$，并满足 $\sum_{k\in\mathcal K_m}\eta_{mk}=1$。在第一阶段，无人机 $m$ 的发射信号为

$$
\boldsymbol x_m[t]
=
\sum_{k\in\mathcal K_m}
\sqrt{p_m^{\mathrm C}[t]\eta_{mk}}
\,\overline{\boldsymbol w}_{mk}[t]s_{mk}[t]
+
\sum_{j\in\mathcal J_m}
\sqrt{p_j^{\mathrm S}[t]}
\,\overline{\boldsymbol r}_{mj}[t]s_{mj}^{\mathrm S}[t],
$$

其中 $s_{mk}[t]$ 和 $s_{mj}^{\mathrm S}[t]$ 分别为单位功率的通信符号和感知符号。不同无人机使用正交接入子带，因而地面接入模型只保留同一无人机内部的通信—感知干扰。这一特化用于隔离 HAPS 处理链的影响，频谱复用可在扩展实验中加入。

无人机 $m$ 到用户 $k$ 的信道向量记为 $\boldsymbol h_{mk}[t]\in\mathbb C^{G_m}$，接收噪声功率为 $\sigma_k^2$。用户 $k\in\mathcal K_m$ 的信干噪比为

$$
\gamma_{mk}[t]
=
\frac{
p_m^{\mathrm C}[t]\eta_{mk}
\left|\boldsymbol h_{mk}^{H}[t]\overline{\boldsymbol w}_{mk}[t]\right|^2
}{
\displaystyle
\sum_{\ell\in\mathcal K_m\setminus\{k\}}
p_m^{\mathrm C}[t]\eta_{m\ell}
\left|\boldsymbol h_{mk}^{H}[t]\overline{\boldsymbol w}_{m\ell}[t]\right|^2
+
\displaystyle
\sum_{j\in\mathcal J_m}
p_j^{\mathrm S}[t]
\left|\boldsymbol h_{mk}^{H}[t]\overline{\boldsymbol r}_{mj}[t]\right|^2
+\sigma_k^2
}.
$$

定义无感知发射时的基准通信 SINR 为

$$
\gamma_{mk}^{(0)}[t]
=
\left.
\gamma_{mk}[t]
\right|_{p_j^{\mathrm S}[t]=0,\ \forall j\in\mathcal J_m}.
$$

上层部署、关联和波束模块应保证 $\gamma_{mk}^{(0)}[t]\ge\gamma_k^{\min}$。若该基础条件不成立，仅关闭感知也无法满足通信服务要求，控制器将当前配置交由上层模块重新关联或更新波束，而不在该帧执行 QF-HPPO。该条件保证后文的空感知动作具有物理可行性。

无人机 $m$ 与目标 $j\in\mathcal J_m$ 的等效双程感知信道向量记为 $\boldsymbol g_{mj}[t]\in\mathbb C^{G_m}$，感知接收噪声功率为 $\sigma_{mj,\mathrm S}^2$。对应的感知 SNR 写为

$$
\Gamma_{mj}[t]
=
\frac{
p_j^{\mathrm S}[t]
\left|\boldsymbol g_{mj}^{H}[t]\overline{\boldsymbol r}_{mj}[t]\right|^2
}{
\displaystyle
\sum_{k\in\mathcal K_m}
p_m^{\mathrm C}[t]\eta_{mk}
\left|\boldsymbol g_{mj}^{H}[t]\overline{\boldsymbol w}_{mk}[t]\right|^2
+
\displaystyle
\sum_{\ell\in\mathcal J_m\setminus\{j\}}
p_\ell^{\mathrm S}[t]
\left|\boldsymbol g_{mj}^{H}[t]\overline{\boldsymbol r}_{m\ell}[t]\right|^2
+\sigma_{mj,\mathrm S}^2
}.
$$

当 $a_j[t]=1$ 时，系统要求 $\Gamma_{m(j)j}[t]$ 达到目标 $j$ 的感知门限 $\Gamma_j^{\min}$。一次合格感知生成大小为 $D_j$ bit 的带时间戳更新，处理每 bit 更新需要 HAPS 执行 $c_j$ 个 CPU cycle。$D_j$ 和 $c_j$ 由感知模式与融合算法确定，在一个运行窗口内固定。

### C. UAV-HAPS 回传与最新更新缓冲

目标 $j$ 的更新首先存入负责无人机 $m(j)$ 的回传缓冲。帧 $t$ 开始时，该缓冲的剩余数据量和生成时间戳分别记为 $Q_j^{\mathrm U}[t]$ bit 与 $g_j^{\mathrm U}[t]$。当 $Q_j^{\mathrm U}[t]=0$ 时，$g_j^{\mathrm U}[t]$ 的数值不参与状态更新。新更新采用替换策略：若帧 $t$ 激活目标 $j$，此前尚未传完的旧更新被丢弃。第一阶段结束后的缓冲状态为

$$
\widetilde Q_j^{\mathrm U}[t]
=
a_j[t]D_j+\bigl(1-a_j[t]\bigr)Q_j^{\mathrm U}[t],
$$

$$
\widetilde g_j^{\mathrm U}[t]
=
a_j[t]t+\bigl(1-a_j[t]\bigr)g_j^{\mathrm U}[t].
$$

系统为目标 $j$ 的回传分配带宽 $b_j[t]$ Hz。HAPS 的共享 D 波段总带宽为 $B^{\mathrm H}$。负责无人机的固定回传功率为 $P_{m(j)}^{\mathrm H}$，UAV-HAPS 信道功率增益为 $h_{m(j)}^{\mathrm H}[t]$，噪声功率谱密度为 $N_0$ W/Hz。回传速率为

$$
R_j^{\mathrm H}[t]
=
b_j[t]\log_2\!\left(
1+
\frac{P_{m(j)}^{\mathrm H}h_{m(j)}^{\mathrm H}[t]}
{N_0b_j[t]}
\right),
$$

单位为 bit/s；当 $b_j[t]=0$ 时，按连续延拓定义 $R_j^{\mathrm H}[t]=0$。本帧最多传输

$$
S_j^{\mathrm B}[t]
=
\min\left\{
\widetilde Q_j^{\mathrm U}[t],
R_j^{\mathrm H}[t]\tau^{\mathrm H}
\right\}
$$

bit。完整更新传输指示量定义为

$$
\chi_j^{\mathrm B}[t]
=
\mathbb 1\left\{
\widetilde Q_j^{\mathrm U}[t]>0,
\ S_j^{\mathrm B}[t]=\widetilde Q_j^{\mathrm U}[t]
\right\}.
$$

因此，无人机缓冲递推为

$$
Q_j^{\mathrm U}[t+1]
=
\left[
\widetilde Q_j^{\mathrm U}[t]-S_j^{\mathrm B}[t]
\right]^+.
$$

与剩余数据对应的生成时间戳递推为

$$
g_j^{\mathrm U}[t+1]
=
\mathbb 1\!\left\{Q_j^{\mathrm U}[t+1]>0\right\}
\widetilde g_j^{\mathrm U}[t].
$$

若 $\chi_j^{\mathrm B}[t]=1$，该更新在帧末进入 HAPS，所需计算量为 $D_jc_j$ cycle，生成时间戳为 $\widetilde g_j^{\mathrm U}[t]$。若新更新替换了尚未传完的旧更新，UAV 侧替换事件记为

$$
d_j^{\mathrm U}[t]
=
a_j[t]\mathbb 1\{Q_j^{\mathrm U}[t]>0\},
$$

该量只用于实验分析，不进入优化目标。

### D. HAPS 计算缓冲与处理后 AoI

HAPS 为每个目标维护一个计算缓冲。帧 $t$ 开始时，目标 $j$ 对应更新的剩余计算量和生成时间戳分别记为 $Q_j^{\mathrm H}[t]$ cycle 与 $g_j^{\mathrm H}[t]$。与 UAV 侧一致，HAPS 只保留同一目标的最新更新。帧 $t$ 开始时可用的缓冲状态参与本帧计算；本帧末完成回传的更新只更新下一帧的 HAPS 缓冲。因此，帧 $t$ 分配给目标 $j$ 的 CPU 频率记为 $f_j[t]$ cycle/s，实际完成的计算量为

$$
S_j^{\mathrm C}[t]
=
\min\left\{
Q_j^{\mathrm H}[t],
f_j[t]\tau^{\mathrm H}
\right\}.
$$

计算完成指示量为

$$
\chi_j^{\mathrm C}[t]
=
\mathbb 1\left\{
Q_j^{\mathrm H}[t]>0,
\ S_j^{\mathrm C}[t]=Q_j^{\mathrm H}[t]
\right\}.
$$

完成本帧计算后、接收新回传更新前的剩余计算量为

$$
\widehat Q_j^{\mathrm H}[t]
=
\left[Q_j^{\mathrm H}[t]-S_j^{\mathrm C}[t]\right]^+.
$$

若 $\chi_j^{\mathrm B}[t]=1$，新完成回传的更新在帧末替换 $\widehat Q_j^{\mathrm H}[t]$ 中尚未处理完的旧更新。由此，下一帧的 HAPS 缓冲递推为

$$
Q_j^{\mathrm H}[t+1]
=
\chi_j^{\mathrm B}[t]D_jc_j
+
\bigl(1-\chi_j^{\mathrm B}[t]\bigr)
\widehat Q_j^{\mathrm H}[t],
$$

$$
g_j^{\mathrm H}[t+1]
=
\chi_j^{\mathrm B}[t]\widetilde g_j^{\mathrm U}[t]
+
\bigl(1-\chi_j^{\mathrm B}[t]\bigr)
\mathbb 1\!\left\{\widehat Q_j^{\mathrm H}[t]>0\right\}
g_j^{\mathrm H}[t].
$$

HAPS 侧的替换事件记为

$$
d_j^{\mathrm H}[t]
=
\chi_j^{\mathrm B}[t]
\mathbb 1\{\widehat Q_j^{\mathrm H}[t]>0\}.
$$

该量同样只作为诊断指标。上述更新忽略过期任务的剩余工作量，因此与最新更新保留协议一致。

目标 $j$ 在帧 $t$ 开始时的处理后 AoI 记为 $A_j[t]$，单位为帧。它表示当前可用目标状态距其生成时刻经过的帧数。若 HAPS 在帧 $t$ 完成目标 $j$ 的计算，结果在帧末可用，下一帧 AoI 重置为从生成帧到完成帧末的系统时间；否则 AoI 增加 1，即

$$
A_j[t+1]
=
\chi_j^{\mathrm C}[t]
\bigl(t+1-g_j^{\mathrm H}[t]\bigr)
+
\bigl(1-\chi_j^{\mathrm C}[t]\bigr)
\bigl(A_j[t]+1\bigr).
$$

实际时间单位的 AoI 为 $A_j[t]\Delta$ 秒。该定义把感知生成、回传等待和 HAPS 计算等待全部纳入新鲜度，并避免在 UAV 捕获回波或 HAPS 收到数据时提前重置 AoI。

### E. 优化问题

目标 $j$ 的重要性权重记为 $\omega_j>0$，并满足 $\sum_{j\in\mathcal J}\omega_j=1$。本文最小化长期加权平均处理后 AoI：

$$
\mathrm{P1}:\quad
\min_{\{a_j[t],p_j^{\mathrm S}[t],b_j[t],f_j[t]\}}
\limsup_{T\to\infty}
\frac{1}{T}
\mathbb E\!\left[
\sum_{t=0}^{T-1}
\sum_{j\in\mathcal J}
\omega_jA_j[t]\Delta
\right].
$$

期望针对用户和目标移动、接入信道及 UAV-HAPS 信道的随机演化。决策变量及其时间尺度如下。

| 变量 | 类型与范围 | 时间尺度 | 实际含义 |
|---|---|---|---|
| $a_j[t]$ | 二元，$\{0,1\}$ | 每帧 | 是否生成目标 $j$ 的新感知更新 |
| $p_j^{\mathrm S}[t]$ | 连续，$[0,P_{m(j)}^{\max}]$ | 每帧 | 目标 $j$ 的感知发射功率 |
| $b_j[t]$ | 连续，$[0,B^{\mathrm H}]$ | 每帧 | 目标 $j$ 更新占用的 UAV-HAPS 带宽 |
| $f_j[t]$ | 连续，$[0,F^{\mathrm H}]$ | 每帧 | HAPS 分配给目标 $j$ 更新的 CPU 频率 |

优化受到以下约束。

**C1：每架无人机的感知容量。** 每帧每架无人机最多生成一个新目标更新：

$$
\sum_{j\in\mathcal J_m}a_j[t]\le1,
\qquad \forall m\in\mathcal M,\ t\in\mathcal T.
$$

该约束保留文献 [2] 的分配目标集合并限制射频与回波接收的同时工作量。

**C2：感知激活与功率联动。** 感知功率只分配给激活目标：

$$
0\le p_j^{\mathrm S}[t]
\le a_j[t]P_{m(j)}^{\max},
\qquad \forall j,t.
$$

**C3：无人机发射功率。** 通信与感知共用无人机射频功率：

$$
\sum_{j\in\mathcal J_m}p_j^{\mathrm S}[t]
\le P_m^{\max},
\qquad \forall m,t.
$$

通信功率由剩余量 $p_m^{\mathrm C}[t]$ 确定，不再作为独立决策变量。

**C4：通信服务质量。** 所有地面用户满足最低 SINR：

$$
\gamma_{mk}[t]\ge\gamma_k^{\min},
\qquad \forall m,\ k\in\mathcal K_m,\ t.
$$

该约束限制感知功率对通信服务的挤占。

**C5：感知质量。** 激活目标必须满足最低感知 SNR：

$$
\Gamma_{m(j)j}[t]
\ge a_j[t]\Gamma_j^{\min},
\qquad \forall j,t.
$$

**C6：共享 UAV-HAPS 带宽。** 带宽只能分配给具有待传更新的目标，并受总带宽限制：

$$
0\le b_j[t]
\le B^{\mathrm H}
\mathbb 1\{\widetilde Q_j^{\mathrm U}[t]>0\},
\qquad \forall j,t,
$$

$$
\sum_{j\in\mathcal J}b_j[t]
\le B^{\mathrm H},
\qquad \forall t.
$$

**C7：HAPS 计算容量。** CPU 只分配给已有计算任务的目标，所有分配不超过 HAPS 容量 $F^{\mathrm H}$：

$$
0\le f_j[t]
\le F^{\mathrm H}\mathbb 1\{Q_j^{\mathrm H}[t]>0\},
\qquad \forall j,t,
$$

$$
\sum_{j\in\mathcal J}f_j[t]
\le F^{\mathrm H},
\qquad \forall t.
$$

**C8：变量域与状态递推。** $a_j[t]\in\{0,1\}$，$p_j^{\mathrm S}[t]\ge0$、$b_j[t]\ge0$、$f_j[t]\ge0$，并满足第 III-C 与 III-D 节的缓冲和 AoI 递推。

P1 是带二元目标激活、连续资源分配、非凸 SINR/SNR 条件和随机缓冲状态的无限时域混合整数序贯优化问题。离散激活决定连续动作的有效维度，感知功率同时影响感知可行性和通信 SINR，带宽与 CPU 分别作用于两个串联缓冲区。当前动作产生的更新只有在未来完成传输和计算后才降低 AoI，因此逐帧贪心最小化当前 AoI 无法反映真实收益。

## IV. 队列感知的在线资源调度

本节给出求解 P1 的 QF-HPPO。算法以 HAPS 为集中控制器，在每帧先生成离散目标激活动作，再生成连续功率、带宽和 CPU 动作。物理可行候选掩码排除无法满足感知与通信必要条件的目标，凸投影把连续策略输出映射到当前帧可行域；缓冲状态和时间戳使策略能够评价延迟完成的 AoI 收益。

### A. 马尔可夫决策过程

为使不同业务和资源档位能够由同一策略处理，定义目标参数

$$
\boldsymbol d_j
=
\left(D_j,c_j,\omega_j,\Gamma_j^{\min}\right),
$$

用户参数 $\boldsymbol d_k=(\gamma_k^{\min},\sigma_k^2)$，以及全局资源参数

$$
\boldsymbol d^{\mathrm{sys}}
=
\left(
B^{\mathrm H},F^{\mathrm H},
\{P_m^{\max},P_m^{\mathrm H}\}_{m\in\mathcal M},
\tau^{\mathrm I},\tau^{\mathrm H}
\right).
$$

这些参数在一个运行回合内固定；训练跨越不同参数档位时，将其归一化后输入网络。帧 $t$ 的状态定义为

$$
\begin{aligned}
\boldsymbol s[t]
=
\bigl(
&\{A_j[t],Q_j^{\mathrm U}[t],g_j^{\mathrm U}[t],
Q_j^{\mathrm H}[t],g_j^{\mathrm H}[t],\boldsymbol d_j\}_{j\in\mathcal J},\\
&\{\boldsymbol h_{mk}[t],\boldsymbol d_k\}_{m\in\mathcal M,\,k\in\mathcal K_m},
\{\boldsymbol g_{mj}[t]\}_{m\in\mathcal M,\,j\in\mathcal J_m},
\{h_m^{\mathrm H}[t]\}_{m\in\mathcal M},\\
&\{\boldsymbol q_m[t],\boldsymbol\xi_m^{q}[t]\}_{m\in\mathcal M},
\{\boldsymbol u_k[t],\boldsymbol\xi_k^{u}[t]\}_{k\in\mathcal K},
\{\boldsymbol v_j[t],\boldsymbol\xi_j^{v}[t]\}_{j\in\mathcal J},
\boldsymbol d^{\mathrm{sys}}
\bigr).
\end{aligned}
$$

位置和移动状态共同决定下一帧的位置分布，当前信道按一阶时变信道模型演化，因此给定动作后的下一状态只依赖 $\boldsymbol s[t]$。若实测移动或信道过程具有更长记忆，应使用固定长度历史或循环编码器扩展状态。时间戳输入网络前使用当前帧与生成帧之差归一化，空缓冲的时间戳置零。

动作由离散目标激活 $\boldsymbol a^{\mathrm D}[t]=\{a_j[t]\}$ 和连续资源动作

$$
\boldsymbol a^{\mathrm C}[t]
=
\{p_j^{\mathrm S}[t],b_j[t],f_j[t]\}_{j\in\mathcal J}
$$

组成。每帧回报取下一帧加权 AoI 的相反数：

$$
r[t]
=
-\sum_{j\in\mathcal J}\omega_jA_j[t+1]\Delta.
$$

这是一个持续运行的平均回报 MDP。最大化 $\liminf_{T\to\infty}T^{-1}\mathbb E[\sum_{t=0}^{T-1}r[t]]$ 与最小化 P1 等价，不额外加入能耗或丢弃罚权；C1–C7 由动作生成与投影保证。

### B. 物理可行候选掩码

对目标 $j\in\mathcal J_m$，先计算在保留用户最低 SINR 所需通信功率后的最大可用感知功率 $\overline p_j^{\mathrm S}[t]$。由于一个无人机每帧至多激活一个目标，固定波束下 $\gamma_{mk}[t]$ 与 $\Gamma_{mj}[t]$ 对 $p_j^{\mathrm S}[t]$ 都是一维分式函数，可通过区间求根得到满足 C4–C5 的感知功率区间

$$
\mathcal P_j[t]
=
\left[
p_j^{\min}[t],
\overline p_j^{\mathrm S}[t]
\right].
$$

若该区间非空，则候选标志 $\mu_j[t]=1$；否则 $\mu_j[t]=0$。算法按无人机顺序采样一个目标或空动作，掩码为

$$
\mathcal M_m[t]
=
\{0\}\cup
\{j\in\mathcal J_m:\mu_j[t]=1\}.
$$

在第 III-B 节的基准通信可行条件下，空动作 $0$ 对应 $a_j[t]=p_j^{\mathrm S}[t]=0$，因而满足 C1–C5。若基准通信条件失效，当前帧直接触发上层重配置，不把空动作误判为可行。该生成方式使每架无人机在 QF-HPPO 的适用状态内始终有可选动作，并避免先选择目标再用固定罚值处理物理层不可行性。

### C. 条件连续策略与可行性投影

离散目标激活确定后，条件连续策略输出定义在 $(0,1)$ 上的 Beta 分布样本。$z_j^p[t]$ 表示激活目标的归一化感知功率，$z_j^b[t]$ 表示第一阶段结束后非空 UAV 缓冲的带宽偏好，$z_j^f[t]$ 表示帧开始时非空 HAPS 缓冲的 CPU 偏好。只为当前有效维度采样，其他维度置零。感知功率通过对应可行区间映射为原始动作：

$$
\widetilde p_j^{\mathrm S}[t]
=
a_j[t]\left(
p_j^{\min}[t]
+z_j^p[t]
\bigl(\overline p_j^{\mathrm S}[t]-p_j^{\min}[t]\bigr)
\right).
$$

带宽和 CPU 原始动作分别取为 $\widetilde b_j[t]=B^{\mathrm H}z_j^b[t]$ 和 $\widetilde f_j[t]=F^{\mathrm H}z_j^f[t]$。将全部原始连续动作记为

$$
\widetilde{\boldsymbol a}^{\mathrm C}[t]
=
\{\widetilde p_j^{\mathrm S}[t],
\widetilde b_j[t],\widetilde f_j[t]\}_{j\in\mathcal J}.
$$

环境不直接执行该动作，而是求解当前帧的无量纲加权欧氏投影。令 $\alpha_p,\alpha_b,\alpha_f>0$ 为三类动作的投影权重，则

$$
\min_{\boldsymbol p,\boldsymbol b,\boldsymbol f}
\sum_j
\left[
\alpha_p
\left(
\frac{p_j-\widetilde p_j^{\mathrm S}}
{P_{m(j)}^{\max}}
\right)^2
+
\alpha_b
\left(
\frac{b_j-\widetilde b_j}
{B^{\mathrm H}}
\right)^2
+
\alpha_f
\left(
\frac{f_j-\widetilde f_j}
{F^{\mathrm H}}
\right)^2
\right]
$$

$$
\mathrm{s.t.}\quad \mathrm{C2}-\mathrm{C7}.
$$

该投影算子记为 $\Pi_{\boldsymbol s[t],\boldsymbol a^{\mathrm D}[t]}$，执行动作定义为

$$
\boldsymbol a^{\mathrm C}[t]
=
\Pi_{\boldsymbol s[t],\boldsymbol a^{\mathrm D}[t]}
\left(\widetilde{\boldsymbol a}^{\mathrm C}[t]\right).
$$

离散动作固定且每架无人机最多激活一个目标后，感知功率的可行区间已由掩码计算，带宽和 CPU 约束分别是带非负边界的单纯形，因此投影可以分解为感知功率裁剪、带宽单纯形投影和 CPU 单纯形投影。在基准通信可行条件下，零带宽和零 CPU 始终满足当前资源约束，投影可行集非空。投影只保证当前帧动作满足硬约束，长期 AoI 性能由策略训练获得。

### D. 策略训练与在线执行

离散策略、条件连续策略和价值网络共享目标级与无人机级特征编码器。令 $\boldsymbol\theta$ 和 $\boldsymbol\psi$ 分别表示策略与价值网络参数，联合策略密度分解为

$$
\pi_{\boldsymbol\theta}
\left(
\boldsymbol a^{\mathrm D}[t],
\widetilde{\boldsymbol a}^{\mathrm C}[t]
\mid\boldsymbol s[t],\boldsymbol M[t]
\right)
=
\pi_{\boldsymbol\theta}^{\mathrm D}
\left(
\boldsymbol a^{\mathrm D}[t]
\mid\boldsymbol s[t],\boldsymbol M[t]
\right)
\pi_{\boldsymbol\theta}^{\mathrm C}
\left(
\widetilde{\boldsymbol a}^{\mathrm C}[t]
\mid\boldsymbol s[t],\boldsymbol a^{\mathrm D}[t]
\right),
$$

其中 $\boldsymbol M[t]=\{\mathcal M_m[t]\}_{m\in\mathcal M}$ 表示全部无人机的候选掩码。训练缓冲区保存采样时使用的掩码、原始 Beta 样本和投影后的执行动作。令 $\boldsymbol\theta_{\mathrm{old}}$ 和 $\boldsymbol\psi_{\mathrm{old}}$ 分别表示采样轨迹时的策略与价值网络参数，PPO [18] 的概率比定义为

$$
\rho_t(\boldsymbol\theta)
=
\frac{
\pi_{\boldsymbol\theta}
\left(
\boldsymbol a^{\mathrm D}[t],
\widetilde{\boldsymbol a}^{\mathrm C}[t]
\mid\boldsymbol s[t],\boldsymbol M[t]
\right)
}{
\pi_{\boldsymbol\theta_{\mathrm{old}}}
\left(
\boldsymbol a^{\mathrm D}[t],
\widetilde{\boldsymbol a}^{\mathrm C}[t]
\mid\boldsymbol s[t],\boldsymbol M[t]
\right)
}.
$$

连续策略密度只包含当前有效的感知功率、非空 UAV 缓冲和非空 HAPS 缓冲维度。由于投影是多对一映射，概率比使用投影前的原始动作密度；投影结果只用于环境状态转移。

P1 是长期平均目标，因此采用平均回报形式的优势估计。令 $\overline r$ 为当前策略平均单帧回报的滑动估计，$V_{\boldsymbol\psi}(\boldsymbol s[t])$ 为差分价值函数，平均回报时序差分误差为

$$
\delta_t
=
r[t]-\overline r
+V_{\boldsymbol\psi_{\mathrm{old}}}(\boldsymbol s[t+1])
-V_{\boldsymbol\psi_{\mathrm{old}}}(\boldsymbol s[t]).
$$

对长度为 $L$ 的连续训练片段，令 $L_t$ 表示从帧 $t$ 到当前片段末尾的剩余帧数，$\lambda_{\mathrm{GAE}}\in[0,1]$ 表示优势衰减参数。使用片段末状态的价值进行自举，得到

$$
\widehat A[t]
=
\sum_{\ell=0}^{L_t-1}
\lambda_{\mathrm{GAE}}^{\ell}\delta_{t+\ell}.
$$

滑动平均 $\overline r$ 在每批轨迹结束后由批次平均回报更新。令 $\epsilon>0$ 为 PPO 截断系数，策略目标为

$$
L^{\mathrm{clip}}(\boldsymbol\theta)
=
\mathbb E_t\!\left[
\min\left(
\rho_t(\boldsymbol\theta)\widehat A[t],
\operatorname{clip}\bigl(\rho_t(\boldsymbol\theta),1-\epsilon,1+\epsilon\bigr)
\widehat A[t]
\right)
\right].
$$

令 $\widehat R[t]=\widehat A[t]+V_{\boldsymbol\psi_{\mathrm{old}}}(\boldsymbol s[t])$，$\mathcal H_t$ 为联合策略熵，$c_v,c_h\ge0$ 分别为价值损失和熵正则权重。训练损失为

$$
L(\boldsymbol\theta,\boldsymbol\psi)
=
-L^{\mathrm{clip}}(\boldsymbol\theta)
+c_v\mathbb E_t\!\left[
\bigl(
V_{\boldsymbol\psi}(\boldsymbol s[t])-\widehat R[t]
\bigr)^2
\right]
-c_h\mathbb E_t[\mathcal H_t].
$$

训练环境从目标轨迹、空地信道和 D 波段信道模型生成连续帧序列；在线阶段只执行一次策略前向传播、候选区间计算和三个小规模投影。

在线流程如下：

1. HAPS 采集目标 AoI、UAV/HAPS 缓冲状态、时间戳、位置和信道估计。
2. 对每个目标计算 $\mathcal P_j[t]$，构造各无人机的候选掩码 $\mathcal M_m[t]$。
3. 离散策略为每架无人机选择一个目标或空动作。
4. 条件连续策略生成感知功率、回传带宽和 HAPS CPU 偏好。
5. 对连续动作执行区间裁剪与单纯形投影，得到满足 C2–C7 的可执行动作。
6. 系统执行通信、感知、回传和计算，按第 III-C 与 III-D 节更新双缓冲和 AoI。
7. 训练阶段保存转移并周期性更新 PPO；部署阶段直接进入下一帧。

若策略网络一次前向传播的复杂度记为 $C_{\mathrm{NN}}$，目标物理区间求解采用固定 $L_p$ 次二分，候选计算复杂度为 $O(JL_p)$；带宽和 CPU 单纯形投影可通过排序在 $O(J\log J)$ 内完成。因此，单帧在线复杂度为

$$
O\bigl(C_{\mathrm{NN}}+JL_p+J\log J\bigr).
$$

QF-HPPO 不保证 P1 的全局最优解。候选掩码和投影能够保证固定波束与正交无人机子带假设下的当前帧 C1–C7；PPO 只提供经验策略改进，不提供无限时域 AoI 最优性或队列稳定性的解析保证。

## V. 实验设计

### A. 实验设置

实验采用文献 [2] 的 HAPS-UAV 两层架构、工作频段和基础物理层参数，并参考 HAP-UAV 感知计算研究 [8]–[10] 设置更新大小、计算密度和 HAPS CPU 的扫描范围。系统设置一架 HAPS、$M\in\{2,4,8\}$ 架无人机、每架无人机 $2$–$6$ 个通信用户和 $2$–$8$ 个目标。sub-6 GHz 接入采用视距主导空地信道；D 波段在文献 [2] 的路径损耗模型上加入合成 Rician 时变衰落，用户和目标分别采用合成 Gauss–Markov 与恒速转弯移动过程。这些移动与小尺度衰落过程用于动态和压力测试，不归因于文献 [2]。速度、航向和转弯角速度按第 IV-A 节定义作为策略状态。目标更新大小 $D_j$、计算密度 $c_j$、HAPS CPU $F^{\mathrm H}$ 和回传带宽 $B^{\mathrm H}$ 按低、中、高三档组合，形成通信受限、计算受限和均衡场景；训练时在每个回合开始采样参数组合，并把第 IV-A 节定义的业务门限和资源参数输入同一策略。

每种方法使用 10 个独立训练种子，并在未参与训练的 30 个移动与信道种子上测试。每个测试种子运行至少 $10^4$ 帧；报告均值、95% 置信区间以及跨目标的 95% AoI 分位数。所有学习方法使用相同网络宽度、环境交互预算和调参次数。

### B. 对比方法

1. **Kanani-NSGA-II**：按文献 [2] 优化回波功率和最小用户 SINR，再用等分带宽与等分 CPU 处理更新。
2. **Freshest-First**：每架无人机选择当前 AoI 最大的物理可行目标，回传带宽和 CPU 均按 AoI 权重分配。
3. **Queue-MaxWeight**：以
   $\omega_jA_j[t]\big/\bigl(Q_j^{\mathrm U}[t]/D_j+Q_j^{\mathrm H}[t]/(D_jc_j)+1\bigr)$
   为优先级进行目标、带宽和 CPU 调度，其中两类缓冲分别除以单个更新的数据量和计算量，使积压项无量纲。
4. **One-Step Greedy**：枚举本帧目标激活，在当前信道下求解连续资源分配，最小化可计算的一步 AoI 上界。
5. **Hybrid-PPO-Penalty**：与 QF-HPPO 使用相同状态和动作，但通过固定奖励罚项处理全部约束，不使用候选掩码和投影。
6. **QF-HPPO**：本文完整方法。
7. **Clairvoyant Offline**：在小规模短窗口上预知未来信道与移动轨迹，采用混合整数搜索和连续优化得到性能上界。

### C. 评价指标与消融实验

主要指标包括加权平均处理后 AoI、目标级 95% AoI、更新完成率、端到端更新时间、UAV 与 HAPS 缓冲等待时间、UAV/HAPS 更新替换率、用户 SINR 违约率、感知 SNR 违约率、资源超配率和单帧推理时间。

消融实验与贡献一一对应：

1. **接收即刷新**：在 HAPS 收到完整回波时重置 AoI，用于检验忽略计算等待是否改变策略和结论。
2. **无 UAV 缓冲**：假设每次回传均在一帧内完成，用于检验回传积压的作用。
3. **无 HAPS 缓冲**：假设 HAPS 计算能力无限，用于检验计算瓶颈。
4. **保留所有更新**：用 FCFS 代替最新更新保留，检验陈旧更新替换机制。
5. **无候选掩码**、**无可行性投影**和**无时间戳特征**：分别检验三个算法模块。

### D. 压力测试与可证伪条件

压力测试逐项改变目标移动速度、D 波段遮挡概率、用户 SINR 门限、更新大小、HAPS CPU、回传带宽、目标数量以及训练—测试移动分布偏移。额外使用有偏信道估计和突发目标出现检验鲁棒性。半实物验证可用多台嵌入式板卡生成回波处理任务，以容器化 HAPS 服务器执行融合工作负载，并用网络仿真器限制 D 波段吞吐；实测更新时间、队列等待和 CPU 周期用于校准 $D_j$ 与 $c_j$。

本文的核心命题是：当回传或 HAPS 计算成为瓶颈时，继续提高感知频率可能增加更新替换和处理后 AoI，队列感知策略应优于只优化回波功率或当前 AoI 的方法。以下结果将否定或显著削弱该命题：

1. 在回传或计算受限区间，感知频率增加仍单调降低处理后 AoI，且不增加更新替换率；
2. 接收即刷新与处理后刷新得到相同策略和近似相同 AoI；
3. Queue-MaxWeight 或 One-Step Greedy 在所有动态场景中达到与 QF-HPPO 相当的性能和可行率；
4. 当 $B^{\mathrm H}$ 与 $F^{\mathrm H}$ 充分大时，QF-HPPO 仍保持显著优势。该情形说明收益可能来自策略容量或调参，而非双缓冲机制。

## 附录 A：新颖性边界与模型风险

### A.1 新颖性边界

HAPS-UAV 架构、通信—感知多目标优化、HAP 感知计算、AoI 和多目标 DRL 均已有研究 [2]–[10], [14]–[17]。本文保留的研究问题是“多 UAV ISAC 回波经过 UAV 回传缓冲和 HAPS 计算缓冲后，在处理完成时刷新目标 AoI”的端到端状态过程，以及由此产生的在线资源调度。该边界不依赖“首次引入 HAPS”“首次使用 AoI”或“首次使用 PPO”等脆弱表述。

### A.2 主要假设与风险

固定目标归属、给定 UAV 位置和给定波束方向使研究集中于运行层缓冲与资源耦合，也忽略了跨无人机目标重分配和波束联合优化。正交无人机接入子带消除了跨无人机地面干扰；若频谱复用成为主要瓶颈，需要扩展 C4–C5。最新更新替换适合目标跟踪，不适合必须保存全部历史样本的遥感归档。完整更新才能进入 HAPS 计算缓冲的假设排除了分块流水处理，后续可用分段队列放宽。

## 参考文献

[1] K. Meng *et al.*, “UAV-enabled integrated sensing and communication: Opportunities and challenges,” *IEEE Wireless Commun.*, vol. 31, no. 2, pp. 97–104, Apr. 2024.

[2] P. Kanani, M. J. Omidi, M. Modarres-Hashemi, and H. Yanikomeroglu, “Optimizing network performance and resource allocation in HAPS-UAV integrated sensing and communication systems for 6G,” *IEEE Trans. Wireless Commun.*, vol. 25, pp. 4098–4112, 2026.

[3] A. M. Benaya, M. S. Hassan, M. H. Ismail, and T. Landolsi, “Aerial ISAC: A HAPS-assisted integrated sensing, communications and computing framework for enhanced coverage and security,” *IEEE Trans. Green Commun. Netw.*, vol. 9, no. 4, pp. 2101–2114, 2025.

[4] X. Guo, J. Shi, J. Wu, R. Zhang, and X. Cheng, “Integrated sensing and communications in multi-UAV networks: A dual-objective optimization perspective,” *IEEE Trans. Wireless Commun.*, vol. 25, pp. 10066–10081, 2026.

[5] Q. Zhu, R. Liu, Q. Liu, and C. Chen, “Resource allocation for UAV swarm-assisted green ISAC networks via multi-agent RL,” *IEEE Trans. Green Commun. Netw.*, vol. 9, no. 3, pp. 1354–1367, 2025.

[6] Y. Bai, Y. Zhang, B. Xie, Z. Chang, Y. Zhang, R. Jantti, and Z. Han, “Age of information minimization in UAV-enabled integrated sensing and communication systems,” *IEEE Trans. Mobile Comput.*, early access, 2026, doi: 10.1109/TMC.2026.3709576.

[7] Z. Liu, X. Liu, W. Yang, and X. Zhang, “Joint sensing and age of information optimization for energy constrained UAV-assisted integrated sensing, calculation, and communication,” *IEEE Trans. Wireless Commun.*, vol. 24, no. 5, pp. 4440–4453, May 2025.

[8] H. Zhao, M. Luan, M. Liyanage, and Z. Chang, “Joint optimization of sensing, communication, and computing for collaborative multi-UAV edge computing system,” *IEEE Trans. Wireless Commun.*, vol. 25, pp. 1272–1286, 2026.

[9] Y. Zhou and X. Liu, “Trade-off between radar sensing and energy consumption in integrated sensing, computing, and communication UAV network,” *IEEE Trans. Green Commun. Netw.*, vol. 10, pp. 511–521, 2026.

[10] F. Song, Q. Yang, M. Deng, H. Xing, Y. Liu, X. Yu, K. Li, and L. Xu, “AoI and energy tradeoff for aerial-ground collaborative MEC: A multi-objective learning approach,” *IEEE Trans. Mobile Comput.*, vol. 23, no. 12, pp. 11278–11294, Dec. 2024.

[11] Z. Jia, Q. Wu, C. Dong, C. Yuen, and Z. Han, “Hierarchical aerial computing for Internet of Things via cooperation of HAPs and UAVs,” *IEEE Internet Things J.*, vol. 10, no. 7, pp. 5676–5688, Apr. 2023.

[12] A. Nabi and S. Moh, “Joint offloading decision, user association, and resource allocation in hierarchical aerial computing: Collaboration of UAVs and HAP,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 8, pp. 7267–7282, Aug. 2025.

[13] Z. Jia, C. Cui, C. Dong, Q. Wu, Z. Ling, D. Niyato, and Z. Han, “Distributionally robust optimization for aerial multi-access edge computing via cooperation of UAVs and HAPs,” *IEEE Trans. Mobile Comput.*, vol. 24, no. 10, pp. 10853–10867, Oct. 2025.

[14] Z. Wang, X.-P. Zhang, W. Ding, Y. Dong, and X. Chen, “A novel integrated sensing and communication scheme in UAVs-enabled vehicular networks with MARL-driven adaptive control,” *IEEE Trans. Mobile Comput.*, vol. 25, no. 1, pp. 132–147, Jan. 2026.

[15] Y. Wu, H. Yu, Y. Zhou, N. Shi, Q. Cai, and J. Shi, “Sensing-error-aware UAV scheduling based on generative diffusion-driven MADRL for ISAC-enabled multi-UAV systems,” *IEEE Trans. Wireless Commun.*, vol. 25, pp. 9782–9798, 2026.

[16] Y. Qin, Z. Zhang, X. Li, W. Huangfu, and H. Zhang, “Deep reinforcement learning based resource allocation and trajectory planning in integrated sensing and communications UAV network,” *IEEE Trans. Wireless Commun.*, vol. 22, no. 11, pp. 8158–8169, Nov. 2023.

[17] X. Ye, H. Lin, X. Song, Y. Wu, and L. Fu, “Multi-objective ISAC for low-altitude economy based on multi-task deep reinforcement learning with mixture of experts,” *IEEE Trans. Mobile Comput.*, early access, 2026, doi: 10.1109/TMC.2026.3693366.

[18] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” arXiv:1707.06347, 2017.

[19] Z. Lyu, G. Zhu, and J. Xu, “Joint maneuver and beamforming design for UAV-enabled integrated sensing and communication,” *IEEE Trans. Wireless Commun.*, vol. 22, no. 4, pp. 2424–2440, Apr. 2023.
