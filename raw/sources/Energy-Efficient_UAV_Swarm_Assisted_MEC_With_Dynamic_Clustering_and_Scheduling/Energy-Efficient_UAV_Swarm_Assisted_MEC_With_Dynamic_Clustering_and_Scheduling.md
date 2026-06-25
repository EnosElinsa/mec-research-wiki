# Energy-Efficient UAV Swarm Assisted MEC with Dynamic Clustering and Scheduling

Jialiuyuan Li∗, Jiayuan Chen∗, Changyan Yi,∗, Tong Zhang∗, Kun Zhu∗ and Jun Cai† ∗College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing, China †Department of Electrical and Computer Engineering, Concordia University, Montreal, QC, H3G 1M8, Canada ´ Email: {jialiuyuan.li, jiayuan.chen, changyan.yi, zhangt, zhukun}@nuaa.edu.cn, jun.cai@concordia.ca

Abstract—In this paper, the energy-efficient unmanned aerial vehicle (UAV) swarm assisted mobile edge computing (MEC) with dynamic clustering and scheduling is studied. In the considered system model, UAVs are divided into multiple swarms, with each swarm consisting of a leader UAV and several follower UAVs to provide computing services to end-users. Unlike existing work, we allow UAVs to dynamically cluster into different swarms, i.e., each follower UAV can change its leader based on the time-varying spatial positions, updated application placement, etc. in a dynamic manner. Meanwhile, UAVs are required to dynamically schedule their energy replenishment, application placement, trajectory planning and task delegation. With the aim of maximizing the longterm energy efficiency of the UAV swarm assisted MEC system, a joint optimization problem of dynamic clustering and scheduling is formulated. Taking into account the underlying cooperation and competition among intelligent UAVs, we further reformulate this optimization problem as a combination of a series of strongly coupled multi-agent stochastic games, and then propose a novel reinforcement learning-based UAV swarm dynamic coordination (RLDC) algorithm for obtaining the equilibrium. Simulations are conducted to evaluate the performance of the RLDC algorithm and demonstrate its superiority over counterparts.

# I. INTRODUCTION

R ECENTLY, unmanned aerial vehicle (UAV) assisted mo-bile edge computing (MEC) [1], [2] has attracted signifi- bileedgecomputing (MEC)[1],[2]hasattractedigificant attentions due to its high mobility, flexible coverage and rapid deployment in providing fast-responsive supplementary computing services to end-users (e.g., IoT devices). Furthermore, by forming into swarms (each of which consists of a leader and multiple followers [3]), UAV swarm assisted MEC can further improve the collaboration among UAVs for enhancing the service quality, and thus has become a popular trend for future applications [4].

Although UAV swarm assisted MEC is envisioned as a lightweight and highly efficient paradigm, it faces several inherent challenges: i) since the MEC service demands of IoT devices vary dynamically, if UAV swarms are predetermined with fixed clustering, the computing workloads among different swarms may be severely unbalanced; ii) UAVs (especially the leaders) are battery-constrained and have to fly to the depot for energy replenishment if necessary, meaning that their swarm formations cannot be maintained long-term static; iii) the limited storage capacities of UAVs (both leaders and followers) impede their abilities to store all applications to fulfill diverse task requirements of IoT devices, indicating that they have to help with each other through task delegations (particularly within the swarm). Recent research efforts in this area include cooperative trajectory planning [5], [6] and collaborative task delegation [7], [8], etc. Nevertheless, there are still some critical issues, especially how UAV swarms can cater to dynamic service requirements of IoT devices, and how UAV swarms can be dynamically clustered based on their spatial positions and updated application placement, which are of great importance but have not yet been well investigated.

In this paper, we study a joint optimization problem of dynamic clustering and scheduling for UAV swarm assisted MEC to maximize the long-term energy efficiency of the system. Specifically, in the considered model, the following decisions are made within each time slot: i) each leader UAV determines whether it should return to the depot for refueling energy and updating the installed applications or the next target service region of its leaded swarm; ii) each follower UAV determines which leader UAV to follow (i.e., the associated swarm), the trajectory in its swarm, and whether to delegate certain tasks to the leader. Since all UAVs are intelligent, they are allowed to make individual decisions, potentially leading to the cooperation and competition among them. To this end, we reformulate the joint optimization problem as a series of complex multi-agent stochastic games, i.e., energy replenishment stochastic game (ERSG), application planning stochastic game (APSG), leader UAV trajectory planning stochastic game (LTSG), dynamic clustering stochastic game (DCSG), follower UAV trajectory planning stochastic game (FTSG), and task delegation stochastic game (TDSG). After analyzing their properties, we then propose a novel reinforcement learning-based UAV swarm dynamic coordination (RLDC) algorithm to obtain the corresponding equilibriums.

The main contributions of this paper are as follows.

• A joint optimization problem of dynamic clustering and scheduling in UAV swarm assisted MEC is formulated, where the objective is to maximize the long-term energy efficiency of all UAVs (including leaders and followers).   
Observing the cooperation and competition among UAVs, we reformulate the optimization problem as a series of coupled multi-agent stochastic games, and then propose a novel algorithm, called RLDC, to obtain the corresponding equilibriums.   
• Extensive simulations are conducted to show the superiority of the proposed RLDC algorithm over counterparts.

The rest of this paper is organized as follows: Section II introduces the system model and problem formulation. In Section

![](images/c830b7d06e6f74240ba916fef47bfa1959cafb336b150acd4c3b6d5af24acff0.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Task offloading"] --> B["Leader UAV"]
    C["Task delegation"] --> D["Follower UAV"]
    E["Follow another leader UAV"] --> F["Applications"]
    G["Interference"] --> H["Tasks"]
    I["Remaining energy of the UAV"] --> J["UAV swarm"]
    K["Service area of UAV swarm"] --> L["Coverage of the follower UAV"]
    M["Depot"] --> N["Robot icon"]
```
</details>

Fig. 1. An illustration of the considered UAV swarm assisted MEC.

III, a problem reformulation based on multi-agent stochastic game is proposed and analyzed, along with the developed RLDC algorithm. Simulation results are provided in Section IV, followed by the conclusion in Section V.

# II. SYSTEM MODEL AND PROBLEM FORMULATION

# A. Network Model

Consider a UAV swarm assisted MEC system deployed in a target region, as illustrated in Fig. 1. The system consists of a group of leader UAVs, denoted as M with $| { \mathcal { M } } | = M ,$ , a group of follower UAVs, denoted as N with $| { \mathcal { N } } | = N$ , and a set of IoT devices scattered randomly on the ground, denoted as K with $| { \boldsymbol { \kappa } } | = K$ . At the edge of the target region, a depot is deployed to serve leader UAVs with energy replenishment and application placement update through wired connections. A timeslotted operation framework is studied, which is characterized by $t \in \{ 1 , 2 , . . . , T \}$ . The target region is uniformly divided into large grids with side length l to limit the activities scope of each swarm. Meanwhile, the large grids are further uniformly divided into small grids with side length q to specify the activities of follower UAVs. Similar to [9], the downlink transmission range of each follower UAV is assumed to be ${ \sqrt { 2 } } q / 2$ , such that it can cover a small grid for computation outcome feedback. At any time slot, each small grid is limited to be covered by only one follower UAV to avoid collisions, where each follower UAV provides supplementary computing services to multiple IoT devices simultaneously within its downlink transmission range. We denote the set of IoT devices served by follower UAV $n \in \mathcal N$ as ${ \mathcal { G } } _ { n }$ , and each IoT devices $k \in \mathcal { K }$ uses the same frequency band B for uplink communications. Then, the signalto-interference-plus-noise ratio (SINR) at follower UAV n with regard to the uplink communication of IoT device k, and the SINR at leader UAV m with regard to the uplink communication of follower UAV n at time slot t, can be expressed as:

$$
\gamma_ {n, k} (t) = \frac {p _ {k} ^ {I} 1 0 ^ {\frac {- \lambda_ {n , k} (t)}{1 0}}}{\sum_ {i \in \mathcal {G} _ {n} \backslash k} p _ {i} ^ {I} 1 0 ^ {\frac {- \lambda_ {n , k} (t)}{1 0}} + \varpi}, \tag {1}
$$

and

$$
\gamma_ {m, n} (t) = \frac {p _ {n} ^ {F} 1 0 ^ {\frac {- \lambda_ {m , n} (t)}{1 0}}}{\varpi}, \tag {2}
$$

respectively. $p _ { k } ^ { I }$ and $p _ { n } ^ { F }$ denote the transmission power of IoT device k and follower UAV n, respectively. \$ indicates the power spectral density of noise. Following the literature [6], $\lambda _ { m , n } ( t )$ and $\lambda _ { n , k } ( t )$ indicate the path loss between leader UAV m and follower UAV $n ,$ and the path loss between follower UAV n and IoT device k at time slot t, respectively. Let $\mathcal { C } = \{ 1 , 2 , . . . , C \}$ denote the set of task type. Based on above expressions, the time of IoT device $k \in \mathcal G _ { n }$ offloading task $c \in { \mathcal { C } }$ to follower UAV n, and the time of follower UAV n delegating task c to leader UAV m at time slot t can be written as:

$$
T _ {n, k, c} ^ {\text { off }} (t) = \frac {\upsilon_ {k , c} (t) \kappa_ {k , c}}{B \log_ {2} (1 + \gamma_ {n , k} (t))}, \tag {3}
$$

and

$$
T _ {m, n, c} ^ {\text { dele }} (t) = \frac {(1 - \varepsilon_ {m} (t)) \delta_ {m , n} (t) \phi_ {m , n , c} (t) \kappa_ {k , c}}{B \log_ {2} (1 + \gamma_ {m , n} (t))}, \tag {4}
$$

respectively. $\kappa _ { k , c }$ indicates the size of task c offloaded from IoT device k. $v _ { k , c } ( t ) \in [ 0 , 1 ]$ , and $\upsilon _ { k , c } ( t ) = 1$ means that IoT device k requests task c at time slot t, otherwise $\boldsymbol { v } _ { k , c } ( t ) = 0$ . Besides, $\varepsilon _ { m } ( t ) \in [ 0 , 1 ]$ , and $\varepsilon _ { m } ( t ) = 1$ means that leader UAV m returns to the depot at time slot t, otherwise $\varepsilon _ { m } ( t ) = 0$ . Meanwhile, $\delta _ { m , n } ( t ) \in [ 0 , 1 ]$ , and $\delta _ { m , n } ( t ) = 1$ means that follower UAV n follows the leader UAV m at time slot t, otherwise $\delta _ { m , n } ( t ) = 0$ . Additionally, $\phi _ { m , n , c } ( t ) \in [ 0 , 1 ]$ , and $\phi _ { m , n , c } ( t ) = 1$ means that follower UAV n delegates task c to the leader UAV m, otherwise $\phi _ { m , n , c } ( t ) = 0$ .

We assume that T of f $T _ { n , k , c } ^ { o f f } ( t ) ~ < ~ T _ { n } ^ { F h o v } ( t )$ , indicating that the hovering time $T _ { n } ^ { F h o v } ( t )$ is sufficiently long for follower UAV n to receive each task offloaded by IoT devices at time slot t. Besides, the application c placed in follower UAV n and leader UAV m can be defined as $\omega _ { n , c } ^ { F } ( t ) \in \{ 0 , 1 \}$ and $\omega _ { m , c } ^ { L } ( t ) \in \{ 0 , 1 \}$ , respectively. $\omega _ { n , c } ^ { F } ( t ) = 1$ means that follower UAV n place the application which can process task c, otherwise $\omega _ { n , c } ^ { F } ( t ) = 0$ . And the definition of $\omega _ { m , c } ^ { L } ( t )$ is similar to that of $\omega _ { n , c } ^ { F } ( t )$ . Consequently, the size of tasks processed by follower UAV n and leader UAV m can be expressed as:

$$
T a s k _ {n} ^ {F} (t) =
$$

$$
\min \left\{\sum_ {k \in \mathcal {G} _ {n}} \sum_ {m = 1} ^ {M} \sum_ {c = 1} ^ {C} \left(1 - \phi_ {m, n, c} (t)\right) v _ {k, c} (t) \omega_ {n, c} ^ {F} (t) \kappa_ {k, c}, \right. \tag {5}
$$

$$
f _ {n} ^ {F} (T _ {n} ^ {F h o v} (t) - \min \{\pmb {T} _ {n} ^ {o f f} (t) \}) \},
$$

and

$$
T a s k _ {m} ^ {L} (t) =
$$

$$
\min \{\sum_ {n = 1} ^ {N} \sum_ {c = 1} ^ {C} \delta_ {m, n} (t) \phi_ {m, n, c} (t) v _ {k, c} (t) \omega_ {m, c} ^ {L} (t) \kappa_ {k, c}, \tag {6}
$$

$$
f _ {m} ^ {L} (T _ {n} ^ {F h o v} (t) - \min \{\pmb {T} _ {m} ^ {d e l e} (t) \}) \},
$$

respectively, where and $\pmb { T } _ { m } ^ { d e l e } ( t ) = \{ T _ { m , 1 , 1 } ^ { d e l e } ( t ) , . . . , T _ { m , n , c } ^ { d e l e } ( t ) , . . . \} . ~ f _ { n } ^ { F }$ $T _ { n } ^ { o f f } ( t ) = \{ T _ { n , 1 , 1 } ^ { o f f } ( t ) , . . . , T _ { n , k , c } ^ { o f f } ( t ) , . . . \}$ Tn,k,c( a nd $f _ { m } ^ { L }$ indicate the computing capacity of follower UAV n and leader UAV m (the number of CPU cycles per second). Then, the energy consumption of follower UAV n and leader UAV m computing tasks can be respectively written as $E _ { n } ^ { c o m p } ( t ) ~ =$ $\xi ( f _ { n } ^ { \bar { F } } ) ^ { 2 } T \bar { a } s k _ { n } ^ { F } ( t )$ and $E _ { m } ^ { c o m p } ( t ) = ( \bar { 1 - } \varepsilon _ { m } ( t ) ) \xi ( f _ { m } ^ { L } ) ^ { 2 } \ddot { T } a s \dot { k } _ { m } ^ { L } ( t )$ , where ξ denotes effective capacitance coefficient. Moreover, the propulsion energy consumption of leader UAV m and follower UAV n with the velocity v can be expressed as:

$$
E _ {m} ^ {p r o} (t) = (1 - \varepsilon_ {m} (t)) (P ^ {p r o} (v) \frac {l}{v} + P ^ {p r o} (0) T _ {n} ^ {L h o v} (t)), \tag {7}
$$

and

$$
\begin{array}{l} E _ {n} ^ {p r o} (t) = P ^ {p r o} (v) \left(\frac {\left((1 - \delta_ {m , n} (t - 1) \delta_ {m , n} (t)) d _ {m , n} (t) \right.}{v} + \frac {q}{v}\right) \\ + P ^ {p r o} (0) T _ {n} ^ {F h o v} (t), \tag {8} \\ \end{array}
$$

respectively, where $P ^ { p r o } ( v )$ is the propulsion power model of UAVs, and its description follows [10]. Furthermore, let $E _ { m } ^ { r e t } ( t )$ be its energy consumption of returning to the depot, which can be written as $\begin{array} { r } { E _ { m } ^ { r e t } ( t ) = \varepsilon _ { m } ( t ) P ^ { p r o } ( v ) d _ { m } ^ { r e t } ( t ) / v , } \end{array}$ , where $d _ { m } ^ { r e t } ( t )$ indicates the distance between leader UAV m and the depot at time slot t.

# B. Problem Formulation

In this paper, the energy efficiency $E ^ { e f f i } ( t )$ means the amount of tasks processed by all UAVs relative to their energy consumption during time slot t. This can be mathematically expressed as

$$
E ^ {e f f i} (t) =
$$

$$
\frac {\sum_ {m = 1} ^ {M} T a s k _ {m} ^ {L} (t) + \sum_ {n = 1} ^ {N} T a s k _ {n} ^ {F} (t)}{\sum_ {m = 1} ^ {M} ((E _ {m} ^ {c o m p} (t) + E _ {m} ^ {p r o} (t) + E _ {m} ^ {r e t} (t)) + \sum_ {n = 1} ^ {N} (E _ {n} ^ {c o m p} (t) + E _ {n} ^ {p r o} (t))}.
$$

Then, in this paper, we aim to jointly optimize the dynamic clustering and scheduling of considered the UAV swarm assisted MEC system, with the objective of maximizing the long-term energy efficiency, and which can be formulated as

$$
\begin{array}{l}\left[ \mathcal {P} 1 \right]: \max _ {\boldsymbol {\mathcal {L}} (t), \boldsymbol {\mathcal {F}} (t), \boldsymbol {\omega} ^ {L} (t), \boldsymbol {\varepsilon} (t), \boldsymbol {\delta} (t), \boldsymbol {\phi} (t)} \lim _ {T \rightarrow + \infty} \frac {1}{T} \sum_ {t = 1} ^ {T} E ^ {e f f i} (t)\\s. t., \sum_ {m = 1} ^ {M} \delta_ {m, n} = 1, \forall n \in \mathcal {N},\end{array}\tag {9}
$$

$$
\sum_ {n = 1} ^ {N} \delta_ {m, n} \geq 1, \forall m \in \mathcal {M}, \tag {10}
$$

$$
\sum_ {m = 1} ^ {M} \omega_ {m, c} ^ {L} (t) \varepsilon_ {m} (t) \geq 1, \forall c \in \mathcal {C}, \tag {11}
$$

$$
\left| \mathcal {F} _ {n} (t) - \mathcal {F} _ {n} (t - 1) \right| ^ {2} = q ^ {2}, \forall n \in \mathcal {N}, \tag {12}
$$

$$
(1 - \varepsilon_ {m} (t)) | \mathcal {L} _ {m} (t) - \mathcal {L} _ {m} (t - 1) | ^ {2} = l ^ {2}, \tag {13}
$$

$$
\left| \mathcal {F} _ {n} (t) - \mathcal {F} _ {n ^ {\prime}} (t) \right| ^ {2} \geq q ^ {2}, \forall n ^ {\prime} \in \mathcal {N} \backslash n, \tag {14}
$$

$$
\left| \mathcal {L} _ {m} (t) - \mathcal {L} _ {m ^ {\prime}} (t) \right| ^ {2} \geq l ^ {2}, \forall m ^ {\prime} \in \mathcal {M} \backslash m, \tag {15}
$$

$$
\delta_ {m, n} (t) \left(1 - \varepsilon_ {m} (t)\right) \left| x _ {m} ^ {L} (t) - x _ {n} ^ {F} (t) \right| \leq \frac {l - q}{2}, \tag {16}
$$

$$
\delta_ {m, n} (t) (1 - \varepsilon_ {m} (t)) | y _ {m} ^ {L} (t) - y _ {n} ^ {F} (t) | \leq \frac {l - q}{2}, \tag {17}
$$

where $\pmb { \mathcal { L } } ( t ) = \{ \mathcal { L } _ { 1 } ( t ) , \mathcal { L } _ { 2 } ( t ) , . . . , \mathcal { L } _ { M } ( t ) \}$ and $\mathcal { F } ( t ) = \{ \mathcal { F } _ { 1 } ( t )$ , $\mathcal { F } _ { 2 } ( t ) , . . . , \mathcal { F } _ { N } ( t ) \}$ denote the location sets of leader UAVs and follower UAVs at time slot $t ,$ respectively. Therein, $\mathcal { L } _ { m } ( t ) =$ $( x _ { m } ^ { L } ( t ) , y _ { m } ^ { L } ( t ) )$ and ${ \mathcal F } _ { n } ( t ) ~ = ~ \bar { ( x _ { n } ^ { F } ( t ) , y _ { n } ^ { F } ( t ) ) }$ represent their horizontal coordinates at time slot $t ,$ respectively. Constraint (9) indicates that each follower UAV must follow a leader UAV at each time slot; constraint (10) indicates that each UAV swarm contains at least one follower UAV at each time slot; constraint (11) indicates that each type of application should be installed in at least one leader UAV hovering over the target region at each time slot $t ;$ constraint (12) and (13) imply that each leader UAV and follower UAV can only move to the centers of large grid and small grid, respectively; constraint (14) and (15) indicate that each small grid and large grid can only be covered by one follower UAV and one leader UAV, respectively, in order to avoid potential collisions; constraint (16) and (17) imply that each follower UAV must remain within its UAV swarm. In the following sections, we will first analyze problem [P1], and then propose a novel algorithm to derive the corresponding solution.

# III. PROBLEM REFORMULATION AND SOLUTION

# A. Problem Reformulation

Considering the intelligence of UAVs, to solve problem [P1], we allow each UAV to autonomously make decisions while ensuring appropriate regulation of cooperation and competition among them. Additionally, considering the uncertainty of the future environment information, for example, task requirements of IoT devices are not available in advance for UAVs, we reformulate the joint optimization problem [P1] as a series of strongly coupled multi-agent stochastic games as follows.

The coupled multi-agent stochastic games are ERSG $\langle \mathcal { U } , \mathcal { S } ^ { E R } , \mathcal { A } ^ { \bar { E } R } , \mathcal { P } ^ { E R } , \mathcal { R } ^ { E R } \rangle$ , APSG $\langle \mathcal { U } , S ^ { A P } , \mathcal { A } ^ { A P } , \mathcal { P } ^ { A P } , \mathcal { R } ^ { A P } \rangle$ , LTSG $\langle \mathcal { U } , S ^ { L T } , \mathcal { A } ^ { L T } , \mathcal { P } ^ { L T } , \mathcal { R } ^ { L T } \rangle$ , DCSG $\langle \mathcal { U } , \mathcal { S } ^ { D C } , \mathcal { A } ^ { D C } , \mathcal { P } ^ { D C }$ , $\mathcal { R } ^ { D C } \rangle$ , $\mathrm { F T S G ~ } \langle \mathcal { U } , \mathcal { S } ^ { F T } , \mathcal { A } ^ { F T } , \mathcal { P } ^ { \dot { F } T } , \mathcal { R } ^ { F T } \rangle$ and TDSG $\langle \mathcal { U } , S ^ { T D }$ , $\mathcal { A } ^ { T D } , \mathcal { P } ^ { T D } , \mathcal { R } ^ { T \dot { D } } \rangle$ . Specifically, for ERSG, each leader UAV $u \in \mathcal { U }$ will choose an action individually based on the current environment state $s ^ { E R } ( t ) \in \mathcal { S } ^ { E R }$ at the beginning of each time slot t, and then form a joint action $\pmb { a } ^ { E \tilde { R } } ( t ) \ \in \ \mathcal { A } ^ { E R }$ . After executing the joint action, rewards will be obtained according to $\mathcal { R } ^ { E R }$ , and the environment states will turn to next ones with $\mathcal { P } ^ { E R }$ . The descriptions of APSG, LTSG, DCSG, FTSG and TDSG are similar to that of ERSG, and are omitted here for conciseness. In the following subsection, we propose a novel algorithm, called RLDC, to obtain equilibriums of these coupled multi-agent stochastic games.

# B. RLDC Algorithm

Since the transitions of states and actions in ERSG, APSG, LTSG, DCSG, FTSG and TDSG satisfy the Markov property, we characterize the strategic decision processes of each leader UAV and follower UAV by a series of respective Markov decision processes (MDPs) [11].

# MDP for each leader UAV in ERSG:

1) Environment state for each leader UAV in ERSG: To reduce the size of the state space in ERSG, we divide the energy of leader UAVs into several levels. Specifically, the energy level of leader UAV m can be written as where Eunit is the UAV energ $E _ { m } ^ { l e v e l } ( t ) = \lceil E _ { m } ^ { r e m a i n } / E ^ { u n i t } \rceil$ state $s ^ { E R } ( t ) \in \mathcal { S } ^ { E R }$ for each leader UAV $m \in \mathcal { M }$ in ERSG at time slot t can be expressed as $s ^ { E R } ( t ) = E ^ { l e v e l } ( t )$ , where $\pmb { E } ^ { l e v e l } ( t ) = \{ E _ { 1 } ^ { l e v e l } ( t ) , \hat { E } _ { 2 } ^ { l e v e l } ( t ) , . . . , E _ { M } ^ { l e v e l } ( t ) \}$ indicates the set of all leader UAVs’ energy levels.

2) Action for each leader UAV in ERSG: At time slot t, leader UAV m ∈ M chooses an action $a _ { m } ^ { E R } ( t ) \in \mathcal { A } _ { m } ^ { E R }$ , where $\mathcal { A } _ { m } ^ { E R }$ is the action set of UAV m in ERSG consisting of two actions, i.e., return to the depot or not.

3) Reward of each leader UAV in ERSG: The immediate reward $r _ { m } ^ { E R } ( t ) ~ \in \mathcal { R } _ { m } ^ { E R }$ of leader UAV $m \in \mathcal { M }$ at time slot t is given by:

$$
r _ {m} ^ {E R} (t) = \left\{ \begin{array}{l l} - 1 0, & \text { if   constraint   (11)   is   violated }, \\ \varepsilon_ {m} (t), & \text { otherwise }. \end{array} \right. \tag {18}
$$

4) State transition probabilities of leader UAVs in ERSG: The state transition probability from state $s ^ { E R }$ to state $s ^ { E R ^ { \prime } }$ by taking the joint action $\pmb { a } ^ { E R } ( \acute { t } ) = ( a _ { 1 } ^ { E R } ( t ) , a _ { 2 } ^ { E R } ( t ) , . . . , a _ { M } ^ { E R } ( t ) )$ can be expressed as PERER $\mathcal { P } _ { s ^ { E R } . s ^ { E R ^ { \prime } } } ^ { E R } ( \pmb { a } ^ { \dot { E } R } ( t ) ) = \bar { P } r ( s ^ { E R } ( t + 1 ) =$ $s ^ { E R ^ { \prime } } | s ^ { E R } ( t ) = s ^ { E R } , \mathbf { { \alpha } } \mathbf { { } } \mathbf { { \alpha } } \mathbf { { } } \mathbf { { \alpha } } ^ { E R } ( t ) )$ .

Note that, the transition probabilities of the other MDPs are similar to that in ERSG, and they are omitted subsequently for conciseness.

# MDP for each leader UAV in APSG:

1) Environment state for each leader UAV in APSG: The environment state $s ^ { A P } ( t ) \bar { \in } \bar { S } ^ { A P }$ for each leader UAV m $\in \mathcal { M }$ in APSG at time slot t consists of applications placed in all leader UAVs, which can be expressed as $s ^ { A P } ( t ) \stackrel { = } { = } \omega ^ { L } ( t )$ .   
2) Action for each leader UAV in APSG: At time slot t, leader UAV m ∈ M chooses an action $a _ { m } ^ { A P } ( t ) \in \mathcal { A } _ { m } ^ { A P } . \mathcal { A } _ { m } ^ { A P }$ signifies that the action set of leader UAV m consisting of $C ! / ( C -$ $S ^ { L } ) * S ^ { L } ! )$ actions, where $S ^ { L }$ denotes the maximum number of applications placed on leader UAV.   
3) Reward of each leader UAV in APSG: The immediate reward rAP ( $r _ { m } ^ { A P } ( t ) ~ \in ~ \mathcal { R } _ { m } ^ { A P }$ of leader UAV $m \in \mathcal { M }$ at time slot t is given by:

$$
r _ {m} ^ {A P} (t) = \sum_ {\tau = 1} ^ {t} \sum_ {n = 1} ^ {N} \sum_ {k \in \mathcal {G} _ {n}} \delta_ {m, n} (\tau) v _ {k} (\tau) \omega_ {m} (\tau), \tag {19}
$$

where $r _ { m } ^ { A P } ( t )$ indicates the amount of tasks computed by leader UAV m before time slot t.

# MDP for each leader UAV in LTSG:

1) Environment state for each leader UAV in LTSG: The environment state $s ^ { L T } ( t ) \stackrel { } { \in } \mathcal { S } ^ { L T }$ for each leader UAV $m \in \mathcal { M }$ in LTSG at time slot t consists of all leader UAVs’ positions $\pmb { \mathscr { L } } ( t )$ and set $\pmb { \delta } ( t )$ , which can be expressed as $s ^ { L T } ( t ) = \{ \mathcal { L } ( t ) , \delta ( t ) \}$ .   
2) Action for each leader UAV in LTSG: At time slot t, leader UAV m ∈ M chooses an action $a _ { m } ^ { L T } ( t ) \in \mathcal { A } _ { m } ^ { L T }$ , where $\mathcal { A } _ { m } ^ { L T }$ is the action set of leader UAV m in LTSG consisting of four possible actions, i.e., moving forward, backward, left or right to an adjacent large grid.   
3) Reward of each leader UAV in LTSG: The immediate reward $r _ { m } ^ { L T } ( t ) ~ \in ~ \mathcal { R } _ { m } ^ { L T }$ of leader UAV $m \in \mathcal { M }$ at time slot

t is given by:

$$
r _ {m} ^ {L T} (t) = \frac {\operatorname{Task} _ {m} ^ {L} (t) + \sum_ {n = 1} ^ {N} \delta_ {m , n} (t) \operatorname{Task} _ {n} ^ {F} (t)}{E _ {m} ^ {\text { remain }} (t - 1) - E _ {m} ^ {\text { remain }} (t)}, \tag {20}
$$

where the numerator indicates the size of tasks computed by the UAV swarm, and the denominator represents the energy consumption of leader UAV m.

# MDP for each follower UAV in DCSG:

1) Environment state for each follower UAV in DCSG: The environment state $s ^ { D C } ( i ) \in \mathcal { S } ^ { D C }$ for each follower UAV $n \in \mathcal N$ at time slot t consists of all leader $\mathrm { U A V s } '$ positions $\pmb { \mathscr { L } } ( t )$ and set $\delta ( t )$ , which can be expressed as $s ^ { D C } ( t ) = \{ \pmb { { \mathcal { L } } } ( t ) , \pmb { \delta } ( t ) \}$ .   
2) Action for each follower UAV in DCSG: At time slot t, followwhere AV  sig $n \in \mathcal N$ chooses an action  action set of followe $a _ { n } ^ { D C } ( t ) ~ \in ~ \mathcal { A } _ { n } ^ { D C }$ $\mathcal { A } _ { n } ^ { D C }$ consisting of M possible actions.   
3) Reward of each follower UAV in DCSG: The immediate reward $r _ { n } ^ { D C } ( t ) \in \mathcal { R } _ { n } ^ { D \bar { C } }$ of follower UAV $n \in \mathcal N$ in DCSG at time slot t is given by $r _ { n } ^ { D C } ( t ) = E ^ { e f f i } ( t )$ .

# MDP for each follower UAV in FTSG:

1) Environment state for each follower UAV in FTSG: The environment state $s ^ { F T } ( t ) ~ \in ~ \bar { S ^ { F T } }$ for each follower UAV $\textit { n } \in \textit { N }$ in FTSG at time slot t consists of all follower UAVs’ positions F (t) and set $\delta ( t )$ , which can be expressed as $\mathbf { \boldsymbol { s } } ^ { F T } ( t ) = \{ \mathcal { F } ( t ) , \delta ( t ) \}$ .   
2) Action for each follower UAV in FTSG: At time slot t, r UAV is the $n \in \mathcal N$ chooses an action set of follower UA $a _ { n } ^ { F T } ( t ) \in \mathcal { A } _ { n } ^ { F T }$ , wherensisting $\mathcal { A } _ { n } ^ { F T } ( t )$ of four possible actions, i.e., moving forward, backward, left or right to an adjacent large grid.   
3) Reward of each follower UAV in FTSG: The immediate reward $r _ { n } ^ { F T } ( t ) ~ \in \mathcal { R } _ { n } ^ { F T }$ of follower UAV $n \in \mathcal N$ in FTSG at time slot t is given by:

$$
r _ {n} ^ {F T} (t) = \frac {\operatorname{Task} _ {n} ^ {F} (t)}{\sum_ {m = 1} ^ {M} \sum_ {c = 1} ^ {C} \delta_ {m , n} p _ {n} ^ {F} T _ {m , n , c} ^ {\text {dele}} (t) + \xi \left(f _ {n} ^ {F}\right) ^ {2} \operatorname{Task} _ {n} ^ {F} (t) + E _ {n} ^ {\text {pro}} (t)}, \tag {21}
$$

where the numerator indicates the size of tasks computed by the follower UAV n, and the denominator represents the energy consumption of follower UAV n.

# MDP for each follower UAV in TDSG:

1) Environment state for each follower UAV in TDSG: The environment state $s ^ { T D } \bar { ( t ) } \in \bar { S ^ { T D } }$ for each follower UAV $n \in \mathcal N$ in TDSG at time slot t consists of leader UAV m’s application placement $\omega _ { m } ^ { L } ( t )$ , follower UAV n’s application placement $\omega _ { n } ^ { F } ( t )$ and set δ(t), which can be expressed as $\mathsf { \bar { s } } ^ { T D } ( t ) = \{ \omega _ { m } ^ { \bar { L } } ( t ) , \omega _ { n } ^ { F } ( t ) , \delta ( t ) \}$ .   
2) Action for each follower UAV in TDSG: At time slot t, follower ${ \mathrm { U A V ~ } } n \in { \mathcal { N } }$ chooses an action $a _ { n } ^ { T D } ( t ) \in \mathcal { A } _ { n } ^ { T D }$ , where $\mathcal { A } _ { n } ^ { T D } ( t )$ is the action set of follower UAV n in TDSG consisting of two possible actions, i.e., whether delegating its tasks to the leader UAV or not.   
3) Reward of each follower UAV in TDSG: The immediate reward $r _ { n } ^ { T D } ( t ) \in \mathcal { R } _ { n } ^ { T \bar { D } }$ of follower UAV $n \in \mathcal N$ in TDSG at

time slot t is given by:

$$
r _ {n} ^ {T D} (t) = \sum_ {m = 1} ^ {M} \sum_ {c = 1} ^ {C} \left(\frac {\operatorname{Task} _ {n} ^ {F} (t) + \delta_ {m , n} (t) \operatorname{Task} _ {m} ^ {L} (t)}{p _ {n} ^ {F} T _ {m , n , c} ^ {\text {dele}} (t) + \xi \left(f _ {n} ^ {F}\right) ^ {2} \operatorname{Task} _ {n} ^ {F} (t) + \delta_ {m , n} (t) \xi \left(f _ {m} ^ {L}\right) ^ {2} \operatorname{Task} _ {m} ^ {L} (t)}\right), \tag {22}
$$

where the numerator indicates the size of tasks computed by leader UAV m and follower UAV n in the same swarm, and the denominator represents the energy consumption of task delegation and task computing.

Based on these MDPs, we propose a novel RLDC algorithm, where Q-learning is utilized to obtain the solution. RLDC includes a series of corresponding learners, namely, leader UAV energy replenishment learner, leader UAV application placement learner, leader UAV trajectory planning learner, follower UAV trajectory planning learner, follower UAV dynamic clustering learner and follower UAV task delegation learner.

The policy of leader UAV energy replenishment learner in UAV m is expressed as πERm $\pi _ { m } ^ { E R } : S ^ { E R } \longrightarrow \mathcal { A } _ { m } ^ { E R }$ , which signifies a probability distribution of actions $a _ { m } ^ { E R } \in \ddot { A } _ { m } ^ { E R }$ am in a state $s ^ { E R }$ .

The Q function of the leader UAV energy replenishment learner in UAV m is the expected reward by executing action $a _ { m } ^ { E R } \in \mathcal { A } _ { m } ^ { E R }$ a m in state $s ^ { E R } \in \mathop { S } ^ { E R }$ under the given policy $\pi _ { m } ^ { E R } ,$ which can be expressed by:

$$
Q _ {m} ^ {E R} (s ^ {E R}, \pmb {a} ^ {E R}, \pi_ {m} ^ {E R}) =
$$

$$
\mathbb {E} (\sum^ {\infty} \sigma^ {\tau} \mathcal {R} _ {m} ^ {E R} (t + \tau + 1) | s ^ {E R} (t) = s ^ {E R}, \tag {23}
$$

$$
\pmb {a} (t) ^ {\tau = 0} E R = \pmb {a} ^ {E R}, \pi_ {m} ^ {E R}),
$$

where σ is a constant discounted factor with $\sigma \in [ 0 , 1 ]$ , and the value of (23) is termed as action value, i.e., Q value.

For striking a balance between exploration and exploitation, in this paper, we consider an -greedy exploration strategy for the leader UAV energy replenishment learner. Specifically, the leader UAV energy replenishment learner in UAV m selects a random action aERm $\mathbf { \bar { \mathbf { \Phi } } } _ { a _ { m } } ^ { E R } \in \mathbf { \Phi } \mathcal { A } _ { m } ^ { E R }$ in state $s ^ { E R } ~ \in ~ { \mathcal { S } } ^ { E R }$ with probability , and selects the best action $a _ { m } ^ { E R * }$ with probability $( 1 - \epsilon )$ $\hookrightarrow E R \bigl ( s ^ { E R } , { \pmb { a } } ^ { E R } , \pi _ { m } ^ { E R } \bigr ) , \forall { \pmb { a } } ^ { E R } \in \mathscr { A } ^ { E R }$ m  m   aER, πERm ), ∀aER ∈ AER with aER∗m being the m- $Q _ { m } ^ { E R } ( s ^ { ' \nu R } , { \pmb a } ^ { E R \ast } , \pi _ { m } ^ { E R } ) \ \dot { \geq }$ ( s E R , $a _ { m } ^ { E R * }$ ER) $\mathbf { \Delta } _ { \mathbf { \mathfrak { a } } ^ { E R * } }$ $a _ { m } ^ { E R } \in \mathcal { A } _ { m } ^ { E R }$ aEm in state $s ^ { E R }$ can be expressed by:

$$
\begin{array}{l} \pi_ {m} ^ {E R} (s ^ {E R}, a _ {m} ^ {E R}) \\ = \left\{ \begin{array}{l} 1 - \epsilon , \text { if } Q _ {m} ^ {E R} (s ^ {E R}, \cdot , \cdot) \text { of } a _ {m} ^ {E R} \text { is   the   highest }, \\ \epsilon , \text { otherwise }. \end{array} \right. \tag {24} \\ \end{array}
$$

In the Q value update step of Q-learning, the leader UAV energy replenishment learner follows the update rule:

$$
\begin{array}{l} Q _ {m} ^ {E R} (s ^ {E R}, \boldsymbol {a} ^ {E R}, t + 1) = \\ Q _ {m} ^ {E R} (s ^ {E R}, \boldsymbol {a} ^ {E R}, t) + \beta^ {E R} (\mathcal {R} _ {m} ^ {E R} (t) + \\ \max _ {\boldsymbol {a} ^ {E R ^ {\prime}} \in \mathcal {A} ^ {E R}} \sigma Q _ {m} ^ {E R} (s ^ {E R ^ {\prime}}, \boldsymbol {a} ^ {E R ^ {\prime}}, t) - Q _ {m} ^ {E R} (s ^ {E R}, \boldsymbol {a} ^ {E R}, t)), \tag {25} \\ \end{array}
$$

where $\beta ^ { E R }$ denotes the learning rate of the leader UAV energy replenishment learner.

Since the settings of other learners are similar to those of leader UAV energy replenishment learner, the settings of other learners are omitted here for conciseness.

Algorithm 1: RLDC Algorithm   
1 Initialize Q value: $Q_{m}^{ER} = Q_{m}^{AP} = Q_{m}^{LT} = Q_{n}^{DC} = Q_{n}^{ER} = Q_{n}^{TD} = 0,$ $\forall m \in M, n \in N.$ 2 Set the maximal iteration counter LOOP, loop = 0 and sum = 0.

3 for loop < LOOP do

4    Set t = 0.
5    while t ≤ T do

6    for m = 1 to M do
7    Observe state $s^{ER}(t)$ , $s^{AP}(t)$ , $s^{LT}(t)$ .
8    Select $a_{m}^{ER}(t)$ according to $\pi_{m}^{ER}(s^{ER}, \cdot)$ .
9    if $\varepsilon_{m}(t) = 1$ then
10    Select $a_{m}^{AP}(t)$ according to $\pi_{m}^{AP}(s^{AP}, \cdot)$ .
11    else
12    Select $a_{m}^{LT}(t)$ according to $\pi_{m}^{LT}(s^{LT}, \cdot)$ .
13    for n = 1 to N do
14    Observe state $s^{DC}(t)$ , $s^{FT}(t)$ , $s^{TD}(t)$ .
15    Select $a_{n}^{DC}(t)$ according to $\pi_{n}^{DC}(s^{DC}, \cdot)$ .
16    Select $a_{n}^{FT}(t)$ according to $\pi_{n}^{FT}(s^{FT}, \cdot)$ .
17    Select $a_{n}^{TD}(t)$ according to $\pi_{n}^{TD}(s^{TD}, \cdot)$ .
18    Obtain the $E^{effi}(t)$ and the rewards $R_{m}^{ER}(t)$ , $R_{m}^{AP}(t)$ , $R_{m}^{LT}(t)$ , $R_{n}^{DC}(t)$ , $R_{n}^{FT}(t)$ and $R_{n}^{TD}(t).$ 19    Update the Q values $Q_{m}^{ER}(t)$ , $Q_{m}^{AP}(t)$ , $Q_{m}^{LT}(t)$ , $Q_{n}^{DC}(t)$ , $Q_{n}^{FT}(t)$ and $Q_{n}^{TD}(t).$ 20    Set $t = t + 1.$ 21    Set sum = sum + ∑ $_{t=1}^T E^{effi}(t)$ 22    Set loop = loop + 1.

23 Output: sum/loop

TABLE I SIMULATION PARAMETERS 

<table><tr><td>Param.</td><td>Value</td><td>Param.</td><td>Value</td><td>Param.</td><td>Value</td></tr><tr><td>M</td><td>3</td><td> $H_{L}$ </td><td>150m</td><td> $p^{L}$ </td><td>2W</td></tr><tr><td>N</td><td>9</td><td> $H_{F}$ </td><td>120m</td><td> $p^{F}$ </td><td>0.2W</td></tr><tr><td>K</td><td>500</td><td>t</td><td>30s</td><td> $f^{L}$ </td><td>2Mbps</td></tr><tr><td>C</td><td>10</td><td>v</td><td>20m/s</td><td> $f^{F}$ </td><td>2Mbps</td></tr><tr><td> $S_{L}$ </td><td>6</td><td>B</td><td>10MHz</td><td>q</td><td>100m</td></tr><tr><td> $S_{F}$ </td><td>4</td><td>f</td><td>3GHz</td><td> $\varpi$ </td><td>-174dBm/Hz</td></tr><tr><td> $\xi$ </td><td> $10^{-18}$ </td><td> $\kappa_{k,c}$ </td><td>10Mbits</td><td>Target region</td><td>2500m  $\times$  2500m</td></tr></table>

Overall, the RLDC algorithm is illustrated in Algorithm 1.

# IV. SIMULATION RESULTS

In this section, we conduct extensive simulations to evaluate the performance of the proposed RLDC algorithm. The values of all simulation parameters are listed in Table I. Similar settings have also been utilized in previous work [12], [13].

For the purpose of comparison, we introduce two benchmark algorithms: a fixed UAV swarm algorithm and a no UAV swarm algorithm. Fixed swarm algorithm is originally designed to maximize the energy efficiency of all UAVs without considering dynamic clustering based on RLDC algorithm. No UAV swarm algorithm is originally designed to maximize the energy efficiency of all UAVs without considering UAV swarms based on RLDC algorithm.

Fig. 2 examines the energy efficiency of all UAVs as the amount of IoT devices varies. Obviously, the energy efficiency of all UAVs exhibits a monotonically increasing trend with the increasing number of IoT devices. This can be attributed to the generation of more task requests by IoT devices as their quantity grows. Furthermore, the results also demonstrate that the proposed RLDC algorithm surpasses both the fixed UAV swarm and no UAV swarm algorithm. This superiority arises from several reasons: i) in cases where the task requests from IoT devices are dynamically changing, the fixed UAV swarm can not dynamically cluster according to the ever-changing task requests, and thereby, many tasks can not be processed; ii) the storage capacities of each UAV are limited, and furthermore, they are unable to delegate the incapable tasks to other UAVs.

![](images/b71780075bcb364608b573106903ed2fba76c79ca9a694a637d22511abf92850.jpg)

<details>
<summary>line</summary>

| Amount of IoT Devices | Proposed RLDC | Fixed Swarm | No Swarm |
| --------------------- | ------------- | ----------- | -------- |
| 100                   | 0             | 0           | 0        |
| 300                   | 320           | 280         | 220      |
| 500                   | 400           | 350         | 280      |
| 700                   | 480           | 420         | 350      |
| 900                   | 520           | 460         | 380      |
| 1100                  | 560           | 500         | 410      |
| 1300                  | 600           | 530         | 430      |
| 1500                  | 640           | 550         | 450      |
| 1700                  | 670           | 560         | 470      |
| 1900                  | 680           | 570         | 480      |
</details>

Fig. 2. Energy efficiency w.r.t. the amounts of IoT devices.

![](images/4f28ebc554b25d178d5cbb0995ee9c290c859f1d774378e71f59d0a023688c56.jpg)

<details>
<summary>line</summary>

| UAV Velocity (m/s) | Proposed RLDC | Fixed Swarm | No Swarm |
| ------------------ | ------------- | ----------- | -------- |
| 10                 | 0             | 0           | 0        |
| 15                 | 250           | 230         | 150      |
| 20                 | 380           | 340         | 260      |
| 25                 | 400           | 370         | 280      |
| 30                 | 420           | 390         | 300      |
| 35                 | 410           | 380         | 290      |
| 40                 | 400           | 370         | 280      |
| 45                 | 380           | 350         | 260      |
| 50                 | 350           | 320         | 220      |
</details>

Fig. 3. Energy efficiency w.r.t. UAV velocities.

![](images/c6261ddc65f8d1e6bdf26c27ba4ed6b36c8560dc0100fd905187e3fd13a81a1e.jpg)

<details>
<summary>line</summary>

| Storage Capacity of Each Leader UAV | Grid Size=25m | Grid Size=50m | Grid Size=75m |
| ----------------------------------- | ------------- | ------------- | ------------- |
| 1                                   | 200           | 240           | 100           |
| 2                                   | 220           | 260           | 105           |
| 3                                   | 230           | 280           | 110           |
| 4                                   | 240           | 300           | 110           |
| 5                                   | 250           | 320           | 110           |
| 6                                   | 260           | 340           | 110           |
| 7                                   | 270           | 360           | 110           |
| 8                                   | 275           | 375           | 110           |
| 9                                   | 280           | 390           | 110           |
| 10                                  | 285           | 400           | 110           |
</details>

Fig. 4. Energy efficiency w.r.t. storage capacities of each leader UAV.

Fig. 3 illustrates the energy efficiency of all UAVs as the UAV velocity varies. Obviously, the energy efficiency of all UAVs initially increases and then decreases with the UAV velocity increasing. Because as the velocity of UAVs increases, there is a reduction in the time taken for movement. As a result, UAVs have more time available for hovering and processing tasks. However, the increase in the number of processing tasks is offset by the higher energy consumption of UAVs caused by their fast velocity. As a result, the drawbacks ultimately outweigh the benefits. The explanations of the proposed RLDC algorithm outperforms the other two algorithms are consistent with those discussed in Fig. 2.

Fig. 4 demonstrates the energy efficiency of all UAVs with varying storage capacities for each leader UAV. It can be observed that the performance under grid size 50m outperforms 25m and 75m. The reason is that grid size 25m includes fewer IoT devices, leading to decreased number of tasks processed by UAVs. In contrast, while the grid size of 75m may contain more IoT devices, it also results in a substantial increase in the energy consumption of UAVs during movement. Therefore, among these three sizes, the grid size of 50m is the most suitable. Furthermore, the results also indicate that the energy efficiency of all UAVs increases as the storage capacity of each UAV grows, which can be attributed to the increased ability to process more types of applications for each UAV.

# V. CONCLUSION

In this paper, with the aim of maximizing the long-term energy efficiency of the UAV swarm assisted MEC system, a joint optimization problem of UAVs’ dynamic clustering and scheduling is formulated. By taking into account the inherent cooperation and competition among intelligent UAVs, we reformulate the optimization problem as a series of coupled multi-agent stochastic games, and then propose a novel RLDC algorithm for obtaining equilibriums. Simulation results show that, compared to counterparts, the proposed RLDC algorithm can significantly increase the energy efficiency of the UAV swarm assisted MEC system.

# REFERENCES

[1] Y. Liao, X. Chen, S. Xia, Q. Ai, and Q. Liu, “Energy minimization for UAV swarm-enabled wireless inland ship MEC network with time windows,” IEEE Trans. Green Commun. Netw., vol. 7, no. 2, pp. 594–608, June 2023.   
[2] Y. Shi, C. Yi, R. Wang, Q. Wu, B. Chen, and J. Cai, “Service migration or task rerouting: A two-timescale online resource optimization for MEC,” IEEE Trans. Wirel. Commun., pp. 1–1, July 2023.   
[3] W. He, H. Yao, T. Mai, F. Wang, and M. Guizani, “Three-stage stackelberg game enabled clustered federated learning in heterogeneous UAV swarms,” IEEE Trans. Veh. Technol., vol. 72, no. 7, pp. 9366–9380, July 2023.   
[4] C. Zhan and Y. Zeng, “Completion time minimization for multi-UAVenabled data collection,” IEEE Trans. Wireless Commun., vol. 18, no. 10, pp. 4859–4872, Oct. 2019.   
[5] J. Chen, C. Yi, J. Li, K. Zhu, and J. Cai, “A triple learner based energy efficient scheduling for multi-UAV assisted mobile edge computing,” in Proc. IEEE ICC, Jun. 2023.   
[6] K. Wang, X. Zhang, L. Duan, and J. Tie, “Multi-UAV cooperative trajectory for servicing dynamic demands and charging battery,” IEEE Trans. Mob. Comput., vol. 22, no. 3, pp. 1599–1614, Mar. 2023.   
[7] T. Li, S. Leng, Z. Wang, K. Zhang, and L. Zhou, “Intelligent resource allocation schemes for UAV-swarm-based cooperative sensing,” IEEE Internet Things J., vol. 9, no. 21, pp. 21 570–21 582, Nov. 2022.   
[8] A. Mukherjee, S. Misra, V. S. P. Chandra et al., “Resource-optimized multiarmed bandit-based offload path selection in edge UAV swarms,” IEEE Internet Things J., vol. 6, no. 3, pp. 4889–4896, June 2019.   
[9] J. Li, C. Yi, J. Chen, K. Zhu, and J. Cai, “Joint trajectory planning, application placement, and energy renewal for UAV-assisted MEC: A triple-learner-based approach,” IEEE Internet of Things J., vol. 10, no. 15, pp. 13 622–13 636, Aug. 2023.   
[10] Y. Zeng, J. Xu, and R. Zhang, “Energy minimization for wireless communication with rotary-wing UAV,” IEEE Trans. Wireless Commun., vol. 18, no. 4, p. 2329–2345, Apr. 2019.   
[11] R. Chen, C. Yi, K. Zhu, B. Chen, J. Cai, and M. Guizani, “A three-party hierarchical game for physical layer security aware wireless communications with dynamic trilateral coalitions,” IEEE Trans. Wirel. Commun., Oct. 2023.   
[12] C. Zhao, J. Liu, M. Sheng, W. Teng, Y. Zheng, and J. Li, “Multi-UAV trajectory planning for energy-efficient content coverage: A decentralized learning-based approach,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 3193–3207, Oct. 2021.   
[13] B. Liu, Y. Wan, F. Zhou, Q. Wu, and R. Hu, “Resource allocation and trajectory design for MISO UAV-assisted MEC networks,” IEEE Trans. Veh. Technol., vol. 71, no. 5, pp. 4933–4948, May 2022.