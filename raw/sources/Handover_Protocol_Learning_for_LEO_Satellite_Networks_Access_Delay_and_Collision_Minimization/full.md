# Handover Protocol Learning for LEO Satellite Networks: Access Delay and Collision Minimization

Ju-Hyung Lee , Member, IEEE, Chanyoung Park , Soohyun Park , and Andreas F. Molisch , Fellow, IEEE

Abstract— This study presents a novel deep reinforcement learning (DRL)-based handover (HO) protocol, called DHO, specifically designed to address the persistent challenge of long propagation delays in low-Earth orbit (LEO) satellite networks’ HO procedures. DHO skips the Measurement Report (MR) in the HO procedure by leveraging its predictive capabilities after being trained with a pre-determined LEO satellite orbital pattern. This simplification eliminates the propagation delay incurred during the MR phase, while still providing effective HO decisions. The proposed DHO outperforms the legacy HO protocol across diverse network conditions in terms of access delay, collision rate, and handover success rate, demonstrating the practical applicability of DHO in real-world networks. Furthermore, the study examines the trade-off between access delay and collision rate and also evaluates the training performance and convergence of DHO using various DRL algorithms.

Index Terms— LEO satellite network, handover, protocol learning, deep reinforcement learning, 6G.

# I. INTRODUCTION

N THE realm of beyond-5G and 6G networks, satellite I constellations utilizing low-Earth orbit (LEO) and medium-Earth orbit (MEO) satellites (SATs) have emerged as a crucial solution for providing global coverage. These constellations, composed of thousands of SATs in close proximity to the Earth, enable high-speed, low-latency broadband internet access in remote and underserved areas across the globe [1], [2]. However, as the number of SATs in mega-constellation networks continues to rise and these networks are increasingly utilized for a diverse range of applications, there is a corresponding increase in the number of devices attempting to access the network, known as massive access. This can lead to a potential for network congestion and an

Manuscript received 30 July 2023; revised 21 October 2023 and 4 December 2023; accepted 4 December 2023. Date of publication 21 December 2023; date of current version 12 July 2024. This work was supported by the Institute of Information & Communications Technology Planning & Evaluation (IITP) Grant funded by the Korea Government through the Ministry of Science and ICT (Information and Communications Technology) (Development of Artificial Intelligence (AI) Bots Collaboration Platform and Self-Organizing AI) under Grant 2022-0-00907. The associate editor coordinating the review of this article and approving it for publication was D. Niyato. (Corresponding author: Soohyun Park.)

Ju-Hyung Lee and Andreas F. Molisch are with the Ming Hsieh Department of Electrical and Computer Engineering, University of Southern California, Los Angeles, CA 90007 USA (e-mail: juhyung.lee@usc.edu; molisch@usc.edu).

Chanyoung Park and Soohyun Park are with the School of Electrical Engineering, Korea University, Seoul 02841, South Korea (e-mail: cosdeneb@korea.ac.kr; soohyun828@korea.ac.kr).

Digital Object Identifier 10.1109/TWC.2023.3342975

increase in latency, which is a significant concern in these networks [3], [4], [5].

Since massive access may negatively impact network performance, new approaches are required to handle it [6]. Conventional transparent-type LEO SAT, which relies on centralized reservation methods, where a limited number of ground stations manage various functions such as handover (HO) and resource allocation for all user equipment (UEs) connected to the mega-constellation, may not be efficient in handling this massive access scenario. To overcome this limitation, regenerative-type LEO SAT has emerged, which is capable of making decisions and performing functions without relying on ground stations1 [7]. However, applying traditional HO protocols used in terrestrial networks to regenerative-type LEO SAT networks may not be optimal as these protocols were not designed for the high dynamics of LEO SAT networks or the long propagation delay encountered in them, leading to unnecessary delay and power consumption from burdensome HO procedures.

In this paper, we propose a novel HO protocol specifically designed for the regenerative-type LEO SAT networks using the deep reinforcement learning (DRL) approach. Our contributions can be summarized as follows:

• A novel HO protocol is proposed for the LEO SAT networks, called DHO. DHO re-designs conventional HO procedures to suit LEO SAT network requirements. The protocol leverages locally observable information, tailored to the unique characteristics of LEO SAT networks.

• The proposed DHO protocol minimizes access delay and collision rate while simplifying the HO process by skipping the Measurement Report (MR), achieving better performance even with lower power consumption. The DHO employs the importance-weighted Actor-Learner architecture, IMPALA algorithm [8], which ensures stable training of cases with large state and action spaces (see Sec. IV-E) compared to other DRL algorithms (see Appendix B).

• Numerical results corroborate that the DHO protocol demonstrates its superiority under various conditions over conventional HO protocol, achieving up to 6.86x and 4.18x lower access delay than conventional HO and

1Transparent-type SATs function by amplifying and forwarding signals, while regenerative-type SATs possess the capability for on-board processing (OBP) and are able to perform functions, such as HO decision [7].

heuristic methods, respectively, (see Table IV and V in Sec. V). Also, the DHO agent behavior (trained policy) reveals the underlying mechanism for its improved performance and its adaptability in various network scenarios (see Table VI in Sec. V).

• Furthermore, the versatility of the DHO protocol in adapting to different network scenarios is also demonstrated (see Table VII in Sec. V).

The rest of the paper is organized as follows: After discussing the related works on HO processes for LEO SATbased non-terrestrial networks (NTN) in Sec. II, Sec. III provides a background and covers the challenges of HO in LEO SAT networks. Sec. IV presents the proposed DHO algorithm and its evaluation method. Sec. V provides simulation results and performance analysis, followed by concluding remarks in Sec. VI.

Notation: Throughout this paper, we use the normal-face font to denote scalars, and boldface font to denote vectors. We use $\mathbb { R } ^ { D \times 1 }$ to represent the D-dimensional space of real-valued vectors. $\nabla _ { \mathbf x } f ( \mathbf x )$ denotes the gradient vector of function f (x).

# II. RELATED WORKS

Various HO strategies have been proposed to address the challenges posed by HO in LEO SAT networks. One such strategy employs a graph theory-based approach, where the relationship between LEO SAT and UE is represented as a graph and node [9], [10], [11], [12]. While this graph-based approach has the potential to find efficient HO decisions, it is only applicable to the central reservation method in transparent-type LEO SAT networks, but not for the regenerative-type LEO SAT networks, which require realtime decisions to be made through on-board processing.

To address this limitation, DRL can be used to make realtime decisions. The use of DRL in wireless communications has been extensively studied, as reviewed in [13]. For instance, in dynamic spectrum sensing/access in cognitive radio, DRL has been applied to determine appropriate spectrum access strategies [14], [15], [16]. Furthermore, the use of DRL can be extended to random access performance improvements in LEO SAT networks [17], [18], [19]. In the context of LEO SAT networks, some studies have applied DRL to improve resource allocation and capacity management, which, however, primarily focus on central decisions [20], [21], [22].

Several studies have also investigated the application of machine learning in HO procedures [23], [24], [25], [26]. For instance, [24] utilizes a DRL methodology in certain HO processes, although in a centralized manner. Reference [25] aims to optimize both beamforming and HO jointly but only addresses the HO process at a high level without consideration for detailed HO procedures. Reference [26] employs a supervised learning approach to enhance the predictive capability of a specific HO procedure; however, this approach yields limited improvements and heavily relies on a data-driven approach. Although previous studies demonstrate the potential of machine learning integration in the HO process, they primarily employ methods that are either too high-level or overly specialized; besides, these studies do not sufficiently account for the dynamic environments typical of NTN.

![](images/b5f9117d455648ec558bed4661e2c4658c4977321c1a199d4dc3b43d22d41466.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["UE"] --> B["HO Event"]
    B --> C["HO Decision"]
    C --> D["HO Admission"]
    D --> E["SN Status Transfer"]
    E --> F["RACH"]
    F --> G["Switch Path"]
    G --> H["HO Complete"]
    I["serving-gNB"] --> J["HO Request"]
    K["target-gNBs"] --> L["HO Request ACK"]
    M["Preparation"] --> N["Measurement Report"]
    O["Execution"] --> P["Random Preamble"]
    Q["Completion"] --> R["Random Access Response"]
    S["Execution"] --> T["RRC Connection Request"]
    U["Execution"] --> V["Contention Resolution"]
    W["Execution"] --> X["HO Confirm"]
    Y["Execution"] --> Z["HO Command"]
```
</details>

Fig. 1. The sequence diagram of conventional HO procedure.

Considering the outlined approaches, our research aims to enhance the DRL-based approach, particularly focusing on HO in LEO SAT networks. We propose a novel DRL-based HO protocol designed to enable efficient real-time decisionmaking, thereby broadening the scope of DRL-based solutions within LEO SAT network contexts.

# III. HANDOVER FOR LEO SAT-BASED NON-TERRESTRIAL NETWORKS

# A. Overview of HO Process

As mentioned previously, transparent-type LEO SATs mainly operate on schedule-based HO mechanisms, such as centralized reservation methods. In these methods, a limited number of ground stations manage various functionalities, including HO and resource allocation for all UEs connected to thousands of LEO SATs. However, in this paper, our primary focus is on another type of platform, regenerativetype LEO SAT. This type of platform is capable of making autonomous decisions and employs a trigger-based HO process, corresponding to the conventional HO process utilized in the 3GPP New Radio (NR).

HO in 3GPP NR, the primary 5G cellular standard, consists of three main phases: preparation, execution, and completion [26]. This process, shown in Fig. 1, ensures the continuous transfer of data sessions or calls when a UE moves from one cell to another [27].

Preparation phase. During the preparation phase, the UE measures signals from the serving and target Node Bs (gNBs), deciding if a HO event is necessary based on five potential conditions outlined in Table I. The handover margin (HOM) and time-to-trigger (TTT) are used to evaluate these conditions. If satisfied, the UE sends a MR to the serving-gNB, leading to a HO Request to the target-gNB. If accepted, the serving-gNB sends a HO Command to the UE, moving to the execution phase.

TABLE I THE ENTERING CONDITIONS OF HO EVENT 

<table><tr><td>Event</td><td>Entering Condition</td></tr><tr><td>A1</td><td>serving-gNB&#x27;s signal becomes stronger (better) than the thresholda.</td></tr><tr><td>A2</td><td>serving-gNB&#x27;s signal becomes weaker (worse) than the threshold.</td></tr><tr><td>A3</td><td>target-gNB&#x27;s signal becomes stronger (better) than serving-gNB&#x27;s signal by a margin of the offset value.</td></tr><tr><td>A4</td><td>target-gNB&#x27;s signal becomes stronger (better) than the threshold.</td></tr><tr><td>A5</td><td>serving-gNB&#x27;s signal becomes weaker than threshold 1, and target-gNB&#x27;s signal becomes stronger than threshold 2.</td></tr></table>

“Event A1 is mainly used to stop the measurement of a certain cell rather than triggering the HO.

Execution phase. In the execution phase, the serving-gNB transfers the UE’s data and a sequence number to the targetgNB [28], and the UE connects to the target-gNB through a random access channel (RACH) process [29], [30]. The UE sends a HO Confirm message when the connection is successful.

Completion phase. The completion phase includes the network entities’ request to switch the packet path from the serving-gNB to the target-gNB, releasing the resources from the serving-gNB once the HO Complete message is transmitted.

The HO process, particularly the preparation phase, is vulnerable to failure under conditions of poor signal quality, where issues such as transmission/reception failure of HOrelated messages or radio link failure (RLF) can occur. Considering the increased vulnerability in the preparation phase in LEO SAT-based NTN, which often faces challenging channel conditions due to their ultra-long link distance, our work focuses on enhancing this initial stage of the HO process.

# B. Challenges in LEO SAT-Based NTN

In LEO SAT-based NTN, HO poses unique challenges compared to terrestrial cellular networks. These challenges include:

1) Long propagation delay: The signal from a UE to an SAT and back to a ground station takes a significant amount of time, leading to delays in the HO process.   
2) Large coverage area: The coverage area of SAT is much larger than that of a terrestrial cell, which can make it more difficult to identify the best target gNB for HO.   
3) Limited resources: The limited resources available on SAT can make it harder to support HO, especially when multiple UEs need to conduct HO at the same time.

As a result of these challenges, HO in LEO SAT networks is considered a more challenging process than the one in terrestrial cellular networks.

1) Challenge: Outdated, Power-Consuming, and Unreliable MR: Specific challenges in LEO SAT networks are the outdated, power-consuming, and unreliable MR. The transmission of the signaling is hampered by a long propagation delay,

which is a result of the physical distance between the ground UE and the LEO SAT providing network services at an altitude of 500 ∼ 2000 [km]. As the propagation speed is constant $( e . g . , \ c \ = \ 2 . 9 9 7 \times 1 0 ^ { 8 } )$ , the propagation delay is proportional to the distance between the two terminals. The one-way propagation delay can be as long as 1.6 ∼ 6 [ms], as shown in Fig. 2a, which can result in MR sent from ground UE to LEO SAT becoming outdated.

Additionally, the long link distance between the UE and LEO SAT necessitates high uplink (UL) signal power consumption during the MR. By calculating the carrier-to-noise ratio (CNR), it is possible to see the required UL transmit power for the UE to periodically transmit signaling to the LEO SAT to report the HO condition and also to estimate its reliability.

For the NTN scenario, CNR can be calculated as:

$$
\begin{array}{l} \mathrm{CNR} [ \mathrm{dB} ] = \mathrm{EIRP} [ \mathrm{dBW} ] - P _ {\mathrm{FS}} [ \mathrm{dB} ] - P _ {\mathrm{A}} [ \mathrm{dB} ] \\ - P _ {\mathrm{SM}} [ \mathrm{dB} ] - P _ {\mathrm{SL}} [ \mathrm{dB} ] + G / T [ \mathrm{dB} / \mathrm{K} ] \\ - k [ \mathrm{dBW/K/Hz} ] - B [ \mathrm{dBHz} ], \tag {1} \\ \end{array}
$$

where EIRP is the equivalent, isotropically radiated power (EIRP) in the transmitter (TX); $\begin{array} { c c l } { P _ { \mathrm { F S } } } & { = } & { 2 0 \log _ { 1 0 } ( f ) \ + } \end{array}$ $2 0 \log _ { 1 0 } ( d ) + 9 2 . 4 5$ with being the carrier frequency f in GHz and the link distance d in km; $P _ { \mathrm { A } }$ is the atmospheric path loss due to gases and rain fades in between groud-to-space; PSM is a shadowing margin; $P _ { \mathrm { S L } }$ is scintillation loss; G/T is is antenna-gain-to-noise-temperature in the receiver (RX); k is the theoretical noise floor or the minimum sensitivity of the receiver as the Boltzmann constant; B is the channel bandwidth. Here, for the UL communication between the LEO SAT at an altitude of 600 [km] and the ground UE, the S-band (2 [GHz]) is considered for handheld-type UE and Ka-band (30 [GHz]) is considered for VSAT-type UE. Note that the parameter values for (1) are summarized in Table. II.

Fig. 2 highlights the challenges faced in the traditional HO process, which can result in significant power consumption for the UE in the uplink transmission, as well as low reliability, due to the procedure of sending the MR.

2) Challenge: High Correlation and Density of Ground UEs: In LEO SAT networks, handling massive HO requests for UEs in densely populated areas poses another challenge, as there is a high correlation among UEs in such areas, as shown in Fig. 3. For instance, in scenarios where ground UEs are situated in a street canyon, they may encounter simultaneous loss and gain of line-of-sight due to the overhead passage of the SAT. As a consequence, the probability of collision increases when multiple UEs attempt to execute HO simultaneously. This high correlation leads to many simultaneous requests from UEs (e.g., A3 events for multiple UEs occurring simultaneously), resulting in a high collision rate and prolonged access delays, negatively impacting network performance. To tackle this challenge, an efficient and effective HO protocol is needed to manage such a large volume of HO requests, minimize the collision rate and access delay, and ensure a high HO success rate. To this end, we propose a novel HO protocol to address these issues, which will be discussed in the following.

![](images/e1a34e81e48f9b878bccf78830e7cd057a5ca11e2834e3c711de1b2419503d19.jpg)

<details>
<summary>line</summary>

| Link Distance [km] | Propagation Delay [ms] |
| ------------------ | ---------------------- |
| 600                | 2                      |
| 1800               | 6                      |
</details>

![](images/d5a926a9784b9a42883962322b8456842d09da107abaaa18b59ef0c485564757.jpg)

<details>
<summary>line</summary>

| Link distance [km] | Uplink CNR [dB] |
| ------------------ | --------------- |
| 600                | 25              |
| 1800               | 14              |
</details>

![](images/f005811e89ff5391b071908eff8ac17f6afd18cb0470d73832b75706cf9dbda4.jpg)

<details>
<summary>line</summary>

| Link distance [km] | Uplink CNR [dB] |
| ------------------ | --------------- |
| 600                | 9.0             |
| 1800               | -2.0            |
</details>

Fig. 2. Propagation delay, CNR, and BER in networks between ground UE and LEO SAT. Each result is calculated by the parameters specified by [7], respectively.

TABLE IIPARAMETERS OF UL TRANSMISSION IN LEO SAT NETWORKS(SEE TABLES VI.1.1.1-1 AND 6.1.1.1-3 OF [7])

<table><tr><td>Parameter</td><td>Value (Handheld)</td><td>Value (VSAT)</td></tr><tr><td>Carrier frequency,  $f$ </td><td>2 [GHz] (S-band)</td><td>30 [GHz] ( $K_a$ -band)</td></tr><tr><td>Bandwidth,  $B$ </td><td>0.4 [MHz]</td><td>400 [MHz]</td></tr><tr><td>TX transmit power</td><td>200 [mW] (23 [dBm])</td><td>2 [W] (33 [dBm])</td></tr><tr><td>TX antenna gain,  $G_T$ </td><td>0 [dBi]</td><td>43.2 [dBi]</td></tr><tr><td>Atmospheric loss,  $P_A$ </td><td>0.1 [dB]</td><td>0.5 [dB]</td></tr><tr><td>Shadowing margin,  $P_{SM}$ </td><td>3 [dB]</td><td>0 [dB]</td></tr><tr><td>Scintillation loss,  $P_{SL}$ </td><td>2.2 [dB]</td><td>0.3 [dB]</td></tr><tr><td> $G/T$ </td><td>1.1 [dB/K]</td><td>13 [dB/K]</td></tr><tr><td>Boltzmann constant,  $k$ </td><td></td><td>-228.6 [dBW/K/Hz]</td></tr></table>

# IV. DRL-BASED HANDOVER PROTOCOL FOR LEO SATELLITE NETWORKS

Existing HO methods for LEO SAT networks are limited by long propagation delays and high power consumption for uplink signaling. To address these issues, we propose a DRL-based HO protocol in which the serving-gNB agent predicts the UE’s network signal information and sends a HO Request to the target-gNB without the need for a MR. This simplifies the HO preparation phase and improves HO performance by overcoming long propagation delays while saving signaling power. Fig. 4 illustrates the proposed protocol. In this section, we introduce the LEO SAT network scenario, evaluation metrics, and detailed protocol design.

# A. Network Scenario

Configuration of LEO SATs and Ground UEs. Consider a set K of orbital planes around Earth. For each orbital plane $k \in \mathcal { K }$ , there is a set $\mathcal { T } _ { k }$ of LEO SATs orbiting on that plane. Additionally, there is a set J of UEs deployed on the ground2 inside an area A. The position of UE $j \in \mathcal I$ is expressed as a 3-dimensional real vector on Cartesian coordinates denoted by $\pmb { q } _ { j } ~ = ~ ( q _ { j } ^ { x } , q _ { j } ^ { y } , q _ { j } ^ { z } ) ~ \in ~ \mathbb { R } ^ { 3 }$ . Similarly, the position and velocity of SAT i at time $t ~ \geq ~ 0$ are denoted by $\begin{array} { r l } { \mathbf { q } _ { i } ( t ) \ = } \end{array}$ $( q _ { i } ^ { x } ( t ) , q _ { i } ^ { y } ( t ) , q _ { i } ^ { z } ( t ) ) \in \mathbb { R } ^ { 3 }$ and ${ \pmb v } _ { i } ( t ) = ( v _ { i } ^ { x } ( t ) , v _ { i } ^ { y } ( t ) , v _ { i } ^ { z } ( t ) ) \in$ $\mathbb { R } ^ { 3 } .$ , respectively. The set of all SATs is denoted by $\cup _ { k \in \mathcal { K } } \mathcal { T } _ { k }$ . We assume that the number of SATs on each orbital plane is equal to each other, given as $| \mathcal { T } _ { k } | = I$ for all $k \in \mathcal { K }$ , and all SATs are moving in a uniform circular motion with the same orbital period T which is an acceptable approximation for the duration of visibility of the SAT to the UE. The arc length between any two neighboring SATs on the same orbital plane is also assumed to be equal to each other.

Consider that time is discretized in slots of length τ . Let $\mathbf { \boldsymbol { q } } _ { i } [ 0 ]$ be the initial position of the SAT $i \in \cup k \in \mathcal { K } \mathcal { T } _ { k }$ at time t = 0. Then, by following the discrete-time state-space model [31], [32], the position of SAT i at time t = mτ can be expressed as

$$
\boldsymbol {q} _ {i} [ m ] = \boldsymbol {q} _ {i} [ 0 ] + \tau \sum_ {m ^ {\prime} = 1} ^ {m} \boldsymbol {v} _ {i} [ m ^ {\prime} \tau ]. \tag {2}
$$

HO Procedure. Consider LEO SAT HO scenario, where UEs in the cell O connect to a serving-SAT, which is acting as a serving-gNB. There are other SATs in the field-of-view (FoV) that are candidates for the HO target, referred to as targetgNBs (or target-SATs), and the serving-SAT can initiate a HO request to the target-SATs if it estimates it necessary. Suppose that the source-SAT and target-SATs are the closest SATs on each orbital plane for the UEs in A. Suppose that there are N HO opportunities during an interval T , after which a UE loses connectivity with the serving-SAT unless it successfully conducts a HO to a target-SAT. The time duration of each HO time slot is $\begin{array} { r } { \tau = \frac { T } { N } } \end{array}$ , such that $\tau \in \mathbb { Z } ^ { + }$ . For simplicity, we will focus only on the N HO opportunities in the rest of this section, and suppose the first time slot starts at $t = 0$ . Here, the time duration of each n-th HO is discretized with $\tau , i . e . , t = n \tau , \forall n \in \{ 1 , 2 , \ldots , N \}$ .

At each HO opportunity, each UE decides whether to send a HO Request and, if so, selects target-SATs to which it will send it. Such a set of actions is represented by $\{ 0 , 1 , \ldots ,$

2Our primary focus is on fixed VAST-type UEs, but mobile handheld-type UEs can also be considered with minor adjustments.

![](images/9a2020bdae30ac085d2bc811fdc17b0bf1ae761fd69919c2d1183866bdc70318.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["serving-SAT"] -->|HO Request| B["target-SAT1"]
    B --> C["target-SAT2"]
    C --> D["orbital plane"]
    D --> E["ground UEs"]
    F["Measurement Report"] --> B
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
```
</details>

Fig. 3. Network scenario. UEs are required to perform HO, transitioning their connections from the serving-SAT to either target-SAT1 or target-SAT2.

$K - 1 \}$ , where $K : = | { \mathcal { K } } |$ is the number of orbital planes and $k = 0$ corresponds to the serving-SAT. The HO action of UE $j \in \mathcal I$ at the n-th HO opportunity is denoted by

$$
a _ {j} [ n ] \in \{0, 1, \dots , K - 1 \}. \tag {3}
$$

Note that $a _ { j } [ n ] = 0$ means that the serving-SAT does not send a HO Request to any target-SAT at the n-th HO opportunity and waits for the next one. Also, note that there can be no HO to another SAT on the same orbital plane.

Successful HO or Collision. There can be two types of collisions in the LEO SAT HO scenario:

1) negative acknowledgment (NACK) due to lack of resource blocks (RBs): If the number of received HO Request sent by serving-SAT is greater than the number of RBs in the target-SAT, collisions will occur.   
2) physical random access channel (PRACH) collision: Collisions occur if multiple UEs that receive the HO Command attempt to access the same target-SAT with the same preamble signature.

Note that once UEs receive the HO Command, the random access (RA) signaling is carried out in two steps, as specified in Release 16 of 5G-NR [33]. Specifically, UEs select a preamble from a set of available preambles for each target-SAT uniformly at random, represented by $p _ { k } [ n ] \in$ $\{ 1 , 2 , \ldots , P \} , \forall k \in \{ 1 , \ldots , K - 1 \}$ , where $P$ represents the number of resources that each SAT can grant during the data transmission duration. In the first step of the RA signaling process, UEs that have determined to access send preambles to the corresponding SATs. In the second step, SATs send feedback to confirm whether there were collisions or not for each chosen preamble. UEs that have chosen colliding preambles fail to access, while those that have chosen preambles without collision succeed in completing the HO, i.e., HO Completion, which is denoted by a binary indicator $a _ { j } ^ { \mathrm { H O } } [ n ]$ . Specifically, $a _ { j } ^ { \mathrm { H O } } [ n ] = 1$ indicates the HO has been completed for UE j, while $a _ { j } ^ { \mathrm { H O } } [ n ] = 0$ indicates the HO has not been completed for UE $j$ at time slot n and $a _ { j } ^ { \mathrm { H O } } [ 0 ] = 0 , \ \forall j$ .

# B. Evaluation

The performance of HO in the LEO SAT networks can be evaluated mainly in terms of collision rate and access delay, as explained in the following.

1) Collision Rate: The collision rate is a measure of the proportion of unsuccessful HO attempts, which can occur due to two factors: NACK due to lack of RBs and PRACH collision.

Collision (NACK due to lack of RBs). This type of collision occurs when there are not enough RBs available on the target-SAT to support the number of UEs attempting to access it. We can represent each HO Request by defining the request indicator $\bar { h } _ { k , j } ^ { \mathrm { R } } [ n ]$ for UE $j \in \mathcal { I }$ attempting to access target-SAT $k \in \mathcal { K }$ at n:

$$
h _ {k, j} ^ {\mathrm{R}} [ n ] = \left\{ \begin{array}{l l} 1 & a _ {j} [ n ] > 0, a _ {j} ^ {\mathrm{HO}} [ n ] = 0, \\ 0 & \text { otherwise }, \end{array} \quad \forall j \in \mathcal {J}, k \in \mathcal {K}. \right. \tag {4}
$$

We can then calculate the collision rate $C _ { k } ^ { \mathrm { R } } [ n ]$ for this type of collision as the ensemble proportion of UEs that attempted to access a target-SAT $k \in \mathcal { K } \backslash \{ k = 0 \}$ with insufficient RBs:

$$
C _ {k} ^ {\mathrm{R}} [ n ] = \left\{ \begin{array}{l l} 0 & \mathrm{R} _ {k} [ n ] - \sum_ {j = 1} ^ {J} h _ {k, j} ^ {\mathrm{R}} [ n ] > 0, \\ \frac {\sum_ {j = 1} ^ {J} h _ {k , j} ^ {\mathrm{R}} [ n ] - \mathrm{R} _ {k} [ n ]}{J} & \text { otherwise }, \end{array} \right. \tag {5}
$$

where $\mathrm { R } _ { k } [ n ]$ represents the available RBs in target-SAT k at time slot n, and $\mathsf { \bar { c } } _ { j } ^ { \mathrm { R } } [ n ]$ indicates the collision due to insufficient RBs for $\mathrm { U E } ~ j \in \mathcal { T }$ at time slot n. In the event of a collision due to insufficient RBs in the target-SAT, the UE that will receive the HO Request acknowledgment (ACK) is selected randomly based on the availability of the RBs. To identify the UE that receives the HO Command, we define the command indicator $h _ { j } ^ { \mathrm { C } } [ n ] \in \{ 0 , 1 , \ldots , K - 1 \} . ~ h _ { j } ^ { \mathrm { C } } [ n ] = 0$ indicates that the UE has not received any HO Command, while $h _ { j } ^ { \mathrm { C } } [ n ] = k$ indicates that the UE has received the command for target-SAT k .

Collision (PRACH collision). This is another type of collision that occurs when multiple UEs attempt to access the same SAT with the same preamble signature.

Denote the collision indicator of UE $j \in \mathcal { T } ^ { \prime } \mathrm { s } \ \mathrm { R A }$ at time slot $n \in \{ 1 , \ldots , N \}$ by $c _ { j } ^ { \mathrm { P } } [ n ]$ , and define it as

$$
c _ {j} ^ {\mathrm{P}} [ n ] = \left\{ \begin{array}{l l} 1 & (h _ {j} ^ {\mathrm{C}} [ n ], p _ {j} [ n ]) = (h _ {j ^ {\prime}} ^ {\mathrm{C}} [ n ], p _ {j ^ {\prime}} [ n ]), a _ {j} ^ {\mathrm{HO}} [ n ] = 0, \\ 0 & \text { otherwise }, \end{array} \right. \tag {6}
$$

if $a _ { j } [ n ] \neq 0$ , and otherwise we have $c _ { j } ^ { \mathrm { P } } [ n ] = 0 .$

The collision rate $C ^ { \mathrm { P } } [ n ]$ is defined as the ensemble proportion of UEs that experienced a PRACH collision and is calculated by averaging $c _ { j } ^ { \mathrm { P } } [ n ]$ over all UEs in $\mathcal { I } _ { : }$ , which is defined as

$$
C ^ {\mathrm{P}} [ n ] = \frac {1}{| \mathcal {J} |} \sum_ {j \in \mathcal {J}} c _ {j} ^ {\mathrm{P}} [ n ]. \tag {7}
$$

Finally, the average collision rate $C [ n ]$ is calculated by summing the collision rate for the lack of RBs $C _ { k } ^ { \mathrm { R } } [ n ]$ over all target-SATs $k \in \mathcal { K } \backslash \{ k = 0 \}$ and adding the PRACH collision rate $C ^ { \mathrm { P } } [ n ]$ :

$$
C [ n ] = \sum_ {k = 1} ^ {K - 1} C _ {k} ^ {\mathrm{R}} [ n ] + C ^ {\mathrm{P}} [ n ]. \tag {8}
$$

Note that a UE cannot experience both types of collisions (NACK due to lack of RBs and PRACH collisions), simultaneously. This is due to the fact that the UE initiates the RA process only after receiving the HO Command, which is sent by the serving-SAT upon receiving the HO Request ACK from the target-SAT. Thus, the RA process can only be initialized when there is no collision in terms of NACK due to lack of RBs.

2) Access Delay: Access delay is another metric in HO scenarios that measures the time it takes for a UE to successfully HO to a target-SAT. The access delay is calculated as the average time it takes for a UE to successfully access a target-SAT, taking into account the number of failed attempts and the time duration between each time slot.

The average access delay is then calculated as:

$$
D [ n ] = \frac {1}{| \mathcal {J} |} \sum_ {j \in \mathcal {J}} (1 - a _ {j} ^ {\mathrm{HO}} [ n ]), \tag {9}
$$

This calculation takes into account the total number of failed HO and the time duration between each time slot to provide an accurate measure of the average access delay.

3) Successful HO (Access) Rate: The successful HO rate is a metric that measures the proportion of UEs that successfully hand over to a target-SAT among all UEs that attempted to do so. It is calculated as the average of the access indicator of all UEs:

$$
H = \frac {1}{| \mathcal {J} |} \sum_ {j \in \mathcal {J}} a _ {j} ^ {\mathrm{HO}} [ N ]. \tag {10}
$$

# C. Protocol Design

In this section, we propose a novel HO protocol for LEO SAT networks, called DHO. As the DHO utilizes DRL techniques for training, we first formulate the problem and cast the problem into a Markov decision process (MDP) model.

1) Sequence of DHO: The proposed DHO protocol for LEO SAT networks includes the following sequence of steps:

1) HO Decision: serving-SAT makes a decision for HO Request, including target-SAT selection and backoff for each UE.   
2) HO Admission: target-SAT sends HO Request ACK if it has available RBs to support the HO request. The serving-SAT then sends HO Command to the UEs that are permitted to hand over to the target-SAT.   
3) Random Access: UEs that receive HO Command attempt to access the target-SAT designated by the serving-SAT, by randomly choosing preambles for RACH access.

4) HO Completion: Completing HO if the UE successfully transfers to the target-SAT specified by the serving-SAT.

Notably, the proposed DHO protocol simplifies the process by eliminating the need for the MR.

To achieve our objective, we employ the DRL approach, driven by two crucial factors: Firstly, the DRL algorithm has the ability to handle complex, high-dimensional decisionmaking problems, making it a suitable choice for optimizing HO procedure in LEO SAT networks. Secondly, the environment in LEO SAT networks is dynamic and stochastic, characterized by rapidly changing network conditions. The DRL algorithm is capable of adapting to these fluctuations and making decisions in real-time, whereas other optimization techniques, such as convex optimization or dynamic programming, may not be equipped to handle such a complex and unpredictable environment.

2) MDP Modeling: The optimization problem mathematically formulated in DHO is to minimize both access delay and collision rate while taking into account the constraints of LEO SAT networks. The problem can be represented as:

$$
\min _ {a _ {j} [ n ]} \sum_ {n = 1} ^ {N} D [ n ] + \nu C [ n ], \text {   s.t.   (2) }. \tag {11}
$$

where ν is a normalization coefficient that balances the tradeoff between access delay and collision rate, and N is the period of time during which HO may occur.

To recast the problem in (11) as a DRL problem, in the following, we first model the network scenario of LEO SATbased NTN as an MDP.

Environment. Environment consists of ground UEs, serving-SAT, and target-SATs interacting with each other, which follows an MDP model. At each time step n, the serving-SAT is an agent that observes a state $\mathbf { s } [ n ] \in { \mathcal { S } } ,$ , and takes action $\mathbf { a } [ n ] \in { \mathcal { A } }$ based on a state-action policy π. Given this action, the state of the agent transitions to $\mathbf { s } [ n + 1 ]$ , and in return, the agent receives a reward $r [ n ]$ that reinforces following an optimal policy $\pi ^ { * }$ .

State. In the MDP model, the state at time index n is defined as:

$$
\mathbf {s} [ n ] = \{n, \boldsymbol {a} ^ {\mathrm{HO}} [ n ], \mathbf {a} [ n - 1 ] \}, \tag {12}
$$

where n represents the time index, $\begin{array} { r l } { { \pmb a } ^ { \mathrm { H O } } [ n ] } & { { } = } \end{array}$ $\{ a _ { 1 } ^ { \mathrm { H O } } [ n ] , a _ { 2 } ^ { \mathrm { H O } } [ \dot { n } ] , \cdot \cdot \cdot , a _ { J } ^ { \mathrm { H O } } [ n ] \}$ , and $\mathbf { a } [ n - 1 ]$ is the previous action taken by the UEs. The inclusion of the time index and previous action serves as a fingerprint for stabilizing experience replay in the DRL process. Besides, the binary indicator of accessed UEs provides information on the current state of the network. Note that s[0] represents the state for $n = 0 ,$ , which is initialized randomly.

The state information is designed to be minimal while still providing sufficient information for decision-making. Each piece of information in the state is carefully selected through extensive tests, as shown in our ablation study in Appendix A. It is worth noting that our proposed DHO utilizes the locally-observable information and does not require additional information, such as the position of the SATs or others, as the accessed UEs provide sufficient information for DHO training. This minimal state design not only reduces data collection overhead but also enhances the convergence of DRL training.

![](images/100ac3525ac29197c458582ea0e3615558fdc28c453adda31c68bd2b589ce200.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["UEs"] --> B["HO Event"]
    B --> C["HO Decision"]
    C --> D["HO Admission"]
    D --> E["Synchronization & Random Access"]
    E --> F["HO Completion"]
    G["serving-SAT"] --> C
    H["target-SATs"] --> D
    I["TTT"] --> B
    J["Measurement Report"] --> C
    K["HO Request"] --> D
    L["HO Request ACK"] --> D
    M["HO Command"] --> E
```
</details>

(a) Conventional HO protocol.

![](images/29477aa53b99e7d3f8b4d3544285cd80a1aa31e0b5af247ec3e9684737e36582.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["UEs"] --> B["serving-SAT"]
    B --> C["target-SATs"]
    C --> D["DRL-based HO Decision"]
    D --> E["HO Request"]
    E --> F["HO Admission"]
    F --> G["HO Request ACK"]
    G --> H["Synchronization & Random Access"]
    H --> I["HO Completion"]
    I --> J["HO Command"]
    J --> D
```
</details>

(b) Proposed DRL-based HO protocol (DHO)   
Fig. 4. The sequence diagrams of traditional and proposed HO protocols for LEO SAT networks.

Action. The action space A in our environment pertains to HO decisions. In order to determine the HO Request for each UE at each HO opportunity, our agent, representing the serving-SAT, employs the HO action $a _ { j } [ n ]$ as defined in (3).

To define the set of HO actions, A, we utilize a one-hot encoded representation. Specifically, we define the set of HO actions for UE j at time index n as:

$$
\mathbf {a} _ {j} [ n ] = \left\{a _ {0}, a _ {1}, a _ {2}, \dots , a _ {K - 1} \right\}, \text {   s.t.   } \sum_ {k = 0} ^ {K - 1} a _ {k} = 1, \tag {13}
$$

where $a _ { k }$ for $k \neq 0$ denotes the association with the $k \mathrm { - }$ th orbital plane, and $a _ { 0 }$ implies that the serving-SAT does not send a HO Request to any target-SAT at the n-th HO opportunity and instead waits for the next one. This onehot encoded representation ensures that exactly one action is selected at each time step, and allows for a clear and efficient representation of the HO decisions made by the agent. Thus, the complete set of action is given as:

$$
\mathbf {a} [ n ] = \left[ \begin{array}{c} \mathbf {a} _ {1} [ n ] \\ \mathbf {a} _ {2} [ n ] \\ \vdots \\ \mathbf {a} _ {J} [ n ] \end{array} \right]. \tag {14}
$$

Reward. The reward function in our proposed DHO is designed to reinforce the serving-SAT to make optimal access decisions by penalizing access delay and collision rate. The reward function, $r [ n ]$ , is defined as the negative of the objective function in (11), which captures this goal:

$$
r [ n ] = - D [ n ] - \nu C [ n ]. \tag {15}
$$

Here, the normalization coefficient ν balances the tradeoff between access delay and collision rate, which will be discussed in Sec. V-D, specifically in Table VII.

It is worth noting that the state and reward information used in our MDP model is locally observable, making it possible to train and execute the DHO in a fully distributed manner. This means that the regenerative type SATs can easily implement our proposed DHO.

# D. Algorithm Details

The proposed DHO employs IMPALA [8], which is a DRL algorithm that provides several advantages over other DRL algorithms, such as DQN [34], A3C [35], and PPO [36].3 IMPALA is an off-policy reinforcement learning algorithm that utilizes parallel actor-learners and importance sampling to improve sampling efficiency and scalability.

In off-policy training, the variance is largely due to the difference between the policy that is used to generate the behavior (behavior policy) and the policy that is being improved (target policy). IMPALA addresses the policy mismatch issue in off-policy learning by using V-trace targets, which are estimated using truncated importance sampling. V-trace targets correct the value estimate by incorporating the difference between the behavior policy and the target policy, which can significantly improve learning performance. IMPALA provides scalability and improved sample efficiency by employing asynchronous updates and importance sampling. It allows for efficient parallelization and effective utilization of collected data, striking a balance between exploration and exploitation. These advantageous features make IMPALA particularly suitable for large-scale environments and complex tasks, such as the HO process in LEO SAT networks.

The process of how the learner updates its policy in IMPALA is as follows:

1) Initialize and update the actor’s policy based on the current learner’s policy.   
2) The actor collects experience in environments.   
3) The actor delivers the collected experience and its policy to the learner.

3DHOs can also be trained with other DRL algorithms that support multidiscrete actions.

4) The learner trains its policy based on the experience and the actor’s policy it receives.

In IMPALA, which is an asynchronous distributed training model, even if different actors update their policies based on the same learner, they may diverge due to the inherent randomness and asynchrony of the training process.

1) V-Trace: In the context of discounted infinite-horizon RL in MDP, we aim to find a policy π that maximizes the expected sum of future discounted rewards. The value function $V ^ { \pi } ( \mathbf { s } )$ represents the expected cumulative rewards starting from state s, and it is defined as $\begin{array} { r } { E _ { \pi } \left\lceil \sum _ { n = 1 } ^ { N } \gamma ^ { t } r [ n ] \right\rceil } \end{array}$ , where $\gamma$ is the discount factor in the range [0, 1).

Consider a trajectory $( { \bf s } [ n ] , { \bf a } [ n ] , r [ n ] ] ) _ { n = s } ^ { n = s + k }$ generated by the actor following a policy $\mu .$ The k-steps V-trace target $v _ { n }$ for approximating the value at state ${ \bf s } [ n ]$ , is defined as:

$$
v [ n ] = V (\mathbf {s} [ n ]) + \sum_ {n = s} ^ {s + k - 1} \gamma [ n - s ] \left(\prod_ {i = s} ^ {n - 1} c [ i ]\right) \delta_ {n} V, \tag {16}
$$

where $\delta _ { n } V ~ = ~ \rho [ n ] \left( r [ n ] + \gamma V ( \mathbf { s } [ n + 1 ] ) - V ( \mathbf { s } [ n ] ) \right)$ is the temporal difference for V . The terms $\rho [ n ]$ and c[n] are truncated importance sampling (IS) weights, with $\rho [ n ] ~ =$ min $\left( \bar { \rho } , \frac { \pi ( \mathbf { a } [ n ] | \mathbf { s } [ n ] ) } { \mu ( \mathbf { a } [ n ] | \mathbf { s } [ n ] ) } \right)$ and $\begin{array} { r } { c [ n ] \ = \ \operatorname* { m i n } \Big ( \bar { c } , \frac { \pi ( \mathbf { a } [ n ] | \mathbf { s } [ n ] ) } { \mu ( \mathbf { a } [ n ] | \mathbf { s } [ n ] ) } \Big ) } \end{array}$ c, ¯ . It is assumed that the truncation levels satisfy ρ¯ ≥ c¯. The truncation levels c¯ and ρ¯ play different roles in the algorithm: ρ¯ impacts the nature of the value function we converge to, whereas c¯ impacts the speed at which we converge to this function.

Off-policy learning is important in the decoupled distributed actor-learner architecture because of the lag between when actions are generated by the actors and when the learner estimates the gradient. By incorporating the V-Trace target, IMPALA addresses the challenge of policy mismatch (policylag) in distributed environments, allowing for a more accurate estimation of the advantage function and improved learning performance.

2) V-Trace Actor-Critic Algorithm: Under off-policy settings, we can use the IS weight between the policy being evaluated $\pi _ { \bar { \rho } }$ and the behavior policy $\mu$ to update our policy parameter in the direction of

$$
\mathbb {E} _ {\mathbf {a} [ n ] \sim \mu (\cdot | \mathbf {s} [ n ])} \left[ \frac {\pi_ {\bar {\rho}} (\mathbf {a} [ n ] | \mathbf {s} [ n ])}{\mu (\mathbf {a} [ n ] | \mathbf {s} [ n ])} \cdot \nabla \log \pi_ {\bar {\rho}} (\mathbf {a} [ n ] | \mathbf {s} [ n ]) q [ n ] | \mathbf {s} [ n ] \right].
$$

Here, q[n] $: = \ r [ n ] + \gamma v [ n + 1 ]$ is an approximation of $Q ^ { \pi _ { \bar { \rho } } } ( \mathbf { s } [ n ] , \mathbf { a } [ n ] )$ , built from the V-trace estimate $v _ { s + 1 }$ at the next state $x _ { s + 1 }$ .

Consider a parametric representation of the value function $V _ { \phi }$ and the current policy $\pi _ { \theta }$ . Trajectories are generated by actors following a behavior policy µ. The V-trace targets v[n] are defined by the equation (16). During training, the value parameters ϕ are updated using gradient descent on the l2 loss towards the target v[n]. This update is performed in the direction of

$$
\big (v [ n ] - V _ {\phi} (\mathbf {s} [ n ]) \big) \nabla_ {\phi} V _ {\phi} (\mathbf {s} [ n ]).
$$

The policy parameters θ are updated in the direction of the policy gradient, which is given by

$$
\rho [ n ] \nabla_ {\theta} \log \pi_ {\theta} (\mathbf {a} [ n ] | \mathbf {s} [ n ]) \big (r [ n ] + \gamma v [ n + 1 ] - V _ {\phi} (\mathbf {s} [ n ]) \big).
$$

Algorithm 1 Training Process for the Proposed DHO   
1 Initialize the learner network's weights $\phi \to \phi_0$ ;

2 for Epoch = 1, MaxEpoch do

3    for each actor $i$ , $\forall i \in [1, I]$ do

4    ▷ Initialize LEO SAT Environments: Set replay buffer $\mathcal{D}_i = \{\}$ and $\mathbf{s}_i[n] \to \mathbf{s}_i[0]$ ;

5    ▷ Update actor weight $\theta_i$ from the learner: Download weights $\theta_i = \phi$ ;

6    for Step = 1, MaxStep do

7    ▷ Select the action $\mathbf{a}_i[n]$ based on its policy $\mu_{\theta_i}(\mathbf{a}_i[n] \mid \mathbf{s}_i[n])$ at every step;

8    ▷ Get reward $r_i[n]$ and move $\mathbf{s}_i[n] \to \mathbf{s}_i[n+1]$ ;

9    ▷ Set experience $\xi_i[n] = \{\mathbf{s}_i[n], \mathbf{a}_i[n], r_i[n], \mathbf{s}_i[n+1]\}$ ;

10    ▷ Update replay buffer: $\mathcal{D}_i = \mathcal{D}_i \cup \xi_i[n]$ ;

11    end

12    ▷ Upload $\mu_{\theta_i}$ and $\mathcal{D}_i$ to the learner;

13    ▷ Update weights $\phi$ of the learner network $\pi_\phi$ on the basis of $\mu_{\theta_i}$ and $\mathcal{D}_i$ ;

14    end

15 end

To prevent premature convergence, an entropy bonus, similar to A3C, can be added in the direction

$$
- \nabla_ {\theta} \sum_ {\mathbf {a}} \pi_ {\theta} (\mathbf {a} | \mathbf {s} [ n ]) \log \pi_ {\theta} (\mathbf {a} | \mathbf {s} [ n ]).
$$

The detailed process of the training is described in Algorithm 1.

# E. Complexity Analysis

In the complexity analysis, we first discuss the training complexity of the DHO, which utilizes the IMPALA algorithm for training. We then introduce the execution complexity of our proposed DHO compared to the conventional HO protocol.

Training complexity. Policy-based DRL, utilizing policy gradient, has been demonstrated to possess superior reward convergence compared to value-based DRL [37]. One example of policy-based DRL is the actor-critic algorithm, such as A2C and A3C. However, as the actor-critic network is an on-policy method, it lacks the ability to utilize an experience replay buffer, as seen in off-policy training methods like DQN [38]. This lack of experience replay buffer can lead to a higher susceptibility to converge to a local minimum or experience oscillations due to correlations between training samples and rapidly changing data distributions.

IMPALA, on the other hand, leverages off-policy multiple actors-learner distributed learning with V-Trace to provide a faster learning rate and improved performance. The use of multiple actors and a distributed learning approach also allows for the efficient utilization of computing resources, making faster convergence possible.

After training, our DRL-based HO agent, DHO, can output an action (i.e., HO Request) in less than a few milliseconds on NVIDIA GeForce RTX 3080 Ti GPU. Further details of the comparison and convergence study of the IMPALA DRL algorithm can be found in Appendix B.

Execution complexity. One of the key advantages of the proposed DHO is its simplification of the HO procedure by skipping the MR step. This simplification reduces the overall HO processing time and conserves UL signaling power that would otherwise be used for the MR in conventional HO protocols. In the DHO, the serving-SAT agent is capable of directly sending a HO Request to the target-SATs without relying on the MR. This is achieved by leveraging the serving-SAT agent’s learned understanding and prediction of the UE’s channel condition. The elimination of the MR step significantly reduces the execution complexity, enhancing the efficiency and effectiveness of the proposed DHO compared to the conventional HO protocol.

TABLE III SIMULATION PARAMETERS 

<table><tr><td colspan="2">Environment Parameter [1]</td></tr><tr><td>Region (area) of interest</td><td> $1000 \times 1000 \, [\text{m}^2]$ </td></tr><tr><td>Number of UE</td><td> $J = 10 - 200$ </td></tr><tr><td># of orbital plane</td><td>3</td></tr><tr><td>Altitude of LEO SAT</td><td> $H_{\text{L}} = 550 \, [\text{km}]$ </td></tr><tr><td>Speed of LEO SAT</td><td> $|\boldsymbol{v}| = 7.59 \times 10^3 \, [\text{m/s}]$ </td></tr><tr><td>Velocity of serving-SAT ( $k = 1$ )</td><td> $\boldsymbol{v}^k \in \{[0, |\boldsymbol{v}|, 0]^T\}$ </td></tr><tr><td>Velocity of target-SATs ( $k = 2, 3$ )</td><td> $\boldsymbol{v}^k \in \left\{ \left[ \frac{|\boldsymbol{v}|}{\sqrt{2}}, \frac{|\boldsymbol{v}|}{\sqrt{2}}, 0 \right]^T, \left[ -\frac{|\boldsymbol{v}|}{\sqrt{2}}, \frac{|\boldsymbol{v}|}{\sqrt{2}}, 0 \right]^T \right\}$ </td></tr><tr><td colspan="2">HO Parameter [39]-[41]</td></tr><tr><td>Period of measurement</td><td> $T_{\text{M}} = 150 \, [\text{ms}]$ </td></tr><tr><td>IIR filter order</td><td> $k_{\text{IIR}} = 4$ </td></tr><tr><td>Forgetting factor</td><td> $\beta_{\text{L3}} = 0.5$ </td></tr><tr><td>Period of HO update</td><td> $T_{\text{U}} = 300 \, [\text{ms}]$ </td></tr><tr><td>Offset for A3 event</td><td>1 [dB]</td></tr><tr><td colspan="2">DRL Training Parameter</td></tr><tr><td>Learning rate</td><td> $10^{-4} \sim 5 \times 10^{-4}$ </td></tr><tr><td>Discount factor</td><td> $0.85 \sim 0.99$ </td></tr><tr><td>Batch size</td><td>10000</td></tr><tr><td># of iterations per update</td><td>10000</td></tr><tr><td># of iterations per episode</td><td>20</td></tr><tr><td># of episodes for training</td><td>1000 ~ 8000</td></tr></table>

# V. NUMERICAL RESULTS

In this section, we demonstrate the effectiveness of the proposed DHO for LEO SAT networks by evaluating the performance metrics of access delay and collision rate.

# A. Simulation Setup

1) Environment: In this study, unless otherwise specified, the ground UEs are uniformly distributed within a 1000×1000 $[ \mathrm { m ^ { 2 } } ]$ area. The scenario includes one serving-SAT (k = 0) and two target-SATs (k = 1 or 2), orbiting at an altitude of 550 [km] in three different orbital planes. Given that LEO forms a spherical shape with its center corresponding with that of the Earth, the orbital speed of LEO SATs is determined based on their altitude using Kepler’s law. The FoV of the UEs in a specific area of interest (A) is assumed to cover one SAT for each orbital lane.

The parameters for conventional HO decision-making are as follows: The filtered HO measurement, ML1 [n] (i.e., received signal strength indicator (RSSI)), is updated every HO measurement period $( T _ { \mathrm { M } } )$ at the UE. The measurement $M _ { \mathrm { L } _ { 3 } } [ n ]$ is evaluated by L3 infinite impulse response (IIR) filtering of L1 received power of downlink reference signals (RSRP) measurements for each HO decision update period $( T _ { \mathrm { U } } = T _ { \mathrm { M } } / \beta _ { \mathrm { L } _ { 3 } } )$ with a forgetting factor $\beta _ { \mathrm { L } _ { 3 } } = 1 / 2 ^ { ( \bar { k _ { \mathrm { I I R } } } / 4 ) }$ , where $k _ { \mathrm { I I R } }$ is the IIR filter order. The L3 filtered measurement is given as [40] and [41]:

$$
M _ {\mathrm{L} _ {3}} [ n ] = \beta_ {\mathrm{L} _ {3}} M _ {\mathrm{L} _ {1}} [ n ] + (1 - \beta_ {\mathrm{L} _ {3}}) M _ {\mathrm{L} _ {3}} [ n - 1 ]. \tag {17}
$$

Note that in scenarios with high doppler shift and high speed, such as in the LEO SAT networks, the log-normal shadowing samples may not be highly correlated. In such cases, a shorter filtering period may result in more accurate HO decisionmaking. When the event A3 criterion is met, i.e., the L3 filtered RSRP of the target cell exceeds that of the serving cell by a predetermined hysteresis margin (referred to as the event A3 offset), the UE sends a notification to the serving cell and relays this event A3 condition through a MR, thereby initiating the HO preparation process.

Table III presents a summary of the main parameters for the environment, the network scenario, specifically those related to HO, and the DRL training.

2) Benchmark: Throughout this section, we evaluate the performance of two benchmark HO methods and our proposed LEO SAT networks-oriented HO, referred to as DHO, as outlined below:

1) HO (Conventional) protocol is a traditional method employed in 4G-LTE and 5G-NR networks. This method utilizes the A3 event to trigger ${ \mathrm { H O } } _ { \mathrm { , } } ^ { 4 }$ and the ground UE performs HO measurements using the estimated RSRP, while also applying filters to mitigate the impact of fading and measurement inaccuracies. At the start of the HO opportunity, the serving-SAT selects a target-SAT based on favorable RSRP. Additional details on this process can be found in Sec. III-A and in Table III, which lists the relevant parameters.

2) Random (Heuristic) protocol selects actions randomly for each HO opportunity in the environment. As a result, each UE receives a HO Command for a specific target-SAT or none at all. However, collisions may occur if multiple UEs try to access the same target-SAT with the same preamble signature (PRACH) when there is an insufficient amount of RB available on the target SAT. Here, the two-step RACH process is assumed for RA signaling, following the guidelines of Release 16 of 5G-NR [33].

3) DHO (Proposed) is our proposed HO method trained using the IMPALA framework, as presented in Algorithm 1. This approach enables each serving-SAT to select the optimal HO action (e.g., HO Request) for all ground UEs to be sent to target-SATs. This method operates under partial state observability, whereby each serving-SAT agent interacts only with ground UEs and utilizes observable state information without communicating with other entities. The learning process can be seen as a partially observable MDP (POMDP).

As discussed in Sec. III, the challenge of massive HO arises in LEO SAT networks due to the high density of ground UEs that need to HO simultaneously; besides, the fast

4Here, the A3 event is used as it is widely used and has a higher occurrence probability in practical deployments. Other entering conditions, e.g., A2, A4, or A5, can also be used for the conventional HO (see Table I).

HO (Conventional） 一 Random (Heuristic） 一 DHO (Proposed)  
![](images/98e97c88b7d3c9c9cf77fc6e776129010ec424e3c68337fc4bd77bb26b986002.jpg)

<details>
<summary>line</summary>

| # of RBs [1/# of UEs] | Avg. Access Delay (Red) | Avg. Access Delay (Blue) | Avg. Access Delay (Green) |
| --------------------- | ------------------------ | ------------------------- | -------------------------- |
| 0.3                   | 10.0                     | 10.0                      | 10.0                       |
| 0.4                   | 5.0                      | 5.0                       | 8.0                        |
| 0.5                   | 0.5                      | 1.0                       | 6.0                        |
| 0.6                   | 0.1                      | 0.8                       | 5.0                        |
| 0.7                   | 0.1                      | 0.7                       | 4.0                        |
| 0.8                   | 0.1                      | 0.6                       | 3.0                        |
| 0.9                   | 0.1                      | 0.5                       | 2.0                        |
| 1.0                   | 0.1                      | 0.5                       | 1.0                        |
</details>

(a) Average access delay

![](images/3a368a499931c0956fb7f82cc65dff95626b95d6502b15be156c6fb44e778a25.jpg)

<details>
<summary>line</summary>

| # of RBs [1/# of UEs] | Avg. Collision Rate (Lack of RB) - Red Line | Avg. Collision Rate (Lack of RB) - Blue Line | Avg. Collision Rate (Lack of RB) - Green Line |
| --------------------- | ------------------------------------------ | -------------------------------------------- | --------------------------------------------- |
| 0.3                   | 10.0                                       | 10.0                                         | 10.0                                          |
| 0.4                   | 1.0                                        | 1.0                                          | 10.0                                          |
| 0.5                   | 0.1                                        | 0.1                                          | 10.0                                          |
| 0.6                   | 0.01                                       | 0.01                                         | 10.0                                          |
| 0.7                   | 0.001                                      | 0.001                                        | 10.0                                          |
| 0.8                   | 0.001                                      | 0.001                                        | 10.0                                          |
| 0.9                   | 0.001                                      | 0.001                                        | 1.0                                           |
| 1.0                   | 0.001                                      | 0.001                                        | 0.01                                          |
</details>

(b) Average colision rate (NACK due to lack of RBs)

![](images/e1434db61bcfdd5a40bc8c2f780f2b14827a4f48ed535a143192ccf203bc3d4c.jpg)

<details>
<summary>line</summary>

| # of RBs [1/# of UEs] | Avg. Collision Rate (Red) | Avg. Collision Rate (Blue) | Avg. Collision Rate (Green) |
| --------------------- | -------------------------- | --------------------------- | ---------------------------- |
| 0.3                   | 5.0                        | 5.0                         | 10.0                         |
| 0.4                   | 2.0                        | 3.0                         | 8.0                          |
| 0.5                   | 1.0                        | 1.5                         | 6.0                          |
| 0.6                   | 0.8                        | 0.5                         | 4.0                          |
| 0.7                   | 0.7                        | 0.3                         | 3.0                          |
| 0.8                   | 0.6                        | 0.2                         | 2.0                          |
| 0.9                   | 0.5                        | 0.1                         | 1.5                          |
| 1.0                   | 0.4                        | 0.1                         | 0.1                          |
</details>

(c) Average collision rate   
Fig. 5. Impact of the number of RBs. x-axis represents the number of RBs per UE on each target-SAT, i.e., Rk/J (J = 10 and P = 5J).

TABLE IV COMPARISON OF ACCESS DELAY AND COLLISION RATE OF DHO WITH BENCHMARK METHODS (HO, RANDOM) FOR THE NUMBER OF RBS IN EACH TARGET-SAT (J = 10 AND P = 5J) 

<table><tr><td colspan="4">Case 1: Enough RBs ( $R_k = J, k \in \{1,2\}$ )</td></tr><tr><td>Schemes</td><td>Avg. Access Delay</td><td>Avg. Collision (Insufficient RB)</td><td>Avg. HO Success</td></tr><tr><td>HO (Conventional)</td><td>0.789 ——H</td><td>0 I—</td><td>1 ——I</td></tr><tr><td>Random (Heuristic)</td><td>0.582 ——H</td><td>0 I—</td><td>1 ——I</td></tr><tr><td>DHO (Proposed)</td><td>0.116 H—</td><td>0 I—</td><td>1 ——I</td></tr><tr><td colspan="4">Case 2: Insufficient RBs ( $R_k = 0.3J, k \in \{1,2\}$ )</td></tr><tr><td>Schemes</td><td>Avg. Access Delay</td><td>Avg. Collision (Insufficient RB)</td><td>Avg. HO Success</td></tr><tr><td>HO (Conventiona)</td><td>13.52 ——H</td><td>12.7 ——H</td><td>0.59 ——H</td></tr><tr><td>Random (Heuristic)</td><td>8.156 ——H</td><td>5.22 ——H</td><td>0.60 ——H</td></tr><tr><td>DHO (Proposed)</td><td>8.053 ——H</td><td>4.15 H—</td><td>0.60 ——H</td></tr></table>

─ HO (Conventional） 一 Random (Heuristic) 一 DHO (Proposed)

![](images/4ae8b0a2328268b32d7884a16c17a299a4a542977017d587072e96f8cfdd9817.jpg)

<details>
<summary>line</summary>

| # of Pramble Signatures [1/# of UEs] | Avg. Access Delay (Red) | Avg. Access Delay (Blue) | Avg. Access Delay (Green) |
| ------------------------------------ | ------------------------ | ------------------------- | -------------------------- |
| 0.5                                  | ~1.2                     | ~1.0                      | ~10.0                      |
| 1                                    | ~0.6                     | ~0.8                      | ~1.0                       |
| 2                                    | ~0.4                     | ~0.7                      | ~0.9                       |
| 3                                    | ~0.3                     | ~0.6                      | ~0.9                       |
| 4                                    | ~0.2                     | ~0.5                      | ~0.9                       |
| 4.5                                  | ~0.1                     | ~0.4                      | ~0.9                       |
</details>

(a) Average access delay.

![](images/4f68f781da8acf01e30332416827f7177137fc641885b9d8b558f6086475f906.jpg)

<details>
<summary>line</summary>

| # of Pramble Signatures [1/# of UEs] | Avg. Collision Rate (Contention) - Green Line | Avg. Collision Rate (Contention) - Red Line | Avg. Collision Rate (Contention) - Blue Line |
| ------------------------------------ | --------------------------------------------- | ------------------------------------------- | -------------------------------------------- |
| 0.5                                  | ~10^1                                         | ~10^0                                       | ~10^0                                        |
| 1                                    | ~10^0                                         | ~10^-1                                      | ~10^-1                                       |
| 2                                    | ~10^-1                                        | ~10^-1                                      | ~10^-2                                       |
| 5                                    | ~10^-2                                        | ~10^-1                                      | ~10^-3                                       |
</details>

(b)Average collision rate (PRACH collision)   
Fig. 6. Impact of the number of preamble signatures. x-axis represents the number of preambles per UE on each target-SAT, i.e., P/J (J = 10 and $\overset { \smile } { R _ { k } } = J , ~ \forall k )$ .

orbital movement of LEO SATs leads to more frequent HO. Therefore, to evaluate the performance of LEO SAT networks under these conditions, we examine our proposed techniques based on two critical factors for a massive HO scenario: the number of available RBs and the number of preamble signatures.

# B. HO Performance Analysis

1) Impact of Number of RBs: The impact of the number of available RBs in each target-SAT on access delay and collision rate is shown in Fig. 5. The x-axis represents the ratio of the number of RBs in a target-SAT to the number of ground UEs, indicating the proportion of available RBs that each target-SAT can be allocateed to ground UEs. It is important to note that in order to express the massive HO situation more efficiently, we consider the ratio of the number of resources per UE rather than directly considering the number of UEs and resources.

Specifically, Fig. 5b presents the collision rate caused by the lack of RBs in the target-SAT, resulting in HO Request NACK. Our proposed DHO approach outperforms the two benchmark methods in terms of access delay and collision rate, especially when there are sufficient RBs available.

TABLE V COMPARISON OF ACCESS DELAY AND COLLISION RATE OF DHO WITH BENCHMARK METHODS (HO, RANDOM) FOR THE NUMBER OF PREAMBLE SIGNATURES FOR EACH TARGET-SAT $( J = 1 0 \mathrm { \ A N D \ } R _ { k } = J , \forall k )$ 

<table><tr><td colspan="3">Case 3: Enough preamble signatures (P = 2J)</td></tr><tr><td>Schemes</td><td>Avg. Access Delay</td><td>Avg. Collision (PRACH Collision)</td></tr><tr><td>HO (Conventional)</td><td>1.231 ——H</td><td>3.31 ——H</td></tr><tr><td>Random (Heuristic)</td><td>0.661 ——H</td><td>1.02 ——H</td></tr><tr><td>DHO (Proposed)</td><td>0.255 ——H</td><td>2.13 ——H</td></tr><tr><td colspan="3">Case 4: Insufficient preamble signatures (P = 0.8J)</td></tr><tr><td>Schemes</td><td>Avg. Access Delay</td><td>Avg. Collision (PRACH Collision)</td></tr><tr><td>HO (Conventional)</td><td>1.740 ——H</td><td>9.41 ——H</td></tr><tr><td>Random (Heuristic)</td><td>0.858 ——H</td><td>3.65 ——H</td></tr><tr><td>DHO (Proposed)</td><td>0.648 ——H</td><td>4.24 ——H</td></tr></table>

![](images/f8f7dceaf19ca8c6129cbbcd56158a3722e5877d4148585a2b46fc89e1126764.jpg)

<details>
<summary>line</summary>

| # of UEs | Norm. Reward | # of Ep. for Convergence |
| -------- | ------------ | ------------------------ |
| 10       | 2            | 10000                    |
| 50       | 0            | 50000                    |
| 100      | -5           | 100000                   |
| 150      | -10          | 120000                   |
| 200      | -15          | 120000                   |
</details>

Fig. 7. Impacts of the number of UE (J = 10, $R _ { k } = 0 . 5 \ J ,$ ∀k, and P = 2J ).

![](images/2eb9b762d0c851bb6e0355262350603cad1a57d32964f00a376441a4eec129e6.jpg)

<details>
<summary>bar</summary>

| Method | Avg. Reward |
| ------ | ----------- |
| s^n[ n] \ {A_i[n]} | 0.8 |
| s^c[n] \ {a HO[n]} | 0.8 |
| s^c[n] \ {a[n-1]} | 0.7 |
| s^c[n] \ {n} | 0.3 |
</details>

![](images/43a625d6451070d4c1b5f4e71f595c570310b44128d6e6d4a6a6d3d774785af4.jpg)

<details>
<summary>bar</summary>

| Method | Avg. Reward |
| ------ | ----------- |
| s[n]   | 0           |
| s[n]{n,α[n-1]} | -2        |
| s[n]{α[0][n],α[n-1]} | -2        |
| s[n]{n,α[0][n]} | -10       |
</details>

Fig. 8. Impact of each information included in s[n].

To further investigate the impact of the number of RBs, in Table IV, we present a comparison of the performance of our proposed DHO, under two scenarios: one in which enough RBs are available $( R _ { k } = J , k \in \{ 1 , 2 \} ) )$ , and another in which the available RBs are insufficient $( R _ { k } = 0 . 3 ~ J , ~ k \in \{ 1 , 2 \} )$ . While all methods eventually do a successful HO for a given RB, the proposed DHO achieves an average access delay that is 6.8x and 5.02x faster than conventional HO and random methods, respectively, when there are sufficient number of RBs available. Similarly, the DHO also enables ground UE to succeed in HO faster and with less collision when there is an insufficient number of RBs available.

Overall, the results of Fig. 5 and Table IV indicate that our proposed DHO exhibits a distinct advantage in terms of access delay, collision rate, and HO success rate when compared to the other two baselines. These findings emphasize the inherent flexibility of DHO in adapting and learning based on the specific network conditions, particularly with regard to the availability of RBs.

2) Impact of Number of Preamble Signatures: Fig. 6 and Table V shows the impact of the number of RACH preamble signatures used in the RA process between the target-SAT and ground UEs, which is conducted after the UE receiving HO Command. The figure and table investigate the performance of HO methods in terms of access delay and collision rate. The x-axis in Fig. 6 represents the ratio of the number of preamble signatures to the number of ground UEs, indicating the proportion of preamble signatures available for the RA procedure. As the number of preamble signatures increases, the probability of PRACH contention (collision) decreases.

Still, the proposed DHO technique demonstrates superior performance in terms of access delay, achieving up to 4.83x and 2.59x faster than conventional HO and random methods, respectively. Interestingly, it, however, lags behind the random method in terms of PRACH collision rate, as shown in Fig. 6b. This can be attributed to the fact that DHO prioritizes access delay over collision rate, thus somewhat accepting a higher collision rate in order to achieve better access delay; this is more clearly indicated in Table V.

Overall, the results Figs. 5 and 6, as well as Tables IV and V provide validation for the effectiveness of our proposed DHO in selecting efficient actions based on specific network conditions, particularly in relation to the number of preamble signatures available. This DHO protocol flexibly behaves when resources are sufficient and when they are insufficient, as elaborated in the following subsection.

# C. DHO Protocol Behavior

In Table VI, the behavior of the DHO protocol is demonstrated. The results demonstrate that when resources are sufficient, DHO sends HO Requests to the greatest extent possible at every opportunity, while when resources are insufficient, DHO frequently opts not to send HO Requests for a few UEs. This adaptive behavior of the DHO agent showcases its capability to adjust its actions based on network conditions, ultimately leading to optimal HO performance.

The behavior of the DHO agent is determined by the current network conditions, and it continuously updates its behavior as the conditions change over time through additional training.5 This ability to adapt to changing network conditions sets the DHO protocol apart from traditional HO methods, which may have limitations in adapting effectively to various network scenarios.

# D. Trade-off: Access Delay and Collision Rate

The proposed DHO uses a reward function that considers both access delay and collision rate to train the serving-SAT’s policy in selecting actions that minimize both factors. However, these two factors are interrelated and present a tradeoff. For instance, in order to minimize the collision rate, the

5The use of transfer learning techniques will allow our DHO agent, trained under specific network conditions, to adapt to new network conditions with only a few additional training episodes; this will be the focus of our future research.

TABLE VI DHO AGENT BEHAVIOR FOR VARIOUS SCENARIOS (J = 10) 

<table><tr><td>Scenario</td><td>HO Request for target-SATs ( $a_j = 1,2$ )</td><td>No HO Request ( $a_j = 0$ )</td></tr><tr><td>Enough RB and PRACH (Case 1 + 3)</td><td>93.7 %</td><td>6.33 %</td></tr><tr><td>Insufficient RB and PRACH (Case 2 + 4)</td><td>8.12 %</td><td>91.8 %</td></tr></table>

TABLE VII TRADE-OFF BETWEEN ACCESS DELAY AND COLLISION RATE (J = 10, $R _ { k } = J ,$ ∀k, AND $P = 5 J )$ 

<table><tr><td>Objective</td><td>Avg. Access Delay</td><td>Avg. Collision (PRACH Collision)</td></tr><tr><td>Delay-Aware ( $\nu = 5$ )</td><td>0.0875 ——H</td><td>0.0845 ——H</td></tr><tr><td>Collision-Aversion ( $\nu = 1/20$ )</td><td>0.3461 ——H</td><td>0.0613 ——H</td></tr></table>

![](images/ad8e141366a37af5203538f6b1329622236783334b401ff6834dbf4e5293778d.jpg)

<details>
<summary>line</summary>

| # of Episode | IMPALA | A3C | PPO | DQN |
| ------------ | ------ | --- | --- | --- |
| 0            | 0      | 0   | 0   | 0   |
| 3000         | -5     | -10 | -15 | -20 |
| 6000         | -5     | -10 | -15 | -20 |
| 9000         | -5     | -10 | -15 | -20 |
</details>

(a) DQN,PPO,A3C,and IMPALA

![](images/3831cdf23a07d3d387c3c3fd31d176caceb06563fbe9e1cd8722537d9f8c18c4.jpg)

<details>
<summary>line</summary>

| # of Episode | IMPALA | A3C | PPO |
| ------------ | ------ | --- | --- |
| 0            | -5.0   | -5.0 | -15.0 |
| 3000         | -2.0   | -4.0 | -8.0  |
| 6000         | -1.0   | -3.0 | -7.0  |
| 9000         | -0.5   | -2.0 | -6.0  |
</details>

(b) PPO,A3C,and IMPALA   
Fig. 9. Comparison of DRL algorithms (J = 10, $R _ { k } = 0 . 3 ~ J ,$ ∀k, and $P = 5 J )$ . The shaded region represents the variance, while the line represents the average of the cumulative reward for an episode.

number of HO Request attempts needs to be minimized, but this can increase the access delay.

The importance placed on either access delay or collision rate may vary depending on the specific application. For instance, in applications requiring ultra-reliable low-latency communications (URLLC) capability, such as real-time wireless control and monitoring systems, minimizing access delay is crucial to ensure timely and reliable transmission of critical data. On the other hand, in massive machine-type communication (MMTC) scenarios, where a large number of devices are connected, minimizing collision rate becomes more important to maximize the overall network efficiency and capacity.

The proposed DHO enables the adjustment of the relative importance of these factors according to the specific requirements of the application, by changing the coefficients of the access delay and collision rate functions in the reward function, represented by ν in Table VII.6

# E. Training and Convergence

The training process for DRL can become increasingly difficult as the dimensions of the state and action spaces increase. This is especially relevant in our network scenario, where the number of UEs is a significant factor, making DRL learning more challenging. Specifically, the action space and state space of DHO are represented by $\mathbb { Z } ^ { J \times K }$ and

$\mathbb { R } ^ { J \times ( 2 J + 1 ) }$ , respectively. In general, as the dimensions of the state space and action space increase, the number of training steps required for the DRL agent to converge also increases. Furthermore, the learning reward tends to decrease with increasing dimensionality. Fig. 7 shows the correlation between the number of UEs and the training step (episode) required. As shown in this result, training with 100 UEs takes approximately five times longer than training with 10 UEs. Our employed IMPALA algorithm is empirically known to be robust and stable in such a high-dimensional state and action space [8]. Our DRL-based HO algorithm can be efficiently scaled up to more UE cases using transfer learning or distributed training, which is deferred for future work.

# VI. CONCLUSION

In conclusion, this work presents a novel HO protocol called DHO to address the challenge of massive access in LEO SAT networks. By using a DRL approach, the DHO protocol is able to minimize access delays and collision rates while simplifying the HO process. The numerical results demonstrate the superiority of the DHO protocol compared to conventional HO methods, with up to 6.8x and 5.02x lower access delay than conventional and heuristic methods, respectively.

As the next step, to fully realize the potential of regenerative-type LEO SAT networks, this will require optimization or a new design of existing specific functions in gNB in terrestrial networks, taking into account the unique characteristics of the NTN, such as their high-dynamic characteristics and massive access.

# APPENDIX A SELECTION OF STATE INFORMATION

The state space of an agent should contain sufficient information for decision-making while minimizing additional data collection overhead from the environment to promote DRL training convergence. To identify the important information to include in the state space, we conducted an extensive study to evaluate the impact of various locally observable information on the performance of the proposed DHO protocol. Our findings are presented in an ablation study in Fig. 8, which illustrates the contribution of each piece of information to the overall system.

We first study the centralized case, referred to as DHO-Centralized, as shown in Fig. 8a. In this case, the state information includes both locally observable and nonobservable (centralized) information (e.g., A3 event $\mathbf { A _ { 3 } } [ n ] )$ , which is defined as:

$$
\mathbf {s} ^ {\mathrm{c}} [ n ] = \{\mathbf {s} [ n ], \mathbf {A _ {3}} [ n ] \}. \tag {18}
$$

Here, the performance of DHO-Centralized serves as an upperbound result of our proposed DHO scheme. As shown in the figure, the DHO protocol achieves near-optimal performance while minimizing complexity. Note that $\mathbf { s } ^ { \mathrm { c } } [ n ] \ \backslash \ \mathbf { A } _ { 3 } [ n ]$ is equivalent to s[n] and that DHO utilizes only locally observable information.

Secondly, Fig. 8b demonstrates that the DHO protocol primarily depends on two locally observable pieces of information: 1) the time index and 2) the accessed UEs. These two pieces of information have a significant impact on the training of DHO. Interestingly, that information is locally observable which highlights the potential for a distributed multi-agent DRL approach in future work.

# APPENDIX B SELECTION OF DRL ALGORITHM

We empirically demonstrate the superior performance of IMPALA over DQN, PPO, and A3C in our specific environment. Fig. 9 showcases the convergence behavior of the three algorithms and provides insights into their performance characteristics. Firstly, as shown in Fig. 9a, we observe that DQN faces challenges in achieving convergence due to the large action space. Unlike IMPALA, A3C, and PPO, which can handle multi-discrete type actions, DQN requires alternative approaches, such as flattening the action space, to select an action from all possible actions. Secondly, as shown in Fig. 9b, IMPALA exhibits better performance compared to A3C and PPO in terms of stable convergence, thanks to its scalability and improved sample efficiency (see Sec. IV-D). These results highlight the advantages of IMPALA over other DRL algorithms in our study.

# REFERENCES

[1] Starlink. Accessed: Sep. 2021. [Online]. Available: https://www. starlink.com/   
[2] Federal Communication Commission (FCC). (Jul. 2020). FCC Authorizes Kuiper Satellite Constellation. [Online]. Available: https://www.fcc.gov/document/fcc-authorizes-kuiper-satelliteconstellation

[3] B. Di, L. Song, Y. Li, and H. V. Poor, “Ultra-dense LEO: Integration of satellite access networks into 5G and beyond,” IEEE Wireless Commun., vol. 26, no. 2, pp. 62–69, Apr. 2019.   
[4] O. Kodheli et al., “Satellite communications in the new space era: A survey and future challenges,” IEEE Commun. Surveys Tuts., vol. 23, no. 1, pp. 70–109, 1st Quart., 2021.   
[5] N. Saeed, A. Elzanaty, H. Almorad, H. Dahrouj, T. Y. Al-Naffouri, and M.-S. Alouini, “CubeSat communications: Recent advances and future challenges,” IEEE Commun. Surveys Tuts., vol. 22, no. 3, pp. 1839–1862, 3rd Quart., 2020.   
[6] M. Handley, “Delay is not an option: Low latency routing in space,” in Proc. 17th ACM Workshop Hot Topics Netw., Nov. 2018, pp. 85–91.   
[7] Solutions for NR to Support Non-Terrestrial Networks (NTN), Standard 3GPP TR38.821 v16.1.0, Jun. 2021.   
[8] L. Espeholt, H. Soyer, and et al., “IMPALA: Scalable distributed deep-RL with importance weighted actor-learner architectures,” in Proc. Int. Conf. mach. learn. (ICML), vol. 80. Stockholm, Sweden, Jul. 2018, pp. 1407–1416.   
[9] Z. Wu, F. Jin, J. Luo, Y. Fu, J. Shan, and G. Hu, “A graph-based satellite handover framework for LEO satellite communication networks,” IEEE Commun. Lett., vol. 20, no. 8, pp. 1547–1550, Aug. 2016.   
[10] Y. Wu, G. Hu, F. Jin, and J. Zu, “A satellite handover strategy based on the potential game in LEO satellite networks,” IEEE Access, vol. 7, pp. 133641–133652, 2019.   
[11] L. Feng, Y. Liu, L. Wu, Z. Zhang, and J. Dang, “A satellite handover strategy based on MIMO technology in LEO satellite networks,” IEEE Commun. Lett., vol. 24, no. 7, pp. 1505–1509, Jul. 2020.   
[12] S. Zhang, A. Liu, C. Han, X. Ding, and X. Liang, “A network-flowsbased satellite handover strategy for LEO satellite networks,” IEEE Wireless Commun. Lett., vol. 10, no. 12, pp. 2669–2673, Dec. 2021.   
[13] N. C. Luong et al., “Applications of deep reinforcement learning in communications and networking: A survey,” IEEE Commun. Surveys Tuts., vol. 21, no. 4, pp. 3133–3174, 4th Quart., 2019.   
[14] M. Chen, A. Liu, W. Liu, K. Ota, M. Dong, and N. N. Xiong, “RDRL: A recurrent deep reinforcement learning scheme for dynamic spectrum access in reconfigurable wireless networks,” IEEE Trans. Netw. Sci. Eng., vol. 9, no. 2, pp. 364–376, Mar. 2022.   
[15] H.-H. Chang, H. Song, Y. Yi, J. Zhang, H. He, and L. Liu, “Distributive dynamic spectrum access through deep reinforcement learning: A reservoir computing-based approach,” IEEE Internet Things J., vol. 6, no. 2, pp. 1938–1948, Apr. 2019.   
[16] Y. Xu, J. Yu, and R. M. Buehrer, “The application of deep reinforcement learning to distributed spectrum access in dynamic heterogeneous environments with partial observations,” IEEE Trans. Wireless Commun., vol. 19, no. 7, pp. 4494–4506, Jul. 2020.   
[17] J.-H. Lee, H. Seo, J. Park, M. Bennis, and Y.-C. Ko, “Learning emergent random access protocol for LEO satellite networks,” IEEE Trans. Wireless Commun., vol. 22, no. 1, pp. 257–269, Jan. 2023.   
[18] J.-H. Leel, D. P. Selvam, A. F. Molisch, and J. Kim, “Reinforcement learning empowered massive IoT access in LEO-based non-terrestrial networks,” in Proc. 13th Int. Conf. Inf. Commun. Technol. Converg. (ICTC), Oct. 2022, pp. 1347–1350.   
[19] J.-H. Lee, H. Seo, J. Park, M. Bennis, Y.-C. Ko, and J. Kim, “Random access protocol learning in LEO satellite networks via reinforcement learning,” in Proc. IEEE 95th Veh. Technol. Conf. (VTC-Spring), Jun. 2022, pp. 1–5.   
[20] P. V. R. Ferreira et al., “Reinforcement learning for satellite communications: From LEO to deep space operations,” IEEE Commun. Mag., vol. 57, no. 5, pp. 70–75, May 2019.   
[21] J.-H. Lee, J. Park, M. Bennis, and Y.-C. Ko, “Integrating LEO satellites and multi-UAV reinforcement learning for hybrid FSO/RF non-terrestrial networks,” IEEE Trans. Veh. Technol., vol. 72, no. 3, pp. 3647–3662, Mar. 2023.   
[22] C. Jiang and X. Zhu, “Reinforcement learning based capacity management in multi-layer satellite networks,” IEEE Trans. Wireless Commun., vol. 19, no. 7, pp. 4685–4699, Jul. 2020.   
[23] J. Du, C. Jiang, J. Wang, Y. Ren, and M. Debbah, “Machine learning for 6G wireless networks: Carrying forward enhanced bandwidth, massive access, and ultrareliable/low-latency service,” IEEE Veh. Technol. Mag., vol. 15, no. 4, pp. 122–134, Dec. 2020.   
[24] V. Yajnanarayana, H. Rydén, and L. Hévizi, “5G handover using reinforcement learning,” in Proc. IEEE 3rd 5G World Forum (5GWF), Sep. 2020, pp. 349–354.

[25] S. Khosravi, H. Shokri-Ghadikolaei, and M. Petrova, “Learning-based handover in mobile millimeter-wave networks,” IEEE Trans. Cognit. Commun. Netw., vol. 7, no. 2, pp. 663–674, Jun. 2021.   
[26] C. Lee, H. Cho, S. Song, and J.-M. Chung, “Prediction-based conditional handover for 5G mm-wave networks: A deep-learning approach,” IEEE Veh. Technol. Mag., vol. 15, no. 1, pp. 54–62, Mar. 2020.   
[27] A. F. Molish, Wireless Communications From Fundamentals to Beyond 5G, 3rd ed. Hoboken, NJ, USA: Wiley, 2023.   
[28] K. Alexandris, N. Nikaein, R. Knopp, and C. Bonnet, “Analyzing x2 handover in LTE/LTE–A,” in Proc. 14th Int. Symp. Modeling Optim. Mobile, Ad Hoc, Wireless Netw. (WiOpt), May 2016, pp. 1–7.   
[29] M. Hasan, E. Hossain, and D. Niyato, “Random access for machineto-machine communication in LTE-advanced networks: Issues and approaches,” IEEE Commun. Mag., vol. 51, no. 6, pp. 86–93, Jun. 2013.   
[30] E. Björnson, E. de Carvalho, J. H. Sørensen, E. G. Larsson, and P. Popovski, “A random access protocol for pilot allocation in crowded massive MIMO systems,” IEEE Trans. Wireless Commun., vol. 16, no. 4, pp. 2220–2234, Apr. 2017.   
[31] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.   
[32] J.-H. Lee, J. Park, M. Bennis, and Y.-C. Ko, “Integrating LEO satellite and UAV relaying via reinforcement learning for non-terrestrial networks,” in Proc. GLOBECOM IEEE Global Commun. Conf., Dec. 2020, pp. 1–6.   
[33] Release 16 Description; Summary of Rel-16 Work Items, Standard 3GPP TR 21.916 v0.5.0, Sep. 2021.   
[34] V. Mnih et al., “Human-level control through deep reinforcement learning,” Nature, vol. 518, pp. 529–533, Feb. 2015.   
[35] V. Mnih et al., “Asynchronous methods for deep reinforcement learning,” in Proc. Int. Conf. Mach. Learn., vol. 48, Feb. 2016, pp. 1928–1937.   
[36] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” 2017, arXiv:1707.06347.   
[37] R. S. Sutton and D. McAllester, “Policy gradient methods for reinforcement learning with function approximation,” in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 12. Denver, CO, USA, Dec. 1999, pp. 1057–1063.   
[38] V. Mnih et al., “Playing Atari with deep reinforcement learning,” 2013, arXiv:1312.5602.   
[39] D. Lopez-Perez, I. Guvenc, and X. Chu, “Mobility management challenges in 3GPP heterogeneous networks,” IEEE Commun. Mag., vol. 50, no. 12, pp. 70–78, Dec. 2012.   
[40] M. Anas, F. D. Calabrese, P.-E. Ostling, K. I. Pedersen, and P. E. Mogensen, “Performance analysis of handover measurements and layer 3 filtering for utran LTE,” in Proc. IEEE 18th Int. Symp. Pers., Indoor Mobile Radio Commun., Sep. 2007, pp. 1–5.   
[41] U. Karabulut, A. Awada, I. Viering, A. N. Barreto, and G. P. Fettweis, “RACH optimization with decision tree based supervised learning for conditional handover in 5G beamformed systems,” 2019, arXiv:1910.11890.

Ju-Hyung Lee (Member, IEEE) received the B.S. and Ph.D. degrees from the School of Electronic Engineering, Korea University, Seoul, South Korea, in 2016 and September 2021, respectively. He is currently a Post-Doctoral Researcher of electrical and computer engineering with the University of Southern California (USC), Los Angeles, CA, USA, and a Research Professor of electrical engineering with Korea University. His research interests include optimization and algorithm design for non-terrestrial networks (NTN), machine learning (ML) for wireless communications, free space optical communications (FSO), and signal processing techniques. He has received awards, including the Best Paper Awards from IEEE ICTC 2021 and 2022, the Travel Grant from IEEE GLOBECOM 2020, the Bronze Prize from the IEEE Seoul Section Student Paper Contest 2020, and the Graduate Research Excellence Award from Korea University in 2021.

Chanyoung Park received the B.S. degree (Hons.) in electrical and computer engineering from Ajou University, Suwon, Republic of Korea, in 2022. He is currently pursuing the Ph.D. degree with the Department of Electrical and Computer Engineering, Korea University, Seoul, Republic of Korea. His research interests include deep learning algorithms and their applications to communications and networks.

Soohyun Park received the B.S. degree in computer science and engineering from Chung-Ang University, Seoul, Republic of Korea, in 2019, and the Ph.D. degree in electrical and computer engineering from Korea University, Seoul, in 2023. She has been a Post-Doctoral Scholar with the Department of Electrical and Computer Engineering, Korea University, since 2023. She was a recipient of the IEEE Vehicular Technology Society (VTS) Seoul Chapter Awards in 2019 and 2023, the IEEE Seoul Section Student Paper Awards in 2020 and 2023, the HFR Research Paper Awards by KICS in 2023, and the Best Reviewer Award by ICT Express (Elsevier) in 2021.

Andreas F. Molisch (Fellow, IEEE) received the Ph.D. and Habilitation degrees from TU Vienna in 1994 and 1999, respectively. After ten years in the industry, he joined the University of Southern California, where he is currently the Solomon Golomb–Andrew and Erna Viterbi Chair Professor. He is the author of five books, including Wireless Communications (3rd edition, 2023), 22 book chapters, more than 300 journal articles, 400 conference papers, as well as 70 granted patents. His work has been cited more than 68,000 times. His H-index is 110. His research interests include wireless communications, with an emphasis on wireless propagation channels, multiantenna systems, ultrawideband signaling and localization, novel modulation methods, joint communication-computation-caching systems, and machine learning for wireless. He is a fellow of the National Academy of Inventors, AAAS, and IET, and a member of the Austrian Academy of Sciences. He was a recipient of numerous awards.