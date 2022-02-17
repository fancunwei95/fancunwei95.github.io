---
title: Lecture 07 (Feb 07, 2022)
classes: wide
excerpt: "Introduction to MA model and conditional loglikelihood maximization method. Introdcution to ARMA model"
date: 2022-02-07

---

The confidence interval for the PACF: the confidence interval for the coefficient, The null hypothesis is iid and thus the line is constant. 

**MA(q) model (Moving average model):**

Recall AR: $x_t = \phi_0 + \phi_1 x_{t-1} + \dots +\phi_q x_{t-q} + \epsilon_t$ 

$\epsilon_t$ iid mean-zero and $\text{var}(\epsilon_t)=\sigma^2$. 

MA(1) is a one-parameter family of $AR(\infty)$ model with $\phi_i = - \theta_1^i$ for $i\geq 1$. 

$$
x_t = \phi_0 - \theta_1 x_{t-1} - \theta_1^2 x_{t-2} -\dots 
$$

with $|\theta_1|<1$. 

This is equivalent to 

$$
x_t + \theta_1x_{t-1} + \theta_1^2 x_{t-2} + \dots  = \phi_0 + \epsilon_t
$$

For $x_{t-1}$, we have 

$$
x_{t-1} + \theta_1 x_{t-2} + \theta_1^2x_{t-3} + \dots = \phi_1 + \epsilon_{t-1}
$$

combine them, we find 

$$
\begin{aligned}
&x_t + \theta_1(\phi_1+\epsilon_{t-1}) = \phi_0 + \epsilon_t\\
&\Rightarrow x_t = (1-\theta_1)\phi_0 + \epsilon_t - \theta_1\epsilon_{t-1}
\end{aligned}
$$

Generally speaking, $MA(q)$ model becomes 

$$
\begin{aligned}
x_t &= c_0 + \epsilon_t - \theta_1\epsilon_{t-1} - \dots -\theta_q \epsilon_{t-q} \\
&=c_0 + (1-\theta_1B -\theta_2 B^2 -\dots -\theta_qB^q) \epsilon_t
\end{aligned}
$$

if $q<\infty$, the $x_t$ has finite memory.
This is stationary and thus, $E[x_t] = c_0 = (1-\theta_1)\phi_0$. 
By indpendence of $\epsilon_t$

$$
\text{Var}(x_t) = \sigma^2(1+\theta_1^2 + \dots+ \theta_q^2)
$$

Setting $c_0 = 0$, consider $MA(1)$, 

$$
x_t = \epsilon_t-\theta_1\epsilon_{t-1}
$$

Then 

$$
\gamma_l = \mathbb{E}(x_{t-l}x_t) = \mathbb(X_{t-l}\epsilon_t) - \theta_1 \mathbb{E}(x_{t-l} \epsilon_{t-1})
$$

The last term is $0$ if $l\geq 2$. when $l=1$, we find 

$$
\mathbb{E}(x_{t-1}\epsilon_{t-1}) = \mathbb{E}(\epsilon_{t-1}^2-\theta_2\epsilon_{t-2}\epsilon_{t-1}) = \sigma^2
$$

Thus, the ACF becomes 

$$
\rho_0 = 1,\quad \rho_1 = \frac{-\theta_1\sigma^2}{(1+\theta_1^2)\sigma^2} = -\frac{\theta_1}{1+\theta_1^2}
$$

Thus, ACF of MA(1) cuts off at lag $1$. 

For MA(2) models:

$$
\rho_0 = 1 \quad \rho_1 = \frac{-\theta_1 + \theta_1\theta_2}{1+\theta_1^2+\theta_2^2},\quad \rho_2 = -\frac{\theta_2}{1+\theta_1^2+\theta_2^2}
$$

**Estimation** : use MLE. 

for $MA(1)$, $x_t = c_0 +\epsilon_t -\theta_1\epsilon_{t-1}$. we have data $x_1,\dots, x_T$ and parameter to estimate $c_0, \theta, \sigma^2$. 

write down the joint likelihood function 

$$
\begin{aligned}
&l(c_0,\theta,\sigma^2|x_1,\dots x_T) \\
&=\log \prod_{i=1}^T \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{\epsilon_i^2}{2\sigma^2}\right)\\
&=-\frac{T}{2} \log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1^T}\left[ \sum_{j=1}^i\theta_1^j(x_{t-j}-c_0)\right]^2
\end{aligned}
$$

because

$$
\begin{aligned}
x_1 = c_0 + \epsilon_1 - \theta_1\epsilon_0\\
x_2 = c_0 + \epsilon_2 - \theta_1\epsilon_1
\end{aligned}
$$

We assume $\epsilon_t=0$ for $t\leq0$  and this is conditional log likelihood. 

This shows $\epsilon_2 = x_2 -c_0 + \theta_1\epsilon_1 = (x_2-c_0) + \theta_1(x_1-c_0)$ . recursively, we find 

$$
\begin{aligned}
\epsilon_t &= (x_t-c_0) + \theta_1\epsilon_{t-1}\\
&=(x_t-c_0) + \theta_1(x_{t-1}-c_0) + \theta_1^2(x_{t-2}-c_0)+\dots +\theta_1^{t-1} (x_1-c_0)
\end{aligned}
$$

The exact likelihood method whould treat $\epsilon_{t}$ for $t\leq 0$ as unknow. Using asymptotic behaviour instead of the second derivative of the loglikelihood for the confidence interval. 

**ARMA Model**

ARMA(1,1) model: $x_t - \phi_1x_{t-1} =  \phi_0 + \epsilon_t - \theta_1\epsilon_{t-1}$. Here $\epsilon_t$ iid white noise. 

need $\phi_1\neq \theta_1$. If they are the same, then we have $\epsilon_t -\epsilon_t = \phi_0 + \phi_1(x_{t-1}-\epsilon_{t-1})$.  This means we can solve $x_t-\epsilon_t$ in terms of $x_0$ and $\epsilon_0$. Also, $\epsilon_t$ are independent. This shows $x_t$ does not have time serieal structure. 


