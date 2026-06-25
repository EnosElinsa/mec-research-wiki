# Enhancing Deep Reinforcement Learning: A Tutorial on Generative Diffusion Models in Network Optimization

Hongyang Du , Graduate Student Member, IEEE, Ruichen Zhang , Member, IEEE, Yinqiu Liu , Jiacheng Wang , Yijing Lin , Graduate Student Member, IEEE, Zonghang Li , Dusit Niyato , Fellow, IEEE, Jiawen Kang , Senior Member, IEEE, Zehui Xiong , Senior Member, IEEE, Shuguang Cui , Fellow, IEEE, Bo Ai , Fellow, IEEE, Haibo Zhou , Senior Member, IEEE, and Dong In Kim , Fellow, IEEE

Abstract—Generative Diffusion Models (GDMs) have emerged as a transformative force in the realm of Generative Artificial Intelligence (GenAI), demonstrating their versatility and efficacy across various applications. The ability to model complex data distributions and generate high-quality samples has made GDMs particularly effective in tasks such as image generation and reinforcement learning. Furthermore, their iterative nature, which involves a series of noise addition and denoising steps, is a powerful and unique approach to learning and generating data. This paper serves as a comprehensive tutorial on applying GDMs in network optimization tasks. We delve into the strengths of GDMs, emphasizing their wide applicability across various domains, such as vision, text, and audio generation. We detail how GDMs can be effectively harnessed to solve complex optimization

Manuscript received 9 August 2023; revised 15 January 2024 and 28 April 2024; accepted 6 May 2024. Date of publication 10 May 2024; date of current version 22 November 2024. This work was supported in part by the National Research Foundation of Korea (NRF) Grant funded by the Korean Government (MSIT) under Grant 2021R1A2C2007638; in part by MSIT through the ICT Creative Consilience Program supervised by the Institute for ICT Planning and Evaluation (IITP) under Grant IITP-2020-0-01821; in part by the National Natural Science Foundation of China (NSFC) under Grant 62102099, Grant U22A2054, Grant 62221001, Grant 62341127, Grant 62271244, and Grant 62293482; in part by the Pearl River Talent Recruitment Program under Grant 2021QN02S643; in part by the Basic Research Project through the Hetao Shenzhen-HK S&T Cooperation Zone under Grant HZQB-KCZYZ-2021067; in part by the Shenzhen Outstanding Talents Training Fund under Grant 202002; in part by the Guangdong Research Project under Grant 2017ZT07X152 and Grant 2019CX01X104; in part by the Guangdong Provincial Key Laboratory of Future Networks of Intelligence under Grant 2022B1212010001; in part by the Shenzhen Key Laboratory of Big Data and Artificial Intelligence under Grant ZDSYS201707251409055; in part by the National Key Research and Development Program under Grant 2021YFB2900301l; in part by the National Natural Science Foundation Original Exploration Project of China under Grant 62250004; in part by the Natural Science Fund for Distinguished Young Scholars of Jiangsu Province under Grant BK20220067; in part by the High-Level Innovation and Entrepreneurship Talent Introduction Program Team of Jiangsu Province under Grant JSSCTD202202; in part by the National Research Foundation (NRF), Singapore, and Infocomm Media Development Authority under its Future Communications Research and Development Programme (FCP), DSO National Laboratories through the AI Singapore Programme (AISG) under Award AISG2-RP-2020-019 and Grant FCP-ASTAR-TG-2022-003, and through MOE Tier 1 under Grant RG87/22; in part by SUTD under Grant SRG-ISTD-2021-165; in part by SUTD-ZJU IDEA Grant under Grant SUTD-ZJU (VP) 202102; in part by the Ministry of Education, Singapore, under its SMU-SUTD Joint Grant under Grant 22-SIS-SMU-048; and in part by the SUTD Kickstarter Initiative (SKI) under Grant 20210204. (Hongyang Du, Ruichen Zhang, Yinqiu Liu, Jiacheng Wang, Yijing Lin, and Zonghang Li contributed equally to this work.) (Corresponding author: Dong In Kim.)

Please see the Acknowledgment section of this article for the author affiliations.

Digital Object Identifier 10.1109/COMST.2024.3400011

problems inherent in networks. The paper first provides a basic background of GDMs and their applications in network optimization. This is followed by a series of case studies, showcasing the integration of GDMs with Deep Reinforcement Learning (DRL), incentive mechanism design, Semantic Communications (SemCom), Internet of Vehicles (IoV) networks, etc. These case studies underscore the practicality and efficacy of GDMs in real-world scenarios, offering insights into network design. We conclude with a discussion on potential future directions for GDM research and applications, providing major insights into how they can continue to shape the future of network optimization.

Index Terms—Diffusion model, deep reinforcement learning, generative AI, AI-generated content, network optimization.

# I. INTRODUCTION

# A. Background

HE EMERGENCE of Generative Artificial Intelligence T (GenAI) has marked a significant milestone, offering a transformative potential that extends beyond the traditional boundaries of Artificial Intelligence (AI) [1]. Unlike conventional AI (also so-called discriminative AI) models that focus primarily on analyzing or classifying existing data, GenAI can create new data, including text, image, audio, synthetic time-series data, and more [1]. This potential of GenAI has far-reaching implications across diverse sectors, from business and science to society at large [2], [3]. For instance, in the business sector, GenAI can power customer service bots or generate product designs, thereby maximizing efficiency and boosting competitive advantages [4]. According to Accenture’s 2023 Technology Vision report [5], 97% of global executives agree that GenAI will revolutionize how AI is used, enabling connections across data types and industries. In the natural science research community, GenAI can aid in generating synthetic data for research, e.g., protein sequences for disease prediction models [6], and accelerating the pace of discoveries [3]. Furthermore, GenAI can augment human creativity in our society, enabling the creation of new art, music, and literary work, thereby enriching our cultural heritage [7].

GenAI is not a singular technique but a collection of various models and methods, each of which is with its unique strengths and applications. Each of these models has contributed to the advancement of AI in different ways, forming the backbone of the current GenAI landscape, in which major examples include:

![](images/3b788c74f87fe19919304ced99654ab11e65c6abef139185c3a7edc2a2f89492.jpg)

<details>
<summary>bar_line</summary>

Number of Published Papers by Searching "Generative Diffusion Model" in Web of Science
| Year | Number of Published Papers |
| :--- | :--- |
| 2014 | 12 |
| 2015 | 14 |
| 2016 | 18 |
| 2017 | 20 |
| 2018 | 26 |
| 2019 | 32 |
| 2020 | 40 |
| 2021 | 63 |
| 2022 | 107 |
| 2023 | 257 |
</details>

Fig. 1. The number of published papers by searching “Generative Diffusion Model” in Web of Science (Access date: Jan-01-2024).

• Transformers: Transformers [8] have revolutionized Natural Language Generation (NLG) tasks, as exemplified by OpenAI’s ChatGPT [9]. They excel in applying context, a critical aspect of language understanding, and allow for greater parallelization of computing during training and inference.   
• Generative Adversarial Networks (GANs): GANs [10] have been instrumental in the field of image synthesis. They consist of a generative model and a discriminative model that interact and compete against each other, leading to continuous improvement in performance.   
• Variational Autoencoders (VAEs): VAEs [11] transform input data into a set of parameters in a latent space, which are then used to generate new data that closely aligns with the original distribution.   
• Flow-based Generative Models: Flow-based models [12] use probabilistic flows for data generation. They employ back-propagation for gradient computation, enhancing learning efficiency. Their ability to directly compute the probability density function during generation makes them computationally efficient, especially in mobile edge networks.   
• Energy-based Generative Models: Energy-based models [13] represent data using energy values. They define an energy function and optimize it to minimize the input data’s energy value. These models are intuitive, flexible, and capable of capturing dependencies by associating an non-normalized probability scalar with each configuration of observed and latent variables.   
• Generative Diffusion Models (GDMs): Initially proposed in [14], the concept of GDMs drew inspiration from the thermodynamic diffusion process. This thermodynamic correlation not only sets GDMs apart from other generative models but also establishes intriguing associations with score-based models [15] and stochastic differential equations [16], thereby enabling unique avenues for further research and applications.

Amidst these techniques, GDMs stand out due to their unique approach to data generation and their ability to model complex data distributions [17]. As shown in Fig. 1, recently, the versatility and potency of GDMs have been demonstrated in numerous applications, particularly in AI-Generated Content (AIGC) domains. For instance, Stable Diffusion [18], a diffusion model-based image generation application, has amassed over 10 million daily users, showcasing the practical utility and popularity of diffusion models. Furthermore, GDMs have been leveraged in various fields. In Computer Vision (CV), they have been used to generate high-quality images from noise, with models such as Denoising Diffusion Probabilistic Models (DDPM) [19] and Denoising Diffusion Implicit Models (DDIM) [20]. They have also been employed in text generation tasks, enhancing the controllability and coherence of the generated text [21]. In the audio domain, GDMs have been used for tasks like symbolic music generation and text-to-speech conversion [22], [23]. Beyond traditional domains, GDMs have been utilized in graph generation [24], [25], [26], molecular and material generation [27], [28], [29], and in synthesizing tabular data to electrocardiogram signal synthesis [30], [31], [32].

The widespread adoption of GDMs can be attributed to several key advantages over other GenAI methods.

• High-quality data generation ability. GDMs employ a forward and reverse diffusion process [33], enabling them to accurately capture complex data distributions and embrace high-quality. This stands in contrast to GANs, which can suffer from mode collapse, and VAEs, which can yield blurry results due to their Gaussian assumption [34].   
• Flexibility. GDMs are adaptable to various types of data and applications due to their reliance on stochastic differential equations [17]. This flexibility is a significant advantage over Transformer-based models, which, while powerful, are primarily designed for sequence data.   
• Simplicity of Implementation. GDMs’ structure, featuring a fixed bottom-up path defined by a diffusion process and a top-down path parameterized by Deep Neural Networks (DNNs), simplifies their implementation [35], [36]. This is a notable advantage over GANs and VAEs, which often require complex architectures and training procedures [37].

# B. Motivations

The significant success of diffusion models has been demonstrated across various domains, which suggests their potential utility in optimization scenarios. Recently, the authors in [38] introduce the Denoising Diffusion Optimization Models (DDOM), which employ an inverse mapping from function values back to input domains, utilizing the GDM’s ability to refine solutions towards optimal outcomes iteratively. Meanwhile, the authors in [39] develop the Graph Diffusion Policy Optimization (GDPO) method, integrating reinforcement learning with diffusion processes to address optimization in graph structures for non-differentiable reward signals. As shown in Table II, these studies exemplify the expanding role of diffusion models in tackling complex problems beyond their traditional generative contexts, inspiring us to support intelligent network optimization [40], [41], [42], [43]. Moreover, future intelligent networks such as Integrated Sensing and Communications (ISAC) [44], [45], Semantic Communications (SemCom) [46], [47], and Internet of Vehicles (IoV) [48] are characterized by high-dimensional configurations, non-linear relationships, and intricate decisionmaking processes that are tightly linked with semantics and interpretations [49]. For example, SemCom networks require a deep understanding of semantic information to facilitate efficient and accurate communication [50], and IoV networks involve the interaction of numerous highly mobile entities with heterogeneous communication capabilities [48], [51]. In all these cases, they exhibit complex dynamics with significant dependencies on prior and current states and the environment, leading to high dimensional and multimodal state distributions [52]. GDMs in this context are capable of capturing such high-dimensional and complex structures and effectively dealing with numerous decision-making processes and optimization problems, understanding and capturing the nuances of the complex trade-offs involved in the operation and optimization of intelligent networks [53].

The roles of GDMs in optimization can be categorized into enhancing decision making and Deep Reinforcement Learning (DRL). In decision-making scenarios, GDMs have been adopted to represent complex dynamics, incorporating additional conditioning variables such as constraints and demonstrating scalability over long time horizons [54], [55]. Specifically, the authors in [55] introduce a diffusion probabilistic model that subsumes much of the trajectory optimization process, effectively aligning sampling with planning strategies for long-horizon and complex control settings. Meanwhile, the authors in [54] show return-conditional diffusion models’ ability to exceed the performance of traditional offline DRL methods by modeling policies with additional variables like constraints to simplify the complexities. In the framework of DRL, GDMs have been employed as policy representations, capturing multi-modal action distributions and improving performance in offline RL tasks [56]. Furthermore, the authors in [57] pioneer a generative approach by decoupling the learned policy into a generative behavior model and an action evaluation model, utilizing GDMbased methods to model diverse behaviors and significantly enhancing the expressiveness and effectiveness of policies in offline RL scenarios. These developments underscore GDMs’ potential to innovate and enrich optimization in complex, high-dimensional spaces, setting the stage for more detailed discussions in Sections II and III.

Despite the promising advantages of GDMs in network optimization, we acknowledge that GDMs also come with their own set of challenges, e.g., the computational complexity introduced by the iterative nature of GDMs. This complexity could potentially pose difficulties in large-scale DRL tasks, such as those involving the optimization of extensive communication networks [58]. Additionally, GDMs might face challenges when dealing with data distributions that are characterized by high levels of noise or irregularities. This is particularly relevant in the context of real-world network traffic data [33]. Nevertheless, these challenges should not overshadow the potential of GDMs in network optimization. Instead, the challenges should be viewed as areas of opportunity for further research and development. The refinement and adaptation of traditional GDMs to address these issues effectively could pave the way for significant advancements in the field of network optimization.

# C. Contributions

The continuous advancements of GDMs in addressing optimization problems have inspired researchers to use them in specific design challenges within intelligent networks, such as optimizing incentive mechanisms [41] and selecting service providers [70]. Despite these developments, we believe that the full potential of GDMs has yet to be explored, in which GDMs are expected to revolutionize the paradigm of AI-driven intelligent network management. In this tutorial paper, we aim to expand the discourse within the network optimization community by presenting the application of GDMs. The value of this tutorial lies in its potential to broaden the existing toolkit for researchers and practitioners in the networking area, introducing new possibilities for integrating GDMs with traditional optimization methods.

While there are several surveys on GDMs, as shown in Table I, these works either provide a broad overview or focus on a specific area, such as CV or Natural Language Processing (NLP), leaving a gap in the comprehensive understanding of GDMs in the context of network optimization. This tutorial bridges this gap by providing an extensive introduction to GDMs, emphasizing their applications in network optimization challenges. Crucially, we present specific case studies drawn from several significant intelligent network scenarios. The contributions of our tutorial are listed below:

• We provide a comprehensive tutorial on the applications of GDMs, particularly in intelligent network optimization. This tutorial aims to offer a broad understanding of the origin, development, and major strength of GDMs, and to detail how the GDMs can be effectively implemented to solve complex optimization problems in the dynamic wireless environment.   
• We provide several case studies regarding the integration of GDMs with future intelligent network scenarios, e.g., DRL, Incentive Mechanism Design, ISAC, SemCom, and IoV Networks. These case studies demonstrate the practicality and efficacy of GDMs in emerging network technologies.   
• We discuss potential directions for GDM research and applications, providing insights into how GDMs can evolve and continue to influence future intelligent network design.

As shown in Fig. 2, the rest of the tutorial is structured as follows: We first study the applications of GDM in network optimization in Section II. The role of GDM in DRL is then explored in Section III. In Section IV, we present GDM’s role in incentive mechanism design. SemCom enhanced by GDMs are discussed in Section V, and Section VI focuses on applying GDMs in IoV Networks. In Section VII, we discuss the applications of GDM to several other network issues, i.e., channel estimation, error correction coding, and channel denoising. Furthermore, we outline potential research directions in Section VIII. Section IX concludes this tutorial.

TABLE I OVERVIEW OF SURVEY PAPERS ON GDMS WITH DIFFERENT APPLICATIONS 

<table><tr><td>Survey</td><td>Contributions</td><td>Emphasis</td></tr><tr><td>[17]</td><td>Discuss generative diffusion models and their applications in CV, speech, bioinformatics, and NLP</td><td rowspan="2">General review of GDMs</td></tr><tr><td>[33]</td><td>Provide an overview of diffusion models research, categorized into efficient sampling, improved likelihood estimation, and handling data with special structures</td></tr><tr><td>[59]</td><td>Discuss use of diffusion models for medical image analysis and various applications</td><td rowspan="4">Focus on the applications of GDMs on CV</td></tr><tr><td>[60]</td><td>Discuss diffusion models in image generation from text and recent advancements in GenAI models</td></tr><tr><td>[61]</td><td>Survey efficient diffusion models for vision and their applications in CV tasks</td></tr><tr><td>[34]</td><td>Survey diffusion models in vision and their applications in various vision tasks</td></tr><tr><td>[62]</td><td>Provide an overview of diffusion models in NLP, discussing text generation, translation, and summarization</td><td>Focus on NLP</td></tr><tr><td>[63]</td><td>Discuss diffusion models in non-autoregressive text generation for improving text generation efficiency</td><td>Focus on non-autoregressive text generation</td></tr><tr><td>[64]</td><td>Analyze the applications of diffusion models for time series data crucial in finance, weather, and healthcare</td><td>Focus on time series data</td></tr><tr><td>[65]</td><td>Discuss knowledge distillation in diffusion models, transferring complex knowledge to simplify models</td><td>Focuses on knowledge distillation</td></tr><tr><td>[66]</td><td>Focus on using diffusion models for generating molecules, proteins, and materials in drug discovery and materials science</td><td>Focus on several specific scientific applications</td></tr><tr><td>[67]</td><td>Discuss audio diffusion models in speech synthesis and recent advancements in GenAI models</td><td>Focus on audio and speech</td></tr><tr><td>[68]</td><td>Provide an overview of diffusion models in bioinformatics, including key concepts and various applications</td><td>Focus on the applications in bioinformatics</td></tr><tr><td>[69]</td><td>Present a survey on generative diffusion models on graphs, providing a state-of-the-art overview</td><td>Focus on the applications of GDMs on graphs</td></tr></table>

# II. NETWORK OPTIMIZATION VIA GENERATIVE DIFFUSION MODELS

This section presents an overview of GDMs, their applications, principles, and extensions to facilitate network optimization. A step-by-step tutorial is provided, using a simple, yet representative, sum rate maximization problem as a demonstrative example, to illustrate the applications of GDMs in wireless environments.

# A. Applications of Generative Diffusion Models

GDMs are known for their unique capabilities, theoretical robustness, and recent improvements in training and sampling efficiency, leading to their adoption in various domains [17], [33].

1) Computer Vision: The evolution and applications of GDMs in the field of vision have been marked by a series of interconnected advancements. Beginning with the DDPM [19] and DDIM [20], the field has shifted towards dynamic and flexible frameworks that can generate high-quality images from noise. Building on this foundation, the reflected diffusion models [71] integrated constraints into the generative process, leading to more faithful samples and expanding the potential applications of GDMs. This concept of flexibility and adaptability was further extended by the DiffCollage model [72], which demonstrated the ability of GDMs to generate largescale content in parallel. The latent flow diffusion models [73] then bridged the gap between image and video generation, synthesizing optical flow sequences [74] in the latent space to create videos with realistic spatial details and temporal motion. Furthermore, the video diffusion models [75] marked a significant milestone in generative modeling research, showcasing the potential of GDMs in generating temporally coherent, high-fidelity videos.

2) Text: Unlike Transformer-based models such as GPT, which focus primarily on sequence data, GDMs offer a unique advantage in their ability to model complex data distributions, making them more versatile for various tasks. Integrating language models into the diffusion process by Diffusion-LM [21] has enhanced the controllability and coherence of the generated text, demonstrating the adaptability of GDMs to different text generation tasks. This adaptability was further evidenced by the latent diffusion energy-based model [76], which introduced an energy-based model into the diffusion process, thereby improving the interpretability and quality of text modeling. The versatility of GDMs was showcased by the DiffuSeq [77] and DiffuSum [78] models, which applied GDMs to diverse tasks such as sequence-to-sequence generation and extractive summarization. Lastly, the innovative approach of the DiffusER model [79] in formulating text editing as a diffusion process further expanded the scope of GDM applications, demonstrating their potential in complex text editing tasks.

![](images/74ff6452c07ceae8dbf782f3166552ce9028386451886ade5eb246c4435b90b5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Tutorial"] --> B["I.A Background"]
    A --> C["I.B Motivations"]
    A --> D["I.C Contributions"]
    B --> E["Section I: Introduction"]
    C --> F["Section II: Network Optimization via Generative Diffusion Models"]
    D --> G["Section III: Deep Reinforcement Learning"]
    E --> H["II.A Applications of GDMs"]
    E --> I["II.B Principles of the GDMs"]
    F --> J["III.A Fundamentals of DRL"]
    F --> K["III.B Application of GDM in DRL"]
    G --> L["III.C Case Study: AIGC Service Provider Selection"]
    H --> M["Section IV. Incentive Mechanism Design"]
    H --> N["Section V. Semantic Communications"]
    I --> O["Section VI. Internet of Vehicles Networks"]
    I --> P["Section VII. Miscellaneous Issues"]
    
    subgraph Section IX: Conclusion
        Q["VII.A Channel Estimation"] --> R["Motivations"] --> S["Case Study"]
        T["VII.B Error Correction Coding"] --> U["Motivations"] --> V["Case Study"]
        W["VII.C Channel Denoising"] --> X["Motivations"] --> Y["Case Study"]
    end
    
    subgraph Section VIII: Future directions
        Z["IV.A Fundamentals of Incentive Mechanisms"] --> AA["Shapley Value"]
        Z --> AB["Stackelberg Game"]
        Z --> AC["Contract Theory"]
        Z --> AD["Auction"]
        Z --> AE["IV.B Application of GDM in Incentive Mechanism Design"]
        Z --> AF["VI.A Fundamentals of IoV Networks"]
        Z --> AG["VI.B Applications of GDM in IoV Networks"]
        Z --> AH["Recovery of Images sent by vehicles"]
        Z --> AI["Optimization Based on GDM"]
        Z --> AJ["VI.C Case Study: A GAI-driven IoV network"]
        Z --> AK["System Model"]
        Z --> AL["Problem Formulation"]
        Z --> AM["GDM-based Joint Channel Selection and Power Allocation"]
        Z --> AN["Numerical Results"]
    end
```
</details>

Fig. 2. Structure of Our Tutorial: We initiate our discussion with the foundational knowledge of GDM and the motivation behind their applications in network optimization. This is followed by exploring GDM’s wide applications and fundamental principles and a comprehensive tutorial outlining the steps for using GDM in network optimization. In the context of intelligent networks, we study the impact of GDM on algorithms, e.g., DRL, and its implications for key scenarios, e.g., incentive mechanism design, SemCom, IoV networks, channel estimation, error correction coding, and channel denoising. We conclude our tutorial by discussing potential future research directions and summarizing the key contributions.

3) Audio: GDMs have been leveraged to create a transformative shift in audio generation. The symbolic music generation model [22] demonstrated the potential of GDMs in generating complex symbolic music. The ProDiff model [23] further showcases the ability of GDMs to generate high-quality text-to-speech outputs rapidly. The MM-Diffusion model [80] further extended the versatility of GDMs, demonstrating their capability to generate joint audio and video content. The DiffWave model [81] and the DiffSinger model [82] enhanced audio synthesis by generating high-fidelity waveforms and expressive singing voices, respectively. Moreover, the CRASH model [83] used the GDM in raw audio synthesis, demonstrating GDMs’ ability to generate high-resolution percussive sounds, offering a more flexible generation capability compared to traditional methods.

4) Others: GDMs were also applied widely to other application domains. In cyber security, GDMs are both robust defense mechanisms and potential attack tools. On the defense side, GDMs offer a novel approach to safeguard against adversarial attacks and enhance privacy through differential privacy techniques [84], [85]. Conversely, GDMs can be manipulated for adversarial example generation and deception attacks, threatening the integrity of systems [86], [87]. In graph generation, GDMs have been utilized to generate intricate graph structures, as demonstrated by the works in [24], [25], [26]. These models have effectively harnessed the power of GDMs to handle discrete data types, showcasing their adaptability in representing complex relationships and structures inherent in graph data. This adaptability extends to the field of molecular and material generation, where models like MolDiff [27], DiffDock-PP [28], and MDM [29] demonstrated how GDMs can be utilized to generate intricate molecular structures, such as proteins in the field of molecular biology and material science. GDMs have shown great potential in handling heterogeneous features and synthesizing diverse tabular and time-series data types. The models presented in CoDi [30], TabDDPM [31], and DiffECG [32] have demonstrated the versatility of GDMs in tasks ranging from synthesizing tabular data to ECG signal synthesis.

The exceptional performance and broad applicability of GDMs can be attributed to their unique design. This has garnered significant attention, particularly in generating diverse high-resolution images, with large-scale models such as GLIDE [88], DALLE-2 [89], Imagen [90], and the fully open-source Stable Diffusion [18] being developed by leading organizations like OpenAI, Nvidia, and Google. Given the widespread use and success of GDMs in the CV domain, we introduce the principles and theory of GDMs in this context in Section II-B. This is a foundation for our subsequent discussion on how GDMs can be extended to facilitate network optimization in Section II-C.

# B. Principles of the GDMs

Unlike GANs that generate samples from a latent vector in a single forward pass through the Generator network [91], GDMs utilize a denoising network to iteratively converge to an approximation of a real sample $x \sim q ( x )$ over a series of estimation steps [92], where $q ( x )$ is the data distribution. This unique design has made GDMs emerge as a powerful tool in the field of generative modeling [60].

![](images/0f2949658cb7c929cb49e9c3df96628ee06251e8b9fbea120df512b83279ab65.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    x0["x₀"] --> x1["x₁"]
    x1 --> ... --> xt1["x_{t-1}"]
    xt1 --> xt2["x_t"]
    xt2 --> ... --> xT1["x_{T-1}"]
    xT1 --> xT["x_T"]
    xT -->|pθ(x_{t-1}|xₜ)| xt1
    xT -->|Forward diffusion| x1
    xT -->|Reverse diffusion| xT
```
</details>

Fig. 3. Illustration of the forward and reverse diffusion processes. The forward diffusion process involves the addition of noise, typically Gaussian noise, to the existing training data. Subsequently, the reverse diffusion process, also referred to as “denoising,” aims to recover the original data from the noise-added version.

As shown in Fig. 3, the underlying principle of GDMs is simple. With an initial input, GDMs progressively introduce Gaussian noise through a series of steps, i.e., the forward diffusion process, which generates the targets for the denoising neural network. Subsequently, the neural network is trained to reverse the noising process and recover the data and content [19]. The reverse diffusion process allows for the generation of new data. In the following, we show the mechanisms of forward diffusion and reverse denoising processes, utilizing an original data point $\mathbf { { x } _ { 0 } } ,$ , e.g., network solution or signal 0matrices, as our exemplar.

1) Forward Diffusion Process: The forward diffusion process can be modeled as a Markov chain with T steps. Let $\mathbf { x } _ { \mathrm { 0 } }$ 0denote the original data. At each step, i.e., t, in the Markov chain, a Gaussian noise with a variance of $\beta _ { t }$ is added to $\mathbf { x } _ { t - 1 }$ to yield $\mathbf { X } _ { t }$ with the distribution $q \big ( \mathbf { x } _ { t } | \mathbf { x } _ { t - 1 } \big )$ 1. This process is represented as

$$
q (\mathbf {x} _ {t} | \mathbf {x} _ {t - 1}) = \mathcal {N} \left(\mathbf {x} _ {t}; \boldsymbol {\mu} _ {t} = \sqrt {1 - \beta_ {t}} \mathbf {x} _ {t - 1}, \boldsymbol {\Sigma} _ {t} = \beta_ {t} \mathbf {I}\right), \tag {1}
$$

where $q \big ( . \mathbf { x } _ { t } | \mathbf { x } _ { t - 1 } \big )$ is a normal distribution, characterized by the mean ${ \pmb { \mu } } _ { t }$ 1and the variance $\Sigma ,$ and I is the identity matrix indicating that each dimension has the same standard deviation $\beta _ { t }$ .

Then, from the original data $\mathbf { x } _ { \mathrm { 0 } }$ to the final $\mathbf { x } _ { T }$ , the posterior 0probability can be expressed in a tractable form as

$$
q (\mathbf {x} _ {1: T} | \mathbf {x} _ {0}) = \prod_ {t = 1} ^ {T} q (\mathbf {x} _ {t} | \mathbf {x} _ {t - 1}) \tag {2}
$$

However, according to (2), sampling $\pmb { x } _ { t } \left( t \in \{ 0 , 1 , \ldots , T \} \right)$ ) xnecessitates t times of calculation, which becomes computationally intensive when t is large. To avoid this, we define t $\alpha _ { t } = 1 - \beta _ { t }$ and $\bar { \alpha } _ { t } = \prod _ { j = 0 } ^ { \nu } \alpha _ { j }$ , enabling us to express $\mathbf { X } _ { t }$ as

$$
\begin{array}{l} \mathbf {x} _ {t} = \sqrt {1 - \beta_ {t}} \mathbf {x} _ {t - 1} + \sqrt {\beta_ {t}} \boldsymbol {\epsilon} _ {t - 1} = \sqrt {\alpha_ {t}} \mathbf {x} _ {t - 2} + \sqrt {1 - \alpha_ {t}} \boldsymbol {\epsilon} _ {t - 2} \\ = \dots = \sqrt {\bar {\alpha} _ {t}} \mathbf {x} _ {0} + \sqrt {1 - \bar {\alpha} _ {t}} \boldsymbol {\epsilon} _ {\mathbf {0}}, \tag {3} \\ \end{array}
$$

where $\epsilon _ { 0 } , \ldots , \epsilon _ { \mathrm { t - 1 } } \ \sim \ { \mathcal { N } } ( \mathbf { 0 } , \mathbf { I } )$ . Consequently, $\mathbf { x } _ { t }$ can be obtained using the following distribution:

$$
\mathbf {x} _ {t} \sim q (\mathbf {x} _ {t} \mid \mathbf {x} _ {0}) = \mathcal {N} \big (\mathbf {x} _ {t}; \sqrt {\bar {\alpha} _ {t}} \mathbf {x} _ {0}, (1 - \bar {\alpha} _ {t}) \mathbf {I} \big). \tag {4}
$$

Given that $\beta _ { t }$ is a hyperparameter, we can precompute $\alpha _ { t }$ and $\bar { \alpha } _ { t }$ for all timesteps. This allows us to sample noise at any timestep t and obtain $\mathbf { X } _ { t }$ . Therefore, we can sample our latent variable $\mathbf { x } _ { t }$ at any arbitrary timestep. The variance parameter $\beta _ { t }$ can be fixed to a constant or chosen under a $\beta _ { t }$ -schedule [19] over T timesteps.

2) Reverse Diffusion Process: When T is large, $x _ { T }$ approximates an isotropic Gaussian distribution [19]. If we can learn the reverse distribution $q ( . \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } )$ , we can sample $\mathbf { x } _ { T }$ from $\mathcal { N } ( \mathbf { 0 } , \mathbf { I } )$ 1, execute the reverse process, and obtain a sample from $q ( x _ { 0 } )$ .

0However, statistical estimates of $q ( . \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } )$ require com-1putations involving the data distribution, which is practically intractable. Therefore, our aim is to estimate $q ( . \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } )$ with a parameterized model $p _ { \theta }$ as follows:

$$
p _ {\theta} (\mathbf {x} _ {t - 1} | \mathbf {x} _ {t}) = \mathcal {N} (\mathbf {x} _ {t - 1}; \mu_ {\theta} (\mathbf {x} _ {t}, t), \boldsymbol {\Sigma} _ {\theta} (\mathbf {x} _ {t}, t)). \qquad (5)
$$

Subsequently, we can obtain the trajectory from $\mathbf { x } _ { T }$ to $\mathbf { x } _ { \mathrm { 0 } }$ as

$$
p _ {\theta} (\mathbf {x} _ {0: T}) = p _ {\theta} (\mathbf {x} _ {T}) \prod_ {t = 1} ^ {T} p _ {\theta} (\mathbf {x} _ {t - 1} \mid \mathbf {x} _ {t}). \tag {6}
$$

By conditioning the model on timestep t, it can learn to predict the Gaussian parameters, i.e., the mean $\pmb { \mu } _ { \boldsymbol { \theta } } ( \mathbf { x } _ { t } , t )$ and the covariance matrix $\Sigma _ { \theta } ( \mathbf { x } _ { t } , t )$ for each timestep.

The training of the GDM involves an optimization of the negative log-likelihood of the training data. According to [19], adding the condition information, e.g., , in the denoising process, $p _ { \theta } ( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } , \pmb { g } )$ gcan be modeled as a noise prediction 1 gmodel with the covariance matrix fixed as

$$
\boldsymbol {\Sigma} _ {\theta} (\mathbf {x} _ {\mathbf {t}}, \boldsymbol {g}, \mathbf {t}) = \beta_ {t} \mathbf {I}, \tag {7}
$$

and the mean is constructed as

$$
\boldsymbol {\mu} _ {\theta} (\boldsymbol {x} _ {t}, \boldsymbol {g}, t) = \frac {1}{\sqrt {\alpha_ {t}}} \left(\boldsymbol {x} _ {t} - \frac {\beta_ {t}}{\sqrt {1 - \bar {\alpha} _ {t}}} \boldsymbol {\epsilon} _ {\theta} (\boldsymbol {x} _ {t}, \boldsymbol {g}, t)\right). \tag {8}
$$

We first sample $\mathbf { x } ^ { T } \sim \mathcal { N } ( \mathbf { 0 } , I )$ and then from the reverse Idiffusion chain parameterized by θ as

$$
\boldsymbol {x} _ {t - 1} \mid \boldsymbol {x} _ {t} = \frac {\boldsymbol {x} _ {t}}{\sqrt {\alpha_ {t}}} - \frac {\beta_ {t}}{\sqrt {\alpha_ {t} (1 - \bar {\alpha} _ {t})}} \boldsymbol {\epsilon} _ {\theta} (\boldsymbol {x} _ {t}, \boldsymbol {g}, t) + \sqrt {\beta_ {t}} \boldsymbol {\epsilon}, \tag {9}
$$

where $\epsilon \sim \mathcal { N } ( 0 , I )$ and $t ~ = ~ 1 , \dots , T$ . Furthermore, the Iauthors in [19] introduced simplifications to the original loss function by disregarding a specific weighting term:

$$
\mathcal {L} _ {t} = \mathbb {E} _ {\mathbf {x} _ {0}, t, \boldsymbol {\epsilon}} \left[ \left\| \boldsymbol {\epsilon} - \boldsymbol {\epsilon} _ {\theta} \left(\sqrt {\bar {a} _ {t}} \mathbf {x} _ {0} + \sqrt {1 - \bar {a} _ {t}} \boldsymbol {\epsilon}, t\right) \right\| ^ {2} \right]. \tag {10}
$$

This effectively shows that instead of predicting the mean of the distribution, the model predicts the noise - at each timestep t.

# C. Motivations of Using GDMs in Network Optimization

We acknowledge that diffusion models, as a type of generative learning technology, were not initially designed for optimization problems. Originally conceived for tasks such as image and audio generation, where their ability to model complex data distributions and generate high-quality samples was paramount, diffusion models have seen their potential for broader applications, as shown in Table II. Specifically, the motivation for using GDMs in network optimization, particularly in intelligent networks, stems from their unique characteristics and capabilities.

First, GDMs possess a robust generative capability, which is suitable in dynamic network optimization with or without expert datasets, $i . e . ,$ , labeled optimal solutions. Unlike conventional applications of GDMs, such as in image or text domains, network optimization does not typically have access to large datasets suitable for offline training [109]. The lack of an expert dataset presents challenges when applying GDMs to facilitate network optimization. Fortunately, in addressing this challenge, the reverse diffusion process of GDMs, involving a denoising network, can be effectively utilized. Specifically, instead of relying on the standard loss function as illustrated in (10), the denoising network can be trained to maximize the value of the final generated solution output [41]. Here, the value is related to the optimization objective function, which is designed to either maximize or minimize a specific outcome based on the given application. In network optimization, the value can be a performance metric like sum rate, latency, or energy efficiency. This training process can be achieved by executing the generated solution within the network environment, followed by network parameter adjustments based on the received feedback. Thus, the obstacle presented by the absence of a suitable dataset transmutes into an opportunity for dynamic online learning and optimization [70]. Notably, when expert datasets are accessible, adjustments can be made to minimize the loss between the expert and the generated solutions. These adjustments enable the GDM to continuously refine its output based on loss, leading to progressively more optimized network solutions with higher objective values.

Second, GDMs can easily incorporate conditioning information into the denoising process. In intelligent networks, optimal solutions, e.g., power allocation schemes and incentive mechanism designs, typically change with the dynamic wireless environment [110]. Therefore, the wireless environment information, such as path loss and small-scale fading channel parameters, can be used as the conditioning information in the denoising process [111]. After sufficient training, the denoising network should be able to generate the optimal solution given any dynamic wireless environment condition [41]. This ability to adapt to dynamic environments and generate optimal solutions is valuable in wireless network optimization.

Furthermore, the relationship between GDMs and DRL in intelligent network optimization is not just the substitution or competition but rather a compliment and/or supplement of each other that allows for mutual enhancement and learning. Specifically, training the denoising network in GDMs, which is guided by feedback from the external environment, embodies a reinforcement learning paradigm [41]. Thus, techniques such as Q-networks can facilitate more effective training of the denoising network [112]. Moreover, GDMs can be leveraged to enhance the performance of various DRL algorithms [70]. For instance, the robust generative capabilities of GDMs can be harnessed in imitation learning, thereby augmenting the performance of offline DRL [35], [58]. In addition, GDMs can substitute the action network in DRL algorithms, where actions are treated as the output of the denoising process [56].

# D. Tutorial With an Example

In this part, we representatively formulate an optimization problem in a wireless network and show a step-by-step tutorial to solve it by using GDMs. We compare the solutions generated by GDMs with the traditional DRL methods, such as Soft Actor-Critic (SAC) [113] and Proximal Policy Optimization (PPO) [114]. The code is available at https://github.com/HongyangDu/GDMOPT.

TABLE II SUMMARY OF PAPERS ON DIFFUSION MODELS IN OPTIMIZATION 

<table><tr><td>Paper</td><td>Key Contributions</td><td>Role of Diffusion Model</td></tr><tr><td>[38]</td><td>Introduces a framework for applying diffusion models in black-box optimization scenarios.</td><td>Employs diffusion processes to generate high-quality solutions iteratively.</td></tr><tr><td>[93]</td><td>Proposes a novel diffusion model approach for enhancing data-driven black-box optimization.</td><td>Applies diffusion models to refine solutions using data-driven insights iteratively.</td></tr><tr><td>[94]</td><td>Develops a graph-based diffusion solver specifically tailored for combinatorial optimization problems.</td><td>Uses diffusion techniques on graphs to solve complex combinatorial tasks more efficiently.</td></tr><tr><td>[39]</td><td>Focuses on optimizing reinforcement learning policies using graph-based diffusion methods.</td><td>Integrates diffusion processes into policy learning to improve decision making in complex environments.</td></tr><tr><td>[95]</td><td>Aims to improve the robustness of models against adversarial attacks.</td><td>Utilizes diffusion models to optimize and enhance model robustness.</td></tr><tr><td>[96]</td><td>Focuses on generating designs under constraints using diffusion models.</td><td>Aids in aligning design generation processes with optimization trajectories.</td></tr><tr><td>[97]</td><td>Proposes a method for designing antigen-specific antibodies.</td><td>Employs diffusion models for the optimization and design of specific antibodies.</td></tr><tr><td>[98]</td><td>Enhances policy optimization in reinforcement learning through diffusion behavior.</td><td>Leverages diffusion models for regularization and improvement of policy optimization.</td></tr><tr><td>[99]</td><td>Presents a framework for adaptive online replanning using diffusion models.</td><td>Facilitates real-time optimization and replanning in dynamic environments.</td></tr><tr><td>[100]</td><td>Introduces a wavelet-based optimization technique for enhancing CT image reconstruction from sparse views.</td><td>Facilitates progressive image enhancement and noise reduction through iterative refinement.</td></tr><tr><td>[101]</td><td>Develops a model for reconstructing high-quality CT images from ultra-sparse data.</td><td>Utilized in iterative reconstruction processes to improve image stability and quality.</td></tr><tr><td>[102]</td><td>Presents a zero-shot approach for 3D human pose estimation using diffusion models.</td><td>Enables effective optimization of pose estimation in zero-shot scenarios by leveraging generative capabilities.</td></tr><tr><td>[103]</td><td>Proposes methods for 3D scene generation, optimization, and planning.</td><td>Plays crucial in generating and optimizing 3D scenes for planning tasks.</td></tr><tr><td>[104]</td><td>Offers an optimization strategy for converting text descriptions into 3D content.</td><td>Improves the text-to-3D conversion process by enhancing content creation and optimization.</td></tr><tr><td>[105]</td><td>Introduces DiffusionFields for optimizing robotic grasp and motion planning.</td><td>Assists in learning cost functions for effective optimization of robotic tasks.</td></tr><tr><td>[106]</td><td>Demonstrates the superiority of diffusion models over GANs in topology optimization tasks.</td><td>Achieves more effective and efficient topology optimization.</td></tr><tr><td>[107]</td><td>Introduces a framework for stochastic optimization based on controlled SDEs.</td><td>Applies diffusion models for optimizing processes in continuous-time datasets.</td></tr><tr><td>[108]</td><td>Develops a diffusion-based path planning method for legged robots.</td><td>Utilizes diffusion models for optimizing 2D path planning tasks.</td></tr></table>

1) Problem Formulation: Consider a wireless communication network where a base station with total power $P _ { T }$ serves a set of users over multiple orthogonal channels. The objective is to maximize the sum rate of all channels by optimally allocating power among the channels. Let $g _ { n }$ denote the channel gain for the $n ^ { \mathrm { t h } }$ channel and $p _ { n }$ denote the power allocated to that channel. The sum rate of all M orthogonal channels is given by the sum of their individual rates [115], which can be expressed as

$$
\sum_ {m = 1} ^ {M} \log_ {2} (1 + g _ {m} p _ {m} / N _ {0}), \tag {11}
$$

where $N _ { 0 }$ is the noise level that can be set as 1 without loss of 0generality for the analysis. The problem is to find the power allocation scheme $\{ p _ { 1 } , \hdots , p _ { M } \}$ that maximizes the capacity

C under the power budget and the non-negativity constraints as

$$
\max _ {\left\{p _ {1}, \dots , p _ {M} \right\}} C = \sum_ {m = 1} ^ {M} \log_ {2} (1 + g _ {m} p _ {m})
$$

$$
\text { s.t., } \left\{ \begin{array}{l} p _ {m} \geq 0, \forall m, \\ \sum_ {m = 1} ^ {M} p _ {m} \leq P _ {T}. \end{array} \right. \tag {12}
$$

The dynamic nature of the wireless environment presents a significant challenge, as the values of the channel gains, denoted as $\left\{ g _ { 1 } , \dots , g _ { M } \right\}$ , can fluctuate within a range. This variability 1is illustrated in Fig. 4, which depicts the sum rate values for different power allocation schemes and channel gains when $M \ = \ 3 .$ . It is evident that changes in channel conditions can significantly impact the optimal power allocation scheme. While various solutions have been proposed to address this issue, the following problems exist:

• Traditional mathematical solutions depend on accurate channel estimation [116]. However, even with precise estimation, the resources and energy consumed by pilot signals and the algorithm to perform the estimation are considerable and also introduce latency.   
• Heuristic algorithms [117] can achieve near-optimal solutions; but they involve multiple iterations in the solution process, leading to increased energy consumption and additional delays.   
• The water-filling algorithm [118], which can optimally solve this problem and provide an upper bound on the achievable sum rate, involves an iterative process to determine the correct number of channels for power allocation. The iteration stems from the fact that power is added to channels until the marginal increase in capacity is equal across all channels, or the power budget is consumed [118]. This process can be computationally intensive, particularly when dealing with a large number of channels.

Given these challenges, AI-based solutions have been proposed. For example, despite requiring a certain overhead, DRL allows for direct model deployment once training is complete. The delay in inferring an optimal solution for a given wireless environment is minimal. However, as the performance of the DRL algorithms continues to improve, the model design becomes more complex. For example, the SAC [113], a state-of-the-art DRL method, involves five networks, including two Q-networks and their target networks and a policy network, which increases the complexity of the model.

As discussed in Section II-C, GDMs are characterized by their simplicity, directness, and robustness. Furthermore, GDMs can easily incorporate the wireless environment as the condition in the denoising process, leveraging their strong generative capacity to generate optimal solutions. For example, the environmental factors such as channel gains and noise, that can influence the optimal solution can be modeled as a vector in (9).

2) GDM as the Solution: Next, we demonstrate how to solve the problem using GDMs. The GDM is trained to generate a power allocation scheme that maximizes the sum

![](images/904cabf807c9f8397b5850ebf04e703b516b8b1caaf903d31319e5306a5f112a.jpg)

<details>
<summary>area_stacked</summary>

| Transmit power P₂ (W) | Sum rate (Bit/s/Hz) |
| --------------------- | ------------------- |
| 0                     | 6.79952             |
| 1                     | 6.79952             |
| 2                     | 6.79952             |
| 3                     | 6.79952             |
| 4                     | 6.79952             |
| 5                     | 6.79952             |
| 6                     | 6.79952             |
| 7                     | 6.79952             |
| 8                     | 6.79952             |
| 9                     | 6.79952             |
| 10                    | 6.79952             |
| 11                    | 6.79952             |
| 12                    | 6.79952             |
| 13                    | 6.79952             |
| 14                    | 6.79952             |
| 15                    | 6.79952             |
| 16                    | 6.79952             |
| 17                    | 6.79952             |
| 18                    | 6.79952             |
| 19                    | 6.79952             |
| 20                    | 6.79952             |
| 21                    | 6.79952             |
| 22                    | 6.79952             |
| 23                    | 6.79952             |
| 24                    | 6.79952             |
| 25                    | 6.79952             |
| 26                    | 6.79952             |
| 27                    | 6.79952             |
| 28                    | 6.79952             |
| 29                    | 6.79952             |
| 30                    | 6.79952             |
| 31                    | 6.79952             |
| 32                    | 6.79952             |
| 33                    | 6.79952             |
| 34                    | 6.79952             |
| 35                    | 6.79952             |
| 36                    | 6.79952             |
| 37                    | 6.79952             |
| 38                    | 6.79952             |
| 39                    | 6.79952             |
| 40                    | 6.79952             |
| 41                    | 6.79952             |
| 42                    | 6.79952             |
| 43                    | 6.79952             |
| 44                    | 6.79952             |
| 45                    | 6.79952             |
| 46                    | 6.79952             |
| 47                    | 6.79952             |
| 48                    | 6.79952             |
| 49                    | 6.79952             |
| 50                    | 6.79952             |
| 51                    | 6.79952             |
| 52                    | 6.79952             |
| 53                    | 6.79952             |
| 54                    | 6.79952             |
| 55                    | 6.79952             |
| 56                    | 6.79952             |
| 57                    | 6.79952             |
| 58                    | 6.79952             |
| 59                    | 6.79952             |
| 60                    | 6.79952             |
| 61                    | 6.79952             |
| 62                    | 6.79952             |
| 63                    | 6.79952             |
| 64                    | 6.79952             |
| 65                    | 6.79952             |
| 66                    | 6.79952             |
| 67                    | 6.79952             |
| 68                    | 6.79952             |
| 69                    | 6.79952             |
| 70                    | 6.79952             |
| 71                    | 6.79952             |
| 72                    | 6.79952             |
| 73                    | 6.79952             |
| 74                    | 6.79952             |
| 75                    | 6.79952             |
| 76                    | 6.79952             |
| 77                    | 6.79952             |
| 78                    | 6.79952             |
| 79                    | 6.79952             |
| 80                    | 6.79952             |
| 81                    | 6.79952             |
| 82                    | 6.79952             |
| 83                    | 6.79952             |
| 84                    | 6.79952             |
| 85                    | 6.79952             |
| 86                    | 6.79952             |
| 87                    | 6.79952             |
| 88                    | 6.79952             |
| 89                    | 6.79952             |
| 90                    | 6.79952             |
| 10                     | nan                 |
</details>

(a)The three orthogonal channel gains are 1,O.5,and 2.5,respectively.

![](images/760fdcb8c69da2b6af8c068adaca7d109a0dd4ef9d987aedf7adc959880a0af2.jpg)

<details>
<summary>area_stacked</summary>

| Transmit power P₁ (W) | Transmit power P₂ (W) | Sum rate (Bit/s/Hz) |
| --------------------- | --------------------- | ------------------- |
| 0                     | 0                     | 5                   |
| 1                     | 1                     | 7                   |
| 2                     | 2                     | 8                   |
| 3                     | 3                     | 9                   |
| 4                     | 4                     | 8.5                 |
| 5                     | 5                     | 7.5                 |
| 6                     | 6                     | 6.5                 |
| 7                     | 7                     | 5.5                 |
| 8                     | 8                     | 4.5                 |
| 9                     | 9                     | 3.5                 |
| 10                    | 10                    | 2.5                 |
| 11                    | 11                    | 1.5                 |
| 12                    | 12                    | 0.5                 |
| 13                    | 13                    | -0.5                |
| 14                    | 14                    | -1.5                |
| 15                    | 15                    | -2.5                |
| 16                    | 16                    | -3.5                |
| 17                    | 17                    | -4.5                |
| 18                    | 18                    | -5.5                |
| 19                    | 19                    | -6.5                |
| 20                    | 20                    | -7.5                |
| 21                    | 21                    | -8.5                |
| 22                    | 22                    | -9.5                |
| 23                    | 23                    | -10.5               |
| 24                    | 24                    | -11.5               |
| 25                    | 25                    | -12.5               |
| 26                    | 26                    | -13.5               |
| 27                    | 27                    | -14.5               |
| 28                    | 28                    | -15.5               |
| 29                    | 29                    | -16.5               |
| 30                    | 30                    | -17.5               |
| 31                    | 31                    | -18.5               |
| 32                    | 32                    | -19.5               |
| 33                    | 33                    | -20.5               |
| 34                    | 34                    | -21.5               |
| 35                    | 35                    | -22.5               |
| 36                    | 36                    | -23.5               |
| 37                    | 37                    | -24.5               |
| 38                    | 38                    | -25.5               |
| 39                    | 39                    | -26.5               |
| 40                    | 40                    | -27.5               |
| 41                    | 41                    | -28.5               |
| 42                    | 42                    | -29.5               |
| 43                    | 43                    | -30.5               |
| 44                    | 44                    | -31.5               |
| 45                    | 45                    | -32.5               |
| 46                    | 46                    | -33.5               |
| 47                    | 47                    | -34.5               |
| 48                    | 48                    | -35.5               |
| 49                    | 49                    | -36.5               |
| 50                    | 50                    | -37.5               |
| Optimal power allocation scheme: P₁ = 2.9, P₂ = 3.6, P₃ = 3.5
</details>

(b) The three orthogonal channel gains are 3,1,and 3,respectively.

![](images/b7bb879251e034c98ed2811fb690b92f56d0502e65299c350fdb5a6fbb0470ca.jpg)

<details>
<summary>surface_3d</summary>

| Transmit power P₁ (W) | Transmit power P₂ (W) | Sum rate (Bit/s/Hz) |
| --------------------- | --------------------- | ------------------- |
| 0                     | 0                     | 3.78                |
| 1                     | 2                     | 3.11                |
| 2                     | 4                     | 7.70355             |
</details>

(c) The three orthogonal channel gains are 1,3,and 1,respectively.   
Fig. 4. The sum rate values for different power allocation schemes and different channel gains with M  3 and total power is 10 . We con observe = Wthat the optimal power allocation scheme and the corresponding peak sum rate values keep changing because of the dynamic wireless environment.

rate. The steps to solve the problem using diffusion models are as follows:

1) Solution Space Definition: The first step in wireless network optimization is to define the solution space. The AI-generated solution represents the optimal power allocation scheme that maximizes the sum rate. This scheme is generated by the GDM through a series of denoising steps applied to Gaussian noise. As shown in Algorithm 1 line 2, in the considered problem, the dimension of the solution vector should be the number of channels, i.e., M. Then, it should be performed in the wireless environment, as shown in Algorithm 1 lines 3–7.

![](images/e89e5465b1c445a56df32bd7eefa52b3cebe340bd2620dfac3331e6ac5f9d4e9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Step 1. Observe current wireless environment"] --> B["Step 2. Find the expert solution, i.e., the optimal solution based on the current state"]
    B --> C["Step 3. Randomly generate Gaussian noise (x_i = √(α_i x_0) + √(1−α_i ε_0))<br>Gaussian noise)<br>Time: Noise schedule"]
    C --> D["Step 4. Add noise to disrupt the expert solution"]
    D --> E["Step 5. Predict the noise by using the solution generation policy"]
    E --> F["Step 6. Calculate loss, update solution generation policy network (arg min L(θ) = E[ε - ε₀(√(α̅ x₀) + √(1−α̅ ε, t, g)"]²])]
    F --> G["Step 7. Analyze the parameters of the CDM"]
    G --> H["Step 8. Predict the noise by using the solution generation policy"]
    H --> I["Step 9. Analyze the objective function value after performing the generated solution"]
    I --> J["Step 10. Analyze the solution generation and evaluation networks' parameters according to the loss functions"]
    
    subgraph Step 1
        A
        B
        C
        D
        E
        F
        G
        H
        I
    end
    
    subgraph Step 2
        G
        H
        I
    end
    
    subgraph Step 3
        J
    end
    
    subgraph Step 4
        K["Perform the solution in intelligent network environment,<br>Record the objective function value r(g,p₀)"]
        L["Calculate the minimum cost function [σₜ(t) = Σₜ(t) / [σₜ(t) - σₜ(t) / [σₜ(t) - σₜ(t) / [σₜ(t) - σₜ(t) / [σₜ(t) - σₜ(t) / [σₜ(t) - σₜ(t) / [σₜ(t) - σₜ(t) / [σₜ(t) - σₜ(t) / [σₜ(t) - σₜ(t) / [σₐ(t) - σₐ(t) / [σₐ(t) - σₐ(t) / [σₐ(t) - σₐ(t) / [σₐ(t) - σₐ(t) / [σₐ(t) - σₐ(t) / [σₐ(t) - σₐ(t) / [σₐ(t) - σₐ(t) / [σₐ(t) - σₐ(t) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1)) / [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [σₐ(t-1))/ [\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ(t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/[\sigmaₐ,t-1)/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{t-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1}/ [\sigma_{s-1}/ [\sigma_{s-1}/ [\sigma_{s-1}/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1}/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_ {s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s-1}/ [\sigma_{s-1})/ [\sigma_{s}"]\n\nu=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    end
```
</details>

Fig. 5. GDM training approaches with and without an expert dataset. Part A illustrates the GDM training scenario when an expert database is accessible. The process learns from the GDM applications in the image domain: the optimal solution is retrieved from the expert database upon observing an environmental condition, followed by the GDM learning to replicate this optimal solution through forward diffusion and reverse denoising process. Part B presents the scenario where no expert database exists. In this case, GDM, with the assistance of a jointly trained solution evaluation network, learns to generate the optimal solution for a given environmental condition by actively exploring the unknown environment.

2) Objective Function Definition: The next step is to define the objective function to be maximized or minimized. In this context, the training objective of the diffusion model is to maximize the sum rate achieved by the GDM-generated power allocation, as shown in Algorithm 1 line 8. The upper bound can be provided by the water-filling algorithm [118].   
3) Dynamic Environment Definition: In wireless networks, the channel conditions can vary among different users, resulting in a dynamic and diverse environment. To accommodate this variability, GDM is designed to generate the optimal power allocation scheme corresponding to a given set of channel conditions. Thus, we consider a general case that each channel gains, $\mathrm { e . g . } , g _ { m } ( m = 1 , \ldots , M )$ , change randomly over a range, e.g., (0.5, 2.5), as shown in Algorithm 2. Note that here we consider the general case. In practice, the uniform distribution can also be replaced with a specific channel fading distribution,

Algorithm 1 Objective Function and Solution Space Definitions   
1: procedure COMPUTEOBJECTIVE(env_state, solutions)
2:    # solutions.dimension = M
3:    total_power ← $P_{T}$ , e.g., 10
4:    weights ← solutions / sum(solutions)
5:    a ← weights * total_power
6:    snr ← g_n * a
7:    rate ← np.log₂(1 + snr)
8:    value ← np.sum(rate)
9:    # upper bound: water(g_n, total_power)
10:    return value

e.g., Rayleigh, Rician, or Nakagami-m. The upper and lower bounds of the channel gains can be chosen correspondingly as needed.

4) Training and Inference: The conditional GDM is proposed to generate the power allocation scheme. This approach diverges from back-propagation algorithms in neural networks or DRL techniques that directly optimize model parameters. Instead, GDMs strive to generate the optimal power allocation scheme by denoising the initial distribution. The power allocation scheme designed in the given environment is denoted as . The pGDM that maps environment states to power allocation schemes is referred to as the solution generation network, i.e., $\pmb { \epsilon } _ { \pmb { \theta } } ( . \pmb { p } | \pmb { g } )$ with neural network parameters pθ. The objective of $\pmb { \epsilon } _ { \theta } ( . \pmb { p } | \pmb { g } )$ is to output a deterministic p gpower allocation scheme that maximizes the expected objective function values as defined in Algorithm 1. The solution generation network is represented via the reverse process of a conditional GDM, according to (9). The end sample of the reverse chain is the final chosen power allocation scheme. According to whether the expert dataset, i.e., the optimal  under pgiven , is available, there are two ways to train the $\epsilon _ { \theta } \colon$

4.1) When there is no expert dataset: A solution evaluation network $Q _ { v }$ is introduced, which can assign a Q-value that represents the expected objective function to an environment-power allocation pair, i.e.,  and . Here, the $Q _ { v }$ g pnetwork acts as a guidance tool for the training of the GDM network, i.e., solution generation network $\epsilon _ { \theta } .$ . The optimal $\epsilon _ { \theta }$ is the network that generates the power allocation scheme $\pmb { p } _ { 0 }$ according to (9) that has p0the highest expected Q-value. Thus, the optimal solution generation network can be computed by

$$
\underset {\boldsymbol {\epsilon} _ {\theta}} {\arg \min} \mathcal {L} _ {\boldsymbol {\epsilon}} (\theta) = - \mathbb {E} _ {\boldsymbol {p} _ {0} \sim \boldsymbol {\epsilon} _ {\theta}} [ Q _ {v} (\boldsymbol {g}, \boldsymbol {p} _ {0}) ]. \tag {13}
$$

The training goal of the solution evaluation network $Q _ { v }$ is to minimize the difference between the predicted Qvalue by the current network and the real Q-value. Thus, the optimization of $Q _ { v }$ is

$$
\underset {Q _ {v}} {\arg \min} \mathcal {L} _ {Q} (v) = \mathbb {E} _ {\boldsymbol {p} _ {0} \sim \pi_ {\theta}} \left[ \| r (\boldsymbol {g}, \boldsymbol {p} _ {0}) - Q _ {v} (\boldsymbol {g}, \boldsymbol {p} _ {0}) \| ^ {2} \right], \tag {14}
$$

where r denotes the objective function value when the generated power allocation scheme ${ \pmb p } _ { 0 }$ is performed p0in the environment . Then, the network structure for training is shown in Part B of Fig 5, and the overall algorithm of GDM in sum rate maximization is given in Algorithm 3.

4.2) When an expert database is available: In some instances of intelligent network optimization, a dataset of expert solutions might already be available. For example, applying traditional optimization schemes over time makes it feasible to obtain the optimal power allocation schemes corresponding to various channel conditions. Utilizing this expert dataset, the loss function can be designed to minimize the gap between the generated power allocation and the expert schemes as follows:

$$
\underset {\pi_ {\theta}} {\arg \min} \mathcal {L} (\theta) = \mathbb {E} _ {\boldsymbol {p} _ {0} \sim \pi_ {\theta}} \left[ \left\| r (\boldsymbol {g}, \boldsymbol {p} _ {0}) - r _ {\exp} (\boldsymbol {g}) \right\| ^ {2} \right], \tag {15}
$$

where $r _ { \mathrm { e x p } } ( \pmb { g } )$ is the objective function value under the exp ggiven . To achieve efficient training, we can use a simgilar process to that used for GDM in the image domain. Let $\mathbf { x } _ { \mathrm { 0 } }$ denote the expert solution $r _ { \mathrm { e x p } }$ . As shown in 0 expPart A of Fig 5, to train GDM by forward diffusion and inverse denoising processes, the optimization of the loss function of the GDM network can be expressed as

Algorithm 2 Dynamic Environment Definition   
1: procedure GENERATESTATE
2:    env_state ← np.zeros(M)
3:    env_state[0] ← np.random.uniform(min, max)
4:    ...
5:    env_state[M - 1] ← np.random.uniform(min, max)
6:    return env_state

$$
\underset {\pi_ {\theta}} {\arg \min} \mathcal {L} (\theta) = \mathbb {E} \left[ \left\| \boldsymbol {\epsilon} - \boldsymbol {\epsilon} _ {\theta} \left(\sqrt {\bar {a} _ {t}} \mathbf {x} _ {0} + \sqrt {1 - \bar {a} _ {t}} \boldsymbol {\epsilon}, t, \boldsymbol {g}\right) \right\| ^ {2} \right], \tag {16}
$$

where - is the added Gaussian noise, $\sqrt { \bar { a } _ { t } } \mathbf { x } _ { 0 } + \sqrt { 1 - \bar { a } _ { t } } \epsilon$ denotes the expert solution after 0the forward diffusion process, and the network $\epsilon _ { \theta }$ can accurately predict the added noise with the inputs including the disrupted expert solution, the timestep information $t ,$ and the environment information condition . After training, when the channel conditions gchange again, the GDM network $\epsilon _ { \theta }$ is capable of efficiently generating the corresponding optimal solution according to (9).

Remark 1: The Algorithm 3 is designed for scenarios where an optimal solution needs to be obtained under specific environmental conditions. However, in intelligent networking, there are many situations where the value of the objective function is not immediately obtained after executing a solution in the environment [119], [120]. A typical example of this is the service provider selection problem, where tasks from users are allocated across various servers, each of which is with unique computing capability [70], [121], [122]. The total utility of all users, which is designed as the objective function to be maximized, can only be calculated after a long period of the allocation process. As a result, a decision-making process, such as allocating user tasks to desired servers, has to be modeled by forming a Markov chain [123]. In such cases, our proposed Algorithm 3 remains useful with minor adjustments. Specifically, the reward part in Algorithm 3 (lines 7–13) needs to be adjusted to take into account the dynamics of the Markov chain and add the discount factor in the loss function model. More details on how to do this, along with examples, are discussed in Section III.

Remark 2: In situations where expert strategies are unavailable for guidance, GDM utilizes a solution evaluation network during the training phase. This is inspired by the Q-network commonly used in DRL [124], [125], [126]. The solution evaluation network estimates the quality of a given solution, e.g., the power allocation scheme in the discussed example, under specific environmental conditions. This quality assessment guides the GDM during its iterative denoising process. Moreover, other advanced techniques from the DRL field can be adopted to make GDM training even more efficient. For example, the double Q-learning technique [127], which aims

# Algorithm 3 GDM in Network Optimization

# Training Phase:

1: Input hyper-parameters: denoising step N, exploration noise    
2: ## Initialize Neural Networks   
3: Initialize solution generation network $\varepsilon _ { \theta }$ with weights $\theta ,$ solution evaluation network $Q _ { v }$ with weights υ   
4: ## Begin Learning Process   
5: Initialize a random process $\mathcal { N }$ for power allocation exploration   
6: while not converge do   
7: At the $j ^ { \mathrm { t h } }$ time moment, observe the current environment $\pmb { g } ^ { ( j ) }$ , which can be simulated by using Algorithm 2   
8: gSet $\pmb { p } _ { N }$ as Gaussian noise. Generate power allocation ( ) $\pmb { p } _ { 0 } ^ { ( j ) }$ by denoising ${ \pmb p } _ { N }$ using $\varepsilon _ { \theta } .$ , according to (9)   
9: p0 pAdd the exploration noise to $\pmb { p } _ { 0 } ^ { ( j ) }$   
10: p0Apply the generated power allocation scheme $\pmb { p } _ { 0 } ^ { ( j ) }$ to 0the environment and observe the objective function value by using Algorithm 1.   
11: Record the real objective function value $r ^ { ( j ) } \Big ( \pmb { g } ^ { ( j ) } , \pmb { p } _ { 0 } ^ { ( j ) } \Big )$   
12: g p0Update the $' Q _ { v }$ according to (14)   
13: Update the $\varepsilon _ { \theta }$ according to (13)   
14: return The trained solution generation network $\varepsilon _ { \theta }$   
1: Observe the environment vector   
g2: Generate the optimal power allocation $\pmb { p } _ { 0 }$ by denoising Gaussian noise using $\varepsilon _ { \theta }$   
3: return The optimal power allocation ${ \pmb p } _ { 0 }$

# Inference Phase:

at reducing over-estimation in Q-learning, can be adopted. This approach maintains two Q-networks, using the smaller Q-value for updates, thus offering a conservative estimate and mitigating over-optimistic solution assessments [127], [128]. Incorporating such methods can augment GDM training, promoting robustness and efficiency.

3) Insights: To better understand the proposed GDM method, we implemented Algorithm 3 to solve the optimization problem in (12) and observed the results. We denote the sum rate obtained by performing the power allocation scheme generated by the GDM in the training process as the test sum rate and use the water-filling algorithm [118] to obtain the upper bound, i.e., the achievable sum rate. The experimental platform for running our proposed algorithms was built on a generic Ubuntu 20.04 system with an AMD Ryzen Threadripper PRO 3975WX 32-Cores CPU and an NVIDIA RTX A5000 GPU.

First, we considered a scenario with M = 3 channels. The channel gain values were randomly selected from 0.5 to 2.5. Note that the upper and lower channel gain limits here can be changed accordingly depending on the actual channel conditions. The number of denoising steps, denoted by T, was set to 9. We then investigated the impact of different learning rates and $\beta$ schedulers on the algorithm’s performance.

![](images/d824cc49bc0d58a6005b6e5eb9b7a0bd2023ce29ec47adde557f4b125a6a63c8.jpg)

<details>
<summary>line</summary>

| Training Epoch | GDM-Learning rate: 0.0005 | GDM-Learning rate: 0.001 | DRL: PPO |
| -------------- | -------------------------- | ------------------------- | -------- |
| 0              | 0.0                        | 0.0                       | 0.0      |
| 50             | -0.3                       | -0.1                      | -0.4     |
| 100            | -0.1                       | -0.1                      | -0.3     |
| 150            | -0.1                       | -0.1                      | -0.4     |
| 200            | -0.1                       | -0.1                      | -0.3     |
| 250            | -0.1                       | -0.1                      | -0.1     |
</details>

Fig. 6. Test reward curves of GDM-aided and DRL-aided optimization methods under different learning rate values, with the number of channels $M = 3 ,$ , and the channel gains vary within 0.5 and 2.5.

![](images/f9b0a40462f718faacc6381bd2f98053716227c34ed4de39ab83e04aedf035f7.jpg)

<details>
<summary>line</summary>

| Training Epoch | GDM-Random Seed: 123 | GDM-Random Seed: 312 | GDM-Random Seed: 231 |
| -------------- | -------------------- | -------------------- | -------------------- |
| 0              | 0.0                  | 0.0                  | 0.0                  |
| 10             | -0.1                 | -0.05                | -0.25                |
| 20             | -0.2                 | -0.1                 | -0.4                 |
| 30             | -0.1                 | -0.05                | -0.3                 |
| 40             | -0.05                | -0.05                | -0.2                 |
| 50             | -0.1                 | -0.05                | -0.45                |
| 60             | -0.05                | -0.05                | -0.1                 |
| 70             | -0.05                | -0.1                 | -0.05                |
| 80             | -0.05                | -0.05                | -0.05                |
| 90             | -0.05                | -0.05                | -0.05                |
| 100            | -0.05                | -0.05                | -0.05                |
</details>

Fig. 7. Test reward curves of GDM-aided optimization methods under different random seed values, with the number of channels $M = 3 ,$ and the channel gains vary within 0.5 and 2.5.

Figure 6 illustrates the gap between achievable and test sum rates against the training epoch. We observe that the conventional DRL method, i.e., PPO, exhibits more significant fluctuations and less effective convergence. The challenges are from the problem’s inherent complexity, the environmental variability, or the influence of specific hyperparameters. However, despite these challenges, both GDM methods outperform the PPO method, irrespective of their learning rates. In the first case, GDM with a learning rate of 0.001 achieves rapid convergence to zero, taking approximately 48 seconds across 60 epochs, underscoring the method’s efficiency. Conversely, with a learning rate of 0.0005, GDM converges more slowly yet effectively reaches zero, requiring about 104 seconds over 130 epochs, reflecting a steadier learning trajectory due to smaller adjustments per iteration. These variations in learning times directly depend on the chosen learning rates, with faster rates enabling quicker learning at the potential cost of overshooting minima. Furthermore, it is pertinent to note the correlation between dataset size and learning dynamics. While not explicitly analyzed in this context, the number of epochs typically reflects the dataset’s size, with more extensive datasets requiring more epochs to achieve thorough learning. This superior performance manifests the GDM’s ability to capture complex patterns and relationships between observations, leading to more accurate action decisions. This ability is advantageous in network optimization problems requiring high-performance, time-efficient, fast-converging solutions.

![](images/97f6a6067ad071f2a776b1e05e072c27a74401f666a06de10908e584769618b8.jpg)

<details>
<summary>line</summary>

| Training Epoch | GDM    | DRL: SAC | DRL: PPO |
| -------------- | ------ | -------- | -------- |
| 0              | -0.1   | -0.1     | -0.1     |
| 50             | -0.7   | -0.2     | -0.8     |
| 100            | -0.2   | -0.3     | -0.6     |
| 150            | -0.1   | -0.2     | -0.7     |
| 200            | -0.1   | -0.1     | -0.6     |
| 250            | -0.1   | -0.1     | -0.2     |
| 300            | -0.1   | -0.1     | -0.3     |
| 350            | -0.1   | -0.1     | -0.4     |
| 400            | -0.1   | -0.1     | -0.3     |
</details>

Fig. 8. Test reward curves of GDM-aided and DRL-aided optimization methods, with the number of channels M  5, and the channel gains vary within 0.5 and 5.

Fig. 7 further shows the robustness of the GDM methods, examining how varying random seeds influence the training performance. The figure delineates three distinct curves, each corresponding to a different random seed. While the random seed is known to significantly sway outcomes in imagerelated GDM applications such as Stable Diffusion [18], our findings reveal a contrasting scenario. After about 50 timesteps, all three cases stabilize, maintaining a gap to zero (where zero signifies the theoretical upper bound) within a negligible margin of 0.05. This observation shows that, unlike in image-related applications where identical text prompts can yield vastly different images based on the seed, the random seed’s impact on performance in this context is minimal. This insight highlights the GDM’s resilience against varying initial conditions, suggesting its consistent ability to learn the power allocation scheme and achieve near-optimal performance, especially in similar network optimization problems.

Then we consider a more complex case that the number of channels is 5 and the channel gains of these 5 channels vary within 0.5 and 5. We compare the performance of GDM and DRL algorithms and study the impact of denoising steps.

In Fig. 8, we examine the performance of the GDM method compared to two DRL methods, i.e., SAC and PPO. All three methods demonstrate convergence, while the final gap values for GDM and SAC are closer to zero, indicating a better power allocation scheme. In contrast, PPO exhibits larger fluctuations and slower convergence. While the final results of GDM and SAC are similar, GDM converges faster, which is attributed to its ability to capture complex patterns and relationships more efficiently. This faster convergence of GDM is particularly beneficial in scenarios where time efficiency is crucial.

![](images/ac5e7f1ee578ff8726a25cd90e062ad34b08b9344a97191ffc5410b3e7dc2cca.jpg)

<details>
<summary>line</summary>

| Training Epoch | GDM-Denoising Step: 12 | GDM-Denoising Step: 3 | GDM-Denoising Step: 6 |
| -------------- | ---------------------- | --------------------- | --------------------- |
| 0              | -0.1                   | -0.1                  | -0.1                  |
| 50             | -0.2                   | -0.2                  | -0.2                  |
| 100            | -0.3                   | -0.3                  | -0.3                  |
| 150            | -0.4                   | -0.4                  | -0.4                  |
| 200            | -0.5                   | -0.5                  | -0.5                  |
| 250            | -0.6                   | -0.6                  | -0.6                  |
| 300            | -0.7                   | -0.7                  | -0.7                  |
| 350            | -0.8                   | -0.8                  | -0.8                  |
| 400            | -0.8                   | -0.8                  | -0.8                  |
</details>

Fig. 9. Test reward curves of GDM-aided optimization methods under different denoising steps, with the number of channels M  5, and the channel gains vary within 0.5 and 5.

![](images/5f889d3e440993cedf72a5769838dade43835513d91812445ad065bf9e16c360.jpg)

<details>
<summary>line</summary>

| Training Epoch | GDM-With Expert Dataset | GDM-Without Expert Dataset | Average Allocation | Random Allocation |
| -------------- | ------------------------ | -------------------------- | ------------------- | ----------------- |
| 0              | 0                        | 0                          | 0                   | 0                 |
| 100            | -2                       | -8                         | -6                  | -10               |
| 200            | -1                       | -6                         | -5                  | -12               |
| 300            | -1                       | -4                         | -5                  | -10               |
| 400            | -1                       | -3                         | -5                  | -8                |
| 500            | -1                       | -2                         | -5                  | -6                |
| 600            | -1                       | -2                         | -5                  | -5                |
</details>

Fig. 10. Test reward curves of GDM-aided optimization methods with and without expert dataset, with the number of channels is 71, i.e., $M = 7 1$ , and the channel gains vary within 2 and 25.

Furthermore, we study the impact of different denoising steps on the performance of the GDM in Fig. 9. The figure presents three curves, each corresponding to a different number of denoising steps. The first curve, representing 6 denoising steps, exhibits the fastest convergence. The second curve, corresponding to 3 denoising steps, converges slower. This slower convergence rate could be attributed to insufficient denoising when the number of steps is small, leading to greater uncertainty in generated power allocation schemes. However, when the number of steps is too larger, as in the third curve where the number of denoising steps is 12, the convergence is slowest. This could be due to the model losing its ability to explore the environment effectively, as excessive denoising might lead to overfitting the training data. This analysis underscores the importance of carefully selecting the number of denoising steps in the GDM, striking a balance between sufficient denoising and maintaining the GDM’s ability to explore the environment.

Fig. 10 shows the test reward curves for GDM-aided optimization methods, both with and without access to an expert dataset, in a scenario with 71 channels, i.e., M = 71, and channel gains varying between 2 and 25. The figure further validates the efficacy of the GDM approaches, irrespective of the availability of the expert dataset. Using an expert dataset in GDM training significantly accelerates the convergence process. However, even without an expert dataset, the GDM approach can independently decrease the gap between the achieved sum rate and the upper bound. Furthermore, two straightforward power allocation schemes, namely average and random allocation, are also presented for comparison. Average allocation, which evenly distributes power among the channels, outperforms random allocation, which arbitrarily assigns power. However, GDM, with its advanced learning capability, outperforms both strategies.

![](images/6ee2ecc1324921f766aa97597fa32101ffdefc4c35cd8118aaae5a89348027e1.jpg)

<details>
<summary>bar</summary>

| Channel number | Transmit power (W) |
| -------------- | ------------------ |
| 0              | 0.1                |
| 5              | 0.2                |
| 10             | 0.3                |
| 15             | 0.1                |
| 20             | 0.4                |
| 25             | 0.2                |
| 30             | 0.4                |
| 35             | 0.2                |
| 40             | 0.4                |
| 45             | 0.2                |
| 50             | 0.3                |
| 55             | 0.2                |
| 60             | 0.3                |
| 65             | 0.4                |
| 70             | 0.2                |
| 75             | 0.3                |
</details>

![](images/4d5ffb352588c0db0101754217c5f2b5e208aac676c66588b9cd074b4ca9dd5b.jpg)

<details>
<summary>bar</summary>

| Channel number | Transmit power (W) |
| -------------- | ------------------ |
| 0              | 0.2                |
| 5              | 0.35               |
| 10             | 0.2                |
| 15             | 0.3                |
| 20             | 0.2                |
| 25             | 0.35               |
| 30             | 0.2                |
| 35             | 0.3                |
| 40             | 0.2                |
| 45             | 0.3                |
| 50             | 0.2                |
| 55             | 0.3                |
| 60             | 0.2                |
| 65             | 0.3                |
| 70             | 0.2                |
| 75             | 0.35               |
</details>

![](images/65643c6e92fbc295cd5d18d6f2af246bfc84e99f0b522f96f0d1596afbc5de08.jpg)

<details>
<summary>bar</summary>

| Channel number | Transmit power (W) |
| -------------- | ------------------ |
| 0              | 0.03               |
| 5              | 0.12               |
| 10             | 0.28               |
| 15             | 0.27               |
| 20             | 0.26               |
| 25             | 0.27               |
| 30             | 0.25               |
| 35             | 0.24               |
| 40             | 0.27               |
| 45             | 0.26               |
| 50             | 0.25               |
| 55             | 0.27               |
| 60             | 0.28               |
| 65             | 0.26               |
| 70             | 0.27               |
| 75             | 0.28               |
</details>

![](images/0ad29001d69b254ba77c3a3f249b9396471f59e2ce4719ab4d61b1b74d3a4a5e.jpg)

<details>
<summary>bar</summary>

| Channel number | Transmit power (W) |
| -------------- | ------------------ |
| 0              | 0.1                |
| 5              | 0.25               |
| 10             | 0.2                |
| 15             | 0.15               |
| 20             | 0.2                |
| 25             | 0.25               |
| 30             | 0.2                |
| 35             | 0.25               |
| 40             | 0.2                |
| 45             | 0.15               |
| 50             | 0.2                |
| 55             | 0.25               |
| 60             | 0.2                |
| 65             | 0.15               |
| 70             | 0.2                |
| 75             | 0.1                |
</details>

![](images/4c027ea2247105a19af5a4e8af7cfb990d081c52ea72b0a1620629cfc6efb259.jpg)

<details>
<summary>bar</summary>

| Channel number | Transmit power (W) |
| -------------- | ------------------ |
| 0              | 0.08               |
| 5              | 0.25               |
| 10             | 0.27               |
| 15             | 0.26               |
| 20             | 0.24               |
| 25             | 0.23               |
| 30             | 0.25               |
| 35             | 0.26               |
| 40             | 0.28               |
| 45             | 0.27               |
| 50             | 0.26               |
| 55             | 0.29               |
| 60             | 0.25               |
| 65             | 0.24               |
| 70             | 0.26               |
| 75             | 0.23               |
</details>

![](images/5d4a53a0d617995363fdcaf2aebd368cd39f824907e8014f31104b142a8b6281.jpg)

<details>
<summary>bar</summary>

| Channel number | Transmit power (W) |
| -------------- | ------------------ |
| 0              | 0.05               |
| 5              | 0.25               |
| 10             | 0.20               |
| 15             | 0.25               |
| 20             | 0.20               |
| 25             | 0.25               |
| 30             | 0.20               |
| 35             | 0.25               |
| 40             | 0.20               |
| 45             | 0.25               |
| 50             | 0.20               |
| 55             | 0.25               |
| 60             | 0.20               |
| 65             | 0.25               |
| 70             | 0.20               |
</details>

Fig. 11. Sub-figures (a) to (e) illustrate the process of 5-step denoising Gaussian noise into the transmit power allocation schemes using a well-trained GDM. Here, we consider 71 channels with the total transmission power of 12 . In these 71 channels, the channel gains differ randomly. Some channels fall Wwithin the range of 2 to 5, others between 10 to 15, and the remaining channels exhibit gains varying from 20 to 25. We simulate using a set of observations obtained by random sampling. Sub-figure (f) is the optimal power allocation scheme obtained by the water-filling algorithm [118].

Fig. 11 visualizes the process of the well-trained GDM generating the power allocation scheme from the Gaussian noise. We consider 71 channels with a total transmission power of 12 W, where the specific channel gains of the 71 channels randomly vary between (2, 5), (10, 15), or (20, 25). Figs. 11 (a)-(e) show the progressive refinement of the power allocation scheme through the denoising process. Fig. 11 (f) presents the optimal power allocation scheme obtained by the water-filling algorithm [118]. This series of figures demonstrates the capability of GDM to generate nearoptimal power allocation schemes through iterative denoising, even when confronted with complex and variable channel conditions. It also highlights the close agreement between the GDM-generated and water-filling algorithm-generated power allocation schemes, emphasizing the effectiveness of GDM in learning and imitating expert solutions. The gap between the sum rate under the power allocation scheme shown in Fig. 11 (e) and the upper bound is 0.11 bit/s/Hz.

Lesson Learned: From the above showcase discussions, we glean several insights into the application of GDMs in network optimization. Firstly, the superior performance of GDMs over traditional DRL methods underscores the transformative potential of GDMs in complex optimization tasks. This is particularly notable in scenarios where rapid convergence and high performance are paramount. Secondly, the learning-related parameters in GDM, such as learning rates and denoising steps, facilitate a novel balance between exploration and exploitation. Notably, the denoising process, acting as a pivotal mechanism in GDMs, introduces a fresh perspective to this classic trade-off in RL as we discussed in Fig. 9. Thirdly, the resilience of GDMs to varying initial conditions and their consistent near-optimal performance, even in the absence of an expert dataset, show the robustness and adaptability. This robustness is particularly crucial in realworld applications where conditions can be unpredictable and data may be imperfect or incomplete. Lastly, the ability of GDMs to generate near-optimal power allocation schemes that are closely aligned with expert solutions underscores their capacity for sophisticated pattern recognition and imitation. This suggests that GDMs can be used as a powerful tool for learning from and leveraging expert knowledge in complex domains in network optimization tasks.

# III. DEEP REINFORCEMENT LEARNING

This section first discusses DRL algorithms and their applications in network optimization [129], [130], followed by examining the integration of GDMs within DRL frameworks [35], [37], [54], [55], [56], [57], [58], [131], [132], [133], [134], [135], [136]. We then present a case study on AIGC service provider selection in edge networks [70].

# A. Fundamentals of DRL

DRL is a powerful approach that combines the strengths of both deep learning and reinforcement learning, enabling the development of algorithms capable of learning to make optimal decisions through interactions with their environment [129], [130]. The DRL framework comprises two main components: the agent and the environment [137]. The agent, a decision-making entity, learns to interact optimally with the environment to maximize a cumulative reward [138]. The environment provides feedback to the agent in the form of rewards based on the actions taken by the agent [139]. This interaction forms the basis of the learning process in DRL. We summarize several representative DRL algorithms as

• Deep Q-Network (DQN): DQN uses a deep neural network for approximating the Q-value function, enabling it to handle high-dimensional state spaces. However, it struggles with high-dimensional or continuous action spaces [140].   
• Prioritized DQN: This variant of DQN prioritizes experiences with high temporal-difference error, leading to faster learning but introducing additional complexity [141].   
Deep Recurrent Q-Network (DRQN): DRQN extends DQN with recurrent neural networks for tasks requiring memory of past information, which is however challenging to train [142].   
• PPO: PPO is a stable policy gradient method that keeps policy updates close to zero, which however may require more samples to learn effectively [114], [143].   
• REINFORCE: REINFORCE directly optimizes the policy function, making it widely applicable but suffering from high variance [144].   
• SAC: SAC maximizes both the expected return and the policy’s entropy, leading to better performance in complex environments at the cost of computational complexity [113].   
• Rainbow: Rainbow combines seven DQN improvements, enhancing performance but increasing implementation complexity [145].

In the context of wireless communications, DRL offers several advantages. First, DRL is adept at handling complex network optimization problems, enabling network controllers to find optimal solutions even without complete and precise network information [129], [146]. This strength is further complemented by DRL’s capacity to enable network entities to learn and accumulate knowledge about the communication and networking environment. This facilitates learning optimal policies without knowing the channel model and mobility pattern [129], [147]. Furthermore, DRL supports autonomous decision-making, reducing communication overheads and boosting network security and robustness [70], [148].

Given these advantages, DRL has found extensive applications in network optimizations [149]. However, it is important to note that DRL also has its limitations, which, however, may be mitigated by the introduction of GDMs:

• Sample Inefficiency: DRL often requires a large number of interactions with the environment to learn effectively, which can be computationally expensive and timeconsuming [129]. GDMs, with the strong ability to model complex data distributions, could reduce the number of samples required.   
• Hyperparameter Sensitivity: The performance of DRL algorithms can be significantly influenced by hyperparameters, demanding meticulous tuning for diverse tasks [150]. GDMs, with their flexible structure and adaptability to various data distributions, could provide a more robust solution.

• Difficulty in Modeling Complex Environments: DRL algorithms may struggle with environments characterized by complex and high-dimensional state and action spaces. By accurately capturing the underlying data distributions, GDMs could provide a more efficient representation of the environment.   
• Instability and Slow Convergence: DRL algorithms may suffer from instability and slow convergence. The unique structure of GDMs involves a diffusion process, potentially offering a more stable and efficient learning process.

# B. Applications of GDM in DRL

The distinctive characteristics of GDMs have been effectively utilized to enhance DRL. These advantages include high expressiveness, the ability to capture multi-modal action distributions, and the potential to integrate with other RL strategies seamlessly. One notable application of GDMs in DRL is presented in [56], where the authors introduced Diffusion Q-learning (Diffusion-QL). This innovative method utilized a GDM as the policy representation, more specifically, a DDPM [19] based on a Multilayer Perceptron (MLP). The authors incorporated the Q-learning guidance into the reverse diffusion chain, facilitating optimal action selection. Through this integration, they demonstrated the expressiveness of GDMs in capturing multi-modal action distributions and showcased their effectiveness in enhancing behavior cloning and policy improvement processes. As a result, Diffusion-QL surpassed previous methods across several D4RL benchmark tasks [151] for offline RL. Complementarily, the work in [57] improves offline RL further by addressing the limitations of distributional expressivity in policy models. In contrast to the approach in [56], the authors in [57] decoupled the learned policy into a generative behavior model and an action evaluation model. This separation facilitated the introduction of a diffusion-based generative behavior model capable of modeling diverse behaviors such as agent’s trajectories. The optimal selection of actions from this behavior model was achieved through importance sampling in concert with an action evaluation model. They also incorporated an in-sample planning technique to mitigate extrapolation error and enhance computational efficiency. The resulting methodology outperformed traditional offline RL methods on D4RL datasets [151] and showed proficiency in learning from heterogeneous datasets. These highlighted studies represent just a subset of the burgeoning body of work on GDMs in DRL. For an extended discussion, Table III reviews various papers about GDM and DRL, summarizing their contributions and impacts. The distinctive ability of GDMs to accurately model complex distributions significantly enhances DRL algorithms, particularly in network settings where decision-making processes frequently require navigating through intricate solution spaces. This capability facilitates more effective and efficient optimization of network configurations and resource allocations compared to traditional models, offering advanced solutions that can dynamically adapt to the complexities inherent in network management.

TABLE III EXTENDED SUMMARY OF PAPERS ON GDM IN DRL 

<table><tr><td>Paper</td><td>Key Contributions</td><td>Results</td></tr><tr><td>[131]</td><td>Leverage Language Augmented Diffusion (LAD) models for language-based skills in RL</td><td>Achieve an average success rate of 72% on the CALVIN language robotics benchmark</td></tr><tr><td>[56]</td><td>Propose Diffusion Q-learning (Diffusion-QL) for offline RL and represent the policy as a GDM</td><td>Achieve state-of-the-art performance on the majority of D4RL benchmark tasks</td></tr><tr><td>[57]</td><td>Decouple policy learning into behavior learning and action evaluation and introduce a generative approach for offline RL</td><td>Achieve superior performance on complex tasks such as AntMaze on D4RL</td></tr><tr><td>[55]</td><td>Develop a diffusion probabilistic model for trajectory optimization and introduce a model directly amenable to trajectory optimization</td><td>Demonstrate effectiveness in control settings emphasizing long-horizon decision-making and test-time flexibility</td></tr><tr><td>[37]</td><td>Introduce Contrastive Energy Prediction (CEP) for learning the exact guidance in diffusion sampling</td><td>Demonstrate effectiveness in offline RL and image synthesis, outperforming existing state-of-the-art algorithms on D4RL benchmarks</td></tr><tr><td>[35]</td><td>Propose a robust version of the Diffusion Implicit Models (DIMs) for better generalization to unseen states in RL</td><td>Show the new approach provides more stable policy improvement and outperforms the baseline DIM methods on various complex tasks</td></tr><tr><td>[132]</td><td>Treat procedure planning as a distribution fitting problem, remove the expensive intermediate supervision and use task labels instead</td><td>Achieve state-of-the-art performance on three instructional video datasets across different prediction time horizons without task supervision</td></tr><tr><td>[133]</td><td>Introduce the Equivariant Diffuser for Generating Interactions (EDGI), an algorithm for MBRL and planning</td><td>Improve sample efficiency and generalization in 3D navigation and robotic object manipulation environments</td></tr><tr><td>[134]</td><td>Propose a general adversarial training framework for multi-agent systems using diffusion learning, enhancing robustness to adversarial attacks</td><td>Demonstrate enhanced robustness to adversarial attacks in simulations with FGM and DeepFool perturbations</td></tr><tr><td>[58]</td><td>Introduce a new imitation learning framework that leverages both conditional and joint probability of the expert distribution, and explore the use of different generative models in the framework</td><td>Outperform baselines in various continuous control tasks including navigation, robot arm manipulation, dexterous manipulation, and locomotion</td></tr><tr><td>[135]</td><td>Introduce a self-evolving method for diffusion-based planners in offline reinforcement learning, demonstrating an ability to improve planning performance for both known and unseen tasks</td><td>Outperform the previous state-of-the-art Diffuser by 20.8% on Maze2D and 7.5% on MuJoCo locomotion, and show better adaptation to new tasks, e.g., KUKA pick-and-place, by 27.9%</td></tr><tr><td>[136]</td><td>Introduce innovations for diffusion models in sequential environments</td><td>Accurately model complex action distributions, outperform state-of-the-art methods on a simulated robotic benchmark, and scale to model human gameplay in complex 3D environments</td></tr><tr><td>[54]</td><td>Apply conditional generative modeling to the problem of sequential decision-making and investigate conditioning on constraints and skills</td><td>Outperform existing offline RL approaches and demonstrate the flexible combination of constraints and composition of skills at test time</td></tr></table>

In summary, the integration of GDMs into DRL, as demonstrated by these representative studies and further summarized in Table III, leverages several key advantages offered by GDMs. The key advantages that GDMs offer to address the disadvantages of DRL as we discussed in Section III-A are listed below:

• Expressiveness: GDMs are capable of modeling complex data distributions, making them well-suited for representing policies in DRL [152]. For instance, in a dynamic traffic routing scenario, the policy needs to adapt to various traffic conditions, road structures, and vehicle

behaviors [153]. GDMs can effectively model such a policy.

• Sample Quality: GDMs are known for generating high-quality samples [23], [154]. In the context of DRL, this translates into the generation of highquality actions or strategies [155]. For example, in a network resource allocation task, the quality of the generated allocation decisions directly impacts the network performance. GDMs can generate high-quality decisions, leading to improved network performance.

• Flexibility: The ability of GDMs to model diverse behaviors is particularly useful in DRL, where the agent needs to adapt to a variety of situations and tasks [156]. In a network management task, for instance, the network may need to adapt to various traffic conditions and user demands. GDMs can model a wide range of behaviors, enabling the network to adapt to these diverse conditions.   
• Planning Capability: GDMs can be used for planning by iteratively denoising trajectories, providing a novel perspective on the decision-making processes in DRL [58]. For example, a DRL agent could use a GDM to plan the network operations, iteratively refining the plan to optimize the network efficiency [135], [136].

While GDMs offer promising advantages in DRL, they also present certain challenges. The iterative nature of GDMs can lead to increased computational complexity, which could be a hurdle in large-scale DRL tasks such as optimizing citywide communication networks [58]. Additionally, GDMs may struggle to accurately model certain data distributions, especially those with high noise levels or irregularities. This could pose challenges in DRL tasks involving real-world network traffic data, which may contain stronhg noise and outliers [33]. While these challenges underline the limitations of GDMs, they also present opportunities for innovative approaches that can effectively harness the benefits of GDMs while mitigating their shortcomings. Leveraging GDMs within advanced DRL algorithms offers a promising solution to both computational complexity and modeling limitations. An example could be found in combining GDMs with SAC [70], a state-of-the-art DRL method known for its efficient learning and robustness. This combination capitalizes on the strength of GDMs in modeling complex action distributions while utilizing the optimization capabilities of SAC, yielding a hybrid model with the potential for enhanced performance and efficiency in complex network optimization tasks. To illustrate this, we delve into a case study, introducing an innovative combination of GDM and SAC.

# C. Case Study: AIGC Service Provider Selection

1) System Model: The AIGC service provider selection problem depicted in Fig. 12 and detailed in [70], can be regarded as an extension of the resource-constrained task assignment problem. This is a well-known challenge in wireless networks where resources are scarce and their efficient utilization is critical to achieving the desired performance [157]. Specifically, we consider a set of sequential tasks and available ASPs, each of which possesses a unique utility function. The objective is to assign users’ AIGC tasks to ASPs in a way that maximizes the overall user utility. This user utility is a function of the required computing resource for each task and it is related to the AIGC model that performs the task. In addition, we acknowledge that the computing resources of each ASP is limited.

From a mathematical perspective, the ASP selection problem can be modeled as an integer programming problem, with the decision variables representing the sequence of task assignments to available ASPs. The formulation also incorporates constraints that capture the limitations on available resources. Failing to meet these constraints can have severe consequences, such as the crash of an ASP and the subsequent termination and restart of its running tasks.

![](images/1f9359475cc020318f93b558696995e4ef54f6f667512877ff111464c0c404f9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["AIGC-as-a-Service"] --> B["Deploy the trained AIGC model to the network edge server"]
    B --> C["Edge Server 1"]
    B --> D["Edge Server 2"]
    B --> E["..."]
    B --> F["Edge Server I"]
    C --> G["AIGC Service Provider Selection Problem"]
    D --> G
    E --> G
    F --> G
    G --> H["User 1"]
    G --> I["User 2"]
    G --> J["..."]
    G --> K["User J"]
    H --> L["Uplink: Tasks, Required Resource"]
    I --> M["I want to see ``A dress to wear with high heels.``"]
    J --> N["..."]
    K --> O["..."]
    P["ASP 1"] --> Q["Edge Server 1"]
    R["ASP 2"] --> S["Edge Server 2"]
    T["ASP I"] --> U["Edge Server I"]
    V["User 1"] --> W["User 2"]
    X["User 2"] --> Y["..."]
    Z["User J"] --> AA["User J"]
    AB["Downlink:"] --> AC["Finished Tasks"]
```
</details>

Fig. 12. AIGC service provider selection problem. Following the paradigm of “AIGC-as-a-Service”, various ASPs deploy their AIGC models onto network edge servers. With user requests arriving, an optimal task scheduler should be designed for real-time user task allocation. The goal is to maximize total user QoE, considering the unique capabilities of each AIGC model and the computing resource constraints of edge servers [70].

![](images/170ce095b8f78acff99fd7dd8a949a460825706dc03a2897557d85768418b1af.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["AaaS Environment"] --> B["Trajectory Collection"]
    B --> C["Observation s1"]
    C --> D["GDM-based Network"]
    D --> E["Reverse Diffusion Chain"]
    E --> F["P7"]
    F --> G["..."]
    G --> H["P1"]
    H --> I["..."]
    I --> J["P0"]
    J --> K["Optimal Action"]
    K --> L["Experience Replay Memory"]
    L --> M["Data Batch"]
    M --> N["GDM-based Network"]
    N --> O["Soft Update"]
    O --> P["Critic 1 Critic 2"]
    P --> Q["Target Actor"]
    Q --> R["Target Critic"]
    R --> S["Qtarget"]
    S --> T["Critic 1 Critic 2"]
    T --> U["Double Critic"]
    U --> V["Qeval"]
    V --> W["GDM-based Network"]
    W --> X["Action"]
    X --> Y["Execute Action"]
    Y --> Z["Probability Sampling"]
    Z --> AA["0.5 1.1"]
    AA --> AB["10 20"]
    AB --> AC["Reward r1 Observation s1+1"]
    AC --> AD["(s1, a1, s1+1, r1)"]
    AD --> AE["Feedback to Actor"]
    AE --> AF["Action"]
    AF --> AG["Update"]
    AG --> AH["Critic Loss"]
    AH --> AI["Optimizer"]
```
</details>

Fig. 13. The overall architecture of the D2SAC algorithm [70].

2) GDM-Based Optimal Decision Generation: The authors in [70] applied GDM to the actor-critic architecture-based DRL paradigm and proposed the Deep Diffusion Soft Actor-Critic (D2SAC) as a deep diffusion reinforcement learning algorithm. As shown in Fig. 13, the D2SAC algorithm incorporates several key components to optimize the policy, including an actor network, a double critic network, a target actor, a target critic, an experience replay memory, and the environment. Here’s a summary and explanation of these components and their roles:

• Trajectory Collection: The agent observes the environment and collects transitions of state by executing actions in the environment. These transitions are regarded as experiences and are added to the experience replay memory. The actor network generates an action distribution over all possible actions given an environment observation and samples an action from this distribution. This action is performed, transitioning to a new state and returning an immediate reward as feedback.

• GDM as the Policy: The core of the actor network is the GDM, which effectively encodes the observation’s representation. It captures the dependencies between the observation and the action space.   
• Experience Replay Memory: This is a method to handle the delay in receiving reward feedback. Experiences are stored and the missing reward is filled in later before updating the GDM-based network. Off-policy training is used to improve the handling of delayed feedback [158].   
• Double Critic Network: During the policy improvement process, the actor network is optimized by sampling minibatches of transitions from the experience replay memory. The double critic network, composed of two separate critic networks, is used to reduce the overestimation bias by providing a conservative estimate of the Q-value function [127].   
• Policy Improvement: The actor learns to maximize the expected cumulative reward for each action at the current state. The maximization problem is solved using the gradient ascent algorithm [159]. Specifically, gradients are calculated over a mini-batch of transitions sampled from the experience replay memory, and the actor network is updated by performing gradient descent on these gradients.   
• Action Entropy Regularization: An entropy regularization term is introduced to prevent the policy from becoming overly confident in certain actions and converging prematurely to a suboptimal solution [160]. This encourages exploration.   
• Q-function Improvement: The Q-function, used for estimating the future rewards of actions, must be accurately estimated for successful optimization. To achieve this, the Temporal Difference (TD) error between two Q networks is minimized during training [161].

Next, we discuss the performance of D2SAC and compare it with seven DRL algorithms as discussed in Section III-A. Furthermore, we demonstrate the efficacy of D2SAC across various benchmark tasks within the DRL domain.

3) Numerical Results: The authors in [70] compared D2SAC with benchmark reinforcement learning algorithms: DQN, DRQN, Prioritized-DQN, Rainbow, REINFORCE, PPO, and SAC. As shown in Fig. 6 in [70], D2SAC’s reward acquisition over time demonstrates its superior ability to balance exploration and exploitation, resulting in more optimal policy decisions.

Table IV presents comparative performance metrics of various control tasks in the Gym environment [163]

• Acrobot-v1: A two-link pendulum simulation, with the goal of maintaining an upright position. The reward system is designed to favor lesser negative values.

• CartPole-v1: A cart-pole system model, where the objective is to prevent a pole from falling. The performance measure here is the average reward, with higher values being desirable.   
• CoinRun-v0: A platform game task where the agent’s goal is to collect a coin while avoiding obstacles. The performance is gauged through the average reward per episode, aiming for higher values.   
• Maze-v0: A maze navigation task, where reaching the goal while taking fewer steps is rewarded. Similar to the previous tasks, higher average reward values indicate better performance.

These benchmarks cover a diverse range of problems, including physics-based control (Acrobot-v1, CartPole-v1), strategy (CoinRun-v0), and pathfinding (Maze-v0). A closer examination of the table reveals that D2SAC significantly outperforms most of the compared policies on these tasks. Specifically, for the Acrobot-v1 task, D2SAC achieves the least negative reward, implying superior performance in the complex task of manipulating the two-link pendulum. In the CartPole-v1 and CoinRun-v0 tasks, D2SAC matches the top-performing algorithms with perfect average rewards of 500 and 10, respectively, indicating a consistent ability to keep the pole upright and successfully collect coins in the platform game. The performance on Maze-v0, although not the highest, is competitive and within the performance range of topperforming policies.

# IV. INCENTIVE MECHANISM DESIGN

In this section, we investigate the applicability of GDM for shaping robust and efficient incentive mechanisms in network designs [70], [111], [164].

# A. Fundamentals of Incentive Mechanisms

Incentive mechanism [70], [111] plays an important role in network optimization for maintaining the network operationality and long-term economic sustainability. Specifically, the mechanism rewards the network participants who share computing, communication, and information resources and services. Take CrowdOut [165], a mobile crowdsourcing system for road safety, as an example. Drivers (using smartphones or vehicular sensors) can report road safety situations that they experience in their urban environments, e.g., speeding, illegal parking, and damaged roads, to the central management center. However, the drivers consume their computing and communication resources, e.g., battery power, CPU, and wireless bandwidth, to sense and report issues. They might be discouraged from actively joining such cooperations without appropriate rewards, especially in the long term. Accordingly, the incentive mechanisms aim at answering the following series of questions: 1) how to encourage the network entities to behave in a certain way that is beneficial to the network, e.g., through the use of rewards, reputation, or credit [166], 2) how to motivate the contribution of resources, 3) how to discourage and prevent the malicious behavior, and 4) how to ensure the fairness. To do so, the incentive mechanisms should be designed to satisfy several properties, including but not limited to Individual Rationality (IR), Incentive Compatibility (IC), fairness, Pareto Efficiency (PE), Collusion Resistance (CR), and Budget Balance (BB) [167]. With years of research, various incentive mechanisms have been presented and widely adopted in network optimization. We consider the following representative techniques for developing incentive mechanisms, including the Stackelberg game, auction, contract theory, and Shapley value.

TABLE IV PERFORMANCE COMPARISONS ON GENERAL BENCHMARK TASKS 

<table><tr><td colspan="2">Policy</td><td>Acrobot-v1</td><td>CartPole-v1</td><td>CoinRun-v0</td><td>Maze-v0</td></tr><tr><td rowspan="7">DRL</td><td>DQN</td><td>-81.81 ± 17.19</td><td>499.80 ± 0.14</td><td>6.00 ± 4.90</td><td>3.00 ± 4.58</td></tr><tr><td>Prioritized-DQN</td><td>-105.20 ± 14.74</td><td>498.70 ± 1.43</td><td>5.00 ± 5.00</td><td>2.00 ± 4.00</td></tr><tr><td>DRQN</td><td>-82.26 ± 14.34</td><td>132.50 ± 69.79</td><td>-</td><td>-</td></tr><tr><td>REINFORCE</td><td>-104.80 ± 14.51</td><td>500.00 ± 0.00</td><td>0.00 ± 0.00</td><td>0.00 ± 0.00</td></tr><tr><td>PPO</td><td>-77.22 ± 8.45</td><td>499.90 ± 0.33</td><td>0.00 ± 0.00</td><td>2.00 ± 4.00</td></tr><tr><td>Rainbow</td><td>-158.10 ± 55.48</td><td>478.30 ± 29.28</td><td>5.00 ± 5.00</td><td>2.00 ± 4.00</td></tr><tr><td>SAC</td><td>-121.00 ± 35.31</td><td>500.00 ± 0.00</td><td>10.00 ± 0.00</td><td>3.00 ± 4.58</td></tr><tr><td rowspan="8">Online[162], [163]</td><td>A2C</td><td>-86.62 ± 25.10</td><td>499.90 ± 1.67</td><td>-</td><td>-</td></tr><tr><td>ACER</td><td>-90.85 ± 32.80</td><td>498.62 ± 23.86</td><td>-</td><td>-</td></tr><tr><td>ACKTR</td><td>-91.28 ± 32.52</td><td>487.57 ± 63.87</td><td>-</td><td>-</td></tr><tr><td>PPO2</td><td>-85.14 ± 26.27</td><td>500.00 ± 0.00</td><td>-</td><td>-</td></tr><tr><td>DQN</td><td>-88.10 ± 33.04</td><td>500.00 ± 0.00</td><td>-</td><td>-</td></tr><tr><td>TRPO</td><td>-</td><td>485.39 ± 70.51</td><td>-</td><td>-</td></tr><tr><td>PPO + IMPALA</td><td>-</td><td>-</td><td>8.95</td><td>9.88</td></tr><tr><td>Rainbow + IMPALA</td><td>-</td><td>-</td><td>5.50</td><td>4.24</td></tr><tr><td>Ours</td><td>D2SAC</td><td>-70.77 ± 4.12</td><td>500.00 ± 0.00</td><td>10.00 ± 0.00</td><td>7.00 ± 4.58</td></tr></table>

1) Stackelberg Game: In game theory, the Stackelberg game refers to an iterative process, in which a leader makes the first move and the remaining followers move sequentially, until reaching the equilibrium [168]. In the network context, the leader, typically a network operator, first determines the resource prices or service charges. Network users, i.e., followers, then determine their resource demands based on the given prices, with the goal of balancing their utility against the cost that they paid for the resources. At the Stackelberg equilibrium, the followers cannot increase their utility by changing their demands, and the leader cannot increase its profit by altering the price. In this way, the network efficiency and the participants’ utilities can be balanced, thereby promoting efficient cooperation. With wide adoption, the Stackelberg game provides a robust foundation for designing network incentive mechanisms.

2) Auction: An auction mechanism is widely adopted for incentivizing resource trading [169]. Specifically, an auctioneer conducts an auction for trading network resources, e.g., bandwidth or computing power, that are subject to allocation among bidders. The auction process begins with the auctioneer announcing the resources to be traded and soliciting bids. Each bidder evaluates its demand and willingness to pay, submitting a bid accordingly. The auctioneer then chooses a subset of bidders as the winners based on the bid amount or more complex rules. Finally, the auctioneer calculates the payment from each winner, which could be the bid amount or another value depending on the auction type, and performs the resource

allocation. Auctions can foster competition among bidders, aiming to maximize social welfare in terms of network utilities while satisfying certain constraints like budget balance, i.e., the auctioneer’s revenue should be positive.

3) Contract Theory: Contract-theoretic incentive mechanisms can effectively address network information asymmetry [170]. In this setup, an employer (typically the network operator or service provider) and an employee (the network user) engage in a contractual agreement. The employer designs contracts specifying service charges, Quality of Service (QoS) levels, and resource allocations. However, it may not have complete information about the employees’ preferences and behaviors, which is called information asymmetry [170]. With contract theory, the employers can launch a series of contracts, which ensures the IR, i.e., the utility of the employee is higher than the threshold and IC, i.e., the employees can acquire the highest utility by faithfully following the contracts that they signed properties of the employees. Hence, the employees behave honestly, driven by utilities, circumventing the undesirable effects, such as selfish strategies, caused by the information asymmetry. Contracttheoretic incentive mechanisms have been widely adopted in various network scenarios and have many variants to support high-dimension resource allocation, heterogeneous employees, etc.

4) Shapley Value: The Shapley Value (SV) is a solution from cooperative game theory, quantifying a player’s marginal contribution across potential coalitions. In the incentive mechanism design, the players contribute to the network and are subject to being rewarded. Hence, SV for each player, denoted by i, can be defined as

$$
S V (i) = \sum_ {\mathbb {S} \subseteq \mathbb {N} \backslash i} \frac {| \mathbb {S} | ! (| \mathbb {N} | - | \mathbb {S} | - 1) !}{| \mathbb {N} | !} [ v (\mathbb {S} \cup i) - v (\mathbb {S}) ], \tag {17}
$$

where S represents a coalition without i, v represents the value function, n is the total number of players. SV can be used to allocate rewards, reputation, or credits, in which the player contributing more resources to the network will have higher SVs, thereby encouraging cooperation and resource contribution to the network.

# B. Applications of GDM in Incentive Mechanism Design

From the above description, we observe that the overall procedure of incentive mechanism design is to model the participants’ utility and thus formulate an optimization problem under constraints. Hence, the problem becomes solving an optimization and finding the optimal incentive mechanism strategies that can maximize the utility. Traditionally, researchers find the optimal solutions following the optimization principle. Nonetheless, this method requires complete and accurate information about the network and, more importantly, is not applicable to complex network scenarios with complicated utility functions. Thanks to the strong ability to model complex environments, GDMs provide new possibilities for solving optimization problems. A typical process of adopting GDMs to design incentive mechanisms contains the following steps.

• Model the network states: The first step is to model the network states. To do so, we typically use a vector, say e, which contains many factors, e.g., the upstream and downstream bandwidth, number of participants, bit error rate, and other scenario-specific factors, to depict the given network environment.   
• Formulate the utilities of participants: Based on the factors in e and other hyperparameters, e.g., the weights of these factors, we can formulate the utility function, as well as the associated constraints. Generally, the incentive mechanism design problem is to maximize the utility while satisfying all the constraints.   
• Customize the GDM settings: Thirdly, we customize the GDM settings according to the incentive mechanism design task. The solution space is the universe of all the possible incentive mechanism strategies. For instance, the action space contains all the possible contracts in the contract-theoretic incentive mechanism. The objective function takes the value of the utility function acquired in Step 2 if all the constraints are satisfied. Otherwise, it takes a large negative value as the constraint violation punishment. The dynamic environment is the vector e.   
• Train GDM and perform inference: Finally, we can perform GDM training. The well-trained GDM can then be used for finding the optimal incentive mechanism design in any given network state e. The details of the training process are elaborated in Section II-D.

# C. Case Study: GDM-Based Contract-Theoretic Incentive Mechanism

1) Background: In this part, we conduct a case study to illustrate how to apply GDMs in a practical incentive mechanism design problem. Specifically, we consider an emerging network scenario, namely mobile AIGC [111], [164]. Currently, the success of ChatGPT ignited the boom of AIGC, while the substantial resource costs of large AIGC models prevent numerous end users from enjoying the easy-accessible AIGC services. To this end, researchers recently presented the concept of mobile AIGC, employing Mobile AIGC Service Providers (MASPs) to provide low-latency and customized AIGC inferences, leveraging mobile communications and edge computing capabilities. Hence, the mobile AIGC network is composed of users and MASPs. The former requests AIGC services from MASPs, and the latter operates the local AIGC models to perform inferences. Given that AIGC inferences are resource-intensive, we utilize contract theory to design an incentive mechanism that rewards the MASPs according to their contributed resources.

2) System Model: Considering the diversity and heterogeneity of the current AIGC models, we divide all MASPs into Z levels according to the complexity of their local models, i.e., from level-1 to level-Z. The model complexity of each level of MASPs (denoted by $\theta _ { 1 } , ~ . . . , ~ \theta _ { \mathcal { Z } } )$ can be 1quantified from different aspects, such as the number of model parameters [171]. Typically, the higher the model complexity, the more powerful the model is, and simultaneously, the more computing resources are required during the inference [172]. In our system, we let the index of level follow the ascending order of model complexity, i.e., the higher the model complexity, the higher the index. Finally, we use $p _ { z }$ to denote the proportion of level-z $( z \in \{ 1 , 2 , \ldots , Z \} )$ ) MASPs in the entire mobile AIGC network.   
3) Utility Formulation: For simplicity, we assume users evaluate the AIGC services using the most fundamental metric, i.e., the service latency. Considering the heterogeneity of MASPs, the expected service quality and the required service fees for different levels of MASPs are different. Hence, the utility of users towards level-z $( z \in \{ 1 , 2 , . . . , Z \} )$ MASPs can be defined as [170]

$$
U _ {\mathrm{U}} ^ {z} = \left[ \alpha_ {1} (\theta_ {z}) ^ {\beta_ {1}} - \alpha_ {2} (\mathcal {L} _ {z} / \mathcal {L} _ {m a x}) ^ {\beta_ {2}} \right] - \mathcal {R} _ {z}, \tag {18}
$$

where $[ \alpha _ { 1 } ( \theta _ { z } ) ^ { \beta _ { 1 } } - \alpha _ { 2 } ( \mathcal { L } _ { z } / \mathcal { L } _ { m a x } ) ^ { \beta _ { 2 } } ]$ is a complexity-latency 1 2metric [170], indicating the revenue that the client can gain. $\mathcal { L } _ { z }$ is the latency requirement of users for level-z MASPs, while $\mathcal { L } _ { m a x }$ is the maximum expected latency. $\alpha _ { 1 } , \alpha _ { 2 } , \beta _ { 1 }$ , and $\beta _ { 2 }$ are weighting factors. $\mathcal { R } _ { z }$ 1 2 1represents the rewards that 2users need to pay for level-z MASPs.

For MASPs, they sell the computational resources by performing AIGC inferences for users. Therefore, the utility of level-z MASPs can be defined as

$$
U _ {\mathrm{SP}} ^ {z} = R _ {z} - \left[ \frac {\left(\mathcal {L} _ {m a x} - \mathcal {L} _ {z}\right)}{\mathcal {L} _ {z}} \cdot \theta_ {z} \right], \tag {19}
$$

where [ (Lmax −Lz )L · θz ] represents the costs of level-z MASPs, $\big [ \frac { ( \mathcal { L } _ { m a x } - \mathcal { L } _ { z } ) } { \mathcal { L } _ { z } } \cdot \theta _ { z } \big ]$ z which is determined by two factors, the model complexity $\theta _ { z }$ and the latency $\mathcal { L } _ { z }$ . Firstly, with $\theta _ { z }$ fixed, the higher the $\mathcal { L } _ { z } ,$ i.e., the longer latency can be tolerated by the users, the smaller the costs. Meanwhile, the larger the $\theta _ { z } .$ , the larger the costs of MASPs, since we have mentioned that complex models typically consume more resources for inference.

4) GDM-Based Optimal Contract Generation: Based on the above descriptions, we design the following contracttheoretic incentive mechanism. Specifically, the users produce a specific contract, formed by $\{ { \mathcal { L } } _ { z } , { \mathcal { R } } _ { z } \} ~ ( z \in \left\{ 1 , 2 , \ldots , Z \right\} )$ , for each level of MASPs, which then decide whether to sign.

The contract design should be optimal, maximizing $U _ { \mathrm { C } }$ while satisfying the IR and IC constraints, i.e.,

$$
\max _ {\mathcal {L} _ {z}, \mathcal {R} _ {z}} \sum_ {z = 1} ^ {\mathcal {Z}} p _ {z} U _ {\mathrm{U}} ^ {z} (\mathcal {L} _ {z}, \mathcal {R} _ {z}, \theta_ {z}),
$$

$\mathrm { s . t . } \ ( \mathrm { I R } ) \colon U _ { \mathrm { S P } } ^ { z } ( \mathcal { L } _ { z } , \mathcal { R } _ { z } , \theta _ { z } ) \geq U _ { t h } ,$

$$
z \in \{1, \dots , \mathcal {Z} \},
$$

$$
\mathrm{(IC)} \colon U _ {\mathrm{SP}} ^ {z} (\mathcal {L} _ {z}, \mathcal {R} _ {z}, \theta_ {z}) \geq U _ {\mathrm{SP}} ^ {z} \big (\mathcal {L} _ {j}, \mathcal {R} _ {j}, \theta_ {z} \big),
$$

$$
z, j \in \{1, \dots , \mathcal {Z} \}, z \neq j, \tag {20}
$$

where $U _ { t h }$ is the utility lower bound for MASPs. Finally, we apply the aforementioned four-step procedure to formulate the GDM training paradigm and find the optimal contract design.

• Model the network state: For simplicity, we consider two types of MASPs in the mobile AIGC network. Hence, the network state vector in our case is defined as $[ n , L _ { m a x } ,$ $p _ { 1 } , p _ { 2 } , \theta _ { 1 } , \theta _ { 2 } ]$ .

1 2 1 2• Formulate the utility of participants: There are two utility functions in our case, i.e., U and $U _ { \mathrm { S P } }$ . The former is U SPthe major utility that we intend to maximize. The latter is used in calculating the constraints, i.e., IR and IC.

• Customize the GDM settings: The space is formed as the universe of the contract design. Each bundle is formed as $\{ \mathcal { L } _ { 1 } , \mathcal { R } _ { 1 } , \mathcal { L } _ { 2 } , \mathcal { R } _ { 2 } \}$ . The hyperparameters $\alpha _ { 1 } , \alpha _ { 2 } , \beta _ { 1 }$ , and $\beta _ { 2 }$ 1 2 2are set as 30, 5, 1 and 1, respectively.

2• Train GDM and perform inference: We train the GDM for more than 50000 epochs. The numerical results are discussed below.

5) Numerical Results: Our experiments validate the GDM’s effectiveness in designing incentive mechanisms. Echoing the observations from [164, Fig. 4], we found that GDM performs comparably to PPO in terms of coverage speed. GDM notably excels in achieving significantly higher rewards than PPO. This superior performance is attributed to two key factors: 1) the GDM keeps denoising and testing new samples in the training process, which fine-tunes the parameters of the solution generation network, and 2) the randomness and dynamics in the wireless environment can be overcome due to the higher sample quality. Additionally, our analysis extends to contract design under three heterogeneous network states, examining the utility function $U _ { \mathrm { U } }$ . Our findings Uindicate that GDM consistently ensures high $U _ { \mathrm { U } }$ values, Umaintaining stability and meeting the IC and IR constraints across various network conditions.

# V. SEMANTIC COMMUNICATIONS

In this section, we consider the SemCom technique and explore the involvement of GDM within the SemCom framework [46], [50], [173].

# A. Fundamentals of Semantic Communications

SemCom [46] refers to extracting and transmitting the most relevant semantic information from raw data to the receivers using AI technology. It aims to lower network loads by selectively transmitting meaningful and contextually relevant information instead of transmitting the entire raw data [174]. SemCom consists of three main components: the semantic encoder, the wireless channel, and the semantic decoder [175].

1) Semantic Encoder: It is responsible for extracting and transmitting relevant semantic information from the raw data provided by the transmitting users [47]. This is typically achieved by utilizing neural networks, which encode the raw data into meaningful semantic representations. The semantic encoder employs various techniques such as feature extraction and dimensionality reduction to capture the essential semantic information [176].

2) Wireless Channels: However, during transmission, the semantic information is subject to physical noise introduced by the wireless channel [177]. Physical noise refers to external factors that interfere with the transmission of the message. It can result in noise-corrupted semantic information, which is then transmitted to the receivers for further processing. The channel component of SemCom handles the transmission of this noise-corrupted semantic information, taking into account the wireless channel characteristics and the potential effects of noise and interference [178].

3) Semantic Decoder: The receivers employ a semantic decoder, $\mathrm { e . g . }$ , implemented by neural networks, to decode the received noise-corrupted semantic information and reconstruct the distorted data. The semantic decoder utilizes its learning capabilities to reverse the encoding process and extract the intended semantic meaning from the received information [179]. Semantic noise arises from the use of symbols that are ambiguous to the receivers. It can also occur when there is a mismatch in understanding between the sender and receiver. By employing sophisticated neural network architectures, the semantic decoder aims to minimize the effects of semantic noise and accurately obtain the original semantic data.

The ultimate objective of SemCom is to effectively convey the intended meaning of the transmitted symbols, rather than transmitting the raw bits directly, thereby reducing communication overhead and enhancing communication effectiveness [173].

# B. Case Study: GDM-Based Resource Allocation for SemCom-Aided AIGC Services

1) Motivation: There are several examples of integrating GenAI technologies in SemCom [180]. For instance, GANs have been employed to develop semantic decoders that tackle the out-of-distribution problem of SemCom [181]. GANs are used to generate realistic and meaningful semantic information based on the available data. Additionally, a variational autoencoder (VAE) is utilized to calculate the lower bound of semantic distortion and derive the corresponding loss function [182]. By incorporating GANs and VAEs, SemCom can enhance the accuracy and fidelity of semantic decoding, thereby improving the overall communication performance [175].

To elucidate the role of GDMs in SemCom, we consider their application in an AIGC service process, illustrated in Fig. 14. The process begins with edge devices collecting primary data, such as photographs. These edge devices then extract semantic information from the data, focusing on meaningful content rather than raw data transmission. The extracted semantic information is significant for AIGC Service Providers (ASPs). Then, ASPs employ GenAI models, inclusive of GDMs, to conduct AIGC inference, transforming semantic information into enriched content, such as stylized animations [183]. The final stage involves multimedia service providers, like Metaverse platforms, leveraging this semantically-enriched content to craft digital offerings for endusers, such as animated avatars [50]. We formulate a unified resource allocation problem for this workflow, considering the limited computing and communication resources allocated to the semantic extraction, AIGC inference, and graphic rendering modules. The objective is to maximize the overall utility by efficiently allocating these resources.

![](images/fa50c608b9e689f8363b52971e649adbf33470424d5ce57e55a46d1cdae10151.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Data Collection"] --> B["Text/Image/Audio/Video"]
    B --> C["Semantic Extraction"]
    D["AIGC Training"] --> E["Semantic Information"]
    E --> F["AIGC Inference"]
    G["Graphic Rendering"] --> H["Digital contents"]
    H --> I["Callback Results"]
    I --> J["Step1: Solution Space Definition Available Bandwidth"]
    I --> K["Step2: Objective Function Definition Utility"]
    I --> L["Step3: Dynamic Environment Definition Channel Conditions and Computing Abilities"]
    M["Step4: Training and Inference The Optimal Strategy"] --> L
```
</details>

Fig. 14. Resource allocation problem in a SemCom-aided AIGC service scenario. First, the edge devices collect raw data, e.g., photos, and extract semantic information. Then, the AIGC service providers use the received semantic information to perform the AIGC inference using GenAI models to obtain meaningful content, e.g., animated style photos. These contents are further used by the multimedia service provider, e.g., Metaverse service provider, to render digital content for the users, e.g., animated style avatars [50].

2) Problem Formulation: The integration gain includes the computing time for semantic extractio n (T comps ), $( T _ { s } ^ { c o m p } )$ AIGC inference $( T _ { a } ^ { \overline { { c o } } m p } )$ , and graphic rendering $( T _ { m } ^ { c o m p } )$ comp ) These times are influenced by the available computing resources and the current computing resource congestion, introducing uncertainty to the utility optimization problem. Concurrently, the transmission time is associated with the transfer of semantic information c $( T _ { a } ^ { c o m m ` }$ ), AIGC content $( T _ { m , u } ^ { c o m m } )$ ), and rendering results $( T _ { m , d } ^ { c o m m } )$ . These times are affected by the allocated communication resources to each part. Specifically, we consider the allocation of bandwidth resources with a $W _ { a } ^ { m } , \ W _ { m } ^ { s } ,$ and $W _ { s } ^ { a }$ denoting the bandwidths for semantic information, AIGC content, and rendering results transmissions, respectively. The objective function is given by $\ln ( R _ { s } ^ { a } ) + \ln ( R _ { a } ^ { m } ) +$ $\ln ( R _ { m } ^ { s } )$ , where $R _ { s } ^ { a } , R _ { s } ^ { a }$ and $R _ { s } ^ { a }$ are the data rates for the transmissions of semantic information, AIGC content, and rendering results, respectively. The logarithmic form is used as we assume that the subjective user experience follows a logarithmic law to the objective performance metrics [184]. The objective function is considered as the reward in the GDM-based resource allocation scheme to find a near-optimal strategy. Following [185], [186], we construct the bandwidth allocation problem as follows:

$$
\max _ {W _ {a} ^ {m}, W _ {m} ^ {s}, W _ {s} ^ {a}} \ln (R _ {s} ^ {a}) + \ln (R _ {a} ^ {m}) + \ln (R _ {m} ^ {s}),
$$

$$
\mathrm{s.t.} T _ {s} ^ {\text {comp}} + T _ {a} ^ {\text {comm}} + T _ {a} ^ {\text {comp}}
$$

$$
+ T _ {m, u} ^ {c o m m} + T _ {m, d} ^ {c o m m} + T _ {m} ^ {c o m p} \leq T _ {\max},
$$

$$
W _ {a} ^ {m} + W _ {m} ^ {s} + W _ {s} ^ {a} \leq W _ {\max}. \tag {21}
$$

3) GDM-Based Resource Allocation Scheme Generation: The optimal bandwidth resource allocation scheme can be generated according to the following steps

• Step 1: Solution Space Definition: The solution space in the proposed problem encompasses allocating available bandwidth for transmission among the semantic extraction, AIGC inference, and rendering modules. The goal is to optimize the utilization of bandwidth resources to ensure efficient communication and collaboration between these modules.

• Step 2: Objective Function Definition: The training objective of the proposed problem is to maximize the utility of the system, which is served as rewards that are obtained by dynamic resource allocation strategies. It should consider the total tolerable transmission time and available resources among these modules.

• Step 3: Dynamic Environment Definition: GDMs are utilized to generate an optimal bandwidth allocation scheme based on a given set of wireless channel conditions and computing capabilities involved in the three modules, such as the semantic entropy and the transmit power. Semantic entropy is defined as the minimum expected number of semantic symbols about the data that is sufficient to predict the task [186]. The semantic entropy and the transmit power are randomly varied within a specific range associated with a given task.

• Step 4: Training and Inference: The conditional GDM generates the optimal bandwidth allocation strategy by mapping different environments to bandwidth allocation designs. The optimal strategy is achieved through the reverse process, where the GDM trains and infers the corresponding allocation policies to maximize the expected cumulative utility.

4) Numerical Results: As studied in [50], the proposed method is implemented on a system running Ubuntu 20.04, equipped with a 32-core CPU and an NVIDIA RTX A5000 GPU. The dynamic environment parameters are sampled using uniform distributions, while the additive Gaussian noise is applied by sampling from normal distributions within the AIGC and rendering modules. [50, Fig. 5] presents the test reward results for GDM and DRL, i.e., PPO in the bandwidth allocation task. This comparison is conducted over 400 training epochs with learning rates set at $3 \times 1 0 ^ { - 7 }$ and $3 \times 1 0 ^ { - 6 } .$ , buffer size 1,000,000, and an exploration noise of 0.01 according to [50]. As depicted in [50, Fig. 5], the curve for DRL exhibits greater volatility compared to that of GDM. Besides, the reward values for GDM are more compact, indicating more stable performance. As the number of training epochs increases, neither exhibits a clear upward or downward trend, which confirms both GDM and

DRL converge. Therefore, GDM outperforms DRL in the bandwidth allocation task. To compare the utilities generated by various bandwidth allocation strategies, characterized by the parameters $[ W _ { s } ^ { a } , W _ { a } ^ { m } , W _ { m } ^ { s } ]$ , GDM and PPO select two distinct network states under dynamic network conditions. These are designated as $\mathbf { G D M } _ { 1 } , \mathbf { G D M } _ { 2 } , \mathbf { P P O } _ { 1 }$ , and $\mathbf { P P O } _ { 2 } .$ . 1 2 1 2The definition of network states follows that presented in [50]. As shown in [50, Fig. 6], the strategies exhibit close alignment in the allocation of bandwidth for $\boldsymbol { W } _ { a } ^ { m }$ , yet there are considerable differences in the other two parameters, $W _ { s } ^ { a }$ and $W _ { m } ^ { s }$ . There is a significant variation in allocating different types of bandwidth across various network states. Additionally, the strategies generated by GDM demonstrate higher utilities than PPO across different network states. Therefore, GDM outperforms PPO in terms of generated strategies in dynamic environments. This superiority can be attributed to the optimal bandwidth allocation mechanism inferred by GDMs, which enables fine-tuning output through denoising steps and facilitates exploration. Consequently, the proposed mechanism exhibits enhanced flexibility, mitigating the effects of uncertainty and noise encountered during the transmission and computing among semantic extraction, AIGC inference, and graphic rendering modules.

# VI. INTERNET OF VEHICLES NETWORKS

In this section, we introduce the concept of IoV networks, discuss the role of GDM in IoV networks, and provide a case study [187], [188].

# A. Fundamentals of IoV Networks

Drawing inspiration from the Internet of Things (IoT), the IoV network turns moving vehicles into information-gathering nodes [187], [189]. Harnessing emerging information and communication technologies facilitates network connectivity between vehicles and other elements, i.e., other vehicles, users, infrastructure, and service platforms. For the IoV network, the goal is to enhance the overall intelligence of the vehicle, as well as improve the safety, fuel efficiency, and driving experience [187].

In the IoV network, vehicles are regarded as data agents for collecting and disseminating data such as traffic patterns, road conditions, and navigation guidance [190]. Managing large amounts of data in the IoV network is a very complex task. As a remedy, GenAI is proposed. In particular, GenAI performs the critical functions of organizing and restoring the data collected within the IoV. Additionally, it can generate synthetic data, enhancing the efficacy of machine learning model training within the network. Furthermore, the contributions of GenAI go beyond simple data management. It utilizes the collected data to inform the real-time decision-making process. This includes predicting traffic conditions, identifying potential hazards, and determining the best route for the driver.

# B. Applications of GDM in IoV Networks

The field of GenAI is composed of several models, and each model brings unique capabilities to various applications. The GDM has attracted much attention among these models due to its unique advantages. Applying the GDM model within IoV networks yields promising results. In particular there are two specific applications as follow:

![](images/21cfa35bcda4a3c23436f85ef25b79561b3f0896be51b64859bee7050142350e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Vehicular 1"] --> B["Video"]
    B --> C["Features Tensor"]
    C --> D["Text Encoder"]
    D --> E["Features Tensor"]
    E --> F["Image"]
    F --> G["Features Picture"]
    G --> H["Text"]
    H --> I["CLIP Text Encoder"]
    I --> J["Features Tensor"]
    J --> K["Network"]
    K --> L["Network"]
    L --> M["Features Tensor"]
    M --> N["Decoder"]
    N --> O["Vehicular 2"]
    O --> P["Adapters"]
    P --> Q["Network"]
    Q --> R["Noise"]
    R --> S["Noise"]
    S --> T["Feedback to Vehicular 2"]
```
</details>

Fig. 15. GenAI-enabled IoV network, where the semantic information extraction step, image skeleton extraction step, wireless transmission step, GenAI-enabled image generation step and image reconstruction step are involved [188].

1) Recovery of Images Sent by Vehicles: In IoV networks, vehicles usually transmit images to communicate information about their environment for safe driving. However, these images may be distorted or lose quality due to transmission errors, noise, or interference. The GDM, with its ability to generate high-quality images, can be employed to recover the original quality of these transmitted images. In particular, the vehicles adopt semantic technology to extract information from images, i.e., as a prompt at the transmitter, and recover it using GDM at the receiver. By doing so, the transmitted data and communication delays can be reduced in IoV.

2) Optimization Based on GDM: The GDM iterative framework suits the IoV network optimization tasks, including path planning and resource allocation [103]. Using stochastic differential equations (SDEs), the model refines solutions progressively via a diffusion process. For example, in path planning, GDM begins with a random path, making iterative refinements based on performance criteria such as travel time and energy consumption. The model uses gradients of these metrics to guide the path updates toward an optimal or nearoptimal solution, stopping iterations when updates become negligible.

Therefore, thanks to the ability to recover high-quality images from transmitted data and iteratively optimize solutions, the GDM provides a powerful tool for enhancing the efficiency and robustness of IoV networks.

# C. Case Study: A GenAI-Driven IoV Network

In this part, we conduct a case study to illustrate how to apply GDMs in IoV design.

1) System Model: Under the 3GPP V2X standard [191], we consider a GenAI-driven IoV network with multiple V2V links as shown in Fig. 15. We aim to ensure reliable, realtime information transmission in our considered network. The orthogonal frequency division multiplexing technology is adopted, where each V2V link can achieve dynamic transmission rates on different sub-channels. Moreover, a successful image transmission rate is introduced as a constraint. This rate is affected by different parameters such as achievable transmission rate, image similarity measure, channel coherence time, and generated image payload.

2) Problem Formulation: In our considered work, We consider transmission rate and image similarity as the performance indicators, and hence they are combined into a unified QoE indicator and used as the optimization goal. As described in (22), an optimization problem is formulated to maximize the system QoE under the constraints of the transmission power budget and the probability of successful transmission for each vehicle, where the channel selection strategy, the transmission power for each vehicle, and the diffusion steps for inserting the skeleton are jointly optimized.

$$
\max _ {\left\{P _ {v}, d _ {v}, c _ {v} \right\}} \sum_ {v \in V} \mathrm{QoE} (v) \tag {22a}
$$

$$
\text { s.t. }: \sum_ {v \in V} p _ {v} \leq P _ {\max}, (\text { PowerBudget }) \tag {22b}
$$

$$
\operatorname * {P r} (v) \geq \operatorname * {P r} _ {\min}, (\text { Transmission   Constraint }) (2 2 c)
$$

$$
c _ {v} \in C, (\text { Channel   Selection   Constraint }) \tag {22d}
$$

$$
d _ {v} \in \mathbb {N} ^ {+}, (\text { Diffusion   Steps   Constraint }) \tag {22e}
$$

$$
\forall v \in V.
$$

3) GDM-Based Joint Channel Selection and Power Allocation: For the formulated problem, a GDM-based DDPG approach is proposed, where the corresponding three tuples of MDP and the network design are as follows.

• MDP design: The state space consists of the current information and previously selected actions, where the current information includes the channel information of each V2V link, the transmission rate of each V2V link, and the generated image payload. The action space consists of the selectable channel, the transmit power, and the diffusion steps for inserting the skeleton. The reward function consists of an instant reward term and a penalty term. The design principle follows that a larger penalty will be given when the constraints are not met, while an instant reward will be given when the constraints are met or the goal becomes higher. Accordingly, the agent can achieve high QoE while satisfying the corresponding constraints.

• GDM-based IoV network design: In our proposed approach, we adopt the GDM-based network. Specifically, the GDM-based network design employs GDMs in two distinct roles. Firstly, GDMs reconstruct received images at the receivers in vehicular networks. Leveraging the multi-modal technique, we utilize the contrastive language-image pre-training (CLIP) framework to incorporate both text and image information in the diffusion process for image reconstruction, which is a task that incorporates denoising steps for image generation and transmits power values. Secondly, another

GDM is tasked with optimizing the number of denoising steps, the channel selection strategies, and the transmit power values. In particular, the IoV network uses a diffusion process to map environmental states to resource allocation strategies, incorporating a crucial denoising step to eliminate less important information and enhance signal clarity during training. The corresponding network operates through a chain mechanism, where each step incrementally refines the solution, ensuring it adapts to temporal dependencies and dynamic environments. This approach can be fine-tuned to generate samples over multiple time steps, enhancing its ability to handle tasks with long-term dependencies.

4) Numerical Results: We conduct experiments to prove the validity of our proposed method. In our simulation setup, the GDM-based approach utilizes a learning rate 3e-7 for both the actor and the critic network. The exploration noise is set at 0.01, and the time step of the diffusion chain is 1. We employ a tanh activation function with a hidden layer of 256 units. The output layer is designed as the cardinality of the action space, while the input layer corresponds to the cardinality of the state space. The discount factor γ is set to 0.95. It is shown that the average cumulative rewards obtained by different types of schemes versus the number of training episodes, where the curves have been smoothened to show the trend more clearly. Our proposed GDM-based approach always outperforms other baselines (i.e., DRL-DDPG, DRL-DQN, greedy, and random schemes) under the same parameter settings when all schemes converge. Although the proposed GDM-based DDPG approach and DDPG-based obtain roughly similar rewards during the training phase, the proposed GDMbased DDPG approach outperforms DDPG after convergence. The reason is that traditional DRL methods may not be able to effectively filter out noise (i.e., useless information in the buffer) in environments. In contrast, the diffusion model in the GDM-based method enhances environment exploration, and its denoising process helps distinguish signal from noise, thereby improving learning results to find reasonable actions.

# VII. MISCELLANEOUS ISSUES

In this section, we discuss the applications of GDM to several other network issues, including channel estimation, error correction coding, and channel denoising.

# A. Channel Estimation

1) Motivations: In wireless communication systems, the wireless channel depends on various factors such as fading, interference, and noise, which can lead to distortions in the received signal. Consequently, researchers introduce channel estimation techniques to estimate the channel response, which can be used to mitigate the impacts caused by the aforementioned factors, thereby enhancing the quality of the received signal. As such, accurate channel estimation is crucial for reliable communication and efficient use of the available bandwidth [192].

So far, several kinds of channel estimation techniques have been proposed, including pilot-based, compressed sensingbased, etc. The pilot-based methods use known pilot symbols inserted in the transmitted signal to estimate the channel response. For instance, the minimum mean square error (MMSE) based method achieves channel estimation by multiplying the received signal with the conjugate of the transmitted signal, followed by division by the sum of the power of the transmitted signal and the noise variance. This method not only minimizes the mean square error between the received signal and the estimated signal but also considers the noise variance, which is important for determining the reliability of the estimated channel coefficients [193]. The compressed sensingbased methods exploit the sparsity of the channel response to estimate it from a small number of measurements. For example, the authors in [194] create a training signal using a random sequence with a known pilot sequence. At the receiver, first-order statistics and the compressed sensing method are applied to estimate the wireless channels with sparse impulse response. Unlike these two methods, data-driven methods employ machine learning algorithms to learn the channel response from the received signal without relying on any prior knowledge of the channel during the offline training phase. After trained, the data-driven methods can estimate the channel in an online phase. For instance, the authors in [195] first use the convolutional neural network (CNN) to extract channel response feature vectors, and then employs recurrent neural network (RNN) for channel estimation. Besides, there are some other techniques, such as optimization-based methods, which use mathematical optimization, such as convex optimization, to estimate the channel response, and hybrid methods that combine different techniques to improve the accuracy and efficiency of channel estimation.

While effective, existing methods still faces several challenges. One of the main challenges is the dynamic nature of the channel, which means that the channel can change rapidly due to various factors such as mobility and interference. This requires channel estimation to be robust to test-time distributional shifts [196]. These shifts naturally occur when the test environment no longer matches the algorithm design conditions, especially at the user side (could be transmitter or receiver), where the propagation conditions may change from indoor to outdoor, whenever the user is moving. An effective solution to this challenge is to use GenAI for robust channel estimation, because of the following main reasons.

• The GenAI model can extract complex patterns from large amount of data and learn in a changing environment. This not only enhances the model’s generalization ability but also enables it to adapt to the dynamic characteristics of the channel, thereby improving the robustness of the estimation.   
• The GenAI model can directly learn the distribution of channel responses from the received signals and use the structure captured by the deep generative model as a prior for inference, eliminating the need for prior knowledge of the sparsifying basis.

![](images/7fd718c5086a6f3514ed96472307eb4847482dbe17266d5f74d7e4c4388dcf87.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph_TrainingPhase["Training phase"]
        A["h"] --> B["⊕"]
        C["CN(0,σ²I)"] --> B
        B --> D["tilde{h}"]
        D --> E["Diffusion model"]
        E --> F["Loss function"]
        G["∇logₚₕ(tilde{h})"] --> F
    end
    subgraph_InferencePhase["Inference phase"]
        H["h_t"] --> I["Pilot consistency"]
        I --> J["Diffusion model (frozen)"]
        J --> K["⊕"]
        L["ηₜ"] --> M["×"]
        N["CN(0,2βηₜI)"] --> M
        M --> O["h_{t+1}"]
    end
    style TrainingPhase fill:#f9f,stroke:#333
    style InferencePhase fill:#bbf,stroke:#333
```
</details>

Fig. 16. During training, the noise is first added to h to obtain h. Then a regression target for the gradient of $\log _ { p _ { H } } ( \tilde { \mathbf { h } } )$ is produced. After that, the log ( )l -loss is used to train the parameters of the deep neural network via backpropagation. After training, the current channel estimate is updated by a pilot consistency term, a diffusion update, and added noise to achieve inference.

Next, we further illustrate applications of GenAI in channel estimation, using MIMO channel estimation via the GenAI model as a case study [196].

2) Case Study: MIMO Channel Estimation Utilizing Diffusion Model: Channel estimation using diffusion model [196] primarily involves training and inference phases, as shown in Fig. 16. The training phase involves using a deep neural network to learn the underlying structure of the channel from a set of noisy channel estimates. The main steps include the following:

• Step 1: Using the received pilot symbols to calculate the noisy channel estimation h.   
• Step 2: Adding the noise to the training channel h to produce a perturbed channel h˜.   
• Step 3: Computing the gradient of $\log _ { p _ { H } } ( \tilde { \mathbf { h } } )$ .   
• Step 4: Producing a regression target for the gradient using the diffusion model.   
• Step 5: Training the parameters of the deep neural network using back-propagation and the l -loss.

2The inference stage involves utilizing the trained model to estimate the channel based on a set of received pilot symbols. The primary steps are as follows:

• Step 1: Updating the current channel estimation via the pilot consistency term, which enforces consistency between the received pilot symbols and the estimated channel.   
• Step 2: The diffusion update is applied to the channel estimate, which smooths out the estimate and helps to reduce noise.   
• Step 3: To prevent the model from converging to a suboptimal solution, noise is added to the updated channel estimate at each step.   
• Step 4: The process is repeated until convergence, at which point the final estimate of the channel is produced.   
It is noteworthy that the iterative algorithm operates independently of the training phase and can accommodate other impairments such as interference scenarios or few-bit quantization of the received pilots.

The proposed model is evaluated by training an NCSNv2 model [197] on complex-valued channel matrices. The model architecture, RefineNet [198], comprises eight layers and approximately 5.2 million parameters. To accommodate complex-valued inputs, the real and imaginary components of the matrix are processed as two separate input channels. Training is performed on a dataset of 20, 000 channel realizations, derived from the clustered delay line (CDL) channel model, with an equal distribution between two antenna spacings [196].

Fig. 2 in [196] presents the test results for in-distribution CDL channels in a blind SNR configuration with $\alpha = 0 . 4$ . The top plot reveals that the comparison algorithm, WGAN [199], captures some aspects of the channel structure for very low antenna spacing. However, its performance peaks, about −26 dB, rapidly in high SNR conditions. Another comparative algorithm, i.e., Lasso [200], similarly exhibits a trend, with its peak value approximately at −22 dB. This effect is more pronounced with an antenna spacing of half wavelength and fewer structural components, indicating that neither baseline employs a suitable prior knowledge. In contrast, the diffusion-based approach exhibits a near-linear reduction in the normalized mean square error (NMSE), aligning with the theoretical findings in [201], without explicit learning of a prior. At an SNR level of 15 dB, the NMSE of the diffusion-based approach is over 12 dB lower than both baseline methods, underscoring the superiority of the diffusion-based approach.

# B. Error Correction Coding

1) Motivations: Developing codes that can be decoded effectively in noisy environments is imperative in wireless communications. Decoding methods fall into two categories: hard and soft decoding [202]. Hard decoding strictly uses the most probable value of the received signal, ignoring any signal quality metrics. In contrast, soft decoding incorporates the most probable signal value and additional signal quality information, thus improving decoding accuracy. While these strategies offer some level of efficacy, decoding complexity escalates with advanced encoding systems, such as algebraic block codes, presenting significant challenges [202]. Decoding these systems optimally often involves adhering to the maximum-likelihood principle—identifying the codeword that maximizes the likelihood of the received signal. However, this approach is identified as NP-hard, implying that an exhaustive search is generally required for the optimal solution, rendering it impractical for real-world applications.

Recent studies, notably those employing model-free machine learning approaches, have aimed at addressing this challenge [203]. Specifically, a transformer-based decoder, which integrates the encoder within its architecture, demonstrated superior performance over traditional methods with significantly reduced time complexity, as detailed in [203]. Despite these advancements, the modelfree paradigm faces critical limitations. Firstly, it demands substantial storage and memory capacity, posing issues for resource-limited devices. Secondly, its non-iterative nature mandates a uniform, computationally demanding neural decoding procedure, irrespective of the extent of codeword corruption.

![](images/0ad669fc2f30612080577e3d33c8f03396ef98546fb944fd201260cb9823794d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Encoder"] --> B["G"]
    B --> C["BPSK"]
    C --> D["x_s"]
    D --> E["x_s + z"]
    E --> F["y"]
    F --> G["Decoder"]
    G --> H["h(·)"]
    H --> I["Σs(y)"]
    I --> J["ε_θ(·)"]
    J --> K["ŷ"]
    L["z~N(0,σ²I_n)"] --> M["x_s + z"]
    M --> N["y"]
    N --> O["Reverse GDM"]
    O --> P["ε_θ(·)"]
```
</details>

Fig. 17. The denoising diffusion error correction codes architecture, where the decoding is performed via the reverse diffusion process [204].

To this end, GDMs have been explored for decoding tasks, as evidenced by recent works [204], [205]. GDMs employ an iterative decoding approach while efficiently adapting to varying degrees of codeword corruption and reducing computational complexity. Specifically, the authors in [204] consider the corruption of channel codewords as a forward diffusion process of GDM. This perspective allows the corruption to be methodically reversed using an adaptive denoising diffusion probabilistic model, presenting a sophisticated yet efficient solution for error correction and signal restoration in communication systems. Moreover, the authors in [205] proposed a diffusion-based image restoration method, Diffusion-based Error Contraction and Correction (DiffECC), leveraging an Ordinary Differential Equation (ODE)-based sampler to formulate a detailed update equation for conditional diffusion. The application of the Adam optimizer enhances neural estimations. The objective is for backward diffusion to reach a stable point at each timestep, aiming for the error term $\epsilon _ { \theta } ( x _ { t } , t )$ to meet a set error benchmark , especially in generating clean images. For image restoration, where unknown factors initially distort inputs, DiffECC innovatively adjusts neural predictions by amalgamating outputs from consecutive denoising stages as a regularization factor.

2) Case Study: Denoising Diffusion Error Correction Codes: As shown in Fig. 17, the elements of the denoising diffusion used for decoding and the proposed architecture are summarized, where the training process is as follows.

• Decoding as a Reverse Diffusion Process. In this stage, a process of “forward diffusion” is used to process codewords sampled from a particular encoding distribution. Specifically, the process gradually transmits codewords by gradually adding a small amount of Gaussian noise, with the size of each step controlled by a specific variance table. Next, data transmission over a noisy communication channel is regarded as a modified iterative diffusion process that requires inversion at the receiving end to decode the original data. Finally, decoding is regarded as a reverse diffusion process, transforming the posterior probability into a Gaussian distribution as per the Bayesian theorem [203]. The goal of the decoder can be defined to predict the channel’s noise.

• Denoising via Parity Check Conditioning. In the decoding process, it is regarded as the reverse denoising process of the GDM, which relies on time steps and can reverse the entire diffusion process by sampling Gaussian noise corresponding to the final step. During training, a time step is randomly sampled, generating noise and a syndrome requiring correction. Owing to its invariance to the transmitted codeword, diffusion decoding can be trained using a single codeword. During inference, the denoising model predicts multiplicative noise, converts it into additive noise, and performs the gradient step in the original additive diffusion process.

Fig. 4 in [204] shows BER obtained by three schemes in terms of the normalized SNR values, i.e., $E _ { b } / N _ { 0 }$ (EbNo), 0over the Rayleigh fading channel environment. It shows that with the increment of the value of EbNo, the GDM-based scheme is superior to other benchmarks. In particular, when the EbNo is 4 dB, the BER obtained by GDM scheme is 50% of that obtained by Binary Phase (BP) scheme, and 11% of that obtained by error correction code transformer (ECCT) scheme [203]. The reason is that the GDM is able to learn to decode, even under some serious noisy fading channels.

# C. Channel Denoising

1) Motivations: GDM-based models are characterized by the ability to add Gaussian noise to the training data gradually and then learn to restore the original data from the noise through a back sampling process. The process is similar to that of a receiver in a wireless communication system, which is required to recover the transmitted signal from the noisy received signal.

Thus, in [206], a GDM-based approach for denoising wireless communication channels is introduced to predict and mitigate channel noise for post-channel equalization and enhance overall system performance. Distinctively, this GDM-based model proposed in [206] operates solely on the principles of forward diffusion, independent of any received signal. When integrated into semantic communication systems utilizing Joint Source-Channel Coding (JSCC), the GDM-based model significantly minimizes the disparity between transmitted and received signals across both Rayleigh fading and additive white Gaussian noise (AWGN) channels. Furthermore, the authors in [207] assess the diffusion model’s capabilities in channel generation and its performance in Endto-End (E2E) communication scenarios, subject to AWGN and authentic Rayleigh fading channels. Their findings validate the diffusion model’s ability to learn the channel distribution accurately. Additionally, it is shown that the E2E framework, facilitated by the diffusion model, achieves a symbol error rate remarkably comparable to that obtained with a channel-aware framework, applicable to both AWGN and Rayleigh fading environments.

2) Case Study: GDM-Based Channel Denoising Model: As shown in Fig. 18, the joint GDM and JSCC architecture is summarized, where the training process is as follows.

![](images/bd94105f5372f78a9c36353ab820f0b1b743f089dadc7df889be6c65ded825f0.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["JSCC Encoder"] -->|x| B["Wireless Channel"]
    B --> C["AWGN Channel"]
    C --> D["Equalization (MMSE)"]
    D --> E["Rx Channel Estimation"]
    E --> F["GDM"]
    F -->|ŷ| G["JSCC Decoder"]
    G -->|y| D
    D -->|yr| H["Rayleigh Channel"]
    H --> C
    style A fill:#cce5ff,stroke:#333
    style F fill:#cce5ff,stroke:#333
```
</details>

Fig. 18. The joint GDM and JSCC system architecture, where GDM is trained using a specialized noise schedule [206].

• Conditional Distribution of The Received Signals: Realvalued and complex-valued symbols are transformed and transmitted in the wireless channel, where the transformation combines the effects of Rayleigh fading gain and additive white Gaussian noise. The received signal is then processed through an MMSE equalizer to produce an equalized complex signal. Study conditional distributions of real-valued vectors using known signal and channel state information. Based on the noise impact and channel state, the signal is reparameterized and a GDM-based channel denoising model is trained to obtain noise estimates.

• Training Algorithm of GDM: In the training process of GDM, the original source signal is first represented in a new parameterized form. At the beginning of training, the Kullback-Leibler divergence [171] is mainly used to optimize the variational upper bound of the negative log-likelihood. During training, the optimal value of a key hyper-parameter is required to be determined. Next, the optimization objective for a series of loss functions is simplified by re-parameterization and re-weighting methods. Finally, the overall loss function is minimized, effectively recovering the original source signal.

Reference [206, Figs. 5 and 6] show PSNR obtained by three schemes regarding the SNR over the AWGN channel and Rayleigh fading channel environments. To achieve optimal performance, both GDM-based JSCC scheme and JSCC scheme must be retrained for a given SNR. It shows that for different values of SNR, the GDM-based JSCC scheme is superior to others. For example, over Rayleigh fading channel with SNR of 20 dB, compared with the JSCC scheme, the GDM-based JSCC scheme can obtain about 1.06 dB gain.

# VIII. FUTURE DIRECTIONS

This section elucidates potential research avenues warranting further examination.

# A. Space-Air-Ground Integrated Network

The Space-Air-Ground Integrated Network (SAGIN) is a promising paradigm for future wireless networks, characterized by its three-dimensional coverage, high capacity, and reliable communications [208], [209], [210]. However, the optimization of SAGIN is a complex task due to the high dimensionality of the network configuration, the heterogeneity of the network elements, and the dynamic nature of the network environment [211], [212]. GDMs, with their ability in complex data distribution modeling, could be a powerful tool for optimizing SAGIN [213].

• Dynamic Network Environment Modeling and Prediction: The dynamic nature of the SAGIN environment poses a significant challenge for its optimization [209], [214]. GDMs can be used to model and predict these dynamic network environments. This would allow for more efficient resource allocation, network scheduling, and routing strategies, as the predictions could provide valuable insights into future network states [215].   
• Synthetic Network Scenario Generation: Testing and validating network optimization algorithms require a variety of network scenarios [216]. GDMs can generate synthetic network scenarios that closely mimic real-world conditions, providing a robust platform for testing and validating these algorithms.   
• Network Scheduling and Routing: SAGIN involves a variety of network elements, each with its unique characteristics and requirements [217], [218]. GDMs can capture these unique characteristics and model the complex interactions between different network elements, facilitating more efficient network scheduling and routing strategies.

# B. Extremely Large-Scale MIMO

Extremely Large-Scale MIMO (XL-MIMO) is an emerging technology that is expected to play a pivotal role in the 6G of wireless mobile networks [219], [220], [221]. XL-MIMO offers vast spatial degrees of freedom by deploying an extremely large number of antennas, leading to significant enhancements in spectral efficiency and spatial degrees of freedom. However, implementing XL-MIMO introduces new challenges, including the need for more flexible hardware designs, a much larger number of antennas, smaller antenna spacing, new electromagnetic characteristics, and near-fieldbased signal processing schemes [222], [223]. GDMs can be instrumental in addressing these challenges and optimizing the performance of XL-MIMO systems. Here are some potential research directions:

• Hybrid Channel Estimation and Modeling: XL-MIMO systems involve a large number of antennas, leading to high-dimensional data [224], and also the co-existence of near-field and far-field channels within the coverage of cellular networks. Especially, in the near-field channel, the channel response vectors depend on both the distance and direction between the transceiver of each antenna element, unlike the far-field channel. Therefore, the increased “huge” complexity for near-field channel estimation may not be resolved with the conventional approaches. GDMs can be used to model and estimate such hybrid channel state information efficiently. They can exploit the inherent graph structure in the spatial domain, where antennas can be considered as nodes and the spatial correlation between antennas as edges. This

can lead to more accurate and efficient channel estimation methods.

• Signal Processing: The signal processing in XL-MIMO systems can be complex due to the large number of antennas and the near-field communication characteristics. Especially, in the latter case, the interference caused by multi-user transmissions can be effectively mitigated by utilizing the higher degree of freedom existing in the distance and direction of near-field channel response vectors. GDMs can be used to develop efficient signal processing algorithms that can handle high-dimensional data and exploit the spatial correlation in the antenna array. This can lead to improved performance in terms of data rate and reliability.   
• Hardware Design and Implementation: XL-MIMO systems involve different hardware designs, such as uniform linear array (ULA)-based, uniform planar array (UPA)-based, and continuous aperture phased (CAP)- based XL-MIMO. GDMs can be used to model and analyze these different designs, helping to understand their characteristics and interrelationships. This can guide the design and implementation of XL-MIMO systems.

# C. Integrated Sensing and Communications

The ISAC unifies wireless sensing and communication systems to efficiently employ limited resources for mutual benefits [225]. It is a key element in future wireless systems, supporting various applications like autonomous driving and indoor localization [44], [226]. The GDM can be utilized in ISAC systems for both data processing and generation. As a processing technique, it can classify and recover ISAC-related data. Moreover, it can generate synthetic ISAC data, a vital function for boosting the training efficiency of neural networks within the ISAC systems. Specifically, GDM has applications in various aspects of the ISAC system.

• ISAC Data Generation: The GDM can be used to generate samples for ISAC network training. For example, in indoor localization based on received signal strength indication (RSSI), the authors in [227] proposed a GAN for RSSI data augmentation. This network generates fake RSSI based on a small set of real collected labeled data. Using these data, the experimental results show that overall localization accuracy of the system has improved by 15.36%. Compared to GAN, GDM has stronger inference capabilities, which enable it to generate better fake data, thereby further enhancing system performance.   
• ISAC Data Processing: Apart from data generation, GenAI models are also commonly used to process ISAC data [228]. For instance, given that the GAN-based semisupervised learning can handle unlabeled and labeled data, the authors in [229] introduced a complement generator that uses a limited amount of unlabeled data to generate samples for training the discriminator. Building on this, they further adjust the number of probability outputs and utilize manifold regularization to stabilize the learning process, enhancing the human activity recognition performance in both semi-supervised and supervised scenarios.

# D. Movable Antenna System

The future of wireless communication networks is expected to be shaped significantly by the integration of movable antennas [230], [231]. Movable or fluid antennas, unlike conventional fixed-position antennas, have the capability of flexible movement and can be deployed at positions with more favorable channel conditions to achieve higher spatial diversity gains [232]. This flexibility enables better coverage and adaptability to changing environmental conditions. By strategically relocating the antenna, it becomes possible to mitigate signal blockage or interference caused by various obstacles, including buildings and vegetation. Therefore, the movable antennas can reap the full diversity in the given spatial region [232]. The complex and dynamic nature of wireless environments, characterized by high-dimensional configurations and non-linear relationships, necessitates sophisticated models like GDMs that can capture such high-dimensional and complex structures.

• Optimization of Antenna Positioning: GDMs can be used to optimize the positioning of movable antennas in real time. By modeling the wireless environment and the effects of different antenna positions, GDMs can generate optimal antenna positions that maximize signal strength and minimize interference.   
• Dynamic Resource Allocation: GDMs can be applied to the dynamic resource allocation problem in movable antennas. By modeling the resource demands and availability in the network, GDMs can generate optimal resource allocation strategies that balance the needs of different network users and maximize network efficiency [233].   
• Predictive Maintenance: Based on historical data, GDMs can be used to predict potential failures in movable antennas. By modeling antenna performance and failure patterns, GDMs can generate predictions about future failures, allowing for proactive maintenance and minimizing network downtime.   
• Integration with Reinforcement Learning: As demonstrated in Section III, the integration of GDMs with reinforcement learning techniques can be further explored in the context of movable antennas. This can lead to more robust and efficient resource slicing and scheduling strategies, enhancing the performance of 5G networks [234] and autonomous vehicles [235].

# IX. CONCLUSION

In this tutorial, the transformative potential of GDMs in intelligent network optimization has been thoroughly explored. The unique strengths of GDMs, including their broad applicability and capability to model complex data distributions, were studied. We highlighted their potential in enhancing the DRL algorithms and providing solutions in key intelligent network scenarios, such as incentive mechanism design, SemCom, IoV networks, channel estimation, error correction coding, and channel denoising. These explorations demonstrated the practicality and efficacy of GDMs in real-world applications. The tutorial concluded by emphasizing the research directions of GDMs in shaping the future of intelligent network optimization and encouraging further exploration in this promising field.

# ACKNOWLEDGMENT

Hongyang Du, Ruichen Zhang, Yinqiu Liu, Jiacheng Wang, and Dusit Niyato are with the College of Computing and Data Science, Nanyang Technological University, Singapore (e-mail: hongyang001@ e.ntu.edu.sg; ruichen.zhang@ntu.edu.sg; yinqiu001@e.ntu.edu.sg; jiacheng.wang@ntu.edu.sg; dniyato@ntu.edu.sg).

Yijing Lin is with the State Key Laboratory of Networking and Switching Technology, Beijing University of Posts and Telecommunications, Beijing 100876, China (e-mail: yjlin@bupt.edu.cn).

Zonghang Li is with the School of Information and Communication Engineering, University of Electronic Sciences and Technology of China, Chengdu 611731, China (e-mail: lizhuestc@gmail.com).

Jiawen Kang is with the School of Automation, Guangdong University of Technology, Guangzhou 510006, China (e-mail: kavinkang@gdut.edu.cn).

Zehui Xiong is with the Pillar of Information Systems Technology and Design, Singapore University of Technology and Design, Singapore (e-mail: zehui\_xiong@sutd.edu.sg).

Shuguang Cui is with the School of Science and Engineering, Future Network of Intelligence Institute, and the Guangdong Provincial Key Laboratory of Future Networks of Intelligence, The Chinese University of Hong Kong (Shenzhen), Shenzhen 518066, China (e-mail: shuguangcui@ cuhk.edu.cn).

Bo Ai is with the State Key Laboratory of Rail Traffic Control and Safety, Beijing Jiaotong University, Beijing 100044, China (e-mail: boai@bjtu.edu.cn).

Haibo Zhou is with the School of Electronic Science and Engineering, Nanjing University, Nanjing 210093, Jiangsu, China (e-mail: haibozhou@nju.edu.cn).

Dong In Kim is with the Department of Electrical and Computer Engineering, Sungkyunkwan University, Suwon 16419, South Korea (e-mail: dongin@skku.edu).

# REFERENCES

[1] M. Jovanovic and M. Campbell, “Generative artificial intelligence: Trends and prospects,” Computer, vol. 55, no. 10, pp. 107–112, Oct. 2022.   
[2] P. Korzynski et al., “Generative artificial intelligence as a new context for management theories: Analysis of ChatGPT,” Central Eur. Manag. J., vol. 31, no. 1, pp. 3–13, 2023.   
[3] R. Peres, M. Schreier, D. Schweidel, and A. Sorescu, “On ChatGPT and beyond: How generative artificial intelligence may affect research, teaching, and practice,” Int. J. Res. Mark., vol. 40, no. 2, pp. 269–275, 2023.   
[4] C. van Dun, L. Moder, W. Kratsch, and M. Röglinger, “ProcessGAN: Supporting the creation of business process improvement ideas through generative machine learning,” Decis. Support Syst., vol. 165, Feb. 2023, Art. no. 113880.   
[5] Accenture. “2023 technology vision report.” Accessed: May 1, 2024. [Online]. Available: https://www.accenture.com/usen/insights/technology/technology-trends-2023.   
[6] B. Ni, D. L. Kaplan, and M. J. Buehler, “Generative design of de novo proteins based on secondary-structure constraints using an attentionbased diffusion model,” Chem, vol. 9, no. 7, pp. 1828–1849, 2023.   
[7] R. Srinivasan and K. Uchino, “Biases in generative art: A causal look from the lens of art history,” in Proc. ACM Conf. Fair. Account. Transp., 2021, pp. 41–51.   
[8] A. Vaswani et al., “Attention is all you need,” in Proc. Adv. Neural Inf. Process. Syst., vol. 30, 2017, pp. 5998–6008.   
[9] O. AI, “GPT-4 technical report,” 2023, arXiv:2303.08774.   
[10] I. J. Goodfellow et al., “Generative adversarial networks,” Commun. ACM, vol. 63, no. 11, pp. 139–144, Nov. 2020.   
[11] D. P. Kingma et al., “An introduction to variational autoencoders,” Found. Trends Mach. Learn., vol. 12, no. 4, pp. 307–392, Apr. 2019.   
[12] D. Rezende and S. Mohamed, “Variational inference with normalizing flows,” in Proc. Int. Conf. Mach. Learn., Lille, France, Jul. 2015, pp. 1530–1538.   
[13] J. Zhao, M. Mathieu, and Y. LeCun, “Energy-based generative adversarial networks,” in Proc. Int. Conf. Mach. Learn., 2017, pp. 1–8.   
[14] J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli, ‘Deep unsupervised learning using nonequilibrium thermodynamics,” in Proc. Int. Conf. Mach. Learn., 2015, pp. 2256–2265.

[15] Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole, “Score-based generative modeling through stochastic differential equations,” in Proc. Int. Conf. Learn. Represent., 2021, p. 6.   
[16] S. Peng and S. Peng, Stochastic Differential Equations. Heidelberg, Germany: Springer, 2019.   
[17] H. Cao, C. Tan, Z. Gao, G. Chen, P.-A. Heng, and S. Z. Li. “A survey on generative diffusion model,” IEEE Trans. Knowl. Data Eng., early access, Feb. 2, 2014, doi: 10.1109/TKDE.2024.3361474.   
[18] “Stable diffusion.” Accessed: May 1, 2024. [Online]. Available: https://stability.ai/   
[19] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” in Proc. Adv. Neural Inf. Process. Syst., vol. 33, 2020, pp. 6840–6851.   
[20] J. Song, C. Meng, and S. Ermon, “Denoising diffusion implicit models,” in Proc. Int. Conf. Learn. Represent., 2020, p. 9.   
[21] X. Li, J. Thickstun, I. Gulrajani, P. S. Liang, and T. B. Hashimoto, “Diffusion-LM improves controllable text generation,” in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022, pp. 4328–4343.   
[22] G. Mittal, J. Engel, C. Hawthorne, and I. Simon, “Symbolic music generation with diffusion models,” in Proc. Int. Soc. Music Inf. Conf., 2021, pp. 468–475.   
[23] R. Huang, Z. Zhao, H. Liu, J. Liu, C. Cui, and Y. Ren, “PRODIFF: Progressive fast diffusion model for high-quality text-to-speech,” in Proc. ACM Int. Conf. Multimedia, 2022, pp. 2595–2605.   
[24] C. Niu, Y. Song, J. Song, S. Zhao, A. Grover, and S. Ermon, “Permutation invariant graph generation via score-based generative modeling,” in Proc. Int. Conf. Artif. Intell. Stat., 2020, pp. 4474–4484.   
[25] C. Vignac, I. Krawczuk, A. Siraudin, B. Wang, V. Cevher, and P. Frossard, “DiGress: Discrete denoising diffusion for graph generation,” in Proc. Int. Conf. Learn. Represent., 2022, p. 9.   
[26] X. Chen, J. He, X. Han, and L.-P. Liu, “Efficient and degree-guided graph generation via discrete diffusion modeling,” in Proc. Int. Conf. Mach. Learn., 2023, pp. 4585–4610.   
[27] X. Peng, J. Guan, Q. Liu, and J. Ma, “MolDiff: Addressing the atombond inconsistency problem in 3D molecule diffusion generation,” in Proc. Int. Conf. Mach. Learn., 2023, pp. 27611–27629.   
[28] M. A. Ketata et al., “DiffDock-PP: Rigid protein-protein docking with diffusion models,” in Proc. Int. Conf. Learn. Represent., 2023, p. 9.   
[29] L. Huang, H. Zhang, T. Xu, and K.-C. Wong, “MDM: Molecular diffusion model for 3D molecule generation,” in Proc. AAAI Conf. Artif. Intell., vol. 37, 2023, pp. 5105–5112.   
[30] C. Lee, J. Kim, and N. Park, “CoDi: Co-evolving contrastive diffusion models for mixed-type tabular synthesis,” in Proc. Int. Conf. Mach. Learn., 2023, pp. 18940–18956.   
[31] A. Kotelnikov, D. Baranchuk, I. Rubachev, and A. Babenko, “TabDDPM: Modelling tabular data with diffusion models,” in Proc. Int. Conf. Mach. Learn., 2023, pp. 17564–17579.   
[32] N. Neifar, A. Ben-Hamadou, A. Mdhaffar, and M. Jmaiel, “DiffECG: A generalized probabilistic diffusion model for ECG signals synthesis,” 2023, arXiv:2306.01875.   
[33] L. Yang et al., “Diffusion models: A comprehensive survey of methods and applications,” ACM Comput. Surveys, vol. 56, no. 4, pp. 1–39, 2023.   
[34] F.-A. Croitoru, V. Hondru, R. T. Ionescu, and M. Shah, “Diffusion models in vision: A survey,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 45, no. 9, pp. 10850–10869, Sep. 2023.   
[35] M. Reuss, M. Li, X. Jia, and R. Lioutikov. “Goal-conditioned imitation learning using score-based diffusion policies,” 2023. [Online]. Available: https://intuitive-robots.github.io/beso-website/   
[36] Y. Li, Y. Lu, R. Zhang, B. Ai, and Z. Zhong, “Deep learning for energy efficient beamforming in MU-MISO networks: A GATbased approach,” IEEE Wireless Commun. Lett., vol. 12, no. 7, pp. 1264–1268, Jul. 2023.   
[37] C. Lu, H. Chen, J. Chen, H. Su, C. Li, and J. Zhu, “Contrastive energy prediction for exact energy-guided diffusion sampling in offline reinforcement learning,” in Proc. Int. Conf. Mach. Learn., 2023, p. 9.   
[38] S. Krishnamoorthy, S. M. Mashkaria, and A. Grover, “Diffusion models for black-box optimization,” in Proc. Int. Conf. Mach. Learn., 2023, pp. 17842–17857.   
[39] Y. Liu, C. Du, T. Pang, C. Li, W. Chen, and M. Lin, “Graph diffusion policy optimization,” 2024, arXiv:2402.16302.   
[40] H. Du et al., “The age of generative AI and AI-generated everything,” 2023, arXiv:2311.00947.   
[41] H. Du, J. Wang, D. Niyato, J. Kang, Z. Xiong, and D. I. Kim, “AI-generated incentive mechanism and full-duplex semantic communications for information sharing,” IEEE J. Sel. Areas Commun., vol. 41, no. 9, pp. 2981–2997, Sep. 2023.

[42] B. Du et al., “YOLO-based semantic communication with generative AI-aided resource allocation for digital twins construction,” IEEE Internet Things J., vol. 11, no. 5, pp. 7664–7678, Mar. 2024.   
[43] H. Du et al., “User-centric interactive AI for distributed diffusion model-based AI-generated content,” 2023, arXiv:2311.11094.   
[44] X. Cheng, D. Duan, S. Gao, and L. Yang, “Integrated sensing and communications (ISAC) for vehicular communication networks (VCN),” IEEE Internet Things J., vol. 9, no. 23, pp. 23441–23451, Dec. 2022.   
[45] J. Wang et al., “Generative AI for integrated sensing and communication: Insights from the physical layer perspective,” 2023, arXiv:2310.01036.   
[46] W. Yang et al., “Semantic communications for future Internet: Fundamentals, applications, and challenges,” IEEE Commun. Surveys Tuts., vol. 25, no. 1, pp. 213–250, 1st Quart., 2023.   
[47] H. Du et al., “Generative AI-aided joint training-free secure semantic communications via multi-modal prompts,” in Proc. IEEE Int. Conf. Acoust. Speech Signal Process., 2023, pp. 1–8.   
[48] L.-M. Ang, K. P. Seng, G. K. Ijemaru, and A. M. Zungeru, “Deployment of IoV for smart cities: Applications, architecture, and challenges,” IEEE Access, vol. 7, pp. 6473–6492, 2018.   
[49] H. Zhou, H. Zhou, J. Li, K. Yang, J. An, and X. Shen, “Heterogeneous ultra-dense networks with traffic hotspots: A unified handover analysis,” IEEE Internet Things J., vol. 10, no. 10, pp. 8825–8838, May 2023.   
[50] Y. Lin et al., “A unified framework for integrating semantic communication and AI-generated content in metaverse,” 2023, arXiv:2305.2023.   
[51] H. Zhou et al., “ChainCluster: Engineering a cooperative content distribution framework for highway vehicular communications,” IEEE Trans. Intell. Transp Syst., vol. 15, no. 6, pp. 2644–2657, Jun. 2014.   
[52] R. Zhang, K. Xiong, X. Tian, Y. Lu, P. Fan, and K. B. Letaief, “Inverse reinforcement learning meets power allocation in multi-user cellular networks,” in Proc. IEEE Conf. Comput. Commun. Workshops (INFOCOM WKSHPS), 2022, pp. 1–2.   
[53] H. Du et al., “Spear or shield: Leveraging generative AI to tackle security threats of intelligent network services,” 2023, arXiv:2306.02384.   
[54] A. Ajay, Y. Du, A. Gupta, J. Tenenbaum, T. Jaakkola, and P. Agrawal, “Is conditional generative modeling all you need for decision-making?” in Proc. Int. Conf. Learn. Represent., May 2023, p. 6.   
[55] M. Janner, Y. Du, J. B. Tenenbaum, and S. Levine, “Planning with diffusion for flexible behavior synthesis,” in Proc. Int. Conf. Mach. Learn., Jul. 2023, pp. 9902–9915.   
[56] Z. Wang, J. J. Hunt, and M. Zhou, “Diffusion policies as an expressive policy class for offline reinforcement learning,” in Proc. Int. Conf. Learn. Represent., May 2023, p. 8.   
[57] H. Chen, C. Lu, C. Ying, H. Su, and J. Zhu, “Offline reinforcement learning via high-fidelity generative Behavior modeling,” in Proc. Int. Conf. Learn. Represent., May 2023, p. 6.   
[58] H.-C. Wang, S.-F. Chen, and S.-H. Sun, “Diffusion model-augmented behavioral cloning,” in Proc. Int. Conf. Mach. Learn. Workshop, 2023, p. 5.   
[59] A. Kazerouni et al., “Diffusion models for medical image analysis: A comprehensive survey,” 2022, arXiv:2211.07804.   
[60] C. Zhang, C. Zhang, M. Zhang, and I. S. Kweon, “Text-to-image diffusion model in generative AI: A survey,” 2023, arXiv:2303.07909.   
[61] A. Ulhaq, N. Akhtar, and G. Pogrebna, “Efficient diffusion models for vision: A survey,” 2022, arXiv:2210.09292.   
[62] H. Zou, Z. M. Kim, and D. Kang, “Diffusion models in NLP: A survey,” 2023, arXiv:2305.14671.   
[63] Y. Li, K. Zhou, W. X. Zhao, and J.-R. Wen, “Diffusion models for non-autoregressive text generation: A survey,” in Proc. Int. Joint Conf. Artif. Intell., 2023, pp. 6692–6701.   
[64] L. Lin, Z. Li, R. Li, X. Li, and J. Gao, “Diffusion models for time series applications: A survey,” Front. Inf. Technol. Electron. Eng., vol. 25, pp. 1–23, Dec. 2023.   
[65] W. Luo, “A comprehensive survey on knowledge distillation of diffusion models,” 2023, arXiv:2304.04262.   
[66] M. Zhang et al., “A survey on graph diffusion models: Generative AI in science for molecule, protein and material,” 2023, arXiv:2304.01565.   
[67] C. Zhang et al., “Audio diffusion model for speech synthesis: A survey on text to speech and speech enhancement in generative AI,” 2023, arXiv:2303.13336.   
[68] Z. Guo et al., “Diffusion models in bioinformatics: A new wave of deep learning revolution in action,” 2023, arXiv:2302.10907.   
[69] W. Fan et al., “Generative diffusion models on graphs: Methods and applications,” 2023, arXiv:2302.02591.

[70] H. Du et al., “Diffusion-based reinforcement learning for edge-enabled AI-generated content services,” IEEE Trans. Mobile Comput., early access, Jan. 19, 2014, doi: 10.1109/TMC.2024.3356178.   
[71] A. Lou and S. Ermon, “Reflected diffusion models,” in Proc. Int. Conf. Mach. Learn., 2023, p. 4.   
[72] Q. Zhang, J. Song, X. Huang, Y. Chen, and M.-Y. Liu, “DiffCollage: Parallel generation of large content with diffusion models,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2023, pp. 10188–10198.   
[73] H. Ni, C. Shi, K. Li, S. X. Huang, and M. R. Min, “Conditional image-to-video generation with latent flow diffusion models,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2023, pp. 18444–18455.   
[74] W. Enkelmann, “Investigations of multigrid algorithms for the estimation of optical flow fields in image sequences,” Comput. Vis. Graph. Image Process., vol. 43, no. 2, pp. 150–177, Feb. 1988.   
[75] J. Ho, T. Salimans, A. Gritsenko, W. Chan, M. Norouzi, and D. J. Fleet, “Video diffusion models,” 2022, arXiv:2204.03458.   
[76] P. Yu et al., “Latent diffusion energy-based model for interpretable text modeling,” in Proc. Int. Conf. Mach. Learn., 2022, p. 6.   
[77] S. Gong, M. Li, J. Feng, Z. Wu, and L. Kong, “DiffuSeq: Sequence to sequence text generation with diffusion models,” in Proc. Int. Conf. Learn. Represent., 2022, p. 9.   
[78] H. Zhang, X. Liu, and J. Zhang, “DiffuSum: Generation enhanced extractive summarization with diffusion,” in Proc. Assoc. Comput. Linguist., 2023, pp. 13089–13100.   
[79] M. Reid, V. J. Hellendoorn, and G. Neubig, “Diffuser: Diffusion via edit-based reconstruction,” in Proc. Int. Conf. Learn. Represent., 2023, pp. 1–6.   
[80] L. Ruan et al., “MM-Diffusion: Learning multi-modal diffusion models for joint audio and video generation,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2023, pp. 10219–10228.   
[81] Z. Kong, W. Ping, J. Huang, K. Zhao, and B. Catanzaro, “DiffWave: A versatile diffusion model for audio synthesis,” in Proc. Int. Conf. Learn. Represent., 2021, p. 2.   
[82] J. Liu, C. Li, Y. Ren, F. Chen, and Z. Zhao, “DiffSinger: Singing voice synthesis via shallow diffusion mechanism,” in Proc. AAAI Conf. Artif. Intell., vol. 36, 2022, pp. 11020–11028.   
[83] S. Rouard and G. Hadjeres, “CRASH: Raw audio score-based generative modeling for controllable high-resolution drum sound synthesis,” in Proc. Int. Soc. Music Inf. Conf., 2021, pp. 579–585.   
[84] L. L. Ankile, A. Midgley, and S. Weisshaar, “Denoising diffusion probabilistic models as a defense against adversarial attacks,” 2023, arXiv:2301.06871.   
[85] S. Ghalebikesabi et al., “Differentially private diffusion models generate useful synthetic images,” 2023, arXiv:2302.13861.   
[86] A. M. Maung and H. Kiya, “Generative model-based attack on learnable image encryption for privacy-preserving deep learning,” 2023, arXiv:2303.05036.   
[87] Z. Blasingame and C. Liu, “Diffusion models for stronger face morphing attacks,” 2023, arXiv:2301.04218.   
[88] A. Q. Nichol et al., “GLIDE: Towards photorealistic image generation and editing with text-guided diffusion models,” in Proc. Int. Conf. Mach. Learn., 2022, pp. 16784–16804.   
[89] OpenAI. “DALL·E 2.” Accessed: May 1, 2024. [Online]. Available: https://openai.com/dall-e-2   
[90] Google Research. “Imagen.” Accessed: May 1, 2024. [Online]. Available: https://imagen.research.google/   
[91] J. Gui, Z. Sun, Y. Wen, D. Tao, and J. Ye, “A review on generative adversarial networks: Algorithms, theory, and applications,” IEEE Trans. Knowl. Data Eng., vol. 35, no. 4, pp. 3313–3332, Apr. 2021.   
[92] H. Du et al., “Exploring collaborative distributed diffusion-based AIgenerated content (AIGC) in wireless networks,” IEEE Netw., early access, Jul. 3, 2023, doi: 10.1109/MNET.006.2300223.   
[93] Z. Li et al., “Diffusion model for data-driven black-box optimization,” 2024, arXiv:2403.13219.   
[94] Z. Sun and Y. Yang, “DifusCo: Graph-based diffusion solvers for combinatorial optimization,” in Proc. Adv. Neural Inf. Process. Syst., vol. 36, 2024, pp. 1–9.   
[95] B. Zhang, W. Luo, and Z. Zhang, “Enhancing adversarial robustness via score-based optimization,” in Proc. Adv. Neural Inf. Process. Syst., vol. 36, 2024, pp. 1–8.   
[96] G. Giannone, A. Srivastava, O. Winther, and F. Ahmed, “Aligning optimization trajectories with diffusion models for constrained design generation,” in Proc. Adv. Neural Inf. Process. Syst., vol. 36, 2024, pp. 1–8.

[97] S. Luo, Y. Su, X. Peng, S. Wang, J. Peng, and J. Ma, “Antigen-specific antibody design and optimization with diffusion-based generative models for protein structures,” in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022, pp. 9754–9767.   
[98] H. Chen, C. Lu, Z. Wang, H. Su, and J. Zhu, “Score regularized policy optimization through diffusion behavior,” in Proc. Int. Conf. Learn. Represent., 2024, pp. 1–8.   
[99] S. Zhou et al., “Adaptive online replanning with diffusion models,” in Proc. Adv. Neural Inf. Process. Syst., vol. 36, 2024, pp. 1–19.   
[100] K. Xu, S. Lu, B. Huang, W. Wu, and Q. Liu, “Stage-by-stage wavelet optimization refinement diffusion model for sparse-view CT reconstruction,” IEEE Trans. Med. Imag., early access, Jan. 18, 2024, doi: 10.1109/TMI.2024.3355455.   
[101] W. Wu and Y. Wang, “Data-iterative optimization score model for stable ultra-sparse-view CT reconstruction,” 2023, arXiv:2308.14437.   
[102] Z. Jiang, Z. Zhou, L. Li, W. Chai, C.-Y. Yang, and J.-N. Hwang, “Back to optimization: Diffusion-based zero-shot 3D human pose estimation,” in Proc. IEEE/CVF Winter Conf. Appl. Comput. Vis., 2024, pp. 6142–6152.   
[103] S. Huang et al., “Diffusion-based generation, optimization, and planning in 3D scenes,” in Proc. IEEE/CVF Comput. Vis. Pattern Recognit., 2023, pp. 16750–16761.   
[104] Y. Huang, J. Wang, Y. Shi, X. Qi, Z.-J. Zha, and L. Zhang, “DreamTime: An improved optimization strategy for text-to-3D content creation,” 2023, arXiv:2306.12422.   
[105] J. Urain, N. Funk, J. Peters, and G. Chalvatzaki, “SE(3)- DiffusionFields: Learning smooth cost functions for joint grasp and motion optimization through diffusion,” in Proc. IEEE Int. Conf. Robot. Autom., 2023, pp. 5923–5930.   
[106] F. Mazé and F. Ahmed, “Diffusion models beat GANs on topology optimization,” in Proc. AAAI Conf. Artif. Intell., vol. 37, 2023, pp. 9108–9116.   
[107] S. W. Park, K. Lee, and J. Kwon, “Neural Markov controlled SDE: Stochastic optimization for continuous-time data,” in Proc. Int. Conf. Learn. Represent., 2021, p. 45.   
[108] J. Liu, M. Stamatopoulou, and D. Kanoulas, “DiPPeR: Diffusion-based 2D path planner applied on legged robots,” 2023, arXiv:2310.07842.   
[109] A. Zappone, M. Di Renzo, M. Debbah, T. T. Lam, and X. Qian, “Model-aided wireless artificial intelligence: Embedding expert knowledge in deep neural networks for wireless system optimization,” IEEE Veh. Technol. Mag., vol. 14, no. 3, pp. 60–69, Mar. 2019.   
[110] X. Lin, N. B. Shroff, and R. Srikant, “A tutorial on cross-layer optimization in wireless networks,” IEEE J. Sel. Areas Commun., vol. 24, no. 8, pp. 1452–1463, Aug. 2006.   
[111] Y. Liu et al., “Deep generative model and its applications in efficient wireless network management: A tutorial and case study,” IEEE Wireless Commun., early access, Apr. 30, 2024, doi: 10.1109/MWC.009.2300165.   
[112] I. Osband, C. Blundell, A. Pritzel, and B. Van Roy, “Deep exploration via bootstrapped DQN,” in Proc. Adv. Neural Inf. Process. Syst., vol. 29, 2016, pp. 1–7.   
[113] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft actor–critic: Offpolicy maximum entropy deep reinforcement learning with a stochastic actor,” in Proc. Int. Conf. Mach. Learn., 2018, pp. 1861–1870.   
[114] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” 2017, arXiv:1707.06347.   
[115] A. Goldsmith, Wireless Communications. Cambridge, U.K.: Cambridge Univ. Press, 2005.   
[116] B. Zheng and R. Zhang, “Intelligent reflecting surface-enhanced OFDM: Channel estimation and reflection optimization,” IEEE Wireless Commun. Lett., vol. 9, no. 4, pp. 518–522, Apr. 2019.   
[117] S. Desale, A. Rasool, S. Andhale, and P. Rane, “Heuristic and metaheuristic algorithms and their relevance to the real world: A survey,” Int. J. Comput. Eng. Res. Trends, vol. 351, no. 5, pp. 2349–7084, May 2015.   
[118] W. Yu, W. Rhee, S. Boyd, and J. M. Cioffi, “Iterative water-filling for Gaussian vector multiple-access channels,” IEEE Trans. Inf. Theory, vol. 50, no. 1, pp. 145–152, Jan. 2004.   
[119] A. Feriani and E. Hossain, “Single and multi-agent deep reinforcement learning for AI-enabled wireless networks: A tutorial,” IEEE Commun. Surveys Tuts., vol. 23, no. 2, pp. 1226–1252, 1st Quart., 2021.   
[120] Y. Yu, T. Wang, and S. C. Liew, “Deep-reinforcement learning multiple access for heterogeneous wireless networks,” IEEE J. Sel. Areas Commun., vol. 37, no. 6, pp. 1277–1290, Jun. 2019.   
[121] H. Du et al., “Enabling AI-generated content services in wireless edge networks,” IEEE Wireless Commun., early access, Feb. 26, 2024, doi: 10.1109/MWC.004.2300015.

[122] H. Zhou, Y. Wu, Y. Hu, and G. Xie, “A novel stable selection and reliable transmission protocol for clustered heterogeneous wireless sensor networks,” Comput. Commun., vol. 33, no. 15, pp. 1843–1849, 2010.   
[123] W.-K. Ching and M. K. Ng. “Markov chains.” 2006. [Online]. Available: https://www.geeksforgeeks.org/markov-chain/   
[124] X. Xu et al., “Service offloading with deep Q-network for digital twinning-empowered Internet of Vehicles in edge computing,” IEEE Trans. Ind. Inform at., vol. 18, no. 2, pp. 1414–1423, Feb. 2020.   
[125] M. Ohira, K. Takano, and Z. Ma, “A novel deep-Q-network-based fine-tuning approach for planar bandpass filter design,” IEEE Microw. Wireless Compon. Lett., vol. 31, no. 6, pp. 638–641, Jun. 2021.   
[126] A. Iqbal, M.-L. Tham, and Y. C. Chang, “Double deep Q-networkbased energy-efficient resource allocation in cloud radio access network,” IEEE Access, vol. 9, pp. 20440–20449, 2021.   
[127] H. Hasselt, “Double Q-learning,” in Proc. Adv. Neural Inf. Process. Syst., vol. 23, 2010, pp. 1–9.   
[128] S. Vimal, M. Khari, R. G. Crespo, L. Kalaivani, N. Dey, and M. Kaliappan, “Energy enhancement using multiobjective ant colony optimization with double Q learning algorithm for IoT based cognitive radio networks,” Comput. Commun., vol. 154, pp. 481–490, Mar. 2020.   
[129] N. C. Luong et al., “Applications of deep reinforcement learning in communications and networking: A survey,” IEEE Commun. Surveys Tuts., vol. 21, no. 4, pp. 3133–3174, 4th Quart., 2019.   
[130] Y. Xu, W. Xu, Z. Wang, J. Lin, and S. Cui, “Load balancing for ultradense networks: A deep reinforcement learning-based approach,” IEEE Internet Things J., vol. 6, no. 6, pp. 9399–9412, Jun. 2019.   
[131] E. Zhang, Y. Lu, W. Wang, and A. Zhang, “LAD: Language augmented diffusion for reinforcement learning,” in Proc. Adv. Neural Inf. Process. Syst. Workshop, 2022, pp. 1–9.   
[132] H. Wang, Y. Wu, S. Guo, and L. Wang, “PDPP: Projected diffusion for procedure planning in instructional videos,” in Proc. Comput. Vis. Pattern Recognit., 2023, pp. 14836–14845.   
[133] J. Brehmer, J. Bose, P. De Haan, and T. Cohen, “EDGI: Equivariant diffusion for planning with embodied agents,” in Proc. Adv. Neural Inf. Process. Syst., vol. 36, 2024, pp. 1–8.   
[134] Y. Cao, E. Rizk, S. Vlaski, and A. H. Sayed, “Multi-agent adversarial training using diffusion learning,” in Proc. IEEE Int. Conf. Acoust. Speech Signal Process. (ICASSP), 2023, pp. 1–5.   
[135] Z. Liang, Y. Mu, M. Ding, F. Ni, M. Tomizuka, and P. Luo, “AdaptDiffuser: Diffusion models as adaptive self-evolving planners,” in Proc. Int. Conf. Mach. Learn., 2023, pp. 20725–20745.   
[136] T. Pearce et al., “Imitating human behaviour with diffusion models,” in Proc. Int. Conf. Learn. Represent., 2023, pp. 1–8.   
[137] R. Zhang, K. Xiong, W. Guo, X. Yang, P. Fan, and K. B. Letaief, “Qlearning-based adaptive power control in wireless RF energy harvesting heterogeneous networks,” IEEE Syst. J., vol. 15, no. 2, pp. 1861–1872, Jun. 2021.   
[138] X. Tian, K. Xiong, R. Zhang, P. Fan, D. Niyato, and K. B. Letaief, “Sum rate maximization in multi-cell multi-user networks: An inverse reinforcement learning-based approach,” IEEE Wireless Commun. Lett., vol. 13, no. 1, pp. 4–8, Jan. 2024.   
[139] R. Zhang, K. Xiong, Y. Lu, B. Gao, P. Fan, and K. B. Letaief, “Joint coordinated beamforming and power splitting ratio optimization in MU-MISO SWIPT-enabled HetNets: A multi-agent DDQN-based approach,” IEEE J. Sel. Areas Commun., vol. 40, no. 2, pp. 677–693, Feb. 2022.   
[140] V. Mnih et al., “Human-level control through deep reinforcement learning,” Nature, vol. 518, no. 7540, pp. 529–533, 2015.   
[141] T. Schaul, J. Quan, I. Antonoglou, and D. Silver, “Prioritized experience replay,” 20115, arXiv:1511.05952.   
[142] M. Hausknecht and P. Stone, “Deep recurrent Q-learning for partially observable MDPs,” in Proc. AAAI Fall Symp., 2015, pp. 1–8.   
[143] R. Zhang, K. Xiong, Y. Lu, P. Fan, D. W. K. Ng, and K. B. Letaief, “Energy efficiency maximization in RIS-assisted SWIPT networks with RSMA: A PPO-based approach,” IEEE J. Sel. Areas Commun., vol. 41, no. 5, pp. 1413–1430, May 2023.   
[144] R. J. Williams, “Simple statistical gradient-following algorithms for connectionist reinforcement learning,” Reinforcement Learn., vol. 8, pp. 5–32, May 1992.   
[145] M. Hessel et al., “Rainbow: Combining improvements in deep reinforcement learning,” in Proc. AAAI Conf. Artif. Intell., vol. 32, 2018, pp. 3215–3222.   
[146] C. Wang, L. Liu, C. Jiang, S. Wang, P. Zhang, and S. Shen, “Incorporating distributed DRL into storage resource optimization of space-air-ground integrated wireless communication network,” IEEE J. Sel. Topics Signal Process., vol. 16, no. 3, pp. 434–446, Mar. 2021.

[147] Y. Li, X. Hu, Y. Zhuang, Z. Gao, P. Zhang, and N. El-Sheimy, “Deep reinforcement learning (DRL): Another perspective for unsupervised wireless localization,” IEEE Internet Things J., vol. 7, no. 7, pp. 6279–6287, Jul. 2019.   
[148] J. Tang, A. Mihailovic, and H. Aghvami, “Constructing a DRL decision making scheme for multi-path routing in all-IP access network,” in Proc. IEEE Global Commun. Conf., 2022, pp. 3623–3628.   
[149] Y. Zhang, Y. Lu, R. Zhang, B. Ai, and D. Niyato, “Deep reinforcement learning for secrecy energy efficiency maximization in RIS-assisted networks,” IEEE Trans. Veh. Technol., vol. 72, no. 9, pp. 12413–12418, Sep. 2023.   
[150] N. M. Ashraf, R. R. Mostafa, R. H. Sakr, and M. Rashad, “Optimizing hyperparameters of deep reinforcement learning for autonomous driving based on whale optimization algorithm,” PLoS ONE, vol. 16, no. 6, 2021, Art. no. e0252754.   
[151] J. Fu, A. Kumar, O. Nachum, G. Tucker, and S. Levine, “D4RL: Datasets for deep data-driven reinforcement learning,” 2020, arXiv:2004.07219.   
[152] F. Vargas, T. Reu, and A. Kerekes, “Expressiveness remarks for denoising diffusion models and samplers,” 2023, arXiv: 2305.09605.   
[153] R. Liu et al., “Balanced traffic routing: Design, implementation, and evaluation,” Ad Hoc Netw., vol. 37, pp. 14–28, Feb. 2016.   
[154] D. Watson, W. Chan, J. Ho, and M. Norouzi, “Learning fast samplers for diffusion models by differentiating through sample quality,” in Proc. Int. Conf. Learn. Represent., 2021, pp. 1–8.   
[155] S. Hong, G. Lee, W. Jang, and S. Kim, “Improving sample quality of diffusion models using self-attention guidance,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jun. 2023, pp. 7462–7471.   
[156] Z. Lyu, X. Xu, C. Yang, D. Lin, and B. Dai, “Accelerating diffusion models via early stop of the diffusion process,” 2022, arXiv:2205.12524.   
[157] M. Dai, L. Luo, J. Ren, H. Yu, and G. Sun, “PSACCF: Prioritized online slice admission control considering fairness in 5G/B5G networks,” IEEE Trans. Netw. Sci. Eng., vol. 9, no. 6, pp. 4101–4114, Jun. 2022.   
[158] S. Gu, E. Holly, T. Lillicrap, and S. Levine, “Deep reinforcement learning for robotic manipulation with asynchronous off-policy updates,” in Proc. IEEE Int. Conf. Robot. Autom., 2017, pp. 3389–3396.   
[159] N. Khaneja, T. Reiss, C. Kehlet, T. Schulte-Herbrüggen, and S. J. Glaser, “Optimal control of coupled spin dynamics: Design of NMR pulse sequences by gradient ascent algorithms,” J. Magn. Reson., vol. 172, no. 2, pp. 296–305, Feb. 2005.   
[160] S. Zhao, M. Gong, T. Liu, H. Fu, and D. Tao, “Domain generalization via entropy regularization,” in Proc. Adv. Neural Inf. Process. Syst., vol. 33, 2020, pp. 16096–16107.   
[161] G. Tesauro et al., “Temporal difference learning and TD-Gammon,” Commun. ACM, vol. 38, no. 3, pp. 58–68, 1995.   
[162] K. Cobbe, C. Hesse, J. Hilton, and J. Schulman, “Leveraging procedural generation to benchmark reinforcement learning,” in Proc. Int. Conf. Mach. Learn., vol. 119, Jul. 2020, pp. 2048–2056.   
[163] A. Raffin. “RL baselines zoo.” 2018. [Online]. Available: https://github.com/araffin/rl-baselines-zoo   
[164] Y. Liu et al., “Blockchain-empowered lifecycle management for AIgenerated content products in edge networks,” IEEE Wireless Commun., early access, Feb. 5, 2024, doi: 10.1109/MWC.003.2300053.   
[165] E. Aubry, T. Silverston, A. Lahmadi, and O. Festor, “CrowdOut: A mobile crowdsourcing service for road safety in digital cities,” in Proc. IEEE Int. Conf. Pervasive Comput. Commun. Workshops (PERCOM WORKSHOPS), 2014, pp. 86–91.   
[166] Y. Liu, K. Wang, Y. Lin, and W. Xu, “LightChain: A lightweight blockchain system for Industrial Internet of Things,” IEEE Trans. Ind. Informat., vol. 15, no. 6, pp. 3571–3581, Jun. 2019.   
[167] R. Zeng, C. Zeng, X. Wang, B. Li, and X. Chu, “A comprehensive survey of incentive mechanism for federated learning,” 2021, arXiv:2106.15406.   
[168] D. Yang, G. Xue, J. Zhang, A. Richa, and X. Fang, “Coping with a smart jammer in wireless networks: A Stackelberg game approach,” IEEE Trans. Wireless Commun., vol. 12, no. 8, pp. 4038–4047, Aug. 2013.   
[169] X. Chen, Y. Deng, G. Zhu, D. Wang, and Y. Fang, “From resource auction to service auction: An auction paradigm shift in wireless networks,” IEEE Wireless Commun., vol. 29, no. 2, pp. 185–191, Apr. 2022.   
[170] J. Kang, Z. Xiong, D. Niyato, D. Ye, D. I. Kim, and J. Zhao, “Toward secure blockchain-enabled Internet of Vehicles: Optimizing consensus management using reputation and contract theory,” IEEE Trans. Veh. Technol., vol. 68, no. 3, pp. 2906–2920, Mar. 2019.

[171] A. Kumar. “Model complexity.” Accessed: May 1, 2024. [Online]. Available: https://vitalflux.com/model-complexity-overfitting-inmachine-learning/   
[172] Microsoft. “The relationshio between model size and performance.” Accessed: May 1, 2024. [Online]. Available: https://learn.microsoft. com/en-us/semantic-kernel/prompt-engineering/llm-models   
[173] Y. Lin et al., “A unified blockchain-semantic framework for wireless edge intelligence enabled Web 3.0,” IEEE Wireless Commun., vol. 31, no. 2, pp. 126–133, Apr. 2024.   
[174] H. Du et al., “Semantic communications for wireless sensing: RISaided encoding and self-supervised decoding,” IEEE J. Sel. Areas Commun., vol. 41, no. 8, pp. 2547–2562, Aug. 2023.   
[175] C. Liang et al., “Generative AI-driven semantic communication networks: Architecture, technologies and applications,” 2023, arXiv:2401.00124.   
[176] H. Du et al., “Rethinking wireless communication security in semantic Internet of Things,” IEEE Wireless Commun. Mag., vol. 30, no. 3, pp. 36–43, Jun. 2023.   
[177] J. Kang et al., “Personalized saliency in task-oriented semantic communications: Image transmission and performance analysis,” IEEE J. Sel. Areas Commun., vol. 41, no. 1, pp. 186–201, Jan. 2022.   
[178] N. Van Huynh et al., “Generative AI for physical layer communications: A survey,” IEEE Trans. Cogn. Commun. Netw., early access, Apr. 3, 2024, doi: 10.1109/tccn.2024.3384500   
[179] Y. Lin et al., “A blockchain-based semantic exchange framework for Web 3.0 toward participatory economy,” IEEE Commun. Mag., vol. 61, no. 8, pp. 94–100, Aug. 2023.   
[180] Y. Lin et al., “Blockchain-aided secure semantic communication for AI-generated content in metaverse,” IEEE Open J. Comput. Soc., vol. 4, pp. 72–83, 2023.   
[181] H. Zhang, S. Shao, M. Tao, X. Bi, and K. B. Letaief, “Deep learning-enabled semantic communication systems with task-unaware transmitter and dynamic data,” IEEE J. Sel. Areas Commun., vol. 41, no. 1, pp. 170–185, Jan. 2023.   
[182] A. A. Alemi, I. Fischer, J. V. Dillon, and K. Murphy, “Deep variational information bottleneck,” in Proc. Int. Conf. Learn. Represent., 2016, pp. 1–8.   
[183] J. Wang et al., “A unified framework for guiding generative AI with wireless perception in resource constrained mobile edge networks,” IEEE Trans. Mobile Comput., early access, Mar. 14, 2024, doi: 10.1109/TMC.2024.3377226.   
[184] H. Du et al., “Attention-aware resource allocation and QoE analysis for metaverse xURLLC services,” IEEE J. Sel. Areas Commun., vol. 41, no. 7, pp. 2158–2175, Jul. 2023.   
[185] Y. Liu, H. Yu, S. Xie, and Y. Zhang, “Deep reinforcement learning for offloading and resource allocation in vehicle edge computing and networks,” IEEE Trans. Veh. Technol., vol. 68, no. 11, pp. 11158–11168, Nov. 2019.   
[186] L. Yan, Z. Qin, R. Zhang, Y. Li, and G. Y. Li, “QoE-aware resource allocation for semantic communication networks,” in Proc. IEEE Global Commun. Conf., 2022, pp. 3272–3277.   
[187] H. Zhou, W. Xu, J. Chen, and W. Wang, “Evolutionary V2X technologies toward the Internet of Vehicles: Challenges and opportunities,” Proc. IEEE, vol. 108, no. 2, pp. 308–323, Feb. 2020.   
[188] R. Zhang et al., “Generative AI-enabled vehicular networks: Fundamentals, framework, and case study,” 2023, arXiv:2304.11098.   
[189] W. Duan, J. Gu, M. Wen, G. Zhang, Y. Ji, and S. Mumtaz, “Emerging technologies for 5G-IoV networks: Applications, trends and opportunities,” IEEE Netw., vol. 34, no. 5, pp. 283–289, Sep./Oct. 2020.   
[190] L. Liang, G. Y. Li, and W. Xu, “Resource allocation for D2D-enabled vehicular communications,” IEEE Trans. Commun., vol. 65, no. 7, pp. 3186–3197, Jul. 2017.   
[191] L. Liang, H. Ye, and G. Y. Li, “Spectrum sharing in vehicular networks based on multi-agent reinforcement learning,” IEEE J. Sel. Areas Commun., vol. 37, no. 10, pp. 2282–2292, Oct. 2019.   
[192] K. Dovelos, M. Matthaiou, H. Q. Ngo, and B. Bellalta, “Channel estimation and hybrid combining for wideband terahertz massive MIMO systems,” IEEE J. Sel. Areas Commun., vol. 39, no. 6, pp. 1604–1620, Jun. 2021.   
[193] Y. Liu, Z. Tan, H. Hu, L. J. Cimini, and G. Y. Li, “Channel estimation for OFDM,” IEEE Commun. Surveys Tuts., vol. 16, no. 4, pp. 1891–1908, 4th Quart., 2014.   
[194] S. J. Nawaz, K. I. Ahmed, M. N. Patwary, and N. M. Khan, “Superimposed training-based compressed sensing of sparse multipath channels,” IET Commun., vol. 6, no. 18, pp. 3150–3156, 2012.

[195] Y. Liao, Y. Hua, X. Dai, H. Yao, and X. Yang, “ChanEstNet: A deep learning based channel estimation for high-speed scenarios,” in Proc. IEEE Int. Conf. Commun. (ICC), 2019, pp. 1–6.   
[196] M. Arvinte and J. I. Tamir, “MIMO channel estimation using scorebased generative models,” IEEE Trans. Wireless Commun., vol. 22, no. 6, pp. 3698–3713, Jun. 2023.   
[197] Y. Song and S. Ermon, “Improved techniques for training score-based generative models,” in Proc. Adv. Neural Inf. Process. Syst., vol. 33, 2020, pp. 12438–12448.   
[198] G. Lin, A. Milan, C. Shen, and I. Reid, “RefineNet: Multi-path refinement networks for high-resolution semantic segmentation,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2017, pp. 1925–1934.   
[199] E. Balevi, A. Doshi, A. Jalal, A. Dimakis, and J. G. Andrews, “High dimensional channel estimation using deep generative networks,” IEEE J. Sel. Areas Commun., vol. 39, no. 1, pp. 18–30, Jan. 2021.   
[200] P. Schniter and A. Sayeed, “Channel estimation and precoder design for millimeter-wave communications: The sparse way,” in Proc. IEEE 48th Asilomar Conf. Signals Syst. Comput., 2014, pp. 273–277.   
[201] A. Jalal, M. Arvinte, G. Daras, E. Price, A. G. Dimakis, and J. Tamir, “Robust compressed sensing mri with deep generative priors,” in Proc. Adv. Neural Inf. Process. Syst., vol. 34, 2021, pp. 14938–14954.   
[202] E. Biglieri, Coding for Wireless Channels. New York, NY, USA: Springer, 2005.   
[203] Y. Choukroun and L. Wolf, “Error correction code transformer,” in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022, pp. 38695–38705.   
[204] Y. Choukroun and L. Wolf, “Denoising diffusion error correction codes,” in Proc. Int. Conf. Mach. Learn., Jul. 2023, p. 9.   
[205] Q. Bao, Z. Hui, R. Zhu, P. Ren, X. Xie, and W. Yang, “Improving diffusion-based image restoration with error contraction and error correction,” in Proc. AAAI Conf. Artif. Intell., vol. 38, 2024, pp. 756–764.   
[206] T. Wu et al., “CDDM: Channel denoising diffusion models for wireless semantic communications,” IEEE Trans. Wireless Commun., early access, Mar. 28, 2024, doi: 10.1109/TWC.2024.3379244.   
[207] M. Kim, R. Fritschek, and R. F. Schaefer, “Learning end-to-end channel coding with diffusion models,” in Proc. Int. ITG Workshop Smart Antennas 13th Conf. Syst. Commun. Coding, 2023, pp. 1–6.   
[208] N. Cheng et al., “Air-ground integrated mobile edge networks: Architecture, challenges, and opportunities,” IEEE Commun. Mag., vol. 56, no. 8, pp. 26–32, Aug. 2018.   
[209] X. Cao, B. Yang, C. Yuen, and Z. Han, “HAP-reserved communications in space-air-ground integrated networks,” IEEE Trans. Veh. Tech., vol. 70, no. 8, pp. 8286–8291, Aug. 2021.   
[210] H. Du, D. Niyato, Y.-A. Xie, Y. Cheng, J. Kang, and D. I. Kim, “Performance analysis and optimization for jammer-aided multiantenna UAV covert communication,” IEEE J. Sel. Areas Commun., vol. 40, no. 10, pp. 2962–2979, Oct. 2022.   
[211] D. Li, S. Wu, J. Jiao, N. Zhang, and Q. Zhang, “Age-oriented transmission protocol design in space-air-ground integrated networks,” IEEE Trans. Wireless Commun., vol. 21, no. 7, pp. 5573–5585, Jul. 2022.   
[212] Z. Jia, M. Sheng, J. Li, and Z. Han, “Toward data collection and transmission in 6G space-air-ground integrated networks: Cooperative HAP and LEO satellite schemes,” IEEE Internet Things J., vol. 9, no. 13, pp. 10516–10528, Sep. 2021.   
[213] R. Zhang et al., “Generative AI for space-air-ground integrated networks (SAGIN),” 2023, arXiv: 2311.06523.   
[214] H. Cui et al., “Space–air–ground integrated network (SAGIN) for 6G: Requirements, architecture and challenges,” China Commun., vol. 19, no. 2, pp. 90–108, Feb. 2022.   
[215] N. Cheng et al., “A comprehensive simulation platform for space-airground integrated network,” IEEE Wireless Commun., vol. 27, no. 1, pp. 178–185, Jan. 2020.   
[216] J. Liu, Y. Shi, Z. M. Fadlullah, and N. Kato, “Space-air-ground integrated network: A survey,” IEEE Commun. Surveys Tuts., vol. 20, no. 4, pp. 2714–2741, 4th Quart., 2018.   
[217] J. Ye, S. Dang, B. Shihada, and M.-S. Alouini, “Space-air-ground integrated networks: Outage performance analysis,” IEEE Trans. Wireless Commun., vol. 19, no. 12, pp. 7897–7912, Dec. 2020.   
[218] W. Mao, K. Xiong, Y. Lu, P. Fan, and Z. Ding, “Energy consumption minimization in secure multi-antenna UAV-assisted MEC networks with channel uncertainty,” IEEE Trans. Wireless Commun., vol. 22, no. 11, pp. 7185–7200, Nov. 2023.   
[219] Z. Wang et al., “A tutorial on extremely large-scale MIMO for 6G: Fundamentals, signal processing, and applications,” IEEE Commun. Surveys Tuts., early access, Jan. 2, 2024, doi: 10.1109/COMST.2023.3349276.

[220] Z. Wang et al., “Extremely large-scale MIMO: Fundamentals, challenges, solutions, and future directions,” IEEE Wireless Commun., early access, Apr. 10, 2023, doi: 10.1109/MWC.132.2200443.   
[221] H. Du, J. Zhang, J. Cheng, and B. Ai, “Millimeter wave communications with reconfigurable intelligent surfaces: Performance analysis and optimization,” IEEE Trans. Commun., vol. 69, no. 4, pp. 2752–2768, Apr. 2021.   
[222] Z. Wang, J. Zhang, B. Ai, C. Yuen, and M. Debbah, “Uplink performance of cell-free massive MIMO with multi-antenna users over jointly-correlated rayleigh fading channels,” IEEE Trans. Wireless Commun., vol. 21, no. 9, pp. 7391–7406, Sep. 2022.   
[223] H. Du et al., “Performance and optimization of reconfigurable intelligent surface aided THz communications,” IEEE Trans. Commun., vol. 70, no. 5, pp. 3575–3593, May 2022.   
[224] Z. Wang, J. Zhang, H. Q. Ngo, B. Ai, and M. Debbah, “Uplink precoding design for cell-free massive MIMO with iteratively weighted MMSE,” IEEE Trans. Commun., vol. 71, no. 3, pp. 1646–1664, Mar. 2023.   
[225] Y. Cui, F. Liu, X. Jing, and J. Mu, “Integrating sensing and communications for ubiquitous IoT: Applications, trends, and challenges,” IEEE Netw., vol. 35, no. 5, pp. 158–167, May 2021.   
[226] J. Wang, Z. Tian, X. Yang, and M. Zhou, “TWPalo: Through-the-wall passive localization of moving human with Wi-Fi,” Comput. Commun., vol. 157, pp. 284–297, Dec. 2020.   
[227] W. Njima, M. Chafii, A. Chorti, R. M. Shubair, and H. V. Poor, “Indoor localization using data augmentation via selective generative adversarial networks,” IEEE Access, vol. 9, pp. 98337–98347, 2021.   
[228] X. Chen, H. Li, C. Zhou, X. Liu, D. Wu, and G. Dudek, “FIDO: Ubiquitous fine-grained WiFi-based localization for unlabelled users via domain adaptation,” in Proc. Web Conf., 2020, pp. 23–33.   
[229] C. Xiao, D. Han, Y. Ma, and Z. Qin, “CsiGAN: Robust channel state information-based activity recognition with GANs,” IEEE Internet Things J., vol. 6, no. 6, pp. 10191–10204, Dec. 2019.   
[230] W. K. New, K.-K. Wong, H. Xu, K.-F. Tong, and C.-B. Chae, “Fluid antenna system: New insights on outage probability and diversity gain,” IEEE Trans. Wireless Commun., vol. 23, no. 1, pp. 128–140, Jan. 2024.   
[231] M. Khammassi, A. Kammoun, and M.-S. Alouini, “A new analytical approximation of the fluid antenna system channel,” IEEE Trans. Wireless Commun., vol. 22, no. 12, pp. 8843–8858, Dec. 2023.   
[232] A. Shojaeifard et al., “MIMO evolution beyond 5G through reconfigurable intelligent surfaces and fluid antenna systems,” Proc. IEEE, vol. 110, no. 9, pp. 1244–1265, Sep. 2022.   
[233] L. Tlebaldiyeva, G. Nauryzbayev, S. Arzykulov, A. Eltawil, and T. Tsiftsis, “Enhancing QoS through fluid antenna systems over correlated Nakagami-m fading channels,” in Proc. IEEE Wireless Commun. Netw. Conf., 2022, pp. 78–83.   
[234] Y. Zhao, F. Zhou, L. Feng, W. Li, and P. Yu, “MADRL-based 3D deployment and user association of cooperative mmWave aerial base stations for capacity enhancement,” Chin. J. Electron., vol. 32, no. 2, pp. 283–294, 2023.   
[235] Y. Lin et al., “DRL-based adaptive sharding for blockchain-based federated learning,” IEEE Trans. Commun., vol. 71, no. 10, pp. 5992–6004, Oct. 2023.

![](images/91e8d596b88352f73799b3d30e41f108085f8c84d2648625929d38949cb1ffe4.jpg)

<details>
<summary>natural_image</summary>

Portrait of a person wearing glasses and a blazer (no text or symbols visible)
</details>

Hongyang Du (Graduate Student Member, IEEE) received the B.Sc. degree from Beijing Jiaotong University, Beijing, China, in 2021, and the Ph.D. degree from the College of Computing and Data Science, Energy Research Institute @ NTU, Nanyang Technological University, Singapore, under the Interdisciplinary Graduate Program. His research interests include edge intelligence, generative AI, semantic communications, and network management. He was the recipient of the IEEE Daniel E. Noble Fellowship Award from the IEEE Vehicular

Technology Society in 2022, of the IEEE Signal Processing Society Scholarship from the IEEE Signal Processing Society in 2023, of the Chinese Government Award for Outstanding Students Abroad in 2023, and of the Singapore Data Science Consortium Dissertation Research Fellowship in 2023. He won the Honorary Mention award in the ComSoc Student Competition from IEEE Communications Society in 2023, and the First and Second Prizes in the 2024 ComSoc Social Network Technical Committee Student Competition. He is the Editor-in-Chief assistant of IEEE COMMUNICATIONS SURVEYS AND TUTORIALS from 2022 to 2024. He was recognized as an Exemplary Reviewer of the IEEE TRANSACTIONS ON COMMUNICATIONS and IEEE COMMUNICATIONS LETTERS in 2021.

![](images/78d0c733f96c64c94c3fcfa74e480774621cb961878110f37dbe517e0bcc8858.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a young man wearing a gray hoodie (no text or symbols visible)
</details>

Ruichen Zhang (Member, IEEE) received the B.E. degree from Henan University, Kaifeng, China, in 2018, and the Ph.D. degree from Beijing Jiaotong University, Beijing, China, in 2023. He is currently working as a Postdoctoral Research Fellow with the College of Computing and Data Science, Nanyang Technological University, Singapore. His research interests include reinforcement learning-enabled wireless communication networks, generative AIenabled wireless communication networks, and heterogeneous wireless networks. He serves as a Reviewer for IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, IEEE TRANSACTIONS ON MOBILE COMPUTING, IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, IEEE INTERNET OF THINGS JOURNAL, and IEEE WIRELESS COMMUNICATION LETTERS.

![](images/a0b4ecff372cd8bb6a0a19cdc50f94addf6b46a23a7e0627eab2c6e416bc5b14.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in formal attire (no text or symbols visible)
</details>

Yinqiu Liu received the B.Eng. degree from the Nanjing University of Posts and Telecommunications, China, in 2020, and the M.Sc. degree from the University of California at Los Angeles, Los Angeles, in 2022. He is currently pursuing the Ph.D. degree with the College of Computing and Data Science, Nanyang Technological University, Singapore. His current research interests include wireless communications, mobile AIGC, and generative AI.

![](images/48e607618698e3d5e9f6e5f26a38a6fb3800c154e24eaebde01c71702c67ceb7.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a young man in a black polo shirt (no text or symbols visible)
</details>

Jiacheng Wang received the Ph.D. degree from the School of Communications and Information Engineering, Chongqing University of Posts and Telecommunications, Chongqing, China. He is a Research Fellow with the College of Computing and Data Science, Nanyang Technological University, Singapore. His research interests include wireless sensing, generative AI, semantic communications, and Metaverse.

![](images/d106b3b479fde6d09cbc65c2cf4ab3b6fec2b8e0bbd2ece63c0975ff1dfa95fe.jpg)

<details>
<summary>natural_image</summary>

Portrait of a person wearing glasses and a white collared shirt (no text or symbols visible)
</details>

Yijing Lin (Graduate Student Member, IEEE) received the bachelor’s degree from North China Electric Power University. She is currently pursuing the Ph.D. degree with the State Key Laboratory of Networking and Switching Technology, Beijing University of Posts and Telecommunications, Beijing, China.

![](images/6c848f2101d86ff5d63d6b07aee7750cd307102193d0f7bf68c8729cb618bdf5.jpg)

<details>
<summary>natural_image</summary>

Portrait of a young man wearing glasses and a white shirt, outdoors with blurred greenery in the background (no text or symbols visible)
</details>

Zonghang Li is currently pursuing the Ph.D. degree with the School of Information and Communication Engineering, University of Electronic Science and Technology of China. He was a Visiting Scholar with Nanyang Technological University and Oxford University. His research interests include intelligent communication and computing systems, distributed machine learning, and federated learning. He was awarded the 2021 Future Network Leading Innovative Scientific and Technological Achievements Award by the China Institute of Communications.

![](images/46cc6e7ae7fdb88e41f065341ccfb19372617c18eebde75c356e005f38c71431.jpg)

<details>
<summary>natural_image</summary>

Portrait of a person wearing glasses and a dark jacket (no visible text or symbols)
</details>

Dusit Niyato (Fellow, IEEE) received the B.Eng. degree from the King Mongkut’s Institute of Technology Ladkrabang, Thailand, in 1999, and the Ph.D. degree in electrical and computer engineering from the University of Manitoba, Canada, in 2008. He is currently a Professor with the School of Computer Science and Engineering, Nanyang Technological University, Singapore. His research interests are in the areas of the Internet of Things, machine learning, and incentive mechanism design.

![](images/b0bca11cf26c1ee1789da1a3d2bf43805264aa43c62ecdad7e76d45665fb0f58.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a white shirt with tie against a blue background (no text or symbols visible)
</details>

Jiawen Kang (Senior Member, IEEE) received the Ph.D. degree from the Guangdong University of Technology, China, in 2018. He was a Postdoctoral Fellow with Nanyang Technological University, Singapore, from 2018 to 2021. He is currently a Full Professor with the Guangdong University of Technology, China. His research interests mainly focus on blockchain, security, and privacy protection in wireless communications and networking.

![](images/938913f25d40408a35fd66bb9f8c27e8bb197aaa62545ffa4b4809309b6b118e.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in formal attire (no text or symbols visible)
</details>

Zehui Xiong (Senior Member, IEEE) received the B.Eng. degree (with Highest Hons.) in telecommunications engineering from the Huazhong University of Science and Technology, Wuhan, China, and the Ph.D. degree in computer science and engineering from Nanyang Technological University, Singapore. He is an Assistant Professor with the Singapore University of Technology and Design, and also an Honorary Adjunct Senior Research Scientist with Alibaba-NTU Singapore Joint Research Institute, Singapore. He was a Visiting Scholar with the Department of Electrical Engineering, Princeton University and a Visiting Scholar with the Broadband Communications Research Lab, Department of Electrical and Computer Engineering, University of Waterloo. He is currently serving as an Associate Director of Future Communications Research and Development Programme. He recognized as a Highly Cited Researcher. He has published more than 200 peer-reviewed research papers in leading journals and flagship conferences. His research interests include wireless communications, Internet of Things, blockchain, edge intelligence, and metaverse. He has won over ten Best Paper Awards in international conferences. In 2023, he was featured on the list of Forbes Asia 30 under 30.

![](images/e06a95415b5152ac06002f98dfe66d23e75aad57b51716d9b1ef302022c08cb2.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a blue suit (no text or symbols visible)
</details>

Shuguang Cui (Fellow, IEEE) received the Ph.D. degree in electrical engineering from Stanford University, CA, USA, in 2005. Afterwards, he has been working as an Assistant Professor, an Associate Professor, a Full Professor, and a Chair Professor of Electrical and Computer Engineering with the University of Arizona, Texas A&M University, UC Davis, and The Chinese University of Hong Kong (Shenzhen) (CUHK-Shenzhen), respectively. He has served as the Executive Dean of the School of Science and Engineering, CUHK-Shenzhen, the Executive Vice Director of the Shenzhen Research Institute of Big Data, and the Director of the Future Network of Intelligence Institute. His current research interests focus on the merging between AI and communication networks. He was a recipient of the IEEE Signal Processing Society 2012 Best Paper Award. In 2020, he won the IEEE ICC Best Paper Award, the ICIP Best Paper Finalist, and the IEEE Globecom Best Paper Award. In 2021, he won the IEEE WCNC Best Paper Award. In 2023, he won the IEEE Marconi Best Paper Award, got elected as a Fellow of the Canadian Academy of Engineering, and starts to serve as the Editor-in-Chief for IEEE TRANSACTIONS ON MOBILE COMPUTING. He was selected as the Thomson Reuters Highly Cited Researcher and listed in the Worlds’ Most Influential Scientific Minds by ScienceWatch in 2014. He has served as the general co-chair and the TPC co-chair for many IEEE conferences. He has also been serving as an Area Editor for IEEE Signal Processing Magazine and an Associate Editor for IEEE TRANSACTIONS ON BIG DATA, IEEE TRANSACTIONS ON SIGNAL PROCESSING, IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS Series on Green Communications and Networking, and IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS. He has been an Elected Member of IEEE Signal Processing Society SPCOM Technical Committee from 2009 to 2014 and the Elected Chair of IEEE ComSoc Wireless Technical Committee from 2017 to 2018. He is a member of the Steering Committee of IEEE TRANSACTIONS ON BIG DATA and the Chair of the Steering Committee of IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING. He is also the Vice Chair of the IEEE VT Fellow Evaluation Committee and a member of the IEEE ComSoc Award Committee. He was an IEEE ComSoc Distinguished Lecturer in 2014 and IEEE VT Society Distinguished Lecturer in 2019.

![](images/cc6165fd5958f41876dbe188d3931648f3fa7f7a005b7fa1028f8b6128cddf72.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in formal attire outdoors, no visible text or symbols
</details>

Bo Ai (Fellow, IEEE) received the M.S. and Ph.D. degrees from Xidian University, Xi’an, China, in 2002 and 2004, respectively. He was with Tsinghua University, Beijing, China, where he was an Excellent Postdoctoral Research Fellow in 2007. He is currently a Professor and an Advisor of Ph.D. candidates with Beijing Jiaotong University, Beijing, where he is also the Deputy Director of the State Key Laboratory of Rail Traffic Control and Safety. He is also currently with the Engineering College, Armed Police Force, Xi’an. His interests include the research and applications of orthogonal frequency-division multiplexing techniques, high-power amplifier linearization techniques, radio propagation and channel modeling, global systems for mobile communications for railway systems, and long-term evolution for railway systems. He has authored or coauthored six books and 270 scientific research papers, and holds 26 invention patents in his research areas. He has received many awards, such as the Qiushi Outstanding Youth Award by HongKong Qiushi Foundation, the New Century Talents by the Chinese Ministry of Education, the Zhan Tianyou Railway Science and Technology Award by the Chinese Ministry of Railways, and the Science and Technology New Star by the Beijing Municipal Science and Technology Commission. He was as the Co-chair or the Session/Track Chair for many international conferences, such as the 9th International Heavy Haul Conference in 2009; the 2011 IEEE International Conference on Intelligent Rail Transportation; HSRCom2011; the 2012 IEEE International Symposium on Consumer Electronics; the 2013 International Conference on Wireless, Mobile and Multimedia; IEEE Green HetNet 2013; and the IEEE 78th Vehicular Technology Conference in 2014. He is an Associate Editor of IEEE TRANSACTIONS ON CONSUMER ELECTRONICS and an Editorial Committee Member of the Wireless Personal Communications. He is a Fellow of the Institution of Engineering and Technology.

![](images/44d2b416670589a67e7c9fbd8ac53acc3d23612ae75681cf09103d46e6a60200.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in formal attire (no text or symbols visible)
</details>

Haibo Zhou (Senior Member, IEEE) received the Ph.D. degree in information and communication engineering from Shanghai Jiao Tong University, Shanghai, China, in 2014. From 2014 to 2017, he was a Postdoctoral Fellow with the Broadband Communications Research Group, Department of Electrical and Computer Engineering, University of Waterloo. He is currently a Full Professor with the School of Electronic Science and Engineering, Nanjing University, Nanjing, China. His research interests include resource management and protocol

design in B5G/6G networks, vehicular ad hoc networks, and space-airground integrated networks. He was a recipient of the 2019 IEEE ComSoc Asia–Pacific Outstanding Young Researcher Award. He served as the Track/Symposium Co-Chair for IEEE/CIC ICCC 2019, IEEE VTC-Fall 2020, IEEE VTC-Fall 2021, WCSP 2022, IEEE GLOBECOM 2022, IEEE ICC 2024, and IEEE GLOBECOM 2024. He is currently an Associate Editor of the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE INTERNET OF THINGS JOURNAL, IEEE Network Magazine, and Journal of Communications and Information Networks. He was an IEEE ComSoc Distinguished Lecturer from 2023 to 2024 and an IEEE VTS Distinguished Lecturer from 2023 to 2025.

![](images/d58e652f02cbf7dc2ca2e00d616bf631f19bcefb25d2ae8d19b7c236c7788e8c.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a dark turtleneck (no text or symbols visible)
</details>

Dong In Kim (Fellow, IEEE) received the Ph.D. degree in electrical engineering from the University of Southern California, Los Angeles, CA, USA, in 1990. He was a Tenured Professor with the School of Engineering Science, Simon Fraser University, Burnaby, BC, Canada. He is currently a Distinguished Professor with the College of Information and Communication Engineering, Sungkyunkwan University, Suwon, South Korea. He was the first recipient of the NRF of Korea Engineering Research Center in Wireless Communications for RF Energy Harvesting from 2014 to 2021. He received several research awards, including the 2023 IEEE ComSoc Best Survey Paper Award and the 2022 IEEE Best Land Transportation Paper Award. He was selected the 2019 recipient of the IEEE ComSoc Joseph LoCicero Award for Exemplary Service to Publications. He was the General Chair of the IEEE ICC 2022, Seoul. Since 2001, he has been serving as an Editor, an Editor at Large, and an Area Editor of Wireless Communications I for IEEE TRANSACTIONS ON COMMUNICATIONS. From 2002 to 2011, he served as an Editor and a Founding Area Editor of Cross-Layer Design and Optimization for IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS. From 2008 to 2011, he served as the Co-Editor-in-Chief for the IEEE/KICS JOURNAL OF COMMUNICATIONS AND NETWORKS. He served as the Founding Editor-in-Chief for the IEEE WIRELESS COMMUNICATIONS LETTERS from 2012 to 2015. He has been listed as a 2020/2022 Highly Cited Researcher by Clarivate Analytics. He is a Fellow of the Korean Academy of Science and Technology and a member of the National Academy of Engineering of Korea.