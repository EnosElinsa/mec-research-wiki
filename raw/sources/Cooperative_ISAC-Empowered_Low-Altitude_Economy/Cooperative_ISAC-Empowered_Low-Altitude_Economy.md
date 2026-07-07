# Cooperative ISAC-Empowered Low-Altitude Economy

Jun Tang , Yiming Yu , Cunhua Pan , Senior Member, IEEE, Hong Ren , Member, IEEE, Dongming Wang , Jiangzhou Wang , Fellow, IEEE, and Xiaohu You , Fellow, IEEE

Abstract— This paper proposes a cooperative integrated sensing and communication (ISAC) scheme for low-altitude sensing scenario, aiming at estimating the parameters of the uncrewed aerial vehicles (UAVs) and enhancing the sensing performance via cooperation. The proposed scheme consists of two stages. In Stage I, we formulate the monostatic parameter estimation problem via using a tensor decomposition model. By leveraging the Vandermonde structure of the factor matrix, a spatial smoothing tensor decomposition scheme is introduced to estimate the UAVs’ parameters. To further reduce the computational complexity, we design a reduced-dimensional (RD) angle of arrival (AoA) estimation algorithm based on generalized Rayleigh quotient (GRQ). In Stage II, the positions and true velocities of the UAVs are determined through the data fusion across the multiple base stations (BSs). Specifically, we first develop a false removing minimum spanning tree (MST)-based data association method to accurately match the BSs’ parameter estimations to the same UAV. Then, a Pareto optimality method and a residual weighting scheme are developed to facilitate the position and velocity estimation, respectively. We further extend our approach to the dual-polarized system. Simulation results validate the effectiveness of the proposed schemes in comparison to conventional techniques.

Index Terms— Integrated sensing and communication (ISAC), cooperative sensing, tensor decomposition, parameter estimation, data fusion.

## I. INTRODUCTION

N THE forthcoming fifth-generation advanced (5G-A) and sixth-generation (6G) mobile communication systems, the plethora of low-altitude applications in transportation, tourism, agriculture and emergency services boosts the burgeoning of low-altitude economy (LAE) [1]. In LAE, the interaction between the uncrewed aerial vehicles (UAVs) and the base stations (BSs) is critical. On one hand, the UAVs need to communicate with the BSs for data transmission. On the other hand, the BSs are also supposed to sense and detect the UAVs to prevent the unauthorized intrusion or collision. To this end, the novel paradigm known as integrated sensing and communication (ISAC) is recognized as a promising solution. Compared to conventional radar deployment, ISAC systems can simultaneously achieve superior sensing capabilities and high data transmission rates [2].

In low-altitude sensing scenarios, depending on the spatial deployment of the transmitter and the receiver, ISAC configurations can be classified into three primary categories: monostatic [3], [4], bistatic [5], [6] and multistatic [7], [8]. Specifically, in bistatic and multistatic systems, one or several BSs act as the transmitters with others serving as the receivers to receive the sensing symbols. However, these configurations impose high requirements on the deployment locations and the synchronization across the multiple BSs. Differently, in monostatic setup, the BS transmits the sensing symbols simultaneously while receiving the echo signals reflected by the UAVs, which simplifies the deployment of the BS and enhances the system’s tolerance to asynchronization. However, conventional monostatic configuration still faces several challenges. First, due to path loss, the sensing performance for the distant UAVs is relatively poor [9]. In addition, if there are obstructions (such as tall buildings or trees) between the UAVs and the BSs, the detection probability will decrease dramatically. Moreover, the comprehensive status of the UAVs, such as their true velocities cannot be fully derived, since only the radial velocities can be estimated from the echo signals [7].

To overcome the above limitations of conventional monostatic configuration, the cooperative ISAC framework was proposed [10], [11], [12], [13], [14]. In cooperative ISAC networks, each BS first estimates the targets’ parameters from the received echo signals. Then, the estimated parameters are fused in the cloud to enhance the sensing performance. In this scenario, the targets that are far from a certain BS may be relatively close to other BSs, thereby enhancing the detection probability and the coverage of the ISAC network. Moreover, more diverse sensing directions and richer targets information brought by the distributed deployment of the BSs further boost the sensing performance, thereby reducing the

Digital Object Identifier 10.1109/TWC.2025.3542399 estimation error and enabling the ability to recover more comprehensive information of the UAVs, such as their true velocities in three-dimensional (3-D) space. Recent studies in the field of cooperative ISAC have aimed at designing the sensing solutions to facilitate the sensing capabilities in various scenarios. In single-antenna setup, [12], [13] designed the two-stage target localization schemes in the orthogonal frequency division multiplexing (OFDM) network, where the ranges of the targets were respectively derived via the compressed sensing (CS) and the two-dimensional (2-D) fast Fourier transform (FFT) algorithms, then the targets’ positions were estimated based on the range estimations. Likewise, [14] first derived the target’s range and radial velocity, and then proposed a symbol-level fusion scheme across the multiple BSs to facilitate the position and velocity estimation. In multiantenna setup, in addition to the ranges and velocities, the BSs are also supposed to capture the angles of arrival (AoAs) of the targets to further enhance the sensing performance, and several classic AoA estimation techniques such as the multiple signal classification (MUSIC) algorithm have been adopted to derive the targets’ AoAs in ISAC systems [15]. Beyond the aforementioned conventional estimation methods, tensor techniques are gaining increasing popularity for extracting the multi-dimensional parameters recently, and have been applied for channel and target parameter estimation. The reason lies in the fact that these techniques can achieve higher estimation accuracy and the derived multi-dimensional parameters are automatically paired [16], [17], [18], [19]. The authors of [19] delved into a preliminary exploration of the tensor-based ISAC, where the channel and target parameter estimation were achieved through a unified tensor approach. However, [19] did not reveal the benefits of improving the sensing accuracy through the multi-BS cooperation.

As previously mentioned, although the above studies have preliminarily demonstrated the potential of cooperative ISAC configuration, most of the existing studies only considered some special scenarios of cooperative ISAC networks (such as single-antenna or single-target cases), lacking the generality to extend to the more complex and practical scenarios. Specifically, for the monostatic parameter estimation, several estimation algorithms only considered the single-target scenarios, when these algorithms are extended to multi-target scenario, additional pairing procedures are supposed to be designed to match the multi-dimensional parameters to the same target. For the multi-BS cooperation, the data association across the BSs is another critical issue in multi-target scenario. Although several association methods have been developed [12], [13], they are merely designed for singleantenna setup. To address these issues, this paper aims to provide a comprehensive scheme for a more general multiantenna multi-target sensing scenario within the cooperative ISAC framework. The main contributions of this work are summarized as follows:

1) We consider a general cooperative ISAC system, aiming at sensing the multiple UAVs via the cooperation across the multiple multi-antenna BSs. To address the challenging sensing issue, a comprehensive sensing scheme is developed.

2) First, several preliminary steps are presented to provide some prior information and guidelines for the subsequent sensing scheme. Then, the monostatic parameter estimation problem is formulated via using a tensor decomposition model. By leveraging the Vandermonde structure of the factor matrix, a spatial smoothing tensor decomposition algorithm is developed to derive the AoAs, ranges, radial velocities, and channel coefficients of the UAVs. Additionally, we develop a reduceddimensional (RD) AoA estimation algorithm based on generalized Rayleigh quotient (GRQ) to further reduce the complexity.

3) Subsequently, a false removing minimum spanning tree (MST)-based multi-BS data association method is presented. Compared to the conventional exhaustive permutation method, this approach not only prevents the false detections from impacting the subsequent data fusion, but also reduces the complexity when there are a large number of UAVs.

4) Finally, a Pareto optimality method and a residual weighting scheme are presented to facilitate the position and velocity estimation, respectively.

5) We also extend our approach to the dual-polarized system via a fourth-order tensor decomposition formulation, which improves the estimation accuracy when the array size is limited.

The remainder of this paper is organized as follows. In Section II, we present the signal and channel model of the cooperative ISAC system. In Section III, we provide several preliminary steps for the proposed cooperative sensing scheme. In Section IV, the parameter estimation problem is formulated via using a tensor decomposition model, and a spatial smoothing tensor decomposition scheme is developed. In Section V, we estimate the positions and velocities of the UAVs. In Section VI, we extend our approach to the dualpolarized system. Finally, the simulations and conclusion are provided in Sections VII and VIII, respectively.

Notations: Lowercase letter, boldface lowercase letter, boldface uppercase letter and calligraphy uppercase letter denote the scalars, vectors, matrices and tensors, respectively, i.e., y, $\mathbf { y } , \ \mathbf { Y } , \mathbf { \mathcal { P } } .$ . The operations $( \cdot ) ^ { \ast } , ( \cdot ) ^ { T } , ( \cdot ) ^ { \bar { H } }$ and (·)<sup>†</sup> represent the conjugate, transpose, Hermitian transpose, and Pseudoinverse, respectively. The notations $\operatorname { T r } ( \mathbf { Y } ) , \ \lVert \mathbf { Y } \rVert _ { F } , \ \lVert \mathbf { y } \rVert _ { 2 }$ and |y| denote the trace of matrix Y, the Frobenius norm of matrix $\mathbf { Y } ,$ , the L2-norm of vector y, and the modulus of scalar $y ,$ respectively. The notations <sup>R</sup> and <sup>C</sup> represent the real field and the complex field, respectively. The symbol $[ \mathbf { Y } ] _ { i j }$ refers to the (i, j)-th entry of matrix Y. The operators ◦, ⊗ and ⊙ denote the outer product, Kronecker product and Khatri-Rao product, respectively. The notation D (y) denotes the diagonal matrix formed by vector y. The operation unvec $M \times N \left( \mathbf { y } \right)$ rearranges $M N \times 1$ vector y into $M \times N$ matrix Y. For two sets A and $B , A \cup B$ denotes the set $\{ x | x \in A$ or $x \in B \}$ , and $\mathcal A \backslash B$ denotes the set $\{ x | x \in A$ and x $\rangle \notin B \}$

## II. SYSTEM MODEL

## A. Signal Model

As shown in Fig. 1, we consider a cooperative ISAC system aiming at sensing the low-altitude UAVs’ flight status, including their positions and velocities. In this system, J BSs first estimate the parameters of the UAVs from the echo signals, then the estimated parameters are fused in the cloud to enhance the sensing performance. In order to avoid the interference between the BSs, we assume that each BS operates in the non-overlapping frequency band. In addition, as shown in Fig. 2, to achieve high spectral efficiency and flexible resource allocation [20], [21], [22] while reducing the deployment costs of radio frequency (RF) chains, we consider a MIMO-OFDM framework with partially-connected hybrid beamforming (HBF) structure, where each BS is equipped with R RF chains and L antennas. Specifically, each RF channel is assumed to be equipped with $L / R$ antennas, where $L / R$ is assumed to be an integer. Moreover, we assume that all the BSs perform the same parameter estimation algorithm before the data fusion is performed. Thus, for notational simplicity, we omit the subscript $j$ of the BSs temporarily. In order to facilitate the formulation of the parameter estimation problem via using tensor decomposition model in the following contents of this paper, we assume that all RF channels of each BS share only one data stream for sensing. In this way, the transmitted signal is given by

![](images/277e738e9afe253a8196d337edff76f1b02fe50f2497a1cda1998cf54de9162a.jpg)  
Fig. 1. Cooperative ISAC system.

$$
s \left( t \right) = \sum _ { m = 0 } ^ { M - 1 } \sum _ { n = 0 } ^ { N - 1 } s _ { m , n } \cdot e ^ { j 2 \pi m \Delta f t } \cdot r \left( t - n T _ { s } \right) ,\tag{1}
$$

where M and N denote the numbers of subcarriers and OFDM symbols, respectively. The notation $\Delta f$ denotes the subcarrier spacing (SCS), $T _ { s }$ denotes the OFDM symbol period (including the cyclic prefix), and r (t) denotes the transmit pulse shaping filter, respectively. The symbol $s _ { m , n }$ denotes the complex data allocated in the m-th subcarrier and the n-th OFDM symbol. Without loss of generality, we assume that $| s _ { m , n } | ^ { 2 } \ = \ 1 , \forall m , n .$ . Then, the transmitted frequency domain signal vector can be expressed as

$$
\begin{array} { r } { \mathbf { x } _ { m , n } = \mathbf { F } _ { T X } \mathbf { e } \cdot s _ { m , n } \in \mathbb { C } ^ { L \times 1 } , } \end{array}\tag{2}
$$

where $\mathbf { F } _ { T X } \triangleq \mathbf { F } _ { T X } ^ { A } \mathbf { F } _ { T X } ^ { D } , \mathbf { F } _ { T X } ^ { A } \in \mathbb { C } ^ { L \times R }$ and $\mathbf { F } _ { T X } ^ { D } \in \mathbb { C } ^ { R \times R }$ denote the transmit analog and digital precoding matrices, respectively. The non-zero elements of $\mathbf { F } _ { T X } ^ { A }$ are subjected to the constant module constraint. The symbol ${ \bf { \bar { e } } } = \left[ { 1 , \ldots , 1 } \right] ^ { T } \in$ $\mathbb { R } ^ { R \times 1 }$ denotes an all-one vector. The received frequency domain signal vector is given by

![](images/bae5f2010877b7d49d8c853c3d42a3ee6359bef26205feaad18938680f266c08.jpg)  
Fig. 2. Partially-connected HBF structure.

$$
\begin{array} { r } { { \bf { y } } _ { m , n } = { \bf { F } } _ { R X } ^ { H } { \bf { H } } _ { m , n } { \bf { x } } _ { m , n } + { \bf { F } } _ { R X } ^ { H } { \bf { n } } _ { m , n } \in \mathbb { C } ^ { R \times 1 } , } \end{array}\tag{3}
$$

where $\mathbf { F } _ { R X } \triangleq \mathbf { F } _ { R X } ^ { A } \mathbf { F } _ { R X } ^ { D } , \mathbf { F } _ { R X } ^ { A } \in \mathbb { C } ^ { L \times R }$ and $\mathbf { F } _ { R X } ^ { D } \in \mathbb { C } ^ { R \times R }$ denote the receive analog and digital combining matrices, respectively. The non-zero elements of $\mathbf { F } _ { R X } ^ { A }$ are also subjected to the constant module constraint. ${ \bf { H } } _ { m , n }$ is the discrete frequency domain sensing channel, which will be given in the following subsection. The notation ${ \mathbf { n } } _ { m , n }$ denotes the additive white Gaussian noise (AWGN). Then, we multiply the received signal vector by the conjugate of the transmitted data to eliminate its impacts, i.e.,

$$
\begin{array} { r } { \tilde { { \bf y } } _ { m , n } = s _ { m , n } ^ { * } { \bf y } _ { m , n } = { \bf F } _ { R X } ^ { H } { \bf H } _ { m , n } { \bf f } _ { T X } + \tilde { \bf n } _ { m , n } , } \end{array}\tag{4}
$$

where $\mathbf { f } _ { T X } \ \triangleq \ \mathbf { F } _ { T X } \mathbf { e } .$ , and $\tilde { \mathbf { n } } _ { m , n } \triangleq s _ { m , n } ^ { * } \mathbf { F } _ { R X } ^ { H } \mathbf { n } _ { m , n }$ is the equivalent noise.

## B. Sensing Channel Model

We assume that there are K UAVs in the cooperative ISAC system. In order to derive the positions and velocities of the UAVs in 3-D space, each BS is equipped with an uniform planar array (UPA) with P and Q antennas located in horizontal and vertical directions, respectively. Thus, the horizontal and vertical steering vectors can be respectively represented as

$$
\mathbf { a } _ { p } \left( \theta _ { k } , \phi _ { k } \right) = \left[ 1 , \ldots , e ^ { j 2 \pi ( P - 1 ) d \sin ( \theta _ { k } ) \cos ( \phi _ { k } ) / \lambda } \right] ^ { T } \in \mathbb { C } ^ { P \times 1 } ,\tag{5}
$$

$$
\mathbf { a } _ { q } \left( \theta _ { k } \right) = \left[ 1 , \ldots , e ^ { j 2 \pi \left( Q - 1 \right) d \cos \left( \theta _ { k } \right) / \lambda } \right] ^ { T } \in \mathbb { C } ^ { Q \times 1 } ,\tag{6}
$$

where d and λ denote the antenna spacing and the wavelength, respectively. The notations $\theta _ { k }$ and $\phi _ { k }$ denote the elevation and azimuth angles of the k-th UAV, respectively. For notational simplicity, we define the virtual angles as $\vartheta \triangleq \sin ( \theta ) \cos ( \phi )$ and $\psi \triangleq \cos ( \theta )$ . In this way, the steering vector of UPA can be rewritten in a compact form as

$$
\mathbf { a } \left( \vartheta _ { k } , \psi _ { k } \right) = \mathbf { a } _ { q } \left( \psi _ { k } \right) \otimes \mathbf { a } _ { p } \left( \vartheta _ { k } \right) \in \mathbb { C } ^ { P Q \times 1 } .\tag{7}
$$

For the considered low-altitude sensing scenario, we assume that there always exists the line-of-sight (LoS) paths between the BSs and the UAVs, while the echo signals reflected by other scatterers are very weak. In addition, we ignore the signals from other BSs (including those transmitted by other BSs and then reflected by the UAVs to the current BS). Because in the case of multi-BS frequency division configuration, the signals from other BSs can be effectively suppressed by each BS designing its own frequency band filter before receiving the echo signals. Thus, the time and delay domain sensing channel can be expressed as

$$
\mathbf { H } ( t , \tau ) = \sum _ { k = 1 } ^ { K } \alpha _ { k } \delta \left( \tau - \tau _ { k } \right) \mathbf { a } \left( \vartheta _ { k } , \psi _ { k } \right) \mathbf { a } \left( \vartheta _ { k } , \psi _ { k } \right) ^ { H } \cdot e ^ { j 2 \pi f _ { k } ^ { d } t } ,\tag{8}
$$

where $\alpha _ { k }$ denotes the channel coefficient, $\begin{array} { r } { \tau _ { k } \ = \ \frac { 2 d _ { k } } { c _ { 0 } } } \end{array}$ and $\begin{array} { r } { f _ { k } ^ { d } = \frac { 2 v _ { k } } { \lambda } } \end{array}$ are the echo delay and the Doppler frequency shift caused by the k-th UAV, respectively. The notation $c _ { 0 }$ denotes the speed of light. The notations $d _ { k }$ and $v _ { k }$ denote the range between the k-th UAV and the BS and its radial velocity to the BS, respectively. Then, by performing the Fourier transform (FT) of delay $\tau$ and sampling the received signal at the n-th OFDM symbol, the discrete frequency domain channel can be expressed as

$$
\begin{array} { l } { { \displaystyle { \bf H } _ { m , n } } } \\ { { \displaystyle \ = \sum _ { k = 1 } ^ { K } \alpha _ { k } { \bf a } \left( \vartheta _ { k } , \psi _ { k } \right) { \bf a } \left( \vartheta _ { k } , \psi _ { k } \right) ^ { H } \cdot e ^ { - j 2 \pi m \Delta f \tau _ { k } } \cdot e ^ { j 2 \pi f _ { k } ^ { d } n T _ { s } } } . } \end{array}\tag{9}
$$

## III. PRELIMINARY STEPS FOR THE COOPERATIVESENSING SCHEME

To enhance the practicality of the proposed cooperative sensing scheme, we present several preliminary steps to provide some prior information and guidelines for the subsequent sensing scheme.

## A. Beam Scanning and UAV Detection

It should be noted that in the scenario where the UAVs are close to the BSs (e.g., less than a hundred meters), the signal-to-noise ratio (SNR) of the echo signals is sufficient to meet the requirements of UAV detection and parameter estimation. In such cases, the precise localization of the UAVs can be achieved directly through several parameter estimation schemes without additional beam scanning or alignment procedures. However, by considering the scenario where the UAVs may be far from the BSs, the following beam scanning and alignment are required to counteract the severe path loss, thereby improving the SNR to facilitate the subsequent parameter estimation.

As shown in Fig. 3(a), we first determine the approximate locations of the UAVs via beam scanning. To further enhance the SNR of the received signals, we combine all the received symbols on each RF chain. In this way, the received signal can be expressed as

$$
\begin{array} { r } { \check { y } _ { m , n } = \mathbf { e } ^ { T } \tilde { \mathbf { y } } _ { m , n } = \mathbf { f } _ { R X } ^ { H } \mathbf { H } _ { m , n } \mathbf { f } _ { T X } + \check { n } _ { m , n } , } \end{array}\tag{10}
$$

where $\mathbf { f } _ { T X }$ and $\begin{array} { r l r } { \mathbf { f } _ { R X } } & { { } \triangleq } & { \mathbf { F } _ { R X } \mathbf { e } } \end{array}$ respectively represent the equivalent beamforming vector and combining vector,

$\mathbf { e } = \left[ 1 , \ldots , 1 \right] ^ { T } \in \mathbb { R } ^ { R \times 1 }$ denotes an all-one vector, and $\check { n } _ { m , n }$ denotes the equivalent noise. During the beam scanning period, we assume that

$$
\mathbf { f } _ { R X } \left( \theta _ { i } , \phi _ { j } \right) = \mathbf { f } _ { T X } \left( \theta _ { i } , \phi _ { j } \right) = \sqrt { \frac { P _ { T } } { P Q } } \mathbf { a } \left( \vartheta _ { i } , \psi _ { j } \right) ,\tag{11}
$$

where $P _ { T }$ denotes the transmit power of the BS, and

$$
\theta _ { i } = \theta _ { 0 } + i \Delta \theta , i = 0 , \ldots , N _ { \mathrm { H } } - 1 ,\tag{12a}
$$

$$
\phi _ { j } = \phi _ { 0 } + j \Delta \phi , \ j = 0 , \ldots , N _ { \mathrm { V } } - 1 ,\tag{12b}
$$

where $\theta _ { 0 }$ and $\phi _ { 0 }$ denote the initial scan angles, $\Delta \theta$ and $\Delta \phi$ denote the scan angle steps, i and $j$ denote the beam indices, $N _ { \mathrm { H } }$ and $N _ { \mathrm { V } }$ respectively denote the number of beams on horizontal and vertical directions, and the total number of scan beams is give by $N _ { \mathrm { H } } N _ { \mathrm { V } }$ . The equivalent beamforming and combining design in (11) can be simply achieved by setting the digital precoding/combining matrix to the identity matrix and filling the non-zero elements of the analog precod ing/combining matrix with the steering vector at $( \theta _ { i } , \phi _ { j } )$

To detect the presence of the UAVs within the beam range, we formulate the following binary hypothesis testing (BHT) problem as [23]

$$
\check { y } _ { m , n } = \left\{ \begin{array} { l l } { \mathcal { H } _ { 0 } : \check { n } _ { m , n } , } \\ { \mathcal { H } _ { 1 } : { \mathbf { f } _ { R X } ^ { H } } { \mathbf { H } _ { m , n } } { \mathbf { f } _ { T X } } + \check { n } _ { m , n } , } \end{array} \right.\tag{13}
$$

where the null hypothesis $( \mathcal { H } _ { 0 } )$ assumes that the BS receives only noise, whereas the alternative hypothesis $( \mathcal { H } _ { 1 } )$ suggests that the BS receives both the reflected echo signals and noise. To solve the above BHT problem, we first need to construct a detector $\tau \left( \cdot \right)$ to map $\tilde { y } _ { m , n }$ to a real number, and then compare it with a predefined threshold $\gamma$ to determine whether to accept $\mathcal { H } _ { 0 }$ or $\mathcal { H } _ { 1 }$ [23], i.e.,

$$
\mathcal { T } \left( \check { y } _ { m , n } \right) \bigotimes _ { \mathscr { H } _ { 0 } } ^ { \mathscr { H } _ { 1 } } \gamma .\tag{14}
$$

By considering the particular scenarios and available prior knowledge, various hypothesis testing methods such as likelihood ratio test (LRT) can be utilized to develop a detector [24]. For further manipulation, we introduce $\{ d _ { i , j } \} _ { i = 0 , i = 0 } ^ { { N _ { \mathrm { H } } } - 1 , { N _ { \mathrm { V } } } - 1 }$ as the detection flag. Specifically, if the UAVs are detected within the beam range with index (i, j), then $d _ { i , j } = 1 ;$ otherwise, $d _ { i , j } = 0$

## B. Estimation of the Number of UAVs

For the beam range where the presence of UAVs is detected $( \mathrm { i . e . , } d _ { i , j } = 1 )$ , it is necessary to further estimate the number of UAVs within the beam range, which can be achieved by considering the information-theoretic criteria [4]. Specifically, we first estimate the covariance of the received signal $\tilde { \mathbf { y } } _ { m , n }$ as

$$
\hat { \mathbf { R } } = \frac { 1 } { M N } \sum _ { m = 0 } ^ { M - 1 } \sum _ { n = 0 } ^ { N - 1 } \tilde { \mathbf { y } } _ { m , n } \tilde { \mathbf { y } } _ { m , n } ^ { H } \in \mathbb { C } ^ { R \times R } .\tag{15}
$$

Then, we perform the singular value decomposition (SVD) of R<sup>ˆ</sup> , i.e., $\hat { \textbf { R } } = \mathbf { U } \pmb { \Lambda } \mathbf { U } ^ { H }$ , where $\boldsymbol { \Lambda } = \mathrm { D } ( [ \lambda _ { 1 } , \dots , \lambda _ { R } ] )$ is a diagonal matrix with the eigenvalues sorted in descending

order, i.e., $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \cdot \cdot \cdot \geq \lambda _ { R } .$ Subsequently, by adopting the minimum description length (MDL) criterion [25], the number of UAVs within the beam range is estimated as<sup>1</sup>

$$
K _ { i , j } = \underset { k \in \{ 1 , \ldots , R - 1 \} } { \arg \operatorname* { m i n } } \ \mathrm { M D L } ( k ) ,\tag{16}
$$

with

$$
\begin{array} { r } { \mathrm { M D L } ( k ) = - \ln \left( \frac { \prod _ { i = k + 1 } ^ { R } \lambda _ { i } ^ { 1 / ( R - k ) } } { \frac { 1 } { R - k } \sum _ { i = k + 1 } ^ { R } \lambda _ { i } } \right) ^ { ( R - k ) M N } } \\ { + \frac { 1 } { 2 } k ( 2 R - k ) \ln \left( M N \right) . } \end{array}\tag{17}
$$

## C. Beam Alignment

After the aforementioned steps, the approximate locations of the UAVs in 3-D space can be determined by recording the indices of the elements that are equal to 1 in $\{ d _ { i , j } \} _ { i = 0 , j = 0 } ^ { N _ { \mathrm { H } } - 1 , N _ { \mathrm { V } } - 1 }$ and the total number of the UAVs can be derived by summing up the estimated number of the UAVs in each beam range as

$$
{ \cal K } = \sum _ { i = 0 , j = 0 } ^ { N _ { \mathrm { H } } - 1 , N _ { \mathrm { V } } - 1 } d _ { i , j } K _ { i , j } ,\tag{18}
$$

which provide valuable prior information and guidelines for the subsequent monostatic parameter estimation. Specifically, as illustrated in Fig. 3(b), we can divide the entire antenna array into $\begin{array} { r } { N ^ { \prime } = \sum _ { i = 0 , j = 0 } ^ { N _ { \mathrm { H } } - 1 , N _ { \mathrm { V } } - 1 } d _ { i , j } } \end{array}$ groups with each group formulating the beam aligned with the directions of $( \theta _ { i } , \phi _ { j } )$ For instance, we can assume that the digital precoding matrix is the identity matrix, while the non-zero elements of the analog precoding matrix are filled with the normalized steering vectors corresponding to the directions of $( \theta _ { i } , \phi _ { j } )$ . However, the non-zero elements of the combining matrix are chosen uniformly from a normalized unit circle to mitigate the AoA estimation ambiguity caused by the dimensional reduction in the HBF structure. Noting that the aforementioned beam-related steps have been widely studied and are not the focus of this paper, in the following part of this paper, we assume that the required prior information, i.e., the beam detection flag $\{ d _ { i , j } \} _ { i = 1 , j = 1 } ^ { N _ { \mathrm { H } } , N _ { \mathrm { V } } }$ and the total number of the UAVs K, have been accurately derived via the aforementioned steps.

## IV. TENSOR DECOMPOSITION APPROACH FORPARAMETER ESTIMATION

In this section, we begin by providing several preliminaries of tensor. Then, we formulate the parameter estimation problem via using a tensor decomposition model. Subsequently, a parameter estimation scheme based on spatial smoothing tensor decomposition is developed. Finally, we discuss the uniqueness and complexity of the tensor decomposition steps.

![](images/6c7ce210cd053a6d4fe2ad9fc34d3abfc77fc50b5ab0d89a2ca4c1f21a2270bc.jpg)  
(a) Beam scanning.  
(b) Beam alignment.  
Fig. 3. An illustration of the beam scanning and alignment.

## A. Tensor Preliminaries

To enhance the readability of this paper, some basic theories and key definitions about tensors are provided. We recommend that the readers refer to [26] for more details.

1) Unfolding: Mode-n unfolding of a tensor $\pmb { \mathcal { X } } \in$ $\mathbb { C } ^ { I _ { 1 } \times I _ { 2 } \times \dots \times I _ { N } }$ denotes that one rearranges the tensor to a matrix. Specifically, tensor element $( i _ { 1 } , i _ { 2 } , \dots , i _ { N } )$ maps to matrix element $( i _ { n } , j )$ , where

$$
j = 1 + \sum _ { \stackrel { k = 1 } { k \neq n } } ^ { N } \left( i _ { k } - 1 \right) J _ { k } , \mathrm { w i t h } J _ { k } = \prod _ { \stackrel { m = 1 } { m \neq n } } ^ { k - 1 } I _ { m } .\tag{19}
$$

2) Rank-1 Tensor: An N-th-order tensor X is a rank-1 tensor if it can be expressed as the outer product of N vectors, i.e.,

$$
\pmb { \chi } = \mathbf { a } ^ { ( 1 ) } \circ \mathbf { a } ^ { ( 2 ) } \circ \cdots \circ \mathbf { a } ^ { ( N ) } .\tag{20}
$$

3) CP Decomposition: CANDECOMP/PARAFAC (CP) decomposition denotes that one decomposes a tensor into a sum of component rank-1 tensors, i.e.,

$$
\pmb { \chi } = \sum _ { r = 1 } ^ { R } \lambda _ { r } \mathbf { a } _ { r } ^ { ( 1 ) } \circ \mathbf { a } _ { r } ^ { ( 2 ) } \circ \cdot \cdot \cdot \circ \mathbf { a } _ { r } ^ { ( N ) } ,\tag{21}
$$

where R denotes the rank of X . The corresponding factor matrix to the n-th mode is defined as $\begin{array} { r l } { \mathbf { A } ^ { ( n ) } } & { { } = } \end{array}$ $\left\lceil \mathbf { a } _ { 1 } ^ { ( n ) } , \dots , \mathbf { a } _ { R } ^ { ( n ) } \ \right\rceil , n = 1 , \dots , N$ . The mode-n unfolding version of X is given by

$$
\begin{array} { r l } & { \mathbf { X } _ { ( n ) } } \\ & { = \mathbf { A } ^ { ( n ) } \mathbf { A } \left( \mathbf { A } ^ { ( N ) } \odot \cdots \odot \mathbf { A } ^ { ( n + 1 ) } \odot \mathbf { A } ^ { ( n - 1 ) } \odot \cdots \odot \mathbf { A } ^ { ( 1 ) } \right) ^ { T } , } \end{array}\tag{22}
$$

where $\pmb { \Lambda } = \mathbf { D } \left( [ \lambda _ { 1 } , \ldots , \lambda _ { R } ] \right)$

## B. Tensor Formulation

Recalling the expression of the received signal and the channel model provided in Section II, we find that the AoAs, Doppler shifts, and time delays caused by the UAVs independently affect the received signal in spatial, time and frequency dimensions, which prompts us to formulate the multi-dimensional parameter estimation via using a tensor decomposition model. Specifically, by substituting (9) into (4) and stacking the received signal among N OFDM symbols and M subcarriers, it is readily verified that the received signal vector $\tilde { \mathbf { y } } _ { m , n }$ can be formulated into a third-order tensor as

$$
\mathcal { \pmb { y } } = \sum _ { k = 1 } ^ { K } \alpha _ { k } \mathbf { b } \left( \vartheta _ { k } , \psi _ { k } \right) \circ \mathbf { o } \left( f _ { k } ^ { d } \right) \circ \mathbf { g } \left( \tau _ { k } \right) + \pmb { \mathscr { N } } \in \mathbb { C } ^ { R \times N \times M } ,\tag{23}
$$

where $\pmb { \mathcal { N } } \in \mathbb { C } ^ { R \times N \times M }$ is the equivalent noise tensor, K denotes the total number of the UAVs, which can be derived by the preliminary steps provided in Section III, and

$$
\begin{array} { r } { \mathbf { b } \left( \boldsymbol { \vartheta } _ { k } , \boldsymbol { \psi } _ { k } \right) = \mathbf { F } _ { R X } ^ { H } \mathbf { a } \left( \boldsymbol { \vartheta } _ { k } , \boldsymbol { \psi } _ { k } \right) \mathbf { a } \left( \boldsymbol { \vartheta } _ { k } , \boldsymbol { \psi } _ { k } \right) ^ { H } \mathbf { f } _ { T X } \in \mathbb { C } ^ { R \times 1 } , } \end{array}\tag{24}
$$

$$
\mathbf { o } \left( f _ { k } ^ { d } \right) = \left[ 1 , e ^ { j 2 \pi T _ { s } f _ { k } ^ { d } } , \ldots , e ^ { j 2 \pi ( N - 1 ) T _ { s } f _ { k } ^ { d } } \right] ^ { T } \in { \mathbb { C } } ^ { N \times 1 } ,\tag{25}
$$

$$
\mathbf { g } \left( \tau _ { k } \right) = \left[ 1 , e ^ { - j 2 \pi \Delta f \tau _ { k } } , \ldots , e ^ { - j 2 \pi \left( M - 1 \right) \Delta f \tau _ { k } } \right] ^ { T } \in \mathbb { C } ^ { M \times 1 } ,\tag{26}
$$

respectively. The corresponding factor matrices of Y are given by

$$
\mathbf { A } ^ { ( 1 ) } = [ \mathbf { b } ( \vartheta _ { 1 } , \psi _ { 1 } ) , \ldots , \mathbf { b } ( \vartheta _ { K } , \psi _ { K } ) ] \in { \mathbb { C } } ^ { R \times K } ,\tag{27}
$$

$$
\mathbf { A } ^ { ( 2 ) } = \left[ \mathbf { o } ( f _ { 1 } ^ { d } ) , \ldots , \mathbf { o } ( f _ { K } ^ { d } ) \right] \in \mathbb { C } ^ { N \times K } ,\tag{28}
$$

$$
\mathbf { A } ^ { ( 3 ) } = [ \alpha _ { 1 } \mathbf { g } ( \tau _ { 1 } ) , \ldots , \alpha _ { K } \mathbf { g } ( \tau _ { K } ) ] \in \mathbb { C } ^ { M \times K } .\tag{29}
$$

Then, the tensor decomposition model is given by

$$
\operatorname* { m i n } _ { \mathbf { A } ^ { ( 1 ) } , \mathbf { A } ^ { ( 2 ) } , \mathbf { A } ^ { ( 3 ) } } \left\| \pmb { \mathcal { V } } - \sum _ { k = 1 } ^ { K } \alpha _ { k } \mathbf { b } \left( \vartheta _ { k } , \psi _ { k } \right) \circ \mathbf { o } \left( f _ { k } ^ { d } \right) \circ \mathbf { g } \left( \tau _ { k } \right) \right\| _ { F } ^ { 2 } .\tag{30}
$$

## C. Factor Matrices Recovery

Instead of solving Problem (30) via the well-known alternative least square (ALS) method [16], we recover the factor matrices by leveraging the Vandermonde structure of $\mathbf { A } ^ { ( 3 ) }$ For notational simplicity, the noise component is ignored in the following derivations. First, the mode-1 unfolding of the third-order tensor Y can be expressed as [26]

$$
\mathbf { Y } _ { ( 1 ) } ^ { T } = \left( \mathbf { A } ^ { ( 3 ) } \odot \mathbf { A } ^ { ( 2 ) } \right) \left( \mathbf { A } ^ { ( 1 ) } \right) ^ { T } \in \mathbb { C } ^ { M N \times R } .\tag{31}
$$

Then, we choose a pair of integer $\{ L _ { 1 } , L _ { 2 } \}$ satisfying $L _ { 1 } +$ $L _ { 2 } = M + 1$ and define the following cyclic choose matrix as

$$
\mathbf { J } _ { l } = \left[ \mathbf { 0 } _ { L _ { 1 } \times ( l - 1 ) } , \mathbf { I } _ { L _ { 1 } } , \mathbf { 0 } _ { L _ { 1 } \times ( L _ { 2 } - l ) } \right] \in \mathbb { C } ^ { L _ { 1 } \times M } .\tag{32}
$$

We then smooth the mode-1 unfolding of $_ { \mathscr { y } }$ as

$$
\begin{array} { r l } & { \mathbf { Y } ^ { S } = \left[ \left( \mathbf { J } _ { 1 } \otimes \mathbf { I } _ { N } \right) \mathbf { Y } _ { ( 1 ) } ^ { T } , \ldots , \left( \mathbf { J } _ { L _ { 2 } } \otimes \mathbf { I } _ { N } \right) \mathbf { Y } _ { ( 1 ) } ^ { T } \right] } \\ & { \quad \quad \stackrel { ( a ) } { = } \left( \mathbf { A } ^ { ( L _ { 1 } , 3 ) } \odot \mathbf { A } ^ { ( 2 ) } \right) \left( \mathbf { A } ^ { ( L _ { 2 } , 3 ) } \odot \mathbf { A } ^ { ( 1 ) } \right) ^ { T } \in \mathbb { C } ^ { L _ { 1 } N \times L _ { 2 } R } , } \end{array}\tag{33}
$$

where $\mathbf { A } ^ { ( L , 3 ) }$ denotes the 1 to L rows of $\mathbf { A } ^ { ( 3 ) }$ . Equation (a) is derived by leveraging the property of Khatri-Rao product, i.e., $\left( \mathbf { A } \otimes \mathbf { B } \right) \left( \mathbf { C } \odot \mathbf { D } \right) = \left( \mathbf { A } \mathbf { C } \right) \odot \left( \mathbf { B } \mathbf { D } \right)$ [27] and the Vandermonde structure of $\mathbf { A } ^ { ( 3 ) }$ , while the details are omitted due to the space limitations. We then perform the truncated SVD of $\mathbf { Y } _ { S }$ as

$$
\mathbf { Y } ^ { S } = \mathbf { U } \boldsymbol { \Sigma } \mathbf { V } ^ { H } ,\tag{34}
$$

where $\mathbf { U } \in \mathbb { C } ^ { L _ { 1 } N \times K } , \Sigma \in \mathbb { C } ^ { K \times K }$ and $\mathbf { V } \in \mathbb { C } ^ { L _ { 2 } R \times K }$ . Given that the columns of U span the same subspace as the columns of $\mathbf { Y } ^ { S }$ , there always exists a full rank matrix $\mathbf { M } \in \mathbb { C } ^ { K \times K }$ satisfying [28]

$$
\mathbf { A } ^ { ( L _ { 1 } , 3 ) } \odot \mathbf { A } ^ { ( 2 ) } = \mathbf { U } \mathbf { M } \in \mathbb { C } ^ { L _ { 1 } N \times K } ,\tag{35}
$$

$$
\mathbf { A } ^ { ( L _ { 2 } , 3 ) } \odot \mathbf { A } ^ { ( 1 ) } = \mathbf { V } ^ { * } \Sigma \mathbf { M } ^ { - T } \in \mathbb { C } ^ { L _ { 2 } R \times K } .\tag{36}
$$

Noting the Vandermonde structure of $\mathbf { A } ^ { ( L _ { 1 } , 3 ) }$ , we have

$$
\left( \underline { { \mathbf { A } } } ^ { ( L _ { 1 } , 3 ) } \odot \mathbf { A } ^ { ( 2 ) } \right) \mathbf { Z } = \overline { { \mathbf { A } } } ^ { ( L _ { 1 } , 3 ) } \odot \mathbf { A } ^ { ( 2 ) } ,\tag{37}
$$

where $\textbf { Z } = \mathrm { ~ D ~ } { \big ( } [ e ^ { - j 2 \pi \Delta f \tau _ { 1 } } , \dots , e ^ { - j 2 \pi \Delta f \tau _ { K } } ] { \big ) } , ~ \underline { { \mathbf { A } } } ^ { ( L _ { 1 } , 3 ) }$ and $\overline { { \mathbf { A } } } ^ { ( L _ { 1 } , 3 ) }$ denote the deletions of the last row and the first row of $\mathbf { A } ^ { ( L _ { 1 } , 3 ) }$ , respectively. Then, one obtains

$$
\underline { { \mathbf { A } } } ^ { ( L _ { 1 } , 3 ) } \odot \mathbf { A } ^ { ( 2 ) } = \mathbf { U } _ { 1 } \mathbf { M } ,\tag{38}
$$

$$
\overline { { \mathbf { A } } } ^ { ( L _ { 1 } , 3 ) } \odot \mathbf { A } ^ { ( 2 ) } = \mathbf { U } _ { 2 } \mathbf { M } ,\tag{39}
$$

where $\mathbf { U } _ { 1 } = \mathbf { U } _ { 1 : ( L _ { 1 } - 1 ) N } ,$ denotes the 1 to $\left( L _ { 1 } - 1 \right) N$ rows of U, and ${ \bf U } _ { 2 } = { \bf U } _ { N + 1 : L _ { 1 } } { \bf \Sigma } _ { N } ,$ <sub>:</sub> denotes the $N + 1$ to $L _ { 1 } N$ rows of U, respectively. Then, combining (38), (39) with (37), we have

$$
{ \bf U } _ { 1 } { \bf M } { \bf Z } = { \bf U } _ { 2 } { \bf M } \Rightarrow { \bf M } { \bf Z } { \bf M } ^ { - 1 } = { \bf U } _ { 1 } ^ { \dagger } { \bf U } _ { 2 } \triangleq \Xi .\tag{40}
$$

Thus, by performing the eigenvalue decomposition (EVD) of $\Xi ,$ we can derive the estimations of Z and M. Since the normalized diagonal elements of Z, i.e., $\begin{array} { r l } { \hat { z } _ { k } } & { { } = } \end{array}$ $[ \mathbf { Z } ] _ { k , k } / | \left[ \mathbf { Z } \right] _ { k , k } | , k = 1 , \ldots , K$ are actually the generators of $\mathbf { A } ^ { ( 3 ) }$ , each column of $\mathbf { A } ^ { ( 3 ) }$ can be recovered as

$$
\hat { \mathbf { a } } _ { k } ^ { ( 3 ) } = \left[ 1 , \hat { z } _ { k } , \ldots , \hat { z } _ { k } ^ { M - 1 } \right] ^ { T } , k = 1 , \ldots , K .\tag{41}
$$

Then, recalling the definition of the Khatri-Rao product, we have

$$
\mathbf { A } ^ { ( L _ { 1 } , 3 ) } \odot \mathbf { A } ^ { ( 2 ) } = \left[ \mathbf { a } _ { 1 } ^ { ( L _ { 1 } , 3 ) } \otimes \mathbf { a } _ { 1 } ^ { ( 2 ) } , . . . , \mathbf { a } _ { K } ^ { ( L _ { 1 } , 3 ) } \otimes \mathbf { a } _ { K } ^ { ( 2 ) } \right] = \mathbf { U } \mathbf { M } .\tag{42}
$$

Thus, given $\hat { \bf A } ^ { ( L _ { 1 } , 3 ) }$ and M, each column of $\mathbf { A } ^ { ( 2 ) }$ can be derived as [28]

$$
\begin{array} { r l } & { \mathbf { a } _ { k } ^ { ( 2 ) } \overset { ( a ) } { = } \left( \frac { \mathbf { a } _ { k } ^ { ( L _ { 1 } , 3 ) ^ { H } } } { \left\| \mathbf { a } _ { k } ^ { ( L _ { 1 } , 3 ) } \right\| _ { 2 } ^ { 2 } } \otimes \mathbf { I } _ { N } \right) \left( \mathbf { a } _ { k } ^ { ( L _ { 1 } , 3 ) } \otimes \mathbf { a } _ { k } ^ { ( 2 ) } \right) } \\ & { \overset { ( b ) } { = } \left( \frac { \mathbf { a } _ { k } ^ { ( L _ { 1 } , 3 ) ^ { H } } } { \left\| \mathbf { a } _ { k } ^ { ( L _ { 1 } , 3 ) } \right\| _ { 2 } ^ { 2 } } \otimes \mathbf { I } _ { N } \right) \mathbf { U m } _ { k } , k = 1 , \dots , K , } \end{array}\tag{43}
$$

where (a) is obtained by using the mixed-product property of the Kronecker product, i.e., $( \mathbf { A } \otimes \mathbf { B } ) ( \mathbf { C } \otimes \mathbf { D } ) = \mathbf { A } \mathbf { C } \otimes \mathbf { B } \mathbf { D }$ (b) is based on (42), and $\mathbf { m } _ { k }$ denotes the k-th column of M.

Similarly, letting $\mathbf { P } \triangleq \mathbf { M } ^ { - T }$ , we can recover each column of $\mathbf { A } ^ { ( 1 ) }$ as [28]

$$
\begin{array} { r l } & { { \mathbf { a } } _ { k } ^ { \left( 1 \right) } \overset { \left( a \right) } { = } \left( \frac { { \mathbf { a } } _ { k } ^ { \left( L _ { 2 } , 3 \right) ^ { H } } } { \left\| { \mathbf { a } } _ { k } ^ { \left( L _ { 2 } , 3 \right) } \right\| _ { 2 } ^ { 2 } } \otimes { \mathbf { I } } _ { R } \right) \left( { \mathbf { a } } _ { k } ^ { \left( L _ { 2 } , 3 \right) } \otimes { \mathbf { a } } _ { k } ^ { \left( 1 \right) } \right) } \\ & { \overset { \left( b \right) } { = } \left( \frac { { \mathbf { a } } _ { k } ^ { \left( L _ { 2 } , 3 \right) ^ { H } } } { \left\| { \mathbf { a } } _ { k } ^ { \left( L _ { 2 } , 3 \right) } \right\| _ { 2 } ^ { 2 } } \otimes { \mathbf { I } } _ { R } \right) { \mathbf { V } } ^ { * } { \Sigma } { \mathbf { p } } _ { k } , k = 1 , \dots , K , } \end{array}\tag{44}
$$

where $\mathbf { p } _ { k }$ denotes the k-th column of P.

## D. Parameter Estimation

In this subsection, we estimate the parameters from the recovered factor matrices. First, the estimation of the time delay $\{ \tau _ { k } \} _ { k = 1 } ^ { K }$ can be derived from the generators of $\mathbf { A } ^ { ( 3 ) }$ i.e.,

$$
\hat { \tau } _ { k } = \frac { \mathcal { L } \hat { z } _ { k } } { - 2 \pi \Delta f } ,\tag{45}
$$

where $\measuredangle \hat { z } _ { k }$ denotes the angle of $\hat { z } _ { k }$ . The estimation of the range $\{ d _ { k } \} _ { k = 1 } ^ { K }$ between the UAVs and the BS can be derived as

$$
\hat { d } _ { k } = \frac { \hat { \tau } _ { k } c _ { 0 } } { 2 } .\tag{46}
$$

The estimation of the Doppler frequency shift $\{ f _ { k } ^ { d } \} _ { k = 1 } ^ { K }$ can be derived by the following correlation-based scheme as [16]

$$
\hat { f } _ { k } ^ { d } = \arg \operatorname* { m a x } _ { f _ { k } ^ { d } } \left| \hat { \mathbf { o } } _ { k } ^ { H } \mathbf { o } \left( f _ { k } ^ { d } \right) \right| ^ { 2 } ,\tag{47}
$$

where $\hat { \mathbf { o } } _ { k }$ denotes the k-th column of $\hat { \mathbf { A } } ^ { ( 2 ) }$ . The radial velocity $\{ v _ { k } \} _ { k = 1 } ^ { K }$ of the UAVs to the BS can be estimated as

$$
\hat { v } _ { k } = \frac { \hat { f } _ { k } ^ { d } \lambda } { 2 } .\tag{48}
$$

Similarly, the estimation of $\{ \vartheta _ { k } , \psi _ { k } \} _ { k = 1 } ^ { K }$ can be derived as

$$
\{ \hat { \vartheta } _ { k } , \hat { \psi } _ { k } \} = \arg \operatorname* { m a x } _ { \vartheta , \psi } \frac { \left| \hat { \mathbf { b } } _ { k } ^ { H } \mathbf { b } ( \vartheta , \psi ) \right| ^ { 2 } } { \left\| \mathbf { b } ( \vartheta , \psi ) \right\| _ { 2 } ^ { 2 } } ,\tag{49}
$$

where $\hat { \mathbf { b } } _ { k }$ denotes the k-th column of $\hat { \mathbf { A } } ^ { ( 1 ) }$ . Noting that Problem (47) can be directly solved by the one-dimensional (1- D) search method. However, performing the two-dimensional (2-D) search method in (49) will result in a heavy computational burden. Thus, we develop a low-complexity AoA estimation algorithm based on GRQ to address Problem (49). Specifically, the objective function (OF) of Problem (49) can be rewritten in (50), shown at the bottom of the page, where equation (a) is derived by eliminating the common factor a $\left( \vartheta , \psi \right) ^ { H } \mathbf { f } _ { T X } \mathbf { f } _ { T X } ^ { H } \mathbf { a } \left( \vartheta , \psi \right)$ from both the numerator and denominator. Equation (b) comes from the reformulation of ${ \bf { a } } \left( { \vartheta , \psi } \right)$ . In specific, we have

$$
\begin{array} { r l } & { \mathbf { a } \left( \theta , \psi \right) = \left( \mathbf { a } _ { q } \left( \psi \right) \cdot 1 \right) \otimes \left( \mathbf { I } _ { p } \mathbf { a } _ { p } \left( \theta \right) \right) } \\ & { \quad \quad = \left( \mathbf { a } _ { q } \left( \psi \right) \otimes \mathbf { I } _ { p } \right) \mathbf { a } _ { p } \left( \theta \right) , } \end{array}\tag{51}
$$

which can be derived by leveraging the mixed-product property of the Kronecker product, i.e., $\left( \mathbf { A } \otimes \mathbf { B } \right) \left( \mathbf { C } \otimes \mathbf { D } \right) \ =$ AC ⊗ BD. Equation (c) is obtained by defining

$$
\mathbf { Q } _ { 1 } ^ { k } ( \psi ) \triangleq \left[ \mathbf { a } _ { q } ( \psi ) \otimes \mathbf { I } _ { P } \right] ^ { H } \mathbf { F } _ { R X } \hat { \mathbf { b } } _ { k } \hat { \mathbf { b } } _ { k } ^ { H } \mathbf { F } _ { R X } ^ { H } \left[ \mathbf { a } _ { q } ( \psi ) \otimes \mathbf { I } _ { P } \right] ,\tag{52a}
$$

$$
{ \bf Q } _ { 2 } ^ { k } \left( \psi \right) \triangleq \left[ { \bf a } _ { q } ( \psi ) \otimes { \bf I } _ { P } \right] ^ { H } { \bf F } _ { R X } { \bf F } _ { R X } ^ { H } \left[ { \bf a } _ { q } ( \psi ) \otimes { \bf I } _ { P } \right] ,\tag{52b}
$$

respectively. Then, Problem (49) can be reformulated as

$$
\begin{array} { r l } { \operatorname* { m a x } } & { { } \frac { { \mathbf { a } } _ { p } ( \vartheta ) ^ { H } { \mathbf { Q } } _ { 1 } ^ { k } ( \psi ) { \mathbf { a } } _ { p } ( \vartheta ) } { { \mathbf { a } } _ { p } ( \vartheta ) ^ { H } { \mathbf { Q } } _ { 2 } ^ { k } ( \psi ) { \mathbf { a } } _ { p } ( \vartheta ) } . } \end{array}\tag{53}
$$

Noting that with fixed ψ, Problem (53) has a well-known GRQ form [27]. It is readily verified that $\mathbf { a } _ { p } ( \vartheta )$ is an eigenvector of the matrix $\Phi ^ { k } \left( \psi \right) \triangleq \left( \mathbf { Q } _ { 2 } ^ { k } ( \psi ) \right) ^ { \dagger } \mathbf { Q } _ { 1 } ^ { k } ( \psi )$ , and the OF value of Problem (53) is the corresponding eigenvalue of $\Phi ^ { k } \left( \psi \right)$ Consequently, we estimate ψ<sub>k</sub> as

$$
\hat { \psi } _ { k } = \arg \operatorname* { m a x } _ { \psi } \lambda _ { \operatorname* { m a x } } \{ \Phi ^ { k } \left( \psi \right) \} ,\tag{54}
$$

where $\lambda _ { \operatorname* { m a x } } \{ \cdot \}$ denotes the maximum eigenvalue of a matrix, and the above problem can be solved by the 1-D search method. At the first glance, performing the EVD of $\Phi ^ { k } \left( \psi \right)$ to obtain the maximum eigenvalue of $\bar { \Phi ^ { k } } \left( \psi \right)$ on several grids will still incur considerable calculation burden. However, the following lemma proves that the EVD of $\Phi ^ { k } \left( \psi \right)$ on each grid is unnecessary.

Lemma 1: Problem (54) is equivalent to the following problem:

$$
\hat { \psi } _ { k } = \arg \operatorname* { m a x } _ { \psi } \mathrm { ~ T r ~ } \big ( \Phi ^ { k } \left( \psi \right) \big ) .\tag{55}
$$

Proof: According to the expression of (52a), it is readily verified that the rank of $\mathbf { Q } _ { 1 } ^ { k } \left( \psi \right)$ is 1. Then, based on the property of the rank of matrix multiplication [27], i.e.,

$$
\operatorname { r a n k } \left( \mathbf { A } \mathbf { B } \right) \leq \operatorname* { m i n } \left\{ \operatorname { r a n k } \left( \mathbf { A } \right) , \operatorname { r a n k } \left( \mathbf { B } \right) \right\} ,\tag{56}
$$

we can prove that the rank of $\Phi ^ { k } \left( \psi \right)$ is always 1. In addition, according to the property of rank-1 matrix [27], we have

$$
\mathrm { T r } \left( \Phi ^ { k } \left( \psi \right) \right) = \lambda ,\tag{57}
$$

where λ denotes the unique non-zero eigenvalue of $\Phi ^ { k } \left( \psi \right)$ Additionally, it is readily verified that $\bar { \Phi } ^ { k } \left( \psi \right)$ is a positive semi-definite matrix, thus, we have Tr $\left( \Phi ^ { k } \left( \psi \right) \right) ~ = ~ \lambda ~ =$ $\lambda _ { \mathrm { m a x } } \left\{ \Phi ^ { k } \left( \psi \right) \right\}$ and the proof is completed. ■

$$
\begin{array} { r l } & { \boldsymbol { f } \left( \vartheta , \psi \right) = \frac { \hat { \mathbf { b } } _ { k } ^ { H } \mathbf { F } _ { R X } ^ { H } \mathbf { a } \left( \vartheta , \psi \right) \mathbf { a } \left( \vartheta , \psi \right) ^ { H } \mathbf { f } _ { T X } \mathbf { f } _ { X X } ^ { H } \mathbf { a } \left( \vartheta , \psi \right) \mathbf { a } \left( \vartheta , \psi \right) ^ { H } \mathbf { F } _ { R X } \hat { \mathbf { b } } _ { k } } { \mathbf { f } _ { T X } ^ { H } \mathbf { a } \left( \vartheta , \psi \right) \mathbf { a } \left( \vartheta \right) ^ { H } \mathbf { f } _ { T X } \mathbf { a } \left( \vartheta , \psi \right) ^ { H } \mathbf { f } _ { R X } \hat { \mathbf { b } } _ { k } } \frac { \left( \mathbf { a } \right) } { \left( \mathbf { b } \right) ^ { H } \mathbf { f } _ { R X } \hat { \mathbf { b } } _ { k } \hat { \mathbf { b } } _ { k } ^ { H } \mathbf { F } _ { R X } ^ { H } \mathbf { a } \left( \vartheta , \psi \right) } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \mathbf { f } _ { T X } ^ { H } \mathbf { a } \left( \vartheta , \psi \right) \mathbf { a } \left( \vartheta , \psi \right) ^ { H } \mathbf { F } _ { R X } \mathbf { F } _ { R X } ^ { H } \mathbf { a } \left( \vartheta , \psi \right) \mathbf { a } \left( \vartheta , \psi \right) ^ { H } \mathbf { f } _ { T X } \mathbf { b } _ { k } \left( \mathbf { a } \right) } \\ &  \quad \quad \quad \quad \stackrel { ( b ) } { = } \frac  \mathbf { a } _ { p } \left( \vartheta \right) ^ { H } \left[ \mathbf { a } _ { q } \left( \psi \right) \otimes \mathbf { I } _ { P } \right] ^ { H } \mathbf { F } _ { R X } \hat { \mathbf { b } } _ { k } ^ { H } \mathbf { F } _ { R X } ^ { H } \left[ \mathbf { a } _ { q } \left( \psi \right) \otimes \mathbf { I } _ { P } \right] \mathbf { a } _ { p } \ \end{array}\tag{50}
$$

Algorithm 1 GRQ-Based Method to Solve Problem (49)   
1: Estimate $\psi _ { k }$ in (55) by the 1-D search method;   
2: Calculate the maximum eigenvalue of $\Phi ^ { k } ( \hat { \psi } _ { k } )$ and the   
corresponding eigenvector $\hat { \mathbf { a } } _ { p } ( \vartheta )$   
3: Calculate $\hat { \mathbf { a } } _ { p } ( \vartheta ) \gets \hat { \mathbf { a } } _ { p } ( \vartheta ) / [ \hat { \hat { \mathbf { a } } } _ { p } ( \vartheta ) ] _ { 1 }$ to eliminate the scal  
ing ambiguity;   
4: Estimate $\vartheta _ { k }$ in (58) by the 1-D search method.

According to Lemma 1, we address Problem (55) to estimate $\psi _ { k }$ by the 1-D search method. Subsequently, the estimation of ${ \bf a } _ { p } \left( \vartheta \right)$ is given by the eigenvector corresponding to the maximum eigenvalue of $\Phi ^ { k } ( { \hat { \psi } } _ { k } )$ . We let $\hat { \mathbf { a } } _ { p } ( \vartheta ) \gets$ $\hat { \mathbf { a } } _ { p } ( \vartheta ) / [ \hat { \mathbf { a } } _ { p } ( \vartheta ) ] _ { 1 }$ <sub>1</sub> to eliminate the scaling ambiguity brought by the EVD, where $[ \cdot ] _ { 1 }$ denotes the first element of a vector. Then, we estimate $\vartheta _ { k }$ as

$$
\hat { \vartheta } _ { k } = \arg \operatorname* { m i n } _ { \vartheta } \ \left\| \mathbf { a } _ { p } \left( \vartheta \right) - \hat { \mathbf { a } } _ { p } \left( \vartheta \right) \right\| _ { 2 } ,\tag{58}
$$

which can still be solved by the 1-D search method. The detailed procedures of the proposed GRQ-based algorithm are summarized in Algorithm 1. Then, the estimations of the elevation and azimuth angles can be derived as

$$
\begin{array} { r } { \hat { \theta } _ { k } = \operatorname { a r c } \cos ( \hat { \psi } _ { k } ) , } \end{array}\tag{59}
$$

$$
\hat { \phi } _ { k } = \operatorname { a r c } \cos \left( \frac { \hat { \vartheta } _ { k } } { \sin ( \hat { \theta } _ { k } ) } \right) .\tag{60}
$$

Finally, we eliminate the scaling ambiguity and estimate the channel coefficients as [17]

$$
[ \Lambda _ { 1 } ] _ { k , k } = \mathbf { b } ^ { \dagger } \left( \hat { \vartheta } _ { k } , \hat { \psi } _ { k } \right) \hat { \mathbf { b } } _ { k } ,\tag{61a}
$$

$$
[ \Lambda _ { 2 } ] _ { k , k } = \mathbf { o } ^ { \dag } \left( \hat { f } _ { k } ^ { d } \right) \hat { \mathbf { o } } _ { k } ,\tag{61b}
$$

$$
\pmb { \Lambda } _ { 3 } = \left( \pmb { \Lambda } _ { 1 } \right) ^ { - 1 } \left( \pmb { \Lambda } _ { 2 } \right) ^ { - 1 } ,\tag{61c}
$$

$$
\hat { \alpha } _ { k } = \left( \left[ \Lambda _ { 3 } \right] _ { k , k } \mathbf { g } \left( \hat { \tau } _ { k } \right) \right) ^ { \dagger } \hat { \mathbf { g } } _ { k } .\tag{61d}
$$

The detailed procedures of the tensor-based parameter estimation scheme are summarized in Algorithm 2.

## E. Uniqueness Analysis

In this subsection, we discuss the uniqueness of the above tensor decomposition, which guarantees the correct recovery of the factor matrices and the subsequent parameter estimation. A well-known Kruskal sufficient uniqueness condition is provided in [29]. In addition, by leveraging more structural information of the factor matrices, the uniqueness can be further relaxed as [19], [28]

Lemma 2: Let $\pmb { \mathcal { X } } ~ \in ~ \mathbb { C } ^ { I _ { 1 } \times I _ { 2 } \times I _ { 3 } }$ be a tensor with three factor matrices $\mathbf { A } ^ { ( 1 ) } \in \mathbb { C } ^ { I _ { 1 } \times K } , \mathbf { A } ^ { ( 2 ) } \in \mathbb { C } ^ { I _ { 2 } \times K }$ and ${ \bf A } ^ { ( 3 ) } \in \\\\mathsf { \Gamma }$ $\mathbb { C } ^ { I _ { 3 } \times K }$ , where $\mathbf { A } ^ { ( 3 ) }$ is a Vandermonde matrix with distinct generators $\{ z _ { k } \} _ { k = 1 } ^ { K }$ . Denote $k _ { \mathbf { A } }$ as the Kruskal-rank of matrix A, if

$$
\left\{ \begin{array} { l l } { k _ { \left( \underline { { \mathbf { A } } } ^ { ( L _ { 1 } , 3 ) } \odot \mathbf { A } ^ { ( 2 ) } \right) } = K , } \\ { k _ { \left( \mathbf { A } ^ { ( L _ { 2 } , 3 ) } \odot \mathbf { A } ^ { ( 1 ) } \right) } = K , } \end{array} \right.\tag{62}
$$

```latex
Algorithm 2 Spatial Smoothing Tensor Decomposition
Approach For Parameter Estimation
1: Mode-1 unfold Y as (31);
2: Choose $\{ L _ { 1 } , L _ { 2 } \}$ and smooth $\mathbf { Y } _ { ( 1 ) } ^ { T }$ to $\mathbf { Y } ^ { S }$ as (33);
3: Perform the SVD of $\mathbf { Y } ^ { S }$ as (34);
4: Perform the EVD of $\Xi$ as (40);
5: Calculate the generators $\begin{array} { r c l } { \hat { z } _ { k } } & { = } & { [ \mathbf { Z } ] _ { k , k } / | [ \mathbf { Z } ] _ { k , k } | , K } & { = } \end{array}$
$1 , \ldots , K ;$
6: Construct each column of $\begin{array} { r l r l } { { \bf A } ^ { ( 3 ) } } & { { } \mathfrak { b } { \bf y } } & { \hat { { \bf g } } ( \tau _ { k } ) } & { { } = } \end{array}$
$\begin{array} { r } { \left[ 1 , \hat { z } _ { k } , \ldots , \hat { z } _ { k } ^ { M - 1 } \right] ^ { T } , k = 1 , \ldots , K ; } \end{array}$
7: Construct each column of $\mathbf { A } ^ { ( 2 ) }$ via (43);
8: Construct each column of $\mathbf { A } ^ { ( 1 ) }$ via (44);
9: Derive the time delay $\{ \hat { \tau } _ { k } \} _ { k = 1 } ^ { K } .$ , range $\{ \hat { d } _ { k } \} _ { k = 1 } ^ { K } ,$ , Doppler
frequency shift $\{ \hat { f } _ { k } ^ { d } \} _ { k = 1 } ^ { K }$ , radial velocity $\{ \hat { v } _ { k } \} _ { k = 1 } ^ { K } ,$ , ele
vation angle $\{ \hat { \theta } _ { k } \} _ { k = 1 } ^ { K }$ and azimuth angle $\{ \hat { \phi } _ { k } \} _ { k = 1 } ^ { K }$
via (45), (46), (47), (48), (59) and (60), respectively.
10: Eliminate the scaling ambiguity and estimate the channel
coefficients via (61a), (61b), (61c) and (61d), respectively.
```

then the rank of X is $K ,$ , and the tensor decomposition is unique. In the generic case, condition (62) becomes

$$
\operatorname* { m i n } \left( \left( L _ { 1 } - 1 \right) I _ { 2 } , L _ { 2 } I _ { 1 } \right) \geq K .\tag{63}
$$

Proof: Please refer to [28].

Recalling the formulation of $\mathbf { \boldsymbol { y } } ,$ the notations $I _ { 1 } , I _ { 2 } ,$ and $I _ { 3 }$ in Lemma 2 respectively denote the number of RF chains $R ,$ the number of OFDM symbols $N ,$ and the number of subcarriers M . Since there are a large number of subcarriers in current MIMO-OFDM systems, we can readily choose a pair of integer $\{ L _ { 1 } , L _ { 2 } \}$ satisfying $L _ { 1 } + L _ { 2 } = M + 1 , \left( L _ { 1 } - 1 \right) I _ { 2 } =$ $( L _ { 1 } - 1 ) N \ge K$ , and $L _ { 2 } I _ { 1 } = L _ { 2 } R \ge K$ . Therefore, the uniqueness condition can be readily satisfied. In addition, the uniqueness implies that the AoAs, Doppler shifts, and time delays will automatically be associated with the same target without designing additional pairing procedures [28].

## F. Complexity Analysis

We next analyze the complexities of the steps in Algorithm 2. It should be pointed out that the complexity of step 2 is negligible, since we can leverage the property of the sparse cyclic choose matrices, i.e., $\mathbf { J } _ { l }$ to collect specific rows of $\dot { \mathbf { Y } } _ { ( 1 ) } ^ { T }$ and stack them into the extended matrix $\mathbf { Y } ^ { S }$ instead of actually multiplying $\mathbf { Y } _ { ( 1 ) } ^ { T }$ by $\mathbf { J } _ { l } .$ At step 3, we perform the truncated SVD of $\dot { \mathbf { Y } } ^ { S }$ , which has the complexity of $\mathcal { O } \left( L _ { 1 } N K L _ { 2 } R \right)$ . At step 4, performing the EVD of $\Xi$ incurs the complexity of $\mathcal { O } \left( K ^ { 3 } \right)$ From step 5 to step $^ { 6 , }$ the reconstruction of $\mathbf { A } ^ { ( 3 ) }$ mainly requires the complexity of O (KM). Next, the total complexity of the reconstruction of $\mathbf { A } ^ { ( 2 ) }$ and $\mathbf { A } ^ { ( 1 ) }$ is given by $\mathcal { O } \left( L _ { 1 } N ^ { 2 } K + L _ { 1 } N K ^ { 2 } + L _ { 2 } R ^ { 2 } K + L _ { 2 } R K ^ { 2 } \right)$ . In the stage of parameter estimation, the derivations of $\{ \hat { f } _ { k } ^ { d } \} _ { k = 1 } ^ { K }$ has the complexity of $\mathcal { O } \left( N G K \right)$ , and the complexity of Algorithm 1 is given by $\mathcal { O } \left( P ^ { 3 } G \dot { K } + P G K \right)$ where G denotes the grid size. Finally, step 10 mainly has the complexity of $\mathcal { O } \left( \left( R + M + N \right) K \right)$ Thus, the total complexity of

![](images/83fa093f5585e075accc20c90e8f1b6834e5c0a8b285fb3b1b651f62709d9df1.jpg)  
Fig. 4. The relationship between the local and the global coordinate.

$$
\begin{array} { r l } & { \mathrm { A l g o r i t h m ~ 2 ~ c a n ~ b e ~ e x p r e s s e d ~ a s ~ } \mathcal { O } \bigl ( L _ { 1 } N K L _ { 2 } R + K ^ { 3 } { + } K M + } \\ & { L _ { 1 } N ^ { 2 } K + L _ { 1 } N K ^ { 2 } + L _ { 2 } R ^ { 2 } K + L _ { 2 } R K ^ { 2 } + N G K + P ^ { 3 } G K \bigr ) . } \end{array}
$$

## V. POSITION AND VELOCITY ESTIMATION

In this section, we enhance the positioning accuracy of the UAVs and recover their true velocities through the multi-BS cooperation, as the above monostatic parameter estimation method can only derive the UAVs’ radial velocities. Specifically, we first develop a false removing MST-based data association method, and then estimate the positions and velocities of the UAVs relying on the parameters estimated by the BSs, i.e., $\{ \hat { \theta } _ { k , j } , \hat { \phi } _ { k , j } , \hat { d } _ { k , j } , \hat { v } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , \top }$ , where the subscript j denotes the BS’s index.

## A. False Removing MST-Based Data Association

Noting that in conventional device-based sensing for active targets that can send/receive RF signals with different signatures, the BSs know the exact mapping between the estimation parameters of a certain target, i.e., each BS knows the true indices for all K UAVs. However, in the considered device-free sensing scenario, the detected UAVs’ indices may be different across the BSs. Thus, before performing the data fusion, we develop a false removing MST-based data association method. The initial phase of the data association involves each BS roughly estimating the positions of K UAVs relying on the AoA and range estimations, i.e., $\{ \hat { \theta } _ { k , j } , \hat { \phi } _ { k , j } , \bar { \hat { d } } _ { k , j } \bar  \} _ { k = 1 , j = 1 } ^ { K , J }$ . Specifically, the k-th UAV’s position estimated by BS<sub>j</sub> is given by

$$
\begin{array} { r } { \hat { \mathbf { p } } _ { k , j } = \hat { d } _ { k , j } \hat { \mathbf { r } } _ { k , j } + \mathbf { p } _ { j } ^ { \mathrm { B } } , } \end{array}\tag{64}
$$

where $\mathbf { p } _ { j } ^ { \mathrm { B } }$ denotes the position of ${ \mathrm { B S } } _ { j }$ in the global coordinate, and

$$
\hat { \mathbf { r } } _ { k , j } = \mathbf { T } \left( \phi _ { j } ^ { \mathrm { B } } \right) \left[ \sin \left( \hat { \theta } _ { k , j } \right) \cos \left( \hat { \phi } _ { k , j } \right) \right] ,\tag{65}
$$

is the direction vector in the global coordinate. The notation $\mathbf { T } \left( \phi _ { j } ^ { \mathrm { B } } \right)$ denotes the transform matrix from the $\mathbf { B } \mathbf { S } _ { j } \mathbf { \bar { \Sigma } } _ { \mathbf { S } }$ local coordinate to the global coordinate. Without loss of generality, as shown in Fig. 4, we assume that the antenna panel of each BS is parallel to the z-axis of the global coordinate, and $\phi _ { j } ^ { \mathbf { B } }$ is the angle between the x-axis of the $\mathbf { B S } _ { j } \mathbf { \ ' } _ { \mathbf { S } }$ local coordinate and the x-axis of the global coordinate. In this way, the transform matrix can be expressed as [7]

![](images/8c85768a48e56a56850790ff4e07272e7c8962ca8a5429d93fab2ecc1829426c.jpg)  
Fig. 5. An illustration of the MST of graph G<sup>˜</sup>.

$$
\begin{array} { r } { \mathbf { T } \left( \phi _ { j } ^ { \mathrm { B } } \right) = \left[ - \frac { \cos \left( \phi _ { j } ^ { \mathrm { B } } \right) } { \sin \left( \phi _ { j } ^ { \mathrm { B } } \right) } \sin \left( \phi _ { j } ^ { \mathrm { B } } \right) 0 \right] . } \\ { 0 \phantom { \frac { \cos \left( \phi _ { j } ^ { \mathrm { B } } \right) } { \cos \left( \phi _ { j } ^ { \mathrm { B } } \right) } 0 } 0 } \end{array}\tag{66}
$$

Then, according to the positioning results of the BSs, i.e., $\{ \widehat { \mathbf { p } } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , J }$ and leveraging the similarity of positioning results for the same UAV across the BSs, a straightforward association approach is to minimize the sum of the Euclidean distances between the positioning results from the different BSs via the exhaustive permutation method [30]. However, the complexity rises sharply with the value of K. In addition, the permutation method does not remove the false detections, while it is evident that integrating these false detection results with the correct detection results will greatly impact the following data fusion process.

To address these issues, we propose a false removing MST-based data association method. Specifically, we first construct an undirected weighted graph $G ~ = ~ ( V , E )$ . The vertex set V represents the union of a series of sub-vertex sets, i.e.,

$$
V = V _ { 1 } \cup V _ { 2 } \cup \cdots \cup V _ { J } ,\tag{67}
$$

where $V _ { j } = \left\{ \left( j - 1 \right) K + 1 , \ldots , j K \right\} , j = 1 , \ldots , J$ denotes the K positioning results of ${ \mathrm { B S } } _ { j }$ . The edge set E is defined as

$$
E = \left\{ ( a , b ) \left| a \in V _ { j } , b \in V \setminus V _ { j } , j = 1 , \ldots , J \right. \right\} ,\tag{68}
$$

and the weights of the edges are defined as the Euclidean distances between the positioning results derived by the BSs, i.e.,

$$
\begin{array} { r l } & { W _ { a b } = | | \hat { \mathbf { p } } _ { ( a - 1 ) \mathrm { ~ m o d ~ } K + 1 , \lfloor \frac { a - 1 } { K } \rfloor + 1 } } \\ & { \qquad - \hat { \mathbf { p } } _ { ( b - 1 ) \mathrm { ~ m o d ~ } K + 1 , \lfloor \frac { b - 1 } { K } \rfloor + 1 } | | _ { 2 } , \forall a , b \in E , } \end{array}\tag{69}
$$

where the notations mod and ⌊·⌋ denote the modulus and floor operations, respectively. To prevent the false detection results from impacting the subsequent data fusion, we define the following edge set as

$$
E ^ { \prime } = \{ ( a , b ) | W _ { \operatorname* { m i n } } ( a ) > \varsigma , a , b \in E \} ,\tag{70}
$$

where $W _ { \mathrm { m i n } } \left( a \right) > \varsigma$ indicates that the shortest adjacent edge of vertex a is longer than the threshold ς. Then, we update

![](images/373d7ec279264fbe4cd6487709215358fa3559070d1733fade033fd206e62940.jpg)

![](images/148df5bb59df91413ce4168e11839d6a64d03c6da85fb42f601bb7f48c706793.jpg)  
(a) Rough position estimation relying on the mean fusion.  
(b) Calculate the OF values.  
Fig. 6. An illustration of the Pareto optimality fusion scheme.

the edge set $\mathrm { a s } ^ { 2 }$

$$
{ \tilde { E } } = E \setminus E ^ { \prime } .\tag{71}
$$

In this way, in the updated graph $\tilde { G } = ( V , \tilde { E } )$ , these false detection results are displayed as the isolated vertices. Then, we derive the MST of the connected components of graph G<sup>˜</sup> via the well-known Prim [31] or Kruskal [32] algorithm. As shown in Fig. 5, given that the positioning results of the BSs for the same UAV are more similar than those for the distinct UAVs, the MST algorithm will always connect the positioning results of the multiple BSs for the same UAV. Subsequently, by removing the K − 1 longest edges from the MST, the positioning results from the BSs for K UAVs are divided into K sub-graphs. By collecting the vertex indices in each sub-graph, the data association can be immediately accomplished. In the following contents of this paper, we assume that each BS holds the same indices of the UAVs. In addition, for a certain UAV, these false detections and estimations derived by the BSs will not be incorporated in the data fusion, even though we still utilize the notation J for notational simplicity.

## B. Position Estimation

After accurate data association, we then perform the data fusion across the multiple BSs. In general, there are two primary fusion strategies: hard fusion and soft fusion [7]. Specifically, the former denotes that each BS estimates and sends the final positioning results, i.e., $\{ \hat { \mathbf { p } } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , J }$ to the cloud. Then, the cloud integrates the position estimations via a (weighted) mean fusion scheme. For instance, the position estimation relying on the mean fusion is given by

$$
\hat { \mathbf { p } } _ { k } = \frac { 1 } { J } \sum _ { j = 1 } ^ { J } \hat { \mathbf { p } } _ { k , j } , \ k = 1 , \ldots , K .\tag{72}
$$

Differently, with the soft fusion strategy, all BSs send the original parameter estimations, including the AoAs and ranges to the cloud. Then, the cloud performs the estimation of the UAVs’ positions via integrating these uploaded parameters.

Since the soft fusion provides more fine-grained information for the data fusion, we mainly focus on this fusion strategy in the following contents of this paper. Specifically, noting that the accuracy of position estimation mainly depends on the range and radial direction (determined by the AoAs) estimations, we respectively define the following range loss function and direction loss function as

$$
f _ { \mathrm { r } } \left( \mathbf { p } _ { k } \right) = \frac { \sum _ { j = 1 } ^ { J } \alpha _ { k , j } \left| d _ { k , j } \left( \mathbf { p } _ { k } \right) - \hat { d } _ { k , j } \right| } { \sum _ { j = 1 } ^ { J } \alpha _ { k , j } } ,\tag{73a}
$$

$$
f _ { \mathrm { d } } \left( \mathbf { p } _ { k } \right) = \frac { \sum _ { j = 1 } ^ { J } \alpha _ { k , j } \left\| \mathbf { r } _ { k , j } \left( \mathbf { p } _ { k } \right) - \hat { \mathbf { r } } _ { k , j } \right\| _ { 2 } } { \sum _ { j = 1 } ^ { J } \alpha _ { k , j } } ,\tag{73b}
$$

where $\begin{array} { r c l } { { d _ { k , j } ( { \bf p } _ { k } ) } } & { { = } } & { { \left\| { { \bf p } _ { k } - { \bf p } _ { j } ^ { \mathrm { B } } } \right\| _ { 2 } } } \end{array}$ denotes the true range between the UAV and the BS, and $\mathbf { r } _ { k , j } \left( \mathbf { p } _ { k } \right)$ denotes the true radial direction vector determined by the k-th UAVs’ true position $\mathbf { p } _ { k } .$ . The notation $\alpha _ { k , j }$ denotes the weight assigned to ${ \mathrm { B } } { \mathrm { S } } _ { j }$ . Specifically, due to path loss, the SNR of the echo signals decreases with the increase of the range between the UAVs and the BSs. Thus, we define the weighting coefficient as

$$
\alpha _ { k , j } = \frac { 1 } { \left( d _ { k , j } ( \mathbf { p } _ { k } ) \right) ^ { \beta _ { 1 } } } ,\tag{74}
$$

where $\beta _ { 1 } > 0$ is a factor introduced to control the weighting intensity. Then, we address the following problem to estimate the position of the k-th UAV, i.e.,

$$
\operatorname* { m i n } _ { \mathbf { p } _ { k } } \left\{ f _ { \mathrm { r } } \left( \mathbf { p } _ { k } \right) , f _ { \mathrm { d } } \left( \mathbf { p } _ { k } \right) \right\} ,\tag{75}
$$

which is a highly nonlinear multi-objective optimization problem with the OFs holding distinct dimensions. To address Problem (75), we propose a Pareto optimality strategy to determine the UAVs’ positions. Specifically, as shown in Fig. 6, we first take the mean fusion result in (72) as a rough position estimation. Then, we construct L lattice points around the rough estimation and calculate the two OF values corresponding to these lattice points. To minimize both two OF values simultaneously, we first recognize the dominated solutions among the lattice points, i.e.,

$$
\tilde { U } _ { k } = \{ \mathbf { p } _ { k } ^ { l _ { 1 } } | f _ { \mathrm { r } } ( \mathbf { p } _ { k } ^ { l _ { 1 } } ) > f _ { \mathrm { r } } ( \mathbf { p } _ { k } ^ { l _ { 2 } } ) , f _ { \mathrm { d } } ( \mathbf { p } _ { k } ^ { l _ { 1 } } ) > f _ { \mathrm { d } } ( \mathbf { p } _ { k } ^ { l _ { 2 } } ) , \mathbf { p } _ { k } ^ { l _ { 1 } } , \mathbf { p } _ { k } ^ { l _ { 2 } } \in U _ { k } \} ,\tag{76}
$$

where $U _ { k } = \left\{ \mathbf { p } _ { k } ^ { 1 } , \ldots , \mathbf { p } _ { k } ^ { L } \right\}$ denotes the set formed by L lattice points. Then, we remove the dominated solutions and retain the Pareto set of the solutions as

$$
\bar { U } _ { k } = U _ { k } \backslash \tilde { U } _ { k } .\tag{77}
$$

Finally, we determine the solution from the Pareto set as the final position estimation relying on the system configuration. Specifically, in the scenarios where each BS is allocated a substantial number of subcarriers but only equipped with relatively a small number of antennas, the range estimation always exhibits a higher precision than AoA estimation. Thus, the range estimation should be more dominant for positioning. In such cases, we can choose the solution from the Pareto set, which has the minimum range loss function value, i.e.,

$$
\hat { \mathbf { p } } _ { k } = \arg \operatorname* { m i n } _ { \mathbf { p } _ { k } ^ { l } \in \bar { U } _ { k } } f _ { \mathrm { r } } \left( \mathbf { p } _ { k } ^ { l } \right) .\tag{78}
$$

![](images/ce252bfb5d54f924f9035bb73d88a450b7f546a845603c73ba6b750b79a24082.jpg)  
Fig. 7. The relationship between the radial velocity and the true velocity (assume that the global coordinate coincides with the local coordinate).

On the flip side, when the BSs are equipped with a large number of antennas but a small number of subcarriers, the AoA estimation becomes the critical factor, guiding the choice of the solution with minimum direction loss function value from the Pareto set, i.e.,

$$
\hat { \mathbf { p } } _ { k } = \arg \operatorname* { m i n } _ { \mathbf { p } _ { k } ^ { l } \in \bar { U } _ { k } } f _ { \mathrm { d } } \left( \mathbf { p } _ { k } ^ { l } \right) .\tag{79}
$$

In addition, we can also take into account the accuracy of AoA and range estimation in the designed monostatic parameter estimation algorithm to achieve better positioning performance. Noting that only several simple calculations are required to calculate the OF values corresponding to the lattice points, so the complexity is tolerant.

## C. Velocity Estimation

Noting that relying on the above positioning scheme, we always achieve an enhanced estimation of the UAVs’ positions via the cooperation compared to the monostatic position estimation. Thus, we can calibrate the previous AoA and range estimations, i.e., $\{ \hat { \theta } _ { k , j } , \hat { \phi } _ { k , j } , \hat { d } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , J }$ relying on the cooperative position estimations. For notational simplicity, we continue to use the original notations to denote the calibrated estimations.

According to the tensor decomposition procedures in Section IV, each BS can only estimate the radial velocities of the UAVs, i.e., $\{ \hat { v } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , J }$ . In this subsection, we estimate the true velocity of each UAV based on $\{ \hat { v } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , J }$ and $\{ \hat { \theta } _ { k , j } , \hat { \phi } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , J } .$ . To perform the estimation, we first explore the relationship between the true velocity and the radial velocity. As shown in Fig. 7, we denote $\mathbf { v } _ { k } ^ { \mathrm { T r u e } } \ =$ $\left[ v _ { k } ^ { x } , v _ { k } ^ { y } , v _ { k } ^ { z } \right] ^ { T }$ as the true velocity of the k-th UAV, where the elements represent the velocity components on the three coordinate axises of the global coordinate. Then, by projecting the three components to the radial direction, we have

$$
\hat { \mathbf { r } } _ { k , j } ^ { T } \mathbf { v } _ { k } ^ { \mathrm { T r u e } } = \hat { v } _ { k , j } + \varepsilon _ { k , j } , \quad j = 1 , \ldots , J ,
$$

where

(80)

where $\hat { \mathbf { r } } _ { k , j }$ denotes the (calibrated) radial direction vector defined by (65), and $\varepsilon _ { k , j }$ denotes the estimation error. As such, by stacking all the radial velocity estimations derived by J BSs, (80) can be rewritten in a more compact form as

$$
\begin{array} { r } { \hat { \Omega } _ { k } \mathbf { v } _ { k } ^ { \mathrm { T r u e } } = \hat { \mathbf { v } } _ { k } + \boldsymbol { \varepsilon } _ { k } , } \end{array}\tag{81}
$$

$$
\hat { \pmb { \Omega } } _ { k } = \left[ \begin{array} { c } { \hat { \mathbf { r } } _ { k , 1 } ^ { T } } \\ { \vdots } \\ { \hat { \mathbf { r } } _ { k , J } ^ { T } } \end{array} \right] , \hat { \mathbf { v } } _ { k } = \left[ \begin{array} { c } { \hat { v } _ { k , 1 } } \\ { \vdots } \\ { \hat { v } _ { k , J } } \end{array} \right] , \varepsilon _ { k } = \left[ \begin{array} { c } { \varepsilon _ { k , 1 } } \\ { \vdots } \\ { \varepsilon _ { k , J } } \end{array} \right] .\tag{82}
$$

Then, the true velocity of the k-th UAV can be derived by the well-known weighted LS (WLS) estimation, i.e.,

$$
\hat { \mathbf { v } } _ { k } ^ { \mathrm { T r u e } } = \left( \hat { \Omega } _ { k } ^ { T } \mathbf { W } _ { k } \hat { \Omega } _ { k } \right) ^ { - 1 } \hat { \Omega } _ { k } ^ { T } \mathbf { W } _ { k } \hat { \mathbf { v } } _ { k } ,\tag{83}
$$

where $\mathbf { W } _ { k } ~ = ~ \operatorname { D } \left( \left[ \gamma _ { k , 1 } , \ldots , \gamma _ { k , J } \right] \right)$ denotes the weighting matrix with the diagonal element $\begin{array} { r } { \gamma _ { k , j } ~ = ~ \frac { 1 } { \left( \hat { d } _ { k , j } \right) ^ { \beta _ { 2 } } } } \end{array}$ denoting the weight assigned to the $\mathbf { B } \mathbf { S } _ { j } \mathbf { \bar { \Sigma } } _ { \mathbf { S } }$ estimation, and $\beta _ { 2 } ~ > ~ 0$ denotes the weighting intensity factor. However, noting that the number of BSs in the cooperative ISAC systems is limited, which makes the above WLS method still sensitive to the estimation error. Therefore, we propose a more robust residual weighting-based method to suppress the impacts of estimation error. Specifically, the method mainly includes the following three steps [33]:

1) Grouping BSs: Noting that to recover the true velocity, at least three BSs’ estimations are required. Therefore, we select all combinations from $J \geq 3 ~ \mathrm { B S s }$ including at least three BSs. In this way, the total number of the combinations is given by

$$
I = \sum _ { j = 3 } ^ { J } C _ { J } ^ { j } .\tag{84}
$$

Then, we collect all the combinations into a set as $\chi =$ $\{ X _ { i } | i = 1 , \ldots , I \}$

2) Calculating Residuals: For a certain combination, we adopt the mentioned WLS method to derive the rough estimation of the k-th UAV’s true velocity relying on the BSs’ estimations within the combination, which is denoted as $\hat { \mathbf { v } } _ { k } ^ { i }$ . Then, we calculate the residuals among all the BSs, i.e.,

$$
\operatorname { R e s } \left( X _ { i } \right) = \sum _ { j = 1 } ^ { J } \gamma _ { k , j } \left( \hat { \mathbf { r } } _ { k , j } ^ { T } \hat { \mathbf { v } } _ { k } ^ { i } - \hat { v } _ { k , j } \right) ^ { 2 } , i = 1 , \ldots , I .\tag{85}
$$

3) Weighting the Estimations Based on the Residuals: Relying on the calculated residuals, the true velocity is estimated as

$$
\hat { \mathbf { v } } _ { k } ^ { \mathrm { T r u e } } = \frac { \sum _ { i = 1 } ^ { I } \Big \{ \mathrm { R e s } \left( X _ { i } \right) ^ { - 1 } \hat { \mathbf { v } } _ { k } ^ { i } \Big \} } { \sum _ { i = 1 } ^ { I } \mathrm { R e s } \left( X _ { i } \right) ^ { - 1 } } .\tag{86}
$$

As previously stated, the number of BSs in cooperative ISAC systems is often limited, so the computational complexity of the above method is tolerant. When the number of BSs is large, we can adopt several existing greedy strategies to further reduce the complexity [34].

Based on the above discussions, the detailed procedures of the overall cooperative position and velocity estimation method are summarized in Algorithm 3.

Algorithm 3 Cooperative Position and Velocity Estimation   
Scheme   
1: Multi-BS data association:   
2: Calculate the UAVs’ positions $\{ \hat { \mathbf { p } } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , J }$ via (64);   
3: Construct graph G with $\{ \widehat { \mathbf { p } } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , J } ;$   
4: Update graph $\tilde { G }$ by removing the false detection results   
via (71);   
5: Derive the MST of graph ${ \tilde { G } } ;$   
6: Remove the $K - 1$ longest edges from the MST and collect   
the vertex indices in each sub-graph.   
7: Position estimation:   
8: Derive the rough position estimation $\{ \hat { \mathbf { p } } _ { k } \} _ { k = 1 } ^ { K }$ via (72);   
9: Construct L lattice points $U _ { k }$ around the rough position   
estimation;   
10: Calculate the two OF values corresponding to lattice   
points $U _ { k }$ via (73a) and (73b);   
11: Remove the dominated solutions and retain the Pareto set   
$\bar { U } _ { k }$ via (77);   
12: Estimate the UAVs’ positions via (78) or (79).   
13: Velocity estimation:   
14: Calibrate the previous AoA and range estimations,   
i.e., $\{ \hat { \theta } _ { k , j } , \hat { \phi } _ { k , j } , \hat { d } _ { k , j } \} _ { k = 1 , j = 1 } ^ { K , J } \mathrm { r e l y i n g }$ on the cooperative   
position estimations;   
15: Group the BSs and adopt the WLS method to derive the   
rough estimation of the $\mathrm { U A V s } '$ true velocity;   
16: Calculate the residuals of the BS combinations via (85);   
17: Weight the estimations with the residuals via (86).

## VI. EXTENSION TO THE DUAL-POLARIZED SYSTEM

In this section, we extend the proposed tensor decomposition parameter estimation scheme to the dual-polarized system. Specifically, the sensing channel matrix is modified as [35]

$$
\mathbf { H } _ { m , n } = \left[ \mathbf { H } _ { m , n } ^ { \mathrm { ( V _ { r } , V _ { t } ) } } ~ \mathbf { H } _ { m , n } ^ { \mathrm { ( V _ { r } , H _ { t } ) } } \right] \in \mathbb { C } ^ { 2 P Q \times 2 P Q } ,\tag{87}
$$

where $\mathbf { H } _ { m , n } ^ { ( \mathrm { V _ { r } , V _ { t } } ) } \in \mathbb { C } ^ { P Q \times P Q }$ denotes the sub-channel matrix between the vertical (V)-polarized transmit antennas and the V-polarized receive antennas (for the considered monostatic sensing scenario, the transmit antennas are also served as the receive antennas), and likewise for the other three blocks in (87). For notational simplicity, let $\delta \in \mathsf { \Omega } \{ \mathrm { V } _ { \mathrm { r } } , \mathrm { H } _ { r } \}$ and $\eta \in \mathsf { \Omega } \{ \mathrm { V } _ { t } , \mathrm { H } _ { t } \}$ . Then, similar to the channel modeling in Section II-B, the $( \delta , \eta )$ -th sub-channel matrix is modeled as

$$
\begin{array} { l } { { \displaystyle { \bf H } _ { m , n } ^ { \delta , \eta } } } \\ { { \displaystyle = \sum _ { k = 1 } ^ { K } \beta _ { k } ^ { ( \delta , \eta ) } { \bf a } \left( \vartheta _ { k } , \psi _ { k } \right) { \bf a } \left( \vartheta _ { k } , \psi _ { k } \right) ^ { H } \cdot e ^ { - j 2 \pi m \Delta f \tau _ { k } } \cdot e ^ { j 2 \pi f _ { k } ^ { d } n T _ { s } } , } } \end{array}\tag{88}
$$

where

$$
\beta _ { k } ^ { ( \delta , \eta ) } = \alpha _ { k } \gamma _ { k } ^ { ( \delta , \eta ) } ,\tag{89}
$$

and $\gamma _ { k } ^ { ( \delta , \eta ) }$ denotes the polarization factor [35]. In order to formulate the received signal into a fourth-order tensor, we set the transmit precoding and the receive combining matrices for both the V-polarized and H-polarized channels to be the same. In this way, the equivalent transmit precoding and receive combining matrices for dual-polarization are respectively given by

$$
\tilde { \mathbf { F } } _ { R X } = \mathbf { I } _ { 2 } \otimes \mathbf { F } _ { R X } \in \mathbb { C } ^ { 2 P Q \times 2 R } ,\tag{90a}
$$

$$
\tilde { \mathbf { F } } _ { T X } = \mathbf { I } _ { 2 } \otimes \mathbf { F } _ { T X } \in \mathbb { C } ^ { 2 P Q \times 2 R } .\tag{90b}
$$

To avoid the interference between dual-polarization, we assume that both dual-polarized channels share the same transmitted data. Then, the received signal vector of each polarization can be expressed as

$$
\begin{array} { r } { \mathbf { y } _ { m , n } ^ { \delta } = \mathbf { F } _ { R X } ^ { H } \mathbf { H } _ { m , n } ^ { \delta } \tilde { \mathbf { F } } _ { T X } \tilde { \mathbf { e } } \cdot s _ { m , n } + \mathbf { F } _ { R X } ^ { H } \mathbf { n } _ { m , n } ^ { \delta } \in \mathbb { C } ^ { R \times 1 } , } \end{array}\tag{91}
$$

where $\mathbf { H } _ { m , n } ^ { \delta } = \left[ \mathbf { H } _ { m , n } ^ { ( \delta , \mathrm { V } _ { t } ) } , \mathbf { H } _ { m , n } ^ { ( \delta , \mathrm { H } _ { t } ) } \right] , \delta \in \left\{ \mathrm { V } _ { r } , \mathrm { H } _ { r } \right\}$ , and $\tilde { \textbf { e } } =$ $[ 1 , \ldots , 1 ] ^ { T } \ \in \ \mathbb { R } ^ { 5 R \times 1 }$ denotes an all-one vector. Similarly, we still multiply the received signal vector by the conjugate of the transmitted data to eliminate its impacts, i.e.,

$$
\begin{array} { r } { \tilde { { \bf y } } _ { m , n } ^ { \delta } = s _ { m , n } ^ { * } { \bf y } _ { m , n } ^ { \delta } = { \bf F } _ { R X } { \bf H } _ { m , n } \tilde { { \bf F } } _ { T X } \tilde { \bf e } + \tilde { \bf n } _ { m , n } ^ { \delta } \in \mathbb { C } ^ { R \times 1 } . } \end{array}\tag{92}
$$

Then, stacking the received signal $\tilde { \mathbf { y } } _ { m , n } ^ { \delta }$ among dual polarization, N OFDM symbols, and M subcarriers into the following fourth-order tensor as

$$
\mathcal { Z } = \sum _ { k = 1 } ^ { K } \alpha _ { k } \mathbf { b } \left( \vartheta _ { k } , \psi _ { k } \right) \circ \pmb { \eta } _ { k } \circ \mathbf { g } \left( \tau _ { k } \right) \circ \mathbf { o } \left( f _ { k } ^ { d } \right) + \pmb { \mathcal { N } } ,\tag{93}
$$

where $\begin{array} { r l r } { \eta _ { k } } & { = } & { \Big [ \gamma _ { k } ^ { ( \mathrm { V _ { r } , V _ { t } } ) } + \gamma _ { k } ^ { ( \mathrm { V _ { r } , H _ { t } } ) } , \gamma _ { k } ^ { ( \mathrm { H _ { r } , V _ { t } } ) } + \gamma _ { k } ^ { ( \mathrm { H _ { r } , H _ { t } } ) } \Big ] ^ { T } , } \end{array}$ and the corresponding factor matrix introduced by dual-polarization is given by

$$
\mathbf { B } = [ \pmb { \eta } _ { 1 } , \dots , \pmb { \eta } _ { K } ] \in \mathbb { C } ^ { 2 \times K } .\tag{94}
$$

The mode-1 unfolding of $\mathcal { Z }$ is given by

$$
\mathbf { Z } _ { ( 1 ) } ^ { T } = \left( \mathbf { A } ^ { ( 3 ) } \odot \mathbf { A } ^ { ( 2 ) } \odot \mathbf { B } \right) \left( \mathbf { A } ^ { ( 1 ) } \right) ^ { T } \in \mathbb { C } ^ { 2 N M \times R } .\tag{95}
$$

Similarly, by defining the combining factor matrix as

$$
\begin{array} { r } { \mathbf { E } \triangleq \mathbf { A } ^ { ( 2 ) } \odot \mathbf { B } , } \end{array}\tag{96}
$$

we can perform the tensor decomposition procedures proposed in Section IV to recover the factor matrices, i.e, $\mathbf { A } ^ { ( 1 ) } , \mathbf { A } ^ { ( 3 ) }$ and E. The decoupling of $\mathbf { A } ^ { ( 2 ) }$ and B are as follows. Let $\hat { \mathbf { E } } _ { k } = \mathrm { u n v e c } _ { 2 \times N } \left( \hat { \mathbf { e } } _ { k } \right)$ , where $\hat { \mathbf { e } } _ { k }$ denotes the k-th column of E<sup>ˆ</sup> . Then, each column of $\mathbf { A } ^ { ( 2 ) }$ and B can be estimated by addressing the following problem as [18]

$$
\left\{ \hat { \mathbf { o } } _ { k } , \hat { \pmb { \eta } } _ { k } \right\} = \arg \operatorname* { m i n } _ { \mathbf { o } _ { k } , { \pmb { \eta } } _ { k } } \left\| \hat { \mathbf { E } } _ { k } - { \pmb { \eta } } _ { k } \mathbf { o } _ { k } ^ { T } \right\| _ { F } ^ { 2 } ,\tag{97}
$$

which can be solved via performing the SVD of $\hat { \mathbf { E } } _ { k }$ . Specifically, according to the Eckart–Young–Mirsky theorem [36], we have $\hat { \pmb { \eta } } _ { k } = \lambda _ { k , 1 } { \bf u } _ { k , 1 }$ and $\hat { \mathbf { o } } _ { k } \ = \mathbf { v } _ { k , 1 } ^ { * }$ , where $\lambda _ { k , 1 } , ~ { \bf u } _ { k , 1 }$ and $\mathbf { v } _ { k , 1 }$ denote the maximum singular value of $\hat { \mathbf { E } } _ { k }$ , the corresponding left singular vector, and the corresponding right singular vector, respectively. Subsequently, we can estimate the multiple parameters from the recovered matrices as discussed in Section IV-D.

![](images/be1413ae6352a2810470d7e63f0fe3cafaab1261f5c79ee18202388114e3e360.jpg)  
Fig. 8. The top view of the simulation layout.

## VII. NUMERICAL SIMULATIONS

In this section, simulation results are presented to evaluate the performance of the proposed schemes. We first provide the simulation parameter settings. Then, we compare the performance of the proposed monostatic parameter estimation scheme with that of conventional techniques. Subsequently, we demonstrate the performance of the cooperative position and velocity estimation. Finally, we evaluate the generality of the proposed scheme in a degraded scenario and compare its performance with the state-of-the-art cooperative ISAC scheme.

## A. Simulation Settings

Unless stated otherwise, the simulation parameters are set as follows: Each BS is equipped with a half-wavelength UPA with $P = 1 6$ and $Q = 2 4$ antennas located in horizontal and vertical directions, respectively. The number of RF chains is given by $R = 6 4$ . The non-zero elements of the precoding matrix are designed with the guidelines of the prior information provided in Section III. The non-zero elements of the combining matrix are chosen uniformly from a normalized unit circle to guarantee the uniqueness of the tensor decomposition [16] and the unambiguity of AoA estimation in the considered HBF structure. In order to avoid the interference between the BSs, we assume that each BS is allocated a non-overlapping 20 MHz bandwidth with 612 subcarriers. We set the central frequency of 4.9 GHz and the SCS of $\Delta f = 3 0$ KHz. The number of OFDM symbols utilized for sensing is set to $N \mathrm { ~  ~ { ~ = ~ } ~ } 7$ . According to the 5G new radio (NR) standard, the total period of OFDM symbol (including the cyclic prefix) is given by $T _ { s } = 3 5 . 6 7 7 \mu \mathrm { s } [ 3 7 ]$ . The velocity of each UAV is uniformly distributed in $[ V _ { \mathrm { m i n } } , V _ { \mathrm { m a x } } ]$ , where $V _ { \mathrm { m i n } } = 5$ km/h and $V _ { \mathrm { m a x } } = 1 0 0$ km/h denote the minimum and the maximum velocity of the UAVs, respectively. The RCS of each UAV is set to $\sigma = 0 . 0 1 \mathrm { ~ m ^ { 2 } }$ . The path loss in dB is given by [38]

$$
\mathrm { P L } = 1 0 3 . 4 + 2 0 \log { ( f / \mathrm { M H z } ) } + 4 0 \log { ( d / \mathrm { k m } ) } - 1 0 \log { \left( \sigma / \mathrm { m ^ { 2 } } \right) } ,\tag{98}
$$

where $f$ denotes the central frequency, and d denotes the range between the UAV and the BS. The noise power density is set to −174 dBm/Hz. For the simulation layout, as depicted in Fig. 8, there are $J = 4$ BSs uniformly situated on a circle with the radius of $r _ { 2 } = 4 5 0 ~ \mathrm { m }$ , with their UPA panels point towards the center of the circle, and the height of each BS is set to 30 m. The transmit power budget of each BS is set to 58 dBm. In addition, it is assumed that there are $K = 4 { \mathrm { U A V s } }$ uniformly distributed with their projections on the x-y plane within a circle with the radius of $r _ { 1 } = 4 0 0 ~ \mathrm { m }$ , and the heights of the UAVs are uniformly distributed in $[ h _ { \operatorname* { m i n } } , h _ { \operatorname* { m a x } } ]$ , where $h _ { \operatorname* { m i n } } = 3 5$ m and $h _ { \operatorname* { m a x } } = 3 0 0$ m denote the lowest and the highest flight heights of the UAVs, respectively. To evaluate the performance of parameter estimation, the following root mean square error (RMSE) is adopted [19], i.e.,

![](images/f136f4d3c9af15faf3e11c5fb4535fd35cfcf4480d2a52b8d2c6ab3bf2e9bdd0.jpg)

![](images/1e8e6f80eb688a077eab979dd17824f9ed678d9e2288ad2d1d024be58757a285.jpg)  
(b) Range

(a) AoA  
![](images/5de1e746a5a7c856e8d0cadc81e778bed081176a1b8cba5034cbe55623504abb.jpg)  
(c) Radial velocity

![](images/3086467509921e770c5a35e9ffcc2245fd6fade1a759b08190d1a43a59a036e0.jpg)  
(d) Position  
Fig. 9. Estimation RMSE vs. the transmit power budget.

$$
\mathrm { R M S E } \left( \mathbf { x } \right) = \sqrt { \frac { 1 } { K } \sum _ { k = 1 } ^ { K } { \| \hat { \mathbf { x } } _ { k } - \mathbf { x } _ { k } \| _ { 2 } ^ { 2 } } } ,\tag{99}
$$

where $\hat { \mathbf { x } } _ { k }$ and $\mathbf { x } _ { k }$ respectively denote the estimated and the true value of parameters, including the UAVs’ AoAs, range, radial velocity, position, and true velocity. The simulation results are obtained by averaging over 95% of more than 1000 independent realizations to ignore the effect of outliers [19]. Additionally, we consider a conventional approach relying on the MUSIC and FFT algorithms as a benchmark (denoted as “Benchmark1”). Specifically, in this scheme, the UAVs’ AoAs are first derived by the well-known 2-D MUSIC algorithm [39]. Then, the 2-D FFT operation is performed to estimate the ranges and radial velocities of UAVs [7]. To ensure the automatic pairing of the multi-dimensional parameters, this benchmark also operates on the formulation of the mode-1 unfolding of tensor Y , i.e., (31).

## B. Monostatic Parameter Estimation

According to the above discussions, since each BS performs the same parameter estimation algorithm before the data fusion, we first set $J \ = \ 1$ to evaluate the performance of the proposed monostatic parameter estimation scheme.

Figs. 9(a)-9(c) respectively illustrate the RMSE of AoA, range, and radial velocity estimation versus the transmit power budget. From Figs. 9(a)-9(c), we observe that as the transmit power increases, both two schemes achieve lower estimation RMSE. In addition, due to the limitations in antenna array size and sensing resource allocation, we find that the estimation RMSE of Benchmark1 is prone to encountering a performance bottleneck. However, the estimation RMSE of the proposed scheme shows a significant decline with the increase of transmit power, which validates its effectiveness. Correspondingly, Fig. 9(d) illustrates that the proposed tensor decomposition scheme achieves higher positioning accuracy than Benchmark1, since the former achieves the enhanced AoA and range estimation performance.

![](images/eb9ecaa84065c3f31ae9c0eb95a31ffc9c44bf382c3285bbb661fb827b9af1d4.jpg)  
Fig. 10. Position estimation RMSE vs. the transmit power budget in the dual-polarized system.

In addition, we also provide the position estimation results in the dual-polarized system (denoted as “DP”) and compare with the single-polarized configuration (denoted as $\mathbf { \tilde { \Sigma } } ^ { \mathrm { s } } \mathbf { P } ^ { \prime } )$ in Fig. 10 with the number of UAVs of $K = 4 .$ . The parameters of DP configuration are set as follows. For the sake of clarity, we rewrite the polarization factor as

$$
\gamma _ { k } ^ { ( \delta , \eta ) } = \sqrt { r _ { k } ^ { ( \delta , \eta ) } } e ^ { j \phi _ { k } ^ { ( \delta , \eta ) } } ,\tag{100}
$$

where $r _ { k } ^ { ( \delta , \eta ) }$ denotes the random variable representing the power ratio of waves from $\eta \mathrm { ~ = ~ } \{ \mathrm { V } _ { t } , \mathrm { H } _ { t } \}$ transmit antennas to $\delta \in \mathsf { \{ V }  _ { \mathrm { r } } , \mathrm { H } _ { r } \}$ receive antennas, $\phi _ { k } ^ { ( \delta , \eta ) }$ denotes the additional phase. According to the 3rd generation partnership project (3GPP) technical report (TR) [40], we let $\begin{array} { r } { r _ { k } ^ { \left( \mathrm { V } _ { r } , \mathrm { V _ { t } } \right) } = } \end{array}$ $\begin{array} { r l r } { \bar { r } _ { k } ^ { ( \mathrm { H } _ { r } , \mathrm { H } _ { \mathrm { t } } ) } } & { { } = } & { 1 } \end{array}$ and $r _ { k } ^ { ( \mathrm { V } _ { r } , \mathbf { \hat { H } _ { t } } ) } , r _ { k } ^ { ( \mathrm { H } _ { r } , \mathrm { V \hat { t } } ) } ~ = ~ 1 / \xi ,$ where $\xi$ denotes the cross-polarization discrimination (XPD) obeying the Log-Normal distribution, i.e., $\xi \sim \mathcal { N } \left( \mu , \sigma ^ { 2 } \right)$ dB with the expectation of $\mu = 8$ and the standard deviation of $\sigma = 4$ The phases are assumed to be random variables obeying the uniform distribution, i.e., $\phi _ { k } ^ { ( \delta , \eta ) } \sim \mathcal { U } \left( 0 , 2 \pi \right)$ . To guarantee the fairness, we also incorporate the double SP configuration (denoted as “Double SP”). Specifically, we set the number of RF chains as ${ \tilde { R } } = 2 R = 1 2 8$ , the number of antennas located in horizontal direction as ${ \tilde { P } } ~ = ~ 2 P ~ = ~ 3 2$ in this configuration. Fig. 10 illustrates that DP configuration achieves higher positioning accuracy than the SP configuration, since the DP configuration provides more abundant amount of samples for the parameter estimation. However, the double SP configuration achieves even higher positioning accuracy than the DP configuration due to the enhanced AoA estimation achieved by more sufficient array manifold information and reduced cumulative error. Nevertheless, the employment of dual polarization is still promising, since it reduces the antenna deployment area compared to the double SP configuration.

![](images/e9bbb0ae273e2fb46e2c7105939d081c70405852b12d393b1a6dfab8b39453d6.jpg)

Fig. 11. The CPU time of the monostatic parameter estimation.  
![](images/6b36ab1616983e2067b909925940b10abaf1f0f491fbd0bbd7a79036ca061ff3.jpg)  
Fig. 12. The CPU time of the multi-BS data association.

Fig. 11 depicts the central processing unit (CPU) time of the monostatic parameter estimation versus the number of UAVs. It can be observed that the proposed tensor decomposition-based scheme is more efficient than Benchmark1. The reason lies in the fact that the MUSIC algorithm requires the 2-D search on (θ, ϕ) for the AoA estimation, whereas for the tensor decomposition scheme, the proposed GRQ-based AoA estimation algorithm can effectively reduce the computational complexity. In addition, we also find that with increased K, the CPU time for both two schemes increases as more calculations are required to derive the parameters.

## C. Cooperative Position and Velocity Estimation

Fig. 12 illustrates the efficiency of the proposed multi-BS data association algorithm. It can be observed that with a small number of UAVs, the CPU time of the proposed algorithm exceeds that of the exhaustive permutation scheme. This is because, in addition to deriving the MST of the updated graph G<sup>˜</sup>, the proposed algorithm needs additional procedures to calculate the distances between the positioning results of each BS and those of other BSs to recognize and remove the false detection results to enhance the cooperative sensing scheme.

![](images/ff54dc93d9103269e445b8ea1d7a5067134fd10642f0418af84157f3d3e91614.jpg)  
(a) Position

![](images/a70f22501dcfc22920a3435c6b384a6befdd1acc2c4ea188fd0436f6301ef094.jpg)  
(b) True velocity  
Fig. 13. Estimation RMSE vs. the number of BSs.

Moreover, as the number of UAVs increases, the computational complexity of the exhaustive permutation method rises sharply, while the CPU time of the proposed algorithm increases slowly, which allows the algorithm to perform well even when there are many UAVs.

Fig. 13(a) depicts the cooperative position estimation RMSE versus the number of BSs with the weighting intensity factor of $\beta _ { 1 } ~ = ~ 0 . 5 .$ As previously outlined, the proposed strategy for selecting the lattice point from the Pareto set is contingent upon the system configuration and the precision of AoA and range estimation. Specifically, for the tensor decomposition scheme, noting that we assign 612 subcarriers but only 384 antennas (with HBF structure) to each BS. In addition, the AoA estimation will also be degraded by the cumulative error effect, which makes the estimation of range more precise than AoA. Thus, we choose the lattice point from the Pareto set according to (78). From Fig. 13(a), we make the following observations: First, we observe that the increase of BSs leads to a continuous improvement in cooperative positioning accuracy, which is significantly higher than the monostatic positioning results (i.e., K = 1). This is attributed to the fact that more BSs provide richer UAVs parameter estimations, i.e., the AoAs and range estimations for the data fusion. Furthermore, it also can be observed that the proposed Pareto optimality scheme further reduces the positioning error compared to the mean fusion scheme. This is because it takes the AoA and range estimations into account with a finer granularity, rather than merely fuse the final positioning results. In addition, it also allocates distinct weights to the BSs according to the ranges between them and the UAVs, making the more accurate estimations more dominant in the fusion process.

Fig. 13(b) shows the cooperative velocity estimation RMSE versus the number of BSs with the weighting intensity factor of $\beta _ { 2 } = 0 . 5 $ . Similarly, it can be observed again from Fig. 13(b) that the velocity estimation error decreases as the number of BSs increases. This is because more BSs provide more information about the radial velocities and AoAs. Furthermore, the proposed residual weighting-based scheme further facilitates the velocity estimation compared to the WLS method due to the suppression of estimation errors.

## D. Performance Evaluation in The Degraded Scenario

To further evaluate the versatility and generality of the proposed sensing scheme, we degrade it to the single-antenna single-target scenario and compare its performance with the state-of-the-art cooperative sensing scheme proposed in [14] (denoted as “Benchmark2”). In the degraded scenario, the following adjustments are performed:

![](images/2fe0d413ab12a0d4093b29af98da11e9d68cba4f631e2b8a3aabaef8c0c2202e.jpg)  
(a) Range

![](images/dab36e70da7f5146821b15aee6decee5809efe9f20b7b9d1fad7d0c5dbe0eead.jpg)  
(b) Radial velocity

![](images/6ada1710572a1d4d98c571c8ce8f1696dcde747c78da6e162fec8dc7a4d9d5d4.jpg)  
(c) Position

![](images/9c9d1484e05e2fd98d76e4af102b58aa9631b6e03f95e0901b317d9fbca56165.jpg)  
(d) True velocity  
Fig. 14. Estimation RMSE vs. the transmit power budget in the degraded scenario.

1) The parameter estimation problem formulated in (30) degenerates into a second-order tensor decomposition model, while the Vandermonde property of the factor matrix can still be utilized to recover the factor matrices and estimate the UAV’s range and radial velocity via the similar procedures provided in Section IV.

2) Without AoA estimation, the rough estimation of the UAV’s position is derived by the LS method [14].

3) Without AoA estimation, the determination of the final position estimation from the lattice points union should only take the minimization of the range loss function into consideration, i.e., (78).

Fig. 14 illustrates the sensing performance of the proposed scheme and of Benchmark2. It should be noted that in the considered single-antenna setup, due to the severe path loss and the limited antenna gain, it is hard to achieve sufficient received SNR to meet the UAV detection and parameter estimation requirements, especially when the UAV is far from the BSs. Thus, in this simulation, we adjust the simulation parameters as $r _ { 1 } = 1 0 0 ~ \mathrm { m } , r _ { 2 } = 1 2 5$ m. In addition, for ease of algorithm implementation, we assume that the UAV and the BSs are situated on the same horizontal plane, and its velocity component in the z-axis is set to zero. From Fig. 14, we find that the proposed scheme demonstrates performance gains in range and position estimation compared to Benchmark2, due to its off-grid approach to directly derive the range estimation relying on the Vandermonde structure of the factor matrix. In terms of radial velocity estimation, the proposed scheme slightly performs worse than Benchmark2, attributed to the cumulative effect of errors, since the radial velocity estimation is affected by the previous range estimation. However, due to the superior position estimation, the proposed solution still achieves comparable performance in true velocity estimation.

Fig. 15 shows the relationship between the estimation RMSE of the cooperative position and true velocity with respect to the number of BSs. As depicted in Fig. 15, the proposed fusion scheme achieves superior position estimation performance compared to the fusion scheme proposed in Benchmark2, while achieving comparable performance in velocity estimation. The results effectively validate the superiority and generality of the proposed fusion scheme. In addition, as previously discussed, the proposed fusion method is applicable for the more general multi-antenna and multi-target scenarios, thereby further highlighting its versatility and potential for broader applications.

![](images/f668361d9ae246c2453473540b6891bd954b8119618e50db2ef505c775702388.jpg)  
(a) Position

![](images/bcde70269c06e9c3d1d612580ea2dcecfb9ff86e17b8eff258a618b6b1d0f7ec.jpg)  
(b) True velocity  
Fig. 15. Estimation RMSE vs. the number of BSs in the degraded scenario.

## VIII. CONCLUSION

In this paper, we proposed a comprehensive cooperative ISAC scheme for low-altitude sensing scenario that includes the monostatic parameter estimation, multi-BS data association, and multi-BS cooperative sensing. Specifically, we first provided preliminary steps for the sensing scheme and formulated the monostatic parameter estimation problem via using a tensor decomposition model to estimate the UAVs’ parameters. Then, a false removing MST-based data association method was developed to accurately match the multiple BSs’ estimations to the same UAV. Subsequently, we proposed a Pareto optimality method and a residual weighting scheme to improve the position and velocity estimation, respectively. Additionally, we also extended our approach to the dual-polarized system. Simulation results demonstrated the superiority of proposed schemes in terms of generality and estimation accuracy to the conventional techniques.

## REFERENCES

[1] Q. Wu et al., “A comprehensive overview on 5G-and-beyond networks with UAVs: From communications to sensing and intelligence,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 2912–2945, Oct. 2021.

[2] F. Liu et al., “Integrated sensing and communications: Toward dualfunctional wireless networks for 6G and beyond,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1728–1767, Jun. 2022.

[3] S. Lu, F. Liu, and L. Hanzo, “The degrees-of-freedom in monostatic ISAC channels: NLoS exploitation vs. reduction,” IEEE Trans. Veh. Technol., vol. 72, no. 2, pp. 2643–2648, Feb. 2023.

[4] L. Pucci, E. Paolini, and A. Giorgetti, “System-level analysis of joint sensing and communication based on 5G new radio,” IEEE J. Sel. Areas Commun., vol. 40, no. 7, pp. 2043–2055, Jul. 2022.

[5] C. Cui, J. Xu, R. Gui, W.-Q. Wang, and W. Wu, “Search-free DOD, DOA and range estimation for bistatic FDA-MIMO radar,” IEEE Access, vol. 6, pp. 15431–15445, 2018.

[6] L. Leyva, D. Castanheira, A. Silva, and A. Gameiro, “Two-stage estimation algorithm based on interleaved OFDM for a cooperative bistatic ISAC scenario,” in Proc. IEEE 95th Veh. Technol. Conf. s(VTC-Spring), Jun. 2022, pp. 1–6.

[7] Z. Han et al., “Cellular network based multistatic integrated sensing and communication systems,” IET Commun., vol. 18, no. 20, pp. 1878–1888, Dec. 2024.

[8] Z. Han et al., “Multistatic integrated sensing and communication system in cellular networks,” in Proc. IEEE Globecom Workshops (GC Wkshps), Dec. 2023, pp. 123–128.

[9] G. Li, S. Wang, K. Ye, M. Wen, D. W. K. Ng, and M. Di Renzo, “Multi-point integrated sensing and communication: Fusion model and functionality selection,” IEEE Wireless Commun. Lett., vol. 11, no. 12, pp. 2660–2664, Dec. 2022.

[10] P. Gao, L. Lian, and J. Yu, “Cooperative ISAC with direct localization and rate-splitting multiple access communication: A Pareto optimization framework,” IEEE J. Sel. Areas Commun., vol. 41, no. 5, pp. 1496–1515, May 2023.

[11] Y. Cao and Q.-Y. Yu, “Joint resource allocation for user-centric cell-free integrated sensing and communication systems,” IEEE Commun. Lett., vol. 27, no. 9, pp. 2338–2342, Sep. 2023.

[12] Q. Shi, L. Liu, S. Zhang, and S. Cui, “Device-free sensing in OFDM cellular network,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1838–1853, Jun. 2022.

[13] Z. Zhang et al., “Target localization in cooperative ISAC systems: A scheme based on 5G NR OFDM signals,” IEEE Trans. Commun., early access, Oct. 28, 2024, doi: 10.1109/TCOMM.2024.3486981.

[14] Z. Wei et al., “Symbol-level integrated sensing and communication enabled multiple base stations cooperative sensing,” IEEE Trans. Veh. Technol., vol. 73, no. 1, pp. 724–738, Jan. 2024.

[15] X. Lu, Z. Wei, R. Xu, L. Wang, B. Lu, and J. Piao, “Integrated sensing and communication enabled multiple base stations cooperative UAV detection,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC Workshops), Jun. 2024, pp. 1882–1887.

[16] Z. Zhou, J. Fang, L. Yang, H. Li, Z. Chen, and R. S. Blum, “Lowrank tensor decomposition-aided channel estimation for millimeter wave MIMO-OFDM systems,” IEEE J. Sel. Areas Commun., vol. 35, no. 7, pp. 1524–1538, Jul. 2017.

[17] Y. Lin, S. Jin, M. Matthaiou, and X. You, “Tensor-based channel estimation for millimeter wave MIMO-OFDM with dual-wideband effects,” IEEE Trans. Commun., vol. 68, no. 7, pp. 4218–4232, Jul. 2020.

[18] R. Wang, H. Ren, C. Pan, G. Zhou, R. Weng, and J. Wang, “Channel estimation for mmWave MIMO-OFDM systems in high-mobility scenarios: Instantaneous model or statistical model?” 2024, arXiv:2403.02942.

[19] R. Zhang et al., “Integrated sensing and communication with massive MIMO: A unified tensor approach for channel and target parameter estimation,” IEEE Trans. Wireless Commun., vol. 23, no. 8, pp. 8571–8587, Aug. 2024.

[20] H. Zhu and J. Wang, “Chunk-based resource allocation in OFDMA systems—Part I: Chunk allocation,” IEEE Trans. Commun., vol. 57, no. 9, pp. 2734–2744, Sep. 2009.

[21] H. Zhu and J. Wang, “Chunk-based resource allocation in OFDMA systems—Part II: Joint chunk, power and bit allocation,” IEEE Trans. Commun., vol. 60, no. 2, pp. 499–509, Feb. 2012.

[22] Y. Cui, X. Jing, and J. Mu, “Integrated sensing and communications via 5G NR waveform: Performance analysis,” in Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP), May 2022, pp. 8747–8751.

[23] F. Liu and C. Masouros, “A tutorial on joint radar and communication transmission for vehicular networks—Part I: Background and fundamentals,” IEEE Commun. Lett., vol. 25, no. 2, pp. 322–326, Feb. 2021.

[24] S. M. Kay, Fundamentals of Statistical Signal Processing. Upper Saddle River, NJ, USA: Prentice-Hall, 1998.

[25] M. Wax and T. Kailath, “Detection of signals by information theoretic criteria,” IEEE Trans. Acoust., Speech, Signal Process., vol. ASSP-33, no. 2, pp. 387–392, Apr. 1985.

[26] T. G. Kolda and B. W. Bader, “Tensor decompositions and applications,” SIAM Rev. Soc. Ind. Appl. Math., vol. 51, no. 3, pp. 455–500, Aug. 2009, doi: 10.1137/07070111X.

[27] X. Zhang, Matrix Analysis and Applications. Beijing, China: Tsinghua Univ. Press, 2004.

[28] M. Sørensen and L. De Lathauwer, “Blind signal separation via tensor decomposition with Vandermonde factor: Canonical polyadic decomposition,” IEEE Trans. Signal Process., vol. 61, no. 22, pp. 5507–5519, Nov. 2013.

[29] J. B. Kruskal, “Three-way arrays: Rank and uniqueness of trilinear decompositions, with application to arithmetic complexity and statistics,” Linear Algebra Appl., vol. 18, no. 2, pp. 95–138, 1977. [Online]. Available: https://www.sciencedirect.com/science/ article/pii/0024379577900696

[30] X. Zhang, F. Wang, and H. Li, “An efficient method for cooperative multi-target localization in automotive radar,” IEEE Signal Process. Lett., vol. 29, pp. 16–20, 2022.

[31] R. C. Prim, “Shortest connection networks and some generalizations,” Bell Syst. Tech. J., vol. 36, no. 6, pp. 1389–1401, Nov. 1957.

[32] J. B. Kruskal Jr., “On the shortest spanning subtree of a graph and the traveling salesman problem,” Proc. Amer. Math. Soc., vol. 7, no. 1, pp. 48–50, Feb. 1956.

[33] P.-C. Chen, “A non-line-of-sight error mitigation algorithm in location estimation,” in Proc. IEEE Wireless Commun. Netw. Conf., Sep. 1999, pp. 316–3201.

[34] J. Xing, J. Zhang, L. Jiao, X. Zhang, and C. Zhao, “A robust wireless sensor network localization algorithm in NLOS environment,” in Proc IEEE Int. Conf. Control Autom., May 2007, pp. 3244–3249.

[35] C. Qian, X. Fu, N. D. Sidiropoulos, and Y. Yang, “Tensor-based channel estimation for dual-polarized massive MIMO systems,” IEEE Trans. Signal Process., vol. 66, no. 24, pp. 6390–6403, Dec. 2018.

[36] G. H. Golub, A. Hoffman, and G. W. Stewart, “A generalization of the Eckart-Young-Mirsky matrix approximation theorem,” Linear Algebra its Appl., vols. 88–89, pp. 317–327, Apr. 1987. [Online]. Available: https://www.sciencedirect.com/science/article/pii/0024379587901145

[37] 5G; NR; User Equipment (UE) Radio Transmission and Reception; Part 1: Range 1 Stand Alone, Standard TS 38.101, 3GPP, Jul. 2023.

[38] Calculation of Free-space Attenuation, document P.524-4, ITU, Aug. 2019.

[39] P. Stoica and A. Nehorai, “MUSIC, maximum likelihood, and Cramer– rao bound,” IEEE Trans. Acoust., Speech, Signal Process., vol. 37, no. 5, pp. 720–741, May 1989.

[40] Study on Channel Model for Frequencies From 0.5 to 100 GHz, document TS 38.901, 3GPP, Dec. 2023.

![](images/d8e1b3e4353435ebb9bedc6de6cf9e4a4a659109b1b5f3c5b459e24e2d7c8adb.jpg)  
Jun Tang received the B.S. degree in communication engineering from Ningbo University, Ningbo, China, in 2024. He is currently pursuing the M.S. degree with the School of Information Science and Engineering, Southeast University, China. His research interests include integrated sensing and communication (ISAC), parameter estimation, and convex optimization.

![](images/e9f03acefd54bcbd7d1a82cdbecfb09220ba7efe45541e51d7e5ebd53eae1053.jpg)  
Yiming Yu is currently a full-time Senior Research Officer with China Mobile Group Design Institute Company Ltd. His research interests include integrated sensing and communications (ISAC), reconfigurable intelligent surfaces (RIS), and 5G/6G spectrum.

![](images/375c365a8f7af1e2e0acec2449bf8730ca1d105373a702e52883bcd591301039.jpg)

Cunhua Pan (Senior Member, IEEE) is currently a Full Professor with Southeast University. His research interests include reconfigurable intelligent surfaces (RIS), AI for wireless, near field communications and sensing, and integrated sensing and communications. He has published over 200 IEEE journal articles. His articles got over 19 000 Google Scholar citations with H-index of 70. He is a Clarivate Highly Cited Researcher. He received the IEEE ComSoc Leonard G. Abraham Prize in 2022, IEEE ComSoc Asia–Pacific Outstanding

Young Researcher Award in 2022, IEEE ComSoc Fred W. Ellersick Prize in 2024, IEEE ComSoc CTTC Early Achievement Award in 2024, IEEE ComSoc SPCC Early Achievement Award in 2024, and IEEE WCSP 2022 Best Paper Award. He supervised one Ph.D. student to win the IEEE Signal Processing Society Best Ph.D. Dissertation Award. He is/was an Editor of IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, IEEE WIRELESS COMMUNICATION LETTERS, and IEEE COMMUNICATIONS LETTERS. He serves as a (leading) Guest Editor for IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, IEEE JOURNAL OF SELECTED TOPICS IN SIGNAL PROCESSING, IEEE INTERNET OF THINGS JOURNAL, IEEE Vehicular Technology Magazine, IEEE Internet of Things Magazine, and IEEE TRANSACTIONS ON GREEN COMMUNICATIONS AND NETWORKING.

![](images/8d8e5c4fcd9fab6415c7e0e562c2ee8d2763c88d16f80b20a96a27a1349bbe16.jpg)

Hong Ren (Member, IEEE) received the B.S. degree from the School of Information Science and Engineering, Southwest Jiaotong University, Chengdu, China, in 2011, and the M.S. and Ph.D. degrees from Southeast University, Nanjing, China, in 2014 and 2018, respectively. From 2016 to 2018, she was a Visiting Student with the University of Southampton, U.K., and from 2018 to 2020, a Post-Doctoral Scholar with the Queen Mary University of London, U.K. She is currently an Associate Professor with Southeast University. Her research interests include

communication and signal processing, cooperative ISAC, AI, and URLLC. She is currently an Editor of IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY and IEEE WIRELESS COMMUNICATION LETTERS. She was recognized as a Clarivate Highly Cited Researcher in 2024. She was a recipient of the 2024 IEEE Communications Society Fred W. Ellersick Prize and the 2022 IEEE Communications Society Leonard G. Abraham Prize.

![](images/1b83fe52da7f370f80f4ffad027c0421795b144b8695db7b87b1f9591a796d46.jpg)

Dongming Wang received the B.S. degree from Chongqing University of Posts and Telecommunications in 1999, the M.S. degree from Nanjing University of Posts and Telecommunications in 2002, and the Ph.D. degree from Southeast University, China, in 2006. He joined the National Mobile Communications Research Laboratory, Southeast University, in 2006, where he is currently a Professor. His research interests include signal processing for wireless communications and large-scale distributed MIMO systems (cell-free massive MIMO).

He served as the Symposium Co-Chair for the 2015 IEEE International Conference on Communications (ICC 2015) and the IEEE Wireless Communications and Signal Processing Conference (IEEE WCSP 2017). He served as an Associate Editor for Science China Information Sciences from 2018 to 2022.

![](images/847e62ba59ab12edb10afd6c4f72b3bd9bdd5396ea5f2602ef297a8beb6f36d5.jpg)

Jiangzhou Wang (Fellow, IEEE) is currently a Professor with Southeast University, China, and an Emeritus Professor with the University of Kent, U.K. He has published more than 500 articles and five books. His research interests are mobile communications. He was a recipient of the 2024 IEEE Communications Society Fred W. Ellersick Prize and the 2022 IEEE Communications Society Leonard G. Abraham Prize. He was the Technical Program Chair of the 2019 IEEE International Conference on Communications (ICC2019), Shanghai, the Execu-

tive Chair of the IEEE ICC2015, London, and the Technical Program Chair of the IEEE WCNC2013. He is an International Member of Chinese Academy of Engineering (CAE), a fellow of the Royal Academy of Engineering (R.A.Eng.), U.K., and a fellow of the IET.

![](images/aa2d24918c45ae443050b938295c12c1eb546d5d21d70b2ad53dd786916111a6.jpg)

Xiaohu You (Fellow, IEEE) received the master’s and Ph.D. degrees in electrical engineering from Southeast University, Nanjing, China, in 1985 and 1988, respectively. Since 1990, he has been with the National Mobile Communications Research Laboratory, Southeast University, where he holds the rank of the Director and a Principal Professor. He is currently the Director and the Chief Scientist of the Purple Mountain Laboratory and the Deputy Director of the Peng Cheng Laboratory. His research interests include broadband wireless transmission

and mobile communication systems and advanced signal processing and its applications. He has contributed over 300 IEEE journal articles and three books in mobile communications. From 1999 to 2018, he was the Principal Expert of the 3G, 4G, and 5G Research Projects of China National 863 Program. Currently, he is a Leading Expert of China’s 6G Task Force Research Project supported by Ministry of Science and Technology of China. He served as the General Chair for IEEE WCNC 2013, IEEE VTC 2016 Spring, and IEEE ICC 2019. He won the Chan Kah Kee Science Award in 2014 and IET Achievement Medal in 2021. He was awarded as an Academician of China Academy of Science in 2023.