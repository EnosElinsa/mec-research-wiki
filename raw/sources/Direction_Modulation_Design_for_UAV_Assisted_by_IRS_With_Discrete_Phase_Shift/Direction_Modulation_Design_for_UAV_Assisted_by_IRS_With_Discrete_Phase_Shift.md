# Direction Modulation Design for UAV Assisted by IRS With Discrete Phase Shift

Maolin Li, Wei Gao, Qi Wu, Feng Shu , Member, IEEE, Cunhua Pan , Senior Member, IEEE, and Di Wu

Abstract—As a physical layer security technology, directional modulation (DM) can be combined with intelligent reflect-ing surface (IRS) to improve the security of drone communications. In this paper, a directional modulation scheme assisted by the IRS is proposed to maximize the transmission rate of uncrewed aerial vehicle (UAV) secure communication. Specifically, with the assistance of the IRS, the UAV transmits legitimate information and maintains its constellation pattern at the location of legitimate users on the ground, while the constellation pattern is disrupted at the eavesdropper’s location. In order to solve the joint optimization problem of digital weight coefficients, UAV position, and IRS discrete phase shift, firstly, the digital weight vector and UAV position are optimized through power minimization. Secondly, three methods are proposed to optimize IRS phase shift, namely vector trajectory (VT) method, cross entropy vector trajectory (CE-VT) algorithm, and block coordinate descent vector trajectory (BCD-VT) algorithm. Compared to traditional cross entropy (CE) methods and block coordinate descent (BCD) methods, the proposed CE-VT and BCD-VT algorithms can improve transmission rate performance. The numerical results validate the effectiveness of the optimization scheme in IRS assisted UAV communication.

Index Terms—Intelligent reflecting surface (IRS), directional modulation (DM), uncrewed aerial vehicle (UAV), vector trajectory (VT) method, discrete phase shift.

## I. INTRODUCTION

sively researched in wireless communications for their versatility in military, civilian, and scientific applications [1], [2], [3]. UAVs can effectively serve as aerial communication relay base stations, significantly enhancing the conditions of long-distance communication channels [4]. With aerial flight capabilities, UAVs can establish shortrange line-of-sight (LoS) communication links with various targets, effectively minimizing signal transmission fading. Wireless communications on UAVs face numerous challenges, including maintaining stable communication, ex-tending communication distance, bolstering an-ti-interference abilities, and efficiently managing and utilizing spectrum resources [5], [6].

Currently, there are many works, which attempt to solve the UAV communication problems. In [7], a novel drone base station control strategy was introduced, leveraging deep reinforcement learning to significantly enhance the transmission coverage and connectivity of wireless communication systems. Further, a comprehensive study was conducted on UAV communications, focusing on the assistance provided by the intelligent reflecting surface (IRS), and the findings revealed that actively altering channels through the deployment of IRS can effectively enhance signal quality [8], [9]. In [10], [11], [12], the method for maximizing system throughput was thoroughly analyzed by concurrently optimizing drone scheduling, trajectory planning, and transmission power allocation, but the optimization of transmission power was not considered. In [13], maximizing energy efficiency was studied by jointly designing power allocation, beamforming, and positioning for UAV. Then, considering collision avoidance and speed constraints, the trajectory optimization problem of UAV was studied [14].

Further, the importance of UAV communications security has been considered and studied. The high possibility of LoS links and the broadcast nature of air-to-ground UAV communications render it vulnerable to eavesdropping attempts by unauthorized individuals. To address the challenge, two technologies, physical layer security [15], [16] and secret communication [17], [18], [19], [20], are mainly used to enhance the security of UAV communications based on upper layer protocol security [21]. In [22], a comprehensive investigation was conducted on the concealed data collection methods employed by a full-duplex UAV, implementing a continuous hovering design flight trajectory, the detection likelihood was significantly diminished in unscheduled user directions through the utilization of artificial noise.

Digital Object Identifier 10.1109/TGCN.2025.3572113

However, achieving concealment on the LoS path poses significant challenges in low-rank channels, as there is a risk of information leakage when the eavesdropping node is situated precisely on the LoS path [23]. The research on IRSs provides a solution to this problem. In [24], the secrecy throughput maximization in multi-input multi-output (MIMO) systems was investigated through the deployment of IRS, and experimental results demonstrated that the utilization of these surfaces significantly enhances the confidentiality performance of the system. In [25], [26], an element-by-element approach was employed to optimize the discrete phase shift of the IRS, resulting in the design of a secure communication waveform, and the radar-communication integrated waveform was designed at the symbol level, ensuring that the modulated symbols can be accurately decoded only in the designated communication direction [27]. With the increase of IRS elements, the complexity of this method is high.

Recently, directional modulation (DM), a state-of-the-art physical layer security technology, has demonstrated its ability to facilitate secure communication at the symbol level. can focus the transmitted signal in the desired direction with correct modulation constellation while scrambling the pattern in other directions, which is a more secure technique than simple beamforming [28], [29], [30]. In [31], a DM design was performed based on a four-dimensional (4-D) antenna array to scramble the signal in undesired directions by time modulation, followed by a time series and static amplitude weighting in [32] for the high sidelobe level problem to further enhance security. For the peak-to-average power ratio (PAPR) and nonlinear distortion problems of DM transmitters, two step peak clipping (TPC) and digital predistortion (DPD) schemes were proposed in [33]. In [34], considering the energy saving security requirements of the Internet of Things, an inverse frequency diversity array was proposed, which adopts a time modulation method. In [35], an energy-efficient DM scheme was proposed using a uniform circular monopole antenna array, reducing interference to other systems.

In addition, low-altitude UAV channels are widely seen as LoS dominated. With the increase of height relative to radius, the LoS probability of all ground positions tends to 1. Through multi-band (L-band, C-band) measurement, it has been pointed out in [36] that the LoS probability exceeds 90% when the altitude exceeds 100 meters. In [37], the performance of LoS channel enhanced by IRS was studied, and the ability of IRS to maintain LoS link stability in complex terrain was verified by theoretical derivation and simulation. However, most studies are based on the perfect channel status information (CSI) of LoS channels. In fact, due to the limited hardware resources, it is difficult to obtain the perfect CSI. To address this challenge, in [38], based on classical channel estimation methods such as least squares and least mean square error, the channel estimation error vector was modeled as a Gaussian distribution variable to study secure communication under imperfect CSI. In [39], a robust beamforming design assisted by IRS was studied given a channel estimation error threshold. In [40], a fast and high-precision direction of arrival (DOA) estimation framework based on machine learning was proposed.

## A. Major Contributions

Based on the analysis, UAVs operating as aerial base stations exhibit a high likelihood of line-of-sight (LoS) and possess broadcasting characteristics for communication. When the link distance between UAVs and eavesdroppers (Eves) is shorter than that of legitimate users, or when eavesdroppers are oriented in the same direction as legitimate users, security becomes more vulnerable. To address this challenge, this paper explores the DM design for a UAV communicating with multiple users, aided by the IRS. The main contributions of this paper are summarized as follows.

• The IRS-assisted UAV DM design is studied. Due to the serious threat posed by the eavesdropper to legitimate transmissions, we use the IRS to assist UAV in better transmitting confidential information to multiple legitimate users on the ground. Specifically, by optimizing the digital weight vector, UAV position, and IRS phase shift matrix, the received symbols at the eavesdropper position are designed to have low amplitude and disturbed phase, while the received symbols at the user position are designed to satisfy the modulation mode.

• We derive the power upper bound of uncertain signals and reduce the rate maximization problem to the signal amplitude maximization problem. According to the complementary cumulative distribution function of the standard Gaussian distribution, the signal amplitude under the minimum receiving sensitivity guarantee is derived, and the symbol alignment constraint between the symbol with noise and the desired symbol is transformed into the symbol alignment constraint under the ideal channel, which avoids the estimation of the phase of the noisy signal and improves the robustness of the system.

• The problem of maximizing transmission rate is studied under the constraints of DM symbol design, receiver sensitivity, maximum transmission power, discrete phase shift, constant modulus, and user position range. For solving the proposed non-convex optimization problem, a UAV position optimization scheme is first designed using the method of minimizing transmission power, and digital weight vectors were obtained through proportional amplification. Given the position of the UAV and the digital weight vector, a low complexity vector trajectory (VT) method is proposed, which is combined with traditional cross entropy (CE) method and block coordinate descending (BCD) method respectively to obtain higher transmission rate performance.

## B. Organization

The rest of this article is organized as follows. In Section II, we present the system model. In Section III, an optimization method for UAV position and digital weight coefficients is proposed. The IRS phase shift matrix optimization method is presented in Section IV. The simulation results are provided in Section V, and the conclusion is presented in Section VI.

![](images/0bec7d5dfe0750f2c8ce99ec595842af8c854eed791756dd353c3dfb65f1b87d.jpg)  
Fig. 1. System model for UAV-DM assisted by IRS.

## C. Notation

Notations: $[ \mathbf { \nabla } ] ^ { T }$ and $[ \mathbf { \nabla } ] ^ { H }$ denote transpose and conjugate transpose, respectively; s, s, and S denote scalar, vector, and matrix, respectively; || || denotes the $l _ { 2 }$ norm; | | denotes the <sup>2</sup>absolute value operation;  represents the rank of the matrix; ⊗ stands for Kronecker product.

## II. SYSTEM MODEL

As shown in Fig. 1, we consider a downlink DM system with $K _ { u }$ ground users, including a single ground point target, i.e., a non-colluded eavesdropper (Eve) with $N _ { e }$ antennas, $n _ { e } = 0 , 1 , \ldots , N _ { e } - 1$ represents the $n _ { e } \mathrm { - t h }$ antenna. A UAV <sup>= 0 1 1</sup>equipped with an N-element uniform linear array (ULA) as a transmitter and an IRS with $M \ = \ M _ { Y } M _ { Z }$ elements arranged uniformly in a plane is deployed at a height of $H _ { R } ,$ serving $K _ { u }$ single antenna users, where $M _ { Y }$ and $M _ { Z }$ represent the number of horizontal and vertical elements for the IRS, $M > N .$ . In three-dimensional space, the depression and azimuth angle are represented by $\theta \in [ 0 , \pi ]$ and $\varphi \in [ 0 , \pi ]$ <sup>[0 ]</sup>, respectively. Select the IRS element closest to the UAV as a reference, the coordinate of the UAV is $\mathbf { u } = [ \theta _ { A , R } , \varphi _ { A , R } , r _ { A , R } ] ^ { T }$ , where $\theta _ { A , R } , \varphi _ { A , R }$ , and $r _ { A , R } = $ $H _ { u } / \cos \theta _ { A , R }$ are the depression angle, azimuth angle, and distance from the UAV to the IRS, respectively. $H _ { u }$ is the height of the UAV from the ground. We represent the user set as $\mathcal { K } = \{ 0 , 1 , \ldots , K _ { u } - 1 \} , K _ { u } < N < M$ . User k and Eve e are located near the IRS, with coordinates represented as $\mathbf { q } _ { k } = [ \theta _ { R , k } , \varphi _ { R , k } , r _ { R , k } ] ^ { T }$ and $\mathbf { v } _ { e } = [ \theta _ { R , e } , \varphi _ { R , e } , r _ { R , e } ] ^ { T }$ where $\theta _ { R , k } ~ ( \theta _ { R , e } ) , \varphi _ { R , k } ( \varphi _ { R , e } )$ , and $r _ { R , k } = - H _ { R } / \cos \theta _ { R , k }$ $( r _ { R , e } )$ are the depression angle, azimuth angle, and distance from the IRS to the user (Eve), respectively. The IRS can be deployed to maintain communication with users in the nearfield area, and the line-of-sight (LoS) path from the UAV to ground users is typically considered far-field communication, considering situations where users are in a mixed near-field and far-field propagation environment. Considering that the maximum phase difference between the spherical wave and plane wave model is no more than $\pi / 8$ , the boundary between the near-field and far-field, i.e., the Fraunhofer distance or Rayleigh distance, is expressed as $2 D ^ { 2 } / \lambda$ , where D represents the aperture of the antenna, and λ represents the wavelength of the carrier [41].

In DM, B signaling symbols are designed to fall exactly in the demodulation area of the receiving constellation point at the user’s location, avoiding channel estimation at the user’s location and increasing additional transmission power to disrupt the receiving constellation pattern at the eavesdropper’s location. Assuming that the channels from the UAV to the IRS and from the IRS to the user k (Eve e) are represented as $\mathbf { G } ~ \in ~ \mathbb { C } ^ { M \times N } , ~ \mathbf { h } _ { R , k } ~ \in ~ \mathbb { C } ^ { M \times 1 } ( \dot { \mathbf { H } } _ { R , e } ~ \in ~ \mathbb { C } ^ { M \times ^ { \bullet } N _ { e } } )$ , and $\mathbf { h } _ { A , k } \in \mathbb { C } ^ { N \times 1 } ( \mathbf { H } _ { A , e } \in \mathbb { C } ^ { N \times N _ { e } } )$ , respectively, and are defined as UAV-IRS channel, IRS-user (IRS-Eve) channel, and UAV-User (UAV-Eve) channel. The b-th $( b = 0 , 1 , . . . , B - 1 )$ symbol received by the k-th user is given as

$$
y _ { b , k } = \left( \mathbf { h } _ { R , k } ^ { T } \Phi \mathbf { G } + \mathbf { h } _ { A , k } ^ { T } \right) \sum _ { i = 0 } ^ { K _ { u } - 1 } \mathbf { v } _ { b , i } s _ { b , i } + n _ { b , k } ,\tag{1}
$$

where $\begin{array} { r l r } { \Phi } & { { } = } & { d i a g ( \gamma _ { 0 } e ^ { j \phi _ { 0 } } , \gamma _ { 1 } e ^ { j \phi _ { 1 } } , \dots , \gamma _ { M - 1 } e ^ { j \phi _ { M - 1 } } ) \quad \in } \end{array}$ $\mathbb { C } ^ { M \times M }$ <sup>0 1 1</sup>represents the reflection coefficient matrix at the IRS, $\mathbf { v } _ { b , i } \in \mathbb { C } ^ { N \times 1 }$ represents the beamforming vector corresponding to the b-th unit energy symbol $s _ { b , i } , \ n _ { b , k } \sim \mathbb { C N } ( 0 , \sigma ^ { 2 } )$ represents the noise at the user assuming that the noise at all user receiving ends is independent and identically distributed. Consider a passive IRS, where the adjustable amplitude and phase of the m-th $( \ m = 0 , \ 1 , . . . , M - 1 )$ reflective unit satisfy $\gamma _ { m } ~ = ~ 1$ and $\phi _ { m } \in [ 0 , 2 \pi ]$ . The symbol received by Eve’s $n _ { e }$ -th antenna is disturbed, which can be expressed as

$$
y _ { b , n _ { e } } = \left( \mathbf { h } _ { R , n _ { e } } ^ { T } \Phi \mathbf { G } + \mathbf { h } _ { A , n _ { e } } ^ { T } \right) \sum _ { i = 0 } ^ { K _ { u } - 1 } \mathbf { v } _ { b , i } s _ { b , i } + n _ { b , n _ { e } } ,\tag{2}
$$

where $n _ { b , e } \sim \mathbb { C N } ( 0 , \sigma ^ { 2 } )$ represents the noise at the Eve, ${ \bf h } _ { A , n _ { e } }$ and ${ \bf h } _ { R , n _ { e } }$ are respectively the UAV-Eve channel and the IRS-Eve channel corresponding to the $n _ { e } \mathrm { - t h }$ antenna. Note that to enhance confidentiality performance, by optimizing ${ \bf w } _ { b }$ and Φ, the amplitude of the phase random complex signal ${ y } _ { b , n _ { e } }$ is smaller than $y _ { b , k }$

Multi-user interference in multi-user scenarios may reduce the transmission rate. To eliminate interference from other users, zero forcing (ZF) method can be used. Then, only the multi-user interference of user k is eliminated, while the eavesdropper e suffers from multi-user interference, we have

$$
\left( \mathbf { h } _ { R , k } ^ { T } \Phi \mathbf { G } + \mathbf { h } _ { A , k } ^ { T } \right) \sum _ { i = 0 , i \neq k } ^ { K _ { u } - 1 } \mathbf { v } _ { b , i } s _ { b , i } = 0 ,\tag{3}
$$

$$
\left( \mathbf { h } _ { R , n _ { e } } ^ { T } \pmb { \Phi } \mathbf { G } + \mathbf { h } _ { A , n _ { e } } ^ { T } \right) \sum _ { i = 0 , i \neq e } ^ { K _ { u } - 1 } \mathbf { v } _ { b , i } s _ { b , i } \neq 0 .\tag{4}
$$

Therefore, user $k$ can correctly demodulate and obtain the transmitted symbols, i,e.,

$$
\begin{array} { r l r } {  { \hat { y } _ { b , k } = \mathbf { v } _ { k } ^ { H } ( \mathbf { h } _ { R , k } ^ { T } \Phi \mathbf { G } + \mathbf { h } _ { A , k } ^ { T } ) ^ { H } ( \mathbf { h } _ { R , k } ^ { T } \Phi \mathbf { G } + \mathbf { h } _ { A , k } ^ { T } ) \mathbf { v } _ { k } s _ { b , k } + n _ { b , k } } } \\ & { } & { = t _ { b , k } s _ { b , k } + n _ { b , k } , \qquad ( 5 ) } \end{array}
$$

where $t _ { b , k }$ is the amplitude of the symbol received by user k. For Eve e, if the channel information of the user is known, equipping more antennas than the number of users of a single antenna can correctly demodulate the transmitted symbols. Therefore, this information transmission method is not secure.

An effective method is to add artificial noise (AN) $z _ { b }$ to the baseband signal, and the symbols received by user k and eavesdropper e can be represented as [42], [43]

$$
\left\{ \begin{array} { l l } { \tilde { y } _ { b , k } = \Big ( { \mathbf { h } } _ { R , k } ^ { T } \Phi { \mathbf { G } } + { \mathbf { h } } _ { A , k } ^ { T } \Big ) { \mathbf { v } } _ { b , k } \left( s _ { b , k } + z _ { b } \right) + n _ { b , k } , } \\ { \tilde { y } _ { b , n _ { e } } = \Big ( { \mathbf { h } } _ { R , n _ { e } } ^ { T } \Phi { \mathbf { G } } + { \mathbf { h } } _ { A , n _ { e } } ^ { T } \Big ) \sum _ { i = 0 } ^ { K _ { u } - 1 } { \mathbf { v } } _ { b , i } \left( s _ { b , i } + z _ { b } \right) + n _ { b , n _ { e } } . } \end{array} \right.\tag{6}
$$

Due to $z _ { b }$ being designed in the null space of user channel, i.e., $( \mathbf { h } _ { R , k } ^ { T } \Phi \mathbf { G } + \mathbf { h } _ { A , k } ^ { \breve { T } } ) \mathbf { v } _ { k } z _ { b } = 0$ , user k can correctly demodulate symbols.

However, the traditional approach of adding AN to the baseband requires channel estimation at the receiver. One way for a receiver to not require channel estimation is through transmitter precoding, which synthesizes symbols at the user and designs difficult to demodulate signal patterns at the eavesdropper, i.e., the user does not need $\mathbf { v } _ { k } ^ { H } ( \mathbf { h } _ { R , k } ^ { T } \Phi \mathbf { G } +$ $\mathbf { h } _ { A , k } ^ { T } ) ^ { H }$ to demodulate the signal, i.e., the receive symbol $\hat { y } _ { b , k } ^ { * }$ at the user is

$$
\hat { y } _ { b , k } ^ { * } = t _ { b , k } s _ { b , k } + n _ { b , k } .\tag{7}
$$

Then, by introducing w, the baseband signal is designed and can be written as

$$
\mathbf { w } _ { b } = \sum _ { i = 0 } ^ { K _ { u } - 1 } \mathbf { v } _ { i } \big ( s _ { b , i } + z _ { b } \big ) .\tag{8}
$$

Correspondingly, the signals received by Eve e and user k can be represented as

$$
\left\{ \begin{array} { l l } { y _ { b , k } = \left( \mathbf { h } _ { R , k } ^ { T } \Phi \mathbf { G } + \mathbf { h } _ { A , k } ^ { T } \right) \mathbf { w } _ { b } + n _ { b , k } , } \\ { y _ { b , n _ { e } } = \left( \mathbf { h } _ { R , n _ { e } } ^ { T } \Phi \mathbf { G } + \mathbf { h } _ { A , n _ { e } } ^ { T } \right) \mathbf { w } _ { b } + n _ { b , n _ { e } } . } \end{array} \right.\tag{9}
$$

## A. Channel Model

Considering that the UAV and the IRS are typically deployed at a certain height from ground users, the actual UAV-IRS, IRS-user, and UAV-user (UAV-Eve) channels consist of LoS-dominated components and low-power non-line-of-sight (NLoS) components. Assuming parameter $g \in \{ \mathcal { K } , e \}$ represents all receivers, i.e., $g \ { \overset { \triangle } { = } } \ k$ represents the user and $g \triangleq e$ denotes the eavesdropper. Then, ${ \bf G } , { \bf h } _ { R , g } ,$ , and ${ \mathbf { h } } _ { A , g }$ can be modelled as

$$
\begin{array} { r } { \mathbf { G } = \sqrt { \alpha _ { A , R } \varepsilon _ { A , R } } \overline { { \mathbf { G } } } + \sqrt { \alpha _ { A , R } \big ( 1 - \varepsilon _ { A , R } \big ) } \hat { \mathbf { G } } , } \end{array}\tag{10}
$$

$$
\begin{array} { r } { \mathbf { h } _ { R , g } = \sqrt { \alpha _ { R , g } \varepsilon _ { R , g } } \overline { { \mathbf { h } } } _ { R , g } + \sqrt { \alpha _ { R , g } \big ( 1 - \varepsilon _ { R , g } \big ) \hat { \mathbf { h } } _ { R , g } } , } \end{array}\tag{11}
$$

$$
\begin{array} { r } { \mathbf { h } _ { A , g } = \sqrt { \alpha _ { A , g } \varepsilon _ { A , g } } \overline { { \mathbf { h } } } _ { A , g } + \sqrt { \alpha _ { A , g } \left( 1 - \varepsilon _ { A , g } \right) } \widehat { \mathbf { h } } _ { A , g } , } \end{array}\tag{12}
$$

where $\alpha _ { A , R } = \rho / d _ { A , R } ^ { 2 } , \alpha _ { R , g } = \rho / d _ { R , g }$ and $\alpha _ { A , g } = \rho / d _ { A , g } ^ { 2 }$ <sup>= =</sup>represent the path loss coefficients in free space, $\rho$ is the channel power gain per unit distance, $d _ { A , R } = \| \mathbf { u } \| , \ d _ { R , k } =$ $\| \mathbf { q } _ { k } \| \left( d _ { R , e } = \| \mathbf { v } _ { e } \| \right)$ , and $d _ { A , k } = \| \mathbf { q } _ { k } - \mathbf { u } \| ( d _ { A , e } = \| \mathbf { v } _ { e } - \mathbf { u } \| )$ <sup>( = ) = ( = )</sup>represent the distances from the UAV to the IRS, the IRS to the user k (Eve e) and the UAV to the user k (Eve e), respectively. $\varepsilon _ { A , R } , \varepsilon _ { R , g }$ and $\varepsilon _ { A , g }$ represent the LoS power ratio coefficients of the corresponding channels. $\bar { \bf G } , \bar { \bf h } _ { R , g } ,$ and $\bar { \mathbf { h } } _ { A , g }$ represent the LoS component. respectively, given as

$$
\begin{array} { r } { \bar { \bf G } = ( { \bf a } _ { A , R } \otimes { \bf b } _ { A , R } ) { \bf h } _ { A , R } ^ { T } , } \end{array}\tag{13}
$$

$$
\overline { { { \bf h } } } _ { R , g } = { \bf a } _ { R , g } \otimes { \bf b } _ { R , g } ,\tag{14}
$$

$$
\begin{array} { r } { \overline { { \mathbf { h } } } _ { A , g } \big ( \theta _ { A , g } \big ) = \bigg [ 1 , e ^ { j \frac { 2 \pi d _ { A } \cos \theta _ { A , g } } { \lambda } } , \ldots , e ^ { j \frac { 2 \pi ( N - 1 ) d _ { A } \cos \theta _ { A , g } } { \lambda } } \bigg ] ^ { T } , } \end{array}\tag{15}
$$

where $d _ { A }$ is the minimum spacing between array elements of the UAV antenna array, λ is the wavelength, $\mathbf { h } _ { A , R } \ \triangleq$ $\mathbf { h } _ { A , R } ( \theta _ { A , R } ) \in \mathbb { C } ^ { N \times 1 } , \mathbf { b } _ { A , R } \triangleq \mathbf { b } _ { A , R } ( \varphi _ { A , R } , \theta _ { A , R } ) \in \mathbb { C } ^ { \dot { M } _ { Y } \times 1 }$ and $\mathbf { a } _ { A , R } \triangleq \mathbf { a } _ { A , R } ( \theta _ { A , R } ) \in \mathbb { C } ^ { M _ { Z } \times 1 }$ represent the steering vectors from the UAV to the reference unit of the IRS, from the UAV to the vertical and horizontal dimensions of the IRS, respectively, are given as

$$
\begin{array} { r } { { \bf h } _ { A , R } = \left[ 1 , e ^ { j \frac { 2 \pi d _ { A } \cos \theta _ { A , R } } { \lambda } } , \dots , e ^ { j \frac { 2 \pi ( N - 1 ) d _ { A } \cos \theta _ { A , R } } { \lambda } } \right] ^ { T } , } \end{array}\tag{16}
$$

$$
\begin{array} { r } { { \bf { a } } _ { A , R } = \left[ 1 , e ^ { j \frac { 2 \pi d _ { R } \cos \theta _ { A , R } } { \lambda } } , \ldots , e ^ { j \frac { 2 \pi d _ { R } \left( M _ { Y } - 1 \right) \cos \theta _ { A , R } } { \lambda } } \right] ^ { T } , } \end{array}\tag{17}
$$

$$
\begin{array} { r } { \mathbf { b } _ { A , R } = \Bigg [ 1 , e ^ { j \frac { 2 \pi d _ { R } \sin \varphi _ { A , R } \sin \theta _ { A , R } } { \lambda } } , \dots , } \\ { e ^ { j \frac { 2 \pi \left( M _ { Z } - 1 \right) d _ { R } \sin \varphi _ { A , R } \sin \theta _ { A , R } } { \lambda } } \Bigg ] ^ { T } , } \end{array}\tag{18}
$$

$\mathbf { a } _ { R , g } ~ \triangleq ~ \mathbf { a } _ { R , g } ( r _ { \nu , g } ) ~ \in ~ \mathbb { C } ^ { M _ { Z } \times 1 }$ and $\mathbf { b } _ { R , g } \triangleq \mathbf { b } _ { R , g } ( r _ { h , g } ) \in$ $\mathbb { C } ^ { \bar { M } _ { Y } \times 1 }$ represent the vertical and horizontal steering vectors from the IRS to the receiver, respectively, written as

$$
\begin{array} { r l } & { \mathbf { a } _ { R , g } \left( r _ { \nu , g } \right) } \\ & { \quad = t _ { c } \Big [ 1 , e ^ { - j 2 \pi r _ { 1 , g } / \lambda } , \dots , e ^ { j 2 \pi r _ { M _ { Z } - 1 , g } / \lambda } \Big ] ^ { T } , } \end{array}\tag{19}
$$

$$
\begin{array} { r l } & { \mathbf { b } _ { R , g } \bigl ( r _ { h , g } \bigr ) } \\ & { \quad = t _ { c } \Bigl [ 1 , e ^ { - j 2 \pi r _ { 1 , g } / \lambda } , \ldots , e ^ { j 2 \pi r _ { M _ { Y } - 1 , g } / \lambda } \Bigr ] ^ { T } , } \end{array}\tag{20}
$$

where $t _ { c } = e ^ { j 2 \pi r _ { g } / \lambda } , d _ { R }$ is the minimum spacing between the IRS elements, and $r _ { g }$ is the distance from the IRS reference unit to the receiver. According to geometric relationships, the distances $r _ { \nu , g }$ and ${ r } _ { h , g }$ from the ν-th $( \nu = 0 , 1 , \ldots , M _ { Z } -$ individual element in the vertical direction and the h-th $( h = 0 , 1 , \ldots , M _ { Y } - 1 )$ element in the horizontal direction of the IRS to the receiver corresponding to the receiver can be given as

$$
r _ { \nu , g } = \sqrt { r _ { R , g } ^ { 2 } + \nu ^ { 2 } d ^ { 2 } - 2 r _ { R , g } \nu d \cos \theta _ { R , g } } ,\tag{21}
$$

$$
r _ { h , g } = \sqrt { r _ { R , g } ^ { 2 } + h ^ { 2 } d ^ { 2 } - 2 r _ { R , g } h d \sin \varphi _ { R , g } \sin \theta _ { R , g } } ,\tag{22}
$$

respectively. G , $\hat { \mathbf { h } } _ { R , g }$ and $\hat { \mathbf { h } } _ { R , g }$ are an independent and identically distributed complex Gaussian random variable with a mean of zero and unit covariance, representing the NLoS component. Accordingly, the aggregated channel from the

UAV to the receiver can be represented as a combination of LoS and NLoS components, i.e.,

$$
\begin{array} { r l } { \| u _ { \tau } - u _ { \tau } ^ { * } - \xi _ { \tau } ^ { * } \| \mathcal { E } _ { q } ^ { 2 } \| _ { L ^ { 2 } } } & { = \bigg | \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) ^ { 2 } - \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) \bigg | _ { L ^ { 2 } } ^ { 2 } } \\ & { = \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) ^ { 2 } + \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) ^ { 2 } + \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) ^ { 2 } + \frac { \widehat { \mu } _ { 0 } } { 2 } } \\ & { = \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) ^ { 2 } + \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) ^ { 2 } + \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) ^ { 2 } + \frac { \widehat { \mu } _ { 0 } } { 2 } } \\ & { \quad \bigg [ \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) ^ { 2 } + \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ] ^ { 2 } + \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ( \frac { \widehat { \mu } _ { 0 } } { 2 } \bigg ) ^ { 2 } + \frac { \widehat { \mu } _ { 0 } } { 2 } } \\ &  = \frac { \widehat { \mu } _ { 0 } }  2 \end{array}\tag{23}
$$

Then, the b-th symbol received by the receiver can be rewritten as

$$
\begin{array} { c } { y _ { b , g } = \Big ( \mathbf { h } _ { g } ^ { L o S } + \mathbf { h } _ { g } ^ { N L o S } \Big ) \mathbf { w } _ { b } + n _ { g } } \\ { = \mathbf { h } _ { g } ^ { L o S } \mathbf { w } _ { b } + \hat { n } _ { b , g } , } \end{array}\tag{24}
$$

where $\hat { n } _ { b , g } = \mathbf { h } _ { g } ^ { N L o S } \mathbf { w } _ { b } + n _ { g }$ is the sum of all uncertain terms, following a Gaussian distribution with modified variance, i.e., $\hat { n } _ { b , g } \sim \mathbb { C N } ( 0 , \hat { \sigma } _ { b , g } ^ { 2 } )$ , satisfying

$$
\begin{array} { r l r } {  { \hat { \sigma } _ { b , g } ^ { 2 } = ( \| \zeta _ { g } ^ { 2 } v ^ { 1 } \overline { { \mathbf { G } } } \Phi \mathbf { w } _ { b } \| ^ { 2 } + \frac { 1 } { 2 } \| \zeta _ { g } ^ { 2 } v ^ { 2 } \Phi \otimes \mathbf { w } _ { b } \| _ { F } ^ { 2 }  } } \\ & { } & { +  ( \zeta _ { g } ^ { 4 } ) ^ { 2 } \| \mathbf { w } _ { b } \| ^ { 2 } + \| \zeta _ { g } ^ { 1 } v ^ { 2 } ( v e c ( \Phi ) \cdot \mathbf { \bar { h } } _ { R , g } ^ { T } ) \otimes \mathbf { w } _ { b } \| _ { F } ^ { 2 } + \sigma ^ { 2 } ) } \\ & { } & { = \| \zeta _ { g } ^ { 2 } v ^ { 1 } \bar { \mathbf { G } } \mathbf { w } _ { b } \| ^ { 2 } + ( \frac { 1 } { 2 } M ( \zeta _ { g } ^ { 2 } v ^ { 2 } ) ^ { 2 }  } \\ & { } & { +  ( \zeta _ { g } ^ { 4 } ) ^ { 2 } + M ( \zeta _ { g } ^ { 1 } v ^ { 2 } ) ^ { 2 } ) \| \mathbf { w } _ { b } \| ^ { 2 } + \sigma ^ { 2 } . } \end{array}
$$

According to (24) and (25), for the b-th symbol, the signalto-noise ratio (SNR) at the receiver can be written as

$$
\mathrm { S N R } _ { b , g } = \frac { \Vert \mathbf { w } _ { b } \mathbf { h } _ { g } ^ { L o S } \Vert ^ { 2 } } { \hat { \sigma } _ { b , g } ^ { 2 } } = \frac { t _ { b , g } ^ { 2 } } { \hat { \sigma } _ { b , g } ^ { 2 } } ,\tag{26}
$$

where ${ t _ { b , g } }$ is the magnitude corresponding to the b-th symbol.

For an ideal beamforming where the beam gain in an undesired direction is zero, the sum of the beam gains in all desired directions is equal to the number of transmitting antennas. In practice, it is difficult to achieve ideal beamforming, and the sum of beam gains satisfies

$$
\begin{array} { r } { \| \bar { \mathbf G } \mathbf { w } _ { b } \| ^ { 2 } \leq N . } \end{array}\tag{27}
$$

According to (25) and (27), the upper bound on the variance of the sum of uncertain terms can be obtained, i.e.,

$$
\begin{array} { r l r } {  { \hat { \sigma } _ { b , g } ^ { 2 } \le ( ( \zeta _ { g } ^ { 2 } v ^ { 1 } ) ^ { 2 } \frac { N } { M P _ { \operatorname* { m a x } } } + \frac { 1 } { 2 } ( \zeta _ { g } ^ { 2 } v ^ { 2 } ) ^ { 2 }  } } \\ & { } & {  + \ \frac { ( \zeta _ { g } ^ { 4 } ) ^ { 2 } } { M } + ( \zeta _ { g } ^ { 1 } v ^ { 2 } ) ^ { 2 } ) M P _ { \operatorname* { m a x } } + \sigma _ { g } ^ { 2 } } \\ & { } & { = \hat { z } _ { g } , } \end{array}\tag{28}
$$

where $P _ { m a x }$ is the maximum transmit power threshold for the UAV. Then, the lower bound of the transmission rate of the user k is expressed as

$$
R _ { b , g } = \log \Big ( 1 + t _ { b , g } ^ { 2 } / \hat { z } _ { g } \Big ) , ~ g \triangleq k .\tag{29}
$$

## B. DM Design Assisted by IRS

Let $^ { t _ { b , k } }$ and ${ t } _ { b , e }$ represent the amplitude of the received symbols at user k and Eve $\boldsymbol { e } , \boldsymbol { \vartheta } _ { b , k }$ and $\boldsymbol { \vartheta } _ { b , e }$ represent the phase of the received symbols at the user and eavesdropper, respectively. The desired constellation pattern $\{ t _ { b , k } e ^ { j \vartheta _ { b , k } } \} _ { b = 0 } ^ { \mathcal { B } - 1 }$ <sup>=0</sup>is synthesized in user directions, while is disrupted to $\{ t _ { b , e } e ^ { j \vartheta _ { b , e } } \} _ { b = 0 } ^ { B - 1 }$ in Eve directions. With $\hat { z } _ { g }$ obtained by (28), <sup>=0</sup>maximizing the transmission rate at the user is equivalent to maximizing ${ t _ { b , k } }$ according to monotonicity. As illustrated in [38], maximizing ${ t _ { b , k } }$ can optimize the user’s reception performance and improve robustness to hardware damage and imperfect CSI. Then, in the constellation pattern design of users and the Eve, the problem of maximizing the user transmission rate under the constraints of the minimum detectable symbol power, maximum transmit power, constant reflection amplitude, discrete phase shift, and positioning range can be formulated as

$$
\begin{array} { r l } { P 1 : \displaystyle { \operatorname* { m a x } _ { \mathbf { w } _ { k } , \Phi , \mathbf { u } } \mathbf { \Lambda } _ { k = 0 } ^ { K _ { n } - 1 } t _ { b , k } } } \\  \mathrm { s . t . } \quad \mathrm { C l } : \displaystyle { \mathbf { k } _ { k } ^ { L o S } \mathbf { w } _ { b } + \hat { n } _ { b , k } = t _ { b , k } e ^ { j \Phi _ { b , k } } \mathrm { , ~ } \forall k , } \\ { \mathrm { C 2 : ~ } \displaystyle { \mathbf { k } _ { b } ^ { L o S } \mathbf { w } _ { b } + \hat { n } _ { b , e } = t _ { b , e } e ^ { j \Phi _ { b , e } } \mathrm { , ~ } \forall e , } } \\ { \mathrm { C 3 : ~ } t _ { b , k } \geq r _ { \operatorname* { m i n } } \mathrm { , ~ } \forall k , } \\ { \mathrm { C 4 : ~ } \displaystyle { \| \mathbf { w } _ { b } \| ^ { 2 } \leq P _ { \operatorname* { m a x } } \mathrm { , ~ } } } \\ { \mathrm { C S : \gamma _ { m } = 1 , \phi _ { m } \in [ 0 , 2 \pi ] , \forall m , ~ } } \\  \mathrm { C 6 : ~ } \displaystyle { \theta _ { \operatorname* { m i n } } \leq \theta _ { \operatorname* { m a x } } \leq \theta _ { \operatorname* { m a x } } , \varphi _ { \operatorname* { m i n } } \leq \varphi _ { A , R } \leq \varphi _ { \operatorname* { m a x } } \mathrm { , ~ } } \end{array}\tag{30}
$$

where, $r _ { \mathrm { m i n } }$ is the minimum received symbol power threshold <sup>min</sup>for the user, reflecting the sensitivity of the user’s received signal, i.e., the minimum symbol power that the user can detect is $r _ { \operatorname* { m i n } } . \ \theta _ { \operatorname* { m i n } }$ and $\theta _ { \mathrm { m a x } }$ represent the minimum and <sup>min min</sup>maximum elevation angles of the UAV, $\varphi _ { \mathrm { m i n } }$ and ϕ <sup>min</sup>represent the minimum and maximum azimuth angles of the UAV, respectively.

However, for the equality constraints C1 and C2, the received symbol phases are strictly aligned with the desired phases, and the phase of uncertain items $\hat { n } _ { b , k }$ and $\hat { n } _ { b , e }$ are <sup>ˆ ˆ</sup>difficult to obtain accurately. The derivation for designing under the presumption of a noise-free environment is as follows.

Based on the concept of constructive interference [38], the symbols received at the user $k$ can be designed by relaxing the phase, which is written as

$$
\begin{array} { r l } & { | \Im \{ \left( \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } + \hat { n } _ { b , k } \right) e ^ { j \vartheta _ { b , k } } \} | } \\ & { \le \left( \Re \{ ( \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } + \hat { n } _ { b , k } ) e ^ { j \vartheta _ { b , k } } \} - t _ { b , k } \right) \tan \varpi , \forall k , b , } \end{array}\tag{31}
$$

where $\varpi \ : = \ : \pi / B$ represents the maximum phase devia-<sup>=</sup>tion from the standard constellation point. However, due to receiving noise and power, (31) may not always be satisfied, resulting in erroneous decoding. To reduce the bit error rate (BER), based on the linear property of Gaussian distribution, (31) can be written as (32), as shown at the bottom of the next page, where is the detection probability threshold, which is the complementary cumulative distribution function with variance $( 1 \dot { \ } + \ \tan ^ { 2 } \dot { \varpi } ) \hat { \sigma } _ { b , k } ^ { 2 }$ . The inverse cumulative distribution function of the standard Gaussian variable is represented as $\Phi ^ { - 1 } ( \cdot )$ , (31) can be written as

$$
\begin{array} { r l } & { | \mathbb { S } \{ \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } e ^ { j \vartheta _ { b , k } } \} | } \\ & { \quad \leq \left( \Re \{ \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } e ^ { j \vartheta _ { b , k } } \} - t _ { b , k } \right) \tan \varpi - \Delta _ { k } , \forall k , b , } \end{array}\tag{33}
$$

where $\Delta _ { k } = \Phi ^ { - 1 } ( 1 - \Gamma ) \sqrt { ( 1 + \tan ^ { 2 } \varpi ) z _ { k } }$ . The right-hand term of (33) is greater than or equal to zero, and the larger its value, the better the receiver’s reception performance. With $( \Re \{ { \bf h } _ { k } ^ { L o S } { \bf w } _ { b } e ^ { j \vartheta _ { b , k } } \} - t _ { b , k } ) \tan \varpi - \bar { \Delta } _ { k } = 0 .$ , estimate the uncertain item $\hat { n } _ { b , g }$ and ensure that the symbol amplitude $\hat { t } _ { b , k } \ge r _ { \operatorname* { m i n } } + \Delta _ { k } / \tan \varpi = r _ { m i n , k }$ to meet the minimum <sup>min</sup>signal reception power at the user’s location. Then, we have $\Re \{ { \bf h } _ { k } ^ { L \bar { o } S } { \bf w } _ { b } e ^ { \bar { j } \vartheta _ { b , k } } \} = \hat { t } _ { b , k }$ . For eavesdropping locations, low amplitude and phase random symbols are [38], [44]. Therefore, the constraints C1 and C2 can be redescribed as

$$
\mathrm { C 1 } ^ { \prime } : \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } = \hat { t } _ { b , k } e ^ { j \vartheta _ { b , k } } , \forall k ,\tag{34}
$$

$$
\mathrm { C 2 ^ { \prime } } : \mathbf { h } _ { e } ^ { L o S } \mathbf { w } _ { b } = t _ { b , e } e ^ { j \vartheta _ { b , e } } , \forall e ,\tag{35}
$$

respectively.

For the phase shift constraint C5 of IRS, in practice, the accuracy of phase shift is limited, $\mathrm { i } . \mathrm { e } . , \phi _ { m }$ can only be selected from a finite set $\mathbb { F } ,$ given by

$$
\phi _ { m } \in \mathbb { F } = \Big [ 0 , 2 \pi / 2 ^ { \tilde { B } } , \ldots , \Big ( 2 ^ { \tilde { B } } - 1 \Big ) 2 \pi / 2 ^ { \tilde { B } } \Big ] ,\tag{36}
$$

where $\tilde { B }$ represents $\tilde { B }$ bits. Then, the problem of maximizing user transmission rate is formulated as

$$
\begin{array} { r l } { P 2 : \underset { \mathbf { w } , \Phi , \mathbf { u } } { \mathrm { M a x } } } & { K _ { u } - 1 } \\ { \mathrm { s . t . } } & { K _ { 0 } \mathbf { a } } \\ { \mathrm { s . t . } } & { \mathrm { C l } ^ { 1 / 2 } : \mathrm { h } _ { k } ^ { L \delta } \mathbf { w } _ { b } = \hat { l } _ { b , k } e ^ { j \phi _ { b , k } } , \forall k , } \\ & { \mathrm { C 2 } ^ { \prime } : \mathrm { h } _ { k } ^ { L \delta } \mathbf { w } _ { b } = t _ { b , e } e ^ { j \phi _ { b , e } } , \forall e , } \\ & { \mathrm { C 3 } ^ { \prime } : \hat { r } _ { k } \geq r _ { m i n , k } , } \\ & { \mathrm { C 4 } : \left. \mathbf { w } _ { b } \right. ^ { 2 } \leq P _ { \operatorname* { m a x } } , } \\ & { \mathrm { C 5 } ^ { \prime } : \gamma _ { m } = 1 , \phi _ { m } \in \mathbb { F } , \forall m , } \\ & { \mathrm { C 6 } : \theta _ { \mathrm { m i n } } \leq \theta _ { A , R } \leq \theta _ { \operatorname* { m a x } } , \varphi _ { \operatorname* { m i n } } } \\ & { \mathrm { \leq } \varphi _ { A , R } \leq \varphi _ { \operatorname* { m a x } } . } \end{array}\tag{37}
$$

However, the constraints C5 and C6 are non-convex, and the optimization variables ${ \bf w } _ { b }$ and $\Phi$ are coupled with each other.

For the case of a large number of the IRS elements, the highly complex exhaustive search method is not applicable.

## C. DoF Analysis

For the far-field assumption, the degree of freedom (DoF) $\mathrm { D o F } _ { e }$ of MIMO communication without IRS deployment at Eve can be expressed as

$$
\mathrm { D o F } _ { e } \leq \operatorname* { m i n } { \mathrm { ~ } ( N , N _ { e } ) } .\tag{38}
$$

For $K _ { u }$ single-antenna multiple access users, the maximum degree of freedom is $K _ { u }$ [45].

Furthermore, deploying MIMO communication with a IRS, the degree of freedom $\mathrm { D o F } _ { e , 0 }$ at Eve can be represented as

$$
\begin{array} { r l r } { \mathrm { D o F } _ { e , 0 } \leq \mathrm { r a n k } \big ( \mathbf { H } _ { R , e } \Phi \bar { \mathbf { G } } + \mathbf { H } _ { A , e } \big ) } & { } & \\ { \leq \mathrm { r a n k } \big ( \mathbf { H } _ { R , e } \Phi \bar { \mathbf { G } } \big ) + \mathrm { r a n k } \big ( \mathbf { H } _ { A , e } \big ) } & { } & \\ { \leq \mathrm { m i n } \quad \big ( \mathrm { r a n k } \big ( \mathbf { H } _ { R , e } \Phi \big ) , \mathrm { r a n k } ( \bar { \mathbf { G } } ) \big ) + \mathrm { r a n k } \big ( \mathbf { H } _ { A , e } \big ) } & { } & \\ { \leq \mathrm { m i n } \quad \big ( \mathrm { m i n } \quad \big ( \mathrm { r a n k } \big ( \mathbf { H } _ { R , e } \Phi \big ) , \mathrm { r a n k } ( \bar { \mathbf { G } } ) \big ) + \mathrm { r a n k } \big ( \mathbf { H } _ { A , e } \big ) \big ) } & { } & \\ { \quad \quad \quad + \mathrm { r a n k } \big ( \mathbf { H } _ { A , e } \big ) } & { } & \\ { = \mathrm { m i n } \quad \big ( \mathrm { r a n k } \big ( \mathbf { H } _ { R , e } \big ) , \mathrm { r a n k } ( \bar { \mathbf { G } } ) \big ) } & { } & \\ { \quad \quad \quad + \mathrm { r a n k } \big ( \mathbf { H } _ { A , e } \big ) . } & { } & { ( 3 9 } \end{array}
$$

In LoS channel, $\mathbf { \widetilde { \mathbf { \Gamma } } } ( \mathbf { H } _ { R , e } ) = \operatorname { r a n k } ( \bar { \mathbf { G } } ) = \operatorname { r a n k } ( \mathbf { H } _ { A , e } ) = 1$ so we have

$$
\mathrm { D o F } _ { e , 0 } \leq 2 .\tag{40}
$$

the degree of freedom $\mathrm { D o F } _ { e , 0 }$ at Eve can be represented as

$$
\begin{array} { r l } & { \mathrm { D o F } _ { u , 0 } \leq \mathrm { r a n k } \big ( \mathbf { H } _ { R , K _ { u } } \Phi \bar { \mathbf { G } } + \mathbf { H } _ { A , K _ { u } } \big ) } \\ & { \qquad \leq \mathrm { r a n k } \big ( \mathbf { H } _ { R , K _ { u } } \Phi \bar { \mathbf { G } } \big ) + \mathrm { r a n k } \big ( \mathbf { H } _ { A , K _ { u } } \big ) } \\ & { \qquad \leq \mathrm { m i n } \quad \big ( \mathrm { r a n k } ( \mathbf { H } _ { R , K _ { u } } \Phi ) , \mathrm { r a n k } ( \bar { \mathbf { G } } ) \big ) + \mathrm { r a n k } \big ( \mathbf { H } _ { A , K _ { u } } \big ) } \\ & { \qquad = \mathrm { m i n } \quad \big ( \mathrm { r a n k } ( \mathbf { H } _ { R , K _ { u } } ) , \mathrm { r a n k } ( \bar { \mathbf { G } } ) \big ) + \mathrm { r a n k } \big ( \mathbf { H } _ { A , K _ { u } } \big ) , } \end{array}\tag{41}
$$

where

$$
\mathbf { H } _ { R , K _ { u } } = \left[ \bar { \mathbf { h } } _ { R , 0 } , \bar { \mathbf { h } } _ { R , 1 } , \ldots , \bar { \mathbf { h } } _ { R , K _ { u } - 1 } \right] ^ { T } \in \mathbb { C } ^ { K _ { u } \times M } ,\tag{42}
$$

$$
\mathbf { H } _ { A , K _ { u } } = \left[ \bar { \mathbf { h } } _ { A , 0 } , \bar { \mathbf { h } } _ { A , 1 } , \ldots , \bar { \mathbf { h } } _ { A , K _ { u } - 1 } \right] ^ { T } \in \mathbb { C } ^ { K _ { u } \times N } .\tag{43}
$$

According to (41), since both $\bar { \bf G }$ and ${ \bf { H } } _ { R , k }$ are non-zero matrices, $( \bar { \bf G } ) \geq 1$ $\mathrm { r a n k } ( \mathbf { H } _ { R , K _ { u } } ) \geq 1$ . In LoS channel, rank $\mathbf { \eta } _ { : } ( \mathbf { H } _ { R , K _ { u } } ) = 1$ <sup>) 1 rank( ) 1</sup>, we have the following inequality

$$
\mathrm { D o F } _ { 1 } \leq 1 + K _ { u } .\tag{44}
$$

For the near-field, in the LoS channel, due to $\mathrm { r a n k } ( \bar { \bf G } ) = 1$ the highest degree of freedom is the same as in the far-field. Therefore, deploying IRS increases the degree of freedom from $K _ { u } \mathrm { ~ t o ~ } 1 + K _ { u }$ compared to the deployment without IRS.

## D. BER Analysis

Using quadrature phase shift keying (QPSK) modulation symbols, the receiver decodes the signal according to the adjusted constellation pattern. The bit error rate (BER) of the receiver can be calculated by [46]

$$
\mathrm { B E R } = \frac { 1 } { 4 } \sum _ { i = 1 } ^ { 4 } Q \left( \frac { L _ { i } ^ { 2 } \sin ( \alpha _ { i } ) } { N _ { 0 } / 2 } \right) ,\tag{45}
$$

where $L _ { i }$ is the amplitude of the received signal, $\alpha _ { i }$ is the minimum angle between the received signal vector and the IQ axis in the constellation diagram, $N _ { 0 } / 2$ is the power spectral <sup>0</sup>density of AWGN, and Q is the complementary cumulative distribution function (CCDF).

## III. PROPOSED UAV POSITION AND DIGITAL WEIGHT VECTOR OPTIMIZATION METHOD

In this section, in order to solve problem (37), we first present the position optimization and digital weight vector optimization methods for UAV.

## A. Position Optimization of UAV-DM System

The appropriate power budget $P _ { \mathrm { m a x } }$ is an important factor <sup>max</sup>for the solution of P2 and P3 [47], [48]. Given the UAV position and IRS reflection coefficient matrix Φ, the minimum transmit power $P _ { \mathrm { m i n } } \leq P _ { \mathrm { m a x } }$ that meets the requirements of <sup>min max</sup>DM design and minimum receiving sensitivity $\hat { t } _ { b , k } = r _ { \operatorname* { m i n } } +$ $\Delta _ { k } / t a n \varpi$ is given by

$$
\begin{array} { r l r } {  { S 1 : \operatorname* { m i n } _ { \mathbf { w } _ { b } } \| \mathbf { w } _ { b } \| ^ { 2 } } } \\ & { } & { \mathrm { s . t . } C 1 ^ { \prime \prime } : \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } = ( r _ { \operatorname* { m i n } } + \Delta _ { k } / \tan \varpi ) e ^ { j \vartheta _ { b , k } } , \forall k , } \\ & { } & { C 2 : \mathbf { h } _ { e } ^ { L o S } \mathbf { w } _ { b } = t _ { b , e } e ^ { j \vartheta _ { b , e } } , \forall e . \qquad } \end{array}
$$

Note that the subproblem S1 is equivalent to the power required to meet the minimum requirements of the system, which is a convex optimization problem, and can be solved by the Lagrange multiplier method, given by

$$
\begin{array} { r } { \mathcal { L } _ { 1 } = \| \mathbf { w } _ { b } \| ^ { 2 } - \pmb { \mu } \Big ( \tilde { \mathbf { H } } ^ { T } \mathbf { w } _ { b } - \tilde { \mathbf { C } } \Big ) , } \end{array}\tag{47}
$$

where $\pmb { \mu } \in \mathbb { C } ^ { 1 \times ( K _ { u } + 1 ) }$ is the Lagrange multiplier,

$$
\begin{array} { r l } & { \tilde { \mathbf { H } } = \left[ \left( \mathbf { h } _ { 0 } ^ { L o S } \right) ^ { T } , \ldots , \left( \mathbf { h } _ { k _ { u } - 1 } ^ { L o S } \right) ^ { T } , \left( \mathbf { h } _ { e } ^ { L o S } \right) ^ { T } \right] } \\ & { \quad = \left[ v ^ { 1 } \zeta _ { 0 } ^ { 1 } \overline { { \mathbf { G } } } ^ { T } \Phi \overline { { \mathbf { h } } } _ { R , 0 } + \zeta _ { 0 } ^ { 3 } \overline { { \mathbf { h } } } _ { A , 0 } , \ldots , \right. } \\ & { \quad \quad \left. v ^ { 1 } \zeta _ { K _ { u } - 1 } ^ { 1 } \bar { \mathbf { G } } ^ { T } \Phi \bar { \mathbf { h } } _ { R , K _ { u } - 1 } + \zeta _ { K _ { u } - 1 } ^ { 3 } \bar { \mathbf { h } } _ { A , K _ { u } - 1 } , \right. } \\ & { \quad \quad \left. v ^ { 1 } \zeta _ { e } ^ { 1 } \overline { { \mathbf { G } } } ^ { T } \Phi \bar { \mathbf { h } } _ { R , e } + \zeta _ { e } ^ { 3 } \overline { { \mathbf { h } } } _ { A , e } \right] \in \mathbb { C } ^ { N \times \left( K _ { u } + 1 \right) } , } \end{array}\tag{48}
$$

$$
\begin{array} { r l r } & { \tilde { \mathbf { C } } = \left[ ( r _ { \operatorname* { m i n } } + \Delta _ { 0 } / \tan \varpi ) e ^ { j \vartheta _ { b , 0 } } , ( r _ { \operatorname* { m i n } } + \Delta _ { 1 } / \tan \varpi ) e ^ { j \vartheta _ { b , 1 } } , \right. } & \\ & { \left. \mathrm { ~ \ } \cdot \mathrm {  ~ \cdot ~ } , ( r _ { \operatorname* { m i n } } + \Delta _ { K _ { u } - 1 } / \tan \varpi ) e ^ { j \vartheta _ { b , K _ { u } - 1 } } , \right. } & \\ & { \left. t _ { e } e ^ { j \vartheta _ { b , e } } \right] ^ { T } \in \mathbb { C } ^ { ( K _ { u } + 1 ) \times 1 } . } & { ( 4 \mathfrak { P } ) } \end{array}
$$

By setting $\partial \mathcal { L } _ { 1 } / \partial \mathbf { w } _ { b } ^ { T } = 0$ , we can obtain

$$
{ \bf w } _ { b } = \frac { 1 } { 2 } \pmb { \mu } \tilde { \bf H } ^ { T } .\tag{50}
$$

Substituting (50) into the constraint condition $C 1 ^ { \prime \prime }$ and $C 2 ^ { \prime }$ yields ${ \bf w } _ { b }$ as

$$
\mathbf { w } _ { b } = \tilde { \mathbf { H } } \Big ( \tilde { \mathbf { H } } ^ { T } \tilde { \mathbf { H } } \Big ) ^ { - T } \tilde { \mathbf { C } } .\tag{51}
$$

Then, according to (51), the minimum power $P _ { \mathrm { m i n } }$ required by the system can be obtained, and $\hat { t } _ { b , k }$ <sup>min</sup>can be increased in proportion to $\sqrt { P } _ { \operatorname* { m a x } } / \| \mathbf { w } _ { b } \|$

<sup>max</sup>Since the positions of IRS and receiver g are fixed, $\zeta _ { g } ^ { 1 \smile } h _ { R , g } ^ { T }$ is regarded as unchanged, and the position of UAV affects $\upsilon ^ { 1 } \overline { { \mathbf { G } } }$ and $\zeta _ { g } ^ { 3 } \overline { { \mathbf { h } } } _ { A , g } .$ . According to (51), we have:

$$
\begin{array} { r l } & { \operatorname* { P r } \left\{ \frac { \mid \Im \left\{ \hat { n } _ { b , k } e ^ { j \vartheta _ { b , k } } \right\} \mid - \Re \left\{ \hat { n } _ { b , k } e ^ { j \vartheta _ { b , t } } \right\} \tan \varpi } { \sqrt { \left( 1 + \tan ^ { 2 } \varpi \right) \hat { \sigma } _ { b , k } ^ { 2 } } } \right. } \\ & { \left. > \frac { \left( \Re \left\{ \sqrt { p } \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } e ^ { j \vartheta _ { b , k } } \right\} - t _ { u } \right) \tan \varpi - \mid \Im \left\{ \sqrt { p } \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } e ^ { j \vartheta _ { b , k } } \right\} \mid } { \sqrt { \left( 1 + \tan ^ { 2 } \varpi \right) \hat { \sigma } _ { b , k } ^ { 2 } } } \right\} < \Gamma , \forall k , b . } \end{array}
$$

$$
\begin{array} { r } { \bar { \bf h } _ { R , g } ^ { T } \Phi \bar { \bf G } { \bf w } _ { b } = \bar { b } _ { A , g } , } \end{array}\tag{52}
$$

$$
\begin{array} { r } { \overline { { \mathbf { h } } } _ { A , g } ^ { T } \mathbf { w } _ { b } = b _ { A , g } , } \end{array}\tag{53}
$$

where ${ \bar { b } } _ { A , g }$ and $b _ { A , g }$ are the beam gain of UAV-IRS-user (UAV-IRS-Eve) and UAV-User (UAV-Eve), respectively. Then, the UAV position optimization problem is formulated as

$$
S 2 : \mathop { \operatorname* { m a x } } _ { \mathbf { u } } \sum _ { k = 0 } ^ { K _ { u } - 1 } | v ^ { 1 } \zeta _ { k } ^ { 1 } \bar { b } _ { A , k } + \zeta _ { k } ^ { 3 } b _ { A , k } |\tag{54}
$$

In accordance with the triangle inequality, we have

$$
\begin{array} { r l } {  { K _ { u } - 1 } } \\ & { \sum _ { k = 0 } ^ { K _ { u } - 1 } | v ^ { 1 } \zeta _ { k } ^ { 1 } \bar { b } _ { A , k } + \zeta _ { k } ^ { 3 } b _ { A , k } | } \\ & { \quad \le \displaystyle \sum _ { k = 0 } ^ { K _ { u } - 1 } \Big ( v ^ { 1 } \zeta _ { k } ^ { 1 } | \bar { b } _ { A , k } | + \zeta _ { k } ^ { 3 } | b _ { A , k } | \Big ) . } \end{array}\tag{55}
$$

Then, the UAV position optimization problem can be reformulated as

$$
\begin{array} { r } { S 3 : \displaystyle \operatorname* { m a x } _ { \mathbf { u } } \displaystyle \sum _ { k = 0 } ^ { K _ { u } - 1 } \left( \upsilon ^ { 1 } \zeta _ { k } ^ { 1 } | \bar { b } _ { A , k } | + \zeta _ { k } ^ { 3 } | b _ { A , k } | \right) } \\ { s . t . \ : \ : C 6 . \qquad } \end{array}\tag{56}
$$

Furthermore, the objective function in (56) is equivalent to

$$
\operatorname* { m i n } _ { \mathbf { u } } ~ J _ { 1 } = \frac { 1 } { \sum _ { k = 0 } ^ { K _ { u } - 1 } \Bigl ( \frac { \sqrt { \rho \varepsilon _ { A , R } } } { d _ { A , R } } \zeta _ { k } ^ { 1 } | \bar { b } _ { A , k } | + \frac { \sqrt { \rho \varepsilon _ { A , k } } } { d _ { A , k } } | b _ { A , k } | \Bigr ) } .\tag{57}
$$

In accordance with the arithmetic-geometric means inequality, i.e.,

$$
\begin{array} { r l r } {  { \frac { 1 } { \sum _ { i = 1 } ^ { n } a _ { i } } \le \frac { 1 } { n } \frac { 1 } { ( \prod _ { i = 1 } ^ { n } a _ { i } ) ^ { 1 / n } } = \frac { 1 } { n } ( \prod _ { i = 1 } ^ { n } \frac { 1 } { a _ { i } } ) ^ { \frac { 1 } { n } } } } \\ & { } & { \le \frac { 1 } { n ^ { 2 } } \displaystyle \sum _ { i = 1 } ^ { n } \frac { 1 } { a _ { i } } \le \sum _ { i = 1 } ^ { n } \frac { 1 } { a _ { i } } . } \end{array}\tag{58}
$$

(32)

With (58), (57) is upper bounded by

$$
\begin{array} { l } { { \displaystyle { J _ { 1 } \leq \sum _ { k = 0 } ^ { K _ { u } - 1 } \left( \frac { d _ { A , R } } { \sqrt { \rho \varepsilon _ { A , R } } \zeta _ { k } ^ { 1 } | \bar { b } _ { A , k } | } + \frac { d _ { A , k } } { \sqrt { \rho \varepsilon _ { A , k } } | b _ { A , k } | } \right) } } } \\ { { \displaystyle { \quad = \sum _ { k = 0 } ^ { K _ { u } - 1 } \left( d _ { A , R } T _ { k } ^ { 1 } + d _ { A , k } T _ { k } ^ { 2 } \right) } , } } \end{array}\tag{59}
$$

where $\begin{array} { r l r } { T _ { k , 1 } } & { { } = } & { 1 / \sqrt { \rho \varepsilon _ { A , R } } \zeta _ { k } ^ { 1 } | \bar { b } _ { A , k } | } \end{array}$ and $\begin{array} { r l } { T _ { k , 2 } } & { { } = } \end{array}$ $1 / \sqrt { \rho \varepsilon _ { A , k } } | \boldsymbol { b } _ { A , k } |$ <sup>= 1 2 =</sup>. Therefore, the approximate solution obtained by minimizing this upper bound can be given by

$$
\operatorname* { m i n } _ { \mathbf { u } } \ J _ { 2 } = \sum _ { k = 0 } ^ { K _ { u } - 1 } \bigl ( d _ { A , R } T _ { k , 1 } + d _ { A , k } T _ { k , 2 } \bigr ) .\tag{60}
$$

By converting spherical coordinates to Cartesian coordinates, with $\theta _ { A , R } , \varphi _ { A , R } , \theta _ { R , k }$ and $\varphi _ { R , k }$ , the Cartesian coordinates of UAV and users can be represented as $( x _ { A } , y _ { A } , H _ { A } - H _ { R } )$ and $( x _ { k } , y _ { k } , - H _ { R } )$ <sup>(</sup>, respectively. For (60), the derivative of $J _ { 2 }$ <sup>)</sup>with respect to $x _ { A }$ and $y _ { A }$ respectively yields

$$
\frac { \partial J _ { 2 } } { \partial x _ { A } } = \sum _ { k = 1 } ^ { K } \Bigl ( ( x _ { A } - x _ { R } ) d _ { A , R } ^ { - 1 } T _ { k , 1 } + ( x _ { A } - x _ { k } ) d _ { A , k } ^ { - 1 } T _ { k , 2 } \Bigr ) ,\tag{61}
$$

$$
\frac { \partial J _ { 2 } } { \partial y _ { A } } = \sum _ { k = 1 } ^ { K } \Bigl ( ( y _ { A } - y _ { R } ) d _ { A , R } ^ { - 1 } T _ { k , 1 } + ( y _ { A } - y _ { k } ) d _ { A , k } ^ { - 1 } T _ { k , 2 } \Bigr ) .\tag{62}
$$

Correspondingly, the second-order derivative of $J _ { 2 }$ is expressed as

$$
\begin{array} { l } { { \displaystyle { \frac { \partial ^ { 2 } J _ { 2 } } { \partial x _ { A } ^ { 2 } } = \sum _ { k = 1 } ^ { K } d _ { A , R } ^ { - 1 } T _ { k , 1 } + d _ { A , k } ^ { - 1 } T _ { k , 2 } } } } \\ { { \displaystyle { - \sum _ { k = 1 } ^ { K } \Bigl ( ( x _ { A } - x _ { R } ) ^ { 2 } d _ { A , R } ^ { - 3 } T _ { k , 1 } + ( x _ { A } - x _ { k } ) ^ { 2 } d _ { A , k } ^ { - 3 } T _ { k , 2 } \Bigr ) } , } } \end{array}\tag{63}
$$

$$
\begin{array} { l } { { \displaystyle { \frac { \partial ^ { 2 } J _ { 2 } } { \partial y _ { A } ^ { 2 } } = \sum _ { k = 1 } ^ { K } d _ { A , R } ^ { - 1 } T _ { k , 1 } + d _ { A , k } ^ { - 1 } T _ { k , 2 } } } } \\ { { \displaystyle { - \sum _ { k = 1 } ^ { K } \biggl ( ( y _ { A } - y _ { R } ) ^ { 2 } d _ { A , R } ^ { - 3 } T _ { k , 1 } + ( y _ { A } - y _ { k } ) ^ { 2 } d _ { A , k } ^ { - 3 } T _ { k , 2 } \biggr ) } , } } \end{array}\tag{64}
$$

$$
\begin{array} { c } { { \displaystyle \frac { \partial ^ { 2 } J _ { 2 } } { \partial x _ { A } y _ { A } } = \frac { \partial ^ { 2 } J _ { 2 } } { \partial y _ { A } x _ { A } } = - \sum _ { i = 1 } ^ { K } ( ( x _ { A } - x _ { R } ) ( y _ { A } - y _ { R } ) d _ { A , k } ^ { - 3 } T _ { k , 1 } } } \\ { { - \sum _ { i = 1 } ^ { K } \biggl ( ( x _ { A } - x _ { k } ) ( y _ { A } - y _ { k } ) d _ { A , k } ^ { - 3 } T _ { k , 2 } \biggr ) . } } \end{array}
$$

Then, the Hessian matrix of $J _ { 2 }$ is given as

$$
\mathbf { H } _ { J _ { 2 } } = \left[ \begin{array} { c c } { \frac { \partial ^ { 2 } J _ { 2 } } { \partial x _ { A } ^ { 2 } } } & { \frac { \partial ^ { 2 } J _ { 2 } } { \partial x _ { A } y _ { A } } } \\ { \frac { \partial ^ { 2 } J _ { 2 } } { \partial y _ { A } x _ { A } } } & { \frac { \partial ^ { 2 } J _ { 2 } } { \partial y _ { A } ^ { 2 } } } \end{array} \right] .\tag{66}
$$

The determinant of $\mathbf { H } _ { J _ { 2 } }$ can be proven to be positive using Cauchy-Schwarz inequality. Therefore, (60) is convex, and by setting $\partial J _ { 2 } / \partial x _ { A } = 0$ and $\partial J _ { 2 } / \partial y _ { A } = 0$ , we can obtain

$$
\begin{array} { r l } & { x _ { A } \displaystyle \sum _ { k = 1 } ^ { K } \Big ( d _ { A , R } ^ { - 1 } T _ { k , 1 } + d _ { A , k } ^ { - 1 } T _ { k , 2 } \Big ) } \\ & { \quad = \displaystyle \sum _ { k = 1 } ^ { K } \Big ( x _ { R } d _ { A , R } ^ { - 1 } T _ { k , 1 } + x _ { k } d _ { A , k } ^ { - 1 } T _ { k , 2 } \Big ) , } \\ & { y _ { A } \displaystyle \sum _ { k = 1 } ^ { K } \Big ( d _ { A , R } ^ { - 1 } T _ { k , 1 } + d _ { A , k } ^ { - 1 } T _ { k , 2 } \Big ) } \\ & { \quad = \displaystyle \sum _ { k = 1 } ^ { K } \Big ( y _ { R } d _ { A , R } ^ { - 1 } T _ { k , 1 } + y _ { k } d _ { A , k } ^ { - 1 } T _ { k , 2 } \Big ) . } \end{array}\tag{67}
$$

(68)

Then, the fixed point iteration method can be used to solve (67). Furthermore, considering the impact of changes in UAV position on ${ \bf w } _ { b }$ , recalculate (51), (52), and (53), and optimize UAV position u again. Note that if $| | \mathbf { w } _ { b } | |$ increases, it means that higher transmit power is required to meet the minimum system requirements, and the iteration ends.

## B. Optimization of Digital Weight Vector

Given the position of UAV and set the transmit power $P _ { \mathrm { { m a x } } } ~ = ~ P _ { \mathrm { { m i n } } } .$ , the subproblem with respect to the digital <sup>max = mi</sup>weight vector ${ \bf w } _ { b }$ is formulated as

$$
\begin{array} { l } { { \displaystyle S 4 : ~ { \cal J } _ { 3 } = \operatorname* { m a x } _ { { \bf w } _ { b } } ~ \sum _ { k = 0 } ^ { K _ { u } - 1 } \hat { t } _ { k } } } \\ { { \mathrm { s . t . } ~ C 1 ^ { \prime } , C 2 ^ { \prime } , C 3 ^ { \prime } , } } \\ { { ~ C 7 : \| { \bf w } _ { b } \| ^ { 2 } = P _ { \operatorname* { m i n } } . } } \end{array}\tag{69}
$$

To solve this problem, the penalty function method is used to represent S4 as

$$
\begin{array} { r l r } { S 5 : } & { J _ { 4 } = \underset { \mathbf { w } _ { b } , \{ \hat { l } _ { b , k } \} } { \operatorname* { m a x } } } & { \displaystyle \sum _ { k = 0 } ^ { K _ { u } - 1 } \hat { t } _ { b , k } } \\ & { } & { \displaystyle - \xi \left( \sum _ { k = 0 } ^ { K _ { u } - 1 } | | \hat { t } _ { b , k } e ^ { j \vartheta _ { b , k } } - \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } | | ^ { 2 } \right. } \\ & { } & { \displaystyle \left. + | | t _ { b , e } e ^ { j \vartheta _ { b , e } } - \mathbf { h } _ { e } ^ { L o S } \mathbf { w } _ { b } | | ^ { 2 } + ( | | \mathbf { w } _ { b } | | ^ { 2 } - P _ { \operatorname* { m i n } } ) ^ { 2 } \right) } \\ & { \mathrm { s . t . } } & { C 3 ^ { \prime } , } \end{array}\tag{0}
$$

where ξ is the penalty variable. Given the $\mathbf { w } _ { b } , ( 7 0 )$ is simplified as the one with respect to $\hat { t } _ { b , k }$ only. Then, calculate $\partial J _ { 4 } / \partial \hat { t } _ { b , k }$ as

$$
\begin{array} { r l } & { \frac { \partial J _ { 4 } } { \partial \hat { t } _ { b , k } } = 1 - 2 \xi \hat { t } _ { b , k } + \xi \Bigl ( ( \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } ) ^ { H } e ^ { j \vartheta _ { b , k } } } \\ & { \qquad + \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } e ^ { - j \vartheta _ { b , k } } \Bigr ) . } \end{array}\tag{71}
$$

By setting $\partial J _ { 4 } / \partial \hat { t } _ { b , k } = 0$ , we can obtain

$$
\hat { t } _ { b , k } = \frac { 1 + \xi \Big ( ( \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } ) ^ { H } e ^ { j \vartheta _ { b , k } } + \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } e ^ { - j \vartheta _ { b , k } } \Big ) } { 2 \xi } .\tag{72}
$$

![](images/bd0eee24110ceb3d7edf3cbd2f3d4ea83b12309c31300238fa3f8eb898d19fa2.jpg)  
Fig. 2. An example of phase selection according to the VT method.

With $C 3 ^ { \prime } .$ , we have

$$
\xi \leq \frac { 1 } { 2 r _ { m i n , k } - \left( ( \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } ) ^ { H } e ^ { j \vartheta _ { b , k } } + \mathbf { h } _ { k } ^ { L o S } \mathbf { w } _ { b } e ^ { - j \vartheta _ { b , k } } \right) } .\tag{73}
$$

With the obtained $\hat { t } _ { b , k }$ , the subproblem with respect to ${ \bf w } _ { b }$ can be formulated as

$$
\begin{array} { r l } & { S 6 : J _ { 5 } = \displaystyle \operatorname* { m a x } _ { { \bf w } _ { b } } - \left( \sum _ { k = 0 } ^ { K _ { u } - 1 } | | \hat { t } _ { b , k } e ^ { j \vartheta _ { b , k } } - { \bf h } _ { k } ^ { L o S } { \bf w } _ { b } | | ^ { 2 } \right. } \\ & { \qquad + \left. | | t _ { b , e } e ^ { j \vartheta _ { b , e } } - { \bf h } _ { e } ^ { L o S } { \bf w } _ { b } | | ^ { 2 } + ( | | { \bf w } _ { b } ^ { T } | | ^ { 2 } - P _ { \mathrm { m i n } } ) ^ { 2 } \right) , } \end{array}\tag{74}
$$

which can be calculated through (51). According to (72) and (51), iteratively optimize $\hat { t } _ { k }$ and ${ \bf w } _ { b }$ until the constraint C4 is not satisfied and the iteration ends.

## IV. OPTIMIZATION OF REFLECTION COEFFICIENT MATRIX

In this section, we propose three methods to optimize the IRS phase shift Φ matrix based on the given UAV position and digital weight vector ${ \bf w } _ { b }$ , in order to achieve the maximum transmission rate.

## A. Proposed Vector Trajectory (VT) Method

With u and ${ \mathbf { w } } _ { b } .$ , the subproblem with respect to Φ is formulated as

$$
S 7 : J _ { 6 } = \operatorname* { m a x } _ { \Phi } \ \sum _ { k = 0 } ^ { K _ { u } - 1 } \hat { t } _ { b , k }\tag{75}
$$

For (75), the sum of user transmission rates is improved by optimizing Φ. To solve this subproblem, a vector trajectory (VT) method is proposed from the perspective of adding multiple complex numbers.

In (52) and (53), both ${ \bar { b } } _ { A , g }$ and $b _ { A , g }$ are complex values, which are obtained by summing a series of complex terms. With $\gamma _ { m } = 1 , \bar { b } _ { A , g }$ can be represented as

$$
\begin{array} { r c l } { \displaystyle \bar { b } _ { A , g } = \sum _ { m = 0 } ^ { M - 1 } \bar { b } _ { A , R , m } \bar { h } _ { R , g , m } e ^ { j \phi _ { m } } } \\ { \displaystyle } & { = \sum _ { m = 0 } ^ { M - 1 } \left. \tau _ { m } \right. e ^ { j \left( \phi _ { m } + \angle \tau _ { m } \right) } , } \end{array}\tag{76}
$$

where

$$
\bar { \mathbf { h } } _ { R , g } = \big [ \bar { h } _ { R , g , 0 } , \bar { h } _ { R , g , 1 } , \ldots , \bar { h } _ { R , g , M - 1 } \big ] ^ { T } ,\tag{77}
$$

$$
\bar { \mathbf { b } } _ { A , R } = \bar { \mathbf { G } } \mathbf { w } _ { b } = \left[ \bar { b } _ { A , R , 0 } , \bar { b } _ { A , R , 1 } , \dots , \bar { b } _ { A , R , M - 1 } \right] ^ { T } ,\tag{78}
$$

$$
\tau _ { m } = \bar { b } _ { A , R , m } \bar { h } _ { R , g , m } .\tag{79}
$$

Given u, ${ \bf w } _ { b } ,$ and $\gamma _ { m } = 1 , \ b _ { A , g }$ and $\tau _ { m }$ are fixed. At the position of user $k ,$ the projection of the unit symbol $e ^ { j \vartheta _ { b , k } }$ by ${ \bar { b } } _ { A , g }$ can be represented as

$$
\begin{array} { r c l } { { } } & { { } } & { { \displaystyle \mathrm { P r o j } _ { e ^ { j \vartheta _ { b , k } } } \bar { b } _ { A , g } = \sum _ { m = 0 } ^ { M - 1 } \left| \tau _ { m } \right| \cos \left( \phi _ { m } + \angle \tau _ { m } - \vartheta _ { b , k } \right) } } \\ { { } } & { { } } & { { \displaystyle = \sum _ { m = 0 } ^ { M - 1 } \left| \tau _ { m } \right| \cos \psi _ { m } , } } \end{array}\tag{80}
$$

where $\psi _ { m } ~ = ~ \phi _ { m } + \angle \tau _ { m } - \vartheta _ { b , k } , ~ - \pi / 2 ~ \leq ~ \psi _ { m } ~ \leq ~ \pi / 2 .$ <sup>= +</sup>According to (80), the smaller $| \psi _ { m } |$ <sup>2 2</sup>, the greater the beam gain ${ \bar { b } } _ { A , g } ,$ , which can achieve a higher user transmission rate. Accordingly, for single user scenarios, the phase shift $\phi _ { m }$ of the m-th unit of the IRS can be optimized by

$$
\begin{array} { r l } { \phi _ { m } ^ { * } = \arg \underset { \phi _ { m } \in \mathbb { F } } { \mathrm { m i n } } } & { \vert \phi _ { m } + \angle \tau _ { m } - \vartheta _ { b , k } \vert } \\ { = \arg \underset { \phi _ { m } \in \mathbb { F } } { \mathrm { m i n } } } & { \vert \psi _ { m } \vert . } \end{array}\tag{81}
$$

Taking $\tilde { B } = 2$ as an example, as shown in Fig. 2, the m-th vector approaches the imaginary axis in the second quadrant, with an expected symbol of $\bar { e ^ { j \vartheta _ { b , k } } }$ . The angle between the rotation of the m-th vector by $3 \pi / 2$ and the expected symbol is the smallest. Therefore, the optimal phase shift of this electromagnetic unit is $3 \pi / 2$

Correspondingly, the worst gain $\hat { b } _ { A , g }$ related to phase shift accuracy $\tilde { B }$ is

$$
\hat { b } _ { A , g } = \sum _ { m = 0 } ^ { M - 1 } | \tau _ { m } | \cos \frac { 2 \pi } { 2 ^ { \tilde { B } + 1 } } .\tag{82}
$$

With $\tilde { B } \ge 1 , 0 \le | \psi _ { m } | \le \pi / 2$ , and then $\widehat { b } _ { A , g } \ \geq \ 0$ . High precision phase shifters are beneficial for achieving higher gains.

For multi-user scenarios, since multiple users share the same IRS, the optimal phase shift set $\begin{array} { r l } { \phi _ { k } } & { { } = } \end{array}$ $\left[ \phi _ { 0 , k } , \phi _ { 1 , k } , \ldots , \phi _ { M - 1 , k } \right] ^ { \hat { T } }$ for each legitimate user is calcu-<sup>0 1 1</sup>lated according to (81). The phase shift values are prioritized from high to low. For example, for the k-th user, based on the gain obtained, for m-th unit, if the value of selecting the first element in $\mathbb { F }$ is greater than the value of when it is the zeroth element, then for user k, selecting the zeroth element in <sup>F</sup> for the m-th unit has a higher priority than choosing the first element. Then, according to the priority of different elements corresponding to users $k$ and IRS units, select the phase with the same priority as the corresponding element as the optimal phase for that unit. For units with different priorities, flexible design can be used to disturb the eavesdropper. According to (82), the gain of the IRS is greater than or equal to zero, which means there is no gain or forward gain for the user.

Algorithm 1 Joint Design of ${ \mathbf { w } } _ { b } .$ , u and Φ With VT Method   
1: Initialize: Iteration index $l = 0 , { \bf w } _ { b } ^ { ( 0 ) } , \Phi ^ { ( 0 ) }$   
2: repeat   
3: $l = l + 1 ;$   
4: Use fixed point iteration method to solve (67);   
5: Update $\hat { t } _ { k }$ according to (72);   
6: Update $\mathbf { w } _ { b } ^ { ( l ) }$ according to (51);   
7: until $| \mathbf { w } _ { b } ^ { ( l + 1 ) } | | ^ { 2 } - P _ { \operatorname* { m a x } } > 0$   
8: Calculate $\phi _ { m } ^ { * }$ <sup>max</sup>according to (85).   
9: Output: Suboptimal solution $\{ \phi _ { m } ^ { * } , \mathbf { w } _ { b } ^ { ( l ) } , x _ { A } ^ { ( l ) } , y _ { A } ^ { ( l ) } \}$

Specifically, introducing matrix $\Phi _ { k }$ corresponding to the $k -$ th user, i.e.,

$$
\begin{array} { r } { \Phi _ { k } = \left[ \begin{array} { c c c c } { \phi _ { k , 0 , 0 } } & { \phi _ { k , 0 , 1 } } & { \cdots \cdot } & { \phi _ { k , 0 , M - 1 } } \\ { \phi _ { k , 1 , 0 } } & { \phi _ { k , 1 , 1 } } & { \cdots \cdot } & { \phi _ { k , 1 , M - 1 } } \\ { \vdots } & { \ddots } & { \vdots } \\ { \phi _ { k , 2 ^ { \tilde { B } - 1 } , 0 } } & { \phi _ { k , 2 ^ { \tilde { B } - 1 } , 1 } } & { \cdots \cdot } & { \phi _ { k , 2 ^ { \tilde { B } - 1 } , M - 1 } } \end{array} \right] , } \end{array}\tag{83}
$$

where the columns represent IRS units, the rows represent priorities, and the phase priorities decrease with increasing row numbers. $\begin{array} { r } { \phi _ { k , \bar { p } , m } = \arg \operatorname* { m i n } _ { \phi _ { k , \bar { p } , m } \in \mathbb { F } } | \phi _ { k , \bar { p } , m } + \angle \tau _ { m } - \vartheta _ { b , k } | } \end{array}$ <sup>¯ ¯</sup>represents the phase corresponding to user k at the m-th IRS unit with priority $\bar { p } = 0 , 1 , \ldots , 2 ^ { B } - 1$ . Then, for the m-th IRS unit, the same phase set $B _ { m }$ corresponding to the same priority for all users can be represented as

$$
\boldsymbol { B _ { m } } = \{ \phi _ { k , \tilde { p } , m } \} _ { \tilde { p } \in \mathcal { P } _ { m } } ,\tag{84}
$$

where $\mathcal { P } _ { m }$ is the priority set corresponding to the same phase at the m-th IRS unit at the m-th IRS unit. Then, the optimal phase in multi-user scenarios can be represented as

$$
\phi _ { m } ^ { * } = \arg \operatorname* { m i n } _ { \phi _ { k , \tilde { p } , m } \in \mathbb { B } _ { m } } | \phi _ { k , \tilde { p } , m } + \angle \tau _ { m } - \vartheta _ { b , k } | .\tag{85}
$$

Correspondingly, the specific steps of the optimization method are summarized in Algorithm 1. $\mathbf { w } _ { b } ^ { ( l ) } , x _ { A } ^ { ( l ) }$ , and $y _ { A } ^ { ( l ) }$ represent the values obtained after the l-th iteration.

The proposed VT method optimizes $\Phi _ { m }$ based on the given $\mathbf { w } _ { b }$ and u. Using the VT method, a larger $b _ { A , R , m }$ is beneficial for achieving higher power gain. Correspondingly, the cross entropy VT (CE-VT) and block coordinate descent VT (BCD-VT) are proposed.

## B. Proposed CE-VT Algorithm

To solve (75), we introduce the cross entropy (CE) method. For the b-th symbol, the minimum cost function value is unknown, i.e., the optimal sample of $\phi$ is uncertain, where $\pmb { \phi } = [ \phi _ { 0 } , \phi _ { 1 } , \dots , \phi _ { M - 1 } ] ^ { T }$ is the phase of IRS. Specifically, a probability matrix $\mathbf { P } ^ { \left( i \right) } \in \mathbb { C } ^ { 2 ^ { \tilde { B } } \times M }$ is introduced to randomly generate X samples of $\phi ,$ and $X _ { e }$ elite samples are selected from them to estimate a new probability matrix $\mathbf { p } ^ { ( i + 1 ) }$ to generate better samples, where i is the iteration index. The probability matrix for the i-th iteration can be expressed as

$$
\begin{array} { r l } & { \mathbf { P } ^ { ( i ) } = \left[ \mathbf { p } _ { 0 } ^ { ( i ) } , \mathbf { p } _ { 1 } ^ { ( i ) } , \dots , \mathbf { p } _ { M - 1 } ^ { ( i ) } \right] , } \\ { \mathrm { w i t h } } & { \mathbf { p } _ { m } ^ { ( i ) } = \left[ p _ { m , 0 } ^ { ( i ) } , p _ { m , 1 } ^ { ( i ) } , \dots , p _ { m , \tilde { B } - 1 } ^ { ( i ) } \right] ^ { T } , } \\ { f o r } & { \qquad i = 0 , 1 , \dots , \bar { I } - 1 , } \end{array}\tag{86}
$$

where $p _ { m , \tilde { b } } ^ { ( i ) } ~ ( \tilde { b } = 0 , 1 , \ldots , 2 ^ { \tilde { B } } - 1 )$ is the probability of the b-th element in <sup>F</sup> being taken, I is the number of iterations.

Assume that all samples and all elements of the same sample are independent of each other, and for the m-th element, all elements in $\mathbf { p } _ { i , m }$ have values between 0 and 1 and the sum is 1, i.e., $\begin{array} { r } { \sum _ { \tilde { b } = 0 } ^ { 2 ^ { \tilde { B } - 1 } } p _ { m , \tilde { b } } ^ { ( i ) } = 1 } \end{array}$ and $0 \leq p _ { m , \tilde { b } } ^ { ( i ) } \leq 1$ . Then, the probability distribution function $G ( \phi ; \mathbf { P } ^ { ( i ) } )$ can be expressed as [49]

$$
\begin{array} { r l r } & { } & { G \Big ( \phi ; \mathbf { P } ^ { ( i ) } \Big ) = \displaystyle \prod _ { m = 0 } ^ { M - 1 } \left( \prod _ { \tilde { b } = 0 } ^ { 2 \tilde { B } - 1 } \left( p _ { m , \tilde { b } } ^ { i } \right) ^ { H \left( \phi _ { m } , F ( \tilde { b } ) \right) } \right) , } \\ & { } & { \mathrm { w i t h } \quad H \Big ( \phi _ { m } , F ( \tilde { b } ) \Big ) = \displaystyle \left. \begin{array} { l l } { 1 \phi _ { \mathrm { m } } = \mathbf { F } \Big ( \tilde { \mathrm { b } } \Big ) } \\ { 0 \phi _ { \mathrm { m } } \neq \mathbf { F } \Big ( \tilde { \mathrm { b } } \Big ) , } \end{array} \right. \qquad ( 8 7 ) } \end{array}
$$

where $F ( \tilde { b } )$ is the b-th entry of <sup>F</sup>. $G ( \phi ; \mathbf { P } ^ { ( i ) } )$ means that the probability that sample $\phi$ is taken when the probability matrix is $\mathbf { P } ^ { ( i ) }$ . In order to obtain better samples, X samples are sorted from large to small based on the objective function value, and the top $X _ { e }$ samples corresponding to the values are selected as elite samples. Then, the probability matrix $\mathbf { P } ^ { ( i + 1 ) }$ of the next iteration can be updated by

$$
\begin{array} { r l } { \displaystyle } & { \underset { { \bf P } ^ { ( i + 1 ) } } { \operatorname* { m a x } } X ^ { - 1 } \sum _ { \bar { x } = 0 } ^ { X _ { e } - 1 } \ln G \Big ( \pmb { \phi } _ { \bar { x } } ; { \bf P } ^ { ( i + 1 ) } \Big ) } \\ { \mathrm { s . t . } } & { \displaystyle \sum _ { \tilde { b } = 0 } ^ { 2 \tilde { B } - 1 } p _ { m , \tilde { b } } ^ { ( i ) } = 1 , 0 \leq p _ { m , \tilde { b } } ^ { ( i ) } \leq 1 , } \end{array}\tag{88}
$$

where $\phi _ { \bar { x } }$ represents the x -th sample. (88) is a convex <sup>¯ ¯</sup>optimization problem that can be solved using the CVX toolbox [50]. Then, iteratively optimize $\mathbf { w } _ { b }$ , u, and Φ, where $\pmb { \Phi } = d i a g ( \pmb { \phi } _ { \mathrm { m a x } } ) , \pmb { \phi } _ { \mathrm { m a x } }$ is the sample corresponding to the <sup>= ( max) max</sup>maximum objective function value.

According to the CE method, higher $\bar { b } _ { A , R , m }$ can be obtained, and (85) can be used to increase the transmission rate. Correspondingly, the specific steps of the optimization method are summarized in Algorithm 2. $\mathbf { w } _ { b } ^ { ( i ) } , x _ { A } ^ { ( i ) }$ , and $y _ { A } ^ { ( i ) }$ represent the values obtained after the i-th iteration.

The CE method, which learns the phase shift optimal distribution through multiple iterative sampling, has lower complexity than the exhaustive search method.

## C. Proposed BCD-VT Algorithm

By using the block coordinate descent (BCD) method, fixing M-1 reflection units and optimizing one unit, the discrete phase constraint problem can be solved.

Specifically, based on the initial phase shift matrix, ${ \bf w } _ { b }$ and Φ can be obtained using (51) and (67). Firstly, optimize the zeroth unit and fix the other M-1 units. The phase of the zeroth unit is taken from the <sup>F</sup>, i.e., the phase values in <sup>F</sup> are traversed to obtain $2 ^ { \tilde { B } }$ objective function values. Update the phase of July 05,2026 at 12:05:13 UTC from IEEE Xplore. Restrictions apply.

Algorithm 2 Joint Design Algorithm of ${ \mathbf { w } } _ { b } ,$ , u and Φ With   
CE-VT Method   
1: Initialize: Iteration index $i = 0 , \mathbf w _ { b } ^ { ( 0 ) } , \mathbf P ^ { ( 0 ) }$   
2: repeat   
3: $i = i + 1 ;$   
4: <sup>= +</sup>Obtain X samples $\{ \phi _ { \bar { x } } \} _ { \bar { x } = 0 } ^ { X - 1 }$ through $\mathbf { P } ^ { ( i ) }$   
5: repeat   
6: $l = l + 1 ;$   
7: Use fixed point iteration method to solve (67);   
8: Update $\hat { t } _ { k }$ according to (72);   
9: Update $\mathbf { \ddot { w } } _ { b } ^ { ( l ) }$ according to (51);   
10: until $| | \mathbf { w } _ { b _ { . } } ^ { ( l + 1 ) } | | ^ { 2 } - P _ { \mathrm { m a x } } > 0$   
11: Update $\bar { \mathbf { P } } ^ { ( i ) }$ according to (88);   
12: until $\mathbf { \bar { P } } ^ { ( i - 2 ) } = \mathbf { P } ^ { ( i - 1 ) } = \mathbf { \bar { P } } ^ { ( i ) }$   
13: Update $\phi _ { \mathrm { m a x } }$ <sup>= =</sup>according to (85);   
14: Output: Suboptimal solution $\{ \phi _ { \mathrm { m a x } } , \mathbf { w } _ { b } ^ { ( i ) } , x _ { A } ^ { ( i ) } , y _ { A } ^ { ( i ) } \}$   
Algorithm 3 Joint Design Algorithm of ${ \mathbf { w } } _ { b } .$ , u and Φ With   
BCD-VT Method   
1: Initialize: Iteration index $l = 0 , \tilde { b } = 0 ,$ , IRS unit index   
$m = 0 , { \bf w } _ { b } ^ { ( 0 ) } , \Phi ^ { ( 0 ) }$   
<sup>=</sup>2: repeat   
3: repeat   
4: Set the phase of the m-th IRS unit to $F ( \tilde { b } )$   
5: $\tilde { b } = \tilde { b } + \mathrm { 1 ; }$   
6: <sup>=</sup>repeat   
7: $l = l + 1 ;$   
8: Use fixed point iteration method to solve (67);   
9: Update $\hat { t } _ { k }$ according to (72);   
10: Update $\mathbf { w } _ { b } ^ { ( l ) }$ according to (51);   
11: until $| | \mathbf { w } _ { b } ^ { ( l + 1 ) } | | ^ { 2 } - P _ { \operatorname* { m a x } } > 0$   
12: until $\tilde { b } = \tilde { B }$   
13: Select the phase corresponding to the maximum objec  
tive function value as the optimal phase for the m-th   
unit.   
14: $m = m + 1 ;$   
15: until $m = M$   
16: Calculate $\phi _ { m } ^ { * }$ according to (85).   
17: Output: Suboptimal solution $\{ \phi _ { m } ^ { * } , \mathbf { w } _ { b } ^ { ( l ) } , x _ { A } ^ { ( l ) } , y _ { A } ^ { ( l ) } \}$

the zeroth element to the phase corresponding to the maximum objective function value. Then, optimize the m-th element and fix the M-1 elements until the last element is optimized.

According to the BCD method, higher $\bar { b } _ { A , R , m }$ can be obtained, and (85) can be used to increase the transmission rate. Correspondingly, the specific steps of the optimization method are summarized in Algorithm 3.

## V. SIMULATION RESULTS

In this section, we evaluated the transmission rate and security performance of a multi-user UAV-DM system through simulation. The UAV is equipped with N 24 antennas, and the number of electromagnetic units on the IRS is $M = 5 7 6$ where $M _ { Y } = M _ { Z } = 2 4$ . The initial position of the UAV is random. The IRS is 1 meter above the ground and its position is (0m, 0m, 0m). The three ground users are located at (10m, 15m, −1m), (20m, 10m, −1m), and $( 1 5 m , 2 0 m , - 1 m )$ respectively. The Eve’s position is (10m, 20m, −1m). The carrier frequency is 50GHz, and $\delta ^ { 2 } = - 1 1 0 d B m$ . The array aperture is 0.39m, and the Rayleigh distance is 50.75m. In simulation, the computer we used is 13-th Gen Intel (R) Core (TM) i7-13700KF 3.40 GHz and 32GB RAM. The main parameters are shown in Table I.

TABLE I THE SIMULATION PARAMETERS
<table><tr><td>Parameters</td><td>Values</td></tr><tr><td>UAV height Number of antennas Number of users</td><td> $H _ { u } = 1 0 0 m$   $N = 2 4$   $K _ { u } = 3$ </td></tr><tr><td>minimum symbol power</td><td> $r _ { m } i n = - 8 0 d B m$ </td></tr><tr><td>represent the LoS power ratio coefficients</td><td> $\varepsilon _ { A , R } = \varepsilon _ { R , g } = \varepsilon _ { A , g } = 0 . 9$ </td></tr><tr><td>Channel power gain per unit distance Power of noise</td><td> $\rho \stackrel { \cdot \cdot } { = } 1 0 ^ { - 3 }$   $\delta ^ { 2 } \stackrel { \prime } { = } - 1 1 0 d B m$ </td></tr></table>

94   
1 。CE in [39]   
92 -  -BCD in [24]   
90   
88   
(dmm) 86 84   
) 82   
Q   
80   
78   
76   
o o o o o e   
74   
0 2 4 6 8 10 12   
Iterations  
Fig. 3. Minimum transmission power $P _ { \mathrm { m i n } }$ versus number of iterations.

![](images/4d542af5ccb4ef0c51516e6af1e8c6444652efdcbb86e6d3aa3fd9411ae89f5e.jpg)  
Fig. 4. The average signal power of different methods.

The convergence curves under the CE method and BCD method are shown in Fig. 3. We investigate the average power under different algorithms, including the vector trajectory (VT) method, cross entropy (CE) method, block coordinate descent (BCD) method, CE-VT algorithm, and BCD-VT algorithm. The deployment without IRS is considered a benchmark, i.e., no IRS. From Fig. 4, it can be observed that as $P _ { m a x }$ increases, the CE-VT algorithm proposed can achieve a signal power improvement of about 6 dBm higher than the CE method, and the BCD-VT algorithm can achieve a signal power improvement of about 5.5 dBm higher than the BCD method, and has a higher performance improvement compared to the VT method. Compared to deploying without RIS, exploiting the CE-VT method, IRS can achieve a signal power gain of 31 dBm. Fig. 5 shows the beam responses obtained using the CE-VT algorithm, which represents the power distribution of the received signal within the region.

![](images/92bf7635269009f66fc6583e7c343af09b4ef345cf70c84629a022b6f639624b.jpg)

Fig. 5. Beam response. The asterisk represents the user, and the circle is the eavesdropper.  
![](images/428600fe48609908e436aa93987ea632c32376136a15d12acaf3b0cfe2163f0c.jpg)  
Fig. 6. The BER of different methods for the zeroth user and Eve.

![](images/8d1a295fa77694078d3b1a2b2b5e8450fc062b710b30bb34bdd88a04f0e0541f.jpg)  
Fig. 7. BER at different locations. The asterisk represents the user, and the circle is the Eve.

![](images/e756b1ca0bff539fc07854b87ec6e345fcf1bc22b3fad76c45fc9bf5a36f9eac.jpg)  
Fig. 8. The achievable transmission rate without uncertain component interference.

![](images/e93986dd5d72743f1115a87e472d8533965c0de7d538e1e3d9eb0790bfef9f9f.jpg)  
Fig. 9. The achievable transmission rate with uncertain component interference.

With a maximum transmission power of $P _ { m a x } = 7 3 . 6 ~ d B m .$ the power of the three users (red asterisk) is −50 dBm, and the eavesdropping (red circle) position is −110 dBm. The proposed method can achieve high power at the user’s location and low power at the eavesdropper’s location.

Fig. 6 illustrates the bit error rate (BER) of the zeroth user at different power spectral densities $N _ { 0 } / 2 .$ . The proposed method <sup>0</sup>has a low bit error rate (BER) at the user’s location and a high BER at the Eve’s location. If $N _ { 0 } / 2$ is less than $1 0 ^ { - 4 . 5 }$ , the VT method is used to maintain an extremely low BER level at the user’s location, and the BER at the Eve’s location gradually increases. If $N _ { 0 } / 2$ is less than $1 0 ^ { - 5 . 1 }$ , and the CE, BCD, CE-<sup>0</sup>VT, and BCD-VT algorithms are used to maintain extremely low BER levels at the user’s location. The BER of the CE and BCD methods at the Eve’s location remains around 0.5, and the BER at the Eve’s location gradually increases under the CE-VT and BCD-VT algorithms. At a signal-to-noise ratio (SNR) of 12 dB, the BER obtained using the BCD method is shown in Fig. 7.

Figs. 8 and 9 illustrate the achievable transmission rates with signal uncertain component interference and without uncertain component, respectively. In Fig. 8, as the maximum transmission power increases, the achievable transmission rate is increased. The achievable transmission rates with CE-VT and BCD-VT are superior to the CE method and BCD method, July 05,2026 at 12:05:13 UTC from IEEE Xplore. Restrictions apply.

![](images/f35fe7393219104b612500f79edafb4edfbc4942a5e5a24970c4d610d7633091.jpg)  
Fig. 10. The achievable transmission rate for different numbers of users.

![](images/c55da6d9aa8d0b312adbdbd743f115549d5cb4ce823add65f02cb0d90a623127.jpg)  
Fig. 11. The achievable transmission rates under different quantization precision.

respectively. Compared to the benchmark without IRS deployment, the proposed CE-VT method can achieve approximately three times the rate gain. In Fig. 9, with uncertain component, the achievable transmission rates under BCD method and BCD-VT are relatively low, the CE method and CE-VT algorithm can achieve higher achievable transmission rates, which tend to stabilize at a maximum transmission power of 50 dBm. For the CE-VT algorithm, the rate improvement obtained is approximately double that of the CE method. Fig. 10 shows the achievable transmission rates for different numbers of users, demonstrating that the proposed scheme is effective for different numbers of users. As shown in Fig. 11, with lower quantization accuracy, higher rate performance can be achieved than without IRS deployment, and the achievable rates increase as quantization accuracy increases. Therefore, exploiting IRS with low phase shift precision can provide more degrees of freedom for DM systems to achieve higher transmission rates, which validates the effectiveness of the proposed methods.

## VI. CONCLUSION

A symbol level design scheme based on DM is proposed for the IRS-assisted UAV communication scenario. In order to realize the maximum transmission rate of UAV-DM system under the constraints of receiver symbol e, receiver sensitivity, maximum transmit power, IRS discrete phase shift, constant modulus and position range, the joint design of digital weight vector, UAV position and IRS phase shift matrix is studied. The scheme first obtains the sub-optimal UAV position by minimizing power. According to the obtained UAV position, the digital weight vector is scaled up to make full use of the given transmitting power. Then, based on the obtained UAV position and digital weight vector, a vector trajectory method is proposed to optimize the IRS phase shift matrix. This method has low complexity, and can be combined with the traditional discrete phase shift optimization method to obtain a higher transmission rate. Simulation results show that the proposed schemes can achieve low bit error rate at the user’s location and high bit error rate at the eavesdropper’s location, and has better transmission rate performance than the traditional CE and BCD methods. Particularly, the rate of the proposed CE-VT is approximately twice that of the CE and far better than those of the remaining methods.

## REFERENCES

[1] J. Li et al., “Mobility support for millimeter wave communications: Opportunities and challenges,” IEEE Commun. Surveys Tuts., vol. 24, no. 3, pp. 1816–1842, 3rd Quart., 2022.

[2] H. Wang, H. Zhao, J. Zhang, D. Ma, J. Li, and J. Wei, “Survey on unmanned aerial vehicle networks: A cyber physical system perspective,” IEEE Commun. Surveys Tuts., vol. 22, no. 2, pp. 1027–1070, 2nd Quart., 2019.

[3] Y. Cao, S. Xu, J. Liu, and N. Kato, “Toward smart and secure V2X communication in 5G and beyond: A UAV-enabled aerial intelligent reflecting surface solution,” IEEE Veh. Technol. Mag., vol. 17, no. 1, pp. 66–73, Mar. 2022.

[4] W. Jiang, B. Ai, M. Li, W. Wu, and X. Shen, “Average age-ofinformation minimization in aerial IRS-assisted data delivery,” IEEE Internet Things J., vol. 10, no. 17, pp. 15133–15146, Sep. 2023.

[5] W. Wu, F. Zhou, B. Wang, Q. Wu, C. Dong, and R. Q. Hu, “Unmanned aerial vehicle swarm-enabled edge computing: Potentials, promising technologies, and challenges,” IEEE Wireless Commun., vol. 29, no. 4, pp. 78–85, Aug. 2022.

[6] H. Hellaoui, M. Bagaa, A. Chelli, T. Taleb, and B. Yang, “On supporting multiservices in UAV-enabled aerial communication for Internet of Things,” IEEE Internet Things J., vol. 10, no. 15, pp. 13754–13768, Aug. 2023.

[7] G. B. Tarekegn, R.-T. Juang, H.-P. Lin, Y. Y. Munaye, L.-C. Wang, and M. A. Bitew, “Deep-reinforcement-learning-based drone base station deployment for wireless communication services,” IEEE Internet Things J., vol. 9, no. 21, pp. 21899–21915, Nov. 2022.

[8] C. You, Z. Kang, Y. Zeng, and R. Zhang, “Enabling smart reflection in integrated air-ground wireless network: IRS meets UAV,” IEEE Wireless Commun., vol. 28, no. 6, pp. 138–144, Dec. 2021.

[9] X. Liu, Y. Yu, F. Li, and T. S. Durrani, “Throughput maximization for RIS-UAV relaying communications,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 10, pp. 19569–19574, Oct. 2022.

[10] X. Liu, B. Lai, B. Lin, and V. C. Leung, “Joint communication and trajectory optimization for multi-UAV enabled mobile internet of vehicles,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 9, pp. 15354–15366, Sep. 2022.

[11] S. Zeng, H. Zhang, B. Di, and L. Song, “Trajectory optimization and resource allocation for OFDMA UAV relay networks,” IEEE Trans. Wireless Commun., vol. 20, no. 10, pp. 6634–6647, Oct. 2021.

[12] S. Zhang, Z. Shi, and J. Liu, “Joint trajectory design and resource allocation for secure-air-ground integrated IoT networks,” IEEE Internet Things J., vol. 10, no. 23, pp. 20458–20471, Dec. 2023.

[13] X. Yu, X. Huang, K. Wang, F. Shu, and X. Dang, “Joint design of power allocation, beamforming, and positioning for energy-efficient UAV-aided multiuser millimeter-wave systems,” IEEE J. Sel. Areas Commun., vol. 40, no. 10, pp. 2930–2945, Oct. 2022.

[14] X. Liang, Q. Deng, F. Shu, and J. Wang, “Energy-efficiency joint trajectory and resource allocation optimization in cognitive UAV systems,” IEEE Internet Things J., vol. 9, no. 22, pp. 23058–23071, Nov. 2022.

[15] Z. Na, C. Ji, B. Lin, and N. Zhang, “Joint optimization of trajectory and resource allocation in secure UAV relaying communications for Internet of Things,” IEEE Internet Things J., vol. 9, no. 17, pp. 16284–16296, Sep. 2022.

[16] Y. Wang et al., “UAV-enabled secure communication with finite blocklength,” IEEE Trans. Veh. Technol., vol. 69, no. 12, pp. 16309–16313, Dec. 2020.

[17] Z. Li, X. Liao, J. Shi, L. Li, and P. Xiao, “MD-GAN-based UAV trajectory and power optimization for cognitive covert communications,” IEEE Internet Things J., vol. 9, no. 12, pp. 10187–10199, Jun. 2022.

[18] Y. Wang, S. Yan, X. Zhou, Y. Huang, and D. W. K. Ng, “Covert communication with energy replenishment constraints in UAV networks,” IEEE Trans. Veh. Technol., vol. 71, no. 9, pp. 10143–10148, Sep. 2022.

[19] Y. Su, S. Fu, J. Si, C. Xiang, N. Zhang, and X. Li, “Optimal hovering height and power allocation for UAV-aided NOMA covert communication system,” IEEE Wireless Commun. Lett., vol. 12, no. 6, pp. 937–941, Jun. 2023.

[20] J. Hu, S. Yan, X. Zhou, F. Shu, and J. Wang, “Covert communications without channel state information at receiver in IoT systems,” IEEE Internet Things J., vol. 7, no. 11, pp. 11103–11114, Nov. 2020.

[21] V. Hassija et al., “Fast, reliable, and secure drone communication: A comprehensive survey,” IEEE Commun. Surveys Tuts., vol. 23, no. 4, pp. 2802–2832, 4th Quart., 2021.

[22] X. Zhou, S. Yan, F. Shu, R. Chen, and J. Li, “UAV-enabled covert wireless data collection,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3348–3362, Nov. 2021.

[23] F. Shu et al., “Beamforming and phase shift design for HR-IRS-aided directional modulation network with a malicious attacker,” IEEE Trans. Wireless Commun., vol. 23, no. 8, pp. 9016–9032, Aug. 2024.

[24] W. Shi, Q. Wu, F. Xiao, F. Shu, and J. Wang, “Secrecy throughput maximization for IRS-aided MIMO wireless powered communication networks,” IEEE Trans. Commun., vol. 70, no. 11, pp. 7520–7535, Nov. 2022.

[25] M. Li et al., “Multi-carrier based positional modulation design with discrete phase values for metasurface elements,” Digit. Signal Process., vol. 137, Jun. 2023, Art. no. 104047.

[26] M. Li, B. Zhang, B. Zhang, W. Liu, T. Kim, and C. Wang, “Directional modulation design for multi-beam multiplexing based on hybrid antenna array structures,” EURASIP J. Adv. Signal Process., vol. 2023, no. 1, p. 64, 2023.

[27] M. Li, B. Zhang, B. Zhang, Y. Ding, T. Kim, and X. Zhao, “Symbol-level design for joint radar communication based on directional modulation,” IEEE Wireless Commun. Lett., vol. 13, no. 2, pp. 442–445, Feb. 2024.

[28] A. Babakhani, D. B. Rutledge, and A. Hajimiri, “Transmitter architectures based on near-field direct antenna modulation,” IEEE J. Solid-State Circuits, vol. 43, no. 12, pp. 2674–2692, Dec. 2008.

[29] M. P. Daly and J. T. Bernhard, “Directional modulation technique for phased arrays,” IEEE Trans. Antennas Propag., vol. 57, no. 9, pp. 2633–2640, Sep. 2009.

[30] Y. Ding and V. F. Fusco, “Directional modulation far-field pattern separation synthesis approach,” IET Microw. Antennas Propagat., vol. 9, no. 1, pp. 41–48, 2015.

[31] Q. J. Zhu, S. W. Yang, R. L. Yao, and Z. P. Nie, “Directional modulation based on 4-D antenna arrays,” IEEE Trans. Antennas Propag., vol. 62, no. 2, pp. 621–628, Feb. 2014.

[32] K. Chen, S. Yang, Y. Chen, S.-W. Qu, and J. Hu, “Hybrid directional modulation and beamforming for physical layer security improvement through 4-D antenna arrays,” IEEE Trans. Antennas Propag., vol. 69, no. 9, pp. 5903–5912, Dec. 2021.

[33] L. Chen, W. Chen, Y. Liu, C. Yang, and Z. Feng, “An efficient directional modulation transmitter with novel crest factor reduction technique,” IEEE Microw. Wireless Compon. Lett., vol. 29, no. 8, pp. 554–556, Aug. 2019.

[34] S. Y. Nusenu, S. Huaizong, Y. Pan, and A. Basit, “Directional modulation with precise legitimate location using time-modulation Retrodirective frequency diversity array for secure IoT communications,” IEEE Syst. J., vol. 15, no. 1, pp. 1109–1119, Mar. 2021.

[35] A. Narbudowicz, A. Zandamela, N. Marchetti, and M. J. Ammann, “Energy-efficient dynamic directional modulation with electrically small antennas,” IEEE Antennas Wireless Propag. Lett., vol. 21, no. 4, pp. 681–684, Apr. 2022.

[36] A. A. Khuwaja, Y. Chen, N. Zhao, M.-S. Alouini, and P. Dobbins, “A survey of channel modeling for UAV communications,” IEEE Commun. Surveys Tuts., vol. 20, no. 4, pp. 2804–2821, 4th Quart., 2018.

[37] J. Sun, K. Guo, F. Zhou, X. Wang, and M. Zhu, “Ris-aided integrated satellite duplex UAV relay terrestrial networks with imperfect hardware and co-channel interference,” EURASIP J. Adv. Signal Process., vol. 2023, no. 1, p. 109, 2023. [Online]. Available: https://doi.org/10.1186/s13634-023-01067-2

[38] Z. Wei, C. Masouros, and F. Liu, “Secure directional modulation with few-bit phase shifters: Optimal and iterative-closed-form designs,” IEEE Trans. Commun., vol. 69, no. 1, pp. 486–500, Jan. 2021.

[39] J. Yao, J. Xu, W. Xu, D. W. K. Ng, C. Yuen, and X. You, “Robust beamforming design for RIS-aided cell-free systems with CSI uncertainties and capacity-limited backhaul,” IEEE Trans. Commun., vol. 71, no. 8, pp. 4636–4649, Aug. 2023.

[40] F. Shu et al., “A new heterogeneous hybrid massive MIMO receiver with an intrinsic ability of removing phase ambiguity of DOA estimation via machine learning,” IEEE Trans. Mach. Learn. Commun. Netw., vol. 3, pp. 17–29, 2025.

[41] M. Cui, Z. Wu, Y. Lu, X. Wei, and L. Dai, “Near-field MIMO communications for 6G: Fundamentals, challenges, potentials, and future directions,” IEEE Commun. Mag., vol. 61, no. 1, pp. 40–46, Jan. 2023.

[42] J. Hu, S. Yan, F. Shu, J. Wang, J. Li, and Y. Zhang, “Artificial-noiseaided secure transmission with directional modulation based on random frequency diverse arrays,” IEEE Access, vol. 5, pp. 1658–1667, 2017.

[43] F. Shu et al., “Enhanced secrecy rate maximization for directional modulation networks via IRS,” IEEE Trans. Commun., vol. 69, no. 12, pp. 8388–8401, Dec. 2021.

[44] B. Zhang et al., “Directional modulation design under a given symbolindependent magnitude constraint for secure IoT networks,” IEEE Internet Things J., vol. 8, no. 20, pp. 15140–15147, Oct. 2021.

[45] D. Tse and P. Viswanath, Fundamentals of Wireless Communication. Cambridge, U.K.: Cambridge Univ. Press, 2005.

[46] Y. Ding and V. Fusco, “BER-driven synthesis for directional modulation secured wireless communication,” Int. J. Microw. Wireless Technol., vol. 6, no. 2, pp. 139–149, 2014.

[47] X. Zhou, S. Yan, J. Hu, J. Sun, J. Li, and F. Shu, “Joint optimization of a UAV’s trajectory and transmit power for covert communications,” IEEE Trans. Signal Process., vol. 67, no. 16, pp. 4276–4290, Aug. 2019.

[48] Q. Liu, L. Shi, L. Sun, J. Li, M. Ding, and F. Shu, “Path planning for UAV-mounted mobile edge computing with deep reinforcement learning,” IEEE Trans. Veh. Technol., vol. 69, no. 5, pp. 5723–5728, May 2020.

[49] W. Chen, X. Ma, Z. Li, and N. Kuang, “Sum-rate maximization for intelligent reflecting surface based terahertz communication systems,” in Proc. IEEE/CIC Int. Conf. Commun. Workshops China (ICCC Workshops), 2019, pp. 153–157.

[50] C. Research. “CVX: MATLAB software for disciplined convex programming, version 2.0 beta.” Sep. 2012. [Online]. Available: http://cvxr.com/cvx

![](images/0d20bc1fbd6f6eeb41cb2c566be0ff842b783922572923e626c4e915034b64fe.jpg)  
Maolin Li is currently pursuing the Ph.D. degree with the School of Information and Communication Engineering, Hainan University, Haikou, China. His research interests include massive MIMO, physical layer security, and intelligent reflecting surface.

![](images/cd090e48823631171202f998c9952e02392f7221196ed39c23d792c1f6fb714f.jpg)

Wei Gao received the B.E. degree in communication engineering and the Ph.D. degree in information and communication engineering from the Huazhong University of Science and Technology in 2014 and 2020, respectively. He is currently a Postdoctoral Fellow with Hainan University. His research interests include network architecture, wireless network access, and radio resources allocation.

![](images/5a3ab76ebc0dfce686ed7b1806bc297a0691147a028f5afc088bfb4e1a954c9b.jpg)  
Qi Wu received the Ph.D. degree from Southeast University, Nanjing, China, in 2009. He is currently an Associate Professor of Control Science and Engineering with the School of Electronic, Information and Electrical Engineering, Shanghai Jiao Tong University, Shanghai, China. His current research interests include pattern recognition and fault diagnosis.

![](images/a9f8a34bb02e5cca3370ab558cb5e58b5a0ee900111d8b0d66f35725e4fd422e.jpg)

Cunhua Pan (Senior Member, IEEE) received Ph.D degree from Southeast University, China, in 2015, where he is a Full Professor. He has published over 200 IEEE journal papers. His papers got over 19000 Google Scholar citations with H-index of 70. His research interests mainly include reconfigurable intelligent surfaces, AI for Wireless, near field communications and sensing, and integrated sensing and communications. He is Clarivate Highly Cited researcher.

![](images/8cfc17f2e7d1e42990a7cb96479485b6b5c1d27921452ad0dde693e70dbc3767.jpg)

Feng Shu (Member, IEEE) was born in 1973. He received the B.S. degree from Fuyang Teaching College, Fuyang, China, in 1994, the M.S. degree from Xidian University, Xi’an, China, in 1997, and the Ph.D. degree from Southeast University, Nanjing, China, in 2002. From 2009 to 2010, he was a Visiting Postdoctoral Fellow with the University of Texas at Dallas, Richardson, TX, USA. From July 2007 to September 2007, he was a Visiting Scholar with the Royal Melbourne Institute of Technology, Melbourne, VIC, Australia. From 2005 to 2020, he was with the School of Electronic and Optical Engineering, Nanjin University of Science and Technology, Nanjing, where he was promoted from an Associate Professor to a Full Professor of supervising Ph.D. students in 2013. Since 2020, he has been with the School of Information and Communication Engineering, Hainan University, Haikou, China, where he is currently a Professor and a Supervisor of Ph.D. and graduate students. Since October 2024, he also has been with the School of Information Science and Technology, Tibet University. He has authored or coauthored more than 400 in archival journals with more than 150 papers on IEEE journals and 280 SCI-indexed papers. His citations are more than 9119 times. He holds one U.S. patent and about 50 Chinese patents. He is also a PI or a CoPI for eight national projects. His research interests include machine learning, wireless networks, wireless location, and array signal processing. He was awarded with the Fujian Prize for Natural Sciences in 2024, the Leading-Talent Plan of Hainan Province in 2020, the Fujian Hundred-Talent Plan of Fujian Province in 2018, and the Mingjian Scholar Chair Professor in 2015. From 2019 to 2024, he is ranked in the 2% Top Scientists by Stanford/Elsevier, and enters the list of 1% Top scientists in 2024. He was an Exemplary Reviewer of IEEE TRANSACTIONS ON COMMUNICATIONS in 2020. He is currently an Editor of IEEE WIRELESS COMMUNICATIONS LETTERS and was a Guest Editor for the journals Chinese Journal of Aeronautics and Journal of Electronics and Information Technology. He was an Editor of IEEE SYSTEMS JOURNAL from 2019 to 2021 and IEEE ACCESS from 2016 to 2018, and also a Guest Editor of IET Communications and Security and Safety.

![](images/21ce839089f85499171f8a00c9b7c88af7dfc0307ed34635c8ff4015acc83093.jpg)

Di Wu received the M.S. degree in information and communication engineering from Hainan University, Haikou, China, in 2018, and the Ph.D. degree in control science and engineering from Shanghai Jiao Tong University, Shanghai, China, in March 2025. From October 2023 to October 2024, he participated in a Ph.D. Joint Training Program with the University of Naples Federico II, Naples, Italy. He currently holds the position of Lecturer with the School of Information and Communication Engineering, Hainan University. His research interests include nonlinear control of aerial vehicles, multiagent communication, and localization and mapping.