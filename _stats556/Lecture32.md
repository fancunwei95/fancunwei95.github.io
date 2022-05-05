---
title: Lecture 32 (April 13, 2022)
classes: wide
excerpt: "Continuation of the discussion of Kalman Filter"
date: 2022-04-13

---

Given the observation, $(y_1, \dots, y_T; x_1,\dots, x_T)$ estimate the unknown parameters $(F, A, H, Q, R)$. 

Idea: Sequentially updating a (linear) projection of the dynamical system (Kalman Filter)

Recall: 

$$
\begin{aligned}
&\xi_{t+1} = F\xi_t + V_{t+1} \\
&y_t = A^T x_t + H^T\xi_t + W_t
\end{aligned}
$$

At each time step, recursively compute the optimal linear predicted value of $\xi_{t+1}$ based on the data observed up to time point $t$, i.e. 

given $D_t = (y_t,\dots, y_1; x_t,\dots, x_1)$  predict 

$$
\hat{\xi}_{t+1|t} = \mathbb{E}(\xi_{t+1}|D_t)
$$

The MSE matrix 

$$
P_{t+1|t} = \mathbb{E}(\hat\xi_{t+1|t} - \xi_{t+1}) (\hat\xi_{t+1|t} - \xi_{t+1})^T
$$

Initialization: $\xi_{1\|0} = \mathbb{E}(\xi_1 \| D_0) $  $= \mathbb{E}[\xi_1]$ where $D_0$ means there is no data. The expected MSE is 

$$
P_{1|0} = \mathbb{E}(\mathbb{E}\xi_1-\xi_1) (\mathbb{E}\xi_1-\xi)^T = \text{Cov}(\xi_1)
$$

Recursion: Given $\hat\xi_{t | t-1}$ and $ P_{t|t-1}$ and data $D_t = D_{t-1} \cup \{y_t,x_t\}$ compute $\xi_{t|t-1}$ and $P_{t+1|t}$.

Note $\mathbb{E} (\xi_t | x_t, D_{t-1}) = \mathbb{E} (\xi_t |D_{t-1}) = \xi_{t|t-1}$. 

(i) Predict the value of $y_t$:

$$
\begin{aligned}
\hat{y}_{t|t-1 } &=\hat{\mathbb{E}}(y_t|x_t, D_{t-1})\\
&= \hat{\mathbb{E}} (A^T x_t + H^T \xi_t + W_t | x_t, D_{t-1}) \\
&=A^T x_t + H^T \hat\xi_{t|t-1} + \mathbb{E} (w_t | x_t, D_{t-1} ) \\
&= A^T x_t + H^T \hat\xi_{t|t-1}
\end{aligned}
$$

MSE matrix: 

$$
\begin{aligned}
&\mathbb{E}(y_t - y_{t|t-1})(y_t - \hat y_{t|t-1}) ^T \\
&=H^T \mathbb{E}(\xi_t - \hat\xi_{t|t-1})(\xi_t-\hat\xi_{t|t-1})^T H + \mathbb{E}w_tw_t^T \\
&= H^T P_{t+1|t} H + R
\end{aligned}
$$

(ii) update the inference about $\xi_t$ with new observation $y_t$. compute 

$$
\hat\xi_{t+1|t} = \mathbb{E} (\xi_t | y_t ,x_t , D_{t-1}) 
$$

optimal prediction:

$$
\hat\xi_{t+1|t} = \hat\xi_{t|t-1} + [\mathbb{E}(\xi_t - \hat\xi_{t|t-1}) (y_t -\hat y_{t|t-1})^T] \times [\mathbb{E}[y_t-\hat y_{t|t-1}][y_t-\hat y_{t|t-1}]]^{-1} (y_t-\hat y_{t|t-1})
$$

The term 

$$
\mathbb{E}(\xi-\hat\xi_{t|t-1}) (y_t - \hat y_{t|t-1})^T = P_{t|t-1} H
$$

This then becomes that 

$$
\hat\xi_{t | t} = \hat\xi_{t|t-1} + P_{t|t-1} H(H^T P_{t+1|t} H + R)^{-1} [y_t - A^T x_t - H^T\hat\xi_{t|t-1}]
$$

and 

$$
\begin{aligned}
&P_{t|t} = \mathbb{E}(\hat\xi_{t|t} - \xi) (\hat\xi_{t|t} - \xi_t)^T \\
&= P_{t|t-1} - P_{t|t-1} H (H^T P_{t|t-1} H +R)^{-1} H^TP_{t|t-1}
\end{aligned}
$$

(iii) predict $\xi_{t+1|t}$, 

$$
\hat\xi_{t+1} = \mathbb{E} (\xi_{t+1}|D_t) = \mathbb{E}(F\xi_t+V_{t+1} |D_t) = F\hat\xi_{t|t}
$$

combining we could have 

$$
\hat\xi_{t+1|t} = F\hat\xi_{t|t-1} + FP_{t|t-1} H(H^T P_{t+1|t} H + R)^{-1}[y_t - A^T x_t - H^T \hat\xi_{t|t-1}] 
$$

the second term is called the Kalman gain. 
and 

$$
P_{t+1|t} = \mathbb{E}(\xi_{t+1}-\hat\xi_{t+1|t}) (\xi_{t+1}-\hat\xi_{t+1|t})^T = FP_{t|t} F^T +Q 
$$

Or 

$$
P_{t+1|t} = F[P_{t|t-1} - P_{t|t-1} H (H^T P_{t|t-1} H + R)^{-1}H^T P_{t|t-1} ] F^T +Q
$$

the two updating equations are the Kalman Filter. 

