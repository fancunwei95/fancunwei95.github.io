---
title: Lecture 19 (March 07, 2022)
classes: wide
excerpt: "Construct statistical test for unit root from samples"
date: 2022-03-07

---


Recall, we want to test the unit root model. That is we have a model $x_t = \phi_1 x_{t-1} + \epsilon_t$ with $x_0 = 0$. We want to test $\phi_1 = 1$ v.s. $\phi_1<1$. The ordinary least square gives 

$$
\hat\phi_1 = \frac{\sum_{t=1}^T x_{t-1}x_t}{\sum_{t=1}^T x_{t-1}^2} = \phi_1 + \frac{\sum_{t=1}^Tx_{t-1} \epsilon_t}{\sum_{t=1}^Tx_{t-1}^2}
$$

we have seen that if $|\phi_1|<1$ then $\sqrt{T}(\hat\phi_1-\phi_1)\rightarrow N(0,1-\phi_1^2)$. The issue is as $\phi_1\rightarrow 1$, the limiting distribution is degenerate. Need a large scale factor than $\sqrt{T}$.  

Then we want to ask what is the right scaling factor and what is the resulting limitiing distribution? 

### Analysis of OLS:

We first notice that 

$$
x_t^2 = (x_{t-1}+\epsilon_t)^2 = x_{t-1}^2 + 2x_{t-1}\epsilon_t + \epsilon_t^2
$$

which gives the numerator of the OLS:

$$
\frac{1}{\sigma^2T} \sum_{t=1}^Tx_{t-1}\epsilon_t = \frac{1}{2T\sigma^2} \sum_{t=1}^T (x_t^2 -x_{t-1}^2-\epsilon_t^2) = \frac{1}{2T\sigma^2}x_T^2 - \frac{1}{2T\sigma^2}\sum_{t=1}^T \epsilon_t^2
$$

If we assume $\epsilon_t \sim N(0,\sigma^2)$.  then  $x_t$ is a discretized Brownian motion. In this case $x_T \sim N(0,\sigma^2T)$,  Since $x_1 = \epsilon_t$ and thus, 

$$
\left(\frac{x_T}{\sigma \sqrt{T}}\right)^2 \sim \epsilon_t^2\sim x_1^2
$$

The last part becomes 

$$
\frac{1}{2T}\sum_{t=1}^T\left(\frac{\epsilon_t}{\sigma}\right)^2\rightarrow \frac{1}{2}\mathbb{E}\left(\frac{\epsilon_t}{\sigma} \right)^2 = \frac{1}{2}
$$

This then shows that 

$$
\frac{1}{\sigma^2T}\sum_{t=1}^T x_{t-1}\epsilon_t \rightarrow \frac{1}{2}(x_1^2-1)
$$

functional central limit theorem gives that 

$$
\frac{1}{T^2}\sum_{t=1}^T x_{t-1}^2 \rightarrow \sigma^2\int_0^1 [w(r)]^2 dr
$$

Combining the above results, we have 

$$
T(\hat\phi_1-\phi_1) \rightarrow \frac{[w(1)^2-1]}{2\int_0^1[w(r)]^2 dr} \quad \text{ as } T\rightarrow \infty
$$

### Another test based on self-normalization

We can construct the t-ratio of $\hat{\phi}_1$ by 

$$
t = \frac{\hat\phi_1-1}{\text{std}(\hat\phi_1)} 
$$

under the null hypothesis that $\phi_1=1$. We thus need to find the standard deviation of the $\hat{\phi}_1$.  Given data $x_1, \dots, x_t$, we can see that 

$$

\text{Var}(\hat\phi_1) = \frac{\sum_{t=1}^T x_{t-1}^2\hat{\sigma}^2}{\left(\sum_{t=1}^T x_{t-1}^2\right)^2} = \frac{\hat{\sigma}^2}{\sum_{t=1}^T x_{t-1}^2}
$$

where $\hat\sigma^2$ is an estimate of $\text{Var}(\epsilon_t) = \sigma^2$.  Here, we used the fact that in the linear regression, we treat $x_{t-1}$ as given and $x_t$ as the label and thus the variance for $x_{t-1}$ does not come into play. We then use the MLE of $(\phi_1, \sigma^2)$ based on $\epsilon_t \sim N(0,\sigma^2)$ to estimate $\hat\sigma^2$.  In linear regression, we simply maximize the likelihood as 

$$
\log \prod_{t=1}^T \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[-\frac{(x_t-\phi_1x_{t-1}^2)}{2\sigma^2}\right] = - \frac{T}{2} \log \sigma^2 - \frac{1}{2\sigma^2} \sum_{t=1}^T(x_t-\phi_1x_{t-1})^2
$$

The estimator of $\sigma^2$ then becomes 

$$
\hat\sigma^2 = \frac{1}{T} \sum_{t=1}^T (x_t-\hat\phi_1 x_{t-1})^2
$$

thus, the t-ratio statsitics becomes 

$$
t = \frac{\hat\phi_1-1}{\sqrt{\hat\sigma^2/\sum_{t=1}^T x_{t-1}^2}} = \frac{\hat\phi_1-1}{\hat\sigma} \sqrt{\sum_{t=1}^Tx_{t-1}^2}
$$

Note that when $T(\hat\phi_1-\phi_1)\rightarrow $ non degenerate limiting distribution, $\hat\phi_1 \rightarrow \phi_1$ and $\hat\sigma^2\rightarrow \sigma^2$. Thus, the t ratio becomes 

$$
t = {T(\hat\phi_1 - 1)} \frac{1}{\hat\sigma} \sqrt{\frac{1}{T^2}\sum_{t=1}^T x_{t-1}^2} \rightarrow \frac{1}{\sigma} \frac{[w(1)^2-1]}{\int_0^1[w(r)]^2 dr} \left(\sigma^2\int_0^1[w(r)]^2 dr \right)^{1/2} = \frac{1/2 [w(1)^2-1]}{\{\int_0^1[w(r)]^2 dr\}^{1/2}}
$$

Remark: If $\epsilon_t$ are not iid noise, then we may model 

$$
x_t = c_t + \phi_1x_{t-1} + \sum_{i=1}^p \beta_i \Delta x_{t-i} + \epsilon_t
$$

where $c_t$ is a deterministic function of time $t$ and $\Delta x_t = x_t - x_{t-i}$. 


