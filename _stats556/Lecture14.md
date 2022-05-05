---
title: Lecture 14 (Feb 23, 2022)
classes: wide
excerpt: "Introduction to ARCH model"
date: 2022-02-23

---


Setup: $(x_t)$ serially uncorrelated but dependent. Let $\mathcal{F}_t$ be the information up to time $t$, i.e. $\mathcal{F}_t = \sigma(x_t,x_{t-1}, \dots)$ . Let $\mu_t = \mathbb{E}[x_t|\mathcal{F}_{t-1}]$ and $\sigma_t^2 = \text{Var}(x_t|\mathcal{F}_{t-1}) = \mathbb{E}[(x_t-\mu_t)^2|\mathcal{F}_{t-1}]$. 

### ARCH(p) model:

Focus on the residual: $r_t = x_t-\mu_t$. The Arch(p) process is 

$$
\begin{aligned}
&r_t = \sigma_t\epsilon_t \\
&\sigma_t^2 = \alpha_0 + \alpha_1 r_{t-1}^2 + \dots + \alpha_p r_{t-p}^2 
\end{aligned}
$$

 where $\epsilon_t$ Iid s.t. $\mathbb{E}[\epsilon_t] = 0$ and $\text{Var}(\epsilon_t) = 1$. 

properties:

1. $\mathbb{E}(r_t) = 0$ 
2. $\text{Var}(r_t) = \mathbb{E}[\mathbb{E}[r_t^2|\mathcal{F}_{t-1}]] = \mathbb{E}(\sigma_t^2 \mathbb{E}(\epsilon_t^2)) = \mathbb{E}(\alpha_0 + \alpha_1r_{t-1}^2 + \dots \alpha_p r_{t-p}^2)$ 

If $r_t$ is weakly stationary, then 
$$
\text{Var}(r_t) = \frac{\alpha_0}{1-\alpha_1-\dots -\alpha_p}
$$

3. $\mathbb{E}(r_tr_s) = 0 , \forall t\neq s$

4. If $\epsilon_t$ has finite fourth moment, then $\mathbb{E}[r_t^4] = \mathbb{E}[\mathbb{E}[\sigma_t^4\sigma_t^4 | \mathcal{F}_{t-1}]]$ if $\epsilon_t$ is normal, then $\mathbb{E}[r_t^4] = 3\mathbb{E}[\sigma_t^4]$.

   If we consider $p=1$, ARCH(1) model, then we could calculate $m_4\equiv \mathbb{E}[r_t^4]$. as 

   $$
   m_4 = 3\left[\alpha_0^2+\alpha_1^2m_4 + 2\alpha_0\alpha_1\frac{\alpha_0}{1-\alpha_1}\right]
   $$
   
   which shows that 
   
   $$
   m_4 = \frac{3\alpha_0^2(1+\alpha_1)}{(1-\alpha_1)(1-3\alpha_1^2)} \geq 0 \quad \Rightarrow 0\leq \alpha_1^2<\frac{1}{3}
   $$
   
   the uncoditional Kurtosis of $r_t$: 
   
   $$
   K:= \frac{\mathbb{E}[r_t^4]}{\text{Var}^2(r_t)} = \frac{2\alpha_0^2(1+\alpha_1)}{(1-\alpha_1)(1-3\alpha_1^2)} \times \frac{1-\alpha_1^2}{\alpha_0^2} = \frac{3(1-\alpha_1^2)}{1-3\alpha_1^2} > 3
   $$
   
   This shows the excessive kurtosis of $r_t$ is positive and thus the tail distribution of $r_t$ is heavier than $N(0,1)$. 

Remark: 

1. The $\sigma_t^2$ equation in ARCH model shows that eh positive and negative shocks $\pm \epsilon_t$ have the same effects on volaitility. 
2. $\alpha_1^2 < 1/3$ is needed to ensure the existence of fourth moment. 

### Estimation of ARCH(p) model. 

Recall $r_t = x_t - \mu_t = x_t - \mathbb{E}(x_t|\mathcal{F}_{t-1})$ . 

Auto regression with ARCH(p) error:
$$
\left\{\begin{aligned}
&x_t = \phi_0 + \phi_1 x_{t-1} + \dots \phi_kx_{t-k} + r_t \\
&r_t = \sigma_t \epsilon_t \\
&\epsilon_t^2 = \alpha_0 + \alpha_1 r_{t-1}^2 + \dots + \alpha_p r_{t-p}^2
\end{aligned}\right.
$$
Call this model as $AR(k)-ARCH(p)$ model , We want to estimate the parameters. $\phi_0, \phi_1,\dots, \phi_k,\alpha_0,\alpha_1,\dots,\alpha_p$. 

Notation in multiple regression:

$$
\begin{aligned}
&m_t = (1,x_{t-1},\dots, x_{t-k})^T \\
&\phi = (\phi_0,\phi_1,\dots,\phi_k)^T \\
&\alpha = (\alpha_0,\alpha_1,\dots,\alpha_p)^T
\end{aligned}
$$

Write AR(k)-ARCH(p) model as 

$$
x_t = m_t^T \phi + \sigma_t \epsilon_t 
$$

with 

$$
\sigma_t^2 = z_t(\phi)^T \alpha \quad\text{with } z_t(\phi) = (1,(x_{t-1} - m_{t-1}^T\phi)^2,\dots, (x_{t-p} - m_{t-p}^T\phi)^2 )^T
$$

Then we could use conditional MLE: conditioned on the first $\max(p,l)$ observations the conditional probability is f

$$
f(x_t|x_{t-1},x_{t-2},\dots) = \frac{1}{\sqrt{2\pi\sigma_t^2}}\exp\left[ - \frac{(x_t-m_t^T\phi)^2}{2\sigma_t^2}\right]
$$

where $\sigma_t^2 = z_t(\phi)^T\alpha$. The log likelihood function then becomes

$$
l(\phi,\alpha) = \sum_{t={p \vee k +1}}^T \left[-\frac{1}{2} \log (2\pi) - \frac{1}{2}\log\sigma_t^2 - \frac{(x_t-m_t^T\phi)^2}{2\sigma_t^2}\right]
$$

and we would maximize it with the constraint that 

$$
\sigma_t^2 = z_t(\phi)^t \alpha. 
$$

The gradient $\nabla l(\phi,\alpha)$ can be derivedd in closed form. 



