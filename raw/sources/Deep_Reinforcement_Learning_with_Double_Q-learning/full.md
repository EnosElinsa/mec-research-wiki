# Deep Reinforcement Learning with Double Q-learning

Hado van Hasselt and Arthur Guez and David Silver

Google DeepMind

# Abstract

The popular Q-learning algorithm is known to overestimate action values under certain conditions. It was not previously known whether, in practice, such overestimations are common, whether they harm performance, and whether they can generally be prevented. In this paper, we answer all these questions affirmatively. In particular, we first show that the recent DQN algorithm, which combines Q-learning with a deep neural network, suffers from substantial overestimations in some games in the Atari 2600 domain. We then show that the idea behind the Double Q-learning algorithm, which was introduced in a tabular setting, can be generalized to work with large-scale function approximation. We propose a specific adaptation to the DQN algorithm and show that the resulting algorithm not only reduces the observed overestimations, as hypothesized, but that this also leads to much better performance on several games.

The goal of reinforcement learning (Sutton and Barto, 1998) is to learn good policies for sequential decision problems, by optimizing a cumulative future reward signal. Q-learning (Watkins, 1989) is one of the most popular reinforcement learning algorithms, but it is known to sometimes learn unrealistically high action values because it includes a maximization step over estimated action values, which tends to prefer overestimated to underestimated values.

In previous work, overestimations have been attributed to insufficiently flexible function approximation (Thrun and Schwartz, 1993) and noise (van Hasselt, 2010, 2011). In this paper, we unify these views and show overestimations can occur when the action values are inaccurate, irrespective of the source of approximation error. Of course, imprecise value estimates are the norm during learning, which indicates that overestimations may be much more common than previously appreciated.

It is an open question whether, if the overestimations do occur, this negatively affects performance in practice. Overoptimistic value estimates are not necessarily a problem in and of themselves. If all values would be uniformly higher then the relative action preferences are preserved and we would not expect the resulting policy to be any worse. Furthermore, it is known that sometimes it is good to be optimistic: optimism in the face of uncertainty is a well-known exploration technique (Kaelbling et al., 1996). If, however, the overestimations are not uniform and not concentrated at states about which we wish to learn more, then they might negatively affect the quality of the resulting policy. Thrun and Schwartz (1993) give specific examples in which this leads to suboptimal policies, even asymptotically.

To test whether overestimations occur in practice and at scale, we investigate the performance of the recent DQN algorithm (Mnih et al., 2015). DQN combines Q-learning with a flexible deep neural network and was tested on a varied and large set of deterministic Atari 2600 games, reaching human-level performance on many games. In some ways, this setting is a best-case scenario for Q-learning, because the deep neural network provides flexible function approximation with the potential for a low asymptotic approximation error, and the determinism of the environments prevents the harmful effects of noise. Perhaps surprisingly, we show that even in this comparatively favorable setting DQN sometimes substantially overestimates the values of the actions.

We show that the idea behind the Double Q-learning algorithm (van Hasselt, 2010), which was first proposed in a tabular setting, can be generalized to work with arbitrary function approximation, including deep neural networks. We use this to construct a new algorithm we call Double DQN. We then show that this algorithm not only yields more accurate value estimates, but leads to much higher scores on several games. This demonstrates that the overestimations of DQN were indeed leading to poorer policies and that it is beneficial to reduce them. In addition, by improving upon DQN we obtain state-of-the-art results on the Atari domain.

# Background

To solve sequential decision problems we can learn estimates for the optimal value of each action, defined as the expected sum of future rewards when taking that action and following the optimal policy thereafter. Under a given policy π, the true value of an action a in a state s is

$$
Q _ {\pi} (s, a) \equiv \mathbb {E} \left[ R _ {1} + \gamma R _ {2} + \dots \mid S _ {0} = s, A _ {0} = a, \pi \right],
$$

where $\gamma \in [ 0 , 1 ]$ is a discount factor that trades off the importance of immediate and later rewards. The optimal value is then $Q _ { * } ( s , a ) = \operatorname* { m a x } _ { \pi } Q _ { \pi } ( s , a )$ . An optimal policy is easily derived from the optimal values by selecting the highestvalued action in each state.

Estimates for the optimal action values can be learned using Q-learning (Watkins, 1989), a form of temporal difference learning (Sutton, 1988). Most interesting problems are too large to learn all action values in all states separately. Instead, we can learn a parameterized value function $Q ( s , a ; \pmb { \theta } _ { t } )$ . The standard Q-learning update for the parameters after taking action $A _ { t }$ in state $\bar { S _ { t } }$ and observing the immediate reward $R _ { t + 1 }$ and resulting state $S _ { t + 1 }$ is then

$$
\boldsymbol {\theta} _ {t + 1} = \boldsymbol {\theta} _ {t} + \alpha (Y _ {t} ^ {\mathrm{Q}} - Q (S _ {t}, A _ {t}; \boldsymbol {\theta} _ {t})) \nabla_ {\boldsymbol {\theta} _ {t}} Q (S _ {t}, A _ {t}; \boldsymbol {\theta} _ {t}). \tag {1}
$$

where α is a scalar step size and the target $Y _ { t } ^ { \mathrm { Q } }$ is defined as

$$
Y _ {t} ^ {\mathrm{Q}} \equiv R _ {t + 1} + \gamma \max _ {a} Q (S _ {t + 1}, a; \pmb {\theta} _ {t}). \qquad (2)
$$

This update resembles stochastic gradient descent, updating the current value $Q ( S _ { t } , A _ { t } ; \pmb { \theta } _ { t } )$ towards a target value $Y _ { t } ^ { \mathrm { Q } }$ .

# Deep Q Networks

A deep Q network (DQN) is a multi-layered neural network that for a given state s outputs a vector of action values $Q ( s , \cdot ; \theta )$ , where θ are the parameters of the network. For an n-dimensional state space and an action space containing m actions, the neural network is a function from $\mathbb { R } ^ { n }$ to $\mathbb { R } ^ { \breve { m } }$ . Two important ingredients of the DQN algorithm as proposed by Mnih et al. (2015) are the use of a target network, and the use of experience replay. The target network, with parameters $\pmb { \theta } ^ { - }$ , is the same as the online network except that its parameters are copied every τ steps from the online network, so that then $\begin{array} { r } { \pmb { \theta } _ { t } ^ { - } = \pmb { \theta } _ { t } , } \end{array}$ , and kept fixed on all other steps. The target used by DQN is then

$$
Y _ {t} ^ {\mathrm{DQN}} \equiv R _ {t + 1} + \gamma \max _ {a} Q (S _ {t + 1}, a; \pmb {\theta} _ {t} ^ {-}). \qquad (3)
$$

For the experience replay (Lin, 1992), observed transitions are stored for some time and sampled uniformly from this memory bank to update the network. Both the target network and the experience replay dramatically improve the performance of the algorithm (Mnih et al., 2015).

# Double Q-learning

The max operator in standard Q-learning and DQN, in (2) and (3), uses the same values both to select and to evaluate an action. This makes it more likely to select overestimated values, resulting in overoptimistic value estimates. To prevent this, we can decouple the selection from the evaluation. This is the idea behind Double Q-learning (van Hasselt, 2010).

In the original Double Q-learning algorithm, two value functions are learned by assigning each experience randomly to update one of the two value functions, such that there are two sets of weights, θ and θ0. For each update, one set of weights is used to determine the greedy policy and the other to determine its value. For a clear comparison, we can first untangle the selection and evaluation in Q-learning and rewrite its target (2) as

$$
Y _ {t} ^ {\mathrm{Q}} = R _ {t + 1} + \gamma Q (S _ {t + 1}, \underset {a} {\operatorname{argmax}} Q (S _ {t + 1}, a; \boldsymbol {\theta} _ {t}); \boldsymbol {\theta} _ {t})  .
$$

The Double Q-learning error can then be written as

$$
Y _ {t} ^ {\text { DoubleQ }} \equiv R _ {t + 1} + \gamma Q (S _ {t + 1}, \underset {a} {\operatorname{argmax}} Q (S _ {t + 1}, a; \boldsymbol {\theta} _ {t}); \boldsymbol {\theta} _ {t} ^ {\prime}). \tag {4}
$$

Notice that the selection of the action, in the argmax, is still due to the online weights $\theta _ { t }$ . This means that, as in $\mathrm { Q } \mathrm { - }$ learning, we are still estimating the value of the greedy policy according to the current values, as defined by $\pmb \theta _ { t } .$ . However, we use the second set of weights ${ \pmb \theta } _ { t } ^ { \prime }$ to fairly evaluate the value of this policy. This second set of weights can be updated symmetrically by switching the roles of θ and $\pmb { \theta } ^ { \prime }$ .

# Overoptimism due to estimation errors

Q-learning’s overestimations were first investigated by Thrun and Schwartz (1993), who showed that if the action values contain random errors uniformly distributed in an interval $[ - \epsilon , \epsilon ]$ then each target is overestimated up to $\gamma \epsilon \frac { m - 1 } { m + 1 }$ m−1 , where m is the number of actions. In addition, Thrun and Schwartz give a concrete example in which these overestimations even asymptotically lead to sub-optimal policies, and show the overestimations manifest themselves in a small toy problem when using function approximation. Later van Hasselt (2010) argued that noise in the environment can lead to overestimations even when using tabular representation, and proposed Double Q-learning as a solution.

In this section we demonstrate more generally that estimation errors of any kind can induce an upward bias, regardless of whether these errors are due to environmental noise, function approximation, non-stationarity, or any other source. This is important, because in practice any method will incur some inaccuracies during learning, simply due to the fact that the true values are initially unknown.

The result by Thrun and Schwartz (1993) cited above gives an upper bound to the overestimation for a specific setup, but it is also possible, and potentially more interesting, to derive a lower bound.

Theorem 1. Consider a state s in which all the true optimal action values are equal at $Q _ { * } ( s , a ) = V _ { * } ( s )$ for some $V _ { * } ( s )$ . Let $Q _ { t }$ be arbitrary value estimates that are on the whole unbiased in the sense that $\begin{array} { r } { \sum _ { a } ( Q _ { t } ( s , a ) - V _ { * } ( s ) ) = 0 , } \end{array}$ , but that are not all correct, such that $\begin{array} { r } { \frac { 1 } { m } \sum _ { a } ( Q _ { t } ( s , a ) - V _ { * } ( s ) ) ^ { 2 } = C } \end{array}$ for some $C > 0$ , where m $\geq 2$ is the number of actions in s. Under these conditions, ma $\begin{array} { r } { \mathfrak { c } _ { a } Q _ { t } ( s , a ) \geq V _ { * } ( s ) + \sqrt { \frac { C } { m - 1 } } . } \end{array}$ . This lower bound is tight. Under the same conditions, the lower bound on the absolute error of the Double Q-learning estimate is zero. (Proof in appendix.)

Note that we did not need to assume that estimation errors for different actions are independent. This theorem shows that even if the value estimates are on average correct, estimation errors of any source can drive the estimates up and away from the true optimal values.

The lower bound in Theorem 1 decreases with the number of actions. This is an artifact of considering the lower bound, which requires very specific values to be attained. More typically, the overoptimism increases with the number of actions as shown in Figure 1. Q-learning’s overestimations there indeed increase with the number of actions, while Double Q-learning is unbiased. As another example, if for all actions $Q _ { * } ( s , \bar { a } ) = V _ { * } ( s )$ and the estimation errors $Q _ { t } ( s , a ) - V _ { * } ( s )$ are uniformly random in [−1, 1], then the overoptimism is m−1 . $\frac { m - 1 } { m + 1 }$ (Proof in appendix.)

![](images/e844c1d0a707f2009788c810ee09e0acb93c6756e7c2a0a02c8745ae477dfd41.jpg)

<details>
<summary>bar</summary>

| number of actions | max_a Q(s, a) - V_*(s) | Q'(s, argmax_a Q(s, a)) - V_*(s) |
| ----------------- | ---------------------- | -------------------------------- |
| 2                 | 0.0                    | 0.0                              |
| 4                 | 0.5                    | 0.0                              |
| 8                 | 0.7                    | 0.0                              |
| 16                | 1.1                    | 0.2                              |
| 32                | 1.2                    | 0.1                              |
| 64                | 1.2                    | 0.1                              |
| 128               | 1.3                    | 0.0                              |
| 256               | 1.4                    | 0.0                              |
| 512               | 1.5                    | 0.0                              |
| 1024              | 1.6                    | 0.0                              |
</details>

Figure 1: The orange bars show the bias in a single $\mathrm { Q } \mathrm { - }$ learning update when the action values are $Q ( s , a ) \ =$ $V _ { * } ( s ) + \epsilon _ { a }$ and the errors $\{ \epsilon _ { a } \} _ { a = 1 } ^ { m }$ are independent standard normal random variables. The second set of action values $Q ^ { \prime }$ , used for the blue bars, was generated identically and independently. All bars are the average of 100 repetitions.

We now turn to function approximation and consider a real-valued continuous state space with 10 discrete actions in each state. For simplicity, the true optimal action values in this example depend only on state so that in each state all actions have the same true value. These true values are shown in the left column of plots in Figure 2 (purple lines) and are defined as either $Q _ { * } ( s , a ) \ = \ \sin ( s )$ (top row) or $Q _ { * } ( s , a ) = 2 \exp ( - s ^ { 2 } )$ (middle and bottom rows). The left plots also show an approximation for a single action (green lines) as a function of state as well as the samples the estimate is based on (green dots). The estimate is a d-degree polynomial that is fit to the true values at sampled states, where $d \ = \ 6$ (top and middle rows) or $d \ = \ 9$ (bottom row). The samples match the true function exactly: there is no noise and we assume we have ground truth for the action value on these sampled states. The approximation is inexact even on the sampled states for the top two rows because the function approximation is insufficiently flexible. In the bottom row, the function is flexible enough to fit the green dots, but this reduces the accuracy in unsampled states. Notice that the sampled states are spaced further apart near the left side of the left plots, resulting in larger estimation errors. In many ways this is a typical learning setting, where at each point in time we only have limited data.

The middle column of plots in Figure 2 shows estimated action value functions for all 10 actions (green lines), as functions of state, along with the maximum action value in each state (black dashed line). Although the true value function is the same for all actions, the approximations differ because we have supplied different sets of sampled states.1 The maximum is often higher than the ground truth shown in purple on the left. This is confirmed in the right plots, which shows the difference between the black and purple curves in orange. The orange line is almost always positive, indicating an upward bias. The right plots also show the estimates from Double Q-learning in ${ \mathrm { b l u e } } ^ { 2 }$ , which are on average much closer to zero. This demonstrates that Double Qlearning indeed can successfully reduce the overoptimism of Q-learning.

The different rows in Figure 2 show variations of the same experiment. The difference between the top and middle rows is the true value function, demonstrating that overestimations are not an artifact of a specific true value function. The difference between the middle and bottom rows is the flexibility of the function approximation. In the left-middle plot, the estimates are even incorrect for some of the sampled states because the function is insufficiently flexible. The function in the bottom-left plot is more flexible but this causes higher estimation errors for unseen states, resulting in higher overestimations. This is important because flexible parametric function approximators are often employed in reinforcement learning (see, e.g., Tesauro 1995; Sallans and Hinton 2004; Riedmiller 2005; Mnih et al. 2015).

In contrast to van Hasselt (2010) we did not use a statistical argument to find overestimations, the process to obtain Figure 2 is fully deterministic. In contrast to Thrun and Schwartz (1993), we did not rely on inflexible function approximation with irreducible asymptotic errors; the bottom row shows that a function that is flexible enough to cover all samples leads to high overestimations. This indicates that the overestimations can occur quite generally.

In the examples above, overestimations occur even when assuming we have samples of the true action value at certain states. The value estimates can further deteriorate if we bootstrap off of action values that are already overoptimistic, since this causes overestimations to propagate throughout our estimates. Although uniformly overestimating values might not hurt the resulting policy, in practice overestimation errors will differ for different states and actions. Overestimation combined with bootstrapping then has the pernicious effect of propagating the wrong relative information about which states are more valuable than others, directly affecting the quality of the learned policies.

The overestimations should not be confused with optimism in the face of uncertainty (Sutton, 1990; Agrawal, 1995; Kaelbling et al., 1996; Auer et al., 2002; Brafman and Tennenholtz, 2003; Szita and Lorincz, 2008; Strehl et al., ˝ 2009), where an exploration bonus is given to states or actions with uncertain values. Conversely, the overestimations discussed here occur only after updating, resulting in overoptimism in the face of apparent certainty. This was already observed by Thrun and Schwartz (1993), who noted that, in contrast to optimism in the face of uncertainty, these overestimations actually can impede learning an optimal policy. We will see this negative effect on policy quality confirmed later in the experiments as well: when we reduce the overestimations using Double Q-learning, the policies improve.

![](images/60e4d3fa99b45cb168be76debfeb1074f81a627d9f51b9ed7cc1255a3bb1b098.jpg)

<details>
<summary>line</summary>

| Method | State | Value |
|--------|-------|-------|
| Q*     | -6    | 0.61  |
| Q*     | -4    | 0.61  |
| Q*     | -2    | 0.61  |
| Q*     | 0     | 0.61  |
| Q*     | 2     | 0.61  |
| Q*     | 4     | 0.61  |
| Q*     | 6     | 0.61  |
| Qt     | -6    | -0.02 |
| Qt     | -4    | -0.02 |
| Qt     | -2    | -0.02 |
| Qt     | 0     | -0.02 |
| Qt     | 2     | -0.02 |
| Qt     | 4     | -0.02 |
| Qt     | 6     | -0.02 |
| maxa   | -6    | +0.47 |
| maxa   | -4    | +0.47 |
| maxa   | -2    | +0.47 |
| maxa   | 0     | +0.47 |
| maxa   | 2     | +0.47 |
| maxa   | 4     | +0.47 |
| maxa   | 6     | +0.47 |
| Double-Q| -6    | +3.35 |
| Double-Q| -4    | +3.35 |
| Double-Q| -2    | +3.35 |
| Double-Q| 0     | +3.35 |
| Double-Q| 2     | +3.35 |
| Double-Q| 4     | +3.35 |
| Double-Q| 6     | +3.35 |
| All estimates and max | -6    | 0.61  |
| All estimates and max | -4    | 0.61  |
| All estimates and max | -2    | 0.61  |
| All estimates and max | 0     | 0.61  |
| All estimates and max | 2     | 0.61  |
| All estimates and max | 4     | 0.61  |
| All estimates and max | 6     | 0.61  |
| bias as function of state | -6    | -0.02 |
| bias as function of state | -4    | -0.02 |
| bias as function of state | -2    | -0.02 |
| bias as function of state | 0     | -0.02 |
| bias as function of state | 2     | -0.02 |
| bias as function of state | 4     | -0.02 |
| bias as function of state | 6     | -0.02 |
| Average error (line)      | -6    | +3.35 |
| Average error (line)      | -4    | +3.35 |
| Average error (line)      | -2    | +3.35 |
| Average error (line)      | 0     | +3.35 |
| Average error (line)      | 2     | +3.35 |
| Average error (line)      | 4     | +3.35 |
| Average error (line)      | 6     | +3.35 |
Double-Q estimate (line) |
| Double-Q estimate (line)   | -6    | +3.35 |
| Double-Q estimate (line)   | -4    | +3.35 |
| Double-Q estimate (line)   | -2    | +3.35 |
| Double-Q estimate (line)   | 0     | +3.35 |
| Double-Q estimate (line)   | 2     | +3.35 |
| Double-Q estimate (line)   | 4     | +3.35 |
| Double-Q estimate (line)   | 6     | +3.35 |
| Average error (line)      | -6    | +3.35 |
| Average error (line)      | -4    | +3.35 |
| Average error (line)      | -2    | +3.35 |
| Average error (line)      | 0     | +3.35 |
| Average error (line)      | 2     | +3.35 |
| Average error (line)      |
</details>

Figure 2: Illustration of overestimations during learning. In each state (x-axis), there are 10 actions. The left column shows the true values $\bar { V _ { * } ( s ) }$ (purple line). All true action values are defined by $Q _ { * } ( s , a ) = V _ { * } ( s )$ . The green line shows estimated values $Q ( s , a )$ for one action as a function of state, fitted to the true value at several sampled states (green dots). The middle column plots show all the estimated values (green), and the maximum of these values (dashed black). The maximum is higher than the true value (purple, left plot) almost everywhere. The right column plots shows the difference in orange. The blue line in the right plots is the estimate used by Double Q-learning with a second set of samples for each state. The blue line is much closer to zero, indicating less bias. The three rows correspond to different true functions (left, purple) or capacities of the fitted function (left, green). (Details in the text)

# Double DQN

The idea of Double Q-learning is to reduce overestimations by decomposing the max operation in the target into action selection and action evaluation. Although not fully decoupled, the target network in the DQN architecture provides a natural candidate for the second value function, without having to introduce additional networks. We therefore propose to evaluate the greedy policy according to the online network, but using the target network to estimate its value. In reference to both Double Q-learning and DQN, we refer to the resulting algorithm as Double DQN. Its update is the same as for DQN, but replacing the target $Y _ { t } ^ { \mathrm { D Q N } }$ with

$$
Y _ {t} ^ {\text { DoubleDQN }} \equiv R _ {t + 1} + \gamma Q (S _ {t + 1}, \underset {a} {\operatorname{argmax}} Q (S _ {t + 1}, a; \boldsymbol {\theta} _ {t}), \boldsymbol {\theta} _ {t} ^ {-})  .
$$

In comparison to Double Q-learning (4), the weights of the second network $\theta _ { t } ^ { \prime }$ are replaced with the weights of the target network $\pmb { \theta } _ { t } ^ { - }$ for the evaluation of the current greedy policy. The update to the target network stays unchanged from DQN, and remains a periodic copy of the online network.

This version of Double DQN is perhaps the minimal possible change to DQN towards Double Q-learning. The goal is to get most of the benefit of Double Q-learning, while keeping the rest of the DQN algorithm intact for a fair comparison, and with minimal computational overhead.

# Empirical results

In this section, we analyze the overestimations of DQN and show that Double DQN improves over DQN both in terms of value accuracy and in terms of policy quality. To further test the robustness of the approach we additionally evaluate the algorithms with random starts generated from expert human trajectories, as proposed by Nair et al. (2015).

Our testbed consists of Atari 2600 games, using the Arcade Learning Environment (Bellemare et al., 2013). The goal is for a single algorithm, with a fixed set of hyperparameters, to learn to play each of the games separately from interaction given only the screen pixels as input. This is a demanding testbed: not only are the inputs high-dimensional, the game visuals and game mechanics vary substantially between games. Good solutions must therefore rely heavily on the learning algorithm — it is not practically feasible to overfit the domain by relying only on tuning.

We closely follow the experimental setting and network architecture outlined by Mnih et al. (2015). Briefly, the network architecture is a convolutional neural network (Fukushima, 1988; LeCun et al., 1998) with 3 convolution layers and a fully-connected hidden layer (approximately 1.5M parameters in total). The network takes the last four frames as input and outputs the action value of each action. On each game, the network is trained on a single GPU for 200M frames, or approximately 1 week.

# Results on overoptimism

Figure 3 shows examples of DQN’s overestimations in six Atari games. DQN and Double DQN were both trained under the exact conditions described by Mnih et al. (2015). DQN is consistently and sometimes vastly overoptimistic about the value of the current greedy policy, as can be seen by comparing the orange learning curves in the top row of plots to the straight orange lines, which represent the actual discounted value of the best learned policy. More precisely, the (averaged) value estimates are computed regularly during training with full evaluation phases of length T = 125, 000 steps as

$$
\frac {1}{T} \sum_ {t = 1} ^ {T} \underset {a} {\operatorname{argmax}} Q (S _ {t}, a; \boldsymbol {\theta})  .
$$

![](images/6180224cbadb35911a4e1454242ef8eb65a5f8f22a6ad9a6812cb9b1d3e0fd71.jpg)  
Figure 3: The top and middle rows show value estimates by DQN (orange) and Double DQN (blue) on six Atari games. The results are obtained by running DQN and Double DQN with 6 different random seeds with the hyper-parameters employed by Mnih et al. (2015). The darker line shows the median over seeds and we average the two extreme values to obtain the shaded area (i.e., 10% and 90% quantiles with linear interpolation). The straight horizontal orange (for DQN) and blue (for Double DQN) lines in the top row are computed by running the corresponding agents after learning concluded, and averaging the actual discounted return obtained from each visited state. These straight lines would match the learning curves at the right side of the plots if there is no bias. The middle row shows the value estimates (in log scale) for two games in which DQN’s overoptimism is quite extreme. The bottom row shows the detrimental effect of this on the score achieved by the agent as it is evaluated during training: the scores drop when the overestimations begin. Learning with Double DQN is much more stable.

The ground truth averaged values are obtained by running the best learned policies for several episodes and computing the actual cumulative rewards. Without overestimations we would expect these quantities to match up (i.e., the curve to match the straight line at the right of each plot). Instead, the learning curves of DQN consistently end up much higher than the true values. The learning curves for Double DQN, shown in blue, are much closer to the blue straight line representing the true value of the final policy. Note that the blue straight line is often higher than the orange straight line. This indicates that Double DQN does not just produce more accurate value estimates but also better policies.

More extreme overestimations are shown in the middle two plots, where DQN is highly unstable on the games Asterix and Wizard of Wor. Notice the log scale for the values on the y-axis. The bottom two plots shows the corresponding scores for these two games. Notice that the increases in value estimates for DQN in the middle plots coincide with decreasing scores in bottom plots. Again, this indicates that the overestimations are harming the quality of the resulting policies. If seen in isolation, one might perhaps be tempted to think the observed instability is related to inherent instability problems of off-policy learning with function approximation (Baird, 1995; Tsitsiklis and Van Roy, 1997; Sutton et al., 2008; Maei, 2011; Sutton et al., 2015). However, we see that learning is much more stable with Double DQN,

<table><tr><td></td><td>DQN</td><td>Double DQN</td></tr><tr><td>Median</td><td>93.5%</td><td>114.7%</td></tr><tr><td>Mean</td><td>241.1%</td><td>330.3%</td></tr></table>

Table 1: Summary of normalized performance up to 5 minutes of play on 49 games. Results for DQN are from Mnih et al. (2015)

suggesting that the cause for these instabilities is in fact Qlearning’s overoptimism. Figure 3 only shows a few examples, but overestimations were observed for DQN in all 49 tested Atari games, albeit in varying amounts.

# Quality of the learned policies

Overoptimism does not always adversely affect the quality of the learned policy. For example, DQN achieves optimal behavior in Pong despite slightly overestimating the policy value. Nevertheless, reducing overestimations can significantly benefit the stability of learning; we see clear examples of this in Figure 3. We now assess more generally how much Double DQN helps in terms of policy quality by evaluating on all 49 games that DQN was tested on.

As described by Mnih et al. (2015) each evaluation episode starts by executing a special no-op action that does not affect the environment up to 30 times, to provide different starting points for the agent. Some exploration during evaluation provides additional randomization. For Double DQN we used the exact same hyper-parameters as for DQN, to allow for a controlled experiment focused just on reducing overestimations. The learned policies are evaluated for 5 mins of emulator time (18,000 frames) with an - greedy policy where $\epsilon = 0 . 0 5$ . The scores are averaged over 100 episodes. The only difference between Double DQN and DQN is the target, using $Y _ { t } ^ { \mathrm { D o u b l e D Q N } }$ rather than $Y ^ { \mathrm { D Q N } }$ . This evaluation is somewhat adversarial, as the used hyperparameters were tuned for DQN but not for Double DQN.

<table><tr><td></td><td>DQN</td><td>Double DQN</td><td>Double DQN (tuned)</td></tr><tr><td>Median</td><td>47.5%</td><td>88.4%</td><td>116.7%</td></tr><tr><td>Mean</td><td>122.0%</td><td>273.1%</td><td>475.2%</td></tr></table>

Table 2: Summary of normalized performance up to 30 minutes of play on 49 games with human starts. Results for DQN are from Nair et al. (2015).

To obtain summary statistics across games, we normalize the score for each game as follows:

$$
\text { score } _ {\text { normalized }} = \frac {\text { score } _ {\text { agent }} - \text { score } _ {\text { random }}}{\text { score } _ {\text { human }} - \text { score } _ {\text { random }}}. \tag {5}
$$

The ‘random’ and ‘human’ scores are the same as used by Mnih et al. (2015), and are given in the appendix.

Table 1, under no ops, shows that on the whole Double DQN clearly improves over DQN. A detailed comparison (in appendix) shows that there are several games in which Double DQN greatly improves upon DQN. Noteworthy examples include Road Runner (from 233% to 617%), Asterix (from 70% to 180%), Zaxxon (from 54% to 111%), and Double Dunk (from 17% to 397%).

The Gorila algorithm (Nair et al., 2015), which is a massively distributed version of DQN, is not included in the table because the architecture and infrastructure is sufficiently different to make a direct comparison unclear. For completeness, we note that Gorila obtained median and mean normalized scores of 96% and 495%, respectively.

# Robustness to Human starts

One concern with the previous evaluation is that in deterministic games with a unique starting point the learner could potentially learn to remember sequences of actions without much need to generalize. While successful, the solution would not be particularly robust. By testing the agents from various starting points, we can test whether the found solutions generalize well, and as such provide a challenging testbed for the learned polices (Nair et al., 2015).

We obtained 100 starting points sampled for each game from a human expert’s trajectory, as proposed by Nair et al. (2015). We start an evaluation episode from each of these starting points and run the emulator for up to 108,000 frames (30 mins at 60Hz including the trajectory before the starting point). Each agent is only evaluated on the rewards accumulated after the starting point.

For this evaluation we include a tuned version of Double DQN. Some tuning is appropriate because the hyperparameters were tuned for DQN, which is a different algorithm. For the tuned version of Double DQN, we increased the number of frames between each two copies of the target network from 10,000 to 30,000, to reduce overestimations further because immediately after each switch DQN and Double DQN both revert to Q-learning. In addition, we reduced the exploration during learning from  = 0.1 to $\epsilon = 0 . 0 1$ , and then used $\epsilon = 0 . 0 0 1$ during evaluation. Finally, the tuned version uses a single shared bias for all action values in the top layer of the network. Each of these changes improved performance and together they result in clearly better results.3

![](images/a151ab1409b774a8e9fe7ff3375864aad184a8a7411139151f5db78051c2109e.jpg)  
Figure 4: Normalized scores on 57 Atari games, tested for 100 episodes per game with human starts. Compared to Mnih et al. (2015), eight games additional games were tested. These are indicated with stars and a bold font.

Table 2 reports summary statistics for this evaluation on the 49 games from Mnih et al. (2015). Double DQN obtains clearly higher median and mean scores. Again Gorila DQN (Nair et al., 2015) is not included in the table, but for completeness note it obtained a median of 78% and a mean of 259%. Detailed results, plus results for an additional 8 games, are available in Figure 4 and in the appendix. On several games the improvements from DQN to Double DQN are striking, in some cases bringing scores much closer to human, or even surpassing these.

Double DQN appears more robust to this more challenging evaluation, suggesting that appropriate generalizations occur and that the found solutions do not exploit the determinism of the environments. This is appealing, as it indicates progress towards finding general solutions rather than a deterministic sequence of steps that would be less robust.

# Discussion

This paper has five contributions. First, we have shown why Q-learning can be overoptimistic in large-scale problems, even if these are deterministic, due to the inherent estimation errors of learning. Second, by analyzing the value estimates on Atari games we have shown that these overestimations are more common and severe in practice than previously acknowledged. Third, we have shown that Double Q-learning can be used at scale to successfully reduce this overoptimism, resulting in more stable and reliable learning. Fourth, we have proposed a specific implementation called Double DQN, that uses the existing architecture and deep neural network of the DQN algorithm without requiring additional networks or parameters. Finally, we have shown that Double DQN finds better policies, obtaining new state-ofthe-art results on the Atari 2600 domain.

# Acknowledgments

We would like to thank Tom Schaul, Volodymyr Mnih, Marc Bellemare, Thomas Degris, Georg Ostrovski, and Richard Sutton for helpful comments, and everyone at Google Deep-Mind for a constructive research environment.

# References

R. Agrawal. Sample mean based index policies with O(log n) regret for the multi-armed bandit problem. Advances in Applied Probability, pages 1054–1078, 1995.   
P. Auer, N. Cesa-Bianchi, and P. Fischer. Finite-time analysis of the multiarmed bandit problem. Machine learning, 47(2-3):235– 256, 2002.   
L. Baird. Residual algorithms: Reinforcement learning with function approximation. In Machine Learning: Proceedings of the Twelfth International Conference, pages 30–37, 1995.   
M. G. Bellemare, Y. Naddaf, J. Veness, and M. Bowling. The arcade learning environment: An evaluation platform for general agents. J. Artif. Intell. Res. (JAIR), 47:253–279, 2013.   
R. I. Brafman and M. Tennenholtz. R-max-a general polynomial time algorithm for near-optimal reinforcement learning. The Journal of Machine Learning Research, 3:213–231, 2003.   
K. Fukushima. Neocognitron: A hierarchical neural network capable of visual pattern recognition. Neural networks, 1(2):119– 130, 1988.   
L. P. Kaelbling, M. L. Littman, and A. W. Moore. Reinforcement learning: A survey. Journal of Artificial Intelligence Research, 4:237–285, 1996.   
Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-based learning applied to document recognition. Proceedings of the IEEE, 86(11):2278–2324, 1998.   
L. Lin. Self-improving reactive agents based on reinforcement learning, planning and teaching. Machine learning, 8(3):293– 321, 1992.

H. R. Maei. Gradient temporal-difference learning algorithms. PhD thesis, University of Alberta, 2011.   
V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski, S. Petersen, C. Beattie, A. Sadik, I. Antonoglou, H. King, D. Kumaran, D. Wierstra, S. Legg, and D. Hassabis. Humanlevel control through deep reinforcement learning. Nature, 518 (7540):529–533, 2015.   
A. Nair, P. Srinivasan, S. Blackwell, C. Alcicek, R. Fearon, A. D. Maria, V. Panneershelvam, M. Suleyman, C. Beattie, S. Petersen, S. Legg, V. Mnih, K. Kavukcuoglu, and D. Silver. Massively parallel methods for deep reinforcement learning. In Deep Learning Workshop, ICML, 2015.   
M. Riedmiller. Neural fitted Q iteration - first experiences with a data efficient neural reinforcement learning method. In J. Gama, R. Camacho, P. Brazdil, A. Jorge, and L. Torgo, editors, Proceedings of the 16th European Conference on Machine Learning (ECML’05), pages 317–328. Springer, 2005.   
B. Sallans and G. E. Hinton. Reinforcement learning with factored states and actions. The Journal of Machine Learning Research, 5:1063–1088, 2004.   
A. L. Strehl, L. Li, and M. L. Littman. Reinforcement learning in finite MDPs: PAC analysis. The Journal of Machine Learning Research, 10:2413–2444, 2009.   
R. S. Sutton. Learning to predict by the methods of temporal differences. Machine learning, 3(1):9–44, 1988.   
R. S. Sutton. Integrated architectures for learning, planning, and reacting based on approximating dynamic programming. In Proceedings of the seventh international conference on machine learning, pages 216–224, 1990.   
R. S. Sutton and A. G. Barto. Introduction to reinforcement learning. MIT Press, 1998.   
R. S. Sutton, C. Szepesvari, and H. R. Maei. A convergent O(n) ´ algorithm for off-policy temporal-difference learning with linear function approximation. Advances in Neural Information Processing Systems 21 (NIPS-08), 21:1609–1616, 2008.   
R. S. Sutton, A. R. Mahmood, and M. White. An emphatic approach to the problem of off-policy temporal-difference learning. arXiv preprint arXiv:1503.04269, 2015.   
I. Szita and A. Lorincz. The many faces of optimism: a unifying ˝ approach. In Proceedings of the 25th international conference on Machine learning, pages 1048–1055. ACM, 2008.   
G. Tesauro. Temporal difference learning and td-gammon. Communications of the ACM, 38(3):58–68, 1995.   
S. Thrun and A. Schwartz. Issues in using function approximation for reinforcement learning. In M. Mozer, P. Smolensky, D. Touretzky, J. Elman, and A. Weigend, editors, Proceedings of the 1993 Connectionist Models Summer School, Hillsdale, NJ, 1993. Lawrence Erlbaum.   
J. N. Tsitsiklis and B. Van Roy. An analysis of temporal-difference learning with function approximation. IEEE Transactions on Automatic Control, 42(5):674–690, 1997.   
H. van Hasselt. Double Q-learning. Advances in Neural Information Processing Systems, 23:2613–2621, 2010.   
H. van Hasselt. Insights in Reinforcement Learning. PhD thesis, Utrecht University, 2011.   
C. J. C. H. Watkins. Learning from delayed rewards. PhD thesis, University of Cambridge England, 1989.

# Appendix

Theorem 1. Consider a state s in which all the true optimal action values are equal at $Q _ { * } ( s , a ) \ : = \ : V _ { * } ( s )$ for some $V _ { * } ( s )$ . Let $Q _ { t }$ be arbitrary value estimates that are on the whole unbiased in the sense that $\dot { \sum } _ { a } ( Q _ { t } ( s , a ) - V _ { * } ( s ) ) = 0 ,$ , but that are not all zero, such that $\begin{array} { r } { \frac { 1 } { m } \bar { \sum } _ { a } ( Q _ { t } ( s , a ) - V _ { * } ( s ) ) ^ { 2 } = C f o r } \end{array}$ r some $C > 0 ,$ , where $m \geq 2$ is the number of actions in s. Under these conditions, maxa $\begin{array} { r } { Q _ { t } ( s , a ) \geq V _ { * } ( s ) + \sqrt { \frac { C } { m - 1 } } } \end{array}$ q Cm−1 . This lower bound is tight. Under the same conditions, the lower bound on the absolute error of the Double Q-learning estimate is zero.

Proof of Theorem 1. Define the errors for each action a as $\epsilon _ { a } =$ $Q _ { t } ( \tilde { s } , \tilde { a } ) - V _ { * } ( s )$ . Suppose that there exists a setting of $\left\{ \epsilon _ { a } \right\}$ such that maxa a $< \sqrt { \frac { C } { m - 1 } } . \mathrm { L e t } \left\{ \epsilon _ { i } ^ { + } \right\}$ be the set of positive  of size $n ,$ and $\{ \epsilon _ { j } ^ { - } \}$ the set of strictly negative  of size $m - n$ (such that $\{ \epsilon \} = \{ \epsilon _ { i } ^ { + } \} \cup \{ \epsilon _ { j } ^ { - } \}$ . If $n = m$ , then $\begin{array} { r } { \sum _ { a } \epsilon _ { a } = 0 \implies } \end{array}$ $\epsilon _ { a } = 0 \forall a$ , which contradicts $\sum _ { a } \epsilon _ { a } ^ { 2 } = m C$ . Hence, it must be that n ≤ m − 1. Then, Pni=1 +i ≤ n maxi +i < nq Cm−1 , $n \leq m - 1$ $\textstyle \sum _ { i = 1 } ^ { n } \epsilon _ { i } ^ { + } \ \leq$ $\begin{array} { r } { \epsilon _ { i } ^ { + } < n \sqrt { \frac { C } { m - 1 } } , } \end{array}$ and therefore (using the constraint $\textstyle \sum _ { a } \epsilon _ { a } = 0 )$ we also have that $\begin{array} { r } { \sum _ { j = 1 } ^ { m - n } | \epsilon _ { j } ^ { - } | < n \sqrt { \frac { C } { m - 1 } } } \end{array}$ . This implies maxj $\begin{array} { r } { | \epsilon _ { j } ^ { - } | < n \sqrt { \frac { C } { m - 1 } } . \mathbf { B } \mathbf { y } } \end{array}$ Cm−1 . By Holder’s inequality, then ¨

$$
\begin{array}{l} \sum_ {j = 1} ^ {m - n} (\epsilon_ {j} ^ {-}) ^ {2} \leq \sum_ {j = 1} ^ {m - n} | \epsilon_ {j} ^ {-} | \cdot \max _ {j} | \epsilon_ {j} ^ {-} | \\ <   n \sqrt {\frac {C}{m - 1}} n \sqrt {\frac {C}{m - 1}}. \\ \end{array}
$$

We can now combine these relations to compute an upper-bound on the sum of squares for all $\epsilon _ { a } .$ :

$$
\begin{array}{l} \sum_ {a = 1} ^ {m} (\epsilon_ {a}) ^ {2} = \sum_ {i = 1} ^ {n} (\epsilon_ {i} ^ {+}) ^ {2} + \sum_ {j = 1} ^ {m - n} (\epsilon_ {j} ^ {-}) ^ {2} \\ <   n \frac {C}{m - 1} + n \sqrt {\frac {C}{m - 1}} n \sqrt {\frac {C}{m - 1}} \\ = C \frac {n (n + 1)}{m - 1} \\ \leq m C. \\ \end{array}
$$

This contradicts the assumption that $\begin{array} { r } { \sum _ { a = 1 } ^ { m } \epsilon _ { a } ^ { 2 } < m C , } \end{array}$ , and therefore maxa $\epsilon _ { a } \geq \sqrt { \frac { C } { m - 1 } } .$ 1 for all settings of  that satisfy the constraints. We can check that the lower-bound is tight by setting $\epsilon _ { a } = \sqrt { \frac { C } { m - 1 } }$ for $a = 1 , \ldots , m - 1$ and $\epsilon _ { m } = - \sqrt { ( m - 1 ) C }$ . This verifies $\sum _ { a } \epsilon _ { a } ^ { 2 } = m C$ and $\textstyle \sum _ { a } \epsilon _ { a } = 0$ .

The only tight lower bound on the absolute error for Double $\mathrm { Q } \mathrm { - }$ learning $\begin{array} { r } { | Q _ { t } ^ { \prime } ( s , \operatorname { a r g m a x } _ { a } Q _ { t } ( s , a ) ) - V _ { * } ( s ) | } \end{array}$ is zero. This can be seen by because we can have

$$
Q _ {t} (s, a _ {1}) = V _ {*} (s) + \sqrt {C \frac {m - 1}{m}},
$$

and

$$
Q _ {t} (s, a _ {i}) = V _ {*} (s) - \sqrt {C \frac {1}{m (m - 1)}}, \text { for } i > 1.
$$

Then the conditions of the theorem hold. If then, furthermore, we have $Q _ { t } ^ { \prime } ( s , a _ { 1 } ) = V _ { * } ( s )$ then the error is zero. The remaining action values $Q _ { t } ^ { \prime } ( s , a _ { i } )$ , for $i > 1$ , are arbitrary. □

Theorem 2. Consider a state s in which all the true optimal action values are equal at $Q _ { * } ( s , a ) = V _ { * } ( s )$ . Suppose that the estimation errors $Q _ { t } ( s , a ) - Q _ { * } ( s , a )$ ) are independently distributed uniformly randomly in $[ - 1 , 1 ] .$ . Then,

$$
\mathbb {E} \left[ \max _ {a} Q _ {t} (s, a) - V _ {*} (s) \right] = \frac {m - 1}{m + 1}
$$

Proof. Define $\epsilon _ { a } = Q _ { t } ( s , a ) - Q _ { * } ( s , a ) ;$ ; this is a uniform random variable in $[ - 1 , 1 ]$ . The probability that max $\alpha Q _ { t } ( s , a ) \leq x$ for some x is equal to the probability that $\epsilon _ { a } \leq x$ for all a simultaneously. Because the estimation errors are independent, we can derive

$$
\begin{array}{l} P (\max _ {a} \epsilon_ {a} \leq x) = P (X _ {1} \leq x \land X _ {2} \leq x \land \dots \land X _ {m} \leq x) \\ = \prod_ {a = 1} ^ {m} P (\epsilon_ {a} \leq x). \\ \end{array}
$$

The function $P ( \epsilon _ { a } \ \leq \ x )$ is the cumulative distribution function (CDF) of $\epsilon _ { a } ,$ which here is simply defined as

$$
P (\epsilon_ {a} \leq x) = \left\{ \begin{array}{l l} 0 & \text { if } x \leq - 1 \\ \frac {1 + x}{2} & \text { if } x \in (- 1, 1) \\ 1 & \text { if } x \geq 1 \end{array} \right.
$$

This implies that

$$
\begin{array}{l} P (\max _ {a} \epsilon_ {a} \leq x) = \prod_ {a = 1} ^ {m} P (\epsilon_ {a} \leq x) \\ = \left\{ \begin{array}{l l} 0 & \text {if x\leq - 1} \\ \left(\frac {1 + x}{2}\right) ^ {m} & \text {if x\in (-1,1)} \\ 1 & \text {if x\geq 1} \end{array} \right. \\ \end{array}
$$

This gives us the CDF of the random variable maxa $\epsilon _ { a } .$ . Its expectation can be written as an integral

$$
\mathbb {E} \left[ \max _ {a} \epsilon_ {a} \right] = \int_ {- 1} ^ {1} x f _ {\mathrm{max}} (x)   \mathrm{d} x  ,
$$

where fined $f _ { \mathrm { m a x } }$ is the probability densi derivative of the CDF: $\begin{array} { r } { \dot { f } _ { \mathrm { m a x } } ( x ) = \frac { \mathrm { d } } { \mathrm { d } x } P ( \operatorname* { m a x } _ { a } \epsilon _ { a } \le } \end{array}$ $x )$ , so that for $x \in [ - 1 , 1 ]$ we have $\begin{array} { r } { f _ { \mathrm { m a x } } ( x ) = \frac { m } { 2 } \left( \frac { 1 + x } { 2 } \right) ^ { m - 1 } } \end{array}$ m   1+x m−1. Evaluating the integral yields

$$
\begin{array}{l} \mathbb {E} \left[ \max _ {a} \epsilon_ {a} \right] = \int_ {- 1} ^ {1} x f _ {\max} (x)   \mathrm{d} x \\ = \left[ \left(\frac {x + 1}{2}\right) ^ {m} \frac {m x - 1}{m + 1} \right] _ {- 1} ^ {1} \\ = \frac {m - 1}{m + 1}. \\ \end{array}
$$

# Experimental Details for the Atari 2600 Domain

We selected the 49 games to match the list used by Mnih et al. (2015), see Tables below for the full list. Each agent step is composed of four frames (the last selected action is repeated during these frames) and reward values (obtained from the Arcade Learning Environment (Bellemare et al., 2013)) are clipped between -1 and 1.

# Network Architecture

The convolution network used in the experiment is exactly the one proposed by proposed by Mnih et al. (2015), we only provide details here for completeness. The input to the network is a 84x84x4 tensor containing a rescaled, and gray-scale, version of the last four frames. The first convolution layer convolves the input with 32 filters of size 8 (stride 4), the second layer has 64 layers of size 4 (stride 2), the final convolution layer has 64 filters of size 3 (stride 1). This is followed by a fully-connected hidden layer of 512 units. All these layers are separated by Rectifier Linear Units (ReLu). Finally, a fully-connected linear layer projects to the output of the network, i.e., the Q-values. The optimization employed to train the network is RMSProp (with momentum parameter 0.95).

# Hyper-parameters

In all experiments, the discount was set to $\gamma = 0 . 9 9$ , and the learning rate to $\alpha = 0 . 0 0 0 2 5$ . The number of steps between target network updates was $\tau = 1 0 , 0 0 0$ . Training is done over 50M steps (i.e., 200M frames). The agent is evaluated every 1M steps, and the best policy across these evaluations is kept as the output of the learning process. The size of the experience replay memory is 1M tuples. The memory gets sampled to update the network every 4 steps with minibatches of size 32. The simple exploration policy used is an -greedy policy with the  decreasing linearly from 1 to 0.1 over 1M steps.

# Supplementary Results in the Atari 2600 Domain

The Tables below provide further detailed results for our experiments in the Atari domain.

<table><tr><td>Game</td><td>Random</td><td>Human</td><td>DQN</td><td>Double DQN</td></tr><tr><td>Alien</td><td>227.80</td><td>6875.40</td><td>3069.33</td><td>2907.30</td></tr><tr><td>Amidar</td><td>5.80</td><td>1675.80</td><td>739.50</td><td>702.10</td></tr><tr><td>Assault</td><td>222.40</td><td>1496.40</td><td>3358.63</td><td>5022.90</td></tr><tr><td>Asterix</td><td>210.00</td><td>8503.30</td><td>6011.67</td><td>15150.00</td></tr><tr><td>Asteroids</td><td>719.10</td><td>13156.70</td><td>1629.33</td><td>930.60</td></tr><tr><td>Atlantis</td><td>12850.00</td><td>29028.10</td><td>85950.00</td><td>64758.00</td></tr><tr><td>Bank Heist</td><td>14.20</td><td>734.40</td><td>429.67</td><td>728.30</td></tr><tr><td>Battle Zone</td><td>2360.00</td><td>37800.00</td><td>26300.00</td><td>25730.00</td></tr><tr><td>Beam Rider</td><td>363.90</td><td>5774.70</td><td>6845.93</td><td>7654.00</td></tr><tr><td>Bowling</td><td>23.10</td><td>154.80</td><td>42.40</td><td>70.50</td></tr><tr><td>Boxing</td><td>0.10</td><td>4.30</td><td>71.83</td><td>81.70</td></tr><tr><td>Breakout</td><td>1.70</td><td>31.80</td><td>401.20</td><td>375.00</td></tr><tr><td>Centipede</td><td>2090.90</td><td>11963.20</td><td>8309.40</td><td>4139.40</td></tr><tr><td>Chopper Command</td><td>811.00</td><td>9881.80</td><td>6686.67</td><td>4653.00</td></tr><tr><td>Crazy Climber</td><td>10780.50</td><td>35410.50</td><td>114103.33</td><td>101874.00</td></tr><tr><td>Demon Attack</td><td>152.10</td><td>3401.30</td><td>9711.17</td><td>9711.90</td></tr><tr><td>Double Dunk</td><td>-18.60</td><td>-15.50</td><td>-18.07</td><td>-6.30</td></tr><tr><td>Enduro</td><td>0.00</td><td>309.60</td><td>301.77</td><td>319.50</td></tr><tr><td>Fishing Derby</td><td>-91.70</td><td>5.50</td><td>-0.80</td><td>20.30</td></tr><tr><td>Freeway</td><td>0.00</td><td>29.60</td><td>30.30</td><td>31.80</td></tr><tr><td>Frostbite</td><td>65.20</td><td>4334.70</td><td>328.33</td><td>241.50</td></tr><tr><td>Gopher</td><td>257.60</td><td>2321.00</td><td>8520.00</td><td>8215.40</td></tr><tr><td>Gravitar</td><td>173.00</td><td>2672.00</td><td>306.67</td><td>170.50</td></tr><tr><td>H.E.R.O.</td><td>1027.00</td><td>25762.50</td><td>19950.33</td><td>20357.00</td></tr><tr><td>Ice Hockey</td><td>-11.20</td><td>0.90</td><td>-1.60</td><td>-2.40</td></tr><tr><td>James Bond</td><td>29.00</td><td>406.70</td><td>576.67</td><td>438.00</td></tr><tr><td>Kangaroo</td><td>52.00</td><td>3035.00</td><td>6740.00</td><td>13651.00</td></tr><tr><td>Krull</td><td>1598.00</td><td>2394.60</td><td>3804.67</td><td>4396.70</td></tr><tr><td>Kung-Fu Master</td><td>258.50</td><td>22736.20</td><td>23270.00</td><td>29486.00</td></tr><tr><td>Montezuma&#x27;s Revenge</td><td>0.00</td><td>4366.70</td><td>0.00</td><td>0.00</td></tr><tr><td>Ms. Pacman</td><td>307.30</td><td>15693.40</td><td>2311.00</td><td>3210.00</td></tr><tr><td>Name This Game</td><td>2292.30</td><td>4076.20</td><td>7256.67</td><td>6997.10</td></tr><tr><td>Pong</td><td>-20.70</td><td>9.30</td><td>18.90</td><td>21.00</td></tr><tr><td>Private Eye</td><td>24.90</td><td>69571.30</td><td>1787.57</td><td>670.10</td></tr><tr><td>Q*Bert</td><td>163.90</td><td>13455.00</td><td>10595.83</td><td>14875.00</td></tr><tr><td>River Raid</td><td>1338.50</td><td>13513.30</td><td>8315.67</td><td>12015.30</td></tr><tr><td>Road Runner</td><td>11.50</td><td>7845.00</td><td>18256.67</td><td>48377.00</td></tr><tr><td>Robotank</td><td>2.20</td><td>11.90</td><td>51.57</td><td>46.70</td></tr><tr><td>Seaquest</td><td>68.40</td><td>20181.80</td><td>5286.00</td><td>7995.00</td></tr><tr><td>Space Invaders</td><td>148.00</td><td>1652.30</td><td>1975.50</td><td>3154.60</td></tr><tr><td>Star Gunner</td><td>664.00</td><td>10250.00</td><td>57996.67</td><td>65188.00</td></tr><tr><td>Tennis</td><td>-23.80</td><td>-8.90</td><td>-2.47</td><td>1.70</td></tr><tr><td>Time Pilot</td><td>3568.00</td><td>5925.00</td><td>5946.67</td><td>7964.00</td></tr><tr><td>Tutankham</td><td>11.40</td><td>167.60</td><td>186.70</td><td>190.60</td></tr><tr><td>Up and Down</td><td>533.40</td><td>9082.00</td><td>8456.33</td><td>16769.90</td></tr><tr><td>Venture</td><td>0.00</td><td>1187.50</td><td>380.00</td><td>93.00</td></tr><tr><td>Video Pinball</td><td>16256.90</td><td>17297.60</td><td>42684.07</td><td>70009.00</td></tr><tr><td>Wizard of Wor</td><td>563.50</td><td>4756.50</td><td>3393.33</td><td>5204.00</td></tr><tr><td>Zaxxon</td><td>32.50</td><td>9173.30</td><td>4976.67</td><td>10182.00</td></tr></table>

Table 3: Raw scores for the no-op evaluation condition (5 minutes emulator time). DQN as given by Mnih et al. (2015).

<table><tr><td>Game</td><td>DQN</td><td>Double DQN</td></tr><tr><td>Alien</td><td>42.75 %</td><td>40.31 %</td></tr><tr><td>Amidar</td><td>43.93 %</td><td>41.69 %</td></tr><tr><td>Assault</td><td>246.17 %</td><td>376.81 %</td></tr><tr><td>Asterix</td><td>69.96 %</td><td>180.15 %</td></tr><tr><td>Asteroids</td><td>7.32 %</td><td>1.70 %</td></tr><tr><td>Atlantis</td><td>451.85 %</td><td>320.85 %</td></tr><tr><td>Bank Heist</td><td>57.69 %</td><td>99.15 %</td></tr><tr><td>Battle Zone</td><td>67.55 %</td><td>65.94 %</td></tr><tr><td>Beam Rider</td><td>119.80 %</td><td>134.73 %</td></tr><tr><td>Bowling</td><td>14.65 %</td><td>35.99 %</td></tr><tr><td>Boxing</td><td>1707.86 %</td><td>1942.86 %</td></tr><tr><td>Breakout</td><td>1327.24 %</td><td>1240.20 %</td></tr><tr><td>Centipede</td><td>62.99 %</td><td>20.75 %</td></tr><tr><td>Chopper Command</td><td>64.78 %</td><td>42.36 %</td></tr><tr><td>Crazy Climber</td><td>419.50 %</td><td>369.85 %</td></tr><tr><td>Demon Attack</td><td>294.20 %</td><td>294.22 %</td></tr><tr><td>Double Dunk</td><td>17.10 %</td><td>396.77 %</td></tr><tr><td>Enduro</td><td>97.47 %</td><td>103.20 %</td></tr><tr><td>Fishing Derby</td><td>93.52 %</td><td>115.23 %</td></tr><tr><td>Freeway</td><td>102.36 %</td><td>107.43 %</td></tr><tr><td>Frostbite</td><td>6.16 %</td><td>4.13 %</td></tr><tr><td>Gopher</td><td>400.43 %</td><td>385.66 %</td></tr><tr><td>Gravitar</td><td>5.35 %</td><td>-0.10 %</td></tr><tr><td>H.E.R.O.</td><td>76.50 %</td><td>78.15 %</td></tr><tr><td>Ice Hockey</td><td>79.34 %</td><td>72.73 %</td></tr><tr><td>James Bond</td><td>145.00 %</td><td>108.29 %</td></tr><tr><td>Kangaroo</td><td>224.20 %</td><td>455.88 %</td></tr><tr><td>Krull</td><td>277.01 %</td><td>351.33 %</td></tr><tr><td>Kung-Fu Master</td><td>102.37 %</td><td>130.03 %</td></tr><tr><td>Montezuma&#x27;s Revenge</td><td>0.00 %</td><td>0.00 %</td></tr><tr><td>Ms. Pacman</td><td>13.02 %</td><td>18.87 %</td></tr><tr><td>Name This Game</td><td>278.29 %</td><td>263.74 %</td></tr><tr><td>Pong</td><td>132.00 %</td><td>139.00 %</td></tr><tr><td>Private Eye</td><td>2.53 %</td><td>0.93 %</td></tr><tr><td>Q*Bert</td><td>78.49 %</td><td>110.68 %</td></tr><tr><td>River Raid</td><td>57.31 %</td><td>87.70 %</td></tr><tr><td>Road Runner</td><td>232.91 %</td><td>617.42 %</td></tr><tr><td>Robotank</td><td>508.97 %</td><td>458.76 %</td></tr><tr><td>Seaquest</td><td>25.94 %</td><td>39.41 %</td></tr><tr><td>Space Invaders</td><td>121.49 %</td><td>199.87 %</td></tr><tr><td>Star Gunner</td><td>598.09 %</td><td>673.11 %</td></tr><tr><td>Tennis</td><td>143.15 %</td><td>171.14 %</td></tr><tr><td>Time Pilot</td><td>100.92 %</td><td>186.51 %</td></tr><tr><td>Tutankham</td><td>112.23 %</td><td>114.72 %</td></tr><tr><td>Up and Down</td><td>92.68 %</td><td>189.93 %</td></tr><tr><td>Venture</td><td>32.00 %</td><td>7.83 %</td></tr><tr><td>Video Pinball</td><td>2539.36 %</td><td>5164.99 %</td></tr><tr><td>Wizard of Wor</td><td>67.49 %</td><td>110.67 %</td></tr><tr><td>Zaxxon</td><td>54.09 %</td><td>111.04 %</td></tr></table>

Table 4: Normalized results for no-op evaluation condition (5 minutes emulator time).

<table><tr><td>Game</td><td>Random</td><td>Human</td><td>DQN</td><td>Double DQN</td><td>Double DQN (tuned)</td></tr><tr><td>Alien</td><td>128.30</td><td>6371.30</td><td>570.2</td><td>621.6</td><td>1033.4</td></tr><tr><td>Amidar</td><td>11.80</td><td>1540.40</td><td>133.4</td><td>188.2</td><td>169.1</td></tr><tr><td>Assault</td><td>166.90</td><td>628.90</td><td>3332.3</td><td>2774.3</td><td>6060.8</td></tr><tr><td>Asterix</td><td>164.50</td><td>7536.00</td><td>124.5</td><td>5285.0</td><td>16837.0</td></tr><tr><td>Asteroids</td><td>871.30</td><td>36517.30</td><td>697.1</td><td>1219.0</td><td>1193.2</td></tr><tr><td>Atlantis</td><td>13463.00</td><td>26575.00</td><td>76108.0</td><td>260556.0</td><td>319688.0</td></tr><tr><td>Bank Heist</td><td>21.70</td><td>644.50</td><td>176.3</td><td>469.8</td><td>886.0</td></tr><tr><td>Battle Zone</td><td>3560.00</td><td>33030.00</td><td>17560.0</td><td>25240.0</td><td>24740.0</td></tr><tr><td>Beam Rider</td><td>254.60</td><td>14961.00</td><td>8672.4</td><td>9107.9</td><td>17417.2</td></tr><tr><td>Berzerk</td><td>196.10</td><td>2237.50</td><td></td><td>635.8</td><td>1011.1</td></tr><tr><td>Bowling</td><td>35.20</td><td>146.50</td><td>41.2</td><td>62.3</td><td>69.6</td></tr><tr><td>Boxing</td><td>-1.50</td><td>9.60</td><td>25.8</td><td>52.1</td><td>73.5</td></tr><tr><td>Breakout</td><td>1.60</td><td>27.90</td><td>303.9</td><td>338.7</td><td>368.9</td></tr><tr><td>Centipede</td><td>1925.50</td><td>10321.90</td><td>3773.1</td><td>5166.6</td><td>3853.5</td></tr><tr><td>Chopper Command</td><td>644.00</td><td>8930.00</td><td>3046.0</td><td>2483.0</td><td>3495.0</td></tr><tr><td>Crazy Climber</td><td>9337.00</td><td>32667.00</td><td>50992.0</td><td>94315.0</td><td>113782.0</td></tr><tr><td>Defender</td><td>1965.50</td><td>14296.00</td><td></td><td>8531.0</td><td>27510.0</td></tr><tr><td>Demon Attack</td><td>208.30</td><td>3442.80</td><td>12835.2</td><td>13943.5</td><td>69803.4</td></tr><tr><td>Double Dunk</td><td>-16.00</td><td>-14.40</td><td>-21.6</td><td>-6.4</td><td>-0.3</td></tr><tr><td>Enduro</td><td>-81.80</td><td>740.20</td><td>475.6</td><td>475.9</td><td>1216.6</td></tr><tr><td>Fishing Derby</td><td>-77.10</td><td>5.10</td><td>-2.3</td><td>-3.4</td><td>3.2</td></tr><tr><td>Freeway</td><td>0.10</td><td>25.60</td><td>25.8</td><td>26.3</td><td>28.8</td></tr><tr><td>Frostbite</td><td>66.40</td><td>4202.80</td><td>157.4</td><td>258.3</td><td>1448.1</td></tr><tr><td>Gopher</td><td>250.00</td><td>2311.00</td><td>2731.8</td><td>8742.8</td><td>15253.0</td></tr><tr><td>Gravitar</td><td>245.50</td><td>3116.00</td><td>216.5</td><td>170.0</td><td>200.5</td></tr><tr><td>H.E.R.O.</td><td>1580.30</td><td>25839.40</td><td>12952.5</td><td>15341.4</td><td>14892.5</td></tr><tr><td>Ice Hockey</td><td>-9.70</td><td>0.50</td><td>-3.8</td><td>-3.6</td><td>-2.5</td></tr><tr><td>James Bond</td><td>33.50</td><td>368.50</td><td>348.5</td><td>416.0</td><td>573.0</td></tr><tr><td>Kangaroo</td><td>100.00</td><td>2739.00</td><td>2696.0</td><td>6138.0</td><td>11204.0</td></tr><tr><td>Krull</td><td>1151.90</td><td>2109.10</td><td>3864.0</td><td>6130.4</td><td>6796.1</td></tr><tr><td>Kung-Fu Master</td><td>304.00</td><td>20786.80</td><td>11875.0</td><td>22771.0</td><td>30207.0</td></tr><tr><td>Montezuma&#x27;s Revenge</td><td>25.00</td><td>4182.00</td><td>50.0</td><td>30.0</td><td>42.0</td></tr><tr><td>Ms. Pacman</td><td>197.80</td><td>15375.00</td><td>763.5</td><td>1401.8</td><td>1241.3</td></tr><tr><td>Name This Game</td><td>1747.80</td><td>6796.00</td><td>5439.9</td><td>7871.5</td><td>8960.3</td></tr><tr><td>Phoenix</td><td>1134.40</td><td>6686.20</td><td></td><td>10364.0</td><td>12366.5</td></tr><tr><td>Pit Fall</td><td>-348.80</td><td>5998.90</td><td></td><td>-432.9</td><td>-186.7</td></tr><tr><td>Pong</td><td>-18.00</td><td>15.50</td><td>16.2</td><td>17.7</td><td>19.1</td></tr><tr><td>Private Eye</td><td>662.80</td><td>64169.10</td><td>298.2</td><td>346.3</td><td>-575.5</td></tr><tr><td>Q*Bert</td><td>183.00</td><td>12085.00</td><td>4589.8</td><td>10713.3</td><td>11020.8</td></tr><tr><td>River Raid</td><td>588.30</td><td>14382.20</td><td>4065.3</td><td>6579.0</td><td>10838.4</td></tr><tr><td>Road Runner</td><td>200.00</td><td>6878.00</td><td>9264.0</td><td>43884.0</td><td>43156.0</td></tr><tr><td>Robotank</td><td>2.40</td><td>8.90</td><td>58.5</td><td>52.0</td><td>59.1</td></tr><tr><td>Seaquest</td><td>215.50</td><td>40425.80</td><td>2793.9</td><td>4199.4</td><td>14498.0</td></tr><tr><td>Skiing</td><td>-15287.40</td><td>-3686.60</td><td></td><td>-29404.3</td><td>-11490.4</td></tr><tr><td>Solaris</td><td>2047.20</td><td>11032.60</td><td></td><td>2166.8</td><td>810.0</td></tr><tr><td>Space Invaders</td><td>182.60</td><td>1464.90</td><td>1449.7</td><td>1495.7</td><td>2628.7</td></tr><tr><td>Star Gunner</td><td>697.00</td><td>9528.00</td><td>34081.0</td><td>53052.0</td><td>58365.0</td></tr><tr><td>Surround</td><td>-9.70</td><td>5.40</td><td></td><td>-7.6</td><td>1.9</td></tr><tr><td>Tennis</td><td>-21.40</td><td>-6.70</td><td>-2.3</td><td>11.0</td><td>-7.8</td></tr><tr><td>Time Pilot</td><td>3273.00</td><td>5650.00</td><td>5640.0</td><td>5375.0</td><td>6608.0</td></tr><tr><td>Tutankham</td><td>12.70</td><td>138.30</td><td>32.4</td><td>63.6</td><td>92.2</td></tr><tr><td>Up and Down</td><td>707.20</td><td>9896.10</td><td>3311.3</td><td>4721.1</td><td>19086.9</td></tr><tr><td>Venture</td><td>18.00</td><td>1039.00</td><td>54.0</td><td>75.0</td><td>21.0</td></tr><tr><td>Video Pinball</td><td>20452.0</td><td>15641.10</td><td>20228.1</td><td>148883.6</td><td>367823.7</td></tr><tr><td>Wizard of Wor</td><td>804.00</td><td>4556.00</td><td>246.0</td><td>155.0</td><td>6201.0</td></tr><tr><td>Yars Revenge</td><td>1476.90</td><td>47135.20</td><td></td><td>5439.5</td><td>6270.6</td></tr><tr><td>Zaxxon</td><td>475.00</td><td>8443.00</td><td>831.0</td><td>7874.0</td><td>8593.0</td></tr></table>

Table 5: Raw scores for the human start condition (30 minutes emulator time). DQN as given by Nair et al. (2015).

<table><tr><td>Game</td><td>DQN</td><td>Double DQN</td><td>Double DQN (tuned)</td></tr><tr><td>Alien</td><td>7.08%</td><td>7.90%</td><td>14.50%</td></tr><tr><td>Amidar</td><td>7.95%</td><td>11.54%</td><td>10.29%</td></tr><tr><td>Assault</td><td>685.15%</td><td>564.37%</td><td>1275.74%</td></tr><tr><td>Asterix</td><td>-0.54%</td><td>69.46%</td><td>226.18%</td></tr><tr><td>Asteroids</td><td>-0.49%</td><td>0.98%</td><td>0.90%</td></tr><tr><td>Atlantis</td><td>477.77%</td><td>1884.48%</td><td>2335.46%</td></tr><tr><td>Bank Heist</td><td>24.82%</td><td>71.95%</td><td>138.78%</td></tr><tr><td>Battle Zone</td><td>47.51%</td><td>73.57%</td><td>71.87%</td></tr><tr><td>Beam Rider</td><td>57.24%</td><td>60.20%</td><td>116.70%</td></tr><tr><td>Berzerk</td><td></td><td>21.54%</td><td>39.92%</td></tr><tr><td>Bowling</td><td>5.39%</td><td>24.35%</td><td>30.91%</td></tr><tr><td>Boxing</td><td>245.95%</td><td>482.88%</td><td>675.68%</td></tr><tr><td>Breakout</td><td>1149.43%</td><td>1281.75%</td><td>1396.58%</td></tr><tr><td>Centipede</td><td>22.00%</td><td>38.60%</td><td>22.96%</td></tr><tr><td>Chopper Command</td><td>28.99%</td><td>22.19%</td><td>34.41%</td></tr><tr><td>Crazy Climber</td><td>178.55%</td><td>364.24%</td><td>447.69%</td></tr><tr><td>Defender</td><td></td><td>53.25%</td><td>207.17%</td></tr><tr><td>Demon Attack</td><td>390.38%</td><td>424.65%</td><td>2151.65%</td></tr><tr><td>Double Dunk</td><td>-350.00%</td><td>600.00%</td><td>981.25%</td></tr><tr><td>Enduro</td><td>67.81%</td><td>67.85%</td><td>157.96%</td></tr><tr><td>Fishing Derby</td><td>91.00%</td><td>89.66%</td><td>97.69%</td></tr><tr><td>Freeway</td><td>100.78%</td><td>102.75%</td><td>112.55%</td></tr><tr><td>Frostbite</td><td>2.20%</td><td>4.64%</td><td>33.40%</td></tr><tr><td>Gopher</td><td>120.42%</td><td>412.07%</td><td>727.95%</td></tr><tr><td>Gravitar</td><td>-1.01%</td><td>-2.63%</td><td>-1.57%</td></tr><tr><td>H.E.R.O.</td><td>46.88%</td><td>56.73%</td><td>54.88%</td></tr><tr><td>Ice Hockey</td><td>57.84%</td><td>59.80%</td><td>70.59%</td></tr><tr><td>James Bond</td><td>94.03%</td><td>114.18%</td><td>161.04%</td></tr><tr><td>Kangaroo</td><td>98.37%</td><td>228.80%</td><td>420.77%</td></tr><tr><td>Krull</td><td>283.34%</td><td>520.11%</td><td>589.66%</td></tr><tr><td>Kung-Fu Master</td><td>56.49%</td><td>109.69%</td><td>145.99%</td></tr><tr><td>Montezuma&#x27;s Revenge</td><td>0.60%</td><td>0.12%</td><td>0.41%</td></tr><tr><td>Ms. Pacman</td><td>3.73%</td><td>7.93%</td><td>6.88%</td></tr><tr><td>Name This Game</td><td>73.14%</td><td>121.30%</td><td>142.87%</td></tr><tr><td>Phoenix</td><td></td><td>166.25%</td><td>202.31%</td></tr><tr><td>Pit Fall</td><td></td><td>-1.32%</td><td>2.55%</td></tr><tr><td>Pong</td><td>102.09%</td><td>106.57%</td><td>110.75%</td></tr><tr><td>Private Eye</td><td>-0.57%</td><td>-0.50%</td><td>-1.95%</td></tr><tr><td>Q*Bert</td><td>37.03%</td><td>88.48%</td><td>91.06%</td></tr><tr><td>River Raid</td><td>25.21%</td><td>43.43%</td><td>74.31%</td></tr><tr><td>Road Runner</td><td>135.73%</td><td>654.15%</td><td>643.25%</td></tr><tr><td>Robotank</td><td>863.08%</td><td>763.08%</td><td>872.31%</td></tr><tr><td>Seaquest</td><td>6.41%</td><td>9.91%</td><td>35.52%</td></tr><tr><td>Skiing</td><td></td><td>-121.69%</td><td>32.73%</td></tr><tr><td>Solaris</td><td></td><td>1.33%</td><td>-13.77%</td></tr><tr><td>Space Invaders</td><td>98.81%</td><td>102.40%</td><td>190.76%</td></tr><tr><td>Star Gunner</td><td>378.03%</td><td>592.85%</td><td>653.02%</td></tr><tr><td>Surround</td><td></td><td>13.91%</td><td>76.82%</td></tr><tr><td>Tennis</td><td>129.93%</td><td>220.41%</td><td>92.52%</td></tr><tr><td>Time Pilot</td><td>99.58%</td><td>88.43%</td><td>140.30%</td></tr><tr><td>Tutankham</td><td>15.68%</td><td>40.53%</td><td>63.30%</td></tr><tr><td>Up and Down</td><td>28.34%</td><td>43.68%</td><td>200.02%</td></tr><tr><td>Venture</td><td>3.53%</td><td>5.58%</td><td>0.29%</td></tr><tr><td>Video Pinball</td><td>-4.65%</td><td>2669.60%</td><td>7220.51%</td></tr><tr><td>Wizard of Wor</td><td>-14.87%</td><td>-17.30%</td><td>143.84%</td></tr><tr><td>Yars Revenge</td><td></td><td>8.68%</td><td>10.50%</td></tr><tr><td>Zaxxon</td><td>4.47%</td><td>92.86%</td><td>101.88%</td></tr></table>

Table 6: Normalized scores for the human start condition (30 minutes emulator time).