---
title: Lecture 02 (Jan 24, 2022)
classes: wide
excerpt: "Calculate the variance and convergence rates for autocorrelation sample estimator by central limit theorem. Introduce statistical tests for ACF."
date: 2022-01-24
---


Reminder: 

**Def [ lag -l  sample autocorrelation]** is 

$$
\hat{\rho} = \frac{\sum_{t=l+1}^T (x_t - \bar{x})(x_{t-l}-\bar{x})}{\sum_{t=1}^T (x_t-\bar{x})^2}
$$

consider two case:

- Case (i): if $(x_t)$ are iid st. $\text{Var}(x_t) =\sigma^2$ and $\mathbb{E}[x_t^4] < \infty$. then
  
  $$
  \sqrt{T} \hat{\rho} = \frac{\frac{1}{\sqrt{T}}\sum_{l+1}^T (x_t - \bar{x})(x_{t+l}-\bar{x})}{\frac{1}{T}\sum_{t=1}^T(x_t-\bar{x})^2}
  $$
  
  replace $\bar{x}$ by $\mu$ because $x-\bar{x} = (x-\mu + \mu-\bar{x})$  and $\mu-\bar{x}$ is of higher order. 

  Thus, 
  
  $$
  \sqrt{T}\hat{\rho} = \frac{\frac{1}{\sqrt{T}}\sum_{t=l+1}^T(x_t-\mu)(x_{t-l}-\mu)}{\frac{1}{T}\sum_{t=1}^T (x_t-\mu)^2}
  $$
  
  The denominator is $\frac{1}{T}\sum_{t=1}^T (x_t-\mu)^2$ converges to $\mathbb{E}(x_t-\mu)^2=\sigma^2$ . 

  Treat $y_t^{(l)} = (x_t-\mu)(x_{t-l}-\mu)$ and it is an $l$-dependent sequence with $\mathbb{E}y_{t}^{(l)}=0$. Then by central limit theorem,  
  
  $$
  \frac{1}{\sqrt{T}} \sum_{t=l+1}^T y_t^{(l)} \rightarrow \mathcal{N}(0,\tau^2)
  $$
  
  with 
  
  $$
  \tau^2 =\gamma_0 + 2\gamma_1 + \dots + 2\gamma_l
  $$
  
  because $y^{(l)}$ is an $l$-dependent sequence. Then 
  
  $$
  \begin{aligned}
  \gamma_m &= \text{Cov}(y_t^{(l)},y_{t+m}^{(l)}) \\
  &= \text{Cov} (x_t-\mu)(x_{t-l}-\mu) (x_{t+m}-\mu)(x_{t+m-l}-\mu)
  \end{aligned}
  $$

  if $m\geq 1$ if $l\neq m$ $\gamma_m=0$. if $l=m$ 
  
  $$
  \gamma_m = \mathbb{E}[(x_t-\mu)^2(x_{t-l}-\mu)(x_{{t+l}}-\mu)] = 0
  $$
  
  Thus, 
  
  $$
  \begin{aligned}
  \tau^2 &= \gamma_0 = \text{Var}(y_t) = \mathbb{E}[y_t^2] \\
  &=\mathbb{E}[(x_t-\mu)^2(x_{t-l}-\mu)^2] \\
  &= \mathbb{E}[(x_t-\mu)^2] \mathbb{E}[(x_{t-l}-\mu)^2]=\sigma^2
  \end{aligned}
  $$
  
  Thus, since the numerator is $\sigma^2$. 
  
  $$
  \sqrt{T}\hat{\rho}\rightarrow \mathcal{N}(0,1)
  $$
  

- Case(ii) $(x_t)$ is a linear time series. 
  
  $$
  x_t = \mu + \epsilon_1 + \psi_1\epsilon_{t-1} + \dots + \psi_{q}\epsilon_{t-q}
  $$
  
  where $\epsilon_t$ are iid with mean zero and $\mathbb{E}[\epsilon^4]<\infty$ with $\psi_0=1$. Then 
  
  $$
  \sqrt{T}\hat{\rho}_l \rightarrow \mathcal{N}(0,\tau^2)
  $$
  
  where 
  
  $$
  \tau^2 = 1 + 2\sum_{i=1}^q \rho_i^2 \quad \text{ for all } l>q
  $$
  
  **Remark** The asymptotic variance only depends on the second moments and no fourth moments show up. This is because the series is linear. 

  General formula when $(x_t)$ is linear time series for $l\geq 1$. 
  
  $$
  \sqrt{T} (\hat{\rho}_l - \rho_l) \rightarrow \mathcal{N}(0,\tau^2)
  $$
  
  where 
  
  $$
  \tau^2 = \sum_{h=1}^\infty (\rho_{h+l}+\rho_{h-l} - 2\rho_h\rho_l)^2
  $$
  
  this is called **Bartlett's formula**. 

  for lag $l>q$, 
  
  $$
  \begin{aligned}
  \tau^2 &= \sum_{h=1}^\infty (\rho_{h+l} + \rho_{h-l} - 2\rho_h\rho_l) \\
  &= \sum_{h=1}^\infty \rho_{h-l}^2 \\
  &= \rho_{l-1}^2 + \rho_{l-2}^2 + \dots + \rho_0^2 + \rho_{-1}^2 + \dots \\
  &= \rho_{q}^2 + \dots + \rho_1^2+\rho_0^2+\rho_{-1}^2+ \dots + \rho_{-q}^2 \\
  &= 1 + 2\sum_{i=1}^q \rho_i^2
  \end{aligned}
  $$

### Testing for ACF

- **inidividual test:** given $l\geq 1$, test $H_0 : \rho_l = 0$  vs $H_1: \rho_l \neq 0$, 
  
  $$
  \frac{\sqrt{T}\hat{\rho}_l}{\tau} \rightarrow \mathcal{N}(0,1)
  $$
  
  Here 
  
  $$
  \tau = \frac{1}{T} \left(1+2\sum_{i=1}^{l-1}\rho_i^2\right)
  $$
  
  Here we repalce the upper limit to $l-1$ because we assume $\rho_l$ decays with $l$ and if we assume $\rho_l =0$, we neglect other terms. This is a weaker form of the test. It underestimate the variance. It rejects more cases and the false negative error is lowered and thus the power is higher. 

- **Portmanteau test:** 

  $H_0:$  $\rho_1 = \dots = \rho_m = 0$. vs $H_1:$ $\rho_i \neq 0$ for some $i\in\{1,\dots,m\}$. 

  **Box-Pierce** : one of the portmanteau test. The statistic:
  $$
  Q^*(m) = T\sum_{i=1}^m \hat{\rho}_i^2
  $$
  If $x_t$ are iid with moment conditions then 
  $$
  Q^*(m) \rightarrow \chi^2(m) ,\quad \text{ as } T\rightarrow \infty
  $$
  
  **Ljung-Box:** The statistic:
  
  $$
  Q(m) = T(T+2) \sum_{i=1}^m \frac{\hat{\rho}^2_i}{T-i}
  $$
  
  This gives more weights to the small legs estimators because there are more samples in the small legs estimation. This imporved power in finite sample.

  The choice of $m$ would be $m\sim \log(T)$. 







