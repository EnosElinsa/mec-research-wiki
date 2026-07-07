# Throughput Maximization for UAV-Enabled Integrated Periodic Sensing and Communication

Kaitao Meng , Member, IEEE, Qingqing Wu , Senior Member, IEEE, Shaodan Ma , Senior Member, IEEE,

Wen Chen , Senior Member, IEEE, Kunlun Wang , Member, IEEE, and Jun Li , Senior Member, IEEE

Abstract— Driven by unmanned aerial vehicle (UAV)’s advantages of flexible observation and enhanced communication capability, it is expected to revolutionize the existing integrated sensing and communication (ISAC) system and promise a more flexible joint design. Nevertheless, the existing works on ISAC mainly focus on exploring the performance of both functionalities simultaneously during the entire considered period, which may ignore the practical asymmetric sensing and communication requirements. In particular, always forcing sensing along with communication may make it is harder to balance between these two functionalities due to shared spectrum resources and limited transmit power. To address this issue, we propose a new integrated periodic sensing and communication (IPSAC) mechanism for the UAV-enabled ISAC system to provide a more flexible trade-off between two integrated functionalities. Specifically, the system achievable rate is maximized via jointly optimizing UAV trajectory, user association, target sensing selection, and transmit beamforming, while meeting the sensing frequency and beam pattern gain requirement for the given targets. Despite that this problem is highly non-convex and involves closely coupled integer variables, we derive the closed-form optimal beamforming vector to dramatically reduce the complexity of beamforming design, and present a tight lower bound of the achievable rate to facilitate UAV trajectory design. Based on the above results, we propose a two-layer penalty-based algorithm to efficiently solve the considered problem. To draw more important insights, the optimal achievable rate and the optimal UAV location are analyzed under a special case of infinity number of antennas. Furthermore, we prove the structural symmetry between the optimal solutions in different ISAC frames without location constraints

in our considered UAV-enabled ISAC system. Based on this, we propose an efficient algorithm for solving the problem with location constraints. Numerical results validate the effectiveness of our proposed designs and also unveil a more flexible trade-off in ISAC systems over benchmark schemes.

Index Terms— Integrated sensing and communication, UAV, periodic sensing, user association, beamforming, trajectory optimization.

## I. INTRODUCTION

D <sup>RIVEN</sup> <sup>by</sup> <sup>spectrum</sup> <sup>reuse</sup> <sup>potential</sup> <sup>and</sup> <sup>enormous</sup>demands of robust sensing ability, there is a recent demands of robust sensing ability, there is a recent surge of interest in the development of integrated (radar) sensing and communications (ISAC) techniques for both academia and industry [1], [2]. Different from the spectrum sharing between separate radar sensing and communication systems [3], ISAC shares the same wireless infrastructures for simultaneously conveying information to the receiver and extracting information from the scattered echoes [4]. Thus, ISAC could not only achieve integration gain to significantly enhance the spectrum utilization efficiency and reduce hardware costs, but also introduce coordination gain to efficiently balance between two functionalities’ performance [4], [5]. With the advancements of massive antennas and millimeter wave (mmWave)/terahertz (THz), ISAC base stations (BSs) could also provide higher sensing resolution and accuracy to enable many location-aware intelligent applications with stringent sensing requirements [6]. Several similar terminologies have been utilized to describe this related research, such as radar-communication (RadCom) [7], [8], dual-functional radar communication (DFRC) [9], [10], joint communication and radar sensing (JCAS) [11], [12]. In the industry, ISAC is regarded as a key technology in Huawei and Nokia for future wireless network investigations [13], [14]; “Hexa-X” project supported by European Commission focuses on extending the localization and sensing capabilities for 6G [15]; Project IEEE 802.11bf plans to develop WLAN sensing by analyzing the received WLAN signals to recognize the features of the intended targets in a given environment [16].

The prior works on ISAC systems have shown that co-designed waveform and beamforming could provide mutual benefits of both sensing and communication [17], [18], [19], [20], [21]. For instance, a joint transmit beamforming model was proposed to optimize the radar transmit beam pattern while meeting the requirement of the signal-to-interferenceplus-noise ratio (SINR) at each communication user [19].

The authors in [20] proposed a Pareto optimization framework of the DFRC system to analyze the achievable performance region of communication and sensing. However, the performance of sensing is generally dependent on the explicit lineof-sight (LoS) links between targets and transceivers, while non-Los (NLoS) links are treated as unfavorable interference for the target sensing. For the potential targets located far away from BSs or blocked by obstacles, the sensing performance will severely degrade or the sensing missions may even fail because of serious path loss of the echoed signals. Hence, terrestrial ISAC BSs could only provide sensing and communication services within a fixed range due to limited transmit power and NLoS signal paths caused by surrounding obstacles.

Driven by the unmanned aerial vehicle (UAV)’ on-demand deployment and strong LoS links features [22], [23], it is expected to be a cost-effective aerial platform to provide enhanced ISAC service. In particular, more flexible observation, better communication quality, larger service coverage could be achieved by exploiting the high mobility of UAVs [24], [25]. Traditional works on UAV-enabled wireless networks mainly focused on the separate design of sensing and/or communication [26], [27], [28], instead of considering integrated waveform and beamforming design for sensing and communication. Different from the separate-design sensing and communication systems, the achievable rate for the UAV-enabled ISAC system is influenced by multiple complicated factors, including beam pattern constraints, resource allocation, as well as beamforming design closely coupled with UAV trajectory. Therefore, this difference leads to a new challenge for the achievable rate maximization problem in UAV-enabled ISAC systems. Most recently, there are several works studying the trajectory or deployment optimization issue in UAV-based ISAC [29], [30], [31]. For instance, the authors in [29] proposed a joint UAV maneuver and transmit beamforming optimization algorithm to maximize the communication performance while ensuring the sensing requirements for the given targets. By deploying multiple UAVs to perform tasks cooperatively, greater coverage of ISAC networks can be achieved [30]. Besides, ISAC-enabled cellular networks can be utilized to monitor and localize the suspicious UAV targets in the sky to protect the physical security [32].

However, the above works on ISAC [17], [18], [19], [20], [21], [29], [30], [32] mainly focused on exploring the performance of both functionalities simultaneously during the entire considered period, where all sensing tasks are performed together with communication all the time. This may ignore the asymmetric sensing and communication requirements in practical systems. In other words, the sensing frequency could be different from the data frame rate. For example, for target tracking scenarios, a relatively low/high sensing frequency is preferred for a low-speed/high-speed object. Hence, sensing frequency should be set based on the targets’ motion state and the timeliness requirement of the specific tasks. Nonetheless, this important aspect of ISAC systems, sensing frequency, has not been taken into account in the literature. On the other hand, always forcing sensing along with communication all the time may introduce excessive sensing, making it is harder to balance between these two functionalities. Furthermore, excessive sensing may result in the waste of spectrum resources and stronger interference to communication users, thereby limiting the performance of communication users. Moreover, forcing both functionalities to work simultaneously will also inevitably cause higher energy consumption, which is unfavorable for the equipment with insufficient energy (e.g., power limited UAVs [33]). Therefore, there is an urgent need to investigate the achievable rate improvement in such scenarios by considering the sensing frequency besides the commonly used sensing power, especially for UAV-enabled ISAC systems due to its autonomous mobility. Note that the fixed-deployment ISAC system considering the sensing frequency is actually a special case of our work. By optimizing the UAV trajectory, the flexibility of beam design and the efficiency of task association for ISAC systems can be further improved. This knowledge gap motivates us to develop effective UAV-enabled ISAC mechanisms to fulfill a more general and flexible trade-off between sensing and communication.

![](images/f2d88ebdcff849acf6efc1f71b71fc01452c90f66776d3303eb178846d04ac8b.jpg)  
Fig. 1. The illustration of UAV-enabled integrated sensing and communication scenarios.

With the above consideration, we study a UAV-enabled ISAC system where one UAV is dispatched to perform sensing tasks while providing downlink communication services for several single-antenna users, as shown in Fig. 1. Considering the practical sensing frequency requirements, we propose an integrated periodic sensing and communication (IPSAC) mechanism where all sensing tasks are periodically executed along with the communication service. Specifically, the achievable rate maximization problem is investigated by jointly optimizing the transmit beamforming, user association, sensing time selection, and UAV trajectory in this work, subject to the sensing frequency and beam pattern gain requirements. As compared to traditional ISAC considered in [29], which always forces the UAV to perform sensing tasks and provide communication service at the same time, our proposed scheme is more general and offers more flexibility to balance between practical sensing and communication over time. Besides, by setting the frequency to infinity or the minimum threshold, it is not difficult to find that both standalone communication and always-sensing are special cases of our considered periodic sensing and communication scenarios.

However, solving this periodic ISAC optimization problem is highly non-trivial. Specifically, it is non-convex and involves integer variables which are closely coupled with UAV trajectory and beamforming vectors. Unlike traditional trajectory optimization problem for single-antenna UAVs, joint beamforming and UAV trajectory optimization problem for ISAC is very complicated, since the location of the UAV is coupled with beamforming vector in a more complex form. Also, the complexity of the trajectory discretization-based method will become intractable in practical scenarios with long mission periods [34]. To address this issue, we first propose a twolayer penalty-based algorithm to solve the achievable rate maximization problem by decoupling the optimized variables and then propose a low-complexity algorithm to solve the considered problem more efficiently. The main contribution in this paper is summarized as follow

• First, we propose a UAV-enabled IPSAC mechanism to achieve a more general and flexible trade-off between sensing power requirement, sensing frequency, and communication performance for multi-users and multi-targets scenarios. Furthermore, we formulate a periodic ISAC problem to maximize the achievable rate while satisfying sensing frequency and beam pattern gain constraints.

• Next, we derive the closed-form beamforming vector under any given UAV location, and present the closed-form optimal achievable rate and sensing location if the number of antennas is infinity, thereby providing guidance for algorithm design. By introducing a tight lower bound of the original objective function, a penaltybased algorithm is proposed to jointly optimize beamforming, user association, sensing time selection, and UAV trajectory.

• Furthermore, to draw useful insights, we prove a novel characteristic of structural symmetry between the optimal solutions in different ISAC frames without initial and final location constraints. Accordingly, we reveal the monotonic relationship between sensing frequency and communication capacity in our considered IPSAC system. Based on this, a low-complexity solution can be constructed while achieving high-quality performance.

• Finally, simulation results unveil a more flexible trade-off in ISAC systems over benchmark schemes and show that the UAV trajectory design plays an important role in balancing sensing and communication performance in IPSAC mechanisms. It is also found that the UAV tends to provide communication services while sensing the target closer to the associated user.

The remainder of this paper is organized as follows. Section II introduces the system model and problem formulation of the UAV-enabled IPSAC system. In Section III, we derive the closed-form optimal beamforming vector and propose a penalty-based algorithm to address the sum achievable rate maximization problem. Section IV presents the symmetrical structure characteristic among ISAC frames and a low-complexity algorithm. Section V provides numerical results to validate the performance of our proposed mechanism. Section VI concludes this paper.

Notations: -x- denotes the Euclidean norm of a complex-valued vector x. For a general matrix X, X , $\boldsymbol { X } ^ { H ^ { \bullet } } , \boldsymbol { X } ^ { T }$ , and $[ X ] _ { p , q }$ denote its rank, conjugate transpose, transpose, and the element in the <sup>p</sup>th row and <sup>q</sup>th column, respectively. For a square matrix $Y , \operatorname { t r } ( Y )$ and $\bar { \pmb { Y } } ^ { - 1 }$ denotes its trace and inverse, respectively, while $Y \succeq 0$ represents that Y is a positive semidefinite matrix. <sup>j</sup> denotes the imaginary unit, $\operatorname { i . e . , } \ j ^ { 2 } = - 1$ . The distribution of a circularly symmetric complex Gaussian (CSCG) random variable with mean <sup>x</sup> and variance $\sigma ^ { 2 }$ is denoted by ${ \mathcal { C N } } ( x , \sigma ^ { 2 } )$ .

![](images/a731b05974ca333a9915a1af94586efd18afc91a444b4ad13db27f95ff1c22f8.jpg)  
Fig. 2. IPSAC mechanism for multi-users and multi-targets scenarios.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

We consider a UAV-enabled ISAC system aimed at sensing several prospective ground targets while providing downlink communication service for $K$ single-antenna users within a given flight period $T \ s .$ The set of the users and that of the prospective targets are denoted by $\mathcal { K } = \{ 1 , \cdots , K \}$ and $\mathcal { I } =$ $\{ 1 , \cdots , J \}$ , respectively. The horizontal location of user <sup>k</sup> is denoted by $\pmb { u } _ { k } = [ u _ { x , k } , u _ { y , k } ] ^ { T }$ , which can be either obtained by global positioning system (GPS) or estimated by uplink signals [35]. The horizontal locations of the potential targets are denoted by $\pmb { v } _ { j } = [ v _ { x , j } , v _ { y , j } ] ^ { T } , j \in \mathcal { I }$ . The value of $v _ { j }$ is determined based on the specific sensing tasks. For example, $\boldsymbol { v } _ { j }$ can be set as the estimated location based on the previous frames for target tracking, or set as a uniformly sampled positions in the region of interest for target detection. The whole mission period $T$ can be discretized into <sup>N</sup> time slots with duration $\begin{array} { r } { \delta _ { t } = \frac { T } { N } . } \end{array}$ , and the index of time slot is denoted by $n \in \mathcal { N } = \{ 1 , \cdots , N \}$ . Here, the time slot is chosen to be sufficiently small, during which the UAV’s location is assumed to be approximately unchanged to facilitate the trajectory and beamforming design for ISAC. The UAV’s horizontal location is denoted by $\mathbf { \bar { q } } [ n ] = [ q _ { x } [ n ] , q _ { y } [ n ] ] ^ { T }$ , where $n \in \mathcal N$ , and the UAV is assumed to fly at a constant altitude of <sup>H</sup> m subject to air traffic control [36]. The general uniform plane array (UPA) is adopted at the UAV, where the number of antennas is denoted by $M = M _ { x } \times M _ { y }$ with $M _ { x }$ and $M _ { y }$ denoting the number of elements along the <sup>x</sup>- and <sup>y</sup>-axis, respectively. The adjacent elements are separated by $\begin{array} { r } { d _ { x } \ = \ d _ { y } \ = \ \frac { \lambda } { 2 } } \end{array}$ , where <sup>λ</sup> denotes the carrier wavelength. Specifically, the UPA is parallel to the ground to facilitate the technical derivation, as shown in Fig. 1.

## A. ISAC Frame

Based on the practical timeliness requirements of sensing tasks, we propose an IPSAC mechanism for multi-user and multi-target scenarios to find a fundamental trade-off between sensing and communication. Specifically, it is assumed that each sensing task should be performed at least once in each ISAC frame, as shown in Fig. 2. Assuming that the total frame number $\begin{array} { r } { L = \frac { T } { T _ { L } } } \end{array}$ is an integer for ease of analysis, where $T _ { L }$ is the frame length.<sup>1</sup> Then, the number of time slots in each ISAC frame is $\begin{array} { r } { N _ { L } = \frac { N } { L } } \end{array}$ and the index of ISAC frame is denoted by $l \in \mathcal { L } = \{ 1 , \cdots , L \}$ . In our proposed IPSAC mechanism, time division multiple access (TDMA) is adopted to avoid signal interference between different information beams due to strong LoS channel, while each target could be sensed in any time slot of each ISAC frame. If the UAV aims to sense target <sup>j</sup> at time slot $n ,$ we denote $c _ { j } [ n ] = 1$ . Otherwise, $c _ { j } [ n ] = 0$ <sup>[ ] = 1</sup>. Also, at most one target can be sensed in each time slot. By performing sensing tasks separately in different time slots, the computational complexity of the target estimation algorithm can be reduced. Based on the above discussion, the following conditions hold

$$
\sum _ { n = ( l - 1 ) N _ { L } + 1 } ^ { l N _ { L } } c _ { j } [ n ] = 1 , \forall l , j ,\tag{1}
$$

$$
\sum _ { j = 1 } ^ { J } c _ { j } [ n ] \leq 1 , \forall n .\tag{2}
$$

Then, the sensing frequency of each target is defined as $1 / T _ { L } = 1 / ( \delta { \cal N } _ { L } )$

## B. Communication and Sensing Model

The communication links between the UAV and the user are assumed to be dominated by the LoS component [37]. Hence, the aerial-ground channel follows the free-space path loss model and the channel power gain from the UAV to user <sup>k</sup> can be expressed as

$$
\beta _ { k } ( \pmb q [ n ] , \pmb u _ { k } ) = \beta _ { 0 } d ( \pmb q [ n ] , \pmb u _ { k } ) ^ { - 2 } = \frac { \beta _ { 0 } } { H ^ { 2 } + \| \pmb q [ n ] - \pmb u _ { k } \| ^ { 2 } } ,\tag{3}
$$

where $\beta _ { 0 }$ represents the channel power at the reference distance 1 m. Besides, the Doppler effect induced by the UAV mobility is assumed to be well compensated at the communication users [24], [38] and the sensing receiver [39], [40], respectively. The transmit array response vector of the UAV towards user $k ' \mathrm { s }$ location $\mathbf { \Delta } \mathbf { u } _ { k }$ is

$$
\begin{array} { r l } &  { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } \quad { \mathbf { } } { \mathbf { } } \quad { \mathbf { } } { \mathbf { } } \quad { \mathbf { } } { \mathbf { } } \quad { \mathbf { } { } } { \mathbf { } } \quad { \mathbf { } { } } { \mathbf { } } \quad { \mathbf { } { } } { \mathbf { } } \quad { \mathbf { } { } } \quad { \mathbf { } } { \mathbf { } } \quad { \mathbf { } { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad { \mathbf { } } \quad  \end{array}\tag{4}
$$

In (4), $\Phi ( { \pmb q } [ n ] , { \pmb u } _ { k } ) = \sin ( \phi ( { \pmb q } [ n ] , { \pmb u } _ { k } ) ) \cos ( \theta ( { \pmb q } [ n ] , { \pmb u } _ { k } ) ) =$ $\frac { q _ { x } \left[ n \right] - u _ { x , k } } { \left\| \bar { \pmb q } \left[ n \right] - \bar { \pmb u } _ { k } \right\| }$ , where $\begin{array} { r l r } { \pmb { \bar { q } } [ n ] } & { { } = } & { [ q _ { x } , q _ { y } , H ] ^ { T } } \end{array}$ , and $\begin{array} { r l } { \bar { \mathbf { \ b { u } } } _ { k } } & { { } = } \end{array}$ $[ u _ { x , k } , u _ { y , k } , 0 ] ^ { T }$ . And $\begin{array} { r l r } { \Omega ( { \pmb q } [ n ] , { \pmb u } _ { k } ) } & { { } = } & { \sin ( \phi ( { \pmb q } [ n ] , { \pmb u } _ { k } ) ) } \end{array}$ sin $\begin{array} { r l r } { ( \theta ( \pmb q [ n ] , \pmb u _ { k } ) ) } & { = } & { \frac { q _ { y } [ n ] - u _ { y , k } } { \| \bar { \pmb q } [ n ] - \bar { \pmb u } _ { k } \| } . \phi ( \pmb q [ n ] , \pmb u _ { k } ) } \end{array}$ represents the zenith angle of departure (AoD) of the signal from the UAV to user <sup>k</sup>’s location ${ \mathbf { } } { \mathbf { } } u _ { k } .$ , and $\theta ( \pmb q [ n ] , \pmb u _ { k } )$ represents its corresponding azimuth AoD. Therefore, the baseband equivalent channel from the UAV to user <sup>k</sup> can be expressed as

$$
h _ { k } ^ { H } \left( q [ n ] , { \pmb u } _ { k } \right) = \sqrt { \beta _ { k } ( { \pmb q } [ n ] , { \pmb u } _ { k } ) } e ^ { - \jmath \frac { 2 \pi d ( { \pmb q } [ n ] , { \pmb u } _ { k } ) } { \lambda } } { \pmb a } ^ { H } \left( { \pmb q } [ n ] , { \pmb u } _ { k } \right) .\tag{5}
$$

Without loss of generality, we assume that the UAV can transmit the information-bearing signal $\scriptstyle { \pmb { s } } _ { k }$ to user <sup>k</sup>, where $s _ { k } , \sim \mathcal { C N } ( 0 , 1 )$ . Moreover, the communication signals are uncorrelated with each other, i.e., $E \left( s _ { k } [ n ] s _ { k ^ { \prime } } [ n ] \right) = 0$ , where $k \neq k ^ { \prime } ,$ , and $k , k ^ { \prime } \in \mathcal { K } \left[ 4 1 \right]$ . The linear transmit precoding is applied at the UAV for the assigned user and target. Hence, the complex baseband transmitted signal at the UAV can be expressed as a weighted sum of communication signals, i.e.,

$$
\pmb { x } [ n ] = \pmb { w } _ { c } [ n ] \sum _ { k = 1 } ^ { K } \alpha _ { k } [ n ] s _ { k } [ n ] , n \in \mathcal { N } ,\tag{6}
$$

where ${ \pmb w } _ { c } [ n ] ~ \in ~ \mathbb { C } ^ { M \times 1 }$ is the corresponding information beamforming vector, and $\alpha _ { k } [ n ] \ = \ 1$ if the UAV transmits signal $s _ { k }$ to user <sup>k</sup> at the <sup>n</sup>th time slot, otherwise, $\alpha _ { k } [ n ] = 0$ Since the UAV only serves at most one user at each time slot, we have the following constraint

$$
\sum _ { k = 1 } ^ { K } \alpha _ { k } [ n ] \leq 1 , ~ \forall , n .\tag{7}
$$

Then, at the <sup>n</sup>th time slot, the received signal at user <sup>k</sup> is

$$
y _ { k } [ n ] = h _ { c , k } ^ { H } \left( q [ n ] , { \pmb u } _ { k } \right) \left( { \pmb w } _ { c } [ n ] \sum _ { k = 1 } ^ { K } \alpha _ { k } [ n ] s _ { k } [ n ] \right) + n _ { k } [ n ] ,\tag{8}
$$

where $n _ { k } [ n ] \sim \mathcal { C N } ( 0 , \sigma _ { k } ^ { 2 } )$ denotes the additive white Gaussian noise (AWGN) at user <sup>k</sup>’s receiver. Accordingly, for $\alpha _ { k } [ n ] =$ , the signal-to-noise ratio (SNR) of user <sup>k</sup> is given by

$$
\gamma _ { k } [ n ] = \frac { \Big | h _ { c , k } ^ { H } \left( \pmb q [ n ] , \pmb u _ { k } \right) \pmb w _ { c } [ n ] \Big | ^ { 2 } } { \sigma _ { k } ^ { 2 } } , ~ \forall n \in \mathcal { N } .\tag{9}
$$

As a result, when $\alpha _ { k } [ n ] = 1$ , the corresponding achievable rate of user <sup>k</sup> at time slot <sup>n</sup> in bits-per-second-per-Hertz (bps/Hz) is

$$
R _ { k } [ n ] = \log _ { 2 } ( 1 + \gamma _ { k } [ n ] ) .\tag{10}
$$

As the communication signals reflected by the target can also be utilized for target parameter estimation in our considered system [18], [42], the communication signals $\{ s _ { k } [ n ] \} _ { k = 1 } ^ { K }$ are further exploited for sensing. As a result, the transmit beam pattern gain from the UAV to the direction of target <sup>j</sup> can be given by

$$
\begin{array} { r l } & { \Gamma \left( { \pmb q } [ n ] , { \pmb v } _ { j } \right) = E \left[ \left| { \pmb a } ^ { H } ( { \pmb q } [ n ] , { \pmb v } _ { j } ) \left( { \pmb x } [ n ] \right) \right| ^ { 2 } \right] } \\ & { \qquad = { \pmb a } ^ { H } ( { \pmb q } [ n ] , { \pmb v } _ { j } ) \underbrace { \left( { \pmb w } _ { c } [ n ] { \pmb w } _ { c } ^ { H } [ n ] \right) } _ { \mathrm { c o v a r i a n c e ~ m a t r i x } } { \pmb a } ( { \pmb q } [ n ] , { \pmb v } _ { j } ) . } \end{array}\tag{11}
$$

Based on the definition in (11), the power of reflected signals from target can be expressed a function of $\Gamma ( \pmb q [ n ] , \pmb v _ { j } )$ together <sup>Γ ( [ ] )</sup>with pathloss from the UAV to the given target, as shown in constraints (12a).<sup>2</sup>

## C. Problem Formulation

In this paper, we aim to maximize the achievable rate by optimizing the beamforming vector, user association, sensing time selection, and UAV trajectory, subject to the requirements of the sensing frequency, sensing power, and quality of service (QoS). Accordingly, the optimization problem is formulated as<sup>3</sup>

(P1):

$$
\operatorname* { m a x } _ { w _ { c } , A , Q , C } \ \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } \alpha _ { k } [ n ] R _ { k } [ n ]\tag{12}
$$

$$
{ \mathrm { s . t . ~ } } ( 1 ) , ( 2 ) , ( 7 ) ,
$$

$$
c _ { j } [ n ] \frac { \Gamma \left( \pmb { q } [ n ] , \pmb { v } _ { j } \right) } { d ( \pmb { q } [ n ] , \pmb { v } _ { j } ) ^ { 2 } } \ge c _ { j } [ n ] \Gamma _ { j } ^ { t h } , \quad \forall j , n ,\tag{12a}
$$

$$
c _ { j } [ n ] \in \{ 0 , 1 \} , \alpha _ { k } [ n ] \in \{ 0 , 1 \} , \forall j , k , n ,\tag{12b}
$$

$$
\frac { 1 } { N _ { L } } \sum _ { n = ( l - 1 ) N _ { L } + 1 } ^ { l N _ { L } } \alpha _ { k } [ n ] R _ { k } [ n ] \geq R _ { k } ^ { t h } ,
$$

$$
\forall k , l ,\tag{12c}
$$

$$
\left\| \pmb { w } _ { c } [ n ] \right\| ^ { 2 } \leq P _ { \operatorname* { m a x } } , \quad \forall n ,\tag{12d}
$$

$$
\| \pmb { q } [ n ] - \pmb { q } [ n - 1 ] \| \leq V _ { \operatorname* { m a x } } \delta _ { t } , \quad \forall n \in \mathcal { N } \backslash \{ 1 \} ,\tag{12e}
$$

$$
\mathbf { \pmb q } [ 1 ] = \mathbf { \pmb q } _ { I } , \mathbf { \pmb q } [ N ] = \mathbf { \pmb q } _ { F } .\tag{12f}
$$

In (P1), $C = \{ c [ n ] \} _ { n = 1 } ^ { N }$ and $A = \{ \alpha [ n ] \} _ { n = 1 } ^ { N }$ , where $c [ n ] =$ $\{ c _ { j } [ n ] \} _ { j = 1 } ^ { J }$ is the target selection at the <sup>n</sup>th time slot and ${ \pmb { \alpha } } [ n ] = \{ \alpha _ { k } [ n ] \} _ { k = 1 } ^ { K }$ is the user association at the <sup>n</sup>th time slot. Similarly, $\bar { { \pmb w } _ { c } } ~ = ~ \{ { \pmb w } _ { c } [ n ] \} _ { n = 1 } ^ { N }$ , and ${ \cal Q } ~ = ~ \{ q [ n ] \} _ { n = 1 } ^ { N }$ <sup>= [ ] = [ ]</sup>Under the given sensing frequency, the beam pattern gain constraints at the direction of targets are given by (12a), where $\Gamma _ { i } ^ { t h }$ denotes the beam pattern gain threshold of target $j$ and $d ( \pmb q [ n ] , \pmb v _ { j } ) ^ { 2 }$ represents the corresponding pathloss. The <sup>( [ ] )</sup>minimum achievable rate requirements in each ISAC frame are given by (12c) to satisfy the quality of service. The total transmit power and the maximum distance between two consecutive locations are constrained as in (12d) and (12e), respectively. The initial and final locations constraints are given by (12f). Besides, if a certain target needs both communication and sensing services (e.g., the sensing results can be utilized for communication enhancement, i.e., sensing gain achieved for communication), another user with the same location could be introduced for this case.

Solving problem (P1) is highly non-trivial, since it is non-convex and involves integer variables which are closely coupled with UAV trajectory and beamforming. To address this problem, we first derive the closed-form optimal beamforming vector and a tight lower bound of the achievable rate. Accordingly, an efficient penalty-based algorithm consisting of two layers is proposed to solve the considered problem. Furthermore, by ignoring initial and final location constraints, we prove the structural symmetry between the optimal solutions in different ISAC frames. Based on this result, a lowcomplexity algorithm is proposed to reduce the computation complexity caused by trajectory discretization, especially for the practical scenarios with long flight periods.

IMPORTANT NOTATIONS AND SYMBOLS USED IN THIS WORK
<table><tr><td>Notation</td><td>Physical meaning</td></tr><tr><td> $\overline { { { \bf { u } } _ { k } , { \bf { v } } _ { j } } }$ </td><td>Location of user k and target j</td></tr><tr><td> $\overrightarrow { \mathbf { q } ( n ] }$ </td><td>UAV&#x27;s location at the nth time slot</td></tr><tr><td>H</td><td>Altitude of the UAV</td></tr><tr><td> $V _ { \mathrm { m a x } }$ </td><td>Maximum speed of the UAV</td></tr><tr><td> $\overline { { T _ { L } } }$ </td><td>Time length of each ISAC frame</td></tr><tr><td> $\overline { { N _ { L } } }$ </td><td>Time slot number of each ISAC frame</td></tr><tr><td> $\overline { { \delta _ { t } } }$ </td><td>Time interval of discrete locations</td></tr><tr><td> $\overline { { \Gamma _ { i } ^ { t h } } }$ </td><td>Threshold of beam pattern gain for target j</td></tr><tr><td> $\overline { { \alpha _ { k } [ n ] } }$ </td><td>Variable indicating whether user k is served at time slot n</td></tr><tr><td> $\underline { { \overline { { c _ { j } [ n ] } } } }$ </td><td>Variable indicating whether target j is sensed at time slot n</td></tr><tr><td> $\underline { w _ { c } }$ </td><td>Beamforming vectors of communication signal</td></tr><tr><td> $\overline { { { \bf x } [ n ] } }$ </td><td>Complex baseband transmitted signal</td></tr><tr><td> $\overrightarrow { R _ { k } ^ { t h } }$ </td><td>Minimum constraint of the achievable rate of user k</td></tr><tr><td>A</td><td>User association matrix</td></tr><tr><td>C</td><td>Sensing time selection matrix</td></tr><tr><td> $\overline { { \boldsymbol { Q } } }$ </td><td>UAV&#x27;s trajectory vector</td></tr></table>

TABLE I

## III. PENALTY-BASED ALGORITHM TO (P1)

In this section, we first investigate the closed-form optimal beamforming vector for the proposed IPSAC mechanism in Section III-A. Then, a tight lower bound of the original objective value is provided in Section III-B, based on which, we propose a penalty-based algorithm to jointly optimize the UAV trajectory, user association, and sensing time selection in Section III-C and Section III-D.

## A. Closed-Form Optimal Beamforming

It can be found that, if $\begin{array} { r } { \sum _ { j = 1 } ^ { J } c _ { j } [ n ] = 0 } \end{array}$ and $\alpha _ { k } [ n ] = 1$ for any given UAV location, the optimal beamforming vector $\begin{array} { r } { \pmb { w } _ { c } ^ { * } ~ = ~ \sqrt { P _ { \operatorname* { m a x } } } \frac { \pmb { h } _ { c , k } ( \pmb { q } [ n ] , \pmb { u } _ { k } ) } { \lVert \pmb { h } _ { c , k } ( \pmb { q } [ n ] , \pmb { u } _ { k } ) \rVert } } \end{array}$ . Otherwise, if $c _ { j } [ n ] ~ = ~ 1$ and $\alpha _ { k } [ n ] = 1$ , the optimal beamforming vector is highly coupled <sup>[ ] = 1</sup>with the UAV trajectory. For notation convenience, denote $h _ { c , k } ^ { H } ( \pmb q [ n ] , \pmb u _ { k } )$ and $\frac { \mathbf { \boldsymbol { a } } ^ { H } ( \mathbf { \dot { q } } [ n ] , \mathbf { \boldsymbol { v } } _ { j } ) } { d ( \mathbf { \boldsymbol { q } } [ n ] , \mathbf { \boldsymbol { v } } _ { j } ) }$ as $h _ { c , k } ^ { H }$ and $h _ { r , j } ^ { H } .$ , respectively. Since maximizing $R _ { k } [ n ]$ is equivalent to maximizing the corresponding received signal strength of $\pmb { w } _ { c } ^ { H } \pmb { h } _ { c , k } \pmb { h } _ { c , k } ^ { H } \pmb { w } _ { c } ,$ the function is dropped in the objective function for simplicity. The received signal strength maximization problem is reduced to

$$
\operatorname* { m a x } _ { { \pmb w } _ { c } } ~ { \pmb w } _ { c } ^ { H } { \pmb h } _ { c , k } { \pmb h } _ { c , k } ^ { H } { \pmb w } _ { c }
$$

$$
\mathrm { s . t . } \ w _ { c } ^ { H } h _ { r , j } h _ { r , j } ^ { H } w _ { c } \geq \Gamma ^ { t h } ,\tag{13}
$$

$$
\| w _ { c } \| ^ { 2 } \leq P _ { \operatorname* { m a x } } .\tag{13a}
$$

(13b)

Although problem (13) is a non-convex optimization problem, we show that it is able to derive the optimal beamforming vector in a closed-form expression and this also facilitates the subsequent UAV trajectory optimization.

Proposition 1: When $c _ { j } [ n ] = 1$ and $\alpha _ { k } [ n ] = 1$ , for any given UAV location q <sup>n</sup> , the optimal beamforming vector can be expressed as

$$
\begin{array} { r } { w _ { c } ^ { * } = \left\{ \begin{array} { l l } { \sqrt { P _ { \operatorname* { m a x } } } \frac { h _ { c , k } } { \| h _ { c , k } \| } , } & { \tilde { \Gamma } \ge \Gamma ^ { t h } } \\ { \frac { 1 } { \lambda _ { 1 } } ( \sqrt { \beta _ { c , k } } h _ { c , k } + \lambda _ { 2 } \sqrt { \Gamma ^ { t h } } h _ { r , j } e ^ { - \jmath \varphi _ { k , j } } ) , } & { \mathrm { O t h e r w i s e } , } \end{array} \right. } \end{array}\tag{14}
$$

where $\begin{array} { r } { \varphi _ { k , j } \ = \ \operatorname { a r c c o s } \frac { \vert \boldsymbol { h } _ { c , k } ^ { H } \boldsymbol { h } _ { r , j } \vert } { \vert \vert \boldsymbol { h } _ { c , k } ^ { H } \vert \vert \vert \vert \boldsymbol { h } _ { r , j } \vert \vert } , \lambda _ { 1 } \ = \ \frac { \Upsilon \vert \vert \boldsymbol { h } _ { c , k } ^ { H } \vert \vert ^ { 2 } \sin \varphi _ { k , j } } { \sqrt { P _ { \operatorname* { m a x } } \vert \vert \boldsymbol { h } _ { r , j } \vert \vert ^ { 2 } - \Gamma ^ { t h } } } , } \end{array}$ $\begin{array} { r } { \lambda _ { 2 } = \frac { \Upsilon \| h _ { c , k } ^ { H } \| ^ { 2 } \sqrt { \Gamma ^ { t h } } - \Upsilon ^ { 2 } \| h _ { c , k } ^ { H } \| \| h _ { r , j } \| \cos \varphi _ { k , j } } { \| h _ { r , j } \| ^ { 2 } \sqrt { P _ { \operatorname* { m a x } } \| h _ { r , j } \| ^ { 2 } } \Upsilon ^ { t h } - ( \Gamma ^ { t h } ) ^ { 2 } } , \beta _ { c , k } = \frac { \| h _ { c , k } ^ { H } \| ^ { 2 } } { \| h _ { r , j } \| ^ { 2 } } \Upsilon ^ { 2 } } \end{array}$ $\Upsilon = \sqrt { \Gamma ^ { t h } } \cos \varphi _ { k , j } + \sqrt { P _ { \operatorname* { m a x } } \| h _ { r , j } \| ^ { 2 } - \Gamma ^ { t h } }$ sin $\varphi _ { k , j }$ , and $\tilde { \Gamma } =$ $\textstyle \frac { M P _ { \operatorname* { m a x } } \cos ^ { 2 } \varphi _ { k , j } } { d ( \pmb { q } [ n ] , \pmb { v } _ { j } ) ^ { 2 } }$

Proof: Please refer to Appendix A.

In Proposition 1, the optimal beamforming vector could be intuitively viewed as two linearly superimposed beams towards user and target, respectively, which directly shows the influencing factors of the associated user’s achievable rate. Also, the closed-form beamforming in (14) can also hold for arbitrary user channels $h _ { c , k } ^ { H }$ . For $\begin{array} { r } { \frac { \overline { { M } } P _ { \operatorname* { m a x } } \cos ^ { 2 } \varphi _ { k , j } } { d ( \pmb { q } [ n ] , \pmb { v } _ { j } ) ^ { 2 } } < \Gamma ^ { t h } } \end{array}$ , the optimal SNR at user <sup>k</sup> can be obtained by plugging $h _ { c , k }$ and $\boldsymbol { h } _ { r , j }$ into $\beta _ { c , k }$ , yielding

$$
\begin{array} { l } { { \gamma _ { k , j } ^ { * } = \gamma _ { 0 } \frac { d ( \boldsymbol { q } [ n ] , \boldsymbol { v } _ { j } ) ^ { 2 } } { d ( \boldsymbol { q } [ n ] , \boldsymbol { u } _ { k } ) ^ { 2 } } } } \\ { { \times \left( \sqrt { \Gamma _ { j } ^ { t h } } \cos \varphi _ { k , j } \boldsymbol { 1 } + \sqrt { \frac { M P _ { \mathrm { m a x } } } { d ( \boldsymbol { q } [ n ] , \boldsymbol { v } _ { j } ) ^ { 2 } } - \Gamma ^ { t h } } \sin \varphi _ { k , j } \right) ^ { 2 } } , } \end{array}\tag{15}
$$

where $\begin{array} { r } { \gamma _ { 0 } = \frac { \beta _ { 0 } } { \sigma ^ { 2 } } } \end{array}$

<sup>=</sup>Remark 1: In (15), the optimal user SNR is mainly determined by two parts: $\sqrt { \Gamma _ { j } ^ { t h } }$ and $\begin{array} { r } { \sqrt { \frac { M P _ { \mathrm { m a x } } } { d ( \pmb q [ n ] , \pmb v _ { j } ) ^ { 2 } } - \Gamma ^ { t h } } } \end{array}$ , together with the channel correlation coefficient, i.e., $\varphi _ { k , j }$ . When COS $\varphi _ { k , j } = 1$ <sup>cos</sup>, the communication channel and target channel are linearly related. In this case, the channel power gain at user <sup>k</sup> is $\displaystyle \dot { \frac { P _ { \mathrm { m a x } } M \beta _ { 0 } } { d ( q [ n ] , u _ { k } ) ^ { 2 } } }$ , which holds if and only if the locations of user and target coincide. Whereas when $\varphi _ { k , j } = 0$ , the communication channel and target channel are orthogonal to each other. In this case, the channel power gain at user <sup>k</sup> is reduced to $\begin{array} { r } { \beta _ { 0 } \frac { M P _ { \mathrm { m a x } } - \Gamma ^ { t h } d ( \pmb { q } [ n ] , \pmb { v } _ { j } ) ^ { 2 } } { d ( \pmb { q } [ n ] , \pmb { u } _ { k } ) ^ { 2 } } } \end{array}$

Lemma 1: If $M _ { x }  \infty$ and $M _ { y }  \infty$ , for any given UAV location q <sup>n</sup> , the optimal user <sup>k</sup>’s SNR during sensing target <sup>j</sup> is denoted by

$$
\gamma _ { k , j } ^ { * } = \left\{ \begin{array} { l l } { \gamma _ { 0 } \displaystyle \frac { M P _ { \operatorname* { m a x } } - \Gamma ^ { t h } d ( \pmb q [ n ] , \pmb v _ { j } ) ^ { 2 } } { d ( \pmb q [ n ] , \pmb u _ { k } ) ^ { 2 } } , ~ \pmb u _ { k } \neq \pmb v _ { j } } \\ { \gamma _ { 0 } \displaystyle \frac { M P _ { \operatorname* { m a x } } } { d ( \pmb q [ n ] , \pmb u _ { k } ) ^ { 2 } } , ~ \mathrm { O t h e r w i s e } , } \end{array} \right.\tag{16}
$$

where $\begin{array} { r } { \gamma _ { 0 } = \frac { \beta _ { 0 } } { \sigma ^ { 2 } } } \end{array}$ . And, the corresponding optimal UAV location <sup>=</sup>with the maximum achievable rate at user <sup>k</sup> during sensing target <sup>j</sup> is given by

$$
\pmb { q } _ { k , j } ^ { * } = \pmb { u } _ { k } + \frac { \sqrt { Z ^ { 2 } + 4 H ^ { 2 } } - Z } { 2 D _ { k , j } } ( \pmb { v } _ { j } - \pmb { u } _ { k } ) ,\tag{17}
$$

where $\begin{array} { r } { Z = \frac { M P _ { \operatorname* { m a x } } } { \Gamma ^ { t h } D _ { k , i } } - D _ { k , j } } \end{array}$ and $D _ { k , j } = \| \pmb { v } _ { j } - \pmb { u } _ { k } \|$ denotes the horizontal distance between user <sup>k</sup> and target <sup>j</sup>.

Proof: Please refer to Appendix B.

According to Lemma 1, the user <sup>k</sup>’s SNR can be simplified as (16) when the number of antennas is large, since the channel $h _ { c , k } ^ { H }$ and $h _ { r , j } ^ { H }$ can be completely irrelevant. However, solving (P1) is still very challenging due to the closely coupled integer variables and highly non-convex constraints. In the next subsection, we derive a tight lower bound of the achievable rate according to the optimal beamforming vector in Proposition 1 to facilitate solving the problem (P1).

## B. Lower Bound of Achievable Rate

For any given user association A, sensing time selection C, and UAV trajectory Q, the optimal beamforming vector ${ \pmb w } _ { c }$ can be obtained based on Proposition 1. Then, its corresponding achievable rate of user <sup>k</sup> at the <sup>n</sup>th time slot is given by

$$
\begin{array} { r } { { \cal R } _ { k } [ n ] = \underbrace { \alpha _ { k } [ n ] \left( 1 - \sum _ { j = 1 } ^ { J } c _ { j } [ n ] \right) { \cal R } _ { k } ^ { C } [ n ] } _ { \mathrm { O n l y ~ c o m m u n i c a t i o n } } } \\ { + \underbrace { \alpha _ { k } [ n ] \sum _ { j = 1 } ^ { J } c _ { j } [ n ] { \cal R } _ { k , j } ^ { I S A C } [ n ] } _ { \mathrm { D u r i n g ~ s e n s i n g } } , } \end{array}\tag{18}
$$

where the user $k ' s$ optimal achievable rate during communication-only time is given by

$$
R _ { k } ^ { C } [ n ] = \log _ { 2 } { \left( 1 + \gamma _ { 0 } \frac { M P _ { \operatorname* { m a x } } } { d ( \pmb q [ n ] , \pmb u _ { k } ) ^ { 2 } } \right) } ,\tag{19}
$$

and the user <sup>k</sup>’s optimal achievable rate during sensing time is given by

$$
\begin{array} { r } { R _ { k , j } ^ { I S A C } [ n ] = \left\{ \begin{array} { l l } { \log _ { 2 } \left( 1 + \gamma _ { 0 } \frac { M P _ { \operatorname* { m a x } } } { d ( q [ n ] , u _ { k } ) ^ { 2 } } \right) , } & { \Gamma _ { k , j } [ n ] \geq \Gamma ^ { t h } } \\ { \log _ { 2 } \left( 1 + \gamma _ { k , j } ^ { \ast } \right) , } & { \mathrm { O t h e r w i s e } , } \end{array} \right. } \end{array}\tag{20}
$$

where $\begin{array} { r } { \Gamma _ { k , j } [ n ] = \frac { M P _ { \operatorname* { m a x } } \cos ^ { 2 } \varphi _ { k , j } } { d ( q [ n ] , \pmb { v } _ { j } ) ^ { 2 } } } \end{array}$ and $\gamma _ { k , j } ^ { * }$ is defined in (15). Hence, the sum achievable rate can be maximized by only jointly optimizing the user association A, sensing time selection $^ { C , }$ and UAV trajectory Q. Nonetheless, the considered problem is still challenging due to the piece-wise non-concave function in (20). To handle this problem, a tight lower bound of $R _ { k , j } ^ { I S A C } [ n ]$ is derived as below.

Lemma 2: The optimal achievable rate of user <sup>k</sup> during sensing target <sup>j</sup> satisfies the following condition

$$
\begin{array} { r l } & { R _ { k } ^ { I S A C } [ n ] \geq \log _ { 2 } \left( 1 + \gamma _ { 0 } \frac { M P _ { \operatorname* { m a x } } - d ( \boldsymbol { q } [ n ] , \boldsymbol { v } _ { j } ) ^ { 2 } \Gamma ^ { t h } } { d ( \boldsymbol { q } [ n ] , \boldsymbol { u } _ { k } ) ^ { 2 } } \right) } \\ & { \quad \quad \quad \quad = \underline { { R } } _ { k , j } ^ { I S A C } [ n ] . } \end{array}\tag{21}
$$

Proof: To prove (21), we only need to ensure that $\begin{array} { r l r } { \gamma _ { k , j } ^ { \ast } } & { { } \ge } & { \gamma _ { 0 } \frac { M P _ { \operatorname* { m a x } } - d ( \pmb q [ n ] , \pmb v _ { j } ) ^ { 2 } \Gamma ^ { t h } } { d ( \pmb q [ n ] , \pmb u _ { k } ) ^ { 2 } } } \end{array}$ holds since the log function is a monotonically increasing function. If $\alpha _ { k } [ n ] \ =$ and $\begin{array} { r l r } { \sum _ { j = 1 } ^ { J } c _ { j } [ n ] } & { = } & { 0 , \mathrm { o r } \frac { M P _ { \mathrm { m a x } } ^ { - } \cos ^ { 2 } \varphi _ { k , j } } { d ( q [ n ] , v _ { j } ) ^ { 2 } } \ge \Gamma ^ { \hat { t } h } } \end{array}$ , the maximum ratio transmission (MRT) is the optimal beamforming vector to problem (P1), and thus, the inequality in (21) obviously holds. In the following, we prove that if $\begin{array} { r } { \frac { M P _ { \operatorname* { m a x } } \rho ^ { 2 } } { d ( q [ n ] , v _ { j } ) ^ { 2 } } < \Gamma ^ { t h } , \rho \sqrt { \Gamma ^ { t h } } + \sqrt { ( 1 - \rho ^ { 2 } ) } \sqrt { \frac { M P _ { \operatorname* { m a x } } } { d ( q [ n ] , v _ { j } ) ^ { 2 } } - \Gamma ^ { t h } } \geq } \end{array}$ $\begin{array} { r } { \sqrt { \frac { M P _ { \mathrm { m a x } } } { d ( \pmb q [ n ] , \pmb v _ { j } ) ^ { 2 } } - \Gamma ^ { t h } } } \end{array}$ . Let $\rho ~ = ~ \cos { \varphi _ { k , j } }$ and $\begin{array} { r } { G = \frac { M P _ { \mathrm { m a x } } } { d ( \pmb { q } [ n ] , \pmb { v } _ { j } ) ^ { 2 } } } \end{array}$ for notation simplicity. Then, for $\mathcal { F } ( \Gamma ^ { t h } , \rho ) \triangleq \rho \sqrt { \Gamma ^ { t h } } +$ $\sqrt { ( 1 - \rho ^ { 2 } ) } \sqrt { G - \Gamma ^ { t h } } ~ - ~ \sqrt { G - \Gamma ^ { t h } }$ , we need to prove $\begin{array} { r l r } { \mathcal { F } ( \Gamma ^ { t h } , \rho ) } & { { } \ge } & { 0 } \end{array}$ for $\begin{array} { r l r } { \Gamma ^ { t h } } & { { } \in } & { ( G \rho , G ] } \end{array}$ . As $\mathcal { F } ( \Gamma ^ { t h } , \rho )$ <sup>(Γ ) 0 Γ ( ]</sup>is an increasing function with respect to $\mathrm { ( w . r . t ) } \ \Gamma ^ { t h }$ $\mathcal { F } ( \Gamma ^ { t h } , \rho ) \geq 0$ if $\begin{array} { r l r } { { \mathcal F } ( G \rho , \rho ) } & { { } \ge } & { 0 , } \end{array}$ where $\begin{array} { r l } { \mathcal { F } ( G \rho , \rho ) } & { { } = } \end{array}$ ${ \sqrt { G } } \left( \rho { + } { \sqrt { ( 1 - \rho ^ { 2 } ) } } { \sqrt { 1 - \rho } } - { \sqrt { 1 - \rho } } \right)$ . For $\rho \in [ 0 , 1 ]$ $\mathcal { F } ( G \rho , \rho )$ is an increasing function w.r.t $\rho ,$ as $\begin{array} { r } { \frac { \partial \mathcal { F } ( G \rho , \rho ) } { \partial \rho } > 0 } \end{array}$ Hence, $\mathcal { F } ( G \rho , \rho ) \geq \mathcal { F } ( 0 , 0 ) = 0$ . Then, plugging ${ \mathcal { F } } ( G \rho , \rho ) \geq$ into (15), we obtain $\begin{array} { r } { \gamma ^ { * } \geq \gamma _ { 0 } \frac { M P _ { \operatorname* { m a x } } - d ( \pmb { q } [ n ] , \pmb { v } _ { j } ) ^ { 2 } \Gamma ^ { t h } } { d ( \pmb { q } [ n ] , \pmb { u } _ { k } ) ^ { 2 } } } \end{array}$ , which thus completes the proof. ■

The lower bound of user <sup>k</sup>’s SNR in (21) is tight if <sup>M</sup> goes to infinity according to Lemma 1. A closer look at this lower bound in (21) reveals that the value of $\varphi _ { k , j }$ is small since $\frac { \sin M \Delta \pi / 2 } { \sin \Delta \pi / 2 }$ is relatively small for $\Delta \geq { \frac { 1 } { M } }$ , and $R _ { k } ^ { I S A C } [ n ] =$ $\underline { { R } } _ { k , j } ^ { I S A C } [ n ]$ when $\begin{array} { r } { \Delta = \frac { 2 i } { M } , i \in \mathbb { Z } , i \neq 0 } \end{array}$ . Based on Lemma 2, the lower bound of the user <sup>k</sup>’s achievable rate can be recast as

$$
\begin{array} { l } { { \underline { { { R } } } _ { k } [ n ] = \alpha _ { k } [ n ] R _ { k } ^ { C } [ n ] } } \\ { { \qquad + \sum _ { j = 1 } ^ { J } \alpha _ { k } [ n ] c _ { j } [ n ] \left( \underline { { { R } } } _ { k , j } ^ { I S A C } [ n ] - R _ { k } ^ { C } [ n ] \right) . } } \end{array}\tag{22}
$$

Then, we introduce problem (P1.1) as the lower bound of the achievable rate maximization problem in the case by setting $R _ { k } [ n ]$ as $\underline { { R } } _ { k } [ n ]$ in (P1). Then, a high-quality solution of problem (P1) can be obtained by solving problem (P1.1), elaborated as follows.

## C. Penalty-Based Problem Transformation

Although the complicated expression of the optimal achievable rate of user <sup>k</sup> is simplified as its tight lower bound, the integer variables $\{ \alpha _ { k } [ n ] \}$ and $\{ c _ { j } [ n ] \}$ are coupled with each <sup>[ ] [ ]</sup>other in the objective function and constraints. To tackle this issue, another variable $e _ { k , j } [ n ] = \alpha _ { k } [ n ] c _ { j } [ n ]$ is introduced to decouple the integer variables. Then, $\underline { { R } } _ { k } [ n ]$ can be rewritten as

$$
\underline { { { R } } } _ { k } [ n ] = \alpha _ { k } [ n ] R _ { k } ^ { C } [ n ] + \sum _ { j = 1 } ^ { J } e _ { k , j } [ n ] \left( \underline { { { R } } } _ { k , j } ^ { I S A C } [ n ] - R _ { k } ^ { C } [ n ] \right) ,\tag{23}
$$

where $e _ { k , j } [ n ] ~ \in ~ \{ 0 , 1 \}$ . To ensure the consistency of the problem (P1.1), some other constraints are introduced to replace that in (1) and (2) as follows

$$
\alpha _ { k } [ n ] \geq e _ { k , j } [ n ] , \forall k , j , n ,\tag{24}
$$

$$
{ \sum } _ { n = ( l - 1 ) N _ { L } + 1 } ^ { l N _ { L } } { \sum } _ { k = 1 } ^ { K } e _ { k , j } [ n ] = 1 , \forall l , j ,\tag{25}
$$

$$
\sum _ { k = 1 } ^ { K } \sum _ { j = 1 } ^ { J } e _ { k , j } [ n ] \leq 1 , \forall n .\tag{26}
$$

(24) ensures that $e _ { k , j } [ n ] ~ = ~ 1$ if and only if $\alpha _ { k } [ n ] \ = \ 1$ Accordingly, we can readily prove that the new introduced problem with the replaced constraints (24)-(26), denoted by (P1.2), is equivalent to (P1.1). Furthermore, the bream pattern gain constraints in (12a) can be transformed into

$$
\sum _ { k = 1 } ^ { K } e _ { k , j } [ n ] ( M P _ { \operatorname* { m a x } } - d ( \pmb { q } [ n ] , \pmb { v } _ { j } ) ^ { 2 } \Gamma _ { j } ^ { t h } ) \ge 0 .\tag{27}
$$

However, converting $\alpha _ { k } [ n ]$ and $e _ { k , j } [ n ]$ to continuous-valued variables and then utilizing rounding function to obtain the binary solution, generally may not satisfy the QoS constraints in (12c) and the beam pattern gain constraints in (12a). Several slack matrices $\bar { \cal A } ~ = ~ \{ \{ \bar { \alpha } _ { k } [ n ] \} _ { n = 1 } ^ { N } \} _ { k = 1 } ^ { K }$ and $\bar { \cal E } ~ = ~ \{ \{ \{ \bar { e } _ { k , j } [ n ] \} _ { n = 1 } ^ { N } \} _ { k = 1 } ^ { K } \} _ { j = 1 } ^ { J }$ are presented to transform the binary constraints into a series of equivalent equality constraints. Specifically, (12b) can be rewritten as

$$
\begin{array} { r } { \alpha _ { k } [ n ] ( 1 - \bar { \alpha } _ { k } [ n ] ) = 0 , \alpha _ { k } [ n ] = \bar { \alpha } _ { k } [ n ] , \forall k , n , ( 2 8 ) } \\ { e _ { k , j } [ n ] ( 1 - \bar { e } _ { k , j } [ n ] ) = 0 , e _ { k , j } [ n ] = \bar { e } _ { k , j } [ n ] , \forall k , j , n . \qquad } \end{array}\tag{29}
$$

We can readily derive that $\alpha _ { k } [ n ]$ and $e _ { k , j } [ n ]$ satisfying the above two constraints must be either 1 or 0, which confirms the equivalence of the transformation of (12b) into these two constraints. Then, (28) and (29) are added to the objective function in (P1.2) as the penalty terms [44], yielding the following optimization problem

$$
\begin{array} { r l r } { { \mathrm { ( P 2 ) } \colon } } & { { \underset { \bar { A } , \bar { E } , A , E , Q } { \operatorname* { m i n } } } } & { { - \underline { { R } } } } \\ { { } } & { { \mathrm { s . t . } \ \mathrm { ( 7 ) } , ( 2 4 ) - ( 2 7 ) , ( 1 2 c ) - ( 1 2 d ) , } } \\ { { } } & { { \mathrm { 1 } \underset { { N _ { L } } } { \operatorname* { m i n } } \sum _ { n = ( l - 1 ) N _ { L } + 1 } ^ { l N _ { L } } \alpha _ { k } [ n ] \underline { { R } } _ { k } [ n ] \geq R _ { k } ^ { t h } , } } & { { } } \\ { { } } & { { \forall k , l , } } & { { ( 3 0 ) } } \end{array}\tag{0}
$$

a)

where <sup>R</sup> is defined in (31), shown at the bottom of the next page, and $\eta ~ > ~ 0$ is the penalty coefficient used to penalize the violation of the equality constraints (28) and (29). Despite relaxing the equality constraints in (28) and (29), it can be readily verified that the solutions obtained will always satisfy the equality constraints (i.e., binary value constraints of $\{ \alpha _ { k } [ n ] \}$ and $\{ e _ { k , j } [ n ] \} )$ , when $\textstyle { \frac { 1 } { \eta } } \to \infty$ . To facilitate efficient optimization, <sup>η</sup> is initialized with a sufficiently large value and then we gradually reduce <sup>η</sup> to a sufficiently small value. As a result, a feasible binary solution can be eventually obtained. In particular, the alternating optimization (AO) method is applied to iteratively optimize the primary variables in different blocks, as shown in Section III-D.

## D. Inner and Outer Layer Iteration

In this subsection, we propose a two-layer penalty-based algorithm. Specifically, in the inner layer, (P2) is divided into three sub-problems in which $\{ \bar { A } , \bar { E } \} , \{ A , E \}$ , and Q are optimized iteratively. In the outer layer, the penalty coefficient is updated to ensure that the constraints (28) and (29) are met eventually.

1) Slack Variables Optimization: For any given $\{ A , E \}$ and Q, (P2) can be expressed as

$$
( \mathrm { P 2 . 1 } ) : \quad \operatorname* { m i n } _ { \bar { A } , \bar { E } } \mathrm { ~ \Omega ~ ^ { - } ~ \underline { { { R } } } ~ }\tag{32}
$$

It is not difficult to find that the slack variables $\bar { \alpha } _ { k } [ n ]$ and $\bar { e } _ { k , j } [ n ]$ are only involved in the objective function. Thus, the optimal slack variables $\bar { \alpha } _ { k } [ n ]$ and $\bar { e } _ { k , j } [ n ]$ can be obtained by <sup>¯ [ ]</sup>setting the derivative of (32) w.r.t. $\bar { \alpha } _ { k } [ n ]$ and $\bar { e } _ { k , j } [ n ]$ to zero, respectively, i.e.,

$$
\bar { \alpha } _ { k } ^ { \mathrm { o p t } } [ n ] = \frac { \alpha _ { k } [ n ] + \alpha _ { k } ^ { 2 } [ n ] } { 1 + \alpha _ { k } ^ { 2 } [ n ] } , ~ \forall k , n ,\tag{33}
$$

$$
\bar { e } _ { j } ^ { \mathrm { o p t } } [ n ] = \frac { e _ { k , j } [ n ] + e _ { k , j } ^ { 2 } [ n ] } { 1 + e _ { k , j } ^ { 2 } [ n ] } , ~ \forall j , k , n .\tag{34}
$$

2) User Association and Sensing Time Selection: For any given $\{ \bar { A } , \bar { E } \}$ and Q, (P2) can be expressed as

$$
\begin{array} { r l } { ( \mathrm { P 2 . 2 } ) \colon } & { \underset { A , E } { \operatorname* { m i n } } - \underline { { R } } } \\ & { \mathrm { s . t . ~ } ( 7 ) , ( 2 4 ) - ( 2 7 ) , ( 3 0 a ) . } \end{array}\tag{35}
$$

It can be seen that problem (35) is convex with a quadratic objective function and linear inequality constraints, which can be solved by standard convex optimization solvers, such as CVX.

3) Trajectory Optimization: For given $\{ \bar { A } , \bar { E } \}$ and $\{ A , E \}$ the UAV trajectory optimization sub-problem is given as follows

$$
\begin{array} { r l } { \mathrm { ( P 2 . 3 ) } \colon } & { \underset { Q } { \operatorname* { m a x } } ~ \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } \underline { { R } } _ { k } [ n ] } \\ & { \mathrm { s . t . } ~ ( 1 2 e ) , ( 1 2 f ) , ( 2 7 ) , ( 3 0 } \end{array}\tag{36}
$$

However, note that (P2.3) is neither concave or quasi-concave due to the non-convex constraints (30a), (12a) and the non-convex objective function (36). In general, there is no efficient method to obtain the optimal solution. In the following, we adopt the successive convex optimization technique to solve (P2.3). To this end, additional slack variables $\{ z _ { c , k } [ n ] \}$ and $\{ z _ { r , j } [ n ] \}$ are introduced, and $R _ { k } ^ { C } [ n ]$ and $\underline { { R } } _ { k , j } ^ { I S A C } [ n ]$ are recast as

$$
\tilde { R } _ { k } ^ { C } [ n ] = B \log _ { 2 } \bigg ( 1 + \beta _ { 0 } \frac { P _ { \operatorname* { m a x } } M } { z _ { c , k } [ n ] } \bigg ) ,\tag{37}
$$

$$
\tilde { R } _ { k , j } ^ { I S A C } [ n ] = \log _ { 2 } \bigg ( 1 + \gamma _ { 0 } \frac { M P _ { \operatorname* { m a x } } - z _ { r , j } [ n ] \Gamma ^ { t h } } { z _ { c , k } [ n ] } \bigg ) ,\tag{38}
$$

together with

$$
z _ { c , k } [ n ] \geq \| \pmb { q } [ n ] - \pmb { u } _ { k } \| ^ { 2 } + H ^ { 2 } , \quad \forall k , n ,\tag{39}
$$

$$
z _ { r , j } [ n ] \geq \| \pmb { q } [ n ] - \pmb { v } _ { j } \| ^ { 2 } + H ^ { 2 } , \forall k , j , n .\tag{40}
$$

For ease of analysis, this new constructed problem is denoted by (P2.4). It can be shown that at the optimal solution of variable $\tilde { R } _ { k } ^ { C } [ n ]$ and $\tilde { R } _ { k , j } ^ { I S A C } [ n ]$ in (P2.4), all the constraints in (39) and (40) are active, since otherwise we can always increase $z _ { c , k } [ n ]$ or $z _ { c , k } [ n ]$ without decreasing the value of the objective function. Hence, (P2.4) is equivalent to (P2.3). Since $\tilde { R } _ { k } ^ { C } [ n ]$ is convex w.r.t. $z _ { c , k } [ n ]$ , for any local point $z _ { c , k } ^ { ( r ) } [ n ]$ <sup>[ ] [ ]</sup>obtained at the <sup>r</sup>th iteration, we have

$$
\begin{array} { l } { { \displaystyle \tilde { R } _ { k } ^ { C } [ n ] = \log _ { 2 } \left( 1 + \frac { A _ { k } } { z _ { c , k } [ n ] } \right) \geq \log _ { 2 } \left( 1 + \frac { A _ { k } } { z _ { c , k } ^ { ( r ) } [ n ] } \right) } } \\ { { \displaystyle ~ - \frac { A _ { k } \left( z _ { c , k } [ n ] - z _ { c , k } ^ { ( r ) } [ n ] \right) } { ( z _ { c , k } ^ { ( r ) } [ n ] ^ { 2 } + A _ { k } z _ { c , k } ^ { ( r ) } [ n ] ) \ln 2 } = \hat { R } _ { k } ^ { C } [ n ] } , } \end{array}\tag{41}
$$

where $\begin{array} { r } { A _ { k } \ = \ \frac { P _ { \mathrm { m a x } } M \beta _ { 0 } } { \sigma _ { k } ^ { 2 } } } \end{array}$ . Furthermore, the Hessian matrix of $\tilde { R } _ { k , j } ^ { I S A C } [ n ]$ regarding variables $z _ { c , k }$ and $z _ { r , j }$ is given by

$$
H _ { k , j } = \frac { 1 } { \ln 2 } \left[ \begin{array} { c c } { \displaystyle \frac { 1 } { z _ { c , k } ^ { 2 } \left[ n \right] } - \frac { 1 } { \left( Z \right) ^ { 2 } } } & { \displaystyle \frac { k _ { 1 } } { \left( Z \right) ^ { 2 } } } \\ { \displaystyle \frac { k _ { 1 } } { \left( Z \right) ^ { 2 } } } & { \displaystyle \frac { - k _ { 1 } ^ { 2 } } { \left( Z \right) ^ { 2 } } } \end{array} \right] ,\tag{42}
$$

where $Z ~ = ~ z _ { c , k } [ n ] + k _ { 1 } z _ { r , j } [ n ] + k _ { 2 } , ~ k _ { 1 } ~ = ~ - \gamma _ { 0 } \Gamma ^ { t h }$ , and $k _ { 2 } = \gamma _ { 0 } M P _ { \mathrm { m a x } } . \ H _ { k , j }$ is a negative definite matrix in the feasible region, as $\begin{array} { r } { | H _ { k , j } | = \frac { - k _ { 1 } ^ { 2 } } { \ln 2 ( z _ { c , k } [ n ] + k _ { 1 } z _ { r , j } [ n ] + k _ { 2 } ) ^ { 2 } z _ { c , k } ^ { 2 } [ n ] } \leq } \end{array}$ , $H _ { k , j } ( 1 , 1 ) \leq 0$ , and $H _ { k , j } ( 2 , 2 ) \ \leq \ 0$ . Hence, $\tilde { R } _ { k , j } ^ { I S A C } [ n ]$ is jointly concave w.r.t. $z _ { c , k }$ and $z _ { r , j }$ . Then, (P2.4) can be converted into

$$
\begin{array} { r l } { { \mathrm { ( P 2 . 5 ) } \colon } } & { { \underset { Q , \{ z _ { c , k } \} , \{ z _ { r , j } \} } { \operatorname* { m a x } } } ~ \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } \hat { R } _ { k } [ n ] } \\ & { \quad \quad \mathrm { s . t . } ~ ( 1 2 e ) , ( 1 2 f ) , ( 2 7 ) , ( 3 9 ) , ( 4 0 ) , } \\ & { \quad \quad \quad \frac { 1 } { N _ { L } } \sum _ { n = ( l - 1 ) N _ { L } + 1 } ^ { l N _ { L } } \hat { R } _ { k } [ n ] \geq R _ { k } ^ { t h } , } \\ & { \quad \quad \quad \forall k , l , } \end{array}\tag{43}
$$

(43a)

where $\begin{array} { r c l } { { \hat { R } _ { k } [ n ] } } & { { = } } & { { \alpha _ { k } [ n ] \hat { R } _ { k } ^ { C } [ n ] + \sum _ { j = 1 } ^ { J } e _ { k , j } [ n ] ( \tilde { R } _ { k , j } ^ { I S A C } [ n ] - } } \end{array}$ $\tilde { R } _ { k } ^ { C } [ n ] )$ . Based on the previous discussions, the objective function and all of the constraints of (P2.5) are concave. Thus, (P2.5) is a convex optimization problem that can be efficiently solved by convex optimization solvers such as CVX.

4) Outer Layer Iteration: In the outer layer, the value of the penalty coefficient <sup>η</sup> is gradually decreased by updating $\eta = z \eta ,$ , where $z \ ( 0 < z < 1 )$ is a scaling factor. A larger value of <sup>z</sup> can achieve better performance but at the cost of more iterations in the outer layer.

## E. Convergence Analysis and Computational Complexity

To show the converged solutions of the proposed penaltybased algorithm, the terminal criteria for the outer layer is given as $( | \alpha _ { k } [ n ] ( 1 - \bar { \alpha } _ { k } [ n ] ) | , | \alpha _ { k } [ n ] - \bar { \alpha } _ { k } [ n ] | , | e _ { k , j } [ n ] ( 1 -$ $\bar { e } _ { k , j } [ n ] ) | , | e _ { k , j } [ n ] - \bar { e } _ { k , j } [ n ] | , \forall k , j , n ) \leq \xi ,$ , where <sup>ξ</sup> is a predefined accuracy. The details of the proposed penalty-based algorithm are shown in Algorithm 1. In the inner layer, with the given penalty coefficient, the objective function of (P2) is non-increasing over each iteration during applying the AO method and the objective of (P2) is upper bounded due to the limited flying time <sup>T</sup> and transmit power $P _ { \mathrm { m a x } }$ As such, a stationary point can be achieved in the inner layer. In the outer layer, the penalty coefficient is gradually decreased so that the equality constraints (28) and (29) are ultimately satisfied. Based on Appendix B in [45], this penalty-based framework is guaranteed to converge.

The complexity of Algorithm 1 can be analyzed as follows. In the inner layer, the main complexity of Algorithm 1

$$
\begin{array} { l } { { \displaystyle { \cal R } = \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } \alpha _ { k } [ n ] { \cal R } _ { k } [ n ] - \frac { 1 } { 2 \eta } \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } ( \vert \alpha _ { k } [ n ] ( 1 - \bar { \alpha } _ { k } [ n ] ) \vert ^ { 2 } + \vert \alpha _ { k } [ n ] - \bar { \alpha } _ { k } [ n ] \vert ^ { 2 } ) } } \\ { { \displaystyle ~ - \frac { 1 } { 2 \eta } \sum _ { n = 1 } ^ { N } \sum _ { j = 1 } ^ { J } \sum _ { k = 1 } ^ { K } ( \vert e _ { k , j } [ n ] ( 1 - \bar { e } _ { k , j } [ n ] ) \vert ^ { 2 } + \vert e _ { k , j } [ n ] - \bar { e } _ { k , j } [ n ] \vert ^ { 2 } ) , } } \end{array}\tag{31}
$$

Algorithm 1 Penalty-Based Algorithm   
1: Initialize $\{ \bar { \pmb { A } } ^ { ( 0 ) } , \bar { \pmb { E } } ^ { ( 0 ) } \} , \{ \pmb { A } ^ { ( 0 ) } , \pmb { E } ^ { ( 0 ) } \}$ , and ${ \cal Q } ^ { ( 0 ) }$ , the itera  
tion number $r = 1$ , the convergence accuracy $\epsilon _ { 1 }$ and $\epsilon _ { 2 }$   
2: repeat   
3: repeat   
4: With given $\{ \{ A ^ { ( r ) } , E ^ { ( r ) } \} , Q ^ { ( r ) } \}$ , obtain $\{ \bar { \boldsymbol { A } } ^ { ( r + 1 ) }$   
$\bar { \pmb { E } } ^ { ( r + 1 ) } \}$ based on (33) and (34).   
5: With given $\{ \{ \bar { \pmb { A } } ^ { ( r ) } , \bar { \pmb { E } } ^ { ( r ) } \} , \pmb { Q } ^ { ( r ) } \}$ , obtain $\{ A ^ { ( r + 1 ) }$   
$\pmb { { \cal E } } ^ { ( r + 1 ) } \}$ by solving the problem in (35).   
6: With given $\{ \{ \bar { A } ^ { ( r ) } , \bar { E } ^ { ( r ) } \} , \{ A ^ { ( r ) } , E ^ { ( r ) } \} \}$ , and obtain   
$\boldsymbol { Q } ^ { ( r + 1 ) }$ by solving the problem in (43).   
7: Calculate $C ^ { ( r + 1 ) * }$ according to the objective function   
of (P2).   
8: $r = r + 1 .$   
9: <sup>=</sup>until $\left| C ^ { ( r + 1 ) * } - C ^ { ( r ) * } \right| \le \epsilon _ { 1 }$   
10: $\eta = z \eta .$   
11: until the constraint violation in (28) and (29) is below a   
threshold $\epsilon _ { 2 } .$   
12: Obtain $\pmb { w } _ { c } ^ { * }$ based on proposition 1.   
13: Recover optimal sensing time selection $C ^ { * }$ based on $A ^ { * }$   
and $E ^ { * }$

comes from steps 5 and 6. In step 5, the complexity of computing $\{ \alpha _ { k } [ n ] \}$ and $\{ e _ { k , j } [ n ] \}$ is $\bar { \mathcal { O } } ( K N + J K \bar { N } ) ^ { 3 . 5 }$ [46], where $K N { \bf \bar { \Psi } } + \bar { J } \bar { K N }$ <sup>[ ] ( + )</sup>stands for the number of variables [46]. <sup>+</sup>Similarly, in step $^ { 6 , }$ the complexity required to compute the UAV trajectory is $\mathcal { O } ( 2 N + \bar { K N } + \bar { J } N ) ^ { 3 . 5 }$ [46], where $2 N +$ $K N + J N$ <sup>(2 + + ) 2 +</sup>denotes the number of variables. Therefore, the total complexity of Algorithm 1 is $\mathcal { O } ( L _ { o u t e r } L _ { i n n e r } ( ( K N +$ $J K N ) ^ { 3 . 5 } + ( 2 N + \bar { K } N + J N ) ^ { 3 . 5 } ) )$ , where $L _ { i n n e r }$ <sup>+</sup>and $L _ { o u t e r }$ <sup>+ (2 + + ) ))</sup>denote the number of iterations required for reaching convergence in the inner and outer layers, respectively.

## IV. ANALYSIS WITHOUT LOCATION CONSTRAINTS AND LOW-COMPLEXITY ALGORITHM FOR SOLVING (P1)

To draw important insights into periodic sensing and communication design, we further study a special case of (P1) where the initial and final location constraints are ignored, denoted by (P3). Specifically, (P3) is given as

$$
\mathrm { ( P 3 ) } \colon \quad \operatorname* { m a x } _ { w _ { c } , A , Q , C } ~ \frac { 1 } { N } \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } \alpha _ { k } [ n ] R _ { k } [ n ]\tag{44}
$$

In the following, we first present the structural characteristics of the optimal solutions in different ISAC frames of (P3). Based on this, a low-complexity algorithm to problem (P1) is proposed to solve (P1).

## A. Analysis of Optimal Solution to (P3)

For ease of analysis, denote $\pmb { \mathcal { X } } _ { l } [ n ] ~ = ~ \{ \pmb { w } _ { c , l } ^ { * } [ n ] , \pmb { \alpha } _ { l } [ n ] ^ { * }$ ， ${ \pmb { c } } _ { l } [ n ] ^ { * } , { \pmb q } _ { l } ^ { * } [ n ] \}$ <sup>[ ] = [ ] [ ]</sup>as the optimal solution of the <sup>n</sup>th time slot of the <sup>l</sup>th ISAC frame, where ${ \pmb w } _ { c , l } ^ { * } [ n ] , { \pmb \alpha } _ { l } ^ { * } [ n ] , { \pmb c } _ { l } ^ { * } [ n ]$ , and ${ \pmb q } _ { l } ^ { * } [ n ]$ represent its corresponding optimal beamforming vector, user association, sensing time selection, and UAV trajectory at the <sup>n</sup>th time slot.

Lemma 3: There always exists an optimal solution to problem (P3) satisfying the following condition

$$
\pmb { \mathscr { X } } _ { l ^ { \prime } } [ n ] = \left\{ \begin{array} { l l } { \pmb { \mathscr { X } } _ { l } [ n ] , } & { | l - l ^ { \prime } | \ | \ 2 } \\ { \pmb { \mathscr { X } } _ { l } [ N _ { L } - n + 1 ] , } & { | l - l ^ { \prime } | \ \pmb { \mathscr { Y } } 2 , } \end{array} \right.\tag{45}
$$

where the symbols | and - represent that $\left| l - l ^ { \prime } \right|$ is divisible and not divisible by 2, respectively, $n \in \{ 1 , \cdots , N _ { L } \}$ , and $l ,$ $l ^ { \prime } \in \mathcal { L }$

Proof: Assume that at the optimal solution to problem (P3), the maximum sum achievable rate of the <sup>l</sup>th ISAC frame is denoted by $C _ { l } ^ { * }$ , its corresponding optimal beamforming vector, user association, sensing time selection, and UAV trajectory are denoted by $\{ x _ { l } [ n ] \} _ { n = l } ^ { N _ { L } }$ . Without loss of generality, we assume that the sum achievable rate $C _ { l } ^ { * }$ of the <sup>l</sup>th ISAC frame is the largest in the set $\{ C _ { 1 } ^ { * } , \cdots , C _ { L } ^ { * } \}$ We can always obtain a solution of the <sup>l</sup>th ISAC frame by reorganizing the elements in $\{ \pmb { x } _ { l } [ n ] \} _ { n = l } ^ { N _ { L } }$ while satisfying the <sup>[ ]</sup>constraints in (12a)-(12f), and its corresponding sum achievable rate $C _ { l } ^ { * } \geq C _ { l ^ { \prime } } ^ { * }$ . Specifically, considering the maximum speed constraint, when $l ^ { \prime } = l + 2 \ i + 1 , \ i \in \mathbb { Z } ,$ a solution <sup>= + 2</sup>whose achievable rate is no less than $C _ { l } ^ { * }$ <sup>1</sup>can be constructed by reversing the sequence of that within the <sup>l</sup>th ISAC frame, $\mathrm { i . e . , }$ $\pmb { \mathscr { X } } _ { l ^ { \prime } } [ n ] = \pmb { \mathscr { X } } _ { l } [ N _ { L } - n + 1 ] , n \in \{ 1 , \cdots , N _ { L } \}$ . Similarly, when $l ^ { \prime } = l + 2 i , i \in \mathbb { Z } .$ , we can readily prove that the solution of <sup>l</sup>th <sup>= +2</sup>is also feasible for the <sup>l</sup>th ISAC frame, i.e., $\pmb { \mathscr { X } } _ { l ^ { \prime } } [ n ] = \pmb { \mathscr { X } } _ { l } [ n ]$ By combing the above results, there always exists an optimal solution to problem (P3) satisfying the condition in (45). This thus completes the proof.

Remark 2: According to Lemma 3, there always exists an optimal solution to problem (P3) in the <sup>l</sup>th ISAC frame, which is exactly equal or opposite in sequence to that of the <sup>l</sup>th ISAC frame. Specifically, for any two time slot $n _ { 1 }$ and $n _ { 2 }$ belong to two adjacent ISAC frames, the optimal solution at time slot $n _ { 1 }$ and that at time slot $n _ { 2 }$ are equal when $n _ { 1 } + n _ { 2 } = l N _ { L } + 1$ i.e., $n _ { 1 }$ and $n _ { 2 }$ are symmetrical with respect to the time instant $l T _ { L } / 2$ , where $l$ is an even number. Hence, Lemma 4 implies that although the UAV trajectories within different ISAC frames are coupled with each other due to the maximum speed constraint, problem (P3) can be solved by only obtaining the solution in the first ISAC frame, while the solutions of other ISAC frames can be obtained based on (45). In particular, the solution of the first ISAC frame for problem (P3) can be efficiently solved by Algorithm 1 due to the similar constraints and objective function.

Proposition 2: The maximum achievable rate in (P3) increases monotonically as $T _ { L }$ increases.

Proof: Based on Lemma 3, there always exists an optimal solution, whose achievable rate in each ISAC frame is equal, denoted by $C _ { l } ^ { * }$ . For any given $T _ { L } ,$ , assume that at the optimal solution to problem (P3), the optimal beamforming, user association, sensing time slots, and UAV trajectory of the <sup>l</sup>th ISAC frame are denoted by $\boldsymbol { w } _ { c , l } ^ { * } , \ \boldsymbol { A } _ { l } ^ { * } , \ \boldsymbol { C } _ { l } ^ { * }$ , and $\boldsymbol { Q } _ { l } ^ { * }$ , respectively. Without loss of generality, the maximum achievable rate in the <sup>l</sup>th frame is denoted by $R ^ { \mathrm { m a x } }$ , its corresponding time slot and UAV location are denoted by $n ^ { \mathrm { m a x } }$ and $\mathbf { \Delta } q ^ { * } [ n ^ { \operatorname* { m a x } } ]$ . Based on the above discussion, for $N _ { L } ^ { \prime } > N _ { L }$ , there always exists a solution, in which the UAV trajectory in the <sup>l</sup>th ISAC frame

can be given by

$$
\begin{array} { r l r } & { } & { Q _ { l } ^ { \prime } = \{ q _ { l } ^ { * } [ 1 ] , \cdots , q _ { l } ^ { * } [ n ^ { \mathrm { m a x } } - 1 ] , \underbrace { q _ { l } ^ { * } [ n ^ { \mathrm { m a x } } ] , \cdots , \bullet _ { l } ^ { * } [ n ^ { \mathrm { m a x } } ] } _ { N _ { L } ^ { \prime } - N _ { L } + 1 } , } \\ & { } & { q _ { l } ^ { * } [ n ^ { \mathrm { m a x } } + 1 ] , \cdots , q _ { l } ^ { * } [ N _ { L } ] \} , \quad \quad \quad ( 4 \ell ^ { * } \mathrm { m a x } ) } \end{array}\tag{6}
$$

and its corresponding beamforming, user association, and sensing time selection is set as the same with that of solution $\{ \{ \pmb { w } _ { c , l } ^ { * } , \pmb { w } _ { r , l } ^ { * } \} , \pmb { A } _ { l } ^ { * } , \pmb { C } _ { l } ^ { * } \}$ based on the UAV location. Let $\Delta l =$ $\begin{array} { r } { \frac { N } { N _ { L } } - \frac { N } { N _ { L } ^ { \prime } } \in \mathbb { Z } } \end{array}$ . Then, the achievable rate based on the UAV trajectory in (46) can be given by

$$
\begin{array} { r l } & { ( L - \Delta l ) \left( C _ { l } ^ { * } + ( N _ { L } ^ { \prime } - N _ { L } ) R ^ { \operatorname* { m a x } } \right) } \\ { = } & { ( L - \Delta l ) C _ { l } ^ { * } + \Delta l N _ { L } R ^ { \operatorname* { m a x } } \geq L C _ { l } ^ { * } . } \end{array}\tag{47}
$$

Hence, the achievable rate with frame length $N _ { L } ^ { \prime }$ is no less than that with frame length $N _ { L }$ , thus completing the proof.

In Proposition 2, we reveal a useful and fundamental trade-off between sensing frequency and communication rate. Note that the above interesting results not only help solve problem (P3) more efficiently but also provide a novel idea to construct a high-quality solution to problem (P1), as elaborated below.

## B. Low-Complexity Algorithm for Solving (P1)

The large mission period $T$ may entail a large number of trajectory points in practice, thus resulting in prohibitive computational complexity for the UAV trajectory design. To handle this problem, a low-complexity method to (P1) is presented based on our derived structural characteristics among ISAC frames (c.f. Lemma 3). To facilitate the analysis, we introduce problem (P3.1) as the achievable rate maximization problem in the case without the initial and final location constraints, which can be expressed similarly as (P2) by removing constraint (12f).

If the optimal achievable rate of problem (P3.1) is denoted by $R ^ { * }$ , it is not difficult to find that the optimal achievable rate of problem (P1) equals to $R ^ { * }$ when $T \to \infty$ . The optimized UAV trajectory of problem (P3.1) obtained via Algorithm 1 is denoted by ${ \cal Q } ^ { \prime } = \{ { \pmb q } ^ { \prime } [ 1 ] , \cdot \cdot \cdot , { \pmb q } ^ { \prime } [ N _ { L } ] \}$ . Then, a high-quality and low-complexity UAV trajectory of (P1) can be obtained by composing three sub-trajectories: The UAV first flies straightly at its maximum speed from the initial location $q _ { I }$ towards $q ^ { * } [ 1 ]$ or $q ^ { * } [ N _ { L } ]$ (closer one); then flies back and forth along the trajectory $Q ^ { \prime } { \mathrm { ; } }$ ; finally flies straightly at its maximum speed to final location $q _ { F }$ . Furthermore, the corresponding optimized sensing time selection and user association for this constructed UAV trajectory can be solved by Algorithm 1 in a similar way. The complexity of this constructed solution is mainly determined by the step of obtaining the solution $\boldsymbol { Q } ^ { \prime } ,$ , which is about $\frac { L ^ { 3 . 5 } - 1 } { L ^ { 3 . 5 } } 1 0 0 \%$ percent reduced as compared to that of solving (P1) via Algorithm 1 directly. In particular, this low-complexity algorithm is preferred when the number of frames <sup>L</sup> is relatively large.

## V. NUMERICAL RESULTS

In this section, numerical results are provided for characterizing the performance of the proposed periodic sensing and communication design and for gaining insights into the design and implementation of UAV-based ISAC systems. In the simulation, we consider an area of 1 km $\times \ 1$ km with $K = 4$ users and $J \ = \ 4$ targets in the interested sensing area. Unless otherwise stated, the system parameters are set as follow. The number of antennas at the UAV $M = 1 6 ~ ( M _ { x } = M _ { y } = 4 )$ and the beam pattern gain threshold $\Gamma ^ { t h } = 6 e ^ { - 5 }$ <sup>= = 4</sup>. The UAV’s maximum horizontal flight speed is set as $V _ { \mathrm { m a x } } = 3 0$ m/s with the flight altitude $H = 4 0$ m. In addition, the channel power gain at the reference distance $d _ { 0 } = 1$ m and the noise power at each user are set as $\beta _ { 0 } = - 3 0$ dB and $\sigma ^ { 2 } = - 1 0 0 ~ \mathrm { d B } .$ respectively, and the maximum transmit power is $P _ { \mathrm { m a x } } = 0 . 1$ W. The flight period, ISAC frame length, and time slot length are denoted by $T = 8 0 \mathrm { ~ s } , T _ { L } = 2 0 \mathrm { ~ s } ,$ , and $\delta _ { t } ~ = ~ 0 . 2 5 ~ \mathrm { s } ,$ respectively. The minimum achievable rate requirement is set as $\bar { R } _ { k } ^ { t h } = \bar { 0 . 2 5 }$ bps/Hz.

We compare our proposed mechanism to two benchmarks

• Straight flight (SF): The UAV flies from the initial location $q _ { I }$ to the final location $q _ { F }$ along the straight line at the constant speed of $\frac { | { \pmb q } _ { F } - { \pmb q } _ { I } | } { T }$

• Fly-Hover-Fly (FHF): The UAV flies straightly at its maximum speed from the initial location to the optimized location obtained via solving the following problem

$$
\begin{array} { r } { \underset { w _ { c } , q , A , C } { \operatorname* { m a x } } \sum _ { k = 1 } ^ { K } R _ { k } } \\ { \mathrm { s . t . } \ ( 1 2 a ) - ( 1 2 d ) . } \end{array}\tag{48}
$$

After hovering at this optimized location, the UAV flies straightly at its maximum speed to the final location.

Except for the UAV trajectory, the corresponding beamforming, user association, and sensing time slots during the flight period of these two benchmarks are obtained by Algorithm 1 without updating the UAV trajectory.

## A. Comparison Versus Sensing Power Requirement

In Figs. 3 and $^ { 4 , }$ the UAV trajectories and the maximum achievable rate are illustrated respectively under different beam pattern gain thresholds $\Gamma ^ { t h }$ for our proposed penalty-based algorithm (Solving problem (P1)) and benchmark schemes. Specifically, it can be observed from Fig. 3 that as the beam pattern gain threshold $\Gamma ^ { t h }$ increases, the UAV’s trajectory shrinks gradually from a relatively larger arc toward users to several smaller arcs between the targets and the users; the closest distance from the UAV to the users also increases since the UAV needs to perform sensing tasks at a location closer to the targets. In particular, when $\Gamma ^ { t h } = 0 ,$ i.e., no beam pattern gain constraint is considered as in [34], the UAV sequentially visits and stays above each of the users by maximally exploiting its mobility; while when $\Gamma ^ { t h } = 1 2 \times$ $1 \dot { 0 } ^ { - 5 }$ , the UAV flies within a smaller region close to the targets <sup>10</sup>due to the higher sensing power requirement. Notice that in this setup, the closer the UAV flies to the targets, the farther it is away from the communication users inevitably. As a result, satisfying the beam pattern gain requirements of the targets will consume more transmit power and thus becomes the bottleneck for improving the maximum achievable rate of the system. Such a situation will become worse when the beam pattern gain and/or the distance between the users and the targets becomes larger.

![](images/2d96ae620d25e961626ae34cf26d28add2e098adc8e5727505b673ba9d8959b5.jpg)

(a) $\Gamma ^ { t h } = 0 .$  
![](images/decc20510f30e51626aff886c98f7d2a9df892bb3be4712227fe660b24213592.jpg)  
(c) $\Gamma ^ { t h } = 6 \times 1 0 ^ { - 5 } .$

![](images/01cc398172ee0268837eb26498aa6e3f3306f73785a590218468b9f9e03f5024.jpg)

(b) $\Gamma ^ { t h } = 2 \times 1 0 ^ { - }$  
![](images/8597073cddaacfd2b7eacd8658766f344e08cb1556e18ec11cb63dfd17f45611.jpg)  
(d) $\Gamma ^ { t h } = 1 2 \times 1 0 ^ { - 5 } .$

Fig. 3. UAV trajectories comparisons among the proposed penalty-based algorithm and benchmarks under different $\Gamma ^ { t h } ~ ( T = 4 0$ s and $T _ { L } = 2 0 ~ \mathrm { s } )$  
![](images/8e347c75b4d38cbfef62f54b2646182e7842f9c3a425ce6baa1410b60f833a44.jpg)  
Fig. 4. Achievable rate versus beam pattern gain threshold.

The effect of the beam pattern gain constraints on the maximum achievable rate is shown in Fig. 4. It is observed from Fig. 4 that the achievable rate gradually decreases as the beam pattern gain threshold $\Gamma ^ { t h }$ increases. Also, the achievable rate gain achieved by our proposed scheme over the “SF” scheme increases as the sensing power requirement decreases, since the UAV’s trajectory can be optimized in a larger feasible region for communication performance improvement. When the beam pattern gain threshold $\Gamma ^ { t h }$ is larger than $4 \times 1 0 ^ { - 5 }$ , the $^ { 6 6 } \mathrm { S F } ^ { \mathrm { , 9 } }$ scheme will become infeasible under the high-frequency sensing requirement, since the QoS constraints of users and the beam pattern gain constraints of targets cannot be satisfied without optimizing UAV trajectory. Moreover, the achievable rate of our proposed scheme achieves significant improvement as compared to the “FHF” scheme under lower sensing frequency, since the low-frequency sensing scenario shares more communication-only time slots in each ISAC frame for improving communication performance.

## B. Comparison Versus Sensing Frequency

In Figs. 5 and 6, we show the UAV trajectories and the maximum achievable rate under different sensing frequency (defined as $1 / T _ { L } )$ for our proposed penalty-based algorithm and benchmark schemes. Specifically, it can be observed from Fig. 5 that as the sensing frequency increases, the UAV’s trajectory shares more turn-backs between the targets and the users since there exist more ISAC frames within a given flight period $T = 4 0 \ \mathrm { s } .$ In particular, when $T = T _ { L }$ , i.e., there is only one sensing time for each target, the UAV can almost fly above each of the users to achieve better air-to-ground channels between the UAV and each user; when $T = 8 T _ { L }$ the UAV trajectory consists of multiple almost overlapping trajectory segments between the targets and one certain user. Generally speaking, as the sensing frequency increases, the UAV trajectory tends to be more restricted to avoid getting too far away from any of the targets.

![](images/d8efe57ebeb656cfc9be1ac735d065e491f0db0ea4cedae6e2379702cbfa069a.jpg)

(a) $T _ { L } = 4 0 s .$  
![](images/19d5ae0dcb0a334739c72498d9e7a5d26416b7e7fa86e4b996b29723215ad220.jpg)  
(c) $T _ { L } = 1 0 s .$

![](images/5f701c3786326f020df4791084dbf366fd4db656b7cdb7a2e8a96a4bb4a5467b.jpg)

(b) $T _ { L } = 2 0 s .$  
![](images/753f0231ea41d4810737106f22c3a45901d86e91b0cc1f01e09572cc06c02c0d.jpg)  
(d) $T _ { L } = 5 s .$

Fig. 5. UAV trajectories comparisons among the proposed penalty-based algorithm and benchmarks under different sensing frequency (defined as $1 / T _ { L } )$ .  
![](images/3c945658813fdd7bf1b4b2e26ffd91d34e9532e870f087f42b03eafe6cce5bc9.jpg)  
Fig. 6. Achievable rate versus sensing frequency requirement.

Fig. 6 shows the performance comparison among sensing power requirement, sensing frequency, and achievable rate. Specifically, as the sensing frequency increases, the achievable rate of all the considered mechanisms decreases, which validates the analysis in Proposition 2. Also, the achievable rate of our proposed algorithm under a higher beam pattern gain threshold $\bar { \Gamma } ^ { t h }$ degrades faster as compared to that under a lower threshold. The main reason is that a higher beam pattern gain threshold forces the UAV to perform sensing tasks at a location closer to the target, thereby resulting in increasing path loss within the communication-only duration. Furthermore, it is observed from Fig. 6 that the achievable rate gain achieved by our proposed scheme over the “FHF” and $\mathbf { \partial } ^ { 6 6 } \mathrm { S F } ^ { \mathrm { 9 } }$ schemes increases as the sensing frequency decreases, as the UAV has more non-sensing time to adjust its trajectory for communication performance improvement.

## C. User-Target Association and Beam Pattern

Next, the user association and target selection at the sensing time slots are shown in Fig. 7, where $T = T _ { L } = 4 0$ s, and $\Gamma ^ { t h } = 1 0 ^ { - 3 }$ <sup>= = 40</sup>. The UAV’s flight speed is illustrated in Fig. 7(a), <sup>Γ = 10</sup>where the user association and target selection are represented by blue and green dashed lines, respectively. Besides, it can be seen from Fig. 7(a) that the UAV tends to provide the communication service for the user which is closer to the associated target. The beam pattern gains in space at two selected sensing time slots are shown in Figs. 7(b) and $7 ( \mathrm { c } )$ where the beams are mainly concentrated in the direction of the selected target’s location and the associated user’s position.

![](images/3f06ca085adc5fd47e18ad2ed7e5a7006fa60a5163b7c08223259fff5dcafe58.jpg)  
(a) UAV trajectory with its speed.

![](images/5a58c3cd4029a6ca3704218a67075845132f3757f1b0fd40aa9743b01af3b86f.jpg)  
(b) Beam pattern at $n = 2 .$

![](images/fd6f1e9e5a2263e35ac915f63e932f397411f6ed6a131b1091d6260ccfa6a7d1.jpg)  
(c) Beam pattern at n = 159.

Fig. 7. UAV trajectory and its corresponding beam pattern gain at sensing time slots.  
![](images/a8d4e809b3f46b45e9ed0c75aeedbd94e8380394e293518857fa8470c6940184.jpg)  
(a) Comparisons under different number of antennas.

![](images/618d2a2cd953d0851f6222b2eceb4b82398b2381971b3940d85814350a27c59c.jpg)  
(b) Comparisons versus different flight periods.  
Fig. 8. Comparisons for proposed penalty-based algorithm and low-complexity algorithm.

## D. Lower Bound’s Gap and Low Complexity Method

Moreover, since problem (P2) is one approximation of problem (P1), we substitute the optimized solution obtained by Algorithm 1 back into the objective function of problem (P1) to obtain the actual achievable user rate, as shown in Fig. 8(a) for comparison. Specifically, the difference of average achievable rate during sensing time between original objective value $R _ { k , j } ^ { I S A C }$ and approximate objective value $\underline { { R } } _ { k , j } ^ { I S A \bar { C } }$ will decrease as the number of antennas increases, where $M _ { x } =$ $M _ { y } .$ In particular, the average achievable rate of the original objective value is almost approximated to the objective value (less than 1 ) when the number of antennas <sup>M</sup> is larger than 16, which justifies the accuracy of our derived lower bound in Lemma 2.

Moreover, we show the communication performance difference between the proposed penalty-based algorithm (refers to Algorithm 1) and the proposed low-complexity algorithm (the proposed algorithm in Section IV-B) under different flight periods <sup>T</sup> in Fig. 8(b). The low-complexity algorithm can achieve a higher gain over the two benchmarks as the flight period increases. Interestingly, the achievable rate gain achieved by the penalty-based algorithm over the low-complexity algorithm will decrease as the flight period increases. In particular, for the proposed low-complexity algorithm, there is only no more than 5 performance loss as compared to the proposed penalty-based algorithm when the flight period is larger than 200 s. This is due to the derived structural characteristics of the optimal solutions among different ISAC frames. Specifically, for large flight periods, the flight time from the initial location or that to the final location accounts for a smaller proportion of the entire flight period <sup>T</sup> , and the corresponding communication rate is approximate to that without the location constraints.

## E. Pathloss Factor For Sensing

The effect of different pathloss factors for sensing power, i.e., the exponent of the distance in (12a), is further evaluated in Fig. 9. Fig. 9(a) shows that under the pathloss with the fourth power of the distance, the UAV trajectory shares several turn-backs between the targets and the users under $T = 2 T _ { L }$ and $\Gamma ^ { t h } = 8 \times 1 0 ^ { - 9 }$ , which is similar to that in Fig. 3(c) but with a much lower beam pattern gain threshold. It can be seen that the pathloss factor mainly affects the distance between the UAV and the target when performing sensing tasks, and has little effect on the overall trajectory trend. Fig. 9(b) shows that under high sensing frequency, the achievable rate also decreases in a similar trend with that in Fig. 4 as the beam pattern gain constraints increases; even under low sensing frequency, the achievable rate decreases faster since the UAV needs to perform sensing tasks at a location closer to the targets under the path loss related to the fourth power of distance.

![](images/a4119eb55903ca6afcbcca20854e5d7a3166cecb5f8963ea6e8a554aa2a097ce.jpg)  
(a) UAV trajectory under 4-exponent pathloss factor.

![](images/89a986927b9368281d56fa6b74584823416ce0ac3ac28bbf588a937a2f2d958e.jpg)  
(b) Comparisons versus beam pattern gain constraints.  
Fig. 9. The UAV trajectory and the achievable rate comparison under the pathloss factor with power of 4.

## VI. CONCLUSION AND FUTURE WORKS

In this paper, we investigated a new type of UAV-enabled periodic ISAC system. Specifically, the beamforming, user association, sensing time selection, and UAV trajectory were jointly optimized to maximize the sum achievable rate. The closed-form optimal beamforming vector was derived to significantly reduce the complexity of beamforming design, and a lower bound of the achievable rate was presented to facilitate UAV trajectory design. By ignoring the initial and final location constraints, a novel symmetric structure of the optimal solutions among adjacent frames was identified to reveal a fundamental trade-off between sensing frequency and communication capacity. Based on this, a low-complexity method was presented based on our derived structural characteristics. The numerical results validated the efficiency of our design over the benchmark schemes and also confirmed the benefits of the periodic ISAC framework. The more general cases considering the effects caused by imperfectly compensated Doppler for multi-UAV ISAC scenarios are worthwhile future works. In addition, the sensing-assisted communication problems considering the sensing gain and clutter interference will be further investigated in our future work.

## APPENDIX A

## PROOF OF PROPOSITION 1

For $\begin{array} { r l r } { \frac { M P _ { \operatorname* { m a x } } \cos ^ { 2 } \varphi _ { k , j } } { d ( q [ n ] , v _ { j } ) ^ { 2 } } } & { { } \ge } & { \Gamma ^ { t h } } \end{array}$ , We can readily derive that the beam pattern gain at target will be no less than the threshold $\Gamma ^ { t h }$ if the optimal beamforming vector is $\sqrt { P _ { \operatorname* { m a x } } } \frac { h _ { c , k } } { \vert \vert h _ { c , k } \vert \vert }$ . In the following, we prove that for $\begin{array} { r } { \frac { M P _ { \operatorname* { m a x } } \cos ^ { 2 } \varphi _ { k , j } } { d ( \pmb q [ n ] , \pmb v _ { j } ) ^ { 2 } } < \Gamma ^ { t h } } \end{array}$ , the optimal beamforming vector equals to $\begin{array} { r } { \frac { 1 } { \lambda _ { 1 } } \big ( \sqrt { \beta _ { c , k } } h _ { c , k } + \lambda _ { 2 } \sqrt { \Gamma ^ { t h } } h _ { r , j } e ^ { \jmath \varphi _ { k , j } } \big ) } \end{array}$

First, it can be easily shown that constraint (13b) is met with equality for the optimal solution since otherwise $\| \pmb { w } _ { c } \|$ can be always increased to improve the objective value until (13b) becomes active. Hence, constraint (13b) can be rewritten as $\| \pmb { w } _ { c } \| ^ { 2 } ~ = ~ P _ { \operatorname* { m a x } }$ . Hence, the corresponding Lagrangian <sup>=</sup>function of (13) is given by

$$
L ( { \boldsymbol { \ w } } _ { c } , \lambda _ { 1 } , \lambda _ { 2 } ) = - { \boldsymbol { \ w } } _ { c } ^ { H } h _ { c , k } h _ { c , k } ^ { H } { \boldsymbol { w } } _ { c } + \lambda _ { 1 } ( \left\| { \boldsymbol { \ w } } _ { c } \right\| ^ { 2 } - P _ { \operatorname* { m a x } } )
$$

$$
+ \lambda _ { 2 } \left( \Gamma ^ { t h } - { \pmb w } _ { c } ^ { H } { \pmb h } _ { r , j } { \pmb h } _ { r , j } ^ { H } { \pmb w } _ { c } \right) .\tag{49}
$$

We can construct the Karush-Kuhn-Tucker (KKT) conditions for the optimal solution at a feasible point as follows

$$
\begin{array} { r l } & { \nabla L ( \pmb { w } _ { c } , \lambda _ { 1 } , \lambda _ { 2 } ) = - \pmb { h } _ { c , k } \pmb { h } _ { c , k } ^ { H } \pmb { w } _ { c } + \lambda _ { 1 } \pmb { w } _ { c } } \\ & { \quad - \lambda _ { 2 } \pmb { h } _ { r , j } \pmb { h } _ { r , j } ^ { H } \pmb { w } _ { c } = 0 , } \end{array}
$$

$$
\lambda _ { 2 } \left( \Gamma ^ { t h } - { \pmb w } _ { c } ^ { H } { \pmb h } _ { r , j } { \pmb h } _ { r , j } ^ { H } { \pmb w } _ { c } \right) = 0 .\tag{50}
$$

(51)

From (50), it can be shown that

$$
\begin{array} { r } { { \pmb h } _ { c , k } { \pmb h } _ { c , k } ^ { H } { \pmb w } _ { c } + \lambda _ { 2 } { \pmb h } _ { r , j } { \pmb h } _ { r , j } ^ { H } { \pmb w } _ { c } = \lambda _ { 1 } { \pmb w } _ { c } . } \end{array}\tag{52}
$$

Multiplying both sides of equation (52) with ${ \pmb w } _ { c }$ leads to

$$
\begin{array} { r } { { \pmb w } _ { c } ^ { H } \pmb { h } _ { c , k } \pmb { h } _ { c , k } ^ { H } \pmb { w } _ { c } + \lambda _ { 2 } \pmb { w } _ { c } ^ { H } \pmb { h } _ { r , j } \pmb { h } _ { r , j } ^ { H } \pmb { w } _ { c } = \lambda _ { 1 } \pmb { w } _ { c } ^ { H } \pmb { w } _ { c } = \lambda _ { 1 } P _ { \mathrm { m a x } } . } \end{array}\tag{53}
$$

Let $\begin{array} { r } { \pmb { h } _ { c , k } ^ { H } \pmb { w } _ { c } = \sqrt { \beta _ { c , k } } e ^ { j \varphi _ { c , k } } , \pmb { h } _ { r , j } ^ { H } \pmb { w } _ { c } = \sqrt { \beta _ { r , j } } e ^ { j \varphi _ { r , j } } } \end{array}$ , it follows that

$$
\beta _ { c , k } + \lambda _ { 2 } \beta _ { r , j } = \lambda _ { 1 } P _ { \operatorname* { m a x } } .\tag{54}
$$

Define $\begin{array} { r c l } { H } & { = } & { [ h _ { c , k } , h _ { r , j } ] . } \end{array}$ , by multiplying both sides of equation (52) with $\left( { \cal H } ^ { H } { \cal H } \right) ^ { - 1 } { \cal H } ^ { H }$ , equation (52) becomes

$$
\begin{array} { r l } & { \left[ \begin{array} { c } { \sqrt { \beta _ { c , k } } e ^ { j \varphi _ { c , k } } } \\ { \lambda _ { 2 } \sqrt { \beta _ { r , j } } e ^ { j \varphi _ { r , j } } } \end{array} \right] } \\ & { \quad = \lambda _ { 1 } \left( \boldsymbol { H } ^ { H } \boldsymbol { H } \right) ^ { - 1 } \boldsymbol { H } ^ { H } \boldsymbol { w } _ { c } } \\ & { \quad = \frac { \lambda _ { 1 } } { V _ { k , j } } \left[ \begin{array} { c c } { \left| h _ { r , j } \right| ^ { 2 } } & { - h _ { c , k } ^ { H } h _ { r , j } } \\ { - \left( h _ { c , k } ^ { H } h _ { r , j } \right) ^ { H } } & { \left| h _ { c , k } ^ { H } \right| ^ { 2 } } \end{array} \right] \left[ \begin{array} { c } { \sqrt { \beta _ { c , k } } e ^ { j \varphi _ { c , k } } } \\ { \sqrt { \beta _ { r , j } } e ^ { j \varphi _ { r , j } } } \end{array} \right] . } \end{array}\tag{55}
$$

In (55), $V _ { k , j } = { \left\| h _ { c , k } ^ { H } \right\| } ^ { 2 } { \| h _ { r , j } \| } ^ { 2 } - { \left| h _ { c , k } ^ { H } h _ { r , j } \right| } ^ { 2 } \neq 0 .$ , otherwise MRT is the optimal beamforming. If $\lambda _ { 2 } = 0$ , it follows that $\begin{array} { r } { \sqrt { \beta _ { r , j } } = \frac { \left\| h _ { c , k } ^ { H } h _ { r , j } \right\| } { \left\| h _ { c , k } ^ { H } \right\| ^ { 2 } } \sqrt { \beta _ { c , k } } } \end{array}$ according to (55). By plugging this condition into $( 5 4 ) , \beta _ { c , k } = P _ { \operatorname* { m a x } } \lvert \lvert h _ { c , k } \rvert \rvert$ , which holds if and only if $\begin{array} { r } { \pmb { w } ^ { * } = \sqrt { P _ { \operatorname* { m a x } } } \frac { \pmb { h } _ { c , k } } { \| \pmb { h } _ { c , k } \| } } \end{array}$ . When $\lambda _ { 2 } \neq 0$ , the KKT condition

$$
\begin{array} { l } { { \displaystyle | \cos \varphi _ { k , j } | = \frac { 1 } { M } \left| \sum _ { m _ { x } = 1 } ^ { M _ { x } } e ^ { j \pi m _ { x } ( \Phi ( q [ n ] , v _ { j } ) - \Phi ( q [ n ] , u _ { k } ) ) } \sum _ { m _ { y } = 1 } ^ { M _ { y } } e ^ { j \pi m _ { y } ( \Omega ( q [ n ] , v _ { j } ) - \Omega ( q [ n ] , u _ { k } ) ) } \right| } } \\ { { \displaystyle \quad \quad = \frac { 1 } { M } \left| e ^ { j \pi M \Delta \Omega / 2 - \jmath \pi \Delta \Omega / 2 } \left( \frac { e ^ { - \jmath \pi M \Delta \Omega / 2 } - e ^ { j \pi M \Delta \Omega / 2 } } { e ^ { - \jmath \pi \Delta \Omega / 2 } - e ^ { \jmath \pi \Delta \Omega / 2 } } \right) \sum _ { m _ { x } = 1 } ^ { M _ { x } } e ^ { j \pi m _ { x } ( \Phi ( q [ n ] , v _ { j } ) - \Phi ( q [ n ] , u _ { k } ) ) } \right| } } \\ { { \displaystyle \quad \quad = \left| \frac { \sin M _ { x } \Delta \Phi \pi / 2 } { M _ { x } \sin \Delta \Phi \pi / 2 } \right| \left| \frac { \sin M _ { y } \Delta \Omega \pi / 2 } { M _ { y } \sin \Delta \Omega \pi / 2 } \right| } . } \end{array}\tag{61}
$$

in (51) can be written as $\pmb { w } _ { c } ^ { H } \pmb { h } _ { r , j } \pmb { h } _ { r , j } ^ { H } \pmb { w } _ { c } = \beta _ { r , j } = \Gamma ^ { t h }$ . Since $\lambda _ { 1 }$ and $\lambda _ { 2 }$ are real-valued, equation (55) can be rewritten as

$$
\left[ \begin{array} { c } { \sqrt { \beta _ { c , k } } } \\ { \lambda _ { 2 } \sqrt { \Gamma ^ { t h } } } \end{array} \right] = \frac { \lambda _ { 1 } } { V _ { k , j } } \left[ \begin{array} { c } { \left\| h _ { r , j } \right\| ^ { 2 } \sqrt { \beta _ { c , k } } - | h _ { c , k } ^ { H } h _ { r , j } | \sqrt { \Gamma ^ { t h } } } \\ { \left\| h _ { c , k } ^ { H } \right\| ^ { 2 } \sqrt { \Gamma ^ { t h } } - | h _ { c , k } ^ { H } h _ { r , j } | \sqrt { \beta _ { c , k } } } \end{array} \right]\tag{56}
$$

and

$$
\left[ \begin{array} { c } { \sqrt { \beta _ { c , k } } } \\ { \lambda _ { 2 } \sqrt { \Gamma ^ { t h } } } \end{array} \right] = \frac { \lambda _ { 1 } } { V _ { k , j } } \left[ \begin{array} { c } { \left\| h _ { r , j } \right\| ^ { 2 } \sqrt { \beta _ { c , k } } + \left| h _ { c , k } ^ { H } h _ { r , j } \right| \sqrt { \Gamma ^ { t h } } } \\ { \left\| h _ { c , k } ^ { H } \right\| ^ { 2 } \sqrt { \Gamma ^ { t h } } + \left| h _ { c , k } ^ { H } h _ { r , j } \right| \sqrt { \beta _ { c , k } } } \end{array} \right] ,\tag{57}
$$

when $\varphi _ { r , j } - \varphi _ { c , k } = - \varphi _ { k , j } + 2 n \pi$ and $\varphi _ { r , j } - \varphi _ { c , k } = - \varphi _ { k , j } +$ $( 2 n + 1 ) \pi , n \in \mathbb { Z } .$ , respectively. By plugging (56) or (57) into (54), then $\beta _ { c , k }$ can be expressed as

$$
\beta _ { c , k } ^ { + } = \frac { \left\| h _ { c , k } ^ { H } \right\| ^ { 2 } } { \left\| h _ { r , j } \right\| ^ { 2 } } \left( \sqrt { \Gamma ^ { t h } } \cos \varphi _ { k , j } + P _ { j } \sin \varphi _ { k , j } \right) ^ { 2 }\tag{58}
$$

or

$$
\beta _ { c , k } ^ { - } = \frac { \left\| h _ { c , k } ^ { H } \right\| ^ { 2 } } { \left\| h _ { r , j } \right\| ^ { 2 } } \Big ( \sqrt { \Gamma ^ { t h } } \cos \varphi _ { k , j } - P _ { j } \sin \varphi _ { k , j } \Big ) ^ { 2 } ,\tag{59}
$$

where $\begin{array} { r l r } { P _ { j } } & { { } = } & { \sqrt { P _ { \mathrm { m a x } } \| h _ { r , j } \| ^ { 2 } - \Gamma ^ { t h } } } \end{array}$ and $\begin{array} { r l } { \varphi _ { k , j } } & { { } = } \end{array}$ arccos $\frac { | \boldsymbol { h } _ { c , k } ^ { H } \boldsymbol { h } _ { r , j } | } { \| \boldsymbol { h } _ { c , k } ^ { H } \| \| \boldsymbol { h } _ { r , j } \| }$ . Since $\beta _ { c , k } ^ { + } > \beta _ { c , k } ^ { - }$ , the optimal solution to problem in (13) can be obtained when $\beta _ { c , k } = \beta _ { c , k } ^ { + }$ . Then, by plugging (58) into (56), we have $\begin{array} { r } { \lambda _ { 1 } ^ { * } = \frac { \Upsilon \left. \left. \boldsymbol { h } _ { c , k } ^ { H } \right. \right. ^ { 2 } \sin \varphi _ { k , j } } { \sqrt { P _ { \operatorname* { m a x } } \left. \boldsymbol { h } _ { r , j } \right. ^ { 2 } - \Gamma ^ { t h } } } } \end{array}$ and $\begin{array} { r l r } { \lambda _ { 2 } ^ { * } } & { { } = } & { \frac { \Upsilon \left. \left. \boldsymbol { h } _ { c , k } ^ { H } \right. \right. ^ { 2 } \sqrt { \Gamma ^ { t h } } - \Upsilon ^ { 2 } \left. \left. \boldsymbol { h } _ { c , k } ^ { H } \right. \right. \left. \left. \boldsymbol { h } _ { r , j } \right. \right. \cos \varphi _ { k , j } ^ { * } } { \| \boldsymbol { h } _ { r , j } \| ^ { 2 } \sqrt { P _ { \operatorname* { m a x } } \| \boldsymbol { h } _ { r , j } \| ^ { 2 } \Gamma ^ { t h } - \left( \Gamma ^ { t h } \right) ^ { 2 } } \sin \varphi _ { k , j } } } \end{array}$ , where $\begin{array} { r } { \Upsilon = \sqrt { \Gamma ^ { t h } } \cos \varphi _ { k , j } + \sqrt { P _ { \operatorname* { m a x } } \left\| h _ { r , j } \right\| ^ { 2 } - \Gamma ^ { t h } \sin \varphi _ { k , j } } } \end{array}$ . Hence, the optimal beamforming can be expressed as

$$
\pmb { w } _ { c } ^ { * } = \frac { 1 } { \lambda _ { 1 } ^ { * } } \left( \sqrt { \beta _ { c , k } ^ { + } } h _ { c , k } + \lambda _ { 2 } ^ { * } \sqrt { \Gamma ^ { t h } } h _ { r , j } e ^ { - \jmath \varphi _ { k , j } } \right) .\tag{60}
$$

By combining the above results above, Proposition 1 is finally proved.

## APPENDIX B PROOF OF LEMMA 1

Let $\begin{array} { r l r } { \Delta \Omega } & { { } = } & { \Omega ( \boldsymbol { q } [ n ] , \boldsymbol { v } _ { j } ) - \Omega ( \boldsymbol { q } [ n ] , \boldsymbol { u } _ { k } ) } \end{array}$ and $\begin{array} { r l r } { \Delta \Phi } & { { } = } & { } \end{array}$ $\Phi ( \pmb q [ n ] , \pmb v _ { j } ) - \Phi ( \pmb q [ n ] , \pmb u _ { k } )$ <sup>)</sup>. When $\Delta \Omega \ = \ 0$ and $\Delta \Phi \ = \ 0 .$ <sup>Φ(</sup>i.e., ${ \pmb u } _ { k } = { \pmb v } _ { j }$ <sup>Φ( [</sup>, then $\begin{array} { r } { \dot { \gamma } _ { 0 } ^ { \ast } = \gamma _ { 0 } \frac { M P _ { \mathrm { m a x } } } { d ( \pmb q [ n ] , \pmb u _ { k } ) ^ { 2 } } } \end{array}$ <sup>= 0</sup>. When $\Delta \Omega \neq 0 .$ <sup>= 0</sup>, and $\Delta \Phi \neq 0 ,$ , | $\varphi _ { k , j } |$ can be recast as shown in (61), shown <sup>ΔΦ = 0 cos</sup>at the top of the page. When $M _ { x } \ \to \ \infty$ or $M _ { y } \  \ \infty ,$ $\left| \frac { \sin M _ { x } \Delta \bar { \Phi } \pi / 2 } { M _ { x } \sin \Delta \Phi \pi / 2 } \right| \left| \frac { \sin \bar { M } _ { y } \bar { \Delta } \Omega \pi / 2 } { M _ { y } \sin \Delta \Omega \pi / 2 } \right| ~ = ~ 0$ , as i.e., $\varphi _ { k , j } ~ = ~ 0 .$

When $\Delta \Omega \ = \ 0$ or $\Delta \Phi \ = \ 0 ;$ , $\varphi _ { k , j }$ can be transformed into $| \begin{array} { c c } { { \displaystyle | \frac { \sin { M _ { x } } \Delta \Phi \pi / 2 } { M _ { x } \sin { \Delta \Phi \pi / 2 } } | } } & { { \mathrm { o r } } } \end{array} \ | \begin{array} { c c } { { \displaystyle \sin { M _ { y } } \Delta \Omega \pi / 2 } } \\ { { \displaystyle M _ { y } \sin { \Delta \Omega \pi / 2 } } } \end{array} | ,$ , respectively. Then, $\cos \varphi _ { k , j } = 0$ when $M _ { x }  \infty$ and $M _ { y }  \infty$ . In this case, $\begin{array} { r } { \gamma _ { k } ^ { * } = \gamma _ { 0 } \frac { M P _ { \operatorname* { m a x } } - \Gamma ^ { t h } d ( \pmb { q } [ n ] , \pmb { v } _ { j } ) ^ { 2 } } { d ( \pmb { q } [ n ] , \pmb { u } _ { k } ) ^ { 2 } } } \end{array}$ . Thus, (16) holds.

Accordingly, we can readily prove that the optimal horizontal coordinate should be within the line formed by $\mathbf { \Delta } \mathbf { u } _ { k }$ and $v _ { j } ,$ Then, the horizontal distance from UAV to user <sup>k</sup> is denoted by <sup>x</sup>, and $x \neq 0 { \mathrm { ~ i f ~ } } u _ { k } \neq v _ { j }$ . By taking the derivative of <sup>x</sup> to $\gamma _ { k } ^ { * }$ , the following condition holds

$$
x ^ { 2 } + \left( \frac { M P _ { \operatorname* { m a x } } } { \Gamma ^ { t h } d ( u _ { k } , v _ { j } ) } - d ( { \pmb u } _ { k } , { \pmb v } _ { j } ) \right) x - H ^ { 2 } = 0 .\tag{62}
$$

Then, the optimal UAV location can be obtained by solving the equation in (62), i.e., $\begin{array} { r } { x = \frac { \sqrt { Z ^ { 2 } + 4 H ^ { 2 } } - Z } { 2 } } \end{array}$ , where $\begin{array} { r } { Z = \frac { M P _ { \mathrm { m a x } } } { \Gamma ^ { t h } D _ { k , j } } - } \end{array}$ $\begin{array} { r } { D _ { k , j } . \mathrm { ~ A s ~ } \frac { x } { D _ { k , j } } = \frac { d ( q [ n ] , { \pmb u } _ { k } ) } { d ( { \pmb u } _ { k } , { \pmb v } _ { j } ) } } \end{array}$ , then the UAV location with maximum achievable rate $\begin{array} { r } { \pmb q _ { k , j } ^ { * } = \pmb { u } _ { k } + \frac { \sqrt { Z ^ { 2 } + 4 H ^ { 2 } } - Z } { 2 D _ { k , j } } ( \pmb { v } _ { j } - \pmb { u } _ { k } ) } \end{array}$ and thus complete the proof.

## REFERENCES

[1] A. Hassanien, M. G. Amin, E. Aboutanios, and B. Himed, “Dualfunction radar communication systems: A solution to the spectrum congestion problem,” IEEE Signal Process. Mag., vol. 36, no. 5, pp. 115–126, Sep. 2019.

[2] A Research Outlook Towards 6G, Ericsson, Stockholm, Sweden, 2020.

[3] B. Li, A. P. Petropulu, and W. Trappe, “Optimum co-design for spectrum sharing between matrix completion based MIMO radars and a MIMO communication system,” IEEE Trans. Signal Process., vol. 64, no. 17, pp. 4562–4575, Sep. 2016.

[4] W. Yuan, Z. Wei, S. Li, J. Yuan, and D. W. K. Ng, “Integrated sensing and communication-assisted orthogonal time frequency space transmission for vehicular networks,” IEEE J. Sel. Topics Signal Process., vol. 15, no. 6, pp. 1515–1528, Nov. 2021.

[5] J. A. Zhang et al., “An overview of signal processing techniques for joint communication and radar sensing,” IEEE J. Sel. Topics Signal Process., vol. 15, no. 6, pp. 1295–1315, Nov. 2021.

[6] H. Godrich, A. M. Haimovich, and R. S. Blum, “Target localization accuracy gain in MIMO radar-based systems,” IEEE Trans. Inf. Theory, vol. 56, no. 6, pp. 2783–2803, Jun. 2010.

[7] C. Sturm and W. Wiesbeck, “Waveform design and signal processing aspects for fusion of wireless communications and radar sensing,” Proc. IEEE, vol. 99, no. 7, pp. 1236–1259, Jul. 2011.

[8] L. Giroto de Oliveira, B. Nuss, M. B. Alabd, A. Diewald, M. Pauli, and T. Zwick, “Joint radar-communication systems: Modulation schemes and system design,” IEEE Trans. Microw. Theory Techn., vol. 70, no. 3, pp. 1521–1551, Mar. 2022.

[9] F. Liu, L. Zhou, C. Masouros, A. Li, W. Luo, and A. Petropulu, “Toward dual-functional radar-communication systems: Optimal waveform design,” IEEE Trans. Signal Process., vol. 66, no. 16, pp. 4264–4279, Aug. 2018.

[10] R. Liu, M. Li, Q. Liu, and A. L. Swindlehurst, “Dual-functional radarcommunication waveform design: A symbol-level precoding approach,” IEEE J. Sel. Topics Signal Process., vol. 15, no. 6, pp. 1316–1331, Nov. 2021.

[11] K. V. Mishra, M. R. B. Shankar, V. Koivunen, B. Ottersten, and S. A. Vorobyov, “Toward millimeter-wave joint radar communications: A signal processing perspective,” IEEE Signal Process. Mag., vol. 36, no. 5, pp. 100–114, Sep. 2019.

[12] J. A. Zhang, X. Huang, Y. J. Guo, J. Yuan, and R. W. Heath, Jr., “Multibeam for joint communication and radar sensing using steerable analog antenna arrays,” IEEE Trans. Veh. Technol., vol. 68, no. 1, pp. 671–685, Jan. 2019.

[13] D. K. Pin Tan et al., “Integrated sensing and communication in 6G: Motivations, use cases, requirements, challenges and future directions,” in Proc. IEEE JC S, Feb. 2021, pp. 1–6.

[14] T. Wild, V. Braun, and H. Viswanathan, “Joint design of communication and sensing for beyond 5G and 6G systems,” IEEE Access, vol. 9, pp. 30845–30857, 2021.

[15] H. Wymeersch et al., “Integration of communication and sensing in 6G: A joint industrial and academic perspective,” in Proc. IEEE PIMRC, Sep. 2021, pp. 1–7.

[16] Project IEEE 802.11bf WLAN Sensing. Accessed: Mar. 19, 2021. [Online]. Available: https://www.ieee802.org/11/Reports/tgbfupdate.htm

[17] Q. Zhang, X. Wang, Z. Li, and Z. Wei, “Design and performance evaluation of joint sensing and communication integrated system for 5G mmWave enabled CAVs,” IEEE J. Sel. Topics Signal Process., vol. 15, no. 6, pp. 1500–1514, Nov. 2021.

[18] Y. Cui, F. Liu, X. Jing, and J. Mu, “Integrating sensing and communications for ubiquitous IoT: Applications, trends, and challenges,” IEEE Netw., vol. 35, no. 5, pp. 158–167, Sep./Oct. 2021.

[19] F. Liu, C. Masouros, A. P. Petropulu, H. Griffiths, and L. Hanzo, “Joint radar and communication design: Applications, state-of-the-art, and the road ahead,” IEEE Trans. Commun., vol. 68, no. 6, pp. 3834–3862, Jun. 2020.

[20] L. Chen, F. Liu, W. Wang, and C. Masouros, “Joint radarcommunication transmission: A generalized Pareto optimization framework,” IEEE Trans. Signal Process., vol. 69, pp. 2752–2765, 2021.

[21] F. Liu, C. Masouros, A. Li, H. Sun, and L. Hanzo, “MU-MIMO communications with MIMO radar: From co-existence to joint transmission,” IEEE Trans. Wireless Commun., vol. 17, no. 4, pp. 2755–2770, Apr. 2018.

[22] L. Gupta, R. Jain, and G. Vaszkun, “Survey of important issues in UAV communication networks,” IEEE Commun. Surveys Tuts., vol. 18, no. 2, pp. 1123–1152, 2nd Quart. 2016.

[23] M. Hua, Y. Wang, Q. Wu, H. Dai, Y. Huang, and L. Yang, “Energyefficient cooperative secure transmission in multi-UAV-enabled wireless networks,” IEEE Trans. Veh. Technol., vol. 68, no. 8, pp. 7761–7775, Aug. 2019.

[24] Q. Wu, L. Liu, and R. Zhang, “Fundamental trade-offs in communication and trajectory design for UAV-enabled wireless network,” IEEE Wireless Commun., vol. 26, no. 1, pp. 36–44, Feb. 2019.

[25] M. Hua, Y. Wang, Z. Zhang, C. Li, Y. Huang, and L. Yang, “Power-efficient communication in UAV-aided wireless sensor networks,” IEEE Commun. Lett., vol. 22, no. 6, pp. 1264–1267, Jun. 2018.

[26] K. Meng, D. Li, X. He, and M. Liu, “Space pruning based time minimization in delay constrained multi-task UAV-based sensing,” IEEE Trans. Veh. Technol., vol. 70, no. 3, pp. 2836–2849, Mar. 2021.

[27] S. Zhang, H. Zhang, Z. Han, H. V. Poor, and L. Song, “Age of information in a cellular internet of UAVs: Sensing and communication trade-off design,” IEEE Trans. Wireless Commun., vol. 19, no. 10, pp. 6578–6592, Oct. 2020.

[28] K. Meng, X. He, D. Li, M. Liu, and C. Xu, “Sensing quality constrained packet rate optimization via multi-UAV collaborative compression and relay,” in Proc. IEEE INFOCOM Workshop, May 2021, pp. 1–6.

[29] Z. Lyu, G. Zhu, and J. Xu, “Joint maneuver and beamforming design for UAV-enabled integrated sensing and communication,” 2021, arXiv:2110.02857.

[30] X. Chen, Z. Feng, Z. Wei, F. Gao, and X. Yuan, “Performance of joint sensing-communication cooperative sensing UAV network,” IEEE Trans. Veh. Technol., vol. 69, no. 12, pp. 15545–15556, Dec. 2020.

[31] Z. Wang, R. Liu, Q. Liu, and L. Han, “QoS-oriented sensingcommunication-control co-design for UAV-enabled positioning,” 2021, arXiv:2108.09725.

[32] Z. Wei, F. Liu, D. W. K. Ng, and R. Schober, “Safeguarding UAV networks through integrated sensing, jamming, and communications,” in Proc. IEEE ICASSP, May 2022, pp. 8737–8741.

[33] Q. Wu et al., “A comprehensive overview on 5G-and-beyond networks with UAVs: From communications to sensing and intelligence,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 2912–2945, Oct. 2021.

[34] Q. Wu and R. Zhang, “Common throughput maximization in UAV-enabled OFDMA systems with delay consideration,” IEEE Trans. Wireless Commun., vol. 66, no. 12, pp. 6614–6627, Dec. 2018.

[35] N. Garcia, H. Wymeersch, E. G. Larsson, A. M. Haimovich, and M. Coulon, “Direct localization for massive MIMO,” IEEE Trans. Signal Process., vol. 65, no. 10, pp. 2475–2487, May 2017.

[36] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.

[37] Q. Wu, J. Xu, and R. Zhang, “Capacity characterization of UAV-enabled two-user broadcast channel,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1955–1971, Sep. 2018.

[38] E. Kang, H. Hwang, and D. Han, “A fine carrier recovery algorithm robustto Doppler shift for OFDM systems,” IEEE Trans. Consum. Electron., vol. 56, no. 3, pp. 1218–1222, Aug. 2010.

[39] M. Xing, X. Jiang, R. Wu, F. Zhou, and Z. Bao, “Motion compensation for UAV SAR based on raw radar data,” IEEE Trans. Geosci. Remote Sens., vol. 47, no. 8, pp. 2870–2883, Aug. 2009.

[40] M. Pieraccini, L. Miccinesi, and N. Rojhani, “A Doppler range compensation for step-frequency continuous-wave radar for detecting small UAV,” Sensors, vol. 19, no. 6, p. 1331, Mar. 2019.

[41] X. Liu, T. Huang, N. Shlezinger, Y. Liu, J. Zhou, and Y. C. Eldar, “Joint transmit beamforming for multiuser MIMO communications and MIMO radar,” IEEE Trans. Signal Process., vol. 68, pp. 3929–3944, 2020.

[42] X. Wang, A. Hassanien, and M. G. Amin, “Dual-function MIMO radar communications system design via sparse array optimization,” IEEE Trans. Aerosp. Electron. Syst., vol. 55, no. 3, pp. 1213–1226, Jun. 2019.

[43] A. Aubry, A. DeMaio, A. Farina, and M. Wicks, “Knowledge-aided (potentially cognitive) transmit signal and receive filter design in signaldependent clutter,” IEEE Trans. Aerosp. Electron. Syst., vol. 49, no. 1, pp. 93–117, Jan. 2013.

[44] D. P. Bertsekas, “Nonlinear programming,” J. Oper. Res. Soc., vol. 48, no. 3, p. 334, 1997.

[45] Y. Cai, Q. Shi, B. Champagne, and G. Y. Li, “Joint transceiver design for secure downlink communications over an amplify-and-forward MIMO relay,” IEEE Trans. Commun., vol. 65, no. 9, pp. 3691–3704, Sep. 2017.

[46] G. Zhang, Q. Wu, M. Cui, and R. Zhang, “Securing UAV communications via joint trajectory and power control,” IEEE Trans. Wireless Commun., vol. 18, no. 2, pp. 1376–1389, Feb. 2019.

![](images/84a86091c9caeabe4753922c3fc995a0e4e1fed45814389a16fe52a3afbb96a8.jpg)

Kaitao Meng (Member, IEEE) received the B.E. and Ph.D. degrees in information engineering from Wuhan University, Wuhan, China, in 2016 and 2021, respectively. He is currently a Post-Doctoral Researcher with the State Key Laboratory of Internet of Things for Smart City, University of Macau, Macau, China. His current research interests include integrated sensing and communication, multi-UAV collaboration, and intelligent reflecting surface.

![](images/929c2429f17a5d1d4c33a3b57fdde68a933b83f6d28a29aea084d82d79bb786e.jpg)

Qingqing Wu (Senior Member, IEEE) received the B.Eng. degree in electronic engineering from the South China University of Technology in 2012 and the Ph.D. degree in electronic engineering from Shanghai Jiao Tong University (SJTU) in 2016. He is currently an Assistant Professor with the State Key Laboratory of Internet of Things for Smart City, University of Macau. From 2016 to 2020, he was a Research Fellow with the Department of Electrical and Computer Engineering, National University of Singapore. He has coauthored more than 100 IEEE

journal articles with 25 ESI highly cited papers and eight ESI hot papers, which have received more than 13 000 Google citations. His current research interests include intelligent reflecting surface (IRS), unmanned aerial vehicle (UAV) communications, and MIMO transceiver design.

He was listed as the Clarivate ESI Highly Cited Researcher in 2021, the Most Influential Scholar Award in AI-2000 by Aminer in 2021, and World’s Top 2% Scientist by Stanford University in 2020 and 2021. He was a recipient of the IEEE Communications Society Young Author Best Paper Award in 2021, the Outstanding Ph.D. Thesis Award of China Institute of Communications in 2017, the Outstanding Ph.D. Thesis Funding in SJTU in 2016, the IEEE ICCC Best Paper Award in 2021, and IEEE WCSP Best Paper Award in 2015. He was the Exemplary Editor of IEEE COMMUNICATIONS LETTERS in 2019 and the exemplary reviewer of several IEEE journals. He serves as an Associate Editor for IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE COMMUNICATIONS LETTERS, IEEE WIRELESS COMMUNICATIONS LET-TERS, IEEE OPEN JOURNAL OF COMMUNICATIONS SOCIETY (OJ-COMS), and IEEE OPEN JOURNAL OF VEHICULAR TECHNOLOGY (OJVT). He is the Lead Guest Editor of IEEE JOURNAL ON SELECTED AREAS IN COM-MUNICATIONS on “UAV Communications in 5G and Beyond Networks,” and the Guest Editor of IEEE OPEN JOURNAL OF VEHICULAR TECHNOLOGY (OJVT) on “6G Intelligent Communications” and IEEE OPEN JOURNAL OF COMMUNICATIONS SOCIETY on “Reconfigurable Intelligent Surface-Based Communications for 6G Wireless Networks.” He is the Workshop Co-Chair of IEEE ICC 2019-2022 workshop on “Integrating UAVs into 5G and Beyond” and the Workshop Co-Chair of IEEE GLOBECOM 2020 and ICC 2021 workshop on “Reconfigurable Intelligent Surfaces for Wireless Communication for Beyond 5G.” He serves as the Workshops and Symposia Officer of Reconfigurable Intelligent Surfaces Emerging Technology Initiative and Research Blog Officer of Aerial Communications Emerging Technology Initiative. He is the IEEE Communications Society Young Professional Chair in Asia Pacific Region.

![](images/c81e8ed1ad2eb07b71d3b16870b58344b4b761aafe0fc30e1be405955a155ef8.jpg)

Shaodan Ma (Senior Member, IEEE) received the double bachelor’s degree in science and economics and the M.Eng. degree in electronic engineering from Nankai University, Tianjin, China, in 1999 and 2002, respectively, and the Ph.D. degree in electrical and electronic engineering from The University of Hong Kong, Hong Kong, in 2006. From 2006 to 2011, she was a Post-Doctoral Fellow at The University of Hong Kong. Since August 2011, she has been with the University of Macau, where she is currently a Professor. Her

research interests include array signal processing, transceiver design, localization, mmwave communications, and massive MIMO. She was the Symposium Co-Chair for various conferences, including 2021 IEEE ICC, 2019 IEEE/CIC ICCC, 2019 IEEE ICC, 2016 IEEE GLOBECOM, and 2016 IEEE ICC. Currently, she serves as an Editor for IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE WIRELESS COMMUNICATIONS LETTERS, and Journal of Communications and Information Networks.

![](images/337b768a134187fe9bdc315926f115b73e828e4bde91e6f3bcfaa3808821b57d.jpg)

Wen Chen (Senior Member, IEEE) is currently a tenured Professor with the Department of Electronic Engineering, Shanghai Jiao Tong University, China, where he is also the Director of the Broadband Access Network Laboratory. He has published more than 110 articles in IEEE journals and more than 120 papers in IEEE conferences, with citations more than 8000 in Google scholar. His research interests include multiple access, wireless AI, and meta-surface communications. He is a fellow of the Chinese Institute of Electronics and the Dis-

tinguished Lecturers of IEEE Communications Society and IEEE Vehicular Technology Society. He is the Shanghai Chapter Chair of IEEE Vehicular Technology Society, an Editor of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE ACCESS, and IEEE OPEN JOURNAL OF VEHICULAR TECHNOLOGY.

![](images/82f978294d813b1923e9c9f29bc6ecdd8662b7254758155a985bf309bc82b4b6.jpg)

Kunlun Wang (Member, IEEE) received the Ph.D. degree in electronic engineering from Shanghai Jiao Tong University, Shanghai, China, in 2016. From 2016 to 2017, he was with Huawei Technologies Company Ltd., where he was involved in energy efficiency algorithm design. From 2017 to 2019, he was with the Key Laboratory of Wireless Sensor Network and Communication, SIMIT, Chinese Academy of Sciences, Shanghai. From 2019 to 2020, he was with the School of Information Science and Technology, ShanghaiTech University. Since 2021, he has been a Professor with the School of Communication and Electronic Engineering, East China Normal University. His current research interests include energy efficient communications, fog/edge computing networks, resource allocation, and optimization algorithm. He is the Lead Guest Editor of IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS on “Multi Tier Computing for Next Generation Wireless Networks.”

![](images/3708f81b2e2083352a8c57a0a887109ef751671a7a0c46448608b55a295a1b11.jpg)

Jun Li (Senior Member, IEEE) received the Ph.D. degree in electronic engineering from Shanghai Jiao Tong University, Shanghai, China, in 2009. From January 2009 to June 2009, he worked with the Department of Research and Innovation, Alcatel Lucent Shanghai Bell, as a Research Scientist. From June 2009 to April 2012, he was a Post-Doctoral Fellow at the School of Electrical Engineering and Telecommunications, University of New South Wales, Australia. From April 2012 to June 2015, he was a Research Fellow at the School of Electrical Engineering, The University of Sydney, Australia. He was a Visiting Professor at Princeton University from 2018 to 2019. Since June 2015, he has been a Professor at the School of Electronic and Optical Engineering, Nanjing University of Science and Technology, Nanjing, China. He has coauthored more than 200 papers in IEEE journals and conferences, and holds one U.S. patents and more than ten Chinese patents in these areas. His research interests include network information theory, game theory, distributed intelligence, multiple agent reinforcement learning and their applications in ultra-dense wireless networks, mobile edge computing, network privacy and security, and the Industrial Internet of Things. He is serving as an Editor for IEEE TRANSACTIONS ON WIRELESS COMMUNICATION and a TPC member for several flagship IEEE conferences.