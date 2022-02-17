---
title: Lecture 04 (Jan 31, 2022)
classes: wide
excerpt: "Introduce AR(2) model and disucss the condition of weakly stationary for AR(1) and AR(2) models"
date: 2022-01-31
---


It is obvious that $\text{Cov}(x_{t-1},\epsilon_t) = 0$ because $\epsilon$ has mean zero. Thus, 

$$
\text{Var}(x_t) = \text{Var} ( \phi_1 x_{t-1} + \epsilon_t) = \phi_1^2 \text{Var}(x_{t-1}) + \text{Var}(\epsilon_t)
$$

due to the fact that  covariance between $x_{t-1}$ and $\epsilon_t$ is zero.  

Because the series is stationary, the variance is the same 

$$ \text{Var}(x_t) = \frac{\sigma^2}{1-\phi_1^2}$$

Summary: if $x_t$ is weakly stationary $AR(1)$ model then, 
$ |\phi_1| < 1.$ If $ | \phi_1 | < 1$ then $ \mathbb{E}(X_t) = \mu$. and 

$$
\text{Var}(x_t) = \sum_{i=0}^\infty \phi_1^{2i} \sigma^2
$$

The covariance 

$$
\gamma_l = \text{Cov}(x_t, x_{t-l}) = \sum_{i=0}^\infty \phi_1^i \phi_1^{i+l} \sigma^2<\infty
$$

Then $x_t$ is weakly stationary $AR(1)$ model. 

Thus,  $x_t$ is an $AR(1)$ model, $ \text{abs}(\phi_1) <1 $ if and only if $x_t$ is weakly stationary. 

Alternaltively, the covariance is 

$$
\begin{aligned}
\text{Cov} (x_t,\epsilon_t) &= \mathbb{E}[(x_t-\mu)\epsilon_t] \\
&= \mathbb{E}[ (\phi_1(x_{t-1}-\mu) + \epsilon_t )\epsilon_t] \\
&= \text{Var}(\epsilon_t) = \sigma^2
\end{aligned}
$$

Thus 

$$
\begin{aligned}
\gamma_l &= \text{Cov}(x_t, x_{t-l}) \\
&= \mathbb{E}[(x_t-\mu)(x_{t-l}-\mu)] \\
&= \phi_1 \gamma_{l-1} + \sigma^2 \mathbf{1}_{l=0}
\end{aligned}
$$

Thus we have a recursion for $\gamma_l$ :

$$
\gamma_0 = \frac{\sigma^2}{1-\phi^2_1} \quad \gamma_l = \phi_1\gamma_{l-1}
$$

For ACF, $\rho_0 =1$ and therefore, $\rho_l = \phi_1^l$. and this decays exponentially fast to zero for $AR(1)$ model. 

**$AR(2)$ model:** $x_t = \phi_0 + \phi_1 x_{t-1} + \phi_2 x_{t-2} +\epsilon_t$. 

By weakly stationary, 

$$
\mu = \mathbb{E}(x_t) = \phi_0 + \phi_1 \mu + \phi_2\mu \quad \Rightarrow \mu = \frac{\phi_0}{1-\phi_1-\phi_2}
$$

similarly to the above process for the $AR(1)$ model, we have the recursion 

$$
\left\{
\begin{aligned}
&\gamma_l = \phi_1 \gamma_{l-1} + \phi_2\gamma_{l-2} \\
&\rho_1 = \phi_1\rho_{l-1} + \phi_2\rho_{l-2}
\end{aligned}
\right.
$$

when $l=1$, we have 

$$
\begin{aligned}
&\rho_1 = \phi_1 + \phi_2 \rho_{-1} = \phi_1 + \phi_2 \rho_1 \\
&\Rightarrow \rho_1 = \frac{\phi_1}{1-\rho_2}
\end{aligned}
$$

If we define a shift operator $B$ such that $B \rho_l = \rho_{l-1}$, then we can rewrite the recursion 

$$
0= (1-\phi_1 B - \phi_2 B^2 ) \rho_l
$$

For $x_{1,2}$ as the two solutions of the polynomial $1- \phi_1x -\phi_2 x^2 = 0$. By some alebra, we can rewrite 

$$
(1-\frac{x}{x_1})(1-\frac{x}{x_2}) = 0
$$

Thus we can factorize as 

$$
(1-\omega_1 B) (1-\omega_2 B) \rho_l = 0
$$

This shows $AR(2)$ is almost a two $AR(1)$ model for the auto-correlation function. 

If we have complex solution, , then $\omega_{1,2}\in\mathbb{C}$. 

