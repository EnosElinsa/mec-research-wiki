# Diffusion-Based Dynamic Contract for Federated AI Agent Construction in Mobile Metaverses

Jinbo Wen , Graduate Student Member, IEEE, Jiawen Kang , Senior Member, IEEE, Yang Zhang , Yue Zhong , Dusit Niyato , Fellow, IEEE, Jie Xu , Fellow, IEEE, Jianhang Tang , Member, IEEE, and Chau Yuen , Fellow, IEEE

Abstract—Mobile metaverses are envisioned as a transformative digital ecosystem that delivers immersive, intelligent, and ubiquitous services through mobile devices. Driven by Large Language Models (LLMs) and Vision-Language Models (VLMs), Artificial Intelligence (AI) agents hold the potential to empower the creation, maintenance, and evolution of mobile metaverses, enabling seamless human-machine interaction and dynamic service adaptation. Currently, AI agents are primarily built upon cloud-based LLMs and VLMs. However, several challenges hinder their efficient deployment, including high service latency and a risk of sensitive data leakage during perception and processing. In this paper, we develop an edge-cloud collaboration-based federated AI agent construction framework in mobile metaverses. Specifically, Edge Servers (ESs), as agent infrastructures, first create agent modules in a distributed manner. The cloud server then integrates these modules into AI

Received 8 August 2025; revised 7 January 2026; accepted 13 February 2026. Date of publication 17 February 2026; date of current version 12 June 2026. This work was supported in part by the National Natural Science Foundation of China (NSFC) under Grant 62572132, Grant U2333202, Grant U22A2054, Grant 62471424, Grant 92267202, and Grant U25A20390, in part by the Guangdong Provincial Natural Science Foundation General Program under Grant 2025A1515010137, in part by the Guangdong Basic and Applied Basic Research Foundation under Grant 2023A1515140137, in part by the Guizhou Provincial Science and Technology Plan Project under Grant QKHRC-KJZY[2025]021 and Grant QKHPT-KXJZ[2025]003, in part by the Shenzhen Fundamental Research Program under Grant JCYJ20250604141209012. This research was also supported by the Seatrium New Energy Laboratory, Singapore Ministry of Education (MOE) Tier 1 under Grant RT5/23 and RG24/24, in part by the Nanyang Technological University (NTU) Centre for Computational Technologies in Finance (NTU-CCTF), and in part by the Research Innovation and Enterprise (RIE), 2025 Industry Alignment Fund-Industry Collaboration Projects (IAF-ICP) under Grant I2301E0026, administered by the Agency for Science, Technology and Research (A\*STAR). (Corresponding author: Yang Zhang.)

Jinbo Wen and Yang Zhang are with the College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing 211106, China (e-mail: jinbo1608@nuaa.edu.cn; yangzhang@nuaa.edu.cn).

Jiawen Kang and Yue Zhong are with the School of Automation, Guangdong University of Technology, Guangzhou 510006, China (e-mail: kavinkang@gdut.edu.cn; 2112404106@mail2.gdut.edu.cn).

Dusit Niyato is with the College of Computing and Data Science, Nanyang Technological University, Singapore 639798 (e-mail: dniyato@ntu.edu.sg).

Jie Xu is with the School of Science and Engineering (SSE), Shenzhen Future Network of Intelligence Institute (FNii-Shenzhen), Shenzhen 518172, China, and also with the Guangdong Provincial Key Laboratory of Future Networks of Intelligence, Chinese University of Hong Kong, Hong Kong (e-mail: xujie@cuhk.edu.cn).

Jianhang Tang is with the State Key Laboratory of Public Big Data, Guizhou University, Guiyang 550025, China (e-mail: jhtang@gzu.edu.cn).

Chau Yuen is with the School of Electrical and Electronics Engineering, Nanyang Technological University, Singapore 639798 (e-mail: chau.yuen@ntu.edu.sg).

This article has supplementary downloadable material available at https://doi.org/10.1109/TSC.2026.3665640, provided by the authors.

Digital Object Identifier 10.1109/TSC.2026.3665640 agents and deploys them at the edge, thereby enabling low-latency AI agent services for users. Considering that ESs may exhibit dynamic levels of willingness to participate in federated AI agent construction, we design a two-period dynamic contract model to continuously incentivize ESs to participate in agent module creation, effectively addressing the dynamic information asymmetry between the cloud server and ESs. Furthermore, we propose an Enhanced Diffusion Model-based Soft Actor-Critic (EDMSAC) algorithm to effectively generate optimal dynamic contracts. In the algorithm, we apply dynamic structured pruning to DM-based actor networks to enhance denoising efficiency and policy learning performance. Simulation results demonstrate that the EDMSAC algorithm outperforms the DMSAC algorithm by up to 23% in optimal dynamic contract generation.

Index Terms—Mobile metaverses, AI agent construction, dynamic contract theory, enhanced diffusion models, deep reinforcement learning.

## I. INTRODUCTION

W ITH the advancement of extended reality, GenerativeArtificial Intelligence (GenAI), and wireless commu- Artificial Intelligence (GenAI),and wireless communication technologies, mobile metaverses are emerging as a transformative digital ecosystem [1]. Positioned as a cornerstone of the next-generation Internet, mobile metaverses have attracted significant attention from both academia and industry due to their robust levels of connectivity, enabling users to interact in real time with immersive and interconnected virtual spaces through mobile devices [2]. Furthermore, mobile metaverses hold the potential to revolutionize various fields, such as healthcare, education, and entertainment [2]. However, the development of mobile metaverses faces several technical challenges. Firstly, conventional content creation methods often involve time-consuming and resource-intensive processes, leading to static virtual content that fails to dynamically adapt to real-time user interactions or environmental variations [3]. Secondly, the inherent limitations of mobile input modalities, such as touchscreen gestures and voice commands, would inevitably degrade the fluidity of immersive interactions.

GenAI is driving the evolution of the metaverse due to its incredible ability to generate novel content [4]. As an advanced paradigm of GenAI, AI agents are expected to play a pivotal role in the creation, maintenance, and evolution of mobile metaverses. Empowered by Large Language Models (LLMs) and Vision-Language Models (VLMs) [5], AI agents are artificial entities comprising four core modules: perception, memory, decision-making, and action. With these modules, AI

1939-1374 © 2026 IEEE. All rights reserved, including rights for text and data mining, and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

agents are capable of perceiving surrounding environments, processing and storing information, formulating strategies, and executing tasks to achieve specific objectives [6]. Within mobile metaverses, AI agents can improve immersion by dynamically generating and adapting virtual content, as well as creating realistic avatars and environments using Digital Twin (DT) and three-dimensional rendering technologies [5]. Moreover, they can deliver personalized and interactive user experiences by acting as intelligent and personalized assistants, guiding users through virtual environments, and tailoring interactions based on individual preferences.

Currently, AI agent construction often relies on cloud-based LLMs and VLMs, which require transmitting perceived data to remote servers for processing before returning results to users [5], [6]. Although AI agents hold significant promise for enabling mobile metaverses, their efficient implementation is hindered by several critical challenges: 1) The cloud-based AI agent architecture introduces inherent service latency, negatively impacting user experience. For example, latency in processing and rendering real-time location data within augmented reality navigation systems may lead to user disorientation, operational inefficiencies, or even safety hazards in scenarios requiring precise spatial awareness [7]. 2) During peak usage periods, cloud servers may experience performance bottlenecks due to simultaneous service requests from large user bases [8]. Such bottlenecks result in response latency and potential service unavailability under high-load conditions, undermining the seamless interaction demanded by immersive metaverse environments. 3) The transmission of perceived data, which often contains sensitive personal information, remains vulnerable to interception during transmission and susceptible to breaches if stored centrally in cloud repositories [9]. This exposes users to risks such as unauthorized tracking, data misuse, and identity theft, particularly in mobile metaverses where data flows across heterogeneous networks.

Motivated by the feasibility of federated model construction [10], [11], [12], [13], [14], we propose a novel edge-cloud collaboration-based federated AI agent construction framework, where Edge Servers (ESs) with sufficient computing and storage resources serve as agent infrastructures responsible for constructing agent modules in a distributed manner, while the cloud server is responsible for integrating these constructed modules into AI agents and eventually deploys them at the edge. Unlike traditional federated learning, which deals with the same task across participating nodes [15], the agent modules in the federated AI agent construction framework can be heterogeneous, with each module performing distinct functions. Furthermore, whereas federated learning typically aims to jointly train a single global model until convergence [15], the construction of multiple agent modules can be done concurrently. Nonetheless, during the construction of agent modules, ESs exhibit different dynamic levels of Willingness to Participate (WTP) over multiple periods due to various factors [16], such as the high energy consumption of agent module construction and the prioritization of other computing tasks. Moreover, the WTP levels of ESs are typically unknown to the cloud server, leading to the intention of some ESs to free-ride on the efforts of others [16]. To this end, we design a dynamic contract-based incentive mechanism to incentivize ESs to participate sustainably in federated AI agent construction, addressing the challenge of dynamic information asymmetry.

Since dynamic contract design in practical scenarios typically involves changing network conditions [16], conventional optimization techniques that rely on complete prior knowledge of the environment must be frequently redesigned [17], which may not be applicable in practical scenarios. Fortunately, Deep Reinforcement Learning (DRL) algorithms have been widely utilized in dynamic scenarios, which can learn optimal strategies through repeated interactions with the environment [18]. Moreover, Generative Diffusion Models (GDMs) with a robust generative capability have shown a strong potential to improve DRL performance [19], [20], [21], particularly by mitigating the risk of convergence to suboptimal solutions. Therefore, we adopt an enhanced diffusion-based DRL algorithm to identify optimal dynamic contracts. The main contributions of this paper are summarized as follows:

- Federated AI Agent Construction Framework: We propose an edge-cloud collaboration-based federated AI agent construction framework in mobile metaverses. In the proposed framework, ESs serve as agent infrastructures, leveraging their computing, storage, and communication resources to construct agent modules in a distributed manner. The cloud server then integrates these created agent modules into complete AI agents and deploys them at the edge, thereby providing low-latency AI agent services for users in mobile metaverses.  
Dynamic Contract-based Incentive Mechanism: Considering the dynamic WTP levels of ESs in federated AI agent construction, we propose a two-period dynamic contract model to motivate ESs to continuously participate in agent module creation. The self-disclosure property of the proposed model ensures that each ES selects the contract best suited to its WTP level, thereby addressing the problem of dynamic information asymmetry. Notably, the two-period dynamic contract design maintains relatively low computational complexity and thus can be recursively extended to multiple periods.  
Diffusion Models for Dynamic Contract Design: We adopt an Enhanced DM-based Soft Actor-Critic (EDMSAC) algorithm to identify optimal dynamic contracts. Specifically, DM-based actor networks possess both analytical and generative capabilities, which can generate dynamic contract samples through an iterative denoising process. To enhance denoising efficiency, we incorporate dynamic structured pruning techniques into DM-based actor networks, enabling a more efficient and scalable exploration of the optimal dynamic contract policy. To the best of our knowledge, this is the first work to leverage DRL algorithms, especially diffusion-based DRL, for optimal dynamic contract design.  
Extensive Simulations for Performance Evaluation: We utilize LLMs called Qwen-VL1 to construct an AI agent capable of operating mobile phones to perform

TABLE ICOMPARISON BETWEEN THE CURRENT LITERATURE AND THIS PAPER IN OPTIMAL CONTRACT DESIGN

<table><tr><td colspan="2">Literature</td><td>[10]</td><td>[16]</td><td>[17]</td><td>[18]</td><td>[22]</td><td>[23]</td><td>[24]</td><td>[25]</td><td>[26]</td><td>[27]</td><td>[28]</td><td>[29]</td><td>Our Paper</td></tr><tr><td rowspan="3">Properties</td><td>Individual Rationality</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Incentive Compatibility</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Intertemporal Consistency</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td><td>√</td></tr><tr><td rowspan="3">Solutions</td><td>Deep Reinforcement Learning</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Diffusion Models</td><td></td><td></td><td>√</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Enhanced Diffusion Models</td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td></tr></table>

simple tasks. Specifically, we leverage Qwen-VL-Plus to create a perception module and Qwen-VL-Max to create decision-making, reflection, and planning modules. This construction process can be extended to the proposed framework. We then compare the EDMSAC algorithm with two DM-based DRL algorithms and three representative DRL benchmark algorithms. Simulation results demonstrate that the EDMSAC algorithm can achieve up to a 23% improvement over the DMSAC algorithm [20] in optimal dynamic contract generation.

The remainder of the paper is organized as follows: Section II reviews the related work, where Table I summarizes the comparison of the current literature and this paper in optimal contract design. Section III introduces the edge-cloud collaboration-based federated AI agent construction framework. In Section IV, we propose the two-period dynamic contract model to motivate ESs to continuously participate in federated AI agent construction. Section V presents the EDMSAC algorithm for generating optimal dynamic contracts. In Section VI, we provide extensive simulation results to demonstrate the feasibility and effectiveness of the proposed framework and algorithm. Section VII concludes the paper.

## II. RELATED WORK

## A. Federated Model Construction

Federated Learning (FL) is a distributed Machine Learning (ML) framework that enables collaborative model training while preserving data privacy through secure aggregation, making it particularly suitable for applications with stringent privacy requirements [30]. Recent research has highlighted the effectiveness and potential of FL in constructing DT and ML models, particularly in enhancing privacy protection and optimizing resource utilization [10], [11], [12], [13], [14]. For instance, the authors in [11] combined FL with DT technology and introduced a trust mechanism to optimize the learning process. Similarly, the authors in [12] leveraged FL to optimize DT-enabled industrial Internet of Things systems. In [13], the authors proposed an FL architecture based on over-the-air computing, enabling the efficient and secure development of DT models. In [14], the authors proposed a generalized federated Reinforcement Learning (RL) framework that incorporates meta-learning techniques, which enables the fusion of RL models trained across multiple intelligent devices into a unified and generalizable model.

Combined with a device-edge-cloud collaborative computing architecture, FL can facilitate efficient model training by enabling small-scale learning on devices while leveraging the cloud for large-scale model updates. This decentralized approach minimizes network dependency, significantly enhancing the responsiveness and operational stability of AI agents and making it a promising solution for AI agent model construction. To the best of our knowledge, there is currently no existing study on the construction of AI agents in wireless mobile environments. Motivated by the aforementioned studies, we aim to develop a novel federated AI agent construction framework, exploring the feasibility and potential of mobile AI agents in wireless networks.

![](images/2f4d7a78bbf76e1097f0ef5f566572b10b8e6d952d0cf901c9249894a82f7aa9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Perception"] --> B["Embedding Models"]
  B --> C["Modality encoder"]
  C --> D["Word embedding layer"]
  E["Integrate created agent modules"] --> F["Cloud Server"]
  G["Action"] --> H["Text"]
  G --> I["Tools"]
  G --> J["Call API"]
  G --> K["Embodiment"]
  L["Edge Server"] --> M["LLMs"]
  L --> N["VLMs"]
  O["Construct agent modules"] --> P["Agent module"]
  Q["User Layer"] --> R["Provide AI agent services (e.g., personal assistants)"]
  S["Send the initial configuration requirements of agent modules"] --> T["Cloud Server"]
  U["Upload created agent modules"] --> V["LLMs"]
  W["Edge Layer"] --> X["User Layer"]
```
</details>

Fig. 1. The proposed edge-cloud collaboration-based federated AI agent construction framework. Note that the interface of personal assistants is from the OmAgent application [35] downloaded by our Android phone.

## B. Contract Theory-Based Wireless Applications

Contract theory is an economic tool that examines cooperation in settings with incomplete information and designs incentives for agents to participate in tasks involving asymmetric information [22]. In the context of FL, the authors in [23] proposed an incentive contract tailored for scenarios with strong information asymmetry, leveraging an iteration algorithm to determine optimal contract elements. In [24], the authors utilized contract theory to motivate privately owned vehicles to contribute their onboard computing resources. Traditional contracts are generally one-dimensional, accounting for a static type of information asymmetry between the two parties involved [25]. Therefore, there is a growing interest in multi-dimensional and dynamic contracts that account for multiple asymmetries and evolving conditions.

As for the applications of multi-dimensional contracts [26], [27], the authors in [26] developed a multi-dimensional contract model to optimize the data rewarding design in mobile networks under asymmetric information. In [27], the authors constructed a multi-dimensional contract theory-based framework, incorporating Prospect Theory (PT) and GDM-based DRL algorithms to optimize the dynamic migration of embodied AI twins in vehicular embodied AI networks. As for the applications of dynamic contracts [16], [25], the authors in [16] proposed a two-period contract-based incentive mechanism to motivate users to participate in FL training under dynamic information asymmetry. In [25], the authors proposed a dynamic contract-based incentive mechanism to motivate vehicles to share their threat data for LLM fine-tuning. Inspired by the above works, we propose a dynamic contract-based incentive mechanism to motivate ESs to continuously participate in AI agent construction.

## C. Deep Reinforcement Learning for Contract Design

RL algorithms have been extensively used to identify optimization strategies [31], [32], including optimal static contract design [18], [28], [29]. For instance, the authors in [28] employed Proximal Policy Optimization (PPO) algorithms to identify optimal contracts, incentivizing mobile devices to share data in mobile AI-Generated Content (AIGC) networks. In [29], the authors utilized the twin-delayed Deep Deterministic Policy Gradient (DDPG) algorithm to determine the incentive reward policy. Nevertheless, traditional DRL algorithms often struggle to directly identify optimal contracts due to the complex Individual Rationality (IR) and Incentive Compatibility (IC) constraints. Fortunately, GDMs excel at capturing high-dimensional information in dynamic and complicated network optimization scenarios [19]. Several studies have explored the use of GDMs for optimal static contract design [17], [22], [27]. For example, the authors in [22] proposed a GDM-based DRL algorithm to generate optimal contracts under PT, addressing the problem of information asymmetry in edge AIGC service provision. However, existing studies still rely on heuristic algorithms for optimal dynamic contract design [16], [25], which may not be practical in real scenarios. To fill this gap, we propose the EDMSAC algorithm to identify optimal dynamic contracts.

## III. EDGE-CLOUD COLLABORATION-BASED FEDERATED AI AGENT CONSTRUCTION FRAMEWORK

In this section, we first introduce the proposed framework for constructing AI agents through edge-cloud collaboration. Then, we present the model quality and energy consumption for federated AI agent construction. Finally, we formulate the utilities of ESs and the cloud server, respectively.

## A. Framework Design

For federated AI agent construction, we consider a central cloud server and a set of geographically distributed ESs, which are usually installed in cellular base stations or roadside units [27], denoted by $\mathcal { N } = \{ 1 , \dots , n , \dots , N \}$ . These ESs possess computing, storage, and communication capabilities sufficient to construct, cache, and transmit agent modules [33]. During the AI agent construction period, AI agents can be split into multiple agent modules, such as perception, memory, and action [5], [6], each responsible for specific tasks based on the featured data perceived by ESs.

As shown in Fig. 1, before the beginning of agent module construction, the cloud server transmits the initial configuration requirements of agent modules to the ESs (Step -1 ) [10]. The ESs, serving as agent infrastructures with sufficient resources such as computing, storage, and communication, leverage local LLMs and AI models (e.g., icon detection models) to construct the agent modules in a distributed manner (Step -2 ) [34]. Upon completing the construction, the ESs upload the constructed agent modules to the cloud server (Step -3 ) [10]. Finally, the cloud server creates the complete AI agents by integrating the uploaded agent modules, i.e., connecting and harmonizing these agent modules into a complete agent (Step -4 ) [33]. Once constructed, the AI agents can be deployed at the edge, allowing users to connect to them through the Internet Protocol (IP) address of the current local area network with the ESs [35], facilitating low-latency AI agent services.

## B. Model Quality of Agent Modules

Agent module construction involves fine-tuning pre-trained large models and other AI models to better process downstream tasks [5]. For example, during the perception module construction, ESs are required to fine-tune visual perception models, such as vision transformer models, to extract corresponding semantic representations from visual inputs using samples of feature data. The extracted semantic content is then passed to LLMs for subsequent processing and reasoning. To evaluate the performance of agent module construction, we employ an L-Lipschitz continuous and ε-strongly convex loss function to approximately calculate the model quality of agent modules [33], [36], which is a widely used definition of model accuracy in federated learning [33], [37]. We denote $Q _ { n }$ as the model quality of agent nmodules created by ES n, which is calculated from the number of training rounds $T _ { n }$ that ES n determines to take for creating nagent modules, as given by [37]

$$
Q _ {n} = 1 - 2 ^ {\frac {- T _ {n} (2 - L \delta) \delta \varepsilon}{2}}, \tag {1}
$$

where $\delta \in ( 0 , \frac { 2 } { L } )$ , L, and $\varepsilon$ are pre-defined hyperparame-Lters [33]. Given that the second derivative of $Q _ { n }$ in (1) is calculated as $\begin{array} { r } { \frac { \partial ^ { 2 } Q _ { n } } { \partial ( T _ { n } ) ^ { 2 } } = - \lbrack \frac { ( 2 - L \delta ) \delta \varepsilon } { 2 } \ln 2 \rbrack ^ { 2 } 2 ^ { \frac { - T _ { n } ( 2 - L \delta ) \delta \varepsilon } { 2 } } < 0 , Q _ { n } } \end{array}$ −[ (2−Lδ)δε ln 2]2 ∂ Tnis a convex function with respect to $T _ { n }$ , indicating that there nexists the optimal number of training rounds for ESs to obtain the highest model quality of agent modules.

## C. Energy Consumption of Edge Servers

We represent the total energy consumption of ES n for federated AI agent construction as $E _ { n } ^ { T o t }$ , which consists of the nenergy consumption of perceiving feature data EP er , $E _ { n } ^ { P e r }$ creating agent modules ECre , $\bar { E } _ { n } ^ { C r e }$ n n and uploading created agent modules to $\ddot { E } _ { n } ^ { U p l }$ $\bar { E } _ { n } ^ { P e r }$

$$
E _ {n} ^ {P e r} = \varsigma_ {n} \Upsilon_ {n} ^ {P e r} D _ {n} ^ {F e a} f _ {n} ^ {2}, \tag {2}
$$

where $\varsigma _ { n }$ is a constant related to the hardware architecture of ES $n , \Upsilon _ { n } ^ { P e r }$ (cycles/bit) is the number of Central Processing Unit n(CPU) cycles required for perceiving feature data, $D _ { n } ^ { F e a }$ (bits) is the size of feature data perceived by ES n, and $f _ { n } \left( \mathrm { H z } \right)$ is the CPU speed of ES n.

After perceiving feature data, ES n constructs agent modules under iterative model training to improve the model quality of agent modules, and its energy consumption of creating agent $E _ { n } ^ { C r e }$ is given by [15]

$$
E _ {n} ^ {C r e} = \rho_ {n} T _ {n} \Upsilon_ {n} ^ {C r e} f _ {n} ^ {2}, \tag {3}
$$

where $\rho _ { n }$ represents the effective switched capacitance of ES n nand ΥCre $\boldsymbol { \Upsilon } _ { n } ^ { C r e }$ (cycles/bit) is the number of CPU cycles required for ncreating one bit of agent modules on ES n.

Then, each ES n uploads its constructed agent modules to the cloud server for integration, and the corresponding energy $E _ { n } ^ { U p l }$ is given by [15]

$$
E _ {n} ^ {U p l} = \frac {P _ {n} D _ {n} ^ {A g e n t}}{r _ {n , c}}, \tag {4}
$$

$P _ { n }$ $n , D _ { n } ^ { A g e n t } ( \mathrm { b i t s } )$ n nthe model size of agent modules constructed by ES $n _ { \mathrm { { ; } } }$ , and $r _ { n , c }$ n,c(Mbps) represents the transmission rate from ES n to the cloud server through the fiber link.

Therefore, the total energy consumption of ES n for federated AI agent construction E  i $E _ { n } ^ { T o t }$ s expressed as

$$
E _ {n} ^ {T o t} = \left(\varsigma_ {n} \Upsilon_ {n} ^ {P e r} D _ {n} ^ {F e a} + \rho_ {n} T _ {n} \Upsilon_ {n} ^ {C r e}\right) f _ {n} ^ {2} + \frac {P _ {n} D _ {n} ^ {A g e n t}}{r _ {n , c}}. \tag {5}
$$

## D. Utilities of Edge Servers and the Cloud Server

For ES n, we define the level of WTP in federated AI agent construction as $\theta _ { n } \ [ 1 6 ]$ , which reflects the perception, communnication, and computing capabilities of ES n [17], [18]. The utility of ES n is formulated based on the reward $R _ { n }$ received $E _ { n } ^ { T }$ nfor federated AI agent construction [16], [18], which is given by

$$
u _ {n} = \theta_ {n} R _ {n} - c T _ {n} - E, \tag {6}
$$

where $c = \sigma \rho _ { n } \Upsilon _ { n } ^ { C r e } f _ { n } ^ { 2 }$ and $E = \sigma ( \varsigma _ { n } \Upsilon _ { n } ^ { P e r } D _ { n } ^ { F e a } f _ { n } ^ { 2 } +$ Agent ). $\frac { P _ { n } D _ { n } ^ { A g e n t } } { r _ { n . c } } )$ Dn Here, σ is the unit cost of energy consumption.

rn,cSimilarly, the utility of the cloud server is formulated based on the total profit obtained from all ESs and the cost of energy consumption of global AI agent integration $E _ { C }$ , as given by

$$
U _ {C S} = \sum_ {n = 1} ^ {N} (\alpha Q _ {n} - R _ {n}) - \sigma E _ {C}, \tag {7}
$$

where α represents a scaling factor that affects the overall magnitude of economic benefits [25], and $E _ { C }$ is influenced by Cseveral factors [37], including the latency of global AI agent integration, both CPU and Graphics Processing Unit (GPU) resources on the cloud, and the average number of instructions in integrating agent modules.

Due to high workload and energy consumption, ESs may not always be willing to participate in federated AI agent construction, indicating that ESs have different levels of WTP for federated AI agent construction [16]. The WTP levels of ESs are generally unknown to the cloud server and may change over multiple training rounds [16], which results in dynamic information asymmetry between the cloud server and ESs. Hence, it is necessary to develop a dynamic incentive scheme for ESs to participate in federated AI agent construction.

## IV. DYNAMIC CONTRACT DESIGN

In this section, we propose a two-period dynamic contract model to motivate ESs to continuously participate in federated AI agent construction under dynamic information asymmetry. Note that the proposed dynamic contract model possesses the inherent correlation between two periods within the whole agent construction time and can be feasibly extended to accommodate multiple periods recursively [16], [25]. In practice, the twoperiod dynamic contract design is efficient to balance incentive effectiveness and computing complexity [16].

## A. Two-Period Dynamic Contract Formulation

Due to information asymmetry, the cloud server only knows the historical distribution of WTP levels of ESs through previous participation records rather than the precise WTP level of each ES [16], [22]. Thus, the cloud server can use data mining tools to divide ESs into a set $\Theta = \{ \theta _ { k } | \theta _ { k } \in \mathbb { N } _ { + } , k \in$ $\mathcal { K } = \{ 1 , \dots , K , K \le N \} \}$ k kof K types based on the historical distribution of WTP levels [16], [22]. Considering the certain correlations in WTP across periods [16], [25], in the first period, the k-th type of ESs can be denoted as $\theta _ { k } ^ { 1 } , \ k \in \mathcal { K }$ , and in the ksecond period, the k-th type of ESs is denoted as $\theta _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) , j \in \mathcal { K }$ , which is an expectation correlated to $\theta _ { k } ^ { 1 }$ . Note that these two ktypes are drawn independently from Θ. Without loss of generality, the types in the first and second periods are sorted in nondecreasing order as $\theta _ { 1 } ^ { 1 } \le \cdot \cdot \cdot \le \theta _ { k } ^ { 1 } \le \cdot \cdot \cdot \le \theta _ { K } ^ { 1 }$ and $\theta _ { 1 } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \leq$ $\cdot \cdot \cdot \leq \theta _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \leq \cdot \cdot \cdot \leq \theta _ { K } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ k K k, respectively [16], [25]. We define $p _ { k } ^ { t }$ j k K kas the probability that ESs belong to type $\theta _ { k } ^ { t }$ during period k t, where $\textstyle \sum _ { k = 1 } ^ { K } p _ { k } ^ { t } = 1 , t \in \{ 1 , 2 \}$ .

k kTo incentivize ESs to continuously participate in federated AI agent construction, the cloud server issues a two-period dynamic contract $\Omega \left( \theta _ { k } ^ { 1 } , \theta _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \right)$ at the beginning of the first k j kperiod before the agent module creation starts. The contract item consists of WTP along with the corresponding reward. In the first period, the contract item designed for type-k ESs is represented as $\{ T _ { k } ^ { 1 } \left( \boldsymbol { \theta } _ { k } ^ { 1 } \right) , R _ { k } ^ { 1 } \left( \boldsymbol { \theta } _ { k } ^ { 1 } \right) \}$ }, and in the second period, the k k k kcontract item designed for the same type-k ESs is represented as $\{ T _ { j } ^ { 2 } \left( \theta _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \right) , \breve { R _ { j } ^ { 2 } } \left( \theta _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \right) \} , k , j \in \mathcal { K } .$ . Thus, the formulation of the two-period dynamic contract Ω is expressed as

$$
\Omega = \left\{\left(T _ {k} ^ {1} \left(\theta_ {k} ^ {1}\right), R _ {k} ^ {1} \left(\theta_ {k} ^ {1}\right)\right), \left(T _ {j} ^ {2} \left(\theta_ {j} ^ {2} \left(\theta_ {k} ^ {1}\right)\right), R _ {j} ^ {2} \left(\theta_ {j} ^ {2} \left(\theta_ {k} ^ {1}\right)\right)\right) \right\}. \tag {8}
$$

For conciseness, we denote $T _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ and $R _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ as $T _ { j } ^ { 2 } \ : \left( \theta _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \right)$ and $R _ { j } ^ { 2 } \ : \left( \theta _ { j } ^ { 2 } \ : \left( \theta _ { k } ^ { 1 } \right) \right)$ j k j k, respectively. Based on (6), the j j k jutility of ESs with type $\theta _ { k } ^ { 1 }$ kin period 1 is given by

$$
u _ {k} ^ {1} \left(T _ {k} ^ {1}\right) = \theta_ {k} ^ {1} R _ {k} ^ {1} \left(\theta_ {k} ^ {1}\right) - c T _ {k} ^ {1} \left(\theta_ {k} ^ {1}\right) - E. \tag {9}
$$

Considering that the WTP level $\theta _ { k } ^ { 1 }$ of type-k ESs in period 1 kwould affect the utility in period 2 [25], the expected utility of type-k ESs in period 2 is given by

$$
U _ {k} = u _ {k} ^ {1} \left(T _ {k} ^ {1}\right) + \underbrace {\beta \sum_ {j = 1} ^ {K} p _ {j} ^ {2} \left(T _ {k} ^ {1}\right) u _ {j} ^ {2} \left(T _ {j} ^ {2} \left(T _ {k} ^ {1}\right)\right)} _ {\text { Expected   discounted   utility }}, \tag {10}
$$

where $\beta \in ( 0 , 1 ]$ and $p _ { j } ^ { 2 } \left( T _ { k } ^ { 1 } \right)$ represent a discount factor j kfor the utility and the probability that type-k ESs belong to type $\theta _ { j } ^ { 2 }$ during period 2, respectively. The second term jin (10) represents the expected discounted utility across all $K$ types that ESs are characterized with certain probabilities in period 2, which is designed to capture the longterm benefit of ESs participating in the federated AI agent construction. A larger $\beta$ indicates a greater valuation of the future utility relative to the current utility [16], [25]. Since WTP levels across two periods are positively correlated [16], we have $p _ { j } ^ { 2 } \left( T _ { k } ^ { 1 } \right) \neq p _ { j } ^ { 2 } \left( T _ { k ^ { \prime } } ^ { 1 } \right)$ and ${ \textstyle \sum _ { j = 1 } ^ { k } } p _ { j } ^ { 2 } \left( { \bar { T } } _ { k } ^ { 1 } \right) u _ { j } ^ { 2 } \left( T _ { j } ^ { 2 } \left( { \bar { T } } _ { k } ^ { 1 } \right) \right) \nearrow$ $\begin{array} { r } { \sum _ { j = 1 } ^ { K } \bar { p } _ { j } ^ { 2 } \left( T _ { k ^ { \prime } } ^ { 1 } \right) u _ { j } ^ { 2 } \left( T _ { j } ^ { 2 } \left( T _ { k ^ { \prime } } ^ { 1 } \right) \right) } \end{array}$ , $k \neq k ^ { \prime }$ j k j j k, with the proof presented j j k j jin Lemma 7 in this paper.

Based on (7), the expected utility of the cloud server in period $t \in \{ 1 , 2 \}$ is derived as [16], [25]

$$
U _ {C S} ^ {t} = \left[ \sum_ {k = 1} ^ {K} p _ {k} ^ {t} N \left(\alpha \left(1 - 2 ^ {\frac {- T _ {k} ^ {t} (2 - L \delta) \delta \varepsilon}{2}}\right) - R _ {k} ^ {t}\right) \right] - \sigma E _ {C}. \tag {11}
$$

Therefore, the total profit of the cloud server over two periods is expressed as

$$
U (\Omega) = U _ {C S} ^ {1} + \beta U _ {C S} ^ {2}. \tag {12}
$$

The dynamic contract Ω is directly applied across two periods. According to [25], the long-term contract cycle is divided into five stages, as shown in Fig. 2.

Stage I. Contract confirmation: At the beginning of federated AI agent construction, the cloud server releases the two-period dynamic contract Ω with a set of contract items to ESs. Upon receiving the contract, each ES evaluates its WTP and selects a suitable contract item.  
Stage II. Agent module creation of period 1: After ESs accept selected contract items, the first period of agent module creation begins. ESs first collect feature data from the surrounding environment through inherent wireless sensors. Based on the collected feature data and the initial values informed by the cloud, ESs create agent modules and upload them to the cloud server for integration.

![](images/430e9215d1b993fbe7ea28b171c1d7a15a28a0fbe0fcd027228d8471c21e8761.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Cloud Server (Contract design)"] --> B["Stage I: Release a dynamic contract with multiple contract items"]
  B --> C["Stage I: Sign suitable contract items"]
  C --> D["Stage II: Upload the constructed agent modules in period 1"]
  D --> E["Stage III: Offer rewards in period 1"]
  E --> F["Stage IV: Upload the constructed agent modules in period 2"]
  F --> G["Stage V: Offer rewards in period 2"]
  G --> H["Edge Servers (Contract confirmation)"]
  H --> I["Period 1"]
  H --> J["Period 2"]
```
</details>

Fig. 2. The workflow of the proposed two-period dynamic contract for agent module construction. To minimize disruptions to the construction progress, the proposed dynamic contract remains valid across both periods without requiring redefinition and retransmission to the ESs in period 2.

Stage III. Contract realization of period 1: At the end of period 1, the cloud server integrates the created agent modules. If the integration is successful, the cloud server will offer the rewards $R _ { k } ^ { 1 } \left( \theta _ { k } ^ { 1 } \right)$  specified in the contract to k kESs. Otherwise, the ESs that fail to fulfill the contractual requirements will not obtain the corresponding rewards.  
Stage IV. Agent module creation of period 2: After completing the agent module creation of period 1, ESs can learn their second-period types, and the subsequent process of agent module creation is similar to Stage II.  
- Stage V. Contract realization of period 2: The contract realization of period 2 is similar to Stage III.

## B. Second-Period Contract Design

Since the second-period contract is independent [16], we first use the standard static contract approach [22] to solve the second-period contract. For a feasible contract, the secondperiod contract should simultaneously satisfy both the IR and IC constraints [16], [25].

Definition 1. (IR Constraints in Period 2): Each type-k ES in period 2 can obtain a non-negative utility by selecting the contract item suitable for its second-period type i, i.e.,

$$
u _ {i} ^ {2} \left(T _ {i} ^ {2} \left(T _ {k} ^ {1}\right)\right) = \theta_ {i} ^ {2} R _ {i} ^ {2} \left(\theta_ {k} ^ {1}\right) - c T _ {i} ^ {2} \left(\theta_ {k} ^ {1}\right) - E \geq 0, \forall i \in \mathcal {K}. \tag {13}
$$

Definition 2. (IC Constraints in Period 2): Each type-k ES in period 2 can achieve the maximum utility by selecting the contract item designed for its second-period type i rather than

any other contract item, i.e.,

$$
\theta_ {i} ^ {2} R _ {i} ^ {2} - c T _ {i} ^ {2} - E \geq \theta_ {i} ^ {2} R _ {j} ^ {2} - c T _ {j} ^ {2} - E,   \forall i \neq j \in \mathcal {K}. \tag {14}
$$

IR constraints in (13) motivate ESs to participate in federated AI agent construction by guaranteeing that their utilities are nonnegative if they select suitable contract items. IC constraints in (14) encourage ESs to reveal their actual type, avoiding the risk that ESs misrepresent their actual types to cheat for higher rewards. In the following, we derive the necessary conditions of the second-period contract.

Lemma 1: For any feasible contract, $R _ { i } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \ge R _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ if and only if $T _ { i } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \ge T _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ , where $i \neq j .$ .

i k j kProof: Please refer to Appendix A, available online.

Lemma 2: For any feasible contract, if $\theta _ { i } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \ge \theta _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ , then $R _ { i } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \ge R _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ .

i k j kProof: Please refer to Appendix B, available online.

Lemma 1 ensures that ESs can receive higher rewards with more training rounds for improving the model quality of agent modules. Lemma 2 indicates that ESs with a higher WTP level can obtain higher rewards. According to Lemmas 1 and 2, we can prove the monotonicity property of the second-period contract as follows:

Lemma 3: (Monotonicity Property): For any feasible contract, if $\theta _ { i } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \ge \theta _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ , then $\dot { T } _ { i } ^ { 2 } \left( \dot { \theta } _ { k } ^ { 1 } \right) \ge T _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ .

i k j k i k j kSince it is exceedingly challenging to make the dynamic contract solution under K number of IR constraints and $K ( K - 1 )$ number of IC constraints, we reduce the number of IR and IC constraints to derive a tractable set of constraints to solve the second-period contract.

Lemma 4. (Reduce IR Constraints in Period 2): The K number of IR constraints in period 2 can be reduced to a single constraint, i.e.,

$$
\theta_ {1} ^ {2} R _ {1} ^ {2} \left(\theta_ {k} ^ {1}\right) - c T _ {1} ^ {2} \left(\theta_ {k} ^ {1}\right) - E = 0. \tag {15}
$$

Proof: Please refer to Appendix C, available online.

Lemma 5: The IC constraints in period 2 can be reduced into Local Downward Incentive Compatibility (LDIC) (16) and Local Upward Incentive Compatibility (LUIC) (17), i.e.,

$$
\theta_ {i} ^ {2} R _ {i} ^ {2} \left(\theta_ {k} ^ {1}\right) - c T _ {i} ^ {2} \left(\theta_ {k} ^ {1}\right) - E \geq \theta_ {i} ^ {2} R _ {i - 1} ^ {2} \left(\theta_ {k} ^ {1}\right) - c T _ {i - 1} ^ {2} \left(\theta_ {k} ^ {1}\right) - E. \tag {16}
$$

$$
\theta_ {i} ^ {2} R _ {i} ^ {2} \left(\theta_ {k} ^ {1}\right) - c T _ {i} ^ {2} \left(\theta_ {k} ^ {1}\right) - E \geq \theta_ {i} ^ {2} R _ {i + 1} ^ {2} \left(\theta_ {k} ^ {1}\right) - c T _ {i + 1} ^ {2} \left(\theta_ {k} ^ {1}\right) - E. \tag {17}
$$

Proof: Please refer to Appendix D, available online.

Lemma 6. (Reduce IC Constraints in Period 2): The $K ( K - 1 )$ number of IC constraints in period 2 can be reduced to (K − 1) number of IC constraints, i.e.,

$$
\theta_ {i} ^ {2} R _ {i} ^ {2} - c T _ {i} ^ {2} - E = \theta_ {i} ^ {2} R _ {i - 1} ^ {2} - c T _ {i - 1} ^ {2} - E,   \forall i \geq 2. \tag {18}
$$

Proof: Please refer to Appendix E, available online.

Based on Lemmas 4 and 6, the K number of IR constraints (13) and $K ( K - 1 )$ number of IC constraints (14) can be reduced to one IR constraint (15) and $( K - 1 )$ number of IC constraints (18). We derive the sufficient and necessary conditions of the feasible contract in period 2 as follows:

Theorem 1. (Sufficient and Necessary Conditions in Period 2): A feasible contract in period 2 must satisfy the following sufficient and necessary conditions:

$1 ) 0 \leq R _ { 1 } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \leq \cdots \leq R _ { k } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \leq \cdots \leq R _ { K } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) .$  
2) $0 \leq T _ { 1 } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \leq \cdots \leq T _ { k } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \leq \cdots \leq T _ { K } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right)$ .  
3) $\theta _ { 1 } ^ { 2 } R _ { 1 } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) - c T _ { 1 } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) - E = 0 .$  
$4 ) ~ \theta _ { i } ^ { 2 } R _ { i } ^ { 2 } - c T _ { i } ^ { 2 } - E = \theta _ { i } ^ { 2 } R _ { i - 1 } ^ { 2 } - c T _ { i - 1 } ^ { 2 } - E , \forall i \geq 2 .$

In Theorem 1, the first two conditions indicate the monotonicity property of the second-period contract. The last two conditions are the simplified IR and IC constraints in period 2, respectively. Based on (15) and (18), the optimal reward in period 2 can be derived by using the iterative method.

Theorem 2: (Optimal Rewards in Period 2): The optimal reward $\left( R _ { i } ^ { 2 } \right) ^ { \star }$ in period 2 is given by

$$
\left(R _ {i} ^ {2}\right) ^ {\star} = \left\{ \begin{array}{l} \frac {c T _ {1} ^ {2} \left(\theta_ {k} ^ {1}\right) + E}{\theta_ {1} ^ {2}}, i = 1, \\ \frac {c T _ {1} ^ {2} \left(\theta_ {k} ^ {1}\right) + E}{\theta_ {1} ^ {2}} + c \sum_ {j = 2} ^ {i} \frac {T _ {j} ^ {2} \left(\theta_ {k} ^ {1}\right) - T _ {j - 1} ^ {2} \left(\theta_ {k} ^ {1}\right)}{\theta_ {j} ^ {2}}, i \neq 1. \end{array} \right. \tag {19}
$$

Proof: Please refer to Appendix F, available online.

![](images/f35841f95602305a7905ea326879e9f454af789ac8aecc837867e20fc69ed8db.jpg)

## C. First-Period Contract Design

For the feasible contract design in period 1, the IR constraints are similar to those in Definition 1, as given by

$$
u _ {k} ^ {1} \left(T _ {k} ^ {1}\right) = \theta_ {k} ^ {1} R _ {k} ^ {1} - c T _ {k} ^ {1} - E \geq 0, \forall k \in \mathcal {K}. \tag {20}
$$

Since ESs may misreport their WTP levels in period 1 to gain higher utilities in period 2 [25], instead of considering just the one-period IC constraints, the cloud server should consider the Intertemporal IC (IIC) constraints to incentivize ESs to reflect their actual types [25], and the IIC constraints are expressed as

$$
\begin{array}{l} u _ {k} ^ {1} \left(T _ {k} ^ {1}\right) + \beta \sum_ {j = 1} ^ {K} p _ {j} ^ {2} \left(T _ {k} ^ {1}\right) u _ {j} ^ {2} \left(T _ {j} ^ {2} \left(T _ {k} ^ {1}\right)\right) \\ \geq u _ {k} ^ {1} \left(T _ {k ^ {\prime}} ^ {1}\right) + \beta \sum_ {j = 1} ^ {K} p _ {j} ^ {2} \left(T _ {k} ^ {1}\right) u _ {j} ^ {2} \left(T _ {j} ^ {2} \left(T _ {k ^ {\prime}} ^ {1}\right)\right), \forall k \neq k ^ {\prime} \in \mathcal {K}. \tag {21} \\ \end{array}
$$

From the IIC constraints in (21), we know that ESs will obtain higher utilities by truthfully declaring their WTP levels. When the first-perioddent, we have $\begin{array} { r } { \sum _ { j = 1 } ^ { K } p _ { j } ^ { 2 } \left( \dot { T } _ { k } ^ { 1 } \right) u _ { j } ^ { 2 } \left( \dot { T } _ { j } ^ { 2 } \left( T _ { k } ^ { 1 } \right) \right) = \sum _ { j = 1 } ^ { K } p _ { j } ^ { 2 } \dot { \left( T _ { k } ^ { 1 } \right) } } \end{array}$ $u _ { j } ^ { 2 } ( T _ { j } ^ { 2 } \left( T _ { k ^ { \prime } } ^ { 1 } \right) )$ $\begin{array} { r l r } { \sum _ { j = 1 } ^ { K } p _ { j } ^ { 2 } \left( T _ { k } ^ { 1 } \right) u _ { j } ^ { 2 } \left( T _ { j } ^ { 2 } \left( T _ { k ^ { \prime } } ^ { 1 } \right) \right) } & { { } } & { } \end{array}$ j j k j j k j j kthe discounted expected utility of the type-k ESs that declare their types are $\theta _ { k ^ { \prime } } ^ { 1 }$ in period 1, and the IIC constraints can be ksimplified as the IC constraints of the standard static contract. In the following, we derive the necessary conditions for the feasible contract in period 1.

Lemma 7: For any feasible contract in period 1, if $\theta _ { k } ^ { 1 } > \theta _ { k ^ { \prime } } ^ { 1 }$ , then $T _ { k } ^ { 1 } > T _ { k ^ { \prime } } ^ { 1 }$ , and $\dot { T } _ { j } ^ { 2 } \left( T _ { k } ^ { 1 } \right) > T _ { j } ^ { 2 } ( T _ { k ^ { \prime } } ^ { 1 } )$ , where $k \neq k ^ { \prime }$ k.

k k j k j kProof: Please refer to Appendix G, available online.

Lemma 8: For any feasible contract in period 1, $T _ { k } ^ { 1 } > T _ { k ^ { \prime } } ^ { 1 }$ if and only if $R _ { k } ^ { 1 } > R _ { k ^ { \prime } } ^ { \mathrm { i } }$ , where $k \neq k ^ { \prime }$ .

k kProof: Please refer to Appendix H, available online.

![](images/e9648667b6be2fc4077a330f676e7643c88d53973719f4e0af3032bdccb97c29.jpg)

Lemma 7 indicates that the ESs with higher WTP levels will perform more training rounds for agent module creation in both period 1 and period 2, even if they have the same WTP level in period 2. Lemma 8 represents the monotonicity of first-period rewards and training rounds, indicating that the ESs with higher WTP levels will receive higher rewards from the cloud server in period 1. Next, we reduce the IR and IIC constraints in period 1, which is similar to period 2.

Lemma 9. (Reduce IR Constraints in Period 1): Similar to (15), the K number of IR constraints in period 1 can also be reduced to a single constraint, i.e.,

$$
\theta_ {1} ^ {1} R _ {1} ^ {1} - c T _ {1} ^ {1} - E = 0. \tag {22}
$$

Lemma 10. (Reduce IIC Constraints in Period 1): Similar to (18), the $K ( K - 1 )$ number of IIC constraints can be reduced to the $( K - 1 )$ number of local downward IIC constraints, which is given by

$$
\begin{array}{l} u _ {k} ^ {1} \left(T _ {k} ^ {1}\right) + \beta \sum_ {j = 1} ^ {K} p _ {j} ^ {2} \left(T _ {k} ^ {1}\right) u _ {j} ^ {2} \left(T _ {j} ^ {2} \left(T _ {k} ^ {1}\right)\right) \\ = u _ {k} ^ {1} \left(T _ {k - 1} ^ {1}\right) + \beta \sum_ {j = 1} ^ {K} p _ {j} ^ {2} \left(T _ {k} ^ {1}\right) u _ {j} ^ {2} \left(T _ {j} ^ {2} \left(T _ {k - 1} ^ {1}\right)\right). \tag {23} \\ \end{array}
$$

The proofs of Lemmas 9 and 10 are similar to Lemmas 4 and 6, respectively. We present the sufficient and necessary conditions of the feasible contract in period 1 in the following.

Theorem 3. (Sufficient and Necessary Conditions in Period 1): A feasible contract in period 1 must satisfy the following sufficient and necessary conditions:

1) $0 \leq R _ { 1 } ^ { 1 } \leq \cdot \cdot \cdot \leq R _ { k } ^ { 1 } \leq \cdot \cdot \cdot \leq R _ { K } ^ { 1 } ,$

2) $0 \leq T _ { 1 } ^ { 1 } \leq \cdots \leq T _ { k } ^ { 1 } \leq \cdots \leq T _ { K } ^ { 1 } ,$

3) $\theta _ { 1 } ^ { 1 } R _ { 1 } ^ { 1 } - c T _ { 1 } ^ { 1 } - E = 0 ,$

$u _ { k } ^ { 1 } \left( T _ { k } ^ { 1 } \right) + \beta \sum _ { j = 1 } ^ { K } p _ { j } ^ { 2 } \left( T _ { k } ^ { 1 } \right) u _ { j } ^ { 2 } \left( T _ { j } ^ { 2 } \left( T _ { k } ^ { 1 } \right) \right)$

$$
= u _ {k} ^ {1} \left(T _ {k - 1} ^ {1}\right) + \beta \sum_ {j = 1} ^ {K} p _ {j} ^ {2} \left(T _ {k} ^ {1}\right) u _ {j} ^ {2} \left(T _ {j} ^ {2} \left(T _ {k - 1} ^ {1}\right)\right).
$$

In Theorem 3, the first two conditions are the monotonicity property of the first-period contract. The last two conditions present the simplified IR and IIC constraints in period 1, respectively. Based on (22) and (23), the optimal reward in period 1 can also be derived using the iterative method.

Theorem 4. (Optimal Rewards in Period 1): The optimal reward $\left( R _ { i } ^ { 1 } \right) ^ { \star }$ in period 1 is given by

$$
\left(R _ {i} ^ {1}\right) ^ {\star} = \left\{ \begin{array}{l} \frac {c T _ {1} ^ {1} + E}{\theta_ {1} ^ {1}}, i = 1, \\ \frac {c T _ {1} ^ {1} + E}{\theta_ {1} ^ {1}} + \sum_ {k = 2} ^ {i} \left[ \left(T _ {k} ^ {1} - T _ {k - 1} ^ {1}\right) \frac {c}{\theta_ {k} ^ {1}} \right. \\ \left. + \frac {\beta}{\theta_ {k} ^ {1}} \sum_ {j = 2} ^ {K} p _ {j} ^ {2} \left(T _ {k} ^ {1}\right) \Phi_ {j} \right], i \neq 1, \end{array} \right. \tag {24}
$$

$\begin{array} { r } { \Phi _ { j } = \sum _ { l = 1 } ^ { j - 1 } [ \theta _ { j } ^ { 2 } c ( T _ { l } ^ { 2 } ( \theta _ { k - 1 } ^ { 1 } ) - T _ { l } ^ { 2 } ( \theta _ { k } ^ { 1 } ) ) ( \frac { 1 } { \theta _ { l } ^ { 2 } } - \frac { 1 } { \theta _ { \scriptscriptstyle { l \_ { - 1 } } } ^ { 2 } } ) ] . } \end{array}$

θl θlProof: The proof of the optimal reward (24) in period 1 is similar to the proof of the optimal reward (19) in period 2. -

## D. Optimal Two-Period Contract

To solve the optimal two-period contract, we substitute the derived optimal rewards (24) and (19) into the expected utility of the cloud server (11), and the expected utility of the cloud server in period 2 is expressed as

$$
U _ {C S} ^ {2} \left(T _ {j} ^ {2} \left(\theta_ {k} ^ {1}\right)\right) = \left[ \sum_ {j = 1} ^ {K} p _ {j} ^ {2} \left(T _ {k} ^ {1}\right) N \left(\alpha Q _ {j} ^ {2} - R _ {j} ^ {2}\right) \right] - \sigma E _ {C}, \tag {25}
$$

where $\begin{array} { r } { Q _ { i } ^ { 2 } = 1 - 2 ^ { \frac { - T _ { j } ^ { 2 } \left( \theta _ { k } ^ { 1 } \right) \left( 2 - L \delta \right) \delta \varepsilon } { 2 } } } \end{array}$

jSimilarly, the expected utility of the cloud server in period 1 is expressed as

$$
U _ {C S} ^ {1} \left(T _ {k} ^ {1}\right) = \left[ \sum_ {k = 1} ^ {K} p _ {k} ^ {1} \left(T _ {k} ^ {1}\right) N \left(\alpha Q _ {k} ^ {1} - R _ {k} ^ {1}\right) \right] - \sigma E _ {C}, \tag {26}
$$

where $Q _ { k } ^ { 1 } = 1 - 2 ^ { \frac { - T _ { k } ^ { 1 } ( 2 - L \delta ) \delta \varepsilon } { 2 } }$

kTherefore, based on (12), the dynamic contract optimization problem is formulated as

$$
\max _ {\left\{T _ {k} ^ {1}, T _ {j} ^ {2} \left(\theta_ {k} ^ {1}\right) \right\}} U _ {C S} ^ {1} \left(T _ {k} ^ {1}\right) + \beta U _ {C S} ^ {2} \left(T _ {j} ^ {2} \left(\theta_ {k} ^ {1}\right)\right)
$$

s.t. (19) and (24). (27)

Remark 1: The number of variables in the dynamic contract optimization problem (27) has been reduced from 4K to 2K. Currently, researchers rely on traditional optimization algorithms, such as heuristic algorithms, to solve this problem [16], [25]. However, in practical scenarios, the parameters of ESs and the cloud server, such as communication channel conditions, fluctuate dynamically. As a result, traditional optimization algorithms must be frequently redesigned and re-implemented, leading to substantial computing resource consumption. Furthermore, traditional algorithms often fail to generalize to practical scenarios when the environment lacks complete and accurate information [17]. DRL algorithms have been successfully applied for optimal static contract design due to their adaptability to dynamic environments [18], [27]. In particular, PPO, as an onpolicy and model-free algorithm, iteratively updates the policy towards optimal performance of contract generation by using a clipped surrogate objective [28], and SAC, as an off-policy algorithm, trains a stochastic policy for optimal dynamic contract generation by maximizing both the expected cumulative reward and policy entropy [22]. Notably, researchers have adopted GDMs to identify optimal static contracts, achieving superior performance compared with traditional DRL algorithms [17], [22]. In particular, the DMSAC algorithm can improve stability and performance over baseline DRL algorithms [20]. Building on this foundation [20], we propose the EDMSAC algorithm that leverages lightweight GDMs to generate optimal dynamic contracts, effectively adapting to the changing environment during federated AI agent construction.

![](images/6e3ffeb407ca0b7e247292dd8cec9e753da3c066950b6bb8588594e9fe1b5873.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Target Actor"] --> B["Denoise"]
  B --> C["Dynamic Pruning"]
  C --> D["Soft Update"]
  D --> E["Update target actor network"]
  E --> F["Target Critic"]
  F --> G["Critic Networks"]
  G --> H["Double Critic"]
  H --> I["Optimizer"]
  I --> J["Replay Buffer"]
    
    subgraph Environment
  K["Fiber link"] --> L["Cloud Server"]
  L --> M["Edge Servers"]
  M --> N["Record"]
  N --> O["Sample"]
  O --> P["Recent"]
  O --> Q["Past"]
    end
    
    subgraph Diffusion Model-based Actor Network
  R["Noise"] --> S["MLP"]
  T["Reverse Process"] --> U["Hidden Layers"]
  V["Gaussian Noise"] --> W["A_M"]
  X["Optimal Contract"] --> Y["A_1"]
  Z["Action A0"] --> AA["A0 → A0 Map"]
  AB["State S"] --> AC["S"]
  AD["Update policy"] --> AE["(S, 1, A1)"]
  AF["Update policy"] --> AG["(S, M, A_M)"]
  AH["Forward Process"] --> AI["A_M-1"]
  AJ["Input Layer"] --> AK["Output Layer"]
    end
    
    subgraph Soft Update
  AL["The z + 1-th training round"] --> AM["The z-th training round"]
  AN["The t1 ... θ1n θm"] --> AO["The t1 ... θm n"]
  AP["The t1 ... θ1n ... θm n"] --> AQ["The t1 ... θ1n ... θm n"]
    end
    
    subgraph Critic Networks
  AR["Critic Qv1"] --> AS["Critic Qv2"]
  AT["Critic Qv3"] --> AU["Critic Qv4"]
  AV["Critic Qv5"] --> AW["Critic Qv6"]
  AX["Critic Qv7"] --> AY["Critic Qv8"]
  AZ["Critic Qv9"] --> BA["Critic Qv10"]
  BB["Critic Qv11"] --> BC["Critic Qv12"]
  BD["Critic Qv13"] --> BE["Critic Qv14"]
  BF["Critic Qv15"] --> BG["Critic Qv16"]
  BH["Critic Qv17"] --> BI["Critic Qv18"]
  BJ["Critic Qv19"] --> BK["Critic Qv20"]
  BL["Critic Qv21"] --> BM["Critic Qv22"]
  BN["Critic Qv23"] --> BO["Critic Qv24"]
  BP["Critic Qv25"] --> BQ["Critic Qv26"]
  BR["Critic Qv27"] --> BS["Critic Qv28"]
  BT["Critic Qv29"] --> BU["Critic Qv30"]
    end
    
    subgraph Double Critic Networks
  BV["Critic Qv3"] --> BW["Critic Qv4"]
  BX["Critic Qv5"] --> BY["Critic Qv6"]
  ZC["Critic Qv7"] --> DA["Critic Qv8"]
  DB["Critic Qv9"] --> DBC["Critic Qv10"]
  DBC --> DBD["Critic Qv11"]
  DBC --> DBE["Critic Qv12"]
  DBC --> DBF["Critic Qv13"]
  DBC --> DBG["Critic Qv14"]
  DBC --> DBH["Critic Qv15"]
  DBC --> DBI["Critic Qv16"]
  DBC --> DBJ["Critic Qv17"]
  DBC --> DBK["Critic Qv18"]
  DBC --> DBL["Critic Qv19"]
  DBC --> DBM["Critic Qv20"]
    end
    
    subgraph Double Critic Networks
        N["Critic Qv3"] <--> O["Critic Qv4"]
        P["Critic Qv5"] <--> Q["Critic Qv6"]
        R["Critic Qv7"] <--> S["Critic Qv8"]
        T["Critic Qv9"] <--> U["Critic Qv10"]
        V["Critic Qv11"] <--> W["Critic Qv12"]
        X["Critic Qv13"] <--> Y["Critic Qv14"]
        Z["Critic Qv15"] <--> AB["Critic Qv16"]
  AB --> Z
    end
```
</details>

Fig. 3. The architecture of the proposed EDMSAC algorithm for dynamic contract design. The EDMSAC algorithm can generate optimal two-period contracts through the denoising process. To enhance denoising efficiency, we innovatively apply dynamic structured pruning techniques to the MLP of DM-based actor networks. Note that the unimportant neurons in the actor networks are simply masked, not removed outright.

## V. ENHANCED DIFFUSION MODEL-BASED SOFT ACTOR-CRITIC ALGORITHMS FOR OPTIMAL DYNAMIC CONTRACT DESIGN

In this section, we first model the optimization problem (27) as a Markov Decision Process (MDP). Subsequently, we introduce the Denoising Diffusion Probabilistic Model (DDPM). Finally, we present the enhanced diffusion policy for optimal dynamic contract design, as shown in Fig. 3.

## A. Markov Decision Process Formulation

MDP is a mathematical framework for modeling decisionmaking problems [39], which is represented as a five-element tuple consisting of a state space, an action space, a reward function, a discount factor determining the weight of the future reward relative to the current reward, and state transition probabilities. In the following, we explicitly define the state space, action space, and reward function of the MDP framework.

1) State Space: At each step $z \in \{ 1 , 2 , \dots , Z \}$ , the state space from the environment is defined as

$$
\boldsymbol {S} \triangleq \left\{N, K, \sigma , P _ {n}, r _ {n, c}, E _ {C}, p _ {k} ^ {1}, p _ {j} ^ {2} \left(T _ {k} ^ {1}\right), \theta_ {k} ^ {1}, \theta_ {j} ^ {2} \right\}, \forall j, k \in \mathcal {K}, \tag {28}
$$

where N and K are constants that do not evolve over time, while the other terms vary with each training round. Notably, the size of the state space S is $( 6 + 3 K + K ^ { 2 } )$ .

2) Action Space: According to the optimization problem (27), the action space in the z-th training round is defined as

$$
\boldsymbol {A} \triangleq \left\{T _ {k} ^ {1}, T _ {j} ^ {2} \left(\theta_ {k} ^ {1}\right) \right\}, \forall j, k \in \mathcal {K}, y e s \tag {29}
$$

where A is mapped from the denoising action A˜ .

3) Reward Function: After executing the action A based on the current state S, the DRL agent receives an immediate reward $r ( S , A )$ . To enhance the stability of its learning process, we define a penalty-based reward function as

$$
r (\boldsymbol {S}, \boldsymbol {A}) = U _ {C S} ^ {1} \left(T _ {k} ^ {1}\right) + \beta U _ {C S} ^ {2} \left(T _ {j} ^ {2} \left(\theta_ {k} ^ {1}\right)\right) - \underbrace {\lambda \sum_ {i = 1} ^ {2 K} \left(\tilde {\boldsymbol {A}} [ i ]\right) ^ {2}} _ {\text { Action   penalty }}, \tag {30}
$$

where λ is a pre-defined parameter that controls the degree of the action penalty.

## B. Denoising Diffusion Probabilistic Models

DDPMs are powerful generative models that generate data based on forward and reverse processes [21]. In the forward process, given initial data $\pmb { x } _ { 0 } \sim q ( \pmb { x } _ { 0 } )$ ), the Gaussian noise is gradually added to the data $\pmb { x } _ { 0 } \sim \pmb { q } ( \pmb { x } _ { 0 } )$ across M steps with a pre-defined variance schedule 
 [40], described as

$$
q \left(\boldsymbol {x} _ {m} | \boldsymbol {x} _ {m - 1}\right) := \mathcal {N} \left(\boldsymbol {x} _ {m}; \sqrt {1 - \epsilon_ {m}} \boldsymbol {x} _ {m - 1}, \epsilon_ {m} \mathbf {I}\right), \tag {31}
$$

where $\epsilon _ { m } = 1 - e ^ { - \frac { \epsilon _ { m i n } } { M } - \frac { 2 m - 1 } { 2 ^ { - } M ^ { 2 } } \left( \epsilon _ { m a x } - \epsilon _ { m i n } \right) }$ − m2˜ 12 (max−min) and I is the identity mmatrix. By using the Markov chain property, the joint distribution of $\pmb { x } _ { 1 } , \ldots , \pmb { x } _ { M }$ conditioned on $\scriptstyle { \pmb x } _ { 0 }$ is given by

$$
q \left(\boldsymbol {x} _ {1: M} | \boldsymbol {x} _ {0}\right) = \prod_ {m = 1} ^ {M} q \left(\boldsymbol {x} _ {m} | \boldsymbol {x} _ {m - 1}\right). \tag {32}
$$

In the reverse process, the DDPM denoises the noisy data $_ { x _ { M } }$ by learning parameterized transitions $g _ { \pmb { \theta } } \big ( \pmb { x } _ { m - 1 } \big | \pmb { x } _ { m } \big )$ [40], which is expressed as

$$
g _ {\boldsymbol {\theta}} (\boldsymbol {x} _ {m - 1} | \boldsymbol {x} _ {m}) = \mathcal {N} (\boldsymbol {x} _ {m - 1}; \mu_ {\boldsymbol {\theta}} (\boldsymbol {x} _ {m}, m), \Sigma_ {\boldsymbol {\theta}} (\boldsymbol {x} _ {m}, m)), \tag {33}
$$

Algorithm 1: EDMSAC for Dynamic Contract Design.  
1 Initialize policy network $\pi_{\theta}$ , critic networks $Q_{v_1}, Q_{v_2}$ , target networks $\hat{\pi}_{\hat{\theta}}, Q_{\hat{v}_1}, Q_{\hat{v}_2}$ , relay buffer $\mathcal{D}$ , pruning rate $\varrho$ , and mask matrices $\boldsymbol{W}$ .

2 ## Training
3 for the training step $v = 1$ to $V$ do
4    for the number of transitions $z = 1$ to $Z$ do
5    ### Generating contracts
6    Observe state $S_z$ and initialize a random normal distribution $\tilde{A}_M \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ .
7    Map $\tilde{A}_0$ to $A_0$ and perform $A_0$ , observe the next state $S_{z+1}$ , and receive reward $r_z$ .
8    Store record $(S_z, A_0, S_{z+1}, r_z)$ into $\mathcal{D}$ .
9    end
10    ### Dynamic pruning
11    Calculate neuron importance of $\theta$ and $\hat{\theta}$ by using (41), respectively.
12    Use the mask matrices $\boldsymbol{W}$ to mask output neurons based on the pruning rate $\varrho$ by (42).
13    ### Parameter updates
14    Sample a random mini-batch of transitions $\mathcal{B}_z$ with size $B$ from $\mathcal{D}$ .
15    Update the policy $\pi_{\theta}$ using $\mathcal{B}_z$ by (43).
16    Update $Q_{v_1}, Q_{v_2}$ using $\mathcal{B}_z$ by (40).
17    Update target networks $\hat{\pi}_{\hat{\theta}}, Q_{\hat{v}_1}, Q_{\hat{v}_2}$ by (44).
18 end
19 Reconstruct the compact policy networks.
20 ## Inference
21 Input a state $S$ .
22 Generate $\tilde{A}_0$ based on the target policy $\hat{\pi}_{\hat{\theta}}$ by (38).
23 return $A_0 = \Omega^*$ .

where $\mu _ { \pmb { \theta } }$ and $\Sigma _ { \theta }$ are parameterized by deep neural networks under the condition that with model parameters θ. Hence, the trajectory from $\begin{array} { r } { \prod _ { m = 1 } ^ { M } ( 1 - \epsilon _ { m } ) \approx 0 } \end{array}$ M is given by $\pmb { x } _ { M }$ to $\scriptstyle { \mathbf { { \mathit { x } } } } _ { 0 }$

$$
g _ {\boldsymbol {\theta}} (\boldsymbol {x} _ {0: M}) = \mathcal {N} (\boldsymbol {x} _ {M}; \mathbf {0}, \mathbf {I}) \prod_ {m = 1} ^ {M} g _ {\boldsymbol {\theta}} (\boldsymbol {x} _ {m - 1} | \boldsymbol {x} _ {m}). \tag {34}
$$

The training objective of DDPMs is to maximize the varia-$\begin{array} { r } { \mathbb { E } _ { q ( \pmb { x } _ { 0 : M } ) } \big [ \mathrm { l n } \frac { g _ { \pmb { \theta } } ( \pmb { x } _ { 0 : M } ) } { q ( \pmb { x } _ { 1 : M } | \pmb { x } _ { 0 } ) } \big ] [ 2 1 ] } \end{array}$ . After q M q Mcompleting the training of DDPMs, the original data $\scriptstyle { \mathbf { { \mathit { x } } } } _ { 0 }$ can be recovered from the noisy data $_ { x _ { M } }$ .

## C. Enhanced Diffusion Policy for Dynamic Contract Design

We define the dynamic contract design policy as $\pi _ { \boldsymbol { \theta } } ( \tilde { \boldsymbol { A } } | S )$ with parameters θ. The goal of $\pi _ { \boldsymbol { \theta } } ( \tilde { \boldsymbol { A } } | S )$ is to generate optimal dynamic contracts by maximizing the expected cumulative reward based on (30), which is given by [20]

$$
\mathbb {E} \left[ \sum_ {z = 0} ^ {Z} \gamma^ {z} (r (\boldsymbol {S} _ {z}, \boldsymbol {A} _ {z}) + \kappa \mathcal {H} (\pi_ {\boldsymbol {\theta}} (\cdot | \boldsymbol {S} _ {z}))) \right], \tag {35}
$$

where $\gamma$ is the discount factor for future rewards, $\mathcal { H } ( \pi _ { \pmb { \theta } } ( \cdot |  { \boldsymbol { S } } _ { z } ) )$ represents the entropy of the policy $\pi _ { \boldsymbol { \theta } } ( S _ { z } )$ z, and κ is the temzperature coefficient that controls the strength of the entropy.

According to (34), the dynamic contract design policy $\pi _ { \boldsymbol { \theta } } ( \tilde { \boldsymbol { A } } | S )$ can be obtained through the reverse process of a conditional DM, expressed as [21]

$$
\pi_ {\boldsymbol {\theta}} \left(\tilde {\boldsymbol {A}} | \boldsymbol {S}\right) = \mathcal {N} \left(\tilde {\boldsymbol {A}} _ {M}; \mathbf {0}, \mathbf {I}\right) \prod_ {m = 1} ^ {M} g _ {\boldsymbol {\theta}} \left(\tilde {\boldsymbol {A}} _ {m - 1} | \tilde {\boldsymbol {A}} _ {m}, \boldsymbol {S}\right), \tag {36}
$$

where the end sample of the reverse chain is ${ \tilde { \cal A } } _ { 0 } .$ According to $[ 2 1 ] , g _ { \pmb { \theta } } ( \tilde { \cal A } _ { m - 1 } | \tilde { \cal A } _ { m } , S )$ is modeled as a Gaussian distribution $\mathcal { N } ( \tilde { \boldsymbol { A } } _ { m - 1 } ; \mu _ { \boldsymbol { \theta } } ( \tilde { \boldsymbol { A } } _ { m } , \boldsymbol { S } , m ) , \boldsymbol { \Sigma } _ { \boldsymbol { \theta } } ( \tilde { \boldsymbol { A } } _ { m } , \boldsymbol { S } , m ) )$ based on (33), with m mthe covariance matrix $\begin{array} { r } { \Sigma _ { \pmb { \theta } } ( \tilde { \bf A } _ { m } , S , m ) = \frac { \zeta _ { m } ( 1 - \bar { \chi } _ { m - 1 } ) } { 1 - \bar { \chi } _ { m } } \mathbf { I } } \end{array}$ and the mean $\mu _ { \pmb \theta } ( \tilde { \pmb A } _ { m } , \pmb S , m )$ constructed as

$$
\mu_ {\boldsymbol {\theta}} \left(\tilde {\boldsymbol {A}} _ {m}, \boldsymbol {S}, m\right) = \frac {1}{\sqrt {\chi_ {m}}} \left(\tilde {\boldsymbol {A}} _ {m} - \frac {\zeta_ {m} \tanh \xi_ {\boldsymbol {\theta}} \left(\tilde {\boldsymbol {A}} _ {m} , \boldsymbol {S} , m\right)}{\sqrt {1 - \bar {\chi} _ {m}}}\right), \tag {37}
$$

where $\zeta _ { m } \in ( 0 , 1 )$ is a hyperparameter for model training, $\chi _ { m } = 1 - \zeta _ { m } ,$ , and χ¯ = m =0 χ [17], [21]. $\xi _ { \pmb { \theta } } ( \tilde { \pmb { A } } _ { m } , \pmb { S } , m )$ is m m m i i mthe Multi-Layer Perceptron (MLP) of DM-based actor networks, as shown in Fig. 3. We first sample $\tilde { \mathbf { A } } _ { M } \sim \mathcal { N } ( \mathbf { 0 } , \mathbf { I } )$ , and then a series of samples $\tilde { \mathbf { A } } _ { m } , m = M , \dots , 1$ Mcan be obtained through mthe reverse diffusion chain parameterized by θ, which is given by

$$
\tilde {\boldsymbol {A}} _ {m - 1} \mid \tilde {\boldsymbol {A}} _ {m} = \frac {\tilde {\boldsymbol {A}} _ {m}}{\sqrt {\chi_ {m}}} - \frac {\zeta_ {m}}{\sqrt {\chi_ {m} (1 - \bar {\chi} _ {m})}} \xi_ {\theta} (\tilde {\boldsymbol {A}} _ {m}, \boldsymbol {S}, m) + \sqrt {\zeta_ {m}} \xi , \tag {38}
$$

where $\xi \sim \mathcal { N } ( \mathbf { 0 } , \mathbf { I } )$ . Notably, when $m = 1 .$ , we have $\xi = 0 [ 2 1 ]$ , [40]. For policy improvement, we introduce the Q-function [21]. Specifically, we create two critic networks $Q _ { v _ { 1 } } , Q _ { v _ { 2 } }$ , target critic networks $Q _ { \hat { v } _ { 1 } } , Q _ { \hat { v } _ { 2 } } ,$ and a target policy $\hat { \pi } _ { \hat { \pmb { \theta } } } .$ . The final policy-learning objective is to minimize the actor loss, which is given by

$$
\mathcal {L} (\boldsymbol {\theta}) = - \mathbb {E} _ {\boldsymbol {S} \sim \mathcal {D}, \tilde {\boldsymbol {A}} _ {0} \sim \pi_ {\boldsymbol {\theta}}} \left[ Q _ {\boldsymbol {v}} \left(\boldsymbol {S}, \tilde {\boldsymbol {A}} _ {0}\right) + \kappa \log \pi_ {\boldsymbol {\theta}} \left(\tilde {\boldsymbol {A}} _ {0} | \boldsymbol {S}\right) \right], \tag {39}
$$

where $Q _ { v } ( S , \tilde { A } _ { 0 } ) = \operatorname * { m i n } \{ Q _ { v _ { 1 } } ( S , \tilde { A } _ { 0 } ) , Q _ { v _ { 2 } } ( S , \tilde { A } _ { 0 } ) \}$ and $\mathcal { D }$ is the relay buffer. To update the Q-function, we minimize the temporal difference error, expressed as

$$
\mathbb {E} _ {\left(\boldsymbol {S} _ {z}, \boldsymbol {A} _ {z}, \boldsymbol {S} _ {z + 1}, r _ {z}\right) \sim \mathcal {B} _ {z}} \left[ \sum_ {i = 1, 2} \left(r \left(\boldsymbol {S} _ {z}, \boldsymbol {A} _ {z}\right) + \gamma^ {z} \left(1 - d _ {z + 1}\right) \right. \right.
$$

$$
\left.\left(Q _ {\hat {\boldsymbol {v}}} \left(\boldsymbol {S} _ {z + 1}\right) - \kappa \log \hat {\pi} _ {\hat {\boldsymbol {\theta}}} \left(\boldsymbol {S} _ {z + 1}\right)\right) - Q _ {\boldsymbol {v} _ {i}} \left(\boldsymbol {S} _ {z}, \boldsymbol {A} _ {z}\right)\right) ^ {2} \left. \right], \tag {40}
$$

where $B _ { z }$ is a mini-batch of transitions sampled from D and $d _ { z + 1 } \in \{ 0 , 1 \}$ is a terminated flag, with $d _ { z + 1 } = 1$ indicating zthat the training episode has ended.

To enhance denoising efficiency, we employ dynamic structured pruning techniques to linear layers of $\xi _ { \theta } ( \cdot , \cdot , \cdot )$ . Considering $\xi _ { \theta } ( \cdot , \cdot , \cdot )$ with H fully connected layers [17], we denote the parameters in the h-th fully connected layer as ${ \pmb \theta } ^ { ( h ) } \in$ $\mathbb { R } ^ { x \times y } , h \in \{ 1 , \ldots , H \}$ . We first calculate the importance of each row in $\bar { \pmb { \theta } } ^ { ( h ) }$ , which is expressed as

$$
\left| \left| \boldsymbol {\theta} _ {i} ^ {(h)} \right| \right| _ {2} = \sqrt {\sum_ {j = 1} ^ {y} \theta_ {i , j} ^ {2}}, i = 1, 2, \dots , x. \tag {41}
$$

Then, we introduce mask matrices $\boldsymbol { W } ^ { ( h ) } \in \mathbb { R } ^ { x \times y }$ to prune fully connected layers with low importance based on the pre-defined pruning rate. The elements of $W ^ { ( h ) } \in \mathbb { R } ^ { x \times y }$ are binary, where $W _ { x } ^ { ( h ) } = 0$ indicates that the output neuron ns otherwise. Hence, the prun $o _ { x } ^ { ( h ) }$ is pruned, whilearameters in the $o _ { x } ^ { ( h ) }$ xh-th fully connected layer are given by

$$
\boldsymbol {\theta} ^ {\prime (h)} = \boldsymbol {\theta} ^ {(h)} \odot \boldsymbol {W} ^ {(h)}, \tag {42}
$$

where $\odot$ represents the Hadamard product [41]. The pruned policy parameters $\pmb { \theta } ^ { \prime }$ can be updated by performing gradient descent algorithms such as Adam, as given by

$$
\boldsymbol {\theta} _ {v + 1} ^ {\prime} \leftarrow \boldsymbol {\theta} _ {v} ^ {\prime} - \eta \nabla_ {\boldsymbol {\theta} _ {v} ^ {\prime}} \mathcal {L} (\boldsymbol {\theta}), \tag {43}
$$

where $\theta _ { v } ^ { \prime }$ are the pruned policy parameters in the v-th training step and $\eta \in ( 0 , 1 ]$ is the learning rate of the actor. Similarly, the parameters of the target policy are also dynamically pruned. During gradient descent, the parameters of the target networks remain frozen and then are updated through a soft update mechanism [20], [21], which is given by

$$
\hat {\boldsymbol {\theta}} _ {v + 1} ^ {\prime} \leftarrow \tau \boldsymbol {\theta} _ {v} ^ {\prime} + (1 - \tau) \hat {\boldsymbol {\theta}} _ {v} ^ {\prime},
$$

$$
\hat {\boldsymbol {v}} _ {i, v + 1} \leftarrow \tau \boldsymbol {v} _ {i, v} + (1 - \tau) \hat {\boldsymbol {v}} _ {i, v}, \text {   for   } i = \{1, 2 \}, \tag {44}
$$

where $\boldsymbol { v } _ { i , v }$ gives the critic parameters in the v-th training step and $\tau \in ( 0 , 1 ]$ is the update rate of the target networks.

Algorithm 1 illustrates the procedure of the EDMSAC algorithm, where its computational complexity primarily consists of three components: In action sampling, the computational overhead arises from environment interaction and the reverse process, with a complexity of $\mathcal { O } ( V Z ( 1 + M | \pmb \theta | ) )$ [20]. In dynamic pruning, the computational overhead is due to the calculations of neuron importance and masking, leading to a complexity of $\begin{array} { r } { \mathcal { O } ( \sum _ { h = 1 } ^ { H } \overset { \cdot } { ( } x ^ { ( h ) } y ^ { ( h ) } + x ^ { ( h ) } \log x ^ { ( \overline { { h } } ) } ) ) } \end{array}$ [41]. In hparameter updates, the computational complexity stems from updating network parameters, given by $\mathcal { O } ( V ( B + 1 ) ( | \pmb { \theta } | +$ $| \pmb { v } | ) )$ [20]. Therefore, the computational complexity of the $\begin{array} { r l } { \mathcal { O } ( V Z ( 1 + M | \pmb { \theta } | ) + \sum _ { h = 1 } ^ { H } ( x ^ { ( h ) } y ^ { ( h ) } + } & { { } } \end{array}$ $x ^ { ( h ) } \log x ^ { ( h ) } \bar { ) } + V ( B + \dot { 1 } ) ( \vert \pmb { \theta } \vert + \vert \pmb { v } \vert ) )$ .

## VI. SIMULATION RESULTS

In this section, we first evaluate the performance of mobile AI agents, where we leverage LLMs called Qwen-VL to construct an AI agent capable of operating a mobile phone to execute various tasks. We then compare the proposed EDMSAC algorithm with several DRL algorithms in optimal dynamic contract design. Finally, we validate the effectiveness of the proposed two-period dynamic contract scheme.

TABLE II SIMULATION PARAMETERS

<table><tr><td>Parameters</td><td>Values</td></tr><tr><td>Number of ESs (N) [37]</td><td>{3,6,12,18}</td></tr><tr><td>Pre-defined hyperparameters (δ,L,ε,λ) [33]</td><td>{0.02,8,2,0.01}</td></tr><tr><td>Constant related to the hardware architecture of ES n (σn) [38]</td><td> $10^{-23}$ </td></tr><tr><td>Number of CPU cycles required for perceiving feature data (YnPer) [33]</td><td>100 cycles/bit</td></tr><tr><td>CPU speed of ES n (fn) [33]</td><td>64 MHz</td></tr><tr><td>Size of feature data perceived by ES n (DnFea) [27]</td><td>1 MB</td></tr><tr><td>Effective switched capacitance of ES n (ρn) [33]</td><td> $10^{-16}$ </td></tr><tr><td>Number of CPU cycles required for creating one bit of agent modules (YnCre) [33]</td><td>120 cycles/bit</td></tr><tr><td>Transmit power of ES n (Pn) [37]</td><td>[20,33] dBm</td></tr><tr><td>Model size of agent modules constructed by ES n (DAgent) [27]</td><td>10 MB</td></tr><tr><td>Transmission rate from ES n to the cloud server through the fiber link (rn,c) [33]</td><td>[1,3] Mbps</td></tr><tr><td>Unit cost of energy consumption (σ) [16]</td><td>[0.5,1]</td></tr><tr><td>Scaling factor that affects the overall magnitude of economic benefits (α) [16]</td><td>{200,250}</td></tr><tr><td>Energy consumption of global AI agent integration (EC) [33]</td><td>[20,25] Joules</td></tr><tr><td>Discount factor (β) [25]</td><td>{0,0.5,1}</td></tr></table>

## A. Experimental Setup

Experiment Settings: We consider ESs with homogeneous hardware capabilities and classify them into two types: high WTP and low WTP [17], [22]. Specifically, $\theta _ { 1 } ^ { t }$ and $\theta _ { 2 } ^ { t }$ are randomly sampled within [15, 20) and [20, 25), respectively [4]. $p _ { k } ^ { 1 }$ and $p _ { k } ^ { \dot { 2 } }$ are randomly generated following the Dirichlet distrik kbution [4]. The setting of simulation parameters is summarized in Table II. For the hyperparameter setting of the EDMSAC algorithm, DM-based actor networks adopt the variance proportional noise schedule strategy [20], where the noise schedule strategy determines the amount of noise injected into input data at each timestep during the forward diffusion process [17]. Both the actor and critic networks are trained using the Adam optimizer, with a weight decay rate of 0.0001 to regularize model weights [20]. The learning rates are set to $2 \times 1 0 ^ { - 7 }$ for the actor networks and $2 \times 1 0 ^ { - 6 }$ for the critic networks, respectively [20]. In addition, the discount factor γ is set to 0.99 [19], the update rate of the target networks τ is set to 0.005 [19], the temperature coefficient κ is set to 0.05 [19], the denoising step M is set to 6 [20], and the pruning rate  is set to 0.5 [17]. Our experiments use PyTorch with CUDA 12.0 on an NVIDIA GeForce RTX 3080 Laptop GPU.

Algorithm Comparisons: To evaluate the performance of the proposed EDMSAC algorithm, we compare it with mainstream DRL algorithms in optimal contract design, and present the core hyperparameter settings used for each algorithm:

![](images/7cf00150924c4eaefb2a34cfb8ad2564bafbf60fb8fa6d1c3f24a21c4591ff29.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["1: Help me log in to Bilibili account"] --> B["2: Select a video at random and like it"]
  B --> C["3: Select random videos using Bilibili accounts"]
  C --> D["4: Select random videos using Bilibili accounts"]
  D --> E["5: Select random videos using Bilibili accounts"]
  E --> F["6: Select random videos using Bilibili accounts"]
  F --> G["7: Select random videos using Bilibili accounts"]
  G --> H["8: Select random videos using Bilibili accounts"]
  H --> I["9: Select random videos using Bilibili accounts"]
  I --> J["10: Select random videos using Bilibili accounts"]
```
</details>

Fig. 4. Two case studies of mobile phone operations based on an AI agent. We call the Qwen-VL-Plus and Qwen-VL-Max models through the Qwen-VL API to construct the mobile AI agent, utilizing Android Debug Bridge (ADB) to operate a mobile phone with the Android OS system, where ADB can simulate all operations of the AI agent [34].

- DMSAC [20]: The DMSAC algorithm does not incorporate the pruning rate. All hyperparameters are kept consistent with those used in the EDMSAC algorithm. It is worth noting that the computational complexity of the DMSAC algorithm is $\mathcal { O } ( V Z ( 1 + M \vert \pmb { \theta } \vert ) + V ( B + 1 ) ( \vert \pmb { \theta } \vert$ $+ | { \boldsymbol { v } } | ) )$ .  
$D M D D P G \ [ I 9 ] { : }$ We set the exploration noise to a fixed Gaussian distribution with zero mean and standard deviation of 0.1. All other basic hyperparameters are the same as those used in the EDMSAC algorithm.  
- $P P O \ [ 2 8 ] { : }$ We apply the tanh activation function as the action bounding method, and set the discount factor γ and the learning rate to 0.95 and $3 \times 1 0 ^ { - 5 }$ , respectively. All other basic hyperparameters are default, which are commonly used in prior literature [28].  
- SAC [22]: We set the learning rate for the temperature coefficient κ to $1 0 ^ { - 4 }$ . The learning rates are set to $1 0 ^ { - 4 }$ for the actor networks and $1 0 ^ { - 3 }$ for the critic networks, respectively. All other basic hyperparameters are the same as those used in the EDMSAC algorithm.  
- $D D P G / I 7 J \mathrm { . }$ We set the learning rates to $1 0 ^ { - 4 }$ for the actor networks and $1 0 ^ { - 3 }$ for the critic networks, respectively. The discount factor γ is set to 0.99. All other basic hyperparameters are the same as those used in the DMDDPG algorithm.

Scheme Comparisons: To evaluate the performance of the proposed dynamic contract scheme, we compare it with other typical contract schemes:

Two-period static contract scheme [25]: This scheme involves executing the static contract twice, and we set $\beta = 0$ to simplify it to a one-stage static contract.  
- Two-period random contract scheme [22]: This scheme randomly generates two-period contracts for ESs. When $\beta \neq 0 ,$ , this scheme operates dynamically across two periods. Conversely, when $\beta = 0$ , this scheme is static.

## B. Practical Implementation Guidelines

We present a practical implementation guideline for the proposed federated AI agent construction framework, investigating how the proposed framework can be closely integrated with the proposed dynamic contract scheme and the EDMSAC algorithm in practical scenarios.

![](images/35276f6e8ef67a24a0953c02c4b9ef56d9af8eba0445894327792ed648e7607a.jpg)

<details>
<summary>stacked bar chart</summary>

| Category | Accuracy (Rounds) | Inaccuracy (Rounds) |
| :--- | :--- | :--- |
| Decision | 10/10 | 0 |
| Reflection | 7/9 | 0 |
| Planning | 6/6 | 0 |
</details>

(a) Case 1.

![](images/36879169a92495caa0721f541c5247d55fb35a386442fea9bde0563d56687fc3.jpg)

<details>
<summary>stacked bar chart</summary>

| Category | Accuracy (Rounds) | Inaccuracy (Rounds) |
| :--- | :--- | :--- |
| Decision | 3 | 4 |
| Reflection | 6 | 1 |
| Planning | 2 | 1 |
</details>

(b) Case 2.  
Fig. 5. Performance evaluation of mobile AI agents.

Infrastructure Initialization: Each ES is equipped with sufficient computing resources (e.g., embedded GPUs) and preloaded with basic AI models from the cloud server. Upon boot-up, ESs establish low-latency communication with the cloud server through fiber links.  
Dynamic Contract Generation: Based on the predicted WTP levels of ESs, the cloud server executes the proposed EDMSAC algorithm to generate the optimal two-period dynamic contract. Then, the cloud server releases the generated dynamic contract to ESs at the beginning of federated AI agent construction.  
- Agent Module Construction: The ESs first select their preferred contract item according to their WTP levels. Following contract confirmation, the ESs construct agent modules using perceived feature data. Then, the ESs upload constructed agent modules to the cloud server. The process can be referred to Section III-A.  
User Interaction Interfaces: The cloud server integrates uploaded modules into complete AI agents and deploys them to ESs. Users can interact with them through intuitive mobile-based interfaces, such as a customized application connected via local IP networks, enabling real-time AI agent services, including personal assistants.

![](images/0845fafd0d64c0a0a7a0f92f72fd58e65ace2c73973f766b6ba0b8ff3c9c731f.jpg)

<details>
<summary>line chart</summary>

| Training Steps | EDMSAC | PPO | SAC | DDPG |
| -------------- | ------ | --- | --- | ---- |
| 0              | ~4.5   | ~4.5 | ~0  | ~-2  |
| 1e5            | ~4.5   | ~4.5 | ~0  | ~-2  |
| 2e5            | ~4.5   | ~4.5 | ~0  | ~-2  |
| 3e5            | ~4.5   | ~4.5 | ~0  | ~-2  |
| 4e5            | ~4.5   | ~4.5 | ~0  | ~-2  |
</details>

(a) EDMSAC vs PPO, SAC,and DDPG.

![](images/2e6491ae68167eb586e47eeb16d257626a6ed2f3892ae46b3f05ebc7023e5aff.jpg)

<details>
<summary>line chart</summary>

| Training Steps | EDMSAC | DMSAC | DMDDPG |
| -------------- | ------ | ----- | ------ |
| 0              | 4.5    | 4.0   | 3.5    |
| 1e5            | 4.8    | 3.8   | 3.4    |
| 2e5            | 4.9    | 3.9   | 3.5    |
| 3e5            | 5.0    | 4.0   | 3.6    |
| 4e5            | 5.1    | 4.1   | 3.7    |
</details>

(b) EDMSAC vs DMSAC and DMDDPG.

![](images/d200dc9b01f284f679175e2049cb7c06366265b4e642e508264f3ef4005fe5b9.jpg)

<details>
<summary>bar chart</summary>

Performance of Generated Dynamic Contracts
| Metric | EDMSAC | PPO | DMSAC | DMDDPG | SAC | DDPG |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Average Test Rewards | 230 | 215 | 185 | 170 | 20 | -110 |
| Total Profit of Cloud Server | 240 | 215 | 205 | 170 | 20 | -110 |
</details>

(c) Performance results.  
Fig. 6. Performance comparisons of the EDMSAC algorithm with several DRL algorithms in optimal dynamic contract design.

## C. Robustness and Security Analysis

Due to its contract-theoretic design and EDMSAC-based optimization, the proposed scheme provides intrinsic robustness and security properties:

1) The IC and IIC constraints of the proposed scheme inherently mitigate strategic misreporting and free-riding behaviors: Since ESs maximize their long-term utilities only by truthfully revealing their WTP levels, any deviation or misreporting leads to a strictly lower expected utility.  
2) The contract realization process across two periods enhances robustness against opportunistic behaviors: The cloud server issues contract-based rewards to the ESs only after successful agent module integration in each period, which discourages non-cooperative actions such as incomplete training.  
3) Uncertainties arising from environments are reflected in the environmental state: The EDMSAC algorithm learns a contract policy that maximizes expected long-term utility, which exhibits robustness to moderate environmental perturbations without requiring explicit failure modeling.

## D. Performance Evaluation of Mobile AI Agents

As illustrated in Fig. 4, we present two case studies in which a mobile AI agent operates a real smartphone to perform tasks. This experiment involves the distributed execution of agent modules, as well as task decomposition and coordination during execution. For the perception module, we leverage Qwen-VL-Plus to create it, and we use the ConvNextViT-document model and the GroundingDINO model as text and icon recognition tools, respectively [34]. For the decision-making, reflection, and planning modules, we leverage Qwen-VL-Max to create them. To evaluate the performance of the constructed AI agent, we adopt several evaluation metrics: Decision Accuracy (DA), which measures the accuracy of the decision-making module; Reflection Accuracy (RA), which assesses the accuracy of the reflection module; and Planning Accuracy (PA), which evaluates the accuracy of the planning module. As shown in Fig. 5, the performance of the AI agent in executing simple tasks, such as Case 1, is superior to that in handling more complex tasks, as in Case 2, as evidenced by higher values of DA, RA, and PA.

![](images/9a43cf0b7835c23e00a75545b55e6c58db833c2a2735ae6e52f6dfe015ca215e.jpg)

<details>
<summary>radar chart</summary>

| Metric | Inference (*1000) | Training |
|--------|-------------------|----------|
| Time (h) | 4.7 | 5.5 |
| CO₂ (kg) | 0.12 | 0.23 |
| CPU (kWh) | 0.071 | 0.12 |
| GPU (kWh) | 0.071 | 0.15 |
| RAM (kWh) | 0.037 | 0.066 |
</details>

Fig. 7. The resource consumption of the proposed EDMSAC algorithm for performing one training and multiple inferences.

Notably, when executing simple tasks, the AI agent may perform additional rounds to verify task completion, leading to increased service latency.

## E. Performance Evaluation of the EDMSAC Algorithm

In Fig. 6, we present a performance comparison between the proposed EDMSAC algorithm and several representative DRL algorithms in optimal contract design, including DMSAC, DMDDPG, PPO, SAC, and DDPG. From Fig. 6(a) and (b), we observe that the proposed EDMSAC algorithm outperforms these DRL algorithms in optimal dynamic contract design because DRL algorithms struggle in different suboptimal solution spaces, especially PPO algorithms. The superior performance of the proposed EDMSAC algorithm can be primarily attributed to two key reasons. First, the EDMSAC algorithm has a strong capability to capture complex environmental information because of GDMs [19], which helps avoid the identification of suboptimal dynamic contracts. Moreover, its fine-grained policy tuning mitigates the impact of environmental randomness, enhancing decision robustness. Second, through structural pruning techniques, the unimportant neurons in the DM-based actor networks are masked rather than permanently removed, thereby preserving the network structure while reducing computational redundancy. Therefore, the EDMSAC algorithm can achieve higher denoising efficiency, enabling the generation of more optimal and stable dynamic contracts. From Fig. 6(c), we also observe that the EDMSAC algorithm achieves a higher total profit of the cloud server compared with other DRL algorithms. Overall, the above analysis demonstrates the effectiveness and superiority of the proposed EDMSAC algorithm in optimizing dynamic contract design, which enhances the system performance of federated AI agent construction under dynamic information asymmetry.

![](images/80531acdaf21cb3ab6097bdba72d793fae259951634ce9013f159496e6048a0c.jpg)

<details>
<summary>line chart</summary>

| Training Steps (×10⁵) | Pruning rate = 0.7 Test Rewards | Pruning rate = 0.5 Test Rewards | Pruning rate = 0.3 Test Rewards | Total Profit of the Cloud Server |
| ---------------------- | -------------------------------- | ------------------------------- | ------------------------------- | -------------------------------- |
| 0                      | ~5.2 × 10⁴                       | ~4.9 × 10⁴                     | ~4.5 × 10⁴                     | 215.36                           |
| 1                      | ~5.5 × 10⁴                       | ~5.0 × 10⁴                     | ~4.7 × 10⁴                     | 243.68                           |
| 2                      | ~5.7 × 10⁴                       | ~5.2 × 10⁴                     | ~4.9 × 10⁴                     | 254.68                           |
| 3                      | ~5.8 × 10⁴                       | ~5.3 × 10⁴                     | ~5.0 × 10⁴                     | -                                |
| 4                      | ~5.9 × 10⁴                       | ~5.4 × 10⁴                     | ~5.1 × 10⁴                     | -                                |
</details>

(a) Pruning rates.

![](images/b9dd5ca16aa2b2e9bcc700b5c8f996f8dbf7b8fecae121f63fc0ee8201ec4fe2.jpg)

<details>
<summary>line chart</summary>

| Training Steps | Test Rewards (×10⁴) | Total Profit of the Cloud Server |
| -------------- | ------------------- | --------------------------------- |
| 3              | 4.8                 | 255.06                            |
| 4              | 4.8                 | 243.68                            |
| √2             | 4.8                 | 226.5                             |
</details>

(b) Denoising steps.

![](images/c80a98de54e6670e719fc94adbc6a41d716c0efa9d4ba9c83388b583783e9dad.jpg)

<details>
<summary>line chart</summary>

| Training Steps (×10⁵) | Test Rewards (×10⁴) | Total Profit of the Cloud Server |
| --------------------- | ------------------- | --------------------------------- |
| LR1                   | ~4.5                | 203.79                            |
| LR2                   | ~4.8                | 243.68                            |
</details>

(c) Learning rates.

Fig. 8. Performance of the EDMSAC algorithm in optimal dynamic contract design under critical hyperparameter settings, where the optimal value corresponding to the optimal hyperparameter is marked in red.  
![](images/5149029f328f55adfbe3c7c0b5e18805bc1731de758cb1d1521c55ad6f83b676.jpg)

<details>
<summary>bar chart</summary>

| Period | Type-1 contract item: T₁ | Type-1 contract item: R₁ | Type-2 contract item: T₂ | Type-2 contract item: R₂ |
| :--- | :--- | :--- | :--- | :--- |
| Period 1 | 30.15 | 42.93 | 33.74 | 51.89 |
| Period 2 | 28.73 | 51.90 | 45.28 | 73.63 |
</details>

(a) State 1.

![](images/8084eeb16c0c67b47ef566a757516415bd522c362c1a4ec39ea53c75dca0509f.jpg)

<details>
<summary>bar chart</summary>

| Period   | Type-1 contract item: T₁ | Type-1 contract item: R₁ | Type-2 contract item: T₂ | Type-2 contract item: R₂ |
| -------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| Period 1 | 30.23                    | 43.65                    | 48.03                    | 86.20                    |
| Period 2 | 27.52                    | 42.22                    | 44.75                    | 60.98                    |
</details>

(b) State 2.

![](images/87defa58db9fcddedbaf5bab4c02280f7abaf11e256ca7da965be709ae4cef0a.jpg)

<details>
<summary>bar chart</summary>

| Period   | Type-1 contract item: T₁ | Type-1 contract item: R₁ | Type-2 contract item: T₂ | Type-2 contract item: R₂ |
| -------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| Period 1 | 25.61                    | 46.04                    | 50.65                    | 124.46                   |
| Period 2 | 36.26                    | 81.58                    | 74.54                    | 133.86                   |
</details>

(c) State 3.

Fig. 9. Two-period dynamic contracts generated by the EDMSAC algorithm under three network states.  
![](images/c78ee038ed6dc11914898d2ee690c43c5eae8ebac1c4aa55ceef78ceb7d1e93c.jpg)

<details>
<summary>line chart</summary>

| Training Epochs | Our scheme | Two-period random dynamic contract | Two-period static contract | Two-period random static contract |
| --------------- | ---------- | ---------------------------------- | -------------------------- | --------------------------------- |
| 0               | 4.3e4      | 3.5e4                              | 2.2e4                      | 1.6e4                             |
| 100             | 4.7e4      | 3.8e4                              | 2.6e4                      | 1.7e4                             |
| 200             | 4.8e4      | 3.9e4                              | 2.7e4                      | 1.7e4                             |
| 300             | 4.9e4      | 3.9e4                              | 2.7e4                      | 1.7e4                             |
| 400             | 5.0e4      | 3.9e4                              | 2.7e4                      | 1.7e4                             |
</details>

(a) Test reward comparison between the proposed scheme and three baseline contract schemes.

![](images/60275d29d42269f1a90a8fb6d00d55c8e516892cba2f58616abfe9327dcd1682.jpg)

<details>
<summary>bar chart</summary>

| Number of ESs | Our scheme | Two-period random dynamic contract | Two-period static contract | Two-period random static contract |
| ------------- | ---------- | ----------------------------------- | -------------------------- | --------------------------------- |
| 3             | 120        | 80                                  | 60                         | 40                                |
| 6             | 250        | 170                                 | 150                        | 80                                |
| 12            | 530        | 370                                 | 330                        | 170                               |
| 18            | 850        | 560                                 | 520                        | 260                               |
</details>

(b)Relationship between the total profit of the cloud server and the number of ESs.

![](images/d3c337c38117ca08b405a50ce79b6c17f45762ae64f7aec70f59e151f4d80035.jpg)

<details>
<summary>line chart</summary>

| Number of ESs | α = 200; β = 0.5 | α = 250; β = 0.5 | α = 200; β = 1.0 | α = 250; β = 1.0 |
| ------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| 0             | 0                | 0                | 0                | 0                |
| 20            | ~1000            | ~2000            | ~1500            | ~3500            |
| 40            | ~2000            | ~4500            | ~3500            | ~6500            |
| 60            | ~3000            | ~7000            | ~5000            | ~9500            |
| 80            | ~4000            | ~9500            | ~6500            | ~12500           |
| 100           | ~5000            | ~11500           | ~7500            | ~14500           |
| 120           | ~6000            | ~14500           | ~8500            | ~15500           |
</details>

(c) Impacts of α and β on the total profit of the cloud server under different numbers of ESs.  
Fig. 10. Performance evaluation of the proposed two-period dynamic contract scheme.

In Fig. 7, we employ the Python package named CodeCarbon2 to estimate the resource consumption of the proposed EDMSAC algorithm for one training session and 20 inference runs. The evaluation considers five dimensions: time (h), CO2 (kg), CPU (kWh), GPU (kWh), and random access memory (kWh). To enhance clarity, we scale the inference results of all five metrics by a factor of 1000. We observe that all metrics for one training session are significantly higher than those for 20 inference sessions. Especially, the total carbon emissions for performing 20 inferences are only 0.123 g. The reason is that the structural pruning

2https://github.com/mlco2/codecarbon

technique can improve computational efficiency of the denoising process, thereby reducing total carbon emissions. These findings indicate the environmental sustainability of the proposed EDM-SAC algorithm in optimal dynamic contract design.

As shown in Fig. 8, we present the performance of the EDMSAC algorithm in optimal dynamic contract design with different hyperparameter configurations. Fig. 8(a) illustrates the performance of the EDMSAC algorithm under different pruning rates, i.e., 30%, 50%, and 70%. We observe that the EDMSAC algorithm demonstrates superior performance under higher pruning rates, leading to faster convergence and higher test rewards. The reason is that a higher pruning rate indicates that more redundant and unimportant neurons in DM-based actor networks are structurally masked. As a result, the pruned DMbased actor networks exhibit better generalization capabilities and are more effective at learning essential features in optimal dynamic contract design. Fig. 8(b) presents the performance of the EDMSAC algorithm under different denoising steps, i.e., 3, 6, and 12. We observe that the EDMSAC algorithm achieves faster convergence and yields higher total profits for the cloud server under a smaller denoising step. The reason is that a smaller denoising step can achieve higher computational efficiency of DM-based actor networks. Fig. 8(c) illustrates the performance of the EDMSAC algorithm under two groups of different learning rates. The first group is the actor networks with a learning rate of $2 \times 1 0 ^ { - 7 }$ and the critic networks with a learning rate of $2 \times 1 0 ^ { - 6 }$ . The second group is the actor networks and critic networks with the same learning rate of $1 0 ^ { - 4 }$ . We observe that the EDMSAC algorithm has better performance under the first group of learning rates, indicating that the pruned actor networks need to learn an efficient policy in optimal dynamic contract design under small learning rates.

## F. Performance Evaluation of the Dynamic Contract Scheme

In Fig. 9, we illustrate the two-period dynamic contracts generated by the EDMSAC algorithm under three network states, with a pruning rate of 0.5 and a denoising step of 6. Additionally, the learning rates of the actor and critic networks are set to $2 \times 1 0 ^ { - 7 }$ and $2 \times 1 0 ^ { - 6 }$ , respectively. Attributed to the exploration and generalization capabilities of GDMs, the proposed EDMSAC algorithm demonstrates the capability to generate optimal dynamic contracts across varying network states, indicating that our algorithm possesses strong adaptability and generalization abilities to the dynamic environments inherent in federated AI agent construction, thereby ensuring robust system performance in mobile metaverses. We observe that in period 2, the ESs with higher types perform more training rounds $T _ { 2 } ^ { k }$ for agent module creation and consequently receive higher rewards $R _ { 2 } ^ { k }$ , which validates Lemmas 1 and 2, respectively. In period 1, the ESs with higher types also perform more training rounds $T _ { i } ^ { k }$ for agent module creation and receive higher rewards $R _ { i } ^ { k }$ i, which demonstrates Lemmas 7 and 8, respectively.

In Fig. 10, we compare the proposed two-period dynamic contract scheme with three baseline contract schemes. Fig. 10(a) presents the test reward comparison between the proposed scheme and three baseline contract schemes. Our dynamic contract scheme consistently achieves higher test rewards compared with the other three contract schemes, indicating that the proposed two-period dynamic contract scheme possesses superior performance. In addition, the test rewards obtained by dynamic contract schemes consistently surpass those of static contract schemes, highlighting the advantages of incorporating adaptability in contract design. The reason is that, unlike static contract schemes, dynamic contract schemes take into account the profit of the cloud server in the second period. As a result, the total profit of the cloud server achieved under the dynamic contract scheme is higher than that of the static contract scheme. Fig. 10(b) illustrates the relationship between the total profit of the cloud server and varying numbers of ESs under four contract schemes. No matter which contract scheme, as the number of ESs increases, the total profit of the cloud server also increases. Moreover, compared with the three baseline contract schemes, the proposed two-period dynamic contract scheme can achieve the highest total profit for the cloud server. This is primarily because the proposed scheme is capable of designing suitable contracts for ESs based on their respective types rather than generating contracts randomly, which enables more effective resource utilization for federated AI agent construction and contributes to higher total profits for the cloud server. Fig. 10(c) presents the impacts of the scaling factor α and the discount factor $\beta$ on the total profit of the cloud server under different numbers of ESs. When $\beta$ remains constant, the total profit of the cloud server increases with the rise of α. The reason is that a larger α reflects a greater overall magnitude of economic benefits allocated to the cloud server, thereby enhancing its total profit. In addition, when α remains constant, the total profit of the cloud server increases as $\beta$ increases. This is primarily because the cloud server obtains higher profits in the second period of federated AI agent construction, thus enhancing its total profit.

## VII. CONCLUSION AND FUTURE WORK

In this paper, we have studied federated AI agent construction in mobile metaverses. Specifically, we have proposed an edge-cloud collaboration-based federated AI agent construction framework in mobile metaverses. In this framework, ESs serve as agent infrastructures to construct agent modules in a distributed manner, and the cloud server subsequently integrates them into complete AI agents and deploys the constructed AI agents at the edge, thereby providing AI agent services for users in mobile metaverses. Considering the dynamic information asymmetry in federated AI agent construction, we have designed a two-period dynamic contract model to incentivize ESs to continuously participate in federated AI agent construction. Furthermore, to effectively identify optimal dynamic contracts, we have proposed the EDMSAC algorithm, in which the redundant neurons of DM-based actor networks are dynamically pruned, thereby enhancing denoising efficiency for dynamic contract sampling. Extensive simulations have demonstrated that the proposed EDMSAC can achieve up to a 23% improvement over the DMSAC algorithm in optimal dynamic contract generation. For future work, we aim to develop a mobile AI agent paradigm built upon the proposed framework, which will empower AI agents with enhanced adaptability and decision-making capabilities in real-world mobile environments. Furthermore, we plan to build a working prototype using real edge devices to transform the proposed framework into a deployable system.

## REFERENCES

[1] X. Ren et al., “Dual-level resource provisioning and heterogeneous auction for mobile metaverse,” IEEE Trans. Mobile Comput., vol. 23, no. 11, pp. 10329–10343, Nov. 2024.  
[2] M. Xu et al., “A full dive into realizing the edge-enabled metaverse: Visions, enabling technologies, and challenges,” IEEE Commun. Surv. Tut., vol. 25, no. 1, pp. 656–700, First Quarter, 2023.  
[3] J. Liu et al., “Optimizing resource allocation for multi-modal semantic communication in mobile AIGC networks: A diffusion-based game approach,” IEEE Trans. Cogn. Commun. Netw., vol. 11, no. 5, pp. 3346–3360, Oct. 2025.  
[4] J. Wen et al., “From generative AI to generative Internet of Things: Fundamentals, framework, and outlooks,” IEEE Internet Things Mag., vol. 7, no. 3, pp. 30–37, May 2024.  
[5] Z. Durante et al., “Agent AI: Surveying the horizons of multimodal interaction,” 2024, arXiv:2401.03568.  
[6] C. Zhang et al., “Proagent: Building proactive cooperative agents with large language models,” in Proc. AAAI Conf. Artif. Intell., 2024, pp. 17591–17599.  
[7] Y. Siriwardhana, P. Porambage, M. Liyanage, and M. Ylianttila, “A survey on mobile augmented reality with 5G mobile edge computing: Architectures, applications, and technical aspects,” IEEE Commun. Surv. Tut., vol. 23, no. 2, pp. 1160–1192, Second Quarter, 2021.  
[8] K. Peng et al., “Large-scale service mesh orchestration with probabilistic routing in cloud data centers,” IEEE Trans. Serv. Comput., vol. 18, no. 2, pp. 868–882, Mar./Apr. 2025.  
[9] V.-L. Nguyen, P.-C. Lin, B.-C. Cheng, R.-H. Hwang, and Y.-D. Lin, “Security and privacy for 6G: A survey on prospective technologies and challenges,” IEEE Commun. Surv. Tut., vol. 23, no. 4, pp. 2384–2428, Fourth Quarter, 2021.  
[10] J. Kang et al., “Blockchain-empowered federated learning for healthcare metaverses: User-centric incentive mechanism with optimal data freshness,” IEEE Trans. Cogn. Commun. Netw., vol. 10, no. 1, pp. 348–362, Feb. 2024.  
[11] W. Sun, S. Lei, L. Wang, Z. Liu, and Y. Zhang, “Adaptive federated learning and digital twin for industrial Internet of Things,” IEEE Trans. Ind. Informat., vol. 17, no. 8, pp. 5605–5614, Aug. 2021.  
[12] W. Yang, W. Xiang, Y. Yang, and P. Cheng, “Optimizing federated learning with deep reinforcement learning for digital twin empowered industrial IoT,” IEEE Trans. Ind. Informat., vol. 19, no. 2, pp. 1884–1893, Feb. 2023.  
[13] B. Jiang, J. Du, C. Jiang, Z. Han, A. Alhammadi, and M. Debbah, “Overthe-air federated learning in digital twins empowered UAV swarms,” IEEE Trans. Wireless Commun., vol. 23, no. 11, pp. 17619–17634, Nov. 2024.  
[14] P. Consul, I. Budhiraja, D. Garg, N. Kumar, R. Singh, and A. S. Almogren, “A hybrid task offloading and resource allocation approach for digital twinempowered UAV-assisted MEC network using federated reinforcement learning for future wireless network,” IEEE Trans. Consum. Electron., vol. 70, no. 1, pp. 3120–3130, Feb. 2024.  
[15] Z. Yang, M. Chen, W. Saad, C. S. Hong, and M. Shikh-Bahaei, “Energy efficient federated learning over wireless communication networks,” IEEE Trans. Wireless Commun., vol. 20, no. 3, pp. 1935–1949, Mar. 2021.  
[16] W. Y. B. Lim et al., “Dynamic contract design for federated learning in smart healthcare applications,” IEEE Internet Things J., vol. 8, no. 23, pp. 16853–16862, Dec. 2021.  
[17] J. Wen, J. Kang, D. Niyato, Y. Zhang, and S. Mao, “Sustainable diffusionbased incentive mechanism for generative AI-driven digital twins in industrial cyber-physical systems,” IEEE Trans. Ind. Cyber- Phys. Syst., vol. 3, pp. 139–149, 2025.  
[18] I. Lotfi, D. Niyato, S. Sun, D. I. Kim, and X. Shen, “Semantic information marketing in the metaverse: A learning-based contract theory framework,” IEEE J. Sel. Areas Commun., vol. 42, no. 3, pp. 710–723, Mar. 2024.  
[19] H. Du et al., “Enhancing deep reinforcement learning: A tutorial on generative diffusion models in network optimization,” IEEE Commun. Surv. Tut., vol. 26, no. 4, pp. 2611–2646, Fourth Quarter, 2024.  
[20] H. Du et al., “Diffusion-based reinforcement learning for edge-enabled AI-generated content services,” IEEE Trans. Mobile Comput., vol. 23, no. 9, pp. 8902–8918, Sep. 2024.  
[21] Z. Wang, J. J. Hunt, and M. Zhou, “Diffusion policies as an expressive policy class for offline reinforcement learning,” in Proc. Int. Conf. Learn. Representations, 2023.  
[22] J. Wen et al., “Diffusion-model-based incentive mechanism with prospect theory for edge AIGC services in 6G IoT,” IEEE Internet Things J., vol. 11, no. 21, pp. 34187–34201, Nov. 2024.  
[23] S. Wang, W. Xia, H. Zhao, Y. Ni, C. Zhu, and H. Zhu, “Incentivizing federated learning with contract theory under strong information asymmetry,” in Proc. 2024 IEEE Wireless Commun. Netw. Conf., 2024, pp. 1–6.  
[24] S. M. A. Kazmi et al., “A novel contract theory-based incentive mechanism for cooperative task-offloading in electrical vehicular networks,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 7, pp. 8380–8395, Jul. 2022.  
[25] C. He, Y. Wang, J. Hu, T. H. Luan, Y. Bi, and Z. Su, “Collaborative vehicular threat sharing: A long-term contract-based incentive mechanism with privacy preservation,” IEEE Trans. Intell. Transp. Syst., vol. 25, no. 12, pp. 21528–21544, Dec. 2024.  
[26] Z. Xiong, J. Kang, D. Niyato, P. Wang, H. V. Poor, and S. Xie, “A multi-dimensional contract approach for data rewarding in mobile networks,” IEEE Trans. Wireless Commun., vol. 19, no. 9, pp. 5779–5793, Sep. 2020.  
[27] Y. Zhong et al., “Generative diffusion-based contract design for efficient AI twin migration in vehicular embodied AI networks,” IEEE Trans. Mobile Comput., vol. 24, no. 5, pp. 4573–4588, May 2025.  
[28] J. Wen et al., “Learning-based Big Data sharing incentive in mobile AIGC networks,” in Proc. 2024 IEEE Glob. Commun. Conf., 2024, pp. 3667–3672.  
[29] N. Zhao, Y. Pei, Y.-C. Liang, and D. Niyato, “A deep reinforcement learning-based contract incentive mechanism for mobile crowdsourcing networks,” IEEE Trans. Veh. Technol., vol. 73, no. 3, pp. 4511–4516, Mar. 2024.  
[30] W. Shen, M. Ye, W. Yu, and P. C. Yuen, “Build yourself before collaboration: Vertical federated learning with limited aligned samples,” IEEE Trans. Mobile Comput., vol. 24, no. 7, pp. 6503–6516, Jul. 2025.  
[31] A. M. Rahmani, J. Tanveer, F. S. Gharehchopogh, S. Rajabi, and M. Hosseinzadeh, “A novel offloading strategy for multi-user optimization in blockchain-enabled mobile edge computing networks for improved Internet of Things performance,” Comput. Elect. Eng., vol. 119, 2024, Art. no. 109514.  
[32] A. M. Rahmani et al., “An optimizing geo-distributed edge layering with double deep Q-networks for predictive mobility-aware offloading in mobile edge computing,” Ad Hoc Netw., vol. 172, 2025, Art. no. 103804.  
[33] R. Chen, C. Yi, F. Zhou, J. Kang, Y. Wu, and D. Niyato, “Federated digital twin construction via distributed sensing: A game-theoretic online optimization with overlapping coalitions,” IEEE Trans. Mobile Comput., vol. 24, no. 11, pp. 12221–12238, Nov. 2025.  
[34] J. Wang et al., “Mobile-agent-v2: Mobile device operation assistant with effective navigation via multi-agent collaboration,” in Proc. Adv. Neural Inf. Process. Syst., 2024, pp. 2686–2710.  
[35] L. Zhang, T. Zhao, H. Ying, Y. Ma, and K. Lee, “OmAgent: A multi-modal agent framework for complex video understanding with task divide-andconquer,” 2024, arXiv:2406.16620.  
[36] H. Li et al., “Collaborative federated learning of unmanned aerial vehicles in space-air-ground integrated network,” Space: Sci. Technol. (United States), vol. 5, 2025, Art. no. 0264.  
[37] Z. Xu et al., “Energy or accuracy? Near-optimal user selection and aggregator placement for federated learning in MEC,” IEEE Trans. Mobile Comput., vol. 23, no. 3, pp. 2470–2485, Mar. 2024.  
[38] C. Ding, J.-B. Wang, H. Zhang, M. Lin, and G. Y. Li, “Joint MIMO precoding and computation resource allocation for dual-function radar and communication systems with mobile edge computing,” IEEE J. Sel. Areas Commun., vol. 40, no. 7, pp. 2085–2102, Jul. 2022.  
[39] K. Moghaddasi, S. Rajabi, and F. S. Gharehchopogh, “An enhanced asynchronous advantage actor-critic-based algorithm for performance optimization in mobile edge computing-enabled internet of vehicles networks,” Peer-to-Peer Netw. Appl., vol. 17, no. 3, pp. 1169–1189, 2024.  
[40] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” in Proc. Adv. Neural Inf. Process. Syst., 2020, pp. 6840–6851.  
[41] J. Kang et al., “Tiny multiagent DRL for twins migration in UAV metaverses: A multileader multifollower stackelberg game approach,” IEEE Internet Things J., vol. 11, no. 12, pp. 21021–21036, Jun. 2024.

![](images/029e8aae77147611fa64ff4f0016ffc44e15f13b102c7e65843aa791e872bff7.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a young man in formal attire against a blue background (no text or symbols visible)
</details>

Jinbo Wen (Graduate Student Member, IEEE) received the BEng degree from the Guangdong University of Technology, Guangzhou, China, in 2023. He is currently working toward the MS degree with the College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, China. His research interests include generative AI for networking, incentive mechanism design, blockchain, and the metaverse.

![](images/6deb3609f2d4231d0d7e0787ca4a8d3720e9c90851577322aff411a9bc59f990.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in a dark polo shirt (no text or symbols visible)
</details>

Jie Xu (Fellow, IEEE) received the BEng and PhD degrees from the University of Science and Technology of China. He is currently an associate professor (Tenured) with the School of Science and Engineering, Shenzhen Future Network of Intelligence Institute (FNii-Shenzhen), and Guangdong Provincial Key Laboratory of Future Networks of Intelligence, The Chinese University of Hong Kong (Shenzhen). His research interests include wireless communications, wireless information and power transfer, UAV communications, edge computing and intelligence,

and integrated sensing and communication (ISAC).

![](images/dfde127d306f640f27401edcc60a5879faede6a5e6296494a5c595c9788860f1.jpg)

<details>
<summary>natural_image</summary>

Portrait of a young man wearing glasses and a black polo shirt against a blue background (no text or symbols visible)
</details>

Jiawen Kang (Senior Member, IEEE) received the PhD degree from the Guangdong University of Technology, Guangzhou, China, in 2018. He was a postdoc with Nanyang Technological University, Singapore, from 2018 to 2021. He is currently a full professor with the Guangdong University of Technology, Guangzhou, China. His research interests mainly focus on generative AI, blockchain, security, and privacy protection in wireless communications and networking.

![](images/23d9ec35e3cc5389fcc6b50adc42f18ab41fc75c10c57050148f666d8be3f687.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in formal attire against a blue background (no text or symbols visible)
</details>

Jianhang Tang (Member, IEEE) received the MS degree in applied statistics from Lanzhou University, Lanzhou, China, in 2015, and the PhD degree in computer science and technology from the Wuhan University of Technology, Wuhan, China, in 2021. He is currently a professor with the State Key Laboratory of Public Big Data, Guizhou University, Guiyang, China. From 2021 to 2022, he was a lecturer with the School of Information Science and Engineering, Yanshan University, Qinhuangdao, China. His research interests include edge computing-assisted

AIGC, edge intelligence, and the Metaverse.

![](images/204489a14a40bcbb55a707d0398022613a6bf9513b920b2dcc2b6f530ae8d511.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man against a solid blue background (no text or symbols visible)
</details>

Yang Zhang received the BEng and MEng degrees from Beihang University, in 2008 and 2011, respectively, and the PhD degree in computer engineering from Nanyang Technological University, Singapore, in 2015. He is currently an associate professor in the College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing, China. He is an editor of the IEEE Transactions on Machine Learning in Communications and Networking. His current research topic is edge computing and multi-agent autonomous systems.

![](images/33382fd55069e06ca863c6cabbd574fa945f2bf9d9f78ec719ca1ae5d7775c1e.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a striped shirt (no text or symbols visible)
</details>

Chau Yuen (Fellow, IEEE) received the BEng and PhD degrees from Nanyang Technological University, Singapore, in 2000 and 2004, respectively. He was a post-doctoral fellow with Lucent Technologies Bell Labs, Murray Hill, in 2005. From 2006 to 2010, he was with the Institute for Infocomm Research, Singapore. From 2010 to 2023, he was with the Engineering Product Development Pillar, Singapore University of Technology and Design. Since 2023, he has been with the School of Electrical and Electronic Engineering, Nanyang Technological University. He

![](images/34b6bc1f76ac56a826b42046405d19f88bed4e879be385f6c2f2ea6351d8fdeb.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a woman in formal attire (no visible text or symbols)
</details>

Yue Zhong received the BEng degree from the Guangdong University of Technology, Guangzhou, China, in 2024. She is currently working toward the MS degree with the School of Automation, Guangdong University of Technology, Guangzhou, China. Her research interests include game theory, contract theory, and embodied AI.

is the Provost’s Chair in Wireless Communications, assistant dean in Graduate College, and cluster director for Sustainable Built Environment with ER@IN. He received IEEE Communications Society Leonard G. Abraham Prize (2024), IEEE Communications Society Best Tutorial Paper Award (2024), IEEE Communications Society Fred W. Ellersick Prize (2023), IEEE Marconi Prize Paper Award in Wireless Communications (2021), IEEE APB Outstanding Paper Award (2023), and EURASIP Best Paper Award for Journal on Wireless Communications and Networking (2021). He currently serves as editor-in-chief for Springer Nature Computer Science, editor for IEEE Transactions on Vehicular Technology, IEEE Transactions on Neural Networks and Learning Systems, and IEEE Transactions on Network Science and Engineering, where he was awarded as IEEE TNSE excellent editor award 2024 and 2022, and Top associate editor for TVT from 2009 to 2015. He also served as the guest editor for several special issues, including IEEE Journal on Selected Areas in Communications, IEEE Wireless Communications, IEEE Communications Magazine, IEEE Vehicular Technology Magazine, and IEEE Transactions on Cognitive Communications and Networking. He is listed as a Top 2% scientist by Stanford University, and also a Highly Cited Researcher by Clarivate Web of Science from 2022. He has 4 US patents and has published more than 700 research papers.

![](images/80aba3bff0d031870ba12cfc0cf2e2b9cc544f5df6cbcf112b6f6982a7274748.jpg)

<details>
<summary>natural_image</summary>

Portrait of a person wearing glasses and a dark jacket (no visible text or symbols)
</details>

Dusit Niyato (Fellow, IEEE) received the BEng degree from the King Mongkut’s Institute of Technology Ladkrabang (KMITL), Thailand, and the PhD degree in electrical and computer engineering from the University of Manitoba, Canada. He is a professor in the College of Computing and Data Science, Nanyang Technological University, Singapore. His research interests are in the areas of mobile generative AI, edge general intelligence, quantum computing and networking, and incentive mechanism design.