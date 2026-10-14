# 电池轮换 UAV-MEC 有状态服务交接：文献基础与场景推导

## 1. 相关研究基础与场景动机

### 1.1 持续运行所需的 UAV 轮换

UAV-MEC 若要在固定区域持续提供计算服务，就不能依赖一架 UAV 一直留在空中。现有研究首先解决单架 UAV 何时应离开服务位置：Ye 等 [13] 在安排任务执行时间时同时决定飞行速度和换电时机，Mei 等 [9] 则在 UAV 执行下一步动作前检查其剩余电量是否足以完成任务并安全返航。这些模型把补能视为飞行与任务计划的一部分，但没有安排另一架 UAV 接替正在运行的服务。

多 UAV 轮换研究进一步回答“由谁接替”和“如何长期周转”。Gupta 等 [10] 联合规划低电量 UAV 的返航轨迹和满电 UAV 的接替轨迹；Arribas 等 [26] 面向多个固定服务位置安排周期性补能，并确定维持长期覆盖所需的 UAV 数量；Liu 等 [28] 通过周期轮换路径保持灾后通信网络持续连通。这类工作已经覆盖替补调度、返航、补能和长期机队周转，但其中的“连续服务”是指服务位置始终有 UAV 覆盖，或者通信链路始终连通。它们没有描述一项正在 UAV 上运行的应用应如何随轮换转移到替补 UAV。

### 1.2 运行中的应用如何迁移到新节点

如果 UAV 只提供无线覆盖，替补到位后即可接替；如果 UAV 还运行视频分析或会话处理等边缘应用，替补还必须继承应用已经产生的数据。例如，跟踪目标的历史、尚未完成请求的处理进度、容器内存和网络连接都会影响应用能否从原处继续运行。若先停止原应用再传输这些内容，整个传输和恢复过程都会形成服务中断；运行中迁移则在原应用继续处理请求时先复制大部分内容，最后只短暂停止原应用并传输剩余部分。

现有有状态迁移研究已经实现了这种运行中交接。Scheuer 等 [5] 在源容器继续处理请求时复制新输入，并在目标端按原顺序回放；Rong 等 [12] 针对视频分析应用区分必须保留和可以重新生成的状态，以减少真正需要传输的数据。Ma 等 [16] 利用容器中可复用的只读内容减少传输量，Calagna 等 [14], [15] 把运行期间的内存更新和网络连接纳入迁移过程，Zhang 等 [17] 则让目标容器先载入常用内存内容，再按需恢复其余部分。这些方法通常假设源节点和目标节点已经连通，而且源节点可以留在原处直到迁移完成。低电量 UAV 不满足这一前提：替补最初仍在飞行，源 UAV 还必须在耗尽返航电量之前结束交接并离开。

### 1.3 UAV-MEC 中不同含义的“迁移”

UAV-MEC 文献中的“迁移”并不总是指转移一个正在运行的应用。García-Gil 等 [2] 根据负载和剩余电量改变微服务的部署位置，但没有描述原实例运行期间产生的状态如何交接；Zhao 等 [22] 在 UAV 之间传输尚未处理的计算任务，Wang 等 [23] 则转移单个任务剩余的输入和已经得到的部分结果。它们分别处理服务部署、待执行任务或单个任务执行到一半时的数据，并不要求替补 UAV 接管一个长期运行的应用并保持其最新状态。

与本文最接近的 UAV-MEC 优化工作已经开始考虑有状态应用。Qiu 等 [8] 联合决定 UAV 轨迹、任务卸载和有状态服务迁移，Feng 等 [11] 则根据车辆移动预测调整服务所在的 UAV 及其轨迹。这些研究说明服务迁移可以与 UAV 移动和资源分配共同优化，但它们没有低电量 UAV 退出、待命 UAV 派出和返站补能的过程。因此，文献中的目标 UAV 是已有空中节点，而不是尚未到达的替补 UAV；迁移完成后，源 UAV 也不需要立即保留电量返航。

### 1.4 电池轮换中的服务交接

目前最直接的两项工作已经把服务交接放入低电量 UAV 替换过程。Ye 等 [27] 在多个补能站之间决定满电 UAV 从哪个站派出、低电量 UAV 返回哪个站，并根据满电 UAV 和充电位是否可用安排派出时机。该文提到转移计算任务的当前状态，却没有说明这些状态由哪些数据组成、如何传输，以及替补接管后如何保持原任务的执行进度，也没有给出完整的数学优化模型。Frejo-Martín 等 [1] 进一步给出了有状态微服务的交接流程：替补起飞后，源 UAV 停止服务；两机建立连接后传输检查点和可写层；替补恢复应用，源 UAV 再返站补能。该文明确了容器状态的交接对象，但仍属于架构与流程设计，没有优化模型、求解算法或实验评估。

上述研究已经分别解决了长期 UAV 轮换、固定节点间的运行中迁移，以及 UAV-MEC 中的任务或服务迁移。因此，本文不能把长期轮换、替补选择或有状态迁移单独作为新问题。现有证据尚未共同描述这些过程在一次轮换中的相互影响：替补的选择和派出时机会改变其到达时间与两机之间的传输条件；源 UAV 在等待替补时继续处理请求，又会产生新的应用状态并消耗电量；最终切换还必须赶在源 UAV 剩余电量不足以返航之前完成。这使替补调度、状态传输和返航安全不能再分开决定。

基于这一边界，本文考虑多个固定服务区域、一个换电站和有限数量的待命 UAV。每当工作 UAV 接近安全返航电量时，控制器选择替补并决定何时派出；替补飞行期间，源 UAV 继续提供服务，两机进入通信范围后开始传输应用状态；状态交接完成后，替补接管服务，源 UAV 返站换电并在完成出动准备后重新进入待命池。研究目标是在长期轮换过程中减少服务中断和轮换能耗，同时保证每次交接完成后源 UAV 仍能安全返航。

本文保留 Arribas 等 [26] 的单站、固定服务位置和长期轮换骨架，并参考 Liu 等 [28] 表示连续时间 UAV 位置和返航能量。在此基础上，本文增加有状态应用交接。应用文件预置沿用 Frejo-Martín 等 [1] 的中央镜像同步流程，源端继续服务期间的增量同步机制参考 Scheuer 等 [5] 和 Rong 等 [12]。

## 2. 系统模型与问题定义

本文考虑一个由中央控制器管理的多区域 UAV-MEC 系统。系统在固定评估时段 $[0,H]$ 内运行，其中 $H$ 的单位为秒，$t\in[0,H]$ 表示全局连续物理时间。服务区域集合和 UAV 机队分别记为 $\mathcal M$ 和 $\mathcal U$。每个区域 $m\in\mathcal M$ 有一个固定的服务悬停点 $\mathbf q_m$，系统设置一个位于 $\mathbf q_0$ 的换电站。换电站始终能够为返回的 UAV 更换满电电池；换电完成后，UAV 经过固定的返站准备时长即可再次派出。每个服务区域包含多个用户终端。用户将请求发送给负责该区域的 UAV，UAV 完成计算后返回结果。应用在处理这些请求时持续产生随时间更新的运行状态；应用运行所需的静态文件，例如应用镜像和依赖库，已经预置在可被派往相应区域的 UAV 上。

当某个服务区域当前提供计算服务的 UAV 达到返航电量阈值时，中央控制器从换电站中可以立即出动的 UAV 组成的待命池中选择一架替补。将这类交接按发生顺序编号为 $e=1,2,\ldots,N$，其中 $N$ 是评估时段内完成的交接次数，第 $e$ 次交接的开始时刻记为 $T_e^{\mathrm{start}}$。在这次交接中，正在提供服务的 UAV 作为源 UAV，选中的 UAV 作为替补 UAV；替补飞往目标区域时，源 UAV 继续处理请求，两机建立机间通信链路后，源 UAV 将运行状态发送给替补，替补恢复应用并接管服务，源 UAV 随后返站换电，完成返站准备后重新回到待命池。交接开始时，机队中的 UAV 按所处环节分为三种状态：正在服务区域提供计算服务的 UAV 处于工作状态，已经位于换电站并可以立即出动的 UAV 处于待命状态，正在返航或尚未完成返站准备的 UAV 暂时不可用。相应的 UAV 集合分别记为 $\mathcal A_e$、$\mathcal R_e$ 和 $\mathcal C_e$；$E_u(t)$ 表示 UAV $u\in\mathcal U$ 在全局时刻 $t$ 的剩余电量。三类集合两两不交并覆盖整个机队，即

$$
\mathcal A_e\cap\mathcal R_e
=
\mathcal A_e\cap\mathcal C_e
=
\mathcal R_e\cap\mathcal C_e
=
\varnothing,
\qquad
\mathcal A_e\cup\mathcal R_e\cup\mathcal C_e
=
\mathcal U.
$$

对每个工作 UAV $u\in\mathcal A_e$，用 $\mu_{u,e}\in\mathcal M$ 表示其在第 $e$ 次交接开始时负责的区域。每个区域恰由一架工作 UAV 服务，因此需要满足

$$
\sum_{u\in\mathcal A_e}
\mathbb I(\mu_{u,e}=m)
=1,
\qquad
\forall m\in\mathcal M.
\tag{C1}
$$

对每架非工作 UAV $u\in\mathcal U\setminus\mathcal A_e$，令 $\rho_{u,e}$ 表示它能够再次出动的最早时刻；$\rho_{u,e}\le T_e^{\mathrm{start}}$ 时，$u\in\mathcal R_e$，否则 $u\in\mathcal C_e$。工作 UAV 的 $\rho_{u,e}$ 记为 $+\infty$。

评估开始时，初始部署已经完成：每个服务区域已有一架工作 UAV，其余 UAV 位于换电站并处于待命状态。因此，$\mathcal R_1=\mathcal U\setminus\mathcal A_1$、$\mathcal C_1=\varnothing$；初始工作 UAV 与服务区域的对应关系 $\mu_{u,1}$ 由部署方案确定。对 $u\in\mathcal R_1$，有 $\rho_{u,1}=0$；对 $u\in\mathcal A_1$，按前述约定取 $\rho_{u,1}=+\infty$。

### 2.1 UAV 飞行模型

令 $E_{u,e}^{\mathrm{trig}}$ 表示事件 $e$ 开始时工作 UAV $u$ 在其服务区域对应的轮换电量阈值。源 UAV $s_e$ 及其服务区域 $m_e$ 是下列集合中的唯一元素：

$$
(s_e,m_e)
\in
\left\{
(u,m)\in\mathcal A_e\times\mathcal M:
\mu_{u,e}=m,
\ E_u(T_e^{\mathrm{start}})
\le
E_{u,e}^{\mathrm{trig}}
\right\}.
$$

$m_e$ 和 $s_e$ 均由事件开始时的系统状态确定，不是控制器的决策变量。

本次轮换对应的服务悬停点和交接点分别记为 $\mathbf q_e^{\mathrm{srv}}$ 和 $\mathbf q_e^{\mathrm{ho}}$。它们是根据触发区域的预设空间配置取得的第 $e$ 次事件参数，不作为控制变量。

控制器在事件开始时选择替补、派出等待时长和重叠服务时长。对每架 UAV $u\in\mathcal U$，用二元变量 $x_{u,e}$ 表示它是否承担第 $e$ 次替补任务；用 $\tau_e^{\mathrm{dep}}$ 表示从事件开始到替补起飞的等待时长，用 $\theta_e$ 表示替补起飞后源 UAV 继续服务的时长。已知指示量 $\chi_{u,e}\in\{0,1\}$ 表示 UAV $u$ 是否能够运行本次轮换区域的应用；$\chi_{u,e}=0$ 时不能作为替补。替补必须在实际起飞时刻已经完成返航和返站准备，因此

$$
\sum_{u\in\mathcal U}x_{u,e}=1,\qquad
x_{u,e}
\le
\mathbb I\left(
\rho_{u,e}\le T_e^{\mathrm{start}}+\tau_e^{\mathrm{dep}}
\right)
\chi_{u,e},
\qquad
x_{u,e}\in\{0,1\},
\tag{C2}
$$

C2 要求选中的 UAV 在 $T_e^{\mathrm{start}}+\tau_e^{\mathrm{dep}}$ 时已经可以派出，并且能够接管该应用；令 $u_e$ 表示唯一满足 $x_{u,e}=1$ 的 UAV $u$。当待命池中暂时没有合适的 UAV 时，控制器可以等待 $\mathcal C_e$ 中某架 UAV 恢复可用，但等待会增加源端状态和能量消耗。如果在允许等待范围内仍不存在满足 C2 的 UAV，事件不可行。

令 $\bar\tau_e^{\mathrm{dep}}$ 和 $\bar\theta_e$ 分别表示派出等待和重叠服务允许的最大时长。为限制过长的等待和交接过程，两个时间决策必须位于允许的运行区间：

$$
0\le\tau_e^{\mathrm{dep}}\le\bar\tau_e^{\mathrm{dep}},
\qquad
0\le\theta_e\le\bar\theta_e,
\tag{C3}
$$

C3 给出替补派出等待和重叠服务时长的决策域。

换电站和服务悬停点均为已知三维坐标。假设飞行空域不存在需要绕行的固定障碍物，UAV 以给定速度沿起点和终点之间的直线飞行。令 $D^{\mathrm A}$ 表示 A2A 链路的通信半径，$d^{\mathrm{safe}}$ 表示两架 UAV 在重叠服务期间必须保持的最小安全距离。对区域 $m$，在换电站到服务悬停点的进场直线上预先设置交接点 $\mathbf q_m^{\mathrm{ho}}$。若该点与服务悬停点的距离为 $r_m^{\mathrm{ho}}\in[d^{\mathrm{safe}},\min\{D^{\mathrm A},\lVert\mathbf q_0-\mathbf q_m\rVert\}]$，则

$$
\mathbf q_m^{\mathrm{ho}}
=
\mathbf q_m+
r_m^{\mathrm{ho}}
\frac{\mathbf q_0-\mathbf q_m}
{\lVert\mathbf q_0-\mathbf q_m\rVert}.
$$

交接点由安全间隔和 A2A 覆盖范围预先确定，不作为 P0 的决策变量。令 $v_u^{\mathrm{out}}$ 表示 UAV $u$ 的出动速度，$v_e^{\mathrm{ret}}$ 表示本次源 UAV 的返航速度。候选 UAV $u$ 飞往本次交接点所需的时间为

$$
\tau_{u,e}^{\mathrm{out}}
=
\frac{\lVert\mathbf q_e^{\mathrm{ho}}-\mathbf q_0\rVert}
{v_u^{\mathrm{out}}}.
$$

源 UAV 从本次服务悬停点返回换电站所需的时间为

$$
\tau_e^{\mathrm{ret}}
=
\frac{\lVert\mathbf q_e^{\mathrm{srv}}-\mathbf q_0\rVert}
{v_e^{\mathrm{ret}}}.
$$

第 $e$ 次事件选中的替补 UAV $u_e$ 在

$$
T_e^{\mathrm{dep}}
:=
T_e^{\mathrm{start}}+\tau_e^{\mathrm{dep}}
$$

时刻起飞，并在

$$
\tau_e^{\mathrm{out}}
=
\sum_{u\in\mathcal U}x_{u,e}\tau_{u,e}^{\mathrm{out}}
$$

秒后到达交接点，即

$$
T_e^{\mathrm{arr}}
:=
T_e^{\mathrm{dep}}+\tau_e^{\mathrm{out}}
$$

飞行期间的位置为

$$
\mathbf q_e^{\mathrm{rep}}(t)
:=
\mathbf q_0+
\frac{t-T_e^{\mathrm{dep}}}{\tau_e^{\mathrm{out}}}
\left(
\mathbf q_e^{\mathrm{ho}}-\mathbf q_0
\right),
\qquad
t\in[T_e^{\mathrm{dep}},T_e^{\mathrm{arr}}].
$$

替补到达后在交接点悬停，源 UAV 在服务切换前保持在 $\mathbf q_e^{\mathrm{srv}}$。两机在时刻 $t$ 的距离为

$$
d_e(t)
:=
\left\lVert
\mathbf q_e^{\mathrm{srv}}-\mathbf q_e^{\mathrm{rep}}(t)
\right\rVert .
$$

### 2.2 A2A 通信模型

用户终端与工作 UAV 之间的业务链路采用固定用户关联的正交频分多址（OFDMA），只负责请求和结果传输。应用状态通过源 UAV 与替补 UAV 之间的 A2A 链路传输。A2A 链路使用固定专用带宽 $B^{\mathrm A}$。令 $P_e^{\mathrm{src,tx}}$ 表示本次源 UAV 的 A2A 发射功率，$\beta_0$ 表示参考距离处的信道增益，$\alpha_{\mathrm A}$ 表示 A2A 路径损耗指数，$N_0$ 表示噪声功率谱密度。第 $e$ 次事件中的瞬时传输速率为

$$
R_e(t)
=
B^{\mathrm A}
\log_2
\left(
1+
\frac{P_e^{\mathrm{src,tx}}\beta_0d_e(t)^{-\alpha_{\mathrm A}}}
{N_0B^{\mathrm A}}
\right).
$$

若 A2A 通信半径为 $D^{\mathrm A}$，则两机首次进入通信范围的时刻由位置关系确定为

$$
T_e^{\mathrm{link}}
=
\inf
\left\{
t\ge T_e^{\mathrm{dep}}:
d_e(t)\le D^{\mathrm A}
\right\}.
$$

若上式不存在有限值，则该替补候选不可行。源 UAV 只有在替补到达交接点且两机已经建立 A2A 链路后才能停止处理新请求，因此还需要满足

$$
T_e^{\mathrm{dep}}
\le
T_e^{\mathrm{link}}
\le
T_e^{\mathrm{arr}}
\le
T_e^{\mathrm{cut}},
\qquad
T_e^{\mathrm{cut}}
=
T_e^{\mathrm{dep}}+\theta_e .
\tag{C4}
$$

C4 约束替补起飞、建立 A2A 链路、到达固定交接点和源端停止接收新请求的先后关系。

### 2.3 状态同步模型

区域 $m$ 的应用在处理用户请求时持续产生需要保留的运行状态。令 $G_m(t)$ 表示该区域自上次成功交接后累计产生的增量状态总量，$\gamma_m$ 表示其产生速率。评估开始时各区域的基准状态已经同步，因此 $G_m(0)=0$；应用持续提供服务时有

$$
\frac{\mathrm d G_m(t)}{\mathrm dt}=\gamma_m.
$$

这里 $\gamma_m$ 的单位为数据量每秒，$G_m(t)$ 的单位为数据量。已经发送的部分在最终切换完成前仍属于当前完整状态，尚未发送的数据量由下文的同步队列单独记录。

为使替补从最近一次交接后的状态继续运行，换电站为每个服务区域保存该次交接完成时的完整应用状态副本；待命 UAV 出动前取得对应副本。因此，预同步阶段只需传输副本之后新增或改变的状态，不再重复传输已经一致的历史状态。交接完成后，替补形成的完整状态更新站内副本；副本更新和预置均在固定的返站准备时间内完成。

第 $e$ 次事件开始时，触发区域已有的增量状态量和状态产生速率分别记为 $G_e^{\mathrm{start}}$ 和 $\gamma_e$。二者均由事件开始时的区域状态确定。

源 UAV 在 $[T_e^{\mathrm{start}},T_e^{\mathrm{cut}})$ 内继续服务，因此切换前需要由替补继承的总状态量为

$$
G_e^{\mathrm{cut}}
=
G_e^{\mathrm{start}}
+
\gamma_e
\left(
T_e^{\mathrm{cut}}-T_e^{\mathrm{start}}
\right)
=
G_e^{\mathrm{start}}
+
\gamma_e
\left(
\tau_e^{\mathrm{dep}}+\theta_e
\right).
$$

预同步不能使用尚未产生的状态，因此采用连续时间流体队列描述同步过程。令 $B_e(t)$ 表示第 $e$ 次事件在时刻 $t$ 尚未传到替补 UAV 的状态量。两机刚进入 A2A 通信范围时，

$$
B_e\left(T_e^{\mathrm{link}}\right)
=
G_e^{\mathrm{start}}
+
\gamma_e
\left(
T_e^{\mathrm{link}}-T_e^{\mathrm{start}}
\right).
$$

在预同步区间 $t\in[T_e^{\mathrm{link}},T_e^{\mathrm{cut}})$ 内，状态以速率 $\gamma_e$ 进入队列，A2A 链路以不超过 $R_e(t)$ 的速率发送。记 $[z]^+=\max\{z,0\}$，队列演化为

$$
\frac{\mathrm d B_e(t)}{\mathrm dt}
=
\begin{cases}
\gamma_e-R_e(t),
& B_e(t)>0,\\[2mm]
\left[\gamma_e-R_e(t)\right]^+,
& B_e(t)=0,
\end{cases}
$$

第二个分支保证队列为空时不会提前使用未来链路容量。源 UAV 停止接收新请求时的剩余状态量和已预同步状态量分别为

$$
G_e^{\mathrm{rem}}
=
B_e\left(T_e^{\mathrm{cut}}\right),
\qquad
S_e
=
G_e^{\mathrm{cut}}-G_e^{\mathrm{rem}} .
$$

$B_e(t)$、$S_e$ 和 $G_e^{\mathrm{rem}}$ 均由状态到达、A2A 速率和两个时间决策推导，不是独立控制变量。令 $R_e^{\mathrm{fin}}>0$ 为最终切换阶段的有效状态传输速率，$T^{\mathrm{freeze}}$、$T^{\mathrm{restore}}$ 和 $T^{\mathrm{redir}}$ 分别为源端冻结应用状态、替补恢复应用和连接重定向的固定时长，则最终切换造成的服务中断时间为

$$
D_e
=
T^{\mathrm{freeze}}
+
\frac{G_e^{\mathrm{rem}}}{R_e^{\mathrm{fin}}}
+
T^{\mathrm{restore}}
+
T^{\mathrm{redir}} .
$$

令 $D^{\max}$ 表示应用允许的最大单次中断时间。为了使每次交接的中断不超过该上限，需要满足

$$
T_e^{\mathrm{end}}
=
T_e^{\mathrm{cut}}+D_e,
\qquad
D_e\le D^{\max}.
\tag{C5}
$$

C5 限制最终切换阶段的服务中断。由于该阶段传输了 $G_e^{\mathrm{rem}}$，并且源端在 $T_e^{\mathrm{cut}}$ 后不再写入新的运行状态，替补在 $T_e^{\mathrm{end}}$ 时载入源端最后确认的完整状态。该状态成为相应区域下一次轮换的基准状态，并在交接后更新到换电站的状态副本；该区域的增量状态量随之重新从零开始累计。

### 2.4 能量消耗模型

基于前文定义的剩余电量 $E_u(t)$，令 $E_u^{\max}$ 表示 UAV $u$ 的满电能量。电量轨迹从评估开始时的初始值 $E_u(0)$ 出发，具体初始值由仿真场景配置，不作为控制器的决策。UAV $u$ 提供区域服务、接收 A2A 状态和直线飞行时的等效功率分别记为 $P_u^{\mathrm{srv}}$、$P_u^{\mathrm{rx}}$ 和 $P_u^{\mathrm{fly}}$；状态冻结、应用恢复和连接重定向中除状态传输之外的固定能耗记为 $E_u^{\mathrm{fin}}$。返航能耗、安全余量和最低服务能量分别记为 $E_{u,m}^{\mathrm{ret}}$、$E_u^{\mathrm{res}}$ 和 $E_u^{\mathrm{min,service}}$。

针对第 $e$ 次事件，$E_e^{\mathrm{src,start}}$ 表示源 UAV 在事件开始时的电量；$P_e^{\mathrm{src,srv}}$、$P_e^{\mathrm{src,tx}}$、$P_e^{\mathrm{rep,fly}}$ 和 $P_e^{\mathrm{rep,rx}}$ 分别表示源 UAV 的服务与发射功率以及替补 UAV 的飞行与接收功率。$E_e^{\mathrm{src,fin}}$、$E_e^{\mathrm{src,ret}}$ 和 $E_e^{\mathrm{src,res}}$ 分别表示源 UAV 的固定切换能耗、返航能耗和返航安全余量；$E_e^{\mathrm{rep,max}}$、$E_e^{\mathrm{rep,fin}}$、$E_e^{\mathrm{rep,min}}$ 和 $E_e^{\mathrm{rep,trig}}$ 分别表示替补 UAV 的满电能量、固定切换能耗、最低服务能量和接管区域的轮换阈值。

在没有参与状态同步或最终切换时，工作 UAV 只消耗区域服务功率，因此其电量满足

$$
\frac{\mathrm d E_u(t)}{\mathrm dt}
=
-P_u^{\mathrm{srv}},
\qquad
u\in\mathcal A_e.
$$

该递推与阈值 $E_{u,e}^{\mathrm{trig}}$ 共同确定后续轮换何时触发。

源 UAV 在事件触发后到 $T_e^{\mathrm{cut}}$ 持续服务，并在 $[T_e^{\mathrm{link}},T_e^{\mathrm{cut}})$ 额外发送状态，因此其停止接收新请求时的电量为

$$
E_e^{\mathrm{src,cut}}
=
E_e^{\mathrm{src,start}}
-
P_e^{\mathrm{src,srv}}
\left(
T_e^{\mathrm{cut}}-T_e^{\mathrm{start}}
\right)
-
P_e^{\mathrm{src,tx}}
\left(
T_e^{\mathrm{cut}}-T_e^{\mathrm{link}}
\right).
$$

最终切换完成后的源 UAV 电量和替补 UAV 电量分别为

$$
E_e^{\mathrm{src,end}}
=
E_e^{\mathrm{src,cut}}
-E_e^{\mathrm{src,fin}}
-P_e^{\mathrm{src,tx}}
\frac{G_e^{\mathrm{rem}}}{R_e^{\mathrm{fin}}},
\qquad
E_e^{\mathrm{rep,end}}
=
E_e^{\mathrm{rep,max}}
-
P_e^{\mathrm{rep,fly}}\tau_e^{\mathrm{out}}
-
P_e^{\mathrm{rep,rx}}
\left(
T_e^{\mathrm{cut}}-T_e^{\mathrm{link}}
\right)
-
P_e^{\mathrm{rep,rx}}
\frac{G_e^{\mathrm{rem}}}{R_e^{\mathrm{fin}}}
-
E_e^{\mathrm{rep,fin}} .
$$

源 UAV 完成最终切换后必须仍有足够能量返回 $\mathbf q_0$，因此需要满足

$$
E_e^{\mathrm{src,end}}
\ge
E_e^{\mathrm{src,ret}}+E_e^{\mathrm{src,res}} .
\tag{C6}
$$

替补 UAV 完成接管后还必须保留最低服务能量，并且不能立即达到区域 $m_e$ 的轮换触发阈值：

$$
E_e^{\mathrm{rep,end}}
\ge
\max
\left\{
E_e^{\mathrm{rep,min}},
E_e^{\mathrm{rep,trig}}
\right\} .
\tag{C7}
$$

C6 和 C7 分别保证源 UAV 能安全返航、替补 UAV 不会在刚接管后立即失去服务能力或再次触发轮换。所有 UAV 在整个评估时段内的剩余电量必须位于其电池容量范围内：

$$
0\le E_u(t)\le E_u^{\max},
\qquad
\forall u\in\mathcal U,\ t\in[0,H].
\tag{C8}
$$

一次事件的轮换能耗只统计参与该次轮换的源 UAV 和替补 UAV，包括替补飞行、源端服务、A2A 状态传输、最终切换和源 UAV 返航；其他区域持续服务的基准能耗在所有策略下相同，不计入该指标：

$$
E_e^{\mathrm{rot}}
=
P_e^{\mathrm{rep,fly}}\tau_e^{\mathrm{out}}
+
P_e^{\mathrm{src,srv}}
\left(
T_e^{\mathrm{cut}}-T_e^{\mathrm{start}}
\right)
+
P_e^{\mathrm{src,tx}}
\left(
T_e^{\mathrm{cut}}-T_e^{\mathrm{link}}
\right)
+
P_e^{\mathrm{rep,rx}}
\left(
T_e^{\mathrm{cut}}-T_e^{\mathrm{link}}
\right)
+
\left(
P_e^{\mathrm{src,tx}}
+
P_e^{\mathrm{rep,rx}}
\right)
\frac{G_e^{\mathrm{rem}}}{R_e^{\mathrm{fin}}}
+
E_e^{\mathrm{src,fin}}
+
E_e^{\mathrm{rep,fin}}
+
E_e^{\mathrm{src,ret}} .
$$

令 $T_e^{\mathrm{prep}}$ 表示本次源 UAV 返站后重新具备派出条件所需的固定准备时长。交接完成后，源 UAV $s_e$ 退出工作集合，替补 UAV $u_e$ 接管区域 $m_e$。下一次事件开始时，工作集合和工作 UAV 到区域的关系更新为

$$
\mathcal A_{e+1}
=
\left(
\mathcal A_e\setminus\{s_e\}
\right)
\cup\{u_e\},
\qquad
\mu_{u,e+1}
=
\begin{cases}
m_e, & u=u_e,\\
\mu_{u,e}, & u\in\mathcal A_e\setminus\{s_e\},
\end{cases}
$$

$$
\rho_{u,e+1}
=
\begin{cases}
T_e^{\mathrm{end}}
+
\tau_e^{\mathrm{ret}}
+
T_e^{\mathrm{prep}},
& u=s_e,\\
+\infty,
& u=u_e,\\
\rho_{u,e},
& \text{otherwise},
\end{cases}
$$

$$
\mathcal R_{e+1}
=
\left\{
u\in\mathcal U\setminus\mathcal A_{e+1}:
\rho_{u,e+1}
\le
T_{e+1}^{\mathrm{start}}
\right\},
\qquad
\mathcal C_{e+1}
=
\mathcal U\setminus
\left(
\mathcal A_{e+1}\cup\mathcal R_{e+1}
\right).
\tag{C9}
$$

其中 $\tau_e^{\mathrm{ret}}$ 是本次源 UAV 从服务点返回换电站的直线飞行时间。源 UAV 的最早可派出时刻在本次交接后更新；任何 UAV $u$ 在其最早可派出时刻恢复满电，即 $E_u(\rho_{u,e+1})=E_u^{\max}$。新工作 UAV 的值设为 $+\infty$，表示其正在服务；其他 UAV 沿用已有的最早可派出时刻。C9 同时更新本次源 UAV 和此前已处于 $\mathcal C_e$ 的其他 UAV。

为使单事件模型成立，本次交接完成前不能有其他工作 UAV 进入必须立即轮换的状态。其他区域的工作 UAV 在事件期间继续提供区域服务，因此需要满足

$$
E_u(T_e^{\mathrm{end}})
=
E_u(T_e^{\mathrm{start}})
-
P_u^{\mathrm{srv}}
\left(
T_e^{\mathrm{end}}-T_e^{\mathrm{start}}
\right)
\ge
E_{u,e}^{\mathrm{trig}},
\quad
\forall u\in\mathcal A_e\setminus\{s_e\},
$$

以及

$$
T_{e+1}^{\mathrm{start}}
\ge
T_e^{\mathrm{end}} .
\tag{C10}
$$

C10 排除多个轮换交接过程的重叠。第 $e$ 次交接结束后，下一事件开始时刻由更新后的工作 UAV 电量首次达到触发阈值的时刻确定；若源 UAV 尚未完成返航和返站准备，它仍属于 $\mathcal C_{e+1}$。

### 2.5 问题构建

基于上述模型，控制器在 $T_e^{\mathrm{start}}$ 只能使用当时已经获得的物理信息。记替补选择向量为 $\mathbf x_e=(x_{u,e})_{u\in\mathcal U}$，用 $\pi$ 表示因果决策策略，则

$$
\left(
\mathbf x_e,
\tau_e^{\mathrm{dep}},
\theta_e
\right)
=
\pi
\left(
m_e,\,
\{G_m(T_e^{\mathrm{start}})\}_{m\in\mathcal M},\,
\{E_u(T_e^{\mathrm{start}})\}_{u\in\mathcal U},\,
\mathcal A_e,\,
\mathcal R_e,\,
\mathcal C_e,\,
\{\mu_{u,e}\}_{u\in\mathcal A_e},\,
\{\rho_{u,e}\}_{u\in\mathcal U}
\right).
\tag{C11}
$$

C11 是因果性约束，禁止策略使用事件开始之后才会获得的链路、位置、状态或能量信息。

这里的“已知信息”只表示控制器在事件开始时能够读取的物理状态，并不预设强化学习或其他特定算法的观测空间；具体求解方法在方法章节中另行定义。

评估时段的末端取在一次完整交接之后，使 $T_N^{\mathrm{end}}\le H$，且时段末尾不存在尚未完成却被忽略的交接。对上述 $N$ 次完整轮换，长期服务中断率定义为

$$
F^{\mathrm{down}}
=
\frac{1}{|\mathcal M|H}
\sum_{e=1}^{N}D_e ,
$$

评估时段内的累计轮换能耗定义为

$$
F^{\mathrm{energy}}
=
\sum_{e=1}^{N}E_e^{\mathrm{rot}} .
$$

其中 $F^{\mathrm{down}}$ 是无量纲的区域平均中断比例，$F^{\mathrm{energy}}$ 的单位为焦耳。由于所有策略使用相同的评估时段长度 $H$，最小化累计轮换能耗与最小化单位时间轮换能耗等价。状态传输量、待命 UAV 数量和返站准备时间作为解释性指标，不单独设置为优化目标。当前模型采用确定性参数和事件开始时可获得的物理状态；若后续将请求到达或状态产生建模为随机过程，可在目标外层增加期望或风险算子。

P0 是确定性的连续时间、事件驱动、序贯混合整数非线性双目标优化问题。离散替补选择决定飞行时间、A2A 链路和后续机队状态，两个连续时间决策共同改变状态同步队列、双方电量和源 UAV 的重新可用时刻。约束 C1–C8 和 C11 对 $e=1,\ldots,N$ 生效，跨事件约束 C9–C10 对 $e=1,\ldots,N-1$ 生效。基于前面已经定义的目标、决策和约束，P0 写为

$$
\mathrm{P0}:\quad
\min_{\pi}
\left(
F^{\mathrm{down}},
F^{\mathrm{energy}}
\right)
\quad
\mathrm{s.t.}\quad
\mathrm{C1\text{--}C11}.
$$

**Decision variables**:

| Variable         | Symbol                                                                                                               | Type / range                            | Meaning |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ------- |
| 替补 UAV 选择    | $x_{u,e}$               | binary,$\{0,1\}$                           | 第$e$ 次轮换是否选择 UAV $u$ 作为替补 |                                         |         |
| 替补派出等待时长 | $\tau_e^{\mathrm{dep}}$ | continuous,$[0,\bar\tau_e^{\mathrm{dep}}]$                                             | 从事件开始到替补起飞的时间              |         |
| 重叠服务时长     | $\theta_e$              | continuous,$[0,\bar\theta_e]$                                                          | 从替补起飞到源 UAV 停止接收新请求的时间 |         |

**State variables**:

| State          | Symbol                                                                                                                 | Type / unit | Meaning |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------- | ------- |
| UAV 状态集合   | $\mathcal A_e,\mathcal R_e,\mathcal C_e$ | three disjoint sets | 第$e$ 次事件开始时工作、待命和暂不可用的 UAV      |             |         |
| 服务区域关系   | $\mu_{u,e}$                              | region index        | 第$e$ 次事件开始时工作 UAV $u$ 负责的服务区域   |             |         |
| 最早可派出时刻 | $\rho_{u,e}$                             | continuous time, s  | UAV$u$ 完成返航和返站准备后能够再次派出的最早时刻 |             |         |
| 应用运行状态量 | $G_m(t)$                                 | data volume         | 区域$m$ 自上次成功交接后产生的增量状态总量        |             |         |
| 同步队列       | $B_e(t)$                                 | data volume         | 第$e$ 次交接中已经产生但尚未传到替补 UAV 的状态量 |             |         |
| UAV 剩余电量   | $E_u(t)$                                 | energy, J           | UAV$u$ 在全局时刻 $t$ 的剩余电量                |             |         |

$S_e$、$G_e^{\mathrm{cut}}$、$G_e^{\mathrm{rem}}$、$D_e$、$E_e^{\mathrm{rot}}$ 和各事件阶段时刻均由上述状态、策略输出和固定参数推导，不作为独立控制变量。

**Constraints summary**:

| ID  | Meaning                                                                |
| --- | ---------------------------------------------------------------------- |
| C1  | 每个服务区域恰由一架工作 UAV 服务。                                    |
| C2  | 替补 UAV 唯一、在实际派出时已经可用且与目标应用兼容。                  |
| C3  | 替补等待时长和重叠服务时长位于运行范围内。                             |
| C4  | 替补建立 A2A 链路并到达交接等待点后，源 UAV 才能停止接收新请求。       |
| C5  | 最终状态传输、恢复和连接重定向完成，且单次中断不超过$D^{\max}$。     |
| C6  | 源 UAV 完成切换后仍保留返航能量和安全余量。                            |
| C7  | 替补 UAV 接管后保留最低服务能量。                                      |
| C8  | 所有 UAV 的剩余电量保持在零与其电池容量之间。                          |
| C9  | 源 UAV 在返航和返站准备完成后重新进入待命集合，区域工作 UAV 完成更新。 |
| C10 | 当前交接期间其他工作 UAV 不触发轮换，轮换事件按时间串行执行。          |
| C11 | 决策只使用事件开始时可获得的信息。                                     |

P0 只汇总上述已经定义的目标、决策和约束，不在最终 formulation 中重新引入物理关系。当前场景保留长期轮换、有限待命池、运行状态增长、移动 A2A 同步和源 UAV 返航安全之间的耦合。

## 3. 逐篇全文证据与阅读清单

|  # | 论文                                                                                                                                   | 全文确认的研究对象与主要决策                                                                                                                           | 对当前场景的可继承部分与边界                                                                                                                                                                                                                        | 全文证据                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -: | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  1 | **Live Migration of Stateful Microservices in UAV-Assisted Networks for Enhanced Availability，ISCC 2025**                       | 低电量触发替补 UAV 起飞；替补预取镜像，源 UAV 停止服务后经 A2A 链路传输检查点和可写层，随后由替补恢复应用、源 UAV 返站。                               | 在当前已核验论文中，这是唯一明确结合低电量 UAV 替换与有状态微服务迁移的直接先行工作。可继承其源 UAV、替补 UAV、检查点传输和返站流程；其工作停留在架构层面，没有数学模型、求解算法或实验，而且替补起飞时源端即停止服务，也没有有限待命池的长期递推。 | [触发与架构](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:53)；[交接步骤](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:70)；[研究边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:121)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|  2 | **Microservices Migration: A Pathway to Improved Energy Efficiency in UAV Networks，Internet of Things 2025**                    | 按时隙调整活动 UAV 之间的微服务放置，并用包含返站飞行能耗的最低电量阈值限制部署决策。                                                                  | 可用于说明微服务放置已经能够感知 UAV 电量和返站需求，但其“迁移”只是活动 UAV 之间的部署变化，不传输运行状态，也不安排替补 UAV 的派出、接管和长期周转。                                                                                             | [电量阈值](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:76)；[优化模型](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:138)；[时隙求解](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:191)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|  3 | **Efficient Management of Composite Heterogeneous Applications at the Network Edge，TNSM 2026**                                  | 在固定边缘服务器之间联合决定有状态或无状态微服务放置、用户分配、CPU、无线资源块和服务版本，并根据内存量及运行中被改写的内存速率估计迁移停机时间。      | 可借鉴有状态与无状态应用的区分及迁移停机估计。计算节点固定，UAV 只是移动用户，因此没有替补飞行、移动 A2A 传输、返航能量或待命池状态。                                                                                                               | [系统角色](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:92)；[迁移模型](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:230)；[优化问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:253)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|  4 | **Time-Constrained Service Handoff for Mobile Edge Computing in 5G，TSC 2023**                                                   | 针对给定大小的 VM 或容器差分，在线选择固定基站之间的传输路径，并满足用户交接期限、网络排队和各基站的传输能量预算。                                     | 可借鉴交接期限、传输排队和能量预算的约束形式。源端和目标端都是固定节点，迁移量预先给定，也没有源应用继续运行时产生新状态的过程以及 UAV 轮换。                                                                                                       | [固定迁移量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:153)；[网络排队](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:161)；[时间与能量约束](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:187)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|  5 | **ReSync: Coordinated Live-Migration for Stateful Containers in Mobile Edge Computing，TMC 2026**                                | 复制初始检查点后让源容器继续处理请求，同时把此后到达的输入复制到目标端并按原顺序重放；通过源端与目标端的处理队列判断目标能否追上源端。                 | 直接支持“源端继续处理、目标端逐步追上”的重叠交接机制。源端和目标端均为固定主机，因此没有替补到达过程、随距离变化的 A2A 链路、源 UAV 返航能量和长期待命池。                                                                                        | [三阶段流程](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:68)；[双队列](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:141)；[稳定条件](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:204)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|  6 | **CORMO-RAN: Energy Efficiency at the Near-RT RIC via Lossless Migration of O-RAN xApps，TMC 2026**                              | 在开放式无线接入网的固定控制器集群中联合安排有状态控制应用迁移与服务器关停；迁移对象可以是完整运行状态，也可以把需要一致保存的状态放在共享存储中。     | 说明有状态迁移可以与节点关停及能耗优化结合，但这里的能耗来自固定服务器集群，关停节点不需要飞行或返航，也不存在替补 UAV 和跨轮换事件的可用性变化。                                                                                                   | [迁移对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:76)；[双活共享状态](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:91)；[实测边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:142)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|  7 | **Context-Aware AIGC Service Migration in Edge Intelligence Networks via Transformer DRL，TSC 2026**                             | 将每轮交互的提示词和生成结果作为会话历史，由控制器决定迁移多少历史内容，并权衡生成准确率、时延和成本。                                                 | 说明运行中形成的会话历史可以成为迁移决策的一部分。该文允许舍弃部分历史以降低成本，且源端和目标端固定，不满足本文要求替补获得最新必要状态并完成电池轮换的条件。                                                                                      | [上下文对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:81)；[窗口定义](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:83)；[优化问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:162)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|  8 | **TOM: Joint Trajectory, Offloading and Migration Optimization in Stateful Service-Oriented UAV-Enabled VEC System，TSC 2025**   | 联合决定多 UAV 三维轨迹、车辆任务卸载和有状态服务的并行迁移计划；每次迁移的数据量由虚拟机内存需求给定。                                                | 在本表的高水平论文中，该文与 UAV 有状态迁移优化最接近，可借鉴移动 UAV 间服务迁移与联合决策的建模方式。它没有低电量触发的源 UAV 与替补 UAV、有限待命池、替补到达过程或源 UAV 返航约束。                                                              | [系统与任务](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:79)；[固定 VM 内存](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:175)；[联合决策](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:200)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|  9 | **Energy-Aware Multi-UAV Collaboration for Data Collection and Trajectory Planning With MADDPG，TNSM 2026**                      | 多架 UAV 收集静态用户的有限数据；每次执行动作前检查完成动作、飞到下一位置并返航所需的能量，不满足时中止动作并返航。                                    | 为“执行当前操作后仍须保留返航能量”提供直接建模依据。其任务是有限数据收集，没有替补 UAV 接管、应用运行状态或跨事件的轮换调度。                                                                                                                     | [数据收集对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:104)；[返航检查](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:216)；[决策变量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:292)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 10 | **Trajectory and Resource Allocation for UAV Replacement to Provide Uninterrupted Service，TCOM 2023**                           | 低电量 UAV 返回充电站、满电 UAV 飞往原服务区域接替；联合优化两架 UAV 的轨迹和面向用户的下行带宽，以维持通信吞吐。                                      | 直接提供低电量源 UAV、满电替补 UAV 和安全返航的物理角色。其连续性只指无线覆盖和吞吐，未迁移应用状态，也未维护长期待命池；本文固定轨迹和带宽，不再重复其轨迹与无线资源优化。                                                                         | [替换过程](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:56)；[能量与端点](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:134)；[联合轨迹与带宽](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:360)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 11 | **Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks，TMC 2026** | 根据车辆移动预测联合选择承载服务的 UAV 及其轨迹，并迁移车辆任务和固定大小的服务配置文件，以长期平均迁移成本约束服务时延。                              | 可借鉴移动 UAV 间的服务承载节点选择和长期在线控制。迁移对象是任务与固定服务配置，不是持续更新的运行状态，并且没有推进电池、返航和待命 UAV 周转。                                                                                                    | [迁移对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:60)；[优化问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:152)；[能量边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:498)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 12 | **Live Migration of Video Analytics Applications in Edge Computing，TMC 2024**                                                   | 将视频分析应用的状态分为永久、关键和可重新生成三类；目标端准备和同步期间源端继续处理视频，最后传输最新关键状态并停止源端。                             | 直接支持应用级状态划分、源端继续处理和最终短暂停服的交接过程。计算节点固定，因此没有替补飞行、移动 A2A 条件、返航能量和长期轮换。                                                                                                                   | [三类状态](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:111)；[源端继续处理](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:166)；[处理后更新状态](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:178)；[有限窗口覆盖](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:216)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 13 | **Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing，TMC 2026**                          | 单架 UAV 依次访问任务点，并在电量不足时返回基站换电；联合决定访问顺序、飞行速度、任务卸载、计算资源购买和换电时机。                                    | 可借鉴飞行、计算、通信和换电能耗的统一核算，以及任务期间的换电时机。执行任务的是同一架 UAV，换电后仍由其继续服务，没有替补 UAV、待命池或有状态应用交接。                                                                                            | [场景](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:37)；[电池与期限](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:136)；[联合决策](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:228)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 14 | **Design, Modeling, and Implementation of Robust Migration of Stateful Edge Microservices，TNSM 2024**                           | 建模内存量、运行中内存更新、检查点与恢复开销以及传输带宽，并保留容器的内存和网络连接状态。                                                             | 可作为运行中状态迁移量、迁移时长和最终停机时间的过程模型。源端和目标端是固定边缘主机，不处理 UAV 到达、返航或长期轮换。                                                                                                                             | [状态对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:49)；[脏页模型](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:59)；[配置公式](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:526)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 15 | **MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge，TNSM 2025**                             | 在固定边缘主机之间选择停服后迁移、单次预拷贝或迭代预拷贝，并联合配置传输带宽和迭代次数，以限制总迁移时间或停机时间。                                   | 可用于选择适合交接期限的状态传输方式，并估计带宽与迭代次数对停机时间的影响。状态规模和内存更新速率由测量结果给定，节点固定，也没有电池和待命池约束。                                                                                                | [运行态迁移](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:53)；[状态标定](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:103)；[编排问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:111)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 16 | **Efficient Live Migration of Edge Services Leveraging Container Layered Storage，TMC 2019**                                     | 先传输容器基础层和基础内存，源端继续运行并迭代传输更新的内存，最终再传可写层、元数据和剩余内存差分。                                                   | 可继承镜像预置、容器分层和源端继续运行时的增量传输机制。该文不包含替补 UAV 的飞行过程、距离相关 A2A 速率、返航能量或长期轮换。                                                                                                                      | [完整迁移流程](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:221)；[最终停止](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:232)；[状态增长边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:425)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 17 | **KubeSPT: Stateful Pod Teleportation for Service Resilience With Live Migration，TSC 2025**                                     | 迁移容器编排平台中应用实例的网络、内存和运行上下文；迭代生成检查点后，目标端优先恢复常用内存页，其余内容在运行中按需恢复。                             | 可作为完整容器网络状态和渐进恢复的系统实现基线。源端与目标端固定，迁移由故障恢复触发，不包含低电量替换、移动 A2A 和待命池周转。                                                                                                                     | [对象与触发](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:11)；[预拷贝与恢复](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:162)；[关停时间](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:302)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 18 | **Multi-Cell Mobile Edge Computing: Joint Service Migration and Resource Allocation，TWC 2021**                                  | 用户切换基站时，在固定边缘服务器之间迁移包含用户配置和应用的虚拟机服务环境，并联合决定虚拟机放置、用户关联和无线资源块；迁移成本固定，迁移时间被忽略。 | 可借鉴服务迁移与无线资源分配的联合建模，但迁移过程被简化为固定成本，无法描述运行状态持续产生及同步所需的时间；固定服务器也没有电池轮换。                                                                                                            | [服务环境与假设](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:45)；[基本问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:82)；[RB 扩展](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:366)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 19 | **Mobility-Aware Seamless Service Migration and Resource Allocation in Multi-Edge IoV Systems，TMC 2025**                        | 在固定边缘服务器之间联合选择服务迁移目的地和 CPU 资源；服务实例包含运行数据和用户上下文，但迁移数据量作为给定输入，任务在迁移完成后才开始处理。        | 明确了服务实例可以包含运行数据和用户上下文，但这些数据在决策前已经给定，且服务迁移时不继续处理任务。因而不能表示替补飞行期间源端继续服务、状态继续变化和返航期限之间的联系。                                                                        | [状态语义](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:13)；[外生迁移量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:62)；[迁移后处理](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:72)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 20 | **Service Migration Strategies Based on Partially Observable and Multi-Objective Optimization，TMC 2026**                        | 在部分可观测的固定 MEC 环境中选择迁移目的服务器，以服务时延以及迁移、传输和计算能耗为多目标；迁移数据量作为给定参数。                                  | 可作为时延与能耗多目标迁移的算法参考。其迁移量外生给定，能耗来自计算和网络而非 UAV 推进电池，也没有替补派出和有限待命池。                                                                                                                           | [迁移与任务时序](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:40)；[能量模型](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:42)；[环境隐状态](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:146)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 21 | **Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC，TWC 2024**                          | 在两个时间尺度上联合决定服务迁移或任务重路由、任务卸载、CPU 和带宽，并通过长期平均能耗约束控制固定 MEC 系统的运行成本；被迁移的应用大小给定。          | 可借鉴跨时隙决策、长期平均指标和在线优化框架。应用大小及服务器集合固定，系统状态不包含待命 UAV 的派出、返站和重新可用过程。                                                                                                                         | [任务队列](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:89)；[固定应用量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:169)；[变量与约束](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:235)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 22 | **Joint Optimization of Trajectory, Offloading, Caching, and Migration for UAV-Assisted MEC，TMC 2025**                          | 联合决定 UAV 轨迹、用户关联、卸载、计算、任务迁移、任务缓存和 A2A 带宽；迁移对象是具有固定输入量和计算需求的未处理任务。                               | 说明 UAV 轨迹、A2A 传输和任务调度可以联合优化。其迁移对象是未处理任务，不是长期运行应用的最新状态；论文也把低电量 UAV 退出留作未来工作，没有替补和轮换。                                                                                            | [对象与互斥动作](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:108)；[队列与成本](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:207)；[低电量边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:1012)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 23 | **Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks，TSC 2025**                               | 根据单个任务的执行进度确定需要迁移的剩余输入和部分结果，并联合决定任务卸载与迁移，同时处理任务的软期限和硬期限。                                       | 为“源端继续计算会改变待迁移数据量”提供最接近的任务级证据。变化对象是单个任务的剩余输入和部分结果，不是长期应用状态，也没有电池替换、待命池和返航约束。                                                                                            | [迁移触发](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:174)；[剩余输入与部分结果](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:158)；[问题与变量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:194)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 24 | **Joint Content Caching, Service Placement, and Task Offloading in UAV-Enabled Mobile Edge Computing Networks，JSAC 2025**       | 联合决定静态内容缓存、应用或库及数据库的服务放置和任务卸载，不迁移应用运行期间产生的状态。                                                             | 用于区分预先部署的静态应用材料与交接时必须更新的运行状态，也支持把静态服务材料提前放在 UAV 上的简化假设；该文没有低电量替换、状态同步或长期轮换。                                                                                                   | [系统与请求](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:35)；[时延与能耗](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:97)；[联合问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:169)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 25 | **Serv-HU: Service Hand-off for UAV-as-a-Service，TSC 2025**                                                                     | 由主服务商选择其他 UAV 服务商接管暂时无法覆盖的地理区域，并联合决定服务价格；飞行能耗作为服务成本的一部分。                                            | 其交接对象是服务商承担的地理覆盖责任，而不是一架低电量 UAV 上正在运行的应用。除术语和飞行成本外，不能直接支撑状态迁移、替补周转或一致接管。                                                                                                         | [问题场景](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:51)；[能耗用途](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:293)；[结论](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:680)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 26 | **Optimizing UAV Resupply Scheduling for Heterogeneous and Persistent Aerial Service，TRO 2023**                                 | 在多个固定空中服务位置与一个补能站之间安排周期轮换，并在不同往返时间下确定轮换顺序、接替间隔和维持持续覆盖所需的最小 UAV 数量。                        | 可直接作为多个固定服务位置、单补能站、周期轮换和有限机队的长期调度基础。其目标是持续覆盖并最小化机队规模，未描述运行应用、A2A 状态传输和替补接管时的最新状态。                                                                                      | [场景与轮换目标](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:45)；[最小机队问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:60)；[HORR/PHERR 调度](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md:68)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 27 | **Seamless Service Handover in UAV-Based Mobile Edge Computing，GLOBECOM 2023**                                                  | 低电量 UAV 返站前提前派出满电 UAV；调度器选择派出站、回收站和派出时机，并检查满电 UAV 与充电位是否可用。论文只在概念上提到转移计算任务的当前状态。     | 是低电量 UAV-MEC 替补派出与补能站资源管理的直接先行工作。它没有完整数学模型，也未形式化具体替补 UAV、应用状态、A2A 传输和库存递推；本文简化为单补能站，但需要把这些关系写入长期优化模型。                                                           | [低电量交接与目标](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:34)；[多站点架构](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:45)；[调度伪代码](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:62)；[仿真设置](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md:99)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 28 | **Cost Optimization of UAV Swarm Network for Persistent Emergency Communication，TGCN 2026**                                     | 在灾后多跳通信网络中联合决定 UAV 与服务位置的对应关系、周期轮换路径和中继树重连方案，并在返航能量约束下最小化机队规模。                                | 可继承周期轮换、返航能量和持续服务约束的建模思路。其轮换对象是通信接入或中继角色，不是有状态应用；本文也不再优化轨迹和中继树。                                                                                                                      | [连续时间位置与链路](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:71)；[问题与约束](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:129)；[返航能量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:123)；[连续时间约束说明](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:190)；[PRP 周期轮换](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:194)；[持续连通结果](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication/Cost_Optimization_of_UAV_Swarm_Network_for_Persistent_Emergency_Communication.md:539) |

建议按各论文对当前模型的作用阅读：

1. **长期轮换骨架：[26] → [28] → [10] → [27]。** [26] 先建立固定服务位置、单补能站和有限机队的周期轮换；[28] 补充返航能量与持续服务约束；[10] 给出一次低电量替换中源 UAV 与替补 UAV 的飞行关系；[27] 再补充待命 UAV、派出时机和补能站资源。
2. **有状态交接过程：[1] → [5] → [12] → [14] → [15] → [16] → [17]。** [1] 用来确认电池轮换中的直接交接流程，其余论文依次核对源端继续运行、状态保留、增量传输、最终停机和目标端恢复可以采用哪些成熟机制。
3. **UAV-MEC 中的迁移对象与联合决策：[8] → [23] → [22] → [11]。** [8] 是 UAV 有状态服务迁移的主要优化参照；[23] 说明继续计算会改变需要迁移的数据；[22] 和 [11] 分别用于比较 A2A 任务传输及固定服务配置迁移与本文运行状态交接的差异。
4. **补充建模依据：[13] → [9] → [21]。** [13] 用于核对换电时机和多类能耗，[9] 支撑返航电量检查，[21] 提供长期平均指标与跨时隙在线决策的参考。

[2]–[4]、[6]、[7]、[18]–[20]、[24] 和 [25] 主要用于澄清微服务放置、固定节点迁移、部分上下文迁移和区域服务责任转移等概念边界，不必作为第一轮精读材料。

## 4. 可行性验证与当前判断

### 4.1 需要验证的三个核心关系

1. **重叠交接能否减少中断。** 在相同源 UAV、替补 UAV 和固定航路下，对比“替补起飞时停止源服务”与“替补飞行期间源端继续服务”两种流程，分别测量飞行等待、最终状态传输、恢复和总中断时间。
2. **状态同步与返航能量是否形成真实权衡。** 标定具体应用的状态产生速率 $\gamma_m$、移动 A2A 速率、最终恢复时间以及源 UAV 的悬停、计算和传输能耗，检查延后切换是否既能减少剩余迁移时间，又会压缩返航能量。
3. **有限待命池是否改变长期决策。** 在不同待命 UAV 数量、轮换事件间隔和返站准备时间下，对比逐事件贪心策略与长期策略，检查替补选择和派出时机是否会改变后续事件的可行替补集合、长期中断率和累计轮换能耗。

实验只需一个经过标定的有状态应用、一组固定服务区域和一个换电站。主要结果报告 $F^{\mathrm{down}}$、$F^{\mathrm{energy}}$、p95 中断时间、无可行替补事件比例和安全返航约束违反次数；状态传输量和待命池利用率用于解释结果，不作为额外目标。无可行替补事件比例是对策略失效的诊断指标，不属于 P0 的目标函数。

### 4.2 必要基线

- **先停后接：** 按 Frejo-Martín 等 [1] 的流程，在替补起飞时停止源服务。
- **首次可用替补：** 每次选择事件开始时待命池中的第一架兼容 UAV 并立即派出；若不存在候选，则记录一次不可行事件。
- **单事件最优：** 对每次轮换独立最小化当前中断和能耗，不考虑返航 UAV 何时重新进入待命池。
- **长期状态感知策略：** 同时考虑候选 UAV 的最早可派出时刻、派出等待、重叠交接以及 $\mathcal A_e$、$\mathcal R_e$、$\mathcal C_e$ 的角色递推，对应 P0。

前两项验证重叠交接的价值，后两项隔离长期待命池带来的收益。由于本文已经固定航路、速度和带宽，不再设置轨迹优化或动态带宽分配基线。

### 4.3 主要风险与退出条件

- 如果替补均同构且应用兼容性相同，替补选择会退化为任意选择；因此至少需要保留电池容量、飞行能耗或应用兼容性中的一种有限异构。
- 如果待命池在所有测试负载下都始终存在多个等价候选，长期问题会退化为彼此独立的单次交接；此时应删除机队可用状态递推，不再主张长期轮换贡献。
- 如果源 UAV 在替补出发时已经没有重叠服务所需的能量，重叠窗口不存在，系统只能通过更早触发轮换解决。
- 如果状态产生速率远低于 A2A 传输能力，或者替补飞行时间很短，重叠同步可能只是显然的流程调整，难以形成独立研究问题。
- 如果固定状态产生率 $\gamma_m$ 无法解释真实应用的状态变化，应改用从原型测得的分段或随机模型，但不同时恢复用户级任务队列和 CPU 决策。
- 如果轮换事件经常并发，串行事件假设失效；第一篇论文应限定为轮换间隔足以避免交接重叠的运行区间，而不是立即扩展到并发匹配。

### 4.4 当前判断

调整后的问题不再只研究一次交接，而是把一次重叠交接嵌入有限待命 UAV 池的长期轮换过程。其核心区别是：当前选择的替补和切换时机既决定本次状态迁移与返航能耗，也决定源 UAV 何时返回待命池，从而影响后续轮换能否及时完成。

Frejo-Martín 等 [1] 已经提出电池轮换中的有状态服务迁移流程；Arribas 等 [26]、Ye 等 [27] 和 Liu 等 [28] 也分别研究了长期补能调度、多补能站派出管理和周期性持续通信。因此，不能把“首次研究电池轮换”或“首次研究替补选择”作为创新主张。更稳妥的定位是：在已核验文献范围内，尚未看到同时建模长期轮换与有状态应用交接的联合优化工作，其中需要共同考虑应用状态持续产生、替补飞行期间的 A2A 传输、最终一致切换和源 UAV 安全返航。只有当重叠交接和状态感知确实改变 $F^{\mathrm{down}}$ 或 $F^{\mathrm{energy}}$，这个场景才足以继续发展为完整的 Trans 论文。
