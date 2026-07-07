# Scalable UAV Multi-Hop Networking via Multi-Agent Reinforcement Learning With Large Language Models

Yanggang Xu , Jirong Zha , Weijie Hong, Xiangmin Yi , Geng Chen, Jianfeng Zheng, Chen-Chun Hsia , and Xinlei Chen , Member, IEEE

Abstract—In disaster scenarios, establishing robust emergency communication networks is critical, and uncrewed aerial vehicles (UAVs) offer a promising solution to rapidly restore connectivity. However, organizing UAVs to form multi-hop networks in largescale dynamic environments presents significant challenges, including limitations in algorithmic scalability and the vast exploration space required for coordinated decision-making. To address these issues, we propose MRLMN, a novel framework that integrates multi-agent reinforcement learning (MARL) and large language models (LLMs) to jointly optimize UAV agents toward achieving optimal networking performance. The framework incorporates a grouping strategy with reward decomposition to enhance algorithmic scalability and balance decision-making across UAVs. In addition, behavioral constraints are applied to selected key UAVs to improve the robustness of the network. Furthermore, the framework integrates LLM agents, leveraging knowledge distillation to transfer their high-level decision-making capabilities to MARL agents. This enhances both the efficiency of exploration and the overall training process. In the distillation module, a Hungarian algorithm-based matching scheme is applied to align the decision outputs of the LLM and MARL agents and define the distillation loss. Extensive simulation results validate the effectiveness of our approach, demonstrating significant improvements in network performance over the MAPPO baseline and other comparison methods, including enhanced coverage and communication quality.

Index Terms—Multi-agent reinforcement learning, large language model, knowledge distillation, multi-hop UAV network.

## I. INTRODUCTION

N <sup>ATURAL</sup> <sup>disasters</sup> <sup>worldwide</sup> <sup>have</sup> <sup>devastating</sup> <sup>impacts,</sup>not only causing loss of life and infrastructure damage not only causing loss of life and infrastructure damage but also disrupting social and economic systems. In 2024, the United States experienced 27 climate disasters that caused over \$1 billion in damage each, with total losses reaching \$184.8 billion and 568 fatalities reported [1]. Communication infrastructure, including base stations (BSs) and fiber-optic cables, is highly vulnerable to disasters such as floods and earthquakes. Communication failures hinder the delivery of humanitarian aid and disrupt life-saving rescue efforts. These breakdowns intensify the challenges faced by disaster-stricken communities. They highlight the urgent need for resilient, rapidly deployable communication systems to support emergency response and recovery.

Uncrewed Aerial Vehicles (UAVs) have emerged as a promising solution to address the communication challenges posed by disasters, owing to their exceptional mobility and agility [2]. UAVs can serve as mobile relay stations, forming multi-hop networks to provide communication services to distant user equipments (UEs). Furthermore, UAVs, operating in air-to-ground and air-to-air channels with minimal obstructions, are more likely to establish reliable line-of-sight propagation paths, thus ensuring robust communication [3]. By strategically optimizing UAV flight trajectories and positions, the quality of communication channels can be significantly enhanced, thereby improving the overall performance of UAV-assisted network systems.

This paper leverages UAV swarms to establish expansive multi-hop networks by connecting distant, operational fixed BSs in disaster-stricken regions, shown in Fig. 1. In situations where disasters create communication dead zones, multiple UAVs are strategically deployed to serve ground UEs. They form a relay network that bridges isolated areas with available BSs, thereby connecting the local network to the core infrastructure. This configuration not only extends coverage to remote areas where conventional communication is infeasible, but also enhances network reliability through the creation of multiple routing paths. In particular, UAV mobility and multi-hop pathways provide the flexibility needed to adapt to the dynamic movement of ground UEs, enabling adaptive routing. In a multi-hop network, precise coordination among multiple UAVs is essential. This necessitates sophisticated trajectory planning and deployment strategies to ensure that each UAV maintains optimal positioning for uninterrupted connectivity.

![](images/5c952a8ede89667ab8a6c00c405600dc0c1687bafd0981b0f7d9f6a129e9c430.jpg)  
Fig. 1. In disaster scenarios, UAVs can rapidly establish temporary multi-hop wireless networks in communication dead zone, thereby restoring connectivity for UEs.

With the rapid advancement of UAV and Internet of Things technologies, extensive research has been devoted to UAV-based communication and networking tasks. Numerous studies have sought to optimize the association and coordination between UAVs and UEs through refined transmission strategies [4], efficient resource management [5], and strategic UAV deployment [6]. Several studies have further explored the applications of UAVs in wireless sensor networks [7], data offloading, and edge computing [8]. Reinforcement learning (RL) techniques, owing to their exceptional decision-making and planning capabilities, have been applied to optimize UAV trajectory planning in dynamic and uncertain environments [8], [9]. These methods aim to improve overall communication performance while addressing the challenges imposed by various operational constraints and environmental uncertainties. However, existing studies primarily focus on the planning of a limited number of UAVs, without addressing the complex coordination required for large-scale multi-UAV systems. In large-scale environments, communication constraints often require the use of multi-hop networks, where connectivity is highly dynamic and unstable. Coordinating UAV swarm within such networks remains a significant challenge.

Optimizing dynamic multi-hop networks formed by UAVs presents several key challenges:

1) One major difficulty lies in the joint optimization and balancing of UAV-specific strategies, which demands a scalable algorithm capable of managing complex coordination. Within the swarm, UAVs must coordinate their roles to collectively establish and maintain a stable network topology. Each UAV’s decision-making not only dictates its own relay selection and communication scheduling, but also influences the strategies of other UAVs within the network. An imbalance in these roles may lead to coverage gaps or network disconnections, triggering cascading effects that undermine network stability and efficiency. The interdependence of these strategic decisions further amplifies the complexity of coordination, requiring UAVs to continuously adjust their behaviors to achieve a globally balanced and optimized network structure.

2) The second challenge arises from the spatial complexity and dynamic nature of multi-hop UAV networks, which significantly expand the exploration space and complicate the training process. In large-scale disaster scenarios, the considerable distances between available BSs and scattered UEs result in an overwhelming number of possible UAV deployment strategies, making it difficult to determine an optimal configuration. This challenge is further exacerbated by the continuously changing network topology and fluctuating channel conditions. Furthermore, the stochastic distribution and unpredictable mobility of UEs introduce further uncertainty into network planning. These spatial and temporal complexities not only increase the difficulty of optimizing UAV placement and routing, but also require continuous adaptation to maintain stable and efficient communication.

These challenges highlight the need for scalable algorithms that enable joint optimization of multi-agent strategies to maintain equilibrium while effectively managing the extensive exploration space. Developing such algorithms is essential for achieving efficient coordination and adaptive decision-making in complex, dynamic multi-hop network environments.

To address the aforementioned challenges, this paper investigates the application of UAV swarms in multi-hop networking for disaster emergency scenarios, focusing on optimizing UAV trajectories to maximize both communication coverage and quality under connectivity constraints. To tackle this problem, we propose a novel multi-agent reinforcement learning (MARL) framework, referred to as MRLMN (Multi-agent Reinforcement learning with Large language model in Multi-hop Networking). The key contributions of this paper are summarized as follows:

This paper formulates the UAV-enabled multi-hop networking task as a multi-objective optimization problem aimed at maximizing network coverage and communication quality while satisfying connectivity constraints. This problem is modeled as a stochastic game to capture the dynamic interactions among UAVs and between UAVs and the environment, explicitly considering collaboration and coordination challenges in large-scale, multi-UAV, and multi-hop network scenarios.

This paper proposes a task-oriented agent grouping strategy and an information aggregation mechanism within a MARL framework. A reward decomposition model is designed based on the grouping strategy to facilitate coordinated decision-making, mitigate non-stationarity, and enhance scalability for large UAV swarms. Behavioral constraints are further applied to critical UAV groups to improve network robustness and prevent detrimental topology disruptions.

This paper designs a knowledge distillation framework that combines Large Language Models (LLMs) with MARL for UAV networking. In our framework, the LLM serves as an offline advisor that provides high-level strategic insights, which are distilled into the MARL agents to guide policy learning, without being deployed for real-time UAV control. LLM outputs are aligned with MARL actions through a per-agent decision matching scheme. The knowledge is then transferred via a tailored distillation loss, facilitating more efficient policy exploration, addressing the coldstart problem, and enhancing the convergence of MARL training.

\- Extensive simulations are conducted to evaluate the proposed approach across different environment scales, UAV swarm sizes, and baseline comparisons. The results demonstrate that MRLMN consistently outperforms existing methods in terms of network coverage, communication quality, and robustness, validating the effectiveness of the proposed mechanisms.

The remainder of this paper is structured as follows. Section II reviews related work on UAV-based networking. Section III formulates the problem and introduces the system model. Section IV presents the proposed MRLMN framework. Section V describes the simulation setup and evaluates performance by comparing the proposed method with other approaches. Finally, Section VI concludes the paper and outlines potential directions for future research.

## II. RELATED WORK

This section reviews existing research relevant to UAVassisted networking, covering optimization-based, RL-based, and LLM-assisted methods. The discussion summarizes key developments in each category, identifies their limitations, and emphasizes the advantages of the proposed approach relative to prior work.

## A. Optimization-Based Methods

In the problem of employing UAVs to provide communication networks for UEs, designing trajectory and resource planning algorithms is complex due to the coupling of various factors. Several studies propose algorithms based on optimization theory to tackle this intricate problem [10], [11]. The majority of these works model the trajectory optimization problem for UAVs within the context of combinatorial optimization problems such as the Traveling Salesman Problem (TSP) and Vehicle Routing Problem (VRP). Building on these well-established frameworks, researchers have developed specialized algorithms to effectively address the optimization challenges present in different UAVassisted networking scenarios. In [12], block coordinate descent and successive convex optimization techniques are applied to optimize UE communication scheduling and UAV trajectory planning. The work in [13] decomposes the optimization problem into different sub-problems and employs fast global K-means along with an interior-point method to optimize the locations of UAVs. In the context of UAV networking problems, some studies focus on optimizing the uplink and downlink communication rates [12], UAV energy consumption [14], [15], quality of service [16] and the number of UEs covered [17]. Under controlled conditions, optimization-based approaches for UAV deployment and planning have demonstrated strong performance and robustness.

However, these methods are significantly hindered by high execution complexity in practical applications [7]. In large-scale dynamic environments, the inherent non-convexity of the optimization problems impedes the attainment of global optimality, thus limiting their overall effectiveness. Furthermore, these algorithms struggle to handle the vast state and action spaces in such networking scenarios, where the high dimensionality complicates accurate modeling and further increases computational complexity. Collectively, these factors constrain the ability of optimization-based methods to rapidly generate effective decisions in rapidly changing and unpredictable large-scale environments.

To address these limitations, the proposed approach leverages MARL to efficiently explore high-dimensional state and action spaces, reducing reliance on precise modeling of the networking task. Task-oriented grouping and reward decomposition simplify the coordination among multiple UAVs, mitigating the computational complexity associated with large-scale deployments. These combined mechanisms allow the framework to generate effective and robust UAV deployment decisions in dynamic, large-scale multi-hop networking scenarios.

## B. RL-Based Methods

In recent years, reinforcement learning (RL) has emerged as a prominent approach for addressing complex optimization challenges in UAV-assisted networks [18], [19], demonstrating remarkable capabilities in sequential decision-making and scheduling tasks. In [20], the authors introduce a constrained deep Q-network to maximize downlink capacity while ensuring comprehensive coverage for all UEs. [21] proposes a dualattention RL technique to address the time-varying UE traffic and mobility challenges in the environment. Additionally, several studies integrate UAV-assisted networking with data offloading and edge computing. These works employ RL algorithms to achieve fair throughput among UAVs [18], [22] or to minimize the content acquisition delay for UEs [8]. Song et al. [23] propose an improved evolutionary multi-objective RL algorithm to address both trajectory control and task offloading problems of the UAVs.

In this context, MARL [24], [25] algorithms enable each UAV to act as an individual decision-maker while leveraging interactions with other UAVs, making them well-suited for multi-hop wireless networks. [26] utilizes a multi-agent deep deterministic policy gradient (MADDPG) approach to optimize task offloading strategies between UEs and UAVs. Similarly, [27] proposes a decentralized multi-agent soft actor-critic algorithm to optimize spectral efficiency among UAVs. To capture the complex relationships between UAVs and UEs, [9] introduces a heterogeneous graph-based formulation that is integrated into MARL frameworks to facilitate the learning of distributed policies for UAVs. And [28] develops an attention-based heterogeneous graph neural network combined with model-based RL to optimize the UAVs’ resource allocation.

Despite significant advancements in MARL, some issues still persist. Many studies assume that the backhaul network interfacing with the core network is fully configured, thereby neglecting the optimization of relay nodes. In large-scale dynamic environments, such assumptions overlook the scalability challenges of coordinating dozens of UAVs for multi-hop relaying. As the number of UAVs increases, RL techniques encounter convergence issues due to the exponential growth of state and action spaces. The intrinsic randomness of RL further complicates long-term link maintenance in UAV networks. Another critical challenge in MARL is the credit assignment, which complicates the evaluation of each UAV’s contribution when only a global reward signal is available. For instance, the suboptimal performance of a single relay UAV can trigger network disconnections and a rapid decline in the global reward, potentially misleading other agents regarding the efficacy of their policies. Similarly, when overall performance gains are driven by a few critical UAVs, the remaining agents may overestimate their contributions. Moreover, the wide range of environmental states in large-scale scenarios results in a vast exploration space, thereby reducing algorithmic robustness. In the early stages of RL training, random initialization of model parameters leads to counterintuitive decisions that prompt unproductive exploration, ultimately impeding the training process.

In response to these challenges, in the proposed framework, UAVs are coordinated through a task-oriented grouping strategy that assigns specific roles, ensuring that relay responsibilities are explicitly considered. To mitigate the scalability and convergence issues arising from high-dimensional state and action spaces, a reward decomposition scheme is applied, which distributes global feedback into more localized signals, thereby improving credit assignment for individual UAVs and stabilizing learning. Behavioral constraints are enforced on critical UAVs to prevent disruptive topology changes, ensuring network robustness despite the intrinsic randomness of RL. Finally, to reduce the burden of exploration in vast and complex environments, large language models are employed during offline training to provide high-level strategic guidance, which is distilled into MARL policies to accelerate learning, guide effective UAV deployment, and maintain decentralized decision-making suitable for real-time operation.

## C. LLM-Based Methods

The development of LLMs has facilitated their application in robotic planning, where they exhibit strong reasoning and decision-making capabilities [29], [30], [31]. Building on this progress, recent studies have extended the use of LLM agents to UAV planning [32], [33], enhancing the efficiency of the planning process in complex environments. Furthermore, integrating LLMs with RL has emerged as a promising research direction. LLMs have been utilized to shape reward functions [34], enabling more nuanced and context-aware feedback for RL agents. They have also been applied to improve state representation [35] by capturing intricate relationships within the environment, which enhances the agent’s understanding of the environmental states. Additionally, LLMs have been employed to refine action selection [36], providing guidance that allows RL agents to make more informed and strategically aligned decisions, ultimately improving the performance of the system. Despite their potential, the application of LLMs in robotics and UAV planning faces notable challenges. In particular, LLMs’ sensitivity to input prompts can lead to inconsistent decision-making, especially in complex and dynamic tasks that require precise control. Moreover, the gap between the generalized knowledge of LLMs and specific domain requirements further complicates their practical integration, with the issue being more pronounced in problems with complex constraints. Existing methods that integrate LLMs with RL often assume low-dimensional or structured action and state spaces and rely on direct translation of LLM outputs into agent actions or hierarchical abstractions. These assumptions are unsuitable for multi-UAV multi-hop networking, where action and state spaces are high-dimensional, strongly coupled, and constrained by connectivity and communication requirements.

In the proposed approach, the semantic-level reasoning of the LLM is combined with the robustness and coordination capability of MARL to address these challenges. During MARL training, the LLM provides high-level strategic guidance for UAV deployment and networking. MRLMN then aligns these strategies with decentralized agent behaviors by assigning LLMsuggested roles via the Hungarian algorithm and distilling the resulting priors into the MARL policies. At deployment, MARL agents execute decisions independently, ensuring scalable and distributed control without requiring online interaction with the LLM.

## III. SYSTEM MODEL

In this section, the system components of the UAV-enabled emergency network and their spatial dynamics within the disaster environment are defined. The communication model is then introduced together with the connectivity constraints required to maintain a feasible multi-hop backhaul link to the core network. Building on these elements, the networking task is formulated as a joint trajectory optimization problem that aims to maximize user coverage and communication quality under practical operational constraints.

## A. Problem Formulation

In the networking system, we consider a setup with $U$ relay $\mathrm { U A V s } , M$ mobile UEs, and G BSs, represented by the sets $u =$ $\{ 1 , 2 , \ldots , U \} , \ \mathcal { M } = \{ 1 , 2 , \ldots , M \}$ , and $\mathcal { G } = \{ 1 , 2 , \dots , G \}$ respectively. The system operates in time slots, indexed as $t \in \tau$ , where $\mathcal { T } = \{ 1 , 2 , \hdots , T \}$ . Treating each entity from the UAV, UE, and BS groups as a node, the overall node set is expressed as $\pmb { \mathscr { N } } = \pmb { \mathscr { U } } \cup \pmb { \mathscr { M } } \cup \pmb { \mathscr { G } } .$ The interaction between these nodes facilitates the establishment of a multi-hop communication network, enabling UEs to maintain consistent connections with BSs. The position of each node $n \in \mathcal N$ at a specific time slot t is described in three-dimensional space by $l _ { n } ( t ) =$ $( x _ { n } ( t ) , y _ { n } ( t ) , z _ { n } ( t ) )$ ). The Euclidean distance between any two nodes $i , j \in \mathcal { N }$ at time t is given by $d _ { i , j } ( t ) = | | l _ { i } ( t ) - l _ { j } ( t ) | | _ { 2 }$ Prior studies on UAV-enabled communication have established modeling principles for node interactions and relay-assisted communication, offering validated abstractions for UAV modeling [37], link quality characterization and connectivity constraints [38], [39]. Complementary work on UAV-supported UE connection and communication adaptation [40], [41] further provides mechanisms for describing how UAVs maintain stable communication connectivity while serving UEs [42], [43]. Building on these foundations, the communication model, connectivity constraints, and optimization objective in this study can be formally established, thereby constructing a complete and consistent formulation of the UAV multi-hop networking task.

## B. Communication Model

In the proposed networking scenario, the communication dynamics are modeled across three types of links: UAV-UE links that facilitate data transmission between UAVs and UEs, UAV-UAV links that enable communication and coordination among UAVs, and BS-UAV links that support connectivity between BSs and UAVs.

UAV-UE links: For the UAV-UE links, a probabilistic path loss framework is employed to model the distinct characteristics and occurrence probabilities of Line-of-Sight (LoS) and Non-Line-of-Sight (NLoS) conditions. This approach captures the additional path loss caused by environmental factors such as shadowing and scattering, which significantly affect air-to-ground communication in realistic propagation environments. The LoS and NLoS path loss model for UAV $u \in u$ and UE $m \in \mathcal { M }$ is defined as

$$
P L _ { u , m } ^ { \mathrm { L o S } } ( t ) { = } 2 0 \log \left( \frac { 4 \pi f _ { c } } { c } \right) { + } 2 0 \log ( d _ { u , m } ( t ) ) { + } \eta _ { \mathrm { L o S } } ,\tag{1}
$$

$$
P L _ { u , m } ^ { \mathrm { N L o S } } ( t ) { = } 2 0 \log \left( \frac { 4 \pi f _ { c } } { c } \right) { + } 2 0 \log ( d _ { u , m } ( t ) ) { + } \eta _ { \mathrm { N L o S } } ,\tag{2}
$$

where $f _ { c }$ is the carrier frequency of the channel, c is the speed of light, $\eta _ { \mathrm { L o S } }$ and $\eta _ { \mathrm { N L o S } }$ are constant values representing the excessive path loss for LoS and NLoS links, respectively. The occurrence probability of the LoS channel follows

$$
P _ { u , m } ^ { \mathrm { L o S } } ( t ) = \frac { 1 } { 1 + a \exp \left[ - b \left( \frac { 1 8 0 } { \pi } \arcsin \left( \frac { z _ { u } ( t ) } { d _ { u , m } ( t ) } \right) - a \right) \right] } ,\tag{3}
$$

where $z _ { u } ( t )$ is the height of the UAV, a and b are environmental constants. The occurrence probability of the NLoS channel is given by $P _ { u , m } ^ { \mathrm { N L o S } } ( t ) = \bar { 1 } - P _ { u , m } ^ { \mathrm { L o S } } ( t )$ . Therefore, the path loss of the UAV-UE links is modeled as

$$
P L _ { u , m } ^ { \mathrm { U A V - U E } } ( t ) = P _ { u , m } ^ { \mathrm { L o S } } ( t ) P L _ { u , m } ^ { \mathrm { L o S } } ( t ) + P _ { u , m } ^ { \mathrm { N L o S } } ( t ) P L _ { u , m } ^ { \mathrm { N L o S } } ( t ) .\tag{4}
$$

UAV-UAV links: For UAV-UAV links, where signal propagation occurs in unobstructed airspace with minimal interference from environmental obstacles and LoS link is the dominant mode of communication, the free-space path loss (FSPL) model is adopted. Thus, the path loss for UAV-UAV links between u, $v \in u$ is given by

$$
P L _ { u , v } ^ { \mathrm { U A V - U A V } } ( t ) = 2 0 \log \left( \frac { 4 \pi f _ { c } } { c } \right) + 2 0 \log ( d _ { u , v } ( t ) ) + \eta _ { \mathrm { L o S } } .\tag{5}
$$

\- BS-UAV links: In this paper, the BS antennas are assumed to be mounted at a high elevation, consistent with real-world deployments. This positioning ensures a largely unobstructed communication environment with UAVs, allowing the channel to be approximated as free space. Under this assumption, the path loss for the link between UAV $u \in u$ and BS $g \in { \mathcal { G } }$ is modeled using the FSPL framework,

$$
P L _ { g , u } ^ { \mathrm { B S - U A V } } ( t ) = 2 0 \log \left( \frac { 4 \pi f _ { c } } { c } \right) + 2 0 \log ( d _ { g , u } ( t ) ) + \eta _ { \mathrm { L o S } } .\tag{6}
$$

Therefore, the received signal power from node $i \in \mathcal { N }$ to $j \in \mathcal N$ is given by

$$
P _ { i , j } ^ { \mathrm { R X } } ( t ) = P _ { i } ^ { \mathrm { T X } } G _ { i } ^ { \mathrm { T X } } G _ { j } ^ { \mathrm { R X } } 1 0 ^ { - P L _ { i , j } ( t ) / 1 0 } ,\tag{7}
$$

where $P _ { i } ^ { \mathrm { T X } }$ and $P _ { i , j } ^ { \mathrm { R X } }$ are the transmitted signal power and received signal power, $\ ' { G _ { i } ^ { \mathrm { T X } } }$ and $G _ { j } ^ { \mathrm { R X } }$ are the gains of the transmitter and receiver antennas, respectively. Accordingly, the signal-tonoise ratio (SNR) from node i to j is denoted as

$$
\rho _ { i , j } ( t ) = \frac { P _ { i , j } ^ { \mathrm { R X } } ( t ) } { 1 0 ^ { N _ { A } / 1 0 } } ,\tag{8}
$$

where $N _ { A }$ represents the noise power in dB form. In the environment, the noise power is computed according to

$$
N _ { A } = - 1 7 4 + 1 0 \log B + N F ,\tag{9}
$$

where -174 dBm/Hz represents the thermal noise power spectral density at room temperature, B represents the system bandwidth in Hz and NF denotes the noise figure. The available data rate from node i to j is determined based on the Shannon capacity formula as

$$
\begin{array} { r } { r _ { i , j } ( t ) = B _ { i , j } \log _ { 2 } ( 1 + \rho _ { i , j } ) , } \end{array}\tag{10}
$$

where $B _ { i , j }$ denotes the bandwidth.

## C. Connectivity Constraint

In multi-hop networks, the connectivity between nodes is crucial in determining whether a UE can successfully connect to the core network. In this paper, binary variables $c _ { m } ^ { \mathrm { U E } }$ and $c _ { u } ^ { \mathrm { U A V } }$ are denoted to indicate whether UE m or UAV u can establish a connection to an available BS through the multi-hop network. The connectivity of each link is determined based on a predefined SNR threshold $\rho _ { \mathrm { t h } }$ , where a link is considered disconnected if its SNR falls below the threshold. Moreover, UAVs can serve as relay nodes for UEs or other UAVs, constituting integral components of the multi-hop network that connects to the BS. A UAV can connect to the BS either directly or through multiple hops, while a UE accesses the core network via UAVs linked to the BS. Consequently, we have

$$
c _ { u } ^ { \mathrm { U A V } } ( t ) = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f } \exists g \in \mathcal { G } , \rho _ { g , u } ( t ) \geq \rho _ { \mathrm { t h } } , } \\ & { \mathrm { o r } \exists v \in \mathcal { U } \backslash \{ u \} , c _ { v } ^ { \mathrm { U A V } } ( t ) = 1 , \rho _ { u , v } ( t ) \geq \rho _ { \mathrm { t h } } } \\ { 0 , } & { \mathrm { o t h e r w i s e } } \end{array} \right.
$$

and

(11)

$$
c _ { m } ^ { \mathrm { U E } } ( t ) = \left\{ \begin{array} { l l } { 1 , } & { \mathrm { i f } \exists u \in \mathcal { U } , c _ { u } ^ { \mathrm { U A V } } ( t ) = 1 , \rho _ { u , m } ( t ) \geq \rho _ { \mathrm { t h } } } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.\tag{12}
$$

Within the network, UAVs select the backhaul path with the fewest relay hops, whereas UEs establish only the connection

that yields the maximum data rate. Accordingly, the data rate available to UE m is defined as

$$
\begin{array} { r } { r _ { m } ^ { \mathrm { U E } } ( t ) = \operatorname* { m a x } \{ r _ { u , m } ( t ) | c _ { u } ^ { \mathrm { U A V } } ( t ) = 1 , \rho _ { u , m } ( t ) \geq \rho _ { \mathrm { t h } } , u \in \mathcal { U } \} . } \end{array}\tag{13}
$$

## D. Objective Model

In this paper, the objective is to maximize the number of connected UEs and the accessible data rate under a set of constraints by optimizing UAV trajectories. To formulate the networking task, we define all $\mathrm { U A V s } ^ { \prime }$ trajectories as $\tau = \{ l _ { u } ( t ) | u \in \mathcal { U } , t \in$ $\tau _  \}$ , which records the coordinates of each UAV over time. The corresponding optimization problem is then defined as

$$
\tau ^ { * } = \underset { \tau } { \mathrm { a r g m a x } } \ \left( \frac { 1 } { T } \sum _ { t = 1 } ^ { T } \left( \frac { 1 } { M } \sum _ { m = 1 } ^ { M } c _ { m } ^ { \mathrm { U E } } ( t ) + \frac { \kappa } { M } \sum _ { m = 1 } ^ { M } r _ { m } ^ { \mathrm { U E } } ( t ) \right) \right)\tag{P1}
$$

$$
\mathrm { s . t . } | | l _ { u } ( t + 1 ) - l _ { u } ( t ) | | _ { 2 } \leq \Delta l _ { u } , \forall u \in \mathcal { U }\tag{C1}
$$

$$
l _ { u } ( t ) \in L ^ { E } , \forall u \in \boldsymbol { u }\tag{C2}
$$

$$
( 1 1 ) \mathrm { a n d } ( 1 2 )\tag{C3}
$$

where κ serves as a weighting factor that balances the objective function. The objective function, as shown in equation (P1), aims to maximize the coverage and data rate of all UEs over the optimization period. The first term represents the number of connected UEs, while the second term captures the data rate achieved by UEs. Constraint (C1) limits the movement of each UAV such that the distance it can travel in a single time slot is $\Delta l _ { u } = \omega \Delta t$ , where ω denotes the UAV speed and $\Delta t$ represents the duration of one time slot. Constraint (C2) restricts UAV trajectories to the spatial confines of the environment, denoted by $L ^ { E }$ . Moreover, the optimization problem is further bounded by communication and connectivity constraints, as delineated in equations (11) and (12).

## IV. METHODOLOGY

To address the scalability challenges and extensive exploration space in large-scale UAV networking, this section introduces the MRLMN framework. The networking objective is reformulated as a stochastic game, and a decentralized learning architecture based on the IPPO is adopted. Coordination is facilitated through an information aggregation mechanism and a role-based grouping strategy with decomposed rewards, while behavioral constraints ensure feasible motion and communication. A knowledge distillation module is employed to integrate LLM guidance, significantly improving exploration efficiency and guiding the learning of agent policies in complex decision scenarios.

## A. Stochastic Game Formulation

To capture the dynamic and uncertain nature of the operational environment and the interdependent decision-making processes of individual UAVs, the multi-UAV networking problem is modeled as a stochastic game defined by the tuple $( \mathcal { U } , \mathcal { S } , \{ \mathcal { A } ^ { u } \} _ { u \in \mathcal { U } } , P , \{ \mathcal { R } ^ { u } \} _ { u \in \mathcal { U } } , \gamma )$

1) State Space $\textstyle s :$ The state space of the networking environment is defined to encompass a) the spatial coordinates of all nodes within the network, b) the status of communication links, including SNR and data rate, c) the connectivity status of each UAV to the available BS via the multi-hop network, denoted by $\{ c _ { u } ^ { \mathrm { U A V } } ( t ) \} _ { u \in \mathcal { U } }$

2) Action Space $\pmb { \mathcal { A } } = \{ \pmb { \mathcal { A } } ^ { u } \} _ { u \in \mathcal { U } } :$ The action space specifies the set of movement decisions available to each UAV. In this paper, the UAVs move at a fixed cruise speed ω, which is treated as a constant system parameter. Accordingly, the action space includes only the selection of movement direction within the planar domain, modeled as eight discrete directional options together with a hovering action. This formulation captures the essential trajectory control while simplifying the decision-making complexity for MARL agents.

3) State Transition Probability P : The state transition defines how the system evolves based on UAV actions and environmental dynamics. Given the current state $s _ { t } .$ , each UAV u selects an action $a _ { t } ^ { u }$ , leading to a new state $s _ { t + 1 }$ with probability $P ( s _ { t + 1 } | s _ { t } , \{ a _ { t } ^ { u } \} _ { u \in \mathcal { U } } )$

4) Reward Model $\mathcal { R } = \{ \mathcal { R } ^ { u } \} _ { u \in \mathcal { U } } :$ The reward model quantifies UAV actions by evaluating network connectivity and data rate. Accordingly, the team reward, representing the environmental feedback on the effectiveness of UAV networking, is defined as

$$
R _ { t } = \frac { 1 } { M } \sum _ { m = 1 } ^ { M } c _ { m } ^ { \mathrm { U E } } ( t ) + \frac { \kappa } { M } \sum _ { m = 1 } ^ { M } r _ { m } ^ { \mathrm { U E } } ( t ) .\tag{14}
$$

Guided by this formulation, a novel reward model is proposed to support UAV decision-making, with detailed formulation provided in Section IV-D. The discount factor $\gamma$ is incorporated to balance immediate and future rewards.

## B. MARL Framework and Algorithm Overview

In this paper, the proposed model is designed based on the MARL algorithm, where multiple agents interact within a shared environment and iteratively refine their behaviors through trial-and-error. Within the model, each UAV u operates based on its own policy $\pi ^ { u } ( a _ { t } ^ { u } | o _ { t } ^ { u } ; \theta ^ { u } )$ , which dictates the action it should take given its observation $o _ { t } ^ { u }$ and learnable parameters of the policy network $\theta ^ { u }$ . The objective is to find a set of UAV policies that maximizes the joint discounted cumulative reward $\scriptstyle \sum _ { k = 0 } ^ { T - t } \gamma ^ { k } R _ { t + k }$ under the joint policy $\pi ( \boldsymbol { a } _ { t } | \boldsymbol { s } _ { t } ) =$ $\begin{array} { r l } { \prod _ { u \in \mathcal { U } } \pi ^ { u } ( a _ { t } ^ { u } | o _ { t } ^ { \overset { . . . } { u } } ) } & { { } } \end{array}$ , where $\mathbf { } \mathbf { } \mathbf { } \mathbf { a } _ { t }$ represents the joint action of all UAVs at time t. To train each UAV with a decentralized policy $\pi ^ { u }$ , the training approach is designed based on the Proximal Policy Optimization (PPO) algorithm [44]. The policy objective for each UAV u is initially defined as

$$
\textstyle { \mathcal { L } } _ { u } ^ { \mathrm { P P O } } ( t , \theta ^ { u } ) = \operatorname { \mathbb { E } } _ { o _ { t } ^ { u } , a _ { t } ^ { u } } [ \operatorname* { m i n } ( \zeta _ { t } ^ { \theta ^ { u } } A _ { t } ^ { u } , \operatorname { c l i p } ( \zeta _ { t } ^ { \theta ^ { u } } , 1 - \epsilon , 1 + \epsilon ) A _ { t } ^ { u } ) ] ,\tag{15}
$$

where $\zeta _ { t } ^ { \theta ^ { u } } = \pi ^ { u } ( a _ { t } ^ { u } | o _ { t } ^ { u } ; \theta ^ { u } ) / \pi ^ { u } ( a _ { t } ^ { u } | o _ { t } ^ { u } ; \theta _ { \mathrm { o l d } } ^ { u } )$ is the probability ratio between the updated and old policies, $A _ { t } ^ { u }$ is the advantage estimation,  is a hyperparameter that controls the clipping range, restricting policy updates to ensure stable training. The PPO entropy loss and critic loss [44] are also incorporated into the training process. The entropy loss encourages exploration by penalizing deterministic behavior and promoting action diversity. The critic loss is designed to improve value estimation accuracy, providing a more reliable baseline for policy updates and enhancing training stability. In this work, PPO is adopted due to its stable training behavior, where the clipped policy-update constraint prevents abrupt policy shifts that could otherwise induce disruptive topology changes or unexpected UE disconnections. Building upon PPO, the Independent PPO (IPPO) [45] formulation is adopted as the base framework because its decentralized policy and critic design allow each UAV to make decisions independently from local observations. This structure reduces the coordination complexity that arises when controlling large UAV swarms, mitigates the curse of dimensionality associated with multi-agent state and action spaces, and supports efficient parallel learning. As a result, IPPO offers natural scalability and robustness in dynamic multi-UAV multi-hop networking environments, making it well-suited for the proposed MRLMN architecture.

To address the challenges associated with UAV networking, several key modules are proposed based on the IPPO framework. To enhance inter-agent cooperation and improve algorithm scalability, an information aggregation module (see Section IV-C) and a grouping strategy (see Section IV-D) are introduced as core components. Meanwhile, the reward mechanism is adjusted to deliver clearer feedback tailored to each agent’s training process (see Section IV-D). During MARL training, the loss function is further augmented with a behavioral constraint term $\mathcal { L } ^ { \mathrm { B C } }$ to encourage the maintenance of robust multi-hop connectivity (see Section IV-E). Additionally, a knowledge distillation loss $\mathcal { L } ^ { \mathrm { K D } }$ based on LLMs is designed to promote structured exploration within the MARL paradigm (see Section IV-F). Consequently, the overall objective for each agent u is expressed as

$$
\operatorname* { m a x } _ { \pi ^ { u } } \mathcal { L } _ { u } ^ { \mathrm { P P O } } ( t ) - \beta _ { 1 } \mathcal { L } _ { u } ^ { \mathrm { K D } } ( t ) - \beta _ { 2 } \mathcal { L } _ { u } ^ { \mathrm { B C } } ( t ) ,\tag{16}
$$

where $\beta _ { 1 }$ and $\beta _ { 2 }$ are weighting coefficients that balance the relative importance of the primary objective with other terms. Through the integration of these components, the proposed framework effectively balances the optimization of network performance, the enforcement of connectivity constraints, and the incorporation of task-specific insights.

## C. Information Aggregation for Coordination

To enhance inter-agent cooperation, an information aggregation module is designed for each agent, and its output, together with the agent’s local observation, serves as the input to both the policy and critic networks. Effective cooperation among UAVs in a multi-agent networking environment relies on the exchange of local observations, enabling more informed decision-making and improved coordination. In the networking problem, UAVs are assumed to be able to share their local observations through the established communication network, enabling each UAV to acquire a more comprehensive view of the environment. The shared information at time t is considered as

$$
\begin{array} { r l } & { \boldsymbol { \xi } ( t ) = \big \{ \{ l _ { n } ( t ) \} _ { n \in { \cal N } , } \big \{ \rho _ { i , j } ( t ) \big \} _ { i , j \in { \cal N } , } } \\ & { \qquad \{ r _ { m } ^ { \mathrm { U E } } ( t ) \} _ { m \in { \cal M } , } \big \{ c _ { u } ^ { \mathrm { U A V } } ( t ) \big \} _ { u \in { \cal U } } \big \} . } \end{array}\tag{17}
$$

![](images/436e2df86b63af612bf54942b3b09ae711dba2d36c6c4f7b1fbfac65d8e9c4b2.jpg)  
Fig. 2. UAVs are grouped by role, with each UAV deploying an independent PPO-based policy and critic network. Local observations are shared among agents, and each UAV receives individualized reward components.

ξ(t) comprises four components: (i) the spatial coordinates l of UAVs, (ii) the quality of multi-hop links, measured by SNR $\rho ,$ (iii) the communication quality $\overset { \cdot } { r } { \mathrm { ~ u } } { \mathrm { E } }$ received by UEs, and (iv) the link status $c ^ { \mathrm { U A V } }$ of UAVs. The local observations are concatenated into ξ(t) based on the four distinct categories rather than simply aggregating individual agents’ local observations, making the aggregation more structured and organized. To establish information sharing among agents, the total observation for each UAV is defined as the concatenation of ξ(t) and a subset of the UAV’s local observation,

$$
o _ { t } ^ { u } = \mathrm { c o n c a t } ( \xi ( t ) , l _ { u } ( t ) , \{ \rho _ { u , i } ( t ) \} _ { i \in \cal N } ) ,\tag{18}
$$

where concat(·) denotes the concatenation operation, with all vectors flattened before being combined. The local observation of UAV u includes its position $\boldsymbol { l } _ { u }$ and the link qualities $\rho _ { u , i }$ of all links associated with it. The inclusion of the local observation is essential to ensure that each observation is uniquely associated with a specific UAV, enabling the policy network to map outputs unambiguously to the corresponding decentralized agent. This structure supports stable policy learning and enables agents to have a more comprehensive understanding of the environment, promoting better coordination and decision-making. In practical deployments, this design is feasible as UAVs exchange only compact coordination messages over the multi-hop network. The information aggregation module can be physically separated from the UE service module, thereby reducing interference and improving system reliability.

## D. Task-Based Agent Grouping and Reward Decomposition

To ensure efficient policy training and model scalability, UAVs are grouped according to their specific roles in the networking task, shown in Fig. 2. Within the networking environment, some UAVs are initially positioned closer to the BSs, making them well-suited for data relay functions. Conversely, some UAVs are located nearer to the UEs yet remain relatively distant from available BSs in emergency conditions, thereby necessitating robust communication links with users. Additionally, certain UAVs may be required to balance both responsibilities. Consequently, the responsibilities and training objectives of different UAV agents vary. To address this heterogeneity, the UAVs are partitioned into different groups $\mathbb { G } _ { i } , i \in \left\{ 1 , 2 , \dots , N _ { \mathbb { G } } \right\}$ Specifically, each UAV u is assigned to a group based on its distance to the nearest BS at time step 0, defined as

$$
d _ { u } ^ { \mathcal { G } } = \operatorname* { m i n } \left\{ d _ { u , g } ( t = 0 ) | g \in \mathcal { G } \right\} .\tag{19}
$$

To enable efficient group partitioning, a quantile-based segmentation strategy is applied to divide them into multiple groups. In this strategy, the UAVs are sorted based on $d _ { u } ^ { \mathcal { G } }$ and then partitioned into groups by dividing the ordered list into quantiles. The number of groups and the size of each group are jointly determined by the total number of UAVs and the spatial scale of the environment. UAVs with smaller $d _ { u } ^ { \mathcal { G } } .$ , typically located closer to BSs, are assigned to smaller groups, with group sizes approximately matching the number of BSs. In contrast, UAVs with larger $d _ { u } ^ { \dot { g } }$ values are grouped into larger subsets to improve communication coverage for UEs. Thus, this grouping strategy ensures that UAVs within the same group exhibit similar proximities to the BSs, while UAVs in different groups display distinct distance ranges. By aligning the training objectives with the distinct roles and responsibilities of UAVs in network tasks, this approach enables the development of customized training strategies.

Considering the distinct UAV groups $\mathbb { G } _ { i }$ , a reward decomposition module is developed to assign differentiated rewards to each agent, thereby ensuring tailored feedback. In the networking task, the overall team reward is formulated to capture both the connectivity and quality of communication service, as defined in (14). To ensure that each UAV receives targeted feedback, the networking task is subdivided into distinct components that delineate different agent responsibilities. The reward decomposition is formulated based on the following metrics:

1) UAV-UE Connection: This component evaluates the number of UEs connected directly to a given UAV u. Initially, a criterion for determining whether UE m is directly connected to UAV u is defined as

$$
\begin{array} { r l } & { I _ { u , m } ( t ) = \Im ( u = \arg \operatorname* { m a x } _ { v \in \mathcal { U } } \{ r _ { v , m } ( t ) | } \\ & { } \\ & { c _ { v } ^ { \mathrm { U A V } } ( t ) = 1 , \rho _ { v , m } ( t ) \geq \rho _ { \mathrm { t h } } \} ) . } \end{array}\tag{20}
$$

where <sup>1</sup>(·) is the indicator function that returns 1 if UAV u can provide the highest communication quality to UE m among all UAVs that m can directly connect to, and UAV u itself maintains a connection to the BSs. Therefore, to encourage UAVs to maintain high-quality communication links, the total data rate provided by UAV u to its connected UEs is measured by

$$
R _ { u } ^ { \operatorname { C o n n } } ( t ) = \sum _ { m = 1 } ^ { M } I _ { u , m } ( t ) r _ { m , u } ( t ) .\tag{21}
$$

The reward $R _ { u } ^ { \mathrm { { C o n n } } }$ incentivizes UAVs based on their direct connections with UEs, promoting efficient connectivity management within the network.

2) Relay Responsibility: In a multi-hop network, without adequate and direct incentives, UAVs may not optimally perform their relay duties, potentially disrupting network robustness, stability and overall performance. To quantify the contribution of UAV u in relaying data for other UAVs and UEs, $R _ { u } ^ { \mathrm { R E } }$ is defined to measure the total number of UEs that relay through UAV u when u serves as a relay among other UAVs. Primarily, the communication path through which a UAV connects to the BSs via a multi-hop network is defined as

$$
\begin{array} { r } { \mathrm { p a t h } _ { u } ( t ) = \left\{ \begin{array} { l l } { ( u \to g ) , \mathrm { i f } \exists g \in \mathcal { G } , \rho _ { g , u } ( t ) \geq \rho _ { \mathrm { t h } } } \\ { ( u \to \mathrm { p a t h } _ { v } ( t ) ) , \mathrm { i f } \mathrm { c o n d i t i o n } ( 2 2 . 1 ) } \\ { \emptyset , \mathrm { o t h e r w i s e } , } \end{array} \right. } \end{array}\tag{22}
$$

where → indicates the backhaul data transmission between network nodes. And condition (22.1) states

$$
\nexists g \in \mathcal { G } , \rho _ { g , u } ( t ) \geq \rho _ { \mathrm { t h } } \mathrm { ~ a n d ~ } v = \underset { v \in \mathcal { V } } { \arg \operatorname* { m i n } } \mathrm { ~ l e n } ( \mathrm { p a t h } _ { v } ( t ) ) ,\tag{22.1}
$$

where len(·) calculates the number of communication hops in a path. Additionally, $\mathcal { V } = \{ v | v \in \mathcal { U } \backslash \{ u \} , \rho _ { u , v } ( t ) \geq$ $\rho _ { \mathrm { t h } } , \operatorname { p a t h } _ { v } ( t ) \neq \varnothing \}$ represents the set of UAVs that UAV u can directly connect to, where each UAV in this set can establish a multi-hop backhaul link to the BSs. Formula (22) ensures that UAVs select the link with the fewest hops for data relaying. Based on all communication paths in the multi-hop network, the set of UAVs relayed through UAV v can be defined by

$$
\mathcal { U } _ { u } ^ { \mathrm { R E } } ( t ) = \{ v | v \in \mathcal { U } \backslash \{ u \} , u \in \mathrm { p a t h } _ { v } ( t ) \} .\tag{23}
$$

Therefore, the relay reward for UAV u is designed as

$$
R _ { u } ^ { \mathrm { R E } } ( t ) = \sum _ { v \in \mathcal { U } _ { u } ^ { \mathrm { R E } } ( t ) } \left( \sum _ { m = 1 } ^ { M } I _ { v , m } ( t ) r _ { m , v } ( t ) \right) .\tag{24}
$$

Based on the two reward components, the rewards for UAVs are composed of the overall team reward and individual contributions related to connecting with UEs and relaying data. These components are aggregated according to specific weights α assigned based on the group <sup>G</sup> that each UAV belongs to. The aggregated result serves as the UAV’s individual reward throughout the training process,

$$
R _ { t } ^ { u } = R _ { t } + \alpha _ { 1 } ^ { u } R _ { u } ^ { \mathrm { C o n n } } ( t ) + \alpha _ { 2 } ^ { u } R _ { u } ^ { \mathrm { R E } } ( t ) .\tag{25}
$$

As UAVs are categorized by role, the weights α are assigned based on group affiliation. For UAVs in groups that prioritize relaying, $\alpha _ { 2 } ^ { u }$ is relatively larger, emphasizing the relay reward $R _ { u } ^ { \mathrm { R E } } ( t )$ . Conversely, UAVs in groups that focus on UE connectivity have a higher $\alpha _ { 1 } ^ { u }$ , reinforcing the importance of $R _ { u } ^ { \mathrm { { C o n n } } } ( t )$ Based on this method, UAV agents prioritize tasks aligned with their designated roles during training, thereby enhancing the efficiency of policy learning.

## E. Behavioral Constraint for Robustness

In this paper, behavioral constraints are introduced to regulate the actions of UAVs directly connected to the BS within multi-hop networks. Notably, disconnections within this group, denoted as <sup>G</sup><sub>BS</sub>, present a significant risk, as they can trigger cascading failures along subsequent relay paths and ultimately lead to widespread network disruption. Thus, the UAVs in group $\mathbb { G } _ { \mathrm { B S } }$ serve as vital intermediaries, facilitating communication among nodes located beyond the BS’s direct transmission range, thereby sustaining overall connectivity and optimizing objectives. To address this issue, if the SNR of the links between $\mathrm { U A V } ~ u \in \mathbb { G } _ { \mathrm { B S } }$ and all BSs falls below $\rho _ { \mathrm { t h } } .$ , the UAV should be guided toward the BS with the highest SNR, defined as

$$
g ^ { * } = \arg \operatorname* { m a x } _ { g \in { \mathcal { G } } } \rho _ { u , g } .\tag{26}
$$

The expected directional guidance for the UAV is subsequently computed as

$$
z _ { u } ^ { \mathrm { B C } } ( t ) = \frac { l _ { g ^ { * } } ( t ) - l _ { u } ( t ) } { | | l _ { g ^ { * } } ( t ) - l _ { u } ( t ) | | _ { 2 } } .\tag{27}
$$

To maintain consistency between the computed guidance direction and the MARL action space, each action $a _ { i } \in { \mathcal { A } }$ is mapped to a direction vector as $z _ { i } = \operatorname* { m a p } ( a _ { i } )$ . For an agent u with action space $\pmb { A } ^ { u }$ , the corresponding set of directional vectors is formulated as

$$
Z ^ { u } = \{ \mathrm { m a p } ( a _ { i } ) \} _ { a _ { i } \in \pmb { A } ^ { u } }\tag{28}
$$

To ensure alignment between the derived guidance and the predefined discrete action space, the desired movement direction toward $g ^ { * }$ is mapped to the closest available action in the action space $\mathbfcal { A } ,$ as defined by

$$
z _ { u } ^ { * } ( t ) = \underset { z _ { i } \in Z ^ { u } } { \arg \operatorname* { m a x } } ~ \cos \left( z _ { u } ^ { \mathrm { B C } } ( t ) , z _ { i } \right) .\tag{29}
$$

To mitigate the risk of large-scale disconnection, a supplementary loss term is introduced for each UAV $u \in \mathbb { G } _ { \mathrm { B S } }$ at time $t ,$ defined as

$$
\begin{array} { r } { \mathcal { L } _ { u } ^ { \mathrm { B C } } ( t ) = - \mathbb { 1 } \big ( ( \underset { g \in \mathcal { G } } { \operatorname* { m a x } } ~ \rho _ { u , g } ( t ) ) < \rho _ { \mathrm { t h } } , u \in \mathbb { G } _ { \mathrm { B S } } \big ) } \\ { w _ { \mathrm { B C } } \log \pi ^ { u } ( \operatorname* { m a p } ^ { - 1 } ( z _ { u } ^ { * } ( t ) ) | o _ { t } ^ { u } ) , } \end{array}\tag{30}
$$

where map $^ { - 1 } ( \cdot )$ represents the inverse of the mapping function map(·), and $w _ { \mathrm { B C } } = | | l _ { g ^ { * } } ( t ) - l _ { u } ( t ) | | _ { 2 }$ scales the loss according to the UAV-BS distance. The imposed constraint on UAV behavior ensures stable connections with BSs, preventing erratic movements that may lead to large-scale network disconnections. This regulation is necessary for UAVs directly connected to BSs, as their movement patterns are more deterministic. In contrast, other UAV groups place greater emphasis on non-myopic planning, requiring increased flexibility to adapt to dynamic network conditions, making strict constraints unnecessary.

## F. LLM Agent and Knowledge Distillation

Given that LLMs possess knowledge and capabilities that are aligned with human preferences, they can be leveraged to guide and enhance the RL training process, thereby reducing unproductive exploration. LLMs do not aim to achieve globally optimal UAV networking solutions, but instead provide highlevel strategic guidance that narrows the MARL exploration space. This guidance effectively mitigates the cold-start problem during the initial stages of MARL training, improving learning efficiency and stability. Pretrained LLMs, although primarily trained on natural language data, can understand high-level semantic information about tasks and scenarios. By embedding chain-of-thought (CoT) reasoning into the inference process, LLM-based agents can interpret tasks, extract key features of networking tasks and environmental states, and make informed decisions. Additionally, random initialization in MARL often leads to inefficient exploration in the early stages, heightening the risk of converging to a local optimum. Given the scarcity of feasible network configurations within the vast search space, we propose utilizing LLM-driven decision-making to enhance the MARL training process. Therefore, an LLM agent is designed to offer an initial attempt at tackling the UAV multi-hop networking task, as shown in Fig. 3. To ensure that the LLM fully comprehends the networking task and the environmental state for better reasoning, the networking scenario is simplified to preclude the analysis of thousands of precise numerical values, such as location coordinates. And LLM agents generally do not perform at the level of models that have undergone domain-specific training. In this paper, the LLM module is designed primarily to supply RL agents with decisions that align with common sense, thereby aiding their exploration and training processes. Thus, the adoption of an appropriately simplified environment is considered both acceptable and beneficial. Notably, a single UAV can provide communication services over a contiguous region. In line with this regional characteristic of network service delivery, the entire environment is partitioned into grid cells. The grid width is configured to ensure that the UAV positioned at the center of each grid cell can communicate with the UAVs in the adjacent cells and establish connections with the majority of UEs within the grid, i.e. meeting the SNR requirements. Thus, the grid side length is given by $\begin{array} { r } { \dot { d } ^ { \mathrm { g r i d } } = \frac { 1 } { \sqrt { 2 } } ( \operatorname* { m a x } \{ d _ { u , v } | \rho _ { u , v } \geq \rho _ { \mathrm { t h } } \} ) } \end{array}$ , where $u , v \in u$ and the SNR $\rho _ { u , v }$ is determined by the distance $d _ { u , v }$ between UAVs. Consequently, the distribution of UEs is quantified by counting the number of UEs in each grid cell. Moreover, the UAV positions generated by the LLM are constrained to the centers of these grid cells, reducing the complexity of considering connectivity constraints.

![](images/a9aac56ce9f91ed2798b3a0c2d3337858250bf54986507001aa343253fc2e9ba.jpg)  
Fig. 3. A knowledge distillation mechanism is proposed to transfer the LLM’s decision-making capabilities to MARL agents. This design incorporates a bipartite matching strategy and a distillation loss function to align the decisions of the LLM and MARL agents, while simultaneously utilizing LLM’s chain-of-thought reasoning.

To effectively harness the LLM’s capabilities, a structured prompt is designed to encapsulate the key aspects of the task, enabling the LLM to generate precise, structured outputs. The input prompt to the LLM consists of several components:

\- Scenario description: Detail the UAV networking tasks, communication constraints, and emphasize relaying in multi-hop network organization.

\- Model behavior and objective: Clarify that the LLM should analyze UE distribution to determine optimal UAV deployment, ensure relay connections, and maximize the objective function.

Output constraints: Specify the desired output format, ${ \mathrm { e . g . } } \quad \cdots$ using the following format: \”[(UAV 3D coordinates), (UAV 3D coordinates) $, \ \dots \ ] \ \backslash \ ^ { \prime \prime } \ . \ . \ .$ ,,

\- Few-shot examples: Include representative input-output examples to guide the LLM in generating structured and accurate responses.

\- Current states: Provide key environmental information, including locations of BSs and UE distribution.

Directly mapping current states to UAV positions poses a challenge for the LLM agent [46], as it requires accounting for UE distribution, organization of multi-hop networks and ensuring UAV connectivity constraints for networking. Inspired by the CoT approach [46], the LLM reasoning process for the problem is partitioned into three sequential steps: a) Analyze UE distribution. Identify densely populated areas and determine candidate UAV deployment locations. b) Address connectivity gaps. Evaluate potential UAV connectivity gaps and reorganize UAV placements to ensure robust network connectivity. c) Determine the final UAV deployment based on the analysis of connectivity constraints and UE distribution. This stepwise approach enables the LLM to use more intermediate tokens to sequentially analyze the scenario and requirements, thereby enhancing the overall quality of the response.

To ensure reliable integration of LLM-generated guidance into MARL training, a rule-based verifier is used to validate UAV deployment plans and filter out infeasible outputs. CoT reasoning by the LLM can produce incorrect or inconsistent intermediate steps when generating high-level strategic plans for complex multi-UAV multi-hop networking tasks. The verifier checks that UAV positions are within operational boundaries and physically reachable. It verifies network connectivity by confirming that multi-hop paths remain connected, only a small number of UAVs are isolated, and sufficient UE coverage is maintained according to predefined thresholds. Deployment plans that fail these checks are discarded, preventing infeasible guidance from influencing MARL policy learning. Other methods, such as Retrieval-Augmented Generation [47], Reasoning and Acting [48], or Supervised Fine-Tuning [49], can also improve the reliability of LLM outputs. However, they introduce substantial computational overhead during training. Discarding invalid outputs using a lightweight, rule-based verifier ensures the quality and reliability of LLM-generated guidance while providing an efficient and practical solution for the task.

Building on the designed LLM agent, a knowledge distillation mechanism is proposed to further enhance MARL performance and guide its training. Within this framework, the LLM is designated as the teacher and the MARL agents as the students. A distillation loss is designed to transfer the LLM’s decisionmaking capabilities to the MARL agents by quantifying the similarity in network outputs between the LLM and the MARL policies. To enable the current UAVs to efficiently approach the positions provided by the LLM, an optimal bipartite matching is computed, establishing a one-to-one correspondence between the LLM-inferred positions $\{ l _ { u } ^ { \mathrm { L L M } } ( t ) \} _ { u \in \mathcal { U } }$ and the current UAV positions $\{ l _ { u } ( t ) \} _ { u \in \mathcal { U } }$ . Thus, a permutation function $\sigma \in { \mathfrak { S } } _ { U }$ is introduced, where ${ \mathfrak { S } } _ { U }$ denotes the symmetric group of all permutations over $U$ elements. The goal is to determine σ that minimizes the pairwise cost

$$
\begin{array} { r } { \mathcal { L } ^ { \mathrm { M A T C H } } \left( l _ { u } , l _ { \sigma ( u ) } ^ { \mathrm { L L M } } \right) = \left. l _ { u } - l _ { \sigma ( u ) } ^ { \mathrm { L L M } } \right. _ { 2 } , } \end{array}\tag{31}
$$

defined as the Euclidean distance between the UAV indexed by u in the environment and its matched counterpart indexed by σ(u) given by the LLM. To obtain the optimal permutation, the objective is formulated as

$$
\boldsymbol { \sigma } ^ { * } = \mathop { \arg \operatorname* { m i n } } _ { \boldsymbol { \sigma } \in \mathfrak { S } _ { U } } \sum _ { \boldsymbol { u } \in \boldsymbol { U } } \mathcal { L } ^ { \mathrm { M A T C H } } \left( \boldsymbol { l } _ { \boldsymbol { u } } , \boldsymbol { l } _ { \boldsymbol { \sigma } ( \boldsymbol { u } ) } ^ { \mathrm { L L M } } \right) .\tag{32}
$$

In this paper, the optimization of the permutation is achieved using the Hungarian algorithm [50]. Under the optimal permutation, the LLM-expected action for each UAV u in the current state is derived as

$$
z _ { u } ^ { \mathrm { L L M } } ( t ) = l _ { \sigma ^ { * } ( u ) } ^ { \mathrm { L L M } } ( t ) - l _ { u } ( t ) .\tag{33}
$$

To align the LLM-inferred action with the MARL agent’s discrete action space, a soft target distribution is constructed based on the cosine similarity between the inferred action and each candidate action in the predefined action space. Specifically, for each discrete action in the MARL action space, the soft target probability is formulated as

$$
\widetilde { p } _ { u } ( z _ { i } , t ) = \frac { \exp ( \cos ( z _ { u } ^ { \mathrm { L L M } } ( t ) , z _ { i } ) / \Omega ) } { \sum _ { z _ { j } \in Z ^ { u } } \exp ( \cos ( z _ { u } ^ { \mathrm { L L M } } ( t ) , z _ { j } ) / \Omega ) } , z _ { i } \in Z ^ { u }\tag{34}
$$

where cos(·) ensures that actions more aligned with the LLMinferred direction receive higher probabilities, $z ^ { u }$ represents the set of directional vectors corresponding to the action space, as defined in (28) and Ω is a temperature parameter that controls the smoothness of the probability distribution. The soft target distribution encapsulates information from LLM, offering nuanced guidance during training [51]. The distillation loss is then defined as the cross-entropy between the MARL agent’s policy and the soft target distribution

$$
\mathcal { L } _ { u } ^ { \mathrm { K D } } ( t ) = - \sum _ { z _ { i } \in \cal Z ^ { u } } \widetilde { p } _ { u } ( z _ { i } , t ) \log \pi ^ { u } ( \operatorname* { m a p } ^ { - 1 } ( z _ { i } ) | o _ { t } ^ { u } ) .\tag{35}
$$

This formulation enables MARL agents to effectively leverage the LLM’s inferred actions as supervisory signals, allowing them to learn the LLM’s decision-making capabilities. In the proposed framework, the LLM participates exclusively during the offline training phase, providing high-level strategic guidance for UAV deployment and multi-hop network coordination. Its outputs are incorporated into MARL policies through a soft target-based distillation loss, ensuring that strategic priors guide the learning process. This offline integration prevents the LLM from participating in real-time UAV control, avoiding additional latency and computational overhead, and making the method feasible for practical network deployments. During online deployment, each UAV executes its MARL policy independently, without LLM inference, ensuring that real-time control is decentralized, incurs no extra computational burden, and remains practical and reproducible in large-scale multi-hop UAV networks. This technique promotes structured exploration and enhances both the training and inference processes of MARL.

## G. Overall Algorithm and Complexity Analysis

The complete training procedure of MRLMN is summarized in Algorithm 1. The framework operates in a hybrid manner. UAVs continuously execute decentralized control using MLPbased policy networks $\pi _ { \theta }$ under the IPPO paradigm, while the LLM is queried only once every $Q _ { \mathrm { L L M } }$ steps to provide highlevel deployment guidance. At each step, UAVs first aggregate observations from other UAVs, take actions through the learned policies, and collect transitions into the replay buffer D. When LLM guidance is triggered, the suggested deployment topology is cached using $\mathcal { T } _ { \mathrm { c a c h e d } } ^ { \mathrm { L L M } }$ and aligned with the UAVs’ current configuration through bipartite matching, enabling knowledge distillation to shape subsequent policy updates. IPPO optimization is then performed at the end of each episode, incorporating both the distillation objective and the behavioral constraint. From a computational perspective, each UAV is equipped with an MLP consisting of L hidden layers of width H. Thus, with U UAVs executing their policies in parallel, the per-step inference cost scales as $\mathcal { O } ( U \cdot L \cdot H ^ { 2 } )$ . During training, the same order applies to forward and backward passes of both the policy and critic networks. LLM reasoning is executed once every $Q _ { \mathrm { L L M } }$ steps, with a single inference cost $\mathcal { C } _ { \mathrm { L L M } }$ contributing an amortized $\mathcal { C } _ { \mathrm { L L M } } / Q _ { \mathrm { L L M } }$ per step. The bipartite matching needed for distillation incurs $\mathcal { O } ( U ^ { 3 } )$ complexity, which is lower than the neural network computations and is invoked once per step. Additionally, the overhead from information aggregation, reward decomposition, and behavioral constraints is minimal. Consequently, MLP-based networks dominate inference complexity, whereas during training, both the neural networks and the amortized LLM guidance jointly determine the overall computational cost.

```latex
Algorithm 1: Training Procedure of MRLMN.
Initialize: Policy networks $\pi _ { \theta } .$ , PPO replay buffer D
Parameters: $N _ { \mathrm { e p } }$ (episodes), T (episode horizon), K
(training epochs), $Q _ { \mathrm { L L M } }$ (LLM guidance interval)
Cache: $\bar { \mathcal { T } } _ { \mathrm { c a c h e d } } ^ { \mathrm { L L M } }  \emptyset$ -Cached LLM-suggested UAV
deployment
for episode $k = 1 \ldots N _ { \mathrm { e p } }$ do
$s _ { 0 } \sim p _ { \mathrm { i n i t } } ( s )$ -Reset environment
Initialize agent grouping for the episode
for step $t = 1 \dots T$ do
$\mathbf { o } _ { t } ^ { \mathrm { i n d } } $ GetEnvironmentObservation $\mathrm { ( s _ { t } ) }$
$\mathbf { o } _ { t }  \mathrm { A g g r e g a t e I n f o } ( \mathbf { o } _ { t } ^ { \mathrm { i n d } }$ , grouping)
-Information aggregation
if t mod $Q _ { \mathrm { L L M } } = = 0$ then
$\mathcal { T } _ { \mathrm { c a c h e d } } ^ { \mathrm { L L M } }  \mathrm { L L M } _ { - }$ _Inference $\left( \mathbf { o } _ { t } \right)$
-Update and cache LLM guidance
end if
$\mathbf { a } _ { t } \sim \pi _ { \theta } ( \cdot \mid \mathbf { o } _ { t } )$
$s _ { t + 1 } , \mathbf { r } _ { t } \gets \mathrm { E n v . S t e p } ( \mathbf { a } _ { t } )$ -Environment transition
$\begin{array} { r } { \sigma ^ { * } = \arg \operatorname* { m i n } _ { \sigma \in \mathfrak { S } _ { U } } \ \sum _ { u \in \mathcal { U } } \mathcal { L } ^ { \mathrm { M A T C H } } ( l _ { u } , l _ { \mathrm { c a c h e d } , \sigma ( u ) } ^ { \mathrm { L L M } } ) } \end{array}$
-Bipartite matching
R<sub>t</sub> ← Reward_Decomp $( \mathbf { r } _ { t } ,$ grouping)
-Reward Decomposition
$\mathcal { D }  \mathcal { D } \cup \big \{ \big ( \mathbf { o } _ { t } , \mathbf { a } _ { t } , \mathbf { R } _ { t } , \mathbf { o } _ { t + 1 } , \sigma ^ { * } \big ) \big \}$
end for
for epoch $1 \ldots K$ do
max<sub>πθ</sub> $\mathcal { L } ^ { \mathrm { P P O } } - \beta _ { 1 } \mathcal { L } ^ { \mathrm { K D } } - \beta _ { 2 } \mathcal { L } ^ { \mathrm { B C } }$
-MARL Optimization with knowledge distillation
and behavioral constraints
end for
end for
```

## V. PERFORMANCE EVALUATION

This section evaluates the proposed MRLMN framework in multi-UAV multi-hop networking scenarios under diverse conditions, including varying environment scales, UAV swarm sizes, baseline comparisons, training dynamics, and ablation studies. The experiments demonstrate the framework’s stability, scalability, adaptability, and coordination effectiveness, while also examining the impact of parameter sharing within agent groups on training efficiency and policy quality. The results highlight the overall superior performance of MRLMN across these settings.

## A. Experimental Setup

1) Environment Setup: To assess the performance of our proposed method, we employ a simulation environment that spans an area of approximately 3.5 km × 3.5km, within which around 150 UEs and 18 UAVs are deployed. The distribution of UEs follows either a uniform pattern or a two-dimensional Gaussian mixture with multiple centers, and their motion follows a Brownian process at a constant velocity. The BSs are strategically positioned at three of the four corners of the area to preclude direct connections with the UEs, thereby simulating communication conditions typically encountered in disaster scenarios. The UAV speed ω is limited to a displacement of 30 meters within each time slot.

2) Training Configuration: For the training process, a total of 25,000 episodes are conducted, with each episode consisting of 400 time slots. The PPO policy and critic networks are implemented as multi-layer perceptrons with five hidden layers, each employing the tanh activation function. And the learning rate is initially set to $3 \times 1 0 ^ { - 4 }$ and is progressively lowered to $1 \times 1 0 ^ { - 4 }$ toward the end of the training process. The LLM guidance is provided using the GPT-4o model [52], which gener ates high-level strategic deployment suggestions during MARL offline training. In the networking task, we assume identical transmitter and receiver antenna gains, with UAV, UE, and BS antenna gains set to $0 , 0 ,$ and 5 dBi, respectively. In equation (P1), the weighting factor κ is defined as 0.025 when the data rate $r ^ { \mathrm { U E } }$ is measured in Mbps. The coefficient $\beta _ { 1 }$ , which controls the weight of the knowledge distillation component, is initially set to 0.5 and is gradually reduced to 0.1 during the final phase of training. It is designed to help improve the effectiveness of MARL by gradually shifting the focus from distillation to the training objective. In MARL training, the UAVs are divided into four groups based solely on the distance relationship between each UAV and the set of BS nodes ${ \mathfrak { s } } ,$ as defined by equation (19). The network parameters of each agent remain independent and are not influenced by the grouping strategy. Furthermore, a detailed discussion on the relationship between parameter sharing in groups and training performance can be found in Section V-D. Due to the substantial inference latency of the LLM, which adversely affects the training efficiency of the MARL agents, LLM inference is performed only at selected time slots within each episode, specifically once every $Q _ { \mathrm { L L M } }$ steps to obtain the required guidance output. For subsequent time slots, the validated LLM outputs are cached and subsequently reused in the computation of the knowledge distillation loss, $\mathcal { L } ^ { \mathrm { K D } }$ . Since the UE distribution typically experiences only minor changes over short time intervals, the retained outputs perform well during these periods. Additionally, given that the LLM agent is primarily tasked with guiding MARL agent training and managing an extensive exploration space, even suboptimal network decisions from the LLM are acceptable, ensuring that this intermittent LLM reasoning strategy does not lead to a sig nificant negative impact on knowledge distillation. Additional critical parameter settings are summarized in Table I. To focus on evaluating MARL coordination and policy performance rather than detailed physical-layer optimization, the bandwidth alloca tion across BS-UAV, UAV-UAV, and UAV-UE links is assumed to be fixed, which serves to mitigate cross-link interference.

3) Performance Metrics: The performance of the algorithm is assessed using two primary metrics: the quality of service, defined as the average data rate per UE, calculated as $\textstyle ( 1 / M ) \sum _ { m = 1 } ^ { M } r _ { m } ^ { \mathrm { U E } }$ and the connected UE proportion $( 1 / M ) \textstyle \sum _ { m = 1 } ^ { M } c _ { m } ^ { \mathrm { U E } }$ , i.e. the proportion of UEs that are successfully connected to the core network relative to the total number of UEs. To evaluate the robustness of each model in the networking task, the number of available UAVs is introduced as another metric. This metric quantifies the number of UAVs that successfully establish and maintain connectivity with the BSs and core network through the multi-hop UAV network. A higher value indicates fewer disconnections, reflecting a more resilient and stable network. Formally, it is measured as $\begin{array} { r } { ( 1 / U ) \sum _ { u \in \mathcal { U } } c _ { u } ^ { \mathrm { U A V } } } \end{array}$ where $c _ { u } ^ { \mathrm { U A V } }$ denotes the connectivity status of UAV u, defined in (11). This metric serves as a key indicator of the stability and effectiveness of each algorithm.

TABLE I  
PARAMETER SETTINGS
<table><tr><td>Parameters</td><td>Value</td></tr><tr><td>System frequency fc</td><td>Around 2.4 GHz</td></tr><tr><td>Bandwidth B for each BS-UAV link</td><td>7MHz</td></tr><tr><td>Bandwidth B for each UAV-UAV link</td><td>5MHz</td></tr><tr><td>Bandwidth B for each UAV-UE link</td><td>1 MHz</td></tr><tr><td>Transmitted signal power  $P ^ { \mathrm { T X } }$  of UAV, BS, UE</td><td>1, 10, 0.4 W</td></tr><tr><td>The excessive path loss for NLoS links ηNLos</td><td>20 dB</td></tr><tr><td>The excessive path loss for LoS links ηLos</td><td>1 dB</td></tr><tr><td>Environmental constant a, b</td><td>9.61, 0.16</td></tr><tr><td>Speed of light c</td><td>3×108m/s</td></tr><tr><td>SNR threshold  $\rho _ { \mathrm { t h } }$ </td><td>25 dB</td></tr><tr><td>Noise figure  $N F$ </td><td>15 dB</td></tr><tr><td>Reward decomposition related  $\mathrm { w e i g h t s } \ \alpha _ { 1 } , \alpha _ { 2 }$ </td><td>1,3</td></tr><tr><td>Objective related weights  $\beta _ { 2 }$ </td><td>0.3</td></tr><tr><td>Temperature parameter Ω</td><td>1</td></tr></table>

## B. Comparative Experiments

In this section, we present a comprehensive performance evaluation of the proposed MRLMN framework by benchmarking it against five representative baselines that include both independently trained agents and cooperative MARL approaches:

GVis: A MARL framework [9] based on heterogeneous graphs, designed to enhance cooperation among UAVs. This method optimizes local observation management and enables cooperation through explicit information exchange among nodes in the network. Slight modifications are made to adapt this framework for application in the UAV networking scenario.

GA2C: A RL framework [53] that integrates graph neural network (GNN) to guide action training within an Advantage Actor-Critic (A2C) architecture. By leveraging hidden representations from network feature correlations, this method captures intricate environmental relationships, thereby enhancing the efficiency of policy training.

\- MAPPO: A MARL algorithm [25] introduced for coordinating agents by utilizing a centralized value function during training, while allowing each agent to act independently during execution. This strategy has demonstrated competitive performance on a range of cooperative benchmark tasks.

\- IA2C: An independent RL method based on the A2C architecture [54]. In this approach, each UAV agent learns its policy independently without explicitly considering the joint state or actions of other agents, serving as a baseline for non-cooperative learning.

\- MAA2C: A multi-agent variant of A2C that employs a centralized training and decentralized execution paradigm similar to MAPPO but relies on the A2C optimization objective.

Fig. 4 shows the training curves over 10 million steps, depicting the performance trends of different methods in terms of the objective function defined in equation (P1). The experiments are set in a 3.5 km × 3.5 km environment with 18 UAVs, evaluating the proposed framework under large-scale networking conditions. The results show that the proposed MRLMN method significantly outperforms the baseline methods throughout the training process. MRLMN exhibits a rapid increase in training performance, stabilizing above 0.8, while the competing methods plateau at much lower values. In detail, GVis performs relatively better among the baselines but still falls short of MRLMN. MAPPO and GA2C stabilize between 0.4 and 0.6, whereas the A2C-based methods converge more slowly and achieve lower overall performance, fluctuating around 0.4. The curves indicate that the proposed algorithm, by integrating multiple modules, achieves superior networking performance. Specifically, the knowledge distillation module enables reinforcement learning agents to rapidly acquire generalized decision-making capabilities, accelerating the overall training process. In parallel, the reward decomposition and behavioral constraints allow for fine-tuning of agent behaviors, ensuring a better adaptation to the unique challenges of UAV multi-hop networking.

![](images/52298fc3349bc5efb340bda154bf2612978be7405626b29bf2adf7cb8262e6a2.jpg)  
Fig. 4. Training curves of different models over training steps, with the team reward computed according to (14). Shaded regions represent the standard deviation.

Furthermore, to provide a comprehensive view of scalability and network robustness, we conduct a detailed comparison against the key baselines (GVis, GA2C, and MAPPO) across several metrics under varying network conditions, including changes in geographical area size and the number of deployed UAVs.

1) Impact of Environment Size: Fig. 5(a), (c), (e) examine the influence of expanding the square environment area from $6 . 7 6 ~ \mathrm { k m ^ { 2 } }$ to 14.44 km , with the number of UAVs fixed at 18. The shaded regions indicate the standard deviation of each method, providing insight into algorithmic stability. In Fig. 5(a), the number of connected UEs for all approaches declines as the area expands, reflecting the increased difficulty of maintaining reliable connections over larger regions populated with numerous UEs. Nevertheless, compared to GVis, GA2C, and MAPPO, MRLMN achieves an average UE coverage improvement of approximately 27% and maintains greater performance stability across the entire range of area sizes. A similar trend is observed in Fig. 5(c), which reports the average data rate in Mbps under the same conditions. MRLMN not only sustains better coverage but also delivers higher throughput across various environment sizes. For these two metrics, GVis and GA2C exhibit similar performance, both relying on GNN-based strategies for UAV coordination. However, MRLMN incorporates scenario-specific grouping and reward mechanisms, allowing for more adaptive decision-making. Additionally, its knowledge distillation method is designed for large-scale environments, further enhancing overall performance. Moreover, it is observed that the objectives of connectivity coverage and communication data rate are correlated. Adjustments in UAV networking that improve network connectivity also tend to increase communication rates, reflecting the overall performance gains achieved through coordinated multi-hop networking. In Fig. 5(e), all methods exhibit a reduction in the number of available UAVs, highlighting the increasing challenge of sustaining multi-hop connectivity over larger regions. Nonetheless, MRLMN maintains a higher number of available UAVs and lower variance compared to other methods, demonstrating its enhanced stability and robustness in large-scale networking scenarios. In smaller environments, MRLMN achieves nearly 100% availability of UAVs, while in larger environments, it outperforms the best alternative by approximately 17%. This advantage stems from MRLMN’s relay-oriented reward design and connectivity-preserving behavioral constraints, which enable more effective multi-hop link management.

![](images/550e7db30ab7134549fe6decea3a35fbd67e75f94d2e6b5facf3a3411b7bee7c.jpg)  
(a)

![](images/c6285608a1098d4f9cbacb781e04bfb4512ba092eb9de79f771dafaff046a4c7.jpg)  
(b)

![](images/626010ac9d653e3438a3e3744ddb8dc196af2b769d20a574543f987f8ff94527.jpg)  
(c)

![](images/d619851e86ef5a05f5d9d8c807cf088d2e489bf55c67974e03adb7ab1465ede2.jpg)  
(d)

![](images/e726ee57be1a29a701a31e2b5ca7ea225da052572397ab3d0c874972b618b0eb.jpg)  
(e)

![](images/4299a9d4f646b846e51b2ea863e537b524d612382f60a82bb1fcd3814d60df84.jpg)  
(f)  
Fig. 5. Comparison of model performance across three key metrics: connected UE proportion, average data rate, and available UAV ratio under varying environment areas and numbers of UAVs. (a) Connected UE proportion versus area size. (b) Connected UE proportion versus number of UAVs. (c) Average data rate versus area size. (d) Average data rate versus number of UAVs. (e) Available UAV ratio versus area size. (f) Available UAV ratio versus number of UAVs. Shaded regions represent the standard deviation.

2) Impact of the Number of UAVs: Fig. 5(b), (d), (f) illustrate the performance of different methods as the number of UAVs increases from 12 to 24, maintaining a 3.5 km × 3.5 km environment. As the number of UAVs increases, the performance of all methods improves, as a large-scale environment requires more UAVs to establish a stable network. Considering these three metrics, MRLMN consistently outperforms all baseline methods, demonstrating superior networking performance even under limited UAV deployment. Specifically, MRLMN achieves an average of 23% higher UE coverage, 52% higher data rate, and a 19% higher UAV availability ratio compared to other methods across all three metrics. As the number of UAVs increases, MRLMN consistently maintains its advantage over other methods, highlighting its scalability. This is largely attributed to the proposed grouping strategy and the design of the group-based reward and behavioral constraint mechanisms, which provide more precise environmental feedback and offer clearer guidance for agent training. Meanwhile, the knowledge distillation module utilizes the matching mechanism to decompose the LLM’s decisions and deliver them to individual agents, providing clear supervisory signals to guide their policy learning.

## C. Ablation Study

To investigate the contribution of each key component in our proposed framework, we conduct an ablation study by testing the system under three different configurations where specific modules are removed:

\- Without Agent Grouping and Reward Decomposition (NR): In this configuration, the grouping and reward decomposition mechanism is omitted. As a result, agents are trained solely with a global reward signal, which obscures the evaluation of individual contributions. This lack of localized feedback makes it more challenging for agents to adjust their own policies effectively, thereby impeding coordinated behavior.

\- Without Knowledge Distillation and LLM Agent (NL): In this configuration, the knowledge distillation module that leverages the LLM agents is omitted. Consequently, agents rely solely on random initialization for their policy parameters during the early stages of training, which leads to extensive unproductive exploration and difficulties in handling the large exploration space. This negatively impacts training efficiency and convergence, ultimately degrading overall performance.

\- Without Behavioral Constraint (NC): This configuration removes the behavioral constraint module designed to ensure the connectivity stability of relay UAVs. As a result, relay UAVs are more prone to disconnections from BSs, increasing the risk of network disconnections. This disruption destabilizes the overall algorithm, leading to greater performance fluctuations and reduced reliability in dynamic environments.

![](images/94fe405ae39c66cba7a5185a42bbb5cfe99bb5663f53f551a65fcd5b41290a57.jpg)  
(a)

![](images/e1763cf2caabe927c5b07b9edb1085abea96805f6b11e7842d61f337c1d5f381.jpg)  
(b)

![](images/00e391718dbc6cb85615e45f64c4066113cedf7abd7dfd9f6a946583996ff4fa.jpg)  
(c)

![](images/80ee522b10383c109d0119d968f3407b4bd61225591b45235706dfe23c04a05e.jpg)  
(d)

![](images/d4e1f9b0a265fcff6383abf4a3e88dddb3c0fb4a46e220d4ac597f83b1e4bdd2.jpg)  
(e)

![](images/28ea4a84af9f9373069ccce9d352ac761b52cfffd395428b7854e58edd508c00.jpg)  
(f)  
Fig. 6. Ablation study on model performance across different area sizes and numbers of UAVs in terms of connected UE proportion, average data rate, and available UAV ratio. (a) Connected UE proportion versus area size. (b) Connected UE proportion versus number of UAVs (c) Average data rate versus area size (d) Average data rate versus number of UAVs. (e) Available UAV ratio versus area size. (f) Available UAV ratio versus number of UAVs. “Ours”, “NC”, “NL”, and “NR” denote different ablation variants Shaded regions represent the standard deviation.

Each configuration is evaluated in the same simulation environment to quantify the individual impact of these components on performance metrics, i.e. network coverage, quality of network service, and algorithm stability.

Fig. 6(a), (c) and (e) illustrate the experimental results as the environmental size increases with a fixed deployment of 18 UAVs. The proposed method outperforms the methods NC, NL, and NR across all environmental configurations. As the environment size expands to 14.44 km , the proposed method continues to deliver superior performance, achieving a connected UE proportion of 46%, an available UAV ratio of 88%, and a data rate of 5.2 Mbps. In contrast, the MRLMN shows a performance decline when specific modules are removed. For instance, the results of NR are notably lower, with a connected UE proportion of 40%, an available UAV ratio of 82%, and a data rate of 4.5 Mbps. Moreover, Fig. 6(b), (d) and (f) demonstrate the performance of the four methods across key metrics as the number of UAVs increases from 12 to 24 in a fixed square environment with a 3.5 km side length. The proposed algorithm exhibits noticeable performance degradation when any of the key modules is removed, indicating the importance of each component in addressing the challenges of multi-hop UAV networking. Specifically, removing any single module results in an average decline of at least 6% in UE coverage and 10% in data rate. In terms of the proportion of UAVs connected to the BS, removing any module also leads to a noticeable performance drop, particularly in large-scale environments with a limited number of deployable UAVs.

These results indicate that the removal of certain modules negatively impacts the networking performance of the proposed algorithm. The performance of NL suggests that the absence of the knowledge distillation module lowers MRLMN performance, emphasizing its critical role. By constraining the exploration space, the distillation loss from LLM agents mitigates inherent exploration challenges in MARL. This facilitates faster convergence and enhances training effectiveness. Additionally, the reduced available UAV ratio observed in NC underscores the role of behavioral constraints in stabilizing the model and preserving network connectivity. The poorer performance of NR in terms of UE coverage and communication rate also highlights the importance of agent grouping and reward decomposition in improving the algorithm’s overall performance. The integration of both methods facilitates efficient training by providing clear and structured environmental feedback, thereby improving performance.

Collectively, these designed components establish a wellintegrated framework that surpasses conventional approaches in maintaining connectivity, ensuring UAV availability, and optimizing data transmission rates. The results indicate that the proposed method offers a highly effective solution for UAVassisted communication systems, particularly in dynamic and large-scale networking scenarios.

## D. Discussion: Parameter Sharing Within Agent Groups

In this section, the impact of incorporating intra-group strategy sharing within the agent grouping scheme on training performance and training time is discussed. As discussed in Section IV-D, UAV agent grouping is established based on the responsibilities assigned to each UAV, which forms the foundation for parameter sharing. It is evident that agents within the same group share similar responsibilities, which makes network parameter sharing within these groups feasible. By reducing the number of parameters that need to be individually trained, parameter sharing can significantly enhance the efficiency of the training process. This approach leads to a decrease in the total number of trainable parameters, resulting in faster convergence and reduced training time under a fixed number of training steps. Specifically, in the experiment, a different number of agents within the UAV group are randomly selected to share their network parameters. This sharing results in varying numbers of networks being trained.

As shown in Fig. 7, the experimental outcomes under different sharing configurations are presented. The experiments are conducted in a 3.5 km by 3.5 km environment with 18 UAVs deployed. In the experiments, agents are divided into four groups, with partial policy sharing applied within each group. As a result, the number of policies to be trained in the MARL framework gradually decreases from 18 (no sharing) to 4 (full sharing within each group). To ensure statistical reliability, each sharing configuration is evaluated through three independent experimental runs. The results clearly demonstrate that an increase in the number of policies leads to a longer training duration, yet yields a marked improvement in overall system performance. As the number of trained policies increases from 4 to 18, the system exhibits consistent performance gains. UE coverage improves from 45% to 65%, while the average data rate rises from 5.1 Mbps to 7.4 Mbps. The proportion of available UAVs also grows steadily, reaching approximately 98% with 18 policies. However, as the number of networks rises from 4 to 18, the increasing volume of trainable network parameters leads to a longer training duration, extending from 20 hours to 40 hours.

![](images/a71ed4c68269acdbed32910d466c910f4eb91c18626d880f9d6d06657193d957.jpg)  
(a)

![](images/1de6d72814e091edc985f9f477fbbfab0691469dae9a51f9dcf6d77c89ba9708.jpg)  
(b)

![](images/1efc71467f43db8f699f3db6d1337eb877edeeb57e42886223d85c464a0d6d74.jpg)  
(c)  
Fig. 7. Experimental analysis of the impact of policy sharing on algorithm training performance. (a) Connected UE proportion versus training time. (b) Average data rate versus training time. (c) Available UAV ratio versus training time. Each dot represents an individual experimental result, where the color indicates the number of trained policies and the circle size reflects the relative magnitude of the standard deviation.

Overall, the experimental results reveal a consistent trend across the three metrics: as the number of training strategies increases, both the training duration and performance improve significantly. This indicates that policy sharing within groups leads to a reduction in the diversity of UAV strategies. In scenarios involving large exploration spaces and dynamic UAV roles, maintaining strategy diversity proves crucial for enhancing the networking performance of the algorithm. It is clear that a balance between training efficiency and algorithm performance needs to be considered during the learning process.

## E. Simulation Results

This section presents the experimental results of the proposed MRLMN algorithm within a simulated environment. In Fig. 8, a total of 18 UAVs are deployed. Fig. 8(a) illustrates the initial configuration at the start of the simulation. As the simulation progresses, UAV trajectories are dynamically planned by the MARL-trained policies, while UEs move randomly within the environment. Gradually, a multi-hop UAV network emerges and evolves, exhibiting enhanced connectivity over time. By the final stage, shown in Fig. 8(d), the network establishes robust communication links with the majority of UEs. These results demonstrate the MRLMN algorithm’s strong capability for multi-hop networking, ensuring both high connectivity and stability in dynamic UAV networking scenarios.

![](images/dd2a6e691ecf4a3cd82a656f4d78894da7300ecc10053ae428addb1531851d35.jpg)  
(a) t=1

![](images/36712d4d8392c079d28643c6c0fd63008a7d3ea064820bf40a10d79970ba78c0.jpg)  
(b) t=100

![](images/98ee2c85a17cab518db24cef1e268c80719d53dddf526baa9d4e22fcb7d49b8a.jpg)  
(c) t=200

![](images/f69d5766468868a490d3821f4165558ca7bc0d8f8ef8e9eaf864f831c428350f.jpg)  
(d) t=400  
Fig. 8. Simulation results of the proposed algorithm within a single episode. Each figure shows the states of the nodes and the UAV network topology, with the evaluation metrics at the current time step displayed below. Three representative UAVs are highlighted using a darker shade, and their trajectories over 100 time steps are depicted by pink paths.

## VI. CONCLUSION

This paper introduces the MRLMN framework, which integrates MARL and LLMs to optimize UAV networking in disaster response scenarios. To address the scalability of the networking problem and enhance coordination among UAVs, the framework incorporates agent grouping and reward decomposition modules. Behavioral constraints based on the grouping mechanism are further applied to ensure robust and stable network formation. Additionally, a knowledge distillation approach enables the transfer of high-level decision-making capabilities from LLMs to MARL agents, accelerating training and improving exploration efficiency. Simulation results demonstrate substantial performance gains in large-scale dynamic environments, confirming the adaptability and effectiveness of the proposed framework across diverse configurations. Future research directions include incorporating practical constraints such as UAV energy consumption, network load balancing, and UAV replacement mechanisms to ensure continuous and reliable operations in large-scale deployments. Enhancing communication reliability through interference management and physical-layer optimization can further support the efficient implementation of multi-hop aerial networks. At the same time, deeper integration of LLMs with MARL, for example, by replacing conventional MARL policies with more expressive decision models, has the potential to improve scalability and adaptability in complex environments. Complementing these developments with validation in real-world deployments would provide valuable insights into the operational feasibility and robustness of the proposed framework.

## REFERENCES

[1] NOAA National Centers for Environmental Information (NCEI), “U.S. billion-dollar weather and climate disasters,” 2025. [Online]. Available: https://www.ncei.noaa.gov/access/billions/

[2] L. Gupta, R. Jain, and G. Vaszkun, “Survey of important issues in UAV communication networks,” IEEE Commun. Surveys Tuts., vol. 18, no. 2, pp. 1123–1152, Secondquarter 2016.

[3] B. Li, Z. Fei, and Y. Zhang, “UAV communications for 5G and beyond: Recent advances and future trends,” IEEE Internet Things J., vol. 6, no. 2, pp. 2241–2263, Apr. 2019.

[4] C. Dai, K. Zhu, and E. Hossain, “Multi-agent deep reinforcement learning for joint decoupled user association and trajectory design in full-duplex multi-UAV networks,” IEEE Trans. Mobile Comput., vol. 22, no. 10, pp. 6056–6070, Oct. 2023.

[5] S. Khairy, P. Balaprakash, L. X. Cai, and Y. Cheng, “Constrained deep reinforcement learning for energy sustainable multi-UAV based random access iot networks with NOMA,” IEEE J. Sel. Areas Commun., vol. 39, no. 4, pp. 1101–1115, Apr. 2021.

[6] S. Cheng, X. Lin, X. Li, and J. Wang, “Joint UAV trajectory and radcom task schedule for IVNs: A game-embedding multi-agent deep reinforcement learning approach,” IEEE Trans. Wireless Commun., vol. 24, no. 1, pp. 181–196, Jan. 2025.

[7] C. H. Liu, Z. Chen, and Y. Zhan, “Energy-efficient distributed mobile crowd sensing: A deep learning approach,” IEEE J. Sel. Areas Commun., vol. 37, no. 6, pp. 1262–1276, Jun. 2019.

[8] J. Ji, K. Zhu, and L. Cai, “Trajectory and communication design for cache- enabled UAVs in cellular networks: A deep reinforcement learning approach,” IEEE Trans. Mobile Comput., vol. 22, no. 10, pp. 6190–6204, Oct. 2023.

[9] X. Zhang, H. Zhao, J. Wei, C. Yan, J. Xiong, and X. Liu, “Cooperative trajectory design of multiple UAV base stations with heterogeneous graph neural networks,” IEEE Trans. Wireless Commun., vol. 22, no. 3, pp. 1495–1509, Mar. 2023.

[10] D.-H. Tran, T. X. Vu, S. Chatzinotas, S. ShahbazPanahi, and B. Ottersten, “Coarse trajectory design for energy minimization in UAV-enabled,” IEEE Trans. Veh. Technol., vol. 69, no. 9, pp. 9483–9496, Sep. 2020.

[11] C. Deng, W. Xu, C.-H. Lee, H. Gao, W. Xu, and Z. Feng, “Energy efficient UAV-enabled multicast systems: Joint grouping and trajectory optimization,” in Proc. 2019 IEEE Glob. Commun. Conf., 2019, pp. 1–7.

[12] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.

[13] F. Fazel, J. Abouei, M. Jaseemuddin, A. Anpalagan, and K. N. Plataniotis, “Secure throughput optimization for cache-enabled multi-UAVs networks,” IEEE Internet Things J., vol. 9, no. 10, pp. 7783–7801, May 2022.

[14] C. Wang, D. Zhai, R. Zhang, G. Kaddoum, and S. Singh, “Energy consumption minimization in dynamic UAV-assisted mobile edge computing networks,” in Proc. IEEE Int. Conf. Commun., 2023, pp. 4671–4676.

[15] Y. A. Sambo, P. V. Klaine, J. P. B. Nadas, and M. A. Imran, “Energy minimization UAV trajectory design for delay-tolerant emergency communication,” in Proc. 2019 IEEE Int. Conf. Commun. Workshops, 2019, pp. 1–6.

[16] J. Yao and N. Ansari, “QoS-Aware power control in Internet of Drones for data collection service,” IEEE Trans. Veh. Technol., vol. 68, no. 7, pp. 6649–6656, Jul. 2019.

[17] M. Samir, S. Sharafeddine, C. M. Assi, T. M. Nguyen, and A. Ghrayeb, “UAV trajectory planning for data collection from time-constrained IoT devices,” IEEE Trans. Wireless Commun., vol. 19, no. 1, pp. 34–46, Jan. 2020.

[18] L. Wang, K. Wang, C. Pan, W. Xu, N. Aslam, and L. Hanzo, “Multi-agent deep reinforcement learning-based trajectory planning for multi-UAV assisted mobile edge computing,” IEEE Trans. Cogn. Commun. Netw., vol. 7, no. 1, pp. 73–84, Mar. 2021.

[19] O. Vinyals et al., “Grandmaster level in Starcraft II using multi-agent reinforcement learning,” Nature, vol. 575, no. 7782, pp. 350–354, 2019.

[20] W. Zhang, Q. Wang, X. Liu, Y. Liu, and Y. Chen, “Three-dimension trajectory design for multi-UAV wireless network with deep reinforcement learning,” IEEE Trans. Veh. Technol., vol. 70, no. 1, pp. 600–612, Jan. 2021.

[21] E. Catté, M. Sana, and M. Maman, “Dual-attention deep reinforcement learning for multi-map 3D trajectory optimization in dynamic 5G networks,” in Proc. IEEE Int. Conf. Commun., 2023, pp. 6417–6422.

[22] R. Ding, F. Gao, and X. S. Shen, “3D UAV trajectory design and frequency band allocation for energy-efficient and fair communication: A deep reinforcement learning approach,” IEEE Trans. Wireless Commun., vol. 19, no. 12, pp. 7796–7809, Dec. 2020.

[23] F. Song et al., “Evolutionary multi-objective reinforcement learning based trajectory control and task offloading in UAV-assisted mobile edge computing,” IEEE Trans. Mobile Comput., vol. 22, no. 12, pp. 7387–7405, Dec. 2023.

[24] F. Christianos, G. Papoudakis, M. A. Rahman, and S. V. Albrecht, “Scaling multi-agent reinforcement learning with selective parameter sharing,” in Proc. 38th Int. Conf. Mach. Learn., M. Meila and T. Zhang, Eds., Jul. 2021, vol. 139, pp. 1989–1998. [Online]. Available: https://proceedings.mlr. press/v139/christianos21a.html

[25] C. Yu, A. Velu, E. Vinitsky, Y. Wang, A. M. Bayen, and Y. Wu, “The surprising effectiveness of PPO in cooperative multi-agent games,” in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022, pp. 24611–24624. [Online]. Available: https://api.semanticscholar.org/CorpusID:232092445

[26] Y. He, Y. Gan, H. Cui, and M. Guizani, “Fairness-based 3-D multi-UAV trajectory optimization in multi-UAV-assisted MEC system,” IEEE Internet Things J., vol. 10, no. 13, pp. 11383–11395, Jul. 2023.

[27] Y. Qin, Z. Zhang, X. Li, W. Huangfu, and H. Zhang, “Deep reinforcement learning based resource allocation and trajectory planning in integrated sensing and communications UAV network,” IEEE Trans. Wireless Commun., vol. 22, no. 11, pp. 8158–8169, Nov. 2023.

[28] J. Ren, Y. Xu, Z. Li, C. Hong, X.-P. Zhang, and X. Chen, “Scheduling UAV swarm with attention-based graph reinforcement learning for ground-to-air heterogeneous data communication,” in Proc. Adjunct Proc. ACM Int. Joint Conf. Pervasive Ubiquitous Comput. 2023 ACM Int. Symp. Wearable Comput., New York, NY, USA, 2023, pp. 670–675, doi: 10.1145/3594739.3612905.

[29] B. Yu, H. Kasaei, and M. Cao, “Co-NAVGPT: Multi-robot cooperative visual semantic navigation using large language models,” 2023, arXiv:2310.07937.

[30] G. Wang et al., “Voyager: An open-ended embodied agent with large language models,” Trans. Mach. Learn. Res., 2024.

[31] Z. Zhou, B. Hu, C. Zhao, P. Zhang, and B. Liu, “Large language model as a policy teacher for training reinforcement learning agents,” in Proc. 33rd Int. Joint Conf. Artif. Intell., 2024, pp. 5671–5679.

[32] X. Xiang, J. Xue, L. Zhao, Y. Lei, C. Yue, and K. Lu, “Real-time integration of fine-tuned large language model for improved decision-making in reinforcement learning,” in Proc. 2024 Int. Joint Conf. Neural Netw., 2024, pp. 1–8.

[33] Y. Xu, Z. Jian, J. Zha, and X. Chen, “Emergency networking using UAVs: A reinforcement learning approach with large language model,” in Proc. 23rd ACM/IEEE Int. Conf. Inf. Process. Sens. Netw., 2024, pp. 281–282.

[34] Y. Du et al., “Guiding pretraining in reinforcement learning with large language models,” in Proc. 40th Int. Conf. Mach. Learn. Proc. Mach. Learn. Res., A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett, Eds., Jul. 2023, vol. 202, pp. 8657–8677. [Online]. Available: https://proceedings.mlr.press/v202/du23f.html

[35] B. Wang et al., “LLM-empowered state representation for reinforcement learning,” in Proc. 41st Int. Conf. Mach. Learn., Ser. Proc. Mach. Learn. Res., R. Salakhutdinov, Z. Kolter, K. Heller, A. Weller, N. Oliver, J. Scarlett, and F. Berkenkamp, Eds., vol. 235. PMLR, 21–27 Jul. 2024, pp. 51348–51375. [Online]. Available: https://proceedings.mlr. press/v235/wang24bh.html

[36] W. Wang, I. Obi, and B.-C. Min, “SRLM: Human-in-loop interactive social robot navigation with large language model and deep reinforcement learning,” 2024, arXiv:2403.15648.

[37] C. Zhao et al., “Flight dynamics to sensing modalities: Exploiting drone ground effect for accurate edge detection,” 2025, arXiv:2509.21085.

[38] A. Hussain, S. Li, T. Hussain, X. Lin, F. Ali, and A. A. AlZubi, “Computing challenges of UAV networks: A comprehensive survey.,” Comput., Mater. Continua, vol. 81, no. 2, pp. 1999–2051, 2024.

[39] M. B. Bezziane, Y. Sahraoui, B. Brik, L. Mekkas, S. Bougeurra, and A. Khaldi, “On the performance evaluation of mobility model-based GPSR routing protocol in flying ad hoc networks,” in Proc. 6th Int. Conf. Pattern Anal. Intell. Syst., 2024, pp. 1–7.

[40] Y. Xu, J. Zha, J. Ren, X. Jiang, H. Zhang, and X. Chen, “Scalable multi-agent reinforcement learning for effective UAV scheduling in multi-hop emergency networks,” in Proc. 30th Annu. Int. Conf. Mobile Comput. Netw., New York, NY, USA, 2024, pp. 2028–2033, doi: 10.1145/3636534.3694730.

[41] J.-H. Kim, M.-C. Lee, and T.-S. Lee, “Generalized UAV deployment for UAV-assisted cellular networks,” IEEE Trans. Wireless Commun., vol. 23, no. 7, pp. 7894–7910, Jul. 2024.

[42] H. Chen, Y. Lin, M. Fu, L. Yao, and M. Sheng, “A survey on reinforcement learning methods for UAV systems,” ACM Comput. Surv., vol. 58, no. 4, pp. 1–37, 2025.

[43] J. Zha, N. Zhou, Z. Liu, T. Sun, and X. Chen, “Diffusion-based filter for fast and accurate collaborative tracking with low data transmission,” Authorea Preprints, 2024.

[44] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” 2017, arXiv:1707.06347.

[45] C. S. de Witt et al., “Is independent learning all you need in the Starcraft multi-agent challenge?,” 2020, arXiv:2011.09533.

[46] J. Wei et al., “Chain of thought prompting elicits reasoning in large language models,” Adv. Neural Inform. Process. Syst., vol. 35, pp. 24824– 24837, 2022.

[47] Y. Sun, J. Hu, W. Cheng, and H. Chen, “DFA-RAG: Conversational semantic router for large language model with definite finite automaton,” in Proc. 41st Int. Conf. Mach. Learn. Proc. Mach. Learn. Res., R. Salakhutdinov, Z. Kolter, K. Heller, A. Weller, N. Oliver, J. Scarlett, and F. Berkenkamp, Eds., Jul. 2024, vol. 235, pp. 47033–47055. [Online]. Available: https://proceedings.mlr.press/v235/sun24e.html

[48] S. Yao et al., “React: Synergizing reasoning and acting in language models,” in Proc. 11th Int. Conf. Learn. Representations., 2023.

[49] W. Song, Z. Li, L. Zhang, H. Zhao, and B. Du, “Sparse is enough in fine-tuning pre-trained large language models,” in Proc. 41st Int. Conf. Mach. Learn., 2024, pp. 46121–46135.

[50] N. Carion, F. Massa, G. Synnaeve, N. Usunier, A. Kirillov, and S. Zagoruyko, “End-to-end object detection with transformers,” in Proc. Eur. Conf. Comput. Vis., 2020, pp. 213–229.

[51] G. Hinton, O. Vinyals, and J. Dean, “Distilling the knowledge in a neural network,” in Proc. NIPS Deep Learn. Representation Learn. Workshop, 2015.

[52] O. (2024), “GPT-4O system card,” 2024, Accessed: Dec. 06, 2025. [Online]. Available: https://openai.com/research/gpt-4o-system-card

[53] K. Li, W. Ni, X. Yuan, A. Noor, and A. Jamalipour, “Deep-graph-based reinforcement learning for joint cruise control and task offloading for aerial edge Internet of Things (EdgeIoT),” IEEE Internet Things J., vol. 9, no. 21, pp. 21676–21686, Nov. 2022.

[54] V. Mnih et al., “Asynchronous methods for deep reinforcement learning,” in Proc. Int. Conf. Mach. Learn., 2016, pp. 1928–1937.

![](images/a290df7651828fed3d986d6045ec9590feb6b89f044192fc70a5494c765fc2fe.jpg)  
Yanggang Xu was born in Sichuan, China, in 1999. He received the BEng degree in communication engineering from the University of Electronic Science and Technology of China (UESTC), Chengdu, China, the BEng degree in electronics and electrical engineering from the University of Glasgow, Glasgow, U.K., in 2022, and the MS degree in data science and information technology from Tsinghua University, Shenzhen, China, in 2025. He is currently with Tencent, Shenzhen, China. His research interests include reinforcement learning, large language models,

multi-agent systems, robotics, and artificial intelligence.

![](images/1a4b2f50f7183eb3e7dc1dae4acfd439fa449ae238a0dab197355ea80b1dea16.jpg)

Jirong Zha received the BS and MS degrees from Beihang University, China, in 2020 and 2023, respectively. She is currently working toward the PhD degree in data science and information technology from Tsinghua University, China. Her research interests include collaborative perception, large language models, multi-agent systems, and distributed state estimation.

Jianfeng Zheng received the BE degree in art and design from Guangxi Minzu University, China, in 2015. He is currently a project manager with Shenzhen Smart City Communication Company, Ltd., Shenzhen, China. His research interests include smart city systems, intelligent transportation, IoT-based sensing, and large-scale system integration.

![](images/56da22e3713383d9fbc227ddd3f03441f946ec7178741fd2f91e8b9a3988a015.jpg)

Weijie Hong received the BS degree in information and computing science from the South China University of Technology, in 2009. He is currently working toward the master’s degree with Tsinghua University. He is also Ltd., and the director with the Guangdong Engineering Technology Research Center for Multimodal Fusion Communication and IoT Sensing. His research interests include AI-IoT, computing power networks, Optical networks, and Low-Altitude Communications.

Xiangmin Yi received the BE degree from the School of Artificial Intelligence, Beijing University of Posts and Telecommunications, Beijing, China, in 2025. He is currently working toward the MS degree with the Tsinghua Shenzhen International Graduate School, Tsinghua University, Shenzhen, China. His research interests include artificial intelligence, large language models, and reinforcement learning.

![](images/62950db96d4b4a5a379689c04e331c297bd0ae30e3b3198eb07137c87555fa98.jpg)

![](images/fd695bc87d82dab641cc84dfc1922e42b2a06765e592789de91febf92fbd2463.jpg)

Geng Chen has been working toward the Undergraduate degree majoring in software engineering with Jilin University, since 2022. His research interests include reinforcement learning and multimodal large language models.

![](images/5581120ae33547027c16faf25c39f316a676a53a484df939a38af5faf064272d.jpg)

![](images/fa564b8f64118c773b80dfd32bfe33394a9862066a8f55da2e709243052099cf.jpg)

Chen-Chun Hsia received the BE degree from the National Cheng Kung University, Tainan, Taiwan, in 2021, and the MS degree from the Shenzhen International Graduate School, Tsinghua University, Shenzhen, China, in 2024. He is currently an ML engineer with Ant Group (Alipay), working on large-scale recommendation retrieval and merchant intelligence systems for payment growth. His interests include representation learning, multimodal real-time generative systems, and end-to-end ML deployment.

![](images/2ed162fe73f053051619aa74b0348a7dfa55be0f362d3c28b4f53c5083fbfb59.jpg)

Xinlei Chen (Member, IEEE) is currently an associate professor with Shenzhen International Graduate School, Tsinghua University. His research interests include mobile sensing and embodied AI. Dr. Chen was the recipient of the several awards from top-tier conference and been selected in Elsevier’s Global Top 2% Scientists List in the past three years.