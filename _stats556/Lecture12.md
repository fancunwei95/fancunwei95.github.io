---
title: Lecture 12 (Feb 18, 2022)
classes: wide
excerpt: "Non parametric estimation of spectral density (Kernel Method)"
date: 2022-02-18

---

There are some restrictons of the parametric estimation. Obviously, when the series does not follow the assumed model, the estimation would be off. 

### Nonparametric estimation

Our goal is to estimate spectram $s(\omega)$, which is the Fourier transform of $\gamma_j$. 

Idea: use smoothness of $s(\omega)$: continuity: $s(\lambda) \rightarrow s(\omega)$ as $\lambda \rightarrow \omega$. 

Local average with weights: (here the weights depend on the distance between $\omega$ and $\lambda$. )

Let $\omega_j = 2\pi j/T$. Kernel estimation for $s(\omega_j)$ :
$$
\tilde{S}(\omega_j) = \sum_{m=-h}^h K(\omega_{j+m}, \omega_j ) \hat{s}(\omega_{j+m})
$$
here the $h$ is the bandwidth. $2\hat{s}(\omega)/s(\omega) \rightarrow \chi^2_2$ and $\hat s(\omega)$ and $\hat s(\lambda)$ are asymptoticaly independent. Here we would let $h\rightarrow \infty$ as $T\rightarrow \infty$ and thus, we have a vanishing variance. Thus, we trade a small bias with a large reduce of variance. If $s(\omega)$ is less smoother, the average introduces a lot of bias. For rough $s(\omega)$, we need smaller $h$. We need some normalizatoin restriction on $k$ as 
$$
\sum_{m=-h}^h K(\omega_{j+m}, \omega_j) = 1
$$
A simple example is 
$$
K(\omega_{j+m}m \omega_j) = \frac{h+1 - |m| }{c(h)}
$$
The normalization $c(h) = (h+1)^2$. (linear decay with distance $m$)

If $h\rightarrow\infty$, the variance of $\tilde S$ vanishes. If $h=o(T)$, the bias is controlled. 

Another look at the kernel method. We do this by using the continuous spectrum although this is not the case in reall application. 
$$
\tilde{s}(\omega) = \frac{1}{2\nu}\int_{\omega-\nu}^{\omega+\nu} \hat{s}(\lambda)d\lambda 
$$
where we used a uniform kernel with band width $\nu$. Recall that 
$$
\begin{aligned}
\hat{s}(\lambda) &= \frac{1}{2\pi} \sum_{j=-T+1}^{T-1} \hat{\gamma}_j e^{-i\lambda j} \\
&=\frac{1}{2\pi} \left[\hat\gamma_0+2\sum_{j=1}^{T-1} \hat\gamma_j \cos(\lambda j)\right]
\end{aligned}
$$
thus, 
$$
\begin{aligned}
\tilde S(\omega) &= \frac{1}{4\pi \nu} \int_{\omega-\nu}^{\omega+\nu} \left(\hat\gamma_0 ++2\sum_{j=1}^{T-1} \hat\gamma_j \cos(\lambda j) \right) d\lambda\\
&=\frac{1}{4\pi\nu} \left[\hat\gamma_0(2\nu) + 2\sum_{j=1}^{T-1} \hat\gamma_j \int_{\omega-\nu}^{\omega+\nu}\cos(\lambda j) d\lambda \right] \\
&= \frac{1}{2\pi}\hat\gamma_0 + \frac{1}{2\pi \nu} \sum_{j=1}^{T-1} \frac{\hat\gamma_j}{j}\left[\sin((\omega+\nu) j) - \sin((\omega-\nu) j)\right]\\
&= \frac{1}{2\pi}\left[\hat\gamma_0 + 2\sum_{j=1}^{T-1} \frac{\sin(\nu j)}{\nu j} \hat\gamma_j\cos(\omega j)\right]
\end{aligned}
$$
The periodogram is 
$$
\hat S(\omega) = \frac{1}{2\pi}\left[\hat\gamma_0 + 2\sum_{j=1}^{T-1} \hat\gamma_j\cos(\omega j)\right]
$$
Thus, the kernel method is a weighted average with weights $\sin(\nu j)/\nu j$ for $\hat\gamma_j$ for lag $j$. 

In the limiting case that $\nu\rightarrow 0$, then $\sin(\nu j)/\nu j \rightarrow 1$ and this reduces to the simple periodogram. 

Connection: 

kernel $K(\omega_{j+m},\omega_j)$ becomes weights for $\hat\gamma_j$ and we call this weight $\kappa_j^*$.

The Bartlett kernel is 
$$
\kappa_j^* = \left\{ \begin{aligned} 
&1 - \frac{j}{q+1} , \quad j= 1,\dots,q\\
&0, \quad j>q
\end{aligned}\right.
$$
 This shows 
$$
\tilde{S}(\omega) = \frac{1}{2\pi}\left[\hat\gamma_0 + 2 \sum_{j=1}^q \left(1-\frac{j}{1+q} \right)\gamma_j \cos(\omega j)\right]
$$
Summary: bias increases as $q$ become larger and variance decreasess. The bias depends on the smoothness of $S(\omega)$. 

i.e. more smoothness $\Rightarrow$ can have larger h or q​.  less smoothness $\Rightarrow$ need to have small $h$ or $q$.

More on Kernel regression :

If we have sample $x_1,\dots x_T$ and $f(x)$. Then we want to esimate $\hat{f}(x)$ by 
$$
\hat f (x) = \arg\min_{c} \sum_{t=-h}^h K(x,x_t) (c-f(x))^2
$$
Take derivative and get 
$$
\hat f(x) = \frac{1}{\sum_{t=-h}^h K(x,x_t)} \sum_{t=-h}^h K(x,x_t)f(x_t)
$$
we can replace $c$ by some function. 


