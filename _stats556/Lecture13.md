---
title: Lecture 13 (Feb 21, 2022)
classes: wide
excerpt: "Introduction to Conditional Variance"
date: 2022-02-21

---



Recall $AR(p)$ model: $x_t = \phi_0 + \phi_1 x_{t-1} + \dots + \phi_n x_{t-n} + r_t$. s.t. that $E[r_t] = 0$ the residual series $r_t$ is iid and the uncoditional variance $\text{Var}(r_t) = \sigma^2$ is a constant. However, the conditional variance may not be a constant. 

conditional variance of $r_t$ can change over time 
$$
r_t^2 = \alpha_0 + \alpha_1r_{t-1}^2 + \alpha_p r_{t-p}^2 + u_t
$$
where $u_t$ is an error process such that $\mathbb{E}[u_t]=0$ and the variance $\text{Var}[u_t] = \tau^2$ and may not be iid. and we expect the error process is uncorrelated $\mathbb{E}u_tu_s=0$ . 

If $Y = f(x) + \epsilon$ , the optimal prediction $\hat{y} = \hat f(x) = \mathbb{E}[Y|x]$, which is a solution that minimize 
$$
\hat f = \min_g \mathbb{E}[Y- g(x)]^2
$$
Thus, the  conditional estimation for $r_t^2$ is 
$$
\mathbb{E}[r_t^2|r_{t-1}^2,r_{t-2}^2,\dots ] = \alpha_0 + \alpha_1 r_{t-1}^2 + \dots + \alpha_p r_{t-p}^2 + \mathbb{E}[u_t|r_{t-1},\dots]
$$
Alternatively, we may reparameterize as (**The Arch Model**)
$$
r_t = \sigma_t \epsilon_t , \quad \text{where }\sigma_t^2 = \alpha_0 + \alpha_t r_{t-1}^2 + \dots + \alpha_pr_{t-p}^2
$$
The two models are equavalent is because 
$$
\mathbb{E} [ r_t^2 | r_{t-1}^2,r_{t-2}^2,\dots] = \sigma_t^2 \mathbb{E}[\epsilon_t^2|r_{t-1}^2,r_{t-2}^2,\dots ] = \sigma_t^2 \text{Var}[\epsilon_t^2] = \sigma_t^2
$$
moreover, the two models are equivalent , 
$$
r_t^2 = \sigma_t^2\epsilon_t^2 = \sigma_t^2 + u_t
$$
This shows $u_t = \sigma_t^2(\epsilon_t^2 -1)$. If we denote the $\mathcal{F}_t$ as the filteration of information, then 
$$
\mathbb{E}[u_t] =\mathbb{E}\mathbb{E}[\sigma_t^2(\epsilon_t^2-1)|\mathcal F_{t-1}] = \mathbb{E}[\sigma_t^2\mathbb{E}[\epsilon_t^2-1]] = 0
$$
The autocrrelation between $r_t$ and $r_{t-l}$ , then 
$$
\mathbb{E}[r_tr_{t-l}] = \mathbb{E} \mathbb{E} [\sigma_t\epsilon_{t}\epsilon_{t-l}\sigma_{t-l}| \mathcal{F}_{t-1}] = \mathbb{E}[\sigma_t\sigma_{t-l} \epsilon_{t-l} \mathbb{E}[\epsilon_t | \mathcal{F}_{t-1}]] = 0
$$

