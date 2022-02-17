---
title: Lecture 08 (Feb 09, 2022)
classes: wide
excerpt: "Introduction to ARMA model and its AR and MA representation"
date: 2022-02-07

---
**The $ARMA(1,1)$ model**
properties: $\mathbb{E}[x_t] - \phi_1\mathbb{E}[x_{t-1}] = \phi_0$. This shows 

$$
\mu = \mathbb{E}(x_t) = \frac{\phi_0}{1-\phi_1}
$$

which is the same as the AR(1) model. 

For second order, assume $\phi_0 = 0$, we find 

$$
\begin{aligned}
&\mathbb{E}(\epsilon_t(x_t-\phi_1x_{t-1})) = \mathbb{E}(\epsilon_t (\epsilon_t-\theta_1\epsilon_{t-1})) = \mathbb{E}(\epsilon_t^2) = \sigma^2 \\
&\Rightarrow \mathbb{E}\epsilon_t x_t = \sigma^2
\end{aligned}
$$

The varaince is 

$$
\begin{aligned}
\text{Var}(x_t) &= \text{Var}(\epsilon_t -\theta_1\epsilon_{t-1} + \phi_1x_{t-1})\\
&= \text{Var}(\epsilon_t) + \text{Var}(\phi_1x_{t-1}-\theta_1\epsilon_{t-1}) \\
&=\sigma^2 + \phi_1^2\text{Var}(x_{t-1}) + \theta_1\sigma^2  - 2\phi_1\theta_1\text{Cov}(x_{t-1},\epsilon_{t-1})
\end{aligned}
$$

since $\text{Cov}(x_{t-1},\epsilon_{t-1})$ is $1$, we have 

$$
\text{Var}(x_t) = \frac{\sigma^2(1+\theta_1^2-2\phi_1\theta_1)}{1-\phi_1^2}
$$

TO get $\gamma_l$, $l\geq 1$, compute 

$$
\mathbb{E}(x_{t-l} (x_t - \phi_1x_{t-1})) = E[x_{t-l}(\epsilon_t-\theta_1\epsilon_{t-1})] 
$$

This becomes 

$$
\begin{aligned}
\gamma_l - \phi_1\gamma_{l-1} = - \theta_1\mathbb{E}x_{t-l}\epsilon_{t-1}
\end{aligned}
$$

for $l=1$, the equation is 

$$
\gamma_1 - \phi_1\gamma_0 = - \theta_1\sigma^2
$$

for $l\geq 2$, we have 

$$
\gamma_l = \phi_1\gamma_{l-1}
$$

thus, ACF is 

$$
\rho_0 = 1,\quad  \rho_1 = \frac{\theta_1\gamma_0 - \theta_1\sigma^2}{\gamma_0}, \quad \rho_l = \phi_1\rho_{l-1}
$$

The ACF does not cut off at any finite order.

Rmk: PACF of ARMA(1,1) also does not cutoff at any finite leg. 

**General, $ARMA(p,q)$ model:**

$$
x_t - \sum_{i=1}^p\phi_ix_{t-i} = \phi_0 +\sum_{j=1}^q \theta_j\epsilon_{t-j}
$$

Write as 

$$
(1-\phi_1B-\phi_2B^2-\dots - \phi_pB^2) x_t = \phi_0 + (1-\theta_1B - \theta_2B^2 -\dots \theta_qB^q)\epsilon_t
$$

abbrieviately, we write 

$$
\phi(B) x_t = \phi_0 + \theta(B)\epsilon_t
$$

The two polynomials, $\theta(B)$ and $\phi(B)$ need to not have **common factors**. otherwise, the order $(p,q)$ of the model can be reduced. The MA part of the ARMA model does not affect the staitonarity of the model. thus, the stationary condition of $ARMA(p,q)$ should be the same as $AR(p)$ model. 

We can divide $\phi(B)$ on both sides to get an $MA$ representation of the $ARMA$ model. 

$$
\frac{\theta(B)}{\phi(B)} = \psi(B) = 1 + \psi_1 B + \psi_2 B^2 +\dots 
$$

we can also get the $AR$ representation by dividing $\theta(B)$ on both sides

$$
\frac{\phi(B)}{\theta(B)} = \pi(B) = 1- \pi_1B -\pi_2B - \dots
$$

For example for $ARMA(1,1)$, $\phi(B) = 1-\phi_1B$ and $\theta(B) = 1-\theta_1B$, 

$$
\begin{aligned}
&\frac{\theta(B)}{\phi(B)} = \frac{1-\theta_1B}{1-\phi_1B} = \frac{1-\phi_1B + \phi_1B - \theta_1B}{1-\phi_1B} \\
&=1+ \frac{(\phi_1-\theta_1)B}{1-\phi_1B} \\
&=1 + (\phi_1-\theta_1)B\frac{1-\phi_1B+\phi_1B}{1-\phi_1B} \\
&=1 + (\phi_1-\theta_1)B + (\phi_1-\theta_1)\phi_1 B^2\frac{1}{1-\phi_1B} \\
&=1 + (\phi_1-\theta_1)B + (\phi_1-\theta_1)\phi_1B^2 + (\phi_1-\theta_1)\phi_1^2B^3 + \dots
\end{aligned}
$$

Thus, $\psi_1 = \phi_1-\theta_1$, $\psi_2 = (\phi_1-\theta_1)\phi_1$, $\psi_3 = (\phi_1-\theta_1)\phi_1^2, \dots$. 

Similarly, 

$$
\pi(B) = \frac{1-\phi_1B}{1-\theta_1B} = 1 - (\theta_1-\phi_1)B - \theta_1(\theta_1-\phi_1)B^2 - \dots
$$

We can write the $ARMA(p,q)$ model as $AR(\infty)$ and $MA(\infty)$. 

$$
\begin{aligned}
&\frac{\phi(B)}{\theta(B)} x_t = \frac{\phi_0}{\theta(B)} + \epsilon_t\\
&\pi(B)x_t = \frac{\phi_0}{1-\theta_1-\theta_2-\dots } + \epsilon_t
\end{aligned}
$$

where $\phi_0/\theta(B) = x$ for some constant $x$ but $B x = x$ for the constant $x$, we thus $\phi_0 = (1-\theta_1-\theta_2-\dots )x$ and we get $x$ as the first term above. In the AR representation, need $\pi_i\rightarrow 0 $ for $i\rightarrow\infty$. This means $ARMA(p,q)$ is invertible. 

We can also write the $ARMA(p,q)$ to $MA(\infty)$. 

$$
\begin{aligned}
x_t &= \frac{\phi_0}{1-\phi_1-\phi_2-\dots} + \frac{\theta(B)}{\phi(B)} \epsilon_t\\
&=\frac{\phi_0}{1-\phi_1-\phi_2-\dots} + \epsilon_t + \psi_1\epsilon_{t-1}+\psi_2\epsilon_{t-2} + \dots
\end{aligned}
$$


