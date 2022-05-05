---
title: Lecture 16 (Feb 28, 2022)
classes: wide
excerpt: "Introduction to Generalized ARCH and model estimation and forecast"
date: 2022-02-28

---

Model checking:

for the residual, we could standardize it $\tilde{r}_t = r_t/\sigma_t$ and we do Ljung Box test on $\tilde{r}_t$ and $\tilde{r}_t^2$. 

Since $\sigma_t^2 = \alpha_0 + \alpha_1 r_{t-1}^2 + \dots + \alpha_p r_{t-p}^2$  and since $\mathbb{E}[r_t|\mathcal{F}_{t-1}] = \sigma_t^2$ we could approximately write 

$$
r_t^2 = \alpha_0 + \alpha_1 r_{t-1}^2+\dots \alpha_pr_{t-p}^2
$$

and we could use PACF to determine the order $p$. 

### Generalized ARCH 

Input : $x_t$ and model $r_t = x_t - \mathbb{E}[x_t|\mathcal{F}_{t-1}]$ and $r_t = \sigma_t \epsilon_t$ with $\epsilon_t$ iid. 

The generalized ARCH models the conditional variance as 

$$
\sigma_t^2 = \alpha_0 + \sum_{i=1}^p \alpha_i r_{t-i}^2 + \sum_{j=1}^q \beta_j \sigma_{t-j}^2
$$

The variance of $r_t$ is 

$$
\text{Var}[r_t^2] = \mathbb{E}[\sigma_t^2] = \alpha_0 + \sum_{i=1}^p \alpha_i \mathbb{E}[r_{t-i}^2] + \sum_{j=1}^q \beta_j \mathbb{E}[\sigma_{t-j}^2] 
$$

Thus, we have 

$$
\text{Var}[r_t] = \frac{\alpha_0}{1-\sum_{i=1}^p \alpha_i -\sum_{j=1}^q \beta_j}
$$

Therefore we need $\sum_{i=1}^p \alpha_i + \sum_{j=1}^q \beta_j < 1$ 

if we define $\eta_t = r_t^2-\sigma_t^2$. Then, we could write 

$$
\begin{aligned}
r_t^2 &= \eta_t + \sigma_t^2 = \eta_t + \alpha_0 + \sum_{i=1}^p \alpha_i r_{t-i}^2 + \sum_{j=1}^q \beta_j (\sigma_{t-j}^2 - r_{t-j}^2 + r_{t-j}^2) \\
&= \eta_t + \alpha_0 + \sum_{i=1}^{p\vee q} (\alpha_i + \beta_i) r_{t-i}^2 - \sum_{j=1}^q \beta_j\eta_{t-j}
\end{aligned}
$$

which is in the ARMA form but the error $\eta$ is not independent. 

The error sequence has mean zero 

$$
\mathbb{E}[\eta_t] = \mathbb{E}[r_t^2] - \mathbb{E}[\eta_t^2] = 0
$$

Then 

$$
\begin{aligned}
\mathbb{E}[\eta_t\eta_{t-j}] &= \mathbb{E}[\mathbb{E}[(r_t^2-\sigma_t^2)(r_{t-j}^2-\sigma_{t-j}^2)|\mathcal{F}_{t-1}]] \\
&= \mathbb{E}[\sigma_t^2\sigma_{t-j}^2(\epsilon_{t-j}^2-1)\mathbb{E}[\epsilon_t^2-1]] = 0
\end{aligned}
$$

Example: GARCH(1,1) model. 

$$
\sigma_t^2 = \alpha_0 + \alpha_1r_{t-1}^2 + \beta_1\sigma_{t-1}^2 
$$

The unconditional Kurtosis is then K

$$
K = \frac{\mathbb{E}r^4_t}{\mathbb{E}[r_{t}^2]^2} = \frac{3[1-(\alpha_1+\beta_1)^2]}{1 - (\alpha_1+\beta_1)^2 -2 \alpha_1^2} > 3
$$

provided that $(\alpha_1+\beta_1)^2+2\alpha_1^2 < 1$. Thus, the tail distribution of GARCH(1,1) residuals is heavier than that of the $\mathcal{N}(0,1)$. 

### Forecast: 

$1$ step ahead prediction of $\sigma_t^2$ :

$$
\widehat{\sigma_{t+1}^2} = \mathbb{E}[\sigma_{t+1}^2| \mathcal{F}_t] = \alpha_0 + \alpha_1 r_{t}^2 + \beta_1 \sigma_{t}^2
$$

Note: 

$$
\sigma_{t+1}^2 = \alpha_0 + (\alpha_1+\beta_1) \sigma_t^2 + \alpha_1(r_t^2-\sigma_t^2)
$$

Thus, 

$$
\sigma_{t+2}^2 = \alpha_0 + (\alpha_1 + \beta_1)\sigma_{t+1}^2 + \alpha_1(\epsilon_{t+1}^2-1)\sigma_{t+1}^2
$$

and we could recurse to get 

$$
\widehat{\sigma_{t+2}^2} = \alpha_0 + (\alpha_1+\beta_1)\mathbb{E}[\sigma_{t+1}^2|
\mathcal{F}_t] = \alpha_0 + (\alpha_1+\beta_1)\widehat{\sigma_{t+1}^2}
$$

which forms a recursion for forecast. This exponential structure shows the mean reverting behaviour and the variance converge to the uncoditional variance $\mathbb{E}[r_t^2]$. 



