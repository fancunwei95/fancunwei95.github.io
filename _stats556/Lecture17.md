---
title: Lecture 17 (March 02, 2022)
classes: wide
excerpt: "Introduction to Non-linear Models including TAR ans SETAR"
date: 2022-03-02

---

In the GARCH(1,1) model, 

$$
\sigma_{t+1}^2 = \alpha_0 + \alpha_1 r_t^2 + \beta_1\sigma_{t}^2
$$

and the one step forecast will be 

$$
\sigma_{t,1}^2 = \alpha_0 + \alpha_1r_t^2 + \beta_1\sigma_t^2
$$

and two step forecast will be 

$$
\sigma_{t+2}^2 = \alpha_0 + (\alpha_1+\beta_1) \sigma_{t+1}^2+\alpha_1\sigma_{t+1}^2(\epsilon_{t+1}^2 -1) = \alpha_0+ (\alpha_1+\beta_1)\widehat{\sigma_{t,1}^2}
$$

Recursively, we have 

$$
\begin{aligned}
\widehat{\sigma_{t,l}^2} &= \alpha_0 + (\alpha_1 + \beta_1) \widehat{\sigma_{t,l-1}^2} \\
&= \alpha_0 \frac{1-(\alpha_1+\beta_1)^{l-1}}{1-(\alpha_1+\beta_1)} + (\alpha_1+\beta_1) \widehat{\sigma_{t,1}^2}
\end{aligned}
$$

as $l\rightarrow \infty$, 

$$
\widehat{\sigma_{t,l}^2} \rightarrow \frac{\alpha_0}{1-(\alpha_1+\beta_1)} = \mathbb{E}[r_t^2]
$$

### Nonlinear time series:

The general form is 
$$
x_t = f(\epsilon_t, \epsilon_{t-1},\dots)
$$

where $\epsilon_t$ iid. This is the Bernoulli shift process. 

The form is too general. Define $\mathcal{F}_t = \sigma(\epsilon_t, \epsilon_{t-1},\dots)$ , then define 

$$
\mu_t = \mathbb{E}[x_t|\mathcal{F}_{t-1}] = g(\mathcal{F}_{t-1})
$$
we can also define 

$$
\sigma_t^2 = \text{Var}[x_t|\mathcal{F}_{t-1}] = h(\mathcal{F}_{t-1})
$$

Then, we are interested in the time series that is of the form:

$$
x_t = g(\mathcal{F}_{t-1}) + h(\mathcal{F}_{t-1}) \epsilon_t
$$

This include ARMA, ARCH, GARCH. 

If $x_t$ is weakly stationary with zero mean, then we can write $x_t$ as 

$$
x_t = \sum_{i=0}^\infty \psi_i \gamma_t 
$$

where $\gamma_t$ are uncorrelated but dependent. This is called the Wold decomposition. (time domain decomposition, corresponding to the frequency domain decomposition)

### Threshold AR(TAR) model:

THe model is 
$$
	x_t = \phi^{(j)}_0 + \phi^{(j)}_1 x_{t-1} + \dots + \phi^{(j)}_p x_{t-p} + \epsilon_t
$$
with $j = 1,\dots, k$ regimes if $r_{j-1}\leq x_{t-d} < r_j $ 

Issue : $\mu_t = \mathbb{E}(x_t | \mathcal{F}_{t-1})$ is not a continuous function at the boundaries $(r_t)_{1}^k$. 

For example 

$$
x_t = \left\{
\begin{aligned}
&-1.5x_{t-1} + \epsilon_t \quad x_{t-1}<1  \\
&0.5x_{t-1} + \epsilon_t \quad x_{t-1}\geq 1
\end{aligned}
\right.
$$

Thus, the conditional mean is 

$$
\begin{aligned}
\mu_t &= \mathbb{E}[(-1.5 x_{t-1} + \epsilon_t) I(x_{t-1}<1) + (0.5 x_{t-1}+\epsilon_t)I(x_{t-1}\geq 1) | \mathcal{F}_{t-1}] \\
&= -1.5 x_{t-1} I(x_{t-1} < 1) + 0.5 x_{t-1} I(x_{t-1}\geq 1)
\end{aligned}
$$

at $x_{t-1} = 1$, the exepcted mean jumps from -1.5 to 0.5 and makes the estimation at the boundary really hard. 

In order to address the issue, we could add some smoothness in the jump and we introduce the STAR(smoothe TAR) model. 

k-regime SETAR model:

$$
x_t = \phi_0^{(i)} + \phi_1^{(j)} x_{t-1} + \dots + \phi^{(p)} x_{t-p} + \epsilon_t
$$
and STAR model:
$$
x_t = \epsilon_t + \left(c_0 + \sum_{i=1}^p\phi_{0,i} \epsilon_{t-i} \right)
$$

as the baseline model, then we add transition

$$
x_t = \epsilon_t + \left(c_0 +\sum_{i=1}^p \phi_{0,j} \epsilon_{t-i}\right) + K\left(\frac{x_{t-d-\Delta}}{s}\right) \left(c_1 + \sum_{i=1}^p \phi_{j,1} \epsilon_{t-j}\right)
$$

and $d$ is the delay parameter, and $\Delta$ is the model transition parameter. $s$ is the scale parameter and $K$ is the kernel. This is the $k=2$ example. 



