# 电池轮换 UAV-MEC 有状态服务交接：研究问题、文献边界与验证路径

## 1. 从 UAV-MEC 持续运行到有状态服务交接

无人机搭载轻量计算服务器后，可以飞到地面边缘设施不足或临时业务集中的区域，就近接收并处理用户请求。这类系统通常称为无人机辅助移动边缘计算（UAV-MEC）。救灾通信、临时活动保障和持续视频分析可能需要运行数小时，单架 UAV 的电池却难以支撑整个服务周期。因此，长期运行通常依靠多架 UAV 轮换：一架在空中提供服务，电量降低后返回补能站，另一架飞来继续服务。

本文把正在提供服务的无人机称为源 UAV，把前来轮换的无人机称为替补 UAV。对于只提供无线接入或无状态计算的系统，替补 UAV 到位并启动同一程序后，服务便可以继续。视频目标跟踪、连续对话推理和流式数据分析则不同。这些应用会在运行中保留目标编号和最近位置、对话历史、窗口中间结果等信息。下文把这类会影响后续处理结果的信息统称为运行状态，把依赖这些信息的应用称为有状态服务。

有状态服务不能只靠替换飞行平台来延续。替补 UAV 即使部署了相同的程序和模型，如果没有获得最新运行状态，目标跟踪可能重新编号，对话可能丢失上下文，尚未结束的分析窗口也可能从头计算。源 UAV 离开前，系统必须把继续服务所必需的状态传给替补 UAV，并确认此后只有替补 UAV 更新这份状态。本文所说的有状态服务交接，就是这一状态转移和服务控制权切换过程。

这里的“有状态服务交接”有明确含义：它不是在不同 UAV 服务商之间转交尚未覆盖的地理区域，也不是为一份大小已经确定的 VM 或容器数据选择传输路径，而是把源 UAV 在运行中形成的必要状态及其唯一更新权交给替补 UAV。

电池轮换还给交接规定了明确的时间边界。负责机群轮换的调度器根据源 UAV 的剩余电量和既定返航路线，可以计算它最迟何时必须停止服务并开始返航；再晚，即使立即停止计算，也可能无法安全抵达补能站。下文把这一时刻称为**最晚开始返航时刻**。替补 UAV 到达后到该时刻之前的这段时间，是两架 UAV 完成交接的可用窗口。

交接窗口内，用户请求仍在到达。源 UAV 如果过早停止处理，等待服务的请求会迅速增加；如果继续处理，已经完成并确认的请求又会改变后续请求依赖的持久状态，其中尚未传给替补 UAV 的部分必须在交接结束前补传。计算和状态传输都会消耗源 UAV 的剩余电量。两架 UAV 之间的空对空链路（air-to-air，A2A）容量也有限，状态不能瞬间传完。因此，多处理请求可以减少等待，却可能增加随后需要传输的状态量，并压缩返航前剩余的时间和电量。

本文研究的问题由此形成：

> 在替补 UAV 已经到达、源 UAV 必须按时返航的条件下，如何决定源 UAV 继续处理多少请求、为 A2A 状态传输分配多少资源，以及何时停止源端处理，使等待请求不超过系统容量、替补 UAV 获得全部必要运行状态，并让源 UAV 在交接后仍有足够电量安全返航。

这个问题不是一般的 UAV 轮换，也不是一般的状态迁移。它关注一个更窄的决策关系：源 UAV 多完成并确认一些请求，会同时减少尚未处理的请求和增加替补处理后续请求时必须继承的跨请求状态；计算、状态传输和返航又使用同一块电池，并受同一个最晚开始返航时刻约束。只有真实应用中确实存在这组关系，而且新增状态量可以由已完成请求量给出可信上界，这个研究问题才成立。

## 2. 一次电池轮换中的交接过程

### 2.1 研究起点与系统边界

一次轮换开始前，轮换调度器已经选定源 UAV 和替补 UAV，规划好源 UAV 的返航路线，并给出替补 UAV 的预计到达时刻和源 UAV 的最晚开始返航时刻。本文接受这些结果作为输入，不再选择替补 UAV，也不重新规划长期机群轮换或连续飞行轨迹。在线交接控制从替补 UAV 到达并建立稳定 A2A 链路后开始，到替补 UAV 独立提供服务、源 UAV 开始返航时结束。

### 2.2 操作顺序

一次交接按以下顺序进行：

1. 在替补 UAV 到达前，系统把应用程序、模型、运行库和一个基础检查点预先部署到替补 UAV。基础检查点是交接开始前保存的一份运行状态，替补 UAV 将在它的基础上接收后续更新。镜像预置、容器分层、检查点/恢复和 A2A 传输均采用现有迁移机制，不作为本文的协议创新。
2. 替补 UAV 到达能够覆盖用户并与源 UAV 通信的位置后，源 UAV 继续处理用户请求，同时把已经确定不会再修改的状态记录传给替补 UAV。为避免两架 UAV 同时修改同一份状态，交接完成前只有源 UAV 可以确认请求已经完成并写入运行状态。
3. 控制器选择停止源端处理的时隙。源 UAV 从该时隙起不再确认新的请求，只传输最后一批运行状态；替补 UAV 载入这些状态并检查其版本。
4. 状态检查通过后，新请求改由替补 UAV 处理，仍在等待的请求也转发给替补 UAV。源 UAV 随即沿既定路线返航。

当替补 UAV 的运行状态与源 UAV 最后确认的处理结果一致，而且后续请求只由替补 UAV 处理时，本次交接完成。这里的服务连续性不只是无线覆盖没有中断，也不只是两架 UAV 安装了同一应用。

### 2.3 交接过程中涉及的数据

在线控制把交接窗口划分为长度相同的时隙，并用 $t$ 表示时隙编号。为了区分“尚未处理的请求”和“已经处理但尚未交给替补 UAV 的状态”，本文把窗口内的数据分为三类。

1. **等待请求队列 $Q[t]$。** $Q[t]$ 表示时隙 $t$ 开始时尚未完成的请求量。这些请求存放在用户设备、接入网关或集中调度器中，尚未改变应用运行状态。交接完成后，它们可以直接交给替补 UAV 处理。
2. **预先部署的静态内容。** 应用程序、模型参数、运行库和基础检查点在交接窗口开始前已经位于替补 UAV，不占用窗口内用于传输最新运行状态的容量。
3. **未同步状态量 $G[t]$。** 基础检查点建立后，源 UAV 完成并确认请求所产生的跨请求必要状态，如果尚未传到替补 UAV，就计入 $G[t]$。这些更新可以由应用级写前日志（write-ahead log，WAL）、带版本号的状态记录或只记录已确认状态变更的事件日志表示。无论采用哪种实现，应用都必须明确哪些后续请求依赖这些更新，并通过一致性实验验证替补 UAV 能否据此继续服务。只保存最近若干帧且会覆盖旧值的窗口、可舍弃的历史上下文和单个未完成任务的中间结果，不属于这里默认的可追加状态类。

上述划分是后续模型成立的前提。如果等待请求实际保存在源 UAV 的容器内，这部分请求也必须随容器迁移，便不能再与运行状态分开建模。如果日志记录所有到达请求，而不区分请求是否已经由源 UAV 完成，那么日志增长主要由外部请求到达率决定，问题将接近 ReSync 的输入回放模型，源端处理量也不再决定需要传输多少状态。

### 2.4 本文决定什么

本文只研究一次交接，源 UAV、替补 UAV、替补到达时刻和最晚开始返航时刻均已给定。控制器在这个窗口内决定：

- 源 UAV 每个时隙完成多少请求；
- 每个时隙为 A2A 状态传输分配多少资源；
- 在哪个时隙停止源端处理并完成最后一次状态传输。

长期 UAV 数量配置、多次轮换之间的替补匹配、通用容器迁移协议、无线接入切换流程、确认消息丢失后的故障恢复，以及模型未覆盖的飞行故障均不在本文范围内。这些机制由上层系统或底层协议处理。

## 3. 当前阅读清单的逐篇全文证据

本节覆盖第 10 节阅读清单中的全部 25 篇论文。每篇均已检查本地 Markdown 正文，并用同目录 PDF 首页核对 venue、年份和 DOI。表中的“未覆盖”只表示该论文没有解决本文所限定的问题，不表示论文质量不足。直接决定创新边界的工作不能因 venue 较低而排除；论文正文中的一般方法和结论则应优先由 TMC、TWC、TCOM、TSC、TNSM 和 JSAC 等高水平期刊支撑。

### 3.1 二十五篇论文的研究对象、覆盖范围与影响

| # | 论文 | 全文确认的研究对象与决策 | 对本文边界的影响 | 全文证据 |
| ---: | --- | --- | --- | --- |
| 1 | **Live Migration of Stateful Microservices in UAV-Assisted Networks for Enhanced Availability，ISCC 2025** | 低电量触发替补，预取镜像后经 A2A 传检查点和可写层，替补恢复，源 UAV 返站。 | **高威胁。** 电池轮换中的有状态微服务交接架构已存在；但论文没有请求队列、CPU/A2A 联合控制、停止处理时刻、返航完成条件和定量优化。 | [触发与架构](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:53)；[交接步骤](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:70)；[研究边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:121) |
| 2 | **Microservices Migration: A Pathway to Improved Energy Efficiency in UAV Networks，Internet of Things 2025** | 按时隙调整 UAV 群中的微服务放置；最低电量阈值包含飞往充电站所需能量。 | **中高威胁。** 电量感知微服务迁移和飞往充电站所需能量均非新问题；但这里的“迁移”是放置变化，没有运行状态传输、停机和一致性过程。 | [电量阈值](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:76)；[优化模型](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:138)；[时隙求解](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:191) |
| 3 | **Efficient Management of Composite Heterogeneous Applications at the Network Edge，TNSM 2026** | 在固定边缘服务器上联合有状态/无状态微服务放置、用户分配、CPU、RB 和版本选择，并用内存量与脏页率估计迁移停机。 | **中高威胁。** 通用有状态编排和资源联合优化已很完整；UAV 只是移动用户，脏页率按服务版本给定，没有请求完成量产生必要状态或返航约束。 | [系统角色](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:92)；[迁移模型](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:230)；[优化问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:253) |
| 4 | **Time-Constrained Service Handoff for Mobile Edge Computing in 5G，TSC 2023** | 为给定大小的 VM/容器差分在线选择传输路径，满足用户交接期限、网络排队和逐 BS 传输能量预算。 | **中等威胁。** 期限—网络队列—能量预算下的在线交接已经存在；区别只能是迁移量由处理决策改变，并且交接后还要满足源 UAV 返航。 | [固定迁移量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:153)；[网络排队](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:161)；[时间与能量约束](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:187) |
| 5 | **ReSync: Coordinated Live-Migration for Stateful Containers in Mobile Edge Computing，TMC 2026** | 检查点后恢复源容器，把新到输入复制到 FIFO，并在目的端按序回放；用两个耦合队列分析同步收敛。 | **中高威胁。** 它已覆盖迁移期间持续服务和状态追平；但增量由外部输入到达产生，不由源端完成多少请求决定，也没有电池和返航。 | [三阶段流程](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:68)；[双队列](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:141)；[稳定条件](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:204) |
| 6 | **CORMO-RAN: Energy Efficiency at the Near-RT RIC via Lossless Migration of O-RAN xApps，TMC 2026** | 在固定 RIC 集群中迁移有状态 xApp 并关停服务器；支持完整运行态迁移和外置强一致共享状态。 | **中等威胁。** 有状态迁移、节点关停和能耗优化均已覆盖；内存量与脏页率经标定给定，固定服务器没有有限机载电量、物理返航或请求完成量控制。 | [迁移对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:76)；[双活共享状态](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:91)；[实测边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:142) |
| 7 | **Context-Aware AIGC Service Migration in Edge Intelligence Networks via Transformer DRL，TSC 2026** | 每次交互形成 prompt 和 generated output 上下文，控制器选择迁移多少历史窗口，在准确率、时延与成本之间权衡。 | **中等威胁。** 已覆盖“完成交互产生可迁上下文”和迁移量选择；但上下文可以舍弃并用精度损失计价，不是必须无损继承的已确认状态。 | [上下文对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:81)；[窗口定义](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:83)；[优化问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:162) |
| 8 | **TOM: Joint Trajectory, Offloading and Migration Optimization in Stateful Service-Oriented UAV-Enabled VEC System，TSC 2025** | 联合多 UAV 三维轨迹、车辆任务卸载和有状态服务并行迁移；迁移模型采用固定 VM 内存量。 | **中等威胁。** 有状态 UAV 服务迁移与卸载联合优化已经存在；dirty page 和 final sync 只在定性描述中出现，模型没有迁移期间源端处理、状态递推、电池容量和返航。 | [系统与任务](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:79)；[固定 VM 内存](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:175)；[联合决策](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:200) |
| 9 | **Energy-Aware Multi-UAV Collaboration for Data Collection and Trajectory Planning With MADDPG，TNSM 2026** | 多 UAV 收集静态用户的有限数据；执行动作前检查动作能量与下一位置返航能量，不足便中止动作并返航。 | **低到中等威胁。** 一步返航能量检查已经存在，不能称为新的安全机制；该文没有服务迁移、替补接管或递归可行性证明。 | [数据收集对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:104)；[返航检查](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:216)；[决策变量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:292) |
| 10 | **Trajectory and Resource Allocation for UAV Replacement to Provide Uninterrupted Service，TCOM 2023** | 低电量 UAV 返回充电站、满电 UAV 前来接替；联合双方轨迹和面向用户的 A2G 下行带宽，维持通信吞吐。 | **场景高威胁、精确问题低威胁。** UAV 轮换、端点和固定交接周期已被完整建模；连续性指覆盖和吞吐，不含应用状态。 | [替换过程](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:56)；[能量与端点](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:134)；[联合轨迹与带宽](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:360) |
| 11 | **Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks，TMC 2026** | 按车辆预测联合服务 UAV 选择与轨迹；迁移任务及固定大小的服务配置文件，以长期平均迁移成本约束时延。 | **低到中等威胁。** 在线多 UAV 服务迁移和轨迹控制已存在；对象不是运行内存状态，无请求积压、迁移中处理、物理电池和返航。 | [迁移对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:60)；[优化问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:152)；[能量边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:498) |
| 12 | **Live Migration of Video Analytics Applications in Edge Computing，TMC 2024** | 将视频应用状态分为 permanent、crucial 和 ephemeral；目的端预热和同步期间源端继续处理，最后同步最新关键状态并停止源端。 | **高威胁。** 它已覆盖“处理后更新必要状态”和迁移期间持续服务；但关键状态是可覆盖的固定长度滑动窗口。本文不能假定多处理一个请求就永久增加一份待传状态。 | [三类状态](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:111)；[源端继续处理](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:166)；[处理后更新状态](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:178)；[有限窗口覆盖](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:216) |
| 13 | **Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing，TMC 2026** | 单 UAV 访问任务点，能量不足时回基站换电；联合路径、速度、卸载、资源购买和换电，满足总任务期限。 | **中等威胁。** 同一电池支付飞行、悬停、计算和卸载，并受硬时限约束的模型已经存在；但没有替补 UAV 或有状态服务交接。 | [场景](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:37)；[电池与期限](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:136)；[联合决策](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:228) |
| 14 | **Design, Modeling, and Implementation of Robust Migration of Stateful Edge Microservices，TNSM 2024** | PAM 建模内存量、脏页迭代、checkpoint/restore 处理开销和带宽；COAT 保持容器与 TCP/套接字状态。 | **中等威胁。** 完整运行态、连接和停机/总时长上界均已研究。“Processing-Aware”指迁移工具的处理开销，不是请求完成量；UAV 是客户端而非返航计算节点。 | [状态对象](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:49)；[脏页模型](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:59)；[配置公式](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:526) |
| 15 | **MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge，TNSM 2025** | 在固定边缘主机间选择 cold/pre-copy/iterative pre-copy、带宽和迭代次数，以总迁移时长或停机上限为约束。 | **中等威胁。** 状态迁移策略与资源配置已有原型；AAV 是客户端或视频源，状态大小和脏页率由 profiler 给定，没有请求队列、电池或返航。 | [运行态迁移](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:53)；[状态标定](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:103)；[编排问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:111) |
| 16 | **Efficient Live Migration of Edge Services Leveraging Container Layered Storage，TMC 2019** | 预传基础层和基础内存，源端继续运行并迭代传脏内存，最后传可写层、元数据和最终内存差分。 | **低到中等威胁。** 镜像预置、容器分层和预拷贝都是可继承机制；工作负载会影响脏内存，但请求完成量不是控制变量，也没有电池和返航。 | [完整迁移流程](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:221)；[最终停止](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:232)；[状态增长边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:425) |
| 17 | **KubeSPT: Stateful Pod Teleportation for Service Resilience With Live Migration，TSC 2025** | 在 Kubernetes 中迁移 pod 的网络、内存和上下文状态；迭代检查点后优先恢复热页，其余页面延迟恢复。 | **中等威胁。** 完整 pod/网络状态和低停机系统基线已经存在；没有用户任务队列、能量或返航，且节点关停预测没有形成硬期限可行域。 | [对象与触发](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:11)；[预拷贝与恢复](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:162)；[关停时间](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:302) |
| 18 | **Multi-Cell Mobile Edge Computing: Joint Service Migration and Resource Allocation，TWC 2021** | 用户切换 BS 时迁移含 profile 和 application 的 VM 服务环境，联合 VM 放置、关联和无线 RB；迁移使用固定成本且时间被忽略。 | **低威胁。** 服务迁移与无线/计算资源联合优化并非创新；但没有真实迁移过程、应用状态生成、队列、期限、能量和返航。 | [服务环境与假设](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:45)；[基本问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:82)；[RB 扩展](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:366) |
| 19 | **Mobility-Aware Seamless Service Migration and Resource Allocation in Multi-Edge IoV Systems，TMC 2025** | 服务实例在语义上包含 runtime data 和 user context，联合选择迁移目的地和 CPU；模型把服务数据量作为外生输入，并在迁移后才处理任务。 | **中等威胁。** 不能声称首次迁移运行数据或用户上下文；剩余差异是状态的内生生成、并发同步、一致切换、硬交接窗口和返航。 | [状态语义](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:13)；[外生迁移量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:62)；[迁移后处理](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:72) |
| 20 | **Service Migration Strategies Based on Partially Observable and Multi-Objective Optimization，TMC 2026** | 在部分可观测环境中选择目的 MEC server，以时延和迁移、传输、计算能耗为多目标；迁移量是外生 service data。 | **低威胁。** 部分可观测、多目标和迁移能耗均非创新；文中的 hidden state 是服务器负载等环境状态，不是应用运行状态，能量也不是电池硬约束。 | [迁移与任务时序](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:40)；[能量模型](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:42)；[环境隐状态](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:146) |
| 21 | **Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC，TWC 2024** | 在真实任务缓存队列上联合迁移/任务重路由、卸载、CPU 和带宽，并以 Lyapunov 方法满足长期平均能耗约束；迁移对象是固定大小应用。 | **中高威胁。** 队列—迁移—资源—能耗—在线控制已被系统覆盖。本文仅能主张处理动作还会改变后续必须迁移的状态，并与硬返航完成条件耦合。 | [任务队列](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:89)；[固定应用量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:169)；[变量与约束](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:235) |
| 22 | **Joint Optimization of Trajectory, Offloading, Caching, and Migration for UAV-Assisted MEC，TMC 2025** | 联合 UAV 轨迹、关联、卸载、计算、任务迁移、缓存和 A2A 带宽；缓存的是未处理任务，迁移对象是固定输入与 CPU 周期的任务。 | **中等威胁。** 真实待处理任务集合、A2A 资源和 UAV 联合控制已有先例；但不是运行状态交接，低电量退出仍留作未来工作。 | [对象与互斥动作](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:108)；[队列与成本](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:207)；[低电量边界](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:1012) |
| 23 | **Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks，TSC 2025** | 根据任务执行进度迁移剩余输入和部分结果，处理进度会内生改变迁移对象，并考虑任务软/硬期限。 | **高威胁。** 它直接覆盖“处理进度改变迁移工作量”。本文必须限定为跨请求持久服务状态，而不是单个未完成任务的剩余输入、检查点或部分输出。该文没有迁移中源端处理、电池和返航。 | [迁移触发](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:174)；[剩余输入与部分结果](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:158)；[问题与变量](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:194) |
| 24 | **Joint Content Caching, Service Placement, and Task Offloading in UAV-Enabled Mobile Edge Computing Networks，JSAC 2025** | 联合静态内容缓存、应用/库/数据库的服务放置和任务卸载；没有运行状态迁移。 | **低威胁。** 静态服务部署与运行状态交接必须严格区分；该文没有请求队列、飞行电池或返航。 | [系统与请求](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:35)；[时延与能耗](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:97)；[联合问题](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:169) |
| 25 | **Serv-HU: Service Hand-off for UAV-as-a-Service，TSC 2025** | 主服务商选择其他 UAV 服务商承担未覆盖的地理区域，并联合定价；飞行能耗进入成本。 | **核心问题低威胁、术语高威胁。** “UAV service hand-off” 已有明确用法，但交接对象是区域服务责任，不是应用运行状态和唯一更新权。 | [问题场景](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:51)；[能耗用途](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:293)；[结论](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:680) |

### 3.2 全文证据带来的关键区分

25 篇论文已经覆盖了本构想的大多数单项机制，但它们所说的“状态”或“迁移数据”并不是同一种对象。

| 已有建模方式 | 代表论文 | 与请求处理的关系 | 为什么不能直接当作本文的未同步状态 |
| --- | --- | --- | --- |
| 内存、脏页和容器可写层 | PAM、MOSE、CORMO-RAN、Layered Storage、KubeSPT、STEP | 运行负载会改变内存，但模型使用给定或标定的内存量、脏页率或脏页集合 | 同一页可以反复覆盖，请求完成量不是联合控制变量，未必随完成请求数持续增加 |
| 外部输入回放 | ReSync；Video Analytics 的帧回放部分 | 由到达源端的输入产生，在目的端重新执行 | 增量由外部输入到达决定，不以源端已经完成并确认多少请求为条件 |
| 可选历史上下文 | AIGC context migration | 完成交互会形成 prompt 和输出上下文 | 控制器可以少迁并接受准确率下降，不要求所有历史无损继承 |
| 可覆盖的应用关键状态 | Video Analytics | 每帧处理后更新目标跟踪状态 | 状态保存在有限滑动窗口中，新状态会覆盖旧状态，不能假设线性累积 |
| 单个任务的执行中间量 | CTMiG | 执行进度决定剩余输入和部分结果 | 这是一次任务的可恢复执行状态，不是后续多个请求共同依赖的持久服务状态 |
| 固定应用、VM 或服务数据量 | OSHM、TOM、OASTR、SR-CL、Multi-Cell MEC | 作为外生参数或固定迁移成本 | 处理动作不会改变后续必须迁移的数据量 |

因此，本文不能再笼统声称“已有工作没有考虑运行中新增状态”或“首次让处理量影响迁移量”。可以继续检验的对象必须更窄：**源 UAV 实际完成并确认一个请求后，会形成可序列化、可去重、带版本且不可丢弃的跨请求服务状态；替补 UAV 若未获得这些更新，后续请求的处理结果或已确认副作用就会错误。** 这一定义排除了固定 VM 内存、一般脏页、外部输入回放、可舍弃上下文、有限滑动窗口以及单个任务的剩余输入或部分结果。

### 3.3 经全部全文核验后的判断

最直接的已有工作已经给出低电量替换、有状态检查点 A2A 传输、替补恢复和源 UAV 返站的完整架构；高水平期刊又分别覆盖 UAV 替换与持续覆盖、换电和任务期限、一步返航能量检查、迁移期间持续服务、状态追平、应用辅助状态同步、任务执行进度相关的迁移量、真实任务队列、迁移/重路由、CPU/无线资源、长期能耗以及有状态微服务编排。任何把这些单项机制重新组合后称为“首次”的表述都站不住。

在这 25 篇已核验全文中，尚未发现工作同时研究以下关系：源 UAV 在替补到达后仍可决定完成多少真实请求；已经完成并确认的请求产生不可丢弃、跨请求依赖的服务状态；请求处理既减少等待请求，又增加交接前必须同步的状态；处理、A2A 状态传输和返航使用同一块有限电池；控制器还要选择停止处理与切换时刻，并保证每次在线动作后仍能在最晚开始返航时刻之前完成必要状态载入、版本确认、连接重定向和唯一更新权切换。

因此，本构想暂时可以继续，但还不能据此断言它具备 TMC 级创新。眼下最需要解决的不是选 DRL 还是 MPC，而是找到真实应用，证明上述跨请求状态确实存在，并排除固定脏页率、输入回放、有限窗口、状态合并和单任务检查点这些更简单的解释。

## 4. 按研究方向归纳后的精确边界

| 文献方向与代表工作 | 已经解决的问题 | 与本文研究问题的区别 |
| --- | --- | --- |
| 电池触发的 UAV 有状态微服务替换：[Frejo-Martín et al., ISCC 2025](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:1) | 低电量触发替补、镜像预置、状态检查点、A2A 最终传输、替补恢复和源 UAV 返回补能站。 | 采用固定交接流程，没有请求处理—新增状态耦合、资源控制、最晚开始返航时刻和完整交接条件。 |
| 电量感知 UAV 微服务迁移：[García-Gil et al., Internet of Things 2025](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:3) | 根据请求负载和剩余电量调整微服务放置，并预留飞往充电站所需电量。 | 未迁移运行状态，也没有源—替补之间的一次交接过程。 |
| 带期限与能量预算的在线交接：[Sharghivand et al., TSC 2023](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:1) | 在网络排队、用户期限和逐 BS 传输能量预算下为固定大小的 VM/容器差分在线选择路径。 | 迁移量外生给定，不含源端处理、运行中新增状态、UAV 返航和一致切换。 |
| 复合有状态/无状态边缘应用编排：[Adeppady et al., TNSM 2026](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:1) | 联合微服务放置、迁移、CPU/RB 和版本选择，以响应时延和停机为约束，并在 Kubernetes 上验证。 | UAV 是用户而非即将返航的计算节点；状态由内存和给定脏页率描述，没有请求—状态—电量的时隙演化。 |
| UAV 服务商之间的区域接力：[Roy et al., TSC 2025](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:1) | 跨服务商补足未覆盖区域，并优化服务商选择和价格。 | “交接”对象是区域服务责任，不是运行状态和写入权。 |
| UAV 替换与持续覆盖：[Gupta et al., TCOM](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:1) | 低电量 UAV 返回充电站，满电 UAV 接替；联合轨迹、带宽与吞吐率维持覆盖连续性。 | 连续性是覆盖/吞吐率，不包含运行时应用状态。 |
| UAV 换电与任务卸载：[Ye et al., TMC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:1) | 联合飞行速度、任务卸载和换电站访问。 | 没有源—替补之间的有状态服务交接。 |
| UAV 在线服务迁移：[Feng et al., TMC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:1) | 联合多 UAV 轨迹、服务迁移、车辆预测和在线资源控制。 | 没有电量决定的最晚开始返航时刻，也没有刻画处理动作如何增加未同步状态量。 |
| 有状态 UAV 服务迁移：[TOM, TSC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:1) | 联合 UAV 轨迹、计算卸载和有状态服务迁移，支持并行迁移。 | 迁移工作量主要由预先给定的 VM 内存状态决定，不会随本交接窗口内的任务处理量变化，也没有同时考虑状态同步和返航的完成条件。 |
| 应用辅助在线迁移：[Rong et al., TMC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:1) | 将状态拆成 warm-up、sync、replay 三类；源端在预热与同步期间继续处理，每帧后更新关键状态。 | 固定服务器不需返航；关键状态是可覆盖的有限窗口。该文说明“处理更新状态”本身不是 gap，必须进一步限定状态的跨请求持久性和不可丢弃性。 |
| 状态迁移系统：[PAM, TNSM](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:1)、[MOSE, TNSM](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:1)、[分层存储迁移，TMC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:3)、[ReSync, TMC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:1) | 建模或实现脏页、容器可写层、输入回放、带宽、迁移时长、停机、连接保持和迁移—切换协调。 | 迁移工作量由观测或标定的内存/脏页变化、可写层或外部输入回放表示，请求完成量不是联合控制变量；固定边缘主机也不需要返航。 |
| 状态保持迁移与节能关停：[CORMO-RAN, TMC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:3) | 联合优化有状态 xApp 迁移、服务器开关和集群能耗，并用测试床标定状态大小、脏页率、迁移时延和功耗。 | 固定服务器关停是节能动作；不存在物理返航和最晚开始返航时刻，也不控制源端处理量及其新增状态。 |
| 随运行累积的上下文迁移：[Wang et al., TSC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:1) | 根据新鲜度和相关性决定是否迁移以及迁移多少历史上下文，联合优化准确率、时延和迁移成本。 | 上下文可以按价值舍弃并以精度损失计价；本文要求所有影响后续结果的已确认状态完整交接。 |
| 固定边缘系统的服务迁移与资源优化：[Liang et al., TWC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:1)、[Chen et al., TMC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:1)、[Hou et al., TMC](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:1) | 已覆盖迁移—无线切换—计算/无线资源联合分配、包含运行数据和用户上下文的外生迁移量，以及部分可观测条件下的时延—能耗多目标迁移。 | 迁移量或迁移代价外生给定，源 MEC 服务器不会因电量降低而返航。 |
| 任务队列、迁移/重路由与在线资源控制：[OASTR, TWC 2024](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:1) | 在真实任务队列上联合迁移/重路由、卸载、CPU、带宽和长期平均能耗，并给出 Lyapunov 性能与稳定性结果。 | 迁移对象是固定大小应用。处理只改变任务队列和能耗，不增加后续必须迁移的服务状态；固定边缘服务器也没有物理返航。 |
| 处理进度相关的 UAV 任务迁移：[CTMiG, TSC 2025](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:1) | 根据任务执行进度迁移剩余输入和部分结果，并考虑任务软/硬期限。 | 它已经覆盖“处理进度改变迁移工作量”。本文只能研究后续多个请求共同依赖的持久服务状态，不能把单任务的可恢复执行中间量改名后重复建模。 |
| 动作前返航能量检查：[Mei et al., TNSM](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:1) | 动作执行前检查动作能量和从下一位置返航的能量，能量不足时中止任务并返航。 | 这是一步模型检查和环境中止规则，不是递归可行性或鲁棒安全定理；也不涉及替补接管和有状态交接。 |

在当前 25 篇已经取得并逐篇核验的全文中，尚未发现一项工作同时满足以下六点。这个结论只针对当前证据集，不应写成对所有文献的绝对“首次”判断。

1. 源计算节点是必须在给定时刻开始返航的 UAV，替补 UAV、到达时刻和返航路线已经确定；
2. 替补到达后，源 UAV 在状态同步期间仍可处理请求，实际完成并确认的请求会产生可序列化、可去重、带版本且不可丢弃的跨请求服务状态，而不是预先给定的容器大小、一般脏页、外部输入回放、可舍弃上下文、有限滑动窗口或单任务部分结果；
3. 等待请求量、未同步状态量和源 UAV 剩余电量分别记录并随 CPU、A2A 传输动作演化；
4. 控制器联合决定继续处理多少请求、传输多少状态以及何时停止源端处理；
5. 交接完成不仅要求状态字节传完，还包括语义所需状态的载入、版本确认、连接重定向和唯一更新权切换；
6. 每次在线决策后，系统仍存在一组后续动作，能够在最晚开始返航时刻前完成上述过程，并使源 UAV 保有返航所需能量和安全余量。

因此，本文剩下的研究对象不是一般的 UAV 替换、有状态迁移、任务进度相关迁移量、期限—能量交接或微服务资源编排，而是：**源 UAV 已完成并确认的请求既减少等待请求，又增加替补 UAV 必须无损继承的跨请求服务状态；处理和状态传输共享有限机载电量，交接后还必须满足返航要求。控制器需要在最晚开始返航时刻前维持整个交接过程的可完成性。**

## 5. 问题的基本模型

### 5.1 时隙内事件顺序与状态演化

令 $t=0$ 表示替补 UAV 到达并建立 A2A 链路的时刻。此时测得等待请求量 $Q[0]$、基础检查点之后仍未传出的状态量 $G[0]$ 和源 UAV 的剩余电量 $E[0]$。此后，在每个时隙 $t$ 开始时，控制器观察 $Q[t]$、$G[t]$ 和 $E[t]$。本时隙新到达的请求量 $A[t]$ 可观测后，控制器决定实际完成并确认的请求量 $\mu[t]$，以及通过 A2A 链路传输的状态量 $s[t]$。本时隙完成并确认的请求在时隙结束时产生新的跨请求必要状态 $W[t]$，该部分状态从下一时隙开始传输。

按照这一事件顺序，等待请求量更新为

$$
Q[t+1]=Q[t]+A[t]-\mu[t],
$$

一般情况下，状态更新还可能包含覆盖、合并或压缩，可以写成

$$
G[t+1]=\Phi\!\left(G[t],s[t],W[t]\right).
$$

本文首先限定一类较窄的应用：每个已确认请求形成带版本的增量记录，记录在替补确认前不能删除，也不会被后续记录覆盖。在这个可追加增量的特例中，上式化为

$$
G[t+1]=[G[t]-s[t]]^++W[t],
$$

其中 $[x]^+=\max\{x,0\}$。如果候选应用会合并、覆盖或压缩状态，就必须标定并使用相应的 $\Phi$，不能继续套用加性递推和后面的线性可行区间。源 UAV 的剩余电量更新为

$$
E[t+1]=E[t]-E^{\mathrm{cpu}}(\mu[t])-E^{\mathrm{A2A}}(s[t])-E^{\mathrm{hov}}[t].
$$

式中，$E^{\mathrm{cpu}}(\mu[t])$、$E^{\mathrm{A2A}}(s[t])$ 和 $E^{\mathrm{hov}}[t]$ 分别表示机载处理器（CPU）执行请求、A2A 状态传输和 UAV 维持服务位置所消耗的能量。应用标定不需要假设 $W[t]$ 与处理量严格线性，但必须在声明的工作负载范围内给出保守上界，例如

$$
0\le W[t]\le \overline W^{\mathrm{bg}}[t]+\overline\eta[t]\mu[t].
$$

其中，$\overline W^{\mathrm{bg}}[t]$ 是与当前请求处理无关的后台状态更新上界，$\overline\eta[t]$ 是单位已完成请求所产生的必要状态量上界。提高 $\mu[t]$ 会减少下一时隙的等待请求，却可能增加未同步状态量，并降低剩余电量。这个上界必须针对“已经完成并向用户确认的请求”标定，并验证去重、幂等和版本顺序；如果 $W[t]$ 只由外部输入到达量决定，处理决策便不会改变后续状态传输量。如果状态只是单个未完成任务的剩余输入或部分输出，问题已经落入进度相关的任务迁移。如果应用允许按信息价值舍弃状态，或新状态会覆盖固定窗口中的旧状态，线性累积关系同样不成立。

### 5.2 停止源端处理时的交接完成条件

令 $c$ 表示源 UAV 停止处理新请求并执行最后一次状态传输的时隙。为了使交接在该时隙结束时完成，需要同时满足以下条件。

源 UAV 停止处理后，尚未传出的运行状态和固定交接元数据必须在该时隙内传完：

$$
G[c]+D^{\mathrm{meta}}\le s^{\mathrm{final}}[c],
$$

其中，$D^{\mathrm{meta}}$ 表示服务控制权、版本号和连接恢复等固定元数据量，$s^{\mathrm{final}}[c]$ 表示停止时隙内可靠可传输的状态量。字节传完还不等于交接完成。令 $T^{\mathrm{latest}}_{\mathrm{ret}}$ 表示最晚开始返航时刻，并分别用 $T_c$、$T^{\mathrm{stop}}_c$、$T^{\mathrm{tx}}_c$、$T^{\mathrm{restore}}_c$、$T^{\mathrm{verify}}_c$ 和 $T^{\mathrm{redir}}_c$ 表示停止时隙的开始时刻，以及停止源端、最终传输、状态载入、版本确认和连接重定向所需时间，则还需要

$$
T_c+T^{\mathrm{stop}}_c+T^{\mathrm{tx}}_c+T^{\mathrm{restore}}_c
+T^{\mathrm{verify}}_c+T^{\mathrm{redir}}_c
\le T^{\mathrm{latest}}_{\mathrm{ret}}.
$$

只有影响后续处理语义的状态已经可用、版本检查通过且唯一更新权完成切换，才视为完成。延迟恢复可以用于非关键页面，但不能把语义所需状态留到切换后再加载而不计入完成时间。该时隙不再处理新请求，因此新到达的请求仍需留在等待队列中：

$$
Q[c]+\overline A[c]\le Q^{\max},
$$

其中，$\overline A[c]$ 是停止时隙内新到达请求量的上界，$Q^{\max}$ 是等待队列容量。完成最后一次状态传输、状态载入和版本确认后，源 UAV 的剩余电量必须覆盖返航所需能量及安全余量：

$$
E[c+1]\ge E^{\mathrm{ret}}(c+1)+E^{\mathrm{res}}.
$$

这里，$E^{\mathrm{ret}}(c+1)$ 表示源 UAV 从交接位置返回补能站所需的保守能量估计，$E^{\mathrm{res}}$ 表示用于覆盖建模误差或执行中止动作的安全余量。最后一次状态传输使用的 A2A 带宽、两架 UAV 的能耗以及固定协议时长都必须计入模型，不能把它视为不消耗资源的瞬时动作。

### 5.3 交接可行条件及其含义

在单服务、固定停止时隙、可追加状态增量和线性保守上界下，可以把一个鲁棒充分可行条件概括为三个累计请求量：

- $M_{\mathrm{req}}(c)$：为了使交接窗口内的等待请求不超过队列容量，源 UAV 至少需要完成的累计请求量；
- $M_{\mathrm{sync}}(c)$：在可用 A2A 容量扣除初始未同步状态、后台更新和固定元数据后，状态传输能力所允许的最大累计请求量；
- $M_{\mathrm{eng}}(c)$：在支付状态传输能耗并保留返航所需能量后，电量预算所允许的最大累计请求量。

令 $M(c)$ 表示停止时隙 $c$ 之前源 UAV 累计完成的请求量。满足保守模型的 $M(c)$ 必须位于以下区间：

$$
M_{\mathrm{req}}(c)
\le M(c) \le
\min\left\{M_{\mathrm{sync}}(c),M_{\mathrm{eng}}(c)\right\}.
$$

因此，候选停止时隙至少要满足 $M_{\mathrm{req}}(c)\le\min\{M_{\mathrm{sync}}(c),M_{\mathrm{eng}}(c)\}$，上述区间才非空。请求负载增加会提高左端的最低处理量；单位请求产生的状态量、初始未同步状态或返航能耗增加会降低右端的保守上限；可靠 A2A 容量、剩余电量或可用交接时间增加则会提高该上限。基于这一关系，可以进一步推导鲁棒充分可行区域随关键参数的单调变化，并得到声明模型下继续提高处理速率时不能超过的保守界。只有与完整离线模型逐实例比较后，才能判断这个界距离真实最大允许处理量有多远。

## 6. 求解思路

可以采用面向交接完成条件的鲁棒模型预测控制。为保持与后续论文表述一致，下文暂称其为终端可行性感知鲁棒模型预测控制（terminal-feasibility-aware robust model predictive control，TF-RMPC）。这里的“终端可行”具体指：从当前时隙出发，仍存在一组后续 CPU 与 A2A 资源动作，能够在既定的源端停止处理时隙满足第 5.2 节的全部交接完成条件。OSHM 已经会为固定迁移数据量检查路径的累计时间和 BS 能量预算，OASTR 已经在任务队列上联合迁移/重路由、CPU、带宽与长期能耗；本文只有在“当前处理动作还会改变未来必须传输的跨请求状态，并且交接后仍要满足源 UAV 返航条件”这一点上才与它们不同。MPC、二次规划和停止时隙枚举只是计算动作序列的手段，不构成独立创新。

1. **应用标定。** 用相互独立的拟合、校准和测试轨迹得到请求到达上界、已确认请求量—新增必要状态上界、状态覆盖/合并规则、可靠 A2A 传输下界、迁移对 CPU/I/O 的干扰，以及处理、传输、悬停、停止、恢复和连接切换的时间与能耗上界；所有参数在最终测试前固定。
2. **交接准入。** 对有限个候选停止时隙分别求解直至交接完成的队列、状态和能量计划。只有至少一个停止时隙能够满足全部交接条件时，系统才启动本次交接；选定后固定该时隙，避免滚动控制通过不断延后停止服务来掩盖资源不足。
3. **滚动控制。** 每个时隙根据实际的 $Q[t]$、$G[t]$、$E[t]$ 和信道状态重新求解 CPU 与 A2A 动作，只执行当前时隙的动作。其余计划用于证明该动作执行后仍可按时完成交接，下一时隙再根据新观测重新计算。
4. **超出建模范围时的处理。** 若请求到达、状态生成、信道或能耗超出预先确定的建模边界，控制器不再沿用模型内保证，而是触发预先规定的停止处理、直接返航或上层恢复流程。协议故障和软件错误应单独记录，不能通过目标函数中的惩罚项吸收。

比较对象应围绕精确差异设计，而不是只比较 PPO、贪心或随机策略。下列工作有的适合作为可复现算法基线，有的只能作为结构消融或系统实现参照，实验中应明确区分：

1. **固定 UAV 替换与交接流程。** 继承 UAV Replacement 的平台轮换周期和 *Live Migration of Stateful Microservices* 的镜像预置、最终检查点、替补恢复与源机返站流程，但不联合优化请求处理、状态传输和停止时刻。
2. **现有状态同步机制。** 以 ReSync 的外部输入双队列、Video Analytics 的预热/同步/回放与有限关键状态窗口，以及 PAM/MOSE/KubeSPT 的内存—脏页—恢复机制为实现参照，分别检验输入回放、可覆盖关键状态或标准预拷贝是否已经足以解释结果。
3. **队列和资源控制已保留、状态量仍外生。** 以 OASTR 为主要结构基线，保留真实任务队列、迁移/重路由、CPU、带宽和能耗约束，把迁移量固定为应用大小；再以 SR-CL 的外生运行数据量和 OSHM/STEP 的固定迁移量或脏页率做消融，统一删除 $W[t]$ 对 $\mu[t]$ 的依赖。
4. **单任务进度相关迁移。** 采用 CTMiG 的“剩余输入加部分结果”作为迁移对象，并保留任务期限，用于确认收益不是来自已有的单任务执行进度模型。若该基线已经能表示候选应用，本文的跨请求状态假设便不成立。
5. **返航条件的结构消融。** 分别比较 Energy-Aware 工作的一步返航能量检查、Flight Speed/Battery Swapping 的电池—任务—期限模型，以及删除物理返航条件的版本。CORMO-RAN 只作为固定服务器关停与能耗优化的边界参照，不宜当成可直接公平复现的算法基线。

AIGC 上下文选择更适合作为研究边界；除非候选应用允许舍弃部分状态，否则不能把近似状态延续与要求语义一致的完整交接直接比较。

## 7. 研究问题、方法与预期认识

**研究问题。** 电量触发轮换后，源 UAV 必须在给定时刻开始返航。对具有跨请求持久状态的流式服务，源 UAV 多完成并确认一部分请求，会减少等待请求，同时产生替补 UAV 继续处理后续请求时不能舍弃的新状态，并消耗原本可用于状态传输和返航的机载电量。当前时隙的动作满足局部资源约束，不代表服务仍能在剩余时间内完成交接。

**方法。** 系统预先部署应用镜像和基础检查点，只建模由已完成并确认的请求产生、具有明确版本和去重语义、且替补 UAV 处理后续请求时必须继承的状态。对每个候选停止时隙，控制器计算等待请求量、未同步状态量、停止与最终传输、状态载入与确认、连接重定向以及返航能量能否同时满足要求，再通过滚动优化执行不会破坏后续交接可行性的 CPU 与 A2A 动作。

**预期认识。** 在普通 MEC 中，提高 CPU 处理速率通常可以减少等待请求；在本场景中，更快的处理还可能增加后续状态传输量，并减少可用于返航的电量。因此，源 UAV 在交接窗口内能够安全完成的请求量，不只由计算能力决定，而是位于“避免等待队列溢出所需的最低处理量”和“状态传输及返航能量允许的最高处理量”之间。

可主张的三项贡献是：

1. 一个经真实应用验证的跨请求状态模型，明确源端实际完成并确认请求如何同时减少等待请求、产生替补必须无损继承的持久状态并消耗有限机载电量；它不同于固定容器/脏页模型、外部输入回放、可舍弃上下文、有限滑动窗口和单任务部分结果；
2. 一个统一最低请求处理需求、必要状态完整交接和安全返航要求的鲁棒充分可行域，并在明确的状态代数与不确定性条件下分析其结构、相对完整离线模型的保守程度、滚动执行后的持续可行性以及关键参数的单调影响；
3. 一个实现上述保证的在线控制器，并通过真实状态迁移原型、小规模离线最优解和压力测试量化请求处理性能、安全性与模型保守程度。

不能作为贡献的内容包括：首次提出 UAV service hand-off；首次研究 UAV 替换、UAV 微服务迁移或 UAV 有状态微服务迁移；首次联合 UAV 轨迹、卸载、缓存或迁移；首次使用预拷贝、CRIU、容器分层、A2A 最终检查点、输入回放或延迟恢复；首次在交接中联合考虑期限、网络排队和能量预算；首次区分有状态/无状态微服务并联合放置、迁移、CPU/RB 分配；首次联合任务队列、服务迁移/重路由、CPU、带宽和长期能耗；首次让单任务执行进度改变剩余输入或部分结果；首次研究部分可观测的时延—能耗多目标迁移、运行中形成的上下文、状态迁移与节能关停或动作前返航能量检查；首次使用 MPC/QP/DRL/Lyapunov；以及首次联合计算和迁移。

## 8. 研究假设与验证标准

| 待确认命题 | 必要证据 | 否定结果 |
| --- | --- | --- |
| 已完成请求量可以预测必要的跨请求状态 | 在独立应用轨迹上测量 $\mu[t]$、序列化状态字节、确认时刻和后续请求依赖；与固定脏页、输入回放、有限窗口和单任务部分结果逐一对照 | 状态只是可覆盖窗口或单任务检查点，主要由外部输入决定，或上界宽到使绝大多数交接被拒绝 |
| 状态递推与候选应用一致 | 检查增量是否可追加；若存在覆盖、合并或压缩，标定 $\Phi$ 并比较一般递推与加性近似 | 实际状态大量合并或覆盖，而模型仍用 $[G-s]^++W$ 线性累积 |
| 应用状态接口能够保持语义一致 | 无迁移运行与交接后运行逐输入比较输出、提交顺序、exactly-once 确认、幂等去重、版本顺序，以及当前唯一更新方及其版本 | 任一声明范围内轨迹出现不可解释的状态分叉，或无法界定请求何时算完成并产生必要状态 |
| 交接可行域不会把不可完成的实例误判为可行 | 用具有完整未来信息的小规模穷举或 MILP 离线解，与交接可行条件逐实例比较 | 条件判定可行，但完整模型无法完成交接 |
| 计算产生的新状态会实质改变决策 | 与 OASTR/SR-CL/OSHM 的外生迁移量、STEP/PAM 的内存—脏页模型、ReSync 输入回放、Video 有限窗口和 CTMiG 单任务进度模型做同轨迹配对 | 完整模型与这些去耦或替代模型在现实参数区间内没有可辨别的动作或结果差异 |
| 迁移干扰和完整切换时间已被计入 | 实测检查点、脏页扫描和传输对源端 CPU/I/O 与吞吐的影响，并测量停止、最终传输、载入、版本确认、连接重定向和切换后的 p99 时延 | 干扰会显著改变 $\mu[t]$ 或状态增长，或固定协议时间使原先判定可行的实例超过最晚开始返航时刻 |
| 在线控制优于最直接的已有流程 | 复现“源端停止—最终检查点传输—替补恢复—源机返航”的固定流程，在相同到达、信道和电量轨迹下比较完成请求量、停机、未同步状态和交接后的剩余电量 | 联合控制没有稳定收益，或收益仅来自更宽松的资源配置 |
| 递归交接约束提高安全性，而不只是增加拒绝 | 与局部约束 MPC 和只考虑当前时隙的方法比较完成率、队列溢出、交接结束时的未同步状态量、返航能量余量和拒绝率 | 安全提升只能依靠拒绝几乎所有交接，或在建模边界内仍发生约束违约 |
| 方法能够在线执行 | 测量状态读取、建模、求解、记录和动作下发的完整 p99 时延 | 声明规模下 p99 达到或超过时隙长度 |

只有这些研究假设同时得到支持，才能形成 TMC 级论文所需的问题机制、理论保证和系统证据。单纯在仿真中使 TF-RMPC 的平均目标值优于 PPO 或贪心算法，不足以证明该研究问题具有独立价值。

## 9. 适用风险与终止或转向条件

1. **只剩已有 UAV 替换协议。** 如果研究最终只是实现低电量触发、镜像预置、检查点 A2A 传输、替补恢复和源机返站，而处理量—新增状态关系没有形成新的模型与可验证结论，那么场景和协议已被最直接的已有工作覆盖，应停止以此作为论文主线。
2. **与 ReSync 的重叠。** 如果候选应用只需记录所有到达输入，新增状态量与 CPU 决策无关，那么 ReSync 的外生输入双队列是更自然的模型。此时研究问题应转为能量感知的 ReSync 调度，不能继续强调处理决策会产生未同步状态。
3. **退化为外生迁移量或内存—脏页模型。** 如果 $W[t]$ 可以由窗口开始时确定的容器大小、外生运行数据量或观测/标定的内存和脏页变化充分描述，CPU 决策不会改变后续状态量，问题就接近 OSHM、SR-CL 或 STEP/PAM 一类既有模型。
4. **与 AIGC 上下文迁移的重叠。** 如果候选应用允许丢弃一部分历史状态，并把后果表示为准确率或效用下降，那么研究对象更接近“迁移哪些上下文”的价值选择。此时必须转向状态价值与近似状态延续，不能继续声称研究完整一致的状态交接。
5. **返航条件不改变决策。** 如果源节点不受有限电池约束、停止服务时刻可以任意延后，或返航所需能量相对剩余电量始终可以忽略，问题就退化为固定集群中的状态迁移、节点关停与能耗编排。
6. **应用状态表示不成立。** 如果影响正确性的隐藏状态不能完整序列化，或者窗口内存在覆盖、合并和非确定性副作用，就不能使用加性状态递推。此时必须标定一般更新算子 $\Phi$，或改用应用特定快照/脏页模型；若因此消除“多处理会增加后续必传状态”的关系，核心问题不再成立。
7. **请求处理对交接的影响太弱。** 如果新增状态相对 A2A 容量几乎可以忽略，CPU 选择不会改变交接可行性，那么两者的关系只在数学上存在、在实际系统中并不重要，应停止该主线。
8. **交接完成条件只是标准 MPC 的直接应用。** 如果最终只能证明一般的滚动计划可延续，而无法给出最低请求处理量与最高允许处理量之间的结构、参数单调性或可检验的安全处理上限，论文容易被评价为把常规方法迁移到新场景。
9. **保证依赖不可校准边界。** 如果信道、状态生成或能耗上界无法在独立测试中维持声明覆盖，持续可行性只能成为理想模型结论，不能支撑安全主张。
10. **缺少真实迁移证据。** 如果没有至少一个容器化流式应用、状态接口和可控 A2A 网络原型，论文无法证明所建模的未同步状态真实存在并且能够被在线控制。
11. **退化为有限窗口或单任务执行状态。** 如果候选应用只保留可覆盖的最近窗口，问题更接近 Video Analytics；如果迁移的是单个未完成任务的剩余输入、检查点或部分结果，问题已经被 CTMiG 覆盖。两者都不能支撑本文的跨请求持久状态主张。
12. **处理只改变请求队列和能耗。** 如果处理动作不增加替补必须继承的状态，剩余问题就是 OASTR 已研究的任务队列、迁移/重路由、CPU、带宽和能耗在线控制，不能继续作为本文主线。
13. **迁移干扰或确认语义未闭合。** 检查点与传输会争用 CPU/I/O，并可能同时改变处理吞吐和脏页变化；如果没有测量这种干扰，或不能实现 exactly-once 确认、幂等去重和版本顺序，$\mu[t]\rightarrow W[t]$ 就不是可验证的因果对象。

最优先的验证不是训练控制器，而是选定一个具体应用，确认其状态语义、已完成请求量与新增必要状态量之间的关系，以及这一关系在较短交接窗口或受限 A2A 容量下是否会实际改变可行决策。

## 10. 相关论文阅读清单

下面 25 篇均已完成全文核验，条目中的说明是核验结论，不是后续待读事项。若要先判断构想是否成立，建议按 **1 → 23 → 5 → 12 → 21 → 19 → 4 → 8 → 10 → 13 → 9** 的顺序阅读：先看最直接的 UAV 有状态替换，再依次排除单任务进度相关迁移、外部输入回放、可覆盖应用状态、队列—资源—能耗在线控制、外生运行数据、固定迁移量期限交接、有状态 UAV 迁移、平台替换、换电期限和一步返航检查。正文的一般方法和结论应优先由 TMC、TWC、TCOM、TSC、TNSM 和 JSAC 等高水平期刊支撑；但直接决定创新边界的工作不能只因 venue 较低而排除。

### A. 场景、状态与返航边界

1. **Live Migration of Stateful Microservices in UAV-Assisted Networks for Enhanced Availability，IEEE ISCC，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability/Live_Migration_of_Stateful_Microservices_in_UAV-Assisted_Networks_for_Enhanced_Availability.md:1)
   全文确认了低电量触发、镜像预置、最终检查点 A2A 传输、替补恢复和源机返站流程，但没有数学优化和定量评估。它直接否定“首次在电池轮换中迁移有状态微服务”的宽泛主张。
2. **Microservices Migration: A Pathway to Improved Energy Efficiency in UAV Networks，Internet of Things，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks/Microservices_Migration_A_Pathway_to_Improved_Energy_Efficiency_in_UAV_Networks.md:3)
   全文确认了电量阈值、飞往充电站所需能量、请求负载和微服务重新放置的关系；论文没有运行状态传输、迁移时长和一致性过程。
3. **Efficient Management of Composite Heterogeneous Applications at the Network Edge，TNSM，2026。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md:1)
   全文确认 UAV 只是移动用户、边缘服务器固定、脏页率按微服务版本给定、迁移链路固定为 50 Mbps；STEP 已联合放置、CPU/RB、版本、响应时延和停机约束。
4. **Time-Constrained Service Handoff for Mobile Edge Computing in 5G，TSC，2023。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md:1)
   全文确认了交接窗口、BS 传输队列、固定 VM/容器差分大小、逐 BS 能量预算和标签修正算法。“期限—网络排队—能量预算下的在线交接”已经不是空白。
5. **ReSync: Coordinated Live-Migration for Stateful Containers in Mobile Edge Computing，TMC，2026。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing/ReSync_Coordinated_Live-Migration_for_Stateful_Containers_in_Mobile_Edge_Computing.md:1)
   全文确认了输入回放双队列、同步收敛条件、可切换阶段、晚触发失败和确定性假设；其增量由外部输入到达产生，不由源端请求完成量产生。
6. **CORMO-RAN: Energy Efficiency at the Near-RT RIC via Lossless Migration of O-RAN xApps，TMC，2026（Early Access）。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md:3)
   全文确认了 SM/SDL 两种状态保持方式、状态大小与脏页率标定、迁移时长和功耗、服务器关停条件及可行范围；“有状态迁移—节点关停—能耗优化”已经被系统研究。
7. **Context-Aware AIGC Service Migration in Edge Intelligence Networks via Transformer DRL，TSC，2026。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL/Context-Aware_AIGC_Service_Migration_in_Edge_Intelligence_Networks_via_Transformer_DRL.md:1)
   全文确认历史上下文由 prompt 和生成输出共同形成，迁移窗口数可以选择，少迁的代价表现为准确率下降。它迫使本文把“必须完整继承的必要状态”与“按价值选择的上下文”明确分开。
8. **TOM: Joint Trajectory, Offloading and Migration Optimization in Stateful Service-Oriented UAV-Enabled VEC System，TSC，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System/TOM_Joint_Trajectory_Offloading_and_Migration_Optimization_in_Stateful_Service-Oriented_UAV-Enabled_VEC_System.md:1)
   全文确认了固定 VM 内存量、迁移时长、并行迁移、卸载和轨迹联合决策；dirty page/final sync 只在定性描述中出现，优化模型没有状态动态。
9. **Energy-Aware Multi-UAV Collaboration for Data Collection and Trajectory Planning With MADDPG，TNSM，2026。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md:1)
   全文确认了动作执行前的“动作能量加下一位置返航能量”检查，失败时从当前位置中止并返航；论文没有递归可行性或鲁棒安全证明。
10. **Trajectory and Resource Allocation for UAV Replacement to Provide Uninterrupted Service，TCOM，2023。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service/Trajectory_and_Resource_Allocation_for_UAV_Replacement_to_Provide_Uninterrupted_Service.md:1)
   全文确认了固定替换周期、替补到位、源机返站、双方轨迹和面向用户的 A2G 下行带宽；没有 A2A 状态传输或应用一致性。
11. **Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks，TMC，2026。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks/Prediction-Assisted_Multi-UAV_Online_Service_Migration_and_Trajectory_Control_for_MEC-Empowered_Vehicular_Networks.md:1)
   全文确认迁移对象是任务和固定大小的服务配置文件，采用 Lyapunov/MADDPG 联合 UAV 选择与轨迹；物理能量约束被留作未来工作。
12. **Live Migration of Video Analytics Applications in Edge Computing，TMC，2024。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md:1)
   全文确认永久、关键和易失状态的划分，以及预热、同步和回放接口。关键目标跟踪状态采用固定长度滑动窗口，直接限制了本文加性状态模型的适用范围。
13. **Optimal Flight Speed Scheduling and Battery Swapping in UAV-Enabled Mobile Edge Computing，TMC，2026。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing/Optimal_Flight_Speed_Scheduling_and_Battery_Swapping_in_UAV-Enabled_Mobile_Edge_Computing.md:1)
   全文确认了电池递推、返航换电、飞行速度、卸载和硬总任务期限的联合模型；它没有替补 UAV 或服务状态交接。

### B. 状态迁移机制与系统实现

14. **Design, Modeling, and Implementation of Robust Migration of Stateful Edge Microservices，TNSM，2024。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md:1)
    全文确认了内存/脏页模型、迁移时长与停机上界、连接保持和真实微服务标定；“Processing-Aware”指迁移工具处理开销，不是请求处理量。
15. **MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge，TNSM，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md:1)
    全文确认了 cold/pre-copy/iterative pre-copy、带宽、迭代次数、停机/总时长目标和 AAV/目标跟踪原型；AAV 是客户端或视频源，不是返航的计算节点。
16. **Efficient Live Migration of Edge Services Leveraging Container Layered Storage，TMC，2019。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage/Efficient_Live_Migration_of_Edge_Services_Leveraging_Container_Layered_Storage.md:3)
    全文确认了预传基础层/内存、源端继续运行、迭代同步脏内存、最终暂停和可写层传输；镜像预置、分层迁移和内存差分均属于可继承机制。
17. **KubeSPT: Stateful Pod Teleportation for Service Resilience With Live Migration，TSC，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/sources/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration/KubeSPT_Stateful_Pod_Teleportation_for_Service_Resilience_With_Live_Migration.md:1)
    全文确认了热页、延迟恢复、网络状态和 Kubernetes 操作语义；它是完整 pod 迁移的强系统基线，但没有任务队列、能量或返航。

### C. 服务/任务迁移与资源编排边界

18. **Multi-Cell Mobile Edge Computing: Joint Service Migration and Resource Allocation，TWC，2021。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md:1)
    全文确认了 VM 服务环境、基站切换和无线资源的联合模型；迁移开销是固定成本，迁移/切换时间相对时隙被忽略，适合作为“联合资源优化已成熟、真实状态交接尚未进入模型”的对照。
19. **Mobility-Aware Seamless Service Migration and Resource Allocation in Multi-Edge IoV Systems，TMC，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md:1)
    全文确认 service instance 在语义上包含 runtime data 和 user context；模型把服务数据量作为外生量，任务在迁移后才处理，没有并发同步、一致切换、硬期限和返航。
20. **Service Migration Strategies Based on Partially Observable and Multi-Objective Optimization，TMC，2026。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization/Service_Migration_Strategies_Based_on_Partially_Observable_and_Multi-Objective_Optimization.md:1)
    全文确认了外生迁移量、迁移/传输/计算能耗、环境部分可观测状态和时延—能耗 Pareto 优化；这里的 hidden state 是服务器负载等环境状态，能量也不是有限电池硬约束。
21. **Service Migration or Task Rerouting: A Two-Timescale Online Resource Optimization for MEC，TWC，2024。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC/Service_Migration_or_Task_Rerouting_A_Two-Timescale_Online_Resource_Optimization_for_MEC.md:1)
    全文确认了真实任务缓存队列、迁移/任务重路由、CPU、带宽、长期能耗约束和 Lyapunov 性能界；迁移对象仍是固定大小应用。这是“队列—资源—能耗在线控制”最重要的边界论文。
22. **Joint Optimization of Trajectory, Offloading, Caching, and Migration for UAV-Assisted MEC，TMC，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC.md:1)
    全文确认了真实任务缓存、任务迁移、A2A 带宽、轨迹和卸载联合控制；缓存/迁移对象是未处理任务，不是服务运行状态，低电量退出仍是未来工作。
23. **Joint Task Offloading and Migration Optimization in UAV-Enabled Dynamic MEC Networks，TSC，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks/Joint_Task_Offloading_and_Migration_Optimization_in_UAV-Enabled_Dynamic_MEC_Networks.md:1)
    全文确认任务执行进度会改变需迁移的剩余输入和部分结果，并考虑软/硬期限。它直接否定“首次让处理进度改变迁移工作量”，也是当前最需要先读的机制竞争者之一。
24. **Joint Content Caching, Service Placement, and Task Offloading in UAV-Enabled Mobile Edge Computing Networks，JSAC，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md:1)
    全文确认 service placement 指应用、库和数据库等静态部署，不是运行状态交接；它主要用于术语消歧。
25. **Serv-HU: Service Hand-off for UAV-as-a-Service，TSC，2025。** [本地全文](/C:/Users/labs2/Desktop/Projects/mec-research-wiki/raw/tmp/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md:1)
    全文确认 hand-off 对象是跨服务商的区域覆盖责任，飞行能耗只进入成本和价格；该文主要用于避免把 UAV service hand-off 写成本文首创。

## 11. 研究构想的成立条件

25 篇全文表明，现有研究已经覆盖本场景的大部分组成部分。最直接的 UAV 论文已经给出低电量触发、满电替补、镜像预置、有状态检查点 A2A 传输、替补恢复和源机返站的完整流程；其他工作分别覆盖平台替换与持续通信、返航换电与任务期限、一步返航能量检查、迁移期间持续服务、输入回放追平、应用辅助状态同步、有状态微服务编排、包含运行数据和用户上下文的服务迁移、真实任务队列上的迁移/重路由与资源—能耗控制，以及执行进度相关的剩余输入和部分结果迁移。本文不能把这些机制中的任何一项或它们的简单拼接作为主要创新。

本文能够成立的核心研究问题是：

> 对具有不可丢弃、跨请求持久状态的流式服务，替补 UAV 到达后，源 UAV 多完成并确认一些请求，会减少等待请求，也会产生替补 UAV 处理后续请求时必须继承的新状态。请求处理和状态传输共同消耗源 UAV 的剩余电量，交接完成后还必须留下飞回补能站所需的能量。源 UAV 因而不能处理得太少，否则等待队列可能溢出；也不能处理得太多，否则新增状态无法按时传完，或交接后剩余电量不足以返航。在线控制器需要在最晚开始返航时刻之前，在这两个边界之间选择请求处理量、状态传输量和停止处理时刻，并把状态载入、版本确认、连接重定向和唯一更新权切换纳入完成条件。

这个构想仍然只能**有条件继续**。相近工作已经很多，目前不能断言它具备 TMC 级创新。第一步必须用真实应用证明“已完成并确认的请求会产生不可丢弃、跨请求依赖的状态”，并排除固定脏页、外部输入回放、有限窗口、可舍弃上下文和单任务部分结果等更简单解释。第二步要证明这组状态在现实交接窗口、A2A 容量和机载电量下确实改变处理与停止决策。之后才能讨论鲁棒充分可行域、滚动执行后的持续可行性、与完整离线解相比的保守程度，以及真实迁移原型中的一致性和返航条件。只有这些证据成立，论文才可能达到 TMC 所要求的问题机制、理论结果和系统证据。

如果应用状态只由外部输入到达决定，或可由固定容器大小、外生运行数据量、内存/脏页变化充分描述；如果状态会像视频关键窗口一样被覆盖、像 AIGC 上下文一样按价值舍弃，或本质上只是单个任务的剩余输入和部分结果；如果处理只改变请求队列与能耗，新增状态相对 A2A 容量又可以忽略；或者必须使用过度保守的边界才能避免违约，那么最窄的研究问题也不能成立。此时应停止或调整主线，而不是继续增加 DRL 或其他调度模块。
