# Age of Information Minimization in UAV-Assisted Covert Communication: Trajectory and Beamforming Design

Shima Salar Hosseini , Paeiz Azmi , Senior Member, IEEE, and Ali Nazari

Abstract—Covert communication is an emerging security solution to prevent or decrease the warden’s detection rate. Unmanned aerial vehicle (UAV), as an aerial covert transmitter, should jointly optimize the trajectory to ensure covertness. The eavesdropper-equipped UAV attempts to adversarially detect covert communication by adjusting its distance and setting the detection threshold. Due to the variation of the air-to-ground channel, the data status may have an expiration time. Information freshness is important in guaranteeing covertness, such as identifying threats and tracking movements. To quantify information freshness, age of Information (AoI), is represents the elapsed time since the most recent successfully decoded information was updated. We investigate UAV-assisted covert communication to minimize AoI with an aerial eavesdropper for the first time. However, to ensure the eavesdropper’s error detection rate, UAVenabled beamforming employs the power-domain non-orthogonal multiple access (PD-NOMA) technique to cover the covert user by a public user. PD-NOMA technique significantly improves the user’s AoI, too. The joint optimization problem contains nonconvex constraints and coupled optimization variables, including UAV trajectory, beamforming design, and the user’s AoI. We have developed an efficient alternating optimization technique to address it. Numerical results demonstrate the impact of the main parameters on the performance of the proposed system.

Index Terms—Unmanned aerial vehicle, covert communication, beamforming design, age of information, power domain non-orthogonal multiple access.

## I. INTRODUCTION

U <sup>NMANNED</sup> <sup>Aerial</sup> <sup>Vehicle</sup> <sup>(UAV)</sup> <sup>have</sup> <sup>the</sup> <sup>potential</sup>to significantly impact the deployment and operation of 5G and future 6G communication systems [1]. UAV as aerial base stations (BS) can enhance network coverage and capacity where traditional ground-BS infrastructure is limited or unavailable. This can help improve network performance and connectivity in remote or disaster-stricken areas [2]. UAV with edge capabilities can process and store data closer to the source, reducing latency and improving data transmission efficiency [3]. UAV can improve security in sensitive, emergency, or high-risk environments to transfer sensitive data securely without the probability of interception or tampering [4]. Regardless of secure communication techniques i.e., encryption, and physical layer security, covert communication as an advanced level of security conceals the existence of confidential wireless transmission and avoids detecting transmission from eavesdroppers [5]. Based on the advantages of UAV mobility discussed above, integrating UAV into a covert network can improve covertness by maneuvering towards legal receivers and maintaining distance from illegal receivers. In [6], in terms of maximizing the average covert transmission rate the UAV’s trajectory, and transmit power are jointly optimized subject to transmission outage and covertness constraints with Willie’s uncertain location. To maximize the average covert transmission rate under the constraints of UAV’ mobility, transmit powers, and warden’s detection error probability, authors jointly optimized the UAV’ transmit powers and three-dimensional (3D) trajectories in [7]. In [8], the 3D trajectory and transmit power of UAV are jointly optimized to maximize the average covert transmission rate subject to the covertness constraint with active ground wardens. The scenario of eavesdropping on multiple wardens from the multiple UAV’s links to ground users is considered in [9], where a UAV-mounted jammer generates artificial noise and assists covert communications. The problem is designed to maxmin the average rate by jointly optimizing user association, bandwidth allocation, UAV transmit power control, and UAV 3D deployment, subject to the detection error probability of each warden’s constraint. The air-to-ground (A2G) links on UAV-assisted covert communication systems cause the perfect detecting channels for an aerial warden, where most of the current articles focus on ground-based wardens, and only a few of them address the presence of an aerial warden. The authors in [10], proposed a UAV-relayed covert communication scheme with a ground transmitter and receiver with finite block length to maximize the effective transmission bits against a flying warden. The hovering location of the warden is obtained from the optimal detection thresholds for maximizing the covertness. Then, the block length and transmit power at the transmitter and the relay subject to the end-to-end error detection probability constraint are jointly optimized. Consequently, UAV-assisted covert communication suffers from high Willie’s eavesdropping due to free-space propagation signals. Beamforming is a promising approach for improving the covert rate with the capability of beamforming antenna design. In [11], the covert beamforming design for Internetof-things (IoT) networks-assisted intelligent reflecting surfaces (IRS) is presented. To maximize the covert rate, Alice and IRS are jointly beamformers designed subject to the perfect covert transmission constraint, total transmit power constraint of Alice, and the quality-of-service (QoS) of the IRS. In [12], Alice communicates with Carol to cover the covert transmission to Bob, focusing on optimizing the beamformer design for enhanced covert transmission rates in a unicast beamforming network. The beamforming design problem to maximize the achievable covert rate under the perfect covert transmission constraint, the QoS of Carol, and the total transmit power constraints of Alice are jointly optimized. The authors in [13] demonstrate the equipping of Alice with an antenna array to perform 3D beamforming in the presence of the jammer with multiple antennas to improve the covert rate. In [14], the UAV satellite covert communication is considered to maximize the covert transmission rate by jointly optimizing the transmitter’s 3D trajectory and 3D beamforming subject to the trajectory and covertness constraints. Consequently, one of the opportunistic techniques to guarantee covertness in the aerial system is proposing UAV-enabled beamforming to improve performance.

In addition, UAV-assisted covert communication can be utilized for emergency response and public safety applications, such as search and rescue missions, disaster assessment, and surveillance, and provide real-time situational awareness and support first responders in critical situations [15]. Enabling real-time coordination and decision-making is useful in military or government operations where confidentiality is paramount without requiring physical infrastructure. UAV’s capabilities such as high mobility and fast deployment can be applied in various applications, including real-time monitoring, surveillance, agriculture, disaster response, and infrastructure inspection [16]. Therefore, UAV can play an effective role in data freshness. Recently, a new metric named “age of information” is used for measuring data freshness, and refers to the time interval between signal generation and reaching the destination node [17]. Minimizing the age of information (AoI) in UAV-assisted covert networks ensures access to the most current data for effective decision-making. UAV missions can enhance the overall effectiveness and efficiency of freshness in different industries such as successful rescue operations, precision agriculture, natural disasters (earthquakes, hurricanes, or wildfires), and inspecting critical infrastructure (bridges, power lines, and pipelines) [18]. Investigation of information freshness in covert networks is a prominent area of interest in delay-sensitive secrecy applications. The authors in [19] jointly optimized the transmits probability and transmits the power of status information to maximize the covert energyefficiency (EE) of the device-to-device (D2D) pair subject to the covertness and information freshness constraints. To minimize the average covert AoI under the covertness constraints, the authors in [20] determined the tradeoff between covertness and timeliness affected by the block length, transmit power, and prior transmission probability. The letter [21] addressed the requirement of information freshness, in the covertness maximization problem subject to the AoI constraint. In [22], the reliable covert communication problem in dynamic environments is demonstrated. To minimize AoI in the time-varying channels, the transmit power of Alice and the user’s AoI are jointly optimized subject to the reliable covert constraint, the total transmit power constraint, the covertness constraint at Eve, and the QoS constraint of all users.

## Motivation and Contribution

UAV with AoI freshness metrics have extensive applications that can support confidential scenarios, such as health assessments, timely medical interventions, identifying threats, and tracking movements. To the best of our knowledge, there has been no research on UAV-assisted covert communication to minimize AoI in the presence of an eavesdropper-equipped UAV with trajectory and tracking capabilities of a covert transmitter. The proposed system model confronts two main challenges: i) the UAV’s communication time depends on the received packets’ AoI of the users, and ii) due to the air-to-ground line-of-sight (LoS) channels, an eavesdropper equipped UAV poses a serious threat to the security of covert communications. To address the mentioned challenges, this study investigates the joint design of UAV trajectory and beamforming to minimize the total AoI through the power-domain non-orthogonal multiple access (PD-NOMA) transmission technique in the presence of an eavesdropperequipped UAV with trajectory and tracking capabilities. The main contributions of this paper are summarized as follows:

• We propose UAV-assisted covert communication using a beamforming technique in the PD-NOMA system for covert and public users against an eavesdropper-equipped UAV. In this context, we formulate UAV trajectory and beamforming design jointly to minimize the AoI, subject to the following constraints: power transmission budget, fairness in terms of guaranteeing the covert user, the covertness optimization, ensuring the user’s packets reception before channel variations, quality of services, and UAV’s maximum flying speed.

• An eavesdropper-equipped UAV makes a decision rule to adversarially detect covert communication by jointly adjusting its distance to the UAV and setting the detection threshold. One of the achievements of this paper is deriving the eavesdropper’s optimal detection error rate independent of his distance to the UAV. This is due to the employment uncertainty in UAV-enabled beamforming. Since the beamformer vectors are designed based on the Channel State Information (CSI) of legitimate links, deriving the detection error rate is challenging for Eve. Therefore, we ensure the covert communication in the worst-case i.e., the eavesdropper operates within the collision avoidance distance constraints of two UAV.

• Additionally, to ensure covert communication of direct channels that are affected by the perfect aerial eavesdropping, we have considered: i) UAV-assisted multiple antennas with beamforming design and uniform distribution power budget, and ii) the capability of the UAV to serve both public and covert users simultaneously, enabled by PD-NOMA technology, which allows multiple users to share the same frequency band by allocating different power levels. Meanwhile, the eavesdropper employs an optimal detection strategy by comparing the average received signal power from Alice with the detection threshold to minimize the error detection rate. Therefore, the superimposition of covert and public signals creates confusion for the eavesdropper.

• Furthermore, by utilizing PD-NOMA, which employs Successive Interference Cancellation (SIC) ordering, all users can receive their packets simultaneously without waiting in a queue. This approach effectively improves the AoI.

• The communication time in the proposed scenario depends on the packets’ AoI of the users. Therefore, we discretize the communication time into time slots, with each duration guaranteeing the full reception of each packet before channel variation occurs. This leads to proposed effective constraints in trajectory design with a freshness approach.

• To tackle the proposed non-convex problems, we develop an alternating optimization approach. Hence, we decoupled our formulated optimization problem into three subproblems to obtain: 1) the AoI of the user which is in a linear programming standard form, 2) the UAV trajectory design which is approximated by the successive convex optimization technique, 3) the beamforming design which is approximated by semidefinite relaxation technique after establishing the rank-one condition. Also, the non-convex constraints are approximated by the first-order Taylor expansion.

• Numerical results represent that the proposed system achieved significant performance: 1) trajectory design and beamforming are both helpful in the achievable rate and AoI, 2) we always guarantee the achievable covert rate despite the presence of an eavesdropper equipped UAV by leveraging two strategies: a) utilizing the UAV as a transmitter that serves the public user through PD-NOMA, which effectively covers the covert user and reduces the eavesdropper’s detection rate, b) serving the public user continuously during flying times while dividing the covert packet into nats and serving the covert user in desirable time slots that meet the constraints, such as covertness and QoS (UAV monitors the covert user and serves her/him as soon as possible at a desirable time to guarantee covert communication in a fresh manner.), 3) the adopted PD-NOMA technique outperforms the orthogonal multiple access scheme from the freshness of AoI and achievable rate. 4), investigating the performance of A2G LoS channels in comparison to Rician channels from two perspectives of the achievable rate and total AoI, 5) Finally, we demonstrate the impact of the proposed eavesdropper-equipped UAV with trajectory and tracking capabilities, comparing its performance to benchmark scenarios such as placing an eavesdropper at a fixed optimal aerial point, an eavesdropper flying within a limited area, and a fixed-ground point concerning the covert detection rate.

![](images/751c512e70849606dcbda864e695489b0cf7d3c12e978d0909886ccfe0ff9ab0.jpg)  
Fig. 1. The considered system model.

Notations: In this paper, scalars are denoted by italic letters, vectors and matrices are respectively represented by boldfaced lowercase and uppercase letters. $\mathbb { R } ^ { \bar { M } \times 1 }$ , and $\mathbb { C } ^ { M \times i }$ are denote the space of M-dimensional real-valued, and complex valued vector, respectively. $\mathbf { a } ^ { T }$ , and $\mathbf { a } ^ { H }$ are transpose, and conjugate transpose of vector a, respectively. Also, |.| denotes the magnitude of a complex number, and k . k denotes the Euclidean norm of vector. The expectation and the probability of x are denoted by $\mathbb { E } \{ x \}$ , and $\operatorname* { P r } \{ x \}$ , respectively. $\mathcal { C N } ( \mu , \sigma ^ { 2 } )$ denotes the complex Gaussian distribution with mean of µ and variance of $\sigma ^ { 2 }$

## II. SYSTEM MODEL

## A. Considered Scenario and Assumptions

As illustrated in Fig. 1, we consider a UAV-assisted covert communication using a beamforming technique in the PD-NOMA system. The UAV, referred to as Alice, with beamforming serves the desired signal to the covert user (Bob) and public user (Carol) through the A2G channels while avoiding detection by the illegitimate user (Eve). Unlike most existing works [23], [24], [25], the probability of the presence of an aerial eavesdropper who can detect covert transmission through the A2G channels is considered. Alice is equipped with M antennas, while legitimate and illegitimate receivers have a single antenna. Let $\mathcal { M } \ = \ \{ 1 , . . . , M \}$ denote the set of Alice’s Antennas. It is a common assumption [26], for ease of exposition, we divide communication time T into N small equal time slots indexed by n where $n \_ { } \in { }$ $\mathcal { N } = \{ 1 , . . . , N \}$ . The location of Alice can be approximately unchanged in each time slot n with length $\delta \ = \ T / N$ [27], even with maximum flying speed $V _ { \mathrm { m a x } }$ . Alice flies horizontally with two-dimensional (2D) Cartesian coordinates $\mathbf { q } [ n ] \triangleq [ \dot { x } [ n ] , y [ n ] ] ^ { T } \in \mathbb { R } ^ { 2 \times 1 }$ at a constant altitude of H above the ground in time slot n. Also, Alice’s trajectory design is constrained by the maximum horizontal flying distance as follows:

$$
\| \mathbf { q } [ n + 1 ] - \mathbf { q } [ n ] \| \leqslant V _ { \operatorname* { m a x } } \delta , \ n = 1 , . . . , N - 1 .\tag{1}
$$

To verify the positive effect of PD-NOMA technique in covert communication, Alice superimposes the public signal $x _ { c } ^ { i } [ n ]$ with covert signal $x _ { b } ^ { i } [ n ]$ and then transmits from the i-th channel during the n-th time slot, as follows:

$$
{ \bf x } ^ { i } [ n ] = { \bf w } _ { c } [ n ] x _ { c } ^ { i } [ n ] + { \bf w } _ { b } [ n ] x _ { b } ^ { i } [ n ] , \ \forall n ,\tag{2}
$$

here, $\mathbf { w } _ { k } [ n ] \ \in \ \mathbb { C } ^ { M \times 1 }$ represents the transmit beamforming vectors for the corresponding set $k \in \{ b , c \}$ , which refers to legitimate users. It is assumed that $\mathbb { E } \{ | x _ { k } ^ { i } [ n ] | ^ { 2 } \} = 1$ , where $i = 1 , \dots , G$ , and G is the total number of channels used for transmitting $\mathbf { x } ^ { i } [ n ]$ to user k.

According to LoS communication links from Alice to the legitimate receivers, the channel gain from Alice to Bob, and Carol during time slot n, which follows the free-space path loss model [26], can be denoted as:

$$
\mathbf { h } _ { k } [ n ] = \sqrt { \mu _ { 0 } d _ { k } ^ { - 2 } [ n ] } \mathbf { a } ( \mathbf { q } [ n ] , \mathbf { u } _ { k } ) ,\tag{3}
$$

where $d _ { k } [ n ] = { \bf \sqrt { \| ~ } q [ } n ] - { \bf u } _ { k } \parallel ^ { 2 } + H ^ { 2 }$ refers to the distance between Alice and the legitimate user in the n-th time slot, and $\mathbf { u } _ { k } = [ x _ { k } , y _ { k } ] \in \mathbb { R } ^ { 2 \times 1 }$ is the 2D Cartesian coordinates of legitimate ground users. The channel power at the reference distance 1m, is denoted by $\mu _ { 0 }$ . Additionally, ${ \mathbf { a } } _ { k } [ n ]$ represents the transmit array response vector of Alice toward the legitimate user k, expressed as:

$$
\mathbf { a } _ { k } [ n ] = \left[ 1 , e ^ { - j 2 \pi { \frac { d } { \lambda } } \sin ( \theta [ n ] ) } , . . . , e ^ { - j 2 \pi { \frac { d } { \lambda } } ( M - 1 ) \sin ( \theta [ n ] ) } \right] ^ { T } ,\tag{4}
$$

where $d ,$ and λ are the space between two adjacent antennas and the carrier wavelength, respectively. Furthermore, $\begin{array} { r } { \sin ( \theta [ n ] ) = \frac { H } { d _ { k } [ n ] } } \end{array}$ , that $\theta [ n ]$ is the angle of departure (AoD) from Alice corresponding to legitimate user k at time slot [n]. Therefore, the received signal at the legitimate users in time slot n is given by:

$$
y _ { k } ^ { i } [ n ] = \mathbf { h } _ { k } ^ { H } [ n ] \mathbf { x } ^ { i } [ n ] + n _ { k } ^ { i } ,\tag{5}
$$

where $n _ { k } ^ { i } \sim \mathcal { C N } ( 0 , \sigma _ { k } ^ { 2 } )$ is the additive white Gaussian noise (AWGN) at legitimate user k, from i-th channel with zero mean and variance $\sigma _ { k } ^ { 2 } .$ , where $k \in \{ b , c \}$ . Hence, the achievable data rates from Alice to Bob and Carol in time slot n can be respectively expressed as:

$$
R _ { b } [ n ] = \log _ { 2 } \left( 1 + \frac { \left| \mathbf { h } _ { b } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] \right| ^ { 2 } } { \sigma _ { b } ^ { 2 } } \right) ,\tag{6}
$$

$$
R _ { c } [ n ] = \log _ { 2 } \left( 1 + \frac { \left| \mathbf { h } _ { c } ^ { H } [ n ] \mathbf { w } _ { c } [ n ] \right| ^ { 2 } } { \left| \mathbf { h } _ { c } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] \right| ^ { 2 } + \sigma _ { c } ^ { 2 } } \right) .\tag{7}
$$

These rate expressions follows the principle of PD-NOMA, where SIC is applied at Bob. As the user with the more favorable channel condition, Bob first decodes and subtracts Carol’s signal before decoding his own. In contrast, Carol decodes her signal directly by treating Bob’s signal as interference [28].

## B. Binary Hypothesis Testing at Eve

Eve attempts to detect covert signal transmissions from A2G links using a radiometer. Also, Eve’s horizontal coordinate is assumed $\mathbf { l } [ n ] ~ \triangleq ~ [ x _ { e } [ n ] , y _ { e } [ n ] ] ^ { T } ~ \in ~ \mathbb { R } ^ { 2 \times 1 }$ at a constant altitude h above the ground in time slot n. Regarding the aerial eavesdropping link between Alice and Eve, the channel gain during time slot n follows a large-scale LoS path loss [10], and is denoted as:

$$
\mathbf { h } _ { e } [ n ] = \sqrt { \mu _ { 0 } d _ { e } ^ { - 2 } [ n ] } \mathbf { a } ( \mathbf { q } [ n ] , \mathbf { 1 } [ n ] ) ,\tag{8}
$$

where $d _ { e } [ n ] = { \sqrt { \| \ \mathbf { q } [ n ] - \mathbf { 1 } [ n ] \ \| ^ { 2 } \ + ( H - h ) ^ { 2 } } }$ refers to the distance between Alice and Eve in the n-th time slot. Similarly to formulation (4), the eavesdropping array response vector of Alice toward Eve is defined as:

$$
\mathbf { a } _ { e } [ n ] = \left[ 1 , e ^ { - j 2 \pi { \frac { d } { \lambda } } \sin ( \phi [ n ] ) } , . . . , e ^ { - j 2 \pi { \frac { d } { \lambda } } ( M - 1 ) \sin ( \phi [ n ] ) } \right] ^ { T } ,\tag{9}
$$

where $\begin{array} { r } { \sin ( \phi [ n ] ) = \frac { H - h } { d _ { e } [ n ] } } \end{array}$ and φ[n] is the AoD of the eavesdropping link from Alice to Eve at time slot [n].

1) Detection Threshold Analysis: The received signal at Eve under two hypothesis tests: null $\mathcal { H } _ { 0 } .$ , and the alternative $\mathcal { H } _ { 1 }$ , is demonstrated as follows:

$$
y _ { e } ^ { i } [ n ] = \left\{ \begin{array} { l l } { { \bf h } _ { e } ^ { H } [ n ] { \bf w } _ { c } [ n ] x _ { c } ^ { i } [ n ] + n _ { e } ^ { i } , \quad \mathcal { H } _ { 0 } , } \\ { { \bf h } _ { e } ^ { H } [ n ] ( { \bf w } _ { c } [ n ] x _ { c } ^ { i } [ n ] + { \bf w } _ { b } [ n ] x _ { b } ^ { i } [ n ] ) + n _ { e } ^ { i } , \quad \mathcal { H } _ { 1 } , } \end{array} \right.\tag{10}
$$

where $n _ { e } ^ { i } \sim \mathcal { C N } ( 0 , \sigma _ { e } ^ { 2 } )$ is the AWGN at Eve from i-th channel with zero mean and variance $\sigma _ { e } ^ { 2 }$

Based on (10), Eve decides Alice’s covert transmission. Hence, the optimal decision rule to minimize the error detection rate at Eve can be expressed as follows:

$$
T _ { e } [ n ] = \frac { 1 } { G } \sum _ { i = 1 } ^ { G } \left| y _ { e } ^ { i } [ n ] \right| ^ { 2 } \gtrapprox \tau [ n ] ,\tag{11}
$$

where $T _ { e } [ n ]$ is the average power of received signal from Alice to Eve, $\tau [ n ]$ is the detection threshold at time slot $n ,$ and $\mathcal { D } _ { 0 }$ and $\mathcal { D } _ { 1 }$ are the decision parameters in favor of $\mathcal { H } _ { \mathrm { 0 } }$ and $\mathcal { H } _ { 1 }$ , respectively. It is common in UAV network literature to assume an infinite number of channel links in each time slot [6]. Similarly, in this scenario, we consider that Eve can receive signals from an infinite number of channel links, i.e., $i \to \infty$ . By noting that $x _ { c } ^ { i } [ n ] , x _ { b } ^ { i } [ n ]$ , and $n _ { e } ^ { i } [ n ]$ are independent, and based on (10), and (11), $T _ { e } [ n ]$ is rewritten as follows:

$$
\begin{array}{c} \begin{array} { r } { T _ { e } [ n ] = \left\{ \left| \mathbf { h } _ { e } ^ { H } [ n ] \mathbf { w } _ { c } [ n ] \right| ^ { 2 } + \sigma _ { e } ^ { 2 } , \quad \mathcal { H } _ { 0 } , \right. \ } \\ { \left. \left| \mathbf { h } _ { e } ^ { H } [ n ] \mathbf { w } _ { c } [ n ] \right| ^ { 2 } + \left| \mathbf { h } _ { e } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] \right| ^ { 2 } + \sigma _ { e } ^ { 2 } , \quad \mathcal { H } _ { 1 } . \right.} \end{array}   \end{array}\tag{12}
$$

The performance of the hypothesis testing at Eve to minimize the detection error rate $\xi [ n ]$ at time slot n, achieved from two probabilities of false alarm $\mathbb { P } _ { \mathrm { F A } } [ n ] = \operatorname* { P r } \{ { \mathcal { D } } _ { 1 } | { \mathcal { H } } _ { 0 } \}$ , and miss detection $\mathbb { P } _ { \mathrm { M D } } [ n ] = \operatorname* { P r } \{ { \mathcal D } _ { 0 } | { \mathcal H } _ { 1 } \}$ , as follows:

$$
\xi [ n ] = \mathbb { P } _ { \mathrm { F A } } [ n ] + \mathbb { P } _ { \mathrm { M D } } [ n ] , ~ \forall n .\tag{13}
$$

In covert communications with an aerial eavesdropper, Eve aims to minimize the detection error rate under the optimal detection threshold value τ [n] and optimal hovering location l[n]. Therefore, we should first derive the minimum optimal detection error rate $\xi ^ { * } [ n ]$ from Eve’s perspective. Afterward, Alice jointly designs the trajectory and beamforming vectors to obtain the optimal covert rate.

2) The Performance of Error Detection Probability: Based on the average received power at Eve presented in (12), the false alarm and miss detection probabilities of the proposed UAV-assisted covert communication using a beamforming technique in the PD-NOMA system are derived as:

$$
\mathbb { P } _ { \mathrm { F A } } [ n ] = \operatorname* { P r } \{ \left| \mathbf { h } _ { e } ^ { H } [ n ] \mathbf { w } _ { c } [ n ] \right| ^ { 2 } + \sigma _ { e } ^ { 2 } > \tau [ n ] \} ,\tag{14}
$$

$$
\mathbb { P } _ { \mathrm { M D } } [ n ] = \operatorname* { P r } \{ \left| \mathbf { h } _ { e } ^ { H } [ n ] \mathbf { w } _ { c } [ n ] \right| ^ { 2 } + \left| \mathbf { h } _ { e } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] \right| ^ { 2 } + \sigma _ { e } ^ { 2 } < \tau [ n ] \} .\tag{15}
$$

Motivated to guarantee covert communication, we employed a UAV-enabled beamforming design to increase Eve’s uncertainties. Since the beamformer vector’s ${ \bf w } _ { k } [ n ]$ are designed based on the Channel State Information (CSI) of legitimate links, deriving the detection error rate is challenging for Eve. Eve assumes that Alice designs the beamformer for each antenna using $w _ { k , m } [ n ] ~ = ~ w _ { k , m } ^ { r } [ n ] + j w _ { k , m } ^ { i } [ n ]$ where $w _ { k , m } ^ { r } [ n ]$ and $w _ { k , m } ^ { i } [ n ]$ are independent and identically distributed (i.i.d.) with normal distributions, specifically $\begin{array} { r } { w _ { \boldsymbol { k } , m } ^ { r } [ n ] \sim \mathcal { N } \left( \boldsymbol { 0 } , \frac { \sigma _ { \boldsymbol { k } , m } ^ { 2 } } { 2 } \right) } \end{array}$ and $\begin{array} { r } { w _ { k , m } ^ { i } [ n ] \ \sim \ N \left( 0 , \frac { \overline { { \sigma _ { k , m } ^ { 2 } } } } { 2 } \right) } \end{array}$ . In addition, the beamforming vectors ${ \bf w } _ { k } [ n ]$ are independently and jointly with complex Gaussian distributions ${ \bf w } _ { k } [ n ] \ \sim$ ${ \mathcal { C N } } ( \mathbf { 0 } , { \pmb { \Sigma } } )$ , where 0 represents the zero-mean vector, and Σ denotes the covariance matrix as follows:

$$
\pmb { \Sigma } = \left[ \begin{array} { c c c c c } { \sigma _ { k , 1 } ^ { 2 } [ n ] } & { 0 } & { \hdots } & { 0 } \\ { 0 } & { \sigma _ { k , 2 } ^ { 2 } [ n ] } & { \hdots } & { 0 } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { 0 } & { \hdots } & { \sigma _ { k , M } ^ { 2 } [ n ] } \end{array} \right] ,\tag{16}
$$

here, $\begin{array} { r l r } { \sigma _ { k , m } ^ { 2 } [ n ] } & { { } = } & { E \{ | \mathrm { w } _ { k , m } [ n ] | ^ { 2 } \} } \end{array}$ is the variance of $\mathrm { w } _ { k , m } [ n ] , ~ k \in \{ b , c \}$ , $m \in \mathcal { M }$ . Eve characterizes the distribution function of the false alarm and miss detection probabilities by denoting $\alpha _ { k } [ n ]$ as follows:

$$
\alpha _ { k } [ n ] = { \bf h } _ { e } ^ { H } [ n ] { \bf w } _ { k } [ n ] = \sum _ { m = 1 } ^ { M } h _ { e , m } ^ { * } [ n ] { \bf w } _ { k , m } [ n ] , k \in \{ b , c \} ,\tag{17}
$$

where the distribution of $\alpha _ { k } [ n ]$ is analyze in the following lemma.

Theorem 1: The sum of independent normally distributed random variables follows a normal distribution [29].

Lemma 1: Following the Theorem 1, since the m-th element of beamforming vector to k-th user follows a complex normal distribution $\mathrm { w } _ { k , m } ^ { - } [ n ] \sim \mathcal { C N } ( 0 , \sigma _ { k , m } ^ { 2 } [ n ] )$ , the distribution of $\alpha _ { k } [ n ]$ can be determined as $\alpha _ { k } [ n ] \sim \mathcal { C N } ( 0 , \varpi _ { k } [ n ] )$ , where $\begin{array} { r } { \varpi _ { \boldsymbol { k } } \dot { [ n ] } = \sum _ { m = 1 } ^ { M } | h _ { e , m } [ n ] | ^ { 2 } \sigma _ { \boldsymbol { k } , m } ^ { 2 } \dot { [ n ] } } \end{array}$ . In addition, $| \alpha _ { k } [ n ] | ^ { 2 }$ follow an exponential distribution, i.e., $\begin{array} { r } { | \alpha _ { k } [ n ] | ^ { 2 } \sim \exp \left( \frac { 1 } { \varpi _ { k } \left[ n \right] } \right) } \end{array}$

Consequently, based on (14), (17) the false alarm probability $\mathbb { P } _ { \mathrm { F A } } [ n ]$ of the proposed scheme at Eve can be derived as follows:

$$
\begin{array} { r l } & { \mathbb { P } _ { \mathrm { F A } } [ n ] = \operatorname* { P r } \{ \left| \alpha _ { c } [ n ] \right| ^ { 2 } + \sigma _ { e } ^ { 2 } > \tau [ n ] \} , } \\ & { \quad \quad = \left\{ \exp \left( \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \varpi _ { c } [ n ] } \right) , \quad \quad \tau [ n ] > \sigma _ { e } ^ { 2 } , \right. } \\ & { \quad \quad \left. 1 , \quad \quad \tau [ n ] < \sigma _ { e } ^ { 2 } . \right. } \end{array}\tag{18}
$$

The miss detection probability $\mathbb { P } _ { \mathrm { M D } } [ n ]$ at Eve is obtained from (15) and (17), in (19), shown at the bottom of the page.

Therefore, the error detection rate $\xi [ n ]$ is obtained by substituting equations (18) and (19) into equation (13) in equation (20), shown at the bottom of the page.

Proof: The detailed is provided in Appendix A.

## C. Age of Information

In the proposed system, we consider Alice flies to serve Bob and Carol with the PD-NOMA technique. However, Alice faces communication time constraints due to limited onboard UAV energy. On the other hand, in time-sensitive applications, the timeliness of received data is important. Therefore, we leverage the information freshness metrics in the context of covert communication in time-varying channels. The age of information refers to the elapsed time from the received packet by the legitimate users that has been generated at Alice, which is defined as follows:

$$
\Delta _ { k } ( t ) = t - \iota _ { k } ( t ) , \ k \in \{ b , c \} ,\tag{21}
$$

where $\iota _ { k } ( t )$ refers to the time the most recently received packet at the k-th legitimate user, was generated at Alice. For ease of exposition, we assume $\Delta _ { k } ( 0 ) = 0$ . To enhance the AoI, we utilize the first come first served (FCFS) method to update the age status [30]. In FCFS systems, a new packet’s transmission is available exactly at the transmitter when the packet’s update in service finishes at the destination. In this manner, the waiting time for updating the packet is almost near zero which will obtain the smallest age of freshness that aligns with the aim of the proposed system model to minimize the AoI.

## III. PROBLEM FORMULATION AND SOLUTION METHODOLOGY

## A. Problem Formulation

In the context of UAV-assisted covert communication using beamforming in the PD-NOMA scheme, our objective is to minimize the total AoI among all legitimate users. This

$$
\begin{array} { r } { \mathbb { P } _ { \mathrm { M D } } [ n ] = \operatorname* { P r } \{ \left| \alpha _ { c } [ n ] \right| ^ { 2 } + \left| \alpha _ { b } [ n ] \right| ^ { 2 } + \sigma _ { e } ^ { 2 } < \tau [ n ] \} = \left\{ \begin{array} { l l } { \frac { \sigma _ { b } [ n ] \exp \left( \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \omega _ { b } [ n ] } \right) - \sigma _ { c } [ n ] \exp \left( \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \omega _ { c } [ n ] } \right) } { \sigma _ { c } [ n ] - \tau _ { b } [ n ] } + 1 , } & { \tau [ n ] > \sigma _ { e } ^ { 2 } , } \\ { 0 , } & { \tau [ n ] < \sigma _ { e } ^ { 2 } . } \end{array} \right. } \end{array}\tag{19}
$$

$$
\begin{array} { r } { \xi [ n ] = \left\{ \begin{array} { l l } { \frac { \varpi _ { b } [ n ] } { \varpi _ { c } [ n ] - \varpi _ { b } [ n ] } \left[ \exp \left( \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \varpi _ { b } [ n ] } \right) - \exp \left( \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \varpi _ { c } [ n ] } \right) \right] + 1 , } & { \tau [ n ] > \sigma _ { e } ^ { 2 } , } \\ { 1 , } & { \tau [ n ] < \sigma _ { e } ^ { 2 } . } \end{array} \right. } \end{array}\tag{20}
$$

is achieved by jointly optimizing the trajectory of Alice (denoted as ${ \mathbf Q } = \{ { \mathbf q } [ n ] , \forall n \} \mathrm { ) }$ , transmit beamformers (denoted as $\textbf { W } = \{ \mathbf { w } _ { k } [ n ] , \forall k , n \} )$ , and the freshness of information (denoted as $\Delta \ = \ \{ \Delta _ { k } [ n ] , \forall k , n \} \big )$ over all time slots. The jointly optimization problem is formulated as:

$$
\underset { { \mathbf { Q } } , { \mathbf { W } } , { \boldsymbol { \Delta } } } { \operatorname* { m i n } } \sum _ { n = 1 } ^ { N } \sum _ { k \in \{ b , c \} } \Delta _ { k } [ n ]\tag{22a}
$$

$$
\mathrm { s . t . } \sum _ { k \in \{ b , c \} } \Vert \textbf { w } _ { k } [ n ] \Vert ^ { 2 } \leqslant T , \ \forall n ,\tag{22b}
$$

$$
| \mathbf { h } _ { k } ^ { H } [ n ] \mathbf { w } _ { c } [ n ] | ^ { 2 } > | \mathbf { h } _ { k } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] | ^ { 2 } , \ k \in \{ b , c \} , \forall n ,\tag{22c}
$$

$$
\operatorname* { m i n } _ { \tau [ n ] , 1 [ n ] } \xi [ n ] \geqslant 1 - \epsilon , \ \forall n ,\tag{22d}
$$

$$
\operatorname* { m a x } _ { k } \Delta _ { k } [ n ] \leqslant \delta , \ \forall n ,\tag{22e}
$$

$$
\Delta _ { c } [ n ] \times R _ { c } [ n ] \geqslant \frac { S _ { c } [ n ] } { B } , \ \forall n ,\tag{22f}
$$

$$
\sum _ { n = 1 } ^ { N } \left( \Delta _ { b } [ n ] \times R _ { b } [ n ] \right) \geqslant { \frac { S _ { b } } { B } } ,\tag{22g}
$$

$$
\| \mathbf { \nabla } \mathbf { q } [ n + 1 ] - \mathbf { q } [ n ] \ \| \leqslant \operatorname* { m a x } _ { k } \Delta _ { k } [ n ] \times V _ { \operatorname* { m a x } } ,
$$

$$
n = 1 , . . . , N - 1 ,\tag{22h}
$$

where the beamformer vectors ${ \bf w } _ { k } [ n ]$ satisfy (22b), that Γ represents the transmit power of Alice with a uniform distribution, subject to an upper bound of $P _ { \mathrm { m a x } }$ . In (22c), we achieve fairness in the NOMA scheme to jointly improve covertness and AoI. This is realized by allocating more power to Carol and enabling the successful implementation of SIC at Bob [31]. The constraint (22d) ensures that the detection error rate minimization problem is not less than a specific value. Constraint (22e) ensures that the maximum age of packet freshness must be shorter than the duration of each time slot, actually before channel variation. The QoS constraints (22f) and (22g) ensure successful packet transmissions from Alice to Bob and Carol with, minimum required sizes $S _ { b }$ and $S _ { c } [ n ]$ , respectively. B denotes the communication bandwidth link. The constraint (22h) guarantees that the total packet is transmitted within the maximum horizontal flight distance of Alice across all time slots.

Lemma 2: To enhance the tractability of the optimization problem, we initially address the optimization constraint (22d) to determine Eve’s optimal detection threshold $\tau ^ { * } [ n ]$ and optimal location l[n], resulting achieving the minimum detection error rate $\xi ^ { * } [ n ]$

Proof: The details are provided in Appendix B.

In the subsequent sections, leveraging Lemma 2, we employ $\xi ^ { * } [ n ] \geqslant 1 - \epsilon$ instead of (22d) as the covertness constraint in our joint optimization problem.

The joint optimization problem (22) is difficult to solve because the UAV trajectory variables Q, beamforming design variables W, and AoI variables $\pmb { \Delta }$ are strongly coupled in the constraints. Furthermore, the covertness constraint (22d), QoS constraints (22f), and (22g) are non-convex, and complicating the solution process. Therefore, to address the non-convex formulated problem, we decompose the joint optimization problem (22) into three sub-problems: AoI freshness optimization, Alice trajectory design, and beamforming design optimization. Subsequently, we developed an efficient alternative optimization algorithm by adopting successive convex (SC) optimization techniques.

## B. Solution Methodology

1) AoI Optimization: To obtain the optimal AoI freshness from optimization problem (22) for a given UAV trajectory design and transmit beamformers {Q, W}, we solve the following optimization problem:

$$
\operatorname* { m i n } _ { \Delta } \ \sum _ { n = 1 } ^ { N } \sum _ { k \in \{ b , c \} } \Delta _ { k } [ n ]\tag{23a}
$$

$$
\mathrm { s . t . } \operatorname* { m a x } _ { k } \Delta _ { k } [ n ] \leqslant \delta , \forall n ,\tag{23b}
$$

$$
\Delta _ { c } [ n ] \times R _ { c } [ n ] \geqslant \frac { S _ { c } [ n ] } { B } , \ \forall n ,\tag{23c}
$$

$$
\sum _ { n = 1 } ^ { N } \left( \Delta _ { b } [ n ] \times R _ { b } [ n ] \right) \geqslant { \frac { S _ { b } } { B } } ,\tag{23d}
$$

$$
\parallel \mathbf { q } [ n + 1 ] - \mathbf { q } [ n ] \parallel \leqslant \operatorname* { m a x } _ { k } \Delta _ { k } [ n ] \times V _ { \operatorname* { m a x } } ,\tag{23e}
$$

since problem (23) and its constraints are in standard linear programming (LP) form, it can be efficiently solved using existing optimization tools like CVX [32].

2) Trajectory Design Optimization: The optimal UAV trajectory design for a specified AoI freshness, and transmit beamformers {∆, W} can be obtained by solving the following optimization problem:

$$
\operatorname* { m i n } _ { \mathbf { Q } } \sum _ { n = 1 } ^ { N } \sum _ { k \in \{ b , c \} } \Delta _ { k } [ n ]\tag{24a}
$$

$$
\mathrm { s . t . } ~ \Delta _ { c } [ n ] \times R _ { c } [ n ] \geqslant \frac { S _ { c } [ n ] } { B } , ~ \forall n ,\tag{24b}
$$

$$
\sum _ { n = 1 } ^ { N } \left( \Delta _ { b } [ n ] \times R _ { b } [ n ] \right) \geqslant { \frac { S _ { b } } { B } } ,\tag{24c}
$$

$$
\begin{array} { r } { \| \mathbf { \delta q } [ n + 1 ] - \mathbf { q } [ n ] \| \leqslant \operatorname* { m a x } _ { k } [ n ] \times V _ { \operatorname* { m a x } } , } \\ { n = 1 , . . . , N - 1 , } \end{array}\tag{24d}
$$

where (24) is a non-convex optimization problem due to the non-convex constraints (24b) and (24c). Accordingly, we adopt a successive convex approximation (SCA) approach to iteratively determine the optimal trajectory design of Alice. On the other hand, to enhance the signal energy and improve the achievable rate, the phase angles $\theta$ of all beamformer vectors can be jointly adjusted to achieve phase alignment of signals from different transmission paths at legitimate users. Therefore, we express the $\mathbf { h } _ { b } ^ { H } [ n ] \mathbf { w } _ { b } [ n ]$ at formulation (25), shown at the bottom of the next page.

Hence, the following upper bound is provided for the term $| \mathbf { h } _ { b } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] |$ :

$$
| \mathbf { h } _ { b } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] | \leqslant { \frac { \sqrt { \mu _ { 0 } } } { d _ { b } [ n ] } } \sum _ { m = 1 } ^ { M } | \mathbf { w } _ { b } ^ { m } [ n ] | .\tag{26}
$$

Consequently, the term $| \mathbf { h } _ { b } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] | ^ { 2 }$ , has the following upper bound:

$$
| \mathbf h _ { b } ^ { H } [ n ] \mathbf w _ { b } [ n ] | ^ { 2 } \leqslant \frac { \mu _ { 0 } z _ { b } [ n ] } { d _ { b } ^ { 2 } [ n ] } ,\tag{27}
$$

where $\begin{array} { r } { z _ { k } [ n ] = \left( \sum _ { m = 1 } ^ { M } | \mathrm { w } _ { k } ^ { m } [ n ] | \right) ^ { 2 } , \ k \in \{ b , c \} } \end{array}$ . Similarly, for $| { \bf h } _ { c } ^ { H } [ n ] { \bf w } _ { k } [ n ] | ^ { 2 }$ , we express the upper bound as follow:

$$
| \mathbf { h } _ { c } ^ { H } [ n ] \mathbf { w } _ { k } [ n ] | ^ { 2 } \leqslant { \frac { \mu _ { 0 } z _ { k } [ n ] } { d _ { c } ^ { 2 } [ n ] } } , \ k \in \{ b , c \} .\tag{28}
$$

Therefore, the achievable data rate at legitimate users are:

$$
\hat { R } _ { b } [ n ] = \log _ { 2 } \left( 1 + \frac { \eta z _ { b } [ n ] } { j _ { b } [ n ] + H ^ { 2 } } \right) ,\tag{29}
$$

$$
\hat { R } _ { c } [ n ] = \log _ { 2 } \left( 1 + \frac { \eta z _ { c } [ n ] } { \eta z _ { b } [ n ] + j _ { c } [ n ] + H ^ { 2 } } \right) ,\tag{30}
$$

where $\eta ~ = ~ \mu _ { 0 } / \sigma ^ { 2 }$ , and inequality $j _ { k } [ n ] \ \leqslant \lVert \ \mathbf { q } [ n ] - \mathbf { u } _ { k } \ \rVert ^ { 2 }$ ， $k \in \{ b , c \}$ are facilitate the derivation of upper bound for the concave data rate function through its first-order Taylor expansion at any point:

$$
\breve { R } _ { b } [ n ] = \log _ { 2 } { \left( \eta z _ { b } [ n ] + j _ { b } [ n ] + H ^ { 2 } \right) } - \log _ { 2 } { \left( j _ { b } ^ { \varsigma } [ n ] + H ^ { 2 } \right) }
$$

$$
- \frac { \log _ { 2 } ( e ) } { j _ { b } ^ { \varsigma } [ n ] + H ^ { 2 } } \left( j _ { b } [ n ] - j _ { b } ^ { \varsigma } [ n ] \right) ,\tag{31}
$$

$$
\begin{array} { l } { \check { R } _ { c } [ n ] = \log _ { 2 } \left( \eta ( z _ { b } [ n ] + z _ { c } [ n ] ) + j _ { c } [ n ] + H ^ { 2 } \right) } \\ { \qquad - \log _ { 2 } \left( \eta z _ { b } [ n ] + j _ { c } ^ { \varsigma } [ n ] + H ^ { 2 } \right) } \\ { \qquad - \displaystyle \frac { \log _ { 2 } ( e ) } { \eta z _ { b } [ n ] + j _ { c } ^ { \varsigma } [ n ] + H ^ { 2 } } \left( j _ { c } [ n ] - j _ { c } ^ { \varsigma } [ n ] \right) . } \end{array}\tag{32}
$$

Since, $j _ { k } [ n ]$ is a slack variable, we have the following inequality by applying the first-order Taylor expansion at the given point $q ^ { S } [ n ]$ for ς-th iteration:

$$
\begin{array} { r } { j _ { k } [ n ] \leqslant \parallel q ^ { \varsigma } [ n ] - \mathbf { u } _ { k } \parallel ^ { 2 } + 2 ( q ^ { \varsigma } [ n ] - \mathbf { u } _ { k } ) ^ { T } ( \mathbf { q } [ n ] - q ^ { \varsigma } [ n ] ) , } \\ { k \in \{ b , c \} , \ \forall n . \qquad ( 3 ) } \end{array}\tag{3}
$$

Consequently, the non-convex optimization problem (24) is replaced with the following convex optimization problem:

$$
\underset { \mathbf { Q } } { \operatorname* { m i n } } \sum _ { n = 1 } ^ { N } \sum _ { k \in \{ b , c \} } \Delta _ { k } [ n ]\tag{34a}
$$

$$
\mathrm { s . t . } ~ \Delta _ { c } [ n ] \times \check { R } _ { c } [ n ] \geqslant \frac { S _ { c } [ n ] } { B } , ~ \forall n ,\tag{34b}
$$

$$
\sum _ { n = 1 } ^ { N } \left( \Delta _ { b } [ n ] \times \check { R } _ { b } [ n ] \right) \geqslant \frac { S _ { b } } { B } ,\tag{34c}
$$

$$
( 2 4 \mathrm { d } ) , ( 3 3 ) .\tag{34d}
$$

Problem (34) is a convex optimization problem that can be effectively solved using standard solvers like CVX [32].

3) Beamforming Optimization: For any given AoI data freshness and as well as UAV trajectory design $\{ \Delta , \mathbf { Q } \}$ , the transmit beamformers of problem (22) can be optimized by solving the following problem:

$$
\operatorname* { m i n } _ { \mathbf { W } } \sum _ { n = 1 } ^ { N } \sum _ { k \in \{ b , c \} } \Delta _ { k } [ n ]\tag{35a}
$$

$$
\mathrm { s . t . } \sum _ { k \in \{ b , c \} } \Vert \textbf { w } _ { k } [ n ] \Vert ^ { 2 } \leqslant T , \ \forall n ,\tag{35b}
$$

$$
| \mathbf { h } _ { k } ^ { H } [ n ] \mathbf { w } _ { c } [ n ] | ^ { 2 } > | \mathbf { h } _ { k } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] | ^ { 2 } , \ k \in \{ b , c \} , \forall n ,\tag{35c}
$$

$$
\xi ^ { * } [ n ] \geqslant 1 - \epsilon , \ \forall n ,\tag{35d}
$$

$$
\Delta _ { c } [ n ] \times R _ { c } [ n ] \geqslant \frac { S _ { c } [ n ] } { B } , \ \forall n ,\tag{35e}
$$

$$
\sum _ { n = 1 } ^ { N } \left( \Delta _ { b } [ n ] \times R _ { b } [ n ] \right) \geqslant { \frac { S _ { b } } { B } } .\tag{35f}
$$

While the objective function (35) and the constraints (35b) and (35c) are convex, it is challenging to achieve the optimal transmit beamformers due to the coupling in nonconvex constraints (35d), (35e), and (35f). We apply the semidefinite relaxation (SDR) and SCA alternating optimization techniques to solve the problem, respectively. Let we define ${ \bf H } _ { k } [ \bar { n } ] = { \bf h } _ { k } [ n ] { \bf h } _ { k } ^ { H } [ n ]$ , and $\mathbf { W } _ { k } [ n ] \bar { \mathbf { \Psi } } = \mathbf { \warrow } \mathbf { w } _ { k } [ n ] \mathbf { w } _ { k } ^ { H } [ n ]$ where ${ \bf W } _ { k } [ n ] ~ \succeq ~ 0$ and rank $( \mathbf { W } _ { k } [ n ] ) ~ = ~ 1 , ~ k ~ \in ~ \{ b , c \}$ In addition, $p _ { k } [ n ] ~ = ~ \mathrm { T r } ( { \bf W } _ { k } [ n ] )$ , and $\begin{array} { r l } { | { \bf h } _ { k } ^ { H } [ n ] { \bf w } _ { k } [ n ] | ^ { 2 } } & { { } = } \end{array}$ $\mathrm { T r } \left( \mathbf { H } _ { k } [ n ] \mathbf { W } _ { k } [ n ] \right)$ . Accordingly, problem (35) is reformulated as:

$$
\operatorname* { m i n } _ { \mathbf { W } } \sum _ { n = 1 } ^ { N } \sum _ { k \in \{ b , c \} } \Delta _ { k } [ n ]\tag{36a}
$$

$$
\mathrm { s . t . } \sum _ { k \in \{ b , c \} } p _ { k } [ n ] \leqslant T , \forall n ,\tag{36b}
$$

$$
\mathrm { T r } \left( \mathbf { H } _ { k } [ n ] \mathbf { W } _ { c } [ n ] \right)
$$

$$
\begin{array} { r } { \geqslant \mathrm { T r } \left( \mathbf { H } _ { k } [ n ] \mathbf { W } _ { b } [ n ] \right) , \ k \in \{ b , c \} , \quad \forall n , } \end{array}\tag{36c}
$$

$$
\Upsilon \left( p _ { b } [ n ] , p _ { c } [ n ] \right) \leqslant \epsilon , \forall n ,\tag{36d}
$$

$$
\frac { 1 } { f _ { k } [ n ] } \leqslant \mathrm { T r } \left( \mathbf { H } _ { k } [ n ] \mathbf { W } _ { k } [ n ] \right) , k \in \{ b , c \} , \forall n ,\tag{36e}
$$

$$
g _ { k } [ n ] \geqslant \sum _ { \Omega ( k ^ { \prime } ) > \Omega ( k ) } \mathrm { T r } ( \mathbf H _ { k } [ n ] \mathbf W _ { k ^ { \prime } } [ n ] ) + \sigma _ { k } ^ { 2 } ,
$$

$$
k , k ^ { \prime } \in \{ b , c \} , \ \forall n ,\tag{36f}
$$

$$
\Delta _ { c } [ n ] \times \log _ { 2 } \left( 1 + \frac { 1 } { f _ { c } [ n ] g _ { c } [ n ] } \right) \geqslant \frac { S _ { c } [ n ] } { B } , \ \forall n ,\tag{36g}
$$

$$
\sum _ { n = 1 } ^ { N } \bigg ( \Delta _ { b } [ n ] \times \log _ { 2 } \bigg ( 1 + \frac { 1 } { f _ { b } [ n ] g _ { b } [ n ] } \bigg ) \bigg ) \geqslant \frac { S _ { b } } { B } ,\tag{36h}
$$

$$
\mathbf { W } _ { k } [ n ] \succeq 0 , ~ k \in \{ b , c \} , ~ \forall n ,
$$

$$
\mathrm { r a n k } \left( \mathbf { W } _ { k } [ n ] \right) = 1 , \ k \in \{ b , c \} , \ \forall n ,\tag{36i}
$$

(36j)

$$
\begin{array} { r } { \mathbf { h } _ { b } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] = \frac { \sqrt { \mu _ { 0 } } \sum _ { m = 1 } ^ { M } \big | \mathbf { w } _ { b } ^ { m } \big [ n \big ] \big | e ^ { j \left( \frac { 2 ( m - 1 ) \pi d } { \lambda } \sin ( \theta ( \mathbf { q } [ n ] , \mathbf { u } _ { b } ) ) + \mathcal { L } \mathbf { w } _ { b } ^ { m } [ n ] \right) } } { d _ { b } \big [ n \big ] } . } \end{array}\tag{25}
$$

where Υ(p<sub>b</sub>[n], p<sub>c</sub>[n]) p<sub>b</sub>[n] × p<sub>c</sub>[n]−p<sub>b</sub>[n] $\begin{array} { r } { \left[ \left( \frac { p _ { c } \left[ n \right] } { p _ { b } \left[ n \right] } \right) ^ { \frac { p _ { b } \left[ n \right] } { p _ { b } \left[ n \right] - p _ { c } \left[ n \right] } } - \left( \frac { p _ { c } \left[ n \right] } { p _ { b } \left[ n \right] } \right) ^ { \frac { p _ { c } \left[ n \right] } { p _ { b } \left[ n \right] - p _ { c } \left[ n \right] } } \right] } \end{array}$ , and Ω(k) specifies the decoding order for user k, where $\bar { \Omega ( k ^ { \prime } ) } > \Omega ( k )$ indicates that user k has a smaller order and therefore detects its signal earlier. Therefore, based on the proposed system model, $| { \bf h } _ { b } [ n ] | > | { \bf h } _ { c } [ n ] |$ |. Based on the non-convex constraints (36d), $( 3 6 \mathrm { g } ) , ~ ( 3 6 \mathrm { h } )$ , and (36j), the problem (36) is a non-convex. Hence, by applying the first-order Taylor expansion to $\Upsilon ( p _ { b } [ n ] , p _ { c } [ n ] )$ at the given points $p _ { b } ^ { \iota } [ n ]$ , and $p _ { c } ^ { \iota } [ n ]$ in the ι-th iteration, the optimal solution is obtained at (37)-(39), shown at the bottom of the page.

$$
\Upsilon ( p _ { b } ^ { \iota } [ n ] , p _ { c } ^ { \iota } [ n ] ) + \sum _ { k \in \{ b , c \} } \left( \frac { \partial \Upsilon ( p _ { b } ^ { \iota } [ n ] , p _ { c } ^ { \iota } [ n ] ) } { \partial p _ { k } ^ { \iota } [ n ] } \right) \times ( p _ { k } [ n ] - p _ { k } ^ { \iota } [ n ] ) \leqslant \epsilon\tag{37}
$$

However, the constraints (36g) and (36h) still lead to nonconvexity of problem formulation (36). With respect to x and y, for $x > 0$ , and $\begin{array} { r } { y > 0 , f ( x , y ) = \log \left( 1 + \frac { 1 } { x y } \right) } \end{array}$ is a joint convex function [33]. Therefore, term log $\begin{array} { r } { \mathrm { \Omega } _ { \mathrm { ~ > 2 } } \left( 1 + \frac { 1 } { f _ { k } \left[ n \right] g _ { k } \left[ n \right] } \right) } \end{array}$ is joint convex function over $f _ { k } [ n ]$ , and $g _ { k } [ n ]$ . Hence, the firstorder Taylor expansion can be used to linearly approximate an upper bound at given local points $f _ { k } ^ { \iota } [ n ]$ , and $g _ { k } ^ { \iota } [ n ]$ to generate a tighter convex substitute:

$$
\begin{array} { r l r } {  { \log _ { 2 } ( 1 + \frac { 1 } { f _ { k } [ n ] g _ { k } [ n ] } ) \geqslant \log _ { 2 } ( 1 + \frac { 1 } { f _ { k } ^ { \iota } [ n ] g _ { k } ^ { \iota } [ n ] } ) } } \\ & { } & { \quad - \frac { \log _ { 2 } ( e ) ( f _ { k } [ n ] - f _ { k } ^ { \iota } [ n ] ) } { f _ { k } ^ { \iota } [ n ] ( 1 + f _ { k } ^ { \iota } [ n ] g _ { k } ^ { \iota } [ n ] ) } - \frac { \log _ { 2 } ( e ) ( g _ { k } [ n ] - g _ { k } ^ { \iota } [ n ] ) } { g _ { k } ^ { \iota } [ n ] ( 1 + f _ { k } ^ { \iota } [ n ] g _ { k } ^ { \iota } [ n ] ) } , } \\ & { } & { \quad = \tilde { R } _ { k } [ n ] , \ k \in \{ b , c \} , \ \forall n . } \end{array}\tag{40}
$$

Then, the optimization problem (36) can be reformulated as follows:

$$
\operatorname* { m i n } _ { \mathbf { W } } \sum _ { n = 1 } ^ { N } \sum _ { k \in \{ b , c \} } \Delta _ { k } [ n ]\tag{41a}
$$

$$
\mathrm { s . t . } ~ \Delta _ { c } [ n ] \times \tilde { R } _ { c } [ n ] \geqslant \frac { S _ { c } [ n ] } { B } , ~ \forall n ,\tag{41b}
$$

$$
\sum _ { n = 1 } ^ { N } \Big ( \Delta _ { b } [ n ] \times \tilde { R } _ { b } [ n ] \Big ) \geqslant \frac { S _ { b } } { B } ,\tag{41c}
$$

$$
( 3 6 \mathrm { b } ) , ( 3 6 \mathrm { c } ) , ( 3 6 \mathrm { e } ) , ( 3 6 \mathrm { f } ) , ( 3 6 \mathrm { i } ) , ( 3 6 \mathrm { j } ) , ( 3 7 ) .\tag{41d}
$$

Nevertheless, problem (41) remains non-convex due to the non-convex rank-one constraint (36j). Therefore, the following theorem is leveraged to address this challenge.

Theorem 2: The optimal transmit beamformer vector is derived from problem (41) without the rank-one constraint (36j) by always satisfying rank $( \mathbf { W } _ { k } [ n ] ) = 1 , \ k \in \{ b , c \}$ , ∀n.

Proof: The details are reported in Appendix C.

According to Theorem 2, a rank-one solution can always be obtained by solving (41) while disregarding the rank-one constraint (36j). Consequently, the formulation presented in (41) qualifies as a convex semidefinite program (SDP) that can be effectively tackled with standard convex optimization tools, such as CVX [32].

## Complexity Analysis

The joint proposed optimization problem is difficult to solve because the UAV trajectory variables, beamforming design variables, and AoI variables are strongly coupled with each other. Therefore, to address the non-convex formulated prob lem, we decompose the joint optimization problem into three sub-problems: AoI freshness optimization, Alice trajectory design, and beamforming design optimization. It is observed that the complexity of the jointly optimized problem mainly depends on that of the three proposed sub-problems. Therefore, we first analyze the complexity of three sub-problems and then calculate the total complexity:

• The complexity of the AoI optimization, which is in standard linear programming (LP) form, is

$$
O _ { \mathrm { A o I } } \triangleq \mathcal { O } \left( 2 N \log \left( \frac { 1 } { \mu } \right) \right)
$$

where N is the number of multiplications, and $\mu$ is the stopping criterion.

• The complexity of the trajectory design optimization is

$$
O _ { \mathrm { T D } } \triangleq \mathcal { O } \left( T _ { \mathrm { T D } } \frac { \log \left( \frac { x } { \tau \mu } \right) } { \log ( \xi _ { 0 } ) } \right)
$$

where $T _ { \mathrm { T D } }$ is the number of iterations for sub-problem trajectory design optimization, and $x = 4 N$ is the total number of constraints of the proposed sub-problem, τ is the initial point for approximation of the accuracy of the interior point method, and $\xi _ { 0 }$ is the updating accuracy.

• The complexity of the beamforming optimization is the

$$
O _ { \mathrm { B F } } \triangleq \mathcal { O } \left( T _ { \mathrm { B F } } \operatorname* { m a x } \left( M , 2 K + 1 \right) ^ { 4 } \sqrt { M } \log _ { 2 } \left( \frac { 1 } { \mu } \right) \right) ,
$$

where $T _ { \mathrm { B F } }$ is the number of iterations for sub-problem beamforming optimization, M is the number of antennas. Also, $k \in \mathcal { K } = \{ b , c \}$ and $K = | { \cal { K } } |$ is the number of user. $\xi _ { 1 }$ is the updating accuracy, too.

$$
\begin{array} { r l } & { \frac { \partial \Upsilon ( p _ { b } ^ { \varepsilon } [ n ] , p _ { c } ^ { \varepsilon } [ n ] ) } { \partial p _ { b } ^ { \varepsilon } [ n ] } = \frac { p _ { c } ^ { \varepsilon } [ n ] } { ( p _ { c } ^ { \varepsilon } [ n ] - p _ { b } ^ { \varepsilon } [ n ] ) ^ { 2 } } \times [ ( \frac { p _ { c } ^ { \varepsilon } [ n ] } { p _ { b } ^ { \varepsilon } [ n ] } ) ^ { \frac { p _ { b } ^ { \varepsilon } [ n ] } { p _ { b } ^ { \varepsilon } [ n ] - p _ { c } ^ { \varepsilon } [ n ] } } - ( 1 + \ln ( \frac { p _ { c } ^ { \varepsilon } [ n ] } { p _ { b } [ n ] ^ { \varepsilon } } ) ) ( \frac { p _ { c } ^ { \varepsilon } [ n ] } { p _ { b } ^ { \varepsilon } [ n ] } ) ^ { \frac { p _ { b } ^ { \varepsilon } [ n ] } { p _ { b } ^ { \varepsilon } [ n ] - p _ { c } ^ { \varepsilon } [ n ] } } ] , } \\ &  \frac { \partial \Upsilon ( p _ { b } ^ { \varepsilon } [ n ] , p _ { c } ^ { \varepsilon } [ n ] ) } { \partial p _ { c } ^ { \varepsilon } [ n ] } = \frac { - p _ { b } ^ { \varepsilon } [ n ] } { ( p _ { c } ^ { \varepsilon } [ n ] - p _ { b } ^ { \varepsilon } [ n ] ) ^ { 2 } } \times [ ( \frac { p _ { c } ^ { \varepsilon } [ n ] } { p _ { b } ^ { \varepsilon } [ n ] } ) ^ { \frac { p _ { b } ^ { \varepsilon } [ n ] } { p _ { b } ^ { \varepsilon } [ n ] - p _ { c } ^ { \varepsilon } [ n ] } } - ( 1 + \ln ( \frac { p _ { c } ^ { \varepsilon } [ n ] } { p _ { b } ^ { \varepsilon } [ n ] } ) ) ( \frac { p _ { c } ^ { \varepsilon } [ n ] } { p _ { b } ^ { \varepsilon } [ n ] } ) ^  \frac { p _ { c } ^ { \varepsilon } [ n ] }  p _ { b } ^ { \varepsilon } [ n ] - p  \end{array}\tag{38}
$$

(39)

![](images/4575fd330f4dd326fdf48d175f6fd2fb6e7679887928a30c22494b714d86ac20.jpg)  
Fig. 2. The achievable rate versus the number of antennas. The study considers three cases: $\Gamma = 1 0 , \Gamma = 2 0 .$ , and $\Gamma = 3 0 .$

Consequently, the total complexity of the proposed optimization problem is

$$
O _ { \mathrm { T o t a l } } \triangleq \mathcal { O } \left( T _ { i } \left( O _ { \mathrm { A o I } } + O _ { \mathrm { T D } } + O _ { \mathrm { B F } } \right) \right)
$$

where $T _ { i }$ is the iteration number.

## IV. NUMERICAL RESULTS

The numerical results demonstrate the potential performance of UAV-assisted covert communication using a beamforming technique within a PD-NOMA framework, even in the presence of an aerial eavesdropper. To ensure covert communication, Alice continuously serves Carol while providing service to Bob during desirable time slots. Bob and Carol are uniformly and randomly distributed in the 2D area of $1 \times 1 ~ \mathrm { k m ^ { 2 } }$ . Alice is equipped with $M = 1 0$ antennas and flies at a fixed altitude of $H = 1 0 0$ m with the maximum speed of $V _ { \mathrm { m a x } } = 3 0$ m/s. The minimum required packet sizes for Bob and Carol are set to $S _ { b } = 4 5$ Mbit, and $S _ { c } [ n ] = 5$ Mbit, respectively. The channel power gain is characterized by $\mu _ { 0 } ~ = ~ - 3 0$ dB. The noise power for legal and illegal receivers is given as $\sigma _ { k } ^ { 2 } ~ = ~ \sigma _ { e } ^ { 2 ^ { \scriptstyle - } } = ~ - 1 0 0 ~ \mathrm { d } \bar { \bf B } , ~ k ~ \in ~ \{ b , \bar { c } \}$ The antenna spacing is set as half of a wavelength. Other parameters include $B = 1 ~ \mathrm { M H z } ,$ , κ = 3 dB, $\lambda _ { 0 } = 0 . 1$ m, and $d _ { \operatorname* { m i n } } = 2 5 \mathrm { ~ m ~ }$

## A. Impact of the Number of Alice Antennas

The achievable rates versus the different numbers of antennas M are represented in Fig. 2. As shown for a given M , Carol’s achievable rate is more than Bob which ensures covert communication due to the following reasons: 1) Alice serves Carol in all time slots while she transmits to Bob in desirable time slots, 2) Alice employs a superposition coding strategy for covert and public signals using the PD-NOMA technique with fairness constraint. Furthermore, increasing the antennas leads to improving the corresponding achievable data rate. On the other hand, the achievable rate for Carol and Bob increases as the transmit power of Alice Γ increases.

The illustration of total AoI versus the number of antennas M is shown in Fig. 3. By employing beamforming techniques, Alice can enhance channel capacity and freshly transmit packets. On the other hand, the constraints (22f) and (22g)

![](images/f819d0ecb46eff358bce7397606ee45c34a3ec263a80b813464ba0323eebd48a.jpg)

Fig. 3. The total AoI of users versus the number of antennas. The stud considers three cases: $\Gamma = 1 0 , \Gamma = 2 0 ,$ and $\Gamma = 3 0$  
![](images/39fb5d688b9417f76a5f98e1035e7347117ecf901625877c5e2413209fb236cd.jpg)  
Fig. 4. The achievable covert rate versus  for different transmit power of Alice Γ.

represent the relation between the achievable data rate and the AoI for Bob and Carol for specific packet sizes. Since increasing the number of antennas increases the achievable rate, user’s AoI improves, too. In addition, a higher power budget corresponds to a lower AoI, too.

## B. Impact of the Different Covertness Requirements Level

Fig. 4. demonstrates the achievable covert rate versus different covertness requirements (22d). According to constraint (22d), by increasing , Eve’s detection error rate decreases. Therefore, Alice can allocate more power to Bob while maintaining covert transmission and improving the $R _ { b }$ . Furthermore, an increase in Alice’s power budget improves Bob’s performance.

The impact of covertness requirements  on the total AoI is studied in Fig. 5. As  increases, the achievable covert rate increases, while the achievable public rate decreases. Based on constraints (22f) and (22g), there is an inverse relevance between the achievable rate and the AoI for specific packet sizes. Consequently, since the achievable public rate is dominant, a reduction in Carol’s rate increases the total AoI. Furthermore, increasing the power budget from Γ = 10 w to $\Gamma = 3 0$ w enables Alice to allocate additional power resources to Carol and Bob, thereby improving the users’ AoI.

## C. Impact of the Different Covert Packet Size

To ensure covert communication, Alice continuously serves Carol while dividing the covert packet into nats [20] and serving Bob in desirable time slots that meet the constraints, such as covertness and QoS. Therefore, by increasing $S _ { b }$ the number of allocated time slots to serve Bob increases, too. As depicted in Fig. 6, the blue part represents the number of time slots in which Alice serves only Carol, while the red part indicates the number of time slots during which Alice serves both users by adopting the PD-NOMA technique. As a result by increasing $S _ { b }$ , the average minimum detection error rate $\xi ^ { * }$ increases, too.

![](images/bedfb7232894765f382540e371b526075479c5160373582e3c8043ae03033bc1.jpg)  
Fig. 5. The total AoI versus  for different transmit power of Alice Γ.

![](images/76a886e2a495dfd02f18fa381b56558e62922b60dbeac349c912f6a7297d51af.jpg)

Fig. 6. An analysis of time slots for different covert packet size $S _ { b } .$  
![](images/f3d0f812430c4bbcb2803b9ba0244499ed2a36d519a4119de358354a50e736f6.jpg)  
Fig. 7. The average detection error rate $\xi ^ { * }$ for different covert packet size S<sub>b</sub>.

We evaluate the covertness communication in the UAVassisted proposed system in Fig. 7. With considering constraint (22d), Alice jointly trajectory and beamforming design to minimize the user’s AoI while ensuring covert communication. In the absence of constraint (22d), Alice employs a similar strategy regardless of Eve’s presence. Consequently, this may enable Eve to detect the covert transmission, resulting in the average of $\xi ^ { * }$ exceeding the guard line.

![](images/787fd38676a3c518868a29f81b88e31552828a6f09f3267b7a340e77f652d314.jpg)  
Fig. 8. The Achievable rate for different covert packet size $S _ { b }$

We investigate the impact of covert packet size on the achievable covert rate in Fig. 8 and compare the performance of the proposed PD-NOMA system against orthogonal multiple access (OMA) as a benchmark. In the PD-NOMA framework, we consider two scenarios: one with the constraint (22d) and one without it. In the absence of (22d), Alice is more flexible in her transmission strategy. Therefore, the achievable rate in this scenario is slightly higher than when applying (22d). This marginal increase indicates that our resources have not been wasted by integrating covert communication into UAV-assisted networks while the covertness is guaranteed. The OMA technique assigns each time slot exclusively to Carol or Bob. Hence, increasing the packet size $S _ { b }$ leads to Alice serving Bob in more time slots, and Carol’s rate is not achievable. Therefore, the OMA depicts a decreasing achievable rate compared to the PD-NOMA scenarios. Consequently, the achievable rate for OMA decreases compared to the PD-NOMA scenarios [34].

As mentioned above, increasing the covert packet size causes an increase in the number of time slots that Alice serves Bob. Consequently, the total AoI for users employing the PD-NOMA technique also increases. The PD-NOMA with constraint (22d) limits the achievable rate and leads to a higher AoI compared to the PD-NOMA technique without (22d). Conversely, when utilizing the OMA technique, whereby Alice transmits data to Carol or Bob in an orthogonal manner, the total AoI decreases in this case. The obtained results are demonstrated in Fig. 9.

## D. Impact of the Covert Parameters on the Trajectory Design

We present Fig. 10 to demonstrate that covertness is guaranteed from the perspective of an aerial Eve even through Alice’s flying path for different covert packet sizes such as $S _ { b } = 2 5$ and $S _ { b } = 8 5$ Mbit. Due to the dominant time slots that Alice serves only Carol, the designed paths for the different covert packet sizes are mostly similar. However, an insignificant difference arises from the time slots in which Alice jointly serves Carol and Bob using the PD-NOMA technique. The upper and lower boxes illustrate the area and stopping points where Alice serves Bob for a given minimum required packet sizes, for example with $S _ { b } = 8 5$ Mbit it takes 10-time slots, while the lower box displays for $S _ { b } = 2 5$ Mbit it takes 3-time slots. The achievable covert rate for larger packets is higher.

![](images/91d8c7addbb5f70aa116b3cdc85e35dfe78bff1e11c41b3a979ca4e9629ee99c.jpg)  
Fig. 9. Total AoI for different covert packet size $S _ { b }$

![](images/4015500dd3b043fd139845e33c97c2e2d84a8b2b3b37f2666c1031db7ac6b16c.jpg)  
Fig. 10. Trajectory design for different covert packet size $S _ { b } .$

![](images/7788be018890f2552644bb1bf014c60aa12f786ba312e096aa073a85d3b0cf68.jpg)  
Fig. 11. Achievable covert rate versus  with different flying paths.

In this study, we illustrate the achievable covert rate and the total AoI versus the covertness requirement for the following schemes: 1) Trajectory Design Path: is obtained by the proposed solution; 2) Assumption path: is obtained by the straight line connecting the initial and final points, 3) Randomly Path: is obtained by the random determination of Alice’s location.

In Fig. 11, increasing  results in a smaller lower bound for the covertness constraint (22d). This enables Alice to serve Bob with less limitation and increases the achievable covert rate $R _ { b }$ for all three schemes. In the trajectory design path scheme, Alice optimally flies closer to Bob, which results in a higher $R _ { b }$

![](images/6739e8cc2a93ba4b12bf85f625dcc2dfcab84ae7c1f66c4db022be4ad36a5b97.jpg)  
Fig. 12. Total AoI versus  with different flying paths.

In Fig. 12, similar to Fig. 5, an increase in  results in a smooth rise in the total AoI. This simulation result aligns with the theoretical analysis that reveals an inverse relationship between the achievable rate and AoI for a given packet size. Consequently, the trajectory design path scheme achieves a lower total AoI which is more desirable.

## E. Impact of the Communication Channels Model

The unique characteristics of the A2G link, including a high probability of the LoS, dynamic node mobility, and susceptibility to shadowing and atmospheric effects, pose a fundamental research challenge in selecting an appropriate fading model. The $\lambda - \kappa - \mu$ distribution, as introduced in [35], [36], effectively models the fading behavior of multipath cluster signals with correlated in-phase and quadrature components under LoS conditions. It is particularly advantageous for characterizing channels in low-altitude UAV links. In addition, to the best of our knowledge and following 3GPP releases, UAV, attributed to their individual feature such as high mobility and altitude capabilities, establish LoS links with more than 99% probability when operating at altitudes above 100 meters within urban macro scenarios [7]. Nonetheless, we further investigate the impact of a hybrid communication model that considers both LoS and non-line-of-sight (NLoS) links as a Rician channel model to address our optimization problem more comprehensively.

The communication links from Alice to the legitimate receivers include both LoS and NLoS components, as a Rician block fading model can be given as:

$$
\begin{array} { l } { { \displaystyle { \bf h } _ { k } [ n ] = \sqrt { \mu _ { 0 } d _ { k } ^ { - 2 } [ n ] } } } \\ { { \displaystyle ~ \times \left( \sqrt { \frac { \kappa } { \kappa + 1 } } { \bf a } ( { \bf q } [ n ] , { \bf u } _ { k } ) + \sqrt { \frac { 1 } { \kappa + 1 } } \tilde { \bf a } ( { \bf q } [ n ] , { \bf u } _ { k } ) \right) , } } \end{array}\tag{42}
$$

where κ denotes the Rician factor. The NLoS component $\tilde { \mathbf { a } } ( \mathbf { q } [ n ] , \mathbf { u } _ { k } ) \in \mathbb { C } ^ { M \times 1 }$ is modeled as complex Gaussian distributed with zero mean and unit variance, i.e., $\tilde { \mathbf { a } } ( \mathbf { q } [ n ] , \mathbf { u } _ { k } ) \sim$ $\mathcal { C N } ( \mathbf { 0 } , \mathbf { I } )$ . and, we express the $\mathbf { h } _ { b } ^ { H } [ n ] \mathbf { w } _ { b } [ n ]$ in Racian channel model, as (43), shown at the bottom of the next page.

![](images/6c3604e4bef0df0354686d0f7dc9f5a5929ce52a3ace9d4155da80c14e969689.jpg)  
Fig. 13. Achievable rate and total AoI for different transmit power of Alice, Γ.

The term $| \mathbf { h } _ { b } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] | ^ { 2 }$ in Rician channel model has the following upper bound:

$$
| \mathbf h _ { b } ^ { H } [ n ] \mathbf w _ { b } [ n ] | ^ { 2 } \leqslant \frac { \mu _ { 0 } z _ { b } [ n ] } { d _ { b } ^ { 2 } [ n ] } ,\tag{44}
$$

where

$$
\begin{array} { l } { \displaystyle \mathsf { z } _ { k } [ n ] } \\ { = \left( \sum _ { m = 1 } ^ { M } | \mathbf { w } _ { k } ^ { m } [ n ] | \left( \sqrt { \frac { \kappa } { \kappa + 1 } } + \sqrt { \frac { 1 } { \kappa + 1 } } | \tilde { \mathbf { a } } ^ { m } ( \mathbf { q } [ n ] , \mathbf { u } _ { k } ) | \right) \right) ^ { 2 } , } \end{array}
$$

and $k \in \{ b , c \}$ . Then, Fig. 13 illustrates the comparison of the impact of varying Alice’s transmit power Γ on the achievable rate and total AoI for both LoS and Rician fading channel models. The results demonstrate that the achievable rate increases with Γ, while the total AoI tends to decrease as Γ increases. This is because the larger power budget provides Alice with greater flexibility in resource allocation. Furthermore, it is observed that the LoS communication link allows a higher achievable rate because of better channel conditions, lower path loss, and fewer multi path effects.

## F. Impact of Eve Trajectory Design

To evaluate the performance of the proposed system model, which involves an Eve-equipped UAV with trajectory and tracking capabilities of Alice, we compare it against various benchmark scenarios. These benchmarks include (i) Eve is located at the optimal point and is fixed during communication time [14], (ii) Eve is flying within a limited area [10], and (iii) Eve is located at the ground-fixed point [6]. The analysis focuses on evaluating the impact of these different Eve strategies on the system’s performance. Hence, Fig. 14 illustrates the ratio of received power at Eve to the transmit power from Alice, $\frac { P _ { e } } { P _ { a } }$ , versus Eve’s location. In the proposed system model, Eve employs an adversarial trajectory and tracking strategy to approach Alice, maintaining the minimum allowable distance of two UAV, as detailed in Appendix B. Appendix B demonstrates that Eve achieves the minimum error detection rate regardless of its distance from Alice. Consequently, the system’s baseline, represented by the gray curve, exhibits a steady, higher $\frac { P _ { e } } { P _ { a } }$ ratio regarded as Eve’s ability to track Alice and stay as close as possible during communication. The purple curve indicates that at the start of communication, Eve is assigned the optimal coordinate to place there, which remains stationary throughout the communication. Therefore, this positioning strategy results in a higher $\frac { P _ { e } } { P _ { a } }$ ratio at the start and end points of communication concerning the transmitter’s trajectory path. The red curve depicts Eve’s mobility along an assumed path. Due to eavesdropping from a fixed transmitter and relay-assisted UAV, this results in changes in the $\frac { P _ { e } } { P _ { a } }$ ratio through Eve’s mobility. Finally, the orange curve represents the achievable $\frac { P _ { e } } { P _ { a } }$ ratio by Eve in the fixed-ground point. Therefore, due to the transmitter trajectory path, Eve may or may not be close to her during the communication time. In summary, this paper proposed a non-idealistic and robust assumption for Eve-eqipped UAV to trajectory and tracking Alice freely with maximized advantages compared to other related works.

![](images/c5f814d2104654e4c2d06f10b71c8c7a01be43ea2ec623dddb3d92c51e5d36a0.jpg)  
Fig. 14. Evaluation of Eve’s trajectory and tracking capability to eavesdrop on covert communication from an aerial transmitter in the proposed system model compared to the different benchmarks.

## V. CONCLUSION

This paper investigated the UAV-assisted covert communication using a beamforming technique in the PD-NOMA system. The problem of minimizing the total AoI was formulated by jointly optimizing the UAV trajectory and beamforming design, and the user’s AoI. Despite considering the aerial

$$
\begin{array} { l } { { \displaystyle \left. \mathbf { h } _ { b } ^ { H } [ n ] \mathbf { w } _ { b } [ n ] = \frac { \sqrt { \mu _ { 0 } } } { d _ { b } [ n ] } \right. \times } } \\ { { \displaystyle \left. \sum _ { m = 1 } ^ { M } \left[ \left( \sqrt { \frac { \kappa } { \kappa + 1 } } | \mathbf { w } _ { b } ^ { m } [ n ] | e ^ { j \left( \frac { 2 ( m - 1 ) \times d } { \lambda } \sin \left( \theta ( \mathbf { q } _ { 0 } / n ) , \mathbf { u } _ { b } \right) \right) + \mathcal { L } \mathbf { w } _ { b } ^ { m } [ n ]  } \right) + \left( \sqrt { \frac { 1 } { \kappa + 1 } } | \mathbf { w } _ { b } ^ { m } [ n ] | \hat { \mathbf { a } } ^ { m } ( \mathbf { q } [ n ] , \mathbf { u } _ { b } ) | e ^ { j \left( \mathcal { L } \hat { \mathbf { a } } ^ { m } ( \mathbf { q } [ n ] , \mathbf { u } _ { b } ) + \mathcal { L } \mathbf { w } _ { b } ^ { m } [ n ] \right) } \right) \right] . } } \en\right)d{array} \end{array}\tag{43}
$$

eavesdropper as the worst case with the capability to make a decision on the detection threshold and his distance to UAV, we guaranteed the covert communication with some assumptions: 1) UAV-enabled beamforming which leads to uncertainties for detection error rate, 2) the public user covered the covert user with the PD-NOMA technique. To tackle the non-convex problem, the original problem was decoupled into three sub-problems, AoI optimization, trajectory design optimization, and beamforming optimization which are solved by developing an alternating optimization solution. Numerical results demonstrated the impact of the main design parameters on the UAV-assisted covert communication system with desirable AoI. The significant performance of the PD-NOMA technique compared to OMA on the achievable rate and user’s AoI was highlighted. Additionally, the assumption that “UAV continuously serves the public user while serving the covert user in desirable time $\mathrm { s l o t } ^ { \prime \mathrm {  s } }$ is well-studied. This work can be extended by integrating distributed multi-modal foundation models (FMs) for intelligent 6G network optimization. Specifically, AI-driven multi-modal fusion aligns network decisions with real-time context (e.g., UAV mobility, channel states, and required QoS), reducing the control loop to minimize AoI. Data parallelism addresses computational and bandwidth bottlenecks in real-time network control [37]. This strategic direction motivates a close integration of AI capabilities with 6G architectures to achieve covert communication in the context-aware of minimum AoI optimization.

## APPENDIX A PROOF OF LEMMA 1

Based on the (14) and (18), the false alarm probability at Eve during the n-th time slot can be expressed as:

$$
\begin{array} { r l } & { \mathbb { P } _ { \mathtt { F A } } [ n ] = \displaystyle \int _ { \tau [ n ] - \sigma _ { e } ^ { 2 } } ^ { \infty } \frac { 1 } { \varpi _ { c } [ n ] } e ^ { - \frac { z } { \varpi _ { c } [ n ] } } d z , \ \forall n , } \\ & { \quad \quad = \displaystyle \frac { 1 } { \varpi _ { c } [ n ] } [ - \varpi _ { c } [ n ] e ^ { - \frac { z } { \varpi _ { c } [ n ] } } ]  _ { \tau [ n ] - \sigma _ { e } ^ { 2 } } ^ { \infty } = e ^ { \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \varpi _ { c } [ n ] } } . } \end{array}\tag{45}
$$

To derive the distribution function of the miss detection probability, we employ the moment-generating function (MGF), which represents the expected value of the exponential function of the random variable. Let X be a random variable, the MGF of $X ,$ denoted by $\phi _ { X } ( s ) = E \{ e ^ { s X } \}$ . If s is a continuous random variable, the following relation between the MGF of $\phi _ { X } ( s )$ and the two-sided Laplace transform of its probability density function $f _ { X } ( x )$ holds $\phi _ { X } ( s ) ~ = ~ L \{ f _ { X } ( x ) \} | _ { s  - s } .$ Hence, the exponential distribution of random variable X with parameter λ is $\begin{array} { r } { \phi _ { X } ( s ) = \frac { \lambda } { \lambda - s } } \end{array}$

With assumption of $v [ n ] = | \alpha _ { c } [ n ] | ^ { 2 } + | \alpha _ { b } [ n ] | ^ { 2 }$ and $| \alpha _ { c } [ n ] | ^ { 2 }$ and $| \alpha _ { b } [ n ] | ^ { 2 }$ are i.i.d, the MGF of $\upsilon [ n ]$ is:

$$
\begin{array} { r l } & { \phi _ { v } ( s ) = \phi _ { | \alpha _ { c } [ n ] | ^ { 2 } } ( s ) \phi _ { | \alpha _ { b } [ n ] | ^ { 2 } } ( s ) } \\ & { \phantom { \phi _ { | \alpha _ { c } [ n ] | } } = \frac { \frac { 1 } { | \alpha _ { c } [ n ] | } } { \frac { 1 } { | \alpha _ { c } [ n ] | } - s } \frac { \frac { 1 } { | \alpha _ { b } [ n ] | } } { \frac { 1 } { | \alpha _ { b } [ n ] | } - s } = \frac { \frac { 1 } { | \alpha _ { c } [ n ] | } \frac { 1 } { | \alpha _ { b } [ n ] | } } { \left( \frac { 1 } { | \alpha _ { c } [ n ] | } - s \right) \left( \frac { 1 } { | \alpha _ { b } [ n ] | } - s \right) } , } \\ & { \phantom { \phi _ { | \alpha _ { c } [ n ] | } } = \frac { \frac { 1 } { | \alpha _ { b } [ n ] | } } { \frac { 1 } { | \alpha _ { b } [ n ] | } - \frac { 1 } { | \alpha _ { c } [ n ] | } \frac { 1 } { | \alpha _ { c } [ n ] | } - s } } \\ & { \phantom { \phi _ { | \alpha _ { c } [ n ] | } } + \frac { \frac { 1 } { | \alpha _ { c } [ n ] | } } { \frac { 1 } { | \alpha _ { c } [ n ] | } - \frac { 1 } { | \alpha _ { b } [ n ] | } } \frac { \frac { 1 } { | \alpha _ { b } [ n ] | } } { \frac { 1 } { | \alpha _ { b } [ n ] | } - s } . } \end{array}
$$

Consequently:

$$
\begin{array} { r l r } & { } & { f _ { \Upsilon } ( v ) = \frac { \frac { 1 } { \varpi _ { c } [ n ] } \frac { 1 } { \varpi _ { b } [ n ] } } { \frac { 1 } { \varpi _ { b } [ n ] } - \frac { 1 } { \varpi _ { c } [ n ] } } \left( e ^ { - \frac { v [ n ] } { \varpi _ { c } [ n ] } } - e ^ { - \frac { v [ n ] } { \varpi _ { b } [ n ] } } \right) , } \\ & { } & { = \frac { 1 } { \varpi _ { c } [ n ] - \varpi _ { b } [ n ] } \left( e ^ { - \frac { v [ n ] } { \varpi _ { c } [ n ] } } - e ^ { - \frac { v [ n ] } { \varpi _ { b } [ n ] } } \right) . } \end{array}\tag{47}
$$

According to (15) and (47), the miss detection probability at Eve for the n-th time slot is determined in (48), shown at the bottom of the page.

Therefore, based on (13), (45), and (48) the detection error rate $\xi [ n ]$ at Eve for $\tau [ n ] > \sigma _ { e } ^ { 2 }$ region, is achieved as:

$$
\xi [ n ] = \frac { \varpi _ { b } [ n ] } { \varpi _ { c } [ n ] - \varpi _ { b } [ n ] } \left[ e ^ { \left( \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \varpi _ { b } [ n ] } \right) } - e ^ { \left( \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \varpi _ { c } [ n ] } \right) } \right] + 1 .\tag{49}
$$

## APPENDIX B PROOF OF LEMMA 2

1) Detection Error Rate Optimization: As mentioned above, aerial Eve is ambitious to minimize the detection error rate $\xi ^ { * } [ n ]$ at each time slot. Corresponding to the achieved detection error rate at (20), ξ[n] is always equal to one for $\tau [ n ] < \sigma _ { e } ^ { 2 }$ region and this is the worst case for Eve. For $\tau [ n ] > \sigma _ { e } ^ { \bar { 2 } }$ region, we note that $\xi [ n ]$ is a function of two variables: the detection threshold $\tau [ n ]$ , and Eve’s location $1 [ n ]$ at each time slot n. Eve attempts to detect the covert transmission by minimizing his distance from Alice $d _ { e } [ n ]$ while determining the optimal detection threshold. Hence, we re-expressed the constraint (22d) as the following optimization problem to find the optimal error detection rate, for $\tau [ n ] > \sigma _ { e } ^ { 2 }$ region:

$$
\operatorname* { m i n } _ { \tau [ n ] , d _ { e } [ n ] } \xi [ n ]\tag{50a}
$$

$$
\mathrm { s . t . ~ } d _ { e } [ n ] \geqslant d _ { \operatorname* { m i n } } ,\tag{50b}
$$

where (53b) is the collision avoidance constraint of Eve and Alice. In general, the optimal solution for the minimization problem and obtaining the corresponding minimum

$$
\begin{array} { r l } & { \mathbb { P } _ { \mathrm { x n p } } [ n ] = \int _ { 0 } ^ { \tau [ n ] - \sigma _ { e } ^ { 2 } } \frac { 1 } { \overline { { \omega _ { c } } } [ n ] - \overline { { \omega _ { b } } } [ n ] } ( e ^ { - \frac { \omega [ n ] } { \mathrm { s e c t } [ n ] } } - e ^ { - \frac { \omega [ n ] } { \mathrm { s b } [ n ] } } ) d v = \frac { 1 } { \overline { { \omega _ { c } } } [ n ] - \overline { { \omega _ { b } } } [ n ] } [ - \overline { { \omega _ { c } } } [ n ] e ^ { - \frac { \omega [ n ] } { \mathrm { s e c t } [ n ] } } + \overline { { \omega _ { b } } } [ n ] e ^ { - \frac { \omega [ n ] } { \mathrm { s e c t } [ n ] } } ] | _ { 0 } ^ { \tau [ n ] - \sigma _ { e } ^ { 2 } } ,  } \\ & { \qquad = \frac { 1 } { \overline { { \omega _ { c } } } [ n ] - \overline { { \omega _ { b } } } [ n ] } [ - \overline { { \omega _ { c } } } [ n ] ( e ^ { - \frac { ( \tau [ n ] - \sigma _ { e } ^ { 2 } ) } { \mathrm { s e c t } [ n ] } } - 1 ) + \overline { { \omega _ { b } } } [ n ] ( e ^ { - \frac { ( \tau [ n ] - \sigma _ { e } ^ { 2 } ) } { \overline { { \omega _ { c } } } [ n ] } } - 1 ) ] = \frac { \overline { { \omega _ { b } } } [ n ] e ^ { \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \mathrm { s e c t } [ n ] } } - \overline { { \omega _ { c } } } [ n ] e ^ { \frac { \sigma _ { e } ^ { 2 } - \tau [ n ] } { \mathrm { s e c t } [ n ] } } } { \overline { { \omega _ { c } } } [ n ] - \overline { { \omega _ { b } } } [ n ] } + 1 } \end{array}\tag{48}
$$

detection error rate $\xi ^ { * } [ n ]$ is partial derivatives. We take a partial derivative for $\tau [ n ]$ and $d _ { e } [ n ]$ and set them equal to zero i.e., $\begin{array} { r } { \frac { \partial \xi [ n ] } { \partial \tau [ n ] } ~ = ~ \frac { { \bf \ddot { \nabla } } \partial { \bf \dot { \xi } } [ n ] } { \partial d _ { e } [ n ] } ~ = ~ { \bf \ddot { \xi } } ^ { 1 } } \end{array}$ . Corresponding to (8), and $\begin{array} { r } { \varpi _ { k } [ n ] = \dot { \sum _ { m = 1 } ^ { M } } | h _ { e , m } [ \dot { n } ] | ^ { 2 } \sigma _ { k , m } ^ { 2 } [ n ] } \end{array}$ , we rewrite $\xi [ n ] =$ $\begin{array} { r } { \frac { B [ n ] } { C [ n ] - B [ n ] } \left\lceil e ^ { \left( \frac { d _ { e } ^ { 2 } [ n ] \left( \sigma _ { e } ^ { 2 } - \tau [ n ] \right) } { \mu _ { 0 } B [ n ] } \right) } - e ^ { \left( \frac { d _ { e } ^ { 2 } [ n ] \left( \sigma _ { e } ^ { 2 } - \tau [ n ] \right) } { \mu _ { 0 } C [ n ] } \right) } \right\rceil + 1 } \end{array}$ , where $\begin{array} { r } { B [ n ] = \sum _ { m = 1 } ^ { M } \sigma _ { b , m } ^ { 2 } [ n ] } \end{array}$ , and $\begin{array} { r } { C [ n ] = \sum _ { m = 1 } ^ { M } \sigma _ { c , m } ^ { 2 } \mathbf { \bar { \Sigma } } [ n ] } \end{array}$ . Therefore, $\frac { \partial \xi [ n ] } { \partial \tau [ n ] }$ and $\frac { \partial \xi [ n ] } { \partial d _ { e } [ n ] }$ are calculated at (51) and (52), shown at the bottom of the page, respectively.

By setting $\begin{array} { r l r } {  { \frac { \partial \xi [ n ] } { \partial \tau [ n ] } } } & { { } = } & { 0 } \end{array}$ , the optimal detection threshold is obtained as $\begin{array} { r } { \tau ^ { * } [ n ] ~ = ~ \sigma _ { e } ^ { 2 } ~ - ~ \ln \left( { \frac { C [ n ] } { B [ n ] } } \right) ^ { \left( { \frac { B [ n ] C [ n ] \mu _ { 0 } } { ( B [ n ] - C [ n ] ) d _ { e } ^ { 2 } [ n ] } } \right) } ~ } \end{array}$ In addition, by setting $\begin{array} { r } { \frac { \partial \xi [ n ] } { \partial d _ { e } [ n ] } ~ = ~ 0 , } \end{array}$ , and assuming $\tau ^ { * } [ n ]$ the optimal value of the error detection rate is independent of the distance between Alice and Eve $d _ { e } [ n ]$ . However, to detect the optimal detection error rate, an aerial Eve using a radiometer detects the maximum received signal energy $T _ { e } [ n ]$ Hence, Eve is faced with the following optimization problem:

$$
\operatorname* { m a x } _ { d _ { e } [ n ] } T _ { e } [ n ]\tag{53a}
$$

$$
\mathrm { s . t . ~ } d _ { e } [ n ] \geqslant d _ { \operatorname* { m i n } } .\tag{53b}
$$

We express the equivalent object of the optimization problem (53) according to the assumption of large-scale LoS path loss link’s model between Alice and Eve [38], as follows:

$$
\begin{array} { l } { \displaystyle \operatorname* { m a x } _ { d _ { e } [ n ] } T _ { e } [ n ] = \operatorname* { m a x } _ { d _ { e } [ n ] } E \{ | y _ { e } [ n ] | ^ { 2 } \} \cong \operatorname* { m a x } _ { d _ { e } [ n ] } \frac { E \{ | y _ { e } | ^ { 2 } \} } { E \{ | y _ { a } | ^ { 2 } \} } , \ ~ } \\ { \displaystyle = \operatorname* { m a x } _ { d _ { e } [ n ] } \frac { P _ { e } } { P _ { a } } = \operatorname* { m a x } _ { d _ { e } [ n ] } \left( \frac { \sqrt { G } \lambda _ { 0 } } { 4 \pi d _ { e } [ n ] } \right) ^ { 2 } , \ ~ } \end{array}\tag{54a}
$$

where $\cong$ is congruent symbol, and $\sqrt { G }$ is the product of the transmit and receive antenna field radiation patterns in the LoS direction with the signal wavelength $\lambda _ { 0 } .$ . It is evident that the maximum error detection rate is attained when the distance between Alice and Eve is minimized, specifically within the allowed flying distance for the two UAV, $d _ { e } [ n ] ~ = ~ d _ { \mathrm { m i n } }$ . Consequently, the corresponding minimum detection error rate $\xi ^ { * } [ n ]$ associated with the optimal detection threshold $\begin{array} { r } { \tau ^ { * } [ n ] = \sigma _ { e } ^ { 2 } - \ln \left( \frac { C [ n ] } { B [ n ] } \right) ^ { \left( \frac { B [ n ] C [ n ] \mu _ { 0 } } { ( B [ n ] - C [ n ] ) d _ { e } ^ { 2 } [ n ] } \right) } } \end{array}$ , and the optimal distance $d _ { e } ^ { * } [ n ] ~ = ~ \ ` { d _ { \mathrm { m i n } } } ,$ is expressed as $\xi ^ { * } [ n ] \ =$ $\begin{array} { r } { \frac { B [ n ] } { C [ n ] - B [ n ] } \left[ \left( \frac { C [ n ] } { B [ n ] } \right) ^ { \frac { C [ n ] } { B [ n ] - C [ n ] } } - \left( \frac { C [ n ] } { B [ n ] } \right) ^ { \frac { B [ n ] } { B [ n ] - C [ n ] } } \right] + 1 . } \end{array}$

## APPENDIX C PROOF OF THEOREM 2

As mentioned previously, in the absence of the rank-one constraint (36j), the problem (41) becomes jointly convex with respect to all optimization variables. Consequently, the optimal solution can be characterized using the Karush-Kuhn-Tucker (KKT) conditions. Specifically, the Lagrangian function of problem (41), with respect to the active beamforming ${ \mathbf W } _ { k } [ n ]$ can be expressed as:

$$
\begin{array} { r l } { \mathcal { L } = \frac { \Delta } { \gamma _ { 1 } } \cdot \sum _ { i = 1 } ^ { N } \frac { \partial \left( \Gamma ^ { i } - \Gamma ^ { i } - \Gamma ^ { i } - \Gamma ^ { i } \right) } { \partial \Gamma ^ { i } } } & { { } } \\ { = } & { { } - \frac { \Delta } { \gamma _ { 1 } } \cdot \sum _ { i = 1 } ^ { N } \frac { \partial \left( \Gamma ^ { i } - \Gamma ^ { i } - \Gamma ^ { i } \right) } { \partial \Gamma ^ { i } } } \\ { \quad } & { { } - \frac { \Delta } { \gamma _ { 1 } } \cdot \sum _ { i = 1 } ^ { N } \frac { \partial \left( \Gamma ^ { i } - \Gamma ^ { i } - \Gamma ^ { i } \right) } { \partial \Gamma ^ { i } } \mathrm { R e } ^ { \mathrm { i } \Gamma } } \\ { \quad } & { { } - \Gamma \cdot \Gamma ^ { i } \Gamma \Gamma _ { i } \Gamma _ { i } \cdot \Gamma _ { i } \cdot \Gamma _ { i } \Gamma _ { i } \mathrm { R e } ^ { \mathrm { i } \Gamma } } \\ { \quad } & { { } - \frac { \Delta } { \gamma _ { 1 } } \cdot \sum _ { i = 1 } ^ { N } \frac { \partial \left( \Gamma ^ { i } - \Gamma ^ { i } - \Gamma ^ { i } \right) } { \partial \Gamma ^ { i } } \mathrm { R e } ^ { \mathrm { i } \Gamma } } \\ { \quad } & { { } - \frac { \Delta } { \gamma _ { 1 } } \cdot \sum _ { i = 1 } ^ { N } \frac { \partial \left( \Gamma ^ { i } - \Gamma ^ { i } - \Gamma ^ { i } \right) } { \partial \Gamma ^ { i } } } \\ { \quad } &  { } - \frac { \Delta } { \gamma _ { 1 } } \cdot \sum _ { i = 1 } ^ { N } \frac { \partial \Gamma ^ { i } } { \partial \Gamma ^ { i } } \left( \frac { \partial \Gamma ^ { i } } { \partial \Gamma ^ { i } } \mathrm { R e } ^ { \mathrm { i } \Gamma } \mathrm { R e } ^ { \mathrm { i } \Gamma } \mathrm { R e } ^ { \mathrm { i } \Gamma } \right) - \frac { \Gamma ^ { i } }  \partial \Gamma ^ \end{array}\tag{55}
$$

The Lagrange multipliers associated with the constraint $- \gamma [ n ] , \rho _ { k } [ n ] , \chi [ n ] , \psi _ { k } [ n ]$ , and $\nu _ { k } [ n ]$ —correspond to (36b)-(36f), respectively. Matrix $\tilde { \mathbf { X } } _ { k } [ n ]$ serves as the Lagrange multiplier matrix associated with the positive semi-definite constraint imposed on ${ \mathbf W } _ { k } [ n ]$ in constraint (36i). To obtained the optimal $\mathbf { W } _ { k } ^ { * } [ n ]$ , the KKT conditions is expressed as:

$$
\left\{ \begin{array} { l l } { \gamma ^ { * } [ n ] , \rho _ { k } ^ { * } [ n ] , \chi ^ { * } [ n ] , \psi _ { k } ^ { * } [ n ] , \nu _ { k } ^ { * } [ n ] \geqslant 0 , } \\ { \tilde { \mathbf { X } } _ { k } ^ { * } [ n ] \succeq \mathbf { 0 } } \\ { \tilde { \mathbf { X } } _ { k } ^ { * } [ n ] \mathbf { W } _ { k } ^ { * } [ n ] = \mathbf { 0 } , } \\ { \nabla _ { \mathbf { W } _ { k } ^ { * } [ n ] } \mathcal { L } = 0 , } \end{array} \right.\tag{56}
$$

where $\gamma ^ { \ast } [ n ] , \rho _ { k } ^ { \ast } [ n ] , \chi ^ { \ast } [ n ] , \psi _ { k } ^ { \ast } [ n ] , \nu _ { k } ^ { \ast } [ n ]$ and $\tilde { \mathbf { X } } _ { k } ^ { * } [ n ]$ stand for the optimal Lagrange multipliers. In addition, the term $\nabla _ { \mathbf { W } _ { k } ^ { * } [ n ] } \mathcal { L }$

$$
\begin{array} { r l } & { \frac { \partial \xi [ n ] } { \partial \tau [ n ] } = \frac { B [ n ] } { C [ n ] - B [ n ] } \left[ - \frac { d _ { c } ^ { 2 } [ n ] } { \mu _ { 0 } B [ n ] } e ^ { \left( \frac { d _ { c } ^ { 2 } [ n ] \left( \sigma _ { c } ^ { 2 } - \tau [ n ] \right) } { \mu _ { 0 } B [ n ] } \right) } + \frac { d _ { c } ^ { 2 } [ n ] } { \mu _ { 0 } C [ n ] } e ^ { \left( \frac { d _ { c } ^ { 2 } [ n ] \left( \sigma _ { c } ^ { 2 } - \tau [ n ] \right) } { \mu _ { 0 } C [ n ] } \right) } \right] , } \\ & { \frac { \partial \xi [ n ] } { \partial d _ { a c } [ n ] } = \frac { B [ n ] } { C [ n ] - B [ n ] } \left[ \frac { 2 d _ { a c } [ n ] \left( \sigma _ { c } ^ { 2 } - \tau [ n ] \right) } { \mu _ { 0 } B [ n ] } e ^ { \left( \frac { d _ { a c } ^ { 2 } [ n ] \left( \sigma _ { c } ^ { 2 } - \tau [ n ] \right) } { \mu _ { 0 } B [ n ] } \right) } - \frac { 2 d _ { a c } [ n ] \left( \sigma _ { c } ^ { 2 } - \tau [ n ] \right) } { \mu _ { 0 } C [ n ] } e ^ { \left( \frac { d _ { a c } ^ { 2 } [ n ] \left( \sigma _ { c } ^ { 2 } - \tau [ n ] \right) } { \mu _ { 0 } C [ n ] } \right) } \right] . } \end{array}\tag{51}
$$

(52)

represent gradient of $\mathcal { L }$ to find the optimal $\mathbf { W } _ { k } ^ { * } [ n ]$ . Hence, $\nabla _ { \mathbf { W } _ { k } ^ { * } [ n ] } \mathcal { L } = 0$ can be calculated as:

$$
\begin{array} { l } { { \displaystyle \nabla { } _ { { \bf W } _ { \{ i } [ n ] } , \mathcal { E } } = - \sum _ { n = 1 } ^ { N } \gamma [ n ] { \bf I } } \ ~  \\ { { \displaystyle \mathrm { ~  ~ { \large ~ \Gamma ~ } ~ } _ { n = 1 } ^ { N } \sum _ { \substack { \mathrm { ~  ~ { ~ \large ~ \sum ~ } ~ } n \in \{ \bf ~ f ~ } _ { \ell \in \mathcal { H } _ { \ell \setminus i } } \} \times \{ n \} \times \left[ n \right] \bf H _ { k } ^ { H } [ n ] } \ ~ } } \\ { { \displaystyle \mathrm { ~  ~ { ~ \large ~ \sum ~ } ~ } _ { n = 1 } ^ { N } \sum \gamma [ n ] \frac { \partial \Upsilon ( p _ { \ell } [ n ] , p _ { \ell } [ n ] ) } { \partial p _ { k } [ n ] } \gamma [ n ] { \bf I } } \ ~ } \\ { { \displaystyle \mathrm { ~ \large ~ \sum ~ } _ { n = 1 } ^ { N } \sum \gamma [ n ] \frac { \partial \Upsilon ( p _ { \ell } [ n ] , p _ { \ell } [ n ] ) } { \partial p _ { k } [ n ] } \gamma [ n ] { \bf I } } \ ~ } \\ { { \displaystyle \mathrm { ~ \large ~ + ~ } \sum _ { n = 1 } ^ { N } \sum _ { \substack { \mathrm { ~ \large ~ \sum ~ } \mathrm { ~ } } n \in \{ \bf ~ f ~ } _ { \ell \setminus i } } \ \gamma _ { \mathrm { a l } } [ n ] { \bf H } _ { k } ^ { H } [ n ] } \ ~  \\ { { \displaystyle \mathrm { ~ \large ~ + ~ } \sum _ { n = 1 } ^ { N } \sum _ { \substack { \mathrm { ~ \large ~ \sum ~ } \mathrm { ~ } } n \in \{ \bf ~ f ~ } _ { \ell \setminus i } } \ \gamma [ n ] = 0 } \ ~  \end{array}\tag{57}
$$

where $\varkappa _ { k } [ n ] = \left\{ \begin{array} { l l } { 1 , } & { ~ k = c , } \\ { - 1 , } & { ~ k = b . } \end{array} \right.$ . Therefore, (58) is obtained from (57), as follows:

$$
\begin{array} { r l } & { \underbrace { \left( \gamma ^ { * } [ n ] + \chi ^ { * } [ n ] \frac { \partial \Upsilon \left( p _ { b } [ n ] , p _ { c } [ n ] \right) } { \partial p _ { k } [ n ] } \right) } _ { \varrho ^ { * } [ n ] } \mathbf { I } } \\ & { = \underbrace { \left( \rho _ { k } ^ { * } [ n ] \varkappa _ { k } [ n ] + \psi _ { k } ^ { * } [ n ] \right) } _ { \vartheta _ { k } ^ { * } [ n ] } \mathbf { H } _ { k } ^ { H } [ n ] + \tilde { \mathbf { X } } _ { k } ^ { * } [ n ] } \end{array}\tag{58}
$$

In addition, by multiplying both sides of (58) by $\mathbf { W } _ { k } ^ { * } [ n ]$ , we derive

$$
\begin{array} { r } { \varrho ^ { * } [ n ] \mathbf { W } _ { k } ^ { * } [ n ] = \vartheta _ { k } ^ { * } [ n ] \mathbf { H } _ { k } [ n ] \mathbf { W } _ { k } ^ { * } [ n ] + \underbrace { \tilde { \mathbf { X } } _ { k } ^ { * } [ n ] \mathbf { W } _ { k } ^ { * } [ n ] } _ { 0 } . } \end{array}\tag{59}
$$

Consequently, using basic rank inequality properties for matrices, we observe that:

$$
\begin{array} { r l r } {  { \mathrm { r a n k } ( \varrho ^ { * } [ n ] \mathbf { W } _ { k } ^ { * } [ n ] ) = \mathrm { r a n k } ( \vartheta _ { k } ^ { * } [ n ] \mathbf { H } _ { k } [ n ] \mathbf { W } _ { k } ^ { * } [ n ] ) } } \\ & { } & { \leqslant \mathrm { r a n k } ( \mathbf { H } _ { k } [ n ] ) = \mathrm { r a n k } ( \mathbf { h } _ { k } [ n ] \mathbf { h } _ { k } ^ { H } [ n ] ) } \\ & { } & { = 1 . } \end{array}
$$

According to, we establish that rank $( \mathbf { W } _ { k } ^ { * } [ n ] ) \leqslant 1$

## REFERENCES

[1] T. Q. Duong, K. J. Kim, Z. Kaleem, M.-P. Bui, and N.-S. Vo, “UAV caching in 6G networks: A survey on models, techniques, and applications,” Phys. Commun., vol. 51, Apr. 2022, Art. no. 101532. [Online]. Available: https://www.sciencedirect.com/science/article/pii/ S1874490721002482

[2] D. Mishra and E. Natalizio, “A survey on cellular-connected UAVs: Design challenges, enabling 5G/B5G innovations, and experimental advancements,” Comput. Netw., vol. 182, Dec. 2020, Art. no. 107451. [Online]. Available: https://www.sciencedirect.com/science/article/pii/ S1389128620311324

[3] J. Hu, C. Chen, L. Cai, M. R. Khosravi, Q. Pei, and S. Wan, “UAVassisted vehicular edge computing for the 6G Internet of Vehicles: Architecture, intelligence, and challenges,” IEEE Commun. Standards Mag., vol. 5, no. 2, pp. 12–18, Jun. 2021.

[4] X. Zhou, S. Yan, F. Shu, R. Chen, and J. Li, “UAV-enabled covert wireless data collection,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3348–3362, Nov. 2021.

[5] X. Jiang et al., “Covert communication in UAV-assisted air-ground networks,” IEEE Wireless Commun., vol. 28, no. 4, pp. 190–197, Aug. 2021.

[6] X. Zhou, S. Yan, J. Hu, J. Sun, J. Li, and F. Shu, “Joint optimization of a UAV’s trajectory and transmit power for covert communications,” IEEE Trans. Signal Process., vol. 67, no. 16, pp. 4276–4290, Aug. 2019.

[7] P. Liu, J. Si, Z. Li, N. Al-Dhahir, and Y. Gao, “Joint 3-D trajectory and power optimization for dual-UAV-assisted short-packet covert communications,” IEEE Internet Things J., vol. 11, no. 10, pp. 17388–17401, May 2024.

[8] F. Yang, C. Wang, J. Xiong, N. Deng, N. Zhao, and Y. Li, “UAV-enabled robust covert communication against active wardens,” IEEE Trans. Veh. Technol., vol. 73, no. 6, pp. 9159–9164, Jun. 2024.

[9] H. Mao, Y. Liu, Z. Xiao, Z. Han, and X.-G. Xia, “Joint resource allocation and 3-D deployment for multi-UAV covert communications,” IEEE Internet Things J., vol. 11, no. 1, pp. 559–572, Jan. 2024.

[10] X. Chen, M. Sheng, N. Zhao, W. Xu, and D. Niyato, “UAV-relayed covert communication towards a flying warden,” IEEE Trans. Commun., vol. 69, no. 11, pp. 7659–7672, Nov. 2021.

[11] S. Ma et al., “Covert beamforming design for intelligent-reflectingsurface-assisted IoT networks,” IEEE Internet Things J., vol. 9, no. 7, pp. 5489–5501, Apr. 2022.

[12] S. Ma et al., “Robust beamforming design for covert communications,” IEEE Trans. Inf. Forensics Security, vol. 16, pp. 3026–3038, 2021.

[13] M. Forouzesh, P. Azmi, N. Mokari, and D. Goeckel, “Covert communication using null space and 3D beamforming: Uncertainty of Willie’s location information,” IEEE Trans. Veh. Technol., vol. 69, no. 8, pp. 8568–8576, Aug. 2020.

[14] J. Yu et al., “Joint 3D beamforming-and-trajectory design for UAVsatellite uplink covert communication,” IEEE Trans. Commun., vol. 73, no. 5, pp. 3469–3481, May 2025.

[15] S. Zhang, H. Zhang, Z. Han, H. V. Poor, and L. Song, “Age of information in a cellular Internet of UAVs: Sensing and communication trade-off design,” IEEE Trans. Wireless Commun., vol. 19, no. 10, pp. 6578–6592, Oct. 2020.

[16] A. Cao, C. Shen, J. Zong, and T.-H. Chang, “Peak age-of-information minimization of UAV-aided relay transmission,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC Workshops), Dublin, Ireland, Jun. 2020, pp. 1–6.

[17] P. D. Mankar, M. A. Abd-Elmagid, and H. S. Dhillon, “Spatial distribution of the mean peak age of information in wireless networks,” IEEE Trans. Wireless Commun., vol. 20, no. 7, pp. 4465–4479, Jul. 2021.

[18] R. Han, J. Wang, L. Bai, J. Liu, and J. Choi, “Age of information and performance analysis for UAV-aided IoT systems,” IEEE Internet Things J., vol. 8, no. 19, pp. 14447–14457, Oct. 2021.

[19] J. Li, D. Wu, C. Yue, Y. Yang, M. Wang, and F. Yuan, “Energy-efficient transmit probability-power control for covert D2D communications with age of information constraints,” IEEE Trans. Veh. Technol., vol. 71, no. 9, pp. 9690–9704, Sep. 2022.

[20] W. Yang, X. Lu, S. Yan, F. Shu, and Z. Li, “Age of information for shortpacket covert communication,” IEEE Wireless Commun. Lett., vol. 10, no. 9, pp. 1890–1894, Sep. 2021.

[21] Y. Wang, S. Yan, W. Yang, and Y. Cai, “Covert communications with constrained age of information,” IEEE Wireless Commun. Lett., vol. 10, no. 2, pp. 368–372, Feb. 2021.

[22] S. S. Hosseini, P. Azmi, and N. Mokari, “Minimizing average age of information in reliable covert communication on time-varying channels,” IEEE Trans. Veh. Technol., vol. 73, no. 1, pp. 651–659, Jan. 2024.

[23] C. Wang et al., “Covert communication assisted by UAV-IRS,” IEEE Trans. Commun., vol. 71, no. 1, pp. 357–369, Jan. 2023.

[24] X. Zhou, S. Yan, D. W. K. Ng, and R. Schober, “Three-dimensional placement and transmit power design for UAV covert communications,” IEEE Trans. Veh. Technol., vol. 70, no. 12, pp. 13424–13429, Dec. 2021.

[25] X. Hou, J. Wang, C. Jiang, X. Zhang, Y. Ren, and M. Debbah, “UAVenabled covert federated learning,” IEEE Trans. Wireless Commun., vol. 22, no. 10, pp. 6793–6809, Oct. 2023.

[26] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.

[27] S. Salar Hosseini, M. R. Javan, and A. Nazari, “Multicasting in NOMAbased UAV networks: Path design and throughput maximisation,” IET Commun., vol. 16, no. 14, pp. 1708–1723, Aug. 2022.

[28] T.-H. Vu, A.-T. Le, N. H. Tu, T. N. Nguyen, and M. Voznak, “On performance of IoT networks with coordinated NOMA transmission: Covert monitoring and information decoding,” IEEE Internet Things J., vol. 12, no. 22, pp. 48069–48084, Nov. 2025.

[29] L. J. Allen, An Introduction to Stochastic Processes With Applications To Biology. Boca Raton, FL, USA: CRC Press, 2010.

[30] W. Lin, L. Li, J. Yuan, Z. Han, M. Juntti, and T. Matsumoto, “Age-ofinformation in first-come-first-served wireless communications: Upper bound and performance optimization,” IEEE Trans. Veh. Technol., vol. 71, no. 9, pp. 9501–9515, Sep. 2022.

[31] S. Vanka, S. Srinivasa, Z. Gong, P. Vizi, K. Stamatiou, and M. Haenggi, “Superposition coding strategies: Design and experimental evaluation,” IEEE Trans. Wireless Commun., vol. 11, no. 7, pp. 2628–2639, Jul. 2012.

[32] M. Grant and S. Boyd. (2020). CVX: MATLAB Software for Disciplined Convexprogramming. [Online]. Available: http://cvxr.com/cvx

[33] X. Mu, Y. Liu, L. Guo, J. Lin, and N. Al-Dhahir, “Exploiting intelligent reflecting surfaces in NOMA networks: Joint beamforming optimization,” IEEE Trans. Wireless Commun., vol. 19, no. 10, pp. 6884–6898, Oct. 2020.

[34] A. Nazari, M. R. Javan, and S. S. Hosseini, “Resource allocation in power domain NOMA-based cooperative multicell networks,” IET Commun., vol. 14, no. 7, pp. 1162–1168, Apr. 2020.

[35] H. Wang, G. Xu, J. Liu, Z. Song, Q. Zhang, and W. Zhang, “The λ-κ- µ fading distribution,” IEEE Antennas Wireless Propag. Lett., vol. 23, no. 12, pp. 4398–4402, Dec. 2024.

[36] J. Liu, G. Xu, H. Wang, C. Zhang, and X. Lu, “Double distribution: Modeling and performance evaluation in non-homogeneous environments,” IEEE Wireless Commun. Lett., vol. 14, no. 10, pp. 3378–3382, Oct. 2025.

[37] J. Du, T. Lin, C. Jiang, Q. Yang, C. F. Bader, and Z. Han, “Distributed foundation models for multi-modal learning in 6G wireless networks,” IEEE Wireless Commun., vol. 31, no. 3, pp. 20–30, Jun. 2024.

[38] A. Goldsmith, Wireless Communications. Cambridge, U.K.: Cambridge Univ. Press, 2005.

![](images/275323911e83aefdb517a6b532ba192ddbed11fbc42128596bdd18a2de1d1b40.jpg)  
Shima Salar Hosseini received the M.Sc. degree in electrical engineering from Shahrood University of Technology (SUT), Shahrood, Iran, in 2019, and the Ph.D. degree in electrical engineering from Tarbiat Modares University, Tehran, Iran, in 2025. Her research interests include of 5G and 6G wireless communication, multiple access techniques, and design and analysis of air-to-ground networks, specially unmanned aerial vehicle (UAV) and optimizing delay sensitive networks.

![](images/d46664160cd05562cd8a32fb0a148ed619a6ec9f96c19f84d8afabec587c9a2f.jpg)

Paeiz Azmi (Senior Member, IEEE) was born in Tehran, Iran, in April 1974. He received the B.Sc., M.Sc., and Ph.D. degrees in electrical engineering from the Sharif University of Technology (SUT), Tehran, in 1996, 1998, and 2002, respectively. Since September 2002, he has been with the Electrical and Computer Engineering Department, Tarbiat Modares University, Tehran, where he became an Associate Professor in January 2006 and is currently a Full Professor. From 1999 to 2001, he was with the Advanced Communication Science Research Labo-

ratory, Iran Telecommunication Research Center (ITRC), Tehran. From 2002 to 2005, he was with the Signal Processing Research Group, ITRC. His current research interests include modulation and coding techniques, digital signal processing, wireless communications, resource allocation, molecular communications, and estimation and detection theories.

![](images/981e88140270d90f2f55ce90200ea56a99065dd8ed397d0be002cd6c7f4c9fe4.jpg)  
Ali Nazari received the M.Sc. degree in electrical engineering from Shahrood University of Technology (SUT), Shahrood, Iran, in 2019. He is currently pursuing the Ph.D. degree with the Signal Processing and Communication System Laboratory, University of Tehran, Tehran, Iran. His research interests cover the cooperative and adaptive wireless communications in 5G and beyond, designing the reconfigurable intelligence surfaces-assisted networks, and estimation and detection of wireless issues.