# Correspondence

# RL-Based Cargo-UAV Trajectory Planning and Cell Association for Minimum Handoffs, Disconnectivity, and Energy Consumption

Nesrine Cherif , Wael Jaafar , Senior Member, IEEE, Halim Yanikomeroglu , Fellow, IEEE, and Abbas Yongacoglu , Life Senior Member, IEEE

Abstract—Unmanned aerial vehicle (UAV) is a promising technology for last-mile cargo delivery. However, the limited on-board battery capacity, cellular unreliability, and frequent handoffs in the airspace are the main obstacles to unleash its full potential. Given that existing cellular networks were primarily designed to service ground users, re-utilizing the same architecture for highly mobile aerial users, e.g., cargo-UAVs, is deemed challenging. Indeed, to ensure a safe delivery using cargo-UAVs, it is crucial to utilize the available energy efficiently, while guaranteeing reliable connectivity for command-and-control and avoiding frequent handoff. To achieve this goal, we propose a novel approach for joint cargo-UAV trajectory planning and cell association. Specifically, we formulate the cargo-UAV mission as a multi-objective problem aiming to 1) minimize energy consumption, 2) reduce handoff events, and 3) guarantee cellular reliability along the trajectory. We leverage reinforcement learning (RL) to jointly optimize the cargo-UAV’s trajectory and cell association. Simulation results demonstrate a performance improvement of our proposed method, in terms of handoffs, disconnectivity, and energy consumption, compared to benchmarks.

Index Terms—Cargo-UAV, cell association, energy consumption, handoff, reinforcement learning.

## I. INTRODUCTION

Cargo unmanned aerial vehicles (cargo-UAVs) are beginning to grab a portion of the worldwide delivery market over many industries due to their increased flexibility and mobility. For instance, Amazon Prime Air service is under development for beyond visual line-of-sight (BVLoS) operations. In August 2021, Amazon got the approval of the federal aviation administration (FAA) to operate its UAV fleet. With this milestone, cargo-UAV based delivery is expected to increase in the near future. Hence, cargo-UAV safety and security are paramount for the roll-out of aerial delivery and its public acceptance [1]. To ensure a safe operation at BVLoS, reliable and permanent command and control (C&C) communications are crucial for cargo-UAVs [2]. Specifically, cellular networks are required to be highly available, reliable, and secure to satisfy C&C requirements. The viability and feasibility of BVLoS cellular-connected UAVs have been examined in several works [3], [4], [5]. However, re-utilizing existing cellular infrastructures for aerial operations brings challenges such as unreliable radio links due for instance to down-tilted antennas of terrestrial base stations (BSs) [6]. Besides, the mobility inheritance of cargo-UAVs may lead to frequent switching from one serving cell to another, a.k.a. handoff, hence, resulting in more signaling overhead that degrades the radio link’s quality.

To guarantee cellular link reliability and reduce latency in terrestrial networks, authors of [7] proposed a deep learning-based handoff prediction strategy for millimiter wave communications. For cellularconnected UAVs, several works focused on optimizing UAV trajectories for BVLoS operations. For instance, in [8], the authors set up a testbed for UAV missions. The performance of such a system was evaluated in [9] in terms of radio link failure and handoff rate. Moreover, the authors of [10] proposed a reinforcement learning (RL) based algorithm that balances between handoff rate and radio link quality for a pre-known UAV trajectory. Finally, we investigated for the first time in [11] cargo-UAV trajectory planning with consideration for energy consumption, communication link disconnectivity, and handoffs. We proposed dynamic programming-based path planning and studied the impact of parameters such as disconnectivity and handoff rates, and impact of BSs’ distribution on energy consumption.

To the best of our knowledge, only [11] examined cargo-UAV trajectory planning from the viewpoints of energy consumption, cellular connection dependability, and handoff, together. However, the suggested solution there neglected the issue of cell affiliation and presupposed that the cargo-UAV is always linked with the cell with the strongest signal, which may result in frequent handoffs. Consequently, we propose in this work a novel algorithm for joint trajectory planning and cell association that aims to minimize energy consumption and number of handoff events leveraging RL, while guaranteeing a reliable communication link with the terrestrial network. It is noteworthy that the reliability of a communication link can be evaluated in terms of cellular disconnectivity time during the cargo-UAV mission.

The remaining of the article is organized as follows. Section II presents the system model. In Section III, we formulate the related problem. Section IV details the proposed RL-based trajectory planning and cell association algorithm for cargo-UAVs, while simulation results are discussed in Section V. Finally, Section VI concludes the article.

## II. SYSTEM MODEL

We consider a 3-dimensional (3D) geographical area in the airspace of the city of Leuven, Belgium, centered at coordinates 50<sup>◦</sup>52’45.3”N 4<sup>◦</sup>42’08.1”E, based on a Cartesian coordinates system $( x , y , z )$ . It is important to highlight that the data herein was generated using the same real data simulator mentioned in [12]. We assume that a cargo-UAV is deployed to deliver an item from a retailer warehouse with coordinates $\mathbf { q } _ { w } = ( x _ { w } , y _ { w } , 0 )$ to a preset drop-off location $\mathbf q _ { d } = ( x _ { d } , y _ { d } , 0 )$ where the customer is expected to pick it up, e.g., at a community drop-off location or the private customer’s porch [1]. The cargo-UAV is expected only to travel either vertically, i.e., at fixed (x, y), or horizontally, i.e., at fixed altitude z <sub>=</sub> h. To safely execute its mission, the cargo-UAV relies on cellular connectivity of the existing terrestrial network for C&C exchanges with a central unit on the ground.

![](images/232eb48b5d2c7cfee98fa87a52858cde1e8ff2a88416c08e77651a359991e594.jpg)  
Fig. 1. Maximum RSRP heatmap of a part of the city of Leuven, Belgium, for different cargo-UAV altitudes (Area is $3 \times 3 \mathrm { k m } ^ { 2 }$ and $f _ { c } = 1 . 8 \ : \mathrm { G H z } ) \ : [ 1 2 ]$

## A. Channel Model

The air-to-ground (A2G) communication channel model has been defined by the 3 rd Generation Partnership Project (3GPP). It encompasses the BS’s antenna gain, LoS probability, and pathloss expressions. For further details on the adopted A2G channel model and its components, we kindly refer the reader to [11, Section II-A].

## B. Received Power Expression

Based on the channel model and assuming that the cargo-UAV is equipped with an omni-directional antenna with unit gain, the average received power from the $i ^ { t h }$ cell, i.e., the Reference Signal Received Power (RSRP), is given by

$$
P _ { r , i } = P _ { T } + G _ { i } - L _ { i } , \forall i = 1 , \ldots , M ,\tag{1}
$$

where $P _ { T }$ is the transmit power of any ground cell in dBm. $G _ { i }$ is the array radiation pattern of the $i ^ { t h }$ cell given by [11, eq.(5)], and $L _ { i }$ is the average pathloss of the channel between the cargo-UAV and the $i ^ { t h }$ cell highlighted in [11, eq.(7)]. Finally, M is the total number of cells in the area. For the sake of simplicity, we assume that frequency planning is orthogonal and optimal, thus eliminating inter-cell interference at cargo-UAVs. Accordingly, the reliability of cellular connectivity depends on the level of RSRP at any potential location in the airspace. For illustrative purposes, we present in Fig. 1 the maximum RSRP level at each grid point of the $( x , y )$ plane at different flying altitudes $h \in \{ 2 0 , 4 0 , 8 0 , 1 2 0 \}$ meters. At low altitudes, e.g., $h = 2 0$ meters, scattered coverage holes are more frequent than for $h = 4 0$ meters. This is due to the presence of more blockages such as buildings, trees, etc., in the Leuven urban area. In contrast, at elevated altitudes, high pathloss coupled with the down-tilt of terrestrial-BS’ antennas weaken extensively the signal strength, thus resulting in more coverage holes areas, as shown for instance at $h = 1 2 0$ meters.

Leveraging the data presented in Fig. 1, the cargo-UAV is considered disconnected when, at its actual location, no cell can guarantee an RSRP equal or higher than a pre-defined RSRP threshold, denoted $T _ { \mathrm { t h } } ^ { 1 } { } ^ { 1 }$ Moreover, a handoff event occurs when the cargo-UAV is associated with a different cell than the previous one to which it was connected. During a cargo-UAV mission, it is important to trigger seldom handoff events, as the latter would destabilize the C&C link and generate an additional amount of overhead data.

## C. Cargo-UAV Energy Consumption Model

The cargo-UAV energy consumption depends on its size, weight, and power, along its movement and communication regimes [13]. It consists of the propulsion energy and the communication energy. Typically, communication energy is very small compared to the propulsion energy, and thus, can be neglected. Using a rotary-wing cargo-UAV, the propulsion energy to fly for a distance d is

$$
E ( v , d ) = P _ { \mathrm { p r o p } } ( v ) d / v , v > 0 ,\tag{2}
$$

where $P _ { \mathrm { p r o p } } ( v )$ is the propulsion power given by [11, eq.(10)] and v is the cargo-UAV velocity. Let $E _ { C }$ and $E _ { S }$ be the initial cargo-UAV energy capacity and emergency reserve energy, respectively. $E _ { C }$ is available for the mission, while $E _ { S }$ is used for emergency pull-backs. Hence, the cargo-UAV’s available energy to travel between the departure and arrival locations is

$$
E _ { A } ( v , h ) = E _ { C } - E _ { S } - 2 E ( v , h ) ,\tag{3}
$$

where $E ( v , h )$ is the required energy to take-off from the dockstation or to land on the drop-off location.

## III. PROBLEM FORMULATION

The cargo-UAV is required to deliver a package from the retailer warehouse (at coordinates $\mathbf { q } _ { w } )$ to a consumer drop-off location (at coordinates $\mathbf { q } _ { d } )$ . Our objective is to achieve this mission while consuming minimum energy, triggering minimum handoff events, while keeping a reliable communication.

Let $\mathcal { T } = \{ \mathbf { q } _ { 1 } , \dots , \mathbf { q } _ { | T | } \}$ be the trajectory of the cargo-UAV, defined by the locations $\mathbf { q } _ { i } = ( x _ { i } , y _ { i } , h )$ . Also, let $\mathcal { C } = \{ c _ { 1 } , \ldots , c _ { | T | } \}$ be the set of cell IDs associated to the cargo-UAV locations in T, where $c _ { i } \in$ $\{ 1 , \ldots , M \}$ . It is noteworthy that at any grid location in the 2D plane at altitude h, the cargo-UAV receives RSRP measurement reports from all potential serving cells. Finally, we assume that the set of experienced RSRPs along the trajectory are represented by $\mathcal { R } = \{ r _ { 1 } , \ldots , r _ { | T | } \}$ Hence, the joint trajectory planning and cell association problem can be formulated as follows:

$$
\begin{array} { r l } { \displaystyle \mathrm { P 1 } : \operatorname* { m i n } _ { \mathcal { T } , \mathcal { C } } } & { { } w _ { \mathrm { e n } } \displaystyle \sum _ { i = 1 } ^ { | \mathcal { T } | - 1 } E ( v , d _ { i , i + 1 } ) + w _ { \mathrm { s i g } } \displaystyle \sum _ { i = 1 } ^ { | \mathcal { T } | - 1 } \mathcal { D } ( d _ { i , i + 1 } ) } \\ { + } & { { } w _ { \mathrm { h o } } \displaystyle \sum _ { i = 1 } ^ { | \mathcal { T } | - 1 } \eta _ { i , i + 1 } } \end{array}\tag{P1}
$$

$$
\mathrm { s . t . } \sum _ { i = 1 } ^ { | T | - 1 } E ( v , d _ { i , i + 1 } ) \leq E _ { A } ( v , h ) ,\tag{P1.a}
$$

$$
\mathbf { q } _ { 1 } = \mathbf { q } _ { w } , \mathrm { ~ a n d ~ } \mathbf { q } _ { \parallel T | } = \mathbf { q } _ { d } ,\tag{P1.b}
$$

where $w _ { \mathrm { x } } , \mathrm { x } \in \{ \mathrm { e n } , \mathrm { s i g } , \mathrm { h o } \}$ are the weights describing the importance given to each metric, energy consumption, radio link disconnectivity and handoffs, respectively, such that $w _ { \mathrm { e n } } + w _ { \mathrm { s i g } } + w _ { \mathrm { h o } } = 1$ . We have $d _ { i , i + 1 } = \| \mathbf { q } _ { i } - \mathbf { q } _ { i + 1 } \|$ , and $\begin{array} { r } { D ( d _ { i , i + 1 } ) = d _ { i , i + 1 } \mathrm { ~ i f ~ } P _ { r , i } < T _ { \mathrm { t h } } } \end{array}$ and $P _ { r , i + 1 } < T _ { \mathrm { t h } } ;$ and $\mathcal { D } ( d _ { i , i + 1 } ) = 0$ otherwise. $\mathcal { D } ( d _ { i , i + 1 } )$ indicates a travelled distance in a coverage hole, i.e., without connectivity. Finally variable $\eta _ { i , i + 1 }$ reflects the handoff event, i.e., $\eta _ { i , i + 1 } = 1 \mathrm { i f } \ c _ { i } \neq c _ { i + 1 }$ and $\eta _ { i , i + 1 } = 0$ otherwise.

A capacitated vehicle routing problem (CVRP) can be used to describe problem (P1) [14]. Indeed, the CVRP is defined as choosing a vehicle’s route with the goal of reducing its overall transport expenses. Logically, the cargo-UAV and its costs in terms of energy consumption, disconnectivity, and handoffs in our system, may be assimilated to the $\mathrm { C V R P } \mathrm { s }$ vehicle and transportation costs, respectively. Given that the CVRP is known to be an NP-hard problem [14], then, by restriction, problem (P1) is also NP-hard.

## IV. PROPOSED RL-BASED TRAJECTORY PLANNING AND CELL ASSOCIATION

To solve the cargo-UAV constrained trajectory planning and cell association problem, we propose here an RL-based approach. First, we briefly overview the adopted RL method. Then, the framework for the proposed RL-based trajectory planning and cell association algorithm, including the definition of states, actions, and rewards are detailed.

## A. RL Background

In RL, an agent, i.e., the cargo-UAV, interacts with its environment, i.e., the airspace. Specifically, it executes an action given its current state and the anticipated future reward. At an instant t, the agent in state s takes an action a. Based on $( s , a )$ , the agent receives a reward $\rho .$ The process is iteratively repeated to maximize the expected reward over time and reach the end of the mission. The RL algorithm can be presented as a Markov decision process (MDP) defined by the $( S , \mathcal { A } , \mathcal { P } _ { s a } , \beta , \mathcal { W } )$ where the set of states is encompassed in $s , { \mathcal { A } }$ is the set of actions. Moreover, $\mathcal { P } _ { s a }$ is the state transition probability of a state $s \in S$ and an action $a \in \mathcal { A } . \ \beta \in [ 0 , 1 )$ is the discount factor. Finally, the reward function of a pair of state-action is W. The optimal policy of the MDP aims to maximize the sum of discounted rewards by associating an optimal action to each state. We adopt here Q-learning to learn the optimal policy for the $\mathrm { { \mathbf { M D P } } } ^ { 2 }$ . The optimal policy adopted by the agent is the set of actions per state with the highest Q-values. The Q-value is given by the Bellman equation as

$$
Q _ { t + 1 } ( s , a ) = ( 1 - \alpha ) Q _ { t } ( s , a ) + \alpha \left[ \mathcal { W } _ { t + 1 } + \beta \operatorname* { m a x } _ { a \prime \in \mathcal { A } } Q _ { t } ( s ^ { \prime } , a ^ { \prime } ) \right] ,\tag{5}
$$

where $Q _ { t } ( s , a )$ is the Q-value for $( s , a )$ pair at episode (or time instant) $t , \alpha$ is the learning rate, $\mathcal { W } _ { t + 1 }$ is the reward of episode $t + 1$ , and $Q _ { t } ( s ^ { \prime } , a ^ { \prime } )$ is the Q-value for state-action $( s ^ { \prime } , a ^ { \prime } )$ in episode t.

## B. Proposed RL-Based Solution

We present here the proposed RL-based trajectory planning and cell association approach to solve problem (P1). The RL agent hosted by the cargo-UAV periodically collects its state. Then, it determines the best action, in terms of motion and cell association, and performs it. The state, action and reward of the RL agent are defined as follows:

Cargo-UAV’s state is defined as $s = \{ \mathbf { q } _ { s } , c _ { s } \}$ where ${ \bf q } _ { s } =$ $( x _ { s } , y _ { s } , h )$ is the 3D location of the cargo-UAV in the airspace and $c _ { s } \in \mathcal { C }$ is the corresponding serving cell ID. In state s, an action a is drawn from action space A, which includes pairs of potential motion direction, i.e., east (E), west (W), norht (N), south (S), north-east (NE), north-west (NW), south-east (SE), and south-west (SW), and cell IDs. The reward function is designed from the objective function of (P1), such that energy consumption, handoffs, and disconnectivity are minimized. Specifically, we express the reward function as

$$
{ \mathcal W } ( s , a ) = w _ { \mathrm { e n } } W _ { \mathrm { m o } } ( s , a ) + w _ { \mathrm { s i g } } W _ { \mathrm { s i g } } ( s , a ) + w _ { \mathrm { h o } } W _ { \mathrm { h o } } ( s , a ) ,\tag{6}
$$

where

$$
W _ { \mathrm { m o } } = \left\{ \begin{array} { l l } { - 1 / \sqrt { 2 } } & { \mathrm { i f ~ m o t i o n ~ d i r e c t i o n \in \{ N , S , E , W \} ~ } } \\ { - 1 } & { \mathrm { o t h e r w i s e , } } \end{array} \right.\tag{7}
$$

is the UAV motion (i.e., energy consumption) penalty,

$$
W _ { \mathrm { h o } } = \left\{ \begin{array} { l l } { 0 } & { \mathrm { i f } c _ { s _ { t } } = c _ { s _ { t + 1 } } } \\ { - 1 } & { \mathrm { o t h e r w i s e } , } \end{array} \right.\tag{8}
$$

<sup>2</sup>Note that more recent and sophisticated RL methods than Q-learning can be explored to solve the developed problem. Such an effort is left within the scope of a future work.

Algorithm 1: Proposed RL-Based Solution.   
Input: Matrix H of size $( J \times J \times M ^ { \prime } )$ is the cellular connectivity   
heatmap at altitude h where J is the airspace grid length and   
width and $M ^ { \prime } < M$ is the number of cells with the highest   
RSRPs; step size; cargo-UAV speed $v ;$ RSRP threshold $T _ { \mathrm { t h } } ;$   
Available energy $E _ { A } ;$ starting location $\mathbf { q } _ { w } ;$ arrival location ${ \bf q } _ { d } .$   
Output: Optimal policy; Trajectory T; Serving cells C.   
1: Initialize Q-table matrix Q with size $( J \times J \times 8 \times M ^ { \prime } )$ with   
$8 \times M ^ { \prime }$ is the size of the action space A.   
2: while maximum number of episodes is not reached do   
3: Initialize $\mathcal { T } = \{ \mathbf { q } _ { 1 } \}$ and $\mathcal { C } = \{ c _ { 1 } \}$   
4: while destination is not reached do   
5: Generate $\kappa \in [ 0 , 1 ]$   
6: if $\kappa < \epsilon$ then   
7: Pick randomly an action from A.   
8: else   
9: Pick $a ^ { * } = \operatorname { a r g m a x } Q ( s , a )$   
$\stackrel { \smile } { a } \in \mathcal { A }$   
10: end if   
11: compute the reward $\mathcal { W } ( s , a )$ using (6).   
12: Update the Q-value for $( s , a )$ using (5).   
13: $\epsilon = \operatorname* { m a x } \{ \epsilon _ { \mathrm { m i n } } , \epsilon - \epsilon _ { \mathrm { d e c } } \}$ with $\epsilon _ { \mathrm { m i n } }$ is the minimum   
allowed value for  and $\epsilon _ { \mathrm { d e c } }$ is the decay for each taken   
action.   
14: end while   
15: end while   
16: Return best $( \mathcal { T } ^ { * } , \mathcal { C } ^ { * } )$

is the handoff cost, and the disconnectivity cost is given by

$$
W _ { \mathrm { s i g } } ( s , a ) = \left\{ \begin{array} { l l } { 0 } & { \mathrm { i f } \mathrm { R S R P } _ { c _ { s _ { t + 1 } } } \geq T _ { \mathrm { t h } } } \\ { - 1 } & { \mathrm { o t h e r w i s e } . } \end{array} \right.\tag{9}
$$

It is imperative to underscore that the weights employed in $( 6 ) , w _ { \mathrm { x } }$ $\mathrm { { x } \in \{ e n , \ s i g , \ h o \} }$ , with respect to each optimizing metric, namely, RSRP level, energy consumption, and handoff rate, primarily serve to elucidate the latter’s importance in the path planning of the cargo-UAV mission. For instance, the RSRP metric, which delineates the cellular link reliability, is expected to have the highest weight value in instances of disconnectivity, given that such occurrences are regarded as the most undesirable events, such as when the cargo-UAV loses connection and as a result it jeopardizes the safety of properties and individuals on the ground. Conversely, handoff events and, to a lesser extent, trajectory detours, are anticipated to receive lower weights compared to disconnectivity events. The RL agent should be trained for a sufficient number of episodes to understand the environment dynamics and improve its decision-making, thus reaching the destination in the most efficient way. The proposed RL-based algorithm is presented in Algorithm 1. Specifically, the RL agent begins with no knowledge about the environment, i.e., an empty Q-table for all state-action combinations. The action space A encompasses all combinations of the motion directions and cell IDs at any given grid location of the 2D airspace plane. Then, the Q-table is built through the exploration/exploitation of the environment, making random/optimized actions, and calculating the corresponding reward. The latter is used to update the Q-value of the related state-action pair using (5). These steps are repeated until the destination is reached within an episode. The execution of this algorithm for a sufficient number of episodes ensures convergence towards the optimal policy. The output of Algorithm 1 is the best strategy of trajectory and associated cells during the delivery mission.

![](images/f3974b2ee5d5886d885f44f8a5f424f6e3370826ae22f92b263d6988693fa124.jpg)  
Fig. 2. Training convergence of proposed algorithm.

## V. SIMULATION RESULTS

In this section, we assess the performance of the RL-based cargo-UAV trajectory planning with respect to cellular service reliability and handoffs. Hence, we compare our proposed algorithm to other benchmarks, i.e., shortest path and RSRP-aware path planning. The onboard battery’s capacity is the sole factor that significantly restricts the calculation of the shortest path baseline. As a result, the cargo-UAV sets the standard for low battery usage by taking the shortest route while being always connected to the BS with the strongest RSRP along the route. In contrast, the RSRP-aware RL-based trajectory planning algorithm determines the path that increases cellular reliability, i.e., with the lowest cellular disconnectivity time while ignoring handoff events.

We assume a $3 \times 3$ km<sup>2</sup> area in the city of Leuven, Belgium, where 20 three-sector BSs and 2 two-sector BSs are deployed. Each sector accounts for a cell, with a total number of 64. The area is divided into grid cells with a step of 20 meters on both X and Y axis. We set the following parameters as v <sub>=</sub> 30 m/s and $E _ { C } - E _ { S } = 2 5 0 0 \mathrm { k J }$ . Finally, typical values of the cargo-UAV related parameters are taken from [15, Table I].

In any given 3D location (at a fixed altitude h), the received RSRP from each available cell in the area is measured and stored as part of the environment states space. For the benchmark algorithms, only the cell with the strongest RSRP is considered to evaluate cellular disconnectivity and handoff performances, whereas our proposed algorithm considers in its states the first three strongest RSRPs, i.e., $N = 3$ Unless stated otherwise, the cellular service RSRP threshold is set to $T _ { \mathrm { t h } } = - 6 5 \mathrm { d B m } , w _ { \mathrm { e n } } = 2 . 5 \% , w _ { \mathrm { s i g } } = 9 0 \%$ , and $w _ { \mathrm { h o } } = 7 . 5 \%$ . For the RL parameters, we set $\beta = 0 . 9 , \alpha = 0 . 0 1 , \epsilon _ { \mathrm { m i n } } = 0 . 0 1$ , and $\epsilon = 0 . 9 9$ The total number of training episodes is fixed to 10<sup>4</sup>.

We show in Fig. 2 the learning curve of the proposed RL-based path planning algorithm. First, the cargo-UAV starts exploring the airspace without any prior knowledge and by randomizing its action, and accordingly constructs its Q-table by associating each realized action to a prospect reward. As the number of training episodes increases, the exploration phase is given less importance and the cargo-UAV starts to exploit the acquired experience to advance towards its destination. This translates into a proportional reward increase with training. As it can be seen, our algorithm converges from episode 3500, and the reward is maximized close to the maximum value 0.

![](images/0a4b33ce11543d4296afe9a3f3e02d2b34b7cc76d0e20b65a9b8310e568eaa23.jpg)  
(a)

![](images/a9e2bb2d3fdc703988c2e6349825e102bca1579b24fa8236cf38e2248128d668.jpg)  
(b)

![](images/15d9a009e1e160c732b37a69a6a7424145e80cfeec32459599768560046d43b0.jpg)  
(c)  
Fig. 3. Comparison of path planning algorithms. (a) Number of handoffs. (b) Disconnectivity along cargo-UAV mission (%). (c) Battery consumption (%).

Fig. 3 compares the performance of the proposed algorithm against those of benchmarks, i.e., “Sh. Path” (for shortest path) and “RSRP” (for only RSRP-aware) [11] algorithms, in terms of number of handoffs, battery consumption percentage, and disconnectivity percentage along the mission’s trajectory. For the proposed algorithm, we considered two configurations, the first with $( w _ { \mathrm { e n } } , w _ { \mathrm { s i g } } , w _ { \mathrm { h o } } ) = ( 2 . 5 \%$ 90%, 7.5%), called “Prop. $1 ^ { \circ }$ and the second with $( w _ { \mathrm { e n } } , w _ { \mathrm { s i g } } ,$ $w _ { \mathrm { h o } } ) = ( 4 \% , 8 0 \% , 1 6 \% )$ , named “Prop. 2”. According to Fig. 3(a)–(b), the shortest path algorithm experiences the highest number of handoffs and disconnectivity percentage for any flying altitude h. This is expected since the shortest path aim to reach the destination in the fastest possible way, regardless of other factors. As a consequence, it consumes the least energy as shown in Fig. 3(c). For RSRP-Aware algorithm, the number of handoffs and disconnectivity percentage are lower than for the previous method, since the cargo-UAV adjusts its trajectory to keep RSRP above the sensitivity threshold, whenever possible. To achieve that, the cargo-UAV traveled extra distances to avoid coverage holes, especially at $h = 8 0$ m where the RSRP signals are weaker. This has resulted in a higher battery consumption than for the shortest path benchmark, i.e., an additional 2% battery drainage. For the proposed algorithm, the number of handoffs and disconnectivity percentage are the lowest, while the consumed energy is approximately the same as the shortest path at $h = 4 0$ m and as the RSRP-Aware one at $h = 8 0$ m. In fact, the energy used by the extra detours of the proposed method, which were taken to reduce both handoffs and disconnectivity (shown in Fig. 4), compensates for the energy consumption of handoff signalling method, thus assuring better handoff and disconnectivity performances than the other methods. Also, when the handoffs weight $w _ { \mathrm { h o } }$ is increased in the reward function from 7.5% to 16%, the number of handoffs can be further reduced, in particular at lower altitudes.

![](images/5155e1943bf1fde6c26de483b0d8d7fe87680716ca1a1c5cd65b5ad177259c67.jpg)  
Fig. 4. Cargo-UAV trajectories (h = 80 m).

![](images/8cd42fdd874f9b2d6f0cf1e9a17e2287c08d6d72cb46e9f0fd4af1ed36ced59a.jpg)  
Fig. 5. Comparison of RSRP’s CDFs.

In Fig. 4, we present the resulting trajectories of the Fig. 3’s algorithms. Although the trajectories of our proposed approach (green and purple lines) experience several detours, it still achieves the mission with the best performances in terms of number of handoffs and disconnectivity, at the cost of a slight increase in energy consumption.

We illustrate in Fig. 5 the cumulative distribution function (CDF) of RSRP for the trajectory planning algorithms, under the same aforementioned assumptions. At the RSRP threshold $T _ { \mathrm { t h } } = - 6 5$ dBm, shown with a vertical line, the proposed method achieves the same low outage probability as the RSRP-based algorithm. Indeed, the proposed scheme’s flexibility allows for reducing the ping-pong handoffs and associated signaling overhead, at the expense of a low RSRP. At RSRP values exceeding the threshold $T _ { \mathrm { t h } }$ , the proposed method’s reliability deteriorates (i.e., higher CDF) compared to the benchmarks. This is expected since our algorithm does not guarantee its optimality beyond the parameters’ values it was trained with.

## VI. CONCLUSION

In this work, we proposed a novel energy-efficient disconnectivity and handoff aware RL-based trajectory planning and cell association algorithm for cargo-UAVs. Through simulations, we prove the superiority of our approach in terms of number of handoffs and disconnectivity, at the expense of a slight increase in battery consumption, when compared to baseline algorithms.

## REFERENCES

[1] N. Cherif, W. Jaafar, H. Yanikomeroglu, and A. Yongacoglu, “3D aerial highway: The key enabler of the retail industry transformation,” IEEE Commun. Mag., vol. 59, no. 9, pp. 65–71, Sep. 2021.

[2] A. Fotouhi et al., “Survey on UAV cellular communications: Practical aspects, standardization advancements, regulation, and security challenges,” IEEE Commun. Surveys Tuts., vol. 21, no. 4, pp. 3417–3442, Fourthquarter 2019.

[3] M. Ozger, M. Vondra, and C. Cavdar, “Towards beyond visual line of sight piloting of UAVs with ultra reliable low latency communication,” in Proc. IEEE Glob. Commun. Conf., 2018, pp. 1–6.

[4] S. Li et al., “Beyond visual line of sight UAV control for remote monitoring using directional antennas,” in Proc. IEEE Glob. Commun. Conf. Workshops, 2019, pp. 1–6.

[5] R. M. de Amorim, J. Wigard, I. Z. Kovacs, T. B. Sorensen, and P. E. Mogensen, “Enabling cellular communication for aerial vehicles: Providing reliability for future applications,” IEEE Veh. Technol. Mag., vol. 15, no. 2, pp. 129–135, Jun. 2020.

[6] N. Cherif, M. Alzenad, H. Yanikomeroglu, and A. Yongacoglu, “Downlink coverage and rate analysis of an aerial user in vertical heterogeneous networks (VHetNets),” IEEE Trans. Wireless Commun., vol. 20, no. 3, pp. 1501–1516, Mar. 2021.

[7] A. Alkhateeb, I. Beltagy, and S. Alex, “Machine learning for reliable mmWave systems: Blockage prediction and proactive handoff,” in Proc. IEEE Glob. Conf. Sig. Inf., 2018, pp. 1055–1059.

[8] A. Fakhreddine, C. Bettstetter, S. Hayat, R. Muzaffar, and D. Emini, “Handover challenges for cellular-connected drones,” in Proc. ACM Workshop Micro Aerial Veh. Netw. Sys. Appl., 2019, pp. 9–14.

[9] S. Euler, H.-L. Maattanen, X. Lin, Z. Zou, M. Bergström, and J. Sedin, “Mobility support for cellular connected unmanned aerial vehicles: Performance and analysis,” in Proc. IEEE Wireless Commun. Netw. Conf., 2019, pp. 1–6.

[10] Y. Chen, X. Lin, T. Khan, and M. Mozaffari, “Efficient drone mobility support using reinforcement learning,” in Proc. IEEE Wireless Commun. Netw. Conf., 2020, pp. 1–6.

[11] N. Cherif, W. Jaafar, H. Yanikomeroglu, and A. Yongacoglu, “Disconnectivity-aware energy-efficient cargo-UAV trajectory planning with minimum handoffs,” in Proc. IEEE Int. Conf. Commun., 2021, pp. 1–6.

[12] A. Colpaert, E. Vinogradov, and S. Pollin, “Aerial coverage analysis of cellular systems at LTE and mmwave frequencies using 3D city models,” Sensors, vol. 18, no. 12, Dec. 2018, Art. no. 4311.

[13] W. Jaafar and H. Yanikomeroglu, “Dynamics of laser-charged UAVs: A battery perspective,” IEEE IoT J., vol. 8, no. 13, pp. 10573–10582, Jul. 2021.

[14] J. K. Lenstra and A. H. G. R. Kan, “Complexity of vehicle routing and scheduling problems,” Networks, vol. 11, no. 2, pp. 221–227, Third Quarter 1981.

[15] Y. Zeng, J. Xu, and R. Zhang, “Energy minimization for wireless communication with rotary-wing UAV,” IEEE Trans. Wireless Commun., vol. 18, no. 4, pp. 2329–2345, Apr. 2019.