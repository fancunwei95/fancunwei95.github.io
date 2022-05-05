---
title: Lecture 18 (March 04, 2022)
classes: wide
excerpt: "Introduction to unit root models"
date: 2022-03-04

---

### unit root nonstationary models

Example of unit root process is random walk $x_t$. $x_t = x_{t-1} + \epsilon_t$. where $\epsilon_t$ is iid with mean zero and variance $\sigma^2$. This is the root $=1$ autoregressive model. 

$x_t$ is unit root non-stationary time series. The series is non stationary is because 

$$
x_t = x_{t-1} + \epsilon_t = \sum_{i=1}^t \epsilon_t 
$$

and thus, the variance of $x_t$ is $t\sigma^2$ which is not a constant across $t$ and thus the process is non-stationary. 

The one step ahead prediction is 

$$
\hat{x}_{t+1} = \mathbb{E}[x_{t+1}|x_t,x_{t-1},\dots] = \mathbb{E}[x_t + \epsilon_{t+1}|x_{t},\dots] = x_t
$$

and two step ahead prediction will be 

$$
\hat{x}_{t+2} = \mathbb{E}[x_t+\epsilon_{t+1}+\epsilon_{t+2}|x_t, x_{t-1},\dots] = x_t
$$

and thus, for any horizon, the prediction will be $x_t$. 

It is also possible the noise has some non-random structure, like ARMA noise. then we define $r_t = x_t - x_{t-1}$. Then we say the process $x_t$ is ARIMA$(p,1,q)$ model. A good example is that the log return is the difference between $\log p_t$ and $\log p_{t-1}$. If we model the log return as ARMA, then the log price series satisfies ARIMA model. 

Idea: differencing transforms non-stationarity time series to stationary series. 

order 1: $r_t = x_t - x_{t-1}$. 

order 2: if $r_t$ is still unit-root, then  we take another differencing $s_t = r_t -r_{t-1}$.

The next question is how do we know whether there is a unit root in the series. 

Model: $x_t = \phi_1 x_{t-1} + \epsilon_t$ where $\epsilon_t$ are iid errors. 

Hypothesis testing:

$H_0 : \phi_1 =1 $ versus $H_1: \phi_1<1$. 

We first take least squares for the regression and get $\hat{\phi}_1 = \arg\min \sum_t (x_t - \theta x_{t-1})^2$. 

We find that 

$$
\begin{aligned}
\hat{\phi}_1 &= \frac{\sum x_{t-1}x_t}{\sum x_{t-1}^2} = \frac{\sum x_{t-1}(\phi_1 x_{t-1}+\epsilon_t)}{\sum x_{t-1}^2} \\
&= \phi_1 + \frac{\sum_{t=1}^T x_{t-1}\epsilon_t}{\sum x^2_{t-1}}
\end{aligned}
$$

The expectation of this estimator is $\phi_1$. We then consider the aympototic behaviour as 

$$
\sqrt{T}(\hat{\phi}_1 - \phi_1) = \frac{\frac{1}{\sqrt{T}}\sum_{t=1}^T x_{t-1}\epsilon_t}{\frac{1}{T}\sum_{t=1}^Tx_{t-1}^2}
$$

The numerator is asymptotic as $\mathcal{N}(0, \sigma^2\gamma_0)$ where $\gamma_0$ is the zero lag covariance. The denominator $\mathbb{E}[x_{t-1}^2] = \gamma_0$.  Thus, Slutsky says 

$$
\sqrt{T}(\hat\phi_1 - \phi_1) \rightarrow \mathcal{N}(0, \frac{\sigma^2}{\gamma_0}) = \mathcal{N}(0, 1-\phi_1^2)
$$

and when $\phi_1\rightarrow 1$, the variance seems vanishing. Under the null hypothesis, however, we have 

$$
\hat\phi_1 = \phi_1 + \frac{\sum_{t=1}^T x_{t-1}\epsilon_t}{ \sum_{t=1}^T x_{t-1}^2}
$$

and 

$$
x_t = (x_{t-1}+\epsilon_t)^2 = x_{t-1}^2 + 2 x_{t-1}\epsilon_t + \epsilon_t^2
$$

However, we find that 

$$
\sum_{t=1}^T x_{t-1}\epsilon_t = \frac{1}{2} \sum_{t=1}^T (x_t^2-x_{t-1}^2) - \frac{1}{2}\sum_{t=1}^T \epsilon_t^2
$$

The telescope sum the first part gives that 

$$
\frac{1}{2} x_T^2 - \frac{1}{2}\sum_{t=1}^T \epsilon_t^2 = \sum_{t=1}^T x_{t-1}\epsilon_t
$$
