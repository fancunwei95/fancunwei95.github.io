---
title: Lecture 20 (March 09, 2022)
classes: wide
excerpt: "Random Walk with Drift term and statistical test for non-zero drift"
date: 2022-03-09

---

### Random walk with constant drift. 

$x_t = \alpha+x_{t-1} + \epsilon_t$. 

we would like to design a statistical test for $\alpha\neq 0$ and the unit root $\phi_1 =1$. We have observed data $x_1,x_2,\dots, x_T$. and we want to test the process $x_t = \alpha + \phi_1x_{t-1} + \epsilon_t$ with null that $\alpha =0 $ and $\phi_1<1$. 

In this case, we would have $x_t = \alpha t + \sum_{i=1}^t \epsilon_t$ by the recursion if we assume $x_0 = 0$. Notice that the first term is of $O(t)$ and the second term is of order $O(\sqrt{t})$. 

If we do the OLS then we minimize 

$$
\min_{\alpha,\phi_1}  \sum_{t=1}^T (x_t-\alpha-\phi_1x_{t-1})^2
$$

have estimates $\hat\alpha$ and $\hat\phi_1$. The esimator looks like 

$$
\begin{pmatrix}
\hat\alpha \\ \hat\phi_1
\end{pmatrix} = \begin{pmatrix} T & \sum_{t=1}^T x_{t-1} \\\sum_{t=1}^T x_{t-1} & \sum_{t=1}^T x_{t-1}^2  \end{pmatrix}^{-1} \begin{pmatrix} \sum_{t=1}^T x_t \\ \sum_{t=1}^T x_{t-1}x_t\end{pmatrix}
$$

We take the inverse and plugin the model for $x_t$, we have 

$$
\begin{pmatrix}
\hat\alpha \\\hat\phi_1\end{pmatrix} = \frac{1}{T \sum x_{t-1}^2 - (\sum x_{t-1})^2} 
\begin{pmatrix}
\sum x_{t-1}^2 & - \sum x_{t-1}  \\
 -\sum x_{t-1}& T
\end{pmatrix}
\begin{pmatrix}
\alpha T + \sum x_{t-1} + \sum \epsilon_t \\
\sum \alpha x_{t-1} + \sum x_{t-1}^2 + \sum x_{t-1}\epsilon_t
\end{pmatrix}
$$

By some algebra, we find that 

$$
\begin{pmatrix}
\hat\alpha \\ \hat\phi_1 
\end{pmatrix} = \begin{pmatrix} \alpha \\ 1 \end{pmatrix} + \frac{1}{T\sum x_{t-1}^2 - (\sum x_{t-1})^2} \begin{pmatrix}\sum x_{t-1}^2  &- \sum x_{t-1} \\ -\sum x_{t-1} & T \end{pmatrix} \begin{pmatrix} \sum \epsilon_t \\ \sum x_{t-1} \epsilon_t \end{pmatrix}
$$

the behaviour of the error term ( the second part of the above equation)

first $\sum_{t=1}^T x_{t-1} = \sum_{t=1}^T \left(\alpha (t-1) + \sum_{i=1}^{t-1} \epsilon_i\right) = O(T^2) + O(T^{3/2})$.  From functional CLT, we expect that the second term behaves like:

$$
T^{-3/2} \sum_{t=1}^T \xi_t \rightarrow \sigma \int_0^1 W(r)dr
$$

where $\xi_t = \sum_{i=1}^t \epsilon_i$. 

And by dividing $T^2$, only the first term $\sum_{t=1}^T \alpha (t-1)$ survives in $T\rightarrow \infty$ limit and thus

$$
\frac{1}{T^2} \sum_{t=1}^T x_{t-1} = \left[O(T^2) + O(T^{3/2}) \right] T^{-2} \rightarrow \frac{\alpha}{2}
$$

The second part 

$$
\sum_{t=1}^T x_{t-1}^2 = \sum_{t=1}^T [\alpha(t-1) +\xi_t]^2 
$$

by similar arguments, we have 

$$
\frac{1}{T^3} \sum_{t=1}^Tx_{t-1}^2 \rightarrow \alpha^2/3
$$

From the above calculation, and additional analysis, we find the correct scaling for the error term is 

$$
\begin{pmatrix}\hat\alpha - \alpha \\ \hat\phi_1 - 1\end{pmatrix} \sim \begin{pmatrix}
T^{-1/2} \\T^{-3/2}
\end{pmatrix}
$$

Then, we could calculate the scaled error as  

$$
\begin{pmatrix}
T^{1/2} & 0 \\ 0 & T^{3/2} 
\end{pmatrix}\begin{pmatrix}\hat\alpha - \alpha \\ \hat\phi_1-1 \end{pmatrix}
$$

This can be calculated as 

$$
\begin{pmatrix}T^{1/2} & 0 \\ 0 & T^{3/2} \end{pmatrix} \begin{pmatrix} T & \sum x_{t-1} \\ \sum x_{t-1} & \sum x_{t-1}^2 \end{pmatrix}^{-1} \begin{pmatrix}T^{1/2} & 0 \\ 0 & T^{3/2} \end{pmatrix}\begin{pmatrix}T^{-1/2} & 0 \\ 0 & T^{-3/2} \end{pmatrix} \begin{pmatrix} \sum \epsilon_t \\ x_{t-1}\epsilon_t\end{pmatrix}
$$

The result is 

$$
\begin{pmatrix}
1 & \frac{1}{T^2}\sum x_{t-1} \\ \frac{1}{T^2}\sum x_{t-1} & \frac{1}{T^3} \sum x_{t-1}^2
\end{pmatrix}^{-1} \begin{pmatrix} \frac{1}{\sqrt{T}} \sum \epsilon_t \\ \frac{1}{T^{3/2}} \sum x_{t-1} \epsilon_t \end{pmatrix} \rightarrow \begin{pmatrix}1 & \frac{\alpha}{2}\\ \frac{\alpha}{2} & \frac{\alpha^2}{3} \end{pmatrix}^{-1} \begin{pmatrix} \frac{1}{\sqrt{T}} \sum \epsilon_t \\ \frac{1}{T^{3/2}} \sum x_{t-1} \epsilon_t \end{pmatrix} 
$$

where the matrix is invertible for $\alpha \neq 0$ because it is positive definite for $\alpha \neq 0$. 

