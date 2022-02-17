---
title: Lecture 03 (Jan 26, 2022)
classes: wide
excerpt: "Some introduction of AR model and linear model covariance calculation."
date: 2022-01-26
---

### Autoregression Moldes (AR)

General linear time series is 

$$
x_t = \mu + \sum_{i=0}^\infty \psi_i \epsilon_i
$$

for white noise $\epsilon$. 

Assum $(x_t)$ is stationary. This means the variance $\text{Var}(x_t)<\infty$ . $\mathbb{E}x_t = \mu$. The variance is 

$$
\gamma_0 = \text{Var}(x_t) = \sum_{i=0}^\infty \psi_i^2 \sigma^2
$$

In order for the series to converge by staitonary requirements, need $\psi_i$ to decay sufficiently fast. 

$$
\begin{aligned}
\gamma_l &= \text{Cov}(x_t, x_{t-l})\\
&= \mathbb{E}[\sum_{i=0}^\infty \psi_i \epsilon_{t-1} \sum_{j=0}^\infty \psi_j (\epsilon_{t-l-j})] \\
&= \sum_{i=0}^\infty \sum_{j=0}^\infty \psi_i\psi_j \mathbb{E}(\epsilon_{t-i}\epsilon_{t-l-j})
\end{aligned}
$$

$\mathbb{E}(\epsilon_{t-i}\epsilon_{t-l-j}) = \sigma^2 \delta(i,l+j)$. This means 

$$
\gamma_l = \sum_{j=0}^\infty \psi_{l+j}\psi_j \sigma^2
$$

This means 

$$
\rho_l = \frac{\gamma_l}{\gamma_0} = \frac{\sum_{j=0}^\infty \psi_j \psi_{j+l}}{\sum_{j=0}^\infty \psi_j^2}
$$

$AR(1)$ Model:

$$
x_t = \phi_0 + \phi_1x_{t-1} + \epsilon_t 
$$

Assum $X_t = \phi_0 + \phi_1 x_{t-1} + \epsilon_t$ is stationary, then 

$$
\mu = \mathbb{E}(x_t) = \phi_0 + \mathbb{E}(x_{t-1}) =  \phi_0 + \phi_1 \mu  \quad 
$$

This means 

$$
\mu = \frac{\phi_0}{1-\phi_1}
$$

Assum $\phi_1\neq 1$ since this case is just random walk. If we have non zero mean, we can rewrite the $AR(1)$ term as 

$$
\begin{aligned}
&x_t = (1-\phi_1) \mu + \phi_1 x_{t-1} + \epsilon_t \\
&x_{t} - \mu = \phi_1(x_{t-1} - \mu) +\epsilon_t
\end{aligned}
$$

This is the debiasing procedure. Wite recursively:

$$
\begin{aligned}
x_t- \mu &= \phi_1(x_{t-1} - \mu) + \epsilon_t \\
&= \phi_1^2(x_{t-2} - \mu) + \phi_1\epsilon_{t-1} + \epsilon_t \\
&= \phi_1^3(x_{t-3}-\mu) + \phi_1^2\epsilon_{t-2} + \phi_1\epsilon_{t-1} + \epsilon_t
\end{aligned}
$$

This reduces to 

$$
x_t = \sum_{i=0}^\infty \phi_1^i \epsilon_{t-i}
$$

AR(1) model is then a linear time series model. 

