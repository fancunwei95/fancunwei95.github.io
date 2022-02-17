---
title: Lecture 06 (Feb 04, 2022)
classes: wide
excerpt: "Introduction to PACF and Information criteria (AIC, BIC)"
date: 2022-02-04
---


The asymptotic statsistics can be used to do the order selection of $AR(p)$. 

### partial autocorrelation function (PACF)

we first list possible AR models

- AR(1) $x_t = \phi_{0,1} + \phi_{1,1} x_{t-1} + \epsilon_{1,t} $ 

- AR(2) $x_t =\phi_{0,2} + \phi_{1,2} x_{t-1} + \phi_{2,2} x_{t-2} + \epsilon_{2,t}$
-  $\vdots$
- AR(p) $x_{t} = \phi_{0,p} + \phi_{1,p} x_{t-1} + \dots +\phi_{p,p}x_{t-p} + \epsilon_{p,t}$

the sample estimated $\hat{\phi}_j$ is the lag-$j$ sample PACF. 

For a stationary AR(p) model:

- $\hat{\phi}_{p,p}\rightarrow \phi_{p,p}$ as $T\rightarrow \infty$
- $\hat{\phi}_{p,l}\rightarrow 0$ for $l>p$ as $T\rightarrow\infty$. 
- $\text{Var}{\hat{\phi}_{l,l}} \sim \frac{1}{T}$  

For an AR(p) model, the sample PACF cuts off at lag $p$. 

### Information criteria (based on likelihood)

A large model will tend to maximize the likelihood with more parameters. Therefore, need to penalize the number of parameters in a given model. 

Guassian AR(p) model $x_t = \phi_1 x_{t-1} + \dots + \phi_p x_{t-p} + \epsilon_t$ with $\epsilon_t\sim \mathcal{N}(0,\sigma^2)$. 

$$
\begin{aligned}
&L(\phi_1,\dots, \phi_p ,\sigma^2 | x_1,\dots,x_T) \\
&= p(x_1,\dots, x_T|\phi_1,\dots,\phi_p,\sigma^2) \\
&= p(x_T|x_{T-1},\dots, x_{T-p}) p(X_{T-1} | x_{T-2},\dots, x_{T-p-1}) \dots p(x_{p+1}|x_p,\dots ,x_1)p(x_p,\dots, x_1)\\
&=\prod_{t=p+1}^T \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x_t-\sum_{j=1}^p \phi_jx_{t-j})^2}{2\sigma^2}\right) p(x_p,\dots, x_1)
\end{aligned}
$$

Thus the log likelihood becomes 

$$
l = - \frac{T-p}{2} \log(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{t=p+1}^T (x_t-M_t\phi)^2
$$

This is the **conditional log likelihood** which means for the last $p(x_p,\dots, x_1)$ doest not come into the calculation and we implicitly assume they are fixed at the sample value. 

The maximize of conditional log likelihood is the same as the least square. for $\sigma^2$ 

$$
\hat{\sigma}^2 = \frac{1}{T-p} \sum_{t=p+1}^T (x_t - M_t \hat{\phi})^2
$$

Thus, the log likelihood becomes 

$$
l(\hat{\phi}, \hat{\sigma^2}) = -\frac{T-p}{2} \log(2\pi \hat{\sigma^2}) - \frac{T-p}{2}
$$

When $p\ll T$ we have 

$$
-\frac{2}{T} l (\hat\phi, \hat{\sigma^2}) \sim \log(2\pi e) + \log(\hat{\sigma^2})
$$

Thus, the only part that depends on the data is the second term. Now information criterion comes into play: add penalty to the log likelihood

$$
IC = - \frac{2}{T} l (\hat{\phi},\hat{\sigma^2}) + \text{complexity of the model}
$$

avoid overfitting. 

### Akaike inforation criterion for AR(p):

$AIC = \log(\hat{\sigma^2}) + \frac{2}{T} \text{number of parameters}$

### Bayesian information criterion :

$BIC = \log(\hat{\sigma^2}) + \frac{p}{T}\log(T)$. 
