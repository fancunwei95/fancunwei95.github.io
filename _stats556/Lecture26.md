---
title: Lecture 26 (March 30, 2022)
classes: wide
excerpt: "Diffusion Processes with Jumps"
date: 2022-03-30

---

### Jump Diffusion Model

Idea: model jumps by a Poisson process

Def: Given a time $t$, let $x_t$ be the number of events occuring during the time period $[0,t]$, Then, $x_t$ is a Poisson process if $X_t \sim \text{Poisson}(\lambda t)$. i.e. 

$$
P(x_t = k ) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}
$$

where $\lambda >0$ constant rate parameter. 

Assume $(x_t)$ Follows:

1. number of events occuring in non-overlapping intervals are independent. 
2. events occur at a constant rate of $\lambda$ per unit time interval
3. events cannot occur simultaneously

Divide the time interval $[0,t]$ by $n$ pieces. Let $x_t$ be the number of events occuring in time $t$ units. Fix $t>0$, Let $Y_i $ be the number of events to occur in the $i$-th bin, $i=1,\dots,n$. 

$$
Y_i \sim \text{Ber}(\lambda \frac{t}{n})
$$

Then, 

$$
X_t = \sum_{i=1}^n Y_i \sim \text{Binomial}(n, \frac{\lambda t}{n})
$$

Fix $k$, we can get 

$$
\begin{aligned}
P(X_t = k) &= {n\choose k}\left(\frac{\lambda t}{n} \right)^k \left(1 - \frac{\lambda t}{n}\right)^{n-k} \\
&=\frac{n!}{k!(n-k)!}\left(\frac{\lambda t}{n}\right)^k \left(1- \frac{\lambda t}{n}\right)^n \left(1 - \frac{\lambda t}{n}\right)^{-k} \\
&\rightarrow \frac{(\lambda t)^k}{k!} e^{-\lambda t} 
\end{aligned}
$$

This is the logic of Poisson process. 

Let $p_t$  be the price  of an asset at time $t$, previously , we modeled 

$$
dP_t = \mu P_t dt + \sigma P_t dw_t
$$

we now have 

$$
\frac{dP_t}{P_t} = \mu dt + \sigma dW_t + d \left[\sum_{i=1}^{n_t} (J_i-1) \right]
$$

where 

$$
\begin{aligned}
&W_t \text{ is the standard BM} \\
&n_t  \text{ is the Poisson process with rate parameter  } \lambda \\
&J_i \text{ is the sequence of iid non-negative r.v.}
\end{aligned}
$$

$J_i$ is the random variable that $X_i = \log (J_i)\sim \text{Laplace} (\kappa ,\eta)$ 

that is 

$$
X - \kappa  = \left\{\begin{aligned} &\xi \quad \text{ with prob }\frac{1}{2}\\
&-\xi \quad \text{ with prob }\frac{1}{2}
\end{aligned}\right.
$$

with $\xi\sim \text{Exp}(\eta)$.  with $\mathbb{E}[\xi] = \eta$ and $\text{Var}[\xi] = \eta^2$

Let $t_i$ be the time of the $i$-th jump, $i=1,\dots, n_t$, 

$$
P_{t_1^{-}}= P_0 \exp\left[(\mu-\frac{\sigma^2}{2})t + \sigma w_t \right]
$$

Then 

$$
P_{t_1} = P_{t_1^{-}} + (J_1-1) P_{t_1^-} = J_1 P_{t_1^-}
$$

At $t_2$, we have 

$$
P_{t_2^{-}} = P_{t_1} \exp\left[ (\mu-\frac{\sigma^2}{2})(t_2-t_1) + \sigma(w_{t_2}-w_{t_1}) \right]
$$

and 

$$
\begin{aligned}
P_{t_2} &= P_{t_1^-} + (J_2-1) P_{t_2}^- = J_2 P_{t_2}^- \\
&= J_2 P_{t_1} \exp\left[(\mu-\frac{\sigma^2}{2})(t_2-t_1) + \sigma (w_{t_2}-w_{t_1}) \right]\\
&= J_2J_1 P_0 \exp\left[ (\mu-\frac{\sigma^2}{2})t_1 + \sigma W_{t_1} \right] \exp \left[(\mu-\frac{\sigma^2}{2})(t_2-t_1) + \sigma (w_{t_2}-w_{t_1}) \right]\\
&= J_2J_1 P_0 \exp \left[(\mu-\frac{\sigma^2}{2})t_2 + \sigma w_{t_2} \right]
\end{aligned}
$$

This shows that in general, 

$$
P_t = P_0 \exp\left[ (\mu-\frac{\sigma^2}{2})t + \sigma w_t\right] \prod_{i=1}^{n_t} J_i
$$

For small $\Delta t$, 

$$
\begin{aligned}
\frac{P_{t+\Delta t} - P_t}{P_t} &= \frac{P_{t+\Delta t}}{P_t} -1  \\
&=\exp\left[ (\mu-\frac{\sigma^2}{2})\Delta t + \sigma (W_{t+\Delta t} - W_t) \right]\left[\prod_{n_t}^{n_{t+\Delta t}} J_i \right] - 1
\end{aligned}
$$

Note that $X_i = \log J_i$, 

$$
\begin{aligned}
\frac{P_{t+\Delta t} - P_t}{P_t} &= \exp \left[(\mu-\frac{\sigma^2}{2})\Delta t + \sigma (W_{t+\Delta t} -W_t) + \sum_{n_t}^{n_{t+\Delta t}} X_i  \right]-1 \\
&\approx \left[(\mu - \frac{\sigma^2}{2})\Delta t + \sigma \Delta W_t + \sum_{n_t}^{n_{t+\Delta t}} X_i \right] + \frac{1}{2}\sigma^2 \Delta t \\
&= \mu \Delta t  + \sigma \sqrt{\Delta t} \epsilon_t + \sum_{n_t}^{n_{t+\Delta t}} X_i
\end{aligned}
$$


